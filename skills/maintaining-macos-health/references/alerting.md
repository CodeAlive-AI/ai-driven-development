# Active alerting

Design and operations of the `mac-health-check` LaunchAgent — the active complement to passive Stats menubar monitoring. It covers critical disk/memory failure signals and persistent CPU anomalies on a developer workstation.

## Table of contents

- [Design principles](#design-principles)
- [Files (canonical paths)](#files-canonical-paths)
- [Why these specific tools](#why-these-specific-tools-current-status)
- [Install / restore on a new Mac](#install--restore-on-a-new-mac)
- [Configuration tuning](#configuration-tuning)
- [Daily operations](#daily-operations)
- [Troubleshooting](#troubleshooting)
- [Removal](#removal-if-user-wants-out)
- [When to re-validate (after macOS updates)](#when-to-re-validate-after-macos-updates)

## Design principles

1. **Three original CRITICAL resource triggers**:
   - Disk free below configured % (default 10 %)
   - Memory pressure Critical AND swap > 8 GB
   - New `JetsamEvent-*.ips` containing `vm-compressor-space-shortage`
2. **Two CPU signals with different severity**:
   - Whole-system CPU busy >= 90 % for 3 readings: critical, audible.
   - One process >= 80 % of a core for 12 readings (~1 h), or >= 40 % for 72 readings (~6 h): silent advisory.
3. **Hysteresis**: consecutive readings eliminate transient spikes. A gap > 15 min resets pending/recovery counters so sleep cannot create a false streak.
4. **Incident lifecycle for CPU**: notify once, remain open, recover only after 3 readings below the recovery threshold, then rearm. No periodic CPU reminders.
5. **Cooldown**: 30 min between repeats of the original disk/memory/Jetsam alerts.
6. **Calibration window**: first 7 days log only for the original resource sensors. CPU starts immediately with conservative defaults and silent per-process advisories.
7. **Suppress-flag**: `touch ~/.config/mac-health/silent` disables all alerts during heavy work. No need to unload the LaunchAgent.
8. **No automatic cleanup or process termination**. CPU notifications expose investigation and stop actions, but the human must select them. Investigation is read-only; stopping is identity-checked, confirm-first, and SIGTERM-first.

This design follows Google SRE alert-fatigue principles plus practitioner consensus from incident.io and Netdata Academy.

## Files (canonical paths)

```
~/bin/mac-health-check                              # the script
~/bin/mac-health-action                             # waits for action clicks and dispatches them
~/.config/mac-health/config.sh                      # thresholds & switches
~/.config/mac-health/silent                         # touch to suppress (manual)
~/Library/LaunchAgents/com.local.mac-health-check.plist
~/Library/Logs/mac-health/health.log                # script's own log
~/Library/Logs/mac-health/launchd.{out,err}.log     # captured stdio from launchd
~/.local/state/mac-health/install_date              # epoch of first run (for calibration)
~/.local/state/mac-health/jetsam_seen               # dedup of jetsam files we've seen
~/.local/state/mac-health/counter.{disk,memory}     # hysteresis counters
~/.local/state/mac-health/cooldown.<key>            # cooldown timestamps
~/.local/state/mac-health/cpu_system_state          # system CPU incident lifecycle
~/.local/state/mac-health/cpu_process.<pid>          # per-PID counters + executable identity
~/Library/Logs/mac-health/cpu-incidents/             # safe top-process snapshots, 30-day retention
```

The skill's `assets/` directory holds the reference copies of the script, plist, and config.

## Why these specific tools (current status)

| Choice | Reason |
|---|---|
| `alerter` (vjeantet/alerter) | `terminal-notifier` is **dead** (last release 2019-11) and silently fails on Apple Silicon Sequoia/Tahoe (issue #312). `osascript display notification` from launchd attributes to "Script Editor" and is unreliable. `alerter` is Swift, actively maintained, works in launchd context. |
| Separate `mac-health-action` process | `alerter` waits for a response. The periodic check launches this small handler in the background, so launchd checks still finish quickly while the notification remains actionable. Multiple alerter actions appear under one `Actions…` dropdown. |
| Claude desktop deep link | Anthropic documents `claude://code/new?q=...&folder=...`; the composer is prefilled and the user confirms the folder and sends. Codex currently has no documented new-session deep link with a prompt, so its interactive read-only CLI is the reliable path. |
| `StartCalendarInterval` (12 entries) | `StartInterval` clock pauses during sleep on laptops (radar 6630231); missed intervals never coalesce. `StartCalendarInterval` fires once on wake regardless of how many minute marks were missed. |
| `EnvironmentVariables.PATH` in plist | LaunchAgent default PATH is `/usr/bin:/bin:/usr/sbin:/sbin` — `/opt/homebrew/bin` (where alerter lives) is absent. Without setting PATH, `command -v alerter` fails inside the script. |
| Hardcoded `/bin/bash` interpreter | `#!/usr/bin/env bash` would resolve to /bin/bash 3.2 anyway under launchd, since EnvironmentVariables apply AFTER shebang lookup. Better to be explicit. |
| File polling for JetsamEvent (not `log show`) | `log show --last 6m` takes 30+ seconds even with `--start` on a busy machine. File polling has async-write latency but on a 5-min cadence it's fine. |
| `/Library/Logs/DiagnosticReports/` not `~/Library/Logs/DiagnosticReports/` | JetsamEvent files are written by kernel to system-wide path. The user-level dir does not always exist. |
| `ps` for process CPU | macOS reports a decaying average over up to one minute. That rejects momentary scheduler noise while remaining cheap (~30 ms on the validated machine). `%CPU` is relative to one logical core and may exceed 100. Only PID, PPID, elapsed time, and executable identity are collected; arguments can contain secrets and are never read or logged. The PPID/executable chain lets an alert attribute helpers to their owning `.app`. |
| Second `iostat` sample for system CPU | Gives a true 0–100 % whole-machine busy value with a one-second interval and negligible CPU overhead. A two-sample `top` run took ~2.2 s and created its own visible load, so it is not used by the daemon. |

## Install / restore on a new Mac

Standard install. Set `SKILL` to wherever this skill is installed (default below assumes the user-level Claude Code skills directory; adjust if you installed it elsewhere):

```bash
SKILL=$HOME/.claude/skills/maintaining-macos-health
mkdir -p ~/bin ~/.config/mac-health ~/Library/Logs/mac-health ~/.local/state/mac-health

cp "$SKILL/assets/mac-health-check"          ~/bin/
cp "$SKILL/assets/mac-health-action"         ~/bin/
cp "$SKILL/assets/config.sh"                 ~/.config/mac-health/
# The plist contains __HOME__ placeholders — substitute the user's actual $HOME
# (launchd does not expand ~ or env vars in plist paths)
sed "s|__HOME__|$HOME|g" "$SKILL/assets/com.local.mac-health-check.plist" \
  > ~/Library/LaunchAgents/com.local.mac-health-check.plist
chmod +x ~/bin/mac-health-check ~/bin/mac-health-action

# Notifier
brew install vjeantet/tap/alerter

# First-launch permission grant (otherwise notifications go nowhere)
alerter --message "mac-health-check installation test" --title "First launch" --timeout 3
# A macOS dialog should ask permission. Accept. Then check System Settings → Notifications → alerter and ensure Alert style is set.

# Passive monitor (recommended companion)
brew install --cask stats
open -a Stats

# Activate
launchctl load -w ~/Library/LaunchAgents/com.local.mac-health-check.plist
launchctl list | grep mac-health    # should show PID and exit code 0
sleep 6
tail -10 ~/Library/Logs/mac-health/health.log
```

Verify it works:

```bash
# Force a synthetic disk-trigger using an override config (no real harm)
TMP=/tmp/mh-test.sh
cat > "$TMP" <<EOF
DISK_VOLUME=/System/Volumes/Data
DISK_CRITICAL_PCT=99
SWAP_CRITICAL_GB=999
MEM_FREE_CRITICAL_PCT=0
COOLDOWN_MINUTES=30
HYSTERESIS_READINGS=1
CALIBRATION_DAYS=0
SUPPRESS_FILE=/dev/null/never
NTFY_URL=
NOTIFIER=alerter
JETSAM_DIR=/tmp/no-such-dir
EOF
rm -f ~/.local/state/mac-health/counter.disk ~/.local/state/mac-health/cooldown.disk_critical
MAC_HEALTH_CONFIG="$TMP" /bin/bash ~/bin/mac-health-check
tail -8 ~/Library/Logs/mac-health/health.log
rm -f "$TMP" ~/.local/state/mac-health/counter.disk ~/.local/state/mac-health/cooldown.disk_critical
```

You should see "ALERT key=disk_critical ... -> delivered via alerter" and a notification in Notification Center.

Run the CPU lifecycle tests from the skill checkout before installing an update:

```bash
/bin/bash tests/test-cpu-monitor.sh
/bin/bash tests/test-cpu-actions.sh
```

The tests use isolated log/state directories, fixture `ps`/`iostat` data, and dry-run action hooks. They cover pending -> firing, single-notification deduplication, recovery, rearm, app attribution (SourceCraft, Docker, Playwriter), incident permissions/metadata, read-only prompts, desktop/CLI routing, system target selection, PID identity checks, and a stop dry-run against a test-owned process.

## Configuration tuning

Edit `~/.config/mac-health/config.sh`:

| Variable | Default | When to change |
|---|---|---|
| `DISK_CRITICAL_PCT` | 10 | Lower if you regularly run >90 % full and accept the risk; raise if you want earlier warning |
| `SWAP_CRITICAL_GB` | 8 | On 16 GB machines lower to 5; on 32+ GB raise to 12 |
| `MEM_FREE_CRITICAL_PCT` | 10 | Match what you observe during normal heavy use + 5 % margin |
| `COOLDOWN_MINUTES` | 30 | Lower to 10 if you want more reminders; raise to 60 to silence repeats |
| `HYSTERESIS_READINGS` | 3 | 1 for instant trigger, 5 for very stable conditions |
| `CALIBRATION_DAYS` | 7 | Set to 0 to skip calibration after restore on a known-good machine |
| `NOTIFIER` | auto | Force `alerter` / `terminal-notifier` / `osascript` / `none` for testing |
| `NTFY_URL` | empty | Set to `https://ntfy.sh/<unguessable-uuid>` for phone push (subscribe in ntfy mobile app) |
| `JETSAM_DIR` | /Library/Logs/DiagnosticReports | Override only for testing |

CPU defaults are intentionally conservative for developer machines:

| Variable | Default | Meaning |
|---|---:|---|
| `CPU_ENABLED` | 1 | Set to 0 to disable CPU collection and alerts |
| `CPU_SYSTEM_BUSY_PCT` | 90 | Whole-machine critical threshold, 0–100 % across all cores |
| `CPU_SYSTEM_BUSY_READINGS` | 3 | 15 minutes before the audible system alert |
| `CPU_PROCESS_HOT_PCT` | 80 | Per-process threshold relative to one core |
| `CPU_PROCESS_HOT_READINGS` | 12 | About one hour before a silent advisory |
| `CPU_PROCESS_LEAK_PCT` | 40 | Lower threshold for a slow, persistent burner |
| `CPU_PROCESS_LEAK_READINGS` | 72 | About six hours before a silent advisory |
| `CPU_PROCESS_RECOVERY_PCT` | 20 | Process must fall below this to begin recovery |
| `CPU_SYSTEM_RECOVERY_PCT` | 70 | System incident begins recovery below this |
| `CPU_RECOVERY_READINGS` | 3 | Consecutive recovery readings before rearm |
| `CPU_MAX_SAMPLE_GAP_MINUTES` | 15 | Longer gap resets consecutive counters |
| `CPU_IGNORE_REGEX` | system/monitor helpers | Executable basenames excluded as primary advisory culprits; still shown in diagnostics |
| `CPU_LOG_TOP_N` | 5 | Process count in each routine CPU log line |
| `CPU_ALERT_TOP_N` | 3 | App/process pairs shown in a notification |
| `CPU_INCIDENT_RETENTION_DAYS` | 30 | Retention for safe incident snapshots |
| `CPU_ACTIONS_ENABLED` | 1 | Add the `Actions…` menu to local CPU notifications |
| `CPU_PREFER_DESKTOP_APPS` | 1 | Prefer a documented desktop prompt handoff when available (currently Claude) |
| `CPU_STOP_ACTION_ENABLED` | 1 | Show `Stop Process…`; it never bypasses revalidation or confirmation |
| `CPU_STOP_GRACE_SECONDS` | 10 | Wait after SIGTERM before offering a separately confirmed SIGKILL |

CPU incident states are `normal -> pending -> firing -> recovering -> normal`. A firing incident never emits periodic repeats. Process exit resolves it silently. PID reuse is guarded by a hash of the executable path.

Notification attribution is deliberately evidence-based and secret-safe. The monitor checks known local tool paths (Playwriter, SourceCraft, Logi Options+), then walks up to 12 PPID links looking for the outer `.app` bundle and reads only its `CFBundleDisplayName`/`CFBundleName`. If no app can be established, it falls back to the executable name (or `OpenCode` for its cache path). A process alert names the app in its title and includes both `App` and `Process` in its body; system saturation shows the top configured number of `App/Process` pairs.

### CPU notification actions

`alerter` renders multiple actions as one `Actions…` dropdown:

1. **Investigate in Codex** — opens an interactive Codex CLI in `--sandbox read-only` with approvals disabled. The prompt asks for fresh CPU sampling, process ancestry, owning-app/CWD attribution, safe logs, evidence/inference separation, and forbids writes, kills, argv/environment/credential inspection.
2. **Investigate in Claude** — prefers Anthropic's documented `claude://code/new` desktop deep link, which prefills the prompt and asks the user to confirm the folder. If unavailable, it opens an interactive Claude CLI in `--permission-mode plan`.
3. **Stop Process…** — for a process alert, targets that exact PID; for system saturation, first asks the user to choose one of the captured top processes. It then verifies the PID still maps to the captured executable hash, belongs to the current user, and remains above the recovery threshold. A modal confirmation precedes SIGTERM. SIGKILL is offered only if it survives the configured grace period and receives a second confirmation and identity check.

Incident files and generated prompt/launcher files are mode `600` inside a mode `700` directory. Process arguments, environment variables, shell startup files, keychains, and credential stores are never collected. Phone pushes remain informational: ntfy actions cannot safely control a local Mac process.

## Daily operations

```bash
# Check it's running
launchctl list | grep mac-health
# (PID column non-dash means actively running; non-zero exit code means recent failure)

# Watch the log
tail -f ~/Library/Logs/mac-health/health.log

# Suppress alerts during heavy work
touch ~/.config/mac-health/silent
# ... work ...
rm ~/.config/mac-health/silent

# Force a check now (bypasses calendar)
/bin/bash ~/bin/mac-health-check

# Review CPU history and captured incident snapshots
grep ' cpu ' ~/Library/Logs/mac-health/health.log | tail -20
ls -lt ~/Library/Logs/mac-health/cpu-incidents/

# Disable only interactive CPU actions (monitoring continues)
# Set CPU_ACTIONS_ENABLED=0 in ~/.config/mac-health/config.sh
```

## Troubleshooting

### LaunchAgent not running

```bash
launchctl list | grep mac-health
# If absent:
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.local.mac-health-check.plist
# Or:
launchctl load -w ~/Library/LaunchAgents/com.local.mac-health-check.plist

# Check launchd's stderr capture
cat ~/Library/Logs/mac-health/launchd.err.log
```

### Notifications go nowhere

1. Run `alerter --message test --title "permission test" --timeout 3` interactively in Terminal. macOS should prompt.
2. System Settings → Notifications → alerter — set to Alerts (not Banners), enable sound and Notification Center.
3. Confirm `which alerter` returns `/opt/homebrew/bin/alerter`.
4. Confirm plist's `EnvironmentVariables.PATH` includes `/opt/homebrew/bin`.

### Notifications attributed to "Script Editor"

osascript fallback fired instead of alerter. Either alerter wasn't on PATH, or it failed. Check:
- `cat ~/.config/mac-health/config.sh` — confirm `NOTIFIER=auto` (not `osascript`)
- Run `command -v alerter` in the script context: temporarily edit the script, add `command -v alerter >> ~/Library/Logs/mac-health/health.log` near the top.

### Constant alerts during heavy dev work

You're past the calibration window and your normal workload exceeds the thresholds. Either:
- Suppress when needed: `touch ~/.config/mac-health/silent`
- Raise thresholds in config.sh
- Increase `HYSTERESIS_READINGS` to 5 or 6

For CPU specifically, tune `CPU_PROCESS_HOT_READINGS` or `CPU_PROCESS_LEAK_READINGS`, or add an executable basename to `CPU_IGNORE_REGEX`. Do not ignore generic runtimes such as `node`, `python`, or `java` by default: a stuck tool hosted by those runtimes is still useful evidence. CPU advisories have no sound and fire only once per incident.

### "I want phone push too"

Set `NTFY_URL=https://ntfy.sh/<your-private-uuid-topic>` in config.sh. Pick a long unguessable string (at least 32 chars) — ntfy.sh public topics are world-readable. Subscribe to that topic in the ntfy mobile app. Test:

```bash
curl -d "test push from mac-health" \
  -H "Title: Test" \
  -H "Priority: high" \
  https://ntfy.sh/<your-topic>
```

For sensitive use, self-host ntfy. The van Werkhoven blog (2025) has the canonical walkthrough.

## Removal (if user wants out)

```bash
launchctl unload ~/Library/LaunchAgents/com.local.mac-health-check.plist
rm ~/Library/LaunchAgents/com.local.mac-health-check.plist
rm ~/bin/mac-health-check
rm -rf ~/.config/mac-health ~/.local/state/mac-health ~/Library/Logs/mac-health
brew uninstall alerter   # optional
brew uninstall --cask stats   # optional
```

Verify clean:

```bash
launchctl list | grep mac-health   # should be empty
ls ~/bin/mac-health-check 2>&1     # No such file
```

## When to re-validate (after macOS updates)

- After every major macOS upgrade (.0 release): re-test the synthetic trigger. TCC permissions sometimes reset, alerter binary may need re-grant.
- If notifications go quiet for > 7 days without explanation: trigger a manual run, check launchd.err.log, re-grant alerter permission.
