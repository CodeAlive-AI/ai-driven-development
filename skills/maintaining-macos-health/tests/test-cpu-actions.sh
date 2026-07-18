#!/bin/bash
set -e
set -o pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")/.." && pwd)
ACTION_SCRIPT="$SCRIPT_DIR/assets/mac-health-action"
TEST_ROOT=$(mktemp -d "${TMPDIR:-/tmp}/mac-health-action-tests.XXXXXX")
TEST_LOG_DIR="$TEST_ROOT/logs"
TEST_INCIDENT_DIR="$TEST_LOG_DIR/cpu-incidents"
TEST_CONFIG="$TEST_ROOT/config.sh"
LOAD_PID=""

cleanup() {
  if [ -n "$LOAD_PID" ]; then
    kill "$LOAD_PID" 2>/dev/null || true
    wait "$LOAD_PID" 2>/dev/null || true
  fi
  [ -d "$TEST_ROOT" ] && rm -rf "$TEST_ROOT"
}
trap cleanup EXIT

fail() {
  printf 'FAIL: %s\n' "$*" >&2
  exit 1
}

mkdir -p "$TEST_INCIDENT_DIR"
cat > "$TEST_CONFIG" <<EOF
CPU_ACTIONS_ENABLED=1
CPU_PREFER_DESKTOP_APPS=1
CPU_STOP_ACTION_ENABLED=1
CPU_STOP_GRACE_SECONDS=1
CPU_PROCESS_RECOVERY_PCT=1
EOF

/usr/bin/yes >/dev/null &
LOAD_PID=$!
sleep 1
LOAD_COMM=$(/bin/ps -ww -p "$LOAD_PID" -o comm= | /usr/bin/sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
LOAD_HASH=$(printf '%s' "$LOAD_COMM" | /usr/bin/shasum -a 256 | /usr/bin/awk '{print $1}')
LOAD_CPU=$(/bin/ps -p "$LOAD_PID" -o %cpu= | /usr/bin/awk '{printf "%d", $1 + 0.5}')
INCIDENT="$TEST_INCIDENT_DIR/cpu-action.log"

cat > "$INCIDENT" <<EOF
format=2
incident_kind=process
timestamp=2026-07-18 12:00:00
created_epoch=100000
system_busy_pct=95 load_1m=4.0 load_5m=3.0 load_15m=2.0
primary_pid=$LOAD_PID
primary_cpu_pct=$LOAD_CPU
primary_app=yes
primary_process=yes
primary_executable=$LOAD_COMM
primary_executable_hash=$LOAD_HASH
cpu_pct	pid	ppid	elapsed	executable
$LOAD_CPU	$LOAD_PID	$$	00:00:01	$LOAD_COMM
EOF
chmod 600 "$INCIDENT"

MAC_HEALTH_CONFIG="$TEST_CONFIG" \
MAC_HEALTH_LOG_DIR="$TEST_LOG_DIR" \
MAC_HEALTH_ACTION_DRY_RUN=1 \
  "$ACTION_SCRIPT" dispatch investigate-codex "$INCIDENT"
grep -q 'DRY-RUN launch provider=codex' "$TEST_LOG_DIR/health.log" \
  || fail 'Codex dry-run launch was not logged'
grep -q 'Work read-only' "${INCIDENT%.log}-codex.prompt" \
  || fail 'investigation prompt is missing read-only guard'

MAC_HEALTH_CONFIG="$TEST_CONFIG" \
MAC_HEALTH_LOG_DIR="$TEST_LOG_DIR" \
MAC_HEALTH_ACTION_DRY_RUN=1 \
  "$ACTION_SCRIPT" dispatch investigate-claude "$INCIDENT"
grep -q 'DRY-RUN launch provider=claude' "$TEST_LOG_DIR/health.log" \
  || fail 'Claude dry-run launch was not logged'

MAC_HEALTH_CONFIG="$TEST_CONFIG" \
MAC_HEALTH_LOG_DIR="$TEST_LOG_DIR" \
MAC_HEALTH_ACTION_DRY_RUN=1 \
MAC_HEALTH_ACTION_CONFIRM=1 \
  "$ACTION_SCRIPT" dispatch stop-process "$INCIDENT"
grep -q "DRY-RUN stop signal=TERM pid=$LOAD_PID" "$TEST_LOG_DIR/health.log" \
  || fail 'safe TERM dry-run was not logged'
kill -0 "$LOAD_PID" 2>/dev/null || fail 'dry-run unexpectedly stopped the fixture process'

SYSTEM_INCIDENT="$TEST_INCIDENT_DIR/cpu-system-action.log"
{
  printf 'format=2\nincident_kind=system\n'
  printf 'timestamp=2026-07-18 12:00:00\ncreated_epoch=100000\n'
  printf 'system_busy_pct=95 load_1m=4.0 load_5m=3.0 load_15m=2.0\n'
  printf 'primary_pid=%s\nprimary_cpu_pct=%s\n' "$LOAD_PID" "$LOAD_CPU"
  printf 'primary_app=yes\nprimary_process=yes\nprimary_executable=%s\n' "$LOAD_COMM"
  printf 'primary_executable_hash=%s\n' "$LOAD_HASH"
  printf 'cpu_pct\tpid\tppid\telapsed\texecutable\n'
  printf '%s\t%s\t%s\t00:00:01\t%s\n' "$LOAD_CPU" "$LOAD_PID" "$$" "$LOAD_COMM"
} > "$SYSTEM_INCIDENT"
chmod 600 "$SYSTEM_INCIDENT"
MAC_HEALTH_CONFIG="$TEST_CONFIG" \
MAC_HEALTH_LOG_DIR="$TEST_LOG_DIR" \
MAC_HEALTH_ACTION_DRY_RUN=1 \
MAC_HEALTH_ACTION_CONFIRM=1 \
MAC_HEALTH_ACTION_PID="$LOAD_PID" \
  "$ACTION_SCRIPT" dispatch stop-process "$SYSTEM_INCIDENT"
[ "$(grep -c "DRY-RUN stop signal=TERM pid=$LOAD_PID" "$TEST_LOG_DIR/health.log")" = "2" ] \
  || fail 'system incident did not choose and validate the requested target PID'

BAD_INCIDENT="$TEST_INCIDENT_DIR/cpu-bad-identity.log"
/usr/bin/sed 's/^primary_executable_hash=.*/primary_executable_hash=not-the-same-process/' \
  "$INCIDENT" > "$BAD_INCIDENT"
chmod 600 "$BAD_INCIDENT"
if MAC_HEALTH_CONFIG="$TEST_CONFIG" \
   MAC_HEALTH_LOG_DIR="$TEST_LOG_DIR" \
   MAC_HEALTH_ACTION_DRY_RUN=1 \
     "$ACTION_SCRIPT" dispatch stop-process "$BAD_INCIDENT"; then
  fail 'identity mismatch should reject the stop action'
fi
grep -q "stop rejected identity changed pid=$LOAD_PID" "$TEST_LOG_DIR/health.log" \
  || fail 'identity mismatch rejection was not logged'

printf 'PASS: CPU action prompts, desktop/CLI routing, dry-run stop, and PID identity guard\n'
