# Native memory runaway guard

`assets/memory-guard/` contains a native C++17 monitor intended as a last-resort response to rapid compressor growth. During the reported incident, memory use was ordinary until 12:23; eight agents then launched parallel work, 49 `python3.14` processes reached 21.9 GiB by 12:29, 51 reached 66.7 GiB by 12:32, the compressor hit its segment ceiling, and the Mac panicked at 12:39. The five-minute `mac-health-check` could not observe or respond quickly enough. The guard samples every second and ranks owned processes for reversible freeze before gradual termination.

## Signals and kernel mapping

On the validated system (macOS 26.6.2 / Darwin 25.6.0 ARM64), these sysctls are readable without root:

| Guard reading | OID / source | What it represents |
|---|---|---|
| Compressor segments | `vm.compressor.segment.total / vm.compressor.segment.limit` | XNU `c_segment_count / c_segments_limit`: allocated compressor segments and the segment-array ceiling. This is the primary signal and mirrors the panic's “segments limit” percentage. |
| Compressed pages | `vm.compressor.pages_compressed / vm.compressor.pages_compressed_limit` | XNU `c_segment_pages_compressed / c_segment_pages_compressed_limit`: uncompressed input pages held in the compressor and its limit; mirrors the panic's “compressed pages limit” percentage. Optional on other OS builds. |
| Swap | `vm.swapusage` | Used and total swap bytes; used bytes are compared with the sample 60 seconds earlier. |
| Pressure hint | `kern.memorystatus_vm_pressure_level` | XNU dispatch levels: Normal=1, Warning=2 (internal Warning and Urgent are collapsed), Critical=4. The sysctl was readable without root on the validated OS. |

Apple's [`vm_compressor.c`](https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/vm/vm_compressor.c) increments/decrements `c_segment_count`, derives `c_segments_limit` from compressor pool capacity, and compares both segment and compressed-page counts with their limits. The exposed sysctl values are the matching counters. XNU's [`kern_memorystatus_notify.c`](https://github.com/apple-oss-distributions/xnu/blob/main/bsd/kern/kern_memorystatus_notify.c) converts internal levels to dispatch levels before exposing `kern.memorystatus_vm_pressure_level`; that is why the public critical value is 4, not the internal enum value 3. The [`memorystatus.md`](https://github.com/apple-oss-distributions/xnu/blob/main/doc/vm/memorystatus.md) and [`memorystatus_notify.md`](https://github.com/apple-oss-distributions/xnu/blob/main/doc/vm/memorystatus_notify.md) documents explain the kernel recovery and pressure paths. `doctor` checks the primary segment counters and pressure sysctl; failure of the primary pair makes it exit 1, and `run` in act mode refuses to start. Missing optional page metrics are shown as unavailable and do not replace the primary signal.

`kern.memorystatus.kill_on_sustained_pressure_window_s`, `_delay_ms`, and `_count` were present (600, 500, 0) in the probe. Their semantics were not established, so this guard does not depend on them. It never uses sudo or sends a signal to another uid.

## Levels and defaults

Thresholds can be overridden in the optional `~/.config/mac-health/memory-guard.conf`
as `KEY=VALUE` lines. Missing config means compiled defaults and `MODE=observe`.
Sample time is `CLOCK_UPTIME_RAW`; gaps preserve counters and slopes use actual
elapsed seconds.

| Level | Entry | `act` response |
|---|---|---|
| CALM | Default. An alarming condition in two successive valid samples enters ALERT or EMERGENCY. A non-alerting sample permits recovery, including after a restart. | Resume one frozen unit, smallest first, every 15 seconds. |
| ALERT | `alert_now` in two successive valid samples: segments >=60%; 30-second slope projects >=90% within 240 seconds; swap grows >=2 GiB in 60 seconds; or dispatch Critical (4) for 5 samples. Five consecutive critical samples enter ALERT directly. Return to CALM after `alert_now` is false for 60 seconds. | On alarming samples, freeze all tier-A units >=500 MiB by score (footprint + 4x 30-second growth), up to 64 decisions per sample. A unit resumed by the guard within 15 minutes is killed instead, at most one kill per 3 seconds. After 120 seconds from entering ALERT, while `alert_now` remains true, kill frozen units only, largest first, one every 30 seconds; continue freezing newly eligible units. |
| EMERGENCY | `emergency_now` in two successive valid samples: segments >=80%, or the 30-second slope projects >=95% within 45 seconds. The first sample where this condition is false returns to ALERT. | Kill one unit, then re-evaluate on a fresh sample, at least 3 seconds after the prior kill. Order: frozen units by footprint; tier A >=300 MiB by score; tier B >=300 MiB only at segments >=88%; tier C >=300 MiB only at >=93%. A trend alone never opens B or C. |

Elapsed time alone never raises a level. ALERT freezes and repeat kills happen
only on samples where `alert_now` is true. Invalid metrics or failed enumeration
leave the level and counters unchanged and produce no action. After a freeze or
kill, trend uses only later samples. It waits 10 seconds, then uses the newest
post-action sample at least 30 seconds old; before one exists it uses the earliest
post-action sample. Slopes use actual elapsed time. The pressure signal is a hint,
never a precondition.

Example configuration:

```text
MODE=observe
ALERT_PCT=60
ALERT_TREND_PCT=90
TREND_WINDOW=240
EMERGENCY_PCT=80
EMERGENCY_TREND_PCT=95
EMERGENCY_WINDOW=45
SWAP_GROWTH_GIB=2
CRITICAL_PRESSURE=4
CRITICAL_SAMPLES=5
ALERT_HOLD_SECONDS=120
FREEZE_MIN_MB=500
TIER_MIN_MB=300
RECOVERY_SECONDS=60
FREEZE_TWICE_WINDOW_SECONDS=900
TIER_B_PCT=88
TIER_C_PCT=93
ALERTER=/opt/homebrew/bin/alerter
# Optional overrides:
LOG_PATH=/Users/me/Library/Logs/mac-health/memory-guard.log
STATE_PATH=/Users/me/.local/state/mac-health/memory-guard.state
# Optional executable-path globs, one PROTECT= line per pattern
PROTECT=/Users/me/Library/SomeApp/*
```

## Eligible process units

Only the current user's processes are enumerated. Footprint comes from `proc_pid_rusage(..., RUSAGE_INFO_V4)` / `ri_phys_footprint`, not RSS. Processes are sampled with libproc. The guard never touches itself, its ancestors or its own children (its notifier); system executable roots (`/System`, `/usr/libexec`, `/usr/sbin`, `/sbin`, `/Library/Apple`); `launchd`, `loginwindow`, `WindowServer`, `Finder`, `Dock`, `SystemUIServer`, `ControlCenter`, `NotificationCenter`; terminal emulators; `tmux`/`screen`; `sshd`/`ssh-agent`; recognized password managers and VPN clients; an `.app` bundle's main executable; or paths matching `PROTECT`.

- **A, batch work:** younger than 30 minutes, outside `.app`, and not a recognized agent runtime. The unit is a PGID; only eligible tier-A members are signaled.
- **B, command-line work:** older command-line processes and agent runtimes (`claude`, `codex`, `devin`, `opencode`, `gemini`, `grok`, `cursor-agent`). Unit is one process.
- **C, app helpers:** helpers inside an `.app` bundle; the app main executable is protected.

A tier-A unit is the eligible tier-A members sharing a PGID; tiers B and C are individual processes. A tier-A group is selected as one unit, but every signal is sent to a pid individually. A group counts as frozen when any member is guard-frozen; recovery resumes every stopped member. If a member is continued externally, the guard will not send it another SIGSTOP during the same ALERT episode. The `explain` output lists candidate names, tier, frozen state, footprint and growth; it never shows arguments or environment. The score is footprint plus four times growth over 30 seconds.

## Consent and commands

`act` requires both `MODE=act` and `~/.config/mac-health/memory-guard-consent.json` with scope version 2. `consent --accept` prints the precise action scope before recording the timestamp and version. Version-1 consent is invalid. Development and installation are not consent; do not create a consent file on the development machine.

```sh
# Build for this Mac, with Xcode Command Line Tools; no dependencies/downloads.
SKILL=/path/to/maintaining-macos-health
sh "$SKILL/assets/build-memory-guard.sh" "$HOME/bin/mac-memory-guard"

# Observe and inspect
mac-memory-guard doctor
mac-memory-guard status
mac-memory-guard explain
mac-memory-guard run --config "$HOME/.config/mac-health/memory-guard.conf"

# Explicit operator recovery
mac-memory-guard resume --all
mac-memory-guard resume PGID
mac-memory-guard consent --show
mac-memory-guard consent --revoke

# Install only after a separate operational request; this feature remains observe-only until enrolled.
mkdir -p "$HOME/Library/LaunchAgents" "$HOME/Library/Logs/mac-health"
sed "s|__HOME__|$HOME|g" "$SKILL/assets/com.local.mac-memory-guard.plist" \
  > "$HOME/Library/LaunchAgents/com.local.mac-memory-guard.plist"
launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/com.local.mac-memory-guard.plist"

# Removal
launchctl bootout "gui/$(id -u)" "$HOME/Library/LaunchAgents/com.local.mac-memory-guard.plist"
rm "$HOME/Library/LaunchAgents/com.local.mac-memory-guard.plist" "$HOME/bin/mac-memory-guard"
```

The log defaults to `~/Library/Logs/mac-health/memory-guard.log`; every line starts with local ISO 8601 time and UTC offset. Metrics are recorded once a minute in CALM and once a second otherwise. Each level change records segment percentage, both trend projections and baseline ages, swap growth over 60 seconds, pressure streak and the active trigger flags. Decision and signal lines contain process name, pid, tier and footprint, never arguments or environment. Group decision names use the largest member. Notifications use `alerter` with a 30-minute timeout and a 30-second rate limit; at most one notifier window is open, and a newer message replaces an unanswered one. The state file defaults to `~/.local/state/mac-health/memory-guard.state` and stores pid, start seconds, start microseconds, PGID and freeze time for each process stopped by the guard. It is replaced atomically after signals. Entries must still match identity, owner, protection rules and stopped state on startup and every tick. `status` shows frozen process names. `resume --all` or `resume PGID` validates identity before SIGCONT. SIGTERM and SIGINT resume guard-frozen processes, clear state and exit.

The test-only `run --test-metrics FILE --test-root PID` switches must be used together. The root must be one of the guard's own ancestors; candidates are limited to its descendants. Test mode ignores home config and consent. An explicit temporary `--config` can lower the floors, and `--test-tick-ms N` sets the test tick. The test runner uses fake metrics and children it starts itself:

```sh
sh "$SKILL/assets/memory-guard/test.sh"
```

## Calibration and limits

Use `MODE=observe` to review level transitions and `would_freeze` / `would_kill`
records against real work, note false positives and missed candidate names, then
tune one threshold at a time. Never tune based only on a single pressure reading.
Re-run `doctor` after macOS upgrades. This is a last line of defence, not a memory
cap; it cannot guarantee time to act if the OS stops scheduling it.
