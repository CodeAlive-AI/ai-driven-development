## A.3.2 - U.MethodDescription: Description Episteme for a Way of Doing

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### A.3.2:1 - Problem frame

**When the reusable way is still only a candidate.** A candidate account or mined behavioural model is not a `U.MethodDescription` merely because it is coherent, executable, process-shaped, or traceable to sources. First use `A.3.1.MR` while the reusable way is still being recovered. Apply this pattern only after the account's `EntityOfConcern` has been admitted as one `U.Method`, and only when that same episteme makes a substantive claim about the Method as a way of doing.

Use this pattern when engineers need reusable claims about how one Method is carried out and must keep those claims distinct from the representation, publication, approval, plan, or actual Work through which the Method is discussed or enacted. In FPF terms, decide whether an already identified `U.Episteme` is a `U.MethodDescription`: whether its `EntityOfConcern` is one admitted `U.Method` and its claims say something substantive about that Method as a way of doing.

**Plain reading.** A method description is the knowledge object whose claims say how one identified method is done. Code, text, or a diagram may represent those claims; a publication occurrence may make an edition available.

Recognizable working moments include:

* a maintenance team comparing a revised procedure with the method used to plan the next service window;
* a clinical team selecting a triage guideline while keeping guideline claims, approval, and patient-specific work separate;
* a production-planning team comparing scheduling-method claims while the MILP representation and solver runs change.

Use it when the working question is:

* which admitted `U.Method` is the episteme's `EntityOfConcern`;
* which claim states the method's transformation or enactment concern, applicability, precondition, effect, bound, or internal composition;
* whether anyone is proposing a use beyond membership; if so, what that use is, where it belongs, and which method claims it needs;
* which `C.29` representation corresponds to the claims, which publication occurrence makes the selected edition available, which publication form expresses it, and which `U.PresentationCarrier` bears that form—but only when the proposed use needs those distinctions;
* whether two epistemes concern the same A.3.1-identified Method and, separately, whether their claim content is equivalent for the proposed use; the later use sections carry any needed scheme correspondence, evidence-reliance, and assurance checks.

**Object being classified.** A.3.2 examines one already identified claim-bearing `U.Episteme` candidate and judges whether that same individual belongs to the dependent kind `U.MethodDescription`. For positive membership, the candidate episteme's C.2.1 `EntityOfConcern` must resolve to one admitted `U.Method`, and at least one of its claims must concern that Method as a way of doing. The Method is the internal subject of the episteme's claims, not a second candidate and not the object being classified. A.3.2 adds neither another episteme identity nor a binary description relation.

**Primary working reader.** An engineer, researcher, publisher, teacher, planner, or auditor who must identify or rely on reusable claims about a method before planning, enactment, comparison, audit, revision, publication, or teaching.

**Primary working concern.** Identify the claim-bearing episteme and its Method first. When someone proposes a further use, name that use and its subject pattern, then ask which claims the use needs and whether this edition contains them. With no proposed use, stop at membership.

**Primary viewpoint.** The practitioner selecting, comparing, or revising method descriptions while method identity and the surrounding representation and publication relations remain explicit.

**First useful move.** Name the candidate `U.Episteme`. Check two things: its C.2.1 `EntityOfConcern` is one admitted `U.Method`, and at least one claim says how that Method is done. If both hold, the same episteme is a `U.MethodDescription`; if either fails, it is not. Only then, if someone proposes a concrete further use, write that use's criterion and result as a separate subject assertion under its exact predicate, with an optional subject-pattern locator. Otherwise stop at membership.

**What goes wrong if missed.** A visible file or diagram is classified by its form, a mere mention is mistaken for a description, or an episteme about a relation structure among several Methods is treated as if it described one composite Method. Planning, enactment, audit, and review then rely on the wrong object.

**What this buys.** The project can identify, compare, revise, and reuse claims about one Method while keeping representation, publication, planned use, enactment, and evidence use distinct.

**Not this pattern when.** Do not infer membership from words such as `algorithm`, `program`, `proof`, `workflow`, `process`, `procedure`, `recipe`, or `model`. Ask what the sentence actually asserts. If its `EntityOfConcern` is not an admitted `U.Method`, or it says nothing substantive about that Method as a way of doing, A.3.2 does not apply. Use the pattern for the actual Method, selected structure, formal declaration, work plan, dated Work, evidence use, or publication use instead.

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

The C.2.1 claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme` remain the identity discriminators of the episteme; A.3.2 adds no second identity. Whether the claims are detailed, current, or reliable enough for a particular planning, enactment, comparison, audit, revision, publication, or teaching use is a separate evaluation. A new receiving use alone neither creates a new method description nor removes membership.

If someone claims empirical grounding, state the C.2.1 `EpistemeEmpiricalGroundingRelation`. If a proposed use depends on a test, write the tested claim, criterion, evidence path, and result under the evaluation, evidence, or assurance pattern that defines them. Do not add these as method-description fields or let a test change membership.

An assertion or description episteme about one dated Work occurrence may cite `methodDescriptionRef` when its claim depends on that description edition. Recover each performing `U.System` and its obtaining assignment of a local agential system-role kind under A.13. Independently admit the Work under A.15.1, including its obtaining `enactsMethod` relation to the Method. Only when precise assignment-bound attribution is claimed, use F.6 `performedUnderAssignment` with that same obtaining assignment of a separately declared `U.SystemRoleAssignment` species.

#### A.3.2:4.2 - Representation-agnostic stance

Begin with the claim-bearing episteme, then distinguish how its claims are made available:

* a `C.29` representation stands in a declared correspondence to the represented claims;
* an `E.24.PUB` publication form expresses the selected episteme edition for one publication use;
* a `U.PresentationCarrier` bears that publication form.

Only the claim-bearing episteme can meet the membership rule in 4.1; keep its representation, form, carrier, and publication occurrence separate.

The representation may use procedural text, code, a diagram, functional composition, a typed pipeline, a state machine, event rules, constraints, a solver formulation, a proof script, a statistical model, or a combination of notations. Notation choice does not decide membership. Read each assertion separately: use A.6.0 or C.29 when it asserts a formal object, A.6.1 or E.20 when it declares an operation family and laws, A.15.2 when it states intended Work, and A.10 or B.3 when another claim relies on it as evidence or assurance.

#### A.3.2:4.3 - Method-description claim content

The membership threshold is positive but small: at least one claim must answer a method-side question about the way of doing. A name, author, citation, catalogue entry, or approval status does not answer such a question. This threshold distinguishes description from mention; it is not a completeness test for a receiving use.

Name the receiving use before asking whether this method-description edition is adequate for it. A receiving use is not required for `U.MethodDescription` membership. If no use is current, stop at the membership result and make no adequacy claim.

| Proposed use | Where that use belongs | What to check in this edition |
| --- | --- | --- |
| membership only | A.3.2 judges the already identified C.2.1 episteme | no adequacy judgment; do not fabricate a receiver |
| preparing planned work | A.15.2 is the pattern for the `U.WorkPlan`; a gate, authority, or evaluation claim stays with its own pattern | does this edition state the applicability, preconditions, parameters, bounds, and stops that the plan cites? |
| enacting or recording dated work | A.15.1 is the pattern for the Work occurrence; its assertion may cite `methodDescriptionRef` when the edition matters | does this edition state the method claims used by that enactment or record? Actual participants and results still need their own relations. |
| comparing, revising, or auditing claim content | C.2.1 identifies each episteme and any persisted comparison or audit result; the concrete evaluation, evidence, or assurance claim stays with its subject pattern | which method claims are preserved, absent, stale, or incompatible for this comparison or audit? |
| publishing or teaching | C.2.1 is the pattern for the claim-bearing or teaching episteme; E.24.PUB is the pattern for publication occurrence and form; use A.15.1 only for teaching Work that actually happened | does this edition preserve the method distinctions needed by this audience or teaching use? |

A.3.2 creates no universal method-description-use relation. Name the concrete receiving object and the pattern that defines or tests the current claim about it. Comparing claim sets, revising a publication, or checking teaching content does not require a fabricated Work occurrence or decision object.

Then inspect the claim concerns that matter for that named use:

| Claim concern | Question for the named receiving use |
| --- | --- |
| Method described | Which admitted `U.Method` is the episteme's `EntityOfConcern`, and under which effective reference scheme is it identified? |
| Transformation or enactment concern | What way of changing, producing, deciding, learning, or checking does the method organize? |
| Generic participant and boundary meanings | Which kinds of entities, resources, conditions, or interfaces may participate in a future enactment, and what method-side meaning does each have? These are semantic claims, not `RelationSignature` SlotSpecs, `OperationAlgebra` positions, planned fillers, or actual participants. |
| Preconditions | Under which states, guards, invariants, participant conditions, or environmental conditions can the method be used? |
| Intended effects | Which postconditions, intended effects, preserved conditions, and failure semantics are claimed for the method? |
| Bounds | Which latency, precision, cost, safety, reliability, uncertainty, or other local bounds constrain the method? |
| System-role kinds and capabilities | Which local system-role kinds and capability thresholds matter for enactment? |
| Parameters | Which values may vary between work occurrences, over which ranges, and when are they bound? |
| Evaluation conditions | Which criterion compares which concrete Work occurrence, referent, measurement, or result, and which pattern contains the defining content for that comparison? |
| Internal composition | Which admitted methods are parts of one composite method, and what organization constructs that whole? |
| Variation, edition, and refinement | Which claim content is preserved or changed, and is the current claim about another episteme edition, equivalence of claim content, or refinement of the method itself? |
| Edition and publication use | Which episteme edition is relied on, and does its publication use affect currentness or availability? |

Calendars, assignees, work authorization, gate passage, and dated execution witnesses are governed by planning, assignment, gate, or work-occurrence patterns. They may cite a method description.

A `U.MethodDescription` describes one admitted Method. It is not the `RelationSignature` that declares participants for one relation kind, the A.6.1 `OperationAlgebra` content that declares arguments and results for an operation family, the `U.WorkPlan` that states intended work, a dated Work occurrence, or any actual-participation relation of that occurrence.

#### A.3.2:4.4 - Method-description acceptance and use boundaries

A project may accept, regulate, prefer, deprecate, or forbid a method description for one stated use, organization, or policy scope. Record that separate publication, gate, authority, or policy claim under its own pattern. It does not establish `U.MethodDescription` membership.

When a method description is used to prepare or enact work, keep the chain explicit:

1. C.2.1 identifies one episteme through its claim content, exact `EntityOfConcern`, and effective `U.ReferenceScheme`; A.3.2 judges that same episteme to be `U.MethodDescription`. Plainly saying that the method description describes the method is shorthand for this constitution and membership judgment, not another binary relation occurrence.
2. `U.WorkPlan` may cite that episteme when preparing dated work.
3. Recover each performing `U.System` and its obtaining assignment of a local agential system-role kind under A.13. A.15.1 independently admits the dated Work and its `enactsMethod` relation to the Method. If precise assignment-bound attribution is claimed, F.6 `performedUnderAssignment` uses that same obtaining assignment of a separately declared `U.SystemRoleAssignment` species. A separate assertion cites `methodDescriptionRef` only when its claim depends on that edition.
4. The word *result* is only a cue. Ask which claim is being made: an A.6.1 application returned a value, a referent changed under A.3.4, Work produced something under A.15.PROD, or a measurement, evaluation, delivery, or acceptance occurred. If the use needs a Work-to-result relation and no exact predicate is defined for it, keep Work and result separate and state `missing-predicate[work-to-result]`. A log, trace, measurement, or result episteme supports another claim only through its evidence relation.

#### A.3.2:4.5 - Method, mechanism, and formal-substrate boundary

Do not classify by the source word alone. First say in plain words what someone is trying to change, produce, select, derive, control, or maintain and what the sentence asserts about it. Then use `E.10.ARCH:3.1` to separate method, mechanism, formal-object, plan, Work, and result claims; write each claim under its own pattern.

For A.3.2 ask only: is this episteme about one admitted Method, and does at least one claim say how that Method is done? If the same source also asserts a mechanism, formal declaration, work plan, dated Work, evidence use, gate, result, publication, or temporal claim, state that claim separately.

Use these claim checks instead of forcing distinct claims into one generic relation:

* A **method-description membership judgment** identifies one admitted `U.Method` as the episteme's exact `EntityOfConcern` and finds at least one substantive claim about that method as a way of doing.
* A **method claim** states the reusable way of doing, its participant meanings, applicability, conditions, intended result or preserved condition, and bounds.
* A **formal-substrate claim** concerns the selected formal object, structure, invariant, or mathematical declaration used for reasoning.
* A **mechanism-declaration claim** concerns the law-governed operation family, direct subject and range fields, operation algebra, law set, admissibility predicates, and applicability. Transport, audit, realization, evaluation, and evidence-use relations remain separately governed neighboring claims.
* A **work claim** concerns one dated occurrence independently admitted under A.15.1: each performing System with its A.13 core, including an obtaining assignment of a separately declared species, the enacted Method, temporal extent, and containing System. Add F.6 attribution through that same assignment only when precise assignment-bound attribution is asserted. Add participant, resource, or work-to-referent claims only through relations that actually obtain; otherwise return the corresponding missing-governor result.

Connect these claims only through an admitted relation whose predicate and participants are present. If no pattern or declaration defines the needed relation, keep the objects separate rather than inferring dual typing.
Example: a `U.MethodDescription` episteme for a scheduling Method can meet the membership rule while a MILP file represents some of its claims. Another episteme may describe the mathematical formulation; a selector mechanism may declare operations over candidate Methods; a dated solver run is Work; and an issued production-schedule episteme is a separate result. Use that result as evidence only through a current A.10 path and its bounded disposition. Without that path, keep the result available but do not rely on it as evidence for another claim.

#### A.3.2:4.6 - Constructor and process-theory note

In the constructor-theory and process-theory interpretation used here, both informational and physical procedures are understood through possible or impossible transformations. That motivates a broad method-description kind without making software code privileged:

* an episteme about an information-transformation method may be represented through a program, proof script, or solver model;
* an episteme about a material, energetic, organizational, or mixed-transformation method may be represented through a procedure, lab protocol, or control recipe;
* an assertion or description about dated Work may cite a method description. Establish the performing System's A.13 core with its obtaining assignment, then independently admit the Work and its `enactsMethod` relation under A.15.1. Use F.6 `performedUnderAssignment` with that same assignment only for a claimed precise assignment-bound attribution;
* a mechanism may declare law-governed operation structure for transformations, but that mechanism claim is separate from the method-description claim.

This interpretation explains why FPF can treat many representation forms uniformly after the current claim and described method are recovered.

#### A.3.2:4.7 - Declarative representation boundary

Some method descriptions use declarative representations: constraint sets, graph patterns, state predicates, SQL-like queries, policy rules, e-graphs, monoidal diagrams, or process constraints. Do not translate such representations into an imperative route unless the method claim actually states an ordered action structure.

Even a representation that runs or is internally consistent may have more than one sound interpretation. If a comparison depends on variables and their bindings, surrounding context, or an e-graph kept across compiler stages, say what counts as equal. Agreement under one such rule does not by itself show whether the Method is the same, whether the claims are equivalent, or whether one episteme edition continued into another.

Use `C.2.P.DR` when a graph path, evidence path, query plan, predicate, checklist, publication face, or neighboring-pattern relation is treated as an action route by its form or layout alone. Recover the direct object or relation and any separate representation use, then check whether the source actually asserts the proposed order. State a genuine ordered Method or WorkPlan as its own subject assertion with the exact defining or constraining ClaimGraph.

#### A.3.2:4.8 - Composite methods and independent method structures

When claims concern relations among methods, first determine whether the related methods construct one admitted composite `U.Method`.

If admitted methods are actual method parts whose organization constitutes one composite method under `A.3.1` and, when order-sensitive composition is current, `B.1.5`, the composite `U.Method` remains the exact `EntityOfConcern`. A `U.MethodDescription` can make substantive claims about that composite method's internal organization without changing its object of concern to an independently selected structure.

Description nodes, workflow boxes, code blocks, proof-script blocks, diagram paths, and table rows are representation constituents. They do not become method parts by position in the description. A constituent can participate in method-holon composition only after the recovered object is itself an admitted `U.Method`.

If a selected relation structure instead connects several methods as alternatives, substitutes, fallbacks, comparison candidates, or members of a family without constituting one composite method, the selected `U.Structure` is the exact `EntityOfConcern` under `A.22` and C.2.1. The resulting episteme can describe that structure, but the present rule does not classify it as `U.MethodDescription`.

An algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural representation can be used to express or analyze either case. Its correspondence to claims is governed separately through `C.29`. A work plan, work occurrence, method-family registry, or selector result also keeps its own governed object and subject pattern.

### A.3.2:5 - Archetypal Grounding

Across the slices below, recognize the claim-bearing episteme before examining how it is represented or published. Ask in this order:

1. Which admitted `U.Method` is its exact `EntityOfConcern`?
2. Which claim says something substantive about that method as a way of doing?
3. Is anyone proposing a use beyond membership? If so, name the use, its subject pattern, and the claims it needs; if not, stop at membership.
4. When expression or availability matters, which `C.29` representation corresponds to the claims, which publication occurrence makes the selected edition available, which publication form expresses it, and which `U.PresentationCarrier` bears that form?

#### A.3.2:5.1 - Industrial procedure

A procedure episteme about `EtchAl2O3@FabA` qualifies when its claims state how the etching Method is done: gas-feed participant meanings, temperature bounds, chamber preconditions, intended etch profile, failure conditions, operator system-role kind, calibration capability threshold, or admitted parameter ranges.

A PDF publication form may express one edition of those claims, and a PLC ladder representation may correspond to some of them. The scheduled maintenance-window preparation is a `U.WorkPlan`; tool run `W-143` is Work. A metrology result supports another claim only through the evidence relation for that claim.

**Named-use replay — preparing `WP-Etch-MW-47`.** The maintenance planner needs four claims before drafting this A.15.2 `U.WorkPlan`: the chamber is empty, inert, and leak-check complete before gas feed; the method's temperature range is 58–62 °C; calibration is no more than 24 hours old; and pressure above the stated bound stops the run. `EtchAl2O3-Description-e7` passes A.3.2 membership because it concerns `EtchAl2O3@FabA` and says how that Method is done. It also states all four needed claims. To verify that this is the current edition, the planner checks its ClaimGraph against publication occurrence `Pub-Etch-e7`, publication form `EtchAl2O3-SOP-e7`, and carrier `FabA-MethodRepository-2026`, plus the source trace from `EtchDescriptionReleaseWork-e7`, performed under `EtchDescriptionMaintainerAssignment-4` with method trace `ClaimGraphReleaseCheck-v2`. A.10 path `EP-Etch-e7-Plan47` links those sources to claim `C-Etch-e7-has-Plan47-claims`. Its bounded use is citing e7 while drafting `WP-Etch-MW-47`; unsupported uses are gate passage, authorization, safe execution, and a claim that Work occurred. Its window reopens when e7, `RecipeWindow-Al2O3-3`, the calibration rule, or a source named in the path changes. `RelianceDisposition=pass` therefore supports citing e7 only for this drafting use.

`EtchAl2O3-Description-brief-e7` still passes membership because it concerns the same Method and states the gas-feed and temperature procedure. It omits the 24-hour calibration condition and pressure stop. A.10 path `EP-Etch-brief-e7-Plan47` points to that brief edition and cannot evidence the two missing claims, so `RelianceDisposition=blocked-current-use` applies to drafting `WP-Etch-MW-47`. Reopen after selecting an edition that states both claims; until then the planner stops or selects another edition. Membership is unchanged. If the result must persist, C.2.1 is the pattern for its result episteme and ClaimGraph, A.10 is the pattern for the evidence path and disposition, and A.15.2 is the pattern for the plan.

#### A.3.2:5.2 - Optimization model

A `U.MethodDescription` episteme for the scheduling Method qualifies when its exact `EntityOfConcern` is `JSScheduleV4@Plant2026` and its claims state how a production schedule is produced or evaluated. A MILP representation and an explicitly recovered solver-configuration representation can stand in declared correspondence to those claims.

A separate formal-substrate episteme can make claims about variables, constraints, objective, admissible solution set, or invariants. A publication form expressing that episteme may be borne by the same presentation carrier. A timestamped solver run is work. A selector mechanism, if declared, is governed by `A.6.1` and `E.20`. Solver search order does not by itself state the project work sequence.

#### A.3.2:5.3 - Proof script

An episteme about a reusable derivation or checking method qualifies when it identifies that `U.Method` exactly and makes a substantive claim about how the derivation or check is done. A proof-assistant script may represent those claims.

A concrete proof-checking session is work. Claims about a formal substrate, a theorem, or evidence for the theorem remain separately governed even when publication forms expressing those epistemes are borne by the same carrier. A publication occurrence makes a selected edition available to an audience for a bounded use.

#### A.3.2:5.4 - Clinical guideline

A guideline episteme qualifies when its exact `EntityOfConcern` is `AcuteAppendicitisTriage@HospitalContext` and its claims state the triage Method through patient-information and resource participant meanings, exclusions, decision criteria, relevant local system-role kinds and capabilities, intended effects, or failure response. A publication form expresses one selected edition, and a publication occurrence can make that edition available; approval status remains a separate claim.

Patient-specific dated enactment is a Work individual admitted under `U.Work`. If a causal claim relies on a triage disposition, diagnostic finding, or measurement result, name that premise and apply `C.28`. Merely using the guideline during Work establishes neither a causal effect nor a causal-use result.

#### A.3.2:5.5 - Workflow diagram

An episteme whose claims state one reusable method may qualify as `U.MethodDescription`; a BPMN or object-centric process model may represent those claims. A diagram can also represent a work plan, event-log model, or independently selected structure, so its notation does not settle the exact `EntityOfConcern`.

If readers treat the diagram as a route that tokens or workers must follow, compare that reading with the source claim. Keep an ordered sequence only when the method claim actually states one. When order comes only from layout, use `C.2.P.DR` and stop at the represented graph, constraints, objects, or events.

### A.3.2:6 - Bias-Annotation

This pattern mainly blocks six recurring biases:

* **carrier-as-description bias**: a PDF file, repository, screen, or presentation carrier is treated as the method description. Identify the episteme whose ClaimGraph is being read, then record its C.29 representation and publication relations separately;
* **description-as-method bias**: the representation is treated as the way of doing itself;
* **description-as-work bias**: executable or operational-looking representation is treated as dated work;
* **approval-as-proof bias**: accepted, approved, or regulated descriptions are treated as evidence, gate passage, or safe execution;
* **notation-prestige bias**: code, formal notation, or solver files are treated as more authoritative than procedures, diagrams, or guidelines. Compare the actual method claims; representation form supplies no priority;
* **imperative-metaphor bias**: graph, query, predicate, or process-model representation is treated as an ordered work-control claim.

First identify the claim-bearing episteme, the claim it makes, and the Method it concerns. When the use needs them, keep its C.29 representation, publication occurrence, publication form, and presentation carrier separate. State each additional plan, Work, evidence, gate, authority, mechanism, formal, or mathematical claim under its exact predicate or constraint with an optional subject-pattern locator.

### A.3.2:7 - Conformance Checklist

**CC-A3.2-1 (Episteme membership).** A.3.2 judges one already identified `U.Episteme` candidate. That same individual is a `U.MethodDescription` only when its C.2.1 `EntityOfConcern` is one admitted `U.Method` and at least one claim says how that Method is done. Representation form, publication form, carrier, approval, and use adequacy do not decide membership; no binary description relation is minted.

**CC-A3.2-2 (Positive description threshold).** The episteme must make at least one substantive claim about the method as a way of doing, such as its transformation or enactment concern, generic participant meanings, applicability, precondition, intended effect or preserved condition, bound, or internal composition. A name, citation, author, catalogue entry, or approval status alone is mention, not method-description membership.

**CC-A3.2-3 (No automatic trigger repair).** Wording such as `algorithm`, `program`, `proof`, `solver`, `workflow`, `process`, `procedure`, `recipe`, or `model` is only a cue. Classify the episteme as `U.MethodDescription` only after its claim and admitted Method pass CC-A3.2-1 and CC-A3.2-2.

**CC-A3.2-4 (Description not work).** Executable-looking material is not a Work occurrence. For a program run, proof-checking session, solver run, lab run, or clinical application, first recover every performing System's A.13 core, including its obtaining assignment of a separately declared species. Admit Work only after A.15.1 independently identifies the world-side occurrence, enacted Method, temporal extent, and containing System. Apply F.6 through that same assignment afterward only when precise assignment-bound attribution is claimed; a missing or failed F.6 attribution leaves independently admitted Work intact. Any participant, resource-use, or work-to-referent claim needs its own admitted relation; if none exists, return the corresponding missing-governor result.

**CC-A3.2-5 (Description not plan or authority).** A method description is not a work plan, gate decision, permission, approval, external-rule authorization, or evidence relation. Those claims may cite the description but require their own subject patterns.

**CC-A3.2-6 (Description not mechanism or declaration).** A method description is neither a `RelationSignature` nor A.6.1 `OperationAlgebra` content and does not close a mechanism claim. If reusable direct-relation participant declaration is current, use A.6.0 and A.6.5. If operation algebra, law set, admissibility predicates, or applicability is current, use `A.6.1`; transport, audit, realization, evaluation, and evidence-use relations remain with their direct patterns.

**CC-A3.2-7 (Description not formal substrate).** A method description does not close a formal-substrate or mathematical-lens claim. If variables, equations, invariants, structure, substrate, or mathematical payoff are current, use `A.6.0`, `C.29`, or the direct mathematical pattern.

**CC-A3.2-8 (No people or calendars inside the description claim).** A method description may state local system-role kinds and capability thresholds that bound admissible enactment. A claim that a particular System belongs to one of those kinds is a separate System-classification judgment. Named people or Systems, dates, schedules, launch values, assignment species and obtaining assignment occurrences, F.6 attributions, and Work witnesses belong to their planning, classification, assignment, or Work patterns.

**CC-A3.2-9 (Parameters and use time).** A method description may state parameter meanings and ranges. A `U.WorkPlan` names planned values against the declaration that gives them meaning. An actual participant or operation value requires an obtaining subject relation or A.6.1 application binding; otherwise keep it planned and return `missing-governor[actual-use]`.

**CC-A3.2-10 (Same subject versus equivalent descriptions).** Two descriptions concern the same `U.Method` only when their `EntityOfConcern` references resolve to the same A.3.1 method identity. A scheme difference may require an F.9 Bridge to interpret a comparison, but the Bridge does not establish Method identity. Shared subject also does not make the epistemes equivalent: state which claims are preserved, absent, incompatible, or inaccurate for the proposed use. Do not use executable agreement, renaming of bound variables, graph equivalence, or persistence across stages by itself to decide whether the Method is the same or different or the claims are equivalent.

**CC-A3.2-11 (Edition and refinement).** A later file or episteme edition does not by itself refine the Method. Use C.2.1 for the edition relation and state which description claims a comparison preserves or strengthens. Then use A.3.1 to decide whether one Method continues or two Methods are being compared, and apply its refinement test only to the world-side Method claim. A one-use comparison may stop as claim content under A.6.RCD; it creates no Method relation occurrence.

**CC-A3.2-12 (Nondeterminism).** When a description permits search, optimization, sampling, nondeterministic choice, or learned behavior, state the admissible result range and the criterion for evaluating actual Work or results. Name the pattern or declaration that defines that criterion.

**CC-A3.2-13 (Cross-context and semantic-locality boundary).** F.9 answers only whether a Bridge obtains between two `SchemeSenseCell` values. For proposed reuse, state a separate C.2.1 claim with the use, direction, correspondence rule, loss tolerance, and affirmative or negative polarity. Positive polarity alone is not reliance. An ordinary below-threshold use with no assurance claim needs `RelianceDisposition=pass` on its A.10 path. When an assurance claim is made or the B.3 threshold is met, enter B.3: positive assurance requires a current positive claim and sufficient record, while no claim or an insufficient record stops or narrows the assurance use. A negative or absent use claim, non-passing A.10 disposition, or non-positive B.3 outcome stops or narrows reuse even while the Bridge obtains. Changes of reference scheme, unit, role taxonomy, claim scope, or model use stay under their own patterns.

**CC-A3.2-14 (Declarative representation).** Use `C.2.P.DR` when a declarative representation's form or layout is being treated as sufficient to prescribe work. Recover the direct object or relation and any representation use. Assert the proposed route, dispatch, call, or work-control sequence only when its exact predicate is defined and current facts satisfy it; otherwise retain the direct object or representation without that unsupported action claim.

**CC-A3.2-15 (Causal-use boundary).** A method description may describe intervention assignment, target-trial emulation, realized-counterfactual sampling, simulation, or causal-evidence collection. It does not by itself establish causal use. If causal effect, intervention success, counterfactual comparison, causal fairness, or policy effect is claimed, use `C.28`.

### A.3.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Treating executable text as sufficient Method identity. | Identify the claim-bearing episteme and the Method it concerns. Membership needs one substantive method claim; C.29 is the pattern for representation correspondence, E.24.PUB is the pattern for publication, and A.15.1 is the pattern for a run that actually happened. |
| Treating a Work log as a method description solely because it records a sequence. | The log is an episteme about dated Work, not the Work or a method description by being recorded. Identify the occurrence under A.15.1; cite or write a separate method description only when its claims pass the membership rule. |
| Inferring safe use solely from protocol approval. | Separate method description, approval or gate claim, safety evidence, work plan, and work occurrence. |
| Leaving the optimization-model claim unresolved. | Ask whether the episteme says how a scheduling Method works or instead states variables, constraints, and an objective for a formal model. Keep the solver run as Work and any selector mechanism under A.6.1/E.20. |
| Inferring project-work dispatch from a query-plan layout. | A database plan or graph may represent ordering without commanding project Work. Use `C.2.P.DR` when layout is being read as dispatch; write a WorkPlan or ordered Method only when its own claim states that sequence. |
| Inferring the workflow sequence solely from a diagram route. | Check whether the method claim states the sequence. If the route is only a graph path, event trace, or drawing convention, keep it in the representation; do not turn it into a WorkPlan or performed Work. |
| Conflating a new file version with refinement of the Method. | Separate the C.2.1 edition relation, a comparison of description claims, and any refinement relation between Methods. A file version establishes none of them. |
| "SOPs are notes, code is the real spec." | Neither notation establishes membership. Compare what each episteme claims about the Method. Ask adequacy only for a concrete proposed use; comparison, publication revision, and teaching-content review require no fabricated Work or decision. |

### A.3.2:9 - Consequences

| Benefit | Cost or caution |
| --- | --- |
| Method descriptions become reusable across notations. | Users must separate method identity from description form. |
| Audits can distinguish description, plan, work, evidence, and authority. | The first repair is to identify the claim-bearing episteme, its Method, and one substantive method claim; replacing vocabulary is not enough. |
| Software, lab, industrial, organizational, and proof-centered descriptions can be compared under one FPF kind. | Some files contain several current claims and must be split into several subject-pattern statements. |
| Equivalent descriptions can be declared without forcing identical notation. | Equivalence and refinement need local criteria. |
| Declarative representations can be used without being turned into ordered work-control claims. | An order inferred solely from form or layout needs `C.2.P.DR`; a supported order needs its subject assertion with its defining or constraining ClaimGraph. |

#### A.3.2:9.1 - Quick use cards

* **Claims first.** The claim-bearing episteme can be `U.MethodDescription`; its exact `U.Method`, C.29 representation, publication occurrence, publication form, and `U.PresentationCarrier` remain distinct.
* **Executable is still not a run.** Runs are Work individuals admitted under `U.Work` only when A.15.1 grounds their occurrences.
* **Representation is not enough.** Read what the code, proof, solver file, procedure, diagram, or workflow actually asserts and name its subject. Only the claim-bearing episteme can pass A.3.2 membership; C.29 keeps the representation correspondence.
* **Mechanism needs its declaration.** Use `A.6.1` when operation algebra, laws, admissibility, or applicability is current; keep transport, audit, realization, evaluation, and evidence-use relations under their direct patterns.
* **Math needs its own claim.** Use `A.6.0` and `C.29` when formal substrate or mathematical-lens use is current.
* **No ordered-action overread.** Use `C.2.P.DR` when declarative representations are overread as ordered action structures.

### A.3.2:10 - Rationale

Projects need reusable claims about ways of doing before any dated work occurs. Treating a file as the method description by appearance hides two decisions that later work needs: which episteme is being relied on, and which admitted method its claims concern. The positive claim threshold makes this distinction usable without demanding a complete procedure card.

The pattern is representation-agnostic because a method can be described through procedural text, code, diagrams, mathematical notation, protocols, or combinations of them. The episteme can be revised and evaluated while its C.29 representations, publication occurrences, publication forms, and presentation carriers change independently. This separation lets a project compare descriptions and judge fitness for a receiving use without turning notation, approval, publication, or enactment into kind membership.

### A.3.2:11 - SoTA-Echoing

| Source line and status, qualified 2026-08-26 | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current constructor-theory and process-theory work | Gogioso et al., "Constructor Theory as Process Theory", EPTCS 397, 2023, arXiv:2401.05364; Deutsch and Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Adopt and adapt: descriptions stay close to transformation claims without becoming the transformation or Work occurrence. | The pattern separates MethodDescription, Method, mechanism, WorkPlan, Work, and evidence across physical, informational, organizational, and mathematical examples. |
| Current scoped-effects and handlers work | Bosman et al., ["A Calculus for Scoped Effects & Handlers"](https://arxiv.org/abs/2304.09697), 2024; Matache et al., ["Scoped Effects as Parameterized Algebraic Theories"](https://arxiv.org/abs/2402.03103), 2024; Kura, ["On Complete Categorical Semantics for Effect Handlers"](https://arxiv.org/abs/2602.03275), 2026. | Adopt the separation of syntax, handling, scope, resources, equations, and semantic model; reject the inference from executable coherence to one uniquely determined semantics. | An executable-looking episteme may describe a Method, but form or one working interpretation does not by itself settle its Method, mechanism law, semantic equivalence, or success. |
| Current binding-aware equality representation | Tiurin, Ghica, and Hu, ["E-Graphs With Bindings"](https://arxiv.org/abs/2505.00807), 2025; Zucker, ["Lifting E-Graphs: A Function Isn't a Constant"](https://arxiv.org/abs/2606.22734), 2026. | Adapt: variables, binders, and contexts need explicit representation semantics; ordinary graph equality is not enough. | When equivalence depends on binding or context, state that comparison basis. Alpha-equivalent or graph-equivalent representations do not automatically identify one Method or equivalent claim content. |
| Current persistent equality representation | Merckx et al., ["E-Graphs as a Persistent Compiler Abstraction"](https://arxiv.org/abs/2602.16707), 2026. | Adapt: an equality representation may persist across several intermediate-representation levels while its expression changes. | Persistence of one representation structure across compiler stages is a C.29 representation fact; it does not establish episteme-edition continuity, Method identity, MethodDescription membership, or performed Work. |
| Historical declarative-versus-imperative programming contrasts | Codd 1970; Kowalski 1979; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004. | Reject as current SoTA; retain only as lineage and regression contrast. | Older slogans remain useful recognition cues, but the reader still asks what the artifact asserts and which FPF object that claim concerns. |

**Qualification and smallest reopen.** Reopen only when a source or an FPF dependency materially changes the membership test, the boundary between representation and semantics, or a named receiving-use decision. Revise the affected row and its matching subsection, case, checklist item, or public cue. A new representation paper or tool release with no such effect does not reopen the whole pattern.

### A.3.2:12 - Relations

* **Builds on:** `C.2.1` for the identity, grounding, and edition relations of the same claim-bearing episteme; `A.3.1` for the exact `U.Method`; and `E.24.UK` for admission of the dependent U-kind.
* **Coordinates with:** `A.3.1` and `B.1.5` for actual Method parts, Method identity, and composite-Method organization; `A.22` for an independently selected structure among several Methods; `A.1.1` only when an independently selected `BoundedModelUseStructure` changes the proposed use; `F.9` only for cross-context `SchemeSenseCell` correspondence; `C.2.1` for the separate claim that one obtaining Bridge suits one bounded use; `A.10` for ordinary evidence reliance on that claim and `B.3` only for the assurance or material-threshold branch; `C.29` for representation correspondence; `E.24.PUB` for publication occurrence and form; `A.15.2` for `U.WorkPlan`; `A.15.1` for `U.Work`; `A.2` for local system-role kinds and System-classification judgments; `A.2.1` for assignment species and obtaining assignment occurrences; F.6 for Work–assignment attribution; `A.2.2` for capability thresholds; and `C.28` for causal-use claims.
* **Separates from:** `A.6.0` formal-substrate declarations; `C.29` mathematical-lens use; `A.6.1 U.Mechanism`; `E.20` mechanism-meaning introduction and revision.
* **Uses for precision restoration:** `F.19` for the connected reading of wording that leaves the claim, object, or relation unclear; `E.10`, `E.10.ARCH`, `F.18`, or `C.2.P.DR` for a remaining word, kind, durable naming, or declarative-representation question.

### A.3.2:End

