## A.1 - Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)

> **Type:** Part A architectural ontology pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.1:0 - Use This When

Use this pattern when a project must say what kind of thing is under concern before it can rely on parts, wholes, boundaries, acting systems, roles, methods, work, architecture, or descriptions.

Typical moments:

- a team calls everything a "system" and then asks physical or operational questions about theories, documents, models, dashboards, or descriptions;
- an episteme is treated as an acting agent that decides, performs work, authorizes, promises, or revises itself;
- a product, organization, machine, document family, research program, bounded context, discipline, work occurrence, or model family must be treated as a whole with parts;
- a list, batch, fleet, pool, clientele, community, or supplier base is expected to act, but no acting system has been admitted;
- architecture or selected-structure claims need the holon whose structure is being selected.

**First useful move.** Name the `U.Entity` under concern. Then decide whether the current claim also admits it as `U.Holon`, and whether a direct governing pattern admits a more specific holon kind such as `U.System`, `U.Episteme`, `U.Work`, `U.BoundedContext`, or `U.Discipline`.

**What goes wrong if missed.** A document edits itself, a theory gets ports, a list becomes an organization, a lathe becomes the super-holon of the workpiece it changes, and architecture is discussed without naming the holon whose structure is selected.

**What this buys.** FPF gets one compact part-whole foundation without turning every whole into a physical system: identity starts at `U.Entity`; part-whole treatment starts at `U.Holon`; acting work attaches to `U.System`; claim-bearing knowledge is carried by `U.Episteme`; other admitted holon kinds keep their own governing patterns.

**Not this pattern when.**

- If the current question is local vocabulary, local invariant, role taxonomy, or meaning inside one semantic frame, use `A.1.1`.
- If the current question is episteme slot discipline, use `C.2.1`.
- If the current question is relation vocabulary or component, portion, aspect, and phase discipline, use `A.14`.
- If the current question is constructive part-whole grounding, use `C.13`; use `B.3.5` for Working-Model assurance grounding.
- If the current question is selected structure over a holon, use `A.22`.
- If the current question is architecture of a holon in context, use `C.30`.
- If the current question is transformation, method, role, work, capability, or functioning, use the direct governing pattern before relying on A.1.

### A.1:1 - Problem Frame

FPF cannot use `system` as its universal root. A pump, theory, software product, legal code, dashboard, research program, work occurrence, bounded context, discipline, and team can all be objects under concern, but they do not all act, exchange matter, execute methods, or carry physical ports.

A.1 separates four questions that are often collapsed:

- **reference:** what can be individuated as `U.Entity`;
- **part-whole treatment:** what can be considered as `U.Holon` in a bounded context;
- **acting eligibility:** what can be admitted as `U.System`;
- **claim-bearing knowledge:** what can be admitted as `U.Episteme`.

Other admitted holon kinds are not created by title, slot position, or ordinary-language label. They remain governed by their direct patterns. Current accepted examples include `U.Work` under `A.15.1`, `U.BoundedContext` under `A.1.1`, and `U.Discipline` under `C.20`.

### A.1:2 - Problem

Without A.1:

1. **System-bias spreads.** Physical and operational assumptions are projected onto epistemes, descriptions, theories, documents, dashboards, and source records.
2. **Epistemes become agents.** A document, model, theory, pattern, or report is said to decide, promise, authorize, perform work, or revise itself.
3. **Collections become collectives by wording.** A set of people, services, files, claims, assets, or suppliers is treated as an acting whole without boundary, coordination, role assignment, capability, method, or work evidence.
4. **Transformation becomes containment.** A system that changes another holon is treated as that holon's super-holon or as a part-whole relation by the fact of interaction.
5. **Architecture loses its grounding holon.** A structure, view, graph, diagram, or architecture claim floats free of the holon whose selected structure is under concern.
6. **Slot position creates false kinds.** A value in a role, source, transformed-object, evidence, publication, or described-holon slot is treated as a new ontology by local name.

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

Use A.1 to decide whether the current object is only a referenceable entity, a holon, or a directly admitted holon kind.

```text
U.Entity
  U.Holon
    U.System
    U.Episteme
    U.Work             only under A.15.1
    U.BoundedContext   only under A.1.1
    U.Discipline       only under C.20
    named C.3 U.Kind   only when a direct governing pattern admits holon treatment
```

This is not a classical taxonomic ladder and not a publication hierarchy. It is a governed admission discipline for part-whole treatment in FPF.

#### A.1:4.1 - U.Entity

`U.Entity` is anything that can be individuated and referenced under a bounded context. It carries no part-whole, acting, claim-bearing, or architecture assumption by itself.

Use `U.Entity` when the current move only needs to point to something: a number, claim, named product, material batch, data value, legal clause, role value, source reference, document, or object under concern.

Do not apply holon aggregation, part-whole grounding, acting-system roles, or architecture claims to a bare `U.Entity` unless a current pattern also admits the entity as `U.Holon` or as a directly governed holon kind.

#### A.1:4.2 - U.Holon

`U.Holon` is the broad part-whole EntityOfConcern: a `U.Entity` considered as a whole with parts and as a possible part of larger wholes in a bounded context.

A holon claim is admissible only when the current text names the bounded context, the identity or recognition rule, the current part relation, and the governing pattern that admits the object under that part-whole treatment.

The A.1 holon slot relation is:

```text
HolonSlotRelation@Context:
  holonRef: U.Holon
  boundedContextRef: U.BoundedContext
  identityOrRecognitionRule:
  partRelationRefs:
  selectedStructureRefs?
  holonDelimitationRelationRefs?
  holonBoundaryCrossingRelationRefs?
  containingWholeRefs?
  admittedHolonKindRef?: U.System | U.Episteme | U.Work | U.BoundedContext | U.Discipline | named C.3 U.Kind admitted by a direct governing pattern
```

This relation is a selected SlotRelation expression, not a new U-kind and not a record that acts. Under open-world discipline, an omitted slot means "not current or not recovered for this claim", not "absent in the world".

#### A.1:4.3 - Admitted Holon Kinds

Current accepted holon-kind examples are:

- `U.System`, governed here as the acting physical or operational holon kind;
- `U.Episteme`, governed here only as a non-agentive claim-bearing holon, with full slot discipline in `C.2.1`;
- `U.Work`, governed by `A.15.1` as a dated 4D occurrence holon;
- `U.BoundedContext`, governed by `A.1.1` as a semantic-frame holon;
- `U.Discipline`, governed by `C.20` as a field-level practice-and-knowledge holon.

No blank "other kind" escape hatch is selected. If a source claims another holon kind, the current FPF use must name the concrete C.3 `U.Kind`, the part-whole relation, the direct governing pattern, and the slot discipline that makes holon treatment admissible before any part-whole, architecture, role, work, evidence, or source-use claim relies on it.

#### A.1:4.4 - U.System

`U.System` is an acting physical or operational holon kind. It can bear work-facing role assignments, capabilities, methods, mechanisms, work occurrences, transformation participation, and responsibility-bearing claims when the direct neighboring patterns make those claims current.

The A.1 system participation relation is:

```text
SystemParticipationRelation@Context:
  systemRef: U.System
  boundedContextRef: U.BoundedContext
  holonDelimitationRelationRef?
  roleAssignmentRefs?
  capabilityRefs?
  methodRefs?
  methodDescriptionRefs?
  mechanismRefs?
  workPlanRefs?
  workOccurrenceRefs?
  transformationParticipationRefs?
  functioningOrFunctionalElementRefs?
  evidenceRelationRefs?
  assuranceRelationRefs?
  temporalAspectRefs?
  dynamicsAspectRefs?
```

This relation links acting-system participation across role, capability, method, mechanism, work, transformation, functioning, evidence, assurance, temporal, and dynamics concerns. It does not collapse those concerns into one kind. Role assignment remains role discipline; method remains method discipline; performed work remains work discipline; transformation remains `U.Transformation`; functioning and functional element remain their direct owners.

#### A.1:4.5 - U.Episteme

`U.Episteme` is a claim-bearing, non-agentive holon kind. It can be changed, used, cited, published, represented, versioned, structured, compared, interpreted, or relied on by acting systems, but it does not act by itself.

Use `C.2.1` and the episteme family for episteme slot relation, claim graph, viewpoint, reference scheme, evidence relation, publication relation, source-use relation, and claim-bearing structure. A.1 only says that an episteme can be treated as a holon when part-whole treatment of the claim-bearing object is current.

Do not say that an episteme decides, approves, performs work, promises, revises itself, authorizes action, or bears responsibility. A system in role may do those things with or about an episteme.

#### A.1:4.6 - Holon Delimitation And Boundary Crossing

Do not create `U.Boundary` or `U.Interaction` from boundary or interaction wording.

Use `HolonDelimitationRelation@Context` when the current claim is about where the holon is delimited in a bounded context: identity rule, membership or part relation, environment relation, selected structure, or current boundary condition.

Use `HolonBoundaryCrossingRelation@Context` when the current claim is about a relation crossing that delimitation: transformation, signal, control, measurement, source use, publication use, evidence relation, probe relation, coupling, or another direct relation. If bounded change under conditions is current, use `A.3.4` for `U.Transformation`; the boundary-crossing relation may point to it but is not the transformation itself.

Do not call every boundary an interface. Use interface language only when a governing signature, module, architecture, port, or interface pattern makes interface meaning current.

External holon vocabularies do not admit FPF kinds by label. If a source says `AgentHolon`, `OrganisationHolon`, `DataHolon`, `ProcessHolon`, `Portal`, `Projection`, or a similar semantic-web holon class, recover the FPF claim before using it. Acting-agent and organization claims require `U.System` admission; data, document, and projected-content claims usually require `U.Episteme`, publication, source, evidence, or description owners; process-holon wording requires work, method, work-plan, or transformation owners; portal or traversal wording requires an access, boundary-crossing, policy, or evidence relation. A.1 admits only the holon or system claim when that claim is current.

Do not call a Markov blanket a holon boundary, interface, interface module, physical component, statistical separator, or agency proof until the current claim is recovered. If source wording says `Markov blanket`, first decide whether it names accepted local Markov dynamics, a mathematical or probabilistic lens, a holon delimitation or boundary-crossing relation, a physical interface module or component, a functional element, a boundary description or publication, or an agency-threshold claim. Apply the direct governing pattern. A.1 admits only the holon and delimitation claim when those are current.

#### A.1:4.7 - Collections, Collection-As-Whole, And Acting Collectives

A list, set, batch, fleet, pool, clientele, community, supplier base, or coverage zone does not become a `U.System` by wording.

First recover whether the source claims:

- membership only, governed by A.14 relation vocabulary;
- collection-as-whole constructive grounding, governed by C.13 and B.3.5 where assurance grounding is current;
- whole-level characteristic, governed by C.16;
- acting collective system, governed by `U.System` admission plus A.15 and role, method, and work owners;
- whole reidentification, governed by B.2.

An acting collective `U.System` needs boundary, coordination, role assignments, capability or method evidence, and work-facing participation. If those are not current, keep the object as a collection or collection-as-whole claim under direct owners.

#### A.1:4.8 - Constructional Grounding

A.1 names holon admission. It does not replace part-whole grounding.

Use:

- A.14 for relation vocabulary such as component, portion, aspect, phase, member, and part-whole relation;
- C.13 for constructive grounding such as `Gamma_m.sum`, `Gamma_m.set`, or slice treatment when the constructional grounding question is current;
- B.3.5 for Working-Model assurance grounding when the part-whole claim is used for assurance or evidence.

FPF avoids unrestricted composition. A set of nearby objects, a graph, a diagram, a role bundle, a method algebra, or a source table does not become a holon merely because it can be described as a whole.

#### A.1:4.9 - Slot Position Does Not Create A Kind

A system in a role-assignment holder slot remains a system. An episteme in an EntityOfConcern slot remains an episteme. A holon whose structure is described does not become the description of that structure. A system changing another holon may fill transformation participation slots without becoming that holon's super-holon. A publication, dashboard, model, or digital twin may describe a holon without becoming that holon.

Use the direct governing pattern for the current slot relation before creating a durable name.

### A.1:5 - Archetypal Grounding (Worked Cases)

#### A.1:5.1 - Pump As Acting System

Pump #37 is a `U.System` holon in a plant maintenance bounded context.

```text
HolonSlotRelation@Context:
  holonRef: Pump #37
  boundedContextRef: PlantLineB.Maintenance.2026
  identityOrRecognitionRule: asset tag plus installed pump boundary
  partRelationRefs: casing, impeller, seals, motor, inlet flange, outlet flange
  holonDelimitationRelationRefs: casing plus inlet and outlet flange delimitation
  holonBoundaryCrossingRelationRefs: water flow, electrical supply, control signal
  admittedHolonKindRef: U.System

SystemParticipationRelation@Context:
  systemRef: Pump #37
  roleAssignmentRefs: cooling-water circulation role
  capabilityRefs: flow-rate envelope
  methodRefs: maintenance method selected by plant rules
  workOccurrenceRefs: performed inspection WO-1842
  transformationParticipationRefs: moving water under operating conditions
```

The pump can bear a role, participate in transformations, and have selected structures. The work order, dashboard, and maintenance procedure are epistemes or publications unless a direct pattern says otherwise.

#### A.1:5.2 - Scientific Theory As Episteme Holon

Newtonian gravitation in a selected edition is a `U.Episteme` holon in a physics-education bounded context.

```text
HolonSlotRelation@Context:
  holonRef: Newtonian gravitation, selected textbook edition
  boundedContextRef: PhysicsEducation.SelectedEdition
  identityOrRecognitionRule: selected claims, definitions, reference scheme, and examples
  partRelationRefs: laws, definitions, derivations, diagrams, exercises, evidence relations
  admittedHolonKindRef: U.Episteme
```

The theory does not teach itself, revise itself, or authorize lab work. A teacher, student, author, reviewer, or software system in role may explain, revise, publish, compare, or use the episteme.

#### A.1:5.3 - Fleet As Collection Or Acting Collective

A fleet list is a membership claim. Fleet availability is a whole-level characteristic. A fleet-coordination organization that coordinates vehicles, drivers, rules, and work can be an acting collective `U.System` only after boundary, coordination, role assignments, capability or method evidence, and work-facing participation are recovered.

If a source says "the fleet responded", A.1 does not accept the sentence by wording. Recover the actual claim: individual vehicle work, fleet-coordination system work, collection-as-whole characteristic, or B.2 whole reidentification.

#### A.1:5.4 - Lathe Changing A Workpiece

A lathe can change a workpiece during manufacturing without becoming the workpiece's super-holon.

Use `A.3.4` for the bounded transformation: transformed object, initial condition, post-state or delta, boundary conditions, acting system participation, method, work occurrence, and evidence. Use A.14 or C.13 for part-whole only when parthood is independently admitted.

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

| Check | Requirement |
| --- | --- |
| `CC-A1-1` | A modeled object is first typed as `U.Entity`, `U.Holon`, `U.System`, `U.Episteme`, or another directly admitted holon kind before part-whole, role, work, or architecture claims rely on it. |
| `CC-A1-2` | A current holon use names bounded context, identity or recognition rule, current part relation, and governing admitting pattern. |
| `CC-A1-3` | Non-listed holon-kind claims name the concrete C.3 `U.Kind`, part-whole relation, direct governing pattern, and slot discipline. |
| `CC-A1-4` | `HolonSlotRelation@Context` is treated as a SlotRelation expression, not as a U-kind or actor. |
| `CC-A1-5` | `SystemParticipationRelation@Context` links role, capability, method, work, transformation, functioning, evidence, and temporal aspects without collapsing them. |
| `CC-A1-6` | `U.Episteme` is non-agentive; systems may transform, publish, cite, or use epistemes, but the episteme does not act by itself. |
| `CC-A1-7` | Collection membership, collection-as-whole, acting collective system, whole-level characteristic, and B.2 whole reidentification are kept distinct. |
| `CC-A1-8` | Boundary wording recovers `HolonDelimitationRelation@Context` or another direct object; interaction wording recovers `HolonBoundaryCrossingRelation@Context`, `U.Transformation`, source use, publication use, evidence relation, probe relation, control relation, or another direct relation. |
| `CC-A1-9` | A system changing another holon is not treated as that holon's super-holon unless a separate part-whole relation is admitted. |
| `CC-A1-10` | A.14, C.13, and B.3.5 remain the direct owners for relation vocabulary, constructive grounding, and Working-Model assurance grounding. |
| `CC-A1-11` | Publication forms and descriptions of holons are kept distinct from the holons they describe. |

### A.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| System as universal root | A theory, document, model, source, or dashboard receives physical system properties. | Re-type as `U.Episteme`, publication, source-use object, or another direct object before using system claims. |
| Document edited itself | A model, theory, or document is said to perform a revision. | Name the `U.System` in role that performed the work and the `U.Episteme` or publication that changed. |
| Collection as actor | A list, batch, pool, fleet, or community is said to decide or perform work. | Recover membership, collection-as-whole, whole-level characteristic, acting collective system, or B.2 whole reidentification. |
| Interaction as one umbrella | Signal, source use, publication use, transformation, measurement, and control are all called interaction. | Recover the direct relation. Use `HolonBoundaryCrossingRelation@Context` only for the boundary-crossing relation and `A.3.4` when bounded change is current. |
| Boundary by drawing | A box, folder, section, dashboard view, or diagram is treated as the holon boundary. | Name the bounded context, identity or recognition rule, and `HolonDelimitationRelation@Context`. |
| Architecture without holon | A selected structure is discussed without the holon whose structure is selected. | Use A.1 to name the holon, then `A.22` and `C.30` for selected structure and architecture. |

### A.1:9 - Consequences

Positive consequences:

- FPF can talk about physical systems, organizations, documents, theories, models, work occurrences, bounded contexts, disciplines, and research programs without making them all systems.
- Acting work stays attached to systems in roles.
- Epistemes can be changed, described, compared, published, and relied on without becoming agents.
- Architecture and selected-structure claims gain a grounding holon.
- Collection-as-whole and acting collective claims become inspectable instead of lexical.

Costs:

- Authors must stop using "system", "boundary", "interaction", "level", "emergence", or "collection" as umbrella substitutes.
- A holon claim must say enough about context, identity, and part relation to be reviewable.
- Some familiar sentences need repair: "the document decided" becomes a claim about a system in role, a decision relation, and an episteme or publication.

### A.1:10 - Rationale

A.1 prevents category errors by separating individuation, part-whole treatment, acting eligibility, and claim-bearing. `U.Entity` gives the minimal referenceable object. `U.Holon` adds part-whole treatment in a bounded context. `U.System` adds acting eligibility. `U.Episteme` adds claim-bearing structure without agentivity. `U.Work`, `U.BoundedContext`, and `U.Discipline` are holon-kind examples only through their governing patterns.

This also prevents ontology duplication. A theory under concern, a theory description, a publication of that description, and the system that edits the publication can all be named without turning each slot position into a new kind. The same discipline is needed by architecture: architecture is selected structure of a holon in context, not a diagram and not a floating root kind.

The constructional stance is conservative: FPF avoids unrestricted composition and uses A.14, C.13, and B.3.5 before a part-whole claim is relied on for another claim or work occurrence. This keeps holonic thinking useful without letting every collection, expression, graph, or source label become a holon.

### A.1:11 - SoTA-Echoing

| Source family | Current lesson for A.1 | FPF decision |
| --- | --- | --- |
| Florio and Linnebo 2024 constructional ontology frame | Construction, identity, dependency, and process distinctions discipline when a whole is being constructed rather than merely named. | A.1 admits holon treatment only with bounded context, identity or recognition rule, current part relation, and direct governing pattern. |
| Core Constructional Ontology and BORO applied ontology lineage | Applied part-whole and identity work needs explicit constructional and refactoring discipline. | A.14, C.13, and B.3.5 remain direct owners for relation vocabulary, constructive grounding, and assurance grounding. |
| Contemporary holonic systems literature | Holon work is often system-facing and useful for coordination, closure, and system-wide outcomes. | `U.System` is retained as acting holon kind, but `U.Holon` is broader than system. |
| Knowledge-representation, provenance, and publication practice | Claim-bearing objects and their publication forms must be separated from acting systems. | `U.Episteme` is a non-agentive holon; systems in role create, publish, cite, compare, or use epistemes. |
| Digital-twin and systems-engineering practice | Models and descriptions need boundary-consistent grounding objects. | Architecture and structure patterns name the described holon before treating selected structure, view, or description as current. |

Treat a stronger source as current only when it changes the root split among `U.Entity`, `U.Holon`, `U.System`, admitted holon kinds, delimitation, boundary crossing, or publication-form separation. A new tool, notation, or diagram style is not enough unless it changes that ontology-side claim.

### A.1:12 - Relations

- **Builds on:** `E.24` for ontic introduction discipline, `E.24.UK` for U-kind admission discipline, and `A.6.5` for slot relation discipline.
- **Coordinates with:** `A.1.1` for bounded context, `A.14` for relation vocabulary, `C.13` for constructive grounding, `B.3.5` for Working-Model assurance grounding, `A.22` for selected structure, `C.30` for architecture, `C.2.1` for episteme slot relation, `A.15` and `A.15.1` for role-method-work and performed work, `A.3.4` for transformation, `C.20` for discipline, and `E.10.ARCH` for wording-use restoration.
- **Used by:** patterns that need a grounding holon, admitted holon kind, acting system, non-agentive episteme, part-whole relation, collection-versus-collective distinction, delimitation relation, or boundary-crossing relation.

### A.1:End

