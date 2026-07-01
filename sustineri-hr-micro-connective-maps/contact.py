#!/usr/bin/env python3
"""Build a contact-sheet preview (all 5 maps together)."""

import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EXPORTS = os.path.join(HERE, "exports")

NAVY, GOLD, STEEL, GRAY, BG = "#012564", "#ab8834", "#496699", "#dbdbdb", "#f6f7f9"

CW, CH = 1600, 1320

maps = [
    (
        "01",
        "HR Is the Face, Not the Source",
        "sustineri_hr_map_01_hr-is-the-face-not-the-source.png",
    ),
    (
        "02",
        "Unlimited PTO Creates a New Problem",
        "sustineri_hr_map_02_unlimited-pto.png",
    ),
    (
        "03",
        "HR Often Becomes a Broken Telephone",
        "sustineri_hr_map_03_broken-telephone.png",
    ),
    (
        "04",
        "AI Will Scale Whatever You Fail to Map",
        "sustineri_hr_map_04_ai-scales-what-you-dont-map.png",
    ),
    (
        "05",
        "HR Is Not the Same as Workforce Architecture",
        "sustineri_hr_map_05_hr-vs-workforce-architecture.png",
    ),
]


def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


cells = ""
for num, title, fn in maps:
    src = b64(os.path.join(EXPORTS, fn))
    cells += f"""
    <div class="cell">
      <div class="thumb"><img src="{src}"/></div>
      <div class="cap"><span class="num">{num}</span>{title}</div>
    </div>"""

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
  html,body{{margin:0;padding:0}}
  #sheet{{width:{CW}px;height:{CH}px;background:{BG};
    font-family:'Liberation Sans',Arial,sans-serif;box-sizing:border-box;
    padding:34px 44px 40px;}}
  .head{{display:flex;justify-content:space-between;align-items:flex-end;
    border-bottom:2px solid {GRAY};padding-bottom:18px;margin-bottom:26px;}}
  .kick{{font-size:15px;font-weight:700;letter-spacing:3px;color:{STEEL};margin-bottom:8px;}}
  .title{{font-size:38px;font-weight:800;color:{NAVY};letter-spacing:-0.5px;}}
  .thesis{{font-size:17px;font-weight:600;font-style:italic;color:{GOLD};
    text-align:right;max-width:520px;line-height:1.35;}}
  .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:26px 26px;}}
  .cell{{background:#fff;border:1px solid {GRAY};border-radius:14px;overflow:hidden;
    box-shadow:0 2px 10px rgba(1,37,100,0.05);}}
  .thumb{{width:100%;aspect-ratio:1/1;overflow:hidden;background:{BG};}}
  .thumb img{{width:100%;height:100%;object-fit:cover;display:block;}}
  .cap{{padding:12px 16px;font-size:16px;font-weight:700;color:{NAVY};
    display:flex;align-items:center;gap:12px;}}
  .num{{background:{NAVY};color:#fff;font-size:13px;font-weight:800;
    border-radius:6px;padding:3px 9px;letter-spacing:1px;}}
  .foot{{grid-column:span 1;display:flex;flex-direction:column;justify-content:center;
    align-items:flex-start;padding:22px 26px;background:{NAVY};border-radius:14px;color:#fff;}}
  .foot .dot{{width:12px;height:12px;border-radius:50%;background:{GOLD};margin-bottom:14px;}}
  .foot .name{{font-size:30px;font-weight:800;letter-spacing:0.5px;}}
  .foot .tag{{font-size:15px;font-weight:600;color:#c7d2e6;margin-top:8px;line-height:1.4;}}
</style></head><body>
<div id="sheet">
  <div class="head">
    <div>
      <div class="kick">SUSTINERI · CONNECTIVE MAP SERIES</div>
      <div class="title">HR Runs Inside a Broken Structure</div>
    </div>
    <div class="thesis">"I do not hate HR people. I hate the structure HR has been forced to operate inside."</div>
  </div>
  <div class="grid">
    {cells}
    <div class="foot">
      <div class="dot"></div>
      <div class="name">Sustineri</div>
      <div class="tag">Workforce architecture, mapped.<br/>Map the structure before you scale it.</div>
    </div>
  </div>
</div></body></html>"""

out = os.path.join(HERE, "contact_sheet.html")
with open(out, "w") as f:
    f.write(html)
print("wrote", out)
