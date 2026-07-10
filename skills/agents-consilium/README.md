# agents-consilium

> **A multi-agent orchestration skill** — fans out one query across **Codex**, **Claude Code**, **OpenCode** (OC-Go), and **Gemini CLI** in parallel, then hands the raw responses back to you. No debate, no committee answer — you adjudicate.

Different frontier models see different things. The union of their findings is materially broader than any single reviewer's.

---

## What you can run

| Mode | Use when… | Entry point | Cost (12KB file) |
|---|---|---|---|
| **Consensus query** | open-ended question — architecture, design, root-cause, brainstorming | `consensus-query.sh` | varies |
| **Code review** *(basic)* | quick file or diff review — security + correctness | `code-review.sh` | $0.10–0.30 |
| **Code review** *(specialists)* | high-stakes diff — adds performance + architecture + consistency | `code-review.sh --mode specialists` | $0.30–0.80 |
| **Superreview** | production-critical file — Pareto sweet-spot from the bench | `superreview.sh` | $0.90–1.50 |
| **Ultrareview** | maximum coverage, lowest false-positives | `ultrareview.sh` | $1.50–3.00 |

> **Pick a mode in 5 seconds:**
> - Talking through ideas → **Consensus query**
> - One PR file, normal review → **Code review (basic)**
> - Touches money / auth / persistence → **Code review (specialists)** or **Superreview**
> - Critical legacy code, no second human reviewer → **Ultrareview**

---

## Install

```bash
npx skills add CodeAlive-AI/ai-driven-development@agents-consilium -g -y
```

Then install at least **one** backend CLI (skill works with any subset):

| Backend | Install | Auth |
|---|---|---|
| [Codex CLI](https://github.com/openai/codex) | `npm i -g @openai/codex` | `codex` (ChatGPT login) |
| [OpenCode](https://opencode.ai) | see site | `opencode providers login opencode` (Zen) · `opencode-go` · or `GOOGLE_GENERATIVE_AI_API_KEY` (direct) |
| [Claude Code](https://docs.claude.com/claude-code) | see site | `claude /login` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `npm i -g @google/gemini-cli` | `GEMINI_API_KEY` |

---

## Quick start

```bash
# Brainstorming / architecture decisions — fan-out across enabled agents
scripts/consensus-query.sh "Should we use Postgres or SQLite for this CLI?"

# Code review of a file or diff
scripts/code-review.sh path/to/file.py
git diff HEAD | scripts/code-review.sh --xml --diff

# Multi-stage deep review (Pareto sweet-spot)
scripts/superreview.sh path/to/file.cs
```

<details>
<summary>More examples — agent overrides, XML output, dry runs</summary>

```bash
# Inspect what's enabled (no LLM calls)
scripts/consensus-query.sh --list-agents

# XML output for downstream agents
scripts/consensus-query.sh --xml "Review this function" < src/auth.py

# Code review — opt into the 5-specialist deep mode
scripts/code-review.sh --mode specialists path/to/file.py

# Ad-hoc agent selection — repeatable, globs supported
scripts/consensus-query.sh -a opencode-go-kimi "Q"           # one agent
scripts/consensus-query.sh -a 'opencode-go-*' "Q"            # all OC-Go models
scripts/consensus-query.sh -x codex "Q"                      # everything except codex
CONSILIUM_AGENTS='codex,opencode-go-kimi' scripts/code-review.sh file.py

# Multi-stage modes — dry-run validates config + plan without LLM calls
scripts/superreview.sh --dry-run path/to/file.cs
scripts/ultrareview.sh --no-fallback path/to/file.cs         # CI-strict mode
```

</details>

---

## How each mode works

<details>
<summary><b>Consensus query</b> — fan-out across heterogeneous models</summary>

Each agent has a `role` in config:

- **analyst** — Rigorous Analyst (precision, edge cases, implementation depth). Default: Codex, Claude Sonnet 5.
- **lateral** — Lateral Thinker (cross-domain patterns, questioning premises, creative alternatives). Default: OpenCode GLM-5.2, Gemini CLI.

Agents respond with a shared structure (Assessment / Key Findings / Blind Spots / Alternatives / Recommendation + confidence) so the caller can compare section by section.

</details>

<details>
<summary><b>Code review</b> — N specialist passes, caller adjudicates</summary>

Two sub-modes:

| Sub-mode | Specialists | Cost factor | When |
|---|---|---|---|
| `--mode basic` *(default)* | security + correctness *(2)* | 1× | every PR |
| `--mode specialists` | + performance + architecture + consistency *(5)* | ~2.5× | high-stakes diffs only |

Both run their N specialists in parallel across whichever agents are enabled (round-robin). Adding a 3rd/4th enabled agent does **not** add a 3rd/4th pass — cost stays fixed at N specializations.

Findings come back as XML:

```xml
<finding severity="critical|high|medium|low" category="security|correctness"
         file="..." line-start="N" line-end="N" confidence="0.0..1.0"
         source-agent="..." source-role="..." quote-valid="true|false">
  <title>…</title>
  <rationale><![CDATA[includes one reason this might be a false positive]]></rationale>
  <suggested-fix><![CDATA[…]]></suggested-fix>
  <quoted-code><![CDATA[verbatim source at line-start..line-end]]></quoted-code>
</finding>
```

Every `<quoted-code>` is cross-checked against the real file on disk — mismatches are flagged `quote-valid="false"` so you can drop probable hallucinations.

</details>

<details>
<summary><b>Superreview</b> — small-swarm + 2 frontier add-ons (10 LLM calls)</summary>

Pareto sweet-spot from the bench. Chosen by marginal-uplift analysis: the small-model base alone closes all `high`-severity issues; the 2 frontier picks were selected to add medium-severity gaps cheapest.

```
Stage 1: discovery-small (7 parallel)    Two cheap models in a 7-pass matrix
                                         (analyst + lateral + 4 specialists)
Stage 2: discovery-frontier (2 parallel) Frontier analyst + frontier lateral,
                                         hand-picked to maximise marginal recall
Stage 3: dedup (deterministic union)
Stage 4: judge                           Sonnet-class model (default)
```

</details>

<details>
<summary><b>Ultrareview</b> — broad-grid + specialists + probe (21 LLM calls)</summary>

Highest severity-weighted recall in the bench, lowest false-positive rate (a heavier judge does the filtering).

```
Stage 1: broad (4 parallel)         4 frontier analysts of different families
                                    (analyst-roled + one lateral)
Stage 2: specialists (15 parallel)  3 small models × 5 roles, uniform cap=10
                                    (security/correctness/performance/architecture/consistency)
Stage 3: probe (1, sequential)      Generic gap-probe — model picks the
                                    highest-risk defect class for THIS input
Stage 4: dedup
Stage 5: judge                      Opus-class judge, with fallback to a
                                    second model if the primary times out
```

The exact model bound to each slot lives in `config.json` and the script's hardcoded agent set — see `--dry-run` for the current binding.

</details>

**Both multi-stage modes** filter findings via the LLM judge before printing:

| Verdict | Action |
|---|---|
| `VALID` | kept |
| `DOWNGRADE` | kept, severity adjusted |
| `DUPLICATE` | dropped |
| `FALSE_POSITIVE` | dropped |

---

## Benchmark results

We benchmarked **9 review architectures** on a 65-issue C# pilot snippet. Severity weights: low=1, medium=3, high=9, critical=27 (max sev-w score = 191).

The two best architectures are now shipped:

| Skill mode | Architecture | Recall | Sev-weighted | Real cost |
|---|---|---:|---:|:---|
| `superreview.sh` | small-swarm + 2 frontier add-ons | 67.7% | **82.7%** | **$0.90–1.53** |
| `ultrareview.sh` | broad-grid + specialists + probe | **72.3%** | **86.4%** | $1.47–2.96 |

> **Why these two?** Superreview gets you 96% of ultrareview's severity-weighted recall at 55% the cost. Ultrareview wins on absolute coverage and FP rate (2/52). Pick by stakes, not by default.

<details>
<summary>Full scoreboard — all 9 architectures we tested</summary>

The `ID` column is an internal scoreboard handle (preset name in the harness) — kept here for reproducibility, not meaningful by itself.

| ID | Architecture | Recall | Sev-w | Real cost | Notes |
|----|---|---:|---:|:---|---|
| h3 | broad-grid + specialists + probe (= **ultrareview**) | 72.3% | **86.4%** | $1.47–2.96 | best sev-w + lowest FP |
| h7 | classifier-gated adaptive pipeline | **73.8%** | 85.9% | $1.98–3.59 | highest absolute recall, expensive, not shipped |
| h9 | small-swarm + 2 frontier add-ons (= **superreview**) | 67.7% | 82.7% | $0.90–1.53 | Pareto sweet-spot |
| h1 | frontier-broad + mixed-cap specialist sweep | 69.2% | 82.2% | $2.18–4.45 | dominated by h3 on every axis |
| h4 | peer-context cross-pollination (P2) | 61.5% | 81.7% | $2.33–4.46 | P2 mechanism didn't pay off |
| h8 | small-only set-cover (no frontier) | 61.5% | 78.5% | $0.73–1.08 | cheapest, but recall capped at 61% |
| h5 | role-partition (no cross-role bleed) | 58.5% | 76.4% | $1.40–2.30 | partition cost real signal |
| h6 | frontier-broad set-cover | 55.4% | 75.4% | $1.51–2.59 | 6 frontier + 3 specialists, overfit |
| h2 | specialists-only (no broad pass) | 60.0% | 73.8% | $1.16–1.67 | narrow findings, no broad context |

Total real cost across all 9 presets: **$13.66–$24.63**. Three presets needed fallback judging after the primary judge timed out on 200+ findings. The shipped `ultrareview.sh` now uses the current default OpenCode model as that fallback.

</details>

<details>
<summary>Per-reviewer contribution — which model contributes what</summary>

Aggregated across all 9 presets, per agent × role (MATCH = judge-confirmed match against ground truth):

| Agent | Best role | Bench appearances | Avg unique GT contributed |
|---|---|---:|---:|
| **Claude Sonnet 5** | `analyst` (45x lateral) | 6 presets | 37 unique GT (analyst mode) |
| **Codex gpt-5.5 (xhigh)** | `analyst` + specialist hybrid | 5 presets | up to 47 MATCH per pass |
| **OC-Go specialist model** | **architecture specialist** | 9 presets | 47 unique GT (specialist 4x analyst) |
| **OC-Go Qwen Plus** | `analyst` | 9 presets | 15 unique GT |
| **OpenCode lateral model** | **`lateral`** | 7 presets | rare but unique angles (arch/design) |
| **OC-Go Kimi** | `analyst` | 1 preset (evidence-thin) | 2 unique GT |

Default config roles are calibrated from this data, with the model ids updated to the current OpenCode roster.

</details>

---

## Configuration

Agents are declared in `config.json`. The default config enables:

- **codex** (`gpt-5.6-sol`, high) + **opencode** (`opencode-go/glm-5.2`)
- **5 additional OpenCode-Go models**: GLM-5.1 · Kimi K2.7 Code · MiniMax M3 · Qwen3.7 Max · Qwen3.7 Plus

Codex GPT-5.6 profiles included in both config files:

| Agent ID | Model | Effort | Intended use |
|---|---|---|---|
| `codex` | `gpt-5.6-sol` | `high` | Default quality-first code-review model |
| `codex-gpt-5.6` | `gpt-5.6` | `high` | Latest alias; wrapper resolves it to Sol |
| `codex-gpt-5.6-terra` | `gpt-5.6-terra` | `medium` | Balanced cost, latency, and quality |
| `codex-gpt-5.6-luna` | `gpt-5.6-luna` | `low` | High-throughput, simple, or strict-latency tasks |

Only `codex` is enabled among these profiles. The others are selectable with `-a <agent-id>` without increasing the default fan-out.

Each entry has 6 fields:

| Field | Purpose |
|---|---|
| `enabled` | Whether it joins `consensus-query` by default |
| `backend` | `codex-cli` · `gemini-cli` · `opencode` · `claude-code` |
| `model` | Model id passed to the CLI |
| `role` | `analyst` (precision) or `lateral` (creative) |
| `label` | Display name in reports |
| `effort` | Reasoning tier — provider-specific (see below) |

The exact `model` and `effort` of every entry live in `config.json` so they can be bumped without touching this README.

<details>
<summary>Reasoning-tier (<code>effort</code>) details per backend</summary>

- **opencode** — `low` / `medium` / `high` / `max` — maps to `opencode run --variant`. Provider-specific; enumerate via `opencode models <provider> --verbose`. See [SKILL.md → Discovering OpenCode reasoning variants](SKILL.md#discovering-opencode-reasoning-variants-per-model).
- **claude-code** — `low` / `medium` / `high` / `xhigh` / `max` — maps to `claude --effort`.
- **codex-cli** — `minimal` / `low` / `medium` / `high` / `xhigh` — maps to `model_reasoning_effort`.
- **gemini-cli** — `effort` is ignored.

`gemini-cli` and `claude-code` are disabled by default (flip `enabled: true` to add). Multiple agents can share one backend (e.g. five OpenCode-Go models all use `backend: "opencode"`); per-agent config is selected by the entry's id, passed through `CONSILIUM_AGENT_ID`.

Set `CONSILIUM_CONFIG=/path/to/custom.json` to use an override file. See `config.example.json` for a fuller template.

</details>

---

## Key features

- **Heterogeneous models** — different training distributions reduce shared blind spots
- **Read-only by default** — backends run with their native tools (Read/Grep/Glob/Bash read-only) but cannot Edit/Write. Enforced per backend via `--sandbox read-only` (Codex) / `--permission-mode plan` (Claude) / `--agent plan` (OpenCode) / `--approval-mode plan` (Gemini).
- **No coordinator, no debate** — caller adjudicates. Debate rounds empirically entrench errors.
- **Hypothesis → Validation → Fix-consistency workflow** — specialists must form a hypothesis, validate via path-feasibility / callers / project docs, then write a concrete fix and verify it eliminates the defect (drops when incoherent).
- **Hallucination + actionability gates** — findings must reference real symbols and carry a concrete fix
- **4-level severity rubric** — operational definitions, action horizons, security + correctness examples
- **Stable XML output** with CDATA — safe for downstream agent consumers
- **Differentiated exit codes** — agent callers can branch on failure mode

---

## Sources, methodology, structure

<details>
<summary>Research grounding</summary>

Code-review mode is grounded in the 2024–2026 agentic code-review literature:

- **VulAgent** (arXiv:2509.11523), **RepoAudit** (arXiv:2501.18160), **AgenticSCR** (arXiv:2601.19138) — hypothesis-validation workflow
- **LLM4PFA** (arXiv:2506.10322) — path-feasibility filter (72-96% SAST FP reduction)
- **CR-Bench** (arXiv:2603.11078) — debate loops lower precision; avoided
- **RovoDev** (arXiv:2601.01129, Atlassian Bitbucket production) — two-gate filter (hallucination + actionability); 38.7% comment resolution, −30.8% PR cycle time
- **Systematic Overcorrection** (arXiv:2603.00539) — fix-guided verification; "Full" prompting (explain + propose fix) outperforms direct judgment
- **Sphinx** (arXiv:2601.04252) — checklist-coverage metric (reusable as eval harness)
- **RevAgent** (arXiv:2511.00517) — critic-as-selector pattern (adjudicator selects, doesn't re-review)
- **Engagement in Code Review** (arXiv:2512.05309) — output format correlates with developer acceptance: locality, concrete fix, educational tone

Severity rubric synthesized from: CVSS v4.0 (FIRST), OWASP Risk Rating, GitHub Advisory Database, Chromium Security Severity Guidelines, Microsoft MSRC, SEI CERT (L1/L2/L3), SonarQube (Blocker/Critical/Major/Minor), Semgrep/CodeQL (SARIF error/warning/note).

</details>

<details>
<summary>File structure</summary>

```
agents-consilium/
├── SKILL.md                         # Agent-facing instructions (loaded on trigger)
├── README.md                        # This file
├── config.json                      # Default agent config
├── config.example.json              # Fuller template with all backends
├── prompts/                         # Multi-stage mode prompts
│   ├── broad-analyst.txt            # Rigorous-analyst broad pass
│   ├── broad-lateral.txt            # Lateral-thinker broad pass
│   ├── specialist.txt               # Parametric specialist (security/correctness/perf/arch/consistency)
│   ├── probe-generic.txt            # Generic gap-probe (model picks focus class)
│   └── judge.txt                    # Production judge (no GT — VALID/DUPLICATE/FP/DOWNGRADE)
└── scripts/
    ├── consensus-query.sh           # Parallel dispatch across enabled agents
    ├── code-review.sh               # 2- or 5-specialist code review (single-stage)
    ├── superreview.sh               # multi-stage: small-swarm + 2 frontier add-ons + sonnet judge
    ├── ultrareview.sh               # multi-stage: broad-grid + specialists + probe + sonnet judge (w/ fallback)
    ├── code_review_validate.py      # Parses findings, validates quoted-code, renders XML/markdown
    ├── common.sh                    # Shared role prompts, exit codes, helpers
    ├── config.sh                    # JSON config loader (Python-backed)
    ├── codex-query.sh               # Codex CLI backend
    ├── claude-query.sh              # Claude Code headless backend
    ├── opencode-query.sh            # OpenCode backend (Zen + Google direct)
    ├── gemini-query.sh              # Gemini CLI backend
    └── lib/                         # Shared building blocks for multi-stage modes
        ├── discovery-pass.sh        # One LLM discovery pass, tmp-isolated
        ├── judge-runner.sh          # LLM judge runner (no GT)
        └── dedup-findings.py        # Union per-pass XML files into one report
```

</details>

---

## Next

- See [SKILL.md](SKILL.md) for the agent-facing reference (loaded on trigger).
- New backend or model? Edit `config.json` — no code changes required.
- Want to verify pipeline structure without spending tokens? Both multi-stage modes have `--dry-run`.

## License

MIT
