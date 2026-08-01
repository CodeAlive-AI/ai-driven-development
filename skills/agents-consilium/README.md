# agents-consilium

Use other coding agents as subagents — even when your primary agent does not support their models.

Most coding agents can only spawn copies of themselves or a small built-in model set. `agents-consilium` removes that boundary. Any coding agent that can run the skill can call a different coding-agent CLI to research, plan, review, or implement work.

For example:

- send repository exploration to Grok 4.5 as a fast, cost-effective researcher;
- ask Claude Fable to produce an independent plan;
- delegate an implementation to Codex, Claude, Grok, or OpenCode;
- review the same change with several unrelated model families and compare what they find.

Each worker runs through its real coding-agent harness, with access to the tools and repository context appropriate for the selected mode. This is not role-play inside one model.

**Steering support:** long-running delegated agents are not fire-and-forget. You can send new guidance while they work, redirect the next turn, inspect status, watch progress, cancel a run, or detach and collect the result later.

## Three ways to use it

| Mode | What it does | Repository access |
|---|---|---|
| `review` | Gets independent opinions or reviews code with multiple agents | Read-only |
| `explore` | Lets one agent investigate a local or remote repository and answer from cited evidence | Read-only |
| `delegate` | Gives one exact agent a task, with optional live steering and detached execution | Full read/write access |

In short:

```text
Need several opinions?         review
Need to understand a repo?     explore
Need another agent to do it?   delegate
```

## Install

```bash
npx skills add CodeAlive-AI/ai-driven-development@agents-consilium -g -y
```

You also need Python 3 and at least one supported coding-agent CLI:

| Agent harness | Command | Supported modes |
|---|---|---|
| [Codex CLI](https://github.com/openai/codex) | `codex` | all |
| [Claude Code](https://docs.claude.com/claude-code) | `claude` | all |
| [OpenCode](https://opencode.ai) | `opencode` | all |
| [Grok Build](https://grok.x.ai) | `grok` | all |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `gemini` | review only |

Authentication stays with each CLI. If it already works in your terminal, Consilium can use it.

The examples below abbreviate the entrypoint as `scripts/consilium`. When running it manually, use the installed script's absolute path and keep your shell in the repository you want the worker to inspect or change.

## Quick start

List the configured workers:

```bash
scripts/consilium --list-agents
```

### Ask several model families

```bash
scripts/consilium review ask -a codex,grok,claude-fable \
  "Propose a migration plan from REST to event-driven processing."
```

The agents work independently. Their answers are returned under separate headings so your primary agent — or you — can compare them without an artificial consensus.

### Use Grok as a repository researcher

```bash
# Explore the current repository
scripts/consilium explore \
  "Trace authentication from the HTTP entry point to authorization checks."

# Explore a remote GitHub repository
scripts/consilium explore --repo owner/repository --ref main \
  "How are plugins discovered and loaded?"
```

`explore` uses Grok 4.5 by default. It returns a direct answer, repository-relative evidence, a small context map, and any gaps it could not verify. Remote repositories are cloned into an isolated temporary workspace and removed afterwards.

### Ask Claude Fable for a plan

```bash
scripts/consilium review ask -a claude-fable \
  "Create a step-by-step implementation plan for DESIGN.md. Do not edit files."
```

### Delegate real work to another agent

```bash
scripts/consilium delegate -a grok \
  "Implement the caching layer described in DESIGN.md and run the relevant tests."
```

`delegate` runs exactly one explicitly selected agent in the current directory and is steerable by default. It has no sandbox or approval prompts, so use it only when you intend to give that agent full control of the repository. Use `--one-shot` for the legacy direct execution path.

### Review code with independent specialists

```bash
# Security + correctness
scripts/consilium review code path/to/file.py

# Security, correctness, performance, architecture, and consistency
scripts/consilium review code --depth specialists path/to/file.py

# Review a diff
git diff HEAD | scripts/consilium review code --diff
```

For deeper, multi-stage reviews with a final judge, use `--depth super` or `--depth ultra`.

## Long-running delegation

Use `--detach` when work should continue after the calling session exits:

```bash
RUN_ID=$(scripts/consilium delegate -a grok --detach \
  "Implement the task in SPEC.md and run the test suite.")

scripts/consilium delegate watch "$RUN_ID"
scripts/consilium delegate wait "$RUN_ID"
```

Every normal delegate is steerable, so the caller can add guidance or change direction while the worker is running:

```bash
scripts/consilium delegate -a codex \
  "Refactor the storage layer."

# From another process, using the run_id printed at startup
scripts/consilium delegate steer run_<id> --mode auto \
  "Keep the public API backward compatible."
scripts/consilium delegate status run_<id> --json
scripts/consilium delegate cancel run_<id>
```

`list --active` recovers a lost run id. `wait` returns the full final answer and never cancels the worker.

## Using it from a coding agent

After installing the skill, ask your agent naturally:

```text
Use agents-consilium to have Grok explore this repository and explain
how background jobs are retried. Cite the relevant files.
```

```text
Ask Claude Fable and Codex for independent plans, compare the trade-offs,
then recommend one. Do not modify the repository.
```

```text
Delegate this implementation to Grok. Watch the run, collect its result,
then verify the changes and tests yourself.
```

The calling agent reads `SKILL.md`, selects the appropriate mode, launches the external worker, and evaluates its output. The external worker is a real process backed by the selected agent and model — not a built-in subagent with a renamed persona.

## Configuration

Agent profiles live in `config.json`. A profile chooses the harness, model, reasoning effort, display label, and whether it participates by default.

```json
{
  "agents": {
    "grok": {
      "enabled": true,
      "backend": "grok-build",
      "model": "grok-4.5",
      "effort": "high",
      "role": "analyst",
      "label": "Grok 4.5 (native, high)"
    }
  }
}
```

Edit `config.json` or point `CONSILIUM_CONFIG` to another file. Model and effort can also be overridden for one invocation:

```bash
CLAUDE_EFFORT=medium scripts/consilium review ask \
  -a claude-fable --prompt-file prompt.md
```

Available overrides: `CODEX_MODEL` / `CODEX_EFFORT`, `CLAUDE_MODEL` / `CLAUDE_EFFORT`, `OPENCODE_MODEL` / `OPENCODE_EFFORT`, `GROK_MODEL` / `GROK_EFFORT`, and `GEMINI_MODEL`.

## Safety and output

- `review` and `explore` are read-only and use each harness's sandbox or tool restrictions (mode capability matrix → `readonly`; unknown modes fail closed).
- `delegate` is intentionally full-access and requires an exact agent id; its execution mode defaults to steerable, while the agent id has no default and there is no multi-agent fan-out.
- Remote exploration blocks unsafe transports, does not fetch submodules or LFS payloads, and treats repository instructions as untrusted data.
- Live progress goes to stderr; the final answer goes to stdout. Normalized events use a closed ConsiliumEvent schema; unknown types are not persisted.
- Complete run artifacts are saved under `CONSILIUM_OUTPUT_DIR` unless `CONSILIUM_SAVE_OUTPUTS=0`.
- There is no timeout, token budget, or fan-out concurrency limit by default. Set `AGENT_TIMEOUT` for a one-shot watchdog, or `CONSILIUM_MAX_PARALLEL=N` to bound review fan-out. Opt-in `CONSILIUM_DEBUG_EVENTS=1` writes a bounded RAW→FINAL event tape.

## Command map

```bash
scripts/consilium review ask [...]
scripts/consilium review code --depth basic|specialists|super|ultra [...]
scripts/consilium explore [--repo SOURCE] [--ref REF] [...]
scripts/consilium delegate -a <exact-agent-id> [...]
scripts/consilium delegate -a <exact-agent-id> --steerable|--one-shot|--detach [...]
scripts/consilium delegate steer|status|cancel|wait|watch|list [...]
scripts/consilium --list-agents
```

The full operational contract, backend flags, exit codes, progress formats, and steering semantics are documented in [`SKILL.md`](SKILL.md).

## Tests

```bash
scripts/tests/run.sh
```

The default suite uses fake backend CLIs, runs offline, and does not spend model tokens.
