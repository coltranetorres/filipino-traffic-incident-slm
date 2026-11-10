# Alias-coverage sensitivity of test location F1

Post-hoc, computed after scoring; not used for any selection. The pre-registered numbers (`data/aliases.json`) remain the ones in the main tables. Here the same stored predictions are re-scored in memory with seven extra bare-name road aliases (listed below); the 95% CI is the same bootstrap (1000 resamples, seed 0) as in the main tables. The `pre-registered` column reproduces `results_test.json` exactly (checked by the script).

Extra aliases (canonical road <- alias): Commonwealth Avenue <- Commonwealth; Shaw Boulevard <- Shaw; Recto Avenue <- Recto; Ortigas Avenue <- Ortigas; Marcos Highway <- Marcos; Kalayaan Avenue <- Kalayaan; McArthur Highway <- McArthur. Extended alias file: `results/aliases_extended_posthoc.json`.

| run | location F1, pre-registered aliases | location F1, extended aliases | change |
|---|---|---|---|
| gemma3-1b-zeroshot | 0.20 [0.14, 0.27] | 0.21 [0.15, 0.28] | +0.012 |
| gemma3-1b-fewshot | 0.18 [0.12, 0.25] | 0.23 [0.16, 0.30] | +0.044 |
| gemma3-1b-lora-n50 | 0.63 [0.57, 0.69] | 0.64 [0.58, 0.69] | +0.004 |
| gemma3-1b-lora-n100 | 0.71 [0.66, 0.77] | 0.72 [0.66, 0.77] | +0.004 |
| gemma3-1b-lora-n207 | 0.72 [0.66, 0.77] | 0.72 [0.66, 0.77] | +0.000 |
| gemma3-1b-4bit-lora-n207 | 0.73 [0.67, 0.79] | 0.73 [0.67, 0.79] | +0.000 |
| qwen2.5-1.5b-zeroshot | 0.45 [0.39, 0.51] | 0.48 [0.43, 0.54] | +0.034 |
| qwen2.5-1.5b-fewshot | 0.64 [0.57, 0.70] | 0.70 [0.64, 0.76] | +0.064 |
| qwen2.5-1.5b-lora-n207 | 0.79 [0.74, 0.84] | 0.80 [0.75, 0.84] | +0.008 |

## Interval separation, LoRA n207 vs few-shot (same model)

| comparison | pre-registered aliases | extended aliases |
|---|---|---|
| gemma3-1b LoRA n207 vs few-shot | separated (CIs do not overlap) | separated (CIs do not overlap) |
| qwen2.5-1.5b LoRA n207 vs few-shot | separated (CIs do not overlap) | not separated (CIs overlap) |
