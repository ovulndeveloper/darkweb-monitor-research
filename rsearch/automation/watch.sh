#!/bin/sh
# Optional local "never stop" watcher. Stop with Ctrl-C.
# GitHub Actions already runs the same jobs every 6 hours; this is for a local machine.
set -eu
INTERVAL="${INTERVAL:-21600}"
DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
cd "$DIR/.."

while :; do
  echo "[$] refresh $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  python3 automation/refresh_catalog.py
  echo "[$] discover $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  python3 automation/discover_candidates.py
  echo "[$] sleep ${INTERVAL}s"
  sleep "$INTERVAL"
done
