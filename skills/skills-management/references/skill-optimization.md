# Reference: Skill Optimization (SkillOpt-style)

A skill is a trainable text artefact of a frozen agent: the model weights stay
fixed and the skill document is the only thing you change. SkillOpt is the
discipline of doing that change as bounded, validated optimisation rather than
blind self-rewrite.

## When to optimise a skill

Use this loop when:

- The skill already exists but underperforms on a measurable task set.
- You have (or can write) a verifier — exact-match, scored output, or LLM
  judge.
- You can produce 20-100 representative tasks with reference answers.

Do NOT use this loop when:

- The task has no measurable success signal (open-ended creative writing
  without rubric).
- You are creating a skill from scratch — write a v0 with `/skill-creator`
  first.
- You only have 1-5 tasks; bounded text optimisation needs evidence.

## Core principles

### 1. Skill = trainable state

The mapping is direct. Parameter corresponds to the skill document, gradient
corresponds to an edit direction derived from a trajectory, learning rate
corresponds to an edit budget, and validation corresponds to a held-out gate.
Figure 1 of the paper sketches this analogy — once you accept it, every later
choice is a question you already know how to answer from regular ML practice.
The implication is that you can borrow the working vocabulary of gradient
descent (overfitting, early stopping, schedule, ablation) and apply it to a
text artefact without forcing the analogy.

### 2. Bounded edits, not blind rewrites

The edit budget `L_t` caps how many changes per step are allowed. Operations
are atomic: `append`, `insert_after`, `replace`, and `delete`. Without a
budget the optimiser will quietly erase useful rules to make room for whatever
the current minibatch is screaming about. The ablation in Table 3 makes this
concrete: the "without lr" row drops by 1-3 points. The practical
consequence is that the apply function must reject any proposal that exceeds
the budget, and the ranking prompt must be told to keep only the top `L_t`
candidates.

### 3. Held-out validation gate

Every candidate skill is scored on a selection split. Accept only if the new
score is STRICTLY greater than the current score. Ties are rejected. This is
what converts reflection from unconditional self-edit into propose-and-test
optimisation. Strict-greater matters because equality lets noise accumulate;
over an epoch the skill drifts even though no single edit "helped". The
selection split must be disjoint from the training rollouts and from the
final test split.

### 4. Rejected-edit buffer

Failed edits are not discarded. They are stored as negative feedback and fed
back into the optimiser on later calls in the same epoch, so the optimiser
stops re-proposing the same patch it has already tried. Removing the buffer
costs 1.6-4.6 points (Table 3). The buffer is per-epoch and reset at the
epoch boundary; the slow update is the mechanism for carrying lessons across
epochs.

### 5. Epoch-wise slow / meta update

Step-level edits learn from the current batch. At the epoch boundary a slow
update runs the same sampled tasks under the previous-epoch skill and the
current-epoch skill, categorises the deltas into improvements, regressions,
persistent failures, and stable successes, and writes longitudinal guidance
into a PROTECTED region delimited by `<!-- SLOW_UPDATE_START -->` and
`<!-- SLOW_UPDATE_END -->`. Step-level edits must never touch this section.
The optimiser-side meta skill is a separate artefact again — it lives in
optimiser memory only and is not shipped with the trained skill.

## Targets to aim for

| Metric | Target | Source |
|---|---|---|
| Final skill tokens | 300-2000 | Table 6 (median 920) |
| Accepted edits per training run | 1-4 | §4.4 |
| Rules style | Procedural, not instance-specific | Fig 4 |
| Validation gate strictness | Strictly greater than current | §3.5 |
| Transferability | Cross-model, cross-harness, cross-benchmark verified | §4.3 |

## The loop in one page

1. Split tasks 4:1:5 (train / selection / test) with a fixed seed.
2. Set `current_skill = best_skill = initial_skill`. Initialise rejected
   buffer and meta-skill (empty).
3. For each epoch `e` in `1..E`:

   a. For each step in epoch:
      - Sample a rollout batch from train. Run the frozen target model with
        `current_skill` on each task. Collect (trajectory, score).
      - Split rollouts into failures and successes. Partition each into
        minibatches.
      - On each minibatch, ask the optimiser to propose at most `L_t`
        atomic edits using `../prompts/analyst_error.md` or
        `../prompts/analyst_success.md`.
      - Merge proposals hierarchically (`../prompts/merge_failure.md` →
        `../prompts/merge_success.md` → `../prompts/merge_final.md`). Rank
        with `../prompts/ranking.md`, clip to `L_t`.
      - Apply edits to a CANDIDATE skill (never touching the protected
        section).
      - Evaluate candidate on the selection split. If STRICTLY greater than
        current selection score, accept (`current_skill = candidate`, update
        best if new high). Else, record edits plus failure summary in the
        rejected buffer.

   b. If `e >= 2`: longitudinal slow update — run the same sampled tasks
      under previous-epoch and current-epoch skills, group into
      improvements / regressions / persistent failures / stable successes,
      ask optimiser via `../prompts/slow_update.md` to overwrite the
      protected section. Run through the validation gate again.

   c. If `e >= 2`: optimiser meta-skill update via
      `../prompts/meta_skill.md`. Optimiser-side only.

4. Report final score on the test split. Export `best_skill.md`.

## Hyperparameter defaults (from the paper)

- Epochs: 4
- Rollout batch `B`: 40
- Reflection minibatch `B_m`: 8
- Edit budget `L_t`: 4 with cosine decay (floor = 2)
- Slow-update samples per epoch: 20
- Schedules supported: constant, linear, cosine

Per-cell defaults differ for small training pools (LiveMathBench: 35 tasks,
rollout batch 200; ALFWorld: 39 train / 140 selection / 134 test). When in
doubt, start from the defaults above and only adjust once you have a
baseline test score to compare against.

## Common failure modes

- **Blind rewrites**: optimiser keeps proposing full rewrites — set a small
  `L_t` and stick to patch mode.
- **Drift via ties**: candidate roughly equal to current gets accepted —
  enforce STRICTLY greater on the gate.
- **Repeating the same bad edit**: optimiser forgets what failed — keep the
  rejected buffer fed into the next call.
- **Slow-update overwritten by step edits**: enforce the
  `<!-- SLOW_UPDATE_START -->` / `<!-- SLOW_UPDATE_END -->` protected region
  in the apply function.
- **Memorising the training split**: score on the selection split, report
  only on test.
- **Instance-specific rules**: skill grows long with task-specific examples
  — run `../scripts/review_skill.py` and watch the `instance-specific-leakage`
  flag.

## Transferability evidence

Table 4 of the paper shows that a SpreadsheetBench skill trained on GPT-5.4
transfers to GPT-5.4-mini for a +9.4 point gain, and a Codex-trained skill
transfers to Claude Code for +59.7 points. The cost of optimising in one
environment can be amortised across related ones — a trained skill is a
reusable artefact, not a one-off configuration. In practice this means a
skill optimised on a strong model with a strict verifier is usually worth
shipping to the cheaper or weaker model that will actually run in
production.

## When to use the script

Run `python3 ../scripts/optimize_skill.py <skill> --tasks tasks.jsonl
--dry-run` first to see the plan. Then drop `--dry-run` to actually run.
Inspect `best_skill.md` and `optimization_report.md`. Diff the result
against the original with `../scripts/diff_skill_versions.py`. Use
`../scripts/log_skill_edit.py` to record any manual follow-up edits you
make after reading the report — those edits also belong in the audit trail.

## References

- Yang et al. *SkillOpt: Executive Strategy for Self-Evolving Agent Skills.*
  Microsoft, May 2026. arXiv:2605.23904.
- See companion files: `../scripts/optimize_skill.py`, `../prompts/*.md`
  (verbatim §C.2 contracts).
