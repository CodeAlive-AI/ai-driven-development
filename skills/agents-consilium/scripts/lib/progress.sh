#!/bin/bash
# Compact semantic live progress → stderr only.
# Never write progress to stdout (stdout is reserved for the final answer).
#
# Style is a process-wide contract shared with normalize_stream.py:
#   full     previews of thinking / answer deltas, per agent (default)
#   compact  content-free liveness counters only
#   none     silence — orchestrator stage lines included
# Callers set it once, before the first progress_* call, via progress_set_style.

progress_style() {
    printf '%s' "${CONSILIUM_PROGRESS_STYLE:-full}"
}

progress_enabled() {
    [[ "$(progress_style)" != "none" ]]
}

# progress_set_style <full|compact|none> [interval-seconds]
# Exports the style (and, for compact, the heartbeat interval) so every child —
# backend_run.sh, normalize_stream.py, nested fan-out layers — inherits it.
# Returns 1 on an unknown style so the caller can emit its own usage error.
progress_set_style() {
    local value="$1" interval="${2:-}"
    case "$value" in
        full)
            export CONSILIUM_PROGRESS_STYLE="full"
            ;;
        compact)
            export CONSILIUM_PROGRESS_STYLE="compact"
            export CONSILIUM_PROGRESS_INTERVAL="${interval:-${CONSILIUM_PROGRESS_INTERVAL:-10}}"
            ;;
        none)
            export CONSILIUM_PROGRESS_STYLE="none"
            ;;
        *)
            return 1
            ;;
    esac
}

progress_info() {
    progress_enabled || return 0
    local scope="$1"; shift
    printf '[consilium] %s %s\n' "$scope" "$*" >&2
}

progress_agent_start() {
    progress_enabled || return 0
    local agent_id="$1" backend="$2" mode="$3" model="${4:-}" effort="${5:-}"
    printf '[consilium] start agent=%s backend=%s mode=%s model=%s effort=%s\n' \
        "$agent_id" "$backend" "$mode" "$model" "$effort" >&2
}

progress_agent_event() {
    progress_enabled || return 0
    local agent_id="$1" typ="$2" preview="${3:-}"
    # Compact: truncate previews
    if [[ ${#preview} -gt 80 ]]; then
        preview="${preview:0:77}..."
    fi
    preview="${preview//$'\n'/ }"
    if [[ -n "$preview" ]]; then
        printf '[consilium] event agent=%s type=%s data=%s\n' "$agent_id" "$typ" "$preview" >&2
    else
        printf '[consilium] event agent=%s type=%s\n' "$agent_id" "$typ" >&2
    fi
}

progress_agent_done() {
    progress_enabled || return 0
    local agent_id="$1" status="$2" exit_code="${3:-0}"
    printf '[consilium] done agent=%s status=%s exit=%s\n' \
        "$agent_id" "$status" "$exit_code" >&2
}

progress_stage() {
    progress_enabled || return 0
    local stage="$1"; shift
    printf '[consilium] stage=%s %s\n' "$stage" "$*" >&2
}
