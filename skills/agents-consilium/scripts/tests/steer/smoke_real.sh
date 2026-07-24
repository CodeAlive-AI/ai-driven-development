#!/bin/bash
# Opt-in real-backend smoke for steerable delegate.
# Default test suite does NOT run this (no network / model spend).
#
# Usage:
#   CONSILIUM_STEER_SMOKE=1 bash scripts/tests/steer/smoke_real.sh -a grok "say hi then wait"
#   CONSILIUM_STEER_SMOKE=1 bash scripts/tests/steer/smoke_real.sh -a claude-code "list files"
#
# Requires real binaries on PATH and valid auth for the chosen agent.
set -euo pipefail

if [[ "${CONSILIUM_STEER_SMOKE:-}" != "1" ]]; then
  echo "Refusing to run real smoke without CONSILIUM_STEER_SMOKE=1" >&2
  echo "This spends model tokens and needs network." >&2
  exit 5
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONSILIUM="$(cd "$SCRIPT_DIR/../.." && pwd)/consilium"

AGENT=""
# Default task exercises concurrent queue: sleep keeps first prompt in-flight
# long enough for a steer to land as queued, then apply after wake.
TASK="Use the shell tool to run sleep 5 before answering. Then reply with exactly the word INITIAL (nothing else) and stop."
STEER_TEXT="Also mention STEERED in your final reply. The complete final reply must contain both INITIAL and STEERED."
STRICT_GROK_CHECKS=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    -a|--agent) AGENT="${2:-}"; shift 2 ;;
    --strict-grok) STRICT_GROK_CHECKS=1; shift ;;
    --steer-text) STEER_TEXT="${2:-}"; shift 2 ;;
    *) TASK="$1"; shift ;;
  esac
done

if [[ -z "$AGENT" ]]; then
  echo "Usage: CONSILIUM_STEER_SMOKE=1 $0 -a <agent-id> [task]" >&2
  exit 5
fi

# Auto-strict for grok (the backend with known late-ack + thought bugs).
if [[ "$AGENT" == "grok" || "$AGENT" == "grok-build" ]]; then
  STRICT_GROK_CHECKS=1
fi

export CONSILIUM_STEER_DIR="${CONSILIUM_STEER_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/consilium-steer-smoke.XXXXXX")}"
echo "CONSILIUM_STEER_DIR=$CONSILIUM_STEER_DIR" >&2
echo "task=$TASK" >&2

# Run steerable in background; capture run_id from stderr
set +e
"$CONSILIUM" delegate -a "$AGENT" --steerable "$TASK" >"$CONSILIUM_STEER_DIR/stdout.txt" 2>"$CONSILIUM_STEER_DIR/stderr.txt" &
PID=$!
set -e

RUN_ID=""
for _ in $(seq 1 100); do
  if [[ -f "$CONSILIUM_STEER_DIR/stderr.txt" ]]; then
    RUN_ID=$(sed -n 's/^run_id=//p' "$CONSILIUM_STEER_DIR/stderr.txt" | head -1)
    [[ -n "$RUN_ID" ]] && break
    RUN_ID=$(grep -o 'run_id=run_[a-f0-9]*' "$CONSILIUM_STEER_DIR/stderr.txt" | head -1 | cut -d= -f2 || true)
    [[ -n "$RUN_ID" ]] && break
  fi
  sleep 0.1
done

if [[ -z "$RUN_ID" ]]; then
  echo "Failed to obtain run_id" >&2
  cat "$CONSILIUM_STEER_DIR/stderr.txt" >&2 || true
  kill "$PID" 2>/dev/null || true
  exit 1
fi
echo "run_id=$RUN_ID" >&2

# Steer while first prompt is still in-flight (sleep 5 window).
sleep 1
echo "steer_text=$STEER_TEXT" >&2
"$CONSILIUM" delegate steer "$RUN_ID" --mode auto "$STEER_TEXT" || true
"$CONSILIUM" delegate status "$RUN_ID" --json | head -c 2000 || true
echo >&2

set +e
wait "$PID"
WAIT_RC=$?
set -e
echo "supervisor_exit=$WAIT_RC" >&2

echo "--- stdout ---"
cat "$CONSILIUM_STEER_DIR/stdout.txt"
echo "--- status ---"
STATUS_JSON=$("$CONSILIUM" delegate status "$RUN_ID" --json || true)
echo "$STATUS_JSON"

RUN_DIR="$CONSILIUM_STEER_DIR/runs/$RUN_ID"
FINAL_FILE=""
if [[ -f "$RUN_DIR/final.txt" ]]; then
  FINAL_FILE="$RUN_DIR/final.txt"
elif [[ -f "$CONSILIUM_STEER_DIR/stdout.txt" ]]; then
  FINAL_FILE="$CONSILIUM_STEER_DIR/stdout.txt"
fi

if [[ "$STRICT_GROK_CHECKS" -eq 1 ]]; then
  echo "--- strict grok checks ---" >&2
  FAIL=0
  BODY=""
  if [[ -n "$FINAL_FILE" && -f "$FINAL_FILE" ]]; then
    BODY=$(cat "$FINAL_FILE")
  else
    BODY=$(cat "$CONSILIUM_STEER_DIR/stdout.txt")
  fi

  # Must contain steered final answer markers
  if ! grep -q 'INITIAL' <<<"$BODY"; then
    echo "FAIL: final/stdout missing INITIAL" >&2
    FAIL=1
  else
    echo "PASS: contains INITIAL" >&2
  fi
  if ! grep -q 'STEERED' <<<"$BODY"; then
    echo "FAIL: final/stdout missing STEERED" >&2
    FAIL=1
  else
    echo "PASS: contains STEERED" >&2
  fi
  # Chain-of-thought must not leak into final (real bug: agent_thought_chunk)
  if grep -q 'The user wants' <<<"$BODY"; then
    echo "FAIL: final/stdout contains thought leak 'The user wants'" >&2
    FAIL=1
  else
    echo "PASS: no thought leak 'The user wants'" >&2
  fi

  # Terminal steer status must be applied with matching evidence
  # Write status to a file so heredoc can own stdin for the checker script.
  STATUS_FILE="$CONSILIUM_STEER_DIR/status-final.json"
  printf '%s\n' "$STATUS_JSON" >"$STATUS_FILE"
  if ! python3 - "$STATUS_FILE" <<'PY'
import json, sys
path = sys.argv[1]
try:
    with open(path, encoding="utf-8") as f:
        st = json.load(f)
except Exception as e:
    print(f"FAIL: status json parse: {e}", file=sys.stderr)
    sys.exit(1)
steers = st.get("steers") or []
if not steers:
    print("FAIL: no steers in status", file=sys.stderr)
    sys.exit(1)
ok_ev = {
    "prompt_complete",
    "prompt_result",
    "running_prompt_id",
    "promptId_notification_meta",
}
applied = [s for s in steers if s.get("mailbox_status") == "applied"]
if not applied:
    print(f"FAIL: no steer with mailbox_status=applied: {steers}", file=sys.stderr)
    sys.exit(1)
good = [s for s in applied if s.get("backend_ack") in ok_ev]
if not good:
    print(f"FAIL: applied steers lack matching evidence: {applied}", file=sys.stderr)
    sys.exit(1)
print(f"PASS: steer applied evidence={good[0].get('backend_ack')}", file=sys.stderr)
state_steers = (st.get("state") or {}).get("steers") or {}
for cid, s in state_steers.items():
    if s.get("status") not in (None, "applied", "delivered"):
        print(
            f"FAIL: state.steers[{cid}].status={s.get('status')} evidence={s.get('evidence')}",
            file=sys.stderr,
        )
        sys.exit(1)
if state_steers:
    print("PASS: state.steers terminal applied", file=sys.stderr)
sys.exit(0)
PY
  then
    FAIL=1
  fi
  if [[ "$FAIL" -ne 0 ]]; then
    echo "STRICT GROK SMOKE FAILED" >&2
    echo "final_file=$FINAL_FILE" >&2
    echo "body_preview:" >&2
    head -c 800 <<<"$BODY" >&2 || true
    echo >&2
    exit 1
  fi
  echo "STRICT GROK SMOKE PASSED" >&2
fi

exit 0
