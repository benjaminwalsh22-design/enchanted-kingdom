#!/usr/bin/env python3
"""Build the single-file app.

Reads `index_template.html` + `assets/icons_b64.json`, inlines the icons and a
web-app manifest as data-URIs, and writes the self-contained `../index.html`.

Run from the `build/` directory:  python3 build.py
"""
import json, base64, pathlib

HERE = pathlib.Path(__file__).parent
b64 = json.load(open(HERE / "assets" / "icons_b64.json"))

manifest = {
    "name": "Enchanted Kingdom",
    "short_name": "Enchanted Kingdom",
    "description": "A magical learning kingdom for ages 4–6 — princesses, unicorns & mermaids.",
    "display": "standalone",
    "orientation": "any",
    "background_color": "#e7d5ff",
    "theme_color": "#c6a7ff",
    "start_url": "./",
    "scope": "./",
    "icons": [
        {"src": "data:image/png;base64," + b64["icon-192.png"], "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "data:image/png;base64," + b64["icon-512.png"], "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
    ],
}
man_b64 = base64.b64encode(json.dumps(manifest).encode()).decode()

html = (HERE / "index_template.html").read_text()
html = (html
        .replace("__ICON180__", b64["icon-180.png"])
        .replace("__ICON192__", b64["icon-192.png"])
        .replace("__MANIFEST__", man_b64))

assert "__ICON" not in html and "__MANIFEST__" not in html, "unfilled token remains"
out = HERE.parent / "index.html"
out.write_text(html)
print(f"built {out} ({round(len(html)/1024,1)} KB)")
