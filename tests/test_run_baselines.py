import importlib.util
import json
from pathlib import Path


def _load():
    p = Path(__file__).resolve().parents[1] / "scripts" / "run_baselines.py"
    spec = importlib.util.spec_from_file_location("run_baselines_mod", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_merge_models_keeps_existing_keys(tmp_path):
    m = _load()
    p = tmp_path / "models.json"
    p.write_text(json.dumps({"gemma3-1b-4bit": "x/4bit", "gemma3-1b": "old"}))
    out = m.merge_models(p, {"gemma3-1b": "new", "qwen": "q"})
    assert out == {"gemma3-1b-4bit": "x/4bit", "gemma3-1b": "new", "qwen": "q"}
    assert json.loads(p.read_text()) == out


def test_merge_models_creates_file(tmp_path):
    m = _load()
    p = tmp_path / "sub" / "models.json"
    assert m.merge_models(p, {"a": "b"}) == {"a": "b"}
    assert json.loads(p.read_text()) == {"a": "b"}
