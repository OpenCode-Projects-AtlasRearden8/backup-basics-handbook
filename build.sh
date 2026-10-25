#!/bin/sh
# Build the Backup Basics Handbook static site into site/.
set -e
cd "$(dirname "$0")"
exec python3 build.py "$@"
