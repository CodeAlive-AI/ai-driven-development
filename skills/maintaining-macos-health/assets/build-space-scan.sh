#!/bin/sh
set -eu
# Explicit local build; no downloads and no automatic installation.
if [ "$#" -ne 1 ]; then
    echo 'usage: build-space-scan.sh OUTPUT_BINARY' >&2
    exit 2
fi
source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
xcrun clang++ -O3 -std=c++17 -Wall -Wextra -Wpedantic -pthread "$source_dir/space-scan/space_scan.cpp" -o "$1"
