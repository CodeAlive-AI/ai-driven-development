#!/bin/bash
set -eu
root=$(cd "$(dirname "$0")/.." && pwd)
tmp=$(mktemp -d "${TMPDIR:-/tmp}/mac-heavy-tests.XXXXXX")
trap 'jobs -pr | xargs -r kill 2>/dev/null || :; rm -rf "$tmp"' EXIT
mkdir -p "$tmp/bin" "$tmp/home" "$tmp/lockroot"
printf '#!/bin/sh\n[ -z "${MAC_HEAVY_TEST_EMPTY_GETCONF:-}" ] || exit 0\nprintf "%%s/\\n" "$MAC_HEAVY_TEST_LOCKROOT"\n' > "$tmp/bin/getconf"
chmod +x "$tmp/bin/getconf"
export MAC_HEAVY_TEST_LOCKROOT="$tmp/lockroot" HOME="$tmp/home" MAC_HEAVY_DIR="$tmp/queue" MAC_HEAVY_STATUS_PATH="$tmp/status" PATH="$tmp/bin:$PATH"
export MAC_HEAVY_GRACE=2 MAC_HEAVY_BUSY_CPU=10 MAC_HEAVY_BUSY_RSS_MB=1024
heavy="$root/mac-heavy"
boot=$(sysctl -n kern.boottime | sed -n 's/.*sec = \([0-9]*\), usec = \([0-9]*\).*/\1 \2/p' | awk '{printf "%s.%06d", $1, $2}')
calm() { printf '%s %s CALM 20 0 0 1 0\n' "$(date +%s)" "$boot" > "$MAC_HEAVY_STATUS_PATH"; }
fail() { echo "FAIL: $*" >&2; exit 1; }
waitfile() { local i=0; while [ ! -e "$1" ] && [ "$i" -lt 100 ]; do sleep .05; i=$((i+1)); done; [ -e "$1" ] || fail "missing $1"; }
stop() { kill "$1" 2>/dev/null || :; wait "$1" 2>/dev/null || :; }
start_idle() { calm; "$heavy" sleep 30 > /dev/null 2> "$tmp/idle.err" & idle=$!; waitfile "$MAC_HEAVY_DIR/holders/$idle"; }
start_busy() { calm; "$heavy" /bin/sh -c 'touch "$1"; exec yes > /dev/null' _ "$tmp/ready" 2> "$tmp/busy.err" & busy=$!; waitfile "$tmp/ready"; }
expect75() { local rc=0; "$@" 2> "$tmp/expect.err" || rc=$?; [ "$rc" -eq 75 ] || fail "expected 75, got $rc"; }
calm
rc=0
"$heavy" --wait 5 -- sh -c 'exit 7' || rc=$?
[ "$rc" -eq 7 ] || fail "separator exit $rc"
"$heavy" --label x true || fail label_command
grep -q '"label":"x"' "$HOME/.local/state/mac-heavy/ledger.jsonl" || fail label_ledger
"$heavy" true
"$heavy" status > "$tmp/tail.status"
tail -n 5 "$HOME/.local/state/mac-heavy/ledger.jsonl" > "$tmp/tail.expected"
sed -n '/^ledger (last 5):$/,$ { /^ledger (last 5):$/d; p; }' "$tmp/tail.status" > "$tmp/tail.actual"
[ "$(wc -l < "$tmp/tail.actual" | tr -d ' ')" -eq 5 ] || fail ledger_tail_count
cmp -s "$tmp/tail.expected" "$tmp/tail.actual" || fail ledger_tail_contents
echo 'PASS: separator, label and last five ledger records'
for option in --help -h; do
  "$heavy" "$option" touch "$tmp/help-ran" > "$tmp/help.out" || fail "help $option"
  [ ! -e "$tmp/help-ran" ] || fail help_ran
  grep -q '^usage:' "$tmp/help.out" || fail help_usage
  grep -q 'status' "$tmp/help.out" || fail help_status
  grep -q '75.*nothing ran' "$tmp/help.out" || fail help_timeout
done
rc=0
"$heavy" --unknown touch "$tmp/unknown-ran" 2> "$tmp/unknown.err" || rc=$?
[ "$rc" -eq 2 ] && [ ! -e "$tmp/unknown-ran" ] || fail unknown_option
grep -q 'unknown option --unknown.*nothing ran' "$tmp/unknown.err" || fail unknown_message
grep -q '^usage:' "$tmp/unknown.err" || fail unknown_usage
rc=0
"$heavy" --wait nope touch "$tmp/bad-wait-ran" 2> "$tmp/bad-wait.err" || rc=$?
[ "$rc" -eq 2 ] && [ ! -e "$tmp/bad-wait-ran" ] || fail bad_wait
grep -q 'bad --wait.*nothing ran' "$tmp/bad-wait.err" || fail bad_wait_message
grep -q '^usage:' "$tmp/bad-wait.err" || fail bad_wait_usage
touch "$tmp/not-directory"
rc=0
MAC_HEAVY_DIR="$tmp/not-directory/queue" "$heavy" true 2> "$tmp/mkdir.err" || rc=$?
[ "$rc" -ne 0 ] || fail queue_directory_error
grep -q 'nothing ran' "$tmp/mkdir.err" || fail queue_directory_message
mkdir -p "$tmp/locked/lock"
rc=0
MAC_HEAVY_DIR="$tmp/locked" "$heavy" true 2> "$tmp/lock.err" || rc=$?
[ "$rc" -ne 0 ] || fail queue_lock_error
grep -q 'nothing ran' "$tmp/lock.err" || fail queue_lock_message
mkdir "$tmp/fallback" "$tmp/cwd"
(
  cd "$tmp/cwd"
  unset MAC_HEAVY_DIR
  export MAC_HEAVY_TEST_EMPTY_GETCONF=1 TMPDIR="$tmp/fallback"
  "$heavy" touch "$tmp/fallback-ran"
)
[ -e "$tmp/fallback-ran" ] || fail fallback_command
[ -d "$tmp/fallback/mac-heavy" ] || fail fallback_queue
[ ! -e "$tmp/cwd/mac-heavy" ] || fail relative_queue
echo 'PASS: help, refusals and getconf fallback'
start_idle
sleep 3
calm
"$heavy" true 2> "$tmp/lend.err" || fail lending
grep -q 'started beside idle' "$tmp/lend.err" || fail lending_notice
grep -q '"beside":1' "$HOME/.local/state/mac-heavy/ledger.jsonl" || fail lending_ledger
stop "$idle"
echo 'PASS: idle lending and ledger'
rm -f "$tmp/ready"; start_busy
expect75 "$heavy" --wait 0 touch "$tmp/not-run"
[ ! -e "$tmp/not-run" ] || fail busy_started
grep -q '"event":"timeout"' "$HOME/.local/state/mac-heavy/ledger.jsonl" || fail timeout_ledger
"$heavy" --now true 2> "$tmp/now.err" || fail bypass
grep -q BYPASS "$tmp/now.err" || fail bypass_notice
grep -q '"bypass":true' "$HOME/.local/state/mac-heavy/ledger.jsonl" || fail bypass_ledger
"$heavy" status > "$tmp/status.out"
grep -q BUSY "$tmp/status.out" || fail busy_status
stop "$busy"
echo 'PASS: busy exclusion, timeout, bypass and status'
start_idle
expect75 "$heavy" --wait 0 true
stop "$idle"
echo 'PASS: grace'
export MAC_HEAVY_GRACE=0 MAC_HEAVY_BUSY_RSS_MB=1
start_idle
expect75 "$heavy" --wait 0 true
stop "$idle"
export MAC_HEAVY_BUSY_RSS_MB=1024
echo 'PASS: RSS'
start_idle
kill -KILL "$idle"; wait "$idle" 2>/dev/null || :
calm; "$heavy" true 2> /dev/null || fail dead
[ ! -e "$MAC_HEAVY_DIR/holders/$idle" ] || fail dead_file
# A live process with an incorrect identity and boot must be removed.
sleep 30 & fake=$!
printf '{"start":"wrong","boot":"wrong","epoch":1}' > "$MAC_HEAVY_DIR/holders/$fake"
"$heavy" true 2> /dev/null || fail identity
[ ! -e "$MAC_HEAVY_DIR/holders/$fake" ] || fail identity_file
stop "$fake"
echo 'PASS: dead and mismatched holders'
printf '%s %s ALERT 65 0 0 1 0\n' "$(date +%s)" "$boot" > "$MAC_HEAVY_STATUS_PATH"
expect75 "$heavy" --wait 0 true
rm "$MAC_HEAVY_STATUS_PATH"; "$heavy" true 2> "$tmp/missing.err"; grep -q unavailable "$tmp/missing.err" || fail missing_guard
printf '1 %s CALM 20 0 0 1 0\n' "$boot" > "$MAC_HEAVY_STATUS_PATH"; "$heavy" true 2> "$tmp/stale.err"; grep -q stale "$tmp/stale.err" || fail stale_guard
echo 'PASS: guard'
calm
export MAC_HEAVY_GRACE=5
"$heavy" /bin/sh -c '"$1" true' _ "$heavy" || fail nested
MAC_HEAVY_LEASE=bogus "$heavy" true 2> "$tmp/mismatch.err" || fail mismatch
grep -q 'does not match' "$tmp/mismatch.err" || fail mismatch_notice
"$heavy" /bin/sh -c 'exit 23' || [ "$?" -eq 23 ] || fail exit
"$heavy" /bin/sh -c 'kill -INT $$' || [ "$?" -eq 130 ] || fail int
[ "$(printf input | "$heavy" cat)" = input ] || fail stdin
"$heavy" printf '%s' sensitive-argument > /dev/null
! grep -q sensitive-argument "$HOME/.local/state/mac-heavy/ledger.jsonl" || fail private_ledger
echo 'PASS: nesting, exit, stdin and ledger privacy'
export MAC_HEAVY_GRACE=0
mkdir "$tmp/lockroot/arai-heavy.lock"
yes > /dev/null & old=$!
printf '%s\n' "$old" > "$tmp/lockroot/arai-heavy.lock/pid"
sleep 2
calm; expect75 "$heavy" --wait 0 true
stop "$old"
printf '99999999\n' > "$tmp/lockroot/arai-heavy.lock/pid"
"$heavy" true || fail v1_dead
[ -d "$tmp/lockroot/arai-heavy.lock" ] || fail v1_deleted
rm -rf "$tmp/lockroot/arai-heavy.lock"
echo 'PASS: v1 busy and dead'
# Simultaneous CPU jobs guard a shared marker while burning CPU.
export MAC_HEAVY_GRACE=2
cat > "$tmp/cpu-job" <<'SH'
#!/bin/bash
mkdir "$HOME/active" 2>/dev/null || touch "$HOME/overlap"
perl -MTime::HiRes=time -e '$end=time+0.3; 1 while time<$end'
rmdir "$HOME/active" 2>/dev/null || :
SH
chmod +x "$tmp/cpu-job"
calm; pids=
for i in 1 2 3 4 5 6 7 8 9 10; do "$heavy" "$tmp/cpu-job" 2> "$tmp/job.$i.err" & pids="$pids $!"; done
for p in $pids; do wait "$p" || fail "job $p"; done
[ ! -e "$HOME/overlap" ] || fail concurrent_overlap
echo 'PASS: ten CPU jobs never overlap'
# A waiter remains visible while a busy tree is active.
rm -f "$tmp/ready"; start_busy
"$heavy" touch "$tmp/after" 2> "$tmp/waiter.err" & waiter=$!
waitfile "$MAC_HEAVY_DIR/waiters/$waiter"
"$heavy" status > "$tmp/status.out"
grep -q "pid=$busy" "$tmp/status.out" || fail status_holder
grep -q "pid=$waiter" "$tmp/status.out" || fail status_waiter
pids=
for i in $(seq 1 20); do ( rc=0; "$heavy" --wait 0 touch "$tmp/race.$i" 2>/dev/null || rc=$?; [ "$rc" -eq 75 ] ) & pids="$pids $!"; done
for p in $pids; do wait "$p" || fail race_admitted; done
stop "$waiter"; stop "$busy"
echo 'PASS: waiter status and twenty simultaneous starts'
export MAC_HEAVY_GRACE=0
mkdir "$tmp/lockroot/arai-heavy.lock"
sleep 30 & old=$!; printf '%s\n' "$old" > "$tmp/lockroot/arai-heavy.lock/pid"
calm; "$heavy" true 2> "$tmp/v1idle.err" || fail v1_idle
grep -q 'started beside idle' "$tmp/v1idle.err" || fail v1_lending_notice
stop "$old"; rm -rf "$tmp/lockroot/arai-heavy.lock"
echo 'PASS: v1 idle lends'
for signal in TERM HUP; do
  rm -f "$tmp/signal.ready" "$tmp/signal.count"
  calm
  "$heavy" perl -e '$|=1; my ($s,$ready,$count)=@ARGV; $SIG{$s}=sub { open my $f, ">>", $count or die $!; print $f "$s\n"; close $f; exit 42 }; open my $r, ">", $ready or die $!; close $r; sleep 30' "$signal" "$tmp/signal.ready" "$tmp/signal.count" 2> "$tmp/signal.err" & holder=$!
  waitfile "$tmp/signal.ready"; kill -"$signal" "$holder"; kill -"$signal" "$holder" 2>/dev/null || :
  rc=0; wait "$holder" || rc=$?; [ "$rc" -eq 42 ] || fail "$signal exit $rc"
  [ "$(wc -l < "$tmp/signal.count" | tr -d ' ')" -eq 1 ] || fail "$signal delivery"
done
echo 'PASS: TERM and HUP forwarded once'
echo 'PASS: basic checks'
# Identity and boot checks are independently exercised with a live PID.
sleep 30 & fake=$!
actual=$(ps -p "$fake" -o lstart= | sed 's/^ *//;s/ *$//')
printf '{"start":"wrong","boot":"%s","epoch":1}' "$boot" > "$MAC_HEAVY_DIR/holders/$fake"
calm; "$heavy" true 2>/dev/null || fail wrong_start
[ ! -e "$MAC_HEAVY_DIR/holders/$fake" ] || fail wrong_start_file
printf '{"start":"%s","boot":"wrong","epoch":1}' "$actual" > "$MAC_HEAVY_DIR/holders/$fake"
"$heavy" true 2>/dev/null || fail wrong_boot
[ ! -e "$MAC_HEAVY_DIR/holders/$fake" ] || fail wrong_boot_file
stop "$fake"
echo 'PASS: independent start identity and boot mismatch'
# Show a busy and an idle holder and an actual waiter in one status snapshot.
export MAC_HEAVY_GRACE=1
start_idle; sleep 3; rm -f "$tmp/ready"; start_busy
"$heavy" true 2> "$tmp/waiter.err" & waiter=$!; waitfile "$MAC_HEAVY_DIR/waiters/$waiter"
"$heavy" status > "$tmp/status.out"
grep "pid=$idle" "$tmp/status.out" | grep -q 'IDLE.*mac-heavy' || fail idle_status
grep "pid=$busy" "$tmp/status.out" | grep -q 'BUSY.*mac-heavy' || fail busy_command_status
grep -q "pid=$waiter" "$tmp/status.out" || fail combined_waiter_status
stop "$waiter"; stop "$busy"; stop "$idle"
echo 'PASS: status shows idle, busy and waiter'
calm
perl -MPOSIX=setsid -e 'setsid() >= 0 or die; exec @ARGV' "$heavy" true || fail terminal_less
echo 'PASS: terminal-less execution'
# Hold each first process snapshot briefly: without flock, contenders all
# observe an empty queue before any of them can publish their holder.
mkdir "$tmp/barrier"
export MAC_HEAVY_TEST_BARRIER="$tmp/barrier"
cat > "$tmp/bin/ps" <<'SH'
#!/bin/bash
if [ "${1:-}" = -axo ] && [ "${2:-}" = pid,ppid,pcpu,rss ]; then
  /bin/ps "$@" > "$MAC_HEAVY_TEST_BARRIER/ps.$$"
  mkdir "$MAC_HEAVY_TEST_BARRIER/seen.$$"
  for i in $(seq 1 30); do
    set -- "$MAC_HEAVY_TEST_BARRIER"/seen.*
    [ "$#" -ge 10 ] && break
    sleep .05
  done
  cat "$MAC_HEAVY_TEST_BARRIER/ps.$$"
else
  exec /bin/ps "$@"
fi
SH
chmod +x "$tmp/bin/ps"
rm -f "$HOME/overlap"
calm; pids=
for i in 1 2 3 4 5 6 7 8 9 10; do "$heavy" "$tmp/cpu-job" 2> "$tmp/barrier.$i.err" & pids="$pids $!"; done
for p in $pids; do wait "$p" || fail "barrier job $p"; done
[ ! -e "$HOME/overlap" ] || fail unlocked_admission_overlap
rm -f "$tmp/bin/ps"
echo 'PASS: synchronized admission race'
# Waiting SIGINT must not start the command, and stopped children appear in status.
export MAC_HEAVY_GRACE=10
start_idle
perl -e '
  my ($tool,$out)=@ARGV; my $p=fork(); die unless defined $p;
  if (!$p) { $SIG{INT}="DEFAULT"; open STDERR, ">", $out or die; exec $tool,"touch","$out.ran"; die }
  select undef,undef,undef,0.8; kill "INT",$p; waitpid $p,0;
  exit(($? >> 8)==130 ? 0 : 1);
' "$heavy" "$tmp/int-wait" || fail waiting_int
[ ! -e "$tmp/int-wait.ran" ] || fail waiting_int_ran
child=$(ps -axo pid,ppid | awk -v p="$idle" '$2 == p { print $1; exit }')
[ -n "$child" ] || fail child_pid
kill -STOP "$child"
"$heavy" status > "$tmp/stopped.out"
grep "pid=$idle" "$tmp/stopped.out" | grep -q SUSPENDED || fail suspended_status
kill -CONT "$child"; stop "$idle"
echo 'PASS: waiting INT and suspended child status'
calm
perl -MPOSIX=setsid -e 'setsid() >= 0 or die; exec @ARGV' "$heavy" sleep 30 2> "$tmp/group.err" & group=$!
waitfile "$MAC_HEAVY_DIR/holders/$group"
child=$(ps -axo pid,ppid | awk -v p="$group" '$2 == p { print $1; exit }')
[ -n "$child" ] || fail process_group_child
wrapper_group=$(ps -p "$group" -o pgid= | tr -d ' ')
child_group=$(ps -p "$child" -o pgid= | tr -d ' ')
[ "$wrapper_group" = "$child_group" ] || fail process_group
stop "$group"
echo 'PASS: shared process group'
echo 'PASS: all tests'
