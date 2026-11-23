# Research proposal: verified dark-web tooling knowledge base

**Date:** 2026-11-23  
**Owner:** repository maintainer  
**Status:** phase 0 complete; URL-only repository

## 1. Problem

The original catalog covers 12 tools, has duplicated sections in `tools_catalog.md`, contains no URLs in the root category tables, and has no consistent way to detect tool death, mirror churn, or new projects. Rankings are asserted without linked evidence.

## 2. Objectives

- **O1:** Expand coverage to all practical software/app categories used in legitimate dark-web research: OSINT/recon, attack-surface intelligence, onion assessment, leak-site tracking, onion discovery, and privacy environments.
- **O2:** Make every claim traceable to a primary source or an explicitly labeled secondary cross-check.
- **O3:** Prevent duplicates across legacy and new documentation.
- **O4:** Keep the URL directory browsable by category, type, and source.
- **O5:** Preserve provenance so readers can distinguish verified tools from indexed links.

## 3. Research questions

| ID | Question | Method |
|---|---|---|
| RQ1 | Which open-source and commercial tools are actively maintained in 2026? | GitHub metadata (stars, forks, `pushed_at`, `archived`), official release pages |
| RQ2 | Which onion search engines are still reachable, and how stable are their addresses? | Two independent secondary sources + explicit `address-verify-needed` labels |
| RQ3 | Which tools cover Windows vs Linux, and how? | Official install docs; platform matrix in registry |
| RQ4 | How do leak-site trackers differ in scope and focus? | Official repos, public dashboards, API docs |
| RQ5 | What privacy environment is appropriate for each research task? | Official Tor Project, Tails, Whonix, Qubes documentation |
| RQ6 | How can coverage grow without injecting duplicate or unverifiable entries? | Normalized identity checks + source provenance + manual review |

## 4. Hypothesis

A deduplicated, evidence-linked URL directory with explicit provenance labels is more useful than a static Markdown catalog, and a manual review gate prevents low-quality links from contaminating verified content.

## 5. Methodology

1. **Source tiers:** primary (official site/repo/docs) > cross-check (independent engine) > secondary (vendor blog/community list).
2. **Engine cross-check:** DDG + Yandex were attempted in parallel; both were intermittently empty on 2026-11-23, so Brave and GitHub search were used as independent fallbacks. All source URLs are preserved in `SOURCES.md`.
3. **Identity normalization:** lowercase, strip scheme/`www`/query/fragment/trailing slash, canonicalize GitHub repos to `owner/repo`.
4. **Dedupe gate:** registry internal check + legacy exclusion list.
5. **Verification record:** every primary entry has a `verified` date, `evidence` URLs, `status`, and optional `safety_note`.
6. **Provenance record:** every apps entry records the source index it came from.

## 6. Data model

`registry/tools.json` fields: `id`, `name`, `category`, `type`, `url`, `repo`, `aliases`, `platforms`, `license`, `rank`, `summary`, `capabilities`, `evidence`, `metrics`, `verified`, `status`, `safety_note`.

Ranking scale: 5 = broad + maintained + primary evidence; 4 = strong with limits; 3 = useful niche; 2 = orientation only; 1 = experimental. Rankings are editorial, not vendor scores.

## 7. Review workflow

```text
Public indexes and primary sources
        -> manual dedupe against exclusions.json + catalog.json
        -> primary source checked by a reviewer
        -> entry added to registry/tools.json or apps/data/catalog.json
        -> README/category/type indexes updated
```

There is no executable code in this repository. Updates are manual pull requests containing URLs and Markdown/JSON data only.

## 8. Quality gates

- No tool is added without a verifiable public URL.
- Primary-verified tools require a `verified` date and at least one `https://` evidence URL.
- Duplicate normalized identities are rejected.
- `.onion` addresses are never hard-coded except the official DuckDuckGo onion service; other engines are marked for address verification.
- Only valid public HTTP(S) URLs are accepted.

## 9. Metrics

| Metric | Target | Measured from |
|---|---|---|
| Primary-verified coverage | >= 20 tools, >= 6 categories | `STATUS.json` |
| Apps directory size | >= 5,000 unique URLs | `apps/STATUS.json` |
| Duplicate collisions | 0 | manual dedupe review |
| Evidence coverage | 100% of primary tools have >= 1 primary URL | `registry/tools.json` |
| Verification age | <= 90 days for every `active` entry | `verified` field |

## 10. Roadmap

- **Phase 0 (done, 2026-11-23):** research pack, 20 primary-verified tools, exclusion list, 5,000+ URL directory.
- **Phase 1:** add clearnet URLs for VormWeb/Tor66/Excavator via trusted directories; confirm Haystak address; record tool licenses precisely.
- **Phase 2:** add release/version tracking for CLI tools as data fields.
- **Phase 3:** add a confidence score and reviewer field to each URL entry.
- **Phase 4 (ongoing):** quarterly manual audit of legacy `tools_catalog.md` against `rsearch/registry/` and `apps/data/catalog.json`.

## 11. Ethics and scope

Defensive research and journalism only. No weaponized exploit code, no stolen data, no targeting of individuals, no instructions for unauthorized access. Leak-site metadata is used for exposure awareness, not for retrieving or redistributing leaked content. Onion scanning is limited to services you operate or are explicitly authorized to assess.

## 12. Acceptance criteria

The repository contains only URLs, Markdown indexes, and JSON data; no tool with a duplicate normalized identity appears in `apps/data/catalog.json` or `rsearch/registry/tools.json`; every primary-verified tool has at least one `https://` evidence URL; and the apps directory reports at least 5,000 entries in `apps/STATUS.json`.
