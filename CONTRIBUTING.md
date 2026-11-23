# Contributing

Thanks for helping keep this research current.

## Adding a tool to `rsearch/`

1. Check `rsearch/registry/exclusions.json` first. If the tool is already in the root README, `tools_catalog.md`, or `categories/`, do not add it to `rsearch`.
2. Add a JSON object to `rsearch/registry/tools.json` with: `id`, `name`, `category`, `type`, `url`, `repo` (if any), `aliases`, `platforms`, `license`, `rank`, `summary`, `capabilities`, `evidence`, `metrics`, `verified`, `status`, and optional `safety_note`.
3. Use at least one primary-source URL in `evidence` (official site, repository, or docs).
4. Run the offline checks:

```sh
python3 -m unittest discover -s rsearch/automation -p 'test_*.py' -v
python3 rsearch/automation/refresh_catalog.py --offline
```

5. Commit `registry/tools.json` and the regenerated `rsearch/CATALOG.md`, `STATUS.json`, and `CHANGELOG.md`. Never hand-edit generated files.

## Updating a legacy tool

Edit the legacy file directly (`README.md`, `tools_catalog.md`, or `categories/`) and add a note to `rsearch/RECONCILIATION.md` if the change conflicts with new research.

## Candidate review

`rsearch/automation/discover_candidates.py` writes staged candidates to `rsearch/candidates/`. Promotion requires a human check of the primary source and a dedupe pass. Do not auto-promote.

## Scope

Defensive security research, OSINT, and journalism only. No weaponized exploit code, no stolen data, no targeting of people, and no unauthorized access instructions.
