## E.22 - Improvement-Oriented Quality Evaluation Question Framing

Status: Core.

### E.22:1 - Problem frame

Use `E.22` when someone is about to ask for a quality evaluation, quality review, returned-finding absorption, improvement proposal, or follow-up hypothesis over an object version named by value, and the question needs to say what kind of evaluation is wanted before the evaluator starts.

`E.22` frames the question. It does not evaluate the object. The values, coordinates, statuses, and stop meanings come from the named object-under-improvement evaluation: for example `E.21` for one pattern version, `E.9.DA` for one `DRR`, `E.2.DA` for an FPF-level object, `C.25` for an engineering quality bundle, or another declared characteristic space, scale set, rubric, or review profile. `E.19` is different: it supplies an admission or refresh review gate and findings profile. Use `E.19` as the object-under-improvement evaluation only when the object being evaluated is an `E.19` review-profile result itself. For one FPF pattern version, `E.21` supplies the coordinate values and `PatternQualityStatus`; `E.19` may later check that the `E.21` result is valid, sufficient for the release seam, and not overread as project evidence, release, gate, assurance, or work.

Not this pattern when the question is already scoped and one direct evaluation is enough. Run the object-under-improvement evaluation directly. Use `E.23` when repeated improvement across passes is needed.

First useful move: write a `QualityEvaluationQuestionFrame` naming the object version, the object-under-improvement evaluation, the purpose, the floor or improvement aim, protected trade-offs, expected evidence basis, and expected result form.

What goes wrong if missed: "review this" can mean too many different things. A floor check may be mistaken for exceptional improvement, a review may suggest work without naming quality movement, absorption may count closed rows without re-evaluating the changed object, or a follow-up suggestion may be overread as a decision, work plan, gate, evidence, assurance, or release.

Primary EntityOfConcern in plain terms: the framed quality-evaluation question for one object version.

### E.22:2 - Problem

Quality evaluations fail when the evaluator has to infer the question. The same object can be checked for floor adequacy, improved toward exceptional expression, compared across trade-offs, mined for open questions, or evaluated after finding absorption. Those purposes produce different findings.

The defect is not that reviewers need more ceremony. The defect is that an unframed question hides the object under improvement, the evaluation that supplies values, and the allowed shape of returned work.

### E.22:3 - Forces

| Force | Tension |
|---|---|
| Cheap readiness vs ambitious improvement | A floor evaluation should be short; exceptional improvement needs richer proposals. |
| Explicit purpose vs reviewer discovery | The request names the purpose, while the reviewer can still report important unasked questions. |
| Evaluation vs follow-up action | A useful evaluation may suggest a follow-up, but the suggestion remains a hypothesis until the pattern that governs the claim, relation, or boundary is applied. |
| Multi-coordinate gain vs Goodhart risk | Raising one visible value can damage usability, affordability, locality, source preservation, or corpus ecology; use `E.13` when the visible value or metric is being treated as the intended value itself. |
| Proposal portfolio vs selected result | Several candidate improvements may be useful without becoming a selected set, pool policy, front insertion, parity, or refresh result. |

### E.22:4 - Solution

`E.22` gives one compact declaration for improvement-oriented quality evaluation questions. It keeps the question from replacing the evaluation and keeps the evaluation result from becoming a decision or work product beyond its authority.

#### E.22:4.1 - Local names and kind settlement

| Local name | Kind and role |
|---|---|
| `QualityEvaluationQuestionFrame` | Compact declaration of the requested quality evaluation before it runs. |
| `ObjectVersionUnderQualityEvaluation` | Exact object version being evaluated. |
| `ObjectUnderImprovementEvaluationRef` | Exact evaluation pattern, characteristic space, scale set, rubric, review profile, or quality bundle that supplies values. |
| `QualityEvaluationPurposeSelection` | Requested evaluation purpose or combined purposes. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor when the frame declares a floor claim. |
| `DesiredImprovementAim` | Requested movement beyond the floor when improvement beyond the floor is requested. |
| `TradeoffProtectionSet` | Qualities that must not silently worsen while visible values improve. |
| `ExpectedEvaluationEvidenceBasis` | Evidence loci the named evaluation must check or name for the requested purpose: object version, corpus/projection loci, source-currentness loci, comparator loci, worked cases, returned findings, or missing loci named by value. |
| `ExpectedQualityEvaluationResultForm` | The result-row shape required by the named evaluation, including coordinate/value/short-rationale rows, mandatory attention-discharge profiles such as `E.21` `PrecisionRestorationProfile`, and any evidence-locus or coordinate-specific payload fields. For `E.21`, this profile collapses word/head/use, phrase-apparatus, repetition/distribution, role-carrier, and pattern-application layers into affected-coordinate effects. |
| `QualityReviewFindingRow` | Actionable row for a returned finding, expected movement, correction direction, and closure test. |
| `KindRestorationCheck` | Required field for any finding or proposal whose correction direction changes wording, naming, or precision-restoration content: pre-repair kind/relation/slot-or-use-position/admissible use/scope, proposed post-repair kind/relation/slot-or-use-position/admissible use/scope, or `not triggered`/`ordinary prose`/`already satisfied`/`blocker` disposition with loci. |
| `CandidateImprovementProposalPortfolio` | Bounded set of proposal rows returned by the evaluation when alternatives are useful. |
| `ImprovementFollowUpHypothesis` | Stop, repair, proposal, trade-off warning, outside-evaluation statement, new-frame statement, or governing pattern for a specific claim, relation, or boundary suggested by the evaluation. This is the proposed improvement follow-up, not a substitute for the evaluation result. |

These names frame and report quality evaluation. They do not select candidates, publish sets, plan work, certify evidence, approve release, or create new values.

#### E.22:4.2 - Quality evaluation purposes

| Purpose value | Use when | Expected result |
|---|---|---|
| `floorEvaluation` | The question is whether the object reaches a declared floor. | Values below floor, first repair, architecture hold, refresh, new-frame assignment, or admissible stop. |
| `exceptionalImprovementEvaluation` | The floor is reached and the requester wants non-dominated improvement toward exceptional expression. | Per-coordinate proposal or no-candidate disposition. |
| `paretoTradeoffEvaluation` | A candidate change may improve some values while worsening protected qualities. | Trade-off account and non-dominated comparison. |
| `candidateImprovementProposalEvaluation` | The requester needs candidate-change proposals before changing the object or generating variants. | Proposal row or bounded proposal portfolio with expected evaluation movement. |
| `openQuestionDiscoveryEvaluation` | The requester wants important unasked questions surfaced. | Question classified as existing-coordinate issue, candidate future coordinate, or outside-evaluation issue. |
| `absorptionEvaluation` | Returned findings or suggestions have been applied or rejected. | Quality-impact account over the changed object. |

Purposes can be combined, but the result keeps them distinguishable. A floor result does not answer exceptional improvement. Absorption count is not quality movement. A proposal is not a selected work item.

#### E.22:4.3 - Question frame
An improvement aim is not a command to make every coordinate exceptional. A `5` is assigned only by the named evaluation after the changed object earns it. The frame may ask for substantive non-dominated proposals that could move named coordinates toward exceptional expression, but it must also allow `no proposal` or `stay at current value` when every plausible change would add apparatus, proof prose, boundary catalogues, or process evidence while damaging protected qualities. That no-proposal result needs checked loci; it is not a cheap refusal to improve.

```text
QualityEvaluationQuestionFrame:
  Object version under quality evaluation: <object version named by value>
  Object-under-improvement evaluation: <exact evaluation>
  Evaluation purpose selection: <floor | exceptional | tradeoff | proposal | open-question | absorption | combined>
  Declared quality floor: <floor and scope, or evaluation default>
  Desired improvement aim: <floor-only | raise toward exceptional | compare variants | propose candidate changes | discover questions | absorption impact>
  Protected trade-offs: <usability | affordability | locality | corpus ecology | neighbour fit | source preservation | other property named by value>
  Expected evidence basis: <object, corpus, source, comparator, worked-case, returned-finding, projection, or missing loci named by value required by the named evaluation and purpose>
  Expected result form: <named evaluation's result-row shape | finding rows | proposal rows | trade-off table | open-question list | absorption-impact account | follow-up hypotheses>
  Non-use boundary: <what this result must not decide, certify, publish, plan, execute, or prove>
```

The shortest floor frame may name only object version, object-under-improvement evaluation, purpose `floorEvaluation`, and declared floor. The named evaluation still runs its required coordinate set and returns the result-row shape, evidence basis, rationales, coordinate-specific payloads, and mandatory attention-discharge profiles required by that evaluation. For one FPF pattern version under `E.21`, compactness never permits omitted coordinates, missing `ShortRationale`, absent `PrecisionRestorationProfile`, inactive/triggered-coordinate shortcuts, scope narrowing, or a blocker-only substitute result.

The frame does not authorize post-hoc scope replacement. If the requested floor is landing-input, corpus-facing, `Stable`, release, external-review, or another stated use, the evaluator measures that use. If a different use becomes interesting, open a new `QualityEvaluationQuestionFrame`; do not report the current request as passed under an easier scope.

#### E.22:4.4 - Finding and proposal rows

An actionable finding has this shape:

```text
QualityReviewFindingRow:
  Review locus: <where the issue was found>
  Object locus: <where the object would change>
  Evaluation effect: <coordinate/status/floor/protected quality/outside evaluation>
  Current value or status: <if known>
  Expected movement: <repair floor | raise toward exceptional | prevent loss | classify outside>
  Correction direction: <what should change>
  Kind restoration check: <required when wording, naming, or precision restoration changes text; otherwise `not triggered`, `ordinary prose`, or `already satisfied` with loci>
  Closure test: <what evidence would close the row>
```

A proposal row uses the same shape plus expected trade-offs and the governing pattern for any outside claim, relation, or boundary when needed. One edit may close several rows, but each row keeps its own disposition and closure evidence.

For wording, naming, and precision-restoration proposals, the correction direction is not "replace X with Y". It must state the recovered object kind, relation, slot or use-position when live, admissible use, and scope before and after the change, or state `not triggered`, `ordinary prose`, `already satisfied`, or `blocker` with loci. A proposal that only removes the suspicious word, that leaves the text unchanged without by-value discharge, or that narrows one kind into another without an accepted decision, is a finding, not a closed repair.

#### E.22:4.5 - Absorption impact values

| Absorption impact | Meaning |
|---|---|
| `coordinateImproved` | A named coordinate or status has stronger content evidence after the change. |
| `floorOnlyClosure` | A below-floor defect was repaired enough for the floor but not exceptional expression. |
| `unchangedBecauseAlreadySatisfied` | The suggestion was already satisfied by value, with loci named by value and the evaluation property it already satisfies. |
| `tradeoffIntroduced` | A repair raised one property and damaged another. |
| `qualityLossDetected` | The applied or proposed change lowers a value or protected quality. |
| `outsideObjectUnderImprovementEvaluation` | The suggestion belongs under another exact evaluation or pattern. |
| `notAdmissibleForDeclaredUse` | The suggestion is rejected for the declared purpose and boundary. |

The absorption result is quality movement under the object-under-improvement evaluation, not a count of accepted rows.

#### E.22:4.6 - OEE/NQD and proposal portfolios

When the object is a candidate, archive/front member, selected set, parity report, refresh report, or declared transformation result, `E.22` can frame the quality question and return proposal rows. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep authority over candidate characteristics, archive/front semantics, pool policy, selected-set publication, parity, and refresh.

### E.22:5 - Worked slices

**Floor evaluation.** A reviewer is asked whether one pattern is ready for ordinary use. The frame names `E.21`, purpose `floorEvaluation`, the declared floor, and the expected `E.21` result form. The result is a complete `E.21` coordinate table with `ShortRationale` and `EvaluationEvidenceBasis`, not a narrative "looks fine."

**Exceptional improvement.** A pattern already passes the floor. The frame asks for substantive non-dominated improvements for named coordinates while protecting usability and related-pattern fit. The result returns proposal rows for content improvements such as missing worked cases, source-currentness carry-through, mature-comparator discharge, deletion of displaced apparatus, or relation cleanup, plus checked no-candidate dispositions for coordinates where no non-dominated content move remains. It does not ask the evaluator to make every coordinate `5`.

**Absorption.** External review returns many suggestions. The frame asks for `absorptionEvaluation`. The result says which changes improved coordinates, which were already satisfied, which introduced trade-offs, and which belong outside the evaluation.

**Proposal portfolio.** A candidate improvement campaign needs alternatives before editing. The frame asks for `candidateImprovementProposalEvaluation`. The result returns bounded proposal rows; selection or generation stays with the pattern that governs that claim and is not decided by the evaluation frame.

### E.22:6 - Bias annotation

This pattern biases FPF toward asking the quality question by value. The bias is useful because unframed review requests often produce plausible but wrong answers.

The bias is bounded. `E.22` does not supply quality values, run repeated improvement, publish selected sets, decide work, or certify project claims.

### E.22:7 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-E22-1` | Name the object version and object-under-improvement named by value evaluation. |
| `CC-E22-2` | State purpose, declared floor or improvement aim, protected trade-offs, and expected result form. |
| `CC-E22-3` | Keep the object-under-improvement evaluation as the source of values and required coordinates. |
| `CC-E22-4` | Represent actionable returned work as row-level findings or proposal rows with expected quality movement, closure tests, and `KindRestorationCheck` when the row proposes wording, naming, or precision-restoration repair. When a relation/signature/lens slot or use-position is live, the row cites the governing pattern named by the evaluation or restoration result; `E.22` frames the improvement question and does not restate that ontology. |
| `CC-E22-5` | For absorption, report quality impact on the changed object, not only applied/not-applied disposition. |
| `CC-E22-6` | State a compact declarative non-use boundary when the result might be overread as decision, work, evidence, assurance, gate, release, certification, publication, parity, refresh, or selected-set authority. Keep the result on the evaluation question and name only the specific outside claim plus the pattern that governs it when one is needed; precision-restoration or phrase-apparatus issues belong to the named evaluation profile and `F.19`, not to a local boundary catalogue. |
| `CC-E22-7` | State what became worse when a proposed or applied improvement raises visible values. |
| `CC-E22-8` | Send repeated improvement to `E.23` after one framed evaluation returns findings or proposals. |
| `CC-E22-8a` | Do not frame `5`, all-`5`, or `5-defensible` as the work target. Frame below-floor repair separately from optional exceptional-improvement proposals. The optional proposal target is substantive content movement, not score proof; allow checked `no proposal` or `stay at current value` only when further change would be dominated by apparatus growth, proof theatre, or protected-quality loss. |
| `CC-E22-9` | Name the expected evidence basis and result-row shape from the object-under-improvement evaluation; `E.22` cannot authorize omitted coordinates, missing rationales, missing mandatory attention-discharge profiles, missing `PrecisionRestorationProfile` when `E.21` is used, unchecked loci, inactive/triggered-coordinate shortcuts, scope narrowing, or a weaker result form. |

### E.22:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **"Review this" prompt.** The evaluator infers purpose. | Add a `QualityEvaluationQuestionFrame`. |
| **Floor pass sold as excellence.** Readiness is mistaken for exceptional improvement. | State `exceptionalImprovementEvaluation` if wanted. |
| **Frame replaces result.** The question frame names a purpose but returns prose, a two-column value table, or proposal rows without the named evaluation's result form. | Re-run the named evaluation and return its required coordinates, evidence basis, rationales, and payload fields. |
| **Scope laundering.** The frame asks one use, but the result answers an easier, local-only, diagnostic, or evaluator-selected use. | Re-run the named evaluation under the requested use; if another use is needed, open a new frame rather than saving the current result. |
| **Applied-count absorption.** Closure count replaces quality movement. | Re-evaluate the changed object and classify impact. |
| **Goodharted improvement.** Visible values rise while protected qualities worsen, or a `5` target makes the evaluator add apparatus instead of improving content. | Frame the expected movement as a substantive content move, add trade-off protection, reject dominated changes, apply `E.13` when a visible value is replacing the intended value, and require checked `no proposal` dispositions when no worthwhile content improvement remains. |
| **Recommendation as decision.** A follow-up hypothesis is treated as chosen work. | Open the exact decision, work, publication, parity, refresh, evidence, or assurance pattern if that claim is needed. |
| **Lexical repair request.** A finding says only "replace this word" or "avoid that wording." | Rewrite the row as a precision-restoration finding with pre/post kind, relation, admissible use, and scope; if no kind-preserving repair is recoverable, leave it blocking. |

### E.22:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Review requests become typed. | Evaluators answer the intended quality question. | Requesters must name the object and evaluation. |
| Exceptional improvement becomes explicit. | Reviews can propose non-dominated improvements rather than stopping at floor defects. | Protected trade-offs must be named. |
| Absorption becomes quality-aware. | Follow-up says what improved or worsened. | Row discharge alone is not enough. |

### E.22:10 - Rationale

There is no neutral generic request when a quality result is wanted. The useful artifact is the framed question: object version, evaluation, purpose, expected evidence basis, expected result form, and boundary. This keeps review helpful without turning it into process control or project authority.

### E.22:11 - SoTA-Echoing

| Claim | Current or retained source line | Local adoption |
|---|---|---|
| Quality evaluation should be multidimensional, diagnostic, and actionable. | Current rubric and long-form evaluation work, including multidimensional LLM rubric evaluation and meta-evaluation lines, treats rubric validity and actionable feedback as current problems. | Findings name evaluation effects, expected movement, correction direction, and closure tests. |
| Feedback needs desired condition, current condition, next action, and evaluative tactics. | Sadler's formative-assessment line and Hattie/Timperley feedback model. | The frame states floor or desired aim, current evaluation object, expected result form, and proposal/no-proposal output. |
| Evaluation questions must derive from purpose. | GQM and GQM+Strategies lineage. | `QualityEvaluationPurposeSelection` precedes values, evidence basis, and proposal shape. |
| Multi-criteria improvement needs trade-offs and non-dominated alternatives. | MCDA, Pareto, ATAM lineage plus current architecture trade-off evaluation work. | `paretoTradeoffEvaluation` and `TradeoffProtectionSet` prevent one-score closure. |
| Measures used as targets can replace the intended object. | Goodhart/Campbell, management-accounting surrogation, and current proxy-failure work. | The frame separates floor repair from substantive exceptional proposals, rejects discharge count, popularity, review count, or all-`5` posture as value, and points proxy-to-value repair to `E.13`. |
| Agents can satisfy a literal specification while missing the intended outcome. | AI safety specification-gaming and reward-hacking lines, including current LLM-judge and reward-model bias work. | `DesiredImprovementAim` names content movement and protected trade-offs; proposal rows cannot close by adding proof apparatus that only satisfies the evaluator. |
| OEE/NQD needs proposal-shaped quality pressure before candidate change. | Current quality-diversity and open-ended exploration lines. | Proposal rows name expected quality movement before generation or selection neighbours consume them. |

### E.22:12 - Relations

| Pattern | Relation |
|---|---|
| `E.21` | Supplies pattern-quality values and required coordinates. |
| `E.9.DA` | Supplies `DRR` decision-adequacy values and required coordinates. |
| `E.2.DA` | Supplies FPF Pillar-adequacy values. |
| `E.19` | Supplies admission or refresh review profiles when that is the evaluation. |
| `E.23` | Governs repeated improvement after framed evaluations return findings or proposal rows. |
| `E.13` | Governs pragmatic utility and proxy-to-value alignment when framed values, visible measures, proposal counts, or all-`5` posture are being used as the intended improvement value. |

| `E.10`, `A.6.P`, `C.2.P`, `F.18` | Repair load-bearing wording and names introduced by frames or findings. |
| `C.16`, `A.17`, `A.18`, `A.19`, `C.25` | Govern characteristics, scales, measurements, characteristic spaces, and quality bundles. |
| `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Govern OEE/NQD candidate, archive/front, pool, selected-set, parity, and refresh claims. |
| `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, `B.3` | Receive decision, call-planning, work, gate, release, evidence, and assurance claims when a quality result is reused beyond evaluation. |

### E.22:End

