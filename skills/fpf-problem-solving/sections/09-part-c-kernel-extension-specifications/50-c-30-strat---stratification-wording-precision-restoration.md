## C.30.STRAT - Stratification Wording Precision Restoration

> **Type:** Architectural precision-restoration subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Stratification and architecture-operation source-label repair.

**Intent.** Recover source wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, and `gate` by completing the `E.10.ARCH` recovery row for that wording use: `semanticAreaBaseConcept`, `semanticAreaSenseFamily`, selected `ontologicalNeighborhood`, primary `EntityOfConcern` kind, encountered FPF kind or reference, relation to the primary `EntityOfConcern`, recovered kind, relation, or claim-use, source-use disposition, governing pattern, admissible use, non-admissible use, and remaining reader use. No conforming `C.30.STRAT` use mints `U.Layer`, `U.Level`, `U.Tier`, `U.Stack`, `U.Ladder`, `U.Rung`, `U.Block`, `U.Expert`, `U.Cache`, or one universal `U.Stratification`.

**Builds on.** `E.10`, `E.10.ARCH`, `E.8`, `F.18`, `C.30.P`, `A.22`, and `C.30`.

**Coordinates with.** `C.30.ASV`, `C.30.LCA`, `C.30.TFS-REL`, `C.30.ILC`, `A.6.M`, `A.6.F`, `E.18`, `C.16.P`, `C.16`, `A.19.SPR`, `C.2.P`, `E.17`, `C.29`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `A.2`, `G.5`, and `C.11`.

**E.10.ARCH governing relation.** When `E.10` encounters a stratification or architecture-operation source label whose `ontologicalNeighborhood`, primary `EntityOfConcern` kind, recovered kind, relation, claim-use, source-use disposition, or governing pattern is hidden, `E.10.ARCH` selects `C.30.STRAT` only until those row fields are recovered or the wording is lowered to ordinary source label, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite. `C.30.STRAT` then stops at the source-label repair row; the governing pattern carries any recovered non-source-label claim or relation.

### C.30.STRAT:0 - Use this when

Use this pattern when stratification or architecture-operation wording is doing FPF-governed work but the selected `ontologicalNeighborhood` and governing pattern for the source-label use are not yet recoverable by value.

Typical source labels:

- `layer`, `level`, `tier`, `stack`, `ladder`, `rung`;
- `block`, `expert`, `cache`, `router`, `gate` when architecture-operation prose uses them as recognition labels before the FPF kind is known.

**What goes wrong if missed.** A source label starts acting as ontology. `Layer` may be taken as a holon level, control layer, publication layer, scale window, or module boundary without saying which ontological neighborhood is being used. `Stack` may become architecture by label. `Block` may become a module. `Expert` may become a role. `Cache` may become a memory relation or state. `Router` may become a decision policy. `Gate` may become a gate decision. None of those interpretations is admissible by word shape alone.

**What this buys.** The practitioner can keep useful source language while recovering the selected `ontologicalNeighborhood` and applying the governing pattern, instead of replacing the source label with another umbrella word.

**First useful move.** Treat the word as a `sourceLabel` and complete the recovery row: source label, bounded text, selected `ontologicalNeighborhood`, primary `EntityOfConcern` kind, relation to that `EntityOfConcern`, recovered kind, relation, or claim-use, governing pattern, admissible use, non-admissible use, and remaining reader use.

**Not this pattern when.** If the governing pattern is already recoverable by value, use it directly. Do not use `C.30.STRAT` merely because a familiar word appears. If the wording is only ordinary source prose with no FPF-governed use, keep ordinary prose or quote-only wording and stop.

### C.30.STRAT:1 - Problem frame

Architecture and engineering sources use compact labels because they work in local practice. Neural-network architecture prose says `block`, `expert`, `cache`, or `router`. Control architecture says `layer`. Organizations say `level` or `tier`. Documentation says `section`, `stack`, or `view`. Mathematical and scale prose says `level`, `resolution`, or `coarse-graining step`.

Those labels are useful recognition cues, but FPF cannot rely on them as kinds. A label is not enough to know whether the next admissible use is module-relation repair, structure selection, functional-structure record, control-structure view, scale-window naming, source-publication return, or non-source-label claim assignment named by value.

The repair question is:

> Which `ontologicalNeighborhood` does this source-label use belong to, and which governing pattern now governs the recovered kind, recovered relation, recovered claim-use, source-use disposition, or non-use disposition?

### C.30.STRAT:2 - Problem

How can FPF keep common stratification and architecture-operation language without:

- minting false root kinds for `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate`;
- making `C.30` govern all structure-like wording;
- making `A.6.M` or `C.30.LCA` carry a duplicate local trigger registry;
- treating source labels as non-source-label FPF-governed claims by appearance;
- removing useful source language before a remaining admissible reader use is recoverable?

### C.30.STRAT:3 - Forces

| Force | Tension |
| --- | --- |
| Source-language usability vs ontology | Practitioners need compact local words; FPF needs selected `ontologicalNeighborhood`, relation named by value or claim-use, source-use disposition, and use boundary. |
| Pattern placement vs ontological neighborhood | The placement is in the `C.30` pattern nest because the recurring first confusion is architecture or structure wording, but recovered claims and relations are governed by the pattern named in `C.30.STRAT:4.2`. |
| Thin repair vs shadow registry | Subject patterns need one pointer, not copied trigger lists. |
| Direct governing pattern vs detour | If the relation, function-like use, control use, scale use, publication use, evidence use, or decision use is already recovered by value, apply the governing pattern directly. |
| Didactic payoff vs sterile precision | The repair is complete only when it leaves one useful move: governing-pattern application, local rewrite, source return, ordinary source label, or blocked use. |

### C.30.STRAT:4 - Solution

Produce a `StratificationSourceLabelRepairNote` or an equivalent local rewrite. The note records the recovered `E.10.ARCH` row fields for this source-label use. It is not itself the selected structure, relation, source publication, neighboring claim record, or governing-pattern result.

```text
StratificationSourceLabelRepairNote:
  sourceLabel:
  boundedTextSpanOrPublicationUnit:
  localSentenceRole:
  encounteredSourceContext:
  semanticAreaBaseConcept:
  semanticAreaSenseFamily:
  selectedOntologicalNeighborhood:
  primaryEntityOfConcernKind:
  encounteredFPFKindOrReference:
  relationToPrimaryEntityOfConcern:
  recoveredKindRelationOrClaimUse:
  sourceUseDisposition:
  governingPatternRef:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderUse:
  disposition:
    governing-pattern-ref | local-rewrite | ordinary-source-label |
    quote-only | reduced-use-cue | blocked-use | incomplete-rewrite
```

#### C.30.STRAT:4.1 - Recovery sequence

1. **Bound the text and label.** Name the sentence, table row, diagram label, publication unit, or source span; copy the source label; and state the local sentence function.
2. **Check cheap closure.** If there is no FPF-governed use, keep ordinary prose or quote-only wording and stop. If one small local rewrite restores the intended non-FPF use, close locally under `E.10`.
3. **Recover candidate ontology.** Recover candidate primary `EntityOfConcern` kinds, candidate encountered FPF kinds or references, relation candidates, claim-use candidates, source-use candidates, scope, time, viewpoint, and context facets. Include literal and intended candidates when metonymy or compression is plausible.
4. **Select the ontological neighborhood.** Select the first applicable neighborhood by recovered relation, claim-use, source-use disposition, formal apparatus, or governing-pattern field set, not by the source label.
5. **State the apparatus that makes the repair checkable.** Use relation slots, control roles and rate bands, module-interface fields, flow fields, transformation-flow fields, characteristic and scale construction, publication relation set, source-use disposition, mathematical-lens fields, evidence relation, assurance argument, gate record, work occurrence, decision record, causal-use record, or ordinary non-use disposition, with scope, time, viewpoint, and context facets only where the recovered claim or use needs them.
6. **Project back to wording.** Produce the repaired wording, compact note, direct governing-pattern application, or non-use disposition. The replacement candidate is accepted only after it passes `E.10`.
7. **State use and move.** State admissible use, non-admissible wider or adjacent use, and one remaining reader use. If no reader use remains, the disposition is reduced-use, quote-only, blocked use, or incomplete rewrite.

#### C.30.STRAT:4.2 - Ontological-neighborhood governing-pattern applications

| Ontological neighborhood selected by recovery | Common source labels | Required recovery apparatus | Governing pattern application |
| --- | --- | --- | --- |
| Control-structure neighborhood | `layer`, `level`, `tier`, sometimes `gate` | Control role, control relation, rate band, bounded context, and, when a supervisor-subholon relation is being made, B.2.5 supervisor-subholon relation. | `C.30.LCA` for control-structure view; `B.2.5`, dynamics, temporal, evidence, assurance, or gate patterns only when those claims are being made separately. |
| Selected-structure or structural-view neighborhood | `layer`, `level`, `stack`, `block`, `view` | Selected structure, hidden structure, lost structure, preserved structure, structural-view selection, correspondence or source-return boundary, and `ArchitectureOf@Context` relation when that relation is being made. | `A.22`, `C.30`, `C.30.ASV`, or named C.30 subpattern. |
| Module-interface and substitution neighborhood | `block`, `cache`, `router`, `expert`, sometimes `layer` or `stack` | Module boundary, interface specification, substitutability relation, variation point, conformance relation, or module-interface reliance boundary. | `A.6.M`; not `C.30.STRAT` once the module-interface relation is recovered. |
| Function-like or transformation-flow neighborhood | `block`, `expert`, `cache`, `router`, `gate`, sometimes `layer` | Transformation or effect claim, path-selection relation, graph node, graph path, graph crossing, architecture-to-transformation-flow relation, or flow valuation under E.18. | `A.6.F`, `E.18`, or `C.30.TFS-REL`. |
| Characteristic, scale, or mathematical-lens neighborhood | `level`, `tier`, `ladder`, `rung`, `layer`, `stack`, `block` | Characteristic, scale, coordinate, value plus declared scoring method, comparison criterion or declared comparability relation, scale window, resolution, coarse-graining, preserved structure, lost structure, C.29 mathematical-lens result, and stop condition when the lens-use claim is being made. | `C.16.P`, characterization pattern governing the claim, or `C.29`. |
| Episteme, publication, view, or source-use neighborhood | `stack`, `layer`, `section`, `view`, `cache`, `gate` | Description episteme, publication unit, publication face, publication form, carrier, source-currentness relation, source-use disposition, source-return condition, or publication label. | `C.2.P`, `E.17`, or the publication or source-use pattern governing the claim. |
| State, currentness, temporal, or dynamics neighborhood | `cache`, `stable`, `level`, `readiness`, sometimes `gate` | Bearer kind, state frame, value set, validity window, currentness relation, dynamics claim, temporal-aspect or rate-band claim, authored temporal-claim adequacy, or reopen condition. | `A.19.SPR`, `A.3.3`, `C.27.TA`, `C.27`, or a state pattern or temporal pattern named by value. |
| Evidence, assurance, gate, work, decision, or causal-use neighborhood | `gate`, `proof`, `safety`, `decision`, `work`, `effect`, sometimes any source label used as authority | Evidence path, assurance argument, constraint-validity record, gate decision, work occurrence, decision record, causal-use record, and non-admissible overread. | `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, or neighboring pattern governing that claim. |
| Ordinary source-label non-use | any source label | No FPF-governed claim after context check; optional quote-only or reduced-use cue. | No precision-restoration pattern application is needed; stop with ordinary wording, quote-only wording, or blocked use. |

#### C.30.STRAT:4.2a - Same-sentence claim boundary

When one sentence uses a source label to carry another FPF-governed claim, do not repeat a local "not proof, not gate, not work" catalogue at every occurrence. Keep the source-label repair in `C.30.STRAT` and apply the governing pattern for each recovered non-source-label claim. `C.30.STRAT:4.2` names the common choices; worked cases keep only local false positives that the source label itself makes tempting.

#### C.30.STRAT:4.3 - Source-label cue table

| Source label family | Recovery discipline |
| --- | --- |
| `layer` | Do not choose by the word. Test control-structure, selected-structure or structural-view, module-interface, scale or mathematical-lens, and publication or source-use neighborhoods. |
| `level` | Test holon-level or aggregation use only when declared by a governing pattern; otherwise test characteristic or scale, ordinal classification, organization scope, work scope, evidence scope, publication grouping, or ordinary source-label non-use. |
| `tier` | Test deployment, service, organization, classification, aggregation, and publication neighborhoods. Deployment or service claims named by value are governed by their governing patterns rather than by `tier` as ontology. |
| `stack` | Test signature or slot construction, relation set or relation chain, architecture or control arrangement, aggregation arrangement, virtualization arrangement, deployment arrangement, publication-section ordering, or ordinary source-label non-use. A stack is not architecture by itself. |
| `ladder` and `rung` | Test ordinal or classification scale, declared maturity or readiness progression, C.28 causal-use ladder or rung, publication taxonomy, or ordinary source-label non-use. Do not use ladder wording for an undeclared progression scale. |
| `block` | Test module-interface or substitution, selected-structure or structural-view, function-like or transformation-flow, mathematical-lens or coarse-graining, evidence, causal-use, gate, and decision neighborhoods. |
| `expert` | In MoE-like prose, test submodel, subholon, specialized transformation, path-selection relation, candidate-selection relation, or actual role or enactment only when an `A.2` or `A.15` role or work claim is being made. |
| `cache` | Test module-interface, flow buffer or path, state or currentness, capacity characteristic, latency characteristic, memory characteristic, reuse characteristic, source-currentness, publication cache, temporal-aspect or rate-band claim, authored temporal-claim adequacy, or ordinary source-label non-use. |
| `router` | Test path selection, flow relation, transformation function or selection function, module-interface relation, candidate selection, decision, or actual role or work only when that claim is being made. |
| `gate` | Test constraint-validity record or gate-decision record, gating function, path selection, flow relation, publication label, or ordinary source-label non-use. A source label `gate` is not gate passage. |

#### C.30.STRAT:4.4 - Placement discipline

`semanticAreaBaseConcept`: stratification wording and architecture-operation source labels.

`semanticArea`: the Part-F semantic row-set used for `layer`, `level`, `tier`, `stack`, `ladder`, and `rung` plus architecture-operation labels such as `block`, `expert`, `cache`, `router`, and `gate` when they are used as source labels before the governing FPF pattern recovers their selected kind, relation, or publication-use boundary.


`semanticAreaSenseFamily`: source-label wording for stratification, ordering, aggregation, and architecture-operation recognition; not a topic label, pattern-placement claim, or pattern-nest grouping.

`ontologicalNeighborhood`: the applicability neighborhood selected by the recovery row, not a second ontology. The admissible neighborhoods are the rows in `C.30.STRAT:4.2`: control structure; selected structure or structural view; module-interface and substitution; function-like or transformation-flow; characteristic, scale, or mathematical-lens use; episteme, publication, view, or source-use; state, currentness, temporal, or dynamics; evidence, assurance, gate, work, decision, or causal-use; and ordinary source-label non-use.

The pattern nest is `C.30.*` because the recurring first failure is architecture or structure wording in architecture-operation prose. That placement does not make `C.30` the governing pattern for non-source-label claims named in `C.30.STRAT:4.2`. The selected `ontologicalNeighborhood` and governing-pattern row decide which pattern governs the case.

#### C.30.STRAT:4.5 - Worked cases

| Wording | Repair |
| --- | --- |
| `The module layer is stable.` | Copy `layer` as source label. Test whether the selected neighborhood is module-interface, scale or comparison, publication or view, or state or temporal. Use `A.6.M`, `C.16.P` or `C.29`, `C.2.P`, `A.19.SPR`, `A.3.3`, `C.27.TA`, or `C.27` only after the neighborhood and apparatus are recovered. |
| `The expert routes the token.` | In MoE prose, `expert` is not a human role by default. Test submodel or subholon, specialized transformation, path-selection relation, architecture-to-transformation-flow relation, candidate selection, or actual role or enactment. Use `A.6.F`, `E.18`, `C.30.TFS-REL`, `G.5`, `C.11`, `A.2`, or `A.15` only for the recovered neighborhood. |
| `The cache proves the architecture scales.` | `cache` may belong to module-interface, flow buffer or path, state or currentness, characteristic, source-currentness, or temporal neighborhoods. `Proves` and `scales` are separate evidence, assurance, and scale or mathematical-lens claims. Use governing patterns for each recovered claim-use; do not let `cache` carry proof. |
| `The LCA upper layer guarantees safety.` | Use `C.30.STRAT` only to recover whether `layer` belongs to the control-structure neighborhood. Then `C.30.LCA` records control roles, relations, rate band, and bounded context. Safety proof or assurance is governed by `B.3`, `A.10` or `G.6`, dynamics, temporal, and gate patterns. |
| `This gate selects the winning architecture.` | If `gate` is a neural-network gating function or router, use `A.6.F` or `E.18`; if it is a project gate decision, use `A.20` or `A.21`; if it is candidate selection, use `G.5` or `C.11`. The label alone decides none of these. |

#### C.30.STRAT:4.5a - Filled repair note

```text
StratificationSourceLabelRepairNote:
  sourceLabel: cache
  boundedTextSpanOrPublicationUnit: "The cache proves the architecture scales."
  localSentenceRole: architecture-operation source label plus separate proof and scale claims
  encounteredSourceContext: inference-service architecture prose where cache names a reusable state or buffer mechanism
  semanticAreaBaseConcept: stratification wording and architecture-operation source labels
  semanticAreaSenseFamily: cache/state/buffer/reuse source-label wording
  selectedOntologicalNeighborhood:
    cache label: state or currentness, module-interface, or flow-buffer neighborhood only after apparatus is recovered
    proves wording: evidence or assurance neighborhood only if an evidence relation or assurance argument is present
    scales wording: characteristic, scale, architecture scale-preference, or mathematical-lens neighborhood only if those fields are present
  primaryEntityOfConcernKind: ArchitectureOf@ServiceContext with a cache-related selected structure or state-bearing module candidate
  encounteredFPFKindOrReference: source label only; no `U.Cache`, no proof record, and no scale claim by word shape
  relationToPrimaryEntityOfConcern: cache is a candidate architecture-relevant structure or state-bearing item; proof and scale are adjacent claim uses
  recoveredKindRelationOrClaimUse: split into cache-structure/state candidate, evidence or assurance overread, and scale or lens-use candidate
  sourceUseDisposition: keep `cache` as source label until the field set named by value is recoverable; lower `proves` if no evidence relation is present
  governingPatternRef: `A.6.M`, `A.6.F`, `E.18`, `A.19.SPR`, or `A.3.3` for cache apparatus when recovered; `C.16.P`, `C.29`, or `C.31.ASAP` for scale or lens use when recovered; `A.10`, `B.3`, or `G.6` for evidence or assurance only when that claim is being made
  admissibleUse: use the sentence to start the field split and then cite only the recovered governing pattern results
  neighboringClaimBoundary: proof, assurance, scale-success, module-substitutability, and architecture-quality claims apply the governing pattern for the recovered claim being made
  remainingReaderUse: write the smallest governing-pattern result for the recovered scale, state, module-interface, flow, evidence, or assurance claim; otherwise keep ordinary source wording or quote-only wording
  disposition: local-rewrite plus governing-pattern-ref application for each recovered claim being made; blocked or reduced-use cue for the rest
```

A compact local rewrite can therefore say: `The response cache is a candidate state-bearing architecture structure. Architecture scaling, mathematical-lens use, proof, and assurance claims are separate claims; apply C.16.P, C.29, C.31.ASAP, A.10, B.3, or G.6 only when one of those claims is being made.`

#### C.30.STRAT:4.6 - Lowering and reopen conditions

A `StratificationSourceLabelRepairNote` remains admissible only while its source span, selected `ontologicalNeighborhood`, governing pattern, and remaining reader use stay recoverable. Reopen or lower the repair when:

- the source label starts carrying a new relation, characteristic, publication, evidence, assurance, gate, work, decision, causal-use, or mathematical-lens claim;
- a direct governing pattern becomes recoverable and `C.30.STRAT` no longer buys action guidance;
- the selected neighborhood was chosen by label similarity rather than by recovered apparatus;
- the repair preserves kind recovery but leaves no useful admissible reader use;
- `E.10.ARCH` changes the required recovery fields, `C.30.P` changes architecture-wording repair law, `F.19` changes apparatus-vs-usability policy, or a more source-label realization pattern now governs a label family currently repaired here.

Lower the result to quote-only, reduced-use cue, blocked use, or incomplete rewrite when the governing pattern, admissible use, non-admissible use, or remaining reader use cannot be stated.

### C.30.STRAT:5 - Archetypal Grounding

| Template element | `U.System` illustration | `U.Episteme` illustration |
| --- | --- | --- |
| Source-label cue | A neural-network architecture source says that an `expert block` sits above a `router layer`. | A source-publication note says that a `cache layer` keeps a diagram or view current. |
| Recovery result | `Expert`, `block`, `router`, and `layer` stay source labels until the repair recovers module-interface, function-like, path-selection, transformation-flow, or selected-structure apparatus. | `Cache` and `layer` stay source labels until the repair recovers publication source-currentness, view, state or currentness, or ordinary non-use apparatus. |
| Admissible move | Apply `A.6.M`, `A.6.F`, `E.18`, `C.30.TFS-REL`, `G.5`, or `C.11` only after the ontological neighborhood is recovered by value. | Apply `C.2.P`, `E.17`, `A.19.SPR`, `A.3.3`, `C.27.TA`, or `C.27` only after the publication named by value, episteme, state, temporal-aspect/rate-band claim, or authored temporal-claim adequacy is recovered. |

### C.30.STRAT:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto and Epist**, **Prag**, **Did**, and **Gov**. Scope: architecture and engineering source-label precision restoration, with non-architecture governing-pattern applications when recovery selects them.

This pattern intentionally biases away from lexical replacement and toward ontology-first recovery. The mitigation is the cheap-closure rule: ordinary source prose stays ordinary, quote-only wording stays quote-only, and already recovered cases skip `C.30.STRAT`.

### C.30.STRAT:7 - Conformance checklist

| ID | Check |
| --- | --- |
| `CC-C30STRAT-1` | The source label is copied as a source label before any FPF kind is assigned. |
| `CC-C30STRAT-2` | The repair names the source label, bounded text, selected `ontologicalNeighborhood`, primary `EntityOfConcern` kind, encountered FPF kind or reference, relation to the primary `EntityOfConcern`, recovered kind, relation, or claim-use, source-use disposition, governing pattern, admissible use, non-admissible use, and remaining reader use. |
| `CC-C30STRAT-3` | No root kind or universal kind is minted for layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or stratification. |
| `CC-C30STRAT-4` | The selected `ontologicalNeighborhood` and governing-pattern row select the governing pattern; the source label does not select the pattern nest by itself. |
| `CC-C30STRAT-5` | Already recovered cases use the governing pattern directly instead of detouring through this pattern. |
| `CC-C30STRAT-6` | The repair distinguishes the neighborhoods in `C.30.STRAT:4.2` when any of them are being used, and it does not compress several ontological neighborhoods being used into one word. |
| `CC-C30STRAT-7` | Subject patterns use at most a thin pointer to this pattern and do not copy this trigger table. |
| `CC-C30STRAT-8` | The result preserves one useful admissible reader use; if no move remains, the disposition is quote-only, reduced-use cue, blocked use, or incomplete rewrite rather than recovered by value. |

### C.30.STRAT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Source label as ontology | `layer`, `block`, `expert`, `cache`, or `gate` is treated as a kind by label. | Complete the `StratificationSourceLabelRepairNote` and select the governing pattern from the recovered neighborhood. |
| C.30 takeover | Any structure-like word is treated as governed by C.30 because it sounds architectural. | Choose by selected `ontologicalNeighborhood`; non-source-label claims are governed by the patterns named in `C.30.STRAT:4.2`. |
| Local trigger fanout | `A.6.M`, `C.30.LCA`, `C.31`, or another subject pattern copies a growing label table. | Keep one thin pointer to `C.30.STRAT` and keep the subject pattern to its own invariant. |
| Expert-as-role false positive | `expert` in MoE prose becomes an `A.2` role-assignment or A.15 work-responsibility claim by word alone. | Treat as source label for submodel, transformation, path selection, or candidate selection unless an `A.2`, `A.2.1`, or `A.15` role-assignment, responsibility, or work claim is actually being made. |
| Gate-as-gate-decision false positive | A gating function, UI label, or source word becomes gate passage. | Use `A.20` or `A.21` only for actual constraint-validity or gate-decision claims; otherwise use the function, flow, publication, or ordinary-label disposition named by value. |

### C.30.STRAT:9 - Consequences

| Benefit | Trade-off or mitigation |
| --- | --- |
| Source labels remain usable recognition cues without becoming root kinds. | The reader pays one recovery-row cost only when FPF-governed use is being made; ordinary prose closes cheaply. |
| Subject patterns avoid copied trigger registries. | Subject patterns need accurate thin pointers to `C.30.STRAT` and still keep their own invariants precise. |
| Source-label wording no longer captures non-source-label claims by sound. | The repair may name several governing patterns when one sentence compresses several claims; the benefit is that each claim remains governed by its governing pattern. |

### C.30.STRAT:10 - Rationale

Stratification words are common because they compress local practice. That compression is useful at entry time and unsafe as ontology. FPF therefore keeps the word as a source label, recovers the `ontologicalNeighborhood`, and then uses the governing pattern for the recovered claim.

The pattern is placed under `C.30` because architecture and structure prose is the recurring entry point. The placement does not make `C.30` the governing pattern for every recovered case. If the recovery result is outside source-label repair, the governing pattern named in `C.30.STRAT:4.2` carries the recovered claim content.

### C.30.STRAT:11 - SoTA-Echoing

Reduced SoTA is sufficient for this precision-restoration pattern. The source practice being adopted is not a new external ontology; it is the observed architecture and engineering habit of using compact labels such as `layer`, `level`, `tier`, `stack`, `block`, `expert`, `cache`, `router`, and `gate` as local recognition language. FPF adapts that practice by keeping labels as source labels and requiring ontology-first recovery before they carry FPF-governed use.

Internal FPF current practice is the governing source here: `E.10` supplies trigger handling, `E.10.ARCH` supplies the recovery architecture, `C.30.P` supplies architecture and structure wording repair, `F.19` supplies apparatus-vs-usability discipline, and governing patterns carry recovered cases. The `Solution`, checklist, worked cases, and relations in this pattern change because that source-use disposition rejects lexical replacement and trigger-table fanout.

**Currentness front.** Recheck this pattern when `E.10.ARCH` changes the recovery row fields, `C.30.P` changes architecture or structure wording repair, `F.19` changes apparatus policy, or a more source-label realization pattern now governs a label family currently repaired here. The smallest changed locus is the affected row field, Relations entry, worked case, or subject-pattern thin pointer; do not rebuild a local trigger registry.

### C.30.STRAT:12 - Relations

- `E.10` catches the trigger and selects this pattern only when stratification or architecture-operation source-label recovery is needed.
- `E.10.ARCH` supplies the recovery architecture, placement rule, and anti-fanout discipline.
- `C.30.P` remains the broader architecture and structure wording repair. `C.30.STRAT` is the narrower stratification source-label realization when those labels recur with a stable recovery shape.
- `A.6.M` governs only recovered module-interface relation and interface-specification cases.
- `C.30.LCA` governs only recovered control-structure view cases with control roles, relations, rate bands, control-layer labels, and bounded context.
- `C.31` and `C.31.RSA` govern only recovered characteristic, reusable-locus, bespoke-residue, `accountingBasisRef`, or report-only share cases.
- `C.33`, `C.34`, and `C.35` carry recovered source-label cases when the label is used for architecture-specific captured structure, lost structure, preserved structure, lost structure in a preservation claim, generated carrier adequacy, or discovered carrier adequacy. `C.30.STRAT` only recovers the source label and receiving owner.
- `C.2.P`, `E.17`, `A.6.F`, `E.18`, `C.30.TFS-REL`, `C.16.P`, `A.19.SPR`, `C.29`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `A.2`, `G.5`, and `C.11` carry their recovered cases when the case is named by value.

Neighboring claims stay with their governing patterns: `A.22` for selected-structure EntityOfConcern, `C.30` for grounded architecture and selected-structure adequacy, `C.30.P` for architecture and structure precision restoration, `C.30.ASV` for structural-view adequacy, `C.30.LCA` for control-structure view adequacy, `A.6.M` for module-interface repair, `A.6.F` for function-use repair, `E.18` for graph, path, crossing, and flow-valuation discipline, `C.16` for characterization, `C.29` for mathematical-lens use, `C.2.P` for source and publication relation repair, and the non-source-label governing patterns named in `C.30.STRAT:4.2`. `C.30.STRAT` governs stratification wording and architecture-operation source-label repair only.

### C.30.STRAT:End

