## A.3.4.P - Transformation Ontic Precision Restoration

> **Type:** A.3.4 precision-restoration child pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

**Plain-name.** Transformation wording repair.

**Intent.** Restore precision when wording about a situation of change hides whether the current FPF object is one bounded `U.Transformation`, a transformed object, a transformer-side system or holon, a method, method description, mechanism, work plan, dated work, functioning relation, transformation-flow structure, mathematical description, dynamics episteme, temporal aspect, evidence relation, publication relation, gate, decision, result, or source label.

**Use this when.** Use `A.3.4.P` when source or FPF-governed wording such as "pipeline", "dataflow", "flow", "network", "circuit", "path", "slice", "workflow", "process", "operation", "transformation", or "change" seems to name the thing under concern, but the text has not yet recovered what kind of FPF value is actually current.

**First useful restoration output.** Fill a compact `TransformationWordingRepair` note: encountered wording, working concern, recovered transformation or non-transformation object, recovered slot or neighboring pattern, retained use, blocked overread, and remaining reader use. Then rewrite only the wording that depends on the recovered kind.

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

The recurring defect is a second ontology by convenience. The same text may treat "process" as method, work occurrence, transformation-flow structure, mechanism, result evidence, and publication diagram. A graph path may become an action route. A network label may become a durable head beside `TransformationFlowStructure`. A function word may collapse functioning, mathematical function, software routine, module allocation, and the transformer-side system.

This pattern restores the current `U.Transformation` ontic first, then assigns linked values to their governing patterns. It is not a word ban and not a synonym table.

### A.3.4.P:2 - Problem

Without this repair:

1. **Source label becomes kind.** "Pipeline", "workflow", "network", "circuit", or "process" is treated as the recovered FPF kind.
2. **Compound structure becomes atomic change.** A flow, path, network, or circuit expression is treated as one `U.Transformation` without identity slots.
3. **Method, mechanism, and work collapse.** A method description, law-governed mechanism, work plan, dated work, or source diagram is selected by vocabulary rather than by current claim.
4. **Functional wording overreaches.** A system, module, port, interface, signature, or function label is treated as the transformation or as proof of functioning.
5. **Mathematical expression becomes world-side ontology.** A graph, morphism, algebra, category, path, network, or circuit expression is treated as the project-world change.
6. **Description or evidence becomes transformation.** A publication, dashboard, source span, proof, or evidence path is treated as the changed object or the change itself.

### A.3.4.P:3 - Forces

| Force | Tension |
| --- | --- |
| Recognition and precision | Source labels help readers recognize a change situation, but FPF use needs recovered kind, slot, and governing pattern. |
| Atomic and compound change | `U.Transformation` identifies one bounded change; `TransformationFlowStructure` composes or locates several transformations and adjacent loci. |
| System and behavior | A system, holon, module, or component may fill a transformer-side slot, while functioning remains transformation or transformation-flow behavior under conditions. |
| Formal and project-world change | A formal construction may be a transformation over a formal object, or it may be a mathematical description of project-world structure; the current object decides. |
| Repair and readability | The repair must recover enough ontology for safe use without turning every ordinary sentence into a table. |

### A.3.4.P:4 - Solution

Restore the change situation in this order.

1. **Name the working concern.** State what the text is trying to do: identify a change, describe a flow, choose a method, claim evidence, compare architectures, describe functioning, or use a publication.
2. **Test for `U.Transformation`.** If one bounded change is current, fill the `A.3.4` identity slots: transformed object, bounded context, initial condition, post-state or delta, transformation relation, boundary or admissibility condition, and temporal or ordering reference when relevant.
3. **Test for neighboring slots.** Decide whether the wording points to a transformer-side system or holon, method, method description, mechanism, work plan, dated work, functioning relation, transformation-flow structure, mathematical description, dynamics episteme, temporal aspect, evidence, source, publication, gate, decision, assurance, result, refresh, or reopen relation.
4. **Use the governing pattern for each filled value.** The slot may belong to the transformation ontic; the filler keeps its own kind and governing pattern.
5. **Rewrite only after kind recovery.** Keep ordinary wording when it is not FPF-governed, write quote-only source wording when no current use is admitted, or rewrite into the recovered FPF kind and relation named by value.
6. **Leave one reader use.** The repaired text must say what the reader may do now: use `A.3.4`, use `E.18`, use `C.29`, use a method, work, or mechanism pattern, keep a quote-only cue, or block the stronger claim.

#### A.3.4.P:4.1 - TransformationWordingRepair note

Use this note only when wording is doing FPF-governed work.

```text
TransformationWordingRepair:
  EncounteredWording:
  WorkingConcern:
  RecoveredEntityOfConcern:
  TransformationCoreDisposition:
  RecoveredSlotOrNeighboringValue:
  GoverningPattern:
  RetainedUse:
  BlockedOverread:
  RemainingReaderUse:
```

`TransformationCoreDisposition` is one of: bounded transformation recovered, not a transformation, not recovered, not current for this claim, quote-only source wording, or blocking missing value.

`TransformationWordingRepair` is a temporary wording-use restoration aid. Its retained output is the wording to keep or rewrite, the blocked overread, and the next governing-pattern application. Project records, evidence relations, gate decisions, work plans, and work occurrences are created only by the governing pattern selected in the note.

#### A.3.4.P:4.2 - Direct governing-pattern selection

| If recovery shows... | Use this governing pattern | Keep this boundary |
| --- | --- | --- |
| one bounded change under conditions | `A.3.4` | A source label does not identify the transformation until the identity slots are recoverable. |
| selected compound structure over transformations and adjacent loci | `E.18` | A flow, path, network, circuit, mesh, chain, loop, or pipeline is a structure form only when the selected structure is current. |
| mathematical expression over a selected structure or formal object | `E.18.2`, `C.29`, `A.6.0`, or the direct formal pattern | A graph, morphism, category, algebra, path, network expression, or circuit expression is not project-world work by notation. |
| semantic way of doing | `A.3.1` | Method is not dated work, mechanism, evidence, or transformation occurrence by label. |
| episteme describing a way of doing | `A.3.2` | Code, protocol, solver model, proof script, process model, or diagram may describe a method without being the method or the work. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, or mechanism-governing-definition assignment | `A.6.1` and `E.20` | Mechanism is not selected by a prestigious "algorithm", "process", or "mechanism" word. |
| planned or dated work | `A.15.2` or `A.15.1` | Plan and work occurrence are not method, method description, transformation-flow structure, or evidence by appearance. |
| pattern-use recommendation, work-entry readiness, language-state move, architecture candidate use, or call-planning next action | `E.10.MOVE` first, then `E.11.PUR`, `A.15.5`, `A.16`, `C.30`, `C.24`, or the direct governing pattern | Move-like wording is not transformation wording unless a bounded `U.Transformation` or selected `TransformationFlowStructure` is actually current. |
| function-like wording inside a change situation | `A.3.4.P` only to decide whether `U.Transformation`, `TransformationFlowStructure`, transformer-side filler, input boundary, output boundary, or `FunctioningRef?` is current; use `A.6.F` for detailed function-kind discrimination | A function word does not decide the transformation, bearer, mathematical function, software routine, module allocation, or architecture view by label. |
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
| `function`, `functional`, or `functioning` | Is the change-situation question about `U.Transformation`, `TransformationFlowStructure`, transformer-side filler, input boundary, output boundary, or `FunctioningRef?`; or is the word asking for function-kind discrimination? | Use `A.3.4` or `E.18` for the transformation-side recovery; use `A.6.F` for function-kind discrimination; use the direct governing pattern when another kind is already recovered. |

#### A.3.4.P:4.4 - Functional transformer settlement

When change-situation wording includes `function`, `functional`, or `functioning`, use this pattern only for the transformation-side recovery:

- Is one bounded `U.Transformation` current?
- Is a `TransformationFlowStructure` current?
- Is the current value a transformer-side filler such as a system, holon, module, bearer, allocation locus, interface, port, or signature-side value?
- Is the current value an input boundary, output boundary, or `FunctioningRef?` for transformation behavior under conditions?

After that recovery, apply `A.6.F` when the question is which function-like kind or relation is being claimed. `A.3.4.P` does not decide mathematical function, software routine, capability, quality, role, work, method, module allocation, evidence use, assurance use, gate use, or decision use except by selecting the governing pattern that owns the recovered value.

#### A.3.4.P:4.5 - Description, publication, and evidence boundary

A diagram, model, dashboard, report, source span, proof, graph, or publication may describe, evidence, or help compare a transformation. It is not the transformation. If the current object is the description or publication, use the episteme, publication, source, or declarative-representation pattern. If the current object is the transformation, keep the description or publication as a neighboring value and state the evidence use, description use, or comparison use separately.

### A.3.4.P:5 - Archetypal Grounding

#### A.3.4.P:5.1 - Refrigerator functional diagram

Source wording says: "The refrigeration circuit moves heat through the cycle."

Repair: recover whether the current claim is a refrigerator subsystem transformation, a `TransformationFlowStructure` over compressor, condenser, expansion, and evaporator transformations, a thermodynamic mechanism, a functional architecture view, or a schematic publication. The circuit label may stay as ordinary domain wording, but FPF use names the selected structure, mechanism, or publication relation.

#### A.3.4.P:5.2 - Neural-network block

Source wording says: "The attention block transforms activations in the model pipeline."

Repair: the block may be a system-like architecture locus or module allocation; activations and tensor shapes may fill input and output slots or signature slots; attention may be a method description or mathematical lens; the pipeline may be a transformation-flow structure. Benchmarks or ablations are evidence or result relations only when their governing patterns are current.

#### A.3.4.P:5.3 - CRISPR editing workflow

Source wording says: "The guide-selection workflow changes the target gene."

Repair: the target-gene edit is the candidate `U.Transformation`; guide selection may be method, method description, work plan, evidence-facing table, or performed lab work according to the current claim. A table rank or workflow diagram does not establish gate passage, deontic permission, work authorization, release authorization, or performed lab work for the edit.

#### A.3.4.P:5.4 - Evidence path near a plant change

Source wording says: "The evidence path lets the valve-change flow proceed."

Repair: an evidence path may be a legitimate `A.10` provenance relation for a named claim. The valve change still needs the transformation, work plan, dated work, gate, assurance, and result relations when those claims are current. The path does not establish work authorization, release authorization, gate passage, or performed work by shape or name.

#### A.3.4.P:5.5 - Filled minimal repair note

```text
TransformationWordingRepair:
  EncounteredWording: "the refrigeration circuit moves heat through the cycle"
  WorkingConcern: recover whether the sentence is about one bounded heat-transfer change, a compound transformation-flow structure, a thermodynamic mechanism, a functional architecture view, or a schematic publication.
  RecoveredEntityOfConcern: refrigerator heat-transfer behavior in the bounded cooling context.
  TransformationCoreDisposition: not one atomic transformation yet; compound transformation-flow structure is current.
  RecoveredSlotOrNeighboringValue: compressor, condenser, expansion, and evaporator transformations are candidate component transformations; thermodynamic laws are mechanism-governing material; the diagram is a publication only if the diagram itself is the current object.
  GoverningPattern: `E.18` for selected transformation-flow structure; `A.3.4` for each bounded component transformation when named; `C.30.ASV` for functional architecture view; direct publication pattern when the schematic publication is current.
  RetainedUse: "circuit" may stay as ordinary domain wording after the selected structure is named.
  BlockedOverread: the circuit label is not proof of functioning, not a gate decision, not dated work, and not one atomic transformation.
  RemainingReaderUse: name the selected transformation-flow structure and then open the direct governing pattern for the next claim being made.
```

### A.3.4.P:6 - Bias-Annotation

Lenses tested: **Onto**, **Arch**, **Prag**, **Epist**, **Gov**.

This pattern intentionally biases toward kind recovery before wording repair. It resists:

- **source-label ontology:** familiar labels such as pipeline, process, network, circuit, or workflow become FPF kinds;
- **graph or path overread:** graph path, evidence path, and carrier path become action route, evidence sufficiency, assurance, deontic permission, work authorization, release authorization, or work sequence;
- **function collapse:** functioning, functional element, module allocation, mathematical function, software routine, and everyday purpose collapse into one "function";
- **semio displacement:** descriptions and publications of transformations replace the transformation under concern;
- **slot-filler fusion:** a method, mechanism, work occurrence, system, or evidence record fills a transformation slot and is then treated as the whole transformation.

### A.3.4.P:7 - Conformance Checklist

| Check | Conformance statement |
| --- | --- |
| `CC-A34P-1` | The repair names the encountered wording and the working concern before selecting a replacement. |
| `CC-A34P-2` | If one bounded transformation is current, the repair names or blocks the `A.3.4` identity slots rather than relying on the source label. |
| `CC-A34P-3` | If a neighboring slot or value is current, the repair names the governing pattern for that filler and does not make the filler a second transformation ontology. |
| `CC-A34P-4` | `TransformationFlowStructure`, graph mathematical description, path mathematical description, and subject-domain network or circuit wording are kept distinct. |
| `CC-A34P-5` | Method, method description, mechanism, work plan, dated work, evidence, gate, decision, assurance, result, source, and publication claims remain with their governing patterns. |
| `CC-A34P-6` | Function-like wording closes here only when the transformation-side value is recovered; detailed function-kind discrimination remains governed by `A.6.F`. |
| `CC-A34P-7` | The repair leaves retained use, blocked overread, and remaining reader use by value. |
| `CC-A34P-8` | The repair order is explicit: `E.10` recognizes the wording, `A.3.4.P` restores the transformation ontic neighborhood, and neighboring patterns govern recovered fillers or facets. |

### A.3.4.P:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Cue word as ontology | "Pipeline", "process", "network", or "circuit" is treated as the FPF kind. | Recover the current object: `U.Transformation`, `TransformationFlowStructure`, mathematical description, method, work, publication, or direct subject pattern. |
| Replacement by smoother umbrella | "Process" is replaced with "flow" or "operation" without recovered kind. | Run the replacement through the same recovery. If the kind is still hidden, keep the row open. |
| Network head inflation | Frequent network or circuit wording becomes a peer durable head. | Use network or circuit as structure form, topology label, mathematical-expression family, domain label, or subject-domain system only when recovered by value. |
| Workflow as performed work | A workflow diagram or process model is treated as dated work. | Use `A.3.2`, `E.18`, or `C.2.P.DR` for the description or structure; use `A.15.1` only for dated work. |
| Function as proof of behavior | A module or port is said to have a function and therefore the transformation is accepted. | Recover bounded transformation, transformer-side filler, input and output boundary or signature boundary, functioning relation, and evidence or result relation when current. |
| Publication as change | A diagram, proof, dashboard, or source span is treated as the changed object or change occurrence. | Use description, publication, evidence, or source-use pattern for the carrier and keep the transformation under `A.3.4`. |

### A.3.4.P:9 - Consequences

- FPF gains one reusable restoration pattern for language about change situations without making every subject pattern carry its own cue list.
- `A.3.4` becomes easier to use because source labels are translated into transformation identity slots and neighboring values.
- `E.18`, `E.18.2`, and `C.29` stay distinct: selected compound structure, mathematical expression, and mathematical-lens use do not collapse.
- Architecture, method, work, mechanism, function, evidence, publication, and temporal patterns can point to the transformation ontic without becoming transformation patterns.
- The cost is one small restoration note when wording is FPF-governed and hides several candidate kinds.
- Reopen this pattern at the smallest affected row when `A.3.4`, `E.18`, `E.18.2`, `C.29`, method, mechanism, work, function, temporal, evidence, publication, or architecture patterns change the governing kind boundary, or when FPF wording repair repeatedly finds a change-situation label that the current settlements cannot recover by value.

### A.3.4.P:10 - Rationale

The current transformation ontology gives FPF one compact way to speak about bounded change. That compactness only helps if wording repair can return common source labels to the correct object and slot. Otherwise source labels reappear as local mini-ontologies: a process ontology here, a graph ontology there, a function ontology elsewhere.

`A.3.4.P` is placed under `A.3.4` because the recurring repair is not about words in general. The repair starts from the `U.Transformation` ontic and asks whether the current use is that ontic, one of its slots, one of its slot fillers, a compound structure, a mathematical description, or a neighboring claim. `E.10` recognizes the wording-use problem; `E.10.ARCH:2.2` distributes direct governing, ontic-level restoration, and facet-level restoration; this pattern performs the ontic-level transformation restoration.

### A.3.4.P:11 - SoTA-Echoing

| Source family | Use of source | What changes here |
| --- | --- | --- |
| Current FPF `A.3.4` transformation ontic | Governing ontology source for bounded change under conditions. | This pattern restores wording by first testing `U.Transformation` identity and participation slots. |
| Current FPF `E.18`, `E.18.2`, and `C.29` | Governing source line for compound transformation-flow structure and mathematical description. | Flow, path, network, circuit, graph, morphism, algebra, and category wording is separated into selected structure, mathematical expression, or lens use. |
| Current FPF `E.10` and `E.10.ARCH` precision-restoration architecture | Governing source line for recognition and distribution. | `E.10` recognizes change-situation wording; `E.10.ARCH:2.2` chooses direct governing, ontic-level restoration, or facet-level restoration; `A.3.4.P` restores only the transformation ontic neighborhood. |
| Current FPF `C.2.P.DR` and method, work, and mechanism patterns | Governing source line for declarative representation, method, mechanism, plan, work, and evidence separation. | Algorithm, workflow, process, proof, and path wording is recovered by current ontic slot, relation position, use relation, or claim kind rather than by programming-paradigm slogans. |
| Current FPF `A.6.F`, `A.6.M`, and architecture structural-view patterns | Governing source line for function-like, module, interface, and structural-view claims. | `A.3.4.P` recovers only the transformation-side value; `A.6.F`, `A.6.M`, `C.30.ASV`, or the direct governing pattern decides the recovered function, module, interface, or structural-view claim. |

SoTA use is conservative: this pattern relies on the current FPF settlements already carried by `A.3.4`, `C.2.P.DR`, and the governing neighboring patterns; it contributes the reusable restoration use for transformation-situation wording.

### A.3.4.P:12 - Relations

- **Builds on:** `A.3.4`, `E.10`, `E.10.ARCH`, `E.24`, `A.6.5`, and `E.8`.
- **Coordinates with:** `E.18`, `E.18.2`, `C.29`, `A.3.1`, `A.3.2`, `A.3.3`, `A.6.0`, `A.6.1`, `E.20`, `A.15.2`, `A.15.1`, `A.6.F`, `A.6.M`, `C.30.ASV`, `C.27.TA`, `C.27`, `A.10`, `C.2.P.DR`, `C.2.1`, `E.17`, and direct gate, decision, assurance, result, source, publication, and release patterns when those claims are current.
- **Coordinates with:** `E.10.MOVE` when source wording about a move, next action, pattern-use recommendation, work-entry readiness, language-state transition, architecture candidate use, or call-planning next action is not actually transformation wording.
- **Selected by:** `E.10` recognition row for change-situation wording when FPF wording repair needs transformation-ontic precision restoration.
- **Specializes:** `A.3.4` for wording-use precision restoration around situations of change.

### A.3.4.P:End

