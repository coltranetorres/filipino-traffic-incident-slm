"""Print the markdown tables used in research/findings.md from the JSON result files.

Usage: uv run python scripts/make_findings_tables.py [table_name ...]
With no arguments every table is printed. Reads experiments/<run>/results*.json and meta*.json only.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from trafficslm.runs import TEST_RUNS  # noqa: E402
from trafficslm.tables import fmt_entry  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
EXP = ROOT / "experiments"

RUNS = TEST_RUNS
# metric label -> path inside "scores" / subset dict
METRICS = {
    "JSON valid": ("json_validity",),
    "Incident macro-F1": ("incident_macro_f1",),
    "Incident macro-F1 (no unknown)": ("incident_macro_f1_no_unknown",),
    "Severity acc": ("severity_acc",),
    "Obstruction acc": ("obstruction_acc",),
    "Language acc": ("language_acc",),
    "Location F1": ("location", "f1"),
    "Abstention": ("abstention",),
}


def load(run, test=True, meta=False):
    name = ("meta" if meta else "results") + ("_test" if test else "") + ".json"
    return json.loads((EXP / run / name).read_text())


def node(res, key, subset=None):
    d = res["scores"] if subset is None else res["subsets"][subset]
    for k in key:
        d = d[k]
    return d


fmt = fmt_entry


def md(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def t_main():
    cols = list(METRICS)
    rows = [[r] + [fmt(node(load(r), METRICS[c])) for c in cols] for r in RUNS]
    return md(["run"] + cols, rows)


def t_cost():
    rows = []
    for r in RUNS:
        m = load(r, meta=True)
        rows.append([r, f"{m['latency_ms_median']:.0f}", f"{m['latency_ms_mean']:.0f}", f"{m['peak_memory_gb']:.2f}"])
    return md(["run", "median latency ms", "mean latency ms", "peak memory GB (per process)"], rows)


def t_valtest():
    cols = ["Incident macro-F1", "Severity acc", "Obstruction acc", "Language acc", "Location F1"]
    rows = []
    for r in ["gemma3-1b-lora-n207", "qwen2.5-1.5b-lora-n207", "gemma3-1b-4bit-lora-n207"]:
        for split, test in (("validation (n=40)", False), ("test (n=176)", True)):
            res = load(r, test=test)
            rows.append([r, split] + [fmt(node(res, METRICS[c])) for c in cols])
    return md(["run", "split"] + cols, rows)


def t_curve():
    cols = ["Incident macro-F1", "Severity acc", "Obstruction acc", "Language acc", "Location F1", "Abstention"]
    rows = []
    for r, n in [("gemma3-1b-fewshot", "0 (few-shot, k=5)"), ("gemma3-1b-lora-n50", "50"),
                 ("gemma3-1b-lora-n100", "100"), ("gemma3-1b-lora-n207", "207")]:
        res = load(r)
        rows.append([n] + [fmt(node(res, METRICS[c])) for c in cols])
    return md(["train items"] + cols, rows)


def t_quant():
    rows = []
    for r in ["gemma3-1b-lora-n207", "gemma3-1b-4bit-lora-n207"]:
        res, mt, mv = load(r), load(r, meta=True), load(r, test=False, meta=True)
        rows.append([r, fmt(node(res, METRICS["Incident macro-F1"])), fmt(node(res, METRICS["Severity acc"])),
                     fmt(node(res, METRICS["Obstruction acc"])), fmt(node(res, METRICS["Location F1"])),
                     f"{mt['latency_ms_median']:.0f}", f"{mt['peak_memory_gb']:.2f}",
                     f"{mv['train_peak_rss_gb']:.2f}", f"{mv['training_wall_s']:.0f}"])
    return md(["run", "Incident macro-F1", "Severity acc", "Obstruction acc", "Location F1",
               "median latency ms (test)", "peak inference mem GB (test)", "train peak RSS GB", "train wall s"], rows)


SUBSETS = ["lang:filipino", "lang:taglish", "lang:english", "tag:noisy", "tag:no_location",
           "tag:short", "tag:ambiguous", "tag:contradictory"]
SUB_RUNS = ["gemma3-1b-fewshot", "gemma3-1b-lora-n207", "qwen2.5-1.5b-fewshot", "qwen2.5-1.5b-lora-n207"]


def t_subset(metric):
    res = {r: load(r) for r in SUB_RUNS}
    rows = []
    for s in SUBSETS:
        n = res[SUB_RUNS[0]]["subsets"][s]["n"]
        rows.append([s, n] + [fmt(node(res[r], METRICS[metric], s)) for r in SUB_RUNS])
    return md(["subset", "n"] + SUB_RUNS, rows)


def t_before_after():
    cols = ["Incident macro-F1", "Severity acc", "Obstruction acc", "Language acc", "Location F1"]
    rows = []
    for fam, base, lora in [("Gemma 3 1B", "gemma3-1b-fewshot", "gemma3-1b-lora-n207"),
                            ("Qwen2.5 1.5B", "qwen2.5-1.5b-fewshot", "qwen2.5-1.5b-lora-n207")]:
        for s in ["lang:english", "tag:noisy"]:
            for label, r in (("few-shot", base), ("LoRA n207", lora)):
                res = load(r)
                rows.append([fam, s, res["subsets"][s]["n"], label] + [fmt(node(res, METRICS[c], s)) for c in cols])
    return md(["model", "subset", "n", "config"] + cols, rows)


def t_data():
    m = json.loads((ROOT / "data/processed/MANIFEST.json").read_text())
    langs = ["filipino", "taglish", "english"]
    rows = [[s, m[s]["count"]] + [f"{m[s]['languages'][l]} ({m[s]['languages'][l] / m[s]['count']:.0%})" for l in langs]
            for s in ("train", "validation", "test")]
    t1 = md(["split", "n"] + langs, rows)
    classes = list(m["train"]["classes"])
    rows = [[c] + [m[s]["classes"][c] for s in ("train", "validation", "test")] for c in classes]
    return t1 + "\n\n" + md(["incident_type", "train", "validation", "test"], rows)


TABLES = {
    "data": t_data, "main": t_main, "cost": t_cost, "valtest": t_valtest, "curve": t_curve, "quant": t_quant,
    "sub_incident": lambda: t_subset("Incident macro-F1"), "sub_severity": lambda: t_subset("Severity acc"),
    "sub_obstruction": lambda: t_subset("Obstruction acc"), "sub_language": lambda: t_subset("Language acc"),
    "sub_location": lambda: t_subset("Location F1"), "sub_abstention": lambda: t_subset("Abstention"), "before_after": t_before_after,
}

if __name__ == "__main__":
    names = sys.argv[1:] or list(TABLES)
    for n in names:
        print(f"<!-- {n} -->\n{TABLES[n]()}\n")
