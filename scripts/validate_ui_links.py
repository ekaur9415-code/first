#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "ui"

missing = []
for html in ROOT.rglob("*.html"):
    text = html.read_text(encoding="utf-8")
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith(("http", "#", "mailto:")):
            continue
        target = (html.parent / href).resolve()
        if not target.exists():
            missing.append((html.relative_to(ROOT.parent), href))

if missing:
    print("Broken internal links found:")
    for file_path, href in missing:
        print(f"- {file_path}: {href}")
    sys.exit(1)

print("All internal UI links are valid.")
