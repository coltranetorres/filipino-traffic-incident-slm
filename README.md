# filipino-traffic-incident-slm

Study of whether a small language model (Gemma 3 1B, Qwen2.5 1.5B), fine-tuned with LoRA, can extract structured
information (incident type, location, severity, road obstruction, language) from synthetic Filipino, English and
Taglish traffic reports, compared with zero-shot and few-shot prompting of the same models. Runs locally with MLX on
Apple silicon. One seed, synthetic data; see `research/findings.md` for results and limits.

## Research question

> Can a relatively small language model (1-4B parameters), fine-tuned on Filipino, English, and Taglish traffic
> incident reports, achieve structured incident understanding while remaining efficient enough to run locally?

Hypothesis, stated before any experiment: LoRA fine-tuning improves structured incident classification and location
extraction over zero-shot and few-shot prompting of the same model, at an inference cost low enough to run locally.

## Summary of findings

Test split, n=176, scored once per run; single seed; synthetic data; 95% bootstrap CIs (details and limits in
`research/findings.md`).

| run | JSON valid | Incident macro-F1 | Severity acc | Obstruction acc | Language acc | Location F1 | Abstention | median latency ms | peak mem GB |
|---|---|---|---|---|---|---|---|---|---|
| gemma3-1b-zeroshot | 0.24 | 0.13 | 0.15 | 0.13 | 0.20 | 0.20 | 0.08 | 725 | 2.86 |
| gemma3-1b-fewshot | 0.28 | 0.24 | 0.18 | 0.16 | 0.16 | 0.18 | 0.25 | 584 | 3.05 |
| gemma3-1b-lora-n50 | 0.99 | 0.48 | 0.52 | 0.51 | 0.43 | 0.63 | 0.92 | 617 | 3.15 |
| gemma3-1b-lora-n100 | 0.99 | 0.57 | 0.57 | 0.57 | 0.77 | 0.71 | 0.90 | 617 | 3.15 |
| gemma3-1b-lora-n207 | 0.99 | 0.61 | 0.48 | 0.55 | 0.77 | 0.72 | 0.93 | 643 | 3.15 |
| gemma3-1b-4bit-lora-n207 | 0.99 | 0.50 | 0.45 | 0.49 | 0.76 | 0.73 | 0.92 | 387 | 1.32 |
| qwen2.5-1.5b-zeroshot | 0.91 | 0.33 | 0.32 | 0.26 | 0.29 | 0.45 | 0.45 | 1099 | 3.34 |
| qwen2.5-1.5b-fewshot | 0.98 | 0.50 | 0.47 | 0.24 | 0.63 | 0.64 | 0.88 | 850 | 3.50 |
| qwen2.5-1.5b-lora-n207 | 0.99 | 0.64 | 0.52 | 0.57 | 0.85 | 0.79 | 0.90 | 861 | 3.71 |

Point estimates; the 95% intervals are in `research/findings.md` section 4.1.

- **Format reliability.** Prompting alone is unreliable for Gemma 3 1B (valid JSON in 24% of zero-shot and 28% of
  few-shot outputs). After LoRA, every fine-tuned run reaches 0.99 JSON validity. Qwen2.5 1.5B few-shot is already
  98% valid.
- **Fine-tuning vs prompting.** Gemma 3 1B LoRA beats its few-shot baseline on every task with non-overlapping
  intervals (incident macro-F1 0.61 vs 0.24, location F1 0.72 vs 0.18), though that baseline is mostly invalid
  output, so format and task effects are mixed. For Qwen2.5 1.5B, LoRA clearly beats few-shot on obstruction
  (0.57 vs 0.24) and language (0.85 vs 0.63); incident type is borderline (0.64 vs 0.50), and severity (0.52 vs 0.47)
  and abstention are not separated. Qwen's location gain (0.79 vs 0.64) disappears under extended road-name aliases.
- **Absolute level is moderate.** Best run (Qwen LoRA): incident macro-F1 0.64, severity 0.52, obstruction 0.57,
  language 0.85, location F1 0.79, abstention 0.90. Severity and obstruction stay around 0.5 to 0.6.
- **No model ranking.** Gemma 1B and Qwen 1.5B intervals overlap on every task. Gemma led on validation and the order
  reversed on test.
- **More data.** Gemma incident macro-F1 rises 0.48, 0.57, 0.61 for 50, 100, 207 training items (intervals overlap);
  only language accuracy clearly improves (0.43 to 0.77 between 50 and 100). Severity is not monotone.
- **Efficiency.** Everything runs locally on a MacBook M4 (median latency 0.4 to 0.9 s per report, 1.3 to 3.7 GB peak
  memory); LoRA training takes 3 to 4 minutes. 4-bit Gemma uses about 40% less latency and 58% less memory, with
  lower point estimates (incident macro-F1 0.50 vs 0.61) that the intervals do not separate.
- **English not harmed.** No drop on English after fine-tuning was seen (n=28, so small drops cannot be ruled out).
- **Caveats.** Synthetic data, 207 training items, one seed, one machine, untuned baselines, and no 4B model tested.

## Conclusion

**Partly yes, with limits.** On our synthetic test set, 1B to 1.5B models fine-tuned with LoRA do reach usable
structured output and run comfortably on a laptop. Both fine-tuned models produce valid JSON 99% of the time (against
24% to 28% for prompted Gemma 3 1B) and clearly outperform prompting of the same model on several tasks, which
supports the hypothesis for Gemma on every task and for Qwen on obstruction and language, but only weakly for Qwen on
incident type, and not for Qwen on severity. Inference needs 1.3 to 3.7 GB of memory and under a second per report,
so "efficient enough to run locally" holds as measured on one MacBook M4.

"Structured incident understanding" is only partly achieved: incident type (macro-F1 about 0.6), severity and
obstruction (about 0.5 to 0.6) are moderate, while language (0.77 to 0.85), location (0.72 to 0.79) and abstention
(about 0.9) are stronger. We cannot say which of the two models is better, that more data helps every task, or that
4-bit quantization costs accuracy (its lower scores are not statistically separated). Because the data is synthetic,
small (207 training items), and run with a single seed, these results show that the approach is feasible, not that it
is reliable on real Filipino traffic reports. The 4B end of the "1-4B" range was not tested.

**Hypothesis check.** The hypothesis was that LoRA fine-tuning improves structured incident classification and
location extraction over zero-shot and few-shot prompting of the same model, at a local inference cost. It is
**largely supported**:

| part of the hypothesis | Gemma 3 1B | Qwen2.5 1.5B |
|---|---|---|
| better than zero-shot | yes, on every task | yes, on every task |
| better than few-shot, incident type | yes (0.61 vs 0.24) | borderline (0.64 vs 0.50) |
| better than few-shot, location | yes (0.72 vs 0.18) | not robust: the gain (0.79 vs 0.64) disappears under extended road-name aliases |
| low enough cost to run locally | yes (0.4 to 0.6 s, 1.3 to 3.2 GB) | yes (0.9 s, 3.7 GB) |

The Gemma few-shot baseline is mostly invalid JSON, so part of its gap is a format effect and not only a task effect.
"Supported" means the measured differences point the hypothesized way on this synthetic test set. It does not mean
the hypothesis is proven, and it says nothing about real-world reports.

## Setup

```
uv sync
uv run pytest -q
```

Models are downloaded from Hugging Face on first use (nothing is bundled). Model ids are in
`experiments/models.json`:

| key | Hugging Face id |
|---|---|
| gemma3-1b | `mlx-community/gemma-3-1b-it-bf16` |
| qwen2.5-1.5b | `mlx-community/Qwen2.5-1.5B-Instruct-bf16` |
| gemma3-1b-4bit | `mlx-community/gemma-3-1b-it-4bit` |

The revisions are not pinned, so a re-download may fetch a newer snapshot of a model repository.

## Data

`data/processed/{train,validation,test}.jsonl` (207 / 40 / 176 items, all synthetic) with sha256 checksums and class
counts in `data/processed/MANIFEST.json`. `trafficslm.data.verify_manifest()` checks them, and the test-split
path calls it. `data/aliases.json` is the road-name alias list used when scoring locations. Label rules are in
`docs/annotation-guidelines.md`; `data/annotations/` holds the annotation batch files.

## Reproduction order

All commands run from the repo root. Runs are written to `experiments/<run>/`.

1. Zero-shot and few-shot baselines on validation (merges model ids into `experiments/models.json`):
   `uv run python scripts/run_baselines.py`
2. LoRA runs, per run name in `scripts/run_lora.py` (`gemma3-1b-lora-n50`, `gemma3-1b-lora-n100`,
   `gemma3-1b-lora-n207`, `qwen2.5-1.5b-lora-n207`, `gemma3-1b-4bit-lora-n207`):
   `uv run python scripts/run_lora.py train <run>` then `uv run python scripts/run_lora.py eval <run>`;
   `uv run python scripts/run_lora.py table` writes `experiments/lora_validation.md`.
3. Model selection on validation only: `research/selection.md` (written before any test run).
4. Test predictions for the nine declared runs, one process each:
   `uv run python scripts/run_test.py all` (or `one <run>`).
5. Score each run on the test split, once, through the guard:
   `uv run python -m trafficslm.evaluate --run experiments/<run> --split test --final`
6. Reports and tables (read stored files only, no model is loaded):
   - `uv run python scripts/make_reports.py` regenerates `results/summary*.md|png` and `results/errors_<run>.md`.
   - `uv run python scripts/make_findings_tables.py [table ...]` prints the tables used in `research/findings.md`.
   - Post-hoc analyses (computed after scoring, not used for any selection):
     `uv run python scripts/alias_sensitivity.py`, `scripts/posthoc_metrics.py`, `scripts/check_leakage.py`
     (write `results/alias_sensitivity_test.md`, `results/posthoc_metrics_test.md`, `results/leakage_check.md`).

`scripts/smoke_infer.py OUT_DIR [model_id] [--few]` is a 3-item smoke check.

## Committed and ignored

Committed: code, data, predictions (`predictions*.jsonl`), `results*.json`, `meta*.json`, tables and write-ups.
Not committed (git-ignored): LoRA adapters (`experiments/*/adapters/`, about 15 MB per weights file, 31 MB per run
folder), `experiments/*/mlx_data/`, `experiments/*/train.log`. Retraining is needed to recreate adapters, and the
test-time inference scripts need them for the LoRA runs.

## Freeze rule and test guard

After `research/selection.md` was committed, no model, prompt, adapter or hyperparameter was changed. The test split
is scored once per declared run: `trafficslm.evaluate` refuses `--split test` without `--final`, and refuses a run
already listed in `experiments/test_runs.log`. Do not edit `data/processed/*`, `data/aliases.json`, stored
predictions, `results*.json` or `meta*.json`; post-hoc analyses go to new files under `results/`.

## Where to read more

- `research/findings.md`: results, limitations, next steps.
- `research/selection.md`: validation-based selection and the declared test plan.
- `docs/annotation-guidelines.md`: label definitions.
- `docs/superpowers/specs/2026-11-10-filipino-traffic-slm-design.md` and `docs/superpowers/plans/`: design and plan.
