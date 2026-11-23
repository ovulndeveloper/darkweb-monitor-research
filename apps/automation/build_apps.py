#!/usr/bin/env python3
"""Build the generated apps/ mega-directory from cached and live public sources.

The verified `rsearch/` registry is never modified here. Every apps/ entry is
provenance-labeled as `primary-verified`, `indexed`, `legacy`, or `archived`.
Keyword blocking is disabled by default: all valid public HTTP(S) links from the
configured sources are indexed; only malformed/non-tool links are skipped.

Usage:
    python3 apps/automation/build_apps.py            # refresh snapshots, then render
    python3 apps/automation/build_apps.py --offline  # render cached snapshots only
    python3 apps/automation/build_apps.py --force    # refetch every snapshot now
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APPS = ROOT / "apps"
DATA = APPS / "data"
SNAPSHOTS = DATA / "snapshots"
SOURCES_FILE = DATA / "sources.json"
CATALOG_FILE = DATA / "catalog.json"
TOOLS = APPS / "tools"
BY_CATEGORY = APPS / "by-category"
BY_TYPE = APPS / "by-type"
RSEARCH_REGISTRY = ROOT / "rsearch" / "registry" / "tools.json"
RSEARCH_EXCLUSIONS = ROOT / "rsearch" / "registry" / "exclusions.json"
USER_AGENT = "darkweb-monitor-research-apps/1.0 (+https://github.com/ovulndeveloper/darkweb-monitor-research)"

CATEGORIES = [
    "OSINT & Reconnaissance",
    "Dark Web Monitoring & Leak Intelligence",
    "Ransomware & Threat Actor Tracking",
    "Onion Search & Discovery",
    "Privacy & Anonymity",
    "Threat Intelligence Platforms",
    "Attack Surface & Exposure",
    "Digital Forensics & Incident Response",
    "Malware Analysis & Detection",
    "Phishing & Fraud Intelligence",
    "Identity & Breach Intelligence",
    "Cryptocurrency & Financial Intelligence",
    "Investigation & Link Analysis",
    "Security Automation & Orchestration",
    "Resource Lists & Directories",
    "Security Tooling & Research",
]

CATEGORY_KEYWORDS: list[tuple[str, tuple[str, ...]]] = [
    ("Ransomware & Threat Actor Tracking", ("ransomware", "ransom", "leak site", "dls", "threat actor", "apt group", "ransomware gang", "double extortion")),
    ("Dark Web Monitoring & Leak Intelligence", ("dark web", "darkweb", "dark-web", "leak intelligence", "data leak", "credential leak", "exposure monitoring", "breach monitoring", "underground forum")),
    ("Onion Search & Discovery", ("onion", "tor network", "hidden service", "onion service", "tor search", "v3 onion")),
    ("Privacy & Anonymity", ("privacy", "anonymous", "anonymity", "opsec", "whonix", "tails os", "tor browser", "vpn", "metadata removal")),
    ("Identity & Breach Intelligence", ("breach", "hibp", "haveibeenpwned", "credential", "password", "identity", "email intelligence", "account takeover")),
    ("Phishing & Fraud Intelligence", ("phishing", "fraud", "scam", "brand protection", "domain abuse", "typosquat", "fake site")),
    ("Cryptocurrency & Financial Intelligence", ("crypto", "bitcoin", "blockchain", "ethereum", "wallet", "ransom payment", "financial intelligence", "transaction tracing")),
    ("Malware Analysis & Detection", ("malware analysis", "malware", "sandbox", "yara", "sigma rule", "detection engineering", "indicator of compromise", "ioc")),
    ("Digital Forensics & Incident Response", ("forensic", "dfir", "incident response", "memory analysis", "artifact", "timeline analysis", "disk image", "log analysis")),
    ("Attack Surface & Exposure", ("attack surface", "exposure", "subdomain", "asset discovery", "port scan", "certificate transparency", "shodan", "censys", "dns recon")),
    ("Threat Intelligence Platforms", ("threat intelligence", "threat-intel", "cti", "misp", "opencti", "siem", "intel feed", "stix", "taxii", "threat hunting")),
    ("Security Automation & Orchestration", ("automation", "soar", "orchestration", "playbook", "workflow", "pipeline", "github actions")),
    ("Investigation & Link Analysis", ("link analysis", "graph analysis", "network graph", "visualization", "maltego", "entity resolution", "relationship graph")),
    ("Resource Lists & Directories", ("awesome", "resource list", "curated", "directory", "cheatsheet", "collection of tools", "list of tools")),
    ("OSINT & Reconnaissance", ("osint", "open-source intelligence", "recon", "reconnaissance", "username", "google dork", "social media intelligence", "people search", "footprinting")),
]

TYPE_KEYWORDS: list[tuple[str, tuple[str, ...]]] = [
    ("awesome-list", ("awesome", "curated list", "resource list", "list of tools")),
    ("directory", ("directory", "index", "link list", "catalogue", "catalog")),
    ("browser-extension", ("browser extension", "chrome extension", "firefox addon", "web extension")),
    ("mobile-app", ("android app", "ios app", "mobile app", "apk")),
    ("desktop-app", ("desktop app", "windows app", "macos app", "electron")),
    ("container", ("docker", "container", "kubernetes", "helm")),
    ("plugin", ("plugin", "extension", "module", "addon", "integration")),
    ("api-service", ("api", "web service", "rest api", "graphql")),
    ("dashboard", ("dashboard", "web ui", "frontend", "gui")),
    ("web-platform", ("platform", "web app", "web application", "web-based", "portal", "service")),
    ("dataset", ("dataset", "data feed", "feed", "database", "corpus")),
    ("library", ("library", "sdk", "python package", "go package", "npm package")),
    ("framework", ("framework", "toolkit", "arsenal")),
    ("cli-tool", ("cli", "command-line", "command line", "terminal", "shell")),
    ("research-project", ("research", "paper", "study", "experiment", "proof of concept")),
]

BAD_LINK_PARTS = (
    "shields.io", "badge.fury.io", "travis-ci", "github.com/topics/",
    "github.com/search?", "opencollective.com", "patreon.com",
    "buymeacoffee.com", "twitter.com", "x.com/", "youtube.com",
    "facebook.com", "linkedin.com", "localhost", "127.0.0.1",
)
IMAGE_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".bmp")

RATE_REMAINING: int | None = None
RATE_RESET = 0


def utc_stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: object) -> bool:
    content = json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    return write_text(path, content)


def write_text(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def norm_key(value: str) -> str:
    """Same identity rule as rsearch/automation/refresh_catalog.py."""
    text = str(value or "").strip().lower()
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


def slugify(value: str, max_len: int = 72) -> str:
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    text = text[:max_len].rstrip("-")
    return text or "entry"


def make_id(key: str, url: str, name: str) -> str:
    if key.startswith("gh:"):
        base = key[3:].replace("/", "-")
    else:
        parsed = urllib.parse.urlparse(url)
        base = (parsed.netloc + parsed.path).strip("/") or name
    return slugify(base, 64) + "-" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:8]


def clean_text(value: object, limit: int = 500) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", str(value or "")))
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip(" -:*\t")
    return text[:limit]


def cell(value: object) -> str:
    return clean_text(value, 240).replace("|", "\\|")


def safe_url(url: str) -> str:
    return str(url or "").strip().rstrip("),.;")


def valid_link(url: str) -> bool:
    url = safe_url(url)
    if not url.startswith(("http://", "https://")):
        return False
    lower = url.lower()
    if any(part in lower for part in BAD_LINK_PARTS):
        return False
    if lower.endswith(IMAGE_EXT):
        return False
    if "github.com/" in lower:
        path = urllib.parse.urlparse(url).path.strip("/").split("/")
        if len(path) < 2 or not path[0] or not path[1]:
            return False
        if path[-1].lower() in {"stargazers", "forks", "issues", "pulls", "releases", "watchers"}:
            return False
    return True


def blocked(text: str, patterns: list[str]) -> bool:
    lowered = text.lower()
    return any(pattern.lower() in lowered for pattern in patterns)


def classify_category(record: dict, hints: dict[str, str]) -> str:
    topics = " ".join(str(t) for t in record.get("topics") or [])
    text = " ".join(
        str(record.get(k) or "")
        for k in ("name", "description", "raw_category")
    ) + " " + topics
    lowered = text.lower()
    best, best_score = None, 0
    for category, keywords in CATEGORY_KEYWORDS:
        score = 0
        for keyword in keywords:
            if keyword in lowered:
                score += 3 if keyword in topics.lower() else 1
        hint = hints.get(record.get("source", "").split(":", 1)[0])
        if hint == category:
            score += 2
        if record.get("category_hint") == category:
            score += 4
        raw = clean_text(record.get("raw_category"), 120).lower()
        if raw and any(word in raw for word in category.lower().replace("&", "and").split()):
            score += 3
        if score > best_score:
            best, best_score = category, score
    return best or "Security Tooling & Research"


def classify_type(record: dict) -> str:
    topics = " ".join(str(t) for t in record.get("topics") or [])
    text = " ".join(str(record.get(k) or "") for k in ("name", "description", "raw_category")) + " " + topics
    lowered = text.lower()
    for type_name, keywords in TYPE_KEYWORDS:
        if any(keyword in lowered for keyword in keywords):
            return type_name
    if record.get("archived"):
        return "research-project"
    return "tool"


def respect_rate_limit() -> None:
    if RATE_REMAINING is not None and RATE_REMAINING <= 1 and RATE_RESET:
        wait = RATE_RESET - time.time() + 2
        if wait > 0:
            print(f"github search rate limit reached; sleeping {int(wait)}s", file=sys.stderr)
            time.sleep(wait)


def fetch_text(url: str, token: str | None = None, retry: bool = True) -> str:
    global RATE_REMAINING, RATE_RESET
    respect_rate_limit()
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT}
    if token and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            remaining = response.headers.get("X-RateLimit-Remaining")
            reset = response.headers.get("X-RateLimit-Reset")
            if remaining is not None:
                RATE_REMAINING = int(remaining)
            if reset is not None:
                RATE_RESET = int(reset)
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        remaining = exc.headers.get("X-RateLimit-Remaining") if exc.headers else None
        reset = exc.headers.get("X-RateLimit-Reset") if exc.headers else None
        if remaining is not None:
            RATE_REMAINING = int(remaining)
        if reset is not None:
            RATE_RESET = int(reset)
        if exc.code in (403, 429) and retry and RATE_RESET:
            wait = RATE_RESET - time.time() + 2
            if 0 < wait < 300:
                time.sleep(wait)
                return fetch_text(url, token, retry=False)
        raise


def snapshot(kind: str, ident: str, url: str, suffix: str, offline: bool, force: bool, ttl_hours: int, token: str | None, warnings: list[str]) -> str | None:
    digest = hashlib.sha1(ident.encode("utf-8")).hexdigest()
    path = SNAPSHOTS / kind / f"{digest}.{suffix}"
    fresh = path.exists() and (time.time() - path.stat().st_mtime) < ttl_hours * 3600
    if path.exists() and (offline or (fresh and not force)):
        return path.read_text(encoding="utf-8")
    if offline:
        warnings.append(f"offline snapshot missing: {kind}/{ident}")
        return None
    try:
        content = fetch_text(url, token)
    except Exception as exc:
        warnings.append(f"fetch failed for {ident}: {exc.__class__.__name__}")
        return path.read_text(encoding="utf-8") if path.exists() else None
    write_text(path, content)
    return content


def record_base(name: str, url: str, description: str = "", source: str = "") -> dict:
    return {
        "name": clean_text(name, 120) or "Untitled",
        "url": safe_url(url),
        "description": clean_text(description),
        "sources": [source] if source else [],
    }


def add_record(records: dict[str, dict], record: dict, blocked_patterns: list[str]) -> None:
    url = safe_url(record.get("url") or "")
    name = clean_text(record.get("name") or "", 120)
    if not url or not name:
        return
    haystack = " ".join(
        str(record.get(k) or "") for k in ("name", "description", "raw_category")
    ) + " " + " ".join(str(t) for t in record.get("topics") or [])
    if blocked(haystack, blocked_patterns):
        return
    key = norm_key(url)
    if not key or key in {"http", "https", "com", "org", "net"}:
        return
    record["url"] = url
    record["name"] = name
    record["key"] = key
    if key not in records:
        records[key] = record
        return
    current = records[key]
    for source in record.get("sources") or []:
        if source not in current["sources"]:
            current["sources"].append(source)
    for field in ("description", "raw_category", "category_hint", "license", "rsearch_id", "rsearch_type"):
        if not current.get(field) and record.get(field):
            current[field] = record[field]
    for field in ("stars", "forks", "rank"):
        if (record.get(field) or 0) > (current.get(field) or 0):
            current[field] = record[field]
    if record.get("topics"):
        current["topics"] = sorted(set(current.get("topics") or []) | set(record["topics"]))
    for flag in ("verified", "legacy", "archived"):
        if record.get(flag):
            current[flag] = True
    if record.get("explicit_category") and not current.get("explicit_category"):
        current["explicit_category"] = record["explicit_category"]
    if record.get("explicit_type") and not current.get("explicit_type"):
        current["explicit_type"] = record["explicit_type"]
    if record.get("evidence"):
        current["evidence"] = sorted(set(current.get("evidence") or []) | set(record["evidence"]))


def map_rsearch_type(value: str) -> str:
    lowered = str(value or "").lower()
    if "directory" in lowered:
        return "directory"
    if "search engine" in lowered:
        return "web-platform"
    if "service" in lowered or "commercial" in lowered:
        return "web-platform"
    if "framework" in lowered:
        return "framework"
    return "tool"


def seed_existing(records: dict[str, dict], blocked_patterns: list[str]) -> None:
    if RSEARCH_REGISTRY.exists():
        registry = load_json(RSEARCH_REGISTRY)
        for tool in registry.get("tools", []):
            url = tool.get("url")
            if not url:
                candidates = [u for u in tool.get("evidence") or [] if str(u).startswith("http")]
                url = candidates[0] if candidates else None
            if not url or not tool.get("repo") and not tool.get("url"):
                # Entries without a canonical address are represented by evidence only.
                pass
            record = record_base(
                tool.get("name") or tool.get("id") or "",
                url or "",
                tool.get("summary") or "",
                "rsearch-registry",
            )
            record.update(
                {
                    "explicit_category": tool.get("category"),
                    "explicit_type": map_rsearch_type(tool.get("type")),
                    "verified": True,
                    "legacy": False,
                    "rsearch_id": tool.get("id"),
                    "rsearch_type": tool.get("type"),
                    "rank": tool.get("rank"),
                    "license": tool.get("license"),
                    "evidence": tool.get("evidence") or [],
                    "archived": bool(tool.get("status", "").startswith("active-but-old")),
                    "metrics": tool.get("metrics") or {},
                }
            )
            add_record(records, record, blocked_patterns)
    if RSEARCH_EXCLUSIONS.exists():
        try:
            exclusions = load_json(RSEARCH_EXCLUSIONS)
        except json.JSONDecodeError:
            exclusions = {"tools": []}
        for item in exclusions.get("tools", []):
            aliases = [a for a in item.get("aliases") or [] if str(a).startswith("http")]
            url = aliases[0] if aliases else None
            if not url:
                continue
            record = record_base(item.get("name") or "", url, "Legacy repository entry cross-referenced for completeness.", "legacy-repo")
            record.update({"legacy": True, "explicit_type": "tool"})
            add_record(records, record, blocked_patterns)


def parse_github(payload_text: str, query: str) -> list[dict]:
    try:
        payload = json.loads(payload_text)
    except json.JSONDecodeError:
        return []
    found = []
    for item in payload.get("items") or []:
        if item.get("fork"):
            continue
        full_name = item.get("full_name") or ""
        url = item.get("html_url") or f"https://github.com/{full_name}"
        if not full_name or not valid_link(url):
            continue
        record = record_base(full_name, url, item.get("description") or "", f"github-search:{query}")
        record.update(
            {
                "topics": item.get("topics") or [],
                "stars": item.get("stargazers_count") or 0,
                "forks": item.get("forks_count") or 0,
                "license": ((item.get("license") or {}).get("spdx_id") or ""),
                "archived": bool(item.get("archived")),
                "pushed_at": item.get("pushed_at"),
                "source_kind": "github",
            }
        )
        found.append(record)
    return found


def parse_awesome(text: str, list_name: str, list_url: str) -> list[dict]:
    found = []
    heading = "Resource list"
    link_re = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", re.IGNORECASE)
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            continue
        for match in link_re.finditer(line):
            before = line[max(0, match.start() - 1):match.start()]
            if before == "!":
                continue
            label = clean_text(match.group(1), 120)
            url = safe_url(match.group(2))
            if not label or not valid_link(url):
                continue
            description = link_re.sub("", line)
            description = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", description)
            record = record_base(label, url, description, f"awesome:{list_name}")
            record.update(
                {
                    "raw_category": heading,
                    "source_url": list_url,
                    "source_kind": "awesome-list",
                }
            )
            found.append(record)
    return found


def collect_records(config: dict, offline: bool, force: bool, token: str | None, warnings: list[str]) -> tuple[dict[str, dict], dict[str, dict]]:
    records: dict[str, dict] = {}
    source_meta: dict[str, dict] = {}
    patterns = config.get("blocked_patterns") or []
    ttl = int(config.get("snapshot_ttl_hours") or 24)
    seed_existing(records, patterns)
    source_meta["rsearch-registry"] = {
        "id": "rsearch-registry",
        "url": "https://github.com/ovulndeveloper/darkweb-monitor-research/tree/main/rsearch/registry/tools.json",
        "kind": "verified registry",
    }
    source_meta["legacy-repo"] = {
        "id": "legacy-repo",
        "url": "https://github.com/ovulndeveloper/darkweb-monitor-research",
        "kind": "legacy repository",
    }

    for spec in config.get("github_queries") or []:
        query = spec["query"]
        source_id = f"github-search:{query}"
        source_meta[source_id] = {
            "id": source_id,
            "url": "https://github.com/search?q=" + urllib.parse.quote(query) + "&type=repositories",
            "kind": "GitHub repository search",
        }
        for page in range(1, int(spec.get("pages") or 1) + 1):
            params = urllib.parse.urlencode(
                {"q": query, "sort": "stars", "order": "desc", "per_page": 100, "page": page}
            )
            url = "https://api.github.com/search/repositories?" + params
            text = snapshot(
                "github", f"{query}:{page}", url, "json",
                offline, force, ttl, token, warnings,
            )
            if not text:
                continue
            for record in parse_github(text, query):
                record["category_hint"] = spec.get("category_hint")
                add_record(records, record, patterns)

    for spec in config.get("awesome_lists") or []:
        name = spec["name"]
        url = spec["url"]
        source_id = f"awesome:{name}"
        source_meta[source_id] = {"id": source_id, "url": url, "kind": "curated awesome list"}
        text = snapshot("list", name, url, "md", offline, force, ttl, None, warnings)
        if not text:
            continue
        for record in parse_awesome(text, name, url):
            record["category_hint"] = spec.get("category_hint")
            add_record(records, record, patterns)

    return records, source_meta


def finalize(records: dict[str, dict], source_meta: dict[str, dict], stamp: str) -> tuple[list[dict], dict[str, dict], dict[str, dict]]:
    hints = {}
    for source_id, meta in source_meta.items():
        hints[source_id] = meta.get("category_hint")
    entries = []
    for key, record in records.items():
        category = record.get("explicit_category") or classify_category(record, hints)
        type_name = record.get("explicit_type") or classify_type(record)
        status = "primary-verified" if record.get("verified") else "legacy" if record.get("legacy") else "indexed"
        if record.get("archived"):
            status = "archived"
        entry = {
            "id": make_id(key, record["url"], record["name"]),
            "key": key,
            "name": record["name"],
            "url": record["url"],
            "description": record.get("description") or "No description provided by the source.",
            "category": category,
            "type": type_name,
            "status": status,
            "sources": sorted(set(record.get("sources") or [])),
            "indexed": stamp[:10],
        }
        for field in ("stars", "forks", "license", "topics", "rank", "pushed_at", "rsearch_id", "rsearch_type", "evidence", "metrics", "raw_category"):
            if record.get(field) not in (None, "", [], {}):
                entry[field] = record[field]
        entries.append(entry)
    entries.sort(key=lambda item: (item["category"].lower(), item["name"].lower(), item["id"]))
    categories = Counter(entry["category"] for entry in entries)
    types = Counter(entry["type"] for entry in entries)
    source_counts = Counter(source for entry in entries for source in entry["sources"])
    for source_id, meta in source_meta.items():
        meta["entry_count"] = source_counts.get(source_id, 0)
    return entries, dict(categories), dict(types)


def render_master(entries: list[dict], categories: dict[str, int], types: dict[str, int], sources: list[dict], stamp: str, min_entries: int) -> str:
    verified = sum(1 for e in entries if e["status"] == "primary-verified")
    legacy = sum(1 for e in entries if e["status"] == "legacy")
    archived = sum(1 for e in entries if e["status"] == "archived")
    lines = [
        "# Apps & Tools Mega Directory",
        "",
        "> Auto-generated by `apps/automation/build_apps.py`. Do not edit by hand.",
        "",
        f"**{len(entries):,} unique entries** across **{len(categories)} categories** and **{len(types)} types**.  ",
        f"Generated {stamp}. Minimum target: {min_entries:,} — " + ("PASS" if len(entries) >= min_entries else "FAIL") + ".  ",
        f"Verification mix: {verified} primary-verified, {legacy} legacy cross-reference, {archived} archived, remainder indexed-from-source.",
        "",
        "## Verification levels",
        "",
        "- **primary-verified**: present in `rsearch/registry/tools.json` with primary-source evidence.",
        "- **indexed**: discovered from a named public source index; provenance is recorded, but each entry has not been individually primary-verified.",
        "- **legacy**: already documented in the original repository, cross-referenced here once for completeness.",
        "- **archived**: source reports the repository as archived; retained for historical research.",
        "",
        "## Category index",
        "",
        "| Category | Entries | Index |",
        "|---|---:|---|",
    ]
    for name in sorted(categories):
        lines.append(f"| {cell(name)} | {categories[name]} | [browse](by-category/{slugify(name)}/README.md) |")
    lines.extend(["", "## Type index", "", "| Type | Entries | Index |", "|---|---:|---|"])
    for name in sorted(types):
        lines.append(f"| {cell(name)} | {types[name]} | [browse](by-type/{slugify(name)}/README.md) |")
    lines.extend(["", "## Sources", "", f"{len(sources)} source definitions are recorded in [`data/sources.json`](data/sources.json) and [`SOURCES.md`](SOURCES.md).", "", "## Full index", ""])
    for category in sorted(categories):
        lines.extend([f"### {category}", "", "| Name | Type | URL | Directory |", "|---|---|---|---|"])
        for entry in entries:
            if entry["category"] != category:
                continue
            lines.append(
                f"| {cell(entry['name'])} | {cell(entry['type'])} | <{entry['url']}> | "
                f"[dir](tools/{slugify(category)}/{entry['id']}/README.md) |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def render_category_index(category: str, entries: list[dict]) -> str:
    cat_slug = slugify(category)
    lines = [
        f"# {category}",
        "",
        f"{len(entries):,} entries. Generated from [`apps/data/catalog.json`](../data/catalog.json); do not edit by hand.",
        "",
        "[← All categories](../CATEGORIES.md) · [Master index](../README.md)",
        "",
        "| Name | Type | Status | URL | Directory |",
        "|---|---|---|---|---|",
    ]
    for entry in entries:
        lines.append(
            f"| {cell(entry['name'])} | {cell(entry['type'])} | {entry['status']} | <{entry['url']}> | "
            f"[dir](../../tools/{cat_slug}/{entry['id']}/README.md) |"
        )
    return "\n".join(lines) + "\n"


def render_type_index(type_name: str, entries: list[dict]) -> str:
    lines = [
        f"# Type: {type_name}",
        "",
        f"{len(entries):,} entries. Generated from [`apps/data/catalog.json`](../data/catalog.json); do not edit by hand.",
        "",
        "[← All types](../TYPES.md) · [Master index](../README.md)",
        "",
        "| Name | Category | Status | URL | Directory |",
        "|---|---|---|---|---|",
    ]
    for entry in entries:
        lines.append(
            f"| {cell(entry['name'])} | {cell(entry['category'])} | {entry['status']} | <{entry['url']}> | "
            f"[dir](../../tools/{slugify(entry['category'])}/{entry['id']}/README.md) |"
        )
    return "\n".join(lines) + "\n"


def render_categories_page(categories: dict[str, int]) -> str:
    lines = [
        "# Categories",
        "",
        "Every generated category, with its current entry count.",
        "",
        "| Category | Entries | Index |",
        "|---|---:|---|",
    ]
    for name in sorted(categories):
        lines.append(f"| {cell(name)} | {categories[name]} | [browse](by-category/{slugify(name)}/README.md) |")
    return "\n".join(lines) + "\n"


def render_types_page(types: dict[str, int]) -> str:
    lines = [
        "# Types",
        "",
        "Every generated entry type, with its current entry count.",
        "",
        "| Type | Entries | Index |",
        "|---|---:|---|",
    ]
    for name in sorted(types):
        lines.append(f"| {cell(name)} | {types[name]} | [browse](by-type/{slugify(name)}/README.md) |")
    return "\n".join(lines) + "\n"


def render_sources_page(sources: list[dict], entries: list[dict], stamp: str) -> str:
    lines = [
        "# Sources for the apps mega-directory",
        "",
        f"Generated {stamp}. Snapshots are cached under `apps/data/snapshots/` and refreshed on the schedule in `apps/data/sources.json`.",
        "",
        "Nothing in this directory replaces the stricter primary-source verification in `rsearch/`. Entries generated from these indexes are marked `indexed`.",
        "",
        "| Source ID | Kind | Entries | URL |",
        "|---|---|---:|---|",
    ]
    for source in sorted(sources, key=lambda s: s["id"]):
        lines.append(
            f"| {cell(source['id'])} | {cell(source.get('kind'))} | {source.get('entry_count', 0)} | <{source.get('url', '')}> |"
        )
    lines.extend(["", "## Link filter", "", "Keyword blocking is disabled. Entries are dropped only when a link is malformed, non-HTTP(S), a badge/image, a social/funding link, or a GitHub profile/search page rather than a repository.", ""])
    return "\n".join(lines)


def render_tools_root(categories: dict[str, int]) -> str:
    lines = [
        "# Tool directories",
        "",
        f"One generated directory per entry, grouped by category. {sum(categories.values()):,} directories total.",
        "",
        "[← Master index](../README.md) · [← Categories](../CATEGORIES.md)",
        "",
        "| Category | Entries | Directory |",
        "|---|---:|---|",
    ]
    for name in sorted(categories):
        lines.append(f"| {cell(name)} | {categories[name]} | [browse]({slugify(name)}/) |")
    return "\n".join(lines) + "\n"


def render_tool_readme(entry: dict) -> str:
    cat_slug = slugify(entry["category"])
    sources = ", ".join(f"`{cell(source)}`" for source in entry["sources"])
    lines = [
        f"# {entry['name']}",
        "",
        f"- **Category:** [{entry['category']}](../../../by-category/{cat_slug}/README.md)",
        f"- **Type:** [{entry['type']}](../../../by-type/{slugify(entry['type'])}/README.md)",
        f"- **Status:** `{entry['status']}`",
        f"- **URL:** <{entry['url']}>",
        f"- **Sources:** {sources}",
        f"- **Indexed:** {entry['indexed']}",
    ]
    if entry.get("stars"):
        lines.append(f"- **GitHub stars at index time:** {entry['stars']}")
    if entry.get("license"):
        lines.append(f"- **License:** {entry['license']}")
    if entry.get("rsearch_id"):
        lines.append(f"- **Verified registry ID:** `{entry['rsearch_id']}`")
    if entry.get("evidence"):
        lines.append("- **Primary evidence:** " + ", ".join(f"<{u}>" for u in entry["evidence"][:5]))
    lines.extend(["", entry["description"], "", f"[← Category index](../../../by-category/{cat_slug}/README.md) · [← Master index](../../../README.md)", ""])
    return "\n".join(lines)


def write_outputs(entries: list[dict], categories: dict[str, int], types: dict[str, int], sources: list[dict], stamp: str, min_entries: int) -> None:
    previous_count = 0
    if CATALOG_FILE.exists():
        try:
            previous_count = len(load_json(CATALOG_FILE).get("entries") or [])
        except (json.JSONDecodeError, OSError):
            previous_count = 0

    write_json(CATALOG_FILE, {
        "schema_version": 1,
        "generated": stamp,
        "min_entries": min_entries,
        "entry_count": len(entries),
        "categories": categories,
        "types": types,
        "entries": entries,
    })
    write_text(APPS / "README.md", render_master(entries, categories, types, sources, stamp, min_entries))
    write_text(APPS / "CATEGORIES.md", render_categories_page(categories))
    write_text(APPS / "TYPES.md", render_types_page(types))
    write_text(APPS / "SOURCES.md", render_sources_page(sources, entries, stamp))
    write_text(TOOLS / "README.md", render_tools_root(categories))
    write_json(APPS / "STATUS.json", {
        "generated": stamp,
        "entry_count": len(entries),
        "category_count": len(categories),
        "type_count": len(types),
        "source_count": len(sources),
        "min_entries": min_entries,
        "requirement_met": len(entries) >= min_entries,
        "categories": categories,
        "types": types,
    })

    expected: set[Path] = set()
    for entry in entries:
        tool_dir = TOOLS / slugify(entry["category"]) / entry["id"]
        expected.add(tool_dir)
        write_text(tool_dir / ".generated", "apps/automation/build_apps.py\n")
        write_text(tool_dir / "README.md", render_tool_readme(entry))

    if TOOLS.exists():
        for cat_dir in TOOLS.iterdir():
            if not cat_dir.is_dir():
                continue
            for tool_dir in cat_dir.iterdir():
                if tool_dir.is_dir() and (tool_dir / ".generated").exists() and tool_dir not in expected:
                    shutil.rmtree(tool_dir)

    for category in sorted(categories):
        subset = [e for e in entries if e["category"] == category]
        write_text(BY_CATEGORY / slugify(category) / "README.md", render_category_index(category, subset))
    for type_name in sorted(types):
        subset = [e for e in entries if e["type"] == type_name]
        write_text(BY_TYPE / slugify(type_name) / "README.md", render_type_index(type_name, subset))

    if previous_count != len(entries):
        with (APPS / "CHANGELOG.md").open("a", encoding="utf-8") as handle:
            handle.write(f"- {stamp}: apps directory rebuilt with {len(entries):,} entries (was {previous_count:,}).\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Render cached snapshots only; no network")
    parser.add_argument("--force", action="store_true", help="Refetch snapshots even when fresh")
    parser.add_argument("--min-entries", type=int, help="Override the minimum entry count for this run")
    args = parser.parse_args()

    config = load_json(SOURCES_FILE)
    if args.min_entries is not None:
        config["min_entries"] = args.min_entries
    token = os.environ.get("GITHUB_TOKEN") or None
    warnings: list[str] = []
    records, source_meta = collect_records(config, args.offline, args.force, token, warnings)
    stamp = utc_stamp()
    entries, categories, types = finalize(records, source_meta, stamp)
    sources = [source_meta[key] for key in sorted(source_meta)]
    write_outputs(entries, categories, types, sources, stamp, int(config.get("min_entries") or 5000))

    print(f"apps build: {len(entries):,} entries, {len(categories)} categories, {len(types)} types, {len(sources)} sources")
    for warning in warnings[:20]:
        print("  warning: " + warning, file=sys.stderr)
    if len(warnings) > 20:
        print(f"  ... {len(warnings) - 20} more warnings", file=sys.stderr)
    if len(entries) < int(config.get("min_entries") or 5000):
        print(f"ERROR: only {len(entries)} entries; target is {config.get('min_entries')}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
