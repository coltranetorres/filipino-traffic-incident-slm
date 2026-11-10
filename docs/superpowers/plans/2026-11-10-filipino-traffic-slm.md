# Filipino Traffic Incident SLM Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the pipeline that scores zero-shot, few-shot and LoRA-fine-tuned small models on structured Filipino/Taglish traffic-report understanding, and produces the per-task results tables for the write-up.

**Architecture:** A small Python package (`trafficslm`) with one module per responsibility: schema, data loading, prompts, inference, metrics, evaluation, training wrapper, reporting. Every model (base or LoRA) is run through the same prompt and the same evaluator. The test split is guarded so it can be scored once per configuration.

**Tech Stack:** `uv` as the runtime and package manager (Python 3.12, project venv in `.venv`, lockfile `uv.lock`), `mlx-lm` (LoRA + generation on Apple Silicon), Pydantic 2, pytest, matplotlib. No sklearn: metrics are implemented in `metrics.py`. All commands in this plan run through `uv run` (e.g. `uv run pytest`, `uv run python -m trafficslm.evaluate`); never call the system `python3` (3.9.6) directly.

**Spec:** `docs/superpowers/specs/2026-11-10-filipino-traffic-slm-design.md` (approved 2026-11-10). Label rules: `docs/annotation-guidelines.md`. Data: `data/processed/{train,validation,test}.jsonl` plus `MANIFEST.json`.

## Global Constraints

- Hardware: MacBook M4, 24 GB unified memory. LoRA on 16-bit weights is the main method; one extra 4-bit (quantized base) LoRA run is a comparison.
- Models: Gemma 3 1B and Qwen2.5 1.5B Instruct (main pair); Gemma 3 4B optional. Substitution (e.g. Qwen2.5 3B, Llama 3.2) is allowed if one fails in MLX-LM.
- Output schema (one JSON object per report): `incident_type` ∈ {vehicle_breakdown, road_accident, road_hazard, flooding, road_closure, heavy_traffic, other, unknown}; `location` {`road`, `landmark`, `direction`} (strings or null; direction ∈ northbound/southbound/eastbound/westbound/null); `severity` ∈ {low, medium, high, unknown}; `road_obstruction` ∈ {none, partial, full, unknown}; `language` ∈ {filipino, english, taglish}.
- Report separate scores per task; no combined score drives conclusions. If a headline number is shown it is the unweighted mean of task scores, labeled secondary.
- Metrics: incident type macro-F1 (also without `unknown`); severity accuracy; obstruction accuracy; language accuracy; location field-level F1 on road/landmark/direction; JSON validity; abstention rate on missing location fields; latency and peak memory. Every score has a 95% bootstrap CI (1000 resamples, seed 0).
- Location scoring: normalized match (lowercase, accents stripped, `ave`→`avenue`, `blvd`→`boulevard`, `hwy`/`hway`→`highway`, alias map in `data/aliases.json`). null predicted for null gold is correct.
- Few-shot baseline: k = 5, drawn from train only, fixed seed, unconstrained decoding. Decoding is greedy (temperature 0).
- Model and hyperparameter choices use the validation split only. The test split (176 items, checksummed in `MANIFEST.json`) is never changed and is scored once per chosen configuration.
- Training data stays at 207 items for now; it grows only if results call for it (the test split never changes).
- Test subsets reported separately: language (filipino/taglish/english) and tags `noisy`, `no_location`, `short`, `ambiguous`, `contradictory`.
- The project directory is not a git repository. Task 1 offers `git init`; if declined, skip commit steps.

## Review Focus

1. Model wraps its JSON in ```` ```json ```` fences or adds prose before/after it → the object must still be parsed. Pinned in Task 1.
2. Model emits an enum value outside the label set, extra keys, or the string `"null"`/`""` for a missing field → invalid or normalized to null; never crashes scoring. Pinned in Tasks 1 and 3.
3. Generation never emits an end token and the JSON is truncated → counted invalid, bounded by `max_tokens`. Pinned in Task 4.
4. A subset has 0 or 1 items (e.g. a tag filter) → metrics return `nan`, not an exception. Pinned in Tasks 3 and 5.
5. The test split is scored by accident, or twice for one run → refused. Pinned in Task 5.

---

## File Structure

```
pyproject.toml / uv.lock              uv-managed deps, pytest config (pythonpath = src)
src/trafficslm/schema.py              enums, Pydantic models, parse_report
src/trafficslm/data.py                split loading, manifest check, stratified subsets
src/trafficslm/prompts.py             system prompt, message builder, MLX dataset writer
src/trafficslm/metrics.py             normalization, F1/accuracy, location, bootstrap CI
src/trafficslm/evaluate.py            scoring a predictions file, subsets, test guard, CLI
src/trafficslm/infer.py               prediction runner + MLX generator
src/trafficslm/train.py               wrapper around `mlx_lm lora`
src/trafficslm/report.py              results table + chart
src/trafficslm/errors.py              error analysis markdown
data/aliases.json                     road alias map
experiments/<run>/                    predictions.jsonl, meta.json, results.json, adapters/
research/findings.md                  write-up (Task 9)
tests/                                one test file per module
```

---

### Task 1: Environment and schema

**Files:**
- Create: `pyproject.toml`, `uv.lock` (both produced by uv), `src/trafficslm/__init__.py`, `src/trafficslm/schema.py`, `tests/test_schema.py`

**Interfaces:**
- Produces: `INCIDENT_TYPES, SEVERITIES, OBSTRUCTIONS, LANGUAGES, DIRECTIONS` (tuples of str); `Location(road: str|None, landmark: str|None, direction: str|None)`; `Report(incident_type, location: Location, severity, road_obstruction, language)`; `Record(Report fields + id: str, split: str, text: str, tags: list[str])` with `Record.target() -> Report`; `parse_report(raw: str) -> Report | None`.

- [ ] **Step 1:** In the project root run `uv init --package --name trafficslm --python 3.12` (keep the `src/trafficslm` layout; delete any sample code uv generates), then `uv add mlx-lm "pydantic>=2" matplotlib` and `uv add --dev pytest`. Set `[tool.pytest.ini_options] pythonpath = ["src"]` in `pyproject.toml`. Confirm `uv run python -c "import mlx_lm, pydantic"` works. Offer `git init` here (ignore `.venv/`, `experiments/*/adapters/`).
- [ ] **Step 2: Write failing tests** in `tests/test_schema.py`: `test_parse_plain_json` (valid object → `Report`), `test_parse_fenced_json` (```` ```json {...} ``` ```` → `Report`), `test_parse_with_prose` (`"Here: {...} done"` → `Report`), `test_parse_invalid_enum_returns_none` (`incident_type="crash"` → `None`), `test_parse_extra_key_returns_none`, `test_parse_truncated_returns_none`, `test_null_string_becomes_none` (`"road": "null"` and `""` → `None`), `test_every_processed_record_validates` (all 423 rows across the three `.jsonl` files load as `Record`).
- [ ] **Step 3:** Run `uv run pytest tests/test_schema.py -v`; expect failures (module missing).
- [ ] **Step 4: Implement** `schema.py` per the Interfaces. `parse_report` takes the first balanced `{...}` after stripping fences, validates strictly (`extra="forbid"`), returns `None` on any error.
- [ ] **Step 5:** Run `uv run pytest tests/test_schema.py -v`; expect all pass.

### Task 2: Data loading and prompts

**Files:**
- Create: `src/trafficslm/data.py`, `src/trafficslm/prompts.py`, `tests/test_data.py`, `tests/test_prompts.py`

**Interfaces:**
- Consumes: `Record`, `Report` from Task 1.
- Produces: `load_split(name: str, root: Path = Path("data/processed")) -> list[Record]`; `verify_manifest(root: Path = Path("data/processed")) -> None` (raises `ValueError` on checksum or count mismatch); `stratified_subset(records: list[Record], n: int, seed: int = 0) -> list[Record]`; `SYSTEM_PROMPT: str`; `build_messages(text: str, shots: Sequence[Record] = ()) -> list[dict]`; `target_json(rec: Record) -> str`; `pick_shots(train: list[Record], k: int = 5, seed: int = 0) -> list[Record]`; `write_mlx_dataset(train: list[Record], valid: list[Record], out_dir: Path) -> None`.

- [ ] **Step 1: Write failing tests.** `test_split_sizes` (207/40/176), `test_verify_manifest_passes`, `test_verify_manifest_detects_edit` (copy data to tmp, append a space, expect `ValueError`), `test_stratified_subset_deterministic_and_covers_classes` (n=50 → 50 items, all 8 classes present, same result for same seed), `test_build_messages_zero_shot` (roles `system, user`), `test_build_messages_few_shot` (k shots → `system` + k×(`user`,`assistant`) + `user`), `test_pick_shots_distinct_classes` (5 shots, 5 distinct `incident_type`, all from train), `test_target_json_round_trips` (`parse_report(target_json(r)) == r.target()`), `test_write_mlx_dataset` (files `train.jsonl`, `valid.jsonl`, each line `{"messages":[system,user,assistant]}`).
- [ ] **Step 2:** Run the two test files; expect failures.
- [ ] **Step 3: Implement.** `SYSTEM_PROMPT` lists the exact label sets from Global Constraints, states that severity is based on reported impact only, that missing information must be `null`/`unknown` and never invented, and that the answer is a single JSON object. `target_json` uses fixed key order, compact separators, `ensure_ascii=False`.
- [ ] **Step 4:** Run both test files; expect pass.

### Task 3: Metrics

**Files:**
- Create: `src/trafficslm/metrics.py`, `data/aliases.json`, `tests/test_metrics.py`

**Interfaces:**
- Produces: `normalize(s: str | None) -> str | None`; `accuracy(gold: list[str], pred: list[str | None]) -> float`; `macro_f1(gold: list[str], pred: list[str | None], exclude: frozenset[str] = frozenset()) -> float` (mean F1 over classes present in gold, after dropping `exclude` classes from both sides' averaging); `location_scores(gold: list[Location], pred: list[Location | None]) -> dict[str, float]` with keys `f1, road_acc, landmark_acc, direction_acc`; `abstention_rate(gold: list[Location], pred: list[Location | None]) -> float`; `bootstrap_ci(metric_on_indices: Callable[[list[int]], float], n_items: int, n_boot: int = 1000, seed: int = 0) -> tuple[float, float]`.
- Rules: invalid predictions (`None`) count as wrong for every field. Location F1: a non-null predicted field is a TP if it equals the normalized gold, otherwise an FP (and an FN if gold was non-null); a null gold with null prediction is not counted in F1 but is counted in `abstention_rate`. Empty input → `float("nan")`.

- [ ] **Step 1: Write failing tests:** `test_normalize` (`"España Boulevard"`, `"Espana Blvd"` → equal; `"null"`, `""`, `None` → `None`; `"EDSA"` and alias `"Epifanio de los Santos Avenue"` → equal), `test_accuracy`, `test_macro_f1_perfect_and_all_wrong`, `test_macro_f1_exclude_unknown`, `test_location_f1_cases` (hand-computed small example with one wrong road, one null correctly predicted, one invented landmark), `test_abstention_rate_counts_invalid_as_failure`, `test_bootstrap_ci_deterministic_and_brackets_mean`, `test_empty_inputs_return_nan` (all functions, no exception).
- [ ] **Step 2:** Run `uv run pytest tests/test_metrics.py -v`; expect failures.
- [ ] **Step 3: Implement** per the rules above. `data/aliases.json` maps canonical road names to alias lists (start with EDSA, Commonwealth, Katipunan, España, Roxas, Taft, Aurora, Quezon Avenue, C5, SLEX, NLEX).
- [ ] **Step 4:** Run; expect pass.

### Task 4: Inference runner

**Files:**
- Create: `src/trafficslm/infer.py`, `tests/test_infer.py`

**Interfaces:**
- Consumes: `build_messages`, `pick_shots`, `load_split`.
- Produces: `Generator = Callable[[list[dict]], str]`; `mlx_generator(model_id: str, adapter_path: str | None = None, max_tokens: int = 200) -> Generator` (greedy); `run_predictions(records: list[Record], generator: Generator, out_dir: Path, shots: Sequence[Record] = (), meta: dict | None = None) -> Path` writes `out_dir/predictions.jsonl` (one `{"id", "raw", "latency_ms"}` per line) and `out_dir/meta.json` (model, adapter, mode, shot ids, mean/median latency, peak memory GB when available).

- [ ] **Step 1: Write failing tests** with a fake generator: `test_run_predictions_writes_one_line_per_record`, `test_latency_recorded_and_positive`, `test_generator_exception_recorded_not_fatal` (a failing item gets `raw: ""` and the run continues), `test_few_shot_messages_passed` (fake generator records the messages it received; first user turn is a shot).
- [ ] **Step 2:** Run; expect failures.
- [ ] **Step 3: Implement.** `mlx_generator` loads once via `mlx_lm.load`, applies the tokenizer chat template, and calls `mlx_lm.generate` with `max_tokens` (truncated output stays as-is; scoring marks it invalid). Use whichever peak-memory call the installed `mlx` version provides.
- [ ] **Step 4:** Run; expect pass.
- [ ] **Step 5 (smoke, needs network/model download):** run 3 validation items on `mlx-community/gemma-3-1b-it-bf16` (verify the exact repo id exists before running; fall back to the closest `mlx-community` Gemma 3 1B instruct build). Expected: 3 lines in `predictions.jsonl`, non-empty `raw`.

### Task 5: Evaluation and test-set guard

**Files:**
- Create: `src/trafficslm/evaluate.py`, `tests/test_evaluate.py`

**Interfaces:**
- Consumes: Task 3 metrics, `parse_report`, `load_split`.
- Produces: `score(records: list[Record], raws: list[str]) -> dict` with keys `n`, `json_validity`, `incident_macro_f1`, `incident_macro_f1_no_unknown`, `severity_acc`, `obstruction_acc`, `language_acc`, `location` (F1 + per-field), `abstention`, each as `{"value": float, "ci": [lo, hi]}`; `score_subsets(records, raws) -> dict[str, dict]` keyed by `lang:<language>` and `tag:<tag>`; `guard_test_access(run_name: str, split: str, final: bool, log_path: Path) -> None` (raises `PermissionError`); CLI `uv run python -m trafficslm.evaluate --run experiments/<run> --split validation|test [--final]` writing `results.json`.

- [ ] **Step 1: Write failing tests:** `test_score_perfect_predictions` (raws built from gold via `target_json` → all metrics 1.0, validity 1.0), `test_score_all_garbage` (validity 0.0, accuracy 0.0, no exception), `test_score_fenced_and_truncated_mix`, `test_subset_with_zero_or_one_item_gives_nan_not_error`, `test_guard_blocks_test_without_final`, `test_guard_allows_first_final_run`, `test_guard_blocks_second_test_run_same_run` (log file in tmp path), `test_guard_ignores_validation`.
- [ ] **Step 2:** Run; expect failures.
- [ ] **Step 3: Implement.** The guard appends `run_name` to `experiments/test_runs.log` on an allowed test run; a name already in the log is refused.
- [ ] **Step 4:** Run; expect pass.

### Task 6: Baselines (zero-shot and few-shot)

**Files:**
- Create: `scripts/run_baselines.sh` (or a `__main__` in `infer.py`), `experiments/` run folders
- Test: smoke assertions in step 3

**Interfaces:**
- Consumes: Tasks 2–5.
- Produces: run folders `experiments/{gemma3-1b,qwen2.5-1.5b}-{zeroshot,fewshot}/` each with `predictions.jsonl`, `meta.json`, `results.json` on the **validation** split.

- [ ] **Step 1:** Confirm the exact MLX repo ids for Gemma 3 1B instruct and Qwen2.5 1.5B Instruct (16-bit) exist; record them in `experiments/models.json`.
- [ ] **Step 2:** Run all four baselines on validation (40 items each) via the CLI, evaluate each.
- [ ] **Step 3: Verify:** each `results.json` has all metric keys, `n == 40`, and `json_validity` is reported (low values are fine and expected for zero-shot; they are a finding, not a failure).
- [ ] **Step 4:** Write the validation baseline table to `experiments/baselines_validation.md` (one row per run, one column per task score).

### Task 7: LoRA training and data-size sweep

**Files:**
- Create: `src/trafficslm/train.py`, `training/config.yaml`, `tests/test_train.py`

**Interfaces:**
- Consumes: `stratified_subset`, `write_mlx_dataset`.
- Produces: `build_command(model: str, data_dir: Path, adapter_dir: Path, iters: int, batch_size: int = 4, learning_rate: float = 1e-5, num_layers: int = 16, seed: int = 0) -> list[str]` (the `uv run python -m mlx_lm lora --train ...` argv); `run_training(model, train_records, valid_records, run_dir, **hparams) -> Path` (writes MLX dataset, runs training, returns adapter dir); `iters_for(n_train: int, batch_size: int, epochs: int = 3) -> int`.

- [ ] **Step 1: Write failing tests:** `test_build_command_contains_required_flags` (model, `--train`, `--data`, `--adapter-path`, `--iters`, `--seed`; check flag names against `uv run python -m mlx_lm lora --help` first), `test_iters_for` (207 items, batch 4, 3 epochs → 156), `test_run_training_writes_dataset_before_launch` (patch subprocess; assert `train.jsonl` and `valid.jsonl` exist and train excludes validation ids).
- [ ] **Step 2:** Run; expect failures. **Step 3:** Implement. Hyperparameters beyond those above are the builder's call; record what was used in `meta.json`.
- [ ] **Step 4:** Train Gemma 3 1B on subsets of 50, 100 and 207 (stratified, seed 0) and Qwen2.5 1.5B on 207; evaluate each on **validation** with the same prompt (zero-shot message format).
- [ ] **Step 5: Verify:** each adapter loads and `json_validity` on validation is reported. Peak training memory must stay under 24 GB; if a run fails, reduce batch size before changing anything else.

### Task 8: 4-bit comparison, optional 4B, and results report

**Files:**
- Create: `src/trafficslm/report.py`, `tests/test_report.py`

**Interfaces:**
- Consumes: `results.json` and `meta.json` files under `experiments/`.
- Produces: `collect(experiments_dir: Path) -> list[dict]` (one row per run: name, model, mode, n_train, split, scores, latency, memory); `write_summary(rows: list[dict], out_md: Path, out_png: Path) -> None` (markdown table with CIs; chart of each task score vs. training size).

- [ ] **Step 1: Write failing tests:** `test_collect_reads_fixture_runs` (two fake run folders in tmp), `test_write_summary_creates_files`, `test_summary_marks_nan_subsets` (nan shown as `n/a`).
- [ ] **Step 2:** Implement; run tests; expect pass.
- [ ] **Step 3:** Run a 4-bit LoRA training of Gemma 3 1B on all 207 items using a 4-bit MLX build of the base model; evaluate on validation. Optionally repeat the best configuration with Gemma 3 4B if memory allows.
- [ ] **Step 4:** Select the final configurations from validation results only; write the choice and reason to `research/selection.md` **before** any test run.

### Task 9: Final test evaluation, error analysis and write-up

**Files:**
- Create: `src/trafficslm/errors.py`, `tests/test_errors.py`, `research/findings.md`

**Interfaces:**
- Produces: `error_report(records: list[Record], raws: list[str], out_md: Path) -> None` (lists wrong items grouped by incident class and by subset tag, with gold vs predicted fields).

- [ ] **Step 1: Write failing tests:** `test_error_report_lists_only_wrong_items`, `test_error_report_groups_by_tag` (fixture of 4 records, 2 wrong). **Step 2:** Implement; run; expect pass.
- [ ] **Step 3:** Run the test split once per configuration chosen in `research/selection.md` (zero-shot, few-shot and fine-tuned for each chosen model) using `--final`. Verify `experiments/test_runs.log` lists each run exactly once and `verify_manifest()` still passes.
- [ ] **Step 4:** Generate `results/summary.md`, the chart, and error reports.
- [ ] **Step 5:** Write `research/findings.md`: hypothesis, setup, per-task results with CIs, noisy-Taglish vs English comparison (does fine-tuning hurt English?), data-size curve, 4-bit result, latency/memory, error analysis, and limitations (synthetic data only, single seed unless more were run, small test subsets). Cite prior work only after reading the sources directly.

---

## Self-Review

- **Spec coverage:** schema/taxonomy (T1), dataset and frozen splits (T2), prompts and baselines with k=5 (T2, T6), LoRA + sweep + 4-bit + 4B (T7, T8), all metrics and CIs and subsets (T3, T5), test-once rule (T5, T9), efficiency (T4, T8), error analysis and write-up (T9). Out of scope per the spec's first milestone: FastAPI service and dashboard.
- **Types:** `Record`, `Report`, `Location`, `Generator`, `score`, `guard_test_access` names are used identically across tasks.
- **Proportion:** the plan lists signatures, test names and pinned values; function bodies are left to the implementer.
