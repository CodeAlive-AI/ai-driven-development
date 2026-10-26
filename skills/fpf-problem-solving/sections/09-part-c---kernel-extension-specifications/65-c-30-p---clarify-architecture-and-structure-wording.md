## C.30.P - Clarify Architecture and Structure Wording (Precision Restoration)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Architecture-structure wording repair.

**Intent.**
Recover architecture or structure wording whose selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or named C.30 subcase is hidden before a reader applies `A.22`, `C.30`, `C.30.ASV`, or a named `C.30.*` pattern.

This pattern does not mint `U.Architecture`, does not fuse architecture and structure into one kind, and does not replace grounded architecture adequacy or structural-view adequacy. It repairs overloaded wording so the architecture, structure, description, view, publication, source, relation, characteristic, mathematical-lens, evidence, assurance, gate, work, decision, causal-use, release, or ordinary-prose use becomes recoverable by value.

**Builds on.** `E.10`, `E.10.ARCH`, `A.22`, `C.30`, `C.30.ASV`, `C.2.P`, `A.6.P`, `A.6.F`, `C.29`, `C.16.P`, `C.16`, `C.25`, `E.17`, and `E.8`.

**Coordinates with.** `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, named `C.30.*` structure and view patterns, `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, `C.28`, `A.15`, `E.11`, and work, release, and publication patterns defining or constraining those claims.

**E.10.ARCH applicability rule.** When `E.10` encounters architecture or structure wording whose selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, source label, or neighboring claim is hidden, `E.10.ARCH` selects `C.30.P` only until the use under repair and subject pattern are recovered. `C.30.P` then stops applying; it does not become a registry of architecture topics or a substitute for `A.22`, `C.30`, `C.30.AD`, or named `C.30.*` patterns.

### C.30.P:0 - Use this when

Use this pattern when architecture or structure wording hides which use is being made.

Typical triggers:

- `architecture`, `architecture description`, `architecture model`, `architecture diagram`, `architecture map`, `architecture dashboard`, `architecture score`;
- `structure`, `structural view`, `structural model`, `module layout`, `component structure`, `interface structure`, or stratification wording or source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` whose technical meaning must be recovered through `C.30.STRAT` before local architecture or structure assignment;
- `graph`, `flow`, `transformation-flow graph expression`, `control sketch`, `LCA diagram`, `ADR`, `dashboard`, `benchmark`, `source`, or `view` being treated as architecture or structure by wording alone;
- a function, module, interface, signature, flow, control, quality, score, evidence, assurance, gate, work, decision, causal-use, or release claim being smuggled under architecture or structure wording.

**What goes wrong if missed.** A diagram becomes the architecture, a graph becomes proof, a view becomes the selected structure, a source document becomes an architecture decision, a score becomes architecture adequacy, or a function, module, or interface claim becomes architecture by default.

**What this buys.** The reader can state the intended claim, retain its useful content, and use the pattern that addresses the remaining question. Clear ordinary wording needs no repair record.

**First useful move.** Recover what the sentence says and what the reader needs to do with it. Keep adequate ordinary wording. Otherwise rewrite the ambiguous claim, then use its subject pattern for any remaining substantive question. A repair note is optional when the repair needs to remain inspectable.

**Not this pattern when.**

- If the use under repair is already a selected structure, use `A.22` directly.
- For an already recoverable `ArchitectureRelation` or bounded `ArchitectureClaim`, use `C.30` directly. For architecture-description identity, correspondence or use, use `C.30.AD`; use `C.30` for the initial description question tied to one architecture move.
- If the use under repair is already an architecture structural view, use `C.30.ASV` or a named `C.30.*` view pattern directly.
- If the claim being made is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens use, characteristic and scale construction, quality characterization, source-use, or relation construction, use the subject pattern for that claim after any architecture or structure wording is demoted or assigned.

### C.30.P:1 - Problem frame

Working engineers often say "architecture" or "structure" while pointing at a useful artifact: a diagram, model, graph, table, dashboard, ADR, code-agent relation graph, neural-network architecture-operation diagram, benchmark result, or source document. Ordinary shorthand is acceptable in FPF-governed prose when the intended use is recoverable. If the artifact is named by a source label such as `block`, `layer`, `expert`, `cache`, `router`, or `gate` whose technical meaning remains unclear, use `C.30.STRAT` before assigning the recovered use locally.

The repair question is:

> Which selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or neighboring claim does the wording name, and which FPF pattern defines or constrains that claim?

The architecture or structure use under repair may be:

- selected structure under `A.22`;
- an `ArchitectureRelation` or bounded `ArchitectureClaim` under `C.30`, its initial description question, or architecture-description use under `C.30.AD`;
- an `ArchitectureStructuralView@Context` or named `C.30.*` subcase;
- a publication, view, face, `PublicationUnit`, carrier, dashboard, ADR, source document, or source-return relation under `C.2.P` or `E.17`;
- a relation construction under `A.6.P`;
- a function or functionality-kind use under `A.6.F`;
- a mathematical-lens use claim under `C.29`;
- a characteristic, scale, score, coordinate, threshold, or quality-coordinate claim under `C.16.P` or `C.16`;
- a Q-bundle or quality-characterization claim under `C.16.Q`, `C.25`, or `E.21`;
- an evidence, assurance, gate, work, decision, causal-use, release, or method claim under its subject pattern;
- ordinary prose with no FPF-governed use being made.

### C.30.P:2 - Problem

The same word can name a structure, a claim about it, or a description used to inspect it. A repair must recover the intended object and claim without losing what the reader can use. It should finish when the sentence and applicable subject rule are clear.
### C.30.P:3 - Forces

| Force | Tension |
| --- | --- |
| Ordinary engineering speech vs FPF kind recovery | Engineers need compact words such as architecture, structure, model, view, graph, module, layer, block, expert, cache, router, and gate; FPF claims need recovered kind, relation, source-use relation, and admissible use. `C.30.STRAT` recovers stratification or source-label meaning when it still hides the technical claim, before `C.30.P` assigns the recovered architecture or structure portion. |
| Architecture description vs architecture itself | Descriptions and views are useful, but they can be overread as the selected structure or architecture claim. |
| Structure generality vs architecture specificity | `A.22` gives selected structure; `C.30` governs grounded architecture adequacy over selected architecture-relevant structures and admits only the thin architecture-description bridge when durable description use is being made. `C.30.AD` governs the full architecture-description mechanism. The repair must not collapse them. |
| Small first move vs heavy record | One clear sentence can complete the repair. A note or fuller architecture description is useful only when the receiving work needs its content. |
| Source and view usefulness vs project authority | A source, dashboard, graph, ADR, or view can guide architecture work without proving evidence, gate passage, decision authority, release permission, or work completion. |

### C.30.P:4 - Solution

Repair architecture or structure wording by producing an `architecture-structure repair note` or an equivalent local rewrite.

An optional note can organize the following information; include only what the repair needs:

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
  relationFunctionClaimRef:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderUse:
  disposition:
```

Use the note only when the repair must remain inspectable. A direct local rewrite is enough when one sentence clearly names the selected-structure claim being made, architecture relation, architecture-description use, structural-view use, source-return relation, or subject pattern.

#### C.30.P:4.1 - Recovery sequence

1. **Read the span.** Read the architecture or structure wording in its sentence and the nearby context needed to recover its meaning. Keep a copy only when the repair needs an inspectable record.
2. **Recover the object and claim.** Identify the subject, predicate, participants and intended use. Distinguish, for example, a selected structure from its description, or an architecture claim from a score or decision. Use the assignment table below for the unresolved kind; keep ordinary prose when no formal distinction changes the claim.
3. **Recover source-publication relations before architecture assignment.** If the wording relies on a source, publication, view, face, `PublicationUnit`, dashboard, ADR, file, carrier, or source-return relation and a source-use, source-currentness, or publication distinction remains hidden, apply `C.2.P` before assigning the architecture or structure claim. If that distinction and its subject pattern are already recoverable, use the subject pattern directly.
4. **Choose the subject pattern for the architecture or structure use.**
   - selected structure -> `A.22`;
   - `ArchitectureRelation`, bounded `ArchitectureClaim`, or its initial description question -> `C.30`;
   - architecture-description identity, correspondence or use -> `C.30.AD`;
   - architecture structural view -> `C.30.ASV`;
   - architecture transformation-flow relation -> `C.30.TFS-REL`;
   - control-structure view -> `C.30.LCA`;
   - cross-scope conflict or frustration triage -> `C.30.ILC`;
   - stratification wording or source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` -> `C.30.STRAT` while the label's technical meaning remains unclear, before choosing the final subject pattern;
   - named C.30 subcase -> that subpattern.
5. **Assign non-architecture claims to their subject patterns.** If the sentence uses architecture wording to carry relation, function or functionality, mathematical-lens, characteristic and scale, quality, evidence, assurance, gate, work, decision, causal-use, release, or method claim, apply the subject pattern for that claim and keep this pattern only for the architecture or structure wording repair.
6. **Preserve the useful conclusion.** State what the repaired wording supports. Add a blocked interpretation only when a plausible reader could take it here and the distinction changes the conclusion or action.
7. **Stop C.30.P after assignment.** Stop after the subject pattern or ordinary-prose demotion is named.

### C.30.P:5 - Subject pattern assignments

| Recovered use, claim kind, or admissible-use boundary | Subject pattern |
| --- | --- |
| selected structure, structural description, structure source-return | `A.22` |
| `ArchitectureRelation`, bounded `ArchitectureClaim`, initial architecture-description question, architecture question card | `C.30` |
| architecture-description identity or use, multi-view correspondence, architecture-description specification-use boundary | `C.30.AD` |
| architecture structural view, structure-kind view, hidden or lost structure | `C.30.ASV` |
| transformation-flow graph expression, flow relation, architecture-to-transformation-flow relation | `E.18.2` for a mathematical flow-graph expression; `E.18` for selected transformation-flow structure; `C.30.TFS-REL` for its bounded architecture-use record; otherwise the subject pattern for the claim being made |
| architecture-synthesis wording | Recover the concrete claim kind, then use the architecture-synthesis routing note below. |
| control structure view, LCA sketch or control sketch | `C.30.LCA` when an architecture control-structure view claim is being made |
| cross-scope conflict or frustration triage | `C.30.ILC` when that question is being asked |
| source, publication, carrier, view, face, `PublicationUnit`, dashboard, ADR, documentation, source-return | `C.2.P` while the relevant distinction remains hidden; otherwise `E.17`, `E.17.0`, or the publication or source-use pattern governing the claim |
| relation construction, basedness, source, base-dependence, evidence and relation-claim discrimination, endpoint compression, comparison | `A.6.P` or the A.6 specialization selected by the recovered claim |
| function, functional, functionality, effect, module, interface, or signature claim | `A.6.F`, `A.6.M`, A.6 signature and slot pattern, or the retained module, interface, or signature specialization selected by the claim |
| stratification or source labels such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` | `C.30.STRAT` while the label's technical meaning remains unclear; after recovery, use `A.22`, `C.30`, `C.30.ASV`, `C.30.LCA`, `C.30.TFS-REL`, `A.6.M`, `A.6.F`, `E.18`, `C.16.P`, `C.29`, or the pattern governing the recovered claim |
| mathematical lens, mapping, model, similarity, preserved-structure and lost-structure as mathematical-lens use | `C.29` |
| characteristic, scale, metric, score, indicator, threshold, architecture score, quality coordinate | `C.16.P` while the meaning remains unclear; otherwise `C.16`, `A.19`, `C.25`, `E.21`, or the pattern governing the claim |
| quality-term or evaluative characterization | `C.16.Q`, `C.25`, `E.21`, or the characterization pattern governing the claim |
| evidence, proof, validation, witness | `A.10` for source recovery and bounded reliance; the defining or testing pattern for the evidence, proof, validation, or witness claim itself |
| assurance, engineering justification, safety case | `B.3` or the applicable assurance pattern for a named assurance claim; the defining domain pattern for a separate safety claim |
| internal constraint, gate, admissibility, release, approval | `A.20` for an internal-constraint result; `A.21` for a named gate decision; the direct domain pattern for the particular admissibility, release, or approval claim |
| work, method, implementation, operation, change execution | `A.15` for the Work family; `A.15.4` while appearance hides a work-reliance prerequisite; `A.3.1` for `U.Method`; `A.3.2` for `U.MethodDescription`; or the work or method pattern governing the claim |
| decision, choice, trade-off result | `C.11` or the decision pattern governing the claim |
| causal-use or intervention claim | `C.28` |

Architecture-synthesis routing note:

- Use `C.32`, `C.32.MLAO`, `C.32.CONWAY`, or `C.32.FAIL` when the recovered claim is a candidate palette, residual-reducing multilevel frame, transformer and transformed correspondence frame, or architecture-synthesis repair cue.
- Use `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, or `G.5` when the recovered claim is comparison-policy use, selector-policy use, local choice, or selected-set result declaration. When publication is current, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.
- Use `C.18` or `C.19` when the recovered claim is archive, front, or pool policy.
- For transformation-flow, function, module, transformer, mathematical-lens, relation-signature, affordance, architecture-use, or move-like wording, recover that claim kind first and use its subject pattern by value.

### C.30.P:5a - Refresh and reopen conditions

Reopen the wording when a changed source meaning, intended use, subject predicate or receiving rule changes what the sentence asserts or what the reader may do with it. Repair the affected claim and its direct use. Retain an adequate sentence when only its packaging changes; a new template or neighboring pattern does not by itself make its meaning unclear.
### C.30.P:6 - Worked cases

| Wording | Repair |
| --- | --- |
| "The architecture is the diagram." | Recover how the diagram is used: as a publication, carrier, source cue, architecture-description rendering, or structural view. It is not the architecture itself. Apply `C.2.P` only while the source-publication distinction remains hidden, then `C.30` or `C.30.ASV` only if the architecture claim or structural view is recovered. |
| "`ArchitectureOf@PlantOps` is defined over structures S1 and S2 under context C." | Direct `C.30`; no `C.30.P` unless another selected structure, architecture-description use, structural-view use, source-return relation, or named C.30 subcase remains hidden. |
| "This ADR changed the architecture." | Recover whether the ADR is a publication, decision record, document with named source-use relation, architecture-description update, work plan, or ordinary source. Use `C.2.P`, `C.11`, `A.15`, or `C.30` when the corresponding claim kind is being made. |
| "The flow graph proves the architecture is safe." | Keep the flow-graph expression, selected flow structure, architecture-use account, and any proof or safety-assurance claim separate. Use `E.18.2` for the mathematical expression, `E.18` for the selected flow structure, `C.30.TFS-REL` for its bounded architecture-use record, `B.3` for assurance and the defining pattern for any separate proof, safety, or evidence claim; use `C.30` only for the grounded architecture claim or thin conditional architecture-description bridge, and `C.30.AD` when the full architecture-description mechanism is being used. |
| "The architecture score improved." | Recover whether the sentence means grounded architecture adequacy, selected-structure characteristic and scale score, pattern-quality coordinate, Q-bundle, benchmark result, gate threshold, or ordinary comparison. Use `C.16.P` while that meaning remains unresolved; an already clear score goes directly to its applicable measurement or evaluation rule. |
| "Functional architecture improved maintainability." | Recover hidden function wording through `A.6.F`, structural-view use through `C.30.ASV`, and the maintainability claim through `C.16.P`, `C.16.Q`, `C.25`, or its domain rule as needed. If improvement is attributed causally to the changed arrangement, use `C.28` for that further claim. |
| "The module layer supports the architecture." | Use `C.30.STRAT` if the source meaning of `layer` remains unclear. Use C.30.P only for the architecture or structure portion after recovery; use `A.6.M` only if a module-interface relation is recovered, `C.30.LCA` only if a control-layer relation is recovered, `C.2.P` if a publication-label or view-label distinction remains hidden, or `A.6.P` if a basedness, source-use, evidence, or reliance relation is being made; otherwise retain an ordinary source-label disposition. |

**Worked repair.** A review says, “The new module layer improved maintainability.” The available results report 80 seconds for revision R1 and 50 seconds for R2 on regression fixture F; the word *layer* merely labels the changed source grouping. The sufficient rewrite is: “On fixture F, the reported regression-test runtime was 80 seconds for R1 and 50 seconds for R2.” It preserves the observed comparison without claiming a structural layer, general maintainability gain or causal effect from two measurements. If the receiving task only needs that runtime comparison and its measurement basis is adequate, stop. If it needs a maintainability conclusion, establish how the measured runtime bears on that characteristic under `C.25` and the domain method; if it needs a causal conclusion, recover the additional intervention and comparison basis under `C.28`. If the grouping itself must be changed, recover its actual constituents and relations before using `A.22` or `C.30`. The stronger question selects the missing work; it does not invalidate the narrower measured result.

### C.30.P:7 - Reduced SoTA row

Architecture-description, model, view, and decision-record practice treats architecture as distinct from architecture descriptions, models, views, viewpoints, diagrams, and decision records. FPF adopts that line only where it changes action guidance: examples, non-use boundaries, subject-pattern assignments, source-return conditions, and conformance checks.

| Practice source | Source-use relation and currentness | What `C.30.P` adopts or adapts | FPF import boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 on architecture descriptions, architecture viewpoints, model kinds, and conformance requirements. | The cited standard is a reference source for architecture-description and viewpoint separation. | Disciplines direct use of `C.30` and `C.30.ASV`; blocks diagram-as-architecture, model-as-architecture, view-as-architecture, and publication-as-architecture overread; disciplines `CC-C30P-2`, `CC-C30P-3`, and `CC-C30P-4`. | Does not import 42010 terminology as FPF ontology; FPF still uses `A.22`, `C.30`, `C.30.ASV`, and named `C.30.*` patterns. |
| SEI "Documenting Software Architectures: Views and Beyond" practice line. | Reference and lineage source for documenting views for stakeholder use. | Disciplines the source, publication, and view split in worked cases and keeps view artifacts useful without making them the selected structure. | Does not make "view" a generic proof or decision record. |
| C4 model practice for developer-friendly architecture diagrams over context, container, component, and code views. | Practice anchor for diagram usefulness and diagram limits. | Disciplines the diagram, block, component, module, and layer examples: a diagram can be an entry or view publication, and unclear source labels are recovered through `C.30.STRAT` before architecture or structure assignment. | Does not make C4 levels, blocks, layers, or containers FPF structure kinds or mandatory architecture views. |
| arc42 architecture documentation template practice. | Practice and reference source for architecture communication, constraints, decisions, and cross-cutting concerns. | Disciplines the distinction between documentation template sections, source publications, decisions, architecture claims, and conditional architecture-description use. | Does not let a documentation section, template heading, or dashboard become architecture authority by label. |
| ADR and MADR architecture decision record practice. | Practice and lineage source for decision-record separation; evidence about template choice does not by itself establish an FPF decision relation. | Disciplines the ADR worked case and the assignment to `C.2.P`, `C.11`, `A.15`, or `C.30`: an ADR may record or motivate a decision; it is not automatically the architecture decision, work execution, or architecture itself. | Does not import ADR label as gate, release, proof, or FPF decision authority. |

These distinctions block diagram-as-architecture, graph-as-proof, view-as-structure-kind, publication-as-claim, and ADR-as-decision overreads. This use does not import any external standard as FPF ontology.

### C.30.P:8 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-C30P-1` | The repaired span makes its object, claim and useful conclusion recoverable. Name the subject pattern for any unresolved substantive question and state a blocked interpretation only when it changes the use; a separate repair record is optional. |
| `CC-C30P-2` | A diagram, model, graph, dashboard, ADR, source, publication, view, face, `PublicationUnit`, file, carrier, or rendering is not treated as architecture or structure by appearance. |
| `CC-C30P-3` | Direct `A.22`, `C.30`, `C.30.ASV`, or named `C.30.*` use applies the subject pattern directly when the selected-structure claim being made, architecture relation, architecture-description use, structural-view use, or named C.30 subcase is already recoverable. |
| `CC-C30P-4` | Source-use, currentness, and publication-to-carrier relation recovery uses `C.2.P` before architecture or structure claim use only while the relevant distinction remains hidden; an already recovered claim goes directly to its subject pattern. |
| `CC-C30P-5` | Function-like, relation-like, mathematical-lens, characteristic and scale, quality, evidence, assurance, gate, work, decision, causal-use, release, and method claims are assigned to their subject patterns. |
| `CC-C30P-6` | The repair does not mint `U.Architecture`, `ArchitectureStructure`, a generic architecture head, or mandatory architecture-repair record. |
| `CC-C30P-8` | The repaired wording preserves one useful admissible reader use; type-correct but inert architecture wording is not recovered by value. |

### C.30.P:9 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Diagram-as-architecture | A diagram, graph, dashboard, ADR, or generated view is said to be the architecture. | Recover publication, carrier, view, or source-use relation and then apply `C.30` or `C.30.ASV` only if the architecture claim or structural-view claim is being made. |
| Architecture-as-proof | Architecture wording carries evidence, assurance, causal proof, gate passage, release permission, or decision authority. | Apply `A.10`, `B.3`, `C.28`, `A.20`, `A.21`, `C.11`, release, or the pattern governing the claim being made. |
| Function-as-default-architecture | Any function, interface, module behavior, or source label such as block is treated as architecture. | Use `C.30.STRAT` for source-label recovery where needed, then `A.6.F`, `C.30.ASV` functional-structure, `C.30.TFS-REL` transformation-flow structure relation, `A.6.M` module-relation repair, or quality pattern governing the claim. |
| Score-as-architecture | A score, metric, benchmark, or quality coordinate is used as architecture adequacy. | Apply `C.16.P` and the measurement named by value, characteristic-space, Q-bundle, pattern-quality, gate, or benchmark pattern. |
| Viewpoint-as-structure-kind | A viewpoint label is used as if it selected structure kind. | Use `C.30.ASV`; recover structure kind and viewpoint separately. |

### C.30.P:10 - Related patterns

- `E.10` catches architecture or structure wording and selects this pattern only when the selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or named C.30 subcase is hidden.
- `E.10.ARCH` defines the shared wording-use recovery order and applicability row.
- `A.22` governs selected structure and structural views as structure.
- `C.30` governs `ArchitectureRelation`, bounded `ArchitectureClaim` and the initial architecture-description question.
- `C.30.AD` governs architecture-description identity, correspondence and use. The description retains its own EntityOfConcern; it need not itself be the subject of another description.
- `C.30.ASV` governs architecture structural views.
- `C.30.STRAT` recovers unclear stratification or source-label meaning before C.30.P assigns the recovered architecture or structure portion.
- Named `C.30.*` patterns define or constrain their own structure adequacy or view adequacy questions.
- `C.2.P` recovers source, publication, view, face, `PublicationUnit`, carrier, and source-use disposition.
- `A.6.P` repairs relation construction; `A.6.F` repairs function and functionality wording; `A.6.M` repairs module-relation and interface-specification wording.
- `C.16.P` repairs unclear characteristic-and-scale wording, and `C.16.Q` repairs unclear quality-term or evaluative characterization wording. Already recoverable claims use their subject rules directly.
- `C.29` governs mathematical-lens use and does not become architecture by analogy.

### C.30.P:End
