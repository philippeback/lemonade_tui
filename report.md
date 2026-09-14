# Lemonade Server Telemetry & Inference Analysis Report

* **Source Log:** `C:\Users\PHILIP~1\AppData\Local\Temp\lemonade-server.log`
* **Analyzed Tasks:** 196

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-06 20:21:54.298` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `22` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `107.67 t/s` (`9.29 ms/tok`) | Time To First Token (TTFT) = `0.19s` |
| **Decode Speed (Generation)** | `21.20 t/s` (`47.17 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `20` (90.9%) / Out: `2` (9.1%) | Total context footprint: `22` tokens |
| **Graphs Reused** | `2` | CUDA/execution graph cache hits |

---

## Task #5 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 00:21:10.455` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `638` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `205.60 t/s` (`4.86 ms/tok`) | Time To First Token (TTFT) = `2.06s` |
| **Decode Speed (Generation)** | `17.34 t/s` (`57.67 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `423` (66.3%) / Out: `215` (33.7%) | Total context footprint: `638` tokens |
| **Graphs Reused** | `214` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 17.04 t/s | 17.21 t/s |
| 2 | 154 | 17.30 t/s | 17.80 t/s |
| 3 | 207 | 17.38 t/s | 17.63 t/s |

---

## Task #223 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 00:21:24.940` (Queue Delay: `0.02s`)
* **Total Context Footprint:** `122` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `162.23 t/s` (`6.16 ms/tok`) | Time To First Token (TTFT) = `0.72s` |
| **Decode Speed (Generation)** | `21.21 t/s` (`47.16 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `116` (95.1%) / Out: `6` (4.9%) | Total context footprint: `122` tokens |
| **Graphs Reused** | `218` | CUDA/execution graph cache hits |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 00:31:52.115` (Queue Delay: `0.02s`)
* **Total Context Footprint:** `22` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `94.80 t/s` (`10.55 ms/tok`) | Time To First Token (TTFT) = `0.21s` |
| **Decode Speed (Generation)** | `21.05 t/s` (`47.49 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `20` (90.9%) / Out: `2` (9.1%) | Total context footprint: `22` tokens |
| **Graphs Reused** | `2` | CUDA/execution graph cache hits |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 00:36:32.403` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `22` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `74.51 t/s` (`13.42 ms/tok`) | Time To First Token (TTFT) = `0.27s` |
| **Decode Speed (Generation)** | `19.63 t/s` (`50.95 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `20` (90.9%) / Out: `2` (9.1%) | Total context footprint: `22` tokens |
| **Graphs Reused** | `2` | CUDA/execution graph cache hits |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 00:44:42.346` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `22` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `103.69 t/s` (`9.64 ms/tok`) | Time To First Token (TTFT) = `0.19s` |
| **Decode Speed (Generation)** | `20.17 t/s` (`49.57 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `20` (90.9%) / Out: `2` (9.1%) | Total context footprint: `22` tokens |
| **Graphs Reused** | `2` | CUDA/execution graph cache hits |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 00:45:37.021` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `22` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `83.24 t/s` (`12.01 ms/tok`) | Time To First Token (TTFT) = `0.24s` |
| **Decode Speed (Generation)** | `19.12 t/s` (`52.31 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `20` (90.9%) / Out: `2` (9.1%) | Total context footprint: `22` tokens |
| **Graphs Reused** | `2` | CUDA/execution graph cache hits |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 00:56:24.076` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `22` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `89.29 t/s` (`11.20 ms/tok`) | Time To First Token (TTFT) = `0.22s` |
| **Decode Speed (Generation)** | `20.30 t/s` (`49.26 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `20` (90.9%) / Out: `2` (9.1%) | Total context footprint: `22` tokens |
| **Graphs Reused** | `2` | CUDA/execution graph cache hits |

---

## Task #5 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 01:00:16.102` (Queue Delay: `0.07s`)
* **Total Context Footprint:** `12022` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `185.93 t/s` (`5.38 ms/tok`) | Time To First Token (TTFT) = `64.17s` |
| **Decode Speed (Generation)** | `14.15 t/s` (`70.69 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `11932` (99.3%) / Out: `90` (0.7%) | Total context footprint: `12022` tokens |
| **Graphs Reused** | `90` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 17.0% | 9.45 | 216.80 |
| 2 | 4,096 | 34.0% | 19.47 | 210.33 |
| 3 | 6,144 | 51.0% | 30.07 | 204.35 |
| 4 | 8,192 | 69.0% | 41.28 | 198.45 |
| 5 | 10,240 | 86.0% | 53.23 | 192.36 |
| 6 | 11,416 | 96.0% | 60.64 | 188.25 |
| 7 | 11,880 | 100.0% | 63.46 | 187.19 |
| 8 | 11,928 | 100.0% | 64.07 | 186.18 |

---

## Task #104 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 01:01:26.820` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `663` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `210.91 t/s` (`4.74 ms/tok`) | Time To First Token (TTFT) = `2.83s` |
| **Decode Speed (Generation)** | `18.10 t/s` (`55.26 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `597` (90.0%) / Out: `66` (10.0%) | Total context footprint: `663` tokens |
| **Graphs Reused** | `154` | CUDA/execution graph cache hits |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 21:54:21.985` (Queue Delay: `0.08s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 17.0% | 8.99 | 227.91 |
| 2 | 4,096 | 34.0% | 18.72 | 218.83 |

---

## Task #0 (Slot 0)

* **Model:** `embeddinggemma-300m-GGUF`
* **Dispatch Time:** `2026-09-07 21:54:50.975` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 6,144 | 51.0% | 29.76 | 206.46 |
| 2 | 8,192 | 69.0% | 41.46 | 197.60 |
| 3 | 10,240 | 86.0% | 52.78 | 194.03 |
| 4 | 11,438 | 96.0% | 60.93 | 187.74 |

---

## Task #0 (Slot 0)

* **Model:** `nomic-embed-text-v2-moe-GGUF`
* **Dispatch Time:** `2026-09-07 21:55:24.087` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 11,880 | 99.0% | 65.35 | 181.79 |
| 2 | 11,950 | 100.0% | 67.52 | 176.98 |

---

## Task #0 (Slot 0)

* **Model:** `nomic-embed-text-v2-moe-GGUF`
* **Dispatch Time:** `2026-09-07 21:55:37.930` (Queue Delay: `N/A`)
* **Total Context Footprint:** `12443` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `175.52 t/s` (`5.70 ms/tok`) | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `0.73 t/s` (`1367.16 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `11954` (96.1%) / Out: `489` (3.9%) | Total context footprint: `12443` tokens |
| **Graphs Reused** | `486` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 0.15 t/s | 0.16 t/s |
| 2 | 146 | 0.23 t/s | 15.23 t/s |
| 3 | 191 | 0.29 t/s | 14.85 t/s |
| 4 | 235 | 0.36 t/s | 14.43 t/s |
| 5 | 275 | 0.42 t/s | 13.22 t/s |
| 6 | 315 | 0.48 t/s | 13.32 t/s |
| 7 | 356 | 0.54 t/s | 13.49 t/s |
| 8 | 402 | 0.61 t/s | 15.11 t/s |
| 9 | 447 | 0.67 t/s | 14.87 t/s |

---

## Task #34 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 22:06:37.266` (Queue Delay: `N/A`)
* **Total Context Footprint:** `403` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `68.45 t/s` (`14.61 ms/tok`) | Time To First Token (TTFT) = `0.92s` |
| **Decode Speed (Generation)** | `15.01 t/s` (`66.62 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `63` (15.6%) / Out: `340` (84.4%) | Total context footprint: `403` tokens |
| **Graphs Reused** | `822` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 15.68 t/s | 15.84 t/s |
| 2 | 145 | 15.38 t/s | 14.74 t/s |
| 3 | 192 | 15.38 t/s | 15.37 t/s |
| 4 | 238 | 15.33 t/s | 15.16 t/s |
| 5 | 282 | 15.18 t/s | 14.38 t/s |
| 6 | 325 | 15.05 t/s | 14.25 t/s |

---

## Task #37 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-07 22:07:00.813` (Queue Delay: `N/A`)
* **Total Context Footprint:** `1909` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `214.13 t/s` (`4.67 ms/tok`) | Time To First Token (TTFT) = `7.12s` |
| **Decode Speed (Generation)** | `19.43 t/s` (`51.47 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1524` (79.8%) / Out: `385` (20.2%) | Total context footprint: `1909` tokens |
| **Graphs Reused** | `1,203` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 1,008 | 66.0% | 4.65 | 216.90 |
| 2 | 1,520 | 100.0% | 7.05 | 215.63 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 19.83 t/s | 20.03 t/s |
| 2 | 161 | 19.90 t/s | 20.01 t/s |
| 3 | 219 | 19.70 t/s | 19.17 t/s |
| 4 | 279 | 19.69 t/s | 19.68 t/s |
| 5 | 338 | 19.63 t/s | 19.33 t/s |

---

## Task #0 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:12:35.506` (Queue Delay: `0.05s`)
* **Total Context Footprint:** `1834` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `106.27 t/s` (`9.41 ms/tok`) | Time To First Token (TTFT) = `16.49s` |
| **Decode Speed (Generation)** | `17.56 t/s` (`56.94 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1752` (95.5%) / Out: `82` (4.5%) | Total context footprint: `1834` tokens |
| **Graphs Reused** | `80` | CUDA/execution graph cache hits |

---

## Task #83 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:13:23.490` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `3680` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `56.75 t/s` (`17.62 ms/tok`) | Time To First Token (TTFT) = `1.02s` |
| **Decode Speed (Generation)** | `14.95 t/s` (`66.89 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `58` (1.6%) / Out: `3622` (98.4%) | Total context footprint: `3680` tokens |
| **Graphs Reused** | `3,686` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 17.36 t/s | 17.54 t/s |
| 2 | 153 | 17.37 t/s | 17.40 t/s |
| 3 | 208 | 17.55 t/s | 18.05 t/s |
| 4 | 262 | 17.62 t/s | 17.91 t/s |
| 5 | 312 | 17.44 t/s | 16.53 t/s |
| 6 | 364 | 17.39 t/s | 17.09 t/s |
| 7 | 416 | 17.38 t/s | 17.29 t/s |
| 8 | 469 | 17.37 t/s | 17.36 t/s |
| 9 | 521 | 17.35 t/s | 17.14 t/s |
| 10 | 573 | 17.34 t/s | 17.21 t/s |
| 11 | 625 | 17.32 t/s | 17.13 t/s |
| 12 | 676 | 17.29 t/s | 16.93 t/s |
| 13 | 728 | 17.28 t/s | 17.16 t/s |
| 14 | 780 | 17.28 t/s | 17.24 t/s |
| 15 | 829 | 17.22 t/s | 16.27 t/s |
| 16 | 876 | 17.12 t/s | 15.61 t/s |
| 17 | 924 | 17.06 t/s | 15.97 t/s |
| 18 | 968 | 16.93 t/s | 14.57 t/s |
| 19 | 1,017 | 16.88 t/s | 15.95 t/s |
| 20 | 1,066 | 16.83 t/s | 16.03 t/s |
| 21 | 1,116 | 16.82 t/s | 16.46 t/s |
| 22 | 1,164 | 16.77 t/s | 15.83 t/s |
| 23 | 1,214 | 16.76 t/s | 16.50 t/s |
| 24 | 1,265 | 16.77 t/s | 16.92 t/s |
| 25 | 1,314 | 16.75 t/s | 16.28 t/s |
| 26 | 1,360 | 16.70 t/s | 15.33 t/s |
| 27 | 1,408 | 16.66 t/s | 15.68 t/s |
| 28 | 1,451 | 16.57 t/s | 14.14 t/s |
| 29 | 1,497 | 16.52 t/s | 14.99 t/s |
| 30 | 1,541 | 16.45 t/s | 14.38 t/s |
| 31 | 1,585 | 16.38 t/s | 14.38 t/s |
| 32 | 1,629 | 16.33 t/s | 14.60 t/s |
| 33 | 1,674 | 16.28 t/s | 14.73 t/s |
| 34 | 1,719 | 16.22 t/s | 14.04 t/s |
| 35 | 1,763 | 16.17 t/s | 14.47 t/s |
| 36 | 1,810 | 16.15 t/s | 15.65 t/s |
| 37 | 1,855 | 16.12 t/s | 14.78 t/s |
| 38 | 1,899 | 16.07 t/s | 14.49 t/s |
| 39 | 1,942 | 16.03 t/s | 14.26 t/s |
| 40 | 1,985 | 15.99 t/s | 14.26 t/s |
| 41 | 2,027 | 15.94 t/s | 13.83 t/s |
| 42 | 2,068 | 15.88 t/s | 13.54 t/s |
| 43 | 2,111 | 15.84 t/s | 14.05 t/s |
| 44 | 2,155 | 15.81 t/s | 14.56 t/s |
| 45 | 2,198 | 15.77 t/s | 14.10 t/s |
| 46 | 2,241 | 15.74 t/s | 14.30 t/s |
| 47 | 2,281 | 15.68 t/s | 13.07 t/s |
| 48 | 2,325 | 15.66 t/s | 14.50 t/s |
| 49 | 2,365 | 15.61 t/s | 13.31 t/s |
| 50 | 2,407 | 15.58 t/s | 14.00 t/s |
| 51 | 2,451 | 15.56 t/s | 14.46 t/s |
| 52 | 2,494 | 15.54 t/s | 14.26 t/s |
| 53 | 2,538 | 15.52 t/s | 14.61 t/s |
| 54 | 2,581 | 15.50 t/s | 14.24 t/s |
| 55 | 2,626 | 15.48 t/s | 14.79 t/s |
| 56 | 2,668 | 15.46 t/s | 13.99 t/s |
| 57 | 2,706 | 15.40 t/s | 12.43 t/s |
| 58 | 2,746 | 15.37 t/s | 13.26 t/s |
| 59 | 2,787 | 15.34 t/s | 13.61 t/s |
| 60 | 2,829 | 15.31 t/s | 13.85 t/s |
| 61 | 2,871 | 15.29 t/s | 13.89 t/s |
| 62 | 2,911 | 15.26 t/s | 13.14 t/s |
| 63 | 2,950 | 15.22 t/s | 12.93 t/s |
| 64 | 2,993 | 15.20 t/s | 14.12 t/s |
| 65 | 3,037 | 15.19 t/s | 14.58 t/s |
| 66 | 3,081 | 15.18 t/s | 14.51 t/s |
| 67 | 3,124 | 15.17 t/s | 14.12 t/s |
| 68 | 3,167 | 15.15 t/s | 14.16 t/s |
| 69 | 3,211 | 15.15 t/s | 14.62 t/s |
| 70 | 3,254 | 15.13 t/s | 14.31 t/s |
| 71 | 3,295 | 15.11 t/s | 13.58 t/s |
| 72 | 3,338 | 15.10 t/s | 14.12 t/s |
| 73 | 3,380 | 15.08 t/s | 13.94 t/s |
| 74 | 3,421 | 15.06 t/s | 13.48 t/s |
| 75 | 3,461 | 15.04 t/s | 13.22 t/s |
| 76 | 3,502 | 15.02 t/s | 13.53 t/s |
| 77 | 3,542 | 15.00 t/s | 13.32 t/s |
| 78 | 3,583 | 14.98 t/s | 13.45 t/s |

---

## Task #3706 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:17:26.790` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `307` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `23.09 t/s` (`43.31 ms/tok`) | Time To First Token (TTFT) = `0.56s` |
| **Decode Speed (Generation)** | `13.26 t/s` (`75.41 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `13` (4.2%) / Out: `294` (95.8%) | Total context footprint: `307` tokens |
| **Graphs Reused** | `3,977` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 13.82 t/s | 13.96 t/s |
| 2 | 142 | 13.78 t/s | 13.70 t/s |
| 3 | 182 | 13.67 t/s | 13.31 t/s |
| 4 | 221 | 13.54 t/s | 12.93 t/s |
| 5 | 259 | 13.39 t/s | 12.58 t/s |

---

## Task #4001 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:20:55.110` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `4080` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `64.03 t/s` (`15.62 ms/tok`) | Time To First Token (TTFT) = `58.82s` |
| **Decode Speed (Generation)** | `12.83 t/s` (`77.96 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `3766` (92.3%) / Out: `314` (7.7%) | Total context footprint: `4080` tokens |
| **Graphs Reused** | `4,288` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 69.0% | 27.53 | 74.38 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 12.84 t/s | 12.97 t/s |
| 2 | 140 | 12.90 t/s | 13.05 t/s |
| 3 | 178 | 12.84 t/s | 12.66 t/s |
| 4 | 217 | 12.86 t/s | 12.93 t/s |
| 5 | 255 | 12.83 t/s | 12.66 t/s |
| 6 | 293 | 12.81 t/s | 12.65 t/s |

---

## Task #4317 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:22:18.421` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `226` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `25.52 t/s` (`39.18 ms/tok`) | Time To First Token (TTFT) = `3.76s` |
| **Decode Speed (Generation)** | `12.53 t/s` (`79.78 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (42.5%) / Out: `130` (57.5%) | Total context footprint: `226` tokens |
| **Graphs Reused** | `4,416` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 12.46 t/s | 12.59 t/s |

---

## Task #4448 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:22:32.565` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `277` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `25.18 t/s` (`39.72 ms/tok`) | Time To First Token (TTFT) = `3.81s` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (34.7%) / Out: `181` (65.3%) | Total context footprint: `277` tokens |
| **Graphs Reused** | `4,595` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 12.47 t/s | 12.60 t/s |
| 2 | 137 | 12.43 t/s | 12.32 t/s |
| 3 | 175 | 12.44 t/s | 12.48 t/s |

---

## Task #4630 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:22:51.075` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `180` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `23.64 t/s` (`42.30 ms/tok`) | Time To First Token (TTFT) = `4.06s` |
| **Decode Speed (Generation)** | `11.70 t/s` (`85.43 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (53.3%) / Out: `84` (46.7%) | Total context footprint: `180` tokens |
| **Graphs Reused** | `4,677` | CUDA/execution graph cache hits |

---

## Task #4715 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:23:02.269` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `64` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `22.42 t/s` (`44.60 ms/tok`) | Time To First Token (TTFT) = `0.71s` |
| **Decode Speed (Generation)** | `12.29 t/s` (`81.40 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `16` (25.0%) / Out: `48` (75.0%) | Total context footprint: `64` tokens |
| **Graphs Reused** | `4,723` | CUDA/execution graph cache hits |

---

## Task #4764 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:23:06.905` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `211` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `23.76 t/s` (`42.09 ms/tok`) | Time To First Token (TTFT) = `4.04s` |
| **Decode Speed (Generation)** | `11.26 t/s` (`88.84 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (45.5%) / Out: `115` (54.5%) | Total context footprint: `211` tokens |
| **Graphs Reused** | `4,836` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 11.27 t/s | 11.39 t/s |

---

## Task #4880 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:23:21.172` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `206` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `22.32 t/s` (`44.81 ms/tok`) | Time To First Token (TTFT) = `4.30s` |
| **Decode Speed (Generation)** | `11.46 t/s` (`87.28 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (46.6%) / Out: `110` (53.4%) | Total context footprint: `206` tokens |
| **Graphs Reused** | `4,944` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 11.44 t/s | 11.55 t/s |

---

## Task #4991 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:23:35.093` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `187` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `22.49 t/s` (`44.46 ms/tok`) | Time To First Token (TTFT) = `4.27s` |
| **Decode Speed (Generation)** | `11.41 t/s` (`87.63 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (51.3%) / Out: `91` (48.7%) | Total context footprint: `187` tokens |
| **Graphs Reused** | `5,032` | CUDA/execution graph cache hits |

---

## Task #5083 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:23:47.341` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 11.67 t/s | 11.79 t/s |
| 2 | 134 | 11.55 t/s | 11.21 t/s |

---

## Task #5220 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:24:04.789` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `1158` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `44.09 t/s` (`22.68 ms/tok`) | Time To First Token (TTFT) = `24.32s` |
| **Decode Speed (Generation)** | `11.66 t/s` (`85.73 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1072` (92.6%) / Out: `86` (7.4%) | Total context footprint: `1158` tokens |
| **Graphs Reused** | `5,247` | CUDA/execution graph cache hits |

---

## Task #5307 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:24:36.488` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `180` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `22.61 t/s` (`44.22 ms/tok`) | Time To First Token (TTFT) = `4.25s` |
| **Decode Speed (Generation)** | `11.56 t/s` (`86.50 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (53.3%) / Out: `84` (46.7%) | Total context footprint: `180` tokens |
| **Graphs Reused** | `5,329` | CUDA/execution graph cache hits |

---

## Task #5392 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:24:48.013` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `159` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `22.26 t/s` (`44.93 ms/tok`) | Time To First Token (TTFT) = `4.31s` |
| **Decode Speed (Generation)** | `11.37 t/s` (`87.96 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (60.4%) / Out: `63` (39.6%) | Total context footprint: `159` tokens |
| **Graphs Reused** | `5,390` | CUDA/execution graph cache hits |

---

## Task #5456 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:24:57.879` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `169` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `21.82 t/s` (`45.84 ms/tok`) | Time To First Token (TTFT) = `4.40s` |
| **Decode Speed (Generation)** | `11.58 t/s` (`86.37 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (56.8%) / Out: `73` (43.2%) | Total context footprint: `169` tokens |
| **Graphs Reused** | `5,460` | CUDA/execution graph cache hits |

---

## Task #5530 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:25:08.600` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `225` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `21.32 t/s` (`46.89 ms/tok`) | Time To First Token (TTFT) = `4.50s` |
| **Decode Speed (Generation)** | `11.29 t/s` (`88.59 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `96` (42.7%) / Out: `129` (57.3%) | Total context footprint: `225` tokens |
| **Graphs Reused** | `5,586` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 11.21 t/s | 11.33 t/s |

---

## Task #5660 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:25:24.492` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `86` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `19.12 t/s` (`52.31 ms/tok`) | Time To First Token (TTFT) = `0.94s` |
| **Decode Speed (Generation)** | `10.46 t/s` (`95.57 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `18` (20.9%) / Out: `68` (79.1%) | Total context footprint: `86` tokens |
| **Graphs Reused** | `5,652` | CUDA/execution graph cache hits |

---

## Task #5729 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:25:31.894` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 11.19 t/s | 11.30 t/s |
| 2 | 135 | 11.26 t/s | 11.47 t/s |
| 3 | 170 | 11.29 t/s | 11.40 t/s |

---

## Task #5910 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:25:49.897` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `801` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `37.63 t/s` (`26.58 ms/tok`) | Time To First Token (TTFT) = `19.80s` |
| **Decode Speed (Generation)** | `10.83 t/s` (`92.31 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `745` (93.0%) / Out: `56` (7.0%) | Total context footprint: `801` tokens |
| **Graphs Reused** | `5,881` | CUDA/execution graph cache hits |

---

## Task #5967 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:26:14.828` (Queue Delay: `0.05s`)
* **Total Context Footprint:** `79` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `18.21 t/s` (`54.91 ms/tok`) | Time To First Token (TTFT) = `0.88s` |
| **Decode Speed (Generation)** | `10.99 t/s` (`90.99 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `16` (20.3%) / Out: `63` (79.7%) | Total context footprint: `79` tokens |
| **Graphs Reused** | `5,942` | CUDA/execution graph cache hits |

---

## Task #6031 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-07 22:26:21.452` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 11.40 t/s | 11.51 t/s |

---

## Task #6150 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-08 07:58:49.185` (Queue Delay: `0.05s`)
* **Total Context Footprint:** `8391` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `58.76 t/s` (`17.02 ms/tok`) | Time To First Token (TTFT) = `141.41s` |
| **Decode Speed (Generation)** | `9.10 t/s` (`109.90 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `8310` (99.0%) / Out: `81` (1.0%) | Total context footprint: `8391` tokens |
| **Graphs Reused** | `6,135` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 25.0% | 19.60 | 104.51 |
| 2 | 4,096 | 50.0% | 48.72 | 84.07 |
| 3 | 6,144 | 74.0% | 86.97 | 70.64 |
| 4 | 8,192 | 99.0% | 135.37 | 60.51 |

---

## Task #6151 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-08 08:01:19.450` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 55.0% | 19.77 | 103.58 |

---

## Task #6280 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-08 19:21:30.828` (Queue Delay: `N/A`)
* **Total Context Footprint:** `1048` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `123.32 t/s` (`8.11 ms/tok`) | Time To First Token (TTFT) = `5.91s` |
| **Decode Speed (Generation)** | `18.30 t/s` (`54.66 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `729` (69.6%) / Out: `319` (30.4%) | Total context footprint: `1048` tokens |
| **Graphs Reused** | `6,486` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 18.52 t/s | 18.70 t/s |
| 2 | 152 | 17.96 t/s | 16.99 t/s |
| 3 | 206 | 17.92 t/s | 17.79 t/s |
| 4 | 263 | 18.12 t/s | 18.89 t/s |

---

## Task #6281 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-08 19:21:54.131` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 11.0% | 19.58 | 104.59 |

---

## Task #0 (Slot 0)

* **Model:** `user.Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 20:25:23.221` (Queue Delay: `N/A`)
* **Total Context Footprint:** `1340` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `14.05 t/s` (`71.20 ms/tok`) | Time To First Token (TTFT) = `56.10s` |
| **Decode Speed (Generation)** | `4.29 t/s` (`233.36 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `788` (58.8%) / Out: `552` (41.2%) | Total context footprint: `1340` tokens |
| **Speculative MTP Acceptance** | `57.76%` (`350/606`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.73` tokens/step | Effective speedup: ~`2.73x` vs single-token decode |
| **Graphs Reused** | `200` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 719 | 91.0% | 49.68 | 14.47 |
| 2 | 784 | 99.0% | 55.38 | 14.16 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 4.07 t/s | 4.11 t/s |
| 2 | 116 | 4.13 t/s | 4.50 t/s |
| 3 | 132 | 4.21 t/s | 4.99 t/s |
| 4 | 150 | 4.35 t/s | 5.73 t/s |
| 5 | 167 | 4.45 t/s | 5.54 t/s |
| 6 | 181 | 4.45 t/s | 4.42 t/s |
| 7 | 196 | 4.48 t/s | 4.82 t/s |
| 8 | 209 | 4.46 t/s | 4.18 t/s |
| 9 | 221 | 4.42 t/s | 3.83 t/s |
| 10 | 233 | 4.38 t/s | 3.78 t/s |
| 11 | 248 | 4.41 t/s | 4.95 t/s |
| 12 | 262 | 4.41 t/s | 4.41 t/s |
| 13 | 274 | 4.38 t/s | 3.82 t/s |
| 14 | 291 | 4.41 t/s | 5.06 t/s |
| 15 | 301 | 4.35 t/s | 3.11 t/s |
| 16 | 313 | 4.32 t/s | 3.68 t/s |
| 17 | 323 | 4.27 t/s | 3.11 t/s |
| 18 | 337 | 4.28 t/s | 4.42 t/s |
| 19 | 346 | 4.22 t/s | 2.82 t/s |
| 20 | 360 | 4.23 t/s | 4.46 t/s |
| 21 | 374 | 4.23 t/s | 4.31 t/s |
| 22 | 391 | 4.27 t/s | 5.18 t/s |
| 23 | 405 | 4.27 t/s | 4.47 t/s |
| 24 | 412 | 4.20 t/s | 2.10 t/s |
| 25 | 426 | 4.20 t/s | 4.24 t/s |
| 26 | 438 | 4.19 t/s | 3.73 t/s |
| 27 | 450 | 4.16 t/s | 3.50 t/s |
| 28 | 462 | 4.15 t/s | 3.77 t/s |
| 29 | 479 | 4.19 t/s | 5.57 t/s |
| 30 | 493 | 4.20 t/s | 4.39 t/s |
| 31 | 511 | 4.23 t/s | 5.64 t/s |
| 32 | 524 | 4.23 t/s | 4.16 t/s |
| 33 | 542 | 4.27 t/s | 5.74 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 20:41:09.062` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `150` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `4.29 t/s` (`232.87 ms/tok`) | Time To First Token (TTFT) = `12.81s` |
| **Decode Speed (Generation)** | `16.75 t/s` (`59.70 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `55` (36.7%) / Out: `95` (63.3%) | Total context footprint: `150` tokens |
| **Speculative MTP Acceptance** | `50.00%` (`57/114`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.50` tokens/step | Effective speedup: ~`2.50x` vs single-token decode |
| **Graphs Reused** | `38` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 51 | 93.0% | 6.29 | 8.11 |

---

## Task #42 (Slot 0)

* **Model:** `Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 20:41:39.593` (Queue Delay: `4.01s`)
* **Total Context Footprint:** `113` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `2.28 t/s` (`438.23 ms/tok`) | Time To First Token (TTFT) = `16.21s` |
| **Decode Speed (Generation)** | `19.51 t/s` (`51.27 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `37` (32.7%) / Out: `76` (67.3%) | Total context footprint: `113` tokens |
| **Speculative MTP Acceptance** | `65.39%` (`51/78`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.96` tokens/step | Effective speedup: ~`2.96x` vs single-token decode |
| **Graphs Reused** | `63` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 26 | 88.0% | 3.94 | 6.60 |
| 2 | 33 | 95.0% | 12.02 | 2.75 |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 21:01:40.949` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `101` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `10.98 t/s` (`91.04 ms/tok`) | Time To First Token (TTFT) = `4.83s` |
| **Decode Speed (Generation)** | `5.43 t/s` (`184.10 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `53` (52.5%) / Out: `48` (47.5%) | Total context footprint: `101` tokens |
| **Speculative MTP Acceptance** | `78.57%` (`33/42`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.36` tokens/step | Effective speedup: ~`3.36x` vs single-token decode |
| **Graphs Reused** | `14` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 42 | 79.0% | 3.03 | 13.85 |
| 2 | 49 | 92.0% | 4.00 | 12.25 |

---

## Task #18 (Slot 0)

* **Model:** `Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 21:02:35.824` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `515` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `11.50 t/s` (`86.97 ms/tok`) | Time To First Token (TTFT) = `4.35s` |
| **Decode Speed (Generation)** | `4.44 t/s` (`225.22 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `50` (9.7%) / Out: `465` (90.3%) | Total context footprint: `515` tokens |
| **Speculative MTP Acceptance** | `59.13%` (`298/504`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.77` tokens/step | Effective speedup: ~`2.77x` vs single-token decode |
| **Graphs Reused** | `179` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 46 | 96.0% | 3.69 | 12.48 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 3.76 t/s | 3.80 t/s |
| 2 | 110 | 3.71 t/s | 3.24 t/s |
| 3 | 122 | 3.73 t/s | 3.93 t/s |
| 4 | 141 | 3.94 t/s | 6.23 t/s |
| 5 | 159 | 4.09 t/s | 5.68 t/s |
| 6 | 168 | 3.99 t/s | 2.85 t/s |
| 7 | 178 | 3.94 t/s | 3.20 t/s |
| 8 | 195 | 4.04 t/s | 5.46 t/s |
| 9 | 210 | 4.05 t/s | 4.29 t/s |
| 10 | 226 | 4.10 t/s | 4.84 t/s |
| 11 | 239 | 4.10 t/s | 4.06 t/s |
| 12 | 255 | 4.15 t/s | 5.20 t/s |
| 13 | 275 | 4.26 t/s | 6.42 t/s |
| 14 | 294 | 4.35 t/s | 6.14 t/s |
| 15 | 311 | 4.40 t/s | 5.41 t/s |
| 16 | 330 | 4.47 t/s | 6.20 t/s |
| 17 | 348 | 4.53 t/s | 5.86 t/s |
| 18 | 366 | 4.57 t/s | 5.66 t/s |
| 19 | 386 | 4.65 t/s | 6.54 t/s |
| 20 | 401 | 4.65 t/s | 4.78 t/s |
| 21 | 410 | 4.59 t/s | 2.90 t/s |
| 22 | 425 | 4.60 t/s | 4.80 t/s |
| 23 | 433 | 4.53 t/s | 2.54 t/s |
| 24 | 445 | 4.51 t/s | 3.85 t/s |
| 25 | 455 | 4.45 t/s | 2.79 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 21:22:25.252` (Queue Delay: `N/A`)
* **Total Context Footprint:** `1173` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `43.69 t/s` (`22.89 ms/tok`) | Time To First Token (TTFT) = `17.83s` |
| **Decode Speed (Generation)** | `18.30 t/s` (`54.65 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `779` (66.4%) / Out: `394` (33.6%) | Total context footprint: `1173` tokens |
| **Speculative MTP Acceptance** | `57.87%` (`250/432`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.74` tokens/step | Effective speedup: ~`2.74x` vs single-token decode |
| **Graphs Reused** | `143` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 719 | 92.0% | 5.96 | 120.72 |
| 2 | 775 | 99.0% | 12.97 | 59.74 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 19.48 t/s | 19.67 t/s |
| 2 | 159 | 19.40 t/s | 19.26 t/s |
| 3 | 214 | 19.06 t/s | 18.15 t/s |
| 4 | 265 | 18.45 t/s | 16.27 t/s |
| 5 | 315 | 18.12 t/s | 16.54 t/s |
| 6 | 373 | 18.18 t/s | 18.55 t/s |

---

## Task #2 (Slot 0)

* **Model:** `Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 21:23:09.540` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 10.0% | 8.71 | 235.19 |
| 2 | 4,096 | 21.0% | 21.41 | 191.33 |
| 3 | 6,144 | 31.0% | 34.60 | 177.59 |
| 4 | 8,192 | 42.0% | 48.50 | 168.89 |
| 5 | 10,240 | 52.0% | 62.99 | 162.56 |
| 6 | 12,288 | 63.0% | 78.07 | 157.40 |
| 7 | 14,336 | 73.0% | 93.49 | 153.35 |
| 8 | 16,384 | 84.0% | 109.55 | 149.55 |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 21:26:28.920` (Queue Delay: `N/A`)
* **Total Context Footprint:** `1160` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `55.96 t/s` (`17.87 ms/tok`) | Time To First Token (TTFT) = `13.92s` |
| **Decode Speed (Generation)** | `18.35 t/s` (`54.50 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `779` (67.2%) / Out: `381` (32.8%) | Total context footprint: `1160` tokens |
| **Speculative MTP Acceptance** | `58.70%` (`243/414`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.76` tokens/step | Effective speedup: ~`2.76x` vs single-token decode |
| **Graphs Reused** | `137` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 775 | 99.0% | 8.88 | 87.28 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 102 | 18.68 t/s | 18.87 t/s |
| 2 | 164 | 19.35 t/s | 20.55 t/s |
| 3 | 206 | 17.90 t/s | 13.87 t/s |
| 4 | 273 | 18.63 t/s | 21.30 t/s |
| 5 | 327 | 18.48 t/s | 17.72 t/s |

---

## Task #2 (Slot 0)

* **Model:** `Qwen3.8-27B-ThinkingCoder`
* **Dispatch Time:** `2026-09-08 21:27:08.756` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 4,096 | 21.0% | 19.19 | 213.41 |
| 2 | 8,192 | 42.0% | 47.66 | 171.89 |
| 3 | 12,288 | 63.0% | 78.44 | 156.66 |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 21:35:10.606` (Queue Delay: `N/A`)
* **Total Context Footprint:** `19643` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `144.32 t/s` (`6.93 ms/tok`) | Time To First Token (TTFT) = `135.22s` |
| **Decode Speed (Generation)** | `14.53 t/s` (`68.82 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `19515` (99.3%) / Out: `128` (0.7%) | Total context footprint: `19643` tokens |
| **Speculative MTP Acceptance** | `52.00%` (`78/150`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.56` tokens/step | Effective speedup: ~`2.56x` vs single-token decode |
| **Graphs Reused** | `50` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 10.0% | 7.10 | 288.39 |
| 2 | 4,096 | 21.0% | 17.76 | 230.65 |
| 3 | 6,144 | 31.0% | 29.07 | 211.33 |
| 4 | 8,192 | 42.0% | 40.84 | 200.57 |
| 5 | 10,240 | 52.0% | 53.11 | 192.80 |
| 6 | 12,288 | 63.0% | 65.86 | 186.58 |
| 7 | 14,336 | 73.0% | 79.30 | 180.79 |
| 8 | 16,384 | 84.0% | 93.33 | 175.55 |
| 9 | 18,432 | 94.0% | 107.97 | 170.72 |
| 10 | 18,999 | 97.0% | 115.61 | 164.34 |
| 11 | 19,424 | 100.0% | 121.23 | 160.23 |
| 12 | 19,511 | 100.0% | 129.25 | 150.96 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 101 | 13.64 t/s | 13.77 t/s |

---

## Task #64 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 21:40:16.501` (Queue Delay: `N/A`)
* **Total Context Footprint:** `1837` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `46.26 t/s` (`21.62 ms/tok`) | Time To First Token (TTFT) = `17.21s` |
| **Decode Speed (Generation)** | `19.02 t/s` (`52.56 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `796` (43.3%) / Out: `1041` (56.7%) | Total context footprint: `1837` tokens |
| **Speculative MTP Acceptance** | `59.95%` (`669/1116`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.80` tokens/step | Effective speedup: ~`2.80x` vs single-token decode |
| **Graphs Reused** | `417` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 719 | 90.0% | 5.79 | 124.20 |
| 2 | 792 | 99.0% | 12.25 | 64.63 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 103 | 18.46 t/s | 18.64 t/s |
| 2 | 167 | 19.36 t/s | 21.00 t/s |
| 3 | 227 | 19.34 t/s | 19.29 t/s |
| 4 | 276 | 18.67 t/s | 16.07 t/s |
| 5 | 340 | 19.00 t/s | 20.59 t/s |
| 6 | 378 | 18.09 t/s | 12.66 t/s |
| 7 | 427 | 17.82 t/s | 15.98 t/s |
| 8 | 488 | 18.03 t/s | 19.66 t/s |
| 9 | 537 | 17.82 t/s | 15.97 t/s |
| 10 | 602 | 18.11 t/s | 20.90 t/s |
| 11 | 667 | 18.34 t/s | 20.75 t/s |
| 12 | 729 | 18.49 t/s | 20.29 t/s |
| 13 | 804 | 18.91 t/s | 24.22 t/s |
| 14 | 855 | 18.76 t/s | 16.66 t/s |
| 15 | 915 | 18.78 t/s | 19.18 t/s |
| 16 | 975 | 18.80 t/s | 19.14 t/s |

---

## Task #65 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 21:41:34.009` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 41 | 100.0% | 4.99 | 8.21 |
| 2 | 71 | 100.0% | 10.46 | 6.79 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 102 | 14.54 t/s | 14.68 t/s |
| 2 | 137 | 13.67 t/s | 11.66 t/s |
| 3 | 166 | 12.69 t/s | 9.51 t/s |
| 4 | 208 | 12.90 t/s | 13.75 t/s |
| 5 | 254 | 13.16 t/s | 14.51 t/s |
| 6 | 288 | 12.88 t/s | 11.14 t/s |
| 7 | 319 | 12.58 t/s | 10.30 t/s |
| 8 | 355 | 12.45 t/s | 11.39 t/s |
| 9 | 387 | 12.27 t/s | 10.57 t/s |
| 10 | 421 | 12.13 t/s | 10.77 t/s |
| 11 | 466 | 12.33 t/s | 14.65 t/s |
| 12 | 502 | 12.29 t/s | 11.81 t/s |
| 13 | 533 | 12.16 t/s | 10.32 t/s |
| 14 | 577 | 12.30 t/s | 14.38 t/s |
| 15 | 603 | 12.08 t/s | 8.66 t/s |
| 16 | 638 | 12.04 t/s | 11.32 t/s |
| 17 | 681 | 12.15 t/s | 14.04 t/s |
| 18 | 707 | 11.97 t/s | 8.63 t/s |
| 19 | 746 | 12.01 t/s | 12.71 t/s |
| 20 | 786 | 12.04 t/s | 12.61 t/s |
| 21 | 824 | 12.05 t/s | 12.41 t/s |
| 22 | 857 | 12.00 t/s | 10.74 t/s |
| 23 | 902 | 12.11 t/s | 14.78 t/s |
| 24 | 949 | 12.24 t/s | 15.26 t/s |
| 25 | 989 | 12.27 t/s | 13.29 t/s |
| 26 | 1,019 | 12.18 t/s | 9.72 t/s |
| 27 | 1,052 | 12.12 t/s | 10.63 t/s |
| 28 | 1,085 | 12.08 t/s | 10.90 t/s |
| 29 | 1,126 | 12.13 t/s | 13.42 t/s |
| 30 | 1,162 | 12.12 t/s | 11.84 t/s |
| 31 | 1,208 | 12.21 t/s | 15.05 t/s |
| 32 | 1,245 | 12.20 t/s | 12.04 t/s |
| 33 | 1,280 | 12.18 t/s | 11.55 t/s |
| 34 | 1,317 | 12.18 t/s | 12.13 t/s |
| 35 | 1,348 | 12.13 t/s | 10.27 t/s |
| 36 | 1,382 | 12.10 t/s | 10.98 t/s |
| 37 | 1,410 | 12.02 t/s | 8.96 t/s |
| 38 | 1,438 | 11.94 t/s | 9.16 t/s |
| 39 | 1,478 | 11.97 t/s | 12.79 t/s |
| 40 | 1,511 | 11.93 t/s | 10.59 t/s |
| 41 | 1,540 | 11.87 t/s | 9.47 t/s |
| 42 | 1,577 | 11.87 t/s | 11.81 t/s |
| 43 | 1,604 | 11.80 t/s | 8.84 t/s |
| 44 | 1,638 | 11.78 t/s | 10.95 t/s |
| 45 | 1,667 | 11.73 t/s | 9.31 t/s |
| 46 | 1,692 | 11.65 t/s | 8.14 t/s |
| 47 | 1,735 | 11.70 t/s | 13.72 t/s |
| 48 | 1,764 | 11.65 t/s | 9.52 t/s |
| 49 | 1,795 | 11.62 t/s | 9.95 t/s |
| 50 | 1,827 | 11.59 t/s | 10.18 t/s |
| 51 | 1,865 | 11.61 t/s | 12.42 t/s |
| 52 | 1,895 | 11.57 t/s | 9.73 t/s |
| 53 | 1,935 | 11.60 t/s | 12.99 t/s |
| 54 | 1,975 | 11.62 t/s | 12.75 t/s |
| 55 | 2,007 | 11.60 t/s | 10.39 t/s |
| 56 | 2,030 | 11.53 t/s | 7.54 t/s |
| 57 | 2,068 | 11.54 t/s | 12.29 t/s |
| 58 | 2,105 | 11.55 t/s | 12.14 t/s |
| 59 | 2,128 | 11.48 t/s | 7.41 t/s |
| 60 | 2,152 | 11.42 t/s | 7.94 t/s |
| 61 | 2,187 | 11.42 t/s | 11.21 t/s |
| 62 | 2,208 | 11.35 t/s | 6.98 t/s |
| 63 | 2,237 | 11.32 t/s | 9.33 t/s |
| 64 | 2,272 | 11.32 t/s | 11.23 t/s |
| 65 | 2,312 | 11.35 t/s | 13.09 t/s |
| 66 | 2,351 | 11.37 t/s | 12.69 t/s |
| 67 | 2,387 | 11.37 t/s | 11.60 t/s |
| 68 | 2,417 | 11.35 t/s | 9.85 t/s |
| 69 | 2,444 | 11.31 t/s | 8.59 t/s |
| 70 | 2,476 | 11.29 t/s | 10.27 t/s |
| 71 | 2,521 | 11.34 t/s | 14.51 t/s |
| 72 | 2,546 | 11.29 t/s | 7.90 t/s |
| 73 | 2,583 | 11.30 t/s | 11.98 t/s |
| 74 | 2,622 | 11.31 t/s | 12.42 t/s |
| 75 | 2,653 | 11.29 t/s | 9.73 t/s |
| 76 | 2,679 | 11.25 t/s | 8.24 t/s |
| 77 | 2,716 | 11.26 t/s | 12.20 t/s |
| 78 | 2,744 | 11.24 t/s | 9.05 t/s |
| 79 | 2,777 | 11.23 t/s | 10.98 t/s |
| 80 | 2,812 | 11.24 t/s | 11.49 t/s |
| 81 | 2,843 | 11.22 t/s | 10.00 t/s |
| 82 | 2,874 | 11.21 t/s | 10.05 t/s |
| 83 | 2,909 | 11.21 t/s | 11.53 t/s |
| 84 | 2,946 | 11.22 t/s | 12.01 t/s |
| 85 | 2,984 | 11.23 t/s | 12.54 t/s |
| 86 | 3,022 | 11.25 t/s | 12.19 t/s |
| 87 | 3,055 | 11.24 t/s | 10.58 t/s |
| 88 | 3,098 | 11.27 t/s | 13.89 t/s |
| 89 | 3,130 | 11.26 t/s | 10.33 t/s |
| 90 | 3,167 | 11.26 t/s | 11.94 t/s |
| 91 | 3,203 | 11.27 t/s | 11.54 t/s |
| 92 | 3,233 | 11.25 t/s | 9.74 t/s |
| 93 | 3,269 | 11.25 t/s | 11.42 t/s |
| 94 | 3,307 | 11.26 t/s | 12.08 t/s |
| 95 | 3,341 | 11.26 t/s | 10.94 t/s |
| 96 | 3,381 | 11.28 t/s | 13.28 t/s |

---

## Task #2109 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 21:46:49.961` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 101 | 15.96 t/s | 16.12 t/s |
| 2 | 135 | 14.40 t/s | 11.20 t/s |
| 3 | 173 | 13.94 t/s | 12.50 t/s |
| 4 | 225 | 14.59 t/s | 17.28 t/s |
| 5 | 276 | 14.94 t/s | 16.65 t/s |
| 6 | 321 | 14.93 t/s | 14.87 t/s |
| 7 | 365 | 14.87 t/s | 14.48 t/s |
| 8 | 404 | 14.62 t/s | 12.66 t/s |
| 9 | 445 | 14.50 t/s | 13.37 t/s |
| 10 | 488 | 14.44 t/s | 13.88 t/s |
| 11 | 535 | 14.51 t/s | 15.30 t/s |
| 12 | 566 | 14.17 t/s | 10.08 t/s |
| 13 | 599 | 13.93 t/s | 10.74 t/s |
| 14 | 627 | 13.62 t/s | 9.24 t/s |
| 15 | 674 | 13.72 t/s | 15.27 t/s |
| 16 | 705 | 13.52 t/s | 10.23 t/s |
| 17 | 741 | 13.43 t/s | 11.91 t/s |
| 18 | 789 | 13.52 t/s | 15.15 t/s |
| 19 | 835 | 13.58 t/s | 14.61 t/s |
| 20 | 875 | 13.54 t/s | 12.82 t/s |
| 21 | 917 | 13.55 t/s | 13.63 t/s |
| 22 | 973 | 13.75 t/s | 18.33 t/s |
| 23 | 1,010 | 13.69 t/s | 12.18 t/s |
| 24 | 1,043 | 13.57 t/s | 10.72 t/s |
| 25 | 1,087 | 13.59 t/s | 14.18 t/s |
| 26 | 1,125 | 13.55 t/s | 12.46 t/s |
| 27 | 1,152 | 13.38 t/s | 8.74 t/s |
| 28 | 1,187 | 13.31 t/s | 11.46 t/s |
| 29 | 1,220 | 13.22 t/s | 10.61 t/s |
| 30 | 1,252 | 13.13 t/s | 10.34 t/s |
| 31 | 1,287 | 13.08 t/s | 11.46 t/s |
| 32 | 1,329 | 13.09 t/s | 13.45 t/s |
| 33 | 1,370 | 13.09 t/s | 13.18 t/s |
| 34 | 1,407 | 13.06 t/s | 12.07 t/s |
| 35 | 1,452 | 13.10 t/s | 14.45 t/s |
| 36 | 1,488 | 13.06 t/s | 11.65 t/s |
| 37 | 1,528 | 13.07 t/s | 13.31 t/s |
| 38 | 1,561 | 13.00 t/s | 10.41 t/s |
| 39 | 1,613 | 13.09 t/s | 16.52 t/s |
| 40 | 1,648 | 13.04 t/s | 11.11 t/s |
| 41 | 1,687 | 13.04 t/s | 12.98 t/s |
| 42 | 1,735 | 13.09 t/s | 15.12 t/s |
| 43 | 1,769 | 13.03 t/s | 10.83 t/s |
| 44 | 1,804 | 12.99 t/s | 11.03 t/s |
| 45 | 1,850 | 13.02 t/s | 14.51 t/s |
| 46 | 1,889 | 13.01 t/s | 12.50 t/s |
| 47 | 1,916 | 12.93 t/s | 8.96 t/s |
| 48 | 1,957 | 12.94 t/s | 13.60 t/s |
| 49 | 1,993 | 12.91 t/s | 11.51 t/s |
| 50 | 2,027 | 12.87 t/s | 10.77 t/s |
| 51 | 2,071 | 12.89 t/s | 14.09 t/s |
| 52 | 2,105 | 12.85 t/s | 10.81 t/s |
| 53 | 2,153 | 12.90 t/s | 15.23 t/s |
| 54 | 2,184 | 12.84 t/s | 9.87 t/s |
| 55 | 2,213 | 12.79 t/s | 9.67 t/s |
| 56 | 2,246 | 12.75 t/s | 10.50 t/s |
| 57 | 2,284 | 12.74 t/s | 12.08 t/s |
| 58 | 2,324 | 12.73 t/s | 12.62 t/s |
| 59 | 2,364 | 12.73 t/s | 12.80 t/s |
| 60 | 2,398 | 12.71 t/s | 11.27 t/s |
| 61 | 2,437 | 12.71 t/s | 12.37 t/s |
| 62 | 2,478 | 12.71 t/s | 12.98 t/s |
| 63 | 2,523 | 12.74 t/s | 14.69 t/s |
| 64 | 2,553 | 12.69 t/s | 9.45 t/s |
| 65 | 2,595 | 12.71 t/s | 13.84 t/s |
| 66 | 2,624 | 12.66 t/s | 9.64 t/s |
| 67 | 2,661 | 12.65 t/s | 11.77 t/s |
| 68 | 2,690 | 12.60 t/s | 9.53 t/s |
| 69 | 2,746 | 12.68 t/s | 17.74 t/s |
| 70 | 2,810 | 12.79 t/s | 21.09 t/s |
| 71 | 2,856 | 12.83 t/s | 15.15 t/s |
| 72 | 2,894 | 12.82 t/s | 12.06 t/s |
| 73 | 2,934 | 12.82 t/s | 13.23 t/s |
| 74 | 2,968 | 12.79 t/s | 10.72 t/s |
| 75 | 2,995 | 12.74 t/s | 8.54 t/s |
| 76 | 3,026 | 12.71 t/s | 10.31 t/s |
| 77 | 3,063 | 12.69 t/s | 11.68 t/s |
| 78 | 3,110 | 12.73 t/s | 15.56 t/s |
| 79 | 3,149 | 12.72 t/s | 12.34 t/s |
| 80 | 3,206 | 12.79 t/s | 17.98 t/s |
| 81 | 3,261 | 12.85 t/s | 18.13 t/s |
| 82 | 3,305 | 12.87 t/s | 13.99 t/s |
| 83 | 3,342 | 12.86 t/s | 12.23 t/s |
| 84 | 3,370 | 12.82 t/s | 9.19 t/s |
| 85 | 3,413 | 12.83 t/s | 13.59 t/s |
| 86 | 3,445 | 12.80 t/s | 10.58 t/s |
| 87 | 3,494 | 12.83 t/s | 15.30 t/s |
| 88 | 3,542 | 12.86 t/s | 15.59 t/s |
| 89 | 3,569 | 12.82 t/s | 8.96 t/s |
| 90 | 3,605 | 12.81 t/s | 11.96 t/s |
| 91 | 3,630 | 12.76 t/s | 8.19 t/s |
| 92 | 3,672 | 12.77 t/s | 13.78 t/s |
| 93 | 3,712 | 12.77 t/s | 12.59 t/s |
| 94 | 3,745 | 12.75 t/s | 10.80 t/s |
| 95 | 3,791 | 12.77 t/s | 15.26 t/s |
| 96 | 3,836 | 12.79 t/s | 14.65 t/s |
| 97 | 3,880 | 12.81 t/s | 14.61 t/s |
| 98 | 3,926 | 12.84 t/s | 15.30 t/s |
| 99 | 3,972 | 12.86 t/s | 15.19 t/s |
| 100 | 4,006 | 12.84 t/s | 11.29 t/s |
| 101 | 4,063 | 12.90 t/s | 18.65 t/s |
| 102 | 4,113 | 12.93 t/s | 16.48 t/s |
| 103 | 4,168 | 12.98 t/s | 18.18 t/s |
| 104 | 4,222 | 13.03 t/s | 17.70 t/s |
| 105 | 4,257 | 13.01 t/s | 11.50 t/s |
| 106 | 4,290 | 12.99 t/s | 10.66 t/s |
| 107 | 4,328 | 12.99 t/s | 12.35 t/s |
| 108 | 4,366 | 12.98 t/s | 12.55 t/s |
| 109 | 4,407 | 12.98 t/s | 13.25 t/s |
| 110 | 4,438 | 12.96 t/s | 10.12 t/s |
| 111 | 4,473 | 12.94 t/s | 11.31 t/s |
| 112 | 4,506 | 12.93 t/s | 10.88 t/s |
| 113 | 4,540 | 12.91 t/s | 11.23 t/s |
| 114 | 4,573 | 12.89 t/s | 10.82 t/s |
| 115 | 4,609 | 12.88 t/s | 11.77 t/s |
| 116 | 4,641 | 12.86 t/s | 10.53 t/s |
| 117 | 4,676 | 12.85 t/s | 11.52 t/s |
| 118 | 4,712 | 12.84 t/s | 11.80 t/s |
| 119 | 4,749 | 12.84 t/s | 12.16 t/s |
| 120 | 4,786 | 12.83 t/s | 12.04 t/s |
| 121 | 4,828 | 12.84 t/s | 13.88 t/s |
| 122 | 4,856 | 12.81 t/s | 9.12 t/s |
| 123 | 4,899 | 12.82 t/s | 13.97 t/s |
| 124 | 4,952 | 12.86 t/s | 17.46 t/s |
| 125 | 4,999 | 12.87 t/s | 15.21 t/s |
| 126 | 5,031 | 12.86 t/s | 10.49 t/s |
| 127 | 5,081 | 12.88 t/s | 16.28 t/s |
| 128 | 5,129 | 12.90 t/s | 15.65 t/s |
| 129 | 5,185 | 12.95 t/s | 18.55 t/s |
| 130 | 5,237 | 12.98 t/s | 16.83 t/s |
| 131 | 5,276 | 12.97 t/s | 12.60 t/s |
| 132 | 5,323 | 12.99 t/s | 15.51 t/s |
| 133 | 5,352 | 12.97 t/s | 9.46 t/s |
| 134 | 5,388 | 12.96 t/s | 11.84 t/s |
| 135 | 5,422 | 12.94 t/s | 11.14 t/s |
| 136 | 5,459 | 12.94 t/s | 11.94 t/s |
| 137 | 5,497 | 12.93 t/s | 12.48 t/s |
| 138 | 5,529 | 12.92 t/s | 10.42 t/s |
| 139 | 5,563 | 12.90 t/s | 11.09 t/s |
| 140 | 5,597 | 12.89 t/s | 11.00 t/s |
| 141 | 5,625 | 12.86 t/s | 9.07 t/s |
| 142 | 5,664 | 12.86 t/s | 12.79 t/s |
| 143 | 5,691 | 12.83 t/s | 8.70 t/s |
| 144 | 5,730 | 12.83 t/s | 12.78 t/s |
| 145 | 5,770 | 12.83 t/s | 12.96 t/s |
| 146 | 5,806 | 12.83 t/s | 11.62 t/s |
| 147 | 5,847 | 12.83 t/s | 13.38 t/s |
| 148 | 5,878 | 12.81 t/s | 9.98 t/s |
| 149 | 5,910 | 12.79 t/s | 10.50 t/s |
| 150 | 5,942 | 12.78 t/s | 10.35 t/s |
| 151 | 5,976 | 12.77 t/s | 11.00 t/s |
| 152 | 6,017 | 12.77 t/s | 13.41 t/s |
| 153 | 6,044 | 12.74 t/s | 8.61 t/s |
| 154 | 6,075 | 12.73 t/s | 10.04 t/s |
| 155 | 6,118 | 12.73 t/s | 13.95 t/s |
| 156 | 6,161 | 12.74 t/s | 13.92 t/s |
| 157 | 6,190 | 12.72 t/s | 9.48 t/s |
| 158 | 6,224 | 12.71 t/s | 10.96 t/s |
| 159 | 6,261 | 12.71 t/s | 12.08 t/s |
| 160 | 6,316 | 12.74 t/s | 17.87 t/s |
| 161 | 6,358 | 12.74 t/s | 13.44 t/s |
| 162 | 6,392 | 12.73 t/s | 11.07 t/s |
| 163 | 6,419 | 12.71 t/s | 8.67 t/s |
| 164 | 6,460 | 12.71 t/s | 13.13 t/s |
| 165 | 6,508 | 12.73 t/s | 15.61 t/s |
| 166 | 6,553 | 12.74 t/s | 14.39 t/s |
| 167 | 6,590 | 12.73 t/s | 11.79 t/s |
| 168 | 6,645 | 12.76 t/s | 17.91 t/s |
| 169 | 6,706 | 12.80 t/s | 19.56 t/s |
| 170 | 6,763 | 12.84 t/s | 18.49 t/s |
| 171 | 6,808 | 12.84 t/s | 14.25 t/s |
| 172 | 6,848 | 12.84 t/s | 12.79 t/s |
| 173 | 6,888 | 12.84 t/s | 12.82 t/s |
| 174 | 6,925 | 12.84 t/s | 11.74 t/s |
| 175 | 6,958 | 12.82 t/s | 10.58 t/s |
| 176 | 7,006 | 12.84 t/s | 15.38 t/s |
| 177 | 7,041 | 12.83 t/s | 11.27 t/s |
| 178 | 7,080 | 12.83 t/s | 12.58 t/s |
| 179 | 7,112 | 12.81 t/s | 10.22 t/s |
| 180 | 7,146 | 12.80 t/s | 10.96 t/s |
| 181 | 7,183 | 12.80 t/s | 11.98 t/s |
| 182 | 7,223 | 12.80 t/s | 12.65 t/s |
| 183 | 7,265 | 12.80 t/s | 13.52 t/s |
| 184 | 7,304 | 12.80 t/s | 12.99 t/s |
| 185 | 7,333 | 12.78 t/s | 9.20 t/s |
| 186 | 7,367 | 12.77 t/s | 10.97 t/s |
| 187 | 7,406 | 12.77 t/s | 12.36 t/s |
| 188 | 7,437 | 12.76 t/s | 10.00 t/s |
| 189 | 7,470 | 12.74 t/s | 10.43 t/s |
| 190 | 7,512 | 12.75 t/s | 13.32 t/s |
| 191 | 7,550 | 12.74 t/s | 12.12 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 21:58:50.002` (Queue Delay: `N/A`)
* **Total Context Footprint:** `19590` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `166.46 t/s` (`6.01 ms/tok`) | Time To First Token (TTFT) = `117.23s` |
| **Decode Speed (Generation)** | `14.49 t/s` (`69.02 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `19515` (99.6%) / Out: `75` (0.4%) | Total context footprint: `19590` tokens |
| **Speculative MTP Acceptance** | `54.02%` (`47/87`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.62` tokens/step | Effective speedup: ~`2.62x` vs single-token decode |
| **Graphs Reused** | `29` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 10.0% | 7.21 | 284.16 |
| 2 | 4,096 | 21.0% | 16.97 | 241.42 |
| 3 | 6,144 | 31.0% | 27.21 | 225.82 |
| 4 | 8,192 | 42.0% | 37.97 | 215.75 |
| 5 | 10,240 | 52.0% | 49.28 | 207.77 |
| 6 | 12,288 | 63.0% | 61.11 | 201.08 |
| 7 | 14,336 | 73.0% | 73.49 | 195.06 |
| 8 | 16,384 | 84.0% | 86.41 | 189.62 |
| 9 | 18,432 | 94.0% | 99.82 | 184.65 |
| 10 | 18,999 | 97.0% | 107.01 | 177.55 |
| 11 | 19,424 | 100.0% | 109.40 | 177.55 |
| 12 | 19,511 | 100.0% | 114.41 | 170.53 |

---

## Task #43 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:04:47.505` (Queue Delay: `N/A`)
* **Total Context Footprint:** `2232` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `103.76 t/s` (`9.64 ms/tok`) | Time To First Token (TTFT) = `7.73s` |
| **Decode Speed (Generation)** | `20.90 t/s` (`47.85 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `802` (35.9%) / Out: `1430` (64.1%) | Total context footprint: `2232` tokens |
| **Speculative MTP Acceptance** | `68.30%` (`961/1407`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.05` tokens/step | Effective speedup: ~`3.05x` vs single-token decode |
| **Graphs Reused** | `492` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 798 | 100.0% | 5.86 | 136.17 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 22.13 t/s | 22.36 t/s |
| 2 | 176 | 23.12 t/s | 24.54 t/s |
| 3 | 225 | 21.13 t/s | 16.17 t/s |
| 4 | 287 | 21.00 t/s | 20.53 t/s |
| 5 | 355 | 21.14 t/s | 21.75 t/s |
| 6 | 411 | 20.72 t/s | 18.41 t/s |
| 7 | 477 | 20.75 t/s | 20.98 t/s |
| 8 | 539 | 20.69 t/s | 20.21 t/s |
| 9 | 605 | 20.78 t/s | 21.56 t/s |
| 10 | 673 | 20.95 t/s | 22.60 t/s |
| 11 | 729 | 20.74 t/s | 18.49 t/s |
| 12 | 795 | 20.80 t/s | 21.56 t/s |
| 13 | 856 | 20.72 t/s | 19.71 t/s |
| 14 | 920 | 20.73 t/s | 20.79 t/s |
| 15 | 979 | 20.65 t/s | 19.54 t/s |
| 16 | 1,040 | 20.60 t/s | 19.81 t/s |
| 17 | 1,105 | 20.64 t/s | 21.39 t/s |
| 18 | 1,179 | 20.82 t/s | 23.90 t/s |
| 19 | 1,244 | 20.82 t/s | 20.87 t/s |
| 20 | 1,306 | 20.80 t/s | 20.33 t/s |
| 21 | 1,371 | 20.82 t/s | 21.32 t/s |

---

## Task #44 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:06:06.177` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 89 | 100.0% | 4.22 | 21.10 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 16.54 t/s | 16.71 t/s |
| 2 | 147 | 16.06 t/s | 15.14 t/s |
| 3 | 175 | 14.27 t/s | 9.02 t/s |
| 4 | 208 | 13.55 t/s | 10.70 t/s |
| 5 | 240 | 12.97 t/s | 10.16 t/s |
| 6 | 266 | 12.30 t/s | 8.34 t/s |
| 7 | 311 | 12.59 t/s | 14.63 t/s |
| 8 | 351 | 12.62 t/s | 12.81 t/s |
| 9 | 384 | 12.41 t/s | 10.55 t/s |
| 10 | 420 | 12.34 t/s | 11.67 t/s |
| 11 | 464 | 12.49 t/s | 14.10 t/s |
| 12 | 496 | 12.33 t/s | 10.38 t/s |
| 13 | 538 | 12.41 t/s | 13.44 t/s |
| 14 | 567 | 12.20 t/s | 9.27 t/s |
| 15 | 607 | 12.25 t/s | 12.99 t/s |
| 16 | 646 | 12.26 t/s | 12.44 t/s |
| 17 | 679 | 12.17 t/s | 10.66 t/s |
| 18 | 712 | 12.08 t/s | 10.51 t/s |
| 19 | 749 | 12.07 t/s | 11.80 t/s |
| 20 | 786 | 12.06 t/s | 11.97 t/s |
| 21 | 826 | 12.09 t/s | 12.79 t/s |
| 22 | 873 | 12.23 t/s | 15.15 t/s |
| 23 | 906 | 12.16 t/s | 10.65 t/s |
| 24 | 937 | 12.07 t/s | 9.93 t/s |
| 25 | 974 | 12.07 t/s | 11.98 t/s |
| 26 | 1,003 | 11.96 t/s | 9.27 t/s |
| 27 | 1,042 | 11.98 t/s | 12.46 t/s |
| 28 | 1,082 | 12.02 t/s | 12.98 t/s |
| 29 | 1,125 | 12.07 t/s | 13.68 t/s |
| 30 | 1,169 | 12.13 t/s | 13.70 t/s |
| 31 | 1,213 | 12.18 t/s | 13.98 t/s |
| 32 | 1,261 | 12.28 t/s | 15.20 t/s |
| 33 | 1,312 | 12.40 t/s | 16.39 t/s |
| 34 | 1,350 | 12.39 t/s | 12.08 t/s |
| 35 | 1,390 | 12.41 t/s | 13.28 t/s |
| 36 | 1,438 | 12.49 t/s | 15.36 t/s |
| 37 | 1,488 | 12.58 t/s | 15.83 t/s |
| 38 | 1,527 | 12.58 t/s | 12.51 t/s |
| 39 | 1,572 | 12.62 t/s | 14.26 t/s |
| 40 | 1,605 | 12.57 t/s | 10.52 t/s |
| 41 | 1,644 | 12.57 t/s | 12.50 t/s |
| 42 | 1,689 | 12.61 t/s | 14.27 t/s |
| 43 | 1,723 | 12.57 t/s | 10.74 t/s |
| 44 | 1,758 | 12.54 t/s | 11.18 t/s |
| 45 | 1,792 | 12.51 t/s | 11.31 t/s |
| 46 | 1,831 | 12.51 t/s | 12.47 t/s |
| 47 | 1,881 | 12.58 t/s | 15.79 t/s |
| 48 | 1,920 | 12.59 t/s | 12.97 t/s |
| 49 | 1,954 | 12.55 t/s | 10.85 t/s |
| 50 | 1,986 | 12.50 t/s | 10.13 t/s |
| 51 | 2,019 | 12.46 t/s | 10.45 t/s |
| 52 | 2,054 | 12.44 t/s | 11.20 t/s |
| 53 | 2,092 | 12.43 t/s | 11.99 t/s |
| 54 | 2,122 | 12.38 t/s | 9.57 t/s |
| 55 | 2,157 | 12.36 t/s | 11.49 t/s |
| 56 | 2,190 | 12.34 t/s | 10.91 t/s |
| 57 | 2,230 | 12.35 t/s | 12.73 t/s |
| 58 | 2,266 | 12.34 t/s | 11.91 t/s |
| 59 | 2,298 | 12.30 t/s | 10.20 t/s |
| 60 | 2,324 | 12.24 t/s | 8.66 t/s |
| 61 | 2,369 | 12.28 t/s | 14.27 t/s |
| 62 | 2,408 | 12.28 t/s | 12.44 t/s |
| 63 | 2,441 | 12.26 t/s | 10.96 t/s |
| 64 | 2,476 | 12.24 t/s | 10.92 t/s |
| 65 | 2,505 | 12.19 t/s | 9.17 t/s |
| 66 | 2,536 | 12.16 t/s | 10.28 t/s |
| 67 | 2,572 | 12.15 t/s | 11.45 t/s |

---

## Task #1735 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:10:37.771` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 102 | 13.57 t/s | 13.70 t/s |
| 2 | 149 | 13.99 t/s | 15.00 t/s |
| 3 | 198 | 14.37 t/s | 15.66 t/s |
| 4 | 242 | 14.35 t/s | 14.24 t/s |

---

## Task #1841 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:11:07.307` (Queue Delay: `N/A`)
* **Total Context Footprint:** `465` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `24.75 t/s` (`40.40 ms/tok`) | Time To First Token (TTFT) = `4.69s` |
| **Decode Speed (Generation)** | `15.51 t/s` (`64.47 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `116` (24.9%) / Out: `349` (75.1%) | Total context footprint: `465` tokens |
| **Speculative MTP Acceptance** | `56.59%` (`219/387`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.70` tokens/step | Effective speedup: ~`2.70x` vs single-token decode |
| **Graphs Reused** | `1,917` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 101 | 14.48 t/s | 14.63 t/s |
| 2 | 151 | 15.00 t/s | 16.15 t/s |
| 3 | 195 | 14.81 t/s | 14.21 t/s |
| 4 | 249 | 15.33 t/s | 17.54 t/s |
| 5 | 299 | 15.43 t/s | 15.97 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:22:35.345` (Queue Delay: `N/A`)
* **Total Context Footprint:** `1109` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `102.35 t/s` (`9.77 ms/tok`) | Time To First Token (TTFT) = `8.04s` |
| **Decode Speed (Generation)** | `19.44 t/s` (`51.45 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `823` (74.2%) / Out: `286` (25.8%) | Total context footprint: `1109` tokens |
| **Speculative MTP Acceptance** | `60.13%` (`184/306`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.80` tokens/step | Effective speedup: ~`2.80x` vs single-token decode |
| **Graphs Reused** | `101` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 819 | 100.0% | 6.05 | 135.39 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 18.12 t/s | 18.30 t/s |
| 2 | 164 | 18.97 t/s | 20.44 t/s |
| 3 | 225 | 19.13 t/s | 19.56 t/s |

---

## Task #2 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:22:59.976` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 10.0% | 7.48 | 273.66 |
| 2 | 4,096 | 21.0% | 17.80 | 230.06 |
| 3 | 6,144 | 31.0% | 28.62 | 214.70 |
| 4 | 8,192 | 42.0% | 39.95 | 205.07 |
| 5 | 10,240 | 52.0% | 51.85 | 197.51 |
| 6 | 12,288 | 63.0% | 64.34 | 191.00 |
| 7 | 14,336 | 73.0% | 77.24 | 185.60 |
| 8 | 16,384 | 84.0% | 90.76 | 180.51 |
| 9 | 18,432 | 94.0% | 104.76 | 175.94 |
| 10 | 19,049 | 97.0% | 112.20 | 169.78 |
| 11 | 19,424 | 99.0% | 116.21 | 167.15 |
| 12 | 19,561 | 100.0% | 122.08 | 160.23 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 101 | 13.86 t/s | 14.00 t/s |
| 2 | 141 | 13.57 t/s | 12.90 t/s |
| 3 | 174 | 12.85 t/s | 10.47 t/s |
| 4 | 210 | 12.63 t/s | 11.69 t/s |
| 5 | 252 | 12.77 t/s | 13.50 t/s |
| 6 | 296 | 12.94 t/s | 14.05 t/s |
| 7 | 318 | 12.24 t/s | 7.08 t/s |
| 8 | 357 | 12.27 t/s | 12.51 t/s |
| 9 | 399 | 12.38 t/s | 13.39 t/s |
| 10 | 434 | 12.28 t/s | 11.29 t/s |
| 11 | 481 | 12.50 t/s | 14.98 t/s |
| 12 | 538 | 12.94 t/s | 18.38 t/s |
| 13 | 584 | 13.06 t/s | 14.67 t/s |
| 14 | 617 | 12.90 t/s | 10.51 t/s |
| 15 | 655 | 12.86 t/s | 12.27 t/s |
| 16 | 686 | 12.68 t/s | 9.83 t/s |
| 17 | 727 | 12.71 t/s | 13.22 t/s |
| 18 | 774 | 12.83 t/s | 14.98 t/s |
| 19 | 813 | 12.80 t/s | 12.34 t/s |
| 20 | 851 | 12.78 t/s | 12.21 t/s |
| 21 | 884 | 12.67 t/s | 10.49 t/s |
| 22 | 924 | 12.68 t/s | 12.77 t/s |
| 23 | 963 | 12.67 t/s | 12.56 t/s |
| 24 | 1,005 | 12.70 t/s | 13.34 t/s |
| 25 | 1,049 | 12.75 t/s | 14.10 t/s |
| 26 | 1,083 | 12.70 t/s | 11.22 t/s |
| 27 | 1,125 | 12.72 t/s | 13.39 t/s |
| 28 | 1,179 | 12.87 t/s | 17.17 t/s |
| 29 | 1,224 | 12.92 t/s | 14.23 t/s |
| 30 | 1,277 | 13.04 t/s | 16.75 t/s |
| 31 | 1,317 | 13.04 t/s | 12.82 t/s |
| 32 | 1,360 | 13.05 t/s | 13.56 t/s |
| 33 | 1,394 | 12.99 t/s | 10.93 t/s |
| 34 | 1,429 | 12.95 t/s | 11.64 t/s |
| 35 | 1,465 | 12.91 t/s | 11.37 t/s |
| 36 | 1,512 | 12.97 t/s | 14.99 t/s |
| 37 | 1,552 | 12.98 t/s | 13.32 t/s |
| 38 | 1,589 | 12.94 t/s | 11.73 t/s |
| 39 | 1,625 | 12.92 t/s | 11.94 t/s |
| 40 | 1,659 | 12.88 t/s | 11.28 t/s |
| 41 | 1,704 | 12.92 t/s | 14.34 t/s |
| 42 | 1,737 | 12.87 t/s | 10.98 t/s |
| 43 | 1,767 | 12.79 t/s | 9.45 t/s |
| 44 | 1,805 | 12.78 t/s | 12.15 t/s |
| 45 | 1,850 | 12.83 t/s | 14.99 t/s |
| 46 | 1,889 | 12.82 t/s | 12.45 t/s |
| 47 | 1,932 | 12.83 t/s | 13.65 t/s |
| 48 | 1,991 | 12.97 t/s | 19.63 t/s |
| 49 | 2,036 | 12.99 t/s | 14.33 t/s |
| 50 | 2,073 | 12.97 t/s | 11.67 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:43:04.801` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `1592` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `64.83 t/s` (`15.42 ms/tok`) | Time To First Token (TTFT) = `21.26s` |
| **Decode Speed (Generation)** | `15.84 t/s` (`63.13 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1378` (86.6%) / Out: `214` (13.4%) | Total context footprint: `1592` tokens |
| **Speculative MTP Acceptance** | `42.20%` (`119/282`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.27` tokens/step | Effective speedup: ~`2.27x` vs single-token decode |
| **Graphs Reused** | `93` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 567 | 41.0% | 5.21 | 108.78 |
| 2 | 725 | 53.0% | 6.45 | 112.48 |
| 3 | 862 | 63.0% | 10.76 | 80.14 |
| 4 | 1,374 | 100.0% | 15.05 | 91.30 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 103 | 16.17 t/s | 16.33 t/s |
| 2 | 150 | 15.79 t/s | 15.03 t/s |
| 3 | 198 | 15.82 t/s | 15.90 t/s |

---

## Task #101 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:44:11.354` (Queue Delay: `4.27s`)
* **Total Context Footprint:** `808` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `47.11 t/s` (`21.23 ms/tok`) | Time To First Token (TTFT) = `13.94s` |
| **Decode Speed (Generation)** | `15.15 t/s` (`65.99 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `657` (81.3%) / Out: `151` (18.7%) | Total context footprint: `808` tokens |
| **Speculative MTP Acceptance** | `40.58%` (`84/207`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.22` tokens/step | Effective speedup: ~`2.22x` vs single-token decode |
| **Graphs Reused** | `161` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 141 | 63.0% | 3.43 | 41.12 |
| 2 | 653 | 100.0% | 7.73 | 84.52 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 14.97 t/s | 15.12 t/s |
| 2 | 150 | 15.27 t/s | 15.91 t/s |

---

## Task #174 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:45:50.259` (Queue Delay: `4.30s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 343 | 91.0% | 4.33 | 79.17 |
| 2 | 374 | 99.0% | 8.62 | 43.38 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 15.89 t/s | 16.05 t/s |
| 2 | 137 | 14.73 t/s | 12.32 t/s |
| 3 | 180 | 14.52 t/s | 13.89 t/s |
| 4 | 226 | 14.56 t/s | 14.72 t/s |
| 5 | 260 | 13.96 t/s | 10.99 t/s |
| 6 | 302 | 13.96 t/s | 13.97 t/s |
| 7 | 346 | 13.98 t/s | 14.07 t/s |
| 8 | 392 | 14.08 t/s | 14.90 t/s |
| 9 | 434 | 14.01 t/s | 13.40 t/s |
| 10 | 469 | 13.80 t/s | 11.67 t/s |
| 11 | 520 | 14.02 t/s | 16.33 t/s |
| 12 | 565 | 14.06 t/s | 14.56 t/s |
| 13 | 621 | 14.35 t/s | 18.11 t/s |
| 14 | 656 | 14.15 t/s | 11.31 t/s |
| 15 | 708 | 14.30 t/s | 16.64 t/s |
| 16 | 756 | 14.37 t/s | 15.42 t/s |
| 17 | 787 | 14.12 t/s | 9.92 t/s |
| 18 | 827 | 14.06 t/s | 12.94 t/s |
| 19 | 863 | 13.96 t/s | 11.95 t/s |
| 20 | 900 | 13.87 t/s | 12.15 t/s |
| 21 | 947 | 13.92 t/s | 14.97 t/s |
| 22 | 989 | 13.92 t/s | 13.96 t/s |
| 23 | 1,026 | 13.84 t/s | 11.90 t/s |
| 24 | 1,062 | 13.77 t/s | 11.97 t/s |
| 25 | 1,096 | 13.67 t/s | 11.29 t/s |
| 26 | 1,150 | 13.81 t/s | 17.34 t/s |
| 27 | 1,191 | 13.80 t/s | 13.40 t/s |
| 28 | 1,224 | 13.67 t/s | 10.40 t/s |
| 29 | 1,267 | 13.68 t/s | 13.75 t/s |
| 30 | 1,316 | 13.76 t/s | 16.17 t/s |
| 31 | 1,354 | 13.71 t/s | 12.17 t/s |
| 32 | 1,387 | 13.62 t/s | 10.92 t/s |
| 33 | 1,425 | 13.59 t/s | 12.53 t/s |
| 34 | 1,474 | 13.67 t/s | 16.31 t/s |
| 35 | 1,517 | 13.68 t/s | 14.26 t/s |
| 36 | 1,556 | 13.67 t/s | 12.98 t/s |
| 37 | 1,617 | 13.83 t/s | 20.13 t/s |
| 38 | 1,680 | 14.00 t/s | 20.33 t/s |
| 39 | 1,737 | 14.12 t/s | 18.78 t/s |
| 40 | 1,798 | 14.26 t/s | 19.94 t/s |
| 41 | 1,853 | 14.35 t/s | 18.18 t/s |
| 42 | 1,909 | 14.44 t/s | 18.16 t/s |
| 43 | 1,953 | 14.44 t/s | 14.30 t/s |
| 44 | 1,991 | 14.40 t/s | 12.62 t/s |
| 45 | 2,037 | 14.41 t/s | 14.98 t/s |
| 46 | 2,075 | 14.37 t/s | 12.66 t/s |
| 47 | 2,126 | 14.42 t/s | 16.69 t/s |
| 48 | 2,173 | 14.44 t/s | 15.30 t/s |
| 49 | 2,216 | 14.43 t/s | 14.11 t/s |
| 50 | 2,259 | 14.42 t/s | 13.93 t/s |
| 51 | 2,307 | 14.45 t/s | 15.79 t/s |
| 52 | 2,344 | 14.40 t/s | 11.92 t/s |
| 53 | 2,387 | 14.39 t/s | 13.86 t/s |
| 54 | 2,424 | 14.35 t/s | 12.07 t/s |
| 55 | 2,456 | 14.28 t/s | 10.32 t/s |
| 56 | 2,485 | 14.19 t/s | 9.57 t/s |
| 57 | 2,516 | 14.13 t/s | 10.23 t/s |
| 58 | 2,556 | 14.11 t/s | 13.08 t/s |
| 59 | 2,594 | 14.08 t/s | 12.37 t/s |
| 60 | 2,627 | 14.02 t/s | 10.62 t/s |
| 61 | 2,671 | 14.03 t/s | 14.45 t/s |
| 62 | 2,709 | 14.00 t/s | 12.39 t/s |
| 63 | 2,744 | 13.96 t/s | 11.32 t/s |
| 64 | 2,780 | 13.93 t/s | 11.85 t/s |
| 65 | 2,819 | 13.91 t/s | 12.62 t/s |
| 66 | 2,854 | 13.87 t/s | 11.33 t/s |
| 67 | 2,894 | 13.86 t/s | 13.15 t/s |
| 68 | 2,936 | 13.86 t/s | 13.55 t/s |
| 69 | 2,979 | 13.86 t/s | 13.92 t/s |
| 70 | 3,014 | 13.82 t/s | 11.22 t/s |
| 71 | 3,065 | 13.86 t/s | 16.36 t/s |
| 72 | 3,115 | 13.89 t/s | 16.24 t/s |
| 73 | 3,162 | 13.90 t/s | 15.04 t/s |
| 74 | 3,229 | 14.01 t/s | 21.66 t/s |
| 75 | 3,305 | 14.14 t/s | 24.17 t/s |
| 76 | 3,358 | 14.18 t/s | 17.04 t/s |
| 77 | 3,409 | 14.21 t/s | 16.69 t/s |
| 78 | 3,486 | 14.35 t/s | 24.73 t/s |
| 79 | 3,544 | 14.40 t/s | 18.70 t/s |
| 80 | 3,599 | 14.45 t/s | 17.84 t/s |
| 81 | 3,638 | 14.42 t/s | 12.51 t/s |
| 82 | 3,677 | 14.40 t/s | 12.67 t/s |
| 83 | 3,716 | 14.38 t/s | 12.65 t/s |
| 84 | 3,761 | 14.38 t/s | 14.34 t/s |
| 85 | 3,814 | 14.41 t/s | 17.13 t/s |
| 86 | 3,863 | 14.43 t/s | 15.63 t/s |
| 87 | 3,918 | 14.46 t/s | 17.75 t/s |
| 88 | 3,955 | 14.44 t/s | 12.30 t/s |
| 89 | 3,989 | 14.41 t/s | 11.21 t/s |
| 90 | 4,033 | 14.40 t/s | 14.14 t/s |
| 91 | 4,071 | 14.38 t/s | 12.17 t/s |
| 92 | 4,115 | 14.38 t/s | 14.24 t/s |
| 93 | 4,160 | 14.38 t/s | 14.30 t/s |
| 94 | 4,209 | 14.39 t/s | 15.57 t/s |
| 95 | 4,248 | 14.37 t/s | 12.56 t/s |
| 96 | 4,291 | 14.37 t/s | 14.28 t/s |
| 97 | 4,341 | 14.39 t/s | 16.67 t/s |
| 98 | 4,386 | 14.39 t/s | 14.47 t/s |
| 99 | 4,424 | 14.37 t/s | 12.19 t/s |
| 100 | 4,470 | 14.37 t/s | 14.75 t/s |
| 101 | 4,513 | 14.37 t/s | 14.31 t/s |
| 102 | 4,557 | 14.37 t/s | 13.99 t/s |
| 103 | 4,604 | 14.38 t/s | 15.21 t/s |
| 104 | 4,649 | 14.38 t/s | 14.42 t/s |
| 105 | 4,707 | 14.42 t/s | 18.58 t/s |
| 106 | 4,763 | 14.45 t/s | 18.31 t/s |
| 107 | 4,803 | 14.44 t/s | 13.17 t/s |
| 108 | 4,843 | 14.43 t/s | 12.75 t/s |
| 109 | 4,891 | 14.44 t/s | 15.71 t/s |
| 110 | 4,943 | 14.46 t/s | 16.59 t/s |
| 111 | 4,989 | 14.46 t/s | 14.99 t/s |
| 112 | 5,042 | 14.49 t/s | 17.30 t/s |
| 113 | 5,090 | 14.50 t/s | 15.98 t/s |
| 114 | 5,129 | 14.49 t/s | 12.78 t/s |
| 115 | 5,174 | 14.48 t/s | 14.08 t/s |
| 116 | 5,231 | 14.51 t/s | 18.13 t/s |
| 117 | 5,282 | 14.53 t/s | 16.56 t/s |
| 118 | 5,331 | 14.55 t/s | 16.23 t/s |
| 119 | 5,376 | 14.55 t/s | 14.69 t/s |
| 120 | 5,425 | 14.56 t/s | 16.12 t/s |
| 121 | 5,475 | 14.58 t/s | 16.61 t/s |
| 122 | 5,532 | 14.61 t/s | 18.78 t/s |
| 123 | 5,581 | 14.62 t/s | 16.26 t/s |
| 124 | 5,643 | 14.67 t/s | 20.08 t/s |
| 125 | 5,692 | 14.68 t/s | 16.07 t/s |
| 126 | 5,733 | 14.67 t/s | 13.59 t/s |
| 127 | 5,792 | 14.70 t/s | 19.27 t/s |
| 128 | 5,846 | 14.73 t/s | 17.97 t/s |
| 129 | 5,901 | 14.75 t/s | 17.86 t/s |
| 130 | 5,959 | 14.79 t/s | 18.97 t/s |
| 131 | 6,011 | 14.80 t/s | 17.30 t/s |
| 132 | 6,064 | 14.82 t/s | 17.11 t/s |
| 133 | 6,110 | 14.82 t/s | 15.28 t/s |
| 134 | 6,156 | 14.83 t/s | 14.99 t/s |
| 135 | 6,201 | 14.82 t/s | 14.52 t/s |
| 136 | 6,263 | 14.86 t/s | 20.37 t/s |
| 137 | 6,320 | 14.89 t/s | 18.36 t/s |
| 138 | 6,373 | 14.91 t/s | 17.48 t/s |
| 139 | 6,430 | 14.93 t/s | 18.42 t/s |
| 140 | 6,492 | 14.97 t/s | 20.03 t/s |
| 141 | 6,546 | 14.99 t/s | 17.76 t/s |
| 142 | 6,612 | 15.03 t/s | 21.53 t/s |
| 143 | 6,671 | 15.06 t/s | 19.37 t/s |
| 144 | 6,736 | 15.11 t/s | 20.96 t/s |
| 145 | 6,782 | 15.10 t/s | 14.95 t/s |
| 146 | 6,835 | 15.12 t/s | 17.35 t/s |
| 147 | 6,883 | 15.12 t/s | 15.67 t/s |
| 148 | 6,923 | 15.11 t/s | 12.91 t/s |
| 149 | 6,966 | 15.10 t/s | 14.03 t/s |
| 150 | 7,017 | 15.11 t/s | 16.46 t/s |
| 151 | 7,067 | 15.12 t/s | 16.25 t/s |
| 152 | 7,117 | 15.12 t/s | 16.06 t/s |
| 153 | 7,168 | 15.13 t/s | 16.39 t/s |
| 154 | 7,214 | 15.13 t/s | 15.09 t/s |
| 155 | 7,275 | 15.16 t/s | 19.72 t/s |
| 156 | 7,335 | 15.19 t/s | 19.56 t/s |
| 157 | 7,386 | 15.20 t/s | 16.36 t/s |
| 158 | 7,434 | 15.20 t/s | 15.37 t/s |
| 159 | 7,479 | 15.20 t/s | 14.71 t/s |
| 160 | 7,534 | 15.21 t/s | 17.61 t/s |
| 161 | 7,583 | 15.22 t/s | 15.98 t/s |
| 162 | 7,631 | 15.22 t/s | 15.31 t/s |
| 163 | 7,686 | 15.23 t/s | 17.75 t/s |
| 164 | 7,737 | 15.24 t/s | 16.59 t/s |
| 165 | 7,784 | 15.24 t/s | 15.19 t/s |
| 166 | 7,844 | 15.26 t/s | 19.15 t/s |
| 167 | 7,888 | 15.26 t/s | 14.36 t/s |
| 168 | 7,946 | 15.28 t/s | 18.69 t/s |
| 169 | 7,989 | 15.27 t/s | 13.99 t/s |
| 170 | 8,038 | 15.27 t/s | 15.57 t/s |
| 171 | 8,089 | 15.28 t/s | 16.97 t/s |
| 172 | 8,144 | 15.30 t/s | 17.71 t/s |
| 173 | 8,187 | 15.29 t/s | 13.73 t/s |
| 174 | 8,237 | 15.29 t/s | 16.08 t/s |
| 175 | 8,282 | 15.29 t/s | 14.33 t/s |
| 176 | 8,324 | 15.28 t/s | 13.42 t/s |
| 177 | 8,376 | 15.28 t/s | 16.82 t/s |
| 178 | 8,415 | 15.27 t/s | 12.49 t/s |
| 179 | 8,467 | 15.28 t/s | 16.60 t/s |
| 180 | 8,515 | 15.28 t/s | 15.53 t/s |
| 181 | 8,579 | 15.31 t/s | 20.45 t/s |
| 182 | 8,626 | 15.31 t/s | 15.15 t/s |
| 183 | 8,682 | 15.32 t/s | 17.86 t/s |
| 184 | 8,735 | 15.33 t/s | 17.13 t/s |
| 185 | 8,785 | 15.33 t/s | 16.13 t/s |
| 186 | 8,829 | 15.33 t/s | 14.10 t/s |
| 187 | 8,877 | 15.33 t/s | 15.41 t/s |
| 188 | 8,935 | 15.35 t/s | 19.28 t/s |

---

## Task #2137 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 22:55:54.644` (Queue Delay: `7.08s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 19.25 t/s | 19.45 t/s |
| 2 | 147 | 17.72 t/s | 15.17 t/s |
| 3 | 194 | 17.14 t/s | 15.58 t/s |
| 4 | 241 | 16.71 t/s | 15.14 t/s |
| 5 | 284 | 16.28 t/s | 14.24 t/s |
| 6 | 316 | 15.45 t/s | 10.65 t/s |
| 7 | 363 | 15.41 t/s | 15.16 t/s |
| 8 | 404 | 15.19 t/s | 13.46 t/s |
| 9 | 443 | 14.91 t/s | 12.50 t/s |
| 10 | 481 | 14.68 t/s | 12.47 t/s |
| 11 | 521 | 14.56 t/s | 13.25 t/s |
| 12 | 561 | 14.42 t/s | 12.81 t/s |
| 13 | 598 | 14.26 t/s | 12.21 t/s |
| 14 | 638 | 14.16 t/s | 12.86 t/s |
| 15 | 675 | 14.04 t/s | 12.17 t/s |
| 16 | 708 | 13.85 t/s | 10.98 t/s |
| 17 | 746 | 13.76 t/s | 12.14 t/s |
| 18 | 784 | 13.70 t/s | 12.64 t/s |
| 19 | 826 | 13.68 t/s | 13.40 t/s |
| 20 | 873 | 13.77 t/s | 15.44 t/s |
| 21 | 908 | 13.64 t/s | 11.14 t/s |
| 22 | 948 | 13.62 t/s | 13.22 t/s |
| 23 | 982 | 13.52 t/s | 11.12 t/s |
| 24 | 1,021 | 13.50 t/s | 12.98 t/s |
| 25 | 1,063 | 13.51 t/s | 13.77 t/s |
| 26 | 1,099 | 13.45 t/s | 11.85 t/s |
| 27 | 1,146 | 13.50 t/s | 14.99 t/s |
| 28 | 1,184 | 13.47 t/s | 12.42 t/s |
| 29 | 1,221 | 13.43 t/s | 12.30 t/s |
| 30 | 1,266 | 13.47 t/s | 14.67 t/s |
| 31 | 1,326 | 13.66 t/s | 19.58 t/s |
| 32 | 1,376 | 13.75 t/s | 16.56 t/s |
| 33 | 1,423 | 13.79 t/s | 15.28 t/s |
| 34 | 1,476 | 13.90 t/s | 17.54 t/s |
| 35 | 1,525 | 13.96 t/s | 15.87 t/s |
| 36 | 1,574 | 14.01 t/s | 15.83 t/s |
| 37 | 1,610 | 13.95 t/s | 11.93 t/s |
| 38 | 1,663 | 14.04 t/s | 17.48 t/s |
| 39 | 1,698 | 13.98 t/s | 11.59 t/s |
| 40 | 1,734 | 13.93 t/s | 11.85 t/s |
| 41 | 1,782 | 13.97 t/s | 15.60 t/s |
| 42 | 1,829 | 14.00 t/s | 15.45 t/s |
| 43 | 1,865 | 13.95 t/s | 11.77 t/s |
| 44 | 1,903 | 13.92 t/s | 12.36 t/s |
| 45 | 1,960 | 14.02 t/s | 18.67 t/s |
| 46 | 2,000 | 14.00 t/s | 12.89 t/s |
| 47 | 2,039 | 13.97 t/s | 12.83 t/s |
| 48 | 2,088 | 14.01 t/s | 15.88 t/s |
| 49 | 2,134 | 14.03 t/s | 14.92 t/s |
| 50 | 2,179 | 14.05 t/s | 14.91 t/s |
| 51 | 2,222 | 14.04 t/s | 13.83 t/s |
| 52 | 2,259 | 14.01 t/s | 12.18 t/s |
| 53 | 2,298 | 13.98 t/s | 12.56 t/s |
| 54 | 2,336 | 13.95 t/s | 12.26 t/s |
| 55 | 2,378 | 13.95 t/s | 13.92 t/s |
| 56 | 2,408 | 13.87 t/s | 9.77 t/s |
| 57 | 2,446 | 13.85 t/s | 12.36 t/s |
| 58 | 2,484 | 13.82 t/s | 12.29 t/s |
| 59 | 2,526 | 13.82 t/s | 13.79 t/s |
| 60 | 2,573 | 13.85 t/s | 15.37 t/s |
| 61 | 2,621 | 13.88 t/s | 15.62 t/s |
| 62 | 2,677 | 13.95 t/s | 18.40 t/s |
| 63 | 2,728 | 13.99 t/s | 16.40 t/s |
| 64 | 2,783 | 14.05 t/s | 17.92 t/s |
| 65 | 2,821 | 14.02 t/s | 12.50 t/s |
| 66 | 2,852 | 13.96 t/s | 9.98 t/s |
| 67 | 2,883 | 13.91 t/s | 10.20 t/s |
| 68 | 2,913 | 13.85 t/s | 9.69 t/s |
| 69 | 2,947 | 13.80 t/s | 10.99 t/s |
| 70 | 2,979 | 13.76 t/s | 10.42 t/s |
| 71 | 3,017 | 13.73 t/s | 12.15 t/s |
| 72 | 3,065 | 13.76 t/s | 15.30 t/s |
| 73 | 3,111 | 13.77 t/s | 14.92 t/s |
| 74 | 3,154 | 13.77 t/s | 13.83 t/s |
| 75 | 3,194 | 13.76 t/s | 13.06 t/s |
| 76 | 3,242 | 13.78 t/s | 15.30 t/s |
| 77 | 3,290 | 13.80 t/s | 15.36 t/s |
| 78 | 3,348 | 13.87 t/s | 18.87 t/s |
| 79 | 3,395 | 13.88 t/s | 14.99 t/s |
| 80 | 3,434 | 13.87 t/s | 12.71 t/s |
| 81 | 3,483 | 13.89 t/s | 15.82 t/s |
| 82 | 3,527 | 13.89 t/s | 14.10 t/s |
| 83 | 3,573 | 13.91 t/s | 14.89 t/s |
| 84 | 3,617 | 13.91 t/s | 14.01 t/s |
| 85 | 3,658 | 13.90 t/s | 13.40 t/s |
| 86 | 3,705 | 13.92 t/s | 15.25 t/s |
| 87 | 3,745 | 13.91 t/s | 13.32 t/s |
| 88 | 3,777 | 13.87 t/s | 10.44 t/s |
| 89 | 3,817 | 13.86 t/s | 12.72 t/s |
| 90 | 3,858 | 13.86 t/s | 13.60 t/s |
| 91 | 3,903 | 13.87 t/s | 15.00 t/s |
| 92 | 3,955 | 13.90 t/s | 16.73 t/s |
| 93 | 3,996 | 13.89 t/s | 13.11 t/s |

---

## Task #4094 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 23:00:53.515` (Queue Delay: `5.50s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 17.68 t/s | 17.86 t/s |
| 2 | 142 | 16.18 t/s | 13.47 t/s |
| 3 | 182 | 15.44 t/s | 13.30 t/s |
| 4 | 219 | 14.71 t/s | 11.95 t/s |
| 5 | 255 | 14.24 t/s | 11.95 t/s |
| 6 | 305 | 14.57 t/s | 16.52 t/s |
| 7 | 340 | 14.15 t/s | 11.29 t/s |
| 8 | 389 | 14.33 t/s | 15.72 t/s |
| 9 | 427 | 14.09 t/s | 12.02 t/s |
| 10 | 466 | 13.98 t/s | 12.93 t/s |
| 11 | 507 | 13.95 t/s | 13.59 t/s |
| 12 | 552 | 13.99 t/s | 14.41 t/s |
| 13 | 594 | 13.95 t/s | 13.42 t/s |
| 14 | 636 | 13.94 t/s | 13.88 t/s |
| 15 | 679 | 13.93 t/s | 13.71 t/s |
| 16 | 722 | 13.94 t/s | 14.21 t/s |
| 17 | 766 | 13.98 t/s | 14.63 t/s |
| 18 | 820 | 14.18 t/s | 17.68 t/s |
| 19 | 863 | 14.18 t/s | 14.20 t/s |
| 20 | 920 | 14.40 t/s | 18.98 t/s |
| 21 | 969 | 14.48 t/s | 15.98 t/s |
| 22 | 1,010 | 14.44 t/s | 13.60 t/s |
| 23 | 1,058 | 14.49 t/s | 15.69 t/s |
| 24 | 1,099 | 14.44 t/s | 13.31 t/s |
| 25 | 1,149 | 14.50 t/s | 15.92 t/s |
| 26 | 1,189 | 14.45 t/s | 13.10 t/s |
| 27 | 1,232 | 14.44 t/s | 14.31 t/s |
| 28 | 1,280 | 14.49 t/s | 15.70 t/s |
| 29 | 1,316 | 14.40 t/s | 11.96 t/s |
| 30 | 1,351 | 14.32 t/s | 11.66 t/s |
| 31 | 1,391 | 14.28 t/s | 13.22 t/s |
| 32 | 1,435 | 14.29 t/s | 14.58 t/s |
| 33 | 1,472 | 14.23 t/s | 12.04 t/s |
| 34 | 1,507 | 14.15 t/s | 11.62 t/s |
| 35 | 1,549 | 14.14 t/s | 13.88 t/s |
| 36 | 1,591 | 14.13 t/s | 13.65 t/s |
| 37 | 1,625 | 14.06 t/s | 11.31 t/s |
| 38 | 1,665 | 14.03 t/s | 13.06 t/s |
| 39 | 1,710 | 14.05 t/s | 14.70 t/s |
| 40 | 1,752 | 14.04 t/s | 13.59 t/s |
| 41 | 1,797 | 14.05 t/s | 14.47 t/s |
| 42 | 1,840 | 14.05 t/s | 14.13 t/s |
| 43 | 1,902 | 14.19 t/s | 20.09 t/s |
| 44 | 1,945 | 14.18 t/s | 13.83 t/s |
| 45 | 1,985 | 14.16 t/s | 13.15 t/s |
| 46 | 2,029 | 14.16 t/s | 14.27 t/s |
| 47 | 2,074 | 14.18 t/s | 14.87 t/s |
| 48 | 2,119 | 14.18 t/s | 14.48 t/s |
| 49 | 2,160 | 14.16 t/s | 13.26 t/s |
| 50 | 2,208 | 14.20 t/s | 15.84 t/s |
| 51 | 2,250 | 14.19 t/s | 13.83 t/s |
| 52 | 2,292 | 14.18 t/s | 13.70 t/s |
| 53 | 2,337 | 14.19 t/s | 14.86 t/s |
| 54 | 2,387 | 14.23 t/s | 16.23 t/s |
| 55 | 2,432 | 14.24 t/s | 14.89 t/s |
| 56 | 2,506 | 14.41 t/s | 23.80 t/s |
| 57 | 2,555 | 14.44 t/s | 15.80 t/s |
| 58 | 2,602 | 14.45 t/s | 15.42 t/s |
| 59 | 2,646 | 14.45 t/s | 14.19 t/s |
| 60 | 2,684 | 14.42 t/s | 12.48 t/s |
| 61 | 2,730 | 14.42 t/s | 14.63 t/s |
| 62 | 2,780 | 14.45 t/s | 16.00 t/s |
| 63 | 2,848 | 14.57 t/s | 22.08 t/s |
| 64 | 2,904 | 14.62 t/s | 17.91 t/s |
| 65 | 2,949 | 14.62 t/s | 14.68 t/s |
| 66 | 3,006 | 14.68 t/s | 18.99 t/s |
| 67 | 3,049 | 14.68 t/s | 14.33 t/s |
| 68 | 3,103 | 14.72 t/s | 17.49 t/s |
| 69 | 3,182 | 14.87 t/s | 25.10 t/s |
| 70 | 3,246 | 14.95 t/s | 20.48 t/s |
| 71 | 3,297 | 14.97 t/s | 16.28 t/s |
| 72 | 3,347 | 14.99 t/s | 16.07 t/s |
| 73 | 3,408 | 15.05 t/s | 19.79 t/s |
| 74 | 3,462 | 15.08 t/s | 17.39 t/s |
| 75 | 3,515 | 15.11 t/s | 16.94 t/s |
| 76 | 3,557 | 15.09 t/s | 13.70 t/s |
| 77 | 3,595 | 15.05 t/s | 12.29 t/s |
| 78 | 3,654 | 15.11 t/s | 19.10 t/s |
| 79 | 3,717 | 15.18 t/s | 20.71 t/s |
| 80 | 3,773 | 15.22 t/s | 18.51 t/s |
| 81 | 3,820 | 15.22 t/s | 15.25 t/s |
| 82 | 3,857 | 15.17 t/s | 11.80 t/s |
| 83 | 3,913 | 15.21 t/s | 18.09 t/s |
| 84 | 3,967 | 15.23 t/s | 17.17 t/s |
| 85 | 4,021 | 15.26 t/s | 17.91 t/s |
| 86 | 4,070 | 15.27 t/s | 15.84 t/s |
| 87 | 4,125 | 15.30 t/s | 18.22 t/s |
| 88 | 4,181 | 15.33 t/s | 17.98 t/s |
| 89 | 4,224 | 15.32 t/s | 14.32 t/s |
| 90 | 4,273 | 15.33 t/s | 16.11 t/s |
| 91 | 4,326 | 15.35 t/s | 16.93 t/s |
| 92 | 4,377 | 15.36 t/s | 16.56 t/s |
| 93 | 4,437 | 15.40 t/s | 19.13 t/s |
| 94 | 4,493 | 15.43 t/s | 17.86 t/s |

---

## Task #6084 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 23:05:54.663` (Queue Delay: `N/A`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 103 | 19.42 t/s | 19.61 t/s |
| 2 | 150 | 17.88 t/s | 15.27 t/s |
| 3 | 205 | 18.00 t/s | 18.33 t/s |
| 4 | 263 | 18.08 t/s | 18.35 t/s |
| 5 | 310 | 17.55 t/s | 15.09 t/s |
| 6 | 345 | 16.69 t/s | 11.66 t/s |
| 7 | 388 | 16.33 t/s | 13.90 t/s |
| 8 | 421 | 15.72 t/s | 10.93 t/s |
| 9 | 463 | 15.54 t/s | 13.93 t/s |
| 10 | 500 | 15.19 t/s | 11.87 t/s |
| 11 | 559 | 15.56 t/s | 19.58 t/s |
| 12 | 601 | 15.39 t/s | 13.50 t/s |
| 13 | 635 | 15.10 t/s | 11.30 t/s |
| 14 | 682 | 15.13 t/s | 15.48 t/s |
| 15 | 731 | 15.17 t/s | 15.76 t/s |
| 16 | 770 | 15.04 t/s | 12.96 t/s |
| 17 | 809 | 14.90 t/s | 12.60 t/s |
| 18 | 846 | 14.76 t/s | 12.32 t/s |
| 19 | 893 | 14.77 t/s | 14.98 t/s |
| 20 | 949 | 14.95 t/s | 18.44 t/s |
| 21 | 992 | 14.90 t/s | 13.94 t/s |
| 22 | 1,042 | 14.97 t/s | 16.39 t/s |
| 23 | 1,083 | 14.91 t/s | 13.57 t/s |
| 24 | 1,131 | 14.94 t/s | 15.77 t/s |
| 25 | 1,181 | 14.99 t/s | 16.19 t/s |
| 26 | 1,227 | 14.97 t/s | 14.47 t/s |
| 27 | 1,278 | 15.04 t/s | 16.99 t/s |
| 28 | 1,323 | 15.02 t/s | 14.48 t/s |
| 29 | 1,371 | 15.05 t/s | 15.87 t/s |
| 30 | 1,405 | 14.93 t/s | 11.23 t/s |
| 31 | 1,453 | 14.95 t/s | 15.70 t/s |
| 32 | 1,489 | 14.85 t/s | 11.65 t/s |
| 33 | 1,528 | 14.80 t/s | 13.00 t/s |
| 34 | 1,572 | 14.78 t/s | 14.12 t/s |
| 35 | 1,621 | 14.81 t/s | 15.73 t/s |
| 36 | 1,658 | 14.72 t/s | 11.83 t/s |
| 37 | 1,702 | 14.71 t/s | 14.10 t/s |
| 38 | 1,751 | 14.74 t/s | 15.87 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3.8-27B-GGUF`
* **Dispatch Time:** `2026-09-08 23:09:49.725` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `2602` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `55.26 t/s` (`18.10 ms/tok`) | Time To First Token (TTFT) = `25.37s` |
| **Decode Speed (Generation)** | `16.37 t/s` (`61.08 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1402` (53.9%) / Out: `1200` (46.1%) | Total context footprint: `2602` tokens |
| **Speculative MTP Acceptance** | `45.68%` (`693/1517`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.37` tokens/step | Effective speedup: ~`2.37x` vs single-token decode |
| **Graphs Reused** | `500` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 567 | 40.0% | 6.32 | 89.67 |
| 2 | 725 | 52.0% | 7.50 | 96.72 |
| 3 | 886 | 63.0% | 12.76 | 69.42 |
| 4 | 1,398 | 100.0% | 18.13 | 77.11 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 103 | 18.05 t/s | 18.22 t/s |
| 2 | 178 | 20.27 t/s | 24.36 t/s |
| 3 | 242 | 20.47 t/s | 21.05 t/s |
| 4 | 292 | 19.57 t/s | 16.13 t/s |
| 5 | 344 | 19.14 t/s | 17.07 t/s |
| 6 | 394 | 18.66 t/s | 15.93 t/s |
| 7 | 436 | 18.04 t/s | 13.76 t/s |
| 8 | 485 | 17.80 t/s | 15.91 t/s |
| 9 | 534 | 17.62 t/s | 16.02 t/s |
| 10 | 577 | 17.30 t/s | 14.09 t/s |
| 11 | 623 | 17.12 t/s | 15.16 t/s |
| 12 | 670 | 16.98 t/s | 15.35 t/s |
| 13 | 715 | 16.81 t/s | 14.68 t/s |
| 14 | 760 | 16.65 t/s | 14.41 t/s |
| 15 | 812 | 16.69 t/s | 17.33 t/s |
| 16 | 857 | 16.59 t/s | 14.89 t/s |
| 17 | 909 | 16.60 t/s | 16.81 t/s |
| 18 | 960 | 16.58 t/s | 16.31 t/s |
| 19 | 1,000 | 16.42 t/s | 13.29 t/s |
| 20 | 1,060 | 16.57 t/s | 19.63 t/s |
| 21 | 1,123 | 16.75 t/s | 20.32 t/s |
| 22 | 1,175 | 16.75 t/s | 16.85 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3-Coder-30B-A3B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-08 23:16:36.192` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `4878` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `481.29 t/s` (`2.08 ms/tok`) | Time To First Token (TTFT) = `2.67s` |
| **Decode Speed (Generation)** | `54.36 t/s` (`18.40 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1284` (26.3%) / Out: `3594` (73.7%) | Total context footprint: `4878` tokens |
| **Graphs Reused** | `3,579` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 171 | 56.52 t/s | 56.85 t/s |
| 2 | 345 | 57.11 t/s | 57.71 t/s |
| 3 | 512 | 56.63 t/s | 55.65 t/s |
| 4 | 680 | 56.43 t/s | 55.85 t/s |
| 5 | 848 | 56.31 t/s | 55.81 t/s |
| 6 | 1,021 | 56.49 t/s | 57.43 t/s |
| 7 | 1,197 | 56.79 t/s | 58.58 t/s |
| 8 | 1,362 | 56.55 t/s | 54.83 t/s |
| 9 | 1,520 | 56.10 t/s | 52.49 t/s |
| 10 | 1,680 | 55.80 t/s | 53.14 t/s |
| 11 | 1,837 | 55.46 t/s | 52.02 t/s |
| 12 | 1,999 | 55.32 t/s | 53.85 t/s |
| 13 | 2,164 | 55.29 t/s | 54.95 t/s |
| 14 | 2,329 | 55.26 t/s | 54.84 t/s |
| 15 | 2,494 | 55.23 t/s | 54.83 t/s |
| 16 | 2,655 | 55.12 t/s | 53.43 t/s |
| 17 | 2,814 | 54.98 t/s | 52.72 t/s |
| 18 | 2,967 | 54.75 t/s | 50.92 t/s |
| 19 | 3,125 | 54.63 t/s | 52.42 t/s |
| 20 | 3,284 | 54.55 t/s | 52.99 t/s |
| 21 | 3,441 | 54.43 t/s | 52.14 t/s |

---

## Task #3595 (Slot 0)

* **Model:** `Qwen3-Coder-30B-A3B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-08 23:21:51.274` (Queue Delay: `3.72s`)
* **Total Context Footprint:** `2190` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `34.70 t/s` (`28.82 ms/tok`) | Time To First Token (TTFT) = `0.03s` |
| **Decode Speed (Generation)** | `55.57 t/s` (`18.00 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1` (0.0%) / Out: `2189` (100.0%) | Total context footprint: `2190` tokens |
| **Graphs Reused** | `5,759` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 113 | 35.62 t/s | 35.94 t/s |
| 2 | 160 | 25.87 t/s | 15.65 t/s |
| 3 | 346 | 37.67 t/s | 61.78 t/s |
| 4 | 542 | 44.45 t/s | 65.06 t/s |
| 5 | 732 | 48.17 t/s | 63.20 t/s |
| 6 | 915 | 50.25 t/s | 60.75 t/s |
| 7 | 1,100 | 51.86 t/s | 61.59 t/s |
| 8 | 1,280 | 52.86 t/s | 59.94 t/s |
| 9 | 1,461 | 53.66 t/s | 60.05 t/s |
| 10 | 1,640 | 54.23 t/s | 59.42 t/s |
| 11 | 1,822 | 54.80 t/s | 60.49 t/s |
| 12 | 2,006 | 55.33 t/s | 61.14 t/s |
| 13 | 2,182 | 55.56 t/s | 58.36 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-10 22:22:17.144` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `704` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `182.94 t/s` (`5.47 ms/tok`) | Time To First Token (TTFT) = `2.36s` |
| **Decode Speed (Generation)** | `49.87 t/s` (`20.05 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `431` (61.2%) / Out: `273` (38.8%) | Total context footprint: `704` tokens |
| **Graphs Reused** | `271` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 147 | 48.57 t/s | 48.90 t/s |

---

## Task #276 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-10 22:24:48.651` (Queue Delay: `0.02s`)
* **Total Context Footprint:** `184` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `6.89 t/s` (`145.23 ms/tok`) | Time To First Token (TTFT) = `0.73s` |
| **Decode Speed (Generation)** | `51.32 t/s` (`19.49 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `5` (2.7%) / Out: `179` (97.3%) | Total context footprint: `184` tokens |
| **Graphs Reused** | `447` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 155 | 51.24 t/s | 51.57 t/s |

---

## Task #457 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-10 22:25:02.566` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `780` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `255.52 t/s` (`3.91 ms/tok`) | Time To First Token (TTFT) = `2.49s` |
| **Decode Speed (Generation)** | `51.73 t/s` (`19.33 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `636` (81.5%) / Out: `144` (18.5%) | Total context footprint: `780` tokens |
| **Graphs Reused** | `589` | CUDA/execution graph cache hits |

---

## Task #605 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-10 22:25:16.450` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `979` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `108.43 t/s` (`9.22 ms/tok`) | Time To First Token (TTFT) = `1.41s` |
| **Decode Speed (Generation)** | `51.54 t/s` (`19.40 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `153` (15.6%) / Out: `826` (84.4%) | Total context footprint: `979` tokens |
| **Graphs Reused** | `1,410` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 155 | 51.22 t/s | 51.55 t/s |
| 2 | 309 | 51.20 t/s | 51.17 t/s |
| 3 | 464 | 51.35 t/s | 51.65 t/s |
| 4 | 621 | 51.53 t/s | 52.08 t/s |
| 5 | 776 | 51.56 t/s | 51.66 t/s |

---

## Task #1434 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-10 22:25:52.862` (Queue Delay: `1.39s`)
* **Total Context Footprint:** `203` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `23.49 t/s` (`42.56 ms/tok`) | Time To First Token (TTFT) = `1.02s` |
| **Decode Speed (Generation)** | `50.96 t/s` (`19.62 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `24` (11.8%) / Out: `179` (88.2%) | Total context footprint: `203` tokens |
| **Graphs Reused** | `1,586` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 154 | 50.84 t/s | 51.17 t/s |

---

## Task #1616 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-10 22:26:05.322` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `763` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `342.33 t/s` (`2.92 ms/tok`) | Time To First Token (TTFT) = `1.86s` |
| **Decode Speed (Generation)** | `52.29 t/s` (`19.12 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `636` (83.4%) / Out: `127` (16.6%) | Total context footprint: `763` tokens |
| **Graphs Reused** | `1,711` | CUDA/execution graph cache hits |

---

## Task #1747 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-10 22:26:19.147` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `557` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `112.65 t/s` (`8.88 ms/tok`) | Time To First Token (TTFT) = `1.40s` |
| **Decode Speed (Generation)** | `51.08 t/s` (`19.58 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `158` (28.4%) / Out: `399` (71.6%) | Total context footprint: `557` tokens |
| **Graphs Reused** | `2,106` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 157 | 51.68 t/s | 52.01 t/s |
| 2 | 311 | 51.43 t/s | 51.18 t/s |

---

## Task #0 (Slot 0)

* **Model:** `2da8c0432f0a42c25c14cbc99f90028a90d3dcd3`
* **Dispatch Time:** `2026-09-10 22:33:51.843` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `624` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `10.36 t/s` (`96.53 ms/tok`) | Time To First Token (TTFT) = `1.45s` |
| **Decode Speed (Generation)** | `23.01 t/s` (`43.46 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `15` (2.4%) / Out: `609` (97.6%) | Total context footprint: `624` tokens |
| **Speculative MTP Acceptance** | `63.49%` (`400/630`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.90` tokens/step | Effective speedup: ~`2.90x` vs single-token decode |
| **Graphs Reused** | `208` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 101 | 25.66 t/s | 25.92 t/s |
| 2 | 179 | 25.42 t/s | 25.13 t/s |
| 3 | 239 | 23.76 t/s | 19.89 t/s |
| 4 | 307 | 23.50 t/s | 22.62 t/s |
| 5 | 364 | 22.60 t/s | 18.78 t/s |
| 6 | 432 | 22.59 t/s | 22.50 t/s |
| 7 | 498 | 22.51 t/s | 22.00 t/s |
| 8 | 571 | 22.65 t/s | 23.69 t/s |

---

## Task #0 (Slot 0)

* **Model:** `user.Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:05:06.490` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `39` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `26.40 t/s` (`37.88 ms/tok`) | Time To First Token (TTFT) = `0.72s` |
| **Decode Speed (Generation)** | `17.17 t/s` (`58.23 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `19` (48.7%) / Out: `20` (51.3%) | Total context footprint: `39` tokens |
| **Speculative MTP Acceptance** | `100.00%` (`14/14`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.80` tokens/step | Effective speedup: ~`3.80x` vs single-token decode |
| **Graphs Reused** | `4` | CUDA/execution graph cache hits |

---

## Task #8 (Slot 0)

* **Model:** `user.Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:05:17.506` (Queue Delay: `1.76s`)
* **Total Context Footprint:** `43` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `28.47 t/s` (`35.13 ms/tok`) | Time To First Token (TTFT) = `0.46s` |
| **Decode Speed (Generation)** | `16.30 t/s` (`61.36 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `13` (30.2%) / Out: `30` (69.8%) | Total context footprint: `43` tokens |
| **Speculative MTP Acceptance** | `100.00%` (`21/21`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `4.00` tokens/step | Effective speedup: ~`4.00x` vs single-token decode |
| **Graphs Reused** | `10` | CUDA/execution graph cache hits |

---

## Task #19 (Slot 0)

* **Model:** `user.Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:05:23.394` (Queue Delay: `0.02s`)
* **Total Context Footprint:** `34` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `16.83 t/s` (`59.43 ms/tok`) | Time To First Token (TTFT) = `0.24s` |
| **Decode Speed (Generation)** | `14.01 t/s` (`71.36 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `4` (11.8%) / Out: `30` (88.2%) | Total context footprint: `34` tokens |
| **Speculative MTP Acceptance** | `90.91%` (`20/22`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.50` tokens/step | Effective speedup: ~`3.50x` vs single-token decode |
| **Graphs Reused** | `16` | CUDA/execution graph cache hits |

---

## Task #30 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:07:03.133` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `1125` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `59.19 t/s` (`16.89 ms/tok`) | Time To First Token (TTFT) = `1.03s` |
| **Decode Speed (Generation)** | `11.44 t/s` (`87.38 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `61` (5.4%) / Out: `1064` (94.6%) | Total context footprint: `1125` tokens |
| **Speculative MTP Acceptance** | `51.84%` (`647/1248`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.56` tokens/step | Effective speedup: ~`2.56x` vs single-token decode |
| **Graphs Reused** | `427` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 13.21 t/s | 13.34 t/s |
| 2 | 135 | 12.64 t/s | 11.28 t/s |
| 3 | 165 | 11.98 t/s | 9.69 t/s |
| 4 | 196 | 11.68 t/s | 10.33 t/s |
| 5 | 238 | 11.95 t/s | 13.37 t/s |
| 6 | 273 | 11.84 t/s | 11.18 t/s |
| 7 | 306 | 11.73 t/s | 10.87 t/s |
| 8 | 350 | 12.01 t/s | 14.35 t/s |
| 9 | 382 | 11.79 t/s | 9.89 t/s |
| 10 | 420 | 11.80 t/s | 11.85 t/s |
| 11 | 455 | 11.77 t/s | 11.42 t/s |
| 12 | 494 | 11.83 t/s | 12.66 t/s |
| 13 | 524 | 11.67 t/s | 9.53 t/s |
| 14 | 559 | 11.65 t/s | 11.25 t/s |
| 15 | 595 | 11.66 t/s | 11.88 t/s |
| 16 | 631 | 11.64 t/s | 11.31 t/s |
| 17 | 671 | 11.71 t/s | 13.03 t/s |
| 18 | 693 | 11.49 t/s | 7.27 t/s |
| 19 | 718 | 11.34 t/s | 8.29 t/s |
| 20 | 760 | 11.45 t/s | 13.76 t/s |
| 21 | 806 | 11.59 t/s | 14.54 t/s |
| 22 | 852 | 11.67 t/s | 13.36 t/s |
| 23 | 883 | 11.61 t/s | 10.00 t/s |
| 24 | 912 | 11.51 t/s | 9.21 t/s |
| 25 | 941 | 11.43 t/s | 9.33 t/s |
| 26 | 975 | 11.40 t/s | 10.74 t/s |
| 27 | 1,021 | 11.52 t/s | 14.81 t/s |
| 28 | 1,051 | 11.45 t/s | 9.53 t/s |

---

## Task #450 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:09:00.040` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `1819` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `130.08 t/s` (`7.69 ms/tok`) | Time To First Token (TTFT) = `2.39s` |
| **Decode Speed (Generation)** | `11.12 t/s` (`89.95 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `311` (17.1%) / Out: `1508` (82.9%) | Total context footprint: `1819` tokens |
| **Speculative MTP Acceptance** | `49.89%` (`904/1812`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.50` tokens/step | Effective speedup: ~`2.50x` vs single-token decode |
| **Graphs Reused** | `1,024` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 101 | 14.86 t/s | 15.01 t/s |
| 2 | 136 | 13.64 t/s | 11.06 t/s |
| 3 | 169 | 12.88 t/s | 10.50 t/s |
| 4 | 202 | 12.47 t/s | 10.70 t/s |
| 5 | 239 | 12.35 t/s | 11.73 t/s |
| 6 | 284 | 12.57 t/s | 13.88 t/s |
| 7 | 324 | 12.58 t/s | 12.67 t/s |
| 8 | 356 | 12.32 t/s | 10.21 t/s |
| 9 | 394 | 12.32 t/s | 12.30 t/s |
| 10 | 431 | 12.30 t/s | 12.07 t/s |
| 11 | 465 | 12.17 t/s | 10.77 t/s |
| 12 | 506 | 12.22 t/s | 12.81 t/s |
| 13 | 534 | 12.02 t/s | 9.23 t/s |
| 14 | 562 | 11.80 t/s | 8.82 t/s |
| 15 | 589 | 11.60 t/s | 8.58 t/s |
| 16 | 613 | 11.39 t/s | 7.88 t/s |
| 17 | 639 | 11.24 t/s | 8.57 t/s |
| 18 | 664 | 11.07 t/s | 8.00 t/s |
| 19 | 698 | 11.06 t/s | 10.81 t/s |
| 20 | 736 | 11.11 t/s | 12.17 t/s |
| 21 | 774 | 11.17 t/s | 12.40 t/s |
| 22 | 806 | 11.14 t/s | 10.42 t/s |
| 23 | 841 | 11.14 t/s | 11.32 t/s |
| 24 | 873 | 11.12 t/s | 10.49 t/s |
| 25 | 908 | 11.12 t/s | 11.08 t/s |
| 26 | 956 | 11.26 t/s | 14.76 t/s |
| 27 | 994 | 11.30 t/s | 12.49 t/s |
| 28 | 1,036 | 11.38 t/s | 13.80 t/s |
| 29 | 1,066 | 11.33 t/s | 9.82 t/s |
| 30 | 1,103 | 11.35 t/s | 11.78 t/s |
| 31 | 1,142 | 11.37 t/s | 11.93 t/s |
| 32 | 1,177 | 11.35 t/s | 10.99 t/s |
| 33 | 1,210 | 11.33 t/s | 10.62 t/s |
| 34 | 1,240 | 11.28 t/s | 9.55 t/s |
| 35 | 1,269 | 11.22 t/s | 9.18 t/s |
| 36 | 1,302 | 11.20 t/s | 10.42 t/s |
| 37 | 1,335 | 11.19 t/s | 10.82 t/s |
| 38 | 1,365 | 11.14 t/s | 9.36 t/s |
| 39 | 1,393 | 11.10 t/s | 9.29 t/s |
| 40 | 1,422 | 11.05 t/s | 9.04 t/s |
| 41 | 1,465 | 11.10 t/s | 13.35 t/s |
| 42 | 1,504 | 11.13 t/s | 12.01 t/s |

---

## Task #1058 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:11:58.105` (Queue Delay: `0.07s`)
* **Total Context Footprint:** `2238` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `138.46 t/s` (`7.22 ms/tok`) | Time To First Token (TTFT) = `3.66s` |
| **Decode Speed (Generation)** | `10.36 t/s` (`96.57 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `507` (22.7%) / Out: `1731` (77.3%) | Total context footprint: `2238` tokens |
| **Speculative MTP Acceptance** | `45.86%` (`1003/2187`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.38` tokens/step | Effective speedup: ~`2.38x` vs single-token decode |
| **Graphs Reused** | `1,745` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 503 | 100.0% | 3.35 | 150.18 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 12.79 t/s | 12.92 t/s |
| 2 | 131 | 12.03 t/s | 10.09 t/s |
| 3 | 157 | 11.25 t/s | 8.51 t/s |
| 4 | 193 | 11.27 t/s | 11.35 t/s |
| 5 | 234 | 11.51 t/s | 12.82 t/s |
| 6 | 266 | 11.34 t/s | 10.22 t/s |
| 7 | 294 | 11.05 t/s | 8.92 t/s |
| 8 | 325 | 10.95 t/s | 10.03 t/s |
| 9 | 354 | 10.78 t/s | 9.19 t/s |
| 10 | 387 | 10.73 t/s | 10.22 t/s |
| 11 | 423 | 10.79 t/s | 11.54 t/s |
| 12 | 448 | 10.56 t/s | 7.79 t/s |
| 13 | 473 | 10.39 t/s | 8.03 t/s |
| 14 | 494 | 10.14 t/s | 6.61 t/s |
| 15 | 524 | 10.12 t/s | 9.82 t/s |
| 16 | 557 | 10.14 t/s | 10.33 t/s |
| 17 | 582 | 10.03 t/s | 8.13 t/s |
| 18 | 608 | 9.93 t/s | 8.14 t/s |
| 19 | 631 | 9.81 t/s | 7.49 t/s |
| 20 | 660 | 9.79 t/s | 9.30 t/s |
| 21 | 695 | 9.85 t/s | 11.20 t/s |
| 22 | 725 | 9.85 t/s | 9.69 t/s |
| 23 | 765 | 9.98 t/s | 13.27 t/s |
| 24 | 800 | 10.04 t/s | 11.39 t/s |
| 25 | 840 | 10.13 t/s | 12.44 t/s |
| 26 | 875 | 10.17 t/s | 11.22 t/s |
| 27 | 903 | 10.12 t/s | 8.82 t/s |
| 28 | 934 | 10.11 t/s | 9.72 t/s |
| 29 | 969 | 10.14 t/s | 11.29 t/s |
| 30 | 995 | 10.09 t/s | 8.40 t/s |
| 31 | 1,040 | 10.22 t/s | 14.36 t/s |
| 32 | 1,079 | 10.28 t/s | 12.20 t/s |
| 33 | 1,112 | 10.29 t/s | 10.41 t/s |
| 34 | 1,139 | 10.25 t/s | 8.97 t/s |
| 35 | 1,172 | 10.25 t/s | 10.24 t/s |
| 36 | 1,209 | 10.30 t/s | 12.06 t/s |
| 37 | 1,244 | 10.33 t/s | 11.60 t/s |
| 38 | 1,278 | 10.35 t/s | 11.07 t/s |
| 39 | 1,314 | 10.38 t/s | 11.67 t/s |
| 40 | 1,351 | 10.42 t/s | 11.80 t/s |
| 41 | 1,383 | 10.41 t/s | 10.06 t/s |
| 42 | 1,416 | 10.41 t/s | 10.41 t/s |
| 43 | 1,446 | 10.40 t/s | 9.93 t/s |
| 44 | 1,483 | 10.43 t/s | 11.78 t/s |
| 45 | 1,526 | 10.50 t/s | 13.63 t/s |
| 46 | 1,557 | 10.48 t/s | 9.80 t/s |
| 47 | 1,585 | 10.46 t/s | 9.30 t/s |
| 48 | 1,610 | 10.41 t/s | 7.95 t/s |
| 49 | 1,642 | 10.41 t/s | 10.61 t/s |
| 50 | 1,670 | 10.38 t/s | 8.90 t/s |
| 51 | 1,702 | 10.38 t/s | 10.22 t/s |

---

## Task #1791 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:17:14.870` (Queue Delay: `0.07s`)
* **Total Context Footprint:** `3486` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `136.03 t/s` (`7.35 ms/tok`) | Time To First Token (TTFT) = `4.91s` |
| **Decode Speed (Generation)** | `10.85 t/s` (`92.19 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `668` (19.2%) / Out: `2818` (80.8%) | Total context footprint: `3486` tokens |
| **Speculative MTP Acceptance** | `50.00%` (`1692/3384`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.50` tokens/step | Effective speedup: ~`2.50x` vs single-token decode |
| **Graphs Reused** | `2,861` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 643 | 98.0% | 4.13 | 155.74 |
| 2 | 664 | 100.0% | 4.56 | 145.59 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 103 | 13.19 t/s | 13.32 t/s |
| 2 | 136 | 12.46 t/s | 10.64 t/s |
| 3 | 164 | 11.77 t/s | 9.29 t/s |
| 4 | 195 | 11.44 t/s | 9.96 t/s |
| 5 | 233 | 11.53 t/s | 11.99 t/s |
| 6 | 272 | 11.71 t/s | 12.92 t/s |
| 7 | 300 | 11.39 t/s | 9.00 t/s |
| 8 | 336 | 11.43 t/s | 11.83 t/s |
| 9 | 366 | 11.30 t/s | 9.99 t/s |
| 10 | 398 | 11.14 t/s | 9.59 t/s |
| 11 | 419 | 10.76 t/s | 6.53 t/s |
| 12 | 442 | 10.51 t/s | 7.44 t/s |
| 13 | 473 | 10.49 t/s | 10.16 t/s |
| 14 | 504 | 10.47 t/s | 10.23 t/s |
| 15 | 526 | 10.26 t/s | 6.99 t/s |
| 16 | 556 | 10.22 t/s | 9.56 t/s |
| 17 | 584 | 10.13 t/s | 8.59 t/s |
| 18 | 628 | 10.32 t/s | 13.81 t/s |
| 19 | 658 | 10.28 t/s | 9.50 t/s |
| 20 | 690 | 10.27 t/s | 10.05 t/s |
| 21 | 718 | 10.22 t/s | 9.13 t/s |
| 22 | 749 | 10.21 t/s | 10.12 t/s |
| 23 | 776 | 10.15 t/s | 8.74 t/s |
| 24 | 807 | 10.15 t/s | 10.04 t/s |
| 25 | 837 | 10.13 t/s | 9.58 t/s |
| 26 | 864 | 10.08 t/s | 8.86 t/s |
| 27 | 892 | 10.04 t/s | 9.00 t/s |
| 28 | 912 | 9.92 t/s | 6.37 t/s |
| 29 | 940 | 9.88 t/s | 8.74 t/s |
| 30 | 969 | 9.86 t/s | 9.28 t/s |
| 31 | 997 | 9.82 t/s | 8.65 t/s |
| 32 | 1,025 | 9.80 t/s | 9.01 t/s |
| 33 | 1,053 | 9.77 t/s | 8.89 t/s |
| 34 | 1,080 | 9.75 t/s | 9.00 t/s |
| 35 | 1,108 | 9.72 t/s | 8.65 t/s |
| 36 | 1,141 | 9.73 t/s | 10.31 t/s |
| 37 | 1,166 | 9.69 t/s | 8.17 t/s |
| 38 | 1,194 | 9.67 t/s | 8.81 t/s |
| 39 | 1,226 | 9.69 t/s | 10.21 t/s |
| 40 | 1,255 | 9.68 t/s | 9.26 t/s |
| 41 | 1,279 | 9.64 t/s | 7.92 t/s |
| 42 | 1,306 | 9.62 t/s | 8.88 t/s |
| 43 | 1,331 | 9.58 t/s | 7.99 t/s |
| 44 | 1,355 | 9.53 t/s | 7.48 t/s |
| 45 | 1,383 | 9.53 t/s | 9.22 t/s |
| 46 | 1,408 | 9.49 t/s | 7.74 t/s |
| 47 | 1,440 | 9.50 t/s | 10.22 t/s |
| 48 | 1,465 | 9.47 t/s | 7.83 t/s |
| 49 | 1,501 | 9.50 t/s | 10.75 t/s |
| 50 | 1,537 | 9.53 t/s | 11.33 t/s |
| 51 | 1,567 | 9.54 t/s | 9.95 t/s |
| 52 | 1,605 | 9.59 t/s | 12.51 t/s |
| 53 | 1,638 | 9.61 t/s | 10.31 t/s |
| 54 | 1,675 | 9.65 t/s | 11.72 t/s |
| 55 | 1,712 | 9.69 t/s | 11.98 t/s |
| 56 | 1,746 | 9.70 t/s | 10.58 t/s |
| 57 | 1,781 | 9.73 t/s | 11.11 t/s |
| 58 | 1,810 | 9.72 t/s | 9.19 t/s |
| 59 | 1,834 | 9.68 t/s | 7.59 t/s |
| 60 | 1,875 | 9.73 t/s | 12.85 t/s |
| 61 | 1,914 | 9.77 t/s | 12.05 t/s |
| 62 | 1,952 | 9.82 t/s | 12.66 t/s |
| 63 | 1,987 | 9.83 t/s | 10.87 t/s |
| 64 | 2,027 | 9.87 t/s | 12.37 t/s |
| 65 | 2,066 | 9.91 t/s | 12.22 t/s |
| 66 | 2,104 | 9.94 t/s | 12.18 t/s |
| 67 | 2,139 | 9.96 t/s | 11.05 t/s |
| 68 | 2,182 | 10.02 t/s | 14.26 t/s |
| 69 | 2,232 | 10.10 t/s | 15.87 t/s |
| 70 | 2,287 | 10.20 t/s | 17.00 t/s |
| 71 | 2,341 | 10.30 t/s | 17.20 t/s |
| 72 | 2,390 | 10.37 t/s | 15.89 t/s |
| 73 | 2,440 | 10.45 t/s | 16.57 t/s |
| 74 | 2,485 | 10.51 t/s | 14.71 t/s |
| 75 | 2,531 | 10.56 t/s | 14.21 t/s |
| 76 | 2,582 | 10.64 t/s | 16.75 t/s |
| 77 | 2,630 | 10.70 t/s | 15.50 t/s |
| 78 | 2,660 | 10.69 t/s | 9.76 t/s |
| 79 | 2,695 | 10.69 t/s | 11.12 t/s |
| 80 | 2,743 | 10.75 t/s | 15.93 t/s |
| 81 | 2,795 | 10.83 t/s | 16.93 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:44:21.467` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `30` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `6.43 t/s` (`155.62 ms/tok`) | Time To First Token (TTFT) = `3.11s` |
| **Decode Speed (Generation)** | `30.28 t/s` (`33.03 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `20` (66.7%) / Out: `10` (33.3%) | Total context footprint: `30` tokens |
| **Speculative MTP Acceptance** | `100.00%` (`6/6`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `4.00` tokens/step | Effective speedup: ~`4.00x` vs single-token decode |
| **Graphs Reused** | `2` | CUDA/execution graph cache hits |

---

## Task #6 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:44:34.858` (Queue Delay: `1.89s`)
* **Total Context Footprint:** `159` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `8.37 t/s` (`119.48 ms/tok`) | Time To First Token (TTFT) = `2.03s` |
| **Decode Speed (Generation)** | `95.37 t/s` (`10.49 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `17` (10.7%) / Out: `142` (89.3%) | Total context footprint: `159` tokens |
| **Speculative MTP Acceptance** | `84.17%` (`101/120`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.52` tokens/step | Effective speedup: ~`3.52x` vs single-token decode |
| **Graphs Reused** | `41` | CUDA/execution graph cache hits |

---

## Task #49 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:46:59.600` (Queue Delay: `1.95s`)
* **Total Context Footprint:** `748` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `8.42 t/s` (`118.76 ms/tok`) | Time To First Token (TTFT) = `2.02s` |
| **Decode Speed (Generation)** | `70.04 t/s` (`14.28 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `17` (2.3%) / Out: `731` (97.7%) | Total context footprint: `748` tokens |
| **Speculative MTP Acceptance** | `54.32%` (`453/834`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.63` tokens/step | Effective speedup: ~`2.63x` vs single-token decode |
| **Graphs Reused** | `316` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 222 | 72.98 t/s | 73.31 t/s |
| 2 | 418 | 69.09 t/s | 65.17 t/s |
| 3 | 639 | 70.53 t/s | 73.43 t/s |

---

## Task #330 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:47:47.731` (Queue Delay: `2.06s`)
* **Total Context Footprint:** `2976` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `29.42 t/s` (`33.99 ms/tok`) | Time To First Token (TTFT) = `6.73s` |
| **Decode Speed (Generation)** | `67.68 t/s` (`14.78 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `198` (6.7%) / Out: `2778` (93.3%) | Total context footprint: `2976` tokens |
| **Speculative MTP Acceptance** | `51.98%` (`1692/3255`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.56` tokens/step | Effective speedup: ~`2.56x` vs single-token decode |
| **Graphs Reused** | `1,389` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 194 | 98.0% | 4.68 | 41.47 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 209 | 68.64 t/s | 68.97 t/s |
| 2 | 411 | 67.72 t/s | 66.81 t/s |
| 3 | 604 | 66.58 t/s | 64.27 t/s |
| 4 | 790 | 65.38 t/s | 61.77 t/s |
| 5 | 960 | 63.57 t/s | 56.33 t/s |
| 6 | 1,123 | 62.02 t/s | 54.24 t/s |
| 7 | 1,304 | 61.70 t/s | 59.80 t/s |
| 8 | 1,459 | 60.44 t/s | 51.57 t/s |
| 9 | 1,614 | 59.42 t/s | 51.28 t/s |
| 10 | 1,803 | 59.72 t/s | 62.39 t/s |
| 11 | 2,056 | 61.93 t/s | 84.12 t/s |
| 12 | 2,358 | 65.10 t/s | 99.88 t/s |
| 13 | 2,655 | 67.67 t/s | 98.58 t/s |

---

## Task #1419 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:49:33.318` (Queue Delay: `2.60s`)
* **Total Context Footprint:** `2674` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `120.55 t/s` (`8.30 ms/tok`) | Time To First Token (TTFT) = `7.76s` |
| **Decode Speed (Generation)** | `68.72 t/s` (`14.55 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `936` (35.0%) / Out: `1738` (65.0%) | Total context footprint: `2674` tokens |
| **Speculative MTP Acceptance** | `53.73%` (`1072/1995`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.61` tokens/step | Effective speedup: ~`2.61x` vs single-token decode |
| **Graphs Reused** | `2,046` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 932 | 100.0% | 5.63 | 165.58 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 193 | 63.77 t/s | 64.11 t/s |
| 2 | 380 | 62.99 t/s | 62.20 t/s |
| 3 | 553 | 61.18 t/s | 57.55 t/s |
| 4 | 730 | 60.57 t/s | 58.73 t/s |
| 5 | 894 | 59.28 t/s | 54.16 t/s |
| 6 | 1,107 | 61.12 t/s | 70.28 t/s |
| 7 | 1,333 | 63.14 t/s | 75.29 t/s |
| 8 | 1,626 | 67.33 t/s | 96.44 t/s |

---

## Task #2089 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:51:27.117` (Queue Delay: `2.54s`)
* **Total Context Footprint:** `2864` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `80.44 t/s` (`12.43 ms/tok`) | Time To First Token (TTFT) = `6.99s` |
| **Decode Speed (Generation)** | `68.42 t/s` (`14.62 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `562` (19.6%) / Out: `2302` (80.4%) | Total context footprint: `2864` tokens |
| **Speculative MTP Acceptance** | `57.05%` (`1453/2547`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.71` tokens/step | Effective speedup: ~`2.71x` vs single-token decode |
| **Graphs Reused** | `2,885` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 558 | 100.0% | 4.78 | 116.65 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 198 | 65.08 t/s | 65.41 t/s |
| 2 | 351 | 57.91 t/s | 50.72 t/s |
| 3 | 517 | 56.96 t/s | 55.05 t/s |
| 4 | 672 | 55.54 t/s | 51.28 t/s |
| 5 | 851 | 56.25 t/s | 59.07 t/s |
| 6 | 1,063 | 58.54 t/s | 69.97 t/s |
| 7 | 1,269 | 59.90 t/s | 68.05 t/s |
| 8 | 1,464 | 60.45 t/s | 64.29 t/s |
| 9 | 1,710 | 62.77 t/s | 81.40 t/s |
| 10 | 1,975 | 65.31 t/s | 88.33 t/s |
| 11 | 2,267 | 68.13 t/s | 96.17 t/s |

---

## Task #2943 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:52:32.690` (Queue Delay: `2.81s`)
* **Total Context Footprint:** `2266` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `57.28 t/s` (`17.46 ms/tok`) | Time To First Token (TTFT) = `6.56s` |
| **Decode Speed (Generation)** | `62.87 t/s` (`15.91 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `376` (16.6%) / Out: `1890` (83.4%) | Total context footprint: `2266` tokens |
| **Speculative MTP Acceptance** | `47.29%` (`1108/2343`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.42` tokens/step | Effective speedup: ~`2.42x` vs single-token decode |
| **Graphs Reused** | `3,658` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 372 | 100.0% | 4.46 | 83.39 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 215 | 70.46 t/s | 70.78 t/s |
| 2 | 405 | 66.66 t/s | 62.85 t/s |
| 3 | 586 | 64.36 t/s | 59.75 t/s |
| 4 | 769 | 63.34 t/s | 60.31 t/s |
| 5 | 960 | 63.23 t/s | 62.76 t/s |
| 6 | 1,161 | 63.84 t/s | 66.95 t/s |
| 7 | 1,345 | 63.46 t/s | 61.19 t/s |
| 8 | 1,517 | 62.67 t/s | 57.09 t/s |
| 9 | 1,708 | 62.72 t/s | 63.14 t/s |

---

## Task #3728 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:54:12.660` (Queue Delay: `0.02s`)
* **Total Context Footprint:** `2082` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `85.09 t/s` (`11.75 ms/tok`) | Time To First Token (TTFT) = `7.24s` |
| **Decode Speed (Generation)** | `71.37 t/s` (`14.01 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `616` (29.6%) / Out: `1466` (70.4%) | Total context footprint: `2082` tokens |
| **Speculative MTP Acceptance** | `60.23%` (`945/1569`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.81` tokens/step | Effective speedup: ~`2.81x` vs single-token decode |
| **Graphs Reused** | `4,174` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 612 | 100.0% | 5.04 | 121.52 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 208 | 68.76 t/s | 69.09 t/s |
| 2 | 381 | 62.93 t/s | 57.13 t/s |
| 3 | 573 | 63.04 t/s | 63.25 t/s |
| 4 | 777 | 64.07 t/s | 67.15 t/s |
| 5 | 984 | 64.98 t/s | 68.64 t/s |
| 6 | 1,239 | 68.14 t/s | 83.89 t/s |

---

## Task #4256 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:55:46.688` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `907` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `42.59 t/s` (`23.48 ms/tok`) | Time To First Token (TTFT) = `6.81s` |
| **Decode Speed (Generation)** | `54.12 t/s` (`18.48 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `290` (32.0%) / Out: `617` (68.0%) | Total context footprint: `907` tokens |
| **Speculative MTP Acceptance** | `35.80%` (`319/891`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.07` tokens/step | Effective speedup: ~`2.07x` vs single-token decode |
| **Graphs Reused** | `4,467` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 286 | 100.0% | 4.59 | 62.33 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 152 | 49.89 t/s | 50.22 t/s |
| 2 | 320 | 52.82 t/s | 55.76 t/s |
| 3 | 491 | 54.18 t/s | 56.91 t/s |

---

## Task #4557 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:57:20.758` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `3315` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `86.07 t/s` (`11.62 ms/tok`) | Time To First Token (TTFT) = `7.56s` |
| **Decode Speed (Generation)** | `64.54 t/s` (`15.49 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `651` (19.6%) / Out: `2664` (80.4%) | Total context footprint: `3315` tokens |
| **Speculative MTP Acceptance** | `53.67%` (`1644/3063`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.61` tokens/step | Effective speedup: ~`2.61x` vs single-token decode |
| **Graphs Reused** | `5,477` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 647 | 100.0% | 5.30 | 122.04 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 200 | 66.23 t/s | 66.56 t/s |
| 2 | 395 | 65.39 t/s | 64.55 t/s |
| 3 | 575 | 63.35 t/s | 59.31 t/s |
| 4 | 750 | 62.08 t/s | 58.23 t/s |
| 5 | 915 | 60.54 t/s | 54.44 t/s |
| 6 | 1,079 | 59.50 t/s | 54.27 t/s |
| 7 | 1,236 | 58.41 t/s | 51.89 t/s |
| 8 | 1,399 | 57.88 t/s | 54.20 t/s |
| 9 | 1,586 | 58.31 t/s | 61.69 t/s |
| 10 | 1,774 | 58.73 t/s | 62.57 t/s |
| 11 | 1,951 | 58.69 t/s | 58.27 t/s |
| 12 | 2,226 | 61.37 t/s | 90.83 t/s |
| 13 | 2,494 | 63.50 t/s | 89.08 t/s |

---

## Task #5583 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-10 23:59:44.847` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `890` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `90.22 t/s` (`11.08 ms/tok`) | Time To First Token (TTFT) = `7.91s` |
| **Decode Speed (Generation)** | `55.37 t/s` (`18.06 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `714` (80.2%) / Out: `176` (19.8%) | Total context footprint: `890` tokens |
| **Speculative MTP Acceptance** | `41.77%` (`99/237`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.25` tokens/step | Effective speedup: ~`2.25x` vs single-token decode |
| **Graphs Reused** | `5,554` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 710 | 100.0% | 5.61 | 126.52 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 171 | 56.64 t/s | 56.97 t/s |

---

## Task #5667 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:00:13.386` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `1726` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `27.18 t/s` (`36.79 ms/tok`) | Time To First Token (TTFT) = `7.14s` |
| **Decode Speed (Generation)** | `61.09 t/s` (`16.37 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `194` (11.2%) / Out: `1532` (88.8%) | Total context footprint: `1726` tokens |
| **Speculative MTP Acceptance** | `49.49%` (`916/1851`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.48` tokens/step | Effective speedup: ~`2.48x` vs single-token decode |
| **Graphs Reused** | `6,164` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 190 | 100.0% | 4.87 | 39.04 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 199 | 65.82 t/s | 66.15 t/s |
| 2 | 370 | 61.16 t/s | 56.53 t/s |
| 3 | 539 | 59.49 t/s | 56.14 t/s |
| 4 | 696 | 57.54 t/s | 51.73 t/s |
| 5 | 864 | 56.95 t/s | 54.61 t/s |
| 6 | 1,050 | 57.76 t/s | 61.83 t/s |
| 7 | 1,261 | 59.46 t/s | 69.71 t/s |
| 8 | 1,483 | 61.23 t/s | 73.64 t/s |

---

## Task #6288 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:01:39.973` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `1838` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `52.05 t/s` (`19.21 ms/tok`) | Time To First Token (TTFT) = `7.47s` |
| **Decode Speed (Generation)** | `65.41 t/s` (`15.29 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `389` (21.2%) / Out: `1449` (78.8%) | Total context footprint: `1838` tokens |
| **Speculative MTP Acceptance** | `56.22%` (`909/1617`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.69` tokens/step | Effective speedup: ~`2.69x` vs single-token decode |
| **Graphs Reused** | `6,697` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 385 | 100.0% | 5.06 | 76.06 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 207 | 68.48 t/s | 68.81 t/s |
| 2 | 382 | 63.18 t/s | 57.91 t/s |
| 3 | 550 | 60.71 t/s | 55.76 t/s |
| 4 | 718 | 59.49 t/s | 55.84 t/s |
| 5 | 915 | 60.62 t/s | 65.08 t/s |
| 6 | 1,118 | 61.73 t/s | 67.33 t/s |
| 7 | 1,359 | 64.35 t/s | 80.06 t/s |

---

## Task #6831 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:03:00.963` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `1993` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `40.46 t/s` (`24.72 ms/tok`) | Time To First Token (TTFT) = `7.42s` |
| **Decode Speed (Generation)** | `60.21 t/s` (`16.61 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `300` (15.1%) / Out: `1693` (84.9%) | Total context footprint: `1993` tokens |
| **Speculative MTP Acceptance** | `49.00%` (`1007/2055`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.47` tokens/step | Effective speedup: ~`2.47x` vs single-token decode |
| **Graphs Reused** | `7,375` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 296 | 100.0% | 5.03 | 58.90 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 192 | 63.11 t/s | 63.44 t/s |
| 2 | 338 | 55.62 t/s | 48.14 t/s |
| 3 | 510 | 56.08 t/s | 57.01 t/s |
| 4 | 687 | 56.80 t/s | 58.98 t/s |
| 5 | 847 | 55.98 t/s | 52.71 t/s |
| 6 | 1,002 | 55.17 t/s | 51.11 t/s |
| 7 | 1,176 | 55.48 t/s | 57.35 t/s |
| 8 | 1,371 | 56.63 t/s | 64.76 t/s |
| 9 | 1,618 | 59.40 t/s | 81.49 t/s |

---

## Task #7520 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:04:56.627` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `750` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `52.77 t/s` (`18.95 ms/tok`) | Time To First Token (TTFT) = `7.67s` |
| **Decode Speed (Generation)** | `50.12 t/s` (`19.95 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `405` (54.0%) / Out: `345` (46.0%) | Total context footprint: `750` tokens |
| **Speculative MTP Acceptance** | `35.12%` (`177/504`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.05` tokens/step | Effective speedup: ~`2.05x` vs single-token decode |
| **Graphs Reused** | `7,540` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 401 | 100.0% | 5.25 | 76.44 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 160 | 52.92 t/s | 53.25 t/s |
| 2 | 298 | 49.38 t/s | 45.84 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 00:17:34.051` (Queue Delay: `0.02s`)
* **Total Context Footprint:** `711` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `325.07 t/s` (`3.08 ms/tok`) | Time To First Token (TTFT) = `1.33s` |
| **Decode Speed (Generation)** | `46.72 t/s` (`21.40 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `433` (60.9%) / Out: `278` (39.1%) | Total context footprint: `711` tokens |
| **Graphs Reused** | `276` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 141 | 46.42 t/s | 46.76 t/s |

---

## Task #281 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 00:17:41.718` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `1143` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `301.52 t/s` (`3.32 ms/tok`) | Time To First Token (TTFT) = `2.09s` |
| **Decode Speed (Generation)** | `46.46 t/s` (`21.52 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `629` (55.0%) / Out: `514` (45.0%) | Total context footprint: `1143` tokens |
| **Graphs Reused** | `786` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 140 | 46.18 t/s | 46.51 t/s |
| 2 | 278 | 45.97 t/s | 45.76 t/s |
| 3 | 419 | 46.25 t/s | 46.82 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Huihui-Qwythos-9B-Claude-Mythos-5-1M-abliterated-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:19:51.414` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `589` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `10.91 t/s` (`91.67 ms/tok`) | Time To First Token (TTFT) = `1.65s` |
| **Decode Speed (Generation)** | `39.26 t/s` (`25.47 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `18` (3.1%) / Out: `571` (96.9%) | Total context footprint: `589` tokens |
| **Speculative MTP Acceptance** | `33.68%` (`287/852`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.01` tokens/step | Effective speedup: ~`2.01x` vs single-token decode |
| **Graphs Reused** | `282` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 118 | 38.94 t/s | 39.27 t/s |
| 2 | 227 | 37.35 t/s | 35.79 t/s |
| 3 | 346 | 38.06 t/s | 39.50 t/s |
| 4 | 468 | 38.63 t/s | 40.32 t/s |

---

## Task #287 (Slot 0)

* **Model:** `Huihui-Qwythos-9B-Claude-Mythos-5-1M-abliterated-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:20:26.845` (Queue Delay: `1.93s`)
* **Total Context Footprint:** `954` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `45.37 t/s` (`22.04 ms/tok`) | Time To First Token (TTFT) = `5.07s` |
| **Decode Speed (Generation)** | `40.93 t/s` (`24.43 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `230` (24.1%) / Out: `724` (75.9%) | Total context footprint: `954` tokens |
| **Speculative MTP Acceptance** | `37.55%` (`383/1020`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.13` tokens/step | Effective speedup: ~`2.13x` vs single-token decode |
| **Graphs Reused** | `618` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 226 | 98.0% | 3.42 | 66.06 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 146 | 47.67 t/s | 48.00 t/s |
| 2 | 273 | 45.01 t/s | 42.31 t/s |
| 3 | 387 | 42.66 t/s | 37.95 t/s |
| 4 | 504 | 41.73 t/s | 38.93 t/s |
| 5 | 640 | 42.31 t/s | 44.58 t/s |

---

## Task #631 (Slot 0)

* **Model:** `Huihui-Qwythos-9B-Claude-Mythos-5-1M-abliterated-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:21:21.069` (Queue Delay: `2.60s`)
* **Total Context Footprint:** `1032` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `32.18 t/s` (`31.08 ms/tok`) | Time To First Token (TTFT) = `5.04s` |
| **Decode Speed (Generation)** | `37.98 t/s` (`26.33 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `162` (15.7%) / Out: `870` (84.3%) | Total context footprint: `1032` tokens |
| **Speculative MTP Acceptance** | `32.80%` (`431/1314`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `1.98` tokens/step | Effective speedup: ~`1.98x` vs single-token decode |
| **Graphs Reused** | `1,052` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 158 | 99.0% | 3.37 | 46.85 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 136 | 44.87 t/s | 45.20 t/s |
| 2 | 244 | 40.12 t/s | 35.44 t/s |
| 3 | 361 | 39.68 t/s | 38.78 t/s |
| 4 | 469 | 38.66 t/s | 35.62 t/s |
| 5 | 578 | 38.11 t/s | 35.91 t/s |
| 6 | 696 | 38.21 t/s | 38.69 t/s |
| 7 | 805 | 37.93 t/s | 36.28 t/s |

---

## Task #1073 (Slot 0)

* **Model:** `Huihui-Qwythos-9B-Claude-Mythos-5-1M-abliterated-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:22:34.484` (Queue Delay: `3.02s`)
* **Total Context Footprint:** `32368` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `41.57 t/s` (`24.06 ms/tok`) | Time To First Token (TTFT) = `5.08s` |
| **Decode Speed (Generation)** | `60.25 t/s` (`16.60 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `211` (0.7%) / Out: `32157` (99.3%) | Total context footprint: `32368` tokens |
| **Speculative MTP Acceptance** | `94.63%` (`23781/25130`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.84` tokens/step | Effective speedup: ~`3.84x` vs single-token decode |
| **Graphs Reused** | `9,302` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 207 | 99.0% | 3.47 | 59.68 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 139 | 45.32 t/s | 45.65 t/s |
| 2 | 251 | 41.30 t/s | 37.24 t/s |
| 3 | 377 | 41.44 t/s | 41.71 t/s |
| 4 | 499 | 41.18 t/s | 40.42 t/s |
| 5 | 621 | 41.08 t/s | 40.65 t/s |
| 6 | 731 | 40.32 t/s | 36.55 t/s |
| 7 | 853 | 40.34 t/s | 40.45 t/s |
| 8 | 974 | 40.31 t/s | 40.11 t/s |
| 9 | 1,109 | 40.78 t/s | 44.49 t/s |
| 10 | 1,239 | 40.98 t/s | 42.77 t/s |
| 11 | 1,377 | 41.39 t/s | 45.46 t/s |
| 12 | 1,504 | 41.41 t/s | 41.65 t/s |
| 13 | 1,688 | 42.92 t/s | 61.18 t/s |
| 14 | 1,910 | 45.11 t/s | 73.63 t/s |
| 15 | 2,137 | 47.13 t/s | 75.49 t/s |
| 16 | 2,361 | 48.83 t/s | 74.46 t/s |
| 17 | 2,585 | 50.31 t/s | 73.98 t/s |
| 18 | 2,807 | 51.61 t/s | 73.85 t/s |
| 19 | 3,031 | 52.79 t/s | 73.99 t/s |
| 20 | 3,255 | 53.86 t/s | 74.14 t/s |
| 21 | 3,479 | 54.82 t/s | 73.89 t/s |
| 22 | 3,703 | 55.68 t/s | 73.61 t/s |
| 23 | 3,927 | 56.46 t/s | 73.42 t/s |
| 24 | 4,151 | 57.17 t/s | 73.38 t/s |
| 25 | 4,370 | 57.76 t/s | 71.75 t/s |
| 26 | 4,590 | 58.31 t/s | 72.12 t/s |
| 27 | 4,810 | 58.82 t/s | 72.02 t/s |
| 28 | 5,026 | 59.29 t/s | 71.95 t/s |
| 29 | 5,242 | 59.71 t/s | 71.58 t/s |
| 30 | 5,458 | 60.10 t/s | 71.48 t/s |
| 31 | 5,670 | 60.41 t/s | 69.67 t/s |
| 32 | 5,882 | 60.73 t/s | 70.53 t/s |
| 33 | 6,094 | 61.02 t/s | 70.59 t/s |
| 34 | 6,301 | 61.25 t/s | 68.56 t/s |
| 35 | 6,497 | 61.36 t/s | 65.27 t/s |
| 36 | 6,685 | 61.39 t/s | 62.56 t/s |
| 37 | 6,873 | 61.41 t/s | 62.07 t/s |
| 38 | 7,061 | 61.42 t/s | 61.83 t/s |
| 39 | 7,249 | 61.43 t/s | 61.59 t/s |
| 40 | 7,441 | 61.47 t/s | 63.02 t/s |
| 41 | 7,637 | 61.53 t/s | 64.11 t/s |
| 42 | 7,833 | 61.60 t/s | 64.33 t/s |
| 43 | 8,029 | 61.67 t/s | 64.48 t/s |
| 44 | 8,225 | 61.72 t/s | 64.05 t/s |
| 45 | 8,421 | 61.77 t/s | 63.97 t/s |
| 46 | 8,617 | 61.82 t/s | 64.05 t/s |
| 47 | 8,809 | 61.86 t/s | 63.77 t/s |
| 48 | 9,000 | 61.90 t/s | 63.40 t/s |
| 49 | 9,192 | 61.93 t/s | 63.73 t/s |
| 50 | 9,384 | 61.97 t/s | 63.64 t/s |
| 51 | 9,576 | 62.00 t/s | 63.48 t/s |
| 52 | 9,768 | 62.02 t/s | 63.05 t/s |
| 53 | 9,960 | 62.04 t/s | 63.26 t/s |
| 54 | 10,151 | 62.05 t/s | 62.78 t/s |
| 55 | 10,343 | 62.07 t/s | 62.74 t/s |
| 56 | 10,531 | 62.07 t/s | 62.35 t/s |
| 57 | 10,717 | 62.06 t/s | 61.50 t/s |
| 58 | 10,909 | 62.08 t/s | 63.24 t/s |
| 59 | 11,101 | 62.10 t/s | 62.89 t/s |
| 60 | 11,293 | 62.11 t/s | 62.73 t/s |
| 61 | 11,481 | 62.11 t/s | 62.41 t/s |
| 62 | 11,669 | 62.11 t/s | 61.85 t/s |
| 63 | 11,857 | 62.11 t/s | 62.33 t/s |
| 64 | 12,045 | 62.11 t/s | 62.15 t/s |
| 65 | 12,233 | 62.11 t/s | 62.14 t/s |
| 66 | 12,421 | 62.11 t/s | 62.28 t/s |
| 67 | 12,609 | 62.11 t/s | 62.02 t/s |
| 68 | 12,793 | 62.10 t/s | 61.31 t/s |
| 69 | 12,977 | 62.08 t/s | 60.87 t/s |
| 70 | 13,165 | 62.08 t/s | 61.65 t/s |
| 71 | 13,353 | 62.07 t/s | 61.53 t/s |
| 72 | 13,537 | 62.05 t/s | 61.00 t/s |
| 73 | 13,725 | 62.05 t/s | 61.49 t/s |
| 74 | 13,909 | 62.03 t/s | 60.77 t/s |
| 75 | 14,093 | 62.01 t/s | 60.69 t/s |
| 76 | 14,277 | 61.99 t/s | 60.48 t/s |
| 77 | 14,461 | 61.97 t/s | 60.34 t/s |
| 78 | 14,645 | 61.94 t/s | 60.05 t/s |
| 79 | 14,829 | 61.92 t/s | 60.31 t/s |
| 80 | 15,013 | 61.91 t/s | 60.78 t/s |
| 81 | 15,196 | 61.88 t/s | 59.75 t/s |
| 82 | 15,379 | 61.86 t/s | 59.85 t/s |
| 83 | 15,559 | 61.84 t/s | 59.97 t/s |
| 84 | 15,739 | 61.81 t/s | 59.84 t/s |
| 85 | 15,919 | 61.79 t/s | 59.66 t/s |
| 86 | 16,099 | 61.76 t/s | 59.59 t/s |
| 87 | 16,279 | 61.74 t/s | 59.79 t/s |
| 88 | 16,459 | 61.72 t/s | 59.68 t/s |
| 89 | 16,639 | 61.69 t/s | 59.52 t/s |
| 90 | 16,819 | 61.66 t/s | 59.04 t/s |
| 91 | 16,999 | 61.64 t/s | 59.49 t/s |
| 92 | 17,179 | 61.61 t/s | 59.17 t/s |
| 93 | 17,359 | 61.59 t/s | 59.42 t/s |
| 94 | 17,543 | 61.58 t/s | 60.53 t/s |
| 95 | 17,731 | 61.58 t/s | 61.65 t/s |
| 96 | 17,915 | 61.56 t/s | 60.43 t/s |
| 97 | 18,099 | 61.55 t/s | 60.08 t/s |
| 98 | 18,279 | 61.52 t/s | 59.05 t/s |
| 99 | 18,459 | 61.50 t/s | 59.43 t/s |
| 100 | 18,639 | 61.49 t/s | 59.77 t/s |
| 101 | 18,819 | 61.47 t/s | 59.86 t/s |
| 102 | 19,007 | 61.47 t/s | 61.49 t/s |
| 103 | 19,191 | 61.46 t/s | 60.68 t/s |
| 104 | 19,375 | 61.45 t/s | 60.17 t/s |
| 105 | 19,555 | 61.43 t/s | 59.89 t/s |
| 106 | 19,735 | 61.42 t/s | 59.49 t/s |
| 107 | 19,915 | 61.40 t/s | 59.54 t/s |
| 108 | 20,095 | 61.38 t/s | 59.57 t/s |
| 109 | 20,275 | 61.36 t/s | 59.55 t/s |
| 110 | 20,455 | 61.35 t/s | 59.59 t/s |
| 111 | 20,635 | 61.33 t/s | 59.25 t/s |
| 112 | 20,819 | 61.33 t/s | 60.92 t/s |
| 113 | 21,007 | 61.33 t/s | 62.14 t/s |
| 114 | 21,195 | 61.34 t/s | 61.53 t/s |
| 115 | 21,375 | 61.31 t/s | 58.96 t/s |
| 116 | 21,551 | 61.29 t/s | 58.10 t/s |
| 117 | 21,727 | 61.26 t/s | 57.80 t/s |
| 118 | 21,907 | 61.24 t/s | 59.06 t/s |
| 119 | 22,087 | 61.22 t/s | 58.85 t/s |
| 120 | 22,263 | 61.19 t/s | 57.54 t/s |
| 121 | 22,443 | 61.17 t/s | 59.06 t/s |
| 122 | 22,619 | 61.15 t/s | 58.59 t/s |
| 123 | 22,795 | 61.13 t/s | 58.59 t/s |
| 124 | 22,979 | 61.12 t/s | 60.77 t/s |
| 125 | 23,163 | 61.12 t/s | 60.37 t/s |
| 126 | 23,347 | 61.12 t/s | 60.72 t/s |
| 127 | 23,531 | 61.11 t/s | 60.03 t/s |
| 128 | 23,715 | 61.10 t/s | 60.33 t/s |
| 129 | 23,899 | 61.10 t/s | 60.55 t/s |
| 130 | 24,083 | 61.09 t/s | 60.24 t/s |
| 131 | 24,263 | 61.08 t/s | 59.69 t/s |
| 132 | 24,439 | 61.06 t/s | 58.22 t/s |
| 133 | 24,623 | 61.05 t/s | 60.25 t/s |
| 134 | 24,807 | 61.05 t/s | 60.25 t/s |
| 135 | 24,991 | 61.04 t/s | 60.02 t/s |
| 136 | 25,171 | 61.02 t/s | 58.96 t/s |
| 137 | 25,351 | 61.01 t/s | 59.52 t/s |
| 138 | 25,531 | 61.00 t/s | 59.82 t/s |
| 139 | 25,709 | 60.99 t/s | 58.65 t/s |
| 140 | 25,885 | 60.96 t/s | 57.92 t/s |
| 141 | 26,065 | 60.95 t/s | 58.93 t/s |
| 142 | 26,245 | 60.94 t/s | 59.55 t/s |
| 143 | 26,417 | 60.91 t/s | 57.33 t/s |
| 144 | 26,589 | 60.89 t/s | 57.29 t/s |
| 145 | 26,765 | 60.87 t/s | 58.07 t/s |
| 146 | 26,941 | 60.86 t/s | 58.64 t/s |
| 147 | 27,117 | 60.83 t/s | 57.85 t/s |
| 148 | 27,289 | 60.81 t/s | 57.10 t/s |
| 149 | 27,465 | 60.79 t/s | 57.52 t/s |
| 150 | 27,641 | 60.77 t/s | 58.13 t/s |
| 151 | 27,813 | 60.75 t/s | 57.31 t/s |
| 152 | 27,989 | 60.73 t/s | 58.57 t/s |
| 153 | 28,165 | 60.71 t/s | 57.90 t/s |
| 154 | 28,341 | 60.70 t/s | 58.33 t/s |
| 155 | 28,517 | 60.68 t/s | 58.09 t/s |
| 156 | 28,693 | 60.66 t/s | 57.79 t/s |
| 157 | 28,869 | 60.65 t/s | 58.23 t/s |
| 158 | 29,045 | 60.63 t/s | 58.17 t/s |
| 159 | 29,221 | 60.62 t/s | 57.96 t/s |
| 160 | 29,397 | 60.60 t/s | 58.02 t/s |
| 161 | 29,573 | 60.58 t/s | 57.67 t/s |
| 162 | 29,745 | 60.56 t/s | 57.09 t/s |
| 163 | 29,921 | 60.54 t/s | 57.34 t/s |
| 164 | 30,097 | 60.52 t/s | 57.52 t/s |
| 165 | 30,269 | 60.50 t/s | 56.97 t/s |
| 166 | 30,441 | 60.48 t/s | 57.23 t/s |
| 167 | 30,613 | 60.46 t/s | 57.10 t/s |
| 168 | 30,781 | 60.43 t/s | 55.97 t/s |
| 169 | 30,953 | 60.41 t/s | 56.61 t/s |
| 170 | 31,125 | 60.39 t/s | 57.11 t/s |
| 171 | 31,297 | 60.37 t/s | 57.10 t/s |
| 172 | 31,469 | 60.35 t/s | 56.60 t/s |
| 173 | 31,641 | 60.33 t/s | 56.82 t/s |
| 174 | 31,813 | 60.31 t/s | 56.19 t/s |
| 175 | 31,985 | 60.28 t/s | 56.03 t/s |
| 176 | 32,156 | 60.26 t/s | 56.22 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 00:28:44.413` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `22` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `4.56 t/s` (`219.38 ms/tok`) | Time To First Token (TTFT) = `4.39s` |
| **Decode Speed (Generation)** | `18.02 t/s` (`55.48 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `20` (90.9%) / Out: `2` (9.1%) | Total context footprint: `22` tokens |
| **Graphs Reused** | `2` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 8 | 40.0% | 4.14 | 1.93 |
| 2 | 16 | 80.0% | 4.22 | 3.79 |

---

## Task #5 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 00:31:43.058` (Queue Delay: `0.02s`)
* **Total Context Footprint:** `28` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `7.01 t/s` (`142.75 ms/tok`) | Time To First Token (TTFT) = `1.57s` |
| **Decode Speed (Generation)** | `54.15 t/s` (`18.47 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `11` (39.3%) / Out: `17` (60.7%) | Total context footprint: `28` tokens |
| **Graphs Reused** | `17` | CUDA/execution graph cache hits |

---

## Task #25 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 00:33:28.367` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `169` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `310.38 t/s` (`3.22 ms/tok`) | Time To First Token (TTFT) = `0.34s` |
| **Decode Speed (Generation)** | `54.47 t/s` (`18.36 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `107` (63.3%) / Out: `62` (36.7%) | Total context footprint: `169` tokens |
| **Graphs Reused** | `77` | CUDA/execution graph cache hits |

---

## Task #90 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 00:33:30.238` (Queue Delay: `0.02s`)
* **Total Context Footprint:** `254` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `59.72 t/s` (`16.75 ms/tok`) | Time To First Token (TTFT) = `1.19s` |
| **Decode Speed (Generation)** | `50.99 t/s` (`19.61 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `71` (28.0%) / Out: `183` (72.0%) | Total context footprint: `254` tokens |
| **Graphs Reused** | `257` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 153 | 50.66 t/s | 50.99 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Huihui-Qwythos-9B-Claude-Mythos-5-1M-abliterated-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:50:04.859` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `1250` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `21.40 t/s` (`46.72 ms/tok`) | Time To First Token (TTFT) = `1.68s` |
| **Decode Speed (Generation)** | `44.83 t/s` (`22.31 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `36` (2.9%) / Out: `1214` (97.1%) | Total context footprint: `1250` tokens |
| **Speculative MTP Acceptance** | `45.24%` (`699/1545`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.36` tokens/step | Effective speedup: ~`2.36x` vs single-token decode |
| **Graphs Reused** | `511` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 143 | 47.18 t/s | 47.51 t/s |
| 2 | 271 | 44.56 t/s | 41.98 t/s |
| 3 | 403 | 44.33 t/s | 43.86 t/s |
| 4 | 527 | 43.52 t/s | 41.08 t/s |
| 5 | 660 | 43.55 t/s | 43.68 t/s |
| 6 | 801 | 44.04 t/s | 46.47 t/s |
| 7 | 932 | 43.90 t/s | 43.09 t/s |
| 8 | 1,058 | 43.64 t/s | 41.80 t/s |

---

## Task #518 (Slot 0)

* **Model:** `Huihui-Qwythos-9B-Claude-Mythos-5-1M-abliterated-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 00:55:53.326` (Queue Delay: `2.86s`)
* **Total Context Footprint:** `834` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `28.75 t/s` (`34.79 ms/tok`) | Time To First Token (TTFT) = `4.97s` |
| **Decode Speed (Generation)** | `41.77 t/s` (`23.94 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `143` (17.1%) / Out: `691` (82.9%) | Total context footprint: `834` tokens |
| **Speculative MTP Acceptance** | `39.66%` (`376/948`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.19` tokens/step | Effective speedup: ~`2.19x` vs single-token decode |
| **Graphs Reused** | `823` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 139 | 98.0% | 3.33 | 41.80 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 137 | 44.90 t/s | 45.23 t/s |
| 2 | 244 | 40.29 t/s | 35.64 t/s |
| 3 | 370 | 40.83 t/s | 41.90 t/s |
| 4 | 513 | 42.43 t/s | 47.20 t/s |
| 5 | 640 | 42.33 t/s | 41.93 t/s |

---

## Task #838 (Slot 0)

* **Model:** `Huihui-Qwythos-9B-Claude-Mythos-5-1M-abliterated-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 01:00:19.412` (Queue Delay: `2.44s`)
* **Total Context Footprint:** `1435` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `32.12 t/s` (`31.14 ms/tok`) | Time To First Token (TTFT) = `4.98s` |
| **Decode Speed (Generation)** | `42.05 t/s` (`23.78 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `160` (11.1%) / Out: `1275` (88.9%) | Total context footprint: `1435` tokens |
| **Speculative MTP Acceptance** | `40.77%` (`702/1722`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.22` tokens/step | Effective speedup: ~`2.22x` vs single-token decode |
| **Graphs Reused** | `1,391` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 156 | 99.0% | 3.33 | 46.85 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 133 | 43.59 t/s | 43.92 t/s |
| 2 | 255 | 42.07 t/s | 40.55 t/s |
| 3 | 364 | 40.13 t/s | 36.22 t/s |
| 4 | 484 | 39.95 t/s | 39.40 t/s |
| 5 | 614 | 40.50 t/s | 42.72 t/s |
| 6 | 742 | 40.78 t/s | 42.13 t/s |
| 7 | 870 | 40.96 t/s | 42.07 t/s |
| 8 | 999 | 41.19 t/s | 42.80 t/s |
| 9 | 1,134 | 41.60 t/s | 44.95 t/s |
| 10 | 1,273 | 42.06 t/s | 46.15 t/s |

---

## Task #276 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:16:11.896` (Queue Delay: `0.40s`)
* **Total Context Footprint:** `684` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `379.76 t/s` (`2.63 ms/tok`) | Time To First Token (TTFT) = `1.44s` |
| **Decode Speed (Generation)** | `51.08 t/s` (`19.58 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `545` (79.7%) / Out: `139` (20.3%) | Total context footprint: `684` tokens |
| **Graphs Reused** | `394` | CUDA/execution graph cache hits |

---

## Task #419 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:16:16.691` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `478` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `164.76 t/s` (`6.07 ms/tok`) | Time To First Token (TTFT) = `1.59s` |
| **Decode Speed (Generation)** | `51.50 t/s` (`19.42 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `262` (54.8%) / Out: `216` (45.2%) | Total context footprint: `478` tokens |
| **Graphs Reused** | `607` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 156 | 51.63 t/s | 51.96 t/s |

---

## Task #638 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:16:29.991` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `1570` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `423.43 t/s` (`2.36 ms/tok`) | Time To First Token (TTFT) = `2.32s` |
| **Decode Speed (Generation)** | `50.41 t/s` (`19.84 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `981` (62.5%) / Out: `589` (37.5%) | Total context footprint: `1570` tokens |
| **Graphs Reused** | `1,192` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 156 | 51.64 t/s | 51.98 t/s |
| 2 | 305 | 50.53 t/s | 49.41 t/s |
| 3 | 457 | 50.52 t/s | 50.51 t/s |

---

## Task #1231 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:18:26.119` (Queue Delay: `1.54s`)
* **Total Context Footprint:** `796` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `398.85 t/s` (`2.51 ms/tok`) | Time To First Token (TTFT) = `1.41s` |
| **Decode Speed (Generation)** | `51.22 t/s` (`19.52 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `564` (70.9%) / Out: `232` (29.1%) | Total context footprint: `796` tokens |
| **Graphs Reused** | `1,421` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 154 | 50.94 t/s | 51.28 t/s |

---

## Task #1467 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:18:32.689` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `872` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `185.09 t/s` (`5.40 ms/tok`) | Time To First Token (TTFT) = `1.55s` |
| **Decode Speed (Generation)** | `51.02 t/s` (`19.60 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `287` (32.9%) / Out: `585` (67.1%) | Total context footprint: `872` tokens |
| **Graphs Reused** | `2,002` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 154 | 50.89 t/s | 51.22 t/s |
| 2 | 307 | 50.82 t/s | 50.76 t/s |
| 3 | 462 | 51.00 t/s | 51.37 t/s |

---

## Task #2055 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:19:37.929` (Queue Delay: `1.10s`)
* **Total Context Footprint:** `915` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `376.25 t/s` (`2.66 ms/tok`) | Time To First Token (TTFT) = `1.48s` |
| **Decode Speed (Generation)** | `50.83 t/s` (`19.67 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `555` (60.7%) / Out: `360` (39.3%) | Total context footprint: `915` tokens |
| **Graphs Reused** | `2,359` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 156 | 51.35 t/s | 51.68 t/s |
| 2 | 308 | 50.85 t/s | 50.35 t/s |

---

## Task #2419 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:19:47.125` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `553` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `169.98 t/s` (`5.88 ms/tok`) | Time To First Token (TTFT) = `1.59s` |
| **Decode Speed (Generation)** | `51.34 t/s` (`19.48 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `270` (48.8%) / Out: `283` (51.2%) | Total context footprint: `553` tokens |
| **Graphs Reused** | `2,639` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 156 | 51.47 t/s | 51.80 t/s |

---

## Task #2705 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:20:01.946` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `1328` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `435.18 t/s` (`2.30 ms/tok`) | Time To First Token (TTFT) = `2.38s` |
| **Decode Speed (Generation)** | `50.00 t/s` (`20.00 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1037` (78.1%) / Out: `291` (21.9%) | Total context footprint: `1328` tokens |
| **Graphs Reused** | `2,927` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 152 | 50.28 t/s | 50.61 t/s |

---

## Task #3000 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:20:17.956` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `1852` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `395.13 t/s` (`2.53 ms/tok`) | Time To First Token (TTFT) = `2.51s` |
| **Decode Speed (Generation)** | `49.64 t/s` (`20.15 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `993` (53.6%) / Out: `859` (46.4%) | Total context footprint: `1852` tokens |
| **Graphs Reused** | `3,781` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 154 | 50.87 t/s | 51.20 t/s |
| 2 | 303 | 50.13 t/s | 49.40 t/s |
| 3 | 452 | 49.90 t/s | 49.44 t/s |
| 4 | 601 | 49.82 t/s | 49.57 t/s |
| 5 | 749 | 49.66 t/s | 49.02 t/s |

---

## Task #3863 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:33:48.407` (Queue Delay: `2.31s`)
* **Total Context Footprint:** `11229` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `515.79 t/s` (`1.94 ms/tok`) | Time To First Token (TTFT) = `21.61s` |
| **Decode Speed (Generation)** | `45.54 t/s` (`21.96 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `11147` (99.3%) / Out: `82` (0.7%) | Total context footprint: `11229` tokens |
| **Graphs Reused** | `3,861` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 4,096 | 37.0% | 4.39 | 933.82 |
| 2 | 6,144 | 55.0% | 7.72 | 795.62 |
| 3 | 8,192 | 74.0% | 11.72 | 698.73 |
| 4 | 10,240 | 92.0% | 16.53 | 619.41 |
| 5 | 10,631 | 95.0% | 17.86 | 595.21 |
| 6 | 11,092 | 100.0% | 19.30 | 574.85 |
| 7 | 11,143 | 100.0% | 20.98 | 531.01 |

---

## Task #3954 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:34:12.331` (Queue Delay: `0.07s`)
* **Total Context Footprint:** `3516` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `286.80 t/s` (`3.49 ms/tok`) | Time To First Token (TTFT) = `10.46s` |
| **Decode Speed (Generation)** | `43.91 t/s` (`22.77 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `2999` (85.3%) / Out: `517` (14.7%) | Total context footprint: `3516` tokens |
| **Graphs Reused** | `4,374` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,050 | 93.0% | 4.98 | 411.72 |
| 2 | 2,483 | 96.0% | 6.53 | 380.20 |
| 3 | 2,995 | 100.0% | 8.30 | 360.66 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 134 | 44.31 t/s | 44.64 t/s |
| 2 | 266 | 44.09 t/s | 43.88 t/s |
| 3 | 397 | 43.94 t/s | 43.65 t/s |

---

## Task #4476 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:34:42.486` (Queue Delay: `7.48s`)
* **Total Context Footprint:** `2251` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `653.20 t/s` (`1.53 ms/tok`) | Time To First Token (TTFT) = `2.54s` |
| **Decode Speed (Generation)** | `50.67 t/s` (`19.73 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1660` (73.7%) / Out: `591` (26.3%) | Total context footprint: `2251` tokens |
| **Graphs Reused** | `4,961` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 154 | 50.69 t/s | 51.02 t/s |
| 2 | 307 | 50.73 t/s | 50.78 t/s |
| 3 | 459 | 50.65 t/s | 50.47 t/s |

---

## Task #5071 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:56:30.422` (Queue Delay: `1.53s`)
* **Total Context Footprint:** `11282` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `520.94 t/s` (`1.92 ms/tok`) | Time To First Token (TTFT) = `21.40s` |
| **Decode Speed (Generation)** | `45.78 t/s` (`21.84 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `11147` (98.8%) / Out: `135` (1.2%) | Total context footprint: `11282` tokens |
| **Graphs Reused** | `5,093` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 4,096 | 37.0% | 4.33 | 944.98 |
| 2 | 6,144 | 55.0% | 7.61 | 807.25 |
| 3 | 8,192 | 74.0% | 11.61 | 705.66 |
| 4 | 10,240 | 92.0% | 16.35 | 626.47 |
| 5 | 10,631 | 95.0% | 17.64 | 602.53 |
| 6 | 11,092 | 100.0% | 19.08 | 581.46 |
| 7 | 11,143 | 100.0% | 20.75 | 536.93 |

---

## Task #5215 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:56:55.745` (Queue Delay: `0.07s`)
* **Total Context Footprint:** `3806` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `291.25 t/s` (`3.43 ms/tok`) | Time To First Token (TTFT) = `10.29s` |
| **Decode Speed (Generation)** | `44.33 t/s` (`22.56 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `2997` (78.7%) / Out: `809` (21.3%) | Total context footprint: `3806` tokens |
| **Graphs Reused** | `5,897` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,050 | 93.0% | 4.93 | 415.81 |
| 2 | 2,481 | 96.0% | 6.49 | 382.44 |
| 3 | 2,993 | 100.0% | 8.21 | 364.44 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 135 | 44.61 t/s | 44.94 t/s |
| 2 | 268 | 44.40 t/s | 44.19 t/s |
| 3 | 401 | 44.36 t/s | 44.28 t/s |
| 4 | 535 | 44.40 t/s | 44.51 t/s |
| 5 | 667 | 44.31 t/s | 43.96 t/s |
| 6 | 801 | 44.33 t/s | 44.41 t/s |

---

## Task #6029 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 01:57:32.262` (Queue Delay: `7.74s`)
* **Total Context Footprint:** `1001` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `361.79 t/s` (`2.76 ms/tok`) | Time To First Token (TTFT) = `1.40s` |
| **Decode Speed (Generation)** | `49.26 t/s` (`20.30 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `507` (50.6%) / Out: `494` (49.4%) | Total context footprint: `1001` tokens |
| **Graphs Reused** | `6,387` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 150 | 49.43 t/s | 49.77 t/s |
| 2 | 297 | 49.14 t/s | 48.84 t/s |
| 3 | 445 | 49.20 t/s | 49.31 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:06:57.688` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `958` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `334.17 t/s` (`2.99 ms/tok`) | Time To First Token (TTFT) = `2.15s` |
| **Decode Speed (Generation)** | `65.86 t/s` (`15.18 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `719` (75.1%) / Out: `239` (24.9%) | Total context footprint: `958` tokens |
| **Graphs Reused** | `237` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 199 | 65.69 t/s | 66.02 t/s |

---

## Task #241 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:05.651` (Queue Delay: `2.13s`)
* **Total Context Footprint:** `780` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `347.70 t/s` (`2.88 ms/tok`) | Time To First Token (TTFT) = `1.69s` |
| **Decode Speed (Generation)** | `66.84 t/s` (`14.96 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `586` (75.1%) / Out: `194` (24.9%) | Total context footprint: `780` tokens |
| **Graphs Reused** | `428` | CUDA/execution graph cache hits |

---

## Task #436 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:12.287` (Queue Delay: `1.98s`)
* **Total Context Footprint:** `71` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `249.81 t/s` (`4.00 ms/tok`) | Time To First Token (TTFT) = `0.26s` |
| **Decode Speed (Generation)** | `69.14 t/s` (`14.46 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `64` (90.1%) / Out: `7` (9.9%) | Total context footprint: `71` tokens |
| **Graphs Reused** | `433` | CUDA/execution graph cache hits |

---

## Task #444 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:12.928` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `290` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `385.98 t/s` (`2.59 ms/tok`) | Time To First Token (TTFT) = `0.53s` |
| **Decode Speed (Generation)** | `69.79 t/s` (`14.33 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `206` (71.0%) / Out: `84` (29.0%) | Total context footprint: `290` tokens |
| **Graphs Reused** | `515` | CUDA/execution graph cache hits |

---

## Task #529 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:15.798` (Queue Delay: `0.66s`)
* **Total Context Footprint:** `325` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `588.71 t/s` (`1.70 ms/tok`) | Time To First Token (TTFT) = `0.31s` |
| **Decode Speed (Generation)** | `67.96 t/s` (`14.72 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `181` (55.7%) / Out: `144` (44.3%) | Total context footprint: `325` tokens |
| **Graphs Reused** | `657` | CUDA/execution graph cache hits |

---

## Task #674 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:19.457` (Queue Delay: `0.75s`)
* **Total Context Footprint:** `324` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `584.91 t/s` (`1.71 ms/tok`) | Time To First Token (TTFT) = `0.31s` |
| **Decode Speed (Generation)** | `70.76 t/s` (`14.13 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `181` (55.9%) / Out: `143` (44.1%) | Total context footprint: `324` tokens |
| **Graphs Reused** | `798` | CUDA/execution graph cache hits |

---

## Task #818 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:22.748` (Queue Delay: `0.69s`)
* **Total Context Footprint:** `127` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `490.35 t/s` (`2.04 ms/tok`) | Time To First Token (TTFT) = `0.22s` |
| **Decode Speed (Generation)** | `58.38 t/s` (`17.13 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `106` (83.5%) / Out: `21` (16.5%) | Total context footprint: `127` tokens |
| **Graphs Reused** | `816` | CUDA/execution graph cache hits |

---

## Task #840 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:23.406` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `862` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `294.46 t/s` (`3.40 ms/tok`) | Time To First Token (TTFT) = `2.57s` |
| **Decode Speed (Generation)** | `66.47 t/s` (`15.04 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `756` (87.7%) / Out: `106` (12.3%) | Total context footprint: `862` tokens |
| **Graphs Reused** | `920` | CUDA/execution graph cache hits |

---

## Task #947 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:29.945` (Queue Delay: `2.20s`)
* **Total Context Footprint:** `853` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `318.34 t/s` (`3.14 ms/tok`) | Time To First Token (TTFT) = `2.37s` |
| **Decode Speed (Generation)** | `66.22 t/s` (`15.10 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `756` (88.6%) / Out: `97` (11.4%) | Total context footprint: `853` tokens |
| **Graphs Reused** | `1,015` | CUDA/execution graph cache hits |

---

## Task #1045 (Slot 0)

* **Model:** `Qwen3-VL-4B-Instruct-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:36.225` (Queue Delay: `2.16s`)
* **Total Context Footprint:** `305` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `561.62 t/s` (`1.78 ms/tok`) | Time To First Token (TTFT) = `0.37s` |
| **Decode Speed (Generation)** | `67.03 t/s` (`14.92 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `206` (67.5%) / Out: `99` (32.5%) | Total context footprint: `305` tokens |
| **Graphs Reused** | `1,112` | CUDA/execution graph cache hits |

---

## Task #6525 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:42.370` (Queue Delay: `1.53s`)
* **Total Context Footprint:** `599` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `192.18 t/s` (`5.20 ms/tok`) | Time To First Token (TTFT) = `2.69s` |
| **Decode Speed (Generation)** | `46.31 t/s` (`21.60 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `517` (86.3%) / Out: `82` (13.7%) | Total context footprint: `599` tokens |
| **Graphs Reused** | `6,467` | CUDA/execution graph cache hits |

---

## Task #6611 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 02:07:47.314` (Queue Delay: `0.07s`)
* **Total Context Footprint:** `3764` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `289.24 t/s` (`3.46 ms/tok`) | Time To First Token (TTFT) = `10.56s` |
| **Decode Speed (Generation)** | `45.05 t/s` (`22.20 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `3054` (81.1%) / Out: `710` (18.9%) | Total context footprint: `3764` tokens |
| **Graphs Reused** | `7,172` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,050 | 93.0% | 4.91 | 417.80 |
| 2 | 2,538 | 96.0% | 6.47 | 392.57 |
| 3 | 3,050 | 100.0% | 8.46 | 360.45 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 137 | 45.08 t/s | 45.41 t/s |
| 2 | 272 | 45.00 t/s | 44.92 t/s |
| 3 | 408 | 45.03 t/s | 45.09 t/s |
| 4 | 544 | 45.04 t/s | 45.06 t/s |
| 5 | 680 | 45.04 t/s | 45.06 t/s |

---

## Task #7326 (Slot 0)

* **Model:** `DeepSeek-R1-Distill-Qwen-7B-Hybrid`
* **Dispatch Time:** `2026-09-11 02:08:21.626` (Queue Delay: `7.72s`)
* **Total Context Footprint:** `924` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `266.28 t/s` (`3.76 ms/tok`) | Time To First Token (TTFT) = `0.58s` |
| **Decode Speed (Generation)** | `50.94 t/s` (`19.63 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `525` (56.8%) / Out: `399` (43.2%) | Total context footprint: `924` tokens |
| **Graphs Reused** | `7,567` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 154 | 50.83 t/s | 51.16 t/s |
| 2 | 307 | 50.87 t/s | 50.92 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 12:10:10.220` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `416` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `388.05 t/s` (`2.58 ms/tok`) | Time To First Token (TTFT) = `0.26s` |
| **Decode Speed (Generation)** | `54.26 t/s` (`18.43 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `101` (24.3%) / Out: `315` (75.7%) | Total context footprint: `416` tokens |
| **Graphs Reused** | `313` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 165 | 54.50 t/s | 54.84 t/s |

---

## Task #318 (Slot 0)

* **Model:** `Gemma-4-E4B-it-GGUF`
* **Dispatch Time:** `2026-09-11 12:19:25.601` (Queue Delay: `0.43s`)
* **Total Context Footprint:** `518` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `492.84 t/s` (`2.03 ms/tok`) | Time To First Token (TTFT) = `0.34s` |
| **Decode Speed (Generation)** | `52.74 t/s` (`18.96 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `168` (32.4%) / Out: `350` (67.6%) | Total context footprint: `518` tokens |
| **Graphs Reused** | `659` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 161 | 53.13 t/s | 53.47 t/s |
| 2 | 319 | 52.84 t/s | 52.54 t/s |

---

## Task #671 (Slot 0)

* **Model:** `DeepSeek-R1-Distill-Qwen-7B-Hybrid`
* **Dispatch Time:** `2026-09-11 12:21:09.192` (Queue Delay: `0.55s`)
* **Total Context Footprint:** `643` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `538.76 t/s` (`1.86 ms/tok`) | Time To First Token (TTFT) = `0.77s` |
| **Decode Speed (Generation)** | `52.23 t/s` (`19.15 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `242` (37.6%) / Out: `401` (62.4%) | Total context footprint: `643` tokens |
| **Graphs Reused** | `1,056` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 161 | 53.03 t/s | 53.36 t/s |
| 2 | 317 | 52.43 t/s | 51.84 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:43:13.415` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 32.0% | 7.45 | 274.90 |
| 2 | 4,096 | 64.0% | 19.02 | 215.30 |
| 3 | 5,851 | 92.0% | 32.38 | 180.72 |
| 4 | 6,238 | 98.0% | 35.70 | 174.74 |
| 5 | 6,352 | 100.0% | 40.00 | 158.79 |
| 6 | 6,363 | 100.0% | 42.29 | 150.47 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 16.39 t/s | 16.56 t/s |
| 2 | 145 | 15.79 t/s | 14.61 t/s |
| 3 | 195 | 15.92 t/s | 16.32 t/s |
| 4 | 250 | 16.29 t/s | 17.71 t/s |
| 5 | 301 | 16.31 t/s | 16.44 t/s |
| 6 | 350 | 16.24 t/s | 15.79 t/s |
| 7 | 404 | 16.42 t/s | 17.67 t/s |
| 8 | 450 | 16.24 t/s | 14.88 t/s |
| 9 | 495 | 16.07 t/s | 14.51 t/s |
| 10 | 552 | 16.28 t/s | 18.37 t/s |
| 11 | 587 | 15.86 t/s | 11.25 t/s |
| 12 | 633 | 15.79 t/s | 15.00 t/s |
| 13 | 676 | 15.65 t/s | 13.80 t/s |
| 14 | 723 | 15.61 t/s | 15.06 t/s |
| 15 | 773 | 15.65 t/s | 16.27 t/s |
| 16 | 811 | 15.44 t/s | 12.18 t/s |
| 17 | 877 | 15.77 t/s | 21.42 t/s |
| 18 | 923 | 15.73 t/s | 14.95 t/s |
| 19 | 986 | 15.95 t/s | 20.05 t/s |
| 20 | 1,034 | 15.93 t/s | 15.57 t/s |
| 21 | 1,093 | 16.07 t/s | 18.97 t/s |
| 22 | 1,154 | 16.22 t/s | 19.44 t/s |
| 23 | 1,208 | 16.27 t/s | 17.53 t/s |
| 24 | 1,271 | 16.43 t/s | 20.15 t/s |

---

## Task #547 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:45:52.205` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `294` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `2.72 t/s` (`367.87 ms/tok`) | Time To First Token (TTFT) = `1.47s` |
| **Decode Speed (Generation)** | `17.61 t/s` (`56.78 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `4` (1.4%) / Out: `290` (98.6%) | Total context footprint: `294` tokens |
| **Speculative MTP Acceptance** | `51.30%` (`177/345`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.54` tokens/step | Effective speedup: ~`2.54x` vs single-token decode |
| **Graphs Reused** | `645` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 102 | 16.22 t/s | 16.38 t/s |
| 2 | 158 | 16.86 t/s | 18.17 t/s |
| 3 | 214 | 17.12 t/s | 17.86 t/s |
| 4 | 274 | 17.59 t/s | 19.48 t/s |

---

## Task #664 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:46:14.871` (Queue Delay: `4.49s`)
* **Total Context Footprint:** `2030` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `121.02 t/s` (`8.26 ms/tok`) | Time To First Token (TTFT) = `3.12s` |
| **Decode Speed (Generation)** | `21.90 t/s` (`45.67 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `377` (18.6%) / Out: `1653` (81.4%) | Total context footprint: `2030` tokens |
| **Speculative MTP Acceptance** | `64.65%` (`1092/1689`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.94` tokens/step | Effective speedup: ~`2.94x` vs single-token decode |
| **Graphs Reused** | `1,201` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 25.80 t/s | 26.06 t/s |
| 2 | 153 | 22.07 t/s | 17.37 t/s |
| 3 | 225 | 22.44 t/s | 23.29 t/s |
| 4 | 289 | 22.05 t/s | 20.78 t/s |
| 5 | 351 | 21.73 t/s | 20.35 t/s |
| 6 | 410 | 21.34 t/s | 19.29 t/s |
| 7 | 478 | 21.47 t/s | 22.27 t/s |
| 8 | 532 | 20.96 t/s | 17.37 t/s |
| 9 | 601 | 21.10 t/s | 22.19 t/s |
| 10 | 682 | 21.59 t/s | 26.15 t/s |
| 11 | 751 | 21.65 t/s | 22.27 t/s |
| 12 | 819 | 21.69 t/s | 22.12 t/s |
| 13 | 885 | 21.65 t/s | 21.09 t/s |
| 14 | 959 | 21.85 t/s | 24.54 t/s |
| 15 | 1,015 | 21.61 t/s | 18.21 t/s |
| 16 | 1,061 | 21.23 t/s | 15.32 t/s |
| 17 | 1,137 | 21.42 t/s | 24.47 t/s |
| 18 | 1,200 | 21.36 t/s | 20.33 t/s |
| 19 | 1,257 | 21.19 t/s | 18.23 t/s |
| 20 | 1,334 | 21.38 t/s | 24.95 t/s |
| 21 | 1,409 | 21.51 t/s | 24.15 t/s |
| 22 | 1,482 | 21.59 t/s | 23.30 t/s |
| 23 | 1,558 | 21.75 t/s | 25.30 t/s |
| 24 | 1,632 | 21.86 t/s | 24.41 t/s |

---

## Task #1230 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:47:49.921` (Queue Delay: `2.28s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 41 | 100.0% | 3.03 | 13.51 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 16.39 t/s | 16.56 t/s |
| 2 | 133 | 14.51 t/s | 10.78 t/s |
| 3 | 174 | 14.28 t/s | 13.59 t/s |
| 4 | 222 | 14.55 t/s | 15.60 t/s |
| 5 | 267 | 14.59 t/s | 14.82 t/s |
| 6 | 314 | 14.69 t/s | 15.24 t/s |
| 7 | 368 | 15.07 t/s | 17.78 t/s |
| 8 | 415 | 15.09 t/s | 15.22 t/s |
| 9 | 460 | 15.03 t/s | 14.55 t/s |
| 10 | 510 | 15.15 t/s | 16.28 t/s |
| 11 | 551 | 14.98 t/s | 13.18 t/s |
| 12 | 599 | 15.03 t/s | 15.66 t/s |
| 13 | 643 | 14.97 t/s | 14.09 t/s |
| 14 | 697 | 15.12 t/s | 17.23 t/s |
| 15 | 752 | 15.29 t/s | 17.79 t/s |
| 16 | 795 | 15.22 t/s | 14.20 t/s |
| 17 | 841 | 15.20 t/s | 14.81 t/s |
| 18 | 892 | 15.29 t/s | 16.99 t/s |
| 19 | 936 | 15.25 t/s | 14.47 t/s |
| 20 | 991 | 15.36 t/s | 17.56 t/s |
| 21 | 1,050 | 15.54 t/s | 19.36 t/s |
| 22 | 1,105 | 15.66 t/s | 18.32 t/s |
| 23 | 1,149 | 15.62 t/s | 14.57 t/s |
| 24 | 1,200 | 15.64 t/s | 16.22 t/s |
| 25 | 1,253 | 15.70 t/s | 17.05 t/s |
| 26 | 1,293 | 15.61 t/s | 13.28 t/s |
| 27 | 1,343 | 15.63 t/s | 16.14 t/s |
| 28 | 1,395 | 15.66 t/s | 16.63 t/s |
| 29 | 1,439 | 15.63 t/s | 14.66 t/s |
| 30 | 1,502 | 15.79 t/s | 20.35 t/s |
| 31 | 1,558 | 15.87 t/s | 18.59 t/s |
| 32 | 1,598 | 15.78 t/s | 12.86 t/s |
| 33 | 1,649 | 15.80 t/s | 16.40 t/s |
| 34 | 1,693 | 15.76 t/s | 14.65 t/s |
| 35 | 1,755 | 15.88 t/s | 19.95 t/s |
| 36 | 1,810 | 15.95 t/s | 18.30 t/s |
| 37 | 1,854 | 15.90 t/s | 14.06 t/s |
| 38 | 1,904 | 15.90 t/s | 16.22 t/s |
| 39 | 1,958 | 15.94 t/s | 17.19 t/s |
| 40 | 2,025 | 16.08 t/s | 21.66 t/s |
| 41 | 2,068 | 16.04 t/s | 14.33 t/s |
| 42 | 2,131 | 16.15 t/s | 20.73 t/s |
| 43 | 2,186 | 16.19 t/s | 18.31 t/s |
| 44 | 2,237 | 16.21 t/s | 16.96 t/s |
| 45 | 2,301 | 16.30 t/s | 20.49 t/s |
| 46 | 2,356 | 16.34 t/s | 18.21 t/s |
| 47 | 2,402 | 16.32 t/s | 15.27 t/s |
| 48 | 2,467 | 16.42 t/s | 20.75 t/s |
| 49 | 2,519 | 16.43 t/s | 17.31 t/s |
| 50 | 2,572 | 16.44 t/s | 16.98 t/s |
| 51 | 2,637 | 16.53 t/s | 20.64 t/s |
| 52 | 2,689 | 16.54 t/s | 17.16 t/s |
| 53 | 2,754 | 16.63 t/s | 21.53 t/s |
| 54 | 2,799 | 16.59 t/s | 14.40 t/s |
| 55 | 2,866 | 16.67 t/s | 20.97 t/s |
| 56 | 2,928 | 16.72 t/s | 19.75 t/s |
| 57 | 2,996 | 16.82 t/s | 22.30 t/s |
| 58 | 3,062 | 16.91 t/s | 21.99 t/s |
| 59 | 3,116 | 16.92 t/s | 17.63 t/s |
| 60 | 3,176 | 16.96 t/s | 19.70 t/s |
| 61 | 3,231 | 16.97 t/s | 17.54 t/s |
| 62 | 3,298 | 17.05 t/s | 21.86 t/s |
| 63 | 3,363 | 17.12 t/s | 21.25 t/s |

---

## Task #3 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:51:20.746` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 102 | 20.80 t/s | 21.01 t/s |
| 2 | 175 | 22.04 t/s | 24.04 t/s |
| 3 | 234 | 21.37 t/s | 19.62 t/s |
| 4 | 293 | 20.99 t/s | 19.61 t/s |
| 5 | 363 | 21.39 t/s | 23.21 t/s |
| 6 | 418 | 20.87 t/s | 17.99 t/s |
| 7 | 484 | 21.00 t/s | 21.88 t/s |
| 8 | 551 | 21.10 t/s | 21.85 t/s |
| 9 | 616 | 21.11 t/s | 21.21 t/s |
| 10 | 669 | 20.78 t/s | 17.59 t/s |
| 11 | 730 | 20.70 t/s | 19.84 t/s |
| 12 | 782 | 20.42 t/s | 17.20 t/s |
| 13 | 830 | 20.09 t/s | 15.83 t/s |
| 14 | 902 | 20.31 t/s | 23.29 t/s |
| 15 | 964 | 20.32 t/s | 20.49 t/s |
| 16 | 1,027 | 20.34 t/s | 20.57 t/s |
| 17 | 1,074 | 20.06 t/s | 15.50 t/s |
| 18 | 1,124 | 19.87 t/s | 16.42 t/s |
| 19 | 1,192 | 19.97 t/s | 21.94 t/s |
| 20 | 1,246 | 19.86 t/s | 17.73 t/s |
| 21 | 1,306 | 19.84 t/s | 19.31 t/s |
| 22 | 1,361 | 19.76 t/s | 18.10 t/s |
| 23 | 1,427 | 19.83 t/s | 21.30 t/s |
| 24 | 1,478 | 19.69 t/s | 16.54 t/s |
| 25 | 1,540 | 19.71 t/s | 20.12 t/s |
| 26 | 1,604 | 19.75 t/s | 20.76 t/s |
| 27 | 1,658 | 19.66 t/s | 17.33 t/s |
| 28 | 1,717 | 19.64 t/s | 19.22 t/s |
| 29 | 1,780 | 19.67 t/s | 20.36 t/s |
| 30 | 1,835 | 19.61 t/s | 17.97 t/s |
| 31 | 1,897 | 19.63 t/s | 20.09 t/s |
| 32 | 1,954 | 19.58 t/s | 18.23 t/s |
| 33 | 2,013 | 19.57 t/s | 19.20 t/s |
| 34 | 2,076 | 19.61 t/s | 20.95 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:55:48.236` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `1180` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `283.53 t/s` (`3.53 ms/tok`) | Time To First Token (TTFT) = `0.97s` |
| **Decode Speed (Generation)** | `86.72 t/s` (`11.53 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `275` (23.3%) / Out: `905` (76.7%) | Total context footprint: `1180` tokens |
| **Speculative MTP Acceptance** | `74.29%` (`624/840`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.23` tokens/step | Effective speedup: ~`3.23x` vs single-token decode |
| **Graphs Reused** | `277` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 266 | 87.32 t/s | 87.65 t/s |
| 2 | 523 | 86.02 t/s | 84.71 t/s |
| 3 | 779 | 85.75 t/s | 85.19 t/s |

---

## Task #2 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:56:00.352` (Queue Delay: `12.10s`)
* **Total Context Footprint:** `11656` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `116.50 t/s` (`8.58 ms/tok`) | Time To First Token (TTFT) = `89.53s` |
| **Decode Speed (Generation)** | `61.34 t/s` (`16.30 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `10430` (89.5%) / Out: `1226` (10.5%) | Total context footprint: `11656` tokens |
| **Speculative MTP Acceptance** | `54.29%` (`759/1398`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.63` tokens/step | Effective speedup: ~`2.63x` vs single-token decode |
| **Graphs Reused** | `737` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 4,096 | 39.0% | 5.16 | 793.73 |
| 2 | 6,144 | 59.0% | 9.14 | 672.32 |
| 3 | 6,238 | 60.0% | 10.41 | 599.20 |
| 4 | 6,341 | 61.0% | 11.37 | 557.84 |
| 5 | 10,426 | 100.0% | 88.87 | 117.32 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 188 | 61.67 t/s | 62.00 t/s |
| 2 | 371 | 60.99 t/s | 60.31 t/s |
| 3 | 559 | 61.29 t/s | 61.90 t/s |
| 4 | 736 | 60.65 t/s | 58.70 t/s |
| 5 | 939 | 61.92 t/s | 67.02 t/s |
| 6 | 1,123 | 61.74 t/s | 60.81 t/s |

---

## Task #757 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:57:53.336` (Queue Delay: `3.45s`)
* **Total Context Footprint:** `2361` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `313.42 t/s` (`3.19 ms/tok`) | Time To First Token (TTFT) = `1.83s` |
| **Decode Speed (Generation)** | `86.06 t/s` (`11.62 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `575` (24.4%) / Out: `1786` (75.6%) | Total context footprint: `2361` tokens |
| **Speculative MTP Acceptance** | `74.83%` (`1237/1653`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.25` tokens/step | Effective speedup: ~`3.25x` vs single-token decode |
| **Graphs Reused** | `1,280` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 266 | 87.43 t/s | 87.76 t/s |
| 2 | 486 | 80.21 t/s | 72.96 t/s |
| 3 | 711 | 78.37 t/s | 74.67 t/s |
| 4 | 968 | 80.08 t/s | 85.23 t/s |
| 5 | 1,248 | 82.65 t/s | 92.95 t/s |
| 6 | 1,534 | 84.62 t/s | 94.40 t/s |

---

## Task #1312 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 20:58:17.038` (Queue Delay: `1.11s`)
* **Total Context Footprint:** `2296` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `201.22 t/s` (`4.97 ms/tok`) | Time To First Token (TTFT) = `2.59s` |
| **Decode Speed (Generation)** | `77.34 t/s` (`12.93 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `521` (22.7%) / Out: `1775` (77.3%) | Total context footprint: `2296` tokens |
| **Speculative MTP Acceptance** | `64.30%` (`1169/1818`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.93` tokens/step | Effective speedup: ~`2.93x` vs single-token decode |
| **Graphs Reused** | `1,879` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 248 | 81.64 t/s | 81.97 t/s |
| 2 | 457 | 75.46 t/s | 69.27 t/s |
| 3 | 698 | 76.97 t/s | 80.00 t/s |
| 4 | 924 | 76.37 t/s | 74.59 t/s |
| 5 | 1,156 | 76.43 t/s | 76.65 t/s |
| 6 | 1,392 | 76.72 t/s | 78.15 t/s |
| 7 | 1,627 | 76.86 t/s | 77.69 t/s |

---

## Task #1922 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:17:45.909` (Queue Delay: `1.08s`)
* **Total Context Footprint:** `13196` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `437.78 t/s` (`2.28 ms/tok`) | Time To First Token (TTFT) = `29.04s` |
| **Decode Speed (Generation)** | `65.28 t/s` (`15.32 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `12711` (96.3%) / Out: `485` (3.7%) | Total context footprint: `13196` tokens |
| **Speculative MTP Acceptance** | `63.85%` (`318/498`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.92` tokens/step | Effective speedup: ~`2.92x` vs single-token decode |
| **Graphs Reused** | `2,042` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 4,096 | 32.0% | 4.98 | 821.84 |
| 2 | 6,144 | 48.0% | 8.73 | 703.98 |
| 3 | 8,192 | 64.0% | 13.25 | 618.49 |
| 4 | 10,240 | 81.0% | 18.43 | 555.56 |
| 5 | 12,195 | 96.0% | 24.28 | 502.19 |
| 6 | 12,707 | 100.0% | 26.62 | 477.41 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 190 | 62.30 t/s | 62.63 t/s |
| 2 | 395 | 65.14 t/s | 67.98 t/s |

---

## Task #1923 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:18:26.366` (Queue Delay: `N/A`)
* **Total Context Footprint:** `19561` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `294.97 t/s` (`3.39 ms/tok`) | Time To First Token (TTFT) = `42.25s` |
| **Decode Speed (Generation)** | `51.41 t/s` (`19.45 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `12462` (63.7%) / Out: `7099` (36.3%) | Total context footprint: `19561` tokens |
| **Speculative MTP Acceptance** | `55.68%` (`4440/7974`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.67` tokens/step | Effective speedup: ~`2.67x` vs single-token decode |
| **Graphs Reused** | `4,672` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 44.0% | 3.86 | 530.07 |
| 2 | 4,096 | 55.0% | 9.02 | 453.99 |
| 3 | 6,144 | 66.0% | 15.00 | 409.71 |
| 4 | 8,192 | 77.0% | 21.70 | 377.44 |
| 5 | 10,240 | 88.0% | 29.06 | 352.40 |
| 6 | 11,946 | 97.0% | 37.20 | 321.15 |
| 7 | 12,458 | 100.0% | 39.31 | 316.89 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 145 | 47.45 t/s | 47.78 t/s |
| 2 | 297 | 48.84 t/s | 50.24 t/s |
| 3 | 454 | 49.84 t/s | 51.84 t/s |
| 4 | 609 | 50.24 t/s | 51.43 t/s |
| 5 | 751 | 49.63 t/s | 47.21 t/s |
| 6 | 911 | 50.13 t/s | 52.61 t/s |
| 7 | 1,074 | 50.65 t/s | 53.75 t/s |
| 8 | 1,218 | 50.28 t/s | 47.69 t/s |
| 9 | 1,368 | 50.21 t/s | 49.67 t/s |
| 10 | 1,538 | 50.77 t/s | 55.79 t/s |
| 11 | 1,698 | 51.00 t/s | 53.26 t/s |
| 12 | 1,857 | 51.12 t/s | 52.39 t/s |
| 13 | 2,027 | 51.53 t/s | 56.60 t/s |
| 14 | 2,200 | 51.95 t/s | 57.38 t/s |
| 15 | 2,346 | 51.69 t/s | 48.03 t/s |
| 16 | 2,494 | 51.51 t/s | 48.78 t/s |
| 17 | 2,648 | 51.46 t/s | 50.66 t/s |
| 18 | 2,787 | 51.10 t/s | 45.12 t/s |
| 19 | 2,927 | 50.85 t/s | 46.45 t/s |
| 20 | 3,077 | 50.78 t/s | 49.37 t/s |
| 21 | 3,219 | 50.59 t/s | 46.89 t/s |
| 22 | 3,359 | 50.39 t/s | 46.03 t/s |
| 23 | 3,524 | 50.56 t/s | 54.31 t/s |
| 24 | 3,653 | 50.22 t/s | 42.51 t/s |
| 25 | 3,804 | 50.23 t/s | 50.33 t/s |
| 26 | 3,971 | 50.40 t/s | 54.78 t/s |
| 27 | 4,125 | 50.43 t/s | 51.27 t/s |
| 28 | 4,255 | 50.17 t/s | 43.01 t/s |
| 29 | 4,398 | 50.07 t/s | 47.32 t/s |
| 30 | 4,535 | 49.91 t/s | 45.11 t/s |
| 31 | 4,682 | 49.86 t/s | 48.54 t/s |
| 32 | 4,821 | 49.74 t/s | 46.09 t/s |
| 33 | 4,988 | 49.90 t/s | 54.93 t/s |
| 34 | 5,171 | 50.20 t/s | 60.02 t/s |
| 35 | 5,337 | 50.33 t/s | 54.88 t/s |
| 36 | 5,489 | 50.33 t/s | 50.27 t/s |
| 37 | 5,637 | 50.29 t/s | 48.79 t/s |
| 38 | 5,802 | 50.41 t/s | 54.86 t/s |
| 39 | 5,997 | 50.77 t/s | 64.22 t/s |
| 40 | 6,181 | 51.02 t/s | 60.74 t/s |
| 41 | 6,340 | 51.06 t/s | 52.66 t/s |
| 42 | 6,526 | 51.31 t/s | 61.76 t/s |
| 43 | 6,699 | 51.44 t/s | 57.04 t/s |
| 44 | 6,862 | 51.49 t/s | 53.41 t/s |
| 45 | 7,019 | 51.50 t/s | 51.97 t/s |

---

## Task #4764 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:21:33.701` (Queue Delay: `6.97s`)
* **Total Context Footprint:** `15221` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `418.97 t/s` (`2.39 ms/tok`) | Time To First Token (TTFT) = `32.22s` |
| **Decode Speed (Generation)** | `62.52 t/s` (`15.99 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `13499` (88.7%) / Out: `1722` (11.3%) | Total context footprint: `15221` tokens |
| **Speculative MTP Acceptance** | `62.29%` (`1123/1803`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.87` tokens/step | Effective speedup: ~`2.87x` vs single-token decode |
| **Graphs Reused** | `5,265` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 4,096 | 30.0% | 5.21 | 786.77 |
| 2 | 6,144 | 46.0% | 9.06 | 678.43 |
| 3 | 8,192 | 61.0% | 13.63 | 601.17 |
| 4 | 10,240 | 76.0% | 18.83 | 543.88 |
| 5 | 12,288 | 91.0% | 24.73 | 496.96 |
| 6 | 12,983 | 96.0% | 28.21 | 460.18 |
| 7 | 13,495 | 100.0% | 29.80 | 452.79 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 196 | 64.79 t/s | 65.12 t/s |
| 2 | 356 | 58.66 t/s | 52.59 t/s |
| 3 | 525 | 57.66 t/s | 55.66 t/s |
| 4 | 706 | 58.11 t/s | 59.47 t/s |
| 5 | 893 | 58.86 t/s | 61.84 t/s |
| 6 | 1,074 | 59.03 t/s | 59.88 t/s |
| 7 | 1,270 | 59.79 t/s | 64.38 t/s |
| 8 | 1,476 | 60.86 t/s | 68.39 t/s |
| 9 | 1,701 | 62.42 t/s | 74.95 t/s |

---

## Task #5152 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:22:37.994` (Queue Delay: `4.52s`)
* **Total Context Footprint:** `3519` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `132.67 t/s` (`7.54 ms/tok`) | Time To First Token (TTFT) = `6.26s` |
| **Decode Speed (Generation)** | `54.99 t/s` (`18.19 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `831` (23.6%) / Out: `2688` (76.4%) | Total context footprint: `3519` tokens |
| **Speculative MTP Acceptance** | `60.46%` (`1734/2868`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.81` tokens/step | Effective speedup: ~`2.81x` vs single-token decode |
| **Graphs Reused** | `6,210` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 827 | 100.0% | 5.23 | 158.19 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 190 | 62.85 t/s | 63.18 t/s |
| 2 | 377 | 62.26 t/s | 61.69 t/s |
| 3 | 542 | 59.58 t/s | 54.25 t/s |
| 4 | 729 | 60.22 t/s | 62.14 t/s |
| 5 | 900 | 59.42 t/s | 56.27 t/s |
| 6 | 1,070 | 58.82 t/s | 55.80 t/s |
| 7 | 1,278 | 60.30 t/s | 69.28 t/s |
| 8 | 1,428 | 59.01 t/s | 49.90 t/s |
| 9 | 1,588 | 58.32 t/s | 52.82 t/s |
| 10 | 1,743 | 57.60 t/s | 51.11 t/s |
| 11 | 1,911 | 57.40 t/s | 55.40 t/s |
| 12 | 2,077 | 57.19 t/s | 54.93 t/s |
| 13 | 2,233 | 56.73 t/s | 51.18 t/s |
| 14 | 2,400 | 56.64 t/s | 55.47 t/s |
| 15 | 2,530 | 55.71 t/s | 42.75 t/s |
| 16 | 2,672 | 55.11 t/s | 46.35 t/s |

---

## Task #5376 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:23:39.156` (Queue Delay: `5.99s`)
* **Total Context Footprint:** `15400` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `417.33 t/s` (`2.40 ms/tok`) | Time To First Token (TTFT) = `32.22s` |
| **Decode Speed (Generation)** | `65.41 t/s` (`15.29 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `13445` (87.3%) / Out: `1955` (12.7%) | Total context footprint: `15400` tokens |
| **Speculative MTP Acceptance** | `67.23%` (`1307/1944`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.02` tokens/step | Effective speedup: ~`3.02x` vs single-token decode |
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
* **Dispatch Time:** `2026-09-11 21:24:45.730` (Queue Delay: `N/A`)
* **Total Context Footprint:** `3033` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `225.04 t/s` (`4.44 ms/tok`) | Time To First Token (TTFT) = `6.47s` |
| **Decode Speed (Generation)** | `61.96 t/s` (`16.14 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1456` (48.0%) / Out: `1577` (52.0%) | Total context footprint: `3033` tokens |
| **Speculative MTP Acceptance** | `63.36%` (`1034/1632`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.90` tokens/step | Effective speedup: ~`2.90x` vs single-token decode |
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

## Task #7542 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:26:44.933` (Queue Delay: `4.57s`)
* **Total Context Footprint:** `6881` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `139.76 t/s` (`7.16 ms/tok`) | Time To First Token (TTFT) = `6.80s` |
| **Decode Speed (Generation)** | `51.43 t/s` (`19.45 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `951` (13.8%) / Out: `5930` (86.2%) | Total context footprint: `6881` tokens |
| **Speculative MTP Acceptance** | `55.75%` (`3711/6657`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.67` tokens/step | Effective speedup: ~`2.67x` vs single-token decode |
| **Graphs Reused** | `9,580` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 947 | 100.0% | 5.78 | 163.75 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 142 | 46.34 t/s | 46.67 t/s |
| 2 | 286 | 47.07 t/s | 47.81 t/s |
| 3 | 456 | 50.16 t/s | 56.35 t/s |
| 4 | 627 | 51.77 t/s | 56.60 t/s |
| 5 | 811 | 53.55 t/s | 60.67 t/s |
| 6 | 991 | 54.61 t/s | 59.92 t/s |
| 7 | 1,142 | 53.91 t/s | 49.74 t/s |
| 8 | 1,310 | 54.10 t/s | 55.47 t/s |
| 9 | 1,450 | 53.27 t/s | 46.58 t/s |
| 10 | 1,582 | 52.25 t/s | 43.13 t/s |
| 11 | 1,737 | 52.15 t/s | 51.15 t/s |
| 12 | 1,880 | 51.75 t/s | 47.40 t/s |
| 13 | 2,018 | 51.25 t/s | 45.29 t/s |
| 14 | 2,171 | 51.20 t/s | 50.51 t/s |
| 15 | 2,299 | 50.59 t/s | 42.09 t/s |
| 16 | 2,485 | 51.25 t/s | 61.21 t/s |
| 17 | 2,661 | 51.67 t/s | 58.28 t/s |
| 18 | 2,826 | 51.81 t/s | 54.31 t/s |
| 19 | 2,975 | 51.68 t/s | 49.26 t/s |
| 20 | 3,147 | 51.89 t/s | 55.75 t/s |
| 21 | 3,273 | 51.39 t/s | 41.54 t/s |
| 22 | 3,415 | 51.21 t/s | 47.22 t/s |
| 23 | 3,598 | 51.60 t/s | 60.24 t/s |
| 24 | 3,744 | 51.46 t/s | 48.29 t/s |
| 25 | 3,892 | 51.36 t/s | 48.89 t/s |
| 26 | 4,045 | 51.32 t/s | 50.29 t/s |
| 27 | 4,208 | 51.41 t/s | 53.91 t/s |
| 28 | 4,364 | 51.40 t/s | 51.12 t/s |
| 29 | 4,489 | 51.04 t/s | 40.98 t/s |
| 30 | 4,616 | 50.73 t/s | 41.64 t/s |
| 31 | 4,767 | 50.70 t/s | 49.92 t/s |
| 32 | 4,912 | 50.62 t/s | 48.24 t/s |
| 33 | 5,086 | 50.83 t/s | 57.46 t/s |
| 34 | 5,226 | 50.70 t/s | 46.34 t/s |
| 35 | 5,420 | 51.08 t/s | 64.08 t/s |
| 36 | 5,587 | 51.18 t/s | 54.77 t/s |
| 37 | 5,758 | 51.34 t/s | 56.87 t/s |
| 38 | 5,923 | 51.42 t/s | 54.38 t/s |

---

## Task #9766 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:28:54.627` (Queue Delay: `7.54s`)
* **Total Context Footprint:** `2396` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `208.45 t/s` (`4.80 ms/tok`) | Time To First Token (TTFT) = `6.57s` |
| **Decode Speed (Generation)** | `57.19 t/s` (`17.49 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1370` (57.2%) / Out: `1026` (42.8%) | Total context footprint: `2396` tokens |
| **Speculative MTP Acceptance** | `57.87%` (`651/1125`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.74` tokens/step | Effective speedup: ~`2.74x` vs single-token decode |
| **Graphs Reused** | `9,950` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 1,366 | 100.0% | 3.91 | 349.47 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 168 | 55.47 t/s | 55.80 t/s |
| 2 | 329 | 54.48 t/s | 53.49 t/s |
| 3 | 482 | 53.28 t/s | 50.88 t/s |
| 4 | 644 | 53.32 t/s | 53.43 t/s |
| 5 | 823 | 54.54 t/s | 59.44 t/s |

---

## Task #10145 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:32:20.544` (Queue Delay: `4.81s`)
* **Total Context Footprint:** `3962` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `128.70 t/s` (`7.77 ms/tok`) | Time To First Token (TTFT) = `6.73s` |
| **Decode Speed (Generation)** | `47.07 t/s` (`21.25 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `866` (21.9%) / Out: `3096` (78.1%) | Total context footprint: `3962` tokens |
| **Speculative MTP Acceptance** | `51.56%` (`1881/3648`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.55` tokens/step | Effective speedup: ~`2.55x` vs single-token decode |
| **Graphs Reused** | `11,153` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 862 | 100.0% | 5.62 | 153.32 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 171 | 55.78 t/s | 56.10 t/s |
| 2 | 311 | 51.22 t/s | 46.60 t/s |
| 3 | 461 | 50.56 t/s | 49.25 t/s |
| 4 | 641 | 52.81 t/s | 59.59 t/s |
| 5 | 810 | 53.45 t/s | 56.03 t/s |
| 6 | 946 | 52.01 t/s | 44.81 t/s |
| 7 | 1,071 | 50.53 t/s | 41.59 t/s |
| 8 | 1,218 | 50.25 t/s | 48.31 t/s |
| 9 | 1,369 | 50.17 t/s | 49.54 t/s |
| 10 | 1,501 | 49.48 t/s | 43.33 t/s |
| 11 | 1,637 | 49.10 t/s | 45.17 t/s |
| 12 | 1,768 | 48.64 t/s | 43.58 t/s |
| 13 | 1,907 | 48.41 t/s | 45.67 t/s |
| 14 | 2,048 | 48.28 t/s | 46.62 t/s |
| 15 | 2,187 | 48.14 t/s | 46.13 t/s |
| 16 | 2,320 | 47.90 t/s | 44.24 t/s |
| 17 | 2,442 | 47.43 t/s | 40.03 t/s |
| 18 | 2,584 | 47.40 t/s | 46.96 t/s |
| 19 | 2,731 | 47.46 t/s | 48.41 t/s |
| 20 | 2,866 | 47.32 t/s | 44.74 t/s |
| 21 | 3,010 | 47.34 t/s | 47.69 t/s |

---

## Task #11366 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:33:39.592` (Queue Delay: `6.51s`)
* **Total Context Footprint:** `4924` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `540.99 t/s` (`1.85 ms/tok`) | Time To First Token (TTFT) = `5.25s` |
| **Decode Speed (Generation)** | `70.34 t/s` (`14.22 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `2838` (57.6%) / Out: `2086` (42.4%) | Total context footprint: `4924` tokens |
| **Speculative MTP Acceptance** | `63.73%` (`1369/2148`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.91` tokens/step | Effective speedup: ~`2.91x` vs single-token decode |
| **Graphs Reused** | `11,860` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,834 | 100.0% | 3.86 | 734.55 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 223 | 73.77 t/s | 74.10 t/s |
| 2 | 396 | 65.66 t/s | 57.54 t/s |
| 3 | 572 | 63.27 t/s | 58.49 t/s |
| 4 | 758 | 62.79 t/s | 61.36 t/s |
| 5 | 960 | 63.62 t/s | 66.92 t/s |
| 6 | 1,166 | 64.26 t/s | 67.46 t/s |
| 7 | 1,359 | 64.16 t/s | 63.53 t/s |
| 8 | 1,603 | 66.22 t/s | 80.62 t/s |
| 9 | 1,868 | 68.62 t/s | 87.90 t/s |

---

## Task #12087 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:36:21.625` (Queue Delay: `1.86s`)
* **Total Context Footprint:** `5202` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `122.98 t/s` (`8.13 ms/tok`) | Time To First Token (TTFT) = `6.50s` |
| **Decode Speed (Generation)** | `44.74 t/s` (`22.35 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `800` (15.4%) / Out: `4402` (84.6%) | Total context footprint: `5202` tokens |
| **Speculative MTP Acceptance** | `45.63%` (`2545/5577`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.37` tokens/step | Effective speedup: ~`2.37x` vs single-token decode |
| **Graphs Reused** | `13,701` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 796 | 100.0% | 5.49 | 145.02 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 125 | 41.05 t/s | 41.38 t/s |
| 2 | 271 | 44.69 t/s | 48.33 t/s |
| 3 | 407 | 44.71 t/s | 44.74 t/s |
| 4 | 532 | 43.94 t/s | 41.62 t/s |
| 5 | 673 | 44.47 t/s | 46.58 t/s |
| 6 | 786 | 43.28 t/s | 37.36 t/s |
| 7 | 903 | 42.61 t/s | 38.61 t/s |
| 8 | 1,043 | 43.08 t/s | 46.38 t/s |
| 9 | 1,193 | 43.80 t/s | 49.51 t/s |
| 10 | 1,322 | 43.68 t/s | 42.60 t/s |
| 11 | 1,478 | 44.37 t/s | 51.28 t/s |
| 12 | 1,621 | 44.64 t/s | 47.54 t/s |
| 13 | 1,758 | 44.66 t/s | 45.00 t/s |
| 14 | 1,881 | 44.40 t/s | 40.92 t/s |
| 15 | 2,023 | 44.57 t/s | 46.95 t/s |
| 16 | 2,168 | 44.80 t/s | 48.30 t/s |
| 17 | 2,285 | 44.44 t/s | 38.68 t/s |
| 18 | 2,424 | 44.54 t/s | 46.20 t/s |
| 19 | 2,552 | 44.42 t/s | 42.32 t/s |
| 20 | 2,691 | 44.50 t/s | 46.04 t/s |
| 21 | 2,822 | 44.44 t/s | 43.26 t/s |
| 22 | 2,957 | 44.45 t/s | 44.60 t/s |
| 23 | 3,073 | 44.18 t/s | 38.29 t/s |
| 24 | 3,200 | 44.08 t/s | 41.67 t/s |
| 25 | 3,332 | 44.07 t/s | 43.94 t/s |
| 26 | 3,479 | 44.24 t/s | 48.45 t/s |
| 27 | 3,604 | 44.13 t/s | 41.31 t/s |
| 28 | 3,753 | 44.30 t/s | 48.96 t/s |
| 29 | 3,901 | 44.47 t/s | 49.21 t/s |
| 30 | 4,048 | 44.62 t/s | 48.99 t/s |
| 31 | 4,192 | 44.73 t/s | 47.87 t/s |
| 32 | 4,323 | 44.67 t/s | 42.99 t/s |

---

## Task #13951 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:38:13.793` (Queue Delay: `7.25s`)
* **Total Context Footprint:** `4661` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `556.08 t/s` (`1.80 ms/tok`) | Time To First Token (TTFT) = `4.55s` |
| **Decode Speed (Generation)** | `78.53 t/s` (`12.73 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `2532` (54.3%) / Out: `2129` (45.7%) | Total context footprint: `4661` tokens |
| **Speculative MTP Acceptance** | `68.63%` (`1433/2088`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.06` tokens/step | Effective speedup: ~`3.06x` vs single-token decode |
| **Graphs Reused** | `14,387` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,528 | 100.0% | 3.22 | 785.73 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 231 | 76.47 t/s | 76.80 t/s |
| 2 | 424 | 70.28 t/s | 64.10 t/s |
| 3 | 623 | 68.84 t/s | 65.95 t/s |
| 4 | 838 | 69.45 t/s | 71.30 t/s |
| 5 | 1,076 | 71.37 t/s | 79.06 t/s |
| 6 | 1,318 | 72.78 t/s | 79.75 t/s |
| 7 | 1,595 | 75.46 t/s | 91.50 t/s |
| 8 | 1,848 | 76.49 t/s | 83.66 t/s |

---

## Task #14651 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:41:04.157` (Queue Delay: `1.74s`)
* **Total Context Footprint:** `2499` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `106.53 t/s` (`9.39 ms/tok`) | Time To First Token (TTFT) = `6.08s` |
| **Decode Speed (Generation)** | `50.28 t/s` (`19.89 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `648` (25.9%) / Out: `1851` (74.1%) | Total context footprint: `2499` tokens |
| **Speculative MTP Acceptance** | `53.49%` (`1141/2133`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.60` tokens/step | Effective speedup: ~`2.60x` vs single-token decode |
| **Graphs Reused** | `15,089` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 644 | 100.0% | 4.98 | 129.41 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 165 | 54.37 t/s | 54.70 t/s |
| 2 | 326 | 53.84 t/s | 53.30 t/s |
| 3 | 480 | 52.72 t/s | 50.52 t/s |
| 4 | 630 | 51.94 t/s | 49.58 t/s |
| 5 | 767 | 50.64 t/s | 45.41 t/s |
| 6 | 943 | 51.95 t/s | 58.56 t/s |
| 7 | 1,097 | 51.75 t/s | 50.55 t/s |
| 8 | 1,244 | 51.34 t/s | 48.50 t/s |
| 9 | 1,396 | 51.23 t/s | 50.30 t/s |
| 10 | 1,545 | 50.98 t/s | 48.84 t/s |
| 11 | 1,677 | 50.30 t/s | 43.47 t/s |
| 12 | 1,831 | 50.38 t/s | 51.21 t/s |

---

## Task #15367 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:41:53.951` (Queue Delay: `6.88s`)
* **Total Context Footprint:** `4550` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `547.90 t/s` (`1.83 ms/tok`) | Time To First Token (TTFT) = `4.33s` |
| **Decode Speed (Generation)** | `77.49 t/s` (`12.91 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `2373` (52.2%) / Out: `2177` (47.8%) | Total context footprint: `4550` tokens |
| **Speculative MTP Acceptance** | `66.81%` (`1453/2175`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.00` tokens/step | Effective speedup: ~`3.00x` vs single-token decode |
| **Graphs Reused** | `15,805` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,369 | 100.0% | 3.02 | 783.67 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 232 | 76.63 t/s | 76.96 t/s |
| 2 | 420 | 69.53 t/s | 62.43 t/s |
| 3 | 630 | 69.50 t/s | 69.42 t/s |
| 4 | 861 | 71.23 t/s | 76.44 t/s |
| 5 | 1,107 | 73.29 t/s | 81.54 t/s |
| 6 | 1,311 | 72.36 t/s | 67.70 t/s |
| 7 | 1,544 | 73.12 t/s | 77.64 t/s |
| 8 | 1,822 | 75.48 t/s | 92.02 t/s |
| 9 | 2,083 | 76.75 t/s | 86.92 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:52:31.925` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `1291` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `88.28 t/s` (`11.33 ms/tok`) | Time To First Token (TTFT) = `3.30s` |
| **Decode Speed (Generation)** | `20.23 t/s` (`49.42 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `291` (22.5%) / Out: `1000` (77.5%) | Total context footprint: `1291` tokens |
| **Speculative MTP Acceptance** | `74.25%` (`689/928`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.22` tokens/step | Effective speedup: ~`3.22x` vs single-token decode |
| **Graphs Reused** | `305` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 102 | 20.35 t/s | 20.55 t/s |
| 2 | 157 | 19.50 t/s | 18.12 t/s |
| 3 | 218 | 19.51 t/s | 19.52 t/s |
| 4 | 279 | 19.62 t/s | 20.03 t/s |
| 5 | 336 | 19.31 t/s | 17.92 t/s |
| 6 | 392 | 19.08 t/s | 17.82 t/s |
| 7 | 459 | 19.44 t/s | 21.84 t/s |
| 8 | 523 | 19.55 t/s | 20.40 t/s |
| 9 | 595 | 19.95 t/s | 23.45 t/s |
| 10 | 647 | 19.66 t/s | 16.84 t/s |
| 11 | 716 | 19.93 t/s | 22.83 t/s |
| 12 | 777 | 19.93 t/s | 20.01 t/s |
| 13 | 845 | 20.07 t/s | 21.73 t/s |
| 14 | 910 | 20.15 t/s | 21.34 t/s |
| 15 | 978 | 20.30 t/s | 22.41 t/s |

---

## Task #316 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:53:26.610` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `1621` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `86.08 t/s` (`11.62 ms/tok`) | Time To First Token (TTFT) = `3.12s` |
| **Decode Speed (Generation)** | `18.85 t/s` (`53.05 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `269` (16.6%) / Out: `1352` (83.4%) | Total context footprint: `1621` tokens |
| **Speculative MTP Acceptance** | `65.93%` (`898/1362`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.98` tokens/step | Effective speedup: ~`2.98x` vs single-token decode |
| **Graphs Reused** | `753` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 102 | 19.55 t/s | 19.74 t/s |
| 2 | 154 | 18.41 t/s | 16.53 t/s |
| 3 | 209 | 18.23 t/s | 17.75 t/s |
| 4 | 269 | 18.55 t/s | 19.74 t/s |
| 5 | 321 | 18.18 t/s | 16.51 t/s |
| 6 | 374 | 18.09 t/s | 17.54 t/s |
| 7 | 421 | 17.77 t/s | 15.59 t/s |
| 8 | 469 | 17.47 t/s | 15.24 t/s |
| 9 | 524 | 17.55 t/s | 18.28 t/s |
| 10 | 581 | 17.61 t/s | 18.15 t/s |
| 11 | 636 | 17.66 t/s | 18.20 t/s |
| 12 | 694 | 17.70 t/s | 18.18 t/s |
| 13 | 744 | 17.58 t/s | 16.03 t/s |
| 14 | 802 | 17.64 t/s | 18.46 t/s |
| 15 | 851 | 17.52 t/s | 15.69 t/s |
| 16 | 904 | 17.48 t/s | 16.92 t/s |
| 17 | 965 | 17.63 t/s | 20.21 t/s |
| 18 | 1,032 | 17.83 t/s | 21.35 t/s |
| 19 | 1,100 | 18.06 t/s | 22.31 t/s |
| 20 | 1,172 | 18.30 t/s | 22.93 t/s |
| 21 | 1,238 | 18.45 t/s | 21.69 t/s |
| 22 | 1,313 | 18.72 t/s | 24.61 t/s |

---

## Task #773 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-11 21:54:43.549` (Queue Delay: `2.13s`)
* **Total Context Footprint:** `3664` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `77.81 t/s` (`12.85 ms/tok`) | Time To First Token (TTFT) = `2.76s` |
| **Decode Speed (Generation)** | `18.82 t/s` (`53.13 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `215` (5.9%) / Out: `3449` (94.1%) | Total context footprint: `3664` tokens |
| **Speculative MTP Acceptance** | `66.41%` (`2297/3459`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.99` tokens/step | Effective speedup: ~`2.99x` vs single-token decode |
| **Graphs Reused** | `1,891` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 103 | 18.56 t/s | 18.74 t/s |
| 2 | 165 | 19.29 t/s | 20.62 t/s |
| 3 | 220 | 18.88 t/s | 17.75 t/s |
| 4 | 279 | 18.84 t/s | 18.69 t/s |
| 5 | 324 | 18.09 t/s | 14.53 t/s |
| 6 | 380 | 18.16 t/s | 18.56 t/s |
| 7 | 430 | 17.96 t/s | 16.59 t/s |
| 8 | 490 | 18.14 t/s | 19.50 t/s |
| 9 | 555 | 18.41 t/s | 20.76 t/s |
| 10 | 608 | 18.29 t/s | 17.17 t/s |
| 11 | 647 | 17.84 t/s | 12.87 t/s |
| 12 | 705 | 17.95 t/s | 19.22 t/s |
| 13 | 764 | 18.02 t/s | 18.96 t/s |
| 14 | 820 | 18.06 t/s | 18.58 t/s |
| 15 | 868 | 17.86 t/s | 15.09 t/s |
| 16 | 919 | 17.77 t/s | 16.26 t/s |
| 17 | 979 | 17.84 t/s | 19.05 t/s |
| 18 | 1,039 | 17.91 t/s | 19.18 t/s |
| 19 | 1,101 | 18.05 t/s | 20.67 t/s |
| 20 | 1,158 | 18.09 t/s | 18.85 t/s |
| 21 | 1,214 | 18.07 t/s | 17.80 t/s |
| 22 | 1,270 | 18.06 t/s | 17.80 t/s |
| 23 | 1,328 | 18.08 t/s | 18.46 t/s |
| 24 | 1,371 | 17.92 t/s | 14.12 t/s |
| 25 | 1,428 | 17.96 t/s | 18.97 t/s |
| 26 | 1,500 | 18.15 t/s | 22.88 t/s |
| 27 | 1,568 | 18.27 t/s | 21.54 t/s |
| 28 | 1,617 | 18.20 t/s | 16.10 t/s |
| 29 | 1,673 | 18.21 t/s | 18.67 t/s |
| 30 | 1,730 | 18.23 t/s | 18.65 t/s |
| 31 | 1,790 | 18.25 t/s | 19.04 t/s |
| 32 | 1,854 | 18.33 t/s | 20.95 t/s |
| 33 | 1,916 | 18.39 t/s | 20.16 t/s |
| 34 | 1,983 | 18.50 t/s | 22.30 t/s |
| 35 | 2,035 | 18.46 t/s | 16.98 t/s |
| 36 | 2,105 | 18.58 t/s | 23.31 t/s |
| 37 | 2,162 | 18.58 t/s | 18.62 t/s |
| 38 | 2,212 | 18.53 t/s | 16.33 t/s |
| 39 | 2,263 | 18.49 t/s | 16.95 t/s |
| 40 | 2,318 | 18.48 t/s | 17.98 t/s |
| 41 | 2,378 | 18.51 t/s | 19.91 t/s |
| 42 | 2,437 | 18.52 t/s | 19.16 t/s |
| 43 | 2,492 | 18.51 t/s | 17.86 t/s |
| 44 | 2,559 | 18.59 t/s | 22.22 t/s |
| 45 | 2,621 | 18.62 t/s | 20.13 t/s |
| 46 | 2,683 | 18.66 t/s | 20.52 t/s |
| 47 | 2,745 | 18.70 t/s | 20.18 t/s |
| 48 | 2,811 | 18.75 t/s | 21.53 t/s |
| 49 | 2,871 | 18.78 t/s | 19.86 t/s |
| 50 | 2,934 | 18.81 t/s | 20.48 t/s |
| 51 | 2,993 | 18.82 t/s | 19.53 t/s |
| 52 | 3,044 | 18.78 t/s | 16.54 t/s |
| 53 | 3,096 | 18.75 t/s | 17.08 t/s |
| 54 | 3,161 | 18.80 t/s | 21.39 t/s |
| 55 | 3,219 | 18.80 t/s | 18.97 t/s |
| 56 | 3,268 | 18.75 t/s | 16.16 t/s |
| 57 | 3,337 | 18.82 t/s | 22.45 t/s |
| 58 | 3,399 | 18.84 t/s | 20.36 t/s |

---

## Task #16096 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 16:19:42.390` (Queue Delay: `1.86s`)
* **Total Context Footprint:** `32` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `26.44 t/s` (`37.82 ms/tok`) | Time To First Token (TTFT) = `0.64s` |
| **Decode Speed (Generation)** | `74.94 t/s` (`13.34 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `17` (53.1%) / Out: `15` (46.9%) | Total context footprint: `32` tokens |
| **Speculative MTP Acceptance** | `66.67%` (`10/15`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.00` tokens/step | Effective speedup: ~`3.00x` vs single-token decode |
| **Graphs Reused** | `15,809` | CUDA/execution graph cache hits |

---

## Task #1929 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 16:20:00.642` (Queue Delay: `3.51s`)
* **Total Context Footprint:** `1296` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `92.46 t/s` (`10.81 ms/tok`) | Time To First Token (TTFT) = `3.20s` |
| **Decode Speed (Generation)** | `19.95 t/s` (`50.14 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `296` (22.8%) / Out: `1000` (77.2%) | Total context footprint: `1296` tokens |
| **Speculative MTP Acceptance** | `74.33%` (`689/927`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.23` tokens/step | Effective speedup: ~`3.23x` vs single-token decode |
| **Graphs Reused** | `2,195` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 19.53 t/s | 19.72 t/s |
| 2 | 156 | 18.95 t/s | 18.01 t/s |
| 3 | 210 | 18.48 t/s | 17.25 t/s |
| 4 | 274 | 18.88 t/s | 20.34 t/s |
| 5 | 346 | 19.62 t/s | 22.99 t/s |
| 6 | 409 | 19.72 t/s | 20.30 t/s |
| 7 | 481 | 20.16 t/s | 23.13 t/s |
| 8 | 531 | 19.76 t/s | 16.56 t/s |
| 9 | 595 | 19.85 t/s | 20.61 t/s |
| 10 | 656 | 19.84 t/s | 19.76 t/s |
| 11 | 724 | 20.00 t/s | 21.75 t/s |
| 12 | 790 | 20.10 t/s | 21.18 t/s |
| 13 | 852 | 20.09 t/s | 20.02 t/s |
| 14 | 922 | 20.25 t/s | 22.40 t/s |
| 15 | 978 | 20.15 t/s | 18.62 t/s |

---

## Task #2245 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 16:20:55.928` (Queue Delay: `0.00s`)
* **Total Context Footprint:** `1685` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `88.26 t/s` (`11.33 ms/tok`) | Time To First Token (TTFT) = `3.10s` |
| **Decode Speed (Generation)** | `18.96 t/s` (`52.75 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `274` (16.3%) / Out: `1411` (83.7%) | Total context footprint: `1685` tokens |
| **Speculative MTP Acceptance** | `67.74%` (`947/1398`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.03` tokens/step | Effective speedup: ~`3.03x` vs single-token decode |
| **Graphs Reused** | `2,655` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 101 | 17.36 t/s | 17.53 t/s |
| 2 | 149 | 16.65 t/s | 15.36 t/s |
| 3 | 198 | 16.41 t/s | 15.73 t/s |
| 4 | 245 | 16.18 t/s | 15.28 t/s |
| 5 | 290 | 15.88 t/s | 14.45 t/s |
| 6 | 333 | 15.61 t/s | 13.99 t/s |
| 7 | 387 | 15.80 t/s | 17.12 t/s |
| 8 | 434 | 15.72 t/s | 15.09 t/s |
| 9 | 489 | 15.98 t/s | 18.31 t/s |
| 10 | 559 | 16.58 t/s | 22.47 t/s |
| 11 | 621 | 16.87 t/s | 19.97 t/s |
| 12 | 679 | 16.99 t/s | 18.49 t/s |
| 13 | 742 | 17.23 t/s | 20.25 t/s |
| 14 | 806 | 17.46 t/s | 20.68 t/s |
| 15 | 868 | 17.65 t/s | 20.53 t/s |
| 16 | 918 | 17.55 t/s | 16.04 t/s |
| 17 | 993 | 17.94 t/s | 24.49 t/s |
| 18 | 1,071 | 18.31 t/s | 24.85 t/s |
| 19 | 1,121 | 18.22 t/s | 16.43 t/s |
| 20 | 1,175 | 18.20 t/s | 17.81 t/s |
| 21 | 1,255 | 18.53 t/s | 25.44 t/s |
| 22 | 1,326 | 18.74 t/s | 23.39 t/s |
| 23 | 1,402 | 18.98 t/s | 24.43 t/s |

---

## Task #2714 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 16:22:15.590` (Queue Delay: `2.16s`)
* **Total Context Footprint:** `2682` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `79.99 t/s` (`12.50 ms/tok`) | Time To First Token (TTFT) = `2.75s` |
| **Decode Speed (Generation)** | `18.67 t/s` (`53.57 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `220` (8.2%) / Out: `2462` (91.8%) | Total context footprint: `2682` tokens |
| **Speculative MTP Acceptance** | `68.23%` (`1654/2424`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.05` tokens/step | Effective speedup: ~`3.05x` vs single-token decode |
| **Graphs Reused** | `3,452` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 102 | 20.80 t/s | 21.01 t/s |
| 2 | 158 | 19.58 t/s | 17.71 t/s |
| 3 | 209 | 18.84 t/s | 16.85 t/s |
| 4 | 259 | 18.18 t/s | 15.86 t/s |
| 5 | 314 | 18.13 t/s | 17.92 t/s |
| 6 | 363 | 17.77 t/s | 15.78 t/s |
| 7 | 423 | 18.03 t/s | 19.81 t/s |
| 8 | 467 | 17.65 t/s | 14.66 t/s |
| 9 | 509 | 17.22 t/s | 13.53 t/s |
| 10 | 563 | 17.27 t/s | 17.74 t/s |
| 11 | 622 | 17.39 t/s | 18.62 t/s |
| 12 | 673 | 17.35 t/s | 16.96 t/s |
| 13 | 724 | 17.30 t/s | 16.62 t/s |
| 14 | 793 | 17.65 t/s | 22.35 t/s |
| 15 | 862 | 17.93 t/s | 22.01 t/s |
| 16 | 919 | 17.98 t/s | 18.70 t/s |
| 17 | 965 | 17.82 t/s | 15.15 t/s |
| 18 | 1,022 | 17.86 t/s | 18.58 t/s |
| 19 | 1,086 | 18.01 t/s | 20.91 t/s |
| 20 | 1,142 | 18.03 t/s | 18.42 t/s |
| 21 | 1,183 | 17.80 t/s | 13.10 t/s |
| 22 | 1,252 | 17.99 t/s | 21.98 t/s |
| 23 | 1,318 | 18.12 t/s | 21.00 t/s |
| 24 | 1,380 | 18.19 t/s | 19.71 t/s |
| 25 | 1,428 | 18.10 t/s | 15.89 t/s |
| 26 | 1,478 | 18.02 t/s | 16.10 t/s |
| 27 | 1,534 | 18.03 t/s | 18.26 t/s |
| 28 | 1,604 | 18.20 t/s | 22.91 t/s |
| 29 | 1,658 | 18.15 t/s | 16.80 t/s |
| 30 | 1,703 | 18.04 t/s | 14.69 t/s |
| 31 | 1,775 | 18.21 t/s | 23.62 t/s |
| 32 | 1,846 | 18.35 t/s | 22.50 t/s |
| 33 | 1,918 | 18.49 t/s | 23.21 t/s |
| 34 | 1,972 | 18.46 t/s | 17.20 t/s |
| 35 | 2,015 | 18.33 t/s | 13.93 t/s |
| 36 | 2,071 | 18.32 t/s | 17.96 t/s |
| 37 | 2,137 | 18.39 t/s | 21.02 t/s |
| 38 | 2,210 | 18.53 t/s | 23.89 t/s |
| 39 | 2,269 | 18.55 t/s | 19.22 t/s |
| 40 | 2,332 | 18.61 t/s | 20.99 t/s |
| 41 | 2,387 | 18.59 t/s | 17.83 t/s |
| 42 | 2,455 | 18.67 t/s | 22.11 t/s |

---

## Task #16104 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 18:15:46.195` (Queue Delay: `0.63s`)
* **Total Context Footprint:** `1853` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `98.83 t/s` (`10.12 ms/tok`) | Time To First Token (TTFT) = `16.17s` |
| **Decode Speed (Generation)** | `47.07 t/s` (`21.25 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1598` (86.2%) / Out: `255` (13.8%) | Total context footprint: `1853` tokens |
| **Speculative MTP Acceptance** | `39.66%` (`138/348`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.19` tokens/step | Effective speedup: ~`2.19x` vs single-token decode |
| **Graphs Reused** | `15,923` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 1,594 | 100.0% | 15.09 | 105.64 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 150 | 49.54 t/s | 49.87 t/s |

---

## Task #16225 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 18:40:38.937` (Queue Delay: `0.05s`)
* **Total Context Footprint:** `1139` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `137.89 t/s` (`7.25 ms/tok`) | Time To First Token (TTFT) = `2.62s` |
| **Decode Speed (Generation)** | `44.53 t/s` (`22.46 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `362` (31.8%) / Out: `777` (68.2%) | Total context footprint: `1139` tokens |
| **Speculative MTP Acceptance** | `36.57%` (`407/1113`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.10` tokens/step | Effective speedup: ~`2.10x` vs single-token decode |
| **Graphs Reused** | `16,290` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 137 | 44.96 t/s | 45.29 t/s |
| 2 | 273 | 45.12 t/s | 45.28 t/s |
| 3 | 394 | 43.45 t/s | 40.12 t/s |
| 4 | 540 | 44.68 t/s | 48.37 t/s |
| 5 | 677 | 44.76 t/s | 45.06 t/s |

---

## Task #16601 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 18:48:57.964` (Queue Delay: `1.32s`)
* **Total Context Footprint:** `3719` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `146.94 t/s` (`6.81 ms/tok`) | Time To First Token (TTFT) = `18.79s` |
| **Decode Speed (Generation)** | `63.28 t/s` (`15.80 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `2761` (74.2%) / Out: `958` (25.8%) | Total context footprint: `3719` tokens |
| **Speculative MTP Acceptance** | `70.23%` (`651/927`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.11` tokens/step | Effective speedup: ~`3.11x` vs single-token decode |
| **Graphs Reused** | `16,594` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 1,870 | 68.0% | 14.21 | 131.62 |
| 2 | 2,245 | 81.0% | 15.28 | 146.94 |
| 3 | 2,739 | 99.0% | 16.45 | 166.50 |
| 4 | 2,757 | 100.0% | 18.06 | 152.67 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 167 | 54.67 t/s | 55.00 t/s |
| 2 | 352 | 57.94 t/s | 61.22 t/s |
| 3 | 544 | 59.81 t/s | 63.57 t/s |
| 4 | 729 | 60.27 t/s | 61.65 t/s |

---

## Task #16918 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 18:56:20.338` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `1955` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `273.22 t/s` (`3.66 ms/tok`) | Time To First Token (TTFT) = `3.65s` |
| **Decode Speed (Generation)** | `77.74 t/s` (`12.86 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `997` (51.0%) / Out: `958` (49.0%) | Total context footprint: `1955` tokens |
| **Speculative MTP Acceptance** | `98.08%` (`715/729`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.94` tokens/step | Effective speedup: ~`3.94x` vs single-token decode |
| **Graphs Reused** | `16,832` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 238 | 78.63 t/s | 78.95 t/s |
| 2 | 478 | 79.10 t/s | 79.57 t/s |
| 3 | 711 | 78.32 t/s | 76.77 t/s |
| 4 | 943 | 77.82 t/s | 76.35 t/s |

---

## Task #17166 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 18:56:58.026` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `1895` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `253.08 t/s` (`3.95 ms/tok`) | Time To First Token (TTFT) = `3.93s` |
| **Decode Speed (Generation)** | `43.14 t/s` (`23.18 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `995` (52.5%) / Out: `900` (47.5%) | Total context footprint: `1895` tokens |
| **Speculative MTP Acceptance** | `38.44%` (`482/1254`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.15` tokens/step | Effective speedup: ~`2.15x` vs single-token decode |
| **Graphs Reused** | `17,246` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 991 | 100.0% | 3.24 | 305.79 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 141 | 46.02 t/s | 46.34 t/s |
| 2 | 281 | 46.32 t/s | 46.63 t/s |
| 3 | 416 | 45.71 t/s | 44.50 t/s |
| 4 | 535 | 44.19 t/s | 39.59 t/s |
| 5 | 664 | 43.85 t/s | 42.50 t/s |
| 6 | 788 | 43.33 t/s | 40.77 t/s |

---

## Task #17589 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 20:14:29.002` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `1837` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `226.67 t/s` (`4.41 ms/tok`) | Time To First Token (TTFT) = `4.12s` |
| **Decode Speed (Generation)** | `72.18 t/s` (`13.85 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `933` (50.8%) / Out: `904` (49.2%) | Total context footprint: `1837` tokens |
| **Speculative MTP Acceptance** | `97.68%` (`674/690`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.93` tokens/step | Effective speedup: ~`3.93x` vs single-token decode |
| **Graphs Reused** | `17,471` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 929 | 100.0% | 3.34 | 277.76 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 227 | 75.15 t/s | 75.47 t/s |
| 2 | 454 | 75.22 t/s | 75.29 t/s |
| 3 | 680 | 75.15 t/s | 75.00 t/s |
| 4 | 869 | 72.02 t/s | 62.66 t/s |

---

## Task #17824 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 20:44:19.064` (Queue Delay: `0.05s`)
* **Total Context Footprint:** `1845` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `226.12 t/s` (`4.42 ms/tok`) | Time To First Token (TTFT) = `4.16s` |
| **Decode Speed (Generation)** | `74.18 t/s` (`13.48 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `941` (51.0%) / Out: `904` (49.0%) | Total context footprint: `1845` tokens |
| **Speculative MTP Acceptance** | `97.97%` (`676/690`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `3.94` tokens/step | Effective speedup: ~`3.94x` vs single-token decode |
| **Graphs Reused** | `17,696` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 937 | 100.0% | 3.40 | 275.33 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 217 | 71.78 t/s | 72.11 t/s |
| 2 | 444 | 73.30 t/s | 74.80 t/s |
| 3 | 672 | 73.85 t/s | 74.95 t/s |
| 4 | 903 | 74.41 t/s | 76.10 t/s |

---

## Task #18059 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 20:45:43.931` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `2209` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `213.07 t/s` (`4.69 ms/tok`) | Time To First Token (TTFT) = `4.41s` |
| **Decode Speed (Generation)** | `41.94 t/s` (`23.84 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `940` (42.6%) / Out: `1269` (57.4%) | Total context footprint: `2209` tokens |
| **Speculative MTP Acceptance** | `39.97%` (`693/1734`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.20` tokens/step | Effective speedup: ~`2.20x` vs single-token decode |
| **Graphs Reused** | `18,268` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 936 | 100.0% | 3.65 | 256.26 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 119 | 39.28 t/s | 39.61 t/s |
| 2 | 241 | 39.79 t/s | 40.30 t/s |
| 3 | 365 | 40.26 t/s | 41.20 t/s |
| 4 | 489 | 40.44 t/s | 40.96 t/s |
| 5 | 615 | 40.63 t/s | 41.40 t/s |
| 6 | 729 | 40.17 t/s | 37.87 t/s |
| 7 | 866 | 40.87 t/s | 45.06 t/s |
| 8 | 988 | 40.77 t/s | 40.05 t/s |
| 9 | 1,124 | 41.22 t/s | 44.77 t/s |

---

## Task #18642 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 20:53:59.963` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `1833` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `212.04 t/s` (`4.72 ms/tok`) | Time To First Token (TTFT) = `6.16s` |
| **Decode Speed (Generation)** | `39.96 t/s` (`25.02 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1306` (71.2%) / Out: `527` (28.8%) | Total context footprint: `1833` tokens |
| **Speculative MTP Acceptance** | `37.37%` (`278/744`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.12` tokens/step | Effective speedup: ~`2.12x` vs single-token decode |
| **Graphs Reused** | `18,513` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 1,281 | 100.0% | 3.06 | 418.96 |
| 2 | 1,302 | 100.0% | 5.25 | 247.83 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 128 | 42.04 t/s | 42.37 t/s |
| 2 | 239 | 39.40 t/s | 36.76 t/s |
| 3 | 368 | 40.52 t/s | 42.76 t/s |
| 4 | 483 | 39.87 t/s | 37.94 t/s |

---

## Task #18895 (Slot 0)

* **Model:** `Huihui-Qwen3.6-35B-A3B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-12 20:54:49.496` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `3044` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `152.51 t/s` (`6.56 ms/tok`) | Time To First Token (TTFT) = `3.74s` |
| **Decode Speed (Generation)** | `41.80 t/s` (`23.92 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `570` (18.7%) / Out: `2474` (81.3%) | Total context footprint: `3044` tokens |
| **Speculative MTP Acceptance** | `42.92%` (`1392/3243`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.29` tokens/step | Effective speedup: ~`2.29x` vs single-token decode |
| **Graphs Reused** | `19,584` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 113 | 36.92 t/s | 37.24 t/s |
| 2 | 231 | 37.89 t/s | 38.85 t/s |
| 3 | 358 | 39.22 t/s | 41.88 t/s |
| 4 | 476 | 39.17 t/s | 39.03 t/s |
| 5 | 593 | 39.01 t/s | 38.36 t/s |
| 6 | 707 | 38.82 t/s | 37.88 t/s |
| 7 | 826 | 38.91 t/s | 39.48 t/s |
| 8 | 967 | 39.84 t/s | 46.29 t/s |
| 9 | 1,091 | 39.95 t/s | 40.87 t/s |
| 10 | 1,222 | 40.32 t/s | 43.65 t/s |
| 11 | 1,352 | 40.56 t/s | 42.92 t/s |
| 12 | 1,490 | 41.00 t/s | 45.96 t/s |
| 13 | 1,621 | 41.17 t/s | 43.17 t/s |
| 14 | 1,737 | 40.95 t/s | 38.12 t/s |
| 15 | 1,869 | 41.11 t/s | 43.30 t/s |
| 16 | 2,002 | 41.30 t/s | 44.19 t/s |
| 17 | 2,115 | 41.07 t/s | 37.34 t/s |
| 18 | 2,248 | 41.21 t/s | 43.60 t/s |
| 19 | 2,405 | 41.77 t/s | 51.79 t/s |

---

## Task #19981 (Slot 0)

* **Model:** `DeepSeek-R1-Distill-Qwen-7B-Hybrid`
* **Dispatch Time:** `2026-09-12 20:59:10.744` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `2524` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `231.25 t/s` (`4.32 ms/tok`) | Time To First Token (TTFT) = `0.60s` |
| **Decode Speed (Generation)** | `28.73 t/s` (`34.80 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `2517` (99.7%) / Out: `7` (0.3%) | Total context footprint: `2524` tokens |
| **Speculative MTP Acceptance** | `41.67%` (`5/12`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.25` tokens/step | Effective speedup: ~`2.25x` vs single-token decode |
| **Graphs Reused** | `19,587` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,001 | 96.0% | 4.58 | 436.71 |
| 2 | 2,492 | 100.0% | 7.40 | 336.92 |
| 3 | 2,513 | 100.0% | 9.99 | 251.44 |

---

## Task #0 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-13 18:40:52.382` (Queue Delay: `0.01s`)
* **Total Context Footprint:** `639` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `63.92 t/s` (`15.65 ms/tok`) | Time To First Token (TTFT) = `3.93s` |
| **Decode Speed (Generation)** | `17.49 t/s` (`57.17 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `251` (39.3%) / Out: `388` (60.7%) | Total context footprint: `639` tokens |
| **Speculative MTP Acceptance** | `42.05%` (`217/516`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.26` tokens/step | Effective speedup: ~`2.26x` vs single-token decode |
| **Graphs Reused** | `170` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 103 | 17.42 t/s | 17.59 t/s |
| 2 | 154 | 17.19 t/s | 16.76 t/s |
| 3 | 210 | 17.52 t/s | 18.48 t/s |
| 4 | 264 | 17.49 t/s | 17.40 t/s |
| 5 | 318 | 17.45 t/s | 17.26 t/s |
| 6 | 372 | 17.50 t/s | 17.75 t/s |

---

## Task #176 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-13 18:45:55.981` (Queue Delay: `1.49s`)
* **Total Context Footprint:** `825` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `71.03 t/s` (`14.08 ms/tok`) | Time To First Token (TTFT) = `6.07s` |
| **Decode Speed (Generation)** | `17.26 t/s` (`57.94 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `431` (52.2%) / Out: `394` (47.8%) | Total context footprint: `825` tokens |
| **Speculative MTP Acceptance** | `40.68%` (`216/531`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.22` tokens/step | Effective speedup: ~`2.22x` vs single-token decode |
| **Graphs Reused** | `344` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 427 | 99.0% | 4.51 | 94.70 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 101 | 18.76 t/s | 18.95 t/s |
| 2 | 155 | 18.33 t/s | 17.58 t/s |
| 3 | 203 | 17.65 t/s | 15.79 t/s |
| 4 | 250 | 17.10 t/s | 15.07 t/s |
| 5 | 307 | 17.36 t/s | 18.60 t/s |
| 6 | 364 | 17.52 t/s | 18.42 t/s |

---

## Task #357 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-13 20:19:23.100` (Queue Delay: `1.83s`)
* **Total Context Footprint:** `411` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `120.67 t/s` (`8.29 ms/tok`) | Time To First Token (TTFT) = `3.38s` |
| **Decode Speed (Generation)** | `7.82 t/s` (`127.91 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `408` (99.3%) / Out: `3` (0.7%) | Total context footprint: `411` tokens |
| **Speculative MTP Acceptance** | `50.00%` (`3/6`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.50` tokens/step | Effective speedup: ~`2.50x` vs single-token decode |
| **Graphs Reused** | `345` | CUDA/execution graph cache hits |

---

## Task #362 (Slot 0)

* **Model:** `Huihui-Qwen3.6-27B-abliterated-MTP-GGUF-Q4_K`
* **Dispatch Time:** `2026-09-13 20:20:08.825` (Queue Delay: `1.32s`)
* **Total Context Footprint:** `1039` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `125.12 t/s` (`7.99 ms/tok`) | Time To First Token (TTFT) = `3.36s` |
| **Decode Speed (Generation)** | `19.33 t/s` (`51.73 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `420` (40.4%) / Out: `619` (59.6%) | Total context footprint: `1039` tokens |
| **Speculative MTP Acceptance** | `49.00%` (`369/753`) | Multi-Token Prediction hit rate |
| **Mean Speculative Length** | `2.47` tokens/step | Effective speedup: ~`2.47x` vs single-token decode |
| **Graphs Reused** | `592` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 19.12 t/s | 19.31 t/s |
| 2 | 154 | 18.59 t/s | 17.70 t/s |
| 3 | 219 | 19.38 t/s | 21.51 t/s |
| 4 | 276 | 19.23 t/s | 18.68 t/s |
| 5 | 330 | 18.97 t/s | 17.73 t/s |
| 6 | 395 | 19.30 t/s | 21.21 t/s |
| 7 | 450 | 19.11 t/s | 17.80 t/s |
| 8 | 503 | 18.91 t/s | 17.39 t/s |
| 9 | 570 | 19.20 t/s | 21.66 t/s |

---

## Task #0 (Slot 0)

* **Model:** `Gemma-4-26B-A4B-it-GGUF`
* **Dispatch Time:** `2026-09-13 20:34:37.651` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `2079` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `204.53 t/s` (`4.89 ms/tok`) | Time To First Token (TTFT) = `7.06s` |
| **Decode Speed (Generation)** | `41.96 t/s` (`23.83 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `1444` (69.5%) / Out: `635` (30.5%) | Total context footprint: `2079` tokens |
| **Graphs Reused** | `631` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 1,440 | 100.0% | 4.75 | 303.47 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 131 | 43.10 t/s | 43.43 t/s |
| 2 | 258 | 42.71 t/s | 42.31 t/s |
| 3 | 382 | 42.25 t/s | 41.32 t/s |
| 4 | 507 | 42.02 t/s | 41.36 t/s |
| 5 | 633 | 41.96 t/s | 41.72 t/s |

---

## Task #640 (Slot 0)

* **Model:** `Gemma-4-26B-A4B-it-GGUF`
* **Dispatch Time:** `2026-09-13 20:38:38.894` (Queue Delay: `0.06s`)
* **Total Context Footprint:** `1586` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `111.29 t/s` (`8.99 ms/tok`) | Time To First Token (TTFT) = `8.30s` |
| **Decode Speed (Generation)** | `42.28 t/s` (`23.65 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `924` (58.3%) / Out: `662` (41.7%) | Total context footprint: `1586` tokens |
| **Graphs Reused** | `1,289` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 642 | 88.0% | 4.37 | 146.80 |
| 2 | 920 | 100.0% | 6.68 | 137.75 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 129 | 42.59 t/s | 42.93 t/s |
| 2 | 258 | 42.74 t/s | 42.89 t/s |
| 3 | 384 | 42.45 t/s | 41.85 t/s |
| 4 | 513 | 42.58 t/s | 42.98 t/s |
| 5 | 637 | 42.32 t/s | 41.26 t/s |

---

## Task #0 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-13 20:43:00.500` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 16.0% | 19.70 | 103.96 |
| 2 | 4,096 | 32.0% | 49.32 | 83.04 |
| 3 | 6,144 | 48.0% | 88.95 | 69.07 |
| 4 | 8,192 | 64.0% | 138.65 | 59.08 |
| 5 | 10,240 | 80.0% | 198.03 | 51.71 |
| 6 | 12,288 | 95.0% | 267.64 | 45.91 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 7.47 t/s | 7.54 t/s |
| 2 | 123 | 7.49 t/s | 7.61 t/s |
| 3 | 145 | 7.45 t/s | 7.25 t/s |
| 4 | 168 | 7.45 t/s | 7.45 t/s |
| 5 | 191 | 7.46 t/s | 7.47 t/s |
| 6 | 213 | 7.43 t/s | 7.23 t/s |
| 7 | 235 | 7.40 t/s | 7.11 t/s |
| 8 | 256 | 7.35 t/s | 6.84 t/s |
| 9 | 279 | 7.36 t/s | 7.43 t/s |
| 10 | 301 | 7.33 t/s | 7.04 t/s |
| 11 | 322 | 7.30 t/s | 6.89 t/s |
| 12 | 343 | 7.27 t/s | 6.82 t/s |
| 13 | 365 | 7.27 t/s | 7.27 t/s |
| 14 | 387 | 7.27 t/s | 7.32 t/s |
| 15 | 408 | 7.25 t/s | 6.80 t/s |
| 16 | 432 | 7.27 t/s | 7.67 t/s |
| 17 | 452 | 7.24 t/s | 6.62 t/s |
| 18 | 473 | 7.21 t/s | 6.75 t/s |
| 19 | 494 | 7.20 t/s | 6.95 t/s |
| 20 | 516 | 7.20 t/s | 7.08 t/s |
| 21 | 540 | 7.22 t/s | 7.67 t/s |
| 22 | 562 | 7.22 t/s | 7.25 t/s |
| 23 | 585 | 7.24 t/s | 7.66 t/s |
| 24 | 608 | 7.25 t/s | 7.66 t/s |
| 25 | 631 | 7.26 t/s | 7.53 t/s |
| 26 | 654 | 7.26 t/s | 7.36 t/s |
| 27 | 677 | 7.27 t/s | 7.55 t/s |
| 28 | 698 | 7.26 t/s | 6.97 t/s |
| 29 | 720 | 7.26 t/s | 7.14 t/s |
| 30 | 741 | 7.25 t/s | 6.82 t/s |
| 31 | 762 | 7.24 t/s | 6.90 t/s |
| 32 | 783 | 7.22 t/s | 6.75 t/s |
| 33 | 806 | 7.22 t/s | 7.30 t/s |
| 34 | 827 | 7.22 t/s | 6.88 t/s |
| 35 | 849 | 7.21 t/s | 7.00 t/s |
| 36 | 869 | 7.19 t/s | 6.54 t/s |
| 37 | 891 | 7.20 t/s | 7.29 t/s |
| 38 | 913 | 7.20 t/s | 7.21 t/s |
| 39 | 933 | 7.18 t/s | 6.58 t/s |
| 40 | 952 | 7.16 t/s | 6.32 t/s |
| 41 | 974 | 7.16 t/s | 7.14 t/s |
| 42 | 996 | 7.15 t/s | 6.87 t/s |
| 43 | 1,018 | 7.15 t/s | 6.79 t/s |
| 44 | 1,039 | 7.14 t/s | 6.69 t/s |
| 45 | 1,060 | 7.13 t/s | 6.72 t/s |
| 46 | 1,081 | 7.12 t/s | 6.89 t/s |
| 47 | 1,103 | 7.12 t/s | 7.06 t/s |
| 48 | 1,124 | 7.11 t/s | 6.76 t/s |
| 49 | 1,145 | 7.11 t/s | 6.99 t/s |
| 50 | 1,166 | 7.10 t/s | 6.74 t/s |
| 51 | 1,186 | 7.10 t/s | 6.60 t/s |
| 52 | 1,206 | 7.09 t/s | 6.53 t/s |
| 53 | 1,226 | 7.07 t/s | 6.36 t/s |
| 54 | 1,246 | 7.06 t/s | 6.54 t/s |
| 55 | 1,266 | 7.05 t/s | 6.46 t/s |
| 56 | 1,287 | 7.05 t/s | 6.81 t/s |
| 57 | 1,307 | 7.04 t/s | 6.60 t/s |
| 58 | 1,327 | 7.03 t/s | 6.61 t/s |
| 59 | 1,347 | 7.03 t/s | 6.50 t/s |
| 60 | 1,368 | 7.03 t/s | 7.00 t/s |
| 61 | 1,388 | 7.02 t/s | 6.66 t/s |
| 62 | 1,408 | 7.01 t/s | 6.57 t/s |
| 63 | 1,428 | 7.01 t/s | 6.59 t/s |
| 64 | 1,448 | 7.00 t/s | 6.38 t/s |
| 65 | 1,468 | 6.99 t/s | 6.62 t/s |
| 66 | 1,488 | 6.98 t/s | 6.51 t/s |
| 67 | 1,509 | 6.98 t/s | 6.76 t/s |
| 68 | 1,529 | 6.97 t/s | 6.38 t/s |
| 69 | 1,548 | 6.96 t/s | 6.21 t/s |
| 70 | 1,569 | 6.96 t/s | 6.85 t/s |
| 71 | 1,590 | 6.96 t/s | 6.82 t/s |
| 72 | 1,610 | 6.95 t/s | 6.49 t/s |
| 73 | 1,630 | 6.95 t/s | 6.63 t/s |
| 74 | 1,650 | 6.94 t/s | 6.59 t/s |
| 75 | 1,670 | 6.94 t/s | 6.66 t/s |
| 76 | 1,691 | 6.94 t/s | 6.91 t/s |
| 77 | 1,711 | 6.94 t/s | 6.65 t/s |
| 78 | 1,733 | 6.94 t/s | 7.04 t/s |
| 79 | 1,754 | 6.94 t/s | 6.96 t/s |
| 80 | 1,775 | 6.94 t/s | 6.75 t/s |
| 81 | 1,796 | 6.93 t/s | 6.85 t/s |
| 82 | 1,817 | 6.93 t/s | 6.89 t/s |
| 83 | 1,838 | 6.93 t/s | 6.74 t/s |
| 84 | 1,859 | 6.93 t/s | 6.93 t/s |
| 85 | 1,880 | 6.93 t/s | 6.91 t/s |
| 86 | 1,901 | 6.93 t/s | 6.89 t/s |
| 87 | 1,922 | 6.93 t/s | 6.71 t/s |
| 88 | 1,943 | 6.93 t/s | 6.86 t/s |
| 89 | 1,964 | 6.93 t/s | 6.83 t/s |
| 90 | 1,984 | 6.92 t/s | 6.62 t/s |
| 91 | 2,005 | 6.92 t/s | 6.87 t/s |
| 92 | 2,026 | 6.92 t/s | 6.72 t/s |
| 93 | 2,047 | 6.92 t/s | 6.81 t/s |
| 94 | 2,067 | 6.91 t/s | 6.41 t/s |
| 95 | 2,088 | 6.91 t/s | 6.82 t/s |
| 96 | 2,108 | 6.91 t/s | 6.45 t/s |
| 97 | 2,127 | 6.90 t/s | 6.30 t/s |
| 98 | 2,147 | 6.90 t/s | 6.62 t/s |
| 99 | 2,166 | 6.89 t/s | 6.32 t/s |
| 100 | 2,186 | 6.89 t/s | 6.49 t/s |
| 101 | 2,204 | 6.88 t/s | 5.90 t/s |
| 102 | 2,225 | 6.88 t/s | 6.76 t/s |
| 103 | 2,245 | 6.88 t/s | 6.57 t/s |
| 104 | 2,263 | 6.87 t/s | 5.86 t/s |
| 105 | 2,283 | 6.86 t/s | 6.38 t/s |
| 106 | 2,304 | 6.86 t/s | 6.82 t/s |
| 107 | 2,324 | 6.86 t/s | 6.42 t/s |
| 108 | 2,344 | 6.86 t/s | 6.51 t/s |
| 109 | 2,365 | 6.86 t/s | 6.84 t/s |
| 110 | 2,386 | 6.85 t/s | 6.78 t/s |
| 111 | 2,407 | 6.85 t/s | 6.75 t/s |
| 112 | 2,427 | 6.85 t/s | 6.61 t/s |
| 113 | 2,448 | 6.85 t/s | 6.71 t/s |
| 114 | 2,469 | 6.85 t/s | 6.73 t/s |
| 115 | 2,490 | 6.85 t/s | 6.90 t/s |
| 116 | 2,509 | 6.85 t/s | 6.33 t/s |
| 117 | 2,529 | 6.84 t/s | 6.41 t/s |
| 118 | 2,549 | 6.84 t/s | 6.50 t/s |
| 119 | 2,571 | 6.84 t/s | 7.10 t/s |
| 120 | 2,592 | 6.84 t/s | 6.71 t/s |
| 121 | 2,611 | 6.84 t/s | 6.24 t/s |
| 122 | 2,630 | 6.83 t/s | 6.30 t/s |
| 123 | 2,650 | 6.83 t/s | 6.44 t/s |
| 124 | 2,670 | 6.83 t/s | 6.59 t/s |
| 125 | 2,689 | 6.82 t/s | 6.24 t/s |
| 126 | 2,709 | 6.82 t/s | 6.66 t/s |
| 127 | 2,730 | 6.82 t/s | 6.76 t/s |
| 128 | 2,749 | 6.82 t/s | 6.30 t/s |
| 129 | 2,769 | 6.81 t/s | 6.44 t/s |
| 130 | 2,786 | 6.80 t/s | 5.45 t/s |
| 131 | 2,806 | 6.80 t/s | 6.35 t/s |
| 132 | 2,825 | 6.79 t/s | 6.06 t/s |
| 133 | 2,844 | 6.79 t/s | 6.18 t/s |
| 134 | 2,863 | 6.79 t/s | 6.27 t/s |
| 135 | 2,883 | 6.78 t/s | 6.37 t/s |
| 136 | 2,901 | 6.78 t/s | 5.86 t/s |
| 137 | 2,920 | 6.77 t/s | 6.32 t/s |
| 138 | 2,940 | 6.77 t/s | 6.50 t/s |
| 139 | 2,960 | 6.77 t/s | 6.45 t/s |
| 140 | 2,980 | 6.77 t/s | 6.62 t/s |
| 141 | 3,001 | 6.77 t/s | 6.65 t/s |
| 142 | 3,020 | 6.76 t/s | 6.19 t/s |
| 143 | 3,040 | 6.76 t/s | 6.30 t/s |
| 144 | 3,059 | 6.76 t/s | 6.21 t/s |
| 145 | 3,080 | 6.76 t/s | 6.81 t/s |
| 146 | 3,100 | 6.76 t/s | 6.63 t/s |
| 147 | 3,120 | 6.75 t/s | 6.63 t/s |
| 148 | 3,141 | 6.75 t/s | 6.68 t/s |
| 149 | 3,161 | 6.75 t/s | 6.61 t/s |
| 150 | 3,179 | 6.75 t/s | 5.77 t/s |
| 151 | 3,199 | 6.75 t/s | 6.63 t/s |
| 152 | 3,218 | 6.74 t/s | 6.16 t/s |
| 153 | 3,237 | 6.74 t/s | 6.33 t/s |
| 154 | 3,257 | 6.74 t/s | 6.48 t/s |
| 155 | 3,277 | 6.74 t/s | 6.49 t/s |
| 156 | 3,297 | 6.73 t/s | 6.56 t/s |
| 157 | 3,317 | 6.73 t/s | 6.53 t/s |
| 158 | 3,337 | 6.73 t/s | 6.51 t/s |
| 159 | 3,356 | 6.73 t/s | 6.33 t/s |
| 160 | 3,376 | 6.73 t/s | 6.45 t/s |
| 161 | 3,396 | 6.73 t/s | 6.46 t/s |
| 162 | 3,416 | 6.72 t/s | 6.37 t/s |
| 163 | 3,436 | 6.72 t/s | 6.35 t/s |
| 164 | 3,456 | 6.72 t/s | 6.52 t/s |
| 165 | 3,475 | 6.72 t/s | 6.09 t/s |
| 166 | 3,495 | 6.72 t/s | 6.47 t/s |
| 167 | 3,515 | 6.71 t/s | 6.59 t/s |
| 168 | 3,536 | 6.71 t/s | 6.71 t/s |
| 169 | 3,555 | 6.71 t/s | 6.16 t/s |
| 170 | 3,575 | 6.71 t/s | 6.52 t/s |
| 171 | 3,595 | 6.71 t/s | 6.52 t/s |
| 172 | 3,615 | 6.71 t/s | 6.57 t/s |
| 173 | 3,635 | 6.71 t/s | 6.45 t/s |
| 174 | 3,654 | 6.70 t/s | 6.28 t/s |
| 175 | 3,672 | 6.70 t/s | 5.90 t/s |
| 176 | 3,691 | 6.70 t/s | 6.11 t/s |
| 177 | 3,710 | 6.69 t/s | 6.16 t/s |
| 178 | 3,729 | 6.69 t/s | 6.19 t/s |
| 179 | 3,749 | 6.69 t/s | 6.41 t/s |
| 180 | 3,767 | 6.68 t/s | 5.76 t/s |
| 181 | 3,786 | 6.68 t/s | 6.31 t/s |
| 182 | 3,805 | 6.68 t/s | 6.18 t/s |
| 183 | 3,824 | 6.68 t/s | 6.04 t/s |
| 184 | 3,844 | 6.67 t/s | 6.33 t/s |
| 185 | 3,864 | 6.67 t/s | 6.43 t/s |
| 186 | 3,883 | 6.67 t/s | 6.24 t/s |
| 187 | 3,903 | 6.67 t/s | 6.43 t/s |
| 188 | 3,922 | 6.67 t/s | 6.20 t/s |
| 189 | 3,942 | 6.67 t/s | 6.35 t/s |
| 190 | 3,962 | 6.66 t/s | 6.37 t/s |
| 191 | 3,980 | 6.66 t/s | 5.93 t/s |
| 192 | 3,998 | 6.66 t/s | 5.95 t/s |
| 193 | 4,018 | 6.66 t/s | 6.47 t/s |
| 194 | 4,037 | 6.65 t/s | 6.13 t/s |
| 195 | 4,055 | 6.65 t/s | 5.91 t/s |
| 196 | 4,074 | 6.65 t/s | 6.28 t/s |
| 197 | 4,093 | 6.64 t/s | 6.12 t/s |
| 198 | 4,112 | 6.64 t/s | 6.30 t/s |
| 199 | 4,130 | 6.64 t/s | 5.65 t/s |
| 200 | 4,149 | 6.63 t/s | 6.06 t/s |
| 201 | 4,168 | 6.63 t/s | 6.09 t/s |
| 202 | 4,188 | 6.63 t/s | 6.57 t/s |
| 203 | 4,207 | 6.63 t/s | 6.05 t/s |
| 204 | 4,227 | 6.63 t/s | 6.29 t/s |
| 205 | 4,245 | 6.62 t/s | 5.83 t/s |
| 206 | 4,264 | 6.62 t/s | 6.20 t/s |
| 207 | 4,282 | 6.62 t/s | 5.97 t/s |
| 208 | 4,300 | 6.62 t/s | 5.91 t/s |
| 209 | 4,318 | 6.61 t/s | 5.98 t/s |
| 210 | 4,336 | 6.61 t/s | 5.70 t/s |
| 211 | 4,353 | 6.60 t/s | 5.64 t/s |
| 212 | 4,372 | 6.60 t/s | 6.02 t/s |
| 213 | 4,392 | 6.60 t/s | 6.42 t/s |
| 214 | 4,411 | 6.60 t/s | 6.26 t/s |
| 215 | 4,431 | 6.60 t/s | 6.38 t/s |
| 216 | 4,449 | 6.59 t/s | 5.66 t/s |
| 217 | 4,469 | 6.59 t/s | 6.45 t/s |
| 218 | 4,489 | 6.59 t/s | 6.40 t/s |
| 219 | 4,508 | 6.59 t/s | 6.12 t/s |
| 220 | 4,527 | 6.59 t/s | 6.16 t/s |
| 221 | 4,547 | 6.59 t/s | 6.43 t/s |
| 222 | 4,567 | 6.59 t/s | 6.39 t/s |
| 223 | 4,586 | 6.58 t/s | 6.07 t/s |
| 224 | 4,605 | 6.58 t/s | 6.30 t/s |
| 225 | 4,624 | 6.58 t/s | 6.13 t/s |
| 226 | 4,644 | 6.58 t/s | 6.60 t/s |
| 227 | 4,663 | 6.58 t/s | 6.02 t/s |
| 228 | 4,682 | 6.58 t/s | 6.12 t/s |
| 229 | 4,701 | 6.57 t/s | 6.21 t/s |
| 230 | 4,720 | 6.57 t/s | 6.27 t/s |
| 231 | 4,739 | 6.57 t/s | 6.31 t/s |
| 232 | 4,759 | 6.57 t/s | 6.38 t/s |
| 233 | 4,778 | 6.57 t/s | 6.14 t/s |
| 234 | 4,797 | 6.57 t/s | 6.09 t/s |
| 235 | 4,815 | 6.56 t/s | 5.96 t/s |
| 236 | 4,834 | 6.56 t/s | 6.12 t/s |
| 237 | 4,853 | 6.56 t/s | 6.26 t/s |
| 238 | 4,872 | 6.56 t/s | 6.05 t/s |
| 239 | 4,890 | 6.56 t/s | 5.87 t/s |
| 240 | 4,908 | 6.55 t/s | 5.70 t/s |
| 241 | 4,926 | 6.55 t/s | 5.81 t/s |
| 242 | 4,942 | 6.54 t/s | 5.11 t/s |
| 243 | 4,959 | 6.54 t/s | 5.61 t/s |
| 244 | 4,978 | 6.54 t/s | 6.13 t/s |
| 245 | 4,996 | 6.54 t/s | 5.96 t/s |
| 246 | 5,014 | 6.53 t/s | 5.66 t/s |
| 247 | 5,029 | 6.53 t/s | 4.93 t/s |
| 248 | 5,045 | 6.52 t/s | 5.20 t/s |
| 249 | 5,063 | 6.52 t/s | 5.85 t/s |
| 250 | 5,080 | 6.51 t/s | 5.59 t/s |
| 251 | 5,098 | 6.51 t/s | 5.92 t/s |
| 252 | 5,116 | 6.51 t/s | 5.78 t/s |
| 253 | 5,134 | 6.51 t/s | 5.73 t/s |
| 254 | 5,153 | 6.50 t/s | 6.19 t/s |
| 255 | 5,171 | 6.50 t/s | 5.84 t/s |
| 256 | 5,188 | 6.50 t/s | 5.62 t/s |
| 257 | 5,205 | 6.50 t/s | 5.66 t/s |
| 258 | 5,224 | 6.50 t/s | 6.28 t/s |
| 259 | 5,243 | 6.49 t/s | 6.12 t/s |
| 260 | 5,262 | 6.49 t/s | 6.25 t/s |
| 261 | 5,280 | 6.49 t/s | 5.89 t/s |
| 262 | 5,298 | 6.49 t/s | 5.84 t/s |
| 263 | 5,316 | 6.49 t/s | 5.91 t/s |
| 264 | 5,336 | 6.49 t/s | 6.38 t/s |
| 265 | 5,355 | 6.48 t/s | 6.18 t/s |
| 266 | 5,373 | 6.48 t/s | 5.92 t/s |
| 267 | 5,391 | 6.48 t/s | 5.94 t/s |
| 268 | 5,409 | 6.48 t/s | 5.98 t/s |

---

## Task #0 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-13 21:15:22.761` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `765` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `94.11 t/s` (`10.63 ms/tok`) | Time To First Token (TTFT) = `6.35s` |
| **Decode Speed (Generation)** | `15.91 t/s` (`62.84 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `598` (78.2%) / Out: `167` (21.8%) | Total context footprint: `765` tokens |
| **Graphs Reused** | `166` | CUDA/execution graph cache hits |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 16.04 t/s | 16.20 t/s |
| 2 | 150 | 16.12 t/s | 16.30 t/s |

---

## Task #168 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-13 21:16:14.606` (Queue Delay: `0.04s`)
* **Total Context Footprint:** `N/A` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `N/A` | Time To First Token (TTFT) = `N/A` |
| **Decode Speed (Generation)** | `N/A` | Autoregressive streaming generation throughput |
| **Tokens Allocation** | Total: `N/A` | Total context footprint: `N/A` tokens |
| **Graphs Reused** | `N/A` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 16.0% | 35.74 | 57.30 |
| 2 | 4,096 | 32.0% | 111.80 | 36.64 |
| 3 | 6,144 | 48.0% | 227.82 | 26.97 |

---

## Task #0 (Slot 0)

* **Model:** `GLM-4.7-Flash-GGUF`
* **Dispatch Time:** `2026-09-13 21:22:49.751` (Queue Delay: `0.03s`)
* **Total Context Footprint:** `19854` tokens

### Key Performance Indicators

| Metric | Value | Architectural Meaning |
|---|---|---|
| **Prefill Speed (Prompt)** | `46.32 t/s` (`21.59 ms/tok`) | Time To First Token (TTFT) = `277.98s` |
| **Decode Speed (Generation)** | `19.98 t/s` (`50.05 ms/tok`) | Autoregressive streaming generation throughput |
| **Tokens Allocation** | In: `12875` (64.8%) / Out: `6979` (35.2%) | Total context footprint: `19854` tokens |
| **Graphs Reused** | `6,951` | CUDA/execution graph cache hits |

### Prefill Scaling Breakdown

| Step | Tokens | Progress | Elapsed (s) | Speed (tok/s) |
|---|---|---|---|---|
| 1 | 2,048 | 16.0% | 6.40 | 320.23 |
| 2 | 4,096 | 32.0% | 24.87 | 164.72 |
| 3 | 6,144 | 48.0% | 56.66 | 108.43 |
| 4 | 8,192 | 64.0% | 101.86 | 80.42 |
| 5 | 10,240 | 80.0% | 160.60 | 63.76 |
| 6 | 12,288 | 95.0% | 233.02 | 52.73 |

### Decode Streaming Breakdown

| Step | Tokens Gen | Cumulative Speed (tg) | Rolling 3s Speed (tg_3s) |
|---|---|---|---|
| 1 | 100 | 21.41 t/s | 21.62 t/s |
| 2 | 170 | 22.09 t/s | 23.15 t/s |
| 3 | 240 | 22.42 t/s | 23.23 t/s |
| 4 | 309 | 22.53 t/s | 22.92 t/s |
| 5 | 377 | 22.55 t/s | 22.64 t/s |
| 6 | 446 | 22.60 t/s | 22.92 t/s |
| 7 | 514 | 22.59 t/s | 22.52 t/s |
| 8 | 583 | 22.62 t/s | 22.82 t/s |
| 9 | 651 | 22.62 t/s | 22.60 t/s |
| 10 | 719 | 22.61 t/s | 22.50 t/s |
| 11 | 787 | 22.60 t/s | 22.58 t/s |
| 12 | 854 | 22.58 t/s | 22.29 t/s |
| 13 | 922 | 22.57 t/s | 22.46 t/s |
| 14 | 989 | 22.54 t/s | 22.20 t/s |
| 15 | 1,056 | 22.52 t/s | 22.11 t/s |
| 16 | 1,124 | 22.51 t/s | 22.34 t/s |
| 17 | 1,191 | 22.48 t/s | 22.09 t/s |
| 18 | 1,258 | 22.46 t/s | 22.11 t/s |
| 19 | 1,324 | 22.43 t/s | 21.81 t/s |
| 20 | 1,390 | 22.40 t/s | 21.82 t/s |
| 21 | 1,457 | 22.38 t/s | 22.05 t/s |
| 22 | 1,522 | 22.34 t/s | 21.51 t/s |
| 23 | 1,588 | 22.32 t/s | 21.70 t/s |
| 24 | 1,653 | 22.29 t/s | 21.58 t/s |
| 25 | 1,718 | 22.26 t/s | 21.64 t/s |
| 26 | 1,783 | 22.24 t/s | 21.60 t/s |
| 27 | 1,848 | 22.21 t/s | 21.43 t/s |
| 28 | 1,913 | 22.19 t/s | 21.60 t/s |
| 29 | 1,977 | 22.15 t/s | 21.24 t/s |
| 30 | 2,041 | 22.12 t/s | 21.14 t/s |
| 31 | 2,106 | 22.10 t/s | 21.37 t/s |
| 32 | 2,170 | 22.06 t/s | 21.07 t/s |
| 33 | 2,234 | 22.04 t/s | 21.25 t/s |
| 34 | 2,297 | 22.01 t/s | 20.88 t/s |
| 35 | 2,361 | 21.98 t/s | 21.02 t/s |
| 36 | 2,425 | 21.96 t/s | 21.10 t/s |
| 37 | 2,488 | 21.93 t/s | 20.91 t/s |
| 38 | 2,552 | 21.91 t/s | 21.10 t/s |
| 39 | 2,615 | 21.88 t/s | 20.79 t/s |
| 40 | 2,678 | 21.85 t/s | 20.73 t/s |
| 41 | 2,742 | 21.83 t/s | 21.02 t/s |
| 42 | 2,804 | 21.80 t/s | 20.48 t/s |
| 43 | 2,867 | 21.77 t/s | 20.69 t/s |
| 44 | 2,928 | 21.74 t/s | 20.24 t/s |
| 45 | 2,990 | 21.71 t/s | 20.52 t/s |
| 46 | 3,052 | 21.69 t/s | 20.54 t/s |
| 47 | 3,114 | 21.66 t/s | 20.37 t/s |
| 48 | 3,176 | 21.64 t/s | 20.58 t/s |
| 49 | 3,237 | 21.61 t/s | 20.27 t/s |
| 50 | 3,298 | 21.58 t/s | 20.08 t/s |
| 51 | 3,359 | 21.55 t/s | 20.05 t/s |
| 52 | 3,419 | 21.52 t/s | 19.90 t/s |
| 53 | 3,480 | 21.49 t/s | 20.21 t/s |
| 54 | 3,540 | 21.46 t/s | 19.75 t/s |
| 55 | 3,600 | 21.43 t/s | 19.87 t/s |
| 56 | 3,661 | 21.41 t/s | 20.10 t/s |
| 57 | 3,721 | 21.38 t/s | 19.74 t/s |
| 58 | 3,781 | 21.35 t/s | 19.93 t/s |
| 59 | 3,841 | 21.33 t/s | 19.71 t/s |
| 60 | 3,900 | 21.30 t/s | 19.62 t/s |
| 61 | 3,960 | 21.28 t/s | 19.95 t/s |
| 62 | 4,019 | 21.25 t/s | 19.59 t/s |
| 63 | 4,078 | 21.22 t/s | 19.66 t/s |
| 64 | 4,137 | 21.20 t/s | 19.44 t/s |
| 65 | 4,196 | 21.17 t/s | 19.42 t/s |
| 66 | 4,255 | 21.14 t/s | 19.36 t/s |
| 67 | 4,312 | 21.11 t/s | 18.93 t/s |
| 68 | 4,371 | 21.09 t/s | 19.52 t/s |
| 69 | 4,429 | 21.06 t/s | 19.19 t/s |
| 70 | 4,487 | 21.03 t/s | 19.18 t/s |
| 71 | 4,546 | 21.01 t/s | 19.38 t/s |
| 72 | 4,604 | 20.98 t/s | 19.01 t/s |
| 73 | 4,662 | 20.96 t/s | 19.31 t/s |
| 74 | 4,720 | 20.93 t/s | 19.01 t/s |
| 75 | 4,777 | 20.91 t/s | 18.94 t/s |
| 76 | 4,835 | 20.88 t/s | 19.13 t/s |
| 77 | 4,892 | 20.86 t/s | 18.90 t/s |
| 78 | 4,950 | 20.84 t/s | 19.14 t/s |
| 79 | 5,007 | 20.81 t/s | 18.79 t/s |
| 80 | 5,064 | 20.78 t/s | 18.75 t/s |
| 81 | 5,121 | 20.76 t/s | 18.92 t/s |
| 82 | 5,177 | 20.74 t/s | 18.66 t/s |
| 83 | 5,234 | 20.71 t/s | 18.88 t/s |
| 84 | 5,290 | 20.69 t/s | 18.62 t/s |
| 85 | 5,346 | 20.66 t/s | 18.50 t/s |
| 86 | 5,403 | 20.64 t/s | 18.71 t/s |
| 87 | 5,459 | 20.62 t/s | 18.51 t/s |
| 88 | 5,516 | 20.60 t/s | 18.73 t/s |
| 89 | 5,572 | 20.57 t/s | 18.41 t/s |
| 90 | 5,627 | 20.55 t/s | 18.31 t/s |
| 91 | 5,683 | 20.52 t/s | 18.48 t/s |
| 92 | 5,738 | 20.50 t/s | 18.30 t/s |
| 93 | 5,794 | 20.48 t/s | 18.43 t/s |
| 94 | 5,849 | 20.45 t/s | 18.19 t/s |
| 95 | 5,904 | 20.43 t/s | 18.10 t/s |
| 96 | 5,960 | 20.41 t/s | 18.38 t/s |
| 97 | 6,015 | 20.38 t/s | 18.17 t/s |
| 98 | 6,071 | 20.36 t/s | 18.33 t/s |
| 99 | 6,125 | 20.34 t/s | 17.88 t/s |
| 100 | 6,179 | 20.31 t/s | 17.92 t/s |
| 101 | 6,234 | 20.29 t/s | 18.08 t/s |
| 102 | 6,288 | 20.27 t/s | 17.83 t/s |
| 103 | 6,343 | 20.25 t/s | 18.05 t/s |
| 104 | 6,397 | 20.22 t/s | 17.74 t/s |
| 105 | 6,451 | 20.20 t/s | 17.71 t/s |
| 106 | 6,505 | 20.18 t/s | 17.83 t/s |
| 107 | 6,559 | 20.15 t/s | 17.72 t/s |
| 108 | 6,613 | 20.13 t/s | 17.86 t/s |
| 109 | 6,666 | 20.11 t/s | 17.54 t/s |
| 110 | 6,719 | 20.09 t/s | 17.57 t/s |
| 111 | 6,773 | 20.06 t/s | 17.80 t/s |
| 112 | 6,826 | 20.04 t/s | 17.50 t/s |
| 113 | 6,880 | 20.02 t/s | 17.74 t/s |
| 114 | 6,933 | 20.00 t/s | 17.48 t/s |

---

