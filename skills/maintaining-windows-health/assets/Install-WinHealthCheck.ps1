<#
.SYNOPSIS
    Install / verify / remove the win-health-check scheduled task.

.DESCRIPTION
    Registers win-health-check.ps1 as a per-user Task Scheduler job that runs
    every 5 minutes in the INTERACTIVE user session. The interactive-session
    principal is deliberate and load-bearing: a task running as SYSTEM (or with
    "run whether user is logged on or not") executes fine but its toasts SILENTLY
    never render - the Windows analog of the macOS "osascript -> Script Editor"
    failure. Toasts require an interactive desktop session, so the task uses the
    logged-on user with LogonType Interactive and RunLevel Limited (toasts need
    no elevation; forcing Highest can hand the task a non-interactive token).

    Sleep behavior: -StartWhenAvailable makes the task catch up once on wake
    (the analog of the macOS plist's StartCalendarInterval coalescing). On
    Modern Standby (S0ix) laptops wake timers are unreliable, so the monitor
    pauses during sleep and resumes on wake - accepted, same as macOS.
    -AllowStartIfOnBatteries / -DontStopIfGoingOnBatteries keep it alive on a
    laptop running on battery.

.PARAMETER Uninstall
    Remove the scheduled task (state/logs under %LOCALAPPDATA%\win-health are
    kept unless -Purge is also given).

.PARAMETER Test
    Fire a synthetic disk-critical alert (no real danger) to confirm the toast
    pipeline works end to end, then exit.

.NOTES
    Run in a normal (non-elevated) PowerShell as the user who should receive the
    alerts. Windows PowerShell 5.1 or PowerShell 7+.
#>

[CmdletBinding()]
param(
    [switch]$Uninstall,
    [switch]$Purge,
    [switch]$Test,
    [switch]$SkipBurntToast
)

$ErrorActionPreference = 'Stop'
$TaskName = 'WinHealthCheck'
$StateDir = Join-Path $env:LOCALAPPDATA 'win-health'
$LogDir   = Join-Path $StateDir 'logs'
$ScriptDst = Join-Path $StateDir 'win-health-check.ps1'
$ConfigDst = Join-Path $StateDir 'win-health-check.config.ps1'

function Write-Step { param([string]$m) Write-Host "[win-health] $m" -ForegroundColor Cyan }

# ---- Uninstall --------------------------------------------------------------
if ($Uninstall) {
    if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Step "Removed scheduled task '$TaskName'."
    } else {
        Write-Step "No scheduled task '$TaskName' found."
    }
    if ($Purge -and (Test-Path -LiteralPath $StateDir)) {
        Remove-Item -LiteralPath $StateDir -Recurse -Force
        Write-Step "Purged $StateDir."
    }
    return
}

# ---- Synthetic test ---------------------------------------------------------
if ($Test) {
    if (-not (Test-Path -LiteralPath $ScriptDst)) {
        throw "win-health-check.ps1 not installed yet. Run install first (no -Test)."
    }
    $tmp = Join-Path $env:TEMP 'win-health-test.config.ps1'
    @'
$DiskVolume = 'C:'
$DiskCriticalPct = 99
$CommitCriticalPct = 999
$MemFreeCriticalPct = 0
$CooldownMinutes = 0
$HysteresisReadings = 1
$CalibrationDays = 0
$Notifier = 'auto'
'@ | Set-Content -LiteralPath $tmp -Encoding UTF8
    Remove-Item -LiteralPath (Join-Path $StateDir 'counter.disk') -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath (Join-Path $StateDir 'cooldown.disk_critical') -ErrorAction SilentlyContinue
    $env:WIN_HEALTH_CONFIG = $tmp
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $ScriptDst
    Remove-Item Env:\WIN_HEALTH_CONFIG -ErrorAction SilentlyContinue
    Write-Step "Synthetic disk alert fired. Check for a toast and the log:"
    Write-Step "  $(Join-Path $LogDir 'health.log')"
    Get-Content -LiteralPath (Join-Path $LogDir 'health.log') -Tail 8 -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath $tmp -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath (Join-Path $StateDir 'counter.disk') -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath (Join-Path $StateDir 'cooldown.disk_critical') -ErrorAction SilentlyContinue
    return
}

# ---- Install ----------------------------------------------------------------
New-Item -ItemType Directory -Force -Path $StateDir, $LogDir | Out-Null

Write-Step "Copying script + config to $StateDir"
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'win-health-check.ps1') -Destination $ScriptDst -Force
if (-not (Test-Path -LiteralPath $ConfigDst)) {
    Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'win-health-check.config.ps1') -Destination $ConfigDst -Force
    Write-Step "Installed default config (edit thresholds in $ConfigDst)."
} else {
    Write-Step "Existing config kept: $ConfigDst"
}

if (-not $SkipBurntToast) {
    if (-not (Get-Module -ListAvailable -Name BurntToast)) {
        Write-Step "Installing BurntToast (CurrentUser scope)..."
        try {
            Install-Module BurntToast -Scope CurrentUser -Force -AcceptLicense -ErrorAction Stop
            Write-Step "BurntToast installed."
        } catch {
            Write-Warning "BurntToast install failed: $($_.Exception.Message)"
            Write-Warning "Toasts will fall back to native WinRT (attributed to PowerShell). Or set NtfyUrl in the config."
        }
    } else {
        Write-Step "BurntToast already available."
    }
}

Write-Step "Registering scheduled task '$TaskName' (interactive session, every 5 min)..."
$action = New-ScheduledTaskAction -Execute 'powershell.exe' `
    -Argument "-NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$ScriptDst`""

$triggerRepeat = New-ScheduledTaskTrigger -Once -At (Get-Date) `
    -RepetitionInterval (New-TimeSpan -Minutes 5)
$triggerLogon = New-ScheduledTaskTrigger -AtLogOn -User "$env:USERDOMAIN\$env:USERNAME"

$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 4) `
    -MultipleInstances IgnoreNew

$principal = New-ScheduledTaskPrincipal `
    -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel Limited

Register-ScheduledTask -TaskName $TaskName -Action $action `
    -Trigger @($triggerRepeat, $triggerLogon) -Settings $settings -Principal $principal -Force | Out-Null

Write-Step "Running once now to verify..."
Start-ScheduledTask -TaskName $TaskName
Start-Sleep -Seconds 4
Get-Content -LiteralPath (Join-Path $LogDir 'health.log') -Tail 8 -ErrorAction SilentlyContinue

Write-Host ""
Write-Step "Done. The first 7-day calibration window is silent (logs only)."
Write-Step "Verify:  Get-ScheduledTask -TaskName $TaskName"
Write-Step "Test:    .\Install-WinHealthCheck.ps1 -Test"
Write-Step "Silence: New-Item -ItemType File -Force -Path '$(Join-Path $StateDir 'silent')'"
Write-Step "Remove:  .\Install-WinHealthCheck.ps1 -Uninstall"
