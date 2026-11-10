import json
import math
from pathlib import Path

from trafficslm.report import collect, write_summary


def _entry(v, lo=None, hi=None):
    return {"value": v, "ci": [lo if lo is not None else v, hi if hi is not None else v]}


def _scores(f1=0.5):
    return {
        "n": 40,
        "json_validity": _entry(1.0),
        "incident_macro_f1": _entry(f1, f1 - 0.1, f1 + 0.1),
        "incident_macro_f1_no_unknown": _entry(f1),
        "severity_acc": _entry(0.6, 0.5, 0.7),
        "obstruction_acc": _entry(0.6),
        "language_acc": _entry(0.6),
        "location": {"f1": _entry(0.6)},
        "abstention": _entry(0.9),
    }


def _mk(root: Path, name, mode, n_train, f1, fname="results.json", model="m/gemma-bf16"):
    d = root / name
    d.mkdir(parents=True)
    (d / fname).write_text(json.dumps({"split": "validation" if fname == "results.json" else "test",
                                       "scores": _scores(f1), "subsets": {}}))
    meta = {"model": model, "mode": mode, "n_train": n_train, "latency_ms_median": 600.0,
            "peak_memory_gb": 3.1, "shot_ids": ["a", "b"] if mode == "few-shot" else []}
    (d / "meta.json").write_text(json.dumps(meta))


def _fixture(tmp_path):
    _mk(tmp_path, "gemma3-1b-lora-n50", "lora", 50, 0.4)
    _mk(tmp_path, "gemma3-1b-lora-n207", "lora", 207, 0.7)
    return tmp_path


def test_collect_reads_fixture_runs(tmp_path):
    rows = collect(_fixture(tmp_path))
    assert len(rows) == 2
    by = {r["name"]: r for r in rows}
    r = by["gemma3-1b-lora-n50"]
    assert r["mode"] == "lora" and r["n_train"] == 50 and r["split"] == "validation"
    assert r["latency_ms"] == 600.0 and r["peak_memory_gb"] == 3.1 and r["shots"] == 0
    assert r["scores"]["incident_macro_f1"]["value"] == 0.4


def test_collect_ignores_test_results_by_default(tmp_path):
    root = _fixture(tmp_path)
    (root / "gemma3-1b-lora-n50" / "results_test.json").write_text(
        json.dumps({"split": "test", "scores": _scores(0.99)}))
    _mk(root, "only-test", "lora", 50, 0.9, fname="results_test.json")
    rows = collect(root)
    assert {r["name"] for r in rows} == {"gemma3-1b-lora-n50", "gemma3-1b-lora-n207"}
    assert all(r["scores"]["incident_macro_f1"]["value"] != 0.99 for r in rows)
    test_rows = collect(root, split="test")
    assert {r["name"] for r in test_rows} == {"gemma3-1b-lora-n50", "only-test"}


def test_write_summary_creates_files(tmp_path):
    rows = collect(_fixture(tmp_path))
    md, png = tmp_path / "out" / "summary.md", tmp_path / "out" / "summary.png"
    write_summary(rows, md, png)
    assert png.stat().st_size > 0
    text = md.read_text()
    assert "gemma3-1b-lora-n50" in text and "0.40 [0.30, 0.50]" in text
    assert "cumulative" in text


def test_summary_marks_nan_subsets(tmp_path):
    rows = collect(_fixture(tmp_path))
    rows[0]["scores"]["severity_acc"] = {"value": math.nan, "ci": [math.nan, math.nan]}
    rows[1]["scores"]["incident_macro_f1_no_unknown"] = {"value": None, "ci": [None, None]}
    md = tmp_path / "s.md"
    write_summary(rows, md, tmp_path / "s.png")
    assert "n/a" in md.read_text()
    assert "nan" not in md.read_text().lower()


def test_chart_label_uses_actual_n(tmp_path, monkeypatch):
    import trafficslm.report as R
    rows = collect(_fixture(tmp_path))
    for r in rows:
        r["scores"]["n"] = 176
        r["split"] = "test"
    labels = []
    import matplotlib.axes
    orig = matplotlib.axes.Axes.set_ylabel

    def spy(self, label, *a, **k):
        labels.append(label)
        return orig(self, label, *a, **k)

    monkeypatch.setattr(matplotlib.axes.Axes, "set_ylabel", spy)
    R._chart(rows, tmp_path / "c.png")
    assert any("n=176" in l and "Test" in l for l in labels), labels


def test_collect_test_split_uses_meta_test(tmp_path):
    root = _fixture(tmp_path)
    _mk(root, "x", "lora", 50, 0.9, fname="results_test.json")
    (root / "x" / "meta_test.json").write_text(json.dumps({"latency_ms_median": 123.0, "peak_memory_gb": 9.9}))
    r = [r for r in collect(root, split="test") if r["name"] == "x"][0]
    assert r["latency_ms"] == 123.0 and r["peak_memory_gb"] == 9.9 and r["n_train"] == 50
