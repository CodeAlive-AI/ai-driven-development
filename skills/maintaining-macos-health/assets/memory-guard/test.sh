#!/bin/sh
set -eu
source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
fixture_dir=$(mktemp -d "${TMPDIR:-/tmp}/memory-guard-test.XXXXXX")
trap 'rm -rf "$fixture_dir"' EXIT HUP INT TERM
gate="$source_dir/../memory-pressure-gate.sh"
sh "$gate" run xcrun clang++ -O1 -g -std=c++17 -Wall -Wextra \
  -fsanitize=address,undefined "$source_dir/tests/core_tests.cpp" \
  -o "$fixture_dir/core_tests"
sh "$gate" run "$fixture_dir/core_tests"
sh "$source_dir/tests/integration.sh"
