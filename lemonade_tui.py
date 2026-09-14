#!/usr/bin/env python3
"""
Lemonade Server Inference Telemetry & Analytics TUI
====================================================
A state-of-the-art Terminal User Interface (TUI) and visual analytics tool
for inspecting LLM inference speed, token allocation, context utilization,
and speculative decoding (Multi-Token Prediction - MTP) efficiency from Lemonade Server logs.

Usage:
  uv run python lemonade_tui.py                           # Interactive Textual TUI (defaults to lemonade-sample.log)
  uv run python lemonade_tui.py "$env:TEMP\\lemonade-server.log" # Inspect specific log file
  uv run python lemonade_tui.py --static [log_file]       # Render Rich terminal dashboard without full TUI
  uv run python lemonade_tui.py --all --static [log_file] # Render all tasks in terminal dashboard
  uv run python lemonade_tui.py --export report.md        # Export telemetry report to markdown
"""

import sys
import os
import re
import time
import argparse
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rich.console import Console, Group
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

# Textual imports
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.screen import ModalScreen
from textual.widgets import (
    Header, Footer, TabbedContent, TabPane, DataTable, Static,
    Label, Button, Markdown, Input
)
from textual.reactive import reactive
from textual.binding import Binding


# ==============================================================================
# Constants & Helpers
# ==============================================================================

# Fixed width formatting for task IDs to prevent top bar and UI layout jitter
TASK_ID_WIDTH = 6


def format_task_id(task_id: int, width: int = TASK_ID_WIDTH) -> str:
    """Format task ID with a fixed number of positions (minimum width) so UI elements stay stable."""
    return f"{task_id:<{width}}"


# ==============================================================================
# Data Models & Sequential Log Parser
# ==============================================================================

@dataclass
class PromptStep:
    timestamp: str
    n_tokens: int
    progress: float
    elapsed_s: float
    speed_tps: float


@dataclass
class GenStep:
    timestamp: str
    n_gen: int
    tg_tps: float
    tg_3s_tps: float


@dataclass
class TaskMetrics:
    task_id: int
    slot_id: int
    is_child: int = 0
    http_request_time: Optional[str] = None
    http_path: Optional[str] = None
    launch_time: Optional[str] = None

    # Prefill / Prompt Processing
    prompt_steps: List[PromptStep] = field(default_factory=list)
    prompt_eval_time_ms: Optional[float] = None
    prompt_tokens: Optional[int] = None
    prompt_ms_per_token: Optional[float] = None
    prompt_tps: Optional[float] = None

    # Generation / Decode
    gen_steps: List[GenStep] = field(default_factory=list)
    eval_time_ms: Optional[float] = None
    gen_tokens: Optional[int] = None
    eval_ms_per_token: Optional[float] = None
    eval_tps: Optional[float] = None

    # Totals
    total_time_ms: Optional[float] = None
    total_tokens: Optional[int] = None

    # Speculative Decoding / MTP
    graphs_reused: Optional[int] = None
    draft_acceptance_rate: Optional[float] = None
    draft_accepted: Optional[int] = None
    draft_generated: Optional[int] = None
    draft_mean_len: Optional[float] = None

    # Slot release & Context
    stop_tokens: Optional[int] = None
    truncated: Optional[int] = None
    lru_t_last: Optional[int] = None

    # Telemetry
    model: Optional[str] = None
    telemetry_tokens: Optional[int] = None
    telemetry_in: Optional[int] = None
    telemetry_out: Optional[int] = None
    ttft_s: Optional[float] = None
    final_tps: Optional[float] = None

    # Raw log lines
    raw_lines: List[str] = field(default_factory=list)

    # In-flight / Lifecycle status
    is_in_flight: bool = False
    is_aborted: bool = False

    @property
    def queue_delay_s(self) -> Optional[float]:
        """Time between HTTP request arrival and slot launch."""
        if not self.http_request_time or not self.launch_time:
            return None
        try:
            from datetime import datetime
            t0 = datetime.strptime(self.http_request_time, "%Y-%m-%d %H:%M:%S.%f")
            t1 = datetime.strptime(self.launch_time, "%Y-%m-%d %H:%M:%S.%f")
            diff = (t1 - t0).total_seconds()
            return diff if diff >= 0 else None
        except Exception:
            return None

    @property
    def end_to_end_tps(self) -> Optional[float]:
        """Total tokens divided by total wall-clock time in seconds."""
        if self.total_tokens and self.total_time_ms and self.total_time_ms > 0:
            return self.total_tokens / (self.total_time_ms / 1000.0)
        return None

    @property
    def draft_rejected(self) -> Optional[int]:
        if self.draft_generated is not None and self.draft_accepted is not None:
            return max(0, self.draft_generated - self.draft_accepted)
        return None

    @property
    def prompt_ratio(self) -> float:
        tot = (self.prompt_tokens or 0) + (self.gen_tokens or 0)
        return (self.prompt_tokens / tot * 100) if tot > 0 and self.prompt_tokens else 0.0

    @property
    def effective_gen_tokens(self) -> Optional[int]:
        if self.gen_tokens is not None:
            return self.gen_tokens
        if self.gen_steps:
            return self.gen_steps[-1].n_gen
        return None

    @property
    def effective_eval_tps(self) -> Optional[float]:
        if self.eval_tps is not None:
            return self.eval_tps
        if self.gen_steps:
            return self.gen_steps[-1].tg_3s_tps
        return None

    @property
    def effective_prompt_tokens(self) -> Optional[int]:
        if self.prompt_tokens is not None:
            return self.prompt_tokens
        if self.prompt_steps:
            return self.prompt_steps[-1].n_tokens
        return None

    @property
    def effective_prompt_tps(self) -> Optional[float]:
        if self.prompt_tps is not None:
            return self.prompt_tps
        if self.prompt_steps:
            return self.prompt_steps[-1].speed_tps
        return None

    @property
    def gen_ratio(self) -> float:
        tot = (self.prompt_tokens or 0) + (self.gen_tokens or 0)
        return (self.gen_tokens / tot * 100) if tot > 0 and self.gen_tokens else 0.0


class LemonadeLogParser:
    """
    Stateful, streamable parser for Lemonade Server logs.
    Supports incremental line feeding for real-time live telemetry tracking.
    """

    def __init__(self, filter_completed: bool = True):
        self.all_tasks: List[TaskMetrics] = []
        self.current_task: Optional[TaskMetrics] = None
        self.current_model: Optional[str] = None
        self.last_http_time: Optional[str] = None
        self.last_http_path: Optional[str] = None
        self.filter_completed = filter_completed

    def feed_line(self, line: str) -> bool:
        """
        Feed a single log line into the parser.
        Returns True if a task was created or updated.
        """
        line_clean = line.strip()
        if not line_clean:
            return False

        # Model detection
        m_model = re.search(r"(?:Model loaded successfully|Ensuring model loaded|Loading model):\s*([^\s,]+)", line_clean)
        if m_model:
            self.current_model = m_model.group(1).replace("user.", "")

        # HTTP request:
        http_m = re.search(r"([\d\-]+ [\d:.]+)\s+\[Info\]\s+\(Server\)\s+(?:POST|GET)\s+([^\s]+)", line_clean)
        if http_m:
            self.last_http_time = http_m.group(1)
            self.last_http_path = http_m.group(2)
            return False

        # Invalidate pending HTTP request and mark in-flight tasks aborted on model unload or reload
        if "load_model:" in line_clean or "Starting Lemonade" in line_clean or "Shutdown complete" in line_clean or "Unload model called" in line_clean:
            self.last_http_time = None
            self.last_http_path = None
            for t in self.all_tasks:
                if t.is_in_flight:
                    t.is_in_flight = False
                    t.is_aborted = True

        # Cancellation / client disconnect
        if "cancel task" in line_clean or "Client disconnected" in line_clean:
            if self.current_task and self.current_task.is_in_flight:
                self.current_task.is_in_flight = False
                self.current_task.is_aborted = True

        # Launch slot: slot launch_slot_: id  0 | task 5376 | processing task, is_child = 0
        launch_m = re.search(
            r"([\d\-]+ [\d:.]+).*slot launch_slot_:\s+id\s+(\d+)\s+\|\s+task\s+(\d+)\s+\|\s+processing task,\s+is_child\s+=\s+(\d+)",
            line_clean
        )
        if launch_m:
            # Mark any prior in-flight task as no longer in flight
            for t in self.all_tasks:
                if t.is_in_flight:
                    t.is_in_flight = False
                    if not (t.stop_tokens is not None or t.eval_time_ms is not None):
                        t.is_aborted = True

            ts = launch_m.group(1)
            slot_id = int(launch_m.group(2))
            task_id = int(launch_m.group(3))
            is_child = int(launch_m.group(4))

            task = TaskMetrics(task_id=task_id, slot_id=slot_id, is_child=is_child, launch_time=ts)
            task.model = self.current_model
            task.http_request_time = self.last_http_time
            task.http_path = self.last_http_path
            self.last_http_time = None
            self.last_http_path = None
            task.is_in_flight = True
            task.is_aborted = False
            task.raw_lines.append(line_clean)
            self.all_tasks.append(task)
            self.current_task = task
            return True

        # Task correlation from line
        task_match = re.search(r"task\s+(\d+)", line_clean)
        if task_match:
            tid = int(task_match.group(1))
            if self.current_task and self.current_task.task_id == tid:
                pass
            else:
                for past_task in reversed(self.all_tasks):
                    if past_task.task_id == tid:
                        self.current_task = past_task
                        break

        if self.current_task:
            self.current_task.raw_lines.append(line_clean)

        # Prompt processing progress
        p_step_m = re.search(
            r"([\d\-]+ [\d:.]+).*slot print_timing:.*prompt processing,\s+n_tokens\s+=\s+(\d+),\s+progress\s+=\s+([\d.]+),\s+t\s+=\s+([\d.]+)\s+s\s+/\s+([\d.]+)\s+tokens per second",
            line_clean
        )
        if p_step_m and self.current_task:
            self.current_task.prompt_steps.append(PromptStep(
                timestamp=p_step_m.group(1),
                n_tokens=int(p_step_m.group(2)),
                progress=float(p_step_m.group(3)),
                elapsed_s=float(p_step_m.group(4)),
                speed_tps=float(p_step_m.group(5))
            ))
            return True

        # Decode generation progress
        g_step_m = re.search(
            r"([\d\-]+ [\d:.]+).*slot print_timing:.*n_gen\s+=\s+(\d+),\s+tg\s+=\s+([\d.]+)\s+t/s,\s+tg_3s\s+=\s+([\d.]+)\s+t/s",
            line_clean
        )
        if g_step_m and self.current_task:
            self.current_task.gen_steps.append(GenStep(
                timestamp=g_step_m.group(1),
                n_gen=int(g_step_m.group(2)),
                tg_tps=float(g_step_m.group(3)),
                tg_3s_tps=float(g_step_m.group(4))
            ))
            return True

        # Prompt eval time summary
        p_eval_m = re.search(
            r"prompt eval time\s+=\s+([\d.]+)\s+ms\s+/\s+(\d+)\s+tokens\s+\(\s*([\d.]+)\s+ms per token,\s+([\d.]+)\s+tokens per second\)",
            line_clean
        )
        if p_eval_m and self.current_task:
            self.current_task.prompt_eval_time_ms = float(p_eval_m.group(1))
            self.current_task.prompt_tokens = int(p_eval_m.group(2))
            self.current_task.prompt_ms_per_token = float(p_eval_m.group(3))
            self.current_task.prompt_tps = float(p_eval_m.group(4))
            return True

        # Generation eval time summary
        eval_m = re.search(
            r"(?<!prompt )eval time\s+=\s+([\d.]+)\s+ms\s+/\s+(\d+)\s+tokens\s+\(\s*([\d.]+)\s+ms per token,\s+([\d.]+)\s+tokens per second\)",
            line_clean
        )
        if eval_m and self.current_task:
            self.current_task.is_in_flight = False
            self.current_task.is_aborted = False
            self.current_task.eval_time_ms = float(eval_m.group(1))
            self.current_task.gen_tokens = int(eval_m.group(2))
            self.current_task.eval_ms_per_token = float(eval_m.group(3))
            self.current_task.eval_tps = float(eval_m.group(4))
            return True

        # Total time summary
        tot_m = re.search(r"total time\s+=\s+([\d.]+)\s+ms\s+/\s+(\d+)\s+tokens", line_clean)
        if tot_m and self.current_task:
            self.current_task.total_time_ms = float(tot_m.group(1))
            self.current_task.total_tokens = int(tot_m.group(2))
            return True

        # Graphs reused
        gr_m = re.search(r"graphs reused\s+=\s+(\d+)", line_clean)
        if gr_m and self.current_task:
            self.current_task.graphs_reused = int(gr_m.group(1))
            return True

        # Draft acceptance (Speculative Decoding / MTP)
        draft_m = re.search(
            r"draft acceptance\s+=\s+([\d.]+)\s+\(\s*(\d+)\s+accepted\s+/\s*(\d+)\s+generated\),\s+mean len\s+=\s+([\d.]+)",
            line_clean
        )
        if draft_m and self.current_task:
            self.current_task.draft_acceptance_rate = float(draft_m.group(1))
            self.current_task.draft_accepted = int(draft_m.group(2))
            self.current_task.draft_generated = int(draft_m.group(3))
            self.current_task.draft_mean_len = float(draft_m.group(4))
            return True

        # Stop processing / Slot release
        stop_m = re.search(r"stop processing:\s+n_tokens\s+=\s+(\d+),\s+truncated\s+=\s+(\d+)", line_clean)
        if stop_m and self.current_task:
            self.current_task.is_in_flight = False
            self.current_task.is_aborted = False
            self.current_task.stop_tokens = int(stop_m.group(1))
            self.current_task.truncated = int(stop_m.group(2))
            return True

        # LRU eviction info
        lru_m = re.search(r"selected slot by LRU,\s+t_last\s+=\s+(\d+)", line_clean)
        if lru_m and self.current_task:
            self.current_task.lru_t_last = int(lru_m.group(1))
            return True

        # Telemetry summary
        telem_m = re.search(
            r"Inference completed:\s+model=([^,]+),\s+tokens=(\d+)\s+\(in=(\d+),\s+out=(\d+)\),\s+ttft=([\d.]+)s,\s+tps=([\d.]+)",
            line_clean
        )
        if telem_m:
            target_task = self.current_task
            if not target_task and self.all_tasks:
                target_task = self.all_tasks[-1]
            if target_task:
                target_task.is_in_flight = False
                target_task.is_aborted = False
                target_task.model = telem_m.group(1).strip()
                target_task.telemetry_tokens = int(telem_m.group(2))
                target_task.telemetry_in = int(telem_m.group(3))
                target_task.telemetry_out = int(telem_m.group(4))
                target_task.ttft_s = float(telem_m.group(5))
                target_task.final_tps = float(telem_m.group(6))
                if target_task.prompt_tokens is None:
                    target_task.prompt_tokens = target_task.telemetry_in
                if target_task.gen_tokens is None:
                    target_task.gen_tokens = target_task.telemetry_out
                if target_task.total_tokens is None:
                    target_task.total_tokens = target_task.telemetry_tokens
            return True

        return False

    def get_tasks(self) -> List[TaskMetrics]:
        if not self.filter_completed:
            return self.all_tasks

        # Keep tasks that have executed prompt or decode steps, telemetry records, or are in flight
        completed = [
            t for t in self.all_tasks
            if t.prompt_tokens is not None
            or t.gen_tokens is not None
            or t.total_tokens is not None
            or t.prompt_steps
            or t.gen_steps
            or t.telemetry_tokens is not None
            or t.is_in_flight
        ]
        return completed if completed else self.all_tasks


def parse_lemonade_log(file_path: str, filter_completed: bool = True) -> List[TaskMetrics]:
    """
    Parse a Lemonade server log file sequentially into structured TaskMetrics objects.
    Handles recurring task IDs, slot re-use, and multi-session logs.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file not found: {file_path}")

    parser = LemonadeLogParser(filter_completed=filter_completed)
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            parser.feed_line(line)

    return parser.get_tasks()


def parse_lemonade_log_with_parser(file_path: str, filter_completed: bool = True):
    """Parse log and return both the task list and the parser instance for efficient live tracking."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file not found: {file_path}")

    parser = LemonadeLogParser(filter_completed=filter_completed)
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            parser.feed_line(line)

    return parser.get_tasks(), parser


# ==============================================================================
# SOTA Rich Terminal Dashboard (Static Mode)
# ==============================================================================

def build_rich_dashboard_renderable(tasks: List[TaskMetrics], log_file: str, show_all: bool = False) -> Group:
    """Build a composable Rich renderable group for static and live streaming terminal displays."""
    items = []
    title_text = Text("[*] LEMONADE SERVER INFERENCE TELEMETRY & PERFORMANCE DASHBOARD", style="bold yellow")
    models_found = sorted(list(set(t.model for t in tasks if t.model)))
    model_summary = f"  |  Models: {', '.join(models_found[:3])}" if models_found else ""
    subtitle = Text(f"Log Source: {log_file}  |  Tasks Analyzed: {len(tasks)}{model_summary}", style="dim cyan")
    items.append(Panel(title_text + Text("\n") + subtitle, box=box.ROUNDED, border_style="yellow"))

    display_tasks = tasks if show_all or len(tasks) <= 5 else tasks[-5:]
    if not show_all and len(tasks) > 5:
        items.append(Text(f"Showing latest 5 of {len(tasks)} completed tasks. Use --all to display every task.\n", style="dim yellow"))

    for idx, t in enumerate(display_tasks, 1):
        task_title = f"Task #{format_task_id(t.task_id, TASK_ID_WIDTH)} (Slot {t.slot_id})"
        if t.is_child:
            task_title += " [Child Task]"

        summary_table = Table(box=box.SIMPLE_HEAVY, show_header=True, header_style="bold magenta")
        summary_table.add_column("Metric Group", style="cyan", width=22)
        summary_table.add_column("Key Indicator", style="white", width=26)
        summary_table.add_column("Observed Value", style="bold green", width=26)
        summary_table.add_column("Architectural Significance", style="dim", width=42)

        # Model & Engine
        summary_table.add_row(
            "Model & Engine",
            "Model Name",
            t.model or "Qwen-35B-MTP-GGUF",
            "Loaded model architecture & quantization"
        )
        if t.queue_delay_s is not None:
            summary_table.add_row(
                "Queue / Dispatch",
                "HTTP -> Slot Launch Delay",
                f"{t.queue_delay_s:.2f} s",
                "Time waiting in scheduling queue before slot allocation"
            )

        # Prefill Speed
        p_speed_str = f"{t.prompt_tps:.2f} t/s" if t.prompt_tps is not None else "N/A"
        if t.prompt_ms_per_token is not None:
            p_speed_str += f"  ({t.prompt_ms_per_token:.2f} ms/tok)"
        p_sig = (
            f"Time To First Token = {t.ttft_s:.2f}s across {t.prompt_tokens} tokens"
            if t.ttft_s is not None and t.prompt_tokens is not None
            else "Prompt ingestion latency"
        )
        summary_table.add_row("Speed: Prefill", "Prompt Throughput (TTFT)", p_speed_str, p_sig)

        # Decode Speed
        d_speed_str = f"{t.eval_tps:.2f} t/s" if t.eval_tps is not None else "N/A"
        if t.eval_ms_per_token is not None:
            d_speed_str += f"  ({t.eval_ms_per_token:.2f} ms/tok)"
        d_sig = (
            f"Autoregressive generation speed ({t.gen_tokens} tokens in {t.eval_time_ms/1000:.2f}s)"
            if t.gen_tokens is not None and t.eval_time_ms is not None
            else "Generation streaming throughput"
        )
        summary_table.add_row("Speed: Generation", "Decode Throughput (TPS)", d_speed_str, d_sig)

        # End-to-End Speed
        e2e_str = f"{t.end_to_end_tps:.2f} t/s" if t.end_to_end_tps is not None else "N/A"
        e2e_sig = (
            f"Total wall time: {t.total_time_ms/1000:.2f}s for {t.total_tokens} tokens"
            if t.total_time_ms is not None and t.total_tokens is not None
            else "Total request duration"
        )
        summary_table.add_row("Speed: End-to-End", "Overall Pipeline Speed", e2e_str, e2e_sig)

        # Token Allocation
        tok_str = (
            f"In: {t.prompt_tokens} ({t.prompt_ratio:.1f}%) | Out: {t.gen_tokens} ({t.gen_ratio:.1f}%)"
            if t.prompt_tokens is not None and t.gen_tokens is not None
            else f"Total tokens: {t.total_tokens or 'N/A'}"
        )
        summary_table.add_row(
            "Token Allocation",
            "Prompt vs Completion",
            tok_str,
            f"Total context footprint = {t.total_tokens or 'N/A'} tokens"
        )

        # Speculative MTP
        if t.draft_acceptance_rate is not None:
            summary_table.add_row(
                "Speculative MTP",
                "Draft Acceptance Rate",
                f"{t.draft_acceptance_rate*100:.2f}%  ({t.draft_accepted}/{t.draft_generated})",
                f"Multi-Token Prediction hit rate (Rejected: {t.draft_rejected})"
            )
            mean_len_str = f"{t.draft_mean_len:.2f} tokens / step" if t.draft_mean_len is not None else "N/A"
            speedup_str = f"Average tokens verified per step (~{t.draft_mean_len:.1f}x speedup)" if t.draft_mean_len else ""
            summary_table.add_row("Speculative MTP", "Mean Speculative Length", mean_len_str, speedup_str)

        # Context & Cache
        graph_str = f"{t.graphs_reused:,} executions" if t.graphs_reused is not None else "N/A"
        summary_table.add_row("Context & Cache", "Graphs Reused / Hit Count", graph_str, "CUDA/backend graph cache hits avoiding kernel launches")

        slot_str = f"{t.stop_tokens:,} tokens (Truncated: {t.truncated})" if t.stop_tokens is not None else "N/A"
        summary_table.add_row("Context & Cache", "Slot Retained Context", slot_str, "Total tokens active in slot KV cache at release")

        items.append(Panel(summary_table, title=f"📊 [bold cyan]Task: {task_title}[/bold cyan]", box=box.ROUNDED))

        # Prefill Table
        if t.prompt_steps:
            p_table = Table(title="⚡ Prompt Ingestion & Prefill Speed Scaling", box=box.SIMPLE, show_header=True)
            p_table.add_column("Step", justify="center", style="cyan")
            p_table.add_column("Tokens Processed", justify="right", style="green")
            p_table.add_column("Progress", justify="center")
            p_table.add_column("Elapsed Time", justify="right", style="yellow")
            p_table.add_column("Chunk Speed", justify="right", style="bold magenta")
            p_table.add_column("Speed Visual", justify="left")

            max_speed = max(s.speed_tps for s in t.prompt_steps) if t.prompt_steps else 1.0
            for s_idx, s in enumerate(t.prompt_steps, 1):
                bar_len = int((s.speed_tps / max_speed) * 20)
                bar = "█" * bar_len + "░" * (20 - bar_len)
                pct_bar = f"[{'■'*int(s.progress*10)}{' '*(10-int(s.progress*10))}] {s.progress*100:5.1f}%"
                p_table.add_row(
                    str(s_idx),
                    f"{s.n_tokens:,}",
                    pct_bar,
                    f"{s.elapsed_s:.2f} s",
                    f"{s.speed_tps:.2f} t/s",
                    f"[magenta]{bar}[/magenta]"
                )
            items.append(p_table)

        # Generation Table
        if t.gen_steps:
            g_table = Table(title="🚀 Token Generation Streaming Dynamics", box=box.SIMPLE, show_header=True)
            g_table.add_column("Step", justify="center", style="cyan")
            g_table.add_column("Tokens Emitted", justify="right", style="green")
            g_table.add_column("Cumulative Speed (tg)", justify="right", style="bold blue")
            g_table.add_column("Rolling 3s Speed (tg_3s)", justify="right", style="bold green")
            g_table.add_column("Rolling Throughput Bar", justify="left")

            max_tg3 = max(s.tg_3s_tps for s in t.gen_steps) if t.gen_steps else 1.0
            for g_idx, g in enumerate(t.gen_steps, 1):
                bar_len = int((g.tg_3s_tps / max_tg3) * 20)
                bar = "█" * bar_len + "░" * (20 - bar_len)
                g_table.add_row(
                    str(g_idx),
                    f"{g.n_gen:,}",
                    f"{g.tg_tps:.2f} t/s",
                    f"{g.tg_3s_tps:.2f} t/s",
                    f"[green]{bar}[/green]"
                )
            items.append(g_table)

    matrix_table = Table(
        title="🔍 WHAT IS POSSIBLE TO EXTRACT: SOTA Lemonade Telemetry Architecture",
        box=box.ROUNDED,
        header_style="bold yellow"
    )
    matrix_table.add_column("Dimension", style="bold cyan", width=16)
    matrix_table.add_column("Available Telemetry Metric", style="white", width=28)
    matrix_table.add_column("Formula / Derivation", style="dim", width=30)
    matrix_table.add_column("Production & Engineering Value", style="green", width=42)
    matrix_table.add_row("Prefill Scaling", "Prompt Throughput (t/s)\nPrompt Latency (ms/tok)", "tokens / prompt_eval_time\neval_time / tokens", "Detect quadratic attention scaling bottlenecks as prompts grow. Tune batch chunking and flash attention.")
    matrix_table.add_row("Decode Speed", "Steady-State TPS\nRolling tg_3s TPS", "n_gen / eval_time\nDelta n_gen / Delta 3s", "Monitor user-perceived streaming speed. Detect thermal throttling or GPU contention via tg_3s jitter.")
    matrix_table.add_row("Time To First Token", "TTFT (Seconds)\nQueue Scheduling Delay", "launch_time + prompt_eval_time\nlaunch_time - http_request_time", "Measure end-to-end interactive latency. Alert when scheduling queue times exceed SLAs.")
    matrix_table.add_row("Speculative MTP", "Draft Acceptance Rate (%)\nMean Speculative Length", "accepted / generated\naccepted_tokens / verification_step", "Evaluate Multi-Token Prediction (MTP) efficiency. Verify whether draft head accelerates decode or wastes FLOPs.")
    matrix_table.add_row("Context & Memory", "Slot Context Retention\nTruncation Status", "stop_processing n_tokens\ntruncated == 0", "Track KV cache memory allocation. Verify that requests fit context boundaries without silent truncation.")
    matrix_table.add_row("Hardware Acceleration", "Graphs Reused", "Count of graph cache hits", "Validates CUDA Graph / static runtime execution graph hits. Prevents recurring driver overhead.")
    items.append(matrix_table)

    return Group(*items)


def render_rich_dashboard(tasks: List[TaskMetrics], log_file: str, show_all: bool = False):
    """Render a comprehensive, beautiful Rich dashboard to stdout."""
    console = Console(legacy_windows=False)
    console.print()
    console.print(build_rich_dashboard_renderable(tasks, log_file, show_all=show_all))
    console.print()


def watch_rich_dashboard(log_file: str, show_all: bool = False, refresh_interval: float = 1.0):
    """Render and dynamically auto-refresh the Rich dashboard whenever new log lines arrive with near-zero overhead."""
    console = Console(legacy_windows=False)
    tasks, parser = parse_lemonade_log_with_parser(log_file)
    file_pos = os.path.getsize(log_file) if os.path.exists(log_file) else 0

    console.print(f"[bold cyan][*] Dynamic Live Dashboard active on: {log_file} (Press Ctrl+C to exit)...[/bold cyan]\n")
    with Live(build_rich_dashboard_renderable(tasks, log_file, show_all=show_all), console=console, refresh_per_second=2, screen=False) as live:
        try:
            while True:
                time.sleep(refresh_interval)
                if not os.path.exists(log_file):
                    continue
                cur_size = os.path.getsize(log_file)
                if cur_size != file_pos:
                    if cur_size < file_pos:
                        file_pos = 0
                        tasks, parser = parse_lemonade_log_with_parser(log_file)
                        file_pos = cur_size
                    else:
                        with open(log_file, "r", encoding="utf-8", errors="replace") as f:
                            f.seek(file_pos)
                            new_lines = f.readlines()
                            file_pos = f.tell()
                        updated = False
                        for line in new_lines:
                            if parser.feed_line(line):
                                updated = True
                        if updated:
                            tasks = parser.get_tasks()
                    live.update(build_rich_dashboard_renderable(tasks, log_file, show_all=show_all))
        except KeyboardInterrupt:
            pass


def print_capability_matrix(console: Console):
    """Print the architectural analysis of what is possible to get from Lemonade Server telemetry."""
    matrix_table = Table(
        title="🔍 WHAT IS POSSIBLE TO EXTRACT: SOTA Lemonade Telemetry Architecture",
        box=box.ROUNDED,
        header_style="bold yellow"
    )
    matrix_table.add_column("Dimension", style="bold cyan", width=16)
    matrix_table.add_column("Available Telemetry Metric", style="white", width=28)
    matrix_table.add_column("Formula / Derivation", style="dim", width=30)
    matrix_table.add_column("Production & Engineering Value", style="green", width=42)

    matrix_table.add_row(
        "Prefill Scaling",
        "Prompt Throughput (t/s)\nPrompt Latency (ms/tok)",
        "tokens / prompt_eval_time\neval_time / tokens",
        "Detect quadratic attention scaling bottlenecks as prompts grow. Tune batch chunking and flash attention."
    )
    matrix_table.add_row(
        "Decode Speed",
        "Steady-State TPS\nRolling tg_3s TPS",
        "n_gen / eval_time\nDelta n_gen / Delta 3s",
        "Monitor user-perceived streaming speed. Detect thermal throttling or GPU contention via tg_3s jitter."
    )
    matrix_table.add_row(
        "Time To First Token",
        "TTFT (Seconds)\nQueue Scheduling Delay",
        "launch_time + prompt_eval_time\nlaunch_time - http_request_time",
        "Measure end-to-end interactive latency. Alert when scheduling queue times exceed SLAs."
    )
    matrix_table.add_row(
        "Speculative MTP",
        "Draft Acceptance Rate (%)\nMean Speculative Length",
        "accepted / generated\naccepted_tokens / verification_step",
        "Evaluate Multi-Token Prediction (MTP) efficiency. Verify whether draft head accelerates decode or wastes FLOPs."
    )
    matrix_table.add_row(
        "Context & Memory",
        "Slot Context Retention\nTruncation Status",
        "stop_processing n_tokens\ntruncated == 0",
        "Track KV cache memory allocation. Verify that requests fit context boundaries without silent truncation."
    )
    matrix_table.add_row(
        "Hardware Acceleration",
        "Graphs Reused",
        "Count of graph cache hits",
        "Validates CUDA Graph / static runtime execution graph hits. Prevents recurring driver overhead."
    )

    console.print(matrix_table)
    console.print()


# ==============================================================================
# SOTA Textual Interactive TUI Application
# ==============================================================================

DOC_TEXT = """
# 🔍 What Is Possible to Extract: SOTA Telemetry Guide

The Lemonade server log exposes a rich set of operational, hardware, and algorithmic metrics that can be extracted for real-time monitoring, capacity planning, and SLA tracking:

### 1. Prefill Scaling & Attention Bottlenecks
* **Metrics:** Progressive chunk `tokens per second`, `progress` (0.0 to 1.0), `prompt eval time` (ms), `ms per token`.
* **Value:** Reveals quadratic attention slowdown as prompt length grows. In Task 5376, chunk throughput dropped from **813 t/s** (at 4K tokens) to **451 t/s** (at 13.4K tokens). Useful for tuning prompt chunk size (`n_batch`) and flash-attention parameters.

### 2. Decode Streaming Throughput & Jitter
* **Metrics:** Step-by-step `n_gen`, cumulative speed `tg`, rolling 3-second speed `tg_3s`.
* **Value:** The rolling `tg_3s` captures immediate generation throughput spikes (ranging between 52 t/s and 74 t/s in our sample), showing the real-time effect of speculative token verification.

### 3. Time To First Token (TTFT)
* **Metrics:** `prompt eval time` (ms) + `queue_delay_s`.
* **Value:** Crucial for user experience. For a 13.4K prompt, TTFT was **32.22 seconds** (~2.4s per 1K tokens), whereas a 1.4K prompt took **6.47 seconds**.

### 4. Speculative Decoding / Multi-Token Prediction (MTP)
* **Metrics:** `draft acceptance` rate, `accepted` vs `generated`, `mean len`.
* **Value:** Measures whether the speculative draft model or MTP heads are generating usable tokens. The observed **67.2% acceptance rate** with a **mean length of 3.02** delivers a near **3x decode speedup** over non-speculative autoregressive inference!

### 5. Execution Graph Reuse (CUDA Graph / Static Cache)
* **Metrics:** `graphs reused = 6849`.
* **Value:** High graph reuse demonstrates that the inference engine is capturing static computation graphs, avoiding driver launch latency and optimizing GPU memory bandwidth.

### 6. Slot & KV Cache Retention
* **Metrics:** `stop processing: n_tokens`, `truncated = 0`, `selected slot by LRU`.
* **Value:** Shows context memory utilization per slot, context cache reuse, and confirms that output was not truncated prematurely by hitting context boundaries.
"""


class JumpToTaskModal(ModalScreen[Optional[int]]):
    """Modal dialog for jumping directly to a task by its Task ID."""

    DEFAULT_CSS = """
    JumpToTaskModal {
        align: center middle;
    }
    #jump-dialog {
        width: 58;
        height: auto;
        background: #161b22;
        border: thick #58a6ff;
        padding: 1 2;
    }
    #jump-title {
        text-style: bold;
        color: #58a6ff;
        text-align: center;
        width: 100%;
        margin-bottom: 1;
    }
    #jump-info {
        color: #8b949e;
        text-align: center;
        width: 100%;
        margin-bottom: 1;
    }
    #jump-error {
        color: #f85149;
        text-align: center;
        width: 100%;
        margin-bottom: 1;
        display: none;
    }
    #task-id-input {
        width: 100%;
        margin-bottom: 1;
        background: #0d1117;
        border: tall #30363d;
    }
    #task-id-input:focus {
        border: tall #58a6ff;
    }
    #jump-btn-row {
        align: center middle;
        height: auto;
        width: 100%;
    }
    #jump-btn-row Button {
        min-width: 10;
        margin: 0 1;
    }
    """

    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=True),
    ]

    def __init__(self, tasks: List[TaskMetrics]):
        super().__init__()
        self.tasks = tasks

    def compose(self) -> ComposeResult:
        with Vertical(id="jump-dialog"):
            yield Label("🎯 Go to Task by ID", id="jump-title")
            if self.tasks:
                first_id = self.tasks[0].task_id
                last_id = self.tasks[-1].task_id
                if len(self.tasks) == 1:
                    info_text = f"Available ID: #{first_id} (1 task in log)"
                else:
                    info_text = f"Available IDs: #{first_id} ... #{last_id} ({len(self.tasks)} tasks in log)"
            else:
                info_text = "No tasks found in log"
            yield Label(info_text, id="jump-info")
            yield Label("", id="jump-error")
            yield Input(placeholder="Enter Task ID (e.g. 5376)", id="task-id-input", type="text")
            with Horizontal(id="jump-btn-row"):
                yield Button("Go [Enter]", id="btn-modal-go", variant="primary")
                yield Button("Cancel [Esc]", id="btn-modal-cancel", variant="default")

    def on_mount(self) -> None:
        self.query_one("#task-id-input", Input).focus()

    def action_cancel(self) -> None:
        self.dismiss(None)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-modal-go":
            self._submit()
        elif event.button.id == "btn-modal-cancel":
            self.dismiss(None)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "task-id-input":
            self._submit()

    def _submit(self) -> None:
        raw_val = self.query_one("#task-id-input", Input).value.strip()
        val = raw_val.lstrip("#").strip()
        err_lbl = self.query_one("#jump-error", Label)
        if not val:
            err_lbl.update("Please enter a Task ID")
            err_lbl.styles.display = "block"
            return
        try:
            target_id = int(val)
        except ValueError:
            err_lbl.update(f"Invalid Task ID: '{raw_val}' (must be a number)")
            err_lbl.styles.display = "block"
            return

        self.dismiss(target_id)


class LemonadeTUIApp(App):
    """Modern, SOTA Textual TUI Application for Lemonade Server telemetry inspection."""

    CSS = """
    Screen {
        background: #0d1117;
        color: #c9d1d9;
    }
    Header {
        background: #161b22;
        color: #f0883e;
        text-style: bold;
    }
    Footer {
        background: #161b22;
    }
    #kpi-strip {
        height: 5;
        margin: 1 1 0 1;
        layout: grid;
        grid-size: 6 1;
        grid-gutter: 1;
    }
    .kpi-card {
        background: #161b22;
        border: round #30363d;
        height: 100%;
        padding: 0 1;
        align: center middle;
    }
    .kpi-card-highlight {
        background: #1c2128;
        border: round #f0883e;
        height: 100%;
        padding: 0 1;
        align: center middle;
    }
    .kpi-title {
        color: #8b949e;
        text-align: center;
        text-style: bold;
    }
    .kpi-val {
        color: #58a6ff;
        text-align: center;
        text-style: bold;
    }
    .kpi-val-green {
        color: #3fb950;
        text-align: center;
        text-style: bold;
    }
    .kpi-val-orange {
        color: #d29922;
        text-align: center;
        text-style: bold;
    }
    #task-bar {
        margin: 0 1;
        height: 3;
        background: #161b22;
        border-bottom: solid #30363d;
        align: center middle;
    }
    #task-banner-label {
        min-width: 38;
    }
    #task-bar Button {
        min-width: 6;
        height: 3;
        margin: 0 1;
        padding: 0 1;
    }
    #btn-toggle-dynamic {
        width: 17;
        min-width: 17;
        max-width: 17;
    }
    #tab-container {
        margin: 0 1 1 1;
        height: 1fr;
    }
    #overview-pane-container {
        height: 1fr;
    }
    #overview-content-scroll {
        height: 1fr;
        min-height: 8;
        border-bottom: solid #30363d;
        margin-bottom: 1;
    }
    #overview-task-table {
        height: 12;
        min-height: 7;
        max-height: 16;
        border: round #30363d;
        background: #0d1117;
    }
    DataTable {
        height: auto;
        max-height: 16;
        border: round #30363d;
        background: #0d1117;
    }
    .text-dim {
        color: #8b949e;
    }
    .text-green {
        color: #3fb950;
        text-style: bold;
    }
    .text-yellow {
        color: #d29922;
        text-style: bold;
    }
    .text-blue {
        color: #58a6ff;
        text-style: bold;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("home", "first_task", "Start", show=True),
        Binding("p", "prev_task", "Prev", show=True),
        Binding("t", "next_task", "Next", show=True),
        Binding("end", "last_task", "End", show=True),
        Binding("g", "goto_task", "Go to #", show=True),
        Binding("d", "toggle_dynamic", "Dynamic/Static", show=True),
        Binding("r", "refresh_data", "Refresh", show=True),
        Binding("1", "tab_overview", "Overview", show=True),
        Binding("2", "tab_speed", "Speed", show=True),
        Binding("3", "tab_tokens", "Tokens", show=True),
        Binding("4", "tab_context", "Context", show=True),
        Binding("5", "tab_matrix", "Telemetry Matrix", show=True),
        Binding("6", "tab_raw", "Raw Log", show=True),
    ]

    current_task_idx = reactive(0)
    dynamic_mode = reactive(True)

    def __init__(self, tasks: List[TaskMetrics], log_file: str, parser: Optional[LemonadeLogParser] = None, dynamic_mode: bool = True, initial_task_idx: Optional[int] = None):
        super().__init__()
        self.tasks = tasks
        self.log_file = log_file
        self.parser = parser or LemonadeLogParser(filter_completed=True)
        self.dynamic_mode = dynamic_mode
        self.initial_task_idx = initial_task_idx
        self.file_pos = os.path.getsize(log_file) if os.path.exists(log_file) else 0
        self._populating_table = False
        self._syncing_cursor = False
        self._highlight_timer = None
        self._pending_task_idx = None
        self.poller_timer = None
        self.task_id_width = max(TASK_ID_WIDTH, max((len(str(t.task_id)) for t in self.tasks), default=TASK_ID_WIDTH))
        if not parser and os.path.exists(log_file):
            with open(log_file, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    self.parser.feed_line(line)

    @property
    def active_task(self) -> Optional[TaskMetrics]:
        if not self.tasks:
            return None
        return self.tasks[self.current_task_idx % len(self.tasks)]

    def get_dynamic_btn_label(self) -> str:
        return "● Dynamic [d]" if self.dynamic_mode else "⏸ Static  [d]"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        # Task Navigation Banner
        with Horizontal(id="task-bar"):
            yield Label(f"Log: {os.path.basename(self.log_file)}  |  ", classes="text-dim")
            yield Label(self.get_task_banner_text(), id="task-banner-label")
            yield Button("|◀ Start", id="btn-start-task", variant="default")
            yield Button("◀ Prev [p]", id="btn-prev-task", variant="default")
            yield Button("Next [t] ▶", id="btn-next-task", variant="primary")
            yield Button("End ▶|", id="btn-end-task", variant="default")
            yield Button("Go to # [g]", id="btn-goto-task", variant="default")
            yield Button(self.get_dynamic_btn_label(), id="btn-toggle-dynamic", variant="success" if self.dynamic_mode else "warning")

        # Top KPI Summary Strip
        with Container(id="kpi-strip"):
            with Vertical(classes="kpi-card-highlight", id="kpi-1"):
                yield Label("ACTIVE TASK", classes="kpi-title")
                yield Label("--", classes="kpi-val", id="val-task")

            with Vertical(classes="kpi-card", id="kpi-2"):
                yield Label("DECODE SPEED", classes="kpi-title")
                yield Label("--", classes="kpi-val-green", id="val-decode")

            with Vertical(classes="kpi-card", id="kpi-3"):
                yield Label("PREFILL (TTFT)", classes="kpi-title")
                yield Label("--", classes="kpi-val", id="val-prefill")

            with Vertical(classes="kpi-card", id="kpi-4"):
                yield Label("TOKENS (IN/OUT)", classes="kpi-title")
                yield Label("--", classes="kpi-val-orange", id="val-tokens")

            with Vertical(classes="kpi-card", id="kpi-5"):
                yield Label("MTP SPECULATION", classes="kpi-title")
                yield Label("--", classes="kpi-val-green", id="val-mtp")

            with Vertical(classes="kpi-card", id="kpi-6"):
                yield Label("GRAPH REUSE", classes="kpi-title")
                yield Label("--", classes="kpi-val", id="val-graph")

        # Tabbed View Container
        with TabbedContent(id="tab-container"):
            # Tab 1: Overview
            with TabPane("1: Overview", id="tab-overview"):
                with Vertical(id="overview-pane-container"):
                    with VerticalScroll(id="overview-content-scroll"):
                        yield Static(id="overview-content")
                    yield Label("📋 All Tasks (Click or Enter to select | [t]/[p] Next/Prev | [Home]/[End] Start/End | [g] Go to ID | [d] Live)", classes="text-yellow", id="table-header-label")
                    yield DataTable(id="overview-task-table")

            # Tab 2: Speed & Throughput
            with TabPane("2: Speed & Throughput", id="tab-speed"):
                with VerticalScroll():
                    yield Label("⚡ Prompt Processing (Prefill) Progressive Throughput", classes="text-blue")
                    yield DataTable(id="prefill-table")
                    yield Label("🚀 Token Generation (Decode) Streaming Throughput", classes="text-green")
                    yield DataTable(id="gen-table")

            # Tab 3: Tokens & MTP Speculation
            with TabPane("3: Tokens & MTP", id="tab-tokens"):
                with VerticalScroll():
                    yield Static(id="tokens-content")

            # Tab 4: Context & Slot Allocation
            with TabPane("4: Context & Slots", id="tab-context"):
                with VerticalScroll():
                    yield Static(id="context-content")

            # Tab 5: Telemetry Capability Matrix
            with TabPane("5: Telemetry Matrix", id="tab-matrix"):
                with VerticalScroll():
                    yield Markdown(DOC_TEXT, id="matrix-markdown")

            # Tab 6: Raw Log Lines
            with TabPane("6: Raw Log", id="tab-raw"):
                with VerticalScroll():
                    yield Static(id="raw-log-content")

        yield Footer()

    def get_task_banner_text(self) -> str:
        if not self.tasks:
            return "No tasks found"
        t = self.active_task
        if not t:
            return "No tasks found"
        if t.is_in_flight:
            status = "[bold yellow]● IN-FLIGHT[/bold yellow]"
        elif t.is_aborted:
            status = "[bold red]✖ ABORTED  [/bold red]"
        else:
            status = "[bold green]✔ DONE     [/bold green]"
        w = getattr(self, "task_id_width", TASK_ID_WIDTH)
        tid_str = format_task_id(t.task_id, w)
        idx_w = len(str(len(self.tasks)))
        return f"Task #{tid_str} (Slot {t.slot_id}) {status} [{self.current_task_idx + 1:>{idx_w}}/{len(self.tasks)}]"

    OVERVIEW_COLS = [
        ("Task ID", "task_id"),
        ("Model", "model"),
        ("Prompt In", "prompt_in"),
        ("Gen Out", "gen_out"),
        ("Prefill t/s", "prefill_tps"),
        ("TTFT", "ttft"),
        ("Decode t/s", "decode_tps"),
        ("MTP Acc", "mtp_acc"),
        ("Mean Len", "mean_len"),
        ("Graphs", "graphs"),
    ]

    def _format_task_row(self, t: TaskMetrics) -> tuple:
        p_in = f"{t.prompt_tokens:,}" if t.prompt_tokens is not None else (f"{t.prompt_steps[-1].n_tokens:,}*" if t.prompt_steps else "-")
        g_out = f"{t.gen_tokens:,}" if t.gen_tokens is not None else (f"{t.gen_steps[-1].n_gen:,}*" if t.gen_steps else "-")
        p_tps = f"{t.prompt_tps:.1f}" if t.prompt_tps is not None else (f"{t.prompt_steps[-1].speed_tps:.1f}*" if t.prompt_steps else "-")
        ttft = f"{t.ttft_s:.2f}s" if t.ttft_s is not None else "-"
        if t.eval_tps is not None:
            d_tps = f"{t.eval_tps:.1f}"
        elif t.gen_steps:
            d_tps = f"{t.gen_steps[-1].tg_3s_tps:.1f}*"
        elif t.is_in_flight:
            d_tps = "eval..."
        elif t.is_aborted:
            d_tps = "aborted"
        else:
            d_tps = "-"

        if t.draft_acceptance_rate is not None:
            mtp = f"{t.draft_acceptance_rate*100:.1f}%"
        elif t.is_in_flight:
            mtp = "in-flight"
        elif t.is_aborted:
            mtp = "aborted"
        else:
            mtp = "-"

        mlen = f"{t.draft_mean_len:.2f}" if t.draft_mean_len is not None else "-"
        gr = f"{t.graphs_reused:,}" if t.graphs_reused is not None else "-"
        m_name = (t.model[:22] + "...") if t.model and len(t.model) > 25 else (t.model or "Unknown Model")
        if t.is_in_flight:
            status_prefix = "⚡"
        elif t.is_aborted:
            status_prefix = "✖"
        else:
            status_prefix = "#"

        w = getattr(self, "task_id_width", TASK_ID_WIDTH)
        task_label = f"{status_prefix}{format_task_id(t.task_id, w)}"
        return (task_label, m_name, p_in, g_out, p_tps, ttft, d_tps, mtp, mlen, gr)

    def on_mount(self) -> None:
        self.title = "Lemonade Server Telemetry & Inference Analytics"
        # Auto-focus the requested initial task or latest task on start
        if self.tasks:
            if self.initial_task_idx is not None and 0 <= self.initial_task_idx < len(self.tasks):
                self.current_task_idx = self.initial_task_idx
            else:
                self.current_task_idx = len(self.tasks) - 1

        self.init_overview_task_table()
        self.init_speed_tables()
        self.update_active_view()
        self.poller_timer = self.set_interval(1.5, self.poll_log_updates)

    def init_overview_task_table(self) -> None:
        self._populating_table = True
        try:
            table = self.query_one("#overview-task-table", DataTable)
            table.cursor_type = "row"
            table.clear(columns=True)
            for label, col_key in self.OVERVIEW_COLS:
                table.add_column(label, key=col_key)

            for idx, t in enumerate(self.tasks):
                table.add_row(*self._format_task_row(t), key=str(idx))

            if table.row_count > 0 and 0 <= self.current_task_idx < table.row_count:
                table.move_cursor(row=self.current_task_idx)
        finally:
            self._populating_table = False

    def init_speed_tables(self) -> None:
        pt = self.query_one("#prefill-table", DataTable)
        pt.clear(columns=True)
        pt.add_columns("Step", "Tokens", "Progress", "Elapsed", "Speed (t/s)", "Relative Speed Bar")

        gt = self.query_one("#gen-table", DataTable)
        gt.clear(columns=True)
        gt.add_columns("Step", "Tokens Gen", "Cumulative tg (t/s)", "Rolling tg_3s (t/s)", "Throughput Bar")

    def poll_log_updates(self, force: bool = False) -> None:
        if not self.dynamic_mode and not force:
            return
        if not os.path.exists(self.log_file):
            return
        try:
            cur_size = os.path.getsize(self.log_file)
            if cur_size == self.file_pos:
                return

            if cur_size < self.file_pos:
                self.file_pos = 0
                self.parser = LemonadeLogParser(filter_completed=True)
                with open(self.log_file, "r", encoding="utf-8", errors="replace") as f:
                    for line in f:
                        self.parser.feed_line(line)
                self.file_pos = cur_size
                self.tasks = self.parser.get_tasks()
                self.current_task_idx = max(0, len(self.tasks) - 1)
                self.init_overview_task_table()
                self.update_active_view()
                return

            with open(self.log_file, "r", encoding="utf-8", errors="replace") as f:
                f.seek(self.file_pos)
                new_lines = f.readlines()
                self.file_pos = f.tell()

            if not new_lines:
                return

            old_count = len(self.tasks)
            updated = False
            for line in new_lines:
                if self.parser.feed_line(line):
                    updated = True

            self.tasks = self.parser.get_tasks()
            new_count = len(self.tasks)
            if self.tasks:
                self.task_id_width = max(self.task_id_width, max(len(str(t.task_id)) for t in self.tasks))

            table = self.query_one("#overview-task-table", DataTable)

            if new_count > old_count:
                self._populating_table = True
                try:
                    for idx in range(old_count, new_count):
                        table.add_row(*self._format_task_row(self.tasks[idx]), key=str(idx))
                finally:
                    self._populating_table = False

                if self.current_task_idx >= old_count - 1:
                    self._switch_to_task_idx(new_count - 1, from_table=False)
                else:
                    self.update_active_view()

            elif updated and self.tasks:
                last_idx = len(self.tasks) - 1
                row_vals = self._format_task_row(self.tasks[last_idx])
                for (_, col_key), val in zip(self.OVERVIEW_COLS, row_vals):
                    try:
                        table.update_cell(str(last_idx), col_key, val)
                    except Exception:
                        pass

                if self.current_task_idx == last_idx:
                    self.update_active_view()

        except Exception:
            pass

    def action_first_task(self) -> None:
        if self.tasks:
            self._switch_to_task_idx(0, from_table=False)
            self.notify(f"Jumped to Start: Task #{self.tasks[0].task_id} [1/{len(self.tasks)}]", timeout=1.5)

    def action_last_task(self) -> None:
        if self.tasks:
            last_idx = len(self.tasks) - 1
            self._switch_to_task_idx(last_idx, from_table=False)
            self.notify(f"Jumped to End: Task #{self.tasks[last_idx].task_id} [{len(self.tasks)}/{len(self.tasks)}]", timeout=1.5)

    def action_next_task(self) -> None:
        if self.tasks:
            new_idx = (self.current_task_idx + 1) % len(self.tasks)
            self._switch_to_task_idx(new_idx, from_table=False)

    def action_prev_task(self) -> None:
        if self.tasks:
            new_idx = (self.current_task_idx - 1) % len(self.tasks)
            self._switch_to_task_idx(new_idx, from_table=False)

    def action_goto_task(self) -> None:
        if not self.tasks:
            self.notify("No tasks found in log", severity="warning", timeout=2.0)
            return
        self.push_screen(JumpToTaskModal(self.tasks), self._handle_jump_task_result)

    def _handle_jump_task_result(self, target_id: Optional[int]) -> None:
        if target_id is None or not self.tasks:
            return

        # 1. Match exact task_id
        for idx, t in enumerate(self.tasks):
            if t.task_id == target_id:
                self._switch_to_task_idx(idx, from_table=False)
                self.notify(f"Jumped to Task #{target_id} [{idx + 1}/{len(self.tasks)}]", timeout=2.0)
                return

        # 2. Fallback: match 1-based index (e.g. 1 for first task)
        if 1 <= target_id <= len(self.tasks):
            idx = target_id - 1
            matched = self.tasks[idx]
            self._switch_to_task_idx(idx, from_table=False)
            self.notify(
                f"Task ID #{target_id} not found; jumped to index [{target_id}/{len(self.tasks)}] (Task #{matched.task_id})",
                timeout=3.0,
            )
            return

        self.notify(f"Task ID #{target_id} not found in {len(self.tasks)} tasks", severity="error", timeout=2.5)

    def action_toggle_dynamic(self) -> None:
        self.dynamic_mode = not self.dynamic_mode
        if self.dynamic_mode:
            self.poll_log_updates(force=True)
            self.notify("DYNAMIC mode active: Live log tailing enabled", timeout=2.0)
        else:
            self.notify("STATIC mode active: Background polling paused", timeout=2.0)
        self.update_active_view()
        try:
            btn = self.query_one("#btn-toggle-dynamic", Button)
            btn.label = self.get_dynamic_btn_label()
            btn.variant = "success" if self.dynamic_mode else "warning"
        except Exception:
            pass

    def action_refresh_data(self) -> None:
        self.poll_log_updates(force=True)
        self.notify("Telemetry snapshot refreshed from log", timeout=1.5)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-start-task":
            self.action_first_task()
        elif event.button.id == "btn-prev-task":
            self.action_prev_task()
        elif event.button.id == "btn-next-task":
            self.action_next_task()
        elif event.button.id == "btn-end-task":
            self.action_last_task()
        elif event.button.id == "btn-goto-task":
            self.action_goto_task()
        elif event.button.id == "btn-toggle-dynamic":
            self.action_toggle_dynamic()

    def _sync_table_cursor_to_current(self) -> None:
        try:
            table = self.query_one("#overview-task-table", DataTable)
            if table.row_count > 0 and 0 <= self.current_task_idx < table.row_count:
                if table.cursor_row != self.current_task_idx:
                    self._syncing_cursor = True
                    try:
                        table.move_cursor(row=self.current_task_idx)
                    finally:
                        self._syncing_cursor = False
        except Exception:
            pass

    def _switch_to_task_idx(self, idx: int, from_table: bool = False) -> None:
        if not self.is_mounted or getattr(self, "_populating_table", False):
            return
        if 0 <= idx < len(self.tasks):
            if idx == self.current_task_idx and from_table:
                return
            self.current_task_idx = idx
            if not from_table:
                self._sync_table_cursor_to_current()
            self.update_active_view()

    def on_data_table_row_highlighted(self, event: DataTable.RowHighlighted) -> None:
        if event.data_table.id != "overview-task-table":
            return
        if getattr(self, "_populating_table", False) or getattr(self, "_syncing_cursor", False):
            return
        try:
            idx = int(event.row_key.value)
        except (ValueError, TypeError, AttributeError):
            idx = event.cursor_row

        if idx == self.current_task_idx:
            return

        self._pending_task_idx = idx
        timer = getattr(self, "_highlight_timer", None)
        if timer is not None:
            timer.stop()
        self._highlight_timer = self.set_timer(0.06, self._apply_debounced_task_switch)

    def _apply_debounced_task_switch(self) -> None:
        idx = getattr(self, "_pending_task_idx", None)
        if idx is not None and idx != self.current_task_idx:
            self._switch_to_task_idx(idx, from_table=True)

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        if event.data_table.id != "overview-task-table":
            return
        if getattr(self, "_populating_table", False) or getattr(self, "_syncing_cursor", False):
            return
        timer = getattr(self, "_highlight_timer", None)
        if timer is not None:
            timer.stop()
            self._highlight_timer = None
        try:
            idx = int(event.row_key.value)
        except (ValueError, TypeError, AttributeError):
            idx = event.cursor_row
        self._switch_to_task_idx(idx, from_table=True)

    def on_tabbed_content_tab_activated(self, event: TabbedContent.TabActivated) -> None:
        self.update_active_view()

    def action_tab_overview(self) -> None:
        self.query_one(TabbedContent).active = "tab-overview"

    def action_tab_speed(self) -> None:
        self.query_one(TabbedContent).active = "tab-speed"

    def action_tab_tokens(self) -> None:
        self.query_one(TabbedContent).active = "tab-tokens"

    def action_tab_context(self) -> None:
        self.query_one(TabbedContent).active = "tab-context"

    def action_tab_matrix(self) -> None:
        self.query_one(TabbedContent).active = "tab-matrix"

    def action_tab_raw(self) -> None:
        self.query_one(TabbedContent).active = "tab-raw"

    def update_active_view(self) -> None:
        t = self.active_task
        if not t:
            return

        try:
            banner_lbl = self.query_one("#task-banner-label", Label)
        except Exception:
            return

        banner_lbl.update(self.get_task_banner_text())

        # 1. Active Task (18 chars constant)
        tag = " ●" if t.is_in_flight else (" ✖" if t.is_aborted else "  ")
        h_tid = f"#{t.task_id}"
        self.query_one("#val-task", Label).update(f"{h_tid:>7} (Slot {t.slot_id}){tag}")

        # 2. Decode Speed (19 chars constant)
        if t.eval_tps is not None and t.eval_ms_per_token is not None:
            ms_str = f"{t.eval_ms_per_token:>5.1f}ms" if t.eval_ms_per_token < 100 else f"{t.eval_ms_per_token:>5.0f}ms"
            decode_str = f"{t.eval_tps:>5.1f} t/s ({ms_str})"
        elif t.eval_tps is not None:
            decode_str = f"{t.eval_tps:>5.1f} t/s          "
        elif t.gen_steps:
            decode_str = f"{t.gen_steps[-1].tg_3s_tps:>5.1f} t/s  (live)  "
        elif t.is_aborted:
            decode_str = f"{'Aborted':^19}"
        else:
            decode_str = f"{'Waiting...':^19}" if t.is_in_flight else f"{'N/A':^19}"
        self.query_one("#val-decode", Label).update(decode_str)

        # 3. Prefill (TTFT) (16 chars constant)
        if t.prompt_tps is not None and t.ttft_s is not None:
            prefill_str = f"{int(t.prompt_tps):>4} t/s ({t.ttft_s:>4.1f}s)"
        elif t.prompt_tps is not None:
            prefill_str = f"{int(t.prompt_tps):>4} t/s        "
        elif t.prompt_steps:
            prefill_str = f"{int(t.prompt_steps[-1].speed_tps):>4} t/s (live)"
        else:
            prefill_str = f"{'N/A':^16}"
        self.query_one("#val-prefill", Label).update(prefill_str)

        # 4. Tokens (In/Out) (19 chars constant)
        p_in = t.prompt_tokens or (t.prompt_steps[-1].n_tokens if t.prompt_steps else None)
        g_out = t.gen_tokens or (t.gen_steps[-1].n_gen if t.gen_steps else None)
        if p_in is not None and g_out is not None:
            tok_str = f"In:{p_in:>5} / Out:{g_out:>4}"
        elif p_in is not None or g_out is not None:
            tok_str = f"In:{p_in or 0:>5} / Out:{g_out or 0:>4}"
        else:
            tok_str = f"{'N/A':^19}"
        self.query_one("#val-tokens", Label).update(tok_str)

        # 5. MTP Speculation (17 chars constant)
        if t.draft_acceptance_rate is not None and t.draft_mean_len is not None:
            mtp_str = f"{t.draft_acceptance_rate*100:>5.1f}% (len {t.draft_mean_len:>4.2f})"
        elif t.is_in_flight:
            mtp_str = f"{'in-flight':^17}"
        elif t.is_aborted:
            mtp_str = f"{'aborted':^17}"
        else:
            mtp_str = f"{'N/A':^17}"
        self.query_one("#val-mtp", Label).update(mtp_str)

        # 6. Graph Reuse (12 chars constant)
        if t.graphs_reused is not None:
            graph_str = f"{t.graphs_reused:>7,} hits"
        else:
            graph_str = f"{'N/A':^12}"
        self.query_one("#val-graph", Label).update(graph_str)

        # Lazy rendering: only refresh the active tab!
        try:
            active_tab = self.query_one(TabbedContent).active
        except Exception:
            active_tab = "tab-overview"

        if active_tab == "tab-overview":
            self.render_overview_pane(t)
        elif active_tab == "tab-speed":
            self.render_speed_tables(t)
        elif active_tab == "tab-tokens":
            self.render_tokens_pane(t)
        elif active_tab == "tab-context":
            self.render_context_pane(t)
        elif active_tab == "tab-raw":
            self.render_raw_pane(t)

    def render_raw_pane(self, t: TaskMetrics) -> None:
        raw_text = "\n".join(t.raw_lines) if t.raw_lines else "No raw lines recorded."
        self.query_one("#raw-log-content", Static).update(Panel(raw_text, title=f"Raw Log Lines (Task {t.task_id})", border_style="dim"))

    def render_overview_pane(self, t: TaskMetrics) -> None:
        text = Text()
        text.append(f"Model: {t.model or 'Unknown Model'}\n", style="bold yellow")
        w = getattr(self, "task_id_width", TASK_ID_WIDTH)
        text.append(f"Task ID: {format_task_id(t.task_id, w)}  |  Slot ID: {t.slot_id}  |  Child Task: {bool(t.is_child)}\n", style="cyan")
        text.append(f"HTTP Arrival: {t.http_request_time or 'N/A'}  |  Slot Launch: {t.launch_time or 'N/A'}\n\n", style="dim")

        if t.is_in_flight:
            text.append("CURRENT STATUS: ● IN-FLIGHT (STREAMING LIVE)\n", style="bold yellow")
            if t.gen_steps:
                latest_g = t.gen_steps[-1]
                text.append(f"  • Emitted {latest_g.n_gen} tokens so far | Current rolling speed: {latest_g.tg_3s_tps:.1f} t/s\n\n", style="green")
            elif t.prompt_steps:
                latest_p = t.prompt_steps[-1]
                text.append(f"  • Ingesting prompt: {latest_p.progress*100:.1f}% ({latest_p.n_tokens} tokens) @ {latest_p.speed_tps:.1f} t/s\n\n", style="yellow")
            else:
                text.append("  • Slot launched, awaiting initial token batch...\n\n", style="dim")
        elif t.is_aborted:
            text.append("CURRENT STATUS: ✖ ABORTED / CANCELLED\n", style="bold red")
            text.append("  • Inference stopped prematurely before completion (model unloaded or client disconnected).\n\n", style="dim")

        # Phase Timeline Bar
        text.append("REQUEST LIFECYCLE PHASES\n", style="bold white")
        q_time = t.queue_delay_s or 0.0
        p_time = (t.prompt_eval_time_ms or 0.0) / 1000.0
        d_time = (t.eval_time_ms or 0.0) / 1000.0
        tot_time = q_time + p_time + d_time

        if tot_time > 0:
            total_bar_width = 44
            q_bar = int((q_time / tot_time) * total_bar_width)
            if q_time > 0 and q_bar == 0:
                q_bar = 1
            p_bar = int((p_time / tot_time) * total_bar_width)
            if p_time > 0 and p_bar == 0:
                p_bar = 1
            d_bar = max(1, total_bar_width - q_bar - p_bar) if d_time > 0 else 0

            if q_bar > 0:
                text.append("█" * q_bar, style="bold red")
            if p_bar > 0:
                text.append("█" * p_bar, style="bold yellow")
            if d_bar > 0:
                text.append("█" * d_bar, style="bold green")
            text.append("\n")

            text.append("  ■ Queue Wait: ", style="bold red")
            text.append(f"{q_time:.2f}s ({q_time/tot_time*100:.1f}%)    ", style="white")
            text.append("■ Prefill (TTFT): ", style="bold yellow")
            text.append(f"{p_time:.2f}s ({p_time/tot_time*100:.1f}%)    ", style="white")
            text.append("■ Decode: ", style="bold green")
            text.append(f"{d_time:.2f}s ({d_time/tot_time*100:.1f}%)\n\n", style="white")

        self.query_one("#overview-content", Static).update(text)

    def render_speed_tables(self, t: TaskMetrics) -> None:
        pt = self.query_one("#prefill-table", DataTable)
        pt.clear()
        if t.prompt_steps:
            max_ps = max((s.speed_tps for s in t.prompt_steps), default=1.0)
            rows_pt = []
            for idx, s in enumerate(t.prompt_steps, 1):
                bar = "█" * int((s.speed_tps / max_ps) * 20)
                rows_pt.append((str(idx), f"{s.n_tokens:,}", f"{s.progress * 100:.1f}%", f"{s.elapsed_s:.2f} s", f"{s.speed_tps:.2f}", bar))
            pt.add_rows(rows_pt)

        gt = self.query_one("#gen-table", DataTable)
        gt.clear()
        if t.gen_steps:
            max_gs = max((s.tg_3s_tps for s in t.gen_steps), default=1.0)
            rows_gt = []
            for idx, s in enumerate(t.gen_steps, 1):
                bar = "█" * int((s.tg_3s_tps / max_gs) * 20)
                rows_gt.append((str(idx), f"{s.n_gen:,}", f"{s.tg_tps:.2f}", f"{s.tg_3s_tps:.2f}", bar))
            gt.add_rows(rows_gt)

    def render_tokens_pane(self, t: TaskMetrics) -> None:
        p_in = t.prompt_tokens or (t.prompt_steps[-1].n_tokens if t.prompt_steps else 0)
        g_out = t.gen_tokens or (t.gen_steps[-1].n_gen if t.gen_steps else 0)
        tot = t.total_tokens or (p_in + g_out)

        in_pct = (p_in / tot * 100) if tot > 0 else 0
        out_pct = (g_out / tot * 100) if tot > 0 else 0

        total_bar_width = 44
        bar_in = int((in_pct / 100) * total_bar_width) if in_pct > 0 else 0
        if p_in > 0 and bar_in == 0:
            bar_in = 1
        bar_out = max(1, total_bar_width - bar_in) if g_out > 0 else 0

        text = Text()
        text.append("TOKEN ALLOCATION & RATIO\n", style="bold white")
        if bar_in > 0:
            text.append("█" * bar_in, style="bold yellow")
        if bar_out > 0:
            text.append("█" * bar_out, style="bold green")
        text.append("\n")

        text.append("  ■ Prompt Input:     ", style="bold yellow")
        text.append(f"{p_in:,} tokens ({in_pct:.1f}%)\n", style="white")
        text.append("  ■ Completion Output:", style="bold green")
        text.append(f"{g_out:,} tokens ({out_pct:.1f}%)\n", style="white")
        text.append("  ■ Total Context:    ", style="bold cyan")
        text.append(f"{tot:,} tokens\n\n", style="bold white")

        if t.draft_acceptance_rate is not None:
            text.append("SPECULATIVE DECODING & MULTI-TOKEN PREDICTION (MTP)\n", style="bold white")
            text.append(f"• Draft Acceptance Rate: {t.draft_acceptance_rate*100:.2f}%\n", style="green")
            gen_val = f"{t.draft_generated:,}" if t.draft_generated is not None else "N/A"
            acc_val = f"{t.draft_accepted:,}" if t.draft_accepted is not None else "N/A"
            rej_val = f"{t.draft_rejected:,}" if t.draft_rejected is not None else "N/A"
            text.append(f"• Speculative Draft Tokens Generated: {gen_val}\n")
            text.append(f"• Speculative Draft Tokens Accepted:  {acc_val}\n", style="green")
            text.append(f"• Speculative Draft Tokens Rejected:  {rej_val}\n", style="red")
            mlen_str = f"{t.draft_mean_len:.2f}" if t.draft_mean_len is not None else "N/A"
            text.append(f"• Mean Speculative Sequence Length:   {mlen_str} tokens/step\n", style="cyan")
            if t.draft_mean_len:
                text.append(f"• Effective Autoregressive Speedup:   ~{t.draft_mean_len:.2f}x faster than single-token decode\n", style="bold yellow")
            text.append("\n")

        self.query_one("#tokens-content", Static).update(Panel(text, title="Token Distribution & Speculative Metrics", border_style="yellow"))

    def render_context_pane(self, t: TaskMetrics) -> None:
        text = Text()
        text.append("CONTEXT WINDOW & SLOT ALLOCATION\n", style="bold white")
        text.append(f"• Slot Identifier:             id {t.slot_id}\n")
        text.append(f"• Task Identifier:             task {t.task_id}\n")
        retained_str = f"{t.stop_tokens:,} tokens in KV cache" if t.stop_tokens is not None else "N/A"
        text.append(f"• Retained Context Tokens:     {retained_str}\n", style="cyan")
        trunc_str = f"{t.truncated} (fits context capacity)" if t.truncated is not None else "N/A"
        text.append(f"• Truncated Tokens:            {trunc_str}\n", style="green" if t.truncated == 0 else "red")
        lru_str = str(t.lru_t_last) if t.lru_t_last is not None else "N/A"
        text.append(f"• LRU Last Used Timestamp:     {lru_str}\n")
        graph_str = f"{t.graphs_reused:,} executions" if t.graphs_reused is not None else "N/A"
        text.append(f"• Graphs Reused:               {graph_str}\n", style="bold blue")
        text.append("  (Static computation graphs are cached to avoid kernel re-instantiation overhead).\n\n")

        if t.queue_delay_s is not None:
            text.append("SCHEDULING QUEUE PERFORMANCE\n", style="bold white")
            text.append(f"• HTTP Request Arrival:        {t.http_request_time}\n")
            text.append(f"• Slot Worker Launch:          {t.launch_time}\n")
            text.append(f"• Dispatch Queue Latency:      {t.queue_delay_s:.3f} seconds\n", style="yellow" if t.queue_delay_s > 1.0 else "green")
            if t.queue_delay_s > 2.0:
                text.append("  Noticeable delay before slot allocation (indicates server busy or queue backlog).\n")

        self.query_one("#context-content", Static).update(Panel(text, title="Context & Engine State", border_style="blue"))


# ==============================================================================
# Markdown Report Exporter
# ==============================================================================

def export_markdown_report(tasks: List[TaskMetrics], log_file: str, out_path: str):
    """Generate a high-depth Markdown analysis report."""
    md = []
    md.append(f"# Lemonade Server Telemetry & Inference Analysis Report\n\n")
    md.append(f"* **Source Log:** `{log_file}`\n")
    md.append(f"* **Analyzed Tasks:** {len(tasks)}\n\n")
    md.append("---\n\n")

    for idx, t in enumerate(tasks, 1):
        md.append(f"## Task #{t.task_id} (Slot {t.slot_id})\n\n")
        md.append(f"* **Model:** `{t.model or 'Unknown / Not Logged'}`\n")
        launch_val = t.launch_time or "N/A"
        queue_val = f"{t.queue_delay_s:.2f}s" if t.queue_delay_s is not None else "N/A"
        md.append(f"* **Dispatch Time:** `{launch_val}` (Queue Delay: `{queue_val}`)\n")
        md.append(f"* **Total Context Footprint:** `{t.total_tokens or 'N/A'}` tokens\n\n")

        md.append("### Key Performance Indicators\n\n")
        md.append("| Metric | Value | Architectural Meaning |\n")
        md.append("|---|---|---|\n")
        p_str = f"`{t.prompt_tps:.2f} t/s`" if t.prompt_tps is not None else "`N/A`"
        if t.prompt_ms_per_token is not None:
            p_str += f" (`{t.prompt_ms_per_token:.2f} ms/tok`)"
        ttft_str = f"`{t.ttft_s:.2f}s`" if t.ttft_s is not None else "`N/A`"
        md.append(f"| **Prefill Speed (Prompt)** | {p_str} | Time To First Token (TTFT) = {ttft_str} |\n")

        d_str = f"`{t.eval_tps:.2f} t/s`" if t.eval_tps is not None else "`N/A`"
        if t.eval_ms_per_token is not None:
            d_str += f" (`{t.eval_ms_per_token:.2f} ms/tok`)"
        md.append(f"| **Decode Speed (Generation)** | {d_str} | Autoregressive streaming generation throughput |\n")

        tok_str = (
            f"In: `{t.prompt_tokens}` ({t.prompt_ratio:.1f}%) / Out: `{t.gen_tokens}` ({t.gen_ratio:.1f}%)"
            if t.prompt_tokens is not None and t.gen_tokens is not None
            else f"Total: `{t.total_tokens or 'N/A'}`"
        )
        md.append(f"| **Tokens Allocation** | {tok_str} | Total context footprint: `{t.total_tokens or 'N/A'}` tokens |\n")

        if t.draft_acceptance_rate is not None:
            acc_pct = f"`{t.draft_acceptance_rate*100:.2f}%`"
            acc_counts = f"(`{t.draft_accepted}/{t.draft_generated}`)" if t.draft_accepted is not None else ""
            md.append(f"| **Speculative MTP Acceptance** | {acc_pct} {acc_counts} | Multi-Token Prediction hit rate |\n")
            mlen_str = f"`{t.draft_mean_len:.2f}` tokens/step" if t.draft_mean_len is not None else "`N/A`"
            speedup_str = f"Effective speedup: ~`{t.draft_mean_len:.2f}x` vs single-token decode" if t.draft_mean_len else ""
            md.append(f"| **Mean Speculative Length** | {mlen_str} | {speedup_str} |\n")

        gr_str = f"`{t.graphs_reused:,}`" if t.graphs_reused is not None else "`N/A`"
        md.append(f"| **Graphs Reused** | {gr_str} | CUDA/execution graph cache hits |\n\n")

        if t.prompt_steps:
            md.append("### Prefill Scaling Breakdown\n\n")
            md.append("| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |\n")
            md.append("|---|---|---|---|---|\n")
            for s_idx, s in enumerate(t.prompt_steps, 1):
                md.append(f"| {s_idx} | {s.n_tokens:,} | {s.progress*100:.1f}% | {s.elapsed_s:.2f} | {s.speed_tps:.2f} |\n")
            md.append("\n")

        if t.gen_steps:
            md.append("### Decode Streaming Breakdown\n\n")
            md.append("| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |\n")
            md.append("|---|---|---|---|\n")
            for g_idx, g in enumerate(t.gen_steps, 1):
                md.append(f"| {g_idx} | {g.n_gen:,} | {g.tg_tps:.2f} t/s | {g.tg_3s_tps:.2f} t/s |\n")
            md.append("\n")

        md.append("---\n\n")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(md))
    print(f"Report written successfully to: {out_path}")


# ==============================================================================
# CLI Entrypoint
# ==============================================================================

def resolve_log_path(raw_arg: str) -> str:
    """Safely resolve file path across PowerShell, CMD, and Unix syntax."""
    path = raw_arg.strip('"\'')
    path = os.path.expandvars(os.path.expanduser(path))

    # Resolve PowerShell literal variable syntax $env:TEMP / ${env:TEMP} / $TEMP
    if "$env:TEMP" in path or "${env:TEMP}" in path:
        temp_dir = os.environ.get("TEMP", os.environ.get("TMP", ""))
        path = path.replace("$env:TEMP", temp_dir).replace("${env:TEMP}", temp_dir)
    elif "$TEMP" in path or "$TMP" in path:
        temp_dir = os.environ.get("TEMP", os.environ.get("TMP", ""))
        path = path.replace("$TEMP", temp_dir).replace("$TMP", temp_dir)

    if not os.path.isabs(path):
        candidates = [
            path,
            os.path.join(os.getcwd(), path),
            os.path.join(r"C:\Dev\github\philippeback\lemonade_tui", path)
        ]
        for c in candidates:
            if os.path.exists(c):
                return c

    return path


def main():
    parser = argparse.ArgumentParser(
        description="Lemonade Server Inference Telemetry & Analytics TUI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("logfile", nargs="?", default="lemonade-sample.log", help="Path to lemonade log file")
    parser.add_argument("--static", action="store_true", help="Render Rich terminal dashboard instead of full interactive TUI")
    parser.add_argument("--dynamic", "-d", "--live", "--watch", "-w", action="store_true", dest="dynamic", help="Enable dynamic live mode (live auto-refresh in terminal dashboard or live tailing in TUI)")
    parser.add_argument("--snapshot", "--static-tui", "--pause", action="store_true", dest="snapshot", help="Start interactive TUI in static snapshot mode (no background polling, maximum responsiveness)")
    parser.add_argument("--all", action="store_true", help="Display all tasks in static mode (defaults to latest 5)")
    parser.add_argument("--include-empty", action="store_true", help="Include cancelled/empty tasks with no token data")
    parser.add_argument("--task", "--task-id", type=int, default=None, help="Focus on or display a specific task by its Task ID")
    parser.add_argument("--export", metavar="OUT_FILE", help="Export analytics report to a markdown file")

    args = parser.parse_args()

    log_path = resolve_log_path(args.logfile)

    if not os.path.exists(log_path):
        print(f"Error: Log file '{log_path}' not found.")
        sys.exit(1)

    # Lightweight live terminal dashboard (zero Textual overhead)
    if (args.static and args.dynamic) or (not sys.stdin.isatty() and args.dynamic):
        watch_rich_dashboard(log_path, show_all=args.all)
        return

    tasks, log_parser = parse_lemonade_log_with_parser(log_path, filter_completed=not args.include_empty)
    if not tasks:
        print(f"Warning: No valid inference tasks found in '{log_path}'.")
        sys.exit(1)

    initial_task_idx = None
    if args.task is not None:
        matched_indices = [i for i, t in enumerate(tasks) if t.task_id == args.task]
        if matched_indices:
            initial_task_idx = matched_indices[0]
            if args.static or not sys.stdin.isatty():
                tasks = [tasks[initial_task_idx]]
        else:
            available_ids = ", ".join(f"#{t.task_id}" for t in tasks[:8])
            if len(tasks) > 8:
                available_ids += f" ... (total {len(tasks)})"
            print(f"Warning: Task #{args.task} not found in log (available: {available_ids}).")

    if args.export:
        export_markdown_report(tasks, log_path, args.export)
        return

    if args.static or not sys.stdin.isatty():
        render_rich_dashboard(tasks, log_path, show_all=args.all)
        return

    # Interactive SOTA Textual App
    dynamic_mode = not args.snapshot
    app = LemonadeTUIApp(tasks, log_path, parser=log_parser, dynamic_mode=dynamic_mode, initial_task_idx=initial_task_idx)
    app.run()


if __name__ == "__main__":
    main()
