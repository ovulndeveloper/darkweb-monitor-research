# Dark Web Tools Research

This directory contains ongoing research into dark-web monitoring tools, search engines, monitoring platforms, and automation.

## Research sections

- [Legacy OSINT frameworks](../categories/osint_tools.md) — comprehensive OSINT automation tools
- [Legacy exposure monitoring](../categories/monitoring_tools.md) — ransomware leak-site and breach monitoring
- [Legacy search engines](../categories/search_engines.md) — dark-web search engines and directories
- [Legacy commercial solutions](../commercial_solutions.md) — enterprise monitoring services
- [Legacy breach monitoring](../breach_monitoring.md) — compromised data and credential monitoring
- [New `rsearch/` pack](../rsearch/README.md) — 20 deduplicated, evidence-linked tools across 6 additional categories
- [Automation scripts](automation_scripts.md) — live refresh/discovery commands

## Update frequency

- Hosted workflow checks for changes every 6 hours: [`research-auto-update.yml`](../.github/workflows/research-auto-update.yml)
- Tool entries are verified against primary sources before promotion into [`rsearch/registry/tools.json`](../rsearch/registry/tools.json)
- Legacy rankings are reviewed manually and conflicts are recorded in [`rsearch/RECONCILIATION.md`](../rsearch/RECONCILIATION.md)

## Contributing research

1. Submit new tool discoveries via Pull Request.
2. Check [`rsearch/registry/exclusions.json`](../rsearch/registry/exclusions.json) before adding anything.
3. Include a primary-source URL, verification date, platform info, and safety note.
4. Run the offline tests before committing generated catalog changes.

## Research notes

- All tools are evaluated on features, platform support, community adoption, update frequency, and documentation quality.
- Ranking scale: ⭐⭐⭐⭐⭐ (excellent) to ⭐ (experimental). See [`ranking_criteria.md`](../ranking_criteria.md).
- Legal and ethical notice applies to all research activities.

*Last verified: 2026-11-23 (UTC)*
