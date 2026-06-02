## E.22 - Improvement-Oriented Quality-Read Question Framing

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative

### E.22:1 - Problem frame

Use `E.22` when one author, reviewer, steward, external reviewer, or domain reviewer is about to ask for an improvement-oriented quality read, quality review, suggested improvements, returned-finding absorption, or multi-coordinate improvement over an object version whose quality is read through an explicit object-under-improvement evaluation: a characteristic space, scale set, rubric, review profile, quality bundle, or FPF pattern that supplies the relevant values.

In this pattern, bare `read` is too wide to carry doctrine. The local governed act is an improvement-oriented quality read: reading one exact object version for quality movement under a declared object-under-improvement evaluation, so that the result can say what remains admissible to do next. The read evaluates the object and returns a next-admissible-move hypothesis such as stop, first repair, narrowing, candidate improvement, trade-off warning, outside-evaluation assignment, or assignment to another exact pattern.

The next-admissible-move hypothesis remains below work planning, project decision, gate, release, evidence, or assurance unless that neighbouring pattern is opened. `E.22` therefore makes reading useful without pretending that the read already decided, planned, executed, approved, or released the next move.

`quality review` is the ordinary phrase for an `E.22`-framed improvement-oriented quality read. `QualityReadQuestionFrame` is the local record that frames that review before the object-under-improvement evaluation runs. A free-form review that does not declare object version, object-under-improvement evaluation, purpose, floor or improvement aim, trade-offs, result form, and non-use boundary is not a `quality review` in this pattern's sense.

Use it especially when the request could mean several different things:

- find blockers until the object reaches an admissible floor;
- raise already-admissible coordinates toward exceptional expression;
- check whether one improvement damaged usability, affordability, locality, corpus ecology, neighbour fit, or another protected quality;
- discover important questions that the requester did not ask;
- absorb returned review findings and state which qualities actually improved;
- read for candidate improvement proposals before changing the object;
- ask what admissible next move follows from the read without yet deciding, planning, executing, approving, or releasing that move;
- frame an OEE/NQD read over one candidate, front, archive, shortlist, parity report, refresh report, or declared transduction result so the read can return a bounded portfolio of evaluation-shaped candidate improvement proposals before generation, candidate-pool policy, front or archive insertion, selected-set publication, parity, or refresh moves to the governing patterns.

**Not this pattern when.** Use `E.23` when the work is a repeated improvement method across passes rather than one framed read. Use the object-under-improvement evaluation itself when the question is already declared and scoped: `E.21` for one authored FPF pattern version, `E.9.DA` for one `DRR` decision-adequacy claim, `E.19` for one admission or refresh review profile, `C.16`, `A.17`, `A.18`, or `A.19` for characteristic and measurement legality, `C.25` for an engineering quality bundle, `C.17` for novelty, value, surprise, constraint-fit, diversity, originality, or resource-efficiency characterization, `C.18` for NQD generation and archive/front semantics, `C.19` for live candidate-pool policy, `G.5` for selected-set publication, `G.9` for parity, `G.11` for refresh, or another exact rubric, review profile, or quality pattern when it governs the object. Use `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, or `B.3` when the live claim has already become decision, call planning, work, gate, release, evidence, or assurance. Use `E.10`, `A.6.P`, or `C.2.P` when the live problem is precision restoration of wording rather than framing a quality-read question.

**First useful move.** Before saying "review this", "improve this", or "what should we do next", name the object version under quality read, the object-under-improvement evaluation that supplies the quality values, the requested read purpose, the declared floor, the desired improvement aim, protected trade-offs, the open-question classification rule, and the kinds of candidate improvement proposals or next-admissible-move hypotheses that the read may return.

**Cheap stop.** If the requester only needs a blocker check for admissible use, declare `floorRead` and the floor. Do not ask for exceptional improvement, Pareto trade-off analysis, open-question discovery, absorption impact, candidate improvement proposals, or next-move alternatives unless those purposes are live.

**What goes wrong if missed.** Reviewers answer the wrong question. A request intended as "raise quality as far as feasible" becomes a blocker audit. A request intended as "is this usable enough?" becomes a maximal rewrite. A returned review is marked "applied" without saying which coordinates improved. A high-coordinate rewrite damages first use, affordability, locality, or corpus ecology and still looks successful. A "read" sounds harmless while it quietly recommends work, selection, release, or assignment without naming the object-under-improvement evaluation or neighbouring pattern. OEE/NQD search changes candidate material without evaluation-shaped proposals, so exploration becomes unguided candidate change rather than disciplined generation and selection.

**What this buys.** `E.22` makes the improvement-oriented quality-read question explicit before the read starts. It separates admissibility, exceptional improvement, trade-off inspection, open-question discovery, absorption impact, candidate improvement proposals, and next-admissible-move hypotheses, so the object-under-improvement evaluation can answer the right question instead of silently defaulting to a floor check.

**Governed object in plain terms.** The governed object is the quality-read question frame: a compact declaration of which improvement-oriented evaluative read purpose is being requested for which object and under which object-under-improvement evaluation, including which candidate improvement proposals or next-admissible-move hypotheses the read may return.

**Primary working reader.** The first reader is the person asking for or running the quality read. The downstream reader is the author who must use the result to repair, narrow, improve, or stop.

### E.22:2 - Problem

Quality reads often begin with an underspecified request such as "review this", "evaluate quality", "improve this", or "tell me what is wrong." Those phrases hide different governed questions.

The first failure is the fantasy of "just reading." A useful quality read always has a purpose: read for admissibility, read for exceptional improvement, read for trade-off exposure, read for open-question discovery, read for absorption impact, or read for candidate improvement proposals and the next admissible move. If the purpose is not declared, the reviewer supplies one implicitly, and the resulting proposal or next move may be too weak, too broad, or assigned to the wrong governing pattern.

The recurring failures are:

1. **Floor-default surprise.** The requester expects maximal improvement, but the reviewer returns only blockers against the minimum floor.
2. **Exceptional-overreach surprise.** The requester expects a cheap readiness check, but the reviewer proposes broad optimization and costly rewrites.
3. **Single-purpose flattening.** A review mixes blockers, exceptional-improvement ideas, trade-off warnings, open questions, and absorption impact without saying which result belongs to which purpose.
4. **Goodhart by review prompt.** The prompt asks to raise visible coordinates without asking what became worse.
5. **Open-question blindness.** Review answers the named checklist but does not say which important question was not asked.
6. **Absorption opacity.** Returned findings are marked applied, but the resulting quality movement is invisible: which coordinates rose, which stayed floor-only, which trade-offs appeared, and which object-under-improvement evaluation now receives unresolved quality work.
7. **Wrong object-under-improvement evaluation.** Pattern-quality, DRR-adequacy, admission review, engineering quality bundles, local rubrics, lexical repair, OEE/NQD set-result questions, and project evidence are collapsed into one broad "quality" request.
8. **Next-move overread.** A read suggests a repair, narrowing, reassign, shortlist, refresh, or work step, and the suggestion is treated as if the read had already made the decision or plan.
9. **Unguided candidate-change exploration.** OEE/NQD exploration changes candidate material without evaluation-shaped proposals, so the candidate generator explores superficial variation without knowing which quality movement each change is meant to test.

### E.22:3 - Forces

| Force | Tension |
|---|---|
| **Low-cost readiness vs ambitious improvement** | A floor check should be cheap, but exceptional improvement needs richer scenario and trade-off reasoning. |
| **Explicit purpose vs reviewer autonomy** | The requester must state the requested read purpose, while the reviewer must still report important unasked questions. |
| **Evaluation vs next move** | A useful read often suggests a next admissible move, but that suggestion must not become decision, planning, work, gate, evidence, assurance, release, or OEE/NQD publication by stealth. |
| **Improvement proposal portfolio vs unguided candidate change** | OEE/NQD and ordinary improvement loops may need a portfolio of candidate improvement proposals, but those proposals should be shaped by a declared object-under-improvement evaluation while generation, pool policy, front or archive handling, selection, publication, parity, and refresh stay with governing patterns. |
| **Multi-coordinate improvement vs Goodhart risk** | Improving one coordinate can degrade another quality that was not foregrounded. |
| **Actionability vs over-instrumentation** | A quality read should return repairable findings without turning every request into a full audit harness. |
| **Specific object-under-improvement evaluation vs shared framing** | `E.21`, `E.9.DA`, `C.25`, local rubrics, declared characteristic spaces, OEE/NQD evaluation patterns, and other quality-bearing evaluations supply their values; `E.22` governs only the question framing that selects the requested read purpose and allowed proposal or next-move hypothesis shape. |
| **External review usefulness vs prompt ambiguity** | External reviewers can supply much better findings when the requested read purpose and desired output are explicit. |

### E.22:4 - Solution

State a `QualityReadQuestionFrame` before running a substantive improvement-oriented quality read.

`QualityReadQuestionFrame := <ObjectVersionUnderQualityRead, ObjectUnderImprovementEvaluationRef, QualityReadPurposeSelection, DeclaredQualityFloor?, DesiredImprovementAim?, TradeoffProtectionSet?, OpenQuestionClassificationRule?, AbsorptionImpactClassificationRule?, CandidateImprovementProposalRule?, NextAdmissibleMoveHypothesisRule?, ExpectedResultForm, NonUseBoundary>`

`QualityReadQuestionFrame` is a local question-framing record. It is not a review result, gate, assurance record, evidence record, release condition, work item, score sheet, discharge-count result, checklist-count result, candidate-pool policy, selector publication, refresh plan, unguided candidate-change policy, or second quality characteristic space.

#### E.22:4.1 - Local names and kind settlement

| Local name | Role | Non-use boundary |
|---|---|---|
| `QualityReadQuestionFrame` | Compact declaration of the requested quality read before the read runs. | Not the quality read itself, not a review packet, not a gate, not an ordered execution plan. |
| `ObjectVersionUnderQualityRead` | Exact object version whose quality is being read. | Not a vague object label, source bundle, campaign, chat thread, or unnamed candidate pool. For OEE/NQD material, name the candidate, front, archive, shortlist, parity report, refresh report, or declared transduction result and the governing pattern that gives it that object kind. |
| `ObjectUnderImprovementEvaluationRef` | The exact evaluation that supplies the read values: for example `E.21`, `E.9.DA`, `E.19`, `C.25`, `C.16`, `A.19`, `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, a declared characteristic space, scale set, rubric, review profile, or another local quality pattern. | Does not let `E.22` borrow that evaluation's values or invent coordinates when no object-under-improvement evaluation is declared. |
| `QualityReadPurposeSelection` | Declared subset of read purposes requested now. | Not an ordered execution sequence and not a maturity ladder. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor for this request, when a floor claim is live. | Not a release gate or proof of quality by itself. |
| `DesiredImprovementAim` | The requested improvement aim beyond the floor, if any. | Not permission to optimize visible values while damaging protected qualities. |
| `TradeoffProtectionSet` | Quality properties that must not be silently degraded while other coordinates improve. | Not a hidden score and not a substitute for the object-under-improvement evaluation's coordinates or values. |
| `OpenQuestionClassificationRule` | How unasked but important questions are classified. | Not an invitation to open unrelated FPF work. |
| `AbsorptionImpactClassificationRule` | How returned-finding absorption classifies coordinate movement and trade-offs. | Not a count of accepted suggestions and not a reviewer-answer log. |
| `CandidateImprovementProposalRule` | Allowed shape for one proposal or a bounded proposal portfolio returned by the read: expected object-under-improvement evaluation movement, affected locus, protected trade-offs, closure test, and neighbour exit. | Not a candidate generator, mutation policy, candidate-pool policy, front or archive insertion rule, selected-set publication, work plan, or proof that any proposed change should be applied. |
| `NextAdmissibleMoveHypothesisRule` | Allowed shapes for next-move hypotheses returned by the read: stop, repair, narrow, candidate improvement proposal, trade-off warning, outside-evaluation assignment, or assignment to an exact neighbouring pattern. | Not a decision result, `CallPlan`, work plan, execution order, gate, release, evidence, assurance, selector publication, pool policy, parity report, or refresh plan. |
| `CandidateImprovementProposalPortfolio` | Bounded set of proposal rows returned by the read when the requester needs alternatives for generation, comparison, selection, or later loop work. | Not a candidate pool, archive, front, shortlist, selected-set publication, parity result, refresh plan, or decision that any proposal wins. |
| `QualityReviewFindingRow` | Stable actionable row for one returned finding that requires repair, narrowing, or explicit non-use. | Not a narrative review paragraph, not a grouped range, and not quality closure by itself. |

These local names remain local to `E.22` unless a separate FPF naming decision promotes one through `F.18`. The word `frame` here means a declared question boundary; it is not a publication face, UI frame, architecture frame, review phase, or generic container.

#### E.22:4.1a - Placement and specialization boundary

`E.22` is not limited to FPF pattern review or `DRR` review. It applies when a quality-bearing object has a declared object-under-improvement evaluation: pattern version, `DRR`, architecture description, engineering work result, method, policy, text, benchmark result, declared transduction result, or other object whose quality values are supplied by an explicit characteristic space, scale set, rubric, review profile, quality bundle, or exact FPF pattern.

`E.22` belongs in Part E because it governs how an FPF-side quality review question is asked before the object-under-improvement evaluation runs. It does not belong inside `E.21` or `E.9.DA`, because those patterns supply object-specific characteristic spaces. It does not belong inside `C.16`, `A.17`, `A.18`, `A.19`, or `C.25`, because it does not define characteristics, scales, measures, characteristic spaces, or quality bundles. It is also not an engineering evaluation method: concrete engineering, design, architecture, or product-review methods stay in the object-under-improvement evaluations that govern them.

Object-specific specializations are not required merely because the object version under quality read is a pattern, `DRR`, engineering work result, architecture, policy, or text. The ordinary shape is: use `E.22` for the question frame; use the exact object-under-improvement evaluation for coordinates, floors, values, dominance, status, and repair. A specialization is admissible only when a recurring object family needs additional read purposes, result forms, or protected trade-offs that cannot be expressed by this generic frame plus the object-under-improvement evaluation.

If no object-under-improvement evaluation is named, `E.22` can only repair the question by requiring one. It cannot turn a bare "review anything" request into quality values.

#### E.22:4.1b - OEE/NQD read placement

`E.22` can frame a quality read over OEE/NQD material, but it does not become OEE/NQD doctrine.

When the object version under quality read is a generated candidate, `Front`, `Q-Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, parity report, refresh report, or declared transduction result, the frame names both:

1. the exact candidate, object version, or set-result family under quality read; and
2. the governing pattern that carries the live semantics.

Typical assignments:

When the declared object-under-improvement evaluation is also the `Q` side of an NQD or OEE comparison, the read may return a bounded portfolio of candidate improvement proposals, not one chosen improvement. Each proposal row states the `Q` movement sought, affected locus, protected trade-offs, closure test, and neighbour exit. The front is set by the object-under-improvement evaluation's declared comparison set, external candidate set, `SoTA` line, front, or archive; it is not inferred from the reader's preference that the object feels better. The portfolio can aim the object version under quality read, generated candidate, or candidate family toward that current non-dominated front, beyond the current front under one declared `Q` component without damaging protected components, or into a not-yet-covered high-`Q` region under declared `Q` components. Choosing which proposals to generate or retain, inserting candidates into a front or archive, publishing a shortlist, and refreshing parity stays with `C.18`, `C.19`, `G.5`, `G.9`, or `G.11`.

| Live read question | Object-under-improvement evaluation or governing pattern |
|---|---|
| Candidate novelty, use-value, surprise, constraint fit, diversity, originality, or resource efficiency | `C.17` or its declared characteristic space |
| NQD generation, descriptor/distance/insertion pins, front/archive semantics, illumination telemetry | `C.18` |
| Live candidate-pool treatment: widen, keep frontier, narrow, sunset, or reroute | `C.19` |
| Public selected-set result: `Shortlist`, `RankedShortlist`, narrowed selected-set transfer, abstain, or escalation | `G.5` |
| Benchmark or parity comparison over selected sets, archives, fronts, or method families | `G.9` |
| Refresh of shipped set results, archive telemetry, parity reports, or OEE/NQD pins | `G.11` |

`E.22` then selects the read purpose: `floorRead`, `exceptionalImprovementRead`, `paretoTradeoffRead`, `openQuestionDiscoveryRead`, `absorptionRead`, or a declared combination. It may ask whether the selected governing pattern has enough information to run, whether the read found a blocker, whether one candidate or set result can improve under the declared evaluation, whether a candidate-change proposal is worth generating, or whether a returned finding changed the object-under-improvement evaluation's result.

The same portfolio rule applies to the ordinary FPF self-use cases. When `E.21` or `E.9.DA` is the object-under-improvement evaluation and the requested purpose is exceptional improvement, the read should not stop at the first defect. It may return a bounded portfolio of non-dominated proposal rows across active coordinates: for example first-use usability, source-content preservation, relation precision, examples, decision-bearing content, and protected trade-offs. The external comparison may be current FPF neighbour practice, accepted `SoTA`, competing pattern candidates, prior front members, or an explicit declared use frontier supplied by the object-under-improvement evaluation. In this use, `SoTA` is the working external front assigned by the object-under-improvement evaluation or accepted source posture. An exceptional proposal may try to reach, maintain, or improve that externally assigned front, but the read itself does not assign `SoTA` to the object. `E.23` governs any repeated application and re-read of those rows.

This is the entry point that keeps OEE/NQD candidate changes from becoming unguided candidate changes. The read proposes candidate changes from object-under-improvement evaluation pressure: what quality movement is expected, what trade-off must be protected, what closure test would make the proposal worth retaining, and which neighbouring pattern must govern generation, pool policy, set-result publication, parity, or refresh.

It must not replace OEE/NQD semantics. In particular, an `E.22` frame must not treat `IlluminationSummary`, coverage, regret, review count, popularity, or one benchmark headline as a quality value unless the governing pattern and policy explicitly promote that signal. It must not rename a `Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, or `ParityReport` as a generic portfolio. It must not collapse candidate quality, archive/front relation, selected-set publication, parity, and refresh into one result.

#### E.22:4.1c - Front-like vocabulary harmonization

Different practices arrive with different words for nearly the same working question: "raise it to all `5`s", "make it exceptional", "reach `SoTA`", "move to the Pareto front", "improve the NQD `Q` side", "return a portfolio", or "publish a shortlist." `E.22` does not make those words synonyms. It turns them into one framed read question and names the object-under-improvement evaluation that supplies the exact meaning.

| Incoming vocabulary | First `E.22` question | Governing pattern or object-under-improvement evaluation |
|---|---|---|
| all `5`s, exceptional, high-coordinate quality | Which object-under-improvement evaluation supplies the coordinates and value meanings? | `E.21`, `E.9.DA`, `C.25`, or another exact quality evaluation |
| `SoTA`, current best, frontier practice | Who assigns the current external front, and what source posture makes it admissible? | object-under-improvement evaluation plus `E.8` source posture and exact `SoTA` rows |
| Pareto front, non-dominated option, no forced winner | Which dominance relation and comparison set are declared? | `E.21`, `E.9.DA`, `C.18`, `G.5`, or exact local characteristic-space pattern |
| NQD, Q-front, archive, open-ended search | Is the live claim candidate quality, novelty, diversity, archive/front semantics, pool policy, or refresh? | `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11` |
| improvement portfolio, proposal portfolio | Is this only proposal rows, or a selected set publication? | `E.22` for proposal rows; `E.23` for repeated application; `G.5` for selected-set publication |
| shortlist, ranked shortlist, selected set | Is a public set result being published? | `G.5`, with parity or refresh through `G.9` or `G.11` when live |

The practical first path is: name the vocabulary used by the requester, translate it to the first object-under-improvement evaluation question, then assign any claim that exceeds the quality-read frame to the governing pattern. This preserves discoverability without letting familiar words import a second ontology.

#### E.22:4.2 - Quality read purposes

`QualityReadPurposeSelection` uses these values:

| Purpose value | Use when | Required result shape |
|---|---|---|
| `floorRead` | The question is whether the object reaches a declared floor for the intended use. | blockers below floor, first repair locus, narrowed use or admissible stop. |
| `exceptionalImprovementRead` | Active coordinates already meet the floor, and the requester wants non-dominated improvements toward exceptional expression where feasible. | per-coordinate improvement candidate from current value toward `exceptionallyExpressedForDeclaredUse`, or a by-value no-candidate disposition saying why no non-dominated edit is feasible, needed, or admissible for that coordinate under the declared use. |
| `paretoTradeoffRead` | A candidate improvement may raise some coordinates while degrading usability, affordability, locality, corpus ecology, neighbour fit, or another quality. | non-dominated candidate comparison, protected-quality losses, and whether a variant should be ordinary-use, high-assurance, narrowed, or rejected. |
| `candidateImprovementProposalRead` | The requester needs one evaluation-shaped proposal or a bounded proposal portfolio before changing an object or generating OEE/NQD variants. | candidate-change proposal row or proposal portfolio with expected object-under-improvement evaluation movement, affected object locus or set-result locus, protected trade-offs, closure test, and neighbour exit when generation, pool policy, front or archive handling, publication, parity, or refresh is live. |
| `openQuestionDiscoveryRead` | The requester wants important unasked questions made visible rather than only answered checklist items. | questions classified as existing-coordinate issue, candidate new coordinate or overlay, or outside the current object-under-improvement evaluation with the exact object-under-improvement evaluation named. |
| `absorptionRead` | Returned review findings or suggested improvements are being absorbed. | applied or not-applied disposition plus coordinate-impact account: improved, floor-only, unchanged, worsened, trade-off introduced, or outside object-under-improvement evaluation. |

The purposes may be combined, but the result must keep them distinguishable. A floor blocker does not answer exceptional improvement. A trade-off warning does not by itself lower a coordinate unless the object-under-improvement evaluation says that the protected quality is active. Open-question discovery does not become permission to rewrite the object outside the declared object-under-improvement evaluation.

If no purpose is declared, the default is `floorRead` under the object-under-improvement evaluation's default floor. Absence of an explicit `exceptionalImprovementRead` means the reviewer is not obligated to propose every plausible edit toward `5`.

#### E.22:4.3 - Prompt grammar

A conforming request has this shape:

```text
Quality-read question:
  Object version under quality read: <exact object version>
  Object-under-improvement evaluation: <E.21 | E.9.DA | E.19 | C.16, A.19, or C.25 | C.17, C.18, C.19, G.5, G.9, or G.11 for OEE/NQD reads | declared characteristic space | scale set | rubric | review profile | other exact evaluation>
  Read purpose selection: <floorRead | exceptionalImprovementRead | paretoTradeoffRead | candidateImprovementProposalRead | openQuestionDiscoveryRead | absorptionRead | combined>
  Declared quality floor: <floor and scope, or "object-under-improvement evaluation default">
  Desired improvement aim: <floor-only | raise non-dominated coordinates toward exceptional | compare variants | propose candidate changes | discover missing questions | absorption impact>
  Protected trade-offs: <usability | affordability | repair locality | corpus ecology | neighbour fit | source-content loss under the object-under-improvement evaluation | entry and projection integrity | other exact properties>
  Open-question classification rule: <classify by existing coordinate | candidate coordinate or overlay | outside object-under-improvement evaluation>
  Candidate improvement proposal rule: <single proposal | bounded proposal portfolio | expected movement | affected locus | protected trade-offs | closure test | neighbour exit>
  Next-admissible-move hypothesis rule: <stop | first repair | narrow use | candidate improvement proposal | trade-off warning | outside-evaluation assignment | assignment to an exact neighbouring pattern>
  Expected result form: <blockers | per-coordinate improvement candidates | candidate-change proposal rows | bounded proposal portfolio | Pareto trade-off table | open-question classification | absorption impact account | next-move hypothesis list>
  Non-use boundary: <what this read must not certify, decide, plan, execute, publish, or rewrite>
```

The short form is admissible when only the floor is live:

```text
Quality-read question:
  Object version under quality read: <exact object version>
  Object-under-improvement evaluation: <exact evaluation>
  Read purpose selection: floorRead
  Declared quality floor: <floor>
```

If the short `floorRead` finds no blocker, a compact admissible-stop statement is enough. If it returns blockers, repairs, narrowed-use requirements, or outside-evaluation assignments, each actionable item becomes a `QualityReviewFindingRow` with exact locus, correction direction, and closure test. The short form makes the question cheap; it does not permit narrative returned work that cannot be discharged row by row.

#### E.22:4.4 - Purpose-specific reviewer questions

| Purpose | Ask the reviewer |
|---|---|
| `floorRead` | Which active coordinates, eligibility rows, statuses, or declared floors fail? What is the first repair, narrowed use, or admissible stop? |
| `exceptionalImprovementRead` | For each active coordinate already at the floor, what non-dominated edit could raise it toward exceptional expression, or why is no non-dominated edit feasible, needed, or admissible for that coordinate under the declared use? What exact text, case, relation, SoTA row, boundary, or example would have to change if a candidate exists? |
| `paretoTradeoffRead` | What became worse while visible coordinates improved? Which protected qualities changed: first-use cost, authoring cost, maintenance cost, neighbour cost, source-loss risk, entry and projection integrity, corpus ecology, or practical payoff? |
| `candidateImprovementProposalRead` | What candidate change or bounded proposal portfolio should be proposed, what object-under-improvement evaluation movement is expected for each row, what trade-off must be protected, what closure test would confirm the movement, and which neighbour governs generation, pool policy, selected-set publication, parity, refresh, decision, planning, or work if a proposal leaves the read? |
| `openQuestionDiscoveryRead` | What important question was not asked? Is it an issue under an existing coordinate, a candidate new coordinate or overlay, or outside this object-under-improvement evaluation under another exact object-under-improvement evaluation? |
| `absorptionRead` | After applying findings, which coordinates improved, which remained floor-only, which stayed unchanged, which worsened, which trade-offs appeared, and which issues moved to another exact object-under-improvement evaluation? |
| any declared purpose with next-move output | Given the object-under-improvement evaluation read, what next admissible move is only a hypothesis: stop, repair, narrow, candidate improvement proposal, outside-evaluation assignment, or assignment to an exact neighbouring pattern? What claim would require `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, `B.3`, `C.18`, `C.19`, `G.5`, `G.9`, or `G.11` before it can be used? |

These are question forms, not mandatory result sections. A reviewer may answer compactly when the object is small and the declared purpose is narrow.

When any purpose returns work for the object version under quality read, the result uses `QualityReviewFindingRow` and names the affected object-under-improvement evaluation coordinate, eligibility row, status, protected quality, or outside object-under-improvement evaluation. Findings such as "improve wording", "make clearer", "add examples", or "tighten rationale" are nonconforming until they state the expected quality movement and the object-under-improvement evaluation effect.

#### E.22:4.5 - Result classification for absorption

`absorptionRead` does not end at "accepted", "applied", "not applied", or "done." Each material finding receives one of these quality-impact classifications:

| Absorption impact | Meaning |
|---|---|
| `coordinateImproved` | A named coordinate or eligibility row has better content evidence under the object-under-improvement evaluation. |
| `floorOnlyClosure` | A blocker or ambiguity was removed enough to carry the declared floor, but not enough to justify exceptional expression. |
| `unchangedBecauseAlreadySatisfied` | The returned suggestion was already satisfied by value in the object version under quality read. |
| `tradeoffIntroduced` | The applied change improved one property while introducing a cost, ripple, or protected-quality risk. |
| `qualityLossDetected` | The applied or proposed change would lower one active coordinate or protected quality. |
| `outsideObjectUnderImprovementEvaluation` | The suggestion belongs under another exact FPF pattern, evaluation, or decision object. |
| `notAdmissibleForDeclaredUse` | The suggestion is rejected for the declared quality-read purpose and non-use boundary. |

The absorption record may stay as a checklist, but the checklist is not the quality result. The quality result is the impact on the object-under-improvement evaluation's characteristic space, status, stop condition, non-use boundary, or assignment to another exact object-under-improvement evaluation.

#### E.22:4.5a - Actionable quality-review finding rows

When a quality read or quality review returns actionable findings, each actionable finding is represented as one `QualityReviewFindingRow`.

`QualityReviewFindingRow := <QualityReviewFindingRowId, ReviewFindingLocus, ObjectLocusUnderRepair, QualityReadPurposeEffect, ObjectUnderImprovementEvaluationEffect, ExpectedQualityMovement, CandidateImprovementProposalSet?, NextAdmissibleMoveHypothesis?, CorrectionDirection, ClosureTest, RowDisposition, DischargeEvidenceRef?>`

The row shape is active for any returned blocker, repair, narrowing, trade-off warning, open question assigned to the object version under quality read, or absorption item that requires executor action. It is not required for a clean `floorRead` that returns only an admissible-stop statement.

| Field | Meaning |
|---|---|
| `QualityReviewFindingRowId` | Stable row id such as `QR-E22-001`; not a range and not "all findings". |
| `ReviewFindingLocus` | Exact locus in the quality review or returned finding. |
| `ObjectLocusUnderRepair` | Exact section, row, name, example, relation, checklist item, SoTA row, or entry cue in the object version under quality read. |
| `QualityReadPurposeEffect` | Which purpose produced the row: `floorRead`, `exceptionalImprovementRead`, `paretoTradeoffRead`, `openQuestionDiscoveryRead`, `absorptionRead`, or a declared combination. |
| `ObjectUnderImprovementEvaluationEffect` | Object-under-improvement evaluation coordinate, eligibility row, status, protected quality, or outside object-under-improvement evaluation affected by the row. |
| `ExpectedQualityMovement` | Expected movement such as blocker removal, coordinate improvement, floor-only closure, quality-loss prevention, trade-off exposure, bounded non-use, or outside-evaluation assignment. |
| `CandidateImprovementProposalSet?` | Optional single proposal or bounded proposal portfolio, with expected object-under-improvement evaluation movement, affected locus, protected trade-offs, closure test, and neighbour exit for each row when generation, pool policy, front or archive handling, selected-set publication, parity, refresh, decision, planning, or work is live. |
| `NextAdmissibleMoveHypothesis?` | Optional stop, repair, narrow, candidate improvement proposal, outside-evaluation assignment, or assignment to an exact neighbouring pattern suggested by the read. |
| `CorrectionDirection` | The concrete repair, narrowing, non-use statement, or object-under-improvement evaluation assignment requested. |
| `ClosureTest` | What must be true in the changed object for the row to close. |
| `RowDisposition` | `open`, `applied`, `alreadySatisfied`, `notAdmissibleForDeclaredUse`, `movedToObjectUnderImprovementEvaluation`, or another local disposition with narrower meaning. |
| `DischargeEvidenceRef?` | Optional exact changed locus or unchanged-by-value locus used by the executor to show what was done. |

"Closed in general", "handled overall", "all rows done", and range closure are nonconforming. If one edit closes several rows, each row still keeps a separate `QualityReviewFindingRowId`, object-under-improvement evaluation effect, closure test, disposition, and discharge evidence.

#### E.22:4.5b - Quality-review record separation

A quality review keeps four records distinct:

1. `QualityReadQuestionFrame` states the question being asked.
2. The reviewer quality result states the object-under-improvement evaluation reading, returned findings, coordinate and value effects, protected-quality trade-offs, bounded non-use, and outside-evaluation assignments.
3. Executor discharge evidence states what changed, which row disposition was selected, and which changed or unchanged object locus is cited for each `QualityReviewFindingRow`.
4. The next reviewer re-read states whether the changed object now satisfies the object-under-improvement evaluation for the declared purpose.

Executor discharge evidence is not the reviewer quality result and is not quality closure by itself. An impact account may show intended or observed movement, but closure comes only from re-running the object-under-improvement evaluation on the changed object or from a reviewer statement that a row was already satisfied by value.

#### E.22:4.6 - Work order for using this pattern

One `quality review` is one framed read of one exact object version.

For one quality review:

1. Name the object version under quality read.
2. Name the quality-read object-under-improvement evaluation.
3. Select one or more quality read purposes.
4. State the declared floor and improvement aim for this read.
5. State protected trade-offs, open-question classification rule, candidate improvement proposal rule, and next-admissible-move hypothesis rule when they are live.
6. Ask the reviewer for the purpose-specific result shape.
7. Run the object-under-improvement evaluation.
8. If absorbing findings, record coordinate impact and trade-offs, not only disposition.
9. If proposing candidate changes, state expected object-under-improvement evaluation movement, protected trade-offs, closure test, and neighbour exit before changing the object or generating variants.
10. State any next admissible move only as a hypothesis unless the exact neighbouring pattern is also opened.
11. Stop that read when the result answers the declared purpose and states any remaining bounded non-use or outside object-under-improvement evaluation.

When the goal is repeated improvement of the object beyond this one read, use `E.23`. `E.23` invokes `E.22` for each review pass and governs row-atomic absorption across passes, object-under-improvement evaluation re-read of the changed object version, method-family or operation-family selection, and the stop, narrow, continue, switch method, or hold decision. `E.22` does not govern the repeated method.

`QualityReviewFindingRow` remains the row shape for returned actionable findings. Executor discharge evidence is not a quality value until the object-under-improvement evaluation re-reads the changed object or states that the row was already satisfied by value.

An all-`5` claim requires an explicit coordinate-value table over the changed object. It cannot be inferred from a floor-pass capsule, a clean discharge table, an external-review absorption pass, landing, popularity, adoption, or the absence of blockers.

#### E.22:4.7 - Self-application boundary

`E.22` may be used to frame a quality read of the `E.22` pattern text. In that case, the object-under-improvement evaluation remains `E.21`; `E.22` supplies only the question frame. A self-read may ask for `floorRead`, `exceptionalImprovementRead`, `paretoTradeoffRead`, `openQuestionDiscoveryRead`, or `absorptionRead`, but the coordinate values, stop result, and repair result still come from `E.21`.

A minimal `E.22` self-application frame is:

```text
Quality-read question:
  Object version under quality read: E.22 authored pattern version
  Object-under-improvement evaluation: E.21
  Read purpose selection: floorRead + exceptionalImprovementRead + paretoTradeoffRead + openQuestionDiscoveryRead
  Declared quality floor: 4 wellExpressedForDeclaredUse on active E.21 coordinates
  Desired improvement aim: raise non-dominated coordinates toward 5 where feasible
  Protected trade-offs: ordinary-use affordability; row-atomic discharge; no object-under-improvement evaluation replacement; no gate, release, or work overread; no reputation-medal scoring
  Open-question classification rule: existing E.21 coordinate | candidate E.21 overlay | outside E.21 under another exact object-under-improvement evaluation
  Expected result form: stable QualityReviewFindingRows plus E.21 coordinate capsule
  Non-use boundary: not a gate, release, assurance, project certificate, or self-certifying quality result
```

Do not create a second quality space in which `E.22` grades the `E.22` question frame. If the self-read exposes a weak question frame, repair the `E.22` text or narrow the declared use; if it exposes a problem in the object-under-improvement evaluation, use the exact object-under-improvement evaluation that governs that problem.

#### E.22:4.8 - Sufficient frame, lowering conditions, and reopen conditions

A `QualityReadQuestionFrame` is sufficient when another reader can recover the object version under quality read, the object-under-improvement evaluation, the selected read purpose, the declared floor or improvement aim, the protected trade-offs when improvement is requested, the classification rule for unasked questions when discovery is requested, the impact classification for absorption when returned findings are being applied, the candidate improvement proposal rule when proposals are requested, the next-admissible-move hypothesis rule when next moves are requested, and the non-use boundary for overread-prone results.

Lower the quality read of an `E.22` use, or repair the frame before running the object-under-improvement evaluation, when any of these is true:

1. object version under quality read is missing or depends on chat memory;
2. object-under-improvement evaluation is missing, so `E.22` would have to invent coordinates;
3. a bare request such as "review this" is later interpreted as `exceptionalImprovementRead` without having declared that purpose;
4. `exceptionalImprovementRead` lacks an active coordinate menu or expected per-coordinate improvement result;
5. `paretoTradeoffRead` lacks protected qualities even though the proposed change can affect usability, affordability, repair locality, corpus ecology, neighbour fit, or entry and projection integrity;
6. `openQuestionDiscoveryRead` lacks classification into existing coordinate, candidate coordinate or overlay, or outside object-under-improvement evaluation;
7. `absorptionRead` records accepted or applied disposition without coordinate-impact classification;
8. the frame lets the resulting quality read be overread as project evidence, assurance, gate, release, certification, safety, compliance, work authority, general approval, checklist-count closure, or discharge-count closure;
9. the frame asks the reviewer to treat popularity, adoption, prior use, absence of use, review count, reviewer praise, external-review completion, landing, release, or award-like signals as quality values rather than as possible pointers to content evidence under the object-under-improvement evaluation.
10. the frame asks for next action, recommendation, reassign, shortlist, refresh, plan, release, work, evidence, assurance, or gate result without saying whether the read may return only a candidate improvement proposal or next-admissible-move hypothesis, or must be assigned to the exact neighbouring pattern.
11. the frame asks for OEE/NQD candidate changes but does not state the object-under-improvement evaluation pressure that makes each proposal worth generating;
12. the frame asks for a proposal portfolio but does not name which neighbouring pattern governs generation, pool policy, front or archive handling, selection, selected-set publication, parity, or refresh.

Reopen or restate the frame when the object version, object-under-improvement evaluation, declared floor, active coordinate menu, protected trade-off set, external findings being absorbed, or expected result form changes. An object-under-improvement evaluation finding may also show that the requested purpose was too narrow; then the extra result is either added to the frame or marked outside the declared frame.

### E.22:5 - Archetypal grounding

**Show, pattern floor read.** A requester says, "Review this E.21 pattern." The frame is missing. `E.22` defaults to `floorRead`: the reviewer checks whether active E.21 coordinates meet the declared floor and returns blockers or admissible stop. The reviewer is not obligated to propose every plausible edit toward `5`.

**Show, exceptional improvement read.** A requester says, "This pattern already has all active E.21 coordinates at `4`; propose non-dominated edits that could raise each one toward `5` without damaging ordinary use." The frame selects `exceptionalImprovementRead` plus `paretoTradeoffRead`. The reviewer must answer per active coordinate and must name protected trade-offs.

**Show, DRR adequacy read.** A requester says, "Can this DRR carry pattern drafting?" The object-under-improvement evaluation is `E.9.DA`, not `E.21`. If the requester wants maximum DRR strength, the frame must say `exceptionalImprovementRead` over the active `E.9.DA` coordinates. Otherwise the default question is only whether the `DRR` meets the declared drafting floor.

**Show, engineering work-result quality read.** A requester says, "Raise this interface design review toward exceptional." The object version under quality read is the named interface design version. The object-under-improvement evaluation is the declared design-quality characteristic space, `C.25` quality bundle, local rubric, or other exact review profile, not `E.21` unless the object is an FPF pattern. `E.22` asks whether the read is floor-only, exceptional-improvement, trade-off, open-question, absorption, candidate-proposal, or a declared combination.

**Show, architecture-quality read.** A requester says, "Review this architecture description and suggest improvements." The object-under-improvement evaluation must be named: for example an architecture-quality rubric, characteristic space, `C.25` quality bundle, or exact architecture review profile. `E.22` prevents the request from silently mixing a blocker check, exceptional improvement, ATAM-like trade-off discovery, and open-question discovery.

**Show, OEE/NQD read.** A requester asks, "Is this generated set good enough to keep exploring from, and what candidate changes should we consider next?" The frame must first name the object version under quality read: one candidate, `Front`, `Q-Front`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, parity report, refresh report, or declared transduction result. It then names the object-under-improvement evaluation: for example `C.17` for candidate characteristics, `C.18` for archive and front semantics, `C.19` for pool policy, `G.5` for selected-set publication, `G.9` for parity, or `G.11` for refresh. `E.22` frames the read purpose and the candidate improvement proposal rule: expected quality movement, protected trade-off, closure test, and neighbour exit for each proposal row. If the useful result is a bounded proposal portfolio, selection by NQD, front or archive placement, selected-set publication, parity, and refresh remain with the governing patterns. `E.22` does not turn illumination telemetry, a public shortlist, or a proposed candidate change into one scalar quality result.

**Show, absorption read.** An external review returns fifty suggestions. A checklist tracks them one by one, but `E.22` requires one additional quality impact result: which coordinates actually improved, which stayed floor-only, which trade-offs were introduced, and which suggestions were outside the object-under-improvement evaluation.

**Near miss, all-to-five prompt.** "Raise all coordinates to exceptional" is incomplete. It lacks protected trade-offs and an open-question classification rule. The repaired frame asks for non-dominated improvements toward exceptional expression where feasible and rejects edits that damage declared usability, affordability, locality, corpus ecology, neighbour fit, or another active protected quality.

### E.22:6 - Bias annotation

`E.22` intentionally biases review prompts toward explicit purpose and away from hidden reviewer authority.

The bias is useful because underspecified prompts repeatedly produce the wrong quality-read purpose. The bias is dangerous when it turns every small review into a long preamble. Keep the short form for ordinary `floorRead` cases.

### E.22:7 - Conformance checklist

| ID | Requirement | Why |
|---|---|---|
| `CC-E22-1` | A nontrivial quality read SHALL name the exact object version under quality read. | Prevents chat memory, source bundles, or campaigns from replacing the object. |
| `CC-E22-2` | A nontrivial quality read SHALL name the object-under-improvement evaluation. | Prevents `E.22` from supplying another evaluation's values. |
| `CC-E22-3` | If no read purpose is declared, the read SHALL be treated as `floorRead`. | Prevents false expectation of exceptional improvement. |
| `CC-E22-4` | `exceptionalImprovementRead` SHALL name the coordinates or active characteristic menu whose values may be raised. | Prevents vague "make it excellent" prompts. |
| `CC-E22-5` | `paretoTradeoffRead` SHALL name protected qualities or use the object-under-improvement evaluation's active protected coordinates. | Prevents Goodhart-style coordinate optimization. |
| `CC-E22-6` | `openQuestionDiscoveryRead` SHALL classify unasked questions as existing-coordinate issue, candidate coordinate or overlay, or outside object-under-improvement evaluation. | Prevents unbounded scope expansion. |
| `CC-E22-7` | `absorptionRead` SHALL record quality impact, not only accepted or applied disposition. | Makes returned review absorption improve the object rather than only close a checklist. |
| `CC-E22-8` | A quality-read frame SHALL state a non-use boundary when the result could be overread as project evidence, assurance, gate, release, certification, safety, compliance, work authority, general approval, checklist-count closure, or discharge-count closure. | Keeps neighbouring pattern authority intact and blocks checklist-count overread. |
| `CC-E22-9` | A reviewer SHALL NOT treat `floorRead` success as evidence that no exceptional improvement is possible. | Keeps admissibility separate from optimization. |
| `CC-E22-10` | A reviewer SHALL NOT treat `exceptionalImprovementRead` as permission to damage declared protected trade-offs. | Keeps improvement multi-coordinate and non-Goodhart. |
| `CC-E22-11` | A quality-read frame SHALL keep review-purpose declaration separate from the receiving quality result. | Prevents the prompt from becoming the quality read. |
| `CC-E22-12` | If the read purpose changes during review or absorption, the frame SHALL be updated or the extra result SHALL be marked outside the declared frame. | Keeps the answer replayable. |
| `CC-E22-13` | A quality-read frame SHALL be repaired before the object-under-improvement evaluation runs when it lacks object version, object-under-improvement evaluation, purpose or default, required protected trade-offs, required classification rule, or non-use boundary for an overread-prone result. | Makes frame sufficiency and lowering conditions testable. |
| `CC-E22-14` | A quality-read frame SHALL keep object kind and object-under-improvement evaluation distinct. Pattern reads use `E.21`; `DRR` reads use `E.9.DA`; other objects use their declared characteristic space, quality bundle, rubric, scale set, review profile, or exact FPF evaluation pattern. | Prevents unnecessary specialization while blocking unbounded "review anything" overread. |
| `CC-E22-15` | A quality-read frame SHALL NOT ask the reviewer to raise or lower values from popularity, adoption, prior use, absence of use, review count, reviewer praise, external-review completion, landing, release, or award-like signals. If such a signal matters, the frame SHALL require the object-under-improvement evaluation to rewrite it into object-content evidence or leave it outside the value read. | Prevents reputation medals from entering the question before the object-under-improvement evaluation runs. |
| `CC-E22-16` | Any actionable returned quality-review finding SHALL be represented as a stable `QualityReviewFindingRow` with row id, review locus, object locus, object-under-improvement evaluation effect, expected quality movement, correction direction, closure test, disposition, and discharge evidence when applied. | Prevents narrative findings from becoming uncheckable executor work. |
| `CC-E22-17` | Actionable quality-review findings SHALL be discharged row by row. One edit MAY close several rows, but each affected row SHALL still be revisited with a separate disposition, changed or unchanged object locus, and closure-test evidence. | Catches "I handled the group" and range-closure failures. |
| `CC-E22-18` | If a quality-read result becomes part of repeated improvement, the repeated method SHALL be governed by `E.23` rather than by extra loop doctrine inside `E.22`. | Keeps one-read question framing distinct from the quality-improvement method. |
| `CC-E22-19` | When the object version under quality read is OEE/NQD material, the quality-read frame SHALL name the exact candidate, front, archive, shortlist, parity report, refresh report, or declared transduction result; the governing pattern that carries its semantics; the read purpose; and the non-use boundary that keeps candidate quality, archive/front semantics, selected-set publication, parity, and refresh distinct. | Lets quality reads plug into OEE/NQD without turning `E.22` into generator, selector, archive, parity, or refresh doctrine. |
| `CC-E22-20` | If a read is expected to suggest what to do next, the frame SHALL say that the result is only a candidate improvement proposal or next-admissible-move hypothesis unless the exact neighbouring pattern is opened for decision, planning, work, gate, evidence, assurance, selected-set publication, parity, refresh, or pool-policy authority. | Preserves the pragmatic usefulness of reads without letting review language smuggle project claims beyond the quality-read frame. |
| CC-E22-21 | If a read is used before OEE/NQD candidate generation or candidate change, it SHALL state the object-under-improvement evaluation pressure, expected movement, protected trade-off, and closure test that make each candidate-change proposal worth generating. | Prevents exploration from degrading into unguided candidate changes while keeping generation, pool policy, selected-set publication, parity, and refresh in the governing patterns. |
| `CC-E22-22` | If a read returns a proposal portfolio, it SHALL state that proposal generation, NQD candidate generation, front or archive insertion, proposal selection, selected-set publication, parity, and refresh belong to exact neighbouring patterns rather than to `E.22`. | Lets a review produce useful alternatives without turning the read into an OEE/NQD selection or publication result. |

### E.22:8 - Common anti-patterns and repairs

| Anti-pattern | Failure | Repair |
|---|---|---|
| **"Review this" prompt.** | The reviewer chooses a purpose implicitly. | Add `QualityReadPurposeSelection` and the object-under-improvement evaluation. |
| **Blocker audit sold as improvement.** | The result only reaches the floor while the requester expected exceptional improvement. | Add `exceptionalImprovementRead` and per-coordinate improvement questions. |
| **Maximal rewrite sold as review.** | The result proposes broad optimization when only readiness was asked. | Narrow to `floorRead` or state the extra purpose explicitly. |
| **All-to-five Goodharting.** | Visible values rise while ordinary use, affordability, locality, or corpus ecology falls. | Add `paretoTradeoffRead` and protected trade-offs. |
| **Open-question silence.** | The reviewer answers the given checklist but misses a missing governing question. | Add `openQuestionDiscoveryRead` and a classification rule. |
| **Applied-count absorption.** | Absorption reports how many suggestions were applied but not what quality changed. | Add `absorptionRead` and impact classification. |
| **Checklist-count quality closure.** | A discharge table says every row is closed, and that count is treated as the quality result. | Run or cite the object-under-improvement evaluation on the changed object; keep row discharge as executor evidence, not quality closure. |
| **Full-loop capture.** | `E.22` starts governing repeated improvement, method-family selection, or stop or switch decisions across passes. | Use `E.22` only to frame each quality read; use `E.23` for the repeated quality-improvement method. |
| **Object-under-improvement evaluation theft.** | The frame starts defining coordinates that belong to `E.21`, `E.9.DA`, `C.16`, `C.25`, a local rubric, or another object-under-improvement evaluation. | Keep `E.22` to purpose declaration; run the exact object-under-improvement evaluation for the read. |
| **Portfolio-quality blur.** | A request asks whether "the portfolio is good" while mixing candidate quality, front/archive semantics, selected-set publication, parity, and refresh. | Name the exact object version under quality read and the governing pattern: `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, or `G.11`; keep `E.22` to the read purpose and non-use boundary. |
| **Recommendation smuggled as reading.** | A read result says what to do next as if it had already decided, planned, approved, or scheduled the move. | Keep the result as a candidate improvement proposal or next-admissible-move hypothesis, or open `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, `B.3`, `G.5`, `G.9`, or `G.11` for the claim that exceeds the quality-read frame. |
| **Unguided candidate change dressed as exploration.** | Candidate material is changed or generated without saying what object-under-improvement evaluation movement the change is meant to test. | Run candidateImprovementProposalRead; state expected movement, affected locus, protected trade-offs, closure test, and OEE/NQD neighbour exit before generation or candidate change. |
| **Single-improvement narrowing.** | The read chooses one improvement when the live request needs a proposal portfolio for NQD comparison or OEE exploration. | Return bounded proposal rows and hand generation, selection, front or archive handling, selected-set publication, parity, and refresh to `C.18`, `C.19`, `G.5`, `G.9`, or `G.11`. |
| **Reputation-medal prompt.** | The request asks the reviewer to score higher because the object is popular, reviewed, landed, awarded, or already used, or lower because it is new and unused. | Rewrite the signal into an exact content-evidence question governed by the object-under-improvement evaluation, or exclude it from the quality value. |

### E.22:9 - Consequences

| Consequence | Benefit | Cost or guard |
|---|---|---|
| Review requests become typed before review starts. | Fewer wrong-answer reviews. | Use the short form for ordinary floor reads. |
| Exceptional improvement becomes an explicit request. | Reviewers can propose higher-value non-dominated edits under the object-under-improvement evaluation rather than stopping at blockers. | The request must also state protected trade-offs. |
| Candidate-change proposals become evaluation-shaped. | Improvement loops and OEE/NQD exploration can generate a proposal portfolio for a reason rather than by unguided candidate changes. | `E.22` must still hand generation, pool policy, front or archive handling, selected-set publication, parity, and refresh to the exact neighbour. |
| Absorption becomes quality-aware. | Returned review follow-up says what improved, not only what was applied. | The impact account should be compact and tied to the object-under-improvement evaluation. |
| Open questions become visible. | Missing questions can improve the object-under-improvement evaluation itself or move to another exact object-under-improvement evaluation. | Open-question discovery must not become unbounded campaign planning. |
| Goodhart risk is checked at the prompt boundary. | Improvement requests carry usability, affordability, locality, corpus ecology, and neighbour-fit protections from the start. | Some plausible "improvements" will be rejected or narrowed. |

### E.22:10 - Rationale

Feedback and review improve an object only when the desired condition, current condition, and next action are distinguishable. If the requested desired condition is merely "acceptable", the reviewer should not be expected to design the best feasible version. If the requested desired condition is "exceptional where feasible", a floor-only blocker pass is under-scoped.

There is no neutral "just read this" in an FPF quality context. The local act in this pattern is an improvement-oriented quality read under a named object-under-improvement evaluation. The frame states what the reader is reading for, and the result states what the object-under-improvement evaluation saw, which candidate improvement proposal follows from that read, and which next admissible move remains only a hypothesis unless another exact pattern receives it.

This is also why `E.22` connects naturally to `E.23` and OEE/NQD. Improvement loops need proposals before changes; OEE/NQD often needs a bounded proposal portfolio before generation, candidate-pool policy, front or archive insertion, selected-set publication, parity, and refresh. `E.22` supplies the evaluative proposal shape. It does not govern the repeated loop, candidate generator, pool policy, selector result, parity result, or refresh plan.

`GQM` discipline gives the same lesson for measurement: questions must follow from the goal. A quality read whose goal is not declared will answer the reviewer's implicit question rather than the requester's intended question.

Multi-coordinate and multi-scale evaluations also need trade-off control. Raising one coordinate can harm another, and a scalar or hidden total order can hide that loss. Therefore `exceptionalImprovementRead` is paired with `paretoTradeoffRead` whenever the proposed changes may affect protected qualities.

`E.22` is deliberately small. It does not define quality coordinates, scales, rubrics, review profiles, OEE/NQD archive semantics, selector results, parity reports, refresh plans, decisions, or work plans. It makes the question to the object-under-improvement evaluation explicit enough that the object-under-improvement evaluation can produce the right kind of answer and the next admissible move can be assigned without overclaim.

### E.22:11 - SoTA-Echoing

`E.22:11` uses `SoTA` in the E.8 sense: current best-known problem-solving practice for the governed problem. A row may mention older lineage only to name the inherited invariant that current practice still uses; lineage does not carry SoTA by itself. Current references are used only for the local read-framing problem named in the row.

| Claim | Current SoTA anchor and retained lineage | Local adoption | Non-use boundary |
|---|---|---|---|
| Quality reads need multidimensional, diagnostic, actionable movement rather than one overall judgement. | Current anchors: `LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts` (ACL 2024), `Human-aligned long-form evaluation (HALF-Eval): Framework for assessing AI-generated content and improvement` (2025), and `RubricEval: A Rubric-Level Meta-Evaluation Benchmark for LLM Judges in Instruction Following` (`arXiv:2603.25133`, 2026) treat rubric quality, multidimensional evaluation, calibration, meta-evaluation, and actionable feedback as live evaluation problems rather than as one score. | `QualityReviewFindingRow`, object-under-improvement evaluation effects, and `absorptionRead` make returned findings name expected quality movement, correction direction, closure test, and discharge evidence; absorption reports quality impact, not only applied or not-applied disposition. | This does not make `E.22` an automated evaluator, LLM judge, benchmark harness, or content-scoring method. |
| Feedback must connect desired condition, current condition, and next action. | Current anchors: `Can LLM feedback enhance review quality? A randomized study of 20K reviews at ICLR 2025` (`arXiv:2504.09737`, Review Feedback Agent) and `FeedEval: Pedagogically Aligned Evaluation of LLM-Generated Essay Feedback` (`arXiv:2601.04574`, ACL ARR 2026 January submission) retain specificity, actionability, validity, and improvement guidance as live quality dimensions. Retained lineage: Hattie and Timperley plus Sadler for the desired-condition, current-condition, and next-action invariant. | `QualityReadQuestionFrame` names purpose, floor or desired improvement aim, expected result form, and first repair or improvement result before the object-under-improvement evaluation reads values. | This does not turn FPF reviews into educational assessment or require a teaching cycle for every small edit. |
| Evaluation questions must be derived from the declared purpose; otherwise values answer the wrong question. | Current anchors: `LLM-Rubric` (ACL 2024), `RUBICON: Rubric-based Evaluation of Domain-Specific Human-AI Conversations` (2024), `HALF-Eval` (2025), and `RubricEval` (`arXiv:2603.25133`, 2026) make task-domain-specific criteria and rubric-level validity live evaluation concerns. Retained lineage: GQM and GQM+Strategies for deriving questions and measures from goals. | `QualityReadPurposeSelection` precedes coordinate reading; a reviewer cannot infer exceptional-improvement questions from a bare "review this" prompt, and a value result is inadmissible when the question belongs to a different object-under-improvement evaluation. | This does not import software-measurement programs, numeric measures, or a GQM document set into ordinary quality reads. |
| Multi-criteria improvement needs explicit trade-offs and non-dominated alternatives. | Current anchors: `The Architecture Tradeoff and Risk Analysis Framework (ATRAF): A Unified Approach for Evaluating Software Architectures, Reference Architectures, and Architectural Frameworks` (`arXiv:2505.00688`, 2025) and `Multi-criteria design methods in facade engineering: State-of-the-art and future trends` (2024) continue the quality-attribute trade-off line for systems and architecture evaluation. Retained lineage: MCDA, Pareto-front reasoning, and ATAM for explicit trade-off points. | `paretoTradeoffRead`, `TradeoffProtectionSet`, protected qualities, and non-dominated improvement wording keep quality improvement from collapsing into one score or one forced winner. | This does not require formal optimization, utility functions, quantitative MCDA, or an architecture-evaluation method for ordinary FPF review. |
| Proxy optimization can make the intended value worse even when visible values improve. | Current anchors: `Goodhart's Law in Reinforcement Learning` (ICLR 2024), current catastrophic-Goodhart reward-misspecification work (NeurIPS 2024), and `RubricEval` (`arXiv:2603.25133`, 2026) show that optimizing a proxy, reward, or weak rubric can degrade the intended value. Retained lineage: Manheim and Garrabrant's Goodhart taxonomy. | `paretoTradeoffRead`, protected qualities, `CC-E22-10`, and `CC-E22-15` require the read to ask what became worse before stopping, especially when visible coordinates, popularity, adoption, review count, or discharge count could be mistaken for quality. | This does not make `E.22` a predictive model of Goodhart mechanisms, adoption model, or AI safety evaluation. |
| OEE/NQD and improvement loops need proposal-shaped candidate changes before generation or candidate change. | Current QD anchor: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026). Retained lineage: OEE/QD archive and front practice, plus feedback-as-next-action review traditions. | `candidateImprovementProposalRead` can return one proposed candidate change or a bounded proposal portfolio. Each row names object-under-improvement evaluation pressure, expected movement, affected locus, protected trade-off, closure test, and neighbour exit before `E.23`, `C.18`, `C.19`, `G.5`, `G.9`, or `G.11` consumes it. | This does not make `E.22` a candidate generator, candidate-change policy, selected-set publisher, parity harness, or refresh orchestrator. |
### E.22:12 - Relations

| Pattern | Relation |
|---|---|
| `E.21` | Receives FPF pattern-quality reads. `E.22` frames whether the `E.21` read is floor-only, exceptional-improvement, trade-off, candidate improvement proposal, open-question, absorption, or a declared combination. |
| `E.9.DA` | Receives `DRR` decision-adequacy reads. `E.22` frames whether the read only tests drafting adequacy or also asks for exceptional decision-adequacy improvement, trade-off control, and candidate improvement proposals. |
| `E.19` | Runs admission and refresh review profiles. `E.22` frames the review question so `E.19` does not silently replace exceptional improvement with blocker review or vice versa. |
| `E.23` | Governs repeated quality-improvement loops. `E.22` frames each improvement-oriented quality read inside the loop and can return candidate improvement proposals; `E.23` governs absorption across passes, object-under-improvement evaluation re-read of changed object versions, method-family selection, and stop, narrow, continue, switch method, or hold decisions. |
| `E.10`, `A.6.P`, `C.2.P`, `F.18` | Repair load-bearing wording and names introduced by the quality-read frame. `E.22` uses those patterns when its local terms become load-bearing outside the frame. |
| `C.16`, `A.17`, `A.18`, `A.19`, `C.25` | Govern characteristics, scales, coordinates, measurements, characteristic spaces, and quality bundles for many quality-bearing objects. `E.22` does not create a new measurement space; it points to the declared object-under-improvement evaluation. |
| `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Receive OEE/NQD quality-read frames when the object version under quality read is a generated candidate, `Front`, `Q-Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, parity report, refresh report, or declared transduction result. `E.22` frames the read purpose and candidate improvement proposal shape, including bounded proposal portfolios; those patterns govern candidate characteristics, generation, archive and front semantics, pool policy, selected-set publication, parity, and refresh. |
| `A.10`, `B.3`, `A.20`, `A.21`, `A.15` | Govern evidence, assurance, local CV status, gates, and work when a quality result is reused for project-side claims. `E.22` must block that overread or name the exact object-under-improvement evaluation or neighbouring pattern. |
| `J.4` | Provides compact entry guidance when the first question is "which quality-read purpose am I actually asking for?" |

### E.22:End

