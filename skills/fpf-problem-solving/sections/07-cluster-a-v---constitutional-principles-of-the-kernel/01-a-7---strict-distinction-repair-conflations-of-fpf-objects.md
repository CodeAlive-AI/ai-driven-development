## A.7 - Strict Distinction: Repair Conflations of FPF Objects (Clarity Lattice)
> **Status:** Stable

### A.7:0 - Use this when

Use this pattern when one sentence, diagram, card, identifier, file, plan, or run is being read as several nearby FPF objects and the team needs to recover the exact relation position before checking the recovered claim under its exact subject predicate. A frequent case is deciding whether the live object is a Method, an episteme that qualifies as MethodDescription, a system Capability, a WorkPlan, or dated Work.

**What goes wrong if missed.** A label such as *algorithm*, *SOP*, *recipe*, or *script* is treated as membership evidence; a direct Method reference is forced through a document; or a description, plan, capability and occurrence inherit one another's force.

**What this buys.** A practitioner can identify the current object, make the smallest direct claim, and stop without manufacturing a description, execution, evidence, gate, or authority relation.

**Primary working object.** The exact sentence or publication position whose nearby objects have been conflated. A.7 restores the distinctions; A.3.1 is the pattern for the Method, C.2.1 is the pattern for episteme identity, A.3.2 is the pattern for same-individual `U.MethodDescription` membership, A.15 is the pattern for plan and Work, and naming/reference patterns contain the defining content for designation and resolution.

**First useful move.** Name the object the receiving use actually needs. For a suspected MethodDescription, first identify one admitted `U.Episteme`, then require one admitted `U.Method` as its exact `EntityOfConcern` and at least one substantive claim about that Method as a way of doing. For a direct Method use, resolve the identifier or receiving `methodRef` under its effective reference scheme; do not invent a MethodDescription.

**Not this pattern when.** If the current object and direct relation are already clear, use the applicable pattern immediately. A.7 supplies no decision about Method identity, episteme identity, MethodDescription membership, capability adequacy, work readiness, occurrence, evidence, publication, or gate passage; handle each such claim under its applicable pattern.

### A.7:1 - Intent

Provide a **single, didactically clear lattice of distinctions** for recognizing and correcting category errors. The pattern addresses four recurrent confusions:

1. **System-role kind vs function** (classification vs behaviour),
2. **MethodDescription vs Method vs Capability vs Work** (description vs abstract way-of-doing vs system ability/envelope vs performed occurrence),
3. **Holon vs System vs Episteme** (what can act and what cannot),
4. **EntityOfConcern vs Description episteme, View, and Publication** (the item under concern vs epistemes and publication relation positions that make it available; specification is a gated use or refinement of a Description episteme, not a third peer member of this distinction).

It harmonizes A.2 and A.2.1 for system-role kinds and system-role-assignment relations, A.3.4 for transformation, A.10 for evidence-provenance and carrier and source-currentness relations, A.14 for advanced mereology, A.15 for System-Role-Method-Work alignment, C.2.1 for episteme constitution and its separate empirical-grounding and edition relations, E.17 for publication and view discipline, and F.9, F.17, and F.18 for bridge and naming discipline.

### A.7:2 - Problem frame

* **Holons (A.1) and systems.** All holons are part-whole units; a System can act because its organization satisfies A.1. Add a local system-role-kind classification or assignment only when the receiving claim uses that stronger distinction.
* **Transformation (A.3.4), Work, and optional attribution.** A claimed change names the affected entity and the direct transformation facts used by the claim. For a precise dated Work claim, first recover each actual performer System and its A.13 core: local agential kind and criterion, classification, obtaining assignment, scope, working situation, window, and supporting evidence. Then admit the occurrence independently under A.15.1 from its performance history, at least one Method actually followed, temporal extent, and at least one obtaining local containing-System relation. A short Work reference may leave these facts implicit only when they remain recoverable. If the current claim must also identify the assignment under which the Work was performed, name the same obtaining assignment and check that attribution separately through F.6. F.6 identifies neither performer nor assignment, and a failed check leaves Work intact.
* **Method and Work backbone (A.3.1, A.3.2, A.15).** Keep MethodDescription, Method, Capability, WorkPlan, and Work distinct. Name only the values used by the current claim. A System acts; a local kind, assignment, Method, or episteme does not.
* **Evidence (A.2.4, A.10).** Identify the exact episteme and the claim for which it is used as evidence. Add provenance, carrier, source-currentness, and reliance relations when the use requires them. Systems inspect or revise epistemes, publish or store their representations on carriers, and rely on their claims; those epistemes do not perform these actions.

Practitioner check: recover the intended referent and action in sentences such as “the document decided” or “the process executed itself”. Correct a literal or metonymic claim that assigns the action to a participant unable to perform it. Keep established shorthand when the capable System and its action are recoverable.

Boundary for use from other patterns: A.7 restores the `EntityOfConcern`, the admissible describing relation, and the publication boundary; then use the defining or testing rule for the remaining claim, with its PatternID kept only as a locator. Do not let A.7 turn an architecture, structure, work, method, evidence, characterization, or decision question into a general discussion of descriptions. If the `EntityOfConcern` is itself a Description episteme or view, keep the pattern centered on that episteme as the item under concern; description-of-description or publication-force issues open only when they are the exact claim being made.

### A.7:3 - Problem

When documents blur the above lines, three classes of defects appear:

1. **Category collapse.** People write “function”, “role”, or “process” interchangeably; teams then disagree whether they are changing a MethodDescription, a Method, a Capability envelope, or reporting an actual Work occurrence.
2. **Agency misplacement.** Epistemes (documents, models) are treated as doers; collectives as raw sets; or a “holon” is used where **only a system** makes sense.
3. **Audit failures.** A MethodDescription alone is taken to establish that its Method was performed; a Work claim lacks its occurrence basis or time span; or a Description episteme, a Description episteme admitted for specification use, a View, publication face, publication unit, or carrier is treated as the `EntityOfConcern`, decision, permission, gate, work occurrence, or assurance result merely because of its label or publication position.

### A.7:4 - Forces

| Force                                        | Tension                                                                                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Didactic brevity vs conceptual precision** | Teams want short words (“process”, “function”) ↔ the framework must keep the four distinction families apart.                          |
| **Universality vs domain idioms**            | We admit engineering idioms (procedure, SOP, algorithm, workflow) ↔ internally we must map them unambiguously.                    |
| **Parsimony vs completeness**                | Minimal concept set ↔ enough distinctions to avoid the classic traps: system-role kind versus function; description, Method, Capability, and Work; and episteme versus carrier. |

### A.7:5 - Solution — The **Clarity Lattice** (normative distinctions & safe vocabulary)

#### A.7:5.1 - **Terminology (normative): orthogonal characteristics**
- **senseFamily** — the categorical characteristic, used by F.7/F.8/F.9: {Role | Status | Measurement | Type‑structure | Method | Execution}. Rows must be **sense‑uniform**.
- **ReferencePlane** — the referent mode per CHR: {world/external | conceptual | epistemic}.
- **EntityOfConcern and Description-episteme boundary** — the item under concern is separated from Description epistemes (E.10.D2, C.2.1). Specification use requires an independently constituted Description episteme, checkable claims, and a named harness, validation, conformance, measurement, or evaluation relation capable of checking them for the stated use. When viewpoint selection affects reliance, preserve or explicitly update the named describing use and its selected viewpoint. Formality, acceptance conditions, a C.16 measurement criterion, and verification practice may contribute under their direct rules. Specification is not a third member of the strict distinction.
- **DesignRunTag** — the design vs run DesignRunTag. It is not a temporal “plane”, generic layer, or stance.
- **Publication face, form, unit, carrier, and rendering boundary** — Description epistemes, including Description epistemes admitted for specification use, may be made available through publication units, publication forms, faces, renderings, and carriers. Their publication positions do not by themselves identify the `EntityOfConcern`, the Description episteme, or a specification-use gate or refinement; readable form alone establishes no evidence, gate passage, work, assurance, or decision force. The ordinary didactic faces for architectural patterns in FPF are:
  {**PlainView** (explanatory prose), **TechCard** (typed cards and IDs), **NormsCard** (TechCard profile for checklists), **AssuranceLane** (evidence bindings)}. Publication faces and forms are orthogonal to the `EntityOfConcern` and Description-episteme boundary, to specification-use gates and refinements, and to DesignRunTag.
- **Direct Description account and specification-use boundary** — a Description episteme is independently identified under C.2.1 by its complete claim content, exact `EntityOfConcern`, and effective `ReferenceScheme`. A.7 introduces no universal EntityOfConcern-to-Description constructor or morphism. When it matters how the claims were produced, selected, carried, or revised, state the exact authoring, measurement, observation, model, source-use, representation, refinement, or other direct relation that is current. A later specification-use claim must satisfy the preceding conjunction under E.10.D2 and the direct pattern that supplies the capable checking relation.

- **EntityOfConcern / episteme / publication boundary** — `EntityOfConcern` names the exact item under concern. An independently identified episteme may genuinely concern a document, publication face, or carrier; bearing or publishing this episteme does not by itself make that object its EntityOfConcern. A Description episteme makes claims about its exact item under its effective scheme. Publication faces, forms, units, renderings, and carriers may make it available, but presentation alone establishes neither episteme identity nor specification use, evidence, gate passage, Work, assurance, or decision force. Evidence and any constitutive contribution to those relations remain governed by their direct rules.
A.7 establishes the following **distinction groups**. Use their **names** and **scope** exactly as below.

#### A.7:5.2 - System-role kind vs function-like wording, functional behaviour, capability, method, and work

* **System-role kind.** One local `U.Kind` with `U.System` candidates and an operative condition for a stable, assignable, work-facing contribution. Its member/non-member boundary and continuity rule complete the C.3 recovery. A practice or source reference locates the definition; it does not identify the kind. An obtaining assignment occurrence may relate a system to that kind only through a directly admitted `U.SystemRoleAssignment` species. The kind is **not behaviour**. Example: the kind currently named `CoolingCirculatorSystemRole`, whose ThermalLoop-7 provenance locates one definition.
* **Function-like wording.** A source phrase such as "function", "behaviour", "service", or "does X" may name a required transformation or effect (A.3.4), functional behaviour (A.6.F), a capability envelope, a method, performed work, a quality, or a structure. Recover the governed claim before choosing the FPF term.
* **Under a system-role assignment.** A System or acting holon that holds an assignment may have a **Capability** to enact a **Method** under conditions. A precise Work claim still uses A.13 to identify the actual performer and A.15.1 to admit the dated occurrence independently. Add F.6 only if the claim must also identify the assignment under which that Work was performed. The system-role kind, assignment, Method, Capability, transformation, and effect do not substitute for the Work or performer.

Safe rewrite for earlier "Holonic Duality (Substance vs Function)": **Holonic Duality (Substance vs system-role kind).** A `U.System` keeps its identity while its classifications and obtaining assignments change. A contribution named by a system-role kind may call for a Method, a Capability envelope to enact that Method under conditions, and possible Work occurrences; none follows from the kind alone.

**Normative guard:** Use **system-role kind** for that exact local `U.Kind`, an admitted direct species under `U.SystemRoleAssignment` for assignment occurrences, **functional behaviour** for a behaviour claim stated with A.6.F, **Method** for the abstract way-of-doing, **Capability** for a holder System's bounded ability or envelope for a Work family or result class under stated conditions, **Work** for the performed occurrence, and **Transformation** or effect wording for an actual change identified with A.3.4. Do not call the kind or assignment itself a function, and do not define Method as Capability or as the transformation or effect itself.

#### A.7:5.3 - MethodDescription vs Method vs Capability vs Work (description vs way-of-doing vs ability envelope vs occurrence)

* **MethodDescription** — one already identified claim-bearing `U.Episteme` whose exact C.2.1 `EntityOfConcern` is one admitted `U.Method` and whose claims, under its effective `U.ReferenceScheme`, say something substantive about that Method as a way of doing. A transformation or enactment concern, generic participant meanings, applicability, precondition, intended effect or preserved condition, bound, or internal method composition can satisfy the positive threshold. The labels *algorithm*, *SOP*, *recipe*, *script*, *procedure*, code, diagram, or design-time artifact are cues only. Authoring, revision, citation, publication, approval, or use time establishes neither episteme identity nor `U.MethodDescription` membership. Its publication cites A.10 carrier/source-currentness refs when the carrier is used as evidence or source.
* **Method** — the **abstract order-sensitive way-of-doing** composed with **Γ\_method** (B.1.5). A Method is not an occurrence, description episteme, or system ability. Actual participants and operation values remain occurrence-side facts of separately admitted `U.Work` and its direct bindings.
* **Capability** — a named holder System's **bounded ability or envelope** for a Work family or result class, stated with its operating and resource conditions, measures, qualification window, and currentness condition. Name a Method or system-role assignment only when that exact condition or fit input is current. It is not the MethodDescription and not the performed Work.
* **Work** — the **dated run-time occurrence** (what actually happened), with resource spend (Γ\_work) and temporal coverage (Γ\_time).

**Designation, reference, and description are different.** A Method identifier designates one exact `U.Method` under the applicable designation rules of an effective `U.ReferenceScheme`. A receiving claim's `methodRef` separately resolves under its effective scheme to that same Method. Neither operation needs a MethodDescription. Cite a separate `methodDescriptionRef` only when that receiving claim actually depends on claims in an exact episteme edition that has already passed A.3.2 membership.

**Minimally viable reference and membership case.** Under `MaintenanceReferenceScheme-2026`, identifier `PumpSealInspectionMethod` designates exact admitted Method `M-PSI`. `MaintenancePlan-47` is a separately governed `U.WorkPlan`; its `methodRef = PumpSealInspectionMethod` resolves directly to `M-PSI`, without a description hop. Episteme `PumpSealInspectionGuide-e3` is independently identified by C.2.1 from its exact claim content, `EntityOfConcern = M-PSI`, and effective scheme. Its claims state the inspection precondition, ordered clean–inspect–classify way of doing, rejection bound, and stop; the same episteme therefore passes A.3.2 membership as `U.MethodDescription`. If `MaintenancePlan-47` relies on those exact e3 claims, a separate `methodDescriptionRef = PumpSealInspectionGuide-e3` may be cited. The plan, Method, MethodDescription, Capability and any later Work remain different objects.

**Recognizable near misses.** A catalogue row containing only `PumpSealInspectionMethod` designates or mentions a Method but is not a MethodDescription. A file named `PumpSealInspectionSOP-v3.pdf` supplies neither the C.2.1 episteme identity nor the substantive method claim by filename. `methodRef = PumpSealInspectionMethod` does not imply that a description exists. A newly authored, revised, cited, approved, published, or used episteme does not gain membership unless its exact Method EntityOfConcern and substantive way-of-doing claim satisfy the same test.

**Normative guard:** A MethodDescription alone does not establish that its Method was performed. Its claims may support a named claim only through the applicable evidence-use relation; never present Method or Capability as if it had happened; never define Method as Capability; never infer MethodDescription membership from form, label, lifecycle time, or use. Resolve direct Method designation and receiving references without mandatory description indirection.

#### A.7:5.4 - Holon vs System vs Episteme (who can act)

* **System or acting holon.** A System can act because its physical or operational organization satisfies A.1. An ordinary sentence may name the recognizable System by a contribution noun: `The engineer designed the pump`, `The reviewer checked the manuscript`, or `The service accepted the request`. Keep that wording when the System and contribution are recoverable and no receiving inference depends on a local system-role kind or assignment identity.
* **System-role kind and assignment, when current.** Add a local system-role-kind classification and obtaining assignment when their identity, extent, or participants are used by the claim, including the A.13 core for precise Work admission. State the admitted assignment species when that relation is current. Precise attribution of an already admitted Work to that assignment remains a separate F.6 claim. The assignment and kind do not make the System able to act and do not act themselves.
* **Capability, Method, and Work, when current.** Name Capability only for an ability or envelope claim, Method only for the way of doing, and Work only for a performed occurrence. An ordinary actor sentence need not materialize all three.
* **Episteme.** An episteme cannot act. A System may author, revise, use, or publish it; state the actual operation, Work, carrier, publication, evidence, or source relation only when the receiving claim uses that distinction.
* **Holon.** Use the umbrella word only when systemness is not part of the claim. If action is asserted, the acting entity must satisfy A.1 as a System; an assignment is not the admission test.

**Progressive example.** `The design team selected valve V-12` is enough for an ordinary design account when the team is a recoverable collective System and no later inference needs a precise Work or assignment identity. If an audit claims dated `ValveSelectionWork-47`, use A.13 to recover `DesignTeamSelectionSystem` as the actual performer with its core basis, then A.15.1 to admit the Work independently from the occurrence facts in :2, including at least one Method actually followed. If the audit must also identify the assignment under which that Work was performed, use F.6 to check `ValveSelectionAssignment-47` and compare its holder with the already identified performer. Keep the core's admitted assignment species, assigned local kind, extent, and evidence recoverable; add another Method, Capability, or further evidence detail only to the degree used by the audit.

#### A.7:5.5 - Episteme vs publication carrier and source-currentness record

* **Episteme** — one C.2.1 knowledge holon identified by its complete claim content, exact `EntityOfConcern`, and effective `ReferenceScheme`. Its content may include a claim, model, or requirement set.
* **Publication carrier** — the physical or digital bearer of an episteme publication or stored representation (file, volume, dataset item).
* **Source-currentness record** — a record of claims about source currentness for a stated use and conditions, distinct from the source episteme and the carrier bearing the record. Use the applicable A.10/G.11 relations when the receiving evidence, source, or reliance claim depends on them.
* **Use:** Evidence use relates an exact episteme to the claim for which it is used (A.2.4). Arguments and validity concern its claims; provenance and reproducibility also need the source, production, carrier, or checking conditions on which the particular use depends. Apply A.10 and B.3 only for the provenance, reliance, or assurance claims actually made.

**Normative guard:** When “we updated the spec” matters to the receiving use, state whether its C.2.1 claim content, EntityOfConcern, or ReferenceScheme changed, a carrier changed, or a source-currentness claim was updated. Name the affected object and its direct relation; a carrier change alone does not establish a new episteme.

#### A.7:5.6 - Formal inclusion, world-side collection, and collective System

- **Mathematical or representation inclusion** — say that an element is in a set, a value fills a tuple place, or a value lies in a coordinate domain under the applicable mathematical statement. Keep the statement with its defining mathematical rule; use `C.29` for an actual mathematical-lens use and `A.19` when a characteristic scale or coordinate is current. No world-side belongs-to relation follows.
- **World-side collection** — identify the collection and use its subject-specific belongs-to rule. That rule says who or what may belong, when belonging begins and ends, whether it may recur, and how past belonging is stated. Belonging alone establishes neither parthood nor holonhood, but it does not prohibit a separately grounded constructive part relation.
- **Collective System** — treat a team or other grouping as an acting System only after the candidate passes all six `A.1` matters. A list, formal set, catalogue, or belongs-to statement does not establish that result.
- **Use the direct relation for every stronger claim:**

  - **ComponentOf** — mechanical or structural part in systems.
  - **ConstituentOf** — logical or content part in epistemes.
  - **PortionOf** — quantitative portion with conserved extensives.
  - **PhaseOf** — temporal part of the same carrier over a proper interval.
  - **System-role assignment** — a System is the `HolderSystemSlot` value in one obtaining occurrence of a directly admitted `U.SystemRoleAssignment` species.

**Normative guard:** Formal inclusion establishes no world-side belonging. Collection belonging establishes neither constructive parthood nor holonhood and does not make either impossible. If a grouping is claimed to act, test it against all six `A.1` matters. Add a local system-role kind, assignment, Method, Work, or constructive part relation only when that separate claim obtains.

#### A.7:5.7 - Operator alignment (required names)

* **Γ\_sys** — composition of **system** properties (physical/systemic).
* **Γ\_method** — composition of **Method** (order, branching).
* **Γ\_time** — composition of **Work** histories and temporal parts.
* **Γ\_work** — composition of **resource spend** and yields tied to Work. Do not track costs with Γ\_method; costs (resources/yield) belong to Γ\_work.

**Normative guard:** Use the four exact operator names for their respective composition claims. For domain “process” or “behaviour”, recover the object and predicate under its direct rule; it may concern a Method, Work, A.3.4 transformation, A.6.F functional behaviour, mechanism, or another domain object. Add an explicit distinction only when the intended value is not cheaply recoverable.

#### A.7:5.8 - EntityOfConcern and Description-episteme boundary vs publication face, form, unit, and carrier boundary (orthogonal, normative)
* **EntityOfConcern-to-description boundary.** A.7 keeps the EntityOfConcern and an episteme that describes it distinct; E.10.D2 supplies the Description and specification-use repair. What the `EntityOfConcern` value is and how it is described are different questions. A Description is a `U.Episteme` about that exact entity under its effective scheme. A named describing use may separately select one viewpoint when the selection changes what is read or checked. Specification is a checkable use or refinement of the independently constituted Description episteme and requires checkable claims plus a named harness, validation, conformance, measurement, or evaluation relation capable of checking them for the stated use. Formality, acceptance, a C.16 measurement criterion, or verification practice may contribute to that test but does not substitute for it. When viewpoint selection affects reliance, preserve or explicitly update the named describing use and its exact selected viewpoint. EntityOfConcern, Description, selected viewpoint, and specification use remain distinct.
* **Publication governs availability.** Publication units, publication forms, faces, renderings, and carriers make Description epistemes available to readers or tools, including Description epistemes admitted for specification use. That availability relation alone identifies neither the `EntityOfConcern` nor the Description episteme and grants no specification use or evidence use. A description may independently concern one of these publication objects. Name A.10 carrier/source-currentness relations when the receiving evidence, source, or reliance use depends on them.
* **Publication-face field pins.** A **TechCard** retains the source pins needed to interpret its claims. For a displayed numeric or comparable characteristic value, resolve the characteristic and its interpretation rule; the **CHR-Pins** fields are {**UnitType**, **ScaleKind**, **ReferencePlane**, **EditionId**}, with each supplied when it affects that interpretation. An E.17 publication profile is separately selected. A nonnumeric description requires no unit or scale merely from being shown as TechCard.
* **Semantic and plane boundary.** A context or ReferencePlane difference alone establishes no F.9 Bridge, `CL`, or trust penalty. When two exact F.17 local senses and the direct F.9 predicate establish a Bridge, cite that relation and a separate bounded-use claim; `CL` remains optional evidence shorthand. A cross-plane use cites its applicable plane relation. Apply a trust penalty only when a named current policy applies to the exact use.

#### A.7:5.8a - Same or near-same EntityOfConcern across descriptions and views

Different descriptions, views, viewpoints, publication units, or role-method-interest positions may concern the same `EntityOfConcern`, different entities of concern, or an unresolved candidate set. A.7 does not accept sameness by publication title, view label, carrier continuity, shared ordinary name, or common reader interest.

Use this split when the text needs to say whether two descriptions or views are about the same thing:

| Case | A.7 relation case | Admissible move |
| --- | --- | --- |
| same referent by value | the localized `EntityOfConcern` or relation named by value, carried by the current claim, or selected by a reference case and the resolved `entityOfConcernRef`, where live, refer to the same item by declared reference discipline | same-entity work inside the declared use |
| preserved by viewing | A.6.3 viewing preserves the exact EntityOfConcern while producing another episteme whose claim content or effective ReferenceScheme may differ; any representation relation and any viewpoint selected for a named describing use remain separate | same-EntityOfConcern Description, Specification, or view transformation |
| publication-unit primary only | a bounded publication unit states what it is mainly about, plus its carried move and outside-work boundary, without establishing a claim-bearing episteme trace by itself | publication-unit stability only |
| bridge-conditional semantic reuse | An F.9 Bridge obtains between two exact local senses, and a separate affirmative bounded-use claim names the proposed use, direction, correspondence rule, tolerated loss, and polarity. A practitioner may first use F.18 to settle the governed value's designations and, only when a durable term row is needed, then use F.17 to constitute that row; neither step establishes the Bridge or licenses reuse, while publication, evidence, and any reliance judgement remain separate. | bridge-scoped semantic reuse only; no entity-identity conclusion follows |
| retargeted under invariant | A.6.4 identifies an exact arrow r between epistemes with different EntitiesOfConcern. A separate C.2.1 bounded-use assertion q about exact r states the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. A separate current-case judgement compares exact facts with q's conditions and proposition and returns `satisfies`, `fails`, or `cannot decide`; `cannot decide` names the missing fact and reopen condition. | retargeted use only after an affirmative q for the named use receives a separate `satisfies` judgement; otherwise retain the exact result, including the missing fact and reopen condition for `cannot decide` |
| unresolved candidate | construction/reference/bridge/witness trace is insufficient | candidate tracking, question framing, or non-use |
| different entity | the applicable identity or reference rule and the available facts establish that the two descriptions concern distinct entities | keep the established difference; a missing sameness or reuse path alone leaves identity unresolved |

When a sameness, difference, or reuse claim needs mathematical justification, use the defining mathematical rule; use C.29 only for an actual lens. E.18 and E.18.1 govern their transformation-flow and problem-to-work carry-through claims, and E.18 applies when a gate crossing is the live relation. A structural, graph, flow, or architecture-description comparison uses its relevant architecture pattern. If no rule supplies the needed identity, correspondence, or postulate-theory justification, leave that claim unresolved.

#### A.7:5.8b - Compact relation-position recovery aid

When one visible source-side carrier, publication face, diagram, dashboard, card, model output, `PublicationUnit`, rendering, or generated artifact can be read as several FPF values at once, use A.7 only to recover the current relation position. Name the current `EntityOfConcern`, Description episteme, view, publication face, publication form, `PublicationUnit`, carrier, rendering, mathematical-lens use, evidence relation, gate decision, work occurrence, authority-reference relation, source-currentness relation, or source-use claim, then apply the subject pattern for that position.

This aid is not a reusable object, local record, table, or master checklist. If the direct governed claim is already clear, do not add an A.7 recovery note; cite the direct pattern.

#### A.7:5.9 - Direct Description account and specification-use boundary (normative)

A.7 uses no `Describe_EoC_DescEp` function. To say that one episteme describes something:

1. identify the Description episteme through its complete C.2.1 claim content, exact `EntityOfConcern`, and effective `ReferenceScheme`;
2. state the claims it makes about that EntityOfConcern in ordinary language;
3. when the receiving use asks how those claims arose or are carried, name the exact authoring, measurement, observation, model, source-use, representation, refinement, or other direct relation and its participants; and
4. keep any publication occurrence, form, face, carrier, evidence use, Work, or specification-use gate separate.

If the EntityOfConcern is itself an episteme, the new Description does not automatically copy, preserve, refine, or extend its claims. Any representation, source-use, comparison, refinement, or loss claim needs its own direct rule. If the EntityOfConcern is a system, structure, Method, Work occurrence, physical object, characteristic, relation, or other non-episteme, claims are likewise not “inside” it waiting to be copied; the actual measurement, observation, model, postulate, authoring, or other relation explains the claim when that explanation is current.

**Example.** `PumpPerformanceDescription-e4` is a C.2.1 episteme whose EntityOfConcern is pump P-12 and whose claims state the measured flow and pressure under the named scheme. `MeasurementRun-88 produced ObservationEpisteme-88`, and that observation supports the stated measurement claim through its direct evidence-use relation. The Description, pump, measurement Work, observation episteme, evidence use, and publication carrier remain different objects. No universal constructor is needed.

A Description episteme becomes usable as a specification when its C.2.1 constitution, checkable claims, and a named harness, validation, conformance, measurement, or evaluation relation capable of checking them for the stated use are recoverable under E.10.D2 and the applicable direct pattern. When viewpoint selection affects reliance, preserve or explicitly update the named describing use and its selected viewpoint. Formality, acceptance conditions, measurement criteria, and verification practice contribute under their own rules; formal notation alone is insufficient. Specification use remains separate from the EntityOfConcern, Description identity, publication expression, and Work.

A Description episteme, its specification-use status, and a publication result are distinct from the dated activity that produces them. An actual describing, formalizing, specifying, or publishing activity may be admitted separately as Work. Use `Gamma_method` for the composition of its Method, `Gamma_time` for Work histories and temporal parts, and `Gamma_work` for resource spend and yields tied to that Work. An ordinary statement about authoring needs those relations only when its claim uses them.

#### A.7:5.10 - Outcome specification strict distinction

A.7 supplies only the distinction. The authoritative promise-facing `OutcomeSpec` shape is in A.2.3:4.1.1, and the authoritative unit-of-delivery counting rule is in A.2.3:4.1.2.

An `OutcomeSpec` is a specification-use episteme form, not a new U-kind, a Work occurrence, an affected entity, a post-work state, an operation-result binding, or a verdict episteme. Its mode says which facts the promise constrains:

* `WorkOnly` constrains selected facts about one or more delivery Work occurrences;
* `ResultOnly` constrains the exact affected referent and required post-work state, regardless of method; and
* `Composite` constrains both.

**Readable example.** `The provider cuts and styles the client's hair within 20 minutes, and the resulting hairstyle meets the stated evening-style condition.` The first clause constrains delivery Work and may name the exact Method. The second constrains the client's post-work hairstyle state. Exact affected-referent, actual-change, production, delivery, acceptance, and evidence-use relations are stated only when the receiving claim needs them. No `U.Work.Delta` field or universal delta record is required; an optional mathematical change expression remains a separate lens when a named comparison uses it.

Evidence supports assertions about the selected Work facts, affected referent, post-work state, and direct relations. Evidence and its carrier do not become any of those facts. Counting is also separate: A.2.3's `unitOfDelivery` says how accepted delivery is counted and how double counting is prevented; it is not part of `OutcomeSpec`.

### A.7:6 - Worked cases

#### A.7:6.1 - System and episteme

**Digital twin and asset.** In this example, `Twin-e4` is a C.2.1 description episteme about the asset. `Maintenance system M updated the asset configuration using Twin-e4.` This ordinary sentence keeps the acting System, asset, and episteme visible. If the receiving claim concerns exact Work, carrier change, evidence, source currentness, or an assignment, add those objects and direct relations separately. Twin-e4 supplies the representation used by M; the updating action belongs to M. A cross-plane use cites only its applicable plane relation and policy.

**Review and manuscript.** `Reviewer Dana reviewed Manuscript-e7 and wrote Review-e2.` This is valid ordinary actor wording when Dana is a recoverable System and no inference uses assignment identity. `PeerReviewGuide-e2` is a MethodDescription only if its exact EntityOfConcern is the PeerReview Method and its claims say substantively how that Method is performed. For a precise audit, use A.13 to identify the review performer and A.15.1 to admit the review Work independently. Add F.6 only if the audit must also identify the assignment under which that Work was performed. Keep the resulting review episteme, manuscript and review carriers, and evidence or source relations separate.

#### A.7:6.2 - Progressive technical examples

**Pump in a cooling loop.** `Pump P-12 circulated coolant during the 10:00-10:45 run.` If that sentence remains ordinary actor wording, no full performance record is required. For a precise Work claim, recover the actual performer and its A.13 core, then use A.15.1 to admit the dated run independently with at least one Method actually followed, the interval, and an obtaining containing-System relation. That core includes an obtaining assignment, here `CoolingLoopCirculationAssignment-17`, its admitted species, holder and assigned-kind participants. Add F.6 only if the claim must also identify the assignment under which the run was performed. Add Capability and another Method only for their own claims; none follows merely from the noun *pump*.

**Standard used in a design.** `The design team used Safety Standard S-174 when selecting valve V-12.` The standard is an episteme and does not act. Its PDF and printed volume are carriers; name them when the receiving source or evidence claim uses them. `Valve Selection SOP v5` is a MethodDescription only after the A.3.2 membership test; the ordinary sentence does not require an assignment. A reliance-bearing Work account uses A.13 to identify the actual performer and A.15.1 to admit `ValveSelectionWork-47` independently. Keep its :2 admission basis, including the core assignment and Method actually followed, recoverable. Add F.6 only if the account must also say under which assignment the Work was performed. Evidence use and current source edition remain separate.

**Set and team.** `{Alice, Bob, 3.14}` is a set and cannot act. `Cooling maintenance team T repaired pump P-12` is ordinary actor wording when T is already recoverable as a collective System. Add its coordination Method, Work occurrence, local system-role kind, or assignment only when the corresponding stronger claim is current.

### A.7:7 - Conformance Checklist (normative)

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Practical test                                                                                                                            |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **CC-A7.1 (System, system-role-kind, and behaviour split)** | A System acts because it satisfies A.1. A local system-role kind classifies it; an assignment occurrence relates it to that kind only when the direct assignment predicate obtains. Method, Capability, Work, transformation, kind, and assignment keep their separate meanings. | Accept ordinary actor wording when the System and contribution are recoverable; add classification, assignment, Capability, Method, or Work only for the stronger current claim. |
| **CC‑A7.2 (Transformer-system-role assignment domain)** | A suffixed source designation such as `TransformerSystemRole@ValveSelectionContext` is only a locator. The exact kind must first be recovered through its C.3 candidate domain, membership distinction, boundary probes, and continuity rule; the suffix identifies none of them. A direct `U.SystemRoleAssignment` species must then admit that kind in its declaration-local kind slot and systems in its holder slot. | Type-check the exact species, holder, kind domain, predicate, applicability, and occurrence identity; do not filter a permissive family value by a role label. |
| **CC-A7.3 (Episteme non-agency)** | An episteme does not act or hold a work-facing assignment. A System may author, revise, use, or publish it. | The ordinary sentence names the acting System; add exact Work, carrier, publication, evidence, source, or assignment relations only when the receiving claim uses them. |
| **CC‑A7.4 (MethodDescription ≠ Method ≠ Capability ≠ Work)** | **MethodDescription** is the same independently identified C.2.1 episteme only when its exact EntityOfConcern is one admitted Method and at least one substantive way-of-doing claim obtains; **Method**, **Capability**, and **Work** retain their separate meanings. Form, label, design-time status, authoring, revision, citation, publication, approval, or use time grants no membership. | Identify the episteme triple and apply the A.3.2 threshold; then name each current Method, Capability claim and dated Work occurrence separately. |
| **CC‑A7.5 (Operator fit)**               | Use **Γ\_method** only for composing **Method**; **Γ\_time** only for **Work** histories; **Γ\_work** only for resource spend/yields; **Γ\_sys** for systemic properties of systems.                                                                                                           | No sentence should use a single generic “process operator” for all four.                                                                 |
| **CC-A7.6 (Carrier/source-currentness reference)** | An evidence-use claim **SHALL** identify the exact episteme and the claim for which it is used. Cite A.10 carrier/source-currentness refs when the particular evidence, source, or reliance use depends on them. | Recover the episteme and target claim, then the carrier or source-currentness facts required by that use; ordinary citation does not itself assert an evidence-use relation. |
| **CC-A7.7 (Formal inclusion, collection, and collective)** | Mathematical set, tuple, coordinate, and other formal inclusion stays with its defining mathematical rule and creates no world-side relation. Use `C.29` for an actual mathematical lens and `A.19` for the relevant characteristic scale or coordinate. A world-side collection uses its own identity and belongs-to rule. A grouping claimed to act must separately pass all six `A.1` matters. | Check the distinct formal, collection, and collective-System claims. Infer neither belonging from formal inclusion nor parthood or holonhood from belonging; do not prohibit a separately grounded constructive part claim. |
| **CC‑A7.8 (Diagram legend)** | Domain “process” or “behaviour” keeps its recovered meaning under the direct rule for that claim. Use the exact Γ operator for a composition claim, and disambiguate an unclear domain use explicitly. | A clear domain sentence may stand; an ambiguous one identifies its actual object and predicate without forcing a Method/Work binary. |
| **CC-A7.9 (Progressive actor wording)** | A contribution noun may stand for a recoverable System in ordinary prose. An assignment, local system-role kind, Capability, Method, or Work is added only when that exact distinction changes a receiving inference. | `The engineer designed the pump` may stand. For a precise Work claim, recover the A.13 core and A.15.1 admission basis stated in :2, including the core assignment and at least one Method actually followed. Add F.6 only if the receiving use must also identify the assignment under which that Work was performed. |
| **CC-A7.10 (Work-facing chain clarity)** | A diagram shows only the positions used by its claim. MethodDescription membership, Capability, assignment, Work, and evidence are not inferred from a complete-looking chain. | Begin with the acting System and direct claim; expand the chain only for a named design, attribution, or reliance use. |
| **CC-A7.11 (Terminology hygiene)** | Avoid bare `actor` when the acting subject is known. Name the System directly or use a recognizable contribution noun. | Assignment identity is required only when a work-facing assignment claim is current; ordinary actor wording does not create one. |
| **CC‑A7.12 (System-role domain guards)** | Work-facing assignment species declare `HolderSystemSlot` for systems or acting holons and a local system-role-kind domain for `AssignedSystemRoleKindSlot`. Epistemes may be used through reference-use, constraint-source-use, evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, or gate-use relations, but those uses create neither a system-role kind nor an assignment. | Each assignment names its occurrence and declared species. The species defines participant meanings, predicate, applicability, and occurrence identity; the occurrence supplies holder, assigned kind, case applicability, and extent. Episteme uses name the relation. |
| **CC-A7.13 (EntityOfConcern and Description visibility)** | Each Description episteme is independently identified by complete claim content, exact EntityOfConcern, and effective ReferenceScheme. A.7 supplies no universal describing constructor. | Text or diagram keeps the EntityOfConcern and Description episteme visible and states any current authoring, measurement, observation, model, source-use, representation, or refinement relation separately. |
| **CC-A7.14 (Description-source discipline)** | A Description about an episteme does not automatically copy or preserve its claims; a Description about a non-episteme does not extract claims from the subject. | Name the exact source-use, representation, refinement, measurement, observation, model, authoring, or other relation that warrants the claim when that explanation is current. |
| **CC-A7.15 (Specification-use boundary)** | When text claims specification force for a specification, formal specification, requirement, acceptance item, harnessed invariant, or measurement-criterion object, it retains the independently constituted Description episteme, checkable claims, and a named harness, validation, conformance, measurement, or evaluation relation capable of checking those claims for the stated use. Preserve or explicitly update the named describing use and selected viewpoint when they affect reliance. C.2.3 formality, A.21 gate or acceptance discipline, C.16 measurement criteria, A.6.2 refinement, and other direct patterns may contribute under their own conditions. E.17 expresses an already admitted specification use; E.10 governs its suffix. Neither publication, suffix, nor formal notation substitutes for the admission conjunction. | Recover the episteme, claims and capable checking relation for the stated use, plus any reliance-relevant viewpoint selection. Specification remains a use of the Description episteme, not a peer ontology class. |
| **CC-A7.16 (Gamma separation)** | A Description episteme, its specification-use status, and a publication result do not carry the cost or time actuals of the activity producing them. | Recover any separately admitted describing, formalizing, specifying, or publishing Work; keep Method composition, Work histories and temporal parts, and Work resource relations distinct. |
| **CC‑A7.17 (Publication face and form discipline)**     | Publication names use the current publication face, form, unit, carrier, and rendering vocabulary. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are faces over epistemes or views; new `...PublicationFace` or `...PublicationForm` heads are not introduced as A.7 kinds in this ontology.                                                 | Token scan shows no ad‑hoc `...PublicationFace` or `...PublicationForm` kinds.                                                       |
| **CC‑A7.18 (Semantic and plane crossings).** | A face relying on an obtaining F.9 Bridge cites its two exact F.17 local senses, that Bridge, and a separate bounded-use claim; `CL` is optional. Other semantic relations use their own predicates and participants. Cross-plane content cites the applicable plane relation. Context or plane difference alone creates no Bridge, `CL`, or penalty; any trust penalty cites the named current policy and its applicability to this use. | Audit resolves the exact semantic or plane relation and any current policy application without inferring one from labels, contexts, planes, cards, or `CL`. |
| **CC-A7.19 (UTS row reference)** | When a selected durable naming settlement and the receiving use require an F.17 term row, public names shown on faces **SHALL** point to that UTS row with twin labels (Tech/Plain), edition pins, and carrier/source-currentness refs when the source or evidence use depends on them. | If the row is needed, recover its identifier, labels, edition pins, and applicable source/evidence refs. Otherwise keep the sufficiently defined local designation; publication alone requires no row. |
| **CC-A7.20 (Direct Method reference)** | An identifier's designation of one exact Method under an effective ReferenceScheme and a receiving claim's resolved `methodRef` remain separate from `U.MethodDescription` membership. Neither requires a description hop; `methodDescriptionRef` is optional and edition-specific only when the receiving claim uses that episteme's claims. | Resolve the identifier and receiving reference directly to the Method, then apply A.3.2 independently only for an actually cited description episteme. |

### A.7:8 - Canonical rewrites (didactic library)

The middle column stipulates facts for each teaching case, including its named System, Method, classification, object, or occurrence; these facts are not recovered from the short quotation in the first column. In a real repair, establish the needed facts before using the corresponding rewrite. Keep an ordinary deployed-System metonymy when that is the recoverable intended reading, and do not invent an actor, Method, classification, or assignment to complete a chain.

| Source wording | Start with | Add only for the stronger claim |
| --- | --- | --- |
| “The process enforced the rule.” | `Control system CS-4 enforced Rule R during Run 12.` | If dated Work is current, recover the actual performer and its A.13 core, then admit the occurrence independently through A.15.1 with the :2 basis, including at least one Method actually followed. If the account must also identify the assignment under which the Work was performed, check it separately through F.6. Add another Method or further evidence detail only when the receiving claim needs it. |
| “The specification decided to tighten limits.” | `Design-control team D changed the limit in Specification-e4.` | The successor episteme, authoring Work, carrier and publication relations when current. The specification never acts. |
| “Our role is pump; the role circulates coolant.” | `Pump P-12 circulates coolant in loop L.` | The local system-role kind for a classification claim; the assignment occurrence only for assignment or attribution; Capability, Method, and Work only for their respective claims. |
| “We followed the blueprint, so it is done.” | `Team T used Method M; completion still requires evidence of the performed Work.` | The blueprint label identifies neither a Method nor a MethodDescription. Cite a MethodDescription only after A.3.2 membership is established and its exact claims are used; keep the blueprint carrier, Work and evidence relations separate. |
| “Team = set of members; it repaired the pump.” | `Team T repaired pump P-12` only after T is recoverable as a collective System under all six `A.1` matters. | State any world-side belongs-to rule separately; add coordination Method, Work, local kind, assignment, or constructive part relation only when that stronger claim is current. |
| “Process cost is tracked by Gamma_method.” | `Work cost is tracked through the applicable work-cost relation; Gamma_method composes the Method.` | Add the actual resource and time relations for the Work occurrence. |
| “Holon has TransformerRole.” | `System S counts under the kind currently named TransformerSystemRole for the ValveSelection use.` | Recover the C.3 kind independently. Add the exact assignment occurrence and species only when an assignment claim is current; the use label is not part of kind identity. |
| “Publication is a special mechanism.” | `Publication makes Description episteme E available through form F on carrier C.` | State the publication occurrence, view or conformance, carrier, and publishing Work under their direct patterns; no universal describing operation is introduced. |

### A.7:9 - Anti‑patterns (with fixes)

1. **System-role-kind-as-behaviour** — calling the **system-role kind** a function or saying it acts.
   **Fix:** Name the acting System and direct behaviour or Work first. Add the local kind, assignment, Method, or Capability only when that stronger claim is current; none of them acts.

2. **Episteme‑as‑system** — “the model routed traffic” when “model” denotes an episteme rather than the deployed acting System.
   **Fix:** Name the System that used the episteme; keep recoverable deployed-System shorthand when that is the intended referent. Add Work, carrier, assignment, evidence, or source details only when the receiving claim uses them.

3. **Triad everywhere** — omitting **Work** entirely.
   **Fix:** Add a Work occurrence only when performed action is claimed; a design-time distinction diagram need not pretend that Work occurred.

4. **Operator blur** — using one “process operator” for everything.
   **Fix:** Choose among **Γ\_method**, **Γ\_time**, **Γ\_work**, **Γ\_sys**.

5. **Formal set, world-side collection, and collective collapse** — mathematical inclusion or collection belonging is used to make a grouping act or to infer constructive parthood.
   **Fix:** Keep formal inclusion with its mathematical or representation rule; state world-side belonging under the collection's own rule; require all six `A.1` matters for a collective System; state any constructive part relation separately.
6. **Unspecified evidence use** — citing content as evidence without identifying the episteme, target claim, or conditions needed for that use.
   **Fix:** Recover the evidence-use relation. Add A.10 carrier/source-currentness refs when that evidence or source use depends on them; a carrier reference alone does not establish support.

7. **Holon/system drift** — “holon maintains temperature”.
   **Fix:** Say **system**; reserve “holon” for neutral mereology.

8. **Function and system-role-kind swap in tables** — columns labelled “Function” whose entries are local system-role kinds.
   **Fix:** Rename the column to **System-role kind**. If behaviour is also being compared, give it a separate column and state the actual behaviour claim under its direct rule, including A.6.F functional behaviour or A.3.4 transformation where applicable.

9. **Process‑word leakage** — domain “process” used as FPF operator.
   **Fix:** Use the exact Γ operator for the composition claim. Keep a clear domain use of “process”; if it is ambiguous, state the actual Method, Work, transformation, mechanism, or other object intended.

10. **Carrier and episteme swap** — “we versioned the model” meaning a file was renamed.
    **Fix:** State whether the **episteme content** changed; if only a carrier was renamed, say so.

11. **Publication-as-mechanism** — modelling “publication” as if it were a Method or Mechanism.
    **Fix:** Identify the Description episteme directly through C.2.1 and keep specification use and publication separate. Name an actual authoring, measurement, observation, model, source-use, representation, or refinement relation only when current; operational build, render, or upload activity is separate Work by a System on carriers.

12. **Form-first MethodDescription** — “this is an SOP/algorithm/script, therefore it is a MethodDescription.”
    **Fix:** Identify the C.2.1 episteme, resolve one admitted Method as its exact EntityOfConcern, and find at least one substantive way-of-doing claim; otherwise retain only the source cue.

13. **Mandatory description hop** — a Method identifier or receiving `methodRef` is forced through a document or description edition.
    **Fix:** Resolve designation and the receiving reference directly to the exact Method under their effective ReferenceScheme discipline; cite `methodDescriptionRef` separately only when its claims are actually used.

14. **Lifecycle time as membership** — authoring, revision, citation, approval, publication, or use is treated as creating MethodDescription membership.
   **Fix:** Keep those Work and neighboring relations under their subject patterns; reapply the same A.3.2 membership test to the independently identified episteme.

### A.7:10 - Consequences

| Benefit                      | Why it matters                                    | Trade‑off / Mitigation                             |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Category safety at scale** | Makes category slips in claims across holarchies easier to recognize and correct. | Slight explicitness; mitigate by keeping ordinary System-and-action wording and adding assignment, kind, Method, Capability, Work, carrier, or evidence detail only when a receiving inference needs it. |
| **Trustworthy evidence**     | Claim-relative evidence use and the applicable A.10 provenance, carrier, and source-currentness relations make the audit basis inspectable. | Requires discipline → provide checklists.          |
| **Operator determinism**     | Correct Γ‑flavour selection preserves invariants. | A bit more modelling → reusable templates.         |
| **On‑ramp for managers**     | Canonical rewrites give immediate phrasing fixes. | Team training → this pattern is the training page. |

#### A.7:10.1 - EntityOfConcern and publication-boundary consequences

| Benefits | Trade‑offs / Mitigations |
|---------|---------------------------|
| **Category-error detection and correction.** Clear separation of System and Episteme, `EntityOfConcern` and Description-episteme boundary, specification use or refinement, and publication availability helps expose recurring modeling defects. | Name publication face, form, unit, carrier, and rendering uses when the distinction matters; E.8 supplies publication-face guidance. |
| **Audit and pedagogy align.** References distinguish the evidence episteme, its target claim, a carrier, and any current source-currentness claim; Normative face houses checklists; Plain face teaches; Tech face types. | Slight increase in pattern length; offset by predictable navigation and machine-checkable CC. |
| **Cross-context and plane safety.** Faces expose an obtaining F.9 Bridge only for two exact local senses and keep its bounded-use claim and optional `CL` separate; cross-plane use exposes its applicable plane relation. | Authors must name only current relations and policies; tooling may assist, but no penalty follows automatically from context, plane, Bridge, or `CL`. |

### A.7:11 - SoTA‑Echoing

* **Digital twins (ISO 23247-1/-2, 2021).** The public previews of [Part 1, §§3.2.2–3.2.5](https://gso-sims-preview-doc-aws.s3-eu-west-1.amazonaws.com/iso-23247-1-2021-en.html) distinguish observable manufacturing elements from synchronized digital representations; [Part 2, §§3.5/5.2.3–5.2.4](https://cdn.standards.iteh.ai/samples/78743/024341895c784ad18c5f6361d5ae074e/ISO-23247-2-2021.pdf) distinguishes implementing and management systems and permits a digital-twin entity to denote a system or systems. **Adapt:** distinguish the representation from its implementing System, and identify the FPF kind from the actual referent.
* **Observability (OpenTelemetry).** [Semantic Conventions 1.44.0](https://opentelemetry.io/docs/specs/semconv/) defines attribute meanings; the [Specification Overview 1.60.0](https://opentelemetry.io/docs/specs/otel/overview/) and [exporter description](https://opentelemetry.io/docs/concepts/components/#exporters) distinguish export components and their data mappings. **Adapt:** keep semantic definitions and transport or representation mappings distinct. Publication-face and publication-form orthogonality is the FPF use of that distinction.
* **Active inference.** In [*Active Inference: A Process Theory* (2017), §§2–2.2](https://discovery.ucl.ac.uk/id/eprint/1530701/1/Friston_Active_Inference_Process_Theory.pdf), Friston, FitzGerald, Rigoli, Schwartenbeck and Pezzulo distinguish a generative model, policies, the generative process, and the action/observation cycle. **Adopt** this historical model/action distinction for A.7's referent recovery; identify the model and acting System under their own FPF rules.
* **Constructor theory.** [Deutsch's *Constructor Theory*, arXiv:1210.7439v2 (17 January 2013), §§1.1/2.14/2.15](https://arxiv.org/abs/1210.7439v2) distinguishes tasks and constructors and also treats information and knowledge as abstract constructors. [Marletto's *Constructor theory of life* (2015), §3.1](https://www.constructortheory.org/wp-content/uploads/2016/03/ct-life.pdf) retains embodied knowledge's constructor role; her [*Constructor Theory of Thermodynamics* (2016)](https://www.constructortheory.org/wp-content/uploads/2016/07/THD-ArXiv-Final.pdf) concerns thermodynamic work and work media. **Adapt** the historical task/realization distinction. A.7 uses that distinction without assigning these source meanings of knowledge or thermodynamic work to `U.Episteme` or `U.Work`.
* **Quality-diversity (MAP-Elites).** In [*Illuminating search spaces by mapping elites* (2015), §3/Fig. 2](https://arxiv.org/pdf/1504.04909), Mouret and Clune describe storing candidate solutions by feature-space cell and retaining the best found for an occupied cell. The returned feature-performance map differs from the run producing it; default parent selection chooses one elite. **Adopt and adapt** this historical archive/execution distinction and collection-valued output example; govern any FPF typed-space or order claim by its own rule.
* **Formal verification and quantities.** [*LiquidHaskell: Experience with Refinement Types in the Real World* (2014)](https://goto.ucsd.edu/~nvazou/real_world_liquid.pdf), by Vazou, Seidel and Jhala, presents logical refinement predicates and contracts. Koenig and Leino's [*Programming Language Features for Refinement*, KRML 248 (2015)](https://leino.science/papers/krml248.pdf), together with the [Dafny Reference Manual's refinement section](https://dafny.org/dafny/DafnyRef/DafnyRef#sec-refinement), describes restricted program refinement. [uom 0.38.0](https://docs.rs/uom/0.38.0/uom/#design) supplies dimension-safe quantities with declared units and conversions. **Adapt** these distinct practices to motivate the specification-use boundary: the claiming specification, formality, refinement, measurement-criterion, and publication patterns govern the applicable check, law, and pins.

### A.7:12 - Rationale (informal)

* **Engineering cognition:** A small, repeatable grammar helps practitioners recognize and correct category slips such as “process vs procedure vs execution”.
* **Compatible with ISO/BORO practice:** Distinguishing reusable ways of doing, claim-bearing description epistemes, system capabilities, and dated operations mirrors established systems-engineering discipline while keeping FPF’s holonic rigor; procedure-like labels remain cues rather than kind evidence.
* **Didactic primacy:** Practitioners start with a readable sentence naming the System, action, subject, or Description. They add assignment, local system-role kind, Method, Capability, WorkPlan, Work, MethodDescription, carrier, source, or evidence relations only when the current claim uses those distinctions.
* **Why name publication faces and forms in A.7?** Strict Distinction already guards the `EntityOfConcern` value from the Description episteme that makes claims about it. In practice, misreadings happen at the publication face: cards and tables are taken as the EntityOfConcern merely because they publish the claims, even when those claims concern another item; governance words leak where physics or logic should stand. Naming publication face, form, unit, carrier, and rendering uses as orthogonal closes that gap without entangling semantics with any tool or notation. Specification use or refinement is also named only to keep it orthogonal to `EntityOfConcern`, Description, and publication expression. This preserves **C-1 universality** and **P-1 Cognitive Elegance**, while giving E.8 a crisp governing source for multi-face presentation rules.

### A.7:13 - Relations

 **Builds on:** A.1 (Holon), A.2 and A.2.1 (system-role kinds and system-role-assignment relations), A.3.1/A.3.2/A.3.4 (Method, MethodDescription, Transformation), A.10 (evidence-provenance, carrier, and source-currentness relations), A.14 (Advanced Mereology), A.15/A.15.1/A.15.2 (System-Role–Method–Work, Work, and WorkPlan Alignment).
* **Constrains:** A.13 (Agency sits on systems only; epistemes non‑behavioural), Part B operators (**Γ_method**/**Γ_time**/**Γ_work**/**Γ_sys**) and their choice points; **publication is not a Γ‑operator**.
* **Extends:** E.8, E.10, Part F and Part G, B.3, and the C-cluster by enforcing the EntityOfConcern/Description boundary, specification-use and publication orthogonality, System/Episteme separation, same or near-same EntityOfConcern discipline across views, and progressive actor wording. Publication remains the separately governed availability of an exact episteme through a form and carrier.
* **Coordinates with:** E.18 for crossing visibility, A.21 for gate checks, E.17 for publication, and E.10 for lexical checks. F.17 identifies exact local senses and F.9 governs an obtaining Bridge between two such senses; a ReferencePlane crossing follows its applicable plane relation. The bounded-use claim, reliance, optional `CL`, and any named policy penalty remain separate.

### A.7:14 - Practitioner one-page review (copy-paste)

**Ordinary repair account**

> `Engineer Dana repaired pump P-12. MaintenanceNote-e4 describes the repair. Carrier C bears publication form F.`

Keep the sentence this short when the receiving use needs no stronger distinction. Contribution nouns such as *engineer*, *reviewer*, *pump*, *team*, or *service* are acceptable when the underlying System and contribution are recoverable and no decision, attribution, admission, or reliance depends on a hidden kind or assignment identity.

**Reliance-bearing expansion, when needed**

> `The practitioner used A.13 to identify System S as the actual performer with its core basis, then used A.15.1 to admit dated Work W independently from its performance history, enacted Method M, temporal extent, and obtaining containing-System relation. If the receiving account must also say under which assignment W was performed, the practitioner uses F.6 to check that relation against the same obtaining assignment A and compare S with A's holder. Keep the required core facts recoverable; add Capability C, another Method, further detail of local system-role kind K, method-description episteme D, carrier P, evidence-use relation R, or resource relations only where the receiving claim relies on them.`

**Six checks**

1. **Acting subject:** Is the acting System recoverable? If assignment identity is not used, do not invent it.
2. **Current distinctions:** Are Method, Capability, Work, assignment, local kind, and MethodDescription named only for claims that actually use them?
3. **Description boundary:** Is each Description episteme independently identified by claim content, EntityOfConcern, and effective scheme, with any authoring, measurement, source-use, representation, or refinement relation stated separately?
4. **Right operator:** `Gamma_method` composes Method; time and resource actuals belong to Work or their direct relations.
5. **Episteme and carrier:** Does the episteme remain non-acting and distinct from its publication form and carrier?
6. **Grouping:** If a group acts, is it recoverable as a collective System rather than merely a set?

**Diagram legend stub**

* `process` in source language may mean Method, Work, transformation, mechanism, or another direct object; recover the live claim.
* A system-role-kind column lists local classifications, not behaviour.
* A behaviour column states the actual behaviour claim under its direct rule; it need not display a full assignment chain.

### A.7:End
