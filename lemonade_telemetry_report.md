# Lemonade Server Telemetry & Inference Analysis Report
* **Source Log:** `lemonade-sample.log`
* **Analyzed Tasks:** 2

---

## Task #5376 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:23:39.156` (Queue Delay: `5.99s`)
* **Total Context Active:** `15400` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `417.33 t/s` (`2.40 ms/tok`) | Time To First Token (TTFT) = `32.22s` |
| **Decode Speed (Generation)** | `65.41 t/s` (`15.29 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `13445` (87.3%) / Out: `1955` (12.7%) | Total footprint: `15400` tokens |
| **Speculative MTP Acceptance** | `67.23%` (`1307/1944`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.02` tokens/step | Effective speedup: ~`3.02x` vs unspeculated decode |
| **Graphs Reused** | `6,849` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 4,096 | 30.0% | 5.03 | 813.54 |
| 2 | 6,144 | 46.0% | 8.96 | 685.70 |
| 3 | 8,192 | 61.0% | 13.69 | 598.19 |
| 4 | 10,240 | 76.0% | 18.89 | 542.19 |
| 5 | 12,288 | 91.0% | 24.79 | 495.61 |
| 6 | 12,929 | 96.0% | 28.31 | 456.76 |
| 7 | 13,441 | 100.0% | 29.76 | 451.62 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 207 | 67.47 t/s | 67.80 t/s |
| 2 | 386 | 63.37 t/s | 59.23 t/s |
| 3 | 576 | 63.26 t/s | 63.03 t/s |
| 4 | 766 | 63.05 t/s | 62.43 t/s |
| 5 | 948 | 62.56 t/s | 60.59 t/s |
| 6 | 1,149 | 63.27 t/s | 66.82 t/s |
| 7 | 1,338 | 63.21 t/s | 62.88 t/s |
| 8 | 1,546 | 63.90 t/s | 68.66 t/s |
| 9 | 1,756 | 64.57 t/s | 69.95 t/s |

---

## Task #6337 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:24:45.730` (Queue Delay: `72.56s`)
* **Total Context Active:** `3033` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `225.04 t/s` (`4.44 ms/tok`) | Time To First Token (TTFT) = `6.47s` |
| **Decode Speed (Generation)** | `61.96 t/s` (`16.14 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1456` (48.0%) / Out: `1577` (52.0%) | Total footprint: `3033` tokens |
| **Speculative MTP Acceptance** | `63.36%` (`1034/1632`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.90` tokens/step | Effective speedup: ~`2.90x` vs unspeculated decode |
| **Graphs Reused** | `7,386` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 1,452 | 100.0% | 3.92 | 370.15 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 196 | 64.67 t/s | 65.00 t/s |
| 2 | 366 | 60.67 t/s | 56.64 t/s |
| 3 | 540 | 59.73 t/s | 57.86 t/s |
| 4 | 699 | 57.93 t/s | 52.56 t/s |
| 5 | 882 | 58.45 t/s | 60.54 t/s |
| 6 | 1,069 | 59.07 t/s | 62.18 t/s |
| 7 | 1,251 | 59.27 t/s | 60.45 t/s |
| 8 | 1,475 | 61.09 t/s | 73.74 t/s |

---

