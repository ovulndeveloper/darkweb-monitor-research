--- Dark Web Monitor Tools Catalog ---

How to Read This Catalog
Each tool entry includes:
• Name - Tool name with link to GitHub/repo
• Rank - ⭐ rating based on features, adoption, and capabilities
• Primary Focus - Main purpose and capabilities
• Windows Support - ✅/❌/🌐
• Linux Support - ✅/❌/🌐
• Key Features - Main functionalities
• Best For - Ideal use cases

1. OSINT Automation & Frameworks

## 1. OSINT Automation & Frameworks
### SpiderFoot
• GitHub: https://github.com/smicallef/spiderfoot
• Rank: ⭐⭐⭐⭐⭐
• Primary Focus: General OSINT, threat intelligence automation
• Windows: ✅ (via Python, installer available)
• Linux: ✅ (native, via package manager or pip)
• Key Features:
   - Integrates with 100+ data sources including dark web sites
   - Web-based interface and CLI
   - Tor exit node detection
   - Breach database monitoring
   - Custom module development
• Best For: Comprehensive OSINT investigations, threat intelligence gathering, attack surface mapping

### Darkdump
• GitHub: https://github.com/josh0xA/darkdump
• Rank: ⭐⭐⭐⭐
• Primary Focus: Deep web scraping, search engine aggregation
• Windows: ❌ (limited, requires Wine/X11 forwarding)
• Linux: ✅ (primary platform)
• Key Features:
   - Six dark web search engines supported
   - Deep scraping with metadata extraction
   - Breach intelligence mode
   - Ahmia blacklist filtering
   - CLI and web interface
• Best For: Deep web searching, email/metadata extraction, breach credential research
## 2. Dark Web Exposure & Monitoring

### Darkwatch
• GitHub: https://github.com/Daemon-VI/darkwatch
• Rank: ⭐⭐⭐⭐
• Primary Focus: Ransomware leak site monitoring, breach data exposure
• Windows: ✅ (via schtasks, desktop alerts)
• Linux: ✅ (via systemd, cron)
• Key Features:
   - Watches ransomware leak sites over managed Tor
   - Scores every hit by context
   - Remediation recommendations (change passwords, enable MFA, etc.)
   - Tor Expert Bundle auto-download
   - Desktop alerts and daily scheduled runs
   - SARIF format for GitHub code scanning
• Best For: Organization exposure monitoring, ransomware risk assessment, individual/digital identity protection
### TorBot
• GitHub: https://github.com/A-deker0/TorBot
• Rank: ⭐⭐⭐
• Primary Focus: Onion service crawling and data collection
• Windows: ❌
• Linux: ✅ (Python-based)
• Key Features:
   - Python-based onion service crawler
   - Configurable depth and breadth
   - Extracts metadata, keywords, documents
   - Can be used for dark web monitoring setups
• Best For: Custom dark web crawling, research data collection, academic studies
## 3. Search Engines & Directories

### Ahmia
• Website: https://ahmia.fi
• Rank: ⭐⭐⭐⭐⭐
• Primary Focus: Filtered dark web search engine
• Windows: ✅ (via Tor Browser)
• Linux: ✅ (via Tor Browser)
• Key Features:
   - Clearnet-accessible .onion search
   - Strict abuse filtering
   - Indexes Tor hidden services only
   - API available
   - Search statistics and reports
• Best For: Safe dark web searching, research with filtering, discovering onion services

### Torch
• Address: http://xmh57jrzrnw6iuq7.onion
• Rank: ⭐⭐⭐⭐
• Primary Focus: General dark web search
• Windows: ✅ (via Tor Browser)
• Linux: ✅ (via Tor Browser)
• Key Features:
   - One of oldest/darkweb search engines
   - Large index of .onion sites
   - Simple .onion address
   - No filtering (broad results)
• Best For: General dark web exploration, finding lesser-known services
### NotEvil
• Address: http://noteilv6w5w.onion
• Rank: ⭐⭐⭐
• Primary Focus: Privacy-focused dark web search
• Windows: ✅ (via Tor Browser)
• Linux: ✅ (via Tor Browser)
• Key Features:
   - Privacy-oriented indexing
   - Smaller, curated index
   - Focus on legitimacy
• Best For: Privacy-conscious searching, finding verified services
## 4. Breach & Credential Monitoring

### HaveIBeenPwned Integration
- Website: https://haveibeenpwned.com
- Rank: ⭐⭐⭐⭐⭐
- Primary Focus: Breach data monitoring and checking
- Windows: ✅ (web interface, API integrations)
- Linux: ✅ (web interface, API integrations)
- Key Features:
  - World's largest breach database
  - API for automated checking
  - Domain monitoring
  - Paste site monitoring
  - Free and premium tiers
- Best For: Individual/company breach checking, API integrations, incident response

### Intelligence X
- Website: https://intelx.io
- Rank: ⭐⭐⭐⭐
- Primary Focus: Historical data search and breach analysis
- Windows: ✅ (web interface)
- Linux: ✅ (web interface)
- Key Features:
  - Search breached data, leaked documents
  - Dark web content monitoring
  - Historical website snapshots
  - API access
  - Multiple search criteria (email, phone, IP, etc.)
- Best For: Deep breach investigations, historical analysis, forensic research

## 5. Commercial/Enterprise Solutions

### ZeroFox
- Website: https://www.zerofox.com
- Rank: ⭐⭐⭐⭐⭐
- Primary Focus: Enterprise dark web monitoring
- Windows: ✅ (dashboard, agents)
- Linux: ✅ (dashboard, APIs)
- Key Features:
  - Comprehensive credential monitoring
  - Personal information surveillance
  - Brand/ IP monitoring
  - AI-powered alert triaging
  - Executive protection
  - Integration with SIEM platforms
- Best For: Enterprises, CISOs, large organizations, compliance requirements

### Recorded Future
- Website: https://www.recordedfuture.com
- Rank: ⭐⭐⭐⭐⭐
- Primary Focus: AI-powered threat intelligence
- Windows: ✅ (platform, integrations)
- Linux: ✅ (platform, integrations)
- Key Features:
  - Predictive threat intelligence
  - Dark web monitoring and analysis
  - TTP (tactics, techniques, procedures) tracking
  - Vulnerability intelligence
  - API and platform integrations
- Best For: Threat hunting, proactive defense, large security operations

### Flashpoint
- Website: https://flashpointintel.com
- Rank: ⭐⭐⭐⭐
- Primary Focus: Cybercrime intelligence
- Windows: ✅ (platform)
- Linux: ✅ (platform)
- Key Features:
  - Cybercrime forum monitoring
  - Dark market tracking
  - Malware intelligence
  - Attribution capabilities
  - Customizable alerts
- Best For: Cybercrime investigation, fraud prevention, intelligence gathering

## Platform Support Summary

| Category | Windows Tools | Linux Tools |
|----------|--------------|-------------|
| OSINT Frameworks | SpiderFoot (✅) | SpiderFoot, Darkdump (✅) |
| Exposure Monitoring | Darkwatch (✅) | Darkwatch (✅) |
| Search Engines | All via Tor Browser | All via Tor Browser |
| Breach Monitoring | HaveIBeenPwned (✅) | HaveIBeenPwned (✅) |
| Commercial Solutions | All support (✅) | All support (✅) |

## Ranking Criteria

Tools are evaluated and ranked on:
1. Feature completeness (40%) - Capabilities, integration, automation
2. Platform compatibility (20%) - Windows/Linux support quality
3. Community adoption (20%) - Stars, forks, user base, reviews
4. Update frequency (10%) - Active maintenance, new features
5. Documentation quality (10%) - Clarity, tutorials, API docs

Ranking scale:
- ⭐⭐⭐⭐⭐ Excellent across all criteria
- ⭐⭐⭐⭐ Strong in most criteria, minor limitations
- ⭐⭐⭐ Good for specific use cases
- ⭐⭐ Basic functionality, limited features
- ⭐ Experimental or very niche

*Last verified: 2026-11-23 (UTC)*
### Photon
• GitHub: https://github.com/icyPhoton/Photon
• Rank: ⭐⭐⭐⭐
• Primary Focus: Advanced web crawling and analysis
• Windows: ✅ (via Python)
• Linux: ✅ (native)
• Key Features:
   - Advanced web crawling capabilities
   - JavaScript rendering
   - URL parameter extraction
   - Dark web support via Tor
   - Export to multiple formats
• Best For: Advanced web intelligence, JavaScript-heavy dark web sites, SEO analysis

### WeLeakInfo
• Website: https://weleakinfo.com
• Rank: ⭐⭐⭐
• Primary Focus: Breach data lookup and verification
• Windows: ✅ (web interface)
• Linux: ✅ (web interface)
• Key Features:
   - Verified breach data database
   - Email and password combination search
   - Subscription-based access
   - Daily updates
   - Search history
• Best For: Breach data verification, checking specific email/password combinations
### theHarvester
• GitHub: https://github.com/laramnesis/theHarvester
• Rank: ⭐⭐⭐⭐
• Primary Focus: Email extraction and reconnaissance
• Windows: ✅ (via Python)
• Linux: ✅ (native)
• Key Features:
   - Email extraction from search engines
   - DNS enumeration
   - Crawler for harvesting emails
   - Multiple output formats
• Best For: Email reconnaissance, footprinting, OSINT gathering

### Recon-ng
• GitHub: https://github.com/lanjelot/recon-ng
• Rank: ⭐⭐⭐⭐
• Primary Focus: Modular OSINT framework
• Windows: ✅ (via Wine)
• Linux: ✅ (native)
• Key Features:
   - Modular framework with plugins
   - Database management
   - Module system for extended functionality
   - Dark web support via Tor
• Best For: Comprehensive OSINT framework, modular reconnaissance

### OSRFramework
• GitHub: https://github.com/OSRFramework
• Rank: ⭐⭐⭐
• Primary Focus: OSINT tools collection
• Windows: ✅ (via Python)
• Linux: ✅ (native)
• Key Features:
   - Collection of OSINT tools
   - Multiple data sources
   - Command line interface
• Best For: OSINT tool collection, various data sources

### We Leak Info
• Website: https://weleakinfo.com
• Rank: ⭐⭐⭐
• Primary Focus: Breach data lookup
• Windows: ✅ (web interface)
• Linux: ✅ (web interface)
• Key Features:
   - Verified breach database
   - Email and password search
   - Subscription-based
• Best For: Breach data lookup, password checks
### theHarvester
• GitHub: https://github.com/laramnesis/theHarvester
• Rank: ⭐⭐⭐⭐
• Primary Focus: Email extraction and reconnaissance
• Windows: ✅ (via Python)
• Linux: ✅ (native)
• Key Features:
   - Email extraction from search engines
   - DNS enumeration
   - Crawler for harvesting emails
   - Multiple output formats
• Best For: Email reconnaissance, footprinting, OSINT gathering

### Recon-ng
• GitHub: https://github.com/lanjelot/recon-ng
• Rank: ⭐⭐⭐⭐
• Primary Focus: Modular OSINT framework
• Windows: ✅ (via Wine)
• Linux: ✅ (native)
• Key Features:
   - Modular framework with plugins
   - Database management
   - Module system for extended functionality
   - Dark web support via Tor
• Best For: Comprehensive OSINT framework, modular reconnaissance

### OSRFramework
• GitHub: https://github.com/OSRFramework
• Rank: ⭐⭐⭐
• Primary Focus: OSINT tools collection
• Windows: ✅ (via Python)
• Linux: ✅ (native)
• Key Features:
   - Collection of OSINT tools
   - Multiple data sources
   - Command line interface
• Best For: OSINT tool collection, various data sources

### We Leak Info
• Website: https://weleakinfo.com
• Rank: ⭐⭐⭐
• Primary Focus: Breach data lookup
• Windows: ✅ (web interface)
• Linux: ✅ (web interface)
• Key Features:
   - Verified breach database
   - Email and password search
   - Subscription-based
• Best For: Breach data lookup, password checks
### theHarvester
• GitHub: https://github.com/laramnesis/theHarvester
• Rank: ⭐⭐⭐⭐
• Primary Focus: Email extraction and reconnaissance
• Windows: ✅ (via Python)
• Linux: ✅ (native)
• Key Features:
   - Email extraction from search engines
   - DNS enumeration
   - Crawler for harvesting emails
   - Multiple output formats
• Best For: Email reconnaissance, footprinting, OSINT gathering

### Recon-ng
• GitHub: https://github.com/lanjelot/recon-ng
• Rank: ⭐⭐⭐⭐
• Primary Focus: Modular OSINT framework
• Windows: ✅ (via Wine)
• Linux: ✅ (native)
• Key Features:
   - Modular framework with plugins
   - Database management
   - Module system for extended functionality
   - Dark web support via Tor
• Best For: Comprehensive OSINT framework, modular reconnaissance

### OSRFramework
• GitHub: https://github.com/OSRFramework
• Rank: ⭐⭐⭐
• Primary Focus: OSINT tools collection
• Windows: ✅ (via Python)
• Linux: ✅ (native)
• Key Features:
   - Collection of OSINT tools
   - Multiple data sources
   - Command line interface
• Best For: OSINT tool collection, various data sources

### We Leak Info
• Website: https://weleakinfo.com
• Rank: ⭐⭐⭐
• Primary Focus: Breach data lookup
• Windows: ✅ (web interface)
• Linux: ✅ (web interface)
• Key Features:
   - Verified breach database
   - Email and password search
   - Subscription-based
• Best For: Breach data lookup, password checks
