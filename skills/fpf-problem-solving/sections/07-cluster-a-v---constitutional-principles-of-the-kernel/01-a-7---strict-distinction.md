## A.7 - Strict Distinction (Clarity Lattice)
> **Status:** Stable

### A.7:1 - Intent

Provide a **single, didactically clear lattice of distinctions** that keeps models free from category errors. This pattern is the guard‑rail that prevents four recurrent confusions:

1. **Role vs Function** (mask vs behaviour),
2. **MethodDescription vs Method vs Capability vs Work** (description vs abstract way-of-doing vs system ability/envelope vs performed occurrence),
3. **Holon vs System vs Episteme** (what can act and what cannot),
4. **EntityOfConcern vs Description episteme, View, and Publication** (the item under concern vs epistemes and publication relation positions that make it available; specification is a gated use or refinement of a Description episteme, not a third peer member of this distinction).

It harmonizes A.2 and A.2.1 (role values and role-assignment relations), A.3.4 (transformation), A.10 (evidence-provenance and carrier/source-currentness relations), A.14 (Advanced Mereology), A.15 (Role-Method-Work Alignment), C.2.1 (`U.EpistemeSlotRelation`), E.17 (publication and view discipline), and F.9, F.17, and F.18 bridge and naming discipline.

### A.7:2 - Problem frame

* **Holons (A.1) and systems.** All holons are part-whole units; **systems or acting holons** enact behaviour through work-facing role assignments in a bounded context.
* **Transformation (A.3.4) and role assignment (A.2/A.2.1).** Every claimed change names the transformation or work occurrence, the affected entity, and any current `U.RoleAssignment` for the acting system or holon; there is no “self-magic”.
* **Method/work backbone (A.3.1, A.3.2, A.15).** We separate **MethodDescription** (description), **Method** (abstract way-of-doing), **Capability** (a system's ability or envelope to enact a Method under conditions), **WorkPlan** (intent window), and **Work** (run-time occurrence), with the acting side expressed through `U.RoleAssignment` when a work-facing role is current.
* **Evidence (A.10).** Knowledge claims cite evidence-provenance and carrier/source-currentness relations; epistemes never “act”; systems inspect, revise, publish, store, or rely on the carriers, publication forms, and project records that make an episteme available.

Practitioner check: if a sentence could be read as “the document decided” or “the process executed itself”, it violates A.7.

Boundary for use from other patterns: A.7 restores the `EntityOfConcern`, the admissible describing relation, and the publication boundary, then returns the work to the subject pattern. Do not let A.7 turn an architecture, structure, work, method, evidence, characterization, or decision question into a general discussion of descriptions. If the `EntityOfConcern` is itself a Description episteme or view, keep the pattern centered on that episteme as the item under concern; description-of-description or publication-force issues open only when they are the exact claim being made.

### A.7:3 - Problem

When documents blur the above lines, three classes of defects appear:

1. **Category collapse.** People write “function”, “role”, or “process” interchangeably; teams then disagree whether they are changing a MethodDescription, a Method, a Capability envelope, or reporting an actual Work occurrence.
2. **Agency misplacement.** Epistemes (documents, models) are treated as doers; collectives as raw sets; or a “holon” is used where **only a system** makes sense.
3. **Audit failures.** A MethodDescription is cited as if it were evidence; Work has no evidence carriers or time span; or a Description episteme, a Description episteme admitted for specification use, a View, publication face, publication unit, or carrier is treated as if it were the `EntityOfConcern`, decision, permission, gate, work occurrence, or assurance result.

### A.7:4 - Forces

| Force                                        | Tension                                                                                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Didactic brevity vs conceptual precision** | Teams want short words (“process”, “function”) ↔ the framework must keep five distinct distinctions apart.                          |
| **Universality vs domain idioms**            | We admit engineering idioms (procedure, SOP, algorithm, workflow) ↔ internally we must map them unambiguously.                    |
| **Parsimony vs completeness**                | Minimal concept set ↔ enough distinctions to avoid the classic traps (role/function; description/method/capability/work; episteme/carrier). |

### A.7:5 - Solution — The **Clarity Lattice** (normative distinctions & safe vocabulary)

#### A.7:5.1 - **Terminology (normative): orthogonal characteristics**
• **senseFamily** — the categorical characteristic, used by F.7/F.8/F.9: {Role | Status | Measurement | Type‑structure | Method | Execution}. Rows must be **sense‑uniform**.
• **ReferencePlane** — the referent mode per CHR: {world/external | conceptual | epistemic}.
• **EntityOfConcern and Description-episteme boundary** — the item under concern is separated from Description epistemes (E.10.D2, C.2.1). Specification use is a gated use or refinement of a Description episteme; the exact gate must name checkability, formality plus checkable constraint, harness, acceptance condition, C.16 measurement criterion, verification use, or another specification-granting neighbouring pattern. Specification is not a third member of the strict distinction.
• **DesignRunTag** — the design vs run DesignRunTag. It is not a temporal “plane”, generic layer, or stance.
• **Publication face, form, unit, carrier, and rendering boundary** — Description epistemes, including Description epistemes admitted for specification use, may be made available through publication units, publication forms, faces, renderings, and carriers. These publication values are not the `EntityOfConcern` value, not the Description episteme itself, not the specification-use gate or refinement, and not evidence, gate passage, work, assurance, or decision force by readable form. The ordinary didactic faces for architectural patterns in FPF are:
  {**PlainView** (explanatory prose), **TechCard** (typed cards and IDs), **NormsCard** (TechCard profile for checklists), **AssuranceLane** (evidence bindings)}. Publication faces and forms are orthogonal to the `EntityOfConcern` and Description-episteme boundary, to specification-use gates and refinements, and to DesignRunTag.
• **Typed describing morphism and specification-use boundary** — `Describe_EoC_DescEp : EntityOfConcern -> DescriptionEpisteme` describes an `EntityOfConcern` value into a Description episteme under a declared construction/reference trace; it is **not** a mechanism and does not execute work. A later refinement, formalisation, or specification-use claim over that Description episteme is governed by the neighboring pattern governing the claim whose force is live: A.6.2 for effect-free episteme refinement, C.2.3 for formality and checkability, A.21 or the relevant gate/acceptance pattern for harness and acceptance force, C.16 for measurement criteria, E.17 for publication expression, and E.10 for suffix discipline. A.7 keeps those boundaries visible but does not turn them into a second strict-distinction member.
  **Laws (normative for A.7):** (DESC-1) *Non-extensibility of content* and (DESC-2) *identity and meaning-preserving composition*. Specification-use/refinement laws are enforced by the neighboring pattern governing the claim that selects the gate and value set.

• **EntityOfConcern / episteme / publication boundary** — `EntityOfConcern` wording names the item under concern under the declared construction/reference trace; it does not name a document, publication face, carrier, or unspecified referent. `Describe_EoC_DescEp` yields a Description-side `U.Episteme` about that `EntityOfConcern` value. A Description episteme may later be used as a specification only when a bounded use declares formality plus checkable constraint, harness, acceptance condition, C.16 measurement criterion, verification use, or another specification-granting gate. Publication faces, cards, views, publication relation positions, records, and carriers remain orthogonal relation positions: they can make Description epistemes available, but they do not become the EntityOfConcern value, the Description episteme, specification-use gate/refinement, evidence, gate passage, work, assurance, or decision force by appearing in a publication form.

A.7 establishes the following **pairs and triplets**. Use their **names** and **scope** exactly as below.

#### A.7:5.2 - Role vs function-like wording, functional behaviour, capability, method, and work

* **Role (role value).** A context-bound work-facing role value assigned through `U.RoleAssignment` (A.2, A.2.1, A.15). A role value is **not behaviour**; it names the assigned work-facing position under which an acting system or holon may enact behaviour. Example: **CoolingCirculatorRole@Context** in a thermal loop.
* **Function-like wording.** A source phrase such as "function", "behaviour", "service", or "does X" may name a required transformation or effect (A.3.4), functional behaviour (A.6.F), a capability envelope, a method, performed work, a quality, or a structure. Recover the governed claim before choosing the FPF term.
* **Under role assignment.** A system or acting holon under a current `U.RoleAssignment` may have a **Capability** to enact a **Method** under conditions and may perform **Work** that produces, maintains, prevents, or checks a transformation/effect. The role is not the behaviour, Method is not identical to transformation/effect, and Capability is not the Method.

Safe rewrite for earlier "Holonic Duality (Substance vs Function)": **Holonic Duality (Substance vs Role).** A `U.System` keeps its identity while changing assigned role values; each assigned role value may require a Method, a Capability envelope to enact that Method under conditions, and possible Work occurrences.

**Normative guard:** Use **Role** for the role value, `U.RoleAssignment` for the assignment relation, **functional behaviour** when A.6.F governs the behaviour claim, **Method** for the abstract way-of-doing, **Capability** for a system ability/envelope to enact a Method under conditions, **Work** for the performed occurrence, and **Transformation** or effect wording when A.3.4 governs the change claim. Do **not** call the role itself a function, and do not define Method as Capability or as the transformation/effect itself.

#### A.7:5.3 - MethodDescription vs Method vs Capability vs Work (description vs way-of-doing vs ability envelope vs occurrence)

* **MethodDescription** — the **description** (algorithm / SOP / recipe / script) at design-time. Its publication cites A.10 carrier/source-currentness refs when the carrier is used as evidence or source.
* **Method** — the **abstract order-sensitive way-of-doing** composed with **Γ\_method** (B.1.5). A Method is not an occurrence and not the system ability itself; **concrete values** are **bound at `U.Work` creation**. Outside executions we **refer to it via MethodDescription** (see A.3.1 CC‑A3.1‑5/‑9; A.15 §2.2, §4.1).
* **Capability** — the **system ability/envelope** to enact a Method under stated roles, conditions, resources, and constraints. A Capability belongs to a system-in-context; it is not the MethodDescription and not the performed Work.
* **Work** — the **dated run‑time occurrence** (what actually happened), with resource spend (Γ\_work) and temporal coverage (Γ\_time).

**Normative guard:** Never use MethodDescription as evidence of Work; never present Method or Capability as if it had happened; never define Method as Capability.

#### A.7:5.4 - Holon vs System vs Episteme (who can act)

* **System or acting holon** — the entity that can enact behaviour when it is the holder of a current work-facing `U.RoleAssignment`.
* **Episteme** — **cannot act** and does **not** hold work-facing roles; it is changed via carriers, publications, and work on those carriers by systems or acting holons. Reference, constraint-source, evidence, status, source, requirement, publication, and assurance uses are direct relation/use cases, not episteme roles.
* **Holon** — umbrella term; **do not** use it where the current claim requires a system as role-assignment holder. Write the exact holder and `U.RoleAssignment(holderRef, roleRef, boundedContextRef)` when a work-facing role such as `TransformerRole@Context` is current.

**Normative guard:** Work-facing roles, including `TransformerRole@Context` when used, are role values in `U.RoleAssignment` and have a system or acting holon as holder in a bounded context. Epistemes do not hold roles merely because they are used as references, evidence, constraints, sources, requirements, publications, or assurance inputs.

#### A.7:5.5 - Episteme vs publication carrier and source-currentness record

* **Episteme** — the knowledge content (claim, model, requirement set).
* **Publication carrier or source-currentness record** — the physical or digital carrier for an episteme publication or stored representation (file, volume, dataset item), tracked through A.10 carrier/source-currentness relations when evidence, source, or reliance use is current.
* **Use:** Evidence, provenance, and reproducibility address **carriers**; arguments and validity address **epistemes**.

**Normative guard:** When you say “we updated the spec”, detail **which carriers** changed (A.10).

#### A.7:5.6 - Collective vs Set, and MemberOf vs Component/Constituent/Portion/Phase (A.14)

* **Set / Collection (MemberOf)** — **mathematical or catalog** grouping; **no joint behaviour** implied.
* **Collective System** — a **system** with boundary and coordination Method (e.g., a team).
* **Use relations correctly:**

  * **ComponentOf** — mechanical/structural part in systems.
  * **ConstituentOf** — logical/content part in epistemes.
  * **PortionOf** — quantitative portion with conserved extensives.
  * **PhaseOf** — temporal part/state across a continuous identity.
  * **RoleAssignment** — a **system or acting holon** is the holder in a current `U.RoleAssignment`.

**Normative guard:** If the grouping is expected to **act**, model a **collective system** (not a set) and provide its role, Method, and Work.

#### A.7:5.7 - Operator alignment (required names)

* **Γ\_sys** — composition of **system** properties (physical/systemic).
* **Γ\_method** — composition of **Method** (order, branching).
* **Γ\_time** — composition of **Work** histories and temporal parts.
* **Γ\_work** — composition of **resource spend** and yields tied to Work. Do not track costs with Γ\_method; costs (resources/yield) belong to Γ\_work.

**Normative guard:** Avoid generic “process” for these operators. Reserve “process” for domain idioms; map internally to **Method** (design) and **Work** (run).

#### A.7:5.8 - EntityOfConcern and Description-episteme boundary vs publication face, form, unit, and carrier boundary (orthogonal, normative)
* **A.7 and E.10.D2 govern the EntityOfConcern-to-description boundary.** What the `EntityOfConcern` value is and how it is described are distinct questions. Description is a `U.Episteme` use with `DescriptionContext`. Specification is a gated use or refinement of a Description episteme, selected by checkability, formality plus checkable constraint, harness, acceptance, C.16 measurement criterion, verification use, or other neighboring pattern governing the claim force; it is not a peer class beside `EntityOfConcern` and Description.
* **Publication governs availability.** Publication units, publication forms, faces, renderings, and carriers make Description epistemes available to readers or tools, including Description epistemes admitted for specification use. They do not become the `EntityOfConcern` value, the Description episteme, the specification-use gate/refinement, or an evidence/source carrier by the same relation; physical and digital carriers stay in A.10 carrier/source-currentness relations when evidence, source, or reliance use is current.
* **Publication-face field pins.** When Description epistemes or Description epistemes admitted for specification use are shown on **TechCard**, the minimal **CHR-Pins** are {**UnitType**, **ScaleKind**, **ReferencePlane**, **EditionId**}.
* **Bridge policy.** Cross-context or cross-reference-plane reuse cites **Bridge id + CL**; **Phi(CL)** and **Phi_plane** penalties apply to **R (trust)** only; **F and G invariant**.

#### A.7:5.8a - Same or near-same EntityOfConcern across descriptions and views

Different descriptions, views, viewpoints, publication units, or role-method-interest positions may concern the same `EntityOfConcern`, different entities of concern, or an unresolved candidate set. A.7 does not accept sameness by publication title, view label, carrier continuity, shared ordinary name, or common reader interest.

Use this split when the text needs to say whether two descriptions or views are about the same thing:

| Case | A.7 relation case | Admissible move |
| --- | --- | --- |
| same referent by value | the localized `EntityOfConcern` or relation named by value, carried by the current claim, or selected by a reference case and the resolved `entityOfConcernRef`, where live, refer to the same item by declared reference discipline | same-entity work inside the declared use |
| preserved by viewing | A.6.3 viewing preserves `entityOfConcernRef` while changing content, representation, viewpoint, or other episteme slots | same-`EntityOfConcern` Description, Specification, or view transformation |
| publication-unit primary only | a bounded publication unit states what it is mainly about, plus its carried move and outside-work boundary, without establishing a claim-bearing episteme trace by itself | publication-unit stability only |
| bridge-conditional near identity | F.9, F.17, or F.18 admits bounded near-identity or substitution under bridge kind, CL, direction, loss, and bridge-admissible use | bridge-scoped reuse only |
| retargeted under invariant | A.6.4 changes `entityOfConcernRef` under `KindBridge`, invariant, and loss discipline | retargeted use only under stated invariant |
| unresolved candidate | construction/reference/bridge/witness trace is insufficient | candidate tracking, question framing, or non-use |
| different entity | no admissible sameness or near-sameness path exists for the intended use | keep entities distinct |

If the same or near-same relation needs mathematical or postulate-theory justification, A.7 stops at the strict-distinction boundary instead of pretending to prove it: use C.29 for the mathematical lens, E.18 and E.18.1 where transformation-flow, carry-through, and postulate-theory work supply the required justification, E.18 where a gate crossing is the live relation, or the relevant architecture pattern where the comparison is about structure, graph, flow, or architecture description.

#### A.7:5.8b - Compact relation-position recovery aid

When one visible source object, such as a diagram, dashboard, card, model output, `PublicationUnit`, carrier, or generated artifact, can be read as several FPF values at once, use A.7 only to recover the current relation position. Name the current `EntityOfConcern`, Description episteme, view, publication face, publication form, `PublicationUnit`, carrier, rendering, mathematical-lens use, evidence relation, gate decision, work occurrence, authority-reference relation, source-currentness relation, or source-use claim, then apply the direct governing pattern for that position.

This aid is not a reusable object, local record, table, or master checklist. If the direct governed claim is already clear, do not add an A.7 recovery note; cite the direct pattern.

#### A.7:5.9 - Typed describing morphism and specification-use boundary (normative)

**What `Describe_EoC_DescEp` means in A.7.** For any `EntityOfConcern` value `X`, *describing X* is the morphism application `Describe_EoC_DescEp(X) : DescriptionEpisteme`. A.7 does not define a second strict-distinction arrow from Description to Specification. When a Description episteme is formalised, constrained, test-harnessed, accepted, or used as a specification, that is an episteme-refinement or specification-use question handled by A.6.2, C.2.3, A.21, C.16, E.17, E.10, or another neighboring pattern governing the claim according to the live force.

**Example.** A formal postulate theorem in physics can be a Description episteme about the behaviour of a physical grounding holon. Its formal language belongs to formality and publication-expression discipline. It becomes a specification only if a bounded use assigns specification force, such as acceptance criteria, harness checks, normative invariants, or verification use. Formal notation alone does not make it a third kind beside the physical `EntityOfConcern` and the Description episteme.

**Invariants (normative for A.7, split by EntityOfConcern kind):**
1. **Episteme-source preservation (DESC-1E).** When the `EntityOfConcern` value `X` is itself a `U.Episteme`, a claim graph, a claim-bearing view, or another claim-bearing source, `Describe_EoC_DescEp(X)` MUST NOT silently add epistemic commitments. Added structure is only declared representation, indexing, cross-reference, or refinement/loss under the neighboring pattern governing the claim that grants it.
2. **Non-episteme describing trace (DESC-1N).** When `X` is a system, structure, work occurrence, role assignment, method, physical object, characteristic, relation, or other non-episteme value, claims are not "inside X" waiting to be copied. A Description episteme may add claims about `X` only through a declared construction, reference, measurement, observation, model, postulate-theory, or witness trace, with admissibility conditions visible for the intended use.
3. **Identity and meaning preservation (DESC-2).** If `f : X -> Y` is a meaning-preserving, bridge-admitted, or construction-preserving map for the selected EntityOfConcern values, then `Describe_EoC_DescEp(f)` is defined only for the declared scope and preserves the identity, near-identity, bridge, loss, or retargeting relation that the governing pattern admits. Where meaningful composition exists, `Describe_EoC_DescEp(f o g) = Describe_EoC_DescEp(f) o Describe_EoC_DescEp(g)` only under that declared relation.
4. **Specification-use refinement case.** If a Description episteme is refined into specification use, the refinement must name the neighboring pattern governing the claim and gate that grants that use. A.7 only requires that the refinement remains separate from the `EntityOfConcern`, from publication expression, and from Work.
5. **Separation from Gamma.** `Describe_EoC_DescEp` and any neighbouring specification-use refinement do **not** compose with **Gamma_method**, **Gamma_time**, or **Gamma_work**; describing, formalising, or specifying is not execution and accrues no resource or time semantics.
6. **Ontology preservation.** Describing any `EntityOfConcern` value, such as a Calculus, Signature, Mechanism, Structure, Work occurrence, or Episteme, via `Describe_EoC_DescEp` does **not** change its ontology; it yields a Description episteme under A.7 rules. Publication through faces, forms, units, and carriers is handled separately in E.17 (MVPK).

#### A.7:5.10 - Bridge to `U.Work` (normative invariants)

**OUTSPEC‑INV‑1 (No metonymy).**
`promisedOutcomeSpecRef` points to an **OutcomeSpec**, not to `U.Work` and not to an extensional delivered-result referent. The *actuals* live on `U.Work` (A.15.1) and its evidence carriers.

**OUTSPEC‑INV‑2 (Evaluability from work evidence).**
All predicates referenced by `workPredicateRef`, `postConditionRef`, and `unitOfDelivery.countingRule.*` MUST be evaluable from `U.Work` facts and cited evidence (including `U.Work.Δ` state records or evidence carriers). They MUST NOT require introspecting the internal structure of the provider system unless that structure is itself exposed as evidence.

**OUTSPEC‑INV‑3 (Counting coherence).**
If `unitOfDelivery` is present, its countingRule MUST select only work episodes that are eligible to satisfy the promise content and MUST not silently double‑count (use `dedupeKeyRef` or a cited policy).

##### A.7:5.10.1 - Canonical examples (didactic)

**Example 1 — Work‑only (promise the work): “provide consultation for ≥5 minutes”.**

```text
OutcomeSpec(OS‑Consult‑5min) := {
  mode: WorkOnly,
  workSpec: {
    methodConstraintRef?: MD‑Consultation,
    workPredicateRef: E‑(duration(work) ≥ 5 minutes)
  }
}

unitOfDelivery := {
  unitLabel: "minute",
  countingRule: {
    selectorRef: E‑(work fulfils OS‑Consult‑5min),
    quantityRef: E‑durationMinutes(work),
    aggregation: sum
  }
}
```

**Example 2 — Result‑only (promise the world state): “a hole of depth ≥ 1 m exists”.**

```text
OutcomeSpec(OS‑Hole‑1m) := {
  mode: ResultOnly,
  resultSpec: {
    deliveredResultReferentRef: kind(Hole),
    statePlaneRef: GeometryPlane,
    postConditionRef: E‑(depth(hole) ≥ 1 m ∧ location(hole) within SiteScope)
  }
}

unitOfDelivery := {
  unitLabel: "hole",
  countingRule: {
    selectorRef: E‑(work fulfils OS‑Hole‑1m),
    quantityRef: E‑1,
    aggregation: count,
    dedupeKeyRef: E‑holeId(work)         // prevents double counting when rework happens
  }
}
```

**Example 3 — Composite (promise both): “hairstyle for the evening, produced within 20 minutes, by cut+style (not a wig)”.**

```text
OutcomeSpec(OS‑Hair‑Evening‑20min) := {
  mode: Composite,
  workSpec: {
    methodConstraintRef: MD‑CutAndStyle‑NoWig,
    workPredicateRef: E‑(duration(work) ≤ 20 minutes)
  },
  resultSpec: {
    deliveredResultReferentRef: kind(HairstyleOnClient),
    statePlaneRef: AppearancePlane,
    postConditionRef: E‑(looksLike(style="Evening") ∧ survivability(afterShower) ≥ acceptable)
  }
}

unitOfDelivery := {
  unitLabel: "session",
  countingRule: {
    selectorRef: E‑(work fulfils OS‑Hair‑Evening‑20min),
    quantityRef: E‑1,
    aggregation: count,
    dedupeKeyRef: E‑appointmentId(work)
  }
}
```

(Where `E‑(…)` denotes an Episteme/predicate defined in the relevant Context; this appendix does not introduce an expression language.)

### A.7:6 - Archetypal Grounding (Tell-Show-Show; System and Episteme)

#### A.7:6.1 - System and Episteme example
**System archetype — “Digital‑twin vs asset”.**
*Claim:* *The twin (episteme) does not “act”; the system or acting holon under a current `U.RoleAssignment` enacts Work on the asset; evidence binds through A.10 carrier/source-currentness and evidence-provenance relations.*
*Show:* A maintenance **MethodDescription** (tech card) lives at design‑time; a **Work** record (assurance face) lists Γ_time, Γ_work, PathId and **carrier** ids for telemetry. The twin’s update is **Work on the carrier**, not the asset; CL^plane penalties are disclosed when twin–asset crossings are analysed.

**Episteme archetype — “Peer‑review vs manuscript”.**
*Claim:* *A review is Work by a **system** (the reviewer) **on carriers** of an episteme (the manuscript).*
*Show:* The **MethodDescription** is the review SOP; the **Work** cites carrier ids (file/edition) and the selected episteme; arguments/rebuttals live on epistemes; acceptance gating lives in CAL, not in CHR cards.

#### A.7:6.2 - Didactic examples

**Example 1 — Pump in a cooling loop**

* **Substance (system):** Centrifugal pump P‑12.
* **Role:** **Cooling‑CirculatorRole**.
* **MethodDescription:** “Loop Circulation v3” (**TechCard**, cited through A.10 carrier/source-currentness refs when evidence or source use is current).
* **Method:** ordered way-of-doing: start → ramp → hold → stop (Γ\_method).
* **Capability:** P-12 control-unit ability/envelope to enact that Method under stated roles, conditions, resources, and constraints.
* **Work:** run on 2025‑08‑09 10:00–10:45; energy ledger via Γ\_work; log via Γ\_time.
* **Safe phrasing:** *“The **system** playing **Cooling‑CirculatorRole** (via the P‑12 control unit as **Transformer**) had the **Capability** to enact the **Method** described by **MethodDescription**, and executed **Work** …”*
* **What not to write:** “The pump’s function is the role” (role ≠ behaviour).

**Example 2 — Standard document cited in a design**

* **Episteme:** “Safety Standard S‑174”.
* **Carriers:** PDF and printed volume with A.10 carrier/source-currentness refs when the standard is used as source or evidence.
* **Use relation:** reference-use or constraint-source-use relation for the valve selection activity, named by its direct governing pattern.
* **Role assignment for work:** `U.RoleAssignment(holderRef=DesignTeamSelectionSystem, roleRef=TransformerRole@ValveSelectionContext, boundedContextRef=ValveSelectionContext)` when the selection work needs a work-facing transformer role value.
* **MethodDescription:** “Valve Selection SOP v5”.
* **Method:** abstract valve-selection way-of-doing described by that SOP.
* **Capability:** design team's selection-service ability/envelope to enact the Method under the project conditions.
* **Work:** dated selection session that **used** the standard; the episteme did **not** act.

**Example 3 — Set vs team**

* **Set (MemberOf):** {Alice, Bob, 3.14} — a collection; **no behaviour** implied.
* **Collective system (team):** boundary, coordination **Method**, supervision **Work**; can hold a current `U.RoleAssignment` for a work-facing role value such as `CoolingMaintenanceRole@Context`.
* **Safe phrasing:** *“`U.RoleAssignment(holderRef=TeamT, roleRef=CoolingMaintenanceRole@Context, boundedContextRef=ContextT)` is current for Work W…”*

### A.7:7 - Conformance Checklist (normative)

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Practical test                                                                                                                            |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑A7.1 (Role/Behaviour split)**       | A **Role** is a context-bound work-facing role value assigned through `U.RoleAssignment`; **behaviour** must be expressed as **Method** (abstract way-of-doing), with **Capability** as the system ability/envelope to enact that Method under conditions and **Work** as the run-time occurrence. | In any sentence, if “role” is used as if it *does* something, rewrite: the acting system or holon under a current role assignment does the Work by enacting a Method through a Capability. |
| **CC‑A7.2 (Transformer-role assignment domain)** | `TransformerRole@Context` may be used only as a work-facing role value in `U.RoleAssignment` whose holder is a system or acting holon in the bounded context. | Type-check: holder is a system or acting holon; the role value itself is not the acting entity and not an old external-transformer shortcut. |
| **CC‑A7.3 (Episteme non‑agency)**        | An **episteme SHALL NOT** be described as acting or holding work-facing roles. Changes to epistemes are governed through publication, carrier, work, evidence-provenance, and source-currentness relations: work on carriers, publication updates, evidence-provenance relations, and source-currentness records governed by A.10/E.17/A.15. | Text contains the acting system or holon, Work occurrence, and carrier/publication/evidence relation when change or evidence is claimed. |
| **CC‑A7.4 (MethodDescription ≠ Method ≠ Capability ≠ Work)** | **MethodDescription** (description episteme), **Method** (abstract way-of-doing), **Capability** (system ability/envelope to enact a Method under conditions), and **Work** (performed occurrence) **SHALL** be kept distinct in wording and modelling.                                                                                                                                                          | Ask: is there a MethodDescription or design-time publication, a Method, a Capability claim about a system, or a dated occurrence? Each live MethodDescription, Method, Capability claim, and dated Work occurrence must be named separately.                                         |
| **CC‑A7.5 (Operator fit)**               | Use **Γ\_method** only for composing **Method**; **Γ\_time** only for **Work** histories; **Γ\_work** only for resource spend/yields; **Γ\_sys** for systemic properties of systems.                                                                                                           | No sentence should use a single generic “process operator” for all three.                                                                 |
| **CC-A7.6 (Carrier/source-currentness reference)** | Any knowledge claim that references documents or data **SHALL** cite publication carriers or A.10 carrier/source-currentness refs when evidence, source, or reliance use is current. | First mention names the carrier or source-currentness reference and the evidence/source relation made recoverable by that reference. |
| **CC‑A7.7 (Collective vs set)**          | If a grouping is expected to **act**, it **MUST** be modelled as a **collective system** (boundary + coordination Method + Work), not as a **MemberOf** set.                                                                                                                                   | Presence of boundary, Method, Work for the group.                                                                                         |
| **CC‑A7.8 (Diagram legend)**             | When domain idioms use **“process”**, diagrams or text **MUST** map them to FPF terms on first occurrence: *process (domain) ≡ Method at design time or Work at run time.*                                                                                                                           | Legend or parenthetical present at first use.                                                                                             |
| **CC‑A7.9 (Substance ⧧ Role wording)**   | The safe formula is **“System or acting holon is holder in `U.RoleAssignment`; under that assigned role value it has Method/Capability; its execution is Work.”** | Sentences follow this order; “function” used only as synonym for **behaviour**, never for the **role**. |
| **CC-A7.10 (Quartet clarity)**           | Any “triad” picture **MAY** be used only as a **design-time stand-in** (role-assignment holder + MethodDescription + Method) and **MUST** be accompanied by explicit **Capability** and **Work** positions elsewhere in the same section. “quartet of quartets” headings **SHALL** be avoided; use **“work-facing chain”** instead. | Diagram has visible **Capability** and **Work** positions/timeline or separate boxes within the same section. |
| **CC‑A7.11 (Terminology hygiene)**       | Avoid **“actor”** as a bare core term. Use the exact acting system or holon plus `U.RoleAssignment(holderRef, roleRef, boundedContextRef)` when a work-facing role is current. | Plain text scan: no bare “actor” in normative core claims; any local role shorthand is bound through A.2/A.2.1. |
| **CC‑A7.12 (Role domain guards)**        | Work-facing role assignments have systems or acting holons as holders. Epistemes may be used through reference-use, constraint-source-use, evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, or gate-use relations, but those uses are not roles. | Role declarations name holder, role value, bounded context, and window when current; episteme uses name the direct relation. |
| **CC-A7.13 (EntityOfConcern-to-Description visibility)**          | Conforming `EntityOfConcern` and Description-episteme use makes `Describe_EoC_DescEp` recoverable and does not conflate it with MVPK, transformation-flow structure, specification use or refinement, or Work steps. If a flow shows only publication faces and forms, the underlying `EntityOfConcern` and Description episteme are recoverable.       | EntityOfConcern and Description episteme are visible in text and diagrams; audit shows the describing operation and its construction/reference trace.                                                             |
| **CC-A7.14 (Describe_EoC_DescEp laws)** | Any implementation of `Describe_EoC_DescEp` MUST enforce the split DESC-1E/DESC-1N/DESC-2 law family. Episteme EoCs preserve or refine source claims under declared loss; non-episteme EoCs receive claims only through declared construction/reference/measurement/model/witness traces. Specification-use refinement is checked by the neighboring pattern governing the claim that grants the gate, not by A.7 as a third strict-distinction member. | Audit shows whether the EoC is episteme-like or non-episteme, which trace introduces claims, and which relation preserves identity, near-identity, bridge, loss, or retargeting. |
| **CC-A7.15 (Specification-use boundary)**         | If text claims that a Description episteme is a specification, formal specification, requirement, acceptance item, harnessed invariant, or measurement-criterion object, it names the exact gate: C.2.3 formality plus checkable constraint, A.21/gate or acceptance discipline, C.16 measurement-criterion discipline, A.6.2 episteme refinement, E.17 publication expression of an already admitted specification use/refinement, E.10 suffix discipline, or another neighboring pattern governing the claim. Formal notation alone is insufficient.                                     | The text shows the specification-granting gate and does not make specification a peer ontology class beside EntityOfConcern and Description.                                                     |
| **CC-A7.16 (Γ-separation)**              | describing morphisms (`Describe_EoC_DescEp`), specification-use refinements, and publication-face or publication-form projections (MVPK) carry no cost/time semantics; **Γ\_method**, Γ\_time and Γ\_work belong to **Method, Work, or System**, not to description, specification-use refinement, or publication. Any aggregate on a card cites the Γ operator and policy.   | No ledger/time fields attached to `Describe_EoC_DescEp`, specification-use refinement, or MVPK publication steps; any “publication cost” is Work in a separate publication service.             |
| **CC‑A7.17 (Publication face and form discipline)**     | Publication names use the current publication face, form, unit, carrier, and rendering vocabulary. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are faces over epistemes or views; new `...PublicationFace` or `...PublicationForm` heads are not introduced as A.7 kinds in this ontology.                                                 | Token scan shows no ad‑hoc `...PublicationFace` or `...PublicationForm` kinds.                                                       |
| **CC‑A7.18 (Bridge+CL on crossings)**    | Any cross‑Context or cross‑plane content on a face **MUST** cite **Bridge id + CL** and **Φ policy‑ids**; penalties apply to **R** only.                                                                         | Presence of Bridge ids and **Φ(CL)** and **Φ_plane** on TechCard or AssuranceLane.                        |
| **CC-A7.19 (UTS row reference)**         | Public names shown on faces **SHALL** point to **UTS rows** with twin labels (Tech/Plain), edition pins, and carrier/source-currentness refs when source or evidence use is current. | Face carries UTS row ids + edition pins plus the current source/evidence refs where needed. |

### A.7:8 - Canonical rewrites (didactic library)

| Instead of (ambiguous)                           | Write (canonical)                                                                                                                               | Why                                                       |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| “The process enforced the rule.”                 | “The acting system under `U.RoleAssignment(..., roleRef=TransformerRole@Context, ...)` executed the **Method**; the **Work** cites evidence carriers ⟨ids⟩.” | Processes don’t act; systems or acting holons do. Evidence uses Work plus A.10 carrier/source-currentness relations. |
| “The specification decided to tighten limits.”   | “The design-control system under a current role assignment updated the **carriers** of the spec, producing **Work** at ⟨time⟩ and recording the A.10/E.17 carrier and publication relations.” | Epistemes are changed via carriers by systems or acting holons. |
| “Our role is pump; the role circulates coolant.” | “`U.RoleAssignment(holderRef=<system>, roleRef=CoolingCirculatorRole@Context, boundedContextRef=<context>)` is current; under this assignment the system has **Method** and **Capability** for coolant circulation; **Work** was executed ⟨when⟩.” | Role value is not behaviour; behaviour is Method/Capability and Work. |
| “We followed the blueprint, so it’s done.”       | “We have a **MethodDescription** and a **Method**; if ability is claimed, name the system **Capability** separately; completion is evidenced by **Work** with ⟨timestamps, outcomes⟩.”                                   | Description, Method, and Capability are not the occurrence.                      |
| “Team = set of members; it performed repair.”    | “The **team** is a **collective system** (boundary + coordination **Method**); it executed **Work** ⟨…⟩.”                                       | Acting groups must be systems, not sets.                  |
| “Process cost is tracked by Γ\_method.”          | “**Work** cost is tracked by **Γ\_work**; **Γ\_method** composes the **Method** (order/branching).”                                             | Operator alignment.                                       |
| “Holon has TransformerRole.”                 | “`U.RoleAssignment(holderRef=<system-or-acting-holon>, roleRef=TransformerRole@Context, boundedContextRef=<context>)`.” | The holder, role value, and bounded context must be explicit. |
| “Publication is a special mechanism.”            | “Publication = availability of existing Description epistemes, including Description epistemes admitted for specification use, through publication units, forms, and faces (MVPK); **describing** is `Describe_EoC_DescEp`, specification use or refinement is governed by the neighboring pattern governing the claiming gate, and any execution around them is separate **Work** by a **system** on **carriers**.” | Publication is not behaviour; it is a Description-episteme-to-publication availability relation in the model. |

### A.7:9 - Anti‑patterns (with fixes)

1. **Role‑as‑behaviour** — calling the **role** “the function”.
   **Fix:** Name the **role**, **Method**, and **Work** explicitly.

2. **Episteme‑as‑system** — “the model routed traffic”.
   **Fix:** Name the **system or acting holon**, its `U.RoleAssignment` when a work-facing role is current, the Work that used the model, and the carriers touched.

3. **Triad everywhere** — omitting **Work** entirely.
   **Fix:** Add the Work position: timestamps, outcomes, Γ_time coverage.

4. **Operator blur** — using one “process operator” for everything.
   **Fix:** Choose among **Γ\_method**, **Γ\_time**, **Γ\_work**, **Γ\_sys**.

5. **Set‑as‑collective** — a MemberOf set “decides”.
   **Fix:** Model a **collective system** with coordination Method.

6. **Evidence without carrier references** — citing ideas without carriers.
   **Fix:** Add A.10 carrier/source-currentness refs and tie claims to evidence or source relations.

7. **Holon/system drift** — “holon maintains temperature”.
   **Fix:** Say **system**; reserve “holon” for neutral mereology.

8. **Function and role swap in tables** — columns labelled “Function” but entries are roles.
   **Fix:** Rename column to **Role**; add a separate **Behaviour (Method and Work)** column.

9. **Process‑word leakage** — domain “process” used as FPF operator.
   **Fix:** Add parenthetical mapping at first use (Method and Work).

10. **Carrier and episteme swap** — “we versioned the model” meaning a file was renamed.
   **Fix:** State whether the **episteme content** changed; if only a carrier was renamed, say so.

11. **Publication-as-mechanism** — modelling “publication” as if it were a Method or Mechanism.
   **Fix:** Separate **describing** (`Describe_EoC_DescEp`), specification-use refinement, and **publication** (MVPK Description-episteme-to-publication face, form, unit, carrier, and rendering availability). If there is operational toil (build, render, upload), model it as **Work** by a **system** on **carriers**; do not change the `EntityOfConcern` value, the Description episteme, specification-use gate/refinement, or the publication relation being presented.

### A.7:10 - Consequences

| Benefit                      | Why it matters                                    | Trade‑off / Mitigation                             |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Category safety at scale** | Prevents silent logic bugs across holarchies.     | Slight verbosity → use local shorthand only after the holder, role value, bounded context, and governing pattern remain recoverable. |
| **Trustworthy evidence**     | Work plus A.10 carrier/source-currentness references make claims auditable. | Requires discipline → provide checklists.          |
| **Operator determinism**     | Correct Γ‑flavour selection preserves invariants. | A bit more modelling → reusable templates.         |
| **On‑ramp for managers**     | Canonical rewrites give immediate phrasing fixes. | Team training → this pattern is the training page. |

#### A.7:10.1 - EntityOfConcern and publication-boundary consequences

| Benefits | Trade‑offs / Mitigations |
|---------|---------------------------|
| **Category-error firewall.** Clear separation of System and Episteme, `EntityOfConcern` and Description-episteme boundary, specification use or refinement, and publication availability removes recurring modeling defects. | Authors must name publication face, form, unit, carrier, and rendering uses explicitly; mitigated by E.8 publication-face guidance. |
| **Audit and pedagogy align.** A.10 carrier/source-currentness refs point to carriers; Normative face houses checklists; Plain face teaches; Tech face types. | Slight increase in pattern length; offset by predictable navigation and machine-checkable CC. |
| **Cross-Context safety.** Bridge+CL discipline is visible on publication faces and forms when they carry cross-context material. | Authors must cite CL policy-ids; tooling can assist (GateCrossing visibility harness), but text remains notation-independent. |

### A.7:11 - SoTA‑Echoing (post‑2015 practice alignment)

* **Digital Twins (ISO 23247, 2021→):** separates the asset (system) from its **digital representation** (episteme) and prescribes governance of twins without attributing *agency* to the twin itself — matching A.7’s “episteme ≠ actor” and carrier discipline. **Adopt.**
* **Observability (OpenTelemetry, 2019-2025):** codifies **semantic conventions** as publication-form discipline over traces, metrics, and logs; semantics are governed by descriptions, not exporters, echoing A.7 publication-face and publication-form orthogonality. **Adapt** (terminology).
* **Active Inference (2017→2024):** separates a **generative model** (episteme) from **actions** by the agent (system), with explicit perception–action cycles — mirroring A.7’s “who can act” and stance separation. **Adopt**
* **Constructor Theory (2016→):** frames knowledge and work as **possible transformations** enacted by constructors (systems), not by informational states — reinforcing “episteme ≠ actor”. **Adopt**
* **Quality‑Diversity (MAP‑Elites family, 2015-2024):** archives are **sets on typed spaces** (descriptions) whose **occurrences** are runs; selection returns **sets** under admissible orders, consonant with A.7 and A.15’s set-returning discipline. **Adopt and adapt**.
* **Refinement-typed specs (2016->):** modern refinement-typed specification toolchains (e.g., Liquid Haskell, Dafny's post-2017 refinements, Rust's `uom` type-level units) treat formalization as **monotonic refinement with pinned units and scales**. A.7 uses them only to motivate the specification-use boundary; the refinement laws belong to the neighboring pattern governing the claiming specification, formality, measurement-criterion, and publication patterns. **Adapt** (terminology; pinning discipline).

### A.7:12 - Rationale (informal)

* **Engineering cognition:** Large programmes fail less from equations than from category slips (“process vs procedure vs execution”). A.7 eliminates these slips by a small, repeatable grammar.
* **Compatible with ISO/BORO practice:** Distinguishing specifications as descriptions, procedures as capabilities, and operations as occurrences mirrors established systems-engineering discipline while keeping FPF’s holonic rigor.
* **Didactic primacy:** Practitioners can approve sentences by spotting the work-facing chain in context: acting system or holon, `U.RoleAssignment`, **MethodDescription**, **Method**, **Capability**, **WorkPlan**, **Work**, and A.10 evidence-provenance or carrier/source-currentness relation where evidence is claimed.
* **Why name publication faces and forms in A.7?** Strict Distinction already guards the `EntityOfConcern` value from the Description episteme that makes claims about it. In practice, misreadings happen at the publication face: cards and tables are mistaken for EntityOfConcern values; governance words leak where physics or logic should stand. Naming publication face, form, unit, carrier, and rendering uses as orthogonal closes that gap without entangling semantics with any tool or notation. Specification use or refinement is also named only to keep it orthogonal to `EntityOfConcern`, Description, and publication expression. This preserves **C-1 universality** and **P-1 Cognitive Elegance**, while giving E.8 a crisp governing source for multi-face presentation rules.

### A.7:13 - Relations

 **Builds on:** A.1 (Holon), A.2 and A.2.1 (role values and role-assignment relations), A.3.1/A.3.2/A.3.4 (Method, MethodDescription, Transformation), A.10 (evidence-provenance and carrier/source-currentness relations), A.14 (Advanced Mereology), A.15/A.15.1/A.15.2 (Role-Method-Work, Work, and WorkPlan Alignment).
* **Constrains:** A.13 (Agency sits on systems only; epistemes non‑behavioural), Part B operators (**Γ_method**/**Γ_time**/**Γ_work**/**Γ_sys**) and their choice points; **publication is not a Γ‑operator**.
* **Extends:** E.8 (Authoring conventions), E.10 (lexical and precision restoration), **Part F and Part G (UTS and CG-Spec or CHR pinning)**, B.3 (assurance-use discipline), C-cluster (selection and archives) by enforcing `EntityOfConcern` and Description-episteme boundary, specification-use boundary, publication availability orthogonality, System and Episteme separation, same or near-same EoC discipline across views, and typed EntityOfConcern-to-Description describing discipline (**publication = Description-episteme-to-publication face, form, unit, carrier, and rendering availability in E.17**).
* **Coordinates with:** **E.18 (gate crossing and OperationalGate(profile))** for crossing visibility and publication gating, **A.21** for gate checks, **F.9, F.17, E.17, and E.18** for Bridge+UTS pinning discipline, **E.10** for lexical SD checks, and **Part F (Bridges and CL)** for explicit cross-Context identity, without embedding any notation dependence.

### A.7:14 - Practitioner one-page review (copy-paste)

**Approval sentence template**

> “`U.RoleAssignment(holderRef=⟨system-or-acting-holon⟩, roleRef=⟨Role@Context⟩, boundedContextRef=⟨Context⟩)` is current for the work; the holder has **Capability** ⟨C⟩ to enact **Method** ⟨M⟩ (from **MethodDescription** ⟨S⟩), executed **Work** ⟨W⟩ on ⟨time⟩, and cites A.10 evidence-provenance or carrier/source-currentness refs ⟨ids⟩; resources are accounted through the governing work-cost relation.”

**Five binary checks**

1. **Bare acting-subject check:** No bare “actor” token in normative core claims; canonical `U.RoleAssignment` phrasing is present when a work-facing role is current.
2. **Clear quartet:** MethodDescription, Method, Capability, and Work are all named (as applicable) and not conflated.
3. **Right Γ:** Γ\_method composes Method; Capability states a system ability/envelope under conditions; Γ\_time covers occurrences; Γ\_work accounts resources; Γ\_sys covers system properties.
4. **Episteme handled:** Epistemes do not act; carriers or source-currentness refs are listed when evidence or source use is current.
5. **Group clarity:** Acting group is a **collective system**, not a MemberOf set.

**Diagram legend stub**

* “process (domain)” ⇒ Method (design‑time) / Work (run‑time).
* Role column lists role values and assignment references (e.g., `CoolingCirculatorRole@Context`).
* Behaviour column shows Method and Work, not the role itself.

### A.7:End

