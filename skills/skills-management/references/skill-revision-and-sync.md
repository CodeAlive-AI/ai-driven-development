# Skill Revision, Topology Reconciliation & Usage Telemetry

Use `scripts/revise_skills.py` (100% read-only diagnostics) and `scripts/sync_skills.py` (quarantine-backed reconciler, `--dry-run` by default) to keep large multi-agent skill libraries healthy.

## Contents

- [When to run revision vs duplicate audit](#when-to-run-revision-vs-duplicate-audit)
- [Usage telemetry modes (`fast` vs `deep`)](#usage-telemetry-modes-fast-vs-deep)
- [Discovery-Pool availability matrix](#discovery-pool-availability-matrix)
- [Porch harness parity & traps](#porch-harness-parity--traps)
- [Reconciling safely with quarantine undo](#reconciling-safely-with-quarantine-undo)

---

## When to run revision vs duplicate audit

- Run **`revise_skills.py`** for full-system hygiene:
  - Broken symlinks & symlink loops (with git rename/consolidation detection so merged skills like `hooks-management -> coding-agents-management` are never blindly repointed).
  - **Ghost directories** without `SKILL.md` (e.g., leftover `__pycache__` folders after renames), while respecting **Hermes** 2-level category folders (`apple/apple-notes/SKILL.md`) and `.bundled_manifest`.
  - **Orphaned lockfile entries** in `~/.agents/.skill-lock.json` and workspace `skills-lock.json` (cleaning symlinks without cleaning `.skill-lock.json` causes `npx skills update` to re-download deleted skills).
  - **Local ↔ Global shadowing & monorepo ancestor walks** (`--scope local|global|all`, `--cwd PATH`, `--scan-skills-dirs`).
  - **4-axis duplicate detection**: exact `name`, folder basename (`dir_name`), normalized slug, and identical directory SHA-256 across different names.
  - **Startup Context Budget** per agent (`name + description` chars/tokens against truncation & catalog caps) and **Trojan Source** invisible/BiDi Unicode checks. For deep third-party security analysis, run the dedicated `skill-inspector` skill.
- Run **`audit_skill_duplicates.py --candidate PATH --fail-on-conflict`** as the fast preflight before installing a single skill.

---

## Usage telemetry modes (`fast` vs `deep`)

Large agent stores easily grow to tens of gigabytes across 14+ harnesses. Both modes are strictly read-only (`mode=ro`, `PRAGMA query_only=ON`) and avoid shelling into slow full-store `grep` scans or triggering `porch` index lock waits:

| Mode | Speed | What it reads | Coverage caveats |
|---|---|---|---|
| `--usage off` | Instant | Filesystem & lockfiles only | No usage stats |
| `--usage fast` *(default)* | < 300 ms | `~/.claude/history.jsonl`, `~/.codex/history.jsonl`, `~/.grok/.../prompt_history.jsonl`, plus `porch` `index-v1.sqlite` (read-only, no `sync()`) | Captures explicit `/skill` and `$skill` triggers; coverage depends on `index-v1.sqlite` completeness (printed inline) |
| `--usage deep --since 30d` | Bounded + cached | Native transcripts pruned by `st_mtime >= since` (JSONL/JSONL.zst) + time-filtered SQL queries (`opencode.db`, `devin/sessions.db`, `hermes/state.db`), memoized in `~/.cache/skills-management/usage-v1.json` | Counts **deduplicated canonical sessions** (`explicit` vs `agent`), includes OpenCode `type='skill'`, excludes `>8` `SKILL.md` reads/session (bulk audits) |

---

## Discovery-Pool availability matrix

By default, `revise_skills.py` shows **Anomaly-First Triage** (`--all` shows every healthy skill) and collapses agents that read `~/.agents/skills` into `Shared(~/.agents)` alongside dedicated/overriding roots (`AGY`, `Claude`, `Qwen`, `Hermes`, `Grok`, `Devin`, `OMP`, plus `Local`; pass `--expand-agents` for all columns):

- `link`: direct 1-hop symlink to canonical directory
- `hop2`: chained (`>=2` hops) or relative symlink
- `copy`: standalone real directory
- `shrd`: inherited via `~/.agents/skills` (plus Hermes `skills.external_dirs` when configured)
- `plug` / `bndl` / `locl`: plugin / Hermes bundled / workspace skill
- `BRKN` / `GHST` / `DRFT` / `SHDW` / `—`: broken link / missing `SKILL.md` / divergent copy / local shadows global / absent

---

## Porch harness parity & traps

`agents.py` maps every skill-consuming `porch` harness via `AGENT_ALIASES` (accepting `agy`, `gemini`, `hermes`, `kimi-code`, `grok-build`, `codex-cli`, `cursor-cli`, `devin-cli`, `claude-desktop`):

- **`antigravity` vs `antigravity-cli` (`agy`)**: App/IDE reads `~/.gemini/config/skills` globally (`reads_shared_global=False`), whereas `agy` also falls back to `~/.agents/skills` (`reads_shared_global=True`). Put links in `~/.gemini/config/skills` pointing **directly** (1-hop) to canonical sources rather than chaining through `~/.agents/skills`.
- **`claude-desktop`**: Code tab shares `~/.claude/skills`; Cowork sessions are ephemeral/cloud-managed.
- **`omp` (Oh My Pi)** vs **`pi`**: `omp` reads `~/.omp/agent/skills` (`extra_global_dirs=["~/.omp/skills", "~/.omp/agent/managed-skills"]`), `~/.agents/skills`, and `.omp/skills` + `.agents/skills`.
- **`porch`**: Orchestrator over worker harnesses — `install_skill.py` and `sync_skills.py` refuse `--agent porch` and direct you to target harnesses.

---

## Reconciling safely with quarantine undo

Every `sync_skills.py` command runs as **`--dry-run` (`staged`)** unless `--apply` is given:

```bash
# 1. Preview zero-risk hygiene (broken links + ghost dirs + .skill-lock.json orphans) + hop collapse
uv run scripts/sync_skills.py --prune-broken --collapse-hops

# 2. Preview safe exact-name repointing against local repos
uv run scripts/sync_skills.py --repoint-broken --source-root ~/my-projects

# 3. Preview replica convergence & cross-agent link parity
uv run scripts/sync_skills.py --converge-replicas --sync-agents claude-code,antigravity,qwen-code

# 4. Execute and receive quarantine tx-id + reload instructions
uv run scripts/sync_skills.py --prune-broken --collapse-hops --apply

# 5. Roll back any --apply cleanly (restores symlinks, raw targets, moved dirs, lockfiles)
uv run scripts/sync_skills.py --undo <tx-id>
```

Divergent copies are **never** overwritten or deleted automatically — inspect the diff summary from `revise_skills.py` and choose one canonical directory first.
