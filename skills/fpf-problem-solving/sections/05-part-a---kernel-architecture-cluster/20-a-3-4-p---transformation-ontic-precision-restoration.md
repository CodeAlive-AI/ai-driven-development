## A.3.4.P - Transformation Ontic Precision Restoration

> **Type:** A.3.4 precision-restoration child pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

**Plain-name.** Transformation wording repair.

**Intent.** Restore precision when wording about a situation of change hides whether the current FPF object is one bounded `U.Transformation`, its exact changed referent, a system claimed to act through an exact performed-work attribution or another direct actor-side relation, a distinct influence source kept under its exact kind and current relation, a method, method description, mechanism, work plan, dated work, functioning relation, transformation-flow structure, mathematical description, dynamics episteme, temporal aspect, evidence relation, publication relation, gate, decision, result, or source label.

**Use this when.** Use `A.3.4.P` when source or FPF-governed wording such as "pipeline", "dataflow", "flow", "network", "circuit", "path", "slice", "workflow", "process", "operation", "transformation", or "change" seems to name the thing under concern, but the text has not yet recovered what kind of FPF value is actually current.

**First useful restoration output.** Fill a compact `TransformationWordingRepair` note: encountered wording, working concern, exact recovered EntityOfConcern, actual-transformation basis or non-transformation disposition, any acting-system claim with its exact governor or unresolved disposition, every influence source's exact kind and current relation, exact neighboring claims, retained use, blocked overread, and remaining reader use. Then rewrite only the wording that depends on the recovered objects.

**What goes wrong if missed.** The text silently creates a local ontology from a convenient source label: "process" becomes method in one paragraph, dated work in another, and transformation-flow structure in a third; "path" becomes evidence sufficiency, assurance, gate passage, deontic permission, work authorization, or release authorization; "function" becomes behavior, bearer, mathematical function, and software routine at once.

**What this buys.** The reader gets one small restoration use that keeps bounded transformations, compound transformation-flow structures, formal descriptions, methods, mechanisms, work, evidence, publications, and functional structures in their governing places before any wording is changed.

**Not this pattern when.**

- If one bounded transformation is already identified and only its ordinary use continues, apply `A.3.4` directly.
- If the current claim is already a selected transformation-flow structure, use `E.18`.
- If the current claim is a graph, morphism, category, algebra, path, circuit expression, network expression, or other mathematical description, use `E.18.2` and `C.29`.
- If the current claim is only a semantic way of doing, method description, mechanism, work plan, dated work, evidence relation, publication relation, gate, decision, assurance, result, or temporal claim, use the direct governing pattern.
- If the word is quoted source wording with no FPF-governed use, keep it quote-only.

### A.3.4.P:1 - Problem frame

People talk about change with convenient source labels. A manufacturing line has a process, an ML paper has an architecture pipeline, a refrigerator has a cycle, a plant model has a flow graph, a team has a workflow, and a proof has a construction path. Those labels often help recognition, but they do not say which FPF object is current.

The recurring defect is a second ontology by convenience. The same text may treat "process" as method, work occurrence, transformation-flow structure, mechanism, result evidence, and publication diagram. A graph path may become an action route. A network label may become a durable head beside `TransformationFlowStructure`. A function word may collapse functioning, mathematical function, software routine, module allocation, a system merely named as actor, and a differently typed influence source whose direct relation has not been recovered.

This pattern restores the current `U.Transformation` ontic first, then assigns linked values to their governing patterns. It is not a word ban and not a synonym table.

### A.3.4.P:2 - Problem

Without this repair:

1. **Source label becomes kind.** "Pipeline", "workflow", "network", "circuit", or "process" is treated as the recovered FPF kind.
2. **Selected structure becomes one actual transformation.** A flow, path, network, or circuit expression is treated as one actual `U.Transformation` or as proof of transformation composition without the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis. Identifying one occurrence at the resolution needed by the current use establishes neither finer transformation parts nor partlessness.
3. **Method, mechanism, and work collapse.** A method description, law-governed mechanism, work plan, dated work, or source diagram is selected by vocabulary rather than by current claim.
4. **Functional wording overreaches.** A system, module, port, interface, signature, or function label is treated as the transformation or as proof of functioning.
5. **Mathematical expression becomes world-side ontology.** A graph, morphism, algebra, category, path, network, or circuit expression is treated as the project-world change.
6. **Description or evidence becomes transformation.** A publication, dashboard, source span, proof, or evidence path is treated as the changed object or the change itself.

### A.3.4.P:3 - Forces

| Force | Tension |
| --- | --- |
| Recognition and precision | Source labels help readers recognize a change situation, but FPF use needs a recovered kind, subject-side occurrence basis, exact relation, and governing pattern. |
| One actual transformation and selected flow structure | `U.Transformation` identifies one independently grounded actual bounded change and establishes neither transformation parthood nor partlessness at the current resolution. `TransformationFlowStructure` positions, relates, or locates transformation loci and adjacent governed values; common structure membership establishes no transformation composition. |
| Acting system and influence source | A role assignment alone does not prove performance, and generic transformation participation does not prove action. Performed-work attribution needs one exact dated Work occurrence admitted under `U.Work`, its direct `performedBy` relation to the covering `U.RoleAssignment`, and any separately governed work-to-change relation needed by the claim; a non-work actor needs another exact direct actor-side governor. Every influence source keeps its own kind and exact relation. |
| Formal and project-world change | A formal construction may be a transformation over a formal object, or it may be a mathematical description of project-world structure; the current object decides. |
| Repair and readability | The repair must recover enough ontology for safe use without turning every ordinary sentence into a table. |

### A.3.4.P:4 - Solution

Restore the change situation in this order.

1. **Name the working concern.** State what the text is trying to do: identify a change, describe a flow, choose a method, claim evidence, compare architectures, describe functioning, or use a publication.
2. **Test for one actual `U.Transformation`.** Recover the exact changed referent; exact temporal extent or exact ordering boundary in a declared formal substrate; boundary conditions; actual characteristic-state and obtaining direct-relation facts before, during, and after that boundary; and the continuity or reidentification rule that makes this one occurrence at the resolution required by the current use. Possible, intended, planned, modelled, predicted, or merely asserted change remains claim content and identifies no actual transformation until this subject-side basis obtains.
3. **Separate an acting-system claim from influence.** For performed work, recover one exact dated Work occurrence admitted under `U.Work`, the exact covering `U.RoleAssignment`, and direct `performedBy(WorkOccurrenceSlot, RoleAssignmentSlot)`; then recover separately the realization, causal, production, or other exact work-to-change relation required by the current use. Role assignment alone and generic transformation participation prove no action. For a non-work functional or physical actor-side claim, recover the exact system and the participant, operation-application, functioning, causal, or other direct actor-side relation supplied by its governor; otherwise leave the actor claim unresolved. Each manufacturing organization, certification organization, design organization, toolchain, communication system, selected structure, method, method family, or other possible influence source first keeps its exact kind—a method or method family is not a holon by label—and receives only the exact architecture, work, communication, constraint, or candidate-synthesis relation current for the claim.
4. **Test neighboring claims.** Decide whether the wording points to a method, method description, mechanism, work plan, dated work, functioning relation, transformation-flow structure, mathematical description, dynamics episteme, temporal aspect, evidence, source, publication, gate, decision, assurance, result, refresh, reopen relation, or another direct subject claim.
5. **Use the exact governing relation for each neighboring value.** A neighboring object keeps its own kind and governor; state its current relation to the transformation, changed referent, work, architecture candidate, or receiving use instead of placing it inside a transformation record.
6. **Rewrite only after kind and relation recovery.** Keep ordinary wording when it is not FPF-governed, write quote-only source wording when no current use is admitted, or rewrite into the recovered FPF kind and exact relation named by value.
7. **Leave one reader use.** The repaired text must say what the reader may do now: use `A.3.4`, use `E.18`, use `C.29`, use a method, work, mechanism, architecture, or evidence pattern, keep a quote-only cue, or block the stronger claim.

#### A.3.4.P:4.1 - TransformationWordingRepair note

Use this note only when wording is doing FPF-governed work.

```text
TransformationWordingRepair:
  EncounteredWording:
  WorkingConcern:
  RecoveredEntityOfConcern:
  ActualTransformationDisposition:
  TransformationOccurrenceBasis:
  ActingSystemDisposition:
  ArchitectureInfluenceDisposition:
  NeighboringClaimAndExactRelation:
  GoverningPattern:
  RetainedUse:
  BlockedOverread:
  RemainingReaderUse:
```

`ActualTransformationDisposition` is one of: actual bounded transformation recovered, not a transformation, not recovered, not current for this claim, quote-only source wording, or blocking missing value.

`TransformationWordingRepair` is a temporary wording-use restoration aid. Its retained output is the wording to keep or rewrite, the blocked overread, and the next governing-pattern application. `ActingSystemDisposition` and `ArchitectureInfluenceDisposition` are temporary note fields, not FPF kinds or universal relations. An actual transformation occurrence is grounded only through its subject-side occurrence basis.

For performed work, an acting-system claim needs one exact dated Work occurrence admitted under `U.Work`, the exact covering `U.RoleAssignment`, direct `performedBy(WorkOccurrenceSlot, RoleAssignmentSlot)`, and the separately governed realization, causal, production, or other work-to-change relation required by the use. For a non-work actor-side claim, use an exact participant, operation-application, functioning, causal, or other direct relation supplied by its governor. If no such relation is recoverable, keep the actor claim unresolved. Every influence source retains its exact kind and only its current architecture, work, communication, constraint, or candidate-synthesis relation; influence establishes no acting fact by itself.

If an episteme asserts possible, intended, planned, modelled, predicted, or actual change, identify that episteme separately through C.2.1 when the assertion is current. Empirical grounding remains optional and, when current, uses its own exact relation; neither the assertion nor its grounding relation substitutes for the actual transformation basis. Project records, gate decisions, work plans, and work occurrences are created only by their direct governing patterns.

#### A.3.4.P:4.2 - Direct governing-pattern selection

| If recovery shows... | Use this governing pattern | Keep this boundary |
| --- | --- | --- |
| one actual bounded change under conditions | `A.3.4` | A source label identifies no transformation until the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis are recoverable. |
| selected structure over transformation loci and adjacent governed values | `E.18` | `TransformationFlowStructure` positions, relates, or locates those loci and values. Selection or common structure membership establishes neither an actual transformation occurrence nor transformation composition, parthood, or partlessness. |
| mathematical expression over a selected structure or formal object | `E.18.2`, `C.29`, `A.6.0`, or the direct formal pattern | A graph, morphism, category, algebra, path, network expression, or circuit expression is not project-world work by notation. |
| semantic way of doing | `A.3.1` | Method is not dated work, mechanism, evidence, or transformation occurrence by label. |
| episteme describing a way of doing | `A.3.2` | Code, protocol, solver model, proof script, process model, or diagram may describe a method without being the method or the work. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, or mechanism-governing-definition assignment | `A.6.1` and `E.20` | Mechanism is not selected by a prestigious "algorithm", "process", or "mechanism" word. |
| planned or dated work | `A.15.2` or `A.15.1` | Plan and work occurrence are not method, method description, transformation-flow structure, or evidence by appearance. |
| pattern-use recommendation, work-entry readiness, language-state move, architecture candidate use, or call-planning next action | `E.10.MOVE` first, then `E.11.PUR`, `A.15.5`, `A.16`, `C.30`, `C.24`, or the direct governing pattern | Move-like wording is not transformation wording unless a bounded `U.Transformation` or selected `TransformationFlowStructure` is actually current. |
| function-like wording inside a change situation | `A.3.4.P` only to distinguish the actual transformation, selected `TransformationFlowStructure`, a system claimed to act under an exact actor-side governor, a differently typed influence source under its exact relation, boundary binding, or `FunctioningRef?`; use `A.6.F` for detailed function-kind discrimination | A function word, role assignment, generic participant fact, module allocation, architecture locus, toolchain, or organization establishes neither the actual transformation nor action by label. |
| state-space and transition-law episteme | `A.3.3` | Dynamics can model possible or claimed change; it is not the transformation itself. |
| time window, cadence, duration, latency, freshness, currentness, trajectory, inertia, or effort | `C.27.TA`; use `C.27` for temporal-claim adequacy | Temporal aspect is not the whole transformation and temporal-claim adequacy is not positive temporal subject matter. |
| evidence, provenance, source, publication, dashboard, view, gate, decision, assurance, result, or release claim | the direct governing evidence, source, publication, gate, decision, assurance, result, or release pattern | A visible record or path does not establish evidence sufficiency, assurance, gate passage, deontic permission, work authorization, release authorization, performed work, or acceptance by itself. |

#### A.3.4.P:4.3 - Common source-label settlements

| Source label | First recovery question | Typical admissible outcomes |
| --- | --- | --- |
| `pipeline` or `dataflow` | Is the current object one transformation, a compound transformation-flow structure, a method description, a work plan, or a publication diagram? | `A.3.4`, `E.18`, `A.3.2`, `A.15.2`, `C.2.P.DR`, or quote-only source wording. |
| `flow` | Is flow the selected structure, a mathematical expression, an actual material, energy, signal, or information flow, or an ordinary source label? | `E.18`, `E.18.2`, `C.29`, direct subject pattern, or quote-only source wording. |
| `network` or `circuit` | Is it a structure form, topology label, mathematical-expression family, functional structure, architecture-selected structure, or subject-domain system? | `E.18`, `E.18.2`, `C.29`, `C.30.ASV`, `A.6.F`, or direct subject pattern. |
| `path` or `slice` | Is it graph path, `PathSlice`, evidence path, carrier path, mathematical path, source quote, or action-route metaphor? | `E.18`, `A.10`, `C.29`, `C.2.P.DR`, carrier wording, source wording, or blocked overread. |
| `workflow` or `process` | Is it method, method description, work plan, dated work, transformation-flow structure, mechanism, or source label? | `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `E.18`, `A.6.1` with `E.20`, or quote-only source wording. |
| `algorithm`, `program`, `solver`, or `proof` | Is it method, method description, formal substrate, mathematical lens, mechanism, work occurrence, evidence, or proof publication? | `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1` with `E.20`, `A.15.1`, `A.10`, `C.2.1`, or the governing publication pattern. |
| `function`, `functional`, or `functioning` | Is the current claim about an actual `U.Transformation`, selected `TransformationFlowStructure`, a performed-work or non-work actor under an exact direct governor, a separately typed influence source, boundary binding, or `FunctioningRef?`; or is the word asking for function-kind discrimination? | Use `A.3.4` or `E.18` for transformation-side recovery; use one exact Work occurrence admitted under `U.Work` plus `performedBy` and a separate work-to-change relation for performed work, or another exact participant, operation-application, functioning, causal, or direct actor-side relation; keep every influence source under its own kind and exact relation; use `A.6.F` for function-kind discrimination. |

#### A.3.4.P:4.4 - Functional change-situation settlement

When change-situation wording includes `function`, `functional`, `functioning`, `transforms`, or `implements`, use this pattern only to recover the exact current claims:

- Is one actual bounded `U.Transformation` established by changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification?
- Is a selected `TransformationFlowStructure` current without being treated as the acting system or the change occurrence?
- Is performed work being attributed to a system? Recover the exact dated Work occurrence admitted under `U.Work`, exact covering `U.RoleAssignment`, and direct `performedBy(WorkOccurrenceSlot, RoleAssignmentSlot)`. Then state separately the realization, causal, production, or other exact work-to-change relation required by the claim. A role assignment, work record, common timestamp, or generic transformation-participant fact does not prove performance.
- Is a non-work functional or physical actor-side claim current? Recover the exact system and the participant, operation-application, functioning, causal, or other direct actor-side relation supplied by its governor. A changed referent, resource, port-bound object, module, or other participant is not an actor merely because it participates. If no actor-side governor is recoverable, leave the actor claim unresolved.
- Is a distinct influence source current? First recover its exact kind. A manufacturing, certification, or design organization may be a system under its direct governor; a toolchain or communication system needs its own admitted kind; a selected structure remains a structure; and a method or method family is not a holon by label. State only the exact architecture, work, communication, constraint, or candidate-synthesis relation current for that value. Influence alone establishes no role, work, actor status, or transformation participation.
- Are exact participant, port, operation-application, relation-signature, or functioning relations current at the boundary? Use their direct governors; do not turn them into generic transformation inputs or outputs.

Do not introduce a `TransformerHolon` kind, a generic transformer role, or a universal architecture-influence relation to bridge these claims. After recovery, apply `A.6.F` when the question is which function-like kind or relation is being claimed. `A.3.4.P` selects the direct governor; it does not infer mathematical function, software routine, capability, quality, work, method, architecture allocation, evidence, assurance, gate, or decision from functional wording.

#### A.3.4.P:4.5 - Description, publication, and evidence boundary

A diagram, model, dashboard, report, source span, proof, graph, or publication may describe, assert, evidence, or help compare a transformation. It is not the transformation and does not supply its subject-side occurrence basis. If the description, assertion, or publication is current, use the episteme, publication, source, or declarative-representation pattern; C.2.1 empirical grounding remains an optional separate relation when the use requires it. If the actual transformation is current, keep every description, assertion, publication, and evidence use as an exact neighboring claim.

### A.3.4.P:5 - Archetypal Grounding

#### A.3.4.P:5.1 - Refrigerator functional diagram

Source wording says: "The refrigeration circuit moves heat through the cycle."

Repair: recover whether the current claim is a refrigerator subsystem transformation, a `TransformationFlowStructure` over compressor, condenser, expansion, and evaporator transformations, a thermodynamic mechanism, a functional architecture view, or a schematic publication. The circuit label may stay as ordinary domain wording, but FPF use names the selected structure, mechanism, or publication relation.

#### A.3.4.P:5.2 - Neural-network block

Source wording says: "The attention block transforms activations in the model pipeline."

Repair: the block may be an architecture locus or module allocation, but that fact alone establishes no actor. If dated inference work is claimed, recover its exact Work occurrence admitted under `U.Work`, covering `U.RoleAssignment`, direct `performedBy`, and the separately governed work-to-activation relation required by the use. If a non-work block action is claimed, recover the exact operation-application, functioning, causal, or other direct actor-side relation; otherwise leave action unresolved. A design organization, method or method family, toolchain, or communication system that shaped the block first keeps its exact kind and then only its exact architecture, work, communication, constraint, or candidate-synthesis relation. Activation and tensor-shape claims use exact participant, port, operation-application, or signature relations; attention may be a method description or mathematical lens; the pipeline may be a transformation-flow structure. Benchmarks or ablations are evidence or evaluation relations only when their governing patterns are current.

#### A.3.4.P:5.3 - CRISPR editing workflow

Source wording says: "The guide-selection workflow changes the target gene."

Repair: the target-gene edit is only a candidate `U.Transformation` until the exact biological referent, edit boundary, boundary conditions, actual sequence and direct-relation facts, and reidentification rule establish one occurrence. Guide selection may be method, method description, work plan, evidence-facing table, or performed lab work according to the current claim. A table rank or workflow diagram establishes neither actual edit, gate passage, deontic permission, work authorization, release authorization, nor performed lab work.

#### A.3.4.P:5.4 - Evidence path near a plant change

Source wording says: "The evidence path lets the valve-change flow proceed."

Repair: an evidence path may be a legitimate `A.10` provenance relation for a named claim. The valve change still needs its exact changed referent, boundary, boundary conditions, actual subject facts, and continuity or reidentification basis; work plan, dated work, gate, assurance, result, and receiving use remain exact neighboring relations when current. The path establishes no work authorization, release authorization, gate passage, performed work, or actual transformation by shape or name.

#### A.3.4.P:5.5 - Filled minimal repair note

```text
TransformationWordingRepair:
  EncounteredWording: "the refrigeration circuit moves heat through the cycle"
  WorkingConcern: recover whether the sentence is about one bounded heat-transfer change, a selected compound transformation-flow structure, a thermodynamic mechanism, a functional architecture view, or a schematic publication.
  RecoveredEntityOfConcern: `RefrigeratorHeatTransferFlowStructure-1`, the exact selected `TransformationFlowStructure` over the compressor, condenser, expansion, and evaporator transformation loci.
  ActualTransformationDisposition: no actual bounded transformation is recovered; `RefrigeratorHeatTransferFlowStructure-1` is the exact current object, and its selection establishes neither transformation composition nor partlessness.
  TransformationOccurrenceBasis: no component transformation occurrence is asserted; each remains unresolved until its exact changed referent, boundary, boundary conditions, actual subject facts, and continuity or reidentification basis are recovered.
  ActingSystemDisposition: unresolved and not asserted; the circuit wording supplies no exact dated Work occurrence admitted under `U.Work`, `performedBy` relation, work-to-change relation, or non-work direct actor-side relation.
  ArchitectureInfluenceDisposition: no influence claim is current and no influence source is selected; any later source must first keep its exact kind and then receive only its exact architecture, work, communication, constraint, or candidate-synthesis relation.
  NeighboringClaimAndExactRelation: the four named transformation loci are positions in `RefrigeratorHeatTransferFlowStructure-1`; their exact transformation occurrences and structure-membership relations remain to be recovered under `E.18` and `A.3.4`. Thermodynamic-law material, functional view, and schematic publication remain unselected neighboring candidates.
  GoverningPattern: `E.18` governs `RefrigeratorHeatTransferFlowStructure-1`; `A.3.4` governs each component transformation only after its occurrence basis is recovered; mechanism, architecture-view, and publication patterns open only if one of those candidate objects becomes current.
  RetainedUse: "circuit" may remain ordinary domain wording for `RefrigeratorHeatTransferFlowStructure-1` after that exact selected structure is named.
  BlockedOverread: `RefrigeratorHeatTransferFlowStructure-1` is not proof of functioning, an actor, dated work, a gate decision, one actual transformation, or transformation composition; its component loci do not establish component occurrences, parthood, or partlessness.
  RemainingReaderUse: use `E.18` for `RefrigeratorHeatTransferFlowStructure-1`; open `A.3.4` only for a component whose exact occurrence basis is recovered, or the direct mechanism, architecture-view, or publication pattern only when that separate object becomes current.
```

### A.3.4.P:6 - Bias-Annotation

Lenses tested: **Onto**, **Arch**, **Prag**, **Epist**, **Gov**.

This pattern intentionally biases toward kind recovery before wording repair. It resists:

- **source-label ontology:** familiar labels such as pipeline, process, network, circuit, or workflow become FPF kinds;
- **graph or path overread:** graph path, evidence path, and carrier path become action route, evidence sufficiency, assurance, deontic permission, work authorization, release authorization, or work sequence;
- **function collapse:** functioning, functional element, module allocation, mathematical function, software routine, and everyday purpose collapse into one "function";
- **semio displacement:** descriptions and publications of transformations replace the transformation under concern;
- **neighboring-object fusion:** a method, mechanism, work occurrence, system, influence source, or evidence record is inferred from wording and then treated as the transformation, its actor, or a transformation participant; generic participation is also treated as action without exact `performedBy`, work-to-change, or other direct actor-side relation.

### A.3.4.P:7 - Conformance Checklist

| Check | Conformance statement |
| --- | --- |
| `CC-A34P-1` | The repair names the encountered wording and the working concern before selecting a replacement. |
| `CC-A34P-2` | If one actual bounded transformation is current, the repair names or blocks its exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis. |
| `CC-A34P-3` | Each neighboring object keeps its own kind and is connected only by an exact current relation to the transformation, changed referent, work, architecture candidate, or receiving use. |
| `CC-A34P-4` | `TransformationFlowStructure`, graph mathematical description, path mathematical description, and subject-domain network or circuit wording are kept distinct. The selected structure positions, relates, or locates transformation loci and adjacent governed values; selection or common membership establishes neither transformation composition, parthood, nor partlessness. |
| `CC-A34P-5` | Method, method description, mechanism, work plan, dated work, evidence, gate, decision, assurance, result, source, and publication claims remain with their governing patterns. |
| `CC-A34P-6` | Function-like wording closes here only after the actual transformation, performed-work attribution or other exact actor-side relation, every influence source's exact kind and relation, and exact boundary relations are distinguished; detailed function-kind discrimination remains governed by `A.6.F`. |
| `CC-A34P-7` | The repair leaves retained use, blocked overread, and remaining reader use by value. |
| `CC-A34P-8` | The repair order is explicit: `E.10` recognizes the wording, `A.3.4.P` restores the transformation ontic neighborhood, and neighboring patterns govern recovered objects and exact relations. |
| `CC-A34P-9` | A performed-work actor claim names one exact dated Work occurrence admitted under `U.Work`, the covering `U.RoleAssignment`, direct `performedBy`, and the separately governed work-to-change relation required by the use; a non-work actor claim names another exact direct actor-side relation. Role assignment or generic participation alone proves neither. |
| `CC-A34P-10` | Possible, intended, planned, modelled, predicted, and merely asserted change stays claim content; any C.2.1 empirical grounding is optional, separate, and not the actual occurrence basis. |

### A.3.4.P:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Cue word as ontology | "Pipeline", "process", "network", or "circuit" is treated as the FPF kind. | Recover the current object: `U.Transformation`, `TransformationFlowStructure`, mathematical description, method, work, publication, or direct subject pattern. |
| Replacement by smoother umbrella | "Process" is replaced with "flow" or "operation" without recovered kind. | Run the replacement through the same recovery. If the kind is still hidden, keep the row open. |
| Network head inflation | Frequent network or circuit wording becomes a peer durable head. | Use network or circuit as structure form, topology label, mathematical-expression family, domain label, or subject-domain system only when recovered by value. |
| Selected structure as transformation composition | Common membership in one flow, path, network, circuit, or pipeline is treated as a composite transformation, transformation-part relation, or proof of indivisibility. | Use `E.18` only to position, relate, or locate transformation loci and adjacent governed values. Ground every actual `U.Transformation` independently under `A.3.4`; common structure membership establishes neither composition, parthood, nor partlessness. |
| Workflow as performed work | A workflow diagram or process model is treated as dated work. | Use `A.3.2`, `E.18`, or `C.2.P.DR` for the description or structure; use `A.15.1` only for dated work. |
| Function as proof of behavior | A module, port, participant, role assignment, or "transformer" label is treated as proof of actual change or action. | Recover the actual transformation basis; for performed work, one exact Work occurrence admitted under `U.Work`, its covering `U.RoleAssignment`, direct `performedBy`, and the required separate work-to-change relation; otherwise the exact participant, operation-application, functioning, causal, or other direct actor-side relation. |
| Architecture influence as action | A manufacturing or certification organization, design organization, method or method family, toolchain, communication system, selected structure, or other value is called the actor because it constrained or enabled a candidate. | Recover the value's exact kind first, then only its exact architecture, work, communication, constraint, or candidate-synthesis relation. A method or method family is not a holon by label, the temporary influence-disposition field is no new relation, and influence alone proves no role, work, actor status, or transformation participation. |
| Publication as change | A diagram, proof, dashboard, or source span is treated as the changed object or change occurrence. | Use description, publication, evidence, or source-use pattern for the carrier and keep the transformation under `A.3.4`. |

### A.3.4.P:9 - Consequences

- FPF gains one reusable restoration pattern for language about change situations without making every subject pattern carry its own cue list.
- `A.3.4` becomes easier to use because source labels are tested against the exact subject-side transformation basis and then routed to exact neighboring relations.
- `E.18`, `E.18.2`, and `C.29` stay distinct: selected compound structure, mathematical expression, and mathematical-lens use do not collapse.
- Architecture, method, work, mechanism, function, evidence, publication, and temporal patterns can point to the transformation ontic without becoming transformation patterns.
- The cost is one small restoration note when wording is FPF-governed and hides several candidate kinds.
- Reopen this pattern at the smallest affected row when `A.3.4`, `E.18`, `E.18.2`, `C.29`, method, mechanism, work, function, temporal, evidence, publication, or architecture patterns change the governing kind boundary, or when FPF wording repair repeatedly finds a change-situation label that the current settlements cannot recover by value.

### A.3.4.P:10 - Rationale

The current transformation ontology gives FPF one compact way to speak about bounded actual change. That compactness only helps if wording repair returns common source labels to the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis. Otherwise source labels reappear as local mini-ontologies: a process ontology here, a graph ontology there, a function ontology elsewhere.

`A.3.4.P` is placed under `A.3.4` because the recurring repair is not about words in general. The repair starts from the `U.Transformation` ontic and asks whether the current use is an actual occurrence established on that basis, a performed-work actor claim grounded by one exact Work occurrence admitted under `U.Work`, `performedBy`, and its required work-to-change relation, a non-work actor claim under another exact direct actor-side governor, a differently typed influence source under its exact relation, a compound structure, a mathematical description, or another neighboring object connected by an exact current relation. `E.10` recognizes the wording-use problem; `E.10.ARCH:2.2` distributes direct governing, ontic-level restoration, and facet-level restoration; this pattern performs the ontic-level transformation restoration.

### A.3.4.P:11 - SoTA-Echoing

| Source family | Use of source | What changes here |
| --- | --- | --- |
| Current FPF `A.3.4` transformation ontic | Governing ontology source for bounded actual change under conditions. | This pattern tests wording against the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis. |
| Current FPF `E.18`, `E.18.2`, and `C.29` | Governing source line for compound transformation-flow structure and mathematical description. | Flow, path, network, circuit, graph, morphism, algebra, and category wording is separated into selected structure, mathematical expression, or lens use. |
| Current FPF `E.10` and `E.10.ARCH` precision-restoration architecture | Governing source line for recognition and distribution. | `E.10` recognizes change-situation wording; `E.10.ARCH:2.2` chooses direct governing, ontic-level restoration, or facet-level restoration; `A.3.4.P` restores only the transformation ontic neighborhood. |
| Current FPF `C.2.P.DR` and method, work, and mechanism patterns | Governing source line for declarative representation, method, mechanism, plan, work, and evidence separation. | Algorithm, workflow, process, proof, and path wording is recovered by exact object, direct relation, use relation, or claim kind rather than by programming-paradigm slogans. |
| Current FPF `A.6.F`, `A.6.M`, A.15.1/F.6, and architecture structural-view patterns | Governing source line for function-like, performer-attribution, module, interface, and structural-view claims. | `A.3.4.P` separates the actual transformation basis, exact performed-work attribution or other direct actor-side relation, every influence source's exact kind and relation, and boundary relations; the direct governing pattern decides each recovered claim. |

SoTA use is conservative: this pattern relies on the current FPF settlements already carried by `A.3.4`, `C.2.P.DR`, and the governing neighboring patterns; it contributes the reusable restoration use for transformation-situation wording.

### A.3.4.P:12 - Relations

- **Builds on:** `A.3.4`, `E.10`, `E.10.ARCH`, `E.24`, `A.6.5`, and `E.8`.
- **Coordinates with:** `E.18` for a selected structure that positions, relates, or locates transformation loci and adjacent governed values without establishing transformation composition, parthood, or partlessness; and with `E.18.2`, `C.29`, `A.3.1`, `A.3.2`, `A.3.3`, `A.6.0`, `A.6.1`, `E.20`, `A.15.2`, `A.15.1`, `A.6.F`, `A.6.M`, `C.30.ASV`, `C.27.TA`, `C.27`, `A.10`, `C.2.P.DR`, `C.2.1`, `E.17`, and direct gate, decision, assurance, result, source, publication, and release patterns when those claims are current.
- **Coordinates with:** `E.10.MOVE` when source wording about a move, next action, pattern-use recommendation, work-entry readiness, language-state transition, architecture candidate use, or call-planning next action is not actually transformation wording.
- **Selected by:** `E.10` recognition row for change-situation wording when FPF wording repair needs transformation-ontic precision restoration.
- **Specializes:** `A.3.4` for wording-use precision restoration around situations of change.

### A.3.4.P:End

