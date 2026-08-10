# Configuration and execution

## Prerequisites

- Python 3
- At least one supported harness: Codex CLI, OpenCode, Claude Code, or native Grok Build
- Gemini CLI is optional and review-only

Authentication stays with each harness.

## Agent profiles

Profiles live in `config.json`; set `CONSILIUM_CONFIG` to use another file.

| Field | Purpose |
|---|---|
| `enabled` | Default participation in `review ask` and the basic review pool |
| `backend` | `codex-cli`, `claude-code`, `opencode`, `grok-build`, or `gemini-cli` |
| `model` | Backend model id |
| `role` | Analyst, lateral, or specialist role |
| `effort` | Backend reasoning effort/variant |
| `label` | Human-readable output label |
| `review_instructions` | Optional profile-specific instructions for non-raw review prompts |
| `supports_delegate` | Optional; set false for review-only profiles |

List effective profiles with:

```bash
scripts/consilium --list-agents
```

Non-empty environment values override profile model/effort for one invocation:

- `CODEX_MODEL`, `CODEX_EFFORT`
- `CLAUDE_MODEL`, `CLAUDE_EFFORT`
- `OPENCODE_MODEL`, `OPENCODE_EFFORT` (`none` omits the variant)
- `GROK_MODEL`, `GROK_EFFORT`
- `GEMINI_MODEL`

## Shell-safe prompts

Prefer `--prompt-file`, stdin, or a single-quoted heredoc for prompts containing backticks, `$`, `!`, or quotes. Double-quoted positional prompts are shell-expanded and may accidentally execute substitutions or leave a backend waiting on stdin.

```bash
scripts/consilium review ask --prompt-file prompt.md
scripts/consilium review ask "$(cat <<'EOF'
Explain `foo` and $PATH handling.
EOF
)"
```

The shell-interpolation warning applies only to positional prompts that still contain backticks or `$()`; file/stdin content is not warned.

## Environment variables

| Variable | Purpose |
|---|---|
| `CONSILIUM_CONFIG` | Alternate profile configuration |
| `CONSILIUM_AGENTS`, `CONSILIUM_EXCLUDE` | Default inclusion/exclusion selection |
| `CONSILIUM_PROGRESS` | Review progress: `full`, `compact`, or `none` |
| `CONSILIUM_OUTPUT_DIR`, `CONSILIUM_RUN_DIR` | Artifact locations |
| `CONSILIUM_SAVE_OUTPUTS` | Disable ordinary archival with `0`; steerable service artifacts remain |
| `CONSILIUM_STEER_DIR` | Steerable registry; reuse the same value for every control command |
| `CONSILIUM_MAX_PARALLEL` | Fan-out concurrency; `0` means unlimited/default |
| `CONSILIUM_DEBUG_EVENTS*` | Opt-in bounded event tape and its path/record/byte limits |
| `CONSILIUM_EXPLORE_ALLOW_LOCAL_REMOTE=1` | Permit `file://` sources for offline tests only |
| `CONSILIUM_EXPLORE_ALLOW_INSECURE=1` | Permit plain HTTP clone URLs |
| `GEMINI_API_KEY` | Gemini CLI authentication when required |

Consilium imposes no execution deadline in any mode. Provider context/output
limits and managed harness settings still apply.
