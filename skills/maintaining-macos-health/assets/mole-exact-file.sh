#!/bin/bash
# Called only by disk_safety.Mole after module hash checks and file staging.
# No sudo, general clean, shell input, log rotation, or policy bypass.
set -euo pipefail
CORE="$1"
ORIGINAL="$2"
TARGET="$3"
[[ "$EUID" -ne 0 ]] || { printf '%s\n' 'Root execution refused' >&2; exit 1; }
if [[ "${MOLE_DRY_RUN:-0}" != "1" ]]; then
    [[ "$TARGET" == */.local/state/mac-health/disk-responses/*/holding/* ]] || {
        printf '%s\n' 'Apply target must be in the controller holding area' >&2; exit 1;
    }
fi
source "$CORE/base.sh"
# Mole's normal log module creates/rotates files in the user's log directory.
# The controller instead captures operations in its private incident audit.
readonly MOLE_LOG_LOADED=1
debug_log() { :; }
debug_file_action() { printf '%s\n' "$*"; }
log_error() { printf '%s\n' "$*" >&2; }
log_warning() { printf '%s\n' "$*" >&2; }
log_operation() { printf '%s\t' "$@"; printf '\n'; }
oplog_enabled() { return 1; }
source "$CORE/file_ops.sh"
source "$CORE/app_protection.sh"
WHITELIST_PATTERNS=("${DEFAULT_WHITELIST_PATTERNS[@]}")
WHITE="$HOME/.config/mole/whitelist"
if [[ -L "$WHITE" ]]; then
    log_error 'Symlinked Mole whitelist refused'; exit 1
fi
if [[ -e "$WHITE" ]]; then
    [[ -f "$WHITE" && -r "$WHITE" ]] || exit 1
    while IFS= read -r line || [[ -n "$line" ]]; do
        line="${line#"${line%%[![:space:]]*}"}"
        line="${line%"${line##*[![:space:]]}"}"
        [[ -z "$line" || "$line" == \#* ]] && continue
        [[ "$line" == "$FINDER_METADATA_SENTINEL" ]] && continue
        line="${line/#\~/$HOME}"
        line="${line//\$HOME/$HOME}"
        line="${line//\$\{HOME\}/$HOME}"
        [[ "$line" == /* && "$line" != *'..'* && ! "$line" =~ [[:cntrl:]] ]] || {
            log_error 'Unsupported whitelist syntax; refusing cleanup'; exit 1;
        }
        WHITELIST_PATTERNS+=("$line")
    done < "$WHITE"
fi
validate_path_for_deletion "$ORIGINAL"
if is_path_whitelisted "$ORIGINAL"; then
    log_error 'Original path protected by Mole whitelist'; exit 1
fi
[[ -f "$TARGET" && ! -L "$TARGET" ]] || exit 1
safe_remove "$TARGET" false
