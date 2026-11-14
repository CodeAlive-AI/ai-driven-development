#!/bin/sh
set -eu
if [ "$#" -ne 1 ]; then echo 'usage: build-memory-guard.sh OUTPUT_BINARY' >&2; exit 2; fi
source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
sh "$source_dir/memory-pressure-gate.sh" run xcrun clang++ -O2 -std=c++17 \
  -Wall -Wextra -Wpedantic -pthread \
  "$source_dir/memory-guard/memory_guard.cpp" -o "$1"
