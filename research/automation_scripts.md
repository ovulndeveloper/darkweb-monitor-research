# Automation Scripts

The placeholder scripts below were replaced by a real, testable pipeline in [`rsearch/`](../rsearch/README.md).

## Live scripts

| Script | Purpose |
|---|---|
| [`rsearch/automation/refresh_catalog.py`](../rsearch/automation/refresh_catalog.py) | Validates the registry, refreshes GitHub/HTTP metadata, renders `CATALOG.md`, `STATUS.json`, and `CHANGELOG.md` |
| [`rsearch/automation/discover_candidates.py`](../rsearch/automation/discover_candidates.py) | Discovers candidates from GitHub search and DuckDuckGo HTML, deduplicates, and stages them in `rsearch/candidates/` |
| [`rsearch/automation/test_research.py`](../rsearch/automation/test_research.py) | Offline tests for normalization, dedupe, exclusions, evidence, and catalog completeness |
| [`rsearch/automation/watch.sh`](../rsearch/automation/watch.sh) | Optional local infinite loop for continuous refreshes |
| [`.github/workflows/research-auto-update.yml`](../.github/workflows/research-auto-update.yml) | Hosted 6-hour schedule with conditional commit |

## Usage

```sh
# From the repository root
python3 -m unittest discover -s rsearch/automation -p 'test_*.py' -v
python3 rsearch/automation/refresh_catalog.py --offline
GITHUB_TOKEN=... python3 rsearch/automation/refresh_catalog.py
python3 rsearch/automation/discover_candidates.py
INTERVAL=21600 sh rsearch/automation/watch.sh
```

## Promotion gate

Discovery never edits the verified registry. A human must check the primary source, assign an evidence URL and verification date, then add the tool to `rsearch/registry/tools.json`. The offline tests block duplicate or evidence-free entries.

*Last verified: 2026-11-23 (UTC)*
