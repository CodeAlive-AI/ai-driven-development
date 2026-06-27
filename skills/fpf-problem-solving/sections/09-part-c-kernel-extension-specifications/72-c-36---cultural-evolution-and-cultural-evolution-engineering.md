## C.36 - Cultural Evolution and Cultural-Evolution Engineering

> **Tech-name:** `CulturalEvolutionEngineering`
> **Plain-name:** cultural evolution and cultural-evolution engineering
> **Type:** Conceptual and project-use pattern (C)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part C
> **Builds on:** `A.1`, `A.2.1`, `A.3.1`, `A.15`, `C.18`, `C.19`, `C.20`, `C.23`, `E.18.1`, `F.9`, `F.17`, `F.18`, `G.5`, and `G.11`.
> **Purpose:** make cultural-evolution and cultural-evolution-engineering cases usable in FPF without minting parallel root kinds for culture, style, tradition, genre, practice, platform, regime, or technique.

### C.36:0 - Use This When

Use this pattern when the current project question is about how a culture, style, tradition, discipline practice, method family, work family, canon, recognition regime, selection regime, or mediating system changes and can be deliberately influenced.

Typical first-use situations:

- an engineering group treats its product family, toolchain, platform family, research program, or AI-agent framework as an evolving set of variants rather than one fixed system;
- a scientific, medical, pedagogical, engineering, music, dance, organizational, or AI-agent discipline is changing through related methods, work products, training forms, memory epistemes, recognition regimes, and selected variants;
- a music or dance steward needs to compare style, genre, technique, scene, canon, platform, or tradition labels without assuming that the label names one root kind;
- a project lead wants an intervention that changes generation, transmission, selection, recognition, memory, method-family, work-family, role-assignment, mediation, architecture, measurement, or refresh relations.

#### C.36:0.1 - What Goes Wrong If Missed

The team treats culture as shared vocabulary, treats style as a genre tree, treats a platform as the cultural object, treats a QD archive as the decision, or treats one scalar popularity or quality score as cultural development. The project can then generate many variants but still lose the relations that make those variants transmissible, recognizable, selectable, retained, refreshed, or turned into work.

#### C.36:0.2 - What This Buys

The practitioner gets one small cultural-evolution case that names the collective holons, role assignments, work families, method families, canon or memory epistemes, recognition and selection regimes, mediation systems or architectures, variant sets, term bridges, current intervention, measurement, and refresh relation. After that, the project can apply the direct governing FPF pattern for the next governed use.

#### C.36:0.3 - First Useful Move

Write a compact `CulturalEvolutionCaseCard@Context`. It names what is changing, which FPF values and governing patterns are current, and which next governing pattern applies.

```text
CulturalEvolutionCaseCard@Context:
  CaseRef:
  BoundedContext:
  CollectiveHolonRefs:
  RoleValueOrAssignmentRefs:
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
  CurrentGoverningPatternRefs:
  RefreshRefs?:
```

Field glosses for first use:

| Field | Meaning in the card |
|---|---|
| `VariantSetRefs` | Generated, retained, inherited, or observed variants whose cultural or engineering evolution is being considered; archive or front authority still comes from `C.18` or `C.19`. |
| `CharacteristicSpaceRefs` | The feature, descriptor, quality, constraint, or value space in which variation and selection become comparable; several feature spaces may be current in one style or tradition case. |
| `LevelOrScopeRefs` | The holon level, discipline scope, scene, product-family scope, team scope, or publication scope in which the case is being judged; this prevents one local trend from becoming the whole culture by wording. |
| `StyleOrTraditionTermRows` | Bridge rows for labels such as style, tradition, genre, school, canon, technique, scene, or platform format; these rows keep familiar terms usable without making them root kinds. |
| `CurrentEvolutionaryQuestion` | The live question: generation, transmission, recognition, selection, retention, mediation, method-family change, work-family change, architecture-candidate treatment, measurement, intervention, or refresh. |
| `CurrentGoverningPatternRefs` | The FPF patterns that govern the current values. C.36 keeps the case together; it does not replace the patterns for archive, front, selected-set publication, decision, work, evidence, architecture, term bridge, or refresh. |

The card is optional and thin. It is not a root U-kind, lifecycle step, evidence record, decision record, publication authority, or replacement for the named governing patterns.

### C.36:1 - Problem Frame

Many current projects no longer develop one isolated object. They shape evolving sets: product families, methods, research directions, medical and pedagogical practices, AI-agent frameworks, musical styles, dance styles, engineering traditions, canons, archives, frontiers, and recognition regimes. The project often generates variants cheaply, while the hard work shifts to problem production, characterization, archive stewardship, comparison, selected-set publication, local choice, performed work, effect measurement, and refresh.

Cultural evolution is current when the changing set is collective-holon or discipline-facing: systems in roles perform related work by related methods; memory or canon epistemes preserve what can be recognized and transmitted; recognition, selection, comparison, platform mediation, or algorithmic mediation changes what variants survive or spread; and method families evolve.

This pattern gives FPF a first-use cultural-evolution object without adding a new top-level part or a root ontology of culture. The same pattern can serve engineering product families, scientific research programs, medical disciplines, pedagogy, music styles, dance styles, organizational cultures, and AI-agent framework evolution because it starts from values governed by existing FPF patterns rather than from domain labels.

### C.36:2 - Problem

Culture, style, tradition, genre, scene, practice, platform, regime, technique, and developmental-machinery wording is useful but dangerous. In source and project prose, one label may point to:

- a method family or method relation structure;
- a work family or family of performed works;
- a role value or role assignment;
- a discipline or collective holon;
- a canon or memory episteme;
- a recognition, selection, measurement, or visibility relation;
- a mediation system, product architecture, platform architecture, or algorithmic mediator;
- an archive, front, current pool, selected set, lineage, or edition set;
- a publication label or cross-context term bridge.

If the project accepts the word as ontology, FPF grows a second ontology beside method, work, role, discipline, episteme, architecture, selection, publication, and refresh. If the project hides the case as an example inside open-ended search, the cultural-evolution question becomes invisible and the first useful move is lost.

### C.36:3 - Forces

| Force | Tension |
|---|---|
| Domain recognizability | Music, dance, medicine, science, engineering, and organizations need familiar words such as style, tradition, technique, school, canon, platform, and regime. |
| Ontological parsimony | Those words often name slot positions or bridges over existing FPF values rather than new root kinds. |
| Variant-set usefulness | Open-ended search, archives, fronts, pools, and selected sets help keep evolving alternatives visible. |
| Cultural-evolution specificity | Variant generation and retention alone do not name transmission, recognition, memory, canon, role assignment, method-family evolution, or mediation. |
| Intervention value | A project needs to change something: a generation relation, transmission relation, recognition relation, selection relation, memory relation, method family, work family, mediation architecture, measurement relation, work plan, performed work, or refresh relation. |
| Didactic economy | The first-use pattern must be readable without becoming a cultural-evolution textbook or a list of every possible overread. |

### C.36:4 - Solution

Recover the cultural-evolution case first, then identify the governing FPF pattern for each current value.

A cultural-evolution case is a collective-holon and discipline-facing situation in which systems in roles perform related work families by related method families, while memory or canon epistemes, recognition and selection regimes, mediation systems or architectures, measurement or visibility relations, and publication forms preserve, transmit, select, suppress, or refresh variants.

Cultural-evolution engineering is deliberate intervention into one or more of those relations. The intervention may change generation, transmission, selection, recognition, memory, method-family, work-family, role-assignment, mediation, architecture, work-plan, performed-work, measurement, or refresh relations.

Keep three record forms available:

- `CulturalEvolutionCaseCard@Context` names the case.
- `StyleTraditionTermBridgeTable@Context` maps local labels to governed FPF values and bridges.
- `CulturalEvolutionInterventionCard@Project` names the intervention and the next governing pattern.

These forms assemble current FPF values. They do not mint `U.Culture`, `U.Style`, `U.Tradition`, `U.Practice`, `U.Genre`, `U.Scene`, `U.Technique`, `U.Platform`, `U.PlatformRegime`, `U.MeasurementRegime`, or `U.DevelopmentalMachine`.

#### C.36:4.1 - Style And Tradition Term Bridge

Use a term bridge when a source or project label must remain usable across contexts.

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel:
  SourceContext:
  GovernedFPFValueOrSlot:
  DirectGoverningPatternRef:
  SenseCellRefs:
  BridgeRefs:
  AdmissibleUse:
  BlockedUse:
  CurrentnessCondition:
```

The table is a term-and-bridge table. `F.17` governs durable term rows, `F.18` governs naming restoration, and `F.9` governs bridge relations. C.36 uses the table only to keep cultural-evolution work connected to those governing patterns.

For music and dance, a label such as `prog`, `post-prog`, `contemporary`, `hip-hop`, `battle`, `TikTok dance`, `canon`, `school`, or `technique` may point to different FPF values in different contexts. The bridge row says which one is current before the project relies on the label.

#### C.36:4.2 - Intervention Card

Use an intervention card when the project deliberately changes part of the cultural-evolution case.

```text
CulturalEvolutionInterventionCard@Project:
  InterventionRef:
  CulturalEvolutionCaseRef:
  ProblemCardRef?:
  TargetedRelation:
  AffectedMethodFamilyRefs?:
  AffectedWorkFamilyRefs?:
  AffectedRoleAssignmentRefs?:
  AffectedCanonOrMemoryEpistemeRefs?:
  AffectedSelectionOrRecognitionRegimeRefs?:
  AffectedMediationSystemOrArchitectureRefs?:
  VariantSetOrPortfolioRefs?:
  TransformationFlowStructureRef?:
  P2WCarryThroughRef?:
  WorkPlanRef?:
  WorkOccurrenceRef?:
  MeasurementOrEffectRef?:
  RefreshRef?:
```

The intervention card does not authorize work. It names the relation being changed and the next governing pattern: `E.18.1` for P2W carry-through, `A.15.2` for work planning, `A.15.1` for performed work, `C.18` or `C.19` for archive and pool treatment, `G.5` for selected-set publication, `C.11` for local choice, `C.30` for architecture, or `G.11` for refresh.

#### C.36:4.3 - Evolution Sense Split

Use this split before applying the pattern:

| Current question | Use |
|---|---|
| A bounded entity changes under conditions. | `A.3.4 U.Transformation`. |
| A temporal aspect, currentness window, rhythm, cadence, or authored temporal claim is current. | `C.27.TA`, `C.27`, or `A.3.3` according to the claim. |
| An engineering project manages an evolving archive, front, current pool, selected set, edition lineage, or family of variants. | `C.18`, `C.19`, `G.5`, `G.11`, and `E.18.1`. |
| A collective-holon or discipline-facing method, work, role, canon, memory, recognition, selection, mediation, style, tradition, or intervention relation is current. | `C.36`. |

An engineering development loop may use C.36, but it does not automatically become cultural evolution. It becomes C.36 work only when the collective-holon or discipline-facing cultural-evolution relations above are current.

#### C.36:4.4 - Platform, Regime, And Attractor Wording

Recover the current object before accepting platform, regime, or attractor wording.

- Platform, recommendation environment, visibility infrastructure, algorithmic mediator, or platform-regime wording may name a system, holon-in-role value, system architecture, product architecture, recognition regime, selection regime, measurement relation, visibility relation, publication relation, bounded context, or source-currentness relation.
- Measurement regime wording may name a characteristic space, measurement relation, visibility relation, publication relation, dashboard relation, source-currentness relation, or comparison setup.
- Attractor, basin, stable-dynamics, state-transition-law, and mathematical-model wording uses `A.3.3`, `C.27`, and `C.29` when that claim is current. Loose style metaphor remains term and bridge work through `F.17`, `F.18`, and `F.9`.

### C.36:5 - Worked Slices

#### C.36:5.1 - Engineering Product Family

An engineering lead has an archive of candidate cooling-module designs, a Q-front over energy use and maintainability, competitor product families, and a roadmap pressure to keep more than one line current. The first C.36 question is not "which module is best?" but whether the project is shaping a product-family culture: shared methods, work products, review criteria, memory epistemes, role assignments, architecture-candidate generation, selection regimes, and refresh rhythm.

If the question is only archive or front treatment, use `C.18` and `C.19`. If the team is changing how the engineering organization generates, recognizes, retains, compares, and learns from module variants, write a `CulturalEvolutionCaseCard@Context` and then use `E.18.1` to carry the accepted problem-side distinction into the next governed use.

#### C.36:5.2 - Music And Dance Style Engineering

A dance community uses the same label for a battle practice, a theater style, a short-video platform format, a pedagogy, and a canon. C.36 starts by writing a style or tradition bridge row:

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel: "contemporary"
  SourceContext: festival choreography lab
  GovernedFPFValueOrSlot: method family plus work family plus canon episteme plus recognition regime
  DirectGoverningPatternRef: C.36, F.17, F.18, F.9, A.3.1, C.20
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
  RoleValueOrAssignmentRefs: dancer, choreographer, teacher, judge, recommender-mediated viewer
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
  CurrentGoverningPatternRefs: C.36, C.18, C.19, G.5, F.17, F.18, F.9, A.3.1, G.11
  RefreshRefs: refresh when platform mediation, judging, canon, or teaching adoption changes
```

The next project move may be `C.18` archive generation, `C.19` current-pool treatment, `G.5` selected-set publication, or an intervention card that changes recognition, pedagogy, canon, or platform mediation.

If this case also claims a new level, new holon, context reframe, feedback-down relation, whole reidentification, cross-scope frustration residual, or interlevel ethical conflict, keep the C.36 case card as cultural-evolution context and apply the direct governing pattern for that claim. For example, use `B.2` or `B.2.P` for MHT and whole-reidentification wording, `A.1` or the direct system or holon pattern for holon-kind and boundary claims, `B.2.5` for supervisor-subholon feedback when that relation is current, `C.30.ILC` and `C.29` for cross-scope architecture residual or mathematical-lens use, and `D.2`, `D.3`, or `D.4` when value, harm, responsibility, or admissible sacrifice across levels is current.

#### C.36:5.3 - AI-Agent Framework Culture

A team develops several AI-agent framework variants and notices that evaluation dashboards change which agent patterns the community copies. The cultural-evolution case includes agent-framework method families, work products, benchmark or dashboard publications, recognition and selection regimes, mediating systems, memory epistemes, and refresh. C.36 keeps those values visible before the project decides whether to change the benchmark, generate new variants, publish a selected set, or revise the method family.

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
| architecture candidate, selected structure, architecture description, or architecture structural view | `C.30`, `C.30.AD`, and `C.30.ASV` |
| new level, new holon, MHT, whole reidentification, boundary reframe, supervisor-subholon feedback, cross-scope frustration residual, or interlevel ethical conflict | keep the `C.36` cultural-evolution case and apply `A.1`, `B.2`, `B.2.P`, `B.2.5`, `C.30.ILC`, `C.29`, `D.2`, `D.3`, `D.4`, or the direct holon, system, architecture, mathematical-lens, or ethics pattern according to the recovered claim |
| local choice among already available options | `C.11` |
| problem-to-work carry-through | `E.18.1` |
| dynamics, temporal adequacy, or mathematical-lens use | `A.3.3`, `C.27`, and `C.29` |

### C.36:7 - SoTA-Echoing

| Source or source family | Adopted FPF move | Rejected overread | Field or boundary changed |
|---|---|---|---|
| Brinkmann et al., `Machine Culture`, arXiv:2311.11388; DOI `10.1038/s41562-023-01742-2`. | Treat intelligent systems as possible mediators or generators of cultural variation, transmission, and selection. | AI agents, recommenders, platforms, or toolchains are only external aids. | `MediationSystemOrArchitectureRefs`, recognition and selection regimes, transmission, memory, and canon refs stay visible in `CulturalEvolutionCaseCard@Context`. |
| Czaplicka, Baumann, and Rahwan, algorithmic mediation and cumulative culture, arXiv:2410.00780; DOI `10.1098/rsif.2024.0686`. | Recover platform or algorithmic mediation through systems, roles, recognition or selection regimes, measurement or visibility relations, and contexts. | `platform regime` becomes a root ontology or a mere publication label. | `MediationSystemOrArchitectureRefs`, `RecognitionOrSelectionRegimeRefs`, and `CurrentGoverningPatternRefs` must name the governing pattern before platform wording is used. |
| Yaman, Tian, and Lindstrom, semantic knowledge and cultural evolution, arXiv:2510.12837; DOI `10.1073/pnas.2530750123`. | Keep method families, work families, characteristic spaces, canon or memory epistemes, and recognition regimes explicit. | Culture is shared vocabulary, random variation alone, or a genre tree. | `MethodFamilyRefs`, `WorkFamilyRefs`, `CanonOrMemoryEpistemeRefs`, and `CharacteristicSpaceRefs` are not optional decoration when semantic knowledge is the live claim. |
| Tchernichovski et al., editing constraints in cultural evolution, arXiv:2502.16694. | Treat editing constraints as constraints on variant sets, characteristic spaces, and effect measurement. | Style engineering is unconstrained idea generation or one scalar taste score. | `VariantSetRefs`, `CharacteristicSpaceRefs`, and measurement or refresh exits must be named when a style intervention changes constraints. |
| Marjieh et al., cultural-evolution mechanisms in experimental social networks, arXiv:2502.12847. | Keep topology, selection, reproduction, social-learning, and mediation relations recoverable. | Cultural evolution is one isolated innovation channel. | `CollectiveHolonRefs`, `RoleAssignmentRefs`, `RecognitionOrSelectionRegimeRefs`, and mediation refs are kept together in the case card. |
| Lee et al., melody and rhythm coevolution, arXiv:2605.05982. | Allow several feature-specific characteristic spaces inside one style or tradition case. | A style label proves one monolithic trajectory. | `CharacteristicSpaceRefs` may carry several feature spaces before selected-set or bridge claims rely on the label. |
| Gautheron et al., popularity feedback in cultural markets, arXiv:2602.09997. | Keep popularity feedback, visibility, recognition, selection, and measurement relations explicit. | Popularity or platform metrics are neutral evidence of value. | `RecognitionOrSelectionRegimeRefs`, measurement refs, and `CurrentGoverningPatternRefs` decide whether to use `C.36`, `C.18`, `G.5`, `G.11`, or an evidence pattern. |
| Current QD and open-ended-engineering rows, including the 2026 Quality-Diversity survey DOI `10.1016/j.swevo.2025.102240`. | Keep archives, fronts, current pools, selected-set publication, evaluator relations, generalization pressure, and refresh with their governing patterns. | C.36 absorbs archive, front, pool, selected-set, or refresh semantics. | `C.18`, `C.19`, `G.5`, and `G.11` stay as named governing patterns; C.36 carries only the cultural-evolution case when that case is current. |

### C.36:8 - Consequences

Positive consequences:

- cultural-evolution work becomes a visible first-use pattern instead of disappearing into examples;
- style, tradition, practice, platform, regime, and technique labels remain usable without becoming root kinds;
- engineering development loops, cultural-evolution cases, archive and front relations, selected-set publication, and refresh stay separated by governing pattern;
- music, dance, science, medicine, pedagogy, organization, product-family, and AI-agent cases can share one FPF modeling line.

Costs:

- first use must name more than one value; a cultural-evolution case is not captured by one label;
- projects must decide whether their question is variant-set generation and retention, cultural-evolution structure, architecture work, local choice, or refresh;
- durable style and tradition terms need term rows and bridge refs when they cross contexts.

### C.36:9 - Rationale

C.36 follows the same ontological economy as the episteme and transformation settlements: a complex practical situation is made usable by naming a small relation bundle over existing FPF values rather than by minting a root kind for every source word. This preserves the working gain from cultural-evolution and open-ended-engineering sources while keeping method, work, role, discipline, episteme, selection, architecture, publication, and refresh authority with their governing patterns.

### C.36:10 - Relations

Builds on: `A.1`, `A.2.1`, `A.3.1`, `A.3.2`, `A.15`, `C.18`, `C.19`, `C.20`, `C.23`, `E.18.1`, `F.9`, `F.17`, `F.18`, `G.5`, and `G.11`.

Coordinates with: `A.3.3`, `C.11`, `C.16`, `C.27`, `C.29`, `C.30`, `C.30.AD`, `C.30.ASV`, and `E.18`.

### C.36:End

