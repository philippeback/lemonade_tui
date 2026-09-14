# Lemonade TUI

<p align="center">
  <img src="website/assets/brand/logo-lemonade-tui.svg" alt="Lemonade TUI Logo" width="480">
</p>

<p align="center">
  <strong>Real-time Inference Telemetry &amp; Systems Analytics for Lemonade Server LLM Workloads</strong>
</p>

<p align="center">
  <a href="#quick-start"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python 3.10+"></a>
  <a href="#quick-start"><img src="https://img.shields.io/badge/package_manager-uv-green.svg" alt="uv"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License: MIT"></a>
  <a href="website/index.html"><img src="https://img.shields.io/badge/docs-website-orange.svg" alt="Documentation Website"></a>
</p>

---

## Overview

**Lemonade TUI** (`lemonade_tui.py`) is a high-performance terminal user interface and diagnostic analytics suite for **Lemonade Server** (and compatible engines such as `llama.cpp`). It continuously parses server logs to provide deep observability into large language model inference dynamics:

* **Two-Phase Latency Breakdown:** Isolates queue scheduling latency, compute-bound prompt prefill (TTFT), and memory-bandwidth-bound autoregressive decode.
* **Speculative Decoding (Multi-Token Prediction - MTP):** Calculates draft acceptance rates ($\alpha$), mean speculative lengths ($\tau$), and effective throughput speedup multipliers.
* **Prefill Scaling Degradation:** Tracks chunk-by-chunk $O(N^2)$ self-attention slowdown as prompt context boundaries grow up to 13.5K+ tokens.
* **Hardware Acceleration & Memory:** Verifies static execution graph reuse (CUDA / Metal graphs) and slot Key-Value (KV) cache context retention.
* **Zero UI Jitter:** Enforces fixed-width layout stabilization (`TASK_ID_WIDTH = 6`, invariant badges, 17-cell mode button) and 60ms debounced table navigation.

---

## Quick Start

### Recommended with `uv` (Zero Setup)

```powershell
# Run the interactive TUI (defaults to sample log if none provided)
uv run python .\lemonade_tui.py

# Inspect active Lemonade Server logs
uv run python .\lemonade_tui.py "$env:TEMP\lemonade-server.log"
```

### Standard `pip` Installation

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Linux / macOS
source .venv/bin/activate

pip install rich textual
python lemonade_tui.py
```

---

## Four Distinct Operational Modes

| Mode | Command | Description |
|---|---|---|
| **1. Fullscreen Interactive Live TUI** | `uv run python .\lemonade_tui.py` | Real-time log tailing with Textual. Dynamic mode enabled by default. |
| **2. Static Snapshot Mode** | `uv run python .\lemonade_tui.py --snapshot` | Fullscreen TUI with background polling paused; zero CPU overhead. |
| **3. Lightweight Terminal Dashboard** | `uv run python .\lemonade_tui.py --static` | Single-shot summary directly to `stdout`. |
| **3b. Live Console Watch Mode** | `uv run python .\lemonade_tui.py --static -w` | Auto-refreshing in-place monitor in terminal scrollback. |
| **4. Automated Markdown Report Export** | `uv run python .\lemonade_tui.py --export report.md` | Exports comprehensive GitHub-ready Markdown telemetry report. |

---

## Interactive Keyboard Controls

| Key | Action | Scope | Description |
|---|---|---|---|
| **`q`** | Quit | Global | Exits the application immediately. |
| **`t`** | Next Task | Global | Selects the next chronological task in the log. |
| **`p`** | Previous Task | Global | Selects the previous chronological task in the log. |
| **`d`** | Toggle Dynamic/Static | Global | Switches between live log tailing and zero-overhead snapshot mode. |
| **`g`** | Go to Task # | Global | Opens the task jump modal dialog. |
| **`r`** | Refresh | Global | Manually re-reads log data from disk in static mode. |
| **`1` - `6`** | Switch Tabs | Global | `1: Overview`, `2: Speed`, `3: Tokens`, `4: Context`, `5: Matrix`, `6: Raw Log`. |
| **`Up / Down`** | Navigate Rows | Overview Table | Rapidly moves selection cursor across tasks (debounced at 60ms). |
| **`Enter`** | Select Task | Overview Table | Instantly commits task selection and updates details. |

---

## Project Structure & Documentation

* **[`lemonade_tui.py`](lemonade_tui.py)**: The complete application engine.
* **[`lemonade_tui_full_guide.md`](lemonade_tui_full_guide.md)**: Comprehensive 847-line reference manual, user guide, theory of metrics, and performance engineering internals.
* **[`lemonade_tui_modularization_plan.md`](lemonade_tui_modularization_plan.md)**: Architectural plan for decomposing the monolithic script into a modular package.
* **[`lemonate_tui_telemetry_guide.md`](lemonate_tui_telemetry_guide.md)**: Deep-dive guide on telemetry extraction and log grammars.
* **[`lemonade-sample.log`](lemonade-sample.log)**: Realistic sample log stream featuring tasks with MTP acceleration and in-flight streaming.
* **[`website/`](website/)**: Official showcase website and browser-based interactive Textual engine simulator.

---

## License

Released under the [MIT License](LICENSE).
