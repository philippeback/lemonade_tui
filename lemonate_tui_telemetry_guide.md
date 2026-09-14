# Lemonade Server Telemetry, Inference Analytics & TUI Guide

This guide provides a comprehensive technical reference for inspecting, analyzing, and benchmarking Large Language Model (LLM) inference using the **Lemonade Server** telemetry log stream and the **`lemonade_tui.py`** Terminal User Interface (TUI).

---

## 1. Executive Summary & Architectural Overview

When serving large generative models—such as `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`—measuring aggregate token rates alone is insufficient for engineering production systems. Hardware-accelerated engines like Lemonade Server execute inference in distinct asynchronous stages with specialized optimizations:

1. **Scheduling & Slot Dispatch:** Queue latency from HTTP ingress (`POST /api/v1/chat/completions`) to worker allocation.
2. **Prefill Phase (Prompt Processing):** Compute-heavy ingestion of prompt context, establishing Key-Value (KV) cache entries and determining **Time To First Token (TTFT)**.
3. **Decode Phase (Autoregressive Token Generation):** Memory-bandwidth-bound sequential token generation, accelerated via **Multi-Token Prediction (MTP) / Speculative Decoding**.
4. **Kernel Graph Execution:** Reusing static computation graphs (e.g. CUDA Graphs) to eliminate repeated kernel launch overhead.
5. **Context Memory Retention:** Preserving KV cache state in slot memory for subsequent conversation turns.

```
 [ HTTP Ingress ] ──► [ Queue Delay ] ──► [ Slot Allocation (id 0) ]
                                                   │
                                                   ▼
                                       [ Prefill / Prompt Processing ]
                                       - Progressive Token Chunking
                                       - Time To First Token (TTFT)
                                                   │
                                                   ▼
                                       [ Decode / Token Generation ]
                                       - Autoregressive Loop
                                       - Speculative MTP Verification
                                       - Rolling Speed (tg_3s) Tracking
                                                   │
                                                   ▼
                                       [ Slot Release & Telemetry ]
                                       - Context Retention (KV Cache)
                                       - Graph Cache Reuse Counters
```

---

## 2. Deep-Dive Telemetry Breakdown from `lemonade-sample.log`

The following metrics are derived directly from the execution traces of **Task #5376** (long prompt) and **Task #6337** (short prompt) on `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`:

### Comparative Task Matrix

| Metric Dimension | Indicator | Task #5376 (Long Prompt) | Task #6337 (Short Prompt) | Architectural Significance |
|---|---|---|---|---|
| **Dispatch** | Queue Delay | `5.99 s` | `72.56 s` | Time waiting in server queue before slot dispatch |
| **Prefill (Input)** | Prompt Tokens | `13,445` tokens (87.3%) | `1,456` tokens (48.0%) | Inbound context footprint |
| **Prefill (Speed)** | Prompt Speed | **`417.33 t/s`** | **`225.04 t/s`** | Overall prompt ingestion throughput |
| **Prefill (Latency)**| Time To First Token | **`32.22 s`** (`2.40 ms/tok`) | **`6.47 s`** (`4.44 ms/tok`) | Interactive user wait time before output starts |
| **Decode (Output)** | Generated Tokens | `1,955` tokens (12.7%) | `1,577` tokens (52.0%) | Model completion length |
| **Decode (Speed)** | Steady-State TPS | **`65.41 t/s`** (`15.29 ms/tok`) | **`61.96 t/s`** (`16.14 ms/tok`) | Autoregressive streaming throughput |
| **Decode (Jitter)** | Rolling 3s Range | `59.23` – `69.95 t/s` | `52.56` – `73.74 t/s` | Instantaneous variation due to speculative hits |
| **Speculative MTP** | Draft Acceptance Rate | **`67.23%`** (`1307/1944`) | **`63.36%`** (`1034/1632`) | Multi-Token Prediction verification hit rate |
| **Speculative MTP** | Mean Speculative Len | **`3.02`** tokens / step | **`2.90`** tokens / step | **~3.0x speedup** over non-speculative decode |
| **End-to-End** | Total Wall Time | `62.09 s` | `31.91 s` | Total slot processing duration |
| **End-to-End** | Pipeline Throughput | **`248.03 t/s`** (15.4k tok) | **`95.06 t/s`** (3.0k tok) | Blended prompt + generation throughput |
| **Context & Cache** | Graph Reuse Count | `6,849` executions | `7,386` executions | Static computation graph cache hits |
| **Context & Cache** | Slot Active Tokens | `15,400` tokens | `16,017` tokens | Active KV cache footprint; Truncated = `0` |

---

## 3. The Four Core Dimensions of Inference Telemetry

### Dimension 1: Speed & Latency Dynamics

#### 1. Prefill Scaling & Attention Slowdown
As context expands, self-attention scales quadratically ($O(N^2)$) or linearly with chunked attention. Lemonade Server prints intermediate timing heartbeats during prompt evaluation:

```
Task #5376 Prefill Progression:
  Step 1:  4,096 tokens (30.0%) in  5.03s -> 813.54 tokens/sec
  Step 2:  6,144 tokens (46.0%) in  8.96s -> 685.70 tokens/sec
  Step 3:  8,192 tokens (61.0%) in 13.69s -> 598.19 tokens/sec
  Step 4: 10,240 tokens (76.0%) in 18.89s -> 542.19 tokens/sec
  Step 5: 12,288 tokens (91.0%) in 24.79s -> 495.61 tokens/sec
  Step 6: 12,929 tokens (96.0%) in 28.31s -> 456.76 tokens/sec
  Step 7: 13,441 tokens (100.0%) in 29.76s -> 451.62 tokens/sec
```
* **Observation:** Ingestion throughput drops from **813.5 t/s** down to **451.6 t/s** as the context fills from 4K to 13.4K tokens.
* **Engineering Action:** Informs optimal setting of chunk batching sizes (`n_batch`) and enables predicting TTFT based on user prompt length.

#### 2. Decode Streaming Throughput (`tg` vs `tg_3s`)
During token generation, Lemonade Server reports cumulative generation speed (`tg`) and rolling 3-second speed (`tg_3s`):
* `tg` represents the stable average throughput across the entire decode phase (**65.41 t/s**).
* `tg_3s` captures immediate burstiness (**52.56 to 73.74 t/s**). Spikes occur when sequential speculative predictions are verified without a single rejection forward pass.

---

### Dimension 2: Tokens & Speculative Decoding (MTP)

**Multi-Token Prediction (MTP)** equips the model with speculative drafting heads that propose multiple candidate tokens simultaneously:

$$\text{Effective Speedup} \approx \text{Mean Speculative Length} = \frac{\text{Tokens Emitted}}{\text{Verification Forward Passes}}$$

* **Observed Acceptance Rates:** **67.23%** (Task 1) and **63.36%** (Task 2).
* **Mean Speculative Length:** **3.02** and **2.90** tokens per step.
* **Architectural Payoff:** A standard autoregressive decoder requires 1 neural network forward pass per generated token (yielding ~20–22 t/s on a 35B model). With MTP accepting ~3 tokens per step, generation throughput reaches **65.41 t/s**—a **~3x acceleration** at zero loss in output quality!

---

### Dimension 3: Context Retention & Memory Utilization

* **Slot Memory Footprint:** Task 1 released at `15,400` tokens; Task 2 retained context up to `16,017` tokens in Slot 0.
* **Truncation Verification:** `truncated = 0` guarantees that prompt context and generations did not overflow the model's configured context window (`n_ctx`).
* **LRU Slot Management:** When slots are saturated, Lemonade Server evicts or re-assigns slots based on Least Recently Used (`t_last = 1842146247`), preserving recent session states when possible.

---

### Dimension 4: What Is Possible to Extract (Capability Matrix)

| Dimension | Available Telemetry Signal | Formula / Derivation | Engineering & Observability Value |
|---|---|---|---|
| **Prefill Scaling** | `prompt_eval_time`, chunk `speed_tps`, `progress` | $\frac{\text{prompt\_tokens}}{\text{prompt\_eval\_time}}$ | Detect attention scaling bottlenecks; tune prompt chunking and flash-attention. |
| **Streaming TPS** | Cumulative `tg`, rolling 3s `tg_3s` | $\frac{\Delta \text{tokens}}{\Delta 3\text{ seconds}}$ | Real-time user streaming smoothness; detect GPU thermal throttling or resource contention. |
| **Interactive Latency** | `ttft_s`, HTTP arrival to launch delay | $t_{\text{slot\_launch}} - t_{\text{http\_request}}$ | Measure customer SLAs; isolate queue backlog from model processing time. |
| **Speculative MTP** | `draft_acceptance_rate`, `mean_len` | $\frac{\text{accepted}}{\text{generated}}$ | Evaluate draft model efficiency; verify whether MTP accelerates inference or wastes compute. |
| **KV Cache & Memory** | `stop_processing n_tokens`, `truncated` | `truncated == 0` | Monitor per-slot VRAM memory; alert on context window overflow. |
| **Kernel Acceleration**| `graphs_reused` | Graph cache hit counter | Validates static graph capture (CUDA Graphs), avoiding CPU-to-GPU dispatch overhead. |

---

## 4. The SOTA TUI Tool: `lemonade_tui.py`

[`lemonade_tui.py`](file:///C:/Dev/github/philippeback/lemonade_tui/lemonade_tui.py) is a standalone, state-of-the-art Python tool designed to parse and visualize Lemonade Server logs. Built using **Textual** and **Rich**, it supports both full interactive terminal mode and static dashboard rendering.

### Feature Summary

* **Top KPI Ribbon:** Displays Active Task, Decode Speed (TPS), Prefill TTFT, In/Out Token Balance, MTP Speculation Rate, and Graph Hits.
* **Interactive Navigation Tabs:**
  1. **`1: Overview`**: Executive summary, Request Lifecycle Phase Gantt bar (`Queue -> Prefill -> Decode`), and comparative multi-task matrix.
  2. **`2: Speed & Throughput`**: Interactive data tables with visual throughput meters for both prompt chunking and generation streaming.
  3. **`3: Tokens & MTP`**: Token distribution bars and detailed MTP draft acceptance vs rejection breakdown.
  4. **`4: Context & Slots`**: Slot identifier, retained KV cache tokens, truncation status, and scheduling queue delay.
  5. **`5: Telemetry Matrix`**: In-TUI reference guide on all derivable metrics and their engineering applications.
  6. **`6: Raw Log`**: Filtered raw log stream for the selected task.

### Operational Usage

#### 1. Interactive TUI Mode (Default)
```bash
python lemonade_tui.py
```
* **Hotkeys:**
  * `t` / `p`: Next / Previous detected task (formatted with fixed-width IDs to keep top bar navigation buttons stable)
  * `1`–`6`: Switch directly between navigation tabs
  * `g`: Direct jump to task by numeric ID
  * `q`: Quit the application

#### 2. Static Terminal Dashboard Mode
For non-interactive environments, CI/CD pipelines, or quick terminal checks:
```bash
python lemonade_tui.py --static
```

#### 3. Custom Log File Inspection
```bash
python lemonade_tui.py path/to/another_server.log
```

#### 4. Markdown Report Export
```bash
python lemonade_tui.py --export performance_report.md
```

---

## 5. Production Tuning & Recommendations

1. **When TTFT Exceeds Latency Budgets:**
   * Look at the chunk ingestion table. If prompt throughput slows below 400 t/s on long prompts, enable Flash Attention (`--flash-attn`) and tune batch chunking (`-b 512` or `-b 1024`).
2. **When Speculative MTP Acceptance Drops Below 50%:**
   * High rejection rates mean the main model is continually discarding speculative tokens, causing redundant computation. Lower the draft sampling temperature or shorten the speculative prediction window.
3. **When Queue Delay is High (> 2.0s):**
   * High delays between `POST` arrival and slot dispatch indicate all inference slots are saturated. Scale the number of concurrent slots (`--parallel` / `-np`) or spin up an additional Lemonade container worker behind a load balancer.
4. **Validating CUDA Graph Efficiency:**
   * Ensure `graphs reused` climbs steadily with generation tokens. If `graphs reused` remains at 0, verify that CUDA Graph support is enabled on the server (`--cuda-graphs` / `--split-mode`).
