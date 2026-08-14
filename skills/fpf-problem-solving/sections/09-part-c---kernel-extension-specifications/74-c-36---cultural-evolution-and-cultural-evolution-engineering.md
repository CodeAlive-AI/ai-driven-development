## C.36 - Cultural Evolution and Cultural-Evolution Engineering

> **Tech-name:** `CulturalEvolutionEngineering`
> **Plain-name:** cultural evolution and cultural-evolution engineering
> **Type:** Conceptual and project-use pattern (C)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part C
> **Builds on:** `A.1`, `A.2.1`, `A.3.1`, `A.3.4`, `A.15`, `A.15.1`, `A.15.6`, `A.15.PROD`, `A.22`, `C.18`, `C.19`, `C.20`, `C.23`, `E.18`, `E.18.1`, `F.6`, `F.9`, `F.17`, `F.18`, `G.5`, and `G.11`.
> **Purpose:** make cultural-evolution and cultural-evolution-engineering cases usable in FPF without minting parallel root kinds for culture, style, tradition, genre, practice, platform, regime, or technique.

### C.36:0 - Use This When

Use this pattern when the current project question is about how a culture, style, tradition, discipline practice, method family, work family, canon, recognition regime, selection regime, or mediating system changes and can be deliberately influenced.

Typical first-use situations:

- an engineering group treats its product family, toolchain, platform family, research program, or AI-agent framework as an evolving set of variants rather than one fixed system;
- a scientific, medical, pedagogical, engineering, music, dance, organizational, or AI-agent discipline is changing through related methods, work products, training forms, memory epistemes, recognition regimes, and selected variants;
- a music or dance steward needs to compare style, genre, technique, scene, canon, platform, or tradition labels without assuming that the label names one root kind;
- a project lead wants an intervention that changes generation, transmission, selection, recognition, memory, method-family, work-family, system-role-assignment, mediation, architecture, measurement, or refresh relations.

#### C.36:0.1 - What Goes Wrong If Missed

The team treats culture as shared vocabulary, treats style as a genre tree, treats a platform as the cultural object, treats a QD archive as the decision, or treats one scalar popularity or quality score as cultural development. The project can then generate many variants but still lose the relations that make those variants transmissible, recognizable, selectable, retained, refreshed, or turned into work.

#### C.36:0.2 - What This Buys

The practitioner gets one small cultural-evolution case that names the collective holons, exact local system-role kinds and any obtaining assignments that matter, work families, method families, canon or memory epistemes, recognition and selection regimes, mediation systems or architectures, variant sets, term bridges, current intervention, measurement, and refresh relation. After that, the project can apply the subject pattern for the next claim.

#### C.36:0.3 - First Useful Move

Write a compact `CulturalEvolutionCaseCard@Context`. It names what is changing, which FPF values and exact subject assertions are current, and which candidate pattern description locates the defining or constraining `ClaimGraph` for the next question.

```text
CulturalEvolutionCaseCard@Context:
  CaseRef:
  BoundedContext:
  CollectiveHolonRefs:
  RoleWordRecoveryRefs?: E.10.ROLE results for every role-like source label used by the case
  DirectParticipationOrPositionRelationRefs?: obtaining direct relations when a label resolves to a participant or organization or representation position
  SystemRoleKindRefs?: U.KindRef, each resolving to one exact local system-role kind
  SystemRoleClassificationJudgmentRefs?: U.RelationRef, each resolving a separate judgment about an admitted System
  SystemRoleAssignmentSpeciesRefs?: U.RelationKindRef, each resolving to one directly declared species under U.SystemRoleAssignment
  SystemRoleAssignmentOccurrenceRefs?: U.RelationRef, each resolving to one obtaining occurrence of a cited species
  WorkFamilyRefs:
  MethodFamilyRefs:
  MethodRelationStructureRefs?:
  MethodDescriptionRefs?:
  CanonOrMemoryEpistemeRefs:
  DisciplineRefs?:
  SelectionOrRecognitionRegimeRefs:
  MediationSystemOrArchitectureRefs?:
  MeasurementOrVisibilityRelationRefs?:
  VariantSetRefs:
  CharacteristicSpaceRefs?:
  LevelOrScopeRefs?:
  StyleOrTraditionTermRows?:
  CurrentEvolutionaryQuestion:
  CurrentPatternLocators:
  RefreshRefs?:
```

Field glosses for first use:

| Field | Meaning in the card |
|---|---|
| `VariantSetRefs` | Generated, retained, inherited, or observed variants whose cultural or engineering evolution is being considered; archive or front authority still comes from `C.18` or `C.19`. |
| `CharacteristicSpaceRefs` | The feature, descriptor, quality, constraint, or value space in which variation and selection become comparable; several feature spaces may be current in one style or tradition case. |
| `LevelOrScopeRefs` | The holon level, discipline scope, scene, product-family scope, team scope, or publication scope in which the case is being judged; this prevents one local trend from becoming the whole culture by wording. |
| `StyleOrTraditionTermRows` | Bridge rows for labels such as style, tradition, genre, school, canon, technique, scene, or platform format; these rows keep familiar terms usable without making them root kinds. |
| `CurrentEvolutionaryQuestion` | The live question. Examples include generation, transmission, recognition, selection, retention, mediation, method-family change, work-family change, architecture-candidate treatment, measurement, intervention, and refresh. |
| `CurrentPatternLocators` | The FPF patterns that define or constrain the current values. Use C.36 to keep the cultural-evolution case together; use the applicable patterns for archive, front, selected-set result declaration, actual publication, decision, work, evidence, architecture, term bridge, or refresh. |

The card is optional and thin. It is not a root U-kind, lifecycle step, evidence record, decision record, publication authority, or replacement for the named subject patterns.

### C.36:1 - Problem Frame

Many current projects no longer develop one isolated object. They shape evolving sets, for example product families, methods, research directions, medical and pedagogical practices, AI-agent frameworks, artistic styles, engineering traditions, canons, archives, frontiers, and recognition regimes. The project often generates variants cheaply, while the hard work shifts to the relations that determine what is produced, recognized, retained, selected, used, changed, or kept current. That work can include, for example, problem production, characterization, archive stewardship, comparison, selected-set result declaration, actual publication, local choice, performed Work, effect measurement, and refresh.

Cultural evolution is current when the changing set is collective-holon or discipline-facing: admitted Systems may perform independently identified dated Work; those Work occurrences enact exact Methods; memory or canon epistemes preserve what can be recognized and transmitted; recognition, selection, comparison, platform mediation, or algorithmic mediation can affect which variants survive or spread; and method families can evolve. Keep all facts required by A.15.1, A.2.1, and F.6 recoverable for each Work occurrence. A local system-role kind, separate System-classification judgment, assignment species, assignment occurrence, Work occurrence, Method, effect claim, responsibility relation, and family description remain different objects.

This pattern gives FPF a first-use cultural-evolution object without adding a new top-level part or a root ontology of culture. The same pattern can serve engineering product families, scientific research programs, medical disciplines, pedagogy, music styles, dance styles, organizational cultures, and AI-agent framework evolution because it starts from values governed by existing FPF patterns rather than from domain labels.

### C.36:2 - Problem

Culture, style, tradition, genre, scene, practice, platform, regime, technique, and developmental-machinery wording is useful but dangerous. In source and project prose, one label may point to:

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
| Intervention value | A project needs to change something: a generation relation, transmission relation, recognition relation, selection relation, memory relation, method family, work family, mediation architecture, measurement relation, work plan, performed work, or refresh relation. |
| Didactic economy | The first-use pattern must be readable without becoming a cultural-evolution textbook or a list of every possible overread. |

### C.36:4 - Solution

Recover the cultural-evolution case first, then identify the governing FPF pattern for each current value.

A cultural-evolution case is a collective-holon and discipline-facing situation. Admitted Systems may perform independently identified dated Work, and those Work occurrences may enact exact Methods. Separately identified work and method families may organize comparison. Memory or canon epistemes, recognition and selection regimes, mediation systems or architectures, measurement or visibility relations, and publication forms preserve, transmit, select, suppress, or refresh variants. Keep all facts required by A.15.1, A.2.1, and F.6 recoverable for each Work occurrence. The case card records the constellation without making a family, assignment, Method, episteme, or selected structure act.

Cultural-evolution engineering proposes or performs deliberate intervention concerning one or more of those relations. The intended intervention may target generation, transmission, selection, recognition, memory, method-family, work-family, system-role-assignment, mediation, architecture, work-plan, performed-Work, measurement, or refresh relations. A card or intention establishes none of the performed Work, actual transformation, effect, measurement, selected structure, responsibility, or authority; each positive claim needs its direct predicate or the exact missing-governor result.

Keep three record forms available:

- `CulturalEvolutionCaseCard@Context` names the case.
- `StyleTraditionTermBridgeTable@Context` maps local labels to governed FPF values and bridges.
- `CulturalEvolutionInterventionCard@Project` names the intervention and the next subject pattern.

These forms assemble current FPF values. They do not mint `U.Culture`, `U.Style`, `U.Tradition`, `U.Practice`, `U.Genre`, `U.Scene`, `U.Technique`, `U.Platform`, `U.PlatformRegime`, `U.MeasurementRegime`, or `U.DevelopmentalMachine`.

#### C.36:4.1 - Style And Tradition Term Bridge

Use a term bridge when a source or project label must remain usable across contexts.

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel:
  SourceContext:
  GovernedFPFValueOrSlot:
  SubjectPatternLocator:
  SenseCellRefs:
  BridgeRefs:
  AdmissibleUse:
  BlockedUse:
  CurrentnessCondition:
```

The table is a term-and-bridge table. `F.17` governs durable term rows, `F.18` governs naming restoration, and `F.9` governs bridge relations. C.36 uses the table only to keep cultural-evolution work connected to those subject patterns.

For music and dance, a label such as `prog`, `post-prog`, `contemporary`, `hip-hop`, `battle`, `TikTok dance`, `canon`, `school`, or `technique` may point to different FPF values in different contexts. The bridge row says which one is current before the project relies on the label.

#### C.36:4.2 - Intervention Card

Use an intervention card when one project proposes or performs a deliberate intervention concerning part of the cultural-evolution case. Keep proposal and performance separate. If actual performance is claimed, name the `U.Work` occurrence and keep all facts required by A.15.1, A.2.1, and F.6 recoverable; add actual change and a direct Work-to-change relation only when each independently obtains. If only an effect is claimed, use its own direct predicate and participants without manufacturing a performer, assignment, or Work. Recover unresolved claim-bearing *role* wording through `E.10.ROLE`; keep a local system-role kind and any separate System-classification judgment independently optional.

```text
CulturalEvolutionInterventionCard@Project:
  ProjectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  InterventionCardProjectUseRelationRef?: U.RelationRef governed by the exact intervention-use or work-use pattern
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
  VariantSetOrPortfolioRefs?:
  TransformationFlowStructureRef?: exact independently selected E.18 TransformationFlowStructure
  P2WCarryThroughRef?:
  WorkPlanRef?:
  InterventionSystemRoleKindRef?: U.KindRef resolving to one exact local system-role kind
  InterventionSystemRoleClassificationJudgmentRef?: U.RelationRef
  InterventionAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
  InterventionAssignmentOccurrenceRef?: U.RelationRef constrained to U.SystemRoleAssignment
  PerformedInterventionWorkRef?: U.EntityRef constrained to U.Work
  ActualTransformationRefs?:
  WorkToTransformationOrEffectClaimRefs?:
  MeasurementRefs?:
  EffectClaimOrRelationRefs?:
  RefreshRef?:
```

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the intervention card is genuinely used in one actual project, `ProjectWorkOccurrenceRef` identifies the exact composite `U.Work` and `InterventionCardProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the card. The suffix or either reference alone establishes no project locality. The intended intervention, card, and composite project Work remain separately identifiable.

When performed intervention Work is current, `PerformedInterventionWorkRef` names the independently identified `U.Work` occurrence. All facts required by A.15.1, A.2.1, and F.6 remain recoverable. A short card may omit only an unused assignment identifier. The local system-role kind and any System-classification judgment remain separate optional facts. Assignment establishes no Work, capability, functioning, authority, or responsibility.

A positive responsibility claim uses an admitted domain predicate through `TargetedRelation` or `EffectClaimOrRelationRefs`; without one, return the A.6.RCD missing-governor result. `ActualTransformationRefs` may cite only independently identified A.3.4 bounded changes. `TransformationFlowStructureRef` instead cites one E.18 transformation-flow structure selected under A.22; adjacency or membership in it proves neither actual change nor Work-to-change. Any positive link from intervention Work to an actual transformation or other effect must cite its declared predicate, an admitted A.6.RCD local claim, or the relevant A.15.PROD branch; otherwise return `missing-governor`. An effect that does not require Work stays on its own direct relation; observing a value neither creates nor proves it.

The intervention card does not authorize Work, and its targeted relation is not an obtaining-effect claim. It names the proposed intervention, the relation being targeted, and the next applicable pattern. Use `E.18.1` for P2W carry-through, `A.15.2` for work planning, `A.15.1` and `F.6` for performed Work, `A.3.4` for actual change, `A.15.PROD` or a direct local claim for production or Work-to-change, `C.18` or `C.19` for archive and pool treatment, `G.5` for selected-set result declaration, `C.11` for local choice, `C.35` when a generated or discovered structure-bearing carrier needs admission before architecture use, `C.30` for a direct architecture question, or `G.11` for refresh. If audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.

#### C.36:4.3 - Evolution Sense Split

Use this split before applying the pattern:

| Current question | Use |
|---|---|
| A bounded entity changes under conditions. | `A.3.4 U.Transformation`. |
| A temporal aspect, currentness window, rhythm, cadence, or authored temporal claim is current. | `C.27.TA`, `C.27`, or `A.3.3` according to the claim. |
| An engineering project manages an evolving archive, front, current pool, selected set, edition lineage, or family of variants. | `C.18`, `C.19`, `G.5`, `G.11`, and `E.18.1`. |
| A collective-holon or discipline-facing method, Work, system-role kind or assignment, canon, memory, recognition, selection, mediation, style, tradition, or intervention relation is current. | `C.36`. |

An engineering development loop may use C.36, but it does not automatically become cultural evolution. It becomes C.36 work only when the collective-holon or discipline-facing cultural-evolution relations above are current.

#### C.36:4.4 - Platform, Regime, And Attractor Wording

Recover the current object before accepting platform, regime, or attractor wording.

- Platform, recommendation environment, visibility infrastructure, algorithmic mediator, or platform-regime wording may name a system, a system classified under an exact local system-role kind, another governed relation participant, a system architecture, product architecture, recognition regime, selection regime, measurement relation, visibility relation, publication relation, bounded context, or source-currentness relation.
- Measurement regime wording may name a characteristic space, measurement relation, visibility relation, publication relation, dashboard relation, source-currentness relation, or comparison setup.
- Attractor, basin, stable-dynamics, state-transition-law, and mathematical-model wording uses `A.3.3`, `C.27`, and `C.29` when that claim is current. Loose style metaphor remains term and bridge work through `F.17`, `F.18`, and `F.9`.

### C.36:5 - Worked Slices

#### C.36:5.1 - Engineering Product Family

An engineering lead has an archive of candidate cooling-module designs, a Q-front over energy use and maintainability, competitor product families, and a roadmap pressure to keep more than one line current. The first C.36 question is not "which module is best?" but whether the project is shaping a product-family culture: shared methods, work products, review criteria, memory epistemes, exact local system-role kinds and any obtaining assignments needed for Work attribution, architecture-candidate generation, selection regimes, and refresh rhythm.

If the question is only archive or front treatment, use `C.18` and `C.19`. If the team is changing how the engineering organization generates, recognizes, retains, compares, and learns from module variants, write a `CulturalEvolutionCaseCard@Context` and then use `E.18.1` to carry the accepted problem-side distinction into the next governed use. When that work yields a generated or discovered carrier that carries or describes selected structure and may enter architecturing, use `C.35` for carrier admission before `C.32`; the cultural-evolution case remains governed here.

#### C.36:5.2 - Music And Dance Style Engineering

A dance community uses the same label for a battle practice, a theater style, a short-video platform format, a pedagogy, and a canon. C.36 starts by writing a style or tradition bridge row:

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel: "contemporary"
  SourceContext: festival choreography lab
  GovernedFPFValueOrSlot: method family plus work family plus canon episteme plus recognition regime
  SubjectPatternLocator: C.36, F.17, F.18, F.9, A.3.1, C.20
  AdmissibleUse: compare variants inside this festival context and state what is being changed
  BlockedUse: treat the word as one root style kind across all dance contexts
  CurrentnessCondition: refresh when the festival, judging, pedagogy, or platform mediation changes
```

The bridge row is not enough when the project is changing the style ecology. Then write the case card:

```text
CulturalEvolutionCaseCard@Context:
  CaseRef: festival-contemporary-2026
  BoundedContext: festival choreography lab and its short-video circulation context
  CollectiveHolonRefs: choreographer collective, dancers, teachers, judges, platform-mediated audience
  RoleWordRecoveryRefs: E.10.ROLE recovery for dancer, choreographer, teacher, judge, and viewer in this festival case
  DirectParticipationOrPositionRelationRefs: festival-performance, choreography-contribution, teaching, judging, and mediated-viewing relations when their domain predicates obtain; otherwise the corresponding row is missing-governor
  SystemRoleKindRefs: omitted — the familiar dance labels do not establish local kinds without criteria
  SystemRoleClassificationJudgmentRefs: omitted — the familiar dance labels establish no classification judgment
  SystemRoleAssignmentSpeciesRefs: omitted — this family-level card asserts no assignment species
  SystemRoleAssignmentOccurrenceRefs: omitted — this family-level card asserts no assignment occurrence or performed Work; any later Work claim names the `U.Work` occurrence and keeps all facts required by A.15.1, A.2.1, and F.6 recoverable
  WorkFamilyRefs: performance, rehearsal, teaching, judging, remixing, platform publication
  MethodFamilyRefs: floorwork method family, improvisation method family, duet-lift method family
  CanonOrMemoryEpistemeRefs: festival archive, teaching syllabus, exemplar video set
  SelectionOrRecognitionRegimeRefs: jury recognition, peer copying, platform recommendation, class adoption
  MediationSystemOrArchitectureRefs: short-video platform and festival publication forms
  MeasurementOrVisibilityRelationRefs: jury scores, replay counts, class adoption counts
  VariantSetRefs: choreography variants and teaching variants from the lab archive
  CharacteristicSpaceRefs: musical timing, body vocabulary, risk, teachability, audience recognizability
  LevelOrScopeRefs: festival scene, teaching network, platform circulation scope
  StyleOrTraditionTermRows: "contemporary" bridge row above
  CurrentEvolutionaryQuestion: change recognition and teaching methods without collapsing the style label into one root kind
  CurrentPatternLocators: C.36, C.18, C.19, G.5, F.17, F.18, F.9, A.3.1, G.11
  RefreshRefs: refresh when platform mediation, judging, canon, or teaching adoption changes
```

The next project move may be `C.18` archive generation, `C.19` current-pool treatment, `G.5` selected-set result declaration, or an intervention card that targets recognition, pedagogy, canon, or platform mediation. If publication is current, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability. The card alone does not prove that the targeted change occurred.

If this case also claims a new level, new holon, context reframe, feedback-down relation, whole reidentification, cross-scope frustration residual, or interlevel ethical conflict, keep the C.36 case card as cultural-evolution context and apply the subject pattern for that claim. For example, use `B.2` or `B.2.P` for MHT and whole-reidentification wording, `A.1` or the direct system or holon pattern for holon-kind and boundary claims, `B.2.5` for supervisor-subholon feedback when that relation is current, `C.30.ILC` and `C.29` for cross-scope architecture residual or mathematical-lens use, and `D.2`, `D.3`, or `D.4` when value, harm, responsibility, or admissible sacrifice across levels is current.

#### C.36:5.3 - AI-Agent Framework Culture

A team develops several AI-agent framework variants and notices that evaluation dashboards change which agent patterns the community copies. The cultural-evolution case includes agent-framework method families, work products, benchmark or dashboard publications, recognition and selection regimes, mediating systems, memory epistemes, and refresh. The case keeps those values visible before the project decides whether to change the benchmark, generate new variants, declare a selected-set result, publish it, or revise the method family.

### C.36:6 - Neighbor Boundaries

| If the current question is... | Use... |
|---|---|
| method, technique, algorithm, practice, or developmental-machinery wording as a way of doing work | `A.3.1`, `A.3.2`, `A.15`, and `C.23` as applicable |
| discipline-level composition and comparison | `C.20` |
| term durability, naming restoration, or bridges across contexts | `F.17`, `F.18`, and `F.9` |
| archive, front, Q-front, descriptor, distance, retained exploration value, or stepping-stone value | `C.18` |
| current pool treatment, exploration or exploitation policy, graduation, narrowing, or sunset | `C.19` |
| selector-facing retained set, shortlist, ranked shortlist, specialist handoff, abstain, or escalation | `G.5` |
| refresh, deprecation, edition, source currentness, lineage, or currentness reporting | `G.11` |
| generated or discovered structure-bearing carrier, architecture candidate, selected structure, architecture description, or architecture structural view | `C.35` for carrier admission before candidate use; `C.32` for candidate synthesis; and `C.30`, `C.30.AD`, or `C.30.ASV` for the direct architecture, description, or view question |
| new level, new holon, MHT, whole reidentification, boundary reframe, supervisor-subholon feedback, cross-scope frustration residual, or interlevel ethical conflict | keep the `C.36` cultural-evolution case and apply `A.1`, `B.2`, `B.2.P`, `B.2.5`, `C.30.ILC`, `C.29`, `D.2`, `D.3`, `D.4`, or the direct holon, system, architecture, mathematical-lens, or ethics pattern according to the recovered claim |
| local choice among already available options | `C.11` |
| problem-to-work carry-through | `E.18.1` |
| dynamics, temporal adequacy, or mathematical-lens use | `A.3.3`, `C.27`, and `C.29` |

### C.36:7 - SoTA-Echoing

| Source or source family | Adopted FPF move | Rejected overread | Field or boundary changed |
|---|---|---|---|
| Brinkmann et al., `Machine Culture`, arXiv:2311.11388; DOI `10.1038/s41562-023-01742-2`. | Treat intelligent systems as possible mediators or generators of cultural variation, transmission, and selection. | AI agents, recommenders, platforms, or toolchains are only external aids. | `MediationSystemOrArchitectureRefs`, recognition and selection regimes, transmission, memory, and canon refs stay visible in `CulturalEvolutionCaseCard@Context`. |
| Czaplicka, Baumann, and Rahwan, algorithmic mediation and cumulative culture, arXiv:2410.00780; DOI `10.1098/rsif.2024.0686`. | Recover platform or algorithmic mediation through systems, roles, recognition or selection regimes, measurement or visibility relations, and contexts. | `platform regime` becomes a root ontology or a mere publication label. | `MediationSystemOrArchitectureRefs`, `RecognitionOrSelectionRegimeRefs`, and `CurrentPatternLocators` must name the subject pattern before platform wording is used. |
| Yaman, Tian, and Lindstrom, semantic knowledge and cultural evolution, arXiv:2510.12837; DOI `10.1073/pnas.2530750123`. | Keep method families, work families, characteristic spaces, canon or memory epistemes, and recognition regimes explicit. | Culture is shared vocabulary, random variation alone, or a genre tree. | `MethodFamilyRefs`, `WorkFamilyRefs`, `CanonOrMemoryEpistemeRefs`, and `CharacteristicSpaceRefs` are not optional decoration when semantic knowledge is the live claim. |
| Tchernichovski et al., editing constraints in cultural evolution, arXiv:2502.16694. | Treat editing constraints as constraints on variant sets, characteristic spaces, and effect measurement. | Style engineering is unconstrained idea generation or one scalar taste score. | `VariantSetRefs`, `CharacteristicSpaceRefs`, and measurement or refresh exits must be named when a style intervention targets constraints; any claim that constraints actually changed still cites its exact A.3.4 and Work-to-change basis. |
| Marjieh et al., cultural-evolution mechanisms in experimental social networks, arXiv:2502.12847. | Keep topology, selection, reproduction, social-learning, and mediation relations recoverable. | Cultural evolution is one isolated innovation channel. | `CollectiveHolonRefs`, local-kind and separate classification refs, any assignment-species and assignment-occurrence refs, `RecognitionOrSelectionRegimeRefs`, and mediation refs are kept together in the case card. |
| Lee et al., melody and rhythm coevolution, arXiv:2605.05982. | Allow several feature-specific characteristic spaces inside one style or tradition case. | A style label proves one monolithic trajectory. | `CharacteristicSpaceRefs` may carry several feature spaces before selected-set or bridge claims rely on the label. |
| Gautheron et al., popularity feedback in cultural markets, arXiv:2602.09997. | Keep popularity feedback, visibility, recognition, selection, and measurement relations explicit. | Popularity or platform metrics are neutral evidence of value. | `RecognitionOrSelectionRegimeRefs`, measurement refs, and `CurrentPatternLocators` decide whether to use `C.36`, `C.18`, `G.5`, `G.11`, or an evidence pattern. |
| Current QD and open-ended-engineering rows, including the 2026 Quality-Diversity survey DOI `10.1016/j.swevo.2025.102240`. | Keep archives, fronts, current pools, selected-set result declaration, evaluator relations, generalization pressure, and refresh distinct from the cultural-evolution case. When publication is current, also keep the source-backed face and source return distinct from the publication occurrence and audience availability. | C.36 absorbs archive, front, pool, selected-set, publication, or refresh semantics. | Use `C.18` for archive and front relations, `C.19` for current-pool treatment, `G.5` for selected-set result declaration, `G.11` for currentness and refresh, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Use C.36 only for the cultural-evolution case. |

**Source-use currentness.** One row's adopted move, rejected overread, and named field or boundary form the smallest source-use decision and stay current only until its cited edition changes, a materially newer cultural-evolution or algorithmic-mediation result challenges that transfer, the current QD/OEE line changes its archive, front, pool, selection, or refresh account, or a directly consumed FPF interface changes. At that trigger, recheck only the affected row and exact field or boundary; revise or withdraw an unsupported transfer and leave unrelated rows current.

### C.36:8 - Consequences

Positive consequences:

- cultural-evolution work becomes a visible first-use pattern instead of disappearing into examples;
- style, tradition, practice, platform, regime, and technique labels remain usable without becoming root kinds;
- engineering development loops, cultural-evolution cases, archive and front relations, selected-set result declaration, publication, and refresh stay distinct, with the definition and test for each current claim applied;
- music, dance, science, medicine, pedagogy, organization, product-family, and AI-agent cases can share one FPF modeling line.

Costs:

- first use must name more than one value; a cultural-evolution case is not captured by one label;
- projects must decide whether their question is variant-set generation and retention, cultural-evolution structure, architecture work, local choice, or refresh;
- durable style and tradition terms need term rows and bridge refs when they cross contexts.

### C.36:9 - Rationale

C.36 follows the same ontological economy as the episteme and transformation settlements: a complex practical situation is made usable by naming a small relation bundle over existing FPF values rather than by minting a root kind for every source word. This preserves the working gain from cultural-evolution and open-ended-engineering sources while keeping method, Work, system-role kind and assignment, discipline, episteme, selection, architecture, publication, and refresh questions with their subject patterns.

### C.36:10 - Relations

Builds on: `A.1`, `A.2.1`, `A.3.1`, `A.3.2`, `A.3.4`, `A.15`, `A.15.1`, `A.15.6`, `A.15.PROD`, `A.22`, `C.18`, `C.19`, `C.20`, `C.23`, `E.18`, `E.18.1`, `F.6`, `F.9`, `F.17`, `F.18`, `G.5`, and `G.11`.

Coordinates with: `A.3.3`, `A.6.RCD`, `C.11`, `C.16`, `C.27`, `C.29`, `C.30`, `C.30.AD`, `C.30.ASV`, `C.32`, and `C.35`.

### C.36:End

