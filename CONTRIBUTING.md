# Contributing

This repository is a **URL and directory listing**, not a code project. Please add links, categories, types, and source notes — not tool source code, exploit code, or downloadable payloads.

## Adding a URL to `apps/`

1. Check [`apps/data/catalog.json`](apps/data/catalog.json) for the normalized identity (canonical URL or GitHub `owner/repo`). Do not add duplicates.
2. Choose the existing category and type that best fit. Category names are listed in [`apps/CATEGORIES.md`](apps/CATEGORIES.md); types in [`apps/TYPES.md`](apps/TYPES.md).
3. Add one entry to `apps/data/catalog.json` with `id`, `key`, `name`, `url`, `description`, `category`, `type`, `status`, `sources`, and `indexed`.
4. Create one directory under `apps/tools/<category>/<id>/README.md` containing the name, type, category, status, URL, source, and a one-line description.
5. Add the same row to [`apps/README.md`](apps/README.md), the relevant `apps/by-category/<slug>/README.md`, and `apps/by-type/<slug>/README.md`.
6. Keep `sources` pointing to a real public index or primary source. Do not invent URLs.

## Adding a primary-verified entry to `rsearch/`

1. Check `rsearch/registry/exclusions.json` first. If the tool is already in the root README, `tools_catalog.md`, or `categories/`, do not add it to `rsearch`.
2. Add a JSON object to `rsearch/registry/tools.json` with `id`, `name`, `category`, `type`, `url`, `repo` (if any), `aliases`, `platforms`, `license`, `rank`, `summary`, `capabilities`, `evidence`, `metrics`, `verified`, `status`, and optional `safety_note`.
3. Use at least one primary-source URL in `evidence` (official site, repository, or docs).
4. Update `rsearch/CATALOG.md`, `STATUS.json`, and `CHANGELOG.md` to match the registry.

## Updating a legacy tool

Edit the legacy file directly (`README.md`, `tools_catalog.md`, or `categories/`) and add a note to `rsearch/RECONCILIATION.md` if the change conflicts with new research.

## Scope

Defensive security research, OSINT, and journalism only. No weaponized exploit code, no stolen data, no targeting of people, and no unauthorized access instructions. Only valid public HTTP(S) URLs are accepted.
