# Suite audit: checking an existing project against this playbook

Read when the task is to audit the tests, gates and QA practice of an existing project, or of one
part of it, with no particular change at hand. The audit replaces the route in `SKILL.md` and ends
in a report with ranked, concrete fixes. Each fix is then done through the normal route. Pruning
the tests around one change is step 3 of the route, not an audit.

Read `suite-audit-worker.md` as well: it defines the signals and the records used below.

## Contents

- [Ground rules](#ground-rules)
- [Size the project](#size-the-project)
- [Ask before starting](#ask-before-starting)
- [Reconnaissance](#reconnaissance)
- [Partition](#partition)
- [Brief and pilot](#brief-and-pilot)
- [Dimensions and who judges them](#dimensions-and-who-judges-them)
- [Reduce and verify](#reduce-and-verify)
- [Rank and recommend](#rank-and-recommend)
- [Report](#report)
- [Failure modes and guards](#failure-modes-and-guards)

## Ground rules

The audit asks of the whole suite what `SKILL.md` asks of one check: does a green run show that
the product is right, do the expectations come from an independent source, do the checks really
run. Then it asks what the suite costs: duplicates, brittle and flaky tests, heavy setup.

```text
size → ask → reconnaissance → partition → pilot shard → fan out
  → check receipts → verify claims → rank → report
```

- **Read-only.** Nothing in the audited repository is created, edited, fixed or committed. Notes
  and worker output go to a scratch directory outside it. Running anything needs the user's yes.
  Until then, collect what is worth running and offer it at the end of the report.
- **The auditor plans, verifies and concludes. Workers scan.** A worker finding is a claim and
  enters the report only as far as the auditor verified it. Agreement between workers adds
  nothing.
- **No score.** No grade, percentage or target count. "Few tests" and "low coverage" are not
  findings. "A material risk has no check at a fitting level" is.
- **Unseen is not fine.** What was not read or not run is reported as not verified.
- **Source of expectations, not correctness.** Without the requirements, the audit shows where
  an expected value comes from and whether the test can fail. Whether the value is right is a
  question to the owner.

## Size the project

Measure before asking: list the test files from version control, count them and their lines, note
the stacks and packages. A few commands, no reading of test bodies.

| Size | Rough sign | Shape of the audit |
|---|---|---|
| Small | Up to about 40 test files or 5,000 lines of test code | No workers. The auditor reads everything and applies the signals of `suite-audit-worker.md` itself. |
| Medium | Up to about 400 test files or 60,000 lines | Workers read every test file. The auditor reads the gates and the critical areas itself. |
| Large | More, or a monorepo with several stacks | Gates and critical areas in full, the rest by sample, with the share read stated. Offer an audit package by package. |

The numbers are starting points. Workers pay off only when briefing them and verifying their
claims costs less than reading the code directly.

## Ask before starting

Ask once, in one message, with the measured size and a default for every item, so that "defaults"
is a complete answer. Use the harness's question tool when it has one.

```text
Audit of <project> at <revision>: <n> test files, about <k> lines of test code, <stacks>.
Plan: <no workers | about N worker runs, about T at the default limit>.

1. Scope: the whole repository, or only some paths? [whole repository]
2. Worker model for the scan: <models this harness can start, cheapest first>, or none.
   [the cheapest that passes a pilot shard]
   Second model, for re-runs and for critical areas too large for the auditor to read:
   <options>. [a different model from the scan's]
3. Workers in parallel: [5]
4. Execution: (a) static: nothing in the project is run; (b) also run the tests with
   <detected command>; (c) also a few sensitivity probes in an isolated copy. [a]
5. Critical areas to weigh first, if you want to name them. [derived from code and docs]
6. A cap on worker runs or on time, if any. [none]
```

- **Models:** offer only what the harness can really start: native subagents, or agents behind
  an installed orchestration tool. Names differ per harness: list them, do not assume. When the
  harness cannot choose a subagent's model, say so and ask only for the limit.
- **Time:** shards × minutes per shard ÷ workers in parallel. A shard of 2,000 lines takes a
  fast model about 7 minutes and a slow one about 15. Correct the estimate after the pilot.
- **Small project:** ask items 1, 4 and 5 only.
- **Nobody to ask** (a non-interactive run), or the answer is "defaults": proceed with the
  defaults and print them at the top of the report. Execution stays static without a yes.
- **No subagents:** work through the shards yourself in the same record format, saving the
  records after each shard. For a large project, audit gates, critical areas and a sample.
- **(a) Static:** for each claim that only a run or a probe can settle, note the exact command,
  what it would settle, its duration and its side effects. These become the suggested runs.
- **(b) Run:** the project's documented command, after establishing what it touches (databases,
  external services, paid APIs) and how long it takes. Listing tests also executes project code.
- **(c) Probe:** a handful of deliberate breaks of the rules that matter most ("Show that the
  test can fail" in `test-quality.md`), in an isolated copy, never in the user's working tree.
  Never a mutation run over the repository for a percentage.

## Reconnaissance

The auditor does this itself by listing, searching and reading configuration. The result is an
audit map in the scratch directory: shards, lens tasks, risk areas, gate facts, exclusions.

1. **Stacks, runners, levels.** Read the matching `stack-*.md`: its traps become the stack
   notes of the briefs. List test files by directory with line counts. Map directories, markers
   and tags to levels in the repository's own vocabulary, and note the levels that are absent.
2. **Exclusions.** Vendored and generated tests, snapshots, recordings and fixture data.
3. **Gates.** How checks run locally and in the pipeline: commands, triggers, conditions,
   blocking and optional jobs, retries, selectors, test selection, caches, thresholds. Include
   the checks that are not tests: types, lint, build.
4. **Risk map.** Where the product keeps access control, money, deletion, user data, migrations,
   concurrency, external services and runtime LLM calls: paths and a one-sentence promise each.
   Label the map "derived" unless the user confirmed it.
5. **Mechanical signals by search, not by model.** Fixed sleeps, skip and focus markers, retry
   settings, tests with no assertion: counts and locations. A hit is a candidate: a sleep inside
   a bounded polling loop or a fixture is not a finding. Classify the hits by reading. The
   classified hits are findings in their own right and the answer key for checking workers.
6. **Existing data, when present.** Pipeline history (ran, skipped, reruns, durations), a
   coverage report, version control history (tests that change with most commits, fixes that
   came without a test). Read it. Do not generate it without permission.

## Partition

- **Shard:** the test files of one module at one level, plus the paths of the code under test.
  Judging a test needs the code it tests, and local duplicates are visible inside a module.
- **Size:** about 2,000 lines of test code or 20 files, whichever is smaller. Shrink it for a
  weaker model. Do not raise it for a stronger one: every model reports fewer findings per line
  as the shard grows. A file over the limit is a shard of its own.
- **Complete and disjoint:** every test file in scope is in exactly one shard or excluded.
- **Critical areas** get their own shards. The auditor reads each one itself and also gives it
  to one worker: models find different things, and one reader misses a third or more. When a
  critical area is too large for the auditor to read, two different models read it and the
  auditor verifies every finding against the test and the code in full.
- **Sample for a large project:** all gates, all critical-area shards, and at least one shard
  per package and level, preferring code that changes often. Widen a stratum when its sample
  shows a pattern that matters.

Shards cannot see each other. What crosses them is a separate lens:

| Lens | Who | Question |
|---|---|---|
| Gates | Auditor | Which checks run on which trigger, which block, where success needs no run |
| Gaps by risk | Auditor; a worker per risk area collects the existing checks | Which check protects each promise, at which level, with what real |
| Top-level routes | Workers on e2e and browser shards, signals L and U | What new boundary each route adds; rule tables replayed through the interface |
| Duplicates across shards | Auditor, joining `file` records by subject | One subject checked at two levels or in two modules |
| QA and evidence practice | Auditor | Charters, done criteria, reports, instructions for contributors and agents |

Workers never start workers: one orchestrator keeps cost and acceptance in one place.

## Brief and pilot

A brief carries paths and facts. It never says what the auditor expects to find.

```text
Read <absolute path>/suite-audit-worker.md first. It is your contract and checklist.

Repository: <absolute root> at <revision>. Read-only.
Task: shard <id>   |   risk area <id>: <promise in one sentence>
Test files: <paths or globs>
Code under test, likely partial: <paths>
Level in this repository's vocabulary: <unit | integration | e2e | mixed | unknown>
Signal families: <all | a subset of O A M L D B F G H U>
Stack notes: <trap lines from the stack file; tags or markers the pipeline selects; or none>
May run: <nothing | exact commands>
Output: write the records to <scratch path>/<id>.jsonl and reply with the end record only
        | reply with the records only
```

- **Delivery.** Some harnesses confine a worker to the repository: it can neither read the
  skill's files nor write to scratch. Then paste `suite-audit-worker.md` into the brief and take
  the records from the reply. Keep the output path short, because workers mistype long ones.
- **Pilot first.** Run one shard that the auditor has read itself, chosen for variety. A model
  passes when it invents no location and misses nothing the auditor would rank in the first two
  tiers. Fix the brief or change the model, then fan out. Repeat the pilot when either changes.
- **Fan out** up to the limit, starting the next worker as each one finishes. Read the first
  results as they arrive.
- **Keep workers read-only.** Use a worker type that cannot write when the harness has one, and
  compare the working tree status before and after. Other writers may move trunk meanwhile, so
  also compare the audited files with the recorded revision.
- **One re-run per failed shard.** First look for the output under a mistyped path. After the
  re-run split the shard, use the second model, read it directly, or report it as not verified.
  No chain of cheap retries.

## Dimensions and who judges them

Workers flag the lettered signals of `suite-audit-worker.md`. Open the defining reference when
verifying a finding, not before.

| Dimension | Defined in |
|---|---|
| O, A: self-confirming and vacuous tests | `test-quality.md`, `case-design.md`, stack traps |
| M, L: doubles, reality, level | `levels-and-doubles.md`, the defect table in `SKILL.md` |
| D: duplicates and trivia | `test-quality.md`, `case-design.md` |
| B, F, H: brittle, flaky, heavy | `flaky-and-brittle.md` |
| G: checks that may be off | `test-quality.md`, `flaky-and-brittle.md` |
| U: UI and e2e hygiene | `ui-automation.md` |
| Gaps by risk | The size and defect tables in `SKILL.md`, `levels-and-doubles.md` |
| QA and evidence practice | `exploratory-qa.md`, `evidence-and-closeout.md` |
| Runtime LLM features | `llm-features.md` |

**Only the auditor judges** the last three rows, the pipeline's gates, duplicates across shards,
whether the gap a double leaves matters, whether a delete or a move keeps the protection, and
every rank.

- **Gates:** apply "Integrity of the check itself" in `test-quality.md` to the pipeline. What does
  no blocking job select? Which job can be green without running? Does skipped count as passed?
  Is a pass after a retry reported as green? Is a critical check left to a nightly run alone?
  When running is allowed, compare the number that ran with the cases in the `file` records.
  A blocking coverage or mutation-score threshold is always listed here as a risk: it rewards
  tests written for the number. It becomes a finding when signals O, A or D2 turn up under it.
- **Gaps:** for each risk area take the fitting check from "Where each defect is caught" in
  `SKILL.md`. Record which checks exist, at which level, what is real in them and which negative
  case is present. Status per promise: checked at a fitting level, checked only where the
  mechanism is removed, no check found, or not verified.
- **QA and evidence practice:** does user-facing work get a pass through the running product?
  Do reports say what was run and what was not verified? Do instructions for contributors and
  agents ask for a test count or a coverage quota?

## Reduce and verify

1. **Receipts.** Every shard has an `end` record, its `file` records cover every file of the
   shard, and every record parses. Otherwise the shard is incomplete. Parse a reply from its
   first record: some models put text before it.
2. **Locations.** Check mechanically that each `quote` occurs in its file: at the cited line,
   or else at the nearest match, since a line may repeat. Drop what does not occur. Many
   failures in one shard discard the shard. A finding may cite a helper outside the shard; the
   same check applies.
3. **Recall.** Compare worker output with the classified search hits from reconnaissance, and
   read a few files that came back clean, critical areas first. Count a match by signal family:
   one skip is G1 to one model and G2 to another. A worker that misses known signals gives no
   evidence by reporting nothing.
4. **Merge.** Group by signal and directory with a tool, not by reading every record. Join `file`
   records by subject. Where several workers read one shard, join their findings by location
   (one file, lines a few apart, or an `also` entry), never by signal code alone.
5. **Verify** by the table below.
6. **Triage** with the categories of `evidence-and-closeout.md`: a confirmed weakness is a defect
   of the test system; a claim that needs a run or a probe stays a plausible risk, with the check
   that would settle it; a judgement that needs the requirement is missing intent and goes to
   the owner; the rest is noise.

| Claim | Minimum before it enters the report |
|---|---|
| Any finding named individually | The auditor reads the cited lines and enough code around them |
| A finding in a critical area | The test and the code under test, read in full |
| Delete, merge or move | The check that keeps the protection is found and named |
| "No check exists" | An independent search of the whole test tree by symbol, route, table and message; coverage data when present |
| A gate is off or cannot block | The configuration read; with permission, a run and its summary line |
| A pattern with many instances | A sample per signal and worker model: five or a tenth, whichever is larger, reported as "reported n, checked m, confirmed k" |
| "This test cannot fail", for an important rule | With permission, a probe: break the rule once in the isolated copy and run the test |
| "Flaky" or "slow" | Run data or pipeline history. From code alone: a flaky source, a heavy setup |

When fewer than about two thirds of a sample confirm, do not report the pattern from worker
claims. Re-scan with the second model, read it directly, or list it as not verified.

Do not pick what to verify by a worker's `conf`: some models mark nearly everything high. Pick
by what the finding would cost if true.

## Rank and recommend

Rank by what a defect would cost, using damage, plausibility and recovery cost:

1. **False confidence where it is costly.** A critical promise has no working check at a fitting
   level, or a gate that should block is silently off.
2. **False confidence elsewhere.** A material behaviour whose only check cannot fail for its
   defect. Retries or quarantine that hide real failures.
3. **Lost signal and cost.** Flaky sources, brittle tests, duplicates, heavy setup, trivia. A
   gate that people bypass because it is slow or noisy moves up a tier.

- **Reachability before rank.** Establish that the behaviour is reachable in the product and
  that no check at another level already protects it.
- **Systemic before per-test.** When one signal repeats across shards, find the common cause: a
  shared fixture or helper, a base class, a runner default, a test template, a missing lint
  rule, an instruction for contributors or agents. Recommend the change at the cause, then a
  bounded sweep. A signal that search finds reliably belongs in a linter, not in a review.
- **Three to seven recommendations.** No "rewrite the suite", and no deletion of a heavy test
  for its duration alone.
- **Noise is dropped** and creates no backlog entry: naming and layout preferences, "too few
  tests" or "low coverage" alone, near-duplicates on different sides of a boundary, call
  assertions where the call is the promise, fakes that only feed data, unreachable conditions,
  any claim without a verified location.

## Report

Reply in the conversation. Write a file only where the user asks for one. Give each section one
status from `SKILL.md`: verified, partially verified, not verified or blocked. For a small project
keep the header, the summary, up to five recommendations, the not-verified list and the
suggested runs.

```text
Test and verification audit: <project> at <revision>, <date>
Scope: <paths>. Excluded: <vendored, generated, recorded>.
Mode: <static | ran: command | probes: n>. Workers: <model, runs, limit | none>.
Read: <n of m test files>. Read by the auditor: <gates, critical areas, samples>.

Summary: what a green run proves today and where it does not, in at most six lines.

Recommendations, in order
1. <Change>. Where: <paths>. Kind: systemic | targeted.
   Today: <the defect that passes unnoticed, or the cost paid>.
   Payoff: <...>. Cost: small | medium | large.
   Evidence: read | run | probe, or reported n, checked m, confirmed k.
   Done when: <the observation that shows it worked>.

Gaps by risk
| Risk area and promise | Checks found: level, what is real | Missing | Status |

Findings
| Id | Dimension | Pattern or location | Instances | Action | Evidence |

Gates: what runs on which trigger, what blocks, what is skipped or never runs.
Not audited or not verified: <area or claim>, the reason, and what would settle it.
Suggested runs: <command>: what it settles, duration, side effects. Static mode only.
Questions for the owner: judgements that need the requirement.
Order of work: gates and critical gaps first, then systemic fixes, then sweeps and cost.
```

End with two offers and do neither without a yes: carry out recommendation 1 through the route
in `SKILL.md`, and, after a static audit, the suggested runs for a deeper pass.

## Failure modes and guards

Invented locations, uneven severity and rubber-stamping are handled above: the location check,
ranking by the auditor alone, the verification table. The rest:

| Failure | Guard |
|---|---|
| A worker stops early or runs out of context | The shard size and the receipts: split and re-run |
| The auditor's context overflows | Workers write records to files and reply with the `end` record. Read aggregates and samples. Keep the audit map on disk |
| A huge monorepo | Package by package under one gates lens, a stated sample, no nested fan-out |
| Generated, vendored or recorded tests | Excluded and listed. Audit the generator or template when it lives in the repository |
| The suite cannot be run here | Static mode and existing pipeline results. Run-dependent claims stay not verified, with the command or log that would settle them |
| A worker changed the repository | Report it and let the user decide. Do not revert on your own |
| The tree moves during the audit | Findings refer to the recorded revision. Compare the audited files with it at the end and re-check the findings in files that changed |
