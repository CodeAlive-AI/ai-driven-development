# agents-consilium

> Multi-agent **review** (read-only), single-agent **explore** (read-only repository context), and single-agent **delegate** (full YOLO) via one CLI: `scripts/consilium`.

Different frontier models see different things. Consilium fans out independent opinions or structured code reviews, explores an unfamiliar codebase and answers from cited evidence, or hands a whole task to one explicitly chosen agent.

---

## What you can run

| Mode | Use when… | Command | Cost (12KB file) |
|---|---|---|---|
| **review ask** | architecture, design, root-cause, brainstorm | `consilium review ask` | varies |
| **review code** *(basic)* | quick file/diff — security + correctness | `consilium review code` | $0.10–0.30 |
| **review code** *(specialists)* | high-stakes — + perf / architecture / consistency | `consilium review code --depth specialists` | $0.30–0.80 |
| **review code** *(super)* | production-critical — multi-stage + judge | `consilium review code --depth super` | $0.90–1.50 |
| **review code** *(ultra)* | maximum coverage | `consilium review code --depth ultra` | $1.50–3.00 |
| **explore** | understand a local or remote codebase, answer from evidence | `consilium explore [--repo SOURCE]` | varies |
| **delegate** | implement a task with one agent, no sandbox | `consilium delegate -a <id>` | varies |
| **delegate --steerable** | delegate while retaining live status/steer/cancel control | `consilium delegate -a <id> --steerable` | varies |
| **delegate --detach** | delegate something that should outlive the caller | `consilium delegate -a <id> --detach` | varies |
| **delegate wait / watch / list** | block on, follow, or rediscover a delegated run | `consilium delegate wait <run_id>` | — |

> **Pick in 5 seconds:** ideas → **ask** · normal PR file → **code basic** · money/auth → **specialists/super** · “how does this codebase work?” → **explore** · “just do it” → **delegate -a …**
>
> `review` looks for problems. `explore` looks for context. They are different jobs — explore never hunts for defects and never emits findings.

---

## Install

```bash
npx skills add CodeAlive-AI/ai-driven-development@agents-consilium -g -y
```

Install at least one backend CLI:

| Backend | CLI | Notes |
|---|---|---|
| Codex CLI | `codex` | ChatGPT login |
| OpenCode | `opencode` | OC-Go / provider auth |
| Claude Code | `claude` | `claude /login` |
| **Grok Build (native)** | `grok` | default Grok path (`backend: grok-build`) |
| Gemini CLI | `gemini` | review-only; needs `GEMINI_API_KEY` |

---

## Quick start

```bash
# Independent opinions
scripts/consilium review ask "Should we use Postgres or SQLite for this CLI?"

# Code review
scripts/consilium review code path/to/file.py
git diff HEAD | scripts/consilium review code --xml --diff
scripts/consilium review code --depth super path/to/file.cs

# Explore context — local tree, or a remote repo (cloned and cleaned up)
scripts/consilium explore "How is authentication wired up?"
scripts/consilium explore --repo owner/repository --ref v2.4.0 "How does the middleware pipeline work?"

# YOLO: one agent, current directory, no sandbox
scripts/consilium delegate -a grok "Add retry with exponential backoff to client.py"
```

<details>
<summary>More examples</summary>

```bash
scripts/consilium --list-agents
scripts/consilium review ask --xml --prompt-file prompt.md
scripts/consilium review ask -a codex,grok "Q"
scripts/consilium review ask -a 'opencode-go-*' -x opencode-go-minimax "Q"
scripts/consilium review code --depth specialists path/to/file.py
scripts/consilium review code --depth ultra --dry-run path/to/file.cs
scripts/consilium explore --repo ~/src/app "Where is the public API assembled?"
scripts/consilium explore --repo owner/repository --depth full --progress verbose --prompt-file question.md
scripts/consilium delegate -a codex --prompt-file task.md
scripts/consilium delegate -a grok --steerable "Implement the task"
# Capture run_id from stderr, then from another process:
scripts/consilium delegate steer run_<id> --mode auto "Additional detail"
scripts/consilium delegate status run_<id> --json

# Detached: survives the caller exiting; collect the answer whenever you like
RUN_ID=$(scripts/consilium delegate -a grok --detach "Implement the task")
scripts/consilium delegate list --active          # lost the run id?
scripts/consilium delegate watch "$RUN_ID"        # one line per meaningful change
scripts/consilium delegate wait  "$RUN_ID"        # blocks, prints the full answer
```

</details>

---

## Observability

- **stderr** — live `[consilium] …` progress (ordinary start lines include resolved model/effort; output is not buffered until end), keyed per invocation (`codex`, `codex.security`, `discovery-small.0.<agent>.<role>`)
- **progress style** — `--progress full|compact|none` on `review ask` and every `review code` depth (env `CONSILIUM_PROGRESS`); `explore` uses `compact|verbose|none`
- **stdout** — final answer only
- **artifacts** — `CONSILIUM_OUTPUT_DIR/run-<mode>-<word>-<word>-<hex>/{raw,normalized,final}/…` plus `final.txt`; run ids are human-readable word pairs, not UUIDs
- **steerable status** — resolved model/effort plus mailbox/backend lifecycle evidence for each steer
- **waiting** — `delegate wait` blocks to a terminal status and prints the full answer (exit `0` completed, `130` cancelled, `70` supervisor died, `75` your `--timeout` expired, `74` completed without text); `delegate watch` streams one line per meaningful change. Neither can hang on a dead supervisor, and neither cancels anything.

---

## Default agents (config.json)

| Id | Backend | Default |
|----|---------|---------|
| `codex` | codex-cli / gpt-5.6-sol high | enabled |
| `opencode-go-kimi-k3` | OpenCode Go / Kimi K3 max | enabled |
| **`grok`** | **grok-build / grok-4.5 high** | **enabled** |
| `claude-opus` | claude-code / claude-opus-5 medium | enabled |
| `claude-fable` | claude-code / claude-fable-5 low | enabled |
| all other profiles | … | disabled |

Edit `config.json` or set `CONSILIUM_CONFIG`.

Agent ids are configured profiles, not an exhaustive list of model/effort
pairs. To use an existing profile with a different reasoning effort for one
invocation, set the backend env override:

```bash
CLAUDE_EFFORT=medium scripts/consilium review ask -a claude-fable --prompt-file prompt.md
```

Do not substitute prompt wording such as "medium-depth review" for an actual
`*_EFFORT` override. In a fan-out, a backend env override applies to every
selected agent on that backend; use a temporary `CONSILIUM_CONFIG` profile if
only one same-backend agent should change.

| Backend | Model override | Effort override |
|---------|----------------|-----------------|
| Codex CLI | `CODEX_MODEL` | `CODEX_EFFORT` |
| Claude Code | `CLAUDE_MODEL` | `CLAUDE_EFFORT` |
| OpenCode | `OPENCODE_MODEL` | `OPENCODE_EFFORT` (`none` omits variant) |
| Grok Build | `GROK_MODEL` | `GROK_EFFORT` |
| Gemini CLI | `GEMINI_MODEL` | none |

---

## Safety model

| Mode | Enforcement |
|------|-------------|
| review | Per-backend sandbox / plan agent / tool denylist (Grok: `--sandbox read-only` **and** tool allowlist — permission-mode plan alone is not enough) |
| delegate | Documented YOLO flags; no sandbox; exact `-a` required |

### Transport note

Ordinary review and one-shot delegate use each harness's direct headless CLI.
Steerable delegate uses the harness's long-lived native interface: Codex app-server,
Claude stream-json replay, OpenCode loopback HTTP/SSE, or Grok Build ACP
(`grok agent stdio`). Review/delegate safety remains enforced by the selected
mode's harness flags and adapter contract.

### Limits

Consilium does not impose a timeout, maximum turn/step count, token budget, or
response-length cap by default. Large prompts use stdin or a prompt file rather
than argv, and complete raw/normalized/final outputs are archived without
truncation. Provider context windows and limits configured inside each harness
still apply. Set a positive `AGENT_TIMEOUT` only when an explicit watchdog is
wanted for ordinary review or one-shot delegate (`0` or unset means unlimited).
Steerable runs intentionally have no wrapper deadline; observe them with
`status` and stop them explicitly with `cancel`.

---

## Tests

```bash
scripts/tests/run.sh
```

Fake CLIs assert argv safety, per-harness model/effort resolution, agent
selection, stream extraction, artifacts, and steerable control behavior.

---

## Breaking changes in v5

1. Single public CLI: `scripts/consilium` (old shell entrypoints removed).
2. Modes: `review ask` / `review code --depth …` / `delegate -a …`.
3. Native Grok Build is the default Grok path (`grok` agent).
4. Explicit observability + artifact contract.
