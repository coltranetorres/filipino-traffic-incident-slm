import json
from pathlib import Path

from trafficslm.schema import Record, Report, parse_report

GOOD = {
    "incident_type": "road_accident",
    "location": {"road": "EDSA", "landmark": "Guadalupe", "direction": "southbound"},
    "severity": "high",
    "road_obstruction": "partial",
    "language": "taglish",
}
DATA = Path(__file__).resolve().parent.parent / "data" / "processed"


def test_parse_plain_json():
    assert isinstance(parse_report(json.dumps(GOOD)), Report)


def test_parse_fenced_json():
    raw = "```json\n" + json.dumps(GOOD) + "\n```"
    assert isinstance(parse_report(raw), Report)


def test_parse_with_prose():
    raw = "Here: " + json.dumps(GOOD) + " done"
    assert isinstance(parse_report(raw), Report)


def test_parse_invalid_enum_returns_none():
    assert parse_report(json.dumps({**GOOD, "incident_type": "crash"})) is None


def test_parse_extra_key_returns_none():
    assert parse_report(json.dumps({**GOOD, "extra": 1})) is None


def test_parse_truncated_returns_none():
    assert parse_report(json.dumps(GOOD)[:-10]) is None


def test_null_string_becomes_none():
    for val in ("null", "", " NULL "):
        loc = {**GOOD["location"], "road": val}
        r = parse_report(json.dumps({**GOOD, "location": loc}))
        assert r is not None and r.location.road is None


def test_every_processed_record_validates():
    n = 0
    for name in ("train", "validation", "test"):
        for line in (DATA / f"{name}.jsonl").read_text().splitlines():
            if line.strip():
                rec = Record.model_validate_json(line)
                assert isinstance(rec.target(), Report)
                n += 1
    assert n == 423
