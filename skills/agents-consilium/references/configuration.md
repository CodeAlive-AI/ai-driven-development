# Configuration and execution

## Prerequisites

- Python 3
- At least one supported harness: Codex CLI, OpenCode, Claude Code, or native Grok Build
- Gemini CLI is optional and review-only
- Devin CLI is optional and opt-in: `devin` v3000.x on PATH, authenticated via `devin auth login`

Authentication stays with each harness.

## Agent profiles

Profiles live in `config.json`; set `CONSILIUM_CONFIG` to use another file.

| Field | Purpose |
|---|---|
| `enabled` | Default participation in `review ask` and the basic review pool |
| `backend` | `codex-cli`, `claude-code`, `opencode`, `grok-build`, `gemini-cli`, or `devin-cli` |
| `model` | Backend model id |
| `role` | Analyst, lateral, or specialist role |
| `effort` | Backend reasoning effort/variant |
| `label` | Human-readable output label |
| `review_instructions` | Optional profile-specific instructions for non-raw review prompts |
| `supports_delegate` | Optional; set false for review-only profiles |

List effective profiles with:

```bash
"$CONSILIUM" --list-agents
```

Non-empty environment values override profile model/effort for one invocation:

- `CODEX_MODEL`, `CODEX_EFFORT`
- `CLAUDE_MODEL`, `CLAUDE_EFFORT`
- `OPENCODE_MODEL`, `OPENCODE_EFFORT` (`none` omits the variant)
- `GROK_MODEL`, `GROK_EFFORT`
- `GEMINI_MODEL`
- `DEVIN_MODEL`; `CONSILIUM_BIN_DEVIN` overrides the `devin` binary

The built-in `codex` profile uses `gpt-6-astra` at `high` effort. Astra accepts
`low`, `medium`, `high`, `xhigh`, and `max`; it does not accept `none`. The
built-in `claude-fable` profile uses `claude-fable-5-1` at `low` effort and
supports the same five effort levels. Start Fable 5.1 at `high` for the hardest
long-horizon work, or retain `low` when it is one reviewer in a larger pool.
The disabled-by-default `opencode-go-muse-spark-1.3-contributor` and
`opencode-go-deepseek-v4.1-flash` profiles use the OpenCode Go catalog at
their maximum effort (`xhigh` for Muse and `max` for DeepSeek). Select either
explicitly with `-a`; keeping them disabled avoids changing the default review
pool. Muse supports `minimal`, `low`, `medium`, `high`, and `xhigh`; DeepSeek
supports `low`, `high`, and `max`. OpenCode Go's
privacy terms state that Muse Spark Contributor prompts and completions may be
used for model training, the service is not zero-data-retention, and availability
is region-limited. Check the current OpenCode Go terms before reviewing sensitive
repositories because catalog and privacy terms can change.

The disabled-by-default `devin` profile uses Devin CLI's `swe-2-high` model;
Devin versions effort into the model id, so there is no effort override. Both
one-shot and steerable paths run over `devin acp` (JSON-RPC 2.0 NDJSON on
stdio) — print mode `devin -p` is not used because a denied or
confirmation-required tool call silently cancels the session without final
text. Review runs `devin acp --agent-type review`, an agent with no write/edit
tools; yolo delegate runs the default agent type under `session/set_mode
bypass`. The helper strips inherited `ACP_BACKEND` from the child environment.

## Shell-safe prompts

Prefer `--prompt-file`, stdin, or a single-quoted heredoc for prompts containing backticks, `$`, `!`, or quotes. Double-quoted positional prompts are shell-expanded and may accidentally execute substitutions or leave a backend waiting on stdin.

```bash
"$CONSILIUM" review ask --prompt-file prompt.md
"$CONSILIUM" review ask "$(cat <<'EOF'
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
| `GEMINI_API_KEY` | Gemini CLI authentication when required |

Consilium imposes no execution deadline in any mode. Provider context/output
limits and managed harness settings still apply.

# Quota inspection

Use the read-only quota command to make scheduling decisions without starting a
review or delegate turn:

```bash
"$CONSILIUM" quota [all|codex|grok]
```

The output is a versioned JSON envelope. Codex is queried through
`account/rateLimits/read` on `codex app-server`; this does not consume an
available reset credit. Grok is queried through the official `/usage` command
in a temporary tmux session on `grok-aws`. Override the safe SSH alias with
`CONSILIUM_GROK_QUOTA_SSH_HOST` and the absolute remote working directory with
`CONSILIUM_GROK_QUOTA_CWD`.

When both providers are requested, one failure does not discard the successful
result. Exit `0` means all requested providers succeeded, `2` means partial
success, and `3` means all requested providers failed.
