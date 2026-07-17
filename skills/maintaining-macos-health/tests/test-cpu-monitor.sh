#!/bin/bash
set -e
set -o pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")/.." && pwd)
CHECK_SCRIPT="$SCRIPT_DIR/assets/mac-health-check"
TEST_ROOT=$(mktemp -d "${TMPDIR:-/tmp}/mac-health-cpu-tests.XXXXXX")

cleanup() {
  if [ -n "$TEST_ROOT" ] && [ -d "$TEST_ROOT" ]; then
    rm -rf "$TEST_ROOT"
  fi
}
trap cleanup EXIT

fail() {
  printf 'FAIL: %s\n' "$*" >&2
  exit 1
}

assert_count() {
  local expected="$1" pattern="$2" file="$3"
  local actual=0
  actual=$(grep -c "$pattern" "$file" 2>/dev/null || true)
  [ "$actual" = "$expected" ] || fail "expected $expected matches for '$pattern', got $actual"
}

setup_case() {
  local name="$1"
  CASE_DIR="$TEST_ROOT/$name"
  CASE_LOG_DIR="$CASE_DIR/logs"
  CASE_STATE_DIR="$CASE_DIR/state"
  CASE_PS="$CASE_DIR/ps.txt"
  CASE_IOSTAT="$CASE_DIR/iostat.txt"
  CASE_CONFIG="$CASE_DIR/config.sh"
  CASE_NOW=100000
  mkdir -p "$CASE_DIR" "$CASE_LOG_DIR" "$CASE_STATE_DIR"

  cat > "$CASE_CONFIG" <<EOF
DISK_VOLUME=/System/Volumes/Data
DISK_CRITICAL_PCT=0
SWAP_CRITICAL_GB=999
MEM_FREE_CRITICAL_PCT=0
COOLDOWN_MINUTES=30
HYSTERESIS_READINGS=99
CALIBRATION_DAYS=99
SUPPRESS_FILE=/dev/null/mac-health-never
NTFY_URL=
NOTIFIER=none
JETSAM_DIR=$CASE_DIR/no-jetsam
CPU_ENABLED=1
CPU_SYSTEM_BUSY_PCT=90
CPU_SYSTEM_BUSY_READINGS=2
CPU_PROCESS_HOT_PCT=80
CPU_PROCESS_HOT_READINGS=2
CPU_PROCESS_LEAK_PCT=40
CPU_PROCESS_LEAK_READINGS=3
CPU_PROCESS_RECOVERY_PCT=20
CPU_SYSTEM_RECOVERY_PCT=70
CPU_RECOVERY_READINGS=2
CPU_MAX_SAMPLE_GAP_MINUTES=15
CPU_IGNORE_REGEX='^(kernel_task|WindowServer|mac-health-check|ps|iostat)$'
CPU_LOG_TOP_N=5
CPU_ALERT_TOP_N=3
CPU_INCIDENT_RETENTION_DAYS=30
CPU_PS_FIXTURE=$CASE_PS
CPU_IOSTAT_FIXTURE=$CASE_IOSTAT
EOF
}

run_check() {
  MAC_HEALTH_CONFIG="$CASE_CONFIG" \
  MAC_HEALTH_LOG_DIR="$CASE_LOG_DIR" \
  MAC_HEALTH_STATE_DIR="$CASE_STATE_DIR" \
  MAC_HEALTH_NOW="$CASE_NOW" \
    /bin/bash "$CHECK_SCRIPT"
}

write_system_sample() {
  local idle_pct="$1"
  cat > "$CASE_IOSTAT" <<EOF
              disk0       cpu    load average
    KB/t  tps  MB/s  us sy id   1m   5m   15m
    5.00  100  1.00  10 10 $idle_pct  1.00 1.00 1.00
EOF
}

# A hot process alerts once, stays deduplicated, recovers, then can alert again.
setup_case process_lifecycle
write_system_sample 80
cat > "$CASE_PS" <<EOF
111 1 95.0 01:00:00 /tmp/csharp-ls
222 1 5.0 00:10:00 /tmp/normal-worker
EOF
run_check
assert_count 0 'ALERT key=cpu_process_advisory' "$CASE_LOG_DIR/health.log"
run_check
assert_count 1 'ALERT key=cpu_process_advisory' "$CASE_LOG_DIR/health.log"
run_check
assert_count 1 'ALERT key=cpu_process_advisory' "$CASE_LOG_DIR/health.log"

cat > "$CASE_PS" <<EOF
111 1 5.0 01:20:00 /tmp/csharp-ls
222 1 5.0 00:30:00 /tmp/normal-worker
EOF
run_check
run_check
assert_count 1 "cpu process recovered name='csharp-ls'" "$CASE_LOG_DIR/health.log"

cat > "$CASE_PS" <<EOF
111 1 95.0 01:40:00 /tmp/csharp-ls
EOF
run_check
run_check
assert_count 2 'ALERT key=cpu_process_advisory' "$CASE_LOG_DIR/health.log"

# Whole-system saturation alerts once and rearms only after recovery.
setup_case system_lifecycle
write_system_sample 5
cat > "$CASE_PS" <<EOF
333 1 15.0 00:30:00 /tmp/worker
EOF
run_check
run_check
assert_count 1 'ALERT key=cpu_system_critical' "$CASE_LOG_DIR/health.log"
run_check
assert_count 1 'ALERT key=cpu_system_critical' "$CASE_LOG_DIR/health.log"

write_system_sample 80
run_check
run_check
assert_count 1 'cpu system recovered' "$CASE_LOG_DIR/health.log"

write_system_sample 5
run_check
run_check
assert_count 2 'ALERT key=cpu_system_critical' "$CASE_LOG_DIR/health.log"

# Ignored executables remain diagnostic context but never become advisories.
setup_case ignored_process
write_system_sample 80
cat > "$CASE_PS" <<EOF
444 1 180.0 02:00:00 /tmp/kernel_task
EOF
run_check
run_check
run_check
assert_count 0 'ALERT key=cpu_process_advisory' "$CASE_LOG_DIR/health.log"
grep -q 'kernel_task pid=444 cpu=180%' "$CASE_LOG_DIR/health.log" \
  || fail 'ignored process missing from diagnostic top list'

# A long sleep/missed interval breaks the consecutive-reading streak.
setup_case sample_gap
write_system_sample 80
cat > "$CASE_PS" <<EOF
555 1 95.0 00:30:00 /tmp/gap-worker
EOF
run_check
CASE_NOW=$(( CASE_NOW + 1200 ))
run_check
assert_count 0 'ALERT key=cpu_process_advisory' "$CASE_LOG_DIR/health.log"
CASE_NOW=$(( CASE_NOW + 300 ))
run_check
assert_count 1 'ALERT key=cpu_process_advisory' "$CASE_LOG_DIR/health.log"
assert_count 1 'cpu process sample gap exceeded' "$CASE_LOG_DIR/health.log"

printf 'PASS: CPU monitor lifecycle, deduplication, recovery, rearm, ignore rules, and gap reset\n'
