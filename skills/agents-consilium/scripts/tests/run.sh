#!/bin/bash
# agents-consilium v5 test suite (fake backends only — no network).
set -euo pipefail

TESTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(cd "$TESTS_DIR/.." && pwd)"
LIB_DIR="$SCRIPTS_DIR/lib"
FAKES="$TESTS_DIR/fakes"
FIX="$TESTS_DIR/fixtures"
CONSILIUM="$SCRIPTS_DIR/consilium"

chmod +x "$FAKES"/* "$CONSILIUM" "$LIB_DIR"/*.sh "$LIB_DIR/normalize_stream.py" 2>/dev/null || true

export CONSILIUM_CONFIG="$FIX/test-config.json"
export CONSILIUM_BIN_CODEX="$FAKES/fake-codex"
export CONSILIUM_BIN_CLAUDE="$FAKES/fake-claude"
export CONSILIUM_BIN_OPENCODE="$FAKES/fake-opencode"
export CONSILIUM_BIN_GROK="$FAKES/fake-grok"
export CONSILIUM_BIN_GEMINI="$FAKES/fake-gemini"
export CONSILIUM_SUPPRESS_SHELL_WARN=1
export AGENT_TIMEOUT=30

PASS=0
FAIL=0
assert_eq() {
  local name="$1" got="$2" want="$3"
  if [[ "$got" == "$want" ]]; then
    echo "  PASS  $name"
    PASS=$((PASS+1))
  else
    echo "  FAIL  $name"
    echo "        got:  $got"
    echo "        want: $want"
    FAIL=$((FAIL+1))
  fi
}
assert_contains() {
  local name="$1" hay="$2" needle="$3"
  if [[ "$hay" == *"$needle"* ]]; then
    echo "  PASS  $name"
    PASS=$((PASS+1))
  else
    echo "  FAIL  $name (missing: $needle)"
    echo "        haystack: $hay"
    FAIL=$((FAIL+1))
  fi
}
assert_not_contains() {
  local name="$1" hay="$2" needle="$3"
  if [[ "$hay" != *"$needle"* ]]; then
    echo "  PASS  $name"
    PASS=$((PASS+1))
  else
    echo "  FAIL  $name (unexpected: $needle)"
    FAIL=$((FAIL+1))
  fi
}
assert_file() {
  local name="$1" path="$2"
  if [[ -f "$path" && -s "$path" ]]; then
    echo "  PASS  $name"
    PASS=$((PASS+1))
  else
    echo "  FAIL  $name (missing/empty: $path)"
    FAIL=$((FAIL+1))
  fi
}
assert_le() {
  local name="$1" got="$2" limit="$3"
  if (( got <= limit )); then
    echo "  PASS  $name"
    PASS=$((PASS+1))
  else
    echo "  FAIL  $name (got $got, expected <= $limit)"
    FAIL=$((FAIL+1))
  fi
}

echo "=== CLI dispatch ==="
out=$("$CONSILIUM" --help 2>&1) || true
assert_contains "help mentions review" "$out" "review"
assert_contains "help mentions delegate" "$out" "delegate"

out=$("$CONSILIUM" --list-agents 2>/dev/null)
assert_contains "list-agents has grok" "$out" 'id="grok"'
assert_contains "list-agents has grok-build backend" "$out" 'backend="grok-build"'

out=$(env -u CONSILIUM_CONFIG "$CONSILIUM" --list-agents 2>/dev/null)
assert_contains "default config resolves from skill root" "$out" 'id="grok"'

timeout_state=$(env -u AGENT_TIMEOUT bash -c \
  'source "$1"; printf "%s|%s" "$AGENT_TIMEOUT" "$TIMEOUT_CMD"' \
  _ "$LIB_DIR/common.sh")
assert_eq "default execution has no timeout" "$timeout_state" "0|"

# Unknown command
set +e
"$CONSILIUM" foobar >/dev/null 2>&1
rc=$?
set -e
assert_eq "unknown command exit 5" "$rc" "5"

echo "=== Argv safety (CONSILIUM_DUMP_ARGV) ==="
dump_review() {
  local agent="$1" outfile="$2"
  CONSILIUM_DUMP_ARGV="$outfile" \
    "$LIB_DIR/backend_run.sh" --mode review --agent-id "$agent" --raw "hello" >/dev/null
}
dump_delegate() {
  local agent="$1" outfile="$2"
  CONSILIUM_DUMP_ARGV="$outfile" \
    "$LIB_DIR/backend_run.sh" --mode delegate --agent-id "$agent" --raw "hello" >/dev/null
}

TMP=$(mktemp -d)

# Codex review: sandbox read-only, never full-bypass
dump_review codex "$TMP/codex-review.json"
argv=$(python3 -c 'import json; print(" ".join(json.load(open("'"$TMP/codex-review.json"'"))["argv"]))')
assert_contains "codex review has read-only sandbox" "$argv" "--sandbox read-only"
assert_not_contains "codex review no full bypass" "$argv" "--dangerously-bypass-approvals-and-sandbox"

# Codex delegate: YOLO bypass, no read-only sandbox
dump_delegate codex "$TMP/codex-del.json"
argv=$(python3 -c 'import json; print(" ".join(json.load(open("'"$TMP/codex-del.json"'"))["argv"]))')
assert_contains "codex delegate has YOLO bypass" "$argv" "--dangerously-bypass-approvals-and-sandbox"
assert_not_contains "codex delegate no read-only sandbox" "$argv" "--sandbox read-only"

# Claude review: plan + disallowed write tools
dump_review claude-code "$TMP/claude-review.json"
argv=$(python3 -c 'import json; print(" ".join(json.load(open("'"$TMP/claude-review.json"'"))["argv"]))')
assert_contains "claude review plan mode" "$argv" "--permission-mode plan"
assert_contains "claude review denies Edit" "$argv" "Edit"
assert_not_contains "claude review no skip-permissions" "$argv" "--dangerously-skip-permissions"

# Claude delegate: skip permissions, no plan
dump_delegate claude-code "$TMP/claude-del.json"
argv=$(python3 -c 'import json; print(" ".join(json.load(open("'"$TMP/claude-del.json"'"))["argv"]))')
assert_contains "claude delegate YOLO" "$argv" "--dangerously-skip-permissions"
assert_not_contains "claude delegate no plan" "$argv" "--permission-mode plan"

# OpenCode review: plan agent
dump_review opencode "$TMP/oc-review.json"
argv=$(python3 -c 'import json; print(" ".join(json.load(open("'"$TMP/oc-review.json"'"))["argv"]))')
assert_contains "opencode review plan agent" "$argv" "--agent plan"
assert_not_contains "opencode review no build agent" "$argv" "--agent build"

# OpenCode delegate: build + auto
dump_delegate opencode "$TMP/oc-del.json"
argv=$(python3 -c 'import json; print(" ".join(json.load(open("'"$TMP/oc-del.json"'"))["argv"]))')
assert_contains "opencode delegate build" "$argv" "--agent build"
assert_contains "opencode delegate auto" "$argv" "--auto"
assert_not_contains "opencode delegate no plan" "$argv" "--agent plan"

# Grok review: sandbox read-only + tool allow/deny
dump_review grok "$TMP/grok-review.json"
argv=$(python3 -c 'import json; print(" ".join(json.load(open("'"$TMP/grok-review.json"'"))["argv"]))')
assert_contains "grok review sandbox read-only" "$argv" "--sandbox read-only"
assert_contains "grok review tools allowlist" "$argv" "--tools"
assert_contains "grok review disallowed tools" "$argv" "--disallowed-tools"
assert_contains "grok review streaming-json" "$argv" "streaming-json"
assert_contains "grok review prompt-file one-shot" "$argv" "--prompt-file"
assert_not_contains "grok review no always-approve" "$argv" "--always-approve"
# --prompt-file is the single-turn-from-file path; do not also require -p/--single
# (those take an inline prompt string and conflict with --prompt-file).

# Grok delegate: always-approve, no sandbox
dump_delegate grok "$TMP/grok-del.json"
argv=$(python3 -c 'import json; print(" ".join(json.load(open("'"$TMP/grok-del.json"'"))["argv"]))')
assert_contains "grok delegate always-approve" "$argv" "--always-approve"
assert_not_contains "grok delegate no sandbox" "$argv" "--sandbox"
assert_contains "grok delegate streaming-json" "$argv" "streaming-json"
assert_contains "grok delegate prompt-file one-shot" "$argv" "--prompt-file"

# Prompts must not be embedded in argv: large tasks are delivered over stdin
# (or a temporary prompt file for Grok), avoiding the OS ARG_MAX ceiling.
echo "=== Unbounded prompt transport ==="
large_prompt="$TMP/large-prompt.txt"
awk 'BEGIN {
  printf "BEGIN_LARGE_PROMPT\n"
  for (i = 0; i < 131072; i++) printf "x"
  printf "\nEND_LARGE_PROMPT\n"
}' > "$large_prompt"
export CONSILIUM_FAKE_ARGV_LOG="$TMP/large-prompt-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
for agent in codex claude-code opencode gemini-cli grok; do
  export CONSILIUM_RUN_DIR="$TMP/run-large-$agent"
  mkdir -p "$CONSILIUM_RUN_DIR"
  "$LIB_DIR/backend_run.sh" --mode review --agent-id "$agent" --raw \
    < "$large_prompt" >/dev/null 2>"$TMP/large-$agent.err"
done
transport_check=$(python3 - "$CONSILIUM_FAKE_ARGV_LOG" <<'PY'
import json
import sys

rows = [json.loads(line) for line in open(sys.argv[1]) if line.strip()]
assert len(rows) == 5, rows
for row in rows:
    argv = "\0".join(row["argv"])
    assert "BEGIN_LARGE_PROMPT" not in argv
    assert "END_LARGE_PROMPT" not in argv
    for forbidden in (
        "--max-turns",
        "--max-budget-usd",
        "--max-tokens",
        "--max-output-tokens",
        "--max-steps",
    ):
        assert forbidden not in row["argv"], (row["bin"], forbidden, row["argv"])
    if row["bin"] == "grok":
        assert "--prompt-file" in row["argv"]
    else:
        data = row.get("stdin", "")
        assert data.startswith("BEGIN_LARGE_PROMPT\n"), row["bin"]
        assert data.endswith("\nEND_LARGE_PROMPT"), row["bin"]
        assert len(data) > 131072, row["bin"]
print("ok")
PY
)
assert_eq "large prompts use stdin or prompt-file, never argv" "$transport_check" "ok"

# Gemini cannot delegate
set +e
"$LIB_DIR/backend_run.sh" --mode delegate --agent-id gemini-cli --raw "x" >/dev/null 2>"$TMP/gem.err"
rc=$?
set -e
assert_eq "gemini delegate rejected" "$rc" "4"
assert_contains "gemini delegate message" "$(cat "$TMP/gem.err")" "review-only"

echo "=== Exact agent selection for delegate ==="
set +e
"$CONSILIUM" delegate "do something" >/dev/null 2>"$TMP/del-no-a.err"
rc=$?
set -e
assert_eq "delegate without -a fails" "$rc" "5"

set +e
"$CONSILIUM" delegate -a 'opencode-*' "x" >/dev/null 2>"$TMP/del-glob.err"
rc=$?
set -e
assert_eq "delegate rejects globs" "$rc" "5"
assert_contains "glob error message" "$(cat "$TMP/del-glob.err")" "exact agent id"

echo "=== Grok streaming-json extraction ==="
export CONSILIUM_FAKE_ARGV_LOG="$TMP/fake-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
export CONSILIUM_RUN_DIR="$TMP/run-grok-ok"
mkdir -p "$CONSILIUM_RUN_DIR"
export CONSILIUM_FAKE_GROK_MODE=ok
out=$(CONSILIUM_SINGLE_AGENT=1 "$LIB_DIR/backend_run.sh" --mode review --agent-id grok --raw "ping" 2>"$TMP/grok.err")
assert_eq "grok extracts final text" "$out" "FAKE_GROK_OK"
assert_file "grok raw artifact" "$CONSILIUM_RUN_DIR/raw/grok.jsonl"
assert_file "grok normalized artifact" "$CONSILIUM_RUN_DIR/normalized/grok.jsonl"
assert_file "grok final artifact" "$CONSILIUM_RUN_DIR/final/grok.txt"
assert_file "grok primary final.txt" "$CONSILIUM_RUN_DIR/final.txt"
assert_contains "progress on stderr" "$(cat "$TMP/grok.err")" "[consilium]"
# stdout must be clean final only
assert_not_contains "stdout has no progress" "$out" "[consilium]"

export CONSILIUM_FAKE_GROK_MODE=error-event
export CONSILIUM_RUN_DIR="$TMP/run-grok-err"
mkdir -p "$CONSILIUM_RUN_DIR"
set +e
"$LIB_DIR/backend_run.sh" --mode review --agent-id grok --raw "ping" >/dev/null 2>"$TMP/grok-err.err"
rc=$?
set -e
assert_eq "grok error event fails" "$rc" "1"

export CONSILIUM_FAKE_GROK_MODE=missing-end
export CONSILIUM_RUN_DIR="$TMP/run-grok-noend"
mkdir -p "$CONSILIUM_RUN_DIR"
set +e
"$LIB_DIR/backend_run.sh" --mode review --agent-id grok --raw "ping" >/dev/null 2>"$TMP/grok-noend.err"
rc=$?
set -e
assert_eq "grok missing end fails" "$rc" "1"

echo "=== Live progress before backend exit (timing/order) ==="
# Fake emits early thought, sleeps, then final. Progress must appear on stderr
# while the backend is still alive — not only after completion.
export CONSILIUM_FAKE_GROK_MODE=slow
export CONSILIUM_FAKE_SLOW_SLEEP=1.0
export CONSILIUM_FAKE_SLOW_MARKER="$TMP/slow-early.marker"
export CONSILIUM_RUN_DIR="$TMP/run-grok-slow"
mkdir -p "$CONSILIUM_RUN_DIR"
rm -f "$CONSILIUM_FAKE_SLOW_MARKER" "$TMP/slow.err" "$TMP/slow.out" "$TMP/slow.live"
: > "$TMP/slow.err"
set +e
"$LIB_DIR/backend_run.sh" --mode review --agent-id grok --raw "ping" \
  >"$TMP/slow.out" 2>"$TMP/slow.err" &
slow_pid=$!
set -e
# Wait until the fake has emitted the early event (still sleeping afterward)
seen_live=0
for _ in $(seq 1 80); do
  if [[ -f "$CONSILIUM_FAKE_SLOW_MARKER" ]]; then
    # Give the pipeline a beat to flush progress, then require progress while alive
    sleep 0.15
    if grep -q 'type=thought' "$TMP/slow.err" 2>/dev/null; then
      if kill -0 "$slow_pid" 2>/dev/null; then
        seen_live=1
        echo 1 > "$TMP/slow.live"
      fi
    fi
    break
  fi
  # Bail early if the process already died without the marker
  if ! kill -0 "$slow_pid" 2>/dev/null; then
    break
  fi
  sleep 0.05
done
set +e
wait "$slow_pid"
slow_rc=$?
set -e
assert_eq "slow grok exit 0" "$slow_rc" "0"
assert_eq "slow grok final text" "$(cat "$TMP/slow.out")" "FAKE_GROK_OK"
assert_eq "progress observed before backend exit" "$seen_live" "1"
assert_contains "slow stderr has thought event" "$(cat "$TMP/slow.err")" "type=thought"
assert_contains "slow stderr has early-progress" "$(cat "$TMP/slow.err")" "early-progress"
assert_not_contains "slow stdout clean" "$(cat "$TMP/slow.out")" "[consilium]"

export CONSILIUM_FAKE_GROK_MODE=ok
unset CONSILIUM_FAKE_SLOW_MARKER CONSILIUM_FAKE_SLOW_SLEEP

echo "=== Review ask with fakes (stdout/stderr split) ==="
export CONSILIUM_RUN_DIR="$TMP/run-ask"
mkdir -p "$CONSILIUM_RUN_DIR"
set +e
out=$("$CONSILIUM" review ask -a codex,grok --raw 2>"$TMP/ask.err" <<'EOF'
What is 2+2?
EOF
)
rc=$?
set -e
# review_ask doesn't have --raw flag; use env
# Re-run properly
export CONSILIUM_RAW_PROMPT=1
export CONSILIUM_RUN_DIR="$TMP/run-ask2"
mkdir -p "$CONSILIUM_RUN_DIR"
set +e
out=$("$CONSILIUM" review ask -a codex,grok "What is 2+2?" 2>"$TMP/ask2.err")
rc=$?
set -e
assert_eq "review ask exit 0" "$rc" "0"
assert_contains "ask has codex answer" "$out" "FAKE_CODEX_OK"
assert_contains "ask has grok answer" "$out" "FAKE_GROK_OK"
assert_contains "ask progress stderr" "$(cat "$TMP/ask2.err")" "[consilium]"
assert_not_contains "ask stdout clean" "$out" "[consilium]"

echo "=== Delegate with fake ==="
export CONSILIUM_RUN_DIR="$TMP/run-del"
mkdir -p "$CONSILIUM_RUN_DIR"
export CONSILIUM_RAW_PROMPT=1
set +e
out=$("$CONSILIUM" delegate -a grok "implement the feature" 2>"$TMP/del.err")
rc=$?
set -e
assert_eq "delegate exit 0" "$rc" "0"
assert_eq "delegate stdout is answer" "$out" "FAKE_GROK_OK"
# Verify YOLO argv was used
assert_contains "delegate fake saw always-approve" "$(cat "$CONSILIUM_FAKE_ARGV_LOG")" "--always-approve"

echo "=== Shell-interpolation warning scope ==="
# Positional with backticks → warn; --prompt-file / stdin with same content → silent.
unset CONSILIUM_SUPPRESS_SHELL_WARN
printf 'Explain `foo` and $(bar).\n' > "$TMP/prompt-with-ticks.txt"
set +e
"$LIB_DIR/backend_run.sh" --mode review --agent-id grok --raw \
  "Explain \`foo\` and \$(bar)." >/dev/null 2>"$TMP/warn-pos.err"
set -e
assert_contains "positional backticks warns" "$(cat "$TMP/warn-pos.err")" "WARNING: prompt contains literal backticks"

set +e
"$LIB_DIR/backend_run.sh" --mode review --agent-id grok --raw \
  --prompt-file "$TMP/prompt-with-ticks.txt" >/dev/null 2>"$TMP/warn-file.err"
set -e
assert_not_contains "prompt-file no shell warn" "$(cat "$TMP/warn-file.err")" "WARNING: prompt contains literal backticks"

set +e
"$LIB_DIR/backend_run.sh" --mode review --agent-id grok --raw \
  >/dev/null 2>"$TMP/warn-stdin.err" < "$TMP/prompt-with-ticks.txt"
set -e
assert_not_contains "stdin no shell warn" "$(cat "$TMP/warn-stdin.err")" "WARNING: prompt contains literal backticks"
export CONSILIUM_SUPPRESS_SHELL_WARN=1

echo "=== normalize_stream.py unit ==="
printf '%s\n' \
  '{"type":"text","data":"A"}' \
  '{"type":"text","data":"B"}' \
  '{"type":"end","stopReason":"EndTurn"}' \
  > "$TMP/stream.jsonl"
python3 "$LIB_DIR/normalize_stream.py" --backend grok-build --agent-id grok \
  --input "$TMP/stream.jsonl" --extract-text --text-out "$TMP/stream.txt" > "$TMP/norm.jsonl"
assert_eq "normalize concat text" "$(cat "$TMP/stream.txt")" "AB"
assert_contains "normalize has end" "$(cat "$TMP/norm.jsonl")" '"type": "end"'

for _ in $(seq 1 30); do
  printf '%s\n' '{"type":"thought","data":"word "}'
done > "$TMP/token-stream.jsonl"
printf '%s\n' '{"type":"end","stopReason":"EndTurn"}' >> "$TMP/token-stream.jsonl"
python3 "$LIB_DIR/normalize_stream.py" --backend grok-build --agent-id grok \
  --input "$TMP/token-stream.jsonl" --progress \
  >"$TMP/token-norm.jsonl" 2>"$TMP/token-progress.err"
progress_lines=$(wc -l < "$TMP/token-progress.err" | tr -d ' ')
assert_le "token deltas coalesce into compact progress" "$progress_lines" "6"

printf '%s\n' '{"type":"error","message":"x"}' > "$TMP/stream-err.jsonl"
set +e
python3 "$LIB_DIR/normalize_stream.py" --backend grok-build --agent-id grok \
  --input "$TMP/stream-err.jsonl" >/dev/null 2>&1
rc=$?
set -e
assert_eq "normalize error fails" "$rc" "1"

echo "=== Review code depth routing (dry structure) ==="
# super dry-run needs full config agents — use real skill config for dry-run only
set +e
out=$(CONSILIUM_CONFIG="$SCRIPTS_DIR/../config.json" \
  "$CONSILIUM" review code --depth super --dry-run "$FIX/sample.py" 2>&1)
rc=$?
set -e
assert_eq "super dry-run exit 0" "$rc" "0"
assert_contains "super dry-run plan" "$out" "DRY RUN"

set +e
out=$(CONSILIUM_CONFIG="$SCRIPTS_DIR/../config.json" \
  "$CONSILIUM" review code --depth ultra --dry-run "$FIX/sample.py" 2>&1)
rc=$?
set -e
assert_eq "ultra dry-run exit 0" "$rc" "0"
assert_contains "ultra dry-run plan" "$out" "DRY RUN"

# basic code review with fakes
export CONSILIUM_CONFIG="$FIX/test-config.json"
export CONSILIUM_RUN_DIR="$TMP/run-code"
mkdir -p "$CONSILIUM_RUN_DIR"
export CONSILIUM_RAW_PROMPT=
# code review will wrap prompts; fakes still return canned text
set +e
out=$("$CONSILIUM" review code --depth basic -a codex,opencode "$FIX/sample.py" 2>"$TMP/code.err")
rc=$?
set -e
# May exit 0 with zero findings after validate, or still 0
assert_eq "code review basic exit 0" "$rc" "0"
assert_contains "code review progress" "$(cat "$TMP/code.err")" "code-review"

echo ""
echo "Results: $PASS passed, $FAIL failed"
rm -rf "$TMP"
if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
exit 0
