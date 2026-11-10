import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from run_baselines import fmt_entry, fmt_num


def test_fmt_entry_ci():
    assert fmt_entry({"value": 0.62, "ci": [0.48, 0.75]}) == "0.62 [0.48, 0.75]"


def test_fmt_entry_null_and_nan():
    assert fmt_entry({"value": None, "ci": [None, None]}) == "n/a"
    assert fmt_entry({"value": float("nan"), "ci": [math.nan, math.nan]}) == "n/a"
    assert fmt_entry({"value": 0.5, "ci": [None, None]}) == "0.50"


def test_fmt_num():
    assert fmt_num(None) == "n/a"
    assert fmt_num(12.345, 1) == "12.3"
