# People 404™ Connective Map — Template

**Purpose:** A reusable, fill-in map of how work actually flows and where it's fragile.
This is the core working artifact of the Work Health Check. One row per role (or per person
where a role is split or shared).

---

## Main connective map

| Role | Formal title | Actual work performed | Depends on | Depended on by | Tools used | Undocumented knowledge | Risk level | Failure impact | Repair recommendation |
|------|--------------|----------------------|------------|----------------|------------|------------------------|-----------|----------------|-----------------------|
| _[role]_ | _[title on the org chart]_ | _[what they really do day to day]_ | _[people/tools/vendors they rely on]_ | _[who relies on them]_ | _[systems]_ | _[what only they know]_ | _[Low/Med/High/Critical]_ | _[what breaks if this fails]_ | _[the fix]_ |
| | | | | | | | | | |
| | | | | | | | | | |

**Risk level guide:**
- **Low** — documented, backed up, low impact if interrupted.
- **Medium** — some concentration or gap, manageable short-term.
- **High** — single point of failure OR undocumented critical work OR overloaded.
- **Critical** — single point of failure AND undocumented AND high impact.

## Dependency summary (derived from the map)

- **Single points of failure:** _[list roles rated High/Critical with no backup]_
- **Undocumented critical work:** _[list]_
- **Overloaded roles:** _[list]_
- **Vendor / tool dependencies with no backup:** _[list]_
- **Informal decision chains:** _[who really decides, off-chart]_

## Formal chart vs. actual work — gap notes

- Where the org chart says one thing and reality does another:
  - _[e.g., "Ops Manager" on chart is actually the de facto IT admin, billing approver, and onboarding owner]_
- Roles missing from the formal chart entirely:
  - _[e.g., the person doing all vendor coordination has no title for it]_

---

## Turning this map into a visual (later)

This template is deliberately text/table-based so it can be filled fast and stays accurate.
To turn it into a visual for the readout:

1. **Nodes = roles/people.** Draw one box per row.
2. **Arrows = dependency.** Draw an arrow from each role to the roles/tools/vendors in its
   "Depends on" column. Arrows pointing *into* a box show who depends on it — the more
   inbound arrows, the more critical.
3. **Color = risk level.** Use the Sustineri palette (Navy `#012564`, Gold `#ab8834` /
   `#e6bb54`, Steel `#496699`, Gray `#dbdbdb`). Suggested: Critical = Gold highlight,
   High = Steel, Low/Med = Gray, structure = Navy.
4. **Compare two views side by side:** the formal org chart (tidy, top-down) vs. the actual
   work chart (messy, cross-cutting). The contrast is the point.

Any diagramming tool works (whiteboard, slides, a diagram app). **Do not** treat the visual
as the deliverable — the analysis and repair recommendations are the value.
