## A.3.1 - U.Method: Context-Defined Way of Doing

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### A.3.1:1 - Problem frame

Use this pattern when a project needs to say **how something is done in principle** without prematurely treating that method or practice claim as a document, program, workflow diagram, plan, run log, role assignment, capability statement, mechanism claim, cultural tradition, discipline position, or mathematical-model claim before those positions are recovered.

Typical moments:

* a team says "the method is the code", "the process is the BPMN", "the workflow is the evidence", or "the solver model is the operation";
* a practice, procedure, protocol, proof script, optimization model, control strategy, or recipe is intended for reuse across many runs;
* two descriptions look different but may describe the same way of doing;
* a graph, query, table, dashboard, checklist predicate, or mathematical representation is being interpreted as if it were an instruction sequence;
* work planning, dated work, method description, formal substrate, mechanism, role assignment, cultural-evolution, discipline, and evidence are starting to collapse into one vague "method" or "practice" word.

**Primary EntityOfConcern.** The `EntityOfConcern` is the `U.Method`: the context-local semantic way of doing a kind of transformation or enactment. `U.Method` is a non-agentive holon kind: methods can have submethods, compose into whole methods, and participate as submethods of larger methods. This does not make a method an actor, a method description, a work plan, or a dated work occurrence. A step label or step description is not a method part unless the recovered object is itself a `U.Method`.

**First useful move.** Name the context-local way of doing, the transformation or enactment it is about, and the kind of governed object or structure whose selected state or condition a future enactment is intended to change or preserve. The method remains this pattern's primary `EntityOfConcern`; this semantic statement establishes no planned assignment, actual participant, actual transformation, or result.

**What goes wrong if missed.** A diagram starts authorizing work, a query plan starts looking like performed work, a program starts looking like proof of operational success, or a graph path starts looking like a route that something followed.

**What this buys.** The project can reuse, compare, describe, plan, enact, and audit a way of doing without confusing the method with its descriptions, runs, mechanisms, mathematical substrates, evidence relations, gates, or authority claims.

**Not this pattern when.** If the current claim is a method description, work plan, dated work occurrence, evidence relation, source relation, mechanism declaration, mathematical-lens use, gate decision, authority claim, or publication-use relation, use the pattern that governs that claim and link it back to the `U.Method` only when the relation is current.

### A.3.1:2 - Problem

Without a current `U.Method` distinction, FPF cannot repair method-like wording cleanly. Texts then slide among several different claims:

1. **Description as method.** A SOP, code repository, proof script, BPMN diagram, SQL query, solver model, or protocol is treated as the method itself.
2. **Plan or run as method.** A calendar plan, access plan, run log, telemetry trace, or work-result record is called the method.
3. **Mechanism or formal substrate as method.** A mathematical object, formal substrate, mechanism declaration, causal model, or control structure is used as if it already selected the way of doing work.
4. **Role or capability leakage.** Named people, organizations, teams, permissions, or capability thresholds are baked into the method instead of being kept in role assignment, authorization, capability, or gate patterns.
5. **Programming-paradigm overread.** Imperative, functional, logical, constraint, object-centric event, or effect-handler wording is taken as a direct ontology of work rather than one possible description or representation of a way of doing.

The practical harm is fragile reliance. Changing a publication looks like changing the method; a run error looks like method invalidation; a mechanism declaration starts authorizing work; and a dashboard cue starts acting like evidence or permission.

### A.3.1:3 - Forces

* A method has enough identity stability to support comparison, reuse, teaching, improvement, and audit across many runs.
* Work still happens in dated situations with exact performer assignments, actual participants, resource uses, conditions, and separately governed effects; a method statement establishes none of those occurrence-side facts.
* Method descriptions can be executable, formal, graphical, procedural, declarative, or hybrid; publication form alone does not decide the method ontology.
* Mechanisms and mathematical substrates often make a method explainable or constrained enough to rely on, but the mechanism claim and the method claim still answer different project questions.
* A useful method statement remains applicable to welding, clinical triage, proof construction, optimization, agent orchestration, lab protocols, software execution, and organizational work without making software notation the default model of method.

### A.3.1:4 - Solution

`U.Method` is the **context-defined semantic way of doing a kind of transformation or enactment**.

**Local method mantra.** *Name the reusable way of doing; bound its context and transformed entity or structure; state its preconditions and intended effects; keep its descriptions, plans, work occurrences, and mechanisms in their own relations; then use the direct pattern for every stronger claim.* This compact formula keeps the Solution in attention. It is not a work order, a `U.WorkPlan`, a dated enactment, or a `DemonstrativeUnfoldingSlice@Context`.

It is a non-agentive holon kind. Part methods can be selected, bounded, ordered, joined, adapted, and hidden or exposed through method interfaces to form a whole method with whole-level preconditions, effects, invariants, constraints, and assurance hooks. The whole method may then be used as a part method in a larger method.

It is not the text, code, diagram, model, plan, run, role, capability, or evidence relation that may be associated with that way of doing. A `U.Method` is:

* **context-defined**: its identity, generic participant meanings, conditions, intended effects, and bounds are interpreted inside a `U.BoundedContext`;
* **semantic**: it is the way of doing that descriptions denote and work may enact;
* **transformation-facing**: it concerns a possible or intended transformation or enactment and the intended effects or preserved conditions, including physical, informational, organizational, mathematical, or hybrid cases; it does not identify an actual change or produced result;
* **description-independent**: one method may be described by several `U.MethodDescription` epistemes;
* **run-independent**: one method may be enacted by many Work occurrences admitted under `U.Work`;
* **assignment-independent**: method admission conditions may name role kinds or capability-fit conditions, but named holders and dated assignments belong elsewhere;
* **participant-semantic**: it may state generic participant meanings and method-side applicability without declaring `RelationSignature` SlotSpecs, `OperationAlgebra` argument or result positions, planned fillers, or actual participants.

The primary repair action is not to replace the word "method" or "practice" with one better word. In ordinary source speech, `practice` often works as a synonym for method-like wording, but it can also name enacted work, role arrangement, discipline, tradition, source label, or cultural-evolution material. Recover the current governed object and claim position first:

| If the text is really about... | Govern it as... |
| --- | --- |
| semantic way of doing | `A.3.1 U.Method` |
| relation or composition among methods, method families, or local method expressions | `A.3.1` with `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern such as `B.1.5` when current; algebraic or graph notation is only `C.29` lens or method-description representation |
| description of that way of doing: SOP, program, proof script, solver model, protocol, diagram, process model, recipe text | `A.3.2 U.MethodDescription` |
| source phrase such as practice, technique, school, tradition, or local method label whose current object is unclear | recover the claim kind first through `E.10` and this table; use `A.1.1` when the phrase names a bounded context, and use `C.36.P` when the cultural-evolution, tradition, style, canon, recognition, selection, or mediation context is current |
| selected formal substrate or mathematical declaration | `A.6.0` and `C.29` when mathematical-lens use is current |
| mechanism declaration or realization relation | `A.6.1` and `E.20` |
| role assignment, role relation, responsibility allocation, or holder eligibility hidden under a practice or method phrase | `A.2`, `A.2.1`, `A.2.7`, and `A.15` as applicable |
| planned dated work or authorization to prepare work | `A.15.2 U.WorkPlan` plus the relevant gate, authority, or commitment pattern |
| dated work occurrence or run; trace, log, or result record | `A.15.1` for the Work occurrence admitted under `U.Work`; the exact evidence, source, measurement, evaluation, production, delivery, acceptance, or other direct pattern for the separate record or result, linked to work only by an obtaining relation |
| field-level discipline, bounded context, community tradition, canon or memory episteme, recognition or selection regime, mediation system, variant set, or cultural-evolution intervention | `A.1.1`, `C.20`, `C.36`, `C.36.P`, `F.17`, `F.18`, `F.9`, `C.18`, `C.19`, `G.5`, or `G.11` according to the recovered claim |
| evidence or provenance relation for a claim | `A.10` |
| graph path, path slice, flow valuation, state predicate, query, table, dashboard, publication face, or pattern relation overread as a method or work sequence | `C.2.P.DR` first, then the direct governing pattern named by the recovery |

#### A.3.1:4.0a - Strategy wording by current position

Treat `strategy` as ordinary source wording until the current position is recovered. Do not mint `U.Strategy`.

When the wording names a context-local reusable way of deciding or acting, the governed value is `U.Method`. A clinical treatment strategy, manufacturing setup strategy, search strategy, or negotiation strategy is a method when it states the reusable way of doing and its preconditions, effects, and bounds.

When a protocol, playbook, program, diagram, or prose passage describes that way, the governed value is `U.MethodDescription`. Reusable strategizing can itself be a `U.Method`; a dated strategy workshop, search episode, or planning session is a Work individual admitted under `U.Work` when its occurrence basis is grounded.

When the current claim selects candidates under criteria or policy pins, use the selector relation and policy values governed by `A.19.SelectorMechanism` and G.5. The word `strategy` does not replace `CriteriaSlot`, `PolicyHooksRef`, `InsertionPolicyRef`, `EmitterPolicyRef`, `PromotionPolicy`, or the emitted `SelectorOutcome` when one of those is the actual claim.

Ordinary quoted or explanatory strategy wording may remain when no FPF-governed method, description, work, selector, or policy claim is being made. The repair is complete when the current position and direct governing pattern are recoverable, not when every occurrence has been replaced by one preferred word.

#### A.3.1:4.1 - Thin first-use method identification


Use the cheapest apparatus that preserves the current distinction:

1. **Ordinary conversational use.** Apply the local mantra, name the method, context, transformed entity or structure, preconditions, effects, and nearest boundary, then stop. Materialize no record when feedback is immediate and no later use relies on replay.
2. **Reliance-bearing use.** Materialize the Plain identification aid below when comparison, transfer, planning, audit, automation, delayed feedback, expensive reversal, or another named use relies on recovering the method identity and its boundary.
3. **Structure-bearing use.** Select a `U.Structure` under `A.22`, designated here as `MethodRelationStructure@BoundedContext`, or open `B.1.5` or another direct composition pattern only when the receiving use relies on relations among methods, method parts, families, descriptions, selectors, or work-facing uses being explicit.

Moving upward must answer a named reliance need. More fields do not make the method real, improve it, authorize its use, or establish that work occurred.

For the reliance-bearing level, state only the fields needed to keep the method claim from collapsing into a description, plan, run, mechanism, or evidence relation. The following is a Plain identification aid, not a record kind, ontic, serialization, or mandatory form:

```text
Method identification aid:
  MethodRef:
  BoundedContext:
  TransformationOrEnactmentKind:
  TransformedEntityOrStructureRef:
  Preconditions:
  IntendedEffectsOrPreservedConditions:
  CurrentMethodDescriptionRefAndEdition:
  WorkRelationWhenCurrent:
  IdentityBasisRelationsAndDirectPatterns:
  QualificationWindow:
  ReviewWhen:
  ClaimBoundary:
```

`ClaimBoundary` names the nearest stronger claim that is not carried by this method statement, such as work authorization, performed work, evidence for success, mechanism declaration, or formal-substrate adequacy. It is a boundary field, not a place to repeat every neighboring pattern.

For reliance-bearing use, every identity-basis entry names one exact relation together with the pattern governing that relation; generic `source`, `support`, or `evidence` wording is not a replay basis. `QualificationWindow` states the context, method variant, and time or edition range for which the identification is being relied on. `ReviewWhen` names which change in context, preconditions, effects, bounds, transformed entity or structure, description relation, or work-facing acceptance relation would make that identification unsafe to reuse without review.

#### A.3.1:4.1a - Closure and bounded non-use

A method identification closes positively for the current use when the context-local way of doing, bounded context, transformation or enactment kind, `A.3.4 transformedEntityOrStructure`, applicable preconditions, intended effects or preserved conditions, and nearest `ClaimBoundary` are recoverable. Add a method-description relation or work relation only when the receiving use relies on a particular description or enactment family.

Close by bounded non-use when the current claim is only a description, plan, dated work occurrence, mechanism, selector result, role relation, evidence relation, publication use, or ordinary quoted wording. If the available material cannot distinguish those positions, keep the source wording as an unresolved cue and stop; do not infer a `U.Method`. A later plan, work occurrence, or evidence result does not keep the method identification open unless it changes a relation on which that identity relied.

#### A.3.1:4.2 - Method and mechanism settlement

Do not decide the method and mechanism question by vocabulary. When a source expression or project concern appears to name changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For ordinary use, keep the local question thin: does the current claim state a `U.Method`, the context-local way of doing a transformation or enactment? If the source label also raises mechanism, formal-substrate, work-plan, dated-work, role-assignment, cultural-evolution, discipline, evidence, source, gate, result, publication, or temporal claims, keep those governed objects linked only by exact direct relations and apply their own patterns.
For a method question, recover one reusable way of doing a transformation or enactment under stated applicability. For a mechanism question, recover one reusable declaration episteme whose semantic content states its exact operation family, direct subject and range fields, operation algebra, laws, admissibility predicates, and Applicability. These are different governed objects. A shared source expression or one operation name does not establish dual typing.

Use separate relation questions for changes and uses around the mechanism:

| Current question | Governing pattern | Recoverable relation or value |
| --- | --- | --- |
| What reusable way of doing is intended or enacted? | `A.3.1 U.Method` | transformation or enactment kind, generic participant meanings, preconditions, intended effects or preserved conditions, bounds, and direct description or work relations only when current |
| What episteme describes that way of doing? | `A.3.2 U.MethodDescription` | exact method described, representation form, parameters, acceptance criteria, edition, and applicable source-use relation |
| What law-governed operation family is declared? | `A.6.1 U.Mechanism` | `EntityOfConcernRef`, effective `U.ReferenceScheme`, direct subject and range fields, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, Applicability, and optional `SignatureManifest` |
| What relation refines, extends, or equates two mechanism declarations? | the exact direct relation in A.6.1; C.29 when mathematical preservation is claimed | exact declaration endpoints, scope, obtaining condition, and preserved or changed semantic content |
| What cross-context sense correspondence is current? | `F.9` | exact `SenseCell` endpoints, Bridge kind, direction, `CL`, loss, and admitted use; an F.9 Bridge neither changes an effective reference scheme nor establishes governed-value identity |
| What entity realizes one mechanism declaration? | the A.6.1 mechanism-realization relation; A.6.REL when occurrence identity is later reused | exact mechanism, realizing entity, realization scope, obtaining predicate, and derived maximal continuous interval |
| What supports a current claim about admission or realization? | the direct evaluation, measurement, and evidence-use patterns | evaluation occurrence, result, evidence, claim scope, and currentness without adding mechanism content |
| Where should new or revised mechanism meaning be governed? | `E.20` | governing-definition assignment for mechanism meaning, suite, plan, wiring, token continuity, or local non-trigger stop |
| What happened this time? | `A.15.1` for one Work occurrence admitted under `U.Work`, plus the direct pattern for each neighboring claim | performer assignment, enacted method, temporal extent, used resources, and affected referent; actual participants and operation arguments or results require exact direct subject relations or A.6.1 application bindings, while change, production, evaluation, delivery, and acceptance remain separately governed |

A method claim may cite a mechanism declaration. An independently governed selector result or actual A.6.1 application may select a method, and an exact direct constraint relation may constrain one; neither the method nor the mechanism declaration acts merely by being named. An A.6.1 operation declaration may type a method as an argument or result kind only when the exact operation family requires that meaning; an actual application binding then belongs to A.6.1. Neither the declaration nor the binding establishes a planned assignment or a dated work occurrence. A mechanism may declare operations that apply, select, compose, or normalize methods. When both objects are current, state the `U.Method` and `U.Mechanism` claims separately. State a mechanism-realization, cross-context sense Bridge, refinement, evaluation, or evidence-use relation only when that relation also obtains.
Fail closed when neither position can be recovered. Do not repair `practice`, `algorithm`, `program`, `workflow`, `process`, `solver`, `proof`, `recipe`, or `control strategy` to `method` or `mechanism` merely because the replacement sounds more technical.

#### A.3.1:4.3 - Method, MethodDescription, WorkPlan, Work

Keep the four positions separate.

| Position | What it means | Common mistaken substitutes |
| --- | --- | --- |
| `U.Method` | how in principle, inside a bounded context | code, SOP, graph, solver model, proof script, workflow diagram |
| `U.MethodDescription` | an episteme that describes a method in a representation | method semantics, actual run, authority to work |
| `U.WorkPlan` | planned dated work or work preparation | timeless method, generic recipe, proof that work happened |
| `U.Work` | admitted kind for dated Work occurrences; one Work individual is one world-side occurrence | method, plan, result interpretation, evidence relation, or record about the occurrence |

The same solver model, repository, protocol, diagram, or run packet may participate in several claims, but each claim keeps its own governed object and direct relations. A solver-model episteme can be a `U.MethodDescription`; its mathematical representation can expose a formal substrate for `C.29`; a solver run can be a Work individual admitted under `U.Work`; an exact measurement, evaluation, or other result can support another claim only through its governing relation. Those claims are not interchangeable.

#### A.3.1:4.4 - Method statement fields

A useful `U.Method` statement can usually recover these fields in ordinary project language:

| Field | What to name |
| --- | --- |
| Method name | the context-local way of doing |
| Bounded context | the project, discipline, organization, regulatory setting, theory, or operational context that interprets the method |
| Transformation or enactment kind | what changes, is produced, decided, derived, controlled, selected, or maintained |
| Transformed entity or structure | the `A.3.4 transformedEntityOrStructure`: material object, information object, organization, episteme, holon, state, or other governed object whose change or preserved condition matters |
| Preconditions | states already in effect for the method to be applicable |
| Effects or postconditions | what successful enactment is meant to produce or preserve |
| Generic participant and boundary meanings | the kinds of entities, resources, conditions, interfaces, and method-side role-kind or capability-fit conditions that a future enactment may involve, without declaring `RelationSignature` SlotSpecs, `OperationAlgebra` positions, planned fillers, or actual participants |
| Capability acceptance conditions | thresholds or envelopes evaluated against a holder's capability, not baked into the method identity |
| Failure and stop conditions | when the method is blocked, when description revision is current, or when work-entry is inadmissible |
| Description relation | which `U.MethodDescription` epistemes currently describe it |
| Work relation | what Work occurrences admitted under `U.Work` may enact the method and how their separate records cite the description used |

This is not a data schema. It is the minimum recognition field set needed before method-like wording can guide work, evidence, assurance, gates, or planning. Generic participant and boundary meanings remain semantic method content: a reusable operation declaration belongs to `A.6.1`, a reusable direct-relation participant declaration belongs to its `RelationSignature` under `A.6.5`, planned use belongs to `U.WorkPlan`, and actual participation belongs to the exact direct subject relation or A.6.1 application binding.

#### A.3.1:4.5 - Representation and programming-paradigm discipline

A `U.Method` does not depend on an imperative step structure.

Imperative procedures, functional compositions, logical rule sets, constraint models, object-centric event models, effect-handler programs, process diagrams, SQL queries, equality-saturation graphs, proof scripts, and optimization models may all help describe, represent, or analyze a way of doing. Their representation style does not by itself decide whether the current claim position is a method, a method description, a formal substrate, a mechanism, a work plan, work, evidence, or a declarative representation under `C.2.P.DR`.

Use this discipline:

* If the text states the semantic way of doing, use `A.3.1`.
* If the text states the representation that describes that way, use `A.3.2`.
* If the text states a formal object or mathematical representation used to reason, use `A.6.0`, `C.29`, or the direct mathematical pattern.
* If the text states a law-governed operation family or its admissibility predicates, use `A.6.1`; use `E.20` when the current question is where that mechanism meaning is governed.
* If the text states a cross-context `SenseCell` Bridge, use `F.9`. If it states a changed effective reference scheme, representation-scheme transition, model-use relation, or EntityOfConcern retargeting, use `C.2.1`, `A.6.3`, `A.6.3.RT`, `A.6.4`, or the direct owner selected by the exact changed object. Use A.6.1 for a mechanism-realization relation and the applicable evaluation and evidence-use pattern for support of a mechanism claim.
* If the text states planned work, use `A.15.2`.
* If the text states dated performed work, use `A.15.1`.
* If the text states an evidence relation or provenance relation, use `A.10`.
* If the text turns a graph, path, query, table, dashboard, predicate, publication face, or pattern relation into a route, call sequence, dispatch, or work procedure by metaphor, use `C.2.P.DR` before choosing the direct governing pattern.

This is why "algorithm" and "practice" are not repaired to "method" automatically. An algorithm-looking expression may indicate a method description, formal substrate, mechanism, control strategy, work plan, work occurrence, evidence relation, or quoted source wording. A practice-looking expression may indicate a method, method family, method relation structure, method description, work plan, dated work, role assignment, bounded context, discipline position, cultural-evolution case, canon or memory episteme, recognition or selection regime, mediation system, evidence relation, or quoted source wording. The repair closes only after recovering the current governed object and claim position.

#### A.3.1:4.6 - Constructor and process-theory settlement

FPF interprets method claims through transformation first, not software notation first.

In the constructor-theory and process-theory source line adopted here, claims about computation, information, dynamics, and procedure are kept close to possible or impossible transformations and their compositional realization. That gives FPF the following settlement:

* an exact system performs dated work that enacts a method only through the A.15.1 occurrence basis, including the covering `U.RoleAssignment`, `performedBy`, and exact enacted-method relation; the reusable method itself creates no actor or `TransformerRole`;
* the method is the context-local way of doing the transformation;
* a method description is an episteme that describes that way;
* a formal substrate or mathematical lens may make the method analyzable, but does not become the method by itself;
* a mechanism may declare a law-governed operation family, its direct subject and range fields, operation algebra, laws, admissibility predicates, and Applicability for a method-facing transformation;
* a cross-context `SenseCell` Bridge under F.9, a reference-scheme or model-use transition under its direct owner, a mechanism-realization relation, and support for a mechanism claim remain distinct neighboring relations; obtaining or changing one of them does not by itself create or replace the mechanism declaration;
* a work plan prepares or schedules dated work;
* dated work is the occurrence that happened.

This settlement covers welding, milling, reagent mixing, clinical triage, proof construction, optimization, scheduling, training, inference, and software execution without making "code" the privileged form of method.

#### A.3.1:4.7 - Semantic identity and variants

Two `U.MethodDescription` epistemes may describe the same `U.Method` in a bounded context when, for the recognized generic participant meanings and conditions of that context, they preserve the same method identity:

* compatible preconditions;
* compatible effects or postconditions;
* compatible non-functional bounds;
* accepted nondeterminism or search behavior;
* the same work-facing acceptance relation.

Different internal control flow, search strategy, proof notation, programming paradigm, diagram notation, or textual format does not by itself make a different method. Conversely, the same name, diagram family, repository, supplier label, or workflow label does not by itself prove identity.

When variants differ only by parameter ranges, equipment envelope, or local representation, keep one method with declared variation when the context accepts that identity. When variants change intended effects, bounds, admitted participant meanings, safety envelope, or work-facing acceptance criteria, declare a refinement, substitution, or distinct method.

#### A.3.1:4.8 - Method relation structure, composition, and work enactment

Methods may compose into larger method holons. Work individuals may stand in exact work-part relations to larger Work occurrences under A.15.1. A work history, log, or account about those occurrences is a separate episteme rather than a larger Work occurrence by being a record. These are related but different claims.

When the current question is one semantic way of doing, the governed object is `U.Method`. When submethods are assembled into a whole method, the governed object is still `U.Method`, now under method-holon composition. When the current question is only a relation among methods, method families, local method expressions, method-description links, or work-facing method-use relations, the governed object is `MethodRelationStructure@BoundedContext`: a context-local structure over method-side values.

By the `E.24.UK` settlement, `MethodRelationStructure@BoundedContext` reuses the already admitted `U.Structure` and is selected under `A.22` for the current bounded use. It admits no new durable U-kind, no method holon, and no closed relation type. The suffix is a readable designation of that selected structure, not a root-kind constructor. Its elements are exact method-side values, and its connections are exact composition, refinement, substitution, iteration, decomposition, family-membership, selector, fallback, description, or use relation occurrences governed by their direct patterns. The list below is recognition guidance, not a substitute schema.

The selected `U.Structure` may include exact occurrences of:

- serial composition;
- parallel composition;
- guarded choice;
- iteration;
- refinement;
- substitution;
- decomposition;
- parameterization;
- method-family membership, selection, fallback, or dispatch relation;
- an exact separately governed applicability, compatibility, selector, description, or work-use relation involving a method-side role-admission or capability-fit condition, when that direct relation is current; selection into the structure establishes neither a planned assignment nor actual participation.

Those relations are design-side or definition-side claims about ways of doing. They are not dated work merely because an implementation, graph, process model, or workflow-looking diagram can be executed or followed.

Method-holon composition is not A.14 structural component mereology. `SerialStepOf`, `ParallelFactorOf`, guarded choice, iteration, typed joins, adapters, and method-interface exposure are arrangement or constraint relations over recovered `U.Method` submethods. Method-description nodes may describe those relations, but they are not method parts unless the governed object is recovered as a `U.Method`. Use `B.1.5` when order-sensitive method composition is current, and use `B.2` when whole reidentification of the composite method is current.

Work composition is occurrence-side: dated work may interleave, split, merge, retry, fail, recover, or be recorded in traces differently from the method description or method relation structure. Method decomposition and work decomposition are coupled because work enacts method, but they are not isomorphic. A temporal work part may enact the same whole method during a slice. An episode may record continuity under one method or mode while spanning several operational parts, repeating a fragment, or being split by evidence policy. A work part corresponds to a submethod only when the candidate factor is recovered as a `U.Method` with method-level preconditions, effects, interface or boundary, and whole-method relation under `B.1.5`.

**Quick distinction for readers.** If the source names a step, stroke, graph node, detector component, event-log segment, telemetry interval, work-plan item, or document section, ask two questions before using method-part wording:

1. Does this candidate name a reusable way of doing with method-level preconditions, effects, interface, and whole-method relation? If yes, recover a `U.Method` submethod.
2. Does this candidate instead name what happened, when it happened, which resources burned, which component behaved, or which evidence slice was recorded? If yes, use `A.15.1` for a Work individual admitted under `U.Work`, `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, evidence, mechanism, system-component behavior, or method-description constituent under the direct pattern.

Algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation may describe or analyze the `U.Structure` selected under `A.22` and designated `MethodRelationStructure@BoundedContext`. That notation is a mathematical or representation lens under `C.29` or a `U.MethodDescription` representation when the description itself is current. Do not name it `U.MethodAlgebra` or treat the lens as the method, method family, work plan, performed work, mechanism, role relation structure, or selector registry.

Do not infer method composition from document modules, graph layout, table order, method-family registry rows, or source-file structure alone. A two-module description is not automatically a two-step method. A path in a graph is not automatically an execution sequence. A pipeline-looking diagram is not automatically dated work. A method-family registry may select among or compose families, but the registry entry is not the method relation structure unless the governing selector or method pattern states that relation by value.

### A.3.1:5 - Archetypal Grounding

Across the slices below, a `U.Method` is not recognized by source wording, notation, or publication form. It is recognized by a stable project answer to this question:

```text
In this bounded context, what way of doing changes, produces, derives, selects, controls, or preserves this transformed entity or structure under these conditions?
```

Manufacturing, optimization, proof, graph or query overread, and clinical triage differ in material, representation, and assurance needs, but they share the same method-identification question. The archetypal failure is also shared: a nearby description, plan, run, mechanism, formalism, or evidence relation takes the method name and silently changes what the project can rely on.

#### A.3.1:5.1 - Manufacturing recipe

`Etch_Al2O3` is the method when the bounded context uses that name for the way of transforming a wafer surface under specified conditions.

The SOP, PLC program, calibration recipe, and supplier note are method descriptions when they describe that method. A planned maintenance-window run is a `U.WorkPlan`. The dated tool run `W-143` is a Work individual admitted under `U.Work` when its A.15.1 occurrence basis is recoverable. Its timestamps and logs belong to separately governed records; they may evidence that work only through an exact evidence-use relation. Gas-flow equations may be a formal substrate or mathematical lens input. Evidence for whether the run met a safety or quality claim is governed separately by `A.10`, `B.3`, `C.27`, or a gate pattern.

#### A.3.1:5.2 - Optimization model

`JS_Schedule_v4` may be the method when it names the project-accepted way of producing a job-shop schedule.

The MILP formulation, solver configuration, and acceptance tests are method descriptions or formal-substrate declarations depending on the current claim. The solver's internal search is not automatically the project work sequence. A scheduled production plan is `U.WorkPlan`. The actual scheduling run is a Work individual admitted under `U.Work` when its A.15.1 occurrence basis is recoverable. The dated scheduling decision record is a separately governed result episteme; describe it as resulting from the run or use it as evidence for another claim only when the corresponding exact work-to-record or evidence-use relation obtains.

#### A.3.1:5.3 - Proof or derivation

`Gauss_Elimination` can be a method for deriving a result under a mathematical context.

A textbook explanation, proof-assistant script, and formal rule set are method descriptions. A concrete proof-assistant run is work. The algebraic structure may be a formal substrate. The claim that this proof is used as evidence for a project decision is an evidence or assurance claim, not part of the method merely because the method produced a derivation.

#### A.3.1:5.4 - Graph or query overread

A graph path, SQL-like query, checklist predicate, or dashboard table may represent a relation, state, evidence structure, provenance structure, or publication face. It becomes a method claim only if the text recovers a semantic way of doing and its work-facing relation.

If the wording says the graph "routes" a project to a pattern, the query "calls" a work sequence, or the table "authorizes" action without a recovered method kind, work kind, gate claim, or authority claim, apply `C.2.P.DR` first.

#### A.3.1:5.5 - Clinical triage protocol

`SepsisTriage_v3` may be the method when the hospital context uses that name for the way of classifying a patient state and selecting the next clinical response.

The protocol PDF, order-set screen, and decision-support rule are method descriptions or publication faces. The clinician's dated assessment is a Work individual admitted under `U.Work`. The physiological model or score formula may be a formal substrate or mathematical lens. An admission policy, a treatment-release gate, and evidence that the triage reduced harm are neighboring claims. Keeping those claims separate prevents a document from becoming authorization, proof, and performed work merely because it describes the method.

### A.3.1:6 - Bias-Annotation

This pattern mainly blocks seven recurring biases:

* **description-as-method bias**: a publication, program, diagram, or protocol is treated as the method instead of a method description;
* **practice-as-method bias**: a source says "practice" and the repair silently chooses `U.Method` without checking whether the current claim is work, role assignment, discipline, cultural-evolution, evidence, source label, or method relation structure;
* **run-as-method bias**: a trace, log, run, or result record is treated as the reusable way of doing;
* **software-notation bias**: code, algorithm, workflow, or programming-paradigm language becomes the default ontology for every method;
* **mechanism-overread bias**: law-governed mechanism or formal-substrate material is treated as if it already selected the project method;
* **holder-as-method bias**: a team, system, supplier, or capability holder becomes the method name;
* **semio-bias**: the discussion shifts from the way of doing to the description, publication, evidence face, or wording repair before the exact method claim is recovered.

The repair is the same in each case: recover `U.Method` when the semantic way of doing is current, and then link neighboring governed objects through their own direct relations.

### A.3.1:7 - Conformance Checklist

**CC-A3.1-1 (Method identity).** `U.Method` is the context-defined semantic way of doing a kind of transformation or enactment. A method claim is not closed by naming a method description, work plan, dated work occurrence, evidence relation, role assignment, capability, mechanism declaration, formal-substrate declaration, publication face, or pattern relation. If one of those claims is also current, state it in its governing pattern and link the governed objects explicitly.

**CC-A3.1-2 (Context anchoring).** Every method identity is interpreted inside a `U.BoundedContext`. Same name across contexts does not prove same method.

**CC-A3.1-3 (Description relation).** A method should have at least one named `U.MethodDescription` when work, assurance, gate, or audit reliance depends on it. Several descriptions may describe the same method only under a stated method-identity relation or criterion.

**CC-A3.1-4 (Assignment-free method).** A method may state role-kind admission conditions or capability-fit conditions. These are method-side admissibility conditions, not deontic obligations by default. The method does not bind named people, teams, organizations, or calendar allocations.

**CC-A3.1-5 (Runtime-free method).** Dated runs are Work individuals admitted under `U.Work`; their performer, temporal, participation, and resource-use facts obtain through exact direct relations. Telemetry, logs, and result records remain separately governed evidence, source, measurement, evaluation, production, delivery, acceptance, or other claim objects; none belongs to method identity by being associated with a run.

**CC-A3.1-6 (Plan-free method).** Work preparation, schedule, go or no-go date, work authorization, and planned work relation belong to `U.WorkPlan`, gate, authority, or commitment patterns.

**CC-A3.1-7 (Mechanism and formal-substrate separation).** A formal substrate, mathematical-lens use, mechanism declaration, mechanism realization, or control model may provide constraints, invariants, or realization facts used when judging a method claim, or may be linked through exact direct relations recovered under `E.10.ARCH:3.1`. It still does not close the method claim unless the current claim states the context-local semantic way of doing and its work-facing identity.

**CC-A3.1-8 (Programming-paradigm neutrality).** Imperative, functional, logical, constraint, object-centric event, effect-handler, and hybrid descriptions are representation choices or description forms until the exact method claim is recovered.

**CC-A3.1-9 (Graph and representation guard).** A graph path, path slice, query, predicate, table, dashboard, publication face, or pattern relation is not a method or work sequence by layout. Use `C.2.P.DR` when representation wording is overread as imperative action.

**CC-A3.1-10 (Method holon, method relation structure, and work composition distinction).** Method-holon composition, method-family selection, fallback, refinement, substitution, iteration, decomposition, and work-occurrence composition remain separate even when they correspond. When submethods are assembled into a whole method, govern the result as `U.Method` with `B.1.5` when order-sensitive composition is current. A step label, step description, order edge, work-plan item, event-log segment, telemetry interval, engine stroke label, detector component, or graph node is not a submethod until it is recovered as a `U.Method` with method-level preconditions, effects, interface or boundary, and whole-method relation. A temporal work part may enact the same whole method during a slice, and an episode may split continuity without changing method identity. When method-side relations are current without whole-method assembly, select a `U.Structure` under `A.22` and designate it `MethodRelationStructure@BoundedContext` for the current use; that designation admits no new durable U-kind, method holon, or closed relation type. Algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation is a lens or representation over the selected method object or structure unless a governing pattern states a different object by value.

**CC-A3.1-11 (Practice wording recovery).** When source wording says `practice`, record the recovered claim kind before accepting a method statement: `U.Method`, method family or method relation structure, `U.MethodDescription`, `U.WorkPlan`, dated Work occurrence admitted under `U.Work`, role assignment or role relation, bounded context, discipline, cultural-evolution case, canon or memory episteme, recognition or selection regime, mediation system, evidence relation, source label, or quote-only wording.

**CC-A3.1-12 (Parameter and variant discipline).** Parameters may be stated as method semantics or described by `U.MethodDescription`. A `U.WorkPlan` may state planned values only against the exact governed declaration current for the plan. An actual value or participant is established only through its exact direct subject relation or A.6.1 operation-application binding; neither method nor description makes it actual. Effects, bounds, admitted participant meanings, and context establish variant identity.

**CC-A3.1-13 (Evidence and assurance boundary).** A method or method description does not by itself prove that work happened, that a result is warranted for the claimed use, that a gate is passed, or that action is authorized. Those claims use the relevant evidence, assurance, gate, temporal, authority, work-plan, or work patterns.

### A.3.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The code is the method." | If the claim is about the repository or executable text, use `U.MethodDescription`; if it is about the semantic way of doing, name the `U.Method` and its context. |
| "The workflow diagram is the work." | Use `U.MethodDescription` for the diagram, `U.WorkPlan` for planned work, and one Work occurrence admitted under `U.Work` for the dated occurrence. |
| "The graph path routes the decision." | If it is graph structure, use `E.18`; if it is overread as route or action, use `C.2.P.DR`; if a gate or authority claim is current, use the direct gate or authority pattern. |
| "The optimization model is the process." | Recover whether the current claim is formal substrate, method description, method semantics, work plan, work, or evidence. |
| "The protocol approval proves safe execution." | Separate publication-state claim, gate or authorization claim, evidence claim or assurance claim, work plan, and dated work. |
| "The team is the method." | Keep holders and assignments in role assignment; keep capability in capability; keep method admission conditions context-local. |

### A.3.1:9 - Consequences

* Method-like language becomes reusable across physical, informational, organizational, and mathematical work without privileging software code or ordered instructions.
* Teams can compare descriptions, variants, and implementations without confusing them with dated work.
* Work planning and evidence become more reliable because a method no longer smuggles in authority, proof, schedule, or performed-work claims.
* The cost is explicit recovery of the governed object and claim position: reliance on wording such as "method", "practice", "algorithm", "workflow", "process", "procedure", "program", "recipe", "proof", or "solver" begins only after the current FPF object or claim is recovered.

#### A.3.1:9.1 - Lowering and local repair conditions

Lower or withdraw the current `U.Method` identification when:

* the text cannot state transformation or enactment kind, `A.3.4 transformedEntityOrStructure`, preconditions, and intended effects;
* the method name is only a document, repository, diagram, model, run log, team name, supplier label, or authorization claim;
* the same typed value is assigned as both `U.Method` and `U.Mechanism` without a governing pattern admitting the dual typing;
* source wording such as `practice` has not been recovered to one current claim position before method reliance begins;
* graph, path, query, table, or predicate wording is treated as ordered execution without `C.2.P.DR` recovery;
* a later `U.MethodDescription`, `U.WorkPlan`, Work occurrence admitted under `U.Work`, `U.Mechanism`, `C.29`, `E.18`, or evidence pattern changes an exact relation or semantic condition on which the method statement relied.

If the semantic way of doing cannot be recovered, withdraw the `U.Method` typing and keep the wording as an unresolved cue. If a neighboring description, plan, work, mechanism, representation, or evidence value has taken the method position, split that value into its direct governing relation. If only one relied-on identity-basis relation changed, review that relation and the affected method identity rather than invalidating every use of the method.

The smallest useful repair is usually local: revise the method identification, split the neighboring value into its governing pattern, or add one `ClaimBoundary` line. A new method-description edition repairs the description relation unless it changes a relied-on method-identity field. A changed work fact repairs the work claim; a changed measurement, evaluation, production, delivery, acceptance, or evidence result repairs that separately governed claim. Neither changes the method unless it changes the accepted participant meanings, preconditions, intended effects, bounds, or transformed-entity relation on which method identity depends. Return to `G.5` or the direct method-family pattern only when repeated project material shows that the current family or selector relation no longer separates methods, descriptions, plans, work, mechanisms, or neighboring claims adequately. A verbose or poorly ordered explanation is a didactic defect to repair in the description; it does not by itself lower the identified method.

### A.3.1:10 - Rationale

FPF needs `U.Method` because practical work often depends on a way of doing before there is one dated work occurrence, one accepted description, one final implementation, or one verified result. Treating the method as the document, code, mechanism, plan, or run makes reuse brittle: changing the publication looks like changing the method, a run error looks like method invalidation, and a mechanism claim starts authorizing work.

The distinction between method and mechanism is especially important because the same source expression or project concern can need both linked values. The method says what way of doing is intended or enacted in context. The mechanism declares a law-governed operation family, its direct subject and range fields, operation algebra, laws, admissibility predicates, and Applicability. A bridge, realization, evaluation, or evidence-use claim may relate to that declaration without becoming part of its semantic content. The method and mechanism may also be linked, but they should not be made two names for one untyped value.

### A.3.1:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Constructor-theory and process-theory bridge, with a current time treatment | Gogioso, Wang-Mascianica, Waseem, Scandolo, and Coecke, ["Constructor Theory as Process Theory"](https://arxiv.org/abs/2401.05364), EPTCS 397, 2023; Deutsch and Marletto, ["Constructor theory of time"](https://arxiv.org/abs/2505.08692), arXiv v3, revised 2026-06-05. | Adopt the separation between a transformation specified as possible or impossible and a concrete process that realizes it. Adapt it beyond physical tasks: an FPF method is identified through the bounded way of transforming or preserving its governed entity or structure; a concrete realizer is connected to a mechanism declaration by a separate realization relation; dated enactment belongs to work. The 2023 paper is a formal bridge and the 2026 paper is a current extension, not evidence that constructor theory alone supplies a universal method ontology. | The pattern starts from transformation or enactment kind and separates method, mechanism, mechanism realization, description, plan, and work. The manufacturing case no longer lets equipment equations or one tool run define the reusable method. |
| Scoped effects, handlers, and current semantic non-uniqueness | Bosman, van den Berg, Tang, and Schrijvers, ["A Calculus for Scoped Effects & Handlers"](https://arxiv.org/abs/2304.09697), LMCS 20(4), 2024; Matache, Lindley, Moss, Staton, Wu, and Yang, ["Scoped Effects as Parameterized Algebraic Theories"](https://arxiv.org/abs/2402.03103), ESOP 2024 extended version; Kura, ["On Complete Categorical Semantics for Effect Handlers"](https://arxiv.org/abs/2602.03275), current 2026 preprint. | Adopt the separation among operation syntax, handling semantics, scope, resources, equations, and type-and-effect information. Kura's result strengthens the guard: even a sound formal account need not be the only semantic model of the same handling constructs. Adapt only as a software-derived stress test; these calculi do not define methods in manufacturing, medicine, or organizational work. | The pattern refuses to repair `algorithm`, `program`, `function`, handler syntax, or one semantic model to `U.Method` merely by programming-paradigm label. The proof and optimization cases ask for the bounded way of doing before admitting a method identity. |
| Current graph, binding, and persistent-equivalence representations | Tiurin, Barrett, Ghica, and Hu, ["Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs"](https://arxiv.org/abs/2406.15882), revised 2025-05-20; Tiurin, Ghica, and Hu, ["Categorical E-Graphs for Lambda Calculi"](https://arxiv.org/abs/2505.00807), revised 2026-06-25; Merckx et al., ["E-Graphs as a Persistent Compiler Abstraction"](https://arxiv.org/abs/2602.16707), current 2026 preprint. | Adapt the demonstrated distinction between represented equivalence or rewriting structure and an ordered instruction sequence. Binding-aware hierarchical hypergraphs and equivalence state preserved across several intermediate-representation levels show why neither graph layout nor one representation level establishes the semantic method or dated work order. These sources are compiler and formal-representation results, not a general ontology of project methods. | Graph paths, queries, tables, rewrite graphs, and persistent compiler structures remain descriptions or formal lenses until a direct method, method-relation, work, evidence, or gate claim is recovered. The graph-overread case and `C.2.P.DR` exit carry this safeguard. |
| Historical declarative versus imperative programming contrasts | Codd 1970; Kowalski 1979; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004; Deutsch 2013; Deutsch and Marletto 2015. | Reject as current SoTA; retain only as lineage and regression contrast. | Older slogans such as "declarative versus imperative" are used only as recognition cues; the repair recovers the exact FPF governed object and claim. |

Review a project's current `U.Method` identification when its bounded context, transformation or enactment kind, transformed entity or structure, preconditions, effects, bounds, or work-facing acceptance relation changes. Review only the linked description, work, mechanism, representation, or evidence relation when that neighboring value changes without changing a method-identity basis. Review the method family or selector under `G.5` only when the available family no longer separates the methods or variants needed for the current use.

When a receiving use relies on the currentness, edition, freshness, telemetry, or decay status of a cited method description or SoTA source, use `G.11` for that currentness relation. A new paper, source edition, implementation, or run is a reason to inspect the affected relation; it does not change the method merely by being newer. Reconsider the A.3.1 distinction itself only when stronger work on constructor theory, process theory, effect systems, process modeling, practice theory, cultural evolution, graph or equivalence representation, or FPF's direct method neighbors overturns a distinction on which the project relies.

### A.3.1:12 - Relations

* **Builds on:** `A.1` holonic foundation, `A.1.1 U.BoundedContext`, `A.2` role, `A.2.1 U.RoleAssignment`, `A.2.2 U.Capability`.
* **Coordinates with:** `A.3.2` for method descriptions and method-relation descriptions; `A.3.3` for dynamics; `A.6.0` for formal-substrate declarations; `A.6.1` and `E.20` for mechanism claims; `C.29` for mathematical-lens use; `G.5` for method-family registries and selector outcomes; `G.11` for relied-on source, edition, freshness, telemetry, and decay currentness; direct method-composition patterns such as `B.1.5` when order-sensitive method composition is current; `A.1.1` for bounded-context meanings hidden by practice wording; `A.2`, `A.2.1`, and `A.2.7` for role values, role assignments, and role relations hidden by practice wording; `A.15.2` for work plans; `A.15.1` for dated work; `C.20`, `C.36`, and `C.36.P` for discipline and cultural-evolution practice wording; `A.10` for evidence relations or provenance relations; `C.2.P.DR` for declarative representations overread as imperative routes or work sequences.
* **Informs:** `E.18` and `E.18.1` when transformation-flow-structure or P2W wording keeps flow-structure descriptions, graph or path mathematical expressions, method claims, and work claims separate.

### A.3.1:End

