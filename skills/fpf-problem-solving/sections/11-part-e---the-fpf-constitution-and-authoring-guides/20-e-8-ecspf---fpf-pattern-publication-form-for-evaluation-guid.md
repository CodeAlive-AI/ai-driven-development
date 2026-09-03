## E.8.ECSPF - FPF Pattern Publication Form for Evaluation Guidance

> **Type:** Authoring method pattern
> **Status:** Stable
> **Normativity:** Normative

### E.8.ECSPF:1 - Problem frame

Use this pattern when an accepted `EvaluationCharacteristicSpaceSpec` constructed or repaired under `A.19.ECS` has been selected for durable FPF publication, and an author must turn it into a practitioner-facing pattern. The question is not "what values should this object be judged by?" but "how should the pattern teach this evaluation so its values remain usable, reviewable, and bounded?"

`A.19.ECS` guides an author in constructing or repairing the evaluation characteristic-space specification: evaluated object kind and, when needed, the object version; declared use, working reader, qualification window, contrast cases, object-kind-fit rule, coordinate and scale bindings, value meanings and preferred movement, evidence and missingness rules, result-row shape, adjacent-value rationales, calibration points, any triggered coordinate payload, protected trade-offs, any declared comparison rule, status meanings, neighbouring-pattern exits, and stop, reopen, `E.22`, and `E.23` conditions. `E.8` supplies the ordinary FPF authoring form. `E.8.ECSPF` tells the author how to carry the accepted specification into that form. The specification, its `CharacteristicSpace`, the authored pattern content, a later evaluation of an object, and the result of that evaluation remain different things.

**Not this pattern when.** Use `A.19.ECS` when the characteristic-space specification itself is missing or inadequate. Use `E.8` when the pattern is not an evaluation-characteristic-space pattern. Use `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, or a project-local evaluation when one already supplies the value meanings for the evaluated object and use. Use `E.22` to frame one quality evaluation and `E.23` to run repeated improvement. Use a local rubric, table, or project rule instead of an FPF pattern when the evaluation is not intended for durable FPF reuse.

**First useful move.** Start from the accepted `A.19.ECS` specification. Before presenting coordinate tables or conformance rows, name the evaluated object kind, declared use, working reader, qualification window, and first action-guiding evaluation use in the pattern's recognition text.

**FPF-publication boundary.** If the evaluation is local, temporary, or project-specific, do not publish an FPF pattern. Keep the `A.19.ECS` specification in the local publication form and cite the FPF neighbouring patterns named by value it uses.

**What goes wrong if missed.** The pattern, the accepted specification, the evaluation, and its result collapse into one supposed object. The pattern then becomes a score sheet, review form, checklist, or taxonomy. The coordinate table appears before the working situation. Readers can see values but cannot tell when to use them, what to do after an evaluation result, which objects are outside the declared evaluated-object kind, or which neighbouring pattern supplies the needed evidence, assurance, gate, work, decision, naming, measurement, or improvement guidance.

**What this buys.** `E.8.ECSPF` lets an author publish evaluation guidance as a real pattern: practitioner-readable first, exact enough for review, and bounded enough for a later evaluator to use with the framing guidance in `E.22` or the repeated-improvement guidance in `E.23`.

**Primary EntityOfConcern in plain terms.** The primary EntityOfConcern is the authored FPF pattern content and its publication form for one accepted evaluation characteristic-space specification.

**Primary working reader.** The first reader is an FPF author or reviewer turning an accepted evaluation characteristic-space specification into a reusable FPF pattern for later practitioners, managers, and stewards.

### E.8.ECSPF:2 - Problem

An author can use `A.19.ECS` to produce a good evaluation characteristic-space specification without yet having guidance on publishing that specification as an FPF pattern. The author can use `E.8` to produce a good generic FPF pattern without yet having guidance on where to place a coordinate set, object-kind-fit rule, evidence basis, result-row shape, calibration points, status set, and stop condition when they are the pattern's main content.

Recurring failures:

1. **Publication-form/content collapse.** The accepted specification, its `CharacteristicSpace`, the authored pattern, a later evaluation, and the evaluation result are treated as one object.
2. **Table-first pattern.** Coordinate rows arrive before evaluated object kind, use, first move, FPF-publication boundary, and object-kind boundary.
3. **Checklist substitution.** Conformance rows replace the `Solution` instead of checking a readable evaluation method.
4. **Underpublished values.** Coordinate names are present, but reader or qualification limits, value meanings, missingness, polarity, protected trade-offs, comparison rule, status meanings, neighbouring exits, or stop and reopen conditions are missing.
5. **Wrong-kind examples.** Worked cases show only passing examples, so the pattern cannot teach below-floor and outside-declared-object-kind boundary outcomes.
6. **Neighbour theft.** Claims about evidence, assurance, gates, work, decisions, naming, measurement, OEE or NQD, or mathematical lenses are carried as if this evaluation-characteristic-space pattern defined or justified them.
7. **Pattern-quality confusion.** The author uses `E.21` to judge whether the FPF pattern version is good, but forgets that the new pattern must still carry the accepted evaluation characteristic-space specification for one evaluated object kind by value.
8. **Quality-carrier leakage.** `E.21` values, corpus projection, README/ToC/E.11/I.2 alignment, retrieval, cold-reader evidence, monolith parity, landing evidence, or developer/reviewer/executor correspondence for the publication form are written into the evaluation pattern as if they were the evaluated object's method.

### E.8.ECSPF:3 - Forces

| Force | Tension |
|---|---|
| **Recognition first vs coordinate completeness** | An evaluation-characteristic-space pattern needs tables, but the reader must first see the working situation and first evaluation use. |
| **Generic E.8 form vs evaluation content** | The canonical pattern skeleton stays fixed, but the evaluation has special content fields from `A.19.ECS`. |
| **Reusable FPF pattern vs local evaluation** | FPF publication is useful only when the evaluation is durable and reusable beyond one local project. |
| **Values named by value vs checklist feel** | Values and statuses must be named by value without making the pattern feel like an administrative form. |
| **Related-pattern statements vs second ontology** | For each outside claim, the pattern must state the concrete contribution it uses from neighbouring content, without forcing every contribution into one verb list or becoming a directory of possibly related patterns. |
| **Evaluation of object vs evaluation of FPF pattern version** | The evaluation judges its evaluated object; `E.21` may separately evaluate whether the authored FPF pattern publication form is good enough. |

### E.8.ECSPF:4 - Solution

When an accepted `A.19.ECS` specification is selected for durable FPF publication, use `E.8` to write a pattern that teaches the specified evaluation, with these additional placement rules:

1. **Keep the objects separate.** The accepted specification says what the evaluation requires. The publication form arranges the pattern. The authored content teaches a later practitioner how to evaluate an object. That later evaluation produces a result. Neither the specification nor its `CharacteristicSpace`, the evaluation, the evaluated object, or the result becomes the pattern.
2. **Put recognition before coordinates.** The opening text names evaluated object kind, declared use, working reader, qualification window, first evaluation use, FPF-publication boundary, what goes wrong, and what the pattern buys before any dense table.
3. **Carry the complete accepted specification by value.** Put every required value, and every optional value whose trigger holds, where a practitioner needs it. Do not discharge this move by citing `A.19.ECS`, copying field names, or pointing to an author-only record. The `Solution` and its nearby practitioner-use sections carry the actual selected values from the accepted specification.
4. **Use worked slices as the discriminating-case test.** Archetypal Grounding and worked cases include a passing evaluated object, a below-floor evaluated object, and an outside-declared-object-kind boundary case.
5. **Keep ordinal coordinates separate and protect against proxy improvement.** Do not create an undeclared total, average, or “overall score” from ordinal coordinates. Whenever a visible value improves, ask whether any intended value or protected trade-off became worse. If the published guidance would reward that loss, stop the comparison and reopen the specification. If a bounded use genuinely needs scalarization, name the particular method, its use, the information it loses, and its applicability and stop or return conditions; do not present that scalar as “the evaluation”.
6. **Keep checklist rows secondary.** Conformance checks verify that the evaluation is recoverable and usable. They do not become the user's method.
7. **State the concrete contribution used for each outside claim.** When `Relations` or a grounded local boundary makes a claim about, for example, evidence, assurance, work, naming, measurement, or improvement, cite the applicable `PatternID` and say in ordinary terms what its content contributes here. It may supply an evidence-use boundary, an assurance calculus, a gate decision rule, a measurement test, repair guidance, or something else; these are examples, not a closed vocabulary. The `PatternID` is enough for ordinary use. Name a particular assertion, episteme edition, or `ClaimGraph` only when interpretation, migration, conflict, publication, or reuse depends on that identity. Treat guidance as a `U.Method`, a qualifying `U.MethodDescription`, or a particular Method use only after its own admission test passes and the current claim needs that identity. Use `F.19` for ordinary wording repair. When a repair can change an FPF-governed meaning, confirm that the evaluated object and its kind, relation or claim kind, live ontic slot, relation position, use relation, admissible use, and scope remain recoverable before and after the repair, as applicable to the changed claim.
8. **Evaluate the authored pattern with `E.21`.** When the FPF pattern is under quality improvement, a reviewer uses `E.21` to evaluate that pattern version. A later evaluator uses the guidance published in the pattern to evaluate the declared object kind. The `E.21` result, corpus-projection evidence, README/ToC/E.11/I.2 alignment, retrieval or cold-reader evidence, monolith parity, landing evidence, and developer/reviewer/executor correspondence stay in the quality, review, projection, or release carriers unless the pattern's own `EntityOfConcern` and user-facing action are that evaluation or projection work.

The authoring flow and the quality-improvement flow are different. First an author carries an accepted specification into a pattern. Later a practitioner may use that pattern's guidance to evaluate an object and record a result. `E.22` and `E.23` provide guidance for framing or repeating that work. A reviewer's later `E.21` evaluation of this pattern is evidence about the authored pattern, not part of the object evaluation that the pattern teaches. That evidence may cause edits to recognition text, coordinates, cases, or boundaries, but it remains outside the pattern unless rewritten as user-facing evaluation guidance.

#### E.8.ECSPF:4.1 - Canonical placement table

| E.8 section | Evaluation-specific content |
|---|---|
| `Problem frame` | Evaluated object kind, declared use, working reader, qualification window, first useful evaluation use, FPF-publication boundary, what goes wrong without this evaluation, and what practical move the evaluation enables. |
| `Problem` | Failure modes that the evaluation prevents: wrong-kind scoring, hidden value drift, proxy value, one-score collapse, missingness confusion, or neighbour theft. |
| `Forces` | Tensions among reuse, coordinate count, readability, measurement admissibility, trade-off protection, local stop, and open-ended improvement. |
| `Solution` | Every required accepted-specification value and every triggered optional value: object and use, reader and qualification limits, cases and kind-fit, coordinate and scale bindings, value meanings and preferred movement, evidence and missingness, result form and calibration, coordinate-specific evidence, trade-offs and comparison, statuses, exits, and stop or reopen conditions. |
| `Archetypal Grounding` | At least one passing evaluated object, one below-floor evaluated object, and one outside-declared-object-kind boundary case. |
| `Bias-Annotation` | Known skew in source examples, reader family, domain tradition, measurement preference, benchmark preference, or FPF-internal reuse. |
| `Conformance Checklist` | Checks that the specification is recoverable, not that a reviewer likes the evaluated object. |
| `Common Anti-Patterns` | Score-sheet pattern, checklist-as-solution, table-first recognition failure, neighbour theft, one total score, hidden value drift. |
| `Consequences` | What changes in practice after a conforming evaluation use, its scope, next action, stop or reopen, and the concrete contribution supplied by neighbouring content for any outside claim. Add a denied consequence only when a plausible intended reader has an independent reason to infer it. |
| `Rationale` | Why this coordinate set and publication-form are selected, including relation to `A.19.ECS` and existing evaluations named by value. |
| `SoTA-Echoing` | Current practice that changes evaluated-object selection, coordinate choice, value meaning, missingness, comparison, or stop discipline. |
| `Relations` | `A.19.ECS`, `E.8`, `E.21`, `E.22`, `E.23`, and exact domain or neighbour patterns. |

#### E.8.ECSPF:4.2 - Local names and kind settlement

| Local name | Function | Non-use boundary |
|---|---|---|
| `AcceptedEvaluationCharacteristicSpaceSpec` | The accepted `A.19.ECS` specification selected for publication. | Not the pattern, the later evaluation, or its result. |
| `EvaluationPatternPublicationForm` | The `E.8` arrangement used to publish the guidance as an FPF pattern. | Not the accepted specification or the authored words, tables, and cases. |
| `AuthoredEvaluationPatternContent` | The recognition text, solution, value meanings, cases, result form, and boundaries through which the pattern teaches the evaluation. | Not an occurrence of evaluation work and not its result. |
| `LaterEvaluationUse` | A later practitioner judges an object using the published guidance and records a result. | Establish a particular `MethodDescription`, `Method`, assignment, or dated `Work` only when that identity matters to the receiving claim. |
| `EvaluationResult` | The coordinate rows, evidence, rationales, and status produced by that later evaluation. | Not the pattern and not the accepted specification. |
| `RecognitionEvaluationUseLine` | Early line saying what object is evaluated, for which use, and what the first admissible evaluation use does. | Not a slogan or pattern-title paraphrase. |
| `DiscriminatingCaseBank` | Passing, below-floor, and outside-declared-object-kind boundary worked slices. | Not only positive examples. |
| `RelatedPatternRelationBlock` | Statements of outside claims, each with the applicable pattern id and its concrete contribution in this use. | Not a general directory, a closed relation-verb vocabulary, or a list of presumed Methods. |
| `EvaluationResultFormBlock` | Published result-form discipline for this evaluation: required row fields, evidence basis, short rationale rule, and any coordinate-specific payload. | Not a review report, project status, or optional appendix. |
| `CalibrationAndPayloadBlock` | Published adjacent-value calibration points and payload rules for values that need comparator, source-currentness, corpus-projection, worked-case, or retrieval evidence. | Not extra bureaucracy and not a second score system. |
| `PatternVersionQualityEvaluation` | Optional `E.21` evaluation over the authored pattern publication form. | Not a replacement for the evaluation for one evaluated object kind and not publication-form method content. |

#### E.8.ECSPF:4.3 - By-value carry-through

Carry the accepted specification through the pattern in practitioner order. “By value” means that the reader can find the actual selected value and use it; a field name, an `A.19.ECS` citation, or an author-only attachment is not enough.

| Practitioner need | Accepted values that must be present |
|---|---|
| Recognize whether to enter | `EvaluatedObjectKindRef`, `DeclaredUseScope`, `WorkingReaderScope`, `QualificationWindow`, and `ObjectVersionUnderImprovementRef` when the evaluation is tied to one object version. |
| Test the boundary | `DiscriminatingCaseSet` and `ObjectKindFitRule`, including admissible, below-floor, and outside-kind outcomes. |
| Judge the object | `CharacteristicSlotSet`, `ScaleBindingSet`, `PolarityAndPreferredMovement`, and `FloorAndExceptionalMeaningSet`, with the actual coordinate and value meanings rather than their field labels. |
| Justify and record a result | `EvaluationEvidenceBasisRule`, `EvidenceAndMissingnessRule`, `ResultRowShape`, `AdjacentValueRationaleRule`, `CalibrationPointSet`, and `CoordinateSpecificEvidencePayloadRule` whenever a coordinate triggers such a payload. |
| Protect a useful result from false improvement | `ProtectedTradeoffSet` and `DominanceOrComparisonRule` whenever the accepted specification declares a comparison rule. |
| Continue, stop, or leave this evaluation | `StatusValueSet`, `StopOrReopenCondition`, `NeighborPatternExitSet`, `E22QuestionFrameUse` when selected, and `E23StartCondition`. |

The fields may be expressed in plain language, tables, or worked cases. Keep them close to the practitioner action they qualify. Do not hide required values in conformance rows, source notes, or review evidence.

### E.8.ECSPF:5 - Archetypal Grounding

**Tell.** Guidance based on an evaluation `CharacteristicSpace` becomes reusable in FPF only when a practitioner can recognize the evaluated object and use before reading the coordinate table. The publication form must teach the evaluation use, not merely list the values. The following slice shows the author's move from an accepted specification to practitioner-facing content.

**Accepted specification.** An author has an accepted `EvaluationCharacteristicSpaceSpec` for one version of a field-service handover instruction.

| Accepted value | Selected content |
|---|---|
| Evaluated object and use | One field-service handover instruction version, judged for readiness for a supervised first use. |
| Working reader and qualification window | A maintenance lead who did not author the instruction; the result remains qualified only while the named equipment configuration and safety-procedure edition remain unchanged. |
| Discriminating cases | A usable handover instruction; an instruction of the same kind that hides its stop condition; and a spare-parts catalogue, which is outside the evaluated object kind. |
| `FirstMoveRecoverability` | `0`: the first move cannot be found; `1`: it can be recovered only with author help or an undeclared source; `2`: the working reader can state and carry out the first move from the instruction. |
| `HazardBoundaryVisibility` | `0`: the hazard or stop boundary is absent; `1`: it is recoverable only by chasing another source; `2`: it appears before the first move and says when to stop or escalate. |
| Evidence and missingness | Observe one cold-reader trial and cite the instruction locus used for each value. An unchecked coordinate is `missing` and cannot be treated as `2`. |
| Result and trade-off | Each row contains coordinate, value, adjacent-value rationale, evidence locus, and missingness. Improving first-move wording must not hide or weaken the hazard boundary. |
| Status and stop | `ready for supervised use` requires `2` on both coordinates with current evidence. Otherwise return `repair`. Reopen after an equipment-configuration or safety-procedure change. |

**Corresponding recognition lines in the authored pattern.**

> Use this pattern when you must decide whether a field-service handover instruction is ready for a supervised first use by a maintenance lead who did not write it. Use it only for the named equipment configuration and safety-procedure edition. First give the current instruction to that reader and ask them to identify the first move and the condition that requires stopping or escalation. A spare-parts catalogue is outside this evaluation.

These lines carry the selected object kind, use, reader, qualification window, first move, and wrong-kind boundary. Merely writing “see `A.19.ECS`” would not.

**Minimal Solution and result form.** The pattern then tells the practitioner to use the current instruction version, observe the cold-reader trial, judge both coordinates from their stated value meanings, and record both rows. For example:

| Coordinate | Value | Adjacent-value rationale | Evidence locus | Missingness |
|---|---:|---|---|---|
| `FirstMoveRecoverability` | `2` | `1` would understate independent recovery; no higher value exists. | Opening instruction and observed first move. | checked |
| `HazardBoundaryVisibility` | `1` | `0` would ignore the recoverable safety reference; `2` would overstate visibility before action. | Safety reference after the first action. | checked |

The returned status is `repair`, because one coordinate remains below its declared ready value. If both checked rows were `2`, the instruction would reach `ready for supervised use`; a spare-parts catalogue would return to evaluation selection before these rows were opened. A simple `A.10` citation is enough to locate the evidence-use discipline for this ordinary case; a particular assertion or `ClaimGraph` is needed only if later interpretation or reuse depends on that identity.

**Near miss, proxy improvement.** An editor shortens the instruction so the first move is easier to find, but deletes the visible stop condition. `FirstMoveRecoverability` rises to `2` while `HazardBoundaryVisibility` falls to `0`. The author must not add or average those ordinal values and call the rewrite better. The protected safety trade-off has been lost, so the pattern returns `repair` and the accepted specification must be reopened if its current status rule would reward that rewrite.

**Show, pattern-quality evaluation.** `E.21` is an evaluation for one FPF pattern version. Its publication form must still open with the working question "is this pattern good enough for the declared use?" before showing coordinates such as first-action recoverability, boundary fit, and SoTA binding.

**Show, local rubric that should not become an FPF pattern.** A project team defines a temporary rubric for choosing a meeting room. The `A.19.ECS` specification may be adequate locally, but no durable FPF pattern is needed because the evaluated object kind and use do not recur across FPF practice.

**Show, object-kind boundary.** A nuclear-plant evaluation can judge nuclear plants and declared comparable power-generation alternatives. A plant inspection report can supply evidence about the plant but is outside that evaluated-object kind: before the evaluation is opened, select a suitable evaluation; after a forced invocation, record an object-kind-fit defect/value rather than treating it as a weak nuclear plant or skipping declared coordinates. The pattern publication form must show that boundary before readers try to use the coordinate table.

### E.8.ECSPF:6 - Bias-Annotation

Evaluation-characteristic-space patterns are vulnerable to domain-example bias: the first examples can silently choose the evaluated object kind, use, and value family for later readers. A conforming publication form names known skew in examples, sources, reader family, domain tradition, measurement preference, benchmark preference, or FPF-internal reuse. When the evaluation claims broad use, the case bank must include heterogeneous evaluated object situations or explicitly narrow the claim.

### E.8.ECSPF:7 - Conformance Checklist

| Check | Requirement | Why |
|---|---|---|
| `CC-E8ECSPF-1` | The pattern SHALL carry every required value from the accepted `EvaluationCharacteristicSpaceSpec` and every optional value whose trigger holds, including reader scope, qualification window, neighbouring exits, and the applicable `E.22` and `E.23` conditions. A citation or field-name list alone does not satisfy this requirement. | Prevents loss between the accepted specification and practitioner-facing content. |
| `CC-E8ECSPF-2` | Recognition text SHALL state evaluated object kind, declared use, working reader, qualification window, first evaluation use, FPF-publication boundary, and object-kind boundary before dense coordinate tables. | Keeps the pattern usable before it becomes reviewable. |
| `CC-E8ECSPF-3` | The `Solution` SHALL carry the accepted specification's values rather than leaving them only in conformance rows, SoTA rows, or examples. | Prevents checklist substitution. |
| `CC-E8ECSPF-4` | Worked cases SHALL include passing, below-floor, and outside-declared-object-kind boundary outcomes. | Tests evaluated-object-kind discrimination. |
| `CC-E8ECSPF-5` | Each coordinate SHALL state value meanings, polarity or no-simple-direction value rule, missingness rule, and protected trade-off when applicable to the declared evaluation use. | Makes evaluation uses repeatable and bounded. |
| `CC-E8ECSPF-5a` | The publication form SHALL prohibit an undeclared total or average over ordinal coordinates. Any admitted scalarization SHALL name its method, declared use, information loss, applicability, and stop or return condition. | Prevents a convenient number from replacing the evaluation. |
| `CC-E8ECSPF-5b` | When one visible value improves, the evaluation use SHALL check whether an intended value or protected trade-off worsened and SHALL stop or reopen when the evaluation would reward that loss. | Blocks proxy improvement and Goodhart-style degradation. |
| `CC-E8ECSPF-6` | When the publication form makes an outside claim, `Relations` SHALL cite the applicable `PatternID` and state its concrete contribution in ordinary language. The contribution is not limited to a fixed verb list. A pattern citation SHALL NOT be retyped as a Method or MethodDescription. Simple relations stay free of phrase apparatus, and architecture-placement reasoning stays out of publication-form evaluation prose. | Prevents a second ontology or apparatus-overwrapped publication form. |
| `CC-E8ECSPF-6a` | Wording, naming, or precision-restoration repairs SHALL follow `F.19`. When a repair can change an FPF-governed meaning, it SHALL check the evaluated object and its kind, relation or claim kind, live ontic slot, relation position, use relation, admissible use, and scope before and after the repair, as applicable to the changed claim. For a claim outside this pattern, cite the applicable pattern id and state its concrete contribution. Require a particular assertion, episteme edition, `ClaimGraph`, `U.Method`, qualifying `U.MethodDescription`, or Method use only when its admission test passes and the receiving claim depends on that identity. | Prevents evaluation patterns from inheriting lexical cleanup as ontology drift or locator use as formal identity. |
| `CC-E8ECSPF-7` | If the authored publication form is under improvement, `E.21` SHALL evaluate FPF pattern-version quality separately from the evaluation's evaluated object result. | Keeps pattern quality distinct from evaluated object quality. |
| `CC-E8ECSPF-8` | An author SHALL not turn a local, temporary, or one-project evaluation specification into an FPF pattern unless its reuse scope is durable and the patterns used for outside claims are named with their concrete contributions. | Blocks needless pattern growth. |
| `CC-E8ECSPF-9` | The publication form SHALL state what would lower, reopen, or retire the accepted specification or the guidance that carries it: changed object kind or object version, changed use, reader, or qualification window, changed use of a cited source, changed source adoption, adaptation, or rejection decision, missing contrast case, coordinate-value drift, missingness or comparison-rule change, or a correction to an exit or outside claim. | Makes maintenance of the pattern testable. |
| `CC-E8ECSPF-10` | The publication form SHALL state the required result row shape and evidence basis. If values need external, comparator, projection, worked-case, or currentness evidence, the result form SHALL require that evidence by value or lower the coordinate. | Prevents the pattern from accepting prose impressions or two-column value lists as evaluation results. |
| `CC-E8ECSPF-11` | A reusable pattern that teaches an evaluation SHALL publish calibration points for common adjacent-value disagreements and any coordinate-specific evidence payload needed to reach floor or exceptional values. | Makes the same evaluation guidance usable by more than one evaluator. |
| `CC-E8ECSPF-12` | The publication form SHALL keep `E.21` values, `PatternQualityStatus`, corpus-projection evidence, README, ToC, E.11, and I.2 alignment, card or retrieval evidence, cold-reader evidence, monolith parity, landing evidence, Developer, Reviewer, and Executor correspondence, and other quality-carrier facts out of the pattern. These facts belong in the `E.21` result, `E.19` run record, README, ToC, E.11, or I.2, card, retrieval, or projection carrier, or release or landing evidence carrier unless the content-use test shows that the pattern's own `EntityOfConcern` and user-facing action are that evaluation or projection work. | Prevents quality of the authored pattern from replacing the evaluation guidance it must teach. |

### E.8.ECSPF:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Score-sheet pattern.** | The pattern is mostly a table of values. | Move evaluated object kind, use, first evaluation use, FPF-publication boundary, and practical consequence into recognition text before the table. |
| **Checklist-as-solution.** | Users are told only what must be checked. | Put the actual evaluation method and record shape in `Solution`; let checklist rows verify it. |
| **Publication-form/content collapse.** | The accepted specification, its `CharacteristicSpace`, the pattern, the evaluated object, the later evaluation, and its result are treated as one thing. | State what each is and show that the pattern teaches the accepted specification; none of the other objects becomes the pattern. |
| **Positive-only case bank.** | Every example passes. | Add below-floor and outside-declared-object-kind boundary cases. |
| **Undeclared total.** | Ordinal coordinate values are added, averaged, or collapsed into an “overall score”. | Keep the coordinates visible; if a bounded scalarization is separately admitted, name its method, use, information loss, applicability, and stop or return condition. |
| **Proxy improvement.** | A visible coordinate rises while a protected value becomes worse, yet the result is called improved. | Compare the changed values and protected trade-offs; stop or reopen when the evaluation rewards the loss. |
| **Related-pattern authority theft.** | The pattern claims authority over evidence, assurance, a gate or release decision, measurement, naming, or improvement. | Cite the applicable pattern and state the concrete contribution used here; keep only the evaluation claim in this pattern. |
| **Rubric promotion.** | A local rubric becomes an FPF pattern because it was useful once. | Keep it local unless durable FPF reuse and evaluated-object scope are established and every outside claim names the applicable pattern and its contribution. |
| **Frozen evaluation publication form.** | The evaluated EntityOfConcern kind, use, use of a cited source, source adoption/adaptation/rejection decision, or coordinate meanings change, but the pattern keeps the old values as if still current. | Reopen `A.19.ECS` for the evaluation EntityOfConcern and state whether earlier evaluation results remain comparable, need a bridge, or must be retired. |
| **Report-shaped evaluation pattern.** | The pattern publishes coordinate names but leaves the returned result as a narrative, score list, or two-column table. | Add a result-form block: coordinate, value, short rationale, evidence basis, and coordinate-specific payload where needed. |
| **Pattern-quality report as evaluation pattern.** | `E.21` status, all-`4` or all-`5` posture, corpus projection, retrieval evidence, README, ToC, E.11, and I.2 alignment, monolith parity, landing readiness, or author or reviewer turn correspondence appears anywhere in the pattern as if it were the evaluation method. | Move that evidence to the quality, review, projection, or release carrier and keep the pattern body focused on the evaluation for the declared evaluated object kind. |
| **Apparatus-overwrapped publication form.** | The evaluation relation is written through ambiguous role, carrier, locus, flow, status, or package words that add no evaluated object kind, coordinate meaning, evidence rule, user-facing action, or exact flow position. | Apply `F.19`; if remaining content still hides a word, head, or use, apply `E.10`, `E.10.ARCH`, `F.18`, or the pattern that defines the affected object or relation. |

### E.8.ECSPF:9 - Consequences

A conforming `E.8.ECSPF` publication form makes evaluation guidance findable, teachable, and reusable inside FPF. It lets a practitioner frame an evaluation with `E.22` or repeat improvement with `E.23` without re-inventing values. It also makes the cost visible: a reusable evaluation pattern must publish more than a local rubric, because it must prevent wrong-kind use, hidden value drift, neighbour theft, and proxy-for-value substitution.

The pattern's output is bounded evaluation guidance and the form of its result. For product certification, release approval, an evidence claim, or an improvement decision, use the applicable pattern and establish the required result or decision.

### E.8.ECSPF:10 - Rationale

The split between `A.19.ECS` and `E.8.ECSPF` preserves the distinction between an evaluation characteristic-space specification, the pattern that teaches its use, a later evaluation, and the resulting record. `A.19.ECS` says what the specification must contain. `E.8.ECSPF` says how to carry that accepted content into an FPF pattern when durable publication is selected. This prevents two symmetric mistakes: stuffing FPF pattern-format requirements into a general characteristic-space construction method, and publishing guidance whose accepted coordinate set is not recoverable by value.

### E.8.ECSPF:11 - SoTA-Echoing

**Source-use convention and qualification.** The current-source decisions below are qualified through 2026-08-15 for the identified editions and this publication-form question. Each source is used only for the content named in its row. Reopen the smallest affected row when a new edition, successor, or materially better competitor changes that adopted content, its scope, or its currentness; a bibliographic change alone does not reopen the pattern.

| Source and stable identity | Adopted content | Change made here | Boundary | Reopen condition |
|---|---|---|---|---|
| [*BenchmarkCards: Large Language Model and Risk Reporting* (arXiv:2410.12974)](https://arxiv.org/abs/2410.12974) | Structured documentation of benchmark properties, including targeted risks and evaluation methodology, to support informed benchmark selection. | When published evaluation guidance relies on a benchmark, its source basis identifies the benchmark properties that affect coordinate or evidence selection. | BenchmarkCards documents benchmark properties. It does not define the whole evaluation process or prescribe how to measure and interpret a result. | Reopen this use if a successor changes which benchmark properties are needed for informed selection. |
| [*Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting* (arXiv:2606.09809)](https://arxiv.org/abs/2606.09809) | Composition of benchmark metadata, evaluation-run data, and model metadata into one interpretable reporting layer, with reader-sensitive interpretation. | The publication form keeps benchmark description, run evidence, evaluated-object metadata, and the evaluation result distinguishable when those values are required. | This is the 2026 *Evaluation Cards* paper. A separate 2025 proposal called *EvalCards* is not a source here unless its content is deliberately selected and identified. | Reopen if the reporting layers or their interpretive use materially change. |
| [*Holistic Evaluation of Language Models* (HELM, arXiv:2211.09110)](https://arxiv.org/abs/2211.09110) | Standardized scenario-and-metric comparison, multi-metric visibility, stated coverage and missingness, and inspectable prompts and completions. | The pattern publishes the declared scenario or use, metric or coordinate meanings, missingness, and evidence needed for comparison instead of a bare aggregate. | HELM is a language-model evaluation suite, not a general FPF publication method. | Reopen if HELM's comparison discipline is superseded for the adopted scenario, metric, or evidence use. |
| [*VHELM: A Holistic Evaluation of Vision Language Models* (arXiv:2410.07112)](https://arxiv.org/abs/2410.07112) | The HELM comparison discipline extended to vision-language models, with modality-relevant aspects and standardized prompting, inference, metrics, and released generations. | A claimed cross-modality evaluation must publish the modality-specific use, procedure, and evidence that actually affect its coordinates. | Only the vision-language extension is adopted; VHELM does not justify claims about every evaluated object or modality. | Reopen if a successor changes the adopted vision-language procedure or exposes a missing modality boundary. |
| [*AHELM: A Holistic Evaluation of Audio-Language Models* (arXiv:2508.21376)](https://arxiv.org/abs/2508.21376) | The HELM comparison discipline extended to audio-language models across audio-relevant aspects, with standardized prompts, inference parameters, metrics, and released outputs. | An audio-language evaluation must publish the audio-specific use, procedure, and evidence that change its coordinates. | AHELM is an audio-language source, not an agent-evaluation source and not evidence for unrelated modalities. | Reopen if a successor changes the adopted audio-language procedure or exposes a missing audio boundary. |
| [*A survey on Quality-Diversity optimization: Approaches, applications, and challenges* (2026, DOI 10.1016/j.swevo.2025.102240)](https://doi.org/10.1016/j.swevo.2025.102240) | Current overview, for this narrow question, of QD feature or descriptor spaces, local quality and objective heads, diversity, containers, comparison or dominance, and evaluation metrics. | The publication form keeps dimensions, comparison rules, and protected trade-offs visible when an aggregate would hide loss. | QD is optimization over a declared feature space, not a universal evaluation architecture. A bounded scalarization remains separately declared with its use, loss, and non-use boundary. | Reopen if a newer synthesis changes the QD comparison used here or if this pattern claims more than the narrow non-scalar lesson. |

Model-card literature and classic pattern-language literature remain historical lineage for intended-use reporting and action-guiding publication. The retained publication lesson is concrete: put recognition and the first evaluation use before coordinate tables. This lineage is not presented as current-best evidence for the question. Current FPF `E.8` supplies the internal authoring rule and is not an external SoTA source.

### E.8.ECSPF:12 - Relations

| Pattern | Relation |
|---|---|
| `E.8` | Defines the canonical FPF authoring form. `E.8.ECSPF` specializes that form for evaluation `CharacteristicSpace` pattern publication forms. |
| `A.19.ECS` | Guides an author in constructing or repairing the evaluation characteristic-space specification. `E.8.ECSPF` helps an author carry the accepted specification into an FPF pattern when durable reuse is selected. |
| `A.19`, `A.17`, `A.18`, `C.16` | Define the corresponding `CharacteristicSpace`, characteristic, scale, coordinate, and measurement-admissibility rules. |
| `E.21` | Guides a reviewer in evaluating the quality of the authored FPF pattern publication form. It does not replace the evaluation for one evaluated object kind. |
| `E.22` | Helps a practitioner frame one quality evaluation using the guidance published in the pattern. |
| `E.23` | Helps an acting system repeat improvement while reusing that published evaluation guidance. |
| `E.9.DA`, `E.2.DA`, `F.18`, `C.25` | Existing or candidate evaluations that may use this authoring specialization when their publication-form is being written or refreshed. |
| `A.10` | Supplies the bounded evidence-use and provenance discipline when an evaluation result is used as evidence. A recorded value alone does not establish an admissible evidence use. |
| `B.3` | Supplies the assurance and reliance calculus when someone relies on an evaluation result. A favourable value alone creates neither assurance nor warranted reliance. |
| `A.20` | Tests whether a constraint on a transformation flow is valid. An evaluation coordinate or status does not establish that flow constraint. |
| `A.21` | Supplies `GateFit` and `GateDecision` for a real gate. An evaluation result may inform a gate without becoming the gate decision. |
| `C.11` | Supplies the general `ChoiceResult` form when an evaluation informs a choice. An evaluation result does not by itself select an option. |
| `A.15` | Supplies the distinctions needed when the claim depends on a particular `MethodDescription`, `Method`, assignment, or performed `Work`. Ordinary pattern use needs no such identity unless the receiving claim turns on it. |
| `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Supply the relevant definitions and tests for OEE or NQD archives, novelty, diversity, pools, selected sets, parity, and refresh claims. |
| `C.29` | Tests whether a mathematical lens is admissible, including which structure is preserved or lost and what stopping bounds follow. Use it only when such a lens actually supports the coordinate or comparison rule. |

### E.8.ECSPF:End

