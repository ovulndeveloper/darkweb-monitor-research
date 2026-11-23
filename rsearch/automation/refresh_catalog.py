#!/usr/bin/env python3
"""Refresh the rsearch catalog from the deduplicated registry.

Stdlib-only, deterministic, and safe to run offline:

    python3 rsearch/automation/refresh_catalog.py            # live refresh
    python3 rsearch/automation/refresh_catalog.py --offline  # render cached data only

Network failures are warnings, not errors: previously verified metadata is kept.
The script never adds tools by itself. New tools enter through review first.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "tools.json"
EXCLUSIONS = ROOT / "registry" / "exclusions.json"
CATALOG = ROOT / "CATALOG.md"
STATUS = ROOT / "STATUS.json"
CHANGELOG = ROOT / "CHANGELOG.md"
USER_AGENT = "darkweb-monitor-research/1.0 (+https://github.com/ovulndeveloper/darkweb-monitor-research)"


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso_now() -> str:
    return utc_now().isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def norm_key(value: str) -> str:
    """Canonical identity key for deduplication."""
    text = str(value).strip().lower()
    text = re.sub(r"^https?://", "", text)
    text = text.split("?", 1)[0].split("#", 1)[0].rstrip("/")
    text = re.sub(r"^www\.", "", text)
    if "github.com/" in text:
        parts = text.split("github.com/", 1)[1].split("/")
        if len(parts) >= 2:
            owner = re.sub(r"[^a-z0-9-]", "-", parts[0]).strip("-")
            repo = re.sub(r"\.git$", "", parts[1])
            repo = re.sub(r"[^a-z0-9-]", "-", repo).strip("-")
            return "gh:" + owner + "/" + repo
    return re.sub(r"[^a-z0-9./-]", "", text.replace("_", "-"))


def tool_keys(tool: dict) -> set[str]:
    values = [tool.get("name", ""), tool.get("url") or ""]
    if tool.get("repo"):
        values.append("https://github.com/" + tool["repo"])
    values.extend(tool.get("aliases") or [])
    return {norm_key(v) for v in values if str(v).strip()}


def validate(registry: dict, exclusions: dict) -> list[str]:
    """Return deduplication/quality errors; empty list means clean."""
    errors: list[str] = []
    seen: dict[str, str] = {}
    excluded: set[str] = set()
    for item in exclusions.get("tools", []):
        excluded.add(norm_key(item["name"]))
        for alias in item.get("aliases", []):
            excluded.add(norm_key(alias))

    for tool in registry.get("tools", []):
        tid = tool.get("id")
        if not tid:
            errors.append("Tool without id: " + str(tool.get("name")))
            continue
        required = {"name", "category", "type", "summary", "evidence", "verified"}
        missing = sorted(required - set(tool))
        if missing:
            errors.append(f"{tid}: missing required fields {missing}")
        if not tool.get("evidence"):
            errors.append(f"{tid}: no evidence URL")
        for key in tool_keys(tool):
            if key in seen and seen[key] != tid:
                errors.append(f"{tid}: duplicate identity '{key}' shared with {seen[key]}")
            seen[key] = tid
            if key in excluded:
                errors.append(f"{tid}: duplicates an excluded legacy tool via '{key}'")
    return errors


def fetch_github(repo: str, token: str | None) -> dict:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=12) as response:
        data = json.load(response)
    return {
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "pushed_at": data.get("pushed_at"),
        "archived": bool(data.get("archived")),
        "license": (data.get("license") or {}).get("spdx_id"),
    }


def check_url(url: str) -> int | None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=8) as response:
            return response.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return None


def refresh(offline: bool) -> tuple[dict, list[str]]:
    registry = load_json(REGISTRY)
    exclusions = load_json(EXCLUSIONS)
    errors = validate(registry, exclusions)
    if errors:
        raise SystemExit("Registry validation failed:\n- " + "\n- ".join(errors))

    token = os.environ.get("GITHUB_TOKEN") or None
    warnings: list[str] = []
    changed: list[str] = []

    for tool in registry["tools"]:
        if offline:
            continue
        if tool.get("repo"):
            try:
                fresh = fetch_github(tool["repo"], token)
            except Exception as exc:
                warnings.append(f"{tool['id']}: GitHub refresh failed ({exc.__class__.__name__})")
            else:
                current = tool.get("github") or {}
                if current != fresh:
                    tool["github"] = fresh
                    changed.append(tool["id"])
        if tool.get("url"):
            status = check_url(tool["url"])
            if status != tool.get("http_status"):
                tool["http_status"] = status
                changed.append(tool["id"])
            if status is not None and status >= 400:
                warnings.append(f"{tool['id']}: {tool['url']} returned HTTP {status}")

    write_json(REGISTRY, registry)
    return registry, warnings + [f"changed: {', '.join(sorted(set(changed)))}" if changed else "no metric changes"]


def render_catalog(registry: dict, stamp: str) -> str:
    tools = sorted(
        registry["tools"],
        key=lambda t: (t["category"].lower(), t["name"].lower()),
    )
    categories: dict[str, list[dict]] = {}
    for tool in tools:
        categories.setdefault(tool["category"], []).append(tool)

    lines = [
        "# rsearch Tool Catalog",
        "",
        f"Generated by `rsearch/automation/refresh_catalog.py` on {stamp} from `rsearch/registry/tools.json`.",
        f"{len(tools)} new tools across {len(categories)} categories. Edit the registry, never this file.",
        "",
        "Existing catalog tools are excluded via `rsearch/registry/exclusions.json`.",
        "",
        "## Summary",
        "",
        "| Category | Tools |",
        "|---|---:|",
    ]
    for name in sorted(categories):
        lines.append(f"| {name} | {len(categories[name])} |")
    lines.extend(["", "## Index", "", "| Tool | Category | Type | Rank | Verified | Status |", "|---|---|---|---:|---|---|"])
    for tool in tools:
        link = f"[{tool['name']}](#{re.sub(r'[^a-z0-9-]', '', tool['id'].lower())})"
        lines.append(
            f"| {link} | {tool['category']} | {tool['type']} | {tool.get('rank', '-')} | "
            f"{tool['verified']} | {tool.get('status', 'active')} |"
        )

    for name in sorted(categories):
        lines.extend(["", f"## {name}", ""])
        for tool in categories[name]:
            anchor = re.sub(r"[^a-z0-9-]", "", tool["id"].lower())
            lines.extend([f"<a id=\"{anchor}\"></a>", "", f"### {tool['name']}", ""])
            lines.append(f"- **Type:** {tool['type']}  ")
            lines.append(f"- **Rank:** {tool.get('rank', '-')}  ")
            lines.append(f"- **Status:** {tool.get('status', 'active')}  ")
            lines.append(f"- **Verified:** {tool['verified']}  ")
            platforms = tool.get("platforms") or {}
            platform_text = ", ".join(f"{k}={v}" for k, v in sorted(platforms.items()))
            lines.append(f"- **Platforms:** {platform_text or 'see source'}  ")
            lines.append(f"- **License:** {tool.get('license', 'unspecified')}  ")
            if tool.get("url"):
                lines.append(f"- **Primary URL:** <{tool['url']}>  ")
            if tool.get("repo"):
                lines.append(f"- **Repository:** https://github.com/{tool['repo']}  ")
            lines.extend(["", tool["summary"], ""])
            capabilities = tool.get("capabilities") or []
            if capabilities:
                lines.append("**Capabilities**")
                lines.append("")
                for item in capabilities:
                    lines.append(f"- {item}")
                lines.append("")
            evidence = tool.get("evidence") or []
            if evidence:
                lines.append("**Evidence:** " + ", ".join(f"<{u}>" for u in evidence))
                lines.append("")
            metrics = tool.get("metrics") or {}
            if metrics:
                metric_text = ", ".join(f"{k}={v}" for k, v in sorted(metrics.items()))
                lines.append(f"**Metrics (as verified):** {metric_text}")
                lines.append("")
            if tool.get("safety_note"):
                lines.append(f"> Safety/verification note: {tool['safety_note']}")
                lines.append("")

    lines.extend(
        [
            "## Ranking scale",
            "",
            "5 = broad, well-maintained, strong primary-source evidence; 4 = strong with limits; 3 = useful niche tool; 2 = orientation/directory only; 1 = experimental.",
            "",
            "Rankings are editorial and evidence-linked, not vendor scores.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Do not use the network; render cached metadata only")
    args = parser.parse_args()

    registry, notes = refresh(args.offline)
    now = utc_now()
    stamp = now.isoformat().replace("+00:00", "Z")
    catalog = render_catalog(registry, stamp)

    previous = CATALOG.read_text(encoding="utf-8") if CATALOG.exists() else ""
    changed = catalog != previous
    if changed:
        CATALOG.write_text(catalog, encoding="utf-8")
        with CHANGELOG.open("a", encoding="utf-8") as handle:
            handle.write(f"- {stamp}: catalog regenerated ({len(registry['tools'])} tools).\n")

    categories = sorted({tool["category"] for tool in registry["tools"]})
    write_json(
        STATUS,
        {
            "last_run": stamp,
            "last_run_date": now.date().isoformat(),
            "mode": "offline" if args.offline else "live",
            "tool_count": len(registry["tools"]),
            "category_count": len(categories),
            "categories": categories,
            "registry_validation": "pass",
            "notes": notes,
        },
    )

    print(f"rsearch refresh: {len(registry['tools'])} tools, {len(categories)} categories")
    for note in notes:
        print("  - " + note)
    print("  - catalog " + ("updated" if changed else "unchanged"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
