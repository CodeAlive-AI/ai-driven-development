#!/bin/bash
#
# delegate — full-YOLO single-agent task execution in the caller's CWD.
# Invoked by: scripts/consilium delegate -a <exact-agent-id> ...
#             scripts/consilium delegate --steerable -a <id> ...
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

# Subcommands: steer | status | cancel
if [[ "${1:-}" == "steer" || "${1:-}" == "status" || "${1:-}" == "cancel" ]]; then
    sub="$1"
    shift
    exec python3 -m steer.control "$sub" "$@"
fi

AGENT_ID=""
PROMPT=""
PROMPT_FILE=""
STEERABLE=0

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
            STEERABLE=1
            shift
            ;;
        --prompt-file)
            shift; PROMPT_FILE="${1:-}"; shift
            ;;
        -h|--help)
            cat <<'EOF'
Usage:
  consilium delegate -a <exact-agent-id> ["task"]
  consilium delegate -a <exact-agent-id> --steerable ["task"]
  consilium delegate steer RUN_ID [--mode auto|queue|interrupt] [--prompt-file FILE] "guidance"
  consilium delegate status RUN_ID [--json]
  consilium delegate cancel RUN_ID

Full-YOLO delegation to exactly one agent in the current working directory.
No sandbox, no approval prompts. Gemini is not supported (review-only).

--steerable starts a long-lived supervisor with a filesystem mailbox so you can
steer / status / cancel the same run. Normal (non-steerable) delegate is one-shot.

Options:
  -a, --agent <id>       Exact agent id from config.json (required for start)
  --steerable            Long-lived steerable session
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
progress_stage "delegate" "agent=$AGENT_ID cwd=$(pwd)${STEERABLE:+ steerable=1}"

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
