"""Output schema for structured traffic-report understanding."""
from __future__ import annotations

import json
import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, ValidationError, field_validator

INCIDENT_TYPES = (
    "vehicle_breakdown", "road_accident", "road_hazard", "flooding",
    "road_closure", "heavy_traffic", "other", "unknown",
)
SEVERITIES = ("low", "medium", "high", "unknown")
OBSTRUCTIONS = ("none", "partial", "full", "unknown")
LANGUAGES = ("filipino", "english", "taglish")
DIRECTIONS = ("northbound", "southbound", "eastbound", "westbound")

IncidentType = Literal[
    "vehicle_breakdown", "road_accident", "road_hazard", "flooding",
    "road_closure", "heavy_traffic", "other", "unknown",
]
Severity = Literal["low", "medium", "high", "unknown"]
Obstruction = Literal["none", "partial", "full", "unknown"]
Language = Literal["filipino", "english", "taglish"]
Direction = Literal["northbound", "southbound", "eastbound", "westbound"]


class Location(BaseModel):
    model_config = ConfigDict(extra="forbid")

    road: str | None = None
    landmark: str | None = None
    direction: Direction | None = None

    @field_validator("road", "landmark", "direction", mode="before")
    @classmethod
    def _missing_to_none(cls, v):
        if isinstance(v, str) and v.strip().lower() in ("", "null"):
            return None
        return v


class Report(BaseModel):
    model_config = ConfigDict(extra="forbid")

    incident_type: IncidentType
    location: Location
    severity: Severity
    road_obstruction: Obstruction
    language: Language


class Record(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    split: str
    text: str
    language: Language
    incident_type: IncidentType
    location: Location
    severity: Severity
    road_obstruction: Obstruction
    tags: list[str] = []

    def target(self) -> Report:
        return Report(
            incident_type=self.incident_type,
            location=self.location,
            severity=self.severity,
            road_obstruction=self.road_obstruction,
            language=self.language,
        )


def _first_object(s: str) -> str | None:
    start = s.find("{")
    if start < 0:
        return None
    depth, in_str, esc = 0, False, False
    for i in range(start, len(s)):
        c = s[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        elif c == '"':
            in_str = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[start : i + 1]
    return None


def parse_report(raw: str) -> Report | None:
    """Parse the first balanced JSON object in model output; None if invalid."""
    text = re.sub(r"```(?:json)?", "", raw)
    obj = _first_object(text)
    if obj is None:
        return None
    try:
        return Report.model_validate(json.loads(obj))
    except (ValueError, ValidationError):
        return None
