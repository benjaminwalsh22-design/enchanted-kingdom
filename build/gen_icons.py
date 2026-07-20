#!/usr/bin/env python3
"""Resize the rendered emblem into app-icon PNGs + base64 bundle.

Expects `assets/emblem_icon_1024.png` (produced by `render_icons.mjs`).
Writes icon-180/192/512.png and `assets/icons_b64.json`.

Run from the `build/` directory:  python3 gen_icons.py
"""
from PIL import Image
import base64, json, pathlib

HERE = pathlib.Path(__file__).parent
ASSETS = HERE / "assets"
im = Image.open(ASSETS / "emblem_icon_1024.png").convert("RGB")

b64 = {}
for name, sz in {"icon-180.png": 180, "icon-192.png": 192, "icon-512.png": 512}.items():
    im.resize((sz, sz), Image.LANCZOS).save(ASSETS / name)
    b64[name] = base64.b64encode((ASSETS / name).read_bytes()).decode()

json.dump(b64, open(ASSETS / "icons_b64.json", "w"))
print("wrote icon PNGs + assets/icons_b64.json")
