#!/bin/bash
#
# Unified backend runner for agents-consilium v5.
#
# Usage:
#   backend_run.sh --mode review|explore|delegate --agent-id <id> [options] ["prompt"]
#   backend_run.sh --mode review --agent-id codex --prompt-file path.txt
#   echo "prompt" | backend_run.sh --mode review --agent-id codex
#
# Options:
#   --mode review|explore|delegate
#                            Required. review/explore = read-only; delegate = full YOLO.
#   --agent-id <id>          Required. Exact config agent id.
#   --role <role>            Override role from config.
#   --prompt-file <path>     Raw prompt from file (implies CONSILIUM_RAW_PROMPT=1).
#   --raw                    Send prompt without principles/role/template wrap.
#   --no-wrap                Alias for --raw.
#   -h, --help
#
# Env overrides (tests use these to inject fake CLIs):
#   CONSILIUM_BIN_CODEX / CONSILIUM_BIN_CLAUDE / CONSILIUM_BIN_OPENCODE
#   CONSILIUM_BIN_GEMINI / CONSILIUM_BIN_GROK
#   CONSILIUM_DUMP_ARGV=<path>  — if set, write the exact argv array as JSONL and exit 0
#                                 without executing (used by argv safety tests).
#
# Observability:
#   progress → stderr live while the model is still running (not post-hoc)
#   final answer text → stdout only
#   artifacts under $CONSILIUM_RUN_DIR when archival enabled
#
# Streaming architecture (structured backends):
#   prompt_file -> backend_cmd 2>stderr_file | normalize_stream.py --raw-out --progress --extract-text
#     • each raw stdout line is persisted immediately (--raw-out, flushed)
#     • each event is normalized and written immediately (stdout → NORM_STREAM)
#     • compact semantic progress reaches stderr before process completion
#   PIPESTATUS preserves backend exit/signal and normalizer validation
#   independently of pipefail rightmost-status semantics.
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

MODE=""
AGENT_ID=""
ROLE_OVERRIDE=""
PROMPT=""
PROMPT_FILE=""
PROMPT_SOURCE=""   # positional | file | stdin — shell-interpolation warn only for positional
RAW_MODE=0
DEBUG_EVENTS=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --mode)        MODE="${2:-}"; shift 2 ;;
        --agent-id)    AGENT_ID="${2:-}"; shift 2 ;;
        --role)        ROLE_OVERRIDE="${2:-}"; shift 2 ;;
        --prompt-file) PROMPT_FILE="${2:-}"; PROMPT_SOURCE="file"; shift 2 ;;
        --raw|--no-wrap) RAW_MODE=1; shift ;;
        --debug-events)
            if [[ -n "${2:-}" && "${2:-}" != -* ]]; then
                DEBUG_EVENTS="$2"; shift 2
            else
                DEBUG_EVENTS="__default__"; shift
            fi
            ;;
        --debug-events=*) DEBUG_EVENTS="${1#--debug-events=}"; shift ;;
        -h|--help)     sed -n '2,40p' "$0"; exit $EXIT_OK ;;
        --)            shift; PROMPT="${1:-}"; PROMPT_SOURCE="positional"; break ;;
        -*)            echo "Error: unknown flag: $1" >&2; exit $EXIT_USAGE ;;
        *)             PROMPT="$1"; PROMPT_SOURCE="positional"; shift; break ;;
    esac
done

[[ -n "$MODE" ]] || { echo "Error: --mode required (review|explore|delegate)" >&2; exit $EXIT_USAGE; }
# Explicit mode→capability matrix (fail closed for unknown modes).
# access_class is the coarse readonly|yolo switch; full matrix fields
# (filesystem/shell/web/memory/subagents) also drive backend-specific argv
# where the backend can enforce them.
MODE_CAPS_JSON="$(
    python3 "$LIB_DIR/mode_policy.py" "$MODE" --json 2>/dev/null
)" || {
    echo "Error: --mode must be a known Consilium mode (review|explore|delegate|…); got: $MODE" >&2
    exit $EXIT_USAGE
}
ACCESS_POLICY="$(
    MODE_CAPS_JSON="$MODE_CAPS_JSON" python3 -c 'import json,os; print(json.loads(os.environ["MODE_CAPS_JSON"])["access_class"])'
)"
MODE_CAP_WEB="$(
    MODE_CAPS_JSON="$MODE_CAPS_JSON" python3 -c 'import json,os; print("true" if json.loads(os.environ["MODE_CAPS_JSON"]).get("web") else "false")'
)"
MODE_CAP_MEMORY="$(
    MODE_CAPS_JSON="$MODE_CAPS_JSON" python3 -c 'import json,os; print("true" if json.loads(os.environ["MODE_CAPS_JSON"]).get("memory") else "false")'
)"
MODE_CAP_SUBAGENTS="$(
    MODE_CAPS_JSON="$MODE_CAPS_JSON" python3 -c 'import json,os; print("true" if json.loads(os.environ["MODE_CAPS_JSON"]).get("subagents") else "false")'
)"
MODE_CAP_SHELL="$(
    MODE_CAPS_JSON="$MODE_CAPS_JSON" python3 -c 'import json,os; print("true" if json.loads(os.environ["MODE_CAPS_JSON"]).get("shell") else "false")'
)"
MODE_CAP_FILESYSTEM="$(
    MODE_CAPS_JSON="$MODE_CAPS_JSON" python3 -c 'import json,os; print(json.loads(os.environ["MODE_CAPS_JSON"]).get("filesystem") or "read")'
)"
[[ -n "$AGENT_ID" ]] || { echo "Error: --agent-id required" >&2; exit $EXIT_USAGE; }

config_validate || exit $EXIT_CONFIG_ERROR

# Shared backend contract: identity, model/effort, binary, capabilities.
# Falls back to config.sh fields if the resolver fails (should not happen).
_RESOLVE_ARGS=(resolve "$AGENT_ID" --mode "$MODE")
if [[ "$MODE" == "delegate" ]]; then
    _RESOLVE_ARGS+=(--require-delegate)
fi
RESOLVED_JSON="$(
    python3 "$LIB_DIR/backend_contract.py" "${_RESOLVE_ARGS[@]}" 2>/dev/null
)" || RESOLVED_JSON=""
unset _RESOLVE_ARGS

if [[ -n "$RESOLVED_JSON" ]]; then
    eval "$(
        RESOLVED_JSON="$RESOLVED_JSON" python3 - <<'PY'
import json, os, shlex
d = json.loads(os.environ["RESOLVED_JSON"])
def emit(k, v):
    print(f"{k}={shlex.quote('' if v is None else str(v))}")
emit("BACKEND", d.get("backend"))
emit("MODEL", d.get("model"))
emit("EFFORT", d.get("effort"))
emit("LABEL", d.get("label") or d.get("agent_id"))
emit("ROLE_ID", d.get("role") or "analyst")
emit("BIN", d.get("binary"))
emit("REVIEW_INSTRUCTIONS", d.get("review_instructions") or "")
emit("ACCESS_POLICY", d.get("access_class") or "")
PY
    )"
    ROLE_ID="${ROLE_OVERRIDE:-$ROLE_ID}"
    ROLE_ID="${ROLE_ID:-analyst}"
    if [[ "$MODE" != "review" ]]; then
        REVIEW_INSTRUCTIONS=""
    fi
else
    BACKEND="$(config_get_field "$AGENT_ID" backend)" || exit $EXIT_CONFIG_ERROR
    MODEL="$(config_get_field "$AGENT_ID" model)"
    LABEL="$(config_get_field "$AGENT_ID" label)"; LABEL="${LABEL:-$AGENT_ID}"
    EFFORT="$(config_get_field "$AGENT_ID" effort)"
    ROLE_ID="${ROLE_OVERRIDE:-$(config_get_field "$AGENT_ID" role)}"
    ROLE_ID="${ROLE_ID:-analyst}"
    REVIEW_INSTRUCTIONS=""
    if [[ "$MODE" == "review" ]]; then
        REVIEW_INSTRUCTIONS="$(config_get_field "$AGENT_ID" review_instructions)"
    fi
    case "$BACKEND" in
        codex-cli)
            MODEL="${CODEX_MODEL:-$MODEL}"
            EFFORT="${CODEX_EFFORT:-$EFFORT}"
            ;;
        claude-code)
            MODEL="${CLAUDE_MODEL:-$MODEL}"
            EFFORT="${CLAUDE_EFFORT:-$EFFORT}"
            ;;
        opencode)
            MODEL="${OPENCODE_MODEL:-$MODEL}"
            EFFORT="${OPENCODE_EFFORT:-$EFFORT}"
            ;;
        grok-build)
            MODEL="${GROK_MODEL:-$MODEL}"
            EFFORT="${GROK_EFFORT:-$EFFORT}"
            ;;
        gemini-cli)
            MODEL="${GEMINI_MODEL:-$MODEL}"
            ;;
    esac
    BIN=""
fi

if [[ "$MODE" == "delegate" ]]; then
    if [[ "$BACKEND" == "gemini-cli" ]]; then
        echo "Error: agent '$AGENT_ID' backend gemini-cli is review-only; cannot delegate" >&2
        exit $EXIT_CONFIG_ERROR
    fi
    supports="$(config_get_field "$AGENT_ID" supports_delegate 2>/dev/null || true)"
    if [[ "$supports" == "false" || "$supports" == "0" ]]; then
        echo "Error: agent '$AGENT_ID' has supports_delegate=false" >&2
        exit $EXIT_CONFIG_ERROR
    fi
fi

if [[ -n "$PROMPT_FILE" ]]; then
    [[ -f "$PROMPT_FILE" ]] || { echo "Error: prompt file not found: $PROMPT_FILE" >&2; exit $EXIT_USAGE; }
    PROMPT="$(cat "$PROMPT_FILE")"
    RAW_MODE=1
    PROMPT_SOURCE="file"
fi

if [[ -z "$PROMPT" && ! -t 0 ]]; then
    PROMPT="$(cat)"
    PROMPT_SOURCE="stdin"
fi
[[ -n "$PROMPT" ]] || { echo "Error: no prompt provided" >&2; exit $EXIT_USAGE; }

# Only warn for unsafe positional-prompt usage. File/stdin content often
# legitimately contains backticks / $(...) from code samples.
if [[ "$PROMPT_SOURCE" == "positional" ]]; then
    warn_shell_special_in_prompt "$PROMPT"
fi

# Drop any inherited FULL_PROMPT *before* assigning. In bash, assigning to a
# name that arrived exported keeps the export attribute — which would put the
# full prompt body back into the child environment and hit ARG_MAX/E2BIG.
unset FULL_PROMPT 2>/dev/null || true

# Stage prompt bodies on disk before the pipeline — never put large text in env.
_PROMPT_STAGE_DIR="$(mktemp -d "${TMPDIR:-/tmp}/consilium-prompt.XXXXXX")"
_PROMPT_USER_FILE="$_PROMPT_STAGE_DIR/user.txt"
_PROMPT_ROLE_FILE="$_PROMPT_STAGE_DIR/role.txt"
printf '%s' "$PROMPT" > "$_PROMPT_USER_FILE"

if [[ "$RAW_MODE" -eq 1 || -n "${CONSILIUM_RAW_PROMPT:-}" ]]; then
    export CONSILIUM_RAW_PROMPT=1
    FULL_PROMPT="$(
        python3 "$LIB_DIR/prompt_pipeline.py" --mode raw --raw --user-file "$_PROMPT_USER_FILE" 2>/dev/null \
        || cat "$_PROMPT_USER_FILE"
    )"
else
    if ! ROLE_PROMPT="$(get_role_prompt "$ROLE_ID")"; then
        rm -rf "$_PROMPT_STAGE_DIR"
        echo "Error: unknown role '$ROLE_ID' for agent $AGENT_ID" >&2
        exit $EXIT_CONFIG_ERROR
    fi
    printf '%s' "$ROLE_PROMPT" > "$_PROMPT_ROLE_FILE"
    if [[ -n "$REVIEW_INSTRUCTIONS" ]]; then
        {
            printf '%s' "$ROLE_PROMPT"
            printf '\n\nMODEL-SPECIFIC REVIEW INSTRUCTIONS:\n%s' "$REVIEW_INSTRUCTIONS"
        } > "$_PROMPT_ROLE_FILE"
    fi
    SKIP_TPL_ARGS=()
    if [[ -n "${CONSILIUM_SKIP_OUTPUT_TEMPLATE:-}" ]]; then
        SKIP_TPL_ARGS+=(--skip-output-template)
    fi
    PIPE_MODE="$MODE"
    if [[ -n "${CONSILIUM_SKIP_OUTPUT_TEMPLATE:-}" && "$MODE" == "review" ]]; then
        PIPE_MODE="review-code"
    fi
    FULL_PROMPT="$(
        python3 "$LIB_DIR/prompt_pipeline.py" \
            --mode "$PIPE_MODE" \
            --role-file "$_PROMPT_ROLE_FILE" \
            --user-file "$_PROMPT_USER_FILE" \
            ${SKIP_TPL_ARGS[@]+"${SKIP_TPL_ARGS[@]}"} \
            2>/dev/null
    )" || FULL_PROMPT=""
    if [[ -z "$FULL_PROMPT" ]]; then
        if [[ -n "$REVIEW_INSTRUCTIONS" ]]; then
            ROLE_PROMPT+=$'\n\nMODEL-SPECIFIC REVIEW INSTRUCTIONS:\n'
            ROLE_PROMPT+="$REVIEW_INSTRUCTIONS"
        fi
        FULL_PROMPT="$(build_prompt "$ROLE_PROMPT" "$PROMPT" </dev/null)"
    fi
fi
rm -rf "$_PROMPT_STAGE_DIR"
unset _PROMPT_STAGE_DIR _PROMPT_USER_FILE _PROMPT_ROLE_FILE
# NEVER export FULL_PROMPT — large prompts exceed ARG_MAX when copied into the
# environment (execve counts env + argv). Prompt bodies travel via temp file /
# stdin only.

# Resolve CLI binary if shared contract did not supply one.
bin_for() {
    case "$1" in
        codex-cli)   echo "${CONSILIUM_BIN_CODEX:-codex}" ;;
        claude-code) echo "${CONSILIUM_BIN_CLAUDE:-claude}" ;;
        opencode)    echo "${CONSILIUM_BIN_OPENCODE:-opencode}" ;;
        gemini-cli)  echo "${CONSILIUM_BIN_GEMINI:-gemini}" ;;
        grok-build)  echo "${CONSILIUM_BIN_GROK:-grok}" ;;
        *)           echo "" ;;
    esac
}

if [[ -z "${BIN:-}" ]]; then
    BIN="$(bin_for "$BACKEND")"
fi
if [[ -z "$BIN" ]]; then
    echo "Error: unknown backend '$BACKEND' for agent $AGENT_ID" >&2
    exit $EXIT_CONFIG_ERROR
fi
if ! command -v "$BIN" &>/dev/null && [[ ! -x "$BIN" ]]; then
    echo "Error: backend CLI not found: $BIN (backend=$BACKEND)" >&2
    exit $EXIT_CONFIG_ERROR
fi

# Codex model alias + default efforts are already applied by backend_contract
# when resolve succeeded; keep shell fallbacks for the legacy path.
if [[ "$BACKEND" == "codex-cli" && "$MODEL" == "gpt-5.6" ]]; then
    MODEL="gpt-5.6-sol"
fi
case "$BACKEND" in
    codex-cli|claude-code|grok-build) EFFORT="${EFFORT:-high}" ;;
    opencode)
        if [[ "$EFFORT" == "none" ]]; then EFFORT=""; fi
        ;;
esac

# Opt-in debug event tape (CLI or CONSILIUM_DEBUG_EVENTS=1).
if [[ -n "$DEBUG_EVENTS" ]]; then
    if [[ "$DEBUG_EVENTS" == "__default__" ]]; then
        export CONSILIUM_DEBUG_EVENTS=1
    else
        export CONSILIUM_DEBUG_EVENTS=1
        export CONSILIUM_DEBUG_EVENTS_PATH="$DEBUG_EVENTS"
    fi
fi

# Progress identity = the invocation, not just the agent. Fan-out layers run the
# same agent in several roles/stages concurrently; without the key their live
# lines are indistinguishable. Artifact paths reuse the same value below.
PROGRESS_ID="${CONSILIUM_ARTIFACT_KEY:-$AGENT_ID}"
progress_agent_start "$PROGRESS_ID" "$BACKEND" "$MODE" "$MODEL" "$EFFORT"

# Ensure run dir + artifact subdirs exist (honors pre-set CONSILIUM_RUN_DIR)
if [[ "${CONSILIUM_SAVE_OUTPUTS:-1}" != "0" ]]; then
    if [[ -z "${CONSILIUM_RUN_DIR:-}" ]]; then
        artifacts_init_run "$MODE"
    else
        mkdir -p "$CONSILIUM_RUN_DIR/raw" "$CONSILIUM_RUN_DIR/normalized" "$CONSILIUM_RUN_DIR/final"
        export CONSILIUM_RUN_DIR
    fi
fi
# Artifact key identifies this invocation. Fan-out callers set an explicit
# CONSILIUM_ARTIFACT_KEY (e.g. "codex.security", "discovery-small.0.x.analyst",
# "judge.primary.claude-code"). Ordinary ask/delegate leave it unset → agent id.
ARTIFACT_KEY="$PROGRESS_ID"
artifacts_paths_for "$ARTIFACT_KEY"

# Build argv into array CMD
CMD=()
PROMPT_VIA_FILE=0
PROMPT_FILE_PATH=""
RUNTIME_SETTINGS_FILE=""

build_cmd_codex() {
    local approval_sandbox
    CMD=("$BIN")
    # Top-level -a is ask-for-approval
    if [[ "$ACCESS_POLICY" == "readonly" ]]; then
        CMD+=(--disable multi_agent --disable multi_agent_v2)
        if [[ "${MODE_CAP_WEB:-true}" == "true" || "${MODE_CAP_WEB:-1}" == "1" ]]; then
            CMD+=(--search)
        fi
        CMD+=(-a never)
        if [[ -n "$EFFORT" ]]; then
            CMD+=(-c "model_reasoning_effort=\"$EFFORT\"")
        fi
        CMD+=(exec --model "$MODEL" --sandbox read-only --skip-git-repo-check --ephemeral)
        if [[ -n "${CONSILIUM_CODEX_NO_MCP:-}" ]]; then
            CMD+=(--ignore-user-config)
        fi
        # Structured events for observability; final text via -o
        CMD+=(--json)
    else
        # delegate YOLO: full bypass, no sandbox
        if [[ -n "$EFFORT" ]]; then
            CMD+=(-c "model_reasoning_effort=\"$EFFORT\"")
        fi
        CMD+=(exec --model "$MODEL" --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check)
        CMD+=(--json)
    fi
    # Prompt + last message file filled at run time via placeholders handled below
}

build_cmd_claude() {
    # -p enables headless print mode; the complete prompt is read from stdin.
    # Review uses Claude's normal tool loop, not its plan workflow.
    CMD=("$BIN")
    if [[ "$ACCESS_POLICY" == "readonly" ]]; then
        # `plan` is the wrong workflow for an independent review: Claude Code
        # deliberately creates a plan artifact under ~/.claude/plans. dontAsk
        # stays non-interactive without activating that workflow. Dedicated
        # edit tools remain unavailable; Bash is trusted to follow the review
        # prompt's report-only contract so git/rg/test diagnostics still work.
        CMD+=(--permission-mode dontAsk)
        # Preserve the full review loop while disabling project/user
        # customizations, hooks, MCP, custom agents, browser integration, and
        # on-disk session history. Unlike --bare, safe-mode does not force an
        # API-key-only authentication path.
        CMD+=(--safe-mode --no-session-persistence --no-chrome)
        CMD+=(--disallowedTools "Edit,Write,NotebookEdit,Agent,Task")
        if [[ "${MODE_CAP_WEB:-true}" == "true" || "${MODE_CAP_WEB:-1}" == "1" ]]; then
            CMD+=(--allowedTools "Bash,WebSearch,WebFetch")
        else
            CMD+=(--allowedTools "Bash")
        fi
    else
        CMD+=(--dangerously-skip-permissions)
    fi
    CMD+=(--model "$MODEL")
    if [[ -n "$EFFORT" ]]; then
        CMD+=(--effort "$EFFORT")
    fi
    # Prefer stream-json for observability when not dumping argv only
    if [[ -z "${CONSILIUM_DUMP_ARGV:-}" ]]; then
        CMD+=(--output-format stream-json --verbose)
    else
        CMD+=(--output-format text)
    fi
    CMD+=(-p)
}

build_cmd_opencode() {
    CMD=("$BIN" run --pure)
    if [[ "$ACCESS_POLICY" == "readonly" ]]; then
        # The built-in plan agent is a planning workflow with its own plan-file
        # permissions. Review needs the full analysis/tool loop instead. Define
        # a primary review agent at runtime: full shell/search, no edits or task
        # delegation. The trusted prompt carries the report-only contract.
        export OPENCODE_CONFIG_CONTENT='{"agent":{"consilium-review":{"description":"Independent read-only review performed without delegation","prompt":"Review independently and read-only. Work alone: never use task delegation, subagents, other models, or external workers. Use Bash, search, and read tools to inspect any repository files needed for the real blast radius. Return only the report; never modify files or external state.","mode":"primary","permission":{"edit":"deny","task":"deny","bash":"allow","read":"allow","glob":"allow","grep":"allow","list":"allow","lsp":"allow","webfetch":"allow","websearch":"allow"}}}}'
        CMD+=(--agent consilium-review --auto)
    else
        # --auto is current (opencode run --help): auto-approve non-denied permissions
        CMD+=(--agent build --auto)
    fi
    CMD+=(-m "$MODEL")
    if [[ -n "$EFFORT" ]]; then
        CMD+=(--variant "$EFFORT")
    fi
    if [[ -z "${CONSILIUM_DUMP_ARGV:-}" ]]; then
        CMD+=(--format json)
    else
        CMD+=(--format default)
    fi
}

build_cmd_gemini() {
    # Review only. Gemini Plan Mode is a planning workflow that writes a plan
    # artifact and restricts tools. YOLO keeps headless review fully capable;
    # extensions/MCP stay disabled and the trusted prompt forbids mutations and
    # delegation. Non-TTY stdin keeps the potentially large prompt off argv.
    # Gemini enables built-in subagents by default. A highest-precedence
    # temporary system settings file disables them for this invocation; `-e
    # none` is the documented way to disable every extension.
    RUNTIME_SETTINGS_FILE="$(mktemp "${TMPDIR:-/tmp}/consilium-gemini-settings.XXXXXX")"
    printf '%s\n' '{"experimental":{"enableAgents":false,"extensionManagement":false,"extensionConfig":false}}' > "$RUNTIME_SETTINGS_FILE"
    export GEMINI_CLI_SYSTEM_SETTINGS_PATH="$RUNTIME_SETTINGS_FILE"
    CMD=("$BIN" --model "$MODEL" --approval-mode yolo -o text -e none --allowed-mcp-server-names "")
}

build_cmd_grok() {
    # One-shot headless: --prompt-file is documented as "Single-turn prompt from a file"
    # (same headless class as -p/--single for inline prompts). Do not also pass -p;
    # --prompt-file alone selects single-turn non-TUI mode.
    # Mode capability fields memory/subagents/shell/filesystem/web drive argv
    # where Grok Build exposes matching flags.
    CMD=("$BIN")
    if [[ "$MODE" == "explore" ]]; then
        # Exploration may run over a repository nobody has vetted, so it keeps a
        # read-only posture and removes the channels through which that
        # repository could act rather than be read: no shell, no write tools, no
        # subagents, no cross-session memory. --cwd points at a neutral parent
        # for remote sources so the clone's own agent config is never discovered.
        #
        # Web search/fetch ARE granted: understanding a codebase routinely means
        # reading the docs, RFCs, and upstream issues it is built against. The
        # residual risk (repository text talking the model into fetching a URL)
        # is handled in prompts/explore.txt, which forbids acting on in-repo
        # instructions and forbids sending repository content to any URL the
        # repository itself supplied.
        CMD+=(--sandbox "${CONSILIUM_EXPLORE_SANDBOX:-read-only}")
        if [[ "${MODE_CAP_WEB:-true}" == "true" ]]; then
            CMD+=(--tools "read_file,grep,list_dir,web_search,web_fetch")
        else
            CMD+=(--tools "read_file,grep,list_dir")
        fi
        CMD+=(--disallowed-tools "search_replace,write,run_terminal_cmd,Agent")
        # mode_policy: explore memory=false, subagents=false
        CMD+=(--no-subagents --no-memory)
        if [[ -n "${CONSILIUM_EXPLORE_CWD:-}" ]]; then
            CMD+=(--cwd "$CONSILIUM_EXPLORE_CWD")
        fi
    elif [[ "$ACCESS_POLICY" == "readonly" ]]; then
        # Kernel sandbox + strict tool allowlist (plan mode alone is NOT read-only).
        # The allowlist is exhaustive, so web tools must be named explicitly —
        # verified against Grok Build 0.2.112: without them the model reports it
        # has no web tool, with them it retrieves and cites live sources.
        CMD+=(--sandbox read-only --no-plan)
        if [[ "${MODE_CAP_WEB:-true}" == "true" ]]; then
            CMD+=(--tools "read_file,grep,list_dir,run_terminal_cmd,web_search,web_fetch")
        else
            CMD+=(--tools "read_file,grep,list_dir,run_terminal_cmd")
        fi
        CMD+=(--disallowed-tools "search_replace,write,Agent")
        # mode_policy review: memory=false, subagents=false — enforce when
        # flags exist (Grok Build supports both).
        if [[ "${MODE_CAP_SUBAGENTS:-false}" != "true" ]]; then
            CMD+=(--no-subagents)
        fi
        if [[ "${MODE_CAP_MEMORY:-false}" != "true" ]]; then
            CMD+=(--no-memory)
        fi
    else
        # YOLO: always-approve, no sandbox flag (default off = unrestricted)
        CMD+=(--always-approve)
    fi
    CMD+=(-m "$MODEL")
    if [[ -n "$EFFORT" ]]; then
        CMD+=(--reasoning-effort "$EFFORT")
    fi
    CMD+=(--output-format streaming-json)
    CMD+=(--verbatim)
    PROMPT_VIA_FILE=1
}

case "$BACKEND" in
    codex-cli)   build_cmd_codex ;;
    claude-code) build_cmd_claude ;;
    opencode)    build_cmd_opencode ;;
    gemini-cli)  build_cmd_gemini ;;
    grok-build)  build_cmd_grok ;;
esac

# Argv dump mode for tests — exact safety properties without executing
if [[ -n "${CONSILIUM_DUMP_ARGV:-}" ]]; then
    dump_cmd=("${CMD[@]}")
    if [[ "$PROMPT_VIA_FILE" -eq 1 ]]; then
        dump_cmd+=(--prompt-file "__PROMPT_FILE__")
    elif [[ "$BACKEND" == "codex-cli" ]]; then
        dump_cmd+=(-o "__LAST_MSG__" -)
    fi
    printf '%s\0' "${dump_cmd[@]}" | AGENT_ID="$AGENT_ID" BACKEND="$BACKEND" MODE="$MODE" MODEL="$MODEL" DUMP_ARGV_PATH="$CONSILIUM_DUMP_ARGV" python3 -c '
import json, os, sys
data = sys.stdin.buffer.read().split(b"\0")
argv = [x.decode() for x in data if x != b""]
obj = {
    "agent_id": os.environ["AGENT_ID"],
    "backend": os.environ["BACKEND"],
    "mode": os.environ["MODE"],
    "model": os.environ["MODEL"],
    "argv": argv,
}
with open(os.environ["DUMP_ARGV_PATH"], "w") as f:
    json.dump(obj, f)
    f.write("\n")
'
    [[ -z "$RUNTIME_SETTINGS_FILE" ]] || rm -f "$RUNTIME_SETTINGS_FILE"
    exit $EXIT_OK
fi

# Prepare temp files
TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/consilium-backend.XXXXXX")"
cleanup_backend() {
    rm -rf "$TMP_DIR"
    [[ -z "$RUNTIME_SETTINGS_FILE" ]] || rm -f "$RUNTIME_SETTINGS_FILE"
}
trap cleanup_backend EXIT

RAW_STREAM="$TMP_DIR/raw.stream"
NORM_STREAM="$TMP_DIR/normalized.jsonl"
FINAL_TEXT="$TMP_DIR/final.txt"
LAST_MSG="$TMP_DIR/last-message.txt"
PROMPT_PATH="$TMP_DIR/prompt.txt"
printf '%s' "$FULL_PROMPT" > "$PROMPT_PATH"
# Free the shell variable and ensure it cannot appear in child environments.
unset FULL_PROMPT
# PROMPT may also be large (stdin/file path); keep for diagnostics only when small.
# Always clear export attribute on PROMPT too if a parent exported it.
if [[ ${#PROMPT} -gt 8192 ]]; then
    unset PROMPT
fi
BACKEND_ERR="$TMP_DIR/stderr.txt"
: > "$RAW_STREAM"
: > "$FINAL_TEXT"

redact_backend_stderr() {
    [[ -s "$BACKEND_ERR" ]] || return 0
    local redacted="$TMP_DIR/stderr.redacted.txt"
    if python3 "$LIB_DIR/redact_stream.py" \
        --input "$BACKEND_ERR" --output "$redacted"; then
        mv "$redacted" "$BACKEND_ERR"
    else
        # Fail closed for display: never print an unredacted backend diagnostic
        # merely because the redactor itself failed.
        printf '%s\n' '[backend stderr redaction failed; original diagnostic suppressed]' \
            > "$BACKEND_ERR"
    fi
}

# Unbuffered Python so progress/raw flushes reach the parent before backend exit.
export PYTHONUNBUFFERED=1

# Run a backend with concurrent line streaming through normalize_stream.py.
# The second argument is an optional stdin file. Remaining args are the full
# command argv (including binary). Large prompts never enter process argv.
# Sets: BACKEND_RC, NORM_RC (and writes RAW_STREAM, NORM_STREAM, FINAL_TEXT).
run_streamed() {
    local backend="$1"
    local stdin_file="$2"
    shift 2
    local -a run_argv=("$@")
    if [[ "$backend" == "opencode" ]]; then
        run_argv=(
            python3 "$LIB_DIR/terminal_guard.py"
            --backend opencode
            --terminal-grace "${CONSILIUM_TERMINAL_GRACE:-2}"
            -- "${run_argv[@]}"
        )
    fi
    local -a norm_argv=(
        python3 "$LIB_DIR/normalize_stream.py"
        --backend "$backend"
        --agent-id "$AGENT_ID"
        --model "$MODEL"
        --effort "$EFFORT"
        --access-policy "$ACCESS_POLICY"
        --input -
        --raw-out "$RAW_STREAM"
        --extract-text --text-out "$FINAL_TEXT"
        --progress
        --progress-id "$PROGRESS_ID"
    )
    # Every mode may pick a style: review defaults to full previews, explore uses
    # a content-free style so neither chain-of-thought nor the incrementally
    # streamed answer body can reach stderr, and none silences the stream.
    if [[ -n "${CONSILIUM_PROGRESS_STYLE:-}" ]]; then
        norm_argv+=(--progress-style "$CONSILIUM_PROGRESS_STYLE")
    fi
    if [[ -n "${CONSILIUM_PROGRESS_INTERVAL:-}" ]]; then
        norm_argv+=(--progress-interval "$CONSILIUM_PROGRESS_INTERVAL")
    fi
    if [[ -n "${CONSILIUM_DEBUG_EVENTS:-}" ]]; then
        if [[ -n "${CONSILIUM_DEBUG_EVENTS_PATH:-}" ]]; then
            norm_argv+=(--debug-events "$CONSILIUM_DEBUG_EVENTS_PATH")
        else
            norm_argv+=(--debug-events)
        fi
    fi
    if [[ "$backend" != "grok-build" ]]; then
        norm_argv+=(--no-validate)
    fi

    set +e
    # Disable pipefail for this pipeline so a mid-stream normalizer failure
    # does not hide the backend exit; we read PIPESTATUS explicitly.
    # Capture PIPESTATUS *immediately* after the pipeline — before any other
    # command (including `fi`) overwrites it.
    set +o pipefail
    local -a _ps
    if [[ -n "$stdin_file" ]]; then
        "${run_argv[@]}" <"$stdin_file" 2>"$BACKEND_ERR" \
            | "${norm_argv[@]}" >"$NORM_STREAM"
        _ps=("${PIPESTATUS[@]}")
    else
        "${run_argv[@]}" 2>"$BACKEND_ERR" \
            | "${norm_argv[@]}" >"$NORM_STREAM"
        _ps=("${PIPESTATUS[@]}")
    fi
    BACKEND_RC=${_ps[0]:-1}
    NORM_RC=${_ps[1]:-0}
    set -o pipefail
    set -e

    # Preserve backend PIPESTATUS when the normalizer also fails. Prefer the
    # backend non-zero (signal/crash) over a normalizer-only failure so
    # callers see the true process outcome. Grok contract additionally requires
    # end present / no error: if backend exited 0 but normalizer failed, surface 1.
    if [[ "${NORM_RC:-0}" -ne 0 && "${BACKEND_RC:-0}" -eq 0 ]]; then
        if [[ "$backend" == "grok-build" ]]; then
            BACKEND_RC=1
        fi
        # Other backends: normalizer failure alone does not rewrite a clean
        # backend exit unless Grok validation applies; PIPESTATUS[0] stays 0.
    fi
    # When both fail, keep BACKEND_RC as-is (already captured from PIPESTATUS[0]).
}

run_and_capture() {
    local exit_code=0
    BACKEND_RC=0
    NORM_RC=0

    case "$BACKEND" in
        codex-cli)
            run_streamed "codex-cli" "$PROMPT_PATH" "${CMD[@]}" -o "$LAST_MSG" -
            exit_code=$BACKEND_RC
            # Codex authoritative final message is -o last-message when present
            if [[ -s "$LAST_MSG" ]]; then
                cat "$LAST_MSG" > "$FINAL_TEXT"
            elif [[ ! -s "$FINAL_TEXT" && -s "$RAW_STREAM" ]]; then
                python3 "$LIB_DIR/normalize_stream.py" \
                    --backend codex-cli --agent-id "$AGENT_ID" \
                    --input "$RAW_STREAM" --extract-text --text-out "$FINAL_TEXT" \
                    --no-validate >/dev/null 2>/dev/null || true
            fi
            ;;
        claude-code)
            run_streamed "claude-code" "$PROMPT_PATH" "${CMD[@]}"
            exit_code=$BACKEND_RC
            # Shared assembly: authoritative non-empty result XOR deltas.
            # Empty/whitespace result must not erase non-empty answer deltas.
            # is_error/error results never become a successful answer body.
            claude_is_error=0
            if [[ -s "$NORM_STREAM" ]]; then
                if python3 -c '
import json,sys
for line in open(sys.argv[1], encoding="utf-8"):
    line=line.strip()
    if not line: continue
    try: o=json.loads(line)
    except Exception: continue
    if o.get("type")=="run_failed":
        sys.exit(0)
sys.exit(1)
' "$NORM_STREAM" 2>/dev/null; then
                    claude_is_error=1
                fi
                python3 -c '
import sys
sys.path.insert(0, sys.argv[3])
from events import assemble_final_text, ConsiliumEvent, EventValidationError
import json
evts=[]
saw_fail=False
for line in open(sys.argv[1], encoding="utf-8"):
    line=line.strip()
    if not line: continue
    try:
        o=json.loads(line)
        if o.get("type")=="run_failed":
            saw_fail=True
            continue
        evts.append(ConsiliumEvent.from_dict(o))
    except Exception:
        continue
# Forensic final may keep deltas for debugging, but is_error path must not
# promote a partial answer as the successful body when caller checks RC.
text = assemble_final_text(evts)
if text:
    open(sys.argv[2],"w",encoding="utf-8").write(text)
' "$NORM_STREAM" "$FINAL_TEXT" "$LIB_DIR" 2>/dev/null || true
            elif [[ -s "$RAW_STREAM" ]]; then
                python3 -c '
import json,sys
deltas=[]
result=None
is_err=False
for line in open(sys.argv[1]):
    line=line.strip()
    if not line: continue
    try:
        o=json.loads(line)
    except Exception:
        continue
    if o.get("type") in ("result", "result_success"):
        if o.get("is_error") or o.get("error"):
            is_err=True
            continue
        r=o.get("result")
        if isinstance(r, str) and r.strip():
            result=r
    elif o.get("type")=="content_block_delta":
        d=o.get("delta") or {}
        if d.get("type")=="text_delta":
            deltas.append(d.get("text",""))
text = result if result is not None else "".join(deltas)
if text:
    open(sys.argv[2],"w").write(text)
if is_err:
    open(sys.argv[2]+".is_error","w").write("1")
' "$RAW_STREAM" "$FINAL_TEXT" 2>/dev/null || true
                if [[ -f "${FINAL_TEXT}.is_error" ]]; then
                    claude_is_error=1
                    rm -f "${FINAL_TEXT}.is_error"
                fi
            fi
            # result/result_success with is_error or error → non-zero even when
            # the CLI process exits 0 and partial deltas exist. Artifacts are
            # preserved; do not emit a successful partial answer.
            if [[ "$claude_is_error" -eq 1 && "$exit_code" -eq 0 ]]; then
                exit_code=1
            fi
            ;;
        opencode)
            run_streamed "opencode" "$PROMPT_PATH" "${CMD[@]}"
            exit_code=$BACKEND_RC
            # Always reassemble with part-id last-write-wins when raw JSON is
            # present. Live extract-text may already be correct; never leave a
            # concatenated H+He+Hello FINAL just because the file is non-empty.
            if [[ -s "$RAW_STREAM" ]] && grep -q '^{' "$RAW_STREAM" 2>/dev/null; then
                python3 -c '
import json,sys
from collections import OrderedDict
snaps=OrderedDict()
deltas=[]
def unwrap(o):
    if not isinstance(o, dict):
        return o
    if isinstance(o.get("payload"), dict) and (o.get("type") is None or o.get("type")=="sync") and o["payload"].get("type"):
        o=o["payload"]
    if o.get("type")=="sync" and isinstance(o.get("syncEvent"), dict):
        se=o["syncEvent"]
        se_type=str(se.get("type") or "")
        if se_type.endswith(".1") or se_type.endswith(".0"):
            se_type=se_type.rsplit(".",1)[0]
        if se_type:
            data=se.get("data") if isinstance(se.get("data"), dict) else {}
            o={"type": se_type, "properties": data if data else se}
    return o
for line in open(sys.argv[1]):
    line=line.strip()
    if not line: continue
    try: o=json.loads(line)
    except Exception: continue
    o=unwrap(o)
    typ=o.get("type") or ""
    props=o.get("properties") if isinstance(o.get("properties"), dict) else o
    if not isinstance(props, dict):
        props=o if isinstance(o, dict) else {}
    part=props.get("part") if isinstance(props.get("part"), dict) else (o.get("part") if isinstance(o.get("part"), dict) else props)
    if typ=="message.part.updated" and isinstance(part, dict):
        pid=str(part.get("id") or part.get("partID") or part.get("partId") or "_")
        t=part.get("text")
        if isinstance(t,str) and t:
            snaps[pid]=t
    elif typ in ("message.part.delta","text"):
        d=""
        if isinstance(props, dict) and isinstance(props.get("delta"), str):
            d=props["delta"]
        if not d and isinstance(part, dict) and isinstance(part.get("delta"), str):
            d=part["delta"]
        if not d:
            d=o.get("text") or o.get("delta") or ""
        if d: deltas.append(str(d))
text="".join(snaps.values()) if snaps else "".join(deltas)
if text:
    open(sys.argv[2],"w").write(text)
' "$RAW_STREAM" "$FINAL_TEXT" 2>/dev/null || true
            elif [[ ! -s "$FINAL_TEXT" && -s "$NORM_STREAM" ]]; then
                python3 -c '
import sys,json
sys.path.insert(0, sys.argv[3])
from events import assemble_final_text, ConsiliumEvent
evts=[]
for line in open(sys.argv[1], encoding="utf-8"):
    line=line.strip()
    if not line: continue
    try: evts.append(ConsiliumEvent.from_dict(json.loads(line)))
    except Exception: continue
text=assemble_final_text(evts)
if text: open(sys.argv[2],"w",encoding="utf-8").write(text)
' "$NORM_STREAM" "$FINAL_TEXT" "$LIB_DIR" 2>/dev/null || true
            elif [[ ! -s "$FINAL_TEXT" && -s "$RAW_STREAM" ]]; then
                # Plain-text fallback when the stream is not JSON.
                cat "$RAW_STREAM" > "$FINAL_TEXT"
            fi
            ;;
        gemini-cli)
            # Backend identity is gemini-cli (not plain); plain-text behaviour retained.
            if command -v "$BIN" &>/dev/null || [[ -x "$BIN" ]]; then
                run_streamed "gemini-cli" "$PROMPT_PATH" "${CMD[@]}"
                exit_code=$BACKEND_RC
            else
                echo "gemini CLI missing" >"$BACKEND_ERR"
                exit_code=4
            fi
            if [[ ! -s "$FINAL_TEXT" && -s "$RAW_STREAM" ]]; then
                cat "$RAW_STREAM" > "$FINAL_TEXT"
            fi
            ;;
        grok-build)
            # --prompt-file is the large-prompt one-shot headless path (see grok --help)
            run_streamed "grok-build" "" "${CMD[@]}" --prompt-file "$PROMPT_PATH"
            exit_code=$BACKEND_RC
            ;;
    esac
    # Non-zero `return` under `set -e` aborts the whole script before the
    # caller can read RC / emit progress_agent_done / persist failure artifacts.
    set +e
    return "$exit_code"
}

progress_info "running" "agent=$PROGRESS_ID backend=$BACKEND"

set +e
run_and_capture
RC=$?
set -e

# Parent workflows tee and archive this diagnostic, so scrub before any display
# or handoff. The unredacted temp file is replaced in place.
redact_backend_stderr

# Persist artifacts (best-effort; never fail the run on copy issues)
if [[ -n "${ART_RAW:-}" ]]; then
    mkdir -p "$(dirname "$ART_RAW")" "$(dirname "$ART_NORM")" "$(dirname "$ART_FINAL")" 2>/dev/null || true
    [[ -f "$RAW_STREAM" ]] && cp "$RAW_STREAM" "$ART_RAW" 2>/dev/null || true
    [[ -f "$NORM_STREAM" ]] && cp "$NORM_STREAM" "$ART_NORM" 2>/dev/null || true
    artifacts_write_final "$ARTIFACT_KEY" "$FINAL_TEXT" 2>/dev/null || true
fi

if [[ $RC -ne 0 ]]; then
    progress_agent_done "$PROGRESS_ID" "failed" "$RC"
    if [[ -s "$BACKEND_ERR" ]]; then
        echo "[$LABEL] backend stderr:" >&2
        cat "$BACKEND_ERR" >&2
    fi
    exit $RC
fi

if [[ ! -s "$FINAL_TEXT" ]]; then
    progress_agent_done "$PROGRESS_ID" "empty" 66
    echo "[$LABEL] empty response" >&2
    exit 66
fi

progress_agent_done "$PROGRESS_ID" "ok" 0
# Final answer ONLY on stdout
cat "$FINAL_TEXT"
exit 0
