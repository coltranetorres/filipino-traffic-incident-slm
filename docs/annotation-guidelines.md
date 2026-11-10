# Annotation Guidelines (v0, draft for owner review)

Label what the report says, never what you assume. If the report doesn't state something, use `unknown` (or `null` for location fields).

## incident_type
| Label | Use when |
|---|---|
| vehicle_breakdown | Stalled, broken-down, flat-tire, overheated vehicle |
| road_accident | Collision, crash, vehicle hitting person/object |
| road_hazard | Debris, fallen tree/post/cables, potholes, open manhole, spills |
| flooding | Flooded road, any depth |
| road_closure | Road/lane closed or blocked on purpose or by works, events, rallies, repairs |
| heavy_traffic | Congestion with no confirmed cause |
| other | A clear cause not listed (broken traffic light, checkpoint, convoy, brownout) |
| unknown | Not enough information to tell |

If a report names both a cause and traffic, label the cause (e.g. broken-down jeep + traffic = vehicle_breakdown).

## severity (based on reported impact only)
- **high**: road impassable or fully blocked, injuries/serious harm reported, standstill, or very long delay (about 1 hour or more).
- **medium**: partial obstruction, slow-moving or heavy traffic, moderate delay.
- **low**: reported as minor, no obstruction, or already cleared/moved aside.
- **unknown**: the report says nothing about impact.
An accident is NOT automatically high.

## road_obstruction
- **full**: all lanes/the road blocked or impassable.
- **partial**: some lanes blocked or open to some vehicles only.
- **none**: stated or clearly implied that nothing blocks the road (includes pure congestion, vehicle moved aside).
- **unknown**: not stated. "Nakaharang" or "sa gitna" alone is `unknown`.

## location
- `road`: canonical name, e.g. EDSA, Commonwealth Avenue, Katipunan Avenue, España Boulevard, Aurora Boulevard, Quezon Avenue, Roxas Boulevard, Taft Avenue, C5, SLEX, NLEX, Skyway. Aliases and spellings map to the canonical name. The scoring alias list (`data/aliases.json`) covers only some of them (for example the long form of EDSA, Espana, Taft, Katipunan; "Edsa" works through case normalization); abbreviations such as `Ave`/`Blvd` and case/accents are also normalized.
- `landmark`: nearest place, intersection, or exit as written, e.g. Cubao, Guadalupe, Ayala.
- `direction`: northbound, southbound, eastbound, westbound, or null. NB/SB/nb/sb map to these.
- Missing information is `null`. Never infer a road from a landmark.

## language
The language label follows the owner's rule, based on spelling:
- **english**: the whole text is English.
- **taglish**: any English-spelled word (excluding road, street and place names) mixed with Filipino. Words such as lane, bus, jeep, traffic and motor count as English even though they are common loanwords.
- **filipino**: no English-spelled words besides names. Filipino-spelled loanwords (trak, dyip, kotse, poste, trapik, trapiko, ambulansya, aksidente) count as Filipino.
- Typos of English words that remain recognisable (accdnt, trfc) count as English, so a Filipino sentence containing one is taglish.

## tags
`noisy` (misspelling/abbreviation), `no_location`, `short`, `ambiguous`, `contradictory`.

## contradictory reports
Keep the primary `incident_type`; set any contradicted field (severity, obstruction) to `unknown`.

## Open points for the owner
Severity cut-offs (flood depth, delay minutes), whether partial closures with a stated detour change severity, and whether `heavy_traffic` with a stated cause should stay out of that class.
