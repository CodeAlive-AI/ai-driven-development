#!/bin/sh
set -eu
source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
fixture_dir=$(mktemp -d "${TMPDIR:-/tmp}/space-scan-build.XXXXXX")
trap 'rm -rf "$fixture_dir"' EXIT HUP INT TERM
cp "$source_dir/space_scan.cpp" "$source_dir/core.hpp" "$fixture_dir/"
cp -R "$source_dir/tests" "$fixture_dir/tests"
xcrun clang++ -O3 -std=c++17 -Wall -Wextra -pthread "$fixture_dir/space_scan.cpp" -o "$fixture_dir/space_scan"
xcrun clang++ -O1 -g -std=c++17 -fsanitize=address,undefined "$fixture_dir/tests/core_tests.cpp" -o "$fixture_dir/core_tests"
"$fixture_dir/core_tests"
python3 "$fixture_dir/tests/integration_macos.py"
python3 "$fixture_dir/tests/tree_macos.py"
