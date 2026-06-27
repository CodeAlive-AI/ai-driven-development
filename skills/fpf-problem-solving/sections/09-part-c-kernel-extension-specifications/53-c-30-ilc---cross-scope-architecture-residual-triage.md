## C.30.ILC - Cross-Scope Architecture Residual Triage

> **Type:** Architectural subpattern under C.30
> **Status:** Stable
> **Normativity:** Normative for FPF pattern, companion-text, and project-description use that claims architecture-specific residuals across declared scopes.

### C.30.ILC:1 - Problem frame

Use this pattern when a project situation contains a cross-scope architecture residual for a described holon, often described in project speech as:

```text
"Optimization at the component scope breaks the wider holon."
"We added modularity, but integration exceptions grew."
"Local agent autonomy conflicts with the control or policy scope."
"At one scale window the architecture is stable; at the next, bespoke bridges appear."
"The team optimizes latency, but the evidence or assurance scope becomes unrepairable."
"We may need to add, split, or mediate a declared holon level, declared scope, control layer, interface grammar, work scope, or evidence scope, but it is not clear which architecture move is admissible."
```

**First-minute use slice.** A robotics team says a local controller upgrade made each arm faster, but cell-level stoppages and audit exceptions grew. Before drawing another architecture view, C.30.ILC records: described holon = assembly cell; declared levels and scopes = arm controller, cell control, evidence scope; level-bearing selected structure = control and evidence-reuse structure; residual-bearing locus = control-rate conflict plus evidence-reuse failure; local repair already attempted = retuned each arm controller; first architecture move = add or change mediator relation or control-layer relation and apply `C.30.ASV` for the selected structural view.

The first useful move is `CrossScopeArchitectureResidualTriageRecord@Context`: name the affected declared holon levels or declared scopes, the selected structure in which those levels or scopes are recoverable, residual-bearing locus, local repair already attempted, why local repair is insufficient, and the first admissible architecture move or governing-pattern application.

The primary `EntityOfConcern` is the cross-scope or interlevel architecture residual in the described holon or holon family under a bounded context. The described holon may be an admitted system, organization-as-system, episteme, work occurrence, bounded context, discipline, or another admitted holon kind. Publication-family material enters through episteme and publication owners; method descriptions enter as epistemes; method values enter through their method owner and relation slots. A phrase in a description, a diagram label, or a mathematical-lens output may make the residual visible, but it is not the residual itself and does not become the center of this pattern.

`InterlevelConflict@Context` applies when two or more declared holon levels, declared scopes, or level-bearing structure relations of the same described holon or holon family impose incompatible or tensioned constraints, objectives, admissibility conditions, tempos, resource allocations, information-transfer relations, or assurance requirements. Examples include declared system levels, declared episteme levels, aggregation scopes, typed control layers, declared organizational scopes, work scopes, evidence scopes, system scopes, environment scopes, description-use scopes, publication-use scopes, or other declared scopes. A selected structure matters here only when it carries, separates, or relates the declared levels or scopes. A conflict between structures belongs in C.30.ILC only when those structures are assigned to different declared holon levels, declared scopes, scale windows, or coarse-graining steps; a same-level, same-scope, or unassigned conflict between structures belongs elsewhere until a level, scope, scale-window, or coarse-graining assignment is recovered.

`FrustrationResidual` applies when a persistent cross-scope or interlevel residual remains after local repairs have been attempted or deemed insufficient: local optimization in one declared holon level or declared scope improves local fit while degrading, blocking, or destabilizing another declared holon level, declared scope, or level-bearing structure relation.

`ComplexityGrowthPressure` is admitted only as conditional architecture pressure: reducing an interlevel residual may require adding, splitting, mediating, or stabilizing a declared holon level, declared scope, aggregation scope, interface grammar, control loop, evidence scope, work-method scope, abstraction scope, source-return scope, or declared system level when that special case is being claimed. It is not a claim that complexity is good or that complexity necessarily grows.

Entry condition: if declared holon levels or declared scopes, the selected structure or architecture structure kind that carries them, one residual-bearing locus, and one first admissible architecture move cannot be named for the described holon in context, keep the issue at ordinary problem framing or `ProblemCard@Context`; do not claim `CrossScopeArchitectureResidualTriageRecord@Context` yet.

What goes wrong if C.30.ILC is missed: a local improvement, control layer, scale label, interface grammar, or evidence reuse is treated as whole-holon architecture adequacy while the residual moves into another declared holon level or declared scope.

What this buys: the practitioner can name the residual-bearing locus, the declared levels or scopes, the local repair already attempted, and one first architecture move without turning multilevel frustration, scale, ethics, evidence, or mathematical-lens use into this pattern's object.

What C.30.ILC buys in practice: the practitioner can keep useful conflict or frustration language as an entry label while governing the architecture residual itself: affected holon levels or scopes, the selected structure that carries them, residual-bearing locus, and one admissible architecture move or governing-pattern application.

`Interlevel conflict` and `frustration` may appear in ordinary project descriptions, but the conforming record governs the residual through declared holon levels or declared scopes, the selected structure that carries them, and a residual-bearing locus. The pattern does not create a generic level scale or `U.Frustration`. It asks which declared holon level, declared scope, aggregation scope, control layer, organizational scope, work scope, evidence scope, system scope, environment scope, scale window, interface grammar, allocation boundary, publication section, or source-return condition bears the residual. A system level or episteme level is a special case of a declared holon level.

Not this pattern when the issue under repair is only ethical value framing, interlevel ethical conflict structure, ethical mediation or decision use, measurement, scale relation, coarse-graining relation, mathematical-lens validation, candidate generation, residual-reducing candidate-set work, final selection, causal outcome, evidence, or assurance. Use the governing pattern and keep C.30.ILC only to the architecture residual-bearing locus.

### C.30.ILC:2 - Problem

Architecture work often starts from a residual: a local fix works in one declared holon level or declared scope and fails in another. Component optimization increases whole-holon or product-line integration cost. A new module boundary reduces local complexity and increases exceptions at the product-line scope. A control layer improves local safety and creates accountability or latency claims elsewhere. A reusable evidence set reduces repeated work and hides a new source-return condition.

The useful architecture intuition is narrower than a new `Frustration` kind: local optimization at one declared holon level or declared scope can create a persistent residual in another declared holon level, declared scope, or level-bearing structure relation. Depending on the claim being made, that residual is governed by `C.29` only when a recoverable multilevel mapping, scale mapping, or coarse-graining mapping is being claimed; by `C.31.ASAP` when architecture scale preference over declared alternatives is being claimed; by `C.32.MLAO` and `C.32` when residual-reducing candidate architecture work is current; and by `G.5` only when selected-set publication is current. An ordinary conflict between structures is not enough for the RG lens or frustration mathematical lens, but a conflict between structures assigned to different declared holon levels or scale windows may be enough when the mapping, preserved-structure line, and lost-structure line are recoverable. The first C.30.ILC output is only the grounded triage record.

Without a pattern, teams either discuss the residual as vague `complexity`, treat it as an ordinary negotiation problem, jump into measurement, use mathematical frustration language as proof, or jump to candidate generation too early. `C.30.ILC` keeps the first move small: identify whether the residual is architecture-shaping and name the first admissible architecture move or governing-pattern application.

The practical work is often not to draw another view. It is to assign the residual to the locus named by value that can bear it: declared holon level, declared scope, level-bearing selected structure, structure kind, constraint, characteristic or Q-bundle, evidence-reuse boundary, source-return condition, or non-architecture claim kind.

### C.30.ILC:3 - Forces

* Local optimization can be real and still be harmful at another declared holon level or declared scope.
* `Level`, `layer`, `scope`, `scale`, `abstraction`, `organization`, `system`, and `environment` labels can sound precise while naming different project-side entities, relations, scopes, or claim kinds.
* Frustration language can be useful because it points to incompatible constraints or fitness contributions, but it can also smuggle a physics, biology, psychology, or global-optimizer ontology into architecture prose.
* Measurement is tempting because the residual feels numeric, but a measure before declared-scope and structure-kind recovery can hide the real conflict.
* Ethical conflict or mediation may be present, but not every cross-scope residual is an ethical conflict or mediation problem.
* Architecture synthesis may be needed, but a small triage output often identifies a narrower move: split scope, add mediator, add interface grammar, change allocation, expose coupling, add evidence scope, accept bounded exception, or return to source.
* The pattern is not a prescribed sequence of moves; architecture work is often case-managed through loops, checks, and dead ends.

### C.30.ILC:4 - Solution

Create a `CrossScopeArchitectureResidualTriageRecord@Context` when an architecture concern is carried by residuals across declared holon levels, declared scopes, or level-bearing structure relations.

```text
CrossScopeArchitectureResidualTriageRecord@Context ::= {
  describedHolonRef,
  boundedContextRef,
  architectureConcernCue,

  declaredHolonLevelRefs?: FinSet(DeclaredHolonLevelRef),
  declaredScopeRefs: FinSet(AggregationScopeRef | DeclaredSystemLevelRef |
                            ControlLayerRef | WorkEvidenceScopeRef |
                            OrganizationScopeRef | SystemEnvironmentScopeRef |
                            RateBandRef | ScaleWindowRef |
                            PublicationSectionRef | OtherDeclaredScopeRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),

  interlevelConflictDescription?,
  conflictCarrierRefs?:
    FinSet(ConstraintRef | ObjectiveRef | AdmissibilityConditionRef |
           TempoRef | ResourceAllocationRef | InformationTransferRelationRef |
           AssuranceRequirementRef | OtherDeclaredConflictCarrierRef),
  localScopeOptimizationClaim?,
  widerScopeOptimizationClaim?,
  conflictingConstraintRefs?,
  conflictingCharacteristicRefs?,
  conflictingQBundleRefs?,

  symptom,
  crossScopeResidualDescription,
  crossScopeResidualLocusKind:
    hiddenCoupling | interfaceException | controlRateConflict |
    scaleWindowLoss | evidenceReuseFailure | regulatoryBespokeResidue |
    workMethodException | dataSemanticDrift |
    placementJurisdictionConflict | securityTrustBoundaryBreak |
    otherDeclared,
  frustrationResidualBefore?,
  complexityGrowthPressure?,
  localRepairAttempted?,
  whyLocalRepairInsufficient?,

  firstAdmissibleArchitectureMove:
    splitDeclaredHolonLevel | mergeDeclaredHolonLevel |
    splitDeclaredScope | mergeDeclaredScope |
    splitDeclaredSystemLevel | mergeDeclaredSystemLevel |
    addMediator | addInterfaceGrammar | addControlLayer |
    addEvidenceScope | addWorkMethodScope | changeAllocation |
    exposeHiddenCoupling | acceptBoundedException |
    applyD3D4 | applyC28 | noArchitectureMove,

  triggeredGoverningPatternRefs?,
  admissibleNextMove,
  stopCondition,
  sourceReturnCondition?
}
```

**Layer, level, tier, stack, and declared-scope labels.** `Declared holon level` is the general level-bearing recovery field for this pattern; system level and episteme level are special cases when the described holon or selected structure makes them relevant to the claim. `System level` may remain as ordinary recognition language when a practitioner would naturally use it, but the record recovers the project-side scope references through `declaredHolonLevelRefs` or `declaredScopeRefs`; a system level is not the default architecture level. When the source says layer, level, tier, or stack, recover exactly one or more of: `declaredHolonLevelRef`, `controlLayerRef`, `declaredSystemLevelRef`, `aggregationScopeRef`, `rateBandRef`, `organizationLevelRef`, `workEvidenceScopeRef`, `scaleWindowRef`, or `publicationSectionRef` when the wording only names a document layer. A move such as `splitDeclaredHolonLevel`, `splitDeclaredScope`, or, in the special system-level case, `splitDeclaredSystemLevel` is admissible only when the affected declared holon level, declared scope, selected structure, declared system level, aggregation scope, control layer, organization scope, work scope, evidence scope, system scope, environment scope, rate band, scale window, publication section, or source-return condition is named. A layer label is not a structure kind, not a system level, not a rate band, and not evidence of separation by itself.

**Interlevel conflict, frustration residual, and complexity-growth recovery.** A conflict is architecture-shaping only when the record names the declared holon levels or declared scopes, the selected structure or structure kind that carries them, and the conflict carrier: constraint, objective, admissibility condition, tempo, resource allocation, information-transfer relation, or assurance requirement. A frustration residual is architecture-shaping only when local repair or local optimization leaves a persistent residual in another declared holon level, declared scope, or level-bearing structure relation. Complexity-growth pressure is only a candidate reason to add, split, mediate, or stabilize structure when that change is expected to reduce the residual enough to justify the new cost and its own residue.

`crossScopeResidualDescription` is not enough by itself. A residual becomes architecture-shaping only when its residual-bearing locus is declared: hidden coupling, interface exception, control-rate conflict, scale-window loss, evidence-reuse failure, regulatory bespoke residue, work-method exception, data-semantics drift, placement or jurisdiction conflict, security trust-boundary break, or another declared locus.

**Multilevel optimization boundary.** `C.30.ILC` can recognize that local optimization in one declared holon level or declared scope degrades another declared holon level or declared scope. It does not optimize the architecture and does not prove that one global function exists. Use `C.29` with `MLU.Description@MultilevelLearningFrustration` only when the mathematical representation supplies a recoverable mapping between declared levels, scopes, scale windows, or coarse-graining steps and states what structure is preserved and lost. Conflicting structures can enter this lens only when each structure is assigned to a declared holon level, scope, scale window, or coarse-graining step and the mapping shows why the conflict is interlevel. If scale window, RG relation, coarse-graining relation, preserved structure, lost structure, or conflict residual slope becomes an architecture scale-preference claim, use `C.31.ASAP` and keep any mathematical-lens claim in `C.29`. If the practitioner needs to generate or compare residual-reducing candidate architecture moves, apply `C.32.MLAO` for the residual-reducing multilevel candidate frame and `C.32` for the candidate palette. Use `G.5` only when selected-set publication is current, `C.11` when final local choice is current, and `C.32.PAD` when project architecture decision is current; `C.30.ILC` stops at the residual and first admissible move. If the case is only a conflict between two selected structures with no declared multilevel mapping or scale mapping, keep it in `C.30`, `C.30.ASV`, `D.3`, `D.4`, `C.28`, evidence, assurance, or decision patterns as applicable.

Anti-collapse rule: no generic frustration score, no risk-matrix residual, no ethical-mediation takeover, no physics or biology ontology transfer, no global-optimizer proof, no causal proof, and no assurance proof. A frustration or risk label does not govern the case until declared holon levels or declared scopes, the selected structure or structure kind that carries them, residual-bearing locus, and first architecture move are recoverable; `D.3` applies only when interlevel ethical conflict structure is current; `D.4` applies only when mediation or decision use of that structure is current.

**Stop condition.** Stop after `CrossScopeArchitectureResidualTriageRecord@Context` when it names the residual and the first admissible architecture move. It does not measure scale preference, generate candidate architectures, mediate ethical conflict, or select a decision. Apply a governing pattern only when a claim kind being made exists:

| Claim kind being made | Governing pattern to apply |
|---|---|
| measurement or characteristic claim | `C.16` or the characteristic pattern that governs the characteristic under evaluation |
| scale window, RG relation, coarse-graining relation, preserved structure, lost structure, or conflict residual slope | `C.31.ASAP` when an architecture scale-preference claim is being made; use `C.29` when mathematical-lens use is being claimed |
| multilevel learning or frustration mathematical-lens use with recoverable level mapping or scale mapping | `C.29` with `MLU.Description@MultilevelLearningFrustration` |
| candidate generation or residual-reducing candidate architecture moves | `C.32.MLAO` when the residual-reducing multilevel frame is current; `C.32` for the candidate palette; `G.5` when selected-set publication is current; `C.11` when final local choice is current; `C.32.PAD` when project architecture decision is current |
| final local choice | `C.11` |
| causal outcome claim | `C.28` |
| evidence or assurance | `A.10`, `B.3`, or `G.6` |
| ethical conflict structure, mediation, or decision use | `D.3` for interlevel ethical conflict structure; `D.4` for mediation and decision use of that structure |

**D.3 and D.4 boundary.** `D.3` handles interlevel ethical conflict structure: affected holons, systems, epistemes, collections, declared levels or scopes, interests or concerns, value frames, agency or responsibility thresholds, methods, work, transformations, evidence, uncertainty, and consequence horizons. `D.4` handles mediation and decision use of that `D.3` structure: mediation, refusal, evidence demand, causal return, assurance return, architecture return, accepted residual, and bounded decision use. `C.30.ILC` handles architecture-specific recognition: whether the conflict or residual is borne by declared holon levels or declared scopes inside a selected structure such as structural views, allocation, interfaces, control rates, work reuse, evidence reuse, scale windows, or coarse-graining loss. It is a triage and architecture-move pattern, not an ethical mediation pattern.

**Architecture-move examples.**

| Cue | Admissible architecture move | Non-admissible overread |
|---|---|---|
| Component optimization breaks integration | expose hidden coupling; add interface grammar; change allocation | Treat local performance as whole-holon adequacy. |
| Modularity reduces local work and increases exceptions | accept bounded exception; revise module boundary; add work scope or evidence scope | Average exceptions into a modularity score without declared scope, comparator, and measurement relation. |
| Local autonomy conflicts with control scope | add control layer; change allocation; apply `C.30.LCA` | Treat autonomy label as causal or safety proof. |
| Evidence reuse hides source loss | add evidence scope; add source-return condition; apply `A.10` or `G.6` | Treat reused evidence as automatically valid in the wider scope. |
| A scale window changes the residual | apply `C.31.ASAP`, with `C.29` when scale-lens use is being made | Treat two observations as a universal scale law. |
| A frustration lens with recoverable level mapping or scale mapping makes candidate moves comparable | use `C.29` for lens adequacy; use `C.32.MLAO` and `C.32` when a residual-reducing candidate palette is current; use `G.5` only when selected-set publication is current | Treat an unassigned or same-scope structure conflict as RG mathematics or frustration mathematics, or treat an interlevel residual without recoverable mapping as a global optimizer, proof, or selected architecture. |

**Worked slice A - clean module layout, bad flow.** A product team redraws modules so each component has an explicit responsibility relation or enactor relation, but order-to-cash flow now crosses more work transfers and exceptions rise. `C.30.ILC` names the module structure, transformation-flow structure, affected work scope, cross-scope residual, and first move: expose hidden coupling or apply `C.30.TFS-REL`. It does not turn the exception count into a modularity measure until `C.16` or the characteristic pattern governing the characteristic under evaluation is applied.

**Worked slice B - AI agent control conflict.** A local agent optimizes its local objective and violates a supervisor's allowed-mode constraint. `C.30.ILC` names the agent scope, supervisor scope or control scope, control relation, local optimization claim, residual-bearing locus, and local repair attempted. The first move may be add control layer, change allocation, or apply `C.30.LCA`. Safety, causality, and gate claims use their governing patterns.

**Worked slice C - evidence scope residue.** A reusable certification evidence set removes repeated evidence work for several product variants, but one variant has a hidden environment difference. `C.30.ILC` names the work scope or evidence scope and source-return condition. The practitioner applies `A.10` or `G.6` when an evidence-validity claim is being made.

**Worked slice D - frustration residual before synthesis.** Several decompositions reduce local module work but each creates a different integration, control-rate, or evidence-reuse residual in another declared scope. `C.30.ILC` records the residuals and first architecture moves. If the team needs a residual-reducing candidate palette, stop the C.30.ILC use and apply `C.32.MLAO` for the residual-reducing frame and `C.32` for the candidate palette. Use `G.5` only when the palette or retained set must become a public selected-set result. If the team claims a multilevel-learning lens or frustration lens, `C.29` carries the lens-use fields and stop condition only after the level mapping, scope mapping, scale-window mapping, or coarse-graining mapping and preserved structure and lost structure are recoverable.

### C.30.ILC:5 - Archetypal Grounding

| Archetype | Without C.30.ILC | With C.30.ILC |
|---|---|---|
| Holon levels | A residual across component, system, episteme, publication-use, control, environment, or product-line scopes is called generic complexity. | The affected declared holon levels or declared scopes, the level-bearing structure, the residual, and the first architecture move are named. |
| Episteme as described holon | A diagram, measurement note, or conflict memo has its own structure, but a second description about it is interpreted as if it already selected a repair. | The episteme can be the described holon; the description of that episteme remains separate from decision, evidence, measurement, selection, or mediation and is governed by the governing pattern when those claims are being made. |

### C.30.ILC:6 - Bias-Annotation

* **Local-success bias.** A local improvement is treated as whole-architecture improvement. Repair by naming the wider declared holon level or declared scope and the residual.
* **Pseudo-level bias.** `Level`, `layer`, or `scope` sounds precise but no declared holon level or declared scope exists. Repair through `declaredHolonLevelRefs` or `declaredScopeRefs`.
* **Generic-structure-conflict bias.** A conflict between selected structures is treated as interlevel conflict even though no declared holon level, scale window, or coarse-graining relation is recoverable. Repair by keeping the case in `C.30`, `C.30.ASV`, or the governing pattern unless the structures are assigned to different declared holon levels or scale windows.
* **Frustration-ontology bias.** A useful conflict or frustration entry label becomes a new first-order architecture kind, physics ontology, biology ontology, or psychology claim. Repair by recovering declared holon levels or declared scopes, the level-bearing structure, conflict carriers, residual-bearing locus, and the governing pattern for any lens, proof, evidence, mediation, or synthesis claim.
* **Global-optimizer bias.** Local optimization in one declared holon level or declared scope is used as if the architecture literally optimizes one global function. Repair by keeping the local optimization claim as a triage input unless `C.29` supplies an admissible mathematical-lens use with recoverable level mapping or scale mapping and the candidate-set or decision pattern carries any synthesis or selection claim.
* **Measurement-first bias.** A residual is measured before its level-bearing structure and scope grounding are declared. Repair by applying `C.16` or the characteristic pattern governing the characteristic under evaluation only after triage names the affected characteristic or measurement relation.
* **Mediation-default bias.** Every conflict is treated as ethical mediation or negotiation. Repair by checking whether the use under repair is architecture structure, allocation, interface grammar, control, work or evidence scope, source-return, or another declared level-bearing architecture relation.
* **Synthesis-jump bias.** A local residual immediately triggers candidate generation. Repair by identifying the first admissible architecture move before applying `C.32.MLAO` and `C.32`; use `G.5` only when selected-set publication is current.

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, view, relation, or repair guidance above.

### C.30.ILC:7 - Conformance Checklist

| ID | Check | Why it matters |
|---|---|---|
| CC-ILC-1 | A conforming use names `describedHolonRef`, `boundedContextRef`, and the architecture concern cue. | Keeps the triage grounded without narrowing architecture to systems. |
| CC-ILC-2 | A conforming use names declared holon levels or declared scopes, not only `level`, `layer`, `scope`, or `scale` prose. | Prevents pseudo-level and pseudo-scope reasoning. |
| CC-ILC-3 | A conforming use names the selected structure or structure kind that carries, separates, or relates the declared levels or scopes affected by the residual. | Keeps the residual interlevel rather than merely a same-level, same-scope, or unassigned conflict between structures. |
| CC-ILC-4 | A conforming use records conflict carriers, local repair attempted, and why local repair was insufficient when a conflict or local repair is claimed. | Prevents premature synthesis and repeated local fixes. |
| CC-ILC-5 | A conforming use states one first admissible architecture move or `noArchitectureMove`. | Makes the output action-guiding without candidate generation. |
| CC-ILC-6 | Evidence, assurance, measurement, causal, ethical, selection, scale, RG, coarse-graining, mathematical-lens, and residual-reducing candidate-set claim kinds use their governing patterns. | Prevents triage from becoming proof, lens adequacy, mediation, synthesis, or selection. |
| CC-ILC-7 | If a source-return condition is needed, the record states what hidden or lost distinction triggers return to the source. | Protects compressed and extracted views. |
| CC-ILC-8 | The stop condition is visible. | Prevents the triage pattern from expanding into a hidden prescribed sequence. |
| CC-ILC-9 | If multilevel learning or frustration is used as mathematics, the record names `C.29`, `MLU.Description@MultilevelLearningFrustration`, the recoverable level mapping or scale mapping, and preserved structure and lost structure; if residual-reducing candidate moves form a candidate set being used, the record names `C.32.MLAO` and `C.32`; if the retained set is being published, it names `G.5`. | Preserves the useful multilevel optimization line without importing ontology, proof, or a hidden selector. |

### C.30.ILC:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Generic complexity bucket | Everything becomes `complexity` or `interlevel conflict`. | Name declared holon levels or declared scopes, level-bearing structure, residual, and first architecture move. |
| Structure conflict as interlevel conflict | Two structures are in tension, but no declared holon level, scale window, or coarse-graining relation is recoverable. | Use `C.30`, `C.30.ASV`, `D.3`, `D.4`, `C.28`, evidence, assurance, or decision patterns as applicable; use C.30.ILC only when the conflict is across declared levels or scopes. |
| Frustration-as-ontology | `Frustration` is treated as a new FPF kind, psychological state, physics kind, biology kind, assurance score, or proof. | Keep frustration as an entry label; recover `FrustrationResidual`, conflict carriers, residual-bearing locus, and governing patterns for `C.29`, evidence, assurance, causal, mediation, or synthesis claims when those claim kinds are being made. |
| Optimization-as-global-proof | A local optimization claim is treated as proof that the whole architecture optimizes one global objective. | Record local and wider-scope claims separately; use `C.29` only for an admissible mathematical lens with recoverable level mapping or scale mapping and use candidate-generation, comparison, or decision patterns for synthesis and selection. |
| Measurement-first conflict | The team starts measuring before declaring what is in conflict. | Run ILC triage first; apply `C.16` or the characteristic pattern governing the characteristic under evaluation only when the measured characteristic is under evaluation. |
| Risk color as cross-scope decision | A red, yellow, or green risk cell, risk matrix, or maturity score decides the cross-scope architecture move or resource-allocation priority. | Recover declared holon levels or declared scopes, structure kind under considerations, the residual, the loss, hazard, or threat relation, selected source, evidence, or relation interpretation, characteristic scale, comparator, gate pattern, and first admissible architecture move; do not treat ordinal risk color as architecture adequacy, evidence sufficiency, causal proof, assurance proof, resource-allocation priority, or gate passage. |
| Mediation-only conflict | A structural residual is treated as ethical mediation with no architecture move. | Use `D.3` only when interlevel ethical conflict structure is current and `D.4` only when mediation or decision use of that structure is current. |
| Hidden candidate generation | The residual immediately spawns many designs. | State the first admissible move; apply `C.32.MLAO` and `C.32` only when residual-reducing candidate work is being claimed, and apply `G.5` only when selected-set publication is current. |
| Scope word without scope record | The text says `level`, `layer`, `scale`, or `scope` without a declared field. | Recover the declared holon level or declared scope named by value, or demote the phrase to ordinary recognition. |

### C.30.ILC:9 - Consequences

The gain is an early architecture move that is small and precise. The practitioner can preserve useful problem language such as conflict, frustration, level, layer, or local optimization while recovering the FPF fields that keep the claim reviewable.

The cost is that `C.30.ILC` refuses to solve the whole problem. It identifies the first architecture move or governing-pattern application. Measurement, scale relation, RG relation, coarse-graining relation, mathematical lens use, ethical mediation, candidate generation, evidence, assurance, and final choice remain outside until those claims are being made.

This makes multilevel optimization usable rather than decorative. `C.30.ILC` identifies the residual that makes optimization relevant; `C.29` carries an admissible mathematical-lens use only when level mapping or scale mapping and preserved structure and lost structure are recoverable; `C.32.MLAO` and `C.32` carry residual-reducing candidate frames and palettes; `G.5` carries selected-set publication; and `C.32.PAD` carries any project architecture decision.

### C.30.ILC:10 - Rationale

Interlevel conflict and frustration are useful Plain entry labels because they point to a recurrent architecture failure: local repair in one declared holon level or declared scope leaves a residual in another. They are dangerous as generic labels because they can hide which level, scope, level-bearing structure, relation, conflict carrier, or source-return condition bears the residual.

A local optimum or successful local repair is therefore not treated as whole-architecture adequacy. It becomes architecture-relevant only when the residual-bearing locus is recoverable and the next architecture use can be named.

`C.30.ILC` keeps the entry label but recovers the architecture relation or structure claim. It treats conflict or frustration as architecture-shaping only when declared holon levels or declared scopes, the level-bearing structure, conflict carriers, and residual-bearing loci are named. This lets FPF preserve the practical intuition without introducing a second ontology of levels, a hidden measurement pattern, a physics or biology transfer, a global optimizer proof, or a prescribed architecture work order.

### C.30.ILC:11 - SoTA-Echoing

| SoTA and practice source | What it contributes | FPF adoption stance | Practitioner implication |
|---|---|---|---|
| Scenario-based architecture trade-off practice, with ATAM-like reasoning used here as lineage and practice source for concern, scenario, sensitivity point, and trade-off recognition rather than as a decision or evidence method. | Architecture work often starts from cross-concern and cross-scope trade-offs rather than one local measurement result. | Adopt and adapt: use the conflict cue for triage, require declared holon levels or scopes, level-bearing structure, and governing patterns for final selection, evidence, assurance, and gate passage. | A residual can start an architecture move without becoming a decision, proof, or safety case. |
| Vanchurin, Wolf, Katsnelson, and Koonin multilevel learning and frustration line, plus the Akhtyrchenko, Katsnelson, and Ustyuzhanin 2026 MSPD paper as selected source pressure rather than full-literature ranking. | Local optimization at one declared holon level, scope, or level-bearing structure relation can create persistent residual in another; frustrated optimization and MSPD-like reasoning can be candidate mathematical lenses when a level mapping or scale mapping is recoverable. | Adopt and adapt: `C.30.ILC` uses this line for architecture triage only. `C.29` with `MLU.Description@MultilevelLearningFrustration` carries mathematical-lens adequacy with preserved structure and lost structure; no `U.Frustration`, universal architecture metric, physics or biology ontology transfer, global optimizer proof, causal proof, assurance proof, or ethical-mediation takeover. | First recover holon levels or scopes, level-bearing structure, conflict carriers, residual-bearing locus, local repair, and the first architecture move. Apply `C.29` only when the lens mapping is being claimed; apply `C.32.MLAO` and `C.32` only when residual-reducing candidate work is current; apply `G.5` only when selected-set publication is current. |
| Control and cyber-physical systems practice. | Local autonomy, feedback, supervisor relations, and rate separation can create cross-scope conflict. | Reuse through `C.30.LCA`, `B.2.5`, `C.27`, and `A.3.3`; do not let ILC carry control proof. | A control conflict is governed by control-structure or dynamics patterns only when those claims are being made. |
| FPF source-return and semantic-coarsening discipline. | Compressed views and reusable records can hide distinctions that matter in a wider scope. | Adopt: add `sourceReturnCondition?` when hidden distinctions carry the residual. | A bounded exception or source-return trigger may be the correct first move. |

### C.30.ILC:12 - Relations

* Builds on `C.30` and `C.30.ASV` for grounded architecture, selected-structure, and structural-view adequacy.
* Uses `A.22` for structure and structural-view discipline.
* Coordinates with `C.30.TFS-REL`, `C.30.LCA`, `A.6.F`, and `A.6.M` when the residual concerns flow, control, function, allocation, module, or interface structure.
* Applies `C.16` or the characteristic pattern that governs the characteristic under evaluation for measurement or characteristic claims.
* Applies `C.29` with `MLU.Description@MultilevelLearningFrustration` only when multilevel learning or frustration is used as a mathematical lens with recoverable level mapping or scale mapping and preserved structure and lost structure; applies `C.31.ASAP` for architecture scale-preference claims and `C.29` for mathematical-lens claims when scale, RG, coarse-graining, preserved structure, lost structure, or scale-window adequacy is being claimed.
* Applies `C.32.P2S` when residual triage must continue through problem-to-structure architecturing; applies `C.32.MLAO` for residual-reducing multilevel candidate frames and `C.32` for candidate palettes; applies `G.5` only when selected-set publication is current.
* Applies `C.11` for final local choice, `C.28` for causal outcome claims, `A.10`, `B.3`, or `G.6` for evidence or assurance, `D.3` for interlevel ethical conflict structure, and `D.4` for mediation and decision use of that structure.

Neighboring claims stay with their governing patterns: `C.30` for grounded architecture and selected-structure adequacy, `C.30.ASV` for structural-view adequacy, `A.22` for structure and structural-view discipline, `C.30.TFS-REL` for architecture-to-transformation-flow relation, `C.30.LCA` for control-structure view relation, `A.6.F` for function-use repair, `A.6.M` for module-interface repair, `C.16` or the local characteristic pattern for the characteristic under evaluation, `C.29` for mathematical-lens use, `C.31.ASAP` for architecture scale-preference, `C.32.P2S` for problem-to-structure carry-through after residual triage, `C.32.MLAO` and `C.32` for residual-reducing candidate work and candidate palettes, `G.5` for selected-set publication, `C.11` for final local choice, `C.28` for causal use, `A.10`, `B.3`, or `G.6` for evidence or assurance, `D.3` for interlevel ethical conflict structure, and `D.4` for mediation and decision use of that structure. `C.30.ILC` governs only cross-scope architecture residual triage.

### C.30.ILC:End

