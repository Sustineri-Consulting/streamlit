# Sustineri — HR Micro Connective Maps

A matched series of five LinkedIn-ready (1080 × 1080) connective-map graphics plus a
contact-sheet preview, supporting the article thesis:

> **"I do not hate HR people. I hate the structure HR has been forced to operate inside."**

The set shows, visually, how HR functions inside a broken ecosystem, how blame gets
assigned, how policy becomes chaos, and why AI amplifies the problem if the structure
is not mapped first.

## Routing note

No existing approved Sustineri / Invisible Ecosystem / connective-mapping workspace was
found on this machine (filesystem searched). Per the lane rules, this fallback workspace
was created and used: **`sustineri-hr-micro-connective-maps`**.

## Brand kit (locked)

| Token | Hex | Use |
|---|---|---|
| Navy | `#012564` | HR node, headlines, caption band, footer |
| Gold | `#ab8834` | blame / amplification arrows, emphasis, accents |
| Gold (light) | `#e6bb54` | secondary accent |
| Steel | `#496699` | connectors, source-node borders, sublines |
| Light gray | `#dbdbdb` | rules, panel borders |
| Neutral BG | `#f6f7f9` | very light background |

Consistent across all five: header (kicker + map index), headline, subline, gold rule,
centered connective map, navy caption band, `Sustineri` footer with tagline.

## Files

```
exports/
  sustineri_hr_map_00_contact-sheet.png            (1600 × 1320)
  sustineri_hr_map_01_hr-is-the-face-not-the-source.png   (1080 × 1080)
  sustineri_hr_map_02_unlimited-pto.png                   (1080 × 1080)
  sustineri_hr_map_03_broken-telephone.png                (1080 × 1080)
  sustineri_hr_map_04_ai-scales-what-you-dont-map.png     (1080 × 1080)
  sustineri_hr_map_05_hr-vs-workforce-architecture.png    (1080 × 1080)
```

Source is code-generated for exact reproducibility:
`build_maps.py` (design system) → `generate.py` (map layouts) / `contact.py` →
`render.sh` (headless-Chromium raster to PNG).

---

## Map 01 — HR Is the Face, Not the Source

**Logic.** HR sits just below center as a navy/gold node. Five decision origins —
Executive Leadership, Finance, Operations, Legal/Compliance, Managers/Supervisors — feed
thin steel arrows *into* HR. A single heavy **gold** arrow rises from Employees/Workforce:
the blame vector. Side labels separate "decision origin is often elsewhere" from "visible
accountability lands here." The asymmetry is the message: many quiet inputs, one loud
arrow of blame, all converging on HR.

**Caption.**
> HR is the surface the organization touches, so it's the surface the organization blames.
> But look at the arrows: leadership, finance, operations, and legal all set the terms. HR
> inherits the impact of decisions it rarely gets to make. Before you assign blame, map the
> origin.

**Alt text.** Connective map titled "HR Is the Face, Not the Source." A navy "HR" node sits
below center. Six nodes surround it — Executive Leadership, Finance, Operations, Legal /
Compliance, Managers / Supervisors — each connected by thin steel arrows pointing into HR.
A thick gold arrow labeled "workforce sentiment · blame" points up from an
Employees / Workforce node into HR. Side labels read "decision origin is often elsewhere"
and "visible accountability lands here."

---

## Map 02 — Unlimited PTO Solves One Problem and Creates Another

**Logic.** A left-to-right cause chain (Cost/Liability Pressure → Leadership Decision →
Unlimited PTO Policy) then branches downward. The policy sets Employee Expectation and
Manager Discretion; combined with Workload/Coverage Reality they converge on a gold-outlined
**Conflict/Friction** node, which hands off to HR Enforcement/Interpretation. The visual
shows a clean top row dissolving into a messy convergence — "simple on paper, tangled in
practice."

**Caption.**
> Unlimited PTO removes accrual complexity. It doesn't remove the underlying tension — it
> relocates it. Expectation meets discretion meets coverage reality, and the ambiguity lands
> on HR to interpret and enforce. A policy is not a system. The friction it creates is
> structural, not personal.

**Alt text.** Flow-style connective map titled "Unlimited PTO Solves One Problem and Creates
Another." Top row: Cost / Liability Pressure → Leadership Decision → Unlimited PTO Policy.
The policy branches down to Employee Expectation and Manager Discretion; these plus a
Workload / Coverage Reality node converge on a gold-outlined Conflict / Friction node, which
connects to an HR Enforcement & Interpretation node. A note reads "removes accrual
complexity → introduces ambiguity."

---

## Map 03 — HR Often Becomes a Broken Telephone

**Logic.** A vertical spine from Frontline Work up to Boardroom/Strategy, with HR
highlighted in the middle. A steel rail on the left ("information moves up") and a gold rail
on the right ("decisions move down") show the two flows that never close into a loop. Gold
break-markers on the spine tag the failure points: no feedback loop, signal loss, HR absorbs
friction, translation gap. HR is literally caught in the middle of an open loop.

**Caption.**
> Information climbs. Decisions descend. But nothing closes the loop — so meaning degrades at
> every handoff. HR sits in the middle of that distortion, absorbing friction from both
> directions and getting blamed for a signal it only relayed. Close the loop, or keep
> shooting the messenger.

**Alt text.** Vertical connective map titled "HR Often Becomes a Broken Telephone." Seven
stacked nodes from bottom to top: Frontline Work, Employee Experience, Supervisor, HR
(highlighted), Operations, Leadership, Boardroom / Strategy. A steel upward arrow on the left
is labeled "information moves up"; a gold downward arrow on the right is labeled "decisions
move down." Gold markers on the spine tag "no feedback loop," "signal loss," "HR absorbs
friction," and "translation gap."

---

## Map 04 — AI Will Scale Whatever You Fail to Map

**Logic.** A fan-in / fan-out amplifier. Six unmanaged inputs on the left (Unmapped Process,
Inconsistent Manager Behavior, Undocumented Exceptions, Compliance Variability, Hidden Work,
Poor Governance) converge via steel arrows into a gold **AI / Automation Layer**. That node
fans out via gold arrows into six harms (Scaled Bias, Faster Errors, Policy Drift, Employee
Harm, Compliance Risk, Lawsuits/Exposure). A small bottom sequence — Map → Lock one loop →
Audit → Validate → Expand — is the corrective path.

**Caption.**
> AI is an amplifier, not a corrective. Feed it unmapped process, inconsistent behavior, and
> undocumented exceptions, and it will scale exactly that — faster, wider, and with a
> compliance paper trail. The fix isn't more model. It's structure: map it, lock one loop,
> audit, validate, then expand.

**Alt text.** Connective map titled "AI Will Scale Whatever You Fail to Map." On the left,
six input nodes — Unmapped Process, Inconsistent Manager Behavior, Undocumented Exceptions,
Compliance Variability, Hidden Work, Poor Governance — connect via steel arrows into a central
gold "AI / Automation Layer" node. From there, gold arrows fan out to six outcome nodes:
Scaled Bias, Faster Errors, Policy Drift, Employee Harm, Compliance Risk, Lawsuits / Exposure.
A bottom sequence reads Map → Lock one loop → Audit → Validate → Expand.

---

## Map 05 — HR Is Not the Same as Workforce Architecture

**Logic.** Two grouped panels. Left ("HR Delivery," steel/white nodes): HR Operations, Talent
Acquisition, HR Business Partnering, Learning/Development. Right ("Workforce Architecture,"
navy/gold nodes): Workforce Architecture and Organizational Design rendered as distinct
emphasis blocks, alongside Leadership Strategy and Finance/Cost Inputs. Dashed bridges connect
the two panels — related, but a different colour, a different container: connected, not
interchangeable.

**Caption.**
> HR delivery keeps the organization running. Workforce architecture decides what the
> organization should be. They connect — but they are not the same discipline, and collapsing
> one into the other is how good HR teams get set up to fail. Name the difference before you
> staff it.

**Alt text.** Connective map titled "HR Is Not the Same as Workforce Architecture." Two panels
sit side by side. The left panel, labeled "HR Delivery," contains HR Operations, Talent
Acquisition, HR Business Partnering, and Learning / Development. The right panel, labeled
"Workforce Architecture," contains Workforce Architecture and Organizational Design as
highlighted navy/gold blocks, plus Leadership Strategy and Finance / Cost Inputs. Dashed lines
bridge the two panels, labeled "connected · not interchangeable."

---

## Reproduce

```bash
uv run python3 generate.py    # writes maps/*.html
bash render.sh                # exports/*.png (1080×1080)
uv run python3 contact.py     # writes contact_sheet.html
# then render the contact sheet at 1600×1320 (see render command in git history)
```
