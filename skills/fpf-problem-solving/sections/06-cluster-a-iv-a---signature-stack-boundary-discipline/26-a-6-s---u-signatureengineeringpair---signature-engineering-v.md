## A.6.S - U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Mixed (normative where RFC 2119 keywords appear; quadrant classification is governed by A.6.B)
> **One-liner:** **explicitly modelling signature engineering as a two-signature arrangement** (TargetSignature + ConstructorSignature), with strict separation between **operator description** and **Work performed by admitted Systems**. F.6 identifies the assignment under which each performer acted; a short account may omit an unused assignment identifier.

**E.24.UK settlement.** `U.SignatureEngineeringPair` is retained as a dependent durable arrangement value under the `U.Signature` and A.6 slot-relation settlement, not as a root U-kind. Its identity is the paired TargetSignature and ConstructorSignature relation used to engineer one boundary signature while keeping operator descriptions, enacted Work, publication faces, and system-role assignments separate. A local pair of documents, work procedure, or editing practice does not become `U.SignatureEngineeringPair` unless the two signature epistemes and their constructor relation are named.

**Use this pattern when** a boundary signature is being engineered through a TargetSignature and a ConstructorSignature, and the project must keep operator descriptions, performed Work and its F.6 attribution, publication faces, and proportional reporting of assignment identity separate.

**What goes wrong if missed.** The signature being engineered, the constructor operation description, and the work that enacts publication or edition change collapse into one “contract/editing” story.

**What this buys.** The relation between TargetSignature and ConstructorSignature becomes explicit: constructor operators stay effect-free episteme morphisms, while performed Work and its F.6 attribution, carriers, and publication faces stay with their own direct patterns. Short accounts expose an assignment identifier only when the receiving claim uses it.

### A.6.S:0 - PCP-TERM/LEX token guards (local-first)

This pattern reserves the following tokens in Tech (normative) register:

* **TargetSignature** — the engineered signature episteme (and its editions) under construction and stabilisation (**not** the EntityOfConcern, and **not** the target source or cell of an F.9 relation).
* **ConstructorSignature** — the enabling signature that describes constructor operations for TargetSignature evolution (do **not** mint a second Tech token such as `EnablingSignature`).

Rename-guards (common collisions):

* **enabling** — Plain adjective meaning “producing/maintaining the TargetSignature”; it is not a `U.*` token.
* **constructor** — MUST be disambiguated as one of: `ConstructorSignature` (episteme), `constructor op` (EFEM), or the admitted System that performs the construction Work. State any local system-role classification and obtaining system-role assignment separately. If the physics term is intended, spell **“Constructor Theory”** explicitly.
* **target** — avoid bare “target” in Tech clauses; use `TargetSignature` or qualify the target (for example, “F.9 target cell” or “target holon”).
* **contract** — if source wording uses this Plain shorthand, recover whether it means `TargetSignature`, Contract Bundle, promise content, commitment, or work/evidence. In this pattern the intended recovered value is usually `TargetSignature`; promises, duties, and gates are classified under `A.6.B` and `A.6.C`.

### A.6.S:1 - Problem frame

Boundary descriptions rarely arrive as fully formed signatures. They show up as “half‑signatures”: an n‑ary relation in natural language, a few overloaded markers (“binding”, “anchoring”, “contract”), and implicit assumptions about bases, scope, and viewpoints. Teams then evolve the boundary through incremental edits, reviews, and partial publications.

FPF already provides local disciplines that help unpack such text into well‑formed components: slot discipline (A.6.5) and explicit base declarations (A.6.6). What is usually missing is a *first‑class* description of the signature-engineering boundary that turns half-signatures into stable, publishable boundary-signature descriptions (“contracts” in Plain shorthand; see §0 guards)—an explicit ConstructorSignature for constructing and evolving a TargetSignature.

When signature construction is not explicitly modeled, three failures recur:

1. the TargetSignature and the ConstructorSignature engineering work get conflated;
2. semantic changes happen without being made explicit as retargeting or edition changes;
3. published faces (views) drift into adding semantics, making TargetSignature meaning ambiguous.

Additionally, authors often (implicitly) treat a signature as if it *acts* (“the constructor builds the signature”).
In FPF this is a category error: an Episteme describes; an admitted `U.System` performs Work. A.15.1 admits that Work, and F.6 identifies the assignment under which each performer acted. The assignment does not act. A short explanation may omit an assignment identifier that no later claim uses.
A.6.S therefore must keep **operator descriptions** separate from their **enactment as work**.

### A.6.S:2 - Problem

FPF needs a pattern for **engineering signatures as boundary epistemes**: a disciplined way to construct, revise, and publish a target `U.Signature` from partial input, while maintaining:

* separation between *signature* and *mechanism* (A.6.0 vs A.6.1),
* separation between *laws*, *admissibility*, *deontics*, and *work evidence* (A.6.B),
* explicit multi‑view publication without semantic drift (E.17),
* reproducible evolution across editions without silent mutation.

### A.6.S:3 - Forces

* **Stability vs evolution.** TargetSignatures must be stable enough to coordinate, yet change as understanding improves.
* **Explicitness vs overhead.** Unpacking slots/bases/views increases clarity but also increases authoring effort.
* **Effect‑free operators vs enacted work.** The construction-and-change language should be expressible as effect-free epistemic morphisms (no measurement or actuation), yet applying constructor operations to signature epistemes is still `U.Work` performed by an admitted System and must be auditable. F.6 identifies the assignment under which each performer acted; a short account may omit an unused assignment identifier.

* **Multi‑view richness vs semantic coherence.** Views help stakeholders, but they risk becoming divergent “versions of truth”.
* **Local meaning vs cross-local reuse.** Signature claim content pins its effective ReferenceScheme where interpretation matters. The local kind and any source-local meaning remain separate values; an actual relation between distinct F.17 cells uses F.9 with its declared limits.
* **Contract talk vs ontology.** “Contract” language invites mixing promises, norms, and invariants; FPF requires quadrant discipline.
* **No epistemic agency.** It is tempting to phrase “the ConstructorSignature constructs…”. In FPF, only Systems act; epistemes do not.

### A.6.S:4 - Solution — two signatures and a small constructor vocabulary

#### A.6.S:4.0 - Ontology and effect profile — constructor operators are epistemes; admitted Systems perform the Work

This pattern relies on **Strict Distinction** (A.7), transformation discipline (A.3.4), Method and Work discipline (A.3.1, A.3.2, A.15, A.15.1, A.15.2), and the separate system-role-kind, assignment, and Work-attribution disciplines (A.2, A.2.1, F.6):

* **ConstructorSignature (operator description; EntityOfConcern and Description-episteme boundary).**
  The ConstructorSignature is an **Episteme** (typically a Description/Spec) that *describes* a small family of constructor operations for signature evolution.
  For each constructor-operation family, the ConstructorSignature SHALL state whether it follows the general EFEM rules in A.6.2, the more specific viewing rules in A.6.3, or the retargeting rules in A.6.4. Its declaration states the effect of the episteme-to-episteme morphism on exact claim content, EntityOfConcern, and effective ReferenceScheme and separately names any empirical-grounding relation, representation relation, describing-use viewpoint selection, view-conformance claim, or edition value it consumes.
  As EFEM, constructor ops are **effect‑free** in the strict A.6.2 sense: **no Work, no Mechanism application, and no mutation of systems or carriers**.
  Concretely: an EFEM step *derives* a successor episteme (often a new edition) and its structured delta; the physical act of materialising that successor on carriers (files, repositories, registries, releases, or carrier and source-currentness records) is **Work** performed by an admitted System. Any local system-role classification remains a separate claim. F.6 identifies the assignment under which each performer acted; a short account may omit an assignment identifier that no later claim uses.

  Value-and-relation alignment requirement (C.2.1:7.1 and A.6.5): for each constructor-operation entry, a conforming ConstructorSignature SHALL state which C.2.1 identity values and neighboring relations it reads or changes and whether it follows the general A.6.2 EFEM rules, the A.6.3 viewing rules, or the A.6.4 retargeting rules. SlotKind, ValueKind, and refMode terms are used only for an exact reusable relation declaration and remain local to its `RelationSignature`.

* **Enactor (capability) vs enactment (world-contact).**
  An admitted `U.System` uses a **Method** and performs particular steps as dated **Work** on carriers such as repositories, releases, pins, and carrier and source-currentness references. A MethodDescription is a separate episteme that describes the Method. F.6 identifies the assignment under which each performer acted; neither a local system-role kind nor an assignment acts. A short account may omit an assignment identifier that no later claim uses.
  This is where traces, review records, evidence refs, and publication carriers appear.

Therefore:

* A ConstructorSignature **describes** how a TargetSignature may be constructed/evolved; it MUST NOT be written as if it *performs* the construction.
* Any step that performs measurements, actuation, validation runs, or other side‑effects is **not** an EFEM; model it as `U.Work` or a mechanism, and classify resulting claims with A.6.B.

#### A.6.S:4.1 - Core move: model signature engineering as a separate boundary

In a conforming design, model **two signatures**:

1. **TargetSignature.**
   The `TargetSignature` you want to stabilize. It is a `U.Signature` per A.6.0: direct `SubjectKind` and `RangedValueKind`, optional `ResultKind`, `SliceSet`, and `ExtentRule` when current, together with `Vocabulary`, `Laws`, and `Applicability`. These are components of the TargetSignature episteme, not a nested container. It does **not** contain admissibility gates, deontic obligations, or evidence claims (those are classified by A.6.B).

2. **ConstructorSignature.**
   A *separate* `U.Signature` whose purpose is to describe the **engineering operations** used to construct and evolve the SoI. Intuitively: it is the boundary signature of the enabling activity that produces the target signature.

A.6.S names this pairing discipline **U.SignatureEngineeringPair**: a signature engineering arrangement where a ConstructorSignature is explicitly defined for (at least) one TargetSignature.

Minimal definition (informative): a `U.SignatureEngineeringPair` binds exactly two signature epistemes for one named signature-engineering question and use: a **TargetSignature** (the boundary signature under stabilization) and a **ConstructorSignature** (the enabling signature describing the constructor operations used to build or evolve the TargetSignature). Each signature carries its own effective scheme, criterion, dependencies, and applicability in claim content; the pair stores neither a local kind nor a source-local meaning.

**Terminology note (C.2.1 alignment + twin discipline).**
This pattern uses `TargetSignature` as the **Tech designation** for “the signature episteme under construction and stabilisation”. It is a designation of the signature's place in this arrangement, not a local system-role kind or system-role assignment.
If a publication needs an explanatory Plain label, it MAY use **“signature of interest (SoI)”** as a **Plain twin** for `TargetSignature`, but Plain twins are didactic only and MUST NOT appear in conformance or acceptance clauses.

Do not conflate the **TargetSignature**—the signature episteme being engineered and published—with its exact C.2.1 EntityOfConcern, the boundary or entity that its claims concern.

In C.2.1 terms:
* the TargetSignature is the episteme, and distinct editions remain distinct epistemes under the C.2.1 identity rule;
* its exact EntityOfConcern is the boundary or entity in the world or model that the signature claims concern; and
* if empirical grounding is claimed, an exact `EpistemeEmpiricalGroundingRelation` separately names the covered claims and grounding holon.
If the “SoI” phrasing risks confusion with C.2.1 “entity‑of‑interest” talk, keep it out of Tech/normative prose and use **TargetSignature** vs **ConstructorSignature** consistently.

**Mint-or-Reuse note (informative).**
This pattern introduces the following **Tech names** in the A.6 cluster:
* **TargetSignature** — the target boundary signature episteme being stabilised;
* **ConstructorSignature** — the enabling signature (episteme) describing constructor operations for TargetSignature evolution;
* **U.SignatureEngineeringPair** — the two‑signature arrangement (TargetSignature + ConstructorSignature).

If any Plain twins are used (for example, “signature of interest”), they MUST follow the E.10 and F.* twin discipline: one-to-one correspondence under the effective scheme, registry entry when that public reuse needs one, and no Plain twin in normative register.

The intended shape is:

* TargetSignature is the published boundary signature used by downstream design and realization work.
* ConstructorSignature is the enabling signature used by authors and reviewers to produce and revise the TargetSignature in a disciplined, reproducible way.

This directly operationalises the idea already hinted in the A.6 cluster relations: A.6.5 and A.6.6 can be read as constructor/enabling operations for building well‑formed signatures. The new step is to **bundle those operations into an explicit ConstructorSignature** rather than leaving them as implicit editorial practice.

#### A.6.S:4.2 - Minimal constructor operation vocabulary

A conforming ConstructorSignature **SHALL** (conceptually) expose a *small, composable* set of operations. At minimum, include two groups of constructor operations, drawn from existing A.6 subpatterns:

**(A) Slot‑level constructor operations** (from A.6.5)

Use the canonical slot verbs to express “what changed” without ambiguity:

* `bind` or `rebind` (Identifier → SlotKind/slot‑instance; name binding only)
* `fill`
* `initialize` (first fill)
* `assign`, `set`, `write`, or `update` (subsequent fill; by‑value replacement)
* `retarget` (Ref slot update; same SlotKind/ValueKind)
* `substitute` (typed replacement with explicit compatibility claim)
* `resolve` or `dereference` (Ref → referent)
* `pass` (parameter filling at call boundaries)

**Avoid “mutate” as a generic edit verb.**
In Core, `mutate/modify` denotes **referent‑internal change while the slot‑content (Ref handle) stays the same**.
In edition‑disciplined contexts, prefer “revise, re-edition, and retarget” rather than “mutate”.

Guidance for naming (by slot qualifier) is inherited from A.6.5: e.g., `Edit<SlotQualifier>` for by‑value changes, `Retarget<SlotQualifier>` for ref changes, and avoid collapsing retargeting into generic “editing”.

**(B) Base‑level constructor operations** (from A.6.6)

Make base declarations and their evolution explicit via base‑change verbs such as:

* `declareBase`
* `withdrawBaseDecl`
* `rebase`
* `repointDependent`
* `rescope`
* `retime`
* `refreshWitnesses`
* `changeBaseRelation`

A ConstructorSignature does not need *all* of these in every use, but it must provide enough to express “what changed” when the SoI’s grounding base, scope, or anchoring assumptions shift.

**Witness refresh note.**
`refreshWitnesses` is an **edit of witness references**, not the generation of new evidence: producing/collecting new witness carriers is **Work**; `refreshWitnesses` only updates the base declaration to reference them.

**Optional but common: view construction operations (A.6.3)**

If the TargetSignature is published via MVPK (recommended), include constructor operations that produce views as **EpistemicViewing** (A.6.3) of the TargetSignature:

* “Emit MVPK faces” as views (PlainView, TechCard, InteropCard, AssuranceLane), explicitly treated as views and governed by E.17 “no new semantics”.
  In particular:
  * `PlainView`, `TechCard`, and `InteropCard` MUST add no new claims beyond the underlying TargetSignature or Mechanism claim set.
  * `AssuranceLane` MAY include procedural adjudication guidance and carrier pointers, but any normative pass-or-fail criteria MUST be stated canonically as `E-*` claims and be cited by ID.

These are best modeled as view‑producing operations whose output is an MVPK face, with the explicit constraint that the face is a view and therefore does not introduce new claims about the EntityOfConcern.
Publishing those faces (commits, releases, registry writes) is Work on carriers; it is not “the signature doing things”.

#### A.6.S:4.3 - Change discipline: Viewing vs Retargeting vs editing

To connect signature engineering to A.6.2–A.6.6, treat changes in four buckets:

1. **Viewing (A.6.3).**
   Use when you change *presentation* (views, stakeholder cards, projections) while preserving the EntityOfConcern.

2. **Slot and base construction edits (A.6.5 and A.6.6).**
   Use when you unpack and make explicit what was implicit (slot kinds, ref modes, base declarations), or when you adjust the SoI’s internal structure without changing what it is “about”.

3. **Editioning + reference retargeting (A.6.5).**
   Use when the TargetSignature meaningfully changes and you need a **new SoI edition** for downstream coordination. In that case, do not silently mutate the existing edition: mint a successor edition and **retarget references** (`Retarget<…>` in the relevant Ref slots) to the new edition.

4. **Epistemic retargeting and structural reinterpretation (A.6.4; rarer).**
   Use only when `EntityOfConcernRef` itself changes under an explicit `KindBridge` and stated invariants (e.g., reinterpretation across kinds/planes). This is distinct from ordinary “new version of the same TargetSignature”.

Rule of thumb:

* If the change can be defended as “same TargetSignature, clearer publication”, prefer slot/base construction plus viewing.
* If the change is “new TargetSignature edition for consumers”, require a new edition plus explicit reference retargeting.
* If the change is “different EntityOfConcern or different kind”, use A.6.4 retargeting under `KindBridge` with explicit invariants.

**EFEM discipline.**
Every constructor operation family declared as an EFEM MUST declare `entityOfConcernChangeMode ∈ {preserve, retarget}` (A.6.2).
**Editioning is orthogonal**: you MAY mint a new edition even under `preserve`, but if you do, downstream references MUST be updated explicitly via slot discipline (A.6.5).
Any operation that performs measurements/actuation/side‑effects MUST be modeled as Work or Mechanism application, not as a constructor op.

#### A.6.S:4.4 - Publication and claim discipline for reproducibility

A conforming signature engineering arrangement **SHOULD** include two publication‑adjacent constraints:

1. **MVPK publication for the TargetSignature (E.17).**
   Publish the TargetSignature through MVPK faces as `U.View` projections with viewpoint accountability (`viewRef` + `viewpointRef`). Each face must be explicitly treated as a view and must not introduce new semantic commitments beyond the underlying signature/mechanism claim set (per E.17 “no new semantics”).

2. **Claim Register for boundary discipline (A.6.B).**
   Maintain a claim register that assigns stable identifiers to atomic claims and classifies them into the correct quadrant (L/A/D/E). The engineering benefit is that changes to the SoI can be tracked as changes to specific claims rather than as unstructured prose diffs.

This keeps signature engineering aligned with A.6.B’s separation:

* **Laws** are stated in the SoI (L-claims).
* **Admissibility** and operational gate conditions are governed by mechanisms (A-claims).
* **Deontics** are about agents (D‑claims), not about epistemes.
* **Evidence/work effects** are recorded as outcomes of work (E‑claims), not smuggled into signatures.

#### A.6.S:4.5 - Signature-construction relation in a transformation-flow structure (informative)

If a team represents signature-construction work as an `E.18` `TransformationFlowStructure`, the A.6.S constructor arrangement is referenced from that structure rather than converted into a second graph ontology:

* EFEM constructor operations appear as transformation-flow loci whose governed value is an A.6.2 effect-free episteme-to-episteme morphism over signature epistemes. They remain constructor-operation descriptions, not performed work.
* Concrete carrier writes (commits, releases, registry writes, and carrier and source-currentness pinning) are performed-Work loci or Work occurrences identified with A.15 and A.15.1. Use A.2 for any separate local system-role classification and A.2.1 and F.6 for the assignment under which each performer acted; a short flow account may omit an unused assignment identifier. Use A.10 for evidence and provenance, E.17 for publication, and the relevant carrier patterns for carriers. None of these values is a constructor operation.
* Validation and admission checks are gate/check loci governed by A.21, with `OperationalGate(profile)`, `GateProfile`, `GateCheckRef`, `GateDecision`, and `DecisionLogRef` named when a gate-decision relation is present.
* Any `EntityOfConcernRef` or kind change is a retargeting relation or structural-reinterpretation relation governed by A.6.4, with explicit `KindBridge` plus invariants and witnesses.

This mapping is optional; A.6.S stays usable as a lightweight signature-engineering discipline even when no `E.18` `TransformationFlowStructure` is declared. When it is declared, use E.18 for the flow structure, C.29 for any graph or path representation, and A.6.S for the signature pair and constructor-operation vocabulary.

#### A.6.S:4.6 - State during construction (informative)

Do not mint a new kernel “signature state” unless you need it.
In most cases, use:

* **edition** + explicit continuity/withdrawal links for semantic evolution, and
* a coarse **status** (`Draft`/`Review`/`Stable`/`Deprecated`) for process signalling.

If a project needs a finer state-change policy (for example, “proposed → reviewed → published → frozen”), model it as Work policy in the ConstructorSignature's Applicability or as a separately identified local state-change episteme; keep the TargetSignature semantics unchanged.
Where state-change policy is normative, express it as a status or state-transition policy for the relevant signature episteme or publication under its effective scheme and ClaimScope, with A.2.4 and F.10 status-use discipline and A.6.5 slot discipline where needed. Do not call the episteme's status a system role or create a system-role assignment for it; use E.10.ROLE to route bare *role* wording to the actual status, state, declaration position, or other direct branch.

### A.6.S:5 - Archetypal Grounding — Tell–Show–Show

**Tell.** A TargetSignature becomes stable and evolvable when you model both the *target signature* and the *engineering signature* that constructs it, and you force every change to be expressed as either (a) a view, (b) a disciplined slot/base construction step, or (c) an explicit retargeting to a new edition.

#### A.6.S:5.1 - Show — System archetype

**Working situation.** A payments microservice exposes an external boundary used by multiple client systems.

**Half‑signature input (what arrives).**
“Service binds a `User` to a `PaymentMethod`, anchors charges to the `Ledger`, and guarantees idempotency.”

**Constructed signature epistemes.**

* **TargetSignature:** `PaymentBoundarySignature`

  * **Vocabulary:** operations like `Authorize`, `Charge`, `Refund`; slots made explicit (e.g., `UserRefSlot`, `PaymentMethodRefSlot`, `LedgerEntryRefSlot`).
  * **Laws (examples):** “Charge is idempotent under IdempotencyKey”; “Refund does not increase net balance”.
  * **Applicability:** Payments external API; effective ReferenceScheme and scope are named by the signature edition.

* **ConstructorSignature:** `PaymentSignatureEngineering`

  * Performer System: `PaymentSignatureEngineeringPipeline`, if that team-and-toolchain candidate is admitted as one `U.System` under A.1. It performs the construction Work. State any local system-role classification separately, and use F.6 to identify the assignment under which it acted. A short example may omit the assignment identifier when it is unused.
    It enacts the constructor operations as Work and produces new editions and publication carriers.

  * Slot operations used (as operator descriptions; enacted via Work):

    * `bind/rebind` to bind API field names (e.g., `userId`, `paymentMethodId`) to SlotKinds (`UserRefSlot`, `PaymentMethodRefSlot`) where a language expression exists,
    * `initialize` or `edit<...>` to introduce SlotSpecs and to by‑value edit Vocabulary and Laws in the TargetSignature,
    * `resolve<…>` to disambiguate overloaded prose markers (e.g., “idempotency”) into explicit SlotKinds + laws,
    * `retarget<LedgerRefSlot>` when switching the referenced ledger holon/edition (ref change, not by‑value editing).
  * Base operations used:

    * `declareBase` to ground “Ledger” via an explicit baseRelation and scope,
    * `rescope` when moving from “internal ledger view” to “external client view”,
    * `refreshWitnesses` when decision‑relevant evidence/pins must be updated for continued use.

* **Publication.**
  MVPK faces published as views of the TargetSignature: a PlainView for non‑specialists, a TechCard for implementers, and an InteropCard for integrators, all derived without adding new claims beyond the canonical claim set.

**What A.6.S prevents here.** The phrase “guarantees idempotency” does not silently become a deontic promise or an operational gate. It becomes: (a) an L‑claim (law) in the SoI; (b) if needed, a mechanism‑level admissibility condition for when the guarantee holds; and (c) evidence claims in work logs when validated.

#### A.6.S:5.2 - Show — Episteme archetype

**Working situation.** A research group publishes a signature for a boundary concept used across multiple theories—a common interface between models.

**Half‑signature input.**
“We define correspondence between model A and model B; parameters are anchored to a reference dataset.”

**Constructed signature epistemes.**

* **TargetSignature:** `ModelCorrespondenceSignature`

  * **Vocabulary:** relation `Corresponds(A_model, B_model, Φ_bridge)` with explicit slot kinds and ref/value modes.
  * **Laws:** invariants about correspondence preservation (“observable X is preserved up to tolerance ε”).
  * **Applicability:** the named model-alignment question and use; effective schemes and any actual F.9 relation are stated separately.

* **ConstructorSignature:** `CorrespondenceSignatureEngineering`

  * Performer System: `CorrespondenceSignatureWorkbench`, if the author-and-toolchain candidate is admitted as one `U.System` under A.1. It performs the construction Work; any local system-role classification and obtaining assignment remain separate.

  * Slot operations used: `resolve` to unpack “correspondence” into an explicit bridge slot; `edit<Laws>` (by‑value) to make tolerance explicit; `retarget<ModelRefSlot>` when moving from a draft model edition to a published edition.
* Base operations used: `declareBase` to ground “reference dataset” as an explicit base with scope/time policy; `retime` when updating the reference window.

* **Publication.**
  The SoI is published in multiple viewpoints (e.g., a mathematical view and an engineering view). Differences are handled as views, not as semantic drift.

**What A.6.S prevents here.** “Anchored to a dataset” does not remain a vague metaphor. It becomes a declared base and, when the dataset changes, an explicit base‑change operation rather than a silent reinterpretation.

### A.6.S:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for signature engineering within the A.6 cluster.

* **Architecture bias (Arch):** pushing a two‑signature structure can feel heavy for small boundaries.
  *Mitigation:* keep the ConstructorSignature minimal; reuse A.6.5/A.6.6 verb sets; treat views as optional unless publication demands them.

* **Onto/Epist bias (Onto/Epist):** treating “editing the signature” as harmless can hide semantic change.
  *Mitigation:* use the Viewing vs Retargeting rule; material meaning changes become explicit retargetings.

* **Pragmatic bias (Prag):** increasing discipline may slow down exploratory work.
  *Mitigation:* allow lightweight ConstructorSignatures early, and tighten conformance as assurance requirements rise.

### A.6.S:7 - Conformance Checklist

|             ID | Requirement                                                                                                                                                                                                                                                               | Purpose                                                               |
| -------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **CC‑A.6.S‑1** | A conforming boundary description **SHALL** identify a **TargetSignature** and (when the boundary is being actively constructed or evolved) a **ConstructorSignature** that describes how the TargetSignature is produced and revised.                                     | Prevents conflating the TargetSignature with the ConstructorSignature engineering work. |
| **CC‑A.6.S‑2** | The ConstructorSignature **SHALL** use (or explicitly relate its terms to) the canonical **slot operation verbs** from A.6.5 and the **base-change lexicon** from A.6.6 (`declareBase`, `rebase`, `rescope`, `retime`, …). It **MUST NOT** use umbrella metaphors (for example, `anchor*`) or “bind/binding” as substitutes for explicit baseRelation/base-change talk, and it **MUST NOT** collapse distinct meanings (for example, using “edit” for both by-value updates and ref retargeting). Source- or project-specific shorthands MAY exist, but each has an explicit relation to the canonical verb class and is registered only when the receiving use needs durable reuse. | Keeps change semantics explicit and reviewable. |
| **CC‑A.6.S‑3** | Any TargetSignature change that alters TargetSignature meaning **SHALL** mint a **new TargetSignature edition** and downstream references **SHALL** be updated via explicit **ref retargeting** (A.6.5), not by silent in‑place mutation. Use A.6.4 retargeting only when `EntityOfConcernRef` changes under a `KindBridge`. | Makes semantic evolution explicit without confusing editioning with described‑entity retargeting. |
| **CC‑A.6.S‑4** | If MVPK is used, each published face (`U.View`) **SHALL** be constructed as a **view** of the canonical L/A/D/E-classified claim set and **MUST NOT** introduce new semantic commitments. `AssuranceLane` MAY add procedural adjudication guidance and evidence pointers, but any normative criteria MUST be stated as canonical `E-*` claims and be cited by ID. | Prevents parallel Contract Bundles or rival canonical claim sets emerging from views.                    |
| **CC‑A.6.S‑5** | Claims about laws, admissibility, deontics, and work evidence **SHALL** be classified using A.6.B’s quadrant discipline and (where used) recorded with stable claim IDs in a claim register.                                                                                  | Prevents quadrant mixing in contract prose.                           |
| **CC‑A.6.S‑6** | The TargetSignature **SHALL NOT** contain operational gate predicates or deontic obligations; such constraints belong to mechanisms and agent norms respectively (A.6.1, A.6.B).                                                                                         | Preserves the signature/mechanism boundary.                           |
| **CC-A.6.S-7** | Constructor operations described by the ConstructorSignature SHALL be expressible as effect-free epistemic morphisms (A.6.2). For each EFEM constructor operation family, the ConstructorSignature MUST declare `entityOfConcernChangeMode` and its C.2.1 value-and-relation read/change profile. Any step that performs measurements, actuation, validation runs, or other side effects MUST be modeled as Work or Mechanism application and cannot be a constructor operation. | Prevents smuggling mechanisms or Work into signature editing. |
| **CC‑A.6.S‑8** | Any concrete change to a TargetSignature edition or its MVPK faces **SHALL** be represented as Work performed by an admitted System, with A.10 evidence and E.17 publication relations where current. It **SHALL** satisfy F.6 for every performer; a short boundary account may omit an assignment identifier not used by its receiving claim. Normative text **MUST NOT** ascribe agency to the signature, local system-role kind, or assignment. | Aligns no-epistemic-agency with current System, Work, assignment, evidence, and publication discipline. |

### A.6.S:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern                                    | Symptom                                                                                                   | Why it fails                                                                | How to avoid or repair                                                                       |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **One publication tries to be TargetSignature plus ConstructorSignature work record** | The same publication mixes the TargetSignature, ConstructorSignature construction notes, review notes, and operational gates. | Collapses TargetSignature, ConstructorSignature, and Work evidence; quadrant mixing becomes inevitable. | Split into TargetSignature plus ConstructorSignature; classify gates as mechanism-side admissibility conditions and duties as deontic commitments. |
| **Silent semantic edits**                       | A law or applicability quietly changes; consumers discover it through breakage.                           | Treats a new TargetSignature edition as the same TargetSignature edition.                                 | Require retargeting to a new SoI edition for semantic changes.                              |
| **Retargeting disguised as “editing”**          | Ref changes and by‑value edits are described with the same verb.                                          | Loses the slot discipline stratification and review clarity.                | Use A.6.5 canonical verbs and `Edit<SlotQualifier>` vs `Retarget<SlotQualifier>`.           |
| **Views become “alternative truths”**           | PlainView says one thing, TechCard says another, and nobody knows which is canonical.                     | A view gained semantics rather than projecting them.                        | Treat MVPK faces as viewings; put canonical semantics in the SoI and reference it.          |
| **Contract talk without quadrant discipline**   | “The interface promises…” is used to state invariants, obligations, and entry conditions interchangeably. | Blends laws, deontics, admissibility, and evidence.                         | Use A.6.B claim classes and claim register entries; rewrite claims into the proper quadrant. |
| **Episteme‑as‑actor** | Text says “the ConstructorSignature builds, validates, or publishes the SoI”. | Violates no epistemic agency and hides the admitted System and dated Work; a system-role kind or assignment may also be mistaken for the actor. | Rewrite: the episteme describes constructor operations; an admitted System performs the Work; F.6 identifies the assignment under which it acted. A short account may omit an unused assignment identifier. |

### A.6.S:9 - Consequences

| Benefits                                                                                                                                | Trade-offs and mitigations                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Reproducible signature evolution.** Changes are expressed as explicit constructor operations and, when needed, explicit retargeting.  | **More signatures.** You now maintain TargetSignature and ConstructorSignature. *Mitigation:* keep ConstructorSignature minimal; treat it as a thin change vocabulary early.  |
| **Boundary discipline becomes teachable.** Reviewers can ask “which constructor op happened here?” instead of arguing over prose diffs. | **Upfront cost.** Slot/base unpacking requires attention. *Mitigation:* reuse A.6.5/A.6.6 templates and canonical verbs.                             |
| **Cleaner separation of concerns.** Signatures stay free of gates and obligations; mechanisms and norms stay explicit.                  | **Temptation to over‑formalize.** Some contexts do not need deep formality. *Mitigation:* apply assurance‑appropriate depth; keep views lightweight. |
| **Multi‑view publication stays coherent.** Views are projections, not semantic forks.                                                   | **Discipline enforcement needed.** Without review habits, teams regress. *Mitigation:* make CC items part of boundary review checklists.             |

**Adoption test (informative).** A signature-engineering use is “A.6.S-ready” when reviewers can point, for every TargetSignature change, to (i) the constructor verbs used (A.6.5 and A.6.6), (ii) the EFEM metadata (`entityOfConcernChangeMode` and value-and-relation read/change profile), and (iii) the performer System, dated Work, F.6 attribution, and publication carriers (A.1, A.15, A.15.1, A.2.1, F.6, A.10, E.17). An ordinary short account may omit an assignment identifier not used by its receiving claim.

### A.6.S:10 - Rationale

The two‑signature move mirrors a recurring engineering insight: stable interfaces often require an explicit description of the *enabling* interface that produces and maintains them. Without this, “engineering the TargetSignature” happens implicitly, and the project loses semantic accountability.

A.6.S treats A.6.5 and A.6.6 as *constructor primitives* and makes them explicit in a ConstructorSignature. This yields a compositional change language: reviewers reason about a boundary’s evolution as sequences of named operations, instead of reverse‑engineering intent from prose.

Connecting signature engineering to A.6.2–A.6.4 provides a principled way to separate:

* **Viewing**: change the view, keep the EntityOfConcern.
* **Construction edits**: unpack structure without silently changing meaning.
* **Retargeting**: acknowledge a new TargetSignature edition and make the transition explicit.

Finally, classifying claims through A.6.B makes “contract” talk ontologically safe: laws, gates, norms, and evidence stop competing for the same paragraph.

**SoTA source note (informative).** The separation between an operation signature and its effectful realization is adopted from modern algebraic effects/handlers; the `U.View` and `U.Viewpoint` responsibility discipline is adapted from ISO/IEC/IEEE 42010; and the “preservation under change” intuition is adapted from categorical optics (see A.6.S:11).

### A.6.S:11 - SoTA-Echoing

* **Adopt: algebraic effects and effect systems separate operation signatures from handler semantics.**
  Contemporary effect systems emphasise that an operation signature can be described independently of how effects are handled. A.6.S adopts the same separation at the signature‑engineering level: the SoI remains the conceptual boundary signature, while construction work and operational enforcement are handled elsewhere (mechanisms, realizations, work evidence). This echoes row‑typed algebraic effects and modern handler formulations (Leijen 2017; Hillerström & Lindley 2018).

* **Adapt: categorical optics treat “focus” and “round‑trip laws” as a disciplined interface for bidirectional structure.**
  Optics offer a compact mathematical language for “what is preserved” under a transformation and when updates are coherent. A.6.S adapts this mindset to boundary evolution: viewing corresponds to projection, and retargeting corresponds to an explicit transition with stated preservation claims. Profunctor optics provide a post‑2015 reference point for this style of interface reasoning (Pickering, Gibbons & Wu 2017).

* **Adapt: architecture description standards formalise `U.Viewpoint` and `U.View` responsibility and reduce semantic drift across representations.**
  ISO/IEC/IEEE 42010 treats views as products of viewpoints, with explicit stakeholder concerns and responsibility. A.6.S adapts that discipline to signature publication: MVPK faces are explicit views derived from the SoI, and the ConstructorSignature makes “how we got this view” part of the signature-engineering trace (ISO/IEC/IEEE 42010:2022).

* **Adopt in spirit: behavioural protocol disciplines treat boundaries as typed interaction protocols with safety commitments.**
  Session and behavioural type practice treats boundaries as protocols with progress and safety properties, which matches the A.6 split between signature laws and mechanism entry gates. A.6.S does not import tooling or typechecking, but it adopts the practice of making boundary interactions explicit and law‑governed (e.g., modern MPST practice as cited in A.6.1).

### A.6.S:12 - Relations

* **Depends on:**

  * A.3.1/A.3.2/A.15/A.15.1/A.15.2 — Method, MethodDescription, WorkPlan, Work, and work-result separation
  * A.7 — Strict Distinction (object ≠ description ≠ carrier; Face ≠ Surface)
  * A.6 — Signature Stack & Boundary Discipline
  * A.6.0 — `U.Signature`
  * A.6.2 — `U.EffectFreeEpistemicMorphing` (constructor ops are EFEM species)
  * A.2, A.2.1, and F.6 — local system-role kinds and the assignment under which each System performed the Work; classification, assignment, performer System, and proportional reporting remain separate
  * C.2.1 — episteme identity through claim content, exact EntityOfConcern, and effective ReferenceScheme, with empirical grounding and edition continuity kept as separate direct relations
  * (optional) E.18 — TransformationFlowStructure, when signature-construction work is represented as a transformation-flow structure
  * E.10 and LEX discipline — if the publication uses Plain twins (“SoI”) or shorthands, keep their exact Tech readings recoverable and keep Plain twins out of normative register
  * A.6.3 — `U.EpistemicViewing`
  * A.6.4 — `U.EpistemicRetargeting`
  * A.6.5 — relation-declaration slot discipline
  * A.6.6 — Base Declaration Discipline
  * A.6.B — Boundary Norm Square & Claim Register discipline
  * E.17 and E.17.0 — MVPK and multi‑view describing

* **Strengthens:** A.6.5 and A.6.6 by making their operation vocabularies first‑class as constructor operations.

* **Constrains:** Any signature evolution narrative: semantic changes must be explicit new editions + reference retargeting; publication faces must be viewings.

#### A.6.S:12.1 - Integration pointers (informative)

Grounding pointers in the current FPF draft (for alignment while integrating):

* Canonical pattern template order and section requirements (E.8).
* SoTA‑Echoing requirements and avoidance of data governance/tool binding (E.8:11, E.8:8).
* A.6 cluster explicitly treats A.6.5/A.6.6 as constructor/enabling operations (motivation for A.6.S).
* A.6.2 “effect‑free episteme morphisms” boundary (constructor ops are EFEM; work/mechanisms are separate).
* A.3.1/A.3.2/A.15/A.15.1/A.15.2 method, method-description, work-plan, and work separation for “constructor described vs enacted”.
* A.7 strict distinction and Face/Surface separation (no object–description–carrier soup).
* A.1 System admission, A.2 local system-role classification, A.2.1/F.6 exact system-role-assignment attribution, A.3.4 transformation, and A.15 Work discipline: an admitted System performs Work; epistemes, local kinds, and assignments do not act.
* Slot operation lexicon and naming guidance (A.6.5).
* Base‑change operation lexicon (A.6.6).
* MVPK faces as fixed view kinds with “no new semantics” intent (E.17).
* Claim register and quadrant separation discipline (A.6.B).

### A.6.S:End

