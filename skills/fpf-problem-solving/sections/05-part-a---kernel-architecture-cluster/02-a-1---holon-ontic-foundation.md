## A.1 - Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)

> **Type:** Part A architectural ontology pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.1:0 - Use This When

Use this pattern when a project must say what kind of thing is under concern before it can rely on parts, wholes, boundaries, acting systems, roles, methods, work, architecture, or descriptions.

Typical moments:

- a team calls everything a "system" and then asks physical or operational questions about theories, documents, models, dashboards, or descriptions;
- an episteme is treated as an acting agent that decides, performs work, authorizes, promises, or revises itself;
- a product, organization, machine, document family, research program, discipline, work occurrence, or model family must be treated as a whole with parts;
- a list, batch, fleet, pool, clientele, community, or supplier base is expected to act, but no acting system has been constructively recognized;
- architecture or selected-structure claims need the holon whose structure is being selected.

**Primary EntityOfConcern.** One exact `U.Entity` candidate whose actual construction may or may not satisfy the constructive recognition criterion for one already admitted holon kind.

**Primary working reader.** A practitioner or modeler who must decide whether part-whole, acting-system, or claim-bearing-holon reasoning is admissible for the exact entity under concern before relying on neighboring work, architecture, evidence, or publication claims.

**First useful move.** Name the exact `U.Entity` under concern. Then test whether its actual construction satisfies the A.1 holon-recognition criterion under an already admitted public holon kind. `E.24.UK` admits the public kind once at ontology level; A.1 does not repeat that decision for each candidate.

**What goes wrong if missed.** A document edits itself, a theory gets ports, a list becomes an organization, a lathe becomes the super-holon of the workpiece it changes, and architecture is discussed without naming the holon whose structure is selected.

**What this buys.** FPF gets one compact part-whole foundation without turning every whole into a physical system: identity starts at `U.Entity`; part-whole treatment starts at `U.Holon`; acting work attaches to `U.System`; claim-bearing knowledge is carried by `U.Episteme`; method holonhood is governed by `U.Method`; other admitted holon kinds keep their own governing patterns.

**Not this pattern when.**

- If the current question is a selected bounded model-use relation organization, use `A.1.1`.
- If the current question is episteme identity, constitution, or neighboring-relation discipline, use `C.2.1`.
- If the current question is relation vocabulary or component, portion, aspect, and phase discipline, use `A.14`.
- If the current question is constructive part-whole grounding, use `C.13`; use `B.3.5` for Working-Model assurance grounding.
- If the current question is selected structure over a holon, use `A.22`.
- If the current question is architecture of a holon, use `C.30`.
- If the current question is transformation, method, role, work, capability, or functioning, use the direct governing pattern before relying on A.1.

### A.1:1 - Problem Frame

FPF cannot use `system` as its universal root. A pump, theory, software product, legal code, dashboard, research program, work occurrence, discipline, and team can all be objects under concern, but they do not all act, exchange matter, execute methods, or carry physical ports.

A.1 separates four questions that are often collapsed:

- **reference:** what can be individuated as `U.Entity`;
- **part-whole treatment:** which exact candidates satisfy the constructive recognition criterion for `U.Holon` or another already admitted public holon kind;
- **acting eligibility:** which recognized holons also satisfy the kind-specific criterion for the already admitted `U.System` kind;
- **claim-bearing knowledge:** which recognized holons also satisfy the kind-specific criterion for the already admitted `U.Episteme` kind.

Entity identity and world-side holon recognition have a context-independent base. Claim scope, effective reference scheme, and selected model-use structure can qualify a particular assertion or use, but none identifies the candidate, makes the constructive criterion true, or admits a public U-kind.

Other admitted holon kinds are not created by title, by filling one locally named slot, or by ordinary-language label. They remain governed by their direct patterns. Current accepted examples include `U.Method` under `A.3.1`, `U.Work` under `A.15.1`, and `U.Discipline` under `C.20`. `BoundedModelUseStructure` under `A.1.1` is `U.Structure`, not a holon kind.

### A.1:2 - Problem

Without A.1:

1. **System-bias spreads.** Physical and operational assumptions are projected onto epistemes, descriptions, theories, documents, dashboards, and source records.
2. **Epistemes become agents.** A document, model, theory, pattern, or report is said to decide, promise, authorize, perform work, or revise itself.
3. **Collections become collectives by wording.** A set of people, services, files, claims, assets, or suppliers is treated as an acting whole without boundary, coordination, role assignment, capability, method, or work evidence.
4. **Transformation becomes containment.** A system that changes another holon is treated as that holon's super-holon or as a part-whole relation by the fact of interaction.
5. **Architecture loses its grounding holon.** A structure, view, graph, diagram, or architecture claim floats free of the holon whose selected structure is under concern.
6. **Slot filling creates false kinds.** A system, episteme, holon, relation occurrence, or other value is given a new intrinsic kind merely because it fills one slot of a role-assignment, evidence, publication, description, or another direct relation.

### A.1:3 - Forces

| Force | Tension |
| --- | --- |
| Universal root vs domain comfort | Practitioners know words such as system, model, product, team, document, program, and discipline; FPF needs a cross-domain root that does not import one domain's assumptions. |
| Identity vs composition | A thing can be individuated before FPF knows whether it has parts or belongs to a larger whole. |
| Acting vs claim-bearing | Systems can enact roles, methods, plans, and work; epistemes can be changed, published, cited, compared, and relied on, but they do not act by themselves. |
| Open-world modeling vs premature completion | A holon slot can be relevant even when not yet filled; omission means "not current or not recovered", not absence in the world. |
| Collection usefulness vs collective agency | Collections can have whole-level characteristics without being acting systems. |
| Architecture usefulness vs math-lens drift | Graphs, algebras, matrices, and embeddings can describe structures; they do not become the structure or holon by spelling. |

### A.1:4 - Solution

Use A.1 to distinguish an exact referenceable entity from a candidate that satisfies the constructive holon criterion under an already admitted public holon kind.

```text
U.Entity
  U.Holon
    U.System
    U.Episteme
    U.Method           only under A.3.1 and direct method-composition patterns
    U.Work             only under A.15.1
    U.Discipline       only under C.20
    named C.3 U.Kind   only when a direct governing pattern admits holon treatment
```

This is not a classical taxonomic ladder and not a publication hierarchy. `E.24.UK` owns public U-kind admission; A.1 owns recognition of exact candidates under the admitted holon kinds and the kind-specific patterns shown above. A selected `U.Structure`, including `BoundedModelUseStructure`, remains dependent relation organization rather than a holon kind.

#### A.1:4.1 - U.Entity

`U.Entity` is anything that can be individuated and referenced. It carries no part-whole, acting, claim-bearing, model-use, or architecture assumption by itself.

Use `U.Entity` when the current move only needs to point to something: a number, claim, named product, material batch, data value, legal clause, role value, reference, document, or another object under concern.

Do not apply holon aggregation, part-whole grounding, acting-system roles, or architecture claims to a bare `U.Entity` unless its actual construction satisfies the A.1 criterion for `U.Holon` or a kind-specific criterion for another already admitted public holon kind.

#### A.1:4.2 - U.Holon And Context-Independent Recognition

`U.Holon` is the broad part-whole EntityOfConcern: an exact `U.Entity` whose actual construction supports treatment as a whole with parts and as a possible part of a larger whole.

Keep ontology admission and candidate recognition separate. `E.24.UK` owns the one-time FPF decision that admits `U.Holon` and every other public holon kind. A.1 owns the constructive criterion by which an exact candidate is recognized under an already admitted kind. Candidate classification is a judgment about that exact entity; it is not a direct relation to a pattern edition, criterion episteme, evaluator, evidence set, or status value.

For one exact candidate, recover six distinct constructive components. Do not let one component stand in for another:

1. **Exact candidate.** Identify one exact `U.Entity` under its direct identity rule.
2. **Exact constituents.** Identify the entities claimed to constitute this candidate. Nearby entities, members of a set, sampled points, and arbitrary slices are not constituents by inclusion or wording.
3. **Constructive part relations and assembly.** Recover the exact obtaining part-relation occurrences under their direct patterns and the assembly by which those constituents compose this candidate. A list, diagram, or shared boundary does not establish those relations.
4. **Reidentification rule.** State the rule that distinguishes this whole and says which constituent, relation, boundary, or phase changes preserve or end its identity.
5. **Composition-grounded whole-level characteristic.** Recover at least one exact characteristic whose value or state is produced or sustained by the composition and is not attributable to one constituent alone.
6. **Possible participation in a larger constructive assembly.** Recover the candidate's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions. Those facts must satisfy the applicability and compatibility conditions of at least one governed larger-assembly construction method or rule under which an admissible construction would include this candidate as a constituent while preserving its identity. One exact episteme may describe that method or state that rule and its conditions; the episteme does not create applicability, compatibility, or possibility.

Name the already admitted holon kind and its direct kind-specific pattern separately from those six components. The candidate satisfies the A.1 criterion when all six world-side components hold and any kind-specific condition is satisfied; it fails when a required component or condition does not hold. Satisfaction or failure does not vary with current evidence availability or evaluator access. Replacing a constituent or part-relation occurrence preserves the same holon only when the reidentification rule admits that change. An unassembled collection fails even when a project card calls it a holon.

Exact dated classification work belongs to `A.15.1`. When a reusable typed recognition-evaluation operation is current, `A.6.1` governs its declared arguments and result plus the actual application bindings. The evaluation returns `true` when its governed inputs determine satisfaction, `false` when they determine failure, and `unknown` when missing evidence or an unavailable dependency prevents either determination. `unknown` is an evaluation result, not a third candidate state: the same candidate can satisfy or fail the criterion while the current evaluation remains unable to determine which.

When another use must inspect or cite the judgment, identify an optional C.2.1 classification-assertion or evaluation-result episteme whose exact EntityOfConcern is the candidate. Its claim content names the admitted kind, the A.1 criterion, the constituent and part-relation facts, reidentification rule, whole-level characteristic, candidate-side compatibility facts, exact construction-method-or-rule episteme, evaluation frame, and `true | false | unknown` judgment needed by that use. The assertion creates none of the candidate, constituents, part relations, assembly, characteristic, compatibility facts, method or rule, larger-assembly possibility, or holonhood.

Exact evidence and assurance relations support or warrant assertion claim content. `G.11` separately governs whether the selected assertion edition is current. Receiving work separately decides whether to rely, decline to rely, defer, or reopen. `B.2` owns the different question whether the existing whole is no longer the right EntityOfConcern for a receiving use. A.1 satisfaction, failure, or evaluation uncertainty supplies neither warrant for a B.2 claim nor grounds for selecting B.2.

In ordinary use, stop after naming the candidate, six constructive components, admitted kind, kind-specific condition, and resulting judgment needed by the current work. Materialize a classification assertion only when a named receiving use depends on that episteme.

#### A.1:4.3 - Admitted Holon Kinds

Current accepted holon-kind examples are:

- `U.System`, governed here as the acting physical or operational holon kind;
- `U.Episteme`, governed here only as a non-agentive claim-bearing holon, with full slot discipline in `C.2.1`;
- `U.Work`, governed by `A.15.1` as the admitted kind for dated 4D occurrence holons;
- `U.Discipline`, governed by `C.20` as a field-level practice-and-knowledge holon;
- `U.Method`, governed by `A.3.1` and method-composition patterns such as `B.1.5` as a non-agentive method holon whose submethods compose into a whole method across levels.

No blank "other kind" escape hatch is selected. A project-local holon classification names its concrete C.3 `U.Kind`, the A.1 criterion, any kind-specific criterion, and the direct patterns for the construction facts it uses. A proposed public `U.*` holon kind first passes `E.24.UK` and gains one direct governing pattern. Neither route may rely on part-whole, architecture, role, work, evidence, or source-use claims before the candidate-side criterion is recoverable.

Candidate recognition is decided by the six candidate-side constructive components in A.1:4.2, not by agentivity, wording, evidence availability, or a B.2 whole-reidentification result. Grounding work selects the participating objects from the surrounding practice or world, fixes their boundaries, identifies constituents and exact part relations, recovers the assembly and reidentification rule, and tests the resulting whole-level characteristic and larger-assembly compatibility. Relations may arrange, constrain, assign, qualify, or describe constituents; those relations do not become constituents by that fact.

`U.Role` and `U.Method` are therefore not decided by whether they act. `U.Episteme` already shows that a non-agentive object can be a holon. The ontology decision is: `U.Method` is a non-agentive holon kind, and `U.Role` is not a holon kind. A method can have submethods composing into whole methods with whole-level preconditions, effects, invariants, interfaces, constraints, and assurance hooks; the resulting method can participate in a larger method. A step label or step description is not a method part by label: it is first recovered as a `U.Method` submethod rather than a method-description node, order relation, work-plan item, or work occurrence. A role value states what a holder is being under one assignment relation and role-taxonomy interpretation; assignment, state, capability, responsibility, permission, commitment, obligation, method participation, and role relation structure remain neighboring objects or relations rather than role parts.

#### A.1:4.4 - U.System

`U.System` is an acting physical or operational holon kind. It can participate in work-facing role assignments, capability relations, method enactment, mechanism realization, work occurrences, transformations, functioning relations, and responsibility-bearing claims when their direct patterns make those claims current.

Its kind-specific condition is acting eligibility: the recognized whole has an actual physical or operational organization through which it can causally participate in work or transformation while preserving its identity. Capability evidence or actual participation can support a classification assertion; a role assignment, work occurrence, or capability relation does not create the system by participation alone.

Keep those relations separate:

- `A.2.1` governs the role-assignment occurrence whose `HolderSystemSlot` is filled by the system.
- `A.2.2` governs capability claims about that system.
- `A.3.1`, `A.3.2`, and the mechanism family govern method, method description, and mechanism realization.
- `A.15.1` governs performed work and the exact relation through which the system is attributed as performer.
- `A.3.4` governs the bounded transformation; the exact direct subject-relation pattern governs the system's participation in it.
- Functioning, evidence, assurance, temporal, and dynamics claims remain with their direct patterns.

A.1 introduces no omnibus participation relation over references to all those occurrences. Listing them together in a worked case creates no additional world-side relation. If the selected organization among several direct relations changes an engineering decision, select that organization as `U.Structure` under A.22 and keep every constituent occurrence under its direct identity. Claim scope, effective reference scheme, and optional model-use structure qualify each dependent assertion only where its direct pattern makes them current.

#### A.1:4.5 - U.Episteme

`U.Episteme` is a claim-bearing, non-agentive holon kind. It can be changed, used, cited, published, represented, versioned, structured, compared, interpreted, or relied on by acting systems, but it does not act by itself.

Use `C.2.1` for episteme identity, `EpistemeConstitutionRelation`, and the direct empirical-grounding and edition relations declared there. Use the neighboring direct patterns for viewpoint, view, claim scope, bounded model use, evidence, publication, source use, carrier, and representation. A.1 only says that an episteme can be treated as a holon when part-whole treatment of the claim-bearing object is current.

A system in role decides, approves, performs work, promises, revises, authorizes, or bears responsibility with or about an episteme. The episteme does not perform those acts by itself.

#### A.1:4.6 - Recover Holon Delimitation And Boundary Crossing

When a claim concerns where a holon is delimited, recover the exact delimitation relation, criterion, or selected structure supplied by the direct holon, mereology, architecture, or domain pattern. Do not force an identity rule, membership relation, environment relation, selected structure, and boundary condition into one universal relation signature. Those objects have different kinds and predicates.

When one direct relation crosses that delimitation, keep the direct relation occurrence under its own pattern and use F.9 for the exact crossing or bridge claim. State the delimited holon, the direct crossing relation, direction, fit, loss, scope, and qualification window that are current for that use. A crossing classification does not replace the signal, control, measurement, transformation, source-use, publication-use, evidence-use, coupling, or other direct relation occurrence.

Do not call every boundary an interface. Use interface language only when a governing signature, module, architecture, port, or interface pattern makes interface meaning current.

External holon vocabularies do not admit FPF kinds or establish candidate holonhood by label. Recover the current FPF claim first. Acting-agent and organization claims test the `U.System` criterion; data, document, and projected-content claims usually use `U.Episteme`, publication, source-use, evidence, or description patterns; process-holon wording uses work, method, work-plan, or transformation patterns; portal or traversal wording uses an access, crossing, policy, or evidence relation. A.1 recognizes only the exact candidate-side holon or system claim when its criterion is satisfied.

A Markov blanket is not a holon boundary by name. First recover whether the source names accepted local Markov dynamics, a mathematical or probabilistic lens, an exact holon-delimitation claim, a physical interface module or component, a functional element, a boundary description, or an agency-threshold claim. Apply the direct governing pattern. A.1 recognizes the exact holon candidate only when its constructive criterion is satisfied; it does not turn the neighboring delimitation claim into holonhood.

#### A.1:4.7 - Collections, Collection-As-Whole, And Acting Collectives

A list, set, batch, fleet, pool, clientele, community, supplier base, or coverage zone does not become a `U.System` by wording.

First recover the current claim: membership under A.14; collection-as-whole constructive grounding under C.13 and B.3.5 when assurance is current; whole-level characteristic under C.16; acting collective recognition under the `U.System` criterion plus A.15.1 work; or whole reidentification under B.2.

An acting collective `U.System` has a boundary, coordination, role assignments, capability or method evidence, and work-facing participation. If those are not current, keep the object as a collection or collection-as-whole claim under direct governing patterns.

#### A.1:4.8 - Constructional Grounding

A.1 governs constructive holon recognition. It does not replace part-whole grounding or E.24.UK public-kind admission.

Use A.14 for relation vocabulary such as component, portion, aspect, phase, member, and part-whole relation; C.13 for constructive grounding such as `Gamma_m.sum`, `Gamma_m.set`, or slice treatment; and B.3.5 for Working-Model assurance grounding when the part-whole claim supports assurance or evidence.

FPF avoids unrestricted composition. A set of nearby objects, graph, diagram, role bundle, method algebra, or source table does not become a holon merely because it can be described as a whole.

#### A.1:4.9 - Slot Filling Does Not Create A Kind

A system that fills `HolderSystemSlot` of a role-assignment occurrence remains a system. An episteme that participates as the EntityOfConcern in an `EpistemeConstitutionRelation` remains an episteme. A system can participate in a transformation through an exact governed direct relation without becoming the changed holon's super-holon. A holon that participates as the EntityOfConcern of a structure-description episteme remains that holon rather than becoming the description.

The SlotSpec belongs to the direct relation declaration. Its SlotKind names the local participant slot; its ValueKind constrains admissible fillers. Filling that slot establishes neither a new intrinsic kind for the filler nor a new relation occurrence unless the direct obtaining predicate and identity rule are also satisfied. Use the direct governing pattern before introducing any durable kind name.

### A.1:5 - Archetypal Grounding (Worked Cases)

#### A.1:5.1 - Pump As Acting System

Pump #37 is first an exact `U.Entity`. Its actual construction satisfies the A.1 criterion for the already admitted `U.System` kind:

- the casing, impeller, seal, motor, and flanges are exact constituent entities;
- exact fastening, enclosure, shaft-coupling, sealing, and connection occurrences constructively assemble those constituents as Pump #37 under their direct part-relation patterns;
- the installed-assembly reidentification rule distinguishes Pump #37 and permits specified maintenance replacements;
- pump-level flow, pressure, and operating characteristics arise from the composition rather than from one constituent;
- its actual boundary, inlet and outlet interfaces, load envelope, and identity-preservation conditions satisfy the applicability and compatibility conditions of the governed plant-installation method by which the pump can remain one constituent of a larger cooling-water system;
- `E.24.UK` already admits `U.System`, while A.1 supplies the common holon criterion and its `U.System` clause supplies acting eligibility.

Those world-side facts make the criterion true whether or not the current project has enough evidence to determine it. Classification work with adequate inputs can return `true` and support a separate C.2.1 assertion. If evidence or one dependency is unavailable, evaluation returns `unknown`; Pump #37 and its criterion satisfaction do not change. Replacing the seal preserves Pump #37 only when the reidentification rule admits that maintenance phase.

If instead an exact coupling, load-envelope, or boundary-interface fact violates a condition of the governed plant-installation method, the candidate fails the criterion even when the drawing and rule-description episteme are current. Governed evaluation returns `false` when that incompatibility is available to it and `unknown` when the needed input is unavailable; neither result changes the world-side failure. Renaming or republishing the cited criterion pattern changes its episteme designation, edition, or currentness, not Pump #37 or the candidate-side facts.

Separate direct relations then state that Pump #37 fills the holder-system slot of its cooling-water circulation role assignment, has a flow-rate capability envelope, is attributed as performer of inspection work WO-1842, and participates in the water-moving transformation. No omnibus participation or candidate-classification relation is added. The pump can have selected structures; its maintenance model may participate in a separately selected `BoundedModelUseStructure`, but that structure neither identifies the pump nor makes it a holon.

#### A.1:5.2 - Scientific Theory As Episteme Holon

Newtonian gravitation in one exact selected edition is first a C.2.1 `U.Episteme` candidate. Its actual claim-bearing constitution can satisfy the A.1 criterion for the already admitted `U.Episteme` kind:

- exact law, definition, derivation, diagram, exercise, and evidence-relation epistemes are the candidate constituents;
- exact claim-composition and episteme part relations organize those constituents as one governed claim-bearing whole;
- the selected-edition reidentification rule distinguishes the theory episteme and states which revisions preserve or end that identity;
- inferential and explanatory characteristics arise from the organized claim-bearing whole rather than from one constituent;
- its actual inferential interfaces, effective reference scheme, applicability conditions, and identity-preservation conditions satisfy the applicability and compatibility conditions of at least one governed method for composing it as a constituent of a larger explanatory or educational episteme;
- `E.24.UK` already admits `U.Episteme`, while C.2.1 supplies the kind-specific constitution condition.

A textbook publication can make this edition available, but the publication form and the episteme that describes the composition method do not create the theory's compatibility or holonhood. Classification work may evaluate the criterion and a separate C.2.1 assertion may state the result; evidence, warrant, edition currentness, receiving reliance, and any B.2 whole-reidentification question remain separately governed.

The theory does not teach itself, revise itself, or authorize laboratory work. A system under an exact role assignment may explain, revise, publish, compare, or use the episteme through separately governed work and relation occurrences.

#### A.1:5.3 - Fleet As Collection Or Acting Collective

A fleet list is a membership claim. Fleet availability is a whole-level characteristic. A fleet-coordination organization that coordinates vehicles, drivers, rules, and work can be an acting collective `U.System` only after boundary, coordination, role assignments, capability or method evidence, and work-facing participation are recovered.

If a source says "the fleet responded", recover the actual claim: individual vehicle work, fleet-coordination system work, collection-as-whole characteristic, or B.2 whole reidentification.

#### A.1:5.4 - Lathe Changing A Workpiece

A lathe can change a workpiece during manufacturing without becoming the workpiece's super-holon.

Use `A.3.4` to identify the bounded transformation from the exact changed referent, extent, boundary conditions, actual change facts, and continuity rule. Use the direct subject patterns for the lathe's participation, method, dated work, work-to-change facts, and evidence. Use A.14 or C.13 for part-whole only when parthood is independently admitted.

### A.1:6 - Bias-Annotation

Lenses tested: **Onto**, **Arch**, **Epist**, **Prag**, **Gov**, **Did**.

This pattern intentionally resists:

- **system-bias:** treating all objects as acting physical systems;
- **episteme-agent bias:** assigning work, authority, or decision to claim-bearing epistemes;
- **collection-bias:** treating any collection as an acting collective;
- **boundary-bias:** treating boundary words, diagrams, folders, or sections as holon delimitation by appearance;
- **interaction-bias:** using one word for transformation, signal, source use, publication use, evidence relation, probe relation, and control relation;
- **math-lens drift:** treating graph, algebra, matrix, tuple, or embedding expressions as the ontology-side structure by spelling;
- **publication-form bias:** treating a document, dashboard, model, register, or digital twin as the holon it describes.

### A.1:7 - Conformance Checklist

| Check | Conformance condition |
| --- | --- |
| `CC-A1-1` | The exact candidate is first individuated as `U.Entity`; `E.24.UK` already admits the public holon kind before A.1 tests candidate recognition under that kind. |
| `CC-A1-2` | A current recognition use separately recovers the exact candidate, exact constituents, constructive part-relation occurrences and assembly, reidentification rule, composition-grounded whole-level characteristic, and candidate-side compatibility with an applicable governed larger-assembly construction method or rule; it then names the already admitted holon kind and its direct kind-specific condition. |
| `CC-A1-3` | A proposed new public holon kind first passes `E.24.UK`; its direct pattern then states the kind-specific membership condition without changing the common A.1 criterion for exact candidates. |
| `CC-A1-4` | Candidate classification is not reified as a status relation. World-side satisfaction or failure, classification work, `true | false | unknown` evaluation, optional C.2.1 assertion identity, evidence or warrant, G.11 edition currentness, receiving-work disposition, and B.2 whole reidentification remain separately governed; no A.1 result warrants a B.2 claim or selects B.2. |
| `CC-A1-5` | Role assignment, capability, method, work, transformation, functioning, evidence, and temporal claims remain separate direct relations; their reference bundle is not asserted as another occurrence. |
| `CC-A1-6` | `U.Episteme` is non-agentive; systems may transform, publish, cite, or use epistemes, but the episteme does not act by itself. |
| `CC-A1-7` | Collection membership, collection-as-whole, acting collective system, whole-level characteristic, and B.2 whole reidentification are kept distinct. |
| `CC-A1-8` | Boundary wording recovers an exact delimitation relation, criterion, or selected structure from its direct pattern; crossing wording preserves the exact crossing relation occurrence and uses F.9 without minting universal delimitation or crossing relation kinds. |
| `CC-A1-9` | A system changing another holon is not treated as that holon's super-holon unless a separate grounded part-whole relation obtains. |
| `CC-A1-10` | A.14, C.13, and B.3.5 remain the direct governing patterns for relation vocabulary, constructive grounding, and Working-Model assurance grounding. |
| `CC-A1-11` | Publication forms and descriptions of holons are kept distinct from the holons they describe. |

### A.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| System as universal root | A theory, document, model, source, or dashboard receives physical system properties. | Re-type as `U.Episteme`, publication, source-use object, or another direct object before using system claims. |
| Document edited itself | A model, theory, or document is said to perform a revision. | Name the `U.System` in role that performed the work and the `U.Episteme` or publication that changed. |
| Collection as actor | A list, batch, pool, fleet, or community is said to decide or perform work. | Recover membership, collection-as-whole, whole-level characteristic, acting collective system, or B.2 whole reidentification. |
| Interaction as one umbrella | Signal, source use, publication use, transformation, measurement, and control are all called interaction. | Recover the exact direct relation; use F.9 for a current crossing claim and `A.3.4` when bounded change is current. |
| Omnibus participation relation | References to role, capability, method, work, transformation, evidence, and time are packed into one additional relation-shaped record. | Keep the direct relation occurrences separate; select their organization as `U.Structure` only when that organization changes the receiving use. |
| Boundary by drawing | A box, folder, section, dashboard view, or diagram is treated as the holon boundary. | Recover the exact delimitation relation, criterion, or selected structure from its direct pattern; keep the drawing as a description or view. |
| Architecture without holon | A selected structure is discussed without the holon whose structure is selected. | Use A.1 to name the holon, then `A.22` and `C.30` for selected structure and architecture. |

### A.1:9 - Consequences

Positive consequences:

- FPF can talk about physical systems, organizations, documents, theories, models, work occurrences, disciplines, research programs, and selected structures without making them all systems or holons.
- Acting work stays attached to systems in roles.
- Epistemes can be changed, described, compared, published, and relied on without becoming agents.
- Architecture and selected-structure claims gain a grounding holon.
- Collection-as-whole and acting collective claims become inspectable instead of lexical.

Costs:

- Practitioners pay the cost of replacing umbrella uses of "system", "boundary", "interaction", "level", "emergence", and "collection" with exact governed claims.
- A reviewable holon-recognition claim states the exact constituents, construction, reidentification, larger-assembly compatibility, whole-level characteristic, admitted kind, and direct governing pattern on which it relies.
- Some familiar sentences need repair: "the document decided" becomes a claim about a system in role, a decision relation, and an episteme or publication.

### A.1:10 - Rationale

A.1 prevents category errors by separating individuation, constructive part-whole recognition, acting eligibility, and claim-bearing. `U.Entity` gives the minimal referenceable object. `U.Holon` adds six separately recoverable constructive components: exact candidate, exact constituents, exact part relations and assembly, reidentification, a composition-grounded whole-level characteristic, and compatible possible participation in a governed larger assembly. `U.System` adds acting eligibility. `U.Episteme` adds claim-bearing structure without agentivity. `U.Work` and `U.Discipline` are holon-kind examples only through their governing patterns; `BoundedModelUseStructure` is selected `U.Structure`, not another holon kind.

The recognition base cannot depend on a prior context object without recursion. It begins with the exact candidate and world-side construction facts. Public-kind admission is the separate one-time `E.24.UK` decision. Classification work may evaluate the criterion, but its `true | false | unknown` result, a C.2.1 assertion, evidence, currentness, and receiving disposition neither participate in a candidate-side relation nor alter the candidate's identity.

This also prevents ontology duplication. A theory under concern, a theory description, a publication of that description, and the system that edits the publication can all be named without turning the filling of one participant slot into a new kind. Architecture likewise starts from the exact holon recognized under an admitted kind whose selected structures matter; diagrams and structure descriptions remain epistemes.

The constructional stance is conservative: FPF avoids unrestricted composition and uses A.14, C.13, and B.3.5 before a part-whole claim is relied on for another claim or work occurrence. This keeps holonic thinking useful without letting every collection, expression, graph, selected structure, or source label become a holon.

### A.1:11 - SoTA-Echoing

A.1 draws on current constructional-ontology, applied-foundational-ontology, and physics-side construction traditions for different questions. None of these sources admits an FPF kind, establishes a candidate's construction, or replaces the direct patterns that govern part relations, work, evidence, or publication.

| Current source and practice answer | Exact use in A.1 | Adoption status and blocked overread |
| --- | --- | --- |
| Florio and Linnebo, [*Introduction to Constructional Ontology*](https://philarchive.org/rec/FLOITC-3), 2024, distinguish constructors, constructor inputs, constructional processes, and the identity consequences of construction choices. | A.1 requires exact constituents, obtaining constructive part relations, assembly, reidentification, and a composition-grounded whole-level characteristic before recognizing a candidate whole. | **Adapt.** A.1 adopts construction-sensitive identity but keeps public-kind admission with `E.24.UK` and direct subject facts with their own patterns; a construction description or selected constructor does not make the candidate a holon. |
| Borgo and Righetti, [“Towards Applied Constructional Ontology”](https://journals.sagepub.com/doi/10.3233/FAIA250480), FOIS 2025, show that applying constructional ontology still requires explicit choices about mereology, dependence, and identity. | A.1 sends exact part-relation vocabulary and constructive grounding to A.14 and C.13, preserves a separate reidentification rule, and uses B.3.5 only when assurance grounding is current. | **Adopt.** The demand for explicit applied choices is adopted; A.1 rejects the shortcut that a constructional-ontology label already settles constituents, parthood, whole identity, or warrant. |
| Deutsch, [*Constructor Theory*](https://arxiv.org/abs/1210.7439), 2012, and Deutsch and Marletto, [“Constructor theory of time”](https://arxiv.org/abs/2505.08692), 2025, treat possible transformations through substrate attributes and constructor conditions rather than through a written task alone. | A.1's larger-assembly component requires the candidate's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions to satisfy the applicability and compatibility conditions of a governed construction method or rule. | **Adapt.** The modal discipline is adopted for candidate recognition; a task, rule episteme, drawing, or evidence item does not create applicability, compatibility, possibility, work, or assembly. |
| Partridge, [*BORO Ontology*](https://borosolutions.net/boro-ontology), C-FORS 2025, supplies a current 4D extensional and unrestricted-composition comparator. | A.1 makes identity through change and actual construction explicit, while using A.14 and C.13 before relying on a part-whole claim. | **Reject wholesale; retain the identity test.** A.1 rejects unrestricted composition and import of BORO's category system, while retaining pressure to state the exact candidate, extent-sensitive reidentification, and construction facts. |

For the Pump #37 and scientific-theory cases in A.1:5, the practical consequence is the same: recover the candidate and its subject-side construction first; use a governed method or rule only to test larger-assembly compatibility; keep evaluation, evidence, assertion, description, and publication as separately governed neighboring objects.

Treat a stronger source as current only when it changes the root split among `U.Entity`, `U.Holon`, `U.System`, admitted holon kinds, delimitation, boundary crossing, or publication-form separation. A new tool, notation, or diagram style is not enough unless it changes that ontology-side claim.

### A.1:12 - Relations

- **Builds on:** `E.24.UK` for one-time public U-kind admission, `A.14` and `C.13` for exact part relations and constructive assembly, and `B.3.5` when Working-Model assurance grounding is current.
- **Coordinates with:** `A.15.1` for dated classification work; `A.6.1` for a current typed evaluation operation and actual bindings; `C.2.1` for classification-assertion or evaluation-result episteme identity; `A.10` and `B.3` for evidence and warrant; `G.11` for assertion-edition currentness; `B.2` for the separate whole-reidentification question; `A.1.1` for bounded model-use structure; `A.22` for selected structure; `C.30` for architecture; `A.3.4` for transformation; `C.20` for discipline; and `E.10.ARCH` for wording-use restoration.
- **Used by:** patterns that need an exact recognized holon, an already admitted holon kind, an acting system, a non-agentive episteme, a grounded part-whole claim, a collection-versus-collective distinction, a delimitation relation, or a boundary-crossing relation.

### A.1:End

