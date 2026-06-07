# win-health-check - configuration
# Dot-sourced by win-health-check.ps1 AFTER its built-in defaults, so anything
# set here overrides the default. Edit thresholds to match your machine.

$DiskVolume          = 'C:'   # drive letter to watch (e.g. 'C:')
$DiskCriticalPct     = 10     # CRITICAL: free disk space below this %
$CommitCriticalPct   = 90     # CRITICAL (primary mem signal): % Committed Bytes In Use above this
$MemFreeCriticalPct  = 5      # CRITICAL (confirmation): available physical RAM below this %
$CooldownMinutes     = 30     # minimum minutes between repeat alerts of the same key
$HysteresisReadings  = 3      # consecutive readings before alert (5 min x 3 = 15 min)
$CalibrationDays     = 7      # initial silent period (logs only, no notifications)

# Touch this file to silence alerts on demand (e.g. during heavy builds):
$SuppressFile = Join-Path $env:LOCALAPPDATA 'win-health\silent'

# Toast notifier: auto | burnttoast | winrt | none
#   auto -> BurntToast if installed, else native WinRT, else log-only.
$Notifier = 'auto'

# Optional ntfy.sh push (works from ANY session, including headless/SYSTEM where
# toasts cannot render). Leave empty to skip. Use a long unguessable topic.
#   $NtfyUrl = 'https://ntfy.sh/your-private-uuid-topic-here'
$NtfyUrl = ''

# Where the kernel writes minidumps (primary crash signal - cheap to poll).
$DumpDir = Join-Path $env:SystemRoot 'Minidump'
