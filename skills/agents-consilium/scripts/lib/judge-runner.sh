#!/bin/bash
#
# judge-runner.sh — production judge pass for ultrareview/superreview modes.
#
# Reads a unioned <code-review-report> XML, the original source under review,
# and runs ONE LLM call that emits a JSON verdicts object (VALID / DUPLICATE /
# FALSE_POSITIVE / DOWNGRADE per finding). No ground-truth comparison — this
# is for production code review, not benchmark scoring.
#
# Usage:
#   judge-runner.sh \
#     --agent <agent-id-from-config.json> \
#     --findings <unioned.xml> \
#     --source <file-or-diff-source> \
#     --input-kind <file|diff> \
#     --out <verdicts.json> \
#     [--artifact-key <key>] \
#     [--prompt <judge.txt>] [--keep-tmp]
#
# Large callers must use JUDGE_INPUT_BODY_FILE (path pointer), not the legacy
# JUDGE_INPUT_BODY env var. After materializing the body, legacy markers are
# unset before any backend child starts.
#
# Exit codes:
#   0 — success, valid JSON written
#   1 — backend produced empty output
#   2 — JSON failed schema validation (no `verdicts` array)
#   3 — backend invocation failed
#   4 — config error (agent or prompt missing)
#   5 — usage error
#
set -euo pipefail

LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(dirname "$LIB_DIR")"
SKILL_DIR="$(dirname "$SCRIPTS_DIR")"

# Pick up colour helpers from lib (v5 layout).
if [[ -f "$LIB_DIR/common.sh" ]]; then source "$LIB_DIR/common.sh"; fi
: "${RED:=$'\033[0;31m'}" "${GREEN:=$'\033[0;32m'}" "${YELLOW:=$'\033[1;33m'}" "${CYAN:=$'\033[0;36m'}" "${NC:=$'\033[0m'}"

AGENT=""
FINDINGS=""
SOURCE=""
INPUT_KIND="file"
OUT=""
PROMPT="$SKILL_DIR/prompts/judge.txt"
KEEP_TMP=""
ARTIFACT_KEY_ARG=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --agent)         AGENT="$2"; shift 2 ;;
        --findings)      FINDINGS="$2"; shift 2 ;;
        --source)        SOURCE="$2"; shift 2 ;;
        --input-kind)    INPUT_KIND="$2"; shift 2 ;;
        --out)           OUT="$2"; shift 2 ;;
        --prompt)        PROMPT="$2"; shift 2 ;;
        --artifact-key)  ARTIFACT_KEY_ARG="$2"; shift 2 ;;
        --keep-tmp)      KEEP_TMP=1; shift ;;
        -h|--help)       sed -n '2,35p' "$0"; exit 0 ;;
        *)               echo -e "${RED}Error: unknown flag: $1${NC}" >&2; exit 5 ;;
    esac
done

for var in AGENT FINDINGS SOURCE OUT; do
    if [[ -z "${!var}" ]]; then
        # Bash 3.2-safe flag wording (no ${var,,}); underscores → hyphens.
        flag=$(printf '%s' "$var" | tr 'A-Z_' 'a-z-')
        echo -e "${RED}Error: --${flag} required${NC}" >&2
        exit 5
    fi
done
[[ -f "$FINDINGS" ]] || { echo -e "${RED}Error: findings xml not found: $FINDINGS${NC}" >&2; exit 4; }
[[ -f "$PROMPT"   ]] || { echo -e "${RED}Error: judge prompt not found: $PROMPT${NC}" >&2; exit 4; }

# Resolve backend script via skill's config.json — same pattern as code-review.sh
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
[[ -f "$BACKEND_SCRIPT" ]] || { echo -e "${RED}Error: backend runner missing: $BACKEND_SCRIPT${NC}" >&2; exit 4; }
chmod +x "$BACKEND_SCRIPT" 2>/dev/null || true

# --- Temp artifacts (backend still runs from caller's CWD) -----------------
TMP_DIR="$(mktemp -d -t "agents-consilium-judge-XXXXXX")"
cleanup() { [[ -z "$KEEP_TMP" ]] && rm -rf "$TMP_DIR" || echo -e "${YELLOW}[debug] keeping tmp: $TMP_DIR${NC}" >&2; }
trap cleanup EXIT

# Render judge prompt with placeholders. SOURCE may be a path (file mode) or
# the literal diff text already on disk (we accept either — "--source" points
# to whatever was reviewed, line-numbered for verification).
# Large bodies are written to files — never exported into the environment
# (ARG_MAX / E2BIG includes env size).
INPUT_LABEL="$SOURCE"
INPUT_BODY_FILE="$TMP_DIR/input-body.txt"
if [[ -f "$SOURCE" ]]; then
    if [[ "$INPUT_KIND" == "file" ]]; then
        awk '{printf "%4d  %s\n", NR, $0}' "$SOURCE" > "$INPUT_BODY_FILE"
    else
        cat "$SOURCE" > "$INPUT_BODY_FILE"
    fi
else
    # SOURCE is a raw label (e.g. "(stdin diff)") — body from optional file
    # or small env path pointer, not the body itself.
    if [[ -n "${JUDGE_INPUT_BODY_FILE:-}" && -f "$JUDGE_INPUT_BODY_FILE" ]]; then
        cat "$JUDGE_INPUT_BODY_FILE" > "$INPUT_BODY_FILE"
    elif [[ -n "${JUDGE_INPUT_BODY:-}" ]]; then
        # Legacy: materialize then drop from env. Prefer JUDGE_INPUT_BODY_FILE.
        printf '%s' "$JUDGE_INPUT_BODY" > "$INPUT_BODY_FILE"
    else
        : > "$INPUT_BODY_FILE"
    fi
fi

# Explicitly drop legacy/in-process body env vars before any backend child.
# Large callers must use JUDGE_INPUT_BODY_FILE; no size cap on that path.
unset JUDGE_INPUT_BODY JR_INPUT_BODY JR_FINDINGS_BODY

FINDINGS_BODY_FILE="$TMP_DIR/findings-body.txt"
cat "$FINDINGS" > "$FINDINGS_BODY_FILE"

# Substitute placeholders via python — paths (small) in env/argv, bodies on disk.
export JR_INPUT_KIND="$INPUT_KIND"
export JR_INPUT_LABEL="$INPUT_LABEL"
export JR_INPUT_BODY_FILE="$INPUT_BODY_FILE"
export JR_FINDINGS_BODY_FILE="$FINDINGS_BODY_FILE"
RENDERED_PROMPT_FILE="$TMP_DIR/rendered-prompt.txt"
python3 - "$PROMPT" "$RENDERED_PROMPT_FILE" <<'PYEOF'
import os, sys
tpl = open(sys.argv[1]).read()
out = (tpl
       .replace('{{INPUT_KIND}}',    os.environ.get('JR_INPUT_KIND', ''))
       .replace('{{INPUT_LABEL}}',   os.environ.get('JR_INPUT_LABEL', ''))
       .replace('{{INPUT_BODY}}',    open(os.environ['JR_INPUT_BODY_FILE']).read())
       .replace('{{FINDINGS_BODY}}', open(os.environ['JR_FINDINGS_BODY_FILE']).read()))
open(sys.argv[2], 'w').write(out)
PYEOF

# After rendering, drop JR_* path helpers so they cannot leak into the child.
unset JR_INPUT_KIND JR_INPUT_LABEL JR_INPUT_BODY_FILE JR_FINDINGS_BODY_FILE

# Explicit key from fan-out (primary vs fallback), or invocation-unique default.
# Never rely solely on ambient inherited CONSILIUM_ARTIFACT_KEY.
if [[ -n "$ARTIFACT_KEY_ARG" ]]; then
    ARTIFACT_KEY="$ARTIFACT_KEY_ARG"
else
    ARTIFACT_KEY="judge.${AGENT}.$$.${RANDOM:-0}"
fi

RAW_OUT="$TMP_DIR/raw-out.txt"
RAW_ERR="$TMP_DIR/raw-err.txt"

# Drain-safe live stderr (no FIFO):
#   backend stdout → RAW_OUT
#   backend stderr → tee → live parent stderr + RAW_ERR
# Pipeline waits for tee; PIPESTATUS[0] is the backend status (not tee).
set +e
set +o pipefail
(
    export CONSILIUM_SKIP_OUTPUT_TEMPLATE=1
    export CONSILIUM_RUN_DIR="${CONSILIUM_RUN_DIR:-}"
    export CONSILIUM_ARTIFACT_KEY="$ARTIFACT_KEY"
    "$BACKEND_SCRIPT" \
        --mode review --agent-id "$AGENT" --role analyst \
        < "$RENDERED_PROMPT_FILE" 2>&1 1>"$RAW_OUT" | tee "$RAW_ERR" >&2
    ps=("${PIPESTATUS[@]}")
    exit "${ps[0]}"
)
rc=$?
set -e
set -o pipefail

if [[ $rc -ne 0 ]]; then
    echo -e "${RED}[judge/$AGENT] backend failed (exit $rc)${NC}" >&2
    # Live stderr already streamed via tee — do not re-print RAW_ERR.
    exit 3
fi

[[ -s "$RAW_OUT" ]] || { echo -e "${RED}[judge/$AGENT] empty output${NC}" >&2; exit 1; }

# Extract JSON object (strip ```json fences or grab first balanced {...}).
mkdir -p "$(dirname "$OUT")"
python3 - "$RAW_OUT" > "$OUT" <<'PYEOF'
import json, re, sys
raw = open(sys.argv[1]).read()
fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
candidate = fence.group(1) if fence else raw
if not fence:
    start = candidate.find("{")
    if start < 0:
        sys.stderr.write("no JSON object found in judge output\n"); sys.exit(2)
    depth = 0
    for i, c in enumerate(candidate[start:], start=start):
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                candidate = candidate[start:i+1]; break
    else:
        sys.stderr.write("unbalanced braces in judge output\n"); sys.exit(2)
try:
    obj = json.loads(candidate)
except Exception as e:
    sys.stderr.write(f"json parse failed: {e}\n"); sys.exit(2)
if "verdicts" not in obj or not isinstance(obj["verdicts"], list):
    sys.stderr.write("judge output missing 'verdicts' array\n"); sys.exit(2)
print(json.dumps(obj, indent=2))
PYEOF

[[ -s "$OUT" ]] || { echo -e "${RED}[judge/$AGENT] JSON extraction failed${NC}" >&2; exit 2; }
echo -e "${GREEN}[judge/$AGENT] ok → $OUT${NC}" >&2
exit 0
