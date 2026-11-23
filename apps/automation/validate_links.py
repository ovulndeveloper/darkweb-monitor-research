#!/usr/bin/env python3
"""Check local Markdown links in the repository. Stdlib only, no network."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def main() -> int:
    broken: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK.finditer(text):
            target = match.group(1).split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "//", "data:")):
                continue
            decoded = target.replace("%20", " ")
            resolved = (path.parent / decoded).resolve()
            if not resolved.exists():
                broken.append(f"{path.relative_to(ROOT)}: {target}")
    if broken:
        print(f"Broken local Markdown links: {len(broken)}", file=sys.stderr)
        for item in broken[:100]:
            print("  - " + item, file=sys.stderr)
        return 1
    print("Local Markdown links: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
