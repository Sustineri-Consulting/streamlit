#!/usr/bin/env python3
"""
Sustineri — HR Micro Connective Maps generator.

Builds a matched series of 1080x1080 connective-map graphics as self-contained
HTML/SVG files, rendered to PNG via headless Chromium.

Design system (locked Sustineri brand kit):
  Navy  #012564   Gold #ab8834 / #e6bb54   Steel #496699   Light gray #dbdbdb
Editorial, connective, high-signal. Thin/medium connectors, geometric nodes.
"""

import html

# ---- Brand palette ---------------------------------------------------------
NAVY = "#012564"
GOLD = "#ab8834"
GOLD_LT = "#e6bb54"
STEEL = "#496699"
GRAY = "#dbdbdb"
GRAY_DK = "#8a93a3"
INK = "#0d1b3d"
BG = "#f6f7f9"
PANEL = "#eef1f5"

W = H = 1080

# ---- Geometry helpers ------------------------------------------------------


class Node:
    def __init__(self, cx, cy, w, h, lines, style):
        self.cx, self.cy, self.w, self.h = cx, cy, w, h
        self.lines, self.style = lines, style

    @property
    def left(self):
        return self.cx - self.w / 2

    @property
    def right(self):
        return self.cx + self.w / 2

    @property
    def top(self):
        return self.cy - self.h / 2

    @property
    def bottom(self):
        return self.cy + self.h / 2

    def border_point(self, tx, ty):
        """Point on this node's rounded-rect border toward (tx,ty)."""
        dx, dy = tx - self.cx, ty - self.cy
        if dx == 0 and dy == 0:
            return self.cx, self.cy
        hw, hh = self.w / 2, self.h / 2
        sx = hw / abs(dx) if dx != 0 else float("inf")
        sy = hh / abs(dy) if dy != 0 else float("inf")
        s = min(sx, sy)
        return self.cx + dx * s, self.cy + dy * s


def measure(lines, fs, weight=600, spacing=0):
    """Rough width of the widest line in px."""
    factor = 0.60 if weight >= 600 else 0.55
    widest = 0.0
    for ln in lines:
        w = len(ln) * fs * factor + len(ln) * spacing
        widest = max(widest, w)
    return widest


# ---- Node styles -----------------------------------------------------------
# Each style: fill, stroke, stroke_w, text color, font-weight, radius, accent
STYLES = {
    # neutral source / context node
    "source": dict(fill="#ffffff", stroke=STEEL, sw=2, tc=NAVY, fw=600, r=16),
    # the HR protagonist — navy block w/ gold ring
    "hr": dict(fill=NAVY, stroke=GOLD, sw=3.5, tc="#ffffff", fw=700, r=16),
    # decision / leadership emphasis
    "lead": dict(fill="#ffffff", stroke=NAVY, sw=2.5, tc=NAVY, fw=700, r=16),
    # amplifier (AI center)
    "amp": dict(fill=GOLD, stroke=NAVY, sw=3, tc=NAVY, fw=700, r=16),
    # negative outcome — muted
    "bad": dict(fill=PANEL, stroke=GRAY_DK, sw=1.5, tc="#334", fw=600, r=14),
    # architecture / strategy emphasis
    "arch": dict(fill=NAVY, stroke=GOLD, sw=2.5, tc="#ffffff", fw=700, r=16),
    # soft input
    "soft": dict(fill="#ffffff", stroke=GRAY_DK, sw=1.5, tc="#334", fw=600, r=14),
    # friction / warning
    "warn": dict(fill="#fbf1dc", stroke=GOLD, sw=2.5, tc=NAVY, fw=700, r=16),
    # neutral strategy
    "strat": dict(fill="#ffffff", stroke=NAVY, sw=2, tc=NAVY, fw=600, r=16),
}


def svg_node(n: Node):
    st = n.style
    fs = st.get("fs", 25)
    lh = fs * 1.16
    total = (len(n.lines) - 1) * lh
    y0 = n.cy - total / 2 + fs * 0.34
    tspans = []
    for i, ln in enumerate(n.lines):
        y = y0 + i * lh
        tspans.append(
            f'<text x="{n.cx:.1f}" y="{y:.1f}" text-anchor="middle" '
            f'font-size="{fs}" font-weight="{st["fw"]}" fill="{st["tc"]}" '
            f'font-family="Liberation Sans, Arial, sans-serif" '
            f'letter-spacing="0.2">{html.escape(ln)}</text>'
        )
    rect = (
        f'<rect x="{n.left:.1f}" y="{n.top:.1f}" width="{n.w:.1f}" height="{n.h:.1f}" '
        f'rx="{st["r"]}" ry="{st["r"]}" fill="{st["fill"]}" stroke="{st["stroke"]}" '
        f'stroke-width="{st["sw"]}"/>'
    )
    return rect + "".join(tspans)


def make_node(cx, cy, lines, style_key, pad_x=30, pad_y=20, fs=25, minw=0):
    st = dict(STYLES[style_key])
    st["fs"] = fs
    w = max(measure(lines, fs, st["fw"]) + pad_x * 2, minw)
    h = len(lines) * (fs * 1.16) + pad_y * 2 - fs * 0.16
    return Node(cx, cy, w, h, lines, st)


# ---- Edges -----------------------------------------------------------------


def edge(a: Node, b: Node, kind="flow", curve=0.0, ax=None, ay=None, bx=None, by=None):
    """Connector from node a to node b with an arrowhead at b."""
    x1, y1 = a.border_point(
        bx if bx is not None else b.cx, by if by is not None else b.cy
    )
    x2, y2 = b.border_point(
        ax if ax is not None else a.cx, ay if ay is not None else a.cy
    )
    styles = {
        "flow": (STEEL, 2.2, "none", "arrow-steel"),
        "faint": (STEEL, 1.6, "none", "arrow-steel"),
        "blame": (GOLD, 6.0, "none", "arrow-gold-big"),
        "gold": (GOLD, 3.0, "none", "arrow-gold"),
        "dash": (GRAY_DK, 2.0, "7 6", "arrow-gray"),
        "info": (STEEL, 2.4, "none", "arrow-steel"),
        "down": (GOLD, 2.4, "none", "arrow-gold"),
    }
    col, sw, dash, marker = styles[kind]
    dasharr = f'stroke-dasharray="{dash}" ' if dash != "none" else ""
    if curve:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        # perpendicular offset
        ndx, ndy = (y2 - y1), -(x2 - x1)
        ln = (ndx**2 + ndy**2) ** 0.5 or 1
        cxp, cyp = mx + ndx / ln * curve, my + ndy / ln * curve
        d = f"M {x1:.1f} {y1:.1f} Q {cxp:.1f} {cyp:.1f} {x2:.1f} {y2:.1f}"
    else:
        d = f"M {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f}"
    return (
        f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" '
        f'{dasharr}stroke-linecap="round" marker-end="url(#{marker})"/>'
    )


def tag(x, y, text, color=GOLD, anchor="middle", fs=18, italic=True):
    style = "italic" if italic else "normal"
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{fs}" '
        f'font-style="{style}" font-weight="600" fill="{color}" '
        f'font-family="Liberation Sans, Arial, sans-serif" '
        f'letter-spacing="0.3">{html.escape(text)}</text>'
    )


def sidenote(x, y, text, w=250, anchor="start"):
    """Small boxed side note with a gold left rule."""
    return (
        f'<line x1="{x}" y1="{y - 16}" x2="{x}" y2="{y + 16}" stroke="{GOLD}" stroke-width="3"/>'
        f'<text x="{x + 14}" y="{y - 2}" font-size="17" font-weight="600" fill="{STEEL}" '
        f'font-family="Liberation Sans, Arial, sans-serif" letter-spacing="0.2">'
        f"{html.escape(text)}</text>"
    )


DEFS = f"""
<defs>
  <marker id="arrow-steel" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7"
    markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="{STEEL}"/></marker>
  <marker id="arrow-gold" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7"
    markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="{GOLD}"/></marker>
  <marker id="arrow-gold-big" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5.5"
    markerHeight="5.5" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="{GOLD}"/></marker>
  <marker id="arrow-gray" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7"
    markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="{GRAY_DK}"/></marker>
</defs>
"""


# ---- Page template ---------------------------------------------------------


def page(num, headline_lines, subline, map_svg):
    kicker = "SUSTINERI  ·  CONNECTIVE MAP"
    idx = f"{num:02d} / 05"
    head = ""
    hy = 118
    for i, ln in enumerate(headline_lines):
        head += (
            f'<text x="70" y="{hy + i * 54}" font-size="46" font-weight="800" '
            f'fill="{NAVY}" font-family="Liberation Sans, Arial, sans-serif" '
            f'letter-spacing="-0.4">{html.escape(ln)}</text>'
        )
    sub_y = hy + len(headline_lines) * 54 + 8
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
  html,body{{margin:0;padding:0}}
  #stage{{width:{W}px;height:{H}px;background:{BG};position:relative;
    font-family:'Liberation Sans', Arial, sans-serif;}}
</style></head>
<body><div id="stage">
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  {DEFS}
  <rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>
  <!-- header -->
  <text x="70" y="60" font-size="19" font-weight="700" fill="{STEEL}"
     letter-spacing="3.2" font-family="Liberation Sans, Arial, sans-serif">{kicker}</text>
  <text x="{W - 70}" y="60" text-anchor="end" font-size="19" font-weight="700" fill="{GOLD}"
     letter-spacing="2" font-family="Liberation Sans, Arial, sans-serif">{idx}</text>
  {head}
  <text x="70" y="{sub_y}" font-size="22" font-weight="500" fill="{STEEL}"
     font-family="Liberation Sans, Arial, sans-serif" letter-spacing="0.2">{html.escape(subline)}</text>
  <line x1="70" y1="{sub_y + 22}" x2="{W - 70}" y2="{sub_y + 22}" stroke="{GRAY}" stroke-width="1.5"/>
  <!-- map -->
  {map_svg}
  <!-- footer -->
  <line x1="70" y1="1006" x2="{W - 70}" y2="1006" stroke="{GRAY}" stroke-width="1.5"/>
  <circle cx="78" cy="1042" r="7" fill="{GOLD}"/>
  <text x="96" y="1049" font-size="24" font-weight="800" fill="{NAVY}"
     letter-spacing="0.5" font-family="Liberation Sans, Arial, sans-serif">Sustineri</text>
  <text x="{W - 70}" y="1049" text-anchor="end" font-size="17" font-weight="600" fill="{GRAY_DK}"
     letter-spacing="0.4" font-family="Liberation Sans, Arial, sans-serif">Workforce architecture, mapped.</text>
</svg>
</div></body></html>"""


def band(text, y, cx=W / 2, fs=None):
    """Bottom 'short text on image' emphasis band. A small gold marker anchors it."""
    if fs is None:
        fs = 22 if len(text) <= 58 else (20 if len(text) <= 70 else 18)
    return (
        f'<rect x="70" y="{y}" width="{W - 140}" height="58" rx="12" fill="{NAVY}"/>'
        f'<rect x="70" y="{y}" width="6" height="58" rx="3" fill="{GOLD}"/>'
        f'<text x="{cx}" y="{y + 38}" text-anchor="middle" font-size="{fs}" font-weight="600" '
        f'fill="#ffffff" font-family="Liberation Sans, Arial, sans-serif" '
        f'letter-spacing="0.2">{html.escape(text)}</text>'
    )
