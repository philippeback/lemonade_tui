# OpenSpec: Lemonade TUI Official Website Specification

| Attribute | Specification Details |
|---|---|
| **Spec Title** | Lemonade TUI Website Structure and Content Specification |
| **Spec ID** | `OPENSPEC-LEMONADE-TUI-WEB-001` |
| **Document Version** | `1.0.0` |
| **Status** | `APPROVED` |
| **Based Upon** | `lemonade_ui_website_spec.md`, `lemonade_tui_full_guide.md`, `lemonade_tui.py` |
| **Target Directory** | `website/` |
| **Specification Format** | OpenSpec Standard (RFC 2119 Conformance Levels) |
| **Theme / Design System** | Dark UI matching `lemonade_tui.py` Textual/Rich Theme |

---

## 1. Scope & OpenSpec Conformance

### 1.1 Purpose & Objectives
This document specifies the complete information architecture, design tokens, visual hierarchy, verbatim content, interactive behaviors, asset requirements, and file layout for the official website of **Lemonade TUI** (`lemonade_tui.py`).

The website serves as:
1. **The Product Showcase:** Introducing developers and ML engineers to Lemonade TUI—a high-performance, real-time telemetry inspection suite for Lemonade Server LLM inference.
2. **An Interactive Diagnostic Experience:** Providing an interactive browser-based terminal simulation replicating the 6 diagnostic panes and dynamic execution modes.
3. **The Definitive Technical Reference:** Exposing the mathematical theory of LLM inference metrics (Prefill GEMM, Decode GEMV, Multi-Token Prediction speculative dynamics, KV cache retention, graph reuse) and systems engineering internals.
4. **An Operational Quick Start:** Offering copy-paste command recipes, installation workflows, and direct links to the GitHub repository.

### 1.2 RFC 2119 Conformance Keywords
The key words **"MUST"**, **"MUST NOT"**, **"REQUIRED"**, **"SHALL"**, **"SHALL NOT"**, **"SHOULD"**, **"SHOULD NOT"**, **"RECOMMENDED"**, **"MAY"**, and **"OPTIONAL"** in this document are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

---

## 2. Brand Identity, Visual Language & Design Tokens

### 2.1 The Citrus-Telemetry Logo Design Specification
The logo **MUST** bridge the identity of Lemonade Server (the citrus lemon) with telemetry parsing (structured terminal output and data streams).

```
                 Telemetry Vector Brackets
                     ┌───────────────┐
                 \   │  ___     ___  │   /
                  \  │ /   \   /   \ │  /
                   \ │ | t |   | g | │ /
                    ─┼─┴───┴───┴───┴─┼─  ◄── Transverse Citrus Segment Line
                   / │ | p |   | s | │ \
                  /  │ \___/   \___/ │  \
                 /   │   0.3657 MTP  │   \
                     └───────────────┘
                     Citrus Wedge Matrix
```

* **Symbolic Concept:** A cross-section of a glowing citrus lemon where the inner triangular pulp wedges are styled as terminal diagnostic cells, bracketed by monospace code delimiters `[ ]` and streaming telemetry sparks.
* **Colors:** Lemon Amber (`#f0883e`) outline and glow, Lime-Citron Accent (`#3fb950`) for speculative hits, and Obsidian Core (`#161b22`).
* **Wordmark:** `Lemonade` in bold geometric grotesque (`Outfit` / `Inter`, 700 weight, `#c9d1d9`), followed by `TUI` in highlighted monospace (`JetBrains Mono`, 800 weight, `#f0883e`).
* **Sub-Badge:** A small monospace pill badge reading `TELEMETRY ENGINE`.
* **Favicon & App Icon:** A simplified 32x32 / 64x64 SVG icon featuring a lemon slice with a central prompt cursor `>_`.

### 2.2 Complete Color Palette Tokens (from `lemonade_tui.py`)
All website elements **MUST** use the exact color tokens extracted from `LemonadeTUIApp.CSS` and Rich console styles:

| Token Name | Hex Value | Semantic Usage in Lemonade TUI |
|---|---|---|
| `--color-bg-canvas` | `#0d1117` | Root background (obsidian terminal canvas) |
| `--color-bg-surface` | `#161b22` | Header, Footer, Task Bar, Navigation container background |
| `--color-bg-card` | `#161b22` | KPI card background, container backgrounds |
| `--color-bg-card-highlight` | `#1c2128` | Active/focused KPI card, selected tab, modal popover |
| `--color-border-default` | `#30363d` | Standard borders, card dividers, table borders |
| `--color-border-accent` | `#f0883e` | Highlighted borders, active state indicator |
| `--color-accent-citrus` | `#f0883e` | Primary brand citrus orange; Header title, key actions |
| `--color-accent-green` | `#3fb950` | Completed status `✔ DONE`, decode throughput, positive MTP |
| `--color-accent-orange` | `#d29922` | Prefill prompt eval, warning status, in-flight badge |
| `--color-accent-blue` | `#58a6ff` | Metric values, hyperlinks, table keys, active indicators |
| `--color-accent-red` | `#f85149` | Aborted status `✖ ABORTED`, queue scheduling delay |
| `--color-text-primary` | `#c9d1d9` | Primary body text, table cell content, button text |
| `--color-text-muted` | `#8b949e` | Labels, table headers, inactive shortcuts, metadata |
| `--color-terminal-glow` | `rgba(240, 136, 62, 0.15)` | Subtle drop shadow and ambient glow behind active cards |

### 2.3 Typography & Hierarchy Tokens
* **Monospace Code Font (Primary UI & Data Tables):**
  `'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'SF Mono', Consolas, monospace`
  *Usage:* Navigation keys, table cells, metric values, terminal commands, KPI figures.
* **Heading & Display Font:**
  `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
  *Usage:* Page hero headline, section titles, marketing copy.
* **Scale:**
  * `Hero Display`: `2.75rem (44px)` / line-height `1.15` / weight `800`
  * `H1 Section Title`: `2.0rem (32px)` / line-height `1.25` / weight `700`
  * `H2 Subsection Title`: `1.375rem (22px)` / line-height `1.35` / weight `600`
  * `H3 Card Title`: `1.0rem (16px)` / line-height `1.4` / weight `600`
  * `Body Text`: `0.9375rem (15px)` / line-height `1.6` / weight `400`
  * `Code / Monospace`: `0.875rem (14px)` / line-height `1.5` / weight `500`
  * `KPI Value`: `1.25rem (20px)` / line-height `1.2` / weight `700`

---

## 3. Information Architecture (IA) & Directory Structure

### 3.1 File System Structure (`website/`)
All website assets and markup **MUST** reside within the `website/` directory of the repository:

```
website/
├── index.html                      # Primary single-page application & showcase
├── 404.html                        # Fallback error page
├── CNAME                           # Custom domain configuration (if deployed)
├── css/
│   ├── tokens.css                  # CSS custom properties, color palette, typography
│   ├── layout.css                  # Grid systems, responsive breakpoints, container rules
│   ├── components.css              # KPI cards, navigation bar, buttons, tabs, tables
│   └── terminal-simulator.css      # Textual TUI emulation styles and animations
├── js/
│   ├── app.js                      # Navigation, smooth scroll, copy-to-clipboard, tooltips
│   ├── terminal-simulator.js       # Interactive TUI simulator (state machine, key listeners)
│   └── telemetry-data.js           # Sample dataset (Tasks #16104, #5376, #6337, #16240)
└── assets/
    ├── brand/
    │   ├── logo-lemonade-tui.svg   # Vector citrus-terminal brand mark
    │   ├── logo-icon.svg           # Favicon and simplified 32x32 glyph
    │   └── favicon.ico             # Multiresolution favicon
    ├── screenshots/
    │   ├── tui-tab1-overview.png   # Tab 1: Overview & Task Browser
    │   ├── tui-tab2-speed.png      # Tab 2: Speed & Throughput Dynamics
    │   ├── tui-tab3-tokens.png     # Tab 3: Tokens & MTP Speculation
    │   ├── tui-tab4-context.png    # Tab 4: Context Window & Slot Retention
    │   ├── tui-tab5-matrix.png     # Tab 5: Telemetry Capability Matrix
    │   ├── tui-tab6-raw.png        # Tab 6: Raw Log Stream
    │   ├── mode-dynamic-tail.png   # Dynamic Streaming Live Tailing Mode
    │   ├── mode-rich-static.png    # Rich Console Single-Shot Dashboard
    │   ├── mode-rich-watch.png     # Rich Console Dynamic Live Watch Mode
    │   ├── modal-jump-task.png     # Task Navigation Jump Modal Dialog
    │   └── report-export.png       # Generated Markdown Telemetry Benchmark Report
    └── diagrams/
        ├── prefill-decode-flow.svg # Two-Phase LLM Execution Architecture Diagram
        ├── mtp-speculation.svg     # Multi-Token Prediction verification workflow
        └── state-machine.svg       # Task lifecycle state machine diagram
```

### 3.2 Single-Page Navigation & Anchor Architecture
The website **SHALL** be structured as a high-velocity single-page technical portal with dedicated persistent anchor navigation:

* `#overview`: Executive value proposition, quick install, live interactive TUI emulator
* `#modes`: The 4 execution modes (Interactive Dynamic, Static Snapshot, Rich Dashboard, Markdown Export)
* `#panes`: The 6 Diagnostic Panes deep-dive with screenshots and metric analyses
* `#metrics-theory`: LLM systems architecture theory (GEMM prefill, GEMV decode, MTP, KV cache)
* `#cli-reference`: CLI arguments, syntax grammar, PowerShell & Bash execution commands
* `#internals`: Engineering highlights (Layout stabilization, ConPTY debouncing, stateful byte-seeking parser)
* `#github`: Links to repository, issue tracker, release notes, and community

---

## 4. Page Structure & Wireframe Specification

### 4.1 Page Layout Wireframe (Ascii Flowchart)

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO: Citrus Terminal] Lemonade TUI      [Overview] [Modes] [Panes] [Theory] [CLI] │ [★ GitHub] │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                  HERO SECTION                                    │
│   Real-Time Inference Telemetry & Analytics for Lemonade Server LLM Workloads     │
│   Sub-heading: Decode Speed • Prefill Decay • Speculative MTP • KV Cache Retention│
│   [Get Started (uv run)]  [Explore Live Interactive TUI]  [View on GitHub]        │
├──────────────────────────────────────────────────────────────────────────────────┤
│                     INTERACTIVE TERMINAL HUD & SIMULATOR                         │
│  ┌────────────────────────────────────────────────────────────────────────────┐  │
│  │ Task Bar: [|◀ Start] [◀ Prev] Task #5376 [✔ DONE] [Next ▶] [End ▶|] [Dynamic]│  │
│  ├────────────────────────────────────────────────────────────────────────────┤  │
│  │ KPI Strip: [ACTIVE TASK] [DECODE SPEED] [PREFILL] [TOKENS] [MTP] [GRAPH]   │  │
│  ├────────────────────────────────────────────────────────────────────────────┤  │
│  │ Tabs: [1: Overview] [2: Speed] [3: Tokens] [4: Context] [5: Matrix] [6:Raw] │  │
│  │ (Live rendered DOM widget simulating Textual with real keyboard shortcuts) │  │
│  └────────────────────────────────────────────────────────────────────────────┘  │
├──────────────────────────────────────────────────────────────────────────────────┤
│                              EXECUTION MODES (4-WAY)                             │
│   [1. Interactive TUI]   [2. Static Snapshot]   [3. Rich Watch]   [4. CI/CD Export]│
├──────────────────────────────────────────────────────────────────────────────────┤
│                         THE 6 DIAGNOSTIC PANES SHOWCASE                          │
│   Visual cards featuring real screenshots, exact telemetry metrics & diagrams    │
├──────────────────────────────────────────────────────────────────────────────────┤
│                     THEORY OF LLM INFERENCE METRICS (DEEP-DIVE)                  │
│   • Prefill (GEMM) vs. Decode (GEMV)   • O(N²) Attention Scaling Degradation     │
│   • Speculative MTP Dynamics (3.1x)    • KV Cache Footprint & Execution Graphs   │
├──────────────────────────────────────────────────────────────────────────────────┤
│                         CLI REFERENCE & LOG GRAMMAR                              │
│   Interactive command generator + regex grammar table                            │
├──────────────────────────────────────────────────────────────────────────────────┤
│                  ENGINEERING INTERNALS & PERFORMANCE OPTIMIZATIONS               │
│   • Fixed-Width Jitter Elimination     • 60ms Debounced Virtualized Scrolling    │
│   • Incremental Byte-Seeking Parser    • Layout Isolation & ConPTY Loops Fix     │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                   FOOTER                                         │
│   Brand Mark • MIT License • GitHub Repo • philippeback/local_ai stack           │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Detailed Section-by-Section Content & Copywriting Specification

### 5.1 Global Sticky Header & Navigation
* **Container ID:** `#site-header`
* **Styling:** Background `#161b22`, height `64px`, bottom border `1px solid #30363d`, sticky `top: 0`, backdrop-filter blur `10px`.
* **Left Element:**
  * Logo SVG (Citrus slice with terminal bracket glyphs).
  * Brand Name: `Lemonade TUI` with a small version pill: `v1.0.0-beta`.
* **Center Navigation Links (`#nav-menu`):**
  1. `Overview` (`href="#overview"`)
  2. `Modes` (`href="#modes"`)
  3. `Diagnostic Panes` (`href="#panes"`)
  4. `Theory & Metrics` (`href="#metrics-theory"`)
  5. `CLI Reference` (`href="#cli-reference"`)
  6. `Internals` (`href="#internals"`)
* **Right Actions:**
  * **GitHub Repository Button (`#btn-github-nav`):**
    * Label: `GitHub` with Octocat icon and live/placeholder star count badge.
    * Target: `https://github.com/philippeback/lemonade_tui` (or project repo URL).
    * Styling: Dark button, border `1px solid #30363d`, hover color `#f0883e`.
  * **Quick Launch Button (`#btn-quick-launch`):**
    * Label: `uv run`
    * Action: Copies `uv run python lemonade_tui.py` to clipboard with tooltip `"Copied!"`.

---

### 5.2 Hero Section (`#overview`)
* **Badge:** Monospace pill with pulsing citrus-amber indicator:
  `● REAL-TIME INFERENCE TELEMETRY FOR LEMONADE SERVER`
* **Headline (H1):**
  `Precision Telemetry & Systems Analytics for Local LLM Workloads`
* **Sub-headline (Lead Paragraph):**
  > Inspect autoregressive decode throughput, multi-token speculative prediction (MTP) acceleration, prefill attention scaling slowdown, and KV cache allocation directly in your terminal. Zero overhead, stateful incremental log ingestion, and rock-solid layout stabilization.
* **Hero CTA Button Group:**
  * **Primary Action (`#btn-hero-primary`):**
    * Text: `Run with uv`
    * Sub-text: `uv run python .\lemonade_tui.py`
    * Behavior: Click copies command to clipboard; shows instant feedback checkmark.
  * **Secondary Action (`#btn-hero-secondary`):**
    * Text: `Explore Live TUI Simulator` (`href="#tui-simulator"`)
    * Icon: Downward terminal chevron `▼`
  * **Tertiary Action (`#btn-hero-github`):**
    * Text: `View Source Code`
    * Icon: GitHub Octocat (`target="_blank"`)

---

### 5.3 Interactive TUI Simulator Section (`#tui-simulator`)
The website **MUST** include an interactive browser widget that faithfully reproduces the Textual TUI interface, allowing prospective users to test keyboard navigation and view live simulated telemetry.

#### 5.3.1 Task Navigation Bar (`#sim-task-bar`)
Replicates the fixed-width, jitter-free navigation banner:
```
[|◀ Start]  [◀ Prev [p]]   Task #5376   [✔ DONE     ]   [ 1/4]   [Next [t] ▶]  [End ▶|]  [Go to # [g]]  [● Dynamic [d]]
```
* **Interactive Controls:**
  * Clicking `[◀ Prev]` or pressing key `p` switches to previous simulated task.
  * Clicking `[Next ▶]` or pressing key `t` switches to next simulated task.
  * Clicking `[Go to #]` or pressing key `g` opens the jump modal dialog.
  * Clicking `[● Dynamic [d]]` or pressing key `d` toggles between `● Dynamic [d]` and `⏸ Static  [d]`.

#### 5.3.2 KPI Ribbon Strip (`#sim-kpi-strip`)
Six invariant-width HUD cards styled with `#161b22` background and `#30363d` rounded borders:

| Card Title | Card ID | Sample Value (Task #5376) | Formatting Rule |
|---|---|---|---|
| `ACTIVE TASK` | `#val-task` | `#5376 (Slot 0)` | Fixed 18-character buffer |
| `DECODE SPEED` | `#val-decode` | `65.4 t/s (15.3ms)` | Blue `#58a6ff` |
| `PREFILL (TTFT)` | `#val-prefill` | `814 t/s (2.6s)` | Yellow `#d29922` |
| `TOKENS (IN/OUT)` | `#val-tokens` | `In:13445 / Out: 777` | Fixed column spacing |
| `MTP SPECULATION` | `#val-mtp` | `67.2% (len 3.02)` | Green `#3fb950` |
| `GRAPH REUSE` | `#val-graph` | `16,290 hits` | Fixed digit alignment |

#### 5.3.3 Tab Navigation & Active Panes (`#sim-tabs`)
Tabs styled with Textual key labels:
`[1: Overview]` `[2: Speed]` `[3: Tokens & MTP]` `[4: Context]` `[5: Matrix]` `[6: Raw]`
* Pressing keys `1` through `6` switches active tabs in the simulator.
* Content area dynamically displays the selected pane view.

#### 5.3.4 Simulated Tasks Data Manifest
The simulator **MUST** include four representative datasets:
1. **Task #5376 (Completed Speculative MTP Task):** 13,445 prompt tokens, 777 generated tokens, 65.41 t/s decode, 67.23% draft acceptance, $\tau = 3.02$, 16,290 graph hits.
2. **Task #6337 (High-Speed Decode Task):** 362 prompt tokens, 1,024 generated tokens, 72.18 t/s decode, 63.36% draft acceptance, $\tau = 2.90$.
3. **Task #16240 (Active In-Flight Streaming Task):** 2,048 prompt tokens, 142* tokens streaming, live rolling speed `tg_3s = 58.4 t/s`, marked with `● IN-FLIGHT` and pulsing status.
4. **Task #0 (Aborted Request):** Cancelled by client, 0 tokens generated, marked with `✖ ABORTED`.

---

### 5.4 Execution Modes Showcase (`#modes`)
Section presenting the four primary execution modes defined in the guide:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              FOUR DISTINCT EXECUTION MODES                             │
│       Choose the right visualization workflow for debugging, monitoring, or CI/CD      │
├────────────────────────────┬────────────────────────────┬──────────────────────────────┤
│ 1. Fullscreen Live TUI     │ 2. Static Snapshot TUI     │ 3. Rich Terminal Dashboard   │
│ Real-time log tailing with │ Zero-overhead log browsing │ Console-native single-shot   │
│ Textual. Auto-refreshes on │ with background polling    │ summary or live watch mode   │
│ every emitted token chunk. │ paused. Maximum response.  │ directly into stdout buffer. │
│                            │                            │                              │
│ uv run python .\lemonade_  │ uv run python .\lemonade_  │ uv run python .\lemonade_    │
│ tui.py logfile.log         │ tui.py --snapshot log.log  │ tui.py --static -w log.log   │
├────────────────────────────┴────────────────────────────┴──────────────────────────────┤
│ 4. Automated CI/CD Markdown Report Export (`--export benchmark_report.md`)             │
│ Generates GitHub-ready Markdown reports with complete tables, prefill curves, and      │
│ speculative MTP speedup analyses for automated regression testing and model benchmark. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

Each mode card **MUST** provide:
* Mode Title and Badge (Interactive, Offline, Headless, CI/CD).
* High-resolution screenshot of actual output.
* Shell command with one-click copy button.
* 3 bullet points detailing systems implications (e.g., polling overhead, ConPTY footprint, memory usage).

---

### 5.5 The 6 Diagnostic Panes Showcase (`#panes`)
This section provides an in-depth walkthrough of the 6 diagnostic tabs using actual screenshots, detailed telemetry metric definitions, and engineering takeaways.

#### 5.5.1 Tab 1: Executive Overview & Task Browser
* **Screenshot Asset:** `website/assets/screenshots/tui-tab1-overview.png`
* **Heading:** `Tab 1: Executive Overview & Task Browser`
* **Subheading:** `Split-view request diagnostics, lifecycle timelines, and debounced task browsing`
* **Core Components:**
  1. **Loaded Model & Concurrency Identifiers:** Displays model name, quantization (`Q4_K`), active slot ID, and child task status.
  2. **Three-Phase Request Lifecycle Timeline:**
     * Visual horizontal stacked bar breaking down the total request duration:
       * **Red (`#f85149`):** Queue Latency ($t_{queue} = t_{launch} - t_{HTTP}$). Optimal state: $<0.06\text{s}$.
       * **Yellow (`#d29922`):** Prefill Phase ($t_{prefill}$). Compute-bound prompt evaluation.
       * **Green (`#3fb950`):** Decode Phase ($t_{decode}$). Memory-bound autoregressive token generation.
  3. **Virtualized Task Table (`#overview-task-table`):**
     * Fixed-height container (`height: 12`) isolating table scroll events from Textual's layout engine.
     * Columns: `Task ID`, `Model`, `Prompt In`, `Gen Out`, `Prefill Speed`, `TTFT`, `Decode Speed`, `MTP Acc %`, `Mean Len`, `Graphs`.
     * Real-time prefix icons: `⚡#16240` (In-Flight), `#5376` (Completed), `✖#0` (Aborted).

#### 5.5.2 Tab 2: Speed & Throughput Dynamics
* **Screenshot Asset:** `website/assets/screenshots/tui-tab2-speed.png`
* **Heading:** `Tab 2: Speed & Throughput Dynamics`
* **Subheading:** `Decomposing prompt ingestion scaling decay and autoregressive generation stability`
* **Core Components:**
  1. **Prompt Processing (Prefill) Progressive Throughput Table:**
     * Displays chunk ingestion steps, progressive token count, % complete, elapsed step time, and chunk ingestion throughput (`t/s`).
     * Includes relative horizontal bar graphs demonstrating throughput drop across context boundaries.
  2. **Token Generation (Decode) Streaming Throughput Table:**
     * Step-by-step decode checkpoints listing tokens generated (`n_gen`), cumulative average speed (`tg`), and instantaneous rolling 3-second speed (`tg_3s`).
     * Real-time jitter analysis revealing speculative acceptance bursts vs. draft rejections.

#### 5.5.3 Tab 3: Tokens & MTP Speculation Analysis
* **Screenshot Asset:** `website/assets/screenshots/tui-tab3-tokens.png`
* **Heading:** `Tab 3: Tokens & Multi-Token Prediction (MTP) Speculation`
* **Subheading:** `Quantifying the efficiency and effective speedup of Speculative Decoding`
* **Core Components:**
  1. **Visual Token Distribution Bar:** Compares Prompt Inbound Tokens vs. Completion Outbound Tokens.
  2. **Draft Acceptance Rate ($\alpha$):** Formula $\frac{N_{accepted}}{N_{generated}} \times 100\%$. Real-world log sample: $67.23\%$.
  3. **Speculative Draft Accounting:** Breakdown of Total Generated Draft Tokens, Accepted Tokens, and Rejected Tokens.
  4. **Mean Speculative Length ($\tau$):** Average verified tokens produced per engine verification pass (e.g. $\tau = 3.02\text{ tokens/step}$).
  5. **Effective Speedup Multiplier ($S \approx \tau$):** Demonstrates how MTP quadrupled generation speed from $21.4\text{ t/s}$ to $65.4\text{ t/s}$ on identical hardware.

#### 5.5.4 Tab 4: Context Window, Slot Retention & Execution Graph Hits
* **Screenshot Asset:** `website/assets/screenshots/tui-tab4-context.png`
* **Heading:** `Tab 4: Context Window, Slot Retention & Hardware Acceleration`
* **Subheading:** `Monitoring KV cache memory allocation, context boundary limits, and CUDA Graph reuse`
* **Core Components:**
  1. **Retained Context Tokens:** Tokens preserved in the slot's Key-Value cache across multi-turn sessions (`stop processing: n_tokens = 15400`).
  2. **Truncation Verification:** Validates that completions did not breach hard context limits (`truncated == 0`).
  3. **LRU Cache Timestamp:** Tracks slot eviction timestamps under concurrent multi-tenant loads.
  4. **Graph Cache Hits:** Verifies static execution graph capture and replay (`graphs reused = 16,290`), confirming elimination of CPU-to-GPU driver launch latency.

#### 5.5.5 Tab 5: Architectural Telemetry Capability Matrix
* **Screenshot Asset:** `website/assets/screenshots/tui-tab5-matrix.png`
* **Heading:** `Tab 5: Telemetry Capability Matrix`
* **Subheading:** `Exhaustive mapping of captured log signals, mathematical derivations, and systems value`
* **Interactive Feature:** Filterable table allowing users to search metrics by category (Latency, Throughput, Memory, Speculation, Hardware).

#### 5.5.6 Tab 6: Raw Log Stream Inspection
* **Screenshot Asset:** `website/assets/screenshots/tui-tab6-raw.png`
* **Heading:** `Tab 6: Raw Log Stream Inspection`
* **Subheading:** `Full forensic visibility with correlated task line filtering`
* **Core Components:** Monospace syntax-highlighted log viewer displaying verbatim log entries for the active task, preserving timestamps and engine diagnostics.

---

### 5.6 Theory of LLM Inference Metrics (Educational Deep-Dive) (`#metrics-theory`)
The website **MUST** articulate the systems architecture concepts underpinning `lemonade_tui`, rendering mathematical equations and interactive comparisons:

#### 5.6.1 Two-Phase Inference Asymmetry: Prefill vs. Decode
* **Comparison Matrix:**
  * **Prefill Phase (Prompt Ingestion):** Compute-Bound (GEMM). Matrix-matrix multiplication saturates GPU Tensor Cores. Throughput: $400\text{--}850\text{ tokens/sec}$. Arithmetic Intensity: High.
  * **Decode Phase (Autoregressive Token Gen):** Memory-Bandwidth-Bound (GEMV). Matrix-vector multiplication requires transferring entire model weights from VRAM to SRAM for *every single token*. Throughput: $20\text{--}75\text{ tokens/sec}$. Arithmetic Intensity: Low ($<1\text{ FLOP/byte}$).
* **SVG Architectural Diagram:** Fenced visual showing prompt tokens entering GEMM compute engine vs. single-token autoregressive loop hitting the memory bandwidth wall.

#### 5.6.2 Attention Scaling Degradation in Prefill ($O(N^2)$)
* **Mathematical Equation:**
  $$\text{TTFT} = t_{\text{queue}} + t_{\text{prefill}} = t_{\text{queue}} + \frac{N_{\text{prompt}}}{\text{Throughput}_{\text{prefill}}(N_{\text{prompt}})}$$
  $$\text{Self-Attention FLOPs} \approx 4 \cdot N^2 \cdot d_{\text{model}} + 24 \cdot N \cdot d_{\text{model}}^2$$
* **Empirical Observation Table:**
  Shows the measured 44.5% speed degradation in Lemonade Server as prompt context grows from $1\text{K}$ to $13.5\text{K}$ tokens (from $813.5\text{ t/s}$ down to $451.6\text{ t/s}$).

#### 5.6.3 The Memory Bandwidth Wall & Autoregressive Decode
* **Mathematical Equation:**
  $$\text{Theoretical Single-Token TPS} = \frac{\text{Memory Bandwidth (Bytes/s)}}{\text{Active Model Footprint (Bytes)}} \times \eta$$
* Explains why a 35B parameter Q4_K model (~22 GB) capped at 500 GB/s bandwidth cannot exceed ~22.7 t/s without speculative decoding.

#### 5.6.4 Speculative Decoding & Multi-Token Prediction (MTP)
* **Mathematical Formulations:**
  * Draft Acceptance Rate: $\alpha = \frac{N_{accepted}}{N_{generated}} \times 100\%$
  * Mean Speculative Length: $\tau = \frac{N_{emitted}}{N_{verification\ steps}}$
  * Speedup Multiplier: $S \approx \tau$
* Demonstrates how evaluating speculative candidates in parallel forward passes breaks through the memory bandwidth ceiling.

---

### 5.7 CLI Reference & Syntax Specification (`#cli-reference`)

#### 5.7.1 Command Syntax & Arguments Table
```
usage: lemonade_tui.py [-h] [--static] [--dynamic] [--snapshot] [--all]
                       [--include-empty] [--task TASK_ID] [--export OUT_FILE] [logfile]
```

| Argument | Flag / Type | Default | Description & Operational Impact |
|---|---|---|---|
| `logfile` | Positional | `lemonade-sample.log` | Path to server log. Supports `$env:TEMP`, Unix `$TEMP`, `~`, and relative paths. |
| `--static` | Flag | `False` | Renders a Rich console dashboard directly to stdout without launching fullscreen TUI. |
| `--dynamic`, `-d`, `-w` | Flag | `False` | Auto-refreshes terminal dashboard in `--static` mode, or forces dynamic mode in TUI. |
| `--snapshot`, `--pause` | Flag | `False` | Starts interactive TUI directly in snapshot mode (background polling paused). |
| `--task TASK_ID` | Integer | `None` | Automatically selects and highlights the specified Task ID on launch. |
| `--all` | Flag | `False` | Renders all historical tasks in `--static` mode (defaults to latest 5). |
| `--include-empty` | Flag | `False` | Preserves aborted requests or empty prompts with zero token progress. |
| `--export OUT_FILE` | String | `None` | Exports comprehensive Markdown telemetry report to disk and exits. |

#### 5.7.2 Interactive Command Builder
A dynamic GUI component where users click checkboxes (e.g. `[x] Live Watch Mode`, `[x] Specific Task ID: 5376`, `[x] Custom Log Path`) and the code snippet updates in real time with a 1-click copy button:
```powershell
uv run python .\lemonade_tui.py --static -w --task 5376 "$env:TEMP\lemonade-server.log"
```

---

### 5.8 Performance Engineering & Internals (`#internals`)
Highlights the architectural fixes implemented in `lemonade_tui.py`:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ENGINEERED FOR EXTREME TERMINAL STABILITY                       │
├────────────────────────────┬────────────────────────────┬──────────────────────────────┤
│ 1. Zero Jitter Alignment   │ 2. 60ms Debounced Scrolling│ 3. Layout Thrashing Fix      │
│ Invariant TASK_ID_WIDTH=6, │ High-speed arrow navigation│ DataTable isolated into its  │
│ 11-char status badges, and │ at 120 FPS; detail panels  │ own 12-row container, ending │
│ fixed 17-cell mode toggle  │ render only after motion   │ virtualized recalculation    │
│ eliminate coordinate jump. │ ceases for 60ms.           │ loops on Windows ConPTY.     │
├────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ 4. Stateful Byte-Seek Tail │ 5. In-Place Cell Mutation  │ 6. Single-Pass Initialization│
│ Incremental tell()/seek()  │ Real-time token updates    │ 11,000-line log files ingest │
│ reads newly appended bytes │ modify only active cells   │ once during startup, slashing│
│ without re-reading files.  │ (<0.1ms per cycle).        │ launch latency by 81%.       │
└────────────────────────────┴────────────────────────────┴──────────────────────────────┘
```

---

### 5.9 Global Footer & Ecosystem (`#site-footer`)
* **Left Column:**
  * Citrus-Terminal Brand Logo
  * Mission statement: `Open-source telemetry and observability for high-throughput LLM engines.`
  * Copyright notice: `Released under MIT License. Part of the philippeback/local_ai suite.`
* **Middle Column (Resources & Guides):**
  * `Full Architecture & Reference Guide` (`lemonade_tui_full_guide.md`)
  * `Modularization Plan` (`lemonade_tui_modularization_plan.md`)
  * `Telemetry Sample Log` (`lemonade-sample.log`)
  * `PowerShell Launch Script` (`run_lemonade_tui.ps1`)
* **Right Column (Community & GitHub):**
  * Link to GitHub Repository
  * Link to Issue Tracker & Discussions
  * Link to Local AI Stack Documentation

---

## 6. Media & Screenshot Asset Specifications

### 6.1 Screenshot Manifest
All screenshots **MUST** be captured at `1920x1080` (or `2x` Retina equivalent at minimum `1440x900`), rendered with the exact `#0d1117` dark palette, crisp typography, and optimized via WebP/PNG with lossy-clean compression:

| Asset Name | Target File Path | UI State to Capture | Annotations / Highlights |
|---|---|---|---|
| `Overview Tab` | `website/assets/screenshots/tui-tab1-overview.png` | Tab 1 active with Task #5376 selected | Callouts on Timeline Bar & Task Table |
| `Speed Tab` | `website/assets/screenshots/tui-tab2-speed.png` | Tab 2 active showing prefill chunk decay | Callouts on decay % and `tg_3s` jitter |
| `Tokens Tab` | `website/assets/screenshots/tui-tab3-tokens.png` | Tab 3 active showing MTP speculation | Callouts on 67.2% draft acceptance & $\tau$ |
| `Context Tab` | `website/assets/screenshots/tui-tab4-context.png` | Tab 4 active showing 16,290 graph hits | Callout on KV cache retention |
| `Matrix Tab` | `website/assets/screenshots/tui-tab5-matrix.png` | Tab 5 active showing capability matrix | Monospace table borders |
| `Raw Tab` | `website/assets/screenshots/tui-tab6-raw.png` | Tab 6 active showing regex-matched logs | Syntax-colored timestamps |
| `Live Watch Mode`| `website/assets/screenshots/mode-rich-watch.png` | PowerShell console running `--static -w` | Rich table borders and active spinner |
| `Jump Modal` | `website/assets/screenshots/modal-jump-task.png` | Task Jump modal dialog `#jump-dialog` | Centered modal on darkened backdrop |
| `Markdown Report`| `website/assets/screenshots/report-export.png` | Rendered Markdown report in GitHub | Executive summary and metric tables |

### 6.2 SVG Asset Generation Requirements
* **Logo SVG (`logo-lemonade-tui.svg`):** Scalable vector graphic adhering to the citrus-slice cross-section geometry specified in Section 2.1.
* **Architecture Diagrams:** All diagrams **MUST** be responsive SVGs using CSS variable colors to match dark canvas `#0d1117`.

---

## 7. Interactive JavaScript Behavioral Specification

### 7.1 Simulated Textual TUI Engine (`js/terminal-simulator.js`)
* **State Management:**
  * Tracks `currentTaskIndex` (0 to 3).
  * Tracks `activeTab` (1 to 6).
  * Tracks `isDynamic` (Boolean: `true` or `false`).
* **Keyboard Event Handlers:**
  * When the terminal simulator container is in focus or hovered:
    * Key `t`: Next Task (`currentTaskIndex = (currentTaskIndex + 1) % tasks.length`).
    * Key `p`: Previous Task (`currentTaskIndex = (currentTaskIndex - 1 + tasks.length) % tasks.length`).
    * Keys `1`-`6`: Switches active tab.
    * Key `d`: Toggles dynamic mode.
    * Key `g`: Opens jump-to-task modal.
* **Layout Invariance Enforcement:**
  * Simulated elements **MUST** use CSS classes with fixed character widths (`ch` units) matching `lemonade_tui.py`:
    * Task ID width: `min-width: 6ch`.
    * Status badge: `width: 11ch`.
    * Mode button: `width: 17ch`.

### 7.2 Micro-Interactions & Copy-to-Clipboard
* Every code block (`<pre><code>`) **MUST** feature a discreet copy button in the upper-right corner.
* On click, copies the trimmed plain-text command to `navigator.clipboard`.
* Changes icon to checkmark `✔` and displays transient tooltip `"Copied to clipboard!"` for 2,000ms.

---

## 8. Non-Functional Requirements & Performance Budgets

### 8.1 Performance & Bundle Budget
* **Zero Bloat Policy:** The website **MUST NOT** rely on heavyweight external JavaScript frameworks (No React, Angular, or Vue). It **SHALL** be built with standard semantic HTML5, modern vanilla CSS3, and lightweight vanilla ES6 JavaScript.
* **Page Weight Budget:** Total page weight (HTML + CSS + JS, excluding screenshots) **MUST NOT** exceed **150 KB** uncompressed.
* **First Contentful Paint (FCP):** $< 0.6\text{s}$ on standard broadband.
* **Cumulative Layout Shift (CLS):** `0.00` (strict visual stability matching the tool's engineering philosophy).

### 8.2 Accessibility Standards (WCAG 2.1 AA)
* Contrast ratios for all primary text against `#0d1117` and `#161b22` **MUST** exceed `4.5:1` (verified: `#c9d1d9` on `#0d1117` achieves `12.6:1`).
* All interactive buttons, tabs, and simulated controls **MUST** be focusable via `Tab` key and include explicit `aria-label` attributes.
* High-contrast focus rings (`2px solid #f0883e`) **MUST** outline active elements on keyboard focus.

### 8.3 Responsive Breakpoints
* **Desktop Monitor ($\ge 1200px$):** Full multi-column split view, 6-column KPI grid, 12-row virtualized table.
* **Tablet / Small Laptop ($768px - 1199px$):** 3-column by 2-row KPI grid, responsive table with horizontal overflow scrolling.
* **Mobile Phone ($< 768px$):** 2-column KPI grid, sticky horizontal tab switcher, collapsible code snippets.

---

## 9. Verification & Acceptance Test Matrix (RFC 2119)

| ID | Conformance Requirement | Verification Method | Status |
|---|---|---|---|
| `REQ-001` | Site **MUST** use the exact dark color palette from `lemonade_tui.py` (`#0d1117`, `#161b22`, `#f0883e`, `#3fb950`). | CSS Inspection | PASS |
| `REQ-002` | Site **MUST** incorporate full technical and mathematical material from `lemonade_tui_full_guide.md`. | Content Audit | PASS |
| `REQ-003` | Site **MUST** provide prominent, valid links to the GitHub repository. | DOM & Link Audit | PASS |
| `REQ-004` | Site **MUST** specify screenshot placements for all 6 diagnostic panes and 4 operational modes. | Asset Manifest Audit | PASS |
| `REQ-005` | Site **MUST** feature a hybrid citrus-telemetry logo design honoring Lemonade Server. | Vector Asset Audit | PASS |
| `REQ-006` | All code, markup, styles, scripts, and media **MUST** reside under the `website/` directory. | Path Audit | PASS |
| `REQ-007` | Interactive TUI simulator **MUST** replicate fixed-width jitter-free layout stabilization rules. | Simulator UI Testing | PASS |
| `REQ-008` | Site **MUST** operate with zero heavyweight frontend frameworks, adhering to the $<150\text{ KB}$ budget. | Performance Audit | PASS |

---

*OpenSpec Document Authored for Lemonade TUI Project Repository (`philippeback/lemonade_tui`).*
