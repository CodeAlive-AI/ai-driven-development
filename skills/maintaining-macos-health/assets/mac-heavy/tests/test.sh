#!/bin/bash
set -eu
root=$(cd "$(dirname "$0")/.." && pwd)
tmp=$(mktemp -d "${TMPDIR:-/tmp}/mac-heavy-tests.XXXXXX")
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/bin" "$tmp/home" "$tmp/lockroot"
cat > "$tmp/bin/getconf" <<'SH'
#!/bin/sh
printf '%s/\n' "$MAC_HEAVY_TEST_LOCKROOT"
SH
chmod +x "$tmp/bin/getconf"
export MAC_HEAVY_TEST_LOCKROOT="$tmp/lockroot" HOME="$tmp/home" MAC_HEAVY_STATUS_PATH="$tmp/status" PATH="$tmp/bin:$PATH" TMPDIR="$tmp/lockroot/"
heavy="$root/mac-heavy"
boot=$(sysctl -n kern.boottime | sed -n 's/.*sec = \([0-9]*\), usec = \([0-9]*\).*/\1 \2/p' | awk '{printf "%s.%06d", $1, $2}')
calm() { printf '%s %s CALM 20 0 0 1 0\n' "$(date +%s)" "$boot" > "$MAC_HEAVY_STATUS_PATH"; }
fail() { echo "FAIL: $*" >&2; exit 1; }
/bin/bash -n "$heavy"
calm
"$heavy" printf 'hello\n' > "$tmp/out"
[ "$(cat "$tmp/out")" = hello ] || fail output
"$heavy" /bin/sh -c 'exit 23' || [ "$?" -eq 23 ] || fail exit
if "$heavy" /bin/sh -c 'kill -INT $$'; then fail int_exit_zero; else rc=$?; fi
[ "$rc" -eq 130 ] || fail "int_exit_$rc"
# The child shell expands $1.
# shellcheck disable=SC2016
"$heavy" /bin/bash -c '"$1" printf nested' _ "$heavy" > "$tmp/out"
[ "$(cat "$tmp/out")" = nested ] || fail nested
MAC_HEAVY_LEASE=bogus "$heavy" true 2> "$tmp/err"
grep -q 'does not match' "$tmp/err" || fail mismatch
rm "$MAC_HEAVY_STATUS_PATH"
"$heavy" true 2> "$tmp/err"
grep -q 'status unavailable' "$tmp/err" || fail missing
printf '%s %s CALM 20 0 0 1 0\n' 1 "$boot" > "$MAC_HEAVY_STATUS_PATH"
"$heavy" true 2> "$tmp/err"
grep -q stale "$tmp/err" || fail stale
printf '%s %s ALERT 65 0 0 1 0\n' "$(date +%s)" "$boot" > "$MAC_HEAVY_STATUS_PATH"
"$heavy" --wait 0 true > "$tmp/out" 2> "$tmp/err" && fail alert
[ "$?" = 75 ] || fail alert_status
"$heavy" --now true 2> "$tmp/err"
grep -q BYPASS "$tmp/err" || fail bypass
grep -q '"bypass":true' "$HOME/.local/state/mac-heavy/ledger.jsonl" || fail ledger_bypass
calm
mkdir "$tmp/lockroot/arai-heavy.lock"
printf '%s\n' 99999999 > "$tmp/lockroot/arai-heavy.lock/pid"
"$heavy" true || fail dead_takeover
mkdir "$tmp/lockroot/arai-heavy.lock"
printf '%s\n' "$$" > "$tmp/lockroot/arai-heavy.lock/pid"
printf 'boot=%s\nstart=wrong\n' "$boot" > "$tmp/lockroot/arai-heavy.lock/owner"
"$heavy" true || fail reused_takeover
mkdir "$tmp/lockroot/arai-heavy.lock"
touch -t 200001010000 "$tmp/lockroot/arai-heavy.lock"
"$heavy" true || fail missing_pid
cat > "$tmp/job" <<'SH'
#!/bin/bash
if ! mkdir "$HOME/active" 2>/dev/null; then touch "$HOME/overlap"; fi
printf '%s\n' "$1"
sleep 0.1
rmdir "$HOME/active"
SH
chmod +x "$tmp/job"
pids=
for i in 1 2 3 4 5 6 7 8 9 10; do "$heavy" "$tmp/job" "$i" > "$tmp/out.$i" 2> "$tmp/err.$i" & pids="$pids $!"; done
for pid in $pids; do wait "$pid" || fail "concurrent $pid"; done
[ ! -e "$HOME/overlap" ] || fail overlap
for i in 1 2 3 4 5 6 7 8 9 10; do [ "$(cat "$tmp/out.$i")" = "$i" ] || fail "output $i"; done
calm
mkdir "$tmp/lockroot/arai-heavy.lock"
printf '%s\n' 99999999 > "$tmp/lockroot/arai-heavy.lock/pid"
"$heavy" "$tmp/job" 11 > "$tmp/race.1" 2>/dev/null & first=$!
"$heavy" "$tmp/job" 12 > "$tmp/race.2" 2>/dev/null & second=$!
wait "$first" || fail first_reclaimer
wait "$second" || fail second_reclaimer
[ ! -e "$HOME/overlap" ] || fail reclaimer_overlap
mkdir "$tmp/lockroot/arai-heavy.lock" "$tmp/lockroot/arai-heavy.reclaim"
printf '%s\n' 99999999 > "$tmp/lockroot/arai-heavy.lock/pid"
sleep 30 & reclaimer=$!
reclaimer_start=$(ps -p "$reclaimer" -o lstart= | sed 's/^ *//;s/ *$//')
printf '%s\n%s\n%s\n' "$reclaimer" "$reclaimer_start" "$(date +%s)" > "$tmp/lockroot/arai-heavy.reclaim/owner"
kill -KILL "$reclaimer"
wait "$reclaimer" 2>/dev/null || :
"$heavy" true || fail stale_reclaimer
mkdir "$tmp/lockroot/arai-heavy.lock" "$tmp/lockroot/arai-heavy.reclaim"
printf '%s\n' 99999999 > "$tmp/lockroot/arai-heavy.lock/pid"
printf '%s\nwrong start\n%s\n' "$$" "$(date +%s)" > "$tmp/lockroot/arai-heavy.reclaim/owner"
"$heavy" true || fail reused_reclaimer
mkdir "$tmp/lockroot/arai-heavy.lock" "$tmp/lockroot/arai-heavy.reclaim"
printf '%s\n' 99999999 > "$tmp/lockroot/arai-heavy.lock/pid"
printf '%s\n%s\n%s\n' "$$" "$(ps -p $$ -o lstart= | sed 's/^ *//;s/ *$//')" "$(date +%s)" > "$tmp/lockroot/arai-heavy.reclaim/owner"
touch -t 200001010000 "$tmp/lockroot/arai-heavy.reclaim"
"$heavy" true || fail old_reclaimer
printf 'pid=%s executable=stale project=test since=1\nstart=wrong\n' "$$" > "$HOME/.local/state/mac-heavy/waiting/$$"
"$heavy" status > "$tmp/status.out"
[ ! -e "$HOME/.local/state/mac-heavy/waiting/$$" ] || fail reused_waiter
calm
"$heavy" sleep 30 > "$tmp/held.out" 2> "$tmp/held.err" & holder=$!
for attempt in 1 2 3 4 5 6 7 8 9 10; do
  child_pid=$(sed -n 's/^child_pid=//p' "$tmp/lockroot/arai-heavy.lock/owner" 2>/dev/null || :)
  [ -n "$child_pid" ] && break
  sleep .1
done
[ -n "$child_pid" ] || fail holder_start
wrapper_pgid=$(ps -p "$holder" -o pgid= | tr -d ' ')
child_pgid=$(ps -p "$child_pid" -o pgid= | tr -d ' ')
recorded_pgid=$(sed -n 's/^child_pgid=//p' "$tmp/lockroot/arai-heavy.lock/owner")
[ "$wrapper_pgid" = "$child_pgid" ] && [ "$wrapper_pgid" = "$recorded_pgid" ] || fail shared_process_group
kill -STOP "$child_pid"
"$heavy" status > "$tmp/status.out"
grep -q SUSPENDED "$tmp/status.out" || fail stopped_status
"$heavy" --wait 0 touch "$tmp/should-not-exist" 2>/dev/null && fail stopped_admission
[ ! -e "$tmp/should-not-exist" ] || fail stopped_started
kill -CONT "$child_pid"
kill -TERM "$holder"
wait "$holder" || result=$?
[ "${result:-0}" = 143 ] || fail "running_TERM ${result:-0}"
calm
perl -MPOSIX=setsid -e 'setsid() >= 0 or die "setsid"; exec @ARGV or die "exec"' "$heavy" sleep 30 > "$tmp/session.out" 2> "$tmp/session.err" & group_holder=$!
attempt=0
while [ "$attempt" -lt 30 ]; do
  recorded_pgid=$(sed -n 's/^child_pgid=//p' "$tmp/lockroot/arai-heavy.lock/owner" 2>/dev/null || :)
  [ "$recorded_pgid" = "$group_holder" ] && break
  sleep .1; attempt=$((attempt+1))
done
[ "$recorded_pgid" = "$group_holder" ] || fail isolated_group_start
kill -STOP -- "-$group_holder"
"$heavy" status > "$tmp/group-status.out"
grep -q SUSPENDED "$tmp/group-status.out" || fail stopped_group_status
"$heavy" --wait 0 touch "$tmp/group-should-not-exist" 2>/dev/null && fail stopped_group_admission
[ ! -e "$tmp/group-should-not-exist" ] || fail stopped_group_started
kill -CONT -- "-$group_holder"
kill -TERM "$group_holder"
wait "$group_holder" || :
calm
"$heavy" sleep 30 > "$tmp/held.out" 2> "$tmp/held.err" & holder=$!
attempt=0
while [ "$attempt" -lt 10 ]; do [ -f "$tmp/lockroot/arai-heavy.lock/owner" ] && break; sleep .1; attempt=$((attempt+1)); done
perl -e '
  my $p = fork(); die "fork" unless defined $p;
  if (!$p) { $SIG{INT} = "DEFAULT"; open STDERR, ">", $ARGV[1] or die $!; exec $ARGV[0], "true"; die $!; }
  select undef, undef, undef, .5; kill "INT", $p; waitpid $p, 0;
  exit(($? >> 8) == 130 ? 0 : 1);
' "$heavy" "$tmp/wait.err" || fail waiting_INT
kill -TERM "$holder"
wait "$holder" || :
calm
export MAC_HEAVY_TEST_TOOL="$heavy"
expect <<'EXPECT' > "$tmp/tty.out" || { cat "$tmp/tty.out" >&2; fail terminal_input; }
set timeout 8
spawn -noecho $env(MAC_HEAVY_TEST_TOOL) /bin/bash -c {echo READY; read x; echo read:$x}
expect -re {(^|\r\n)READY\r\n} {} timeout {exit 1} eof {exit 1}
send "hello-tty\r"
expect -re {\r\nread:hello-tty\r\n} {} timeout {exit 1} eof {exit 1}
expect eof
lassign [wait] pid spawnid os_error result
exit $result
EXPECT
tr -d '\r' < "$tmp/tty.out" | awk 'NF && $0 != "READY" && $0 != "hello-tty" && $0 != "read:hello-tty" { exit 1 }' || fail unexpected_terminal_output
calm
expect <<'EXPECT' > "$tmp/ctrlc.out" || { cat "$tmp/ctrlc.out" >&2; fail terminal_ctrl_c; }
set timeout 4
spawn -noecho $env(MAC_HEAVY_TEST_TOOL) /bin/sh -c {echo READY; exec sleep 30}
expect -re {(^|\r\n)READY\r\n} {} timeout {exit 1} eof {exit 1}
send "\003"
expect {
  eof {}
  timeout {exec kill -TERM [exp_pid]; expect eof; exit 1}
}
lassign [wait] pid spawnid os_error result
if {$result != 130} { exit 1 }
EXPECT
calm
"$heavy" -- sh -c 'printf abc | tr a-z A-Z' > "$tmp/pipeline.out"
[ "$(cat "$tmp/pipeline.out")" = ABC ] || fail pipeline
calm
# Perl, not the shell, expands the variables in this child program.
# shellcheck disable=SC2016
"$heavy" perl -e '$|=1; $SIG{TERM}=sub { open my $f, ">>", $ARGV[0] or die; print $f "TERM\n"; close $f; exit 42 }; print "READY\n"; sleep 30' "$tmp/term.count" > "$tmp/term.ready" 2> "$tmp/term.err" & term_holder=$!
attempt=0
while [ "$attempt" -lt 30 ] && ! grep -q READY "$tmp/term.ready"; do sleep .1; attempt=$((attempt+1)); done
grep -q READY "$tmp/term.ready" || fail term_child_start
kill -TERM "$term_holder"
kill -TERM "$term_holder" 2>/dev/null || :
term_result=0
wait "$term_holder" || term_result=$?
[ "$term_result" -eq 42 ] || fail "term_child_exit $term_result"
[ "$(wc -l < "$tmp/term.count" | tr -d ' ')" -eq 1 ] || fail term_delivery_count
echo 1 > "$HOME/.local/state/mac-heavy/ledger.started"
pids=
for i in 1 2 3 4 5 6 7 8 9 10; do
  "$heavy" --now --label "concurrent-$i" true > /dev/null 2> "$tmp/bypass.$i.err" & pids="$pids $!"
done
for pid in $pids; do wait "$pid" || fail concurrent_ledger_job; done
for i in 1 2 3 4 5 6 7 8 9 10; do
  # Count matching lines across current and rotated files, without filenames.
  # shellcheck disable=SC2126
  count=$(grep -h -F '"label":"concurrent-'"$i"'"' "$HOME"/.local/state/mac-heavy/ledger*.jsonl | wc -l | tr -d ' ')
  [ "$count" -eq 2 ] || fail "ledger_lines_$i=$count"
done
echo 'PASS: terminal Ctrl-C, pipeline, TERM exactly once and concurrent ledger rotation'
grep -h -q '"suspended":true' "$HOME"/.local/state/mac-heavy/ledger*.jsonl || fail suspended_ledger
echo 'PASS: racing cleaners, stopped holder and TERM forwarding'
! grep -h -q 'sensitive-argument' "$HOME"/.local/state/mac-heavy/ledger*.jsonl || fail argv
"$heavy" printf '%s' sensitive-argument > /dev/null
! grep -h -q 'sensitive-argument' "$HOME"/.local/state/mac-heavy/ledger*.jsonl || fail argv
printf 'PASS: bash syntax, output, status, nesting, stale takeover, bypass, ledger and 10-way exclusion\n'
