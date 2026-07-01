#!/usr/bin/env python3
"""Generate the 5 Sustineri HR connective maps as HTML files."""

import os

from build_maps import (
    GOLD,
    GRAY,
    GRAY_DK,
    STEEL,
    band,
    edge,
    make_node,
    page,
    sidenote,
    svg_node,
    tag,
)

HERE = os.path.dirname(os.path.abspath(__file__))
MAPS = os.path.join(HERE, "maps")
os.makedirs(MAPS, exist_ok=True)


def render_nodes(nodes):
    return "".join(svg_node(n) for n in nodes)


# ===========================================================================
# MAP 01 — HR Is the Face, Not the Source
# ===========================================================================
def map01():
    hr = make_node(540, 662, ["HR"], "hr", fs=40, minw=190, pad_y=30)
    exec_ = make_node(540, 300, ["Executive", "Leadership"], "lead", fs=23)
    fin = make_node(250, 330, ["Finance"], "source", fs=23)
    ops = make_node(830, 330, ["Operations"], "source", fs=23)
    legal = make_node(185, 505, ["Legal /", "Compliance"], "source", fs=23)
    mgr = make_node(900, 505, ["Managers /", "Supervisors"], "source", fs=23)
    emp = make_node(540, 870, ["Employees /", "Workforce"], "source", fs=23)

    sources = [exec_, fin, ops, legal, mgr]
    edges = "".join(edge(s, hr, "flow") for s in sources)
    blame = edge(emp, hr, "blame")

    labels = (
        tag(540, 244, "DECISION ORIGIN IS OFTEN ELSEWHERE", GOLD, fs=18, italic=False)
        + sidenote(672, 690, "Visible accountability lands here")
        + tag(690, 800, "workforce sentiment  ·  blame", GOLD, "start", fs=19)
    )
    body = (
        edges
        + blame
        + render_nodes(sources + [emp, hr])
        + labels
        + band("HR is where the impact shows up — not where the decision started.", 930)
    )
    return page(
        1,
        ["HR Is the Face, Not the Source"],
        "Visible accountability vs. actual decision origin",
        body,
    )


# ===========================================================================
# MAP 02 — Unlimited PTO Solves One Problem and Creates Another
# ===========================================================================
def map02():
    cost = make_node(210, 335, ["Cost /", "Liability Pressure"], "source", fs=22)
    lead = make_node(540, 335, ["Leadership", "Decision"], "lead", fs=22)
    pto = make_node(858, 335, ["Unlimited", "PTO Policy"], "arch", fs=22)

    emp = make_node(215, 545, ["Employee", "Expectation"], "source", fs=22)
    disc = make_node(540, 545, ["Manager", "Discretion"], "source", fs=22)
    work = make_node(865, 545, ["Workload /", "Coverage Reality"], "source", fs=22)

    conf = make_node(360, 735, ["Conflict /", "Friction"], "warn", fs=23)
    hr = make_node(760, 735, ["HR Enforcement", "& Interpretation"], "hr", fs=22)

    e = []
    e.append(edge(cost, lead, "flow"))
    e.append(edge(lead, pto, "flow"))
    e.append(edge(pto, emp, "flow", curve=40))
    e.append(edge(pto, disc, "flow"))
    e.append(edge(emp, conf, "flow"))
    e.append(edge(disc, conf, "flow"))
    e.append(edge(work, conf, "flow"))
    e.append(edge(conf, hr, "gold"))

    labels = tag(
        540,
        858,
        "Removes accrual complexity  →  introduces ambiguity",
        GOLD,
        "middle",
        fs=21,
    )
    body = (
        "".join(e)
        + render_nodes([cost, lead, pto, emp, disc, work, conf, hr])
        + labels
        + band("A clean policy on paper can become messy in practice.", 930)
    )
    return page(
        2,
        ["Unlimited PTO Solves One Problem —", "and Creates Another"],
        "How a simple policy turns into operational friction",
        body,
    )


# ===========================================================================
# MAP 03 — HR Often Becomes a Broken Telephone
# ===========================================================================
def map03():
    cx = 430
    board = make_node(cx, 300, ["Boardroom /", "Strategy"], "lead", fs=22)
    lead = make_node(cx, 392, ["Leadership"], "source", fs=22)
    ops = make_node(cx, 484, ["Operations"], "source", fs=22)
    hr = make_node(cx, 576, ["HR"], "hr", fs=28, minw=170)
    sup = make_node(cx, 668, ["Supervisor"], "source", fs=22)
    exp = make_node(cx, 760, ["Employee", "Experience"], "source", fs=22)
    front = make_node(cx, 852, ["Frontline", "Work"], "source", fs=22)

    stack = [board, lead, ops, hr, sup, exp, front]
    # chain connectors (thin, neutral)
    chain = ""
    for a, b in zip(stack, stack[1:]):
        x1, y1 = a.cx, a.bottom
        x2, y2 = b.cx, b.top
        chain += (
            f'<line x1="{x1}" y1="{y1:.1f}" x2="{x2}" y2="{y2:.1f}" '
            f'stroke="{GRAY_DK}" stroke-width="1.8"/>'
        )

    # directional rails
    rails = (
        f'<line x1="205" y1="850" x2="205" y2="302" stroke="{STEEL}" stroke-width="3" '
        f'marker-end="url(#arrow-steel)"/>'
        f'<line x1="655" y1="310" x2="655" y2="858" stroke="{GOLD}" stroke-width="3" '
        f'marker-end="url(#arrow-gold)"/>'
        f'<text x="188" y="580" transform="rotate(-90 188 580)" text-anchor="middle" '
        f'font-size="17" font-weight="700" fill="{STEEL}" letter-spacing="2.5" '
        f'font-family="Liberation Sans, Arial, sans-serif">INFORMATION MOVES UP</text>'
        f'<text x="672" y="580" transform="rotate(90 672 580)" text-anchor="middle" '
        f'font-size="17" font-weight="700" fill="{GOLD}" letter-spacing="2.5" '
        f'font-family="Liberation Sans, Arial, sans-serif">DECISIONS MOVE DOWN</text>'
    )

    def breakdown(y, text):
        # broken-line marker crossing the spine + gold tag to the right
        return (
            f'<circle cx="{cx}" cy="{y}" r="6" fill="#fff" stroke="{GOLD}" stroke-width="3"/>'
            + tag(710, y + 5, text, GOLD, "start", fs=18)
        )

    marks = (
        breakdown(346, "no feedback loop")  # boardroom <-> leadership
        + breakdown(530, "signal loss")  # ops <-> hr
        + tag(710, 581, "HR absorbs friction", GOLD, "start", fs=18)  # at HR
        + breakdown(714, "translation gap")  # supervisor <-> employee exp
    )

    body = (
        rails
        + chain
        + render_nodes(stack)
        + marks
        + band(
            "When the loop is not closed, HR becomes the messenger and the target.", 930
        )
    )
    return page(
        3,
        ["HR Often Becomes", "a Broken Telephone"],
        "Signal loss between frontline reality and strategy",
        body,
    )


# ===========================================================================
# MAP 04 — AI Will Scale Whatever You Fail to Map
# ===========================================================================
def map04():
    lx, rx = 200, 880
    ys = [292, 384, 476, 568, 660, 752]
    left_labels = [
        ["Unmapped Process"],
        ["Inconsistent", "Manager Behavior"],
        ["Undocumented", "Exceptions"],
        ["Compliance", "Variability"],
        ["Hidden Work"],
        ["Poor Governance"],
    ]
    right_labels = [
        ["Scaled Bias"],
        ["Faster Errors"],
        ["Policy Drift"],
        ["Employee Harm"],
        ["Compliance Risk"],
        ["Lawsuits /", "Exposure"],
    ]
    left = [
        make_node(lx, y, l, "soft", fs=19, pad_x=20) for y, l in zip(ys, left_labels)
    ]
    right = [
        make_node(rx, y, l, "bad", fs=19, pad_x=20) for y, l in zip(ys, right_labels)
    ]
    ai = make_node(
        540, 522, ["AI /", "Automation Layer"], "amp", fs=26, minw=230, pad_y=26
    )

    e = "".join(edge(n, ai, "flow") for n in left)
    e += "".join(edge(ai, n, "gold") for n in right)

    # bottom fix-sequence
    seq = ["Map", "Lock one loop", "Audit", "Validate", "Expand"]
    sy = 858
    pills = f'<text x="70" y="{sy + 6}" font-size="17" font-weight="700" fill="{STEEL}" letter-spacing="2" font-family="Liberation Sans, Arial, sans-serif">THE FIX</text>'
    px = 205
    prev = None
    for i, s in enumerate(seq):
        w = len(s) * 20 * 0.6 + 40
        n = make_node(px + w / 2, sy, [s], "strat", fs=19, pad_y=13)
        if prev is not None:
            pills += edge(prev, n, "flow")
        pills += svg_node(n)
        prev = n
        px += w + 46

    body = (
        e
        + render_nodes(left + right)
        + svg_node(ai)
        + pills
        + band("AI does not fix broken structure. It accelerates it.", 928)
    )
    return page(
        4,
        ["AI Will Scale Whatever", "You Fail to Map"],
        "Automation amplifies whatever structure it inherits",
        body,
    )


# ===========================================================================
# MAP 05 — HR Is Not the Same as Workforce Architecture
# ===========================================================================
def map05():
    # panels
    lpx, lpw = 82, 420
    rpx, rpw = 578, 420
    ptop, ph = 330, 560
    panels = (
        f'<rect x="{lpx}" y="{ptop}" width="{lpw}" height="{ph}" rx="22" fill="#eef1f5" stroke="{GRAY}" stroke-width="1.5"/>'
        f'<rect x="{rpx}" y="{ptop}" width="{rpw}" height="{ph}" rx="22" fill="#f4f1e8" stroke="#d9cfb2" stroke-width="1.5"/>'
        f'<text x="{lpx + 26}" y="{ptop + 42}" font-size="19" font-weight="800" fill="{STEEL}" letter-spacing="2.5" font-family="Liberation Sans, Arial, sans-serif">HR DELIVERY</text>'
        f'<text x="{rpx + 26}" y="{ptop + 42}" font-size="19" font-weight="800" fill="{GOLD}" letter-spacing="2.5" font-family="Liberation Sans, Arial, sans-serif">WORKFORCE ARCHITECTURE</text>'
    )
    lcx, rcx = lpx + lpw / 2, rpx + rpw / 2
    lys = [430, 540, 650, 760]
    left = [
        make_node(lcx, lys[0], ["HR Operations"], "source", fs=22),
        make_node(lcx, lys[1], ["Talent Acquisition"], "source", fs=22),
        make_node(lcx, lys[2], ["HR Business", "Partnering"], "source", fs=22),
        make_node(lcx, lys[3], ["Learning /", "Development"], "source", fs=22),
    ]
    right = [
        make_node(rcx, lys[0], ["Workforce", "Architecture"], "arch", fs=22),
        make_node(rcx, lys[1], ["Organizational", "Design"], "arch", fs=22),
        make_node(rcx, lys[2], ["Leadership Strategy"], "lead", fs=22),
        make_node(rcx, lys[3], ["Finance /", "Cost Inputs"], "source", fs=22),
    ]
    # bridges — connected, not interchangeable (dashed)
    bridges = (
        edge(left[2], right[1], "dash")
        + edge(left[3], right[0], "dash")
        + edge(left[0], right[2], "dash")
    )
    bridge_label = tag(
        540, 300, "CONNECTED · NOT INTERCHANGEABLE", GOLD, fs=18, italic=False
    )

    body = (
        panels
        + bridges
        + render_nodes(left + right)
        + bridge_label
        + band("Connected functions are not the same function.", 930)
    )
    return page(
        5,
        ["HR Is Not the Same as", "Workforce Architecture"],
        "Related functions are not interchangeable functions",
        body,
    )


BUILDERS = {
    "sustineri_hr_map_01_hr-is-the-face-not-the-source": map01,
    "sustineri_hr_map_02_unlimited-pto": map02,
    "sustineri_hr_map_03_broken-telephone": map03,
    "sustineri_hr_map_04_ai-scales-what-you-dont-map": map04,
    "sustineri_hr_map_05_hr-vs-workforce-architecture": map05,
}

if __name__ == "__main__":
    for name, fn in BUILDERS.items():
        path = os.path.join(MAPS, name + ".html")
        with open(path, "w") as f:
            f.write(fn())
        print("wrote", path)
