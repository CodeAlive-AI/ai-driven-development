# Triage — first 5 minutes

When the user reports trouble, or an alert fires, identify which signal class fired before doing anything destructive. The right response differs. Run the snapshot read-only; nothing here deletes anything.

## Table of contents

- [Quick state snapshot](#quick-state-snapshot-always-run-first)
- [Signal classification](#signal-classification)
  - [A. Disk-driven](#a-disk-driven-most-common)
  - [B. Memory / commit-driven](#b-memory--commit-driven)
  - [C. BSOD / crash / unexpected shutdown](#c-bsod--crash--unexpected-shutdown)
  - [D. New crash dump appeared](#d-new-crash-dump-appeared)
  - [E. "PC just feels slow"](#e-pc-just-feels-slow)
- [Decision tree](#decision-tree)
- [What to NOT do at triage](#what-to-not-do-at-triage)

## Quick state snapshot (always run first)

Run in an **elevated** PowerShell (`Get-Counter` memory objects, `Get-WinEvent System`, and DISM need admin). Everything here is read-only.

```powershell
Write-Host "=== Disk ==="
Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' |
  Select-Object DeviceID,
    @{N='SizeGB';E={[math]::Round($_.Size/1GB,1)}},
    @{N='FreeGB';E={[math]::Round($_.FreeSpace/1GB,1)}},
    @{N='FreePct';E={[math]::Round($_.FreeSpace/$_.Size*100,1)}} | Format-Table -Auto

Write-Host "=== Memory / commit ==="
$os = Get-CimInstance Win32_OperatingSystem
"RAM free %  = {0}" -f [math]::Round($os.FreePhysicalMemory/$os.TotalVisibleMemorySize*100,1)
Get-Counter '\Memory\Available MBytes','\Memory\% Committed Bytes In Use','\Paging File(_Total)\% Usage' -EA SilentlyContinue |
  Select-Object -Expand CounterSamples | Select-Object Path, CookedValue | Format-Table -Auto

Write-Host "=== Recent crashes (7d) ==="
Get-WinEvent -FilterHashtable @{LogName='System'; Id=41,1001,6008; StartTime=(Get-Date).AddDays(-7)} -EA SilentlyContinue |
  Select-Object TimeCreated, Id, ProviderName | Sort-Object TimeCreated -Desc | Select-Object -First 10 | Format-Table -Auto
Get-ChildItem "$env:SystemRoot\Minidump" -Filter *.dmp -EA SilentlyContinue |
  Sort-Object LastWriteTime -Desc | Select-Object -First 5 Name, LastWriteTime

Write-Host "=== Top working-set processes ==="
Get-Process | Sort-Object WS -Desc | Select-Object -First 15 Name, Id,
  @{N='WS_MB';E={[math]::Round($_.WS/1MB)}}, @{N='CPU';E={[math]::Round($_.CPU)}} | Format-Table -Auto

Write-Host "=== Health-check log if installed ==="
$hl = Join-Path $env:LOCALAPPDATA 'win-health\logs\health.log'
if (Test-Path $hl) { Get-Content $hl -Tail 20 }
```

## Signal classification

### A. Disk-driven (most common)

Symptoms: low free space, "out of space", install/update failures.

- **free % < 10** → CRITICAL. Run Tier 1–6 from `cleanup-tiers.md` immediately.
- **free % 10–20** → HIGH. Run Tier 1–3, propose Tier 4–6. Usually manageable.
- **free % > 20** → user-perception issue. Audit with a tree sizer (WizTree CLI export, or `Get-ChildItem $env:USERPROFILE -Directory | %{ ... }`) and target specifically.

Prefer `Get-CimInstance Win32_LogicalDisk` (uint64 bytes) over `Get-PSDrive` (doubles) for the threshold math.

### B. Memory / commit-driven

Symptoms: slow, stuttering, swap/pagefile growing, fans up.

- **Commit % is the primary signal** (`\Memory\% Committed Bytes In Use`). Commit charge is total reserved virtual memory (RAM + pagefile). Commit-limit exhaustion is the real Windows OOM — the analog of macOS swap saturation.
  - **> 85 %** → critical; commit failures / OOM risk. Pair with **available RAM < 5 %** for a true CRITICAL.
  - **75–85 %** → warning; pagefile is expanding aggressively.
  - **< 60 %** → healthy.
- **Do NOT alarm on "In Use" RAM % alone.** `\Memory\Available MBytes` includes **standby/cache** pages that are instantly reclaimable. Task Manager showing 14/16 GB "in use" with 2 GB available is normal and healthy. Memory Compression (`(Get-MMAgent).MemoryCompression`) extending RAM is also normal.
- VM-driven: WSL2 (`vmmem`/`vmmemWSL`) and Docker Desktop can dominate. Check WSL memory cap in `%USERPROFILE%\.wslconfig` (`memory=`). Rule of thumb: keep WSL ≤ ~1/2 host RAM.

### C. BSOD / crash / unexpected shutdown (rare but severe)

Symptoms: PC rebooted on its own; "Windows recovered from an unexpected shutdown".

```powershell
$since = (Get-Date).AddDays(-14)
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-Kernel-Power'; Id=41; StartTime=$since} -EA SilentlyContinue |
  Select-Object TimeCreated, @{N='BugcheckCode';E={ ([xml]$_.ToXml()).Event.EventData.Data | ?{$_.Name -eq 'BugcheckCode'} | %{$_.'#text'} }}
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WER-SystemErrorReporting'; Id=1001; StartTime=$since} -EA SilentlyContinue |
  Select-Object TimeCreated, Message
```

Interpret:
- **Kernel-Power 41** with `BugcheckCode = 0` → power loss / hard reset (no BSOD). Nonzero `BugcheckCode` (decimal stop code) → a bluescreen occurred.
- **WER-SystemErrorReporting 1001** → the BSOD record with the stop code and dump path.
- **WHEA-Logger 1** (fatal) / **18** (corrected) → hardware errors. A single corrected error after S0ix resume is usually benign; sustained sequences are not.
- Cross-check disk free at the time and whether commit was saturated — a memory/commit crisis can precede an OOM-driven crash.

After a crash of this class: confirm it's a one-off (look back 30 days), run cleanup Tier 1–7 for breathing room, install/verify the alerter (`alerting.md`), and if a VM (WSL/Docker/Hyper-V) was the proximate cause, discuss reducing its memory cap.

### D. New crash dump appeared

This is the alerter's loudest signal and a leading indicator of (C). Find recent dumps:

```powershell
Get-ChildItem "$env:SystemRoot\Minidump" -Filter *.dmp -EA SilentlyContinue |
  Where-Object LastWriteTime -gt (Get-Date).AddDays(-2) |
  Select-Object FullName, LastWriteTime, @{N='MB';E={[math]::Round($_.Length/1MB,1)}}
Get-Item "$env:SystemRoot\MEMORY.DMP" -EA SilentlyContinue
```

If a fresh dump exists, the system already bugchecked. **Keep the dumps** until triaged — they are forensic evidence (never delete as "cleanup" before the cause is understood). Analyze with WinDbg/`!analyze -v` or `Get-WinEvent` 1001 for the stop code.

### E. "PC just feels slow"

Usually commit/memory pressure, thermal throttling, or startup bloat — not a "RAM cleaner" problem.

```powershell
# Startup inventory (causes, not symptoms). Autorunsc (Sysinternals) is the CLI form of Autoruns:
#   autorunsc.exe -accepteula -a * -c -h -s | ConvertFrom-Csv | Sort-Object Entry
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location | Format-Table -Auto
(Get-MMAgent).MemoryCompression   # True = OS compressing pages (normal, not a fault)
```

If nothing stands out, fall back to the memory/commit flow (B). **Do not run "RAM optimizers"** — they purge working sets/standby and make the next access slower, not faster.

## Decision tree

```
ALERT or USER REPORT
       │
       ▼
   free % < 20? ──yes──▶ A. Disk-driven (cleanup-tiers.md)
       │
       no
       ▼
   crash event /
   dump last 24h? ──yes──▶ C/D. Read stop code, keep dumps, propose cleanup + alerter
       │
       no
       ▼
   commit % > 85 AND
   RAM free < 5%? ──yes──▶ B. Memory/commit-driven, check WSL/Docker caps
       │
       no
       ▼
   thermal / startup ──yes──▶ E. Startup audit, thermal advice (no RAM cleaners)
       │
       no
       ▼
   user perception → tree-size audit, propose targeted cleanup
```

## What to NOT do at triage

- Don't run a broad cleanup reflexively. Identify what's hurting first.
- Don't delete crash dumps before the crash is triaged — they're evidence.
- Don't delete `pagefile.sys` / `swapfile.sys` / `hiberfil.sys`, touch WinSxS by hand, or run a registry cleaner. None of those are "cleanup".
- Don't run "RAM optimizer" tools — purging standby/working sets degrades performance.
- Don't `Stop-Process` the top working-set process to "free memory" — corrupts open handles (Docker volumes, DB writes, unsaved work). Ask the user to close it gracefully.
