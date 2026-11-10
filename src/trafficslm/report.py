"""Collect run results and write the validation summary table and chart."""
from __future__ import annotations

import json
from pathlib import Path

from .tables import build_table

TASKS = [
    ("incident_macro_f1", "Incident macro-F1"),
    ("severity_acc", "Severity accuracy"),
    ("obstruction_acc", "Obstruction accuracy"),
    ("language_acc", "Language accuracy"),
    ("json_validity", "JSON validity"),
]
FOOTNOTE = (
    "\n\nNote: peak_memory_gb for the zero-/few-shot baselines is a cumulative-process peak "
    "(the baselines ran in one process, so the column rises monotonically across them); LoRA runs "
    "were evaluated in their own process, so their memory is a per-process peak. Do not compare "
    "memory between the two groups.\n"
)


def _results_file(split: str) -> str:
    return "results.json" if split == "validation" else f"results_{split}.json"


def collect(experiments_dir: Path, split: str = "validation") -> list[dict]:
    rows = []
    for d in sorted(Path(experiments_dir).iterdir()):
        rf = d / _results_file(split)
        if not (d.is_dir() and rf.exists()):
            continue
        res = json.loads(rf.read_text(encoding="utf-8"))
        meta_p = d / "meta.json"
        meta = json.loads(meta_p.read_text(encoding="utf-8")) if meta_p.exists() else {}
        if split == "test" and (d / "meta_test.json").exists():
            meta = {**meta, **json.loads((d / "meta_test.json").read_text(encoding="utf-8"))}
        rows.append({
            "name": d.name, "model": meta.get("model"), "mode": meta.get("mode"),
            "n_train": meta.get("n_train"), "split": res.get("split", split),
            "scores": res["scores"], "latency_ms": meta.get("latency_ms_median"),
            "peak_memory_gb": meta.get("peak_memory_gb"), "shots": len(meta.get("shot_ids") or []),
        })
    return rows


def _val(e):
    v = e.get("value") if isinstance(e, dict) else None
    return v if isinstance(v, (int, float)) and v == v else None


def _chart(rows, out_png: Path) -> None:
    split_name = "Test" if any(r.get("split") == "test" for r in rows) else "Validation"
    n_items = next((r["scores"].get("n") for r in rows if r["scores"].get("n")), None)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    pts = sorted((r for r in rows if r["mode"] == "lora" and r["n_train"] in (50, 100, 207)
                  and "gemma" in (r["model"] or "").lower() and "4bit" not in (r["model"] or "")
                  and "4bit" not in r["name"]), key=lambda r: r["n_train"])
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for i, (key, label) in enumerate(TASKS):
        xs, ys, lo, hi = [], [], [], []
        for r in pts:
            e = r["scores"].get(key)
            v = _val(e)
            if v is None:
                continue
            ci = e.get("ci") or [None, None]
            l, h = (c if isinstance(c, (int, float)) and c == c else v for c in ci[:2])
            xs.append(r["n_train"]); ys.append(v); lo.append(max(v - l, 0)); hi.append(max(h - v, 0))
        if xs:
            ax.errorbar([x + (i - 2) * 1.5 for x in xs], ys, yerr=[lo, hi], marker="o", capsize=3, label=label)
    ax.set_xticks([50, 100, 207])
    ax.set_xlabel("LoRA training set size n (Gemma 3 1B)")
    ax.set_ylabel(f"{split_name} score (n={n_items}, 95% CI)")
    ax.set_ylim(0, 1.05)
    ax.set_title(f"Gemma 3 1B LoRA: {split_name.lower()} score vs training size")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="lower right")
    fig.tight_layout()
    Path(out_png).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=150)
    plt.close(fig)


def write_summary(rows: list[dict], out_md: Path, out_png: Path) -> None:
    runs = {r["name"]: ({"scores": r["scores"]},
                        {"latency_ms_median": r["latency_ms"], "peak_memory_gb": r["peak_memory_gb"]})
            for r in rows}
    out_md = Path(out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    is_test = any(r.get("split") == "test" for r in rows)
    note = ("\n\nNote: each test run was executed in its own process, so peak_memory_gb is a per-process "
            "peak for every row.\n") if is_test else FOOTNOTE
    out_md.write_text(f"# {'Test' if is_test else 'Validation'} summary (value [95% CI])\n\n"
                      + build_table(runs) + note, encoding="utf-8")
    _chart(rows, Path(out_png))
