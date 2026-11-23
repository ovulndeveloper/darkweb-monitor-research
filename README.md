# Dark Web Monitor Research Repo

A curated collection of dark web monitoring tools with rankings, categories, and platform support (Windows/Linux).

## Purpose

This repository serves as a research resource for comparing dark web monitoring tools by category and capability, finding tools compatible with Windows and Linux platforms, understanding tool rankings and focus areas, and researching open-source and commercial dark web monitoring solutions.

## Tool Categories

### 1. OSINT Automation & Frameworks

Tools that provide comprehensive OSINT automation and data aggregation.

| Tool | Rank | Primary Focus | Windows | Linux | Description |
|------|------|--------------|---------|-------|-------------|
| SpiderFoot | ⭐⭐⭐⭐⭐ | General OSINT, threat intelligence | ✅ | ✅ | Automates OSINT for threat intelligence and attack surface mapping. Integrates with 100+ data sources including dark web sites, breach databases, and Tor exit nodes. |
| Darkdump | ⭐⭐⭐⭐ | Deep web scraping, search | ❌ | ✅ | OSINT interface for deep web scraping. Fetches results from multiple dark web search engines, supports deep scraping, and includes breach intelligence mode. |

### 2. Dark Web Exposure & Monitoring

Tools specifically focused on monitoring ransomware leak sites, breach data, and exposure.

| Tool | Rank | Primary Focus | Windows | Linux | Description |
|------|------|--------------|---------|-------|-------------|
| Darkwatch | ⭐⭐⭐⭐ | Ransomware leak sites, breach monitoring | ✅ | ✅ | Dark web exposure monitor that watches ransomware leak sites, breach/paste data, and onion pages over managed Tor. Scores every hit and provides remediation recommendations. |
| TorBot | ⭐⭐⭐ | Onion service crawling | ❌ | ✅ | Python-based crawler for onion services. Can be used for dark web monitoring and data collection. |

### 3. Search Engines & Directories

Tools for searching and discovering dark web content.

| Tool | Rank | Primary Focus | Windows | Linux | Description |
|------|------|--------------|---------|-------|-------------|
| Ahmia | ⭐⭐⭐⭐⭐ | Dark web search engine | ✅ (via Tor Browser) | ✅ (via Tor Browser) | Clearnet-accessible dark web search engine with filtering. Indexes Tor hidden services with strict abuse filtering. |
| Torch | ⭐⭐⭐⭐ | General dark web search | ✅ (via Tor Browser) | ✅ (via Tor Browser) | One of the oldest and largest dark web search engines. |

### 4. Breach & Credential Monitoring

Tools and services focused on compromised data monitoring.

| Tool | Rank | Primary Focus | Windows | Linux | Description |
|------|------|--------------|---------|-------|-------------|
| HaveIBeenPwned Integration | ⭐⭐⭐⭐⭐ | Breach data monitoring | ✅ | ✅ | Industry-standard breach monitoring service. API available for integration. |
| Intelligence X | ⭐⭐⭐⭐ | Historical data search | ✅ | ✅ | Search engine for breached data, leaked documents, and dark web content. |

### 5. Commercial/Enterprise Solutions

(Note: These are commercial services, not open-source tools)

| Tool | Rank | Primary Focus | Windows | Linux | Description |
|------|------|--------------|---------|-------|-------------|
| ZeroFox | ⭐⭐⭐⭐⭐ | Enterprise dark web monitoring | ✅ | ✅ | Comprehensive dark web monitoring with credential, personal info, and IP monitoring. |
| Recorded Future | ⭐⭐⭐⭐⭐ | Threat intelligence | ✅ | ✅ | AI-powered threat intelligence platform with dark web monitoring capabilities. |## 📈 Ranking System
Tools are ranked based on:
- ⭐⭐⭐⭐⭐ (5 stars): Industry-leading, comprehensive coverage, highly rated
- ⭐⭐⭐⭐ (4 stars): Strong capabilities, good reputation
- ⭐⭐ (2 stars): Basic functionality, limited features
- ⭐⭐⭐ (3 stars): Functional, niche-focused
- ⭐ (1 star): Experimental or very specialized
Ranking considers: features, user reviews, platform support, integration capabilities, and community adoption.

## 🖥️ Platform Support Legend
- ✅ Full support - Tool officially supports or works well on this platform
- ❌ No support - Tool does not support this platform
- 🌐 Via Tor Browser - Accessible through Tor browser on any platform

## 🔍 How to Use This Repository
1. Browse categories above to find tools matching your needs
2. Check platform compatibility column for Windows/Linux support
3. Review rankings to prioritize tools
4. Follow links to GitHub repos or official sites for more details
5. Contribute - Add new tools or update existing entries via Pull Requests

## 📂 Repository Structure
- `README.md` - This file - overview and categories
- `tools_catalog.md` - Detailed tool catalog (will be created)
- `categories/` - Category-specific documentation
- `ranking_criteria.md` - How tools are ranked
- `CONTRIBUTING.md` - Guidelines for contributing

## 🤝 Contributing
We welcome contributions! To add or update tools:
1. Fork the repository
2. Add tool to the appropriate category in `tools_catalog.md`
3. Follow the existing format and ranking criteria
4. Submit a Pull Request

Please ensure tools are:
- Relevant to dark web monitoring
- Have documentation or open-source availability
- Support Windows and/or Linux (or clearly note platform limitations)

## ⚠️ Legal & Ethical Notice
- Only monitor dark web content you have permission to access
- Comply with all applicable laws and regulations
- Use tools responsibly for legitimate security research and defense purposes
- Respect privacy and legal boundaries when accessing dark web content
*Last updated: November 2026*
