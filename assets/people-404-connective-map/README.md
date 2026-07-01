# Connective Mapping — People 404™ Micro Map

**Title:** *Connective Mapping Starts Where the Work Actually Happens*
**Use:** LinkedIn / article support graphic for Sustineri Consulting Group.

## Files

| File | Purpose |
| --- | --- |
| `connective_map.svg` | Source vector (infinitely scalable, editable text). |
| `connective_map.png` | Export at 2480 × 3800 px (2× retina), ready for LinkedIn / article. |
| `generate_map.py` | Regenerates the SVG from data (edit labels/colors here). |
| `render_png.py` | Renders the SVG to PNG via headless Chromium. |

To regenerate after editing labels or colors:

```bash
python3 generate_map.py      # writes connective_map.svg
python3 render_png.py        # writes connective_map.png (needs Chromium/Playwright)
```

## The idea in plain language

Most organizations only see the **formal org chart** — titles, departments, and
reporting lines. That chart tells you who *reports* to whom. It does **not** tell
you where the work actually moves, or which roles the whole system quietly leans
on to function.

**Connective mapping** flips the starting point. Instead of starting at the top
of a hierarchy, it starts at the *center of the work*: the role the organization
cannot function without. Then it maps **outward** in three layers.

### How to read the map (center → out)

1. **Center — Critical Function Role**
   "The work the system depends on." This is the anchor. Not a job title — the
   *function* everything else quietly relies on.

2. **First ring — Daily Work** (gold)
   The everyday work this role actually performs: *fixes issues, moves
   information, keeps records clean, supports decisions, prevents delays.*
   These are the connective lines drawn straight to the center — the work itself.

3. **Second ring — Dependencies** (steel)
   *Who and what depends on that daily work:* leadership decisions, customer /
   client experience, compliance, payroll / finance, operations, technology,
   field execution. When the center works, all of these keep moving.

4. **Outer ring — Failure Signals** (dashed, light)
   *What the organization actually feels when the work is interrupted:* delays,
   duplicate work, confusion, rework, burnout, missed handoffs, decision
   bottlenecks. These are the symptoms leadership usually notices **first** —
   without realizing they trace back to the center.

The dashed outer ring is deliberate: failure signals are the visible edge of an
invisible dependency. You see the symptom long before you see the cause.

## The split view: two pictures of the same role

| Formal Org Chart | Actual Work Chart |
| --- | --- |
| Title | Who depends on them |
| Department | What they fix |
| Reporting line | What breaks without them |
| | Where the work really moves |

Same person. Two completely different pictures. The org chart shows *position*.
The work chart shows *load-bearing reality*. Connective mapping is how you make
the second picture visible **before** the failure signals force you to.

## Important framing

This map is **not about blame**, and it is **not an org chart**. It is a
systems-level view of where real work happens and what is at risk when that work
is interrupted. The goal is visibility and resilience — identify the invisible
critical roles, understand the web of dependency around them, and protect the
connections *before* they break.

## Brand

- Navy `#012564` · Gold `#ab8834` / `#e6bb54` · Steel `#496699` · Light gray `#dbdbdb`
- Footer: **Sustineri Consulting Group | People 404™**
