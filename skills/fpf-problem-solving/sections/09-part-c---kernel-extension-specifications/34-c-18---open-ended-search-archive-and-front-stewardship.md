## C.18 - Open-Ended Search Archive and Front Stewardship

> **Tech-name:** `OpenEndedSearchArchiveAndFrontStewardship`
> **Plain-name:** open-ended search archive and front stewardship
> **Type:** C-pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Purpose:** retain candidates for stated exploration purposes and report the non-dominated set under a declared comparison, while preserving the basis needed to interpret either return.

### C.18:0 - Use This When

Use this pattern when generating or retaining variants raises a practical question: which candidates belong on the current front, which should remain available for exploration, and what changed in the basis for those decisions? A retained stepping stone can matter even when another candidate currently dominates it.

**First useful move.** Name the candidate set, the comparison or retention rule actually needed, and the supported return. If the question asks only which candidates are non-dominated, return that front under the declared comparator. If it asks what to keep for later exploration, state the archive membership and its retention reason. Keep the two answers distinct when both are needed.

An ordinary set description and explanation can finish the work. Use a reusable record when another use needs its references, editions or history. Generation alone can return a variant set without creating an archive or front; use C.40 when constructing or changing the material itself is the missing work.

#### C.18:0.1 - What Goes Wrong If Missed

The project treats an archive as a shortlist, a front as a decision, illumination telemetry as dominance, a retained stepping stone as current best, or a cultural-style variant as a root cultural kind. Generation looks productive, but the next relation is unclear—for example, whether to retain, compare, declare a selected-set result, choose locally, plan work, measure effects, refresh, or write a cultural-evolution case.

#### C.18:0.2 - What This Buys

The practitioner can retain a promising but currently dominated variant, report a front without treating it as a choice, and determine which comparison or retention claims must change after an edition or policy changes. Records can preserve those grounds for reuse; they are not the practical result by themselves.

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

Keep the claims about archive membership, front membership, telemetry, generation and later use distinct. Use the following record forms when their persistent account is needed; an adequate existing description need not be recopied.

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
  nextGoverningRelation: applicable pattern locator | none when the current question is complete
```

Use this record when an archive account must remain available for reuse—for example, retained exploration value, coverage, novelty, diversity, stepping-stone value, future reachability, curriculum expansion, lineage, or archive policy. Do not use the archive record as a selected-set result declaration or work permission.

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
  nextGoverningRelation: applicable pattern locator | none when the current question is complete
```

Use this record when a front account must remain available for reuse—for example, non-domination, Pareto relation, Q-front membership, comparator currentness, admissibility, or partial-order preservation. The front may feed a later G.5 use, but it is not itself a declared selected-set result; declare that result from the front through `G.5` under its own basis.

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

When loop-engineering practice generates many candidates—for example, prompts or harness variants—use C.18 for the generation and any archive/front claims the receiving work needs. Keep the descriptor, retention and lineage basis for those claims; add the record below when their reuse requires it. This does not say that the loop improved. Use `E.23` only when one retained object version is changed and re-evaluated through repeated passes under a declared object-under-improvement evaluation; use `G.9` for parity between variants and `G.5` when a selected-set result must be declared.

When the missing work is to change usable material and examine the resulting variation, `C.40` supplies that development and warranted continuation, with or without an already selected contribution. `C.40.CD` constructs problems and obtaining ways together through target application when those operations are needed. The record below describes generation; filling it does not perform these operations.

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
  nextGoverningRelation: applicable pattern locator | none when the current question is complete
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

Every optional field whose name ends in `Ref?` points to a separately identified object, claim, policy profile, or measurement basis. `dedupThreshold?` is not a reference: it carries one declared scalar threshold value. `deduplicationUnit?` carries its unit literal. Fill `emitterPolicyRef?` and `insertionPolicyRef?` only when the cited C.19 profile or insertion policy applies to the current pool treatment. When a threshold is inherited, the cited profile supplies `dedupThreshold`, `deduplicationBasisRef`, and `deduplicationUnit`; when it is not inherited, carry the scalar in `dedupThreshold?` and its basis and unit in `deduplicationBasisRef?` and `deduplicationUnit?`. These references and scalars do not give C.19 a generation operation or change the archive and front relations stated through C.18. In particular, `problemCardRef?` may cite a C.22.2 problem-side episteme but creates neither an actual Problem nor a `ProblematicForRelation` under `C.22.PFR`. Naming a generated variant, archive entry, front membership, telemetry value, or retained-exploration claim alone establishes neither an improvement-result nor a work-result identity and creates no relation from generation Work to a result. `nextGoverningRelation` locates the next applicable pattern when another question remains; use `none` when the current result is sufficient. The locator does not itself make a choice, declare a selected-set result, authorize work, perform refresh or make any relation obtain.

Use this record when a generation account needs the retained references and history. For architecture moves involving candidates named in `architectureCandidateRefs`, use `C.30`, `C.30.ASV`, or `C.30.AD` as applicable. Use `C.36` for cultural-evolution cases involving variants named in `culturalVariantRefs`. Local choice uses `C.11`; work planning and performed work use the A.15 family; effect measurement uses its direct measurement and evaluation patterns; refresh uses `G.11`. P2W carry-through uses `E.18.1` when an accepted problem-side distinction must be preserved into the next relation.

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

**Worked micro-case.** A cooling-module search previously admits only fixed rectangular layouts assembled by the same connection operators and evaluated under the same thermal/maintainability comparator. A new layout far from the archive remains exploratory if those rules still admit it. For this comparison, take a validated curved-channel building block and its construction operator as supplied inputs. Adding them is expansive only when the earlier generator could not express the resulting layouts and the comparison still uses a compatible higher-order regime. If the operator itself is missing, C.39.RO and the applicable subject Methods must supply its construction before that addition can be claimed. Replacing candidate admission and retention with a context-adaptive rule that changes which successors count is transformational only when the earlier/candidate rule mapping and observed reachability support that stronger claim. A higher novelty score alone establishes none of these transitions.


#### C.18:4.4 - Front And Archive Are Different Returns


- Start from one declared candidate or eligibility set.
- Return the non-dominated front from the relation-token set under the declared comparator or dominance set.
- Return the exploration archive separately when retained exploration value, coverage, novelty, diversity, stepping-stone value, or future reachability is current.
- Keep tie-breakers and telemetry explicit so diversity, illumination, or popularity signals do not rewrite front semantics.
- Before promoting telemetry or a popularity-like signal into the comparator, dominance set, or selected-set criteria, check which intended archive/front uses or values become worse or more fragile when that signal improves. State the affected uses or values, or the checked loci when none worsened, and cite the policy or decision authority that admits the promotion and any trade-off. If this basis or authority is missing, keep the signal as telemetry. Use it as a bounded tie-breaker only when a separate applicable policy already admits that use.
- Use `RetentionIntent=steppingStone` when retention exists for frontier expansion or later curriculum value rather than current dominance.
- If one source line keeps both returns, say that the front answers current non-domination while the archive answers retained exploration value.

#### C.18:4.5 - Cultural And Architecture Variant Boundaries

For architecture-candidate generation, C.18 records generation, archive, front, descriptor, telemetry, and retained exploration value. C.30 governs the architecture claim: `ArchitectureOf@Context`, selected structure or structure kind, affected characteristic, and next architecture move.

For cultural variants, C.18 records the generated or retained variant set and its descriptors, lineage, telemetry, and archive or front relation. Use C.36 for a cultural-evolution case when collective-holon or discipline-facing Method, Work, system-role kind or assignment, canon, memory, recognition, selection, mediation, style, tradition, or intervention relations are current. Use F.17 to identify local senses when needed, F.18 when a durable new name is required, and F.9 when a use depends on semantic correspondence between different local senses. Source-local labels such as style, tradition or genre can retain their cited meanings.

### C.18:5 - Conformance Checklist

- `CC-C18-1` Before generation, archive update, or front publication, name and pin the descriptor, characteristic, distance, and family-coordinate bases actually used by that operation.
- `CC-C18-2` Archive and front returns are separate from a selected-set result unless one is explicitly declared from them through `G.5`.
- `CC-C18-3` Telemetry remains telemetry unless a declared policy promotes it into the comparator, dominance set, or selected-set criteria and the governing record names the affected intended archive/front uses or values, or the checked loci when none worsened, together with the authority that admits the promotion and any trade-off.
- `CC-C18-4` For archive use, record the applicable retention policy, retained exploration value, lineage, and edition pins. When a stepping-stone use is claimed, record that use and its basis.
- `CC-C18-5` Use C.30 family patterns before making an architecture move with a candidate.
- `CC-C18-6` Use C.36 for cultural-evolution claims about variants, and term-bridge patterns when durable label or bridge work is current.
- `CC-C18-7` Refresh uses `G.11` with the smallest affected archive, front, descriptor, edition, or lineage locus.
- `CC-C18-8` Agent-loop, harness-loop, workflow-store, or DPF-seed variants retained in an archive name their descriptor, lineage, and next governing relation, together with any telemetry on which the retained-exploration claim relies; archive membership alone establishes no quality improvement. Quality-improvement claims require their own re-evaluation; use `E.23` only for repeated improvement passes.
- `CC-C18-9` A filled `projectLocality?` names independently admitted dated generation and composite project `U.Work` occurrences, the subject pattern, and one exact obtaining relation; `@Project` alone remains retrieval-only.
- `CC-C18-10` Problem-card, result, selected-set, choice, work, and refresh references remain references to separately governed objects or next subject patterns and create none of those identities or relations.
- `CC-C18-11` When a claim relies on a source premise, keep its edition and use basis recoverable. A material revision or contrary evidence reopens the dependent archive, front or generation claim through G.11; unaffected claims remain reusable.
- `CC-C18-12` When the §4.3a branch applies, exploratory, expansive, or transformational wording names the earlier and candidate effective space declarations, changed component, counterfactual or trajectory evidence, uncertainty, blocked stronger claim, and next relation; distance, rarity, novelty, or local progress alone does not prove space change.





### C.18:6 - Archetypal Grounding

**System-facing case.** A robotics team generates gait variants. The front records non-dominated speed and energy relations under declared measures. The archive retains diverse coordination patterns because some are stepping stones for new terrain. Telemetry reports coverage. A selected-set result may later be declared through `G.5`. If it must be available to an audience, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability. Performed test runs use A.15.

**Architecture case.** A cooling-module project keeps an archive of modular layout variants and a front over maintainability and energy use. C.18 records descriptors, archive policy, front relation, and telemetry. Use C.30 to name the selected structure and affected architecture characteristic, then decide whether to make an architecture move with a retained variant.

**Cultural case.** A dance-lab project generates movement variants around several source labels. C.18 records generated variants, descriptors, archive membership, front relation, and lineage. Use C.36 to determine whether the lab is deliberately changing the cultural practice; use F.17/F.9 when an actual label correspondence is needed and F.18 when the work needs a durable new name.

**Completed front/archive comparison.** Suppose three eligible cooling-module candidates have comparable readings for energy per operating cycle and time for the same service operation. Both quantities are minimized under the declared comparator.

| Candidate | Energy per cycle | Service-operation time |
| --- | --- | --- |
| A | 8 kWh | 20 min |
| B | 10 kWh | 25 min |
| C | 12 kWh | 15 min |

A dominates B because both readings are lower. A and C are incomparable: A uses less energy, while C takes less service time. The front is therefore `{A, C}`. The project's archive policy also retains one representative of every admitted connector family for later recombination. B is the only available representative of family J, so the archive retains B even though B is absent from the front. That retention is a coverage decision under the stated policy, not evidence that B performs better or will produce a successful later design.

“Front `{A, C}`; retain B in the archive as the family-J representative” answers this question. No selected-set declaration or design choice follows automatically. If another J-family variant arrives, reconsider retention under the same policy; if the comparator or measurement basis changes, recompute the affected front relations.

### C.18:7 - Bias-Annotation

Lexical and semiotic bias are controlled by keeping archive, front, telemetry, selected-set result declaration, audience publication, local choice, cultural-evolution case, architecture move, work permission, and evidence relations distinct. Mathematical descriptions of descriptor maps, fronts, distances, coverage, or novelty use the mathematical-lens pattern when lens adequacy matters.

### C.18:8 - Consequences

Positive consequences:

- archives keep exploration value while local choice remains separately governed;
- fronts preserve partial-order and comparator semantics;
- architecture and cultural-variant generation become usable without creating parallel root kinds;
- refresh and source-currentness have clear loci.

Costs:

- keep archive and front accounts distinct when both returns are used; generation alone need not create either return;
- a later selection, choice, plan or measurement needs its own grounds and may need a reusable record;
- descriptor editions and distance definitions require maintenance.

### C.18:9 - Rationale

Current quality-diversity, illumination search, open-ended engineering, and evolutionary-engineering practice shows that retained diversity, stepping stones, archive lineage, and descriptor currentness often matter before a single choice is justified. FPF keeps that practical gain while preventing archive and front language from replacing comparison, selected-set result declaration, audience publication, architecture, cultural evolution, work, evidence, decision, or refresh patterns.

### C.18:10 - SoTA-Echoing

The cited editions contribute different parts of archive and front practice. Retention value, current dominance and a claim of open-ended change keep separate grounds.

| Source and scope | Contribution | Use boundary |
| --- | --- | --- |
| Lin et al., *Quality-Diversity Optimization as Multi-Objective Optimization*, arXiv:2602.00478v1 (2026-01-31) | Treats QD/Q-front comparison through declared objective components and dominance. | Cell filling or popularity does not supply the comparator. Keep the front, archive, selected-set declaration and publication uses separate. |
| Qin et al., *A survey on Quality-Diversity optimization: Approaches, applications, and challenges*, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI `10.1016/j.swevo.2025.102240`, `https://www.sciencedirect.com/science/article/pii/S2210650225003979` | Surveys approaches, applications, archive/diversity use and open challenges. | Its taxonomy does not replace the actual retention, comparison or generation relations. G.5 governs a selected-set declaration; E.17/E.24.PUB govern its publication when needed. |
| Batra et al., *Quality Diversity for Robot Learning: Limitations and Future Directions*, arXiv:2407.17515v1 (2024-07-09) | Makes retained exploration value, generalization pressure and archive limitations relevant beyond current dominance. | Bounded archive occupancy alone does not establish usefulness or open-ended evolution. State the retention basis and cite telemetry only when the claim relies on it. |
| Zhang et al., *Darwin Godel Machine*, arXiv:2505.22954v3 (2026-03-12) | Connects generated agents, archive lineage and empirically evaluated changes. | An archive or generated change does not establish improvement. Repeated evaluation and source-currentness questions use their own conditions. |
| Novikov et al., *AlphaEvolve*, arXiv:2506.13131v1 (2025-06-16) | Connects generated algorithm candidates to evaluation and retained search results. | Generated text remains distinct from its Method, evaluation result, selected set and performed Work. The actual next question determines the needed subject rule. |
| Taylor, [*Evolutionary Innovations and Where to Find Them*](https://arxiv.org/abs/1806.01883), 2019; Di Bona et al., [higher-order novelties](https://www.nature.com/articles/s41467-024-55115-y), 2025; Kalambokidis et al., [diversity and open-ended evolution](https://www.nature.com/articles/s44260-026-00072-4), 2026 | Distinguishes exploration, expansion and transformation through the generator, evaluator, building blocks, retention/reproduction and environment. | A taxonomy or high novelty value does not establish space change in a transferred case. Section 4.3a requires the earlier/candidate relation and evidence limit; causal production uses C.28. |

### C.18:11 - Relations

Builds on: `C.16`, `A.19.CPM`, `A.19.SelectorMechanism`, and `E.18`.

Coordinates with: `C.19` for current-pool treatment, `C.11.CRC` for a finite configuration-relative comparison, `C.11` for local choice, `C.28` for causal support of a space-change claim, `G.5` for selected-set result declaration, `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence and audience availability, `G.9` for parity and benchmark comparison, `G.11` for refresh, `E.23` when an archived object version enters a declared quality-improvement loop, `E.18.1` for P2W carry-through, `C.30` family for architecture candidates, `C.32.P2S` for problem-to-structure carry-through, `C.32` for candidate palette admission, `C.35` for generated or discovered result adequacy before archive or front use of architecture candidates, `C.36` for cultural-evolution cases, `F.17`, `F.18`, and `F.9` for term and bridge work, and the A.15 family for planning or performed work.



### C.18:End
