# Review mode

Use review for independent opinions or defect finding. Review is always read-only. Consilium keeps agents independent; it does not merge or rank answers from `ask`, `basic`, or `specialists`. The calling agent judges them. `super` and `ultra` deliberately add an LLM judge after deterministic deduplication.

## Ask

```bash
scripts/consilium review ask "Should we use Postgres or SQLite?"
scripts/consilium review ask --xml --prompt-file prompt.md
scripts/consilium review ask -a codex,grok "Review this approach"
scripts/consilium review ask -a 'opencode-go-*' -x opencode-go-minimax "Q"
scripts/consilium review ask --progress compact -a codex,grok "Q"
```

Each agent's answer is returned under its own heading.

## Code review depths

```bash
scripts/consilium review code path/to/file.py
scripts/consilium review code --depth specialists --xml path/to/file.py
git diff HEAD | scripts/consilium review code --diff
scripts/consilium review code --depth super path/to/file.cs
scripts/consilium review code --depth ultra --dry-run path/to/file.cs
```

| Depth | Use when | Work performed |
|---|---|---|
| `basic` (default) | Routine file or diff review | Security + correctness; fixed two passes with quoted-code validation |
| `specialists` | Broader mid-cost coverage is wanted without a judge | Adds performance, architecture, and consistency |
| `super` | High-risk or release-blocking review; recommended high-stakes default | Multi-stage discovery, deterministic deduplication, and an LLM judge |
| `ultra` | The user explicitly prioritizes maximum coverage over cost and latency | Maximum multi-stage discovery and an LLM judge |

Choose one depth for a review. Do not run every depth sequentially.

Do not invoke Grok's `/review` slash command. Consilium owns review semantics.

## Agent profiles and runtime effort

`--list-agents` shows configured profiles, not every model/effort combination. Select an exact profile and use a backend environment override when its model is right but its effort is not. Prompt wording such as “medium-depth review” does not change backend reasoning effort.

```bash
CLAUDE_EFFORT=medium scripts/consilium review ask \
  -a claude-fable --prompt-file prompt.md
```

| Backend | Model override | Effort override | CLI mapping |
|---|---|---|---|
| Codex CLI | `CODEX_MODEL` | `CODEX_EFFORT` | `--model`, `model_reasoning_effort` |
| Claude Code | `CLAUDE_MODEL` | `CLAUDE_EFFORT` | `--model`, `--effort` |
| OpenCode | `OPENCODE_MODEL` | `OPENCODE_EFFORT` | `-m`, `--variant`; `none` omits variant |
| Grok Build | `GROK_MODEL` | `GROK_EFFORT` | `-m`, `--reasoning-effort` |
| Gemini CLI | `GEMINI_MODEL` | none | `--model` |

In fan-out, an environment override affects every selected profile on that backend. Use a temporary `CONSILIUM_CONFIG` profile when only one same-backend agent should change.

## Progress and outputs

`review ask` and every code-review depth accept `--progress`; `CONSILIUM_PROGRESS` is the environment fallback.

The CLI default remains `full`. Agent callers should normally use `compact`,
as recommended in `SKILL.md`, unless live content previews are specifically
useful.

| Style | stderr |
|---|---|
| `full` (default) | Live per-agent thinking and answer previews |
| `compact` | Content-free liveness counters only |
| `none` | No stage, pass, or model progress; failures and stdout report remain |

Invocation-specific keys distinguish parallel passes of the same agent and match their artifact keys. Large fan-outs can set `CONSILIUM_MAX_PARALLEL=N`; `0` is unlimited and remains the default.

## Exit codes

For `review ask`, `basic`, and `specialists`: `0` all succeeded; `2` partial result; `3` all failed; `4` configuration error; `5` usage error. Partial code-review reports are still emitted from successful specialists.
