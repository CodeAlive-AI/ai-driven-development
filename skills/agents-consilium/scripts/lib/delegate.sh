#!/bin/bash
#
# delegate — full-YOLO single-agent task execution in the caller's CWD.
# Invoked by: scripts/consilium delegate -a <exact-agent-id> ...
#             scripts/consilium delegate --one-shot -a <id> ...
#             scripts/consilium delegate steer|status|cancel ...
#
# No sandbox, no approval prompts, no extra confirmation flag.
# Exact agent id only — no globs, no defaults.
#
set -euo pipefail

LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "$LIB_DIR/common.sh"
# shellcheck source=config.sh
source "$LIB_DIR/config.sh"
# shellcheck source=progress.sh
source "$LIB_DIR/progress.sh"
# shellcheck source=artifacts.sh
source "$LIB_DIR/artifacts.sh"

STEER_PY="$LIB_DIR/steer"
export PYTHONPATH="${LIB_DIR}${PYTHONPATH:+:$PYTHONPATH}"

# Control subcommands. A case is required rather than a run-id-shaped test:
# `list` takes no run id. There is no ambiguity with a start invocation —
# starting always requires -a <agent-id>, so an agent id never lands here.
case "${1:-}" in
    steer|status|cancel|wait|watch|list)
        sub="$1"
        shift
        exec python3 -m steer.control "$sub" "$@"
        ;;
esac

AGENT_ID=""
PROMPT=""
PROMPT_FILE=""
STEERABLE=1
LAUNCH_MODE="default"
DETACH=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        -a|--agent|--agents)
            shift
            if [[ -z "${1:-}" ]]; then
                echo "Error: -a requires an exact agent id" >&2
                exit $EXIT_USAGE
            fi
            # Reject globs and commas — exact id only
            if [[ "$1" == *'*'* || "$1" == *'?'* || "$1" == *','* || "$1" == *'['* ]]; then
                echo "Error: delegate requires an exact agent id (no globs/lists). Got: $1" >&2
                exit $EXIT_USAGE
            fi
            if [[ -n "$AGENT_ID" ]]; then
                echo "Error: delegate accepts exactly one -a <agent-id>" >&2
                exit $EXIT_USAGE
            fi
            AGENT_ID="$1"
            shift
            ;;
        --steerable)
            if [[ "$LAUNCH_MODE" == "one-shot" ]]; then
                echo "Error: --steerable and --one-shot are mutually exclusive" >&2
                exit $EXIT_USAGE
            fi
            STEERABLE=1
            LAUNCH_MODE="steerable"
            shift
            ;;
        --one-shot)
            if [[ "$LAUNCH_MODE" == "steerable" ]]; then
                echo "Error: --steerable and --one-shot are mutually exclusive" >&2
                exit $EXIT_USAGE
            fi
            STEERABLE=0
            LAUNCH_MODE="one-shot"
            shift
            ;;
        --detach)
            DETACH=1
            shift
            ;;
        --prompt-file)
            shift; PROMPT_FILE="${1:-}"; shift
            ;;
        -h|--help)
            cat <<'EOF'
Usage:
  consilium delegate -a <exact-agent-id> ["task"]
  consilium delegate -a <exact-agent-id> --one-shot ["task"]
  consilium delegate -a <exact-agent-id> --detach ["task"]
  consilium delegate steer RUN_ID [--mode auto|queue|interrupt] [--prompt-file FILE] "guidance"
  consilium delegate status RUN_ID [--json]
  consilium delegate cancel RUN_ID
  consilium delegate wait RUN_ID [--json] [--quiet]
  consilium delegate watch RUN_ID [--heartbeat SEC] [--json]
  consilium delegate list [--active|--all] [--reap] [--json]

Full-YOLO delegation to exactly one agent in the current working directory.
No sandbox, no approval prompts. Gemini is not supported (review-only).

Delegate starts a long-lived steerable supervisor by default, with a filesystem
mailbox for steer / status / cancel. --one-shot selects the legacy direct run.

--detach keeps the default steerable mode, prints run_id on stdout, and returns immediately.
The supervisor becomes its own session leader, so the run survives the caller
exiting. Collect the answer later with `delegate wait RUN_ID`.

wait blocks until the run is terminal and prints the full final answer.
Exit: 0 completed, 130 cancelled, 70 supervisor died, 74 completed but no
answer text, otherwise the agent's own failure code.

watch streams lifecycle changes and heartbeats, not tool/file/text progress,
and exits with the same codes. Use wait to print the final answer.
list finds runs again when the run id was lost.

Options:
  -a, --agent <id>       Exact agent id from config.json (required for start)
  --steerable            Explicit alias for the default steerable session
  --one-shot             Direct non-steerable run
  --detach               Start the steerable session detached; print run_id and exit
  --prompt-file <path>   Task / guidance from file
  -h, --help
EOF
            exit $EXIT_OK
            ;;
        --) shift; PROMPT="${1:-}"; break ;;
        -*) echo "Error: unknown flag: $1" >&2; exit $EXIT_USAGE ;;
        *)  PROMPT="$1"; shift; break ;;
    esac
done

if [[ -z "$AGENT_ID" ]]; then
    echo "Error: delegate requires -a <exact-agent-id> (no default agent)" >&2
    exit $EXIT_USAGE
fi

# A detached run requires the steerable registry and cannot use the direct
# one-shot path.
if [[ "$DETACH" -eq 1 && "$STEERABLE" -ne 1 ]]; then
    echo "Error: --detach and --one-shot are mutually exclusive" >&2
    exit $EXIT_USAGE
fi

# Normalize every task source into one private temp file exactly once. This
# supports regular files, FIFOs, and pseudo-files such as /dev/stdin without a
# second read/cp (macOS fcopyfile rejects copying /dev/fd-backed stdin). It also
# preserves trailing newlines and keeps large bodies out of argv and env.
_del_prompt_tmp="$(mktemp "${TMPDIR:-/tmp}/consilium-delegate-task.XXXXXX")"
chmod 600 "$_del_prompt_tmp"
cleanup_delegate_prompt() { rm -f "$_del_prompt_tmp"; }
trap cleanup_delegate_prompt EXIT

if [[ -n "$PROMPT_FILE" ]]; then
    [[ -r "$PROMPT_FILE" ]] || { echo "Error: prompt source not readable: $PROMPT_FILE" >&2; exit $EXIT_USAGE; }
    if ! cat -- "$PROMPT_FILE" > "$_del_prompt_tmp"; then
        echo "Error: failed to read prompt source: $PROMPT_FILE" >&2
        exit $EXIT_USAGE
    fi
elif [[ -n "$PROMPT" ]]; then
    printf '%s' "$PROMPT" > "$_del_prompt_tmp"
elif [[ ! -t 0 ]]; then
    cat > "$_del_prompt_tmp"
fi

if [[ ! -s "$_del_prompt_tmp" ]]; then
    echo "Error: no task prompt provided" >&2
    exit $EXIT_USAGE
fi

config_validate || exit $EXIT_CONFIG_ERROR

# Exact id must exist
if ! BACKEND="$(config_get_field "$AGENT_ID" backend 2>/dev/null)"; then
    echo "Error: unknown agent id: $AGENT_ID" >&2
    exit $EXIT_CONFIG_ERROR
fi

# Reject review-only agents before creating artifacts or entering the Python
# supervisor. backend_run.sh repeats this as defense in depth for direct calls.
SUPPORTS_DELEGATE="$(config_get_field "$AGENT_ID" supports_delegate 2>/dev/null || true)"
if [[ "$BACKEND" == "gemini-cli" || "$SUPPORTS_DELEGATE" == "false" || "$SUPPORTS_DELEGATE" == "0" ]]; then
    echo "Error: agent '$AGENT_ID' is review-only (supports_delegate=false)" >&2
    exit $EXIT_CONFIG_ERROR
fi

export CONSILIUM_MODE="delegate"
export CONSILIUM_SINGLE_AGENT=1
artifacts_init_run "delegate"
if [[ "$STEERABLE" -eq 1 ]]; then
    progress_stage "delegate" "agent=$AGENT_ID cwd=$(pwd) steerable=1"
else
    progress_stage "delegate" "agent=$AGENT_ID cwd=$(pwd) one_shot=1"
fi

# Delegate sends the task as-is (no consilium review principles wrap that forbids writes)
export CONSILIUM_RAW_PROMPT=1

if [[ "$STEERABLE" -eq 1 ]]; then
    # Large prompts reach the supervisor through the normalized file only.
    # Protocol artifacts: use CONSILIUM_RUN_DIR only when ordinary archival is on.
    # With CONSILIUM_SAVE_OUTPUTS=0, artifacts_init_run clears RUN_DIR — never fall
    # back to project cwd (".") because that would write ./raw ./final.txt into the
    # user's tree. Empty artifacts-dir tells the supervisor to place protocol
    # artifacts under the private 0700 registry run dir (meta records the path).
    ART=""
    if [[ "${CONSILIUM_SAVE_OUTPUTS:-1}" != "0" && -n "${CONSILIUM_RUN_DIR:-}" ]]; then
        ART="$CONSILIUM_RUN_DIR"
    fi
    REG_ARGS=()
    if [[ -n "${CONSILIUM_STEER_DIR:-}" ]]; then
        REG_ARGS+=(--registry-root "$CONSILIUM_STEER_DIR")
    fi
    if [[ "$DETACH" -eq 1 ]]; then
        # Detached: stdio goes to a private log the supervisor relocates under
        # its own run dir once the run id exists. The answer is never read from
        # this log — run_dir/final.txt stays authoritative and `wait` serves it.
        _det_log="$(mktemp "${TMPDIR:-/tmp}/consilium-detach.XXXXXX")"
        _det_idf="$(mktemp "${TMPDIR:-/tmp}/consilium-detach-id.XXXXXX")"
        chmod 600 "$_det_log" "$_det_idf"
        _det_log_kept=0
        cleanup_detach() {
            [[ "$_det_log_kept" -eq 1 ]] || rm -f "$_det_log"
            rm -f "$_det_idf"
            cleanup_delegate_prompt
        }
        trap cleanup_detach EXIT

        python3 -m steer.supervisor \
            --agent-id "$AGENT_ID" \
            --task-file "$_del_prompt_tmp" \
            --cwd "$(pwd)" \
            --artifacts-dir "$ART" \
            --log-file "$_det_log" \
            --run-id-file "$_det_idf" \
            --detach-setsid \
            "${REG_ARGS[@]+"${REG_ARGS[@]}"}" \
            </dev/null >>"$_det_log" 2>&1 &
        _det_pid=$!
        disown "$_det_pid" 2>/dev/null || true

        # Block until the run id lands in the handshake file. This is
        # synchronisation, not polish: the supervisor reads the task file before
        # create_run, and our EXIT trap deletes that file the moment this script
        # returns. The log cannot serve as the handshake — the supervisor moves
        # it under the run dir as soon as the run id exists.
        _det_run_id=""
        while [[ -z "$_det_run_id" ]]; do
            _det_run_id="$(head -1 "$_det_idf" 2>/dev/null | tr -d '[:space:]' || true)"
            [[ -n "$_det_run_id" ]] && break
            if ! kill -0 "$_det_pid" 2>/dev/null; then
                # The supervisor may have finished a fast run and moved its log
                # already; only a genuinely absent id is a startup failure.
                _det_run_id="$(head -1 "$_det_idf" 2>/dev/null | tr -d '[:space:]' || true)"
                [[ -n "$_det_run_id" ]] && break
                echo "Error: detached supervisor exited before reporting a run id" >&2
                _det_log_kept=1
                tail -n 40 "$_det_log" >&2 2>/dev/null || true
                rm -f "$_det_log"
                exit $EXIT_GENERIC
            fi
            sleep 0.1
        done
        # The supervisor owns the log from here (it relocates it under the run
        # dir); never delete it on the way out.
        _det_log_kept=1

        progress_stage "delegate" "detached run_id=$_det_run_id"
        echo "run_id=$_det_run_id" >&2
        # stdout carries the run id alone so `RUN_ID=$(… --detach …)` works.
        echo "$_det_run_id"
        exit $EXIT_OK
    fi

    # Run supervisor in-process (foreground); prints run_id early on stderr
    # and final answer on stdout when complete.
    python3 -m steer.supervisor \
        --agent-id "$AGENT_ID" \
        --task-file "$_del_prompt_tmp" \
        --cwd "$(pwd)" \
        --artifacts-dir "$ART" \
        "${REG_ARGS[@]+"${REG_ARGS[@]}"}"
    exit $?
fi

# Always use the normalized file so backend_run never re-reads /dev/stdin,
# treats content as positional input, or places a large task in argv/env.
"$LIB_DIR/backend_run.sh" --mode delegate --agent-id "$AGENT_ID" --raw --prompt-file "$_del_prompt_tmp"
exit $?
