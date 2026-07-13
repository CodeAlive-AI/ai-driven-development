## E.11.PUR - Pattern-Use Applicability, Recommendation, and Coordination

> **Type:** Pattern-language use pattern (E)
> **Status:** Stable
> **Normativity:** Normative for reliance-bearing applicability findings, pattern-use recommendations, and coordination among candidate FPF pattern uses.

### E.11.PUR:1 - Problem frame

#### E.11.PUR:1.1 - Use this when

Use `E.11.PUR` after one or more `CandidatePatternUse@Context` values are available and a person or assisting agent needs to decide whether each use fits, which use to recommend, or how several uses should be coordinated for the current concern.

**Primary EntityOfConcern.** One current PUR-governed value over already inspected candidate pattern uses: a `PatternUseApplicabilityFinding@Context`, a `PatternUseRecommendation@Context`, or a `PatternUseCoordination@Context`. A `PatternUseOrderingRelation@Context` is current only inside the coordination it qualifies.

**What this buys.** Applicability no longer silently becomes recommendation, and presentation order no longer silently becomes workflow order. A project can preserve exact reasons for a consequential recommendation without burdening ordinary bounded use with five separate forms.

**Not this pattern when.** Use `E.11` while public cards are still being compared. Use `E.11.PUA` to apply one selected pattern and obtain its first result. Use A.15 for work planning or performed work, A.21 for a gate decision, and the direct decision or authorization pattern when those claims are current.

### E.11.PUR:2 - Problem

Several different claims are often compressed into "use this pattern next." A pattern can fit the problem frame but fail its Solution conditions. It can be applicable yet not be the recommended use because another pattern produces a more useful first result. Several candidate uses can belong together without forming a sequence, and a sequence can be shown without creating a WorkPlan.

When these distinctions are missing, familiar PatternIDs become proxies for value. Teams recommend the pattern they know, copy one result description into several order relations, and treat a diagram or teaching order as execution order.

### E.11.PUR:3 - Forces

| Force | Pressure on the solution |
| --- | --- |
| Compact ordinary judgement | A local reversible use should permit one concise rationale. |
| Addressable reliance | Transfer, audit, automation, delayed feedback, or costly reversal can rely on separate fit findings. |
| Applicability versus recommendation | A fit finding does not select a candidate for current use. |
| Plural coordination | Several candidates may be alternatives, complements, or partially ordered. |
| Exact precedence | Result-based precedence reuses the prerequisite candidate's exact expectation. |
| No work overread | Pattern-use coordination does not plan, authorize, or perform project work. |
| Proxy resistance | Pattern familiarity, score, and publication order are not evidence of expected practical gain. |

### E.11.PUR:4 - Solution

Evaluate candidate uses against five distinct fit aspects. Keep those aspects in one compact rationale for ordinary bounded use. Materialize separate findings only when a named receiving reliance needs them. Aggregate applicability before issuing a recommendation. Coordinate several candidates with an explicit local ordering mode and pairwise precedence relations only where a real basis exists.

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

#### E.11.PUR:4.2 - Recommendation

```text
PatternUseRecommendationSupportProfileValue = ordinaryCompact | relianceBearing

PatternUseRecommendation@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
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
  strongerNeighborPatternRef?: U.EntityRef, referencing one U.MethodDescription
  recommendationBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Recommendation selects one applicable candidate for the current concern because its expected result and receiving use are preferable under the stated rationale. In `ordinaryCompact`, the applicability result and compact rationale are carried directly and `applicabilityFindingRef` is absent. In `relianceBearing`, the same recommendation also cites one current applicability finding whose five fit findings can be replayed independently. The profile changes support cardinality, not the recommendation kind or authority. A recommendation does not authorize work, establish a gate, prove evidence sufficiency, or create the expected result.

When a stronger neighboring pattern better addresses the current question, name it and use the recommendation boundary to return. Familiarity with the current candidate is not a recommendation basis.

#### E.11.PUR:4.3 - Coordination without forced order

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
  boundedContextRef: U.BoundedContextRef
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
  precedenceConditionRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  orderingRationaleRef: U.EpistemeRef, referencing one PatternUseCoordinationRationale@Context
  RelationRefKind: U.EntityRef
  Direction: prerequisiteCandidatePatternUseRef -> dependentCandidatePatternUseRef
  Dependence: bounded-context local to coordinationRef and both candidate editions
  Identity: <coordinationRef, prerequisiteCandidatePatternUseRef, dependentCandidatePatternUseRef, precedenceBasis, precedenceConditionRef>
```

The prerequisite and dependent candidates are different members of the same coordination relation. When `precedenceBasis=prerequisiteResult`, `precedenceBasisResultExpectationRef` is present and equals the prerequisite candidate's exact result expectation. The ordering relation never copies result kind or relation-signature slots. For `methodPrecondition` and `sharedConstraintResolution`, the result-expectation position is absent.

The dependent candidate use is admitted under a precedence relation only after its precedence basis is established. Page order, seminar order, identifier order, or visual adjacency does not create that relation.

#### E.11.PUR:4.5 - Practical procedure

1. Recover each candidate's current concern, direct pattern, Solution, expectation, and ordinary boundary.
2. Choose `ordinaryCompact` unless a named receiving use needs the fit aspects to remain independently addressable; use `relianceBearing` only for that reliance.
3. Inspect all five fit aspects. In ordinary use, keep them in one compact rationale. Under named reliance, materialize five separate findings and one applicability finding.
4. State the aggregate applicability result directly in the recommendation; when a reliance-bearing applicability finding exists, the two result values agree.
5. Recommend an applicable candidate only when its result and receiving use answer the current concern better than the live alternatives.
6. Coordinate several candidates as unordered, partially ordered, or totally ordered. Add a pairwise relation only when one declared precedence basis is current.
7. Stop at the recommendation or coordination result. Continue to PUA, P2W, planning, gate, decision, or work only when that next claim becomes current.

#### E.11.PUR:4.6 - Replay and currentness

Replay an ordinary compact recommendation from its candidate, applicability result, compact rationale over all five aspects, current live alternatives, expected result and receiving use, and recommendation boundary. Replay a reliance-bearing recommendation from those same positions plus the current applicability finding and its five fit findings. Replay coordination from its members, question, ordering mode, pairwise relations, precedence bases, and stop boundary.

Recheck the smallest affected finding or relation when a candidate `Solution`, result expectation, fit basis, live alternative, receiving use, coordination member, precedence basis, or boundary changes. A changed candidate fit reopens its applicability and any recommendation that relied on it. A changed prerequisite expectation reopens only the affected ordering relations and their dependent uses unless the coordination question or membership also changed. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; PUR supplies the judgement-specific values and change conditions.

### E.11.PUR:5 - Archetypal Grounding

#### E.11.PUR:5.1 - Applicable but not recommended

A team considering a high-cost pump test has candidate uses of `C.28` causal triage and `A.21` gate discipline. Both may be applicable. The immediate uncertainty is whether a causal model output may support intervention, so `C.28` offers the more useful first result.

Recommend `C.28` without claiming that the test is authorized. The later gate use remains a separate candidate whose applicability can be reconsidered after the causal-use result exists.

Because this local recommendation is reversible and no later use relies on five separate findings, the team records `recommendationSupportProfile=ordinaryCompact`, the applicability result, and one compact rationale over all five aspects. If a later gate review needs to replay each aspect independently, that review may create current fit findings and a current applicability finding from the then-current basis. It does not claim that those addressable findings existed when the earlier compact recommendation was made; the original compact rationale remains its historical basis.

#### E.11.PUR:5.2 - Unordered complementary uses

A clinical team needs both a terminology repair and an evidence-basis review before revising a protocol. Neither result is a prerequisite for the other in the current context.

Use one coordination relation with `orderingMode=unordered`. The team may perform the uses in either order or in parallel. Their coexistence does not create a lifecycle or WorkPlan.

#### E.11.PUR:5.3 - Result-based precedence

A design team's architecture-candidate comparison begins only after its evaluation coordinates are defined. One candidate use of `A.19.ECS` expects an `EvaluationCharacteristicSpaceSpec`; the dependent comparison use consumes that exact result.

Use `precedenceBasis=prerequisiteResult` and point to the ECS candidate's existing expectation. Do not copy `EvaluationCharacteristicSpaceSpec` and its signature into new ordering fields. After the result is grounded, the dependent use can begin under its own Solution.

#### E.11.PUR:5.4 - Method precondition is not a result dependency

A machining pattern assumes an admitted material-kind classification. The classification is a method precondition already current in the bounded context, not the result of another candidate pattern use.

If coordination is still useful, use `methodPrecondition` and leave the result-expectation position absent. Do not invent a prerequisite result merely to make the relation look uniform.

#### E.11.PUR:5.5 - Repair a stale copied prerequisite locally

An older architecture coordination copied `EvaluationCharacteristicSpaceSpec` and its signature into an ordering record. The ECS candidate's current expectation later changed, leaving the copy stale while both candidates, their applicability findings, the coordination question, and `partialOrder` mode remained sound.

Repair only the ordering relation: remove the copied result description, set `precedenceBasis=prerequisiteResult`, and reference the ECS candidate's current expectation. The dependent use returns until that expected result is grounded. Candidate inspection, applicability, coordination membership, and direct Solutions do not restart.

#### E.11.PUR:5.6 - A higher recommendation score can reduce useful fit

An assistant ranks candidate pattern uses by historical recommendation acceptance. The familiar `A.21` gate candidate receives a higher score and is recommended first more often for causal-use uncertainty. Recommendation acceptance rises, but wrong-turn returns also rise because the needed `C.28` causal-use result is still absent.

The score improved while first-result fit and receiving-use value worsened. Keep the historical score as telemetry, apply `E.13` to the substitution, and base recommendation on current applicability, expected result, receiving use, and live alternatives. A higher score is not another fit finding.

### E.11.PUR:6 - Bias-Annotation

- **Applicability-as-recommendation bias.** A fitting pattern is automatically selected. Compare the expected practical result and live alternatives before recommending it.
- **Favorite-pattern proxy bias.** Familiar PatternID substitutes for current value. State the concern, expected result, and receiving use in the rationale.
- **Five-form bias.** Every ordinary use creates five findings. Keep them in one compact rationale unless their separate identity is relied on.
- **Sequence bias.** Presentation order becomes precedence. Repair by naming the pairwise basis.
- **Result-copy bias.** Prerequisite result kind is duplicated in ordering fields. Reuse the prerequisite candidate's exact expectation.

### E.11.PUR:7 - Conformance Checklist

| ID | Check | Passing condition |
| --- | --- | --- |
| `PUR-1` | Candidate basis | Every evaluated candidate has an inspected Solution and exact result expectation. |
| `PUR-2` | Five aspects | Reliance-bearing applicability has exactly one finding for each fit criterion. |
| `PUR-3` | Aggregate | Every recommendation states an applicability result after all five aspects are considered. When a reliance-bearing applicability finding exists, its result agrees with the recommendation and carries a missing-basis boundary when needed. |
| `PUR-4` | Recommendation | Recommended candidate is applicable and its result answers the current concern under a compact explicit rationale. `ordinaryCompact` has no applicability-finding ref; `relianceBearing` has one current finding with five addressable fit findings. |
| `PUR-5` | Coordination | All members concern the same bounded coordination question and have distinct candidate identities. |
| `PUR-6` | Ordering mode | Unordered has no pairwise relations; partial and total order contain only justified pairwise relations. |
| `PUR-7` | Exact precedence | `prerequisiteResult` reuses the prerequisite candidate's expectation; other basis values leave that position absent. |
| `PUR-8` | Boundary | Recommendation or coordination does not assert plan, work, gate, decision, authorization, or subject result. |

### E.11.PUR:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails | Repair |
| --- | --- | --- |
| Recommend before aggregating fit | A partial match is overread as selection. | Resolve all five aspects or return `insufficientBasis`. |
| Rank every candidate | A scalar order hides complements and incomparable results. | Use unordered or partial coordination when that matches the current relation. |
| Use sequence as WorkPlan | Pattern-use relations acquire dates, resources, and work authority they do not own. | Create an A.15.2 WorkPlan only when intended work is current. |
| Copy the prerequisite result | Duplicated kind and signature can drift from the candidate expectation. | Reference the exact expectation. |
| Treat recommendation as authorization | Guidance bypasses evidence, gate, commitment, or work governance. | Continue to the direct governing pattern for the stronger claim. |

### E.11.PUR:9 - Consequences

**Benefits.** A team can explain why a pattern fits, why it is recommended, and how several uses relate without creating a false workflow. Reliance-bearing decisions remain replayable. Result-based precedence stays synchronized with the candidate expectation.

**Costs.** Consequential recommendations need explicit rationales and sometimes five addressable findings. Partial orders need pairwise relations. Ranking candidates that solve different questions produces an inadmissible comparison rather than a useful shortcut.

### E.11.PUR:10 - Rationale

Applicability, recommendation, and coordination answer different questions. Applicability asks whether a candidate's conditions hold. Recommendation asks which applicable use best serves the current concern. Coordination asks how several candidate uses belong together. Keeping the questions separate prevents a familiar label or score from becoming an unexamined decision.

Pairwise precedence is intentionally narrow. A graph of pattern uses can be unordered, partially ordered, or totally ordered. Only a current dependency justifies an edge, and only a prerequisite result justifies a result-expectation reference. This preserves graph structure without turning every explanation into a chain.

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
- **Coordinates with:** `E.11` for public discovery, `A.19` and `A.19.ECS` for subject comparison, `E.18.1` for P2W, `G.11` for currentness orchestration, and the direct pattern governing any plan, work, gate, evidence, decision, or authorization claim.
- **Leads to:** `E.11.PUA` for applying the recommended pattern, or to the exact neighboring pattern when the recommendation makes a stronger subject claim current.

### E.11.PUR:End

