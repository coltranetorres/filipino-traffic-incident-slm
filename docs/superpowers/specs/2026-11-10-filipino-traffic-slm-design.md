# Filipino Traffic Incident Understanding with Small Language Models — Design

Status: draft for approval. Project name: not chosen yet (deliberately deferred; "RoadSense PH" is taken).

## 1. Intent and the why

This is an applied research project, not an app. It asks one question:

> Can a relatively small language model (1–4B parameters), fine-tuned on Filipino, English, and Taglish traffic incident reports, achieve structured incident understanding while remaining efficient enough to run locally?

The owner (a single researcher on a MacBook M4, 24 GB unified memory) wants to publish findings, whatever they turn out to be. A negative or mixed result is a valid result. The deliverable is the evidence: a dataset, a reproducible pipeline, and a results write-up. A demo UI is secondary.

The system turns an informal traffic report into structured JSON. It is an experimental layer for crowdsourced reports and does not replace official traffic monitoring.

## 2. Hypothesis (stated before experiments run)

LoRA fine-tuning a small model on a domain-specific Filipino/Taglish traffic dataset improves structured incident classification and location extraction over zero-shot and few-shot prompting of the same model, while keeping inference cost low enough to run locally.

"Reliable" is NOT defined as a pass/fail threshold. We cannot yet justify a threshold, so we report separate scores per task with confidence intervals and let readers judge reliability from the numbers.

Prior work: no specific papers are cited in this document. Before publishing, the owner (or the assistant, with the owner checking) must read the existing Filipino and Taglish NLP benchmarks and related work directly, and cite only what has been verified from the source. Do not rely on summaries or memory for claims about what those papers do.

## 3. Task and output schema

One structured-prediction problem per report. Example:

Input: `May truck na nasiraan sa EDSA southbound near Cubao. Grabe traffic, one lane blocked.`

Output:
```json
{
  "incident_type": "vehicle_breakdown",
  "location": {"road": "EDSA", "landmark": "Cubao", "direction": "southbound"},
  "severity": "high",
  "road_obstruction": "partial",
  "language": "taglish"
}
```

Starting taxonomy (small on purpose; revise after the pilot):
- incident_type: vehicle_breakdown, road_accident, road_hazard, flooding, road_closure, heavy_traffic, other, unknown
- severity: low, medium, high, unknown. Severity is based on reported impact, never assumed from incident type (an accident is not automatically high).
- road_obstruction: none / partial / full / unknown (precise values to be fixed in the annotation guidelines).
- language: filipino, english, taglish.
- location fields (road, landmark, direction) may be null. The model must output null/unknown when information is absent and must not invent details.

An annotation guideline document defines each label with positive and negative examples and tie-break rules. Writing it is the first piece of work, before any large-scale data generation.

## 4. Dataset

- Minimum size: about 600 labeled examples. Planned split: about 400 train, 50 validation, 150 test. Grow if results are too noisy to separate models. A 300–500 example pilot validates the taxonomy first.
- Coverage: Filipino, English, Taglish; informal abbreviations; misspellings and grammar errors; incomplete reports; ambiguous reports; reports with no location; contradictory reports; very short reports.
- Sources: the AI assistant (Claude) generates most training data; the owner reviews and edits it. The owner writes or heavily rewrites the test set so it does not mirror the generator's style. Real reports may be added only where permission to use them exists.
- Leakage rule: no shared template, underlying sentence, or near-duplicate between train/validation and test. Check this before any training.
- Test set is held out and untouched until the final evaluation. Model and hyperparameter choices use the validation set only.
- Test subsets reported separately: Taglish, Filipino, English, noisy/misspelled, missing-information, short, contradictory. Each class should have enough test examples to score; the rarest classes may need targeted additions or may be reported as low-confidence.
- Data-efficiency study: train on 50, 100, 250, and full (about 400+) examples to show how much labeled data is needed.

Current state (approved 2026-11-10): frozen splits in `data/processed/` (`train.jsonl` 207, `validation.jsonl` 40, `test.jsonl` 176, checksums in `MANIFEST.json`). The test set is fixed at 176 (larger than the 150 first planned, to give the noisy and contradictory subsets enough items). Training data is held at 207 for now and grows only if results call for it; the test set never changes. Language labels follow the owner's rule: all-English = english; any English word (excluding road/street/place names) mixed with Filipino = taglish; no English words = filipino. Words spelled like English (bus, jeep, lane, motor) count as English.

Owner decisions on data (2026-11-10): the owner rewrites and modifies the assistant's drafts, including the test set (draft test items are marked `test_draft` until the owner has rewritten and signed off on them). No real reports are available, so the whole dataset is synthetic and the write-up must say findings cover synthetic Filipino/Taglish traffic text. Generation happens in chat, no API script. There is no publication target; multi-seed runs are "if time allows". Pilot file: `data/annotations/pilot_v0.json` (about 150 items); guideline: `docs/annotation-guidelines.md`.

## 5. Models and training

- Tooling (the assistant's default, not agreed in detail): Python, MLX-LM, LoRA on Apple Silicon, JSONL data.
- Models: Gemma 3 1B and Qwen2.5 1.5B Instruct as the main pair. Gemma 3 4B as an optional larger comparison (fits in 24 GB). Verify current MLX compatibility of each before committing.
- Main method: LoRA on 16-bit weights. The owner decided against QLoRA as the main method. A 4-bit (quantized-base) LoRA run is an extra comparison for the "runs efficiently locally" angle.
- Baselines: zero-shot and few-shot prompting for each model, using the same output schema.
- Experiments: baselines per model, LoRA per model, data-size sweep, 4-bit comparison, and a check that fine-tuning for Taglish/noisy input does not hurt English performance.

## 6. Evaluation

Report separate scores per task. No single combined score is used for conclusions. If a headline number is wanted, it is the unweighted mean of task scores, labeled secondary.

Metrics:
- Incident type: macro-F1 (plus per-class results).
- Severity: accuracy (and macro-F1).
- Location: span or field-level F1 on road, landmark, direction.
- Road obstruction: accuracy.
- JSON validity: share of outputs that parse and match the schema.
- Hallucination/abstention: on missing-information reports, how often the model correctly outputs unknown/null.
- Latency and memory on the M4.

Rigor requirements:
- Confidence intervals (bootstrap) on every reported score, because the test set is small.
- Multiple training seeds if time allows; otherwise state that a single seed was used.
- Metric definitions and the test set are fixed before experiments run.
- Final test evaluation runs once per chosen configuration.
- Error analysis: categorized failures, with examples.

## 7. Goals, non-goals, anti-goals

Goals: a publishable, reproducible evaluation (with a literature review done from primary sources); an honest answer to the research question; a clean dataset and annotation guideline.

Non-goals: replacing official traffic monitoring; a production service; scraping real social media posts without permission; a general Filipino benchmark.

Anti-goals (failure even if technically working): a test set the model has effectively memorized; a result produced by trying variations on the test set until one looks good; labels that quietly encode the generator's assumptions instead of the reported impact; a model that fills in locations or severity the report never stated.

## 8. Constraints

- Hardware: MacBook M4, 24 GB unified memory.
- Single researcher; the owner reviews the data. Deadline not stated; the plan assumes working at the owner's pace.
- Dataset creation and Filipino-language review are the main bottleneck, not training compute.

## 9. Proposed layout (the builder may adjust)

```
data/ (raw, processed, annotations)   training/   evaluation/   inference/   experiments/   research/findings.md   README.md
```
An optional later dashboard and FastAPI inference service are out of scope for the first milestone.

## 10. Left to the builder

Exact label definitions beyond Section 3 (guided by the pilot), prompt wording for baselines, LoRA hyperparameters, repo structure, experiment-tracking approach, and how to generate and deduplicate the synthetic data.

## 11. Assistant's calls (not yet agreed with the owner)

- Default stack (MLX-LM, Python, JSONL) and the model list.
- Split sizes (400/50/150) and the data-size sweep values.
- Bootstrap confidence intervals and the unweighted-mean headline.
- Starting obstruction values (none/partial/full/unknown).
- Labels: generated examples carry the generator's intended label, then the owner reviews them. A blind relabel of a random sample (about 10%) measures label noise.
- Location scoring: normalized match (case, spacing, and a small alias list such as EDSA = Epifanio de los Santos Avenue). Null predicted for null gold counts as correct. Aliases are fixed in the annotation guideline before evaluation.
- Contradictory or multi-incident reports: schema stays one object. The gold label is the primary incident, and any field the report contradicts is `unknown`.
- Macro-F1 includes `other` and `unknown`. Also report macro-F1 without `unknown`, since rare classes make the score volatile at 150 test examples.
- Models can be substituted (for example Qwen2.5 3B or Llama 3.2) if one fails in MLX-LM. Frameworks other than MLX are allowed only as a fallback.
- Few-shot baseline: k = 5, examples drawn from train only. The main comparison uses unconstrained decoding. Constrained decoding for JSON can be an extra row.
- A large-model reference (an API model) is optional, as an upper bound, if budget allows.
