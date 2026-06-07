<#
.SYNOPSIS
    Read-only preflight inventory for a Windows 11 cleanup window. Deletes
    NOTHING - it only collects the decision points so the agent and the user can
    classify safely before any destructive step.

.DESCRIPTION
    Windows analog of the macOS triage snapshot + the author's audit template.
    Gathers: drives, Component Store size (DISM), VSS shadow storage, user
    profiles, third-party drivers, %TEMP% size, recent crash dumps + crash
    events, AND the Windows-only safety signals that have no macOS analog and are
    easy to forget: Controlled Folder Access state, OneDrive Known Folder Move
    redirection of Desktop/Documents, BitLocker protection status, and
    reparse-point (junction/symlink) presence under scan roots.

    Run as Administrator for the DISM / shadow-storage / driver sections.

.PARAMETER ReportPath
    Where to write the text report. Defaults to a timestamped file under %TEMP%.

.PARAMETER ScanRoot
    Folder(s) to scan for reparse points (repeatable). Defaults to %USERPROFILE%.
#>

[CmdletBinding()]
param(
    [string]$ReportPath,
    [string[]]$ScanRoot
)

$ErrorActionPreference = 'Continue'
if (-not $ReportPath) {
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $ReportPath = Join-Path $env:TEMP "Win11-Cleanup-Audit-$stamp.txt"
}
if (-not $ScanRoot) { $ScanRoot = @($env:USERPROFILE) }

function Add-Section {
    param([string]$Title, [scriptblock]$Body)
    $header = "`n=== $Title ==="
    $header | Tee-Object -FilePath $ReportPath -Append | Out-Null
    Write-Host $header -ForegroundColor Cyan
    try {
        & $Body | Out-String | Tee-Object -FilePath $ReportPath -Append
    } catch {
        "  (section error: $($_.Exception.Message))" | Tee-Object -FilePath $ReportPath -Append
    }
}

"Windows 11 cleanup audit - $(Get-Date -Format 'u')" | Set-Content -LiteralPath $ReportPath -Encoding UTF8

Add-Section 'DRIVES' {
    Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' |
        Select-Object DeviceID,
            @{N='SizeGB';E={[math]::Round($_.Size/1GB,1)}},
            @{N='FreeGB';E={[math]::Round($_.FreeSpace/1GB,1)}},
            @{N='FreePct';E={ if ($_.Size) { [math]::Round($_.FreeSpace/$_.Size*100,1) } else { 0 } }} |
        Format-Table -AutoSize
}

Add-Section 'MEMORY / COMMIT' {
    $os = Get-CimInstance Win32_OperatingSystem
    $commit = 'n/a'
    try { $commit = [math]::Round((Get-Counter '\Memory\% Committed Bytes In Use' -ErrorAction Stop).CounterSamples[0].CookedValue,1) } catch { }
    $page = 'n/a'
    try { $page = [math]::Round((Get-Counter '\Paging File(_Total)\% Usage' -ErrorAction Stop).CounterSamples[0].CookedValue,1) } catch { }
    [pscustomobject]@{
        TotalRAM_GB    = [math]::Round($os.TotalVisibleMemorySize/1MB,1)
        FreeRAM_GB     = [math]::Round($os.FreePhysicalMemory/1MB,1)
        FreeRAM_Pct    = [math]::Round($os.FreePhysicalMemory/$os.TotalVisibleMemorySize*100,1)
        CommitInUsePct = $commit
        PagefilePctUse = $page
    } | Format-List
}

Add-Section 'PAGEFILE / HIBERFIL' {
    Get-CimInstance Win32_PageFileUsage |
        Select-Object Name, AllocatedBaseSize, CurrentUsage, PeakUsage | Format-Table -AutoSize
    $hib = Get-Item -LiteralPath (Join-Path $env:SystemDrive '\hiberfil.sys') -Force -ErrorAction SilentlyContinue
    if ($hib) { "hiberfil.sys = $([math]::Round($hib.Length/1GB,2)) GB (hibernation ON)" }
    else      { "hiberfil.sys absent (hibernation OFF)" }
}

Add-Section 'COMPONENT STORE (WinSxS)' {
    cmd /c 'Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore'
}

Add-Section 'SHADOW STORAGE / RESTORE' {
    cmd /c 'vssadmin list shadowstorage'
}

Add-Section 'USER PROFILES' {
    Get-CimInstance Win32_UserProfile |
        Select-Object LocalPath, LastUseTime, Loaded, Special |
        Sort-Object LocalPath | Format-Table -AutoSize
}

Add-Section 'THIRD-PARTY DRIVERS' {
    cmd /c 'pnputil /enum-drivers'
}

Add-Section 'WINDOWS.OLD / ROLLBACK WINDOW' {
    if (Test-Path -LiteralPath (Join-Path $env:SystemDrive '\Windows.old')) {
        "Windows.old present:"
        cmd /c 'Dism.exe /Online /Get-OSUninstallWindow'
    } else { "No Windows.old present." }
}

Add-Section 'TEMP SIZE' {
    foreach ($p in @($env:TEMP, (Join-Path $env:SystemRoot 'Temp'))) {
        if (Test-Path -LiteralPath $p) {
            $sum = (Get-ChildItem -LiteralPath $p -Recurse -Force -ErrorAction SilentlyContinue |
                    Measure-Object Length -Sum).Sum
            "{0,-40} {1,8:N0} MB" -f $p, ([math]::Round(($sum/1MB),0))
        }
    }
}

Add-Section 'RECENT CRASH DUMPS' {
    $cutoff = (Get-Date).AddDays(-30)
    @(
        Get-ChildItem (Join-Path $env:SystemRoot 'Minidump') -Filter '*.dmp' -ErrorAction SilentlyContinue
        Get-Item (Join-Path $env:SystemRoot 'MEMORY.DMP') -ErrorAction SilentlyContinue
    ) | Where-Object { $_ -and $_.LastWriteTime -gt $cutoff } |
        Select-Object FullName, LastWriteTime, @{N='SizeMB';E={[math]::Round($_.Length/1MB,1)}} |
        Format-Table -AutoSize
}

Add-Section 'RECENT CRASH EVENTS (7d)' {
    $since = (Get-Date).AddDays(-7)
    Get-WinEvent -FilterHashtable @{ LogName='System'; Id=41,1001,6008; StartTime=$since } -ErrorAction SilentlyContinue |
        Select-Object TimeCreated, Id, ProviderName |
        Sort-Object TimeCreated -Descending | Select-Object -First 15 | Format-Table -AutoSize
}

# ---- Windows-only safety signals (no macOS analog) -------------------------
Add-Section 'CONTROLLED FOLDER ACCESS (ransomware protection)' {
    try {
        $cfa = (Get-MpPreference -ErrorAction Stop).EnableControlledFolderAccess
        "EnableControlledFolderAccess = $cfa  (1/2 = ON; deletes in Documents/Pictures/Desktop may be BLOCKED by Defender, not a tool bug)"
    } catch { "Get-MpPreference unavailable: $($_.Exception.Message)" }
}

Add-Section 'ONEDRIVE KNOWN FOLDER MOVE' {
    foreach ($name in 'Desktop','Documents','Pictures') {
        $p = Join-Path $env:USERPROFILE $name
        $item = Get-Item -LiteralPath $p -Force -ErrorAction SilentlyContinue
        $isReparse = $item -and ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)
        $redirected = if ($isReparse -or ($item -and $item.FullName -like '*OneDrive*')) { 'REDIRECTED into OneDrive (deletes propagate to cloud + all devices)' } else { 'local' }
        "{0,-10} {1}" -f $name, $redirected
    }
}

Add-Section 'BITLOCKER' {
    try {
        Get-BitLockerVolume -ErrorAction Stop |
            Select-Object MountPoint, VolumeStatus, ProtectionStatus, EncryptionPercentage |
            Format-Table -AutoSize
    } catch { "Get-BitLockerVolume unavailable (needs admin / BitLocker feature): $($_.Exception.Message)" }
}

Add-Section 'REPARSE POINTS UNDER SCAN ROOTS (recurse hazard)' {
    foreach ($root in $ScanRoot) {
        if (-not (Test-Path -LiteralPath $root)) { continue }
        "Root: $root"
        Get-ChildItem -LiteralPath $root -Recurse -Depth 4 -Force -Directory -ErrorAction SilentlyContinue |
            Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint } |
            Select-Object -First 40 -ExpandProperty FullName
    }
}

Write-Host ""
Write-Host "[audit] Report written to $ReportPath" -ForegroundColor Green
