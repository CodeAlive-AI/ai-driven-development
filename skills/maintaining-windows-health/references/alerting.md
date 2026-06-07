# Active alerting

Design and operations of the `win-health-check` scheduled task — the active complement to passively watching Task Manager / Resource Monitor. Windows analog of the macOS `mac-health-check` LaunchAgent.

## Table of contents

- [Design principles](#design-principles)
- [Files (canonical paths)](#files-canonical-paths)
- [Why these specific choices](#why-these-specific-choices)
- [Install / restore on a new PC](#install--restore-on-a-new-pc)
- [Verify it works](#verify-it-works)
- [Configuration tuning](#configuration-tuning)
- [Daily operations](#daily-operations)
- [Troubleshooting](#troubleshooting)
- [Removal](#removal)

## Design principles

1. **Three CRITICAL-only triggers**, no warnings or hints:
   - Disk free below configured % (default 10).
   - Commit pressure above % AND available RAM below % (defaults 90 / 5). **Commit % is primary** — `Available MBytes` includes standby/cache, so it alone is not a low-memory signal; commit-limit exhaustion is.
   - A new crash minidump in `C:\Windows\Minidump` (immediate, no hysteresis).
2. **Hysteresis**: 3 consecutive readings before the disk/memory alert (15 min on a 5-min cadence). Kills transient spikes.
3. **Cooldown**: 30 min between repeats of the same key. Prevents storms.
4. **Calibration window**: first 7 days log-only. Observe your noise floor before alerts engage.
5. **Suppress flag**: create `%LOCALAPPDATA%\win-health\silent` to mute during heavy work — no need to unregister the task.
6. **No auto-cleanup.** The alert notifies; the human decides. (Google SRE alert-fatigue consensus.)

## Files (canonical paths)

```
%LOCALAPPDATA%\win-health\win-health-check.ps1          # the script (installed copy)
%LOCALAPPDATA%\win-health\win-health-check.config.ps1   # thresholds & switches
%LOCALAPPDATA%\win-health\silent                        # touch to suppress
%LOCALAPPDATA%\win-health\logs\health.log               # script's own log
%LOCALAPPDATA%\win-health\install_date                  # epoch of first run (calibration)
%LOCALAPPDATA%\win-health\dumps_seen                    # dedup of crash dumps seen
%LOCALAPPDATA%\win-health\counter.{disk,memory}         # hysteresis counters
%LOCALAPPDATA%\win-health\cooldown.<key>                # cooldown timestamps
Scheduled Task: \WinHealthCheck                         # per-user, interactive session
```

The skill's `assets/` directory holds the reference copies (`win-health-check.ps1`, `win-health-check.config.ps1`, `Install-WinHealthCheck.ps1`).

## Why these specific choices

| Choice | Reason |
|---|---|
| **Task runs in the INTERACTIVE user session** (principal = logged-on user, `LogonType Interactive`, `RunLevel Limited`) | This is load-bearing. A task running as **SYSTEM** (or "run whether user is logged on or not") executes fine but its toasts **silently never render** — toasts are drawn by `explorer.exe` in the user's desktop session (Session 1+), not Session 0. This is the exact Windows analog of the macOS "osascript → Script Editor" failure. `Highest` run level is unnecessary for toasts and can hand the task a non-interactive token, so use `Limited`. |
| **BurntToast for toasts** | BurntToast registers its own AppUserModelID, so the toast is attributed cleanly (not to "PowerShell") and click/activation works. Install once: `Install-Module BurntToast -Scope CurrentUser`. |
| **Native WinRT as fallback** | Zero-dependency `ToastNotificationManager`, but **requires AUMID registration** or it doesn't render / is attributed to "PowerShell" — the same pathology as the macOS osascript fallback. Documented but secondary. |
| **ntfy.sh as the headless escape hatch** | More important than on macOS: when there is **no interactive session** (locked machine, server SKU, SYSTEM task), toasts are impossible and ntfy is the only channel. `Invoke-RestMethod` works from any session. |
| **`-Once` + `-RepetitionInterval 5min`** | The only reliable way to get indefinite sub-hourly repetition via the ScheduledTasks cmdlets. |
| **`-StartWhenAvailable`** | Catch up once on wake after a missed trigger — the analog of the macOS plist's `StartCalendarInterval` coalescing (the macOS lesson was that `StartInterval` pauses during sleep). |
| **`-AllowStartIfOnBatteries -DontStopIfGoingOnBatteries`** | Default tasks are AC-only; without these a laptop on battery never checks — a silent-death mode the macOS LaunchAgent doesn't have. |
| **Minidump file poll as primary crash signal; narrow `Get-WinEvent` only as confirmation** | A broad `Get-WinEvent` over a wide window is slow and throws "no events found" as a terminating error — the analog of the macOS `log show` being too slow. Polling `C:\Windows\Minidump` is cheap. |
| **Commit % as primary memory signal** | `Available MBytes` counts reclaimable standby/cache; commit-limit exhaustion is the real OOM. |

**Modern Standby (S0ix):** on many Windows 11 laptops, wake timers are unreliable and `powercfg /a` won't show S3 — this is normal, not a fault. The task pauses during sleep and `-StartWhenAvailable` runs it once on wake. Accepted, same trade-off as macOS.

## Install / restore on a new PC

Run a **non-elevated** PowerShell as the user who should receive alerts (interactive-session principal). From the skill's `assets/`:

```powershell
cd <skill>\assets
# Installs BurntToast, copies script+config to %LOCALAPPDATA%\win-health, registers the task,
# runs once to verify:
.\Install-WinHealthCheck.ps1
```

What it does: installs the BurntToast module (CurrentUser), copies the script and a default config, then registers `\WinHealthCheck` with the interactive-session principal, 5-minute repetition, `-StartWhenAvailable`, battery-friendly settings, and a 4-minute execution limit.

To skip the module (use native WinRT or ntfy only): `.\Install-WinHealthCheck.ps1 -SkipBurntToast`.

## Verify it works

```powershell
# Synthetic disk-critical alert (no real danger): forces DiskCriticalPct=99, hysteresis=1, calibration=0
.\Install-WinHealthCheck.ps1 -Test
```

You should see a toast and an `ALERT key=disk_critical … -> delivered` line in `%LOCALAPPDATA%\win-health\logs\health.log`. Confirm the task is registered:

```powershell
Get-ScheduledTask -TaskName WinHealthCheck | Select-Object TaskName, State
Get-ScheduledTaskInfo -TaskName WinHealthCheck | Select-Object LastRunTime, LastTaskResult, NextRunTime
```

## Configuration tuning

Edit `%LOCALAPPDATA%\win-health\win-health-check.config.ps1`:

| Variable | Default | When to change |
|---|---|---|
| `$DiskCriticalPct` | 10 | lower if you routinely run >90% full and accept it; raise for earlier warning |
| `$CommitCriticalPct` | 90 | the primary memory trigger; lower to 85 for earlier warning |
| `$MemFreeCriticalPct` | 5 | confirmation gate; match your normal heavy-use floor + margin |
| `$CooldownMinutes` | 30 | lower for more reminders; raise to silence repeats |
| `$HysteresisReadings` | 3 | 1 = instant; 5–6 = very stable only |
| `$CalibrationDays` | 7 | 0 to skip on a known-good restore |
| `$Notifier` | auto | `burnttoast` / `winrt` / `none` to force |
| `$NtfyUrl` | empty | `https://ntfy.sh/<long-unguessable-topic>` for phone/desktop push |
| `$DumpDir` | `%SystemRoot%\Minidump` | override only for testing |

## Daily operations

```powershell
# Is it running?
Get-ScheduledTaskInfo -TaskName WinHealthCheck | Select-Object LastRunTime, LastTaskResult

# Watch the log
Get-Content (Join-Path $env:LOCALAPPDATA 'win-health\logs\health.log') -Wait -Tail 20

# Suppress during heavy work, then re-enable
New-Item -ItemType File -Force -Path (Join-Path $env:LOCALAPPDATA 'win-health\silent')
Remove-Item (Join-Path $env:LOCALAPPDATA 'win-health\silent')

# Force a check now
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $env:LOCALAPPDATA 'win-health\win-health-check.ps1')
```

## Troubleshooting

### Task runs but no toast appears
1. **Most common:** the task is running as SYSTEM / "whether user is logged on or not". Re-run `Install-WinHealthCheck.ps1` so the principal is the interactive user (`LogonType Interactive`). Verify: `(Get-ScheduledTask WinHealthCheck).Principal`.
2. Confirm BurntToast: `Get-Module -ListAvailable BurntToast`. If absent, `Install-Module BurntToast -Scope CurrentUser`.
3. Check Settings → System → Notifications is on and Focus Assist / Do Not Disturb isn't suppressing it.
4. As a session-independent fallback, set `$NtfyUrl` and subscribe in the ntfy app.

### Toast attributed to "PowerShell"
The native WinRT fallback fired without an AUMID. Install BurntToast (it registers an AUMID) and set `$Notifier = 'burnttoast'`.

### Task never runs on a laptop
It was AC-only or paused during sleep. Re-run the installer (sets `-AllowStartIfOnBatteries`); accept that S0ix may delay the post-wake run (`-StartWhenAvailable` catches up once).

### Constant alerts during heavy work
Past calibration and your normal workload exceeds thresholds. Suppress (`silent` file), raise thresholds, or increase `$HysteresisReadings`.

### "I want phone push too"
Set `$NtfyUrl = 'https://ntfy.sh/<your-private-uuid-topic>'` (≥ 32 random chars — public topics are world-readable), subscribe in the ntfy mobile app, and test:

```powershell
Invoke-RestMethod -Method Post -Uri 'https://ntfy.sh/<topic>' -Body 'test' -Headers @{ Title='Test'; Priority='high' }
```

## Removal

```powershell
.\Install-WinHealthCheck.ps1 -Uninstall          # remove the task (keeps logs/state)
.\Install-WinHealthCheck.ps1 -Uninstall -Purge   # also delete %LOCALAPPDATA%\win-health
# Optional: Uninstall-Module BurntToast
```
