# Post-hoc metrics on the test split (n=176)

Post-hoc, computed after scoring; not used for any selection. Not part of the pre-registered metric list. Point estimates only (no confidence intervals). Computed from the stored `predictions_test.jsonl` of each run; invalid outputs count as a wrong prediction (no class predicted). Severity macro-F1 averages over the severity classes present in the gold labels (low, medium, high, unknown).

## Severity macro-F1

| run | severity macro-F1 |
|---|---|
| gemma3-1b-zeroshot | 0.20 |
| gemma3-1b-fewshot | 0.25 |
| gemma3-1b-lora-n50 | 0.46 |
| gemma3-1b-lora-n100 | 0.53 |
| gemma3-1b-lora-n207 | 0.44 |
| gemma3-1b-4bit-lora-n207 | 0.43 |
| qwen2.5-1.5b-zeroshot | 0.27 |
| qwen2.5-1.5b-fewshot | 0.44 |
| qwen2.5-1.5b-lora-n207 | 0.45 |

## Per-class incident-type precision / recall / F1

Cells are `precision / recall / F1`. `n/a` means the quantity is undefined (no predictions of that class for precision). Gold support per class (test): vehicle_breakdown 22, road_accident 23, road_hazard 21, flooding 24, road_closure 23, heavy_traffic 23, other 20, unknown 20.

| run | vehicle_breakdown | road_accident | road_hazard | flooding | road_closure | heavy_traffic | other | unknown |
|---|---|---|---|---|---|---|---|---|
| gemma3-1b-zeroshot | 0.40 / 0.45 / 0.43 | 0.00 / 0.00 / 0.00 | 0.33 / 0.14 / 0.20 | 1.00 / 0.04 / 0.08 | 0.50 / 0.09 / 0.15 | 1.00 / 0.09 / 0.16 | n/a / 0.00 / 0.00 | n/a / 0.00 / 0.00 |
| gemma3-1b-fewshot | 0.40 / 0.18 / 0.25 | 0.25 / 0.04 / 0.07 | 0.71 / 0.24 / 0.36 | 1.00 / 0.33 / 0.50 | 0.67 / 0.17 / 0.28 | 0.00 / 0.00 / 0.00 | 0.00 / 0.00 / 0.00 | 0.62 / 0.40 / 0.48 |
| gemma3-1b-lora-n50 | 0.80 / 0.18 / 0.30 | 0.32 / 0.74 / 0.45 | 0.36 / 0.81 / 0.50 | 0.88 / 0.58 / 0.70 | 0.85 / 0.48 / 0.61 | 0.80 / 0.35 / 0.48 | 0.30 / 0.15 / 0.20 | 0.62 / 0.65 / 0.63 |
| gemma3-1b-lora-n100 | 0.77 / 0.45 / 0.57 | 0.68 / 0.57 / 0.62 | 0.37 / 0.76 / 0.50 | 0.88 / 0.58 / 0.70 | 0.56 / 0.65 / 0.60 | 0.57 / 0.57 / 0.57 | 0.38 / 0.30 / 0.33 | 0.71 / 0.60 / 0.65 |
| gemma3-1b-lora-n207 | 0.70 / 0.86 / 0.78 | 0.55 / 0.78 / 0.64 | 0.50 / 0.86 / 0.63 | 0.94 / 0.71 / 0.81 | 0.53 / 0.70 / 0.60 | 0.72 / 0.57 / 0.63 | 0.75 / 0.15 / 0.25 | 0.88 / 0.35 / 0.50 |
| gemma3-1b-4bit-lora-n207 | 0.64 / 0.82 / 0.72 | 0.53 / 0.74 / 0.62 | 0.36 / 0.90 / 0.51 | 0.91 / 0.42 / 0.57 | 0.59 / 0.74 / 0.65 | 0.71 / 0.52 / 0.60 | 0.50 / 0.05 / 0.09 | 1.00 / 0.15 / 0.26 |
| qwen2.5-1.5b-zeroshot | 0.28 / 0.91 / 0.43 | 0.36 / 0.17 / 0.24 | 0.22 / 0.43 / 0.29 | 1.00 / 0.08 / 0.15 | 0.88 / 0.30 / 0.45 | 0.74 / 0.61 / 0.67 | n/a / 0.00 / 0.00 | 0.86 / 0.30 / 0.44 |
| qwen2.5-1.5b-fewshot | 0.50 / 0.64 / 0.56 | 0.80 / 0.35 / 0.48 | 0.24 / 0.76 / 0.36 | 1.00 / 0.25 / 0.40 | 0.81 / 0.57 / 0.67 | 0.68 / 0.65 / 0.67 | 0.67 / 0.20 / 0.31 | 0.56 / 0.50 / 0.53 |
| qwen2.5-1.5b-lora-n207 | 0.83 / 0.68 / 0.75 | 0.47 / 0.83 / 0.60 | 0.40 / 0.81 / 0.54 | 1.00 / 0.42 / 0.59 | 0.75 / 0.78 / 0.77 | 0.81 / 0.74 / 0.77 | 0.78 / 0.35 / 0.48 | 0.91 / 0.50 / 0.65 |
