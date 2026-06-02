## C.30.ILC - Cross-Scope Architecture Residual Triage

> **Type:** Architectural subpattern under C.30
> **Status:** Stable
> **Normativity:** Normative for FPF pattern, support-text, and project-description use that claims architecture-specific residuals across declared scopes.

### C.30.ILC:1 - Problem frame

Use this pattern when architecture work is triggered by statements such as:

```text
"Optimization at the component scope breaks the wider system."
"We added modularity, but integration exceptions grew."
"Local agent autonomy conflicts with the control or policy scope."
"At one scale window the architecture is stable; at the next, bespoke bridges appear."
"The team optimizes latency, but the evidence or assurance scope becomes unrepairable."
"We may need a declared system level, control layer, mediator, interface grammar, or work/evidence scope, but it is not clear which architecture move is admissible."
```

The first useful move is `CrossScopeArchitectureResidualTriage@Context`: name the affected declared scopes, structure kinds, residual carrier, local repair already attempted, why local repair is insufficient, and the first admissible architecture move or exact governing pattern application.

Entry condition: if declared scopes, at least one architecture structure kind, and one first admissible architecture move cannot be named in one sentence, keep the phrase as an ordinary source cue or `ProblemCard@Context`, not as `CrossScopeArchitectureResidualTriage@Context`.


What goes wrong if C.30.ILC is missed: a local improvement, control layer, scale label, interface grammar, or evidence reuse is treated as whole-architecture adequacy while the residual moves into another declared scope.

What C.30.ILC buys in practice: the practitioner can keep the useful conflict or frustration wording as a Plain source cue, recover the affected scopes and structure kinds, and stop at one admissible architecture move or exact governing pattern application.

`Interlevel conflict` and `frustration` may stay as ordinary source cues, but the conforming record recovers them through declared scopes, structure kinds, and residual carrier. The pattern does not create a generic level scale or `U.Frustration`. It asks which declared system level, aggregation scope, control layer, organizational scope, work/evidence scope, system/environment scope, scale window, interface grammar, allocation boundary, or source-return condition is carrying the residual.

Not this pattern when the live issue is stakeholder negotiation, ethics, measurement, scale/coarse-graining, candidate generation, final selection, causal outcome, evidence, assurance, or mathematical-lens validation. Use `D.3`/`D.4`, `C.16` or an admitted characteristic/measurement receiving pattern, `C.29` or an admitted scale/coarse-graining receiving pattern when that lens is live, `G.5` or an admitted candidate-generation receiving pattern, `C.11`, `C.28`, `A.10`/`B.3`/`G.6`, or `C.29` respectively.

### C.30.ILC:2 - Problem

Architecture work often starts from a residual: a local fix works in one scope and fails in another. Component optimization increases system integration cost. A new module boundary reduces local complexity and increases exceptions at the product-line scope. A control layer improves local safety and creates accountability or latency claims elsewhere. A reusable evidence set reduces repeated work and hides a new source-return obligation.

Without a pattern, teams either discuss the residual as vague `complexity`, treat it as ordinary stakeholder conflict, jump into measurement, or open a new architecture synthesis effort too early. `C.30.ILC` keeps the first move small: identify whether the residual is architecture-shaping and name the first admissible architecture move or exact exact governing pattern application.

The practical work is often not to draw another view. It is to distribute the residual across the carrier that can actually bear it: declared scope, structure kind, constraint, characteristic or Q-bundle, evidence-reuse boundary, source-return condition, or non-architecture claim kind.

### C.30.ILC:3 - Forces

* Local optimization can be real and still be harmful at another declared scope.
* `Level`, `layer`, `scope`, `scale`, `abstraction`, `organization`, and `system/environment` wording can sound precise while naming different objects.
* Measurement is tempting because the residual feels numeric, but a measure before declared scope and structure-kind recovery can hide the real conflict.
* Ethics and stakeholder mediation may be live, but not every cross-scope residual is a mediation problem.
* Architecture synthesis may be needed, but a small triage output often identifies a narrower move: split scope, add mediator, add interface grammar, change allocation, expose coupling, add evidence scope, accept bounded exception, or return to source.
* The pattern is not a prescribed sequence of moves; architecture work is often case-managed through loops, checks, and dead ends.

### C.30.ILC:4 - Solution

Create a `CrossScopeArchitectureResidualTriage@Context` record when an architecture concern is carried by residuals across declared scopes or structure kinds.

```text
CrossScopeArchitectureResidualTriage@Context ::= {
  describedHolonRef,
  boundedContextRef,
  liveArchitectureConcernCue,

  declaredScopeRefs: FinSet(AggregationScopeRef | DeclaredSystemLevelRef |
                            ControlLayerRef | WorkEvidenceScopeRef |
                            OrganizationScopeRef | SystemEnvironmentScopeRef |
                            RateBandRef | ScaleWindowRef |
                            PublicationSectionRef | OtherDeclaredScopeRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),

  localScopeOptimizationClaim?,
  widerScopeOptimizationClaim?,
  conflictingConstraintRefs?,
  conflictingCharacteristicRefs?,
  conflictingQBundleRefs?,

  symptom,
  crossScopeResidualDescription,
  crossScopeResidualCarrierKind:
    hiddenCoupling | interfaceException | controlRateConflict |
    scaleWindowLoss | evidenceReuseFailure | regulatoryBespokeResidue |
    workMethodException | dataSemanticDrift |
    placementJurisdictionConflict | securityTrustBoundaryBreak |
    otherDeclared,
  localRepairAttempted?,
  whyLocalRepairInsufficient?,

  firstAdmissibleArchitectureMove:
    splitDeclaredSystemLevel | mergeDeclaredSystemLevel | addMediator |
    addInterfaceGrammar | addControlLayer | addEvidenceScope |
    addWorkMethodScope | changeAllocation | exposeHiddenCoupling |
    acceptBoundedException | applyD3D4 | applyC28 |
    noArchitectureMove,

  triggeredGoverningPatternRefs?,
  admissibleNextMove,
  stopCondition,
  sourceReturnCondition?
}
```

**Layer, level, tier, stack, and system-level wording.** `System level` may remain as ordinary recognition language when a practitioner would naturally use it, but the record recovers it through `declaredScopeRefs`. When the source says layer, level, tier, or stack, recover exactly one or more of: `controlLayerRef`, `declaredSystemLevelRef`, `aggregationScopeRef`, `rateBandRef`, `organizationLevelRef`, `workEvidenceScopeRef`, `scaleWindowRef`, or `publicationSectionRef` when the wording only names a document layer. A move such as `splitDeclaredSystemLevel` is admissible only when the affected declared system level, aggregation scope, control layer, organization scope, work/evidence scope, system/environment scope, rate band, scale window, publication section, or source-return condition is named. A layer label is not a structure kind, not a system level, not a rate band, and not evidence of separation by itself.

`crossScopeResidualDescription` is not enough by itself. A residual becomes architecture-shaping only when its carrier is declared: hidden coupling, interface exception, control-rate conflict, scale-window loss, evidence-reuse failure, regulatory bespoke residue, work-method exception, data-semantics drift, placement or jurisdiction conflict, security trust-boundary break, or another declared carrier.

Anti-collapse rule: no generic frustration score, no risk-matrix residual, and no stakeholder-mediation takeover. A frustration or risk label is only a cue until declared scopes, structure kinds, residual carrier, and first architecture move are recoverable; stakeholder mediation applies `D.3`/`D.4` only when values, ethical conflict, or negotiation is live.

**Stop condition.** Stop after `CrossScopeArchitectureResidualTriage@Context` when it names the residual and the first admissible architecture move. It does not measure scale preference, generate candidate architectures, mediate stakeholder conflict, or select a decision. Apply an exact governing pattern only when a live claim kind exists:

| Live claim kind | Governing pattern to apply |
|---|---|
| measurement or characteristic claim | `C.16` or an admitted characteristic/measurement receiving pattern |
| scale or coarse-graining claim | `C.29` or an admitted scale/coarse-graining receiving pattern when the scale lens is live |
| candidate generation | `G.5` or an admitted candidate-generation receiving pattern |
| final local choice | `C.11` |
| causal outcome claim | `C.28` |
| evidence or assurance | `A.10`, `B.3`, or `G.6` |
| ethical or stakeholder mediation | `D.3` / `D.4` |
| mathematical-lens transfer | `C.29` |

**D.3/D.4 boundary.** `D.3` and `D.4` handle conflict topology, values, stakeholder mediation, and ethical negotiation. `C.30.ILC` handles architecture-specific recognition: whether the conflict is carried by declared scopes, structural views, allocation, interfaces, control rates, work/evidence reuse, scale windows, or coarse-graining loss. It is a triage and architecture-move pattern, not a negotiation pattern.

**Architecture-move examples.**

| Cue | Admissible architecture move | Non-admissible overread |
|---|---|---|
| Component optimization breaks integration | expose hidden coupling; add interface grammar; change allocation | Treat local performance as system adequacy. |
| Modularity reduces local work and increases exceptions | accept bounded exception; revise module boundary; add work/evidence scope | Average exceptions into a modularity score without declared basis. |
| Local autonomy conflicts with control scope | add control layer; change allocation; apply `C.30.LCA` | Treat autonomy label as causal or safety proof. |
| Evidence reuse hides source loss | add evidence scope; add source-return condition; apply `A.10`/`G.6` | Treat reused evidence as automatically valid in the wider scope. |
| A scale window changes the residual | apply `C.29` or an admitted scale/coarse-graining receiving pattern if the scale lens is live | Treat two observations as a universal scale law. |

**Worked slice A - clean module layout, bad flow.** A product team redraws modules so each component has an explicit responsibility/enactor relation, but order-to-cash flow now crosses more work transfers and exceptions rise. `C.30.ILC` names the module structure, flow/transduction structure, affected work scope, cross-scope residual, and first move: expose hidden coupling or open `C.30.TGA-FLOW-REL`. It does not turn the exception count into a modularity measure until `C.16` or an admitted characterization-support receiving pattern is live.

**Worked slice B - AI agent control conflict.** A local agent optimizes its local objective and violates a supervisor's allowed-mode constraint. `C.30.ILC` names the agent scope, supervisor/control scope, control relation, and local repair attempted. The first move may be add control layer, change allocation, or open `C.30.LCA`. Safety, causality, and gate claims use their exact governing patterns.

**Worked slice C - evidence scope residue.** A reusable certification evidence set removes repeated evidence work for several product variants, but one variant has a hidden environment difference. `C.30.ILC` names the work/evidence scope and source-return condition. It applies `A.10` or `G.6` when evidence validity becomes live.

### C.30.ILC:5 - Archetypal Grounding

| Archetype | Without C.30.ILC | With C.30.ILC |
|---|---|---|
| System | A residual across component, system, control, or environment scopes is called generic complexity. | The affected declared scopes and structure kinds are named, and the first architecture move is bounded. |
| Episteme | A diagram, measurement note, or conflict memo is read as if it already selected a repair. | The record preserves the cue, separates support from decision, and applies the exact governing pattern when evidence, measurement, selection, or mediation is live. |

### C.30.ILC:6 - Bias-Annotation

* **Local-success bias.** A local improvement is treated as whole-architecture improvement. Repair by naming the wider scope and the residual.
* **Pseudo-level bias.** `Level`, `layer`, or `scope` sounds precise but no declared scope exists. Repair through `declaredScopeRefs`.
* **Measurement-first bias.** A residual is measured before its structure-kind and scope basis are declared. Repair by opening `C.16` or an admitted characteristic/measurement receiving pattern only after triage names the affected characteristic or measurement basis.
* **Mediation-default bias.** Every conflict is treated as stakeholder conflict. Repair by checking whether the live object is architecture structure, allocation, interface grammar, control, work/evidence scope, or source-return.
* **Synthesis-jump bias.** A local residual immediately triggers candidate generation. Repair by identifying the first admissible architecture move before opening `G.5` or an admitted candidate-generation receiving pattern.

This checklist verifies the preceding guidance after the practitioner has chosen the live move; it is not a required project control form and not a substitute for the card, note, view, relation, or repair move above.

### C.30.ILC:7 - Conformance Checklist


| ID | Check | Why it matters |
|---|---|---|
| CC-ILC-1 | A conforming use names `describedHolonRef`, `boundedContextRef`, and the live architecture concern. | Keeps the triage grounded. |
| CC-ILC-2 | A conforming use names declared scopes, not only `level`, `layer`, `scope`, or `scale` prose. | Prevents pseudo-scope reasoning. |
| CC-ILC-3 | A conforming use names the architecture structure kinds affected by the residual. | Keeps the residual architectural rather than generic. |
| CC-ILC-4 | A conforming use records local repair attempted and why local repair was insufficient when a local repair is claimed. | Prevents premature synthesis and repeated local fixes. |
| CC-ILC-5 | A conforming use states one first admissible architecture move or `noArchitectureMove`. | Makes the output action-guiding without opening candidate generation. |
| CC-ILC-6 | Evidence, assurance, measurement, causal, ethical, selection, scale, and mathematical-lens claim kinds use their exact governing patterns. | Prevents triage from becoming proof or synthesis. |
| CC-ILC-7 | If a source-return condition is live, the record states what hidden or lost distinction triggers return to the source. | Protects compressed and extracted views. |
| CC-ILC-8 | The stop condition is visible. | Prevents the triage pattern from expanding into a hidden prescribed sequence. |

### C.30.ILC:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Generic complexity bucket | Everything becomes `complexity` or `interlevel conflict`. | Name declared scopes, structure kinds, residual, and first architecture move. |
| Measurement-first conflict | The team starts measuring before declaring what is in conflict. | Run ILC triage first; open `C.16` or an admitted characteristic/measurement receiving pattern only when the measured characteristic is live. |
| Risk color as cross-scope decision | A red, yellow, or green risk cell, risk matrix, or maturity score decides the cross-scope architecture move or resource-allocation priority. | Recover declared scopes, live structure kinds, the residual, the loss, hazard, or threat path, selected support reading, characteristic scale, comparator, gate pattern, and first admissible architecture move; do not treat ordinal risk color as architecture adequacy, evidence sufficiency, causal proof, assurance proof, resource-allocation priority, or gate passage. |
| Stakeholder-only conflict | A structural residual is sent to mediation with no architecture move. | Use `D.3`/`D.4` only when values, stakeholder negotiation, or ethical mediation is live. |
| Hidden candidate generation | The residual immediately spawns many designs. | State the first admissible move; open `G.5` or an admitted candidate-generation receiving pattern only when candidate generation is live. |
| Scope word without scope record | The text says `level`, `layer`, `scale`, or `scope` without a declared field. | Recover the exact declared scope or demote the phrase to ordinary recognition. |

### C.30.ILC:9 - Consequences

The gain is an early architecture move that is small and precise. The practitioner can preserve useful problem language such as conflict, frustration, level, layer, or local optimization while recovering the FPF fields that keep the claim reviewable.

The cost is that `C.30.ILC` often refuses to solve the whole problem. It identifies the first architecture move or exact governing pattern application. Measurement, mathematical lens use, stakeholder mediation, candidate generation, evidence, assurance, and final choice remain outside until they are live.

### C.30.ILC:10 - Rationale

Interlevel conflict and frustration are useful Plain source cues because they point to a recurrent architecture failure: local repair in one scope leaves a residual in another. They are dangerous as generic labels because they can hide which scope, structure kind, relation, or source-return condition is actually responsible.

A local optimum or successful local repair is therefore not treated as whole-architecture adequacy. It becomes architecture-relevant only when the cross-scope residual carrier is recoverable and the next move can be named.

`C.30.ILC` keeps the cue but recovers the object. It treats conflict/frustration as architecture-shaping only when declared scopes and architecture structure kinds are named. This lets FPF support the practical intuition without introducing a second ontology of levels, a hidden measurement pattern, or a prescribed architecture work order.

### C.30.ILC:11 - SoTA-Echoing

| SoTA/practice anchor | What it supports | FPF adoption stance | Practitioner implication |
|---|---|---|---|
| Scenario-based architecture trade-off practice, with ATAM-like reasoning used here as lineage and practice basis for concern, scenario, sensitivity point, and trade-off recognition rather than as a decision or evidence method. | Architecture work often starts from cross-concern and cross-scope trade-offs rather than one local measurement result. | Adopt and adapt: use the conflict cue for triage, require declared scopes and structure kinds, and keep final selection, evidence, assurance, and gate passage in exact governing patterns. | A residual can start an architecture move without becoming a decision, proof, or safety case. |
| Complex systems and multi-scale modeling practice. | Local interactions can produce residuals or constraints at wider declared scopes. | Adapt: use scale and scope language only after the FPF record declares the relevant scope or scale window. | `Interlevel`, conflict, and frustration language remains a cue until fields recover the scopes and residual carrier. |
| Control and cyber-physical systems practice. | Local autonomy, feedback, supervisor relations, and rate separation can create cross-scope conflict. | Reuse through `C.30.LCA`, `B.2.5`, `C.27`, and `A.3.3`; do not let ILC carry control proof. | A control conflict opens control-structure or dynamics support only when live. |
| FPF source-return and semantic-coarsening discipline. | Compressed views and reusable records can hide distinctions that matter in a wider scope. | Adopt: add `sourceReturnCondition?` when hidden distinctions carry the residual. | A bounded exception or source-return trigger may be the correct first move. |

### C.30.ILC:12 - Relations

* Builds on `C.30` and `C.30.ASV` for architecture-description and structural-view adequacy.
* Uses `A.22` for structure and structural-view discipline.
* Coordinates with `C.30.TGA-FLOW-REL`, `C.30.LCA`, `A.6.F`, and module/interface patterns when the residual concerns flow, control, function, allocation, module, or interface structure.
* Applies `C.16` or an admitted characteristic/measurement receiving pattern for measurement or characteristic claims, `C.29` or an admitted scale/coarse-graining receiving pattern for scale/coarse-graining claims, `G.5` or an admitted candidate-generation receiving pattern for candidate generation, `C.11` for final local choice, `C.28` for causal outcome claims, `A.10`/`B.3`/`G.6` for evidence or assurance, `D.3`/`D.4` for ethical or stakeholder mediation, and `C.29` for mathematical-lens transfer.

Does not replace: `C.30` architecture-description adequacy, `C.30.ASV` structural-view adequacy, `A.22` structure carrier, `C.30.TGA-FLOW-REL` flow/TGA relation, `C.30.LCA` control-structure view relation, `A.6.F` function-use repair, module/interface repair patterns, `C.16` or admitted characteristic/measurement receiving patterns, `C.29` or admitted scale/coarse-graining receiving patterns, `G.5` or admitted candidate-generation receiving patterns, `C.11` final local choice, `C.28` causal-use support, `A.10`/`B.3`/`G.6` evidence or assurance, `D.3`/`D.4` ethical or stakeholder mediation, or `C.29` mathematical-lens adequacy.

### C.30.ILC:End
