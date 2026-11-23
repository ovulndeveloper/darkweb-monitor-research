# rsearch — continuous dark-web tool research

This directory is the research layer added on 2026-11-23. It contains **20 new tools** that are not described in the original `README.md`, `tools_catalog.md`, or `categories/` files. Nothing here duplicates those entries; the exclusion list is documented and manually enforced.

This is a URL/documentation section. It does not contain software code.

## What is here

| Path | Purpose |
|---|---|
| `CATALOG.md` | Curated, evidence-linked catalog of new tools |
| `STATUS.json` | Counts, categories, validation state |
| `CHANGELOG.md` | Update log |
| `RESEARCH_PROPOSAL.md` | Research questions, method, metrics, roadmap |
| `SOURCES.md` | Every source URL found during research, with confidence notes |
| `RECONCILIATION.md` | Conflicts with legacy catalog and resolutions |
| `registry/tools.json` | Human-maintained, deduplicated source of truth |
| `registry/exclusions.json` | Legacy tools that must never be re-added here |

## Deduplication policy

1. A tool is identified by normalized name, canonical URL, GitHub `owner/repo`, and aliases.
2. Identity keys are checked against `registry/tools.json` **and** `registry/exclusions.json`.
3. A duplicate identity is rejected during manual review.
4. New entries require a verification date and at least one primary-source URL.

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

The root `README.md` links to every category and URL, including these new tools. The larger URL-only directory is in [`apps/`](../apps/README.md).

## Legal and ethical notice

Research only. No weaponized exploit code, no stolen data, and no instructions for attacking systems you do not own or are not authorized to test. Tools that touch onion services or leak sites carry real operational and legal risk; follow the safety note on each entry and the parent repository notice.
