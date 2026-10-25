#!/bin/sh
# Verify the handbook: run the build, then page/link/credit/command checks.
set -e
cd "$(dirname "$0")"
./build.sh >&2
exec python3 test.py
