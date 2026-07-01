#!/usr/bin/env python3
"""Generate the People 404 'Connective Mapping' micro map as an SVG.

The graphic has four conceptual layers arranged as a radial map (center node +
three concentric rings) plus a side-by-side "Formal Org Chart" vs "Actual Work
Chart" comparison. Colors follow the Sustineri brand palette.

Run:  python3 generate_map.py   ->  writes connective_map.svg
"""

import math
from html import escape

# ---------------------------------------------------------------- brand palette
NAVY = "#012564"
GOLD = "#ab8834"
GOLD_BRIGHT = "#e6bb54"
STEEL = "#496699"
GRAY = "#dbdbdb"
INK = "#0d1b34"  # near-navy text on light backgrounds
BG = "#f6f7f9"  # clean off-white canvas
PANEL = "#ffffff"
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"

W, H = 1240, 1900


# ---------------------------------------------------------------- text helpers
def text_w(s, size):
    """Rough Arial/Helvetica advance width."""
    return len(s) * size * 0.56


def wrap(text, max_chars):
    """Greedy word wrap; keeps a trailing '/' attached to its word."""
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if len(cand) > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return lines


svg = []


def add(s):
    svg.append(s)


def pill(cx, cy, lines, *, fill, stroke, text_color, size, dashed=False, bold=False):
    """Rounded 'pill' node centered at (cx, cy) holding 1-3 lines of text."""
    pad_x, pad_y = 22, 14
    line_h = size + 6
    tw = max(text_w(l, size) for l in lines)
    pw = tw + pad_x * 2
    ph = line_h * len(lines) + pad_y * 2
    x, y = cx - pw / 2, cy - ph / 2
    r = ph / 2
    dash = ' stroke-dasharray="4 5"' if dashed else ""
    add(
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{pw:.1f}" height="{ph:.1f}" '
        f'rx="{r:.1f}" ry="{r:.1f}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="1.5"{dash}/>'
    )
    total_h = line_h * len(lines)
    start = cy - total_h / 2 + line_h / 2
    weight = 700 if bold else 600
    for i, l in enumerate(lines):
        ty = start + i * line_h + size * 0.35
        add(
            f'<text x="{cx:.1f}" y="{ty:.1f}" font-family="{FONT}" '
            f'font-size="{size}" font-weight="{weight}" fill="{text_color}" '
            f'text-anchor="middle">{escape(l)}</text>'
        )
    return pw, ph


# ================================================================ canvas
add(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}" font-family="{FONT}">'
)
add("<defs>")
add(
    f'<linearGradient id="centerGrad" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="#023081"/>'
    f'<stop offset="1" stop-color="{NAVY}"/></linearGradient>'
)
add(
    f'<linearGradient id="footerGrad" x1="0" y1="0" x2="1" y2="0">'
    f'<stop offset="0" stop-color="{NAVY}"/>'
    f'<stop offset="1" stop-color="#02194a"/></linearGradient>'
)
add(
    '<filter id="soft" x="-20%" y="-20%" width="140%" height="140%">'
    '<feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0b1b3a" '
    'flood-opacity="0.14"/></filter>'
)
add("</defs>")
add(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# ================================================================ header
add(
    f'<text x="{W / 2}" y="76" font-size="21" font-weight="700" fill="{GOLD}" '
    f'text-anchor="middle" letter-spacing="4">CONNECTIVE MAPPING &#183; PEOPLE 404&#8482;</text>'
)
add(
    f'<text x="{W / 2}" y="132" font-size="43" font-weight="800" fill="{NAVY}" '
    f'text-anchor="middle">Connective Mapping Starts Where the</text>'
)
add(
    f'<text x="{W / 2}" y="182" font-size="43" font-weight="800" fill="{NAVY}" '
    f'text-anchor="middle">Work Actually Happens</text>'
)
add(
    f'<rect x="{W / 2 - 70}" y="204" width="140" height="5" rx="2.5" fill="{GOLD_BRIGHT}"/>'
)
add(
    f'<text x="{W / 2}" y="250" font-size="22" font-weight="500" fill="{STEEL}" '
    f'text-anchor="middle">Start with the roles the system can&#8217;t function without &#8212; '
    f"then map who depends on them,</text>"
)
add(
    f'<text x="{W / 2}" y="280" font-size="22" font-weight="500" fill="{STEEL}" '
    f'text-anchor="middle">what they fix, and what breaks when that work is interrupted.</text>'
)

# ================================================================ radial map
CX, CY = W / 2, 790
R1, R2, R3 = 232, 358, 488  # daily work / dependencies / failure signals

# faint concentric guide circles
for r in (R1, R2, R3):
    add(
        f'<circle cx="{CX}" cy="{CY}" r="{r}" fill="none" stroke="{GRAY}" '
        f'stroke-width="1.4" stroke-dasharray="2 7" opacity="0.9"/>'
    )

# ---- ring data (angles start at top, -90 deg, clockwise) ----
daily = [
    "Fixes issues",
    "Moves information",
    "Keeps records clean",
    "Supports decisions",
    "Prevents delays",
]
deps = [
    "Leadership decisions",
    "Customer / client experience",
    "Compliance",
    "Payroll / finance",
    "Operations",
    "Technology",
    "Field execution",
]
fails = [
    "Delays",
    "Duplicate work",
    "Confusion",
    "Rework",
    "Burnout",
    "Missed handoffs",
    "Decision bottlenecks",
]


def ring_positions(items, radius, start_deg):
    n = len(items)
    out = []
    for i, it in enumerate(items):
        a = math.radians(start_deg + i * 360 / n)
        out.append((it, CX + radius * math.cos(a), CY + radius * math.sin(a)))
    return out


# connector lines: center -> daily work (the work the role personally does)
for it, x, y in ring_positions(daily, R1, -90):
    add(
        f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" '
        f'stroke="{STEEL}" stroke-width="1.6" opacity="0.5"/>'
    )

# outer ring (failure signals) - drawn first so inner rings sit on top
for it, x, y in ring_positions(fails, R3, -90 + (360 / len(fails)) / 2):
    pill(
        x,
        y,
        wrap(it, 11),
        fill="#eceef1",
        stroke=STEEL,
        text_color=NAVY,
        size=19,
        dashed=True,
    )

# second ring (dependencies)
for it, x, y in ring_positions(deps, R2, -90):
    pill(
        x,
        y,
        wrap(it, 12),
        fill=STEEL,
        stroke="#2f4d70",
        text_color="#ffffff",
        size=19,
    )

# first ring (daily work)
for it, x, y in ring_positions(daily, R1, -90):
    pill(
        x,
        y,
        wrap(it, 12),
        fill=GOLD_BRIGHT,
        stroke=GOLD,
        text_color=NAVY,
        size=19,
        bold=True,
    )

# center node
cw, ch = 238, 116
add(
    f'<rect x="{CX - cw / 2}" y="{CY - ch / 2}" width="{cw}" height="{ch}" rx="16" '
    f'fill="url(#centerGrad)" stroke="{GOLD}" stroke-width="2.5" filter="url(#soft)"/>'
)
add(
    f'<text x="{CX}" y="{CY - 14}" font-size="26" font-weight="800" fill="#ffffff" '
    f'text-anchor="middle">Critical Function</text>'
)
add(
    f'<text x="{CX}" y="{CY + 16}" font-size="26" font-weight="800" fill="{GOLD_BRIGHT}" '
    f'text-anchor="middle">Role</text>'
)
add(
    f'<text x="{CX}" y="{CY + 44}" font-size="15" font-weight="500" '
    f'fill="#c7d2e8" text-anchor="middle">The work the system depends on</text>'
)

# ---- legend ----
LEG_Y = 1318
legend = [
    (GOLD_BRIGHT, GOLD, NAVY, "Daily work"),
    (STEEL, STEEL, "#ffffff", "Who / what depends on them"),
    ("#eceef1", STEEL, NAVY, "What breaks when work stops"),
]
# measure to center the row
gap = 40
chip = 20
seg_ws = [chip + 10 + text_w(lbl, 20) for *_, lbl in legend]
total = sum(seg_ws) + gap * (len(legend) - 1)
lx = W / 2 - total / 2
for (fill, stroke, _tc, lbl), sw in zip(legend, seg_ws):
    dash = ' stroke-dasharray="3 4"' if lbl.startswith("What breaks") else ""
    add(
        f'<rect x="{lx:.1f}" y="{LEG_Y - chip + 4}" width="{chip}" height="{chip}" '
        f'rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.5"{dash}/>'
    )
    add(
        f'<text x="{lx + chip + 10:.1f}" y="{LEG_Y}" font-size="20" font-weight="600" '
        f'fill="{INK}" text-anchor="start">{escape(lbl)}</text>'
    )
    lx += sw + gap

# ================================================================ comparison
add(
    f'<text x="{W / 2}" y="1402" font-size="27" font-weight="800" fill="{NAVY}" '
    f'text-anchor="middle">Same role. Two very different pictures.</text>'
)

PY, PH = 1430, 340
PAD = 60
PWD = (W - PAD * 3) / 2
lx0 = PAD
rx0 = PAD * 2 + PWD


def panel(x, title, items, *, accent, muted=False):
    header_fill = GRAY if muted else NAVY
    title_col = "#54627a" if muted else "#ffffff"
    add(
        f'<rect x="{x}" y="{PY}" width="{PWD:.1f}" height="{PH}" rx="16" '
        f'fill="{PANEL}" stroke="{accent}" stroke-width="{2 if muted else 3}" '
        f'filter="url(#soft)"/>'
    )
    add(
        f'<path d="M{x + 16},{PY} h{PWD - 32:.1f} a16,16 0 0 1 16,16 v46 h{-PWD:.1f} '
        f'v-46 a16,16 0 0 1 16,-16 z" fill="{header_fill}"/>'
    )
    add(
        f'<text x="{x + PWD / 2:.1f}" y="{PY + 42}" font-size="24" font-weight="800" '
        f'fill="{title_col}" text-anchor="middle">{escape(title)}</text>'
    )
    iy = PY + 104
    for it in items:
        add(f'<circle cx="{x + 40}" cy="{iy - 6}" r="5" fill="{accent}"/>')
        add(
            f'<text x="{x + 60}" y="{iy}" font-size="21" font-weight="{500 if muted else 600}" '
            f'fill="{"#5a6478" if muted else INK}" text-anchor="start">{escape(it)}</text>'
        )
        iy += 50


panel(
    lx0,
    "Formal Org Chart",
    ["Title", "Department", "Reporting line"],
    accent="#b9bfc9",
    muted=True,
)
panel(
    rx0,
    "Actual Work Chart",
    [
        "Who depends on them",
        "What they fix",
        "What breaks without them",
        "Where the work really moves",
    ],
    accent=GOLD,
)

# center arrow: formal -> actual
axc = W / 2
ayc = PY + PH / 2
add(
    f'<circle cx="{axc}" cy="{ayc}" r="30" fill="{NAVY}" stroke="{GOLD}" stroke-width="2.5"/>'
)
add(
    f'<path d="M{axc - 11},{ayc - 9} L{axc + 9},{ayc} L{axc - 11},{ayc + 9}" fill="none" '
    f'stroke="{GOLD_BRIGHT}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
)

# ================================================================ footer
FY = 1810
add(f'<rect x="0" y="{FY}" width="{W}" height="{H - FY}" fill="url(#footerGrad)"/>')
add(f'<rect x="0" y="{FY}" width="{W}" height="4" fill="{GOLD}"/>')
add(
    f'<text x="{W / 2}" y="{FY + 56}" font-size="25" font-weight="700" fill="#ffffff" '
    f'text-anchor="middle">Sustineri Consulting Group '
    f'<tspan fill="{GOLD_BRIGHT}">&#124;</tspan> '
    f'<tspan fill="{GOLD_BRIGHT}">People 404&#8482;</tspan></text>'
)

add("</svg>")

with open("connective_map.svg", "w") as f:
    f.write("\n".join(svg))
print("wrote connective_map.svg", W, H)
