"""Prompt construction and target serialisation."""
from __future__ import annotations

import json
from collections.abc import Sequence

from .schema import Record

SYSTEM_PROMPT = (
    "Extract a structured report from a Filipino/Taglish/English traffic report. "
    "Reply with a single JSON object only, no other text, in this exact shape:\n"
    '{"incident_type":...,"location":{"road":...,"landmark":...,"direction":...},'
    '"severity":...,"road_obstruction":...,"language":...}\n'
    "incident_type: vehicle_breakdown | road_accident | road_hazard | flooding | "
    "road_closure | heavy_traffic | other | unknown\n"
    "severity: low | medium | high | unknown\n"
    "road_obstruction: none | partial | full | unknown\n"
    "language: filipino | english | taglish\n"
    "direction: northbound | southbound | eastbound | westbound | null\n"
    "Rules: severity reflects the reported impact only (an accident is not automatically high). "
    "If information is missing, use null (road, landmark, direction) or unknown; never invent details."
)


def target_json(rec: Record) -> str:
    t = rec.target()
    obj = {
        "incident_type": t.incident_type,
        "location": {
            "road": t.location.road,
            "landmark": t.location.landmark,
            "direction": t.location.direction,
        },
        "severity": t.severity,
        "road_obstruction": t.road_obstruction,
        "language": t.language,
    }
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def build_messages(text: str, shots: Sequence[Record] = ()) -> list[dict]:
    msgs: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]
    for s in shots:
        msgs.append({"role": "user", "content": s.text})
        msgs.append({"role": "assistant", "content": target_json(s)})
    msgs.append({"role": "user", "content": text})
    return msgs
