#!/bin/bash
#
# explore — single-agent, read-only context exploration of a local or remote repo.
# Invoked by: scripts/consilium explore [options] ["question"]
#
# explore is not review. It does not look for defects, does not score anything,
# and never loads review roles, review_instructions, or the Assessment/Blind
# Spots/Recommendation template. It builds a relevance-first map of the context
# a question actually depends on, and answers from cited evidence.
#
# Lifecycle:
#   resolve source → (clone) → collect provenance → run one agent → cleanup
#
# Observability contract (same as the rest of consilium):
#   progress → stderr    final answer → stdout    artifacts → CONSILIUM_RUN_DIR
#
set -euo pipefail

LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "$LIB_DIR/../.." && pwd)"
# shellcheck source=common.sh
source "$LIB_DIR/common.sh"
# shellcheck source=config.sh
source "$LIB_DIR/config.sh"
# shellcheck source=progress.sh
source "$LIB_DIR/progress.sh"
# shellcheck source=artifacts.sh
source "$LIB_DIR/artifacts.sh"

DEFAULT_AGENT="grok"

REPO_SPEC="."
REF=""
AGENT_ID=""
PROMPT=""
PROMPT_FILE=""
PROMPT_SOURCE=""
DEPTH="1"
PROGRESS="compact"
KEEP_CLONE=0

usage() {
    cat <<'EOF'
Usage: consilium explore [options] ["question"]

Explore a repository's context and answer a question from cited evidence.
Read-only. Exactly one agent. Never reviews, never hunts for defects.

Options:
  --repo SOURCE          Local path, owner/repo (GitHub), or git URL (default: .)
  --ref REF              Branch, tag, or commit — remote sources only
  -a, --agent ID         Exact agent id (default: grok). Non-Grok agents run with
                         reduced isolation; see SKILL.md.
  --prompt-file FILE     Question from a file
  --depth N|full         Clone depth for remote sources (default: 1)
  --progress compact|verbose|none
                         Live progress detail on stderr (default: compact).
                         Never includes chain-of-thought or the answer body.
  --keep-clone           Do not delete the clone; print its path (debugging)
  -h, --help

Examples:
  consilium explore "How is authentication wired up?"
  consilium explore --repo ~/src/app "Where is the public API assembled?"
  consilium explore --repo owner/repository "What handles incremental builds?"
  consilium explore --repo owner/repository --ref v2.4.0 --prompt-file q.md

Exit codes: 0 ok · 4 config · 5 usage · 6 source error · other = backend exit.
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --repo)         shift; REPO_SPEC="${1:-}"; shift ;;
        --repo=*)       REPO_SPEC="${1#--repo=}"; shift ;;
        --ref)          shift; REF="${1:-}"; shift ;;
        --ref=*)        REF="${1#--ref=}"; shift ;;
        --depth)        shift; DEPTH="${1:-}"; shift ;;
        --depth=*)      DEPTH="${1#--depth=}"; shift ;;
        --progress)     shift; PROGRESS="${1:-}"; shift ;;
        --progress=*)   PROGRESS="${1#--progress=}"; shift ;;
        --keep-clone)   KEEP_CLONE=1; shift ;;
        --prompt-file)  shift; PROMPT_FILE="${1:-}"; PROMPT_SOURCE="file"; shift ;;
        -a|--agent)
            shift
            if [[ -z "${1:-}" ]]; then
                echo "Error: -a requires an exact agent id" >&2
                exit $EXIT_USAGE
            fi
            # Exploration is single-agent by design: one coherent context map,
            # not N partial ones the caller has to reconcile.
            if [[ "$1" == *'*'* || "$1" == *'?'* || "$1" == *','* || "$1" == *'['* ]]; then
                echo "Error: explore requires an exact agent id (no globs/lists). Got: $1" >&2
                exit $EXIT_USAGE
            fi
            if [[ -n "$AGENT_ID" ]]; then
                echo "Error: explore accepts exactly one -a <agent-id>" >&2
                exit $EXIT_USAGE
            fi
            AGENT_ID="$1"
            shift
            ;;
        -h|--help)      usage; exit $EXIT_OK ;;
        --)             shift; PROMPT="${1:-}"; PROMPT_SOURCE="positional"; break ;;
        -*)             echo "Error: unknown flag: $1" >&2; exit $EXIT_USAGE ;;
        *)              PROMPT="$1"; PROMPT_SOURCE="positional"; shift; break ;;
    esac
done

case "$PROGRESS" in
    compact|verbose|none) ;;
    *)
        echo "Error: --progress must be compact, verbose, or none (got: $PROGRESS)" >&2
        exit $EXIT_USAGE
        ;;
esac

AGENT_ID="${AGENT_ID:-$DEFAULT_AGENT}"

# ---------------------------------------------------------------------------
# question
# ---------------------------------------------------------------------------

if [[ -n "$PROMPT_FILE" ]]; then
    if [[ -n "$PROMPT" ]]; then
        echo "Error: cannot combine --prompt-file with a positional question" >&2
        exit $EXIT_USAGE
    fi
    [[ -r "$PROMPT_FILE" ]] || { echo "Error: prompt file not readable: $PROMPT_FILE" >&2; exit $EXIT_USAGE; }
    PROMPT="$(cat -- "$PROMPT_FILE")"
    PROMPT_SOURCE="file"
fi

if [[ -z "$PROMPT" && ! -t 0 ]]; then
    PROMPT="$(cat)"
    PROMPT_SOURCE="stdin"
fi

if [[ -z "$PROMPT" ]]; then
    echo "Error: no question provided" >&2
    exit $EXIT_USAGE
fi

if [[ "$PROMPT_SOURCE" == "positional" ]]; then
    warn_shell_special_in_prompt "$PROMPT"
fi

# ---------------------------------------------------------------------------
# agent validation
# ---------------------------------------------------------------------------

config_validate || exit $EXIT_CONFIG_ERROR

if ! BACKEND="$(config_get_field "$AGENT_ID" backend 2>/dev/null)"; then
    echo "Error: unknown agent id: $AGENT_ID" >&2
    exit $EXIT_CONFIG_ERROR
fi

# Every isolation guarantee explore advertises — neutral CWD, kernel sandbox
# profile, no memory, no subagents, no web — is implemented with Grok Build
# flags. Other backends still run read-only, but they get their review-grade
# posture, which is a materially weaker promise. Say so instead of implying
# uniform safety.
ISOLATION_LEVEL="full"
if [[ "$BACKEND" != "grok-build" ]]; then
    ISOLATION_LEVEL="reduced"
fi

# ---------------------------------------------------------------------------
# source resolution
# ---------------------------------------------------------------------------

export CONSILIUM_MODE="explore"
export CONSILIUM_SINGLE_AGENT=1

progress_stage "explore" "agent=$AGENT_ID repo=$REPO_SPEC${REF:+ ref=$REF}"
progress_info "resolve" "source=$REPO_SPEC"

RESOLVE_ARGS=(--repo "$REPO_SPEC" --depth "$DEPTH")
[[ -n "$REF" ]] && RESOLVE_ARGS+=(--ref "$REF")

RESOLVED_JSON="$(mktemp "${TMPDIR:-/tmp}/consilium-explore-src.XXXXXX")"
set +e
python3 "$LIB_DIR/source_resolver.py" "${RESOLVE_ARGS[@]}" > "$RESOLVED_JSON"
resolve_rc=$?
set -e
if [[ $resolve_rc -ne 0 ]]; then
    rm -f "$RESOLVED_JSON"
    exit $EXIT_SOURCE_ERROR
fi

# Read resolver output into shell variables in one pass.
eval "$(python3 - "$RESOLVED_JSON" <<'PY'
import json, shlex, sys
d = json.load(open(sys.argv[1]))
def emit(name, value):
    if value is None:
        text = ""
    elif isinstance(value, bool):
        text = "true" if value else "false"
    else:
        text = str(value)
    print(f"{name}={shlex.quote(text)}")
emit("SRC_KIND", d["source_kind"])
emit("SRC_URL_REDACTED", d.get("source_url_redacted"))
emit("SRC_WORKSPACE", d.get("workspace"))
emit("SRC_ROOT", d["exploration_root"])
emit("SRC_AGENT_CWD", d["agent_cwd"])
emit("SRC_REL", d.get("source_rel") or ".")
emit("SRC_ISOLATION", d.get("isolation"))
emit("SRC_COMMIT", (d.get("git") or {}).get("resolved_commit"))
emit("SRC_BRANCH", (d.get("git") or {}).get("branch"))
emit("SRC_SHALLOW", (d.get("git") or {}).get("shallow"))
emit("SRC_DIRTY", (d.get("git") or {}).get("dirty"))
emit("SRC_STRATEGY", d.get("clone_strategy"))
PY
)"

CLONE_KEPT=0
cleanup_explore() {
    local rc=$?
    rm -f "$RESOLVED_JSON" "${PROMPT_PATH:-}" 2>/dev/null || true
    if [[ -n "${SRC_WORKSPACE:-}" && -d "${SRC_WORKSPACE:-}" ]]; then
        if [[ "$KEEP_CLONE" -eq 1 ]]; then
            CLONE_KEPT=1
            progress_info "cleanup" "clone kept at $SRC_WORKSPACE/source"
        else
            rm -rf "$SRC_WORKSPACE"
            progress_info "cleanup" "workspace removed"
        fi
    fi
    return $rc
}
# Cover the signal paths too: an interrupted explore must not leave a clone of
# somebody else's repository sitting in TMPDIR.
trap cleanup_explore EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

if [[ "$SRC_KIND" == "remote" ]]; then
    progress_info "source" "remote=$SRC_URL_REDACTED strategy=$SRC_STRATEGY commit=${SRC_COMMIT:0:12}"
else
    progress_info "source" "kind=$SRC_KIND root=$SRC_ROOT commit=${SRC_COMMIT:0:12}${SRC_DIRTY:+ dirty=$SRC_DIRTY}"
fi

if [[ "$ISOLATION_LEVEL" == "reduced" ]]; then
    echo -e "${YELLOW}[consilium] WARNING: agent '$AGENT_ID' (backend $BACKEND) does not support" >&2
    echo -e "  explore's isolation flags. It runs read-only, but repository-local agent" >&2
    echo -e "  configuration (AGENTS.md, CLAUDE.md) may be discovered while reading files," >&2
    echo -e "  and memory, subagents, and web access follow that backend's own defaults." >&2
    echo -e "  Use the default Grok agent for untrusted repositories.${NC}" >&2
fi

# ---------------------------------------------------------------------------
# prompt assembly
# ---------------------------------------------------------------------------

PROMPT_PATH="$(mktemp "${TMPDIR:-/tmp}/consilium-explore-prompt.XXXXXX")"
chmod 600 "$PROMPT_PATH"

{
    cat "$SKILL_ROOT/prompts/explore.txt"
    printf '\n---\n\n## Repository facts (collected by the orchestrator, not by you)\n\n'
    python3 - "$RESOLVED_JSON" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
g = d.get("git") or {}
inv = d.get("inventory") or {}
rel = d.get("source_rel") or "."
root_desc = "the current working directory" if rel == "." else f"the `{rel}/` subdirectory of the working directory"

print(f"- Exploration root: {root_desc}. All citations must be relative to it.")
print(f"- Source kind: {d['source_kind']}")
if d.get("source_url_redacted"):
    print(f"- Origin: {d['source_url_redacted']}")
if d.get("requested_ref"):
    print(f"- Requested ref: {d['requested_ref']}")
if g.get("resolved_commit"):
    print(f"- Resolved commit: {g['resolved_commit']}")
if g.get("branch"):
    print(f"- Branch: {g['branch']}")
if g.get("commit_subject"):
    date = f" ({g['commit_date']})" if g.get("commit_date") else ""
    print(f"- HEAD commit{date}: {g['commit_subject']}")
if g.get("shallow"):
    print("- Shallow checkout: history before HEAD is NOT available. Do not reason about it.")
if g.get("dirty"):
    print("- Working tree has uncommitted changes: what you read may differ from the commit above.")
if not g.get("is_git"):
    print("- Not a git repository: no commit, branch, or history information exists.")

print()
print(f"### File inventory — {inv.get('total_files', 0)} files ({inv.get('source', 'n/a')})")
if inv.get("truncated"):
    print()
    print("This inventory is a directory-level rollup, NOT a complete file list. "
          "Individual files are omitted; use list_dir to descend into a directory "
          "that looks relevant.")
print()
print("```")
print(inv.get("body", ""))
print("```")
PY
    printf '\n---\n\n## Question\n\n'
    printf '%s\n' "$PROMPT"
} > "$PROMPT_PATH"

# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------

artifacts_init_run "explore"

# Provenance: extend the run's meta.json with everything needed to reproduce or
# audit this exploration. Never write the unredacted URL.
if [[ -n "${CONSILIUM_RUN_DIR:-}" ]]; then
    CONSILIUM_RUN_DIR="$CONSILIUM_RUN_DIR" \
    EXPLORE_AGENT="$AGENT_ID" EXPLORE_BACKEND="$BACKEND" \
    EXPLORE_ISOLATION="$ISOLATION_LEVEL" EXPLORE_PROGRESS="$PROGRESS" \
    EXPLORE_KEEP="$KEEP_CLONE" EXPLORE_CALLER_CWD="$(pwd)" \
    EXPLORE_PROMPT_PATH="$PROMPT_PATH" EXPLORE_QUESTION="$PROMPT" \
    python3 - "$RESOLVED_JSON" <<'PY' 2>/dev/null || true
import hashlib, json, os, sys

run_dir = os.environ["CONSILIUM_RUN_DIR"]
meta_path = os.path.join(run_dir, "meta.json")
try:
    meta = json.load(open(meta_path))
except Exception:
    meta = {}

src = json.load(open(sys.argv[1]))
g = src.get("git") or {}
model = os.environ.get("GROK_MODEL") or ""

meta.update({
    "mode": "explore",
    "agent_id": os.environ["EXPLORE_AGENT"],
    "backend": os.environ["EXPLORE_BACKEND"],
    "isolation": os.environ["EXPLORE_ISOLATION"],
    "source_kind": src["source_kind"],
    "source_input": src["source_input"],
    "source_url_redacted": src.get("source_url_redacted"),
    "requested_ref": src.get("requested_ref"),
    "resolved_commit": g.get("resolved_commit"),
    "branch": g.get("branch"),
    "shallow": g.get("shallow"),
    "dirty": g.get("dirty"),
    "clone_depth": src.get("clone_depth"),
    "clone_strategy": src.get("clone_strategy"),
    "caller_cwd": os.environ["EXPLORE_CALLER_CWD"],
    "exploration_root": src["exploration_root"],
    "agent_cwd": src["agent_cwd"],
    "inventory_total_files": (src.get("inventory") or {}).get("total_files"),
    "inventory_truncated": (src.get("inventory") or {}).get("truncated"),
    "progress_style": os.environ["EXPLORE_PROGRESS"],
    "clone_kept": os.environ["EXPLORE_KEEP"] == "1",
    "question_sha256": hashlib.sha256(
        os.environ["EXPLORE_QUESTION"].encode("utf-8")
    ).hexdigest(),
})
if model:
    meta["model_override"] = model

with open(meta_path, "w") as f:
    json.dump(meta, f, indent=2)
    f.write("\n")
PY
fi

# Progress style: never `full` — that would stream chain-of-thought and the
# answer body onto stderr, which exploration explicitly must not do.
case "$PROGRESS" in
    compact) export CONSILIUM_PROGRESS_STYLE=compact; export CONSILIUM_PROGRESS_INTERVAL=10 ;;
    verbose) export CONSILIUM_PROGRESS_STYLE=compact; export CONSILIUM_PROGRESS_INTERVAL=2 ;;
    none)    export CONSILIUM_PROGRESS_STYLE=none ;;
esac

if [[ "$BACKEND" == "grok-build" ]]; then
    export CONSILIUM_EXPLORE_CWD="$SRC_AGENT_CWD"
    # An isolated workspace holds a clone nobody vetted: constrain filesystem
    # reach to it. A trusted local tree keeps read-only, which is the same
    # posture review already uses in the user's own repository.
    if [[ "$SRC_ISOLATION" == "isolated-workspace" ]]; then
        export CONSILIUM_EXPLORE_SANDBOX="strict"
    else
        export CONSILIUM_EXPLORE_SANDBOX="read-only"
    fi
fi

progress_info "exploring" "agent=$AGENT_ID isolation=$ISOLATION_LEVEL cwd=$SRC_AGENT_CWD"

cd "$SRC_AGENT_CWD"

set +e
"$LIB_DIR/backend_run.sh" --mode explore --agent-id "$AGENT_ID" --raw --prompt-file "$PROMPT_PATH"
RC=$?
set -e

if [[ "$KEEP_CLONE" -eq 1 && -n "${SRC_WORKSPACE:-}" ]]; then
    progress_info "artifacts" "clone retained: $SRC_WORKSPACE/source"
fi

exit $RC
