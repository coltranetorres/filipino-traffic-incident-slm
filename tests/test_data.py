import json
import shutil
from pathlib import Path

import pytest

from trafficslm.data import (
    load_split, pick_shots, stratified_subset, target_json,
    verify_manifest, write_mlx_dataset,
)
from trafficslm.prompts import SYSTEM_PROMPT, build_messages
from trafficslm.schema import INCIDENT_TYPES, parse_report

ROOT = Path(__file__).resolve().parent.parent / "data" / "processed"


def test_split_sizes():
    assert [len(load_split(n, ROOT)) for n in ("train", "validation", "test")] == [207, 40, 176]


def test_verify_manifest_passes():
    verify_manifest(ROOT)


def test_verify_manifest_detects_edit(tmp_path):
    shutil.copytree(ROOT, tmp_path / "p")
    with open(tmp_path / "p" / "test.jsonl", "ab") as f:
        f.write(b" ")
    with pytest.raises(ValueError):
        verify_manifest(tmp_path / "p")


def test_verify_manifest_detects_count_mismatch(tmp_path):
    shutil.copytree(ROOT, tmp_path / "p")
    m = json.loads((tmp_path / "p" / "MANIFEST.json").read_text())
    m["test"]["count"] = 1
    (tmp_path / "p" / "MANIFEST.json").write_text(json.dumps(m))
    with pytest.raises(ValueError):
        verify_manifest(tmp_path / "p")


def test_stratified_subset_deterministic_and_covers_classes():
    recs = load_split("test", ROOT)
    a = stratified_subset(recs, 50, seed=0)
    b = stratified_subset(recs, 50, seed=0)
    assert len(a) == 50
    assert [r.id for r in a] == [r.id for r in b]
    assert {r.incident_type for r in a} == set(INCIDENT_TYPES)


def test_build_messages_zero_shot():
    m = build_messages("hello")
    assert [x["role"] for x in m] == ["system", "user"]
    assert m[0]["content"] == SYSTEM_PROMPT
    assert m[1]["content"] == "hello"


def test_build_messages_few_shot():
    shots = pick_shots(load_split("train", ROOT))
    m = build_messages("q", shots)
    assert [x["role"] for x in m] == ["system"] + ["user", "assistant"] * 5 + ["user"]
    assert m[2]["content"] == target_json(shots[0])


def test_pick_shots_distinct_classes():
    train = load_split("train", ROOT)
    shots = pick_shots(train, k=5, seed=0)
    assert len(shots) == 5
    assert len({s.incident_type for s in shots}) == 5
    ids = {r.id for r in train}
    assert all(s.id in ids for s in shots)
    assert [s.id for s in shots] == [s.id for s in pick_shots(train, k=5, seed=0)]


def test_target_json_round_trips():
    for r in load_split("validation", ROOT):
        assert parse_report(target_json(r)) == r.target()
    s = target_json(load_split("train", ROOT)[0])
    assert s.startswith('{"incident_type":') and ", " not in s.split('"text"')[0]


def test_write_mlx_dataset(tmp_path):
    tr, va = load_split("train", ROOT), load_split("validation", ROOT)
    write_mlx_dataset(tr, va, tmp_path / "out")
    for name, recs in (("train", tr), ("valid", va)):
        lines = (tmp_path / "out" / f"{name}.jsonl").read_text(encoding="utf-8").splitlines()
        assert len(lines) == len(recs)
        row = json.loads(lines[0])
        assert list(row) == ["messages"]
        assert [x["role"] for x in row["messages"]] == ["system", "user", "assistant"]
        assert row["messages"][2]["content"] == target_json(recs[0])
