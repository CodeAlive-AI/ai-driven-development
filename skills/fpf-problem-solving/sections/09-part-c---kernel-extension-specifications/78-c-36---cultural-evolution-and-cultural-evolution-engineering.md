## C.36 - Cultural Evolution and Cultural-Evolution Engineering

> **Tech-name:** `CulturalEvolutionEngineering`
> **Plain-name:** cultural evolution and cultural-evolution engineering
> **Type:** Conceptual and project-use pattern (C)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.36:1 - Problem frame

Use this pattern when the current project question is about how a culture, style, tradition, discipline practice, method family, work family, canon, recognition regime, selection regime, or mediating system changes and can be deliberately influenced.

Typical first-use situations:

- an engineering group treats its product family, toolchain, platform family, research program, or AI-agent framework as an evolving set of variants rather than one fixed system;
- a scientific, medical, pedagogical, engineering, music, dance, organizational, or AI-agent discipline is changing through related methods, work products, training forms, memory epistemes, recognition regimes, and selected variants;
- a music or dance steward needs to compare style, genre, technique, scene, canon, platform, or tradition labels without assuming that the label names one root kind;
- a project lead wants to influence the evolving practice—for example by changing how variants are generated, transmitted, recognized, selected, remembered, measured, or refreshed, or by changing a Method family, Work family, assignment, mediating architecture, or performed intervention.

#### C.36:1.1 - What goes wrong if missed

The team treats culture as shared vocabulary, treats style as a genre tree, treats a platform as the cultural object, treats a QD archive as the decision, or treats one scalar popularity or quality score as cultural development. The project can then generate many variants but still lose the relations that make those variants transmissible, recognizable, selectable, retained, refreshed, or turned into work.

#### C.36:1.2 - What this buys

The practitioner gets one small statement of the cultural relations now supported, what is changing or worth continuing, and the next action or stop. Add collective holons, local system-role kinds, classifications, assignments, Work and Method families, canon or memory epistemes, architectures, measurements, and refresh relations only when the current claim actually needs them.

#### C.36:1.3 - First useful move

Start with one ordinary sentence. For example: `In this dance school, teachers transmit variants through teaching, the festival archive retains and presents records of variants, jury recognition and peer copying select variants, and the current intervention changes how new variants enter the syllabus.` Add the next pattern only when its definition or test changes the action. A qualified current account or a decision to continue the existing arrangement may finish without a new intervention.

When the result must be retained or handed on, use a small card:

```text
CulturalEvolutionCaseCard@Context:
  CaseRef:
  CaseScopeOrModelUseBoundary:
  CollectiveHolonOrDisciplineScope:
  VariantRefsOrDescription:
  TransmissionRecognitionSelectionOrMemoryRelations:
  MediationOrMeasurementRefs?:
  PublicationRefs?:
  CurrentEvolutionaryQuestion:
  ApplicablePatternRefs?:
  NextActionOrStop:
```

`@Context` is part of the card's context-qualified retrieval name. `CaseScopeOrModelUseBoundary` names the actual project, discipline, scene, product-family, publication, or model-use boundary. This boundary stops a local trend from becoming the whole culture merely by wording. `PublicationRefs` is optional: when a publication distinction matters, name only the exact E.17 source-backed face or exact E.24.PUB publication occurrence, publication form, presentation carrier, audience-declaration episteme, bounded-use-declaration episteme, or availability claim needed by this case. The card does not require a complete publication record. Actual access, reliance, use, and Work stay outside this field unless their own direct relations or occurrences are separately current.

Variants may be generated, retained, inherited, or observed. An archive or front claim still uses C.18 or C.19.

Expand the card only when later use needs more detail. Possible additions include direct participation or position relations; local system-role kinds, separate System-classification judgments, assignment species and obtaining occurrences; Work and Method families; Method relation structures and descriptions; canon or memory epistemes; recognition and selection regimes; mediation systems or architectures; characteristic spaces; style or tradition term rows; publication relations; measurement; and refresh. Each addition identifies its own object or obtaining relation; the card creates none of them.

The card is optional and keeps the case's claims together; their definition and testing remain with the applicable patterns.

#### C.36:1.4 - Working scope

Many current projects no longer develop one isolated object. They shape, for example, product families, methods, research directions, medical and pedagogical practices, AI-agent frameworks, artistic styles, engineering traditions, canons, archives, frontiers, and recognition regimes as these evolve. The project often generates variants cheaply, while the hard work shifts to the relations that determine what is produced, recognized, retained, selected, used, changed, or kept current. That work can include, for example, problem production, characterization, archive stewardship, comparison, selected-set result declaration, actual publication, local choice, performed Work, effect measurement, and refresh.

Cultural evolution is current when the question is how a collective or discipline generates, transmits, recognizes, selects, retains, or changes variants. Memory or canon epistemes, recognition and selection relations, comparison, platform or algorithmic mediation, and changing Method families may all matter.

When the case says that Work was performed, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated Work occurrence and enacted Method. Add A.2.1 and F.6 only when the case or receiving use expressly represents precise assignment-bound attribution; missing or failed F.6 leaves the Work intact. A local system-role kind, classification judgment, assignment species, assignment occurrence, Work occurrence, Method, effect claim, responsibility relation, and family description remain separate.

This pattern provides a first-use cultural-evolution case. The same pattern can serve engineering product families, scientific research programs, medical disciplines, pedagogy, music styles, dance styles, organizational cultures, and AI-agent framework evolution because it begins with existing FPF objects and relations rather than domain labels.

### C.36:2 - Problem

Culture, style, tradition, genre, scene, practice, platform, regime, technique, and developmental-machinery wording is useful but dangerous. In source and project prose, one label may point, for example, to:

- a method family or method relation structure;
- a work family or family of performed works;
- an exact local system-role kind, its classification judgment, or a separately obtaining system-role-assignment occurrence;
- a discipline or collective holon;
- a canon or memory episteme;
- a recognition, selection, measurement, or visibility relation;
- a mediation system, product architecture, platform architecture, or algorithmic mediator;
- an archive, front, current pool, selected set, lineage, or edition set;
- a publication label or cross-context term bridge.

If the project accepts the word as ontology, FPF grows a second ontology beside method, Work, system-role kind and assignment, discipline, episteme, architecture, selection, publication, and refresh. If the project hides the case as an example inside open-ended search, the cultural-evolution question becomes invisible and the first useful move is lost.

### C.36:3 - Forces

| Force | Tension |
|---|---|
| Domain recognizability | Music, dance, medicine, science, engineering, and organizations need familiar words such as style, tradition, technique, school, canon, platform, and regime. |
| Ontological parsimony | Those words often name slot positions or bridges over existing FPF values rather than new root kinds. |
| Variant-set usefulness | Open-ended search, archives, fronts, pools, and selected sets help keep evolving alternatives visible. |
| Cultural-evolution specificity | Variant generation and retention alone do not name transmission, recognition, memory, canon, system-role assignment, method-family evolution, or mediation. |
| Continuation and intervention value | A project may keep a sufficiently supported practice or change an identified generation, transmission, recognition, selection, memory, Method, Work, mediation, measurement, or refresh relation. A proposed change must warrant its burden and displaced work. |
| Didactic economy | The first-use pattern must be readable without becoming a cultural-evolution textbook or a list of every possible overread. |

### C.36:4 - Solution

First state the cultural-evolution case in ordinary language: which practice and variants are in play, which relations transmit, recognize, select, retain, or mediate them, what the available basis supports, and whether to continue, change, narrow, or stop. Keep the population, period, uncertainty, and receiving-use limits that matter to this conclusion. Then use the applicable FPF pattern only for a claim whose definition or test matters.

An admitted System may perform dated Work, and that Work may enact a Method. Work and Method families may organize comparison. Variants may be preserved, transmitted, selected, suppressed, or refreshed through canon or memory epistemes, recognition and selection relations, mediation systems or architectures, measurement or visibility relations, and publication forms.

These are separate facts. For every claimed Work occurrence, recover each exact actual performer through A.13 and let A.15.1 independently admit the Work. Add assignment and F.6 only when the case or receiving use expressly represents precise assignment-bound attribution. Keep families, assignments, Methods, epistemes, and selected structures distinct from the actual performers and Work.

Cultural-evolution engineering proposes or performs a deliberate change to one or more of these relations. Proposal, performed Work, actual transformation, measured effect, responsibility, authority, selected structure, and publication are different claims. Assert each as obtaining only when its own predicate is satisfied.

Keep a project choice separate from what happens across a practice or population. A project may choose or authorize an intervention, but that does not show that variants were transmitted, recognized, selected, retained, or lost. Conversely, observed spread or persistence does not authorize the project action or show that it succeeded. When both questions matter, record the project choice and performed intervention through their own patterns, then record the cultural relations and their observed change here.

When the question is how the practice may develop, retain credible hypotheses whose differences could change the continuation, forecast, or warranted use. State the uncertainty that matters; a fixed number of hypotheses is not a completion condition. Use `B.5` and `B.5.2` for a needed hypothesis account and its consequences. A bounded forecast or continuation may be complete on the available basis while a stronger explanation remains unresolved.

Select a new observation or intervention when its attainable result can improve that use enough to warrant its whole cost, delay, participant burden, and displaced work. Include the effort of designing and describing a proposed study, before treating it as an available option. Use `C.11.DUA` when that connection between a demanded inquiry and its receiving value needs recovery, and `C.11` when a named deciding System and an already formed bounded choice exist. The direct DPF or field Method designs and performs a selected inquiry; C.36 is not a general research-budget method. An unavailable or unhelpful probe withholds only the claim that needs it, not an independently supported current account. It creates no study assignment or omitted-experiment record.

Use `A.3.3` when the claim states a state space and transition law, `C.28` when the current use relies on a causal claim, and `A.15.7` for the next action during ongoing Work. Use `A.10`, `C.16`, and `C.27` for the evidence, measurement, and time questions that actually arise.

Use only the smallest form the current task needs:

- `CulturalEvolutionCaseCard@Context` keeps a multi-relation case together;
- `StyleTraditionTermBridgeTable@Context` keeps a familiar local label connected to the recovered FPF value or relation;
- `CulturalEvolutionInterventionCard@Project` retains an intervention when proposal, Work, effect, or later comparison needs explicit identity.

These forms assemble existing FPF values; cultural labels retain the object or relation meaning recovered for this use.

#### C.36:4.1 - Style And Tradition Term Bridge

Use a term bridge when a source or project label must remain usable across contexts.

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel:
  SourceContext:
  RecoveredFPFValueOrRelation:
  ApplicablePatternRef:
  SenseCellRefs:
  BridgeRefs:
  AdmissibleUse:
  BlockedUse:
  CurrentnessCondition:
```

The table records term use and any actual bridge. F.17 supplies durable term rows, F.18 supplies naming restoration, and F.9 defines bridge relations. C.36 uses the result only to keep the cultural-evolution case connected to those exact contributions.

For music and dance, a label such as `prog`, `post-prog`, `contemporary`, `hip-hop`, `battle`, `TikTok dance`, `canon`, `school`, or `technique` may point to different FPF values in different contexts. The bridge row says which one is current before the project relies on the label.

#### C.36:4.2 - Intervention Card

Use an intervention card when a project must retain the identity of a proposed or performed intervention. First write the ordinary claim: what relation will change, by what proposed action, what effect is expected, how it will be measured, and what would stop or redirect the attempt. For example: `The festival will change jury feedback timing; adoption in the next teaching cycle is the measured effect; use A.15.2 for the plan and A.3.4 only if an actual change later obtains.`

Keep proposal and performance separate. The full card below is an assurance expansion, not a first-use form.

Open its Work, assignment, transformation, effect, architecture, and publication fields only when those identities matter. `AffectedMediationSystemOrArchitectureRefs` names actual mediating Systems or architectures only. Publication refs name only the exact objects needed by the intervention; omit them otherwise. Actual access, reliance, use, and Work stay outside this field unless separately current. If actual performance is claimed, recover each exact performer through A.13 and let A.15.1 independently admit the `U.Work`. Add assignment and F.6 only when the card or receiving use expressly represents precise assignment-bound attribution; missing or failed F.6 leaves the Work intact. Add actual change and a Work-to-change relation only when each independently obtains. An effect can obtain without manufacturing a performer, assignment, or Work. Recover unresolved claim-bearing *role* wording through E.10.ROLE; a local system-role kind and classification judgment remain independently optional.

```text
CulturalEvolutionInterventionCard@Project:
  ProjectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  InterventionCardProjectUseRelationRef?: U.RelationRef, only when a named pattern defines this project-use relation and the occurrence obtains
  InterventionRef:
  CulturalEvolutionCaseRef:
  ProblemCardRef?:
  TargetedRelation:
  AffectedMethodFamilyRefs?:
  AffectedWorkFamilyRefs?:
  AffectedAssignmentSpeciesRefs?: U.RelationKindRef, each constrained under U.SystemRoleAssignment
  AffectedAssignmentOccurrenceRefs?: U.RelationRef, each constrained to U.SystemRoleAssignment and paired with its species
  AffectedCanonOrMemoryEpistemeRefs?:
  AffectedSelectionOrRecognitionRegimeRefs?:
  AffectedMediationSystemOrArchitectureRefs?:
  PublicationRefs?: refs to the exact E.17 source-backed face or E.24.PUB publication occurrence, publication form, presentation carrier, audience-declaration episteme, bounded-use-declaration episteme, or availability claim needed by this intervention
  VariantSetOrPortfolioRefs?:
  TransformationFlowStructureRef?: exact independently selected E.18 TransformationFlowStructure
  P2WCarryThroughRef?:
  WorkPlanRef?:
  InterventionSystemRoleKindRef?: U.KindRef resolving to one exact local system-role kind
  InterventionSystemRoleClassificationJudgmentRef?: U.RelationRef
  InterventionAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
  InterventionAssignmentOccurrenceRef?: U.RelationRef constrained to U.SystemRoleAssignment
  PerformedInterventionWorkRef?: U.EntityRef constrained to U.Work
  PerformedInterventionWorkAttributionRefs?: refs to obtaining F.6 performedUnderAssignment relations only when the card or receiving use expressly represents attribution
  ActualTransformationRefs?:
  WorkToTransformationOrEffectClaimRefs?:
  MeasurementRefs?:
  EffectClaimOrRelationRefs?:
  RefreshRef?:
```

`@Project` is part of the card's retrieval name. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood.

When the card is used in an actual project, `ProjectWorkOccurrenceRef` identifies the composite `U.Work`, and `InterventionCardProjectUseRelationRef` identifies the direct relation by which that Work uses the card. The suffix or either reference alone establishes no project locality. The proposed intervention, card, and project Work remain separate.

Use the expanded identity fields only when a later claim or comparison needs them. For performed intervention Work, recover each exact actual performer through A.13 and let `PerformedInterventionWorkRef` name an independently admitted A.15.1 `U.Work`. `PerformedInterventionWorkAttributionRefs`, assignment species, and assignment occurrence are optional and appear only when the card or receiving use expressly represents precise assignment-bound attribution through the same obtaining A.13 assignment. A proposal omits Work and attribution fields. A local system-role kind and classification judgment remain optional and separate. Assignment establishes no classification, Work, capability, functioning, authority, or responsibility.

**Responsibility and change.** A positive responsibility claim needs an admitted domain predicate through `TargetedRelation` or `EffectClaimOrRelationRefs`; otherwise return A.6.RCD's `missing-governor`. `ActualTransformationRefs` may cite only changes independently identified under A.3.4.

**Flow representation.** `TransformationFlowStructureRef` may cite an E.18 transformation-flow structure selected under A.22. Membership or adjacency in that structure proves neither actual change nor a Work-to-change link.

**Work-to-change.** A positive link from intervention Work to an actual transformation or effect needs a direct predicate that obtains for those participants, an exact A.6.1 application binding when that declaration supplies the link, or an admitted A.6.RCD local claim. If none applies, return the reason-specific non-assertability result.

**Effects and production.** A.15.PROD answers only its production-work, entity-inception, or completion question; it does not supply the Work-to-change link. An effect that does not require Work stays on its own direct relation. Observing a value alone does not prove the effect.

The intervention card keeps the proposed intervention, targeted relation, and next applicable pattern together; it neither authorizes Work nor establishes that a targeted effect obtains.

For planning and performance, use E.18.1 for P2W carry-through, A.15.2 for work planning, A.13 and A.15.1 for exact actual performers and independently admitted Work, and A.2.1/F.6 only when precise assignment-bound attribution is expressly consumed. Use A.3.4 for actual change. A.15.PROD may answer one current production-work, entity-inception, or completion question; the Work-to-change link still uses the direct predicate, A.6.1 binding, A.6.RCD local claim, or non-assertability result above.

For archive or pool treatment use C.18 or C.19; for a selected-set result use G.5; for local choice use C.11; for a generated or discovered result intended for architecture use, use C.35's first result: a sentence identifying the exact result by its truthful kind, its obtaining or proposed organization, the next-use condition, and the limit or return; for an architecture question use C.30; and for refresh use G.11. If audience availability is current, use E.17 for a source-backed publication face and return to source, and E.24.PUB for the publication occurrence, form, carrier, audience, bounded use, and availability.

#### C.36:4.3 - Evolution Sense Split

When generic *development* or *evolution* wording still hides the changed or represented subject, needed continuity or membership, posture, direction or value basis, or direct owner, enter through `E.10.DEV` before this split. A recovered cultural-population or discipline-facing variant claim may continue here. A non-cultural population or lineage without an admitted owner remains the exact architecture gap returned by `E.10.DEV`; do not substitute C.36. Open `E.10.MOVE` afterward only when a separately relied-on trajectory, route, path, ordering, posture, or representation ambiguity remains.

Then use this cultural split:

| Current question | Use |
|---|---|
| Generic development or evolution wording still hides the changed or represented subject, continuity or membership, posture, direction or value basis, or direct owner. | Use `E.10.DEV` first; return to C.36 only if the recovered claim is cultural-population or discipline-facing cultural evolution. |
| A bounded entity changes under conditions. | `A.3.4 U.Transformation`. |
| A temporal aspect, currentness window, rhythm, cadence, or authored temporal claim is current. | `C.27.TA`, `C.27`, or `A.3.3` according to the claim. |
| An engineering project manages an evolving archive, front, current pool, selected set, edition lineage, or family of variants. | `C.18`, `C.19`, `G.5`, `G.11`, and `E.18.1`. |
| A collective-holon or discipline-facing method, Work, system-role kind or assignment, canon, memory, recognition, selection, mediation, style, tradition, or intervention relation is current. | `C.36`. |

An engineering development loop may use C.36, but it does not automatically become cultural evolution. It becomes C.36 work only when the collective-holon or discipline-facing cultural-evolution relations above are current.

#### C.36:4.4 - Platform, Regime, And Attractor Wording

Recover the current object before accepting platform, regime, or attractor wording.

- Platform, recommendation environment, visibility infrastructure, algorithmic mediator, or platform-regime wording may name a System, a System classified under a local system-role kind, another relation participant, a system or product architecture, recognition or selection relation, measurement or visibility relation, publication relation, model-use boundary, project scope, or source-currentness relation.
- Measurement regime wording may name a characteristic space, measurement relation, visibility relation, publication relation, dashboard relation, source-currentness relation, or comparison setup.
- Attractor, basin, stable-dynamics, state-transition-law, and mathematical-model wording uses `A.3.3`, `C.27`, and `C.29` when that claim is current. Loose style metaphor remains term and bridge work through `F.17`, `F.18`, and `F.9`.

### C.36:5 - Archetypal Grounding

**Tell.** The dance-school sentence in the Problem frame is the minimum case: teachers transmit variants through teaching; an archive retains and presents records; recognition and peer copying supply their own selection relations; and one proposed intervention targets how variants enter the syllabus without claiming success.

**Show.** The engineering-product-family and music-and-dance slices below show how unlike projects recover Methods, Work, variants, memory epistemes, recognition or selection relations, mediating Systems, and refresh without inventing one root culture kind.

**Show again.** The AI-agent slice separates a project's benchmark choice from performed change and from later evidence that a wider practice generated, copied, recognized, selected, retained, or lost variants. The neighboring-boundary table then gives reduced non-use cases for claims that stay with their direct patterns.

#### C.36:5.1 - Engineering Product Family

An engineering lead has an archive of candidate cooling-module designs, a Q-front over energy use and maintainability, competitor product families, and a roadmap pressure to keep more than one line current. The first C.36 question is not "which module is best?" but whether the project is shaping a product-family culture: shared methods, work products, review criteria, memory epistemes, exact local system-role kinds and any obtaining assignments needed for Work attribution, architecture-candidate generation, selection regimes, and refresh rhythm.

If the question is only archive or front treatment, use `C.18` and `C.19`. If the team is changing how the engineering organization generates, recognizes, retains, compares, and learns from module variants, write a `CulturalEvolutionCaseCard@Context` and then use `E.18.1` to carry the accepted problem-side distinction into the next use. When that work yields a generated or discovered result intended for architecture use, use `C.35`'s one-sentence first result to state its admissible use and remaining condition before `C.32` candidate synthesis; the cultural-evolution case remains in C.36.

#### C.36:5.2 - Music And Dance Style Engineering

A dance community uses the same label for a battle practice, a theater style, a short-video platform format, a pedagogy, and a canon. C.36 starts by writing a style or tradition bridge row:

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel: "contemporary"
  SourceContext: festival choreography lab
  RecoveredFPFValueOrRelation: method family plus work family plus canon episteme plus recognition regime
  ApplicablePatternRef: C.36, F.17, F.18, F.9, A.3.1, C.20
  AdmissibleUse: compare variants inside this festival context and state what is being changed
  BlockedUse: treat the word as one root style kind across all dance contexts
  CurrentnessCondition: refresh when the festival, judging, pedagogy, or platform mediation changes
```

The bridge row is not enough when the project is changing the style ecology. Then write the case card:

```text
CulturalEvolutionCaseCard@Context:
  CaseRef: festival-contemporary-2026
  CaseScopeOrModelUseBoundary: festival choreography lab and its short-video circulation scope
  CollectiveHolonRefs: choreographer collective, dancers, teachers, judges, platform-mediated audience
  RoleWordRecoveryRefs: E.10.ROLE recovery for dancer, choreographer, teacher, judge, and viewer in this festival case
  DirectParticipationOrPositionRelationRefs: festival-performance, choreography-contribution, teaching, judging, and mediated-viewing relations when their domain predicates obtain; when an occurrence cannot be asserted, use A.6.RCD's reason-specific boundary: missing-governor, missing-information, factually unsupported, or the governing rule's inapplicable result
  SystemRoleKindRefs: omitted — the familiar dance labels do not establish local kinds without criteria
  SystemRoleClassificationJudgmentRefs: omitted — the familiar dance labels establish no classification judgment
  SystemRoleAssignmentSpeciesRefs: omitted — this family-level card asserts no assignment species
  SystemRoleAssignmentOccurrenceRefs: omitted — this family-level card asserts no assignment occurrence or performed Work; any later Work claim first recovers each exact performer through A.13 and lets A.15.1 independently admit the Work, adding A.2.1/F.6 only when precise assignment-bound attribution is expressly consumed
  WorkFamilyRefs: performance, rehearsal, teaching, judging, remixing, platform publication
  MethodFamilyRefs: floorwork method family, improvisation method family, duet-lift method family
  CanonOrMemoryEpistemeRefs: festival archive, teaching syllabus, exemplar video set
  SelectionOrRecognitionRegimeRefs: jury recognition, peer copying, platform recommendation, class adoption
  MediationSystemOrArchitectureRefs: short-video recommendation System
  PublicationRefs: festival programme form and published-video form under E.24.PUB
  MeasurementOrVisibilityRelationRefs: jury scores, replay counts, class adoption counts
  VariantSetRefs: choreography variants and teaching variants from the lab archive
  CharacteristicSpaceRefs: musical timing, body vocabulary, risk, teachability, audience recognizability
  LevelOrScopeRefs: festival scene, teaching network, platform circulation scope
  StyleOrTraditionTermRows: "contemporary" bridge row above
  CurrentEvolutionaryQuestion: change recognition and teaching methods without collapsing the style label into one root kind
  ApplicablePatternRefs: C.36, C.18, C.19, G.5, F.17, F.18, F.9, A.3.1, G.11
  RefreshRefs: refresh when platform mediation, judging, canon, or teaching adoption changes
```

The next project move may be `C.18` archive generation, `C.19` current-pool treatment, `G.5` selected-set result declaration, or an intervention card that targets recognition, pedagogy, canon, or platform mediation. If publication is current, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. The card alone does not prove that the targeted change occurred.

If the case also claims a new level, new holon, model-use or scope reframe, feedback-down relation, whole reidentification, cross-scope frustration residual, or interlevel ethical conflict, keep the C.36 result and test the additional claim separately.

For example, use B.2 or B.2.P for MHT and whole reidentification; A.1 or the applicable System or holon pattern for kind and boundary claims; B.2.5 for an obtaining supervisor-subholon feedback relation; C.30.ILC and C.29 for cross-scope architecture residual or mathematical-lens use; and D.2, D.3, or D.4 for value, harm, responsibility, or admissible sacrifice across levels.

#### C.36:5.3 - AI-Agent Framework Culture

A team develops several AI-agent framework variants and notices that evaluation dashboards change which agent patterns the community copies. The cultural-evolution case includes agent-framework method families, work products, benchmark or dashboard publications, recognition and selection regimes, mediating systems, memory epistemes, and refresh. The case keeps those values visible before the project decides whether to change the benchmark, generate new variants, declare a selected-set result, publish it, or revise the method family.

If the team chooses a new benchmark, that is a project choice, not evidence that the wider practice selected it. Record the choice with `C.11` and any planned or performed change through the applicable Work and change patterns. Use C.36 separately for later evidence that agent patterns were generated, copied, recognized, selected, retained, or lost across the practice. Widespread persistence does not retroactively authorize the project choice.

#### C.36:5.4 - Neighbor boundaries

| If the current question is... | Use... |
|---|---|
| method, technique, algorithm, practice, or developmental-machinery wording as a way of doing work | `A.3.1`, `A.3.2`, `A.15`, and `C.23` as applicable |
| discipline-level composition and comparison | `C.20` |
| term durability, naming restoration, or bridges across contexts | `F.17`, `F.18`, and `F.9` |
| archive, front, Q-front, descriptor, distance, retained exploration value, or stepping-stone value | `C.18` |
| current pool treatment, exploration or exploitation policy, graduation, narrowing, or sunset | `C.19` |
| selector-facing retained set, shortlist, ranked shortlist, specialist handoff, abstain, or escalation | `G.5` |
| refresh, deprecation, edition, source currentness, lineage, or currentness reporting | `G.11` |
| generated or discovered result intended for architecture use, architecture candidate, selected structure, architecture description, or architecture structural view | `C.35` for the exact result's admissible use, obtaining or proposed organization, next-use condition, and limit or return; `C.32` for candidate synthesis; and `C.30`, `C.30.AD`, or `C.30.ASV` for the direct architecture, description, or view question |
| new level, new holon, MHT, whole reidentification, model-use or scope reframe, supervisor-subholon feedback, cross-scope frustration residual, or interlevel ethical conflict | keep the C.36 cultural-evolution result and use A.1, B.2, B.2.P, B.2.5, C.30.ILC, C.29, D.2, D.3, D.4, or the applicable holon, System, architecture, mathematical-lens, or ethics pattern |
| local choice among already available options | `C.11`; use `C.36` separately only when generation, transmission, recognition, selection, retention, or loss across a practice or population is also current |
| problem-to-work carry-through | `E.18.1` |
| dynamics, temporal adequacy, or mathematical-lens use | `A.3.3`, `C.27`, and `C.29` |

#### C.36:5.5 - Continue the Supported Practice or Select a Useful Trial

In a constructed dance-school case, the same teachers and learners have repeatedly used the current archive examples in the stated class, and the available teaching observations support that bounded transmission claim. No participant, access, or protection condition has changed. Continue the arrangement for that class. The teachers' remaining time is needed to run it; an additional comparison would displace useful teaching without changing the present continuation. The account need not invent a rival explanation or a study, and it makes no claim about other schools or long-term retention.

Now suppose the next class must learn from the archive without teacher assistance. The current observations do not support that receiving condition. The school has an authorized preparation session in which the learners can try a representative task, access and support are available, and its result will determine whether the archive-only arrangement can be used or teaching support must remain. Select that bounded trial through the direct teaching Method. This completes the recommendation to test, not the trial or a transmission claim for the new condition. A later tested-change claim must use the actual receiving Work and observations; causal explanation remains a separate question.

### C.36:6 - Bias-Annotation

**Scope:** Limited to cultural-evolution questions about variants and their generation, transmission, recognition, selection, retention, loss, mediation, and deliberate influence across one named practice, population, collective, or Discipline boundary. C.36 is not a universal culture ontology, a project-authority rule, or a claim that every evolving engineering object is cultural evolution.

| Lens | Likely drift | Repair |
|---|---|---|
| **Gov** | A case card, project choice, intervention proposal, or observed population trend is read as authorization, responsibility, acceptance, or policy. | Keep each project decision and authority claim with its direct pattern; C.36 records only the cultural relations and intervention distinctions actually current. |
| **Arch** | One platform, archive, genre tree, lifecycle, or dashboard is treated as the cultural architecture. | Recover the relevant Methods, Work, subjects, memory epistemes, mediation, recognition, selection, measurement, and refresh relations; use architecture patterns only for actual architecture claims. |
| **Onto-Epist** | A familiar label, publication, model, score, or intervention card becomes the practice, population, variant, relation, performed Work, or effect. | Recover the object and relation under the applicable pattern; keep descriptions and records distinct from the subjects and occurrences they describe. |
| **Prag** | Every optional card field is filled, while the project still cannot say what is supported or worth continuing or changing. | Start with the one-sentence case and open only fields whose identities change the current conclusion, proposal, Work, effect, comparison, or return. |
| **Did** | Specialist evolutionary language or formal relation lists hide the recognizable project situation. | Use ordinary language first, then add the smallest exact terms and pattern references needed to make the claim and next action clear, including any boundary against a real overread. |

### C.36:7 - Conformance Checklist

| Check | Passing observation |
|---|---|
| **CC-C36-1 — Recognizable case** | The text names the practice, population, collective, or Discipline boundary; the variants; the cultural-evolution relation currently at issue; and the next action or stop. |
| **CC-C36-2 — Small first result** | A cold reader can use the one-sentence case or small case card before encountering the assurance expansion. Optional fields appear only when their identities change a later claim. |
| **CC-C36-3 — Recovered objects** | Familiar words such as *culture*, *style*, *tradition*, *practice*, *platform*, *regime*, and *technique* do not stand in for several unseparated FPF objects or relations. |
| **CC-C36-4 — Project choice** | A project decision or authorization is recorded through its direct pattern and is not offered as evidence of transmission, recognition, selection, retention, loss, intervention performance, or effect. |
| **CC-C36-5 — Proposal, Work, and effect** | A proposed intervention, planned Work, performed Work, actual transformation, Work-to-change relation, and measured effect remain separate. Every asserted Work occurrence has exact A.13-qualified performers and independent A.15.1 admission. Assignment and F.6 refs appear only when the card or receiving use expressly represents precise assignment-bound attribution. |
| **CC-C36-6 — Population observation** | Observed spread, popularity, persistence, or loss identifies its population, period, measurement, and relation; it neither authorizes the project nor proves the intervention caused the observation. |
| **CC-C36-7 — Mediation** | A platform, recommender, archive, publication, or provider is named by its actual kind and relation. Mediation does not become selection, value, authority, or cultural control by label. |
| **CC-C36-8 — Separate effect test** | The intervention's expected effect, observed value, measurement relation, and effect claim are recoverable separately; observing a value alone does not prove the effect. |
| **CC-C36-9 — Neighbor boundary** | Archive/front, pool, selected-set, local-choice, publication, architecture, currentness, transformation, Work, and mathematical-model claims use their direct patterns when current. |
| **CC-C36-10 — Source and refresh** | Every adopted SoTA move retains its stated limit and currentness trigger; a source label or newer date alone does not establish a cultural relation. |
| **CC-C36-11 — Possible development** | When the question is how the practice may develop, the answer retains credible action-changing hypotheses and relevant uncertainty; it may finish as a bounded forecast or continuation on sufficient available grounds. A selected observation or intervention has a feasible, worthwhile receiving contribution, including study-design effort and displaced work. Use `B.5`/`B.5.2` for needed hypotheses and consequences, `C.11.DUA` for a questionable inquiry demand, `C.11` for an already formed bounded choice, and the direct DPF or field Method for selected inquiry. There is no fixed hypothesis count or compulsory next probe. Actual tested change, temporal, dynamics, and causal claims keep their direct evidence conditions. |

### C.36:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
|---|---|---|
| **Project choice means population selection** | A bounded decision says what the project chose, not what a practice or population later recognized or retained. | Keep the project choice with `C.11` or its direct decision pattern and state separately the cultural relations supported by current evidence. Withhold an unsupported stronger claim; obtain new cultural evidence only when its receiving use warrants that inquiry. |
| **Performed intervention means success** | Work can occur without producing the intended transformation or effect. | Keep performed Work, actual change, Work-to-change relation, measurement, and effect claim separate. |
| **Observed spread authorizes the intervention** | Popularity or persistence supplies neither authority nor a retrospective project decision. | State the observation and its limits; use the direct authority or decision pattern for any authorization claim. |
| **One platform controls culture** | A mediating System can change visibility, transmission, or selection conditions without becoming the culture or proving control. | Identify the System, architecture, mediation relation, scope, and observed consequence separately. |
| **Archive or front equals cultural selection** | Retention in an engineering set is not automatically social recognition, population selection, use, or canon formation. | Use `C.18`/`C.19` for archive, front, and pool treatment and C.36 only for separately supported cultural relations. |
| **Popularity score equals value** | Visibility and feedback can amplify variants while measuring neither practitioner value nor effect. | Name the measurement and proxy relation; use `E.13` and the applicable value/evidence patterns when reliance is current. |
| **Local label becomes a root kind** | *Style*, *school*, *tradition*, *technique*, or *regime* can hide different objects and relations across cases. | Use the term bridge and recover the current FPF value or relation before relying on the label. |
| **Card as permission or proof** | A case or intervention card is a working episteme; a recorded Work or effect claim still needs its own grounds. | Use it only to keep exact claims together, then apply the direct pattern for each decision, Work, transformation, effect, or publication claim. |

### C.36:9 - Consequences

Positive consequences:

- practitioners can identify the cultural-evolution question and finish a qualified current account or warranted continuation, selecting a new inquiry only when it contributes enough to the receiving use;
- style, tradition, practice, platform, regime, and technique labels remain usable without becoming root kinds;
- engineering development loops, cultural-evolution cases, archive and front relations, selected-set result declaration, publication, and refresh stay distinct, with the definition and test for each current claim applied;
- music, dance, science, medicine, pedagogy, organization, product-family, and AI-agent cases can share one FPF modeling line.

Costs:

- first use must name more than one value; a cultural-evolution case is not captured by one label;
- projects must decide whether their question is variant-set generation and retention, cultural-evolution structure, architecture work, local choice, or refresh;
- durable style and tradition terms need term rows and bridge refs when they cross contexts.

### C.36:10 - Rationale

C.36 keeps a complex practical situation usable by naming a small bundle of existing FPF objects and relations instead of minting a root kind for every source word. This preserves the gain from cultural-evolution and open-ended-engineering sources while leaving Method, Work, system-role kind and assignment, discipline, episteme, selection, architecture, publication, and refresh claims with the patterns that define or test them.

### C.36:11 - SoTA-Echoing

| Source or source family | Adopted FPF move | Rejected overread | Field or boundary used |
|---|---|---|---|
| Brinkmann et al., `Machine Culture`, arXiv:2311.11388; DOI `10.1038/s41562-023-01742-2`. | Treat intelligent systems as possible mediators or generators of cultural variation, transmission, and selection. | AI agents, recommenders, platforms, or toolchains are only external aids. | `MediationSystemOrArchitectureRefs`, recognition and selection regimes, transmission, memory, and canon refs stay visible in `CulturalEvolutionCaseCard@Context`. |
| Czaplicka, Baumann, and Rahwan, algorithmic mediation and cumulative culture, arXiv:2410.00780; DOI `10.1098/rsif.2024.0686`. | Recover platform or algorithmic mediation by identifying the mediating System or architecture, any local system-role classification or direct participation relation, the recognition or selection relation, the measurement or visibility relation, and the actual scope or model-use boundary. | `platform regime` becomes a root ontology or a mere publication label. | `MediationSystemOrArchitectureRefs`, `SelectionOrRecognitionRegimeRefs`, and `ApplicablePatternRefs` identify the needed rule before platform wording is used. |
| Yaman, Tian, and Lindstrom, semantic knowledge and cultural evolution, arXiv:2510.12837; DOI `10.1073/pnas.2530750123`. | Keep method families, work families, characteristic spaces, canon or memory epistemes, and recognition regimes explicit. | Culture is shared vocabulary, random variation alone, or a genre tree. | `MethodFamilyRefs`, `WorkFamilyRefs`, `CanonOrMemoryEpistemeRefs`, and `CharacteristicSpaceRefs` are required when semantic knowledge is the live claim. |
| Tchernichovski et al., editing constraints in cultural evolution, arXiv:2502.16694. | Treat editing constraints as constraints on variant sets, characteristic spaces, and effect measurement. | Style engineering is unconstrained idea generation or one scalar taste score. | `VariantSetRefs`, `CharacteristicSpaceRefs`, and measurement or refresh exits must be named when a style intervention targets constraints; any claim that constraints actually changed still cites its exact A.3.4 and Work-to-change basis. |
| Marjieh et al., cultural-evolution mechanisms in experimental social networks, arXiv:2502.12847. | Keep topology, selection, reproduction, social-learning, and mediation relations recoverable. | Cultural evolution is one isolated innovation channel. | `CollectiveHolonRefs`, local-kind and separate classification refs, any assignment-species and assignment-occurrence refs, `SelectionOrRecognitionRegimeRefs`, and mediation refs are kept together in the case card. |
| Lee et al., melody and rhythm coevolution, arXiv:2605.05982. | Allow several feature-specific characteristic spaces inside one style or tradition case. | A style label proves one monolithic trajectory. | `CharacteristicSpaceRefs` may carry several feature spaces before selected-set or bridge claims rely on the label. |
| Gautheron et al., popularity feedback in cultural markets, arXiv:2602.09997. | Keep popularity feedback, visibility, recognition, selection, and measurement relations explicit. | Popularity or platform metrics are neutral evidence of value. | `SelectionOrRecognitionRegimeRefs`, measurement refs, and `ApplicablePatternRefs` identify whether to use `C.36`, `C.18`, `G.5`, `G.11`, or an evidence pattern. |
| Current QD and open-ended-engineering rows, including the 2026 Quality-Diversity survey DOI `10.1016/j.swevo.2025.102240`. | Keep archives, fronts, current pools, selected-set result declaration, evaluator relations, generalization pressure, and refresh distinct from the cultural-evolution case. When publication is current, also keep the source-backed face and source return distinct from the publication occurrence and audience availability. | C.36 absorbs archive, front, pool, selected-set, publication, or refresh semantics. | Use `C.18` for archive and front relations, `C.19` for current-pool treatment, `G.5` for selected-set result declaration, `G.11` for currentness and refresh, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Use C.36 only for the cultural-evolution case. |

**Source-use currentness.** One row's adopted move, rejected overread, and named field or boundary form the smallest source-use decision and stay current only until its cited edition changes, a materially newer cultural-evolution or algorithmic-mediation result challenges that transfer, the current QD/OEE line changes its archive, front, pool, selection, or refresh account, or a directly consumed FPF interface changes. At that trigger, recheck only the affected row and exact field or boundary; revise or withdraw an unsupported transfer and leave unrelated rows current.

### C.36:12 - Relations

Builds on: `A.1`, `A.2.1`, `A.3.1`, `A.3.2`, `A.3.4`, `A.15`, `A.15.1`, `A.15.6`, `A.15.PROD`, `A.22`, `C.18`, `C.19`, `C.20`, `C.23`, `E.18`, `E.18.1`, `F.6`, `F.9`, `F.17`, `F.18`, `G.5`, and `G.11`.

Coordinates with: `E.10.DEV` for generic development or evolution wording before the cultural case is known, `E.10.MOVE` for a remaining independent trajectory or path ambiguity, `C.36.P` for cultural-evolution wording repair, `A.3.3`, `A.6.1`, `A.6.RCD`, `C.11`, `C.11.DUA`, `C.16`, `C.27`, `C.29`, `C.30`, `C.30.AD`, `C.30.ASV`, `C.32`, and `C.35`.

### C.36:End

