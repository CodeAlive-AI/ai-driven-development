#!/bin/sh
set -eu

source_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
asset_dir=$(CDPATH= cd -- "$source_dir/.." && pwd)
gate="$asset_dir/memory-pressure-gate.sh"
tmp_parent=${TMPDIR:-/tmp}
tmp_parent=${tmp_parent%/}
tmp=$(mktemp -d "$tmp_parent/memory-guard-integration.XXXXXX")
guard_pid=
plain_one=
plain_two=
plain_small=
codex_pid=
protected_pid=
app_pid=

cleanup_children() {
  if [ -n "$guard_pid" ]; then
    kill -TERM "$guard_pid" 2>/dev/null || true
    wait "$guard_pid" 2>/dev/null || true
  fi
  for pid in "$plain_one" "$plain_two" "$plain_small" "$codex_pid" "$protected_pid" \
    "$app_pid"; do
    if [ -n "$pid" ]; then
      kill -CONT "$pid" 2>/dev/null || true
      kill -TERM "$pid" 2>/dev/null || true
    fi
  done
  sleep 0.1
  for pid in "$guard_pid" "$plain_one" "$plain_two" "$plain_small" "$codex_pid" \
    "$protected_pid" "$app_pid"; do
    if [ -n "$pid" ]; then
      child_cmd=$(ps -p "$pid" -o command= 2>/dev/null || true)
      case "$child_cmd" in
        "$tmp"/*)
          kill -KILL "$pid" 2>/dev/null || true
          ;;
      esac
      wait "$pid" 2>/dev/null || true
    fi
  done
}

clear_child_pids() {
  guard_pid=
  plain_one=
  plain_two=
  plain_small=
  codex_pid=
  protected_pid=
  app_pid=
}

cleanup_and_clear_children() {
  cleanup_children
  clear_child_pids
}
trap cleanup_children EXIT HUP INT TERM

sh "$gate" run xcrun clang -O0 "$source_dir/tests/signal_child.c" -o "$tmp/child"
cp "$tmp/child" "$tmp/plain-one"
cp "$tmp/child" "$tmp/plain-two"
cp "$tmp/child" "$tmp/plain-small"
cp "$tmp/child" "$tmp/codex"
cp "$tmp/child" "$tmp/protected-child"
mkdir -p "$tmp/Editor.app/Contents/Frameworks/Nested.app/Contents/Frameworks"
cp "$tmp/child" "$tmp/Editor.app/Contents/Frameworks/Nested.app/Contents/Frameworks/app-helper"
sh "$asset_dir/build-memory-guard.sh" "$tmp/mac-memory-guard"

start_children() {
  "$tmp/plain-one" & plain_one=$!
  "$tmp/plain-two" & plain_two=$!
  "$tmp/plain-small" & plain_small=$!
  "$tmp/codex" & codex_pid=$!
  "$tmp/protected-child" & protected_pid=$!
  "$tmp/Editor.app/Contents/Frameworks/Nested.app/Contents/Frameworks/app-helper" & app_pid=$!
  sleep 0.2
}

write_config() {
  mode=$1
  state=$2
  log=$3
  cat > "$tmp/config" <<EOF
MODE=$mode
FREEZE_MIN_MB=7
TIER_MIN_MB=1
ALERT_PCT=60
EMERGENCY_PCT=80
ALERT_TREND_PCT=90
EMERGENCY_TREND_PCT=95
TIER_B_PCT=88
TIER_C_PCT=93
PROTECT=*protected-child
ALERTER=$tmp/not-installed
STATE_PATH=$state
LOG_PATH=$log
EOF
}

write_series() {
  file=$1
  shift
  : > "$file"
  for value in "$@"; do
    printf '%s 100 0 0\n' "$value" >> "$file"
  done
}

is_stopped() {
  ps -p "$1" -o stat= 2>/dev/null | grep -q 'T'
}

assert_running() {
  stat=$(ps -p "$1" -o stat= 2>/dev/null || true)
  if [ -z "$stat" ]; then
    echo "FAIL: pid $1 should still exist" >&2
    exit 1
  fi
  case "$stat" in
    *T*)
      echo "FAIL: pid $1 should be running" >&2
      exit 1
      ;;
  esac
}

assert_stopped() {
  if ! is_stopped "$1"; then
    echo "FAIL: pid $1 should be stopped" >&2
    exit 1
  fi
}

assert_timestamped_log() {
  if ! awk '
    {
      if (substr($0, 5, 1) != "-" || substr($0, 8, 1) != "-" ||
          substr($0, 11, 1) != "T" || substr($0, 14, 1) != ":" ||
          substr($0, 17, 1) != ":" ||
          (substr($0, 20, 1) != "+" && substr($0, 20, 1) != "-") ||
          substr($0, 23, 1) != ":" || substr($0, 26, 1) != " ")
        exit 1
      seen = 1
    }
    END { if (!seen) exit 1 }
  ' "$1"; then
    echo "FAIL: log lines are not local ISO 8601 timestamps: $1" >&2
    exit 1
  fi
}

start_children
write_config act "$tmp/a.state" "$tmp/a.log"
{
  printf '1 50 100 0 0\n'
  printf '2 60 100 0 0\n3 60 100 0 0\n'
  printf '4 10 100 0 0\n63 10 100 0 0\n64 10 100 0 0\n'
  printf '78 10 100 0 0\n79 10 100 0 0\n'
} > "$tmp/a.metrics"
"$tmp/mac-memory-guard" run --config "$tmp/config" --test-metrics "$tmp/a.metrics" \
  --test-root "$$" --test-tick-ms 500 > "$tmp/a.out" 2>&1 &
guard_pid=$!
attempt=0
while [ "$attempt" -lt 30 ]; do
  if is_stopped "$plain_one" && is_stopped "$plain_two"; then
    break
  fi
  attempt=$((attempt + 1))
  sleep 0.2
done
assert_stopped "$plain_one"
assert_stopped "$plain_two"
assert_running "$codex_pid"
assert_running "$protected_pid"
assert_running "$app_pid"
assert_running "$plain_small"
attempt=0
while [ "$attempt" -lt 60 ]; do
  stopped=0
  is_stopped "$plain_one" && stopped=$((stopped + 1))
  is_stopped "$plain_two" && stopped=$((stopped + 1))
  if [ "$stopped" -eq 1 ]; then
    break
  fi
  attempt=$((attempt + 1))
  sleep 0.2
done
stopped=0
is_stopped "$plain_one" && stopped=$((stopped + 1))
is_stopped "$plain_two" && stopped=$((stopped + 1))
if [ "$stopped" -ne 1 ]; then
  echo "FAIL: expected one A unit resumed after the first 60 seconds" >&2
  exit 1
fi
attempt=0
while [ "$attempt" -lt 60 ]; do
  if ! is_stopped "$plain_one" && ! is_stopped "$plain_two"; then
    break
  fi
  attempt=$((attempt + 1))
  sleep 0.2
done
assert_running "$plain_one"
assert_running "$plain_two"
wait "$guard_pid"
guard_pid=
echo "PASS (a): ALERT stopped tier A; CALM resumed one unit 15 seconds apart"

write_config act "$tmp/b.state" "$tmp/b.log"
{
  printf '1 50 100 0 0\n2 60 100 0 0\n3 60 100 0 0\n'
  printf '4 85 100 0 0\n5 85 100 0 0\n8 85 100 0 0\n'
  printf '11 85 100 0 0\n14 90 100 0 0\n17 95 100 0 0\n'
} > "$tmp/b.metrics"
"$tmp/mac-memory-guard" run --config "$tmp/config" --test-metrics "$tmp/b.metrics" \
  --test-root "$$" --test-tick-ms 10 > "$tmp/b.out" 2>&1 &
guard_pid=$!
wait_for_signal() {
  pattern=$1
  expected=$2
  attempt=0
  while [ "$attempt" -lt 120 ]; do
    observed=$(grep -c "$pattern" "$tmp/b.log" 2>/dev/null || true)
    if [ "${observed:-0}" -ge "$expected" ]; then
      return 0
    fi
    attempt=$((attempt + 1))
    sleep 0.05
  done
  echo "FAIL: missing signal pattern $pattern count $expected" >&2
  exit 1
}
assert_dead() {
  stat=$(ps -p "$1" -o stat= 2>/dev/null || true)
  case "$stat" in
    ""|*Z*) ;;
    *)
      echo "FAIL: pid $1 should have been killed" >&2
      exit 1
      ;;
  esac
}
wait_for_signal 'signal=SIGTERM name=plain-' 1
assert_running "$codex_pid"
assert_running "$app_pid"
assert_running "$plain_small"
wait_for_signal 'signal=SIGTERM name=plain-' 2
assert_running "$codex_pid"
assert_running "$app_pid"
assert_running "$plain_small"
wait_for_signal 'signal=SIGTERM name=plain-small' 1
assert_dead "$plain_small"
assert_running "$codex_pid"
assert_running "$app_pid"
wait_for_signal 'signal=SIGTERM name=codex' 1
assert_running "$app_pid"
wait_for_signal 'signal=SIGTERM name=app-helper' 1
wait "$guard_pid"
guard_pid=
assert_dead "$plain_one"
assert_dead "$plain_two"
assert_dead "$codex_pid"
assert_dead "$app_pid"
assert_running "$protected_pid"
echo "PASS (b): at 85% frozen A then unfrozen A; B at 90%, C at 95%"
cleanup_and_clear_children

start_children
write_config observe "$tmp/c.state" "$tmp/c.log"
write_series "$tmp/c.metrics" '1 50' '2 60' '3 60' '4 85' '5 85'
"$tmp/mac-memory-guard" run --config "$tmp/config" --test-metrics "$tmp/c.metrics" \
  --test-root "$$" --test-tick-ms 1 > "$tmp/c.out" 2>&1
assert_running "$protected_pid"
assert_running "$plain_one"
assert_running "$plain_two"
assert_running "$codex_pid"
assert_running "$app_pid"
assert_running "$plain_small"
echo "PASS (c): observe script sent no signals"
cleanup_and_clear_children

"$tmp/plain-one" & plain_one=$!
write_config act "$tmp/d.state" "$tmp/d.log"
{
  printf '1 50 100 0 0\n2 60 100 0 0\n3 60 100 0 0\n'
  second=4
  while [ "$second" -le 1000 ]; do
    printf '%s 60 100 0 0\n' "$second"
    second=$((second + 1))
  done
} > "$tmp/d.metrics"
"$tmp/mac-memory-guard" run --config "$tmp/config" --test-metrics "$tmp/d.metrics" \
  --test-root "$$" --test-tick-ms 10 > "$tmp/d.out" 2>&1 &
guard_pid=$!
attempt=0
while [ "$attempt" -lt 30 ] && ! is_stopped "$plain_one"; do
  attempt=$((attempt + 1))
  sleep 0.1
done
assert_stopped "$plain_one"
kill -TERM "$guard_pid"
wait "$guard_pid"
guard_pid=
assert_running "$plain_one"
echo "PASS (d): SIGTERM shutdown resumed guard-frozen children"
cleanup_and_clear_children

"$tmp/plain-two" & plain_two=$!
sleep 0.2  # let the child exec and set its group first; an earlier stop raced it
kill -STOP "$plain_two"
pgid=$(ps -p "$plain_two" -o pgid= | tr -d ' ')
write_config act "$tmp/e.state" "$tmp/e.log"
printf '%s 0 0 %s 1\n' "$plain_two" "$pgid" > "$tmp/e.state"
write_series "$tmp/e.metrics" '1 10' '2 10'
"$tmp/mac-memory-guard" run --config "$tmp/config" --test-metrics "$tmp/e.metrics" \
  --test-root "$$" --test-tick-ms 1 > "$tmp/e.out" 2>&1
assert_stopped "$plain_two"
kill -CONT "$plain_two"
echo "PASS (e): stale start identity was dropped without signalling its pid"

cleanup_and_clear_children

"$tmp/plain-one" & plain_one=$!
sleep 0.1
"$tmp/plain-two" "$plain_one" & plain_two=$!
sleep 0.2
write_config act "$tmp/f.state" "$tmp/f.log"
{
  printf '1 50 100 0 0\n2 60 100 0 0\n3 60 100 0 0\n'
  printf '4 60 100 0 0\n5 10 100 0 0\n65 10 100 0 0\n66 10 100 0 0\n'
} > "$tmp/f.metrics"
"$tmp/mac-memory-guard" run --config "$tmp/config" --test-metrics "$tmp/f.metrics" \
  --test-root "$$" --test-tick-ms 500 > "$tmp/f.out" 2>&1 &
guard_pid=$!
attempt=0
while [ "$attempt" -lt 30 ]; do
  if is_stopped "$plain_one" && is_stopped "$plain_two"; then
    break
  fi
  attempt=$((attempt + 1))
  sleep 0.1
done
assert_stopped "$plain_one"
assert_stopped "$plain_two"
kill -CONT "$plain_two"
assert_running "$plain_two"
wait "$guard_pid"
guard_pid=
assert_running "$plain_one"
assert_running "$plain_two"
if [ "$(grep -c 'signal=SIGSTOP name=plain-' "$tmp/f.log")" -ne 2 ]; then
  echo "FAIL: partially resumed group was signalled again in the same ALERT episode" >&2
  exit 1
fi
grep -q 'decision=resume name=plain-' "$tmp/f.log"
echo "PASS (f): CALM resumed the remaining frozen member after an external SIGCONT"

cleanup_and_clear_children

# (g) The guard's own notifier is its child, eligible by size and age; it must never be
# frozen (live incident 2026-11-14: the guard froze its own pile of alerter windows).
cp "$tmp/child" "$tmp/alerter"
"$tmp/plain-one" & plain_one=$!
sleep 0.2
write_config act "$tmp/g.state" "$tmp/g.log"
sed "s|^ALERTER=.*|ALERTER=$tmp/alerter|" "$tmp/config" > "$tmp/config.g"
mv "$tmp/config.g" "$tmp/config"
{
  printf '1 50 100 0 0\n2 60 100 0 0\n3 60 100 0 0\n4 60 100 0 0\n5 60 100 0 0\n'
  printf '6 60 100 0 0\n7 60 100 0 0\n8 60 100 0 0\n9 10 100 0 0\n69 10 100 0 0\n'
  printf '70 10 100 0 0\n'
} > "$tmp/g.metrics"
"$tmp/mac-memory-guard" run --config "$tmp/config" --test-metrics "$tmp/g.metrics" \
  --test-root "$$" --test-tick-ms 500 > "$tmp/g.out" 2>&1 &
guard_pid=$!
notifier=
attempt=0
while [ "$attempt" -lt 40 ]; do
  notifier=$(pgrep -f "^$tmp/alerter" | head -1 || true)
  if [ -n "$notifier" ] && is_stopped "$plain_one"; then
    break
  fi
  attempt=$((attempt + 1))
  sleep 0.1
done
if [ -z "$notifier" ]; then
  echo "FAIL: the guard did not start its notifier" >&2
  exit 1
fi
assert_stopped "$plain_one"
sleep 2
assert_running "$notifier"
wait "$guard_pid"
guard_pid=
for pid in $(pgrep -f "^$tmp/alerter" || true); do
  kill -TERM "$pid" 2>/dev/null || true
done
if grep -q 'name=alerter' "$tmp/g.log"; then
  echo "FAIL: the guard selected its own notifier" >&2
  exit 1
fi
assert_running "$plain_one"
echo "PASS (g): the guard never selected its own notifier child"

grep -q 'transition=CALM->ALERT' "$tmp/a.log"
grep -q 'transition=ALERT->CALM' "$tmp/a.log"
assert_timestamped_log "$tmp/a.log"
assert_timestamped_log "$tmp/b.log"
assert_timestamped_log "$tmp/c.log"
assert_timestamped_log "$tmp/d.log"
assert_timestamped_log "$tmp/e.log"
assert_timestamped_log "$tmp/f.log"
assert_timestamped_log "$tmp/g.log"
echo "PASS: transition records and timestamped integration logs"
cleanup_and_clear_children
echo "7 child-only signal integration scenarios passed"
trap - EXIT HUP INT TERM
rm -rf "$tmp"
