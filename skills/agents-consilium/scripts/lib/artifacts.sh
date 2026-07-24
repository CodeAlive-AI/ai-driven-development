#!/bin/bash
# Per-run artifact layout for agents-consilium.
#
# Layout:
#   $CONSILIUM_RUN_DIR/
#     meta.json
#     raw/<key>.jsonl          # backend raw stdout (structured when available)
#     normalized/<key>.jsonl   # normalized semantic events
#     final/<key>.txt          # final text answer per invocation
#     final.txt                # primary final answer (single-agent or combined)
#
# Keys identify the *invocation*, not only the agent id:
#   - ask / delegate: plain agent id (e.g. "grok") — one shot per agent
#   - code review (basic/specialists): "agent.role" (e.g. "codex.security")
#   - multi-stage discovery (super/ultra): explicit fan-out keys of the form
#     "<stage>.<index>.<agent>.<role>" passed via --artifact-key
#   - judge attempts: "judge.primary.<agent>" / "judge.fallback.<agent>"
# Fan-out layers always pass an explicit key. discovery-pass / judge-runner
# never rely on an ambient inherited CONSILIUM_ARTIFACT_KEY alone — if called
# without --artifact-key they choose an invocation-unique default.
# backend_run uses CONSILIUM_ARTIFACT_KEY when set, else agent id.
#
# Env:
#   CONSILIUM_OUTPUT_DIR  — parent for auto run dirs (default: ${TMPDIR}/agents-consilium-outputs)
#   CONSILIUM_RUN_DIR     — if set, use this directory (created if missing)
#   CONSILIUM_SAVE_OUTPUTS — set 0 to disable (no-op helpers)
#   CONSILIUM_ARTIFACT_KEY — per-invocation key set by fan-out callers (see backend_run.sh)

artifacts_init_run() {
    local mode="${1:-unknown}"
    if [[ "${CONSILIUM_SAVE_OUTPUTS:-1}" == "0" ]]; then
        CONSILIUM_RUN_DIR=""
        export CONSILIUM_RUN_DIR
        return 0
    fi
    if [[ -z "${CONSILIUM_RUN_DIR:-}" ]]; then
        local parent="${CONSILIUM_OUTPUT_DIR:-${TMPDIR:-/tmp}/agents-consilium-outputs}"
        mkdir -p "$parent"
        CONSILIUM_RUN_DIR="$(mktemp -d "${parent%/}/run-${mode}.XXXXXX")"
    else
        mkdir -p "$CONSILIUM_RUN_DIR"
    fi
    mkdir -p "$CONSILIUM_RUN_DIR/raw" "$CONSILIUM_RUN_DIR/normalized" "$CONSILIUM_RUN_DIR/final"
    export CONSILIUM_RUN_DIR
    python3 -c '
import json, os, time
path = os.path.join(os.environ["CONSILIUM_RUN_DIR"], "meta.json")
meta = {
    "mode": os.environ.get("CONSILIUM_MODE", ""),
    "cwd": os.getcwd(),
    "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "pid": os.getpid(),
}
with open(path, "w") as f:
    json.dump(meta, f, indent=2)
    f.write("\n")
' 2>/dev/null || true
    if declare -F progress_info >/dev/null 2>&1; then
        progress_info "artifacts" "run_dir=$CONSILIUM_RUN_DIR"
    fi
}

artifacts_paths_for() {
    # Sets: ART_RAW ART_NORM ART_FINAL for invocation key $1
    # Key is agent id, agent.role, or a fan-out key (stage.index.agent.role / judge.*).
    local key="$1"
    local safe
    safe="$(printf '%s' "$key" | LC_ALL=C tr -c 'A-Za-z0-9._-' '_')"
    if [[ -z "${CONSILIUM_RUN_DIR:-}" || "${CONSILIUM_SAVE_OUTPUTS:-1}" == "0" ]]; then
        ART_RAW=""
        ART_NORM=""
        ART_FINAL=""
        return 0
    fi
    mkdir -p "$CONSILIUM_RUN_DIR/raw" "$CONSILIUM_RUN_DIR/normalized" "$CONSILIUM_RUN_DIR/final"
    ART_RAW="$CONSILIUM_RUN_DIR/raw/${safe}.jsonl"
    ART_NORM="$CONSILIUM_RUN_DIR/normalized/${safe}.jsonl"
    ART_FINAL="$CONSILIUM_RUN_DIR/final/${safe}.txt"
}

artifacts_write_final() {
    local key="$1"
    local text_file="$2"
    artifacts_paths_for "$key"
    if [[ -n "$ART_FINAL" && -f "$text_file" ]]; then
        cp "$text_file" "$ART_FINAL"
        # Primary final.txt = last successful single-agent answer, or first write
        if [[ ! -f "$CONSILIUM_RUN_DIR/final.txt" ]]; then
            cp "$text_file" "$CONSILIUM_RUN_DIR/final.txt"
        else
            # For multi-agent, overwrite with combined marker only if single-agent mode
            if [[ "${CONSILIUM_SINGLE_AGENT:-}" == "1" ]]; then
                cp "$text_file" "$CONSILIUM_RUN_DIR/final.txt"
            fi
        fi
    fi
}

artifacts_set_primary_final() {
    local text_file="$1"
    [[ -n "${CONSILIUM_RUN_DIR:-}" && -f "$text_file" ]] || return 0
    cp "$text_file" "$CONSILIUM_RUN_DIR/final.txt"
}
