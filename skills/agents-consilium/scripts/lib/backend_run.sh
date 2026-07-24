#!/bin/bash
#
# Unified backend runner for agents-consilium v5.
#
# Usage:
#   backend_run.sh --mode review|delegate --agent-id <id> [options] ["prompt"]
#   backend_run.sh --mode review --agent-id codex --prompt-file path.txt
#   echo "prompt" | backend_run.sh --mode review --agent-id codex
#
# Options:
#   --mode review|delegate   Required. review = read-only; delegate = full YOLO.
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
#   PIPESTATUS preserves backend exit (timeout/signal) and normalizer validation
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

while [[ $# -gt 0 ]]; do
    case "$1" in
        --mode)        MODE="${2:-}"; shift 2 ;;
        --agent-id)    AGENT_ID="${2:-}"; shift 2 ;;
        --role)        ROLE_OVERRIDE="${2:-}"; shift 2 ;;
        --prompt-file) PROMPT_FILE="${2:-}"; PROMPT_SOURCE="file"; shift 2 ;;
        --raw|--no-wrap) RAW_MODE=1; shift ;;
        -h|--help)     sed -n '2,40p' "$0"; exit $EXIT_OK ;;
        --)            shift; PROMPT="${1:-}"; PROMPT_SOURCE="positional"; break ;;
        -*)            echo "Error: unknown flag: $1" >&2; exit $EXIT_USAGE ;;
        *)             PROMPT="$1"; PROMPT_SOURCE="positional"; shift; break ;;
    esac
done

[[ -n "$MODE" ]] || { echo "Error: --mode required (review|delegate)" >&2; exit $EXIT_USAGE; }
[[ "$MODE" == "review" || "$MODE" == "delegate" ]] || {
    echo "Error: --mode must be review or delegate (got: $MODE)" >&2
    exit $EXIT_USAGE
}
[[ -n "$AGENT_ID" ]] || { echo "Error: --agent-id required" >&2; exit $EXIT_USAGE; }

config_validate || exit $EXIT_CONFIG_ERROR

BACKEND="$(config_get_field "$AGENT_ID" backend)" || exit $EXIT_CONFIG_ERROR
MODEL="$(config_get_field "$AGENT_ID" model)"
LABEL="$(config_get_field "$AGENT_ID" label)"; LABEL="${LABEL:-$AGENT_ID}"
EFFORT="$(config_get_field "$AGENT_ID" effort)"
ROLE_ID="${ROLE_OVERRIDE:-$(config_get_field "$AGENT_ID" role)}"
ROLE_ID="${ROLE_ID:-analyst}"

if [[ "$MODE" == "delegate" ]]; then
    # Gemini is review-only.
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

if [[ "$RAW_MODE" -eq 1 || -n "${CONSILIUM_RAW_PROMPT:-}" ]]; then
    export CONSILIUM_RAW_PROMPT=1
    FULL_PROMPT="$PROMPT"
else
    if ! ROLE_PROMPT="$(get_role_prompt "$ROLE_ID")"; then
        echo "Error: unknown role '$ROLE_ID' for agent $AGENT_ID" >&2
        exit $EXIT_CONFIG_ERROR
    fi
    # build_prompt may also read stdin as context; we already consumed stdin.
    # CONSILIUM_SKIP_OUTPUT_TEMPLATE is honored by build_prompt (code-review schemas).
    FULL_PROMPT="$(build_prompt "$ROLE_PROMPT" "$PROMPT" </dev/null)"
fi
# NEVER export FULL_PROMPT — large prompts exceed ARG_MAX when copied into the
# environment (execve counts env + argv). Prompt bodies travel via temp file /
# stdin only.

# Resolve CLI binary (overridable for tests)
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

BIN="$(bin_for "$BACKEND")"
if [[ -z "$BIN" ]]; then
    echo "Error: unknown backend '$BACKEND' for agent $AGENT_ID" >&2
    exit $EXIT_CONFIG_ERROR
fi
if ! command -v "$BIN" &>/dev/null && [[ ! -x "$BIN" ]]; then
    echo "Error: backend CLI not found: $BIN (backend=$BACKEND)" >&2
    exit $EXIT_CONFIG_ERROR
fi

# Codex model alias normalization
if [[ "$BACKEND" == "codex-cli" && "$MODEL" == "gpt-5.6" ]]; then
    MODEL="gpt-5.6-sol"
fi

# Default efforts
case "$BACKEND" in
    codex-cli|claude-code|grok-build) EFFORT="${EFFORT:-high}" ;;
    opencode)
        if [[ "$EFFORT" == "none" ]]; then EFFORT=""; fi
        ;;
esac

progress_agent_start "$AGENT_ID" "$BACKEND" "$MODE" "$MODEL"

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
ARTIFACT_KEY="${CONSILIUM_ARTIFACT_KEY:-$AGENT_ID}"
artifacts_paths_for "$ARTIFACT_KEY"

# Build argv into array CMD
CMD=()
PROMPT_VIA_FILE=0
PROMPT_FILE_PATH=""

build_cmd_codex() {
    local approval_sandbox
    CMD=("$BIN")
    # Top-level -a is ask-for-approval
    if [[ "$MODE" == "review" ]]; then
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
    CMD=("$BIN")
    if [[ "$MODE" == "review" ]]; then
        CMD+=(--permission-mode plan)
        # Defense in depth: deny write tools even if plan is misconfigured
        CMD+=(--disallowedTools "Edit,Write,NotebookEdit")
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
    if [[ "$MODE" == "review" ]]; then
        CMD+=(--agent plan)
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
    # Review only. Non-TTY stdin selects headless mode without putting the
    # potentially large prompt in argv.
    CMD=("$BIN" --model "$MODEL" --approval-mode plan -o text -e "" --allowed-mcp-server-names "")
}

build_cmd_grok() {
    # One-shot headless: --prompt-file is documented as "Single-turn prompt from a file"
    # (same headless class as -p/--single for inline prompts). Do not also pass -p;
    # --prompt-file alone selects single-turn non-TUI mode.
    CMD=("$BIN")
    if [[ "$MODE" == "review" ]]; then
        # Kernel sandbox + strict tool allowlist (plan mode alone is NOT read-only)
        CMD+=(--sandbox read-only)
        CMD+=(--tools "read_file,grep,list_dir")
        CMD+=(--disallowed-tools "search_replace,write,run_terminal_cmd,Agent")
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
    exit $EXIT_OK
fi

# Prepare temp files
TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/consilium-backend.XXXXXX")"
cleanup_backend() { rm -rf "$TMP_DIR"; }
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
    local -a norm_argv=(
        python3 "$LIB_DIR/normalize_stream.py"
        --backend "$backend"
        --agent-id "$AGENT_ID"
        --input -
        --raw-out "$RAW_STREAM"
        --extract-text --text-out "$FINAL_TEXT"
        --progress
    )
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
    if [[ -n "$TIMEOUT_CMD" ]]; then
        if [[ -n "$stdin_file" ]]; then
            $TIMEOUT_CMD "${AGENT_TIMEOUT}s" "${run_argv[@]}" <"$stdin_file" 2>"$BACKEND_ERR" \
                | "${norm_argv[@]}" >"$NORM_STREAM"
            _ps=("${PIPESTATUS[@]}")
        else
            $TIMEOUT_CMD "${AGENT_TIMEOUT}s" "${run_argv[@]}" 2>"$BACKEND_ERR" \
                | "${norm_argv[@]}" >"$NORM_STREAM"
            _ps=("${PIPESTATUS[@]}")
        fi
    else
        if [[ -n "$stdin_file" ]]; then
            "${run_argv[@]}" <"$stdin_file" 2>"$BACKEND_ERR" \
                | "${norm_argv[@]}" >"$NORM_STREAM"
            _ps=("${PIPESTATUS[@]}")
        else
            "${run_argv[@]}" 2>"$BACKEND_ERR" \
                | "${norm_argv[@]}" >"$NORM_STREAM"
            _ps=("${PIPESTATUS[@]}")
        fi
    fi
    BACKEND_RC=${_ps[0]:-1}
    NORM_RC=${_ps[1]:-0}
    set -o pipefail
    set -e

    # Grok contract: success requires process exit 0 AND normalizer validation
    # (end present, no error event). Prefer backend non-zero (timeout/signal)
    # when both fail.
    if [[ "$backend" == "grok-build" && "${NORM_RC:-0}" -ne 0 ]]; then
        if [[ "${BACKEND_RC:-0}" -eq 0 ]]; then
            BACKEND_RC=1
        fi
    fi
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
            # Prefer authoritative result over streamed deltas (no duplication).
            if [[ -s "$RAW_STREAM" ]]; then
                python3 -c '
import json,sys
deltas=[]
result=None
for line in open(sys.argv[1]):
    line=line.strip()
    if not line: continue
    try:
        o=json.loads(line)
    except Exception:
        deltas.append(line); continue
    if o.get("type") in ("result", "result_success") and isinstance(o.get("result"), str):
        result=o["result"]
    elif o.get("type")=="content_block_delta":
        d=o.get("delta") or {}
        if d.get("type")=="text_delta":
            deltas.append(d.get("text",""))
# Prefer result (complete answer) over concatenated deltas.
text = result if result is not None else "".join(deltas)
if text or result is not None:
    open(sys.argv[2],"w").write(text if text is not None else "")
' "$RAW_STREAM" "$FINAL_TEXT" 2>/dev/null || true
            fi
            ;;
        opencode)
            run_streamed "opencode" "$PROMPT_PATH" "${CMD[@]}"
            exit_code=$BACKEND_RC
            if [[ ! -s "$FINAL_TEXT" && -s "$RAW_STREAM" ]]; then
                if ! grep -q '^{' "$RAW_STREAM" 2>/dev/null; then
                    cat "$RAW_STREAM" > "$FINAL_TEXT"
                else
                    python3 -c '
import json,sys
chunks=[]
for line in open(sys.argv[1]):
    line=line.strip()
    if not line: continue
    try: o=json.loads(line)
    except Exception: continue
    part=o.get("part") or o
    t=part.get("text") or o.get("text")
    if t: chunks.append(t)
open(sys.argv[2],"w").write("".join(chunks))
' "$RAW_STREAM" "$FINAL_TEXT" 2>/dev/null || true
                fi
            fi
            ;;
        gemini-cli)
            if command -v "$BIN" &>/dev/null || [[ -x "$BIN" ]]; then
                run_streamed "plain" "$PROMPT_PATH" "${CMD[@]}"
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

progress_info "running" "agent=$AGENT_ID backend=$BACKEND"

set +e
run_and_capture
RC=$?
set -e

# Persist artifacts (best-effort; never fail the run on copy issues)
if [[ -n "${ART_RAW:-}" ]]; then
    mkdir -p "$(dirname "$ART_RAW")" "$(dirname "$ART_NORM")" "$(dirname "$ART_FINAL")" 2>/dev/null || true
    [[ -f "$RAW_STREAM" ]] && cp "$RAW_STREAM" "$ART_RAW" 2>/dev/null || true
    [[ -f "$NORM_STREAM" ]] && cp "$NORM_STREAM" "$ART_NORM" 2>/dev/null || true
    artifacts_write_final "$ARTIFACT_KEY" "$FINAL_TEXT" 2>/dev/null || true
fi

if [[ $RC -ne 0 ]]; then
    progress_agent_done "$AGENT_ID" "failed" "$RC"
    if [[ -s "$BACKEND_ERR" ]]; then
        echo "[$LABEL] backend stderr:" >&2
        cat "$BACKEND_ERR" >&2
    fi
    exit $RC
fi

if [[ ! -s "$FINAL_TEXT" ]]; then
    progress_agent_done "$AGENT_ID" "empty" 66
    echo "[$LABEL] empty response" >&2
    exit 66
fi

progress_agent_done "$AGENT_ID" "ok" 0
# Final answer ONLY on stdout
cat "$FINAL_TEXT"
exit 0
