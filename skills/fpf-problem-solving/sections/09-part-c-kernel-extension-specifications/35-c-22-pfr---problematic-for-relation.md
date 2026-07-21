## C.22.PFR - Problematic-For Relation

> **Type:** Conceptual (C)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Actual problem.

### C.22.PFR:1 - Problem frame

**Use this when.** Use this pattern when an actual condition may be adverse for one exact entity and use, and a receiving claim needs to distinguish the actual Problem from a signal, criterion description, evaluation, assessment claim, ProblemCard, or claim that no suitable method is currently known.

**First useful move.** Name the actual-condition relation. Then name the exact predicate, entity, scope, and interval for which that predicate applies. If the condition falls on the adverse side of that applicable predicate, say plainly: "This condition is a problem for this entity in this scope." Expose a PFR occurrence only when another claim needs that Problem identity.

**What goes wrong if missed.** A card or evaluation result is allowed to create a Problem; the same criterion is applied to the wrong entity or scope; a new description edition creates a false new Problem; or one continuously adverse episode is split every time evidence is sampled. Conversely, two adverse episodes separated by demonstrated non-adverse behavior collapse into one occurrence.

**What this buys.** Actual Problems can exist before discovery, can be referenced while still ongoing, and can be distinguished across repeated adverse episodes. One exact applicability relation supplies the predicate, problem-for entity, claim scope, and declared criterion-applicability window used by PFR; its actual occurrence extent is separately derived from uninterrupted obtaining. Measurements, evaluations, evidence, claims, cards, and method search remain available without becoming Problem identity.

**Early battery contrast.** A battery-voltage condition below the applicable vehicle-start bound can already participate in an actual PFR before anyone notices it. A later maintenance card is an episteme describing that condition and Problem; writing or accepting the card creates neither. Discovering a supported charging or replacement method changes present solvability, not the still-adverse condition. Only actual change of the condition, loss of criterion applicability, or cessation of adverse predicate truth ends that PFR.

**Not this pattern when.** Use `C.22.2` when the current object is a problem-side card, signal, hypothesis, forecast, scenario, anticipated-condition claim, or reviewable formulation rather than an actual PFR. Use `C.27`, `C.28`, or the exact direct forecast, scenario, counterfactual, or anticipated-condition governor when that claim is current. Use the selected A.19 comparison, `G.4` acceptance, state, gate, or measurement pattern when the current question is how to evaluate or support the adverse predicate. Use `E.18.1`, `E.23`, and the direct NQD or OEE patterns for repeated problematization, search, work, evaluation, and continuation.

### C.22.PFR:2 - Problem

An actual Problem is neither a record nor a free-standing quality label. It depends on an actual condition and on a criterion that applies to one exact entity, scope, and interval. The relation obtains when the condition is on the adverse side of that applicable predicate.

FPF needs one identity for this dependent evaluative relation without copying values owned by `ProblemCriterionApplicabilityRelation` into additional writable PFR slots. It also needs to distinguish continuous adverse episodes from repeated episodes while refusing to infer a recovery from missing observations or evidence.

### C.22.PFR:3 - Forces

| Force | Tension |
|---|---|
| Actuality vs discoverability | A Problem can obtain before anyone evaluates, notices, describes, or publishes it. |
| Readable problem talk vs typed dependence | Practitioners need a direct sentence, while load-bearing use needs exact condition and applicability occurrences. |
| One applicability relation vs duplicated participants | Predicate, problem-for entity, claim scope, and declared criterion-applicability window are useful independently of PFR but must not be writable both as applicability-relation participants and as PFR participants; the applicability occurrence extent remains derived. |
| Continuous identity vs repeated episodes | One adverse episode may receive many assessments; the same participants may also stand in later adverse episodes after a real recovery. |
| Open episode use vs final interval | Current work needs to reference a Problem before the adverse episode has ended. |
| Predicate truth vs epistemic support | Evaluation and evidence support claims about adverse truth but do not make the world-side dependent relation obtain. |
| Solvability vs Problem actuality | Finding a method changes what can be done, not whether the current condition remains adverse. |
| Anticipated-condition claim vs actual occurrence | A useful forecast, scenario, or hazard card can describe a possible condition before any actual-condition relation obtains. |

### C.22.PFR:4 - Solution

Model an actual Problem as one obtaining `ProblematicForRelation`, a dependent evaluative `U.Relation` between exactly two relation occurrences: the actual condition and the applicability of a characteristic-space predicate.

#### C.22.PFR:4.1 - Use one exact criterion-applicability relation

`CharacteristicSpacePredicate` is a by-value predicate used by an A.19 comparison, acceptance, state, gate, or other direct consumer. It is not a new U-kind, publication record, description edition, or comparison result. Its meaning is recoverable from the declared characteristic-space coordinates, scales, normalization or bridge values, operator, cut or band, polarity, and the selected direct consumer's governed comparator, admissibility, and predicate-use semantics. A separately performed evaluation remains `U.Work`; its result episteme and evidential-support relations remain separately governed, and none of these constitutes predicate meaning.

**Public name settlement.** The following F.18 NameCard names the applicability relation kind. It does not make one applicability occurrence obtain and does not replace the relation signature below.

```text
NameCard:
  NameCardId: NC-PROBLEM-CRITERION-APPLICABILITY-RELATION
  GovernedValueRef: ProblemCriterionApplicabilityRelation under C.22.PFR
  GoverningPatternRef: C.22.PFR
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: obtaining relation that canonically links one characteristic-space predicate to one exact problem-for entity over one claim scope and one declared criterion-applicability window; repeated occurrences with the same four participants are distinguished by maximal continuous actual obtaining
  TechLabel: ProblemCriterionApplicabilityRelation
  PlainLabel: problem-criterion applicability
  CandidateSet: ProblemCriterionApplicabilityRelation; CriterionApplicabilityRelation; ProblemCriterionUseRelation; ApplicableProblemCriterion
  RejectedCandidates: CriterionApplicabilityRelation overclaims a universal criterion ontology; ProblemCriterionUseRelation hides obtaining applicability behind use wording; ApplicableProblemCriterion turns a relation into an adjective-headed value
  SelectionRationale: preserve distinct applicability occurrences for different exact entities, scopes, or declared windows and after demonstrated loss and restoration of applicability, without making a predicate-description edition identity-bearing
  LineageEntries: replaces description-edition and generic criterion-use identity proposals
  RefreshCondition: reopen if the four fixed participants plus maximal continuous actual obtaining cannot distinguish applicability occurrences
```

Use one individuable dependent `U.Relation` for applicability:

```text
ProblemCriterionApplicabilityRelation:
  ProblemCriterionPredicateSlot: CharacteristicSpacePredicate, byValue
  ProblemForEntitySlot: U.Entity, byRef with an exact local ValueKind
  PredicateClaimScopeSlot: U.ClaimScope, byValue
  DeclaredCriterionApplicabilityWindowSlot: DeclaredCriterionApplicabilityWindow, byValue; use an explicit unbounded value when no finite bound is intended
```

This relation states that one exact predicate applies to one exact entity for one claim scope under one declared criterion-applicability window. It obtains only while that fixed applicability predicate is actually true under the declared window. One occurrence is identified by the four fixed participants plus the maximal continuous period of actual obtaining. Changing a participant yields another occurrence; demonstrated loss and later restoration of applicability yields distinct occurrences even when all four participants stay fixed. A coextensional description edition or carrier change does not change either the predicate participant or the occurrence. Assessment windows, evidence-relevance intervals, description editions, and claim-currentness windows remain with their own claims and relations.

A semantic predicate change selects a different predicate participant; it is not an edition-only repair. If the new predicate replaces the old predicate for the same use and the old applicability therefore ceases, the old applicability occurrence ends and a new occurrence begins only if the new predicate actually applies. The PFR dependent on the old occurrence can then end, and another PFR can begin under the new occurrence when adverse truth obtains. If both predicates remain applicable, two applicability occurrences may coexist; a new criterion description alone does not prove replacement or cessation.

#### C.22.PFR:4.2 - Keep the PFR signature reduced to two participants

**Public name settlement.** The following F.18 NameCard names the actual dependent evaluative relation. It does not create the Problem, add a third participant, or replace the occurrence-identity rule.

```text
NameCard:
  NameCardId: NC-PROBLEMATIC-FOR-RELATION
  GovernedValueRef: ProblematicForRelation under C.22.PFR
  GoverningPatternRef: C.22.PFR
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: actual dependent evaluative relation with one actual-condition relation occurrence and one problem-criterion-applicability relation occurrence as its only non-derived participants, individuated for each maximal continuous adverse interval
  TechLabel: ProblematicForRelation
  PlainLabel: actual problem
  CandidateSet: ProblematicForRelation; AdverseCriterionAssessmentRelation; ProblemUseRelation; ProblemRelation; ProblemSituationRelation
  RejectedCandidates: AdverseCriterionAssessmentRelation omits the problem-for relation; ProblemUseRelation hides the actual adverse condition; ProblemRelation hides criterion applicability; ProblemSituationRelation falsely requires situation
  SelectionRationale: make ordinary Problem recoverable without copying applicability participants and distinguish repeated adverse episodes without requiring a universal adverse-evaluation relation occurrence
  LineageEntries: situation-first, card-as-world, bearer-duplicating, and description-edition identity proposals retired
  RefreshCondition: reopen if participant references plus the derived maximal continuous adverse interval cannot distinguish repeated PFR occurrences, or if the applicability projection becomes ambiguous
```

**No-mint disposition for root `U.Problem`.** Do not introduce a second problem entity beside the obtaining `ProblematicForRelation` occurrence. That occurrence is the actual Problem; a `ProblemCard`, criterion description, assessment claim, or local Plain label may describe or designate it but does not supply another world-side identity.

The complete non-derived participant set is:

```text
ProblematicForRelation:
  ActualConditionRelationSlot: U.Relation, byRef
  ProblemCriterionApplicabilityRelationSlot: U.Relation, byRef
```

The first reference resolves to the exact obtaining relation that constitutes the actual condition under its direct pattern. The second resolves to the exact obtaining applicability relation from C.22.PFR:4.1.

PFR has no separately writable condition-bearer, predicate, problem-for-entity, claim-scope, applicability-window, assessment-window, or description-edition slot. Those values already have canonical owners. A readable claim projects them from the two participants:

```text
PFR.problemCriterionPredicate
  := PFR.problemCriterionApplicabilityRelation.problemCriterionPredicate
PFR.problemForEntity
  := PFR.problemCriterionApplicabilityRelation.problemForEntity
PFR.predicateClaimScope
  := PFR.problemCriterionApplicabilityRelation.predicateClaimScope
PFR.declaredCriterionApplicabilityWindow
  := PFR.problemCriterionApplicabilityRelation.declaredCriterionApplicabilityWindow
PFR.problemCriterionApplicabilityExtent
  := maximal continuous obtaining extent of PFR.problemCriterionApplicabilityRelation
```

This is a derivation from one participant, not a consistency check between copies.

#### C.22.PFR:4.3 - Use predicate truth as the obtaining condition

`ProblematicForRelation` obtains exactly when all three conditions hold:

1. The exact `ActualConditionRelation` obtains under its direct pattern.
2. The exact `ProblemCriterionApplicabilityRelation` obtains, and its by-value predicate is well-typed for its exact entity and claim scope under its declared criterion-applicability window.
3. The actual condition falls on the adverse side of that predicate under the scales, comparator, cut or band, polarity, and admissibility semantics governed by the selected direct consumer pattern.

The direct consumer evaluates and supports a claim that the adverse predicate obtains. Comparison outcomes, acceptance outcomes, state or gate results, measurements, evidence, and assessment claims may support that claim. They are not automatically PFR participants, and their production does not make PFR obtain.

A Problem can therefore obtain unnoticed. Later detection produces work, evidence, and claims about the already obtaining relation; it does not create retroactive actuality.

#### C.22.PFR:4.4 - Identify repeated adverse episodes

The occurrence identity is:

```text
<actualConditionRelationRef,
 problemCriterionApplicabilityRelationRef,
 maximalContinuousAdverseInterval>
```

`maximalContinuousAdverseInterval` is a derived temporal extent of the PFR occurrence. It is not a writable participant slot and not a new kind. It is the maximal continuous interval during which both participant relations obtain and the actual condition stays on the adverse side of the applicable predicate.

Participant references alone are insufficient because the same participant occurrences can be adverse, non-adverse, and adverse again. A universal constituting evaluation reference is also insufficient because direct consumer patterns do not all individuate such an occurrence, and evaluation is epistemic support rather than what universally constitutes PFR.

#### C.22.PFR:4.5 - Keep one usable identity while the episode is open

Represent a current adverse episode as:

```text
[adverseEpisodeStart, open]
```

For a current reference, this notation denotes the same derived maximal interval whose end is not yet known. `open` is an endpoint sentinel, not the current clock time. As the episode continues, the interval remains `[adverseEpisodeStart, open]`; each observation does not mint a new interval or PFR identity. When the episode is shown to end, record the end endpoint on the same occurrence. Replacing the open endpoint with the recovered end is closure of its derived temporal extent, not replacement by another occurrence.

Use the A-B-C regression:

- During interval A, the condition is demonstrated adverse. One PFR occurrence is current as `[A.start, open]` and later closes at A's end.
- During interval B, the condition is demonstrated non-adverse under the same applicability semantics. The first PFR does not obtain in B.
- During interval C, the condition is again demonstrated adverse. A later PFR occurrence begins with the same two participant references but a different `maximalContinuousAdverseInterval`.

A missing assessment, unavailable measurement, stale evidence item, or gap in support is `unknown`. It is not demonstrated non-adverse behavior. Such a gap neither closes nor splits PFR by itself. Adjacent or overlapping assessment windows inside a continuously adverse episode likewise do not split it.

#### C.22.PFR:4.6 - Keep anticipated-condition claims, solvability, and cards separate

A possible or anticipated problem remains an exact forecast, scenario, counterfactual, or anticipated-condition claim in `ProblemCard@Context` or another episteme until an actual-condition relation, an applicability relation, and adverse predicate truth all obtain. `C.2.1` governs its assertion identity and polarity; `C.27`, `C.28`, or the exact direct claim pattern governs assumptions, horizon, and non-actual semantics; `A.10` or the receiving evaluation separately governs supported, refuted, or unresolved reliance. None of those claim-side facts establishes a current PFR. A card may describe zero, one, or several independently obtaining PFR occurrences; several cards may describe one PFR under different viewpoints.

A claim that no supported method is currently available concerns the admitted method set, evidence, constraints, and acceptance use. Selecting or discovering a method changes current solvability. It does not end PFR while the actual condition remains adverse. Performed repair work can end or change the actual-condition occurrence and thereby end PFR.

Repeated problematization, method search, work, evaluation, and continuation occur in work and transformation flows governed by `E.18.1` and `E.23`. A claim or plan may carry a reference to the same PFR while work and transformation occurrences participate in a selected transformation-flow structure. Neither that PFR reference use nor any flow-structure relation enters PFR identity. A later PFR is a later occurrence because its participants or maximal continuous adverse interval differ, not because flow work revisits an earlier transformation or relation.

#### C.22.PFR:4.7 - Preserve the lightweight path

Ordinary use writes the readable assertion:

> The actual condition is adverse under the predicate applicable to this entity and scope; therefore this condition is a problem for that entity.

The predicate and problem-for entity are projected from the applicability relation. The user does not fill a PFR record by default. Explicitly individuate and expose the PFR only when another claim must compare, qualify, change, nest, plan from, or refer to that actual Problem.

### C.22.PFR:5 - Archetypal Grounding

**Engineering case: battery below the start bound.** The battery voltage-state relation is the actual-condition participant. A vehicle-start applicability relation carries the start predicate, exact vehicle, intended-start scope, and declared criterion-applicability window. Its actual extent is the maximal continuous period in which that applicability obtains. PFR obtains when the voltage condition is on the adverse side. An alarm, measurement report, or maintenance card may later support and publish that claim; none is the Problem occurrence.

**Formal case: a proof gap.** An unresolved-consequence relation is the actual-condition participant. A proof-acceptance applicability relation carries the exact proof-use entity, acceptance scope, predicate, and declared criterion-applicability window. PFR is actual for that proof use when the unresolved relation is adverse under the predicate; it need not be a Problem for every use of the proof episteme.

**Clinical case: patient-specific adversity.** A clinical-condition relation is the actual-condition participant. The applicability occurrence carries a patient-specific predicate, the patient as problem-for entity, admitted care scope, and declared criterion-applicability window. Diagnosis and assessment remain epistemes. PFR has no copied patient or diagnosis slot.

**Organizational case: hand-off failure.** A missed-transfer relation is the condition participant. A service applicability relation carries the service predicate, affected receiving work, scope, and declared criterion-applicability window. Coordination participants remain inside the missed-transfer relation; the receiving work is projected from applicability rather than duplicated in PFR.

**One condition, two affected uses.** One hot-surface condition is paired with two applicability occurrences carrying the same by-value predicate but different exact receiving work or system participants and scopes. When the condition is adverse under both applicability occurrences, two PFR occurrences obtain and are distinguished by their applicability-relation references; PFR copies neither receiving participant nor scope.

**Unnoticed and repaired.** A condition and applicability can make PFR obtain before monitoring exists. Selecting a repair method changes the solvability claim. Performing repair work that ends the adverse condition ends PFR; the work and its result relations remain separately governed.

### C.22.PFR:6 - Bias-Annotation

This pattern has an actuality bias: Plain **problem** names an obtaining dependent relation. The anticipated-condition guard preserves forecasts, scenarios, counterfactuals, hazards, and problem formulations as useful epistemes under their exact claim governors without backdating actuality.

It has a predicate-centered bias because adverse truth is load-bearing. The applicability relation prevents a criterion from becoming globally adverse by label; exact entity, scope, and interval stay explicit.

It also has a continuous-time bias for occurrence identity. Discrete-state and event-based domains can supply equivalent maximal continuous episode boundaries under their temporal reference. Evidence gaps remain unknown in either representation.

### C.22.PFR:7 - Conformance Checklist

1. The actual condition is an explicitly individuated obtaining `U.Relation` under its direct pattern.
2. `CharacteristicSpacePredicate` is given by value and is not replaced by a criterion-description identifier or edition.
3. `ProblemCriterionApplicabilityRelation` has the predicate, exact problem-for entity, claim scope, and declared criterion-applicability window as its four participants; its actual occurrence extent is the maximal continuous period of obtaining.
4. PFR has exactly two non-derived participant slots: actual condition and criterion applicability.
5. Predicate, entity, scope, declared criterion-applicability window, and actual applicability-occurrence extent are projected from applicability rather than copied into PFR.
6. The selected direct consumer pattern governs comparator, cuts or bands, polarity, admissibility, evaluation, and support.
7. Evaluation work, outcomes, measurements, evidence, assessment claims, descriptions, and cards do not create or identify PFR by default.
8. PFR identity includes the derived maximal continuous adverse interval.
9. An ongoing episode uses `[adverseEpisodeStart, open]`; observation updates do not mint successive occurrences, and closure retains the occurrence.
10. Demonstrated non-adverse B between adverse A and C produces two PFR occurrences; an evidence gap does not.
11. Method availability and solvability claims remain separate from PFR actuality and identity.
12. Possible conditions remain exact forecast, scenario, counterfactual, or anticipated-condition claims under their direct governors until both participant relations and adverse predicate truth obtain; assertion polarity and reliance posture do not substitute for those obtaining conditions.
13. Ordinary readable use can stop before explicit PFR materialization when no receiving claim needs Problem identity.

### C.22.PFR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Card-created Problem | Creating or accepting a ProblemCard is treated as Problem actuality. | Test actual-condition obtaining, applicability obtaining, and adverse predicate truth; keep the card as an episteme about zero or more occurrences. |
| Duplicated applicability | Predicate, entity, scope, or interval is writable in both applicability and PFR. | Keep those values only in `ProblemCriterionApplicabilityRelation` and derive PFR projections. |
| Assessment-constituted PFR | Evaluation work or an assessment result becomes the universal third PFR participant. | Let the direct consumer evaluate and support adverse truth; keep PFR's participant set reduced. |
| Evidence-window splitting | Each measurement or assessment window creates a new Problem occurrence. | Derive one maximal continuous adverse interval and keep support windows with their claims. |
| Unknown-as-recovery | Missing evidence is treated as proof that the condition was non-adverse. | Preserve `unknown`; split PFR only at demonstrated non-adverse behavior or participant change. |
| Open-interval churn | Every later observation replaces `[start, open]` with a new current interval and identifier. | Keep the stable open sentinel until closure; then record the recovered end on the same occurrence. |
| Method-selected resolution | Finding a repair method is treated as ending the Problem. | Update the solvability claim; end PFR only when the adverse condition or another obtaining condition ceases. |
| Criterion-edition identity | Rewording or republishing a coextensional criterion creates a new Problem. | Recover the by-value predicate; create another applicability occurrence only when a fixed participant changes or when actual applicability ceases and later obtains again. |

### C.22.PFR:9 - Consequences

**Benefits.** PFR gives actual Problems stable identity without turning cards or evaluations into world-side constituents. Two entities or scopes can use one predicate without collision, repeated adverse episodes remain distinguishable, and ongoing episodes can be referenced before closure. Unknown evidence remains epistemically honest.

**Costs.** A load-bearing use must recover a by-value predicate and exact applicability relation. Direct consumer patterns must state how adverse truth is evaluated, including comparator and polarity semantics. Temporal identity requires a real recovery boundary rather than assessment timestamps.

**Limits.** C.22.PFR does not define domain criteria, measurement methods, comparator semantics, acceptance policy, evidence sufficiency, method search, repair work, or problem-card publication. It governs only actual Problem obtaining, dependence, projection, and occurrence identity.

### C.22.PFR:10 - Rationale

Applicability is independently useful: it states which predicate applies to which entity and use under which declared criterion-applicability window even when no adverse condition currently exists. Keeping those four participants canonical there prevents disagreements between duplicated fields, while maximal continuous actual obtaining distinguishes repeated applicability occurrences without adding a fifth participant. PFR adds the exact missing fact: the named actual condition is adverse for that applicability occurrence.

The maximal continuous adverse interval resolves a genuine identity collision. Participant references alone cannot distinguish adverse A from adverse C after demonstrated recovery B. Assessment identity cannot solve the problem because several assessments can support one episode and an unnoticed episode can exist before assessment. A derived temporal extent distinguishes occurrences without importing epistemic support into world-side identity.

### C.22.PFR:11 - SoTA-Echoing

| Current line | What it contributes | FPF adoption |
|---|---|---|
| FPF `A.19`, `A.19.CPM`, `G.4`, and direct state and gate patterns | Current FPF already separates characteristic-space predicate, comparison semantics, typed acceptance use, and supported outcome. | **Adopt directly.** Put the by-value predicate in applicability and leave comparison, acceptance, evaluation, and support with the selected consumer rather than duplicating them in PFR. |
| FPF `A.6.REL` relation-occurrence discipline | Relation occurrences can be explicit participants and repeated occurrences can use temporal extent when participant identity is insufficient. | **Adopt directly.** Use two relation participants and the derived maximal continuous adverse interval. |
| FPF `A.15.1` and `C.27.TA` temporal conventions | Ongoing occurrences can carry an explicitly open end, while temporal statements name bearer, reference, and interval instead of inferring time from observation records. | **Adapt.** Use `[adverseEpisodeStart, open]`, preserve one occurrence through closure, and keep assessment windows outside identity. |
| Operator seminar practice on development work, selected slides (2026) | Practical explanation separates problematization, characteristics and criteria, method search, performed work, working results, and repeated improvement while keeping them in one understandable progression. | **Adapt as a use-pressure test.** Keep actual PFR identity with the adverse condition and criterion applicability; route method search, work, results, and repetition through their direct patterns and `E.18.1`/`E.23` instead of making them PFR participants. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | Current relation and situation comparisons provide stress pressure for dependent relations, reification, and occurrence identity. | **Use as a comparator.** Retain a dependent relation with explicit participants and identity while avoiding a universal situation object or imported category hierarchy. |
| [TypeDB relation instances](https://typedb.com/docs/core-concepts/typeql/entities-relations-attributes/) | Relation instances can participate in other relation instances in an implementable model. | **Adapt as implementation evidence.** Permit actual-condition and applicability occurrences as PFR participants without treating the database model as the source of PFR truth. |

These lines change the Solution by keeping evaluation outside PFR, admitting relation occurrences as participants, and giving an ongoing adverse episode one stable open-ended identity.

### C.22.PFR:12 - Relations

- `A.6.REL` governs explicit individuation of both PFR participants and PFR itself when a receiving use needs identity.
- `A.6.5` governs the two PFR participant SlotSpecs and the four applicability SlotSpecs.
- `A.19` governs `CharacteristicSpacePredicate`; `A.19.CPM` governs comparison semantics, while `G.4` governs typed acceptance clauses when acceptance is the selected direct consumer.
- `C.16`, `A.18`, and direct measurement patterns govern characteristics, scales, and measurements used by the predicate.
- `C.22` governs selector-facing task typing and TaskSignature assignment after a problem-side episteme is usable.
- `C.22.2` governs ProblemCard claims, signals, forecasts, scenarios, anticipated-condition cues, descriptions, next use, and publication without creating PFR; the exact direct claim pattern governs each claim carried there.
- `A.15.1` and `A.3.4` govern repair work and changes to the actual-condition relation.
- `E.18.1`, `E.23`, and direct NQD and OEE patterns govern repeated problematization, method search, work, evaluation, and continuation; relations locating or ordering those occurrences in a transformation-flow structure do not enter PFR identity.
- `C.27.TA` governs temporal aspect statements when interval publication or temporal adequacy is current.
- `A.10`, `B.3`, and `G.11` govern evidence use, assurance, and source or claim currentness.

### C.22.PFR:End

