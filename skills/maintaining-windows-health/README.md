# maintaining-windows-health

A hands-on playbook skill for **Windows 11** disk cleanup, dev-machine optimization, and proactive health alerting. It is the Windows port of [`maintaining-macos-health`](../maintaining-macos-health/) — same three-layer architecture and the same drift-protection safety invariant, rebuilt around Windows-native tooling.

> **Recovery and prevention**, not blind deletion. The skill follows a managed cycle: inventory → classify → delete only with Microsoft-supported tools → verify integrity → keep a rollback path.

## What it does

Three layers, mirroring the macOS skill:

1. **Triage** (`references/triage.md`) — classify which signal fired: disk-driven, commit-memory-driven, BSOD/crash, or "feels slow" — with a read-only PowerShell snapshot.
2. **Recovery** (`references/cleanup-tiers.md`, `never-touch.md`, `native-tools.md`) — a 10-tier, risk-ordered cleanup playbook (Storage Sense → discuss-first), a hard blacklist of what never to delete, and the native-tooling safety floor + project-artifact purge map.
3. **Automation / alerting** (`references/alerting.md`, `assets/*.ps1`) — a drift-protected HTML cleanup UI plus a Task Scheduler + BurntToast alerter (3 CRITICAL-only triggers, hysteresis, calibration window).

## The safety invariant

```
scan  →  build JSON  →  user picks in the HTML UI  →  selection JSON  →  apply deletes ONLY selected_items
```

`assets/apply-cleanup-selection.py` is the only sanctioned way to apply a cleanup. It never hand-rolls `Remove-Item`; it reads the user's picks from the selection JSON and validates every command before running it. The validator is a **Windows rewrite** (not a translation) of the macOS one, because NTFS + PowerShell offer several ways to spell a protected path that a naive check misses:

- NTFS path canonicalization (separator unification, `..` collapse, trailing dot/space stripping) like Win32 `GetFullPath`
- refusal of UNC/device paths (`\\?\`, `\\.\`), 8.3 short names (`PROGRA~1`), Alternate Data Streams, and non-filesystem providers (`HKLM:`, `Env:`)
- a **longest-prefix-wins** allow/deny classifier so carve-outs resolve correctly (`C:\Windows` denied, but `C:\Windows\Temp` allowed; `C:\Users\me` allowed, but `C:\Users\me\.ssh` denied)
- a **two-tier wrapper** model: cache tools (npm/docker/dotnet…) are trusted; irreversible tools (`vssadmin delete`, DISM `/ResetBase`, `wevtutil cl`, `pnputil /delete-driver`, `powercfg /h off`) require an explicit protected-override
- a refusal of command chaining/injection metacharacters (`; | & \` $( :: > <`)

## Quick start

Read-only preflight audit:

```powershell
.\assets\Audit-WinHealth.ps1     # drives, Component Store, shadow storage, drivers, CFA, KFM, BitLocker, reparse points, dumps
```

Interactive cleanup (requires Python 3 for the HTML UI):

```powershell
python3 .\assets\render-cleanup-plan.py %TEMP%\cleanup-data.json   # opens the picker, writes the selection JSON
python3 .\assets\apply-cleanup-selection.py %TEMP%\cleanup-selection-<ts>.json   # applies only what was picked
```

Install the alerter (non-elevated, interactive session — required for toasts):

```powershell
.\assets\Install-WinHealthCheck.ps1        # installs BurntToast, registers the 5-min task, runs once
.\assets\Install-WinHealthCheck.ps1 -Test  # synthetic disk alert to confirm the toast pipeline
```

## File map

```
SKILL.md                         agent entry point (workflows A–D, safety rules, quirks)
references/
  triage.md                      which signal fired (read-only snapshot)
  cleanup-tiers.md               10 risk-ordered tiers, PowerShell blocks
  never-touch.md                 hard blacklist + Windows-only dangers
  native-tools.md                safety floor, purge map, validator rules, 3rd-party caveats
  alerting.md                    Task Scheduler + BurntToast + ntfy alerter design
assets/
  win-health-check.ps1           the monitor (PS 5.1 compatible)
  win-health-check.config.ps1    thresholds
  Install-WinHealthCheck.ps1     registers the task (interactive session); -Test / -Uninstall
  Audit-WinHealth.ps1            read-only preflight inventory
  render-cleanup-plan.py         HTML cleanup UI (cross-platform, Python 3)
  apply-cleanup-selection.py     the only sanctioned apply path (Windows validator)
  test_validate_command.py       adversarial validator tests (safety-core gate)
```

## Key Windows-specific guardrails

- **Toasts need an interactive session.** The scheduled task is registered as the logged-on user (`LogonType Interactive`), never SYSTEM — a SYSTEM task's toasts silently no-op.
- **`Remove-Item` is permanent** (no Recycle Bin) and **recursive deletes can escape through junctions** — always `-LiteralPath`, never recurse a reparse point.
- **OneDrive KFM / Files On-Demand** — deleting redirected/placeholder files propagates to the cloud and every device.
- **Clean with commands, not folders** — WinSxS via DISM, Driver Store via pnputil, shadows via vssadmin, logs via wevtutil, hiberfil via powercfg. The registry is never a cleanup target.
- **Commit %, not "available MB", is the memory signal** — `Available MBytes` includes reclaimable standby/cache.

## Verification status

Authored and statically verified on a macOS machine (no Windows runtime available):

- ✅ **Verified here:** PowerShell AST parse of all `.ps1` (via `pwsh`), `py_compile` of both Python scripts, and the adversarial validator suite (`test_validate_command.py`) — pure NTFS string logic that runs on any OS and is the safety-core gate.
- ⚠️ **Requires a Windows smoke-test before fully trusting:** real NTFS behavior of `GetFullPath`/8.3/ADS/reparse resolution, toast rendering and AUMID attribution, SYSTEM-vs-interactive session behavior, Task Scheduler registration semantics on S0ix/battery, and the exact output of DISM/vssadmin/wevtutil/pnputil. Gate the alerter and apply-on-real-paths behind this smoke-test.

## Credits & sources

Built on official Microsoft Learn guidance for Storage Sense, `cleanmgr`, DISM (WinSxS), `pnputil`, `vssadmin`, `wevtutil`, `powercfg`, `Get-WinEvent`, Task Scheduler, and BurntToast, plus the macOS sibling's incident-validated architecture. See `references/` for inline citations of the behavior each rule depends on.
