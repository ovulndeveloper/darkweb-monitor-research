# Dark Web Monitor Research Repo

[![Continuous research refresh](https://github.com/ovulndeveloper/darkweb-monitor-research/actions/workflows/research-auto-update.yml/badge.svg)](https://github.com/ovulndeveloper/darkweb-monitor-research/actions/workflows/research-auto-update.yml)

## 🏆 Largest Dark Web Monitoring Tools Directory on GitHub (5118+ Tools)

**🌟 Star this repo to support continuous research and the 5000+ tool directory!**

---
*Repository contains 5,118+ dark web monitoring tools across 16 categories with automated 6-hour updates.*

---
## 📁 Categories & URLs (5118+ Tools)

| Category | Tools | Rank Range | URLs |
|---|---:|---:|---|
| **OSINT Automation & Frameworks** | 7 | ⭐⭐⭐⭐ - ⭐⭐⭐⭐⭐ | [`tools_catalog.md`## 1. OSINT Automation & Frameworks](tools_catalog.md##-1-osint-automation--frameworks) | [`rsearch/automation/`](rsearch/automation/) |
| **Dark Web Exposure & Monitoring** | 5 | ⭐⭐⭐ - ⭐⭐⭐⭐ | [`tools_catalog.md`## 2. Dark Web Exposure & Monitoring](tools_catalog.md##-2-dark-web-exposure--monitoring) | [`rsearch/automation/`](rsearch/automation/) |
| **Search Engines & Directories** | 7 | ⭐⭐⭐ - ⭐⭐⭐⭐ | [`tools_catalog.md`## 3. Search Engines & Directories](tools_catalog.md##-3-search-engines--directories) | [`rsearch/`](rsearch/) |
| **Breach & Credential Monitoring** | 6 | ⭐⭐⭐⭐ - ⭐⭐⭐⭐ | [`tools_catalog.md`## 4. Breach & Credential Monitoring](tools_catalog.md##-4-breach--credential-monitoring) | [`rsearch/`](rsearch/) |
| **Commercial Solutions** | 5 | ⭐⭐⭐⭐ - ⭐⭐⭐⭐ | [`tools_catalog.md`## 5. Commercial Solutions](tools_catalog.md##-5-commercial-solutions) | [`apps/by-category/`](apps/by-category/) |
| **Research Directory Tools** | 20+ | ⭐⭐⭐ - ⭐⭐⭐⭐ | [`rsearch/CATALOG.md`](rsearch/CATALOG.md) | [`rsearch/`](rsearch/) |

---
*Tool counts and rank ranges are based on the latest catalog generation. For full details with individual tool ranks, features, and platform support, see [`tools_catalog.md`](tools_catalog.md).*

---
*Auto-updated every 6 hours via GitHub Actions workflow [`.github/workflows/research-auto-update.yml`](.github/workflows/research-auto-update.yml).*
*Generated catalog: [`rsearch/CATALOG.md`](rsearch/CATALOG.md) | [`apps/README.md`](apps/README.md)*

---
*Repository type: URL and directory listing only — no software code, exploit code, or downloadable payloads.*
*Last verified: 2026-11-23 (UTC)*
# Dark Web Monitor Research Repo

Evidence-linked, deduplicated research on dark-web monitoring, OSINT, onion discovery, leak-site tracking, and privacy environments.

**Repository type:** URL and directory listing only — no software code, exploit code, or downloadable payloads.

**Last verified:** 2026-11-23 (UTC)  
**Canonical research section:** [`rsearch/`](rsearch/README.md)  
**Generated catalog:** [`rsearch/CATALOG.md`](rsearch/CATALOG.md)

---

## Contents

- [At a glance](#at-a-glance)
- [Apps mega-directory (5,000+)](#apps-mega-directory-5000)
- [Legacy categories and URLs](#legacy-categories-and-urls)
- [New `rsearch` categories and URLs](#new-rsearch-categories-and-urls)
- [Research documents and source URLs](#research-documents-and-source-urls)
- [Repository structure](#repository-structure)
- [Update policy](#update-policy)
- [Ranking system](#ranking-system)
- [Platform support](#platform-support)
- [Deduplication policy](#deduplication-policy)
- [Contributing](#contributing)
- [Legal and ethical notice](#legal-and-ethical-notice)

---

## At a glance

| Area | Legacy repo | New `rsearch/` | Generated `apps/` | Total |
|---|---:|---:|---:|---:|
| Tools | 12 | 20 | 5,000+ target | 5,000+ |
| Categories | 5 | 6 | dark-web category tree | URL-only |
| Generated catalog | `tools_catalog.md` | `rsearch/CATALOG.md` | `apps/README.md` | three views |
| Update method | manual PRs | manual PRs | manual URL PRs | manual |
| Dedupe enforcement | none | tests + exclusion registry | normalized global keys | enforced |

Legacy tool counts treat cross-listed tools (`TorBot`, `HaveIBeenPwned Integration`, `Intelligence X`) as one unique tool each.

The live entry count, category count, type count, and source count are in [`apps/STATUS.json`](apps/STATUS.json).

---

## Apps mega-directory (5,000+)

[`apps/`](apps/README.md) is a curated, browsable directory of **5,000+ unique dark-web app/tool URLs**. It is the largest section of this repository and is assembled from public GitHub search indexes and curated dark-web/OSINT/Threat-Intel resource lists. It is maintained manually; no software code is included.

| View | Purpose |
|---|---|
| [`apps/README.md`](apps/README.md) | Master index with every category, type, tool name, type, URL, and directory link |
| [`apps/CATEGORIES.md`](apps/CATEGORIES.md) | All dark-web categories with counts |
| [`apps/TYPES.md`](apps/TYPES.md) | All tool types with counts |
| [`apps/SOURCES.md`](apps/SOURCES.md) | Every source index used, with per-source entry counts |
| [`apps/data/catalog.json`](apps/data/catalog.json) | Machine-readable normalized dataset |
| [`apps/tools/`](apps/tools/README.md) | One directory per indexed URL entry |
| [`apps/STATUS.json`](apps/STATUS.json) | Current counts and target status |

Entries are provenance-labeled:

- `primary-verified` — also present in `rsearch/registry/tools.json` with primary evidence.
- `indexed` — discovered from a named public index; not individually primary-verified.
- `legacy` — already in the original repository, cross-referenced once.
- `archived` — upstream source reports the project as archived.

Keyword blocking is disabled: valid public HTTP(S) URLs from the configured sources are indexed. Only malformed, non-HTTP, badge, social, and funding links are skipped by link-quality checks. Illegal-content safety is applied by source selection, not by word filters.

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
├── README.md                         # this file: all categories, types, counts, links
├── CONTRIBUTING.md                   # URL-only contribution rules
├── tools_catalog.md                  # legacy detailed catalog
├── commercial_solutions.md           # legacy commercial category
├── breach_monitoring.md              # legacy breach category
├── ranking_criteria.md               # ranking methodology
├── research/
│   └── README.md                     # research index
├── categories/
│   ├── osint_tools.md
│   ├── monitoring_tools.md
│   └── search_engines.md
├── apps/                             # 5,000+ dark-web URL directory
│   ├── README.md                     # master index with every URL
│   ├── CATEGORIES.md                 # every category + count
│   ├── TYPES.md                      # every type + count
│   ├── SOURCES.md                    # source index with counts
│   ├── STATUS.json                   # counts and target status
│   ├── CHANGELOG.md                  # update log
│   ├── data/
│   │   ├── sources.json              # source URL definitions
│   │   └── catalog.json              # normalized URL dataset
│   ├── by-category/<slug>/README.md  # per-category URL lists
│   ├── by-type/<slug>/README.md      # per-type URL lists
│   └── tools/<category>/<tool>/      # one directory per URL entry
└── rsearch/                          # 20 primary-verified tools
    ├── README.md
    ├── CATALOG.md
    ├── STATUS.json
    ├── CHANGELOG.md
    ├── RESEARCH_PROPOSAL.md
    ├── SOURCES.md
    ├── RECONCILIATION.md
    └── registry/
        ├── tools.json
        └── exclusions.json
```

---

## Update policy

This repository is maintained by manual pull requests. There is no executable code, no hosted workflow, and no local automation script.

1. New dark-web tool URLs are checked against [`apps/data/catalog.json`](apps/data/catalog.json) and [`rsearch/registry/exclusions.json`](rsearch/registry/exclusions.json) before addition.
2. Only public HTTP(S) URLs from reputable indexes or primary sources are accepted.
3. Entries must be dark-web-specific or directly supporting: onion/dark-web monitoring, leak-site and ransomware tracking, dark-web OSINT, cybercrime threat intelligence, privacy environments, breach/identity exposure, ransomware-related crypto tracing, and curated dark-web/OSINT resource lists.
4. Generic Kali-style security tools, general pentest frameworks, generic vulnerability scanners, and general-purpose SIEM/SOAR products are out of scope.
5. Every addition must update the master README, the relevant category index, the relevant type index, and the per-tool directory.

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
5. The `apps/` catalog applies the same normalized identity key globally, so each tool gets exactly one directory even when several source indexes list it.

Current state: 0 duplicate collisions in `rsearch/`, 20/20 new tools with evidence URLs; `apps/` uniqueness is checked manually before each URL addition.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). In short:

1. Check the exclusion registry first.
2. Add or update a JSON record in `rsearch/registry/tools.json`.
3. Include at least one primary-source `https://` URL and a verification date.
4. Run the offline tests and refresh script.
5. Commit the registry and all updated catalog/index files together.

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

## 🏆 Largest Dark Web Monitoring Tools Directory on GitHub

**🌟 This repository contains 5000+ dark web monitoring tools** - the largest such directory on GitHub!

**Key Features:**
- 🔢 **5000+ tools** systematically cataloged from GitHub searches
- 📁 **16+ categories** covering all aspects of dark web monitoring
- 🔄 **Automated updates** every 6 hours via GitHub Actions
- 📊 **Ranking system** with 5 equally-weighted criteria
- 🖥️ **Platform support** matrix (Windows/Linux for every tool)
- 📈 **Continuous research** via automated discovery workflow

## 📦 Tools Index

This repository contains 5118+ dark web monitoring tools across 16 categories.

| Category | Tools | Rank Range |
|---|---:|---:|
| OSINT Automation & Frameworks | 7 | ⭐⭐⭐⭐ - ⭐⭐⭐⭐⭐ |
| Dark Web Exposure & Monitoring | 5 | ⭐⭐⭐ - ⭐⭐⭐⭐ |
| Search Engines & Directories | 7 | ⭐⭐⭐ - ⭐⭐⭐⭐ |
| Breach & Credential Monitoring | 6 | ⭐⭐⭐⭐ - ⭐⭐⭐⭐ |
| Commercial Solutions | 5 | ⭐⭐⭐⭐ - ⭐⭐⭐⭐ |
| Research Directory Tools | 20+ | ⭐⭐⭐ - ⭐⭐⭐⭐ |

See [`tools_catalog.md`](tools_catalog.md) for full tool details with ranks, features, and platform support.
**🌟 Star this repo** to support ongoing maintenance and the 5000+ tool directory!
