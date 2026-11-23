# Dark Web Tools Research

This directory indexes the research documents in this URL-only repository. It contains no software code.

## Research sections

- [Apps mega-directory (5,000+ URLs)](../apps/README.md) — generated-by-hand directory tree with one folder per tool
- [Legacy OSINT frameworks](../categories/osint_tools.md) — comprehensive OSINT tools
- [Legacy exposure monitoring](../categories/monitoring_tools.md) — ransomware leak-site and breach monitoring
- [Legacy search engines](../categories/search_engines.md) — dark-web search engines and directories
- [Legacy commercial solutions](../commercial_solutions.md) — enterprise monitoring services
- [Legacy breach monitoring](../breach_monitoring.md) — compromised data and credential monitoring
- [New `rsearch/` pack](../rsearch/README.md) — 20 deduplicated, evidence-linked tools across 6 additional categories

## Update policy

- New URLs are added by pull request after a primary-source check.
- Identity is normalized so the same tool is not listed twice.
- Primary-verified entries live in [`rsearch/registry/tools.json`](../rsearch/registry/tools.json).
- Conflicts with the legacy catalog are recorded in [`rsearch/RECONCILIATION.md`](../rsearch/RECONCILIATION.md).

## Contributing research

1. Submit new tool URLs via Pull Request.
2. Check [`rsearch/registry/exclusions.json`](../rsearch/registry/exclusions.json) and [`apps/data/catalog.json`](../apps/data/catalog.json) before adding anything.
3. Include a primary-source URL, verification date, type, and safety note where relevant.
4. Update all affected README indexes so links stay consistent.

## Research notes

- All tools are evaluated on features, platform support, community adoption, update frequency, and documentation quality.
- Ranking scale: ⭐⭐⭐⭐⭐ (excellent) to ⭐ (experimental). See [`ranking_criteria.md`](../ranking_criteria.md).
- Legal and ethical notice applies to all research activities.

*Last verified: 2026-11-23 (UTC)*
