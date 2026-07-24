#!/bin/bash
# Compact semantic live progress → stderr only.
# Never write progress to stdout (stdout is reserved for the final answer).

progress_info() {
    local scope="$1"; shift
    printf '[consilium] %s %s\n' "$scope" "$*" >&2
}

progress_agent_start() {
    local agent_id="$1" backend="$2" mode="$3" model="${4:-}"
    printf '[consilium] start agent=%s backend=%s mode=%s model=%s\n' \
        "$agent_id" "$backend" "$mode" "$model" >&2
}

progress_agent_event() {
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
    local agent_id="$1" status="$2" exit_code="${3:-0}"
    printf '[consilium] done agent=%s status=%s exit=%s\n' \
        "$agent_id" "$status" "$exit_code" >&2
}

progress_stage() {
    local stage="$1"; shift
    printf '[consilium] stage=%s %s\n' "$stage" "$*" >&2
}
