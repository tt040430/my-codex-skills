#!/usr/bin/env bash
set -eu
root="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$root/scripts/sync_references.py" --check
