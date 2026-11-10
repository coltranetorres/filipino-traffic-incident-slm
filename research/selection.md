# Model selection (validation only, written before any test run)

All numbers are on the validation split (n=40), value with 95% CI, from `experiments/*/results.json`.
No test-split result exists at the time of writing (`experiments/test_runs.log` does not exist).

## 1. Best fine-tuned configuration per model family

Rule: highest validation incident macro-F1 (primary); ties broken by severity accuracy, then smaller n_train.

- **Gemma 3 1B: `gemma3-1b-lora-n207`** (16-bit base, full train split). Incident macro-F1 0.77 [0.58, 0.90],
  severity acc 0.72 [0.57, 0.85], JSON validity 1.00. Alternatives: n100 0.58 / 0.70, n50 0.42 / 0.68, and the
  4-bit LoRA `gemma3-1b-4bit-lora-n207` 0.46 / 0.60. n207 has the highest primary metric with no tie.
- **Qwen2.5 1.5B: `qwen2.5-1.5b-lora-n207`** (the only fine-tuned Qwen run). Incident macro-F1 0.60 [0.38, 0.74],
  severity acc 0.62 [0.45, 0.78], JSON validity 1.00. Note that Qwen few-shot (0.57 / 0.53) is not a fine-tuned
  configuration and is not eligible here; it is scored as a baseline.

## 2. Declared test plan (Task 9): each configuration scored exactly once on the test split

| # | Run folder | Why |
|---|---|---|
| 1 | `gemma3-1b-zeroshot` | baseline |
| 2 | `gemma3-1b-fewshot` | baseline |
| 3 | `gemma3-1b-lora-n207` | best Gemma LoRA (also the n=207 point of the data-size curve) |
| 4 | `qwen2.5-1.5b-zeroshot` | baseline |
| 5 | `qwen2.5-1.5b-fewshot` | baseline |
| 6 | `qwen2.5-1.5b-lora-n207` | best Qwen LoRA |
| 7 | `gemma3-1b-lora-n50` | data-size curve |
| 8 | `gemma3-1b-lora-n100` | data-size curve |
| 9 | `gemma3-1b-4bit-lora-n207` | quantization comparison |

Nine runs in total. The optional Gemma 3 4B comparison is skipped (controller ruling), so it is not in the plan.

## 3. Freeze rule

After this file is committed, no model, prompt, adapter, or hyperparameter changes are made. The test split is run
once per listed run, through the guard with `--final`. Any failure of a listed run is reported as is, not re-tuned.

## 4. Caveats

- Validation has n=40, so CIs are wide (incident macro-F1 CIs span roughly 0.3 to 0.35 in width). Gemma n207 vs Qwen
  n207 (0.77 vs 0.60) have overlapping CIs; the choice of best config within each family is a point-estimate
  ranking, and gaps within CI are not claimed as wins.
- The Gemma n100 vs n207 and 16-bit vs 4-bit differences should be read with the same caution; the 4-bit drop
  (0.77 to 0.46 F1) is the largest gap but a single seed and n=40 limit what can be concluded.
- Validation subsets (language, tags) have 2 to 17 items; subset scores are descriptive only.
- All runs use one seed (0); no variance across seeds is estimated.
