# Reference: Optimization Run Grading Checklist

Once `../scripts/optimize_skill.py` finishes, the operator audits the run
before promoting `best_skill.md` to the deployed skill. This checklist is the
ship/no-ship gate. It enforces SkillOpt discipline at the boundary between an
optimisation artefact and a production skill.

Pair this checklist with `./optimization-artifacts-schemas.md` (what the
files contain) and `./skill-optimization.md` (why each gate exists).

## Pre-flight (before opening the artefacts)

1. Confirm `splits.json` was produced from a fixed `--seed`. Compare the
   seed against the run command line; mismatched seeds invalidate
   cross-run comparison.
2. Confirm the verifier is discriminating. If `llm-judge` always returns
   1, accept-rate is meaningless. Sample five `rollouts.jsonl` rows and
   re-grade them by hand.
3. Confirm split freshness. The test split must contain no task ids that
   appear in any previous run's training split for the same skill. Cross
   `splits.json` against the historical archive in
   `<skill>/.skill_edit_log.jsonl` `ref` fields.
4. Confirm the target model is the production model, or that you have a
   transferability plan. Optimising on Opus and shipping to Haiku is fine
   but requires explicit re-evaluation of `best_skill.md` against the
   actual deployment target.
5. Confirm the run command line is recorded somewhere reproducible — at
   minimum, store it in the `ref` field when you eventually
   `log_skill_edit.py`. A missing command line means the run is a
   one-shot.
6. Confirm `meta_skill.json` content has not been copied verbatim into
   `current_skill.md`. The optimiser-side memory is not a shippable
   artefact.
7. Confirm no aborted step left an orphan `candidate.md` newer than
   `current_skill.md`. If so, the run state is inconsistent — re-run with
   `--resume` until clean.

## Reviewing best_skill.md

- Token count must fall in 300-2000. Outside this band, the skill is
  either underspecified or bloated (paper Table 6: median 920).
- Diff against `initial_skill.md`. Net token growth above +40% is a yellow
  flag; growth above +80% is a red flag unless the run started from a
  near-empty skill.
- Scan for instance-specific markers: exact task ids, verbatim training
  prompts, named entities that only appear in the training split. These
  indicate memorisation, not generalisation.
- Confirm the protected slow-update block is intact: a single
  `<!-- SLOW_UPDATE_START -->` and `<!-- SLOW_UPDATE_END -->` pair, with
  prose between them, not JSON dumps or rollout transcripts.
- Procedural rules outnumber reactive rules. "Do X when Y" beats "If X
  fails, also try Y, Z, and W" by a wide margin in Fig 4-style audits.
- Header anchor density should be one section header per ~150-300 tokens.
  Wall-of-text skills make `insert_after` edits brittle in the next run.
- No prose that addresses the optimiser ("the previous skill version
  said..."). All text addresses the target agent at inference time.
- No leftover debugging scaffolding (TODO, XXX, "test this", commented-out
  blocks).

## Reviewing edit_apply_report.json

- Total accepted edits per training run should land in 1-4 per epoch
  (paper §4.4). Substantially higher means the gate was loose or the
  baseline was very weak.
- Each accepted edit's `reasoning` field must explain a pattern across
  multiple failures or successes, not patch a single example. Single-task
  reasoning is overfitting.
- `apply_report` arrays inside each entry should show all edits applied
  successfully. A run where every accepted candidate had silent skips
  means the optimiser is proposing edits whose targets do not exist —
  rank-and-clip is masking the failure.
- Distribution of `op` values: `append` and `insert_after` should
  dominate. Frequent `replace` and `delete` suggest the optimiser is
  fighting prior content rather than extending it.
- Support count — the number of distinct task ids each edit's reasoning
  cites — should average two or more. Edits driven by a single trajectory
  are memorisation.
- Source-type balance: at least one accepted edit should originate from
  the success-analyst path (`prompts/analyst_success.md`). Failure-only
  runs miss reinforcement opportunities.
- No two accepted edits should be semantic duplicates. If the optimiser
  keeps re-discovering the same lesson, the previous slow-update missed
  it.

## Reviewing rejected_buffer.json

- Remember this file holds only the LAST epoch's rejections — earlier
  epochs were cleared at the boundary. To see full reject history, walk
  `epoch-{e}/step-{s}/decision.json` files with `accepted: false`.
- A persistent rejected edit appearing across multiple steps within the
  same epoch means the optimiser is stuck. Manually inject the edit's
  inverse into `meta_skill.json` before the next run, or rewrite the
  relevant analyst prompt.
- Distribution across steps should be roughly uniform. All rejections
  concentrated in the final steps of an epoch suggests the LR floor is too
  high — the optimiser is still proposing budget-sized patches when it
  should be tightening.
- Magnitude of `score_delta` matters more than count. Rejected edits with
  `score_delta` close to zero are noise; clustered around -0.05 to -0.15
  are real regressions the optimiser keeps proposing.
- A rejected buffer larger than the accepted log over the same epoch is a
  plateau signal. Either widen the train split, lower the LR floor, or
  conclude the skill has converged for this task set.
- An empty rejected buffer with non-zero accepted edits is suspect: it
  means every proposed candidate cleared the gate, which is implausible
  unless the gate or verifier is broken.

## Reviewing optimization_report.md and test_rollouts.jsonl

- Final test score must exceed baseline selection score by a margin
  larger than the verifier noise floor. Re-run the baseline twice; the
  delta between those runs is your noise floor.
- The per-step history table must show a non-trivial accept/reject mix.
  All-accept = gate too loose. All-reject = optimiser misaligned with
  task; either the prompts are wrong or `L_t` is too aggressive.
- Selection-vs-test gap. Score `(best_score_selection - test_score)`. A
  gap above 0.10 signals overfitting to the selection split — rotate the
  splits and re-validate before shipping.
- Per-step `Candidate` column should not oscillate wildly. Smooth-ish
  decay with periodic jumps after slow-update is healthy. Jagged sawtooth
  means high variance, likely from a flaky verifier or a too-small
  rollout batch.
- Variance across `test_rollouts.jsonl` rows. If most items are 1 and a
  handful are 0, study the failing items — they are the next training
  set. If scores look uniformly random, the verifier is broken.
- Cost per absolute point. Compute `approx_tokens / (test_score - baseline)`
  if the denominator is positive. Compare against past runs in the same
  skill's archive — rising cost per point means diminishing returns.
- Step count should approximate `epochs * ceil(train / rollout_batch)`.
  Significantly fewer means the run aborted; cross-check `state.epoch`
  against `--epochs`.
- Approx tokens reported is rough. For real cost accounting, capture the
  CLI billing output separately — this field is for trend comparison
  across runs, not for finance.

## Reviewing meta_skill.json

- Content should be actionable optimiser guidance — heuristics like "when
  three failures share a regex, propose a single consolidated rule" — not
  task-level rules.
- It should acknowledge at least one failure mode observed in the run.
  Pure cheerleading text means `meta_skill.md` was not engaging with the
  longitudinal comparison.
- It must not leak into the trained skill. Grep `best_skill.md` for any
  sentence longer than 12 words that also appears in `meta_skill.json`.
  Overlap is a contamination bug.
- The `epoch` field should equal the run's final epoch. An earlier value
  means the meta-skill step failed in the final epoch and the previous
  guidance was retained.
- File absent is acceptable for runs with `--epochs 1` (the step never
  runs). For multi-epoch runs, absence means every `meta_skill_step` call
  returned empty — investigate the `meta_skill.md` prompt before the next
  run.

## Red flags (any one of these blocks shipping)

- `test_score < baseline_score`. The optimiser made the skill worse on
  the held-out split. Ship `initial_skill.md` and rerun with a different
  seed.
- Protected slow-update markers missing or duplicated in `best_skill.md`.
  Apply-function discipline broke; fix the script before re-running.
- More than 50% of accepted edits cite a single training task id in their
  reasoning. The run memorised the train split.
- `best_skill.md` contains `OPTIMIZER MEMORY` headers, JSON blobs, or
  anything that looks copied from a prompt template. Contamination.
- Verifier-derived scores in `test_rollouts.jsonl` do not match a hand
  re-grade of three random failing items. Verifier is broken; the entire
  run is uninterpretable.
- Selection score and test score differ by more than 0.20 with the
  selection score higher. Overfit to selection — either the selection
  split is too small or the gate ran too many times.
- Step count below `epochs * 0.5 * ceil(train / rollout_batch)`. The run
  aborted mid-flight; either resume or discard.
- `tokens_best > 2 * tokens_initial` with `test_delta < 0.05`. The skill
  ballooned for a marginal gain — token-cost-per-point is unacceptable.

## Green-light decision

For a run that clears every checklist gate, ship via:

```
cp <output-dir>/best_skill.md ~/.claude/skills/<skill>/SKILL.md
python3 ../scripts/log_skill_edit.py <skill> \
  --reason "Promoted from SkillOpt run; test_delta=+X.XXX" \
  --source from-trajectory \
  --ref <output-dir> \
  --snapshot
```

The `--snapshot` is mandatory on optimisation-driven promotions so that
`../scripts/diff_skill_versions.py` can bisect regressions later. The
`--ref` should point at the run's output directory so the trail back to
the rollouts is one command away.

For a marginal run — clears most gates but `test_delta_vs_baseline` is
between 0 and the verifier noise floor — do not ship. Instead, keep
`best_skill.md` archived under `<skill>/.skill_archive/` for diff fodder
in the next run and re-optimise with a different seed or a larger
training pool. Mark this branch decision in `.skill_edit_log.jsonl` even
when no edit is made, by appending an entry with
`--source manual --reason "Skipped marginal run <id>"` so future audits
see the skipped branch.

For a failed run — at least one red flag — do not ship and do not archive
`best_skill.md`. Delete the run's output directory once the cause is
identified (broken verifier, wrong target model, contaminated splits).
Keep `splits.json` if the same task set will be reused. File the root
cause in the skill's troubleshooting reference before another optimisation
run starts; an unrecorded failure mode is one the next run will repeat.
