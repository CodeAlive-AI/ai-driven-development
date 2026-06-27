## C.18 - Open-Ended Search Archive and Front Stewardship

> **Tech-name:** `OpenEndedSearchArchiveAndFrontStewardship`
> **Plain-name:** open-ended search archive and front stewardship
> **Type:** C-pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part C
> **Builds on:** `C.16`, `C.19`, `G.5`, `G.11`, `E.18`, `E.18.1`, `A.19.CPM`, `A.19.SelectorMechanism`, `C.30`, `F.17`, `F.18`, and `F.9`.
> **Purpose:** make archive, front, Q-front, descriptor, telemetry, retained exploration value, stepping-stone value, lineage, edition, architecture-candidate generation, and cultural-variant generation usable without turning them into publication, decision, work permission, or cultural-evolution authority.

### C.18:0 - Use This When

Use this pattern when a project needs to generate, retain, compare, or report many candidate variants while preserving descriptor editions, distance definitions, archive policies, front semantics, telemetry, lineage, and retained exploration value.

Typical cases include quality-diversity archives, open-ended engineering variant sets, Pareto or Q-front treatment, phenotype-like descriptor maps, architecture-candidate generation, style or tradition variant generation, scientific or engineering school variants, and candidate pools whose value is not captured by one immediate selected set.

#### C.18:0.1 - What Goes Wrong If Missed

The project treats an archive as a shortlist, a front as a decision, illumination telemetry as dominance, a retained stepping stone as current best, or a cultural-style variant as a root cultural kind. Generation looks productive, but the next relation is unclear: retain, compare, publish selected set, choose locally, plan work, measure effects, refresh, or write a cultural-evolution case.

#### C.18:0.2 - What This Buys

The practitioner gets separate records for archive, front, and generation. Each record pins descriptors, characteristic spaces, edition refs, retention policy, telemetry, lineage, and next governing relation. Downstream selection, architecture, cultural evolution, work planning, measurement, and refresh then start from named records rather than from a broad archive label.

### C.18:1 - Problem Frame

Open-ended search and quality-diversity work deliberately keep more than one candidate alive. That is useful for engineering, science, design, music, dance, AI-agent frameworks, medical method families, and other evolving practices. The same archive or front label can hide strong candidates, weak but promising stepping stones, coverage-expanding variants, architecture candidates, cultural variants, and telemetry-only signals.

The primary `EntityOfConcern` in C.18 is the archive or front relation being stewarded: which variants are generated or retained, under which descriptor and characteristic space, with which edition and lineage pins, and with which next relation available. C.18 is not a local-choice pattern, not a selected-set publication pattern, not a cultural-evolution subject-governing pattern, and not an architecture pattern.

### C.18:2 - Problem

Without C.18, a team often compresses several different objects into one word such as archive, front, Q-front, portfolio, style pool, or candidate set. That loses four distinctions:

- a front answers current non-domination under a declared comparator or dominance set;
- an archive answers retained exploration value, coverage, stepping-stone value, or future reachability under a declared retention policy;
- telemetry reports search health, coverage, novelty, diversity, or lineage but does not by itself dominate alternatives;
- downstream selected-set publication, local choice, architecture work, cultural-evolution case work, planning, performed work, and refresh each have their own governing pattern.

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

Keep archive, front, telemetry, generation, and downstream relations as separate records.

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
  nextGoverningRelation:
```

Use this record when the current question is retained exploration value, coverage, novelty, diversity, stepping-stone value, future reachability, curriculum expansion, lineage, or archive policy. Do not use the archive record as a selected-set publication or work permission.

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
  selectedSetPublicationRef?:
  nextGoverningRelation:
```

Use this record when the current question is non-domination, Pareto relation, Q-front membership, comparator currentness, admissibility, or partial-order preservation. The front may feed `G.5`, but it is not itself a selected-set publication unless `G.5` makes that publication.

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
  nextGoverningRelation: C.36 case card or G.11 refresh, depending on the current question
```

```text
FrontRecord@Context:
  frontRef: cooling-module-maintainability-energy-front
  candidateSetRef: retained cooling-module architecture candidates
  comparatorOrDominanceSetRef: energy-use and maintainability comparator
  admissibilityRef: safety and manufacturing constraints already admitted by project policy
  descriptorMapRef: thermal performance, service access, part count, manufacturing tolerance
  characteristicSpaceRef: product-family architecture characteristic space
  relationTokenSetRef: non-dominated candidates under current comparator
  excludedTelemetryRefs: tests outside the current temperature envelope
  selectedSetPublicationRef: empty until G.5 publishes the selected set
  nextGoverningRelation: C.30 architecture candidate treatment or G.5 selected-set publication
```

#### C.18:4.3 - Generation And Downstream-Use Record
When loop-engineering practice generates many agent prompts, harness variants, workflow variants, or framework seeds, `C.18` records generation, archive, front, descriptors, telemetry, retained exploration value, lineage, and next governing relation. It does not say that the loop improved. Use `E.23` only when a retained object version is changed and re-evaluated; use `G.9` for parity between variants and `G.5` when a selected set must be published.

```text
OpenEndedVariantGenerationRecord@Project:
  problemCardRef?:
  generationMethodOrFamilyRef:
  variantSetRef:
  descriptorMapRef:
  characteristicOrDescriptorSetRef:
  archiveOrFrontRef?:
  architectureCandidateRefs?:
  culturalVariantRefs?:
  telemetryRefs?:
  workPlanOrMeasurementRef?:
  refreshRef?:
  nextGoverningRelation:
```

Use this record when generation is current. `architectureCandidateRefs` become architecture moves only through `C.30`, `C.30.ASV`, or `C.30.AD`. `culturalVariantRefs` become cultural-evolution cases only through `C.36`. Work planning, performed work, effect measurement, and refresh use the A.15 family and `G.11`. P2W carry-through uses `E.18.1` when an accepted problem-side distinction must be preserved into the next relation.

#### C.18:4.4 - Front And Archive Are Different Returns

- Start from one declared candidate or eligibility set.
- Return the non-dominated front over the declared comparator, dominance set, or relation-token set.
- Return the exploration archive separately when retained exploration value, coverage, novelty, diversity, stepping-stone value, or future reachability is current.
- Keep tie-breakers and telemetry explicit so diversity, illumination, or popularity signals do not rewrite front semantics.
- Use `RetentionIntent=steppingStone` when retention exists for frontier expansion or later curriculum value rather than current dominance.
- If one source line keeps both returns, say that the front answers current non-domination while the archive answers retained exploration value.

#### C.18:4.5 - Cultural And Architecture Variant Boundaries

For architecture-candidate generation, C.18 records generation, archive, front, descriptor, telemetry, and retained exploration value. C.30 governs the architecture claim: `ArchitectureOf@Context`, selected structure or structure kind, affected characteristic, and next architecture move.

For cultural variants, C.18 records the generated or retained variant set and its descriptors, lineage, telemetry, and archive or front relation. C.36 governs the cultural-evolution case when collective-holon or discipline-facing method, work, role, canon, memory, recognition, selection, mediation, style, tradition, or intervention relations are current. F.17, F.18, and F.9 govern durable term and bridge work for labels such as style, tradition, genre, scene, school, and technique.

### C.18:5 - Conformance Checklist

- `CC-C18-1` Descriptor, characteristic, distance, and family-coordinate refs are named before generation, archive update, or front publication.
- `CC-C18-2` Archive and front returns are separate unless a governing pattern explicitly publishes a selected set from one of them.
- `CC-C18-3` Telemetry remains telemetry unless a declared policy promotes it into the comparator, dominance set, or selected-set criteria.
- `CC-C18-4` Retained exploration value, stepping-stone use, lineage, and edition pins are recorded for archive use.
- `CC-C18-5` Architecture candidates use C.30 family patterns before becoming architecture moves.
- `CC-C18-6` Cultural variants use C.36 or term-bridge patterns before becoming cultural-evolution claims.
- `CC-C18-7` Refresh uses `G.11` with the smallest affected archive, front, descriptor, edition, or lineage locus.
- `CC-C18-8` Agent-loop, harness-loop, workflow-store, or DPF-seed variants retained in an archive name their descriptor, lineage, telemetry, and next governing relation; archive membership does not claim quality improvement without `E.23` re-evaluation.



### C.18:6 - Archetypal Grounding

**System-facing case.** A robotics team generates gait variants. The front records non-dominated speed and energy relations under declared measures. The archive retains diverse coordination patterns because some are stepping stones for new terrain. Telemetry reports coverage. A selected set may later be published through `G.5`; performed test runs use A.15.

**Architecture case.** A cooling-module project keeps an archive of modular layout variants and a front over maintainability and energy use. C.18 records descriptors, archive policy, front relation, and telemetry. C.30 decides whether any retained variant becomes an architecture move by naming the selected structure and affected architecture characteristic.

**Cultural case.** A dance-lab project generates movement variants around several source labels. C.18 records generated variants, descriptors, archive membership, front relation, and lineage. C.36 decides whether the lab is deliberately changing a cultural-evolution case; F.17, F.18, and F.9 handle the label bridges.

### C.18:7 - Bias-Annotation

Lexical and semiotic bias are controlled by keeping archive, front, telemetry, selected-set publication, local choice, cultural-evolution case, architecture move, work permission, and evidence relations distinct. Mathematical descriptions of descriptor maps, fronts, distances, coverage, or novelty use the mathematical-lens pattern when lens adequacy matters.

### C.18:8 - Consequences

Positive consequences:

- archives keep exploration value without pretending to decide;
- fronts preserve partial-order and comparator semantics;
- architecture and cultural-variant generation become usable without creating parallel root kinds;
- refresh and source-currentness have clear loci.

Costs:

- teams must keep at least archive and front records separate;
- one generated variant may need several downstream records before it becomes selected, chosen, planned, worked, measured, or refreshed;
- descriptor editions and distance definitions require maintenance.

### C.18:9 - Rationale

Current quality-diversity, illumination search, open-ended engineering, and evolutionary-engineering practice shows that retained diversity, stepping stones, archive lineage, and descriptor currentness often matter before a single choice is justified. FPF keeps that practical gain while preventing archive and front language from replacing comparison, selected-set publication, architecture, cultural evolution, work, evidence, decision, or refresh patterns.

### C.18:10 - SoTA-Echoing

| Source or source family | Adopted FPF move | Rejected overread | Field or boundary changed |
|---|---|---|---|
| Lin et al., `Quality-Diversity Optimization as Multi-Objective Optimization`, arXiv:2602.00478. | Treat QD and Q-front work through declared Q components, `DominanceSet`, comparator refs, archive relation, front relation, selected-set publication, and refresh. | Cell-filling or popularity accounts are the current ontology by default. | `FrontRecord@Context` must keep dominance grounds, comparator refs, and Q-component refs explicit. |
| Qin et al., `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI `10.1016/j.swevo.2025.102240`, `https://www.sciencedirect.com/science/article/pii/S2210650225003979`. | Use current survey support for approaches, applications, archive use, diversity use, and challenge framing. | Survey taxonomy replaces FPF governing loci. | `ExplorationArchiveRecord@Context`, `FrontRecord@Context`, and `OpenEndedVariantGenerationRecord@Project` stay governed by C.18 while selected-set publication and refresh stay with `G.5` and `G.11`. |
| Batra et al., `Quality Diversity for Robot Learning: Limitations and Future Directions`, arXiv:2407.17515. | State retained exploration value, generalization pressure, and limitations when an archive is used beyond current dominance. | Bounded archives or cell occupancy are enough evidence that NQD and OEE are useful. | `retainedValue`, `retentionPolicyRef`, `telemetryRefs`, and `nextGoverningRelation` must be filled when the archive is relied on. |
| Zhang et al., `Darwin Godel Machine`, arXiv:2505.22954. | Keep generated agents, archive lineage, empirically validated changes, method-family use, evaluation, and refresh separate. | OEE is one winner-selection method or source-free self-improvement story. | `OpenEndedVariantGenerationRecord@Project` records generation and archive or front linkage, while evaluation and refresh move to their governing patterns. |
| Novikov et al., `AlphaEvolve`, arXiv:2506.13131. | Separate generated method text, method description, evaluator relation, selected set, source-use relation, performed work, and work result. | Generated algorithm text is proof, gate permission, accepted method selection, or performed work. | `evaluatorOrComparatorRef`, lineage, source refs, and `nextGoverningRelation` decide whether to use C.18, A.19, `G.5`, `C.11`, A.15, or `G.11`. |
| Cultural-evolution and style-engineering source pressure from the music and dance intake. | Keep generated style or tradition variants as archive or front records until a cultural-evolution case or term bridge is current. | A cultural-style variant is a root cultural kind or a selected set by label. | `culturalVariantRefs` continue to `C.36`, `F.17`, `F.18`, or `F.9`; selected-set labels continue to `G.5`. |
| Architecture-search and product-family work. | Treat retained structures as candidate architecture moves only after the architecture claim is named. | An archive of layouts is the architecture or the architecture decision. | Architecture candidates exit to `C.30`, `C.30.ASV`, `C.30.AD`, or `C.32.P2S` after C.18 records descriptor, archive or front relation, and telemetry. |

### C.18:11 - Relations

Builds on: `C.16`, `A.19.CPM`, `A.19.SelectorMechanism`, and `E.18`.

Coordinates with: `C.19` for current-pool treatment, `G.5` for selected-set publication, `G.9` for parity and benchmark comparison, `G.11` for refresh, `E.23` when an archived object version enters a declared quality-improvement loop, `E.18.1` for P2W carry-through, `C.30` family, `C.32.P2S`, `C.32`, and `C.35` for architecture candidates, problem-to-structure carry-through, candidate palette admission, and generated or discovered carrier adequacy before archive or front use, `C.36` for cultural-evolution cases, `F.17`, `F.18`, and `F.9` for term and bridge work, and the A.15 family for planning or performed work.



### C.18:End

