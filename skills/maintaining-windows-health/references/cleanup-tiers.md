# Cleanup tiers

Ten tiers, ordered by risk and reward. Always start at the lowest, only escalate if the goal isn't met. Each tier ends with a free-space checkpoint. **Prefer native Microsoft-supported tools and the tool's own cache command over hand-rolled `Remove-Item`** — see `native-tools.md`. Every destructive item the agent surfaces in the cleanup UI runs through `assets/apply-cleanup-selection.py`, which validates the command before executing; do not bypass it with ad-hoc deletions.

## Table of contents

- [Tier 1 — Storage Sense + trivial wins](#tier-1--storage-sense--trivial-wins-low-risk)
- [Tier 2 — Package manager caches](#tier-2--package-manager-caches)
- [Tier 3 — Browser & Electron caches](#tier-3--browser--electron-caches)
- [Tier 4 — Stale IDE / SDK versions](#tier-4--stale-ide--sdk-versions)
- [Tier 5 — Downloads (interactive)](#tier-5--downloads-interactive)
- [Tier 6 — Component Store (DISM)](#tier-6--component-store-dism)
- [Tier 7 — Project artifacts (purge)](#tier-7--project-artifacts-purge)
- [Tier 8 — Docker & WSL2 / Hyper-V VHDX](#tier-8--docker--wsl2--hyper-v-vhdx)
- [Tier 9 — Elevated: Windows.old, DO, Event Logs, restore points](#tier-9--elevated-windowsold-delivery-optimization-event-logs-restore-points)
- [Tier 10 — Discuss-first](#tier-10--discuss-first)
- [Large-file visibility pass](#large-file-visibility-pass)
- [Reset prevention recipes](#reset-prevention-recipes)
- [After cleanup](#after-cleanup)

**Baseline first:**

```powershell
Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' |
  Select-Object DeviceID, @{N='FreeGB';E={[math]::Round($_.FreeSpace/1GB,1)}}, @{N='FreePct';E={[math]::Round($_.FreeSpace/$_.Size*100,1)}}
# For Tiers 3 (Electron) and 8 (Docker/WSL): quit the apps / `wsl --shutdown` first.
```

---

## Tier 1 — Storage Sense + trivial wins (low risk)

The biggest safe win on Windows is the built-in tooling. Start here.

```powershell
# GUI: Settings → System → Storage → "Cleanup recommendations" (temp files, large/unused, cloud-synced, unused apps).
# Enable Storage Sense to keep it tidy automatically (per-user):
Start-Process ms-settings:storagesense

# Recycle Bin (all drives)
Clear-RecycleBin -Force -ErrorAction SilentlyContinue

# User + Windows temp older than N days (Remove-Item is PERMANENT — no Recycle Bin)
$cut = (Get-Date).AddDays(-14)
Get-ChildItem $env:TEMP -Force -EA SilentlyContinue | Where-Object LastWriteTime -lt $cut |
  Remove-Item -Recurse -Force -EA SilentlyContinue
Get-ChildItem "$env:SystemRoot\Temp" -Force -EA SilentlyContinue | Where-Object LastWriteTime -lt $cut |
  Remove-Item -Recurse -Force -EA SilentlyContinue   # needs admin

# Legacy Disk Cleanup, scripted (define a profile once, run it anywhere):
cleanmgr /sageset:1   # tick categories in the dialog once
cleanmgr /sagerun:1   # runs that profile on all drives
```

⚠️ Leave **Prefetch** (`C:\Windows\Prefetch`) alone — deleting it slows boot for ~tens of MB. Don't delete `Windows.edb` (search index) live; rebuild via Settings or stopping `WSearch` instead.

---

## Tier 2 — Package manager caches

All regenerate on next build. Use the tool's own command where it exists — they keep index integrity better than `Remove-Item`.

```powershell
npm cache clean --force
pnpm store prune
dotnet nuget locals all --clear
pip cache purge
if (Get-Command uv -EA SilentlyContinue) { uv cache clean }
if (Get-Command cargo -EA SilentlyContinue) { cargo cache --autoclean }  # needs cargo-cache; else: Remove-Item "$env:USERPROFILE\.cargo\registry\cache" -Recurse -Force
if (Get-Command go -EA SilentlyContinue) { go clean -cache; go clean -modcache }
# Gradle wrapper dists / downloaded JDKs (regenerate on next build):
Remove-Item "$env:USERPROFILE\.gradle\wrapper\dists" -Recurse -Force -EA SilentlyContinue
Remove-Item "$env:USERPROFILE\.gradle\caches\jars-*" -Recurse -Force -EA SilentlyContinue
# Playwright/Puppeteer browser binaries — list, then remove old versions only:
Get-ChildItem "$env:USERPROFILE\AppData\Local\ms-playwright" -EA SilentlyContinue
```

---

## Tier 3 — Browser & Electron caches

⚠️ **Quit the apps first.** Running apps regenerate cache mid-write and can glitch.

```powershell
# Cache-family subfolders only — NEVER IndexedDB / Local Storage / Cookies / "User Data\Default" wholesale.
$apps = @(
  "$env:APPDATA\Slack",
  "$env:APPDATA\Notion",
  "$env:APPDATA\Microsoft\Teams",
  "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default",
  "$env:LOCALAPPDATA\Google\Chrome\User Data\Default",
  "$env:APPDATA\Code",
  "$env:APPDATA\Cursor"
)
$cacheSubs = 'Cache','Code Cache','GPUCache','DawnCache','DawnGraphiteCache','GrShaderCache','ShaderCache','Service Worker\CacheStorage'
foreach ($a in $apps) {
  foreach ($s in $cacheSubs) { Remove-Item (Join-Path $a $s) -Recurse -Force -EA SilentlyContinue }
}
```

Browser cache is also clearable from each browser's own Settings → Privacy → Clear browsing data (pick **Cached images and files** only; leave cookies/passwords). In Edge with sync on, clearing browsing data can affect synced devices.

⚠️ Do NOT delete `IndexedDB`, `Local Storage`, `Cookies`, Telegram `tdata\`, or anything carrying app state — see `never-touch.md`.

---

## Tier 4 — Stale IDE / SDK versions

```powershell
# JetBrains: list data dirs, remove only confirmed-stale major.minor versions
Get-ChildItem "$env:APPDATA\JetBrains" -Directory -EA SilentlyContinue | Select-Object Name
# e.g. keep Rider2025.1, remove Rider2024.3:
# Remove-Item "$env:APPDATA\JetBrains\Rider2024.3" -Recurse -Force
# Caches/logs/indexes for current versions (re-index on next launch — slow but safe):
Remove-Item "$env:LOCALAPPDATA\JetBrains\*\caches" -Recurse -Force -EA SilentlyContinue
Remove-Item "$env:LOCALAPPDATA\JetBrains\*\log"    -Recurse -Force -EA SilentlyContinue

# .NET old SDKs — list first; remove only if a newer same-major exists:
dotnet --list-sdks
# Visual Studio leftover component cache:
Remove-Item "$env:ProgramData\Microsoft\VisualStudio\Packages\_Instances\*\..\..\..\*.cache" -EA SilentlyContinue
```

---

## Tier 5 — Downloads (interactive)

Largest variable category. Show the breakdown first; always confirm before delete.

```powershell
Get-ChildItem "$env:USERPROFILE\Downloads" -File -EA SilentlyContinue |
  Sort-Object Length -Desc | Select-Object -First 30 Name,
    @{N='MB';E={[math]::Round($_.Length/1MB,1)}}, LastWriteTime
```

⚠️ **OneDrive Known Folder Move:** Downloads is usually local, but **Desktop / Documents / Pictures are often redirected into OneDrive**. Deleting a redirected file removes the cloud copy and propagates to every synced device. Check before touching those folders (the audit script reports KFM status). Propose for deletion: installers (`.iso/.msi/.exe/.zip`) older than 30 days that were already used; extracted folders sitting next to their archive; old recordings.

---

## Tier 6 — Component Store (DISM)

WinSxS grows with updates. **Never delete WinSxS by hand** — Microsoft says the system can stop booting/updating. Analyze, then clean only if recommended.

```powershell
Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore   # look for "Component Store Cleanup Recommended : Yes"
Dism.exe /Online /Cleanup-Image /StartComponentCleanup    # only if reclaimable / recommended
```

`/ResetBase` (removes the ability to uninstall existing updates) is **Tier 10**, not here.

---

## Tier 7 — Project artifacts (purge)

Highest-reward tier on a dev machine. Regenerable build/dependency dirs, age-gated. There is **no mature Mole-for-Windows**, so the apply-script validator is the only safety floor here — keep `mtime ≥ 7 days` and `-LiteralPath`, and never recurse through a reparse point (junctions in `node_modules`/pnpm store/WSL escape recursive deletes). See `native-tools.md` for the marker→target map and the safe-purge harness.

```powershell
# Inventory candidate roots (HOME by default; pass external drives as scan roots to the apply script):
$roots = "$env:USERPROFILE\source","$env:USERPROFILE\repos","$env:USERPROFILE\dev","$env:USERPROFILE\Projects"
$cut = (Get-Date).AddDays(-7)
foreach ($r in $roots) {
  if (-not (Test-Path $r)) { continue }
  Get-ChildItem $r -Recurse -Depth 4 -Directory -Force -EA SilentlyContinue |
    Where-Object { $_.Name -in 'node_modules','.next','.nuxt','dist','build','target','__pycache__','.venv','.gradle' -and
                   $_.LastWriteTime -lt $cut -and
                   -not ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) } |
    Select-Object FullName, LastWriteTime
}
# Surface the confirmed list in the cleanup UI; apply via apply-cleanup-selection.py (per-item -LiteralPath Remove-Item).
```

⚠️ `bin`/`obj` only for confirmed .NET projects (sibling `*.csproj`); `vendor` only for PHP Composer (Go/Rails `vendor` is hand-curated). Check `git status` for uncommitted state before deleting build dirs.

---

## Tier 8 — Docker & WSL2 / Hyper-V VHDX

```powershell
docker system df              # see reclaimable
docker image prune -f
docker builder prune -f
docker volume ls -f dangling=true    # review BEFORE removing — data volumes live here
```

⚠️ Never `docker system prune -af --volumes` without listing volumes — it deletes data volumes (postgres/mongo data) unconfirmed.

**WSL2 / Docker-Desktop VHDX — compact, never delete.** `ext4.vhdx` is the entire Linux filesystem; deleting it destroys all your WSL data. It grows and doesn't auto-shrink. Reclaim by compacting:

```powershell
wsl --shutdown
# Find the disk, then compact it (run from an elevated prompt):
$vhdx = "$env:LOCALAPPDATA\Packages\<DistroPackage>\LocalState\ext4.vhdx"
Optimize-VHD -Path $vhdx -Mode Full   # Hyper-V module; OR use diskpart 'compact vdisk' on Home SKUs
```

---

## Tier 9 — Elevated: Windows.old, Delivery Optimization, Event Logs, restore points

Each needs admin and an explicit OK. Use the **command**, not folder deletion.

```powershell
# Windows.old — ONLY after confirming you won't roll back. Check the rollback window first:
Dism.exe /Online /Get-OSUninstallWindow
# Then remove via Settings → System → Storage → Temporary files → "Previous Windows installation(s)", or cleanmgr.

# Delivery Optimization cache (auto-capped anyway; point fix, not routine):
Delete-DeliveryOptimizationCache -Force

# Event Logs — EXPORT before clearing (forensics). Pattern: export then clear:
wevtutil epl Application "$env:USERPROFILE\Desktop\Application-backup.evtx" /ow:true
wevtutil cl Application /bu:"$env:USERPROFILE\Desktop\Application-before-clear.evtx"

# System Restore points — only if you have another backup/rollback:
vssadmin list shadowstorage
# vssadmin delete shadows /for=C: /oldest      # destroys restore points — discuss first
```

---

## Tier 10 — Discuss-first

Each item has real, often irreversible side effects. Explicit user OK required (the apply-script flags these as requiring a protected-override even though the tool is "supported").

```powershell
# DISM /ResetBase — removes ability to UNINSTALL existing updates. Stable baselines only.
Dism.exe /Online /Cleanup-Image /StartComponentCleanup /ResetBase

# Driver Store — remove stale third-party packages AFTER inventory/export:
pnputil /enum-drivers
# pnputil /export-driver oem42.inf C:\DriverBackup    # back up first
# pnputil /delete-driver oem42.inf /uninstall

# Shadow copies / restore points (loses rollback):
# vssadmin delete shadows /for=C: /all

# Hibernation off (frees hiberfil.sys; breaks hybrid sleep / fast startup; data-loss risk on power loss):
# powercfg /h off          # or shrink: powercfg /h /type reduced

# Pagefile — almost never "junk". Needed for modified pages + crash dumps. Leave system-managed.
Get-CimInstance Win32_PageFileUsage | Select-Object Name, AllocatedBaseSize, CurrentUsage, PeakUsage
```

⚠️ **Registry is never a cleanup target.** Microsoft does not support registry cleaners; "registry bloat" is a myth as a space/perf source. Only export-and-edit a specific known key when fixing a concrete problem.

---

## Large-file visibility pass

Run this after the tier scans and before building the cleanup JSON. Its purpose is visibility, not automatic deletion: it catches the large one-off files the user may no longer need, while keeping them unchecked/protected in the single final UI unless they are clearly safe cache.

```powershell
$roots = @(
  $env:USERPROFILE,
  $env:LOCALAPPDATA,
  $env:APPDATA,
  "$env:USERPROFILE\RiderProjects",
  "$env:USERPROFILE\PycharmProjects",
  "$env:USERPROFILE\source",
  "$env:USERPROFILE\repos",
  "$env:USERPROFILE\dev",
  "$env:USERPROFILE\Projects",
  "$env:USERPROFILE\GitHub",
  "$env:USERPROFILE\Code",
  "$env:USERPROFILE\work"
) | Where-Object { $_ -and (Test-Path -LiteralPath $_) } | Select-Object -Unique

$denyRegex = '\\\.git\\objects\\|\\Windows\\|\\Program Files( \(x86\))?\\|\\ProgramData\\Package Cache\\'

foreach ($root in $roots) {
  Get-ChildItem -LiteralPath $root -Recurse -File -Force -EA SilentlyContinue |
    Where-Object {
      $_.Length -gt 500MB -and
      $_.FullName -notmatch $denyRegex -and
      -not ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) -and
      -not ($_.Attributes -band [IO.FileAttributes]::Offline)
    } |
    Sort-Object Length -Desc |
    Select-Object -First 80 FullName,
      @{N='GB';E={[math]::Round($_.Length/1GB,2)}},
      LastWriteTime,
      Extension
}
```

When converting these findings to JSON:

- Mark user data, synced media, model weights (`.gguf`, `.safetensors`, `.onnx`), archives, app/project assets, app diagnostic dumps, and profiler captures as `protected: true`, `default_selected: false`, with a concrete warning.
- Include those protected findings in the same final cleanup JSON as the safe cache/temp/build-artifact candidates. Do not open a second UI round just for large files.
- Show VHDX files as inventory, but do not offer bare deletion. Use compact/prune workflows only; a WSL/Docker VHDX may be an entire filesystem.
- Do not offer `.git\objects` files as direct deletes. If a repository is too large, propose Git-native cleanup (`git gc`, removing stale branches, deleting the whole repo if the user chooses), not object-file deletion.
- Do not include cloud placeholders or Files On-Demand stubs. Deleting them deletes the cloud item.

---

## Reset prevention recipes

```powershell
# Storage Sense policy: run monthly, clear Recycle Bin > 30d (Settings → Storage → Storage Sense), or via Intune/GPO in a fleet.
# pnpm global store with hardlinks (dedupes across projects):
pnpm config set store-dir "$env:LOCALAPPDATA\pnpm-store"
# Docker tidy alias (PowerShell profile):
'function docker-tidy { docker container prune -f; docker image prune -f; docker builder prune -f }' |
  Add-Content $PROFILE
# Cap WSL memory so it stops ballooning (%USERPROFILE%\.wslconfig):
"[wsl2]`nmemory=8GB`nswap=2GB" | Set-Content "$env:USERPROFILE\.wslconfig"
```

---

## After cleanup

```powershell
# 1. Report the delta:
Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'" |
  Select-Object @{N='FreeGB';E={[math]::Round($_.FreeSpace/1GB,1)}}

# 2. Integrity post-check (Microsoft-recommended order):
Dism /Online /Cleanup-Image /CheckHealth
sfc /scannow

# 3. Re-check Windows Update opens, drivers intact, restore points still per plan.
# 4. Recommend the alerter (alerting.md) to prevent recurrence.
```

If freed space looks smaller than deleted, allow a minute — Storage Sense/`cleanmgr` defer some deletion, and `Remove-Item` to Recycle-Bin-bypassing paths is immediate while NTFS metadata settles.
