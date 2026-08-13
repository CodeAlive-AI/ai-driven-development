# Operationalize a Finding Workflow

Convert a recurring review finding or design rule into an executable gate, then record it in the project's agent instructions. This is how the skill's discipline survives beyond the session that applied it: a machine-enforced rule is harder to erode under delivery pressure than a prose convention, and a rule recorded in project memory reaches every future session.

## When to Use

- The same class of finding appeared in review twice or more (complexity, layering, logging, naming, duplication).
- A design decision was made that future changes must respect (dependency direction, boundary parsing, forbidden imports).
- You just finished applying this skill to a repository and want the thresholds and commands to persist.

## Prerequisites

- Write access to the repository's lint/build/CI configuration.
- `references/tooling/commands.md` for tool options per ecosystem.

---

## Workflow Steps

### Step 1: Name the Finding Class

- [ ] State the rule in one falsifiable sentence ("Domain must not import DataAccess", "no method above cyclomatic complexity 15", "no unparameterised SQL").
- [ ] Confirm it is stable — a constraint that will change next sprint is not worth automating.
- [ ] Confirm it is mechanically expressible. Intent and architecture judgment stay with review; only objective constraints become gates.

### Step 2: Pick the Cheapest Enforcing Layer

In order of preference — earlier layers give faster feedback:

| Layer | Use for |
|---|---|
| Formatter | Style — never spend review or prose rules on it |
| Type system / strict mode | Nullability, invalid states, contract drift |
| Linter rule | Complexity thresholds, forbidden patterns, naming |
| Architecture test | Dependency direction, cycles, layer rules |
| Unit/property test | Behavioral invariants |
| CI-only check | Slow or cross-cutting checks (duplication, dead code, mutation) |

### Step 3: Implement the Gate Narrowly

- [ ] Enable one rule, not a whole rule pack — packs create noise and invite blanket suppression.
- [ ] Brownfield: apply the ratchet (`references/codebase-setup/rules.md`) — fix existing violations in one slice, then flip the rule to error so it cannot regress.
- [ ] Verify the gate fails on a deliberate violation before trusting it (same principle as seeing a test fail).

### Step 4: Record in Project Agent Instructions

Add to the repository's `CLAUDE.md` / `AGENTS.md` (create the section if missing):

- [ ] The canonical verification command(s) — build, test, lint — exactly as CI runs them.
- [ ] Project-specific thresholds that override this skill's defaults (e.g. "CC review trigger here is 10").
- [ ] Accepted exceptions and their rationale, so future agents do not re-litigate or silently violate them.
- [ ] Chosen measurement commands from `references/tooling/commands.md` that fit this repository.

Keep the section short — a map to authoritative config files, not a duplicate of them.

### Step 5: Retire the Prose Version

- [ ] Stop flagging the now-automated rule in reviews — the gate owns it.
- [ ] If a document listed the rule as a manual check, replace the text with a pointer to the gate.

---

## Quick Checklist

```
[ ] Rule stated in one falsifiable sentence, stable, mechanical
[ ] Cheapest enforcing layer chosen
[ ] Gate implemented narrowly; seen failing on a violation
[ ] Brownfield violations ratcheted, then rule flipped to error
[ ] Canonical commands + thresholds + exceptions recorded in project agent instructions
[ ] Prose/manual version retired
```

## Common Mistakes

| Mistake | Why It's Bad | Do Instead |
|---------|--------------|------------|
| Enabling a full analyzer pack at once | Noise flood → blanket suppressions | One rule at a time, ratcheted |
| Automating a judgment call | False positives destroy trust in gates | Automate objective constraints only |
| Gate added but instructions not updated | Next agent re-derives or fights the gate | Always do Step 4 |
| Keeping the manual check alongside the gate | Double cost, drift | Retire the prose version |

## Exit Criteria

- [ ] The gate fails the build/CI on violation and passes on current mainline.
- [ ] Project agent instructions name the gate, its threshold, and the canonical commands.
