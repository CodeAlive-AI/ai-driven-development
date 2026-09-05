## C.18 - Open-Ended Search Archive and Front Stewardship

> **Tech-name:** `OpenEndedSearchArchiveAndFrontStewardship`
> **Plain-name:** open-ended search archive and front stewardship
> **Type:** C-pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part C
> **Builds on:** `C.16`, `A.19.CPM`, `A.19.SelectorMechanism`, and `E.18`.
> **Coordinates with:** `C.19`, `C.11.CRC`, `C.11`, `C.28`, `G.5`, `G.9`, `G.11`, `E.23`, `E.18.1`, `E.17`, `E.24.PUB`, the `C.30` family, `C.32.P2S`, `C.32`, `C.35`, `C.36`, `F.17`, `F.18`, `F.9`, and the A.15 family.
> **Purpose:** make archive, front, Q-front, descriptor, telemetry, retained exploration value, stepping-stone value, lineage, edition, architecture-candidate generation, and cultural-variant generation usable without turning them into publication, decision, work permission, or cultural-evolution authority.

### C.18:0 - Use This When

Use this pattern when a project needs to generate, retain, compare, or report many candidate variants while preserving descriptor editions, distance definitions, archive policies, front semantics, telemetry, lineage, retained exploration value, and any action-bearing claim that generation stayed inside or changed the effective possibility space.

Typical cases include quality-diversity archives, open-ended engineering variant sets, Pareto or Q-front treatment, phenotype-like descriptor maps, architecture-candidate generation, style or tradition variant generation, scientific or engineering school variants, and candidate pools whose value is not captured by one immediate selected set.

#### C.18:0.1 - What Goes Wrong If Missed

The project treats an archive as a shortlist, a front as a decision, illumination telemetry as dominance, a retained stepping stone as current best, or a cultural-style variant as a root cultural kind. Generation looks productive, but the next relation is unclear—for example, whether to retain, compare, declare a selected-set result, choose locally, plan work, measure effects, refresh, or write a cultural-evolution case.

#### C.18:0.2 - What This Buys

The practitioner gets separate records for archive, front, and generation. Together, these records pin descriptors, characteristic spaces, edition refs, retention policy, telemetry, lineage, and next governing relation. Downstream selection, architecture, cultural evolution, work planning, measurement, and refresh then start from named records rather than from a broad archive label.

### C.18:1 - Problem Frame

Open-ended search and quality-diversity work deliberately keep more than one candidate alive. That is useful for engineering, science, design, music, dance, AI-agent frameworks, medical method families, and other evolving practices. The same archive or front label can hide strong candidates, weak but promising stepping stones, coverage-expanding variants, architecture candidates, cultural variants, and telemetry-only signals.

The primary `EntityOfConcern` in C.18 is the archive or front relation being stewarded: which variants are generated or retained, under which descriptor and characteristic space, with which edition and lineage pins, and with which next relation available. C.18 does not answer a local-choice, selector-result declaration, cultural-evolution, or architecture question.

### C.18:2 - Problem

Without C.18, a team often compresses several different objects into one word such as archive, front, Q-front, portfolio, style pool, or candidate set. That loses the distinctions between front, archive, and telemetry use:

- a front answers current non-domination under a declared comparator or dominance set;
- an archive answers retained exploration value, coverage, stepping-stone value, or future reachability under a declared retention policy;
- telemetry reports search health, coverage, novelty, diversity, or lineage but does not by itself dominate alternatives.

Use `G.5` for downstream selected-set result declaration, `C.11` for local choice, the applicable `C.30` or `C.32` pattern for an architecture claim or candidate, `C.36` for cultural-evolution case work, `A.15.2` for planning, `A.15.1` for performed Work, and `G.11` for currentness and refresh.

### C.18:3 - Forces

| Force | Tension |
|---|---|
| Exploration value | A retained variant may be valuable as a stepping stone even when it is not on the current front. |
| Front honesty | A front must preserve the declared comparator, dominance set, admissibility, and partial-order semantics. |
| Descriptor currentness | Descriptor maps, distance definitions, characteristic spaces, and family coordinates change over time. |
| Practical continuation | Engineering teams need selected sets, architecture candidates, work plans, and measurements from archives without letting the archive authorize those moves. |
| Cultural and style cases | Music, dance, science, medical, product, and AI-agent variants need source labels and term bridges without minting cultural root kinds. |
| Telemetry usefulness | Coverage, novelty, diversity, QD score, and lineage are useful signals but can be overread as value, proof, or decision. |

### C.18:4 - Solution

Keep records for archive, front, telemetry, generation, and downstream relations separate.

#### C.18:4.1 - Archive Record

```text
ExplorationArchiveRecord@Context:
  archiveRef:
  variantSetRef:
  descriptorMapRef:
  characteristicSpaceRef:
  distanceDefinitionRef?:
  retentionPolicyRef:
  retainedExplorationValue:
  steppingStoneUse?:
  lineageOrEditionPins:
  telemetryRefs?:
  currentnessAsOf:
  currentStatus:
  stopOrRefreshReason:
  nextGoverningRelation:
```

Use this record when the current question is about archive use—for example, retained exploration value, coverage, novelty, diversity, stepping-stone value, future reachability, curriculum expansion, lineage, or archive policy. Do not use the archive record as a selected-set result declaration or work permission.

#### C.18:4.2 - Front Record

```text
FrontRecord@Context:
  frontRef:
  candidateSetRef:
  comparatorOrDominanceSetRef:
  admissibilityRef:
  descriptorMapRef?:
  characteristicSpaceRef?:
  relationTokenSetRef:
  excludedTelemetryRefs?:
  selectedSetResultRef?:
  currentnessAsOf:
  currentStatus:
  stopOrRefreshReason:
  nextGoverningRelation:
```

Use this record when the current question is about front use—for example, non-domination, Pareto relation, Q-front membership, comparator currentness, admissibility, or partial-order preservation. The front may feed a later G.5 use, but it is not itself a declared selected-set result; declare that result from the front through `G.5` under its own basis.

#### C.18:4.2a - Filled Archive And Front Micro-Records

```text
ExplorationArchiveRecord@Context:
  archiveRef: dance-lab-variant-archive-2026
  variantSetRef: choreography variants generated during a festival lab
  descriptorMapRef: timing, body vocabulary, risk, teachability, audience recognizability
  characteristicSpaceRef: festival style-engineering characteristic space
  distanceDefinitionRef: difference in timing and body-vocabulary descriptors
  retentionPolicyRef: keep rare but teachable variants and variants that open later combination work
  retainedExplorationValue: stepping stones for teaching and later style intervention
  steppingStoneUse: candidate material for C.36 cultural-evolution case work
  lineageOrEditionPins: lab session, teacher edit, platform-publication edition
  telemetryRefs: replay counts, class adoption counts, jury notes
  currentnessAsOf: lab records and platform-publication edition reviewed through 2026-07-31
  currentStatus: active for retained exploration and teaching use
  stopOrRefreshReason: reopen through G.11 if the teaching-use judgement, retention policy, lineage, or platform edition changes
  nextGoverningRelation: C.36
```

For this example's current question, the field names `C.36` as the next applicable pattern. If one of the stated changes makes refresh current, `G.11` becomes the next applicable pattern instead; it is not a second simultaneous locator.

```text
FrontRecord@Context:
  frontRef: cooling-module-maintainability-energy-front
  candidateSetRef: retained cooling-module architecture candidates
  comparatorOrDominanceSetRef: energy-use and maintainability comparator
  admissibilityRef: safety and manufacturing constraints already admitted by project policy
  descriptorMapRef: thermal performance, service access, part count, manufacturing tolerance
  characteristicSpaceRef: product-family architecture characteristic space
  relationTokenSetRef: comparison relation-token set supporting non-dominated candidates under current comparator
  excludedTelemetryRefs: tests outside the current temperature envelope
  currentnessAsOf: comparator, safety constraints, and test evidence reviewed through 2026-07-31
  currentStatus: active non-dominated front for the declared comparator
  stopOrRefreshReason: reopen if eligibility, comparator, dominance grounds, or evidence edition changes
  nextGoverningRelation: C.30
```

For this example's current question, the field names `C.30` as the next applicable pattern. Omit `selectedSetResultRef?` until an exact G.5 result exists. If declaring a selector outcome later becomes current, start a separate `G.5` use; if the front's basis changes, start `G.11` refresh. Neither possible continuation belongs in the current locator.

#### C.18:4.3 - Generation And Downstream-Use Record

When loop-engineering practice generates many candidates—for example, agent prompts, harness variants, workflow variants, or framework seeds—use `C.18` to record generation, archive, front, descriptors, telemetry, retained exploration value, lineage, and the next applicable pattern. This does not say that the loop improved. Use `E.23` only when one retained object version is changed and re-evaluated through repeated passes under a declared object-under-improvement evaluation; use `G.9` for parity between variants and `G.5` when a selected-set result must be declared.

```text
OpenEndedVariantGenerationRecord@Project:
  problemCardRef?:
  generationMethodOrFamilyRef:
  sourceRefs?:
  evaluatorOrComparatorRef?:
  emitterPolicyRef?:
  insertionPolicyRef?:
  dedupThreshold?:
  deduplicationBasisRef?:
  deduplicationUnit?:
  variantSetRef:
  descriptorMapRef:
  characteristicOrDescriptorSetRef:
  archiveOrFrontRef?:
  architectureCandidateRefs?:
  culturalVariantRefs?:
  telemetryRefs?:
  projectLocality?:
    generationWorkOccurrenceRef:
    compositeProjectWorkOccurrenceRef:
    governingRelationPatternRef:
    exactGenerationToProjectRelationRef:
  workPlanOrMeasurementRef?:
  refreshRef?:
  currentnessAsOf:
  currentStatus:
  stopOrRefreshReason:
  nextGoverningRelation:
```

Across the archive, front, and generation records, `currentnessAsOf` names the replay date or window together with the relevant pinned editions; `currentStatus` states whether the recorded archive/front/generation relation is active, held, closed, or stale for its declared use; and `stopOrRefreshReason` names the condition that ended it or the exact trigger that would reopen its currentness. These fields record the boundary but do not perform refresh. When source, descriptor, comparator, policy, evidence, or edition currentness becomes the live question, `nextGoverningRelation` points to `G.11` and `refreshRef?` may cite the separately governed refresh record.

Here `@Project` is a compatibility and retrieval cue, not a project kind or relation assertion. Fill `projectLocality?` only after both Work occurrences have been admitted independently and the cited relation actually obtains under its direct governor. `generationWorkOccurrenceRef` names the exact dated generation `U.Work`; `compositeProjectWorkOccurrenceRef` names the selected composite project `U.Work`; and `exactGenerationToProjectRelationRef` cites, rather than creates, the exact work-part, containing-work, decision-use, source-use, or other governed relation. Use work parthood only when the complete `A.15.1` basis holds. Otherwise omit `projectLocality?`: the `@Project` suffix remains retrieval-only and establishes no project Work, parthood, authority, context, or viewpoint.

For example, a completed harness-generation run may state:

```text
projectLocality:
  generationWorkOccurrenceRef: HarnessVariantGenerationRun-2026-07-31 : U.Work
  compositeProjectWorkOccurrenceRef: AgentHarnessProjectWork-2026 : U.Work
  governingRelationPatternRef: A.15.1
  exactGenerationToProjectRelationRef: OperationalPartOf_work(HarnessVariantGenerationRun-2026-07-31, AgentHarnessProjectWork-2026)
```

Every optional field whose name ends in `Ref?` points to a separately identified object, claim, policy profile, or measurement basis. `dedupThreshold?` is not a reference: it carries one declared scalar threshold value. `deduplicationUnit?` carries its unit literal. Fill `emitterPolicyRef?` and `insertionPolicyRef?` only when the cited C.19 profile or insertion policy applies to the current pool treatment. When a threshold is inherited, the cited profile supplies `dedupThreshold`, `deduplicationBasisRef`, and `deduplicationUnit`; when it is not inherited, carry the scalar in `dedupThreshold?` and its basis and unit in `deduplicationBasisRef?` and `deduplicationUnit?`. These references and scalars do not give C.19 a generation operation or change the archive and front relations stated through C.18. In particular, `problemCardRef?` may cite a C.22.2 problem-side episteme but creates neither an actual Problem nor a `ProblematicForRelation` under `C.22.PFR`. Naming a generated variant, archive entry, front membership, telemetry value, or retained-exploration claim alone establishes neither an improvement-result nor a work-result identity and creates no relation from generation Work to a result. `nextGoverningRelation` is a locator for the next applicable pattern; it does not itself make a choice, declare a selected-set result, authorize work, perform refresh, or make any relation obtain.

Use this record when generation is current. For architecture moves involving candidates named in `architectureCandidateRefs`, use `C.30`, `C.30.ASV`, or `C.30.AD` as applicable. Use `C.36` for cultural-evolution cases involving variants named in `culturalVariantRefs`. Local choice uses `C.11`; work planning and performed work use the A.15 family; effect measurement uses its direct measurement and evaluation patterns; refresh uses `G.11`. P2W carry-through uses `E.18.1` when an accepted problem-side distinction must be preserved into the next relation.

#### C.18:4.3a - Distinguish exploration inside a space from change to the space

Apply this branch only when whether the effective possibility space changed can alter retention, comparison, generation, architecture, or the next decision. Start by declaring the current space through the candidate grammar or type boundary, generator and operators, available building blocks, evaluator or comparator, retention or reproduction rule, goals or actions, and environment that matter for this case. The declaration may be ordinary domain content or a cited description; it does not create a universal `PossibilitySpace` kind.

Then state the smallest supported mode:

| Mode wording | Required claim | Blocked overread |
| --- | --- | --- |
| **exploratory** | The candidate, trajectory, or recombination is new or distant under the declared descriptors but remains admissible under the same effective generator, types/operators, evaluator, retention rule, and environment. | Archive distance, novelty, local learning progress, or rarity does not prove that the space expanded. |
| **expansive** | A new dimension, candidate type, operator, building block, goal/action, or reachable region becomes admissible while the higher-order generation/evaluation regime remains sufficiently comparable for the stated use. | A newly visited region is not expansion unless it was unavailable under the earlier effective space. |
| **transformational** | The rule or representation that generates, admits, evaluates, retains, reproduces, or environmentally enables candidates changes so that what counts as a candidate, successor, or acceptable result changes. | Rewording, a new score, or one surprising candidate does not establish a changed regime. |

The first result is one ordinary `C.2.1` claim naming the earlier and candidate space declarations, exact changed component, mode wording, counterfactual or trajectory evidence, uncertainty, blocked stronger claim, and next governing relation. Use `C.28` for a causal claim that the component change produced the new reachability. Use `C.11.CRC` when a finite space-changing intervention must be compared with the current configuration, and `C.11` for the later choice.

Stop at ordinary same-space exploration when no action depends on the stronger mode. Reopen only when the candidate grammar, generator, operator set, evaluator, retention/reproduction rule, goals/actions, environment, evidence, or receiving decision changes.

**Worked micro-case.** A cooling-module search previously admits only fixed rectangular layouts assembled by the same connection operators and evaluated under the same thermal/maintainability comparator. A new layout far from the archive remains exploratory if those rules still admit it. Adding a validated curved-channel building block and operator is expansive only when the earlier generator could not express the resulting layouts and the comparison still uses a compatible higher-order regime. Replacing candidate admission and retention with a context-adaptive rule that changes which successors count is transformational only when the earlier/candidate rule mapping and observed reachability support that stronger claim. A higher novelty score alone establishes none of these transitions.


#### C.18:4.4 - Front And Archive Are Different Returns


- Start from one declared candidate or eligibility set.
- Return the non-dominated front from the relation-token set under the declared comparator or dominance set.
- Return the exploration archive separately when retained exploration value, coverage, novelty, diversity, stepping-stone value, or future reachability is current.
- Keep tie-breakers and telemetry explicit so diversity, illumination, or popularity signals do not rewrite front semantics.
- Before promoting telemetry or a popularity-like signal into the comparator, dominance set, or selected-set criteria, state which intended archive/front use or value becomes worse when that signal improves and cite the policy or decision authority that admits the trade-off. If either answer is missing, keep the signal as telemetry or an explicitly bounded tie-breaker rather than silently promoting it.
- Use `RetentionIntent=steppingStone` when retention exists for frontier expansion or later curriculum value rather than current dominance.
- If one source line keeps both returns, say that the front answers current non-domination while the archive answers retained exploration value.

#### C.18:4.5 - Cultural And Architecture Variant Boundaries

For architecture-candidate generation, C.18 records generation, archive, front, descriptor, telemetry, and retained exploration value. C.30 governs the architecture claim: `ArchitectureOf@Context`, selected structure or structure kind, affected characteristic, and next architecture move.

For cultural variants, C.18 records the generated or retained variant set and its descriptors, lineage, telemetry, and archive or front relation. Use C.36 for a cultural-evolution case when collective-holon or discipline-facing Method, Work, system-role kind or assignment, canon, memory, recognition, selection, mediation, style, tradition, or intervention relations are current. Use F.17, F.18, and F.9 for durable term and bridge work for labels such as style, tradition, genre, scene, school, and technique.

### C.18:5 - Conformance Checklist

- `CC-C18-1` Descriptor, characteristic, distance, and family-coordinate refs are named before generation, archive update, or front publication.
- `CC-C18-2` Archive and front returns are separate from a selected-set result unless one is explicitly declared from them through `G.5`.
- `CC-C18-3` Telemetry remains telemetry unless a declared policy promotes it into the comparator, dominance set, or selected-set criteria and the governing record names both the intended archive/front use or value made worse by that promotion and the authority that admits the trade-off.
- `CC-C18-4` Retained exploration value, stepping-stone use, lineage, and edition pins are recorded for archive use.
- `CC-C18-5` Use C.30 family patterns before making an architecture move with a candidate.
- `CC-C18-6` Use C.36 for cultural-evolution claims about variants, and term-bridge patterns when durable label or bridge work is current.
- `CC-C18-7` Refresh uses `G.11` with the smallest affected archive, front, descriptor, edition, or lineage locus.
- `CC-C18-8` Agent-loop, harness-loop, workflow-store, or DPF-seed variants retained in an archive name their descriptor, lineage, telemetry, and next governing relation; archive membership alone establishes no quality improvement. Quality-improvement claims require their own re-evaluation; use `E.23` only for repeated improvement passes.
- `CC-C18-9` A filled `projectLocality?` names independently admitted dated generation and composite project `U.Work` occurrences, the subject pattern, and one exact obtaining relation; `@Project` alone remains retrieval-only.
- `CC-C18-10` Problem-card, result, selected-set, choice, work, and refresh references remain references to separately governed objects or next subject patterns and create none of those identities or relations.
- `CC-C18-11` The SoTA basis names its reviewed-through boundary and exact mutable editions; a material source revision, newer field survey, or contrary archive, descriptor-generalization, or OEE-evaluation evidence records a reopen trigger and hands refresh to `G.11`.
- `CC-C18-12` When the §4.3a branch applies, exploratory, expansive, or transformational wording names the earlier and candidate effective space declarations, changed component, counterfactual or trajectory evidence, uncertainty, blocked stronger claim, and next relation; distance, rarity, novelty, or local progress alone does not prove space change.





### C.18:6 - Archetypal Grounding

**System-facing case.** A robotics team generates gait variants. The front records non-dominated speed and energy relations under declared measures. The archive retains diverse coordination patterns because some are stepping stones for new terrain. Telemetry reports coverage. A selected-set result may later be declared through `G.5`. If it must be available to an audience, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability. Performed test runs use A.15.

**Architecture case.** A cooling-module project keeps an archive of modular layout variants and a front over maintainability and energy use. C.18 records descriptors, archive policy, front relation, and telemetry. Use C.30 to name the selected structure and affected architecture characteristic, then decide whether to make an architecture move with a retained variant.

**Cultural case.** A dance-lab project generates movement variants around several source labels. C.18 records generated variants, descriptors, archive membership, front relation, and lineage. Use C.36 to determine whether the lab is deliberately changing the cultural practice; F.17, F.18, and F.9 handle the label bridges.

### C.18:7 - Bias-Annotation

Lexical and semiotic bias are controlled by keeping archive, front, telemetry, selected-set result declaration, audience publication, local choice, cultural-evolution case, architecture move, work permission, and evidence relations distinct. Mathematical descriptions of descriptor maps, fronts, distances, coverage, or novelty use the mathematical-lens pattern when lens adequacy matters.

### C.18:8 - Consequences

Positive consequences:

- archives keep exploration value while local choice remains separately governed;
- fronts preserve partial-order and comparator semantics;
- architecture and cultural-variant generation become usable without creating parallel root kinds;
- refresh and source-currentness have clear loci.

Costs:

- teams must keep at least archive and front records separate;
- one generated variant may need several downstream records before it becomes selected, chosen, planned, worked, measured, or refreshed;
- descriptor editions and distance definitions require maintenance.

### C.18:9 - Rationale

Current quality-diversity, illumination search, open-ended engineering, and evolutionary-engineering practice shows that retained diversity, stepping stones, archive lineage, and descriptor currentness often matter before a single choice is justified. FPF keeps that practical gain while preventing archive and front language from replacing comparison, selected-set result declaration, audience publication, architecture, cultural evolution, work, evidence, decision, or refresh patterns.

### C.18:10 - SoTA-Echoing

**Source-currentness boundary.** This source-use basis was reviewed through 2026-08-26. Mutable preprints are pinned below to the edition actually used; the Qin et al. survey is pinned to its DOI-fixed journal article. Reopen the affected source-use row through `G.11` when a cited revision changes the archive, front, generation, or evaluation claim used here; when a newer field survey materially changes the known QD/OEE boundary; or when contrary evidence changes what can be claimed about bounded archives, descriptor generalization, or open-ended evaluation. C.18 records that trigger and the affected row but does not itself perform refresh.

| Source or source family | Adopted FPF move | Rejected overread | Field or boundary changed |
|---|---|---|---|
| Lin et al., `Quality-Diversity Optimization as Multi-Objective Optimization`, arXiv:2602.00478v1 (2026-01-31). | Treat QD and Q-front work through declared Q components, `DominanceSet`, comparator refs, archive relation, front relation, G.5 selected-set result declaration, separate audience publication, and refresh. | Cell-filling or popularity accounts are the current ontology by default. | `FrontRecord@Context` must keep dominance grounds, comparator refs, and Q-component refs explicit. |
| Qin et al., `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI `10.1016/j.swevo.2025.102240`, `https://www.sciencedirect.com/science/article/pii/S2210650225003979`. | Use current survey support for approaches, applications, archive use, diversity use, and challenge framing. | Survey taxonomy replaces FPF relation definitions. | Use `C.18` to state and test the `ExplorationArchiveRecord@Context`, `FrontRecord@Context`, and `OpenEndedVariantGenerationRecord@Project`; use `G.5` for selected-set result declaration, `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence and audience availability, and `G.11` for refresh. |
| Batra et al., `Quality Diversity for Robot Learning: Limitations and Future Directions`, arXiv:2407.17515v1 (2024-07-09). | State retained exploration value, generalization pressure, and limitations when an archive is used beyond current dominance. | Bounded archives or cell occupancy are enough evidence that NQD and OEE are useful. | `retainedExplorationValue`, `retentionPolicyRef`, `telemetryRefs`, and `nextGoverningRelation` must be filled when the archive is relied on. |
| Zhang et al., `Darwin Godel Machine`, arXiv:2505.22954v3 (2026-03-12). | Keep generated agents, archive lineage, empirically validated changes, method-family use, evaluation, and refresh separate. | OEE is one winner-selection method or source-free self-improvement story. | `OpenEndedVariantGenerationRecord@Project` records generation and archive or front linkage, while evaluation and refresh move to their subject patterns. |
| Novikov et al., `AlphaEvolve`, arXiv:2506.13131v1 (2025-06-16). | Separate generated method text, method description, evaluator relation, selected set, source-use relation, performed work, and work result. | Generated algorithm text is proof, gate permission, accepted method selection, or performed work. | Use `evaluatorOrComparatorRef`, lineage, source refs, and `nextGoverningRelation` to determine whether to use C.18, A.19, `G.5`, `C.11`, A.15, or `G.11`. |
| Cultural-evolution and style-engineering source pressure from the music and dance intake. | Keep generated style or tradition variants as archive or front records until a cultural-evolution case or term bridge is current. | A cultural-style variant is a root cultural kind or a selected set by label. | `culturalVariantRefs` continue to `C.36`, `F.17`, `F.18`, or `F.9`; selected-set result declaration continues to `G.5`, with a stable public identity added only through its conditional UTS branch. |
| Architecture-search and product-family work. | Treat retained structures as candidates for an architecture move only after the architecture claim is named. | An archive of layouts is the architecture or the architecture decision. | Architecture candidates require `C.30`, `C.30.ASV`, `C.30.AD`, or `C.32.P2S` after C.18 records descriptor, archive or front relation, and telemetry. |
| Taylor, [*Evolutionary Innovations and Where to Find Them*](https://arxiv.org/abs/1806.01883), 2019, read with Di Bona et al., [higher-order novelties](https://www.nature.com/articles/s41467-024-55115-y), 2025, and Kalambokidis et al., [diversity and open-ended evolution](https://www.nature.com/articles/s44260-026-00072-4), 2026. | Distinguish exploratory, expansive, and transformational claims; keep generator, evaluator, building blocks, retention/reproduction, environment, and opportunity structure explicit. | A taxonomy or high novelty/diversity result proves that a transferred non-evolutionary case changed its possibility space. | `C.18:4.3a` requires an exact earlier/candidate mapping and evidence limit; causal production uses `C.28`. |

### C.18:11 - Relations

Builds on: `C.16`, `A.19.CPM`, `A.19.SelectorMechanism`, and `E.18`.

Coordinates with: `C.19` for current-pool treatment, `C.11.CRC` for a finite configuration-relative comparison, `C.11` for local choice, `C.28` for causal support of a space-change claim, `G.5` for selected-set result declaration, `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence and audience availability, `G.9` for parity and benchmark comparison, `G.11` for refresh, `E.23` when an archived object version enters a declared quality-improvement loop, `E.18.1` for P2W carry-through, `C.30` family for architecture candidates, `C.32.P2S` for problem-to-structure carry-through, `C.32` for candidate palette admission, `C.35` for generated or discovered result adequacy before archive or front use of architecture candidates, `C.36` for cultural-evolution cases, `F.17`, `F.18`, and `F.9` for term and bridge work, and the A.15 family for planning or performed work.



### C.18:End

