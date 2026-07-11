## A.3.1 - U.Method: Context-Defined Way of Doing

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### A.3.1:1 - Problem frame

Use this pattern when a project needs to say **how something is done in principle** without prematurely treating that method or practice claim as a document, program, workflow diagram, plan, run log, role assignment, capability statement, mechanism claim, cultural tradition, discipline position, or mathematical-model claim before those positions are recovered.

Typical moments:

* a team says "the method is the code", "the process is the BPMN", "the workflow is the evidence", or "the solver model is the operation";
* a practice, procedure, protocol, proof script, optimization model, control strategy, or recipe must be reused across many runs;
* two descriptions look different but may describe the same way of doing;
* a graph, query, table, dashboard, checklist predicate, or mathematical representation is being interpreted as if it were an instruction sequence;
* work planning, dated work, method description, formal substrate, mechanism, role assignment, cultural-evolution, discipline, and evidence are starting to collapse into one vague "method" or "practice" word.

**Primary EntityOfConcern.** The `EntityOfConcern` is the `U.Method`: the context-local semantic way of doing a kind of transformation or enactment. `U.Method` is a non-agentive holon kind: methods can have submethods, compose into whole methods, and participate as submethods of larger methods. This does not make a method an actor, a method description, a work plan, or a dated work occurrence. A step label or step description is not a method part unless the recovered object is itself a `U.Method`.

**First useful move.** Name the context-local way of doing, the transformation or enactment it is about, and the `EntityOfConcern` whose state, result, selection, derivation, control relation, or maintained condition changes or is preserved.

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

* A method must be stable enough to compare, reuse, teach, improve, and audit across many runs.
* Work still happens in dated situations with named systems, resources, holders, conditions, and outcomes; a method statement must not pretend that the dated work has already occurred.
* Method descriptions can be executable, formal, graphical, procedural, declarative, or hybrid; their publication form must not decide the method ontology by itself.
* Mechanisms and mathematical substrates often make a method explainable or constrained enough to rely on, but the mechanism claim and the method claim still answer different project questions.
* A useful method statement must stay broad enough for welding, clinical triage, proof construction, optimization, agent orchestration, lab protocols, software execution, and organizational work without making software notation the default model of method.

### A.3.1:4 - Solution

`U.Method` is the **context-defined semantic way of doing a kind of transformation or enactment**.

It is a non-agentive holon kind. Part methods can be selected, bounded, ordered, joined, adapted, and hidden or exposed through method interfaces to form a whole method with whole-level preconditions, effects, invariants, constraints, and assurance hooks. The whole method may then be used as a part method in a larger method.

It is not the text, code, diagram, model, plan, run, role, capability, or evidence relation that may be associated with that way of doing. A `U.Method` is:

* **context-defined**: its identity, admissible inputs, conditions, effects, and bounds are interpreted inside a `U.BoundedContext`;
* **semantic**: it is the way of doing that descriptions denote and work may enact;
* **transformation-facing**: it concerns a possible or intended transformation, enactment, or produced result, including physical, informational, organizational, mathematical, or hybrid transformations;
* **description-independent**: one method may be described by several `U.MethodDescription` epistemes;
* **run-independent**: one method may be enacted by many `U.Work` occurrences;
* **assignment-independent**: method admission conditions may name role kinds or capability-fit conditions, but named holders and dated assignments belong elsewhere.

The primary repair action is not to replace the word "method" or "practice" with one better word. In ordinary source speech, `practice` often works as a synonym for method-like wording, but it can also name enacted work, role arrangement, discipline, tradition, source label, or cultural-evolution material. Recover the current slot first:

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
| dated work occurrence, run, trace-backed execution, result record | `A.15.1 U.Work` and evidence or source patterns when an evidence relation or source relation is current |
| field-level discipline, bounded context, community tradition, canon or memory episteme, recognition or selection regime, mediation system, variant set, or cultural-evolution intervention | `A.1.1`, `C.20`, `C.36`, `C.36.P`, `F.17`, `F.18`, `F.9`, `C.18`, `C.19`, `G.5`, or `G.11` according to the recovered claim |
| evidence or provenance relation for a claim | `A.10` |
| graph path, path slice, flow valuation, state predicate, query, table, dashboard, publication face, or pattern relation overread as a method or work sequence | `C.2.P.DR` first, then the direct governing pattern named by the recovery |

#### A.3.1:4.1 - Thin first-use record

For ordinary first use, write only the fields needed to keep the method claim from collapsing into a description, plan, run, mechanism, or evidence relation:

```text
Method statement:
  MethodRef:
  BoundedContext:
  TransformationOrEnactmentKind:
  EntityOfConcern:
  Preconditions:
  IntendedEffectsOrPreservedConditions:
  CurrentMethodDescriptionRef:
  WorkRelation:
  ClaimBoundary:
```

`ClaimBoundary` names the nearest stronger claim that is not carried by this method statement, such as work authorization, performed work, evidence for success, mechanism declaration, or formal-substrate adequacy. It is a boundary field, not a place to repeat every neighboring pattern.

#### A.3.1:4.2 - Method and mechanism settlement

Do not decide the method and mechanism question by vocabulary. When a source expression or project concern appears to name changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For this host, keep the local question thin: does the current claim state a `U.Method`, the context-local way of doing a transformation or enactment? If the source label also raises mechanism, formal-substrate, work-plan, dated-work, role-assignment, cultural-evolution, discipline, evidence, source, gate, result, publication, or temporal claims, keep those values linked only by explicit relation positions and apply their own governing patterns.
* In **method position**, the current claim is the context-local way of doing a transformation or enactment.
* In **mechanism position**, the current claim is a law-governed declaration or revision of operations, laws, admissibility predicates, transport, audit relation set, and monotone realizations under `A.6.1` and `E.20`.

Do not assign the same typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits such dual typing. Slot-position labels do not create alternate ontology.

This gives the working distinction:

| Current question | Governing pattern | What must be recoverable |
| --- | --- | --- |
| What way of doing is intended or enacted? | `A.3.1 U.Method` | context, transformation or enactment kind, preconditions, effects, work-facing identity, description relation |
| What description states the way of doing? | `A.3.2 U.MethodDescription` | episteme, representation form, method described, parameters, acceptance criteria, edition relation or source relation when current |
| What law-governed operation structure is being declared, specialized, transported, or realized? | `A.6.1 U.Mechanism` | `SubjectBlock`, `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, `Applicability`, `Transport`, `Audit`, realization relation |
| Where should new or revised mechanism meaning be governed? | `E.20` | governing-definition assignment for mechanism meaning, suite, plan, wiring, token continuity, or local non-trigger stop |
| What happened this time? | `A.15.1 U.Work` | performer, method enacted, method-description source relation when current, time window, parameters, resources, outcome |

A method may cite a mechanism, be selected by a mechanism, be constrained by a mechanism, or be one value in a mechanism's slot. A mechanism may govern an operation algebra whose operations include applying, selecting, composing, or normalizing methods. Those links do not collapse the typed values or their governing claims. If both claims are current, write both: the `U.Method` statement for the way of doing, and the `U.Mechanism` statement for the law-governed declaration or realization relation.

Fail closed when neither position can be recovered. Do not repair `practice`, `algorithm`, `program`, `workflow`, `process`, `solver`, `proof`, `recipe`, or `control strategy` to `method` or `mechanism` merely because the replacement sounds more technical.

#### A.3.1:4.3 - Method, MethodDescription, WorkPlan, Work

Keep the four positions separate.

| Position | What it means | Common mistaken substitutes |
| --- | --- | --- |
| `U.Method` | how in principle, inside a bounded context | code, SOP, graph, solver model, proof script, workflow diagram |
| `U.MethodDescription` | an episteme that describes a method in a representation | method semantics, actual run, authority to work |
| `U.WorkPlan` | planned dated work or work preparation | timeless method, generic recipe, proof that work happened |
| `U.Work` | dated work occurrence | method, plan, result interpretation, evidence relation |

The same solver model, repository, protocol, diagram, or run packet may participate in several claims, but each claim has its own slot. A solver model can be a `U.MethodDescription`; its mathematical formulation can also expose a formal substrate for `C.29`; a solver run can be `U.Work`; a run result can be evidence for a separate claim. Those claims are not interchangeable.

#### A.3.1:4.4 - Method statement fields

A useful `U.Method` statement can usually recover these fields in ordinary project language:

| Field | What to name |
| --- | --- |
| Method name | the context-local way of doing |
| Bounded context | the project, discipline, organization, regulatory setting, theory, or operational context that interprets the method |
| Transformation or enactment kind | what changes, is produced, decided, derived, controlled, selected, or maintained |
| EntityOfConcern under transformation | the material object, information object, organization, episteme, holon, or state whose transformation matters |
| Preconditions | what must already hold for the method to be applicable |
| Effects or postconditions | what successful enactment is meant to produce or preserve |
| Interface or signature | inputs, outputs, ports, resources, constraints, or role-kind admission conditions needed to state the method without naming this run |
| Capability requirements | thresholds or envelopes to be checked against a holder's capability, not baked into the method identity |
| Failure and stop conditions | when the method is blocked, when a description must be revised, or when work must not start |
| Description relation | which `U.MethodDescription` epistemes currently describe it |
| Work relation | what kind of `U.Work` may enact it and how runs cite the description used |

This is not a data schema. It is the minimum recognition field set needed before method-like wording can guide work, evidence, assurance, gates, or planning.

#### A.3.1:4.5 - Representation and programming-paradigm discipline

A `U.Method` does not require an imperative step structure.

Imperative procedures, functional compositions, logical rule sets, constraint models, object-centric event models, effect-handler programs, process diagrams, SQL queries, equality-saturation graphs, proof scripts, and optimization models may all help describe, represent, or analyze a way of doing. Their representation style does not by itself decide whether the current claim position is a method, a method description, a formal substrate, a mechanism, a work plan, work, evidence, or a declarative representation under `C.2.P.DR`.

Use this discipline:

* If the text states the semantic way of doing, use `A.3.1`.
* If the text states the representation that describes that way, use `A.3.2`.
* If the text states a formal object or mathematical representation used to reason, use `A.6.0`, `C.29`, or the direct mathematical pattern.
* If the text states a law-governed operation structure, admissibility predicate set, transport clause, or realization relation, use `A.6.1` or `E.20`.
* If the text states planned work, use `A.15.2`.
* If the text states dated performed work, use `A.15.1`.
* If the text states an evidence relation or provenance relation, use `A.10`.
* If the text turns a graph, path, query, table, dashboard, predicate, publication face, or pattern relation into a route, call sequence, dispatch, or work procedure by metaphor, use `C.2.P.DR` before choosing the direct governing pattern.

This is why "algorithm" and "practice" are not repaired to "method" automatically. An algorithm-looking expression may indicate a method description, formal substrate, mechanism, control strategy, work plan, work occurrence, evidence relation, or quoted source wording. A practice-looking expression may indicate a method, method family, method relation structure, method description, work plan, dated work, role assignment, bounded context, discipline position, cultural-evolution case, canon or memory episteme, recognition or selection regime, mediation system, evidence relation, or quoted source wording. The repair must recover the slot.

#### A.3.1:4.6 - Constructor and process-theory settlement

FPF interprets method claims through transformation first, not software notation first.

In the constructor-theory and process-theory source line adopted here, claims about computation, information, dynamics, and procedure are kept close to possible or impossible transformations and their compositional realization. That gives FPF the following settlement:

* a system in a transformer-like role can enact a method;
* the method is the context-local way of doing the transformation;
* a method description is an episteme that describes that way;
* a formal substrate or mathematical lens may make the method analyzable, but does not become the method by itself;
* a mechanism may declare law-governed operation structure, admissibility predicates, transport, and realization relations for a method-facing transformation, but that mechanism claim is not the same claim as selecting, describing, planning, or enacting a method;
* a work plan prepares or schedules dated work;
* dated work is the occurrence that happened.

This settlement covers welding, milling, reagent mixing, clinical triage, proof construction, optimization, scheduling, training, inference, and software execution without making "code" the privileged form of method.

#### A.3.1:4.7 - Semantic identity and variants

Two `U.MethodDescription` epistemes may describe the same `U.Method` in a bounded context when, for the recognized inputs and conditions of that context, they preserve the same method identity:

* compatible preconditions;
* compatible effects or postconditions;
* compatible non-functional bounds;
* accepted nondeterminism or search behavior;
* the same work-facing acceptance relation.

Different internal control flow, search strategy, proof notation, programming paradigm, diagram notation, or textual format does not by itself make a different method. Conversely, the same name, diagram family, repository, supplier label, or workflow label does not by itself prove identity.

When variants differ only by parameter ranges, equipment envelope, or local representation, keep one method with declared variation when the context accepts that identity. When variants change effects, bounds, accepted inputs, safety envelope, or work-facing acceptance criteria, declare a refinement, substitution, or distinct method.

#### A.3.1:4.8 - Method relation structure, composition, and work enactment

Methods may compose into larger method holons. Work occurrences may compose into larger work histories. These are related but different claims.

When the current question is one semantic way of doing, the governed object is `U.Method`. When submethods are assembled into a whole method, the governed object is still `U.Method`, now under method-holon composition. When the current question is only a relation among methods, method families, local method expressions, method-description links, or work-facing method-use relations, the governed object is `MethodRelationStructure@BoundedContext`: a context-local structure over method-side values.

A method relation structure may include:

- serial composition;
- parallel composition;
- guarded choice;
- iteration;
- refinement;
- substitution;
- decomposition;
- parameterization;
- method-family membership, selection, fallback, or dispatch relation;
- a relation from method role-admission condition to accepted role assignment when work admission depends on it.

Those relations are design-side or definition-side claims about ways of doing. They are not dated work merely because an implementation, graph, process model, or workflow-looking diagram can be executed or followed.

Method-holon composition is not A.14 structural component mereology. `SerialStepOf`, `ParallelFactorOf`, guarded choice, iteration, typed joins, adapters, and method-interface exposure are arrangement or constraint relations over recovered `U.Method` submethods. Method-description nodes may describe those relations, but they are not method parts unless the governed object is recovered as a `U.Method`. Use `B.1.5` when order-sensitive method composition is current, and use `B.2` when the composite method requires whole reidentification.

Work composition is occurrence-side: dated work may interleave, split, merge, retry, fail, recover, or be recorded in traces differently from the method description or method relation structure. Method decomposition and work decomposition are coupled because work enacts method, but they are not isomorphic. A temporal work part may enact the same whole method during a slice. An episode may record continuity under one method or mode while spanning several operational parts, repeating a fragment, or being split by evidence policy. A work part corresponds to a submethod only when the candidate factor is recovered as a `U.Method` with method-level preconditions, effects, interface or boundary, and whole-method relation under `B.1.5`.

**Quick distinction for readers.** If the source names a step, stroke, graph node, detector component, event-log segment, telemetry interval, work-plan item, or document section, ask two questions before using method-part wording:

1. Does this candidate name a reusable way of doing with method-level preconditions, effects, interface, and whole-method relation? If yes, recover a `U.Method` submethod.
2. Does this candidate instead name what happened, when it happened, which resources burned, which component behaved, or which evidence slice was recorded? If yes, use `U.Work`, `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, evidence, mechanism, system-component behavior, or method-description constituent under the direct pattern.

Algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation may describe or analyze a selected `MethodRelationStructure@BoundedContext`. That notation is a mathematical or representation lens under `C.29` or a `U.MethodDescription` representation when the description itself is current. Do not name it `U.MethodAlgebra` or treat the lens as the method, method family, work plan, performed work, mechanism, role relation structure, or selector registry.

Do not infer method composition from document modules, graph layout, table order, method-family registry rows, or source-file structure alone. A two-module description is not automatically a two-step method. A path in a graph is not automatically an execution sequence. A pipeline-looking diagram is not automatically dated work. A method-family registry may select among or compose families, but the registry entry is not the method relation structure unless the governing selector or method pattern states that relation by value.

### A.3.1:5 - Archetypal Grounding

Across the slices below, a `U.Method` is not recognized by source wording, notation, or publication form. It is recognized by a stable project answer to this question:

```text
In this bounded context, what way of doing changes, produces, derives, selects, controls, or preserves the EntityOfConcern under these conditions?
```

Manufacturing, optimization, proof, graph or query overread, and clinical triage differ in material, representation, and assurance needs, but they share the same method slot. The archetypal failure is also shared: a nearby description, plan, run, mechanism, formalism, or evidence relation takes the method name and silently changes what the project can rely on.

#### A.3.1:5.1 - Manufacturing recipe

`Etch_Al2O3` is the method when the bounded context uses that name for the way of transforming a wafer surface under specified conditions.

The SOP, PLC program, calibration recipe, and supplier note are method descriptions when they describe that method. A planned maintenance-window run is a `U.WorkPlan`. Tool run `W-143` with timestamps and logs is `U.Work`. Gas-flow equations may be a formal substrate or mathematical lens input. Evidence for whether the run met a safety or quality claim is governed separately by `A.10`, `B.3`, `C.27`, or a gate pattern.

#### A.3.1:5.2 - Optimization model

`JS_Schedule_v4` may be the method when it names the project-accepted way of producing a job-shop schedule.

The MILP formulation, solver configuration, and acceptance tests are method descriptions or formal-substrate declarations depending on the current claim. The solver's internal search is not automatically the project work sequence. A scheduled production plan is `U.WorkPlan`; the actual scheduling run and resulting dated decision record may be `U.Work` and evidence for separate claims.

#### A.3.1:5.3 - Proof or derivation

`Gauss_Elimination` can be a method for deriving a result under a mathematical context.

A textbook explanation, proof-assistant script, and formal rule set are method descriptions. A concrete proof-assistant run is work. The algebraic structure may be a formal substrate. The claim that this proof is used as evidence for a project decision is an evidence or assurance claim, not part of the method merely because the method produced a derivation.

#### A.3.1:5.4 - Graph or query overread

A graph path, SQL-like query, checklist predicate, or dashboard table may represent a relation, state, evidence structure, provenance structure, or publication face. It becomes a method claim only if the text recovers a semantic way of doing and its work-facing relation.

If the wording says the graph "routes" a project to a pattern, the query "calls" a work sequence, or the table "authorizes" action without a recovered method kind, work kind, gate claim, or authority claim, apply `C.2.P.DR` first.

#### A.3.1:5.5 - Clinical triage protocol

`SepsisTriage_v3` may be the method when the hospital context uses that name for the way of classifying a patient state and selecting the next clinical response.

The protocol PDF, order-set screen, and decision-support rule are method descriptions or publication faces. The clinician's dated assessment is `U.Work`. The physiological model or score formula may be a formal substrate or mathematical lens. An admission policy, a treatment-release gate, and evidence that the triage reduced harm are neighboring claims. Keeping those claims separate prevents a document from becoming authorization, proof, and performed work merely because it describes the method.

### A.3.1:6 - Bias-Annotation

This pattern mainly blocks six recurring biases:

* **description-as-method bias**: a publication, program, diagram, or protocol is treated as the method instead of a method description;
* **practice-as-method bias**: a source says "practice" and the repair silently chooses `U.Method` without checking whether the current claim is work, role assignment, discipline, cultural-evolution, evidence, source label, or method relation structure;
* **run-as-method bias**: a trace, log, run, or result record is treated as the reusable way of doing;
* **software-notation bias**: code, algorithm, workflow, or programming-paradigm language becomes the default ontology for every method;
* **mechanism-overread bias**: law-governed mechanism or formal-substrate material is treated as if it already selected the project method;
* **holder-as-method bias**: a team, system, supplier, or capability holder becomes the method name;
* **semio-bias**: the discussion shifts from the way of doing to the description, publication, evidence face, or wording repair before the method slot is recovered.

The repair is the same in each case: recover the `U.Method` slot when the semantic way of doing is current, and then link neighboring values through their own slots or relations.

### A.3.1:7 - Conformance Checklist

**CC-A3.1-1 (Method slot).** `U.Method` is the context-defined semantic way of doing a kind of transformation or enactment. A method claim is not closed by naming a method description, work plan, dated work occurrence, evidence relation, role assignment, capability, mechanism declaration, formal-substrate declaration, publication face, or pattern relation. If one of those claims is also current, state it in its governing pattern and link the positions explicitly.

**CC-A3.1-2 (Context anchoring).** Every method identity is interpreted inside a `U.BoundedContext`. Same name across contexts does not prove same method.

**CC-A3.1-3 (Description relation).** A method should have at least one named `U.MethodDescription` when work, assurance, gate, or audit reliance depends on it. Several descriptions may describe the same method only under a stated method-identity relation or criterion.

**CC-A3.1-4 (Assignment-free method).** A method may state role-kind admission conditions or capability-fit conditions. These are method-side admissibility conditions, not deontic obligations by default. The method does not bind named people, teams, organizations, or calendar slots.

**CC-A3.1-5 (Runtime-free method).** Dated runs, timestamps, telemetry, logs, and work-result records belong to `U.Work` and associated evidence patterns or source patterns, not to the method identity.

**CC-A3.1-6 (Plan-free method).** Work preparation, schedule, go or no-go date, work authorization, and planned work relation belong to `U.WorkPlan`, gate, authority, or commitment patterns.

**CC-A3.1-7 (Mechanism and formal-substrate separation).** A formal substrate, mathematical-lens use, mechanism declaration, mechanism realization, or control model may provide constraints, invariants, or realization facts used when judging a method claim, or may be linked by typed relation-position claims under `E.10.ARCH:3.1`. It still does not close the method claim unless the current claim states the context-local semantic way of doing and its work-facing identity.

**CC-A3.1-8 (Programming-paradigm neutrality).** Imperative, functional, logical, constraint, object-centric event, effect-handler, and hybrid descriptions are representation choices or description forms until the method slot is recovered.

**CC-A3.1-9 (Graph and representation guard).** A graph path, path slice, query, predicate, table, dashboard, publication face, or pattern relation is not a method or work sequence by layout. Use `C.2.P.DR` when representation wording is overread as imperative action.

**CC-A3.1-10 (Method holon, method relation structure, and work composition distinction).** Method-holon composition, method-family selection, fallback, refinement, substitution, iteration, decomposition, and work-occurrence composition must stay separate even when they correspond. When submethods are assembled into a whole method, govern the result as `U.Method` with `B.1.5` when order-sensitive composition is current. A step label, step description, order edge, work-plan item, event-log segment, telemetry interval, engine stroke label, detector component, or graph node is not a submethod until it is recovered as a `U.Method` with method-level preconditions, effects, interface or boundary, and whole-method relation. A temporal work part may enact the same whole method during a slice, and an episode may split continuity without changing method identity. When method-side relations are current without whole-method assembly, recover `MethodRelationStructure@BoundedContext`. Algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation is a lens or representation over the selected method object or method relation structure unless a governing pattern states a different object by value.

**CC-A3.1-11 (Practice wording recovery).** When source wording says `practice`, record the recovered claim kind before accepting a method statement: `U.Method`, method family or method relation structure, `U.MethodDescription`, `U.WorkPlan`, dated `U.Work`, role assignment or role relation, bounded context, discipline, cultural-evolution case, canon or memory episteme, recognition or selection regime, mediation system, evidence relation, source label, or quote-only wording.

**CC-A3.1-12 (Parameter and variant discipline).** Parameters may be declared at method or method-description level; concrete values are bound in work planning or work occurrence. Variant identity must be justified by effects, bounds, accepted inputs, and context.

**CC-A3.1-13 (Evidence and assurance boundary).** A method or method description does not by itself prove that work happened, that a result is warranted for the claimed use, that a gate is passed, or that action is authorized. Those claims use the relevant evidence, assurance, gate, temporal, authority, work-plan, or work patterns.

### A.3.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The code is the method." | If the claim is about the repository or executable text, use `U.MethodDescription`; if it is about the semantic way of doing, name the `U.Method` and its context. |
| "The workflow diagram is the work." | Use `U.MethodDescription` for the diagram, `U.WorkPlan` for planned work, and `U.Work` for dated occurrence. |
| "The graph path routes the decision." | If it is graph structure, use `E.18`; if it is overread as route or action, use `C.2.P.DR`; if a gate or authority claim is current, use the direct gate or authority pattern. |
| "The optimization model is the process." | Recover whether the current claim is formal substrate, method description, method semantics, work plan, work, or evidence. |
| "The protocol approval proves safe execution." | Separate publication-state claim, gate or authorization claim, evidence claim or assurance claim, work plan, and dated work. |
| "The team is the method." | Keep holders and assignments in role assignment; keep capability in capability; keep method admission conditions context-local. |

### A.3.1:9 - Consequences

* Method-like language becomes reusable across physical, informational, organizational, and mathematical work without privileging software code or ordered instructions.
* Teams can compare descriptions, variants, and implementations without confusing them with dated work.
* Work planning and evidence become more reliable because a method no longer smuggles in authority, proof, schedule, or performed-work claims.
* The cost is explicit slot recovery: when wording says "method", "practice", "algorithm", "workflow", "process", "procedure", "program", "recipe", "proof", or "solver", the user must recover which FPF object or claim position is current before relying on it.

#### A.3.1:9.1 - Lowering and refresh conditions

Lower confidence in a `U.Method` use when:

* the text cannot state transformation or enactment kind, `EntityOfConcern`, preconditions, and intended effects;
* the method name is only a document, repository, diagram, model, run log, team name, supplier label, or authorization claim;
* the same typed value is assigned as both `U.Method` and `U.Mechanism` without a governing pattern admitting the dual typing;
* practice wording has not been recovered to method, method relation structure, work, role assignment, bounded context, discipline, cultural-evolution, evidence, source label, or quote-only use before method reliance begins;
* the first usable move requires a long related-pattern catalogue before the method slot is visible;
* graph, path, query, table, or predicate wording is treated as ordered execution without `C.2.P.DR` recovery;
* a later `U.MethodDescription`, `U.WorkPlan`, `U.Work`, `U.Mechanism`, `C.29`, `E.18`, or evidence pattern changes the slot relation on which the method statement relied.

The smallest useful repair is usually local: rewrite the method statement, split the neighboring value into its governing pattern, or add one `ClaimBoundary` line. Reopen the wider method family only when repeated project material shows that `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, `U.Mechanism`, formal substrate, role assignment, bounded context, discipline, cultural-evolution material, evidence, or mathematical-lens use can no longer be separated by the current slot rules.

### A.3.1:10 - Rationale

FPF needs `U.Method` because practical work often depends on a way of doing before there is one dated work occurrence, one accepted description, one final implementation, or one verified result. Treating the method as the document, code, mechanism, plan, or run makes reuse brittle: changing the publication looks like changing the method, a run error looks like method invalidation, and a mechanism claim starts authorizing work.

The distinction between method and mechanism is especially important because the same source expression or project concern can need both linked values. The method says what way of doing is intended or enacted in context. The mechanism says what law-governed operation structure, admissibility predicate set, transport, audit relation set, or realization relation is being declared. These values may be linked, but they should not be made two names for one untyped value.

### A.3.1:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current constructor-theory and process-theory work | Gogioso, Wang-Mascianica, Waseem, Scandolo, and Coecke, "Constructor Theory as Process Theory", EPTCS 397, 2023, arXiv:2401.05364; Deutsch and Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Adopt and adapt: method claims are interpreted through possible or intended transformations and their realization, not through software notation first. | The pattern starts from transformation or enactment kind and separates method, mechanism, description, plan, and work. |
| Current scoped-effects and handlers work | Bosman, van den Berg, Tang, and Schrijvers, "A Calculus for Scoped Effects & Handlers", LMCS 20(4), 2024, arXiv:2304.09697; Matache, Lindley, Moss, Staton, Wu, and Yang, "Scoped Effects as Parameterized Algebraic Theories", ESOP 2024 extended version, arXiv:2402.03103. | Adopt: operation syntax, semantic handling, scope, resources, equations, and type information plus effect information are separate concerns. | The pattern refuses to repair `algorithm`, `program`, or `function` to `method` merely by programming-paradigm label. |
| Current graph and equivalence representation work | Tiurin, Barrett, Ghica, and Hu, "Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs", arXiv:2406.15882, v2 revised 2025-05-20. | Adapt: graph, query, equivalence, and rewrite structures can be representations without being ordered instructions. | Graph path, query, and table overreads are repaired with `C.2.P.DR` unless a direct graph, method, work, evidence, or gate claim is recovered. |
| Historical declarative versus imperative programming contrasts | Codd 1970; Kowalski 1979; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004; Deutsch 2013; Deutsch and Marletto 2015. | Reject as current SoTA; retain only as lineage and regression contrast. | Older slogans such as "declarative versus imperative" are used only as recognition cues; the repair recovers FPF kind and slot. |

Refresh this pattern when current work on constructor theory, process theory, effect systems, process modeling, practice theory, cultural-evolution work, graph and equivalence representations, or FPF's own method, work, role, discipline, and mechanism patterns changes the governing distinction among method, method description, formal substrate, mechanism, role assignment, work plan, dated work, cultural-evolution material, and evidence.

### A.3.1:12 - Relations

* **Builds on:** `A.1` holonic foundation, `A.1.1 U.BoundedContext`, `A.2` role, `A.2.1 U.RoleAssignment`, `A.2.2 U.Capability`.
* **Coordinates with:** `A.3.2` for method descriptions and method-relation descriptions; `A.3.3` for dynamics; `A.6.0` for formal-substrate declarations; `A.6.1` and `E.20` for mechanism claims; `C.29` for mathematical-lens use; `G.5` for method-family registries and selector outcomes; direct method-composition patterns such as `B.1.5` when order-sensitive method composition is current; `A.1.1` for bounded-context meanings hidden by practice wording; `A.2`, `A.2.1`, and `A.2.7` for role values, role assignments, and role relations hidden by practice wording; `A.15.2` for work plans; `A.15.1` for dated work; `C.20`, `C.36`, and `C.36.P` for discipline and cultural-evolution practice wording; `A.10` for evidence relations or provenance relations; `C.2.P.DR` for declarative representations overread as imperative routes or work sequences.
* **Informs:** `E.18` and `E.18.1` when transformation-flow-structure or P2W wording must keep flow-structure descriptions, graph/path mathematical expressions, method claims, and work claims separate.

### A.3.1:End

