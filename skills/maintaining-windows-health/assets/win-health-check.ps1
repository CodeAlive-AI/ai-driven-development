<#
.SYNOPSIS
    win-health-check - minimal noise-resistant Windows 11 health monitor.

.DESCRIPTION
    PowerShell port of the macOS mac-health-check LaunchAgent script. Three
    CRITICAL-only triggers, each guarded by hysteresis + cooldown + a calibration
    window so it stays quiet under normal heavy dev load:

      1) Disk free below threshold on the watched volume (3 consecutive readings)
      2) Memory commit pressure above threshold AND available RAM below threshold
         (3 consecutive readings). Commit % is the PRIMARY signal - '\Memory\
         Available MBytes' includes standby/cache, so high "available" alone does
         not mean healthy; commit-limit exhaustion is the real Windows OOM signal.
      3) A NEW crash minidump appears in C:\Windows\Minidump (immediate, via file
         polling - the cheap analog of the macOS JetsamEvent file poll). A narrow
         Get-WinEvent BugCheck query is used only as confirmation.

    No auto-cleanup. The alert notifies; the human decides.

.NOTES
    Designed to run from a per-user Task Scheduler job in the INTERACTIVE user
    session (so toasts render). See Install-WinHealthCheck.ps1. Compatible with
    Windows PowerShell 5.1 (shipped with Windows 11) and PowerShell 7+.

    Override config for testing:  $env:WIN_HEALTH_CONFIG = 'C:\path\cfg.ps1'
#>

[CmdletBinding()]
param()

$ErrorActionPreference = 'Continue'

# ---- Defaults (config can override) ----------------------------------------
$DiskVolume         = 'C:'
$DiskCriticalPct    = 10
$CommitCriticalPct  = 90
$MemFreeCriticalPct = 5
$CooldownMinutes    = 30
$HysteresisReadings = 3
$CalibrationDays    = 7
$Notifier           = 'auto'
$NtfyUrl            = ''
$DumpDir            = Join-Path $env:SystemRoot 'Minidump'

$StateDir = Join-Path $env:LOCALAPPDATA 'win-health'
$LogDir   = Join-Path $StateDir 'logs'
$SuppressFile = Join-Path $StateDir 'silent'

# ---- Load config ------------------------------------------------------------
$ConfigPath = $env:WIN_HEALTH_CONFIG
if (-not $ConfigPath) { $ConfigPath = Join-Path $StateDir 'win-health-check.config.ps1' }
if (Test-Path -LiteralPath $ConfigPath) { . $ConfigPath }

$LogFile          = Join-Path $LogDir 'health.log'
$InstallDateFile  = Join-Path $StateDir 'install_date'
$DumpsSeenFile    = Join-Path $StateDir 'dumps_seen'

New-Item -ItemType Directory -Force -Path $StateDir, $LogDir | Out-Null

$Now = [int][double]::Parse((Get-Date -UFormat %s))

function Write-HealthLog {
    param([string]$Message)
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    Add-Content -LiteralPath $LogFile -Value "$ts $Message" -Encoding UTF8
}

# ---- Calibration window -----------------------------------------------------
if (-not (Test-Path -LiteralPath $InstallDateFile)) {
    Set-Content -LiteralPath $InstallDateFile -Value $Now -Encoding ASCII
}
$InstallDate     = [int](Get-Content -LiteralPath $InstallDateFile -ErrorAction SilentlyContinue)
$DaysSinceInstall = [math]::Floor(($Now - $InstallDate) / 86400)
$InCalibration   = $DaysSinceInstall -lt $CalibrationDays

function Test-Suppressed {
    if (Test-Path -LiteralPath $SuppressFile) { return $true }
    if ($InCalibration) { return $true }
    return $false
}

function Test-InCooldown {
    param([string]$Key)
    $file = Join-Path $StateDir "cooldown.$Key"
    if (-not (Test-Path -LiteralPath $file)) { return $false }
    $last = [int](Get-Content -LiteralPath $file -ErrorAction SilentlyContinue)
    $elapsedMin = [math]::Floor(($Now - $last) / 60)
    return ($elapsedMin -lt $CooldownMinutes)
}

function Set-Cooldown { param([string]$Key)
    Set-Content -LiteralPath (Join-Path $StateDir "cooldown.$Key") -Value $Now -Encoding ASCII
}

function Get-BumpedCounter {
    param([string]$Key)
    $file = Join-Path $StateDir "counter.$Key"
    $v = 0
    if (Test-Path -LiteralPath $file) { $v = [int](Get-Content -LiteralPath $file -ErrorAction SilentlyContinue) }
    $v++
    Set-Content -LiteralPath $file -Value $v -Encoding ASCII
    return $v
}

function Reset-Counter { param([string]$Key)
    Remove-Item -LiteralPath (Join-Path $StateDir "counter.$Key") -ErrorAction SilentlyContinue
}

# ---- Notifiers --------------------------------------------------------------
function Send-Toast {
    param([string]$Title, [string]$Message)
    $choice = $Notifier
    if ($choice -eq 'none') { return }

    if ($choice -eq 'auto' -or $choice -eq 'burnttoast') {
        if (Get-Module -ListAvailable -Name BurntToast) {
            try {
                Import-Module BurntToast -ErrorAction Stop
                New-BurntToastNotification -Text $Title, $Message -ErrorAction Stop
                return
            } catch {
                Write-HealthLog "  -> BurntToast failed: $($_.Exception.Message)"
            }
        }
    }

    if ($choice -eq 'auto' -or $choice -eq 'winrt') {
        try {
            Send-WinRtToast -Title $Title -Message $Message
            return
        } catch {
            Write-HealthLog "  -> WinRT toast failed: $($_.Exception.Message)"
        }
    }

    Write-HealthLog "  -> no toast channel available (install BurntToast or set NtfyUrl)"
}

function Send-WinRtToast {
    # Native, dependency-free fallback. Attributed to PowerShell unless a custom
    # AUMID shortcut is registered (BurntToast is the recommended path).
    param([string]$Title, [string]$Message)
    $null = [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
    $null = [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime]
    $xml = @"
<toast><visual><binding template="ToastGeneric"><text>$([System.Security.SecurityElement]::Escape($Title))</text><text>$([System.Security.SecurityElement]::Escape($Message))</text></binding></visual></toast>
"@
    $doc = New-Object Windows.Data.Xml.Dom.XmlDocument
    $doc.LoadXml($xml)
    $appId = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe'
    $toast = [Windows.UI.Notifications.ToastNotification]::new($doc)
    [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($appId).Show($toast)
}

function Send-NtfyPush {
    param([string]$Title, [string]$Message)
    if (-not $NtfyUrl) { return }
    try {
        Invoke-RestMethod -Method Post -Uri $NtfyUrl -Body $Message -TimeoutSec 5 `
            -Headers @{ Title = $Title; Priority = 'high'; Tags = 'warning' } | Out-Null
    } catch {
        Write-HealthLog "  -> ntfy push failed: $($_.Exception.Message)"
    }
}

function Send-Alert {
    param([string]$Key, [string]$Title, [string]$Message, [string]$Reason)
    Write-HealthLog "ALERT key=$Key reason='$Reason' title='$Title' msg='$Message'"

    if (Test-Suppressed) {
        if (Test-Path -LiteralPath $SuppressFile) {
            Write-HealthLog "  -> suppressed (silent file)"
        } else {
            Write-HealthLog "  -> suppressed (calibration day=$DaysSinceInstall/$CalibrationDays)"
        }
        return
    }
    if (Test-InCooldown $Key) {
        Write-HealthLog "  -> cooldown active for '$Key', skip"
        return
    }
    Set-Cooldown $Key
    Send-Toast -Title $Title -Message $Message
    Send-NtfyPush -Title $Title -Message $Message
    Write-HealthLog "  -> delivered"
}

# ---- Sensor 1: Disk free ----------------------------------------------------
function Test-Disk {
    $deviceId = $DiskVolume.TrimEnd('\')
    if ($deviceId -notmatch ':$') { $deviceId = "${deviceId}:" }
    $d = Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DeviceID='$deviceId'" -ErrorAction SilentlyContinue
    if (-not $d -or -not $d.Size) { Write-HealthLog "disk: volume $deviceId not found"; return }
    $pctFree = [math]::Floor($d.FreeSpace * 100 / $d.Size)
    Write-HealthLog "disk volume=$deviceId free_pct=$pctFree threshold=$DiskCriticalPct"

    if ($pctFree -lt $DiskCriticalPct) {
        $count = Get-BumpedCounter 'disk'
        Write-HealthLog "  disk below threshold (count=$count/$HysteresisReadings)"
        if ($count -ge $HysteresisReadings) {
            Send-Alert -Key 'disk_critical' -Title 'Disk Critical' `
                -Message "Free: $pctFree% on $deviceId. Run Storage cleanup or review Downloads." `
                -Reason "disk_free=$pctFree%"
        }
    } else {
        Reset-Counter 'disk'
    }
}

# ---- Sensor 2: Memory commit pressure --------------------------------------
function Get-CounterValue {
    param([string]$Path)
    try {
        return (Get-Counter -Counter $Path -SampleInterval 1 -MaxSamples 1 -ErrorAction Stop).CounterSamples[0].CookedValue
    } catch {
        return $null
    }
}

function Test-Memory {
    $os = Get-CimInstance -ClassName Win32_OperatingSystem -ErrorAction SilentlyContinue
    $freePct = 100
    if ($os -and $os.TotalVisibleMemorySize -gt 0) {
        $freePct = [math]::Round($os.FreePhysicalMemory / $os.TotalVisibleMemorySize * 100, 1)
    }
    $commitPct = Get-CounterValue '\Memory\% Committed Bytes In Use'
    if ($null -eq $commitPct) { Write-HealthLog 'memory: commit counter unavailable'; $commitPct = 0 }
    $commitPct = [math]::Round($commitPct, 1)
    Write-HealthLog "memory free_pct=$freePct commit_pct=$commitPct crit_free=$MemFreeCriticalPct crit_commit=$CommitCriticalPct"

    if ($commitPct -gt $CommitCriticalPct -and $freePct -lt $MemFreeCriticalPct) {
        $count = Get-BumpedCounter 'memory'
        Write-HealthLog "  memory critical (count=$count/$HysteresisReadings)"
        if ($count -ge $HysteresisReadings) {
            Send-Alert -Key 'memory_critical' -Title 'Memory Critical' `
                -Message "Commit at $commitPct%, free RAM $freePct%. Close heavy apps." `
                -Reason "commit=$commitPct% free=$freePct%"
        }
    } else {
        Reset-Counter 'memory'
    }
}

# ---- Sensor 3: New crash minidumps -----------------------------------------
function Test-CrashDumps {
    if (-not (Test-Path -LiteralPath $DumpsSeenFile)) { New-Item -ItemType File -Force -Path $DumpsSeenFile | Out-Null }
    $seen = @(Get-Content -LiteralPath $DumpsSeenFile -ErrorAction SilentlyContinue)
    $seenSet = @{}; foreach ($s in $seen) { $seenSet[$s] = $true }

    $dumps = @()
    if (Test-Path -LiteralPath $DumpDir) {
        $dumps += Get-ChildItem -LiteralPath $DumpDir -Filter '*.dmp' -ErrorAction SilentlyContinue
    }
    $memDmp = Join-Path $env:SystemRoot 'MEMORY.DMP'
    if (Test-Path -LiteralPath $memDmp) { $dumps += Get-Item -LiteralPath $memDmp -ErrorAction SilentlyContinue }

    $cutoff = (Get-Date).AddHours(-24)
    $newCount = 0
    foreach ($f in $dumps) {
        if (-not $f) { continue }
        if ($seenSet.ContainsKey($f.Name)) { continue }
        Add-Content -LiteralPath $DumpsSeenFile -Value $f.Name -Encoding UTF8
        if ($f.LastWriteTime -lt $cutoff) { continue }   # old dump, just record as seen
        $newCount++
        $stamp = $f.LastWriteTime.ToString('yyyy-MM-dd HH:mm')
        Write-HealthLog "crash NEW dump: $($f.Name) ($stamp)"
        Send-Alert -Key 'crash_dump' -Title 'System Crash Detected' `
            -Message "New crash dump $($f.Name) at $stamp. Review reliability; save work." `
            -Reason $f.Name
    }
    Write-HealthLog "crash scan new=$newCount"

    # Trim seen list if it grows large
    $lines = @(Get-Content -LiteralPath $DumpsSeenFile -ErrorAction SilentlyContinue)
    if ($lines.Count -gt 500) {
        $lines[-250..-1] | Set-Content -LiteralPath $DumpsSeenFile -Encoding UTF8
    }
}

# ---- Main -------------------------------------------------------------------
Write-HealthLog "=== run start (calibration=$InCalibration, days=$DaysSinceInstall) ==="
try { Test-Disk }       catch { Write-HealthLog "ERROR Test-Disk: $($_.Exception.Message)" }
try { Test-Memory }     catch { Write-HealthLog "ERROR Test-Memory: $($_.Exception.Message)" }
try { Test-CrashDumps } catch { Write-HealthLog "ERROR Test-CrashDumps: $($_.Exception.Message)" }
Write-HealthLog "=== run end ==="
