# Sustineri — Connective Map Workflow (PROVISIONAL)

> ## ⚠️ PROVISIONAL CONNECTIVE MAP WORKFLOW
> Created because **no existing workflow was found in this repo/workspace**.
> A canonical Sustineri brand workflow **does exist in ROOT** and takes precedence
> — see [`CANONICAL_VALIDATION.md`](./CANONICAL_VALIDATION.md).
> **Do not merge / do not treat as canonical until validated by the founder.**
>
> Controlling authority (rank-1): `Sustineri_Brand_Kit.md` at
> `00_System_Core/AI_Operating_System/07_Templates/Brand/`. The canonical builder
> is the `sustineri-house-ui` skill, gated by the Brand Inception Gate. This repo
> build did **not** load the kit by path or run the gate, and it carries known
> brand deviations (invented logo, sans headline, gradients/shadows) documented in
> the validation file. Reconcile before promotion.

A provisional, reproducible pipeline for Sustineri **connective-map** social
graphics (LinkedIn thought-leadership). It exists so the SHRM/AI post has a
working asset now; it is a candidate for the ROOT system, not a replacement for it.

## What this is

A brand-locked, code-driven system for producing high-trust systems maps. Layout
is authored in HTML/SVG against the locked brand kit, then rendered to retina PNG
with the pre-installed headless Chromium. Fully reproducible and non-destructive:
edit the source, re-render, source assets are never overwritten.

## Layout

```
source/
  brandkit.css        # LOCKED brand kit — palette, watermark mark, typography, components. Reuse; don't fork.
  render.sh           # headless-Chromium render step: render.sh <in.html> <out.png> <W> <H>
  *_connective_map.html      # portrait master (1080x1350, LinkedIn 4:5)  — working source
  *_connective_map_alt.html  # square alt    (1080x1080, LinkedIn 1:1)    — working source
  *_connective_map_sharp.html # sharper/diagnostic copy variant (portrait) — working source
  *_connective_map_tight.html # fewer-words mobile variant (square)   — working source
output/
  *_watermarked.png        # portrait 4:5, standard copy       (2160x2700 @2x)
  *_watermarked_alt.png    # square 1:1, standard copy          (2160x2160 @2x)
  *_watermarked_sharp.png  # portrait 4:5, sharper/diagnostic   (2160x2700 @2x)
  *_watermarked_tight.png  # square 1:1, fewer words / mobile   (2160x2160 @2x)
caption.md              # suggested LinkedIn caption
CANONICAL_VALIDATION.md # ROOT validation + brand-deviation findings (READ FIRST)
```

## Brand kit (locked)

| Token | Hex | Use |
|-------|-----|-----|
| Navy | `#012564` | primary ink, core node, structural zone |
| Gold | `#ab8834` | accents, solution zone, brand mark ring |
| Gold (bright) | `#e6bb54` | on-navy highlight (core eyebrow) |
| Steel | `#496699` | secondary text, connectors, "reactive" zone |
| Gray | `#dbdbdb` | dividers; desaturated "what broke" zone |

Fonts: Liberation Sans (body/headline), Liberation Serif (the "S" monogram mark).
These are metric-compatible with Arial/Times and render identically headless.

> **Deviation note:** the canonical kit specifies **serif headlines** and treats the
> logo as a protected asset (no substituted wordmark/monogram). This provisional
> build uses a sans headline and an invented mark — both flagged for reconciliation
> in `CANONICAL_VALIDATION.md`.

## Watermark

Established here as the reusable Sustineri watermark method (no standalone mark
asset existed, so one is defined in `brandkit.css` and inlined per page):

1. **Roundel monogram** — navy ring + gold inner ring + serif "S", centered behind
   the core at ~7% opacity. Also used at full opacity as the header/footer logo lockup.
2. **Diagonal wordmark** — "SUSTINERI" set large, letter-spaced, rotated ~-21°,
   ~4.5% opacity, behind the map.

Both sit on `z-index:0` behind all content, so main text stays fully legible.
Visible-but-not-disruptive, integrated into the composition, brand mark undistorted.

## Rebuild / iterate

```bash
cd source
bash render.sh shrm_ai_work_architecture_connective_map.html \
     ../output/shrm_ai_work_architecture_connective_map_watermarked.png 1080 1350
bash render.sh shrm_ai_work_architecture_connective_map_alt.html \
     ../output/shrm_ai_work_architecture_connective_map_watermarked_alt.png 1080 1080
```

Chromium binary: `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`
(`--force-device-scale-factor=2` gives the 2× retina export.)

## The map (SHRM / AI work-architecture)

Central thesis: **Map the Work Before You Scale the Tool.** Four zones flow
clockwise 1→2→3→4:

1. **Reactive HR Frame** (steel) — what SHRM & mainstream HR emphasized
2. **What Was Actually Missing** (navy) — the unmapped work ecosystem
3. **What Broke Under AI** (gray, desaturated) — AI dropped into unmapped systems
4. **The Solution Path** (gold) — connective mapping → responsible scaling

Reactive framing → missing architecture → structural failure → connective solution.
