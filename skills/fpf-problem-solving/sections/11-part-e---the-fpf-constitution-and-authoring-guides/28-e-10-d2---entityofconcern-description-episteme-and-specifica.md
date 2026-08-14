## E.10.D2 - EntityOfConcern, Description Episteme, and Specification-Use Discipline
> **Status:** Stable

*Definitional pattern - normative, notation-agnostic*

> **One-sentence summary.** Start from the exact work, decision, or other receiving use; recover the description episteme through C.2.1's exact `<ClaimGraph, EntityOfConcern, effective ReferenceScheme>` constitution; and add specification, viewpoint, view, model-use, evidence, publication, carrier, or representation machinery only when that receiving use depends on its separately governed relation.

**Status.** Definitional pattern.
**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; C.2.1 **Episteme Identity, Constitution, Grounding, and Edition**; A.2.6 **Claim Scope**; A.1.1 **Bounded Model-Use Structure**; C.29 **Mathematical Representation**.
**Coordinates with.** E.10 **Ontological Precision Restoration**; E.17.0 **Viewpoint and View Membership**; E.17 and E.24.PUB **Publication**; A.10 and B.3 **Evidence and Assurance**; G.11 **Currentness**; A.3.2 **Method Description**; F.9 **Bridge**; F.4 **System-Role-Kind Description**; F.5 **Naming Discipline**.
**Non-goals.** This pattern introduces no description kind, slot relation, context tuple, card schema, publication kind, or representation kind. It does not decide whether claims are true, current, sufficient, authoritative, or permitted. It handles each live question under the subject pattern while keeping the described object and the claim-bearing episteme recoverable.

### E.10.D2:1 - Problem frame

Use this pattern when one passage names an exact entity and also speaks of a description, specification, view, diagram, publication, file, dashboard, model, evidence item, assurance result, gate result, or decision around it. The recognizable failure is that the wording makes one of those neighboring objects stand in for the entity, the episteme, or the authority for the next action.

Begin with the receiving use:

1. What exact work, decision, comparison, inquiry, preservation, teaching, publication, or other use needs the description?
2. What is the next unresolved question or choice for that use? Do not invent one for a use that has none.
3. What exact claim content is being used?
4. What exact `U.Entity` is the `EntityOfConcern` of that claim-bearing whole?
5. Which effective `U.ReferenceScheme` supplies the designation and interpretation rules that make those claims readable about that entity?

The last three answers recover the C.2.1 `EpistemeConstitutionRelation`. If identity is all the receiving use needs, stop there. Otherwise open only the neighboring object or relation needed for the next visible sentence or action.

Not this pattern when the live question is already an exact evidence path, assurance claim, work occurrence, gate decision, commitment, Bridge, publication occurrence, representation correspondence, or state fact. Use its direct governor. Return here only if the wording also obscures which entity is being described or which episteme carries the claims.

The working distinctions are:

* the **EntityOfConcern** is the independently identified entity about which the selected claim-bearing whole makes its claims;
* a **description episteme** is an ordinary `U.Episteme` used to carry descriptive claims about that EntityOfConcern;
* a **describing use** names the receiving use and may select one exact viewpoint when that selection changes what is read or checked; selection changes neither episteme identity nor conformance;
* **specification use** is a checkable use of a description episteme, not a third peer ontology class;
* viewpoint, view, claim scope, model-use structure, grounding, evidence, edition, publication, carrier, and representation remain neighboring objects and relations.

This buys a small practical result: the reader can say what is described, which claim-bearing episteme is being used, what the receiving use needs next, and where any additional claim is governed. A formal-looking file, card, suffix, approval, or diagram gains no ontological or practical authority by appearance.

### E.10.D2:2 - Problem

1. **Entity-description collapse.** The EntityOfConcern is identified with the episteme, diagram, card, file, dashboard, or work record that says something about it.
2. **Record-shaped constitution.** A local tuple, filled card, context record, or field list is treated as what makes the episteme exist.
3. **Specification inflation.** Detailed or official-looking prose is called a `...Spec` although no checkable claims and no exact harness or validation relation are present.
4. **Neighbor collapse.** Viewpoint, view, claim scope, model-use structure, grounding, evidence, edition, publication, carrier, and representation become fields of one omnibus description object.
5. **Use-free qualification.** Context, scope, structure, currentness, or publication machinery is required without naming the receiving use that needs it.
6. **Agency and authority leakage.** A description, standard, card, approval label, or publication is said to perform work, authorize action, or establish a world-side fact without its direct relation.

### E.10.D2:3 - Forces

| Force | Pressure |
|---|---|
| **Short practitioner move vs recoverable ontology** | Readers need a concise first move, while a load-bearing claim must still recover the exact C.2.1 constitution and any live neighboring relation. |
| **Stable episteme identity vs changing uses** | One episteme can be viewed, checked, published, represented, or used differently without acquiring another identity. |
| **Checkability vs official appearance** | A document can be detailed, approved, or schema-backed without satisfying specification-use conditions. |
| **Useful qualification vs mandatory context record** | A receiving use may need viewpoint, scope, model-use, or publication qualification; imposing all of them on every description recreates an omnibus record. |
| **Recursive description vs a meta-ontology** | An episteme can itself be described, but that case should use ordinary C.2.1 recursion rather than another description layer. |

### E.10.D2:4 - Solution

For the current passage or artifact:

1. **Name the receiving use.** State the exact work, decision, inquiry, comparison, preservation, teaching, publication, or other use and what it needs next.
2. **Recover the episteme constitution.** Identify the exact `U.ClaimGraph`, exact EntityOfConcern, and effective `U.ReferenceScheme`; test whether `EpistemeConstitutionRelation` obtains under C.2.1.
3. **Classify the expression or use.** Decide whether the current object is the claim-bearing description episteme, a specification use of it, an assertion about another object, a publication form, a carrier, or a representation. Do not infer the answer from a suffix or medium.
4. **Open only a needed neighbor.** Add empirical grounding, viewpoint, view, claim scope, model-use structure, evidence, edition, specification evaluation, publication, form, carrier, currentness, or representation only when the named receiving use depends on its direct relation.
5. **Stop at the smallest sufficient result.** Do not produce a universal description card. A readable sentence naming the receiving use, the recovered episteme, its EntityOfConcern, and the one needed neighboring relation is normally enough.

The ordinary minimum is prose, not a mandatory record:

> For `<receiving use>`, episteme `<E>` carries claims `<G>` about exact EntityOfConcern `<T>` under effective scheme `<R>`. `<One named neighboring relation>` is additionally current because `<the next action depends on it>`.

If no neighboring relation is needed, omit the second sentence. If the C.2.1 triple or the required direct governor cannot be recovered, return that exact blocker instead of filling a generic context field.

### E.10.D2:4.1 - Core recovery discipline

#### E.10.D2:4.1.1 - EntityOfConcern

`EntityOfConcern` is the one exact independently identified `U.Entity` about which the selected claim-bearing whole makes its claims. It may be a system, work occurrence, method, episteme, direct relation occurrence, characteristic, structure, pattern, or another admitted entity. It is neither a universal object bucket nor the authoring target merely because the author is editing it.

A ClaimGraph may designate several other entities as participants in relational, comparative, negative, counterfactual, or modal claims. Those designations do not by themselves create a joint EntityOfConcern. Select a relation occurrence, collection, or structured whole only after its direct pattern independently identifies that entity.

#### E.10.D2:4.1.2 - Description episteme

A description episteme is an ordinary `U.Episteme` whose exact `U.ClaimGraph` contains descriptive claims about its exact EntityOfConcern under its effective `U.ReferenceScheme`. Its identity is the C.2.1 constitution triple; E.10.D2 adds no `subjectRef`, description slot, `isDescriptionOf` relation, context constituent, or peer description ontology.

Its ClaimGraph may contain labels, characterizations, criteria, structural or behavioral claims, diagrams interpreted under a scheme, or other claim-bearing content. Those claims and representations do not become parts or properties of the EntityOfConcern unless the corresponding direct subject pattern establishes them.

For one named describing use, state the exact viewpoint P it selects when that selection changes interpretation or action. Keep the episteme, its EntityOfConcern, the use, and P distinct. The selection is not an episteme identity discriminator and establishes neither viewpoint conformance nor `U.View` membership.

#### E.10.D2:4.1.3 - Specification-use admission

Use a `...Spec` name only when the receiving use depends on specification force and all applicable conditions are recoverable:

1. the exact description episteme and its C.2.1 constitution;
2. checkable claims, invariants, criteria, or acceptance conditions in its ClaimGraph;
3. a named harness, validation, conformance, measurement, or evaluation relation capable of checking those claims for the stated use;
4. when viewpoint selection affects reliance, the named describing use and its exact selected viewpoint are preserved or explicitly updated.

Declared formality, notation discipline, comparators, tolerances, and measurement rules are named when the claims depend on them. They do not substitute for the checkable claims or the harness. If the conditions are absent, call the episteme a description and present proposed criteria as proposals; a `Spec` suffix, schema, signature, approval, or publication does not supply specification force.

Specification use does not create another episteme identity. A revision that changes ClaimGraph, EntityOfConcern, or effective ReferenceScheme identifies another episteme under C.2.1; a changed harness, evaluation result, publication, or relying use changes its own neighboring object or relation.

#### E.10.D2:4.1.4 - Model-use structure

A `BoundedModelUseStructure` is selected only when the receiving assertion, calculation, interpretation, comparison, or other use depends on the organization of admitted model-applicability, model-use, and coherence relations governed by A.1.1. The receiving use designates that exact structure through its direct relation. The structure is never a constituent of description-episteme identity merely because the episteme is used inside it.

If a proposed dependent relation species genuinely requires one exact model-use structure as an identity-bearing participant, its own pattern must declare that participant and its obtaining and identity rules. E.10.D2 supplies no generic context relation as a shortcut.

#### E.10.D2:4.1.5 - Episteme about an episteme

When an episteme is being described, use ordinary recursion: the earlier episteme is the exact EntityOfConcern of the description episteme; the latter has its own ClaimGraph and effective ReferenceScheme. A publication, rendering, or representation of either remains separate. No mandatory context recursion, meta-description kind, or second episteme ontology is needed.

### E.10.D2:5 - Naming discipline

**Default suffix.** Use `...Description` when naming a description episteme for a practitioner-facing use.

**Reserved suffix.** Use `...Spec` only when the specification-use conditions above obtain. Do not use it as a synonym for detailed, official, approved, formal-looking, or stored in a schema.

**Entity names.** Name the EntityOfConcern by its independently governed kind and identity: one exact local system-role kind, `Method`, `System`, `Architecture`, `Characteristic`, `PromiseContent`, `Work`, `Episteme`, or another exact kind. Append `Description`, `Spec`, `View`, `Publication`, `Form`, `Carrier`, or `Representation` only when that neighboring object is what the name actually designates.

**Relation language.** Prefer the direct governing verb: a description carries claims about an entity; a publication occurrence makes an edition available; a carrier bears a form; a representation corresponds under a scheme; evidence supports an assertion; an admitted system performs work. Do not turn those verbs into one generic description link.

**Ambiguous role language.** When source wording says that a description, source, standard, requirement, evidence item, publication, dashboard, or view “has a role,” recover its exact evidence-use, source-use, standard-use, requirement-use, publication-use, assurance-use, or gate-use relation. For a claimed Work use, name the exact premise, governed reference, decision-use relation, or A.6.1 operation-argument binding and its actual participants. If the claimed use needs another relation and no direct governor supplies its predicate and participants, return the exact `missing-governor` result rather than inferring a universal description-to-Work or episteme-to-Work relation. Open one exact occurrence of a directly declared `U.SystemRoleAssignment` species only when an independently admitted `U.System` is assigned to one exact local system-role kind for the bounded work; an acting holon is eligible only after that exact entity has independently passed `U.System` admission for this claim.

### E.10.D2:6 - Invariants

**D2-1 (Direct constitution).** Every description episteme is identified through the exact C.2.1 `<ClaimGraph, EntityOfConcern, effective ReferenceScheme>` constitution; no local record or tuple replaces it.

**D2-2 (Entity-description distinction).** The EntityOfConcern and a description episteme about it are distinct, including when the EntityOfConcern is itself an episteme.

**D2-3 (Specification is a use).** Specification force requires checkable claims and a named harness or validation relation. When viewpoint selection affects reliance, preserve or update the named describing use and its exact selection. Specification is not a peer class or label effect.

**D2-4 (Conditional neighbors).** Grounding, viewpoint, view, claim scope, model-use structure, evidence, edition, publication, carrier, currentness, and representation enter only through their subject patterns when the receiving use depends on them.

**D2-5 (Stable identity across use).** Changed description use, viewpoint selection, harness, evidence, publication, form, carrier, rendering, or representation does not by itself change episteme identity.

**D2-6 (Work and authority separation).** An episteme, plan, checklist, specification, standard, file, or dashboard performs no work and grants no permission, acceptance, assurance, or world-side truth without the exact direct relation.

**D2-7 (No label-only sameness).** Identical labels across schemes, scopes, viewpoints, model-use structures, or contexts establish neither the same EntityOfConcern nor the same episteme. Use the governing identity and Bridge rules.

**D2-8 (Representation separation).** A tuple, card, graph node, schema field, notation token, file, or UI element may participate in a representation or publication of a recovered object; it is not that object by position or appearance.

**D2-9 (No generic context relation).** E.10.D2 defines no `U.EpistemeSlotRelation`, positive `DescriptionContext` value or tuple, `BoundedContextRef` constituent, mandatory context recursion, or universal description relation. The old names may appear only as explicitly rejected source wording.

### E.10.D2:7 - Recovery decisions

| Current need | Recover | Do not infer |
|---|---|---|
| Identify or cite the claim-bearing description | Exact ClaimGraph, exact EntityOfConcern, effective ReferenceScheme, and obtaining C.2.1 constitution | Identity from title, file, card, context field, or publication |
| Read one episteme for a concern-bearing describing use | The named describing use and the exact viewpoint P it selects when that selection changes the reading | Viewpoint conformance, `U.View` membership, or another episteme identity |
| Rely on description as a specification | Checkable claims and an exact checking harness or validation relation; preserve or update a selected viewpoint only when reliance depends on it | Specification force from suffix, formality, approval, or storage format |
| Use a selected organization of model use | Exact A.1.1 BoundedModelUseStructure designated by the receiving use | Structure as an episteme constituent or generic context |
| Describe an episteme | A new C.2.1 episteme whose EntityOfConcern is the earlier episteme | Mandatory meta-description layer or context recursion |
| Use unchanged content differently | The same episteme when all three identity discriminators remain fixed, plus the changed neighboring use relation | A new episteme merely from changed viewpoint selection, evidence, publication, carrier, or representation |
| Use a changed ClaimGraph, EntityOfConcern, or effective scheme | Another episteme under C.2.1 | Continuity from a retained label or file path |

### E.10.D2:8 - Neighboring use routing

Open a neighboring object only after naming the receiving use and recovering the description episteme. The same episteme can participate in several of the uses below; each use retains its own subject pattern, participants, obtaining condition, and identity.

#### E.10.D2:8.1 - Describing use, viewpoint, and view

For one named describing use, state that the use selects one exact `U.Viewpoint` episteme P when that selection changes what is read or checked. It says from which concern-bearing viewpoint the already identified episteme is being read for that use.

That selection:

* does not acquire C.2.1 episteme identity;
* does not establish `EpistemeViewpointConformanceRelation`;
* does not admit or remove same-individual `U.View` membership;
* selects no receiving view and performs no A.6.3 viewing construction;
* may change between two describing uses while the episteme remains unchanged.

Call the same episteme a `U.View` only when it conforms to at least one exact `U.Viewpoint` episteme under E.17.0's fixed membership rule. Direct authoring and A.6.3 source-to-receiving construction can produce an episteme but grant no view membership. A rendering, publication form, or carrier-borne display is not a view by appearance. If one use must select several viewpoints, first identify their exact C.13 collection and any organization the use actually needs; do not overload one context qualification.

#### E.10.D2:8.2 - Scope, model use, grounding, evidence, and currentness

Use A.2.6 when the receiving use depends on the exact claim scope and its context-slice membership. Use A.1.1 when the receiving use depends on one exact `BoundedModelUseStructure`. Neither scope nor structure becomes a description constituent merely because a table displays it.

Use C.2.1 empirical grounding only when claims must be mapped to exact observation, intervention, measurement, or test relations involving one grounding holon. Use A.10 when the use relies on an exact evidence-provenance path; use B.3 when an assurance claim is made or its material-reliance threshold is met. Evidence, assurance, or an evaluation result can support an assertion about a description or its specification use; none makes the subject-side claim true, changes the EntityOfConcern, or mutates the description episteme. State the exact validity or reliance window when that receiving use depends on one.

Use G.11 when currentness of the description edition, evidence path, harness, viewpoint, publication, or another neighbor matters to the receiving use. A currentness judgment applies to that exact object or relation; it is not a generic status field of the EntityOfConcern.

Where claims cross reference schemes, first recover the exact F.17 source and receiving senses and the obtaining F.9 Bridge needed by the direct use. A separate current C.2.1 claim states whether that Bridge is suitable for the named bounded use, direction, correspondence rule, and loss tolerance; A.10 or B.3 separately governs reliance. A Bridge, profile, card, or shared spelling is neither a licence nor proof that comparison, translation, or work occurred.

#### E.10.D2:8.3 - Edition, publication, form, and carrier

Changed ClaimGraph, EntityOfConcern, or effective ReferenceScheme identifies another episteme under C.2.1. When the receiving use also claims continuity between two epistemes, use the exact C.2.1 edition relation. A version label, file history, publication order, shared name, or collection membership establishes neither another episteme nor edition continuity.

Use E.24.PUB to distinguish these actual publication-side objects and relations:

| Current object or relation | What it does | What it does not establish |
|---|---|---|
| selected episteme edition | carries the claim content made available | publication occurrence, form, carrier, audience access, or reliance |
| audience-declaration episteme | states the audience criterion | that a concrete receiver obtained, read, understood, or relied on the edition |
| bounded-use-declaration episteme | states supported operations or decisions, conditions, and excluded stronger uses | permission, acceptance, assurance, or actual work by itself |
| publication form | expresses the selected edition for the declared publication use | episteme identity or a durable public form kind by position |
| `U.PresentationCarrier` | physically or digitally bears the publication form | the episteme, the form, or the EntityOfConcern |
| publication occurrence | makes the selected edition available to the declared audience for the declared bounded use | expression, bearing, access work, reading, or reliance |

The subject pattern keeps the verbs exact: `PublicationFormExpressionRelation` relates edition, form, and bounded-use declaration; `PublicationFormBearingRelation` relates form and carrier; `EpistemePublicationRelation` governs bounded availability of the selected edition through that form and carrier. Rendering, printing, uploading, indexing, or access-control work remains dated `U.Work` performed by systems. Plain “published episteme” names contingent participation in a publication occurrence, not a durable `U.EpistemePublication` kind.

One encountered thing can enter several relations without their objects collapsing. A completed inspection card may be a claim-bearing episteme; its reusable layout may be a publication form; a sheet or file may be a carrier; and a publication occurrence may make the selected card-episteme edition available to a maintenance team for one bounded use. Each claim is recovered independently.

#### E.10.D2:8.4 - Representation

Use C.29 when notation elements, diagram elements, tuple positions, graph nodes, table cells, schemas, or tool structures stand in an explicit representation correspondence to independently recovered objects for a declared modeling or reasoning use. A representation can change what users can inspect or calculate without becoming the represented entity, episteme, direct relation occurrence, or proof that the represented predicate obtains.

A diagram therefore has distinct branches:

* if its exact ClaimGraph, EntityOfConcern, and effective ReferenceScheme satisfy C.2.1, the selected claim-bearing whole is an episteme;
* if that same episteme conforms to an exact viewpoint, E.17.0 may admit it as a `U.View`;
* its graphical arrangement may separately be a publication form or a C.29 representation according to the receiving use;
* a screen, sheet, or file may bear the form as a carrier;
* a publication occurrence may make one selected episteme edition available.

No branch follows from visual appearance, generation history, a heading, or a repository path.

#### E.10.D2:8.5 - Work, status, and authority

Only admitted systems perform authoring, evaluation, revision, publication, viewing, query, rendering, and use work under the corresponding work relations. The resulting episteme, publication, carrier, trace, or evaluation result does not perform that work.

Epistemic and deontic statuses over epistemes are not `SystemRoleAssignmentStateRelation` occurrences, system states, or runtime facts about the EntityOfConcern. A gate verdict, permission, commitment, acceptance, requirement use, standard use, source use, or Work authorization needs the pattern that defines, constrains, or tests that claim. Neither a description nor its publication grants those effects by label, approval mark, or availability.

### E.10.D2:9 - Archetypal grounding and bias annotation

**System case.** A service-interface description carries claims about one exact system interface under its effective scheme. The interface is the EntityOfConcern. A selected viewpoint for a safety review, a conformance harness, a publication to operators, and a deployment gate are four separate uses; none belongs in episteme identity.

**Episteme case.** A DRR, pattern, safety case, source set, or model episteme can itself be the EntityOfConcern of another episteme. A review note about it uses ordinary C.2.1 recursion. Its dashboard, PDF, publication, evidence path, and review work remain separate regardless of which one the reader first encounters.

**Card and diagram case.** A filled card or diagram can be a claim-bearing episteme when its C.2.1 constitution is recoverable. Its layout can separately be a publication form or representation, and its file can be a carrier. Filling or displaying it makes no subject relation obtain.

The dominant bias is substitution by the most visible object: a reader sees a file, diagram, dashboard, card, label, or status and lets it replace the independently governed entity, episteme, relation occurrence, or authority needed for the decision. The corrective move is not lexical replacement. Recover the exact object and direct relation for the named receiving use.

### E.10.D2:10 - Anti-patterns and repairs

| Anti-pattern | Symptom | Repair |
|---|---|---|
| **Entity-description collapse** | “The method is the document”; “the architecture is the diagram”; “the role contains the checklist.” | Recover the exact EntityOfConcern and C.2.1 description episteme; handle every subject-side claim under its subject pattern. |
| **Filled-card ontology** | A completed tuple, record, table, or schema is treated as what makes the episteme or relation exist. | Recover the governed object and obtaining relation first; treat the record as an episteme, form, carrier, or representation only when its own recognition conditions hold. |
| **Spec by name** | Any detailed, approved, or formal-looking write-up is called `...Spec`. | Use `...Description` until checkable claims, the describing-use qualification, and an exact harness or validation relation are all recoverable. |
| **Context as identity** | A project, viewpoint selection, or model-use setting is copied into episteme identity. | Keep the C.2.1 identity triple fixed; state only the exact use qualification or neighboring relation the receiver needs. |
| **Describing-use erasure** | A description is read as globally viewpoint-free, or a prior use's selected viewpoint is silently reused. | Name the current receiving use and its exact selected viewpoint when that selection affects the reading; changing the selection alone does not reidentify the episteme. |
| **View by appearance or construction** | A generated table, diagram, query result, or published face is called a `U.View`. | Apply E.17.0 conformance for view membership; use A.6.3 only for actual source-to-receiving construction and E.24.PUB/C.29 for form or representation uses. |
| **Publication as authority** | Availability, an approval mark, card, dashboard, or file is treated as permission, evidence, assurance, gate result, decision, or work. | Recover the exact publication occurrence, then apply the direct governor for the stronger claim. |
| **Carrier identity** | A file path, screen, sheet, or repository entry is treated as the episteme or EntityOfConcern. | Identify the exact carrier and bearing relation while keeping form, publication occurrence, episteme, and EntityOfConcern separate. |
| **Status-state leakage** | Evidence, requirement, approval, or standard status becomes an assignment-state relation or runtime value. | Keep status claims on their exact epistemic or deontic subject; use A.2.5 only for one exact `U.SystemRoleAssignment` satisfying one `SystemRoleAssignmentStatePredicate`. |
| **Episteme-role shortcut** | “The standard plays the compliance role”; “the evidence has the approval role”; “the source authorizes work.” | Recover the exact standard-use, evidence-use, source-use, assurance-use, gate-use, or publication-use relation. For a claimed Work use, name the exact premise, governed reference, decision-use relation, or A.6.1 operation-argument binding and its actual participants; if no direct governor supplies the needed predicate and participants, return the exact `missing-governor` result. Reserve `U.SystemRoleAssignment` for exact assignments of independently admitted systems to local system-role kinds. |

### E.10.D2:11 - Worked examples

Each example begins with a receiving use and stops after the smallest sufficient recovery. It adds no generic description record.

#### E.10.D2:11.1 - Description of a system-role kind

A method author needs readers to recognize work-facing `ChangeAuthoritySystemRole@OperationsReview` before checking any assignment. `ChangeAuthoritySystemRoleKindDescription` is a C.2.1 episteme whose exact EntityOfConcern is that independently admitted local system-role kind, whose ClaimGraph describes its work-facing sense, and whose effective scheme is the selected operations-review reference scheme.

For the named operations-review use, state that it selects the exact operations viewpoint. The ClaimGraph may cite credential criteria, a mandate window, separation-of-duty constraints, capability expectations, and a direct `SystemRoleAssignmentStateRelation` when those neighbors are current. The system-role-kind description contains none of the assignment, checklist, graph, criteria, or relation occurrence. The description admits no holder and creates no `U.SystemRoleAssignment`.

The receiving use needs recognizability, not specification force, so the practitioner stops with the description. A specification use opens only if exact checkable system-role-kind claims and their checking harness are named.

#### E.10.D2:11.2 - Method description

A team wants to teach `BacklogRefinement`, an independently admitted `U.Method`. `BacklogRefinementMethodDescription` is one C.2.1 episteme about that exact method. A.3.2 admits the same episteme as `U.MethodDescription` only when its claims make a substantive statement about the method as a way of doing—for example its applicability, preconditions, effects, bounds, enactment concern, or internal composition.

A practice card's claim-bearing content may be that episteme; its reusable layout may be a publication form or C.29 representation, and its sheet or file may be a carrier. Classify a calendar session, chat thread, or ticket update from its actual facts as a Work occurrence, assertion or record, publication-side object, or another object whose kind and applicable relation are already known; medium and label do not decide. An assertion or work record whose claim depends on the exact method-description edition may cite that edition through the exact premise, typed reference, or A.6.1 operation-argument binding required by the receiving claim. Separately, A.15.1 states the exact relation by which an actual dated Work occurrence enacts the admitted Method; the method-description episteme is not a participant of that relation. Bibliographic metadata, approval, or a method label alone grants neither method-description membership nor specification force.

#### E.10.D2:11.3 - Architecture description and view

An architecture review asks how one exact `ArchitectureOf@Context(PaymentService)` addresses the operations concern. An architecture-description episteme carries claims about that architecture under its effective scheme. The named review use selects the exact operations viewpoint.

The episteme is a `U.View` only if the E.17.0 conformance relation to an exact viewpoint obtains. A structural graph can be part of its interpreted claim content, a C.29 representation, or a publication form according to the named use; no visual branch makes the graph the architecture. An ADR or dashboard creates no permission, assurance, or work relevance without the corresponding direct claim. If work uses the description, state the exact premise, reference, decision-use, or operation-argument relation through which the performed work actually consumes it.

#### E.10.D2:11.4 - Specification use

An integration team needs to decide whether a service-interface description is fit to drive a conformance test. The exact interface is the EntityOfConcern of `PaymentInterfaceDescription`; its ClaimGraph states message, ordering, error, and tolerance claims under the effective interface scheme. The current describing use selects one exact integration viewpoint.

The team may call the episteme `PaymentInterfaceSpec` for this use only after the relevant claims are checkable and the exact conformance harness or validation relation is named. If viewpoint selection affects reliance, the named describing use and its exact selected viewpoint are preserved or explicitly updated. Formal notation or an approval signature can help interpret or constrain a neighboring claim, but neither substitutes for those conditions. A changed test result changes the result or reliance claim; it does not reidentify the interface or the episteme.

#### E.10.D2:11.5 - Publication form and carrier

A completed pump-inspection card is a claim-bearing episteme when its exact ClaimGraph, inspected pump as EntityOfConcern, and effective maintenance scheme satisfy C.2.1. The reusable card layout may fill the publication-form participant meaning for a maintenance use; one tablet file may be a `U.PresentationCarrier`; and an E.24.PUB publication occurrence may make the selected card-episteme edition available to a declared maintenance audience.

The card episteme, layout, file, and availability occurrence retain different identities. Filling, uploading, or opening the card is dated work. Availability establishes neither that a technician read it nor that its claims are true or relied upon.

#### E.10.D2:11.6 - Episteme about an episteme

A reviewer writes an assessment of one exact DRR edition. The DRR episteme is the EntityOfConcern of the assessment episteme; the assessment has its own ClaimGraph and effective scheme. A PDF of either may be a carrier, a publication occurrence may make an edition available, and an evidence path may support the review assertion. None of those neighbors requires a meta-description kind or context recursion.

#### E.10.D2:11.7 - Same content, different use

One unchanged equipment-description episteme is first read under a maintenance viewpoint and later under a training viewpoint. Its ClaimGraph, EntityOfConcern, and effective scheme remain fixed, so C.2.1 identifies the same episteme. The two named describing uses select different viewpoints. The second selection neither creates another episteme nor proves conformance to either viewpoint.

If the training use adds another publication occurrence with another form or carrier, or relies on another evidence path, only those neighboring objects and relations change. If the training edition changes a claim or its effective interpretation scheme, C.2.1 instead identifies another episteme; retained wording or a shared file does not preserve identity.

#### E.10.D2:11.8 - Minimal dashboard repair

A project note says, “The architecture dashboard approves the deployment role.” The immediate receiving use is an operations discussion of the release candidate. Recover the smallest truthful result:

* `PaymentServiceArchitectureDescription` is the C.2.1 episteme about exact `ArchitectureOf@Context(PaymentService)`;
* one describing-use qualification selects the exact operations viewpoint;
* the dashboard may be a publication form, carrier, representation, or view only under the recognition rule for that exact use;
* no checkable-claims-plus-harness basis has been named, so specification force is not admitted;
* no gate verdict, permission relation, acting system, system-role assignment, or performed deployment work has been established.

If the exact E.24.PUB objects are recoverable, the admissible next sentence is that one publication occurrence makes the selected architecture-description edition available for operations discussion through a dashboard publication form borne by an exact display or file carrier. “Approves” and “deployment role” remain non-assertable until their direct governors and case facts are named. The practitioner stops there instead of replacing the original sentence with another overloaded noun.

### E.10.D2:12 - Consequences

| Consequence | Cost or boundary |
|---|---|
| Description and specification wording becomes safer across FPF. | Authors must recover one C.2.1 constitution and the receiving use instead of relying on a suffix, title, or filled context record. |
| One episteme can remain stable across changed viewpoint selections, harnesses, evidence, publications, carriers, and representations. | Each changed neighboring use needs its own subject pattern when it matters to the next action. |
| Publication, evidence, assurance, gate, work, state, and system-role-kind or assignment claims remain independently testable. | Prose can become slightly longer when a source phrase compressed several non-substitutable relations. |
| The ordinary move stays small because optional neighbors are opened conditionally. | A genuinely load-bearing neighbor cannot be hidden merely to keep the sentence short. |
| A local application can return an exact blocker. | Reopen when the receiving use, C.2.1 discriminator, required direct governor, or checkability basis cannot be recovered from current facts. |

### E.10.D2:13 - Rationale

The durable core is a two-object distinction: one independently identified EntityOfConcern and one C.2.1 episteme carrying claims about it. Specification is a checkable use of that episteme. Viewpoint selection, view membership, scope, model-use structure, grounding, evidence, assurance, edition, publication, carrier, representation, and work have different reasons to obtain and different identity rules.

Making those neighbors fields of a description tuple would erase those rules and make formality, publication, approval, or a shared context label look constitutive. Requiring all of them for every description would also make ordinary use needlessly heavy. Receiving-use-first routing preserves both reliability and economy: recover the exact constitution, add the one neighbor needed for the next action, then stop.

### E.10.D2:14 - SoTA-echoing and source use

| Source or practice line | FPF use | Boundary |
|---|---|---|
| ISO/IEC/IEEE 42010 architecture-description practice, retained as established-practice lineage | Preserve the useful separation among described architecture, concern-bearing viewpoint, view, correspondence, and publication when testing architecture cases. | It is neither FPF ontology nor a claim about the current best architecting method; it grants no evidence, assurance, gate, decision, or work authority. |
| ISO/IEC/IEEE 29148:2018 requirements-engineering practice, retained as established specification lineage | Stress that specification use depends on checkable requirements, verification or validation, and a named life-cycle use rather than official appearance. | The standard does not supply C.2.1 identity, E.17.0 describing-use viewpoint selection, or the direct FPF checking relation; detailed prose is not a specification by name. |
| Current FPF C.2.1, E.17.0, E.24.PUB, A.1.1, A.2.6, A.10/B.3, G.11, and C.29 interfaces | Supply the authoritative local identities and direct-use boundaries for episteme, viewpoint/view, publication, model use, scope, reliance, currentness, and representation. | E.10.D2 consumes those interfaces; it does not mint a rival description ontology or copy every neighbor into one pattern. |
| Rodin's constructive identity and near-sameness line, used as conceptual lineage | Keep same-label and different-presentation cases answerable by explicit identity discriminators and evidence-backed comparison. | Similar wording or a shared formal substrate does not establish the same EntityOfConcern, same episteme, an obtaining Bridge, or admissible substitution. |

Reopen this source-use synthesis when a cited standard changes the practical distinction, or when the current FPF constitution, viewpoint, publication, specification-use, Bridge, or representation interface changes enough that one of the routed decisions above would be stated differently. A newer source matters only when it changes the working decision, not merely because it is newer.

### E.10.D2:15 - Relations

**Builds on:**

* **A.7 - Strict Distinction.** Supplies the general discipline for keeping an independently governed entity distinct from epistemic and presentation-side objects around it.
* **C.2.1 - Episteme Identity, Constitution, Grounding, and Edition.** Supplies the exact ClaimGraph, EntityOfConcern, effective ReferenceScheme constitution and the neighboring grounding and edition relations.
* **E.10 - Ontological Precision Restoration.** Supplies subject-first recovery and the rule that a word, field, position, or representation does not create the governed object.

**Coordinates with:**

* **E.17.0, E.17, and E.24.PUB.** Use E.17.0 for a named describing use's viewpoint selection, viewpoint membership, and view membership; use E.17 and E.24.PUB for publication occurrence, publication form, and carrier bearing. None of these changes C.2.1 identity.
* **A.2.6 and A.1.1.** Govern claim scope and bounded model-use structure only when the receiving use depends on them.
* **A.10, B.3, and G.11.** Govern evidence provenance, assurance reliance, and currentness for exact objects and relations.
* **C.29, A.6.2, A.6.3, A.6.4, and F.9.** Govern representation, episteme morphing, source-to-receiving construction, retargeting, and cross-scheme Bridge semantics without label-only sameness.
* **A.3.2, F.4, and F.5.** Define method-description membership, system-role-kind-description content, and naming after the exact object and local sense are recovered.
* **A.15.1 and direct receiving-use patterns.** Govern performed work and the exact premise, reference, decision-use, or operation-argument relations through which work actually uses an episteme.

### E.10.D2:16 - Repair moves

Use these repairs on live prose; retain old spellings only as quoted source-side trigger wording:

1. Start with the exact receiving work, decision, comparison, inquiry, preservation, teaching, or publication use and its next unresolved question or action.
2. Replace `DescribedEntity*`, `EntityOfInterest`, `EoI`, `EoIClass`, and generic “object under description” wording with the exact EntityOfConcern and its independently governed identity.
3. Replace local episteme-slot, subject-field, tuple, card, or context-record constitution with the exact C.2.1 ClaimGraph, EntityOfConcern, and effective ReferenceScheme test.
4. Replace peer-layer I-D-S wording with EntityOfConcern, description episteme, and admitted specification use; specification is not a third peer kind.
5. Replace a positive source-side `DescriptionContext` with the named describing use and the exact viewpoint it selects when that selection changes the reading. Keep selection outside episteme identity, conformance, and view membership; do not recreate the rejected tuple under another name.
6. Replace “the role contains a characteristic space, state relation, or checklist” with a precise claim: the system-role-kind-description episteme characterizes one exact local system-role kind using claims that cite those independently governed objects or relations.
7. Replace carrier identity with the exact publication form, `U.PresentationCarrier`, bearing relation, and publication occurrence required by the current use.
8. Replace `...Spec` names lacking checkable claims and a named harness or validation relation with `...Description`. Preserve or update the selected viewpoint only when the relying describing use depends on it.
9. Route permission, evidence, assurance, gate, decision, promise, commitment, work, publication, view, Bridge, retargeting, currentness, and representation claims to their exact direct governors.
10. Replace “role of this description, source, standard, evidence, or publication” with the exact typed use relation. Use one exact occurrence of a directly declared `U.SystemRoleAssignment` species only for an independently admitted `U.System` assigned to one exact local system-role kind; an acting holon is eligible only after that exact entity has independently passed `U.System` admission for the claim.
11. Delete mandatory context recursion for descriptions of epistemes; use ordinary C.2.1 recursion with the earlier episteme as EntityOfConcern.
12. Stop when the recovered constitution and one needed neighboring relation make the next action clear; do not complete a universal description card.

### E.10.D2:17 - Conformance checklist

| ID | Check |
|---|---|
| **CC-D2-1** | Is the exact receiving use and its next question or action named before optional qualification machinery is opened? |
| **CC-D2-2** | Does every description episteme recover the exact C.2.1 ClaimGraph, EntityOfConcern, and effective ReferenceScheme, without a local slot relation or record-shaped constitution? |
| **CC-D2-3** | Is the EntityOfConcern independently identified and kept distinct from the description episteme, including in episteme-about-episteme cases? |
| **CC-D2-4** | When one describing use selects a viewpoint, are the use and exact viewpoint named separately from episteme identity, conformance, and `U.View` membership? |
| **CC-D2-5** | Does every `...Spec` use have checkable claims and an exact harness or validation relation, with any reliance-relevant viewpoint selection preserved or updated for the named describing use? |
| **CC-D2-6** | Are grounding, view, scope, model-use structure, evidence, assurance, edition, currentness, publication, carrier, and representation opened only when the receiving use depends on their direct relation? |
| **CC-D2-7** | Are publication occurrence, form, carrier, view, representation, file, dashboard, and work record kept distinct from the EntityOfConcern and episteme? |
| **CC-D2-8** | Is current prose free of peer-layer I-D-S vocabulary, `intensional object`, `DescribedEntity*`, `EntityOfInterest`, `EoI`, `EoIClass`, mandatory context recursion, and a local DescriptionContext tuple? |
| **CC-D2-9** | Is the word `plane` absent for this distinction, with `ReferencePlane` reserved for a subject pattern such as CHR that actually defines it? |
| **CC-D2-10** | Is wording about the “role” of a description, source, standard, requirement, evidence item, publication, dashboard, or view resolved to its exact typed use rather than a spurious `U.SystemRoleAssignment`? |
| **CC-D2-11** | Do systems perform work while epistemes carry claims, and are statuses, gate verdicts, permission, acceptance, assurance, and runtime state kept under their subject patterns? |
| **CC-D2-12** | Does the application stop at the smallest sufficient result or return one exact missing-fact or missing-governor blocker? |

### E.10.D2:18 - Phrasebook

| Avoid | Use |
|---|---|
| “The role contains the state graph.” | “The system-role-kind description carries claims about one exact local kind and may cite a separately governed `SystemRoleAssignmentStateRelation`; the graph is a representation only when that use is current.” |
| “The diagram is the architecture.” | “Recover the architecture-description episteme first; then classify the diagram as claim content, `U.View`, publication form borne by a carrier, or C.29 representation only under the rule for the named use.” |
| “MethodSpec draft.” | “MethodDescription draft; specification use is not admitted until checkable claims and the exact harness or validation relation are present. Name a viewpoint only when the relying describing use depends on it.” |
| “The PDF is the method.” | “The method-description episteme concerns the exact method; the PDF carrier bears a publication form that expresses a selected episteme edition.” |
| “Same label, same thing.” | “Compare ClaimGraph, EntityOfConcern, and effective scheme; when schemes differ, recover the exact senses, obtaining Bridge, and bounded-use reliance claim.” |
| “Evidence status is a role state.” | “The status claim concerns its exact epistemic or deontic subject; use `SystemRoleAssignmentStateRelation` only for one exact assignment and predicate, or the direct system-state relation for another runtime fact.” |
| “The source has the approval role.” | “State the exact source-use, evidence-use, assurance-use, gate-use, or publication-use relation. For a claimed Work use, name the exact premise, governed reference, decision-use relation, or A.6.1 operation-argument binding and its actual participants; otherwise return the exact `missing-governor` result. None is a work-facing role assignment by wording.” |
| “Fill the description context tuple.” | “Name the receiving use and the exact viewpoint it selects only when that selection changes what the receiver reads or checks; do not create a context tuple.” |
| “The dashboard approves deployment.” | “An exact publication occurrence may make the architecture-description edition available through a dashboard form borne by a carrier; an exact gate verdict or permission relation is separately required for approval.” |

### E.10.D2:19 - Didactic memory

Use the short memory **use, claims, entity, scheme, one needed neighbor**:

1. **Use.** What exact work, decision, inquiry, comparison, preservation, teaching, or publication use needs the description?
2. **Claims.** What exact ClaimGraph is being used?
3. **Entity.** What exact independently identified EntityOfConcern are those claims about?
4. **Scheme.** What effective ReferenceScheme makes the claims readable about that entity?
5. **One needed neighbor.** Does the next action actually need a describing-use viewpoint, specification checking, grounding, scope, model-use structure, evidence, edition, currentness, publication, carrier, representation, Bridge, or work use?
6. **Stop.** Add only that direct relation, or stop after constitution if none is needed.

The older memory “entity, description, admitted specification use” remains a useful three-word reminder, but it is not a three-kind ontology. Entity names the independently governed concern; description names the C.2.1 claim-bearing episteme used descriptively; specification names a checkable use admitted for one receiving purpose.

### E.10.D2:End

