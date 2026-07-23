## A.3.2 - U.MethodDescription: Description Episteme for a Way of Doing

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### A.3.2:1 - Problem frame

Use this pattern when engineers need reusable claims about how one method is carried out and must keep those claims distinct from the representation, publication, approval, plan, or actual work through which the method is discussed or enacted. In FPF terms, decide whether an already identified `U.Episteme` is a `U.MethodDescription`: whether its exact `EntityOfConcern` is one admitted `U.Method` and its claims say something substantive about that method as a way of doing.

**Plain reading.** A method description is the knowledge object whose claims say how one identified method is done. Code, text, or a diagram may represent those claims; a publication occurrence may make an edition available; neither fact decides membership.

Recognizable working moments include:

* a maintenance team comparing a revised procedure with the method used to plan the next service window;
* a clinical team selecting a triage guideline while keeping guideline claims, approval, and patient-specific work separate;
* a production-planning team comparing scheduling-method claims while the MILP representation and solver runs change.

Use it when the working question is:

* which admitted `U.Method` is the exact `EntityOfConcern`;
* which claim states the method's transformation or enactment concern, applicability, precondition, effect, bound, or internal composition;
* which work or decision should rely on those claims, and whether the claims are adequate for that receiving use;
* which `C.29` representation corresponds to the claims, which publication occurrence makes the selected edition available, which publication form expresses that edition, and which `U.PresentationCarrier` bears the form, when those distinctions affect the work;
* whether the exact EntityOfConcern references resolve to the same A.3.1-reidentified method, and, as a separate question, whether the claim contents are equivalent for the receiving use; when effective `U.ReferenceScheme` values differ, an exact F.9 Bridge can establish only the current `SenseCell` correspondence and admitted use, not method identity or claim equivalence.

**Primary EntityOfConcern.** The exact `EntityOfConcern` is the admitted `U.Method` being described. `U.MethodDescription` is the same `U.Episteme` individual already identified through `C.2.1`; the dependent kind adds a membership judgment, not another described entity or another identity rule.

**Primary working reader.** An engineer or researcher who must rely on reusable claims about a method before planning, enactment, comparison, audit, or revision.

**Primary working concern.** Identify the claim-bearing episteme and exact method first, then judge separately whether the claims are adequate for the current work or decision.

**Primary viewpoint.** The practitioner selecting, comparing, or revising method descriptions while method identity and the surrounding representation and publication relations remain explicit.

**First useful move.** Name the exact `U.Method`, then point to at least one claim that says how that method is done. Name the work or decision that will use the claim. Evaluate adequacy for that receiving use separately from membership.

**What goes wrong if missed.** A visible file or diagram is classified by its form, a mere mention is mistaken for a description, or an episteme about a relation structure among several methods is treated as if it described one composite method. Planning, enactment, audit, and review then rely on the wrong governed object.

**What this buys.** The project can identify, compare, revise, and reuse method descriptions while keeping the described `U.Method`, `RelationSignature`, `OperationAlgebra`, C.29 representations, publication occurrences and forms, presentation carriers, work plans, work occurrences, and evidence under their own governing patterns.

**Not this pattern when.** Do not infer membership from words such as `algorithm`, `program`, `proof`, `workflow`, `process`, `procedure`, `recipe`, or `model`. Recover the current claim and exact governed object. If no admitted `U.Method` is the exact `EntityOfConcern`, or the episteme makes no substantive claim about its way of doing, this membership rule does not apply. Use the governing pattern for the actual method, selected structure, formal substrate, `RelationSignature`, `OperationAlgebra`, work plan, work occurrence, evidence use, or publication use.

### A.3.2:2 - Problem

Without a precise `U.MethodDescription` distinction, projects collapse several different claims:

1. **Description as run.** A flowchart, repository, executable, lab protocol, or solver file is treated as if it were the dated work occurrence.
2. **Description as method semantics.** A notation or file is treated as the method itself, so equivalent descriptions look like competing methods and different methods can hide behind one document name.
3. **Description as plan or authority.** A protocol, dashboard cue, gate-looking entry, or approved procedure note is treated as a work plan, permission, gate passage, or evidence result.
4. **Description as declaration, mechanism, or formal substrate.** A proof script, algorithm, model, or rule set is treated as if it already were a `RelationSignature`, an A.6.1 operation declaration, a mechanism law set, or a mathematical substrate.
5. **Imperative overread.** A declarative representation, graph path, query plan, constraint model, or state predicate is interpreted as an ordered work-control claim.
6. **Subject identity and description equivalence collapse.** Two epistemes that concern the same method are treated as equivalent despite incompatible claims, or a notational difference is used to fork method identity without the A.3.1 reidentification rule.

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

`U.MethodDescription` is a same-individual dependent kind of `U.Episteme`. Membership holds when the already identified episteme has one admitted `U.Method` as its exact `EntityOfConcern` and its claims, interpreted under the effective `U.ReferenceScheme`, make at least one substantive claim about that method as a way of doing. Such a claim may state the method's transformation or enactment concern, generic participant meanings, applicability, precondition, intended effect or preserved condition, bound, or internal method composition. These are claims about method semantics, not planned assignments or actual participation. Naming the method, giving bibliographic metadata, or stating approval alone does not establish membership.

The C.2.1 claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme` remain the identity discriminators of the episteme; A.3.2 adds no second identity. Whether the claims are detailed, current, or reliable enough for a particular planning, enactment, comparison, audit, or review use is a separate evaluation. A new receiving use alone neither creates a new method description nor removes membership.

Empirical grounding, when current, uses the exact C.2.1 `EpistemeEmpiricalGroundingRelation`. Formal or empirical testing and receiving-use evaluation use the separately governed evaluation, evidence, or assurance relations required by that use. Neither grounding nor testing is an intrinsic method-description field or an identity or membership condition.

The assertion or description episteme about an exact dated Work occurrence admitted under `U.Work` may cite the method description through `methodDescriptionRef` when its receiving claim depends on that edition. The independently obtaining `performedBy` and `enactsMethod` relations involving that Work individual connect it to the exact performer assignment and enacted method. The description itself neither performs work nor is enacted.

#### A.3.2:4.2 - Representation-agnostic stance

Begin with the claim-bearing episteme, then distinguish how its claims are made available:

* a `C.29` representation stands in a declared correspondence to the represented claims;
* an `E.24.PUB` publication form expresses the selected episteme edition for one publication use;
* a `U.PresentationCarrier` bears that publication form.

These are different objects and relations. None becomes `U.MethodDescription` by appearance. Only the claim-bearing episteme, not its representation, form, carrier, or publication occurrence, can meet the membership rule in 4.1.

The representation may use procedural text, code, a diagram, functional composition, a typed pipeline, a state machine, event rules, constraints, a solver formulation, a proof script, a statistical model, or a combination of notations. Notation choice does not decide membership. The same representation may also correspond to claims about a formal substrate, mechanism, work plan, or evidence; recover each current claim and governed object separately.

#### A.3.2:4.3 - Method-description claim content

The membership threshold is positive but small: at least one claim must answer a method-side question about the way of doing. A name, author, citation, catalogue entry, or approval status does not answer such a question. This threshold distinguishes description from mention; it is not a completeness test for a receiving use.

For the work or decision that will rely on the episteme, inspect the claim concerns that matter there:

| Claim concern | Question for the current work or decision |
| --- | --- |
| Method described | Which admitted `U.Method` is the exact `EntityOfConcern`, and under which effective reference scheme is it identified? |
| Transformation or enactment concern | What way of changing, producing, deciding, learning, or checking does the method organize? |
| Generic participant and boundary meanings | Which kinds of entities, resources, conditions, or interfaces may participate in a future enactment, and what method-side meaning does each have? These are semantic claims, not `RelationSignature` SlotSpecs, `OperationAlgebra` positions, planned fillers, or actual participants. |
| Preconditions | Under which states, guards, invariants, participant conditions, or environmental conditions can the method be used? |
| Intended effects | Which postconditions, intended effects, preserved conditions, and failure semantics are claimed for the method, without asserting an actual result? |
| Bounds | Which latency, precision, cost, safety, reliability, uncertainty, or other local bounds constrain the method? |
| Roles and capabilities | Which role kinds and capability thresholds matter for enactment? |
| Parameters | Which values may vary between work occurrences, over which ranges, and when are they bound? |
| Evaluation conditions | Which separately governed criteria or comparators would evaluate a work occurrence, affected referent, measurement, evaluation result, or other direct object for the receiving use? |
| Internal composition | Which admitted methods are parts of one composite method, and what organization constructs that whole? |
| Variation, edition, and refinement | Which claim content is preserved or changed, and is the current claim about another episteme edition, equivalence of claim content, or refinement of the method itself? |
| Edition and publication use | Which episteme edition is relied on, and does its publication use affect currentness or availability? |

Calendars, assignees, work authorization, gate passage, and dated execution witnesses are governed by planning, assignment, gate, or work-occurrence patterns. They may cite a method description but do not become its claim content merely because they appear beside it.

A `U.MethodDescription` describes one exact method. It is not the `RelationSignature` that declares participant SlotSpecs for one admitted direct relation kind, not the A.6.1 `OperationAlgebra` content that declares typed arguments and results for one operation family, not the `U.WorkPlan` that states particular intended work, and not a dated Work occurrence admitted under `U.Work` or any of that occurrence's actual participant relations.

#### A.3.2:4.4 - Method-description acceptance and use boundaries

A method description may be accepted, regulated, preferred, deprecated, or forbidden in a bounded context. That is a separate publication, gate, authority, or policy claim. Such a claim neither establishes membership nor turns the description into work, evidence, a gate decision, or a mechanism.

When a method description is used to prepare or enact work, keep the chain explicit:

1. C.2.1 identifies one episteme through its claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme`; A.3.2 judges that same episteme to be `U.MethodDescription`. Plainly saying that the method description describes the method is shorthand for this constitution and membership judgment, not another binary relation occurrence.
2. `U.WorkPlan` may cite that episteme when preparing dated work.
3. Independently obtaining `performedBy -> U.RoleAssignment` and actual `enactsMethod -> U.Method` relations involve the exact dated Work occurrence admitted under `U.Work`, not the method description; a separate assertion cites `methodDescriptionRef` only when the receiving claim depends on that description edition.
4. A boundary word such as *result* does not select one work-result relation. Recover the exact affected entity, actual change, A.6.1 operation-result binding, local A.15.PROD production-work, entity-identity-inception, or production-completion claim, measurement or evaluation result, delivery, acceptance, or other direct relation current for the use. Result, log, trace, and measurement epistemes participate in evidence or assurance only through their governing relations.

#### A.3.2:4.5 - Method, mechanism, and formal-substrate boundary

Do not decide method, mechanism, or formal substrate by the source word alone. When a source expression or project concern appears to name changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For this host, keep the local question thin: does this already identified `U.Episteme` describe the exact `U.Method` named as its EntityOfConcern? If the same source expression or project concern also raises mechanism, formal-substrate, work-plan, dated-work, evidence, source-use, gate, result, publication, or temporal claims, identify those governed objects and direct relations separately and apply their own patterns.

Use these claim checks instead of forcing distinct claims into one generic relation:

* A **method-description membership judgment** identifies one admitted `U.Method` as the episteme's exact `EntityOfConcern` and finds at least one substantive claim about that method as a way of doing.
* A **method claim** concerns the context-defined semantic way of doing.
* A **formal-substrate claim** concerns the selected formal object, structure, invariant, or mathematical declaration used for reasoning.
* A **mechanism-declaration claim** concerns the law-governed operation family, direct subject and range fields, operation algebra, law set, admissibility predicates, and applicability. Transport, audit, realization, evaluation, and evidence-use relations remain separately governed neighboring claims.
* A **work claim** concerns a dated occurrence with its performer assignment, enacted method, temporal extent, resources, affected referent, and separately governed actual participant relations; witnesses and results retain their own direct governors.

Connect these claims only through the exact direct relations their governing patterns admit. Do not infer that one individual instantiates both `U.Method` and `U.Mechanism`, or that a method description is work, merely because one expression supports several claims.
Example: a scheduling-method episteme can meet the membership rule while a MILP file represents some of its claims. A separately identified episteme can make claims about the mathematical formulation as a formal substrate; a selector mechanism can declare admissible selection operations over candidate methods; a scheduled solver run is work; an issued production-schedule episteme remains a separately governed result and can support another claim only through an exact evidence-use relation. Those claims may be linked, but one does not close the others.

#### A.3.2:4.6 - Constructor and process-theory note

In the constructor-theory and process-theory interpretation used here, both informational and physical procedures are understood through possible or impossible transformations. That motivates a broad method-description kind without making software code privileged:

* an episteme about an information-transformation method may be represented through a program, proof script, or solver model;
* an episteme about a material, energetic, organizational, or mixed-transformation method may be represented through a procedure, lab protocol, or control recipe;
* an assertion or description about an exact dated Work occurrence admitted under `U.Work` may cite a method description, while the independently obtaining `performedBy` and `enactsMethod` relations involving that Work individual identify the performer assignment and enacted method; no actor or `TransformerRole` follows from the description;
* a mechanism may declare law-governed operation structure for transformations, but that mechanism claim is separate from the method-description claim.

This note is not a license to call every algorithm-looking expression a method description. It only explains why FPF can treat many representation forms uniformly after the current claim and described method are recovered.

#### A.3.2:4.7 - Declarative representation boundary

Some method descriptions use declarative representations: constraint sets, graph patterns, state predicates, SQL-like queries, policy rules, e-graphs, monoidal diagrams, or process constraints. Do not translate such representations into an imperative route unless the method claim actually states an ordered action structure.

If the source turns a graph path, evidence path, query plan, predicate, checklist, publication face, or pattern relation into a route, dispatch, call sequence, work-control sequence, or work workflow by metaphor, apply `C.2.P.DR` before assigning the direct governing pattern.

#### A.3.2:4.8 - Composite methods and independent method structures

When claims concern relations among methods, first determine whether the related methods construct one admitted composite `U.Method`.

If admitted methods are actual method parts whose organization constitutes one composite method under `A.3.1` and, when order-sensitive composition is current, `B.1.5`, the composite `U.Method` remains the exact `EntityOfConcern`. A `U.MethodDescription` can make substantive claims about that composite method's internal organization without changing its object of concern to an independently selected structure.

Description nodes, workflow boxes, code blocks, proof-script blocks, diagram paths, and table rows are representation constituents. They do not become method parts by position in the description. A constituent can participate in method-holon composition only after the recovered object is itself an admitted `U.Method`.

If a selected relation structure instead connects several methods as alternatives, substitutes, fallbacks, comparison candidates, or members of a family without constituting one composite method, the selected `U.Structure` is the exact `EntityOfConcern` under `A.22` and C.2.1. The resulting episteme can describe that structure, but the present rule does not classify it as `U.MethodDescription`.

An algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural representation can be used to express or analyze either case. Its correspondence to claims is governed separately through `C.29`. A work plan, work occurrence, method-family registry, or selector result also keeps its own governed object and governing pattern.

### A.3.2:5 - Archetypal Grounding

Across the slices below, recognize the claim-bearing episteme before examining how it is represented or published. Ask in this order:

1. Which admitted `U.Method` is its exact `EntityOfConcern`?
2. Which claim says something substantive about that method as a way of doing?
3. Which work or decision will rely on the claim, and is the episteme adequate for that receiving use?
4. When expression or availability matters, which `C.29` representation corresponds to the claims, which publication occurrence makes the selected edition available, which publication form expresses it, and which `U.PresentationCarrier` bears that form?

#### A.3.2:5.1 - Industrial procedure

A procedure episteme about `EtchAl2O3@FabA` qualifies when its claims state how the etching method is done: gas-feed participant meanings, temperature bounds, chamber preconditions, intended etch profile, failure conditions, operator role kind, calibration capability threshold, or admitted parameter ranges.

A PDF publication form may express one edition of those claims, and a PLC ladder representation may correspond to some of them. Their visible forms do not establish membership. The scheduled maintenance-window preparation is `U.WorkPlan`; tool run `W-143` is a Work individual admitted under `U.Work`; an exact metrology measurement result can support another claim only through the governing evidence relation.

#### A.3.2:5.2 - Optimization model

A scheduling-method episteme qualifies when its exact `EntityOfConcern` is `JSScheduleV4@Plant2026` and its claims state how a production schedule is produced or evaluated. A MILP representation and an explicitly recovered solver-configuration representation can stand in declared correspondence to those claims.

A separate formal-substrate episteme can make claims about variables, constraints, objective, admissible solution set, or invariants. A publication form expressing that episteme may be borne by the same presentation carrier, but the carrier does not make the claims or establish their truth. A timestamped solver run is work. A selector mechanism, if declared, is governed by `A.6.1` and `E.20`. Solver search order does not by itself state the project work sequence.

#### A.3.2:5.3 - Proof script

An episteme about a reusable derivation or checking method qualifies when it identifies that `U.Method` exactly and makes a substantive claim about how the derivation or check is done. A proof-assistant script may represent those claims. The script's notation does not establish membership.

A concrete proof-checking session is work. Claims about a formal substrate, a theorem, or evidence for the theorem remain separately governed even when publication forms expressing those epistemes are borne by the same carrier. A publication occurrence, not the form or carrier, makes a selected edition available to an audience for a bounded use.

#### A.3.2:5.4 - Clinical guideline

A guideline episteme qualifies when its exact `EntityOfConcern` is `AcuteAppendicitisTriage@HospitalContext` and its claims state the triage method through patient-information and resource participant meanings, exclusions, decision criteria, relevant role kinds and capabilities, intended effects, or failure response. A publication form expresses one selected edition, and a publication occurrence can make that edition available; approval status remains a separate claim.

Patient-specific dated enactment is a Work individual admitted under `U.Work`. If a separately governed triage disposition, diagnostic finding, measurement result, or other exact effect is used for a causal claim, apply `C.28`; neither enactment nor causal use changes method-description membership.

#### A.3.2:5.5 - Workflow diagram

An episteme whose claims state one reusable method may qualify as `U.MethodDescription`; a BPMN or object-centric process model may represent those claims. A diagram can also represent a work plan, event-log model, or independently selected structure, so its notation does not settle the exact `EntityOfConcern`.

If the diagram is read as a route that tokens or workers must follow, check whether ordered enactment is genuinely claimed by the method. If a graph, constraint, object, or event structure has merely been turned into a route by wording, use `C.2.P.DR` and recover the direct governing pattern.

### A.3.2:6 - Bias-Annotation

This pattern mainly blocks six recurring biases:

* **carrier-as-description bias**: a PDF file, repository, screen, or presentation carrier is treated as the method description instead of recovering the claim-bearing episteme and its exact representation or publication relations;
* **description-as-method bias**: the representation is treated as the way of doing itself;
* **description-as-work bias**: executable or operational-looking representation is treated as dated work;
* **approval-as-proof bias**: accepted, approved, or regulated descriptions are treated as evidence, gate passage, or safe execution;
* **notation-prestige bias**: code, formal notation, or solver files are treated as more authoritative than procedures, diagrams, or guidelines without recovering the claim-bearing epistemes and their governed objects;
* **imperative-metaphor bias**: graph, query, predicate, or process-model representation is treated as an ordered work-control claim.

The repair is to recover the current claim, its exact governed object, and the claim-bearing episteme first. Then distinguish any C.29 representation correspondence, publication occurrence, publication form, and presentation carrier, and keep method, work, plan, evidence, gate, authority, mechanism, formal-substrate, and mathematical-lens claims in their governing patterns.

### A.3.2:7 - Conformance Checklist

**CC-A3.2-1 (Episteme membership).** `U.MethodDescription` is the same individual as an already identified `U.Episteme`. Its exact `EntityOfConcern` is one admitted `U.Method`; representation form, publication form, carrier, approval, and use adequacy do not decide membership.

**CC-A3.2-2 (Positive description threshold).** The episteme must make at least one substantive claim about the method as a way of doing, such as its transformation or enactment concern, generic participant meanings, applicability, precondition, intended effect or preserved condition, bound, or internal composition. A name, citation, author, catalogue entry, or approval status alone is mention, not method-description membership.

**CC-A3.2-3 (No automatic trigger repair).** `Algorithm`, `program`, `proof`, `solver`, `workflow`, `process`, `procedure`, `recipe`, and `model` wording must not be repaired to `U.MethodDescription` until the current claim is recovered and the exact described `U.Method` is identified.

**CC-A3.2-4 (Description not work).** A method description is not a work occurrence. Executability does not change this: a program run, proof-checking session, solver run, lab run, or clinical application is a Work individual admitted under `U.Work` only when the A.15.1 occurrence basis is recoverable at the needed grain and the exact performer, method, temporal, containing-system, affected-referent, binding, and resource-use relations obtain independently.

**CC-A3.2-5 (Description not plan or authority).** A method description is not a work plan, gate decision, permission, approval, external-rule authorization, or evidence relation. Those claims may cite the description but require their own governing patterns.

**CC-A3.2-6 (Description not mechanism or declaration).** A method description is neither a `RelationSignature` nor A.6.1 `OperationAlgebra` content and does not close a mechanism claim. If reusable direct-relation participant declaration is current, use A.6.0 and A.6.5. If operation algebra, law set, admissibility predicates, or applicability is current, use `A.6.1`; transport, audit, realization, evaluation, and evidence-use relations remain with their direct patterns.

**CC-A3.2-7 (Description not formal substrate).** A method description does not close a formal-substrate or mathematical-lens claim. If variables, equations, invariants, structure, substrate, or mathematical payoff are current, use `A.6.0`, `C.29`, or the direct mathematical pattern.

**CC-A3.2-8 (No people or calendars inside the description claim).** A method description may state role kinds and capability thresholds that bound admissible enactment. Named people, dates, schedules, launch values, and work witnesses belong to work planning, role assignment, or work occurrence claims.

**CC-A3.2-9 (Parameters and use time).** Parameters may be stated as method semantics or described by `U.MethodDescription`. A `U.WorkPlan` may state planned values only against an exact governed declaration. An actual participant or operation value is established only through its exact direct subject relation or A.6.1 operation-application binding; neither the method description nor a work record supplies a generic binding relation.

**CC-A3.2-10 (Same subject versus equivalent descriptions).** Two method descriptions concern the same `U.Method` when their exact EntityOfConcern references resolve to the same method reidentified under A.3.1 and the semantic-locality relations required by the use. That shared subject does not make the epistemes equivalent. A claim-equivalence judgment must state which method-description claims are preserved; incompatible, incomplete, or inaccurate claims can concern the same method while receiving different adequacy results. Different notation, control structure, or representation style by itself neither splits method identity nor establishes description equivalence.

**CC-A3.2-11 (Edition and refinement).** A later episteme edition uses the exact C.2.1 `EpistemeEditionRelation` and does not by itself refine the method. A method-description comparison must state which claims are preserved or strengthened. A method-refinement claim must instead identify the exact methods and use A.3.1, B.1.5, or another direct method-relation owner; a new file version establishes none of these claims.

**CC-A3.2-12 (Nondeterminism).** If the method description permits search, optimization, sampling, nondeterministic choice, or learned behavior, it must state the admissible intended-effect range and the separately governed criteria needed to evaluate actual work or results; the description establishes neither.

**CC-A3.2-13 (Cross-context and semantic-locality boundary).** Cross-context reuse creates no generic bridge or alignment relation. Use F.9 only for exact cross-context `SenseCell` correspondence and admitted use; govern effective-reference-scheme change, unit transformation, role-taxonomy use, assumptions, acceptance criteria, claim scope, and selected model use under their exact direct patterns. Name identity alone is insufficient.

**CC-A3.2-14 (Declarative representation).** If a method description contains declarative representations, do not overread them as ordered work-control claims. Use `C.2.P.DR` when route, path, call, dispatch, work-control sequence, workflow, or lifecycle language hides the represented object or direct governing pattern.

**CC-A3.2-15 (Causal-use boundary).** A method description may describe intervention assignment, target-trial emulation, realized-counterfactual sampling, simulation, or causal-evidence collection. It does not by itself establish causal use. If causal effect, intervention success, counterfactual comparison, causal fairness, or policy effect is claimed, use `C.28`.

### A.3.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The code is the method." | Recover the claim-bearing episteme and exact `U.Method`. The episteme is `U.MethodDescription` only when it meets the positive claim threshold. Identify separately whether a code expression is used as a `C.29` representation, whether a publication form expresses the selected edition, and which carrier bears that form; a run is a Work individual admitted under `U.Work` only on the A.15.1 occurrence basis. |
| "Yesterday's log is our procedure." | The log is an episteme that may describe or evidence exact work through its governing relation; it is not the work or method description by being recorded. Recover the dated occurrence and cite or write the method description separately. |
| "The approved protocol proves safe use." | Separate method description, approval or gate claim, safety evidence, work plan, and work occurrence. |
| "The optimization model is the process." | Recover whether the current claim is method description, formal substrate, method, mechanism, work plan, work, or evidence. |
| "The query plan calls the next step." | Check whether this is a database plan, method description, formal representation, or metaphorical overread; use `C.2.P.DR` when needed. |
| "The diagram's route is the workflow." | Recover whether the route is graph path, method sequence, work plan, event trace, or diagram convention. |
| "The new version refines the old one." | Distinguish a C.2.1 episteme edition, an equivalence or adequacy judgment over description claims, and a refinement relation between methods. State the preserved or strengthened content and use the direct owner; a file version establishes none of the three. |
| "SOPs are notes, code is the real spec." | Neither notation establishes membership. Compare the claim-bearing epistemes by their exact methods, substantive method claims, and adequacy for the current work or decision; govern each representation separately. |

### A.3.2:9 - Consequences

| Benefit | Cost or caution |
| --- | --- |
| Method descriptions become reusable across notations. | Users must separate method identity from description form. |
| Audits can distinguish description, plan, work, evidence, and authority. | The first repair is to recover the current claim and exact governed object, then apply the membership rule; a vocabulary replacement is not enough. |
| Software, lab, industrial, organizational, and proof-centered descriptions can be compared under one FPF kind. | Some files contain several current claims and must be split into several governing-pattern statements. |
| Equivalent descriptions can be declared without forcing identical notation. | Equivalence and refinement need local criteria. |
| Declarative representations can be used without being turned into ordered work-control claims. | Route-like language needs `C.2.P.DR` or a direct governing-pattern assignment. |

#### A.3.2:9.1 - Quick use cards

* **Claims first.** The claim-bearing episteme can be `U.MethodDescription`; its exact `U.Method`, C.29 representation, publication occurrence, publication form, and `U.PresentationCarrier` remain distinct.
* **Executable is still not a run.** Runs are Work individuals admitted under `U.Work` only when A.15.1 grounds their occurrences.
* **Representation is not enough.** Code, proof, solver, procedure, diagram, and workflow wording requires recovery of the current claim and exact governed object.
* **Mechanism needs its declaration.** Use `A.6.1` when operation algebra, laws, admissibility, or applicability is current; keep transport, audit, realization, evaluation, and evidence-use relations under their direct patterns.
* **Math needs its own claim.** Use `A.6.0` and `C.29` when formal substrate or mathematical-lens use is current.
* **No ordered-action overread.** Use `C.2.P.DR` when declarative representations are overread as ordered action structures.

### A.3.2:10 - Rationale

Projects need reusable claims about ways of doing before any dated work occurs. Treating a file as the method description by appearance hides two decisions that later work needs: which episteme is being relied on, and which admitted method its claims concern. The positive claim threshold makes this distinction usable without demanding a complete procedure card.

The pattern is representation-agnostic because a method can be described through procedural text, code, diagrams, mathematical notation, protocols, or combinations of them. The episteme can be revised and evaluated while its C.29 representations, publication occurrences, publication forms, and presentation carriers change independently. This separation lets a project compare descriptions and judge fitness for a receiving use without turning notation, approval, publication, or enactment into kind membership.

### A.3.2:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current constructor-theory and process-theory work | Gogioso, Wang-Mascianica, Waseem, Scandolo, and Coecke, "Constructor Theory as Process Theory", EPTCS 397, 2023, arXiv:2401.05364; Deutsch and Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Adopt and adapt: descriptions are kept close to transformation claims without becoming the transformation or work occurrence. | The pattern separates method description, method, mechanism, work plan, work, and evidence across physical, informational, organizational, and mathematical examples. |
| Current scoped-effects and handlers work | Bosman, van den Berg, Tang, and Schrijvers, "A Calculus for Scoped Effects & Handlers", LMCS 20(4), 2024, arXiv:2304.09697; Matache, Lindley, Moss, Staton, Wu, and Yang, "Scoped Effects as Parameterized Algebraic Theories", ESOP 2024 extended version, arXiv:2402.03103. | Adopt: operation syntax, semantic handling, scope, resources, equations, and type information plus effect information are separate concerns. | Executable-looking descriptions are not automatically method semantics, mechanism law, work, or proof of success. |
| Current graph and equivalence representation work | Tiurin, Barrett, Ghica, and Hu, "Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs", arXiv:2406.15882, v2 revised 2025-05-20. | Adapt: graph, query, equivalence, and rewrite structures can be representations without being ordered instructions. | Declarative method-description representations are repaired with `C.2.P.DR` when wording turns them into ordered work-control claims. |
| Historical declarative versus imperative programming contrasts | Codd 1970; Kowalski 1979; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004. | Reject as current SoTA; retain only as lineage and regression contrast. | Older slogans remain useful recognition cues, but the repair recovers the current claim and governed object instead of choosing one programming-paradigm label. |

Refresh this pattern when current work on process theory, effect systems, executable specifications, process modeling, graph and equivalence representations, or FPF's own method, method-description, work, mechanism, and mathematical-lens patterns changes the governing distinction.

### A.3.2:12 - Relations

* **Builds on:** `C.2.1` for the identity, grounding, and edition relations of the same claim-bearing episteme; `A.3.1` for the exact `U.Method`; and `E.24.UK` for admission of the dependent U-kind.
* **Coordinates with:** `A.3.1` and `B.1.5` for actual method parts, method identity, and composite-method organization; `A.22` for an independently selected structure among several methods; `A.1.1` only when an independently selected `BoundedModelUseStructure` changes the current use; `F.9` only for exact cross-context `SenseCell` correspondence and admitted use; `C.29` for representation correspondence; `E.24.PUB` for publication occurrence and form; `A.15.2 U.WorkPlan`; `A.15.1 U.Work`; `A.2` and `A.2.1` for role and role-assignment claims; `A.2.2` for capability thresholds; `A.10` and `B.3` for evidence and assurance; `C.28` for causal-use claims.
* **Separates from:** `A.6.0` formal-substrate declarations; `C.29` mathematical-lens use; `A.6.1 U.Mechanism`; `E.20` mechanism-meaning introduction and revision.
* **Uses for precision restoration:** `E.10`, `E.10.ARCH`, `F.18`, and `C.2.P.DR` when method-like or representation-like wording hides the current claim, governed object, or direct governing pattern.

### A.3.2:End

