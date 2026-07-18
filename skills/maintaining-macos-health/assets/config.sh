# Mac Health Check — config
# Override defaults here. Sourced by ~/bin/mac-health-check.

DISK_VOLUME=/System/Volumes/Data
DISK_CRITICAL_PCT=10        # CRITICAL: disk free below this %
SWAP_CRITICAL_GB=8          # used together with critical memory pressure
MEM_FREE_CRITICAL_PCT=10    # memory_pressure 'free %' below this
COOLDOWN_MINUTES=30         # min minutes between repeat alerts of same key
HYSTERESIS_READINGS=3       # consecutive readings before alert (5min × 3 = 15min)
CALIBRATION_DAYS=7          # initial silent period (logs only, no alerts)

# CPU monitoring for a developer workstation. The LaunchAgent runs every
# 5 minutes, so reading counts below also define the sustained duration.
CPU_ENABLED=1

# Whole-system utilization is 0..100% across all logical cores.
CPU_SYSTEM_BUSY_PCT=90
CPU_SYSTEM_BUSY_READINGS=3       # ~15 min; critical alert with sound

# Per-process %CPU is relative to one logical core and may exceed 100%.
CPU_PROCESS_HOT_PCT=80
CPU_PROCESS_HOT_READINGS=12      # ~1 hour; silent advisory
CPU_PROCESS_LEAK_PCT=40
CPU_PROCESS_LEAK_READINGS=72     # ~6 hours; silent advisory

# An incident closes only after sustained recovery. It sends no repeats while
# open, so these thresholds replace a CPU-specific notification cooldown.
CPU_PROCESS_RECOVERY_PCT=20
CPU_SYSTEM_RECOVERY_PCT=70
CPU_RECOVERY_READINGS=3
CPU_MAX_SAMPLE_GAP_MINUTES=15  # sleep/long pause resets consecutive readings

# Match executable basenames only. Ignored processes still appear in top-N
# diagnostics but cannot become the primary per-process advisory.
CPU_IGNORE_REGEX='^(kernel_task|WindowServer|mac-health-check|ps|iostat)$'

CPU_LOG_TOP_N=5
CPU_ALERT_TOP_N=3
CPU_INCIDENT_RETENTION_DAYS=30

# Local notification actions. Investigations are read-only. "Stop Process…"
# always asks for confirmation, revalidates PID identity/ownership/current CPU,
# sends SIGTERM first, and offers SIGKILL only after the grace period.
CPU_ACTIONS_ENABLED=1
CPU_PREFER_DESKTOP_APPS=1
CPU_STOP_ACTION_ENABLED=1
CPU_STOP_GRACE_SECONDS=10

# Path to "silence" flag — touch this file to disable alerts on demand
SUPPRESS_FILE="$HOME/.config/mac-health/silent"

# Optional ntfy.sh URL for phone push (leave empty to skip)
# NTFY_URL="https://ntfy.sh/your-private-uuid-topic-here"
NTFY_URL=""
