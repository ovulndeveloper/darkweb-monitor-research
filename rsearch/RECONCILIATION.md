# Reconciliation with the legacy catalog

This file records where new research disagrees with the original repository content. Legacy files were left intact so nothing is silently overwritten.

| Legacy claim | New evidence | Resolution |
|---|---|---|
| `NotEvil` listed as an active ⭐⭐⭐ search engine | SOCRadar (2026-06-03) says it went offline in 2024; Factually (2026-06-15) cross-checks that it is not reliably operational | Added to `exclusions.json` as legacy; not re-added to `rsearch`. Recommend marking it `inactive` in the legacy files. |
| `Torch` listed ⭐⭐⭐⭐ with broad coverage | SOCRadar notes partial V3 coverage and high dead-link rate after V2 deprecation | Kept in exclusions; documented caveat here. |
| `tools_catalog.md` repeated sections 2 and 3 verbatim and repeated SpiderFoot feature lines | File inspection | Duplicate block and repeated lines removed; canonical legacy catalog remains. |
| `README.md` said `tools_catalog.md - will be created`, but the file exists | File inspection | Fixed in the updated root README. |
| Root category tables had no tool URLs | User request | Updated root README with URL columns for all 11 categories. |
| README linked `commercial_solutions.md`, `breach_monitoring.md`, and `ranking_criteria.md`, but none existed | File inspection | Created all three files with URLs and ranking methodology. |
| `tools_catalog.md` listed ZeroFox as `https://www.zeroxfox.com` | Official site `https://www.zerofox.com` | Typo corrected. |
| `research/automation_scripts.md` contained only TODO placeholders | File inspection | Replaced with links and commands for the real automation pipeline. |
| `dls-monitor` license | GitHub API says MIT; README footer says unlicense | Registry stores both with a "verify" note. |
| OnionScan install instructions reference Go 1.6/1.7 | Official README | Registry status is `active-but-old-toolchain`. |
| Haystak showed as active in secondary sources | Direct fetch of `https://haystak.com/` returned 404 | Registry status is `address-verify-needed`; no onion mirror hard-coded. |
| Existing ranking system lists 5, 4, 2, 3, 1 stars out of order | README inspection | New catalog defines an explicit 5-to-1 scale; legacy text unchanged. |

## Non-duplication guarantee

`rsearch/registry/exclusions.json` contains all 12 legacy tools with aliases. `refresh_catalog.py::validate()` and `test_research.py` both fail if any new tool collides with them. The 20 tools in `rsearch` were selected specifically to fill gaps rather than repeat existing entries.
