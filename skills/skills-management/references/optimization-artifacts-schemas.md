# Reference: Optimization Run Artifacts — JSON Schemas

The SkillOpt loop produces a fixed set of artefacts on disk. This is the formal
contract so downstream tools (`../scripts/aggregate_runs.py`, dashboards,
audits) can read them without coupling to the optimiser source. Schema stability
is a v3.x guarantee — breaking changes bump the major version.

## Output directory layout

`../scripts/optimize_skill.py` writes everything under `--output-dir`. The
tree below shows what exists after a complete run with `--epochs E` and
`steps_per_epoch = ceil(len(train) / rollout_batch)`:

```
<output-dir>/
├── splits.json
├── state.json
├── current_skill.md
├── best_skill.md
├── initial_skill.md            (snapshot of SKILL.md at run start)
├── meta_skill.json             (only if epoch >= 2 completed)
├── rejected_buffer.json        (per-epoch; cleared at epoch boundary)
├── edit_apply_report.json      (append-only accepted-edit log)
├── optimization_report.md      (written at end of run)
├── test_rollouts.jsonl         (written at end of run)
└── epoch-{e}/
    └── step-{s}/
        ├── rollouts.jsonl
        ├── proposals.json
        ├── candidate.md        (only if edits were proposed)
        └── decision.json       (only if edits were proposed)
```

The manual audit trail lives next to the deployed skill itself, not in the
optimisation output dir:

```
<skill-root>/
├── .skill_edit_log.jsonl
└── .skill_snapshots/
    └── SKILL.<sha8>.md         (one per --snapshot invocation)
```

---

## splits.json

Deterministic train/selection/test partition derived from `--seed` and task
ids. Written once per run; re-read on `--resume`.

Location: `<output-dir>/splits.json`

```json
{
  "seed": 42,
  "train": ["task-001", "task-007", "task-012"],
  "selection": ["task-003", "task-015"],
  "test": ["task-002", "task-005", "task-009", "task-011"]
}
```

- `seed` — int. The seed passed to `--seed` (default 42).
- `train` — list of task id strings (originally from `tasks.jsonl`).
- `selection` — list of task id strings; used by the validation gate.
- `test` — list of task id strings; held out until the final evaluation.

---

## state.json

Resumable optimiser state. Overwritten after every step and at every epoch
boundary.

Location: `<output-dir>/state.json`

```json
{
  "epoch": 3,
  "step": 0,
  "current_score": 0.62,
  "best_score": 0.71
}
```

- `epoch` — 1-indexed epoch number. `state.epoch > args.epochs` means the
  run is complete.
- `step` — last completed step within the current epoch. Reset to 0 at each
  epoch boundary.
- `current_score` — mean verifier score (0.0-1.0) of `current_skill.md` on
  the selection split. `null` before the baseline pass.
- `best_score` — highest selection score observed so far across all
  accepted candidates.

---

## rollouts.jsonl

One JSON object per line. One file per step holding the (task, output,
score) triples produced by `evaluate_skill`.

Location: `<output-dir>/epoch-{e}/step-{s}/rollouts.jsonl`

```json
{"task_id": "task-001", "prompt": "Summarise...", "reference": "Expected text", "output": "Model output", "score": 1}
{"task_id": "task-007", "prompt": "Translate...", "reference": "Expected text", "output": "Model output", "score": 0}
```

- `task_id` — string. Matches an id from `tasks.jsonl`.
- `prompt` — string. The verbatim task prompt passed to the target model.
- `reference` — string. The reference answer (empty string if the task has none).
- `output` — string. The target model's stdout. Empty string if the rollout
  raised an exception (logged but not failed).
- `score` — int. 0 or 1; the verifier verdict.

---

## proposals.json

Optimiser output for one step: the merged + ranked edit set plus the
intermediate merge outputs for debugging.

Location: `<output-dir>/epoch-{e}/step-{s}/proposals.json`

```json
{
  "edits": [
    {"op": "append", "target": null, "content": "## Edge cases\n- ...", "reasoning": "Failures share missing edge-case handling"}
  ],
  "merged_failure": {"edits": [...], "reasoning": "..."},
  "merged_success": {"edits": [...], "reasoning": "..."},
  "merged_final": {"edits": [...], "reasoning": "..."}
}
```

- `edits` — list of edit objects. Each has:
  - `op` — one of `"append"`, `"insert_after"`, `"replace"`, `"delete"`.
  - `target` — string or null. Required for all ops except `append`.
  - `content` — string. Empty for `delete`.
  - `reasoning` — string. Optimiser's justification; free-form.
- `merged_failure` / `merged_success` / `merged_final` — intermediate
  `{edits, reasoning}` envelopes produced by `merge_failure.md`,
  `merge_success.md`, `merge_final.md` respectively. Useful when auditing
  why a particular edit survived ranking.

---

## decision.json

Validation-gate outcome for one step. Written only when at least one edit
was proposed.

Location: `<output-dir>/epoch-{e}/step-{s}/decision.json`

```json
{
  "candidate_score": 0.65,
  "current_score": 0.62,
  "delta": 0.03,
  "accepted": true,
  "L_t": 4,
  "apply_report": [
    {"index": 0, "op": "append", "target_preview": "", "applied": true, "error": null},
    {"index": 1, "op": "replace", "target_preview": "## Step 3...", "applied": false, "error": "replace target not found: '## Step 3...'"}
  ],
  "edits": [...]
}
```

- `candidate_score` — float 0.0-1.0. Mean verifier score of the candidate
  on the selection split.
- `current_score` — float 0.0-1.0. Score the candidate must strictly beat.
- `delta` — `candidate_score - current_score`.
- `accepted` — bool. True iff `candidate_score > current_score` (strict).
- `L_t` — int. Edit budget enforced for this step.
- `apply_report` — list of per-edit application records. `applied=false`
  means the edit was skipped (target missing, touches protected region, or
  unknown op). The candidate is built from the surviving edits.
- `edits` — copy of the proposed edits the optimiser passed in.

---

## candidate.md / current_skill.md / best_skill.md / initial_skill.md

Plain markdown files holding skill text at four lifecycle points.

- `candidate.md` (per step) — what was produced by applying `edits` to
  `current_skill.md`. Written before the validation gate; not promoted on
  reject.
- `current_skill.md` (run-wide) — the rolling state. Updated on every
  accept and on every slow-update.
- `best_skill.md` (run-wide) — the highest-selection-score skill seen.
  Promoted via `shutil.copyfile` from `current_skill.md` whenever
  `best_score` advances.
- `initial_skill.md` (run-wide) — the SKILL.md as it existed at run start.
  Written once and never modified. Use this for the baseline delta.

---

## edit_apply_report.json

Append-only log of every accepted candidate across all epochs/steps in this
run. Read on `--resume` to rebuild history.

Location: `<output-dir>/edit_apply_report.json`

```json
[
  {
    "epoch": 1,
    "step": 2,
    "score_before": 0.58,
    "score_after": 0.62,
    "edits": [
      {"op": "append", "target": null, "content": "...", "reasoning": "..."}
    ]
  }
]
```

- One entry per accepted step. The `edits` field is the post-rank-and-clip
  list — what actually applied. Reject events live in `rejected_buffer.json`
  instead.

---

## rejected_buffer.json

Per-epoch buffer of rejected proposals. Fed back into the optimiser within
the same epoch as negative feedback. Cleared (overwritten with `[]`) at
every epoch boundary.

Location: `<output-dir>/rejected_buffer.json`

```json
[
  {
    "epoch": 2,
    "step": 1,
    "score_delta": -0.04,
    "reason": "validation gate: candidate score not strictly greater",
    "edits": [{"op": "replace", "target": "...", "content": "..."}]
  }
]
```

- `score_delta` — negative or zero. Equal to `candidate_score - current_score`
  at reject time.
- `reason` — currently only the strict-gate reason. Other rejection causes
  (e.g. apply failure on every edit) bypass this file because no candidate
  was ever scored.

---

## meta_skill.json

Optimiser-side memory. Written at every epoch boundary from epoch 2 onward
when `meta_skill_step` returns non-empty content. Never shipped with the
trained skill.

Location: `<output-dir>/meta_skill.json`

```json
{
  "content": "When failures share a regex theme, prefer one consolidated rule over per-case edits.",
  "epoch": 3
}
```

- `content` — free-form guidance text. Injected as `OPTIMIZER MEMORY` at
  the head of every analyst/merge/rank prompt in the next epoch.
- `epoch` — the epoch in which this guidance was produced.

---

## optimization_report.md (frontmatter and table schema)

Human-readable end-of-run summary. Generated by `write_optimization_report`.
This file is markdown, not JSON; the schema below describes the sections
downstream tools should expect.

Location: `<output-dir>/optimization_report.md`

Required sections (in order):

1. `# SkillOpt Optimization Report: <skill_name>`
2. `## Summary` — bullet list with these exact keys:
   - `Baseline selection score: <float|"n/a">`
   - `Best selection score: <float|"n/a">`
   - `Final test score: <float>` (3 decimal places)
   - `Steps recorded: <int>`
   - `Accepted edits: <int>`
   - `Rejected proposals (last epoch buffer): <int>`
   - `Approx tokens (rough): <int>`
3. `## L_t Schedule` — markdown table with columns `Epoch | L_t`.
4. `## Per-step History` — markdown table with columns
   `Epoch | Step | L_t | Pass | Fail | Candidate | Current | Best | Accepted`.
5. `## Accepted Edits (Table 6 / Fig 4 style)` — up to ten subsections, one
   per accepted step, listing up to three edits each.

Parsers should treat the Summary bullet list as the authoritative
key-value source; the tables are for humans.

---

## test_rollouts.jsonl

Same shape as the per-step `rollouts.jsonl` but written once at the end of
the run from `best_skill.md` against the held-out test split.

Location: `<output-dir>/test_rollouts.jsonl`

```json
{"task_id": "task-002", "prompt": "...", "reference": "...", "output": "...", "score": 1}
```

Fields are identical to the per-step `rollouts.jsonl` schema above.

---

## Manual audit artefacts (written by log_skill_edit.py)

These live next to the deployed skill and persist across optimisation runs.
They are the trail for hand-edits, not for `optimize_skill.py` runs.

### .skill_edit_log.jsonl

Append-only audit log of manual edits. One JSON object per line, in
chronological order.

Location: `<skill-root>/.skill_edit_log.jsonl`

```json
{"timestamp": "2026-05-26T10:30:00+00:00", "sha_before": "abc123...", "sha_after": "def456...", "body_lines": 142, "body_tokens": 1820, "delta_tokens": 47, "reason": "Add edge case from bug #123", "source": "from-bug", "ref": "#123", "user": "alice"}
```

- `timestamp` — ISO 8601 UTC timestamp.
- `sha_before` — SHA-256 of the previous `SKILL.md` content. `null` for the
  first entry.
- `sha_after` — SHA-256 of the current `SKILL.md` content.
- `body_lines` — int. Line count of the body (after frontmatter strip).
- `body_tokens` — int. Approximate tokens (`len(body) // 4`).
- `delta_tokens` — int or null. `body_tokens - prev_body_tokens`; null for
  the first entry.
- `reason` — string. Required free-form note.
- `source` — one of `"manual"`, `"from-bug"`, `"from-trajectory"`,
  `"from-review"`, `"external"`. Add new values by extending the CLI choices.
- `ref` — string or null. External reference (PR url, bug id, run id, etc.).
- `user` — string or null. Value of `$USER` at log time.

### .skill_snapshots/SKILL.<sha8>.md

Verbatim copy of `SKILL.md` taken when `log_skill_edit.py --snapshot` is
passed. Filename uses the first 8 hex chars of `sha_after`.

Location: `<skill-root>/.skill_snapshots/SKILL.<sha8>.md`

- One file per unique snapshot. The script never overwrites an existing
  snapshot — collisions on the 8-char prefix are silently ignored.
- Pair with `../scripts/diff_skill_versions.py` to bisect regressions.

---

Schema stability is a v3.x guarantee. Breaking changes (renamed fields,
removed keys, changed semantics) bump the major version of
`skills-management`. Additive fields may appear within a major version;
consumers should ignore unknown keys rather than fail.
