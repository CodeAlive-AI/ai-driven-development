## B.1.5 - Gamma_method - Order-Sensitive Method Composition and Work Enactment

> **Type:** Part B composition and grounding pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.1.5:0 - Use This When

Use this pattern when a project must decide whether several recovered methods compose into one larger `U.Method`, and when order, guarded choice, parallel branches, typed joins, adapters, or method-interface exposure changes the identity of that whole method.

Typical moments:

- a procedure, workflow, algorithm, pipeline, proof route, clinical protocol, manufacturing recipe, inference pipeline, or operational playbook has named steps or branches;
- changing the order of two candidate submethods changes the result or the admissible conditions of use;
- a diagram or code file looks like a method, but it may be only a method description, a work plan, a dated work trace, a selector registry, or a mathematical lens;
- a larger method must expose some interactions at its boundary while hiding internal steps;
- assurance needs to know which joins, adapters, cutsets, or exposed interfaces make the composite method reliable enough to enact.

**Primary EntityOfConcern.** The EntityOfConcern is an order-sensitive method-composition claim: a claim that recovered `U.Method` values form one composite `U.Method` under a bounded context.

**First useful move.** For each apparent step or branch, recover the governed object before composing anything: `U.Method`, `U.MethodDescription`, `U.WorkPlan`, dated `U.Work`, `MethodRelationStructure@BoundedContext`, method-family registry or selector outcome, mathematical lens, mechanism, formal substrate, or quoted wording that does not yet carry a method claim.

**What goes wrong if missed.** A flowchart becomes the method, a plan item becomes a submethod, an event log becomes proof that a method was enacted, an order edge becomes a part, or a registry of alternatives is treated as one composed method. Then work starts from a description or label whose method identity, joins, interfaces, and failure conditions were never recovered.

**What this buys.** The project can admit a composite `U.Method` only when method parts, whole-forming relations, whole identity, interface exposure, assurance hooks, and enactment boundary are explicit. If that threshold is not met, the project still has a useful lower object: a selected method relation structure, description, plan, work record, lens, or `A.15.4` appearance-based reliance repair request.

**Not this pattern when.**

- If the current claim is one semantic way of doing with no order-sensitive composition question, use `A.3.1`.
- If the current claim is a representation that describes a method or method relation structure, use `A.3.2`.
- If the current claim is intended work, use `A.15.2`.
- If the current claim is a dated occurrence, use `A.15.1`.
- If the current claim is structural component parthood, use `A.14`, `C.13`, and `B.3.5`.
- If the current claim is only a method-family registry, selector, fallback relation, or alternative set without one whole-method assembly, use `G.5` or `MethodRelationStructure@BoundedContext`.

### B.1.5:1 - Problem Frame

`U.Method` is a non-agentive method holon kind. A method can have submethods and can participate as a submethod in a larger method. This does not mean every step-looking node, document section, file module, graph edge, work-plan item, or work occurrence is a method part.

Order-sensitive method composition is a narrow constructive question:

```text
Given recovered U.Method parts in one bounded context,
which whole-forming relations assemble them into one larger U.Method,
and what whole-level commitments make the resulting method reidentifiable and enactable?
```

The whole method is not the diagram, code, schedule, event log, or work history that may describe, plan, record, or evidence it. Work enacts the method; the method does not perform work.

`Gamma_method` is the name for this method-composition discipline. It is not a new root U-kind, not a workflow notation, not a resource-accounting operator, and not a substitute for `U.Work`.

### B.1.5:2 - Problem

Without B.1.5:

1. **Source-wording composition.** "Step", "stage", "activity", "task", "procedure", "workflow", "pipeline", or "algorithm" wording is accepted as method composition without recovering the actual objects.
2. **Description-as-method.** A workflow diagram, BPMN model, code repository, proof script, table, checklist, or graph path is treated as the composite method itself.
3. **Order as mereology.** `SerialStepOf`, `ParallelFactorOf`, guarded choice, or fallback relation is placed in a structural part-whole chain.
4. **Typed joins disappear.** One submethod's output is assumed to satisfy the next submethod's precondition without an adapter, bridge, conversion, or declared equivalence.
5. **Interface exposure is hidden.** Callers rely on internal interactions that should be encapsulated, or fail to see interactions that the composite method must expose.
6. **Run-time leakage.** Resources, timestamps, telemetry, performed values, and outcomes are baked into the method instead of being recorded on `U.Work`.
7. **False whole method.** A method-family registry, fallback table, selector rule, or local relation structure is treated as one whole method although no whole-method identity has been recovered.

### B.1.5:3 - Forces

| Force | Tension |
| --- | --- |
| Method reuse vs source concreteness | Teams need a reusable way of doing, while sources often show only one description, run, or plan. |
| Order fidelity vs compact modeling | Important sequences and joins must remain explicit without turning every diagram edge into ontology. |
| Whole-method identity vs relation usefulness | Some method-side relations are useful without asserting one composite method whole. |
| Interface exposure vs encapsulation | A composite method must state which interactions callers may rely on and which remain internal. |
| Assurance vs execution | Assurance needs joins, adapters, cutsets, and failure conditions; execution evidence belongs to work and evidence patterns. |

### B.1.5:4 - Solution

Admit one composite `U.Method` only when all composition coordinates are recovered.

```text
OrderSensitiveMethodComposition:
  WholeMethodRef: U.Method
  BoundedContextRef: U.BoundedContext
  PartMethodRefs: non-empty set of U.Method
  WholeFormingRelations:
    serial | parallel | guardedChoice | iteration | refinement | substitution | fallback | adapter | typedJoin
  WholeIdentity:
    preconditions
    effects or postconditions
    invariants
    accepted inputs and outputs
    failure and stop conditions
  MethodInterfaceExposure:
    exposed interactions
    forwarded interactions
    encapsulated interactions
  MHTOrWholeReidentification:
    whole-level commitment or B.2 relation when needed
  AssuranceHooks:
    typed joins, adapters, fragile branches, cutsets, evidence targets
  EnactmentBoundary:
    which U.Work may enact this method and which U.MethodDescription describes it
  LoweredDispositionIfNotComposite:
    MethodRelationStructure | U.MethodDescription | U.WorkPlan | U.Work | G.5 selector | lens | A.15.4 appearance-based reliance repair request
```

#### B.1.5:4.1 - Recover Parts Before Composition

Do not start from the word "step". Start from the object claim.

An apparent step can be:

- a `U.Method` submethod;
- a description constituent inside `U.MethodDescription`;
- a plan item inside `U.WorkPlan`;
- a dated `U.Work` occurrence or work part;
- an order relation, fallback relation, or selector relation inside `MethodRelationStructure@BoundedContext`;
- a mathematical or representation lens over a relation structure;
- mechanism or formal-substrate material;
- quoted wording that does not yet carry a method claim.

Only the first case can be a method part. Do not mint `U.StepSpec`, `U.StepMethod`, `U.MethodStep`, or `U.MethodAlgebra` for the others.

#### B.1.5:4.2 - Admit The Composite Method

When the apparent parts are recovered as `U.Method` values, compose them only after naming the whole-forming relations:

- **serial composition** when one submethod's accepted result is a precondition for the next;
- **parallel composition** when branches can proceed independently under a declared join condition;
- **guarded choice** when one branch is selected by a declared predicate;
- **iteration** when a submethod repeats until a stop condition is met;
- **refinement or substitution** when a submethod can stand in for another under declared bounds;
- **fallback or dispatch** when a selector chooses a method family member;
- **adapter** when a conversion method is needed to make a typed join admissible.

For order-sensitive composition, the method-composition claim also needs the order apparatus by reference: `OrderSpecRef`, any context hash or partial-order reproducibility condition inherited from `B.1.4`, and the typed join or adapter evidence that says one submethod's accepted outputs meet the next submethod's preconditions. This preserves the old capability-continuity obligation without treating "capability type" as the capability instance itself.

The result is one composite `U.Method` only when the whole has its own identity: preconditions, effects, invariants, accepted inputs and outputs, failure conditions, and work-facing acceptance relation. If those whole-level commitments cannot be named, lower the claim to `MethodRelationStructure@BoundedContext` or another neighboring object.

#### B.1.5:4.3 - Keep Order Out Of Structural Mereology

`SerialStepOf`, `ParallelFactorOf`, guarded choice, iteration, fallback, adapter, and typed join are method-composition or method-relation claims. They are not A.14 component parthood.

Use A.14, C.13, and B.3.5 when the claim is about structural parts of a holon. Use B.1.5 when the claim is about how ways of doing compose into a larger way of doing. The same project may need both, but they are different relation families.

When the current method-composition claim needs explicit order aggregation, context hash, partial-order soundness, or `Gamma_ctx` notation, use `B.1.4` for that ordered-relation apparatus. `B.1.4` can express the order discipline; B.1.5 still decides whether the recovered ordered methods are enough to admit one composite `U.Method`.

When the current claim is temporal phasing of the same carrier or method-description edition history, use the pattern that governs the phase or temporal claim rather than B.1.5. A phase boundary becomes a B.2-family question only when the boundary also introduces whole reidentification, closure, supervision, or context rebase. Order, phase, structural parthood, and MHT are different claims even when one source diagram uses one line for all of them.

#### B.1.5:4.4 - Expose The Composite Method Interface

A composite method needs an interface exposure decision:

- **exposed:** a caller may rely on the interaction as part of the whole method;
- **forwarded:** a caller may address an internal submethod interaction through a declared namespace or adapter;
- **encapsulated:** the interaction is internal and cannot be relied on from outside the whole method.

The interface exposure decision is part of the composite method identity when outside work, assurance, planning, or substitution relies on it. It is not a publication layout decision.

#### B.1.5:4.4.1 - Method Interface Card (MIC)

When an interface exposure decision is reliance-bearing, publish it as a compact Method Interface Card (MIC). The MIC is a method-description or assurance-facing card about the composite method; it is not a new U-kind and not the method itself.

```text
MethodInterfaceCard:
  methodRef: U.Method
  methodDescriptionRef?: U.MethodDescription
  orderSpecRef?: B.1.4 order apparatus
  externalInteractions:
    - interactionName
      exposureMode: exposed | forwarded | encapsulated
      acceptedInputOrCallSignature
      preconditions
      postconditionsOrEffects
      qualityEnvelopeRefs?
  invariants
  adapterOrTypedJoinRefs?
  assuranceHookRefs?
  rationale
```

Use a MIC when callers, planners, auditors, or substituting methods may rely on the composite boundary. For lightweight internal use, a few exposure lines may be enough; do not create a separate card by ritual.

#### B.1.5:4.5 - Keep Method Admission And Work Occurrence Separate

B.1.5 admits and grounds a composite `U.Method`. It may require a `U.MethodDescription` to describe the composition. It does not by itself create performed work.

A performed enactment is `U.Work` under `A.15.1`. The work record cites:

- the enacted `U.Method`;
- the method-description reference when current;
- the performer through `U.RoleAssignment`;
- the time window, parameter bindings, affected referent, resource ledger, outcome, and evidence relations.

Resource aggregation, elapsed time, telemetry, retries, and work outcomes belong to `U.Work`, `Gamma_work`, and evidence patterns. They do not become parts of the method.

The composition link is not one-to-one. A work occurrence may enact the whole method without exposing every submethod as a separate work part. A temporal work slice often enacts the same whole method during a selected interval. An episode may span several method factors, repeat one factor, or be split by evidence policy without changing the method identity. A work part enacts a submethod only when that submethod has already been recovered as `U.Method`; otherwise the current object is a work part, method-description node, evidence segment, mechanism material, system-component behavior, or `A.15.4` appearance-based reliance repair request.

**Reader check.** Before saying that a work part enacts a submethod, name both sides:

- the occurrence-side object: parent `U.Work`, part relation, interval or boundary event, performer, resources or evidence role;
- the method-side object: recovered `U.Method` submethod, whole-forming relation, preconditions, effects, interface, and whole-method identity.

If either side is missing, lower only that side. Do not repair a missing submethod by inventing a work part, and do not repair a missing work part by inventing a submethod.

#### B.1.5:4.5.1 - Planning And Performed-Work Obligations

B.1.5 has two common use positions, but they are positions in use, not two U-kinds:

- **Planning or description-side use.** Recover the submethods, order apparatus, typed joins or adapters, method interface exposure, invariants, and whole-level commitments. The output is a composite `U.Method` claim and, when a representation is needed, a `U.MethodDescription` or MIC that describes that method.
- **Performed-work use.** A `U.Work` occurrence may cite the composite `U.Method` and the method-description reference it used. The work record checks role assignment, capability-fit or admission conditions when current, preconditions, postconditions, order conformance, MIC-honouring interactions, resource ledger handoff, and evidence relations. These checks annotate or support the performed work; they do not become parts of the method.
- **Assurance use.** Identify cutset submethods, fragile typed joins, adapter points, mapping congruence or CL-sensitive edges, and the envelope or scope in which the composite method is expected to hold. B.3 and related assurance patterns evaluate those hooks; B.1.5 only makes them visible.

Useful invariants remain: a single recovered submethod composed alone does not create a surprising new method; order is deterministic only under the declared order apparatus; composite quality or throughput is constrained by critical path and weakest-link considerations unless a B.2-family whole reidentification claim is separately admitted; strengthening a submethod, adapter, or typed join should not make the composite method worse unless a stated side condition changes.

#### B.1.5:4.6 - Use MethodRelationStructure Below Whole-Method Threshold

Use `MethodRelationStructure@BoundedContext` when method-side relations are current but one whole method is not admitted. Typical cases:

- a fallback registry selects among alternatives;
- a workflow diagram relates method descriptions but does not recover method parts;
- a method family has refinement, substitution, or dispatch relations;
- a graph or algebra analyzes method relations as a lens;
- a cross-context source uses the same method names without a bridge for method identity;
- a work plan orders tasks but does not define one reusable method.

This lower object is not a failure. It is the right governed object when relation structure is useful but method holon composition is not current.

### B.1.5:5 - Worked Slices

#### B.1.5:5.1 - Manufacturing Recipe

`AssembleFrame`, `InstallMotor`, and `RunFunctionalTest` are recovered as `U.Method` values in a bounded manufacturing context. `InstallMotor` must precede `RunFunctionalTest`; the test accepts the installed harness as input; an adapter method is needed when a supplier motor uses a different connector.

The composite `BuildAndVerifyPumpUnit` is admitted as a `U.Method` only after the whole states its preconditions, accepted inputs, final effect, exposed start and abort interactions, encapsulated internal calibration interactions, and failure conditions. The actual Tuesday build is `U.Work`; resource burn and test telemetry are not method parts.

#### B.1.5:5.2 - Emergency Intake

`RegisterPatient`, `AssessVitals`, `ClassifyUrgency`, and `RouteToCare` may compose into `EmergencyIntake@Hospital`. The guarded choice is driven by declared vital-sign and symptom predicates. A role assignment and capability check determine who may enact the work, but they are not parts of the method.

If the source only provides a wall poster with boxes and arrows, the current object is first `U.MethodDescription`. The composite `U.Method` is admitted only when the hospital context recovers the methods, guards, typed joins, failure response, and interface exposure.

#### B.1.5:5.3 - Learned Model Pipeline

A neural-network pipeline may describe feature extraction, embedding, attention, retrieval, ranking, and explanation generation. Some blocks may be formal substrate or mechanism material, some may be `U.MethodDescription`, and some may be recovered as `U.Method` values.

The pipeline is one composite `U.Method` only when it has accepted inputs, outputs, invariants or admissibility conditions, typed joins, fallback behavior, failure conditions, and work-facing acceptance criteria. Otherwise keep the graph as a method description, mathematical lens, mechanism material, or `MethodRelationStructure@BoundedContext`.

#### B.1.5:5.4 - Evidence Synthesis And Publication

`CollectDatasets`, `NormalizeSchemas`, `EstimateModel`, `CrossValidate`, and `DraftManuscript` can compose into `EvidenceSynthesisPublish@ResearchContext` only when each candidate is recovered as a `U.Method` and the typed joins are explicit. `NormalizeSchemas` must produce a feature or evidence space acceptable to `EstimateModel`; legacy datasets may need adapter methods; `CrossValidate` may be a critical cutset for later assurance; `DraftManuscript` may require a provenance or SCR condition before publication work is admitted.

A paper draft, workflow diagram, repository, or notebook is first a `U.MethodDescription` or another episteme. The publication work is `U.Work`. Compute, storage, reviewer time, and artifact-release resource costs belong to `U.Work` and `Gamma_work`. The MIC may expose `Submit()` and `ReleaseArtifacts()`, forward a parameterized `CrossValidate.Folds(k)` interaction, and encapsulate ad hoc scrubbing utilities.

### B.1.5:6 - Conformance Checks

| Check | Requirement |
| --- | --- |
| `CC-B1.5-1` | Every claimed method part is recovered as a `U.Method` value before method-holon composition is admitted. |
| `CC-B1.5-2` | Step wording, description nodes, plan items, work occurrences, file modules, graph edges, and source wording are not method parts by position or wording. |
| `CC-B1.5-3` | Serial, parallel, guarded, iterative, fallback, adapter, and typed-join relations are method-composition or method-relation claims, not structural component parthood. |
| `CC-B1.5-4` | The composite method states whole-level preconditions, effects, invariants, accepted inputs and outputs, failure conditions, and work-facing acceptance relation. |
| `CC-B1.5-5` | Interface exposure distinguishes exposed, forwarded, and encapsulated interactions when outside reliance depends on the method boundary. |
| `CC-B1.5-6` | `U.MethodDescription`, `U.WorkPlan`, `U.Work`, mechanism, formal substrate, mathematical lens, evidence, and publication-use claims remain with their direct patterns. |
| `CC-B1.5-7` | If whole-method identity is not recovered, the claim is lowered to `MethodRelationStructure@BoundedContext` or another neighboring object without demoting `U.Method` as a holon kind. |
| `CC-B1.5-8` | When the composite method needs whole reidentification or emergence-family explanation, use `B.2` in addition to B.1.5. |
| `CC-B1.5-9` | A work part is not evidence of a submethod unless the method-side candidate is recovered as `U.Method`; temporal slices, episodes, event-log segments, telemetry intervals, engine strokes, detector components, and work-plan items stay with their direct patterns until that recovery is made. |
| `CC-B1.5-10` | Order-sensitive composition that relies on order semantics names the `B.1.4` order apparatus, including `OrderSpecRef`, context hash, partial-order soundness, or equivalent order evidence when current. |
| `CC-B1.5-11` | Typed joins show capability-continuity evidence as input/output, pre/post, adapter, bridge, or equivalence claims without turning those signatures into `U.Capability` instances. |
| `CC-B1.5-12` | Reliance-bearing composite boundaries publish MIC or equivalent exposure lines and performed work honours only the exposed or forwarded interactions unless the method is revised. |
| `CC-B1.5-13` | Resource costs, yields, dissipation, telemetry, and resource ledgers are handed to `U.Work`, `B.1.6`, and evidence patterns; B.1.5 may point to them but does not aggregate them. |
| `CC-B1.5-14` | Assurance hooks name cutsets, fragile joins, adapter points, CL-sensitive mappings, and envelope or scope refs for B.3; apparent super-additivity is returned to B.2-family whole reidentification instead of being averaged into the method. |

### B.1.5:7 - Anti-Patterns And Repairs

| Anti-pattern | Repair |
| --- | --- |
| "The workflow diagram is the composite method." | First govern the diagram as `U.MethodDescription`; admit a composite `U.Method` only after recovered submethods and whole-forming relations are named. |
| "Step A is part of the method because it is a box." | Recover whether the box denotes a `U.Method`, description node, plan item, work occurrence, relation edge, or lens expression. |
| "Parallel branches can join because the picture rejoins." | State the typed join, adapter, or equivalence relation; otherwise the composite method is not admitted. |
| "The selector table is the method." | Use `G.5` or `MethodRelationStructure@BoundedContext` unless one whole method with whole-level commitments is recovered. |
| "The run proved the method structure." | Record the run as `U.Work` and evidence separately; use it as evidence only through the governing evidence or assurance relation. |
| "The phase is a method step." | Use phase or temporal relation discipline for carrier phases and use B.2 only when the phase boundary changes whole identity, supervision, closure, or context. |
| "The join improves throughput, so the method has emergence." | First name critical path, cutsets, typed joins, and CL-sensitive mappings for assurance; open B.2 only when the whole-level reidentification claim remains. |
| "The MIC is a nice diagram." | Treat MIC as reliance-bearing method-interface description only when callers, planners, auditors, or substitutions depend on exposed, forwarded, or encapsulated interactions. |

#### B.1.5:7.1 - Consequences And Rationale

B.1.5 buys deterministic method composition without confusing method, method description, work occurrence, resource ledger, and assurance argument. The practitioner sees what is being composed by order and typed joins, what is spent by performed work, and what is later assessed by assurance.

The cost is explicitness: submethods, order apparatus, typed joins, adapters, interface exposure, and assurance hooks must be named before the composite method can be relied on. That cost prevents hidden brittleness at joins and accidental external dependencies at method boundaries.

The rationale is the old strict distinction in updated ontology. Order is semantic but not structural parthood. A method can be a non-agentive holon, but a step label, graph node, phase, source section, or work part is not a method part until the `U.Method` object is recovered. `Gamma_method` composes ways of doing; `Gamma_work` accounts resources; B.3 evaluates assurance; B.2 handles whole reidentification when the composed method participates as a new whole.

### B.1.5:8 - SoTA-Echoing

| Source line | Selected source examples already carried by neighbouring hosts | What FPF takes | What FPF does not take |
| --- | --- | --- | --- |
| Current workflow, case, decision, process-mining, and object-centric event-log practice separates process models from event logs and resource records. | `A.15` carries BPMN, CMMN, DMN, DDD, service-design, and ITIL source use; `A.15.1` carries dated work-occurrence identity. | B.1.5 keeps method, method description, work plan, dated work, event trace, and resource aggregation separate while still allowing evidence return from work occurrence to method admission. | A workflow notation, event log, or trace is not the composite method. |
| Typed functional, effect, protocol, and workflow-composition practice treats composition as constrained by interfaces, preconditions, postconditions, handlers, and admissible order. | `A.3.1` and `A.3.2` carry method versus method-description separation, constructor-theory or process-theory source-material use, scoped-effect analogy, and return discipline for method-description references. | B.1.5 requires typed joins, adapters, exposed or encapsulated interactions, preconditions, outputs, and failure conditions before admitting a composite method. | A type signature, process-theory description, or source-material description alone does not ground dated work occurrence. |
| Systems and software architecture practice uses interface exposure and encapsulation to make composed behavior reliable and substitutable. | `A.15.2` carries plan versus occurrence discipline; `A.15` carries role-assignment and method-enactment alignment. | B.1.5 makes method-interface exposure part of method identity when outside work, planning, substitution, or assurance relies on it. | Publication layout or diagram position does not decide whether an interaction is exposed, forwarded, or encapsulated. |
| FPF holon and whole-reidentification patterns require parts, whole-forming relations, whole-level commitments, and higher-level participation. | `A.1`, `B.2`, `A.14`, `C.13`, and `B.3.5` provide neighbouring holon, whole-reidentification, and structural-parthood tests. | Composite method admission is a method-holon grounding question with method-side whole-forming relations, not a structural-component parthood shortcut. | Method-composition order is not automatically A.14 component parthood. |

### B.1.5:9 - Relations

- Builds on `A.1` for holon admission and non-agentive holon kinds.
- Builds on `B.1.4` when the method-composition claim uses `Gamma_ctx`, ordered-relation aggregation, context hash, or partial-order soundness.
- Builds on `A.3.1` for `U.Method`.
- Builds on `A.3.2` for `U.MethodDescription`.
- Coordinates with `A.15`, `A.15.1`, and `A.15.2` for role, method, work-plan, and performed-work separation.
- Coordinates with `B.1.6` and `Gamma_work` for work-resource aggregation.
- Coordinates with `B.3` for weakest-link, cutset, CL-sensitive mapping, and assurance evidence use.
- Coordinates with `A.14`, `C.13`, and `B.3.5` when structural parthood and constructive grounding are current.
- Coordinates with `B.2` when whole reidentification, MHT, or emergence-family explanation is current.
- Coordinates with `G.5` when method-family registry, selector, fallback, or candidate-set relation is current.
- Coordinates with `C.29`, `A.6.0`, `A.6.1`, and `E.20` when mathematical lens, formal substrate, or mechanism claim is current.
- Coordinates with `E.10` for method, step, process, workflow, ownership/stewardship, requirement, and source wording precision recovery.

### B.1.5:End

