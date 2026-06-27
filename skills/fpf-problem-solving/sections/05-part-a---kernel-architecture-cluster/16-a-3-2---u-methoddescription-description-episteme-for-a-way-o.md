## A.3.2 - U.MethodDescription: Description Episteme for a Way of Doing

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### A.3.2:1 - Problem frame

Use this pattern when a project needs to say what text, code, diagram, rule set, solver formulation, proof script, SOP, protocol, or process model **describes a method**.

Use it when the working question is:

* which `U.Method` is being described;
* which representation states the fields needed for reuse, review, planning, audit, or enactment;
* whether two descriptions preserve the same method identity in one bounded context;
* which parameters, preconditions, effects, admissible outcomes, and acceptance criteria are stated by the description;
* whether an executable file, proof script, workflow diagram, or optimization model is only a method description, or whether a different FPF claim is current.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.MethodDescription`: an `U.Episteme` that describes a `U.Method` in some representation.

**First useful move.** Name the method being described, the bounded context in which its identity is judged, the representation form, and the fields by which work can later cite or enact the described method.

**What goes wrong if missed.** Code becomes "the method", a workflow diagram becomes work, an approved protocol becomes evidence of safe execution, a proof script becomes mechanism law, or a declarative representation becomes an ordered work-control claim.

**What this buys.** The project can improve, compare, version, audit, and reuse method descriptions without collapsing them into method semantics, work plans, dated work, mechanisms, mathematical substrates, gates, authority claims, or evidence relations.

**Not this pattern when.** Do not use this pattern merely because the source says `algorithm`, `program`, `proof`, `workflow`, `process`, `procedure`, `recipe`, or `model`. First recover the slot. The current claim may instead be `A.3.1 U.Method`, `A.6.0` formal-substrate declaration, `C.29` mathematical-lens use, `A.6.1` or `E.20` mechanism meaning, `A.15.2 U.WorkPlan`, `A.15.1 U.Work`, an evidence relation, a publication-use relation, or quote-only source wording.

### A.3.2:2 - Problem

Without a precise `U.MethodDescription` distinction, projects collapse several different claims:

1. **Description as run.** A flowchart, repository, executable, lab protocol, or solver file is treated as if it were the dated work occurrence.
2. **Description as method semantics.** A notation or file is treated as the method itself, so equivalent descriptions look like competing methods and different methods can hide behind one document name.
3. **Description as plan or authority.** A protocol, dashboard cue, gate-looking entry, or approved procedure note is treated as a work plan, permission, gate passage, or evidence result.
4. **Description as mechanism or formal substrate.** A proof script, algorithm, model, or rule set is treated as if it already declared operation algebra, laws, admissibility predicates, transport, or mathematical substrate.
5. **Imperative overread.** A declarative representation, graph path, query plan, constraint model, or state predicate is interpreted as an ordered work-control claim.
6. **Unstated equivalence.** Two descriptions intended to describe the same method are not given a local identity criterion, so teams fork method meaning by accident.

### A.3.2:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Representation versus method semantics | Many representations can describe one method; one representation can also carry other claims. |
| Reuse versus enactment | A method description should be reusable before any particular work occurrence happens. |
| Precision versus notation plurality | SOPs, code, proof scripts, solver models, process models, and lab protocols can all be useful without forcing one algorithmic paradigm. |
| Reviewability versus overclaim | A description may be reviewable and executable, but that does not make it evidence, authorization, work, or mechanism law. |
| Identity versus variation | Variants, refinements, parameter values, and contextual bridges must be visible enough to prevent silent method drift. |

### A.3.2:4 - Solution

#### A.3.2:4.1 - Definition

`U.MethodDescription` is an `U.Episteme` that describes a `U.Method` in a representation such as text, code, diagram, model, rule set, proof script, protocol, or executable form.

A method description is the episteme that describes a way of doing. Associated method semantics, work occurrences, work plans, performers, capabilities, mechanisms, formal substrates, and evidence relations remain separate governed values. A system in a transformer-like role may enact a method during `U.Work` while using a method description, but the description itself does not enact anything.

Working distinction:

| Claim being made | Governing pattern |
| --- | --- |
| context-defined semantic way of doing | `A.3.1 U.Method` |
| representation that describes that way of doing | `A.3.2 U.MethodDescription` |
| selected formal object, invariant, substrate, or mathematical declaration | `A.6.0`, `C.29`, or another direct mathematical pattern |
| law-governed operation structure, admissibility predicate set, transport, or realization relation | `A.6.1`, with `E.20` when mechanism meaning is introduced or revised |
| planned dated work, work preparation, schedule, or launch value | `A.15.2 U.WorkPlan` plus gate or authority patterns when a gate or authority claim is current |
| dated occurrence with witnesses, logs, measurements, and outputs | `A.15.1 U.Work` |
| evidence relation or provenance relation for a claim, effect, or use | `A.10`, `B.3`, `G.6`, or the direct evidence pattern or assurance pattern |

#### A.3.2:4.2 - Representation-agnostic stance

`U.MethodDescription` does not privilege imperative procedures or software code. A method description can be written as:

* an SOP, checklist, BPMN diagram, PLC ladder, shell script, or operational protocol;
* functional composition, typed pipeline, process model, state machine, or event rule set;
* SAT, SMT, MILP, theorem-prover, proof-assistant, or constraint-model file;
* statistical or ML training, evaluation, inference, or deployment description;
* lab protocol, clinical guideline, control recipe, or organizational rule set;
* a hybrid form that combines several representations.

These forms are `U.MethodDescription` only when the current claim is that they describe a method. A solver formulation may also expose a formal substrate. A program run may be `U.Work`. A mechanism card may declare laws and admissibility predicates. A proof may be evidence for a claim. A workflow diagram may describe a method or a work plan depending on the fields it actually states. Representation style alone does not decide the FPF kind.

#### A.3.2:4.3 - Method-description fields

A useful method description usually makes these fields recoverable in the current bounded context:

| Field | What to recover |
| --- | --- |
| Method described | the named `U.Method` and the bounded context where the name has meaning |
| Inputs and outputs | accepted inputs, produced outputs, resources, interfaces, ports, and relevant standards |
| Preconditions | states, guards, invariants, input conditions, and required environmental conditions |
| Effects | postconditions, guaranteed effects, produced result kinds, and failure semantics |
| Bounds | latency, precision, cost, safety envelope, reliability, uncertainty, or other local bounds |
| Role and capability requirements | role kinds and capability thresholds required for enactment, not named people |
| Parameters | values that may vary across work occurrences, defaults, ranges, and binding time |
| Acceptance criteria | how a work occurrence or result is judged against the method description |
| Variants and refinement | declared deltas, preserved interface, strengthened preconditions or effects, and identity criterion |
| Source and edition | publication, file, document, or source relation when reliance depends on a version |

Calendars, assignees, work authorization, gate passage, and dated execution witnesses are not part of the method-description claim. They may cite the method description, but they are governed elsewhere.

#### A.3.2:4.4 - Method-description acceptance and use boundaries

A method description may be accepted, regulated, preferred, deprecated, or forbidden in a bounded context. That is a separate publication, gate, authority, or policy claim. The acceptance label does not turn the description into work, evidence, a gate decision, or a mechanism.

When a method description is used to prepare or enact work, keep the chain explicit:

1. `U.MethodDescription` describes `U.Method`.
2. `U.WorkPlan` may cite that description when preparing dated work.
3. A system in a role assignment enacts the method during `U.Work`.
4. Work outputs, logs, traces, measurements, or publications may become evidence only through the governing evidence or assurance pattern.

#### A.3.2:4.5 - Method, mechanism, and formal-substrate boundary

Do not decide method, mechanism, or formal substrate by the source word alone. When a source expression or project concern appears to name changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For this host, keep the local question thin: is the current claim an episteme that describes a method? If the same source expression or project concern also raises method, mechanism, formal-substrate, work-plan, dated-work, evidence, source, gate, result, publication, or temporal claims, keep those values linked only by explicit relation positions and apply their own governing patterns.

The local position checks are:
* In **method-description position**, the claim is that a representation describes a method.
* In **method position**, the claim is the context-defined semantic way of doing.
* In **formal-substrate position**, the claim is the selected formal object, structure, invariant, or mathematical declaration used for reasoning.
* In **mechanism position**, the claim is the law-governed operation algebra, law set, admissibility predicates, applicability, transport, audit relation set, or realization relation.
* In **work position**, the claim is a dated occurrence with witnesses and outputs.

Those links remain typed relation-position links to separately governed claims. Do not assign the same typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits such dual typing; a slot-position label names the relation position, not a new ontology.

Example: a MILP file can describe a scheduling method; the mathematical formulation can be a formal substrate; a selector mechanism can declare admissible selection operations over candidate methods; a scheduled solver run is work; the resulting production schedule can become evidence for a separate claim. Those claims may be linked, but one does not close the others.

#### A.3.2:4.6 - Constructor and process-theory note

In the constructor-theory and process-theory interpretation used here, both informational and physical procedures are understood through possible or impossible transformations. That motivates a broad method-description kind without making software code privileged:

* a program, proof script, or solver model may describe a method for information transformation;
* an SOP, lab protocol, or control recipe may describe a method for material, energetic, organizational, or mixed transformation;
* a method description can be used by a system in a transformer-like role during work;
* a mechanism may declare law-governed operation structure for transformations, but that mechanism claim is separate from the method-description claim.

This note is not a license to call every algorithm-looking expression a method description. It only explains why FPF can treat many representation forms uniformly after the current slot is recovered.

#### A.3.2:4.7 - Declarative representation boundary

Some method descriptions use declarative representations: constraint sets, graph patterns, state predicates, SQL-like queries, policy rules, e-graphs, monoidal diagrams, or process constraints. Do not translate such representations into an imperative route unless the method claim actually states an ordered action structure.

If the source turns a graph path, evidence path, query plan, predicate, checklist, publication face, or pattern relation into a route, dispatch, call sequence, work-control sequence, or work workflow by metaphor, apply `C.2.P.DR` before assigning the direct governing pattern.

#### A.3.2:4.8 - Method-relation descriptions and algebra lenses

A method description may describe not only one `U.Method`, but also a selected `MethodRelationStructure@BoundedContext`: the relation structure by which methods or method families compose, refine, substitute, iterate, dispatch, or fall back in one bounded context.

Keep the positions separate:

- the method relation structure is the selected structure among method-side values;
- the method description is the episteme that describes that structure;
- algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation is a mathematical or representation lens when it is used to analyze or express the structure;
- a work plan or dated work occurrence is governed by `A.15.2` or `A.15.1`;
- a method-family registry or selector outcome is governed by `G.5` when that registry or selector result is current.

Do not treat "method algebra", "workflow graph", "pipeline", or "selector calculus" as a method, work plan, performed work, or method-family registry merely by word choice. Recover which value the representation describes and name the governing pattern before using the label.

### A.3.2:5 - Archetypal Grounding

Across the slices below, `U.MethodDescription` is recognized by its relation to a method, not by its carrier or notation:

```text
In this bounded context, which representation describes which U.Method, for which later work, review, planning, audit, or enactment use?
```

#### A.3.2:5.1 - Industrial procedure

`SOP_Etch_v7.pdf` and a PLC ladder file describe `EtchAl2O3@FabA`.

The method description states gas-flow inputs, temperature bounds, chamber preconditions, expected etch profile, failure conditions, operator role kind, calibration capability threshold, and accepted parameter ranges.

The scheduled maintenance-window run is `U.WorkPlan`; tool run `W-143` is `U.Work`; metrology output becomes evidence only when an evidence pattern governs the relevant claim or use; gas-flow equations may require `C.29` or `A.6.0`.

#### A.3.2:5.2 - Optimization model

A MILP model and solver configuration describe `JSScheduleV4@Plant2026` when the current claim is the method for producing a production schedule.

The same files may also carry formal-substrate claims: variables, constraints, objective, admissible solution set, and invariants. A solver run with timestamps is work. A selector mechanism, if declared, lives under `A.6.1` and `E.20`.

Do not infer that solver search order is the project work sequence.

#### A.3.2:5.3 - Proof script

A proof-assistant script may describe the method for deriving a theorem, expose a formal substrate, or serve as evidence for a claim. The method-description claim is current only when the script is used as the representation of the reusable way of deriving or checking.

A concrete proof-checking session is work. A theorem publication or source citation is publication use or evidence use. The algebraic or type-theoretic structure may require a mathematical-lens or formal-substrate declaration.

#### A.3.2:5.4 - Clinical guideline

A clinical guideline describes `AcuteAppendicitisTriage@HospitalContext` when it states the triage method: inputs, exclusions, decision criteria, role kind, capability requirements, expected result, and failure response.

Regulatory acceptance, authorization to use, patient-specific dated enactment, and causal-use claims are separate. If the resulting work is used for a causal claim, apply `C.28`.

#### A.3.2:5.5 - Workflow diagram

A BPMN or object-centric process model can be a method description when it states the reusable method. It can also be a work-plan view, source data, event-log model, process-mining representation, or publication face.

If the diagram is being interpreted as a route that tokens or workers must follow, check whether that route claim is truly part of the method. If it is only a diagrammatic overread of constraints, objects, events, or graph structure, use `C.2.P.DR` and the direct governing pattern.

### A.3.2:6 - Bias-Annotation

This pattern mainly blocks six recurring biases:

* **carrier-as-description bias**: the PDF, repository, file, screen, or publication face is treated as the method description without checking what episteme it carries;
* **description-as-method bias**: the representation is treated as the way of doing itself;
* **description-as-work bias**: executable or operational-looking representation is treated as dated work;
* **approval-as-proof bias**: accepted, approved, or regulated descriptions are treated as evidence, gate passage, or safe execution;
* **notation-prestige bias**: code, formal notation, or solver files are treated as more real than SOPs, diagrams, or guidelines without field recovery;
* **imperative-metaphor bias**: graph, query, predicate, or process-model representation is treated as an ordered work-control claim.

The repair is to recover what the representation describes, then keep neighboring method, work, plan, evidence, gate, authority, mechanism, formal-substrate, and mathematical-lens claims in their governing patterns.

### A.3.2:7 - Conformance Checklist

**CC-A3.2-1 (Episteme).** `U.MethodDescription` is an `U.Episteme` describing a `U.Method`. It may be expressed in text, code, diagram, model, rule set, or executable form, but the publication form or representation form does not determine the current FPF claim.

**CC-A3.2-2 (Method linkage).** A method description must name or recover the `U.Method` it describes and the bounded context where the method identity is judged.

**CC-A3.2-3 (No automatic trigger repair).** `Algorithm`, `program`, `proof`, `solver`, `workflow`, `process`, `procedure`, `recipe`, and `model` wording must not be repaired to `U.MethodDescription` until the current slot is recovered.

**CC-A3.2-4 (Description not work).** A method description is not a work occurrence. Executability does not change this: program runs, proof-checking sessions, solver runs, lab runs, and clinical applications are `U.Work` when dated occurrence fields are current.

**CC-A3.2-5 (Description not plan or authority).** A method description is not a work plan, gate decision, permission, approval, external-rule authorization, or evidence relation. Those claims may cite the description but require their own governing patterns.

**CC-A3.2-6 (Description not mechanism).** A method description does not close a mechanism claim. If operation algebra, law set, admissibility predicates, applicability, transport, audit, or realization relation is current, use `A.6.1` and `E.20` as needed.

**CC-A3.2-7 (Description not formal substrate).** A method description does not close a formal-substrate or mathematical-lens claim. If variables, equations, invariants, structure, substrate, or mathematical payoff are current, use `A.6.0`, `C.29`, or the direct mathematical pattern.

**CC-A3.2-8 (No people or calendars inside the description claim).** A method description may state role kinds and capability thresholds required for enactment. Named people, dates, schedules, launch values, and work witnesses belong to work planning, role assignment, or work occurrence claims.

**CC-A3.2-9 (Parameters and binding time).** Parameters may be declared in the method or method description. Concrete run values are bound in `U.WorkPlan` or `U.Work` according to the current claim.

**CC-A3.2-10 (Equivalence).** Two method descriptions describe the same `U.Method` in a bounded context only when they preserve the same method identity: accepted inputs, preconditions, effects, bounds, and acceptance criteria. Different notation, control structure, or representation style is not enough to split or merge method identity.

**CC-A3.2-11 (Refinement).** A refinement claim must state what is preserved and what is strengthened: interface, preconditions, postconditions, effects, bounds, or accepted outcomes. Refinement is not implied by a new file version.

**CC-A3.2-12 (Nondeterminism).** If the method description permits search, optimization, sampling, nondeterministic choice, or learned behavior, it must state the admissible outcome set and acceptance criteria needed to judge work results.

**CC-A3.2-13 (Context bridge).** Cross-context reuse requires an explicit bridge or alignment relation for terms, units, roles, assumptions, and acceptance criteria. Name identity alone is insufficient.

**CC-A3.2-14 (Declarative representation).** If a method description contains declarative representations, do not overread them as ordered work-control claims. Use `C.2.P.DR` when route, path, call, dispatch, work-control sequence, workflow, or lifecycle language hides the represented object or direct governing pattern.

**CC-A3.2-15 (Causal-use boundary).** A method description may describe intervention assignment, target-trial emulation, realized-counterfactual sampling, simulation, or causal-evidence collection. It does not by itself establish causal use. If causal effect, intervention success, counterfactual comparison, causal fairness, or policy effect is claimed, use `C.28`.

### A.3.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The code is the method." | If the claim is about the repository or executable form, use `U.MethodDescription`; if it is about the semantic way of doing, name the `U.Method`; if it is about a run, use `U.Work`. |
| "Yesterday's log is our procedure." | The log is work evidence or a work record. Write or cite the method description separately. |
| "The approved protocol proves safe use." | Separate method description, approval or gate claim, safety evidence, work plan, and work occurrence. |
| "The optimization model is the process." | Recover whether the current claim is method description, formal substrate, method, mechanism, work plan, work, or evidence. |
| "The query plan calls the next step." | Check whether this is a database plan, method description, formal representation, or metaphorical overread; use `C.2.P.DR` when needed. |
| "The diagram's route is the workflow." | Recover whether the route is graph path, method sequence, work plan, event trace, or diagram convention. |
| "The new version refines the old one." | State the preserved interface and strengthened preconditions, effects, outcomes, or bounds. |
| "SOPs are notes, code is the real spec." | Treat both as possible method descriptions; judge by recoverable method fields, not representation prestige. |

### A.3.2:9 - Consequences

| Benefit | Cost or caution |
| --- | --- |
| Method descriptions become reusable across notations. | Users must separate method identity from description form. |
| Audits can distinguish description, plan, work, evidence, and authority. | The first repair step is slot recovery, not a vocabulary replacement. |
| Software, lab, industrial, organizational, and proof-centered descriptions can be compared under one FPF kind. | Some files contain several current claims and must be split into several governing-pattern statements. |
| Equivalent descriptions can be declared without forcing identical notation. | Equivalence and refinement need local criteria. |
| Declarative representations can be used without being turned into ordered work-control claims. | Route-like language needs `C.2.P.DR` or a direct governing-pattern assignment. |

#### A.3.2:9.1 - Quick use cards

* **Written way is not the way itself.** A method description describes a `U.Method`.
* **Executable is still not a run.** Runs are `U.Work`.
* **Representation is not enough.** Code, proof, solver, SOP, diagram, and workflow words require slot recovery.
* **Mechanism needs laws.** Use `A.6.1` and `E.20` when operation algebra, laws, admissibility, transport, audit, or realization is current.
* **Math needs its own claim.** Use `A.6.0` and `C.29` when formal substrate or mathematical-lens use is current.
* **No ordered-action overread.** Use `C.2.P.DR` when declarative representations are overread as ordered action structures.

### A.3.2:10 - Rationale

FPF needs `U.MethodDescription` because a project often works with recipes, programs, protocols, diagrams, and formal files before any dated work occurs. Those representations can be improved, versioned, compared, audited, and cited; treating them as the method itself, the run, the authorization, or the evidence destroys those distinctions.

The pattern is intentionally representation-agnostic. A method description is an episteme about a way of doing, not a privileged notation. Code and solver files can be method descriptions, but so can SOPs, guidelines, lab protocols, proof scripts, and diagrams when the current claim is that they describe a method.

### A.3.2:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current constructor-theory and process-theory work | Gogioso, Wang-Mascianica, Waseem, Scandolo, and Coecke, "Constructor Theory as Process Theory", EPTCS 397, 2023, arXiv:2401.05364; Deutsch and Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Adopt and adapt: descriptions are kept close to transformation claims without becoming the transformation or work occurrence. | The pattern separates method description, method, mechanism, work plan, work, and evidence across physical, informational, organizational, and mathematical examples. |
| Current scoped-effects and handlers work | Bosman, van den Berg, Tang, and Schrijvers, "A Calculus for Scoped Effects & Handlers", LMCS 20(4), 2024, arXiv:2304.09697; Matache, Lindley, Moss, Staton, Wu, and Yang, "Scoped Effects as Parameterized Algebraic Theories", ESOP 2024 extended version, arXiv:2402.03103. | Adopt: operation syntax, semantic handling, scope, resources, equations, and type information plus effect information are separate concerns. | Executable-looking descriptions are not automatically method semantics, mechanism law, work, or proof of success. |
| Current graph and equivalence representation work | Tiurin, Barrett, Ghica, and Hu, "Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs", arXiv:2406.15882, v2 revised 2025-05-20. | Adapt: graph, query, equivalence, and rewrite structures can be representations without being ordered instructions. | Declarative method-description representations are repaired with `C.2.P.DR` when wording turns them into ordered work-control claims. |
| Historical declarative versus imperative programming contrasts | Codd 1970; Kowalski 1979; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004. | Reject as current SoTA; retain only as lineage and regression contrast. | Older slogans remain useful recognition cues, but the repair recovers FPF kind and slot instead of choosing one programming-paradigm label. |

Refresh this pattern when current work on process theory, effect systems, executable specifications, process modeling, graph and equivalence representations, or FPF's own method, method-description, work, mechanism, and mathematical-lens patterns changes the governing distinction.

### A.3.2:12 - Relations

* **Builds on:** `A.3.1 U.Method`; `A.1.1 U.BoundedContext`; episteme and publication machinery where source, edition, or publication use is current.
* **Coordinates with:** `A.15.2 U.WorkPlan`; `A.15.1 U.Work`; `A.2` and `A.2.1` for role and role-assignment claims; `A.2.2` for capability thresholds; `A.10` and `B.3` for evidence and assurance; `C.28` for causal-use claims.
* **Separates from:** `A.6.0` formal-substrate declarations; `C.29` mathematical-lens use; `A.6.1 U.Mechanism`; `E.20` mechanism-meaning introduction and revision.
* **Uses for precision restoration:** `E.10`, `E.10.ARCH`, `F.18`, and `C.2.P.DR` when method-like or representation-like wording hides the governed slot.

### A.3.2:End

