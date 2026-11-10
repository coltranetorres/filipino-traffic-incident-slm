import json
from pathlib import Path
from unittest import mock

from trafficslm.data import load_split
from trafficslm.train import build_command, iters_for, run_training


def test_build_command_contains_required_flags():
    cmd = build_command("m/x", Path("d"), Path("a"), iters=10)
    for flag in ("--model", "--train", "--data", "--adapter-path", "--iters", "--seed", "--mask-prompt"):
        assert flag in cmd
    assert cmd[cmd.index("--model") + 1] == "m/x"
    assert cmd[cmd.index("--iters") + 1] == "10"
    assert cmd[:6] == ["uv", "run", "python", "-m", "mlx_lm", "lora"]
    assert "--test" not in cmd and not any("test" in c for c in cmd if c.startswith("--"))


def test_iters_for():
    assert iters_for(207, 4, 3) == 156
    assert iters_for(50, 4) == 39


def test_run_training_writes_dataset_before_launch(tmp_path):
    train = load_split("train")[:20]
    valid = load_split("validation")
    seen = {}

    def fake_run(cmd, **kw):
        d = Path(cmd[cmd.index("--data") + 1])
        seen["train"] = [json.loads(l) for l in (d / "train.jsonl").read_text().splitlines()]
        seen["valid"] = (d / "valid.jsonl").exists()
        return mock.Mock(returncode=0)

    with mock.patch("trafficslm.train.subprocess.run", side_effect=fake_run):
        out = run_training("m/x", train, valid, tmp_path)
    assert seen["valid"] and len(seen["train"]) == 20
    users = [m["content"] for ex in seen["train"] for m in ex["messages"] if m["role"] == "user"]
    assert not any(r.text in u for r in valid for u in users)
    assert out == tmp_path / "adapters"


def test_finalize_lora_meta_sets_mode_and_reads_adapter_config(tmp_path):
    from trafficslm.train import finalize_lora_meta

    (tmp_path / "adapter_config.json").write_text(json.dumps(
        {"mask_prompt": True, "fine_tune_type": "lora", "num_layers": 16, "batch_size": 4,
         "iters": 39, "learning_rate": 1e-5, "seed": 0, "extra": 1}))
    m = finalize_lora_meta({"mode": "zero-shot", "n": 40}, tmp_path, ["a", "b"])
    assert m["mode"] == "lora" and m["train_cmd"] == ["a", "b"]
    assert m["adapter_config"] == {"mask_prompt": True, "fine_tune_type": "lora", "num_layers": 16,
                                   "batch_size": 4, "iters": 39, "learning_rate": 1e-5, "seed": 0}
    assert m["mask_prompt"] is True and m["n"] == 40
