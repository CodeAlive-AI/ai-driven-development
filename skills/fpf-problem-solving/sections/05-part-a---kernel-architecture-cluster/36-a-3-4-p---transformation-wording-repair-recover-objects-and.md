## A.3.4.P - Transformation Wording Repair: Recover Objects and Claims

> **Type:** A.3.4 precision-restoration child pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

**Intent.** Restore precision when wording about change hides the object or claim under concern. Distinguish a bounded transformation and its changed referent from acting-System and influence claims, then identify the neighboring objects and their relations before rewriting.

**Use this when.** Use `A.3.4.P` when source or FPF-governed wording such as "pipeline", "dataflow", "flow", "network", "circuit", "path", "slice", "workflow", "process", "operation", "transformation", or "change" seems to name the thing under concern, but the text has not yet recovered what kind of FPF value is actually current.

**First useful move.** State what the passage claims and about which subject. Recover the meaning of the ambiguous word and the conditions that change its use. Test an actual-change claim under A.3.4; open actor, influence and other neighboring questions only when the passage makes those claims. Then rewrite the affected wording, preserving its useful content. Keep a `TransformationWordingRepair` note only when the receiving use needs inspectable detail.

**Not this pattern when.**

- If one bounded transformation is already identified and only its ordinary use continues, apply `A.3.4` directly.
- If the current claim is already a selected transformation-flow structure, use `E.18`.
- If the current claim is a graph, morphism, category, algebra, path, circuit expression, network expression, or other mathematical description, use `E.18.2` and `C.29`.
- If the current claim is only a semantic way of doing, method description, mechanism, work plan, dated work, evidence relation, publication relation, gate, decision, assurance, result, or temporal claim, use the subject pattern.
- If the word is quoted source wording with no FPF-governed use, keep it quote-only.

### A.3.4.P:1 - Problem frame

People talk about change with familiar labels—for example, a manufacturing process, refrigeration cycle, or team workflow. Recover the object and claim when that wording leaves an FPF-governed distinction unresolved.

The recurring defect is a second ontology by convenience. The same text may treat "process" as method, work occurrence, transformation-flow structure, mechanism, result evidence, and publication diagram. A graph path may become an action route. A network label may become a durable head beside `TransformationFlowStructure`. A function word may collapse functioning, mathematical function, software routine, module allocation, a system merely named as actor, and a differently typed influence source whose direct relation has not been recovered.

This pattern distinguishes the actual change, its description and any neighboring claims, then uses the subject pattern for each unresolved question.

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
| Recognition and precision | Source labels help readers recognize a situation; an unresolved FPF claim needs its kind, participants, governing relation and applicable conditions recovered. |
| One actual transformation and selected flow structure | `U.Transformation` identifies one independently grounded actual bounded change and establishes neither transformation parthood nor partlessness at the current resolution. `TransformationFlowStructure` positions, relates, or locates transformation loci and adjacent governed values; common structure membership establishes no transformation composition. |
| Acting System and influence source | An assignment occurrence alone does not prove performance, and generic transformation participation does not prove action. Performed Work requires each precise performer's A.13 core and independent A.15.1 admission; add F.6 afterward only when precise assignment-bound attribution is current. Any Work-to-change relation required by the claim remains separate. A non-Work actor needs another exact direct actor-side relation. Every influence source keeps its own kind and exact relation. |
| Formal and project-world change | A formal construction may be a transformation over a formal object, or it may be a mathematical description of project-world structure; the current object decides. |
| Repair and readability | Recover enough ontology for the current use. Record a repair note only when the receiving use needs inspectable detail. |

### A.3.4.P:4 - Solution

Restore the change situation in this order.

1. **Name the working concern.** State what the text is trying to do: identify a change, describe a flow, choose a method, claim evidence, compare architectures, describe functioning, or use a publication.
2. **Test an actual-change claim when one is made.** Under A.3.4, identify the continuing changed subject, temporal extent or formal ordering boundary, boundary conditions, actual characteristic and relation facts, and continuity or reidentification rule. A plan, prediction or assertion alone leaves occurrence unresolved; its content can support occurrence facts when its evidence or derivation use warrants them.
3. **Separate an acting-System claim from influence when either is asserted.** For dated Work, recover each precise performer’s A.13 core and independently admit the Work under A.15.1; add F.6 afterward only for precise attribution to that same assignment. Establish the Work-to-change relation required by the claim separately. A non-Work action needs the System and the participant, operation-application, functioning, causal or other actor-side relation defined by its subject pattern. An influence source keeps its own kind: for example, an organization, toolchain, selected structure or Method. Identify the architecture, Work, communication, constraint or other relation by which that source influences the subject; leave an unsupported claim unresolved.
4. **Recover the neighboring claims the passage needs.** A way of doing, performed Work, a flow structure and evidence for a result require different objects and relations. Use the selection table in 4.2 for those questions.
5. **Use the exact governing relation for each neighboring value.** A neighboring object keeps its own kind and governor; state its current relation to the transformation, changed referent, work, architecture candidate, or receiving use instead of placing it inside a transformation record.
6. **Rewrite after kind and relation recovery.** Keep ordinary domain wording when it conveys the recovered kind and relation unambiguously. Keep quoted source wording within its supported source use. Use F.19 to preserve the complete claim while removing unnecessary apparatus; an unresolved meaning leaves the dependent wording unresolved.
7. **Make the next use recoverable.** The reader should be able to use the identified object or claim under its subject pattern, retain the bounded source use, or recognize the missing basis that limits the claim.

#### A.3.4.P:4.1 - TransformationWordingRepair note

Use this optional note when the receiving use needs an inspectable repair. Fill only the fields needed by that use; an ordinary wording repair can finish in the revised passage.

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
  StopOrReturnCondition:
  BlockedOverread?:
  RemainingReaderUse:
```

`ActualTransformationDisposition` is one of: actual bounded transformation recovered, not a transformation, not recovered, not current for this claim, quote-only source wording, or blocking missing value.

`TransformationWordingRepair` holds wording-repair information. `RetainedUse` identifies the use of the encountered wording that remains; `RemainingReaderUse` names the next action with the recovered object or claim. Include `BlockedOverread?` only for a mistaken interpretation with an independent local ground, a plausible intended reader and an effect on truth, understanding or use under F.19:4. The actor and influence fields describe the claims actually being examined; they introduce no kinds or relations.

Use the actor and influence tests in 4.4 only for the claims represented in those fields.

If an episteme asserts possible, intended, planned, modelled, predicted, or actual change, identify that episteme separately through C.2.1 when the assertion is current. Empirical grounding remains optional and, when current, uses its own exact relation; neither the assertion nor its grounding relation substitutes for the actual transformation basis. Use the governing subject pattern's requirements when creating a project record, gate decision, work plan, or work occurrence.

#### A.3.4.P:4.2 - Subject pattern selection

| If recovery shows... | Use this subject pattern | Keep this boundary |
| --- | --- | --- |
| one actual bounded change under conditions | `A.3.4` | A source label identifies no transformation until the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis are recoverable. |
| selected structure over transformation loci and adjacent governed values | `E.18` | `TransformationFlowStructure` positions, relates, or locates those loci and values. Selection or common structure membership establishes neither an actual transformation occurrence nor transformation composition, parthood, or partlessness. |
| mathematical expression over a selected structure or formal object | `E.18.2`, `C.29`, `A.6.0`, or the direct formal pattern | Recover project-world work separately under `A.15.1` when the current use also claims it. |
| semantic way of doing | `A.3.1` | Recover the semantic way of doing under `A.3.1`; identify dated work, mechanism, evidence, or transformation claims separately when current. |
| episteme describing a way of doing | `A.3.2` | For example, code, a protocol, a solver model, a proof script, a process model, or a diagram may describe a method. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, or mechanism-governing-definition assignment | `A.6.1` and `E.20` | Recover the mechanism's defining content under `A.6.1` and `E.20`. |
| planned or dated work | `A.15.2` or `A.15.1` | Identify the plan or dated occurrence under its governing pattern; recover any Method, MethodDescription, transformation-flow structure, or evidence claim separately. |
| pattern-use recommendation, work-entry readiness, language-state move, architecture candidate use, or call-planning next action | The applicable subject pattern; use `E.10.MOVE` when the move-like meaning remains unresolved | Move-like wording is not transformation wording unless a bounded `U.Transformation` or selected `TransformationFlowStructure` is actually current. |
| function-like wording inside a change situation | `A.3.4.P` only to distinguish the actual transformation, selected `TransformationFlowStructure`, a System claimed to act under an exact actor-side relation, a differently typed influence source under its exact relation, boundary binding, or `FunctioningRef?`; use `A.6.F` for detailed function-kind discrimination | For an actual-transformation claim, recover its occurrence basis; for an actor claim, use the performed-Work or non-Work basis in 4.4. |
| state-space and transition-law episteme | `A.3.3` | Dynamics can model possible or claimed change; recover any claimed actual occurrence independently under `A.3.4`. |
| time window, cadence, duration, latency, freshness, currentness, trajectory, inertia, or effort | `C.27.TA`; use `C.27` for temporal-claim adequacy | `C.27.TA` supplies positive temporal subject matter; `C.27` governs temporal-claim adequacy. Recover transformation identity under `A.3.4` when that separate claim is current. |
| evidence, provenance, source, publication, dashboard, view, gate, decision, assurance, result, or release claim | the direct governing evidence, source, publication, gate, decision, assurance, result, or release pattern | A visible record or path does not establish evidence sufficiency, assurance, gate passage, deontic permission, work authorization, release authorization, performed work, or acceptance by itself. |

#### A.3.4.P:4.3 - Common source-label settlements

| Source label | First recovery question | Typical admissible outcomes |
| --- | --- | --- |
| `pipeline` or `dataflow` | Is the current object one transformation, a compound transformation-flow structure, a method description, a work plan, or a publication diagram? | `A.3.4`, `E.18`, `A.3.2`, `A.15.2`, `C.2.P.DR`, or quote-only source wording. |
| `flow` | Is flow the selected structure, a mathematical expression, an actual material, energy, signal, or information flow, or an ordinary source label? | `E.18`, `E.18.2`, `C.29`, direct subject pattern, or quote-only source wording. |
| `network` or `circuit` | Is it a structure form, topology label, mathematical-expression family, functional structure, architecture-selected structure, or subject-domain system? | `E.18`, `E.18.2`, `C.29`, `C.30.ASV`, `A.6.F`, or direct subject pattern. |
| `path` or `slice` | Is it graph path, `PathSlice`, evidence path, carrier path, mathematical path, source quote, or action-route metaphor? | `E.18`, `A.10`, `C.29`, `C.2.P.DR`, carrier wording, source wording, or an explicit stop when no exact current claim is recovered. |
| `workflow` or `process` | Is it method, method description, work plan, dated work, transformation-flow structure, mechanism, or source label? | `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `E.18`, `A.6.1` with `E.20`, or quote-only source wording. |
| `algorithm`, `program`, `solver`, or `proof` | Is it method, method description, formal substrate, mathematical lens, mechanism, work occurrence, evidence, or proof publication? | `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1` with `E.20`, `A.15.1`, `A.10`, `C.2.1`, or the governing publication pattern. |
| `function`, `functional`, or `functioning` | Does the passage claim an actual change, flow structure, action, influence or boundary relation, or does the function-like kind itself remain unresolved? | Use the conditional tests in 4.4 for the claimed relations; use `A.6.F` for remaining function-kind discrimination. |

#### A.3.4.P:4.4 - Functional change-situation settlement

When change-situation wording includes `function`, `functional`, `functioning`, `transforms`, or `implements`, use this pattern only to recover the exact current claims:

- Is one actual bounded `U.Transformation` established by changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification?
- Is a selected `TransformationFlowStructure` current without being treated as the acting system or the change occurrence?
- Is performed Work being attributed to a System? Recover each precise performer's A.13 core and independently admit the Work under A.15.1. Add F.6 only when precise assignment-bound attribution is current, then state separately the realization, causal, production, or other Work-to-change relation required by the claim. An assignment occurrence, Work record, common timestamp, or generic transformation-participant fact does not prove performance.
- Is a non-work functional or physical actor-side claim current? Recover the exact system and the participant, operation-application, functioning, causal, or other direct actor-side relation supplied by its governor. If no actor-side governor is recoverable, leave the actor claim unresolved.
- Is a distinct influence source claimed? Recover its kind and influence relation. An organization can be an admitted System, a selected structure remains a structure, and a Method or Method family is not made a holon by its label. Use the architecture, Work, communication, constraint or candidate-synthesis relation the claim needs. System membership and action require their own bases when those claims are made.
- Are exact participant, port, operation-application, relation-signature, or functioning relations current at the boundary? Keep them under their direct governors; a transformation input or output requires its own direct relation.

After recovering the claim, apply `A.6.F` if the function-like kind or relation remains unresolved. Otherwise use the governing subject pattern directly.

#### A.3.4.P:4.5 - Description, publication, and evidence boundary

A diagram or report, for example, may describe a transformation, state a claim about it, provide evidence for that claim, or help compare transformations. When an actual transformation is claimed, recover its subject-side occurrence basis separately. If the description, assertion, or publication is current, use the episteme, publication, source, or declarative-representation pattern; C.2.1 empirical grounding remains an optional separate relation when the use requires it. If the actual transformation is current, keep every description, assertion, publication, and evidence use as an exact neighboring claim.

### A.3.4.P:5 - Archetypal Grounding

#### A.3.4.P:5.1 - Refrigerator functional diagram

Source wording says: "The refrigeration circuit moves heat through the cycle."

Repair: recover whether the current claim is a refrigerator subsystem transformation, a `TransformationFlowStructure` over compressor, condenser, expansion, and evaporator transformations, a thermodynamic mechanism, a functional architecture view, or a schematic publication. The circuit label may stay as ordinary domain wording, but FPF use names the selected structure, mechanism, or publication relation.

#### A.3.4.P:5.2 - Neural-network block

Source wording says: "The attention block transforms activations in the model pipeline."

Repair: the block may be an architecture locus or module allocation. For a claimed action, apply the dated-Work or non-Work test in 4.4 and establish any Work-to-activation relation required by the use. A design organization, Method, toolchain or communication System that influenced the block keeps its own kind and influence relation. Activation and tensor-shape claims use their participant, port, operation-application or signature relations. An episteme describing an admitted attention Method may be a MethodDescription under A.3.2; C.29 governs a mathematical-representation use when one is made. The pipeline may be a transformation-flow structure. Use the applicable evidence or evaluation pattern when relying on a benchmark or ablation result.

#### A.3.4.P:5.3 - CRISPR editing workflow

Source wording says: "The guide-selection workflow changes the target gene."

Repair: the target-gene edit is only a candidate `U.Transformation` until the exact biological referent, edit boundary, boundary conditions, actual sequence and direct-relation facts, and reidentification rule establish one occurrence. Guide selection may be method, method description, work plan, evidence-facing table, or performed lab work according to the current claim.

#### A.3.4.P:5.4 - Evidence path near a plant change

Source wording says: "The evidence path lets the valve-change flow proceed."

Repair: an evidence path may be a legitimate `A.10` provenance relation for a named claim. The valve change still needs its exact changed referent, boundary, boundary conditions, actual subject facts, and continuity or reidentification basis; work plan, dated work, gate, assurance, result, and receiving use remain exact neighboring relations when current. The path establishes no work authorization, release authorization, gate passage, performed work, or actual transformation by shape or name.

#### A.3.4.P:5.5 - Filled minimal repair note

```text
TransformationWordingRepair:
  EncounteredWording: "the refrigeration circuit moves heat through the cycle"
  WorkingConcern: recover whether the sentence is about one bounded heat-transfer change, a selected compound transformation-flow structure, a thermodynamic mechanism, a functional architecture view, or a schematic publication.
  RecoveredEntityOfConcern: `RefrigeratorHeatTransferFlowStructure-1`, the exact selected `TransformationFlowStructure` over the compressor, condenser, expansion, and evaporator transformation loci.
  ActualTransformationDisposition: no actual occurrence claim is made; the current object is the selected `RefrigeratorHeatTransferFlowStructure-1`.
  NeighboringClaimAndExactRelation: the four named loci are positions in `RefrigeratorHeatTransferFlowStructure-1`; bindings to actual transformation occurrences have not been established.
  GoverningPattern: `E.18` governs `RefrigeratorHeatTransferFlowStructure-1`; use `A.3.4` when a claim about an actual component occurrence needs its basis established.
  RetainedUse: "circuit" may remain ordinary domain wording for `RefrigeratorHeatTransferFlowStructure-1` after that exact selected structure is named.
  StopOrReturnCondition: use the selected structure; a later claim about an actual occurrence needs the A.3.4 occurrence basis and remains unresolved while that basis is missing.
  RemainingReaderUse: use `E.18` for `RefrigeratorHeatTransferFlowStructure-1`; open the applicable subject pattern when an additional claim is needed.
```

One rewritten sentence for this selected structure is: “RefrigeratorHeatTransferFlowStructure-1 has four positions: compressor, condenser, expansion and evaporator.”

### A.3.4.P:6 - Bias-Annotation

Familiar domain words can bias kind selection before the actual claim is recovered. The refrigeration and attention examples show why the same label may describe a structure, mechanism or action. Start from the sentence’s participants and predicate, and retain an already adequate ordinary domain expression.

### A.3.4.P:7 - Conformance Checklist

| Check | Conformance statement |
| --- | --- |
| `CC-A34P-1` | The repair names the encountered wording and the working concern before selecting a replacement. |
| `CC-A34P-2` | If one actual bounded transformation is current, the repair names or blocks its exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification basis. |
| `CC-A34P-3` | Each neighboring object keeps its own kind and is connected only by an exact current relation to the transformation, changed referent, work, architecture candidate, or receiving use. |
| `CC-A34P-4` | `TransformationFlowStructure`, graph mathematical description, path mathematical description, and subject-domain network or circuit wording are kept distinct. The selected structure positions, relates, or locates transformation loci and adjacent governed values; composition, parthood, and partlessness require their direct predicates. |
| `CC-A34P-5` | Method, method description, mechanism, work plan, dated work, evidence, gate, decision, assurance, result, source, and publication claims remain with their subject patterns. |
| `CC-A34P-6` | Function-like wording distinguishes the actual-change, action, influence and boundary claims that it makes; detailed function-kind discrimination remains governed by `A.6.F`. |
| `CC-A34P-7` | The repaired wording preserves its needed use and makes any material stop or subject-pattern return recoverable. An optional warning meets the F.19:4 plausible-reader test. |
| `CC-A34P-8` | F.19 handles ordinary precise-plain-language rewriting. For unresolved change-situation wording, `E.10` supplies recognition cues, `A.3.4.P` restores the transformation ontic neighborhood, and neighboring patterns define or constrain recovered objects and exact relations. |
| `CC-A34P-9` | For a performed-Work actor claim, recover each precise performer's A.13 core and independently admit the Work under A.15.1; add F.6 afterward only when precise assignment-bound attribution is current and separately name the Work-to-change relation required by the use. A non-Work actor claim names another exact direct actor-side relation. |
| `CC-A34P-10` | Possible, intended, planned, modelled or predicted change remains the corresponding claim content. An assertion or its empirical grounding supports only what its evidence or derivation warrants; an actual-occurrence claim requires the A.3.4 basis. |

### A.3.4.P:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Cue word as ontology | "Pipeline", "process", "network", or "circuit" is treated as the FPF kind. | Recover the current object: `U.Transformation`, `TransformationFlowStructure`, mathematical description, method, work, publication, or direct subject pattern. |
| Replacement by smoother umbrella | "Process" is replaced with "flow" or "operation" without recovered kind. | Run the replacement through the same recovery. If the kind is still hidden, leave it unresolved. |
| Network head inflation | Frequent network or circuit wording becomes a peer durable head. | Use network or circuit as structure form, topology label, mathematical-expression family, domain label, or subject-domain system only when recovered by value. |
| Selected structure as transformation composition | Common membership in one flow, path, network, circuit, or pipeline is treated as a composite transformation, transformation-part relation, or proof of indivisibility. | Use `E.18` only to position, relate, or locate transformation loci and adjacent governed values. Ground every actual `U.Transformation` independently under `A.3.4`; common structure membership establishes neither composition, parthood, nor partlessness. |
| Workflow as performed work | A workflow diagram or process model is treated as dated work. | Use `A.3.2`, `E.18`, or `C.2.P.DR` for the description or structure; use `A.15.1` only for dated work. |
| Function as proof of behavior | A module, port, participant, assignment occurrence, or "transformer" label is treated as proof of actual change or action. | Recover the actual transformation basis. For performed Work, recover each precise performer's A.13 core and independently admit the Work under A.15.1; add F.6 only when precise assignment-bound attribution is current, and name the required separate Work-to-change relation. Otherwise use the exact participant, operation-application, functioning, causal, or other direct actor-side relation. |
| Architecture influence as action | A manufacturing or certification organization, design organization, Method or Method family, toolchain, communication System, selected structure, or other value is called the actor because it constrained or enabled a candidate. | Recover the value's exact kind first, then only its exact architecture, Work, communication, constraint, or candidate-synthesis relation. For an actor claim, apply the separate performed-Work or non-Work test in 4.4. |
| Publication as change | A diagram, proof, dashboard, or source span is treated as the changed object or change occurrence. | Recover the cited object's kind and use under its subject pattern; use `A.3.4` for any claimed actual change. |

### A.3.4.P:9 - Consequences

- The reader can keep a recognizable domain expression while making its object and relation unambiguous.
- A.3.4 establishes the basis needed by an actual-change claim; other subject patterns answer the separate claims.
- The ordinary result is the repaired wording and the needed stop or subject-pattern return; use a `TransformationWordingRepair` note only when the receiving use needs recoverable detail.

### A.3.4.P:10 - Rationale

Words such as process and circuit are useful across several disciplines, but they can conceal different subjects and predicates. Recovering those differences lets the reader choose the appropriate occurrence test or construction without replacing every familiar word with a formal label.

A change description can concern an actual occurrence, an acting System, an influence source, a selected structure or a representation. Each has its own conditions. The conditional sequence therefore starts from the claim being made and restores only the distinctions needed to interpret and use it.

### A.3.4.P:11 - SoTA-Echoing

A.3.4 supplies the actual-change criterion and its comparison with theories of change. E.18 distinguishes selected transformation-flow structure from occurrence, and C.29 supplies representation correspondence. This pattern connects ambiguous change-situation wording to those different tests. E.10 supplies recognition cues; F.19 governs the connected reading and rewrite. The function, method, Work and publication patterns supply the remaining subject distinctions when those claims are made.

### A.3.4.P:12 - Relations

- **Builds on:** `A.3.4`, `E.10`, `E.10.ARCH`, `E.24`, `A.6.5`, `E.8`, and `F.19`.
- **Coordinates with:** `E.18` for a selected structure that positions, relates, or locates transformation loci and adjacent governed values without establishing transformation composition, parthood, or partlessness; and with `E.18.2`, `C.29`, `A.3.1`, `A.3.2`, `A.3.3`, `A.6.0`, `A.6.1`, `E.20`, `A.15.2`, `A.15.1`, `A.6.F`, `A.6.M`, `C.30.ASV`, `C.27.TA`, `C.27`, `A.10`, `C.2.P.DR`, `C.2.1`, `E.17`, and direct gate, decision, assurance, result, source, publication, and release patterns when those claims are current.
- **Coordinates with:** `E.10.MOVE` when source wording about a move, next action, pattern-use recommendation, work-entry readiness, language-state transition, architecture candidate use, or call-planning next action is not actually transformation wording.
- **Selected by:** `E.10` recognition row for change-situation wording when FPF wording repair needs transformation-ontic precision restoration.
- **Specializes:** `A.3.4` for wording-use precision restoration around situations of change.

### A.3.4.P:End
