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
# Parent shells may carry a leftover FULL_PROMPT; backend_run must not re-export it.
unset FULL_PROMPT 2>/dev/null || true
for agent in codex claude-code opencode gemini-cli grok; do
  export CONSILIUM_RUN_DIR="$TMP/run-large-$agent"
  mkdir -p "$CONSILIUM_RUN_DIR"
  env -u FULL_PROMPT "$LIB_DIR/backend_run.sh" --mode review --agent-id "$agent" --raw \
    < "$large_prompt" >/dev/null 2>"$TMP/large-$agent.err"
done
transport_check=$(python3 - "$CONSILIUM_FAKE_ARGV_LOG" <<'PY'
import json
import sys

rows = [json.loads(line) for line in open(sys.argv[1]) if line.strip()]
# Primary CLI rows only (ignore grok-prompt-meta helpers).
primary = [r for r in rows if r.get("bin") in ("codex", "claude", "opencode", "gemini", "grok")]
assert len(primary) == 5, primary
for row in primary:
    argv = "\0".join(row["argv"])
    assert "BEGIN_LARGE_PROMPT" not in argv
    assert "END_LARGE_PROMPT" not in argv
    assert row.get("has_FULL_PROMPT") is False, row["bin"]
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
# Grok body arrives via --prompt-file (meta row)
meta = [r for r in rows if r.get("bin") == "grok-prompt-meta"]
assert meta and meta[-1]["prompt_len"] > 131072, meta
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

echo "=== Claude stream-json: authoritative result wins over distinct delta ==="
# Delta and result strings differ — final answer must be result, never delta/concat.
export CONSILIUM_FAKE_CLAUDE_MODE=ok
export CONSILIUM_RUN_DIR="$TMP/run-claude-dup"
mkdir -p "$CONSILIUM_RUN_DIR"
export CONSILIUM_FAKE_ARGV_LOG="$TMP/claude-dup-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
out=$(CONSILIUM_SINGLE_AGENT=1 "$LIB_DIR/backend_run.sh" \
  --mode review --agent-id claude-code --raw "ping" 2>"$TMP/claude-dup.err")
assert_eq "claude backend_run prefers result over delta" "$out" "FAKE_CLAUDE_RESULT"
assert_not_contains "claude backend_run has no delta text" "$out" "FAKE_CLAUDE_DELTA"
# Count occurrences in final artifact
claude_final="$CONSILIUM_RUN_DIR/final/claude-code.txt"
if [[ -f "$claude_final" ]]; then
  count=$(grep -o 'FAKE_CLAUDE_RESULT' "$claude_final" | wc -l | tr -d ' ')
  delta_count=$(grep -c 'FAKE_CLAUDE_DELTA' "$claude_final" 2>/dev/null || true)
else
  count=$(grep -o 'FAKE_CLAUDE_RESULT' <<<"$out" | wc -l | tr -d ' ')
  delta_count=0
fi
delta_count="${delta_count:-0}"
assert_eq "claude final artifact result once" "$count" "1"
assert_eq "claude final artifact no delta" "$delta_count" "0"
# Normalized stream still has both text delta and result events
assert_file "claude raw artifact" "$CONSILIUM_RUN_DIR/raw/claude-code.jsonl"
assert_contains "claude raw has delta" "$(cat "$CONSILIUM_RUN_DIR/raw/claude-code.jsonl")" "content_block_delta"
assert_contains "claude raw has result" "$(cat "$CONSILIUM_RUN_DIR/raw/claude-code.jsonl")" '"type":"result"'
assert_file "claude normalized artifact" "$CONSILIUM_RUN_DIR/normalized/claude-code.jsonl"
assert_contains "claude norm has text event" "$(cat "$CONSILIUM_RUN_DIR/normalized/claude-code.jsonl")" '"type": "text"'
assert_contains "claude norm has result event" "$(cat "$CONSILIUM_RUN_DIR/normalized/claude-code.jsonl")" '"type": "result"'
assert_contains "claude progress on stderr" "$(cat "$TMP/claude-dup.err")" "[consilium]"

# result-only stream (no deltas)
export CONSILIUM_FAKE_CLAUDE_MODE=result-only
export CONSILIUM_RUN_DIR="$TMP/run-claude-result-only"
mkdir -p "$CONSILIUM_RUN_DIR"
out=$(CONSILIUM_SINGLE_AGENT=1 "$LIB_DIR/backend_run.sh" \
  --mode review --agent-id claude-code --raw "ping" 2>"$TMP/claude-ro.err")
assert_eq "claude result-only answer once" "$out" "FAKE_CLAUDE_RESULT"
count=$(grep -o 'FAKE_CLAUDE_RESULT' <<<"$out" | wc -l | tr -d ' ')
assert_eq "claude result-only count" "$count" "1"
export CONSILIUM_FAKE_CLAUDE_MODE=ok

# Unit-level: normalize_stream extract-text with *distinct* delta+result
printf '%s\n' \
  '{"type":"content_block_delta","delta":{"type":"text_delta","text":"DELTA_ONLY"}}' \
  '{"type":"result","result":"RESULT_WINS"}' \
  > "$TMP/claude-stream.jsonl"
python3 "$LIB_DIR/normalize_stream.py" --backend claude-code --agent-id claude \
  --input "$TMP/claude-stream.jsonl" --extract-text --text-out "$TMP/claude-extract.txt" \
  --no-validate --progress >"$TMP/claude-norm.jsonl" 2>"$TMP/claude-norm.err"
assert_eq "normalize claude result wins over delta" "$(cat "$TMP/claude-extract.txt")" "RESULT_WINS"
assert_not_contains "normalize extract has no delta" "$(cat "$TMP/claude-extract.txt")" "DELTA_ONLY"
assert_contains "normalize keeps result event" "$(cat "$TMP/claude-norm.jsonl")" '"type": "result"'
assert_contains "normalize keeps text event" "$(cat "$TMP/claude-norm.jsonl")" '"type": "text"'

printf '%s\n' \
  '{"type":"result","result":"ONLY"}' \
  > "$TMP/claude-stream-ro.jsonl"
python3 "$LIB_DIR/normalize_stream.py" --backend claude-code --agent-id claude \
  --input "$TMP/claude-stream-ro.jsonl" --extract-text --text-out "$TMP/claude-extract-ro.txt" \
  --no-validate >/dev/null
assert_eq "normalize claude result-only once" "$(cat "$TMP/claude-extract-ro.txt")" "ONLY"

echo "=== Prompt > ARG_MAX; inherited FULL_PROMPT must not reach child ==="
ARG_MAX_BYTES="$(getconf ARG_MAX 2>/dev/null || echo 262144)"
# Slightly larger than ARG_MAX so an env export of the body would E2BIG.
OVER_SIZE=$((ARG_MAX_BYTES + 4096))
huge_prompt="$TMP/huge-prompt.txt"
python3 -c '
import sys
n = int(sys.argv[1])
sys.stdout.write("BEGIN_HUGE_PROMPT\n")
sys.stdout.write("H" * n)
sys.stdout.write("\nEND_HUGE_PROMPT\n")
' "$OVER_SIZE" > "$huge_prompt"
export CONSILIUM_FAKE_ARGV_LOG="$TMP/huge-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
export CONSILIUM_RUN_DIR="$TMP/run-huge"
mkdir -p "$CONSILIUM_RUN_DIR"
# Start with an *inherited exported* FULL_PROMPT (do not env -u). backend_run
# must unset it so the child does not see it, while still delivering >ARG_MAX body.
export FULL_PROMPT="LEAKED_INHERITED_FULL_PROMPT_MUST_NOT_REACH_CHILD"
set +e
"$LIB_DIR/backend_run.sh" --mode review --agent-id codex --raw \
  < "$huge_prompt" >"$TMP/huge.out" 2>"$TMP/huge.err"
huge_rc=$?
set -e
assert_eq "huge prompt backend exit 0" "$huge_rc" "0"
assert_eq "huge prompt final answer" "$(cat "$TMP/huge.out")" "FAKE_CODEX_OK"
huge_check=$(python3 - "$CONSILIUM_FAKE_ARGV_LOG" "$OVER_SIZE" <<'PY'
import json, sys
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
assert rows, "no fake log rows"
codex = [r for r in rows if r.get("bin") == "codex"]
assert codex, rows
row = codex[-1]
assert row.get("has_FULL_PROMPT") is False, row
stdin = row.get("stdin") or ""
assert "LEAKED_INHERITED_FULL_PROMPT" not in stdin, stdin[:120]
assert stdin.startswith("BEGIN_HUGE_PROMPT\n"), stdin[:80]
assert stdin.rstrip().endswith("END_HUGE_PROMPT"), stdin[-80:]
assert len(stdin) > int(sys.argv[2]), len(stdin)
print("ok")
PY
)
assert_eq "huge prompt reaches fake; FULL_PROMPT not in env" "$huge_check" "ok"

# Grok path (prompt-file) also must not re-export inherited FULL_PROMPT
: > "$CONSILIUM_FAKE_ARGV_LOG"
export CONSILIUM_RUN_DIR="$TMP/run-huge-grok"
mkdir -p "$CONSILIUM_RUN_DIR"
export FULL_PROMPT="LEAKED_INHERITED_FULL_PROMPT_MUST_NOT_REACH_CHILD"
set +e
"$LIB_DIR/backend_run.sh" --mode review --agent-id grok --raw \
  < "$huge_prompt" >"$TMP/huge-grok.out" 2>"$TMP/huge-grok.err"
huge_grok_rc=$?
set -e
assert_eq "huge grok exit 0" "$huge_grok_rc" "0"
huge_grok_check=$(python3 - "$CONSILIUM_FAKE_ARGV_LOG" "$OVER_SIZE" <<'PY'
import json, sys
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
meta = [r for r in rows if r.get("bin") == "grok-prompt-meta"]
base = [r for r in rows if r.get("bin") == "grok"]
assert base and meta, rows
assert all(r.get("has_FULL_PROMPT") is False for r in base + meta), (base, meta)
m = meta[-1]
assert m["prompt_len"] > int(sys.argv[2]), m
assert m["prompt_startswith"].startswith("BEGIN_HUGE_PROMPT")
assert m["prompt_endswith"].endswith("END_HUGE_PROMPT")
print("ok")
PY
)
assert_eq "huge grok prompt-file; FULL_PROMPT absent" "$huge_grok_check" "ok"
unset FULL_PROMPT 2>/dev/null || true

echo "=== Delegate positional normalized off argv ==="
export CONSILIUM_FAKE_ARGV_LOG="$TMP/del-pos-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
export CONSILIUM_RUN_DIR="$TMP/run-del-pos"
mkdir -p "$CONSILIUM_RUN_DIR"
set +e
out=$("$CONSILIUM" delegate -a grok "implement positional task XYZ" 2>"$TMP/del-pos.err")
rc=$?
set -e
assert_eq "delegate positional exit 0" "$rc" "0"
assert_eq "delegate positional stdout" "$out" "FAKE_GROK_OK"
del_pos_check=$(python3 - "$CONSILIUM_FAKE_ARGV_LOG" <<'PY'
import json, sys
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip() and '"bin": "grok"' in l or '"bin":"grok"' in l.replace(" ","")]
# parse properly
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
grok = [r for r in rows if r.get("bin") == "grok"]
assert grok, rows
argv = grok[-1]["argv"]
joined = "\0".join(argv)
assert "implement positional task XYZ" not in joined, argv
assert "--prompt-file" in argv
print("ok")
PY
)
assert_eq "delegate positional not in backend argv" "$del_pos_check" "ok"
# --prompt-file path still works
printf 'from file task\n' > "$TMP/del-file-prompt.txt"
: > "$CONSILIUM_FAKE_ARGV_LOG"
export CONSILIUM_RUN_DIR="$TMP/run-del-file"
mkdir -p "$CONSILIUM_RUN_DIR"
set +e
out=$("$CONSILIUM" delegate -a grok --prompt-file "$TMP/del-file-prompt.txt" 2>"$TMP/del-file.err")
rc=$?
set -e
assert_eq "delegate --prompt-file exit 0" "$rc" "0"
assert_eq "delegate --prompt-file stdout" "$out" "FAKE_GROK_OK"

echo "=== Discovery/judge backends run from caller CWD ==="
# discovery-pass must not cd into empty temp; fake records cwd.
export CONSILIUM_FAKE_ARGV_LOG="$TMP/cwd-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
CALLER_CWD="$TMP/project-cwd"
mkdir -p "$CALLER_CWD"
printf 'def x():\n    return 1\n' > "$CALLER_CWD/app.py"
body_file="$TMP/cwd-body.txt"
awk '{printf "%4d  %s\n", NR, $0}' "$CALLER_CWD/app.py" > "$body_file"
# Minimal prompt template with placeholders
printf 'ROLE={{ROLE}}\nBODY:\n{{INPUT_BODY}}\n{{CAP_DIRECTIVE}}\n' > "$TMP/cwd-prompt.txt"
export CONSILIUM_RUN_DIR="$TMP/run-cwd"
mkdir -p "$CONSILIUM_RUN_DIR"
set +e
(
  cd "$CALLER_CWD"
  "$LIB_DIR/discovery-pass.sh" \
    --agent grok --role analyst --cap uncapped \
    --prompt "$TMP/cwd-prompt.txt" \
    --input-kind file --input-label app.py \
    --input-body-file "$body_file" \
    --out "$TMP/cwd-out.xml"
) >"$TMP/cwd-pass.out" 2>"$TMP/cwd-pass.err"
cwd_rc=$?
set -e
assert_eq "discovery-pass exit 0" "$cwd_rc" "0"
cwd_check=$(python3 - "$CONSILIUM_FAKE_ARGV_LOG" "$CALLER_CWD" <<'PY'
import json, os, sys
want = os.path.realpath(sys.argv[2])
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
got = [os.path.realpath(r["cwd"]) for r in rows if "cwd" in r]
assert got, rows
assert all(c == want for c in got), (got, want)
print("ok")
PY
)
assert_eq "discovery backend cwd is caller project" "$cwd_check" "ok"

echo "=== Artifact keys disambiguate agent role reuse ==="
export CONSILIUM_FAKE_ARGV_LOG="$TMP/art-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
export CONSILIUM_RUN_DIR="$TMP/run-art-reuse"
mkdir -p "$CONSILIUM_RUN_DIR"
# One agent, two roles in parallel (basic mode with single agent)
set +e
out=$("$CONSILIUM" review code --depth basic -a codex "$FIX/sample.py" 2>"$TMP/art.err")
rc=$?
set -e
assert_eq "artifact reuse review exit 0" "$rc" "0"
# Expect codex.security and codex.correctness artifacts (not a single codex.txt overwrite)
assert_file "artifact codex.security final" "$CONSILIUM_RUN_DIR/final/codex.security.txt"
assert_file "artifact codex.correctness final" "$CONSILIUM_RUN_DIR/final/codex.correctness.txt"
assert_file "artifact codex.security raw" "$CONSILIUM_RUN_DIR/raw/codex.security.jsonl"
assert_file "artifact codex.correctness raw" "$CONSILIUM_RUN_DIR/raw/codex.correctness.jsonl"
# Ordinary single-agent ask still uses plain agent id
export CONSILIUM_RUN_DIR="$TMP/run-art-ask"
mkdir -p "$CONSILIUM_RUN_DIR"
export CONSILIUM_RAW_PROMPT=1
set +e
"$CONSILIUM" review ask -a grok "plain ask" >/dev/null 2>"$TMP/art-ask.err"
set -e
assert_file "ask artifact plain agent id" "$CONSILIUM_RUN_DIR/final/grok.txt"

echo "=== review code exit codes: partial / all-fail / all-ok ==="
# all-ok already covered above (exit 0). Partial: one agent fails mid-pass.
# Force grok fail mode while codex succeeds — assign both via two agents.
export CONSILIUM_FAKE_GROK_MODE=fail
export CONSILIUM_RUN_DIR="$TMP/run-code-partial"
mkdir -p "$CONSILIUM_RUN_DIR"
export CONSILIUM_RAW_PROMPT=
set +e
out=$("$CONSILIUM" review code --depth basic -a codex,grok "$FIX/sample.py" 2>"$TMP/code-partial.err")
partial_rc=$?
set -e
# With 2 agents and 2 roles: codex→security, grok→correctness. grok fails → partial.
assert_eq "code review partial exit 2" "$partial_rc" "2"
# Report still emitted from successful specialist(s) on stdout and/or final.txt
partial_has_output=0
[[ -n "$out" ]] && partial_has_output=1
[[ -s "${CONSILIUM_RUN_DIR}/final.txt" ]] && partial_has_output=1
assert_eq "partial emits report from successes" "$partial_has_output" "1"

# all fail
export CONSILIUM_FAKE_GROK_MODE=fail
# Make codex fail too via a wrapper — use only grok for both roles
export CONSILIUM_RUN_DIR="$TMP/run-code-allfail"
mkdir -p "$CONSILIUM_RUN_DIR"
set +e
out=$("$CONSILIUM" review code --depth basic -a grok "$FIX/sample.py" 2>"$TMP/code-allfail.err")
allfail_rc=$?
set -e
assert_eq "code review all-fail exit 3" "$allfail_rc" "3"
export CONSILIUM_FAKE_GROK_MODE=ok

echo "=== Failure stderr not duplicated ==="
# Use missing-end so a known normalize diagnostic is always present once.
export CONSILIUM_FAKE_GROK_MODE=missing-end
export CONSILIUM_RUN_DIR="$TMP/run-stderr-dup"
mkdir -p "$CONSILIUM_RUN_DIR"
export CONSILIUM_RAW_PROMPT=1
set +e
"$CONSILIUM" review ask -a grok "fail please" >"$TMP/stderr-dup.out" 2>"$TMP/stderr-dup.err"
set -e
export CONSILIUM_FAKE_GROK_MODE=ok
# progress_agent_done failed line should appear once (live via tee, not re-catted)
fail_lines=$(grep -c 'status=failed' "$TMP/stderr-dup.err" 2>/dev/null || true)
fail_lines="${fail_lines:-0}"
assert_eq "failed status once on stderr" "$fail_lines" "1"
# Known diagnostic must appear exactly once (not <=1 — zero would be a false green).
norm_err_count=$(grep -c 'grok stream missing end event' "$TMP/stderr-dup.err" 2>/dev/null || true)
norm_err_count="${norm_err_count:-0}"
assert_eq "normalize error exactly once on stderr" "$norm_err_count" "1"
# backend stderr banner from backend_run should not be doubled
banner_count=$(grep -c 'backend stderr:' "$TMP/stderr-dup.err" 2>/dev/null || true)
banner_count="${banner_count:-0}"
assert_le "backend stderr banner not duplicated" "$banner_count" "1"

echo "=== No-FIFO redirect-failure path terminates promptly ==="
# Old named-FIFO design could hang forever if the writer never opened.
# Force a failed stdout redirect (OUT is a directory) and supervise externally
# (harness timeout only — no internal AGENT_TIMEOUT required).
mkdir -p "$TMP/bad-out-as-dir"
printf 'BODY={{INPUT_BODY}}\n' > "$TMP/redir-prompt.txt"
printf '1  code\n' > "$TMP/redir-body.txt"
export CONSILIUM_RUN_DIR="$TMP/run-redir-fail"
mkdir -p "$CONSILIUM_RUN_DIR"
redir_out=$(python3 - "$LIB_DIR/discovery-pass.sh" "$TMP" <<'PY'
import subprocess, sys, os
script, tmp = sys.argv[1], sys.argv[2]
cmd = [
    script,
    "--agent", "grok", "--role", "analyst", "--cap", "uncapped",
    "--prompt", os.path.join(tmp, "redir-prompt.txt"),
    "--input-kind", "file", "--input-label", "x",
    "--input-body-file", os.path.join(tmp, "redir-body.txt"),
    "--out", os.path.join(tmp, "bad-out-as-dir"),  # directory → redirect fails
]
try:
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=8,
                       env=os.environ.copy())
    print(f"DONE:{p.returncode}")
except subprocess.TimeoutExpired:
    print("HUNG")
PY
)
assert_not_contains "redirect-failure did not hang" "$redir_out" "HUNG"
assert_contains "redirect-failure terminated" "$redir_out" "DONE:"
# Non-zero exit expected (failed invocation)
redir_rc="${redir_out#DONE:}"
if [[ "$redir_rc" != "0" && "$redir_rc" != "HUNG" && -n "$redir_rc" ]]; then
  echo "  PASS  redirect-failure non-zero exit ($redir_rc)"
  PASS=$((PASS+1))
else
  echo "  FAIL  redirect-failure non-zero exit (got $redir_rc)"
  FAIL=$((FAIL+1))
fi

echo "=== discovery-pass grep -c zero findings (no double-zero) ==="
# Empty findings output still reports "0 finding(s)" not "0\n0"
export CONSILIUM_FAKE_ARGV_LOG="$TMP/grep0-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
export CONSILIUM_RUN_DIR="$TMP/run-grep0"
mkdir -p "$CONSILIUM_RUN_DIR"
# Use a fake that returns non-finding text (FAKE_GROK_OK has no <finding>)
printf 'BODY={{INPUT_BODY}}\n' > "$TMP/grep0-prompt.txt"
printf '1  code\n' > "$TMP/grep0-body.txt"
set +e
"$LIB_DIR/discovery-pass.sh" \
  --agent grok --role analyst --cap uncapped \
  --prompt "$TMP/grep0-prompt.txt" \
  --input-kind file --input-label x \
  --input-body-file "$TMP/grep0-body.txt" \
  --out "$TMP/grep0-out.xml" \
  >"$TMP/grep0.out" 2>"$TMP/grep0.err"
grep0_rc=$?
set -e
assert_eq "discovery zero-findings exit 0" "$grep0_rc" "0"
# Must be exactly "0 finding(s)" once — not "0\n0 finding(s)"
assert_contains "zero findings message" "$(cat "$TMP/grep0.err")" "0 finding(s)"
# Reject the double-zero bug: "0\n0 finding" or "00 finding"
assert_not_contains "no double-zero bug" "$(cat "$TMP/grep0.err" | tr '\n' ' ')" "0 0 finding"

echo "=== Explicit distinct artifact keys for multi-pass discovery + judge ==="
export CONSILIUM_FAKE_ARGV_LOG="$TMP/artkey-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
export CONSILIUM_RUN_DIR="$TMP/run-artkeys"
mkdir -p "$CONSILIUM_RUN_DIR"
# Poison ambient key — fan-out must not use it for both passes.
export CONSILIUM_ARTIFACT_KEY="ambient.poison.key"
printf 'BODY={{INPUT_BODY}}\n' > "$TMP/artkey-prompt.txt"
printf '1  code\n' > "$TMP/artkey-body.txt"
set +e
"$LIB_DIR/discovery-pass.sh" \
  --agent grok --role analyst --cap uncapped \
  --prompt "$TMP/artkey-prompt.txt" \
  --input-kind file --input-label x \
  --input-body-file "$TMP/artkey-body.txt" \
  --out "$TMP/artkey-a.xml" \
  --artifact-key "discovery-small.0.grok.analyst" \
  >"$TMP/artkey-a.out" 2>"$TMP/artkey-a.err"
"$LIB_DIR/discovery-pass.sh" \
  --agent grok --role lateral --cap uncapped \
  --prompt "$TMP/artkey-prompt.txt" \
  --input-kind file --input-label x \
  --input-body-file "$TMP/artkey-body.txt" \
  --out "$TMP/artkey-b.xml" \
  --artifact-key "discovery-small.1.grok.lateral" \
  >"$TMP/artkey-b.out" 2>"$TMP/artkey-b.err"
set -e
assert_file "discovery key 0 final" "$CONSILIUM_RUN_DIR/final/discovery-small.0.grok.analyst.txt"
assert_file "discovery key 1 final" "$CONSILIUM_RUN_DIR/final/discovery-small.1.grok.lateral.txt"
assert_file "discovery key 0 raw" "$CONSILIUM_RUN_DIR/raw/discovery-small.0.grok.analyst.jsonl"
assert_file "discovery key 1 raw" "$CONSILIUM_RUN_DIR/raw/discovery-small.1.grok.lateral.jsonl"
# Ambient poison must not be the only artifact written
if [[ -f "$CONSILIUM_RUN_DIR/final/ambient.poison.key.txt" ]]; then
  echo "  FAIL  ambient artifact key was used"
  FAIL=$((FAIL+1))
else
  echo "  PASS  ambient artifact key not used for discovery"
  PASS=$((PASS+1))
fi

# Judge primary vs fallback distinct keys; inherited legacy body must not reach child.
printf '<findings/>\n' > "$TMP/judge-findings.xml"
printf 'line one\n' > "$TMP/judge-source.py"
# Minimal judge prompt that still renders placeholders
printf 'KIND={{INPUT_KIND}}\nLABEL={{INPUT_LABEL}}\nBODY={{INPUT_BODY}}\nFINDINGS={{FINDINGS_BODY}}\n{"verdicts":[]}\n' \
  > "$TMP/judge-prompt.txt"
export JUDGE_INPUT_BODY="LEGACY_MARKER_MUST_NOT_REACH_BACKEND_CHILD"
export CONSILIUM_FAKE_ARGV_LOG="$TMP/judge-argv.jsonl"
: > "$CONSILIUM_FAKE_ARGV_LOG"
set +e
"$LIB_DIR/judge-runner.sh" \
  --agent grok \
  --findings "$TMP/judge-findings.xml" \
  --source "$TMP/judge-source.py" \
  --input-kind file \
  --out "$TMP/verdicts-primary.json" \
  --prompt "$TMP/judge-prompt.txt" \
  --artifact-key "judge.primary.grok" \
  >"$TMP/judge-p.out" 2>"$TMP/judge-p.err"
j1=$?
"$LIB_DIR/judge-runner.sh" \
  --agent codex \
  --findings "$TMP/judge-findings.xml" \
  --source "$TMP/judge-source.py" \
  --input-kind file \
  --out "$TMP/verdicts-fallback.json" \
  --prompt "$TMP/judge-prompt.txt" \
  --artifact-key "judge.fallback.codex" \
  >"$TMP/judge-f.out" 2>"$TMP/judge-f.err"
j2=$?
set -e
# Fake backends emit non-JSON answers → stable schema-failure exit 2; artifacts still written.
assert_eq "judge primary schema-failure exit" "$j1" "2"
assert_eq "judge fallback schema-failure exit" "$j2" "2"
assert_file "judge primary artifact" "$CONSILIUM_RUN_DIR/final/judge.primary.grok.txt"
assert_file "judge fallback artifact" "$CONSILIUM_RUN_DIR/final/judge.fallback.codex.txt"
judge_env_check=$(python3 - "$CONSILIUM_FAKE_ARGV_LOG" <<'PY'
import json, sys
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
assert rows, "no fake log"
# Every backend child must not see legacy body env markers.
for r in rows:
    assert r.get("has_JUDGE_INPUT_BODY") is not True, r
    assert r.get("has_JR_INPUT_BODY") is not True, r
    assert r.get("has_JR_FINDINGS_BODY") is not True, r
print("ok")
PY
)
assert_eq "judge legacy body env absent in backend" "$judge_env_check" "ok"
unset JUDGE_INPUT_BODY CONSILIUM_ARTIFACT_KEY 2>/dev/null || true

# Direct call without --artifact-key gets an invocation-unique default (not ambient).
export CONSILIUM_ARTIFACT_KEY="ambient.poison.key"
export CONSILIUM_RUN_DIR="$TMP/run-artkey-default"
mkdir -p "$CONSILIUM_RUN_DIR"
: > "$CONSILIUM_FAKE_ARGV_LOG"
set +e
"$LIB_DIR/discovery-pass.sh" \
  --agent grok --role analyst --cap uncapped \
  --prompt "$TMP/artkey-prompt.txt" \
  --input-kind file --input-label x \
  --input-body-file "$TMP/artkey-body.txt" \
  --out "$TMP/artkey-default.xml" \
  >"$TMP/artkey-def.out" 2>"$TMP/artkey-def.err"
set -e
# Must not write under ambient.poison.key
if [[ -f "$CONSILIUM_RUN_DIR/final/ambient.poison.key.txt" ]]; then
  echo "  FAIL  default key ignored ambient (wrote ambient key)"
  FAIL=$((FAIL+1))
else
  echo "  PASS  default discovery key ignores ambient"
  PASS=$((PASS+1))
fi
# Some discovery.*.txt should exist
default_arts=$(find "$CONSILIUM_RUN_DIR/final" -name 'discovery.*.txt' 2>/dev/null | wc -l | tr -d ' ')
if [[ "${default_arts:-0}" -ge 1 ]]; then
  echo "  PASS  default discovery wrote invocation-unique artifact"
  PASS=$((PASS+1))
else
  echo "  FAIL  default discovery wrote invocation-unique artifact (found $default_arts)"
  FAIL=$((FAIL+1))
fi
unset CONSILIUM_ARTIFACT_KEY 2>/dev/null || true

echo "=== Bash 3.2 required-arg validation (exit 5) ==="
# Invoke under /bin/bash so Apple Bash 3.2 paths are exercised (no ${var,,}).
set +e
/bin/bash "$LIB_DIR/discovery-pass.sh" --role analyst \
  >"$TMP/disc-miss.out" 2>"$TMP/disc-miss.err"
dmiss_rc=$?
/bin/bash "$LIB_DIR/judge-runner.sh" --agent grok \
  >"$TMP/judge-miss.out" 2>"$TMP/judge-miss.err"
jmiss_rc=$?
set -e
assert_eq "discovery-pass missing required exit 5" "$dmiss_rc" "5"
assert_contains "discovery-pass missing required diagnostics" \
  "$(cat "$TMP/disc-miss.err")" "required"
assert_contains "discovery-pass missing required names flag" \
  "$(cat "$TMP/disc-miss.err")" "--agent"
assert_eq "judge-runner missing required exit 5" "$jmiss_rc" "5"
assert_contains "judge-runner missing required diagnostics" \
  "$(cat "$TMP/judge-miss.err")" "required"
# First missing among AGENT FINDINGS SOURCE OUT is --findings when only --agent set
assert_contains "judge-runner missing required names flag" \
  "$(cat "$TMP/judge-miss.err")" "--findings"

echo "=== Steerable delegate (deterministic fakes) ==="
# Subprocess suite with its own counters; fold into PASS/FAIL.
chmod +x "$FAKES"/steer/* 2>/dev/null || true
set +e
STEER_OUT=$(PYTHONPATH="$LIB_DIR${PYTHONPATH:+:$PYTHONPATH}" python3 "$TESTS_DIR/steer/test_steer_e2e.py" 2>&1)
STEER_RC=$?
set -e
printf '%s\n' "$STEER_OUT"
# Parse "steer tests: N passed, M failed"
steer_pass=$(printf '%s\n' "$STEER_OUT" | sed -n 's/.*steer tests: \([0-9]*\) passed.*/\1/p' | tail -1)
steer_fail=$(printf '%s\n' "$STEER_OUT" | sed -n 's/.*steer tests: [0-9]* passed, \([0-9]*\) failed.*/\1/p' | tail -1)
steer_pass=${steer_pass:-0}
steer_fail=${steer_fail:-1}
PASS=$((PASS + steer_pass))
FAIL=$((FAIL + steer_fail))
if [[ $STEER_RC -ne 0 && $steer_fail -eq 0 ]]; then
  echo "  FAIL  steerable suite non-zero exit without fail count"
  FAIL=$((FAIL + 1))
fi

# CLI surface for steerable modes
help_out=$("$CONSILIUM" delegate -h 2>&1) || true
assert_contains "delegate help mentions steerable" "$help_out" "steerable"
assert_contains "delegate help mentions steer" "$help_out" "steer"
assert_contains "delegate help mentions status" "$help_out" "status"
assert_contains "delegate help mentions cancel" "$help_out" "cancel"

echo ""
echo "Results: $PASS passed, $FAIL failed"
rm -rf "$TMP"
if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
exit 0
