# Dark Web Monitor Research Repo

Evidence-linked, deduplicated research on dark-web monitoring, OSINT, onion discovery, leak-site tracking, and privacy environments.

**Repository type:** URL and directory listing only — no software code, exploit code, or downloadable payloads.

**Last verified:** 2026-11-23 (UTC)  
**Canonical research section:** [`rsearch/`](rsearch/README.md)  
**Generated catalog:** [`rsearch/CATALOG.md`](rsearch/CATALOG.md)

---

## Contents

- [At a glance](#at-a-glance)
- [Apps mega-directory (6,780 URLs)](#apps-mega-directory-6780-urls)
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

| Area | Legacy repo | New `rsearch/` | `apps/` directory |
|---|---:|---:|---:|
| Tools | 12 | 20 | 6,780 |
| Categories | 5 | 6 | 10 |
| Catalog view | `tools_catalog.md` | `rsearch/CATALOG.md` | `apps/README.md` |
| Update method | manual PRs | manual PRs | manual URL PRs |
| Dedupe enforcement | none | exclusion registry | normalized global keys |

Legacy tool counts treat cross-listed tools (`TorBot`, `HaveIBeenPwned Integration`, `Intelligence X`) as one unique tool each.

The live entry count, category count, type count, and source count are in [`apps/STATUS.json`](apps/STATUS.json).

---

## Apps mega-directory (6,780 URLs)

[`apps/`](apps/README.md) is a curated, browsable directory of **6,780 unique dark-web app/tool URLs**. It is the largest section of this repository and is assembled from public GitHub search indexes and curated dark-web/OSINT/Threat-Intel resource lists. It is maintained manually; no software code is included.

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

Scope is enforced by source selection and explicit out-of-scope patterns, not by word-blocking valid URLs. Only malformed, non-HTTP, badge, social, funding, and clearly off-topic or spam links are skipped. Illegal-content safety is applied through reputable source selection.

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
├── apps/                             # 6,780-entry dark-web URL directory
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
3. Any collision is rejected during manual review before a URL is added.
4. A URL is added only after a primary-source or named-index check.
5. The `apps/` catalog applies the same normalized identity key globally, so each tool gets exactly one directory even when several source indexes list it.

Current state: 0 duplicate collisions in `rsearch/`, 20/20 new tools with evidence URLs; `apps/` uniqueness is checked manually before each URL addition.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). In short:

1. Check the exclusion registry first.
2. Add or update a JSON record in `rsearch/registry/tools.json`.
3. Include at least one primary-source `https://` URL and a verification date.
4. Update the matching category index, type index, per-tool directory, and master README row.
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

<!-- COMPLETE_DARK_WEB_URL_INDEX_BEGIN -->

## Complete dark-web URL index

6,780 URLs. Mirrored from [`apps/README.md`](apps/README.md).

| Category | URLs |
|---|---:|
| [Cryptocurrency & Financial Intelligence](apps/by-category/cryptocurrency-financial-intelligence/README.md) | 10 |
| [Dark Web Monitoring & Leak Intelligence](apps/by-category/dark-web-monitoring-leak-intelligence/README.md) | 227 |
| [Identity & Breach Intelligence](apps/by-category/identity-breach-intelligence/README.md) | 34 |
| [OSINT & Reconnaissance](apps/by-category/osint-reconnaissance/README.md) | 3319 |
| [Onion Search & Discovery](apps/by-category/onion-search-discovery/README.md) | 393 |
| [Phishing & Fraud Intelligence](apps/by-category/phishing-fraud-intelligence/README.md) | 431 |
| [Privacy & Anonymity](apps/by-category/privacy-anonymity/README.md) | 415 |
| [Ransomware & Threat Actor Tracking](apps/by-category/ransomware-threat-actor-tracking/README.md) | 505 |
| [Resource Lists & Directories](apps/by-category/resource-lists-directories/README.md) | 5 |
| [Threat Intelligence Platforms](apps/by-category/threat-intelligence-platforms/README.md) | 1441 |

### Cryptocurrency & Financial Intelligence

| Name | Type | URL |
|---|---|---|
| Adamant-im/adamant-im | web-platform | <https://github.com/Adamant-im/adamant-im> |
| bobslayerX/crypttrace | dashboard | <https://github.com/bobslayerX/crypttrace> |
| chaincase-app/Chaincase-iOS-Beta | research-project | <https://github.com/chaincase-app/Chaincase-iOS-Beta> |
| deeponion/deeponion | tool | <https://github.com/deeponion/deeponion> |
| getkenning/kenning | cli-tool | <https://github.com/getkenning/kenning> |
| https://fms.gov.ge | web-platform | <https://fms.gov.ge> |
| metaspartan/denarius | tool | <https://github.com/metaspartan/denarius> |
| MyEtherWallet/ethereum-lists | tool | <https://github.com/MyEtherWallet/ethereum-lists> |
| OffcierCia/On-Chain-Investigations-Tools-List | awesome-list | <https://github.com/OffcierCia/On-Chain-Investigations-Tools-List> |
| watsoncore/Gansar | framework | <https://github.com/watsoncore/Gansar> |

### Dark Web Monitoring & Leak Intelligence

| Name | Type | URL |
|---|---|---|
| 07enesavci/tor-web-scraper | api-service | <https://github.com/07enesavci/tor-web-scraper> |
| 0xbitx/DEDSEC_STOR | web-platform | <https://github.com/0xbitx/DEDSEC_STOR> |
| 0xbitx/DEDSEC_TOR-GHOST | tool | <https://github.com/0xbitx/DEDSEC_TOR-GHOST> |
| 0xHexX1/tor-onion-crawler | tool | <https://github.com/0xHexX1/tor-onion-crawler> |
| 0XX7C00/MSEP | tool | <https://github.com/0XX7C00/MSEP> |
| 201Harsh/DarkWeb | tool | <https://github.com/201Harsh/DarkWeb> |
| 24x7StreamShop/Netflix-Phishing | web-platform | <https://github.com/24x7StreamShop/Netflix-Phishing> |
| 7ife/cbdw | tool | <https://github.com/7ife/cbdw> |
| 7Ragnarok7/DEDMAP | web-platform | <https://github.com/7Ragnarok7/DEDMAP> |
| 99Cryptonic/Tor-Browser-64x68bit | tool | <https://github.com/99Cryptonic/Tor-Browser-64x68bit> |
| abdulhamid529589/Learn-Ethical-Hacking | tool | <https://github.com/abdulhamid529589/Learn-Ethical-Hacking> |
| adityaax/darkweb-directory | awesome-list | <https://github.com/adityaax/darkweb-directory> |
| Ahmia | tool | <https://ahmia.fi> |
| ail-project/ail-framework | api-service | <https://github.com/ail-project/ail-framework> |
| ail-project/onion-lookup | tool | <https://github.com/ail-project/onion-lookup> |
| akashblackhat/dark_web.py | framework | <https://github.com/akashblackhat/dark_web.py> |
| akashblackhat/DarkWeb | tool | <https://github.com/akashblackhat/DarkWeb> |
| Aleph Open Search | tool | <https://open-search.aleph-networks.eu> |
| AlgorithmCodexIT/MercAI-Darknet | plugin | <https://github.com/AlgorithmCodexIT/MercAI-Darknet> |
| Ali-hey-0/Hacking-Tools | tool | <https://github.com/Ali-hey-0/Hacking-Tools> |
| Ali-hey-0/Ransomware.Jigsaw | tool | <https://github.com/Ali-hey-0/Ransomware.Jigsaw> |
| alok-kumar8765/cybersecurity-osint-ai-productivity-guide | awesome-list | <https://github.com/alok-kumar8765/cybersecurity-osint-ai-productivity-guide> |
| anubhavanonymous/HostOnion | web-platform | <https://github.com/anubhavanonymous/HostOnion> |
| AnupamKhurana/robin-custom | tool | <https://github.com/AnupamKhurana/robin-custom> |
| api-evangelist/authentic8 | api-service | <https://github.com/api-evangelist/authentic8> |
| api-evangelist/flashpoint | api-service | <https://github.com/api-evangelist/flashpoint> |
| api-evangelist/terbium-labs | api-service | <https://github.com/api-evangelist/terbium-labs> |
| apurvsinghgautam/conference-talks | tool | <https://github.com/apurvsinghgautam/conference-talks> |
| AradhyaMaheshwari-bit/DCRP-Discord-Darkweb-Bot | tool | <https://github.com/AradhyaMaheshwari-bit/DCRP-Discord-Darkweb-Bot> |
| arnav-kr/tor-tutorial | web-platform | <https://github.com/arnav-kr/tor-tutorial> |
| AshwinAmbal/DarkWeb-Crawling-Indexing | directory | <https://github.com/AshwinAmbal/DarkWeb-Crawling-Indexing> |
| AtharvaKitkaru/multilabel-classifier-for-darkweb | research-project | <https://github.com/AtharvaKitkaru/multilabel-classifier-for-darkweb> |
| atxcowboy/panomity-darkweb-press | plugin | <https://github.com/atxcowboy/panomity-darkweb-press> |
| B0bTheSkull/darkdump_crawl | api-service | <https://github.com/B0bTheSkull/darkdump_crawl> |
| B611/nyja | framework | <https://github.com/B611/nyja> |
| bad-antics/darkweb-ops | api-service | <https://github.com/bad-antics/darkweb-ops> |
| bad-antics/tor-service | web-platform | <https://github.com/bad-antics/tor-service> |
| BenAmpel/hackersignal | dataset | <https://github.com/BenAmpel/hackersignal> |
| bharat3645/CyberHack | container | <https://github.com/bharat3645/CyberHack> |
| BlackDragonCZ/ProjectMercury | browser-extension | <https://github.com/BlackDragonCZ/ProjectMercury> |
| blubskye/yunonet | tool | <https://github.com/blubskye/yunonet> |
| bunseokbot/darklight | tool | <https://github.com/bunseokbot/darklight> |
| ByteBreach/torspy | library | <https://github.com/ByteBreach/torspy> |
| cabalcx/deepblur | plugin | <https://github.com/cabalcx/deepblur> |
| cibr-qcri/dizzy-datasets | dataset | <https://github.com/cibr-qcri/dizzy-datasets> |
| cipher-attack/cipher-osint | plugin | <https://github.com/cipher-attack/cipher-osint> |
| cipher4559/threatgrid | api-service | <https://github.com/cipher4559/threatgrid> |
| ckjbug/Hacking | tool | <https://github.com/ckjbug/Hacking> |
| CloudlyHack/CloudlyHost | tool | <https://github.com/CloudlyHack/CloudlyHost> |
| codedByCan/Dark_Web_de_Site_Kurma | tool | <https://github.com/codedByCan/Dark_Web_de_Site_Kurma> |
| Conso1eCowb0y/Deepminer | research-project | <https://github.com/Conso1eCowb0y/Deepminer> |
| CoopTRUE/CatDen | tool | <https://github.com/CoopTRUE/CatDen> |
| Coordinate-Cat/onion-hosting-1222 | research-project | <https://github.com/Coordinate-Cat/onion-hosting-1222> |
| Corrodedhearts/Dark-Osint | framework | <https://github.com/Corrodedhearts/Dark-Osint> |
| CristianSaftoiu/OSINT-Prototype | tool | <https://github.com/CristianSaftoiu/OSINT-Prototype> |
| CruelDev69/tor-network-search-engine | research-project | <https://github.com/CruelDev69/tor-network-search-engine> |
| curated-intel/Initial-Access-Broker-Landscape | tool | <https://github.com/curated-intel/Initial-Access-Broker-Landscape> |
| CyberSoldiers/onion_check | tool | <https://github.com/CyberSoldiers/onion_check> |
| cynkai/d4d-scce | dashboard | <https://github.com/cynkai/d4d-scce> |
| cysec-lab/onion-soup | tool | <https://github.com/cysec-lab/onion-soup> |
| dark-web-tutorials/hidden-wiki | dashboard | <https://github.com/dark-web-tutorials/hidden-wiki> |
| dark.fail | directory | <https://dark.fail/> |
| DarkHater01/K4L1NUX-DarkWeb-Monitor | tool | <https://github.com/DarkHater01/K4L1NUX-DarkWeb-Monitor> |
| DarkOwl | directory | <https://www.darkowl.com/> |
| darksearch.io | api-service | <https://darksearch.io/> |
| darkseid-security/darkweb | web-platform | <https://github.com/darkseid-security/darkweb> |
| Darkwatch | tool | <https://github.com/Daemon-VI/darkwatch> |
| darkwebjp/darkweb-ready | plugin | <https://github.com/darkwebjp/darkweb-ready> |
| davide-perez/datavisexp-agora | tool | <https://github.com/davide-perez/datavisexp-agora> |
| Debajyoti0-0/HiddenLinks-Explorer | cli-tool | <https://github.com/Debajyoti0-0/HiddenLinks-Explorer> |
| DedSecInside/TorBot | tool | <https://github.com/DedSecInside/TorBot> |
| Dev9269/darkforce | container | <https://github.com/Dev9269/darkforce> |
| dheeraj-jayaswal/DarkWeb-From-The-Trenches | research-project | <https://github.com/dheeraj-jayaswal/DarkWeb-From-The-Trenches> |
| DimosMellios/DarkShotLearning | tool | <https://github.com/DimosMellios/DarkShotLearning> |
| dimyme/onion_host | web-platform | <https://github.com/dimyme/onion_host> |
| doktornand/LeakOrNot | tool | <https://github.com/doktornand/LeakOrNot> |
| element-protocol/element-protocol | tool | <https://github.com/element-protocol/element-protocol> |
| euphoria95/OnionAccelerator | container | <https://github.com/euphoria95/OnionAccelerator> |
| fabriziosalmi/naso | api-service | <https://github.com/fabriziosalmi/naso> |
| facenano/darkwebspider | research-project | <https://github.com/facenano/darkwebspider> |
| fairhive-labs/tor-proxy | container | <https://github.com/fairhive-labs/tor-proxy> |
| FarBeyondUs/DRGLS | web-platform | <https://github.com/FarBeyondUs/DRGLS> |
| fastfire/deepdarkCTI | tool | <https://github.com/fastfire/deepdarkCTI> |
| feloex/vanity-onion | web-platform | <https://github.com/feloex/vanity-onion> |
| fevra-dev/ShadowHunter | api-service | <https://github.com/fevra-dev/ShadowHunter> |
| fish-not-phish/open-vbrowser | container | <https://github.com/fish-not-phish/open-vbrowser> |
| fsociety-git/onionwatch | tool | <https://github.com/fsociety-git/onionwatch> |
| gayanku/darkweb_clearweb_darktopics | dataset | <https://github.com/gayanku/darkweb_clearweb_darktopics> |
| gayanku/NBC-Softmax | research-project | <https://github.com/gayanku/NBC-Softmax> |
| GGianluppi/darkweb_website | tool | <https://github.com/GGianluppi/darkweb_website> |
| Giddyspurz/Dark-Web-Links | tool | <https://github.com/Giddyspurz/Dark-Web-Links> |
| gjbatista/Telegram-DarkWeb-Monitoring | api-service | <https://github.com/gjbatista/Telegram-DarkWeb-Monitoring> |
| gt0day/AnonGT | tool | <https://github.com/gt0day/AnonGT> |
| guyfawkesnight1605/website | tool | <https://github.com/guyfawkesnight1605/website> |
| h6465617468/Happy2EncryptedChat | tool | <https://github.com/h6465617468/Happy2EncryptedChat> |
| HelenaReallyHateCoding/nightwire | cli-tool | <https://github.com/HelenaReallyHateCoding/nightwire> |
| hj1980/torbjorn | tool | <https://github.com/hj1980/torbjorn> |
| hrbrmstr/darkdumpr | tool | <https://github.com/hrbrmstr/darkdumpr> |
| hrhv/tor-nginx-proxy | container | <https://github.com/hrhv/tor-nginx-proxy> |
| hzagaming/tor-onion-cluster | web-platform | <https://github.com/hzagaming/tor-onion-cluster> |
| imshewale/DarkSite | tool | <https://github.com/imshewale/DarkSite> |
| imvickykumar999/CustomOnionURL | web-platform | <https://github.com/imvickykumar999/CustomOnionURL> |
| imvickykumar999/DarkWeb-Flask-CRUD | tool | <https://github.com/imvickykumar999/DarkWeb-Flask-CRUD> |
| imvickykumar999/Flask-XAMPP-Onion-Host | tool | <https://github.com/imvickykumar999/Flask-XAMPP-Onion-Host> |
| imvickykumar999/haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion | tool | <https://github.com/imvickykumar999/haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion> |
| imvickykumar999/prjd5pmbug2cnfs67s3y65ods27vamswdaw2lnwf45ys3pjl55h2gwqd.onion | tool | <https://github.com/imvickykumar999/prjd5pmbug2cnfs67s3y65ods27vamswdaw2lnwf45ys3pjl55h2gwqd.onion> |
| imvickykumar999/silk-road-on-dark-web | tool | <https://github.com/imvickykumar999/silk-road-on-dark-web> |
| imvickykumar999/Tesseract-Image-Search | tool | <https://github.com/imvickykumar999/Tesseract-Image-Search> |
| imvickykumar999/Vanity-Image | web-platform | <https://github.com/imvickykumar999/Vanity-Image> |
| Intelligence X | tool | <https://intelx.io> |
| iqlip/Onion_Endpoints_Fetcher | web-platform | <https://github.com/iqlip/Onion_Endpoints_Fetcher> |
| JacobJandon/OnionClaw | web-platform | <https://github.com/JacobJandon/OnionClaw> |
| JacobJandon/Sicry | web-platform | <https://github.com/JacobJandon/Sicry> |
| Jam0k/Ransomware-Intel | dataset | <https://github.com/Jam0k/Ransomware-Intel> |
| Jam0k/Threat-Intelligence-MCP | api-service | <https://github.com/Jam0k/Threat-Intelligence-MCP> |
| JarryShaw/darc | tool | <https://github.com/JarryShaw/darc> |
| Jash-2000/Dark-Web-analysis | research-project | <https://github.com/Jash-2000/Dark-Web-analysis> |
| jkpnen/dread-parser | tool | <https://github.com/jkpnen/dread-parser> |
| jonypeixoto/hacking-hub | cli-tool | <https://github.com/jonypeixoto/hacking-hub> |
| joshhighet/ransomwatch | research-project | <https://github.com/joshhighet/ransomwatch> |
| joychandbd/darkweb | tool | <https://github.com/joychandbd/darkweb> |
| JUSTSAIF/28P-Chat | web-platform | <https://github.com/JUSTSAIF/28P-Chat> |
| KaanTuran28/CTI_Scrapper_2 | api-service | <https://github.com/KaanTuran28/CTI_Scrapper_2> |
| KaanTuran28/CTI_Scrapper_3 | container | <https://github.com/KaanTuran28/CTI_Scrapper_3> |
| KatrielMoses/voidaccess | web-platform | <https://github.com/KatrielMoses/voidaccess> |
| KingAkeem/TorBotApp | desktop-app | <https://github.com/KingAkeem/TorBotApp> |
| kot1lin/cipher-darkweb-websites | web-platform | <https://github.com/kot1lin/cipher-darkweb-websites> |
| l0lsec/flare-lookup-cli | api-service | <https://github.com/l0lsec/flare-lookup-cli> |
| logicshrey/Dark-Web-Exposure-Threat-Intelligence | web-platform | <https://github.com/logicshrey/Dark-Web-Exposure-Threat-Intelligence> |
| Lucksi/Darkus | tool | <https://github.com/Lucksi/Darkus> |
| mabiasoft/Dark-Web-Search-Engine-Tools | tool | <https://github.com/mabiasoft/Dark-Web-Search-Engine-Tools> |
| machine1337/anonsurf | tool | <https://github.com/machine1337/anonsurf> |
| mahdy-gribkov/DarkWeb-Scanner | api-service | <https://github.com/mahdy-gribkov/DarkWeb-Scanner> |
| Malwareman007/UnderworldQuest | cli-tool | <https://github.com/Malwareman007/UnderworldQuest> |
| maxieds/public-file-stashes | dataset | <https://github.com/maxieds/public-file-stashes> |
| Mhmdjazarah/TIScan | plugin | <https://github.com/Mhmdjazarah/TIScan> |
| michelledelgadob/Visualizaci-n-de-datos | tool | <https://github.com/michelledelgadob/Visualizaci-n-de-datos> |
| mikalv/awesome-i2p | awesome-list | <https://github.com/mikalv/awesome-i2p> |
| milosilo/onion_detector | tool | <https://github.com/milosilo/onion_detector> |
| mohsecurity254/mohsecurity254.github.io | directory | <https://github.com/mohsecurity254/mohsecurity254.github.io> |
| Morgan-Sell/darknet-economics | tool | <https://github.com/Morgan-Sell/darknet-economics> |
| MTXPr0ject/Dark-Web-Links | web-platform | <https://github.com/MTXPr0ject/Dark-Web-Links> |
| mynkpdr/darkwebdemo | tool | <https://github.com/mynkpdr/darkwebdemo> |
| N1ckw1ck/Dark_OSINT | directory | <https://github.com/N1ckw1ck/Dark_OSINT> |
| N4rr34n6/MonOnion | api-service | <https://github.com/N4rr34n6/MonOnion> |
| N4rr34n6/OnionDomainExtractor | api-service | <https://github.com/N4rr34n6/OnionDomainExtractor> |
| N4rr34n6/OnionScanner | plugin | <https://github.com/N4rr34n6/OnionScanner> |
| nataliaumeyor-hue/finsentinel-aml-intelligence | web-platform | <https://github.com/nataliaumeyor-hue/finsentinel-aml-intelligence> |
| NexvisionLab/Darkweb-search-engine | directory | <https://github.com/NexvisionLab/Darkweb-search-engine> |
| NGlory7/TorOsintScraper | web-platform | <https://github.com/NGlory7/TorOsintScraper> |
| nikhilnayak98/cdp | tool | <https://github.com/nikhilnayak98/cdp> |
| nikita-bachhas/Analysis-of-Ransomware-Groups | api-service | <https://github.com/nikita-bachhas/Analysis-of-Ransomware-Groups> |
| oniontree-org/oniontree | web-platform | <https://github.com/oniontree-org/oniontree> |
| PabloChatTR/deep-web-siteler-2023 | tool | <https://github.com/PabloChatTR/deep-web-siteler-2023> |
| Pandya-mayur/GhostCrawler | tool | <https://github.com/Pandya-mayur/GhostCrawler> |
| panzertime/dw-findingstore | tool | <https://github.com/panzertime/dw-findingstore> |
| PasteHunter | tool | <https://github.com/kevthehermit/PasteHunter> |
| paulveillard/cybersecurity-dark-web | awesome-list | <https://github.com/paulveillard/cybersecurity-dark-web> |
| phantomx39/Scraper | api-service | <https://github.com/phantomx39/Scraper> |
| phishing-hunter/dark-fess | container | <https://github.com/phishing-hunter/dark-fess> |
| prakhar0x01/Tornet_Granted | web-platform | <https://github.com/prakhar0x01/Tornet_Granted> |
| Pranith-Jain/deepdarkcti-parser | directory | <https://github.com/Pranith-Jain/deepdarkcti-parser> |
| PritamSarbajna/dark-web-scraper | tool | <https://github.com/PritamSarbajna/dark-web-scraper> |
| Priteshmane7895/dark-web-threat-intelligence-crawler | tool | <https://github.com/Priteshmane7895/dark-web-threat-intelligence-crawler> |
| PROxZIMA/DarkSpider | tool | <https://github.com/PROxZIMA/DarkSpider> |
| psbdmp | tool | <https://psbdmp.ws/> |
| punyamsingh/Dark-Web-Reporting-System | tool | <https://github.com/punyamsingh/Dark-Web-Reporting-System> |
| pushprajthakre/CounterIntelCTI | tool | <https://github.com/pushprajthakre/CounterIntelCTI> |
| pwndb | web-platform | <https://github.com/davidtavarez/pwndb> |
| pystemon | tool | <https://github.com/cvandeplas/pystemon> |
| qompassai/ghost | tool | <https://github.com/qompassai/ghost> |
| qompassai/tor | tool | <https://github.com/qompassai/tor> |
| Rajveer2009/Dark-Website | tool | <https://github.com/Rajveer2009/Dark-Website> |
| redblade7/darkwebmysterybot | tool | <https://github.com/redblade7/darkwebmysterybot> |
| Req999/darkwebspyder | api-service | <https://github.com/Req999/darkwebspyder> |
| RicYaben/midnight_sea | research-project | <https://github.com/RicYaben/midnight_sea> |
| ritchiemwewa/pyahmia | api-service | <https://github.com/ritchiemwewa/pyahmia> |
| ritchiemwewa/tor2tor | web-platform | <https://github.com/ritchiemwewa/tor2tor> |
| Rohankaf/Rottweiler | api-service | <https://github.com/Rohankaf/Rottweiler> |
| sakuraven/artigo-deep-web | tool | <https://github.com/sakuraven/artigo-deep-web> |
| samrigby64/umbra | api-service | <https://github.com/samrigby64/umbra> |
| sanfor2004/XGS | web-platform | <https://github.com/sanfor2004/XGS> |
| shellytrifonov/dark-web-scraper | container | <https://github.com/shellytrifonov/dark-web-scraper> |
| shiftctrlspace/library | web-platform | <https://github.com/shiftctrlspace/library> |
| sidmulajkar/side-projects | tool | <https://github.com/sidmulajkar/side-projects> |
| SlowsieNT/fastonion | web-platform | <https://github.com/SlowsieNT/fastonion> |
| SnehalPrince/UMBRA-Intelligence-platform | dashboard | <https://github.com/SnehalPrince/UMBRA-Intelligence-platform> |
| snippray/Hell0 | web-platform | <https://github.com/snippray/Hell0> |
| some-man1/TorSearcher | tool | <https://github.com/some-man1/TorSearcher> |
| SOUMAJYOTI/Hacker_Social_Networks | tool | <https://github.com/SOUMAJYOTI/Hacker_Social_Networks> |
| spideydotjs/gengar | web-platform | <https://github.com/spideydotjs/gengar> |
| ss-d3v/onionX | web-platform | <https://github.com/ss-d3v/onionX> |
| strauss02/scraper-backend | api-service | <https://github.com/strauss02/scraper-backend> |
| suadatbiniqbal/VeilScrape | dashboard | <https://github.com/suadatbiniqbal/VeilScrape> |
| sukesh-ak/Torify.NET | tool | <https://github.com/sukesh-ak/Torify.NET> |
| sumithemmadi/tor-hidden-service-on-heroku | web-platform | <https://github.com/sumithemmadi/tor-hidden-service-on-heroku> |
| sumithemmadi/Tor-Onion-Service-On-Heroku | web-platform | <https://github.com/sumithemmadi/Tor-Onion-Service-On-Heroku> |
| sureshpandiyan1/DarkTorrentSearcher | cli-tool | <https://github.com/sureshpandiyan1/DarkTorrentSearcher> |
| sylhetyhackvenger/ONYXINT | api-service | <https://github.com/sylhetyhackvenger/ONYXINT> |
| Tarunjit45/repo-specialist | api-service | <https://github.com/Tarunjit45/repo-specialist> |
| teal33t/poopak | container | <https://github.com/teal33t/poopak> |
| TeamHexCommand/drugsy | api-service | <https://github.com/TeamHexCommand/drugsy> |
| TeamKillerX/kyosuke | api-service | <https://github.com/TeamKillerX/kyosuke> |
| The-Osint-Toolbox/Darkweb-OSINT | tool | <https://github.com/The-Osint-Toolbox/Darkweb-OSINT> |
| thehackerthathacks/rsx-osint | framework | <https://github.com/thehackerthathacks/rsx-osint> |
| thunderstornX/dark-web-monitor-lite | tool | <https://github.com/thunderstornX/dark-web-monitor-lite> |
| torserv/torserv | web-platform | <https://github.com/torserv/torserv> |
| tpdlshdmlrkfmcla/Dark_Web | tool | <https://github.com/tpdlshdmlrkfmcla/Dark_Web> |
| trsi-me/TS-OSINT | api-service | <https://github.com/trsi-me/TS-OSINT> |
| Tweacked/bone-browser | tool | <https://github.com/Tweacked/bone-browser> |
| unicxa/OpenJavaTerm | web-platform | <https://github.com/unicxa/OpenJavaTerm> |
| urbanadventurer/WhatWeb | tool | <https://github.com/urbanadventurer/WhatWeb> |
| UsamaMatrix/ai-threat-intel | tool | <https://github.com/UsamaMatrix/ai-threat-intel> |
| Vampsecure-Labs/vamp-darkweb-intel | cli-tool | <https://github.com/Vampsecure-Labs/vamp-darkweb-intel> |
| Viralmaniar/DDWPasteRecon | directory | <https://github.com/Viralmaniar/DDWPasteRecon> |
| vlall/Darksearch | api-service | <https://github.com/vlall/Darksearch> |
| vshulcz/darkweb_search_engine | tool | <https://github.com/vshulcz/darkweb_search_engine> |
| W4W1R3/PARPUS_LABS | framework | <https://github.com/W4W1R3/PARPUS_LABS> |
| wayenfrei3/acadiaforum | tool | <https://github.com/wayenfrei3/acadiaforum> |
| webdragon63/Inspy | tool | <https://github.com/webdragon63/Inspy> |
| wiseaidev/dark-web-rust | research-project | <https://github.com/wiseaidev/dark-web-rust> |
| wjyxiaojiu-del/gravity-topology | tool | <https://github.com/wjyxiaojiu-del/gravity-topology> |
| wolketich/THM-Writeup | library | <https://github.com/wolketich/THM-Writeup> |
| X-3306/darkweb-website | tool | <https://github.com/X-3306/darkweb-website> |
| xbara0x/nullius-in-onion | web-platform | <https://github.com/xbara0x/nullius-in-onion> |
| yottajunaid/Master-Darknet-Backup | dashboard | <https://github.com/yottajunaid/Master-Darknet-Backup> |
| zuzke/capNcook | container | <https://github.com/zuzke/capNcook> |

### Identity & Breach Intelligence

| Name | Type | URL |
|---|---|---|
| breach-parse | cli-tool | <https://github.com/hmaverickadams/breach-parse> |
| bugourmet/mailhunter | cli-tool | <https://github.com/bugourmet/mailhunter> |
| check-if-email-exists | tool | <https://github.com/reacherhq/check-if-email-exists> |
| CredenShow | tool | <https://credenshow.com/> |
| databreach.com | tool | <https://databreach.com/> |
| DDoSecrets | tool | <https://ddosecrets.org/> |
| EmailHarvester | tool | <https://github.com/maldevel/EmailHarvester> |
| HEROIC.NOW | tool | <https://heroic.com/> |
| HIB Ransomed | tool | <https://haveibeenransom.com/> |
| https://numbuster.com | tool | <https://numbuster.com> |
| https://phonebookoftheworld.com/tbilisi/ | tool | <https://phonebookoftheworld.com/tbilisi/> |
| hudsonrock.com | tool | <https://www.hudsonrock.com/free-report> |
| ibnaleem/rules | tool | <https://github.com/ibnaleem/rules> |
| ibnaleem/tables | awesome-list | <https://github.com/ibnaleem/tables> |
| IKnowYour.Dad | tool | <https://iknowyour.dad/> |
| khast3x/h8mail | web-platform | <https://github.com/khast3x/h8mail> |
| LeakCheck/leakcheck-api | api-service | <https://github.com/LeakCheck/leakcheck-api> |
| LeakPeek | tool | <https://leakpeek.com/> |
| LeakRadar | directory | <https://leakradar.io/en> |
| libphonenumber | library | <https://github.com/google/libphonenumber> |
| martinvigo/email2phonenumber | tool | <https://github.com/martinvigo/email2phonenumber> |
| NumLookup | tool | <https://www.numlookup.com/> |
| numverify | api-service | <https://numverify.com> |
| Phonebook.cz | directory | <https://phonebook.cz/> |
| RanaKhan77/Exposure-Check-OSINT | container | <https://github.com/RanaKhan77/Exposure-Check-OSINT> |
| RansomLook | tool | <https://www.ransomlook.io/> |
| Requiem232/weakpass-cli | api-service | <https://github.com/Requiem232/weakpass-cli> |
| scatteredsecrets.com | web-platform | <https://scatteredsecrets.com/> |
| Snusbase | dataset | <https://snusbase.com/> |
| StealSeek | tool | <https://stealseek.io/> |
| Twilio Lookup | api-service | <https://www.twilio.com/docs/lookup> |
| Vendor History | tool | <https://vendorhistory.com/> |
| Whiteintel | tool | <https://whiteintel.io/> |
| XposedOrNot | api-service | <https://xposedornot.com> |

### OSINT & Reconnaissance

| Name | Type | URL |
|---|---|---|
| 003random/getJS | tool | <https://github.com/003random/getJS> |
| 003random/ICU | dataset | <https://github.com/003random/ICU> |
| 00xc/h2buster | directory | <https://github.com/00xc/h2buster> |
| 0bin | tool | <https://0bin.net> |
| 0x0be/yesitsme | tool | <https://github.com/0x0be/yesitsme> |
| 0x0FB0/pulsar | plugin | <https://github.com/0x0FB0/pulsar> |
| 0x1Jar/spy-py | plugin | <https://github.com/0x1Jar/spy-py> |
| 0x6rss/instagram-private-graph | tool | <https://github.com/0x6rss/instagram-private-graph> |
| 0x6rss/matkap | tool | <https://github.com/0x6rss/matkap> |
| 0xAgun/All1 | tool | <https://github.com/0xAgun/All1> |
| 0xarun/s1mr3c | tool | <https://github.com/0xarun/s1mr3c> |
| 0xcyberpj/tweet-machine | tool | <https://github.com/0xcyberpj/tweet-machine> |
| 0xDanielLopez/phishing_kits | tool | <https://github.com/0xDanielLopez/phishing_kits> |
| 0xDanielLopez/TweetFeed | dataset | <https://github.com/0xDanielLopez/TweetFeed> |
| 0xDanielLopez/TweetFeed_code | dataset | <https://github.com/0xDanielLopez/TweetFeed_code> |
| 0xdekster/deksterecon | web-platform | <https://github.com/0xdekster/deksterecon> |
| 0xdekster/ReconNote | web-platform | <https://github.com/0xdekster/ReconNote> |
| 0xdf hacks stuff | tool | <https://0xdf.gitlab.io> |
| 0xNyk/xint | cli-tool | <https://github.com/0xNyk/xint> |
| 0xPrateek/Stardox | api-service | <https://github.com/0xPrateek/Stardox> |
| 0xPugal/bounty.sh | cli-tool | <https://github.com/0xPugal/bounty.sh> |
| 0xPugal/SubDomz | tool | <https://github.com/0xPugal/SubDomz> |
| 0xRamInf0sec/SocialRecon | tool | <https://github.com/0xRamInf0sec/SocialRecon> |
| 0xSaikat/findme | framework | <https://github.com/0xSaikat/findme> |
| 123tool/liner-osint-tool-app | dashboard | <https://github.com/123tool/liner-osint-tool-app> |
| 1337isnot1337/DOPPLERGEIST | tool | <https://github.com/1337isnot1337/DOPPLERGEIST> |
| 192 (UK) | tool | <https://www.192.com> |
| 1in9e/gosint | web-platform | <https://github.com/1in9e/gosint> |
| 1in9e/icp-domains | tool | <https://github.com/1in9e/icp-domains> |
| 1N3/BlackWidow | web-platform | <https://github.com/1N3/BlackWidow> |
| 1N3/Goohak | tool | <https://github.com/1N3/Goohak> |
| 1N3/Sn1per | plugin | <https://github.com/1N3/Sn1per> |
| 1ojew/osint-rehberi | dashboard | <https://github.com/1ojew/osint-rehberi> |
| 1st Headlines | tool | <https://www.1stheadlines.com> |
| 220vk.com | tool | <https://220vk.com/> |
| 2Chat | tool | <https://2chat.co/tools/whatsapp-checker> |
| 2lingual Search | tool | <https://www.2lingual.com> |
| 3mmarx/AcquiFinder | api-service | <https://github.com/3mmarx/AcquiFinder> |
| 3mmarx/Medium-Miner | tool | <https://github.com/3mmarx/Medium-Miner> |
| 3nock/OTE | research-project | <https://github.com/3nock/OTE> |
| 411 (US) | tool | <https://www.411.com> |
| 44za12/mailsleuth | api-service | <https://github.com/44za12/mailsleuth> |
| 4chan Search | tool | <https://4chansearch.com/> |
| 4m3rr0r/SubreconGemini | tool | <https://github.com/4m3rr0r/SubreconGemini> |
| 4ryanwalia/Myrecon | api-service | <https://github.com/4ryanwalia/Myrecon> |
| 5nacks/OSINTBookmarks | framework | <https://github.com/5nacks/OSINTBookmarks> |
| 69KaPuChiNo/MetaGhost | tool | <https://github.com/69KaPuChiNo/MetaGhost> |
| 6abd/horus | api-service | <https://github.com/6abd/horus> |
| 7onez/cti-expert | api-service | <https://github.com/7onez/cti-expert> |
| 7RU7H/Archive | directory | <https://github.com/7RU7H/Archive> |
| 7WaySecurity/cloud_osint | awesome-list | <https://github.com/7WaySecurity/cloud_osint> |
| A1 Website Download | tool | <https://www.microsystools.com/products/website-download> |
| A3h1nt/Grawler | api-service | <https://github.com/A3h1nt/Grawler> |
| a3r0id/OSINT-Scripts | tool | <https://github.com/a3r0id/OSINT-Scripts> |
| aa419 Fake Sites Database | dataset | <https://db.aa419.org/fakebankslist.php> |
| aaarghhh/awesome_osint_blockchain_analysis | awesome-list | <https://github.com/aaarghhh/awesome_osint_blockchain_analysis> |
| AabyssZG/Open-Source-Information-Leakage | tool | <https://github.com/AabyssZG/Open-Source-Information-Leakage> |
| aadinternals | directory | <https://aadinternals.com/osint> |
| aalex954/HTTP-Fingerprinting-Server | tool | <https://github.com/aalex954/HTTP-Fingerprinting-Server> |
| aalex954/MSFT-IP-Tracker | cli-tool | <https://github.com/aalex954/MSFT-IP-Tracker> |
| aancw/Belati | research-project | <https://github.com/aancw/Belati> |
| aashifm1/OSINT-framework | framework | <https://github.com/aashifm1/OSINT-framework> |
| aasimxs/raven | web-platform | <https://github.com/aasimxs/raven> |
| abdulhalimaltuntas/capsaicin | directory | <https://github.com/abdulhalimaltuntas/capsaicin> |
| AbelPhilippe/superhashida | web-platform | <https://github.com/AbelPhilippe/superhashida> |
| abhisharma404/vault | tool | <https://github.com/abhisharma404/vault> |
| Abine | tool | <https://www.abine.com> |
| abuse.ch | dataset | <https://abuse.ch/> |
| Abusech | web-platform | <https://hunting.abuse.ch> |
| Abuseipdb | tool | <https://www.abuseipdb.com/> |
| abuseipdb.com/api | api-service | <https://www.abuseipdb.com/api> |
| ABYZNewsLinks | tool | <https://www.abyznewslinks.com> |
| Academia | web-platform | <https://academia.edu> |
| Academic Journals | tool | <https://www.academicjournals.org> |
| Acceis/leakScraper | tool | <https://github.com/Acceis/leakScraper> |
| Accuranker | research-project | <https://www.accuranker.com> |
| ACRA BizFile | web-platform | <https://www.bizfile.gov.sg/> |
| Ademking/FlashFuzz | plugin | <https://github.com/Ademking/FlashFuzz> |
| aditya720p/FaceDeface | tool | <https://github.com/aditya720p/FaceDeface> |
| Adium | tool | <https://adium.im> |
| adjisoft/redzeye | tool | <https://github.com/adjisoft/redzeye> |
| ADS-B Exchange | tool | <https://www.adsbexchange.com/> |
| Aeon | tool | <https://www.aeontimeline.com> |
| aetherdll/SealFinder | cli-tool | <https://github.com/aetherdll/SealFinder> |
| African Journal Online | web-platform | <https://www.ajol.info> |
| Agence France-Presse (AFP) | tool | <https://www.afp.com> |
| AgentFNS_Bot | tool | <https://t.me/AgentFNS_bot> |
| AgentSultanHub/dcrxoikn | tool | <https://github.com/AgentSultanHub/dcrxoikn> |
| AGOA Data Center | tool | <https://agoa.info> |
| AhmadHassan-BTed/SilentSniffer | framework | <https://github.com/AhmadHassan-BTed/SilentSniffer> |
| ahmadsalamifar/OmniCrawler | api-service | <https://github.com/ahmadsalamifar/OmniCrawler> |
| ahrefs | research-project | <https://ahrefs.com> |
| AidData | tool | <https://aiddata.org> |
| airborne-commando/OPSEC-OSINT-Tools | dashboard | <https://github.com/airborne-commando/OPSEC-OSINT-Tools> |
| AIS-catcher | tool | <https://github.com/jvde-github/AIS-catcher> |
| ajayalf/KUMAL_OSINT | tool | <https://github.com/ajayalf/KUMAL_OSINT> |
| ajuelosemmanuel/duolingOSINT | api-service | <https://github.com/ajuelosemmanuel/duolingOSINT> |
| ajuelosemmanuel/philINT | tool | <https://github.com/ajuelosemmanuel/philINT> |
| akamhy/waybackpy | api-service | <https://github.com/akamhy/waybackpy> |
| akashblackhat/no-infoga.py | tool | <https://github.com/akashblackhat/no-infoga.py> |
| Akwa-al/TraceLens | tool | <https://github.com/Akwa-al/TraceLens> |
| al-sultani/url-tracker | tool | <https://github.com/al-sultani/url-tracker> |
| Alb-310/Geogramint | research-project | <https://github.com/Alb-310/Geogramint> |
| AlbertArakelyan/Hound | framework | <https://github.com/AlbertArakelyan/Hound> |
| alectoaa/Alecto-OSINT | api-service | <https://github.com/alectoaa/Alecto-OSINT> |
| aleksandergrambelik-png/sanderhub-docs | mobile-app | <https://github.com/aleksandergrambelik-png/sanderhub-docs> |
| Aleph | api-service | <https://github.com/Belluxx/Aleph> |
| alephdata/aleph | dataset | <https://github.com/alephdata/aleph> |
| AlephNullSK/dnsgen | research-project | <https://github.com/AlephNullSK/dnsgen> |
| Aletheia (image forensics) | tool | <https://www.aletheia.ai> |
| AlexC-ux/Arina-OSINT-nickname-checker | framework | <https://github.com/AlexC-ux/Arina-OSINT-nickname-checker-> |
| Alfredredbird/tookie-osint | framework | <https://github.com/Alfredredbird/tookie-osint> |
| Alikhalkhali/active-ip | tool | <https://github.com/Alikhalkhali/active-ip> |
| All-in-One | tool | <https://all-io.net> |
| Alleba (Philippines) | tool | <https://www.alleba.com> |
| AllStocksLinks | research-project | <https://www.allstocks.com/links> |
| AllTheInternet | tool | <https://www.alltheinternet.com> |
| Alltop | tool | <https://alltop.com> |
| AllYouCanRead | tool | <https://www.allyoucanread.com> |
| almroot/proxylist | tool | <https://github.com/almroot/proxylist> |
| alpkeskin/mosint | web-platform | <https://github.com/alpkeskin/mosint> |
| alterx | tool | <https://github.com/projectdiscovery/alterx> |
| ALW1EZ/PANO | web-platform | <https://github.com/ALW1EZ/PANO> |
| American Society of Civil Engineers | tool | <https://ascelibrary.org> |
| AnalyzeID | tool | <https://analyzeid.com/> |
| Anas0x1/reconas | tool | <https://github.com/Anas0x1/reconas> |
| Ancestry | tool | <https://www.ancestry.com> |
| ANG13T/netspionage | cli-tool | <https://github.com/ANG13T/netspionage> |
| ANG13T/SatIntel | research-project | <https://github.com/ANG13T/SatIntel> |
| ANG13T/skytrack | tool | <https://github.com/ANG13T/skytrack> |
| Ankit-ku-panda/ALL-IN-OSINT | framework | <https://github.com/Ankit-ku-panda/ALL-IN-OSINT> |
| Ankit-ku-panda/Simple-Osint | framework | <https://github.com/Ankit-ku-panda/Simple-Osint> |
| AnLoMinus/ScanPro | tool | <https://github.com/AnLoMinus/ScanPro> |
| anmolksachan/CVESeeker | tool | <https://github.com/anmolksachan/CVESeeker> |
| anmolksachan/TheTimeMachine | tool | <https://github.com/anmolksachan/TheTimeMachine> |
| AnnusShahzad/Threadline | api-service | <https://github.com/AnnusShahzad/Threadline> |
| Anomali ThreatStream | web-platform | <https://www.anomali.com> |
| Anon-Artist/R3C0Nizer | web-platform | <https://github.com/Anon-Artist/R3C0Nizer> |
| AnonCatalyst/Coeus-OSINT-ToolBox | web-platform | <https://github.com/AnonCatalyst/Coeus-OSINT-ToolBox> |
| AnonCatalyst/DepthSearch | api-service | <https://github.com/AnonCatalyst/DepthSearch> |
| AnonCatalyst/EXEC-TOOLKIT | plugin | <https://github.com/AnonCatalyst/EXEC-TOOLKIT> |
| AnonCatalyst/InsightHub | dashboard | <https://github.com/AnonCatalyst/InsightHub> |
| AnonCatalyst/NmapGuidon | dashboard | <https://github.com/AnonCatalyst/NmapGuidon> |
| AnonCatalyst/Odinova | api-service | <https://github.com/AnonCatalyst/Odinova> |
| AnonCatalyst/Ominis-OSINT | api-service | <https://github.com/AnonCatalyst/Ominis-OSINT> |
| AnonCatalyst/OpenZenith | framework | <https://github.com/AnonCatalyst/OpenZenith> |
| AnonCatalyst/WebDiver | api-service | <https://github.com/AnonCatalyst/WebDiver> |
| AnonCatalyst/WebHound | api-service | <https://github.com/AnonCatalyst/WebHound> |
| anonymousRAID/OSINT-Mapping-Tool | api-service | <https://github.com/anonymousRAID/OSINT-Mapping-Tool> |
| Answers.com | tool | <https://www.answers.com> |
| antoniaci/blackbird | tool | <https://github.com/antoniaci/blackbird> |
| anurag708989/recon_methodology | tool | <https://github.com/anurag708989/recon_methodology> |
| ANY.RUN | tool | <https://any.run/> |
| AnyeDuke/Enterprise-Security-Skill | tool | <https://github.com/AnyeDuke/Enterprise-Security-Skill> |
| Anzo52/osintbeast | dataset | <https://github.com/Anzo52/osintbeast> |
| Aol | tool | <https://search.aol.com> |
| AP | tool | <http://hosted.ap.org> |
| Ap6pack/outrider-recon | web-platform | <https://github.com/Ap6pack/outrider-recon> |
| Apify | api-service | <https://www.apify.com/?fpr=3nr7v8> |
| Apify's Google Maps Scraper | api-service | <https://apify.com/compass/crawler-google-places> |
| APITube | api-service | <https://apitube.io> |
| Apollo.io | tool | <https://www.apollo.io/> |
| apple-fritter/RTSP.to-webcam | dashboard | <https://github.com/apple-fritter/RTSP.to-webcam> |
| appsec.fyi OSINT Resources | tool | <https://appsec.fyi/osint.html> |
| appsecco/bugcrowd-levelup-subdomain-enumeration | tool | <https://github.com/appsecco/bugcrowd-levelup-subdomain-enumeration> |
| appsecco/spaces-finder | tool | <https://github.com/appsecco/spaces-finder> |
| apurvsinghgautam/dark-web-osint-tools | awesome-list | <https://github.com/apurvsinghgautam/dark-web-osint-tools> |
| apurvsinghgautam/robin | tool | <https://github.com/apurvsinghgautam/robin> |
| Aravindha1234u/Probe_spider | framework | <https://github.com/Aravindha1234u/Probe_spider> |
| Arbor.js | tool | <https://arborjs.org> |
| ARCANGEL0/Mitsu | dashboard | <https://github.com/ARCANGEL0/Mitsu> |
| ArcGIS | research-project | <https://livingatlas.arcgis.com/en/browse/> |
| Archivarix Tube Search | tool | <https://tube.archivarix.net/> |
| Archive.is | tool | <https://archive.is> |
| archive.today | tool | <https://archive.ph/> |
| Arctic Shift | api-service | <https://github.com/ArthurHeitmann/arctic_shift> |
| arcx1/Telegram-OSINT-2022 | awesome-list | <https://github.com/arcx1/Telegram-OSINT-2022> |
| arhaxor21/BruteList | tool | <https://github.com/arhaxor21/BruteList> |
| Arkham Intelligence | tool | <https://www.arkhamintelligence.com/> |
| Armaan29-09-2005/AI-OSINT-Security-Analyzer | plugin | <https://github.com/Armaan29-09-2005/AI-OSINT-Security-Analyzer> |
| arnold117/iOS-NOIR | tool | <https://github.com/arnold117/iOS-NOIR> |
| ArnoSXE/Inversia | tool | <https://github.com/ArnoSXE/Inversia> |
| ARPSyndicate/awesome-intelligence | awesome-list | <https://github.com/ARPSyndicate/awesome-intelligence> |
| arrester/SubSurfer | tool | <https://github.com/arrester/SubSurfer> |
| arxhr007/Aliens_eye | tool | <https://github.com/arxhr007/Aliens_eye> |
| asaotomo/FofaMap | api-service | <https://github.com/asaotomo/FofaMap> |
| ascii2d | tool | <https://ascii2d.net/> |
| asdfgh1445/ctf-super-hub | tool | <https://github.com/asdfgh1445/ctf-super-hub> |
| Ask | tool | <https://www.ask.com> |
| ASpacesys/camera-pose-estimation-from-landmarks | tool | <https://github.com/ASpacesys/camera-pose-estimation-from-landmarks> |
| assafkip/investigators-copilot | plugin | <https://github.com/assafkip/investigators-copilot> |
| assetfinder | tool | <https://github.com/tomnomnom/assetfinder> |
| AtDork | tool | <https://github.com/amnottdevv/atdork> |
| Atennebris/Point-Zero | api-service | <https://github.com/Atennebris/Point-Zero> |
| atenreiro/opensquat | research-project | <https://github.com/atenreiro/opensquat> |
| atiilla/GeoIntel | api-service | <https://github.com/atiilla/GeoIntel> |
| atiilla/gitrecon | api-service | <https://github.com/atiilla/gitrecon> |
| Atlas | research-project | <https://atlas.co> |
| Atlasify | research-project | <http://www.atlasify.com> |
| atmoner/TwitWork | desktop-app | <https://github.com/atmoner/TwitWork> |
| Atom | tool | <https://browser.ru/> |
| atraxsrc/wayback-Urls | tool | <https://github.com/atraxsrc/wayback-Urls> |
| AudienceCue | research-project | <https://audiencecue.com/en/tools/youtube-comment-downloader> |
| Audiense | tool | <https://www.audiense.com> |
| aufzayed/digit | tool | <https://github.com/aufzayed/digit> |
| aufzayed/HydraRecon | tool | <https://github.com/aufzayed/HydraRecon> |
| autocheck.com | tool | <https://autocheck.com/> |
| Autumn-27/ScopeSentry | tool | <https://github.com/Autumn-27/ScopeSentry> |
| AvastrOficial/OsintBsz | api-service | <https://github.com/AvastrOficial/OsintBsz> |
| AVinfoBot | tool | <https://t.me/AVskp_Bot> |
| avtocodbot | tool | <https://t.me/avtocodbot> |
| avtogram_bot | tool | <https://telegram.me/ABTOGRAMBOT> |
| AvtoNomer | tool | <https://t.me/avtonomerbot> |
| Aware-online.com | tool | <https://www.aware-online.com/en/osint-tools> |
| Awasu | tool | <https://www.awasu.com> |
| Awesome Translations list | awesome-list | <https://github.com/mbiesiad/awesome-translations#tools> |
| awesome-crypto-investigation | awesome-list | <https://github.com/edwardtay/awesome-crypto-investigation> |
| awesome-scrapers | awesome-list | <https://github.com/edwardtay/awesome-scrapers> |
| AWS Public Datasets | dataset | <https://aws.amazon.com/datasets> |
| aydinnyunus/exifLooter | tool | <https://github.com/aydinnyunus/exifLooter> |
| AynOps/AynOps | cli-tool | <https://github.com/AynOps/AynOps> |
| ayoubfathi/leaky-paths | api-service | <https://github.com/ayoubfathi/leaky-paths> |
| ayxkaddd/Osint-ToolKit | api-service | <https://github.com/ayxkaddd/Osint-ToolKit> |
| Aziuk/Dorkhunter | plugin | <https://github.com/Aziuk/Dorkhunter> |
| AzizKpln/Gokboru_Intel | tool | <https://github.com/AzizKpln/Gokboru_Intel> |
| Azure Tenant Resolution by PingCastle | research-project | <https://tenantresolution.pingcastle.com> |
| b-satwik/project-chimera-osint-challenge | framework | <https://github.com/b-satwik/project-chimera-osint-challenge> |
| b0dj0x/emailphantom | framework | <https://github.com/b0dj0x/emailphantom> |
| b0dj0x/facetracer | framework | <https://github.com/b0dj0x/facetracer> |
| b0dj0x/userreaper | framework | <https://github.com/b0dj0x/userreaper> |
| b3b0/snipehunt | cli-tool | <https://github.com/b3b0/snipehunt> |
| b3rito/yotter | directory | <https://github.com/b3rito/yotter> |
| b3stp4st3r/manuleye | framework | <https://github.com/b3stp4st3r/manuleye> |
| BackgroundChecks.com | tool | <https://www.backgroundchecks.com> |
| bad-antics/nullsec-pineapple-suite | web-platform | <https://github.com/bad-antics/nullsec-pineapple-suite> |
| badchars/darknet-mcp-server | tool | <https://github.com/badchars/darknet-mcp-server> |
| Bafomet666/OSINT-SAN | api-service | <https://github.com/Bafomet666/OSINT-SAN> |
| Bafomet666/OSINT-SAN-PRO | framework | <https://github.com/Bafomet666/OSINT-SAN-PRO> |
| bagaspra16/find-what | cli-tool | <https://github.com/bagaspra16/find-what> |
| bagaspra16/whos-famous | cli-tool | <https://github.com/bagaspra16/whos-famous> |
| bahricrypto/SNR-Edit | framework | <https://github.com/bahricrypto/SNR-Edit> |
| Baidu (China) | tool | <https://www.baidu.com> |
| Baidu Images | tool | <https://image.baidu.com> |
| Baidu Maps | research-project | <https://map.baidu.com/> |
| bakhirev/assayo | tool | <https://github.com/bakhirev/assayo> |
| balestek/hashtray | tool | <https://github.com/balestek/hashtray> |
| balestek/medor | web-platform | <https://github.com/balestek/medor> |
| banaxou/infonyx | tool | <https://github.com/banaxou/infonyx> |
| Bank for International Settlements Statistics | tool | <https://www.bis.org/statistics/index.htm> |
| Barcode Reader | tool | <https://online-barcode-reader.inliteresearch.com> |
| Barkov.net | tool | <https://vk.barkov.net> |
| Base | tool | <https://www.base-search.net> |
| Batchgeo | research-project | <https://batchgeo.com> |
| batuhaniskr/twitter-intelligence | api-service | <https://github.com/batuhaniskr/twitter-intelligence> |
| BayLak-Egypt/simple-toolkit-for-termux | plugin | <https://github.com/BayLak-Egypt/simple-toolkit-for-termux> |
| bayshier/awesome-osint-arsenal-zh | awesome-list | <https://github.com/bayshier/awesome-osint-arsenal-zh> |
| bayshier/ghosttrack-zh | tool | <https://github.com/bayshier/ghosttrack-zh> |
| BBC News | tool | <https://www.bbc.co.uk/news> |
| BC100Dev/OsintInteractive | web-platform | <https://github.com/BC100Dev/OsintInteractive> |
| be0vlk/lambchop | research-project | <https://github.com/be0vlk/lambchop> |
| Beaker | tool | <http://beakernotebook.com> |
| BeanPaste | tool | <https://beanpaste.fun/> |
| bedros-p/fireblazer | api-service | <https://github.com/bedros-p/fireblazer> |
| BeenVerified | tool | <https://www.backgroundchecks.com/solutions/beenverified> |
| beenverified.com | tool | <https://beenverified.com/> |
| Befunky | tool | <https://www.befunky.com> |
| Bellingcat | tool | <https://www.bellingcat.com/> |
| Bellingcat Online Investigation Toolkit | api-service | <https://bellingcat.gitbook.io/toolkit> |
| Bellingcat Online Researcher Survey: Tool Wishes | research-project | <https://docs.google.com/spreadsheets/d/1vNJRMrlwI7i06diBJtRJWrvt4YuPOqlbUV5o00P_YmE/edit#gid=1378107220> |
| Bellingcat OSM Search | tool | <https://github.com/bellingcat/osm-search> |
| Bellingcat ShadowFinder | tool | <https://github.com/bellingcat/ShadowFinder> |
| Bellingcat's Online Investigation Toolkit | framework | <https://bit.ly/bcattools> |
| Berchez/SteamReveal | api-service | <https://github.com/Berchez/SteamReveal> |
| Berkely Library: Data Lab | library | <http://www.lib.berkeley.edu/libraries/data-lab> |
| bernsteining/instaloctrack | research-project | <https://github.com/bernsteining/instaloctrack> |
| bertotrgopegope/osint-v3 | tool | <https://github.com/bertotrgopegope/osint-v3> |
| beta.companieshouse.gov.uk | tool | <https://beta.companieshouse.gov.uk/> |
| Betaface | tool | <https://www.betaface.com/demo.html> |
| Better Business Bureau | research-project | <https://www.bbb.org> |
| BeVigil | mobile-app | <https://bevigil.com/search> |
| Bevigil/BeVigil-OSINT-CLI | api-service | <https://github.com/Bevigil/BeVigil-OSINT-CLI> |
| Beyond | tool | <https://www.beyond.com> |
| bgoldmann/robin | api-service | <https://github.com/bgoldmann/robin> |
| BGP.he.net | framework | <https://bgp.he.net> |
| BGP.tools | framework | <https://bgp.tools> |
| bgpmap.net | tool | <https://bgpmap.net> |
| Bgpview.io | research-project | <https://bgpview.io> |
| bhavsec/reconspider | framework | <https://github.com/bhavsec/reconspider> |
| Bibsonomy | tool | <https://www.bibsonomy.org> |
| BigBodyCobain/Shadowbroker | tool | <https://github.com/BigBodyCobain/Shadowbroker> |
| bilawalsidhu/gods-eye-view | tool | <https://github.com/bilawalsidhu/gods-eye-view> |
| bincheck.io | tool | <https://bincheck.io/> |
| Bing | tool | <https://www.bing.com> |
| Bing Images | tool | <https://www.bing.com/images> |
| Bing Maps | research-project | <https://www.bing.com/maps> |
| Bing News | tool | <https://www.bing.com/news> |
| Bing Visual Search | tool | <https://www.bing.com/visualsearch> |
| Bing Webmaster Tools | research-project | <https://www.bing.com/toolbox/webmaster> |
| BishopFox/GitGot | api-service | <https://github.com/BishopFox/GitGot> |
| Bitdefender Threat Map | tool | <https://threatmap.bitdefender.com/> |
| Bitquery | directory | <https://bitquery.io> |
| Bitwarden | web-platform | <https://bitwarden.com> |
| Bizeurope | research-project | <http://www.bizeurope.com> |
| Bizint | tool | <https://www.bizint.com> |
| Biznar | tool | <http://biznar.com> |
| BJW333/findpeopleinfo | framework | <https://github.com/BJW333/findpeopleinfo> |
| Bl4ckM1rror/KerberoShutdown | directory | <https://github.com/Bl4ckM1rror/KerberoShutdown> |
| Black Book Online | directory | <https://www.blackbookonline.info> |
| Black-G7/OSINT-X | tool | <https://github.com/Black-G7/OSINT-X> |
| blackarch.org | tool | <https://blackarch.org/> |
| Blackbird | tool | <https://github.com/p1ngul1n0/blackbird> |
| blackhatethicalhacking/AdminPBuster | tool | <https://github.com/blackhatethicalhacking/AdminPBuster> |
| blacklanternsecurity/bbot | framework | <https://github.com/blacklanternsecurity/bbot> |
| blacklanternsecurity/public-dns-servers | tool | <https://github.com/blacklanternsecurity/public-dns-servers> |
| Blacklist Checker | api-service | <https://blacklistchecker.com/> |
| BlackWidow | tool | <https://softbytelabs.com/wp/blackwidow/> |
| blark/aiodnsbrute | tool | <https://github.com/blark/aiodnsbrute> |
| blax-dev/Osint-Navigator-Tool | tool | <https://github.com/blax-dev/Osint-Navigator-Tool> |
| Blockchain.com Explorer | tool | <https://www.blockchain.com/explorer> |
| Blockchair | tool | <https://blockchair.com/> |
| BlogSearchEngine | tool | <http://www.blogsearchengine.org> |
| Bloomberg | research-project | <https://www.bloomberg.com/research/company/overview/overview.asp> |
| blue24bluer/BlueSky | dashboard | <https://github.com/blue24bluer/BlueSky> |
| Bluesky | tool | <https://bsky.app> |
| blueskynet | api-service | <https://github.com/jakecreps/blueskynet> |
| bmi_np_bot | tool | <https://t.me/MNProbot> |
| Boardreader | tool | <https://boardreader.com> |
| bormaxi8080/awesome-books-for-osinters | awesome-list | <https://github.com/bormaxi8080/awesome-books-for-osinters> |
| Bottlenose | tool | <http://bottlenose.com> |
| boxcryptor | tool | <https://www.boxcryptor.com> |
| BP Statistical Review of World Energy | tool | <https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html> |
| bpaste | tool | <https://bpa.st/> |
| Brandwatch | web-platform | <https://www.brandwatch.com> |
| Brave | tool | <https://brave.com> |
| Brave | tool | <https://search.brave.com> |
| BreachDirectory | directory | <https://breachdirectory.org> |
| BreachForums Status | tool | <https://www.breachforums.cx> |
| Breadcrumbs | tool | <https://www.breadcrumbs.app/> |
| BreaGG/DAEDALUS | container | <https://github.com/BreaGG/DAEDALUS> |
| Bridge.Leslibres | tool | <https://bridge.leslibres.org> |
| Bridge.Suumitsu | tool | <https://bridge.suumitsu.eu> |
| Bright Data | api-service | <https://get.brightdata.com/tsf6w05nyw3n> |
| BrightCloud | tool | <https://brightcloud.com/tools/url-ip-lookup.php> |
| BrightCloud Threat Intelligence | dataset | <https://brightcloud.com> |
| Bromite | tool | <https://www.bromite.org/> |
| BrownBook | research-project | <https://www.brownbook.net/> |
| Browserleaks | tool | <https://browserleaks.com/> |
| Browserling | research-project | <https://www.browserling.com> |
| Brute Ratel C4 | tool | <https://bruteratel.com> |
| BscScan | tool | <https://bscscan.com> |
| btc-toolkit | framework | <https://github.com/devdavidejesus/btc-toolkit> |
| BTFM: Blue Team Field Manual | tool | <https://www.amazon.com/dp/154101636X> |
| buanzo/webmon | container | <https://github.com/buanzo/webmon> |
| Bubblemaps | tool | <https://bubblemaps.io> |
| Buffer | tool | <https://buffer.com> |
| BugBountyHunter | tool | <https://www.bugbountyhunter.com> |
| bugourmet/tgsint-bot | api-service | <https://github.com/bugourmet/tgsint-bot> |
| bugourmet/tgsint-scripts | api-service | <https://github.com/bugourmet/tgsint-scripts> |
| Bugs-B0unt3r/rutas-aprendizaje-osint | tool | <https://github.com/Bugs-B0unt3r/rutas-aprendizaje-osint> |
| Built With Flarum | tool | <https://builtwithflarum.com/> |
| BuiltWith | research-project | <https://builtwith.com> |
| BunkerWeb Live Cyber Attack Threat Map | web-platform | <https://threatmap.bunkerweb.io/> |
| Bureau Van Dijk | research-project | <https://www.bvdinfo.com> |
| BuscaPaginasBlancas | tool | <https://github.com/GeiserX/BuscaPaginasBlancas> |
| BushidoUK/Open-source-tools-for-CTI | research-project | <https://github.com/BushidoUK/Open-source-tools-for-CTI> |
| Business Source | research-project | <https://www.ebscohost.com/academic/business-source-complete> |
| Buzz sumo | tool | <https://buzzsumo.com> |
| byt3bl33d3r/WitnessMe | research-project | <https://github.com/byt3bl33d3r/WitnessMe> |
| C0MPL3XDEV/E4GL30S1NT | framework | <https://github.com/C0MPL3XDEV/E4GL30S1NT> |
| C3EQUALZz/TeleOSinter | tool | <https://github.com/C3EQUALZz/TeleOSinter> |
| C3n7ral051nt4g3ncy/cURL_for_OSINT | tool | <https://github.com/C3n7ral051nt4g3ncy/cURL_for_OSINT> |
| C3n7ral051nt4g3ncy/GitOSINT_Bot | research-project | <https://github.com/C3n7ral051nt4g3ncy/GitOSINT_Bot> |
| C3n7ral051nt4g3ncy/HandleHawk | web-platform | <https://github.com/C3n7ral051nt4g3ncy/HandleHawk> |
| C3n7ral051nt4g3ncy/Masto | api-service | <https://github.com/C3n7ral051nt4g3ncy/Masto> |
| C3n7ral051nt4g3ncy/OSINT_Inception-links | tool | <https://github.com/C3n7ral051nt4g3ncy/OSINT_Inception-links> |
| C3n7ral051nt4g3ncy/WebOSINT | api-service | <https://github.com/C3n7ral051nt4g3ncy/WebOSINT> |
| c4seus/lacis | tool | <https://github.com/c4seus/lacis> |
| CachedView | tool | <https://cachedview.com> |
| Cacoo | tool | <https://cacoo.com> |
| caetano-dev/OSINT-guide | dashboard | <https://github.com/caetano-dev/OSINT-guide> |
| calesthio/Crucix | tool | <https://github.com/calesthio/Crucix> |
| California Justice Watch | api-service | <https://cajusticewatch.com> |
| calinux-py/GitHub-OSINT | browser-extension | <https://github.com/calinux-py/GitHub-OSINT> |
| CallerID Test | research-project | <https://calleridtest.com/> |
| CampusCareerCenter | tool | <https://www.campuscareercenter.com> |
| Canada411 | tool | <https://www.canada411.ca> |
| Canadian Business Research | research-project | <https://www.canada.ca/en/services/business/research.html> |
| canarytokens.org | tool | <https://canarytokens.org/> |
| CanLaw | tool | <http://www.canlaw.com> |
| Canva | tool | <https://www.canva.com> |
| capitol-cli | api-service | <https://github.com/NPCmillionaire/capitol-cli> |
| Cappricio-Securities/ghostrecon | tool | <https://github.com/Cappricio-Securities/ghostrecon> |
| Captin Fact | tool | <https://captainfact.io/> |
| capture0x/Resonant | framework | <https://github.com/capture0x/Resonant> |
| CareerBuilder | tool | <https://www.careerbuilder.com> |
| carlosbarrosovieira/osint-scanner | web-platform | <https://github.com/carlosbarrosovieira/osint-scanner> |
| carlospolop/bashReconScan | tool | <https://github.com/carlospolop/bashReconScan> |
| Carrot2 | tool | <https://search.carrot2.org> |
| CartoDB | research-project | <https://cartodb.com> |
| Caselaw Access Project | research-project | <https://case.law/> |
| CashedPages | tool | <http://www.cachedpages.com> |
| caster0x00/Above | tool | <https://github.com/caster0x00/Above> |
| Castrick | tool | <https://castrickclues.com> |
| CC.LA | library | <https://cc.la> |
| CCleaner | tool | <https://www.piriform.com/ccleaner> |
| ccreater222/slime | tool | <https://github.com/ccreater222/slime> |
| CCTV | plugin | <https://github.com/IvanGlinkin/CCTV> |
| cdua-org/ReconSR | framework | <https://github.com/cdua-org/ReconSR> |
| CellEight/subsurface | tool | <https://github.com/CellEight/subsurface> |
| Censys | tool | <https://search.censys.io/> |
| censys/censys-recon-ng | plugin | <https://github.com/censys/censys-recon-ng> |
| CentBrowser | tool | <https://www.centbrowser.com> |
| Center for International Earth Science Information Network | tool | <http://www.ciesin.org> |
| CentOS Pastebin Service | web-platform | <https://paste.centos.org/> |
| Central Ops | research-project | <https://centralops.net> |
| CEPII | tool | <https://www.cepii.fr/CEPII/en/welcome.asp> |
| Cerast Intelligence | research-project | <https://search.cerast-intelligence.com/> |
| CertKit Certificate Search | tool | <https://www.certkit.io/tools/ct-logs/> |
| Cgboal/SonarSearch | api-service | <https://github.com/Cgboal/SonarSearch> |
| chadi0x/TheBigBrother | web-platform | <https://github.com/chadi0x/TheBigBrother> |
| Chainabuse | dataset | <https://www.chainabuse.com/> |
| Chainalysis Reactor | web-platform | <https://www.chainalysis.com/product/reactor/> |
| chainreactors/gogo | plugin | <https://github.com/chainreactors/gogo> |
| champmq/GoogleFU | tool | <https://github.com/champmq/GoogleFU> |
| champmq/TheScrapper | api-service | <https://github.com/champmq/TheScrapper> |
| ChangeDetect | tool | <http://www.changedetect.com> |
| ChangeDetection | tool | <https://www.changedetection.com> |
| ChangeDetection.io | tool | <https://changedetection.io> |
| ChangeDetection.io Open Source | tool | <https://github.com/dgtlmoon/changedetection.io> |
| chaos-client | dataset | <https://github.com/projectdiscovery/chaos-client> |
| charliebrassington/one | framework | <https://github.com/charliebrassington/one> |
| Chart.js | library | <https://www.chartjs.org> |
| chartblocks | tool | <https://www.chartblocks.com> |
| chat.deepseek.com | research-project | <https://chat.deepseek.com/> |
| chat.openai.com | research-project | <https://chat.openai.com/> |
| ChatSearchRobot | tool | <https://t.me/ChatSearchRobot> |
| Chatsecure | tool | <https://chatsecure.org> |
| Check | tool | <https://meedan.com/check> |
| CheckLeaked | api-service | <https://checkleaked.cc/> |
| CheckUser | tool | <https://checkuser.vercel.app/> |
| checkusernames.com | web-platform | <https://checkusernames.com/> |
| chetstriker/LLMtary | web-platform | <https://github.com/chetstriker/LLMtary> |
| chiasmod0n/chiasmodon | framework | <https://github.com/chiasmod0n/chiasmodon> |
| choirurrizal/paraminer | tool | <https://github.com/choirurrizal/paraminer> |
| chqdo/disclosure | framework | <https://github.com/chqdo/disclosure> |
| chrismaddalena/ODIN | directory | <https://github.com/chrismaddalena/ODIN> |
| christophetd/censys-subdomain-finder | tool | <https://github.com/christophetd/censys-subdomain-finder> |
| Chrome | tool | <https://www.google.com/chrome> |
| ChronoVerify | api-service | <https://chronoverify.com> |
| ChuckNorr1s/cdn-cracker | tool | <https://github.com/ChuckNorr1s/cdn-cracker> |
| CIA World Factbook | tool | <https://www.cia.gov/library/publications/the-world-factbook> |
| CIA World Factbook | tool | <https://www.cia.gov/the-world-factbook/> |
| cia.gov/readingroom | web-platform | <https://www.cia.gov/readingroom> |
| ciber-int-osint/OsintLatam | framework | <https://github.com/ciber-int-osint/OsintLatam> |
| Cielo | tool | <https://cielo.finance> |
| cipher387/API-s-for-OSINT | awesome-list | <https://github.com/cipher387/API-s-for-OSINT> |
| cipher387/cheatsheets | tool | <https://github.com/cipher387/cheatsheets> |
| cipher387/Dorks-collections-list | awesome-list | <https://github.com/cipher387/Dorks-collections-list> |
| cipher387/linux-for-OSINT-21-day | cli-tool | <https://github.com/cipher387/linux-for-OSINT-21-day> |
| cipher387/osint_stuff_tool_collection | awesome-list | <https://github.com/cipher387/osint_stuff_tool_collection> |
| cipher387/osintmap | web-platform | <https://github.com/cipher387/osintmap> |
| Cipherstick | tool | <https://cipherstick.tech> |
| CIRCL Hashlookup | tool | <https://www.circl.lu/services/hashlookup> |
| Circos | tool | <http://circos.ca> |
| Cisco Talos Intelligence | tool | <https://talosintelligence.com/ebc_spam> |
| Cisco Talos Intelligence | tool | <https://talosintelligence.com/reputation_center> |
| CiteSeerX | tool | <http://citeseer.ist.psu.edu> |
| cl1p | cli-tool | <https://Cl1p.net> |
| Clarify | tool | <https://clarify.io> |
| clarketm/s3recon | tool | <https://github.com/clarketm/s3recon> |
| Classmates | tool | <https://www.classmates.com> |
| Clats97/ClatScope | tool | <https://github.com/Clats97/ClatScope> |
| claude.ai | research-project | <https://claude.ai/> |
| Clearbit Connect | browser-extension | <https://connect.clearbit.com> |
| ClerkBot | tool | <https://t.me/clerksecretbot> |
| Clip Blast | cli-tool | <http://www.clipblast.com> |
| CloudBrute | tool | <https://github.com/0xsha/CloudBrute> |
| Cloudflare Radar | tool | <https://radar.cloudflare.com> |
| cloudlist | api-service | <https://github.com/projectdiscovery/cloudlist> |
| cloudtracer/ThreatPinchLookup | plugin | <https://github.com/cloudtracer/ThreatPinchLookup> |
| clouedoc/AutoSQLi | research-project | <https://github.com/clouedoc/AutoSQLi> |
| Clustermaps | tool | <https://clustrmaps.com/> |
| CNN | tool | <https://edition.cnn.com> |
| Cobalt Strike | framework | <https://www.cobaltstrike.com> |
| Code Finder | tool | <https://codefinder.dev/> |
| cognis-digital/awesome-drone-warfare-osint | awesome-list | <https://github.com/cognis-digital/awesome-drone-warfare-osint> |
| coldvisionz/osint-investigation | framework | <https://github.com/coldvisionz/osint-investigation> |
| College Recruiter | tool | <https://www.collegerecruiter.com> |
| Colorbrewer | research-project | <https://colorbrewer2.org> |
| Columbus Project | api-service | <https://github.com/elmasy-com/columbus> |
| com.lullar.com | tool | <https://com.lullar.com/> |
| Commander Search | tool | <https://www.commandersearch.com> |
| commie | tool | <https://commie.io/> |
| Comodo Dragon | tool | <https://www.comodo.com/home/browsers-toolbars/browser.php> |
| Company Registration Round the World | research-project | <https://www.commercial-register.sg.ch/home/worldwide.html> |
| Company Research Resources by Country Comparably | research-project | <https://www.comparably.com> |
| CompeteShark | research-project | <https://competeshark.com> |
| CompreFace | container | <https://github.com/exadel-inc/CompreFace> |
| conflict-investigations/liveuamap-analysis | api-service | <https://github.com/conflict-investigations/liveuamap-analysis> |
| conflict-investigations/media-search-engine | api-service | <https://github.com/conflict-investigations/media-search-engine> |
| conflict-investigations/nzz-maps | api-service | <https://github.com/conflict-investigations/nzz-maps> |
| Constella Intelligence | tool | <https://constellaintelligence.com> |
| ContactOut | tool | <https://contactout.com/> |
| Context | tool | <https://ctxt.io/> |
| ControlC Pastebin | tool | <https://Controlc.com> |
| Coowon | tool | <https://coowon.com> |
| Copernicus Browser | tool | <https://browser.dataspace.copernicus.eu/> |
| copilot.microsoft.com | plugin | <https://copilot.microsoft.com/> |
| Core | tool | <https://core.ac.uk/search> |
| core-val/webscout | web-platform | <https://github.com/core-val/webscout> |
| corndoctor626/steam-probiv | framework | <https://github.com/corndoctor626/steam-probiv> |
| Corporate Information | research-project | <https://www.corporateinformation.com> |
| CorporationWiki | research-project | <https://www.corporationwiki.com/> |
| cosad3s/hfinder | tool | <https://github.com/cosad3s/hfinder> |
| cosad3s/njsdump | tool | <https://github.com/cosad3s/njsdump> |
| cosad3s/postleaks | library | <https://github.com/cosad3s/postleaks> |
| CourtListener | tool | <https://www.courtlistener.com/> |
| cr0mll/cyberclopaedia | tool | <https://github.com/cr0mll/cyberclopaedia> |
| Craiglist | tool | <https://losangeles.craigslist.org> |
| CrawlGraph | research-project | <https://crawlgraph.com> |
| creately | tool | <https://creately.com> |
| creationdatebot | tool | <https://t.me/creationdatebot> |
| Creative Commons Attribution-ShareAlike 4.0 International | tool | <https://creativecommons.org/licenses/by-sa/4.0/> |
| Creepy | tool | <https://github.com/ilektrojohn/creepy> |
| Crime Brasil | api-service | <https://crimebrasil.com.br> |
| Criminal IP | web-platform | <https://www.criminalip.io/> |
| criminalip.io/developer | api-service | <https://www.criminalip.io/developer> |
| Crossfilter | tool | <https://square.github.io/crossfilter> |
| CrowdMap | research-project | <https://crowdmap.com> |
| CrowdStrike Falcon Intelligence | web-platform | <https://www.crowdstrike.com/products/threat-intelligence/> |
| CRT Certificate Search | tool | <https://crt.sh> |
| CrunchBase | dataset | <https://www.crunchbase.com> |
| CryptoBot | tool | <https://t.me/CryptoBot> |
| cryptome.org | web-platform | <https://cryptome.org/> |
| Crystal Intelligence | tool | <https://crystalintelligence.com> |
| CScorza/OSINT-FORENSICS-MOBILE | tool | <https://github.com/CScorza/OSINT-FORENSICS-MOBILE> |
| CScorza/OSINTAnonymous | tool | <https://github.com/CScorza/OSINTAnonymous> |
| CScorza/OSINTInvestigation | tool | <https://github.com/CScorza/OSINTInvestigation> |
| cspshivam/easyrecon | tool | <https://github.com/cspshivam/easyrecon> |
| csvkit | tool | <https://github.com/wireservice/csvkit> |
| CTFR | tool | <https://github.com/UnaPibaGeek/ctfr> |
| CTLRQ Address Lookup | research-project | <https://ctrlq.org/maps/address> |
| Cupidcr4wl | web-platform | <https://github.com/OSINTI4L/cupidcr4wl> |
| Cutapaste | tool | <https://cutapaste.net/> |
| cve-search/git-vuln-finder | tool | <https://github.com/cve-search/git-vuln-finder> |
| CVFox | tool | <http://www.cvfox.com> |
| Cyb3rtch/Cyb3rtech-Tool | framework | <https://github.com/Cyb3rtch/Cyb3rtech-Tool> |
| Cyber Alert | tool | <http://www.cyberalert.com> |
| Cyber-Courses/Cyber-Library | library | <https://github.com/Cyber-Courses/Cyber-Library> |
| Cyber-Dioxide/IP_Rover | tool | <https://github.com/Cyber-Dioxide/IP_Rover> |
| Cyber-note/Full-Bug-Bounty-Hunting-Methodology-2026 | tool | <https://github.com/Cyber-note/Full-Bug-Bounty-Hunting-Methodology-2026> |
| cybercdh/kitphishr | tool | <https://github.com/cybercdh/kitphishr> |
| CyberDemon73/DorkSide | api-service | <https://github.com/CyberDemon73/DorkSide> |
| CyberGordon | tool | <https://cybergordon.com> |
| CyberIntelligenceLab/CTI-House | research-project | <https://github.com/CyberIntelligenceLab/CTI-House> |
| CyberLegionnaire/OSINT_Tools | tool | <https://github.com/CyberLegionnaire/OSINT_Tools> |
| cyberninja-69/osinter | plugin | <https://github.com/cyberninja-69/osinter> |
| cybersecurity-dev/awesome-open-source-intelligence | awesome-list | <https://github.com/cybersecurity-dev/awesome-open-source-intelligence> |
| Cybersight-Security/OSINT-Toolkit | directory | <https://github.com/Cybersight-Security/OSINT-Toolkit> |
| cybervault-team/vosint | tool | <https://github.com/cybervault-team/vosint> |
| Cybrary | tool | <https://www.cybrary.it> |
| cyh-skill/field-graph | research-project | <https://github.com/cyh-skill/field-graph> |
| Cyotek WebCopy | tool | <https://www.cyotek.com/cyotek-webcopy> |
| Cyreslab-AI/shodan-mcp-server | tool | <https://github.com/Cyreslab-AI/shodan-mcp-server> |
| d-Rickyy-b/certstream-server-go | cli-tool | <https://github.com/d-Rickyy-b/certstream-server-go> |
| D3Ext/go-recon | framework | <https://github.com/D3Ext/go-recon> |
| D3js | library | <https://d3js.org> |
| d3mondev/puredns | tool | <https://github.com/d3mondev/puredns> |
| d3xm0s/Reconx | tool | <https://github.com/d3xm0s/Reconx> |
| daehee/govcloud | tool | <https://github.com/daehee/govcloud> |
| DailyEarth | tool | <https://dailyearth.com> |
| DailyMotion | tool | <https://www.dailymotion.com> |
| Dalistin/biometrics-osint | tool | <https://github.com/Dalistin/biometrics-osint> |
| Dalistin/HowToFind-free | tool | <https://github.com/Dalistin/HowToFind-free> |
| Dalistin/insta-osint | tool | <https://github.com/Dalistin/insta-osint> |
| Dalistin/steam-osint | tool | <https://github.com/Dalistin/steam-osint> |
| Dalistin/VK-OSINT | tool | <https://github.com/Dalistin/VK-OSINT> |
| dalunacrobate/BioIG | plugin | <https://github.com/dalunacrobate/BioIG> |
| dalunacrobate/DaProfiler | tool | <https://github.com/dalunacrobate/DaProfiler> |
| danieldurnea/FBI-tools | awesome-list | <https://github.com/danieldurnea/FBI-tools> |
| dankertea51-cpu/Sled | api-service | <https://github.com/dankertea51-cpu/Sled> |
| Danush-Aries/reconweave | web-platform | <https://github.com/Danush-Aries/reconweave> |
| daprofiler/DaProfiler | research-project | <https://github.com/daprofiler/DaProfiler> |
| darama22/Malware-Research-Hub | directory | <https://github.com/darama22/Malware-Research-Hub> |
| Darkdump | tool | <https://github.com/josh0xA/darkdump> |
| Darkelf-Labs/Darkelf-OSINT-Ai | research-project | <https://github.com/Darkelf-Labs/Darkelf-OSINT-Ai> |
| Darksight-Analytics/tgspyder | api-service | <https://github.com/Darksight-Analytics/tgspyder> |
| Data Visualization Catalogue | directory | <https://datavizcatalogue.com> |
| Data.com Connect | research-project | <https://connect.data.com> |
| Data.gov.uk | tool | <https://data.gov.uk> |
| DataForSEO | api-service | <https://dataforseo.com/?aff=255379> |
| DataInt Databook | api-service | <https://databook.dataint.net> |
| Datalux/Osintgram | api-service | <https://github.com/Datalux/Osintgram> |
| Datasploit | tool | <https://github.com/DataSploit/datasploit> |
| Datawrapper | tool | <https://datawrapper.de> |
| datXpert | tool | <https://telegram.me/datxpertbot> |
| daudmalik06/ReconCat | tool | <https://github.com/daudmalik06/ReconCat> |
| daudmalik06/WMB-Scrapper | tool | <https://github.com/daudmalik06/WMB-Scrapper> |
| Daum (South Korea) | tool | <https://www.daum.net/> |
| davidleonstr/osint-console | tool | <https://github.com/davidleonstr/osint-console> |
| DBPedia | tool | <https://wiki.dbpedia.org> |
| DBpedia | tool | <https://www.dbpedia.org> |
| dCallsBot | tool | <https://t.me/dCallsBot> |
| ddosecrets.com | web-platform | <https://ddosecrets.com/> |
| de digger | tool | <https://www.dedigger.com/> |
| Dedicated or Not | research-project | <https://dedicatedornot.com> |
| dedsec1121fk/DedSec | tool | <https://github.com/dedsec1121fk/DedSec> |
| DedSecInside/gotor | container | <https://github.com/DedSecInside/gotor> |
| deebong/OSINT-KYC-Link-Mapper | dashboard | <https://github.com/deebong/OSINT-KYC-Link-Mapper> |
| DeepFace | framework | <https://github.com/serengil/deepface> |
| Defuse | tool | <https://defuse.ca/pastebin.htm> |
| DeHashed | tool | <https://dehashed.com/> |
| Dehashed CLI | api-service | <https://github.com/hmaverickadams/DeHashed-API-Tool> |
| dehashed.com/docs | api-service | <https://dehashed.com/docs> |
| Deltafeed | dataset | <https://bitreading.com/deltafeed> |
| demo.f4map.com | tool | <https://demo.f4map.com/> |
| DEMON1A/zzl | tool | <https://github.com/DEMON1A/zzl> |
| deniss-eh/OSINT_RESOURCES | tool | <https://github.com/deniss-eh/OSINT_RESOURCES> |
| DenizShabani/telegramscraper | api-service | <https://github.com/DenizShabani/telegramscraper> |
| Denoroy737/Telegram_OSINT | tool | <https://github.com/Denoroy737/Telegram_OSINT> |
| Descartes Labs | research-project | <https://maps.descarteslabs.com/> |
| DescobertasDigitais/Maya | api-service | <https://github.com/DescobertasDigitais/Maya> |
| desirelovellcom/OSINT | tool | <https://github.com/desirelovellcom/OSINT> |
| det0xgravity/truebearing-osint | dashboard | <https://github.com/det0xgravity/truebearing-osint> |
| Detectiva | tool | <https://detectiva.link/rezervBot> |
| Deturl | tool | <https://deturl.com> |
| Dev2023-Op/awesome-opsec | awesome-list | <https://github.com/Dev2023-Op/awesome-opsec> |
| Devang-Solanki/recon.cloud | api-service | <https://github.com/Devang-Solanki/recon.cloud> |
| devanshbatham/FavFreak | tool | <https://github.com/devanshbatham/FavFreak> |
| devanshbatham/Gorecon | directory | <https://github.com/devanshbatham/Gorecon> |
| devanshbatham/ParamSpider | tool | <https://github.com/devanshbatham/ParamSpider> |
| developer.shodan.io | api-service | <https://developer.shodan.io/> |
| developers.google.com/custom-search | api-service | <https://developers.google.com/custom-search> |
| developers.virustotal.com | api-service | <https://developers.virustotal.com/> |
| devploit/geminiHunter | mobile-app | <https://github.com/devploit/geminiHunter> |
| DevVj-1/Hacking-Social_Media-Accounts | tool | <https://github.com/DevVj-1/Hacking-Social_Media-Accounts> |
| devxprite/infoooze | tool | <https://github.com/devxprite/infoooze> |
| DFW1N/DFW1N-OSINT | awesome-list | <https://github.com/DFW1N/DFW1N-OSINT> |
| Dheerajmadhukar/karma_v2 | framework | <https://github.com/Dheerajmadhukar/karma_v2> |
| dheerajydv19/Social-Media-Osint | tool | <https://github.com/dheerajydv19/Social-Media-Osint> |
| dhn/spk | tool | <https://github.com/dhn/spk> |
| dhn/udon | tool | <https://github.com/dhn/udon> |
| Dice | tool | <https://www.dice.com> |
| DiffChecker | tool | <https://www.diffchecker.com/image-diff/> |
| digga | framework | <https://digga.dev> |
| DiggReader | tool | <https://digg.com/login?next=%2Freader> |
| digiKam | research-project | <https://www.digikam.org/> |
| Digital Footprint Check | tool | <https://www.digitalfootprintcheck.com/free-checker.html> |
| digital-forensics.sans.org | tool | <https://digital-forensics.sans.org/> |
| digitaldisarray/OSINT-Tools | tool | <https://github.com/digitaldisarray/OSINT-Tools> |
| Dimaslg/osintBOX | framework | <https://github.com/Dimaslg/osintBOX> |
| dimondevceo/glazboga | tool | <https://github.com/dimondevceo/glazboga> |
| dincertekin/mailogle | tool | <https://github.com/dincertekin/mailogle> |
| dirsoooo/Recon | tool | <https://github.com/dirsoooo/Recon> |
| Disconnect | tool | <https://disconnect.me> |
| Discord Lookup | tool | <https://discordlookup.com> |
| Discord Sensor | tool | <https://telegram.me/discordsensorbot> |
| DiscordChatExporter | tool | <https://github.com/Tyrrrz/DiscordChatExporter> |
| DiscordHistory | tool | <https://disboard.org> |
| DiscordOSINT | tool | <https://github.com/husseinmuhaisen/DiscordOSINT> |
| Discoshell | cli-tool | <https://github.com/foozzi/discoshell> |
| Distill Web Monitor | browser-extension | <https://distill.io/> |
| divinelabio/Argus | directory | <https://github.com/divinelabio/Argus> |
| diyari-mussa/Caller-OSINT | tool | <https://github.com/diyari-mussa/Caller-OSINT> |
| djirtou/aether-osint | tool | <https://github.com/djirtou/aether-osint> |
| dmytrokurochkin/Easy-Osint-Bot | research-project | <https://github.com/dmytrokurochkin/Easy-Osint-Bot> |
| DNS History | research-project | <https://completedns.com/dns-history/> |
| DNS History | tool | <https://dnshistory.org> |
| DNSai | research-project | <https://dnsai.com/dns-tools/> |
| DNSDumpster | research-project | <https://dnsdumpster.com> |
| dnsrecon | tool | <https://github.com/darkoperator/dnsrecon> |
| DNSservices | web-platform | <https://github.com/0x4f53/dnsservices> |
| DNSStuff | research-project | <https://www.dnsstuff.com> |
| DNSViz | research-project | <https://dnsviz.net> |
| dnsx | framework | <https://github.com/projectdiscovery/dnsx> |
| Do Not Track | tool | <http://donottrack.us> |
| Doble-2/osint-d2 | api-service | <https://github.com/Doble-2/osint-d2> |
| DocumentCloud | web-platform | <https://www.documentcloud.org> |
| dokDork/SiteSniper | tool | <https://github.com/dokDork/SiteSniper> |
| Dolphin Radar | tool | <https://www.dolphinradar.com/web-viewer-for-instagram> |
| Domain Crawler | research-project | <https://www.domaincrawler.com> |
| Domain Dossier | research-project | <https://centralops.net/co/DomainDossier.aspx> |
| Domain Hunter | api-service | <https://github.com/WhiteBite/Domain-Hunter> |
| Domain Intelligence | research-project | <https://oti-labs.com/domain-intelligence-api> |
| Domain Tools | research-project | <https://whois.domaintools.com> |
| DomainEye Reverse WHOIS | tool | <https://domaineye.com/reverse-whois> |
| DomainRecon | research-project | <https://kriztalz.sh/domain-recon/> |
| Dominoc925 | research-project | <https://dominoc925-pages.appspot.com/mapplets/cs_mgrs.html> |
| dootss/shodan-dorks | tool | <https://github.com/dootss/shodan-dorks> |
| DorkCraft | tool | <https://github.com/juandresrodca/DorkCraft> |
| DorkGenius | tool | <https://dorkgenius.com/> |
| DorkGPT | tool | <https://www.dorkgpt.com/> |
| DorkSearch | library | <https://dorksearch.com/> |
| Dorky | tool | <https://dorky.io> |
| DownloadHelper | tool | <https://www.downloadhelper.net> |
| doxbin | tool | <https://doxbin.net/> |
| doxcord | tool | <https://github.com/boringthegod/doxcord> |
| DPA International | tool | <https://www.dpa-international.com> |
| dpaste | tool | <https://Dpaste.com> |
| dpaste2 | tool | <https://Dpaste.org> |
| Dra-Ganzz/Premium-Call | cli-tool | <https://github.com/Dra-Ganzz/Premium-Call> |
| Dragkob/A1NT | web-platform | <https://github.com/Dragkob/A1NT> |
| Draugiem (Latvia) | tool | <https://www.draugiem.lv> |
| Drew-Alleman/DataSurgeon | tool | <https://github.com/Drew-Alleman/DataSurgeon> |
| drooling/email-osint | tool | <https://github.com/drooling/email-osint> |
| drooling/phosint | tool | <https://github.com/drooling/phosint> |
| Dropmark | tool | <https://www.dropmark.com> |
| DrowLink/osint-toolkit | web-platform | <https://github.com/DrowLink/osint-toolkit> |
| DrW3b/enumax | tool | <https://github.com/DrW3b/enumax> |
| DualMaps | research-project | <https://www.mapchannels.com/dualmaps7/map.htm> |
| DuckDuckGo URL scraper | tool | <https://github.com/its0x08/duckduckgo> |
| dump1090 | tool | <https://github.com/flightaware/dump1090> |
| Dune Analytics | dashboard | <https://dune.com> |
| Dupli Checker | tool | <https://www.duplichecker.com/reverse-image-search.php> |
| dygraphs | tool | <https://dygraphs.com> |
| dzidulajubilee/OmenWatch | api-service | <https://github.com/dzidulajubilee/OmenWatch> |
| e-m3din4/deep-hlr | api-service | <https://github.com/e-m3din4/deep-hlr> |
| e-m3din4/osintxphone | api-service | <https://github.com/e-m3din4/osintxphone> |
| Earthcam | tool | <https://www.earthcam.com> |
| easely | tool | <https://www.easel.ly> |
| Easy whois | research-project | <https://www.easywhois.com> |
| EasyVIN | tool | <https://t.me/EasyVINbot> |
| ecstatic-nobel/OSweep | tool | <https://github.com/ecstatic-nobel/OSweep> |
| EDGAR U.S. Securities and Exchange Commission Filings | research-project | <https://www.edgar-online.com> |
| Edge | tool | <https://www.microsoft.com/en-us/windows/microsoft-edge/microsoft-edge> |
| Edi-San24/OSINT-Pivot-Engine | tool | <https://github.com/Edi-San24/OSINT-Pivot-Engine> |
| edoardogerosa/pockint | dashboard | <https://github.com/edoardogerosa/pockint> |
| edoardottt/cariddi | plugin | <https://github.com/edoardottt/cariddi> |
| edoardottt/csprecon | tool | <https://github.com/edoardottt/csprecon> |
| edoardottt/favirecon | web-platform | <https://github.com/edoardottt/favirecon> |
| edoardottt/scilla | tool | <https://github.com/edoardottt/scilla> |
| EdOverflow/contact.sh | tool | <https://github.com/EdOverflow/contact.sh> |
| EdOverflow/megplus | research-project | <https://github.com/EdOverflow/megplus> |
| edwardtay/awesome-OSINT | awesome-list | <https://github.com/edwardtay/awesome-OSINT> |
| ef1500/Elastichunt | dataset | <https://github.com/ef1500/Elastichunt> |
| egnake/LeakRecon | api-service | <https://github.com/egnake/LeakRecon> |
| egnake/Ohsint-Framework | directory | <https://github.com/egnake/Ohsint-Framework> |
| egrul_bot | tool | <https://t.me/egrul_bot> |
| eHow | tool | <https://www.ehow.com> |
| ehsahil/recon-my-way | tool | <https://github.com/ehsahil/recon-my-way> |
| eInvestigator | tool | <https://www.einvestigator.com/> |
| Ekultek/GitRekt | tool | <https://github.com/Ekultek/GitRekt> |
| Ekultek/WhatBreach | dataset | <https://github.com/Ekultek/WhatBreach> |
| Ekultek/Zeus-Scanner | tool | <https://github.com/Ekultek/Zeus-Scanner> |
| elblaxican/Tankvill-OSINT-Photo-Hunter | api-service | <https://github.com/elblaxican/Tankvill-OSINT-Photo-Hunter> |
| elbraino/awesome-blackhat-arsenal | awesome-list | <https://github.com/elbraino/awesome-blackhat-arsenal> |
| elceef/dnstwist | tool | <https://github.com/elceef/dnstwist> |
| elfarsaouiomar/monitor-new-subdomain | api-service | <https://github.com/elfarsaouiomar/monitor-new-subdomain> |
| eliasgranderubio/cartuxeira | web-platform | <https://github.com/eliasgranderubio/cartuxeira> |
| Elite-Security-Systems/radar | api-service | <https://github.com/Elite-Security-Systems/radar> |
| Elliptic | tool | <https://www.elliptic.co> |
| elm1nst3r/GHOST-osint-crm | web-platform | <https://github.com/elm1nst3r/GHOST-osint-crm> |
| Elsevier | tool | <https://www.elsevier.com> |
| Eluta (Canada) | tool | <https://www.eluta.ca> |
| Email Address Validator | tool | <https://www.email-validator.net> |
| Email Extractor | tool | <https://99tools.net/email-extractor/> |
| Email Format | tool | <https://email-format.com> |
| Email Permutator | tool | <https://www.polished.app/email-permutator/> |
| email-checker.net | tool | <https://email-checker.net/> |
| EmailHippo | web-platform | <https://tools.verifyemailaddress.io> |
| EmailRep | web-platform | <https://emailrep.io> |
| Emergent | tool | <https://www.emergent.info> |
| EmobileTracker.com | web-platform | <https://www.emobiletracker.com/> |
| emppu-dev/HakuHaukka | framework | <https://github.com/emppu-dev/HakuHaukka> |
| emrekybs/OsintCase | framework | <https://github.com/emrekybs/OsintCase> |
| emrekybs/Pip-Intel | tool | <https://github.com/emrekybs/Pip-Intel> |
| emrekybs/SOCMIntelligence | framework | <https://github.com/emrekybs/SOCMIntelligence> |
| emrekybs/tgsherlock | framework | <https://github.com/emrekybs/tgsherlock> |
| emrekybs/veiled-eye | framework | <https://github.com/emrekybs/veiled-eye> |
| EncSF MP | tool | <https://encfsmp.sourceforge.net> |
| EndlessFractal/WHOIScope | tool | <https://github.com/EndlessFractal/WHOIScope> |
| engineer1469/WifiSeeker | tool | <https://github.com/engineer1469/WifiSeeker> |
| Eniro (Sweden) | tool | <https://www.eniro.se> |
| epi052/recon-pipeline | tool | <https://github.com/epi052/recon-pipeline> |
| Epic Privacy Browser | tool | <https://www.epicbrowser.com> |
| EpicVIN | research-project | <https://epicvin.com/> |
| Epieos | tool | <https://epieos.com> |
| Epieos Tools | tool | <https://tools.epieos.com> |
| Epstein Exposed | dataset | <https://epsteinexposed.com> |
| Equasis | dataset | <https://www.equasis.org/> |
| er4vn/i-Detector | tool | <https://github.com/er4vn/i-Detector> |
| er4vn/TeleStrike | tool | <https://github.com/er4vn/TeleStrike> |
| Eraser | tool | <https://eraser.heidi.ie> |
| eremit4/favihunter | tool | <https://github.com/eremit4/favihunter> |
| erkanrzgc/open-source-intelligence | web-platform | <https://github.com/erkanrzgc/open-source-intelligence> |
| Escape-Technologies/awesome-attack-surface-management | awesome-list | <https://github.com/Escape-Technologies/awesome-attack-surface-management> |
| Escape-Technologies/graphinder | api-service | <https://github.com/Escape-Technologies/graphinder> |
| eschultze/URLextractor | tool | <https://github.com/eschultze/URLextractor> |
| eslam3kl/3klCon | framework | <https://github.com/eslam3kl/3klCon> |
| Esri | research-project | <https://www.esri.com> |
| estebanpdl/osintgpt | tool | <https://github.com/estebanpdl/osintgpt> |
| estebanpdl/telegram-tracker | api-service | <https://github.com/estebanpdl/telegram-tracker> |
| eth0izzle/shhgit | api-service | <https://github.com/eth0izzle/shhgit> |
| eth0izzle/the-endorser | tool | <https://github.com/eth0izzle/the-endorser> |
| Etherscan | tool | <https://etherscan.io/> |
| ethiack/ai4eh | tool | <https://github.com/ethiack/ai4eh> |
| Etools | tool | <https://www.etools.ch> |
| Etusivu | tool | <https://pastebin.fi/> |
| EU BRIS | web-platform | <https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-search-company-eu_en> |
| Eurojobs | tool | <https://www.eurojobs.com> |
| Euronews | tool | <https://www.euronews.com> |
| Europages | research-project | <https://www.europages.co.uk> |
| European Business Register | research-project | <http://www.ebr.org> |
| European Union Open Data Portal | web-platform | <https://open-data.europa.eu/en/data> |
| Eurostat | tool | <https://ec.europa.eu/eurostat> |
| EUvsDisinfo | dataset | <https://euvsdisinfo.eu/category/blog/feed/> |
| Evil-Twins-X/SubEvil | api-service | <https://github.com/Evil-Twins-X/SubEvil> |
| evildevill/Hackerwasi | plugin | <https://github.com/evildevill/Hackerwasi> |
| evilsocket/xray | research-project | <https://github.com/evilsocket/xray> |
| evyatarmeged/Raccoon | tool | <https://github.com/evyatarmeged/Raccoon> |
| Exhibit | tool | <https://www.simile-widgets.org/exhibit> |
| EXIFEditor.io | tool | <https://exifeditor.io> |
| ExifTool | tool | <https://exiftool.org/> |
| ExifTool | tool | <https://www.sno.phy.queensu.ca/~phil/exiftool> |
| Exonera Tor | dataset | <https://exonerator.torproject.org> |
| experte.com/email-finder | tool | <https://www.experte.com/email-finder> |
| ExpertiseFinder | tool | <https://www.expertisefinder.com> |
| ExpertPages | tool | <https://expertpages.com> |
| Experts.com | tool | <https://www.experts.com> |
| exploit-db.com | dataset | <https://www.exploit-db.com/> |
| ExportData | tool | <https://www.exportdata.io/> |
| expose-team/apify | api-service | <https://github.com/expose-team/apify> |
| expose-team/cli | framework | <https://github.com/expose-team/cli> |
| expose-team/skills | framework | <https://github.com/expose-team/skills> |
| expose-team/zapier | plugin | <https://github.com/expose-team/zapier> |
| extiop/git2mail | api-service | <https://github.com/extiop/git2mail> |
| Extravi/araa-search | api-service | <https://github.com/Extravi/araa-search> |
| ExtReMLapin/crestline | api-service | <https://github.com/ExtReMLapin/crestline> |
| eyedex | directory | <https://www.eyedex.org/> |
| EyeTON | tool | <https://telegram.me/istoneyebot> |
| Ezilon | research-project | <https://www.ezilon.com> |
| FabienEphKa/SCORPIOSINT | web-platform | <https://github.com/FabienEphKa/SCORPIOSINT> |
| face_recognition | api-service | <https://github.com/ageitgey/face_recognition> |
| Faceagle | tool | <https://faceagle.com/> |
| Facebook Friend List Scraper | api-service | <https://github.com/narkopolo/fb_friend_list_scraper> |
| Facebook GraphQL Scraper | api-service | <https://github.com/XD-MHLOO/facebook-gql-scraper> |
| Facebook Search | tool | <https://search.fb.com/> |
| FaceCheck.ID | tool | <https://facecheck.id> |
| faceseek.online | tool | <https://faceseek.online/> |
| Fact Check | tool | <https://www.factcheck.org> |
| Factiva | research-project | <https://global.factiva.com> |
| Factiva | tool | <https://www.dowjones.com/factiva> |
| facusturla/osint-argentina | framework | <https://github.com/facusturla/osint-argentina> |
| fadidevv/keyhunter | api-service | <https://github.com/fadidevv/keyhunter> |
| FaganFinder | tool | <https://www.faganfinder.com/engines> |
| Faizee-Asad/InstaRecon | research-project | <https://github.com/Faizee-Asad/InstaRecon> |
| Fake News – Inforrm's Blog | dataset | <https://inforrm.org/tag/fake-news/feed/> |
| fakeimagedetector.com | tool | <https://www.fakeimagedetector.com/> |
| Family Search | tool | <https://familysearch.org> |
| FamilyTreeNow | research-project | <https://familytreenow.com> |
| Fanpage Karma | tool | <https://www.fanpagekarma.com> |
| FastPeopleSearch | tool | <https://www.fastpeoplesearch.com/> |
| FatalS3C/gitsint | tool | <https://github.com/FatalS3C/gitsint> |
| FaviconHash | tool | <https://kriztalz.sh/favicon-hash/> |
| FaxVIN | research-project | <https://www.faxvin.com/> |
| Fb-sleep-stats | tool | <https://github.com/sqren/fb-sleep-stats> |
| fb0sh/dsh-pentester | container | <https://github.com/fb0sh/dsh-pentester> |
| feddedz/feddedosint | framework | <https://github.com/feddedz/feddedosint> |
| Federal Bureau of Prisons - Inmate Locator (US) | tool | <https://www.bop.gov/inmateloc> |
| Feed Exileed | dataset | <http://feed.exileed.com> |
| Feed Filter Maker | dataset | <https://feed.janicek.co> |
| FeedBooster | dataset | <https://www.qsensei.com> |
| Feederator | dataset | <http://www.feederator.org> |
| Feedly | dataset | <https://www.feedly.com> |
| FeedReader | dataset | <https://www.feedreader.com> |
| FetchRSS | tool | <https://fetchrss.com> |
| ffffffff0x/Digital-Privacy | research-project | <https://github.com/ffffffff0x/Digital-Privacy> |
| Fierce | tool | <https://github.com/mschwager/fierce> |
| File Search Engine | tool | <https://www.filesearch.link/> |
| FileListing | tool | <https://filelisting.com/> |
| FilePursuit | tool | <https://filepursuit.com/> |
| Filesec.io | directory | <https://filesec.io> |
| FileVault | tool | <https://support.apple.com/en-us/HT204837> |
| Filmot | directory | <https://filmot.com/> |
| FinalNotes Obituary Research Guide | dashboard | <https://www.finalnotes.page/obituary-research-guide/> |
| FinalRecon | framework | <https://github.com/thewhiteh4t/FinalRecon> |
| Find my Facebook ID | plugin | <https://randomtools.io> |
| Find Security Contacts | directory | <https://findsecuritycontacts.com> |
| Find YouTube Video | tool | <https://findyoutubevideo.thetechrobo.ca/> |
| Find-pdf-doc | tool | <http://www.findpdfdoc.com> |
| Findomain/Findomain | api-service | <https://github.com/Findomain/Findomain> |
| FindStickerCreator | tool | <https://t.me/SPOwnerBot> |
| findsubdomains | web-platform | <https://findsubdomains.com/> |
| Firefox | tool | <https://www.mozilla.org> |
| firms.modaps.eosdis.nasa.gov | tool | <https://firms.modaps.eosdis.nasa.gov/> |
| Fish4Jobs | tool | <https://www.fish4.co.uk> |
| fkkarakurt/reconic | tool | <https://github.com/fkkarakurt/reconic> |
| Flash Earth | research-project | <https://www.flashearth.com> |
| flashnuke/WebRecon | directory | <https://github.com/flashnuke/WebRecon> |
| Flashpoint | web-platform | <https://flashpoint.io> |
| Flickr | tool | <https://flickr.com/search/> |
| Flickr | tool | <https://www.flickr.com> |
| FlightAware | web-platform | <https://www.flightaware.com/> |
| Flightradar24 | tool | <https://www.flightradar24.com/> |
| Flintgliboom/OSINT-Tool-For-TG | framework | <https://github.com/Flintgliboom/OSINT-Tool-For-TG> |
| Flipboard | tool | <https://flipboard.com> |
| Flot | tool | <https://www.flotcharts.org> |
| FOCA | tool | <https://github.com/ElevenPaths/FOCA> |
| Focsec | api-service | <https://focsec.com> |
| FOFA | tool | <https://en.fofa.info/> |
| FofaInfo/Awesome-FOFA | awesome-list | <https://github.com/FofaInfo/Awesome-FOFA> |
| foia.gov | web-platform | <https://foia.gov/> |
| Fold3 (US Military Records) | tool | <https://www.fold3.com> |
| Foller.me | tool | <https://foller.me> |
| Follow.net | research-project | <https://follow.net> |
| FollowThatPage | tool | <https://www.followthatpage.com> |
| Forbes Global 2000 | research-project | <https://www.forbes.com/global2000/> |
| Forensically | framework | <https://29a.ch/photo-forensics/> |
| forensics.media | cli-tool | <https://forensics.media/tools/> |
| forshaur/aarya | web-platform | <https://github.com/forshaur/aarya> |
| FotoForensics | tool | <https://www.fotoforensics.com> |
| Fr6ey/BugRecon | tool | <https://github.com/Fr6ey/BugRecon> |
| Frame by Frame | plugin | <https://chrome.google.com/webstore/detail/frame-by-frame/cclnaabdfgnehogonpeddbgejclcjneh/> |
| France24 | tool | <https://www.france24.com> |
| frangelbarrera/Abster-Intelligence | web-platform | <https://github.com/frangelbarrera/Abster-Intelligence> |
| frangelbarrera/osint-agent-skills | framework | <https://github.com/frangelbarrera/osint-agent-skills> |
| frangelbarrera/OSINT-BIBLE | awesome-list | <https://github.com/frangelbarrera/OSINT-BIBLE> |
| Free Full PDF | tool | <https://www.freefullpdf.com> |
| Free OSINT Training | tool | <https://freetraining.dfirdiva.com/free-osint-training> |
| Free Proxy List | research-project | <https://github.com/proxifly/free-proxy-list> |
| Freebase | tool | <https://developers.google.com/freebase> |
| FreeCarrierLookup | research-project | <https://freecarrierlookup.com/> |
| freelabz/secator | tool | <https://github.com/freelabz/secator> |
| FreetoolZ/tool | framework | <https://github.com/FreetoolZ/tool> |
| Fridtjof-Nansen/fridtjof-nansen-investigation-platform | web-platform | <https://github.com/Fridtjof-Nansen/fridtjof-nansen-investigation-platform> |
| frishtik/osint-tools-mcp-server | tool | <https://github.com/frishtik/osint-tools-mcp-server> |
| frknaykc/SecOps-Google-Dork-Collection | research-project | <https://github.com/frknaykc/SecOps-Google-Dork-Collection> |
| frkndncr/WebAnalyzer | plugin | <https://github.com/frkndncr/WebAnalyzer> |
| Full Fact | tool | <https://fullfact.org> |
| FullContact | api-service | <https://www.fullcontact.com> |
| FullHunt | tool | <https://fullhunt.io/> |
| Fundacio-i2CAT/InfoHound | tool | <https://github.com/Fundacio-i2CAT/InfoHound> |
| Fused-Gaming/breach-around | framework | <https://github.com/Fused-Gaming/breach-around> |
| FusionCharts | tool | <https://www.fusioncharts.com> |
| FuzzingMyGF/Email_to_Github_account | tool | <https://github.com/FuzzingMyGF/Email_to_Github_account> |
| Fylings | web-platform | <https://www.fylings.com> |
| fyoorer/ShadowClone | tool | <https://github.com/fyoorer/ShadowClone> |
| g0ldencybersec/CloudRecon | tool | <https://github.com/g0ldencybersec/CloudRecon> |
| g0ldencybersec/EasyEASM | tool | <https://github.com/g0ldencybersec/EasyEASM> |
| gabamnml/hoper | tool | <https://github.com/gabamnml/hoper> |
| galihap76/collector | api-service | <https://github.com/galihap76/collector> |
| galile0ff/galileoff-Dorkful | tool | <https://github.com/galile0ff/galileoff-Dorkful> |
| Gapminder World | tool | <https://www.gapminder.org/data> |
| gau | tool | <https://github.com/lc/gau> |
| GCPBucketBrute | tool | <https://github.com/RhinoSecurityLabs/GCPBucketBrute> |
| GeckoSplat/rexif | tool | <https://github.com/GeckoSplat/rexif> |
| gemini.google.com | research-project | <https://gemini.google.com/> |
| Genealogy Bank | tool | <https://www.genealogybank.com> |
| Genealogy Links | directory | <https://www.genealogylinks.net> |
| GeoAziz/DarkReconX | framework | <https://github.com/GeoAziz/DarkReconX> |
| Geocreepy | tool | <https://www.geocreepy.com> |
| GeoGig | research-project | <https://geogig.org> |
| Geograph | tool | <https://www.geograph.org.uk/> |
| geoguessr.com | tool | <https://geoguessr.com/> |
| GeoHints | tool | <https://geohints.com/> |
| GeoInfer | research-project | <https://geoinfer.com> |
| GeoMacFinder | tool | <https://t.me/geomacbot> |
| GeoNames | research-project | <https://www.geonames.org> |
| Georgian-Wordlist | framework | <https://github.com/rawfilejson/Georgian-Wordlist> |
| Geosearch | tool | <https://www.geosearchtool.com> |
| GeoSpy | tool | <https://geospy.ai/> |
| GeoSpy | tool | <https://geospy.web.app/> |
| GeoSpy Pro | tool | <https://geospy.ai/pro> |
| Gerdoo (Iran) | tool | <https://gerdoo.me> |
| german-namestnikov/unhidens | tool | <https://github.com/german-namestnikov/unhidens> |
| Get-Metadata.com | tool | <https://www.get-metadata.com> |
| Getairplane | tool | <https://telegram.me/getairplane_bot> |
| getChatList | tool | <https://telegram.me/getchatlistbot> |
| getcontact.com | tool | <https://getcontact.com/> |
| getdeadrecon/deadrecon | framework | <https://github.com/getdeadrecon/deadrecon> |
| getnotify.com | tool | <https://getnotify.com/> |
| GetSendGifts | tool | <https://telegram.me/GetSendGiftsProBot> |
| GetTikVideo | tool | <https://gettikvideo.com/tiktok-profile-picture-downloader> |
| gh4rib/onions | web-platform | <https://github.com/gh4rib/onions> |
| Ghiro | tool | <https://www.getghiro.org> |
| GHNames | tool | <https://ghnames.com/> |
| Ghostery | tool | <https://www.ghostery.com> |
| gijn.org | tool | <https://gijn.org/> |
| gildas-lormeau/SingleFile | browser-extension | <https://github.com/gildas-lormeau/SingleFile> |
| gildas-lormeau/SingleFile-MV3 | plugin | <https://github.com/gildas-lormeau/SingleFile-MV3> |
| giriaryan694-a11y/ary.osint | awesome-list | <https://github.com/giriaryan694-a11y/ary.osint> |
| GitHub gist | tool | <https://gist.github.com> |
| github.com | api-service | <https://github.com/Xquik-dev/x-twitter-scraper> |
| github.com/Astrosp/Awesome-OSINT-For-Everything | awesome-list | <https://github.com/Astrosp/Awesome-OSINT-For-Everything> |
| github.com/elementalsouls/Claude-OSINT | plugin | <https://github.com/elementalsouls/Claude-OSINT> |
| github.com/hisxo/ReconAIzer | plugin | <https://github.com/hisxo/ReconAIzer> |
| github.com/mandiant/commando-vm | tool | <https://github.com/mandiant/commando-vm> |
| github.com/Manisso/fsociety | awesome-list | <https://github.com/Manisso/fsociety> |
| github.com/sinwindie/OSINT | awesome-list | <https://github.com/sinwindie/OSINT> |
| github.com/tracelabs/awesome-osint | awesome-list | <https://github.com/tracelabs/awesome-osint> |
| github.com/Z4nzu/hackingtool | awesome-list | <https://github.com/Z4nzu/hackingtool> |
| github_monitor | tool | <https://github.com/misiektoja/github_monitor> |
| GithubRecon | tool | <https://kriztalz.sh/github-recon/> |
| GitLabe/OSINT-Pentest-Framework | framework | <https://github.com/GitLabe/OSINT-Pentest-Framework> |
| GitLeak | tool | <https://gitleak.io> |
| gitsint-rs/gitsint-rs | web-platform | <https://github.com/gitsint-rs/gitsint-rs> |
| gitstq/TraceHunter | web-platform | <https://github.com/gitstq/TraceHunter> |
| giuliacassara/awesome-social-engineering | awesome-list | <https://github.com/giuliacassara/awesome-social-engineering> |
| gl0bal01/gl0bal01 | tool | <https://github.com/gl0bal01/gl0bal01> |
| gl0bal01/intel-codex | framework | <https://github.com/gl0bal01/intel-codex> |
| Glassdoor | research-project | <https://www.glassdoor.com> |
| glebarez/cero | tool | <https://github.com/glebarez/cero> |
| GLEIF LEI Search | directory | <https://search.gleif.org/> |
| Glit | tool | <https://github.com/shadawck/glit> |
| globalEdge | research-project | <https://globaledge.msu.edu> |
| globalEDGE Database of International Business Statistics | dataset | <https://globaledge.msu.edu/tools-and-data/dibs> |
| GlobalExperts | tool | <http://www.theglobalexperts.org> |
| gmapcatcher | tool | <https://github.com/heldersepu/gmapcatcher> |
| gnebbia/pdlist | tool | <https://github.com/gnebbia/pdlist> |
| GNU PG | tool | <https://www.gnupg.org/download/index.html> |
| Gobuster | directory | <https://github.com/OJ/gobuster> |
| gocaio/goca | tool | <https://github.com/gocaio/goca> |
| gokhancode/OSINT-Tools | tool | <https://github.com/gokhancode/OSINT-Tools> |
| gokulapap/Reconator | tool | <https://github.com/gokulapap/Reconator> |
| gokulapap/submax | tool | <https://github.com/gokulapap/submax> |
| GONZOsint/geowifi | dataset | <https://github.com/GONZOsint/geowifi> |
| GONZOsint/gitrecon | tool | <https://github.com/GONZOsint/gitrecon> |
| GONZOsint/gvision | api-service | <https://github.com/GONZOsint/gvision> |
| GONZOsint/Namechk | research-project | <https://github.com/GONZOsint/Namechk> |
| Goo (Japan) | tool | <http://www.goo.ne.jp> |
| GoodFirms | research-project | <https://www.goodfirms.co/> |
| goodoleusa/atropos | dashboard | <https://github.com/goodoleusa/atropos> |
| Goodsearch | tool | <https://www.goodsearch.com> |
| Goofram | tool | <http://www.goofram.com> |
| Google Adwords | research-project | <https://adwords.google.com> |
| Google Alerts | web-platform | <https://www.google.com/alerts> |
| Google Custom Search | tool | <https://www.google.com/cse> |
| Google Developers: Charts | tool | <https://developers.google.com/chart> |
| Google Earth | tool | <https://earth.google.com/> |
| Google Earth | research-project | <https://www.google.com/earth> |
| Google Earth Pro | research-project | <https://www.google.com/intl/en/earth/versions/#earth-pro> |
| Google Finance | tool | <https://www.google.com/finance> |
| Google Groups | tool | <https://groups.google.com> |
| Google Guide Advanced Operators | dashboard | <http://www.googleguide.com/advanced_operators_reference.html> |
| Google Hacking Database (GHDB) | directory | <https://www.exploit-db.com/google-hacking-database> |
| Google Image | tool | <https://images.google.com> |
| Google Lens | tool | <https://lens.google.com/> |
| Google Maps | research-project | <https://www.google.com/maps> |
| Google My Maps | research-project | <https://www.google.com/maps/about/mymaps> |
| Google News | tool | <https://news.google.com> |
| Google News Print Archive | tool | <https://news.google.com/newspapers> |
| Google Public Data Explorer | tool | <https://www.google.com/publicdata/directory> |
| Google Scholar | tool | <https://scholar.google.com> |
| Google Search | tool | <https://www.google.com> |
| Google Similar Pages | tool | <https://chrome.google.com/webstore/detail/google-similar-pages/pjnfggphgdjblhfjaphkjhfpiiekbbej> |
| Google Trends | research-project | <https://www.google.com/trends> |
| GoSecure/burp-ntlm-challenge-decoder | plugin | <https://github.com/GoSecure/burp-ntlm-challenge-decoder> |
| Government of Canada Open Data | tool | <https://open.canada.ca/en> |
| govint | cli-tool | <https://github.com/NPCmillionaire/govint> |
| gowthamaraj/OSINT-Explorer | framework | <https://github.com/gowthamaraj/OSINT-Explorer> |
| GPG Tools | tool | <https://gpgtools.org> |
| Gpredict | tool | <https://github.com/csete/gpredict> |
| GPSVisualizer | research-project | <https://www.gpsvisualizer.com> |
| Gqrx | tool | <https://github.com/gqrx-sdr/gqrx> |
| Gr1mmie/autoenum | directory | <https://github.com/Gr1mmie/autoenum> |
| grabify.link | tool | <https://grabify.link/> |
| graniet/operative-framework | plugin | <https://github.com/graniet/operative-framework> |
| GraphSense | tool | <https://graphsense.org> |
| GraphX | tool | <https://spark.apache.org/graphx> |
| GraphyStories | research-project | <https://app.graphystories.com> |
| GrassGIS | research-project | <https://grass.osgeo.org> |
| GrayhatWarfare | directory | <https://buckets.grayhatwarfare.com> |
| GrayhatWarfare | directory | <https://grayhatwarfare.com/> |
| gregalletti/CTF_tools | awesome-list | <https://github.com/gregalletti/CTF_tools> |
| grep.app | tool | <https://grep.app/> |
| Grey Guide | dashboard | <https://greyguide.isti.cnr.it> |
| Grey Literature Strategies | tool | <http://greylitstrategies.info> |
| Grey Literature – List of Gateways | tool | <https://csulb.libguides.com/graylit> |
| GreyNet International | tool | <https://www.greynet.org> |
| Greynoise | tool | <https://greynoise.io/> |
| GreyNoise | tool | <https://viz.greynoise.io/> |
| grizzsec/JackOSINT | tool | <https://github.com/grizzsec/JackOSINT> |
| GroupDa | tool | <https://groupda.com/telegram/group/search> |
| Groupio | tool | <https://en.groupio.app/> |
| Guardian Project | tool | <https://guardianproject.info> |
| Guerrilla Mail | tool | <https://www.guerrillamail.com> |
| GuideStar | dashboard | <https://www.guidestar.org> |
| gwen001/google-search | tool | <https://github.com/gwen001/google-search> |
| gwen001/pentest-tools | tool | <https://github.com/gwen001/pentest-tools> |
| h0tak88r/AutoSubRecon | tool | <https://github.com/h0tak88r/AutoSubRecon> |
| h0tak88r/subfalcon | dataset | <https://github.com/h0tak88r/subfalcon> |
| h4r5h1t/webcopilot | tool | <https://github.com/h4r5h1t/webcopilot> |
| h6nt3r/jssf | tool | <https://github.com/h6nt3r/jssf> |
| Hack The Box | tool | <https://www.hackthebox.com> |
| Hack-with-Github/Powerful-Plugins | plugin | <https://github.com/Hack-with-Github/Powerful-Plugins> |
| Hack23/cia | web-platform | <https://github.com/Hack23/cia> |
| Hacker101 | library | <https://www.hacker101.com> |
| hackerdogs-ai/hd-mcpservers-docker | container | <https://github.com/hackerdogs-ai/hd-mcpservers-docker> |
| Hackerest/pwneye | tool | <https://github.com/Hackerest/pwneye> |
| Hacking: The Art of Exploitation (book) | tool | <https://nostarch.com/hacking2.htm> |
| HackingLZ/gibson | tool | <https://github.com/HackingLZ/gibson> |
| Hacknorith/OSINT_Notes_TCM | tool | <https://github.com/Hacknorith/OSINT_Notes_TCM> |
| HackTricks | tool | <https://book.hacktricks.xyz> |
| HackUnderway/SearchPhone | api-service | <https://github.com/HackUnderway/SearchPhone> |
| HackUnderway/WhatsOSINT | tool | <https://github.com/HackUnderway/WhatsOSINT> |
| haithamaouati/Kraken | tool | <https://github.com/haithamaouati/Kraken> |
| hakluke/hakip2host | tool | <https://github.com/hakluke/hakip2host> |
| hakluke/hakrawler | web-platform | <https://github.com/hakluke/hakrawler> |
| hakrevdns | tool | <https://github.com/hakluke/hakrevdns> |
| halans/osint-explorer | web-platform | <https://github.com/halans/osint-explorer> |
| halans/osint-explorer-v2 | directory | <https://github.com/halans/osint-explorer-v2> |
| haltman-io/ip-thc | dataset | <https://github.com/haltman-io/ip-thc> |
| harelhz/echoscope | tool | <https://github.com/harelhz/echoscope> |
| harleo/asnip | tool | <https://github.com/harleo/asnip> |
| Harmari (Unified Listings Search) | tool | <https://www.harmari.com/search/unified> |
| HARO | tool | <https://www.helpareporter.com> |
| harpa.ai | tool | <https://harpa.ai/> |
| HARSHRAJ2789/darkscan | web-platform | <https://github.com/HARSHRAJ2789/darkscan> |
| HashBin | tool | <https://hashb.in/#Q===> |
| hastebin | tool | <https://www.toptal.com/developers/hastebin/> |
| Hatching Triage | tool | <https://tria.ge/> |
| HaveIBeenPwned Integration | tool | <https://haveibeenpwned.com> |
| haveibeenpwned.com/API | api-service | <https://haveibeenpwned.com/API> |
| haveibeenzuckered | dataset | <https://haveibeenzuckered.com/> |
| HCL Threat Map | tool | <https://www.hcltech.com/hcl-threat-map> |
| hdyrawan/w4f | web-platform | <https://github.com/hdyrawan/w4f> |
| Headhunter | tool | <http://www.headhunter.com> |
| HeadlineSpot | tool | <http://www.headlinespot.com> |
| Henriquemonovular780/Legendary_OSINT | api-service | <https://github.com/Henriquemonovular780/Legendary_OSINT> |
| Here | research-project | <https://here.com> |
| here | api-service | <https://www.reddit.com/r/pushshift/> |
| hessman/gcert | research-project | <https://github.com/hessman/gcert> |
| hhhrrrttt222111/Dorkify | api-service | <https://github.com/hhhrrrttt222111/Dorkify> |
| Highcharts | tool | <https://www.highcharts.com> |
| HighWire: Free Online Full-text Articles | tool | <https://highwire.stanford.edu/lists/freeart.dtl> |
| HimeraSearch | tool | <https://t.me/HimeraNeGBL8Pro1dp_Search_bot> |
| hippiiee/Hippie-OSINT-Toolkit | framework | <https://github.com/hippiiee/Hippie-OSINT-Toolkit> |
| Hiroxx-glichter/IZ-OSINT-TOOLS | tool | <https://github.com/Hiroxx-glichter/IZ-OSINT-TOOLS> |
| HIS Piers | tool | <https://www.ihs.com/products/piers.html> |
| hisxo/gitGraber | web-platform | <https://github.com/hisxo/gitGraber> |
| hivemoderation.com | tool | <https://hivemoderation.com/> |
| hkm/whoishere.py | desktop-app | <https://github.com/hkm/whoishere.py> |
| hlr-lookups.com | tool | <https://www.hlr-lookups.com/> |
| Hohli | tool | <https://charts.hohli.com> |
| homanp/infinite-monitor | dashboard | <https://github.com/homanp/infinite-monitor> |
| Homemetry | tool | <https://homemetry.com> |
| HoneyLabs | api-service | <https://honeylabs.net> |
| Hooey webprint | tool | <http://www.hooeeywebprint.com.s3-website-us-east-1.amazonaws.com/download.html> |
| Hootsuite | tool | <https://hootsuite.com> |
| Hoovers | research-project | <https://www.hoovers.com> |
| HOPain/OSINT-Search-Tools | tool | <https://github.com/HOPain/OSINT-Search-Tools> |
| Hotspot Shield | tool | <https://www.hotspotshield.com> |
| Hound0x/JSIntelliRecon | api-service | <https://github.com/Hound0x/JSIntelliRecon> |
| HowToFind-bot/osint-tools | directory | <https://github.com/HowToFind-bot/osint-tools> |
| HowToFind-bot/YaSeeker | api-service | <https://github.com/HowToFind-bot/YaSeeker> |
| HTTPs Everywhere | tool | <https://www.eff.org/https-everywhere/> |
| https://1tv.ge | tool | <https://1tv.ge> |
| https://acb.gov.ge | tool | <https://acb.gov.ge> |
| https://agenda.ge | tool | <https://agenda.ge> |
| https://agruni.edu.ge | research-project | <https://agruni.edu.ge> |
| https://amerikiskhma.com | web-platform | <https://amerikiskhma.com> |
| https://archive.gov.ge | directory | <https://archive.gov.ge> |
| https://archive.org/details/1989-tbilisi-1_202408 | tool | <https://archive.org/details/1989-tbilisi-1_202408> |
| https://atlanticcouncil.org/programs/digital-forensic-research-lab/ | research-project | <https://atlanticcouncil.org/programs/digital-forensic-research-lab/> |
| https://auto.ss.ge | dataset | <https://auto.ss.ge> |
| https://autopapa.ge | dataset | <https://autopapa.ge> |
| https://bankofgeorgia.ge | tool | <https://bankofgeorgia.ge> |
| https://basisbank.ge | tool | <https://basisbank.ge> |
| https://batumelebi.netgazeti.ge | tool | <https://batumelebi.netgazeti.ge> |
| https://bgp.he.net/country/GE | tool | <https://bgp.he.net/country/GE> |
| https://bm.ge | tool | <https://bm.ge> |
| https://boost.worldbank.org | tool | <https://boost.worldbank.org> |
| https://btu.edu.ge | tool | <https://btu.edu.ge> |
| https://budget.ge | tool | <https://budget.ge> |
| https://catagi.ge | research-project | <https://catagi.ge> |
| https://cellfie.ge | tool | <https://cellfie.ge> |
| https://census2024.geostat.ge | tool | <https://census2024.geostat.ge> |
| https://cesko.ge | tool | <https://cesko.ge> |
| https://cesko.ge/en/amomrchevlebi | web-platform | <https://cesko.ge/en/amomrchevlebi> |
| https://civil.ge | tool | <https://civil.ge> |
| https://commersant.ge | tool | <https://commersant.ge> |
| https://competition.ge | dataset | <https://competition.ge> |
| https://constcourt.ge | dataset | <https://constcourt.ge> |
| https://courtwatch.ge | dataset | <https://courtwatch.ge> |
| https://credobank.ge | tool | <https://credobank.ge> |
| https://crrc.ge | research-project | <https://crrc.ge> |
| https://crystal.ge | tool | <https://crystal.ge> |
| https://csb.gov.ge | web-platform | <https://csb.gov.ge> |
| https://cu.edu.ge | tool | <https://cu.edu.ge> |
| https://cv.ge | web-platform | <https://cv.ge> |
| https://data.gov.ge | web-platform | <https://data.gov.ge> |
| https://data.ipu.org/parliament/GE | tool | <https://data.ipu.org/parliament/GE> |
| https://data.worldbank.org/country/georgia | web-platform | <https://data.worldbank.org/country/georgia> |
| https://dea.gov.ge | desktop-app | <https://dea.gov.ge> |
| https://democracyresearch.ge | research-project | <https://democracyresearch.ge> |
| https://digitallibrary.tsu.ge | library | <https://digitallibrary.tsu.ge> |
| https://dis.gov.ge | dataset | <https://dis.gov.ge> |
| https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGwYr9DI2UncoqJQ | framework | <https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGwYr9DI2UncoqJQ> |
| https://ecd.court.ge | dataset | <https://ecd.court.ge> |
| https://ecd.court.ge/CurrentCase | dataset | <https://ecd.court.ge/CurrentCase> |
| https://ecd.court.ge/Decision | dataset | <https://ecd.court.ge/Decision> |
| https://ecd.court.ge/FinalDocument | dataset | <https://ecd.court.ge/FinalDocument> |
| https://ecd.court.ge/PublicNotification | dataset | <https://ecd.court.ge/PublicNotification> |
| https://economy.ge | web-platform | <https://economy.ge> |
| https://ecourt.ge | desktop-app | <https://ecourt.ge> |
| https://elibrary.emis.ge | web-platform | <https://elibrary.emis.ge> |
| https://emis.ge | web-platform | <https://emis.ge> |
| https://enreg.reestri.gov.ge | dataset | <https://enreg.reestri.gov.ge> |
| https://eqe.ge | web-platform | <https://eqe.ge> |
| https://euvsdisinfo.eu | dataset | <https://euvsdisinfo.eu> |
| https://evercar.ge | dataset | <https://evercar.ge> |
| https://extra.ge | tool | <https://extra.ge> |
| https://factcheck.ge | tool | <https://factcheck.ge> |
| https://finca.ge | tool | <https://finca.ge> |
| https://forbes.ge | tool | <https://forbes.ge> |
| https://formulanews.ge | tool | <https://formulanews.ge> |
| https://freeuni.edu.ge | directory | <https://freeuni.edu.ge> |
| https://gavel.ge | web-platform | <https://gavel.ge> |
| https://geofacts.ge | web-platform | <https://geofacts.ge> |
| https://georgiancinema.ge | dataset | <https://georgiancinema.ge> |
| https://georgiatoday.ge | tool | <https://georgiatoday.ge> |
| https://geostat.ge | tool | <https://geostat.ge> |
| https://geostat.ge/en/modules/categories/735/population-census | plugin | <https://geostat.ge/en/modules/categories/735/population-census> |
| https://geostat.ge/ka/modules/categories/858/monatsemta-baza | plugin | <https://geostat.ge/ka/modules/categories/858/monatsemta-baza> |
| https://gita.gov.ge | tool | <https://gita.gov.ge> |
| https://github.com/drawrowfly/tiktok-scraper | web-platform | <https://github.com/drawrowfly/tiktok-scraper> |
| https://globalpublicprocurementdata.org/gppd/country_profile/GE | web-platform | <https://globalpublicprocurementdata.org/gppd/country_profile/GE> |
| https://gov.ge | web-platform | <https://gov.ge> |
| https://gse.ge | tool | <https://gse.ge> |
| https://gtu.ge | research-project | <https://gtu.ge> |
| https://gyla.ge | tool | <https://gyla.ge> |
| https://heritage.gov.ge | dataset | <https://heritage.gov.ge> |
| https://home.ge | web-platform | <https://home.ge> |
| https://home.ss.ge | web-platform | <https://home.ss.ge> |
| https://homesearch.ge | web-platform | <https://homesearch.ge> |
| https://hr.ge | web-platform | <https://hr.ge> |
| https://hra.gov.ge | tool | <https://hra.gov.ge> |
| https://icij.org | research-project | <https://icij.org> |
| https://icij.org/investigations/ | dataset | <https://icij.org/investigations/> |
| https://idfi.ge | tool | <https://idfi.ge> |
| https://iliauni.edu.ge | dataset | <https://iliauni.edu.ge> |
| https://imedinews.ge | tool | <https://imedinews.ge> |
| https://imf.org/en/Countries/GEO | web-platform | <https://imf.org/en/Countries/GEO> |
| https://insurance.gov.ge | dataset | <https://insurance.gov.ge> |
| https://interpressnews.ge | tool | <https://interpressnews.ge> |
| https://ipinfo.io/countries/ge | tool | <https://ipinfo.io/countries/ge> |
| https://isfed.ge | dataset | <https://isfed.ge> |
| https://jam-news.net | tool | <https://jam-news.net> |
| https://jobs.ge | web-platform | <https://jobs.ge> |
| https://justice.gov.ge | web-platform | <https://justice.gov.ge> |
| https://kavkasia.ge | tool | <https://kavkasia.ge> |
| https://korter.ge | web-platform | <https://korter.ge> |
| https://liberali.ge | tool | <https://liberali.ge> |
| https://libertybank.ge | tool | <https://libertybank.ge> |
| https://library.iliauni.edu.ge | dataset | <https://library.iliauni.edu.ge> |
| https://livo.ge | web-platform | <https://livo.ge> |
| https://magticom.ge | tool | <https://magticom.ge> |
| https://makler.ge | web-platform | <https://makler.ge> |
| https://maps.google.com | web-platform | <https://maps.google.com> |
| https://matsne.gov.ge | dataset | <https://matsne.gov.ge> |
| https://matsne.gov.ge/en/document/view/16426 | tool | <https://matsne.gov.ge/en/document/view/16426> |
| https://matsne.gov.ge/en/document/view/31702 | tool | <https://matsne.gov.ge/en/document/view/31702> |
| https://mdfgeorgia.ge | tool | <https://mdfgeorgia.ge> |
| https://mes.gov.ge | web-platform | <https://mes.gov.ge> |
| https://mfa.gov.ge | web-platform | <https://mfa.gov.ge> |
| https://mof.gov.ge | web-platform | <https://mof.gov.ge> |
| https://moh.gov.ge | tool | <https://moh.gov.ge> |
| https://mrdi.gov.ge | web-platform | <https://mrdi.gov.ge> |
| https://mtavari.tv | tool | <https://mtavari.tv> |
| https://museum.ge | dataset | <https://museum.ge> |
| https://my.gov.ge | web-platform | <https://my.gov.ge> |
| https://myauto.ge | dataset | <https://myauto.ge> |
| https://myauto.ge/en/vin | dataset | <https://myauto.ge/en/vin> |
| https://myhome.ge | web-platform | <https://myhome.ge> |
| https://myjobs.ge | web-platform | <https://myjobs.ge> |
| https://mymarket.ge | tool | <https://mymarket.ge> |
| https://myparts.ge | dataset | <https://myparts.ge> |
| https://mythdetector.com | web-platform | <https://mythdetector.com> |
| https://mythdetector.com/en/factchecker-db/ | dataset | <https://mythdetector.com/en/factchecker-db/> |
| https://naec.ge | web-platform | <https://naec.ge> |
| https://napr.gov.ge | web-platform | <https://napr.gov.ge> |
| https://napr.gov.ge/en/service/information-services/extract-public-register | web-platform | <https://napr.gov.ge/en/service/information-services/extract-public-register> |
| https://napr.gov.ge/en/service/registers | web-platform | <https://napr.gov.ge/en/service/registers> |
| https://nbg.gov.ge | tool | <https://nbg.gov.ge> |
| https://nbg.gov.ge/en/monetary-policy/currency | tool | <https://nbg.gov.ge/en/monetary-policy/currency> |
| https://nbg.gov.ge/en/supervision | tool | <https://nbg.gov.ge/en/supervision> |
| https://nbg.gov.ge/en/supervision/aml-cft | tool | <https://nbg.gov.ge/en/supervision/aml-cft> |
| https://ncdc.ge | tool | <https://ncdc.ge> |
| https://ndi.org/georgia | tool | <https://ndi.org/georgia> |
| https://nea.gov.ge | dataset | <https://nea.gov.ge> |
| https://netgazeti.ge | tool | <https://netgazeti.ge> |
| https://nfa.gov.ge | dataset | <https://nfa.gov.ge> |
| https://nic.ge | tool | <https://nic.ge> |
| https://nic.ge/en/domains/whois | tool | <https://nic.ge/en/domains/whois> |
| https://nirsoft.net/countryip/ge_total.html | tool | <https://nirsoft.net/countryip/ge_total.html> |
| https://nplg.gov.ge | library | <https://nplg.gov.ge> |
| https://nsdi.gov.ge | web-platform | <https://nsdi.gov.ge> |
| https://oc-media.org | tool | <https://oc-media.org> |
| https://occrp.org | tool | <https://occrp.org> |
| https://odapi.spa.ge | api-service | <https://odapi.spa.ge> |
| https://ogpgeorgia.gov.ge | web-platform | <https://ogpgeorgia.gov.ge> |
| https://ombudsman.ge | tool | <https://ombudsman.ge> |
| https://opencorporates.com/companies/ge | tool | <https://opencorporates.com/companies/ge> |
| https://opendata.spa.ge | web-platform | <https://opendata.spa.ge> |
| https://openlibrary.ge | library | <https://openlibrary.ge> |
| https://opensanctions.org/datasets/ext_ge_company_registry/ | dataset | <https://opensanctions.org/datasets/ext_ge_company_registry/> |
| https://opensanctions.org/datasets/ge_declarations/ | dataset | <https://opensanctions.org/datasets/ge_declarations/> |
| https://parliament.ge | web-platform | <https://parliament.ge> |
| https://patrol.gov.ge | tool | <https://patrol.gov.ge> |
| https://phr.ge | tool | <https://phr.ge> |
| https://pog.gov.ge | tool | <https://pog.gov.ge> |
| https://police.ge | web-platform | <https://police.ge> |
| https://president.gov.ge | web-platform | <https://president.gov.ge> |
| https://probation.moj.gov.ge | tool | <https://probation.moj.gov.ge> |
| https://procreditbank.ge | tool | <https://procreditbank.ge> |
| https://procurement.gov.ge | desktop-app | <https://procurement.gov.ge> |
| https://publika.ge | tool | <https://publika.ge> |
| https://radiotavisupleba.ge | web-platform | <https://radiotavisupleba.ge> |
| https://railway.ge | tool | <https://railway.ge> |
| https://research.domaintools.com/statistics/tldpedia/ge | research-project | <https://research.domaintools.com/statistics/tldpedia/ge> |
| https://rs.ge | web-platform | <https://rs.ge> |
| https://rs.ge/Eservices-en | web-platform | <https://rs.ge/Eservices-en> |
| https://rs.ge/TaxPayer-en | dataset | <https://rs.ge/TaxPayer-en> |
| https://rustavi2.ge | tool | <https://rustavi2.ge> |
| https://sao.ge | tool | <https://sao.ge> |
| https://scihub.copernicus.eu | web-platform | <https://scihub.copernicus.eu> |
| https://sda.gov.ge | web-platform | <https://sda.gov.ge> |
| https://securingdemocracy.gmfus.org/hamilton-dashboard/ | dashboard | <https://securingdemocracy.gmfus.org/hamilton-dashboard/> |
| https://silknet.com | tool | <https://silknet.com> |
| https://skolebi.emis.ge | web-platform | <https://skolebi.emis.ge> |
| https://socialjustice.org.ge | tool | <https://socialjustice.org.ge> |
| https://ss.ge | desktop-app | <https://ss.ge> |
| https://ssa.gov.ge | web-platform | <https://ssa.gov.ge> |
| https://start.me | framework | <https://start.me> |
| https://students.emis.ge | web-platform | <https://students.emis.ge> |
| https://studiomonitori.ge | tool | <https://studiomonitori.ge> |
| https://supremecourt.ge | dataset | <https://supremecourt.ge> |
| https://tabula.ge | tool | <https://tabula.ge> |
| https://tbcbank.ge | tool | <https://tbcbank.ge> |
| https://tbilisi.gov.ge | tool | <https://tbilisi.gov.ge> |
| https://tbilisihome.ge | web-platform | <https://tbilisihome.ge> |
| https://tenders.procurement.gov.ge | web-platform | <https://tenders.procurement.gov.ge> |
| https://transparency.ge | tool | <https://transparency.ge> |
| https://tsu.ge | dataset | <https://tsu.ge> |
| https://tvpirveli.ge | tool | <https://tvpirveli.ge> |
| https://ug.edu.ge | tool | <https://ug.edu.ge> |
| https://unishka.substack.com/p/osint-of-georgia | dashboard | <https://unishka.substack.com/p/osint-of-georgia> |
| https://web.archive.org/web/*/*.ge | tool | <https://web.archive.org/web/*/*.ge> |
| https://whois.ipip.net/iso/GE | directory | <https://whois.ipip.net/iso/GE> |
| https://wine.gov.ge | dataset | <https://wine.gov.ge> |
| HTTrack | directory | <https://www.httrack.com> |
| Hubii | tool | <http://hubii.com> |
| Hudson Rock | tool | <https://www.hudsonrock.com/free-tools> |
| Hudson Rock | framework | <https://www.hudsonrock.com/threat-intelligence-cybercrime-tools> |
| Hudson Rock Cavalier | tool | <https://cavalier.hudsonrock.com> |
| hueristiq/xsubfind3r | container | <https://github.com/hueristiq/xsubfind3r> |
| hueristiq/xurlfind3r | cli-tool | <https://github.com/hueristiq/xurlfind3r> |
| huggingface.co/chat | research-project | <https://huggingface.co/chat/> |
| Human Development Reports | tool | <https://hdr.undp.org/en/global-reports> |
| humandecoded/twayback | tool | <https://github.com/humandecoded/twayback> |
| Hunchly | tool | <https://www.hunch.ly/> |
| Hunt3r0x/zWATCHER | tool | <https://github.com/Hunt3r0x/zWATCHER> |
| Hunter | tool | <https://hunter.io> |
| Hunter Search Engine | tool | <https://hunter.how/> |
| hunter.io/api | api-service | <https://hunter.io/api> |
| HunxByts/GhostTrack | tool | <https://github.com/HunxByts/GhostTrack> |
| HunxByts/INSTA-OSINT | api-service | <https://github.com/HunxByts/INSTA-OSINT> |
| Hybrid Analysis | web-platform | <https://www.hybrid-analysis.com> |
| Hyperlapse | research-project | <https://github.com/TeehanLax/Hyperlapse.js> |
| HypeStat | research-project | <https://www.hypestat.com> |
| i-inteligence's | tool | <https://www.i-intelligence.eu> |
| I2P | tool | <https://geti2p.net> |
| iamnotnotacat/VoidCat-Harness | framework | <https://github.com/iamnotnotacat/VoidCat-Harness> |
| iamshafayat/JSpider | api-service | <https://github.com/iamshafayat/JSpider> |
| iamunixtz/Lazy-Hunter | api-service | <https://github.com/iamunixtz/Lazy-Hunter> |
| ibnaleem/gosearch | framework | <https://github.com/ibnaleem/gosearch> |
| ibnaleem/instatracker | api-service | <https://github.com/ibnaleem/instatracker> |
| ibnaleem/snapscoretracker | tool | <https://github.com/ibnaleem/snapscoretracker> |
| ibnu76/batok | framework | <https://github.com/ibnu76/batok> |
| Icann Lookup | research-project | <https://lookup.icann.org/en/lookup> |
| IccTeam/OwlTrack | tool | <https://github.com/IccTeam/OwlTrack> |
| ice-doom/EyeJo | tool | <https://github.com/ice-doom/EyeJo> |
| Iconosquare | tool | <https://iconosquare.com> |
| IDCrawl | tool | <https://www.idcrawl.com/> |
| IDCrawl | tool | <https://www.idcrawl.com/username> |
| Idealist | tool | <https://www.idealist.org> |
| idefasoft/Emora-Project | dashboard | <https://github.com/idefasoft/Emora-Project> |
| ideone | tool | <https://Ideone.com> |
| IGDetective | tool | <https://www.igdetective.com> |
| igorbrigadir/twitter-advanced-search | tool | <https://github.com/igorbrigadir/twitter-advanced-search> |
| ILO World Employment and Social Outlook Trends | tool | <https://www.ilo.org/global/research/global-reports/weso/2015/lang--en/index.htm> |
| ILOSTAT | tool | <https://www.ilo.org/ilostat/faces/oracle/webcenter/portalapp/pagehierarchy/Page137.jspx?_afrLoop=443508925711569&clean=true#%40%3F_afrLoop%3D443508925711569%26clean%3Dtrue%26_adf.ctrl-state%3Dl4dwldaf3_9> |
| Image Identification Project | tool | <https://www.imageidentify.com> |
| Image Raider | tool | <https://www.imageraider.com> |
| ImAyrix/cut-cdn | tool | <https://github.com/ImAyrix/cut-cdn> |
| imdivineva/osint-drillbook | tool | <https://github.com/imdivineva/osint-drillbook> |
| imedkablavi/OSINT-Roadmap | framework | <https://github.com/imedkablavi/OSINT-Roadmap> |
| IMF World Economic Outlook Database | dataset | <https://www.imf.org/external/ns/cs.aspx?id=28> |
| ImgOps | tool | <https://imgops.com/> |
| Imgur | tool | <https://imgur.com> |
| Imgur | tool | <https://imgur.com/search?q=> |
| Immersive Labs | web-platform | <https://www.immersivelabs.com> |
| immunIT/TeamsUserEnum | api-service | <https://github.com/immunIT/TeamsUserEnum> |
| immuniweb.com/websec | web-platform | <https://www.immuniweb.com/websec/> |
| Impact-I/x8-Burp | api-service | <https://github.com/Impact-I/x8-Burp> |
| Impersonal.me | tool | <http://www.impersonal.me> |
| Imperva Live Threat Map | web-platform | <https://www.imperva.com/cyber-threat-attack-map/> |
| ImpulseAdventure | tool | <https://www.impulseadventure.com/photo/jpeg-snoop.html> |
| Inc. 5000 | research-project | <https://www.inc.com/inc5000> |
| Indeed | research-project | <https://www.indeed.com> |
| Index Mundi | directory | <https://www.indexmundi.com> |
| indiancybertroops/DorKey | plugin | <https://github.com/indiancybertroops/DorKey> |
| indiancybertroops/ReconHound | api-service | <https://github.com/indiancybertroops/ReconHound> |
| IndieHum/zaal | framework | <https://github.com/IndieHum/zaal> |
| Infobel | web-platform | <https://www.infobel.com/> |
| infobyte/emploleaks | tool | <https://github.com/infobyte/emploleaks> |
| Infogr.am | tool | <https://infogr.am> |
| InfoMinder | tool | <https://www.infominder.com/webminder> |
| Inforensics/osint-vm | framework | <https://github.com/Inforensics/osint-vm> |
| InfoSecREDD/DeLookup | api-service | <https://github.com/InfoSecREDD/DeLookup> |
| Infosniper | research-project | <https://www.infosniper.net> |
| InfoStealers | directory | <https://infostealers.info/en/info> |
| InfoTracer | tool | <https://infotracer.com/> |
| InitRoot/fransRecon | tool | <https://github.com/InitRoot/fransRecon> |
| initstring/cloud_enum | tool | <https://github.com/initstring/cloud_enum> |
| initstring/linkedin2username | tool | <https://github.com/initstring/linkedin2username> |
| Inkscape | tool | <https://inkscape.org> |
| InMobPrefix | dataset | <https://github.com/hstsethi/in-mob-prefix> |
| Innocentive | tool | <https://www.innocentive.com> |
| InQuest/omnibus | tool | <https://github.com/InQuest/omnibus> |
| Insecam | directory | <https://insecam.org/> |
| Inshorts | tool | <https://www.inshorts.com> |
| Insight | tool | <https://t.me/ibhld_bot> |
| InsightFace | framework | <https://github.com/deepinsight/insightface> |
| Inspire Geoportal | web-platform | <https://inspire-geoportal.ec.europa.eu> |
| InstaAnonym | tool | <https://t.me/instaanonymbot> |
| InstaBot | tool | <https://telegram.me/InstaBot> |
| Instagram | tool | <https://www.instagram.com> |
| Instaloader | tool | <https://instaloader.github.io/> |
| instaloader/instaloader | web-platform | <https://github.com/instaloader/instaloader> |
| Instant Google Street View | research-project | <https://www.instantstreetview.com> |
| InstantAtlas | research-project | <https://www.instantatlas.com> |
| instantusername.com | tool | <https://instantusername.com/> |
| insto | api-service | <https://github.com/subzeroid/insto> |
| Instya | tool | <https://www.instya.com> |
| Intel471 | web-platform | <https://intel471.com> |
| IntelBase | web-platform | <https://intelbase.is/> |
| Intelligence X | tool | <https://intelx.io/tools> |
| IntellyWeave | web-platform | <https://github.com/vericle/intellyweave> |
| intelowlproject/IntelOwl | tool | <https://github.com/intelowlproject/IntelOwl> |
| intelseclab/osintelligence | awesome-list | <https://github.com/intelseclab/osintelligence> |
| IntelTechniques | tool | <https://inteltechniques.com/> |
| IntelTechniques Tools | framework | <https://inteltechniques.com/tools/> |
| International Energy Agency Statistics | tool | <https://www.iea.org/statistics> |
| International Labour Comparisons | tool | <https://www.bls.gov/fls/chartbook.htm> |
| International Trade Center | tool | <https://www.intracen.org/ByCountry.aspx> |
| Internet Archive | tool | <https://archive.org/> |
| Internet Archive: Open Source Videos | tool | <https://archive.org/details/opensource_movies> |
| Internet Experts | tool | <http://www.internetexperts.info> |
| internet-relay-chat/IRCP | tool | <https://github.com/internet-relay-chat/IRCP> |
| Intezer | tool | <https://analyze.intezer.com/> |
| intoDNS | research-project | <http://www.intodns.com> |
| IntoDNS.ai | research-project | <https://intodns.ai> |
| Intrigue Core | framework | <https://github.com/intrigueio/intrigue-core> |
| invid-project.eu | framework | <https://www.invid-project.eu/> |
| iojw/socialscan | web-platform | <https://github.com/iojw/socialscan> |
| IP 2 Geolocation | research-project | <https://ip2geolocation.com> |
| IP 2 Location | research-project | <http://www.ip2location.com/demo.aspx> |
| IP Checking | research-project | <http://www.ipchecking.com> |
| IP Geolocation API DB-IP | api-service | <https://db-ip.com> |
| IP Location | research-project | <https://www.iplocation.net> |
| IP Location.io | research-project | <https://iplocation.io> |
| ip-api.com | api-service | <http://ip-api.com/> |
| IP.THC.ORG | api-service | <https://ip.thc.org/> |
| ip2geo.dev | api-service | <https://ip2geo.dev> |
| IP2Location | api-service | <https://www.ip2location.com/demo> |
| IPFingerprints | research-project | <https://www.ipfingerprints.com> |
| ipinfo.io | tool | <https://ipinfo.io/> |
| ipinfo.io/developers | api-service | <https://ipinfo.io/developers> |
| iplogger.org | tool | <https://iplogger.org/> |
| IPOK | browser-extension | <https://ipok.io> |
| ipverse/as-ip-blocks | tool | <https://github.com/ipverse/as-ip-blocks> |
| IPVoid | research-project | <https://www.ipvoid.com> |
| IQDB | web-platform | <https://iqdb.org/> |
| ishandutta2007/Awesome-Dark-Web-Monitoring-Threat-Reconnaissance | awesome-list | <https://github.com/ishandutta2007/Awesome-Dark-Web-Monitoring-Threat-Reconnaissance> |
| Ishanoshada/GDorks | web-platform | <https://github.com/Ishanoshada/GDorks> |
| Ishanoshada/Owl-Eye | library | <https://github.com/Ishanoshada/Owl-Eye> |
| Islegitsite | tool | <https://www.islegitsite.com/> |
| ismailtsdln/ReconDorker | framework | <https://github.com/ismailtsdln/ReconDorker> |
| isMalicious | web-platform | <https://ismalicious.com> |
| ISP.Tools | web-platform | <https://www.isp.tools> |
| iSpionage | research-project | <https://www.ispionage.com> |
| Itar-Tass | tool | <http://www.itar-tass.com> |
| ItIsMeCall911/Awesome-Telegram-OSINT | awesome-list | <https://github.com/ItIsMeCall911/Awesome-Telegram-OSINT> |
| ITP Infotrack | tool | <https://infotrackpeople.org/> |
| itsmehacker/CardPwn | tool | <https://github.com/itsmehacker/CardPwn> |
| itsmehacker/DarkScrape | api-service | <https://github.com/itsmehacker/DarkScrape> |
| iudicium/pryingdeep | research-project | <https://github.com/iudicium/pryingdeep> |
| ivan-sincek/penetration-testing-cheat-sheet | tool | <https://github.com/ivan-sincek/penetration-testing-cheat-sheet> |
| IVMachiavelli/OSINT_Team_Links | tool | <https://github.com/IVMachiavelli/OSINT_Team_Links> |
| ivpaste | tool | <https://Ivpaste.com> |
| ivre/ivre | web-platform | <https://github.com/ivre/ivre> |
| iZito | tool | <https://www.izito.com> |
| j3ssie/goverview | tool | <https://github.com/j3ssie/goverview> |
| j3ssie/metabigor | api-service | <https://github.com/j3ssie/metabigor> |
| j3ssie/osmedeus | framework | <https://github.com/j3ssie/osmedeus> |
| JackJuly/linkook | web-platform | <https://github.com/JackJuly/linkook> |
| jakecreps/poastal | tool | <https://github.com/jakecreps/poastal> |
| jamditis/claude-skills-journalism | tool | <https://github.com/jamditis/claude-skills-journalism> |
| JARM | tool | <https://github.com/salesforce/jarm> |
| jasperan/whatsapp-osint | tool | <https://github.com/jasperan/whatsapp-osint> |
| Java Infovis Toolkit | framework | <https://philogb.github.io/jit> |
| JavierOlmedo/ipdiscover | tool | <https://github.com/JavierOlmedo/ipdiscover> |
| Jeffreys Image Metadata Viewer | tool | <http://exif.regex.info/> |
| jerlendds/osintbuddy | plugin | <https://github.com/jerlendds/osintbuddy> |
| jerlendds/osintbuddy-plugins | plugin | <https://github.com/jerlendds/osintbuddy-plugins> |
| jermanuts/bad-opsec | tool | <https://github.com/jermanuts/bad-opsec> |
| jermiDEV/pikmist | dashboard | <https://github.com/jermiDEV/pikmist> |
| jhatzimalis/LazyOSINT | cli-tool | <https://github.com/jhatzimalis/LazyOSINT> |
| JHWH-L/jhwh-cyber-recon | desktop-app | <https://github.com/JHWH-L/jhwh-cyber-recon> |
| Jieyab89/OSINT-Cheat-sheet | api-service | <https://github.com/Jieyab89/OSINT-Cheat-sheet> |
| Jihashtag/osaa | framework | <https://github.com/Jihashtag/osaa> |
| jimen0/fdns | api-service | <https://github.com/jimen0/fdns> |
| JIMPL | tool | <https://jimpl.com/> |
| jishanthpapi/jish-aint-gay-we-catching-chethann-boii | api-service | <https://github.com/jishanthpapi/jish-aint-gay-we-catching-chethann-boii-> |
| jkctech/Flipper-Zero-Scripts | tool | <https://github.com/jkctech/Flipper-Zero-Scripts> |
| JoasASantos/Digital-Footprint-Checklist | tool | <https://github.com/JoasASantos/Digital-Footprint-Checklist> |
| Jobs (Poland) | tool | <https://www.jobs.pl> |
| Jobsite (UK) | tool | <https://www.jobsite.co.uk> |
| joda32/CertCrunchy | tool | <https://github.com/joda32/CertCrunchy> |
| Joe Sandbox | tool | <https://www.joesandbox.com> |
| Joe Sandbox | tool | <https://www.joesecurity.org/> |
| jofpin/trape | research-project | <https://github.com/jofpin/trape> |
| jollncoelho/Osint-Zhetikal-Master-toolkit-v2 | framework | <https://github.com/jollncoelho/Osint-Zhetikal-Master-toolkit-v2> |
| jollncoelho/OsintGodseye | api-service | <https://github.com/jollncoelho/OsintGodseye> |
| jonaylor89/facebook_totem | tool | <https://github.com/jonaylor89/facebook_totem> |
| jonaylor89/sherlock-rs | cli-tool | <https://github.com/jonaylor89/sherlock-rs> |
| jonaylor89/toutatis | tool | <https://github.com/jonaylor89/toutatis> |
| jonperk318/telegram-parsers | tool | <https://github.com/jonperk318/telegram-parsers> |
| jordanpotti/OffensiveCloudDistribution | tool | <https://github.com/jordanpotti/OffensiveCloudDistribution> |
| joshhighet/bebop | web-platform | <https://github.com/joshhighet/bebop> |
| JoshuaMart/AutoRecon | cli-tool | <https://github.com/JoshuaMart/AutoRecon> |
| Josue87/AnalyticsRelationships | tool | <https://github.com/Josue87/AnalyticsRelationships> |
| Josue87/EmailFinder | research-project | <https://github.com/Josue87/EmailFinder> |
| Josue87/MetaFinder | research-project | <https://github.com/Josue87/MetaFinder> |
| Journal Guide | dashboard | <https://www.journalguide.com> |
| Journal Seek | tool | <https://journalseek.net> |
| jp-220738/OsintInteractive | web-platform | <https://github.com/jp-220738/OsintInteractive> |
| JPEG Audit | tool | <https://jpegaudit.com> |
| JPEGsnoop | tool | <https://sourceforge.net/projects/jpegsnoop> |
| JpGraph | tool | <https://jpgraph.net> |
| jqPlot | plugin | <https://www.jqplot.com> |
| jsbin | tool | <https://Jsbin.com> |
| JSTOR | tool | <https://www.jstor.org> |
| juangjaguar/SubOracle | framework | <https://github.com/juangjaguar/SubOracle> |
| juanluDeveloper/OsintSpector | tool | <https://github.com/juanluDeveloper/OsintSpector> |
| Judyrecords | tool | <https://www.judyrecords.com/> |
| Junar | tool | <https://junar.com> |
| justdeleteme | tool | <https://justdelete.me> |
| justpaste | tool | <https://Justpaste.it> |
| K-Ecosystem/k-osint | framework | <https://github.com/K-Ecosystem/k-osint> |
| K2SOsint/K2SOsint | plugin | <https://github.com/K2SOsint/K2SOsint> |
| K2SOsint/Legendary_OSINT | tool | <https://github.com/K2SOsint/Legendary_OSINT> |
| K4N3CO-LABS/Lab-STAR | library | <https://github.com/K4N3CO-LABS/Lab-STAR> |
| kacakb/jsfinder | tool | <https://github.com/kacakb/jsfinder> |
| kaifcodec/phonsint | web-platform | <https://github.com/kaifcodec/phonsint> |
| kaifcodec/user-scanner | research-project | <https://github.com/kaifcodec/user-scanner> |
| kamehameha-ctrl/sniperscope | tool | <https://github.com/kamehameha-ctrl/sniperscope> |
| Kamerka | tool | <https://github.com/woj-ciech/Kamerka-GUI> |
| karim852/KUMO-Domain-Recon-Tool | plugin | <https://github.com/karim852/KUMO-Domain-Recon-Tool> |
| Karma Decay | tool | <http://karmadecay.com/> |
| karndeepbaror/traceintel | api-service | <https://github.com/karndeepbaror/traceintel> |
| KartaView | web-platform | <https://kartaview.org/> |
| KartaView | research-project | <https://kartaview.org/map/> |
| KartaVision | tool | <https://kartavision.com/> |
| Kartograph | research-project | <http://kartograph.org> |
| Kaspersky Cyberthreat live Map | tool | <https://cybermap.kaspersky.com/> |
| Katbin | tool | <https://katb.in> |
| KatrielMoses/MailAccess | api-service | <https://github.com/KatrielMoses/MailAccess> |
| KawaCoder/GhostRecon | framework | <https://github.com/KawaCoder/GhostRecon> |
| kawainime26/lacakdevbot | tool | <https://github.com/kawainime26/lacakdevbot> |
| KaylaTellier/SELFBOT-VTX | tool | <https://github.com/KaylaTellier/SELFBOT-VTX> |
| Kcisti/bat-security-toolkit | framework | <https://github.com/Kcisti/bat-security-toolkit> |
| KeePass Password Safe | tool | <https://keepass.info> |
| KELA | web-platform | <https://kelacyber.com> |
| kennbroorg/iKy | tool | <https://github.com/kennbroorg/iKy> |
| kernelstub/Nox | framework | <https://github.com/kernelstub/Nox> |
| kevtoe/worldview | web-platform | <https://github.com/kevtoe/worldview> |
| Keyword Discovery | research-project | <https://www.keyworddiscovery.com> |
| Keyword Spy | research-project | <https://www.keywordspy.com> |
| KeywordTool | research-project | <https://keywordtool.io> |
| kh4sh3i/smartrecon | cli-tool | <https://github.com/kh4sh3i/smartrecon> |
| khashashin/ogi | framework | <https://github.com/khashashin/ogi> |
| khast3x/Offensive-Dockerfiles | container | <https://github.com/khast3x/Offensive-Dockerfiles> |
| ki9mu/ARL-plus-docker | container | <https://github.com/ki9mu/ARL-plus-docker> |
| KiMiGuel/MeXiCOSINT | framework | <https://github.com/KiMiGuel/MeXiCOSINT> |
| Kirozaku/Wiwok | api-service | <https://github.com/Kirozaku/Wiwok> |
| Kismet | tool | <https://www.kismetwireless.net/> |
| Klear | tool | <https://klear.com> |
| klezVirus/vortex | framework | <https://github.com/klezVirus/vortex> |
| Kloth | research-project | <https://www.kloth.net/services> |
| knockpy | tool | <https://github.com/guelfoweb/knockpy> |
| Knoema | tool | <https://knoema.com> |
| knowem.com | tool | <https://knowem.com/> |
| Knowledge guide to international company registration | dashboard | <https://www.icaew.com/en/library/subject-gateways/business-management/company-administration/knowledge-guide-international-company-registration> |
| Knowledge-Wisdom-Understanding/recon | tool | <https://github.com/Knowledge-Wisdom-Understanding/recon> |
| ko2sec/apkizer | mobile-app | <https://github.com/ko2sec/apkizer> |
| koala73/worldmonitor | plugin | <https://github.com/koala73/worldmonitor> |
| koenrh/s3enum | tool | <https://github.com/koenrh/s3enum> |
| komomon/Komo | tool | <https://github.com/komomon/Komo> |
| Kompass | directory | <https://www.kompass.com> |
| kpcyrd/sn0int | framework | <https://github.com/kpcyrd/sn0int> |
| Krebs on Security | dataset | <https://krebsonsecurity.com/feed/> |
| Kribrum | tool | <https://kribrum.io/> |
| krishealty/worm | framework | <https://github.com/krishealty/worm> |
| krishpranav/vesper | cli-tool | <https://github.com/krishpranav/vesper> |
| krishpranav/wpscan | tool | <https://github.com/krishpranav/wpscan> |
| kristofhracza/hank | framework | <https://github.com/kristofhracza/hank> |
| KTZgraph/sarenka | container | <https://github.com/KTZgraph/sarenka> |
| Kubenew/Osint-Harvester | framework | <https://github.com/Kubenew/Osint-Harvester> |
| kunshdeep2812/reco | tool | <https://github.com/kunshdeep2812/reco> |
| l4rm4nd/LinkedInDumper | api-service | <https://github.com/l4rm4nd/LinkedInDumper> |
| Lacis | research-project | <https://c4seus.github.io/lacis/> |
| laitoxx/Laitoxx-Multi-Tool | dataset | <https://github.com/laitoxx/Laitoxx-Multi-Tool> |
| LandMatrix | tool | <https://landmatrix.org> |
| landoncrabtree/awesome-cyber | awesome-list | <https://github.com/landoncrabtree/awesome-cyber> |
| LASDovah/OSINT-Page | research-project | <https://github.com/LASDovah/OSINT-Page> |
| lastfm_monitor | web-platform | <https://github.com/misiektoja/lastfm_monitor> |
| Lastpass | tool | <https://lastpass.com> |
| Latinobarometro | tool | <https://www.latinobarometro.org> |
| laurabgularte/osint-framework | framework | <https://github.com/laurabgularte/osint-framework> |
| Lazy Scholar | tool | <http://www.lazyscholar.org> |
| lc/secretz | tool | <https://github.com/lc/secretz> |
| Leadrogue/Lanflux | tool | <https://github.com/Leadrogue/Lanflux> |
| Leaflet | library | <https://leafletjs.com> |
| Leak OSINT | tool | <https://telegram.me/Leak_SSINTbot> |
| Leak-Lookup | tool | <https://leak-lookup.com/> |
| LeakCheck | dataset | <https://leakcheck.io/> |
| leakcheck.net | tool | <https://leakcheck.net/> |
| Leakfarsi/Leakfa.com | tool | <https://github.com/Leakfarsi/Leakfa.com> |
| leakix.net | web-platform | <https://leakix.net/> |
| LeakRadar | tool | <https://leakradar.io/> |
| Leandro-SM/OSINT-BR | framework | <https://github.com/Leandro-SM/OSINT-BR> |
| LeetAnalytica/Overview | dataset | <https://github.com/LeetAnalytica/Overview> |
| Leibniz Information Centre For Science and Technology University Library | directory | <https://www.tib.eu/en/search-discover/> |
| Lekssays/shellfinder | cli-tool | <https://github.com/Lekssays/shellfinder> |
| Lenso.ai | tool | <https://lenso.ai> |
| Lenso.ai | tool | <https://lenso.ai/en> |
| leobeosab/sharingan | tool | <https://github.com/leobeosab/sharingan> |
| LERS Portal Directory (Ministry of Cyber Affairs) | directory | <https://ministryofcyberaffairs.com/lers> |
| lesma.eu | cli-tool | <https://lesma.eu/> |
| lesmes333/OSINT-Prototype | tool | <https://github.com/lesmes333/OSINT-Prototype> |
| letox4/OsintHunter | plugin | <https://github.com/letox4/OsintHunter> |
| leveryd-asm/asm | container | <https://github.com/leveryd-asm/asm> |
| Lexxrt/FireFly | tool | <https://github.com/Lexxrt/FireFly> |
| Lgutier9249/SNI-XHTTP-V1.1 | web-platform | <https://github.com/Lgutier9249/SNI-XHTTP-V1.1> |
| lhitori/Smog | framework | <https://github.com/lhitori/Smog> |
| Library of Congress: Ask a Librarian | library | <https://www.loc.gov/rr/askalib> |
| Library, University of Michigan: Statistics and Datasets | dataset | <https://www.lib.umich.edu/browse/Statistics%20and%20Data%20Sets> |
| LibreWolf | tool | <https://librewolf.net> |
| Licenseplates | directory | <http://www.worldlicenseplates.com/> |
| Lifka/hacking-resources | cli-tool | <https://github.com/Lifka/hacking-resources> |
| lina767/digital-war-room | api-service | <https://github.com/lina767/digital-war-room> |
| LinaYorda/OSINT-browser-extentions | browser-extension | <https://github.com/LinaYorda/OSINT-browser-extentions> |
| LinaYorda/osintkoSCR | tool | <https://github.com/LinaYorda/osintkoSCR> |
| LinkBase | tool | <https://link-base.org/> |
| Linkode(alpha) | tool | <https://linkode.org/> |
| LinkScope | web-platform | <https://accentusoft.com/> |
| LinkScope Client | cli-tool | <https://github.com/AccentuSoft/LinkScope_Client> |
| Linkuroius | tool | <https://linkurio.us> |
| Liodeus/swaggerHole | tool | <https://github.com/Liodeus/swaggerHole> |
| LIONIC Cyber Threat Map | tool | <https://www.lionic.com/monitoring/> |
| lissy93/web-check | tool | <https://github.com/lissy93/web-check> |
| List of Newspapers.com | research-project | <http://www.listofnewspapers.com> |
| Listify | tool | <https://listify.okfnlabs.org> |
| LittleSis | dataset | <https://littlesis.org/> |
| live demo | api-service | <https://whitebite.github.io/Domain-Hunter/> |
| Liveuamap | research-project | <https://liveuamap.com/> |
| LizardPope1101/osint-forge | plugin | <https://github.com/LizardPope1101/osint-forge> |
| lizTheDeveloper/flyover-scrub | tool | <https://github.com/lizTheDeveloper/flyover-scrub> |
| LocalFocus | tool | <https://www.localfocus.nl> |
| locallhosts/security-network-builder | api-service | <https://github.com/locallhosts/security-network-builder> |
| Lockbin | tool | <https://lockbin.com> |
| lockfale/OSINT-Framework | framework | <https://github.com/lockfale/OSINT-Framework> |
| Logibook | directory | <https://logibook.dataint.net> |
| Logpasta | web-platform | <https://logpasta.com/> |
| Lookup-ID.com | tool | <https://lookup-id.com> |
| lord-alfred/ipranges | tool | <https://github.com/lord-alfred/ipranges> |
| loseys/Oblivion | dashboard | <https://github.com/loseys/Oblivion> |
| lost-rob0t/quasar | framework | <https://github.com/lost-rob0t/quasar> |
| Lu1sDV/wafmeow | tool | <https://github.com/Lu1sDV/wafmeow> |
| Lucidchart | tool | <https://www.lucidchart.com> |
| Lucksi/Mr.Holmes | framework | <https://github.com/Lucksi/Mr.Holmes> |
| Lupovis/GetIPReputation | api-service | <https://github.com/Lupovis/GetIPReputation> |
| lutfizp/Number2Gram | framework | <https://github.com/lutfizp/Number2Gram> |
| Lycos | tool | <https://www.lycos.com> |
| Lycos Image Search | tool | <https://search.lycos.com> |
| Lydia-England/ncl-tools | tool | <https://github.com/Lydia-England/ncl-tools> |
| M0m0SMS-OSINT/Maltego | framework | <https://github.com/M0m0SMS-OSINT/Maltego> |
| m3n0sd0n4ld/GooFuzz | tool | <https://github.com/m3n0sd0n4ld/GooFuzz> |
| m3n0sd0n4ld/uDork | web-platform | <https://github.com/m3n0sd0n4ld/uDork> |
| m8sec/CrossLinked | api-service | <https://github.com/m8sec/CrossLinked> |
| m8sec/nullinux | tool | <https://github.com/m8sec/nullinux> |
| m8sec/subscraper | tool | <https://github.com/m8sec/subscraper> |
| m8sec/SubWalker | tool | <https://github.com/m8sec/SubWalker> |
| Macmod/goblob | tool | <https://github.com/Macmod/goblob> |
| MacTash/DorkForge | tool | <https://github.com/MacTash/DorkForge> |
| MagPortal | web-platform | <http://www.magportal.com> |
| Maigret OSINT bot | tool | <https://t.me/osint_maigret_bot> |
| Mail.Ru Social Network Search | tool | <https://go.mail.ru/search_social> |
| Mailbox | tool | <https://mailbox.org> |
| MailFinder | tool | <https://github.com/mishakorzik/MailFinder> |
| MailTester | tool | <https://mailtester.com> |
| Mailvelope | tool | <https://www.mailvelope.com> |
| Majestic | research-project | <https://majestic.com> |
| Malfrats/OSINT-Map | dashboard | <https://github.com/Malfrats/OSINT-Map> |
| Malfrats/xeuledoc | tool | <https://github.com/Malfrats/xeuledoc> |
| malikelnawawy3-arch/Telegram-OSINT-Toolkit | api-service | <https://github.com/malikelnawawy3-arch/Telegram-OSINT-Toolkit> |
| Malpedia | dataset | <https://malpedia.caad.fkie.fraunhofer.de/> |
| MalShare | tool | <https://malshare.com/> |
| Maltego | web-platform | <https://www.maltego.com/> |
| maltego-trx | library | <https://github.com/MaltegoTech/maltego-trx> |
| Maltiverse | api-service | <https://maltiverse.com/> |
| MalwareBazaar | tool | <https://bazaar.abuse.ch/browse/> |
| malwaredojo/IntelBox | framework | <https://github.com/malwaredojo/IntelBox> |
| malwaredojo/loki | framework | <https://github.com/malwaredojo/loki> |
| Mamik11/Osinweb | framework | <https://github.com/Mamik11/Osinweb> |
| Mamont | tool | <https://www.mmnt.ru/> |
| Mandiant Advantage | web-platform | <https://www.mandiant.com/advantage> |
| mantisfury/ArkhamMirror | container | <https://github.com/mantisfury/ArkhamMirror> |
| Map Maker | research-project | <https://maps.co> |
| MapAList | research-project | <https://mapalist.com> |
| MapBox | research-project | <https://www.mapbox.com> |
| Mapchart.net | research-project | <https://mapchart.net> |
| MapChecking | research-project | <https://www.mapchecking.com/> |
| mapcidr | tool | <https://github.com/projectdiscovery/mapcidr> |
| Maperitive | research-project | <http://maperitive.net> |
| MapHub | research-project | <https://maphub.net> |
| Mapillary | api-service | <https://www.mapillary.com/> |
| Mapillary | api-service | <https://www.mapillary.com/app/> |
| MapJam | research-project | <https://mapjam.com> |
| Mapline | research-project | <https://mapline.com> |
| Mapquest | research-project | <https://www.mapquest.com> |
| marc-shade/world-intel-mcp | api-service | <https://github.com/marc-shade/world-intel-mcp> |
| marcolivierbouch/dirbpy | tool | <https://github.com/marcolivierbouch/dirbpy> |
| MarineTraffic | web-platform | <https://www.marinetraffic.com/> |
| Mark Monitor WHOIS | research-project | <https://whois-webform.markmonitor.com/whois/> |
| massdns | tool | <https://github.com/blechschmidt/massdns> |
| Master Password | tool | <https://masterpasswordapp.com> |
| matamorphosis/Scrummage | dashboard | <https://github.com/matamorphosis/Scrummage> |
| mateofumis/dumpdork | framework | <https://github.com/mateofumis/dumpdork> |
| mathis2001/Cert4Recon | tool | <https://github.com/mathis2001/Cert4Recon> |
| mathis2001/WebHackUrls | tool | <https://github.com/mathis2001/WebHackUrls> |
| MattMoony/d4v1d | web-platform | <https://github.com/MattMoony/d4v1d> |
| MattMoony/t0m | api-service | <https://github.com/MattMoony/t0m> |
| mattwright324/youtube-comment-suite | api-service | <https://github.com/mattwright324/youtube-comment-suite> |
| mattwright324/youtube-metadata | api-service | <https://github.com/mattwright324/youtube-metadata> |
| Maven | tool | <https://www.maven.co> |
| Maxar | research-project | <https://discover.digitalglobe.com/> |
| Maxar Open Data | tool | <https://vantor.com/company/open-data-program> |
| maxar.com | tool | <https://maxar.com/> |
| MaxMind | dataset | <https://www.maxmind.com> |
| Maxthon | tool | <https://www.maxthon.com> |
| Maxwell747/OSINT-OCTOPUS | dashboard | <https://github.com/Maxwell747/OSINT-OCTOPUS> |
| may215/awesome-termux-hacking | awesome-list | <https://github.com/may215/awesome-termux-hacking> |
| mbrg/zapcreds | api-service | <https://github.com/mbrg/zapcreds> |
| mdhama/lazyshot | tool | <https://github.com/mdhama/lazyshot> |
| MDHD99/ContactHoundOSINT | framework | <https://github.com/MDHD99/ContactHoundOSINT> |
| meanii/Search4 | tool | <https://github.com/meanii/Search4> |
| Meawfy | directory | <https://meawfy.com/> |
| megadose/cqfd | tool | <https://github.com/megadose/cqfd> |
| megadose/cqfd-maltego | tool | <https://github.com/megadose/cqfd-maltego> |
| megadose/facebook_totem | tool | <https://github.com/megadose/facebook_totem> |
| megadose/Fl0wj0b | tool | <https://github.com/megadose/Fl0wj0b> |
| megadose/holehe | tool | <https://github.com/megadose/holehe> |
| megadose/holehe-maltego | tool | <https://github.com/megadose/holehe-maltego> |
| megadose/hunter-maltego | tool | <https://github.com/megadose/hunter-maltego> |
| megadose/ignorant | tool | <https://github.com/megadose/ignorant> |
| megadose/nqntnqnqmb | tool | <https://github.com/megadose/nqntnqnqmb> |
| megadose/nqntnqnqmb-maltego | tool | <https://github.com/megadose/nqntnqnqmb-maltego> |
| megadose/OnionSearch | tool | <https://github.com/megadose/OnionSearch> |
| megadose/phoneinfoga-maltego | tool | <https://github.com/megadose/phoneinfoga-maltego> |
| megadose/Quidam | tool | <https://github.com/megadose/Quidam> |
| megadose/quidam-maltego | tool | <https://github.com/megadose/quidam-maltego> |
| megadose/totem-maltego | tool | <https://github.com/megadose/totem-maltego> |
| megadose/toutatis | tool | <https://github.com/megadose/toutatis> |
| megadose/toutatis-maltego | tool | <https://github.com/megadose/toutatis-maltego> |
| MehmetYukselSekeroglu/eye_of_web | tool | <https://github.com/MehmetYukselSekeroglu/eye_of_web> |
| melbadry9/ScanApi | api-service | <https://github.com/melbadry9/ScanApi> |
| melbadry9/WhoEnum | tool | <https://github.com/melbadry9/WhoEnum> |
| Memento Time Travel | tool | <https://timetravel.mementoweb.org> |
| memoryswordsmanlaud/fieldkit-awesome-osint-list | awesome-list | <https://github.com/memoryswordsmanlaud/fieldkit-awesome-osint-list> |
| mempool.space | tool | <https://mempool.space> |
| Mention | tool | <https://en.mention.com> |
| mention.com | tool | <https://mention.com/> |
| Mergent Intellect | research-project | <https://www.mergentintellect.com> |
| Mergent Online | research-project | <https://www.mergentonline.com/login.php> |
| Merklemap | tool | <https://www.merklemap.com/> |
| Metacafe | tool | <http://www.metacafe.com> |
| MetaClean | desktop-app | <https://github.com/Moresyl/metaclean> |
| Metadata Viewer | tool | <https://kriztalz.sh/metadata-viewer/> |
| MetaDefender | web-platform | <https://metadefender.com> |
| Metagoofil | tool | <https://github.com/laramies/metagoofil> |
| MetaOSINT/MetaOSINT.github.io | research-project | <https://github.com/MetaOSINT/MetaOSINT.github.io> |
| metascion/GallantWarrior | plugin | <https://github.com/metascion/GallantWarrior> |
| MetaSleuth | tool | <https://metasleuth.io> |
| Metasploitable | tool | <https://docs.rapid7.com/metasploit/metasploitable-2/> |
| Metatube | tool | <https://www.metatube.com> |
| mhmdiaa/chronos | framework | <https://github.com/mhmdiaa/chronos> |
| mhmdiaa/second-order | tool | <https://github.com/mhmdiaa/second-order> |
| mhmdiaa/waybackrobots | tool | <https://github.com/mhmdiaa/waybackrobots> |
| michalstankiewicz4-cell/IPscanner | cli-tool | <https://github.com/michalstankiewicz4-cell/IPscanner> |
| michenriksen/aquatone | research-project | <https://github.com/michenriksen/aquatone> |
| michenriksen/birdwatcher | api-service | <https://github.com/michenriksen/birdwatcher> |
| michenriksen/gitrob | api-service | <https://github.com/michenriksen/gitrob> |
| Microsoft Academic | tool | <https://academic.research.microsoft.com> |
| midoxnet/mapperplus | tool | <https://github.com/midoxnet/mapperplus> |
| MikeMeliz/TorCrawl.py | tool | <https://github.com/MikeMeliz/TorCrawl.py> |
| Million Short | tool | <https://millionshort.com> |
| Minerva OSINT | tool | <https://minervaosint.com> |
| mishakorzik/ReconCat | tool | <https://github.com/mishakorzik/ReconCat> |
| misiektoja/instagram_monitor | container | <https://github.com/misiektoja/instagram_monitor> |
| MISP | web-platform | <https://www.misp-project.org/> |
| MISP Galaxy | tool | <https://www.misp-galaxy.org> |
| MISP/misp-training | tool | <https://github.com/MISP/misp-training> |
| MistTrack | tool | <https://misttrack.io> |
| mitchmoser/sputnik | browser-extension | <https://github.com/mitchmoser/sputnik> |
| MITRE ATT&CK | tool | <https://attack.mitre.org> |
| MITRE D3FEND | tool | <https://d3fend.mitre.org> |
| mixaoc/Osint-Sync | plugin | <https://github.com/mixaoc/Osint-Sync> |
| Mixi (Japan) | tool | <https://mixi.jp> |
| mmpx12/xenv | tool | <https://github.com/mmpx12/xenv> |
| mmuhacker/mud-enc | cli-tool | <https://github.com/mmuhacker/mud-enc> |
| Mnemonic Passive DNS | tool | <https://passivedns.mnemonic.no> |
| mnp_bot | tool | <https://t.me/mnp_bot> |
| Modest Maps | research-project | <https://modestmaps.com> |
| modhopm3982/md5-hashtray | tool | <https://github.com/modhopm3982/md5-hashtray> |
| Mohamad-Mortada/Osintgram | api-service | <https://github.com/Mohamad-Mortada/Osintgram> |
| Mojeek | tool | <https://www.mojeek.com/> |
| momenbasel/gorobots | tool | <https://github.com/momenbasel/gorobots> |
| momenbasel/keyFinder | browser-extension | <https://github.com/momenbasel/keyFinder> |
| Monster | tool | <https://www.monster.com> |
| montysecurity/C2-Tracker | dataset | <https://github.com/montysecurity/C2-Tracker> |
| MorDavid/NetworksDB-MCP | plugin | <https://github.com/MorDavid/NetworksDB-MCP> |
| morganegautier/osint-starter | tool | <https://github.com/morganegautier/osint-starter> |
| mosadov/Astrym | api-service | <https://github.com/mosadov/Astrym> |
| moscovium-mc/CloudRip | tool | <https://github.com/moscovium-mc/CloudRip> |
| Mostly Harmless | tool | <https://kerrick.github.io/Mostly-Harmless/#features> |
| MotherSearchBot | tool | <https://t.me/MotherSearchBot> |
| Mozilla HTTP Observatory | tool | <https://developer.mozilla.org/en-US/observatory> |
| Mr-Destroyer/ZimZilla | tool | <https://github.com/Mr-Destroyer/ZimZilla> |
| Mr-Pstar7/NIK-checker | tool | <https://github.com/Mr-Pstar7/NIK-checker> |
| Mr-Pstar7/osint-ig | tool | <https://github.com/Mr-Pstar7/osint-ig> |
| MrCl0wnLab/SimpleReconSubdomain | tool | <https://github.com/MrCl0wnLab/SimpleReconSubdomain> |
| mrco24/PH-Recon | tool | <https://github.com/mrco24/PH-Recon> |
| MrGodLink/OSINT-Tracker | web-platform | <https://github.com/MrGodLink/OSINT-Tracker> |
| MrHacker-X/specter-osint | dashboard | <https://github.com/MrHacker-X/specter-osint> |
| mridun-gupta/sitrep | dataset | <https://github.com/mridun-gupta/sitrep> |
| mrofcodyx/gxsuid | dataset | <https://github.com/mrofcodyx/gxsuid> |
| mrofcodyx/sporTracker | research-project | <https://github.com/mrofcodyx/sporTracker> |
| MrTuxx/SocialPwned | api-service | <https://github.com/MrTuxx/SocialPwned> |
| mrvcoder/Bug-Hunting-methodologies | tool | <https://github.com/mrvcoder/Bug-Hunting-methodologies> |
| mrvcoder/cloud_data | tool | <https://github.com/mrvcoder/cloud_data> |
| mrvcoder/GetASN | cli-tool | <https://github.com/mrvcoder/GetASN> |
| MrX0955/SecurityNexus | plugin | <https://github.com/MrX0955/SecurityNexus> |
| mschwager/gitem | tool | <https://github.com/mschwager/gitem> |
| mswell/burnrecon | tool | <https://github.com/mswell/burnrecon> |
| MtamVP/Dupin | tool | <https://github.com/MtamVP/Dupin> |
| MuckRack | dataset | <https://muckrack.com> |
| Mugshots | tool | <https://mugshots.com/> |
| muhammadwali0/d0rkw3b | framework | <https://github.com/muhammadwali0/d0rkw3b> |
| Muhib-Mehdi/OSINT-NEXUS | api-service | <https://github.com/Muhib-Mehdi/OSINT-NEXUS> |
| mukul975/Anthropic-Cybersecurity-Skills | web-platform | <https://github.com/mukul975/Anthropic-Cybersecurity-Skills> |
| Mullvad Browser | tool | <https://mullvad.net/en/browser> |
| Multirbl | tool | <https://multirbl.valli.org/dnsbl-lookup> |
| MustBePresent | tool | <https://mustbepresent.com> |
| mvanhorn/last30days-skill | plugin | <https://github.com/mvanhorn/last30days-skill> |
| mwakidenis/WebCheck-OSINT | container | <https://github.com/mwakidenis/WebCheck-OSINT> |
| mxrch/GHunt | framework | <https://github.com/mxrch/GHunt> |
| mxrch/GitFive | tool | <https://github.com/mxrch/GitFive> |
| Myallsearch | tool | <https://www.myallsearch.com> |
| Mylnikov Geolocation | tool | <https://www.mylnikov.org> |
| MyTweetAlerts | tool | <https://www.mytweetalerts.com/> |
| n0kovo/DomainDouche | api-service | <https://github.com/n0kovo/DomainDouche> |
| n0kovo/fb_friend_list_scraper | api-service | <https://github.com/n0kovo/fb_friend_list_scraper> |
| n0kovo/gohashmob | api-service | <https://github.com/n0kovo/gohashmob> |
| n0kovo/n0kovo_subdomains | tool | <https://github.com/n0kovo/n0kovo_subdomains> |
| n0paste | tool | <https://n0paste.eu/> |
| N0rz3/Eyes | cli-tool | <https://github.com/N0rz3/Eyes> |
| N0rz3/GitSint | tool | <https://github.com/N0rz3/GitSint> |
| N0rz3/Inspector | tool | <https://github.com/N0rz3/Inspector> |
| N0rz3/Phunter | tool | <https://github.com/N0rz3/Phunter> |
| N0rz3/TraxOsint | tool | <https://github.com/N0rz3/TraxOsint> |
| N0rz3/Zehef | tool | <https://github.com/N0rz3/Zehef> |
| n11xY/n1xYosint | plugin | <https://github.com/n11xY/n1xYosint> |
| N1ckw1ck/Clear_OSINT | api-service | <https://github.com/N1ckw1ck/Clear_OSINT> |
| n3tph4t0m/stegscope | tool | <https://github.com/n3tph4t0m/stegscope> |
| Nab6eel/UPI-AND-OSINT | framework | <https://github.com/Nab6eel/UPI-AND-OSINT> |
| Nachricht | web-platform | <https://nachricht.co/> |
| Najdi (Slovenia) | tool | <https://www.najdi.si> |
| Name Checkr | web-platform | <http://www.namecheckr.com> |
| Name Checkup | tool | <https://namecheckup.com> |
| Name Chk | web-platform | <https://www.namechk.com> |
| NameKetchup | web-platform | <https://nameketchup.com> |
| Nansen | tool | <https://nansen.ai> |
| NAPALM FTP Indexer | directory | <https://www.searchftps.net/> |
| NarcoScope | tool | <https://narcoscope.com> |
| NASA Worldview | tool | <https://worldview.earthdata.nasa.gov/> |
| Nation Master | tool | <https://www.nationmaster.com/statistics> |
| National Company Registers | research-project | <https://en.wikipedia.org/wiki/List_of_company_registers> |
| National Speakers Association | tool | <https://www.nsaspeaker.org> |
| nationalcellulardirectory.com | directory | <https://www.nationalcellulardirectory.com/> |
| natlas/natlas | tool | <https://github.com/natlas/natlas> |
| Naukri (India) | tool | <https://www.naukri.com> |
| Naver (South Korea) | tool | <https://www.naver.com> |
| ne2ro/data-osinthub | tool | <https://github.com/ne2ro/data-osinthub> |
| nebaz.ru | tool | <https://nebaz.ru/> |
| Neeshant01/nee-osint | framework | <https://github.com/Neeshant01/nee-osint> |
| nekobin | tool | <https://nekobin.com/> |
| neospl0it/osint-bookmark | awesome-list | <https://github.com/neospl0it/osint-bookmark> |
| NerdyData | tool | <https://nerdydata.com> |
| Netcraft Site Report | web-platform | <https://sitereport.netcraft.com> |
| Netcraft Site Report | dataset | <https://toolbar.netcraft.com/site_report?url=undefined#last_reboot> |
| Netlas Cookbook | tool | <https://academy.netlas.io> |
| netlas-io/netlas-cookbook | awesome-list | <https://github.com/netlas-io/netlas-cookbook> |
| netlas-io/netlas-dorks | tool | <https://github.com/netlas-io/netlas-dorks> |
| Netlas.io | tool | <https://app.netlas.io/> |
| Netlas.io | tool | <https://netlas.io/> |
| netrixone/udig | tool | <https://github.com/netrixone/udig> |
| NETSCOUT Cyber Threat Map | tool | <https://horizon.netscout.com/> |
| netsecurity-as/recon365 | directory | <https://github.com/netsecurity-as/recon365> |
| netstalking-core/netstalking-catalogue | directory | <https://github.com/netstalking-core/netstalking-catalogue> |
| netstalking-core/netstalking-osint | tool | <https://github.com/netstalking-core/netstalking-osint> |
| Netvibes | tool | <https://www.netvibes.com> |
| NEUROAUTOSEARCH | tool | <https://t.me/noblackAuto_bot> |
| New Paste | tool | <https://paste1.com/> |
| News Map | tool | <http://newsmap.jp> |
| News Now | tool | <https://www.newsnow.co.uk> |
| News360 | tool | <https://news360.com> |
| Newsblur | tool | <https://newsblur.com> |
| NewsBot | tool | <https://getnewsbot.com> |
| Newseum - Today Front Pages | tool | <https://www.newseum.org/todaysfrontpages> |
| Newsinshorts | tool | <https://newsinshorts.com> |
| Newslink | tool | <http://www.newslink.org> |
| NewsLookup | tool | <http://www.newslookup.com> |
| Newspaper Map | research-project | <https://newspapermap.com> |
| Newspaperindex | directory | <http://www.newspaperindex.com> |
| Newspapers.com | research-project | <https://www.newspapers.com> |
| NewsWhip | tool | <https://www.newswhip.com> |
| Newswise | tool | <https://www.newswise.com> |
| nextcorebdofficial/osint-hub | api-service | <https://github.com/nextcorebdofficial/osint-hub> |
| nextplay-box/Nextplay-box | tool | <https://github.com/nextplay-box/Nextplay-box> |
| Nhoya/gOSINT | api-service | <https://github.com/Nhoya/gOSINT> |
| ni5arga/apipie | api-service | <https://github.com/ni5arga/apipie> |
| ni5arga/deanonymizer | cli-tool | <https://github.com/ni5arga/deanonymizer> |
| ni5arga/sightline | api-service | <https://github.com/ni5arga/sightline> |
| nicb.org/vincheck | tool | <https://www.nicb.org/vincheck> |
| Nidhzz1005/DigitalFootprint | api-service | <https://github.com/Nidhzz1005/DigitalFootprint> |
| nielsing/yar | tool | <https://github.com/nielsing/yar> |
| Nighthawk | tool | <https://www.mdsec.co.uk/nighthawk/> |
| Nighty3098/SkyFall | framework | <https://github.com/Nighty3098/SkyFall> |
| Nikhilbharti284/NexusOSINT | api-service | <https://github.com/Nikhilbharti284/NexusOSINT> |
| nil0x42/dnsanity | tool | <https://github.com/nil0x42/dnsanity> |
| Ning | tool | <https://www.ning.com> |
| Ninja-Yubaraj/FireFly-v2 | framework | <https://github.com/Ninja-Yubaraj/FireFly-v2> |
| ninoseki/mihari | tool | <https://github.com/ninoseki/mihari> |
| ninoseki/mitaka | browser-extension | <https://github.com/ninoseki/mitaka> |
| nishu2402/HEAVEN-GeoIntel | web-platform | <https://github.com/nishu2402/HEAVEN-GeoIntel> |
| nitefood/asn | api-service | <https://github.com/nitefood/asn> |
| nitkinov/HunterA2 | plugin | <https://github.com/nitkinov/HunterA2> |
| NixIntel | tool | <https://nixintel.info/> |
| nixintel/o365chk | tool | <https://github.com/nixintel/o365chk> |
| Nixory | tool | <https://nixory.sourceforge.net> |
| noarche/ezOSINT | cli-tool | <https://github.com/noarche/ezOSINT> |
| NoblerWorks-HQ/IRONSIGHT | api-service | <https://github.com/NoblerWorks-HQ/IRONSIGHT> |
| Nod | tool | <https://get-nod.com> |
| Nodebox | tool | <https://www.nodebox.net> |
| Nominatim | tool | <https://github.com/osm-search/Nominatim> |
| noobgameur/Meta-Detect | api-service | <https://github.com/noobgameur/Meta-Detect> |
| NoPaste | tool | <https://nopaste.boris.sh/> |
| nopaste.net | cli-tool | <https://nopaste.net/> |
| North Data | tool | <https://www.northdata.com/> |
| NoScript | tool | <https://noscript.net> |
| Notablist | research-project | <https://www.notablist.com> |
| notebooklm.google.com | research-project | <https://notebooklm.google.com/> |
| Notes | tool | <https://notes.io/> |
| Notey | tool | <https://www.notey.com> |
| NotLoBi/NotLoBi | framework | <https://github.com/NotLoBi/NotLoBi> |
| novitae/sterraxcyl | research-project | <https://github.com/novitae/sterraxcyl> |
| nox-project/nox-framework | framework | <https://github.com/nox-project/nox-framework> |
| NPCmillionaire/super-awesome-tools-list | awesome-list | <https://github.com/NPCmillionaire/super-awesome-tools-list> |
| NRC Research Press | research-project | <https://www.nrcresearchpress.com> |
| nsa.gov | web-platform | <https://nsa.gov/> |
| NullArray/DorkNet | web-platform | <https://github.com/NullArray/DorkNet> |
| NullArray/IntRec-Pack | tool | <https://github.com/NullArray/IntRec-Pack> |
| nullt3r/jfscan | web-platform | <https://github.com/nullt3r/jfscan> |
| numbpill3d/cardputer-adv-diviner | web-platform | <https://github.com/numbpill3d/cardputer-adv-diviner> |
| nyxgeek/onedrive_user_enum | tool | <https://github.com/nyxgeek/onedrive_user_enum> |
| OA.mg | directory | <https://oa.mg> |
| oasm-platform/open-asm | web-platform | <https://github.com/oasm-platform/open-asm> |
| obitouka/InstagramPrivSniffer | awesome-list | <https://github.com/obitouka/InstagramPrivSniffer> |
| Observable | tool | <https://observablehq.com/> |
| Obsidian | tool | <https://obsidian.md> |
| OCCRP Aleph | dataset | <https://aleph.occrp.org/> |
| octo8-debug/xurl | tool | <https://github.com/octo8-debug/xurl> |
| Octosuite | framework | <https://github.com/bellingcat/octosuite> |
| ODCrawler | tool | <https://odcrawler.xyz/> |
| ODIN | tool | <https://search.odin.io/> |
| Odnoklassniki (Russia) | tool | <https://ok.ru> |
| OECD Aid Database | dataset | <https://www.oecd.org/dac/stats/data.htm> |
| OECD Data | tool | <https://data.oecd.org> |
| OECD Factbook | tool | <https://www.oecd-ilibrary.org/economics/oecd-factbook_18147364> |
| OffcierCia/non-typical-OSINT-guide | awesome-list | <https://github.com/OffcierCia/non-typical-OSINT-guide> |
| Offendersearch | api-service | <https://offendersearch.app> |
| Offensive-terseness86/BlackHoleTrash | cli-tool | <https://github.com/Offensive-terseness86/BlackHoleTrash> |
| Offliberty | tool | <http://offliberty.com> |
| OffSec Proving Grounds | tool | <https://www.offsec.com/labs/individual/> |
| offseq/threadsrecon | tool | <https://github.com/offseq/threadsrecon> |
| Offshore Leak Database | dataset | <https://offshoreleaks.icij.org> |
| OffShore.cat | web-platform | <https://offshore.cat/?page=vpn> |
| OffShore.cat | web-platform | <https://offshore.cat/vpn> |
| ogel4s/Evolvement | tool | <https://github.com/ogel4s/Evolvement> |
| OhShINT/ohshint.gitbook.io | tool | <https://github.com/OhShINT/ohshint.gitbook.io> |
| ohsusannamarie/bookmarklet-os | framework | <https://github.com/ohsusannamarie/bookmarklet-os> |
| OKLink | dashboard | <https://www.oklink.com> |
| okpulse/osint-stividor | tool | <https://github.com/okpulse/osint-stividor> |
| OkSearch | tool | <https://telegram.me/OkSearchBot> |
| Olaowo5/Ola_Osint | api-service | <https://github.com/Olaowo5/Ola_Osint> |
| Oldcircle/geo-sleuth | cli-tool | <https://github.com/Oldcircle/geo-sleuth> |
| oldkingcone/SpyGlass | api-service | <https://github.com/oldkingcone/SpyGlass> |
| olizimmermann/s3dns | tool | <https://github.com/olizimmermann/s3dns> |
| OmeaReader | tool | <https://www.jetbrains.com/omea/reader> |
| omkarcloud/adobe-stock-scraper | api-service | <https://github.com/omkarcloud/adobe-stock-scraper> |
| omkarcloud/google-images-scraper | api-service | <https://github.com/omkarcloud/google-images-scraper> |
| omkarcloud/instagram-scraper | api-service | <https://github.com/omkarcloud/instagram-scraper> |
| omkarcloud/mobile-de-scraper | api-service | <https://github.com/omkarcloud/mobile-de-scraper> |
| omkarcloud/tiktok-scraper | api-service | <https://github.com/omkarcloud/tiktok-scraper> |
| omoika-institute/framework | plugin | <https://github.com/omoika-institute/framework> |
| omoika-institute/omoika | plugin | <https://github.com/omoika-institute/omoika> |
| One Look Reverse Dictionary | research-project | <https://www.onelook.com/reverse-dictionary.shtml> |
| OneMillionTweetMap | tool | <http://onemilliontweetmap.com> |
| Onet.pl (Poland) | tool | <https://www.onet.pl> |
| onhexgroup/Awesome-Search-Engines-for-Cybersecurity-Researchers | awesome-list | <https://github.com/onhexgroup/Awesome-Search-Engines-for-Cybersecurity-Researchers> |
| onhexgroup/Conferences | tool | <https://github.com/onhexgroup/Conferences> |
| onionbag2/osint-tools | awesome-list | <https://github.com/onionbag2/osint-tools> |
| OnionLand Search | tool | <https://onionlandsearchengine.com> |
| OnlineNewspapers | research-project | <https://www.onlinenewspapers.com> |
| OnlyF0uR/ClioSec | framework | <https://github.com/OnlyF0uR/ClioSec> |
| OnWebChange | tool | <https://onwebchange.com> |
| ONYPHE | directory | <https://search.onyphe.io/> |
| Onyphe | tool | <https://www.onyphe.io/> |
| Open Access Scientific Journals | tool | <https://www.pagepress.org> |
| Open Data Network | tool | <http://www.opendatanetwork.com> |
| Open DNS | tool | <https://www.opendns.com/home-internet-security> |
| Open Grey | tool | <https://www.opengrey.eu> |
| Open PGP | tool | <https://www.enigmail.net/index.php/en> |
| Open Site Explorer | research-project | <https://moz.com/researchtools/ose> |
| Open Street Map | research-project | <https://www.openstreetmap.org> |
| open-source | tool | <https://github.com/Berchez/OSINT-steam> |
| Open-source intelligence (OSINT) | awesome-list | <https://en.wikipedia.org/wiki/Open-source_intelligence> |
| Open-Source Intelligence (Reverse Image) | tool | <https://oosint.com> |
| OpenAerialMap | tool | <https://openaerialmap.org/> |
| OpenALPR | library | <https://github.com/openalpr/openalpr> |
| OpenCellID | dataset | <https://opencellid.org> |
| OpenCorporates | research-project | <https://opencorporates.com> |
| OpenDataUABot | tool | <https://t.me/OpenDataUABot> |
| OpenLayers | library | <https://openlayers.org> |
| OpenLeads | api-service | <https://github.com/Samyrrrrrr990/openleads> |
| OpenLinkProfiler | research-project | <https://www.openlinkprofiler.org/> |
| OPENLOAD Bot | tool | <https://t.me/OPENLOADTOPBOT> |
| OpenOSINT/OpenOSINT | plugin | <https://github.com/OpenOSINT/OpenOSINT> |
| OpenOwnership Register | research-project | <https://register.openownership.org/> |
| OpenPhish | dataset | <https://openphish.com> |
| OpenRailwayMap | tool | <https://www.openrailwaymap.org/> |
| OpenSanctions | api-service | <https://www.opensanctions.org/> |
| OpenSanctions | tool | <https://www.opensanctions.org/search/> |
| opensemanticsearch/open-semantic-search | web-platform | <https://github.com/opensemanticsearch/open-semantic-search> |
| OpenSky Network | api-service | <https://opensky-network.org/> |
| Opera | tool | <https://www.opera.com> |
| OpinionCrawl | tool | <https://www.opinioncrawl.com> |
| opsdisk/metagoofil | tool | <https://github.com/opsdisk/metagoofil> |
| opsdisk/pagodo | api-service | <https://github.com/opsdisk/pagodo> |
| ORA | tool | <http://www.casos.cs.cmu.edu/projects/ora/software.php> |
| ORA-LITE | tool | <https://www.cmu.edu/casos-center/research/tools/> |
| Orange (France) | tool | <https://www.orange.fr> |
| Orbis directory | directory | <http://orbisdirectory.bvdinfo.com/version-20161014/OrbisDirectory/Companies> |
| orgobversary/robinshood | framework | <https://github.com/orgobversary/robinshood> |
| Oscobo Search Engine | tool | <https://oscobo.co.uk> |
| OSINT Ambition Publication | tool | <https://publication.osintambition.org/> |
| OSINT Belarus | tool | <https://t.me/s/osintby> |
| OSINT Combine Blog | dataset | <https://www.osintcombine.com/blog-feed.xml> |
| OSINT Dojo | tool | <https://www.osintdojo.com/resources/> |
| OSINT Framework | directory | <https://osintframework.com/> |
| OSINT Team | tool | <https://www.osintteam.com/> |
| OSINT Techniques | tool | <https://www.osinttechniques.com/blog> |
| OSINT Tools and Resources Handbook | tool | <https://www.i-intelligence.eu/open-source-intelligence-tools-and-resources-handbook/> |
| OSINT Updates - a free weekly newsletter for OSINTers | tool | <https://osintupdates.com/> |
| osint-dev-team/osint-framework | container | <https://github.com/osint-dev-team/osint-framework> |
| OSINT-Experts-Society/Consensus-OSINT | cli-tool | <https://github.com/OSINT-Experts-Society/Consensus-OSINT> |
| osint-poisk-bot/osint-bot | tool | <https://github.com/osint-poisk-bot/osint-bot> |
| osint-poisk-bot/osint-catalog | awesome-list | <https://github.com/osint-poisk-bot/osint-catalog> |
| osint-poisk-bot/osint-framework | framework | <https://github.com/osint-poisk-bot/osint-framework> |
| osint-poisk-bot/osint-instrumenty | tool | <https://github.com/osint-poisk-bot/osint-instrumenty> |
| osint-recon | framework | <https://github.com/JMarchiori13/osint-recon> |
| OSINT-SPY | framework | <https://github.com/SharadKumar97/OSINT-SPY> |
| OSINT-Steam | tool | <https://osint-steam.vercel.app/en> |
| OSINT-TECHNOLOGIES/dpulse | api-service | <https://github.com/OSINT-TECHNOLOGIES/dpulse> |
| OSINT-Tool | browser-extension | <https://www.osint-tool.com/> |
| OSINT-Trace/Social-Media-Checker | api-service | <https://github.com/OSINT-Trace/Social-Media-Checker> |
| osint.industries | tool | <https://www.osint.industries/> |
| OSINT.SH | tool | <https://osint.sh/> |
| osintambition/Awesome-Browser-Extensions-for-OSINT | awesome-list | <https://github.com/osintambition/Awesome-Browser-Extensions-for-OSINT> |
| osintario/osintario.github.io | awesome-list | <https://github.com/osintario/osintario.github.io> |
| osintbrazuca/osint-brazuca | tool | <https://github.com/osintbrazuca/osint-brazuca> |
| osintbrazuca/osint-brazuca-regex | tool | <https://github.com/osintbrazuca/osint-brazuca-regex> |
| osintbrazuca/SimpleReconDorking | tool | <https://github.com/osintbrazuca/SimpleReconDorking> |
| osintbuddy/osintbuddy | desktop-app | <https://github.com/osintbuddy/osintbuddy> |
| OSINTCabal/Cabal-Link-Thief | tool | <https://github.com/OSINTCabal/Cabal-Link-Thief> |
| OSINTCabal/Contact-Analyzer | tool | <https://github.com/OSINTCabal/Contact-Analyzer> |
| OSINTCabal/DeepSearch | plugin | <https://github.com/OSINTCabal/DeepSearch> |
| OsintCat | api-service | <https://www.osintcat.net/> |
| OSINTCurious | tool | <https://osintcurio.us/> |
| osintdojo.com | web-platform | <https://osintdojo.com/> |
| OSINTEye | desktop-app | <https://github.com/atiilla/OsintEye> |
| Osintgraph | tool | <https://github.com/XD-MHLOO/Osintgraph> |
| Osintkit | tool | <https://t.me/osintkit_check_bot> |
| OsintNET/osintnet-public | web-platform | <https://github.com/OsintNET/osintnet-public> |
| OSINTNova | web-platform | <https://app.osintnova.com/> |
| osintrack.com | tool | <https://osintrack.com/> |
| OSINTResearch/osintresearch.github.io | framework | <https://github.com/OSINTResearch/osintresearch.github.io> |
| OSINTResourcesHub/engine | framework | <https://github.com/OSINTResourcesHub/engine> |
| OSINTResourcesHub/osintresourceshub.github.io | framework | <https://github.com/OSINTResourcesHub/osintresourceshub.github.io> |
| osintshifu/awesome-osint-repos | awesome-list | <https://github.com/osintshifu/awesome-osint-repos> |
| osintshifu/Cyber-Intelligence-GPT | framework | <https://github.com/osintshifu/Cyber-Intelligence-GPT> |
| osintshifu/osint-tradecraft | framework | <https://github.com/osintshifu/osint-tradecraft> |
| osintshifu/querytool | framework | <https://github.com/osintshifu/querytool> |
| OsintStalker | tool | <https://github.com/milo2012/osintstalker> |
| osmedeus/osmedeus-base | tool | <https://github.com/osmedeus/osmedeus-base> |
| osmedeus/osmedeus-workflow | tool | <https://github.com/osmedeus/osmedeus-workflow> |
| OSSEC | tool | <https://ossec.github.io> |
| OTInstaller/otinstaller | dashboard | <https://github.com/OTInstaller/otinstaller> |
| oussamaln/AEGIS-INTEL | research-project | <https://github.com/oussamaln/AEGIS-INTEL> |
| Outwit | tool | <https://www.outwit.com> |
| Overhead24 | research-project | <https://overhead24.com> |
| Overpass Turbo | tool | <https://overpass-turbo.eu/> |
| Overseas Company Registers | research-project | <https://www.gov.uk/government/publications/overseas-registries/overseas-registries> |
| OverTheWire Wargames | tool | <https://overthewire.org> |
| owasp-amass/amass | tool | <https://github.com/owasp-amass/amass> |
| OWASP/D4N155 | api-service | <https://github.com/OWASP/D4N155> |
| Owez/yark | tool | <https://github.com/Owez/yark> |
| owl234/ARL-Next | container | <https://github.com/owl234/ARL-Next> |
| Oxford Journals | tool | <https://www.oxfordjournals.org> |
| OXT | web-platform | <https://oxt.me/> |
| p0dalirius/GetFortinetSerialNumber | tool | <https://github.com/p0dalirius/GetFortinetSerialNumber> |
| p0dalirius/ListValidGSuiteEmails | tool | <https://github.com/p0dalirius/ListValidGSuiteEmails> |
| p0dalirius/RDWAtool | directory | <https://github.com/p0dalirius/RDWAtool> |
| P3GLEG/PwnBack | plugin | <https://github.com/P3GLEG/PwnBack> |
| P3run/otwartezrodla | plugin | <https://github.com/P3run/otwartezrodla> |
| paaster | tool | <https://paaster.io/> |
| pablosnt/rekono | web-platform | <https://github.com/pablosnt/rekono> |
| pacer.uscourts.gov | web-platform | <https://pacer.uscourts.gov/> |
| packet.guru | cli-tool | <https://packet.guru/> |
| PageGlimpse | research-project | <http://www.pageglimpse.com> |
| Palimpsest | dataset | <https://www.palimpsest.info> |
| pallab-js/link-mage | tool | <https://github.com/pallab-js/link-mage> |
| Palladio | tool | <https://hdlab.stanford.edu/palladio> |
| Panopticlick | cli-tool | <https://panopticlick.eff.org> |
| pantchox/Twitark | dataset | <https://github.com/pantchox/Twitark> |
| Paper-Pen/GatherInfo | research-project | <https://github.com/Paper-Pen/GatherInfo> |
| Paperboy | research-project | <https://www.thepaperboy.com> |
| Pappers | tool | <https://www.pappers.fr/> |
| parrotsec.org | tool | <https://parrotsec.org/> |
| Parse Everything | api-service | <https://github.com/zenkdom/parse-everything-global> |
| Parseek (Iran) | tool | <https://www.parseek.com> |
| PassiveTotal (RiskIQ) | tool | <https://community.riskiq.com> |
| PasswordSearch | tool | <https://telegram.me/PasswordSearchBot> |
| PAST2212/certthreat | tool | <https://github.com/PAST2212/certthreat> |
| Paste.Cash | tool | <https://www.paste.cash/> |
| paste.debian | tool | <https://Paste.debian.net> |
| paste.ee | tool | <https://Paste.ee> |
| paste.in.ua | tool | <https://paste.in.ua/> |
| paste.kde | tool | <https://Paste.kde.org> |
| Paste.Monster | api-service | <https://paste.monster/> |
| Paste.Quest | tool | <https://pastequest.com/> |
| paste.sh | tool | <https://paste.sh/> |
| paste.ubuntu | tool | <https://paste.ubuntu.com> |
| Pastebin | tool | <https://pastebin.com/> |
| Pastebin.cz | tool | <https://www.pastebin.cz/en/> |
| Pastery | tool | <https://www.pastery.net/> |
| PasteShr | tool | <https://www.pasteshr.com/> |
| PasteSite.Net | tool | <https://pastesite.net/> |
| Patent Attorneys/Agent Search | tool | <https://oedci.uspto.gov/OEDCI/> |
| Paul Hensel’s General Informational Data Page | tool | <https://www.paulhensel.org/dataintl.html> |
| paulpogoda/OSINT-CSE | tool | <https://github.com/paulpogoda/OSINT-CSE> |
| paulpogoda/OSINT-for-countries-V2.0-MOVED | tool | <https://github.com/paulpogoda/OSINT-for-countries-V2.0-MOVED-> |
| paulpogoda/OSINT-Tools-China | tool | <https://github.com/paulpogoda/OSINT-Tools-China> |
| paulpogoda/OSINT-Tools-Emirates | tool | <https://github.com/paulpogoda/OSINT-Tools-Emirates> |
| paulpogoda/OSINT-Tools-India | tool | <https://github.com/paulpogoda/OSINT-Tools-India> |
| paulpogoda/OSINT-Tools-Iran | tool | <https://github.com/paulpogoda/OSINT-Tools-Iran> |
| paulpogoda/OSINT-Tools-Russia | tool | <https://github.com/paulpogoda/OSINT-Tools-Russia> |
| paulpogoda/OSINT-Tools-Syria | tool | <https://github.com/paulpogoda/OSINT-Tools-Syria> |
| paulpogoda/OSINT-Tools-Taiwan | tool | <https://github.com/paulpogoda/OSINT-Tools-Taiwan> |
| paulpogoda/OSINT-Tools-UK | tool | <https://github.com/paulpogoda/OSINT-Tools-UK> |
| paulpogoda/Scam-Surface-Mapper | research-project | <https://github.com/paulpogoda/Scam-Surface-Mapper> |
| paulrekaris/TGA-COVID19-Vaccine-Safety-Monitoring-Audit | framework | <https://github.com/paulrekaris/TGA-COVID19-Vaccine-Safety-Monitoring-Audit> |
| paulveillard/cybersecurity-osint | awesome-list | <https://github.com/paulveillard/cybersecurity-osint> |
| PeakVisor | tool | <https://peakvisor.com/> |
| pedrodeivid/osint-resources | tool | <https://github.com/pedrodeivid/osint-resources> |
| Peekalink | api-service | <https://www.peekalink.io> |
| PeekYou | tool | <https://peekyou.com/> |
| Peepmail | tool | <http://www.samy.pl/peepmail> |
| Peerblock | tool | <https://forums.peerblock.com> |
| Penn World Table | tool | <https://www.rug.nl/research/ggdc/data/pwt/pwt-8.1> |
| Pentest-Tools.com | research-project | <https://pentest-tools.com/information-gathering/google-hacking> |
| PentesterLab | tool | <https://pentesterlab.com> |
| Perplexity | tool | <https://www.perplexity.ai> |
| Perry Castaneda Library | library | <https://www.lib.utexas.edu/maps> |
| Perspective | dataset | <https://github.com/finos/perspective> |
| PeterDaveHello/top-1m-domains | tool | <https://github.com/PeterDaveHello/top-1m-domains> |
| petstuk/Aperture-OSINT-Workbench | plugin | <https://github.com/petstuk/Aperture-OSINT-Workbench> |
| Pew Research Center | research-project | <https://www.pewinternet.org/datasets> |
| PGPKeyAnalyser | tool | <https://kriztalz.sh/pgp-key-analyser/> |
| Ph055a/OSINT_Collection | dataset | <https://github.com/Ph055a/OSINT_Collection> |
| Phantom Tide | dashboard | <https://github.com/tg12/phantomtide> |
| Phind | tool | <https://phindai.org/> |
| phind.com | research-project | <https://www.phind.com/> |
| phishdestroy/destroylist | api-service | <https://github.com/phishdestroy/destroylist> |
| phishdestroy/DestroyScammers | research-project | <https://github.com/phishdestroy/DestroyScammers> |
| PhishStats | dataset | <https://phishstats.info/> |
| PhishTank | tool | <https://phishtank.org> |
| Phone Validator | web-platform | <https://www.phonevalidator.com/index.aspx> |
| phoneintel/phoneintel | tool | <https://github.com/phoneintel/phoneintel> |
| PhoneNumber-OSINT | tool | <https://github.com/spider863644/PhoneNumber-OSINT> |
| PhonePe/mantis | framework | <https://github.com/PhonePe/mantis> |
| Photo Sherlock | mobile-app | <https://photosherlock.com/> |
| PhotoBucket | tool | <https://photobucket.com> |
| Pic2Map | research-project | <https://www.pic2map.com/> |
| Picarta | tool | <https://www.picarta.ai/> |
| picoCTF | web-platform | <https://picoctf.org> |
| Picodash | tool | <https://www.picodash.com> |
| PicTriev | tool | <https://www.pictriev.com> |
| Pidgin | tool | <https://www.pidgin.im> |
| pielco11/fav-up | api-service | <https://github.com/pielco11/fav-up> |
| pielco11/telescan | api-service | <https://github.com/pielco11/telescan> |
| pieterunperceived553/holehe | web-platform | <https://github.com/pieterunperceived553/holehe> |
| pikpikcu/hostinject | tool | <https://github.com/pikpikcu/hostinject> |
| pikpikcu/js-finding | tool | <https://github.com/pikpikcu/js-finding> |
| pikpikcu/nodecraw | plugin | <https://github.com/pikpikcu/nodecraw> |
| pikpikcu/nuubi | tool | <https://github.com/pikpikcu/nuubi> |
| pikpikcu/XRCross | tool | <https://github.com/pikpikcu/XRCross> |
| Piktochart | tool | <https://piktochart.com> |
| PimEyes | tool | <https://pimeyes.com> |
| PimEyes | tool | <https://telegram.me/pimeyesbot> |
| Pingroupie | tool | <https://pingroupie.com> |
| pinkycourse/GhostIntel | framework | <https://github.com/pinkycourse/GhostIntel> |
| Pinterest | web-platform | <https://www.pinterest.com> |
| Pinterest Pin Stats | tool | <https://chromewebstore.google.com/detail/pinterest-pin-stats-sort/mcmkeopcpbfgjlakblglpcccpodbjkel> |
| Pipl | tool | <https://pipl.com> |
| pirate/mesh-networking | library | <https://github.com/pirate/mesh-networking> |
| Pixel Block | tool | <https://chrome.google.com/webstore/detail/pixelblock/jmpmfcjnflbcoidlgapblgpgbilinlem> |
| Pixsy | tool | <https://www.pixsy.com/> |
| Pixxa | tool | <https://www.pixxa.com> |
| Plotly | tool | <https://plot.ly> |
| Plunkett Research | research-project | <https://www.plunkettresearchonline.com> |
| pMiszkin/OSINT-Tools | awesome-list | <https://github.com/pMiszkin/OSINT-Tools> |
| PolygonScan | tool | <https://polygonscan.com> |
| Polymaps | research-project | <https://polymaps.org> |
| Population Reference Bureau Data Finder | tool | <https://www.prb.org/DataFinder.aspx> |
| PortInsight.io | tool | <https://portinsight.io/ports> |
| PortSwigger Web Security Academy | tool | <https://portswigger.net/web-security> |
| portswigger.net | tool | <https://portswigger.net/> |
| portswigger.net/burp | web-platform | <https://portswigger.net/burp> |
| Postuf/telegram-osint-lib | api-service | <https://github.com/Postuf/telegram-osint-lib> |
| potato-security/PotatoTool | cli-tool | <https://github.com/potato-security/PotatoTool> |
| povvo/sleuth | tool | <https://github.com/povvo/sleuth> |
| powerexploit/Ashok | tool | <https://github.com/powerexploit/Ashok> |
| Pown Recon | framework | <https://github.com/pownjs/pown-recon> |
| ppanthony/faceymcface | framework | <https://github.com/ppanthony/faceymcface> |
| ppfeister/sylva | tool | <https://github.com/ppfeister/sylva> |
| ppmpreetham/vesperplusplus | framework | <https://github.com/ppmpreetham/vesperplusplus> |
| PR Newswire | tool | <https://www.prnewswire.com> |
| praetorian-inc/NTLMRecon | tool | <https://github.com/praetorian-inc/NTLMRecon> |
| PravinTheCoder/pictosint-by-pravin | framework | <https://github.com/PravinTheCoder/pictosint-by-pravin> |
| Preceden | tool | <https://www.preceden.com/> |
| Predicta Search | tool | <https://predictasearch.com> |
| Press Reader | tool | <https://www.pressreader.com> |
| Privacy Badger | tool | <https://www.eff.org/privacybadger> |
| Privacy.com | tool | <https://privacy.com> |
| Privazer | tool | <https://privazer.com> |
| PRNewswire | tool | <https://prnmedia.prnewswire.com> |
| Profil3r | tool | <https://github.com/Greyjedix/Profil3r> |
| Profil3r | tool | <https://github.com/Rog3rSm1th/Profil3r> |
| ProfileImageIntel | tool | <https://profileimageintel.com/> |
| projectdiscovery/asnmap | library | <https://github.com/projectdiscovery/asnmap> |
| projectdiscovery/httpx | library | <https://github.com/projectdiscovery/httpx> |
| projectdiscovery/subfinder | tool | <https://github.com/projectdiscovery/subfinder> |
| projectdiscovery/uncover | cli-tool | <https://github.com/projectdiscovery/uncover> |
| projectdiscovery/urlfinder | tool | <https://github.com/projectdiscovery/urlfinder> |
| Proton Mail | tool | <https://protonmail.com> |
| Provereno-Media/OSINT-Tools-Cuba | framework | <https://github.com/Provereno-Media/OSINT-Tools-Cuba> |
| Proviesec/Proviesec-Bug-Bounty-Dorking-Site-PBBDS | tool | <https://github.com/Proviesec/Proviesec-Bug-Bounty-Dorking-Site-PBBDS> |
| PRS Risk Indicators | tool | <https://www.prsgroup.com> |
| psjs12/TelegramDetective | tool | <https://github.com/psjs12/TelegramDetective> |
| Public Transport Maps | tool | <https://cipher387.github.io/public_transport_maps/> |
| PublicWWW | tool | <https://publicwww.com/> |
| PubMed | tool | <https://www.ncbi.nlm.nih.gov/pubmed> |
| Pullpush | directory | <https://pullpush.io/> |
| Pulsedive | dataset | <https://pulsedive.com> |
| Purpl3-Dev/OSINTLAB | api-service | <https://github.com/Purpl3-Dev/OSINTLAB> |
| Pushpenderrathore/OSINT | tool | <https://github.com/Pushpenderrathore/OSINT> |
| Pushshift API | api-service | <https://pushshift.io/> |
| pwn.college | tool | <https://pwn.college> |
| pwnfoo/NTLMRecon | tool | <https://github.com/pwnfoo/NTLMRecon> |
| pwnwriter/haylxon | cli-tool | <https://github.com/pwnwriter/haylxon> |
| pwnwriter/kanha | tool | <https://github.com/pwnwriter/kanha> |
| pwnxotus/DIGI-NETRA | framework | <https://github.com/pwnxotus/DIGI-NETRA> |
| Pyba | framework | <https://github.com/fauvidoTechnologies/PyBrowserAutomation/> |
| qbitseclabs/osint | container | <https://github.com/qbitseclabs/osint> |
| qeeqbox/analyzer | tool | <https://github.com/qeeqbox/analyzer> |
| qeeqbox/social-analyzer | api-service | <https://github.com/qeeqbox/social-analyzer> |
| QGIS | research-project | <https://qgis.org> |
| QGIS | tool | <https://github.com/qgis/QGIS> |
| QlikView | tool | <https://www.visualintelligence.co.nz/qlikview> |
| Quadrigram | tool | <https://www.quadrigram.com> |
| Quake (360.cn) | tool | <https://quake.360.net> |
| Qualys SSL Check | research-project | <https://www.ssllabs.com/ssltest/> |
| Quantcast | research-project | <https://www.quantcast.com> |
| Quetzal Search | tool | <https://www.quetzal-search.info> |
| Quick Sprout | research-project | <https://www.quicksprout.com> |
| QuickCode | tool | <https://quickcode.io/> |
| QuickMaps | research-project | <https://chrome.google.com/webstore/detail/quick-maps/bgbojmobaekecckmomemopckmeipecij> |
| QuickscoperXZ/osint_auto_t | tool | <https://github.com/QuickscoperXZ/osint_auto_t> |
| Quora | tool | <https://www.quora.com> |
| Qwant | tool | <https://www.qwant.com> |
| Qzone (China) | tool | <https://qzone.qq.com> |
| r1cksec/corptrace | tool | <https://github.com/r1cksec/corptrace> |
| r3curs1v3-pr0xy/vajra | web-platform | <https://github.com/r3curs1v3-pr0xy/vajra> |
| R4yGM/dorkscout | tool | <https://github.com/R4yGM/dorkscout> |
| r57-labs/chaos | tool | <https://github.com/r57-labs/chaos> |
| radioactivetobi/geo-recon | cli-tool | <https://github.com/radioactivetobi/geo-recon> |
| radmorex/osint-launcher | cli-tool | <https://github.com/radmorex/osint-launcher> |
| Radware Live Cyber Threat Map | tool | <https://livethreatmap.radware.com/> |
| rainiersvn/aegis | web-platform | <https://github.com/rainiersvn/aegis> |
| RAJANAGORI/Nightingale | container | <https://github.com/RAJANAGORI/Nightingale> |
| Raphael | tool | <https://dmitrybaranovskiy.github.io/raphael> |
| RapidDNS | api-service | <https://rapiddns.io> |
| RAW | tool | <https://raw.densitydesign.org> |
| rawfilejson/awesome-osint-arsenal | awesome-list | <https://github.com/rawfilejson/awesome-osint-arsenal> |
| Reacher | api-service | <https://reacher.email> |
| readloud/Osintgram | api-service | <https://github.com/readloud/Osintgram> |
| readsb | dataset | <https://github.com/wiedehopf/readsb> |
| Realmec21/osint-ru | awesome-list | <https://github.com/Realmec21/osint-ru> |
| Realradioactive/OSINTCENTER | framework | <https://github.com/Realradioactive/OSINTCENTER> |
| RECAP Archive | tool | <https://www.courtlistener.com/recap/> |
| recap-cli | api-service | <https://github.com/NPCmillionaire/recap-cli> |
| Recon-ng | tool | <https://github.com/lanmaster53/recon-ng> |
| reconhub/learn | web-platform | <https://github.com/reconhub/learn> |
| reconness/reconness | web-platform | <https://github.com/reconness/reconness> |
| reconness/reconness-agents | tool | <https://github.com/reconness/reconness-agents> |
| reconurge/flowsint | web-platform | <https://github.com/reconurge/flowsint> |
| recosint/osint-tools | web-platform | <https://github.com/recosint/osint-tools> |
| RecruitEm | tool | <https://recruitin.net/> |
| REDARCS | tool | <https://the-eye.eu/redarcs/> |
| Reddit | tool | <https://www.reddit.com> |
| Reddit Archive | tool | <http://www.redditarchive.com> |
| Reddit Comment Lookup | tool | <https://randomtools.io/reddit-comment-search/> |
| Reddit Comment Search | tool | <https://redditcommentsearch.com/> |
| Reddit Suite | tool | <https://chrome.google.com/webstore/detail/reddit-enhancement-suite/kbmfpngjjgdllneeigpgjifpgocmfgmb> |
| Reddit User Analyser | tool | <https://atomiks.github.io/reddit-user-analyser/> |
| reddit-user-analyser | tool | <https://github.com/atomiks/reddit-user-analyser> |
| reddit-user-analyser.netlify.app | tool | <https://reddit-user-analyser.netlify.app/> |
| RedditMetis | tool | <https://redditmetis.com/> |
| RedditSearch.io | tool | <https://redditsearch.io> |
| redhuntlabs/Awesome-Asset-Discovery | awesome-list | <https://github.com/redhuntlabs/Awesome-Asset-Discovery> |
| redhuntlabs/BurpSuite-Asset_Discover | plugin | <https://github.com/redhuntlabs/BurpSuite-Asset_Discover> |
| redi-git/SCCM_SLAP | tool | <https://github.com/redi-git/SCCM_SLAP> |
| RedirectDetective | research-project | <https://redirectdetective.com> |
| redteam.to | directory | <https://redteam.to> |
| Reed (UK) | tool | <https://www.reed.co.uk> |
| Reeder | tool | <https://reederapp.com> |
| Refloow/Refloow-Geo-Forensics | tool | <https://github.com/Refloow/Refloow-Geo-Forensics> |
| RegDateBot | tool | <https://t.me/regdate_clone_bot> |
| Reginald-Gillespie/GitSniff | tool | <https://github.com/Reginald-Gillespie/GitSniff> |
| regvk.com | tool | <https://regvk.com/> |
| Reinvicta-Tech/beatrooter | tool | <https://github.com/Reinvicta-Tech/beatrooter> |
| Related Repos | tool | <https://relatedrepos.com/> |
| remnux.org | tool | <https://remnux.org/> |
| remonsec/Pri0tx | research-project | <https://github.com/remonsec/Pri0tx> |
| Remote DNS Lookup | research-project | <https://remote.12dt.com> |
| renkagod/osint-toolbox-mcp | container | <https://github.com/renkagod/osint-toolbox-mcp> |
| Rentry | web-platform | <https://rentry.co/> |
| Reposearch | tool | <http://codefinder.org/> |
| ReseacherID | tool | <https://www.researcherid.com> |
| Research Gate | research-project | <https://www.researchgate.net> |
| Resolver | tool | <https://metaproductsrevolver.com> |
| RetroPackets/Fugitive | tool | <https://github.com/RetroPackets/Fugitive> |
| Reunion | tool | <https://reunion.com> |
| Reuters | tool | <https://www.reuters.com> |
| Revealer.cc | tool | <https://revealer.cc> |
| Reverse Image Search Anywhere | browser-extension | <https://reverseimage.app/> |
| Reverse Phone Check | research-project | <https://www.reversephonecheck.com> |
| Reverse Phone Lookup | web-platform | <https://www.reversephonelookup.com/> |
| ReverseImageLocation | research-project | <https://reverseimagelocation.com> |
| RevEye | browser-extension | <https://github.com/steven2358/reveye> |
| RevoltSecurities/GoogleDorker | tool | <https://github.com/RevoltSecurities/GoogleDorker> |
| rhematt/Snap-Scraper | tool | <https://github.com/rhematt/Snap-Scraper> |
| rick417/twayback-player | tool | <https://github.com/rick417/twayback-player> |
| risshe92/docprobe | tool | <https://github.com/risshe92/docprobe> |
| ritchiemwewa/osinteye | container | <https://github.com/ritchiemwewa/osinteye> |
| ritchiemwewa/oxdork | research-project | <https://github.com/ritchiemwewa/oxdork> |
| ritchiemwewa/thedevilseye | web-platform | <https://github.com/ritchiemwewa/thedevilseye> |
| ritchiemwewa/thorndyke | research-project | <https://github.com/ritchiemwewa/thorndyke> |
| RiteTag | tool | <https://ritetag.com> |
| Rival IQ | tool | <https://www.rivaliq.com> |
| rix4uni/Bug-Bounty-Tampermonkey-Scripts | tool | <https://github.com/rix4uni/Bug-Bounty-Tampermonkey-Scripts> |
| rix4uni/cvemapping | tool | <https://github.com/rix4uni/cvemapping> |
| rix4uni/emailextractor | research-project | <https://github.com/rix4uni/emailextractor> |
| rix4uni/GarudRecon | tool | <https://github.com/rix4uni/GarudRecon> |
| rix4uni/gosqli | tool | <https://github.com/rix4uni/gosqli> |
| rix4uni/haktrailsfree | api-service | <https://github.com/rix4uni/haktrailsfree> |
| rix4uni/ipfinder | tool | <https://github.com/rix4uni/ipfinder> |
| rix4uni/originiphunter | api-service | <https://github.com/rix4uni/originiphunter> |
| rix4uni/pvreplace | tool | <https://github.com/rix4uni/pvreplace> |
| rix4uni/pyxss | tool | <https://github.com/rix4uni/pyxss> |
| rix4uni/resolvers | tool | <https://github.com/rix4uni/resolvers> |
| rix4uni/socialfinder | tool | <https://github.com/rix4uni/socialfinder> |
| rix4uni/subdog | tool | <https://github.com/rix4uni/subdog> |
| rix4uni/techfinder | library | <https://github.com/rix4uni/techfinder> |
| rix4uni/tldscan | tool | <https://github.com/rix4uni/tldscan> |
| rix4uni/uforall | tool | <https://github.com/rix4uni/uforall> |
| rix4uni/unew | cli-tool | <https://github.com/rix4uni/unew> |
| rix4uni/vulntechfinder | tool | <https://github.com/rix4uni/vulntechfinder> |
| rix4uni/WordList | tool | <https://github.com/rix4uni/WordList> |
| rix4uni/wordpress-plugins | plugin | <https://github.com/rix4uni/wordpress-plugins> |
| rix4uni/xsschecker | tool | <https://github.com/rix4uni/xsschecker> |
| rix4uni/xssrecon | tool | <https://github.com/rix4uni/xssrecon> |
| riza/linx | tool | <https://github.com/riza/linx> |
| rndinfosecguy/BlackSignal | tool | <https://github.com/rndinfosecguy/BlackSignal> |
| rndinfosecguy/Scavenger | tool | <https://github.com/rndinfosecguy/Scavenger> |
| Robtex | web-platform | <https://www.robtex.com> |
| RocketReach | tool | <https://rocketreach.co> |
| RogueSMG/Scavenger | tool | <https://github.com/RogueSMG/Scavenger> |
| ronin-rb/ronin-app | dataset | <https://github.com/ronin-rb/ronin-app> |
| Roo7K1d/D0x-K1t-v2 | web-platform | <https://github.com/Roo7K1d/D0x-K1t-v2> |
| roodriiigooo/GITLEAK_EXPLORER | tool | <https://github.com/roodriiigooo/GITLEAK_EXPLORER> |
| Root-Me | tool | <https://www.root-me.org> |
| rootdr-backup/Reconner | web-platform | <https://github.com/rootdr-backup/Reconner> |
| RossGeerlings/webstor | tool | <https://github.com/RossGeerlings/webstor> |
| rotemreiss/uddup | tool | <https://github.com/rotemreiss/uddup> |
| Router Passwords | dataset | <https://www.routerpasswords.com> |
| roxm337/blacklance | framework | <https://github.com/roxm337/blacklance> |
| RSS Feed Reader | dataset | <https://chrome.google.com/webstore/detail/rss-feed-reader/pnjaodmkngahhkoihejjehlcdlnohgmp> |
| RSS Micro | tool | <http://www.rssmicro.com> |
| RSS Search Engine | tool | <https://ctrlq.org/rss> |
| RSS Search Hub | tool | <http://www.rsssearchhub.com> |
| RSSOwl | tool | <https://www.rssowl.org> |
| RTFM: Red Team Field Manual | tool | <https://www.amazon.com/dp/B07RJG62SJ> |
| rtl_433 | tool | <https://github.com/merbanan/rtl_433> |
| rubberneckrepair179/compliance-gpt | framework | <https://github.com/rubberneckrepair179/compliance-gpt> |
| Ruby570bocadito/OSINT-EYE | api-service | <https://github.com/Ruby570bocadito/OSINT-EYE> |
| Rusprofile | tool | <https://www.rusprofile.ru/> |
| RuthGnz/SpyScrap | container | <https://github.com/RuthGnz/SpyScrap> |
| ruyynn/GhostIntel | awesome-list | <https://github.com/ruyynn/GhostIntel> |
| RykerWilder/osint-hub | tool | <https://github.com/RykerWilder/osint-hub> |
| rzaeen/Muhqqiq-OSINT | tool | <https://github.com/rzaeen/Muhqqiq-OSINT> |
| s-r-e-e-r-a-j/IPAnalyzer | cli-tool | <https://github.com/s-r-e-e-r-a-j/IPAnalyzer> |
| s-r-e-e-r-a-j/NetSpecter | tool | <https://github.com/s-r-e-e-r-a-j/NetSpecter> |
| s-r-e-e-r-a-j/WebExtractor | api-service | <https://github.com/s-r-e-e-r-a-j/WebExtractor> |
| s-r-e-e-r-a-j/WebSift | cli-tool | <https://github.com/s-r-e-e-r-a-j/WebSift> |
| s0md3v/Arjun | api-service | <https://github.com/s0md3v/Arjun> |
| s0md3v/Orbit | tool | <https://github.com/s0md3v/Orbit> |
| s0md3v/Photon | tool | <https://github.com/s0md3v/Photon> |
| s0md3v/ReconDog | tool | <https://github.com/s0md3v/ReconDog> |
| s0md3v/SubGPT | research-project | <https://github.com/s0md3v/SubGPT> |
| s0md3v/Zen | tool | <https://github.com/s0md3v/Zen> |
| S3cur3Th1sSh1t/WinPwn | cli-tool | <https://github.com/S3cur3Th1sSh1t/WinPwn> |
| S3Scanner | api-service | <https://github.com/sa7mon/S3Scanner> |
| s41r4j/phomber | framework | <https://github.com/s41r4j/phomber> |
| sa7mon/venmo-data | dataset | <https://github.com/sa7mon/venmo-data> |
| saeeddhqan/Maryam | framework | <https://github.com/saeeddhqan/Maryam> |
| Safari | tool | <https://www.apple.com/safari> |
| SafeNetix/osintbox | framework | <https://github.com/SafeNetix/osintbox> |
| SafeNote | web-platform | <https://safenote.co/> |
| SagarBiswas-MultiHAT/osint-exposure-toolkit | framework | <https://github.com/SagarBiswas-MultiHAT/osint-exposure-toolkit> |
| SagarBiswas-MultiHAT/The-BlackHAT-roadmap | directory | <https://github.com/SagarBiswas-MultiHAT/The-BlackHAT-roadmap> |
| SAGE Journals | tool | <https://online.sagepub.com> |
| sahildari/R3CON | tool | <https://github.com/sahildari/R3CON> |
| saitarrun/Xploit404 | framework | <https://github.com/saitarrun/Xploit404> |
| SameID | research-project | <https://sameid.net> |
| sammwyy/Reccon | web-platform | <https://github.com/sammwyy/Reccon> |
| SamueleAmato/Near | framework | <https://github.com/SamueleAmato/Near> |
| SangMata (beta) | tool | <https://t.me/SangMata_beta_bot> |
| SangMataInfo_bot | tool | <https://t.me/SangMataInfo_bot> |
| SANS Internet Storm Center Diary (Full Text) | dataset | <https://isc.sans.edu/rssfeed_full.xml> |
| sans.org | tool | <https://sans.org/> |
| SAPO (Portugal) | tool | <https://www.sapo.pt> |
| saramazal/ethical-hacking-study | research-project | <https://github.com/saramazal/ethical-hacking-study> |
| SAS Planet | research-project | <https://www.sasgis.org/sasplaneta/> |
| SatDump | tool | <https://github.com/SatDump/SatDump> |
| Satellites Pro | research-project | <https://satellites.pro/> |
| SauceNAO | tool | <https://saucenao.com/> |
| savaskarofficial/savaskarofficial | mobile-app | <https://github.com/savaskarofficial/savaskarofficial> |
| SaveYoutubeBot | tool | <https://t.me/SaveYoutubeBot> |
| sayan9168/nexus-osint | api-service | <https://github.com/sayan9168/nexus-osint> |
| Sayanthrock-Developer/GitHub-Rock | mobile-app | <https://github.com/Sayanthrock-Developer/GitHub-Rock> |
| Sayari | tool | <https://sayari.com/> |
| sayeedjoy/Date-Sniffer | plugin | <https://github.com/sayeedjoy/Date-Sniffer> |
| sc1341/InstagramOSINT | research-project | <https://github.com/sc1341/InstagramOSINT> |
| ScamAdviser | tool | <https://www.scamadviser.com> |
| ScanMalware | dataset | <https://scanmalware.com> |
| Scav-engeR/ELOHIM | dashboard | <https://github.com/Scav-engeR/ELOHIM> |
| Science Publications | tool | <https://www.thescipub.com> |
| ScienceDirect | tool | <https://www.sciencedirect.com> |
| ScienceDomain | tool | <https://www.sciencedomain.org> |
| SCIRP | tool | <https://www.scirp.org> |
| Scoot | research-project | <https://www.scoot.co.uk> |
| ScoutSuite | tool | <https://github.com/nccgroup/ScoutSuite> |
| screem500/tiktok-osint-toolkit | dashboard | <https://github.com/screem500/tiktok-osint-toolkit> |
| Scribble Maps | research-project | <https://scribblemaps.com> |
| Scribd | tool | <https://www.scribd.com> |
| Script Safe | tool | <https://chrome.google.com/webstore/detail/scriptsafe/oiigbmnaadbkfbmpbfijlflahbdbdgdf?hl=en> |
| scrt.link | tool | <https://scrt.link/> |
| Scweet | api-service | <https://github.com/Altimis/Scweet> |
| SDR++ | web-platform | <https://github.com/AlexandreRouma/SDRPlusPlus> |
| sds-osint/holehe-web | tool | <https://github.com/sds-osint/holehe-web> |
| sds-osint/transforms | tool | <https://github.com/sds-osint/transforms> |
| Search by Image | browser-extension | <https://github.com/dessant/search-by-image> |
| search.censys.io/api | api-service | <https://search.censys.io/api> |
| Search.ch (Switzerland) | tool | <https://www.search.ch> |
| Search.com | tool | <https://www.search.com> |
| Search4faces | web-platform | <https://search4faces.com/> |
| Search4faces | tool | <https://search4faces.com/en/> |
| Search_firm_bot | tool | <https://t.me/Search_firm_bot> |
| SearchBug | tool | <https://www.searchbug.com> |
| SearchCode | api-service | <https://searchcode.com> |
| SearchDorks | tool | <https://kriztalz.sh/search-dorks/> |
| SearchFiles.de | tool | <https://searchfiles.de/> |
| Searchforchats | tool | <https://telegram.me/searchforchatsbot> |
| SearchIsBack | tool | <https://searchisback.com> |
| SearchPeopleFREE | research-project | <https://www.searchpeoplefree.com/phone-lookup> |
| SearXNG | tool | <https://searxng.org/> |
| SEC EDGAR | tool | <https://www.sec.gov/edgar> |
| sec-it/BFAC-Burp-Extension | plugin | <https://github.com/sec-it/BFAC-Burp-Extension> |
| sec0ps/va-pt | framework | <https://github.com/sec0ps/va-pt> |
| SecApps Recon | tool | <https://secapps.com/market/recon> |
| secretoplatatito-wq/Cool | mobile-app | <https://github.com/secretoplatatito-wq/Cool> |
| secretoplatatito-wq/Test | framework | <https://github.com/secretoplatatito-wq/Test> |
| SecShiv/OneDorkForAll | research-project | <https://github.com/SecShiv/OneDorkForAll> |
| Section 16 Deadline Calculator | research-project | <https://github.com/Turner-Levey/section-16-deadline-calculator> |
| Sector035 | tool | <https://sector035.nl/> |
| Secure Gateway Live Cyber Threat Map | tool | <https://securegateway.com/map/v5/> |
| securedrop.org | web-platform | <https://securedrop.org/> |
| Secureito | tool | <https://www.secureito.com> |
| Securesha | tool | <https://securesha.re> |
| Security Onion | tool | <https://securityonionsolutions.com> |
| SecurityTrails | api-service | <https://securitytrails.com/> |
| SecurityTrails | api-service | <https://securitytrails.com/dns-trails> |
| seedon198/Farsight | framework | <https://github.com/seedon198/Farsight> |
| Seek (Australia) | tool | <https://www.seek.com.au> |
| seekr-osint/seekr | framework | <https://github.com/seekr-osint/seekr> |
| seintpl/osint | tool | <https://github.com/seintpl/osint> |
| Selfoss | tool | <https://selfoss.aditu.de> |
| SEMrush | research-project | <https://www.semrush.com> |
| senran101604/sagemode | web-platform | <https://github.com/senran101604/sagemode> |
| sensepost/Frack | research-project | <https://github.com/sensepost/Frack> |
| Sentiment140 | tool | <http://www.twittersentiment.appspot.com> |
| Sentinel Hub | research-project | <https://www.sentinel-hub.com/explore/sentinelplayground/> |
| Sentinel Visualizer | tool | <https://www.fmsasg.com> |
| sentinel-hub.com | tool | <https://sentinel-hub.com/> |
| SEO Chat Tools | research-project | <http://tools.seochat.com> |
| SEOTools for Excel | research-project | <https://seotoolsforexcel.com> |
| SerpApi | api-service | <https://serpapi.com/> |
| SerpScan | cli-tool | <https://github.com/Alaa-abdulridha/SerpScan> |
| Serpstat | research-project | <https://serpstat.com> |
| service.nalog.ru | web-platform | <https://service.nalog.ru/> |
| servicelogon/awesome-recon-tools | awesome-list | <https://github.com/servicelogon/awesome-recon-tools> |
| SESRIC Basic Social and Economic Indicators | tool | <https://www.sesric.org/baseind.php> |
| SESRIC Databases | dataset | <https://www.sesric.org/databases-index.php> |
| Seznam(Czech Republic) | tool | <https://seznam.cz> |
| SH1ROdev/SHIROMU | api-service | <https://github.com/SH1ROdev/SHIROMU> |
| Sh1Yo/x8 | tool | <https://github.com/Sh1Yo/x8> |
| Shad0w-ops/H.I.V.E | api-service | <https://github.com/Shad0w-ops/H.I.V.E> |
| ShadowFinder-Web | cli-tool | <https://kluter.github.io/ShadowFinder-Web> |
| shadowhunter1024/osint-framework-chinese | framework | <https://github.com/shadowhunter1024/osint-framework-chinese> |
| Shadowmap | tool | <https://shadowmap.org/> |
| Shadowserver | dashboard | <https://dashboard.shadowserver.org/> |
| shadowuneed/Auron_Anti-Corruption-2026 | api-service | <https://github.com/shadowuneed/Auron_Anti-Corruption-2026> |
| Shakedash-dev/GmailOSINT | web-platform | <https://github.com/Shakedash-dev/GmailOSINT> |
| shallvhack/awesome-osint-toolkit | awesome-list | <https://github.com/shallvhack/awesome-osint-toolkit> |
| shallvhack/Flight-Tracker | api-service | <https://github.com/shallvhack/Flight-Tracker> |
| shallvhack/osint-journo-web | tool | <https://github.com/shallvhack/osint-journo-web> |
| sham00n/buster | tool | <https://github.com/sham00n/buster> |
| sham00n/waybulk | tool | <https://github.com/sham00n/waybulk> |
| Shanti Interactive | tool | <http://www.viseyes.org> |
| sharsil/mailcat | api-service | <https://github.com/sharsil/mailcat> |
| shelld3v/flydns | cli-tool | <https://github.com/shelld3v/flydns> |
| sheriffsec/shadow-scan | web-platform | <https://github.com/sheriffsec/shadow-scan> |
| Sherlock | tool | <https://t.me/Getcontact123qwerty_bot?start=_ref_jGW8Sa_iEmG9V> |
| sherlock-project/sherlock | cli-tool | <https://github.com/sherlock-project/sherlock> |
| sherlock-project/sherlockproject.xyz | tool | <https://github.com/sherlock-project/sherlockproject.xyz> |
| SherlockEye | tool | <https://sherlockeye.io/> |
| SheSource | tool | <https://www.shesource.org> |
| shivendrachauhanhacker/OSINT_toolkit | api-service | <https://github.com/shivendrachauhanhacker/OSINT_toolkit> |
| shmilylty/OneForAll | tool | <https://github.com/shmilylty/OneForAll> |
| ShobhitMishra-bot/SWS-Recon-Tool | tool | <https://github.com/ShobhitMishra-bot/SWS-Recon-Tool> |
| shoebpate1/diffJs | tool | <https://github.com/shoebpate1/diffJs> |
| shoedactylorhizamaculatafuchsii29/osint-username-search | web-platform | <https://github.com/shoedactylorhizamaculatafuchsii29/osint-username-search> |
| ShortTimeNoSee/OSINT-Deck | directory | <https://github.com/ShortTimeNoSee/OSINT-Deck> |
| Shotstars | tool | <https://github.com/snooppr/shotstars> |
| ShtrafKZBot | tool | <https://t.me/ShtrafKZBot> |
| shubaly/lucid-contributions | tool | <https://github.com/shubaly/lucid-contributions> |
| shubhampathak/autosetup | cli-tool | <https://github.com/shubhampathak/autosetup> |
| shuffledns | tool | <https://github.com/projectdiscovery/shuffledns> |
| si9int/cc.py | tool | <https://github.com/si9int/cc.py> |
| sichutancha/TelegramCommentScraper | api-service | <https://github.com/sichutancha/TelegramCommentScraper> |
| sichutancha/YouTubeCommentScraper | tool | <https://github.com/sichutancha/YouTubeCommentScraper> |
| Siddhesh-Agarwal/IP-DB | dataset | <https://github.com/Siddhesh-Agarwal/IP-DB> |
| sidxparab/Subdomain-Enumeration-Guide | dashboard | <https://github.com/sidxparab/Subdomain-Enumeration-Guide> |
| siedysoes/csix-osint | tool | <https://github.com/siedysoes/csix-osint> |
| Signal | tool | <https://signal.org> |
| Silent circle | tool | <https://www.silentcircle.com> |
| Silobreaker | tool | <https://www.silobreaker.com> |
| SiloGit/OSINT-and-Redteam-Grimoire | tool | <https://github.com/SiloGit/OSINT-and-Redteam-Grimoire> |
| SilverPoision/Rock-ON | tool | <https://github.com/SilverPoision/Rock-ON> |
| Similar Web | research-project | <https://www.similarweb.com> |
| SimilarSites | tool | <https://www.similarsites.com> |
| Simon-s-trash-pile/Heimdall | framework | <https://github.com/Simon-s-trash-pile/Heimdall> |
| simplelogin.io | web-platform | <https://simplelogin.io/> |
| SimplyHired | tool | <https://www.simplyhired.com> |
| SimplySecurity/SimplyEmail | framework | <https://github.com/SimplySecurity/SimplyEmail> |
| SirYadav1/AdwanceSNI-2.0 | cli-tool | <https://github.com/SirYadav1/AdwanceSNI-2.0> |
| SiteQ8/PublicEye | plugin | <https://github.com/SiteQ8/PublicEye> |
| SitesLike | tool | <https://www.siteslike.com> |
| SiteSucker | tool | <https://ricks-apps.com/osx/sitesucker/index.html> |
| Siv-nick/WhoCord | dashboard | <https://github.com/Siv-nick/WhoCord> |
| six2dez/dorks_hunter | tool | <https://github.com/six2dez/dorks_hunter> |
| six2dez/reconftw | tool | <https://github.com/six2dez/reconftw> |
| Skopenow | tool | <https://www.skopenow.com/news> |
| skriptkiddy98x/osint-atlas | awesome-list | <https://github.com/skriptkiddy98x/osint-atlas> |
| skynet0x01/tugarecon | framework | <https://github.com/skynet0x01/tugarecon> |
| sl4x0/subfree | api-service | <https://github.com/sl4x0/subfree> |
| Sleipnir | tool | <https://www.fenrir-inc.com/jp/sleipnir> |
| Sleuth For The Truth | tool | <http://sleuthforthetruth.com/> |
| SlideShare | tool | <https://www.slideshare.net> |
| Slimjet | tool | <https://www.slimjet.com> |
| SmallSEOTools | research-project | <https://smallseotools.com> |
| SmartImage | tool | <https://github.com/Decimation/SmartImage> |
| smitovski/BlackSearchV5 | tool | <https://github.com/smitovski/BlackSearchV5> |
| SMS Activate | tool | <https://t.me/PrivatePhoneBot> |
| SnailSploit/Awesome-Snail-OSINT | awesome-list | <https://github.com/SnailSploit/Awesome-Snail-OSINT> |
| SnapIntel | api-service | <https://github.com/Kr0wZ/SnapIntel> |
| Snappa | tool | <https://snappa.io> |
| snippet.host | tool | <https://snippet.host/> |
| snooppr/snoop | api-service | <https://github.com/snooppr/snoop> |
| snooptsz/findanyfile | tool | <https://github.com/snooptsz/findanyfile> |
| Snopes | tool | <https://www.snopes.com> |
| Snort | tool | <https://www.snort.org> |
| snov.io | tool | <https://snov.io/> |
| Snov.io | tool | <https://snov.io/email-finder> |
| snscrape | api-service | <https://github.com/JustAnotherArchivist/snscrape> |
| snuri00/osint-mcp | web-platform | <https://github.com/snuri00/osint-mcp> |
| Snusbase API | api-service | <https://snusbase.com/api> |
| SOAR | research-project | <https://soar.earth/> |
| socai-io/jev-social | cli-tool | <https://github.com/socai-io/jev-social> |
| Social DownORNot | tool | <http://social.downornot.com> |
| Social Links | tool | <https://blog.sociallinks.io/> |
| Social Searcher | tool | <https://www.social-searcher.com> |
| SocialBakers | tool | <https://www.socialbakers.com> |
| SocialBlade | tool | <https://socialblade.com> |
| Socialcatfish | tool | <https://socialcatfish.com/> |
| SocialLinks-IO/sociallinks-api | api-service | <https://github.com/SocialLinks-IO/sociallinks-api> |
| socialmention.com | web-platform | <http://socialmention.com/> |
| SOCRadar | web-platform | <https://socradar.io> |
| SoGou (China) | tool | <https://www.sogou.com/> |
| some-man1/OSINT-IP | api-service | <https://github.com/some-man1/OSINT-IP> |
| Songbird0x77/netcrawler | tool | <https://github.com/Songbird0x77/netcrawler> |
| Soovle | research-project | <https://www.soovle.com> |
| SORRYSPLASH/Stalker | tool | <https://github.com/SORRYSPLASH/Stalker> |
| SOsintOps/Argos | tool | <https://github.com/SOsintOps/Argos> |
| SOsintOps/claudii-exploratores | tool | <https://github.com/SOsintOps/claudii-exploratores> |
| SOsintOps/Wukong | tool | <https://github.com/SOsintOps/Wukong> |
| sotelodev2008/Sotelosint | cli-tool | <https://github.com/sotelodev2008/Sotelosint> |
| sou1ton-exe/GENESIS-OSINT-Tool-v1.1.0 | tool | <https://github.com/sou1ton-exe/GENESIS-OSINT-Tool-v1.1.0> |
| SoundCounselorSpeak/arcabit-internet-security-2026 | tool | <https://github.com/SoundCounselorSpeak/arcabit-internet-security-2026> |
| Sourcebot | directory | <https://www.sourcebot.dev/> |
| SourceGraph | tool | <https://sourcegraph.com/search> |
| Sources | tool | <https://www.sources.com> |
| SourcingDenis/free-online-competitive-intelligence | awesome-list | <https://github.com/SourcingDenis/free-online-competitive-intelligence> |
| soxoj/awesome-osint-mcp-servers | awesome-list | <https://github.com/soxoj/awesome-osint-mcp-servers> |
| soxoj/claude-osint-deploy | plugin | <https://github.com/soxoj/claude-osint-deploy> |
| soxoj/counter-osint-guide-ru | dashboard | <https://github.com/soxoj/counter-osint-guide-ru> |
| soxoj/maigret | api-service | <https://github.com/soxoj/maigret> |
| soxoj/marple | plugin | <https://github.com/soxoj/marple> |
| soxoj/noimosiny-checker | tool | <https://github.com/soxoj/noimosiny-checker> |
| soxoj/osint-cli-tool-skeleton | cli-tool | <https://github.com/soxoj/osint-cli-tool-skeleton> |
| soxoj/osint-namecheckers-list | awesome-list | <https://github.com/soxoj/osint-namecheckers-list> |
| soxoj/socid-extractor | api-service | <https://github.com/soxoj/socid-extractor> |
| soxoj/telegram-bot-dumper | api-service | <https://github.com/soxoj/telegram-bot-dumper> |
| Spacebin | tool | <https://spaceb.in/> |
| Spade-sec/jsowl | api-service | <https://github.com/Spade-sec/jsowl> |
| Spamhaus | tool | <https://check.spamhaus.org/> |
| Speakezee | tool | <https://www.speakezee.org> |
| SpectralOps/netz | tool | <https://github.com/SpectralOps/netz> |
| spekulatius/first-last | tool | <https://github.com/spekulatius/first-last> |
| SpiderFoot | tool | <https://github.com/smicallef/spiderfoot> |
| SpiderFoot | plugin | <https://www.spiderfoot.net> |
| SpiderLabs/HostHunter | tool | <https://github.com/SpiderLabs/HostHunter> |
| Spideroak | tool | <https://spideroak.com> |
| SpiderSuite | dashboard | <https://github.com/3nock/SpiderSuite> |
| spidersuite/SpiderSuite | dashboard | <https://github.com/spidersuite/SpiderSuite> |
| Spix0r/cloudrecon | tool | <https://github.com/Spix0r/cloudrecon> |
| Spix0r/robofinder | tool | <https://github.com/Spix0r/robofinder> |
| spmedia/Threat-Actor-Usernames-Scrape | api-service | <https://github.com/spmedia/Threat-Actor-Usernames-Scrape> |
| Spokeo | tool | <https://www.spokeo.com> |
| Spoof Me | plugin | <https://spoof-me.com/> |
| SpoofCheck | tool | <https://spoofchecker.online/> |
| spotify_monitor | web-platform | <https://github.com/misiektoja/spotify_monitor> |
| spotify_profile_monitor | web-platform | <https://github.com/misiektoja/spotify_profile_monitor> |
| Springer | tool | <https://link.springer.com> |
| Spy Dialer | research-project | <https://spydialer.com/> |
| spyboy-productions/omnisci3nt | directory | <https://github.com/spyboy-productions/omnisci3nt> |
| SpyCloud | tool | <https://spycloud.com> |
| SpyFu | research-project | <https://www.spyfu.com> |
| SpyGGbot | tool | <https://telegram.me/SpyGGbot> |
| Spyk3r/DomainDNA | tool | <https://github.com/Spyk3r/DomainDNA> |
| spyschools/osint-indonesia-v4 | api-service | <https://github.com/spyschools/osint-indonesia-v4> |
| spyschools/osint-spyschools | framework | <https://github.com/spyschools/osint-spyschools> |
| SRWare Iron | tool | <https://www.srware.net/en/software_srware_iron.php> |
| sshh12/llm_osint | api-service | <https://github.com/sshh12/llm_osint> |
| StackExchange | tool | <https://stackexchange.com> |
| stanfrbd/cyberbro | container | <https://github.com/stanfrbd/cyberbro> |
| statikkills/Astra | framework | <https://github.com/statikkills/Astra> |
| statikkills/Bloom---OSINT-Framework | dataset | <https://github.com/statikkills/Bloom---OSINT-Framework> |
| Statista | tool | <https://www.statista.com> |
| StatsCrop | research-project | <https://www.statscrop.com> |
| Steam-OSINT | tool | <https://github.com/matiash26/steam-osint> |
| Steganography Online Codec | tool | <https://www.pelock.com/products/steganography-online-codec> |
| stored.website | tool | <https://stored.website> |
| StormBrawlerSack/legwork-osint-ai-investigator | research-project | <https://github.com/StormBrawlerSack/legwork-osint-ai-investigator> |
| Storyful | tool | <https://storyful.com> |
| StoryMap | tool | <https://storymap.knightlab.com> |
| StoryMaps | research-project | <https://storymaps.arcgis.com/en> |
| Street Crime Map | research-project | <https://streetcrimemap.co.uk/> |
| StuccoSwordsmanStyle/pegboard-osint-toolkit | framework | <https://github.com/StuccoSwordsmanStyle/pegboard-osint-toolkit> |
| stukryptx/DarkLens | web-platform | <https://github.com/stukryptx/DarkLens> |
| Sub3 Suite | plugin | <https://github.com/3nock/sub3suite> |
| SubDomainRadar.io | research-project | <https://subdomainradar.io> |
| Subhunt | api-service | <https://github.com/ahmadouniass/Subdomains-finder-subhunt> |
| Sublist3r | tool | <https://github.com/aboul3la/Sublist3r> |
| Subreddits | tool | <https://subreddits.org> |
| SubredditStats | tool | <https://subredditstats.com> |
| subzeroid/instagrapi | api-service | <https://github.com/subzeroid/instagrapi> |
| succinylcholinefrenchleave974/FIXTT | dataset | <https://github.com/succinylcholinefrenchleave974/FIXTT> |
| SunCalc | research-project | <https://www.suncalc.org/> |
| sundowndev/phoneinfoga | framework | <https://github.com/sundowndev/phoneinfoga> |
| Superdesk | tool | <https://www.superdesk.org> |
| superhedgy/AttackSurfaceMapper | tool | <https://github.com/superhedgy/AttackSurfaceMapper> |
| SuprisedNerd/sshdetective | tool | <https://github.com/SuprisedNerd/sshdetective> |
| Surfface | tool | <https://surfface.com> |
| Surftg_bot | tool | <https://t.me/surftg_bot> |
| Surveilliance Self Defense | tool | <https://ssd.eff.org> |
| swanandx/rustywitness | cli-tool | <https://github.com/swanandx/rustywitness> |
| Swisscows | tool | <https://swisscows.com/> |
| Sybil-Scan/revwhoix | api-service | <https://github.com/Sybil-Scan/revwhoix> |
| Sybil-Scan/TLDbrute | tool | <https://github.com/Sybil-Scan/TLDbrute> |
| sylhetyhackvenger/DIGITALDART | cli-tool | <https://github.com/sylhetyhackvenger/DIGITALDART> |
| sylhetyhackvenger/GOBLIN-Tsunami | framework | <https://github.com/sylhetyhackvenger/GOBLIN-Tsunami> |
| sylhetyhackvenger/NetWhisper | tool | <https://github.com/sylhetyhackvenger/NetWhisper> |
| sylhetyhackvenger/NombreHUNT | plugin | <https://github.com/sylhetyhackvenger/NombreHUNT> |
| sylhetyhackvenger/RootEye | cli-tool | <https://github.com/sylhetyhackvenger/RootEye> |
| sylhetyhackvenger/ShadowTrace | web-platform | <https://github.com/sylhetyhackvenger/ShadowTrace> |
| sylhetyhackvenger/Silkfang | tool | <https://github.com/sylhetyhackvenger/Silkfang> |
| sylhetyhackvenger/STRATASCAN | tool | <https://github.com/sylhetyhackvenger/STRATASCAN> |
| sylhetyhackvenger/SubOracle | framework | <https://github.com/sylhetyhackvenger/SubOracle> |
| sylhetyhackvenger/TikTap | api-service | <https://github.com/sylhetyhackvenger/TikTap> |
| Sync.ME | research-project | <https://sync.me/> |
| SyntaxSouq/osintflow | api-service | <https://github.com/SyntaxSouq/osintflow> |
| syswraith/heimdall | api-service | <https://github.com/syswraith/heimdall> |
| t.me/cyberbezopasno | tool | <https://t.me/cyberbezopasno> |
| t.me/OSINT_group | tool | <https://t.me/OSINT_group> |
| t.me/overbafer1 | tool | <https://t.me/overbafer1> |
| t.me/Social_engineering | tool | <https://t.me/Social_engineering> |
| Tableau | tool | <https://www.tableau.com> |
| Tableau | research-project | <https://www.tableausoftware.com> |
| Tableau Public | tool | <https://public.tableau.com> |
| TABurns27/burn-suite | tool | <https://github.com/TABurns27/burn-suite> |
| Tagboard | tool | <https://tagboard.com> |
| Tagdef | tool | <https://tagdef.com> |
| Tagul | tool | <https://tagul.com> |
| tahsan2544/Email-SPY | framework | <https://github.com/tahsan2544/Email-SPY> |
| Tails | tool | <https://tails.boum.org> |
| tal7aouy/tracekit | framework | <https://github.com/tal7aouy/tracekit> |
| Talkaboutcybersecurity/GitMonitor | tool | <https://github.com/Talkaboutcybersecurity/GitMonitor> |
| Talkwalker | tool | <https://www.talkwalker.com> |
| tamimhasan404/Chart-Of-Wordlist | awesome-list | <https://github.com/tamimhasan404/Chart-Of-Wordlist> |
| tamimhasan404/FFUF-Tips-And-Tricks | tool | <https://github.com/tamimhasan404/FFUF-Tips-And-Tricks> |
| tamimhasan404/Google-Dorks | tool | <https://github.com/tamimhasan404/Google-Dorks> |
| tamimhasan404/Nmap-Cheat-Sheet | tool | <https://github.com/tamimhasan404/Nmap-Cheat-Sheet> |
| tamimhasan404/Oneliner404 | tool | <https://github.com/tamimhasan404/Oneliner404> |
| tamimhasan404/Wordlist404 | tool | <https://github.com/tamimhasan404/Wordlist404> |
| Taonn/EmailAll | tool | <https://github.com/Taonn/EmailAll> |
| tar1090 | tool | <https://github.com/wiedehopf/tar1090> |
| taranis-ai/taranis-ai | tool | <https://github.com/taranis-ai/taranis-ai> |
| TaranYourAss/gitside-man | tool | <https://github.com/TaranYourAss/gitside-man> |
| Taringa (Latin America) | tool | <http://www.taringa.net> |
| tatsuya6502/recon_ex | tool | <https://github.com/tatsuya6502/recon_ex> |
| Taylor & Francis Online | tool | <https://www.tandfonline.com> |
| tbckr/trident | framework | <https://github.com/tbckr/trident> |
| tbrazilosintz78/tbrazilosintz78.github.io | web-platform | <https://github.com/tbrazilosintz78/tbrazilosintz78.github.io> |
| tdh8316/Investigo | cli-tool | <https://github.com/tdh8316/Investigo> |
| Te-k/harpoon | framework | <https://github.com/Te-k/harpoon> |
| Teamingzooper/omnisint | cli-tool | <https://github.com/Teamingzooper/omnisint> |
| tech-anupam/OSINTFORIND | framework | <https://github.com/tech-anupam/OSINTFORIND> |
| tegridydev/python-OSINT-notebook | dashboard | <https://github.com/tegridydev/python-OSINT-notebook> |
| Telegago | tool | <https://cse.google.com/cse?q=+&cx=006368593537057042503:efxu7xprihg#gsc.tab=0&gsc.q=%20&gsc.page=1> |
| Telegram channels scraper TeleGraphite | tool | <https://github.com/hamodywe/telegram-scraper-TeleGraphite> |
| Telegram Finder | tool | <https://www.telegram-finder.io/> |
| Telegram Nearby Map | library | <https://github.com/tejado/telegram-nearby-map> |
| Telegram Search (lyzem.com) | tool | <https://lyzem.com> |
| Telegram-Archive | tool | <https://github.com/GeiserX/Telegram-Archive> |
| telegram-phone-number-checker | tool | <https://github.com/bellingcat/telegram-phone-number-checker> |
| TelegramDB/TelegramDB | web-platform | <https://github.com/TelegramDB/TelegramDB> |
| Telemetr | tool | <https://telemetr.io> |
| Telepahty | tool | <https://github.com/proseltd/Telepathy-Community> |
| Telepathy | framework | <https://github.com/prose-intelligence-ltd/Telepathy-Community> |
| Telerecon | framework | <https://github.com/sockysec/Telerecon> |
| TeleSearch | tool | <https://telesearch.me/> |
| Teleteg | tool | <https://teleteg.com/> |
| TeleTracker | tool | <https://github.com/tsale/TeleTracker> |
| telpoisk.com | directory | <https://telpoisk.com/> |
| terlinH4X/Track-IP-Address | api-service | <https://github.com/terlinH4X/Track-IP-Address> |
| termuxhackers-id/sigit | framework | <https://github.com/termuxhackers-id/sigit> |
| TermuxHackz/X-osint | dataset | <https://github.com/TermuxHackz/X-osint> |
| testpilot8105/barghest | tool | <https://github.com/testpilot8105/barghest> |
| Text Machine | tool | <https://textmachine.org/en/text-tools/cipher-identifier> |
| Textures.js | tool | <https://riccardoscalco.github.io/textures> |
| tg-chat-dump | dataset | <https://github.com/renkagod/tg-chat-dump> |
| tgcrawler | tool | <https://github.com/iggisv9t/tgcrawler> |
| TgramSearch | directory | <https://tgramsearch.com/> |
| tgscan | tool | <https://github.com/tgscan/tgscan> |
| TGScope | directory | <https://tgscope.io/> |
| TGScope Channel Creation Date | tool | <https://tgscope.io/tools/telegram-channel-creation-date> |
| TGStat | web-platform | <https://tgstat.com/> |
| th3unkn0n/osi.ig | tool | <https://github.com/th3unkn0n/osi.ig> |
| Thale's Cyberthreat Map | tool | <https://cds.thalesgroup.com/en/cyberthreat/hitmap> |
| thalha-a9/helix | tool | <https://github.com/thalha-a9/helix> |
| That'sThem | tool | <https://thatsthem.com> |
| ThatsThem | tool | <https://thatsthem.com/reverse-email-lookup> |
| The Atlas of Economic Complexity | tool | <https://atlas.cid.harvard.edu> |
| The Citizen Lab | dataset | <https://citizenlab.ca/feed/> |
| The Collection of Computer Science Bibliographies | tool | <https://liinwww.ira.uka.de/bibliography/index.html> |
| The Data and Story Library | library | <https://lib.stat.cmu.edu/DASL> |
| The Hidden Wiki | directory | <https://thehiddenwiki.org> |
| The National Archives (UK) | tool | <https://www.nationalarchives.gov.uk> |
| The Old Reader | tool | <https://theoldreader.com> |
| The Open Syllabus Project | tool | <https://opensyllabusproject.org/> |
| The Web Application Hacker's Handbook (book) | web-platform | <https://www.amazon.com/dp/1118026470> |
| The-Osint-Toolbox/Email-Username-OSINT | tool | <https://github.com/The-Osint-Toolbox/Email-Username-OSINT> |
| The-Osint-Toolbox/OSINT-Browser-Extensions | browser-extension | <https://github.com/The-Osint-Toolbox/OSINT-Browser-Extensions> |
| The-Osint-Toolbox/OSINT-Communities-Practitioners | tool | <https://github.com/The-Osint-Toolbox/OSINT-Communities-Practitioners> |
| The-Osint-Toolbox/Social-Media-OSINT | tool | <https://github.com/The-Osint-Toolbox/Social-Media-OSINT> |
| The-Osint-Toolbox/Telegram-OSINT | plugin | <https://github.com/The-Osint-Toolbox/Telegram-OSINT> |
| The-Osint-Toolbox/Telephone-OSINT | tool | <https://github.com/The-Osint-Toolbox/Telephone-OSINT> |
| The-Osint-Toolbox/Website-OSINT | tool | <https://github.com/The-Osint-Toolbox/Website-OSINT> |
| theahmadov/slash | tool | <https://github.com/theahmadov/slash> |
| TheArqsz/JSRecon-Buddy | browser-extension | <https://github.com/TheArqsz/JSRecon-Buddy> |
| TheBinitGhimire/GitHub-Recon | tool | <https://github.com/TheBinitGhimire/GitHub-Recon> |
| thebristolsound/birdbrain | desktop-app | <https://github.com/thebristolsound/birdbrain> |
| thecyberneh/scriptkiddi3 | cli-tool | <https://github.com/thecyberneh/scriptkiddi3> |
| thefr0gg/sleuth | tool | <https://github.com/thefr0gg/sleuth> |
| thehananasif/Mr.Homes-by-Hanan-Asif | api-service | <https://github.com/thehananasif/Mr.Homes-by-Hanan-Asif> |
| thehappydinoa/awesome-censys-queries | awesome-list | <https://github.com/thehappydinoa/awesome-censys-queries> |
| theHarvester | tool | <https://github.com/laramies/theHarvester> |
| theintercept.com | web-platform | <https://theintercept.com/> |
| thekaix/cyber-ops-automation | tool | <https://github.com/thekaix/cyber-ops-automation> |
| thelikes/fuzzmost | tool | <https://github.com/thelikes/fuzzmost> |
| TheLinuxndroid/F-OSINT | tool | <https://github.com/TheLinuxndroid/F-OSINT> |
| theosintvault/vaulttrace-imei | dataset | <https://github.com/theosintvault/vaulttrace-imei> |
| These Are the Tools Open Source Researchers Say They Need | research-project | <https://www.bellingcat.com/resources/2022/08/12/these-are-the-tools-open-source-researchers-say-they-need/> |
| thevillagehacker/Bug-Hunting-Arsenal | framework | <https://github.com/thevillagehacker/Bug-Hunting-Arsenal> |
| TheWebCo | tool | <https://thewebco.ai> |
| thewhiteh4t/nexfil | tool | <https://github.com/thewhiteh4t/nexfil> |
| thewhiteh4t/pwnedOrNot | api-service | <https://github.com/thewhiteh4t/pwnedOrNot> |
| thomashousset/WayTrace | api-service | <https://github.com/thomashousset/WayTrace> |
| Threads | tool | <https://www.threads.net> |
| Threat Actor Username Search | tool | <https://threatactorusernames.com> |
| ThreatConnect | web-platform | <https://threatconnect.com> |
| ThreatFox | web-platform | <https://threatfox.abuse.ch> |
| ThreatMiner | web-platform | <https://www.threatminer.org/> |
| ThreatQ | web-platform | <https://www.threatq.com> |
| ThreatsEye \| Live Cyber Threat Map | tool | <https://threatseye.io/threats-map> |
| thumpersecure/Telespot | tool | <https://github.com/thumpersecure/Telespot> |
| thumpersecure/Telespotter | tool | <https://github.com/thumpersecure/Telespotter> |
| Thunderbird | tool | <https://www.mozilla.org/en-US/thunderbird> |
| Thunderbird | tool | <https://www.thunderbird.net/en-US/> |
| Tianyancha | web-platform | <https://www.tianyancha.com/> |
| TIGMINT/TIGMINT | dashboard | <https://github.com/TIGMINT/TIGMINT> |
| tik-spyder | cli-tool | <https://github.com/estebanpdl/tik-spyder> |
| Tik-tok | tool | <https://datanews.github.io/tik-tok> |
| Tiki-toki | tool | <https://www.tiki-toki.com> |
| TikTok Finder Country | tool | <https://tiktokfindercountry.xyz> |
| TikTokStalker | tool | <https://tiktok.einzzcookie.org> |
| tillson/git-hound | tool | <https://github.com/tillson/git-hound> |
| Timeflow | tool | <https://github.com/FlowingMedia/TimeFlow/wiki> |
| Timeline | tool | <https://timeline.knightlab.com> |
| Timeline | tool | <https://www.simile-widgets.org/timeline> |
| Timetoast | tool | <https://www.timetoast.com> |
| Tinder | tool | <https://www.gotinder.com> |
| TinEye | tool | <https://tineye.com> |
| TinyScan | research-project | <https://www.tiny-scan.com> |
| Tme-s | api-service | <https://github.com/axmaier/tme-s> |
| TnYtCoder/DorkScout | api-service | <https://github.com/TnYtCoder/DorkScout> |
| tojo54/HashScope-WebTrace-Browser-History-Analysis | tool | <https://github.com/tojo54/HashScope-WebTrace-Browser-History-Analysis> |
| tomsec8/IntelHub | browser-extension | <https://github.com/tomsec8/IntelHub> |
| Toofr | tool | <https://www.toofr.com> |
| Topic Watch | tool | <https://github.com/0xzerolight/topic_watch> |
| Topix | tool | <http://www.topix.com> |
| topscoder/fourohme | cli-tool | <https://github.com/topscoder/fourohme> |
| Tor Browser | tool | <https://www.torproject.org/projects/torbrowser.html.en> |
| Tor Project | tool | <https://www.torproject.org> |
| Torch | tool | <https://www.torchbrowser.com> |
| TorrentFreak List of VPNs | web-platform | <https://torrentfreak.com/vpn-services-anonymous-review-2017-170304/> |
| toshon-jennings/cassandra | dashboard | <https://github.com/toshon-jennings/cassandra> |
| TOsint | research-project | <https://github.com/drego85/tosint> |
| Trace | web-platform | <https://trace.manus.space> |
| Trace Labs Blog | dataset | <https://www.tracelabs.org/blog/rss.xml> |
| trace.moe | tool | <https://trace.moe/> |
| TraceFind | tool | <https://tracefind.info> |
| tracelabs.org | tool | <https://tracelabs.org/> |
| TracePoint | cli-tool | <https://kluter.github.io/TracePoint/> |
| TracerouteVisualizer | research-project | <https://kriztalz.sh/traceroute-visualizer/> |
| Tracxn | research-project | <https://tracxn.com> |
| Trading Economics | tool | <https://www.tradingeconomics.com> |
| Transit Visualisation Client | cli-tool | <https://tracker.geops.ch> |
| Transparency.org Corruption Perception Index | directory | <https://www.transparency.org/cpi2015> |
| Trends24 | tool | <https://trends24.in> |
| TRExpertWitness | tool | <https://trexpertwitness.com> |
| Tribal-Chief-001/LittleFinger | framework | <https://github.com/Tribal-Chief-001/LittleFinger> |
| trickest/cloud | tool | <https://github.com/trickest/cloud> |
| trickest/enumerepo | tool | <https://github.com/trickest/enumerepo> |
| trickest/github-logs | api-service | <https://github.com/trickest/github-logs> |
| trickest/insiders | tool | <https://github.com/trickest/insiders> |
| trickest/mgwls | directory | <https://github.com/trickest/mgwls> |
| trickest/mkpath | directory | <https://github.com/trickest/mkpath> |
| trickest/mksub | tool | <https://github.com/trickest/mksub> |
| trickest/scripts | tool | <https://github.com/trickest/scripts> |
| TRM Labs | web-platform | <https://www.trmlabs.com> |
| Trooclick | cli-tool | <https://trooclick.com> |
| Truecaller | research-project | <https://truecaller.com> |
| TruePeopleSearch | tool | <https://www.truepeoplesearch.com/> |
| TrueScreen C2PA Viewer | tool | <https://truescreen.io/c2pa-viewer/> |
| Tsurugi Linux | framework | <https://tsurugi-linux.org/> |
| Tubuep | tool | <https://github.com/bibanon/tubeup> |
| Tumblr | tool | <https://www.tumblr.com> |
| Tumblr Search | tool | <https://www.tumblr.com/search> |
| TuriBot | tool | <https://t.me/TuriBot> |
| TutPaste | tool | <https://tutpaste.com/> |
| tvedad/VEDAD-Terminal | api-service | <https://github.com/tvedad/VEDAD-Terminal> |
| TwChat | tool | <http://twchat.com> |
| TweetAPI Twitter ID Finder | api-service | <https://tweetapi.com/tools/twitter-id-finder> |
| TweetBinder | dashboard | <https://www.tweetbinder.com> |
| TweetDeck | tool | <https://www.tweetdeck.com> |
| TweetMap | tool | <https://github.com/cga-harvard/Data_Science_Big_Data_Projects/tree/master/scripts/Geotweets> |
| TweetMap | tool | <http://mapd.csail.mit.edu/tweetmap> |
| TweetMap | tool | <http://worldmap.harvard.edu/tweetmap> |
| twelvesec/gasmask | tool | <https://github.com/twelvesec/gasmask> |
| TwexAPI Twitter Viewer | api-service | <https://twexapi.io/twitter-viewer> |
| Twilio | api-service | <https://www.twilio.com/docs/lookup/v2-api> |
| Twingly | tool | <https://www.twingly.com> |
| twintproject/twint | api-service | <https://github.com/twintproject/twint> |
| Twitch Search | tool | <https://www.twitch.tv/directory> |
| Twiteur | tool | <https://twiteur.com> |
| Twitter Audit | tool | <https://www.twitteraudit.com> |
| Twitter Chat Schedule | tool | <https://tweetreports.com/twitter-chat-schedule> |
| twscrape | tool | <https://github.com/vladkens/twscrape> |
| txuswashere/Open-Source-INTelligence | awesome-list | <https://github.com/txuswashere/Open-Source-INTelligence> |
| txuswashere/OSINT | framework | <https://github.com/txuswashere/OSINT> |
| tyranroot/Tyra-SherLock | mobile-app | <https://github.com/tyranroot/Tyra-SherLock> |
| tyranroot/User-Osint | framework | <https://github.com/tyranroot/User-Osint> |
| TYTTheo/Osdint | tool | <https://github.com/TYTTheo/Osdint> |
| U-Find | tool | <https://u-find.com> |
| u777-web/x7-osint-toolkit | framework | <https://github.com/u777-web/x7-osint-toolkit> |
| UAV Radar | api-service | <https://uavradar.live/> |
| Ubersuggest | research-project | <https://ubersuggest.org> |
| ubikron/Awesome-AI-OSINT | awesome-list | <https://github.com/ubikron/Awesome-AI-OSINT> |
| uBlock Origin | tool | <https://github.com/gorhill/uBlock> |
| UCBrowser | tool | <https://www.ucweb.com> |
| UCYBERS/Awesome-Blackhat-Tools | awesome-list | <https://github.com/UCYBERS/Awesome-Blackhat-Tools> |
| Ujjwaljain4u/reconagent | api-service | <https://github.com/Ujjwaljain4u/reconagent> |
| UjsGit/Notes-on-OSINT | framework | <https://github.com/UjsGit/Notes-on-OSINT> |
| UK Companies House | tool | <https://find-and-update.company-information.service.gov.uk/> |
| UK Phone Book | tool | <https://www.ukphonebook.com/> |
| Ultimate Social Scrapers | api-service | <https://github.com/harismuneer/Ultimate-Social-Scrapers> |
| umair9747/4oFour | framework | <https://github.com/umair9747/4oFour> |
| umair9747/bucky | web-platform | <https://github.com/umair9747/bucky> |
| Umar-MultiverseCode/OSNIT-TOOLS | directory | <https://github.com/Umar-MultiverseCode/OSNIT-TOOLS> |
| umutcamliyurt/JSRecon | tool | <https://github.com/umutcamliyurt/JSRecon> |
| UN COMTRADE Database | dataset | <https://comtrade.un.org> |
| UN Data | tool | <https://data.un.org> |
| Unamer | tool | <https://telegram.me/unamer_bot> |
| UNCTAD Country Fact Sheets | tool | <https://unctad.org/en/Pages/DIAE/World%20Investment%20Report/Country-Fact-Sheets.aspx> |
| UNCTAD Investment Country Profiles | tool | <https://unctad.org/en/Pages/Publications/Investment-country-profiles.aspx> |
| UNCTAD STAT | tool | <https://unctadstat.unctad.org> |
| UNDPs Human Development Index | directory | <https://hdr.undp.org/en/data> |
| UNECE | tool | <https://w3.unece.org/PXWeb/en> |
| UNESCO Institute for Statistics | tool | <https://uis.unesco.org> |
| Unfurl | tool | <https://dfir.blog/unfurl/> |
| unicodeveloper/globalthreatmap | tool | <https://github.com/unicodeveloper/globalthreatmap> |
| UniCourt | tool | <https://unicourt.com/> |
| UNIDO Statistical Databases | dataset | <https://www.unido.org/resources/statistics/statistical-databases.html> |
| Universal Radio Hacker | tool | <https://github.com/jopohl/urh> |
| Universal Scammer List | tool | <https://universalscammerlist.com/> |
| Unknownx007/NixSINT | cli-tool | <https://github.com/Unknownx007/NixSINT> |
| UNStats Social Indicators | tool | <https://unstats.un.org/unsd/demographic/products/socind> |
| Unternehmensregister | tool | <https://www.unternehmensregister.de/en> |
| Upsala Conflict Data Program | tool | <https://www.pcr.uu.se/research/UCDP> |
| urbanadventurer/urlcrazy | tool | <https://github.com/urbanadventurer/urlcrazy> |
| urbanadventurer/username-anarchy | tool | <https://github.com/urbanadventurer/username-anarchy> |
| urlDNA | research-project | <https://urldna.io/> |
| URLhaus | research-project | <https://urlhaus.abuse.ch> |
| urlQuery | research-project | <https://urlquery.net> |
| urlscan | web-platform | <https://urlscan.io/> |
| urlscan.io/docs/api | api-service | <https://urlscan.io/docs/api/> |
| URLVoid | research-project | <https://www.urlvoid.com> |
| US Data and Statistics | tool | <https://www.usa.gov/statistics> |
| UseOSINT/Skills | web-platform | <https://github.com/UseOSINT/Skills> |
| User Search | tool | <https://www.usersearch.org> |
| User Searcher | tool | <https://www.user-searcher.com> |
| username_to_id_bot | tool | <https://t.me/username_to_id_bot> |
| UserSearch-Public/onequery-api | api-service | <https://github.com/UserSearch-Public/onequery-api> |
| USGS (EarthExplorer) | dataset | <https://earthexplorer.usgs.gov/> |
| UsInfoBot | tool | <https://t.me/usinfobot> |
| USPhoneBook | research-project | <https://www.usphonebook.com/> |
| utkusen/shotlooter | tool | <https://github.com/utkusen/shotlooter> |
| utkusen/socialhunter | research-project | <https://github.com/utkusen/socialhunter> |
| utkusen/urlhunter | web-platform | <https://github.com/utkusen/urlhunter> |
| utkusen/wholeaked | tool | <https://github.com/utkusen/wholeaked> |
| v4d1/Dome | tool | <https://github.com/v4d1/Dome> |
| v4resk/BreachCheck | tool | <https://github.com/v4resk/BreachCheck> |
| Vacato | research-project | <https://vacato.io> |
| vaguileradiaz/tinfoleak | dashboard | <https://github.com/vaguileradiaz/tinfoleak> |
| vaibhavkrjha/shufti | framework | <https://github.com/vaibhavkrjha/shufti> |
| Validin | api-service | <https://app.validin.com/> |
| Validin | tool | <https://www.validin.com/> |
| Vault | research-project | <https://www.vault.com> |
| vault.fbi.gov | desktop-app | <https://vault.fbi.gov/> |
| vaultbin | tool | <https://vaultb.in/> |
| Vehicle Number Search Toolbox | tool | <https://cipher387.github.io/venicle_number_search_toolbox/> |
| Velociraptor Server | tool | <https://docs.velociraptor.app> |
| Venacus | tool | <https://venacus.com> |
| Venngage | tool | <https://venngage.com> |
| Veoh | tool | <https://www.veoh.com> |
| Verification Handbook | tool | <https://verificationhandbook.com> |
| VerifiedHer | tool | <https://verifiedher.com> |
| Verify Email | tool | <https://verify-email.org> |
| Verisign | research-project | <https://dnssec-debugger.verisignlabs.com> |
| versionista | tool | <https://versionista.com> |
| Verybin | tool | <https://www.verybin.com/> |
| VesselFinder | tool | <https://www.vesselfinder.com> |
| vflame6/leaker | tool | <https://github.com/vflame6/leaker> |
| ViaMichelin | research-project | <https://www.viamichelin.com> |
| Video Stabilization Methods | tool | <https://github.com/yaochih/awesome-video-stabilization> |
| View in Google Earth | research-project | <https://www.mgmaps.com/kml/#view> |
| ViewDNS.info | research-project | <https://viewdns.info> |
| Vigilante.pw | directory | <https://vigilante.pw> |
| vijaysahuofficial/UserReCon | web-platform | <https://github.com/vijaysahuofficial/UserReCon> |
| vil/H4X-Tools | api-service | <https://github.com/vil/H4X-Tools> |
| Vimeo | tool | <https://vimeo.com> |
| vincenzo-afk/ReconGPT | plugin | <https://github.com/vincenzo-afk/ReconGPT> |
| VineLink | web-platform | <https://www.vinelink.com/#state-selection> |
| Viralmaniar/BigBountyRecon | tool | <https://github.com/Viralmaniar/BigBountyRecon> |
| Viralmaniar/I-See-You | tool | <https://github.com/Viralmaniar/I-See-You> |
| Viralmaniar/XposedOrNot | tool | <https://github.com/Viralmaniar/XposedOrNot> |
| virtuanista/osint-atlas | awesome-list | <https://github.com/virtuanista/osint-atlas> |
| Virus Total | research-project | <https://www.virustotal.com/> |
| VirusZzHkP/The-Black-Tiger | cli-tool | <https://github.com/VirusZzHkP/The-Black-Tiger> |
| Vis.js | tool | <https://visjs.org> |
| Vishal-HaCkEr1910/Phone-Number-Tracker | api-service | <https://github.com/Vishal-HaCkEr1910/Phone-Number-Tracker> |
| Visme | tool | <https://www.visme.co> |
| Visual Investigative Scenarios | tool | <https://vis.occrp.org> |
| Visualize Free | tool | <https://visualizefree.com> |
| Visualize.me | tool | <http://vizualize.me> |
| visually | tool | <https://create.visual.ly> |
| visualping | tool | <https://visualping.io> |
| Vivaldi | tool | <https://vivaldi.com> |
| vixkram/OSINTBox-data | tool | <https://github.com/vixkram/OSINTBox-data> |
| Vizala | tool | <https://vizala.com> |
| VK Community Search | tool | <https://vk.com/communities> |
| VK People Search | tool | <https://vk.com/people> |
| VK.watch | tool | <https://vk.watch/> |
| vk.watch/ID/profile | tool | <https://vk.watch/ID/profile> |
| VK5 | tool | <https://vk5.city4me.com> |
| VKontakte | tool | <https://vk.com> |
| vkxd/VeltCLI | cli-tool | <https://github.com/vkxd/VeltCLI> |
| VMRay Analyzer | web-platform | <https://www.vmray.com> |
| vognik/maltego-telegram | tool | <https://github.com/vognik/maltego-telegram> |
| VoilaNorbert | research-project | <https://www.voilanorbert.com> |
| VolkanSah/The_Collector | dataset | <https://github.com/VolkanSah/The_Collector> |
| voltsparx/Silinocide-C | framework | <https://github.com/voltsparx/Silinocide-C> |
| voltsparx/Silinosic-X | web-platform | <https://github.com/voltsparx/Silinosic-X> |
| Vortex | tool | <https://www.dotmatics.com/products/vortex> |
| Vortimo OSINT Tool | browser-extension | <https://www.vortimo.com/> |
| Voter Records | research-project | <https://voterrecords.com/> |
| VPN Comparison by That One Privacy Guy | web-platform | <https://thatoneprivacysite.net/> |
| VPNDetection | browser-extension | <https://vpndetection.io> |
| vsec7/BurpSuite-Xkeys | plugin | <https://github.com/vsec7/BurpSuite-Xkeys> |
| VulnHub | tool | <https://www.vulnhub.com> |
| VulnYX | web-platform | <https://vulnyx.com> |
| vvspower/pinosin | framework | <https://github.com/vvspower/pinosin> |
| vx-underground | research-project | <https://vx-underground.org/> |
| w0h1v/mcp-maigret | container | <https://github.com/w0h1v/mcp-maigret> |
| w0h1v/mcp-shodan | api-service | <https://github.com/w0h1v/mcp-shodan> |
| w3snoop | research-project | <https://webboar.com.w3snoop.com> |
| wakeful/veil | tool | <https://github.com/wakeful/veil> |
| Walla (Israel) | tool | <https://www.walla.co.il> |
| WalletExplorer | web-platform | <https://www.walletexplorer.com/> |
| WalletLabels | api-service | <https://www.walletlabels.xyz> |
| Wappalyzer | framework | <https://www.wappalyzer.com/> |
| WatchDogSecurity/porch-pirate | api-service | <https://github.com/WatchDogSecurity/porch-pirate> |
| Waterfox | tool | <https://www.waterfox.net/> |
| WATools | tool | <https://watools.io/> |
| wavefnx/sigmund | cli-tool | <https://github.com/wavefnx/sigmund> |
| Wayback Machine | tool | <http://archive.org/web/web.php> |
| Wayback Machine | tool | <https://web.archive.org/> |
| Wayback Machine Archiver | tool | <https://github.com/jsvine/waybackpack> |
| Wayback-Archive | tool | <https://github.com/GeiserX/Wayback-Archive> |
| Wayback-Diff | tool | <https://github.com/GeiserX/Wayback-Diff> |
| Waybackurls | tool | <https://github.com/tomnomnom/waybackurls> |
| waymore | tool | <https://github.com/xnl-h4ck3r/waymore> |
| WayTrace | api-service | <https://waytrace.org/> |
| wddadk/Offensive-OSINT-Tools | awesome-list | <https://github.com/wddadk/Offensive-OSINT-Tools> |
| weakpass.com | tool | <https://weakpass.com/> |
| wearlig/Phone-number-OSINT | framework | <https://github.com/wearlig/Phone-number-OSINT> |
| wearlig/Telegram-Osint | framework | <https://github.com/wearlig/Telegram-Osint> |
| Web Archives | browser-extension | <https://github.com/dessant/web-archives> |
| Web Resource Ledger | api-service | <https://webresourceledger.com> |
| Web-Check | research-project | <https://web-check.as93.net/> |
| web-check.xyz | tool | <https://web-check.xyz/> |
| webamon-org/webamon-cli | cli-tool | <https://github.com/webamon-org/webamon-cli> |
| webanalyze | tool | <https://github.com/rverton/webanalyze> |
| WebAssistant | tool | <https://www.proxy-offline-browser.com/download.html> |
| WebBreacher/obsidian-osint-templates | tool | <https://github.com/WebBreacher/obsidian-osint-templates> |
| WebBreacher/WhatsMyName | dataset | <https://github.com/WebBreacher/WhatsMyName> |
| WebMeUp | directory | <https://webmeup.com> |
| WebMii | tool | <https://webmii.com> |
| WebReader | tool | <https://www.getwebreader.com> |
| Webscore | research-project | <https://garvit835.github.io/WebScore/> |
| Webscout | research-project | <https://webscout.io/> |
| Website Informer | research-project | <https://website.informer.com> |
| Website Ripper Copier | tool | <https://www.tensons.com/products/websiterippercopier> |
| WebSite Watcher | tool | <https://www.aignes.com/index.htm> |
| WebsiteTechMiner.py | api-service | <https://github.com/cybersader/WebsiteTechMiner-py> |
| Weibo (China) | tool | <https://weibo.com> |
| west-wind/abuse-insights | tool | <https://github.com/west-wind/abuse-insights> |
| west-wind/LAR | cli-tool | <https://github.com/west-wind/LAR> |
| WhatIsMyIPAddress | research-project | <https://whatismyipaddress.com> |
| Whatsapp CheckLeaked | api-service | <https://whatsapp.checkleaked.cc/> |
| WhatsApp-OSINT | tool | <https://github.com/kinghacker0/WhatsApp-OSINT> |
| WhatsInMyFile | tool | <https://whatsinmyfile.com/> |
| WhatsMyName | web-platform | <https://whatsmyname.app/> |
| White Pages (US) | tool | <https://www.whitepages.com> |
| WhiteIntel | research-project | <https://whiteintel.dev> |
| whiterabb17/sifter | framework | <https://github.com/whiterabb17/sifter> |
| WHO Data | tool | <https://www.who.int/gho/en> |
| Who.is | research-project | <https://who.is/> |
| whoamijas0n/Soranin | framework | <https://github.com/whoamijas0n/Soranin> |
| WHOIS / RDAP | tool | <https://www.whois.com/whois/> |
| Whois Arin Online | api-service | <https://whois.arin.net> |
| whois.com | tool | <https://www.whois.com/> |
| WhoisDomBot | tool | <https://t.me/WhoisDomBot> |
| WhoIsHostingThis | research-project | <https://www.whoishostingthis.com> |
| WhoisMind | research-project | <https://www.whoismind.com> |
| Whoisology | research-project | <https://whoisology.com> |
| WhoIsRequest | research-project | <https://whoisrequest.com> |
| whoisxmlapi.com | api-service | <https://whoisxmlapi.com/> |
| whoownswhat.justfix.org | tool | <https://whoownswhat.justfix.org/en/> |
| whopostedwhat.com | web-platform | <https://whopostedwhat.com/> |
| WhosBuilt | research-project | <https://whosbuilt.com> |
| whosouvikkk/moonwitch-osint-bot | api-service | <https://github.com/whosouvikkk/moonwitch-osint-bot> |
| Whoxy | api-service | <https://www.whoxy.com> |
| Wickr | tool | <https://wickr.com> |
| WiGLE | dataset | <https://wigle.net/> |
| Wikidata | tool | <https://www.wikidata.org> |
| wikileaks.org | web-platform | <https://wikileaks.org/> |
| Wikimapia | api-service | <https://wikimapia.org> |
| Wikipedia | tool | <https://en.wikipedia.org> |
| Wiley | tool | <http://eu.wiley.com> |
| Wiley | tool | <https://www.wiley.com> |
| Winds | tool | <https://winds.getstream.io> |
| Windy | research-project | <https://www.windy.com/> |
| WIPO | tool | <https://www3.wipo.int/branddb/en/> |
| wirzka/incursore | tool | <https://github.com/wirzka/incursore> |
| Wolfram Alpha | tool | <https://www.wolframalpha.com> |
| Wolfram Alpha Facebook Report | tool | <https://www.wolframalpha.com/input/?i=facebook+report> |
| wolfsecur1ty/InvMap | cli-tool | <https://github.com/wolfsecur1ty/InvMap> |
| Word Tracker | research-project | <https://www.wordtracker.com> |
| Wordlist-Generator | framework | <https://github.com/rawfilejson/Wordlist-Generator> |
| World Bank Data | tool | <https://data.worldbank.org> |
| World Bank Data | tool | <https://datatopics.worldbank.org/consumption/home> |
| World Bank Doing Business | tool | <https://www.doingbusiness.org> |
| World Bank Enterprise Surveys | tool | <https://www.enterprisesurveys.org> |
| World Bank Investing Across Borders | tool | <http://iab.worldbank.org> |
| World Digital Library | library | <https://www.wdl.org> |
| World Integrated Trade Solution | tool | <https://wits.worldbank.org> |
| World Monitor | dashboard | <https://www.worldmonitor.app> |
| World-Newspapers | research-project | <https://www.world-newspapers.com> |
| WorldMap Harvard | research-project | <https://worldmap.harvard.edu> |
| WorldNews | tool | <https://wn.com> |
| Worldwide OSINT Tools Map | dataset | <https://cipher387.github.io/osintmap/> |
| WorldWideScience.org | tool | <http://worldwidescience.org> |
| WOT | tool | <https://www.mywot.com> |
| wotschofsky/domain-digger | framework | <https://github.com/wotschofsky/domain-digger> |
| WPF0Ff/Email-Probiv | framework | <https://github.com/WPF0Ff/Email-Probiv> |
| WPF0Ff/Instagram-probiv-osint | tool | <https://github.com/WPF0Ff/Instagram-probiv-osint> |
| WPF0Ff/SteamProbiv | framework | <https://github.com/WPF0Ff/SteamProbiv> |
| WPF0Ff/usa-osint | tool | <https://github.com/WPF0Ff/usa-osint> |
| WPF0Ff/YoutubeProbiv | tool | <https://github.com/WPF0Ff/YoutubeProbiv> |
| Wpscan | tool | <https://wpscan.com> |
| WPTK/aircraft-research-claude-skill | research-project | <https://github.com/WPTK/aircraft-research-claude-skill> |
| Write.as | tool | <https://write.as/> |
| WTO Statistics | tool | <https://www.wto.org/english/res_e/statis_e/statis_e.htm> |
| wuqiao15860/osintPanel | dashboard | <https://github.com/wuqiao15860/osintPanel> |
| Wynyard Group | tool | <https://wynyardgroup.com> |
| x0rr-dan/s1c0n | tool | <https://github.com/x0rr-dan/s1c0n> |
| x0rz/phishing_catcher | tool | <https://github.com/x0rz/phishing_catcher> |
| x1mdev/ReconPi | container | <https://github.com/x1mdev/ReconPi> |
| x1n-Q/OSINT-Hub | dashboard | <https://github.com/x1n-Q/OSINT-Hub> |
| X7-VANTHOR/Reconip | tool | <https://github.com/X7-VANTHOR/Reconip> |
| xadhrit/terra | api-service | <https://github.com/xadhrit/terra> |
| xaitax/x-account-location-device | plugin | <https://github.com/xaitax/x-account-location-device> |
| xajkep/wordlists | tool | <https://github.com/xajkep/wordlists> |
| XDeadHackerX/NetSoc_OSINT | api-service | <https://github.com/XDeadHackerX/NetSoc_OSINT> |
| XDeadHackerX/The_spy_job | dashboard | <https://github.com/XDeadHackerX/The_spy_job> |
| xdisform/Spider | tool | <https://github.com/xdisform/Spider> |
| xdrew87/iris | web-platform | <https://github.com/xdrew87/iris> |
| xenod0chy/osint-gui | dashboard | <https://github.com/xenod0chy/osint-gui> |
| xerohackcom/webrecon | cli-tool | <https://github.com/xerohackcom/webrecon> |
| Xing | tool | <https://www.xing.com> |
| Xing Groups | tool | <https://www.xing.com/communities> |
| xnoncywer/email-osint | research-project | <https://github.com/xnoncywer/email-osint> |
| XORbit01/webpalm | tool | <https://github.com/XORbit01/webpalm> |
| xPloits3c/DorkEye | awesome-list | <https://github.com/xPloits3c/DorkEye> |
| xPloits3c/xPloits3c | tool | <https://github.com/xPloits3c/xPloits3c> |
| xploitstech/Xteam | tool | <https://github.com/xploitstech/Xteam> |
| Xquik | web-platform | <https://xquik.com> |
| Xquik-dev/x-twitter-advanced-search | api-service | <https://github.com/Xquik-dev/x-twitter-advanced-search> |
| xReverseLabs/Api-Documentation | api-service | <https://github.com/xReverseLabs/Api-Documentation> |
| xReverseLabs/SubRecon | tool | <https://github.com/xReverseLabs/SubRecon> |
| xsser01/phantomcollect | framework | <https://github.com/xsser01/phantomcollect> |
| XyberWolf/ReconWolf | tool | <https://github.com/XyberWolf/ReconWolf> |
| Y0oshi/Project-Deep-Focus | dashboard | <https://github.com/Y0oshi/Project-Deep-Focus> |
| Yahoo Answers | tool | <https://answers.yahoo.com> |
| Yahoo Groups | tool | <https://groups.yahoo.com> |
| Yahoo Image Search | tool | <https://images.search.yahoo.com> |
| Yahoo Maps | research-project | <https://maps.yahoo.com> |
| Yahoo News | tool | <https://news.yahoo.com> |
| Yahoo Video Search | tool | <https://video.search.yahoo.com> |
| Yahoo! Search | tool | <https://www.yahoo.com> |
| Yandex (Russia) | tool | <https://www.yandex.com> |
| Yandex Wordstat | research-project | <https://wordstat.yandex.com> |
| Yangtoinette/LAB-OSINT-Writeups | tool | <https://github.com/Yangtoinette/LAB-OSINT-Writeups> |
| Yangtoinette/OSINT-Industries-Writeups | tool | <https://github.com/Yangtoinette/OSINT-Industries-Writeups> |
| Yangtoinette/OSINTOPIA-Writeups | tool | <https://github.com/Yangtoinette/OSINTOPIA-Writeups> |
| YARAif | tool | <https://yaraify.abuse.ch/scan/> |
| YARAify | tool | <https://yaraify.abuse.ch/> |
| YashGoti/analyzeJS | tool | <https://github.com/YashGoti/analyzeJS> |
| YashGoti/gal | tool | <https://github.com/YashGoti/gal> |
| YazeedOliwah/Black_Viru5_Recon_v1.0 | tool | <https://github.com/YazeedOliwah/Black_Viru5_Recon_v1.0> |
| yee-yore/DorkAgent | tool | <https://github.com/yee-yore/DorkAgent> |
| yezz123/SoIG | api-service | <https://github.com/yezz123/SoIG> |
| yogeshojha/rengine | web-platform | <https://github.com/yogeshojha/rengine> |
| yogsec/One-Liner-OSINT | framework | <https://github.com/yogsec/One-Liner-OSINT> |
| yogsec/OSINT-Tools | awesome-list | <https://github.com/yogsec/OSINT-Tools> |
| yogsec/People-Search | web-platform | <https://github.com/yogsec/People-Search> |
| yogsec/Physical-Pentesting-Tools | framework | <https://github.com/yogsec/Physical-Pentesting-Tools> |
| yoramvandevelde/TLSenum | tool | <https://github.com/yoramvandevelde/TLSenum> |
| yottajunaid/SECT_Internship_Project | research-project | <https://github.com/yottajunaid/SECT_Internship_Project> |
| YOU | tool | <https://you.com> |
| You Get Signal | research-project | <https://www.yougetsignal.com> |
| YouControl | research-project | <https://youcontrol.com.ua/en/> |
| YousefNein/OSINT-Hub | api-service | <https://github.com/YousefNein/OSINT-Hub> |
| YouTube Data Viewer | tool | <https://www.amnestyusa.org/citizenevidence> |
| YouTube DataViewer | tool | <https://citizenevidence.amnestyusa.org/> |
| YouTube Geofind | tool | <https://mattw.io/youtube-geofind/> |
| YouTube Metadata | tool | <https://mattw.io/youtube-metadata/> |
| youtube-geofind | tool | <https://github.com/mattwright324/youtube-geofind> |
| Yozoxir/TraceEye | tool | <https://github.com/Yozoxir/TraceEye> |
| yt-dlp | web-platform | <https://github.com/yt-dlp/yt-dlp/> |
| ythx-101/x-tweet-fetcher | api-service | <https://github.com/ythx-101/x-tweet-fetcher> |
| yukselberkay/asnap | web-platform | <https://github.com/yukselberkay/asnap> |
| Yumpu | tool | <https://www.yumpu.com> |
| YusufMarall/p3n4thing | container | <https://github.com/YusufMarall/p3n4thing> |
| yuyudhn/osintname | tool | <https://github.com/yuyudhn/osintname> |
| Yvesssn/DetectDee | tool | <https://github.com/Yvesssn/DetectDee> |
| yyhuni/lunafox | web-platform | <https://github.com/yyhuni/lunafox> |
| z0m31en7/Uscrapper | api-service | <https://github.com/z0m31en7/Uscrapper> |
| ZabaSearch | tool | <https://www.zabasearch.com/> |
| ZakariaBlase/Cyber-Workspace | awesome-list | <https://github.com/ZakariaBlase/Cyber-Workspace> |
| Zanran | tool | <https://zanran.com> |
| Zapmeta | tool | <https://www.zapmeta.com> |
| zaproxy.org | web-platform | <https://zaproxy.org/> |
| Zarcolio/grepaddr | cli-tool | <https://github.com/Zarcolio/grepaddr> |
| Zarebin (Iran) | tool | <https://zarebin.ir> |
| Zauba Corp | web-platform | <https://www.zaubacorp.com/> |
| ZBin | tool | <https://zbin.dev/> |
| Zeemaps | research-project | <https://www.zeemaps.com> |
| zer0yu/xrecon | tool | <https://github.com/zer0yu/xrecon> |
| ZeroBin | tool | <https://sebsauvage.net/paste/> |
| ZeroBounce | web-platform | <https://www.zerobounce.net> |
| Zetoc | tool | <http://zetoc.jisc.ac.uk> |
| zhaji2333/CkSKILLS | tool | <https://github.com/zhaji2333/CkSKILLS> |
| zhongwencool/observer_cli | dashboard | <https://github.com/zhongwencool/observer_cli> |
| Zierax/GoogleDorker | tool | <https://github.com/Zierax/GoogleDorker> |
| zillow.com | tool | <https://zillow.com/> |
| ZingChart | tool | <https://www.zingchart.com> |
| Zintro | tool | <https://www.zintro.com> |
| ZipRecruiter | tool | <https://www.ziprecruiter.com> |
| zlaxtert-code/EMAIL-BOUNCE-CHECKERV4.5.1 | tool | <https://github.com/zlaxtert-code/EMAIL-BOUNCE-CHECKERV4.5.1> |
| zlaxtert-code/PHONE-TRACEV1.0.1 | tool | <https://github.com/zlaxtert-code/PHONE-TRACEV1.0.1> |
| zlaxtert-code/URL-AUTO-SCANNER | plugin | <https://github.com/zlaxtert-code/URL-AUTO-SCANNER> |
| ZMail | tool | <https://zmail.sourceforge.net> |
| Zomato/vinifera | tool | <https://github.com/Zomato/vinifera> |
| Zoom Earth | research-project | <https://zoom.earth/> |
| ZoomEye | tool | <https://www.zoomeye.ai/> |
| Zscaler Global Threat Map Dashboard | dashboard | <https://threatlabz.zscaler.com/cloud-insights/threat-map-dashboard> |
| zuxu4n/Rosint | tool | <https://github.com/zuxu4n/Rosint> |
| Дезертир | tool | <https://vk.com/app3046467> |
| Ответы | tool | <https://otvet.mail.ru/> |
| Фари | tool | <https://telegram.me/faribybot> |

### Onion Search & Discovery

| Name | Type | URL |
|---|---|---|
| 0x1bd/TorMod | tool | <https://github.com/0x1bd/TorMod> |
| 0xddekaee/torcon | web-platform | <https://github.com/0xddekaee/torcon> |
| 0xLeif/Onion-POC | tool | <https://github.com/0xLeif/Onion-POC> |
| 0xPratikPatil/torlens | api-service | <https://github.com/0xPratikPatil/torlens> |
| 0xROOTPLS/Prefix32 | web-platform | <https://github.com/0xROOTPLS/Prefix32> |
| 1ab1/onion-domains | web-platform | <https://github.com/1ab1/onion-domains> |
| 1Birdo/Gostress-Tor-V2 | dashboard | <https://github.com/1Birdo/Gostress-Tor-V2> |
| 3MPER0RR/TorNodeExplore | api-service | <https://github.com/3MPER0RR/TorNodeExplore> |
| 42ways/onion-architecture-blueprint | tool | <https://github.com/42ways/onion-architecture-blueprint> |
| 7erduk/tor | research-project | <https://github.com/7erduk/tor> |
| 7ife/chat-box | dataset | <https://github.com/7ife/chat-box> |
| 90ssolo/monero-tor-i2p-node | tool | <https://github.com/90ssolo/monero-tor-i2p-node> |
| abdullah2993/toker | container | <https://github.com/abdullah2993/toker> |
| abhicodes07/Toralizer | cli-tool | <https://github.com/abhicodes07/Toralizer> |
| abhrankan/luggage-ice | web-platform | <https://github.com/abhrankan/luggage-ice> |
| abiabdillahx/onionize | container | <https://github.com/abiabdillahx/onionize> |
| Abrifq/tor-detector-c | tool | <https://github.com/Abrifq/tor-detector-c> |
| Abrifq/tor-detector-js | tool | <https://github.com/Abrifq/tor-detector-js> |
| adrien2p/accumulator | tool | <https://github.com/adrien2p/accumulator> |
| adventuresin9/9front-mt7688 | tool | <https://github.com/adventuresin9/9front-mt7688> |
| Adytm404/onion-domain-generator | web-platform | <https://github.com/Adytm404/onion-domain-generator> |
| aedenmurray/toc | tool | <https://github.com/aedenmurray/toc> |
| agentofuser/git-remote-tor | web-platform | <https://github.com/agentofuser/git-remote-tor> |
| AgeOfMarcus/hackerman | library | <https://github.com/AgeOfMarcus/hackerman> |
| aghayeffemin/aspnetcore-clean-architecture | api-service | <https://github.com/aghayeffemin/aspnetcore-clean-architecture> |
| agustinfranc/onion-backend-v2 | tool | <https://github.com/agustinfranc/onion-backend-v2> |
| agustinfranc/onion-clientes-frontend | dashboard | <https://github.com/agustinfranc/onion-clientes-frontend> |
| agustinfranc/onion-frontend | dashboard | <https://github.com/agustinfranc/onion-frontend> |
| aIligat0r/TorSocksBag | container | <https://github.com/aIligat0r/TorSocksBag> |
| ajvb/awesome-tor | awesome-list | <https://github.com/ajvb/awesome-tor> |
| ak1t0/flame | web-platform | <https://github.com/ak1t0/flame> |
| alberto2005-coder/TorLite_Browser | research-project | <https://github.com/alberto2005-coder/TorLite_Browser> |
| AlbertSadykovOfficial/tor-http-proxy-server | container | <https://github.com/AlbertSadykovOfficial/tor-http-proxy-server> |
| aldemeery/onion | tool | <https://github.com/aldemeery/onion> |
| alecmuffett/real-world-onion-sites | web-platform | <https://github.com/alecmuffett/real-world-onion-sites> |
| AlexanderLivanov/IntruderToolkit | framework | <https://github.com/AlexanderLivanov/IntruderToolkit> |
| AlexanderYastrebov/onion-vanity-address | web-platform | <https://github.com/AlexanderYastrebov/onion-vanity-address> |
| alexdeathway/torswitch | tool | <https://github.com/alexdeathway/torswitch> |
| alextanhongpin/go-onion | web-platform | <https://github.com/alextanhongpin/go-onion> |
| altport/onionshare-optimized | web-platform | <https://github.com/altport/onionshare-optimized> |
| alx-xlx/download-web-directory | directory | <https://github.com/alx-xlx/download-web-directory> |
| Amitpnk/Onion-architecture-ASP.NET-Core | plugin | <https://github.com/Amitpnk/Onion-architecture-ASP.NET-Core> |
| amnestywebsite/onion-website | web-platform | <https://github.com/amnestywebsite/onion-website> |
| amookia/torflask | container | <https://github.com/amookia/torflask> |
| AnarchoTechNYC/ansible-role-tor | web-platform | <https://github.com/AnarchoTechNYC/ansible-role-tor> |
| aniketchavan2211/Onion-Sites | web-platform | <https://github.com/aniketchavan2211/Onion-Sites> |
| anonymex3/XBrowser-SHIELD-DOWNLOADS | mobile-app | <https://github.com/anonymex3/XBrowser-SHIELD-DOWNLOADS> |
| anonymousvano/uncensored-hidden-wiki | web-platform | <https://github.com/anonymousvano/uncensored-hidden-wiki> |
| Ar1sto/SnakeEye | cli-tool | <https://github.com/Ar1sto/SnakeEye> |
| ARCANGEL0/OnionChat | web-platform | <https://github.com/ARCANGEL0/OnionChat> |
| arhhhhh404/Lain-Requester | tool | <https://github.com/arhhhhh404/Lain-Requester> |
| aseemselim45-afk/synthesia-newest | tool | <https://github.com/aseemselim45-afk/synthesia-newest> |
| astros3x/Astri | tool | <https://github.com/astros3x/Astri> |
| Attacks-on-Tor/Attacks-on-Tor | web-platform | <https://github.com/Attacks-on-Tor/Attacks-on-Tor> |
| bencevans/nightlink | research-project | <https://github.com/bencevans/nightlink> |
| BenJ1337/scrap-steam-market-via-tor-network | tool | <https://github.com/BenJ1337/scrap-steam-market-via-tor-network> |
| benjojo/six-onions | tool | <https://github.com/benjojo/six-onions> |
| beriktassuly/onion-forum | tool | <https://github.com/beriktassuly/onion-forum> |
| berty/go-libp2p-tor-transport | tool | <https://github.com/berty/go-libp2p-tor-transport> |
| BillDietrich/linkcheckerhtml | plugin | <https://github.com/BillDietrich/linkcheckerhtml> |
| BlackRabbitZ/Onion-Projects | web-platform | <https://github.com/BlackRabbitZ/Onion-Projects> |
| BlackRabbitZ/OnionCall | web-platform | <https://github.com/BlackRabbitZ/OnionCall> |
| bonifield/splunk_on_security_onion | tool | <https://github.com/bonifield/splunk_on_security_onion> |
| BryanApolonio/Deep-Index | directory | <https://github.com/BryanApolonio/Deep-Index> |
| bugfest/tor-controller | container | <https://github.com/bugfest/tor-controller> |
| ByteBreach/torhost | web-platform | <https://github.com/ByteBreach/torhost> |
| c14it0n/torgeforge | web-platform | <https://github.com/c14it0n/torgeforge> |
| captain-redbeard/XOR-Onion | tool | <https://github.com/captain-redbeard/XOR-Onion> |
| cathugger/mkp224o | web-platform | <https://github.com/cathugger/mkp224o> |
| chrisch88dev/onionloom | cli-tool | <https://github.com/chrisch88dev/onionloom> |
| chrisdavidmiles/tor-redirect.js | web-platform | <https://github.com/chrisdavidmiles/tor-redirect.js> |
| ciehanski/oniongen-hs | tool | <https://github.com/ciehanski/oniongen-hs> |
| CitkaneArchive/onion-tests | web-platform | <https://github.com/CitkaneArchive/onion-tests> |
| cnjdev/OnionPeeler | tool | <https://github.com/cnjdev/OnionPeeler> |
| Coordinate-Cat/lab-py3-tor-blog | web-platform | <https://github.com/Coordinate-Cat/lab-py3-tor-blog> |
| Coordinate-Cat/t0r-lib | web-platform | <https://github.com/Coordinate-Cat/t0r-lib> |
| cpatn/OnionChat | api-service | <https://github.com/cpatn/OnionChat> |
| crimza/solaris-marketplace | web-platform | <https://github.com/crimza/solaris-marketplace> |
| cy6or9/uuo | dashboard | <https://github.com/cy6or9/uuo> |
| cyberanchor/eMailCompare | web-platform | <https://github.com/cyberanchor/eMailCompare> |
| CyberCoreAccess/onion-website | tool | <https://github.com/CyberCoreAccess/onion-website> |
| cyphar/mkonion | container | <https://github.com/cyphar/mkonion> |
| cypherbits/onionbb | plugin | <https://github.com/cypherbits/onionbb> |
| cyrixhero/blog.code | tool | <https://github.com/cyrixhero/blog.code> |
| Danukeru/torv3_vanity_addr_vulkan | web-platform | <https://github.com/Danukeru/torv3_vanity_addr_vulkan> |
| DanWin/hosting | web-platform | <https://github.com/DanWin/hosting> |
| DanWin/mail-hosting | web-platform | <https://github.com/DanWin/mail-hosting> |
| Darkwebwikito/Darkweb | directory | <https://github.com/Darkwebwikito/Darkweb> |
| david-marin-0xff/david-marin-0xff.github.io | web-platform | <https://github.com/david-marin-0xff/david-marin-0xff.github.io> |
| david-marin-0xff/el-guero-onion | web-platform | <https://github.com/david-marin-0xff/el-guero-onion> |
| dbalan/tor-address | tool | <https://github.com/dbalan/tor-address> |
| Detox/routing | tool | <https://github.com/Detox/routing> |
| dirtyfilthy/freshonions-torscraper | web-platform | <https://github.com/dirtyfilthy/freshonions-torscraper> |
| dlion/guessTor | tool | <https://github.com/dlion/guessTor> |
| Dogmax123/Outlaw | cli-tool | <https://github.com/Dogmax123/Outlaw> |
| dragonfruitnetwork/onionfruit | tool | <https://github.com/dragonfruitnetwork/onionfruit> |
| DuckDuckGo Onion Service | web-platform | <https://duckduckgo.com/onion> |
| EffectiveAF/insta-onion | web-platform | <https://github.com/EffectiveAF/insta-onion> |
| egypcio/criptobaiao | tool | <https://github.com/egypcio/criptobaiao> |
| eightyfive/fetch-run | api-service | <https://github.com/eightyfive/fetch-run> |
| einyx/tor-ingress-controller | container | <https://github.com/einyx/tor-ingress-controller> |
| Eliazar-byte/Union-Imperial | web-platform | <https://github.com/Eliazar-byte/Union-Imperial-> |
| Eltotiz/TorSearch | cli-tool | <https://github.com/Eltotiz/TorSearch> |
| embetrix/meta-tor | web-platform | <https://github.com/embetrix/meta-tor> |
| emon5122/onionforge | container | <https://github.com/emon5122/onionforge> |
| EndGameddos/EndGame-V3 | web-platform | <https://github.com/EndGameddos/EndGame-V3> |
| EpicureanHeron/onionWeatherOLED | api-service | <https://github.com/EpicureanHeron/onionWeatherOLED> |
| Err0r-ICA/TORhunter | web-platform | <https://github.com/Err0r-ICA/TORhunter> |
| erwincas/secureweb_flyshop | web-platform | <https://github.com/erwincas/secureweb_flyshop> |
| eslutz/Torarr | directory | <https://github.com/eslutz/Torarr> |
| ethicaljivitesh/ToRDirectoryEnumerator | directory | <https://github.com/ethicaljivitesh/ToRDirectoryEnumerator> |
| eyeblech/onion-guide | dashboard | <https://github.com/eyeblech/onion-guide> |
| eyedeekay/onramp | web-platform | <https://github.com/eyedeekay/onramp> |
| FamilyOfficeOrg/FamilyOfficeOnionLocation5 | plugin | <https://github.com/FamilyOfficeOrg/FamilyOfficeOnionLocation5> |
| fbnmtz/torctl | container | <https://github.com/fbnmtz/torctl> |
| fenjalal/gateforum | web-platform | <https://github.com/fenjalal/gateforum> |
| filirnd/orpi | cli-tool | <https://github.com/filirnd/orpi> |
| Fonta1n3/FullyNoded | tool | <https://github.com/Fonta1n3/FullyNoded> |
| fphammerle/docker-onion-service | container | <https://github.com/fphammerle/docker-onion-service> |
| fte/ognon-radar | api-service | <https://github.com/fte/ognon-radar> |
| ftTower/Onion | web-platform | <https://github.com/ftTower/Onion> |
| FujiwaraChoki/tor-demo | tool | <https://github.com/FujiwaraChoki/tor-demo> |
| gatodev-cpu/OnionChat | web-platform | <https://github.com/gatodev-cpu/OnionChat> |
| Gauravst/monerod-proxy-tor | tool | <https://github.com/Gauravst/monerod-proxy-tor> |
| GC2211-ghuru/Thirteen | web-platform | <https://github.com/GC2211-ghuru/Thirteen> |
| GermaniU/tor-mcp-proxy | api-service | <https://github.com/GermaniU/tor-mcp-proxy> |
| gh4rib/onion | web-platform | <https://github.com/gh4rib/onion> |
| gh4rib/osint | tool | <https://github.com/gh4rib/osint> |
| ghaziwali/Hulios | web-platform | <https://github.com/ghaziwali/Hulios> |
| glurp/ruby-onion-omega2 | tool | <https://github.com/glurp/ruby-onion-omega2> |
| gonzdn/OnionArquitecture_Redis | web-platform | <https://github.com/gonzdn/OnionArquitecture_Redis> |
| gp2112/snowflake-cli | cli-tool | <https://github.com/gp2112/snowflake-cli> |
| graph90/openclaw-darknet-fetch | tool | <https://github.com/graph90/openclaw-darknet-fetch> |
| grezzled/AutoTor | cli-tool | <https://github.com/grezzled/AutoTor> |
| h0ek/onionscout | web-platform | <https://github.com/h0ek/onionscout> |
| hafizuddinso/Post-Quantum | tool | <https://github.com/hafizuddinso/Post-Quantum> |
| hansalemaos/obackup | tool | <https://github.com/hansalemaos/obackup> |
| hardcod3dd/freshonions-torscraper-reborn | web-platform | <https://github.com/hardcod3dd/freshonions-torscraper-reborn> |
| Haystak | web-platform | <https://haystak.com/> |
| hIMEI29A/gichidan | cli-tool | <https://github.com/hIMEI29A/gichidan> |
| hIMEI29A/gotorsocks | tool | <https://github.com/hIMEI29A/gotorsocks> |
| Hitarashi/dhap | tool | <https://github.com/Hitarashi/dhap> |
| HiveMinds/SSL4Tor | web-platform | <https://github.com/HiveMinds/SSL4Tor> |
| httpscl/tor2webz | web-platform | <https://github.com/httpscl/tor2webz> |
| Hyphonical/Onyun | container | <https://github.com/Hyphonical/Onyun> |
| hypnotract/laravel-onion-architecture | tool | <https://github.com/hypnotract/laravel-onion-architecture> |
| i2z1/ggonion | tool | <https://github.com/i2z1/ggonion> |
| imadeanaccount1/onionbot | tool | <https://github.com/imadeanaccount1/onionbot> |
| imvickykumar999/Termux-Darkweb | tool | <https://github.com/imvickykumar999/Termux-Darkweb> |
| infowebaurix-wq/open-ui-hidden | container | <https://github.com/infowebaurix-wq/open-ui-hidden> |
| ITALICOder/LibertyC2 | cli-tool | <https://github.com/ITALICOder/LibertyC2> |
| itsOwen/i2pd-tails-os | tool | <https://github.com/itsOwen/i2pd-tails-os> |
| jacawaca/the-cake-router | cli-tool | <https://github.com/jacawaca/the-cake-router> |
| jackweiwang/dlibFaceRecognitionHttpServer | tool | <https://github.com/jackweiwang/dlibFaceRecognitionHttpServer> |
| jacopotediosi/Onionscanner | web-platform | <https://github.com/jacopotediosi/Onionscanner> |
| jakbin/django-tor | web-platform | <https://github.com/jakbin/django-tor> |
| jakbin/flask-tor | web-platform | <https://github.com/jakbin/flask-tor> |
| jakbin/tor-proxy | web-platform | <https://github.com/jakbin/tor-proxy> |
| jakejarvis/docker-tor | container | <https://github.com/jakejarvis/docker-tor> |
| jamieweb/jamieweb | tool | <https://github.com/jamieweb/jamieweb> |
| jankammerath/torgate | plugin | <https://github.com/jankammerath/torgate> |
| jeannesbryan/nion | web-platform | <https://github.com/jeannesbryan/nion> |
| JGiraldo29/giralnet | tool | <https://github.com/JGiraldo29/giralnet> |
| jhossuarodriguez/SistemaGestorPacientes | tool | <https://github.com/jhossuarodriguez/SistemaGestorPacientes> |
| johnwalicki/Node-RED-Onion-Omega2-Examples | tool | <https://github.com/johnwalicki/Node-RED-Onion-Omega2-Examples> |
| jonathan-reisdorf/node-onion-omega-oled-text | research-project | <https://github.com/jonathan-reisdorf/node-onion-omega-oled-text> |
| joshuavanderpoll/Onion-V3-Generator | web-platform | <https://github.com/joshuavanderpoll/Onion-V3-Generator> |
| jschmidtnj/torwebsite | tool | <https://github.com/jschmidtnj/torwebsite> |
| JSLess/Chat | tool | <https://github.com/JSLess/Chat> |
| jswan00/Tor-shipt | tool | <https://github.com/jswan00/Tor-shipt> |
| juga0/onbasca | tool | <https://github.com/juga0/onbasca> |
| juga0/onbasca_hax_slides | tool | <https://github.com/juga0/onbasca_hax_slides> |
| Jul10l1r4/getrails | directory | <https://github.com/Jul10l1r4/getrails> |
| k4m4/active-onions | tool | <https://github.com/k4m4/active-onions> |
| k4m4/onion-regex | tool | <https://github.com/k4m4/onion-regex> |
| kawaiipantsu/onionpeel-toolbox | tool | <https://github.com/kawaiipantsu/onionpeel-toolbox> |
| kayraaktas/tor-scraper | api-service | <https://github.com/kayraaktas/tor-scraper> |
| keithhetrick/hidden-coffee | container | <https://github.com/keithhetrick/hidden-coffee> |
| kevinl95/BridgeButtons | tool | <https://github.com/kevinl95/BridgeButtons> |
| KeyWeeUsr/OnionProxy | container | <https://github.com/KeyWeeUsr/OnionProxy> |
| Kibidango086/gopeed-extension-tor | plugin | <https://github.com/Kibidango086/gopeed-extension-tor> |
| kk80586/tradeONION | cli-tool | <https://github.com/kk80586/tradeONION> |
| KM-Mozammel/TaskManagerSolution | api-service | <https://github.com/KM-Mozammel/TaskManagerSolution> |
| kpcyrd/narnia | web-platform | <https://github.com/kpcyrd/narnia> |
| KyleBing/onion-theme-wireframe | tool | <https://github.com/KyleBing/onion-theme-wireframe> |
| lalaio1/Onion-sites | web-platform | <https://github.com/lalaio1/Onion-sites> |
| LashSesh/ophanion | web-platform | <https://github.com/LashSesh/ophanion> |
| LashSesh/thronion | web-platform | <https://github.com/LashSesh/thronion> |
| layogtima/ferment | tool | <https://github.com/layogtima/ferment> |
| lazy-am/zvart | tool | <https://github.com/lazy-am/zvart> |
| libreops/libreonion | tool | <https://github.com/libreops/libreonion> |
| lidarbtc/torshammer | web-platform | <https://github.com/lidarbtc/torshammer> |
| LIDSOL/papime-pe102718-mecanismos-de-privacidad-y-anonimato | api-service | <https://github.com/LIDSOL/papime-pe102718-mecanismos-de-privacidad-y-anonimato> |
| LittleAtariXE/OnionPortal | container | <https://github.com/LittleAtariXE/OnionPortal> |
| LittleAtariXE/OnionsFarmer | tool | <https://github.com/LittleAtariXE/OnionsFarmer> |
| LoomisLoud/onion-crawler | tool | <https://github.com/LoomisLoud/onion-crawler> |
| luannguyenQV/nestjs-hexagon-onion-ddd-boilerplate | tool | <https://github.com/luannguyenQV/nestjs-hexagon-onion-ddd-boilerplate> |
| lucianjames/TorPlusPlus | web-platform | <https://github.com/lucianjames/TorPlusPlus> |
| lucianjames/TorPlusPlusExamples | web-platform | <https://github.com/lucianjames/TorPlusPlusExamples> |
| luebke-dev/chive | web-platform | <https://github.com/luebke-dev/chive> |
| Luisgb98/cybersec-bootcamp | api-service | <https://github.com/Luisgb98/cybersec-bootcamp> |
| lukasbecvar/ghost-talk | web-platform | <https://github.com/lukasbecvar/ghost-talk> |
| lukechilds/onionite | tool | <https://github.com/lukechilds/onionite> |
| lukereichold/swift-multiaddr | library | <https://github.com/lukereichold/swift-multiaddr> |
| lvndry/jazz-plugin-onion | plugin | <https://github.com/lvndry/jazz-plugin-onion> |
| Lz4Lz/tor-proxy-mc | tool | <https://github.com/Lz4Lz/tor-proxy-mc> |
| m2gi-duboise/OnionMQ | tool | <https://github.com/m2gi-duboise/OnionMQ> |
| maceip/trap | tool | <https://github.com/maceip/trap> |
| macipv6/onion-crawler-analyst | dashboard | <https://github.com/macipv6/onion-crawler-analyst> |
| MadLadsTechnology/Onion-Router | api-service | <https://github.com/MadLadsTechnology/Onion-Router> |
| mairecheco/onionroot | web-platform | <https://github.com/mairecheco/onionroot> |
| ManasSoni-2009/OnionGrade | dashboard | <https://github.com/ManasSoni-2009/OnionGrade> |
| MarinX/jsonrpconion | web-platform | <https://github.com/MarinX/jsonrpconion> |
| MarinX/monion | web-platform | <https://github.com/MarinX/monion> |
| MarinX/tor-phishy | plugin | <https://github.com/MarinX/tor-phishy> |
| MatrixTM26/TorDROID | web-platform | <https://github.com/MatrixTM26/TorDROID> |
| maxbeizer/gh-onion | plugin | <https://github.com/maxbeizer/gh-onion> |
| meeDamian/onions | awesome-list | <https://github.com/meeDamian/onions> |
| Melzar/onion-architecture-boilerplate | api-service | <https://github.com/Melzar/onion-architecture-boilerplate> |
| mf-rl/TorFileDownload | tool | <https://github.com/mf-rl/TorFileDownload> |
| MGreif/tor-hidden-service-docker | container | <https://github.com/MGreif/tor-hidden-service-docker> |
| mig5/check-site-up | web-platform | <https://github.com/mig5/check-site-up> |
| MiguelRiazaValverde/hanna | framework | <https://github.com/MiguelRiazaValverde/hanna> |
| milahu/darknet-git-hosting-services | web-platform | <https://github.com/milahu/darknet-git-hosting-services> |
| milenkodj/Onion.Solution | tool | <https://github.com/milenkodj/Onion.Solution> |
| MineFartS/oniongen | research-project | <https://github.com/MineFartS/oniongen> |
| mirsamantajbakhsh/OnionHarvester | tool | <https://github.com/mirsamantajbakhsh/OnionHarvester> |
| mitjafelicijan/not-garlic | research-project | <https://github.com/mitjafelicijan/not-garlic> |
| mkl159/guardianplay-onion | plugin | <https://github.com/mkl159/guardianplay-onion> |
| mkl159/Miyoo-Bifrost | tool | <https://github.com/mkl159/Miyoo-Bifrost-> |
| morian/leek | tool | <https://github.com/morian/leek> |
| mpelaezv/InClub.Compras | web-platform | <https://github.com/mpelaezv/InClub.Compras> |
| mrargun/.net-core-onion-architecture | framework | <https://github.com/mrargun/.net-core-onion-architecture> |
| muerfox/Onion-Brute | container | <https://github.com/muerfox/Onion-Brute> |
| muizo1950/ProjectWeb-ArtoBawang | tool | <https://github.com/muizo1950/ProjectWeb-ArtoBawang> |
| mycodedoesnotcompile2/arti_mirror | tool | <https://github.com/mycodedoesnotcompile2/arti_mirror> |
| nagilum/tordl | cli-tool | <https://github.com/nagilum/tordl> |
| nakasyou/deno_tor | tool | <https://github.com/nakasyou/deno_tor> |
| nametoolong/oregano | research-project | <https://github.com/nametoolong/oregano> |
| nao1215/onionscan | tool | <https://github.com/nao1215/onionscan> |
| nao1215/tornago | web-platform | <https://github.com/nao1215/tornago> |
| nazar-pc/ronion | framework | <https://github.com/nazar-pc/ronion> |
| ncryptsion/multitorx | tool | <https://github.com/ncryptsion/multitorx> |
| nesiler/identity-sample | api-service | <https://github.com/nesiler/identity-sample> |
| Nespartious/RustBalance | web-platform | <https://github.com/Nespartious/RustBalance> |
| NetKnightsClub/OnionEye | api-service | <https://github.com/NetKnightsClub/OnionEye> |
| NexvisionLab/OnionGlass | tool | <https://github.com/NexvisionLab/OnionGlass> |
| nicdercole/webserver-tor-lighttpd | container | <https://github.com/nicdercole/webserver-tor-lighttpd> |
| nicholasadamou/onion-pi | cli-tool | <https://github.com/nicholasadamou/onion-pi> |
| NisooJadhav/snowflake | tool | <https://github.com/NisooJadhav/snowflake> |
| noor633/trcX | cli-tool | <https://github.com/noor633/trcX> |
| NoxCreations/TorPHP | web-platform | <https://github.com/NoxCreations/TorPHP> |
| NoxCreations/torv3py | web-platform | <https://github.com/NoxCreations/torv3py> |
| nukkerman2000/oniondist | web-platform | <https://github.com/nukkerman2000/oniondist> |
| number571/awesome-anonymity | awesome-list | <https://github.com/number571/awesome-anonymity> |
| octagono/skink | web-platform | <https://github.com/octagono/skink> |
| oktupol/rsync-onion | web-platform | <https://github.com/oktupol/rsync-onion> |
| oliverchen415/onion_ml | tool | <https://github.com/oliverchen415/onion_ml> |
| Onion-Search-Engine/Mozilla-Add-ons | plugin | <https://github.com/Onion-Search-Engine/Mozilla-Add-ons> |
| Onion-Search-Engine/Onion-Search-Engine | dashboard | <https://github.com/Onion-Search-Engine/Onion-Search-Engine> |
| onion-wiki/onionwiki | tool | <https://github.com/onion-wiki/onionwiki> |
| OnionBrowser/OnionBrowser | tool | <https://github.com/OnionBrowser/OnionBrowser> |
| OnionDotLive/onionliveplugin | browser-extension | <https://github.com/OnionDotLive/onionliveplugin> |
| OnionIoT/OOS-App-RFID | tool | <https://github.com/OnionIoT/OOS-App-RFID> |
| OnionLand | web-platform | <https://onionland.io> |
| onionltd/EndGame | web-platform | <https://github.com/onionltd/EndGame> |
| onionltd/go-omg | dashboard | <https://github.com/onionltd/go-omg> |
| OnionSearcher/.OnionSearcher | tool | <https://github.com/OnionSearcher/.OnionSearcher> |
| OnionSearcher/.PrettyOnionNameFinder | web-platform | <https://github.com/OnionSearcher/.PrettyOnionNameFinder> |
| oniontester/OnionStrike | framework | <https://github.com/oniontester/OnionStrike> |
| OnionTM/OnionAdmin | tool | <https://github.com/OnionTM/OnionAdmin> |
| OnionTM/OnionDDoS | tool | <https://github.com/OnionTM/OnionDDoS> |
| OnionTM/OnionTCP | tool | <https://github.com/OnionTM/OnionTCP> |
| oniontree-org/oniontree-omg-tools | dashboard | <https://github.com/oniontree-org/oniontree-omg-tools> |
| Onionwikibest/Onionwiki | tool | <https://github.com/Onionwikibest/Onionwiki> |
| Onionwkitor/Onionwiki | tool | <https://github.com/Onionwkitor/Onionwiki> |
| OzelTam/onion-crawler | research-project | <https://github.com/OzelTam/onion-crawler> |
| OzelTam/OnionCrawler | dashboard | <https://github.com/OzelTam/OnionCrawler> |
| pablo-chacon/camo | tool | <https://github.com/pablo-chacon/camo> |
| PartTimeLegend/torless | research-project | <https://github.com/PartTimeLegend/torless> |
| peeboy7/KinanJeff-Directory | directory | <https://github.com/peeboy7/KinanJeff-Directory> |
| PeterDaveHello/tor-socks-proxy | container | <https://github.com/PeterDaveHello/tor-socks-proxy> |
| phillid/sand-leek | research-project | <https://github.com/phillid/sand-leek> |
| phoityne/pty-mcp-server | cli-tool | <https://github.com/phoityne/pty-mcp-server> |
| PietroJomini/zeniba | api-service | <https://github.com/PietroJomini/zeniba> |
| placDev/mappers | library | <https://github.com/placDev/mappers> |
| placDev/mappers-nest | library | <https://github.com/placDev/mappers-nest> |
| plan44/p44sbbd | plugin | <https://github.com/plan44/p44sbbd> |
| ppad-tech/bolt4 | tool | <https://github.com/ppad-tech/bolt4> |
| Praexor/mainnet-neutrino-onion-lnd | tool | <https://github.com/Praexor/mainnet-neutrino-onion-lnd> |
| pred2k/onion-sites | tool | <https://github.com/pred2k/onion-sites> |
| PrivAtlas/Jet-USDJJ | research-project | <https://github.com/PrivAtlas/Jet-USDJJ> |
| proximacentav-pp/onionmail-reborn | container | <https://github.com/proximacentav-pp/onionmail-reborn> |
| pvaviloff/php-guidelines-example | dashboard | <https://github.com/pvaviloff/php-guidelines-example> |
| qbitroot/rsa2onion | web-platform | <https://github.com/qbitroot/rsa2onion> |
| qbitseclabs/getrails-tool | directory | <https://github.com/qbitseclabs/getrails-tool> |
| r2ality/torify | dashboard | <https://github.com/r2ality/torify> |
| rdkr/oniongen-go | tool | <https://github.com/rdkr/oniongen-go> |
| revery-project/revery | tool | <https://github.com/revery-project/revery> |
| reyzzzl/Hyperion-CLI | cli-tool | <https://github.com/reyzzzl/Hyperion-CLI> |
| ricsirigu/streamerd | tool | <https://github.com/ricsirigu/streamerd> |
| RiotKit/ansible-role-vanguards | tool | <https://github.com/RiotKit/ansible-role-vanguards> |
| riteshekbote/oniontui | web-platform | <https://github.com/riteshekbote/oniontui> |
| rizl123/onionmint | web-platform | <https://github.com/rizl123/onionmint> |
| rommapp/grout | cli-tool | <https://github.com/rommapp/grout> |
| RootDev4/Tor-Request | plugin | <https://github.com/RootDev4/Tor-Request> |
| RuiSiang/chatNT | tool | <https://github.com/RuiSiang/chatNT> |
| SafwanLjd/torquests | api-service | <https://github.com/SafwanLjd/torquests> |
| salif/lemmy-onion-service | web-platform | <https://github.com/salif/lemmy-onion-service> |
| SalvadorPalmaRodriguez/enola-cli-lite | container | <https://github.com/SalvadorPalmaRodriguez/enola-cli-lite> |
| sambacha/tor-server | web-platform | <https://github.com/sambacha/tor-server> |
| samuelmanzanera/clean-node-api | api-service | <https://github.com/samuelmanzanera/clean-node-api> |
| saper-2/oo-kmod-ds2413-2100h | plugin | <https://github.com/saper-2/oo-kmod-ds2413-2100h> |
| SarahRoseLives/OniVex | tool | <https://github.com/SarahRoseLives/OniVex> |
| sarun2003/Onion-Router-Path-Visualization | dashboard | <https://github.com/sarun2003/Onion-Router-Path-Visualization> |
| satwikkansal/tor-hidden-service-python | web-platform | <https://github.com/satwikkansal/tor-hidden-service-python> |
| scresh/Digamma | tool | <https://github.com/scresh/Digamma> |
| seanpm2001/Bliss_Browser_Onion | tool | <https://github.com/seanpm2001/Bliss_Browser_Onion> |
| searchformyusername/Dark-Net-Websites-Dataset | dataset | <https://github.com/searchformyusername/Dark-Net-Websites-Dataset> |
| SergeyBitpix/TheOnionRouter_master | tool | <https://github.com/SergeyBitpix/TheOnionRouter_master> |
| sginne/Allium | tool | <https://github.com/sginne/Allium> |
| sh4den/Discord-Tor | tool | <https://github.com/sh4den/Discord-Tor> |
| shesek/onionfile | web-platform | <https://github.com/shesek/onionfile> |
| ShookLyngs/chain | plugin | <https://github.com/ShookLyngs/chain> |
| shyboytm/gamepal-dark-onion-os | tool | <https://github.com/shyboytm/gamepal-dark-onion-os> |
| Silur/riffled | tool | <https://github.com/Silur/riffled> |
| sl251/zlibrary-tor | api-service | <https://github.com/sl251/zlibrary-tor> |
| smolcars/react-native-nitro-tor | plugin | <https://github.com/smolcars/react-native-nitro-tor> |
| sn0b4ll/aria2-onion-downloader | tool | <https://github.com/sn0b4ll/aria2-onion-downloader> |
| stefanpejcic/onion-location | tool | <https://github.com/stefanpejcic/onion-location> |
| successor1/projectsato | tool | <https://github.com/successor1/projectsato> |
| suprstarrd/PlusOnion | web-platform | <https://github.com/suprstarrd/PlusOnion> |
| SWORDIntel/c2-enum-toolkit | framework | <https://github.com/SWORDIntel/c2-enum-toolkit> |
| systemkeyy/eon | web-platform | <https://github.com/systemkeyy/eon> |
| systemli/ansible-role-onion | web-platform | <https://github.com/systemli/ansible-role-onion> |
| t-bast/echalotte | research-project | <https://github.com/t-bast/echalotte> |
| t-bast/go-libp2p-echalotte | tool | <https://github.com/t-bast/go-libp2p-echalotte> |
| tasooshi/torboost | tool | <https://github.com/tasooshi/torboost> |
| tc4dy/support-tor-for-freedom | web-platform | <https://github.com/tc4dy/support-tor-for-freedom> |
| tdex-network/tor-proxy | cli-tool | <https://github.com/tdex-network/tor-proxy> |
| teal33t/torget.py | web-platform | <https://github.com/teal33t/torget.py> |
| tgbv/onion-tools | web-platform | <https://github.com/tgbv/onion-tools> |
| thecountrox/tor-share | desktop-app | <https://github.com/thecountrox/tor-share> |
| theonion/onionbot | plugin | <https://github.com/theonion/onionbot> |
| TheOnionBay/TORrents | tool | <https://github.com/TheOnionBay/TORrents> |
| TheTorGuy/Tornado | web-platform | <https://github.com/TheTorGuy/Tornado> |
| THSamurai/TorKill | tool | <https://github.com/THSamurai/TorKill> |
| tillit-cc/tillit | web-platform | <https://github.com/tillit-cc/tillit> |
| tn3w/torflake | tool | <https://github.com/tn3w/torflake> |
| tn3w/TorRunner | web-platform | <https://github.com/tn3w/TorRunner> |
| tomrsae/ronion | library | <https://github.com/tomrsae/ronion> |
| Tor66 | directory | <https://socradar.io/blog/top-10-dark-web-search-engines-in-2025/> |
| TorMap/tormap | web-platform | <https://github.com/TorMap/tormap> |
| torservers/onionize-docker | container | <https://github.com/torservers/onionize-docker> |
| Torwikito/torwiki | tool | <https://github.com/Torwikito/torwiki> |
| TR2NLG/onion-color-balance | tool | <https://github.com/TR2NLG/onion-color-balance> |
| trimstray/multitor | tool | <https://github.com/trimstray/multitor> |
| tum-taskforce/allium | library | <https://github.com/tum-taskforce/allium> |
| uknowuserqq/Zen-OSINT---MULTI-TOOL | dataset | <https://github.com/uknowuserqq/Zen-OSINT---MULTI-TOOL-> |
| unkaktus/onionutil | tool | <https://github.com/unkaktus/onionutil> |
| unkaktus/torsh | cli-tool | <https://github.com/unkaktus/torsh> |
| update692/torping | cli-tool | <https://github.com/update692/torping> |
| VaimpierOfficial/Onion-Engine | tool | <https://github.com/VaimpierOfficial/Onion-Engine> |
| veilcall/tor | web-platform | <https://github.com/veilcall/tor> |
| vergecurrency/vDroid | research-project | <https://github.com/vergecurrency/vDroid> |
| VolkanSah/playing-with-scapy-and-stem | tool | <https://github.com/VolkanSah/playing-with-scapy-and-stem> |
| VolkanSah/SherlocksHome | web-platform | <https://github.com/VolkanSah/SherlocksHome> |
| wait-what/torcaddy | container | <https://github.com/wait-what/torcaddy> |
| warlock/multitor | research-project | <https://github.com/warlock/multitor> |
| WaterSeer/UniversityProject | web-platform | <https://github.com/WaterSeer/UniversityProject> |
| WesleyJw/modern-data-stack | container | <https://github.com/WesleyJw/modern-data-stack> |
| wesmar/OnionDownloader | api-service | <https://github.com/wesmar/OnionDownloader> |
| whispering3/marketplace-platform | web-platform | <https://github.com/whispering3/marketplace-platform> |
| wille/relayawards | research-project | <https://github.com/wille/relayawards> |
| willmeyers/onionsweep | tool | <https://github.com/willmeyers/onionsweep> |
| wybiral/torgo | web-platform | <https://github.com/wybiral/torgo> |
| xxczaki/onion-omega2-coronavirus-oled | plugin | <https://github.com/xxczaki/onion-omega2-coronavirus-oled> |
| Yanik39/TORNet | container | <https://github.com/Yanik39/TORNet> |
| yasserbdj96/hiphp | container | <https://github.com/yasserbdj96/hiphp> |
| Yearning9/onion-bot | tool | <https://github.com/Yearning9/onion-bot> |
| YegorMedvedev/python-onion-scaffold | tool | <https://github.com/YegorMedvedev/python-onion-scaffold> |
| yqbrad/CleanArchitectureTemplate | tool | <https://github.com/yqbrad/CleanArchitectureTemplate> |
| yubo9807/onion_node | tool | <https://github.com/yubo9807/onion_node> |
| yuvaldd9/odidion | web-platform | <https://github.com/yuvaldd9/odidion> |
| z23c/z23 | tool | <https://github.com/z23c/z23> |
| Zaczero/Tor4NET | library | <https://github.com/Zaczero/Tor4NET> |
| zarkones/OnionC2 | tool | <https://github.com/zarkones/OnionC2> |
| zer-far/onion-nest | container | <https://github.com/zer-far/onion-nest> |
| zgruza/Daniel-Winzen-Onion-Link-List-Scraper | tool | <https://github.com/zgruza/Daniel-Winzen-Onion-Link-List-Scraper> |
| zgruza/Daniel_Winzen_Onion_Link_List_API | directory | <https://github.com/zgruza/Daniel_Winzen_Onion_Link_List_API> |
| zhaogongchengsi/onion | tool | <https://github.com/zhaogongchengsi/onion> |
| zhaopei0418/onion-http | tool | <https://github.com/zhaopei0418/onion-http> |
| ZishanAdThandar/HackerProxyPro | plugin | <https://github.com/ZishanAdThandar/HackerProxyPro> |

### Phishing & Fraud Intelligence

| Name | Type | URL |
|---|---|---|
| 0n1cOn3/FluxER | tool | <https://github.com/0n1cOn3/FluxER> |
| 0u44/Termux-Hotspot | web-platform | <https://github.com/0u44/Termux-Hotspot> |
| 0x204/ClickFix-Turnstile | cli-tool | <https://github.com/0x204/ClickFix-Turnstile> |
| 0xbitx/DEDSEC_STARSYNC | tool | <https://github.com/0xbitx/DEDSEC_STARSYNC> |
| 0xbitx/DEDSEC_TIKTOKVB | tool | <https://github.com/0xbitx/DEDSEC_TIKTOKVB> |
| 2002hackerr/zphishing | tool | <https://github.com/2002hackerr/zphishing> |
| 4w4k3/Umbrella | tool | <https://github.com/4w4k3/Umbrella> |
| aalex954/evilginx2-TTPs | framework | <https://github.com/aalex954/evilginx2-TTPs> |
| AbdullahZafs/URLSp00f | tool | <https://github.com/AbdullahZafs/URLSp00f> |
| Abhijeetbyte/Insta-login | tool | <https://github.com/Abhijeetbyte/Insta-login> |
| Abhinandan-Khurana/PhishSleuth | plugin | <https://github.com/Abhinandan-Khurana/PhishSleuth> |
| abhisheksaxena1998/Malicious-Urlv5 | browser-extension | <https://github.com/abhisheksaxena1998/Malicious-Urlv5> |
| AbirHasan2005/ShellPhish | cli-tool | <https://github.com/AbirHasan2005/ShellPhish> |
| adamff-dev/ESP8266-Captive-Portal | web-platform | <https://github.com/adamff-dev/ESP8266-Captive-Portal> |
| AdarshVajpayee19/Phishing | tool | <https://github.com/AdarshVajpayee19/Phishing> |
| AdityaBhatt3010/npm-Supply-Chain-Attack-IoCs-Detection-Remediation | tool | <https://github.com/AdityaBhatt3010/npm-Supply-Chain-Attack-IoCs-Detection-Remediation> |
| AdrMXR/KitHack | mobile-app | <https://github.com/AdrMXR/KitHack> |
| AdroitAdorKhan/antipopads-re | research-project | <https://github.com/AdroitAdorKhan/antipopads-re> |
| ag-michael/EmailScanner | directory | <https://github.com/ag-michael/EmailScanner> |
| ahmedbahroun06/PhishLens | container | <https://github.com/ahmedbahroun06/PhishLens> |
| akacdev/SinkingYachts | api-service | <https://github.com/akacdev/SinkingYachts> |
| akacdev/Urlscan | api-service | <https://github.com/akacdev/Urlscan> |
| Akshay-Arjun/69phisher | awesome-list | <https://github.com/Akshay-Arjun/69phisher> |
| AkutoSai/PyReconExSploit-Framework | framework | <https://github.com/AkutoSai/PyReconExSploit-Framework> |
| Alcatraz2033/homodeus | tool | <https://github.com/Alcatraz2033/homodeus> |
| alexbieber/SocioPhish | tool | <https://github.com/alexbieber/SocioPhish> |
| Alpha-1729/ESP_WiFi_Captive_Portal | web-platform | <https://github.com/Alpha-1729/ESP_WiFi_Captive_Portal> |
| AlteredSecurity/365-Stealer | tool | <https://github.com/AlteredSecurity/365-Stealer> |
| Altify-Developing/Altify-Developing-Main | cli-tool | <https://github.com/Altify-Developing/Altify-Developing-Main> |
| AmadeusITGroup/CrawlerBox | framework | <https://github.com/AmadeusITGroup/CrawlerBox> |
| ammnt/DeadEnd | tool | <https://github.com/ammnt/DeadEnd> |
| andpalmier/makephish | tool | <https://github.com/andpalmier/makephish> |
| andpalmier/phishflood | tool | <https://github.com/andpalmier/phishflood> |
| Angry-Pineapple3121/Malware-Research | research-project | <https://github.com/Angry-Pineapple3121/Malware-Research> |
| AntiScam-Squad/pi-hole | tool | <https://github.com/AntiScam-Squad/pi-hole> |
| aravindvnair99/Phishing | desktop-app | <https://github.com/aravindvnair99/Phishing> |
| Arcanum-Sec/wraith | framework | <https://github.com/Arcanum-Sec/wraith> |
| ArchismanKarmakar/Facebook-Phishing-page-php | tool | <https://github.com/ArchismanKarmakar/Facebook-Phishing-page-php> |
| aress31/vulcan | cli-tool | <https://github.com/aress31/vulcan> |
| ariashirazi/InstaBrowser | tool | <https://github.com/ariashirazi/InstaBrowser> |
| arjunindia/fb-phisher-python | tool | <https://github.com/arjunindia/fb-phisher-python> |
| ArunHax/AH-Phisher | cli-tool | <https://github.com/ArunHax/AH-Phisher> |
| atexio/mercure | research-project | <https://github.com/atexio/mercure> |
| athrvadeshmukh/Instagram-and-Facebook-login-page | tool | <https://github.com/athrvadeshmukh/Instagram-and-Facebook-login-page> |
| atulya2109/facebook-phishing | tool | <https://github.com/atulya2109/facebook-phishing> |
| avechuch0/telegram-bigbang | tool | <https://github.com/avechuch0/telegram-bigbang> |
| Avenge-hacker/Avenge | tool | <https://github.com/Avenge-hacker/Avenge> |
| Avenge-hacker/Tool-Avenge | tool | <https://github.com/Avenge-hacker/Tool-Avenge> |
| BadSamuraiDev/bs-lists | tool | <https://github.com/BadSamuraiDev/bs-lists> |
| Bert-JanP/Domain-Response | tool | <https://github.com/Bert-JanP/Domain-Response> |
| Bhaviktutorials/shark | tool | <https://github.com/Bhaviktutorials/shark> |
| bhikandeshmukh/AdvPhishing | tool | <https://github.com/bhikandeshmukh/AdvPhishing> |
| bhikandeshmukh/Blackeye-v2.0 | tool | <https://github.com/bhikandeshmukh/Blackeye-v2.0> |
| bhikandeshmukh/shark | tool | <https://github.com/bhikandeshmukh/shark> |
| bhikandeshmukh/Shark-Lite | tool | <https://github.com/bhikandeshmukh/Shark-Lite> |
| BinRecon-Corp/blackeye | tool | <https://github.com/BinRecon-Corp/blackeye> |
| birdbee44/Resources | tool | <https://github.com/birdbee44/Resources> |
| Bitwise-01/ApeX | tool | <https://github.com/Bitwise-01/ApeX> |
| Bitwise-01/Spectre | tool | <https://github.com/Bitwise-01/Spectre> |
| BiZken/PhishMailer | tool | <https://github.com/BiZken/PhishMailer> |
| blark/cli-phisher | cli-tool | <https://github.com/blark/cli-phisher> |
| blwhit/ClickFix-FakeCaptcha-Cloudflare | cli-tool | <https://github.com/blwhit/ClickFix-FakeCaptcha-Cloudflare> |
| bolster-inc/neo | api-service | <https://github.com/bolster-inc/neo> |
| bradleyjkemp/abwhose | tool | <https://github.com/bradleyjkemp/abwhose> |
| bradleyjkemp/submit-safebrowsing | api-service | <https://github.com/bradleyjkemp/submit-safebrowsing> |
| Bricktech2000/WebInfo | research-project | <https://github.com/Bricktech2000/WebInfo> |
| brijrajparmar27/Instaphish | tool | <https://github.com/brijrajparmar27/Instaphish> |
| bufgix/hookup | research-project | <https://github.com/bufgix/hookup> |
| calinux-py/WhoDAT | api-service | <https://github.com/calinux-py/WhoDAT> |
| CanIPhish/CanIBeSpoofed | tool | <https://github.com/CanIPhish/CanIBeSpoofed> |
| CanIPhish/Phishious | framework | <https://github.com/CanIPhish/Phishious> |
| cenk/malware-domains | tool | <https://github.com/cenk/malware-domains> |
| cenk/nrd | dataset | <https://github.com/cenk/nrd> |
| chenjj/espoofer | tool | <https://github.com/chenjj/espoofer> |
| Chocolate4U/Iran-clash-rules | tool | <https://github.com/Chocolate4U/Iran-clash-rules> |
| Chocolate4U/Iran-sing-box-rules | cli-tool | <https://github.com/Chocolate4U/Iran-sing-box-rules> |
| Chocolate4U/Iran-v2ray-rules | cli-tool | <https://github.com/Chocolate4U/Iran-v2ray-rules> |
| cipheras/cipherginx | tool | <https://github.com/cipheras/cipherginx> |
| cloudsecnetwork/phishintel | tool | <https://github.com/cloudsecnetwork/phishintel> |
| CodingRanjith/autophisher | framework | <https://github.com/CodingRanjith/autophisher> |
| COSSAS/bigphish | tool | <https://github.com/COSSAS/bigphish> |
| crazywifi/SMTP_Relay_Phisher | tool | <https://github.com/crazywifi/SMTP_Relay_Phisher> |
| CrimsonForge-io/king-phisher | framework | <https://github.com/CrimsonForge-io/king-phisher> |
| CryptoScamDB/api.cryptoscamdb.org | api-service | <https://github.com/CryptoScamDB/api.cryptoscamdb.org> |
| CryptoScamDB/blacklist | dataset | <https://github.com/CryptoScamDB/blacklist> |
| CryptoScamDB/legacy.cryptoscamdb.org | dataset | <https://github.com/CryptoScamDB/legacy.cryptoscamdb.org> |
| curtbraz/PhishAPI | api-service | <https://github.com/curtbraz/PhishAPI> |
| Cyber-Anonymous/Dark-Phish | framework | <https://github.com/Cyber-Anonymous/Dark-Phish> |
| cyberboyplas/ipcollector | cli-tool | <https://github.com/cyberboyplas/ipcollector> |
| cyberboyplas/WhPhisher | cli-tool | <https://github.com/cyberboyplas/WhPhisher> |
| cybersertex/WindowsPhishingPayloads-CreatorTools | tool | <https://github.com/cybersertex/WindowsPhishingPayloads-CreatorTools> |
| D00Movenok/BounceBack | tool | <https://github.com/D00Movenok/BounceBack> |
| D00Movenok/HTMLSmuggler | tool | <https://github.com/D00Movenok/HTMLSmuggler> |
| d3c0d3er/Blackeye-incl-ngrok | tool | <https://github.com/d3c0d3er/Blackeye-incl-ngrok> |
| d4rk5id3r/StealthLink | dashboard | <https://github.com/d4rk5id3r/StealthLink> |
| D4Vinci/Dr0p1t-Framework | framework | <https://github.com/D4Vinci/Dr0p1t-Framework> |
| danieloz147/ios-clickfix-templates | cli-tool | <https://github.com/danieloz147/ios-clickfix-templates> |
| dappoo/ShellPhiser | cli-tool | <https://github.com/dappoo/ShellPhiser> |
| DarkAnHell/FastPhish | framework | <https://github.com/DarkAnHell/FastPhish> |
| darkarp/chromepass | tool | <https://github.com/darkarp/chromepass> |
| david3107/squatm3 | tool | <https://github.com/david3107/squatm3> |
| david3107/squatm3gator | research-project | <https://github.com/david3107/squatm3gator> |
| decidedlygray/mfa_slipstream_poc | research-project | <https://github.com/decidedlygray/mfa_slipstream_poc> |
| deepeshdm/Phishing-Attack-Domain-Detection | tool | <https://github.com/deepeshdm/Phishing-Attack-Domain-Detection> |
| Defence-Hackers/ADVFB | tool | <https://github.com/Defence-Hackers/ADVFB> |
| deFr0ggy/NightOwl | tool | <https://github.com/deFr0ggy/NightOwl> |
| denniskniep/DeviceCodePhishing | tool | <https://github.com/denniskniep/DeviceCodePhishing> |
| denniskniep/fido-cross-device-phishing | tool | <https://github.com/denniskniep/fido-cross-device-phishing> |
| DFIR Platform | web-platform | <https://platform.dfir-lab.ch> |
| diogo-fernan/domfind | tool | <https://github.com/diogo-fernan/domfind> |
| Discord-AntiScam/scam-links | dataset | <https://github.com/Discord-AntiScam/scam-links> |
| dmdhrumilmistry/GooglePhish | container | <https://github.com/dmdhrumilmistry/GooglePhish> |
| dnstwister/dnstwister | web-platform | <https://github.com/dnstwister/dnstwister> |
| dr1nk0rdi3/phishreport | tool | <https://github.com/dr1nk0rdi3/phishreport> |
| DRACULA-HACK/C-hacks | tool | <https://github.com/DRACULA-HACK/C-hacks> |
| drcrypterdotru/clickfix-builder | dashboard | <https://github.com/drcrypterdotru/clickfix-builder> |
| dsnezhkov/deepsea | tool | <https://github.com/dsnezhkov/deepsea> |
| DuckySoLucky/discord-phishing-links | tool | <https://github.com/DuckySoLucky/discord-phishing-links> |
| duo-labs/isthislegit | dashboard | <https://github.com/duo-labs/isthislegit> |
| duo-labs/phish-collect | tool | <https://github.com/duo-labs/phish-collect> |
| duocircle/Office365-Setup-DKIM-DMARC-SPF | dashboard | <https://github.com/duocircle/Office365-Setup-DKIM-DMARC-SPF> |
| Ealenn/AdGuard-Home-List | tool | <https://github.com/Ealenn/AdGuard-Home-List> |
| ecstatic-nobel/Not-Anti-Virus | tool | <https://github.com/ecstatic-nobel/Not-Anti-Virus> |
| eded333/TheFuckingList | tool | <https://github.com/eded333/TheFuckingList> |
| edgarluck/Face-Phish | tool | <https://github.com/edgarluck/Face-Phish> |
| edoardottt/defango | plugin | <https://github.com/edoardottt/defango> |
| ElliotAlderson51/Fsociety-Phishing-Tool | tool | <https://github.com/ElliotAlderson51/Fsociety-Phishing-Tool> |
| elliotwutingfeng/GlobalAntiScamOrg-blocklist | tool | <https://github.com/elliotwutingfeng/GlobalAntiScamOrg-blocklist> |
| EmadYaY/PhishiUrl | tool | <https://github.com/EmadYaY/PhishiUrl> |
| EricksonAtHome/blackeye | tool | <https://github.com/EricksonAtHome/blackeye> |
| Err0r-ICA/Phishbait | tool | <https://github.com/Err0r-ICA/Phishbait> |
| ESDAUNG/PhishDataset | dataset | <https://github.com/ESDAUNG/PhishDataset> |
| Esox-Lucius/PiHoleblocklists | tool | <https://github.com/Esox-Lucius/PiHoleblocklists> |
| EstAlvB/Phishing-Detection-with-BERT | tool | <https://github.com/EstAlvB/Phishing-Detection-with-BERT> |
| EwyBoy/Counter-Phishing-Tool | web-platform | <https://github.com/EwyBoy/Counter-Phishing-Tool> |
| f4T1H21/Wi-Phi | web-platform | <https://github.com/f4T1H21/Wi-Phi> |
| fairnightzz/Discord-Login-Phishing | dataset | <https://github.com/fairnightzz/Discord-Login-Phishing> |
| faizann24/phishytics-machine-learning-for-phishing | tool | <https://github.com/faizann24/phishytics-machine-learning-for-phishing> |
| FiltersHeroes/KAD | tool | <https://github.com/FiltersHeroes/KAD> |
| FiltersHeroes/KADhosts | tool | <https://github.com/FiltersHeroes/KADhosts> |
| Flangvik/Bobber | dataset | <https://github.com/Flangvik/Bobber> |
| FLOCK4H/Cappy | web-platform | <https://github.com/FLOCK4H/Cappy> |
| flurdy/bad_usernames | web-platform | <https://github.com/flurdy/bad_usernames> |
| fluxxset/Evilpunch | framework | <https://github.com/fluxxset/Evilpunch> |
| Foo-Manroot/FvS | web-platform | <https://github.com/Foo-Manroot/FvS> |
| forta-network/labelled-datasets | dataset | <https://github.com/forta-network/labelled-datasets> |
| frangelbarrera/Awesome-Hacking-with-AI | awesome-list | <https://github.com/frangelbarrera/Awesome-Hacking-with-AI> |
| FreeZeroDays/GoPhish-Templates | tool | <https://github.com/FreeZeroDays/GoPhish-Templates> |
| frknaykc/Awesome-Malicious-Infra-Hunting-Queries | awesome-list | <https://github.com/frknaykc/Awesome-Malicious-Infra-Hunting-Queries> |
| Ganatra-Ruchir/zphisher | container | <https://github.com/Ganatra-Ruchir/zphisher> |
| Garrettiscool101/zphisher | framework | <https://github.com/Garrettiscool101/zphisher> |
| GeorgePatsias/AskCreds-CS | tool | <https://github.com/GeorgePatsias/AskCreds-CS> |
| getgophish.com | web-platform | <https://getgophish.com/> |
| Getshell/Phishing | cli-tool | <https://github.com/Getshell/Phishing> |
| github.com/rsmusllp/king-phisher | framework | <https://github.com/rsmusllp/king-phisher> |
| GL1T0H/End-To-End-SOC-Home-Lab | tool | <https://github.com/GL1T0H/End-To-End-SOC-Home-Lab> |
| gophish/gophish | framework | <https://github.com/gophish/gophish> |
| GoSecure/gophish-cli | cli-tool | <https://github.com/GoSecure/gophish-cli> |
| GregaVrbancic/Phishing-Dataset | web-platform | <https://github.com/GregaVrbancic/Phishing-Dataset> |
| GSRHaX/NGL-Phish | research-project | <https://github.com/GSRHaX/NGL-Phish> |
| hacefresko/EvilPortal | web-platform | <https://github.com/hacefresko/EvilPortal> |
| hackerxphantom/HACK-CAMERA | tool | <https://github.com/hackerxphantom/HACK-CAMERA> |
| hackerxphantom/XPHISHER | tool | <https://github.com/hackerxphantom/XPHISHER> |
| HackingLZ/ip-obfuscation | research-project | <https://github.com/HackingLZ/ip-obfuscation> |
| HackUnderway/URLHunter | api-service | <https://github.com/HackUnderway/URLHunter> |
| HackWeiser360/MaxPhisher | tool | <https://github.com/HackWeiser360/MaxPhisher> |
| hagezi/dns-blocklists | dataset | <https://github.com/hagezi/dns-blocklists> |
| hagezi/dns-servers | tool | <https://github.com/hagezi/dns-servers> |
| haleemyousef/FacebookPhisher | directory | <https://github.com/haleemyousef/FacebookPhisher> |
| harsxv/awesome-malware | awesome-list | <https://github.com/harsxv/awesome-malware> |
| hasanfirnas/symbiote | tool | <https://github.com/hasanfirnas/symbiote> |
| HaxL0p4/L0p4-Toolkit | framework | <https://github.com/HaxL0p4/L0p4-Toolkit> |
| hazcod/dnstwist | tool | <https://github.com/hazcod/dnstwist> |
| helidem/CVE-2025-24054_CVE-2025-24071-PoC | library | <https://github.com/helidem/CVE-2025-24054_CVE-2025-24071-PoC> |
| HiDe-Techno-Tips/Blackeye-for-Windows | cli-tool | <https://github.com/HiDe-Techno-Tips/Blackeye-for-Windows> |
| hoangminh5210119/deauther | dashboard | <https://github.com/hoangminh5210119/deauther> |
| HorusTeknoloji/TR-PhishingList | research-project | <https://github.com/HorusTeknoloji/TR-PhishingList> |
| hossein-mohseni/ngrok_mask | tool | <https://github.com/hossein-mohseni/ngrok_mask> |
| htr-tech/nexphisher | cli-tool | <https://github.com/htr-tech/nexphisher> |
| htr-tech/zphisher | framework | <https://github.com/htr-tech/zphisher> |
| hxrofo/hotspotphisher | research-project | <https://github.com/hxrofo/hotspotphisher> |
| IAmBlackHacker/Facebook-phishing | framework | <https://github.com/IAmBlackHacker/Facebook-phishing> |
| Iankulani/resistance_bot | web-platform | <https://github.com/Iankulani/resistance_bot> |
| idfp/lnk-builder | tool | <https://github.com/idfp/lnk-builder> |
| idfp/masquerade | tool | <https://github.com/idfp/masquerade> |
| Ignitetch/AdvPhishing | tool | <https://github.com/Ignitetch/AdvPhishing> |
| ineesdv/Tangled | web-platform | <https://github.com/ineesdv/Tangled> |
| iocium/download.dangerous.domains | tool | <https://github.com/iocium/download.dangerous.domains> |
| ItsMeAbhishekRai/xerxes | tool | <https://github.com/ItsMeAbhishekRai/xerxes> |
| itsmehacker/AllPhish | tool | <https://github.com/itsmehacker/AllPhish> |
| Itsmmdoha/d0ppelganger | tool | <https://github.com/Itsmmdoha/d0ppelganger> |
| jackaduma/HomoglyphAttacksDetector | tool | <https://github.com/jackaduma/HomoglyphAttacksDetector> |
| jackmichalak/phishim | tool | <https://github.com/jackmichalak/phishim> |
| jarelllama/Scam-Blocklist | api-service | <https://github.com/jarelllama/Scam-Blocklist> |
| jaykali/maskphish | tool | <https://github.com/jaykali/maskphish> |
| jaykali/shellphish | cli-tool | <https://github.com/jaykali/shellphish> |
| JoasASantos/ShadowPhish | framework | <https://github.com/JoasASantos/ShadowPhish> |
| JoelGMSec/EvilnoVNC | container | <https://github.com/JoelGMSec/EvilnoVNC> |
| johnvexcoder/Hacker-Hook | tool | <https://github.com/johnvexcoder/Hacker-Hook> |
| kanugurajesh/Cookie-Webpage | tool | <https://github.com/kanugurajesh/Cookie-Webpage> |
| kawaiipantsu/spamassassin-rules | tool | <https://github.com/kawaiipantsu/spamassassin-rules> |
| kdhacker1995/Social-Fish-v2.0 | tool | <https://github.com/kdhacker1995/Social-Fish-v2.0> |
| keanu19970228/facebook_login_page | tool | <https://github.com/keanu19970228/facebook_login_page> |
| keanu19970228/paypal_fake_pages | tool | <https://github.com/keanu19970228/paypal_fake_pages> |
| KerberosSec/Hemera | tool | <https://github.com/KerberosSec/Hemera> |
| king04aman/Phishing | tool | <https://github.com/king04aman/Phishing> |
| KINGSABRI/creds-harvester | tool | <https://github.com/KINGSABRI/creds-harvester> |
| Kl0ibi/esp32_hackingtool | web-platform | <https://github.com/Kl0ibi/esp32_hackingtool> |
| kleo/android-portals | web-platform | <https://github.com/kleo/android-portals> |
| KnightmareVIIVIIXC/AIO-Firebog-Blocklists | cli-tool | <https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists> |
| KnightSec-Official/Phlexish | tool | <https://github.com/KnightSec-Official/Phlexish> |
| krishnakatyal/Elliot | cli-tool | <https://github.com/krishnakatyal/Elliot> |
| KURO-CODE/Skeleton | tool | <https://github.com/KURO-CODE/Skeleton> |
| kurogai/nero-phishing-server | tool | <https://github.com/kurogai/nero-phishing-server> |
| kushvaibhav/phish.py | tool | <https://github.com/kushvaibhav/phish.py> |
| l4rm4nd/PhishDock | container | <https://github.com/l4rm4nd/PhishDock> |
| LakshyaSharma207/CamPhish | tool | <https://github.com/LakshyaSharma207/CamPhish> |
| landoncrabtree/ScrapeIn | tool | <https://github.com/landoncrabtree/ScrapeIn> |
| Largo-m/cyphisher | tool | <https://github.com/Largo-m/cyphisher> |
| Lennolium/PrivacyShield | tool | <https://github.com/Lennolium/PrivacyShield> |
| LetsDefend/Phishing-Email-Analysis | tool | <https://github.com/LetsDefend/Phishing-Email-Analysis> |
| liakoyras/thesis-phishing-email-detection | research-project | <https://github.com/liakoyras/thesis-phishing-email-detection> |
| LinkSec/phishing-templates | tool | <https://github.com/LinkSec/phishing-templates> |
| LiveGray/OPENORCHID | tool | <https://github.com/LiveGray/OPENORCHID> |
| Lookyloo/phishtank-lookup | api-service | <https://github.com/Lookyloo/phishtank-lookup> |
| loosehose/stride | framework | <https://github.com/loosehose/stride> |
| lp-db/lp-db | dataset | <https://github.com/lp-db/lp-db> |
| lucasayres/url-feature-extractor | dataset | <https://github.com/lucasayres/url-feature-extractor> |
| Lucksi/Titanium | tool | <https://github.com/Lucksi/Titanium> |
| lucthienphong1120/BITB-Phishing | tool | <https://github.com/lucthienphong1120/BITB-Phishing> |
| LxaNce-Hacker/lxancephisher | framework | <https://github.com/LxaNce-Hacker/lxancephisher> |
| LxaNce-Hacker/TechDeceit | dashboard | <https://github.com/LxaNce-Hacker/TechDeceit> |
| lynxthecat/adblock-lean | tool | <https://github.com/lynxthecat/adblock-lean> |
| M4cs/BlackEye-Python | tool | <https://github.com/M4cs/BlackEye-Python> |
| m4lal0/camShots | tool | <https://github.com/m4lal0/camShots> |
| m4n3dw0lf/pythem | container | <https://github.com/m4n3dw0lf/pythem> |
| machine1337/shortenurl | tool | <https://github.com/machine1337/shortenurl> |
| machine1337/userfinder | web-platform | <https://github.com/machine1337/userfinder> |
| madhanmaaz/white-spikes | tool | <https://github.com/madhanmaaz/white-spikes> |
| mamba-9mm/phishing | tool | <https://github.com/mamba-9mm/phishing> |
| manashma/BlackManPhishing | tool | <https://github.com/manashma/BlackManPhishing> |
| manic-code/Emerging-Malicious-Domain-Blocklist | tool | <https://github.com/manic-code/Emerging-Malicious-Domain-Blocklist> |
| marco-acorte/antispam-it | dataset | <https://github.com/marco-acorte/antispam-it> |
| marcosValle/awesome-windows-red-team | awesome-list | <https://github.com/marcosValle/awesome-windows-red-team> |
| martinsohn/Office-phish-templates | tool | <https://github.com/martinsohn/Office-phish-templates> |
| MattKeeley/Spoofy | tool | <https://github.com/MattKeeley/Spoofy> |
| mauricelambert/MaliciousPDF | library | <https://github.com/mauricelambert/MaliciousPDF> |
| meetsalmvn/S-Bait | framework | <https://github.com/meetsalmvn/S-Bait> |
| mgeeky/PhishingPost | tool | <https://github.com/mgeeky/PhishingPost> |
| mgeeky/VisualBasicObfuscator | tool | <https://github.com/mgeeky/VisualBasicObfuscator> |
| mirkoviviano/FYP-Fuck-You-Phisher | tool | <https://github.com/mirkoviviano/FYP-Fuck-You-Phisher> |
| Mixore/Phishing-Discord-Servers-List | research-project | <https://github.com/Mixore/Phishing-Discord-Servers-List> |
| moghimi/phishdetector | browser-extension | <https://github.com/moghimi/phishdetector> |
| MohammedRaouf99/Evil-AP | tool | <https://github.com/MohammedRaouf99/Evil-AP> |
| molangning/fire-av | tool | <https://github.com/molangning/fire-av> |
| monkeym4ster/DomainFuzz | tool | <https://github.com/monkeym4ster/DomainFuzz> |
| moorada/neferpitool | tool | <https://github.com/moorada/neferpitool> |
| morgenm/nlp-ai-phishing | tool | <https://github.com/morgenm/nlp-ai-phishing> |
| mrjuice01/shark01 | tool | <https://github.com/mrjuice01/shark01> |
| MrLuit/EtherScamDB | dataset | <https://github.com/MrLuit/EtherScamDB> |
| MrM8BRH/Privacy-Security-FOSS-Resources | awesome-list | <https://github.com/MrM8BRH/Privacy-Security-FOSS-Resources> |
| mrsheepsheep/idp-passthrough-phishing | tool | <https://github.com/mrsheepsheep/idp-passthrough-phishing> |
| mvondracek/wifimitm | tool | <https://github.com/mvondracek/wifimitm> |
| nayanmapara/PhishBuster | research-project | <https://github.com/nayanmapara/PhishBuster> |
| Nehboro/nehboro | browser-extension | <https://github.com/Nehboro/nehboro> |
| NickTaylor0/trawler | web-platform | <https://github.com/NickTaylor0/trawler> |
| nickvourd/RTI-Toolkit | plugin | <https://github.com/nickvourd/RTI-Toolkit> |
| nico-duitsmann/goldphish | tool | <https://github.com/nico-duitsmann/goldphish> |
| ninoseki/miteru | tool | <https://github.com/ninoseki/miteru> |
| ninoseki/osakana | research-project | <https://github.com/ninoseki/osakana> |
| notdodo/docker-sneaky-gophish | container | <https://github.com/notdodo/docker-sneaky-gophish> |
| obscuritylabs/InfoPhish | tool | <https://github.com/obscuritylabs/InfoPhish> |
| olihough86/stinkyphish | research-project | <https://github.com/olihough86/stinkyphish> |
| olizimmermann/phishcollector | framework | <https://github.com/olizimmermann/phishcollector> |
| omergunal/PoT | tool | <https://github.com/omergunal/PoT> |
| operatorequals/wormnest | tool | <https://github.com/operatorequals/wormnest> |
| Optane002/ZPhisher | cli-tool | <https://github.com/Optane002/ZPhisher> |
| OspreyProject/Osprey | browser-extension | <https://github.com/OspreyProject/Osprey> |
| P-BitM-Framework/P-BitM | container | <https://github.com/P-BitM-Framework/P-BitM> |
| P0cL4bs/flexphish | framework | <https://github.com/P0cL4bs/flexphish> |
| Panda-Bro4you/oPANDAoPhishing | tool | <https://github.com/Panda-Bro4you/oPANDAoPhishing> |
| pembriahmad/EAS-Phish | cli-tool | <https://github.com/pembriahmad/EAS-Phish> |
| pentestgeek/phishing-frenzy | framework | <https://github.com/pentestgeek/phishing-frenzy> |
| perviz19/EchoPhish | tool | <https://github.com/perviz19/EchoPhish> |
| philomathic-guy/Malicious-Web-Content-Detection-Using-Machine-Learning | browser-extension | <https://github.com/philomathic-guy/Malicious-Web-Content-Detection-Using-Machine-Learning> |
| phish-report/IOK | tool | <https://github.com/phish-report/IOK> |
| Phishcan/phishcan-data | dataset | <https://github.com/Phishcan/phishcan-data> |
| phishdestroy/medium-archive-phishdestroy | web-platform | <https://github.com/phishdestroy/medium-archive-phishdestroy> |
| phishdestroy/Nigerian-dignity | directory | <https://github.com/phishdestroy/Nigerian-dignity> |
| phishdestroy/ScamIntelLogs | research-project | <https://github.com/phishdestroy/ScamIntelLogs> |
| phishdestroy/trustname-evidence | dataset | <https://github.com/phishdestroy/trustname-evidence> |
| Phishing-Database/Phishing.Database | dataset | <https://github.com/Phishing-Database/Phishing.Database> |
| phishingclub/phishingclub | framework | <https://github.com/phishingclub/phishingclub> |
| phishingclub/session-sushi | browser-extension | <https://github.com/phishingclub/session-sushi> |
| PhishyAlice/awesome-phishing | awesome-list | <https://github.com/PhishyAlice/awesome-phishing> |
| pinkythegawd/youtube-phishing-page | tool | <https://github.com/pinkythegawd/youtube-phishing-page> |
| pionxzh/FakeUrlBar | tool | <https://github.com/pionxzh/FakeUrlBar> |
| Pipioli/social-pay | tool | <https://github.com/Pipioli/social-pay> |
| Pizz33/FTPlnk_phishing | tool | <https://github.com/Pizz33/FTPlnk_phishing> |
| polkadot-js/phishing | awesome-list | <https://github.com/polkadot-js/phishing> |
| portable36/SpyPhisher | tool | <https://github.com/portable36/SpyPhisher> |
| PrimePoobah/Pi-hole-Blocklist-Catalog | directory | <https://github.com/PrimePoobah/Pi-hole-Blocklist-Catalog> |
| princekrvert/Asura | tool | <https://github.com/princekrvert/Asura> |
| purple-ranger-0/ptrack-mobiletracker | tool | <https://github.com/purple-ranger-0/ptrack-mobiletracker> |
| qeeqbox/url-sandbox | container | <https://github.com/qeeqbox/url-sandbox> |
| quantumcore/NetworkStealer | framework | <https://github.com/quantumcore/NetworkStealer> |
| R3LI4NT/articulos | tool | <https://github.com/R3LI4NT/articulos> |
| r4msolo/pyshing | tool | <https://github.com/r4msolo/pyshing> |
| r4tur1/NullPhish | plugin | <https://github.com/r4tur1/NullPhish> |
| raginx/gophish-ng | framework | <https://github.com/raginx/gophish-ng> |
| Raikia/FiercePhish | framework | <https://github.com/Raikia/FiercePhish> |
| ravenastar-js/shortlinks-scams | tool | <https://github.com/ravenastar-js/shortlinks-scams> |
| ravisharma011/RSPhisher | plugin | <https://github.com/ravisharma011/RSPhisher> |
| RedFurrFox/PSpammer | tool | <https://github.com/RedFurrFox/PSpammer> |
| RedSiege/EXCELntDonut | cli-tool | <https://github.com/RedSiege/EXCELntDonut> |
| redteamsecurity2023/EvilnoVNC | container | <https://github.com/redteamsecurity2023/EvilnoVNC> |
| rencora/evilginx3-phishlet-templates | tool | <https://github.com/rencora/evilginx3-phishlet-templates> |
| render437/render.phisher | framework | <https://github.com/render437/render.phisher> |
| rewiaca/telegram-social-engineering-tool | framework | <https://github.com/rewiaca/telegram-social-engineering-tool> |
| Rickidevs/RickPhis | tool | <https://github.com/Rickidevs/RickPhis> |
| ritheshnayak/RM-phisher | cli-tool | <https://github.com/ritheshnayak/RM-phisher> |
| rivetternregard/acid-test-osint-scam-checker | tool | <https://github.com/rivetternregard/acid-test-osint-scam-checker> |
| rnlioilm/passmepass | tool | <https://github.com/rnlioilm/passmepass> |
| robinroy03/twitter-phishing | research-project | <https://github.com/robinroy03/twitter-phishing> |
| romainmarcoux/malicious-domains | tool | <https://github.com/romainmarcoux/malicious-domains> |
| romainmarcoux/malicious-outgoing-ip | tool | <https://github.com/romainmarcoux/malicious-outgoing-ip> |
| rsmusllp/king-phisher-plugins | plugin | <https://github.com/rsmusllp/king-phisher-plugins> |
| rsmusllp/king-phisher-templates | framework | <https://github.com/rsmusllp/king-phisher-templates> |
| rubikproxy/rubikphish | tool | <https://github.com/rubikproxy/rubikphish> |
| s0ld13rr/claude-code-backdoor | tool | <https://github.com/s0ld13rr/claude-code-backdoor> |
| safebuffer/edge-hot-delivery | cli-tool | <https://github.com/safebuffer/edge-hot-delivery> |
| SagarBiswas-MultiHAT/PhishGuard-AI | dataset | <https://github.com/SagarBiswas-MultiHAT/PhishGuard-AI> |
| SajidIbnNayeem/CphishTermux | tool | <https://github.com/SajidIbnNayeem/CphishTermux> |
| salihpy/TgaHacking | tool | <https://github.com/salihpy/TgaHacking> |
| sammwyy/SpearCopy | api-service | <https://github.com/sammwyy/SpearCopy> |
| SamueleAmato/exaPhisher | tool | <https://github.com/SamueleAmato/exaPhisher> |
| Schillings/SwordPhish | tool | <https://github.com/Schillings/SwordPhish> |
| seanthegeek/yaramail | library | <https://github.com/seanthegeek/yaramail> |
| secleGhost/Devil-IP-Grabber | framework | <https://github.com/secleGhost/Devil-IP-Grabber> |
| sexettin78/sexettintool | tool | <https://github.com/sexettin78/sexettintool> |
| shaeferd/Phishing-Detection | tool | <https://github.com/shaeferd/Phishing-Detection> |
| sheatsley/datasets | dataset | <https://github.com/sheatsley/datasets> |
| shivaya-dav/DogeRat | tool | <https://github.com/shivaya-dav/DogeRat> |
| Shlucus/FlipperZero-GooglePortal | web-platform | <https://github.com/Shlucus/FlipperZero-GooglePortal> |
| sid321axn/Detection_of_Malicious_URLs | library | <https://github.com/sid321axn/Detection_of_Malicious_URLs> |
| siddhant385/flask-phishing | framework | <https://github.com/siddhant385/flask-phishing> |
| SiddhantOffl/cam-virus | cli-tool | <https://github.com/SiddhantOffl/cam-virus> |
| simplerhacking/Evilginx-Course | tool | <https://github.com/simplerhacking/Evilginx-Course> |
| simplerhacking/Evilginx3-Discord-Phishlet | research-project | <https://github.com/simplerhacking/Evilginx3-Discord-Phishlet> |
| simplerhacking/Evilginx3-Microsoft365-Phishlet | tool | <https://github.com/simplerhacking/Evilginx3-Microsoft365-Phishlet> |
| simplerhacking/Evilginx3-Phishlets | tool | <https://github.com/simplerhacking/Evilginx3-Phishlets> |
| simplerhacking/Phishing-Keyword-List | tool | <https://github.com/simplerhacking/Phishing-Keyword-List> |
| simplerhacking/Phishlet-Creator | tool | <https://github.com/simplerhacking/Phishlet-Creator> |
| Sitiaro/Phisher-X | cli-tool | <https://github.com/Sitiaro/Phisher-X> |
| sjbell/phishalytics | api-service | <https://github.com/sjbell/phishalytics> |
| sjhgvr/oisd | tool | <https://github.com/sjhgvr/oisd> |
| sky9262/phishEye | tool | <https://github.com/sky9262/phishEye> |
| smed79/easylist-hosts | tool | <https://github.com/smed79/easylist-hosts> |
| sneakerhax/PyPhisher | tool | <https://github.com/sneakerhax/PyPhisher> |
| solanav/phishflood | tool | <https://github.com/solanav/phishflood> |
| SpiderLabs/Jorogumo | tool | <https://github.com/SpiderLabs/Jorogumo> |
| spieredd/PRONOTE-CLONE-PHISHING-WEBSITE | api-service | <https://github.com/spieredd/PRONOTE-CLONE-PHISHING-WEBSITE> |
| spyboy-productions/Facad1ng | dashboard | <https://github.com/spyboy-productions/Facad1ng> |
| sublime-security/emailrep.io | api-service | <https://github.com/sublime-security/emailrep.io> |
| sublime-security/static-files | tool | <https://github.com/sublime-security/static-files> |
| sublime-security/sublime-platform | web-platform | <https://github.com/sublime-security/sublime-platform> |
| sublime-security/sublime-rules | tool | <https://github.com/sublime-security/sublime-rules> |
| superagent-ai/brin | tool | <https://github.com/superagent-ai/brin> |
| surajr/URL-Classification | tool | <https://github.com/surajr/URL-Classification> |
| SwiftOnSecurity/SwiftFilter | tool | <https://github.com/SwiftOnSecurity/SwiftFilter> |
| SyedShaheerHussain/Anti_Phishing_Email_Detector_gui | dashboard | <https://github.com/SyedShaheerHussain/Anti_Phishing_Email_Detector_gui> |
| SystemJargon/filters | tool | <https://github.com/SystemJargon/filters> |
| t0mer/SafeUrl | container | <https://github.com/t0mer/SafeUrl> |
| t4d/PhishingKit-Yara-Rules | tool | <https://github.com/t4d/PhishingKit-Yara-Rules> |
| t4d/PhishingKit-Yara-Search | tool | <https://github.com/t4d/PhishingKit-Yara-Search> |
| t4d/StalkPhish | research-project | <https://github.com/t4d/StalkPhish> |
| t4d/StalkPhish-OSS | tool | <https://github.com/t4d/StalkPhish-OSS> |
| taielab/Taie-AutoPhishing | tool | <https://github.com/taielab/Taie-AutoPhishing> |
| Tanmay-Tiwaricyber/tphisher | framework | <https://github.com/Tanmay-Tiwaricyber/tphisher> |
| tassoneroberto/phishing-websites | research-project | <https://github.com/tassoneroberto/phishing-websites> |
| TbhVishal/ClickShield | api-service | <https://github.com/TbhVishal/ClickShield> |
| Tempest-Solutions-Company/pihole_blocklists | research-project | <https://github.com/Tempest-Solutions-Company/pihole_blocklists> |
| tevora-threat/Dragnet | tool | <https://github.com/tevora-threat/Dragnet> |
| TH3xACE/genAvatar | tool | <https://github.com/TH3xACE/genAvatar> |
| The-Robin-Hood/Portal-Xtend | web-platform | <https://github.com/The-Robin-Hood/Portal-Xtend> |
| thelinuxuser-choice/hidephish | tool | <https://github.com/thelinuxuser-choice/hidephish> |
| TheQmaks/phishgram | framework | <https://github.com/TheQmaks/phishgram> |
| TheresAFewConors/Sooty | cli-tool | <https://github.com/TheresAFewConors/Sooty> |
| thiagoaraujosec/YPhish | tool | <https://github.com/thiagoaraujosec/YPhish> |
| Toxic-Noob/Link-X | framework | <https://github.com/Toxic-Noob/Link-X> |
| trailofbits/tacklebox | framework | <https://github.com/trailofbits/tacklebox> |
| trailofbits/trailofphish | research-project | <https://github.com/trailofbits/trailofphish> |
| treeleaves30760/FakeFaceBook | tool | <https://github.com/treeleaves30760/FakeFaceBook> |
| trusteddomainproject/OpenDKIM | tool | <https://github.com/trusteddomainproject/OpenDKIM> |
| TYehan/SocialPhish | tool | <https://github.com/TYehan/SocialPhish> |
| U53RW4R3/ShortcutGen | tool | <https://github.com/U53RW4R3/ShortcutGen> |
| UndeadSec/EvilURL | research-project | <https://github.com/UndeadSec/EvilURL> |
| UndeadSec/SocialFish | tool | <https://github.com/UndeadSec/SocialFish> |
| UndeadSec/SocialFishMobile | research-project | <https://github.com/UndeadSec/SocialFishMobile> |
| v3lip/PhishingSpammer | tool | <https://github.com/v3lip/PhishingSpammer> |
| v4d1/SpoofThatMail | tool | <https://github.com/v4d1/SpoofThatMail> |
| varrickkoh/IDN-Homograph-Generator | tool | <https://github.com/varrickkoh/IDN-Homograph-Generator> |
| vexsx/instagram-phishing | web-platform | <https://github.com/vexsx/instagram-phishing> |
| vinaytz/Vphisher | tool | <https://github.com/vinaytz/Vphisher> |
| vneogi199/Phishing-detection-using-data-mining-Python | browser-extension | <https://github.com/vneogi199/Phishing-detection-using-data-mining-Python> |
| vpav/doppelganger | tool | <https://github.com/vpav/doppelganger> |
| w0h1v/mcp-dnstwist | tool | <https://github.com/w0h1v/mcp-dnstwist> |
| wariv/DarkLnk | tool | <https://github.com/wariv/DarkLnk> |
| werdox/phishfactory | tool | <https://github.com/werdox/phishfactory> |
| wesleyraptor/streamingphish | container | <https://github.com/wesleyraptor/streamingphish> |
| Whitecat18/Javahexor | library | <https://github.com/Whitecat18/Javahexor> |
| Whomrx666/Xphisher | tool | <https://github.com/Whomrx666/Xphisher> |
| wifiphisher/extra-phishing-pages | tool | <https://github.com/wifiphisher/extra-phishing-pages> |
| wifiphisher/wifiphisher | framework | <https://github.com/wifiphisher/wifiphisher> |
| wisespace-io/nettfiske | tool | <https://github.com/wisespace-io/nettfiske> |
| WorkofAditya/PhisherMan | cli-tool | <https://github.com/WorkofAditya/PhisherMan> |
| Wraient/Google-Phishing-with-ESP8266 | tool | <https://github.com/Wraient/Google-Phishing-with-ESP8266> |
| xbaysal11/phish-js | api-service | <https://github.com/xbaysal11/phish-js> |
| xiecat/goblin | tool | <https://github.com/xiecat/goblin> |
| XielQs/JsPhisher | tool | <https://github.com/XielQs/JsPhisher> |
| XiphosResearch/smsisher | research-project | <https://github.com/XiphosResearch/smsisher> |
| XKMR/discord-link-phishing | tool | <https://github.com/XKMR/discord-link-phishing> |
| yangr0/BlackPhish | research-project | <https://github.com/yangr0/BlackPhish> |
| yasserjanah/IZanamiFramework | framework | <https://github.com/yasserjanah/IZanamiFramework> |
| YehudaEi/Google-Fake-Login-Page | research-project | <https://github.com/YehudaEi/Google-Fake-Login-Page> |
| yeyintminthuhtut/Awesome-Red-Teaming | awesome-list | <https://github.com/yeyintminthuhtut/Awesome-Red-Teaming> |
| Yezz123-Archive/Phisher | tool | <https://github.com/Yezz123-Archive/Phisher> |
| yogeshwaran01/maskurl | framework | <https://github.com/yogeshwaran01/maskurl> |
| zachlagden/Pi-hole-Optimized-Blocklists | tool | <https://github.com/zachlagden/Pi-hole-Optimized-Blocklists> |
| Zaczero/pihole-phishtank | tool | <https://github.com/Zaczero/pihole-phishtank> |
| Zaeem20/VirusX5 | tool | <https://github.com/Zaeem20/VirusX5> |

### Privacy & Anonymity

| Name | Type | URL |
|---|---|---|
| 05nelsonm/kmp-tor | web-platform | <https://github.com/05nelsonm/kmp-tor> |
| 0x27/ssh_keyscanner | web-platform | <https://github.com/0x27/ssh_keyscanner> |
| 0xdea/configurations | web-platform | <https://github.com/0xdea/configurations> |
| 19-84/redd-archiver | container | <https://github.com/19-84/redd-archiver> |
| 39ff/docker-rotating-proxy | container | <https://github.com/39ff/docker-rotating-proxy> |
| 3xploitGuy/torwebsite | container | <https://github.com/3xploitGuy/torwebsite> |
| 7c/torfilter | tool | <https://github.com/7c/torfilter> |
| 813492291816/BitChan | tool | <https://github.com/813492291816/BitChan> |
| absingh31/Tor_Spider | api-service | <https://github.com/absingh31/Tor_Spider> |
| abysshint/tor-control-panel | dashboard | <https://github.com/abysshint/tor-control-panel> |
| Acira-dev/AciraBrowser | desktop-app | <https://github.com/Acira-dev/AciraBrowser> |
| Adamant-im/adamant | tool | <https://github.com/Adamant-im/adamant> |
| AdnanHodzic/anon-hotspot | tool | <https://github.com/AdnanHodzic/anon-hotspot> |
| AdvOR/advor | cli-tool | <https://github.com/AdvOR/advor> |
| aeonBTC/Mempal | tool | <https://github.com/aeonBTC/Mempal> |
| aforensics/HiddenVM | tool | <https://github.com/aforensics/HiddenVM> |
| aleff-github/onion-routing-anatomy | tool | <https://github.com/aleff-github/onion-routing-anatomy> |
| aliascash/alias-wallet-archive | web-platform | <https://github.com/aliascash/alias-wallet-archive> |
| alireza-rezaee/tor-nodes | tool | <https://github.com/alireza-rezaee/tor-nodes> |
| alphaSeclab/awesome-network-stuff | awesome-list | <https://github.com/alphaSeclab/awesome-network-stuff> |
| Am0rphous/Dark-Net-Collection | web-platform | <https://github.com/Am0rphous/Dark-Net-Collection> |
| amoghbl1/tor-browser | tool | <https://github.com/amoghbl1/tor-browser> |
| anmolksachan/CloudFail | dataset | <https://github.com/anmolksachan/CloudFail> |
| Anon-Planet/thgtoa | dashboard | <https://github.com/Anon-Planet/thgtoa> |
| anoni-net/docs | dashboard | <https://github.com/anoni-net/docs> |
| anonomi-org/anonomi-android | web-platform | <https://github.com/anonomi-org/anonomi-android> |
| AnonymousMessenger/AnonymousMessenger | tool | <https://github.com/AnonymousMessenger/AnonymousMessenger> |
| ANTISEC12/torforwindows | tool | <https://github.com/ANTISEC12/torforwindows> |
| antitree/private-tor-network | container | <https://github.com/antitree/private-tor-network> |
| arades79/hyperdome | research-project | <https://github.com/arades79/hyperdome> |
| ArchiveBox/good-karma-kit | container | <https://github.com/ArchiveBox/good-karma-kit> |
| arminkz/TorPi | tool | <https://github.com/arminkz/TorPi> |
| assafmo/IsTorExit | cli-tool | <https://github.com/assafmo/IsTorExit> |
| atx/prometheus-tor_exporter | tool | <https://github.com/atx/prometheus-tor_exporter> |
| audibleblink/doxycannon | container | <https://github.com/audibleblink/doxycannon> |
| Avenge-hacker/Instainsane | tool | <https://github.com/Avenge-hacker/Instainsane> |
| awesome-windows11/CensorNet | awesome-list | <https://github.com/awesome-windows11/CensorNet> |
| ayadseghairi/tornet | library | <https://github.com/ayadseghairi/tornet> |
| baatout/tor-ip-rotation-python-example | tool | <https://github.com/baatout/tor-ip-rotation-python-example> |
| bad-antics/marshall | desktop-app | <https://github.com/bad-antics/marshall> |
| baroxyton/zlibrary-eapi-documentation | mobile-app | <https://github.com/baroxyton/zlibrary-eapi-documentation> |
| basil00/Tallow | tool | <https://github.com/basil00/Tallow> |
| BenWestgate/Bails | tool | <https://github.com/BenWestgate/Bails> |
| bezumiya/GoLiveBypass | plugin | <https://github.com/bezumiya/GoLiveBypass> |
| bhikandeshmukh/instainsane | cli-tool | <https://github.com/bhikandeshmukh/instainsane> |
| blckbx/lnd-hybrid-mode | dashboard | <https://github.com/blckbx/lnd-hybrid-mode> |
| bleachbit.org | tool | <https://bleachbit.org/> |
| blocoio/snowflake | mobile-app | <https://github.com/blocoio/snowflake> |
| blueprint-freespeech/gosling | web-platform | <https://github.com/blueprint-freespeech/gosling> |
| brainfucksec/archtorify | tool | <https://github.com/brainfucksec/archtorify> |
| BrowserBox/BrowserBox | tool | <https://github.com/BrowserBox/BrowserBox> |
| brunneis/scihub-downloader | container | <https://github.com/brunneis/scihub-downloader> |
| bulwark-crypto/Bulwark | tool | <https://github.com/bulwark-crypto/Bulwark> |
| ByteBreach/tornet | tool | <https://github.com/ByteBreach/tornet> |
| captn3m0/cosmere-books | tool | <https://github.com/captn3m0/cosmere-books> |
| cbeuw/Cloak | tool | <https://github.com/cbeuw/Cloak> |
| cea-sec/TorPylle | research-project | <https://github.com/cea-sec/TorPylle> |
| Chara-Freedom/Tor-Portable | tool | <https://github.com/Chara-Freedom/Tor-Portable> |
| chr15m/gitnonymous | cli-tool | <https://github.com/chr15m/gitnonymous> |
| ciehanski/onionbox | web-platform | <https://github.com/ciehanski/onionbox> |
| cmars/onionpipe | web-platform | <https://github.com/cmars/onionpipe> |
| cmars/ormesh | web-platform | <https://github.com/cmars/ormesh> |
| commit-issues/google-dorking | tool | <https://github.com/commit-issues/google-dorking> |
| ComradOrg/Comrad | api-service | <https://github.com/ComradOrg/Comrad> |
| ContentAutomation/YouTubeWatcher | container | <https://github.com/ContentAutomation/YouTubeWatcher> |
| coskundeniz/ad_clicker | cli-tool | <https://github.com/coskundeniz/ad_clicker> |
| cowlicks/bypasser | browser-extension | <https://github.com/cowlicks/bypasser> |
| coyim/coyim | web-platform | <https://github.com/coyim/coyim> |
| creekorful/bathyscaphe | web-platform | <https://github.com/creekorful/bathyscaphe> |
| cretz/bine | library | <https://github.com/cretz/bine> |
| cretz/tor-dht-poc | tool | <https://github.com/cretz/tor-dht-poc> |
| cristiancmoises/torando | tool | <https://github.com/cristiancmoises/torando> |
| cryptomator.org | cli-tool | <https://cryptomator.org/> |
| CScorza/Data-Protection | tool | <https://github.com/CScorza/Data-Protection> |
| CyberAndi/CyberSecurity-Box | tool | <https://github.com/CyberAndi/CyberSecurity-Box> |
| cybersertex/Tor-Proxychains | tool | <https://github.com/cybersertex/Tor-Proxychains> |
| cyphernet-labs/cyphernet.rs | framework | <https://github.com/cyphernet-labs/cyphernet.rs> |
| cypnk/Bare | directory | <https://github.com/cypnk/Bare> |
| Da2dalus/CerebroSMS | api-service | <https://github.com/Da2dalus/CerebroSMS> |
| daijro/EssayGen | api-service | <https://github.com/daijro/EssayGen> |
| danielstjules/toragent | tool | <https://github.com/danielstjules/toragent> |
| DanWin/le-chat-php | web-platform | <https://github.com/DanWin/le-chat-php> |
| DanWin/onion-link-list | web-platform | <https://github.com/DanWin/onion-link-list> |
| dbeley/gsmarena-scraper | container | <https://github.com/dbeley/gsmarena-scraper> |
| DcodingTheWeb/ProxAllium | dashboard | <https://github.com/DcodingTheWeb/ProxAllium> |
| Debajyoti0-0/ToriFY | cli-tool | <https://github.com/Debajyoti0-0/ToriFY> |
| deedy5/requests_tor | tool | <https://github.com/deedy5/requests_tor> |
| deep-fingerprinting/df | dataset | <https://github.com/deep-fingerprinting/df> |
| deeponion/deeponion-legacy | tool | <https://github.com/deeponion/deeponion-legacy> |
| Delta-Kronecker/Delta-Tor | web-platform | <https://github.com/Delta-Kronecker/Delta-Tor> |
| Delta-Kronecker/Tor-Bridges-Collector | tool | <https://github.com/Delta-Kronecker/Tor-Bridges-Collector> |
| denisse-dev/irc-bouncer | tool | <https://github.com/denisse-dev/irc-bouncer> |
| DennisFeldbusch/CheatSheet | tool | <https://github.com/DennisFeldbusch/CheatSheet> |
| deutsia/deutsia-radio | tool | <https://github.com/deutsia/deutsia-radio> |
| dhtpdud/YANGPA | tool | <https://github.com/dhtpdud/YANGPA> |
| digitalautonomy/wahay | web-platform | <https://github.com/digitalautonomy/wahay> |
| digitalblossom/alternative-frontends | awesome-list | <https://github.com/digitalblossom/alternative-frontends> |
| DigneZzZ/remnawave-scripts | tool | <https://github.com/DigneZzZ/remnawave-scripts> |
| disappeerlabs/disappeer | dashboard | <https://github.com/disappeerlabs/disappeer> |
| Disconnect Search | tool | <https://search.disconnect.me/> |
| dockage/tor-privoxy | container | <https://github.com/dockage/tor-privoxy> |
| dockur/tor | container | <https://github.com/dockur/tor> |
| DotNetAge/scrapy_plus | plugin | <https://github.com/DotNetAge/scrapy_plus> |
| dr-bonez/tor-v3-vanity | tool | <https://github.com/dr-bonez/tor-v3-vanity> |
| drduh/Debian-Privacy-Server-Guide | dashboard | <https://github.com/drduh/Debian-Privacy-Server-Guide> |
| dryruby/tor.rb | library | <https://github.com/dryruby/tor.rb> |
| du82/nonograph | web-platform | <https://github.com/du82/nonograph> |
| DuckDuckGo | tool | <https://duckduckgo.com> |
| dunglas/php-torcontrol | library | <https://github.com/dunglas/php-torcontrol> |
| DusanMadar/ScrapeMeAgain | container | <https://github.com/DusanMadar/ScrapeMeAgain> |
| DusanMadar/TorIpChanger | container | <https://github.com/DusanMadar/TorIpChanger> |
| DVKunion/SeaMoon | tool | <https://github.com/DVKunion/SeaMoon> |
| EddiePiazza/schedule-4-real | plugin | <https://github.com/EddiePiazza/schedule-4-real> |
| Edu4rdSHL/tor-router | tool | <https://github.com/Edu4rdSHL/tor-router> |
| ehloonion/onionmx | web-platform | <https://github.com/ehloonion/onionmx> |
| elvesmrodrigues/scrapy-tor-proxy-rotation | tool | <https://github.com/elvesmrodrigues/scrapy-tor-proxy-rotation> |
| elzabrowser/elza | desktop-app | <https://github.com/elzabrowser/elza> |
| Enegnei/JacobAppelbaumLeavesTor | tool | <https://github.com/Enegnei/JacobAppelbaumLeavesTor> |
| Enkidu-6/tor-ddos | tool | <https://github.com/Enkidu-6/tor-ddos> |
| erdiaker/torrequest | tool | <https://github.com/erdiaker/torrequest> |
| ethereum/webtor-rs | cli-tool | <https://github.com/ethereum/webtor-rs> |
| evildevill/instahack | tool | <https://github.com/evildevill/instahack> |
| FaFre/WebLibre | container | <https://github.com/FaFre/WebLibre> |
| FedericoCeratto/nim-tor | web-platform | <https://github.com/FedericoCeratto/nim-tor> |
| Feliz-SZK/Neutron | tool | <https://github.com/Feliz-SZK/Neutron> |
| flicus/flibot | tool | <https://github.com/flicus/flibot> |
| foxhole-team/foxhole-guard | tool | <https://github.com/foxhole-team/foxhole-guard> |
| FoxMoss/kurrat | tool | <https://github.com/FoxMoss/kurrat> |
| freedomofpress/container-onion-service | container | <https://github.com/freedomofpress/container-onion-service> |
| freedomofpress/fingerprint-securedrop | web-platform | <https://github.com/freedomofpress/fingerprint-securedrop> |
| garethflowers/tor-browser-portable | tool | <https://github.com/garethflowers/tor-browser-portable> |
| Gedsh/InviZible | mobile-app | <https://github.com/Gedsh/InviZible> |
| gergelykalman/torspray | tool | <https://github.com/gergelykalman/torspray> |
| GFW4Fun/x-ui-pro | cli-tool | <https://github.com/GFW4Fun/x-ui-pro> |
| GH05T-HUNTER5/GH05T-INSTA | tool | <https://github.com/GH05T-HUNTER5/GH05T-INSTA> |
| GH05T-HUNTER5/insta-breaker | tool | <https://github.com/GH05T-HUNTER5/insta-breaker> |
| gh4rib/lyrebird | tool | <https://github.com/gh4rib/lyrebird> |
| Gianguyen1234/A-section-to-know-about-Tor | web-platform | <https://github.com/Gianguyen1234/A-section-to-know-about-Tor> |
| Gibiru | tool | <https://gibiru.com/> |
| givps/AutoScriptXray | tool | <https://github.com/givps/AutoScriptXray> |
| globaleaks/globaleaks-whistleblowing-software | web-platform | <https://github.com/globaleaks/globaleaks-whistleblowing-software> |
| GnosiWorks/Kryfo | tool | <https://github.com/GnosiWorks/Kryfo> |
| go-compile/localrelay | web-platform | <https://github.com/go-compile/localrelay> |
| goastian/midori-android | tool | <https://github.com/goastian/midori-android> |
| gosuda/portal-tunnel | web-platform | <https://github.com/gosuda/portal-tunnel> |
| grishmadev/conan | tool | <https://github.com/grishmadev/conan> |
| gSpotx2f/ruantiblock | research-project | <https://github.com/gSpotx2f/ruantiblock> |
| gSpotx2f/ruantiblock_openwrt | tool | <https://github.com/gSpotx2f/ruantiblock_openwrt> |
| guardianproject/orbot-android | tool | <https://github.com/guardianproject/orbot-android> |
| guardianproject/tor-android | library | <https://github.com/guardianproject/tor-android> |
| GuruProduction/GURUbyUnusLumen | mobile-app | <https://github.com/GuruProduction/GURUbyUnusLumen> |
| HalilDeniz/PrivacyNet | web-platform | <https://github.com/HalilDeniz/PrivacyNet> |
| hardcore-sushi/TorVirt | container | <https://github.com/hardcore-sushi/TorVirt> |
| hassio-addons/app-tor | plugin | <https://github.com/hassio-addons/app-tor> |
| haveno-dex/haveno | web-platform | <https://github.com/haveno-dex/haveno> |
| hazae41/echalote | tool | <https://github.com/hazae41/echalote> |
| HelloZeroNet/ZeroNet | tool | <https://github.com/HelloZeroNet/ZeroNet> |
| hnhx/librex | api-service | <https://github.com/hnhx/librex> |
| hnhx/website | tool | <https://github.com/hnhx/website> |
| hossein-mohseni/tor-GUI | dashboard | <https://github.com/hossein-mohseni/tor-GUI> |
| HotCakeX/Privacy-Anonymity-Compartmentalization | container | <https://github.com/HotCakeX/Privacy-Anonymity-Compartmentalization> |
| htrgouvea/nipe | tool | <https://github.com/htrgouvea/nipe> |
| hundehausen/tor-hidden-service-docker | container | <https://github.com/hundehausen/tor-hidden-service-docker> |
| hyundotio/magicpad | desktop-app | <https://github.com/hyundotio/magicpad> |
| iCepa/iCepa | plugin | <https://github.com/iCepa/iCepa> |
| igareck/anti-dpi-for-russia | cli-tool | <https://github.com/igareck/anti-dpi-for-russia> |
| igareck/vpn-configs-for-russia | cli-tool | <https://github.com/igareck/vpn-configs-for-russia> |
| Ilshidur/tor-relay-docker | container | <https://github.com/Ilshidur/tor-relay-docker> |
| ilyaglow/dockerfiles | container | <https://github.com/ilyaglow/dockerfiles> |
| Iman/javidnet | tool | <https://github.com/Iman/javidnet> |
| internetarchive/internetarchivebot | tool | <https://github.com/internetarchive/internetarchivebot> |
| InvisiProxy/InvisiProxyLTS | container | <https://github.com/InvisiProxy/InvisiProxyLTS> |
| ipsn/go-libtor | library | <https://github.com/ipsn/go-libtor> |
| isPique/Tor-IP-Changer | tool | <https://github.com/isPique/Tor-IP-Changer> |
| itshaadi/torbox | container | <https://github.com/itshaadi/torbox> |
| jakedent/seo-bot | tool | <https://github.com/jakedent/seo-bot> |
| james-see/elector | desktop-app | <https://github.com/james-see/elector> |
| jarocheng0123/Tor_VPN_BTC | tool | <https://github.com/jarocheng0123/Tor_VPN_BTC> |
| jehy/rutracker-free | cli-tool | <https://github.com/jehy/rutracker-free> |
| jivoi/ansible-pentest-with-tor | tool | <https://github.com/jivoi/ansible-pentest-with-tor> |
| jobiryasir/darkweb-data-breach-osint | research-project | <https://github.com/jobiryasir/darkweb-data-breach-osint> |
| joelverhagen/TorSharp | cli-tool | <https://github.com/joelverhagen/TorSharp> |
| johalputt/VayuPress | web-platform | <https://github.com/johalputt/VayuPress> |
| jonathancross/jc-docs | tool | <https://github.com/jonathancross/jc-docs> |
| jstrieb/ctf-collab | web-platform | <https://github.com/jstrieb/ctf-collab> |
| juev/tor-relay-scanner-go | tool | <https://github.com/juev/tor-relay-scanner-go> |
| Jugendhackt/haskell-ricochet | web-platform | <https://github.com/Jugendhackt/haskell-ricochet> |
| k4m4/onioff | tool | <https://github.com/k4m4/onioff> |
| k4m4/tor-detect | tool | <https://github.com/k4m4/tor-detect> |
| Kagi Search | tool | <https://kagi.com/> |
| karthi-the-hacker/SocialEngineer | api-service | <https://github.com/karthi-the-hacker/SocialEngineer> |
| kdmukai/raspi4_bitcoin_node_tutorial | dashboard | <https://github.com/kdmukai/raspi4_bitcoin_node_tutorial> |
| keepassxc.org | tool | <https://keepassxc.org/> |
| keroserene/snowflake | tool | <https://github.com/keroserene/snowflake> |
| KevinColemanInc/awesome-privacy | awesome-list | <https://github.com/KevinColemanInc/awesome-privacy> |
| KNG7-P/Se7en-Pro | cli-tool | <https://github.com/KNG7-P/Se7en-Pro> |
| koifinance/NixCore | web-platform | <https://github.com/koifinance/NixCore> |
| koroblabs/ferrite-server | tool | <https://github.com/koroblabs/ferrite-server> |
| kragniz/tor-controller | container | <https://github.com/kragniz/tor-controller> |
| kurogai/deepweb-scappering | tool | <https://github.com/kurogai/deepweb-scappering> |
| layters/testshop | research-project | <https://github.com/layters/testshop> |
| leplusorg/docker-tor | container | <https://github.com/leplusorg/docker-tor> |
| Limych/antizapret | tool | <https://github.com/Limych/antizapret> |
| lizzthabet/speculative-camouflage | tool | <https://github.com/lizzthabet/speculative-camouflage> |
| lspahija/torchestrator | container | <https://github.com/lspahija/torchestrator> |
| luantak/ToRat | web-platform | <https://github.com/luantak/ToRat> |
| lukechilds/onionoo-node-client | api-service | <https://github.com/lukechilds/onionoo-node-client> |
| m0rtem/CloudFail | dataset | <https://github.com/m0rtem/CloudFail> |
| MagicalBitcoin/libtor | tool | <https://github.com/MagicalBitcoin/libtor> |
| MakeFortuneQuietly/FreeProxyTor | tool | <https://github.com/MakeFortuneQuietly/FreeProxyTor> |
| malfp/tormalwarefp | tool | <https://github.com/malfp/tormalwarefp> |
| malwareworld/MalwareWorld | tool | <https://github.com/malwareworld/MalwareWorld> |
| maqp/tfc | web-platform | <https://github.com/maqp/tfc> |
| MarMarLabs/anon-research | research-project | <https://github.com/MarMarLabs/anon-research> |
| Marten4n6/TinyTor | cli-tool | <https://github.com/Marten4n6/TinyTor> |
| matejbasic/PythonScrapyBasicSetup | api-service | <https://github.com/matejbasic/PythonScrapyBasicSetup> |
| matiasinsaurralde/transports | tool | <https://github.com/matiasinsaurralde/transports> |
| matinrco/tor | tool | <https://github.com/matinrco/tor> |
| mattcg/socks5-http-client | cli-tool | <https://github.com/mattcg/socks5-http-client> |
| mattes/rotating-proxy | container | <https://github.com/mattes/rotating-proxy> |
| maximilianromer/Onion-Search-MCP | web-platform | <https://github.com/maximilianromer/Onion-Search-MCP> |
| MBHudson/Vigilante-Toolset | web-platform | <https://github.com/MBHudson/Vigilante-Toolset> |
| meanos/meanOs | tool | <https://github.com/meanos/meanOs> |
| meejah/carml | cli-tool | <https://github.com/meejah/carml> |
| meejah/txtorcon | tool | <https://github.com/meejah/txtorcon> |
| MeisterP/torbrowser-overlay | tool | <https://github.com/MeisterP/torbrowser-overlay> |
| metamarcdw/nowallet | tool | <https://github.com/metamarcdw/nowallet> |
| michaldziuba03/tor-client | cli-tool | <https://github.com/michaldziuba03/tor-client> |
| milesrichardson/docker-onion-nmap | container | <https://github.com/milesrichardson/docker-onion-nmap> |
| MiniRobotDev/TorBridge | tool | <https://github.com/MiniRobotDev/TorBridge> |
| mishakorzik/proxy-terminal | cli-tool | <https://github.com/mishakorzik/proxy-terminal> |
| mmcloughlin/pearl | tool | <https://github.com/mmcloughlin/pearl> |
| mohamed-ladjal-AI/auto_facebook_creator | tool | <https://github.com/mohamed-ladjal-AI/auto_facebook_creator> |
| mohamed-ladjal-AI/auto_facebook_creator_v2 | tool | <https://github.com/mohamed-ladjal-AI/auto_facebook_creator_v2> |
| monji024/GhostIp | tool | <https://github.com/monji024/GhostIp> |
| monsmain/ighack | tool | <https://github.com/monsmain/ighack> |
| mritd/dockerfile | container | <https://github.com/mritd/dockerfile> |
| MrMatin0/Aether | cli-tool | <https://github.com/MrMatin0/Aether> |
| mthbernardes/ipChecker | container | <https://github.com/mthbernardes/ipChecker> |
| mullvad.net | tool | <https://mullvad.net/> |
| multivoltage/adflyroboTOR | cli-tool | <https://github.com/multivoltage/adflyroboTOR> |
| mytechnotalent/TOR-Everything | dashboard | <https://github.com/mytechnotalent/TOR-Everything> |
| naborajs/Termux-Tor-IP-Rotator | web-platform | <https://github.com/naborajs/Termux-Tor-IP-Rotator> |
| negyio/negy | container | <https://github.com/negyio/negy> |
| NetworkCats/Merged-IP-Data | dataset | <https://github.com/NetworkCats/Merged-IP-Data> |
| Nickguitar/VPNTabs | container | <https://github.com/Nickguitar/VPNTabs> |
| nishant-Tiwari24/veil | desktop-app | <https://github.com/nishant-Tiwari24/veil> |
| nocturne-cybersecurity/Nocturne-Attack | framework | <https://github.com/nocturne-cybersecurity/Nocturne-Attack> |
| noob-hackers/ighack | tool | <https://github.com/noob-hackers/ighack> |
| norpol/opensshd-tor-easy-setup | web-platform | <https://github.com/norpol/opensshd-tor-easy-setup> |
| NOXCIS/Wiregate | container | <https://github.com/NOXCIS/Wiregate> |
| NPCmillionaire/unredact.tools | cli-tool | <https://github.com/NPCmillionaire/unredact.tools> |
| ntddk/onionstack | web-platform | <https://github.com/ntddk/onionstack> |
| ntddk/peeling-onions | web-platform | <https://github.com/ntddk/peeling-onions> |
| NullArray/NetSet | tool | <https://github.com/NullArray/NetSet> |
| NullHypothesis/exitmap | research-project | <https://github.com/NullHypothesis/exitmap> |
| NullHypothesis/scramblesuit | tool | <https://github.com/NullHypothesis/scramblesuit> |
| NullHypothesis/sybilhunter | tool | <https://github.com/NullHypothesis/sybilhunter> |
| NullHypothesis/zoossh | library | <https://github.com/NullHypothesis/zoossh> |
| nusenu/ansible-relayor | tool | <https://github.com/nusenu/ansible-relayor> |
| nusenu/OrNetStats | tool | <https://github.com/nusenu/OrNetStats> |
| nyxnor/onionjuggler | web-platform | <https://github.com/nyxnor/onionjuggler> |
| Obscurix/Obscurix | tool | <https://github.com/Obscurix/Obscurix> |
| offset/onion-vanity-address | web-platform | <https://github.com/offset/onion-vanity-address> |
| Onion-Search-Engine/Onion-Search-Engine-Android | mobile-app | <https://github.com/Onion-Search-Engine/Onion-Search-Engine-Android> |
| onionshare.org | tool | <https://onionshare.org/> |
| onionshare/onionshare | web-platform | <https://github.com/onionshare/onionshare> |
| onionshare/onionshare-android | web-platform | <https://github.com/onionshare/onionshare-android> |
| opsxcq/docker-tor | container | <https://github.com/opsxcq/docker-tor> |
| opsxcq/docker-tor-hiddenservice-nginx | container | <https://github.com/opsxcq/docker-tor-hiddenservice-nginx> |
| orjail/orjail | tool | <https://github.com/orjail/orjail> |
| osminogin/docker-tor-simple | container | <https://github.com/osminogin/docker-tor-simple> |
| osminogin/tornote | cli-tool | <https://github.com/osminogin/tornote> |
| osservatorionessuno/patela | cli-tool | <https://github.com/osservatorionessuno/patela> |
| Otsmane-Ahmed/sliver-tor-bridge | web-platform | <https://github.com/Otsmane-Ahmed/sliver-tor-bridge> |
| owerdogan/whoami-project | tool | <https://github.com/owerdogan/whoami-project> |
| p2pool-starter-stack/pithead | container | <https://github.com/p2pool-starter-stack/pithead> |
| PanagiotisDrakatos/T0rlib4Android | web-platform | <https://github.com/PanagiotisDrakatos/T0rlib4Android> |
| PanagiotisDrakatos/T0rlib4j | web-platform | <https://github.com/PanagiotisDrakatos/T0rlib4j> |
| parazyd/tordam | web-platform | <https://github.com/parazyd/tordam> |
| paulmillr/micro-key-producer | tool | <https://github.com/paulmillr/micro-key-producer> |
| Phinee/Onion-Search-Engine-Android | mobile-app | <https://github.com/Phinee/Onion-Search-Engine-Android> |
| pielco11/DOT | research-project | <https://github.com/pielco11/DOT> |
| pogzyb/asyncwhois | cli-tool | <https://github.com/pogzyb/asyncwhois> |
| Polycarbohydrate/awesome-tor | awesome-list | <https://github.com/Polycarbohydrate/awesome-tor> |
| privcycoin/privcy | tool | <https://github.com/privcycoin/privcy> |
| proton.me | tool | <https://proton.me/> |
| protonvpn.com | tool | <https://protonvpn.com/> |
| qeeqbox/woodpecker | tool | <https://github.com/qeeqbox/woodpecker> |
| quantumcore/iris | tool | <https://github.com/quantumcore/iris> |
| QuiteAFancyEmerald/InvisiProxy-Legacy | container | <https://github.com/QuiteAFancyEmerald/InvisiProxy-Legacy> |
| r0oth3x49/Tor | plugin | <https://github.com/r0oth3x49/Tor> |
| r3bo0tbx1/tor-guard-relay | container | <https://github.com/r3bo0tbx1/tor-guard-relay> |
| r3nt0n/torDDoS | web-platform | <https://github.com/r3nt0n/torDDoS> |
| R4yGM/garlicshare | web-platform | <https://github.com/R4yGM/garlicshare> |
| Raffy27/OrionBot | api-service | <https://github.com/Raffy27/OrionBot> |
| Raffy27/OrionPanel | dashboard | <https://github.com/Raffy27/OrionPanel> |
| Raffy27/OrionServer | web-platform | <https://github.com/Raffy27/OrionServer> |
| rahra/onioncat | tool | <https://github.com/rahra/onioncat> |
| ralphwetzel/theonionbox | dashboard | <https://github.com/ralphwetzel/theonionbox> |
| RD17/DeTor | api-service | <https://github.com/RD17/DeTor> |
| ResistalProxy/resistal | tool | <https://github.com/ResistalProxy/resistal> |
| ricochet-im/ricochet | dashboard | <https://github.com/ricochet-im/ricochet> |
| RightToPrivacy/snowflake-tor-service | web-platform | <https://github.com/RightToPrivacy/snowflake-tor-service> |
| RoboSats/robosats | tool | <https://github.com/RoboSats/robosats> |
| rosehgal/tortipi | tool | <https://github.com/rosehgal/tortipi> |
| ruped24/tor_ip_switcher | tool | <https://github.com/ruped24/tor_ip_switcher> |
| ruped24/toriptables2 | web-platform | <https://github.com/ruped24/toriptables2> |
| ruped24/toriptables3 | web-platform | <https://github.com/ruped24/toriptables3> |
| rustybird/corridor | tool | <https://github.com/rustybird/corridor> |
| rustybird/qubes-app-split-browser | tool | <https://github.com/rustybird/qubes-app-split-browser> |
| s045pd/DarkNet_ChineseTrading | dashboard | <https://github.com/s045pd/DarkNet_ChineseTrading> |
| sahilchaddha/rudyjs | container | <https://github.com/sahilchaddha/rudyjs> |
| SamNet-dev/conduit-manager | web-platform | <https://github.com/SamNet-dev/conduit-manager> |
| SamNet-dev/torware | container | <https://github.com/SamNet-dev/torware> |
| samogod/tornado | web-platform | <https://github.com/samogod/tornado> |
| Samourai-Wallet/samourai-wallet-android | tool | <https://github.com/Samourai-Wallet/samourai-wallet-android> |
| samsesh/tor-in-termux | tool | <https://github.com/samsesh/tor-in-termux> |
| sandipbera35/vpndesk | web-platform | <https://github.com/sandipbera35/vpndesk> |
| sanjayadanushka712/Ghost-Night | framework | <https://github.com/sanjayadanushka712/Ghost-Night> |
| scidsg/hushline | tool | <https://github.com/scidsg/hushline> |
| scriptzteam/Tor-Bridges-Collector | tool | <https://github.com/scriptzteam/Tor-Bridges-Collector> |
| scriptzteam/Tor-Bridges-Collector-v2 | tool | <https://github.com/scriptzteam/Tor-Bridges-Collector-v2> |
| secdr/awesome-anonymity-papers | awesome-list | <https://github.com/secdr/awesome-anonymity-papers> |
| SecOps-Institute/Tor-IP-Addresses | tool | <https://github.com/SecOps-Institute/Tor-IP-Addresses> |
| seevik2580/tor-ip-changer | cli-tool | <https://github.com/seevik2580/tor-ip-changer> |
| SekouD/lyricsmaster | library | <https://github.com/SekouD/lyricsmaster> |
| serejandmyself/privacy-basics | tool | <https://github.com/serejandmyself/privacy-basics> |
| shadawck/awesome-darknet | awesome-list | <https://github.com/shadawck/awesome-darknet> |
| shadow/shadow | research-project | <https://github.com/shadow/shadow> |
| shahradelahi/docker-torproxy | container | <https://github.com/shahradelahi/docker-torproxy> |
| shahradelahi/node-tor-control | library | <https://github.com/shahradelahi/node-tor-control> |
| Shark-vil/xray_easy_install_script | research-project | <https://github.com/Shark-vil/xray_easy_install_script> |
| Sifir-io/react-native-tor | cli-tool | <https://github.com/Sifir-io/react-native-tor> |
| SimonDaNinja/youtube_rss | cli-tool | <https://github.com/SimonDaNinja/youtube_rss> |
| soxoj/counter-osint-guide-en | dashboard | <https://github.com/soxoj/counter-osint-guide-en> |
| Speek-App/Speek | tool | <https://github.com/Speek-App/Speek> |
| srixivas/PcapXray | tool | <https://github.com/srixivas/PcapXray> |
| st-mich43l/ghostnet | web-platform | <https://github.com/st-mich43l/ghostnet> |
| Startpage | tool | <https://www.startpage.com/> |
| stevenengler/socksns | tool | <https://github.com/stevenengler/socksns> |
| Stintik-123/StintikVPN | tool | <https://github.com/Stintik-123/StintikVPN> |
| storopoli/dead-man-switch | library | <https://github.com/storopoli/dead-man-switch> |
| StreisandEffect/streisand | web-platform | <https://github.com/StreisandEffect/streisand> |
| sudodevdante/enchat | cli-tool | <https://github.com/sudodevdante/enchat> |
| sumithemmadi/ghost-over-tor-on-heroku | web-platform | <https://github.com/sumithemmadi/ghost-over-tor-on-heroku> |
| suuhm/unblock-proxy.sh | tool | <https://github.com/suuhm/unblock-proxy.sh> |
| swisscows | tool | <https://swisscows.com/en> |
| syncthing.net | tool | <https://syncthing.net/> |
| systemli/ansible-role-hidden-service | web-platform | <https://github.com/systemli/ansible-role-hidden-service> |
| szorfein/dotfiles | awesome-list | <https://github.com/szorfein/dotfiles> |
| szorfein/paranoid-ninja | container | <https://github.com/szorfein/paranoid-ninja> |
| tbrand/dystopia | research-project | <https://github.com/tbrand/dystopia> |
| techchipnet/ip-changer | tool | <https://github.com/techchipnet/ip-changer> |
| TechnitiumSoftware/Mesh | tool | <https://github.com/TechnitiumSoftware/Mesh> |
| termermc/tor-reverse-proxy | tool | <https://github.com/termermc/tor-reverse-proxy> |
| testdasi/openvpn-client-aio | container | <https://github.com/testdasi/openvpn-client-aio> |
| tgeek77/compose-scripts-tor | container | <https://github.com/tgeek77/compose-scripts-tor> |
| thedmdim/rollter | container | <https://github.com/thedmdim/rollter> |
| tigthor/NSA-CIA-Blocklist | tool | <https://github.com/tigthor/NSA-CIA-Blocklist> |
| tomMoulard/make-my-server | container | <https://github.com/tomMoulard/make-my-server> |
| tor2web/Tor2web | web-platform | <https://github.com/tor2web/Tor2web> |
| toralf/torutils | tool | <https://github.com/toralf/torutils> |
| torproject/chutney | tool | <https://github.com/torproject/chutney> |
| torproject/onionbalance | web-platform | <https://github.com/torproject/onionbalance> |
| torproject/sbws | research-project | <https://github.com/torproject/sbws> |
| torproject/stem | library | <https://github.com/torproject/stem> |
| torproject/tor | tool | <https://github.com/torproject/tor> |
| torproject/tor4zh | tool | <https://github.com/torproject/tor4zh> |
| torproject/torbrowser-releases | research-project | <https://github.com/torproject/torbrowser-releases> |
| torproject/torspec | tool | <https://github.com/torproject/torspec> |
| torpyorg/torpy | web-platform | <https://github.com/torpyorg/torpy> |
| TotallyNotAHaxxer/Red-Rabbit | framework | <https://github.com/TotallyNotAHaxxer/Red-Rabbit> |
| Tribler/tribler | cli-tool | <https://github.com/Tribler/tribler> |
| Tunnelsats/tunnelsats | tool | <https://github.com/Tunnelsats/tunnelsats> |
| u1234x1234/torpool | container | <https://github.com/u1234x1234/torpool> |
| ultrafunkamsterdam/aionion | tool | <https://github.com/ultrafunkamsterdam/aionion> |
| ultrafunkamsterdam/toraio | cli-tool | <https://github.com/ultrafunkamsterdam/toraio> |
| unkaktus/onionize | directory | <https://github.com/unkaktus/onionize> |
| usableprivacy/upribox | research-project | <https://github.com/usableprivacy/upribox> |
| user234683/youtube-local | cli-tool | <https://github.com/user234683/youtube-local> |
| utopicnarwhal/flibusta-mobile | mobile-app | <https://github.com/utopicnarwhal/flibusta-mobile> |
| ValdikSS/tor-relay-scanner | tool | <https://github.com/ValdikSS/tor-relay-scanner> |
| ValtteriL/OnionFermenter | web-platform | <https://github.com/ValtteriL/OnionFermenter> |
| veracrypt.fr | tool | <https://veracrypt.fr/> |
| vincenzo-afk/NEXUS-ENGINE | directory | <https://github.com/vincenzo-afk/NEXUS-ENGINE> |
| vishnuprasadh/pricingscraper | api-service | <https://github.com/vishnuprasadh/pricingscraper> |
| vital987/vubuntu | container | <https://github.com/vital987/vubuntu> |
| wabarc/archive.is | library | <https://github.com/wabarc/archive.is> |
| WalletWasabi/WalletWasabi | web-platform | <https://github.com/WalletWasabi/WalletWasabi> |
| wallneradam/docker-tor-proxy | container | <https://github.com/wallneradam/docker-tor-proxy> |
| webfp/tor-browser-selenium | tool | <https://github.com/webfp/tor-browser-selenium> |
| Whitecat18/Mavoc-Antivirus | research-project | <https://github.com/Whitecat18/Mavoc-Antivirus> |
| Whonix/whonix-firewall | tool | <https://github.com/Whonix/whonix-firewall> |
| whos-zycher/opsec-guide | dashboard | <https://github.com/whos-zycher/opsec-guide> |
| wireadmin/wireadmin | web-platform | <https://github.com/wireadmin/wireadmin> |
| wisepythagoras/website-fingerprinting | tool | <https://github.com/wisepythagoras/website-fingerprinting> |
| WMAL/kodachios | framework | <https://github.com/WMAL/kodachios> |
| Wonderfall/dockerfiles | container | <https://github.com/Wonderfall/dockerfiles> |
| wybiral/shh | web-platform | <https://github.com/wybiral/shh> |
| XDeadHackerX/Encrypt | tool | <https://github.com/XDeadHackerX/Encrypt> |
| xjasonlyu/tun2socks | tool | <https://github.com/xjasonlyu/tun2socks> |
| yassine/soxy-driver | container | <https://github.com/yassine/soxy-driver> |
| yazgx97/auto-change-tor-ip | tool | <https://github.com/yazgx97/auto-change-tor-ip> |
| yottajunaid/Master-Darknet | dashboard | <https://github.com/yottajunaid/Master-Darknet> |
| Zaeem20/FREE_PROXIES_LIST | tool | <https://github.com/Zaeem20/FREE_PROXIES_LIST> |
| zapek/Xeres | tool | <https://github.com/zapek/Xeres> |
| zhaow-de/rotating-tor-http-proxy | container | <https://github.com/zhaow-de/rotating-tor-http-proxy> |
| ZKAW/website-cloner | tool | <https://github.com/ZKAW/website-cloner> |
| znetstar/tor-router | tool | <https://github.com/znetstar/tor-router> |
| Zopolis4/TorghostNG | tool | <https://github.com/Zopolis4/TorghostNG> |
| zotil/TorBox | tool | <https://github.com/zotil/TorBox> |
| zuazo/alpine-tor-docker | container | <https://github.com/zuazo/alpine-tor-docker> |
| zydou/arti | tool | <https://github.com/zydou/arti> |
| zzzkeil/wireguard-dnscrypt-tor-server | research-project | <https://github.com/zzzkeil/wireguard-dnscrypt-tor-server> |

### Ransomware & Threat Actor Tracking

| Name | Type | URL |
|---|---|---|
| 0u44/FunnyWare | tool | <https://github.com/0u44/FunnyWare> |
| 0u44/PythoniC | tool | <https://github.com/0u44/PythoniC> |
| 0u44/USB-Ransom | tool | <https://github.com/0u44/USB-Ransom> |
| 0x00000FF/rensenware-cut | api-service | <https://github.com/0x00000FF/rensenware-cut> |
| 0x00wolf/PATHBYTER-Hybrid-Encryption-Ransomware-with-Multiprocessing-in-Python | tool | <https://github.com/0x00wolf/PATHBYTER-Hybrid-Encryption-Ransomware-with-Multiprocessing-in-Python> |
| 0x0allenace/Email_Body_Analysis | dashboard | <https://github.com/0x0allenace/Email_Body_Analysis> |
| 0xbitx/DEDSEC_RANSOMWARE | tool | <https://github.com/0xbitx/DEDSEC_RANSOMWARE> |
| 0xbitx/DEDSEC_RANSOMWARE_BUILDER | tool | <https://github.com/0xbitx/DEDSEC_RANSOMWARE_BUILDER> |
| 0xvpr/Malicious-Software-Research | cli-tool | <https://github.com/0xvpr/Malicious-Software-Research> |
| 17tayyy/priv4te | tool | <https://github.com/17tayyy/priv4te> |
| 1d8/bstry | research-project | <https://github.com/1d8/bstry> |
| 1paton/nweaRansomware | plugin | <https://github.com/1paton/nweaRansomware> |
| 3ratic/Whippet | tool | <https://github.com/3ratic/Whippet> |
| 4zv4l/ransomware | tool | <https://github.com/4zv4l/ransomware> |
| 74lg0/PyMalwareOS | tool | <https://github.com/74lg0/PyMalwareOS> |
| 8linkz-sec/Ransomware-Bot | tool | <https://github.com/8linkz-sec/Ransomware-Bot> |
| 9aylas/S3X-B3B4S-ransomware-decryption | tool | <https://github.com/9aylas/S3X-B3B4S-ransomware-decryption> |
| a0zhar/babukv3 | tool | <https://github.com/a0zhar/babukv3> |
| a0zhar/GandCrab | tool | <https://github.com/a0zhar/GandCrab> |
| a0zhar/NotPetya | tool | <https://github.com/a0zhar/NotPetya> |
| ab-dek/Ransomware | tool | <https://github.com/ab-dek/Ransomware> |
| Ace-Krypton/Alice | research-project | <https://github.com/Ace-Krypton/Alice> |
| Ace-Krypton/Krypton-V2 | tool | <https://github.com/Ace-Krypton/Krypton-V2> |
| adrgs/nelasod-recover | tool | <https://github.com/adrgs/nelasod-recover> |
| advanced-threat-research/DarkSide-Config-Extract | research-project | <https://github.com/advanced-threat-research/DarkSide-Config-Extract> |
| AhmadMAnis/PhantomLink | cli-tool | <https://github.com/AhmadMAnis/PhantomLink> |
| AhndreWalters/Ransomware-Incident-Response-Playbook | tool | <https://github.com/AhndreWalters/Ransomware-Incident-Response-Playbook> |
| AhsanAyub/deep_static_ransomware_analysis | tool | <https://github.com/AhsanAyub/deep_static_ransomware_analysis> |
| AhsanAyub/irp-driven-ransomware-analysis | tool | <https://github.com/AhsanAyub/irp-driven-ransomware-analysis> |
| AiGptCode/Ai-Security-URL | web-platform | <https://github.com/AiGptCode/Ai-Security-URL> |
| AiGptCode/AiGPT-WordPress-Exploitation-Framework | plugin | <https://github.com/AiGptCode/AiGPT-WordPress-Exploitation-Framework> |
| AiGptCode/Analysis-TCP-UDP | tool | <https://github.com/AiGptCode/Analysis-TCP-UDP> |
| AiGptCode/ANYDESK-BACKDOOR | cli-tool | <https://github.com/AiGptCode/ANYDESK-BACKDOOR> |
| AiGptCode/iphoneprofile | research-project | <https://github.com/AiGptCode/iphoneprofile> |
| AiGptCode/RAR-NextgenerationAI-expliot | cli-tool | <https://github.com/AiGptCode/RAR-NextgenerationAI-expliot> |
| AiGptCode/Xz_vulnerability_crossplatform | web-platform | <https://github.com/AiGptCode/Xz_vulnerability_crossplatform> |
| AIwolfie/ransom_bae | dashboard | <https://github.com/AIwolfie/ransom_bae> |
| ajayrandhawa/Cryptolocker | tool | <https://github.com/ajayrandhawa/Cryptolocker> |
| akalankauk/Keep-It-Secure-File-Encryption | tool | <https://github.com/akalankauk/Keep-It-Secure-File-Encryption> |
| akari-sora/synology-nas-cli | cli-tool | <https://github.com/akari-sora/synology-nas-cli> |
| aktechnohacker/Ransomware-samples | tool | <https://github.com/aktechnohacker/Ransomware-samples> |
| alb1183/CatLocker | tool | <https://github.com/alb1183/CatLocker> |
| albertzsigovits/malware-notes | research-project | <https://github.com/albertzsigovits/malware-notes> |
| alestanalves/video-malware | research-project | <https://github.com/alestanalves/video-malware> |
| alexander695/Felix | tool | <https://github.com/alexander695/Felix> |
| alfredang/cybersecuritysimulator | web-platform | <https://github.com/alfredang/cybersecuritysimulator> |
| AlphaDelta/DUMB | tool | <https://github.com/AlphaDelta/DUMB> |
| Altify-Developing/GitHubViewBot | tool | <https://github.com/Altify-Developing/GitHubViewBot> |
| Altify-Developing/stats | tool | <https://github.com/Altify-Developing/stats> |
| alvarorichard/ArmaSec | tool | <https://github.com/alvarorichard/ArmaSec> |
| alvin-tosh/Kenyatta-Ransomware | research-project | <https://github.com/alvin-tosh/Kenyatta-Ransomware> |
| alvin-tosh/Malware-Exhibit | research-project | <https://github.com/alvin-tosh/Malware-Exhibit> |
| amaitou/Xorcry | directory | <https://github.com/amaitou/Xorcry> |
| Amo0p/LockBitRansomWare | research-project | <https://github.com/Amo0p/LockBitRansomWare> |
| AnandaRauf/Ranak-Pinak-Ransomware-Jinak-Penetration-Testing-Akumulatif | tool | <https://github.com/AnandaRauf/Ranak-Pinak-Ransomware-Jinak-Penetration-Testing-Akumulatif-> |
| AnandBinuArjun/RANSOMWATCH | dashboard | <https://github.com/AnandBinuArjun/RANSOMWATCH> |
| andpalmier/goransom | research-project | <https://github.com/andpalmier/goransom> |
| aparisot84/Sandbox-Ransomware-Analysis-Dataset | dataset | <https://github.com/aparisot84/Sandbox-Ransomware-Analysis-Dataset> |
| APT Groups and Operations | tool | <https://docs.google.com/spreadsheets/u/0/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/pubhtml?pli=1#> |
| armscyber/communityedition | tool | <https://github.com/armscyber/communityedition> |
| Arnaleeo/LockBit-RansomWare | research-project | <https://github.com/Arnaleeo/LockBit-RansomWare> |
| ASm0ty/Babuk-RansomWare---October-2023 | research-project | <https://github.com/ASm0ty/Babuk-RansomWare---October-2023> |
| astafofo/Ransomware-Database | dataset | <https://github.com/astafofo/Ransomware-Database> |
| atapour/ransomware-classification | tool | <https://github.com/atapour/ransomware-classification> |
| AtharDar/smart-decoy-ransomware-defense | tool | <https://github.com/AtharDar/smart-decoy-ransomware-defense> |
| avast/decryptor-keys | tool | <https://github.com/avast/decryptor-keys> |
| Axion-Security/Malaria | research-project | <https://github.com/Axion-Security/Malaria> |
| aymenbrahimdjelloul/MalwareScan | web-platform | <https://github.com/aymenbrahimdjelloul/MalwareScan> |
| AyoobAli/ransomwatch-cli | cli-tool | <https://github.com/AyoobAli/ransomwatch-cli> |
| bamless/cryptor | web-platform | <https://github.com/bamless/cryptor> |
| baum1810/Ransomware-POC | tool | <https://github.com/baum1810/Ransomware-POC> |
| bbbbbrie/awesome-ransomware | awesome-list | <https://github.com/bbbbbrie/awesome-ransomware> |
| BenjaminGuzman/fsociety-ransomware | tool | <https://github.com/BenjaminGuzman/fsociety-ransomware> |
| bhassani/WannacryDecompiled | tool | <https://github.com/bhassani/WannacryDecompiled> |
| bhusalb/gt-ransomware-simulation | research-project | <https://github.com/bhusalb/gt-ransomware-simulation> |
| Bi.Zone | tool | <https://gti.bi.zone/> |
| bierschi/butterfly | tool | <https://github.com/bierschi/butterfly> |
| bing0o/simple_ransomware | tool | <https://github.com/bing0o/simple_ransomware> |
| Bitwise-01/Thor | tool | <https://github.com/Bitwise-01/Thor> |
| biyivi/ransomware | tool | <https://github.com/biyivi/ransomware> |
| bl4de/research | research-project | <https://github.com/bl4de/research> |
| Black-Hell-Team/TheBhTiNjector | plugin | <https://github.com/Black-Hell-Team/TheBhTiNjector> |
| BlasphemiumThe3rd/Ransomware-Decrypt | tool | <https://github.com/BlasphemiumThe3rd/Ransomware-Decrypt> |
| BlazeInferno64/Lcrypto | library | <https://github.com/BlazeInferno64/Lcrypto> |
| BRANDEFENSE/IoC | research-project | <https://github.com/BRANDEFENSE/IoC> |
| BRANDEFENSE/threat-actor-dataset | dataset | <https://github.com/BRANDEFENSE/threat-actor-dataset> |
| BRANDEFENSE/Threat-Intelligence-Researches | research-project | <https://github.com/BRANDEFENSE/Threat-Intelligence-Researches> |
| BreachHQ | tool | <https://breach-hq.com/threat-actors> |
| bstnbuck/ItsSoEasy | research-project | <https://github.com/bstnbuck/ItsSoEasy> |
| BushidoUK/Ransomware-Tool-Matrix | tool | <https://github.com/BushidoUK/Ransomware-Tool-Matrix> |
| buter-chkalova/RvbbitSafe | research-project | <https://github.com/buter-chkalova/RvbbitSafe> |
| byt3n33dl3/ExpertBosun | directory | <https://github.com/byt3n33dl3/ExpertBosun> |
| calinux-py/Flipper | cli-tool | <https://github.com/calinux-py/Flipper> |
| calinux-py/PowerShell | cli-tool | <https://github.com/calinux-py/PowerShell> |
| capetron/incident-response-plan-template | tool | <https://github.com/capetron/incident-response-plan-template> |
| caronero/Z-ransom | tool | <https://github.com/caronero/Z-ransom> |
| Casualtek/Ransomchats | tool | <https://github.com/Casualtek/Ransomchats> |
| cdong1012/GoCryptor | tool | <https://github.com/cdong1012/GoCryptor> |
| Check Point Live Cyber Threat Map | tool | <https://threatmap.checkpoint.com/> |
| Chibraax/Ransomware | dashboard | <https://github.com/Chibraax/Ransomware> |
| Chibraax/Ransomware--SeriousBuf00n | dashboard | <https://github.com/Chibraax/Ransomware--SeriousBuf00n> |
| CLXZ4353/lockbit-rescue-v2 | web-platform | <https://github.com/CLXZ4353/lockbit-rescue-v2> |
| codassassin/very-basic-ransomware | research-project | <https://github.com/codassassin/very-basic-ransomware> |
| codesiddhant/Jasmin-Ransomware | framework | <https://github.com/codesiddhant/Jasmin-Ransomware> |
| codingo/Ransomware-Json-Dataset | dataset | <https://github.com/codingo/Ransomware-Json-Dataset> |
| Concinnity-Risks/RansomCoinPublic | tool | <https://github.com/Concinnity-Risks/RansomCoinPublic> |
| crocodyli/ThreatActors-TTPs | tool | <https://github.com/crocodyli/ThreatActors-TTPs> |
| crvvdev/cpp-ransomware | library | <https://github.com/crvvdev/cpp-ransomware> |
| cryptwareapps/Malware-Database | web-platform | <https://github.com/cryptwareapps/Malware-Database> |
| curated-intel/MOVEit-Transfer | tool | <https://github.com/curated-intel/MOVEit-Transfer> |
| curufti/Conti-RW | research-project | <https://github.com/curufti/Conti-RW> |
| CYB3RMX/Qu1cksc0pe | mobile-app | <https://github.com/CYB3RMX/Qu1cksc0pe> |
| cyberexpertsng/Nigeria-Cyber-Incidents | tool | <https://github.com/cyberexpertsng/Nigeria-Cyber-Incidents> |
| CyberSaR-KAUST/Ransomware-Malware-Family-Detection-Dataset | dataset | <https://github.com/CyberSaR-KAUST/Ransomware-Malware-Family-Detection-Dataset> |
| Cybersight-Security/Malware-Samples | research-project | <https://github.com/Cybersight-Security/Malware-Samples> |
| Cyreslab-AI/ransomware-live-mcp-server | tool | <https://github.com/Cyreslab-AI/ransomware-live-mcp-server> |
| d-Raco/android-malware-source-code-samples | dataset | <https://github.com/d-Raco/android-malware-source-code-samples> |
| D1se0/RansomwareLocker_Education | tool | <https://github.com/D1se0/RansomwareLocker_Education> |
| d33pster/ransomware | tool | <https://github.com/d33pster/ransomware> |
| d4rk-d4nph3/Ransomware-Reports | research-project | <https://github.com/d4rk-d4nph3/Ransomware-Reports> |
| Da2dalus/The-MALWARE-Repo | tool | <https://github.com/Da2dalus/The-MALWARE-Repo> |
| dalthunter/intel-reports | awesome-list | <https://github.com/dalthunter/intel-reports> |
| DaniAffCH/Ransomware | tool | <https://github.com/DaniAffCH/Ransomware> |
| Dark Web Informer | tool | <https://darkwebinformer.com/threat-actor-database/> |
| DarxiSR/CRYLINE-v3.0 | research-project | <https://github.com/DarxiSR/CRYLINE-v3.0> |
| DarxiSR/CRYLINE-v5.0 | research-project | <https://github.com/DarxiSR/CRYLINE-v5.0> |
| deadPix3l/CryptSky | tool | <https://github.com/deadPix3l/CryptSky> |
| DefWolf/Lithium.PHP-ransomware | tool | <https://github.com/DefWolf/Lithium.PHP-ransomware> |
| DEMON1A/ransomware-sample | tool | <https://github.com/DEMON1A/ransomware-sample> |
| depalmar/AI-Powered-Ransomware-Intelligence-Agent | api-service | <https://github.com/depalmar/AI-Powered-Ransomware-Intelligence-Agent> |
| DestroyerDarkNess/Shareware-Ransomware | tool | <https://github.com/DestroyerDarkNess/Shareware-Ransomware> |
| Dethada/Ransomware | tool | <https://github.com/Dethada/Ransomware> |
| DharkonSK/A2-Cryptor-Ransomware | tool | <https://github.com/DharkonSK/A2-Cryptor-Ransomware> |
| DharkonSK/ADZP_20_Complex_Virus | tool | <https://github.com/DharkonSK/ADZP_20_Complex_Virus> |
| DharkonSK/FMLN_Ransomware | tool | <https://github.com/DharkonSK/FMLN_Ransomware> |
| didipostman/MyVirus | tool | <https://github.com/didipostman/MyVirus> |
| Discordmodsbers/inferno | tool | <https://github.com/Discordmodsbers/inferno> |
| dmdhrumilmistry/pyhtools | api-service | <https://github.com/dmdhrumilmistry/pyhtools> |
| drapl0n/dransomware | tool | <https://github.com/drapl0n/dransomware> |
| DRCRecoveryData/WAV-Repair-Tool | tool | <https://github.com/DRCRecoveryData/WAV-Repair-Tool> |
| DrMint/Anti-Ransomware | tool | <https://github.com/DrMint/Anti-Ransomware> |
| droidefense/engine | framework | <https://github.com/droidefense/engine> |
| DTonomy-Inc/Ransomware | awesome-list | <https://github.com/DTonomy-Inc/Ransomware> |
| dubniczky/Ransomware | tool | <https://github.com/dubniczky/Ransomware> |
| DyoneZ/LockBit-RansomWare | research-project | <https://github.com/DyoneZ/LockBit-RansomWare> |
| echo-devim/NoCrypt | plugin | <https://github.com/echo-devim/NoCrypt> |
| eddiechu/Encrypt-Delete-Test | tool | <https://github.com/eddiechu/Encrypt-Delete-Test> |
| eddiechu/Ransomware-meets-loop | tool | <https://github.com/eddiechu/Ransomware-meets-loop> |
| EddyErkel/Powershell_updateHostsFile | cli-tool | <https://github.com/EddyErkel/Powershell_updateHostsFile> |
| EdinsonRequena/ransomware-with-python-3 | tool | <https://github.com/EdinsonRequena/ransomware-with-python-3> |
| ejserna/Ransomware | tool | <https://github.com/ejserna/Ransomware> |
| Elijahhx/Dead1ock-h4ck | research-project | <https://github.com/Elijahhx/Dead1ock-h4ck> |
| enginestein/Virus-Collection | tool | <https://github.com/enginestein/Virus-Collection> |
| Err0r-ICA/Ransomware | tool | <https://github.com/Err0r-ICA/Ransomware> |
| esfelurm/android-ransomware | tool | <https://github.com/esfelurm/android-ransomware> |
| eshlomo1/Ransomware-NOTE | plugin | <https://github.com/eshlomo1/Ransomware-NOTE> |
| ETDA | tool | <https://apt.etda.or.th/cgi-bin/listgroups.cgi> |
| EternalBlue445/DontWannaCry | tool | <https://github.com/EternalBlue445/DontWannaCry> |
| evilstdio/ransomware | tool | <https://github.com/evilstdio/ransomware> |
| exploreourbrain/MicinWare-PHP-Ransomware | tool | <https://github.com/exploreourbrain/MicinWare-PHP-Ransomware> |
| f0wl/configwalker | tool | <https://github.com/f0wl/configwalker> |
| f0wl/REconfig-linux | tool | <https://github.com/f0wl/REconfig-linux> |
| f6-dfir/Ransomware | tool | <https://github.com/f6-dfir/Ransomware> |
| fabrimagic72/malware-samples | tool | <https://github.com/fabrimagic72/malware-samples> |
| Fadouse/rustransomware | framework | <https://github.com/Fadouse/rustransomware> |
| farshinekev-rgb/owly | dashboard | <https://github.com/farshinekev-rgb/owly> |
| fen1l/BWare | tool | <https://github.com/fen1l/BWare> |
| FirstBlood12/NotPetyaOpenSSL | tool | <https://github.com/FirstBlood12/NotPetyaOpenSSL> |
| FirstBlood12/RedPetyaOpenSSL | tool | <https://github.com/FirstBlood12/RedPetyaOpenSSL> |
| Flooding-against-Ransomware/ranflood | tool | <https://github.com/Flooding-against-Ransomware/ranflood> |
| FogSecurity/yes3-scanner | tool | <https://github.com/FogSecurity/yes3-scanner> |
| ForbiddenProgrammer/conti-pentester-guide-leak | dashboard | <https://github.com/ForbiddenProgrammer/conti-pentester-guide-leak> |
| fportantier/mosnar | cli-tool | <https://github.com/fportantier/mosnar> |
| FrancescoDiSalesGithub/commodore64-ransomware | tool | <https://github.com/FrancescoDiSalesGithub/commodore64-ransomware> |
| frknaykc/Dragon-ThreatResearchHQ | research-project | <https://github.com/frknaykc/Dragon-ThreatResearchHQ> |
| FuckingSilly/RatonCrypter | tool | <https://github.com/FuckingSilly/RatonCrypter> |
| Fytex/simple-ransomware | tool | <https://github.com/Fytex/simple-ransomware> |
| Ganatra-Ruchir/ransomware-canary-detector | tool | <https://github.com/Ganatra-Ruchir/ransomware-canary-detector> |
| gau820827/Ransome-killer | tool | <https://github.com/gau820827/Ransome-killer> |
| gemartin99/Stockholm | tool | <https://github.com/gemartin99/Stockholm> |
| gharty03/Conti-Ransomware | research-project | <https://github.com/gharty03/Conti-Ransomware> |
| Gheris-579/RANSOMEWARE | tool | <https://github.com/Gheris-579/RANSOMEWARE> |
| Ghost-crypto-exe/2024-Malware-Repository | research-project | <https://github.com/Ghost-crypto-exe/2024-Malware-Repository> |
| Ghost-crypto-exe/HCRYPT-Ransomware | tool | <https://github.com/Ghost-crypto-exe/HCRYPT-Ransomware> |
| GiacomoFerro/python3-ransomware | tool | <https://github.com/GiacomoFerro/python3-ransomware> |
| GlebYoutuber/WormLockerRansomwarebyCYBERSOLDIER | tool | <https://github.com/GlebYoutuber/WormLockerRansomwarebyCYBERSOLDIER> |
| GlgApr/Malware-Analyzer | tool | <https://github.com/GlgApr/Malware-Analyzer> |
| GoofyAhhDev/Ransomware-Sample-Python | tool | <https://github.com/GoofyAhhDev/Ransomware-Sample-Python> |
| gr33ntii/malware-collection | tool | <https://github.com/gr33ntii/malware-collection> |
| grepstrength/RansomWhere | research-project | <https://github.com/grepstrength/RansomWhere> |
| gustavohenrique/ransomware | tool | <https://github.com/gustavohenrique/ransomware> |
| h3xduck/Umbra | plugin | <https://github.com/h3xduck/Umbra> |
| habibkaratas/sorry-ransomware-analysis | tool | <https://github.com/habibkaratas/sorry-ransomware-analysis> |
| hackthedev/teardrop | tool | <https://github.com/hackthedev/teardrop> |
| HalilDeniz/BackDoorSim | cli-tool | <https://github.com/HalilDeniz/BackDoorSim> |
| HalilDeniz/RansomwareSim | tool | <https://github.com/HalilDeniz/RansomwareSim> |
| Haroun-Haeder/MalwareDatabase | dataset | <https://github.com/Haroun-Haeder/MalwareDatabase> |
| hasherezade/petya_green | tool | <https://github.com/hasherezade/petya_green> |
| hasherezade/petya_key | tool | <https://github.com/hasherezade/petya_key> |
| hasherezade/petya_recovery | tool | <https://github.com/hasherezade/petya_recovery> |
| hauni97/Blockchain-enabled-Adversarial-Threat-Intelligence-Sharing-for-Robust-Ransomware-Detection-air-gaps | tool | <https://github.com/hauni97/Blockchain-enabled-Adversarial-Threat-Intelligence-Sharing-for-Robust-Ransomware-Detection-air-gaps> |
| haxdoggy/ransomware-groups | tool | <https://github.com/haxdoggy/ransomware-groups> |
| hazcod/ransomwhere | tool | <https://github.com/hazcod/ransomwhere> |
| hectorm/hblock | cli-tool | <https://github.com/hectorm/hblock> |
| hectorm/hblock-resolver | container | <https://github.com/hectorm/hblock-resolver> |
| HeightCoder/Chaos-Ransomware-Builder | tool | <https://github.com/HeightCoder/Chaos-Ransomware-Builder> |
| HeightCoder/Hakuna-Matata-Ransomware-Source | tool | <https://github.com/HeightCoder/Hakuna-Matata-Ransomware-Source> |
| HeightCoder/Yashma-Ransomware | tool | <https://github.com/HeightCoder/Yashma-Ransomware> |
| HeightCoder/ZagreuS-Ransomware-Builder | tool | <https://github.com/HeightCoder/ZagreuS-Ransomware-Builder> |
| Heisenberg7876/Research-Project-The-Hidden-Side-of-Cybercrime-A-Study-of-Dark-Web-Activities-and-Threats | research-project | <https://github.com/Heisenberg7876/Research-Project-The-Hidden-Side-of-Cybercrime-A-Study-of-Dark-Web-Activities-and-Threats> |
| Hex1629/Ac0ddRansom | tool | <https://github.com/Hex1629/Ac0ddRansom> |
| Hex1629/CRYPTHEX_RANSOMWARE | tool | <https://github.com/Hex1629/CRYPTHEX_RANSOMWARE> |
| Hildaboo/BabukRansomware | tool | <https://github.com/Hildaboo/BabukRansomware> |
| Hildaboo/BabukRansomwareSourceCode | tool | <https://github.com/Hildaboo/BabukRansomwareSourceCode> |
| Hildaboo/NotPetyaFileEncryptor | tool | <https://github.com/Hildaboo/NotPetyaFileEncryptor> |
| Hildaboo/Rensenware | tool | <https://github.com/Hildaboo/Rensenware> |
| Hildaboo/Unidentified081Server | tool | <https://github.com/Hildaboo/Unidentified081Server> |
| Hildaboo/WannaCryServerEmulator | tool | <https://github.com/Hildaboo/WannaCryServerEmulator> |
| Hildaboo/xorist | tool | <https://github.com/Hildaboo/xorist> |
| hjunker/ProcessBouncer | cli-tool | <https://github.com/hjunker/ProcessBouncer> |
| hrshadhin/hosts | tool | <https://github.com/hrshadhin/hosts> |
| HugoLB0/Ransom0 | dataset | <https://github.com/HugoLB0/Ransom0> |
| HUGOW04/TuWare | tool | <https://github.com/HUGOW04/TuWare> |
| ickerwx/phishing-botnets-ransomware | tool | <https://github.com/ickerwx/phishing-botnets-ransomware> |
| Idov31/rustomware | research-project | <https://github.com/Idov31/rustomware> |
| iltosec/python_ransomware | tool | <https://github.com/iltosec/python_ransomware> |
| InferiorAK/RansoInferor | tool | <https://github.com/InferiorAK/RansoInferor> |
| ion-storm/emotet-malware-killer | tool | <https://github.com/ion-storm/emotet-malware-killer> |
| ionsec/RansomProtect | tool | <https://github.com/ionsec/RansomProtect> |
| iss4cf0ng/OpenPetya | tool | <https://github.com/iss4cf0ng/OpenPetya> |
| Itay-Dum/keylogger_ransomware | tool | <https://github.com/Itay-Dum/keylogger_ransomware> |
| Itz-Agasta/nerrf | container | <https://github.com/Itz-Agasta/nerrf> |
| ivan-sincek/php-ransomware | directory | <https://github.com/ivan-sincek/php-ransomware> |
| j-moriarti/pDNSf-Hosts-collection | tool | <https://github.com/j-moriarti/pDNSf-Hosts-collection> |
| J4NN0/wannacry-ish | tool | <https://github.com/J4NN0/wannacry-ish> |
| j91321/conti-manuals-analysis | tool | <https://github.com/j91321/conti-manuals-analysis> |
| JackImpact1023/PetyaRansomware-CSharpEdition | tool | <https://github.com/JackImpact1023/PetyaRansomware-CSharpEdition> |
| Jam0k/Cyber-Threat-Intelligence-API | api-service | <https://github.com/Jam0k/Cyber-Threat-Intelligence-API> |
| jamestiotio/NoMoreRansom | tool | <https://github.com/jamestiotio/NoMoreRansom> |
| jaywyawhare/Ransomware | web-platform | <https://github.com/jaywyawhare/Ransomware> |
| jeeberrr/kingsnake | tool | <https://github.com/jeeberrr/kingsnake> |
| jenkinsmichpa/coconut_crab | tool | <https://github.com/jenkinsmichpa/coconut_crab> |
| jflyup/goMS17-010 | tool | <https://github.com/jflyup/goMS17-010> |
| jhanZDj/LockBit | research-project | <https://github.com/jhanZDj/LockBit> |
| jimmy-ly00/Ransomware-PoC | tool | <https://github.com/jimmy-ly00/Ransomware-PoC> |
| JLChnToZ/RansomHoneyPot | research-project | <https://github.com/JLChnToZ/RansomHoneyPot> |
| JMousqueton/Badware | cli-tool | <https://github.com/JMousqueton/Badware> |
| JMousqueton/CTI-MSTeams-Bot | dataset | <https://github.com/JMousqueton/CTI-MSTeams-Bot> |
| JMousqueton/RansomSim | dashboard | <https://github.com/JMousqueton/RansomSim> |
| JMousqueton/ransomware.live | tool | <https://github.com/JMousqueton/ransomware.live> |
| Joao-b4/mart-malware-dart | tool | <https://github.com/Joao-b4/mart-malware-dart> |
| joeavanzato/impact | tool | <https://github.com/joeavanzato/impact> |
| JoelGMSec/PSRansom | cli-tool | <https://github.com/JoelGMSec/PSRansom> |
| jordanricky1604-ship-it/malware-families-catalog | directory | <https://github.com/jordanricky1604-ship-it/malware-families-catalog> |
| julupu/jamsomware | tool | <https://github.com/julupu/jamsomware> |
| justakazh/LazyWare | tool | <https://github.com/justakazh/LazyWare> |
| JustThinkingHard/ebpf-antiransomware-rust | tool | <https://github.com/JustThinkingHard/ebpf-antiransomware-rust> |
| Jx00001/SukiPyRansomware | tool | <https://github.com/Jx00001/SukiPyRansomware> |
| k1shlabs/wazuh-fim-adh | research-project | <https://github.com/k1shlabs/wazuh-fim-adh> |
| kaixinol/Ransomware-Maker.cs | research-project | <https://github.com/kaixinol/Ransomware-Maker.cs> |
| kakashi-kx/apt-emulation-platform | web-platform | <https://github.com/kakashi-kx/apt-emulation-platform> |
| KanakSasak/procSniper | framework | <https://github.com/KanakSasak/procSniper> |
| Kelvin0428/Ransomware-Group-TI | tool | <https://github.com/Kelvin0428/Ransomware-Group-TI> |
| kennysarnoski-jarvis/aris-sentinel | cli-tool | <https://github.com/kennysarnoski-jarvis/aris-sentinel> |
| kh4sh3i/Ransomware | web-platform | <https://github.com/kh4sh3i/Ransomware> |
| kh4sh3i/Ransomware-Samples | tool | <https://github.com/kh4sh3i/Ransomware-Samples> |
| khamazz/LockBit-RansomWare | research-project | <https://github.com/khamazz/LockBit-RansomWare> |
| Ki4nb/VSphereRansomwareRecovery | tool | <https://github.com/Ki4nb/VSphereRansomwareRecovery> |
| kimd155/GhostLock | api-service | <https://github.com/kimd155/GhostLock> |
| kinomakino/ransomware_file_extensions | plugin | <https://github.com/kinomakino/ransomware_file_extensions> |
| KNOWLEDGENOW | tool | <https://know.netenrich.com/content/track/threat-actor> |
| Krn0s/CrypToxin-A-Discord-advanced-ransomware | tool | <https://github.com/Krn0s/CrypToxin-A-Discord-advanced-ransomware> |
| kuzeyardabulut/RustyLock | tool | <https://github.com/kuzeyardabulut/RustyLock> |
| Largo-m/Ransomware-Analyzer | web-platform | <https://github.com/Largo-m/Ransomware-Analyzer> |
| lawndoc/RanSim | cli-tool | <https://github.com/lawndoc/RanSim> |
| lazarusholic | tool | <https://lazarus.day/actors/> |
| leeberg/CashCatRansomwareSimulator | plugin | <https://github.com/leeberg/CashCatRansomwareSimulator> |
| leJBP/adaptative-ransomware | tool | <https://github.com/leJBP/adaptative-ransomware> |
| leohidalgo/little-snitch---rule-groups | tool | <https://github.com/leohidalgo/little-snitch---rule-groups> |
| liesware/meliora | tool | <https://github.com/liesware/meliora> |
| litemars/hARMful | framework | <https://github.com/litemars/hARMful> |
| lithnet/access-manager | directory | <https://github.com/lithnet/access-manager> |
| LittleAtariXE/Draconus | cli-tool | <https://github.com/LittleAtariXE/Draconus> |
| LJ9859/Malware-Database | dataset | <https://github.com/LJ9859/Malware-Database> |
| lllong1377/c3rb3r-never-rebooted-still-no-key | tool | <https://github.com/lllong1377/c3rb3r-never-rebooted-still-no-key> |
| lopes/cordyceps | tool | <https://github.com/lopes/cordyceps> |
| Lucas310302/XMRansom | tool | <https://github.com/Lucas310302/XMRansom> |
| m1-llie/Remembrall | research-project | <https://github.com/m1-llie/Remembrall> |
| M3str3/Ransomware | tool | <https://github.com/M3str3/Ransomware> |
| M507/Proof-of-Concept-CSharp-Ransomware | tool | <https://github.com/M507/Proof-of-Concept-CSharp-Ransomware> |
| machine1337/fudransome | tool | <https://github.com/machine1337/fudransome> |
| MalDev101/WoundedGryphon | cli-tool | <https://github.com/MalDev101/WoundedGryphon> |
| Malpedia | tool | <https://malpedia.caad.fkie.fraunhofer.de/actors> |
| malvuln/RansomDLLs | research-project | <https://github.com/malvuln/RansomDLLs> |
| Malwareman007/Hacking_Tools | tool | <https://github.com/Malwareman007/Hacking_Tools> |
| Malwareman007/Ransomware | tool | <https://github.com/Malwareman007/Ransomware> |
| malwarepad/toy-ransomware | api-service | <https://github.com/malwarepad/toy-ransomware> |
| MalwareSamples/Linux-Malware-Samples | research-project | <https://github.com/MalwareSamples/Linux-Malware-Samples> |
| manigohan/shoujocrypt | plugin | <https://github.com/manigohan/shoujocrypt> |
| MaorSabag/SafeCrypt | tool | <https://github.com/MaorSabag/SafeCrypt> |
| maravento/blackweb | tool | <https://github.com/maravento/blackweb> |
| marcopandolfo/RansomwareJS | tool | <https://github.com/marcopandolfo/RansomwareJS> |
| marcus9467/rubrik | api-service | <https://github.com/marcus9467/rubrik> |
| marichu-kt/SafeRansomwareLab | research-project | <https://github.com/marichu-kt/SafeRansomwareLab> |
| MarkTauber/batch-somware | tool | <https://github.com/MarkTauber/batch-somware> |
| marmos91/ransomware | tool | <https://github.com/marmos91/ransomware> |
| mathio3/Ro3b-HTTP-botnet | cli-tool | <https://github.com/mathio3/Ro3b-HTTP-botnet> |
| mattjang96/YARA | research-project | <https://github.com/mattjang96/YARA> |
| mauri870/ransomware | research-project | <https://github.com/mauri870/ransomware> |
| mauricelambert/RansomWare | tool | <https://github.com/mauricelambert/RansomWare> |
| mazen160/shennina | tool | <https://github.com/mazen160/shennina> |
| MBAHABYK/RANSOMEWARE | tool | <https://github.com/MBAHABYK/RANSOMEWARE> |
| mdshoaibuddinchanda/ransomware-detection-cnn2D | dashboard | <https://github.com/mdshoaibuddinchanda/ransomware-detection-cnn2D> |
| MechaDragonX/Fafnir-CPP | research-project | <https://github.com/MechaDragonX/Fafnir-CPP> |
| MechaDragonX/Fafnir.NET | tool | <https://github.com/MechaDragonX/Fafnir.NET> |
| michelep/WannaCryNetScanner | tool | <https://github.com/michelep/WannaCryNetScanner> |
| mihneamanolache/Simple-Python-Ransomware | tool | <https://github.com/mihneamanolache/Simple-Python-Ransomware> |
| MinegamesAdministrationTool-zz/MineHackingTools | tool | <https://github.com/MinegamesAdministrationTool-zz/MineHackingTools> |
| MinervaLabsResearch/Vaccinator | research-project | <https://github.com/MinervaLabsResearch/Vaccinator> |
| MISP Galaxy | tool | <https://www.misp-galaxy.org/360net/> |
| MisquaLX/LockBit-RansomWare | research-project | <https://github.com/MisquaLX/LockBit-RansomWare> |
| mitchellkrogza/Badd-Boyz-Bitcoin-Scammers | tool | <https://github.com/mitchellkrogza/Badd-Boyz-Bitcoin-Scammers> |
| mitchellkrogza/Badd-Boyz-Hosts | cli-tool | <https://github.com/mitchellkrogza/Badd-Boyz-Hosts> |
| mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites | cli-tool | <https://github.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites> |
| monsifhmouri/Windows-System-Annihilator | research-project | <https://github.com/monsifhmouri/Windows-System-Annihilator> |
| MottaSec/akira-ransomware-reverse | research-project | <https://github.com/MottaSec/akira-ransomware-reverse> |
| mstfknn/malware-sample-library | library | <https://github.com/mstfknn/malware-sample-library> |
| mstfknn/ransomware-decryptors | research-project | <https://github.com/mstfknn/ransomware-decryptors> |
| mthcht/awesome-lists | awesome-list | <https://github.com/mthcht/awesome-lists> |
| muchdogesec/ransomwarekb | tool | <https://github.com/muchdogesec/ransomwarekb> |
| n3mu3lw/Zamok | tool | <https://github.com/n3mu3lw/Zamok> |
| nacheteam/charla-ransomware | tool | <https://github.com/nacheteam/charla-ransomware> |
| natekali/Pazuzu-Locker | tool | <https://github.com/natekali/Pazuzu-Locker> |
| nathanzilgo/Python-Ransomware | tool | <https://github.com/nathanzilgo/Python-Ransomware> |
| nbs32k/Petya2 | tool | <https://github.com/nbs32k/Petya2> |
| ncorbuk/Python-Ransomware | tool | <https://github.com/ncorbuk/Python-Ransomware> |
| neilboyt/Babuk-RansomWare-CRACKED | research-project | <https://github.com/neilboyt/Babuk-RansomWare-CRACKED> |
| nirizr/vss-ransom-restore | web-platform | <https://github.com/nirizr/vss-ransom-restore> |
| northsia/M-Rans | desktop-app | <https://github.com/northsia/M-Rans> |
| NotoriousRebel/Hall-of-Ransom | tool | <https://github.com/NotoriousRebel/Hall-of-Ransom> |
| NuclearPhoenixx/ransom-prevention | research-project | <https://github.com/NuclearPhoenixx/ransom-prevention> |
| NullArray/Cypher | research-project | <https://github.com/NullArray/Cypher> |
| nullbyt3zx01/KingLocker | tool | <https://github.com/nullbyt3zx01/KingLocker> |
| NYAN-x-CAT/Lime-RAT | research-project | <https://github.com/NYAN-x-CAT/Lime-RAT> |
| oknyshuk/nakitai | web-platform | <https://github.com/oknyshuk/nakitai> |
| OPENHUNTING.IO | library | <https://openhunting.io/threat-library> |
| Ort0x36/Dimorf | tool | <https://github.com/Ort0x36/Dimorf> |
| OverTheNet/---_SAMPLE_MALWARE | tool | <https://github.com/OverTheNet/---_SAMPLE_MALWARE> |
| Ovusi/Pysces_Ransomware | tool | <https://github.com/Ovusi/Pysces_Ransomware> |
| PanagiotisDrakatos/JavaRansomware | tool | <https://github.com/PanagiotisDrakatos/JavaRansomware> |
| pangeran-droid/android-ransomware-simulation | tool | <https://github.com/pangeran-droid/android-ransomware-simulation> |
| paranormalactivity22/Malware-DB | dataset | <https://github.com/paranormalactivity22/Malware-DB> |
| parzibyte/ransomware-linux-gpg | tool | <https://github.com/parzibyte/ransomware-linux-gpg> |
| pcmarcon/malduino-payload-samples | cli-tool | <https://github.com/pcmarcon/malduino-payload-samples> |
| PeterDaveHello/threat-hostlist | tool | <https://github.com/PeterDaveHello/threat-hostlist> |
| phantom0004/KRYPT0S-Ransomware_POC | research-project | <https://github.com/phantom0004/KRYPT0S-Ransomware_POC> |
| pierky/blocklistsaggregator | tool | <https://github.com/pierky/blocklistsaggregator> |
| Pranith-Jain/dfir-threat-intel-platform | web-platform | <https://github.com/Pranith-Jain/dfir-threat-intel-platform> |
| privtools/ransomposts | tool | <https://github.com/privtools/ransomposts> |
| prodaft/malware-ioc | research-project | <https://github.com/prodaft/malware-ioc> |
| Projects-Developer/Ransomware-Detection-System-using-Machine-Learning | tool | <https://github.com/Projects-Developer/Ransomware-Detection-System-using-Machine-Learning> |
| pudurvenu/AI-NextGen | framework | <https://github.com/pudurvenu/AI-NextGen> |
| pushprajthakre/malwareCTI | tool | <https://github.com/pushprajthakre/malwareCTI> |
| PyMarcus/Cryptonita | tool | <https://github.com/PyMarcus/Cryptonita> |
| PyMarcus/daemonium | api-service | <https://github.com/PyMarcus/daemonium> |
| Pyran1/MalwareCollection | library | <https://github.com/Pyran1/MalwareCollection> |
| qnighy/ransomware-demo | tool | <https://github.com/qnighy/ransomware-demo> |
| Qumulo/QumuloAlerts | tool | <https://github.com/Qumulo/QumuloAlerts> |
| r0ck3r008/Ryuk | tool | <https://github.com/r0ck3r008/Ryuk> |
| R3DRUN3/magnet | framework | <https://github.com/R3DRUN3/magnet> |
| R3LI4NT/PURGE-Ransomware | tool | <https://github.com/R3LI4NT/PURGE-Ransomware> |
| R3LI4NT/XilentLocker | tool | <https://github.com/R3LI4NT/XilentLocker> |
| r3nt0n/markransom | tool | <https://github.com/r3nt0n/markransom> |
| rafaeljusto/toglacier | tool | <https://github.com/rafaeljusto/toglacier> |
| rahulrajdixit/Ransomware-Script-For-Demo | directory | <https://github.com/rahulrajdixit/Ransomware-Script-For-Demo> |
| ransomfeed/RF-lookup | dataset | <https://github.com/ransomfeed/RF-lookup> |
| RansomLook/RansomLook | tool | <https://github.com/RansomLook/RansomLook> |
| ransomNews/RedACT | dataset | <https://github.com/ransomNews/RedACT> |
| Raqeeb27/ShadowCrypt | tool | <https://github.com/Raqeeb27/ShadowCrypt> |
| redmagnu5/ForbiddenTear | research-project | <https://github.com/redmagnu5/ForbiddenTear> |
| regantemudo/dfir-playbooks | research-project | <https://github.com/regantemudo/dfir-playbooks> |
| retr00exe/pyransom | tool | <https://github.com/retr00exe/pyransom> |
| reuelmagistrado/cartint | tool | <https://github.com/reuelmagistrado/cartint> |
| rf-peixoto/Graverobber | tool | <https://github.com/rf-peixoto/Graverobber> |
| ring0shady/RansomWare | tool | <https://github.com/ring0shady/RansomWare> |
| rishank-shah/PMAT-Final-Report | tool | <https://github.com/rishank-shah/PMAT-Final-Report> |
| robacarp/nemucod_decrypt | tool | <https://github.com/robacarp/nemucod_decrypt> |
| robo3945/RaTS | tool | <https://github.com/robo3945/RaTS> |
| Ronny12345-art/Real-darkweb-links | tool | <https://github.com/Ronny12345-art/Real-darkweb-links> |
| root-acch/NotInfecktya | tool | <https://github.com/root-acch/NotInfecktya> |
| roothaxor/Ransom | tool | <https://github.com/roothaxor/Ransom> |
| rpgeeganage/file-less-ransomware-demo | tool | <https://github.com/rpgeeganage/file-less-ransomware-demo> |
| rthxr/Malware | tool | <https://github.com/rthxr/Malware> |
| Ruturaj4/Mobile-Security-Paper_summaries | library | <https://github.com/Ruturaj4/Mobile-Security-Paper_summaries> |
| rwillmann/WannaCry-Outbreak-Data-12-May-2017---19-May-2017 | dataset | <https://github.com/rwillmann/WannaCry-Outbreak-Data-12-May-2017---19-May-2017-> |
| saed-gpr/ransomware | tool | <https://github.com/saed-gpr/ransomware> |
| saferwall/malware-souk | dataset | <https://github.com/saferwall/malware-souk> |
| sagikandleker/Cyber-Labs-Protection | cli-tool | <https://github.com/sagikandleker/Cyber-Labs-Protection> |
| sakshatshinde/WannaLaugh | tool | <https://github.com/sakshatshinde/WannaLaugh> |
| Samdatastellar/Nopyfy-Ransomware | web-platform | <https://github.com/Samdatastellar/Nopyfy-Ransomware> |
| samuelgradientai-sys/c3rb3r-synology-recovery | tool | <https://github.com/samuelgradientai-sys/c3rb3r-synology-recovery> |
| sandravizz/Data-breach-analysis | tool | <https://github.com/sandravizz/Data-breach-analysis> |
| saniyakolangde/Ransomware | tool | <https://github.com/saniyakolangde/Ransomware> |
| sausagenoods/shady | tool | <https://github.com/sausagenoods/shady> |
| Sean-Everett/Splunk-Boss_of_the_SOC_v1 | tool | <https://github.com/Sean-Everett/Splunk-Boss_of_the_SOC_v1> |
| seanpm2001/Nuclear-Ad-Bombs-Specification | tool | <https://github.com/seanpm2001/Nuclear-Ad-Bombs-Specification> |
| seanpm2001/Ransomware-Info | dataset | <https://github.com/seanpm2001/Ransomware-Info> |
| securenza/SecurityFeed | api-service | <https://github.com/securenza/SecurityFeed> |
| SecurityRonin/nameback | tool | <https://github.com/SecurityRonin/nameback> |
| seekbytes/MicroSCOPE | tool | <https://github.com/seekbytes/MicroSCOPE> |
| sera619/PandorasBox---HackWithPython | tool | <https://github.com/sera619/PandorasBox---HackWithPython> |
| sergiLopez/Flanders-Trojan | tool | <https://github.com/sergiLopez/Flanders-Trojan> |
| SergioZ3R0/Sergio-Code | tool | <https://github.com/SergioZ3R0/Sergio-Code> |
| sgagankumar/NotAMalware | tool | <https://github.com/sgagankumar/NotAMalware> |
| Sh1r0ko11/AndroCrypt | tool | <https://github.com/Sh1r0ko11/AndroCrypt> |
| Shadow8021/darkwaves | research-project | <https://github.com/Shadow8021/darkwaves> |
| shaktavist/Online-Security-Tools | tool | <https://github.com/shaktavist/Online-Security-Tools> |
| shamindraparui/MTechRansomwareDetection | tool | <https://github.com/shamindraparui/MTechRansomwareDetection> |
| shantoroy/intro-2-cybersecurity-in-python | tool | <https://github.com/shantoroy/intro-2-cybersecurity-in-python> |
| SHIFox8/synology-dsm-vuln-scanner | tool | <https://github.com/SHIFox8/synology-dsm-vuln-scanner> |
| shivaya-dav/DogeRus | tool | <https://github.com/shivaya-dav/DogeRus> |
| simonrdavies/NapierOne | api-service | <https://github.com/simonrdavies/NapierOne> |
| simplerhacking/evilgophish-course | tool | <https://github.com/simplerhacking/evilgophish-course> |
| Siradankullanici/HaikuRansomware | tool | <https://github.com/Siradankullanici/HaikuRansomware> |
| SitinCloud/Owlyshield | framework | <https://github.com/SitinCloud/Owlyshield> |
| skaspi/dynamic-ransom | tool | <https://github.com/skaspi/dynamic-ransom> |
| smottoms/ransomware-simulation | container | <https://github.com/smottoms/ransomware-simulation> |
| SOCRadar LABS | tool | <https://socradar.io/labs/threat-actor/> |
| SOCRadarSTRU/STRU-threat-intel | research-project | <https://github.com/SOCRadarSTRU/STRU-threat-intel> |
| Sokow86/awesome-malware-resources | awesome-list | <https://github.com/Sokow86/awesome-malware-resources> |
| sourceclear/ransomware-poc | tool | <https://github.com/sourceclear/ransomware-poc> |
| SparkyzCodez/FSRM-Anti-ransomware | cli-tool | <https://github.com/SparkyzCodez/FSRM-Anti-ransomware> |
| Squareek/Dangerous-Trojan | tool | <https://github.com/Squareek/Dangerous-Trojan> |
| StevenBlack/hosts | plugin | <https://github.com/StevenBlack/hosts> |
| streambinder/cryptoloacker | web-platform | <https://github.com/streambinder/cryptoloacker> |
| StringManolo/nbmxbsf | framework | <https://github.com/StringManolo/nbmxbsf> |
| StukovBlack/AndroidRansomware | research-project | <https://github.com/StukovBlack/AndroidRansomware> |
| SuatKoray/Amethyst | tool | <https://github.com/SuatKoray/Amethyst> |
| substationworm/IndCyberSecLetters | tool | <https://github.com/substationworm/IndCyberSecLetters> |
| SUmidcyber/ZeroScout | framework | <https://github.com/SUmidcyber/ZeroScout> |
| SVelizDonoso/ransomware | tool | <https://github.com/SVelizDonoso/ransomware> |
| SyedShaheerHussain/Ransomware-Simulation-and-Defense-Mechanism-Python-GUI | dashboard | <https://github.com/SyedShaheerHussain/Ransomware-Simulation-and-Defense-Mechanism-Python-GUI> |
| Tacola320/RaaS_mitre | web-platform | <https://github.com/Tacola320/RaaS_mitre> |
| tarcisio-marinho/GonnaCry | library | <https://github.com/tarcisio-marinho/GonnaCry> |
| TechSavvyTaco/Android-Termux-Ransomware-Proof-of-Concept | research-project | <https://github.com/TechSavvyTaco/Android-Termux-Ransomware-Proof-of-Concept> |
| teozoia/Caronte | tool | <https://github.com/teozoia/Caronte> |
| termuxhackers-id/sara | framework | <https://github.com/termuxhackers-id/sara> |
| TF0X/F0Xware | tool | <https://github.com/TF0X/F0Xware> |
| Thales | tool | <https://cds.thalesgroup.com/en/cyberthreat/attacks-page> |
| TheCreeper/UselessLocker | tool | <https://github.com/TheCreeper/UselessLocker> |
| thedevtoolsmith/KMike | tool | <https://github.com/thedevtoolsmith/KMike> |
| thedudefello/ToxicDatabase | dataset | <https://github.com/thedudefello/ToxicDatabase> |
| thenurhabib/ransomware | tool | <https://github.com/thenurhabib/ransomware> |
| thez3r0/n00blocker | tool | <https://github.com/thez3r0/n00blocker> |
| thiagorcdl/bitcoin_heist | tool | <https://github.com/thiagorcdl/bitcoin_heist> |
| thisisnzed/Anywhere | cli-tool | <https://github.com/thisisnzed/Anywhere> |
| thisisnzed/Pandora | cli-tool | <https://github.com/thisisnzed/Pandora> |
| ThoughtfulDev/SupergirlOnCrypt | tool | <https://github.com/ThoughtfulDev/SupergirlOnCrypt> |
| ThreatLabz/ransomware_notes | research-project | <https://github.com/ThreatLabz/ransomware_notes> |
| ThreatLabz/tools | tool | <https://github.com/ThreatLabz/tools> |
| THU-WingTecher/MarauderMap | dataset | <https://github.com/THU-WingTecher/MarauderMap> |
| tidalcyber/cyber-threat-profiling | library | <https://github.com/tidalcyber/cyber-threat-profiling> |
| tiuxo/hosts | tool | <https://github.com/tiuxo/hosts> |
| TomasPhilippart/ebpfangel | tool | <https://github.com/TomasPhilippart/ebpfangel> |
| truelockmc/python-ransomware | tool | <https://github.com/truelockmc/python-ransomware> |
| Tsuyoken/kencryptor | cli-tool | <https://github.com/Tsuyoken/kencryptor> |
| Tugamer89/RansomTuga | tool | <https://github.com/Tugamer89/RansomTuga> |
| twelvesec/panicbutton | desktop-app | <https://github.com/twelvesec/panicbutton> |
| Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist | cli-tool | <https://github.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist> |
| umutcamliyurt/GoCry | web-platform | <https://github.com/umutcamliyurt/GoCry> |
| undo-ransomware/ransomware_detection | tool | <https://github.com/undo-ransomware/ransomware_detection> |
| usrtem/Conti-Leak-Analysis | tool | <https://github.com/usrtem/Conti-Leak-Analysis> |
| usrtem/TrickBot-Analysis | research-project | <https://github.com/usrtem/TrickBot-Analysis> |
| V-H-R-Oliveira/Lcry | plugin | <https://github.com/V-H-R-Oliveira/Lcry> |
| vaiitoMYSQTIK/Conti-RW-NEW | research-project | <https://github.com/vaiitoMYSQTIK/Conti-RW-NEW> |
| VaimpierOfficial/Vaim-RamSom | tool | <https://github.com/VaimpierOfficial/Vaim-RamSom> |
| venkatesh-jaganathan/Ransomware-identification | tool | <https://github.com/venkatesh-jaganathan/Ransomware-identification> |
| Vimwix/Dll-Database | dataset | <https://github.com/Vimwix/Dll-Database> |
| vineelsai26/Malware | research-project | <https://github.com/vineelsai26/Malware> |
| Viralmaniar/Phirautee | cli-tool | <https://github.com/Viralmaniar/Phirautee> |
| ViRb3/cdx2018-ransomware-decryptor | research-project | <https://github.com/ViRb3/cdx2018-ransomware-decryptor> |
| VirusSign/malware-samples | dataset | <https://github.com/VirusSign/malware-samples> |
| vmeazevedo/ransomware_py | tool | <https://github.com/vmeazevedo/ransomware_py> |
| VolkanSah/Ransy-EDU | tool | <https://github.com/VolkanSah/Ransy-EDU> |
| Voraka/Gomasom_Decryptor | tool | <https://github.com/Voraka/Gomasom_Decryptor> |
| VQD-BSV-Official/RecoveryJpeg | tool | <https://github.com/VQD-BSV-Official/RecoveryJpeg> |
| vricosti/ech0raix_decryptor | tool | <https://github.com/vricosti/ech0raix_decryptor> |
| Vvoox/Ransomware_Py | tool | <https://github.com/Vvoox/Ransomware_Py> |
| Wapiti08/Defense_Evasion_with_GAN | api-service | <https://github.com/Wapiti08/Defense_Evasion_with_GAN> |
| wcsf-rd/Adrenaline-CryptoSentinel | tool | <https://github.com/wcsf-rd/Adrenaline-CryptoSentinel> |
| webmestudio/my-ransomeware | cli-tool | <https://github.com/webmestudio/my-ransomeware> |
| websec/EduRansW-Educational-Ransomware | tool | <https://github.com/websec/EduRansW-Educational-Ransomware> |
| west-wind/Conti-leaks | tool | <https://github.com/west-wind/Conti-leaks> |
| Whomrx666/exploit-X | mobile-app | <https://github.com/Whomrx666/exploit-X> |
| wiced1/Ransomware | tool | <https://github.com/wiced1/Ransomware> |
| wille/cry | web-platform | <https://github.com/wille/cry> |
| Willie-Conway/Cybersecurity-History-Event-Log | cli-tool | <https://github.com/Willie-Conway/Cybersecurity-History-Event-Log> |
| Willie-Conway/PATHOGEN | research-project | <https://github.com/Willie-Conway/PATHOGEN> |
| WRG-11/wrg-sigma-rules | plugin | <https://github.com/WRG-11/wrg-sigma-rules> |
| XeinTDM/PyRansom | tool | <https://github.com/XeinTDM/PyRansom> |
| Xeroxxhah/l0ck | tool | <https://github.com/Xeroxxhah/l0ck> |
| yannickboog/ransomwatch | research-project | <https://github.com/yannickboog/ransomwatch> |
| zelon88/Ransomware_Defender | tool | <https://github.com/zelon88/Ransomware_Defender> |
| zR00t1/WannaCry | tool | <https://github.com/zR00t1/WannaCry> |
| Zzutiky666/LockBit | research-project | <https://github.com/Zzutiky666/LockBit> |

### Resource Lists & Directories

| Name | Type | URL |
|---|---|---|
| anavargas071822/mcp-server-bazaar | awesome-list | <https://github.com/anavargas071822/mcp-server-bazaar> |
| awesome-privacy | awesome-list | <https://github.com/Lissy93/awesome-privacy/> |
| awesome-threat-intelligence | awesome-list | <https://github.com/hslatman/awesome-threat-intelligence> |
| jivoi/awesome-osint | awesome-list | <https://github.com/jivoi/awesome-osint> |
| lissy93/personal-security-checklist | awesome-list | <https://github.com/lissy93/personal-security-checklist> |

### Threat Intelligence Platforms

| Name | Type | URL |
|---|---|---|
| 0n1cOn3/The-NSO-Blacklist | research-project | <https://github.com/0n1cOn3/The-NSO-Blacklist> |
| 0x0allenace/email-conversation-integrity-detection | plugin | <https://github.com/0x0allenace/email-conversation-integrity-detection> |
| 0x4427/Defanger | plugin | <https://github.com/0x4427/Defanger> |
| 0x4D31/fatt | tool | <https://github.com/0x4D31/fatt> |
| 0x4D31/hassh-utils | container | <https://github.com/0x4D31/hassh-utils> |
| 0x783kb/Threat-Analysis-Handbook | cli-tool | <https://github.com/0x783kb/Threat-Analysis-Handbook> |
| 0xAnalyst/DefenderATPQueries | tool | <https://github.com/0xAnalyst/DefenderATPQueries> |
| 0xAnalyst/Sysmon | tool | <https://github.com/0xAnalyst/Sysmon> |
| 0xCBradford/Vera5 | plugin | <https://github.com/0xCBradford/Vera5> |
| 0xflux/rust_shellcode | cli-tool | <https://github.com/0xflux/rust_shellcode> |
| 0xhav0c/ARGUS | desktop-app | <https://github.com/0xhav0c/ARGUS> |
| 0xm4g1c/ThreatSense | api-service | <https://github.com/0xm4g1c/ThreatSense> |
| 0xMarcio/pocindex | directory | <https://github.com/0xMarcio/pocindex> |
| 0xNasef/SOC-AI-Assistant | tool | <https://github.com/0xNasef/SOC-AI-Assistant> |
| 0xrajneesh/Microsoft-Defender-EDR-Home-Lab | tool | <https://github.com/0xrajneesh/Microsoft-Defender-EDR-Home-Lab> |
| 0xrajneesh/Wireshark-Home-Lab | tool | <https://github.com/0xrajneesh/Wireshark-Home-Lab> |
| 0xrawsec/gene | tool | <https://github.com/0xrawsec/gene> |
| 0xrawsec/whids | tool | <https://github.com/0xrawsec/whids> |
| 0xsha/CrazyWall | tool | <https://github.com/0xsha/CrazyWall> |
| 0xsha/sweetie-data | dataset | <https://github.com/0xsha/sweetie-data> |
| 0xtf/nsm-attack | tool | <https://github.com/0xtf/nsm-attack> |
| 0xTnxl/silentlink | research-project | <https://github.com/0xTnxl/silentlink> |
| 1000001AS/super-duper-eureka | tool | <https://github.com/1000001AS/super-duper-eureka> |
| 123dars/CTI-Dashboard | dashboard | <https://github.com/123dars/CTI-Dashboard> |
| 2000pawan/Cyber-Attack-Threat-Classification | dataset | <https://github.com/2000pawan/Cyber-Attack-Threat-Classification> |
| 3c7/infrastructure-tracking-schema | tool | <https://github.com/3c7/infrastructure-tracking-schema> |
| 3CORESec/S2AN | tool | <https://github.com/3CORESec/S2AN> |
| 401trg/detections | tool | <https://github.com/401trg/detections> |
| 401trg/utilities | tool | <https://github.com/401trg/utilities> |
| 4nt11/EYENET | web-platform | <https://github.com/4nt11/EYENET> |
| 4R9UN/fastmcp-threatintel | tool | <https://github.com/4R9UN/fastmcp-threatintel> |
| 777genius/social-monitor | api-service | <https://github.com/777genius/social-monitor> |
| 9b/boxcar | dataset | <https://github.com/9b/boxcar> |
| a2awais/Nation-State-APT-Intelligence | web-platform | <https://github.com/a2awais/Nation-State-APT-Intelligence> |
| a2awais/Threat-Hunting | web-platform | <https://github.com/a2awais/Threat-Hunting> |
| a3r0id/mass-scanning-tools | web-platform | <https://github.com/a3r0id/mass-scanning-tools> |
| A3sal0n/CyberThreatHunting | tool | <https://github.com/A3sal0n/CyberThreatHunting> |
| Aabyss-Team/Ban-Hacker-IP-Plan | tool | <https://github.com/Aabyss-Team/Ban-Hacker-IP-Plan> |
| AAH20/Apex_Cyber_Sentinel | tool | <https://github.com/AAH20/Apex_Cyber_Sentinel> |
| aakashraman/usbhawk | tool | <https://github.com/aakashraman/usbhawk> |
| Aamir-Muhammad/CrowdStrike-Queries | tool | <https://github.com/Aamir-Muhammad/CrowdStrike-Queries> |
| Aaniket09/AI-SOC-Agent | cli-tool | <https://github.com/Aaniket09/AI-SOC-Agent> |
| aaravshah1311/Agent-2 | cli-tool | <https://github.com/aaravshah1311/Agent-2> |
| aaronkaplan/cti-llm | tool | <https://github.com/aaronkaplan/cti-llm> |
| Aathithya-Shanmuga-Sundaram/ClarusSight | dashboard | <https://github.com/Aathithya-Shanmuga-Sundaram/ClarusSight> |
| AbdallaElzedy/Cortex-XSIAM | tool | <https://github.com/AbdallaElzedy/Cortex-XSIAM> |
| AbdaullahAG/ThreatLens | api-service | <https://github.com/AbdaullahAG/ThreatLens> |
| AbeWinters/Threat-Profiles-for-Control-Prioritization | tool | <https://github.com/AbeWinters/Threat-Profiles-for-Control-Prioritization> |
| AbstractionsLab/PyFlowintel | api-service | <https://github.com/AbstractionsLab/PyFlowintel> |
| AbstractionsLab/satrap-dl | container | <https://github.com/AbstractionsLab/satrap-dl> |
| acorvello/data-analysis | tool | <https://github.com/acorvello/data-analysis> |
| action-ai-institute/MABEL-dataset | dataset | <https://github.com/action-ai-institute/MABEL-dataset> |
| activecm/rita | framework | <https://github.com/activecm/rita> |
| adulau/misp-osint-collection | tool | <https://github.com/adulau/misp-osint-collection> |
| adulau/the-art-of-pivoting | tool | <https://github.com/adulau/the-art-of-pivoting> |
| adulau/threat-actor-explorer | dataset | <https://github.com/adulau/threat-actor-explorer> |
| advanced-threat-research/Yara-Rules | research-project | <https://github.com/advanced-threat-research/Yara-Rules> |
| advens/libenrich | dataset | <https://github.com/advens/libenrich> |
| Afabio2007/weekend-lottery-contract | tool | <https://github.com/Afabio2007/weekend-lottery-contract> |
| ag2020sa/cti-ai-trust-gateway | api-service | <https://github.com/ag2020sa/cti-ai-trust-gateway> |
| ahmedmohamed007/ThreatFeed-Analyzer | dataset | <https://github.com/ahmedmohamed007/ThreatFeed-Analyzer> |
| ail-project/ail-feeder-leak | plugin | <https://github.com/ail-project/ail-feeder-leak> |
| ail-project/CCWget | tool | <https://github.com/ail-project/CCWget> |
| airbus-cert/ntTraceControl | cli-tool | <https://github.com/airbus-cert/ntTraceControl> |
| aj-tap/huntsman | framework | <https://github.com/aj-tap/huntsman> |
| AJahmadcyber/homelab-mdr | tool | <https://github.com/AJahmadcyber/homelab-mdr> |
| ajcyberdefense/cowrie-honeypot | tool | <https://github.com/ajcyberdefense/cowrie-honeypot> |
| ajmelian/Buscador-de-Vulnerabilidades | api-service | <https://github.com/ajmelian/Buscador-de-Vulnerabilidades> |
| Ak-cybe/soc-roadmap-2026 | tool | <https://github.com/Ak-cybe/soc-roadmap-2026> |
| akajhon/MalOps-Agent | tool | <https://github.com/akajhon/MalOps-Agent> |
| aleksandergrambelik-png/SanderShield | api-service | <https://github.com/aleksandergrambelik-png/SanderShield> |
| alenpepaxx1/Global-Cyber-Threat-Map | tool | <https://github.com/alenpepaxx1/Global-Cyber-Threat-Map> |
| alessandromrc/tor-monitoring | tool | <https://github.com/alessandromrc/tor-monitoring> |
| alessandromrc/unwanted-threats | dataset | <https://github.com/alessandromrc/unwanted-threats> |
| alex-ilgayev/secfeed | dataset | <https://github.com/alex-ilgayev/secfeed> |
| alexlinos/threat-feed-me | api-service | <https://github.com/alexlinos/threat-feed-me> |
| alextibor/wazuh-fortigate-rules-decoders | tool | <https://github.com/alextibor/wazuh-fortigate-rules-decoders> |
| alhemdrew/Project-watchdog | web-platform | <https://github.com/alhemdrew/Project-watchdog> |
| alicangnll/CTI_Arastirmalarim | tool | <https://github.com/alicangnll/CTI_Arastirmalarim> |
| alkivi-sas/3cx-freshdesk-macos | tool | <https://github.com/alkivi-sas/3cx-freshdesk-macos> |
| AlphaKiloDelta/A-Cost-Efficient-Threat-Intelligence-Platform-Powered-by-Crowdsourced-OSINT | web-platform | <https://github.com/AlphaKiloDelta/A-Cost-Efficient-Threat-Intelligence-Platform-Powered-by-Crowdsourced-OSINT> |
| alt3kx/wafaray | tool | <https://github.com/alt3kx/wafaray> |
| alt3kx/wafparan01d3 | tool | <https://github.com/alt3kx/wafparan01d3> |
| altered-intelligence/scry | api-service | <https://github.com/altered-intelligence/scry> |
| alvin-tosh/Infosec-and-Hacking-Scripts | tool | <https://github.com/alvin-tosh/Infosec-and-Hacking-Scripts> |
| amarokinc/bad-asn | tool | <https://github.com/amarokinc/bad-asn> |
| AmmarAikan/ACTIT-Platform | container | <https://github.com/AmmarAikan/ACTIT-Platform> |
| AmmarAikan/AmmarAikan | tool | <https://github.com/AmmarAikan/AmmarAikan> |
| AmmarAikan/CTI-Tool-Showcase | tool | <https://github.com/AmmarAikan/CTI-Tool-Showcase> |
| AmnestyTech/investigations | tool | <https://github.com/AmnestyTech/investigations> |
| ancailliau/synapse-onyphe | api-service | <https://github.com/ancailliau/synapse-onyphe> |
| ancailliau/SynSharp | web-platform | <https://github.com/ancailliau/SynSharp> |
| ancientswede/Huginn | tool | <https://github.com/ancientswede/Huginn> |
| andreicscs/HoneyWire | container | <https://github.com/andreicscs/HoneyWire> |
| andreitrcv/Intel-LLM | tool | <https://github.com/andreitrcv/Intel-LLM> |
| andrewrebora/APT-Groups-and-Operations-SQL | dataset | <https://github.com/andrewrebora/APT-Groups-and-Operations-SQL> |
| aniknohan/misp-phishing-threat-intelligence-lab | tool | <https://github.com/aniknohan/misp-phishing-threat-intelligence-lab> |
| anpa1200/adversarygraph | container | <https://github.com/anpa1200/adversarygraph> |
| anpa1200/AIDebug | research-project | <https://github.com/anpa1200/AIDebug> |
| anpa1200/anpa1200.github.io | research-project | <https://github.com/anpa1200/anpa1200.github.io> |
| anpa1200/CTI | research-project | <https://github.com/anpa1200/CTI> |
| anpa1200/cti-analyst-field-manual | research-project | <https://github.com/anpa1200/cti-analyst-field-manual> |
| anpa1200/CTI_as_a_Code | container | <https://github.com/anpa1200/CTI_as_a_Code> |
| anpa1200/customer-driven-ai-cti-project-template | tool | <https://github.com/anpa1200/customer-driven-ai-cti-project-template> |
| anpa1200/cvss_4.0 | cli-tool | <https://github.com/anpa1200/cvss_4.0> |
| anpa1200/opencti-intelligent-shield | tool | <https://github.com/anpa1200/opencti-intelligent-shield> |
| anpa1200/operation-desert-hydra | tool | <https://github.com/anpa1200/operation-desert-hydra> |
| anpa1200/PE-Import-Analyzer | api-service | <https://github.com/anpa1200/PE-Import-Analyzer> |
| anpa1200/stratus-ai | container | <https://github.com/anpa1200/stratus-ai> |
| anpa1200/Unpacker | tool | <https://github.com/anpa1200/Unpacker> |
| anpa1200org/start-here | tool | <https://github.com/anpa1200org/start-here> |
| Anshulrajkumar/MayaSec | library | <https://github.com/Anshulrajkumar/MayaSec> |
| Antharia/att-ck-dataset | dataset | <https://github.com/Antharia/att-ck-dataset> |
| anvilogic-forge/armory | tool | <https://github.com/anvilogic-forge/armory> |
| anyrun/YARA | tool | <https://github.com/anyrun/YARA> |
| api-evangelist/censys | api-service | <https://github.com/api-evangelist/censys> |
| api-evangelist/tenfold | plugin | <https://github.com/api-evangelist/tenfold> |
| apurvsinghgautam/PastebinScrapy | api-service | <https://github.com/apurvsinghgautam/PastebinScrapy> |
| ARaChn3/gfb | tool | <https://github.com/ARaChn3/gfb> |
| arachne-threat-intel/spindle | tool | <https://github.com/arachne-threat-intel/spindle> |
| arelli/simpleSTIX | tool | <https://github.com/arelli/simpleSTIX> |
| ares-369/zarqa | web-platform | <https://github.com/ares-369/zarqa> |
| arinchatterg/rstpscanner | tool | <https://github.com/arinchatterg/rstpscanner> |
| arkregiel/RansomReport | tool | <https://github.com/arkregiel/RansomReport> |
| arnydo/PSEmailRep | plugin | <https://github.com/arnydo/PSEmailRep> |
| ArshiBansal/cyberthreat_intelligence_ai | web-platform | <https://github.com/ArshiBansal/cyberthreat_intelligence_ai> |
| ArshiBansal/URL_Threat_Analyzer | dataset | <https://github.com/ArshiBansal/URL_Threat_Analyzer> |
| Arszilla/Pwn-The-Jewels | web-platform | <https://github.com/Arszilla/Pwn-The-Jewels> |
| artk-code/virgil | tool | <https://github.com/artk-code/virgil> |
| asantiagorivera8/weak-cipher-detector | tool | <https://github.com/asantiagorivera8/weak-cipher-detector> |
| ashwin-patil/blue-teaming-with-kql | tool | <https://github.com/ashwin-patil/blue-teaming-with-kql> |
| ashwin-patil/threat-hunting-with-notebooks | tool | <https://github.com/ashwin-patil/threat-hunting-with-notebooks> |
| ashwinvis98/adversarial-ai-cti | tool | <https://github.com/ashwinvis98/adversarial-ai-cti> |
| ashwinvis98/opencti-ai-enrichment | tool | <https://github.com/ashwinvis98/opencti-ai-enrichment> |
| ashwinvis98/promptlsh | tool | <https://github.com/ashwinvis98/promptlsh> |
| asif-visionary/Advanced-CyberShield-Phishing-Detector | dashboard | <https://github.com/asif-visionary/Advanced-CyberShield-Phishing-Detector> |
| assafkip/kipi | web-platform | <https://github.com/assafkip/kipi> |
| assafkip/theia | tool | <https://github.com/assafkip/theia> |
| AssuranceMaladieSec/CertStreamMonitor | dataset | <https://github.com/AssuranceMaladieSec/CertStreamMonitor> |
| atlas-bear/osint-tools | container | <https://github.com/atlas-bear/osint-tools> |
| Audityzer/Audityzer-PRO | framework | <https://github.com/Audityzer/Audityzer-PRO> |
| AuvaLabs/threatwatch | web-platform | <https://github.com/AuvaLabs/threatwatch> |
| aw-junaid/Hacking-Tools | research-project | <https://github.com/aw-junaid/Hacking-Tools> |
| awaisawaisop698-hub/cyber-logs-analyzer | web-platform | <https://github.com/awaisawaisop698-hub/cyber-logs-analyzer-> |
| aws-samples/sample-agentic-attack-tree-generator | plugin | <https://github.com/aws-samples/sample-agentic-attack-tree-generator> |
| Aya8sa/AccessControlProject | tool | <https://github.com/Aya8sa/AccessControlProject> |
| Ayibongwe02/Cybersecurity-Incident-Threat-Intelligence-Hub | dashboard | <https://github.com/Ayibongwe02/Cybersecurity-Incident-Threat-Intelligence-Hub> |
| ayushkp930/PhishMatrix | web-platform | <https://github.com/ayushkp930/PhishMatrix> |
| ayushkp930/PhishShield-Pro | tool | <https://github.com/ayushkp930/PhishShield-Pro> |
| Azerbaijan-Cybersecurity-Center/LogCTIAI | tool | <https://github.com/Azerbaijan-Cybersecurity-Center/LogCTIAI> |
| b-lamer/ePaperNewsFeed | dataset | <https://github.com/b-lamer/ePaperNewsFeed> |
| backbay-labs/clawdstrike | web-platform | <https://github.com/backbay-labs/clawdstrike> |
| backbay-labs/hush | tool | <https://github.com/backbay-labs/hush> |
| backbay-labs/thrunt-god | plugin | <https://github.com/backbay-labs/thrunt-god> |
| BADGUIDS/badguids.github.io | dashboard | <https://github.com/BADGUIDS/badguids.github.io> |
| banaxou/dark-sherlock | tool | <https://github.com/banaxou/dark-sherlock> |
| Barnes70/TLCTC | tool | <https://github.com/Barnes70/TLCTC> |
| bartblaze/MaTiRe | tool | <https://github.com/bartblaze/MaTiRe> |
| bartblaze/Yara-rules | tool | <https://github.com/bartblaze/Yara-rules> |
| bayufedra/ipti | tool | <https://github.com/bayufedra/ipti> |
| bdg9412/artex-ko-plus | tool | <https://github.com/bdg9412/artex-ko-plus> |
| beenuar/AiSOC | api-service | <https://github.com/beenuar/AiSOC> |
| beenuar/shieldapp-android | api-service | <https://github.com/beenuar/shieldapp-android> |
| bekkaze/abusebox | container | <https://github.com/bekkaze/abusebox> |
| benjamin-small/stix-meta-explorer | tool | <https://github.com/benjamin-small/stix-meta-explorer> |
| BenJonesVA/vt-to-misp | api-service | <https://github.com/BenJonesVA/vt-to-misp> |
| benscha/KQLAdvancedHunting | tool | <https://github.com/benscha/KQLAdvancedHunting> |
| bentleygd/CSIC | dataset | <https://github.com/bentleygd/CSIC> |
| Bert-JanP/Hunting-Queries-Detection-Rules | tool | <https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules> |
| Bert-JanP/Open-Source-Threat-Intel-Feeds | dataset | <https://github.com/Bert-JanP/Open-Source-Threat-Intel-Feeds> |
| bfuzzy/auditd-attack | framework | <https://github.com/bfuzzy/auditd-attack> |
| bhavikmalhotra/ThreatPad | container | <https://github.com/bhavikmalhotra/ThreatPad> |
| bhxinderj/cti-rag-analyst-support | tool | <https://github.com/bhxinderj/cti-rag-analyst-support> |
| binalyze/tigma | tool | <https://github.com/binalyze/tigma> |
| Biswajit1999/lattice-radiation-twin | cli-tool | <https://github.com/Biswajit1999/lattice-radiation-twin> |
| bitbug0x55AA/personal-cti-streamliner | container | <https://github.com/bitbug0x55AA/personal-cti-streamliner> |
| bl4ckr0ss3/ttpscope | cli-tool | <https://github.com/bl4ckr0ss3/ttpscope> |
| blackhillsinfosec/EventLogging | directory | <https://github.com/blackhillsinfosec/EventLogging> |
| blackorbird/APT_REPORT | tool | <https://github.com/blackorbird/APT_REPORT> |
| BlackSnufkin/OdinEye | dashboard | <https://github.com/BlackSnufkin/OdinEye> |
| blackstork-io/blackstork-cli | cli-tool | <https://github.com/blackstork-io/blackstork-cli> |
| blackstork-io/blackstork-templates | tool | <https://github.com/blackstork-io/blackstork-templates> |
| blitzcti/sgecti | framework | <https://github.com/blitzcti/sgecti> |
| bobby-tablez/TTP-Threat-Feeds | dataset | <https://github.com/bobby-tablez/TTP-Threat-Feeds> |
| bogdanticu88/ApexHunter | tool | <https://github.com/bogdanticu88/ApexHunter> |
| boringtools/git-alerts | tool | <https://github.com/boringtools/git-alerts> |
| BRANDEFENSE/exploited-vulnerabilities-dataset | dataset | <https://github.com/BRANDEFENSE/exploited-vulnerabilities-dataset> |
| brayden031/brayden031 | cli-tool | <https://github.com/brayden031/brayden031> |
| brayden031/varalyze | tool | <https://github.com/brayden031/varalyze> |
| BrewedIntel/apt-resources | awesome-list | <https://github.com/BrewedIntel/apt-resources> |
| BrewedIntel/cyber-training-resources | awesome-list | <https://github.com/BrewedIntel/cyber-training-resources> |
| BrewedIntel/threat-intel-mailing-lists | awesome-list | <https://github.com/BrewedIntel/threat-intel-mailing-lists> |
| Briella009/Triagebloom | tool | <https://github.com/Briella009/Triagebloom> |
| briwandt/modern-infostealer-research | research-project | <https://github.com/briwandt/modern-infostealer-research> |
| BrsDincer/OpenAI_ChatGPT_App_Injection_Investigation_Results_And_Scripts | framework | <https://github.com/BrsDincer/OpenAI_ChatGPT_App_Injection_Investigation_Results_And_Scripts> |
| brunoaugusto1978/threatforge | web-platform | <https://github.com/brunoaugusto1978/threatforge> |
| brunomarsola/ioc-enrichment-toolkit | framework | <https://github.com/brunomarsola/ioc-enrichment-toolkit> |
| brunos3d/crysknife | tool | <https://github.com/brunos3d/crysknife> |
| brunosergi/darkweb-forums-tracker | container | <https://github.com/brunosergi/darkweb-forums-tracker> |
| brunosergi/tldr-threat-reports | container | <https://github.com/brunosergi/tldr-threat-reports> |
| brycampbell/YARA | tool | <https://github.com/brycampbell/YARA> |
| Bugs-B0unt3r/google-sheets-hunting-bad-domains | api-service | <https://github.com/Bugs-B0unt3r/google-sheets-hunting-bad-domains> |
| BushidoUK/Abused-Legitimate-Services | web-platform | <https://github.com/BushidoUK/Abused-Legitimate-Services> |
| BushidoUK/Android-Banking-Trojan-Nexus | tool | <https://github.com/BushidoUK/Android-Banking-Trojan-Nexus> |
| BushidoUK/CTI-Analyst-Challenge | tool | <https://github.com/BushidoUK/CTI-Analyst-Challenge> |
| BushidoUK/CTI-Lexicon | tool | <https://github.com/BushidoUK/CTI-Lexicon> |
| BushidoUK/CTI-Quiz | tool | <https://github.com/BushidoUK/CTI-Quiz> |
| BushidoUK/CTI-Regex | tool | <https://github.com/BushidoUK/CTI-Regex> |
| BushidoUK/Exploring-APT-campaigns | tool | <https://github.com/BushidoUK/Exploring-APT-campaigns> |
| BushidoUK/Project-Orbital | tool | <https://github.com/BushidoUK/Project-Orbital> |
| BushidoUK/UK-Critical-Infrastructure | research-project | <https://github.com/BushidoUK/UK-Critical-Infrastructure> |
| c1cad4/robotcyb | api-service | <https://github.com/c1cad4/robotcyb> |
| calamityz/CTI-Installation-Connection | dashboard | <https://github.com/calamityz/CTI-Installation-Connection> |
| canstralian/PowerShellToolkit | framework | <https://github.com/canstralian/PowerShellToolkit> |
| carbon-evolution/osiris | dashboard | <https://github.com/carbon-evolution/osiris> |
| Carlitosh/CTI-Model-QGIS | tool | <https://github.com/Carlitosh/CTI-Model-QGIS> |
| carlpit/ioc-extractor | cli-tool | <https://github.com/carlpit/ioc-extractor> |
| CCXLabs/CCXDigger | tool | <https://github.com/CCXLabs/CCXDigger> |
| cedricg-mirror/cedricg-mirror.github.io | tool | <https://github.com/cedricg-mirror/cedricg-mirror.github.io> |
| center-for-threat-informed-defense/adversary_emulation_library | library | <https://github.com/center-for-threat-informed-defense/adversary_emulation_library> |
| center-for-threat-informed-defense/attack-control-framework-mappings | framework | <https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings> |
| center-for-threat-informed-defense/attack-flow | dataset | <https://github.com/center-for-threat-informed-defense/attack-flow> |
| center-for-threat-informed-defense/attack-powered-suit | browser-extension | <https://github.com/center-for-threat-informed-defense/attack-powered-suit> |
| center-for-threat-informed-defense/attack_to_veris | research-project | <https://github.com/center-for-threat-informed-defense/attack_to_veris> |
| center-for-threat-informed-defense/cloud-analytics | web-platform | <https://github.com/center-for-threat-informed-defense/cloud-analytics> |
| center-for-threat-informed-defense/cti-blueprints | tool | <https://github.com/center-for-threat-informed-defense/cti-blueprints> |
| center-for-threat-informed-defense/insider-threat-ttp-kb | tool | <https://github.com/center-for-threat-informed-defense/insider-threat-ttp-kb> |
| center-for-threat-informed-defense/m3tid | research-project | <https://github.com/center-for-threat-informed-defense/m3tid> |
| center-for-threat-informed-defense/sightings_ecosystem | tool | <https://github.com/center-for-threat-informed-defense/sightings_ecosystem> |
| center-for-threat-informed-defense/technique-inference-engine | tool | <https://github.com/center-for-threat-informed-defense/technique-inference-engine> |
| center-for-threat-informed-defense/threat-modeling-with-attack | tool | <https://github.com/center-for-threat-informed-defense/threat-modeling-with-attack> |
| center-for-threat-informed-defense/top-attack-techniques | tool | <https://github.com/center-for-threat-informed-defense/top-attack-techniques> |
| center-for-threat-informed-defense/tram | web-platform | <https://github.com/center-for-threat-informed-defense/tram> |
| CERN-CERT/pDNSSOC | tool | <https://github.com/CERN-CERT/pDNSSOC> |
| cert-orangecyberdefense/datalake-taxii-integration | container | <https://github.com/cert-orangecyberdefense/datalake-taxii-integration> |
| CERTCC/Vulnerability-Data-Archive | dataset | <https://github.com/CERTCC/Vulnerability-Data-Archive> |
| ch33r10/BlueSpace2021 | tool | <https://github.com/ch33r10/BlueSpace2021> |
| ch33r10/DEFCON29-BTV-ThreatReportRoulette | tool | <https://github.com/ch33r10/DEFCON29-BTV-ThreatReportRoulette> |
| ch33r10/SunflowerCon | tool | <https://github.com/ch33r10/SunflowerCon> |
| ch33r10/THOTCON0xB | tool | <https://github.com/ch33r10/THOTCON0xB> |
| chainguard-dev/osquery-defense-kit | tool | <https://github.com/chainguard-dev/osquery-defense-kit> |
| ChiefGyk3D/typo-sniper | container | <https://github.com/ChiefGyk3D/typo-sniper> |
| Chill-Ethical-People/Optrasight | web-platform | <https://github.com/Chill-Ethical-People/Optrasight> |
| ChistaDev/Chista | framework | <https://github.com/ChistaDev/Chista> |
| Chocapikk/malware_analysis_react2shell | api-service | <https://github.com/Chocapikk/malware_analysis_react2shell> |
| ChrisBurkett/ClaudeStrike | dashboard | <https://github.com/ChrisBurkett/ClaudeStrike> |
| ChrisHuber1/KustoForge | web-platform | <https://github.com/ChrisHuber1/KustoForge> |
| christian-taillon/sunburst-hunting | research-project | <https://github.com/christian-taillon/sunburst-hunting> |
| christophetd/Adaz | directory | <https://github.com/christophetd/Adaz> |
| christophetd/mindmaps | tool | <https://github.com/christophetd/mindmaps> |
| cibervengadores/IOCs | tool | <https://github.com/cibervengadores/IOCs> |
| Cipherkrish69x/SOC-Analyst-Project | tool | <https://github.com/Cipherkrish69x/SOC-Analyst-Project> |
| Ciprian-LocalPulse/Umbra-Exchange | plugin | <https://github.com/Ciprian-LocalPulse/Umbra-Exchange> |
| CIRCL/circl-threat-intel-workshop | api-service | <https://github.com/CIRCL/circl-threat-intel-workshop> |
| ciscocsirt/GOSINT | framework | <https://github.com/ciscocsirt/GOSINT> |
| CityBaseInc/SIAC | research-project | <https://github.com/CityBaseInc/SIAC> |
| clayball/nector | tool | <https://github.com/clayball/nector> |
| clearvox/Callcontrol-Client | cli-tool | <https://github.com/clearvox/Callcontrol-Client> |
| CodeByHarri/Sigma2KQL | tool | <https://github.com/CodeByHarri/Sigma2KQL> |
| codewhitesec/apollon | tool | <https://github.com/codewhitesec/apollon> |
| codewhitesec/daphne | tool | <https://github.com/codewhitesec/daphne> |
| codeyourweb/hnuke | api-service | <https://github.com/codeyourweb/hnuke> |
| codeyourweb/irma | tool | <https://github.com/codeyourweb/irma> |
| codeyourweb/vt-rulesets-exporter | tool | <https://github.com/codeyourweb/vt-rulesets-exporter> |
| Condor2026/diabolic_france_v3 | api-service | <https://github.com/Condor2026/diabolic_france_v3> |
| Condor2026/INFORME-DE-INTELIGENCIA-DE-AMENAZAS-CIBERNETICAS-CTI-GLOBAL | tool | <https://github.com/Condor2026/INFORME-DE-INTELIGENCIA-DE-AMENAZAS-CIBERNETICAS-CTI-GLOBAL> |
| Condor2026/Nebula_AntiScan2 | api-service | <https://github.com/Condor2026/Nebula_AntiScan2> |
| Condor2026/Nexus_Osint_X | api-service | <https://github.com/Condor2026/Nexus_Osint_X> |
| Continuum-AI-Corp/Orca-AI-Incident-Archive | dataset | <https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive> |
| contivenv/Vault_tecnologias_guilherme | dashboard | <https://github.com/contivenv/Vault_tecnologias_guilherme> |
| ControlCompass/ControlCompass.github.io | tool | <https://github.com/ControlCompass/ControlCompass.github.io> |
| coolacid/docker-misp | container | <https://github.com/coolacid/docker-misp> |
| CooperCyberCoffee/opencti_mcp_server | tool | <https://github.com/CooperCyberCoffee/opencti_mcp_server> |
| Correia-jpv/fucking-awesome-malware-analysis | awesome-list | <https://github.com/Correia-jpv/fucking-awesome-malware-analysis> |
| cr4kn4x/the-stix-intern | framework | <https://github.com/cr4kn4x/the-stix-intern> |
| craciunoiuc/acs-homework-index | directory | <https://github.com/craciunoiuc/acs-homework-index> |
| crimson-crawler/python-sdk | api-service | <https://github.com/crimson-crawler/python-sdk> |
| crimsonvector/BPH_Research | dataset | <https://github.com/crimsonvector/BPH_Research> |
| CriticalPathSecurity/Public-Intelligence-Feeds | dataset | <https://github.com/CriticalPathSecurity/Public-Intelligence-Feeds> |
| CriticalPathSecurity/Zeek-Intelligence-Feeds | dataset | <https://github.com/CriticalPathSecurity/Zeek-Intelligence-Feeds> |
| crowdsecurity/crowdsec | container | <https://github.com/crowdsecurity/crowdsec> |
| CrowdStrike/MISP-tools | api-service | <https://github.com/CrowdStrike/MISP-tools> |
| csirtgadgets/bearded-avenger | research-project | <https://github.com/csirtgadgets/bearded-avenger> |
| csirtgadgets/csirtg-smrt-v1 | research-project | <https://github.com/csirtgadgets/csirtg-smrt-v1> |
| csirtgadgets/verbose-robot | research-project | <https://github.com/csirtgadgets/verbose-robot> |
| cti-brief/cti-brief.github.io | dataset | <https://github.com/cti-brief/cti-brief.github.io> |
| cti-cmm/framework | framework | <https://github.com/cti-cmm/framework> |
| ctinet/stixnet | api-service | <https://github.com/ctinet/stixnet> |
| ctitools/neurocti-small | tool | <https://github.com/ctitools/neurocti-small> |
| cudeso/misp-reporting | tool | <https://github.com/cudeso/misp-reporting> |
| curated-intel/Log4Shell-IOCs | cli-tool | <https://github.com/curated-intel/Log4Shell-IOCs> |
| curated-intel/Threat-Actor-Profile-Guide | dashboard | <https://github.com/curated-intel/Threat-Actor-Profile-Guide> |
| CuriosidadesDeHackers/MyThreatSuite | web-platform | <https://github.com/CuriosidadesDeHackers/MyThreatSuite> |
| CuriosidadesDeHackers/Telegram-Bot-para-Gestion-de-Indicadores-de-Compromiso-IOCs-y-CTI | tool | <https://github.com/CuriosidadesDeHackers/Telegram-Bot-para-Gestion-de-Indicadores-de-Compromiso-IOCs-y-CTI> |
| cwbae10-purdue/CTI-EACL24 | dataset | <https://github.com/cwbae10-purdue/CTI-EACL24> |
| Cyb3r-Monk/RITA-J | tool | <https://github.com/Cyb3r-Monk/RITA-J> |
| Cyb3r-Monk/Threat-Hunting-and-Detection | tool | <https://github.com/Cyb3r-Monk/Threat-Hunting-and-Detection> |
| cyb3rmik3/KQL-threat-hunting-queries | tool | <https://github.com/cyb3rmik3/KQL-threat-hunting-queries> |
| CYB3RMX/C2Data | dataset | <https://github.com/CYB3RMX/C2Data> |
| CYB3RMX/MalwareHashDB | dataset | <https://github.com/CYB3RMX/MalwareHashDB> |
| Cyb3rWard0g/HELK | container | <https://github.com/Cyb3rWard0g/HELK> |
| cyberblu3s/CyberBlue | container | <https://github.com/cyberblu3s/CyberBlue> |
| cybercrime-atlas/project-cosmos | tool | <https://github.com/cybercrime-atlas/project-cosmos> |
| CyberDataLab/disinfox | web-platform | <https://github.com/CyberDataLab/disinfox> |
| cyberdefenders/DetectionLabELK | tool | <https://github.com/cyberdefenders/DetectionLabELK> |
| CyberFlooD/DUDIX-CTI | tool | <https://github.com/CyberFlooD/DUDIX-CTI> |
| CyberFlooD/Evil-Domains | tool | <https://github.com/CyberFlooD/Evil-Domains> |
| Cyberfortress-Labs/Cyberfortress-IntelOwl-CTI | tool | <https://github.com/Cyberfortress-Labs/Cyberfortress-IntelOwl-CTI> |
| cyberphor/Spiritbox | plugin | <https://github.com/cyberphor/Spiritbox> |
| cyberprogramming1/GhostWire_CTI | web-platform | <https://github.com/cyberprogramming1/GhostWire_CTI> |
| cybersecify/OpenEASD | container | <https://github.com/cybersecify/OpenEASD> |
| cybersheepdog/Analyst-Tool | tool | <https://github.com/cybersheepdog/Analyst-Tool> |
| Cybersight-Security/URL-Analysis-Tool | web-platform | <https://github.com/Cybersight-Security/URL-Analysis-Tool> |
| cyberspacesec/apnic-skills | api-service | <https://github.com/cyberspacesec/apnic-skills> |
| cybledev/odin-sdk-go | api-service | <https://github.com/cybledev/odin-sdk-go> |
| cyc123456789/Tom-Magic | api-service | <https://github.com/cyc123456789/Tom-Magic> |
| CyCat-project/cycat-service | api-service | <https://github.com/CyCat-project/cycat-service> |
| cyentific-rni/misp-security-playbook-object | tool | <https://github.com/cyentific-rni/misp-security-playbook-object> |
| cyentific-rni/security-playbook-stix-misp-exchange | plugin | <https://github.com/cyentific-rni/security-playbook-stix-misp-exchange> |
| cyentific-rni/stix2.1-coa-playbook-extension | plugin | <https://github.com/cyentific-rni/stix2.1-coa-playbook-extension> |
| Cylvarkana/Cylvarkana-Django | research-project | <https://github.com/Cylvarkana/Cylvarkana-Django> |
| Cynthianfatkid/RookSIEM | tool | <https://github.com/Cynthianfatkid/RookSIEM> |
| cystack/stealer-fingerprints | directory | <https://github.com/cystack/stealer-fingerprints> |
| d3v-sh/d3m0n-agent | cli-tool | <https://github.com/d3v-sh/d3m0n-agent> |
| d3vFl0wlo/studious-tribble | tool | <https://github.com/d3vFl0wlo/studious-tribble> |
| D4-project/d4-core | cli-tool | <https://github.com/D4-project/d4-core> |
| D4-project/passive-ssh | tool | <https://github.com/D4-project/passive-ssh> |
| dalthunter/dalthunter | awesome-list | <https://github.com/dalthunter/dalthunter> |
| DamonMohammadbagher/ETWNetMonv3 | tool | <https://github.com/DamonMohammadbagher/ETWNetMonv3> |
| dandye/adk_runbooks | tool | <https://github.com/dandye/adk_runbooks> |
| dandye/ai-runbooks | tool | <https://github.com/dandye/ai-runbooks> |
| danieleperera/SocAnalystArsenal | framework | <https://github.com/danieleperera/SocAnalystArsenal> |
| DanPazlev/cti-hunt-loop-kit | tool | <https://github.com/DanPazlev/cti-hunt-loop-kit> |
| danzek/awesome-lol | awesome-list | <https://github.com/danzek/awesome-lol> |
| darkquasar/AIMOD2 | framework | <https://github.com/darkquasar/AIMOD2> |
| darkquasar/cybernethunter | research-project | <https://github.com/darkquasar/cybernethunter> |
| darses/cti | tool | <https://github.com/darses/cti> |
| DART-Laboratory/Flash-IDS | research-project | <https://github.com/DART-Laboratory/Flash-IDS> |
| DaSa7/deadband | web-platform | <https://github.com/DaSa7/deadband> |
| DashTX707/mena-detection-library | library | <https://github.com/DashTX707/mena-detection-library> |
| Data-Unix/MCP-MALTEGO | tool | <https://github.com/Data-Unix/MCP-MALTEGO> |
| dataaispark-spec/Hermes-Predictive-Attack-Paths-Detector | container | <https://github.com/dataaispark-spec/Hermes-Predictive-Attack-Paths-Detector> |
| databricks-industry-solutions/context-graph-analytics | tool | <https://github.com/databricks-industry-solutions/context-graph-analytics> |
| datosyciber/TFM | tool | <https://github.com/datosyciber/TFM> |
| davidonzo/apiosintDS | api-service | <https://github.com/davidonzo/apiosintDS> |
| davidonzo/Threat-Intel | api-service | <https://github.com/davidonzo/Threat-Intel> |
| davidquicast/vulnerability-intelligence-diagrammatic-reasoning | dataset | <https://github.com/davidquicast/vulnerability-intelligence-diagrammatic-reasoning> |
| davincico/Threat-Intel-Tools | tool | <https://github.com/davincico/Threat-Intel-Tools> |
| dboudreau00/BruceEDR-Framework | framework | <https://github.com/dboudreau00/BruceEDR-Framework> |
| dc401/optic-ioc | browser-extension | <https://github.com/dc401/optic-ioc> |
| deathlabs/deathlabs | tool | <https://github.com/deathlabs/deathlabs> |
| decal/werdlists | awesome-list | <https://github.com/decal/werdlists> |
| decoderloop/rust-malware-gallery | research-project | <https://github.com/decoderloop/rust-malware-gallery> |
| dedsec-terminal/greyfield | cli-tool | <https://github.com/dedsec-terminal/greyfield> |
| deepfield/public-research | research-project | <https://github.com/deepfield/public-research> |
| DeepTempo/socbench | tool | <https://github.com/DeepTempo/socbench> |
| deeztek/Hermes-Secure-Email-Gateway | container | <https://github.com/deeztek/Hermes-Secure-Email-Gateway> |
| defend.network | directory | <https://defend.network> |
| Delaldincer/timeline-cti-explorer | api-service | <https://github.com/Delaldincer/timeline-cti-explorer> |
| DeltaZulu-OU/MispConnectorApp | plugin | <https://github.com/DeltaZulu-OU/MispConnectorApp> |
| Dentrax/falco-gpt | container | <https://github.com/Dentrax/falco-gpt> |
| depalmar/ai_for_the_win | container | <https://github.com/depalmar/ai_for_the_win> |
| dessertlab/cti-to-mitre-with-nlp | research-project | <https://github.com/dessertlab/cti-to-mitre-with-nlp> |
| dev-lu/osint_toolkit | web-platform | <https://github.com/dev-lu/osint_toolkit> |
| Dev-next-gen/orodruin | api-service | <https://github.com/Dev-next-gen/orodruin> |
| devikakumawat8/threat-intel-reports | tool | <https://github.com/devikakumawat8/threat-intel-reports> |
| devops-ia/helm-opencti | container | <https://github.com/devops-ia/helm-opencti> |
| devsecops/awesome-devsecops | awesome-list | <https://github.com/devsecops/awesome-devsecops> |
| dferrell30/Defender-KQL-Playbook | tool | <https://github.com/dferrell30/Defender-KQL-Playbook> |
| dfirtnt/Huntable-CTI-Studio | api-service | <https://github.com/dfirtnt/Huntable-CTI-Studio> |
| dgunter/Blog-Code | tool | <https://github.com/dgunter/Blog-Code> |
| dgunter/ParseZeekLogs | tool | <https://github.com/dgunter/ParseZeekLogs> |
| Dhruv00098/sherlock | tool | <https://github.com/Dhruv00098/sherlock> |
| digisquad-repo/digi-magnet | tool | <https://github.com/digisquad-repo/digi-magnet> |
| digisquad-repo/kunai-rules | tool | <https://github.com/digisquad-repo/kunai-rules> |
| Digital Shadows SearchLight | web-platform | <https://www.reliaquest.com> |
| dinosn/security-knowledge-base | cli-tool | <https://github.com/dinosn/security-knowledge-base> |
| disc0nct/Open-Source-Dockerized-SOC | container | <https://github.com/disc0nct/Open-Source-Dockerized-SOC> |
| djkurlander/knock-knock | container | <https://github.com/djkurlander/knock-knock> |
| Dmmalveaux/CyberSecurity-Projects | tool | <https://github.com/Dmmalveaux/CyberSecurity-Projects> |
| DNSBunker/CTI | cli-tool | <https://github.com/DNSBunker/CTI> |
| docintelapp/DocIntel | web-platform | <https://github.com/docintelapp/DocIntel> |
| domainsi/Garuda-ssh | plugin | <https://github.com/domainsi/Garuda-ssh> |
| DomainTools/DomainCAT | tool | <https://github.com/DomainTools/DomainCAT> |
| DotX-47/Live_Monitor | tool | <https://github.com/DotX-47/Live_Monitor> |
| DotX-47/Password_Checker | tool | <https://github.com/DotX-47/Password_Checker> |
| dragnet-dev/dragnet | dataset | <https://github.com/dragnet-dev/dragnet> |
| drb-ra/C2IntelFeeds | dataset | <https://github.com/drb-ra/C2IntelFeeds> |
| Dread Scraper | dataset | <https://github.com/NPCmillionaire/dread-scraper> |
| DreadFog/OpenFraudMonitoring | web-platform | <https://github.com/DreadFog/OpenFraudMonitoring> |
| drneox/nutcracker | framework | <https://github.com/drneox/nutcracker> |
| duggytuxy/Data-Shield_IPv4_Blocklist | web-platform | <https://github.com/duggytuxy/Data-Shield_IPv4_Blocklist> |
| dvrone/tg-cyberkit | framework | <https://github.com/dvrone/tg-cyberkit> |
| DXC-0/open-eve-dashboard | container | <https://github.com/DXC-0/open-eve-dashboard> |
| DXC-0/soc-ressources | tool | <https://github.com/DXC-0/soc-ressources> |
| Ebryx/aws-threathunting | tool | <https://github.com/Ebryx/aws-threathunting> |
| echelongraph/echelongraph-mcp | dashboard | <https://github.com/echelongraph/echelongraph-mcp> |
| EclecticIQ Intelligence Center | web-platform | <https://www.eclecticiq.com> |
| eclecticiq/cabby | cli-tool | <https://github.com/eclecticiq/cabby> |
| eclecticiq/git4intel | tool | <https://github.com/eclecticiq/git4intel> |
| eclecticiq/OpenTAXII | tool | <https://github.com/eclecticiq/OpenTAXII> |
| eclecticiq/stix-icons | tool | <https://github.com/eclecticiq/stix-icons> |
| ecstatic-nobel/Analyst-Arsenal | framework | <https://github.com/ecstatic-nobel/Analyst-Arsenal> |
| ecstatic-nobel/pOSINT | cli-tool | <https://github.com/ecstatic-nobel/pOSINT> |
| Edi-San24/ioc-reputation-scorer | tool | <https://github.com/Edi-San24/ioc-reputation-scorer> |
| edoardogerosa/delator | tool | <https://github.com/edoardogerosa/delator> |
| edoardogerosa/dnsmorph | tool | <https://github.com/edoardogerosa/dnsmorph> |
| edoardogerosa/sentinel-attack | api-service | <https://github.com/edoardogerosa/sentinel-attack> |
| edoardottt/defangjs | library | <https://github.com/edoardottt/defangjs> |
| EfstratiosLontzetidis/misp-tweetfeed-integration | plugin | <https://github.com/EfstratiosLontzetidis/misp-tweetfeed-integration> |
| EfstratiosLontzetidis/pythia | tool | <https://github.com/EfstratiosLontzetidis/pythia> |
| EfstratiosLontzetidis/WhatHitMe | tool | <https://github.com/EfstratiosLontzetidis/WhatHitMe> |
| Einsteinium01/Intrusion-Detection-System | dashboard | <https://github.com/Einsteinium01/Intrusion-Detection-System> |
| elastic/detection-rules | tool | <https://github.com/elastic/detection-rules> |
| elastic/securitylabs-thrunting-tools | cli-tool | <https://github.com/elastic/securitylabs-thrunting-tools> |
| Elemental-attack/Elemental | library | <https://github.com/Elemental-attack/Elemental> |
| ElkinStas/cti-multi-agent | container | <https://github.com/ElkinStas/cti-multi-agent> |
| elvidence/MISP | api-service | <https://github.com/elvidence/MISP> |
| emalderson/ThePhish | tool | <https://github.com/emalderson/ThePhish> |
| emirmorgan/mui-dashboard | dashboard | <https://github.com/emirmorgan/mui-dashboard> |
| emmanuelgjr/genai_incidents | dataset | <https://github.com/emmanuelgjr/genai_incidents> |
| EmreEkinci1/Naga | api-service | <https://github.com/EmreEkinci1/Naga> |
| emrekybs/Douglas-042 | web-platform | <https://github.com/emrekybs/Douglas-042> |
| en3ra/cyber-incident-analysis | research-project | <https://github.com/en3ra/cyber-incident-analysis> |
| EndlessFractal/Threat-Intel-Feed | dataset | <https://github.com/EndlessFractal/Threat-Intel-Feed> |
| Enlightenism/IronClaw-Security | web-platform | <https://github.com/Enlightenism/IronClaw-Security> |
| erenguvensec/RepChecker | api-service | <https://github.com/erenguvensec/RepChecker> |
| eric-sabe/honey | cli-tool | <https://github.com/eric-sabe/honey> |
| erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary | dataset | <https://github.com/erickatwork/CrowdStrike-Falcon-Events-Data-Dictionary> |
| eris-ot/marlinspike | container | <https://github.com/eris-ot/marlinspike> |
| ErTapanJatakia/ORVIKA | tool | <https://github.com/ErTapanJatakia/ORVIKA> |
| eschultze/phishstats-api-network | api-service | <https://github.com/eschultze/phishstats-api-network> |
| Eshan00/Phisher-Fisher | plugin | <https://github.com/Eshan00/Phisher-Fisher> |
| eshlomo1/Microsoft-Sentinel-SecOps | tool | <https://github.com/eshlomo1/Microsoft-Sentinel-SecOps> |
| esoadamo/micro-cti | api-service | <https://github.com/esoadamo/micro-cti> |
| espyerx-x/Shodan-and-Censys-automation | api-service | <https://github.com/espyerx-x/Shodan-and-Censys-automation> |
| ethack/tht | container | <https://github.com/ethack/tht> |
| Ethan-Andrews/Exploitarium-Detections | research-project | <https://github.com/Ethan-Andrews/Exploitarium-Detections> |
| Ethan-Andrews/ThreatIntel-Aggregator | api-service | <https://github.com/Ethan-Andrews/ThreatIntel-Aggregator> |
| EvoluxBR/greenswitch | plugin | <https://github.com/EvoluxBR/greenswitch> |
| Excalibra/corporate-information-confidentiality-security-check-manual | tool | <https://github.com/Excalibra/corporate-information-confidentiality-security-check-manual> |
| ez3r0sec/JamfProThreatHunting | tool | <https://github.com/ez3r0sec/JamfProThreatHunting> |
| f-bader/DefenderAndSentinelQueries | tool | <https://github.com/f-bader/DefenderAndSentinelQueries> |
| fabriziosalmi/wildbox | container | <https://github.com/fabriziosalmi/wildbox> |
| Fadavvi/Yara-Repo | tool | <https://github.com/Fadavvi/Yara-Repo> |
| fagner-fmlo/cybersysbr-research | research-project | <https://github.com/fagner-fmlo/cybersysbr-research> |
| faisalusuf/ThreatIntelligence | tool | <https://github.com/faisalusuf/ThreatIntelligence> |
| Faizan-Khanx/SQL-CommandGenerator | web-platform | <https://github.com/Faizan-Khanx/SQL-CommandGenerator> |
| fareedfauzi/MANTIS | tool | <https://github.com/fareedfauzi/MANTIS> |
| febrezo/spuc | cli-tool | <https://github.com/febrezo/spuc> |
| febrezo/stix4rust | tool | <https://github.com/febrezo/stix4rust> |
| felixkoch/TheDialer | plugin | <https://github.com/felixkoch/TheDialer> |
| feromirdanton-ui/Operation-CloudFix-ClickFix-Malware | cli-tool | <https://github.com/feromirdanton-ui/Operation-CloudFix-ClickFix-Malware> |
| FFraud-com/ip-fraud-database | api-service | <https://github.com/FFraud-com/ip-fraud-database> |
| fhightower/ioc-finder | research-project | <https://github.com/fhightower/ioc-finder> |
| filipi86/Threat-Hunting | research-project | <https://github.com/filipi86/Threat-Hunting> |
| filippofinke/infectio | tool | <https://github.com/filippofinke/infectio> |
| FIRSTdotorg/automation-sig-www | tool | <https://github.com/FIRSTdotorg/automation-sig-www> |
| fish-not-phish/ttpnav | library | <https://github.com/fish-not-phish/ttpnav> |
| flatmarstheory/Cyber-Newsroom-Public | dataset | <https://github.com/flatmarstheory/Cyber-Newsroom-Public> |
| Flowtriq/ftagent-lite | tool | <https://github.com/Flowtriq/ftagent-lite> |
| FNBIP/aegis-osint-map | directory | <https://github.com/FNBIP/aegis-osint-map> |
| format81/TI-Mindmap-GPT | api-service | <https://github.com/format81/TI-Mindmap-GPT> |
| Fortiguard Labs | tool | <https://fortiguard.fortinet.com/threat-map> |
| FortiGuard Labs | tool | <https://www.fortiguard.com/threat-actor> |
| fox-it/cobaltstrike-beacon-data | dataset | <https://github.com/fox-it/cobaltstrike-beacon-data> |
| fr0gger/jupyter-collection | tool | <https://github.com/fr0gger/jupyter-collection> |
| fr3dux/dark-threat-radar | api-service | <https://github.com/fr3dux/dark-threat-radar> |
| francoisfried/Defender-Advanced-Hunting-Queries | framework | <https://github.com/francoisfried/Defender-Advanced-Hunting-Queries> |
| frangelbarrera/aegistrace-threat-intelligence | dashboard | <https://github.com/frangelbarrera/aegistrace-threat-intelligence> |
| freetaxii/testlab | tool | <https://github.com/freetaxii/testlab> |
| FrenchEthicalsHackers/WebScanner | api-service | <https://github.com/FrenchEthicalsHackers/WebScanner> |
| FrenchEthicalsHackers/WSL-KaliLinux-AutoInstaller | web-platform | <https://github.com/FrenchEthicalsHackers/WSL-KaliLinux-AutoInstaller> |
| frknaykc/DragonsEye-RansomwareTracker | api-service | <https://github.com/frknaykc/DragonsEye-RansomwareTracker> |
| fukusuket/THuntLab | container | <https://github.com/fukusuket/THuntLab> |
| furk4n0zturk/MachinePreparer | tool | <https://github.com/furk4n0zturk/MachinePreparer> |
| fyankov96/agentic-soc-analyst | plugin | <https://github.com/fyankov96/agentic-soc-analyst> |
| G4rb3n/SOC-Copilot | tool | <https://github.com/G4rb3n/SOC-Copilot> |
| GACWR/ouba-paper | research-project | <https://github.com/GACWR/ouba-paper> |
| GainSec/LeakScope | web-platform | <https://github.com/GainSec/LeakScope> |
| galile0ff/galileoff-AndroidSpy | api-service | <https://github.com/galile0ff/galileoff-AndroidSpy> |
| galile0ff/galileoff-OnionScraper | api-service | <https://github.com/galile0ff/galileoff-OnionScraper> |
| galile0ff/galileoff-WebScraper | api-service | <https://github.com/galile0ff/galileoff-WebScraper> |
| gameworkerkim/CYBER-THREAT-INTELLIGENCE-REPORT | tool | <https://github.com/gameworkerkim/CYBER-THREAT-INTELLIGENCE-REPORT> |
| gariiuu/lain | dashboard | <https://github.com/gariiuu/lain> |
| Garyson26/Wiestell_threatIntel_platform | web-platform | <https://github.com/Garyson26/Wiestell_threatIntel_platform> |
| gaut1ham/Network_Security_Tools | tool | <https://github.com/gaut1ham/Network_Security_Tools> |
| gbikram/OSINT-Explorer-Website | tool | <https://github.com/gbikram/OSINT-Explorer-Website> |
| gcrahay/otx_misp | research-project | <https://github.com/gcrahay/otx_misp> |
| Geekmaster-General/IOCs | tool | <https://github.com/Geekmaster-General/IOCs> |
| gensecaihq/Wazuh-Autopilot | container | <https://github.com/gensecaihq/Wazuh-Autopilot> |
| gensecaihq/Wazuh-MCP-Server | tool | <https://github.com/gensecaihq/Wazuh-MCP-Server> |
| ger1e/para11ax | tool | <https://github.com/ger1e/para11ax> |
| ger1e/personal-site-lp | tool | <https://github.com/ger1e/personal-site-lp> |
| gertjanbruggink/metrics | directory | <https://github.com/gertjanbruggink/metrics> |
| gertjanbruggink/threat-landscape-training-corpus | directory | <https://github.com/gertjanbruggink/threat-landscape-training-corpus> |
| Ghost0Mod3/trash_panda_usb | plugin | <https://github.com/Ghost0Mod3/trash_panda_usb> |
| GhostTroops/scan4all | awesome-list | <https://github.com/GhostTroops/scan4all> |
| GiTaDi-CrEaTe/zero-log | cli-tool | <https://github.com/GiTaDi-CrEaTe/zero-log> |
| GitGuardian - Public GitHub Monitoring | tool | <https://www.gitguardian.com/monitor-public-github-for-secrets> |
| githubfoam/ELK-sandbox | tool | <https://github.com/githubfoam/ELK-sandbox> |
| githubfoam/osquery-sandbox | tool | <https://github.com/githubfoam/osquery-sandbox> |
| githubfoam/suricata-sandbox | tool | <https://github.com/githubfoam/suricata-sandbox> |
| githubfoam/zeek-sandbox | tool | <https://github.com/githubfoam/zeek-sandbox> |
| gl0bal01/malware-analysis-claude-skills | framework | <https://github.com/gl0bal01/malware-analysis-claude-skills> |
| gmagklaras/POFR | dashboard | <https://github.com/gmagklaras/POFR> |
| goal31121/MoRSE-AI | tool | <https://github.com/goal31121/MoRSE-AI> |
| GodwillFoka/cyberillsec-illwatch | api-service | <https://github.com/GodwillFoka/cyberillsec-illwatch> |
| GokbakarE/RuleSetRAT | research-project | <https://github.com/GokbakarE/RuleSetRAT> |
| GONZOsint/pywhatcms | api-service | <https://github.com/GONZOsint/pywhatcms> |
| google/mcp-security | tool | <https://github.com/google/mcp-security> |
| google/threat-team | tool | <https://github.com/google/threat-team> |
| gorkemguler/trackactor | api-service | <https://github.com/gorkemguler/trackactor> |
| GossiTheDog/ThreatHunting | tool | <https://github.com/GossiTheDog/ThreatHunting> |
| gpplabs/threat-actor-index | directory | <https://github.com/gpplabs/threat-actor-index> |
| GreedyBear-Project/GreedyBear | web-platform | <https://github.com/GreedyBear-Project/GreedyBear> |
| grepstrength/GoVettersTools | api-service | <https://github.com/grepstrength/GoVettersTools> |
| grepstrength/malsnitch | api-service | <https://github.com/grepstrength/malsnitch> |
| GreyNoise-Intelligence/pygreynoise | library | <https://github.com/GreyNoise-Intelligence/pygreynoise> |
| gripebomb/ThreatDeck | web-platform | <https://github.com/gripebomb/ThreatDeck> |
| GurukiranShiv/Threat-Intel-Graph-Platform | container | <https://github.com/GurukiranShiv/Threat-Intel-Graph-Platform> |
| H3llKa1ser/SOC-Assistant-Guide | dashboard | <https://github.com/H3llKa1ser/SOC-Assistant-Guide> |
| H3NRYBAIT/threatpivot | container | <https://github.com/H3NRYBAIT/threatpivot> |
| h4m5t/SecNotes | tool | <https://github.com/h4m5t/SecNotes> |
| h4m5t/VulnAlert | tool | <https://github.com/h4m5t/VulnAlert> |
| h4vox/PlanqX_EDR-Endpoint-Detection-and-Response | plugin | <https://github.com/h4vox/PlanqX_EDR-Endpoint-Detection-and-Response> |
| hackerman70000/apt-reports | tool | <https://github.com/hackerman70000/apt-reports> |
| HackingLZ/svg_phishing_tools | research-project | <https://github.com/HackingLZ/svg_phishing_tools> |
| had-nu/brimmed-hat | dataset | <https://github.com/had-nu/brimmed-hat> |
| hamhus/USD-CTI-Listener | plugin | <https://github.com/hamhus/USD-CTI-Listener> |
| haooah01/Hyper-Interacting-MORE---Code-Reverside-Intelligence-2In1 | tool | <https://github.com/haooah01/Hyper-Interacting-MORE---Code-Reverside-Intelligence-2In1> |
| HaoY-l/threat-intel-hub | tool | <https://github.com/HaoY-l/threat-intel-hub> |
| harvard-itsecurity/docker-misp | container | <https://github.com/harvard-itsecurity/docker-misp> |
| Haseeb-1698/CyberPulse | dashboard | <https://github.com/Haseeb-1698/CyberPulse> |
| hashlookup/hashlookup-gui | dashboard | <https://github.com/hashlookup/hashlookup-gui> |
| Hatchepsoute/sigma-rules | tool | <https://github.com/Hatchepsoute/sigma-rules> |
| hedgerow-dev/coldframe | tool | <https://github.com/hedgerow-dev/coldframe> |
| hejsoftware/cti-plugin-ts-starter | plugin | <https://github.com/hejsoftware/cti-plugin-ts-starter> |
| helixmap/sigwood | tool | <https://github.com/helixmap/sigwood> |
| henriqclaro/INI3A-EQ2 | tool | <https://github.com/henriqclaro/INI3A-EQ2> |
| hernannh/ipflame | plugin | <https://github.com/hernannh/ipflame> |
| hernic/JTypoSquatting | dashboard | <https://github.com/hernic/JTypoSquatting> |
| himanshu76-cyber/Cybersecurity-Risk-Assessment-SME | framework | <https://github.com/himanshu76-cyber/Cybersecurity-Risk-Assessment-SME> |
| Himilp/Open-Source-SOC | tool | <https://github.com/Himilp/Open-Source-SOC> |
| hm-seclab/YAFRA | framework | <https://github.com/hm-seclab/YAFRA> |
| hnsh3in/threat-intel-digest | container | <https://github.com/hnsh3in/threat-intel-digest> |
| Homas/ioc2rpz | dataset | <https://github.com/Homas/ioc2rpz> |
| hookprobe/hookprobe | tool | <https://github.com/hookprobe/hookprobe> |
| hpthreatresearch/subcrawl | plugin | <https://github.com/hpthreatresearch/subcrawl> |
| https://eauction.ge | web-platform | <https://eauction.ge> |
| https://nbe.gov.ge | web-platform | <https://nbe.gov.ge> |
| Hugh-Kumbi/Operation-Phantom-Store | tool | <https://github.com/Hugh-Kumbi/Operation-Phantom-Store> |
| Hugo-C/rustJarm | tool | <https://github.com/Hugo-C/rustJarm> |
| Hunt3r0x/inficted | tool | <https://github.com/Hunt3r0x/inficted> |
| huntbase-io/hunt-md | tool | <https://github.com/huntbase-io/hunt-md> |
| HuntDownProject/KoodousFinder | mobile-app | <https://github.com/HuntDownProject/KoodousFinder> |
| huoji120/DuckSysEye | tool | <https://github.com/huoji120/DuckSysEye> |
| i-hmzakhan/Aegis-AI | dataset | <https://github.com/i-hmzakhan/Aegis-AI> |
| Iankulani/acd-sub | plugin | <https://github.com/Iankulani/acd-sub> |
| Iankulani/awesome-grizzly | awesome-list | <https://github.com/Iankulani/awesome-grizzly> |
| Iankulani/awesome_cyclopus | awesome-list | <https://github.com/Iankulani/awesome_cyclopus> |
| Iankulani/awesome_okapi | awesome-list | <https://github.com/Iankulani/awesome_okapi> |
| Iankulani/cyclopus | api-service | <https://github.com/Iankulani/cyclopus> |
| Iankulani/hermit-crab-v1 | research-project | <https://github.com/Iankulani/hermit-crab-v1> |
| Iankulani/lynx_spider | web-platform | <https://github.com/Iankulani/lynx_spider> |
| Iankulani/network-ultimate-eye-doc | tool | <https://github.com/Iankulani/network-ultimate-eye-doc> |
| Iankulani/power_shark | container | <https://github.com/Iankulani/power_shark> |
| Iankulani/rebellion_bot | api-service | <https://github.com/Iankulani/rebellion_bot> |
| Iankulani/super_crab_v1 | web-platform | <https://github.com/Iankulani/super_crab_v1> |
| Iankulani/war-crab-v2 | research-project | <https://github.com/Iankulani/war-crab-v2> |
| Iankulani/war-shark-v1 | web-platform | <https://github.com/Iankulani/war-shark-v1> |
| Iankulani/war_squid | research-project | <https://github.com/Iankulani/war_squid> |
| IBM X-Force Exchange Current Malicious Activity | tool | <https://exchange.xforce.ibmcloud.com/activity/map> |
| ibnaleem/amaterasu | tool | <https://github.com/ibnaleem/amaterasu> |
| ibnaleem/peoxide | library | <https://github.com/ibnaleem/peoxide> |
| ibnaleem/vtscan | api-service | <https://github.com/ibnaleem/vtscan> |
| ibu-cyx0/CTI-Automation-Platform | dashboard | <https://github.com/ibu-cyx0/CTI-Automation-Platform> |
| ictinnovations/asterisk-ami-node | cli-tool | <https://github.com/ictinnovations/asterisk-ami-node> |
| ictinnovations/freeswitch-esl-node | api-service | <https://github.com/ictinnovations/freeswitch-esl-node> |
| ictinnovations/ictagent | browser-extension | <https://github.com/ictinnovations/ictagent> |
| ictinnovations/ictcore | api-service | <https://github.com/ictinnovations/ictcore> |
| ictinnovations/ictcrm | plugin | <https://github.com/ictinnovations/ictcrm> |
| id-cpe/public | api-service | <https://github.com/id-cpe/public> |
| idiljot-singh/Stenwatch | tool | <https://github.com/idiljot-singh/Stenwatch> |
| ihebski/ioc_extractor | web-platform | <https://github.com/ihebski/ioc_extractor> |
| Ilesnat/n8n_cyber_intel | tool | <https://github.com/Ilesnat/n8n_cyber_intel> |
| ilostmypassword/Melissae-Honeypot-Framework | container | <https://github.com/ilostmypassword/Melissae-Honeypot-Framework> |
| Incognito-User/CTI-Tooling | dashboard | <https://github.com/Incognito-User/CTI-Tooling> |
| ine-labs/ThreatSeeker | tool | <https://github.com/ine-labs/ThreatSeeker> |
| Infinit3i/hunt-ai | research-project | <https://github.com/Infinit3i/hunt-ai> |
| Infinitum-IT/IOAs | web-platform | <https://github.com/Infinitum-IT/IOAs> |
| infinitumitlabs/Karakurt-Hacking-Team-CTI | tool | <https://github.com/infinitumitlabs/Karakurt-Hacking-Team-CTI> |
| infosecn1nja/TTPMapper | tool | <https://github.com/infosecn1nja/TTPMapper> |
| innowaluza/Patch-Pulse | desktop-app | <https://github.com/innowaluza/Patch-Pulse> |
| inodee/threathunting-spl | tool | <https://github.com/inodee/threathunting-spl> |
| InQuest/yara-rules | tool | <https://github.com/InQuest/yara-rules> |
| intelowlproject/go-intelowl | api-service | <https://github.com/intelowlproject/go-intelowl> |
| intelowlproject/IntelOwl-ng | research-project | <https://github.com/intelowlproject/IntelOwl-ng> |
| interplains/zero-breach | tool | <https://github.com/interplains/zero-breach> |
| interprobe/IoCData | dataset | <https://github.com/interprobe/IoCData> |
| inthecyber-group/securityonion-n8n-workflows | tool | <https://github.com/inthecyber-group/securityonion-n8n-workflows> |
| IntSights | api-service | <https://intsights.com> |
| iocx-dev/iocx | cli-tool | <https://github.com/iocx-dev/iocx> |
| iomoath/file_watchtower | tool | <https://github.com/iomoath/file_watchtower> |
| iomoath/yara-scanner | tool | <https://github.com/iomoath/yara-scanner> |
| ION28/BLUESPAWN | tool | <https://github.com/ION28/BLUESPAWN> |
| IsaacAtunbi15/threatsift | cli-tool | <https://github.com/IsaacAtunbi15/threatsift> |
| ishandutta2007/Awesome-Digital-Risk-Protection | awesome-list | <https://github.com/ishandutta2007/Awesome-Digital-Risk-Protection> |
| ishandutta2007/Awesome-Threat-Intelligence-Platform | awesome-list | <https://github.com/ishandutta2007/Awesome-Threat-Intelligence-Platform> |
| IterateAI/OpenThreatDetection | tool | <https://github.com/IterateAI/OpenThreatDetection> |
| itshamzabendelladj/AIGuardSIEM | container | <https://github.com/itshamzabendelladj/AIGuardSIEM> |
| ivan-sincek/chad | tool | <https://github.com/ivan-sincek/chad> |
| ivan-sincek/domain-extractor | research-project | <https://github.com/ivan-sincek/domain-extractor> |
| ivan-sincek/memory-dumper | research-project | <https://github.com/ivan-sincek/memory-dumper> |
| ivan-sincek/nagooglesearch | tool | <https://github.com/ivan-sincek/nagooglesearch> |
| IviweNomzaza/Security-Orchestration-Automation-Response | tool | <https://github.com/IviweNomzaza/Security-Orchestration-Automation-Response> |
| ivre/obsidian-ivre-plugin | plugin | <https://github.com/ivre/obsidian-ivre-plugin> |
| izm1chael/Anomy | research-project | <https://github.com/izm1chael/Anomy> |
| j4ckrisz/Hackzzz | research-project | <https://github.com/j4ckrisz/Hackzzz> |
| Jack-McDowell/DEEPGLASS | tool | <https://github.com/Jack-McDowell/DEEPGLASS> |
| jackaduma/SecBERT | tool | <https://github.com/jackaduma/SecBERT> |
| jackaduma/ThreatReportExtractor | tool | <https://github.com/jackaduma/ThreatReportExtractor> |
| JacobDicksonOfficial/Network-Forensics-IDS | tool | <https://github.com/JacobDicksonOfficial/Network-Forensics-IDS> |
| jacobdjwilson/awesome-annual-security-reports | awesome-list | <https://github.com/jacobdjwilson/awesome-annual-security-reports> |
| jacobstickney/ThreatActorProcedures-MITRE-ATTACK | framework | <https://github.com/jacobstickney/ThreatActorProcedures-MITRE-ATTACK> |
| Jacox98/n8n-nodes-ransomware-live | api-service | <https://github.com/Jacox98/n8n-nodes-ransomware-live> |
| jakub/dumper | research-project | <https://github.com/jakub/dumper> |
| Jam0k/Public-Feeds-IOCs | dataset | <https://github.com/Jam0k/Public-Feeds-IOCs> |
| Jam0k/threatcluster-digest | tool | <https://github.com/Jam0k/threatcluster-digest> |
| jameschrisa/cyberthreat-research | research-project | <https://github.com/jameschrisa/cyberthreat-research> |
| janennacircumpolar374/repo-intel | awesome-list | <https://github.com/janennacircumpolar374/repo-intel> |
| jaskeerat01/darkweb-scraper | tool | <https://github.com/jaskeerat01/darkweb-scraper> |
| jasonsford/intel_collector | library | <https://github.com/jasonsford/intel_collector> |
| JavierMun/WhoIsWhoAPT | tool | <https://github.com/JavierMun/WhoIsWhoAPT> |
| jegly/globalcve | web-platform | <https://github.com/jegly/globalcve> |
| JethroPhuah/CTI-Agent-Project | web-platform | <https://github.com/JethroPhuah/CTI-Agent-Project> |
| jgamblin/isthisipbad | dataset | <https://github.com/jgamblin/isthisipbad> |
| jh00nbr/Phishruffus | tool | <https://github.com/jh00nbr/Phishruffus> |
| jingkang99/bloglinks | research-project | <https://github.com/jingkang99/bloglinks> |
| JiscCTI/misp-docker | container | <https://github.com/JiscCTI/misp-docker> |
| jischell-msft/RemoteManagementMonitoringTools | research-project | <https://github.com/jischell-msft/RemoteManagementMonitoringTools> |
| JMousqueton/CTI-Teams-Notification | tool | <https://github.com/JMousqueton/CTI-Teams-Notification> |
| JMousqueton/DNS-Spy | cli-tool | <https://github.com/JMousqueton/DNS-Spy> |
| JMousqueton/honeypot-attack-map | tool | <https://github.com/JMousqueton/honeypot-attack-map> |
| JMousqueton/IoCManager | web-platform | <https://github.com/JMousqueton/IoCManager> |
| JMousqueton/OpenCTI-Docker | container | <https://github.com/JMousqueton/OpenCTI-Docker> |
| JMousqueton/RiskAnalyzer-The-Quizz | tool | <https://github.com/JMousqueton/RiskAnalyzer-The-Quizz> |
| joeavanzato/LogBoost | tool | <https://github.com/joeavanzato/LogBoost> |
| jonas-koeritz/asterisk-csp | web-platform | <https://github.com/jonas-koeritz/asterisk-csp> |
| jonathan6661/P1sty | tool | <https://github.com/jonathan6661/P1sty> |
| jonrau1/SyntheticSun | web-platform | <https://github.com/jonrau1/SyntheticSun> |
| JosephAwana23/Ghost-Aegis-SE | tool | <https://github.com/JosephAwana23/Ghost-Aegis-SE> |
| joshuagodwin7929/Purple-Team-Automation | directory | <https://github.com/joshuagodwin7929/Purple-Team-Automation> |
| JPCERTCC/YAMAGoya | tool | <https://github.com/JPCERTCC/YAMAGoya> |
| jstnk9/MISP | tool | <https://github.com/jstnk9/MISP> |
| Jul10l1r4/X-force | library | <https://github.com/Jul10l1r4/X-force> |
| julioliraup/Antiphishing | tool | <https://github.com/julioliraup/Antiphishing> |
| justin-lyon/sf-five9-subscriber | api-service | <https://github.com/justin-lyon/sf-five9-subscriber> |
| jwashek/TTPMap | cli-tool | <https://github.com/jwashek/TTPMap> |
| jwashek/veCTIon | tool | <https://github.com/jwashek/veCTIon> |
| jymcheong/SysmonResources | tool | <https://github.com/jymcheong/SysmonResources> |
| kaaaanoooo/local-ioc-db | dataset | <https://github.com/kaaaanoooo/local-ioc-db> |
| kaansk/Go-MISPFeedGenerator | api-service | <https://github.com/kaansk/Go-MISPFeedGenerator> |
| kaiiyer/rajappan | framework | <https://github.com/kaiiyer/rajappan> |
| Karneades/awesome-malware-persistence | awesome-list | <https://github.com/Karneades/awesome-malware-persistence> |
| Karneades/malware-persistence | tool | <https://github.com/Karneades/malware-persistence> |
| karthikkbala/MISP-QRadar-Integration | plugin | <https://github.com/karthikkbala/MISP-QRadar-Integration> |
| kasiakicler/ai-cyber-risk-intelligence | dashboard | <https://github.com/kasiakicler/ai-cyber-risk-intelligence> |
| KasperskyLab/threat-intelligence | plugin | <https://github.com/KasperskyLab/threat-intelligence> |
| Kathayra/HT-Trackr | tool | <https://github.com/Kathayra/HT-Trackr> |
| katochnitish/MRCI-Preproc | tool | <https://github.com/katochnitish/MRCI-Preproc> |
| kaua-silbershlach-parodes/a-elite-estrangeira-ids | tool | <https://github.com/kaua-silbershlach-parodes/a-elite-estrangeira-ids> |
| kawaiipantsu/ransomwatch | container | <https://github.com/kawaiipantsu/ransomwatch> |
| KC7-Foundation/kc7 | tool | <https://github.com/KC7-Foundation/kc7> |
| KevinCyberz/Kevin-cyber-Tech-Services | web-platform | <https://github.com/KevinCyberz/Kevin-cyber-Tech-Services-> |
| kevinmhorvath/threat-intel-toolkit | api-service | <https://github.com/kevinmhorvath/threat-intel-toolkit> |
| keyokemona/purple-team | tool | <https://github.com/keyokemona/purple-team> |
| KeysGuard/KeysGuardQ | tool | <https://github.com/KeysGuard/KeysGuardQ> |
| kh4sh3i/Cyber-Threat-Hunting | awesome-list | <https://github.com/kh4sh3i/Cyber-Threat-Hunting> |
| khalil-b1/goosint | tool | <https://github.com/khalil-b1/goosint> |
| khalil-b1/goosint-cyber-news | awesome-list | <https://github.com/khalil-b1/goosint-cyber-news> |
| khutsosandlana/khutsosandlana | tool | <https://github.com/khutsosandlana/khutsosandlana> |
| kienmarkdo/Telegram-OSINT-for-Cyber-Threat-Intelligence-Analysis | tool | <https://github.com/kienmarkdo/Telegram-OSINT-for-Cyber-Threat-Intelligence-Analysis> |
| KillahPotatoes/KP-Liberation | tool | <https://github.com/KillahPotatoes/KP-Liberation> |
| kim-kimani/burpsuite-ai-pentest-extension | plugin | <https://github.com/kim-kimani/burpsuite-ai-pentest-extension> |
| Kim-San04/threat-intel-dashboard | container | <https://github.com/Kim-San04/threat-intel-dashboard> |
| kimburkeanalytics/beyond-phishing-llm-threat-actor-tracker | framework | <https://github.com/kimburkeanalytics/beyond-phishing-llm-threat-actor-tracker> |
| KingGekko/Protosyte | framework | <https://github.com/KingGekko/Protosyte> |
| KINGJAVA911/FrankSherlock | directory | <https://github.com/KINGJAVA911/FrankSherlock> |
| Kirtar22/ATTACK-Threat_Intel | tool | <https://github.com/Kirtar22/ATTACK-Threat_Intel> |
| knight0x07/BiBi-Windows-Wiper-Analysis | tool | <https://github.com/knight0x07/BiBi-Windows-Wiper-Analysis> |
| knight0x07/DarkGate-Install-Script-via-DNS-TXT-Record | tool | <https://github.com/knight0x07/DarkGate-Install-Script-via-DNS-TXT-Record> |
| knight0x07/Lnk2Vbs | research-project | <https://github.com/knight0x07/Lnk2Vbs> |
| knight0x07/onMouseMove-HtmlFile-PoC | research-project | <https://github.com/knight0x07/onMouseMove-HtmlFile-PoC> |
| knight0x07/pyc2bytecode | research-project | <https://github.com/knight0x07/pyc2bytecode> |
| KnightChaser/MITREAttackScrapper | tool | <https://github.com/KnightChaser/MITREAttackScrapper> |
| kobaw23214/ThreatLens-API | container | <https://github.com/kobaw23214/ThreatLens-API> |
| kraloveckey/threat-intelligence-feeds | dataset | <https://github.com/kraloveckey/threat-intelligence-feeds> |
| kraven-security/python-threat-hunting-tools | tool | <https://github.com/kraven-security/python-threat-hunting-tools> |
| Krishita17/global-threat-policy-tracker | directory | <https://github.com/Krishita17/global-threat-policy-tracker> |
| krishnateja-ai/CyberSentinel-AI | tool | <https://github.com/krishnateja-ai/CyberSentinel-AI> |
| krystianbajno/check_proxy.py | tool | <https://github.com/krystianbajno/check_proxy.py> |
| Ksnaik1702/Cybersecurity-Awareness-Threat-Intelligence-Dashboard | plugin | <https://github.com/Ksnaik1702/Cybersecurity-Awareness-Threat-Intelligence-Dashboard> |
| Kubashok/malicious-c2-infrastructure | dataset | <https://github.com/Kubashok/malicious-c2-infrastructure> |
| kunai-project/kunai | tool | <https://github.com/kunai-project/kunai> |
| kyriasanta/Healthcare-Threat-Intelligence-Assessment | tool | <https://github.com/kyriasanta/Healthcare-Threat-Intelligence-Assessment> |
| lab52io/Syspce | tool | <https://github.com/lab52io/Syspce> |
| LabVIEWCommunityTraining/cti-documentation | tool | <https://github.com/LabVIEWCommunityTraining/cti-documentation> |
| LabVIEWCommunityTraining/GettingStartedLabVIEW1-Spanish | research-project | <https://github.com/LabVIEWCommunityTraining/GettingStartedLabVIEW1-Spanish> |
| LaresLLC/SysmonConfigPusher | tool | <https://github.com/LaresLLC/SysmonConfigPusher> |
| Largo-m/Instagram-Phishing-Page | tool | <https://github.com/Largo-m/Instagram-Phishing-Page> |
| LasCC/SentinelOne-Userscript | tool | <https://github.com/LasCC/SentinelOne-Userscript> |
| laugiov/scambuster | research-project | <https://github.com/laugiov/scambuster> |
| lawndoc/AdvancedHuntingQueries | tool | <https://github.com/lawndoc/AdvancedHuntingQueries> |
| lcpdn/docs-suricata | research-project | <https://github.com/lcpdn/docs-suricata> |
| LeenAdeeb/IOC-Enricher | cli-tool | <https://github.com/LeenAdeeb/IOC-Enricher> |
| lehmariaa/linkscyberthreatintelligence | tool | <https://github.com/lehmariaa/linkscyberthreatintelligence> |
| LEO-007-tech/CYBER-SHIELD | web-platform | <https://github.com/LEO-007-tech/CYBER-SHIELD> |
| levensailor/py-cisco-cti-remote | plugin | <https://github.com/levensailor/py-cisco-cti-remote> |
| lewiswigmore/virus.xcheck | cli-tool | <https://github.com/lewiswigmore/virus.xcheck> |
| li-zhenyuan/Knowledge-enhanced-Attack-Graph | research-project | <https://github.com/li-zhenyuan/Knowledge-enhanced-Attack-Graph> |
| Liberty91LTD/cti-skills | plugin | <https://github.com/Liberty91LTD/cti-skills> |
| lidless-labs/maltego-mcp | cli-tool | <https://github.com/lidless-labs/maltego-mcp> |
| lidless-labs/misp-mcp | cli-tool | <https://github.com/lidless-labs/misp-mcp> |
| like-a-freedom/cti-stats-collector | tool | <https://github.com/like-a-freedom/cti-stats-collector> |
| like-a-freedom/cti_normalizer | tool | <https://github.com/like-a-freedom/cti_normalizer> |
| lion-gu/ioc-explorer | tool | <https://github.com/lion-gu/ioc-explorer> |
| lmihaig/facultate | tool | <https://github.com/lmihaig/facultate> |
| lmyrefelt/misc-cti-2-stix | web-platform | <https://github.com/lmyrefelt/misc-cti-2-stix> |
| LoelStark/Cyber-Labs | tool | <https://github.com/LoelStark/Cyber-Labs> |
| Loginsoft-LLC/Linux-Exploit-Detection | tool | <https://github.com/Loginsoft-LLC/Linux-Exploit-Detection> |
| Loginsoft-LLC/threat-detection-rules | tool | <https://github.com/Loginsoft-LLC/threat-detection-rules> |
| lokinpendawa/aethel_core | tool | <https://github.com/lokinpendawa/aethel_core> |
| lol_monitor | web-platform | <https://github.com/misiektoja/lol_monitor> |
| LOLESXi-Project/LOLESXi | research-project | <https://github.com/LOLESXi-Project/LOLESXi> |
| loneicewolf/CTIO | tool | <https://github.com/loneicewolf/CTIO> |
| loneicewolf/PEN300-Template | tool | <https://github.com/loneicewolf/PEN300-Template> |
| loneicewolf/SOC-200-LightPreparation | tool | <https://github.com/loneicewolf/SOC-200-LightPreparation> |
| Ls4ss/ReconHound | tool | <https://github.com/Ls4ss/ReconHound> |
| luca-ramseyer/raml-kql | desktop-app | <https://github.com/luca-ramseyer/raml-kql> |
| lucas-link-code/Threat-Profiler | api-service | <https://github.com/lucas-link-code/Threat-Profiler> |
| lutichris1991/agentwhite | dashboard | <https://github.com/lutichris1991/agentwhite> |
| M-AmirSohail/iocflow | tool | <https://github.com/M-AmirSohail/iocflow> |
| m0n4/YARA-Matches-Correspondance-Array | tool | <https://github.com/m0n4/YARA-Matches-Correspondance-Array> |
| m3mike/cti-sensor-backend | dashboard | <https://github.com/m3mike/cti-sensor-backend> |
| M507/AI-SOC-Agent | web-platform | <https://github.com/M507/AI-SOC-Agent> |
| ma111e/melody | research-project | <https://github.com/ma111e/melody> |
| Madalitso-Saulos/Cyber200Forge | web-platform | <https://github.com/Madalitso-Saulos/Cyber200Forge> |
| Madmegsox1/netnoot | tool | <https://github.com/Madmegsox1/netnoot> |
| Mah3Sec/ForgeGuardian | web-platform | <https://github.com/Mah3Sec/ForgeGuardian> |
| mahend72/AM-CTI-Risk | framework | <https://github.com/mahend72/AM-CTI-Risk> |
| malek-alhu/marketplace-phaas-tracker | web-platform | <https://github.com/malek-alhu/marketplace-phaas-tracker> |
| Maloyroyorko/DVGA-application-security-assessment | api-service | <https://github.com/Maloyroyorko/DVGA-application-security-assessment> |
| Malwagon | api-service | <https://malwagon.com> |
| MalwareIntel | web-platform | <https://malwareintel.es> |
| MalwareSamples/Malware-Feed | dataset | <https://github.com/MalwareSamples/Malware-Feed> |
| mandiant/capa | tool | <https://github.com/mandiant/capa> |
| mandiant/flare-learning-hub | tool | <https://github.com/mandiant/flare-learning-hub> |
| mandiant/thiri-notebook | api-service | <https://github.com/mandiant/thiri-notebook> |
| mandiant/xrefer | plugin | <https://github.com/mandiant/xrefer> |
| manishrawat21/Cisa-KEV-Threat-Intel-Orchestrator | directory | <https://github.com/manishrawat21/Cisa-KEV-Threat-Intel-Orchestrator> |
| mannyfred/MentalTi | research-project | <https://github.com/mannyfred/MentalTi> |
| ManuelBerrueta/BST | container | <https://github.com/ManuelBerrueta/BST> |
| maramraboudi/ecthp-threat-hunting-notes | dashboard | <https://github.com/maramraboudi/ecthp-threat-hunting-notes> |
| marcvspt/cyberthreat-ai | tool | <https://github.com/marcvspt/cyberthreat-ai> |
| marcvspt/iocdb-share | api-service | <https://github.com/marcvspt/iocdb-share> |
| martinkubecka/C2Hunter | web-platform | <https://github.com/martinkubecka/C2Hunter> |
| marxgoo/Wazuh-SOC-Lab | tool | <https://github.com/marxgoo/Wazuh-SOC-Lab> |
| Masriyan/CTI-Product-Assesment-Matrix | web-platform | <https://github.com/Masriyan/CTI-Product-Assesment-Matrix> |
| masterxhackerx420-oss/wolfsec-live-map | tool | <https://github.com/masterxhackerx420-oss/wolfsec-live-map> |
| matanolabs/matano | tool | <https://github.com/matanolabs/matano> |
| matchylabs/matchy | tool | <https://github.com/matchylabs/matchy> |
| mateusdias96cs/aegis-threat-intelligence | api-service | <https://github.com/mateusdias96cs/aegis-threat-intelligence> |
| MatrixTM26/MatrixDocs | tool | <https://github.com/MatrixTM26/MatrixDocs> |
| matteounitn/Threat-Intelligence-telegram | tool | <https://github.com/matteounitn/Threat-Intelligence-telegram> |
| mattft0/cape-docker | container | <https://github.com/mattft0/cape-docker> |
| mattnotmax/hash_hunter | cli-tool | <https://github.com/mattnotmax/hash_hunter> |
| mattreduce/cti-self-study | research-project | <https://github.com/mattreduce/cti-self-study> |
| mauricelambert/CTI | tool | <https://github.com/mauricelambert/CTI> |
| mawg0ud/VulnVortex | tool | <https://github.com/mawg0ud/VulnVortex> |
| mayur-esh/threat-report-killchain | tool | <https://github.com/mayur-esh/threat-report-killchain> |
| mdecrevoisier/EVTX-to-MITRE-Attack | tool | <https://github.com/mdecrevoisier/EVTX-to-MITRE-Attack> |
| mdecrevoisier/SIGMA-detection-rules | cli-tool | <https://github.com/mdecrevoisier/SIGMA-detection-rules> |
| meese-enterprises/redirect-tracker | tool | <https://github.com/meese-enterprises/redirect-tracker> |
| mehrazino/tg-cybersec | awesome-list | <https://github.com/mehrazino/tg-cybersec> |
| meltedinhex/analyst-ai-pack | library | <https://github.com/meltedinhex/analyst-ai-pack> |
| merv3guler/cyber-news-feed | api-service | <https://github.com/merv3guler/cyber-news-feed> |
| MFMokbel/Crawlector | framework | <https://github.com/MFMokbel/Crawlector> |
| mgeha/fernsprecher | tool | <https://github.com/mgeha/fernsprecher> |
| Mhackiori/AGIR | tool | <https://github.com/Mhackiori/AGIR> |
| Mhackiori/STIXnet | tool | <https://github.com/Mhackiori/STIXnet> |
| mhearsh/threat-intel-feed | dataset | <https://github.com/mhearsh/threat-intel-feed> |
| mheerspink75/portfolio_project | tool | <https://github.com/mheerspink75/portfolio_project> |
| michaelelizarov/apt-intelligence-dashboard | dashboard | <https://github.com/michaelelizarov/apt-intelligence-dashboard> |
| MichelleBark/Cyber-Threat-Detection | research-project | <https://github.com/MichelleBark/Cyber-Threat-Detection> |
| Microck/delvn | dataset | <https://github.com/Microck/delvn> |
| MII-Cybersec/Threat-Hunting-Notebook | tool | <https://github.com/MII-Cybersec/Threat-Hunting-Notebook> |
| Mikaru0Mystic/sectinel | plugin | <https://github.com/Mikaru0Mystic/sectinel> |
| mikeroyal/Digital-Forensics-Guide | dashboard | <https://github.com/mikeroyal/Digital-Forensics-Guide> |
| mikopbx/ModuleBitrix24Integration | plugin | <https://github.com/mikopbx/ModuleBitrix24Integration> |
| mikopbx/ModuleCTIClient | plugin | <https://github.com/mikopbx/ModuleCTIClient> |
| mikopbx/ModulePT1CCore | plugin | <https://github.com/mikopbx/ModulePT1CCore> |
| minellogiacomo/SWIFT-RISKS-OF-FINANCIAL-SYSTEM-IN-A-CYBER-ERA | tool | <https://github.com/minellogiacomo/SWIFT-RISKS-OF-FINANCIAL-SYSTEM-IN-A-CYBER-ERA> |
| MishcondeReya/Covid-19-CTI | tool | <https://github.com/MishcondeReya/Covid-19-CTI> |
| misogare/awesome-cybercrimefs | awesome-list | <https://github.com/misogare/awesome-cybercrimefs> |
| MISP/best-practices-in-threat-intelligence | tool | <https://github.com/MISP/best-practices-in-threat-intelligence> |
| MISP/cti-transmute | web-platform | <https://github.com/MISP/cti-transmute> |
| MISP/docker-misp | container | <https://github.com/MISP/docker-misp> |
| MISP/intelligence-icons | tool | <https://github.com/MISP/intelligence-icons> |
| MISP/mail_to_misp | api-service | <https://github.com/MISP/mail_to_misp> |
| MISP/MISP | web-platform | <https://github.com/MISP/MISP> |
| MISP/misp-book | tool | <https://github.com/MISP/misp-book> |
| MISP/misp-dashboard | dashboard | <https://github.com/MISP/misp-dashboard> |
| MISP/misp-galaxy | tool | <https://github.com/MISP/misp-galaxy> |
| MISP/misp-galaxy-mcp | tool | <https://github.com/MISP/misp-galaxy-mcp> |
| MISP/misp-iconify | tool | <https://github.com/MISP/misp-iconify> |
| MISP/MISP-maltego | dataset | <https://github.com/MISP/MISP-maltego> |
| MISP/misp-mcp | web-platform | <https://github.com/MISP/misp-mcp> |
| MISP/misp-modules | plugin | <https://github.com/MISP/misp-modules> |
| MISP/misp-playbooks | tool | <https://github.com/MISP/misp-playbooks> |
| MISP/misp-sighting-server | tool | <https://github.com/MISP/misp-sighting-server> |
| MISP/misp-warninglists | tool | <https://github.com/MISP/misp-warninglists> |
| MISP/misp-wireshark | plugin | <https://github.com/MISP/misp-wireshark> |
| MISP/misp-workbench | tool | <https://github.com/MISP/misp-workbench> |
| MISP/Synthetic-Exercise-World-Format | tool | <https://github.com/MISP/Synthetic-Exercise-World-Format> |
| MISP/threat-actor-intelligence-server | tool | <https://github.com/MISP/threat-actor-intelligence-server> |
| mitre-attack/attack-archives | research-project | <https://github.com/mitre-attack/attack-archives> |
| mitre-attack/attack-evals | research-project | <https://github.com/mitre-attack/attack-evals> |
| mitre-attack/attack-navigator | web-platform | <https://github.com/mitre-attack/attack-navigator> |
| mitre-attack/attack-scripts | library | <https://github.com/mitre-attack/attack-scripts> |
| mitre-attack/attack-stix-data | tool | <https://github.com/mitre-attack/attack-stix-data> |
| mitre-attack/attack-website | tool | <https://github.com/mitre-attack/attack-website> |
| mitre-attack/car | tool | <https://github.com/mitre-attack/car> |
| mitre-attack/mitreattack-python | plugin | <https://github.com/mitre-attack/mitreattack-python> |
| mitre/cti | tool | <https://github.com/mitre/cti> |
| MITRECND/mitrecnd.github.io | research-project | <https://github.com/MITRECND/mitrecnd.github.io> |
| miunasu/IDA-Skill | research-project | <https://github.com/miunasu/IDA-Skill> |
| Mixture-of-RAGs-Security-Experts/MoRSE | tool | <https://github.com/Mixture-of-RAGs-Security-Experts/MoRSE> |
| mkdemir/opencti-watcher | plugin | <https://github.com/mkdemir/opencti-watcher> |
| MLSecOpsHub/agentic-attack-index | directory | <https://github.com/MLSecOpsHub/agentic-attack-index> |
| mobinert/HORUS | cli-tool | <https://github.com/mobinert/HORUS> |
| MohammadThabetHassan/TokenAbuse-Azure | tool | <https://github.com/MohammadThabetHassan/TokenAbuse-Azure> |
| mohdahsank001/Cyber-attack-analysis-using-Splunk-and-PCAP-Analyser | tool | <https://github.com/mohdahsank001/Cyber-attack-analysis-using-Splunk-and-PCAP-Analyser> |
| MonkeySeC-sys/Sandworm-PoC | framework | <https://github.com/MonkeySeC-sys/Sandworm-PoC> |
| MonkeySeC-sys/WeapingAngel | api-service | <https://github.com/MonkeySeC-sys/WeapingAngel> |
| Monukarthik/Securing-the-web-using-URL-based-analysis-and-Machine-Learning-Algorithms | tool | <https://github.com/Monukarthik/Securing-the-web-using-URL-based-analysis-and-Machine-Learning-Algorithms> |
| MoriartyPuth/Cyber-kill-chain-tool | web-platform | <https://github.com/MoriartyPuth/Cyber-kill-chain-tool> |
| mosse-security/threat-hunting-samples | dataset | <https://github.com/mosse-security/threat-hunting-samples> |
| mouadboudhar/Security-Operations-Center | dashboard | <https://github.com/mouadboudhar/Security-Operations-Center> |
| MOUKA-513/awesome-silent-security | awesome-list | <https://github.com/MOUKA-513/awesome-silent-security> |
| MrBridgeHQ/osint-researcher-claude | framework | <https://github.com/MrBridgeHQ/osint-researcher-claude> |
| mrezwanulbari/MITRE-ATT-CK-Threat-Defense-Framework | framework | <https://github.com/mrezwanulbari/MITRE-ATT-CK-Threat-Defense-Framework> |
| mrheinen/lophiid | research-project | <https://github.com/mrheinen/lophiid> |
| MrLouisWright/defang-sentinel | library | <https://github.com/MrLouisWright/defang-sentinel> |
| MrLouisWright/ioc-sentinel | tool | <https://github.com/MrLouisWright/ioc-sentinel> |
| MrM8BRH/Defensive-Security-Hub | dataset | <https://github.com/MrM8BRH/Defensive-Security-Hub> |
| Mrutyunjayamuduli1998/telegram-cti-monitor | plugin | <https://github.com/Mrutyunjayamuduli1998/telegram-cti-monitor> |
| mrwadams/attackgen | framework | <https://github.com/mrwadams/attackgen> |
| msdbg/Exploit-Index | directory | <https://github.com/msdbg/Exploit-Index> |
| msdirtbag/ADXFlowmaster | tool | <https://github.com/msdirtbag/ADXFlowmaster> |
| mthcht/Purpleteam | awesome-list | <https://github.com/mthcht/Purpleteam> |
| mthcht/threatcheck | plugin | <https://github.com/mthcht/threatcheck> |
| mthcht/ThreatHunting-Keywords | awesome-list | <https://github.com/mthcht/ThreatHunting-Keywords> |
| mthcht/ThreatHunting-Keywords-sigma-rules | tool | <https://github.com/mthcht/ThreatHunting-Keywords-sigma-rules> |
| mthcht/ThreatHunting-Keywords-yara-rules | awesome-list | <https://github.com/mthcht/ThreatHunting-Keywords-yara-rules> |
| mthcht/ThreatIntel-Reports | research-project | <https://github.com/mthcht/ThreatIntel-Reports> |
| muchdogesec/awesome_threat_intel_blogs | awesome-list | <https://github.com/muchdogesec/awesome_threat_intel_blogs> |
| muchdogesec/obstracts | tool | <https://github.com/muchdogesec/obstracts> |
| muchdogesec/stix4doge | plugin | <https://github.com/muchdogesec/stix4doge> |
| muchdogesec/stixviewer | library | <https://github.com/muchdogesec/stixviewer> |
| muchdogesec/txt2stix | plugin | <https://github.com/muchdogesec/txt2stix> |
| Mugeshwaran-k/AI-powered-threat-detection | tool | <https://github.com/Mugeshwaran-k/AI-powered-threat-detection> |
| mukul975/cve-mcp-server | api-service | <https://github.com/mukul975/cve-mcp-server> |
| munazajamil/Malware-Traffic-Analysis-in-Wireshark | tool | <https://github.com/munazajamil/Malware-Traffic-Analysis-in-Wireshark> |
| munazajamil/web-security-audit-report | tool | <https://github.com/munazajamil/web-security-audit-report> |
| mustafadalga/code-injector | tool | <https://github.com/mustafadalga/code-injector> |
| mustafadalga/dictionary-attack | tool | <https://github.com/mustafadalga/dictionary-attack> |
| mustafaefeercoban/Fedora-Workstation-Hardening | tool | <https://github.com/mustafaefeercoban/Fedora-Workstation-Hardening> |
| mustafaefeercoban/Poland-CTI-Prototype | container | <https://github.com/mustafaefeercoban/Poland-CTI-Prototype> |
| muzi5622/CTI_Platform | web-platform | <https://github.com/muzi5622/CTI_Platform> |
| mvelazc0/msInvader | tool | <https://github.com/mvelazc0/msInvader> |
| mxm0z/awesome-intelligence-writing | awesome-list | <https://github.com/mxm0z/awesome-intelligence-writing> |
| mylesagnew/poc_opencti | container | <https://github.com/mylesagnew/poc_opencti> |
| mytechnotalent/0x01-ARM-32-Hacking-Hello-World | tool | <https://github.com/mytechnotalent/0x01-ARM-32-Hacking-Hello-World> |
| mytechnotalent/0x02-ARM-32-Hacking-Int | tool | <https://github.com/mytechnotalent/0x02-ARM-32-Hacking-Int> |
| mytechnotalent/0x03-ARM-32-Hacking-Float | tool | <https://github.com/mytechnotalent/0x03-ARM-32-Hacking-Float> |
| mytechnotalent/0x04-ARM-32-Hacking-Double | tool | <https://github.com/mytechnotalent/0x04-ARM-32-Hacking-Double> |
| mytechnotalent/0x05-ARM-32-Hacking_Char | tool | <https://github.com/mytechnotalent/0x05-ARM-32-Hacking_Char> |
| mytechnotalent/0x06-ARM-32-Hacking-Char-Pointer | tool | <https://github.com/mytechnotalent/0x06-ARM-32-Hacking-Char-Pointer> |
| mytechnotalent/Hacking-Windows | api-service | <https://github.com/mytechnotalent/Hacking-Windows> |
| mytechnotalent/IIA | library | <https://github.com/mytechnotalent/IIA> |
| mytechnotalent/ToyOS | tool | <https://github.com/mytechnotalent/ToyOS> |
| mytechnotalent/Zeek-Network-Security-Monitor | tool | <https://github.com/mytechnotalent/Zeek-Network-Security-Monitor> |
| mzainxo/ICADS | tool | <https://github.com/mzainxo/ICADS> |
| mzainxo/ICADS-android-app | mobile-app | <https://github.com/mzainxo/ICADS-android-app> |
| N4SOC/O365-ThreatHunting | cli-tool | <https://github.com/N4SOC/O365-ThreatHunting> |
| n5za/osint-mcp | plugin | <https://github.com/n5za/osint-mcp> |
| nabeelxy/syara | tool | <https://github.com/nabeelxy/syara> |
| NagaSivaGunturu/ioc-insight | tool | <https://github.com/NagaSivaGunturu/ioc-insight> |
| nasbench/MindMaps | tool | <https://github.com/nasbench/MindMaps> |
| navid-alizadeh-v/splunk-abuseipdb-enrichment | api-service | <https://github.com/navid-alizadeh-v/splunk-abuseipdb-enrichment> |
| navid-alizadeh-v/Splunk-MISP-Threat-Intelligence-Collector | api-service | <https://github.com/navid-alizadeh-v/Splunk-MISP-Threat-Intelligence-Collector> |
| ndr-repo/awesome-threat-hunting | awesome-list | <https://github.com/ndr-repo/awesome-threat-hunting> |
| ndr-repo/iL_ipEnum | tool | <https://github.com/ndr-repo/iL_ipEnum> |
| ndr-repo/otx2subdomains | cli-tool | <https://github.com/ndr-repo/otx2subdomains> |
| ndr-repo/ThatsMyType | tool | <https://github.com/ndr-repo/ThatsMyType> |
| Nebulock-Inc/agentic-threat-hunting-framework | framework | <https://github.com/Nebulock-Inc/agentic-threat-hunting-framework> |
| Nebulock-Inc/macos-coresigma | framework | <https://github.com/Nebulock-Inc/macos-coresigma> |
| NenXMaster-AB/spectre | web-platform | <https://github.com/NenXMaster-AB/spectre> |
| Neo23x0/NoCat | cli-tool | <https://github.com/Neo23x0/NoCat> |
| Neo23x0/signature-base | dataset | <https://github.com/Neo23x0/signature-base> |
| Nervi0z/btl1-field-notes | tool | <https://github.com/Nervi0z/btl1-field-notes> |
| Net-Zer0/Git-MalScan | mobile-app | <https://github.com/Net-Zer0/Git-MalScan> |
| NewBee119/Ti_Collector | dataset | <https://github.com/NewBee119/Ti_Collector> |
| NFON-AG/CTI-API | api-service | <https://github.com/NFON-AG/CTI-API> |
| nicocti/stidantic | library | <https://github.com/nicocti/stidantic> |
| nicscda/fist-framework | framework | <https://github.com/nicscda/fist-framework> |
| NIGHTCREW-CL/CTI | tool | <https://github.com/NIGHTCREW-CL/CTI> |
| nikgreg99/cyber-daily-parser | tool | <https://github.com/nikgreg99/cyber-daily-parser> |
| NikolaiT/IP-Address-API | api-service | <https://github.com/NikolaiT/IP-Address-API> |
| nilsonpmjr/VANTAGE | web-platform | <https://github.com/nilsonpmjr/VANTAGE> |
| nimbusmancer/Kustonomicon | tool | <https://github.com/nimbusmancer/Kustonomicon> |
| ninedter/pcap-hunter | tool | <https://github.com/ninedter/pcap-hunter> |
| ninoseki/apullo | tool | <https://github.com/ninoseki/apullo> |
| ninoseki/ayashige | dataset | <https://github.com/ninoseki/ayashige> |
| ninoseki/ioc-extractor | library | <https://github.com/ninoseki/ioc-extractor> |
| nishikawaakira/Shenron | tool | <https://github.com/nishikawaakira/Shenron> |
| nitram509/android-web-telephony-integration | plugin | <https://github.com/nitram509/android-web-telephony-integration> |
| nizarsaidi-exe/SOC-ITSM-Platform | directory | <https://github.com/nizarsaidi-exe/SOC-ITSM-Platform> |
| njcx/BlackIPS | api-service | <https://github.com/njcx/BlackIPS> |
| NorShadeed/cybercore-cti | tool | <https://github.com/NorShadeed/cybercore-cti> |
| nshalabi/SysmonTools | tool | <https://github.com/nshalabi/SysmonTools> |
| nttcom/metemcyber | framework | <https://github.com/nttcom/metemcyber> |
| nutthakorn7/SOC-SOP | tool | <https://github.com/nutthakorn7/SOC-SOP> |
| NVISOsecurity/Detection-and-Hunting-Queries | tool | <https://github.com/NVISOsecurity/Detection-and-Hunting-Queries> |
| NVISOsecurity/ee-outliers | framework | <https://github.com/NVISOsecurity/ee-outliers> |
| O-X-L/risk-db | api-service | <https://github.com/O-X-L/risk-db> |
| oasis-open/cti-documentation | tool | <https://github.com/oasis-open/cti-documentation> |
| oasis-open/cti-pattern-validator | tool | <https://github.com/oasis-open/cti-pattern-validator> |
| oasis-open/cti-python-stix2 | api-service | <https://github.com/oasis-open/cti-python-stix2> |
| oasis-open/cti-stix-elevator | tool | <https://github.com/oasis-open/cti-stix-elevator> |
| oasis-open/cti-stix-generator | tool | <https://github.com/oasis-open/cti-stix-generator> |
| oasis-open/cti-stix-slider | tool | <https://github.com/oasis-open/cti-stix-slider> |
| oasis-open/cti-stix-validator | tool | <https://github.com/oasis-open/cti-stix-validator> |
| oasis-open/cti-stix-visualization | tool | <https://github.com/oasis-open/cti-stix-visualization> |
| oasis-open/cti-stix2-json-schemas | tool | <https://github.com/oasis-open/cti-stix2-json-schemas> |
| oasis-open/cti-taxii-client | library | <https://github.com/oasis-open/cti-taxii-client> |
| oasis-open/cti-taxii-server | library | <https://github.com/oasis-open/cti-taxii-server> |
| Odiambo/TerraTest | tool | <https://github.com/Odiambo/TerraTest> |
| Odysafe/ODYSAFE-CTI | plugin | <https://github.com/Odysafe/ODYSAFE-CTI> |
| OISF/suricata | tool | <https://github.com/OISF/suricata> |
| olafhartong/ATTACKdatamap | framework | <https://github.com/olafhartong/ATTACKdatamap> |
| olafhartong/TA-Sysmon-deploy | tool | <https://github.com/olafhartong/TA-Sysmon-deploy> |
| olafhartong/ThreatHunting | dashboard | <https://github.com/olafhartong/ThreatHunting> |
| OllieJC/tbat | tool | <https://github.com/OllieJC/tbat> |
| ology/Chess-Inspector | tool | <https://github.com/ology/Chess-Inspector> |
| OmarAK-Git/cti-apt-emulator | tool | <https://github.com/OmarAK-Git/cti-apt-emulator> |
| onion-lookup | api-service | <https://onion.ail-project.org/> |
| op7ic/GeoIPPlotter | tool | <https://github.com/op7ic/GeoIPPlotter> |
| open-circle-ltd/chocolatey.wwphone-cti | cli-tool | <https://github.com/open-circle-ltd/chocolatey.wwphone-cti> |
| OpenCTI-Platform/client-python | web-platform | <https://github.com/OpenCTI-Platform/client-python> |
| OpenCTI-Platform/connectors | web-platform | <https://github.com/OpenCTI-Platform/connectors> |
| OpenCTI-Platform/opencti | web-platform | <https://github.com/OpenCTI-Platform/opencti> |
| opencybersecurityalliance/firepit | tool | <https://github.com/opencybersecurityalliance/firepit> |
| opencybersecurityalliance/kestrel-lang | tool | <https://github.com/opencybersecurityalliance/kestrel-lang> |
| opencybersecurityalliance/stix-shifter | library | <https://github.com/opencybersecurityalliance/stix-shifter> |
| OraclesTech/guardian-sdk | api-service | <https://github.com/OraclesTech/guardian-sdk> |
| orchicyb/OrchiCyb-AI-Attack | dashboard | <https://github.com/orchicyb/OrchiCyb-AI-Attack> |
| Orestistsira/cacao-knowledge-base | tool | <https://github.com/Orestistsira/cacao-knowledge-base> |
| Orion-Intelligence/Orion-Intelligence-Solution | web-platform | <https://github.com/Orion-Intelligence/Orion-Intelligence-Solution> |
| osintbrazuca/osint-brazuca-nuclei-templates | tool | <https://github.com/osintbrazuca/osint-brazuca-nuclei-templates> |
| OsintMilGrau/emailfinder-bot | tool | <https://github.com/OsintMilGrau/emailfinder-bot> |
| osintph/falconeye | api-service | <https://github.com/osintph/falconeye> |
| osintph/threatintel-platform | web-platform | <https://github.com/osintph/threatintel-platform> |
| OsmanKandemir/associated-threat-analyzer | web-platform | <https://github.com/OsmanKandemir/associated-threat-analyzer> |
| OsmanKandemir/indicator-intelligence | research-project | <https://github.com/OsmanKandemir/indicator-intelligence> |
| OsmanKandemir/web-wordlist-generator | web-platform | <https://github.com/OsmanKandemir/web-wordlist-generator> |
| osV22/ATTACK-Force-Graph | framework | <https://github.com/osV22/ATTACK-Force-Graph> |
| OTRF/ThreatHunter-Playbook | tool | <https://github.com/OTRF/ThreatHunter-Playbook> |
| OTT-Cybersecurity-LLC/lyrie-ai | tool | <https://github.com/OTT-Cybersecurity-LLC/lyrie-ai> |
| ottodanp/flask-recon | tool | <https://github.com/ottodanp/flask-recon> |
| OTX AlienVault | research-project | <https://otx.alienvault.com/> |
| ousher/tia-framework | framework | <https://github.com/ousher/tia-framework> |
| OWASP/www-chapter-noida | tool | <https://github.com/OWASP/www-chapter-noida> |
| ozanunal0/viper | dashboard | <https://github.com/ozanunal0/viper> |
| pakdekro/DrawMeAStix | tool | <https://github.com/pakdekro/DrawMeAStix> |
| palmpon001/Social-Media | framework | <https://github.com/palmpon001/Social-Media> |
| PaloAltoNetworks/Unit42-timely-threat-intel | tool | <https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel> |
| PandH4cker/threaty-rs | api-service | <https://github.com/PandH4cker/threaty-rs> |
| panguard-ai/panguard-ai | tool | <https://github.com/panguard-ai/panguard-ai> |
| parthdmaniar/coronavirus-covid-19-SARS-CoV-2-IoCs | tool | <https://github.com/parthdmaniar/coronavirus-covid-19-SARS-CoV-2-IoCs> |
| PAST2212/domainthreat | api-service | <https://github.com/PAST2212/domainthreat> |
| Patrowl/PatrowlDocs | api-service | <https://github.com/Patrowl/PatrowlDocs> |
| Patrowl/PatrowlEngines | api-service | <https://github.com/Patrowl/PatrowlEngines> |
| Patrowl/PatrowlHears | api-service | <https://github.com/Patrowl/PatrowlHears> |
| Patrowl/PatrowlManager | api-service | <https://github.com/Patrowl/PatrowlManager> |
| patternex/patternex-feed | dataset | <https://github.com/patternex/patternex-feed> |
| paulveillard/cybersecurity-blue-team | awesome-list | <https://github.com/paulveillard/cybersecurity-blue-team> |
| paulveillard/cybersecurity-cyberinsurance | awesome-list | <https://github.com/paulveillard/cybersecurity-cyberinsurance> |
| paulveillard/cybersecurity-cyberloss | awesome-list | <https://github.com/paulveillard/cybersecurity-cyberloss> |
| paulveillard/cybersecurity-penetration-testing | awesome-list | <https://github.com/paulveillard/cybersecurity-penetration-testing> |
| paulveillard/cybersecurity-red-team | awesome-list | <https://github.com/paulveillard/cybersecurity-red-team> |
| paulveillard/cybersecurity-SOAR | awesome-list | <https://github.com/paulveillard/cybersecurity-SOAR> |
| paulveillard/cybersecurity-talks | awesome-list | <https://github.com/paulveillard/cybersecurity-talks> |
| paulveillard/cybersecurity-threat-detection | awesome-list | <https://github.com/paulveillard/cybersecurity-threat-detection> |
| paulveillard/cybersecurity-threat-intelligence | awesome-list | <https://github.com/paulveillard/cybersecurity-threat-intelligence> |
| paulveillard/cybersecurity-tools | framework | <https://github.com/paulveillard/cybersecurity-tools> |
| paulveillard/cybersecurity-web-security | awesome-list | <https://github.com/paulveillard/cybersecurity-web-security> |
| paulveillard/cybsecurity-cs | framework | <https://github.com/paulveillard/cybsecurity-cs> |
| PavanSK-01/Hybrid-Network-Intrusion-Detection-System | research-project | <https://github.com/PavanSK-01/Hybrid-Network-Intrusion-Detection-System> |
| pe3zx/crowdstrike-falcon-queries | tool | <https://github.com/pe3zx/crowdstrike-falcon-queries> |
| pe3zx/mthc | framework | <https://github.com/pe3zx/mthc> |
| PeacefullyBrewed/ThreatIntel | tool | <https://github.com/PeacefullyBrewed/ThreatIntel> |
| pedramamini/ThreatIngestor | web-platform | <https://github.com/pedramamini/ThreatIngestor> |
| pendakwahteknologi/security-threat-agent | dashboard | <https://github.com/pendakwahteknologi/security-threat-agent> |
| peng-gao-lab/beacon-cti | dataset | <https://github.com/peng-gao-lab/beacon-cti> |
| peng-gao-lab/ctinexus | framework | <https://github.com/peng-gao-lab/ctinexus> |
| PerceptraHQ/sheut-community | tool | <https://github.com/PerceptraHQ/sheut-community> |
| percipioxyz/camport_gentl | plugin | <https://github.com/percipioxyz/camport_gentl> |
| Perkins-Fund/Malware-Bible | research-project | <https://github.com/Perkins-Fund/Malware-Bible> |
| PeterDaveHello/chkdomain | web-platform | <https://github.com/PeterDaveHello/chkdomain> |
| PeterDaveHello/nrd-list-downloader | cli-tool | <https://github.com/PeterDaveHello/nrd-list-downloader> |
| PeterDaveHello/url-shorteners | tool | <https://github.com/PeterDaveHello/url-shorteners> |
| peterhanily/threatcaddy | tool | <https://github.com/peterhanily/threatcaddy> |
| Pharos AI | dashboard | <https://conflicts.app> |
| phat0x8/Secbert-cda-attack-classification | research-project | <https://github.com/phat0x8/Secbert-cda-attack-classification> |
| phishdestroy/namesilo-evidence | dataset | <https://github.com/phishdestroy/namesilo-evidence> |
| phishdestroy/nicenic-evidence | dataset | <https://github.com/phishdestroy/nicenic-evidence> |
| phishdestroy/shortdot-evidence | dataset | <https://github.com/phishdestroy/shortdot-evidence> |
| picatz/falconz | api-service | <https://github.com/picatz/falconz> |
| PigeonSec/kestrel | dataset | <https://github.com/PigeonSec/kestrel> |
| PiRogueToolSuite/colander | web-platform | <https://github.com/PiRogueToolSuite/colander> |
| PiRogueToolSuite/threatr | api-service | <https://github.com/PiRogueToolSuite/threatr> |
| pogzyb/certificate.stream | tool | <https://github.com/pogzyb/certificate.stream> |
| pogzyb/czdsdump | web-platform | <https://github.com/pogzyb/czdsdump> |
| pol73rge1s7/Pentesting-and-Hacking-Scripts | tool | <https://github.com/pol73rge1s7/Pentesting-and-Hacking-Scripts> |
| PolitoInc/ELK-Hunting | tool | <https://github.com/PolitoInc/ELK-Hunting> |
| Pr0cella/AttackFlow | framework | <https://github.com/Pr0cella/AttackFlow> |
| praiselily/Siege | tool | <https://github.com/praiselily/Siege> |
| prajwalnayaka/UEBA | dataset | <https://github.com/prajwalnayaka/UEBA> |
| prakhar0x01/Xpose | api-service | <https://github.com/prakhar0x01/Xpose> |
| Pranav-ai-cyber/network-security-basics | tool | <https://github.com/Pranav-ai-cyber/network-security-basics> |
| Pranav-ai-cyber/SCT_CS_2 | library | <https://github.com/Pranav-ai-cyber/SCT_CS_2> |
| Pranav-ai-cyber/SCT_CS_3 | tool | <https://github.com/Pranav-ai-cyber/SCT_CS_3> |
| Pranay-Kumar-02/sentinel-ai | api-service | <https://github.com/Pranay-Kumar-02/sentinel-ai> |
| Pranith-Jain/cti-ai-skills | dataset | <https://github.com/Pranith-Jain/cti-ai-skills> |
| Pranith-Jain/cti-platform | web-platform | <https://github.com/Pranith-Jain/cti-platform> |
| precize/iran-apt-mitre-attack-matrix | research-project | <https://github.com/precize/iran-apt-mitre-attack-matrix> |
| president-xd/raptor | tool | <https://github.com/president-xd/raptor> |
| ProAdmin007/Poland-Energy-Attack-Visualizer-2025-2026 | api-service | <https://github.com/ProAdmin007/Poland-Energy-Attack-Visualizer-2025-2026> |
| prodaft/cradle | web-platform | <https://github.com/prodaft/cradle> |
| prox0959/CryptoClipGuard | cli-tool | <https://github.com/prox0959/CryptoClipGuard> |
| psn_monitor | web-platform | <https://github.com/misiektoja/psn_monitor> |
| PsychoSanchez/CTI-Application | plugin | <https://github.com/PsychoSanchez/CTI-Application> |
| psyklopp/Cybersecurity-News | web-platform | <https://github.com/psyklopp/Cybersecurity-News> |
| PwCUK-CTO/OperationCloudHopper | tool | <https://github.com/PwCUK-CTO/OperationCloudHopper> |
| PwnLabMe-Project/Security-Resources | tool | <https://github.com/PwnLabMe-Project/Security-Resources> |
| qasimqlf/StepbyStep_CyberSecurity | dashboard | <https://github.com/qasimqlf/StepbyStep_CyberSecurity> |
| qeeqbox/chameleon | tool | <https://github.com/qeeqbox/chameleon> |
| qeeqbox/raven | tool | <https://github.com/qeeqbox/raven> |
| qeeqbox/reports | research-project | <https://github.com/qeeqbox/reports> |
| QinetiQ-Cyber-Intelligence/OpenCTI-Terraform | web-platform | <https://github.com/QinetiQ-Cyber-Intelligence/OpenCTI-Terraform> |
| qwertyhq/xray-analyzer | dashboard | <https://github.com/qwertyhq/xray-analyzer> |
| qyzan/apikeyScan | api-service | <https://github.com/qyzan/apikeyScan> |
| r-smith/deceptifeed | dataset | <https://github.com/r-smith/deceptifeed> |
| r1cksec/cheatsheets | directory | <https://github.com/r1cksec/cheatsheets> |
| R4z1xx/malwatcher | container | <https://github.com/R4z1xx/malwatcher> |
| radhika-gupta-13/Aegis-Cyber-2.0 | dashboard | <https://github.com/radhika-gupta-13/Aegis-Cyber-2.0> |
| radiantwave/zammad-ami-easybell | container | <https://github.com/radiantwave/zammad-ami-easybell> |
| rafaelmoreiraal/-tcc-cti-misp | tool | <https://github.com/rafaelmoreiraal/-tcc-cti-misp> |
| rafosw/DesyncRAT | tool | <https://github.com/rafosw/DesyncRAT> |
| Raghu3696/Cyber-Threat-Predictive-Analytics-for-Improving-Cyber-Supply-Chain-Security | tool | <https://github.com/Raghu3696/Cyber-Threat-Predictive-Analytics-for-Improving-Cyber-Supply-Chain-Security> |
| rajeshsharma001/pythongame001 | tool | <https://github.com/rajeshsharma001/pythongame001> |
| RandomRhythm/Vendor-Threat-Triage-Lookup | api-service | <https://github.com/RandomRhythm/Vendor-Threat-Triage-Lookup> |
| rangertaha/urlinsane | tool | <https://github.com/rangertaha/urlinsane> |
| ransomfeed/ddosint | dataset | <https://github.com/ransomfeed/ddosint> |
| ransomfeed/Ransomfeed_OpenCTI_connector | api-service | <https://github.com/ransomfeed/Ransomfeed_OpenCTI_connector> |
| ransomNews/RedACT-reports | tool | <https://github.com/ransomNews/RedACT-reports> |
| Rat5ak/TPOT-OTX-Publisher | tool | <https://github.com/Rat5ak/TPOT-OTX-Publisher> |
| RavinduRathnayaka/LiveThreatMap-dashboard | dashboard | <https://github.com/RavinduRathnayaka/LiveThreatMap-dashboard> |
| RayenGader/apt34-oilrig-threat-profile | tool | <https://github.com/RayenGader/apt34-oilrig-threat-profile> |
| rcmaehl/Cisco-Enhancer | framework | <https://github.com/rcmaehl/Cisco-Enhancer> |
| Realynx/PolySIEM | dashboard | <https://github.com/Realynx/PolySIEM> |
| reconurge/reconcrawl | cli-tool | <https://github.com/reconurge/reconcrawl> |
| reconurge/recontrack | cli-tool | <https://github.com/reconurge/recontrack> |
| RedSideSecurity/AnyStix | tool | <https://github.com/RedSideSecurity/AnyStix> |
| referefref/honeydet | tool | <https://github.com/referefref/honeydet> |
| referefref/modpot | web-platform | <https://github.com/referefref/modpot> |
| referefref/spamhole-ng | tool | <https://github.com/referefref/spamhole-ng> |
| referefref/ssh-honey-gateway | tool | <https://github.com/referefref/ssh-honey-gateway> |
| RegioHelden/innovazammad | plugin | <https://github.com/RegioHelden/innovazammad> |
| reloading01/certstream-server-rust | tool | <https://github.com/reloading01/certstream-server-rust> |
| reloading01/threat-intelligence-dataset | dataset | <https://github.com/reloading01/threat-intelligence-dataset> |
| remiallain/echogram | api-service | <https://github.com/remiallain/echogram> |
| RescueSocial/Hollywood_Disinformation_Amber-Depp-Musk | web-platform | <https://github.com/RescueSocial/Hollywood_Disinformation_Amber-Depp-Musk> |
| REScure Threat Intel Feed | plugin | <https://rescure.fruxlabs.com/> |
| resistec/diamond-model-editor | web-platform | <https://github.com/resistec/diamond-model-editor> |
| rezahamzeh69/TGLF-Net-ZeroDay-IDS | framework | <https://github.com/rezahamzeh69/TGLF-Net-ZeroDay-IDS> |
| rf-peixoto/phishing_pot | research-project | <https://github.com/rf-peixoto/phishing_pot> |
| rfackroyd/detection-engineering-starter-pack | tool | <https://github.com/rfackroyd/detection-engineering-starter-pack> |
| rhed-IT/Cybersecurity-Threat-Intelligence-Analysis-Level-3-Certification | tool | <https://github.com/rhed-IT/Cybersecurity-Threat-Intelligence-Analysis-Level-3-Certification> |
| rhettrestive2123/CarCanvas | dashboard | <https://github.com/rhettrestive2123/CarCanvas> |
| RiadhBenlamine/Apache-logger | tool | <https://github.com/RiadhBenlamine/Apache-logger> |
| ridgelinecyberdefence/Enterprise-Detection-Engineering | dashboard | <https://github.com/ridgelinecyberdefence/Enterprise-Detection-Engineering> |
| ringcentral/rc-unified-crm-extension | plugin | <https://github.com/ringcentral/rc-unified-crm-extension> |
| rinjanianalytics/cti-platform-api | api-service | <https://github.com/rinjanianalytics/cti-platform-api> |
| rinjanianalytics/cti-platform-dashboard | api-service | <https://github.com/rinjanianalytics/cti-platform-dashboard> |
| rix4uni/nucleihub-templates | tool | <https://github.com/rix4uni/nucleihub-templates> |
| RizwanBuhari/Stalactite-ThreatLens | tool | <https://github.com/RizwanBuhari/Stalactite-ThreatLens> |
| Rizzy1857/ArteFact | framework | <https://github.com/Rizzy1857/ArteFact> |
| RM-ReactorHunt/Threat-Hunting-Team-THT | research-project | <https://github.com/RM-ReactorHunt/Threat-Hunting-Team-THT-> |
| RobPinna/Trust-surface | tool | <https://github.com/RobPinna/Trust-surface> |
| rodanmaharjan/ThreatIntelligence | tool | <https://github.com/rodanmaharjan/ThreatIntelligence> |
| romaingenard/osint-ai-toolkit | framework | <https://github.com/romaingenard/osint-ai-toolkit> |
| RoomaSec/RmEye | tool | <https://github.com/RoomaSec/RmEye> |
| rp-holdings/rp-stealth-security | container | <https://github.com/rp-holdings/rp-stealth-security> |
| rshipp/awesome-malware-analysis | awesome-list | <https://github.com/rshipp/awesome-malware-analysis> |
| RSN601KRI/Guard.code | api-service | <https://github.com/RSN601KRI/Guard.code> |
| rstcloud/rstthreats | web-platform | <https://github.com/rstcloud/rstthreats> |
| rulezet/rulezet-cast | plugin | <https://github.com/rulezet/rulezet-cast> |
| rulezet/rulezet-core | web-platform | <https://github.com/rulezet/rulezet-core> |
| rx4747/cti-investigation-vault | tool | <https://github.com/rx4747/cti-investigation-vault> |
| rx4747/cti-stix-workbench | plugin | <https://github.com/rx4747/cti-stix-workbench> |
| S-L1/ti_scraper | api-service | <https://github.com/S-L1/ti_scraper> |
| s-tip/stip-common | web-platform | <https://github.com/s-tip/stip-common> |
| s0cm0nkey/Security-Reference-Guide | dashboard | <https://github.com/s0cm0nkey/Security-Reference-Guide> |
| S4i1M/Cyber-News-Bits | api-service | <https://github.com/S4i1M/Cyber-News-Bits> |
| s4ntrx/Cybersecurity-Threats-Guide | dashboard | <https://github.com/s4ntrx/Cybersecurity-Threats-Guide> |
| SackOfHacks/ICS-PCAP-Challenges | dashboard | <https://github.com/SackOfHacks/ICS-PCAP-Challenges> |
| SackOfHacks/Industrial-Cybersecurity-2nd-Edition | tool | <https://github.com/SackOfHacks/Industrial-Cybersecurity-2nd-Edition> |
| SackOfHacks/OT_Security_OnePagers | tool | <https://github.com/SackOfHacks/OT_Security_OnePagers> |
| saghet/OpenRecon | api-service | <https://github.com/saghet/OpenRecon> |
| sajjad47/AITIR-Framework | framework | <https://github.com/sajjad47/AITIR-Framework> |
| salecharohit/semhound | tool | <https://github.com/salecharohit/semhound> |
| Sam-codes11/Cybathon-SIH | web-platform | <https://github.com/Sam-codes11/Cybathon-SIH-> |
| Sam0x90/CTI | research-project | <https://github.com/Sam0x90/CTI> |
| sameerwire/Threat-Intelligence-Dashboard | dashboard | <https://github.com/sameerwire/Threat-Intelligence-Dashboard> |
| sandeepmothukuri/Enterprise-Detection-Engineering-SOC-Lab | container | <https://github.com/sandeepmothukuri/Enterprise-Detection-Engineering-SOC-Lab> |
| Sandesh14015/CASHNET | web-platform | <https://github.com/Sandesh14015/CASHNET> |
| sandialabs/scot | tool | <https://github.com/sandialabs/scot> |
| sanjanb/cti-nlp-system | api-service | <https://github.com/sanjanb/cti-nlp-system> |
| sapphirex00/Threat-Hunting | research-project | <https://github.com/sapphirex00/Threat-Hunting> |
| SayamAlt/Cybersecurity-Threat-Intelligence-System-using-Neo4j-Graphiti-and-Pydantic-AI | dataset | <https://github.com/SayamAlt/Cybersecurity-Threat-Intelligence-System-using-Neo4j-Graphiti-and-Pydantic-AI> |
| sbousseaden/EVTX-ATTACK-SAMPLES | dataset | <https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES> |
| sbousseaden/macOS-ATTACK-DATASET | dataset | <https://github.com/sbousseaden/macOS-ATTACK-DATASET> |
| sbousseaden/PCAP-ATTACK | tool | <https://github.com/sbousseaden/PCAP-ATTACK> |
| sbousseaden/Slides | tool | <https://github.com/sbousseaden/Slides> |
| sbousseaden/YaraHunts | tool | <https://github.com/sbousseaden/YaraHunts> |
| Scarbaci/SSHapendoes | tool | <https://github.com/Scarbaci/SSHapendoes> |
| screem500/cti-reports | research-project | <https://github.com/screem500/cti-reports> |
| SCS-Labs/TheWatchList | dataset | <https://github.com/SCS-Labs/TheWatchList> |
| sduff/mitre_attack_csv | tool | <https://github.com/sduff/mitre_attack_csv> |
| Seadox/Zerogram | cli-tool | <https://github.com/Seadox/Zerogram> |
| Seadox/Zerogram-UI | web-platform | <https://github.com/Seadox/Zerogram-UI> |
| SecOpsNews/news | dashboard | <https://github.com/SecOpsNews/news> |
| secureworks/taegis-threat-hunting-tutorials | tool | <https://github.com/secureworks/taegis-threat-hunting-tutorials> |
| Security-Onion-Solutions/securityonion | dashboard | <https://github.com/Security-Onion-Solutions/securityonion> |
| SecurityClaw/SecurityClaw | tool | <https://github.com/SecurityClaw/SecurityClaw> |
| Securonix/AutonomousThreatSweeper | tool | <https://github.com/Securonix/AutonomousThreatSweeper> |
| secutils-dev/secutils | api-service | <https://github.com/secutils-dev/secutils> |
| seinz100754-eng/vt-warden | api-service | <https://github.com/seinz100754-eng/vt-warden> |
| SEKOIA-IO/automation-library | library | <https://github.com/SEKOIA-IO/automation-library> |
| SEKOIA-IO/Community | tool | <https://github.com/SEKOIA-IO/Community> |
| SEKOIA-IO/documentation | tool | <https://github.com/SEKOIA-IO/documentation> |
| sercanokur/GhostCatcherEDR | web-platform | <https://github.com/sercanokur/GhostCatcherEDR> |
| sfakiana/FIRST-CTI-2023 | tool | <https://github.com/sfakiana/FIRST-CTI-2023> |
| shallvhack/shallvhack.github.io | tool | <https://github.com/shallvhack/shallvhack.github.io> |
| shaunbny/PhiShield-ai | tool | <https://github.com/shaunbny/PhiShield-ai> |
| shellcromancer/cti-go | cli-tool | <https://github.com/shellcromancer/cti-go> |
| Shivam-Jha96/NetPulse | tool | <https://github.com/Shivam-Jha96/NetPulse> |
| Shlucus/Security-Bookmarks | library | <https://github.com/Shlucus/Security-Bookmarks> |
| SHolzhauer/elastic-tip | tool | <https://github.com/SHolzhauer/elastic-tip> |
| shope115/she-love-me | plugin | <https://github.com/shope115/she-love-me> |
| signorrayan/Splunk-Threat-Hunting | dashboard | <https://github.com/signorrayan/Splunk-Threat-Hunting> |
| silascutler/botnet_logs | dataset | <https://github.com/silascutler/botnet_logs> |
| Simiyuu/realtime-cti-honeypot | container | <https://github.com/Simiyuu/realtime-cti-honeypot> |
| simohowaanaa/darknet-analyst-lab | tool | <https://github.com/simohowaanaa/darknet-analyst-lab> |
| SimonSwopes/Stakeout | tool | <https://github.com/SimonSwopes/Stakeout> |
| SkxOverKill/Pulse_Intel | web-platform | <https://github.com/SkxOverKill/Pulse_Intel> |
| SlimKQL/Detections.AI | tool | <https://github.com/SlimKQL/Detections.AI> |
| slowmist/blockchain-threat-intelligence | web-platform | <https://github.com/slowmist/blockchain-threat-intelligence> |
| smidrkal/OpenCTI | container | <https://github.com/smidrkal/OpenCTI> |
| smjennings/threat-intel-daily | tool | <https://github.com/smjennings/threat-intel-daily> |
| SNAPKITTYWEST/p3q-tsql | mobile-app | <https://github.com/SNAPKITTYWEST/p3q-tsql> |
| SNischayPrasad/Cybersecurity-Awareness-Threat-Intelligence-Dashboard | dashboard | <https://github.com/SNischayPrasad/Cybersecurity-Awareness-Threat-Intelligence-Dashboard> |
| SOC-101/SOC-Introduction | tool | <https://github.com/SOC-101/SOC-Introduction> |
| SOC-CyberART/CARTI-Feeds | dataset | <https://github.com/SOC-CyberART/CARTI-Feeds> |
| sohankanna/india-threat-tracker | mobile-app | <https://github.com/sohankanna/india-threat-tracker> |
| SOLANKYYY/signal-desk | tool | <https://github.com/SOLANKYYY/signal-desk> |
| sophos/sophos-central-api-connector | api-service | <https://github.com/sophos/sophos-central-api-connector> |
| SoulSec/resource-threat-hunting | tool | <https://github.com/SoulSec/resource-threat-hunting> |
| soxoj/telegram-bot-dumper-go | api-service | <https://github.com/soxoj/telegram-bot-dumper-go> |
| spacepatcher/firehol-ip-aggregator | api-service | <https://github.com/spacepatcher/firehol-ip-aggregator> |
| Spacial/awesome-csirt | awesome-list | <https://github.com/Spacial/awesome-csirt> |
| Spayker/a3wasp-core | cli-tool | <https://github.com/Spayker/a3wasp-core> |
| Spayker/a3wasp-hc | cli-tool | <https://github.com/Spayker/a3wasp-hc> |
| Spayker/a3wasp-missions | tool | <https://github.com/Spayker/a3wasp-missions> |
| Spayker/a3wasp-server | tool | <https://github.com/Spayker/a3wasp-server> |
| Speicherstadt/kontext | web-platform | <https://github.com/Speicherstadt/kontext> |
| spkatragadda/intelliHunt | container | <https://github.com/spkatragadda/intelliHunt> |
| spktrvm/CTI-Portfolio | cli-tool | <https://github.com/spktrvm/CTI-Portfolio> |
| spmedia/Crypto-Scam-and-Crypto-Phishing-Threat-Intel-Feed | dataset | <https://github.com/spmedia/Crypto-Scam-and-Crypto-Phishing-Threat-Intel-Feed> |
| spmedia/PhishingSecLists | cli-tool | <https://github.com/spmedia/PhishingSecLists> |
| spmedia/Telegram-Channel-Joiner | api-service | <https://github.com/spmedia/Telegram-Channel-Joiner> |
| SPYCIIII/Password_Checker_Randomizer | desktop-app | <https://github.com/SPYCIIII/Password_Checker_Randomizer> |
| spydisec/spydithreatintel | dataset | <https://github.com/spydisec/spydithreatintel> |
| sr-maximus/P-CIDER | tool | <https://github.com/sr-maximus/P-CIDER> |
| sroberts/awesome-iocs | awesome-list | <https://github.com/sroberts/awesome-iocs> |
| ssnkhan/adversarial-threat-modelling | tool | <https://github.com/ssnkhan/adversarial-threat-modelling> |
| ssnkhan/CyberChef | tool | <https://github.com/ssnkhan/CyberChef> |
| ssnkhan/infrastructure-hunting | tool | <https://github.com/ssnkhan/infrastructure-hunting> |
| ssnkhan/mihari-maltego-transform | dataset | <https://github.com/ssnkhan/mihari-maltego-transform> |
| stairwell-inc/threat-research | research-project | <https://github.com/stairwell-inc/threat-research> |
| StamusNetworks/Clear-NDR-ISO | dashboard | <https://github.com/StamusNetworks/Clear-NDR-ISO> |
| StamusNetworks/scirius | dashboard | <https://github.com/StamusNetworks/scirius> |
| stanfrbd/mcp-cyberbro | api-service | <https://github.com/stanfrbd/mcp-cyberbro> |
| steam_monitor | web-platform | <https://github.com/misiektoja/steam_monitor> |
| StephenOTT/STIX-Faker | tool | <https://github.com/StephenOTT/STIX-Faker> |
| StephenOTT/STIX-Java | library | <https://github.com/StephenOTT/STIX-Java> |
| StephenOTT/TAXII-Server | tool | <https://github.com/StephenOTT/TAXII-Server> |
| steponeerror/ip-radar | api-service | <https://github.com/steponeerror/ip-radar> |
| SteveClement/misp-monitor | plugin | <https://github.com/SteveClement/misp-monitor> |
| STIX Viewer | tool | <https://stix-viewer.threatlandscape.io/> |
| stratosphereips/AIP | tool | <https://github.com/stratosphereips/AIP> |
| stratosphereips/ip_enrich | tool | <https://github.com/stratosphereips/ip_enrich> |
| SubaruSama/COGNOS | tool | <https://github.com/SubaruSama/COGNOS> |
| SubashGhimire/Hunting-Queries-and-Detection-Rule-Microsoft-Sentinel-Defender | tool | <https://github.com/SubashGhimire/Hunting-Queries-and-Detection-Rule-Microsoft-Sentinel-Defender> |
| substationworm/CTF-Write-Ups | tool | <https://github.com/substationworm/CTF-Write-Ups> |
| sudo-flgr/anhanga | tool | <https://github.com/sudo-flgr/anhanga> |
| sugarhillconsultants/secure-data-fusion-platform | container | <https://github.com/sugarhillconsultants/secure-data-fusion-platform> |
| SUmidcyber/Malware-Analysis-Reports | tool | <https://github.com/SUmidcyber/Malware-Analysis-Reports> |
| SUmidcyber/PortPatrol | container | <https://github.com/SUmidcyber/PortPatrol> |
| sumitsaini-sec/SOC-L1-investigation-lab | tool | <https://github.com/sumitsaini-sec/SOC-L1-investigation-lab> |
| sundruid/muonfp | tool | <https://github.com/sundruid/muonfp> |
| sunilgentyala/gsh-framework | framework | <https://github.com/sunilgentyala/gsh-framework> |
| svch0stz/TheThreatHuntLibrary | library | <https://github.com/svch0stz/TheThreatHuntLibrary> |
| svo80/vti_search | tool | <https://github.com/svo80/vti_search> |
| SwagataGhosh7/TrustGuard-AI | web-platform | <https://github.com/SwagataGhosh7/TrustGuard-AI> |
| SwiftOnSecurity/sysmon-config | tool | <https://github.com/SwiftOnSecurity/sysmon-config> |
| SylvesterDuah/The_Guardian_of_AI_Alignment | tool | <https://github.com/SylvesterDuah/The_Guardian_of_AI_Alignment> |
| syne0/M365-HoneyTenant-Config-Guide | dashboard | <https://github.com/syne0/M365-HoneyTenant-Config-Guide> |
| synthient/public-research | research-project | <https://github.com/synthient/public-research> |
| sysfox/ShadowShell | cli-tool | <https://github.com/sysfox/ShadowShell> |
| t4d/PhishingKitHunter | tool | <https://github.com/t4d/PhishingKitHunter> |
| tanbro/exosip2ctypes | tool | <https://github.com/tanbro/exosip2ctypes> |
| TangoisdownHQ/TID-Recon-Dog | container | <https://github.com/TangoisdownHQ/TID-Recon-Dog> |
| TanoojSeelam/Phishing-URL-Detection-Using-ML | tool | <https://github.com/TanoojSeelam/Phishing-URL-Detection-Using-ML> |
| TanoojSeelam/PhishingSites | cli-tool | <https://github.com/TanoojSeelam/PhishingSites> |
| taoq-ai/ziran | tool | <https://github.com/taoq-ai/ziran> |
| TaskForce47/Liberation | research-project | <https://github.com/TaskForce47/Liberation> |
| tasooshi/exfilkit | tool | <https://github.com/tasooshi/exfilkit> |
| Tcotl/AgentCapture | api-service | <https://github.com/Tcotl/AgentCapture> |
| Te-k/pybinaryedge | api-service | <https://github.com/Te-k/pybinaryedge> |
| Te-k/pysafebrowsing | library | <https://github.com/Te-k/pysafebrowsing> |
| TeamLoick/lolinck-api | api-service | <https://github.com/TeamLoick/lolinck-api> |
| teixeira0xfffff/Cybercrime-Forums | research-project | <https://github.com/teixeira0xfffff/Cybercrime-Forums> |
| Tekila11/opencti-vuln-toolkit | plugin | <https://github.com/Tekila11/opencti-vuln-toolkit> |
| telekom-security/malware_analysis | research-project | <https://github.com/telekom-security/malware_analysis> |
| teler-sh/teler | research-project | <https://github.com/teler-sh/teler> |
| TeMiroYteHasheo/The-Hunters-Framework | framework | <https://github.com/TeMiroYteHasheo/The-Hunters-Framework> |
| tenzir/threatbus | research-project | <https://github.com/tenzir/threatbus> |
| tertiarycourses/TGS-2024049211-CompTIA-Cybersecurity-Analyst-CySAPlus-Training | dashboard | <https://github.com/tertiarycourses/TGS-2024049211-CompTIA-Cybersecurity-Analyst-CySAPlus-Training> |
| tg12/dns-honeypot | research-project | <https://github.com/tg12/dns-honeypot> |
| tg12/phantomstars | tool | <https://github.com/tg12/phantomstars> |
| tg12/pihole-phishtank-list | research-project | <https://github.com/tg12/pihole-phishtank-list> |
| tg12/PoC_CVEs | dataset | <https://github.com/tg12/PoC_CVEs> |
| tg12/rapid7_OSINT | api-service | <https://github.com/tg12/rapid7_OSINT> |
| Th3Tr1ckst3r/GReverse | api-service | <https://github.com/Th3Tr1ckst3r/GReverse> |
| thalesgroup-cert/Thalesgroup-misp-taxonomy | tool | <https://github.com/thalesgroup-cert/Thalesgroup-misp-taxonomy> |
| thalesgroup-cert/Watcher | web-platform | <https://github.com/thalesgroup-cert/Watcher> |
| ThalesGroup/sherlock-threathunting-tool | api-service | <https://github.com/ThalesGroup/sherlock-threathunting-tool> |
| The-Bugger/Net-Guard | dashboard | <https://github.com/The-Bugger/Net-Guard> |
| The-Privacy-Commons-Institute/chrome-mal-ids | browser-extension | <https://github.com/The-Privacy-Commons-Institute/chrome-mal-ids> |
| TheArshiaKhan/SOC-home-lab | tool | <https://github.com/TheArshiaKhan/SOC-home-lab> |
| TheekshaniPramodya/Phishing-Detection-RandomForest-RCA | tool | <https://github.com/TheekshaniPramodya/Phishing-Detection-RandomForest-RCA> |
| TheHive-Project/Cortex | api-service | <https://github.com/TheHive-Project/Cortex> |
| TheHive-Project/Cortex-Analyzers | tool | <https://github.com/TheHive-Project/Cortex-Analyzers> |
| TheHive-Project/DigitalShadows2TH | plugin | <https://github.com/TheHive-Project/DigitalShadows2TH> |
| TheJ-Erk400/reflectrepoter | web-platform | <https://github.com/TheJ-Erk400/reflectrepoter> |
| themalwarenews/AbuseIPdb | api-service | <https://github.com/themalwarenews/AbuseIPdb> |
| theparanoids/rdfp | cli-tool | <https://github.com/theparanoids/rdfp> |
| TheShivNand/Adversarial-Training-for-Robust-Intrusion-Detection-using-CIC-IDS2018 | dataset | <https://github.com/TheShivNand/Adversarial-Training-for-Robust-Intrusion-Detection-using-CIC-IDS2018> |
| TheZubairUsman/ssrf-cheatsheet-2025 | tool | <https://github.com/TheZubairUsman/ssrf-cheatsheet-2025> |
| thirdeyeintelligence/Memoirs-of-a-Threat-Hunter | tool | <https://github.com/thirdeyeintelligence/Memoirs-of-a-Threat-Hunter> |
| thisisessa/AI-Driven-Automated-Incident-Response-Platform | web-platform | <https://github.com/thisisessa/AI-Driven-Automated-Incident-Response-Platform> |
| ThisIsLibra/m3 | framework | <https://github.com/ThisIsLibra/m3> |
| thomasunise/argus | web-platform | <https://github.com/thomasunise/argus> |
| THORCollective/HEARTH | research-project | <https://github.com/THORCollective/HEARTH> |
| THORCollective/threat-hunting-mcp-server | tool | <https://github.com/THORCollective/threat-hunting-mcp-server> |
| threadlinqs-cmd/intelthreadlinqs-mcp | tool | <https://github.com/threadlinqs-cmd/intelthreadlinqs-mcp> |
| ThreatDefence/agentic-attack-detections | framework | <https://github.com/ThreatDefence/agentic-attack-detections> |
| threathunterX/underground-slang-lexicon | research-project | <https://github.com/threathunterX/underground-slang-lexicon> |
| ThreatLens | api-service | <https://github.com/AbdaullahAG/Threat_Intel_Project> |
| THREATRADAR-Pipeline/ThreatRadar | dataset | <https://github.com/THREATRADAR-Pipeline/ThreatRadar> |
| ThreatRecall/zettelforge | tool | <https://github.com/ThreatRecall/zettelforge> |
| thremulation-station/thremulation-station | tool | <https://github.com/thremulation-station/thremulation-station> |
| tomchop/malcom | tool | <https://github.com/tomchop/malcom> |
| tomwechsler/Active_Directory_Advanced_Threat_Hunting | directory | <https://github.com/tomwechsler/Active_Directory_Advanced_Threat_Hunting> |
| toolswatch/vFeed | api-service | <https://github.com/toolswatch/vFeed> |
| toonight/NEMESIS | tool | <https://github.com/toonight/NEMESIS> |
| topher-lo/hunts | dataset | <https://github.com/topher-lo/hunts> |
| TorranceTech/sentinel-osint | tool | <https://github.com/TorranceTech/sentinel-osint> |
| tracebit-com/turingpot | framework | <https://github.com/tracebit-com/turingpot> |
| traut/jupyter-widget-stixview | library | <https://github.com/traut/jupyter-widget-stixview> |
| traut/stixview | library | <https://github.com/traut/stixview> |
| travisbgreen/hunting-rules | tool | <https://github.com/travisbgreen/hunting-rules> |
| trickest/elasticsearch_index | directory | <https://github.com/trickest/elasticsearch_index> |
| trilwu/apttrail | dataset | <https://github.com/trilwu/apttrail> |
| triw0lf/report-to-hunt | tool | <https://github.com/triw0lf/report-to-hunt> |
| tronplex/cover | tool | <https://github.com/tronplex/cover> |
| Truvis/SplunkDashboards | plugin | <https://github.com/Truvis/SplunkDashboards> |
| Truvis/Suricata_Threat-Hunting-Rules | tool | <https://github.com/Truvis/Suricata_Threat-Hunting-Rules> |
| tusarbhuia6294-spec/ELITESYNC-SOC-AI | tool | <https://github.com/tusarbhuia6294-spec/ELITESYNC-SOC-AI> |
| tvfischer/ps-srum-hunting | cli-tool | <https://github.com/tvfischer/ps-srum-hunting> |
| txuswashere/2024-state-of-the-art | tool | <https://github.com/txuswashere/2024-state-of-the-art> |
| txuswashere/Cyber-Attacks-Mitigation | tool | <https://github.com/txuswashere/Cyber-Attacks-Mitigation> |
| txuswashere/Gamaker | tool | <https://github.com/txuswashere/Gamaker> |
| txuswashere/PenTestingLab.es | awesome-list | <https://github.com/txuswashere/PenTestingLab.es> |
| tylabs/dovehawk | plugin | <https://github.com/tylabs/dovehawk> |
| typedb-osi/typedb-cti | web-platform | <https://github.com/typedb-osi/typedb-cti> |
| typosquatter/ail-typo-squatting | dataset | <https://github.com/typosquatter/ail-typo-squatting> |
| typosquatter/ail-typo-website | library | <https://github.com/typosquatter/ail-typo-website> |
| ugurrates/CABTA | web-platform | <https://github.com/ugurrates/CABTA> |
| ujwal-1/Honeypot-BaitShell | cli-tool | <https://github.com/ujwal-1/Honeypot-BaitShell> |
| UnkL4b/GitMiner3 | tool | <https://github.com/UnkL4b/GitMiner3> |
| unknownhad/CloudIntel | tool | <https://github.com/unknownhad/CloudIntel> |
| UPinar/contrastapi | api-service | <https://github.com/UPinar/contrastapi> |
| uptycslabs/IOCs | research-project | <https://github.com/uptycslabs/IOCs> |
| Urbi5g/SOC-Home-Lab-Splunk | dashboard | <https://github.com/Urbi5g/SOC-Home-Lab-Splunk> |
| urcuqui/WhiteHat | research-project | <https://github.com/urcuqui/WhiteHat> |
| urldna/urldna | api-service | <https://github.com/urldna/urldna> |
| urlscore/Urlscore.ai | api-service | <https://github.com/urlscore/Urlscore.ai> |
| urlvet/urlvet | tool | <https://github.com/urlvet/urlvet> |
| usrtem/AI-Cybersecurity-Research | framework | <https://github.com/usrtem/AI-Cybersecurity-Research> |
| usrtem/LokiBot-Malware-Analysis | dashboard | <https://github.com/usrtem/LokiBot-Malware-Analysis> |
| usrtem/Malware-Classification-Qilin | cli-tool | <https://github.com/usrtem/Malware-Classification-Qilin> |
| utkusen/baitroute | library | <https://github.com/utkusen/baitroute> |
| utmstack/UTMStack | tool | <https://github.com/utmstack/UTMStack> |
| uttambodara/rootme-solution | web-platform | <https://github.com/uttambodara/rootme-solution-> |
| uuluul/CTI_Project_Layers | dashboard | <https://github.com/uuluul/CTI_Project_Layers> |
| VaasHunter/threat-hunting-labs | tool | <https://github.com/VaasHunter/threat-hunting-labs> |
| VaghesanSundaram/cti-claim-provenance | research-project | <https://github.com/VaghesanSundaram/cti-claim-provenance> |
| Vamshi31-bodd/security-log-analyzer | tool | <https://github.com/Vamshi31-bodd/security-log-analyzer> |
| ventz/docker-cif | container | <https://github.com/ventz/docker-cif> |
| VeroSec/DACTIE | tool | <https://github.com/VeroSec/DACTIE> |
| vfeedio/pyvfeed | api-service | <https://github.com/vfeedio/pyvfeed> |
| Vigil-SOC/vigil | tool | <https://github.com/Vigil-SOC/vigil> |
| vinayakcyber/TTP-Mapper | api-service | <https://github.com/vinayakcyber/TTP-Mapper> |
| vinsk0h/KQLab | web-platform | <https://github.com/vinsk0h/KQLab> |
| Viralmaniar/MurMurHash | web-platform | <https://github.com/Viralmaniar/MurMurHash> |
| Virus-Samples/Malware-Sample-Sources | dataset | <https://github.com/Virus-Samples/Malware-Sample-Sources> |
| VirusTotal/virustotal-mcp | plugin | <https://github.com/VirusTotal/virustotal-mcp> |
| visiongaiatechnology/gedefenseandroid | web-platform | <https://github.com/visiongaiatechnology/gedefenseandroid> |
| visualbasic6/chatter | research-project | <https://github.com/visualbasic6/chatter> |
| Vith0r/StackSentry | cli-tool | <https://github.com/Vith0r/StackSentry> |
| VladTepes84/Rekos | cli-tool | <https://github.com/VladTepes84/Rekos> |
| vlegoy/rcATT | tool | <https://github.com/vlegoy/rcATT> |
| vmkspv/lenspect | tool | <https://github.com/vmkspv/lenspect> |
| vnelai/friday-overtime-cti-lab | tool | <https://github.com/vnelai/friday-overtime-cti-lab> |
| vnelai/opencti-investigation-lab | tool | <https://github.com/vnelai/opencti-investigation-lab> |
| vobiz-ai/Vobiz-Freshdesk-Calling | cli-tool | <https://github.com/vobiz-ai/Vobiz-Freshdesk-Calling> |
| vobiz-ai/Vobiz-Pipedrive-Calling | cli-tool | <https://github.com/vobiz-ai/Vobiz-Pipedrive-Calling> |
| Voidly Censorship Index | directory | <https://voidly.ai/censorship-index> |
| volexity/threat-intel | tool | <https://github.com/volexity/threat-intel> |
| VolkanSah/Detection-Labs-for-Palantir-Style-Activity | research-project | <https://github.com/VolkanSah/Detection-Labs-for-Palantir-Style-Activity> |
| VSecDK/VSec-CTI-League | tool | <https://github.com/VSecDK/VSec-CTI-League> |
| vsxsentry/vsxsentry.github.io | plugin | <https://github.com/vsxsentry/vsxsentry.github.io> |
| vuldb/cyber_threat_intelligence | tool | <https://github.com/vuldb/cyber_threat_intelligence> |
| vulnersCom/api | api-service | <https://github.com/vulnersCom/api> |
| w0h1v/mcp-virustotal | api-service | <https://github.com/w0h1v/mcp-virustotal> |
| w8mej/ThreatPlays | tool | <https://github.com/w8mej/ThreatPlays> |
| wagga40/LogsTotal | tool | <https://github.com/wagga40/LogsTotal> |
| wazuh/wazuh | container | <https://github.com/wazuh/wazuh> |
| WeaverHeavy/Threat-Intelligence-Tradecraft | plugin | <https://github.com/WeaverHeavy/Threat-Intelligence-Tradecraft> |
| weisshorn-cyd/gocti | cli-tool | <https://github.com/weisshorn-cyd/gocti> |
| werdelesmarcio/iPyScan | tool | <https://github.com/werdelesmarcio/iPyScan> |
| Wes974/indic | web-platform | <https://github.com/Wes974/indic> |
| wesinator/ergenekon | tool | <https://github.com/wesinator/ergenekon> |
| wesinator/GroundTruths | tool | <https://github.com/wesinator/GroundTruths> |
| wesinator/ICD203-intel-analysis | research-project | <https://github.com/wesinator/ICD203-intel-analysis> |
| wesinator/indicator-deprecation-calculator | web-platform | <https://github.com/wesinator/indicator-deprecation-calculator> |
| wesinator/threatconnect-utils | api-service | <https://github.com/wesinator/threatconnect-utils> |
| whichbuffer/CTTC | api-service | <https://github.com/whichbuffer/CTTC> |
| whiterabb17/r3ngine-mobile | mobile-app | <https://github.com/whiterabb17/r3ngine-mobile> |
| wi5nuu/SENTINEL-X-X-Domain-Threat-Fusion-Platform | api-service | <https://github.com/wi5nuu/SENTINEL-X-X-Domain-Threat-Fusion-Platform> |
| WiLL75G/soc-analyst-toolkit | framework | <https://github.com/WiLL75G/soc-analyst-toolkit> |
| williamjsmail/Barracuda | tool | <https://github.com/williamjsmail/Barracuda> |
| wisepythagoras/honeyshell | cli-tool | <https://github.com/wisepythagoras/honeyshell> |
| wizhardhacker1/HIVE-SECURITY | tool | <https://github.com/wizhardhacker1/HIVE-SECURITY> |
| wolffcatskyy/crowdsec-blocklist-import | container | <https://github.com/wolffcatskyy/crowdsec-blocklist-import> |
| wolffcatskyy/crowdsec-unifi-bouncer | tool | <https://github.com/wolffcatskyy/crowdsec-unifi-bouncer> |
| woodonggyu/cti | tool | <https://github.com/woodonggyu/cti> |
| woodonggyu/nvd-feed | dataset | <https://github.com/woodonggyu/nvd-feed> |
| woodonggyu/virustotal-api | api-service | <https://github.com/woodonggyu/virustotal-api> |
| World Monitor Tech | dashboard | <https://tech.worldmonitor.app> |
| wrhalpin/GNAT | research-project | <https://github.com/wrhalpin/GNAT> |
| wrhalpin/SandGNAT | research-project | <https://github.com/wrhalpin/SandGNAT> |
| x-KUNAL-x/CYBERSECURITY-TASK-3 | web-platform | <https://github.com/x-KUNAL-x/CYBERSECURITY-TASK-3> |
| x-KUNAL-x/CYBERSECURITY-TASK-5 | tool | <https://github.com/x-KUNAL-x/CYBERSECURITY-TASK-5> |
| x-KUNAL-x/CYBERSECURITY-TASK-7 | browser-extension | <https://github.com/x-KUNAL-x/CYBERSECURITY-TASK-7> |
| x-KUNAL-x/CYBERSECURITY-TASK-8 | tool | <https://github.com/x-KUNAL-x/CYBERSECURITY-TASK-8> |
| x3m-ai/Camelot | dashboard | <https://github.com/x3m-ai/Camelot> |
| xakepnz/BLUELAY | tool | <https://github.com/xakepnz/BLUELAY> |
| xakepnz/enterpriseattack | plugin | <https://github.com/xakepnz/enterpriseattack> |
| Xanderux/C2watcher | dataset | <https://github.com/Xanderux/C2watcher> |
| xaphody/SOC-Analyst-Tool | tool | <https://github.com/xaphody/SOC-Analyst-Tool> |
| xbox_monitor | web-platform | <https://github.com/misiektoja/xbox_monitor> |
| xdrew87/nexusintel | api-service | <https://github.com/xdrew87/nexusintel> |
| XenoCoreGiger31/README.md | tool | <https://github.com/XenoCoreGiger31/README.md> |
| xn-twist/xn-twist | tool | <https://github.com/xn-twist/xn-twist> |
| yankywilson/jdy-botnet-threat-analysis | tool | <https://github.com/yankywilson/jdy-botnet-threat-analysis> |
| yankywilson/jdy-tasking-decryption | tool | <https://github.com/yankywilson/jdy-tasking-decryption> |
| yankywilson/kyber-ransomware-analysis | dashboard | <https://github.com/yankywilson/kyber-ransomware-analysis> |
| yankywilson/m365-bec-estate-2026 | tool | <https://github.com/yankywilson/m365-bec-estate-2026> |
| yassinmohamed1111/rodork | api-service | <https://github.com/yassinmohamed1111/rodork> |
| Yavuzlar/CTI-Reports | tool | <https://github.com/Yavuzlar/CTI-Reports> |
| yeti-platform/pyeti | api-service | <https://github.com/yeti-platform/pyeti> |
| yeti-platform/yeti | web-platform | <https://github.com/yeti-platform/yeti> |
| yoelapu/intelstrike | tool | <https://github.com/yoelapu/intelstrike> |
| yogsec/Hacking-Tools | awesome-list | <https://github.com/yogsec/Hacking-Tools> |
| yorkeccak/globalhackmap | cli-tool | <https://github.com/yorkeccak/globalhackmap> |
| yukh1402/cti-stix-diamond-activity-attack-graph | tool | <https://github.com/yukh1402/cti-stix-diamond-activity-attack-graph> |
| Yuning-J/VulnerabilityClassifier | tool | <https://github.com/Yuning-J/VulnerabilityClassifier> |
| yvesstan/SIEM_Solution-Research-Project | research-project | <https://github.com/yvesstan/SIEM_Solution-Research-Project> |
| zahidayturan/go-tor-scraper | api-service | <https://github.com/zahidayturan/go-tor-scraper> |
| zahidayturan/go-web-scraper-cti | api-service | <https://github.com/zahidayturan/go-web-scraper-cti> |
| ZakariaHibaoui2/threat-intel-ioc-extractor | tool | <https://github.com/ZakariaHibaoui2/threat-intel-ioc-extractor> |
| Zakurath/AI-Threat-Aggregator | tool | <https://github.com/Zakurath/AI-Threat-Aggregator> |
| zaneGittins/bifract | cli-tool | <https://github.com/zaneGittins/bifract> |
| zdhenard42/SOC-Multitool | browser-extension | <https://github.com/zdhenard42/SOC-Multitool> |
| zerber0s/BF-ELK | tool | <https://github.com/zerber0s/BF-ELK> |
| Zeroska/Ordo | tool | <https://github.com/Zeroska/Ordo> |
| zerty/Benny-Edition-CTI-0.97-Zerty-Modification | tool | <https://github.com/zerty/Benny-Edition-CTI-0.97-Zerty-Modification> |
| zhiephie/cti | plugin | <https://github.com/zhiephie/cti> |
| Zikmadol/trapline-ioc | dataset | <https://github.com/Zikmadol/trapline-ioc> |
| zinwave/cti-kit | plugin | <https://github.com/zinwave/cti-kit> |
| ZishanAdThandar/hackify | tool | <https://github.com/ZishanAdThandar/hackify> |
| ziyadnz/threat-intel-ip-feeds | web-platform | <https://github.com/ziyadnz/threat-intel-ip-feeds> |
| zsazsa-project/zsazsa | web-platform | <https://github.com/zsazsa-project/zsazsa> |
| zshguy/tyrian-detection-pack | directory | <https://github.com/zshguy/tyrian-detection-pack> |
| Zypherion-Technologies/HallWatch | tool | <https://github.com/Zypherion-Technologies/HallWatch> |

<!-- COMPLETE_DARK_WEB_URL_INDEX_END -->
