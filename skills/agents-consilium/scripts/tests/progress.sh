#!/bin/bash
# Review-mode observability tests. Sourced by run.sh (uses its assert_* helpers,
# PASS/FAIL, fake backends, and $TMP).
#
# What must hold:
#   - every review depth accepts --progress full|compact|none and rejects junk
#   - none is total silence on stderr, while stdout still carries the report
#   - compact is content-free (counters), full carries per-agent previews
#   - progress identity is the invocation (agent, agent.role), so parallel
#     passes of the same agent are distinguishable live
#   - run ids and run dirs are human-readable word pairs, not raw hex

echo "=== review progress: CLI contract ==="

# Earlier sections pin CONSILIUM_RUN_DIR to inspect artifacts; these tests need
# the auto-created (human-named) run dir instead.
unset CONSILIUM_RUN_DIR

PT="$TMP/progress"
mkdir -p "$PT"
PSRC="$PT/sample.py"
cat > "$PSRC" <<'EOF'
def divide(a, b):
    return a / b
EOF

assert_matches() {
  local name="$1" value="$2" pattern="$3"
  if printf '%s' "$value" | grep -Eq "$pattern"; then
    echo "  PASS  $name"
    PASS=$((PASS+1))
  else
    echo "  FAIL  $name"
    echo "        got:     $value"
    echo "        pattern: $pattern"
    FAIL=$((FAIL+1))
  fi
}

out=$("$CONSILIUM" review ask --progress bogus "q" 2>&1) && rc=0 || rc=$?
assert_eq "ask rejects unknown --progress" "$rc" "5"
assert_contains "ask --progress error names the values" "$out" "full, compact, or none"

out=$("$CONSILIUM" review code --progress bogus "$PSRC" 2>&1) && rc=0 || rc=$?
assert_eq "code rejects unknown --progress" "$rc" "5"

out=$("$CONSILIUM" review code --depth super --progress bogus "$PSRC" 2>&1) && rc=0 || rc=$?
assert_eq "super rejects unknown --progress" "$rc" "5"

out=$("$CONSILIUM" review code --depth ultra --progress bogus "$PSRC" 2>&1) && rc=0 || rc=$?
assert_eq "ultra rejects unknown --progress" "$rc" "5"

out=$("$CONSILIUM" review ask --help 2>&1) || true
assert_contains "ask help documents --progress" "$out" "--progress full|compact|none"

out=$("$CONSILIUM" review code --help 2>&1) || true
assert_contains "code help documents --progress" "$out" "--progress <full|compact|none>"

out=$("$CONSILIUM" --help 2>&1) || true
assert_contains "top-level help documents progress styles" "$out" "Live progress (all review depths)"
assert_contains "top-level help names CONSILIUM_PROGRESS" "$out" "CONSILIUM_PROGRESS"

echo "=== review progress: styles ==="

# full (default): per-agent previews reach stderr while the run is in flight.
"$CONSILIUM" review ask -a codex "explain" >"$PT/full.out" 2>"$PT/full.err" || true
full_err="$(cat "$PT/full.err")"
assert_contains "full progress starts the agent" "$full_err" "start agent=codex"
assert_contains "full progress finishes the agent" "$full_err" "done agent=codex status=ok"
assert_contains "full progress previews content" "$full_err" "type=text data="
assert_file "full progress leaves stdout intact" "$PT/full.out"

# compact: liveness only — counters, never model content.
"$CONSILIUM" review ask --progress compact -a codex "explain" >"$PT/compact.out" 2>"$PT/compact.err" || true
compact_err="$(cat "$PT/compact.err")"
assert_contains "compact progress emits counters" "$compact_err" "chunks="
assert_contains "compact progress emits elapsed" "$compact_err" "elapsed="
assert_not_contains "compact progress carries no content" "$compact_err" "type=text data="
assert_file "compact progress leaves stdout intact" "$PT/compact.out"

# none: silence, including the orchestrator's own stage lines.
"$CONSILIUM" review ask --progress none -a codex "explain" >"$PT/none.out" 2>"$PT/none.err" || true
assert_eq "none is silent on stderr" "$(wc -c < "$PT/none.err" | tr -d ' ')" "0"
assert_file "none still answers on stdout" "$PT/none.out"

# The env fallback is what a wrapper sets once for a whole session.
CONSILIUM_PROGRESS=none "$CONSILIUM" review ask -a codex "explain" >/dev/null 2>"$PT/env.err" || true
assert_eq "CONSILIUM_PROGRESS=none is honored" "$(wc -c < "$PT/env.err" | tr -d ' ')" "0"

# Silence must not swallow the report itself, nor real failures.
"$CONSILIUM" review code --depth basic --progress none -a codex "$PSRC" >"$PT/code-none.out" 2>"$PT/code-none.err" || true
assert_eq "code none is silent on stderr" "$(wc -c < "$PT/code-none.err" | tr -d ' ')" "0"
assert_file "code none still reports on stdout" "$PT/code-none.out"

echo "=== review progress: per-invocation identity ==="

# Code review runs one agent per role. Progress must name the role, otherwise
# two concurrent passes of the same agent are indistinguishable on stderr.
"$CONSILIUM" review code --depth basic -a codex "$PSRC" >/dev/null 2>"$PT/code.err" || true
code_err="$(cat "$PT/code.err")"
assert_contains "code progress keys the security pass" "$code_err" "agent=codex.security"
assert_contains "code progress keys the correctness pass" "$code_err" "agent=codex.correctness"
assert_contains "code progress reports per-pass completion" "$code_err" "done agent=codex.security"

# ask has no per-role fan-out: the plain agent id stays the key.
assert_not_contains "ask progress keeps the plain agent id" "$full_err" "agent=codex."

echo "=== human-readable run ids ==="

assert_matches "human id is two words plus a short tail" \
  "$(python3 "$LIB_DIR/human_id.py" "run_")" '^run_[a-z]+-[a-z]+-[0-9a-f]{4}$'

uniq_count=$(python3 -c "
import sys
sys.path.insert(0, '$LIB_DIR')
from human_id import human_id
print(len({human_id('run_') for _ in range(200)}))
")
assert_eq "human ids stay unique over 200 draws" "$uniq_count" "200"

# The artifact run dir is quoted back to the caller — it must read as words.
run_parent="$PT/outputs"
mkdir -p "$run_parent"
CONSILIUM_OUTPUT_DIR="$run_parent" "$CONSILIUM" review ask -a codex "explain" >/dev/null 2>"$PT/rundir.err" || true
run_dir_name="$(basename "$(find "$run_parent" -maxdepth 1 -mindepth 1 -type d | head -1)")"
assert_matches "run dir reads as words" "$run_dir_name" '^run-ask-[a-z]+-[a-z]+-[0-9a-f]{4}$'
assert_contains "run dir path is reported live" "$(cat "$PT/rundir.err")" "run_dir=$run_parent/"

# Delegate's steerable run id is typed by hand into `delegate status <id>`.
steer_id=$(python3 -c "
import sys
sys.path.insert(0, '$LIB_DIR')
from steer.util import new_run_id
print(new_run_id('run_'))
")
assert_matches "steerable run id reads as words" "$steer_id" '^run_[a-z]+-[a-z]+-[0-9a-f]{4}$'
