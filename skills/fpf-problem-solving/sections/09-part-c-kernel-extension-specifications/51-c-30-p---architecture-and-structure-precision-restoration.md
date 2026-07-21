## C.30.P - Architecture and Structure Precision Restoration

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Architecture-structure wording repair.

**Intent.**
Recover architecture or structure wording whose selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or named C.30 subcase is hidden before a reader applies `A.22`, `C.30`, `C.30.ASV`, or a named `C.30.*` pattern.

This pattern does not mint `U.Architecture`, does not fuse architecture and structure into one kind, and does not replace grounded architecture adequacy or structural-view adequacy. It repairs overloaded wording so the architecture, structure, description, view, publication, source, relation, characteristic, mathematical-lens, evidence, assurance, gate, work, decision, causal-use, release, or ordinary-prose use becomes recoverable by value.

**Builds on.** `E.10`, `E.10.ARCH`, `A.22`, `C.30`, `C.30.ASV`, `C.2.P`, `A.6.P`, `A.6.F`, `C.29`, `C.16.P`, `C.16`, `C.25`, `E.17`, and `E.8`.

**Coordinates with.** `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, named `C.30.*` structure and view patterns, `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, `C.28`, `A.15`, `E.11`, and work, release, and publication patterns governing those claims.

**E.10.ARCH governing relation.** When `E.10` encounters architecture or structure wording whose selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, source label, or neighboring claim is hidden, `E.10.ARCH` selects `C.30.P` only until the use under repair and governing pattern are recovered. `C.30.P` then stops applying; it does not become a registry of architecture topics or a substitute for `A.22`, `C.30`, `C.30.AD`, or named `C.30.*` patterns.

### C.30.P:0 - Use this when

Use this pattern when architecture or structure wording hides which use is being made and recoverable by value.

Typical triggers:

- `architecture`, `architecture description`, `architecture model`, `architecture diagram`, `architecture map`, `architecture dashboard`, `architecture score`;
- `structure`, `structural view`, `structural model`, `module layout`, `component structure`, `interface structure`, or stratification wording or source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` that must go to `C.30.STRAT` before local architecture or structure assignment;
- `graph`, `flow`, `transformation-flow graph expression`, `control sketch`, `LCA diagram`, `ADR`, `dashboard`, `benchmark`, `source`, or `view` being treated as architecture or structure by wording alone;
- a function, module, interface, signature, flow, control, quality, score, evidence, assurance, gate, work, decision, causal-use, or release claim being smuggled under architecture or structure wording.

**What goes wrong if missed.** A diagram becomes the architecture, a graph becomes proof, a view becomes the selected structure, a source document becomes an architecture decision, a score becomes architecture adequacy, or a function, module, or interface claim becomes architecture by default.

**What this buys.** The reader can recover the architecture or structure use under repair, block the overread, and move to the governing pattern: selected structure under `A.22`, grounded architecture claim or conditional architecture description under `C.30`, architecture structural view under `C.30.ASV`, stratification-wording repair and source-label repair under `C.30.STRAT`, architecture transformation-flow relation under `C.30.TFS-REL`, control-structure view under `C.30.LCA`, mathematical lens under `C.29`, characteristic and scale repair under `C.16.P`, or a project-side evidence, assurance, gate, work, decision, causal-use, release, or publication pattern.

**First useful move.** Ask which selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or neighboring claim the architecture or structure wording is actually naming, then either apply the architecture or structure pattern named by value directly or use one `architecture-structure repair note` to assign the claim elsewhere.

**Not this pattern when.**

- If the use under repair is already a selected structure, use `A.22` directly.
- If the use under repair is already `ArchitectureOf@Context`, use `C.30` directly. If the use under repair is the full `ArchitectureDescription@Context` mechanism, use `C.30.AD`; use `C.30` only for the thin architecture-description bridge tied to one architecture move.
- If the use under repair is already an architecture structural view, use `C.30.ASV` or a named `C.30.*` view pattern directly.
- If the claim being made is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens use, characteristic and scale construction, quality characterization, source-use, or relation construction, use the governing pattern for that claim after any architecture or structure wording is demoted or assigned.

### C.30.P:1 - Problem frame

Working engineers often say "architecture" or "structure" while pointing at a useful artifact: a diagram, model, graph, table, dashboard, ADR, code-agent relation graph, neural-network architecture-operation diagram, benchmark result, or source document. Ordinary speech is acceptable; FPF-governed prose is not. If the artifact is named by a source label such as `block`, `layer`, `expert`, `cache`, `router`, or `gate`, use `C.30.STRAT` before assigning the recovered use locally.

The repair question is:

> Which selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or neighboring claim does the wording name, and which FPF pattern governs that claim?

The architecture or structure use under repair may be:

- selected structure under `A.22`;
- an `ArchitectureOf@Context` claim under `C.30`, a thin architecture-description bridge under `C.30`, or the full architecture-description mechanism under `C.30.AD`;
- an `ArchitectureStructuralView@Context` or named `C.30.*` subcase;
- a publication, view, face, `PublicationUnit`, carrier, dashboard, ADR, source document, or source-return relation under `C.2.P` or `E.17`;
- a relation construction under `A.6.P`;
- a function or functionality-kind use under `A.6.F`;
- a mathematical-lens use claim under `C.29`;
- a characteristic, scale, score, coordinate, threshold, or quality-coordinate claim under `C.16.P` or `C.16`;
- a Q-bundle or quality-characterization claim under `C.16.Q`, `C.25`, or `E.21`;
- an evidence, assurance, gate, work, decision, causal-use, release, or method claim under its governing pattern;
- ordinary prose with no FPF-governed use being made.

### C.30.P:2 - Problem

How can FPF repair architecture or structure wording without:

- creating `U.Architecture`;
- treating architecture and structure as one fused kind;
- treating a description, view, diagram, graph, dashboard, source, ADR, model, or publication as the architecture itself;
- assigning all function, flow, module-interface, signature, control, evidence, assurance, gate, decision, work, quality, mathematical-lens, or source claims to architecture;

- duplicating first-stage repair lists inside `A.22`, `C.30`, `C.30.ASV`, and every named `C.30.*` subpattern?

### C.30.P:3 - Forces

| Force | Tension |
| --- | --- |
| Ordinary engineering speech vs FPF kind recovery | Engineers need compact words such as architecture, structure, model, view, graph, module, layer, block, expert, cache, router, and gate; FPF claims need recovered kind, relation, source-use relation, and admissible use. `C.30.STRAT` governs the stratification-wording family and source-label family before `C.30.P` assigns any architecture or structure portion. |
| Architecture description vs architecture itself | Descriptions and views are useful, but they can be overread as the selected structure or architecture claim. |
| Structure generality vs architecture specificity | `A.22` gives selected structure; `C.30` governs grounded architecture adequacy over selected architecture-relevant structures and admits only the thin architecture-description bridge when durable description use is being made. `C.30.AD` governs the full architecture-description mechanism. The repair must not collapse them. |
| Small first move vs heavy record | Most wording cases need one repair note and a direct governing-pattern assignment, not a full architecture description. |
| Source and view usefulness vs project authority | A source, dashboard, graph, ADR, or view can guide architecture work without proving evidence, gate passage, decision authority, release permission, or work completion. |
| Cross-pattern consistency vs shadow registry | Architecture hosts should not carry duplicate trigger lists once `C.30.P` exists. |

### C.30.P:4 - Solution

Repair architecture or structure wording by producing an `architecture-structure repair note` or an equivalent local rewrite.

Minimum fields:

```text
ArchitectureOrStructureRepairNote:
  triggerSpan:
  boundedTextSpanOrPublicationUnit:
  encounteredFPFKindOrReference:
  candidateClaimUses:
  selectedClaimUse:
  sourcePublicationRelationSet?:
  relationClaimSlice?:
  functionOrFunctionalityClaim?:
  structureKindOrArchitectureQuestion?:
  characteristicOrQualityClaimSlice?:
  mathLensClaimSlice?:
  projectSideClaim?:
  governingPatternRef:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderUse:
  disposition:
```

Use the note only when the repair must remain inspectable. A direct local rewrite is enough when one sentence clearly names the selected-structure claim being made, architecture relation, architecture-description use, structural-view use, source-return relation, or governing pattern.

#### C.30.P:4.1 - Recovery sequence

1. **Capture the trigger.** Copy the architecture or structure wording and the sentence that uses it.
2. **Recover the encountered FPF kind or reference.** Decide whether the text points to a selected structure, architecture claim, description, view, diagram, graph, model, dashboard, ADR, source document, carrier, publication, stratification-wording case or source-label case for `C.30.STRAT`, function, module-interface relation, signature, flow, control, score, quality term, evidence, gate, work, decision, release, or ordinary prose.
3. **Recover source-publication relations before architecture assignment.** If the wording relies on a source, publication, view, face, `PublicationUnit`, dashboard, ADR, file, carrier, or source-return relation, apply `C.2.P` for source-use, source-currentness, and publication relations before assigning the architecture or structure claim.
4. **Choose the governing pattern for the architecture or structure use.**
   - selected structure -> `A.22`;
   - `ArchitectureOf@Context`, selected architecture-relevant structure, or thin conditional `ArchitectureDescription@Context` bridge use -> `C.30`;
   - full `ArchitectureDescription@Context` mechanism -> `C.30.AD`;
   - architecture structural view -> `C.30.ASV`;
   - architecture transformation-flow relation -> `C.30.TFS-REL`;
   - control-structure view -> `C.30.LCA`;
   - cross-scope conflict or frustration triage -> `C.30.ILC`;
   - stratification wording or source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` -> `C.30.STRAT` before choosing the final governing pattern;
   - named C.30 subcase -> that subpattern.
5. **Assign non-architecture claims to their governing patterns.** If the sentence uses architecture wording to carry relation, function or functionality, mathematical-lens, characteristic and scale, quality, evidence, assurance, gate, work, decision, causal-use, release, or method claim, apply the governing pattern for that claim and keep this pattern only for the architecture or structure wording repair.
6. **State admissible and non-admissible use.** Say what the reader may do with the repaired wording and what non-admissible adjacent interpretation is blocked.
7. **Stop C.30.P after assignment.** Stop after the governing pattern or ordinary-prose demotion is named.

### C.30.P:5 - Direct governing-pattern assignments

| Recovered use, claim kind, or admissible-use boundary | Governing pattern |
| --- | --- |
| selected structure, structural description, structure source-return | `A.22` |
| `ArchitectureOf@Context`, selected architecture-relevant structure, thin conditional `ArchitectureDescription@Context` bridge use, architecture question card | `C.30` |
| full `ArchitectureDescription@Context` mechanism, architecture-description multi-view set, architecture-description specification-use boundary | `C.30.AD` |
| architecture structural view, structure-kind view, hidden or lost structure | `C.30.ASV` |
| transformation-flow graph expression, flow relation, architecture-to-transformation-flow relation | `C.30.TFS-REL` when an architecture-to-transformation-flow relation claim is being made; otherwise `E.18` or the governing pattern for the claim being made |
| architecture-synthesis wording | Recover the concrete claim kind, then use the architecture-synthesis routing note below. |
| control structure view, LCA sketch or control sketch | `C.30.LCA` when an architecture control-structure view claim is being made |
| cross-scope conflict or frustration triage | `C.30.ILC` when that question is being asked |
| source, publication, carrier, view, face, `PublicationUnit`, dashboard, ADR, documentation, source-return | `C.2.P`, `E.17`, `E.17.0`, or the publication or source-use pattern governing the claim |
| relation construction, basedness, source, base-dependence, evidence and relation-claim discrimination, endpoint compression, comparison | `A.6.P` or the A.6 specialization selected by the recovered claim |
| function, functional, functionality, effect, module, interface, or signature claim | `A.6.F`, `A.6.M`, A.6 signature and slot pattern, or the retained module, interface, or signature specialization selected by the claim |
| stratification or source labels such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` | `C.30.STRAT`; after recovery, use `A.22`, `C.30`, `C.30.ASV`, `C.30.LCA`, `C.30.TFS-REL`, `A.6.M`, `A.6.F`, `E.18`, `C.16.P`, `C.29`, or the pattern governing the recovered claim |
| mathematical lens, mapping, model, similarity, preserved-structure and lost-structure as mathematical-lens use | `C.29` |
| characteristic, scale, metric, score, indicator, threshold, architecture score, quality coordinate | `C.16.P`, then `C.16`, `A.19`, `C.25`, `E.21`, or the pattern governing the claim |
| quality-term or evaluative characterization | `C.16.Q`, `C.25`, `E.21`, or the characterization pattern governing the claim |
| evidence, proof, validation, witness | `A.10` or the evidence pattern governing the claim |
| assurance, engineering justification, safety case | `B.3` or the assurance pattern governing the claim |
| gate, admissibility, release, approval | `A.20`, `A.21`, release or admissibility pattern, or the gate pattern governing the claim |
| work, method, implementation, operation, change execution | `A.15`, `A.15.4`, `U.Method`, `U.MethodDescription`, or the work or method pattern governing the claim |
| decision, choice, trade-off result | `C.11` or the decision pattern governing the claim |
| causal-use or intervention claim | `C.28` |

Architecture-synthesis routing note:

- Use `C.32`, `C.32.MLAO`, `C.32.CONWAY`, or `C.32.FAIL` when the recovered claim is a candidate palette, residual-reducing multilevel frame, transformer and transformed correspondence frame, or architecture-synthesis repair cue.
- Use `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, or `G.5` when the recovered claim is comparison-policy use, selector-policy use, local choice, or selected-set publication.
- Use `C.18` or `C.19` when the recovered claim is archive, front, or pool policy.
- For transformation-flow, function, module, transformer, mathematical-lens, relation-signature, affordance, architecture role, or move-like wording, recover that claim kind first and use its governing pattern by value.

### C.30.P:5a - Refresh and reopen conditions

Reopen or narrow `C.30.P` when the FPF pattern-language ecology changes the first architecture or structure entry:

- a named `C.30.*`, structural-view, architecture transformation-flow, LCA or control, module-interface, mathematical-lens, characteristic, evidence, assurance, gate, work, decision, causal-use, release, or publication pattern now governs one row directly;
- source-current architecture-description, view, model, decision-record, or architecture-documentation practice changes one adopted distinction in `C.30.P:7`;
- README, ToC, `E.11`, retrieval, or local Problem-frame entry cues change the first practical entry for hidden architecture or structure wording;
- a governing pattern starts copying first-stage architecture or structure trigger lists that belong here;
- `C.30.P` begins to act as a registry of architecture topics rather than a wording-use repair pattern for hidden selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or named C.30 subcase.

The refresh action is to remove, narrow, or reassign the first-stage row. It is not to preserve old assignment wording as history.

### C.30.P:6 - Worked cases

| Wording | Repair |
| --- | --- |
| "The architecture is the diagram." | The diagram is a publication, carrier, source cue, architecture description rendering, or structural view. It is not the architecture itself. Apply `C.2.P` if a a source-publication relation set is being made, then `C.30` or `C.30.ASV` only if the architecture claim or structural view is recovered. |
| "`ArchitectureOf@PlantOps` is defined over structures S1 and S2 under context C." | Direct `C.30`; no `C.30.P` unless another selected structure, architecture-description use, structural-view use, source-return relation, or named C.30 subcase remains hidden. |
| "This ADR changed the architecture." | Recover whether the ADR is a publication, decision record, document with named source-use relation, architecture-description update, work plan, or ordinary source. Use `C.2.P`, `C.11`, `A.15`, or `C.30` when the corresponding claim kind is being made. |
| "The flow graph proves the architecture is safe." | Flow graph expression and architecture-to-transformation-flow relation are not proof or safety assurance. Use `E.18` and `C.30.TFS-REL` for flow relation, `B.3` or evidence patterns for assurance, `C.30` only for the grounded architecture claim or thin conditional architecture-description bridge, and `C.30.AD` when the full architecture-description mechanism is being used. |
| "The architecture score improved." | Recover whether the sentence means grounded architecture adequacy, selected-structure characteristic and scale score, pattern-quality coordinate, Q-bundle, benchmark result, gate threshold, or ordinary comparison. Apply `C.16.P` before any score-based use. |
| "Functional architecture improved maintainability." | Recover function or functionality use via `A.6.F` when hidden, then architecture structural view via `C.30.ASV` or quality or maintainability via `C.16.P`, `C.16.Q`, `C.25`, or quality pattern governing the claim. |
| "The module layer supports the architecture." | Treat `layer` first as a source label and apply `C.30.STRAT`. Return to C.30.P only for the architecture or structure portion after recovery; return to `A.6.M` only if a module-interface relation is recovered, to `C.30.LCA` only if a control-layer relation is recovered, to `C.2.P` if this is a publication label or view label, to `A.6.P` if a basedness, source-use, evidence, or reliance relation is being made, or to ordinary source-label disposition. |

### C.30.P:7 - Reduced SoTA row

Current architecture-description, model, view, and decision-record practice treats architecture as distinct from architecture descriptions, models, views, viewpoints, diagrams, and decision records. FPF adopts that line only where it changes action guidance: examples, non-use boundaries, governing-pattern assignments, source-return conditions, and conformance checks.

| Practice source | Source-use relation and currentness | What `C.30.P` adopts or adapts | FPF import boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 on architecture descriptions, architecture viewpoints, model kinds, and conformance requirements. | Current standard and reference source for architecture-description and viewpoint separation. | Disciplines direct use of `C.30` and `C.30.ASV`; blocks diagram-as-architecture, model-as-architecture, view-as-architecture, and publication-as-architecture overread; disciplines `CC-C30P-2`, `CC-C30P-3`, and `CC-C30P-4`. | Does not import 42010 terminology as FPF ontology; FPF still uses `A.22`, `C.30`, `C.30.ASV`, and named `C.30.*` patterns. |
| SEI "Documenting Software Architectures: Views and Beyond" practice line. | Current reference and lineage source for documenting views for stakeholder use. | Disciplines the source, publication, and view split in worked cases and keeps view artifacts useful without making them the selected structure. | Does not make "view" a generic proof or decision record. |
| C4 model current practice for developer-friendly architecture diagrams over context, container, component, and code views. | Current practice anchor for diagram usefulness and diagram limits. | Disciplines the diagram, block, component, module, and layer examples: a diagram can be an entry or view publication, and source labels are recovered through `C.30.STRAT` before architecture or structure assignment. | Does not make C4 levels, blocks, layers, or containers FPF structure kinds or mandatory architecture views. |
| arc42 current architecture documentation template practice. | Current practice and reference source for architecture communication, constraints, decisions, and cross-cutting concerns. | Disciplines the distinction between documentation template sections, source publications, decisions, architecture claims, and conditional architecture-description use. | Does not let a documentation section, template heading, or dashboard become architecture authority by label. |
| ADR and MADR architecture decision record practice. | Current practice and lineage source for decision-record separation; current empirical ADR work may refine template choice, but does not replace FPF decision ontology. | Disciplines the ADR worked case and the assignment to `C.2.P`, `C.11`, `A.15`, or `C.30`: an ADR may record or motivate a decision; it is not automatically the architecture decision, work execution, or architecture itself. | Does not import ADR label as gate, release, proof, or FPF decision authority. |

This row belongs in this pattern because it blocks diagram-as-architecture, graph-as-proof, view-as-structure-kind, publication-as-claim, and ADR-as-decision overreads. It does not import any external standard as FPF ontology.

### C.30.P:8 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-C30P-1` | The repair names the trigger span, encountered FPF kind or reference, selected use under repair, governing pattern, admissible use, non-admissible use, and remaining reader use. |
| `CC-C30P-2` | A diagram, model, graph, dashboard, ADR, source, publication, view, face, `PublicationUnit`, file, carrier, or rendering is not treated as architecture or structure by appearance. |
| `CC-C30P-3` | Direct `A.22`, `C.30`, `C.30.ASV`, or named `C.30.*` use applies the governing pattern directly when the selected-structure claim being made, architecture relation, architecture-description use, structural-view use, or named C.30 subcase is already recoverable. |
| `CC-C30P-4` | Source-use, currentness, and publication-to-carrier relation recovery uses `C.2.P` before architecture or structure claim use when that relation set is being made. |
| `CC-C30P-5` | Function-like, relation-like, mathematical-lens, characteristic and scale, quality, evidence, assurance, gate, work, decision, causal-use, release, and method claims are assigned to their governing patterns. |
| `CC-C30P-6` | The repair does not mint `U.Architecture`, `ArchitectureStructure`, a generic architecture head, or mandatory architecture-repair record. |
| `CC-C30P-7` | The subject architecture or structure pattern keeps its own invariant central and carries at most a thin pointer back to this pattern. |
| `CC-C30P-8` | The repaired wording preserves one useful admissible reader use; type-correct but inert architecture wording is not recovered by value. |

### C.30.P:9 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Diagram-as-architecture | A diagram, graph, dashboard, ADR, or generated view is said to be the architecture. | Recover publication, carrier, view, or source-use relation and then apply `C.30` or `C.30.ASV` only if the architecture claim or structural-view claim is being made. |
| Architecture-as-proof | Architecture wording carries evidence, assurance, causal proof, gate passage, release permission, or decision authority. | Apply `A.10`, `B.3`, `C.28`, `A.20`, `A.21`, `C.11`, release, or the pattern governing the claim being made. |
| Function-as-default-architecture | Any function, interface, module behavior, or source label such as block is treated as architecture. | Use `C.30.STRAT` for source-label recovery where needed, then `A.6.F`, `C.30.ASV` functional-structure, `C.30.TFS-REL` transformation-flow structure relation, `A.6.M` module-relation repair, or quality pattern governing the claim. |
| Score-as-architecture | A score, metric, benchmark, or quality coordinate is used as architecture adequacy. | Apply `C.16.P` and the measurement named by value, characteristic-space, Q-bundle, pattern-quality, gate, or benchmark pattern. |
| Viewpoint-as-structure-kind | A viewpoint label is used as if it selected structure kind. | Use `C.30.ASV`; recover structure kind and viewpoint separately. |
| Repair registry duplication | `A.22`, `C.30`, `C.30.ASV`, or a named `C.30.*` host copies architecture or structure first-stage repair lists. | Keep the subject invariant there and use one thin pointer to `C.30.P`. |

### C.30.P:10 - Related patterns

- `E.10` catches architecture or structure wording and selects this pattern only when the selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or named C.30 subcase is hidden.
- `E.10.ARCH` defines the shared wording-use recovery order and applicability row.
- `A.22` governs selected structure and structural views as structure.
- `C.30` governs grounded `ArchitectureOf@Context` adequacy and thin conditional `ArchitectureDescription@Context` bridge use.
- `C.30.AD` governs the full architecture-description mechanism when `ArchitectureDescription@Context` is the EntityOfConcern under repair.
- `C.30.ASV` governs architecture structural views.
- `C.30.STRAT` governs stratification wording or source-label wording before C.30.P assigns any recovered architecture or structure portion.
- Named `C.30.*` patterns govern their own structure adequacy or view adequacy questions.
- `C.2.P` recovers source, publication, view, face, `PublicationUnit`, carrier, and source-use disposition.
- `A.6.P` repairs relation construction; `A.6.F` repairs function and functionality wording; `A.6.M` repairs module-relation and interface-specification wording.
- `C.16.P` repairs characteristic-and-scale wording, and `C.16.Q` repairs quality-term or evaluative characterization wording before score or quality use.
- `C.29` governs mathematical-lens use and does not become architecture by analogy.

### C.30.P:End

