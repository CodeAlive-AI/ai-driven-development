---
name: maintaining-windows-health
description: Hands-on playbook for Windows 11 disk cleanup, dev-machine optimization, and proactive health alerting. Use when the PC is full or slow, when a BSOD / Kernel-Power 41 / crash dump / commit-memory pressure happened, when the user asks to free disk space, audit storage, set up disk/memory alerts, or restore the same monitoring on a new PC. Built around native Microsoft-supported tooling (Storage Sense, cleanmgr, DISM, pnputil, vssadmin, wevtutil, powercfg) as the safety floor, a drift-protected HTML cleanup UI, and a Task Scheduler + BurntToast alerter. Covers dev machines with heavy AI/Docker/WSL workloads. Not for general Windows support, hardware diagnostics, GPU/driver troubleshooting, antivirus/malware removal, Windows Update repair, networking, or app-specific performance problems unrelated to disk or memory pressure.
---

# Maintaining Windows 11 Health

Recovery and prevention playbook for Windows 11 disk and memory crises. A Windows port of the `maintaining-macos-health` skill: same three layers (triage → tiered recovery → automation/alerting) and the same safety invariant — **scan → JSON → user picks in a UI → apply deletes only what was picked** — but with Windows-native tooling and Windows-specific "never touch" rules. The same playbook works for routine cleanup or first-time setup on a new machine.

## Table of contents

- [When to use](#when-to-use)
- [Skill layout](#skill-layout)
- [Core mental model](#core-mental-model)
- [Standard workflows](#standard-workflows)
  - [A. "Free space NOW" (incident response)](#a-free-space-now-incident-response)
  - [B. "Set up alerting" (new machine or first time)](#b-set-up-alerting-new-machine-or-first-time)
  - [C. Alerter stopped working / making noise](#c-alerter-stopped-working--making-noise)
  - [D. "Uninstall an app cleanly"](#d-uninstall-an-app-cleanly)
- [Safety rules (non-negotiable)](#safety-rules-non-negotiable)
- [Domain quirks captured](#domain-quirks-captured)
- [Outcomes scale](#outcomes-scale)

## When to use

Trigger on any of:

- Disk free < 20 % or user complains about being out of space
- BSOD / unexpected reboot / Kernel-Power 41 / WHEA error / a new crash dump in `C:\Windows\Minidump`
- "PC is slow", commit pressure high (`% Committed Bytes In Use` > 85), pagefile growing
- User wants to set up monitoring/alerting from scratch
- Migration to a new Windows PC → restore the same alerter
- General "clean my PC" / "audit storage" / "free space" requests

## Skill layout

| File | Use for |
|---|---|
| `references/triage.md` | First 5 minutes — which signal fired (disk / commit-memory / BSOD-crash / "feels slow"), read-only snapshot |
| `references/cleanup-tiers.md` | Tiered cleanup playbook (10 tiers, low-risk → discuss-first), copy-paste-safe PowerShell blocks |
| `references/never-touch.md` | Categories that **must not** be deleted even elevated (hard-protected prefixes synced with the validator + Windows-only dangers) |
| `references/native-tools.md` | The safety floor: native Microsoft tooling, project-artifact purge marker→target map, the apply-script validator rules, third-party caveats |
| `references/alerting.md` | Full alerter design: 3 CRITICAL-only triggers, hysteresis, calibration, Task Scheduler interactive session, BurntToast + ntfy, S0ix/battery |
| `assets/win-health-check.ps1` | Production PowerShell monitor (PS 5.1 compatible) |
| `assets/win-health-check.config.ps1` | Default thresholds |
| `assets/Install-WinHealthCheck.ps1` | Registers the scheduled task in the interactive user session; `-Test` / `-Uninstall` |
| `assets/Audit-WinHealth.ps1` | Read-only preflight inventory (drives, Component Store, shadow storage, profiles, drivers, CFA, KFM, BitLocker, reparse points, dumps) |
| `assets/render-cleanup-plan.py` | Interactive HTML cleanup-plan UI. Renders categorised checkboxes from a JSON of scan findings, serves on `127.0.0.1:18347`, opens the browser, waits for the user's selection, writes it to `%TEMP%\cleanup-selection-<ts>.json`. Used by Workflow A. **Requires Python 3.** |
| `assets/apply-cleanup-selection.py` | The **only sanctioned way** to apply a cleanup selection. Reads `selected_items` from a selection JSON and executes each item's `command` via PowerShell. Windows-rewritten validator (NTFS canonicalization, deny/allow longest-prefix, provider/UNC/ADS/8.3/chaining refusal, two-tier wrappers) + operations log. Supports `--dry-run`. |
| `assets/test_validate_command.py` | Adversarial unit tests for the validator — the safety-core gate. Runs on any OS. |

Read the relevant reference before acting. Do NOT operate from memory of these files — the details are calibrated to Windows-specific failure modes and small changes break safety.

## Core mental model

1. **Native tooling is the safety floor.** Unlike macOS (Mole), Windows has no mature community safety tool — so Storage Sense / Cleanup recommendations / `cleanmgr` / DISM do the heavy lifting, and the apply-script validator is the *only* line behind project-artifact purge. Use the supported command for anything the OS maintains itself.
2. **Clean with commands, not by deleting folders.** WinSxS → DISM; Driver Store → pnputil; shadow copies → vssadmin; Event Logs → wevtutil; hiberfil → powercfg. Hand-deleting these corrupts the OS.
3. **Commit %, not "available MB", is the memory signal.** `Available MBytes` includes reclaimable standby/cache; commit-limit exhaustion is the real Windows OOM.
4. **Drift protection via the selection JSON.** The HTML UI writes exactly what the user picked; `apply-cleanup-selection.py` deletes only `selected_items`. Never hand-roll `Remove-Item` in the apply phase.
5. **Escalate conservatively.** Start zero-risk (Storage Sense, caches, Recycle Bin), only reach project artifacts, Docker/WSL VHDX, Component Store, and elevated/discuss-first tiers if needed.

## Standard workflows

### A. "Free space NOW" (incident response)

1. **Triage** — read `references/triage.md`, identify which signal fired and how urgent. Run `assets/Audit-WinHealth.ps1` (read-only) for the preflight inventory (drives, Component Store, shadow storage, drivers, **CFA / OneDrive KFM / BitLocker / reparse points**).
2. **Snapshot baseline** — record free GB on the target drive.
3. **Run all scans, don't delete yet** — work the tiers in `references/cleanup-tiers.md` in *inventory* mode (list candidates, sizes, ages), including the large-file visibility pass. Capture everything before opening the browser; deletion comes only after the user picks via the UI. The cleanup UI should be a single final questionnaire containing safe cleanup candidates, protected/discuss-first items, and large suspicious user/workload files together, not a sequence of separate UI rounds.
4. **Python gate** — the cleanup UI needs Python 3. Check for a real interpreter (`py -3 --version`, or a `python.exe` that isn't the Microsoft Store alias). **If Python is missing, ask the user for permission to install it** (`winget install Python.Python.3.12`), then continue. Do not silently skip the UI.
5. **Resolve unknown items before building JSON** — for every candidate > 500 MB you cannot explain in one sentence (unfamiliar app/folder, vendor cache, VM/VHDX, model weights), research it first: check `references/never-touch.md`, then delegate a quick lookup to the `web-searcher` subagent ("what is `<path>` on Windows 11, safe to delete in 2026"). Write a concrete `description` (1–3 sentences in the user's language) into the item. **Never show vague placeholders like "unknown".**
6. **Show large-but-not-safe items too** — any explainable item > 500 MB that is user-owned or workload-owned but not a safe cache must still appear in the same final UI, normally `protected: true`, `default_selected: false`, with a concrete `warning`. Examples: old `.7z/.zip/.iso` archives, `.gguf`/`.safetensors` model weights, project/game assets, app diagnostic dumps, profiler snapshots, synced-folder media, and VHDX files. Visibility is required because only the user can know whether these are still needed. Do not include hard-protected system internals as bare-delete candidates; show them only through supported tools, or omit deletion entirely if no supported action exists.
7. **Build one data JSON** — every candidate becomes a structured `item` (id, label, path, size_bytes, age_days, kind, **PowerShell `command`**, mandatory `description`, optional `protected` + `warning`). Use the schema in `assets/render-cleanup-plan.py`. Irreversible-tool commands (DISM `/ResetBase`, `vssadmin delete`, `wevtutil cl`, `pnputil /delete-driver`, `powercfg /h off`) should be marked `protected: true`. Do not open the UI until this unified JSON contains both safe default-selected items and protected unchecked items.
8. **Render and open the cleanup UI**:
   ```powershell
   python3 <skill>\assets\render-cleanup-plan.py %TEMP%\cleanup-data-<ts>.json
   ```
   It serves on `127.0.0.1:18347`, opens the browser, and **blocks** until Submit/Cancel. On submit it writes `%TEMP%\cleanup-selection-<ts>.json`. Tell the user out loud: "браузер открыт — поставь галочки, нажми Submit, потом пингани меня." Then **stop and wait**.
9. **After the user pings** — read the selection JSON, render their choices back in chat (categories, item list, total GB, any protected overrides flagged), and **ask one explicit confirmation** before deleting.
10. **Apply via the helper — never hand-rolled `Remove-Item`**:
   ```powershell
   python3 <skill>\assets\apply-cleanup-selection.py %TEMP%\cleanup-selection-<ts>.json
   #   add --scan-root D:\projects to allow bare deletes on an external dev drive
   ```
   It reads `selected_items`, validates each `command` (NTFS canonicalization, deny/allow longest-prefix, provider/UNC/ADS/8.3/chaining refusal), skips protected items not in `protected_overrides`, runs each via `powershell.exe`, and logs to `%LOCALAPPDATA%\win-health\operations.log`. `--dry-run` previews. **The selection JSON is the single source of truth.**
11. **Post-check** — report the free-space delta, then `Dism /Online /Cleanup-Image /CheckHealth` + `sfc /scannow` to confirm nothing was broken. Stop at the goal.

Hard-protected items (per `references/never-touch.md`) must always appear in the UI with `"protected": true` + a concrete `warning` — the UI dims them and requires a per-item confirm before they can be checked. Never omit a protected item user data depends on; visibility teaches the surrounding risk.

### B. "Set up alerting" (new machine or first time)

Run a **non-elevated** PowerShell as the user who should receive alerts (interactive session — required for toasts):

```powershell
cd <skill>\assets
.\Install-WinHealthCheck.ps1     # installs BurntToast, copies script+config, registers the task, runs once
```

Then read `references/alerting.md` for tuning. The task is registered in the interactive user session (NOT SYSTEM — that silently swallows toasts), every 5 minutes, `-StartWhenAvailable`, battery-friendly. The first 7-day calibration window is silent (logs only). Verify with `.\Install-WinHealthCheck.ps1 -Test`.

### C. Alerter stopped working / making noise

Read `references/alerting.md` § Troubleshooting. Common causes:
- Task running as SYSTEM / "whether user is logged on or not" → toasts silently never render. Re-run the installer (interactive principal).
- BurntToast not installed → toast attributed to "PowerShell" or absent. `Install-Module BurntToast -Scope CurrentUser`.
- Laptop never checks → was AC-only / paused in sleep. Re-run installer (battery flags + `-StartWhenAvailable`).
- Constant alerts during heavy work → create `%LOCALAPPDATA%\win-health\silent`, raise thresholds, or increase hysteresis.

### D. "Uninstall an app cleanly"

Prefer `winget uninstall --id <App.Id>` (clean, supported). For apps with stubborn leftovers, BCUninstaller (review the leftover list) is the dev-friendly option. Never hand-delete `Program Files` install dirs or registry keys to "remove" an app — that orphans the MSI/uninstall state. Always confirm before removing user data folders.

## Safety rules (non-negotiable)

1. **Never delete without dry-run + user confirmation** for any tier ≥ 5 or any elevated operation.
2. **Never bypass `references/never-touch.md`** — even if the user explicitly asks. Push back, explain the consequence.
3. **Clean with commands, not folders.** WinSxS via DISM, Driver Store via pnputil, shadows via vssadmin, logs via wevtutil (export before clear), hiberfil via powercfg. Never `Remove-Item` these.
4. **The registry is never a cleanup target.** No registry cleaners (Microsoft-unsupported). The validator refuses registry-provider deletes.
5. **Apply phase reads only the selection JSON.** Never hand-roll `Remove-Item` or hard-code paths from the earlier scan when applying — that's how you delete items the user unchecked. Use `assets/apply-cleanup-selection.py`, which iterates `selected_items` only.
6. **`Remove-Item` is permanent** (no Recycle Bin) and recursive deletes can escape through junctions — always `-LiteralPath`, never recurse a reparse point. Prefer move-to-quarantine when the user is unsure.
7. **No auto-cleanup tied to alerts.** Alerts notify; the human decides.
8. **Keep crash dumps until triaged** — they're forensic evidence, not cleanup.

## Domain quirks captured

- **SYSTEM session can't show toasts.** A scheduled task as SYSTEM executes but its toasts silently no-op (Session 0 has no desktop). Register the task in the interactive user session — the Windows analog of the macOS "osascript → Script Editor" trap.
- **`Remove-Item -Recurse` follows junctions** and can delete the target's contents — the classic data-loss bug. Dev trees are full of junctions (npm/pnpm store, Docker, WSL). Use `-LiteralPath`; never recurse a `FILE_ATTRIBUTE_REPARSE_POINT`.
- **`Remove-Item` bypasses the Recycle Bin** — deletion is immediate and permanent, unlike dragging to the bin.
- **OneDrive KFM** redirects Desktop/Documents/Pictures into OneDrive — deleting there propagates to all devices. Files On-Demand placeholders (`RECALL_ON_DATA_ACCESS`/`OFFLINE`) are cloud originals; deleting the stub deletes the cloud file.
- **Controlled Folder Access** blocks deletes in Documents/Pictures/Desktop with Access Denied from Defender — distinguish from a real error.
- **`Available MBytes` includes standby/cache** — high "available" doesn't mean healthy; commit-limit exhaustion is the real OOM signal.
- **`pagefile.sys` and `swapfile.sys` are two different files**; `C:\Windows\Installer` + `Package Cache` break MSI repair if deleted; **Prefetch** should not be cleaned (myth).
- **Modern Standby (S0ix)** makes wake timers unreliable and hides S3 — normal, not a fault. The task pauses in sleep and catches up on wake via `-StartWhenAvailable`.
- **General rule**: if you can't describe a folder in one sentence (especially > 500 MB), don't guess — delegate a `web-searcher` lookup before writing the item's `description`. If you can describe it but it may be user data, still show it in the single final cleanup UI as protected and unchecked by default.

## Outcomes scale

A representative recovery on a dev machine that hit ~8 % free under heavy AI/Docker/WSL load:

- Largest single contribution: project build artifacts (`node_modules`, `bin`/`obj`, `target`, `.next`) via Tier 7 purge.
- WSL2 / Docker `*.vhdx` compaction (not deletion): often 10–40 GB reclaimed.
- Component Store cleanup via DISM after many cumulative updates: a few GB.
- Package-manager caches (npm/pnpm/NuGet/pip/cargo/gradle): a few GB.
- `Downloads` review (old installers, ISOs): variable, often 10–20 GB.
- Elevated tier (Windows.old after rollback check, Delivery Optimization, exported+cleared logs): variable.

Active alerter installed with a 7-day calibration window; verified via the synthetic disk-trigger test before going live. Numbers scale with workload and disk size — light users see less; heavy AI/Docker/WSL/IDE users see more.
