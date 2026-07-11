## E.18.1 - Principles-to-Work Carry-Through

> **Tech-name:** `PrinciplesToWorkCarryThrough`
> **Plain-name:** principles-to-work carry-through relation
> **Type:** Architectural pattern (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part E -> E.18 child pattern
> **Builds on:** `E.18` Transformation Flow Structure, `C.22.2` ProblemCard@Context, `A.6.0` `U.Signature`, `A.6.1` `U.Mechanism`, the A.15 work family, `C.29`, `C.16`, `F.9`, `A.20`, `A.21`, and Part G comparison, selection, and refresh patterns.
> **Purpose:** relate an accepted problem-side record to the next FPF kind named by value, relation, record, or pattern application while preserving useful first-principles carry-through.

### E.18.1:1 - Problem frame

Use this pattern when an accepted `ProblemCard@Context` is ready enough to guide work, but the next FPF use is not yet settled. The practitioner has an unsettled carry-through question: which problem-side distinction can be carried into the next FPF relation or record named by value?

The primary EntityOfConcern is the P2W carry-through relation: the relation between an accepted problem-side record and the next FPF use whose governing relation can be named by value. P2W keeps a carried distinction usable by turning it into one recoverable next FPF use instead of letting an inspiring explanation become an all-purpose project claim.

#### E.18.1:1.1 - Use this when

- an accepted `ProblemCard@Context` names a working problem and the team needs a disciplined next FPF use toward method, planning, performed work, or result interpretation;
- a first-principles, `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, mechanism-position, method-position, `A.15.2 U.WorkPlan` or plan-item, performed-work, result-record, or source-currentness cue is present, but the FPF kind or relation to use next is still unsettled;
- a transformation-flow structure, mathematical path relation in a graph-shaped description, flow diagram, principle scheme, scenario, functional description, or source publication helps the team think, while the next FPF use must still be recovered as an FPF kind or relation named by value;
- a result artifact, telemetry line, acceptance record, quality-evaluation record, done-state update, feedback pin, or integration claim needs to be unpacked before it can guide the next FPF use.

#### E.18.1:1.2 - What goes wrong if missed

The team jumps from a convincing problem-side formulation into downstream language without naming the FPF relation being used. The work then looks connected to first principles, but the next record is unclear, the result phrase becomes too broad, and measurement or source-currentness changes have no honest return relation.

#### E.18.1:1.3 - What this buys

The practitioner gets one next FPF use whose governing relation is named: write a P2W carry-through record, recover the next FPF kind or relation, write or use the governed record, stop with a reduced-use cue, or return to the earlier application whose assumption changed. The payoff is practical: first-principles thinking remains action-guiding without becoming hidden work authorization.

#### E.18.1:1.4 - Not this pattern when

- there is no accepted problem-side record; use `C.22.2` or the problem-side pattern named by value first;
- the FPF kind under repair, relation, and record to write are already settled; use that pattern directly and do not add a P2W layer;
- the requested output is a local project procedure, schedule, or work-management method; use the relevant work, planning, method, gate, or operational-management pattern;
- the requested record or claim is an evidence case, assurance case, gate record, decision record, architecture description, publication-use claim, or wording-use repair; use the recovered relation and its governing pattern directly.

### E.18.1:2 - Problem

First-principles work often becomes useful exactly when a problem-side formulation is ready enough to guide downstream work or work-planning use. The accepted problem card may expose an invariant, mathematical lens, functional role, mechanism-position candidate, method candidate family, planning constraint, result cue, or changed measurement assumption. Without P2W, that useful distinction is either overcompressed into "we have a solution" or scattered across several related FPF patterns before the working distinction is preserved.

P2W solves a carry-through problem. It takes an accepted problem-side record, states the distinction it can carry, selects the next FPF application, typed governed value, relation, or record named by its governing pattern, and records what was written, stopped, split, or reopened. The pattern succeeds only when a practitioner can replay the carry-through from accepted problem-side record plus carried distinction to the next governed record without importing the rule of another pattern into P2W.

### E.18.1:3 - Forces

| Force | What P2W must preserve | Pressure to manage |
|---|---|---|
| First-principles usefulness | A strong problem-side insight may guide method, planning, work, or result interpretation. | The insight is tempting to treat as a completed downstream claim. |
| Governing-kind precision | The next FPF kind or relation must be recoverable before a continuing carry-through relation is used. | Diagrams, graph-shaped expressions, and source wording can look sufficient without a record to write. |
| Practical readability | First use needs a compact record and a quick continuing FPF use. | Too much boundary prose can hide the working P2W application. |
| Non-linear use | P2W may skip, branch, split, stop, or reopen loci in the carry-through structure. | A readable diagram or graph-shaped expression can be mistaken for a required project sequence. |
| Result usefulness | Result phrases often point to artifacts, telemetry, acceptance, measurement, refresh, or role enactability. | One broad result word can hide several different records. |
| Governing-pattern economy | Direct governing patterns keep their own rules. | Repeating their non-use doctrine inside P2W creates content fanout. |

### E.18.1:4 - Solution

The solution has two parts: use the declarative carry-through structure below to select one relation-governed P2W application, then fill the carry-through or replay record only for the relation being made. The locus and relation vocabulary names which distinction can be preserved, which FPF relation is recovered, which record is written, which cue is stopped, and which earlier application reopens after a problem-side result becomes useful for work.

#### E.18.1:4.0 - P2W Declarative Carry-Through Structure

Use P2W as a declarative carry-through structure of relation-governed applications from an accepted `ProblemCard@Context` to accepted FPF applications. The structure is not a prescribed FPF-use procedure. It can be expressed as a graph-shaped description or joined with a `U.MethodDescription` or `U.WorkPlan` only when that description or plan is the current EntityOfConcern of a governed use: a `U.MethodDescription`, `U.WorkPlan`, `TransformationFlowStructure`, flow valuation, or `E.18.2` mathematical description. P2W itself shows which distinction can be preserved, which FPF relation is recovered, which record is written, which cue is stopped, and which earlier application reopens after a problem-side result becomes useful for work.

The carry-through structure has nine recurring loci. A concrete P2W application selects a carry-through slice: it may use one locus, branch into several applications, split one wording span from an admitted source publication or source-use record into several records, stop with a reduced-use cue, or reopen an earlier locus when measurement or `G.11` source-currentness relation changes.

| Locus | Question answered | Output of the P2W application |
|---|---|---|
| `AcceptedProblemSideRecordAndCarriedDistinction` | What accepted problem-side record or accepted `ProblemCard@Context`, and which carried distinction, are being preserved for the next use? | Problem-card reference plus carried distinction. |
| `NextFPFUseQuestion` | What is the next unsettled FPF kind or relation? | One question stated in FPF vocabulary. |
| `FirstPrinciplesLens` | What structure, invariant, loss, or payoff makes the next use worth formal treatment? | Preserved structure, lost structure, payoff, and stop condition. |
| `DeclarationStack` | Which `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, ontology, CHR, measurement, normalization, or bridge relation is needed? | Declaration or reference to the declaration relation named by value. |
| `MechanismMethodCandidate` | Is the next work-facing issue mechanism-position meaning, method-position meaning, method comparison, or retained-set handling? | Mechanism cue, method cue, comparison cue, selector cue, or retained-set cue. |
| `TransformationTemporalAspect` | Is the next issue a bounded transformation under conditions, a temporal aspect of a governed object or claim, or the adequacy of an authored temporal claim? | `A.3.4`, `C.27.TA`, or `C.27` application. |
| `WorkPreparation` | Is a planning record, planned slot-filling baseline, feasibility note, evidence-reference pin, or freshness request needed? | `U.WorkPlan`, PlanItem, or the `A.15.3` planned slot-filling ontic through `SlotFillingsPlanItem`. |
| `PerformedWorkAndResult` | Has dated `U.Work` occurred, and what result-related records appeared? | Work occurrence plus unpacked artifact, telemetry, acceptance, measurement, source-use relation, or role-enactability relation. |
| `ReturnAndRefresh` | Did measurement, `G.11` source-currentness relation, reference plane, or problem-side wording change an earlier assumption? | Return to the affected application with the changed relation named. |

P2W relation labels are `carry`, `recover`, `write`, `split`, `stop`, and `return`. `Carry` preserves a distinction from the problem side. `Recover` names the FPF kind or relation. `Write` creates or amends the governed record. `Split` separates one wording span from an admitted source into several applications. `Stop` preserves a reduced-use cue when no relation-governed continuation is available. `Return` reopens the smallest earlier application whose assumption changed. These are carry-through relation labels for P2W use, not a project-work procedure.

#### E.18.1:4.0a - P2W Unfolding Structure Block

When the P2W use needs explicit unfolding structure, write the local block below or a filled equivalent. It references the current `E.18.3` transformation-flow unfolding structure because P2W carries accepted problem-side records through a transformation-flow slice toward one or more admissible next FPF uses.

```text
P2WUnfoldingStructureBlock:
  unfoldingStructureRef: current ConstraintGovernedTransformationFlowUnfoldingStructure record
  acceptedProblemCardRef:
  principleOrDistinctionRefs[]:
  carryThroughStructureRef:
  governingPatternLoci[]:
  admissibleNextForms[]:
    patternUseRecommendation |
    methodSelectionFrame |
    mechanismRealizationFrame |
    workPlanningSeed |
    evaluationRefreshFrame |
    returnToGoverningPatternRequest
  methodWorkLinkageRef?:
  evidenceOrGateLinkageRef?:
  blockedOverread: not workflow, not performed work, not launch permission
```

`unfoldingStructureRef` names the current local structure record. If that record is also declared as a narrower A.22.CGUS specialization, that relation belongs in `specializedStructureRef?` on the A.22.CGUS record, not in this local block slot.

`P2WUnfoldingStructureBlock` is a local `E.18.3` transformation-flow unfolding structure block governed here for principles-to-work carry-through use. It is not a root U-kind, not a workflow, not performed work, and not launch permission. `E.18.1` governs the carry-through relation among accepted problem-side records, distinctions, governing-pattern loci, and admissible next forms; method, work, evidence, gate, and currentness claims leave to their direct governing patterns.

Use the block when a reader must see how accepted problem-side records constrain the next FPF use or use set. `acceptedProblemCardRef` or equivalent accepted problem-side record is mandatory: raw principles, attractive distinctions, source prose, or model outputs do not directly become work. `admissibleNextForms[]` tells what can be written next; it does not say that the project must execute a sequence.

`methodWorkLinkageRef?` points to `MethodWorkUnfoldingLinkage@Context` only when the method-work relation itself must stay inspectable. If a next form is work-facing, exit to the A.15 family before claiming plan, readiness, launch, or performed work. If evidence or gate claims appear, exit to `A.10`, `B.3`, `A.20`, or `A.21`. If a `G.11` source-currentness relation or edition-decay claim changes the carry-through, use `G.11` for currentness and return to the smallest affected P2W locus.

#### E.18.1:4.1 - Carry-through record

For first-minute use, fill only `ProblemCardRef`, `CarriedDistinction`, `NextFPFUseQuestion`, and either `RecoveredFPFKindOrRelation` or `StopCondition`. Use the remaining fields only when the application continues, splits, writes a record, or returns after a changed assumption.

Use one filled record when applying P2W. It is the local project-facing record of the pattern. Do not copy an empty form into project material; if a field cannot be filled with recovered claim content, state the stop condition or leave the field out.

```text
P2W carry-through record:
  ProblemCardRef: ProblemCard@Context PC-FAB-042, accepted for a cooling-fixture deformation problem.
  CarriedDistinction: the deformation is not one more tuning defect; the problem card identifies a conserved heat-flow structure that must survive method choice.
  NextFPFUseQuestion: does the team need mathematical-lens use or a `U.Signature(profile=FormalSubstrate)` declaration before method selection?
  P2WLocus: FirstPrinciplesLens -> DeclarationStack.
  RecoveredFPFKindOrRelation: mathematical-lens use plus `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame` declaration relation.
  SelectedApplication: `C.29` for preserved and lost structure; `A.6.0` for `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame` when the declaration is written.
  WrittenRecordOrApplication: a short `U.Signature(profile=FormalSubstrate)` declaration naming the heat-flow invariant, the boundary conditions being preserved, the deformation factors left outside the model, and the payoff for later method comparison.
  NotCarried: no method is selected by this record.
  StopCondition: stop before method selection until comparator, measurement, and selected-set relations are named.
  ReturnTrigger: later result measurement shows that the planned module-interface constraint used the wrong reference plane.
  SourceCurrentnessCheck: source-currentness repair and refresh reopen the measurement, normalization, planning, and method-comparison applications; the earlier U.Work occurrence is cited but not rewritten by P2W.
```

`ProblemCardRef` and `CarriedDistinction` locate the accepted problem-side record and the distinction being carried. `NextFPFUseQuestion`, `P2WLocus`, and `RecoveredFPFKindOrRelation` keep the next FPF kind or relation explicit before a continuing carry-through relation is used. `SelectedApplication` and `WrittenRecordOrApplication` name what is used or written.

`NotCarried` is a compact field, not a place to repeat boundary doctrine from other governing patterns. It names only the local overread that would change this P2W application. `StopCondition`, `ReturnTrigger`, and `SourceCurrentnessCheck` keep stopping and reopening tied to a changed relation, measurement, source-currentness, or problem-side assumption.

This record shows the complete P2W relation structure: problem-side distinction, first-principles value, selected FPF application, written record, stop condition, and return after measurement and source-currentness change.

#### E.18.1:4.1a - Development-loop first-application record

Use this record when cheap generation, open-ended search, or evolutionary-engineering work makes many possible variants easy to produce before the project has a clear problem, characteristic set, comparison basis, selected set, work entry, or refresh rule.

```text
DevelopmentLoopFirstApplicationRecord@Project:
  ProblemCardRef:
  ImprovementConcern:
  CharacteristicOrDescriptorSetRef:
  VariantSetOrArchiveRef:
  ComparisonOrFrontRef:
  SelectedSetOrChoiceRuleRef:
  AutonomyBudgetRef:
  EvidenceAssuranceOrConfidenceUseRef?:
  ArchitectureCandidateRef:
  WorkPlanOrWorkRef:
  EffectMeasurementRef:
  RefreshOrResidualTriageRef:
  NextGoverningRelation:
```

The record does not create a development-factory kind, portfolio kind, or archive authority. It is a P2W carry-through record shape: the accepted problem-side distinction is preserved until one next governing relation can be named. If `NextGoverningRelation` is generation, retention, comparison, selection, architecture-candidate work, planning, performed work, effect measurement, residual triage, or refresh, continue in the pattern that governs that relation.

In development-for-developed work, cheap variant generation shifts effort toward problem production, characterization, archive stewardship, fair comparison, choice rule, decision record, autonomy boundary, trust and confidence use, evidence, assurance, performed work, effect measurement, currentness, and refresh. P2W keeps that shift usable by carrying the problem-side distinction into exactly one next relation instead of treating an archive, front, selected set, confidence phrase, or choice rule as work authorization.

Source wording in an admitted source publication or source-use record, such as "trust budget", is recovered to existing FPF relations: evidence support, assurance-sensitive confidence use, gate or release conditions, source-currentness, autonomy boundaries, `A.15.5` work-entry readiness, or decision records. It is not a new `U.TrustBudget`.

Field-compression map:

| Development concern | Record field | Governing continuation |
|---|---|---|
| Problem factory or problem production | `ProblemCardRef` and `ImprovementConcern` | `C.22.2` when the problem statement, opportunity, anomaly, or accepted problem-side record is current. |
| Solution variants, stepping stones, archives, or retained populations | `VariantSetOrArchiveRef` | `C.18` for archive, front, descriptor, retained-value, lineage, and generation records; `C.19` when live-pool or explore-exploit treatment is current. |
| Acceptance criteria, descriptors, parity expressions, and value dimensions | `CharacteristicOrDescriptorSetRef` | `C.16` when a characteristic space, descriptor set, indicator expression, or acceptance expression is being selected or repaired. |
| Fair comparison and front treatment | `ComparisonOrFrontRef` | `A.19.CPM` for comparison mechanism and `C.18` or `C.19` for front or pool records. |
| Selected set or explicit choice rule | `SelectedSetOrChoiceRuleRef` | `G.5` for selected-set publication or set-returning dispatch; `A.19.SelectorMechanism` when selector construction is current. |
| Local choice and decision record | `SelectedSetOrChoiceRuleRef` plus a separate decision reference when filled | `C.11` only when one local choice, commitment, or decision record is being made. |
| Autonomy budget or permitted generator action | `AutonomyBudgetRef` | `E.16` when an autonomy declaration or boundary is current. |
| Trust, evidence, assurance, or confidence use | `EvidenceAssuranceOrConfidenceUseRef?` | `A.10`, `B.3`, `G.6`, `A.20`, `A.21`, or another direct evidence, assurance, gate, release, or provenance pattern when confidence is used to support action, publication, selection, work entry, or acceptance. |
| Architecture candidate | `ArchitectureCandidateRef` | `C.30`, `C.30.ASV`, `C.30.AD`, or `C.30.ILC` when the candidate changes architecture, structural view, architecture description, or interlevel residual treatment. |
| Planning and performed work | `WorkPlanOrWorkRef` | `A.15` family patterns when a plan, plan item, work occurrence, or work-result relation is current. |
| Measurement, result, residual, and refresh | `EffectMeasurementRef` and `RefreshOrResidualTriageRef` | Measurement and result patterns by value, `G.11` for refresh or currentness, and the governing level-and-residual pattern when an interlevel residual is current. |

#### E.18.1:4.1b - Development-for-developed first-minute slice
For a fast DPF seed, use this slice to keep the seed-to-hardening carry-through readable without pretending that the seed is public-ready. An admitted problem-side record or entry cue may carry a domain question, a `G.2` source-use record, a source `U.EpistemePublication` reference, a source-pack cue or source-pack return, and a provisional framework purpose into `E.4.PFAD`, `E.4.PFR`, pattern seeds, quality evaluation, `E.23` improvement, and `G.11` currentness. P2W does not replace those governing patterns. It only preserves the carried distinction until the next governing relation is named.

Use this slice when a project source publication or source-use record says that AI agents or cheap generators make solution variants easy while problem setting, characteristic choice, fair comparison, selected-set choice, and effect measurement become the expensive work.

```text
DevelopmentLoopFirstApplicationRecord@Project:
  ProblemCardRef: accepted problem-side record for the development cycle.
  ImprovementConcern: what must become better, easier to change, easier to test, or more valuable.
  CharacteristicOrDescriptorSetRef: the characteristic, descriptor, indicator, acceptance, or parity expression being selected now.
  VariantSetOrArchiveRef: `C.18` archive, front, Q-front, or retained variant set.
  ComparisonOrFrontRef: `A.19.CPM` comparison relation or `C.19` live-pool or front treatment.
  SelectedSetOrChoiceRuleRef: `G.5` selected-set publication or explicit choice rule.
  EvidenceAssuranceOrConfidenceUseRef: `A.10`, `B.3`, evidence, provenance, gate, release, or confidence-use relation when current.
  ArchitectureCandidateRef: `C.30` family relation only when architecture of a holon or episteme is the object being changed.
  WorkPlanOrWorkRef: `A.15` plan or dated work when action is actually planned or performed.
  EffectMeasurementRef: measurement or result relation named by value.
  RefreshOrResidualTriageRef: `G.11` refresh or currentness relation, or the governing residual-triage pattern.
  NextGoverningRelation: one relation from the filled fields above.
```

```text
DevelopmentLoopFirstApplicationRecord@Project:
  ProblemCardRef: PC-DEV-041, "cheap generator produces many cooling-module layouts, but the project lacks a fair problem and comparison basis"
  ImprovementConcern: keep more maintainable low-energy module variants alive before choosing a product-family direction
  CharacteristicOrDescriptorSetRef: energy use, service access, manufacturability, thermal margin, test cost
  VariantSetOrArchiveRef: C.18 retained cooling-module candidate archive
  ComparisonOrFrontRef: A.19.CPM comparator over energy use and maintainability plus C.18 front record
  SelectedSetOrChoiceRuleRef: no selected-set publication yet; G.5 is next only after the comparator and front are accepted
  AutonomyBudgetRef: E.16 generator boundary for allowed layout search and test spending
  EvidenceAssuranceOrConfidenceUseRef: B.3 confidence-use relation plus A.10 evidence refs for prototype tests; no trust-budget kind is minted
  ArchitectureCandidateRef: C.30 candidate architecture relation for retained layouts that change selected structure
  WorkPlanOrWorkRef: empty until an A.15 work-plan relation is made
  EffectMeasurementRef: thermal and serviceability measurement relation to be named before any work-entry, gate, or authorization relation is relied on
  RefreshOrResidualTriageRef: G.11 refresh when descriptor, test, competitor, or source-currentness changes
  NextGoverningRelation: C.18 front record now; C.30 or G.5 only after the front and comparator are current
```

If a source calls these "problem factory", "solution factory", or "factory of factories", treat the phrase as a project label for work-organization slices: problem-setting work, variant-production work, and capability-building work. The phrase does not add a new FPF kind. Continue only through the filled field named by `NextGoverningRelation`.

#### E.18.1:4.2 - Positive carry-through table

| Locus reached | P2W application | Record or continuation |
|---|---|---|
| Accepted problem-side output | State what is carried from the problem card and what question under repair remains. | P2W carry-through record begins. |
| First-principles or mathematical cue | Name preserved structure, lost structure, payoff, and stop condition. | Mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration. |
| Ontology, UTS, CHR, or `PrincipleFrame` cue | Order ontology, UTS, characteristic, measurement, and principle-frame declarations before downstream use. | Declaration-stack application. |
| Mechanism-position or method-position cue | Separate mechanism-position meaning from method-position meaning, method comparison, and retained-set handling. | Mechanism-position, method-position, method-comparison, selector, or retained-set application. |
| Bounded transformation or temporal-aspect cue | Separate bounded transformation, temporal aspect, and temporal-claim adequacy. | `A.3.4` for bounded transformation, `C.27.TA` for temporal aspect, or `C.27` when authored temporal-claim adequacy or currentness-use is being made. |
| Planning cue | Write or amend a planning record, plan item, evidence-reference pin, freshness request, or planned constraint. | `A.15.2 U.WorkPlan` or plan-item application. |
| Dated performed `U.Work` | Record the work occurrence and relation to plan, gate, launch values, provenance, and later result records. | Performed-work application plus any separate entry or provenance relation. |
| Result phrase | Split the phrase into artifact, resource, launch-value, telemetry, acceptance, measurement, source-use relation, quality, done-state, feedback, parity, refresh, or role-enactability relation. | One or more result-related applications. |
| Changed measurement or `G.11` source-currentness relation | Return to the smallest earlier application whose assumption changed. | Measurement, normalization, source-currentness repair, refresh, planning, method-comparison, or problem-side correction. |

#### E.18.1:4.3 - Locus Use Details

Problem-side input: P2W starts only from an accepted problem-side record. The record carries the distinction that matters for the next FPF use, not the whole problem-side pattern.

First-principles and declarations: mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, ontology, UTS, CHR, measurement, normalization, bridge, and `PrincipleFrame` references are handled as declaration-stack applications. The P2W record names which declaration or direct governing relation is being written or cited, what structure is preserved, what is lost, and which downstream relation is still unsettled.

When mathematical wording points both to a formal declaration and to a mathematical lens, P2W does not decide by vocabulary. Use the slot discipline in `A.6.0:10a.1`: `A.6.0` governs `U.Signature(profile=FormalSubstrate)` declaration, `C.29` governs mathematical-lens use, `A.6.1` governs mechanism consumption or realization, and `E.18.1` governs only the carry-through cue and next-relation selection.

Mechanism and method: do not decide by noun. Recover the claim position. A mechanism-position claim names operation algebra, law set, applicability predicates, effect realization, or mechanism-description need. A method-position claim names a context-defined semantic way of doing work, candidate set, comparison, selector, retained set, or selected-record need. A shared source label, project-side name, or recognizable change concern may require linked method value and mechanism-position value, but P2W records only which relation is being carried through and leaves the other candidate governed value as a stopped cue unless its governing pattern is applied.

Transformation and temporal aspects: a problem-side distinction may point to a bounded transformation, a temporal aspect, and a temporal-claim adequacy question at once. Do not fold these into method, mechanism, plan, or work. `A.3.4` governs bounded transformation under conditions, including transformed object, pre-state, post-state, condition set, and admissible effect claim. `C.27.TA` governs temporal aspects such as interval, deadline, cadence, rhythm, synchronization, currentness window, recovery timing, or stabilization timing when the aspect itself is being named. `C.27` governs adequacy, supported use, unsupported use, or source-currentness use of authored temporal claims.

Planning and performed work: planning records are `A.15.2 U.WorkPlan` values or plan-item records, including evidence-reference pins, feasibility notes, freshness requests, and planned constraints. Performed work is a dated `U.Work` occurrence. P2W records which side of that boundary the carry-through record uses and which later result records have appeared.

Result carry-through: a result phrase is treated as a bundle of possible records. The P2W application is to unpack it before it guides any next FPF use.

Structure, publication, function, module-interface, and integration cues: a transformation-flow structure, mathematical graph description, diagram, or publication can help classify the P2W application. Function wording continues only as an `A.6.F` function or functional-relation claim; interface, port, protocol, connection, resource limit, or integration wording continues only as a module-interface, signature-slot, reusable-structure, or architecture relation named by value through `A.6.M`, `A.6.5`, `C.31`, or the `C.30` family. Otherwise the wording remains only a classification cue for the P2W record.

#### E.18.1:4.4 - Boundary and relation discipline

P2W is not a catalogue of boundary doctrines from other governing patterns. It has one local boundary rule: carry only the distinction accepted on the problem side, recover the next FPF kind or relation, and stop anything that would require a different governing relation until that relation is being made.

| Cue or changed assumption | Local P2W decision | Continuation |
|---|---|---|
| Accepted problem-side record or entry cue | Carry only the accepted distinction and the next FPF-use question. | Continue when the next FPF kind or relation is named; otherwise stop before P2W begins. |
| First-principles or mathematical wording | State preserved structure, lost structure, payoff, and stop condition. | Continue only as mathematical-lens use or as a `U.Signature(profile=FormalSubstrate)` declaration when that relation is being made. |
| Declaration-stack wording | Keep the declaration being made separate from measurement, normalization, comparison, ontology, or bridge relations. | Continue through the declaration relation that changes this P2W application. |
| Work-facing, temporal, or result wording | Recover the concrete mechanism-position, method-position, bounded-transformation, temporal, planning, performed-work, or result-related relation. | Continue through the matching application; split one wording span from an admitted source only when several relations are being made. |
| Another governed relation appears inside the wording span from an admitted source | Preserve the cue as wording from the admitted source or as a source-pack cue, but do not import its governing rule into P2W. | Continue only through the relation that changes this P2W application; leave the other cue stopped until its governing relation is being made. |

#### E.18.1:4.5 - Return and refresh rule

P2W can reopen earlier applications without becoming a required work procedure. Reopen only the smallest application whose assumption changed:

| Changed assumption | Smallest reopened application |
|---|---|
| measurement value, unit, scale, reference plane, or transport relation | measurement, normalization, bridge, or comparison application |
| changed source-use record, admitted reference-publication edition, source-pack reference, source-currentness relation, or publication-use relation | work-relevant appearance-based reliance repair, publication-use, `G.11` refresh, or the direct governing-pattern application named by the changed relation |
| result artifact, telemetry, acceptance, done-state, or role-enactability record | result-related split plus the evidence named by value, measurement, quality, role, or refresh relation |
| method set, comparator, selector, retained set, or selected record | method-comparison, selector, retained-set, or selected-record application |
| problem-side statement or accepted carried distinction | problem-side correction in the problem-card application |

The earlier dated `U.Work` occurrence remains a dated occurrence. P2W may cite it during return, but the changed assumption determines which application is reopened.

#### E.18.1:4.6 - Relation selection aid

Use this aid after the carry-through record when several cues compete for the continuing FPF application. It names the relation family P2W must recover before another pattern can govern the claim; pattern names for those families are listed once in `E.18.1:12`.

| What the wording span from an admitted source makes current | Relation to recover before continuation | Local P2W application |
|---|---|---|
| accepted problem-side distinction | accepted `ProblemCard@Context` or equivalent accepted problem-side record plus one unsettled next relation | State what is carried and what question remains. |
| preserved or lost structure, invariant, near-sameness, formal payoff, or formal stop condition | mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration | Name preserved structure, lost structure, payoff, and stop condition. |
| postulate, observability, unit, plane, comparator, threshold, ontology edition, CHR edition, normalization, bridge, or measurement | the declaration or measurement-family relation being made | Write or cite only that relation. |
| mechanism position, method position, method candidate set, comparator, selector, retained set, or selected record | the mechanism, method, comparison, selector, retained-set, or selected-record relation being made | Keep these relation positions distinct and continue only through the recovered one. |
| bounded transformation, temporal aspect, dynamics episteme, or temporal supported-use claim | `A.3.4`, `C.27.TA`, `A.3.3`, or `C.27` relation according to the claim being made | Split one phrase when it carries several of these relations. |
| planning record, plan item, performed work, launch value, result artifact, telemetry, acceptance, measurement, refresh, or role enactability | `A.15.2 U.WorkPlan`, plan-item, dated `U.Work`, or the result-related relation being made | Write or cite the record being made; do not let generic result wording guide the next FPF use. |
| structure, transformation-flow cue, diagram, scenario, view, graph expression, publication, module-interface, function, evidence-looking, gate-looking, or decision-looking wording | the relation named by value in the wording span from the admitted source, or no continuation if none is recoverable | Use the wording span only as classification until the relation is recovered. |

#### E.18.1:4.7 - Lowering and reopen block

Use this block when the carry-through record cannot preserve and continue the stronger-looking cue from a wording span in an admitted source or from a source-pack cue. P2W succeeds when it leaves one relation-governed application. If the application is not recoverable by value, lower the cue, stop, or reopen the smallest affected application.

| Claim family | Lowering or stop condition | Reopened or continuing relation |
|---|---|---|
| Accepted problem-side record or entry cue | No accepted `ProblemCard@Context`, or the accepted problem-side statement changes the carried distinction. | Stop before P2W begins, or return to the problem-side record named by value that changed. |
| First-principles, mathematical, formal, or declaration-stack claim | Preserved structure, lost structure, payoff, stop condition, declaration relation, measurement relation, normalization relation, bridge relation, or comparison relation cannot be named. | Lower to a reduced-use cue from the wording span in the admitted source or from a source-pack cue; continue only after the recovered declaration, mathematical-lens, measurement, normalization, bridge, or comparison relation is being made. |
| Mechanism, method, selected-set, transformation, temporal, dynamics, planning, performed-work, or result claim | The wording span from the admitted source blurs relation positions that change different P2W applications. | Split to the recovered relation and continue only through that relation. |
| Another governed relation is only signaled by a label, diagram, port, module-interface phrase, publication, view, approval word, readiness word, or wording phrase | The wording span from the admitted source classifies a possible relation but does not name the relation being made. | Preserve the cue and stop local continuation until the governed relation is recoverable by value. |

#### E.18.1:4.8 - Replay and currentness record

Use this compact record after `G.11` source-currentness repair, appearance-based reliance repair, changed measurement, changed problem-side record, FPF pattern change, or a use-found defect. The record keeps replay local: it says what changed, what still carries, what no longer carries, and which application reopens.

```text
P2W replay and currentness check:
  OriginalRecordRef:
  ChangedInput:
  ChangedAssumptionKind:
  StillCarried:
  NoLongerCarried:
  SmallestReopenedApplication:
  GoverningRelationChecked:
  CurrentnessResult:
  NextFPFUse:
```

`ChangedAssumptionKind` names the assumption kind, such as measurement, unit, reference plane, source-use record, source-currentness relation, problem-side statement, method set, comparator, module-interface relation, publication-use relation, or FPF pattern change. `StillCarried` and `NoLongerCarried` prevent a source-currentness change from silently rewriting the whole carry-through slice. `SmallestReopenedApplication` keeps the repair local, and `NextFPFUse` states whether to continue, stop, split, lower to a reduced-use cue, or return to the problem-side pattern.

### E.18.1:5 - Archetypal Grounding

`E.18.1` is grounded in a simple System and Episteme contrast. In System-facing work, an accepted problem-side record may lead toward method choice, planning, performed work, result records, and result measurement. In Episteme-facing work, the same record may lead toward a `U.Signature(profile=FormalSubstrate)` declaration, mathematical-lens use, description, publication, evidence, or gate-related claims. The P2W application asks one question in both cases: which FPF kind or relation can carry the next claim being made?

| Archetype | System-side grounding | Episteme-side grounding |
|---|---|---|
| Tell | A manufacturing team accepts a problem card showing that a fabrication issue is caused by a missing functional constraint. | A research team accepts a problem card showing that two descriptions may be almost the same only under a declared `U.Signature(profile=FormalSubstrate)`. |
| Show without P2W | The team treats the principle scheme as method selection, work plan, performed work, and acceptance evidence at once. | The team treats mathematical equivalence as real-world identity, measurement validation, evidence, and decision claim. |
| Show with P2W | The team writes a carry-through record, separates method comparison from `A.15.2 U.WorkPlan` and plan-item records, records dated `U.Work`, and unpacks result records. | The team writes a carry-through record, separates mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, bridge, measurement, evidence, and provenance relations, and keeps equivalence bounded by the declared formal relation. |

#### E.18.1:5.1 - Worked slices

1. **Thin first-principles start.** An accepted `ProblemCard@Context` says the problem is not one more local tuning task because a conserved structure is being ignored. P2W records the carried distinction, recovers mathematical-lens use and `U.Signature(profile=FormalSubstrate)` declaration only if needed, and stops before method selection until comparator, measurement, and selected-set relations are named.

2. **Planning from selected enough method.** A method family is selected enough for planning. P2W carries the planning relation; the plan records planned constraints, planned fillers, evidence-reference pins, and freshness requests.

3. **Performed work after planning.** A dated work occurrence has appeared. P2W carries the performed-work relation and records which gate, release, provenance, or launch-value relation is separate from the occurrence.

4. **Result interpretation without generic result.** A source says the work result proves that the approach worked. P2W unpacks artifact, telemetry, measurement, evidence, acceptance, quality-evaluation, refresh, and role-enactability candidates before any one of them guides the next FPF use.

5. **Functional explanatory order.** A source diagram places `U.Signature(profile=FormalSubstrate)`, principle frame, mechanism, normalization, method selection, planning, performed work, and result measurement in one readable order. P2W uses the diagram to classify applications while keeping physical time and performed-work chronology with their own patterns.

6. **Interface split before P2W use.** A source says a port-throughput limit makes a solution feasible after integration. P2W first splits the phrase: module-interface relation (`A.6.M`), `E.18` transformation-flow relation or `A.6.F` function or throughput relation when function use is being claimed, WorkPlan constraint (`A.15.2`), dated `U.Work` occurrence (`A.15.1`), evidence or gate claim (`A.10`, `G.6`, `A.20`, or `A.21`), or architecture and structural-view claim (`C.30` family). The carry-through record writes only the relation that changes the P2W application being made and leaves the other readings as stopped cues.

7. **Result measurement returns to planning.** A performed `U.Work` occurrence produced telemetry and an artifact. Later measurement shows that the planned module-interface constraint was interpreted against the wrong reference plane. P2W splits measurement, reference-plane repair, source-currentness repair, refresh, planning revision, and method-comparison claims. If the original `ProblemCard@Context` no longer states the right problem, the problem-side correction returns to the problem-side pattern.

#### E.18.1:5.2 - Additional worked situations

| Situation | P2W application | What changes |
|---|---|---|
| First-minute use | A practitioner has only an accepted `ProblemCard@Context` and the sentence "the cooling fixture violates the heat-flow invariant." Fill `ProblemCardRef`, `CarriedDistinction`, `NextFPFUseQuestion`, and `RecoveredFPFKindOrRelation` or `StopCondition`. | The next P2W application becomes a `C.29` and `A.6.0` application, not method selection or evidence writing. |
| Diagram and approval note in the same source publication or source-use record | The same source publication contains a diagram, a test photo, and a manager note saying "approved." Keep P2W focused on the distinction carried from the problem-side result. | Diagram cue, evidence-looking cue, and gate-looking cue are separated by relation recovery; the P2W record keeps only the carried distinction and next relation. |
| Principle story without accepted problem-side record | A source has an inspiring principle story but no accepted `ProblemCard@Context`. | P2W stops before it begins; the source remains a reduced-use cue until `C.22.2` or the problem-side pattern named by value accepts a problem-side record. |
| Acceptance label hides wrong measurement | A dashboard shows a green acceptance label, but the measurement used the wrong reference plane. | Acceptance color does not guide the next FPF use; P2W returns to measurement, normalization, source-currentness repair, planning, and method comparison. |
| Changed unit after source-currentness repair | Later source-currentness repair changes only the unit and reference plane used by the planning constraint. | P2W reopens the smallest affected applications; the earlier dated `U.Work` occurrence is cited, not rewritten. |
| Near-sameness under a formal declaration | A mathematical near-sameness claim preserves heat-flow structure but loses deformation factors outside the model. | P2W uses `C.29` for mathematical-lens use and `A.6.0` for `U.Signature(profile=FormalSubstrate)`, names preserved and lost structure, and prevents the lens from settling empirical truth or work authorization. |
| FPF relation rule changes after a P2W record | A governing FPF pattern changes the boundary for architecture-description, evidence, or `A.15.4` appearance-based reliance repair use. Fill the replay and currentness check: changed rule, still-carried distinction, no-longer-carried cue, smallest reopened application, and next FPF use. | The earlier carry-through record is replayed rather than trusted by age; only the affected architecture-description, evidence, `A.15.4`, or P2W field changes. |
| Relation selection would over-select from one phrase | A source says "the new port contract proves integration readiness." P2W splits module-interface relation, `E.18` transformation-flow relation, dated `U.Work` occurrence, evidence cue, gate cue, and architecture-description cue. | Only the relation that changes the P2W application being made is written; the remaining readings stop as named cues until their governed relations are being made. |
| Formal claim loses payoff | A `U.Signature(profile=FormalSubstrate)` declaration preserves a neat invariant, but no practical payoff or downstream stop condition can be stated for the accepted problem-side record. | The mathematical phrase lowers to a reduced-use cue; P2W does not justify method selection, evidence, gate, or `A.15.2` planning from mathematical prestige alone. |
| Result source-use relation becomes stale | A result-looking source-use relation or publication cue is later replaced by a fresher source-use relation with a different artifact reference and measurement reference. | P2W uses `A.15.4` appearance-based reliance repair before result carry-through; stale result wording cannot continue as evidence, acceptance, or quality evaluation. |

#### E.18.1:5.3 - Pilot examples for coupled transformation-flow slices

These pilots are grounding checks, not source terminology to import. They exercise the same common shape: one current `TransformationFlowStructure` can relate several transformation-flow valuations or slices, one slice may develop or select a usable product, another slice may apply it, and an evaluation or refresh slice may return to the smallest affected development or application locus. The transformation-flow structure does not merge the slice-local objects, `DesignRunTag` boundaries, evidence, gates, work occurrences, or the relation position that the carried object fills inside each slice. Use each pilot to check whether the P2W use being made can name the joined transformation-flow slices, the carried object's slice-local relation position, the `DesignRunTag` boundary, and the smallest reopened slice.

| Pilot | P2W use being made | What it tests |
|---|---|---|
| Coffee service STF | An accepted service-quality problem carries heat or mass-balance structure through `U.Signature(profile=FormalSubstrate)`, declaration-stack, mechanism-position, normalization, method-selection, `A.15.2 U.WorkPlan` or plan-item records, dated `U.Work`, telemetry, measurement, and refresh relations. | Positive whole-chain readability, freshness, set-return selection, launch values only in performed work, and relation-local refresh. |
| Compiler design and run | Toolchain construction, compiler use, and product execution are separate applications; design and run changes pass through the gate and work relations being used. | `DesignRunTag`, launch gate, reproducible build currentness, `G.11` source-currentness relation, and no collapse of build, run, and product work. |
| TAMP and MPC robotics | Method selection and `A.15.2` planning records may be revised under a declared progress or budget condition before performed work. | Branching and cycle use without imposing one mandatory work procedure, and no launch-value binding before performed work. |
| AutoML and QD | Method selection returns a Pareto, QD, front, or archive set under comparator and descriptor editions, not a hidden scalar winner. | Set-return discipline, comparator currentness, no hidden scalarization, and retained-set refresh. |
| Freshness or physical-transport case | Work planning and performed work depend on freshness windows, transport relations, units, reference planes, and source-currentness. | No implicit `latest`, no unbridged unit or plane comparison, and smallest affected refresh. |
| Integration under module-interface constraints | After assembly, a result phrase may mean role-enactability under module-interface constraints, evidence, gate, architecture, function, or work relation. | Result carry-through is not artifact-only or telemetry-only; module-interface and integration wording must recover the relation being claimed. |
| Tool-product-use chain | A design-tagged transformation-flow slice makes a tool; a later run or use slice uses the tool to make a chair; another slice uses the chair as context for writing a text. | One selected `TransformationFlowStructure` can relate all slices, but the same carried object may fill a run-result position in one slice and a design-side input, tool, context, or constraint position in another. The relation-position shift is explicit, tied to the `E.18` transformation-flow relation and any `DesignRunTag` being used, and does not change the object's kind by wording. |
| FPF pattern development and self-evolving specification | A development transformation-flow slice creates or repairs a pattern, specification, or process description through drafting, quality evaluation, publication projection, and admitted publication; a later use slice applies that product to its own `EntityOfConcern`; a defect found in use returns to the smallest development slice for repair. | Development, application, and evaluation slices are joined by transfer and return relations inside one selected `TransformationFlowStructure` while keeping objects and `DesignRunTag` boundaries separate; evaluation records or use-found evidence change the product through edits to the smallest development slice, not by entering the used publication's practitioner-facing prose. |

#### E.18.1:5.4 - Filled P2W output records

Use these as replayable outputs, not as new templates.

```text
P2W output record:
  ProblemCardRef: ProblemCard@Context PC-COOL-017, accepted for a cooling-loop stabilization problem.
  CarriedDistinction: the observed deformation is not one more tuning defect; a conserved heat-flow structure must survive method comparison.
  NextFPFUseQuestion: which formal or mathematical relation is needed before method selection?
  RecoveredFPFKindOrRelation: mathematical-lens use plus `U.Signature(profile=FormalSubstrate)` declaration.
  SelectedApplication: `C.29` for preserved and lost structure; `A.6.0` for the formal-substrate declaration.
  WrittenRecordOrApplication: declare the heat-flow invariant, boundary conditions, excluded deformation factors, and practical payoff for comparator selection.
  LocalStop: method selection waits until comparator, measurement, and selected-set relations are named.
```

```text
P2W output record:
  ProblemCardRef: ProblemCard@Context PC-PORT-008, accepted for an integration-throughput problem.
  CarriedDistinction: the port-throughput phrase may carry module-interface, `E.18` transformation-flow, work-plan, performed-work, evidence, gate, and architecture relations, but only one relation changes this P2W application.
  NextFPFUseQuestion: which relation is being written now?
  RecoveredFPFKindOrRelation: `A.6.M` module-interface relation plus `E.18` transformation-flow relation; `A.15.2` planning constraint is written only if the planning record is being made.
  SelectedApplication: `A.6.M` for the port contract; `E.18` for the transformation-flow relation; `A.15.2` only for the planned constraint.
  WrittenRecordOrApplication: write the module-interface constraint and `E.18` transformation-flow relation; stop evidence and gate cues until their governing relations are being made.
  LocalStop: no readiness proof or work authorization follows from the port phrase by itself.
```

### E.18.1:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Ontological and epistemic**, **Prag**, **Did**. Scope: **accepted problem-side record plus carried distinction moving toward FPF applications**.

- **Governance bias (Gov):** authorization, gate, release, assurance, and decision cues are preserved only as local cues until the relevant FPF relation is recovered.
- **Architectural bias (Arch):** diagrams, selected structures, and module-interface language help classify the next P2W application; they do not displace the P2W carry-through relation.
- **Ontological and epistemic bias:** `U.Signature(profile=FormalSubstrate)`, near-sameness, source publication, and evidence-looking language are turned into recovered FPF kinds and relations.
- **Pragmatic bias (Prag):** the carry-through structure is useful for action without becoming a required project procedure.
- **Didactic bias (Did):** the positive carry-through structure and filled record come before the boundary table, so precision does not bury the working P2W application.

### E.18.1:7 - Conformance Checklist

- `CC-E18.1-1` The P2W use starts from an accepted `ProblemCard@Context` or stops before P2W begins.
- `CC-E18.1-2` The carry-through record states `ProblemCardRef`, `CarriedDistinction`, `NextFPFUseQuestion`, `RecoveredFPFKindOrRelation`, `SelectedApplication`, `WrittenRecordOrApplication`, `NotCarried`, `StopCondition`, `ReturnTrigger`, and `SourceCurrentnessCheck`.
- `CC-E18.1-3` The positive carry-through structure is recoverable: accepted problem-side record plus carried distinction, question under repair, first-principles lens, declaration stack, mechanism position, method position, planning, performed work, result records, and return or refresh.
- `CC-E18.1-4` One wording span from an admitted source may split into several FPF applications; the record does not compress them into one generic token.
- `CC-E18.1-5` Result wording is unpacked into concrete result-related relations; a generic `WorkResult` kind is not admitted.
- `CC-E18.1-6` `PrincipleFrame` references keep postulates and CHR observability distinct from units, planes, comparators, thresholds, ontology editions, CHR editions, plans, work, evidence, and gates.
- `CC-E18.1-7` Measurement, `G.11` source-currentness relation, reference-plane, method-set, comparator, or problem-side changes return to the smallest affected application.
- `CC-E18.1-8` Non-P2W governing rules appear only as a recovered relation in `E.18.1:4.6` and as a pattern list in Relations, not as repeated local doctrine.
- `CC-E18.1-9` Local boundary wording remains only where it names a near-miss that changes the next P2W application.
- `CC-E18.1-10` The pattern leaves one useful relation-governed action: write the carry-through record, write or use the governed record, split a wording span from an admitted source, stop with a reduced-use cue, or return to a changed application.
- `CC-E18.1-11` Archetypal grounding can replay at least one coupled transformation-flow-slice pilot from `E.18.1:5.3`; the pilot joins development, application, evaluation, and repair slices in one selected `TransformationFlowStructure` while keeping their objects, slice-local relation positions, `DesignRunTag` boundaries, and evidence distinct. The self-evolving-spec pilot keeps development-slice evidence or use-found evidence outside the used pattern, specification, or process description.
- `CC-E18.1-12` Every carried claim family can be lowered, stopped, split, or reopened through `E.18.1:4.7`; a cue from a wording span in an admitted source or from a source-pack cue that cannot name the recovered FPF kind or relation remains a reduced-use cue.
- `CC-E18.1-13` Every replay after a changed source-use record, source-publication relation, measurement, problem-side record, or FPF relation rule names the changed assumption kind, what is still carried, what is no longer carried, the smallest reopened application, the governing relation checked, and the next FPF use.
- `CC-E18.1-14` When a generated DPF seed or cheap framework seed enters P2W, the record names the `G.2` source-use record, source `U.EpistemePublication` reference, source-pack cue, or source-pack return when that source use is current, the problem-side cue when that is current, the next governing relation (`G.2`, `E.4.PFAD`, `E.4.PFR`, `E.8`, `E.21`, `E.23`, `G.11`, or another direct governing pattern), and the stop condition that prevents the seed from becoming public authority by generation alone.



### E.18.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Boundary fanout.** The pattern repeats long lists of what P2W is not. | Keep relation discipline in `E.18.1:4.4`; make local sections state the next P2W application. |
| **Carry-through-as-procedure.** A carry-through structure, diagram, or graph-shaped expression is read as a required project sequence. | Treat it as relation-governed carry-through over FPF applications; use `stop`, `split`, and `return` relations. |
| **ProblemCard-as-solution.** The accepted problem card is treated as method, plan, work, evidence, or result. | Write the carried distinction and next FPF-use question before selecting an application. |
| **Math-as-authority.** A `U.Signature(profile=FormalSubstrate)` declaration, mathematical lens, or near-sameness does all downstream work. | Record preserved structure, lost structure, payoff, and stop condition; continue through the recovered relation. |
| **Generic result token.** "Result" becomes one local kind. | Split the phrase into artifact, telemetry, acceptance, quality, measurement, refresh, source-use relation, evidence, or role-enactability relation. |
| **Interface shortcut.** Interface, port, protocol, connection, resource, or integration wording selects function, method, work, evidence, gate, or architecture by itself. | Recover the module-interface, signature-slot, function, architecture, work, evidence, or gate relation before continuing. |

### E.18.1:9 - Consequences

| Consequence | Benefit | Cost or mitigation |
|---|---|---|
| The carry-through record becomes the local project record. | A practitioner can replay the carry-through from problem-side output to continuing FPF application. | The record adds a small step before downstream work. |
| Positive carry-through structure comes before boundary. | First use is readable before the heavier relation aid. | Boundary checks are still available in one canonical section. |
| Result language becomes unpackable. | Artifacts, telemetry, acceptance, measurement, refresh, and role enactability can be handled by their own records. | More than one application may be needed for one wording span from an admitted source. |
| P2W stays non-procedural. | The pattern can be used in many project situations without prescribing one local procedure. | Teams that want a work procedure must add method material or `A.15.2` planning material outside P2W. |
| Related patterns keep their authority. | P2W avoids duplicating evidence, gate, decision, architecture, publication, mechanism, and work-family doctrine. | Users consult the pattern named by the recovered relation when that relation is being made. |

### E.18.1:10 - Rationale

`E.18.1` is a child of `E.18` because P2W uses a transformation-flow structure as its setting when the carry-through relation spans several transformation-flow slices, loci, or returns. It does not define graph semantics or prescribe performed-work order. It defines a local carry-through pattern for turning accepted problem-side records into a next FPF use whose governing relation is named.

The design puts the positive carry-through table first because repeated negative distinction sets can make a pattern whose primary EntityOfConcern is P2W behave like reference policing. P2W needs precision, but precision is useful here only when it leaves a surviving action: write the carry-through record, recover the FPF kind or relation, use the governed record, stop, split, or return.

### E.18.1:11 - SoTA-Echoing

**SoTA alignment rule.** P2W borrows useful distinctions from practice traditions only after they can be stated as a P2W carry-through application: accepted problem-side record, carried distinction, recovered FPF relation, written record, stop condition, and local return. Currentness can change because an admitted source-use record, source publication, source pack, publication-use relation, `G.11` source-currentness relation, telemetry relation, measurement assumption, reference-plane assumption, or similar governed relation changes. It can also change because an FPF pattern changes the relation rule used by the carry-through record. In both cases P2W reopens only the smallest affected application.

| Practice tradition | Distinction kept for P2W | P2W invariant | Practitioner implication | Reopen if |
|---|---|---|---|---|
| Development-for-developed practice with cheap solution generation. | Cheap solution variants make problem production, characteristic choice, fair comparison, selected-set publication, decision record, autonomy budget, performed work, measurement, and refresh the expensive work. | `DevelopmentLoopFirstApplicationRecord@Project` carries only the accepted problem-side distinction and the next governed relation; it does not become a development-factory kind, portfolio kind, archive authority, or lifecycle. | An engineering lead can start with one thin record and then apply `C.22.2`, `C.16`, `A.19`, `C.18`, `C.19`, `G.5`, `C.11`, `E.16`, `A.15` family patterns, `G.11`, or `C.30.ILC` according to the field that is current. | The problem framing, characteristic set, comparator, selected-set publication, decision relation, autonomy declaration, work plan, measurement, residual, or refresh relation changes. |
| Current OEE-style generated-method source set, such as Darwin Godel Machine, AlphaEvolve, and DeepEvolve-style cases. | Generated methods, method descriptions, evaluators, selected sets, `G.2` source-use records, source-use relations, work results, and refresh each have different authority. | P2W preserves the problem-side distinction until the generated-variant, comparison, selector, work, measurement, source-currentness, or refresh relation is named. | Generated algorithm text can be used as a cue without becoming proof, gate passage, accepted method selection, or performed work. | Evaluator, source-use, source-currentness, method-description, selected-set, work-result, or refresh assumptions change. |
| Current QD and OEE survey pressure, including Quality-Diversity survey DOI `10.1016/j.swevo.2025.102240`. | Archives, fronts, diversity pressure, stepping stones, and retained variants often matter before one choice is justified. | P2W names whether the next relation is archive or front stewardship, pool treatment, selected-set publication, local choice, work planning, performed work, measurement, or refresh. | The project can keep the archive useful without letting archive or front language authorize work or decide one winner. | Descriptor, distance, dominance, archive policy, comparator, publication, or refresh currentness changes. |
| Model-based engineering and systems practice separates model, view, requirement, evidence, and performed-work records because each has different authority. | A useful diagram or view can classify the next relation without changing the governed kind. | P2W separates transformation-flow structure, mathematical graph description, view, publication, evidence, gate, and work applications before the next FPF use. | The practitioner can use a diagram as a classification cue without letting the diagram authorize work, prove readiness, or settle evidence. | The project source-use record, architecture-description relation, evidence relation, gate relation, or release relation changes. |
| Traceability and digital-thread practice values continuity from problem, rationale, method, plan, work, and result while keeping record kinds distinct. | A trace is useful only when each record kind remains named. | P2W carries a problem-side record through a replayable carry-through record while keeping problem card, work plan, performed work, evidence, provenance, result, and refresh relations distinct. | The team can replay a carry-through slice from problem to work without treating trace continuity as evidence, approval, or performed work. | `G.11` source-currentness repair, provenance, refresh, or work-family rule changes the currentness relation. |
| Formal-methods and mathematical-modeling practice uses `U.Signature(profile=FormalSubstrate)` declarations to preserve invariants, expose lost structure, and make equivalence conditions explicit. | Mathematical value is recoverable only through preserved structure, lost structure, payoff, and stop condition. | P2W separates mathematical-lens use from the `U.Signature(profile=FormalSubstrate)` declaration and from empirical, work, evidence, or authorization claims. | A mathematical idea helps choose the next disciplined FPF use without becoming proof of real-world identity or authorization to act. | Mathematical-lens, signature, bridge, measurement, normalization, comparison, or source-currentness assumptions change. |
| Assurance, safety, evidence, gate, and decision practice treats confidence, acceptance, validation, approval, and release as distinct relations. | Labels and readiness phrases are cues, not local authority. | P2W preserves the cue, recovers the relation, and stops local authority until the governed relation is being made. | A warning, green label, or approval note remains useful without becoming an evidence case, gate record, decision, or release. | Evidence, assurance, gate, conformance, release, work-entry readiness, or decision relation changes. |

### E.18.1:12 - Relations
- `A.22.CGUS` supplies the general constraint-governed unfolding structure when P2W must expose loci, constraints, admissible next forms, and stop or return conditions.
- `E.18.3` supplies the transformation-flow unfolding specialization for the `P2WUnfoldingStructureBlock`; P2W remains a carry-through use, not a workflow, launch permission, or performed-work record.
- `G.2` governs source-use records, source-pack return, evidence anchors for admitted source publications, and source-currentness payloads before DPF hardening can rely on a seed drawn from those admitted sources.
- `E.4.DPF`, `E.4.PFAD`, and `E.4.PFR` govern DPF authoring, framework architecture decisions, and framework relation records when a generated or cheap seed is carried toward hardening.
- `E.23` governs repeated quality improvement only after the object version and evaluation are recoverable; P2W may carry a seed to that point but does not become the improvement method.
- `G.11` governs currentness, admitted-source decay, source-use relation change, edition change, and refresh when a changed source publication, source-use relation, or telemetry reopens the smallest affected P2W application.

- `E.18` governs selected `TransformationFlowStructure`, transfer annotations, flow valuation, `ConstraintValidity`, `GateFit`, gate profile, design tags, and run tags.
- `C.22.2` governs the accepted problem-side record and problem-side claims related to the carried distinction.
- `C.29`, `A.6.0`, `E.14`, `F.17`, `F.9`, `C.16`, `A.19.UNM`, and Part G govern mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, principle-frame, ontology, UTS, bridge, measurement, normalization, and comparison relations.
- `A.6.1` and `E.20` govern mechanism and mechanism-method stabilization relations. `A.3.4`, `C.27.TA`, `C.27`, and `A.3.3` govern bounded transformation, temporal aspect, temporal-claim adequacy, and dynamics-episteme relations.
- `G.5`, `G.9`, `A.19.SelectorMechanism`, `C.18`, and `C.19` govern candidate-set, comparison, selector, retained-set, and selected-record relations.
- `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, and `A.15.5` govern role-method-work alignment, performed work, planning, planned baselines, work-relevant appearance-based reliance repair, and work-entry readiness.
- `A.10`, `B.3`, `G.6`, `E.19`, `A.20`, `A.21`, and `C.11` govern evidence, assurance, provenance, conformance, gate, release, and decision claims.
- `C.30`, `C.30.AD`, `C.30.ASV`, `C.32.P2S`, `C.31`, `A.6.M`, `A.6.F`, `E.10`, `E.17`, and `E.17.EFP` govern architecture, architecture-description, structural-view, problem-to-structure architecturing, reusable-structure, module-interface, function, wording-use, publication, and publication-use claims.

### E.18.1:End

