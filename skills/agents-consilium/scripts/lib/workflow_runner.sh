#!/bin/bash
#
# workflow_runner.sh — reusable bounded fan-out runner for Consilium plans.
#
# Consumes declarative pass lines (from workflow_plans.py --shell) or is called
# by review_ask / review_code / review_super / review_ultra helpers.
#
# Concurrency:
#   CONSILIUM_MAX_PARALLEL=0   unlimited (default; historical behaviour)
#   CONSILIUM_MAX_PARALLEL=N   at most N concurrent background jobs
#
# Contract preserved:
#   - partial (exit 2) / all-failed (exit 3) via caller aggregation
#   - per-invocation artifact keys (never ambient alone)
#   - deterministic stage ordering (caller launches stages in order)
#   - live stderr via tee
#   - independent per-pass outputs
#
# Usage (launch one pass):
#   workflow_runner.sh launch-backend \
#     --mode review --agent-id ID [--role ROLE] [--artifact-key KEY] \
#     [--raw] --out OUT --err ERR < prompt
#
# Usage (await with optional concurrency already applied by launcher):
#   workflow_runner.sh await-pids --pids-file FILE --exits-file FILE
#
# Usage (bounded parallel launch of discovery passes):
#   workflow_runner.sh run-discovery-plan \
#     --plan-lines-file FILE --prompts-dir DIR \
#     --input-kind K --input-label L --input-body-file B \
#     --resp-dir DIR
#
set -euo pipefail

LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "$LIB_DIR/common.sh" 2>/dev/null || true

max_parallel() {
    local n="${CONSILIUM_MAX_PARALLEL:-0}"
    if ! [[ "$n" =~ ^[0-9]+$ ]]; then
        n=0
    fi
    printf '%s' "$n"
}

# Wait until fewer than N background jobs (of our tracked PIDs) are running.
# With N=0, never blocks (unlimited).
throttle() {
    local limit="$1"
    shift
    # remaining args: current pids (may be empty)
    if [[ "$limit" -eq 0 ]]; then
        return 0
    fi
    local -a pids=("$@")
    while true; do
        local alive=0
        local p
        for p in "${pids[@]:-}"; do
            [[ -z "$p" ]] && continue
            if kill -0 "$p" 2>/dev/null; then
                alive=$((alive + 1))
            fi
        done
        if [[ "$alive" -lt "$limit" ]]; then
            return 0
        fi
        sleep 0.05
    done
}

cmd_launch_backend() {
    local mode="" agent="" role="" art_key="" raw=0 out="" err=""
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --mode) mode="$2"; shift 2 ;;
            --agent-id) agent="$2"; shift 2 ;;
            --role) role="$2"; shift 2 ;;
            --artifact-key) art_key="$2"; shift 2 ;;
            --raw) raw=1; shift ;;
            --out) out="$2"; shift 2 ;;
            --err) err="$2"; shift 2 ;;
            *) echo "Error: unknown flag: $1" >&2; return 5 ;;
        esac
    done
    [[ -n "$mode" && -n "$agent" && -n "$out" && -n "$err" ]] || {
        echo "Error: launch-backend requires --mode --agent-id --out --err" >&2
        return 5
    }
    local -a extra=()
    [[ -n "$role" ]] && extra+=(--role "$role")
    [[ "$raw" -eq 1 ]] && extra+=(--raw)
    (
        set +e
        set +o pipefail
        export CONSILIUM_RUN_DIR="${CONSILIUM_RUN_DIR:-}"
        export CONSILIUM_SAVE_OUTPUTS="${CONSILIUM_SAVE_OUTPUTS:-}"
        if [[ -n "$art_key" ]]; then
            export CONSILIUM_ARTIFACT_KEY="$art_key"
        else
            unset CONSILIUM_ARTIFACT_KEY 2>/dev/null || true
        fi
        if [[ "$mode" == "review" && -z "${CONSILIUM_RAW_PROMPT:-}" ]]; then
            # discovery / code paths often skip Assessment template
            :
        fi
        "$LIB_DIR/backend_run.sh" \
            --mode "$mode" --agent-id "$agent" ${extra[@]+"${extra[@]}"} \
            2>&1 1>"$out" | tee "$err" >&2
        ps=("${PIPESTATUS[@]}")
        exit "${ps[0]}"
    )
}

# Await every tracked pid; append exit codes into named arrays by reference
# via globals _WR_SUCCEEDED / _WR_FAILED and list of outs already known.
_await_stage_pids() {
    local -a stage_pids=("$@")
    local p code
    for p in "${stage_pids[@]:-}"; do
        [[ -z "$p" ]] && continue
        code=0
        wait "$p" || code=$?
        if [[ $code -eq 0 ]]; then
            _WR_SUCCEEDED=$((_WR_SUCCEEDED + 1))
        else
            _WR_FAILED=$((_WR_FAILED + 1))
        fi
    done
}

cmd_run_discovery_plan() {
    local plan_file="" prompts_dir="" input_kind="" input_label="" input_body="" resp_dir=""
    local stage_barriers=1
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --plan-lines-file) plan_file="$2"; shift 2 ;;
            --prompts-dir) prompts_dir="$2"; shift 2 ;;
            --input-kind) input_kind="$2"; shift 2 ;;
            --input-label) input_label="$2"; shift 2 ;;
            --input-body-file) input_body="$2"; shift 2 ;;
            --resp-dir) resp_dir="$2"; shift 2 ;;
            # Explicit opt-out if a caller wants a single flattened wave.
            --no-stage-barriers) stage_barriers=0; shift ;;
            *) echo "Error: unknown flag: $1" >&2; return 5 ;;
        esac
    done
    [[ -f "$plan_file" && -n "$prompts_dir" && -n "$resp_dir" ]] || {
        echo "Error: run-discovery-plan missing required args" >&2
        return 5
    }
    mkdir -p "$resp_dir"
    local limit
    limit="$(max_parallel)"
    local -a pids=()
    local -a stage_pids=()
    local -a labels=()
    local -a outs=()
    local line stage index agent role cap prompt art_key out_file
    local current_stage=""
    _WR_SUCCEEDED=0
    _WR_FAILED=0

    while IFS= read -r line || [[ -n "$line" ]]; do
        [[ -z "$line" || "$line" == \#* ]] && continue
        IFS='|' read -r stage index agent role cap prompt art_key <<< "$line"
        [[ -z "$agent" || -z "$role" ]] && continue

        # Stage barrier: when the plan declares a new stage id, wait for the
        # previous stage's PIDs before launching more. Sequential stages (e.g.
        # probe after specialists) must not be flattened into one wave.
        if [[ "$stage_barriers" -eq 1 && -n "$current_stage" && "$stage" != "$current_stage" ]]; then
            _await_stage_pids "${stage_pids[@]:-}"
            stage_pids=()
        fi
        current_stage="$stage"

        # Unique out path: include index so multi-role same agent/stage does not clobber.
        out_file="$resp_dir/${stage}.${index}.${agent}.${role}.xml"
        # Backpressure within the current stage only.
        if [[ "$limit" -gt 0 ]]; then
            while true; do
                local alive=0 p
                for p in "${stage_pids[@]:-}"; do
                    [[ -n "$p" ]] && kill -0 "$p" 2>/dev/null && alive=$((alive + 1))
                done
                [[ "$alive" -lt "$limit" ]] && break
                sleep 0.05
            done
        fi
        "$LIB_DIR/discovery-pass.sh" \
            --agent "$agent" --role "$role" --cap "${cap:-uncapped}" \
            --prompt "$prompts_dir/${prompt}" \
            --input-kind "$input_kind" \
            --input-label "$input_label" \
            --input-body-file "$input_body" \
            --out "$out_file" \
            --artifact-key "$art_key" &
        pids+=("$!")
        stage_pids+=("$!")
        labels+=("$stage:$agent/$role")
        outs+=("$out_file")
    done < "$plan_file"

    # Drain the final stage.
    _await_stage_pids "${stage_pids[@]:-}"

    local succeeded=$_WR_SUCCEEDED failed=$_WR_FAILED i
    # Emit machine-readable summary for callers.
    printf 'succeeded=%s\n' "$succeeded"
    printf 'failed=%s\n' "$failed"
    printf 'total=%s\n' "${#pids[@]}"
    for i in "${!outs[@]}"; do
        printf 'out=%s\n' "${outs[$i]}"
    done

    if [[ $succeeded -eq 0 ]]; then
        return 3
    fi
    if [[ $failed -gt 0 ]]; then
        return 2
    fi
    return 0
}

cmd_emit_plan() {
    local plan_id="$1"
    shift
    python3 "$LIB_DIR/workflow_plans.py" "$plan_id" --shell "$@"
}

usage() {
    sed -n '2,40p' "$0"
}

main() {
    local cmd="${1:-}"
    shift || true
    case "$cmd" in
        launch-backend) cmd_launch_backend "$@" ;;
        run-discovery-plan) cmd_run_discovery_plan "$@" ;;
        emit-plan) cmd_emit_plan "$@" ;;
        max-parallel) max_parallel; echo ;;
        -h|--help|help|"") usage; return 0 ;;
        *) echo "Error: unknown command: $cmd" >&2; return 5 ;;
    esac
}

main "$@"
