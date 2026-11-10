"""Error analysis: list wrong predictions grouped by gold class, subset tag and language."""
from __future__ import annotations

from pathlib import Path

from .evaluate import TAGS
from .metrics import normalize
from .schema import INCIDENT_TYPES, LANGUAGES, Record, parse_report

FIELDS = ("incident_type", "severity", "road_obstruction", "language")
LOC_FIELDS = ("road", "landmark", "direction")


def _diffs(rec: Record, raw: str) -> tuple[list[str], str]:
    """Return (list of 'field: gold -> pred' strings, predicted summary)."""
    p = parse_report(raw)
    if p is None:
        return ["invalid JSON"], (raw or "").strip().replace("\n", " ")[:200] or "(empty)"
    out = []
    for f in FIELDS:
        g, q = getattr(rec, f), getattr(p, f)
        if g != q:
            out.append(f"{f}: gold={g} pred={q}")
    for f in LOC_FIELDS:
        g, q = getattr(rec.location, f), getattr(p.location, f)
        if normalize(g) != normalize(q):
            out.append(f"location.{f}: gold={g} pred={q}")
    return out, p.model_dump_json()


def _esc(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def _table(title: str, rows: list[tuple[str, int, int]]) -> list[str]:
    lines = [f"### {title}", "", "| group | errors / size |", "|---|---|"]
    lines += [f"| {name} | {e} / {n} |" for name, e, n in rows]
    return lines + [""]


def error_report(records: list[Record], raws: list[str], out_md: Path) -> None:
    if len(records) != len(raws):
        raise ValueError(f"{len(records)} records but {len(raws)} predictions")
    wrong = []  # (record, diffs, pred)
    wrong_ids = set()
    for r, raw in zip(records, raws):
        d, pred = _diffs(r, raw)
        if d:
            wrong.append((r, d, pred))
            wrong_ids.add(r.id)

    def count(pred):
        sel = [r for r in records if pred(r)]
        return sum(r.id in wrong_ids for r in sel), len(sel)

    classes = [c for c in INCIDENT_TYPES if any(r.incident_type == c for r in records)]
    lines = ["# Error analysis", "",
             f"{len(wrong)} of {len(records)} items have at least one wrong field "
             "(incident_type, severity, road_obstruction, language, any location field, or invalid JSON).", ""]
    lines += ["## Count summary", ""]
    lines += _table("By gold incident class",
                    [(c, *count(lambda r, c=c: r.incident_type == c)) for c in classes])
    lines += _table("By subset tag",
                    [(t, *count(lambda r, t=t: t in r.tags)) for t in TAGS])
    lines += _table("By language",
                    [(g, *count(lambda r, g=g: r.language == g)) for g in LANGUAGES])

    def items(rs):
        out = []
        for r, d, pred in rs:
            out += [f"- `{r.id}` [{r.language}; tags: {', '.join(r.tags) or '-'}] {_esc(r.text)}",
                    f"  - errors: {'; '.join(d)}",
                    f"  - predicted: {_esc(pred)}"]
        return out

    lines += ["## Wrong items by gold incident class", ""]
    for c in classes:
        sub = [w for w in wrong if w[0].incident_type == c]
        if sub:
            lines += [f"### {c} ({len(sub)})", ""] + items(sub) + [""]
    lines += ["## Wrong items by subset tag", ""]
    for t in TAGS:
        sub = [w for w in wrong if t in w[0].tags]
        if sub:
            lines += [f"### {t} ({len(sub)})", ""] + [f"- `{w[0].id}`: {'; '.join(w[1])}" for w in sub] + [""]
    lines += ["## Wrong items by language", ""]
    for g in LANGUAGES:
        sub = [w for w in wrong if w[0].language == g]
        if sub:
            lines += [f"### {g} ({len(sub)})", ""] + [f"- `{w[0].id}`: {'; '.join(w[1])}" for w in sub] + [""]
    out_md = Path(out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
