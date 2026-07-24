#!/bin/bash
#
# discovery-pass.sh — run ONE discovery pass (broad-analyst | broad-lateral |
# specialist | probe). Used by superreview.sh and ultrareview.sh.
#
# Usage:
#   discovery-pass.sh \
#     --agent <agent-id> --role <role> --cap <N|uncapped> \
#     --prompt <prompt-template.txt> \
#     --input-kind <file|diff> --input-label <label> \
#     --input-body-file <path-to-line-numbered-or-raw-body> \
#     --out <output.xml> \
#     [--artifact-key <key>] [--keep-tmp]
#
# Behaviour:
#   - Renders {{INPUT_KIND}}, {{INPUT_LABEL}}, {{INPUT_BODY}}, {{ROLE}},
#     {{CAP_DIRECTIVE}} into the chosen prompt.
#   - Resolves backend via $CONSILIUM_CONFIG (default: skill's config.json).
#   - Keeps temp artifacts under an isolated /tmp dir but runs the backend
#     from the caller's original CWD (so project files remain readable).
#   - Writes the agent's raw stdout (which should contain <finding> XML
#     elements per the prompt schema) directly to --out.
#   - Artifact keys are set explicitly via --artifact-key (fan-out callers
#     pass stage/index). Without it, an invocation-unique default is chosen —
#     ambient CONSILIUM_ARTIFACT_KEY is never trusted alone.
#
# Exit codes:
#   0 — backend ok, output written
#   1 — backend produced empty output
#   3 — backend invocation failed
#   4 — config error
#   5 — usage error
#
set -euo pipefail

LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(dirname "$LIB_DIR")"
SKILL_DIR="$(dirname "$SCRIPTS_DIR")"

if [[ -f "$LIB_DIR/common.sh" ]]; then source "$LIB_DIR/common.sh"; fi
: "${RED:=$'\033[0;31m'}" "${GREEN:=$'\033[0;32m'}" "${YELLOW:=$'\033[1;33m'}" "${CYAN:=$'\033[0;36m'}" "${NC:=$'\033[0m'}"

AGENT=""; ROLE=""; CAP="uncapped"; PROMPT=""
INPUT_KIND="file"; INPUT_LABEL=""; INPUT_BODY_FILE=""; OUT=""; KEEP_TMP=""
ARTIFACT_KEY_ARG=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --agent)             AGENT="$2"; shift 2 ;;
        --role)              ROLE="$2"; shift 2 ;;
        --cap)               CAP="$2"; shift 2 ;;
        --prompt)            PROMPT="$2"; shift 2 ;;
        --input-kind)        INPUT_KIND="$2"; shift 2 ;;
        --input-label)       INPUT_LABEL="$2"; shift 2 ;;
        --input-body-file)   INPUT_BODY_FILE="$2"; shift 2 ;;
        --out)               OUT="$2"; shift 2 ;;
        --artifact-key)      ARTIFACT_KEY_ARG="$2"; shift 2 ;;
        --keep-tmp)          KEEP_TMP=1; shift ;;
        -h|--help)           sed -n '2,35p' "$0"; exit 0 ;;
        *)                   echo -e "${RED}Error: unknown flag: $1${NC}" >&2; exit 5 ;;
    esac
done

for var in AGENT ROLE PROMPT INPUT_LABEL INPUT_BODY_FILE OUT; do
    if [[ -z "${!var}" ]]; then
        # Bash 3.2-safe flag wording (no ${var,,}); underscores → hyphens.
        flag=$(printf '%s' "$var" | tr 'A-Z_' 'a-z-')
        echo -e "${RED}Error: --${flag} required${NC}" >&2
        exit 5
    fi
done
[[ -f "$PROMPT" ]]          || { echo -e "${RED}Error: prompt not found: $PROMPT${NC}" >&2; exit 4; }
[[ -f "$INPUT_BODY_FILE" ]] || { echo -e "${RED}Error: body file not found: $INPUT_BODY_FILE${NC}" >&2; exit 4; }

CONSILIUM_CONFIG="${CONSILIUM_CONFIG:-$SKILL_DIR/config.json}"
[[ -f "$CONSILIUM_CONFIG" ]] || { echo -e "${RED}Error: config not found: $CONSILIUM_CONFIG${NC}" >&2; exit 4; }

BACKEND="$(python3 -c "
import json, sys
d = json.load(open('$CONSILIUM_CONFIG'))['agents']
if '$AGENT' not in d:
    sys.stderr.write('agent not in config: $AGENT\n'); sys.exit(1)
print(d['$AGENT']['backend'])
")" || exit 4

BACKEND_SCRIPT="$LIB_DIR/backend_run.sh"
[[ -x "$BACKEND_SCRIPT" || -f "$BACKEND_SCRIPT" ]] || {
    echo -e "${RED}Error: backend runner missing: $BACKEND_SCRIPT${NC}" >&2
    exit 4
}
chmod +x "$BACKEND_SCRIPT" 2>/dev/null || true

# Cap directive — same wording as the harness.
if [[ "$CAP" == "uncapped" || "$CAP" == "0" ]]; then
    CAP_DIRECTIVE="OUTPUT: no upper bound on the number of findings. Emit every distinct, defensible finding that survives the gates above."
else
    CAP_DIRECTIVE="OUTPUT CAP: emit at most $CAP findings. If more candidates survive the gates, keep the top $CAP by (severity, confidence)."
fi

TMP_DIR="$(mktemp -d -t "agents-consilium-pass-XXXXXX")"
cleanup() { [[ -z "$KEEP_TMP" ]] && rm -rf "$TMP_DIR" || echo -e "${YELLOW}[debug] keeping tmp: $TMP_DIR${NC}" >&2; }
trap cleanup EXIT

# Paths only in the environment — never the body contents (ARG_MAX / E2BIG).
export DP_INPUT_KIND="$INPUT_KIND"
export DP_INPUT_LABEL="$INPUT_LABEL"
export DP_INPUT_BODY_FILE="$INPUT_BODY_FILE"
export DP_ROLE="$ROLE"
export DP_CAP_DIRECTIVE="$CAP_DIRECTIVE"
RENDERED_PROMPT_FILE="$TMP_DIR/rendered-prompt.txt"
python3 - "$PROMPT" "$RENDERED_PROMPT_FILE" <<'PYEOF'
import os, sys
tpl = open(sys.argv[1]).read()
body = open(os.environ['DP_INPUT_BODY_FILE']).read()
out = (tpl
       .replace('{{INPUT_KIND}}',    os.environ.get('DP_INPUT_KIND', ''))
       .replace('{{INPUT_LABEL}}',   os.environ.get('DP_INPUT_LABEL', ''))
       .replace('{{INPUT_BODY}}',    body)
       .replace('{{ROLE}}',          os.environ.get('DP_ROLE', ''))
       .replace('{{CAP_DIRECTIVE}}', os.environ.get('DP_CAP_DIRECTIVE', '')))
open(sys.argv[2], 'w').write(out)
PYEOF

# Drop render helpers before the backend child starts.
unset DP_INPUT_KIND DP_INPUT_LABEL DP_INPUT_BODY_FILE DP_ROLE DP_CAP_DIRECTIVE

# Explicit key from fan-out, or an invocation-unique safe default. Never rely
# solely on an ambient inherited CONSILIUM_ARTIFACT_KEY (would collide).
if [[ -n "$ARTIFACT_KEY_ARG" ]]; then
    ARTIFACT_KEY="$ARTIFACT_KEY_ARG"
else
    ARTIFACT_KEY="discovery.${AGENT}.${ROLE}.$$.${RANDOM:-0}"
fi

mkdir -p "$(dirname "$OUT")"
RAW_ERR="$TMP_DIR/raw-err.txt"

# Drain-safe live stderr (no FIFO):
#   backend stdout → --out file
#   backend stderr → tee → live parent stderr + RAW_ERR
# Pipeline waits for tee; PIPESTATUS[0] is the backend status (not tee).
# Works on Apple Bash 3.2 and Bash 5.x. No timeout wrapper.
set +e
set +o pipefail
(
    export CONSILIUM_SKIP_OUTPUT_TEMPLATE=1
    export CONSILIUM_RUN_DIR="${CONSILIUM_RUN_DIR:-}"
    export CONSILIUM_ARTIFACT_KEY="$ARTIFACT_KEY"
    "$BACKEND_SCRIPT" \
        --mode review --agent-id "$AGENT" --role "$ROLE" \
        < "$RENDERED_PROMPT_FILE" 2>&1 1>"$OUT" | tee "$RAW_ERR" >&2
    ps=("${PIPESTATUS[@]}")
    exit "${ps[0]}"
)
rc=$?
set -e
set -o pipefail

if [[ $rc -ne 0 ]]; then
    echo -e "${RED}[$AGENT/$ROLE] backend failed (exit $rc)${NC}" >&2
    # Live stderr already streamed via tee — do not re-print RAW_ERR.
    exit 3
fi

if [[ ! -s "$OUT" ]]; then
    echo -e "${RED}[$AGENT/$ROLE] empty output${NC}" >&2
    exit 1
fi

# grep -c exits 1 when count is 0; do not `|| echo 0` (that prints "0\n0").
n="$(grep -c "<finding\b" "$OUT" 2>/dev/null || true)"
n="${n:-0}"
echo -e "${GREEN}[$AGENT/$ROLE] ok → $n finding(s)${NC}" >&2
exit 0
