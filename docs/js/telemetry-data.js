/**
 * Realistic Telemetry Datasets for Lemonade TUI Simulator
 * Directly extracted from lemonade-sample.log and benchmark traces.
 */
window.LEMONADE_DATASETS = [
  {
    taskId: 5376,
    slotId: 0,
    status: "DONE",
    statusText: "✔ DONE     ",
    statusClass: "tui-status-done",
    model: "Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K",
    promptTokens: 13445,
    genTokens: 777,
    ttftSec: 22.70,
    prefillTps: 451.6,
    decodeTps: 65.4,
    msPerToken: 15.3,
    draftAcceptance: 67.2,
    draftMeanLen: 3.02,
    graphsReused: 16290,
    queueDelaySec: 0.054,
    prefillSec: 22.70,
    decodeSec: 11.88,
    retainedTokens: 16017,
    truncated: 0,
    rawLog: `[2026-09-12 18:15:45.102] HTTP POST /api/v1/chat/completions - Streaming
[2026-09-12 18:15:45.156] launch_slot_with_task: id = 5376, slot = 0, is_child = 0
[2026-09-12 18:15:48.358] prompt eval time = 5034.12 ms / 4096 tokens ( 30.46 % done, 813.54 tokens per second)
[2026-09-12 18:15:55.201] prompt eval time = 11872.44 ms / 8192 tokens ( 60.93 % done, 598.19 tokens per second)
[2026-09-12 18:16:03.471] prompt eval time = 20140.10 ms / 12288 tokens ( 91.40 % done, 495.61 tokens per second)
[2026-09-12 18:16:06.030] prompt eval time = 22700.15 ms / 13445 tokens ( 1.69 ms per token, 451.62 tokens per second)
[2026-09-12 18:16:09.110] n_gen = 196, tg = 64.67 tokens/s, tg_3s = 65.00 tokens/s
[2026-09-12 18:16:15.120] n_gen = 540, tg = 59.73 tokens/s, tg_3s = 57.86 tokens/s
[2026-09-12 18:16:24.135] n_gen = 1069, tg = 59.07 tokens/s, tg_3s = 62.18 tokens/s
[2026-09-12 18:16:30.145] n_gen = 1475, tg = 61.09 tokens/s, tg_3s = 73.74 tokens/s
[2026-09-12 18:16:30.190] draft acceptance = 0.6723 ( 1113 accepted / 1656 generated), mean len = 3.02 ( 3.02 tokens/step)
[2026-09-12 18:16:30.201] graphs reused = 16290
[2026-09-12 18:16:30.210] eval time = 11878.50 ms / 777 tokens ( 15.29 ms per token, 65.41 tokens per second)
[2026-09-12 18:16:30.220] stop processing: n_tokens = 16017, truncated = 0
[2026-09-12 18:16:30.225] Inference completed: model=Qwen3.6-35B-A3B-Q4_K, tokens=14222 (in=13445, out=777), ttft=22.70s, tps=65.41`
  },
  {
    taskId: 6337,
    slotId: 0,
    status: "DONE",
    statusText: "✔ DONE     ",
    statusClass: "tui-status-done",
    model: "Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K",
    promptTokens: 1452,
    genTokens: 1475,
    ttftSec: 3.92,
    prefillTps: 370.2,
    decodeTps: 61.1,
    msPerToken: 16.4,
    draftAcceptance: 63.4,
    draftMeanLen: 2.90,
    graphsReused: 7386,
    queueDelaySec: 0.048,
    prefillSec: 3.92,
    decodeSec: 24.15,
    retainedTokens: 16017,
    truncated: 0,
    rawLog: `[2026-09-12 18:22:10.045] HTTP POST /api/v1/chat/completions - Streaming
[2026-09-12 18:22:10.093] launch_slot_with_task: id = 6337, slot = 0, is_child = 0
[2026-09-12 18:22:14.015] prompt eval time = 3922.50 ms / 1452 tokens ( 2.70 ms per token, 370.17 tokens per second)
[2026-09-12 18:22:17.110] n_gen = 196, tg = 64.67 tokens/s, tg_3s = 65.00 tokens/s
[2026-09-12 18:22:38.250] n_gen = 1475, tg = 61.09 tokens/s, tg_3s = 73.74 tokens/s
[2026-09-12 18:22:38.290] draft acceptance = 0.6336 ( 1034 accepted / 1632 generated), mean len = 2.90 ( 2.90 tokens/step)
[2026-09-12 18:22:38.305] graphs reused = 7386
[2026-09-12 18:22:38.312] eval time = 24145.20 ms / 1475 tokens ( 16.37 ms per token, 61.09 tokens per second)
[2026-09-12 18:22:38.320] Inference completed: model=Qwen3.6-35B-A3B-Q4_K, tokens=2927 (in=1452, out=1475), ttft=3.92s, tps=61.09`
  },
  {
    taskId: 16240,
    slotId: 0,
    status: "IN-FLIGHT",
    statusText: "● IN-FLIGHT",
    statusClass: "tui-status-inflight",
    model: "Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K",
    promptTokens: 2048,
    genTokens: 142,
    isStreaming: true,
    ttftSec: 4.12,
    prefillTps: 497.1,
    decodeTps: 58.4,
    msPerToken: 17.1,
    draftAcceptance: 59.4,
    draftMeanLen: 2.82,
    graphsReused: 2140,
    queueDelaySec: 0.052,
    prefillSec: 4.12,
    decodeSec: 2.43,
    retainedTokens: 2190,
    truncated: 0,
    rawLog: `[2026-09-12 18:30:02.100] HTTP POST /api/v1/chat/completions - Streaming
[2026-09-12 18:30:02.152] launch_slot_with_task: id = 16240, slot = 0, is_child = 0
[2026-09-12 18:30:06.272] prompt eval time = 4120.00 ms / 2048 tokens ( 2.01 ms per token, 497.09 tokens per second)
[2026-09-12 18:30:08.702] n_gen = 142, tg = 58.43 tokens/s, tg_3s = 58.40 tokens/s (Streaming active...)`
  },
  {
    taskId: 0,
    slotId: 0,
    status: "ABORTED",
    statusText: "✖ ABORTED  ",
    statusClass: "tui-status-aborted",
    model: "Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K",
    promptTokens: 128,
    genTokens: 0,
    ttftSec: 0,
    prefillTps: 0,
    decodeTps: 0,
    msPerToken: 0,
    draftAcceptance: 0,
    draftMeanLen: 0,
    graphsReused: 0,
    queueDelaySec: 0.061,
    prefillSec: 0,
    decodeSec: 0,
    retainedTokens: 0,
    truncated: 0,
    rawLog: `[2026-09-12 18:35:12.800] HTTP POST /api/v1/chat/completions
[2026-09-12 18:35:12.861] launch_slot_with_task: id = 0, slot = 0, is_child = 0
[2026-09-12 18:35:13.100] Client disconnected or task cancelled before decode step.
[2026-09-12 18:35:13.102] Slot 0 released. (Task #0 aborted)`
  }
];
