#!/bin/bash
#
# delegate — full-YOLO single-agent task execution in the caller's CWD.
# Invoked by: scripts/consilium delegate -a <exact-agent-id> ...
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

AGENT_ID=""
PROMPT=""
PROMPT_FILE=""

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
        --prompt-file)
            shift; PROMPT_FILE="${1:-}"; shift
            ;;
        -h|--help)
            cat <<'EOF'
Usage: consilium delegate -a <exact-agent-id> ["task"]

Full-YOLO delegation to exactly one agent in the current working directory.
No sandbox, no approval prompts. Gemini is not supported (review-only).

Options:
  -a, --agent <id>       Exact agent id from config.json (required)
  --prompt-file <path>   Task prompt from file
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

if [[ -n "$PROMPT_FILE" ]]; then
    [[ -f "$PROMPT_FILE" ]] || { echo "Error: prompt file not found: $PROMPT_FILE" >&2; exit $EXIT_USAGE; }
    PROMPT="$(cat "$PROMPT_FILE")"
fi

if [[ -z "$PROMPT" && ! -t 0 ]]; then
    PROMPT="$(cat)"
fi
if [[ -z "$PROMPT" ]]; then
    echo "Error: no task prompt provided" >&2
    exit $EXIT_USAGE
fi

config_validate || exit $EXIT_CONFIG_ERROR

# Exact id must exist
if ! config_get_field "$AGENT_ID" backend >/dev/null 2>&1; then
    echo "Error: unknown agent id: $AGENT_ID" >&2
    exit $EXIT_CONFIG_ERROR
fi

export CONSILIUM_MODE="delegate"
export CONSILIUM_SINGLE_AGENT=1
artifacts_init_run "delegate"
progress_stage "delegate" "agent=$AGENT_ID cwd=$(pwd)"

# Delegate sends the task as-is (no consilium review principles wrap that forbids writes)
export CONSILIUM_RAW_PROMPT=1

# Prefer --prompt-file so backend_run does not treat file content as a
# positional prompt (avoids misleading shell-interpolation warnings).
if [[ -n "$PROMPT_FILE" ]]; then
    exec "$LIB_DIR/backend_run.sh" --mode delegate --agent-id "$AGENT_ID" --raw --prompt-file "$PROMPT_FILE"
else
    exec "$LIB_DIR/backend_run.sh" --mode delegate --agent-id "$AGENT_ID" --raw -- "$PROMPT"
fi
