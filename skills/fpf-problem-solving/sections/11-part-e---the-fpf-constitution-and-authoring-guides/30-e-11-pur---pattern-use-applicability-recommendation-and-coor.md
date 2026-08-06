## E.11.PUR - Pattern-Use Applicability, Recommendation, and Coordination

> **Type:** Pattern-language use pattern (E)
> **Status:** Stable
> **Normativity:** Normative for deciding applicability, recommendation, and coordination among candidate FPF pattern uses, with addressable support only when a later use relies on it.

### E.11.PUR:1 - Problem frame

#### E.11.PUR:1.1 - Use this when

Use `E.11.PUR` after one or more candidate pattern uses have been inspected and a person or assisting agent needs to decide whether each use fits, which use to recommend, or how several uses should be coordinated for the current concern. The candidates may remain conversational in ordinary bounded use; addressable `CandidatePatternUse@Context` values are required only when a named later reliance needs them.

**Primary EntityOfConcern.** One current applicability, recommendation, or coordination judgement over already inspected candidate pattern uses. When that judgement must remain addressable, it may be represented by `PatternUseApplicabilityFinding@Context`, `PatternUseRecommendation@Context`, or `PatternUseCoordination@Context`; a `PatternUseOrderingRelation@Context` exists only inside the coordination it qualifies.

The `@Context` suffix on these compatibility support names is retrieval wording only. It names no bounded-context entity, generic situation, project container, relation participant, or identity field; every episteme follows C.2.1 identity, and an ordering relation follows its own participant, condition, obtaining, and occurrence rules.

**What this buys.** Applicability no longer silently becomes recommendation, and presentation order no longer silently becomes workflow order. A project can preserve exact reasons for a consequential recommendation without burdening ordinary bounded use with five separate forms.

**Not this pattern when.** Use `E.11` while public entries are still being compared. Use `E.11.PUA` to use one selected pattern and obtain its first result. Use A.15 for work planning or performed work, A.21 for a gate decision, and the direct decision or authorization pattern when those claims are current.

In this pattern, *next move* is Plain shorthand for the currently recommended pattern use or conditional continuation. It is not a shared `Move` identity, `U.Method`, `U.WorkPlan`, performed `U.Work`, or actual `U.Transformation`; selection or imperative wording performs nothing.

### E.11.PUR:2 - Problem

Several different claims are often compressed into “use this pattern next.” A pattern can fit the Problem frame but fail its `Solution` conditions. It can be applicable yet not be the recommended use because another applicable pattern offers a more useful first result for the current concern. Several candidate uses can belong together without forming a sequence, and displaying a sequence creates no WorkPlan, performed work, Transformation, or transformation-flow structure.

When these distinctions are missing, familiar PatternIDs become proxies for value. Teams recommend the pattern they know, copy one result description into several order relations, and treat a diagram or teaching order as execution order.

### E.11.PUR:3 - Forces

| Force | Pressure on the solution |
| --- | --- |
| Compact ordinary judgement | A local reversible use should permit one concise rationale. |
| Addressable reliance | Transfer, audit, automation, delayed feedback, or costly reversal can rely on separate fit findings. |
| Applicability versus recommendation | A fit finding does not select a candidate for current use. |
| Plural coordination | Several candidates may be alternatives, complements, or partially ordered. |
| Exact precedence | Result-based precedence reuses the prerequisite candidate's exact expectation and current directly grounded closure. |
| No work overread | Pattern-use coordination does not plan, authorize, or perform project work. |
| Proxy resistance | Pattern familiarity, score, and publication order are not evidence of expected practical gain. |

### E.11.PUR:4 - Solution

Evaluate candidate uses against five distinct fit aspects. An ordinary reversible judgement may remain conversational: keep the aspects in one compact rationale, state the aggregate applicability, then recommend by expected first result and live alternatives. Materialize separate findings or a recommendation episteme only when a named later use needs addressable support. Coordinate several candidates with an explicit local ordering mode and add pairwise precedence only where a real basis exists.

#### E.11.PUR:4.1 - Fit and applicability

```text
PatternUseFitCriterionValue =
  problemFrame | forces | solutionConditions | ordinaryBoundary | resultAndReceivingUse

PatternUseFitResultValue = fit | misfit | insufficientBasis
PatternUseApplicabilityResultValue = applicable | inapplicable | insufficientBasis

PatternUseFitFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  fitCriterion: PatternUseFitCriterionValue
  fitResult: PatternUseFitResultValue
  fitRationaleRef: U.EpistemeRef, referencing one CandidatePatternUseRationale@Context

PatternUseApplicabilityFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  fitFindingRefs[5]: U.EpistemeRef, each referencing one PatternUseFitFinding@Context
  applicabilityResult: PatternUseApplicabilityResultValue
  missingBasisBoundaryRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The five criteria refer to one candidate. In ordinary conversation, inspect all five and state the aggregate result in the recommendation without materializing five findings. `PatternUseApplicabilityFinding@Context` is the reliance-bearing support episteme: when it exists, its five findings cover each criterion exactly once. `applicable` follows only when all five are `fit`; any `misfit` yields `inapplicable`; one or more `insufficientBasis` values yield `insufficientBasis` and a missing-basis boundary.

`problemFrame` compares the candidate pattern's Problem frame with the current concern; it does not assert that an actual Problem obtains. When an actual Problem is relied on, cite one current C.22.PFR `ProblematicForRelation` occurrence with its exact actual-condition and criterion-applicability participants and adverse-episode identity. A ProblemCard, fit finding, assessment, or recommendation may support a claim about that occurrence but neither creates nor splits it.

#### E.11.PUR:4.2 - Recommendation

State the ordinary recommendation first: which candidate is applicable, why its expected first result serves the current concern better than the live alternatives, and where to stop or return. If the judgement is local, reversible, and has no named later reliance, that readable statement is sufficient.

When the recommendation must remain addressable, use the schema below. `ordinaryCompact` keeps one compact rationale and no five-finding dossier; `relianceBearing` adds the current applicability finding only because a named later use needs independent replay.

```text
PatternUseRecommendationSupportProfileValue = ordinaryCompact | relianceBearing

PatternUseRecommendation@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the selected CandidatePatternUse@Context
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  recommendationSupportProfile: PatternUseRecommendationSupportProfileValue
  applicabilityResult: PatternUseApplicabilityResultValue
  compactApplicabilityAndSelectionRationaleRef: U.EpistemeRef, referencing one CandidatePatternUseRationale@Context
  applicabilityFindingRef?: U.EpistemeRef, referencing one PatternUseApplicabilityFinding@Context
  expectedResultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  strongerNeighborPatternRef?: U.EntityRef, referencing the exact neighboring FPF pattern episteme only when its identity changes the recommendation
  recommendationBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Recommendation selects one applicable candidate for the current concern because its expected first result serves that concern better than the live alternatives and, when a receiving use is current, supports that use under the stated rationale. A conversational judgement needs no record. In an addressable `ordinaryCompact` recommendation, the applicability result and compact rationale are carried directly and `applicabilityFindingRef` is absent. In `relianceBearing`, the same recommendation also cites one current applicability finding whose five fit findings can be replayed independently. The profile changes support cardinality, not the recommendation kind or authority.

When an addressable recommendation is materialized, `expectedResultExpectationRef` points to its exact E.11.PUA expectation. It identifies the expected result and only the pattern, relative-object, or category-correct basis distinctions that expectation actually uses; it does not assert that the result exists or that any relation, A.6.1 binding, or local claim is current. A recommendation does not authorize work, establish a gate, prove evidence sufficiency, create the expected result, or supply its later closure.

When a stronger neighboring pattern better addresses the current question, name it and state the return condition. Populate `strongerNeighborPatternRef` only when the exact pattern identity matters to an addressable recommendation. The reference does not establish formal `U.MethodDescription` membership; such membership requires its own A.3.2 basis. Familiarity with the current candidate is not a recommendation reason.

#### E.11.PUR:4.3 - Coordination without forced order

For ordinary local coordination, state the candidates, whether they are unordered, partially ordered, or totally ordered, any real precedence basis, and the stop boundary in readable prose. Materialize the rationale, coordination episteme, and any pairwise ordering relations only when a named later use needs that coordination to remain addressable.

```text
PatternUseOrderingModeValue = unordered | partialOrder | totalOrder

PatternUseCoordinationRationale@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the coordination-question episteme
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  subjectCandidatePatternUseRefs[2..*]: U.EpistemeRef, each referencing one CandidatePatternUse@Context
  coordinationRationaleDescriptionRef: U.EpistemeRef
  rationaleBasisEpistemeRefs[]: U.EpistemeRef
  coordinationBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context

PatternUseCoordination@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the coordination-question episteme
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  memberCandidatePatternUseRefs[2..*]: U.EpistemeRef, each referencing one CandidatePatternUse@Context
  orderingMode: PatternUseOrderingModeValue
  orderingRelationRefs[]?: U.EntityRef, each referencing one PatternUseOrderingRelation@Context
  coordinationRationaleRef: U.EpistemeRef, referencing one PatternUseCoordinationRationale@Context
  stopBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

`unordered` has no ordering relations. `partialOrder` and `totalOrder` use explicit pairwise relations. A total order is the bounded `PatternUseSequence@Context` specialization under its named receiving use; it is not a universal route or project WorkPlan.

#### E.11.PUR:4.4 - Pairwise precedence

```text
PatternUsePrecedenceBasisValue =
  prerequisiteResult | methodPrecondition | sharedConstraintResolution

PatternUseOrderingRelation@Context <: U.Relation:
  coordinationRef: U.EpistemeRef, referencing one PatternUseCoordination@Context
  prerequisiteCandidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  dependentCandidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  precedenceBasis: PatternUsePrecedenceBasisValue
  precedenceBasisResultExpectationRef?: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  precedenceBasisResultClosureFindingRef?: U.EpistemeRef, referencing one current PatternUseResultClosureFinding@Context
  precedenceConditionRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  orderingRationaleRef: U.EpistemeRef, referencing one PatternUseCoordinationRationale@Context
  RelationRefKind: U.EntityRef
  Direction: prerequisiteCandidatePatternUseRef -> dependentCandidatePatternUseRef
  Dependence: local to coordinationRef, both candidate editions, the precedence basis and condition, and any current result-closure support to coordinationRef and both candidate editions
  Identity: <coordinationRef, prerequisiteCandidatePatternUseRef, dependentCandidatePatternUseRef, precedenceBasis, precedenceConditionRef>
```

The prerequisite and dependent candidates are different members of the same coordination relation. When `precedenceBasis=prerequisiteResult`, both result references are present. `precedenceBasisResultExpectationRef` equals the prerequisite candidate's exact expectation. `precedenceBasisResultClosureFindingRef` resolves to that same candidate and expectation and reports the independently identified result or obtaining relation plus the category-correct basis that makes the precedence claim true. Predicate, pattern locator, `ClaimGraph`, Method, plan, dated Work, Transformation, evaluation, decision, or later-use object appear only when the cited closure actually depends on them. The ordering relation copies none of those fields.

The closure finding is a C.2.1 episteme and creates neither the result nor the ordering relation. The ordering relation obtains only while its `precedenceConditionRef` is satisfied by the result and category-correct basis reported there. A missing relation rule or information, false predicate, or absent operation binding leaves the precedence relation non-obtaining and the dependent use at its return boundary. For `methodPrecondition` and `sharedConstraintResolution`, both result-reference positions are absent.
The dependent candidate use is admitted under a precedence relation only after its precedence basis is established. Page order, seminar order, identifier order, or visual adjacency does not create that relation.

#### E.11.PUR:4.5 - Practical procedure

1. Recover each candidate's current concern, direct pattern, Solution, expectation, and ordinary boundary.
2. Keep a local reversible applicability, recommendation, or coordination judgement conversational when no named later reliance needs it. When a recommendation must remain addressable, choose `ordinaryCompact` unless that reliance needs the fit aspects separately addressable; use `relianceBearing` only for that reliance.
3. Inspect all five fit aspects. In ordinary use, keep them in one compact rationale. Under named reliance, materialize five separate findings and one applicability finding.
4. State the aggregate applicability result directly in the recommendation; when a reliance-bearing applicability finding exists, the two result values agree.
5. Recommend an applicable candidate only when its expected result serves the current concern better than the live alternatives; include a receiving use only when one is current. The expectation is not an achieved result.
6. Coordinate several candidates as unordered, partially ordered, or totally ordered. Add a pairwise relation only when one declared precedence basis is current. For `prerequisiteResult`, require the prerequisite candidate's exact expectation and one current E.11.PUA result-closure finding with the complete direct basis.
7. Stop at the recommendation or coordination result. A Plain *next move* names only the recommended pattern use or conditional continuation. Continue to PUA, P2W, planning, gate, decision, or work only when that next claim becomes current.

#### E.11.PUR:4.6 - Replay and currentness

Replay an ordinary conversational or addressable compact recommendation from the current concern, inspected candidate pattern and `Solution`, aggregate applicability, compact rationale over all five aspects, live alternatives, expected result, any current receiving use, and recommendation boundary. Replay a reliance-bearing recommendation from those same positions plus the current applicability finding and its five fit findings. Replay coordination from its inspected candidate uses, question, ordering mode, any pairwise precedence and bases, stop boundary, and, for each `prerequisiteResult` relation, the exact expectation and current E.11.PUA closure finding.

Recheck the smallest affected finding or relation when a candidate `Solution`, result expectation, result entity, relative object, direct basis or defining `ClaimGraph`, fit basis, live alternative, dependent use, coordination member, precedence basis, condition, or boundary changes. A changed candidate fit reopens its applicability and any recommendation that relied on it. A changed prerequisite expectation or closure reopens only the affected ordering relations and their dependent uses unless the coordination question or membership also changed. Separate G.11 assertions state edition, telemetry, currentness-window, and decay facts; PUR supplies the judgment-specific values and change conditions.

### E.11.PUR:5 - Archetypal Grounding

#### E.11.PUR:5.1 - Applicable but not recommended

A team considering a high-cost pump test has candidate uses of `C.28` causal triage and `A.21` gate discipline. Both may be applicable. The immediate uncertainty is whether a causal model output may support intervention, so `C.28` offers the more useful first result. That uncertainty and the recommendation are epistemic; neither asserts an actual C.22.PFR Problem.

Recommend `C.28` without claiming that the test is authorized. The later gate use remains a separate candidate whose applicability can be reconsidered after the causal-use result exists.

Because this local recommendation is reversible and no named later use relies on it, the team states the applicability result and one compact rationale over all five aspects in the working conversation; it materializes no recommendation episteme or support profile. If a later gate review needs to replay each aspect independently, that review may create current fit findings and a current applicability finding from the then-current basis. It does not backdate those addressable findings; the original readable rationale, when retained in its ordinary carrier, remains the earlier recommendation's historical basis.

#### E.11.PUR:5.2 - Unordered complementary uses

A clinical team needs both a terminology repair and an evidence-basis review before revising a protocol. Neither result is a prerequisite for the other in the current context.

State an unordered coordination: the team may use either pattern first or use them in parallel. No coordination episteme or ordering relation is required for that local judgement. If the later protocol revision becomes a named reliance that needs the coordination replayable, materialize one `PatternUseCoordination@Context` with `orderingMode=unordered` and no ordering relations. Their coexistence does not create a lifecycle or WorkPlan.

#### E.11.PUR:5.3 - Result-based precedence

A design team's architecture-candidate comparison begins only after its evaluation coordinates are defined. One candidate use of `A.19.ECS` expects an `EvaluationCharacteristicSpaceSpec`; the dependent comparison use consumes that exact result.

Use `precedenceBasis=prerequisiteResult`, point to the ECS candidate's existing expectation, and cite its current E.11.PUA result-closure finding. The closure must identify the exact `EvaluationCharacteristicSpaceSpec`, its defining or constraining `ClaimGraph` and pattern locator, the evaluation or Method use relative to which it is this result, and the direct relation, A.6.1 binding, or local-claim basis with its exact predicate. Do not copy the spec or its signature into ordering fields. Until that basis is current, no precedence occurrence is established and the dependent use stays at its return boundary.

#### E.11.PUR:5.4 - Method precondition is not a result dependency

A machining pattern assumes an admitted material-kind classification. The classification is a method precondition already current for that exact machining use, not the result of another candidate pattern use.

If coordination is still useful, use `methodPrecondition` and leave both result-reference positions absent. Do not invent a prerequisite result merely to make the relation look uniform.

#### E.11.PUR:5.5 - Repair a stale copied prerequisite locally

An older architecture coordination copied `EvaluationCharacteristicSpaceSpec` and its signature into an ordering record. The ECS candidate's current expectation later changed, leaving the copy stale while both candidates, their applicability findings, the coordination question, and `partialOrder` mode remained sound.

Repair only the ordering relation: remove the copied result description, set `precedenceBasis=prerequisiteResult`, and reference the ECS candidate's current expectation and current E.11.PUA result-closure finding. If the exact result, relative object, direct basis, predicate, or defining `ClaimGraph` cannot be recovered, keep the precedence relation non-obtaining and the dependent use at its return boundary. Candidate inspection, applicability, coordination membership, and direct `Solution` content do not restart.

#### E.11.PUR:5.6 - A higher recommendation score can reduce useful fit

An assistant ranks candidate pattern uses by historical recommendation acceptance. The familiar `A.21` gate candidate receives a higher score and is recommended first more often for causal-use uncertainty. Recommendation acceptance rises, but wrong-turn returns also rise because the needed `C.28` causal-use result is still absent.

The score improved while first-result fit and receiving-use value worsened. Keep the historical score as telemetry, apply `E.13` to the substitution, and base recommendation on current applicability, expected result, receiving use, and live alternatives. A higher score is not another fit finding.

### E.11.PUR:6 - Bias-Annotation

- **Applicability-as-recommendation bias.** A fitting pattern is automatically selected. Compare the expected practical result and live alternatives before recommending it.
- **Favorite-pattern proxy bias.** Familiar PatternID substitutes for current value. State the concern, expected result, and any current receiving use in the rationale.
- **Five-form bias.** Every ordinary use creates five findings. Keep them in one compact rationale unless their separate identity is relied on.
- **Sequence bias.** Presentation order becomes precedence. Repair by naming the pairwise basis.
- **Result-copy or expectation-as-result bias.** A prerequisite result kind is duplicated in ordering fields, or its expectation is treated as achieved. Reuse the prerequisite candidate's exact expectation and current E.11.PUA closure finding; the closure reports but does not create the exact result and direct basis.

### E.11.PUR:7 - Conformance Checklist

| ID | Check | Passing condition |
| --- | --- | --- |
| `PUR-1` | Candidate basis | Every evaluated candidate has an inspected `Solution` and a recoverable expected first result or honest blocker; an exact PUA expectation is required only for an addressable recommendation or result-based precedence. |
| `PUR-2` | Five aspects | Ordinary judgement considers all five fit aspects in one rationale; reliance-bearing applicability has exactly one finding for each aspect. |
| `PUR-3` | Aggregate | A recommendation follows the aggregate applicability judgement. If an addressable applicability finding exists, its result agrees and carries a missing-basis boundary when needed. |
| `PUR-4` | Recommendation | The recommended candidate is applicable and its expected result serves the current concern better than live alternatives. An addressable `ordinaryCompact` recommendation has no applicability-finding ref; `relianceBearing` has one current five-finding result. |
| `PUR-5` | Coordination | All members concern the same bounded coordination question and remain distinct candidate uses. |
| `PUR-6` | Ordering mode | Unordered has no pairwise relations; partial and total order contain only justified pairwise relations. |
| `PUR-7` | Exact precedence | `prerequisiteResult` reuses the prerequisite candidate's exact expectation and one current E.11.PUA closure whose result and category-correct basis satisfy the stated condition; other basis values leave both result positions absent. |
| `PUR-8` | Boundary | Recommendation or coordination asserts no plan, work, gate, decision, authorization, actual Problem, Transformation, or subject result. |
| `PUR-9` | Problem actuality | A Problem-frame fit or ProblemCard is not an actual Problem; a relied-on actual Problem resolves to one C.22.PFR occurrence. |
| `PUR-10` | Plain move | *Next move* names only a recommendation or conditional continuation; it creates no Move identity and performs no Work or Transformation. |

### E.11.PUR:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails | Repair |
| --- | --- | --- |
| Recommend before aggregating fit | A partial match is overread as selection. | Resolve all five aspects or return `insufficientBasis`. |
| Rank every candidate | A scalar order hides complements and incomparable results. | Use unordered or partial coordination when that matches the current relation. |
| Use sequence as WorkPlan | Pattern-use relations acquire dates, resources, and work authority that no such relation establishes. | Create an A.15.2 WorkPlan only when intended work is current. |
| Copy or merely expect the prerequisite result | Duplicated kind and signature can drift from the candidate expectation, while an expectation alone proves no result or basis. | Reference the exact expectation and one current E.11.PUA closure finding; if its result or direct basis is absent, keep the precedence relation non-obtaining. |
| Treat a context label as identity | A project, domain, or context label is made a participant or identity field for recommendation or coordination. | Identify the C.2.1 episteme from its claim content, EntityOfConcern, and effective reference scheme; keep every neighboring scope, model-use, work, and qualification relation separate. |
| Treat recommendation as authorization | Guidance bypasses evidence, gate, commitment, or work governance. | Continue to the direct evidence, gate, decision, authorization, or work pattern for that stronger claim. |

### E.11.PUR:9 - Consequences

**Benefits.** A team can explain why a pattern fits, why another is recommended, and how several uses relate without creating a false workflow. Ordinary reversible judgement remains light; reliance-bearing recommendations remain replayable. Result-based precedence stays synchronized with the candidate expectation and the actual PUA result closure.

**Costs.** A consequential or delayed-use recommendation needs an explicit rationale and may need five addressable fit findings. Partial orders need justified pairwise relations. Ordinary local judgement pays no record cost merely for symmetry, and candidates that answer different questions are not forced into a scalar ranking.

### E.11.PUR:10 - Rationale

Applicability, recommendation, and coordination answer different questions. Applicability asks whether a candidate's conditions hold. Recommendation asks which applicable use best serves the current concern. Coordination asks how several candidate uses belong together. Keeping the questions separate prevents a familiar label or score from becoming an unexamined decision.

Pairwise precedence is intentionally narrow. A set of candidate pattern uses can be unordered, partially ordered, or totally ordered. Only a current dependency justifies an edge. A prerequisite-result edge needs both the exact expectation and an E.11.PUA closure whose result and category-correct basis satisfy the stated condition; neither a result label nor an expectation can do so. This preserves graph structure without turning every explanation into a chain or minting a generic result relation.

### E.11.PUR:11 - SoTA-Echoing

| Source or practice line | Problem-solving move taken here | Adoption and boundary |
| --- | --- | --- |
| Que et al., *LLM-as-a-Judge for Reliable and Explainable Offline Evaluation in Top-K Recommendation*, KDD 2026, arXiv:2606.22961 | Observed feedback and Top-K scores can be biased proxies; pair a judgement with explicit rationale rather than treating the score as self-explanatory. | Adapt the proxy warning and rationale pressure to current candidate fit and expected-result reasoning. Reject the recommender, Top-K, user-profile, and LLM-judge ontology as a model of FPF recommendation authority. |
| Nunes and Jannach, *A Systematic Review and Taxonomy of Explanations in Decision Support and Recommender Systems*, User Modeling and User-Adapted Interaction 27 (2017) | Lineage for separating recommendation explanation functions and making reasons addressable to a receiving decision. | Retain as lineage, not current-best evidence. Candidate and coordination rationales do not prove applicability or authorize action. |
| Jin, Bai, and Oulasvirta, *Modeling Trial-and-Error Navigation With a Sequential Decision Model of Information Scent*, arXiv:2603.11759 (2026) | Preserve bounded search, wrong-turn recovery, and reconsideration under limited attention. | Adapt to candidate reconsideration and return boundaries. The preprint does not decide recommendation authority or record cardinality. |
| Current FPF NQD and OEE lines together with A.19 comparison practice | Preserve plural candidates, non-dominated alternatives, explicit comparison spaces, and dynamic reconsideration. | Adopt the plurality discipline. PUR coordinates pattern uses but does not replace subject-domain candidate evaluation. |

The practical implication is to recommend a use for its expected result, not for its familiarity or score, and to add order only where a real dependency exists.

Que et al. is the current decision-bearing recommender source in this narrow use; Nunes and Jannach supplies lineage. The 2026 navigation preprint supplies bounded reconsideration, while current FPF NQD, OEE, and A.19 supply the transdisciplinary candidate and comparison basis. These sources change `4.1-4.5` and `5.6`; none decides FPF kinds or recommendation authority.

Reopen the score-proxy adaptation when stronger evaluation evidence shows that the relied-on score tracks current expected-result and receiving-use fit without the identified exposure or rationale loss. Reopen the wrong-turn adaptation when peer review, replication, or use evidence changes the value of reconsideration. `G.11` orchestrates source and telemetry currentness; PUR changes the affected fit, rationale, recommendation, or return relation.

### E.11.PUR:12 - Relations

- **Builds on:** `E.11.PUA` for candidate uses, expectations, rationales, and boundaries; `A.6.5` for slot discipline; and `E.18` for coupled-flow relations when results cross flows.
- **Coordinates with:** `E.11` for public discovery; `C.22.PFR` for an actual Problem; `A.19`, `A.19.ECS`, and `A.19.CPM` for characteristic-space construction and comparison; `E.18.1` for P2W; `G.11` for currentness; and the direct pattern that defines, constrains, or tests any stronger plan, work, transformation, gate, evidence, decision, authorization, result, or basis claim.
- **Leads to:** `E.11.PUA` for using the recommended pattern, or to the exact neighboring pattern when the stronger claim becomes current.

### E.11.PUR:End

