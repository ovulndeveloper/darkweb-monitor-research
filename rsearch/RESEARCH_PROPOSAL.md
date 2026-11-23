# Research proposal: continuously verified dark-web tooling knowledge base

**Date:** 2026-11-23
**Owner:** repository maintainer
**Status:** proposed, phase 0 implemented in `rsearch/`

## 1. Problem

The original catalog covers 12 tools, has duplicated sections in `tools_catalog.md`, contains no URLs in the root category tables, and has no mechanism to detect tool death, mirror churn, or new projects. Rankings are asserted without linked evidence.

## 2. Objectives

- **O1:** Expand coverage to all practical software/app categories used in legitimate dark-web research: OSINT/recon, attack-surface intelligence, onion assessment, leak-site tracking, onion discovery, and privacy environments.
- **O2:** Make every claim traceable to a primary source or an explicitly labeled secondary cross-check.
- **O3:** Prevent duplicates across legacy and new documentation.
- **O4:** Keep the knowledge base continuously updated with minimal manual work.
- **O5:** Produce a reusable, testable, standards-based automation pipeline that other research repos can copy.

## 3. Research questions

| ID | Question | Method |
|---|---|---|
| RQ1 | Which open-source and commercial tools are actively maintained in 2026? | GitHub API metadata (stars, forks, `pushed_at`, `archived`), official release pages |
| RQ2 | Which onion search engines are still reachable, and how stable are their addresses? | Two independent secondary sources + explicit `address-verify-needed` labels |
| RQ3 | Which tools cover Windows vs Linux, and how? | Official install docs; platform matrix in registry |
| RQ4 | How do leak-site trackers differ in scope and automation? | Official repos, public dashboards, API docs |
| RQ5 | What privacy environment is appropriate for each research task? | Official Tor Project, Tails, Whonix, Qubes documentation |
| RQ6 | How can coverage be updated continuously without injecting unverified junk? | Staged discovery + dedupe + tests + human promotion gate |

## 4. Hypothesis

A deduplicated registry with evidence-linked entries, refreshed on a schedule, will stay materially fresher than a static Markdown catalog, while a staging queue prevents low-quality automated additions from contaminating verified content.

## 5. Methodology

1. **Source tiers:** primary (official site/repo/docs) > cross-check (independent engine) > secondary (vendor blog/community list).
2. **Engine cross-check:** DDG + Yandex were attempted in parallel; both were intermittently empty on 2026-11-23, so Brave (`private`) and GitHub search were used as independent fallbacks. All source URLs are preserved in `SOURCES.md`.
3. **Identity normalization:** lowercase, strip scheme/`www`/query/fragment/trailing slash, canonicalize GitHub repos to `owner/repo`.
4. **Dedupe gate:** registry internal check + legacy exclusion list; failure blocks rendering.
5. **Verification record:** every entry has `verified` date, `evidence` URLs, `status`, and optional `safety_note`.
6. **Automation:** render deterministically; refresh GitHub metrics and HTTP status; stage new candidates; commit only on real changes.

## 6. Data model

`registry/tools.json` fields: `id`, `name`, `category`, `type`, `url`, `repo`, `aliases`, `platforms`, `license`, `rank`, `summary`, `capabilities`, `evidence`, `metrics`, `verified`, `status`, `safety_note`.

Ranking scale: 5 = broad + maintained + primary evidence; 4 = strong with limits; 3 = useful niche; 2 = orientation only; 1 = experimental. Rankings are editorial, not vendor scores.

## 7. Automation architecture

```
GitHub API + DDG HTML  ->  discover_candidates.py  ->  candidates/YYYY-MM-DD.json
                                  |                     (never auto-promoted)
                                  v
registry/tools.json + exclusions.json -> validate() -> refresh_catalog.py
                                  |                     -> CATALOG.md
                                  |                     -> STATUS.json
                                  |                     -> CHANGELOG.md
                                  v
GitHub Actions (cron 17 */6 * * *) -> tests -> refresh -> discover -> conditional commit
```

Local equivalent: `sh rsearch/automation/watch.sh` (runs forever until interrupted).

## 8. Quality gates

- Offline `unittest` suite: normalization, dedupe, exclusion enforcement, evidence presence, catalog completeness.
- No network in tests.
- Live refresh failures degrade to cached metadata with warnings.
- No tool is added without a `verified` date and at least one `https://` evidence URL.
- `.onion` addresses are never hard-coded except the official DuckDuckGo onion service; other engines are marked for address verification.

## 9. Metrics

| Metric | Target | Measured from |
|---|---|---|
| New tool coverage | >= 20 tools, >= 6 categories | `STATUS.json` |
| Duplicate collisions | 0 | `validate()` output |
| Evidence coverage | 100% of tools have >= 1 primary URL | unit test |
| Freshness | <= 6 hours between scheduled refreshes | workflow cron |
| Verification age | <= 90 days for every `active` entry | `verified` field |
| Candidate review latency | <= 7 days for score >= 2 candidates | `candidates/` dates |

## 10. Roadmap

- **Phase 0 (done, 2026-11-23):** research pack, 20 tools, registry, exclusion list, offline tests, 6-hour workflow.
- **Phase 1 (next 2 weeks):** add missing clearnet URLs for VormWeb/Tor66/Excavator via trusted directories; confirm Haystak address; record tool licenses precisely.
- **Phase 2 (month 1):** add release/version tracking for CLI tools (theHarvester, Recon-ng, OnionScan, dls-monitor, ransomware.live) via GitHub releases API.
- **Phase 3 (month 2):** add a confidence score and reviewer field; enable PR-based promotion for score-2 candidates.
- **Phase 4 (ongoing):** quarterly manual audit of legacy `tools_catalog.md` against `rsearch/registry/`; merge final canonical catalog into root README.

## 11. Ethics and scope

Defensive research and journalism only. No weaponized exploit code, no stolen data, no targeting of individuals, no instructions for unauthorized access. Leak-site metadata is used for exposure awareness, not for retrieving or redistributing leaked content. Onion scanning is limited to services you operate or are explicitly authorized to assess.

## 12. Acceptance criteria

`python3 -m unittest discover -s rsearch/automation -p 'test_*.py'` passes offline; `refresh_catalog.py --offline` regenerates `CATALOG.md` without network; the workflow commits nothing when outputs are unchanged; and no entry in `rsearch/` appears in `registry/exclusions.json`.
