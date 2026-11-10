from trafficslm.prompts import SYSTEM_PROMPT
from trafficslm.schema import DIRECTIONS, INCIDENT_TYPES, LANGUAGES, OBSTRUCTIONS, SEVERITIES


def test_system_prompt_lists_labels():
    for label in (*INCIDENT_TYPES, *SEVERITIES, *OBSTRUCTIONS, *LANGUAGES, *DIRECTIONS):
        assert label in SYSTEM_PROMPT
    assert "null" in SYSTEM_PROMPT and "JSON" in SYSTEM_PROMPT
    assert "never invent" in SYSTEM_PROMPT.lower() or "do not invent" in SYSTEM_PROMPT.lower()
    assert "not automatically high" in SYSTEM_PROMPT
    assert len(SYSTEM_PROMPT) < 1500
