#!/bin/bash
#
# review ask — multi-agent independent opinions (was consensus-query).
# Invoked by: scripts/consilium review ask ...
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

OUTPUT_FORMAT="markdown"
LIST_ONLY=false
PROMPT=""
PROMPT_FILE=""
PROMPT_SOURCE=""   # positional | file | stdin
INCLUDE_PATTERNS=()
EXCLUDE_PATTERNS=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --xml)          OUTPUT_FORMAT="xml"; shift ;;
        --list-agents)  LIST_ONLY=true; shift ;;
        --prompt-file)  shift; PROMPT_FILE="${1:-}"; PROMPT_SOURCE="file"; shift ;;
        -a|--agents|--agent)
                        shift
                        IFS=',' read -ra _parts <<< "${1:-}"
                        INCLUDE_PATTERNS+=("${_parts[@]}")
                        shift
                        ;;
        -x|--exclude)   shift
                        IFS=',' read -ra _parts <<< "${1:-}"
                        EXCLUDE_PATTERNS+=("${_parts[@]}")
                        shift
                        ;;
        -h|--help)
            cat <<'EOF'
Usage: consilium review ask [options] ["question"]

Options:
  --xml                 Emit <consilium-report> XML
  --list-agents         Print agent plan as XML and exit
  --prompt-file <path>  Send file contents verbatim (raw mode)
  -a, --agents <ID|GLOB>  Include agents (repeatable; globs ok)
  -x, --exclude <ID|GLOB> Exclude agents
  -h, --help

Prompt may also come from stdin when no positional is given.
EOF
            exit $EXIT_OK
            ;;
        --)             shift; PROMPT="${1:-}"; PROMPT_SOURCE="positional"; break ;;
        -*)             echo -e "${RED}Error: unknown flag: $1${NC}" >&2; exit $EXIT_USAGE ;;
        *)              PROMPT="$1"; PROMPT_SOURCE="positional"; shift; break ;;
    esac
done

if [[ -n "$PROMPT_FILE" ]]; then
    if [[ ! -f "$PROMPT_FILE" ]]; then
        echo -e "${RED}Error: prompt file not found: $PROMPT_FILE${NC}" >&2
        exit $EXIT_USAGE
    fi
    if [[ -n "$PROMPT" ]]; then
        echo -e "${RED}Error: cannot combine --prompt-file with a positional prompt${NC}" >&2
        exit $EXIT_USAGE
    fi
    PROMPT="$(cat "$PROMPT_FILE")"
    PROMPT_SOURCE="file"
    export CONSILIUM_RAW_PROMPT=1
fi

if [[ ${#INCLUDE_PATTERNS[@]} -eq 0 && -n "${CONSILIUM_AGENTS:-}" ]]; then
    IFS=',' read -ra INCLUDE_PATTERNS <<< "$CONSILIUM_AGENTS"
fi
if [[ ${#EXCLUDE_PATTERNS[@]} -eq 0 && -n "${CONSILIUM_EXCLUDE:-}" ]]; then
    IFS=',' read -ra EXCLUDE_PATTERNS <<< "$CONSILIUM_EXCLUDE"
fi

config_validate || exit $EXIT_CONFIG_ERROR

if $LIST_ONLY; then
    config_xml_plan
    exit $EXIT_OK
fi

STDIN_CONTENT=""
if [[ ! -t 0 ]]; then
    STDIN_CONTENT=$(cat)
fi
if [[ -z "$PROMPT" && -n "$STDIN_CONTENT" ]]; then
    PROMPT="$STDIN_CONTENT"
    STDIN_CONTENT=""
    PROMPT_SOURCE="stdin"
    progress_info "note" "using stdin as the prompt"
fi
if [[ -z "$PROMPT" ]]; then
    echo -e "${RED}Error: No prompt provided${NC}" >&2
    exit $EXIT_USAGE
fi

# Shell-interpolation warning only for unsafe positional usage — not file/stdin.
if [[ "$PROMPT_SOURCE" == "positional" ]]; then
    warn_shell_special_in_prompt "$PROMPT"
fi

export CONSILIUM_MODE="review-ask"
artifacts_init_run "ask"

ALL_AGENTS=()
while IFS= read -r a; do
    [[ -n "$a" ]] && ALL_AGENTS+=("$a")
done < <(config_all_agents)

CANDIDATES=()
if [[ ${#INCLUDE_PATTERNS[@]} -gt 0 ]]; then
    for a in "${ALL_AGENTS[@]}"; do
        config_match_any "$a" "${INCLUDE_PATTERNS[@]}" && CANDIDATES+=("$a")
    done
    if [[ ${#CANDIDATES[@]} -eq 0 ]]; then
        echo -e "${RED}Error: no agents matched --agents patterns: ${INCLUDE_PATTERNS[*]}${NC}" >&2
        exit $EXIT_CONFIG_ERROR
    fi
else
    while IFS= read -r a; do
        [[ -n "$a" ]] && CANDIDATES+=("$a")
    done < <(config_enabled_agents)
fi

ENABLED_AGENTS=()
if [[ ${#EXCLUDE_PATTERNS[@]} -gt 0 ]]; then
    for a in "${CANDIDATES[@]}"; do
        config_match_any "$a" "${EXCLUDE_PATTERNS[@]}" || ENABLED_AGENTS+=("$a")
    done
else
    ENABLED_AGENTS=("${CANDIDATES[@]}")
fi

if [[ ${#ENABLED_AGENTS[@]} -eq 0 ]]; then
    echo -e "${RED}Error: no agents remain after filters / none enabled${NC}" >&2
    exit $EXIT_CONFIG_ERROR
fi

progress_stage "ask" "agents=${ENABLED_AGENTS[*]}"
export CONSILIUM_SUPPRESS_SHELL_WARN=1

declare -a AGENT_IDS PIDS OUT_FILES ERR_FILES LABELS MODELS ROLES BACKENDS STATUSES EXITS

for agent in "${ENABLED_AGENTS[@]}"; do
    backend="$(config_get_field "$agent" backend)"
    label="$(config_get_field "$agent" label)"; label="${label:-$agent}"
    model="$(config_get_field "$agent" model)"
    role="$(config_get_field "$agent" role)"

    AGENT_IDS+=("$agent")
    LABELS+=("$label")
    MODELS+=("$model")
    ROLES+=("$role")
    BACKENDS+=("$backend")

    if ! config_is_enabled "$agent"; then
        progress_info "override" "agent=$agent forced via --agents (enabled=false)"
    fi

    out=$(mktemp)
    err=$(mktemp)
    EXTRA_ARGS=()
    if [[ -n "${CONSILIUM_RAW_PROMPT:-}" ]]; then
        EXTRA_ARGS+=(--raw)
    fi
    if [[ -n "$STDIN_CONTENT" ]]; then
        # Append context to prompt for this agent
        agent_prompt="${PROMPT}"$'\n\n--- Input ---\n'"${STDIN_CONTENT}"
    else
        agent_prompt="$PROMPT"
    fi
    (
        export CONSILIUM_RUN_DIR
        export CONSILIUM_SAVE_OUTPUTS
        # Live progress → parent stderr; also capture for failure reporting.
        printf '%s' "$agent_prompt" | "$LIB_DIR/backend_run.sh" \
            --mode review --agent-id "$agent" "${EXTRA_ARGS[@]}" \
            >"$out" 2> >(tee "$err" >&2)
    ) &
    STATUSES+=("pending")
    EXITS+=("0")
    OUT_FILES+=("$out")
    ERR_FILES+=("$err")
    PIDS+=("$!")
done

cleanup() {
    for f in "${OUT_FILES[@]:-}" "${ERR_FILES[@]:-}"; do
        [[ -n "$f" ]] && rm -f "$f"
    done
}
trap cleanup EXIT

for i in "${!AGENT_IDS[@]}"; do
    pid="${PIDS[$i]}"
    [[ -z "$pid" ]] && continue
    code=0
    wait "$pid" || code=$?
    EXITS[$i]="$code"
    out_bytes=$(wc -c < "${OUT_FILES[$i]}" | tr -d ' ')
    if [[ $code -eq 0 && $out_bytes -gt 0 ]]; then
        STATUSES[$i]="ok"
    elif [[ $code -eq 0 ]]; then
        EXITS[$i]=66
        STATUSES[$i]="failed"
        progress_info "empty" "agent=${AGENT_IDS[$i]}"
    else
        STATUSES[$i]="failed"
    fi
    # Forward per-agent stderr progress already emitted; surface failures
    if [[ "${STATUSES[$i]}" == "failed" && -s "${ERR_FILES[$i]}" ]]; then
        cat "${ERR_FILES[$i]}" >&2 || true
    fi
done

queried=0; succeeded=0; failed=0
for i in "${!AGENT_IDS[@]}"; do
    case "${STATUSES[$i]}" in
        ok)      queried=$((queried+1)); succeeded=$((succeeded+1)) ;;
        failed)  queried=$((queried+1)); failed=$((failed+1)) ;;
    esac
done

# Build report into temp then print to stdout as the final answer
REPORT=$(mktemp)
{
if [[ "$OUTPUT_FORMAT" == "xml" ]]; then
    echo "<consilium-report prompt-length=\"${#PROMPT}\">"
    for i in "${!AGENT_IDS[@]}"; do
        agent="${AGENT_IDS[$i]}"
        label="${LABELS[$i]}"
        model="${MODELS[$i]}"
        role="${ROLES[$i]}"
        backend="${BACKENDS[$i]}"
        status="${STATUSES[$i]}"
        code="${EXITS[$i]}"
        printf '  <agent id="%s" label="%s" backend="%s" model="%s" role="%s" status="%s" exit-code="%s">\n' \
            "$(printf '%s' "$agent"   | xml_escape)" \
            "$(printf '%s' "$label"   | xml_escape)" \
            "$(printf '%s' "$backend" | xml_escape)" \
            "$(printf '%s' "$model"   | xml_escape)" \
            "$(printf '%s' "$role"    | xml_escape)" \
            "$status" "$code"
        case "$status" in
            ok)
                printf '    <response>'
                cat "${OUT_FILES[$i]}" | cdata_wrap
                printf '</response>\n'
                ;;
            failed)
                printf '    <error>'
                cat "${ERR_FILES[$i]}" | cdata_wrap
                printf '</error>\n'
                ;;
        esac
        echo "  </agent>"
    done
    for agent in "${ALL_AGENTS[@]}"; do
        in_enabled=false
        for a in "${ENABLED_AGENTS[@]}"; do
            [[ "$a" == "$agent" ]] && in_enabled=true && break
        done
        $in_enabled && continue
        label="$(config_get_field "$agent" label)"; label="${label:-$agent}"
        model="$(config_get_field "$agent" model)"
        role="$(config_get_field "$agent" role)"
        backend="$(config_get_field "$agent" backend)"
        if config_is_enabled "$agent"; then status_attr="filtered"; else status_attr="disabled"; fi
        printf '  <agent id="%s" label="%s" backend="%s" model="%s" role="%s" status="%s"/>\n' \
            "$(printf '%s' "$agent"   | xml_escape)" \
            "$(printf '%s' "$label"   | xml_escape)" \
            "$(printf '%s' "$backend" | xml_escape)" \
            "$(printf '%s' "$model"   | xml_escape)" \
            "$(printf '%s' "$role"    | xml_escape)" \
            "$status_attr"
    done
    echo "</consilium-report>"
else
    for i in "${!AGENT_IDS[@]}"; do
        label="${LABELS[$i]}"
        model="${MODELS[$i]}"
        status="${STATUSES[$i]}"
        code="${EXITS[$i]}"
        echo ""
        echo "## ${label} Response (${model})"
        echo ""
        case "$status" in
            ok)      cat "${OUT_FILES[$i]}" ;;
            failed)  echo "[${label} query failed with exit code $code]"; cat "${ERR_FILES[$i]}" ;;
        esac
    done
    inactive_any=false
    for agent in "${ALL_AGENTS[@]}"; do
        in_enabled=false
        for a in "${ENABLED_AGENTS[@]}"; do
            [[ "$a" == "$agent" ]] && in_enabled=true && break
        done
        $in_enabled && continue
        $inactive_any || { echo ""; echo "## Inactive agents (not queried)"; echo ""; inactive_any=true; }
        label="$(config_get_field "$agent" label)"; label="${label:-$agent}"
        model="$(config_get_field "$agent" model)"
        if config_is_enabled "$agent"; then reason="filtered by --agents/--exclude"; else reason="disabled in config"; fi
        echo "- ${label} (${model}) — ${reason}"
    done
    echo ""
    echo "---"
    echo "END OF CONSENSUS REPORT"
fi
} > "$REPORT"

artifacts_set_primary_final "$REPORT"
cat "$REPORT"
rm -f "$REPORT"

if [[ $succeeded -eq $queried ]]; then
    exit $EXIT_OK
elif [[ $succeeded -eq 0 ]]; then
    exit $EXIT_ALL_FAILED
else
    exit $EXIT_PARTIAL
fi
