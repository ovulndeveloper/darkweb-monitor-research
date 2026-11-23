# Dark Web Monitor Research Repo

[![Continuous research refresh](https://github.com/ovulndeveloper/darkweb-monitor-research/actions/workflows/research-auto-update.yml/badge.svg)](https://github.com/ovulndeveloper/darkweb-monitor-research/actions/workflows/research-auto-update.yml)

Evidence-linked, deduplicated research on dark-web monitoring, OSINT, onion discovery, leak-site tracking, and privacy environments.

**Last verified:** 2026-11-23 (UTC)  
**Canonical research section:** [`rsearch/`](rsearch/README.md)  
**Generated catalog:** [`rsearch/CATALOG.md`](rsearch/CATALOG.md)

---

## Contents

- [At a glance](#at-a-glance)
- [Legacy categories and URLs](#legacy-categories-and-urls)
- [New `rsearch` categories and URLs](#new-rsearch-categories-and-urls)
- [Research documents and source URLs](#research-documents-and-source-urls)
- [Repository structure](#repository-structure)
- [Automatic updates](#automatic-updates)
- [Ranking system](#ranking-system)
- [Platform support](#platform-support)
- [Deduplication policy](#deduplication-policy)
- [Contributing](#contributing)
- [Legal and ethical notice](#legal-and-ethical-notice)

---

## At a glance

| Area | Legacy repo | New `rsearch/` | Total unique |
|---|---:|---:|---:|
| Tools | 12 | 20 | 32 |
| Categories | 5 | 6 | 11 |
| Generated catalog | `tools_catalog.md` | `rsearch/CATALOG.md` | both |
| Update method | manual PRs | 6-hour GitHub Actions + local watcher | continuous |
| Dedupe enforcement | none | tests + exclusion registry | enforced |

Legacy tool counts treat cross-listed tools (`TorBot`, `HaveIBeenPwned Integration`, `Intelligence X`) as one unique tool each.

---

## Legacy categories and URLs

These tools were already present in the repository and are deliberately **not repeated** in `rsearch/`. Their URLs are listed here so every legacy category has a working link.

### 1. OSINT Automation & Frameworks

Documentation: [`categories/osint_tools.md`](categories/osint_tools.md)

| Tool | Rank | Primary focus | Windows | Linux | URL |
|---|---|---|---|---|---|
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | ⭐⭐⭐⭐⭐ | General OSINT, threat intelligence | ✅ | ✅ | https://github.com/smicallef/spiderfoot |
| [Darkdump](https://github.com/josh0xA/darkdump) | ⭐⭐⭐⭐ | Deep web scraping, search aggregation | ❌ | ✅ | https://github.com/josh0xA/darkdump |
| [TorBot](https://github.com/A-deker0/TorBot) | ⭐⭐⭐ | Onion service crawling | ❌ | ✅ | https://github.com/A-deker0/TorBot |

### 2. Dark Web Exposure & Monitoring

Documentation: [`categories/monitoring_tools.md`](categories/monitoring_tools.md)

| Tool | Rank | Primary focus | Windows | Linux | URL |
|---|---|---|---|---|---|
| [Darkwatch](https://github.com/Daemon-VI/darkwatch) | ⭐⭐⭐⭐ | Ransomware leak sites, breach exposure | ✅ | ✅ | https://github.com/Daemon-VI/darkwatch |
| TorBot *(cross-listed above)* | ⭐⭐⭐ | Onion crawling for monitoring | ❌ | ✅ | https://github.com/A-deker0/TorBot |

### 3. Search Engines & Directories

Documentation: [`categories/search_engines.md`](categories/search_engines.md)

| Tool | Rank | Primary focus | Windows | Linux | URL / address |
|---|---|---|---|---|---|
| [Ahmia](https://ahmia.fi) | ⭐⭐⭐⭐⭐ | Filtered onion search | ✅ via Tor | ✅ via Tor | https://ahmia.fi |
| Torch | ⭐⭐⭐⭐ | General onion search | ✅ via Tor | ✅ via Tor | `http://xmh57jrzrnw6iuq7.onion` |
| NotEvil *(status disputed)* | ⭐⭐⭐ | Privacy-focused search | ✅ via Tor | ✅ via Tor | `http://noteilv6w5w.onion` |
| [HaveIBeenPwned](https://haveibeenpwned.com) | ⭐⭐⭐⭐⭐ | Breach data | ✅ | ✅ | https://haveibeenpwned.com |
| [Intelligence X](https://intelx.io) | ⭐⭐⭐⭐ | Historical/breach data search | ✅ | ✅ | https://intelx.io |

> `NotEvil` is retained here for historical accuracy. New research reports it offline or unreliable; see [`rsearch/RECONCILIATION.md`](rsearch/RECONCILIATION.md).

### 4. Breach & Credential Monitoring

Documentation: [`breach_monitoring.md`](breach_monitoring.md)

| Tool | Rank | Primary focus | Windows | Linux | URL |
|---|---|---|---|---|---|
| [HaveIBeenPwned](https://haveibeenpwned.com) | ⭐⭐⭐⭐⭐ | Breach checking, domain monitoring | ✅ | ✅ | https://haveibeenpwned.com |
| [Intelligence X](https://intelx.io) | ⭐⭐⭐⭐ | Breached documents, historical data | ✅ | ✅ | https://intelx.io |

### 5. Commercial / Enterprise Solutions

Documentation: [`commercial_solutions.md`](commercial_solutions.md)

| Tool | Rank | Primary focus | Windows | Linux | URL |
|---|---|---|---|---|---|
| [ZeroFox](https://www.zerofox.com) | ⭐⭐⭐⭐⭐ | Enterprise digital-risk monitoring | ✅ | ✅ | https://www.zerofox.com |
| [Recorded Future](https://www.recordedfuture.com) | ⭐⭐⭐⭐⭐ | Threat intelligence platform | ✅ | ✅ | https://www.recordedfuture.com |
| [Flashpoint](https://flashpointintel.com) | ⭐⭐⭐⭐ | Cybercrime intelligence | ✅ | ✅ | https://flashpointintel.com |

The full legacy detail view is [`tools_catalog.md`](tools_catalog.md).

---

## New `rsearch` categories and URLs

`rsearch/` adds 20 tools across 6 categories. Every entry is in [`rsearch/registry/tools.json`](rsearch/registry/tools.json) and rendered into [`rsearch/CATALOG.md`](rsearch/CATALOG.md).

### 1. OSINT & Reconnaissance

| Tool | Type | Rank | URL |
|---|---|---:|---|
| [theHarvester](https://github.com/laramies/theHarvester) | open-source | 5 | https://github.com/laramies/theHarvester |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | open-source | 4 | https://github.com/lanmaster53/recon-ng |
| [Maltego](https://www.maltego.com/) | commercial/freemium | 5 | https://www.maltego.com/ |
| [OSINT Framework](https://osintframework.com/) | directory | 4 | https://osintframework.com/ |

### 2. Attack Surface & Internet Intelligence

| Tool | Type | Rank | URL |
|---|---|---:|---|
| [Shodan](https://www.shodan.io/) | commercial/freemium | 5 | https://www.shodan.io/ |
| [Censys](https://censys.io/) | commercial/freemium | 5 | https://censys.io/ |

### 3. Onion Service Assessment

| Tool | Type | Rank | URL |
|---|---|---:|---|
| [OnionScan](https://github.com/s-rah/onionscan) | open-source | 4 | https://github.com/s-rah/onionscan |

### 4. Leak Site & Ransomware Tracking

| Tool | Type | Rank | URL |
|---|---|---:|---|
| [ransomware.live](https://www.ransomware.live/) | open-source + service | 5 | https://www.ransomware.live/ |
| [dls-monitor](https://github.com/cyberiskvision/dls-monitor) | open-source | 4 | https://github.com/cyberiskvision/dls-monitor |

### 5. Onion Search & Discovery

| Tool | Type | Rank | URL / address |
|---|---|---:|---|
| [DuckDuckGo Onion Service](https://duckduckgo.com/onion) | search engine | 4 | https://duckduckgo.com/onion |
| Haystak | search engine | 4 | https://haystak.com/ *(HTTP 404 at verification; re-check address)* |
| OnionLand | search engine | 3 | https://onionland.io *(verify independently)* |
| Tor66 | search/directory | 3 | verify via trusted directory |
| Excavator | search engine | 3 | verify via trusted directory |
| VormWeb | search engine | 3 | verify via trusted directory |
| The Hidden Wiki | directory | 2 | verify via trusted directory |

No unverified `.onion` mirrors are hard-coded in the registry. Addresses that churn are marked `address-verify-needed` or `verify-independently`.

### 6. Privacy & Research Environment

| Tool | Type | Rank | URL |
|---|---|---:|---|
| [Tor Browser](https://www.torproject.org/download/) | open-source | 5 | https://www.torproject.org/download/ |
| [Tails](https://tails.net/) | open-source | 5 | https://tails.net/ |
| [Whonix](https://www.whonix.org/) | open-source | 5 | https://www.whonix.org/ |
| [Qubes OS](https://www.qubes-os.org/) | open-source | 5 | https://www.qubes-os.org/ |

---

## Research documents and source URLs

| Document | Purpose |
|---|---|
| [`rsearch/README.md`](rsearch/README.md) | Research pack overview and usage |
| [`rsearch/CATALOG.md`](rsearch/CATALOG.md) | Generated, evidence-linked catalog |
| [`rsearch/RESEARCH_PROPOSAL.md`](rsearch/RESEARCH_PROPOSAL.md) | Research questions, method, metrics, roadmap |
| [`rsearch/SOURCES.md`](rsearch/SOURCES.md) | Every source URL found, with confidence notes |
| [`rsearch/RECONCILIATION.md`](rsearch/RECONCILIATION.md) | Conflicts with legacy catalog and resolutions |
| [`rsearch/STATUS.json`](rsearch/STATUS.json) | Last run, counts, categories, validation state |
| [`rsearch/CHANGELOG.md`](rsearch/CHANGELOG.md) | Generated update log |
| [`rsearch/registry/tools.json`](rsearch/registry/tools.json) | Human-maintained source of truth |
| [`rsearch/registry/exclusions.json`](rsearch/registry/exclusions.json) | Legacy tools blocked from re-entry |
| [`research/automation_scripts.md`](research/automation_scripts.md) | Automation usage notes |
| [`ranking_criteria.md`](ranking_criteria.md) | Ranking methodology |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution and promotion rules |

Primary source hubs used for verification:

- GitHub API: https://api.github.com/
- theHarvester: https://github.com/laramies/theHarvester
- Recon-ng: https://github.com/lanmaster53/recon-ng
- OnionScan: https://github.com/s-rah/onionscan
- dls-monitor: https://github.com/cyberiskvision/dls-monitor
- ransomware.live: https://www.ransomware.live/
- Shodan: https://www.shodan.io/
- Censys: https://censys.io/
- Maltego: https://www.maltego.com/
- OSINT Framework: https://osintframework.com/
- Tor Project: https://www.torproject.org/
- Tails: https://tails.net/
- Whonix: https://www.whonix.org/
- Qubes OS: https://www.qubes-os.org/
- DuckDuckGo onion service: https://duckduckgo.com/onion

The complete set of primary, cross-check, discovery-only, and rejected URLs is in [`rsearch/SOURCES.md`](rsearch/SOURCES.md).

---

## Repository structure

```text
darkweb-monitor-research/
├── README.md                         # this file
├── CONTRIBUTING.md                   # contribution and promotion rules
├── tools_catalog.md                  # legacy detailed catalog
├── commercial_solutions.md           # legacy commercial category
├── breach_monitoring.md              # legacy breach category
├── ranking_criteria.md               # ranking methodology
├── research/
│   ├── README.md                     # research index
│   └── automation_scripts.md         # automation usage notes
├── categories/
│   ├── osint_tools.md
│   ├── monitoring_tools.md
│   └── search_engines.md
├── rsearch/
│   ├── README.md
│   ├── CATALOG.md                    # generated
│   ├── STATUS.json                   # generated
│   ├── CHANGELOG.md                  # generated
│   ├── RESEARCH_PROPOSAL.md
│   ├── SOURCES.md
│   ├── RECONCILIATION.md
│   ├── registry/
│   │   ├── tools.json
│   │   └── exclusions.json
│   ├── automation/
│   │   ├── refresh_catalog.py
│   │   ├── discover_candidates.py
│   │   ├── queries.json
│   │   ├── test_research.py
│   │   └── watch.sh
│   └── candidates/                   # staged, review-only
└── .github/workflows/
    └── research-auto-update.yml      # cron: every 6 hours
```

---

## Automatic updates

### Hosted automation

[`.github/workflows/research-auto-update.yml`](.github/workflows/research-auto-update.yml) runs every 6 hours (`17 */6 * * *`, UTC). On each run it:

1. Runs offline unit tests.
2. Refreshes GitHub/HTTP metadata for verified tools.
3. Discovers new candidates from GitHub search and DuckDuckGo HTML.
4. Writes candidates to `rsearch/candidates/` for human review.
5. Regenerates `CATALOG.md`, `STATUS.json`, and `CHANGELOG.md`.
6. Commits only when generated output actually changes.

New candidates are **never** auto-promoted into the verified registry.

### Local commands

```sh
# Offline validation and rendering
python3 -m unittest discover -s rsearch/automation -p 'test_*.py' -v
python3 rsearch/automation/refresh_catalog.py --offline

# Live refresh (GITHUB_TOKEN optional, raises rate limits)
GITHUB_TOKEN=... python3 rsearch/automation/refresh_catalog.py
python3 rsearch/automation/discover_candidates.py

# Local continuous loop, 6-hour interval by default
INTERVAL=21600 sh rsearch/automation/watch.sh
```

---

## Ranking system

Each tool is scored on five equally weighted criteria:

1. Feature completeness
2. Platform compatibility
3. Community adoption
4. Update frequency
5. Documentation quality

| Score | Meaning |
|---|---|
| ⭐⭐⭐⭐⭐ / 5 | Excellent across all criteria, primary-source verified |
| ⭐⭐⭐⭐ / 4 | Strong with minor limitations |
| ⭐⭐⭐ / 3 | Useful niche tool |
| ⭐⭐ / 2 | Basic or orientation-only |
| ⭐ / 1 | Experimental or very specialized |

Full methodology: [`ranking_criteria.md`](ranking_criteria.md).

---

## Platform support

| Category | Windows | Linux | Notes |
|---|---|---|---|
| OSINT Automation & Frameworks | SpiderFoot | SpiderFoot, Darkdump, TorBot | Darkdump is Linux-first |
| Exposure Monitoring | Darkwatch | Darkwatch, TorBot | TorBot is cross-listed |
| Search Engines & Directories | via Tor Browser | via Tor Browser | Onion addresses churn |
| Breach & Credential Monitoring | web/API | web/API | HIBP, Intelligence X |
| Commercial Solutions | dashboards/API | dashboards/API | web-based |
| OSINT & Reconnaissance | Python/web | native | theHarvester, Recon-ng, Maltego, OSINT Framework |
| Attack Surface Intelligence | web/API | web/API | Shodan, Censys |
| Onion Service Assessment | limited | native | OnionScan uses Go + Tor |
| Leak Site Tracking | web/API | native/container | dls-monitor uses GitHub Actions |
| Onion Search & Discovery | via Tor Browser | via Tor Browser | verify addresses first |
| Privacy & Research Environment | Tor Browser, Tails host | all tools | Qubes is Linux-host only |

Platform legend: ✅ full support · ❌ unsupported · 🌐 via browser/Tor · ⚠️ verify before use.

---

## Deduplication policy

1. Identity is normalized from name, canonical URL, GitHub `owner/repo`, and aliases.
2. Every new tool is checked against `rsearch/registry/tools.json` **and** `rsearch/registry/exclusions.json`.
3. Any collision fails the offline test suite and blocks catalog generation.
4. Discovery output is staged only; a human promotes entries after primary-source verification.

Current state: 0 duplicate collisions, 20/20 new tools with evidence URLs.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). In short:

1. Check the exclusion registry first.
2. Add or update a JSON record in `rsearch/registry/tools.json`.
3. Include at least one primary-source `https://` URL and a verification date.
4. Run the offline tests and refresh script.
5. Commit the registry and regenerated catalog files together.

Legacy files may still be edited directly, but conflicts should be recorded in [`rsearch/RECONCILIATION.md`](rsearch/RECONCILIATION.md).

---

## Legal and ethical notice

- Research, defensive security, and journalism only.
- No weaponized exploit code, stolen data, or instructions for unauthorized access.
- Access only content you are permitted to access; comply with all applicable laws.
- Leak-site metadata is for exposure awareness, not for retrieving or redistributing leaked content.
- Scan onion services only when you operate them or have explicit authorization.

---

*Maintained with the goal of being the most transparent, reproducible dark-web research catalog on GitHub. Star ⭐ the repo to support continuous verification.*

*Last updated: 2026-11-23 (UTC)*
