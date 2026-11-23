#!/usr/bin/env python3
"""Continuously discover candidate tools without polluting the verified registry.

Sources: GitHub repository search (token optional) and DuckDuckGo HTML results.
Every candidate is deduplicated against the verified registry, the legacy
exclusion list, and previously seen candidates. Candidates are staged for human
review; they are never auto-promoted into tools.json.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from refresh_catalog import EXCLUSIONS, REGISTRY, ROOT, USER_AGENT, load_json, norm_key, write_json

QUERIES = ROOT / "automation" / "queries.json"
CANDIDATES = ROOT / "candidates"
SEEN = CANDIDATES / "seen.json"
KEYWORDS = (
    "dark web", "onion", "tor ", "osint", "leak site", "ransomware",
    "breach", "threat intelligence", "hidden service", "dehashed",
)


def request_json(url: str, token: str | None) -> dict:
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.load(response)


def request_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.read().decode("utf-8", errors="replace")


def github_candidates(query: str, token: str | None) -> list[dict]:
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(
        {"q": query, "sort": "stars", "order": "desc", "per_page": 10}
    )
    try:
        payload = request_json(url, token)
    except Exception:
        return []
    found = []
    for item in payload.get("items", []):
        description = (item.get("description") or "").strip()
        found.append(
            {
                "url": item.get("html_url"),
                "title": item.get("full_name"),
                "description": description,
                "source": "github-search",
                "query": query,
                "stars": item.get("stargazers_count", 0),
            }
        )
    return found


def ddg_candidates(query: str) -> list[dict]:
    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": query})
    try:
        html = request_text(url)
    except Exception:
        return []
    found = []
    encoded = re.findall(r'uddg=([^&"]+)', html)
    for raw in encoded:
        target = urllib.parse.unquote(raw)
        if target.startswith("http"):
            found.append({"url": target, "title": target, "description": "", "source": "ddg-html", "query": query})
    direct = re.findall(r'href="(https?://[^"]+)"', html)
    for target in direct:
        if "duckduckgo.com" not in target:
            found.append({"url": target, "title": target, "description": "", "source": "ddg-html", "query": query})
    return found


def score(candidate: dict) -> tuple[int, str]:
    text = (candidate.get("description") or "") + " " + (candidate.get("title") or "")
    text = text.lower()
    if any(word in text for word in KEYWORDS):
        if candidate.get("stars", 0) >= 50:
            return 2, "relevant description and >=50 GitHub stars"
        return 1, "relevant description"
    return 0, "keyword match not confirmed in title/description"


def main() -> int:
    registry = load_json(REGISTRY)
    exclusions = load_json(EXCLUSIONS)
    queries = json.loads(QUERIES.read_text(encoding="utf-8"))["queries"]
    seen = load_json(SEEN) if SEEN.exists() else {"keys": []}

    known: set[str] = set()
    for tool in registry["tools"]:
        known.update(k for k in tool_keys(tool) if k)
    for item in exclusions["tools"]:
        known.add(norm_key(item["name"]))
        for alias in item.get("aliases", []):
            known.add(norm_key(alias))
    known.update(seen.get("keys", []))

    token = os.environ.get("GITHUB_TOKEN") or None
    collected: dict[str, dict] = {}
    for query in queries:
        for candidate in github_candidates(query, token) + ddg_candidates(query):
            url = candidate.get("url")
            if not url or not url.startswith("http"):
                continue
            key = norm_key(url)
            if not key or key in known or key in collected:
                continue
            points, reason = score(candidate)
            candidate.update(
                {
                    "key": key,
                    "score": points,
                    "reason": reason,
                    "discovered": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
                }
            )
            collected[key] = candidate

    CANDIDATES.mkdir(parents=True, exist_ok=True)
    if collected:
        date = datetime.now(timezone.utc).date().isoformat()
        write_json(CANDIDATES / f"{date}.json", {"candidates": [collected[k] for k in sorted(collected)]})
        seen["keys"] = sorted(set(seen.get("keys", [])) | set(collected))
        write_json(SEEN, seen)

    qualified = sum(1 for item in collected.values() if item["score"] >= 2)
    print(f"discovery: {len(collected)} new candidate(s), {qualified} qualified for review, {len(known)} known keys skipped")
    print("candidates are staged only; no registry entries were added")
    return 0


if __name__ == "__main__":
    sys.exit(main())
