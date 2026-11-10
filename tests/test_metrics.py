import math

from trafficslm.metrics import (
    abstention_rate, accuracy, bootstrap_ci, location_scores, macro_f1, normalize,
)
from trafficslm.schema import Location


def L(road=None, landmark=None, direction=None):
    return Location(road=road, landmark=landmark, direction=direction)


def test_normalize():
    assert normalize("España Boulevard") == normalize("Espana Blvd")
    assert normalize("Ortigas Ave") == normalize("ortigas avenue")
    assert normalize("Marcos Hwy") == normalize("Marcos Highway")
    for v in ("null", "  NULL ", "", None):
        assert normalize(v) is None
    assert normalize("EDSA") == normalize("Epifanio de los Santos Avenue")
    assert normalize("C-5") == normalize("C5")


def test_accuracy():
    assert accuracy(["a", "b", "c", "d"], ["a", "b", "x", None]) == 0.5


def test_macro_f1_perfect_and_all_wrong():
    assert macro_f1(["a", "b"], ["a", "b"]) == 1.0
    assert macro_f1(["a", "b"], ["b", "a"]) == 0.0
    assert macro_f1(["a"], ["a"]) == 1.0
    assert macro_f1(["a", "b"], [None, None]) == 0.0


def test_macro_f1_exclude_unknown():
    gold = ["a", "a", "b", "unknown"]
    pred = ["a", "b", "b", "a"]
    assert math.isclose(macro_f1(gold, pred), 7 / 18)
    assert math.isclose(macro_f1(gold, pred, exclude=frozenset({"unknown"})), 7 / 12)
    assert math.isnan(macro_f1(["unknown"], ["unknown"], exclude=frozenset({"unknown"})))


def _loc_case():
    gold = [L("EDSA", "Ayala", "northbound"), L(), L("Taft Avenue")]
    pred = [L("Epifanio de los Santos Avenue", "Ayala", "southbound"), L(),
            L("Roxas Blvd", "Mall X")]
    return gold, pred


def test_location_f1_cases():
    gold, pred = _loc_case()
    s = location_scores(gold, pred)
    # TP=2, FP=3, FN=2 -> 4/9
    assert math.isclose(s["f1"], 4 / 9)
    assert math.isclose(s["road_acc"], 2 / 3)
    assert math.isclose(s["landmark_acc"], 2 / 3)
    assert math.isclose(s["direction_acc"], 2 / 3)
    s2 = location_scores(gold, [None, None, None])
    assert s2["f1"] == 0.0 and s2["road_acc"] == 0.0


def test_abstention_rate_counts_invalid_as_failure():
    gold, pred = _loc_case()
    assert math.isclose(abstention_rate(gold, pred), 0.8)
    assert abstention_rate([L(), L()], [L(), None]) == 0.5
    assert abstention_rate([L(), L()], [L("EDSA"), L()]) == 5 / 6


def test_bootstrap_ci_deterministic_and_brackets_mean():
    vals = [1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0]

    def m(idx):
        return sum(vals[i] for i in idx) / len(idx)

    a = bootstrap_ci(m, len(vals))
    assert a == bootstrap_ci(m, len(vals))
    assert a[0] <= 0.7 <= a[1] and a[0] < a[1]
    one = bootstrap_ci(m, 1)
    assert len(one) == 2


def test_empty_inputs_return_nan():
    assert math.isnan(accuracy([], []))
    assert math.isnan(macro_f1([], []))
    assert all(math.isnan(v) for v in location_scores([], []).values())
    assert math.isnan(abstention_rate([], []))
    lo, hi = bootstrap_ci(lambda idx: 0.0, 0)
    assert math.isnan(lo) and math.isnan(hi)
