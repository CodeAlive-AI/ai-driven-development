## A.6.5 - U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Relation slot discipline.

### E.24.UK settlement

`U.RelationSlotDiscipline` is retained as a root durable relation-slot discipline kind. It governs the reusable SlotSpec discipline for relation-bearing structures: local SlotKinds, admitted ValueKinds, and by-value or RefKind filling. It is not `U.Relation`, not a generic interface kind, not a slot position, not a record form, and not a publication form.

**Use this when.** Use this pattern when a relation, operator, record, episteme slot relation, signature vocabulary item, interface specification, method description, service-access description, role assignment, evidence-use relation, status-use relation, or transformation-flow structure needs named positions and typed fillers rather than a loose parameter list.

**Primary EntityOfConcern.** The EntityOfConcern is `U.RelationSlotDiscipline`: the FPF discipline for declaring the positions of a relation-bearing structure, the kinds of values admitted at those positions, and the reference or by-value mode used when a filled instance stores content.

**First useful move.** For the current relation-bearing value, name the governing pattern and write each relevant position as a `SlotSpec = <SlotKind, ValueKind, refMode>`. Then say whether the filled slot instance stores a value by value or stores a reference of a `RefKind`.

**What goes wrong if missed.** Teams treat "role", "argument", "field", "port", "parameter", "endpoint", "holder", "target", "source", "interface", or "ref" as if the word already said whether it is a position, a filler kind, a filled reference, a described object, or a neighboring relation. This creates duplicate ontology: the same project situation becomes a role in one pattern, an interface in another, a slot in a third, and an evidence relation in a fourth.

**What this buys.** A relation-bearing pattern can say exactly which slots it has, what may fill each slot, how filled instances point to or embed those fillers, and which neighboring pattern governs any role, capability, method, work, evidence, status, publication, or interface claim that appears near the relation.

**Not this pattern when.** Do not use `A.6.5` as a generic relation ontology, as a second `U.Signature`, as an interface root kind, as a role ontology, or as a universal wording-repair pattern. Use the direct governing pattern when the current question is relation identity (`A.6.P` or a relation-specific pattern), signature declaration (`A.6.0`), role value (`A.2`), role assignment (`A.2.1`), evidence use (`A.10`, `B.3`, `G.6`), status use (`F.10`), publication or view use (`E.17*`), module interface (`A.6.M` and architecture patterns), functional port or functional structure (`A.6.F`, `E.18`, architecture patterns), or wording-use triage (`E.10`, `E.10.ARCH`, `A.6.RSIR`).

### A.6.5:1 - Problem frame

FPF relies on n-ary relations and operators throughout the corpus: episteme slot relations, role assignments, method and method-description signatures, evidence-use relations, status-use relations, service-access descriptions, interface specifications, architecture structures, view relations, transformation-flow structures, and formal-substrate declarations.

The same local phrase can hide three different things:

1. a named position in one relation-bearing structure;
2. the kind of value admitted at that position;
3. the reference or embedded value placed in one filled relation instance.

For example, `EntityOfConcernSlot`, `U.Entity`, and `entityOfConcernRef` are not three spellings for one thing. The first names a slot position. The second names a filler kind. The third is a filled reference field in an instance. When these layers are blurred, substitutions, retargetings, interface claims, role assignments, evidence-use relations, and episteme morphisms become hard to review.

The governing distinction is important: `A.6.5` supplies relation-slot discipline. It does not decide what a relation is in general, and it does not replace `U.Signature`. Relation identity remains with the pattern that governs the relation. Signature identity remains with `A.6.0`. `A.6.5` gives both of them a disciplined way to talk about positions and fillers.

### A.6.5:2 - Problem

Without a shared slot discipline, FPF texts fall into recurring category errors.

1. **Slot, value, and reference are treated as one object.** A field such as `entityOfConcernRef` is read as the slot, the described object, and the stored reference at the same time.
2. **Kernel kinds are used as slot names.** Writers say "the `U.Holon` of this relation" when they mean a local slot whose filler has ValueKind `U.Holon`.
3. **Role words become argument-position words.** "The role of the subject" or "provider role in the relation" may mean an actual `U.Role`, a local SlotKind, an evidence-use position, a service-access relation, or ordinary prose.
4. **Reference suffixes drift.** A `*Ref` token is sometimes used for a value kind, sometimes for a field, and sometimes for a slot. Downstream readers cannot tell what is being retargeted.
5. **Substitution rules cannot be localized.** If a text cannot say which SlotKind stays fixed and which ValueKind remains compatible, "replace X with Y" becomes a hand-waved compatibility claim.
6. **Interface and port wording overgeneralizes.** "Interface" may mean module interface, signature, port, protocol, API description, service-access package, or boundary claim bundle. A.6.5 helps declare slots inside those values, but it does not create a generic `U.Interface`.
7. **Evidence and status relations are mistaken for roles.** An episteme used as evidence, a standard used as a requirement, or a publication used as a status source is treated as a `U.RoleAssignment` case even though the current claim is evidence use, source use, publication use, assurance use, or status use.

The practical failure is simple: local convenience produces global incoherence.

### A.6.5:3 - Forces

| Force | Tension |
|---|---|
| Simplicity vs expressiveness | Practitioners need a small vocabulary, but relation-bearing structures must still expose positions, filler kinds, reference modes, and change operations. |
| Reuse vs false unification | The same SlotSpec discipline should serve epistemes, signatures, role assignments, evidence-use relations, status-use relations, interfaces, services, and transformation-flow structures without pretending those relations are one relation kind. |
| Role ontology vs slot discipline | `U.Role` must stay a real work-facing role value, while relation positions must not be named as roles merely because they participate in a relation. |
| Description boundary vs instance filling | A pattern may describe a slot relation, while a project instance fills it. Description, publication, and filled relation values must stay distinct. |
| Tool alignment vs FPF ontology | Programming, database, type-system, and API practices already use parameters, fields, references, and updates, but FPF must recover their kinds before borrowing their words. |
| Binding-time clarity vs metaphor | "Early binding", "late binding", "assignment", and "update" are useful only when the affected link is named: name to slot, slot to content, or reference to referent. |

### A.6.5:4 - Solution

`U.RelationSlotDiscipline` says that a relation-bearing structure with named positions uses `SlotSpec` declarations. A `SlotSpec` separates the local position, the admitted filler kind, and the instance reference mode.

```text
SlotSpec := <SlotKind, ValueKind, refMode>
refMode := ByValue | RefKind
```

This is a discipline over relation-bearing structures. It is not the identity of the relation itself. It is not a new kind for every possible field name. It is not a publication form.

#### A.6.5:4.1 - SlotKind, ValueKind, and RefKind

**SlotKind** names one position in one relation-bearing structure. It is structural and local to a governing relation, operator, record, signature vocabulary item, episteme slot relation, role assignment, interface specification, or other signatured bundle. Examples include `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `EvidenceTargetClaimSlot`, `RoleValueSlot`, `AssignmentWindowSlot`, `ServiceEndpointSlot`, and `DatasetSlot`.

**ValueKind** names what kind of value may fill that position. Examples include `U.Entity`, `U.Holon`, `U.System`, `U.Role`, `U.Method`, `U.MethodDescription`, `U.Episteme`, `U.ClaimGraph`, `U.Viewpoint`, `U.Characteristic`, and `U.ReferenceScheme`. A ValueKind is governed by its own pattern. It does not become a SlotKind because it fills a slot.

**RefKind** names how a filled relation instance points to a value when the value is not embedded by value. Examples include `U.EntityRef`, `U.HolonRef`, `U.SystemRef`, `U.RoleRef`, `U.MethodRef`, `U.EpistemeRef`, `U.ViewpointRef`, and `U.CharacteristicRef`. A RefKind is about references, not about the value itself.

**Slot instance** is the particular position in one filled relation instance. **Slot content** or **slot filler** is what the filled instance stores at that position. The slot content is either an embedded value of the ValueKind or a reference of the RefKind. If it is a reference, resolving it gives a referent value or editioned referent.

#### A.6.5:4.2 - Well-formed SlotSpec discipline

For each named position in a relation-bearing structure:

```text
Well-formedness constraint A6.5-S1 (SlotSpec completeness):
  each SlotSpec has exactly one SlotKind, exactly one ValueKind, and exactly one refMode.

Well-formedness constraint A6.5-S2 (SlotKind locality):
  SlotKind is interpreted relative to the governing relation-bearing structure.

Well-formedness constraint A6.5-S3 (ValueKind preservation):
  a substitution at a slot preserves the SlotKind and uses a filler whose kind is the declared ValueKind or an admitted subkind.

Well-formedness constraint A6.5-S4 (RefKind honesty):
  when refMode is a RefKind, the slot content is a reference value, not the referent itself.
```

A `U.Signature` uses this discipline when its vocabulary declares an n-ary relation or operator. The SlotSpecs live inside the relevant vocabulary item. They do not add a fifth row to the `A.6.0` Signature Block and do not move operational guards from `A.6.1` or method and work patterns into the signature.

#### A.6.5:4.3 - Naming discipline for `*Slot` and `*Ref`

Use `*Slot` only for SlotKinds. Do not use `*Slot` for ValueKinds, RefKinds, concrete fields, or publication labels.

Use `*Ref` only for RefKinds or fields whose type is a RefKind. Do not use `*Ref` for SlotKinds or for the value itself.

ValueKind names do not carry `*Slot` or `*Ref`. If a current source name violates this rule, recover the intended kind before renaming. The repair may split one old token into a SlotKind, a ValueKind, and a RefKind or field.

Do not use `Role` as the head noun for a SlotKind. `U.Role` is a role value governed by `A.2`. A relation position that admits a `U.Role` filler can be named `RoleValueSlot`; a position filled by a system or acting holon under a role assignment can be named `RoleHolderSlot` or a context-specific refinement. The head remains `Slot`, and the `U.Role` value remains a value.

#### A.6.5:4.4 - Role assignment under slot discipline

`U.RoleAssignment` is a typed assignment relation value for work-facing roles. It can be expressed with SlotSpecs without reducing roles to slots.

Core SlotSpecs for a work-facing role assignment include:

| SlotKind | ValueKind | refMode | Meaning |
|---|---|---|---|
| `RoleHolderSlot` | `U.System` or acting holon admitted by the governing work or method pattern as system-like performer | `RefKind` selected by the governing context | The system or admitted acting holon that holds the role in this bounded context. |
| `RoleValueSlot` | `U.Role` | `RefKind` or by-value local role value | The role value being assigned. |
| `BoundedContextSlot` | `U.BoundedContext` | `RefKind` or by-value context descriptor | The context in which the assignment has meaning. |
| `AssignmentWindowSlot` | temporal window value governed by the temporal pattern current in the context | `ByValue` or selected RefKind | The time window for the assignment claim. |
| `AssignmentJustificationSlot` | source, decision, gate, or claim relation governed by its direct pattern | selected by the direct pattern | The relation that justifies the assignment when such justification is current. |

Direct work-role patterns may add work-role qualifier slots. Evidence-use, source-use, publication-use, standard-use, requirement-use, assurance-use, and status-use relations do not become RoleAssignment slots merely because their prose says "role of the evidence" or "role of the standard". Those uses are governed by their direct patterns.

`RoleEnactment` is not introduced here as a root ontic. When a named fact is needed, use `RoleEnactmentFact` for the derived fact that a `U.Work` occurrence was performed under a specific `U.RoleAssignment`, or write the direct relation such as `Work.performedBy = RoleAssignment`.

#### A.6.5:4.5 - Evidence-use and status-use relations are not work roles

An episteme may be used as evidence for several claims. This creates evidence-use relation instances, not several roles held by the episteme.

Typical evidence-use SlotKinds include:

| SlotKind | ValueKind | Meaning |
|---|---|---|
| `EvidenceEpistemeSlot` | `U.Episteme` or admitted evidence episteme species | The episteme being used as evidence. |
| `EvidenceTargetClaimSlot` | claim value governed by the claim pattern current in context | The claim to which the evidence-use relation is addressed. |
| `EvidenceClaimGroundingHolonSlot` | `U.Holon` when the target claim needs grounding | The holon in which the target claim is grounded when current. |
| `EvidenceClaimScopeSlot` | scope value governed by the claim or evidence pattern | The scope for the evidence-use relation. |
| `EvidencePolaritySlot` | confirming, rebutting, undercutting, or another locally governed polarity value | The direction of bearing on the target claim. |
| `EvidenceRelevanceWindowSlot` | temporal or freshness window value | The window in which the evidence-use claim remains usable. |
| `EvidenceAssuranceUseSlot` | assurance-use relation or assurance input value | The assurance use when current. |
| `EvidenceWeightModelSlot` | weight, confidence, or calculus value governed by the evidence or assurance pattern | The model used to aggregate or compare evidence when current. |

Status-use relations likewise name the status bearer, status value, status scope, status window, and use relation under the direct status or assurance pattern. They do not create status roles for epistemes.

#### A.6.5:4.6 - Interface, port, and signature wording

`A.6.5` is often needed when a source says "interface", "port", "endpoint", "API", "protocol", or "connector". These words do not select one FPF kind by themselves.

Recover the current EntityOfConcern first:

| Source cue | Common recovery |
|---|---|
| interface between modules | module-interface claim, boundary claim, port relation, signature, protocol, or evidence of conformance under `A.6.M` and architecture patterns |
| port in a functional description | functional port or transformation-flow structure under `A.6.F`, `E.18`, or architecture patterns |
| API | software API description, service-access description, protocol, publication form, or boundary claim bundle |
| endpoint | relation endpoint, service endpoint, network endpoint, evidence target, claim target, or ordinary source label |
| signature | `U.Signature` under `A.6.0`, using A.6.5 SlotSpecs for n-ary vocabulary items |

After the governing EntityOfConcern is selected, use `A.6.5` only to state the SlotSpecs inside that value. Do not mint a generic `U.Interface` or erase interface language when it is the ordinary engineering recognition cue.

#### A.6.5:4.7 - Slot operation lexicon

Use slot-operation words by the link they affect.

| Operation word | Affected link | Use |
|---|---|---|
| bind or rebind | identifier or name to SlotKind, slot instance, or language-level value | Use for name binding. Do not use `bind` as a synonym for writing slot content. |
| fill | slot instance to slot content | Use as the generic verb for providing content to a slot instance. |
| initialize | first fill | Use when the slot instance previously had no content. |
| assign, set, or update | subsequent slot-content replacement | Use when replacing content in an already filled slot instance. |
| retarget | reference slot update, preserving SlotKind and ValueKind | Use when replacing one reference with another reference to another referent. |
| substitute | typed replacement with explicit compatibility claim | Use when the important claim is ValueKind or admitted-subkind compatibility. |
| resolve or dereference | reference to referent | Use when a reference is mapped to the value or editioned referent it points to. |
| revise or issue a re-edition | referent content change under edition discipline | Prefer these words to vague mutation when the referent itself changes across editions. |
| pass | parameter slot filling at a call or service boundary | Use only when the current relation is a method, service, protocol, or call boundary with parameter slots. |

Avoid person metaphors such as `occupant` for slot content. Use `slot content` or `slot filler`. If a local Plain register uses a metaphor, it cannot carry FPF-governed role, evidence, or status meaning.

#### A.6.5:4.8 - Binding time and currentness of slot operations

"Early binding" and "late binding" are admissible only after the affected link is named.

Use:

- early or late name binding for identifier-to-slot or identifier-to-value links;
- early or late slot filling for when a slot instance receives content;
- eager or lazy resolution for when a reference is resolved to a referent;
- dynamic dispatch only when a method or operation selection relation actually uses runtime context to select the invoked operation.

If the text does not say which link is affected, keep the phrase ordinary or repair it before use.

### A.6.5:5 - Archetypal Grounding

**System case: refrigerator functional architecture.** A refrigerator functional diagram may describe a transformation-flow structure: compressor, condenser, expansion valve, evaporator, sensors, controller, and refrigerant flow. An interface or port in that description is not automatically a generic interface kind. If the current EntityOfConcern is the functional port between evaporator and compressor, recover the functional or transformation-flow relation first, then declare SlotSpecs such as `UpstreamTransformationSlot`, `DownstreamTransformationSlot`, `TransferredMediumSlot`, `BoundaryConditionSlot`, and `ObservedCharacteristicSlot`. The refrigerant, components, controller, and temperature characteristic remain fillers governed by their own patterns.

**Episteme case: model evaluation result.** A `ModelEvaluationResult` episteme can use `EntityOfConcernSlot` with ValueKind `U.Method`, `DatasetSlot` with ValueKind `U.Entity`, `TargetCharacteristicSlot` with ValueKind `U.Characteristic`, `GroundingHolonSlot` with ValueKind `U.Holon`, and `ClaimGraphSlot` with ValueKind `U.ClaimGraph` by value. Retargeting `DatasetSlot` from `Dataset_A` to `Dataset_B` changes a reference filler. Editing the threshold inside `ClaimGraphSlot` changes embedded claim content. Those are different operations.

**Role case: inspection work.** A maintenance context assigns `InspectorRole` to `Robot_7` for a window. The role assignment relation can fill `RoleHolderSlot = Robot_7`, `RoleValueSlot = InspectorRole`, `BoundedContextSlot = MaintenanceLine_A`, and `AssignmentWindowSlot = from 2026-06-15T09:00 to 2026-06-15T11:00`. The robot's capability remains `U.Capability`, the inspection method remains `U.Method` or `U.MethodDescription`, the planned inspection remains `U.WorkPlan`, and the performed inspection remains `U.Work`.

**Evidence case: one report for two claims.** One report episteme can be used as evidence for Claim A and Claim B. The episteme is not assigned two evidence roles. FPF creates two evidence-use relations with different `EvidenceTargetClaimSlot` fillers and any distinct scope, polarity, relevance-window, or weight-model fillers.

### A.6.5:6 - Bias-Annotation

This pattern has a typed-structure bias: it prefers explicit positions and filler kinds over conversational shorthand. That bias is intentional because relation-bearing FPF prose must remain reusable across epistemes, signatures, roles, interfaces, methods, evidence, status, and architecture.

This pattern also has an episteme-example bias because `C.2.1` is the mature precedent for slot relation discipline. The Solution generalizes beyond epistemes and explicitly includes work-facing role assignments, evidence-use relations, status-use relations, interfaces, ports, and transformation-flow structures.

The anti-bias guard is that `A.6.5` never makes description or publication the center unless the current EntityOfConcern is itself a description or publication relation. It starts from the relation-bearing EntityOfConcern and only then describes how its slots may be specified or published.

### A.6.5:7 - Conformance Checklist

1. **SlotSpec completeness.** Every FPF-governed n-ary relation, operator, record, or signature vocabulary item introduced by the pattern names SlotKind, ValueKind, and refMode for each governed position.
2. **SlotKind locality.** SlotKind is interpreted relative to the governing relation-bearing structure; the same label does not float as a universal kind without a governing pattern.
3. **ValueKind separation.** ValueKinds remain governed by their own patterns and do not inherit `*Slot` or `*Ref` suffixes.
4. **RefKind honesty.** A `*Ref` name denotes a reference kind or a field typed by a reference kind, not the referent itself.
5. **Role boundary.** Role-valued slots may admit `U.Role` fillers, but SlotKinds are not roles and role labels do not create capability, method, status, evidence, or work.
6. **RoleAssignment boundary.** A work-facing `U.RoleAssignment` uses core SlotSpecs for holder, role value, bounded context, and assignment window; evidence-use and status-use relations are not folded into RoleAssignment.
7. **Evidence and status direct-pattern use.** Epistemes used as evidence, sources, standards, requirements, definitions, explanations, publications, status bearers, or assurance inputs are governed through direct evidence-use, source-use, publication-use, status-use, or assurance-use patterns, not through `U.RoleAssignment` for epistemes.
8. **Interface recovery.** Interface, API, port, protocol, connector, or endpoint wording is first recovered to its governing EntityOfConcern; `A.6.5` supplies only the SlotSpecs inside the recovered value.
9. **Operation verb discipline.** Slot changes use bind, fill, initialize, assign, retarget, substitute, resolve, revise, re-edition, or pass according to the link being changed.
10. **No generic relation replacement.** A pattern does not cite `A.6.5` as the governing source for relation identity, evidence authority, assurance, gate passage, method admission, work execution, or publication truth.

### A.6.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
|---|---|---|
| `RoleSlot` as a generic relation position | It can hide whether `role` means `U.Role`, argument position, provider relation, evidence use, or ordinary prose. | Name the actual SlotKind, such as `RoleValueSlot`, `RoleHolderSlot`, or a domain slot, and name the ValueKind separately. |
| Source label `EvidenceRole` for an episteme | It gives an episteme a work-facing role assignment it does not have. | Use an evidence-use relation with `EvidenceEpistemeSlot`, `EvidenceTargetClaimSlot`, and related slots. |
| "The API role is provider" | API, provider, role, promise, service, and interface may be different values. | Recover API description, provider role assignment, service promise relation, or interface specification under direct patterns. |
| `EntityOfConcernRef` used as a value kind | A reference field is treated as the described object. | Split `EntityOfConcernSlot`, ValueKind, and `entityOfConcernRef` or equivalent RefKind field. |
| "Late binding" without the affected link | The reader cannot tell whether name binding, slot filling, resolution, or method dispatch is late. | Rewrite as late name binding, late slot filling, lazy resolution, or dynamic dispatch with the governing relation named. |
| `interface` repaired by deleting the word | The useful engineering recognition cue is lost. | Keep interface as ordinary cue, then recover the governing EntityOfConcern and its SlotSpecs. |

### A.6.5:9 - Consequences

`A.6.5` adds a small amount of explicit metadata to relation-bearing structures. The payoff is that substitutions, retargetings, evidence-use distinctions, role-assignment boundaries, interface claims, and episteme morphisms become reviewable.

It also prevents ontology overgrowth. A value filling a slot does not become a new kind because it is used in that slot. Conversely, a slot label does not become the value. This is the same discipline that keeps `U.Episteme` compact in `C.2.1` and keeps `U.Role` compact in the role `ontologicalNeighborhood`.

The cost is naming care. Authors must recover the current governing pattern before accepting a slot name. That is cheaper than maintaining several local ontologies for the same project situation. Reopen the governing pattern, not `A.6.5`, when a current case depends on relation identity, evidence authority, status meaning, role ontology, method admission, work execution, publication use, architecture semantics, or another value that SlotSpec discipline only references.

### A.6.5:10 - Rationale

FPF needs relations that are strong enough for engineering use but light enough for cross-domain pattern work. The SlotKind, ValueKind, and RefKind separation gives FPF a compact relation-position discipline without turning every relation into a new formal calculus.

The key design choice is modularity. `A.6.5` is central because many patterns need SlotSpecs. It remains narrow because relation identity, evidence authority, status meaning, role ontology, method admission, work execution, publication use, and architecture semantics belong to their own patterns.

The role decision is especially important. If every slot position is called a role, `U.Role` loses its work-facing meaning. If every episteme used as evidence gets an evidence role, FPF grows a second role ontology for epistemes. `A.6.5` keeps both errors visible: a role may fill a slot, but slot position labels do not create alternate ontology.

### A.6.5:11 - SoTA-Echoing

| Practice line | FPF adoption |
|---|---|
| Typed records, row-polymorphic data, and effect-row practice distinguish field labels from field types and from effects or resources. | Adopt the structural lesson: position labels and filler kinds are separate. Adapt it into SlotKind, ValueKind, and RefKind so the same discipline applies to epistemes, roles, evidence-use relations, interfaces, and transformation-flow structures. |
| Dependent and refinement type practice makes admissible values depend on declared indices, contexts, and predicates. | Adopt the need to expose the admissibility predicate. In FPF, ValueKind compatibility and context-local subkind admission are named rather than hidden in prose. |
| Optics and lens practice manipulates focused positions in larger structures under composition laws. | Echo the focus-position idea: SlotKind names the focused position; ValueKind names the admitted filler; RefKind says whether the focused value is embedded or reached through a reference. |
| Database, protocol, and API schema practice separates schema declarations from records, messages, and runtime handling. | Adopt the declaration-instance separation. A SlotSpec describes a relation position; a filled relation instance, API call, evidence-use relation, or work occurrence is not the SlotSpec itself. |
| Contemporary architecture and interface practice treats ports, APIs, protocols, and connectors as heterogeneous description and boundary constructs rather than one universal interface type. | Adapt this by refusing generic `U.Interface`; recover the governing EntityOfConcern first, then use SlotSpecs only inside that recovered value. |

### A.6.5:12 - Relations

`A.6.0` governs `U.Signature`; `A.6.5` supplies SlotSpec discipline for n-ary vocabulary items inside signatures.

`A.6.P` governs qualified relation precision restoration; `A.6.5` supplies the slot discipline consumed by relation-restoration patterns.

`E.24` governs ontic introduction. `A.6.5` is one reusable discipline used by ontic introductions, but it does not create a new ontic every time a slot label appears.

`C.2.1` is the mature precedent for slot relation discipline in epistemes. `A.6.5` keeps its `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, and `ReferenceSchemeSlot` usable across morphisms and publication patterns.

`A.2`, `A.2.1`, `A.2.5`, `A.2.7`, and `A.15` govern role values, role assignments, role-state checks, role relation structure, and role-method-work alignment. `A.6.5` only expresses the SlotSpecs of relations that include role values or role assignments.

`A.10`, `B.3`, `G.6`, `C.28`, and `F.10` govern evidence-use, assurance, causal-use, provenance, and status-use relations. Evidence-role and status-role source wording is governed through typed evidence-use, assurance, causal-use, provenance, or status-use relations, not through work-role assignment.

`A.6.M`, `A.6.F`, `E.18`, `C.30.TFS-REL`, and architecture patterns govern interface, port, functional, and transformation-flow cases. `A.6.5` applies only after the governing EntityOfConcern has been recovered.

`E.10`, `E.10.ARCH`, `F.18`, and `A.6.RSIR` govern wording-use triage and naming. They require each relation, signature, interface, role, slot, capability, method, function, concern, or interest word to be resolved under its direct governing pattern, using `A.6.5` when relation-position discipline is the current issue.

### A.6.5:End

