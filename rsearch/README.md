# rsearch — continuous dark-web tool research

This directory is the research layer added on 2026-11-23. It contains **20 new tools** that are not described in the original `README.md`, `tools_catalog.md`, or `categories/` files. Nothing here duplicates those entries; the exclusion list is enforced by tests and by the refresh job.

## What is here

| Path | Purpose |
|---|---|
| `CATALOG.md` | Generated, evidence-linked catalog of new tools (never edit by hand) |
| `STATUS.json` | Last run metadata, counts, categories, validation state |
| `CHANGELOG.md` | Append-only log of automated catalog regenerations |
| `RESEARCH_PROPOSAL.md` | Proposed research program, questions, metrics, roadmap |
| `SOURCES.md` | Every source URL found during research, with confidence notes |
| `RECONCILIATION.md` | Conflicts with the legacy catalog and how they were handled |
| `registry/tools.json` | Human-maintained, deduplicated source of truth |
| `registry/exclusions.json` | Legacy tools that must never be re-added here |
| `automation/refresh_catalog.py` | Renders the catalog and refreshes GitHub/HTTP metadata |
| `automation/discover_candidates.py` | Continuously stages new candidates from GitHub + DDG |
| `automation/watch.sh` | Optional local infinite loop (Ctrl-C to stop) |
| `candidates/` | Staged, deduplicated candidates awaiting human review |

## Quick start

```sh
# From the repository root — validate and render without network
python3 -m unittest discover -s rsearch/automation -p 'test_*.py' -v
python3 rsearch/automation/refresh_catalog.py --offline

# Live refresh (GITHUB_TOKEN optional but raises rate limits)
GITHUB_TOKEN=... python3 rsearch/automation/refresh_catalog.py
python3 rsearch/automation/discover_candidates.py

# Local never-stop watcher (6-hour interval by default)
INTERVAL=21600 sh rsearch/automation/watch.sh
```

GitHub Actions runs the same validation + refresh + discovery every 6 hours and commits only when outputs actually change.

## Deduplication policy

1. A tool is identified by normalized name, canonical URL, GitHub `owner/repo`, and aliases.
2. Identity keys are checked against `registry/tools.json` **and** `registry/exclusions.json`.
3. Any collision fails the offline test suite and blocks catalog rendering.
4. Discovery results go to `candidates/` only. A human promotes them into `registry/tools.json` with at least one primary-source URL and a verification date.

## Verification levels

- **Primary**: official project site, official repository, or official API/docs.
- **Cross-check**: at least one independent search engine or second source (Brave/DDG/Yandex/GitHub search were used; DDG and Yandex were intermittently unavailable on 2026-11-23, so Brave and GitHub were used as fallbacks).
- **Secondary only**: search-engine status entries (Haystak, Tor66, Excavator, OnionLand, VormWeb, Hidden Wiki) are marked `address-verify-needed` or `verify-independently` because `.onion` mirrors churn.

## Categories covered

1. OSINT & Reconnaissance
2. Attack Surface & Internet Intelligence
3. Onion Service Assessment
4. Leak Site & Ransomware Tracking
5. Onion Search & Discovery
6. Privacy & Research Environment

The root `README.md` now links to every category and URL, including these new tools.

## Legal and ethical notice

Research only. No weaponized exploit code, no stolen data, and no instructions for attacking systems you do not own or are not authorized to test. Tools that touch onion services or leak sites carry real operational and legal risk; follow the safety note on each entry and the parent repository notice.
