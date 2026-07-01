from playwright.sync_api import sync_playwright
import pathlib
svg = pathlib.Path("connective_map.svg").read_text()
W, H, SCALE = 1240, 1900, 2
html = f'<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0;padding:0}}</style></head><body>{svg}</body></html>'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=SCALE)
    pg.set_content(html, wait_until="networkidle")
    el = pg.query_selector("svg")
    el.screenshot(path="connective_map.png")
    b.close()
print("rendered png")
