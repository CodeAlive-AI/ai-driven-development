# agents-consilium

> Multi-agent **review** (read-only) and single-agent **delegate** (full YOLO) via one CLI: `scripts/consilium`.

Different frontier models see different things. Consilium fans out independent opinions or structured code reviews, or hands a whole task to one explicitly chosen agent.

---

## What you can run

| Mode | Use when… | Command | Cost (12KB file) |
|---|---|---|---|
| **review ask** | architecture, design, root-cause, brainstorm | `consilium review ask` | varies |
| **review code** *(basic)* | quick file/diff — security + correctness | `consilium review code` | $0.10–0.30 |
| **review code** *(specialists)* | high-stakes — + perf / architecture / consistency | `consilium review code --depth specialists` | $0.30–0.80 |
| **review code** *(super)* | production-critical — multi-stage + judge | `consilium review code --depth super` | $0.90–1.50 |
| **review code** *(ultra)* | maximum coverage | `consilium review code --depth ultra` | $1.50–3.00 |
| **delegate** | implement a task with one agent, no sandbox | `consilium delegate -a <id>` | varies |

> **Pick in 5 seconds:** ideas → **ask** · normal PR file → **code basic** · money/auth → **specialists/super** · “just do it” → **delegate -a …**

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
scripts/consilium delegate -a codex --prompt-file task.md
```

</details>

---

## Observability

- **stderr** — live `[consilium] …` progress (not buffered until end)
- **stdout** — final answer only
- **artifacts** — `CONSILIUM_OUTPUT_DIR/run-*/{raw,normalized,final}/…` plus `final.txt`

---

## Default agents (config.json)

| Id | Backend | Default |
|----|---------|---------|
| `codex` | codex-cli / gpt-5.6-sol high | enabled |
| `opencode` + OC-Go roster | opencode | enabled |
| **`grok`** | **grok-build / grok-4.5 high** | **enabled** |
| `opencode-xai-grok45` | opencode xAI fallback | disabled |
| `claude-*`, `gemini-cli` | … | disabled / review-only |

Edit `config.json` or set `CONSILIUM_CONFIG`.

---

## Safety model

| Mode | Enforcement |
|------|-------------|
| review | Per-backend sandbox / plan agent / tool denylist (Grok: `--sandbox read-only` **and** tool allowlist — permission-mode plan alone is not enough) |
| delegate | Documented YOLO flags; no sandbox; exact `-a` required |

### Transport note

Consilium drives backends via **direct headless CLI** (not ACP). Grok Build already has native ACP (`grok agent stdio`); a separate `grok-acp` is unnecessary. ACP is not the batch transport because review/delegate safety is CLI-flag enforcement, and Codex/Claude would need adapters — direct CLI is the uniform path with live stream observability.

---

## Tests

```bash
scripts/tests/run.sh
```

Fake CLIs assert argv safety, agent selection, stream extraction, and artifacts.

---

## Breaking changes in v5

1. Single public CLI: `scripts/consilium` (old shell entrypoints removed).
2. Modes: `review ask` / `review code --depth …` / `delegate -a …`.
3. Native Grok Build is the default Grok path (`grok` agent).
4. Explicit observability + artifact contract.
