## C.30.P - Architecture and Structure Precision Restoration

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Architecture-structure wording repair.

**Intent.**
Recover architecture or structure wording whose live object is hidden before a reader applies `A.22`, `C.30`, `C.30.ASV`, or an exact `C.30.*` pattern.

This pattern does not mint `U.Architecture`, does not fuse architecture and structure into one kind, and does not replace architecture-description adequacy or structural-view adequacy. It repairs overloaded wording so the exact architecture, structure, description, view, publication, source, relation, characteristic, mathematical-lens, evidence, assurance, gate, work, decision, causal-use, release, or ordinary-prose use becomes recoverable.

**Builds on.** `E.10`, `E.10.ARCH`, `A.22`, `C.30`, `C.30.ASV`, `C.2.P`, `A.6.P`, `A.6.F`, `C.29`, `C.16.P`, `C.16`, `C.25`, `E.17`, and `E.8`.

**Coordinates with.** `C.30.TGA-FLOW-REL`, `C.30.LCA`, `C.30.ILC`, exact `C.30.*` structure/view patterns, `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, `C.28`, `A.15`, exact work/release/publication patterns, and `J.4`.

### C.30.P:0 - Use this when

Use this pattern when architecture or structure wording hides which object is live.

Typical triggers:

- `architecture`, `architecture description`, `architecture model`, `architecture diagram`, `architecture map`, `architecture dashboard`, `architecture score`;
- `structure`, `structural view`, `structural model`, `layer`, `module layout`, `block`, `component structure`, `interface structure`;
- `graph`, `flow`, `TGA graph`, `control sketch`, `LCA diagram`, `ADR`, `dashboard`, `benchmark`, `source`, or `view` being treated as architecture or structure by wording alone;
- a function, module, interface, signature, flow, control, quality, score, evidence, assurance, gate, work, decision, causal-use, or release claim being smuggled under architecture/structure wording.

**What goes wrong if missed.** A diagram becomes the architecture, a graph becomes proof, a view becomes the selected structure, a source document becomes an architecture decision, a score becomes architecture adequacy, or a function/module/interface claim becomes architecture by default.

**What this buys.** The reader can recover the live object, block the overread, and move to the exact pattern: selected structure under `A.22`, architecture description under `C.30`, architecture structural view under `C.30.ASV`, TGA-flow relation under `C.30.TGA-FLOW-REL`, control-structure view under `C.30.LCA`, mathematical lens under `C.29`, characteristic/scale repair under `C.16.P`, or a project-side evidence, assurance, gate, work, decision, causal-use, release, or publication pattern.

**First useful move.** Ask what object the architecture or structure wording is actually naming, then either apply the exact architecture/structure pattern directly or use one `architecture-structure repair note` to assign the claim elsewhere.


**Not this pattern when.**

- If the live object is already a selected structure, use `A.22` directly.
- If the live object is already `ArchitectureOf@Context` or `ArchitectureDescription@Context`, use `C.30` directly.
- If the live object is already an architecture structural view, use `C.30.ASV` or an exact `C.30.*` view pattern directly.
- If the live claim is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens adequacy, characteristic/scale construction, quality characterization, source-transfer, or relation construction, use the exact pattern for that claim after any architecture/structure wording is demoted or assigned.

### C.30.P:1 - Problem frame

Working engineers often say "architecture" or "structure" while pointing at a useful artifact: a diagram, model, graph, table, dashboard, ADR, code-agent relation graph, neural-network block diagram, benchmark result, or source document. Ordinary speech is acceptable; FPF-force-bearing prose is not.

The repair question is:

> What live object does the architecture or structure wording name, and which exact FPF pattern now carries the claim?

The live object may be:

- selected structure under `A.22`;
- an `ArchitectureOf@Context` claim or `ArchitectureDescription@Context` under `C.30`;
- an `ArchitectureStructuralView@Context` or exact `C.30.*` subcase;
- a publication, view, face, `PublicationUnit`, carrier, dashboard, ADR, source document, or source-return relation under `C.2.P` / `E.17`;
- a relation construction under `A.6.P`;
- a function-like carrier under `A.6.F`;
- a mathematical-lens adequacy claim under `C.29`;
- a characteristic, scale, score, coordinate, threshold, or quality-coordinate claim under `C.16.P` or `C.16`;
- a Q-bundle or quality-characterization claim under `C.16.Q`, `C.25`, or `E.21`;
- an evidence, assurance, gate, work, decision, causal-use, release, or method claim under its exact pattern;
- ordinary prose with no current FPF force.

### C.30.P:2 - Problem

How can FPF repair architecture or structure wording without:

- creating `U.Architecture`;
- treating architecture and structure as one fused kind;
- treating a description, view, diagram, graph, dashboard, source, ADR, model, or publication as the architecture itself;
- assigning all function, flow, module/interface, signature, control, evidence, assurance, gate, decision, work, quality, mathematical-lens, or source claims to architecture;

- duplicating first-stage repair lists inside `A.22`, `C.30`, `C.30.ASV`, and every exact `C.30.*` subpattern?

### C.30.P:3 - Forces

| Force | Tension |
| --- | --- |
| Ordinary engineering speech vs FPF kind recovery | Engineers need compact words such as architecture, structure, model, view, layer, graph, and module; FPF claims need recovered kind, relation, source-transfer posture, and admissible use. |
| Architecture description vs architecture itself | Descriptions and views are useful, but they can be overread as the selected structure or architecture claim. |
| Structure generality vs architecture specificity | `A.22` gives selected structure; `C.30` governs architecture descriptions over selected structures. The repair must not collapse them. |
| Small first move vs heavy record | Most wording cases need one repair note and exit, not a full architecture description. |
| Source and view usefulness vs project authority | A source, dashboard, graph, ADR, or view can guide architecture work without proving evidence, gate passage, decision authority, release permission, or work completion. |
| Cross-pattern consistency vs shadow registry | Architecture hosts should not carry duplicate trigger lists once `C.30.P` exists. |

### C.30.P:4 - Solution

Repair architecture/structure wording by producing an `architecture-structure repair note` or an equivalent local rewrite.

Minimum fields:

```text
ArchitectureOrStructureRepairNote:
  triggerSpan:
  boundedTextSpanOrPublicationUnit:
  encounteredObjectKind:
  candidateLiveObjects:
  selectedLiveObject:
  sourceOrPublicationStack?:
  relationClaimSlice?:
  functionCarrier?:
  structureKindOrArchitectureQuestion?:
  characteristicOrQualityClaimSlice?:
  mathematicalLensClaimSlice?:
  projectSideClaim?:
  exactReceivingPattern:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderMove:
  disposition:
```

Use the note only when the repair must remain inspectable. A direct local rewrite is enough when one sentence clearly names the live object and exact receiving pattern.

#### C.30.P:4.1 - Recovery sequence

1. **Capture the trigger.** Copy the architecture or structure wording and the sentence that uses it.
2. **Recover the encountered object.** Decide whether the text points to a selected structure, architecture claim, description, view, diagram, graph, model, dashboard, ADR, source document, carrier, publication, function, module/interface, signature, flow, control, score, quality term, evidence, gate, work, decision, release, or ordinary prose.
3. **Recover source/publication first when live.** If the wording relies on a source, publication, view, face, `PublicationUnit`, dashboard, ADR, file, carrier, or source-return relation, apply `C.2.P` for the source/current and publication stack before assigning the architecture or structure claim.
4. **Choose the architecture/structure object.**
   - selected structure -> `A.22`;
   - architecture claim or architecture description -> `C.30`;
   - architecture structural view -> `C.30.ASV`;
   - TGA-flow relation -> `C.30.TGA-FLOW-REL`;
   - control-structure view -> `C.30.LCA`;
   - cross-scope conflict/frustration triage -> `C.30.ILC`;
   - exact C.30 subcase -> that subpattern.
5. **Exit non-architecture claims.** If the sentence uses architecture wording to carry relation, function-like carrier, mathematical lens, characteristic/scale, quality, evidence, assurance, gate, work, decision, causal-use, release, or method force, send that force to the exact pattern and keep this pattern only for the architecture/structure wording repair.
6. **State admissible and non-admissible use.** Say what the reader may do with the repaired wording and what non-admissible adjacent interpretation is blocked.
7. **Return to the subject pattern.** Stop after the exact receiving pattern or ordinary-prose demotion is named.

### C.30.P:5 - Direct receiving-pattern exits

| Recovered object or claim force | Exit |
| --- | --- |
| selected structure, structural description, structure source-return | `A.22` |
| `ArchitectureOf@Context`, architecture description, architecture question card | `C.30` |
| architecture structural view, structure-kind view, hidden/lost structure | `C.30.ASV` |
| TGA graph, flow relation, transduction-flow architecture relation | `C.30.TGA-FLOW-REL` when architecture-flow description is live; otherwise `E.18` or exact TGA pattern |
| control structure view, LCA/control sketch | `C.30.LCA` when architecture control-structure view is live |
| cross-scope conflict or frustration triage | `C.30.ILC` when that exact question is live |
| source, publication, carrier, view, face, `PublicationUnit`, dashboard, ADR, documentation, source-return | `C.2.P`, `E.17`, `E.17.0`, or exact publication/source pattern |
| relation construction, basedness, support-like claim-force discrimination, endpoint compression, comparison | `A.6.P` or retained exact A.6 specialization |
| function, functional, functionality, effect, module/interface/signature carrier | `A.6.F`, `A.6.M`, A.6 signature-stack pattern, or retained exact module/interface/signature specialization |
| mathematical lens, mapping, model, similarity, preserved/lost structure as mathematical-lens adequacy | `C.29` |
| characteristic, scale, metric, score, indicator, threshold, architecture score, quality coordinate | `C.16.P`, then `C.16`, `A.19`, `C.25`, `E.21`, or exact receiving pattern |
| quality/evaluative characterization | `C.16.Q`, `C.25`, `E.21`, or exact characterization pattern |
| evidence, proof, validation, witness | `A.10` or exact evidence pattern |
| assurance, engineering justification, safety case | `B.3` or exact assurance pattern |
| gate, admissibility, release, approval | `A.20`, `A.21`, release/admissibility pattern, or exact gate pattern |
| work, method, implementation, operation, change execution | `A.15`, `A.15.4`, `U.Method`, `U.MethodDescription`, or exact work/method pattern |
| decision, choice, trade-off result | `C.11` or exact decision pattern |
| causal-use or intervention claim | `C.28` |

### C.30.P:5a - Refresh and reopen conditions

Reopen or narrow `C.30.P` when current pattern-language ecology changes the first architecture/structure entry:

- a new exact `C.30.*`, structural-view, TGA-flow, LCA/control, module/interface, mathematical-lens, characteristic, evidence, assurance, gate, work, decision, causal-use, release, or publication pattern can receive one row directly;
- current architecture-description, view, model, decision-record, or architecture-documentation practice changes one adopted distinction in `C.30.P:7`;
- `J.4` entry projection changes the first practical entry for hidden architecture/structure wording;
- a receiving pattern starts copying first-stage architecture/structure trigger lists that belong here;
- `C.30.P` begins to act as a registry of architecture topics rather than a wording-use repair pattern for hidden live objects.

The refresh action is to remove, narrow, or redirect the first-stage row. It is not to preserve old exits as history.

### C.30.P:6 - Worked cases


| Wording | Repair |
| --- | --- |
| "The architecture is the diagram." | The diagram is a publication, carrier, source cue, architecture description rendering, or structural view. It is not the architecture itself. Apply `C.2.P` if source/publication stack is live, then `C.30` or `C.30.ASV` only if the architecture claim or structural view is recovered. |
| "`ArchitectureOf@PlantOps` is defined over structures S1/S2 under context C." | Direct `C.30`; no `C.30.P` unless another hidden object remains. |
| "This ADR changed the architecture." | Recover whether the ADR is a publication, decision record, document with named source-basis role, architecture-description update, work plan, or ordinary source. Use `C.2.P`, `C.11`, `A.15`, or `C.30` as live. |
| "The TGA graph proves the architecture is safe." | TGA graph and architecture-flow relation are not proof or safety assurance. Use `E.18` / `C.30.TGA-FLOW-REL` for flow relation, `B.3` or evidence patterns for assurance, and `C.30` only for architecture-description claim. |
| "The architecture score improved." | Recover whether the sentence means architecture-description adequacy, characteristic/scale score, pattern-quality coordinate, Q-bundle, benchmark result, gate threshold, or ordinary comparison. Apply `C.16.P` before any score-based use. |
| "Functional architecture improved maintainability." | Recover function-like carrier via `A.6.F` when hidden, then architecture structural view via `C.30.ASV` or quality/maintainability via `C.16.P`, `C.16.Q`, `C.25`, or exact quality pattern. |
| "The module layer supports the architecture." | Recover whether layer is structure kind, `A.6.M` module/interface relation, publication view, A.6.6 basedness relation, evidence support, or ordinary help. Use `C.30.P` only to assign the architecture/structure wording, then `A.6.P`, `A.6.M`, or the retained exact A.6 specialization for the non-architecture claim. |

### C.30.P:7 - Reduced SoTA row

Current architecture-description, model, view, and decision-record practice treats architecture as distinct from architecture descriptions, models, views, viewpoints, diagrams, and decision records. FPF adopts that line only where it changes action guidance: examples, non-use boundaries, exact exits, source-return conditions, and conformance checks.

| Practice basis | Source posture | What `C.30.P` adopts or adapts | FPF import boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 on architecture descriptions, architecture viewpoints, model kinds, and conformance requirements. | Current-standard/reference support for architecture-description and viewpoint separation. | Disciplines direct exits to `C.30` and `C.30.ASV`; blocks diagram/model/view/publication-as-architecture overread; supports `CC-C30P-2`, `CC-C30P-3`, and `CC-C30P-4`. | Does not import 42010 terminology as FPF ontology; FPF still uses `A.22`, `C.30`, `C.30.ASV`, and exact `C.30.*` patterns. |
| SEI "Documenting Software Architectures: Views and Beyond" practice line. | Current reference and lineage support for documenting views for stakeholder use. | Disciplines the source/publication/view split in worked cases and keeps view artifacts useful without making them the selected structure. | Does not make "view" a generic proof or decision object. |
| C4 model current practice for developer-friendly architecture diagrams over context, container, component, and code views. | Current practice anchor for diagram usefulness and diagram limits. | Disciplines the diagram, block, component, module, and layer examples: a diagram can be an entry or view publication, not architecture by appearance. | Does not make C4 levels FPF structure kinds or mandatory architecture views. |
| arc42 current architecture documentation template practice. | Current practice/reference support for architecture communication, constraints, decisions, and cross-cutting concerns. | Disciplines the distinction between documentation template sections, source publications, decisions, and architecture-description claims. | Does not let a documentation section, template heading, or dashboard become architecture authority by label. |
| ADR/MADR architecture decision record practice. | Current practice and lineage support for decision-record separation; current empirical ADR work may refine template choice, but does not replace FPF decision ontology. | Disciplines the ADR worked case and exact exits to `C.2.P`, `C.11`, `A.15`, or `C.30`: an ADR may record or motivate a decision; it is not automatically the architecture decision, work execution, or architecture itself. | Does not import ADR status as gate, release, proof, or FPF decision authority. |

This row is live in this pattern because it blocks diagram-as-architecture, graph-as-proof, view-as-structure-kind, publication-as-claim, and ADR-as-decision overreads. It does not import any external standard as FPF ontology.
### C.30.P:8 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-C30P-1` | The repair names the trigger span, encountered object kind, selected live object, exact receiving pattern, admissible use, non-admissible use, and remaining reader move. |
| `CC-C30P-2` | A diagram, model, graph, dashboard, ADR, source, publication, view, face, `PublicationUnit`, file, carrier, or rendering is not treated as architecture or structure by appearance. |
| `CC-C30P-3` | Direct `A.22`, `C.30`, `C.30.ASV`, or exact `C.30.*` use applies the exact pattern directly when the live object is already recoverable. |
| `CC-C30P-4` | Source/current and publication/carrier stack recovery uses `C.2.P` before architecture or structure claim use when that stack is live. |
| `CC-C30P-5` | Function-like, relation-like, mathematical-lens, characteristic/scale, quality, evidence, assurance, gate, work, decision, causal-use, release, and method claims exit to exact receiving patterns. |
| `CC-C30P-6` | The repair does not mint `U.Architecture`, `ArchitectureStructure`, generic architecture object, or mandatory architecture-repair record. |
| `CC-C30P-7` | The subject architecture or structure pattern keeps its own invariant central and carries at most a thin pointer back to this pattern. |
| `CC-C30P-8` | The repaired wording preserves one useful admissible reader move; type-correct but inert architecture wording is not recovered by value. |

### C.30.P:9 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Diagram-as-architecture | A diagram, graph, dashboard, ADR, or generated view is said to be the architecture. | Recover publication/carrier/view/source role and then apply `C.30` or `C.30.ASV` only if the architecture claim or structural view is live. |
| Architecture-as-proof | Architecture wording carries evidence, assurance, causal proof, gate passage, release permission, or decision authority. | Exit to `A.10`, `B.3`, `C.28`, `A.20`, `A.21`, `C.11`, release, or exact pattern. |
| Function-as-default-architecture | Any function, functional block, interface, or module behavior is treated as architecture. | Use `A.6.F` and `C.30.ASV` functional-structure, TGA-flow, `A.6.M` module/interface, or exact quality pattern. |
| Score-as-architecture | A score, metric, benchmark, or quality coordinate is used as architecture adequacy. | Apply `C.16.P` and the exact measurement, characteristic-space, Q-bundle, pattern-quality, gate, or benchmark pattern. |
| Viewpoint-as-structure-kind | A viewpoint label is used as if it selected structure kind. | Use `C.30.ASV`; recover structure kind and viewpoint separately. |
| Repair registry duplication | `A.22`, `C.30`, `C.30.ASV`, or an exact `C.30.*` host copies architecture/structure first-stage repair lists. | Keep the subject invariant there and use one thin pointer to `C.30.P`. |

### C.30.P:10 - Related patterns

- `E.10` catches architecture/structure wording and selects this pattern only when the live object is hidden.
- `E.10.ARCH` defines the shared wording-use recovery order and applicability row.
- `A.22` governs selected structure and structural views as structure.
- `C.30` governs architecture descriptions and `ArchitectureOf@Context`.
- `C.30.ASV` governs architecture structural views.
- Exact `C.30.*` patterns govern their own structure/view adequacy questions.
- `C.2.P` recovers source, publication, view, face, `PublicationUnit`, carrier, and source-transfer use.
- `A.6.P` repairs relation construction; `A.6.F` repairs function-like carrier wording; `A.6.M` repairs module/interface relation wording.
- `C.16.P` and `C.16.Q` repair characteristic/scale and quality/evaluative characterization wording before score or quality use.
- `C.29` governs mathematical-lens adequacy and does not become architecture by analogy.

### C.30.P:End

