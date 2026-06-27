## C.2.1 - U.Episteme - Epistemes and their slot relation

> **Type:** Pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly marked informative
> **One-line summary.** `U.Episteme` is the holon type for epistemes; its internal ontology is given by `U.EpistemeSlotRelation`, a typed n-ary relation with `SlotSpec` discipline over `EntityOfConcern`, `GroundingHolon`, `ClaimGraph`, `Viewpoint`, `View`, and `ReferenceScheme`. Under `C.29`, a filled episteme may be represented as a tuple view over that relation; `ClaimGraph` and `JustificationGraph` remain graph-valued fillers or attached graph-valued structures, not tuples. A coarse Symbol-Concept-Object triangle may be used only as a didactic projection of this slot relation, not as the normative ontology.

**Use this pattern when** a theory, model, specification, standard, proof, algorithm, diagram, dashboard, view, or publication is being treated as a knowledge holon and the project must know what it is about, what claim graph it carries, how it is grounded, which viewpoint or view is current, and which reference scheme makes the claims readable.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.Episteme`: a knowledge holon whose identity and admissible use are governed by `U.EpistemeSlotRelation`, not by its carrier, notation, publication face, or one didactic semantic-triangle projection.

**First useful move.** Fill the small episteme slot relation: `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot`, `ViewpointSlot`, and `ViewSlot` when current. Then decide which claim, view, publication, specification-use, morphism, evidence, or grounding relation is actually being used, and keep that relation with its governing pattern.

**What goes wrong if missed.** A PDF, diagram, proof script, algorithm text, model output, or dashboard becomes "the theory"; the described EntityOfConcern drifts; a publication is used as evidence or authority by appearance; and several local description triangles grow into incompatible episteme ontologies.

**What this buys.** The practitioner can keep the episteme, its described object, grounding holon, claim graph, viewpoint, view, reference scheme, carrier, publication, and evidence relation separate while still using one compact slot relation across C.2, A.6.2, A.6.3, A.6.4, E.17, and related description and specification-use patterns.

**Not this pattern when.** Use the direct governing pattern when the current question is the described system or holon (`A.7` and system or holon patterns), a publication face or carrier (`E.17`), evidence or assurance (`A.10`, `G.6`, `B.3`), mathematical-lens use (`C.29`), a method or method description (`A.3.1`, `A.3.2`), or a wording-use repair (`E.10`, `C.2.P`, `C.2.P.DR`, `F.18`, `F.19`). `C.2.1` governs the episteme slot relation itself.

### C.2.1:1 - Problem Frame

FPF’s kernel recognises two archetypal sub‑holons: **System** and **Episteme**. Systems are operational wholes; **epistemes** are **knowledge holons**—theories, models, specifications, standards, algorithms, proofs—whose reason for being is to **say something defeasible or deductive about something** and to be **held to account** by justification.

**Readers.** Engineering managers and lead designers who need a uniform way to reason about **theories, specifications, algorithms, proofs**—from charter memos up to formal axiomatics—without collapsing into tooling or discipline‑specific notations.

KD‑CAL (C.2) needs a precise notion of **what an episteme is** and **how it mediates** between:

* the thing(s) it is about,
* the contexts and systems that ground and test it, and
* the representational machinery (notations, carriers, operations) we use to work with it.

Contemporary work on **formal languages as cognitive tools** (Dutilh Novaes), **operational iconicity** of notations (Krӓmer), **material engagement** (Malafouris), **distributed representations** and **latent-space communication** in ML, and **tool-augmented reasoning** (ReAct-style agent loops) shows that:
* the relation between an episteme and its **EntityOfConcernSlot** is not a single undifferentiated “Object” vertex: it involves explicit **slots and morphisms** (EntityOfConcern-reference mapping, grounding, evaluation) typed by SlotKinds and contexts;
* **representations** come in heterogeneous forms (symbolic, diagrammatic, latent, interactive), with very different **admissible operations**;
* **inference** is often **mixed‑mode**: symbolic reasoning plus calls to tools, solvers, and learned models.

FPF therefore needs a **more modular, slot-relation ontology** for epistemes which:
* keeps **KD-CAL** and the boundary between `EntityOfConcern` and Description episteme plus specification use and refinement discipline intact,
* is compatible with **A.6.0** and **A.6.5** signatures (`SlotKind`, `ValueKind`, and `RefKind`),
* can be used uniformly by A.6.2-A.6.4 (epistemic morphisms) and E.17.* (views & publication),
* preserves real graph-valued structures such as `ClaimGraph` and `JustificationGraph` as values inside or beside the episteme relation, and
* keeps the coarse **semantic triangle** only as a **didactic projection**, not the normative ontology.

In this pattern:
* `U.Episteme` is the **holon genus** for epistemes (C.2), with components and identity governed by A.1, A.6.0, and A.7.
* `U.EpistemeSlotRelation` names the **internal slot relation** of `U.Episteme`: the small, typed n-ary relation over episteme positions (`EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`) on which KD-CAL, A.6.2-A.6.4 and E.17.* rely.
* Species such as `U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication` are holonic realisations of `U.Episteme` whose component structure is constrained to be compatible with `U.EpistemeSlotRelation`.

**Adopted EntityOfConcern family.** C.2.1 uses `EntityOfConcernSlot`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernChangeMode`, and `EntityOfConcernClass` as the adopted slot, ref, and class family. These names are the current C.2.1 vocabulary and must not be shadowed by a second episteme ontology.

### C.2.1:2 - Problem

Without a shared **episteme constitution**, teams fall into recurring failure modes:

1. **EntityOfConcern-Description episteme-publication carrier soup.** Diagrams and files are treated as *the theory itself*. Changes to a PDF are confused with theoretical change.
2. **EntityOfConcern blur.** A spec seems to describe “everything in general”. The **EntityOfConcernSlot** - what exactly this knowledge describes - is implicit and drifts, while the **GroundingHolonSlot** that would say where the claim is grounded is also missing.
3. **Proof vs program confusion.** Algorithms, specifications, and proofs are mixed: a “proof” is used as if it were a tested routine; a “program” is cited as if it entailed a theorem (Curry–Howard misunderstood).
4. **Trust without evidence relation.** Claims accumulate with no explicit **justification graph** or **evidence freshness**, so assurance degrades invisibly.
5. **Category errors at execution.** Epistemes appear as *actors* (“the standard enforces…”) instead of **systems** acting *with* or *on* epistemes such as data sets or algorithms.

The coarse Symbol-Concept-Object semantic triangle is useful only as a didactic projection over the richer slot relation: **Concept** approximates `ClaimGraph`, **Object** approximates `EntityOfConcern` plus `ReferenceScheme`, and **Symbol** approximates notation or representation tokens.

This projection can still help with:
* separating **meaning** (Concept) from **carriers**, and
* integrating KD‑CAL’s **F–G–R** characteristics (Formality, ClaimScope, Reliability).

But the projection has structural blind spots when used as ontology:

1. **No explicit EntityOfConcern slot.**
   The “Object vertex” bundles together *what the episteme is about* with *how we interpret and test it*. There is no explicit **slot** for the entity of concern (`U.Entity`) and no clear separation between:
   * the **EntityOfConcern value**, and
   * the **ReferenceScheme** used to read claims as statements about that thing.

2. **Grounding collapses into Object.**
   Material and organisational contexts (labs, infrastructures, organisations) that **ground** an episteme (in Malafouris' sense) are hidden in the Object and Reference map. KD-CAL and Bridges need explicit **GroundingHolon** positions.

3. **Viewpoints are not first‑class.**
   ISO‑style **viewpoints** (families of stakeholders, concerns, conformance rules) and their induced **views** appear only indirectly, via KD‑CAL or MVPK. There is no explicit `U.Viewpoint` / `U.View` pair at the episteme core, which makes it hard to:

   * connect to **DescriptionContext** for Description epistemes, including Description epistemes admitted for specification use,
   * organize multi‑view descriptions (E.17.0), or
   * align publication viewpoints with engineering viewpoints.

4. **Representations and operations are compressed into “Symbol”.**
   Very different representational regimes are flattened into one Symbol vertex:

   * label-only notations (no internal inference calculus),
   * fully operational calculi (e.g., proof assistants),
   * interactive visualisations,
   * latent vectors and prompt‑programs for LLMs.
     There is no place to say “this representation admits **syntactic inference** of such‑and‑such kind” vs “this is just a **passive label**”.

5. **No explicit signature discipline.**
   The triangle speaks of "Object", "Concept", and "Symbol" but not of **slots** and **references** in the sense of A.6.5 `U.RelationSlotDiscipline`. In episteme this leads to:
   * names where **slot, value and ref** are conflated (`EntityOfConcernRef` used as if it were a slot),
   * ambiguity between the **EntityOfConcern value** (what the episteme describes) and the **episteme** (the description),
   * fragile interoperability with signatures for roles, methods, services.

Thus we have problems of:
* **EntityOfConcern drift.**
 Specifications and models accumulate without a stable notion of **which EntityOfConcernSlot value they carry**; fields like `SubjectRef` carry too many distinct meaning-kinds and resist safe refactoring.
* **Viewpoint confusion.**
  Engineering, publication and governance views are mixed, making it hard to maintain consistency across publication faces and publication forms or to reason about conformity of descriptions under different viewpoints.
* **Representation mismatches.**
  Trade‑offs between neural vs symbolic, diagrammatic vs textual, or interactive vs batch representations cannot be expressed at the episteme level; they leak into ad‑hoc tool descriptions.
* **Broken modularity.**
  As soon as we add KD-CAL, LOG-CAL, MVPK, and E.18, multiple **implicit triangles** appear, each with slightly different semantics, instead of a single shared `U.EpistemeSlotRelation`.

We need a replacement for the triangle that keeps its **didactic clarity** but matches the **slot-relation, graph-valued-claim, and morphism-centric** reality of contemporary epistemic work.

### C.2.1:3 - Forces

| Force                                          | Tension we must resolve                                                                                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Geometry vs. operations**                    | Simple geometric pictures (triangles) are memorable; real epistemic work is **slot-relation disciplined** and often contains real graph-valued claim, evidence, or dependency structures. |
| **Universality vs. representation regimes**    | One ontology must accommodate symbolic calculi, diagrams, DSLs, interactive notebooks, and latent vectors.                             |
| **EntityOfConcern vs. Description episteme and specification use and refinement** | The `EntityOfConcern` value is not the Description episteme produced by this describing, viewing, or morphing use; however, the EntityOfConcern value may itself be a `U.Episteme` when an episteme is the current `EntityOfConcern`. Specification is not a third peer class in C.2.1; it is a gated use or refinement of a Description episteme selected by neighbouring formality plus checkable constraint, harness, acceptance, C.16 measurement criterion, suffix, verification, or publication-expression discipline for an already admitted specification use. |
| **Viewpoint locality vs. reuse**               | Viewpoints should be **local** to families of descriptions, yet we want reusable **viewpoint bundles** across domains (E.17.1 and E.17.2). |
| **Slot discipline vs. usability**              | A clean `SlotKind`/`ValueKind`/`RefKind` discipline is vital for reasoning, but must not render engineering episteme unreadable.             |
| **Stability vs. SoTA evolution**               | The core must remain stable while integrating evolving practices: LLM tool‑use, ReAct‑style loops, structured cospans, optics, etc.    |

### C.2.1:4 - Solution - `U.EpistemeSlotRelation` as the normative episteme ontology

#### C.2.1:4.0 - Overview

For `U.Episteme`, `U.EpistemeSlotRelation` is the normative **small, typed n-ary relation with SlotSpecs** over the core episteme positions. It is not a graph object and not a tuple object. Under `C.29`, the same slot relation may be viewed as a tuple for filled-value reasoning or as a graph or hypergraph diagram for dependency reasoning, but those are mathematical-lens views. Graph-valued fillers such as `U.ClaimGraph` remain real graph-kinds inside the relation.

**Positions and slots.**
  Minimal **kernel SlotKinds** (with their ValueKinds) that every episteme can refer to, following A.6.5:
  * `EntityOfConcernSlot`  (ValueKind `U.Entity` or a declared subkind) -> *"what this episteme is about"*;
  * `GroundingHolonSlot`   (ValueKind `U.Holon`) -> *"where this is grounded and in what holon"*;
  * `ClaimGraphSlot`       (ValueKind `U.ClaimGraph`) -> *"what is being said (claim content)"*;
  * `ReferenceSchemeSlot`  (ValueKind `U.ReferenceScheme`) -> *"how we read claims as statements about entities"*;
  * `ViewpointSlot`        (ValueKind `U.Viewpoint`) -> *"under which viewpoint we read or validate this episteme"*;
  * `ViewSlot`             (ValueKind `U.View`) -> *"a view-episteme produced under a viewpoint"*.

* **Slots and signatures.**
  These positions are realised as **SlotKinds** with associated **ValueKinds** and **RefKinds** under `U.RelationSlotDiscipline` (A.6.5). An **episteme kind** (`U.EpistemeKind`) is a **signature** over these slots.

* **Episteme as n-ary relation and as holon.**
  Each concrete episteme instance can be seen both as:

  * a **filled value assignment** over this slot relation; when C.29 tuple reasoning is current, the assignment may be viewed as a tuple view without becoming a second episteme kind, and
  * a **holon with components** (`U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication`) whose fields correspond to those slots.

`U.Episteme` is thus the holon type whose components are *disciplined* by the `U.EpistemeSlotRelation`; C.2.1 fixes that discipline.

* **Morphisms.**
  Simple **epistemic morphisms** (EntityOfConcern-reference mapping, grounding, encoding, evaluation) are expressed as ordinary relations or functions between these positions and their graph-valued or non-graph-valued fillers. A.6.2-A.6.4 then specify general laws for effect-free morphisms over `U.Episteme`.

* **Symbol-Concept-Object triangle as didactic projection.**
  The classic Symbol-Concept-Object triangle becomes a **didactic view** of this slot relation, not the normative ontology; it is simply the projection to:

  * `Symbol` ~= a subset of `U.RepresentationScheme`/`U.RepresentationToken`,
  * `Concept` ~= `U.ClaimGraph`,
  * `Object` ~= `{EntityOfConcern, ReferenceScheme}`.

The rest of this pattern fixes the **minimal core** needed by KD-CAL, A.6.2-A.6.4 and E.17.*. The representational nodes (`U.RepresentationScheme`, `U.RepresentationToken`, `U.PresentationCarrier`, `U.RepresentationOperation`) are introduced as an **extension C.2.1+**, preserving the slot-relation boundary and profile defined here.

#### C.2.1:4.1 - Minimal epistemic positions (nodes & slots)

This section defines the **minimal position set** for `U.EpistemeSlotRelation` and the associated **SlotKinds**. These are the positions that A.6.2-A.6.4 and E.17.* can rely on.

##### C.2.1:4.1.1 - `EntityOfConcernSlot` — “what this episteme is about”

**Tech:** `EntityOfConcernSlot` (SlotKind), `entityOfConcernRef : U.EntityRef` (Ref slot in tuples or cards).
**Plain:** *EntityOfConcern value*, *entity of concern*. The plain phrase helps readers name the slot value; it is not a current Tech head.

**Intent.** Provide a **single, explicit slot** for the entity (or entities) that an episteme is about, preventing conflation of Object, Reference, and Context.

**Normative definition.**

1. `EntityOfConcernSlot` is a **SlotKind** in the sense of A.6.5 `U.RelationSlotDiscipline`.

   * Its **ValueKind** is `U.Entity`.
   * Its **RefKind** is `U.EntityRef` (or a species thereof) and **MUST** be realised in data as a field named `entityOfConcernRef : U.EntityRef` (E.10 discipline).
1. Species of `U.EpistemeKind` **MAY** constrain the ValueKind to a subtype `EntityOfConcernClass ⊑ U.Entity` (for example, “the entity of concern is always a `U.Holon` and, more specifically, a `U.System` or `U.Episteme`”). The subtype **MUST NOT** be named `U.EntityOfConcern`; “EntityOfConcern value” is a local slot-use phrase, not a durable U-kind.
2. When source wording or a draft uses `U.EpistemicObject` as a separate kind, repair it as **"`U.Entity` filling `EntityOfConcernSlot`"** and keep the source wording only as source wording governed by E.10 and F.18.

**Didactic cue.**
“Ask: *What, exactly, is this description about?* That is the EntityOfConcern.”

##### C.2.1:4.1.2 - `GroundingHolonSlot` - where this is grounded and in what holon

**Tech:** `GroundingHolonSlot` (SlotKind), `groundingHolonRef : U.HolonRef?`.
**Plain:** *grounding holon*, *holon‑of‑grounding*, *engagement context*.

**Intent.** Capture the **material–social holon** (system, lab, infrastructure, organisation, runtime environment) with respect to which an episteme’s claims are **tested, calibrated or validated**.

**Normative definition.**

1. `GroundingHolonSlot` is a **SlotKind** with:

   * **ValueKind** `U.Holon`,
   * **RefKind** `U.HolonRef` (or a species thereof),
   * and recommended field name `groundingHolonRef? : U.HolonRef` in episteme cards or views.
2. `GroundingHolonSlot` is **optional** at the minimal core: an episteme may be **un‑grounded** at M‑mode (e.g., purely mathematical), but any episteme used for **empirical evaluation or assurance** under KD‑CAL **SHALL** either:

   * populate `groundingHolonRef`, or
   * declare explicitly that no such grounding is possible (e.g., counterfactuals, abstract logics), with consequences reflected in KD‑CAL `R`.
3. The phrase *“grounding holon”* is **plain‑register**; there is no durable U-kind `U.GroundingHolon`. It always means “the holon currently filling `GroundingHolonSlot` for this episteme.”

**Didactic cue.**
"Ask: *In which lab, organisation, or world-slice do we test or observe this?* That is the GroundingHolon."

##### C.2.1:4.1.3 - `U.ClaimGraph` and `ClaimGraphSlot` — claim content

**Tech:** `U.ClaimGraph` (ValueKind), `ClaimGraphSlot` (SlotKind).
**Plain:** *claim graph*, *claim content*.

**Intent.** Reuse the existing KD‑CAL notion of **ClaimGraph** as the episteme’s **claim body**, but make its slot value use explicit.

**Normative definition.**

1. `U.ClaimGraph` is the **ValueKind** for `ClaimGraphSlot`:

   * nodes: typed claims (definitions, axioms, theorems, requirements, properties, assumptions);
   * edges: logical, derivational, or refinement relations, as already defined in C.2.
2. `ClaimGraphSlot` is a **SlotKind** whose instances are always **stored by value** in core patterns:

   * `content : U.ClaimGraph` is the normative field in `U.EpistemeCard` / `U.EpistemeView`;
   * C.2.1 **MUST NOT** introduce `U.ClaimGraphRef` as a ValueKind. Any reference type for ClaimGraphs, if needed, is a **RefKind** defined by discipline packs on top of `U.ClaimGraph`.
3. `ClaimGraphSlot` is **mandatory**: every `U.EpistemeKind` that uses C.2.1 **SHALL** have exactly one `ClaimGraphSlot`.

**Didactic cue.**
“Ask: *What is actually being claimed, defined, required, proved?* That is the ClaimGraph.”

##### C.2.1:4.1.4 - `U.Viewpoint` and `ViewpointSlot` — perspective of concerns and validators

**Tech:** `U.Viewpoint` (ValueKind), `ViewpointSlot` (SlotKind), `viewpointRef : U.ViewpointRef?`.
**Plain:** *viewpoint*, *perspective*, *stakeholder perspective*.

**Intent.** Provide a **first-class reusable catalogue** for ISO-style viewpoints and their generalisations, as used by E.17.0 `U.MultiViewDescribing`, MVPK, and TEVB.

**Normative definition.**

1. `U.Viewpoint` is the type of **viewpoint specifications**:

   * system or acting-holon families with current role assignments and stakeholder groups the viewpoint speaks for,
   * their **concerns**,
   * allowed **kinds of Description epistemes and Description epistemes admitted for specification use**,
   * and **conformance rules** for views under this viewpoint.
     (The internal structure of `U.Viewpoint` is fixed in E.17.0, not here.)
2. `ViewpointSlot` is a **SlotKind** with:

   * **ValueKind** `U.Viewpoint`,
   * **RefKind** `U.ViewpointRef`,
   * normative field name `viewpointRef? : U.ViewpointRef` on episteme cards or views.
3. For Description epistemes, including Description epistemes admitted for specification use, under E.10.D2, `viewpointRef` is a **mandatory part of `DescriptionContext`**; C.2.1 treats that as a **species-level constraint**, not as a universal requirement for all epistemes.
4. `ViewpointSlot` may be unset in purely internal, pre‑viewpoint epistemes (e.g., raw formal developments), but any episteme that participates in **MultiViewDescribing** (E.17.0) **MUST** set it or be deterministically associated to it via a `ViewpointBundle`.

**Didactic cue.**
“Ask: *Who is this for, and what do they need to see to accept it?* That is the Viewpoint.”

##### C.2.1:4.1.5 - `U.EpistemeView` / `U.View` and `ViewSlot` — episteme‑level views

**Tech:** `U.EpistemeView` (species of `U.Episteme`), selected short form `U.View`; `ViewSlot` (SlotKind); `viewRef : U.ViewRef`.
**Plain:** *view*, *epistemic view*.

**Intent.** Distinguish **view‑epistemes** (views **of** Description epistemes or Description epistemes admitted for specification use) from both:

* the underlying Description epistemes or Description epistemes admitted for specification use themselves, and
* the MVPK literal `publication-face form` and `interop publication form` values of `publication-face kind`, plus the publication-side carriers and renderings on which views are made available (E.17, publication-face-kind discipline, and A.10 carrier and source-currentness relations when evidence or reliance use is current).

**Normative definition.**

1. `U.EpistemeView` is a **species of `U.Episteme`** whose episteme kind includes, at minimum:

   * one `ClaimGraphSlot` (typically a **sliced or projected ClaimGraph**),
   * one `EntityOfConcernSlot`,
   * one `ViewpointSlot`,
   * and appropriate `ReferenceSchemeSlot`.
2. `U.View` is the **selected short form** for `U.EpistemeView` in E-cluster patterns (especially E.17.*), used where the word “view” is conventional.
3. `ViewSlot` is a **SlotKind** whose:

   * **ValueKind** is `U.View`,
   * **RefKind** is `U.ViewRef` (or `U.EpistemeViewRef` species),
   * intended usage is **in meta‑structures** such as `U.MultiViewDescribing` families and MVPK.
4. `ViewSlot` **MUST NOT** be confused with publication-face labels, `publication-face kind` declarations, or carrier slots: a concrete MVPK face that is a view is represented as `U.View` or `U.EpistemeView`, while the face label, publication-form profile, literal `publication-face form` or `interop publication form` `publication-face kind` value, and carrier or rendering remain separate relation positions.

**Didactic cue.**
“Ask: *Which particular slice of the description under this viewpoint are we talking about?* That is the View.”

##### C.2.1:4.1.6 - `U.ReferenceScheme` and `ReferenceSchemeSlot` — interpreting ClaimGraph as claims about entities

**Tech:** `U.ReferenceScheme` (ValueKind), `ReferenceSchemeSlot` (SlotKind); `referenceScheme? : U.ReferenceScheme`.
**Plain:** *reference scheme*, *interpretation scheme*, *description scheme*.

**Intent.** Separate **what is being said** (ClaimGraph) from **how claims are read as statements about entities and contexts** (designation, measurement, evaluation envelopes), without reifying the referents themselves as a vertex.

**Normative definition.**

1. `U.ReferenceScheme` is a **component type of epistemes**, not an external entity:

   * it determines how nodes of `U.ClaimGraph` are mapped to **properties or relations** over values of `EntityOfConcernSlot`,
   * it specifies **measurement and evaluation templates** (how to test claims on `GroundingHolon`),
   * it fixes **claim-scope predicates and admissible regions** over declared `U.ContextSlice` selectors (and, where needed, references to domain spaces used inside those selectors).
2. `ReferenceSchemeSlot` is a **SlotKind** with:

   * **ValueKind** `U.ReferenceScheme`,
   * **no RefKind in the minimal core** (ReferenceSchemes are stored by value as `referenceScheme? : U.ReferenceScheme` fields on episteme cards or views).
     Discipline packs **may** introduce `U.ReferenceSchemeRef` as a **RefKind**, but **must not** repurpose it as a new ValueKind.
3. `ReferenceScheme` is the place where Object-vertex concerns are split into explicit claim-to-EntityOfConcern and claim-to-grounding rules:

   * it does **not** “contain” the EntityOfConcern value or grounding referent,
   * it carries the **rules** that tie claims to entities and groundings.

**Didactic cue.**
“Ask: *Given this ClaimGraph, how exactly do we treat it as talking about these entities in these contexts, and how do we test it?* That is the ReferenceScheme.”

##### C.2.1:4.1.7 - Minimal slot relation and extension C.2.1+

The **minimal `U.EpistemeSlotRelation` core** for C.2.1 consists of positions (the episteme core SlotKinds of A.6.5 CC-A.6.5-5):
* `EntityOfConcernSlot` (ValueKind `U.Entity`),
* `GroundingHolonSlot` (ValueKind `U.Holon`),
* `ClaimGraphSlot` (ValueKind `U.ClaimGraph`),
* `ViewpointSlot` (ValueKind `U.Viewpoint`),
* `ViewSlot` (ValueKind `U.View`),
* `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`).

This pattern **only fixes these positions** and their SlotSpec discipline. It does not turn every graph-valued value into a tuple and does not turn the tuple into a graph.
The **extension C.2.1+** (second step of the refactor) adds:
* `U.RepresentationScheme` and `RepresentationSchemeSlot`,
* `U.RepresentationToken` and `RepresentationTokenSlot`,
* `U.PresentationCarrier` and `PresentationCarrierSlot`,
* `U.RepresentationOperation` and `RepresentationOperationSlot` (with inference regime annotations),

without changing:
* the definition of `U.EpistemeKind`,
* the minimal `U.EpistemeCard` interface,
* or the assumptions A.6.2-A.6.4 and E.17.* make about episteme components.

In C.2.1+ `U.PresentationCarrier`, publication-face-kind values, MVPK face, carrier, and rendering relations remain **publication-side carriers, faces, forms, units, or rendering relations**, not semantic parts of the episteme:
`U.PresentationCarrier` values are linked to `U.Episteme` and `U.View` via MVPK and publication-face-kind discipline relations, such as `isCarriedBy` and MVPK face relations, and **MUST NOT** be counted as components when reasoning about episteme identity, EntityOfConcernSlot filling, GroundingHolonSlot filling, or KD-CAL morphisms. Changing carriers, publication faces, publication forms, units, or renderings alone **never** changes the `U.Episteme` instance determined by C.2.1; it only produces `U.Work` occurrences that publish or republish the same `U.Episteme`.

##### C.2.1:4.1.8 - Attached epistemic structures (non-slot components)

`U.EpistemeSlotRelation` deliberately does **not** reify every episteme-adjacent structure as a slot. Several key structures remain **attached, non-slot components** of `U.Episteme`:
* **`JustificationGraph`** - the argument and evidence graph for nodes of `U.ClaimGraph` (A.10 and B.3).
* **`EvidenceBindings`** - per-claim evidence-use bindings, A.10 evidence-provenance refs, or B.3 assurance-evidence refs that connect claims to evidence-producing or evidence-interpreting `U.Work` occurrences, role assignments when current, carrier and source-currentness records, and publication or carrier relations.
* **`EditionSeries`** - the `PhaseOf` chain of episteme editions (A.14) with change-class annotations (symbol-only vs ClaimGraph vs ReferenceScheme changes).
* **`ScopeCard` and `U.ClaimScope`** - USM scope values (A.2.6) describing where the episteme's claims hold.

These attached structures are **not extra positions** of `U.EpistemeSlotRelation`; they hang off the `U.ClaimGraph` and `U.ReferenceScheme` pair and are governed by KD-CAL (C.2), A.10, and B.3. C.2.1 only requires that an episteme which participates in KD-CAL exposes them in a way that keeps **ClaimGraph, ReferenceScheme, Evidence, EditionSeries, and `ClaimScope`** clearly distinguishable.

#### C.2.1:4.2 - Episteme as n‑ary relation and as holon

To prevent confusion between **EntityOfConcern values**, their **descriptions**, and the **slots they fill in an episteme**, C.2.1 explicitly treats epistemes both as:

1. **n‑ary relations with a signature** (slots & values), and
2. **holons with components** (fields & parts).

##### C.2.1:4.2.1 - `U.EpistemeKind` — episteme as a typed n‑ary relation

**Tech:** `U.EpistemeKind` (ValueKind).

**Intent.** Provide a **signature‑level** description of an episteme as an n‑ary relation whose arguments are governed by `SlotKind`/`ValueKind`/`RefKind` triples per A.6.5.

**Normative definition.**

1. Every episteme that participates in KD‑CAL **belongs to some `U.EpistemeKind`**.
   The kind determines:

   * which **SlotKinds** appear (`EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`, …),
   * the **ValueKind** for each slot (declared through C.3 `U.Kind`, an admitted durable U-kind, a direct governed value kind, a Concept-Set row, or an imported signature symbol),
   * the **RefKind** used to store it in episteme (when applicable).
1. `U.EpistemeKind` is a **special case** of `U.Signature` (A.6.0), with its slots governed by `U.RelationSlotDiscipline` (A.6.5). C.2.1 **MUST NOT** define an alternative slot discipline.
2. For the minimal core, every `U.EpistemeKind` **MUST** include:
   * exactly one `ClaimGraphSlot`,
   * at least one `EntityOfConcernSlot`,
   * and at least one `ReferenceSchemeSlot`.
     Inclusion of `GroundingHolonSlot`, `ViewpointSlot`, `ViewSlot` **MAY** be species-level constraints (mandatory for Description epistemes, including Description epistemes admitted for specification use, optional for others).

**Didactic cue.**
“An `EpistemeKind` is the *kind declaration* for an episteme: which positions it has and what can go into them.”

##### C.2.1:4.2.2 - Filled episteme value assignment and C.29 tuple view

**Tech:** filled episteme value assignment over `U.EpistemeSlotRelation`; C.29 tuple view when tuple reasoning is current.

**Intent.** Model a filled use of an episteme's slot relation without making tuple, graph, or publication form into the ontology head.

**Normative definition.**

1. A filled episteme value assignment supplies one governed value or reference for each asserted SlotKind in the associated `U.EpistemeKind`:
   * for each SlotKind in the associated `U.EpistemeKind`, a value of the slot's **ValueKind** or a reference value of **RefKind**, if the kind is configured as such.
2. The filled assignment is **notation-agnostic** and **carrier-agnostic**: it does not know about files, formats, publication faces, publication forms, or carriers.
   It exists to give A.6.2-A.6.4 a minimal notion of "episteme as a filled point over the episteme SlotRelation".
3. Under `C.29`, the same filled assignment may be viewed as a tuple when tuple reasoning is the selected mathematical lens. That tuple view is a mathematical-lens representation of the filled SlotRelation, not a second episteme kind and not a replacement for graph-valued fillers such as `U.ClaimGraph`.
4. In ordinary episteme work, the filled assignment rarely appears directly; it is typically **induced** by `U.EpistemeCard` and `U.EpistemeView` (which add component structure and meta-information).

**Didactic cue.**
"A filled episteme assignment says *what fills which slots*; if C.29 asks for tuple reasoning, read that assignment as a tuple view."

##### C.2.1:4.2.3 - `U.EpistemeCard`, `U.EpistemePublication`, `U.EpistemeView` — holonic realisations

**Tech:** `U.EpistemeCard`, `U.EpistemePublication`, `U.EpistemeView` (species of `U.Episteme`).

**Intent.** Provide **holon-level structures** that engineers can work with (components, mereology, provenance), while keeping them aligned with `U.EpistemeKind` and `U.EpistemeSlotRelation`.

**Normative definition.**

1. **`U.EpistemeCard`.**
   A species of `U.Episteme` whose components correspond one‑to‑one to slots of some `U.EpistemeKind`:
   * `content : U.ClaimGraph` (for `ClaimGraphSlot`),
   * `entityOfConcernRef : U.EntityRef` (for `EntityOfConcernSlot`),
   * `groundingHolonRef? : U.HolonRef` (for `GroundingHolonSlot`),
   * `viewpointRef? : U.ViewpointRef` (for `ViewpointSlot`),
   * `referenceScheme? : U.ReferenceScheme` (for `ReferenceSchemeSlot`),
   * optionally `representationSchemeRef? : U.RepresentationSchemeRef` (C.2.1+),
   * `meta : Edition, Provenance, Status...`.
     Minimal episteme identity is the pair `⟨content, entityOfConcernRef⟩` within a `U.BoundedContext`; all other fields are optional at the genus level but may be mandatory in species. Changes that alter `content` or the effective `referenceScheme` (or that intentionally re-identify `entityOfConcernRef`) **SHALL** be realised as new phases in an `U.EditionSeries` (PhaseOf chain) under A.14 and A.7. Changes confined to `U.PresentationCarrier`, publication-side values, MVPK face, carrier, or rendering relations **do not** create a new episteme; they are captured as publication work over the same `U.Episteme`.
2. **`U.EpistemePublication`.**
   A species representing **epistemes that have been published** through publication faces, publication forms, or MVPK relations. It:
   * has at least the components of `U.EpistemeCard`,
   * plus references to MVPK `U.View`, face identity, literal `publication-face form` or `interop publication form` `publication-face kind` values, publication-scope fields, profile fields, and external carrier or rendering refs as required by E.17 and publication-face-kind discipline,

   * but **does not** re-interpret face labels, `publication-face kind` values, or carriers or renderings as parts of the episteme; carriers remain external.

3. **`U.EpistemeView`.**
   As defined in §4.1.5, a species of `U.Episteme` representing a **view** under a specific `U.Viewpoint`.
   Its components are a specialisation of `U.EpistemeCard`:
   * ClaimGraph often a restricted projection of a base description and specification-useification,
   * Viewpoint fixed,
   * ReferenceScheme tailored to that viewpoint.

**Alignment requirement.**
For any of these species, the pattern **MUST** state explicitly:
* which `U.EpistemeKind` it realises, and
* how each component maps to a SlotKind or RefKind under `U.RelationSlotDiscipline`.

This ensures that A.6.2–A.6.4 can treat any `U.Episteme*` uniformly as both:
* a category-theory object in the category **Ep**, and
* a structured holon with components.

##### C.2.1:4.2.3a - Episteme, publication, view, carrier, cue, and authority-reference relation positions  *(normative)*

C.2.1 is the default FPF pattern for claim-bearing units. Do not mint a generic `U.SemioObject`, `U.SemioticObject`, `U.SignObject`, `U.WorkingObject`, or `U.SourceMaterial` when the claim-bearing unit in question should be modeled as an episteme. Use `U.Episteme` or a declared species of `U.Episteme`.

When the same claim-bearing unit is available to readers, tools, or downstream work as a published episteme, name that relation position as `U.EpistemePublication` or as a governed `U.Episteme` publication. Then keep the adjacent relation positions separate:

* **publication form** - the concrete form in which the episteme is made available for some use, such as a cue pack, transfer-prepared claim set, prompt form, partial normal form, record, card, table, or local C.29 output;
* **view, including MVPK face** - `U.View` or `U.EpistemeView` under a declared `U.Viewpoint`, including MVPK faces such as `PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane`;
* **carrier or rendering** - the document, dashboard, generated screen, trace file, transport envelope, display, or A.10 carrier and source-currentness record that bears or renders a publication;
* **source-finding cue** - a badge, tile, heading, signature-looking mark, credential display, generated explanation, or other cue that helps find a source but does not by itself create an authority-reference relation;
* **governing pattern reference and authority-reference field** - `governingPatternRef` when one FPF pattern governs admissible interpretation or use; `authoritySourceRef` when a non-pattern authority-source referent such as an external standard, editioned register, decision record, gate decision, policy source, or role-assignment or status register carries the relevant authority. The publication records this reference; it does not become the referenced authority.

For latent, distributed, reconstructed, or model-state material, do not call the encountered material a `U.Episteme` merely because it can be decoded into prose, embedded in a vector space, or shown as a dashboard cue. It becomes an episteme only when the needed C.2.1 positions are recoverable for the current use: at least the `EntityOfConcernSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot` or equivalent interpretation rule, and any current grounding, viewpoint, view, publication, carrier, source-use, evidence, or authority-reference relation named by the direct governing pattern.

No publication form, view, face, carrier, rendering, source-finding cue, dashboard signal, credential display, generated explanation, FPF pattern file, or FPF pattern section is itself a substitute for a governed `U.Episteme`, an evidence relation, an assurance claim, a gate decision, a permission, a role claim, a status claim, or a `U.Work` occurrence. If the next use concerns work, keep candidate reliance, `U.WorkPlanning`, planned work, actual `U.Work`, work result, and work-result measurement in their own work-side patterns rather than storing them inside the episteme or its carrier.

##### C.2.1:4.2.4 - SlotKind, ValueKind, and RefKind discipline for EntityOfConcern and GroundingHolon

C.2.1 adopts **A.6.5 `U.RelationSlotDiscipline`** wholesale. For the two key positions:
1. **EntityOfConcernSlot.**
   * `SlotKind = EntityOfConcernSlot`;
   * `ValueKind = U.Entity` (species may constrain to `EntityOfConcernClass ⊑ U.Entity`);
   * `RefKind = U.EntityRef` (or a species thereof);
   * normative field name in episteme cards: `entityOfConcernRef : U.EntityRef`.
     No durable U-kind named `U.EntityOfConcern` is introduced; the phrase “EntityOfConcern value” always means “an instance of `U.Entity` filling `EntityOfConcernSlot`”.
1. **GroundingHolonSlot.**
   * `SlotKind = GroundingHolonSlot`;
   * `ValueKind = U.Holon`;
   * `RefKind = U.HolonRef`;
   * normative field name: `groundingHolonRef? : U.HolonRef`.
     There is no durable U-kind `U.GroundingHolon`; “grounding holon” is a **slot-filler phrase**.
Any episteme text that mixes slot, value, and ref concepts (e.g., using `EntityOfConcernRef` as if it were a type) **MUST** be repaired to this discipline when the claim is current; C.2.1 provides the normative reference, and F.18 or the relevant discipline pattern governs any naming decision.

#### C.2.1:4.3 - Minimal epistemic morphisms (informal schema)

> **Note.** The full mathematical treatment (categories Ep and Ref, entityOfConcern functor `α : Ep → Ref`, and effect‑free morphisms) lives in A.6.2–A.6.4. Here we fix only the **episteme-slot relations** that C.2.1 expects to exist between its positions.

At the level of `U.EpistemeCard` components and SlotKinds, we assume the following **primitive relations** (not all are functions):

1. **`entityOfConcernSet : U.Episteme → P(U.Entity)`**
   *derivable from `EntityOfConcernSlot` and `ReferenceScheme`*
   * For an episteme `E`, `entityOfConcernSet(E)` is (at least) the singleton containing the entity referenced by `entityOfConcernRef(E)`; in more complex cases, it may be a finite set or bundle of entities, determined by `ReferenceScheme`.
   * The **functorial EntityOfConcern mapping** `δ_E : Ep → Ref` used in A.6.2–A.6.4 is the categorical lift of this relation: it forgets episteme internals and keeps only the EntityOfConcern value in the ReferencePlane determined by the pair `<EntityOfConcernSlot, GroundingHolonSlot>`.

2. **`grounds : (U.Entity, U.Holon) ⇝ GroundingRelation`**
   *relates EntityOfConcern values to grounding holons*
   * Captures how values of `EntityOfConcernSlot` are **situated** in holons that make evaluation possible (labs, infrastructures, organisations).
   * Need not be total or functional; an entity may admit multiple grounding holons, or none.

3. **`designates : (U.ReferenceScheme, U.ClaimGraph, U.Entity, U.Holon) ⇝ DesignationProfile`**
   *how claims are read as statements about entities in contexts*
   * Specifies, for each claim in `content` and each `<entityOfConcernRef, groundingHolonRef>`, what property or relation it purports to state, and under what conditions.

4. **`satisfies` or `evaluatesTo : (U.ClaimGraph, U.ReferenceScheme, U.Holon) -> TruthProfile or SuccessProfile`**
   *evaluation of claims under a reference scheme and grounding*
   * Forms the bridge to KD‑CAL’s `F, G, R` evaluation; details are given in C.2 and B.3.

5. **View-related morphisms** (to be connected with A.6.3):
   * `viewProject : (U.Episteme, U.Viewpoint) → U.View`
     — effect-free, **EntityOfConcern-preserving** projection that slices `ClaimGraph` and specialises `ReferenceScheme` under a given viewpoint.
   * `viewEmbed : U.View → U.Episteme`
     — embedding of a view back into the wider episteme, typically as a reference with correspondence proofs.

5. **Reflexive entityOfConcern guard.**
   When `EntityOfConcernSlot` or `ReferenceScheme` picks out an episteme or claim that includes the referring claim itself (**ReferencePlane = episteme**), publishers **SHALL** ensure that the induced justification and evaluation structure is **acyclic per evaluation chain**: reflexive describe or citation handles may exist as literature handles, but they MUST NOT form a minimal justification cycle for acceptance or KD-CAL assurance. Self-reference is allowed as a citation pattern, not as a way to close justification loops.

These are **not yet laws**; they are the **hooks** that A.6.2–A.6.4 will formalise into:
* `U.EffectFreeEpistemicMorphing` (Ep→Ep morphisms over this structure),
* `U.EpistemicViewing` (entityOfConcern‑preserving Ep→Ep),
* `U.EpistemicRetargeting` (entityOfConcern‑retargeting Ep→Ep).

### C.2.1:5 - Semantic triangle as didactic view  *(informative)*

**Position.** The classical semiotic or semantic triangle ("Symbol-Concept-Object", Ogden-Richards and Frege-Carnap style) is **not** the normative ontology for epistemes in FPF. For `U.Episteme`, it is treated as a **didactic projection** of `U.EpistemeSlotRelation`. The projection compresses several SlotSpecs and graph-valued fillers into three teaching corners:
* **"Symbol" corner** ~= {`U.RepresentationToken`, `U.RepresentationScheme`, `U.PresentationCarrier`} when C.2.1+ is in use; in the minimal core this is collapsed into whichever external carrier bears the `U.ClaimGraph` publication.
* **"Concept" corner** ~= `U.ClaimGraph` + `U.ReferenceScheme` under a chosen `U.Viewpoint`. This is the claim content plus its interpretation recipe.
* **"Object" corner** ~= the slot filler of `EntityOfConcernSlot` (ValueKind `U.Entity`) plus the slot filler of `GroundingHolonSlot` (ValueKind `U.Holon`) and the grounding relation between them.

Under this didactic projection the triangle is a **three-corner quotient** of the episteme slot relation:
```text
(Symbol)      = RepresentationToken + Scheme + Carrier
(Concept)     = ClaimGraph + ReferenceScheme (+ Viewpoint)
(Object)      = EntityOfConcern + GroundingHolon
```

All **viewpoints, operations, carriers and reference planes** are suppressed in the classical diagram. The cost of this suppression is precisely the confusion that motivates C.2.1:
* describing becomes a single unlabeled arrow,
* inference regimes disappear,
* measurement and grounding are invisible.

**Didactic use.** C.2.1 allows the triangle **only** in the following cases:
1. As an **introductory picture** in guidance material ("this is the coarse triangle; the actual pattern is the episteme slot relation").
2. As a **quotient diagram**: an explicit note that "this figure ignores viewpoint, grounding, carrier, and operationality; see C.2.1 for the full structure".
3. As an **external-triangle alignment aid** when mapping to standards or literature that speak only in triangle terms.

**Guard.** Any pattern or documentation page that uses a "semantic triangle" diagram **MUST** either:
* explicitly state "this is a didactic projection of C.2.1 `U.EpistemeSlotRelation`", or
* treat it as an external-triangle reference when aligning with external standards.

The triangle **MUST NOT** be used as a kernel-level ontology or as a source for morphism laws. All normative reasoning about epistemes proceeds via the slots, graph-valued fillers, non-graph-valued fillers, and components governed by `U.EpistemeSlotRelation`.

### C.2.1:6 - Interaction with EntityOfConcern and Description-episteme boundary, specification use and refinement, and DescriptionContext  *(normative)*

C.2.1 is the **episteme-side slot schema** that the boundary between `EntityOfConcern` and Description episteme discipline (A.7, E.10.D2) relies on. The link is made via `DescriptionContext`, not by treating EntityOfConcern value, Description epistemes, and specification use and refinement as layers, carriers, or peer ontology classes.

#### C.2.1:6.1 - DescriptionContext over C.2.1 components

For any episteme that is a **Description** in the sense of E.10.D2, including a Description episteme admitted for specification use, the field `subjectRef : U.SubjectRef` is interpreted as a **DescriptionContext triple**:
```
DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩
```

where:
* `EntityOfConcernRef : U.EntityRef` — fills `EntityOfConcernSlot` (ValueKind `U.Entity`, species often constrained via EntityOfConcernClass ⊑ `U.Entity`).
* `BoundedContextRef : U.BoundedContextRef` — points to the context that fixes vocabulary, units, and admissible inferences for this description (E.10.D1).
* `ViewpointRef : U.ViewpointRef` — fills `ViewpointSlot` (ValueKind `U.Viewpoint`) and determines which concerns, system or acting-holon families with current role assignments, stakeholder groups, and conformance rules apply.

**Normative requirement (DESCCTX-13).**
For every `...Description` episteme, and every `...Spec` use admitted by neighbouring specification use and refinement gates:
1. `subjectRef` **SHALL** be decodable to a well‑formed DescriptionContext triple.
2. `EntityOfConcernRef` from that triple **SHALL** be identical to the field `entityOfConcernRef` that fills `EntityOfConcernSlot` in the corresponding `U.EpistemeCard`/`U.EpistemeView`.
3. `ViewpointRef` in DescriptionContext **SHALL** agree with `viewpointRef` in the episteme card or be uniquely derivable from a `U.ViewpointBundle` in E.17.1 (with the derivation rule documented).

EntityOfConcern values such as `U.System`, `U.Method`, `U.Role`, or `U.Episteme` appear in C.2.1 as values of `EntityOfConcernSlot` when an episteme describes, views, or retargets them. They are not the Description episteme produced by that use. The boundary between `EntityOfConcern` and Description episteme separates the EntityOfConcern value from the Description episteme; specification use and refinement is a separate gated use or refinement of that Description episteme, not a third peer ontology class. This boundary does not ban epistemes from being EntityOfConcern values.

**Example.** A formal postulate theorem in physics can be a Description episteme about the behaviour of a physical grounding holon. Its `EntityOfConcernSlot` points to the physical grounding holon, or to the exact behavior, method, or work entity only when a governing pattern has selected that entity under concern; its claim graph carries the theorem, postulates, and derivation; its formal language belongs to formality and publication-expression discipline. It becomes a specification only if a bounded use assigns specification force, such as acceptance criteria, harness checks, normative invariants, C.16 measurement criteria, or verification use. Formal notation alone does not change the slot relation into a third `Specification` ontology class.

#### C.2.1:6.2 - EntityOfConcern-to-Description morphism and specification-use boundary over C.2.1


* **Describing (`Describe_EoC_DescEp : EntityOfConcern -> DescriptionEpisteme`).**
  Produces an episteme whose:
  * `content : U.ClaimGraph` encodes the descriptive claims about the `EntityOfConcern` value,
  * `entityOfConcernRef` points to the EntityOfConcern value,
  * `groundingHolonRef` (if present) fixes where the description is evaluated or tested,
  * `viewpointRef` selects the describing viewpoint.

  `Describe_EoC_DescEp` is **conformant** to A.6.2 but not an Ep→Ep morphism (domain is the `EntityOfConcern` value, codomain is a Description-side `U.Episteme`). C.2.1 provides the **codomain schema** and ensures that the resulting Description has a valid DescriptionContext.

C.2.1 does not decide that a Description episteme has become a Specification. If a bounded use formalises, constrains, test-harnesses, accepts, or publishes a Description episteme as a specification, the governing pattern must name the exact specification-use gate: A.6.2 for effect-free episteme refinement, C.2.3 for formality and checkability, A.21 or the relevant gate or acceptance pattern for harness and acceptance force, C.16 for measurement criteria, E.17 for publication expression, and E.10 for suffix discipline. The C.2.1 requirement is only that the Description episteme keeps the same `entityOfConcernRef`, `BoundedContextRef`, and `ViewpointRef` unless a retargeting or viewing pattern named by value declares otherwise.

C.2.1 does **not** define the full `EntityOfConcern` / Description-episteme boundary or the specification-use gates; it only insists that any `...Description` episteme, and any `...Spec` use admitted by neighbouring gates, must:
* implement `U.EpistemeCard` or `U.EpistemeView` **with** `content`, `entityOfConcernRef`, `groundingHolonRef?`, `viewpointRef?`, and `referenceScheme?` fields, and
* wire these fields into `subjectRef` as DescriptionContext.

### C.2.1:7 - Alignment with A.6.2–A.6.4 (episteme morphisms)  *(normative)*
`U.EpistemeSlotRelation` is the **slot-relation substrate** for the episteme morphism patterns:
* A.6.2 `U.EffectFreeEpistemicMorphing`
* A.6.3 `U.EpistemicViewing`
* A.6.4 `U.EpistemicRetargeting`

#### C.2.1:7.1 - Effect‑free episteme morphisms (A.6.2) over C.2.1
For any `f : X → Y` that is an instance of `U.EffectFreeEpistemicMorphing`:
* **Typed episteme values.**
  X and Y are `U.Episteme` instances realised as `U.EpistemeCard` / `U.EpistemeView` with at least the minimal core components:

  ```
  content            : U.ClaimGraph
  entityOfConcernRef : U.EntityRef      // EntityOfConcernSlot
  groundingHolonRef? : U.HolonRef       // GroundingHolonSlot
  viewpointRef?      : U.ViewpointRef   // ViewpointSlot
  referenceScheme?   : U.ReferenceScheme// ReferenceSchemeSlot (ByValue)
  ```

  Any additional C.2.1+ components (RepresentationScheme, Tokens, Carriers, Operations) are visible to A.6.2 only through their declared SlotKinds (A.6.5).
* **EntityOfConcernChangeMode characteristic.**
  `f` **MUST** declare a **`entityOfConcernChangeMode ∈ {preserve, retarget}`**:
  * `preserve` - `entityOfConcernRef(Y) = entityOfConcernRef(X)` and any change to `groundingHolonRef` or `viewpointRef` must be justified by Bridges or CorrespondenceModel, without changing the EntityOfConcernSlot value;
  * `retarget` — permitted only for A.6.4 species; see below; in this case the characteristic records an intentional change in the pair `<entityOfConcernRef, groundingHolonRef>` under a declared `KindBridge` in the appropriate ReferencePlane.

  This **EntityOfConcernChangeMode** is a CHR-style *characteristic* (A.17) on episteme morphisms, which points directly to `EntityOfConcernSlot`. Avoid introducing a separate “entityOfConcern” term alongside `EntityOfConcern`.

* **Component discipline.**
  P0–P5 from A.6.2 are read **directly** in terms of C.2.1 components:
  * purity => only C.2.1 components of Y may change; no Work or Mechanism side-effects;
  * conservativity ⇒ claims in `content_Y` read via `referenceScheme_Y` about the new `<EntityOfConcern, GroundingHolon>` do not go beyond what already follows from `content_X` via `referenceScheme_X` under the declared EntityOfConcernChangeMode and Bridges;
  * functoriality ⇒ composition of such transformations respects the slot structure and ReferenceSchemes.

Any Ep-to-Ep pattern that operates on `U.Episteme` **MUST** state which C.2.1 slots it reads and which it may write, in terms of SlotKinds, ValueKinds, and RefKinds (A.6.5), and then declare itself a species of A.6.2, A.6.3, or A.6.4 as appropriate.

#### C.2.1:7.2 - EpistemicViewing (A.6.3) as entityOfConcern‑preserving projections

`U.EpistemicViewing` is the **EntityOfConcern-preserving** species of A.6.2. Over C.2.1 this means:
* `entityOfConcernRef(Y) = entityOfConcernRef(X)` — the same value in `EntityOfConcernSlot`.
* `groundingHolonRef` is preserved, or changed only within a fixed grounding context (e.g. normalising identifiers for the same lab or runtime).
* `viewpointRef` is either:
  * preserved (internal normalisation under the same viewpoint), or
  * replaced by another `U.ViewpointRef` *within* a `U.MultiViewDescribing` family (E.17.0), with invariants enforced by a CorrespondenceModel.
* `content` and `referenceScheme` are transformed **conservatively**: no new claim content about the same `EntityOfConcern` is introduced.

Typical examples:
* filtering or aggregating `U.ClaimGraph` to a view relevant for a stakeholder group;
* rendering a behavioural specification into a tabular or diagrammatic episteme under a publication viewpoint;
* normalising a logic‑heavy episteme into a more operational one, while keeping the same system EntityOfConcern and context.

In terms of SoTA, EpistemicViewing behaves like a **lens** or **optic** over C.2.1: a focus (SlotKinds for content and representation) is manipulated while the EntityOfConcern is fixed.

#### C.2.1:7.3 - EpistemicRetargeting (A.6.4) as EntityOfConcern-bundle retargeting on episteme morphisms

`U.EpistemicRetargeting` is the species of A.6.2 where **`entityOfConcernChangeMode = retarget`**.
It is always a **morphism between epistemes** (`f : X → Y` in `U.Episteme`), but the adjective “retargeting” refers **not** to the fact that an episteme is mapped to another episteme (this is true for all A.6.2 species), and **not** to a separate entityOfConcern, but specifically to the **change in the EntityOfConcern-bundle** classified by C.2.1:
* `entityOfConcernRef(Y) ≠ entityOfConcernRef(X)` — the value stored for `EntityOfConcernSlot` changes;
* a `KindBridge` must relate `Kind(entityOfConcernRef(X))` and `Kind(entityOfConcernRef(Y))`;
* `groundingHolonRef` may remain the same (e.g. same plant, different subsystem) or be transformed along a Bridge in the same ReferencePlane.

In practice, many retargetings operate on the **`EntityOfConcernSlot`/`GroundingHolonSlot` pair** (for example, when an episteme about a physical module is re-interpreted as an episteme about a function-holon realised in a different environment). The characteristic `entityOfConcernChangeMode` still classifies such morphisms by whether this pair is preserved or intentionally re-identified under a `KindBridge` and reference-plane policy; the episteme on the codomain side is just the usual A.6.2 codomain episteme.

Over C.2.1 this is used for:
* **functional vs structural reinterpretation** (e.g. an episteme about a physical module retargeted to an episteme about the function it realises; StructuralReinterpretation in E.18 becomes a species of A.6.4);
* **signal vs spectrum** transitions (Fourier-style moves where the `EntityOfConcernSlot` value changes from time-domain signal to frequency-domain representation but an invariant, such as energy, is preserved);
* **data vs model** transitions (e.g. retargeting an episteme about raw observations to an episteme about a learnt model, with an invariant such as likelihood or sufficient statistics).

C.2.1 ensures that these retargetings have a **clear domain `EntityOfConcernSlot` value and codomain `EntityOfConcernSlot` value** and that any such move is expressed as a morphism over well-typed slots, not as an unstructured rewrite of “subject” or “object” labels.

### C.2.1:8 - Alignment with E.17.* (Multi‑View Describing & Publication)  *(normative)*

`U.EpistemeSlotRelation` underpins the E.17 cluster:
* E.17.0 `U.MultiViewDescribing`
* E.17.1 `U.ViewpointBundleLibrary`
* E.17.2 `TEVB — Typical Engineering Viewpoints Bundle`
* E.17 `MVPK — Multi‑View Publication Kit`

#### C.2.1:8.1 - Multi‑View Describing (E.17.0)

`U.MultiViewDescribing` organises **families of Description epistemes and Description epistemes admitted for specification use** over a shared entity of concern:
* The **EntityOfConcernClass** parameter of E.17.0 is a species constraint on the ValueKind of `EntityOfConcernSlot` (`EntityOfConcernClass ⊑ U.Entity`).
* Each member of a multi‑view family is a `…Description`/`…Spec` episteme with:
  * `entityOfConcernRef` into that EntityOfConcernClass,
  * `viewpointRef` drawn from a `U.ViewpointBundle`,
  * `subjectRef` decoding to DescriptionContext.

Within this pattern:
* `U.Viewpoint` is **exactly** the ValueKind of `ViewpointSlot` in C.2.1.
* `U.View` is `U.EpistemeView`, a species of `U.Episteme` whose `content` is already restricted to a particular `U.Viewpoint` and often also to a particular `U.RepresentationScheme`.

C.2.1 thus supplies the **per‑episteme** structure that E.17.0 rearranges into multi‑view families.

#### C.2.1:8.2 - Viewpoint bundles (E.17.1 and E.17.2)

`U.ViewpointBundleLibrary` and TEVB specialise the `U.Viewpoint` node:
* A ViewpointBundle is a **set of `U.Viewpoint` instances** tailored to a class of entities of concern (e.g., holons in engineering contexts).
* TEVB fixes `EntityOfConcernClass = U.Holon` (typically `U.System` or `U.Episteme`) and provides canonical engineering viewpoints: functional, structural, role‑enactor, interface‑oriented, etc.

From the C.2.1 perspective:

* these bundles populate the ValueKind of `ViewpointSlot`;
* engineering episteme species that want to be “TEVB‑aligned” must restrict `viewpointRef` to TEVB’s `EngineeringVPId` set, while keeping the same EntityOfConcernSlot discipline.

#### C.2.1:8.3 - MVPK (E.17) as publication over C.2.1 views

MVPK treats `U.View` (i.e. `U.EpistemeView`) as its primary input:
* it uses `U.EpistemicViewing` species (A.6.3) to generate publication‑oriented views from engineering or logical views;
* it then publishes these `U.View` epistemes through declared publication-face-kind values with declared publication viewpoints and faces.

C.2.1’s distinction between:

* `U.Viewpoint` (epistemic perspective specification) and
* `U.PresentationCarrier` (carrier in C.2.1+ and publication-face-kind discipline)

keeps **epistemic perspective and physical medium separate**:
* MVPK operates on `U.View` epistemes and then on carriers;
* the same View can be realised on multiple carriers without changing its entityOfConcern or ClaimGraph.

Any MVPK species that claims to be C.2.1‑conformant **MUST**:
* treat `U.View` as a `U.EpistemeView` with a valid C.2.1 core,
* document which C.2.1 slots it reads and writes (typically only representation-related and carrier-related ones, leaving `EntityOfConcernSlot` and `GroundingHolonSlot` untouched),
* refrain from introducing new claims about the EntityOfConcern value beyond what is in the source `U.View`’s ClaimGraph.

### C.2.1:9 - Archetypal Grounding

**System-description episteme.** A pump maintenance specification is an episteme whose EntityOfConcernSlot points to the pump or pump class, whose GroundingHolonSlot may point to the plant or test bench, whose ClaimGraph states maintenance claims, and whose ReferenceScheme explains how part names, measurements, and operating states refer to the pump in that bounded context. The PDF, database row, and rendered checklist are publication and carrier values, not the episteme itself.

**Episteme-about-episteme case.** A review note about a simulation model is also an episteme, but its EntityOfConcernSlot points to the simulation model episteme. The slot relation still separates the reviewed episteme, the review episteme, the claim graph, grounding holon, reference scheme, and evidence relation; the fact that the EntityOfConcern value is itself an episteme does not create a second ontology.

**Multi-view description case.** An architecture description may publish several views under different viewpoints. Each view is an episteme view constrained by the same episteme slot relation, while the publication face or carrier belongs to E.17 rather than to the episteme core.

### C.2.1:10 - Bias-Annotation  *(informative)*

**Episteme‑first and pragmatics‑first.**
The pattern assumes that a claim-bearing episteme is meaningful only when it is **about something for someone under some perspective**. This follows the pragmatic turn in semantics: EntityOfConcern and concerns are not afterthoughts but part of the core structure. The slot relation is organized around EntityOfConcern, GroundingHolon, Viewpoint, and ClaimGraph positions, while graph-valued fillers such as `ClaimGraph` and `JustificationGraph` remain distinct values inside those positions.

**Operational and representational bias.**
C.2.1+ anticipates that certain RepresentationSchemes are **operational** in Novaes’ sense (admitting direct syntactic inference, like pen-and-paper arithmetic or proof states) while others are **purely notational**. The pattern remains neutral on which schemes are used but bakes in a place for operations and carriers so that:

* symbol‑manipulating tools (SAT solvers, SMT solvers, proof assistants, classical programming languages),
* distributed and latent representations (LLM embeddings, latent protocols like "DroidSpeak", "Coconut"-style communication),
* hybrid ReAct‑style agent loops

can all be treated as different species operating over the same `U.EpistemeSlotRelation`. There is a bias towards making these operational differences **explicit** instead of hiding them behind "the model".

**Viewpoint and stakeholder bias.**
The pattern leans on the ISO‑style idea that viewpoints encode **stakeholder concerns and role‑families**, but it generalises this beyond architecture. `U.Viewpoint` is intentionally context-local and not bound to any single discipline; still, the examples are skewed toward engineering and epistemic use‑cases.

**Didactic bias.**
The pattern is written to be teachable: semantic triangles are kept as didactic projections; examples like stools on lab rigs, services and SLAs, and model‑evaluation epistemes are deliberately simple. This may under‑represent more exotic epistemes (e.g. artistic, law-domain, or socio‑technical ones), but the intention is that these use the same slots with different species‑level constraints.

### C.2.1:11 - Conformance Checklist  *(normative)*

**CC‑C.2.1‑1 - Minimal core components for episteme species.**
Any species of `U.Episteme` that participates in the boundary between `EntityOfConcern` and Description episteme discipline, specification use and refinement, or E.17 multi-view and publishing **MUST** be representable as `U.EpistemeCard` or `U.EpistemeView` with at least:

```
content            : U.ClaimGraph
entityOfConcernRef : U.EntityRef
groundingHolonRef? : U.HolonRef
viewpointRef?      : U.ViewpointRef
referenceScheme?   : U.ReferenceScheme      // ByValue
meta               : ...                      // edition, provenance, status (A.7 and F.15)
```

and corresponding SlotSpecs consistent with A.6.5 (`EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`).

**CC‑C.2.1‑2 - No durable U-kind for “EntityOfConcern” or “GroundingHolon”.**
Patterns **MUST NOT** introduce durable U-kinds `U.EntityOfConcern` or `U.GroundingHolon`:
* EntityOfConcernSlot has ValueKind `U.Entity` ( species‑constrained via EntityOfConcernClass if needed),
* GroundingHolonSlot has ValueKind `U.Holon`.

Plain terms "EntityOfConcern value" and "grounding holon" are allowed only as **slot-filler descriptions** under the declared SlotKind, ValueKind, and RefKind discipline.

**CC-C.2.1-3 - SlotKind, ValueKind, and RefKind discipline.**
All episteme‑related slots, including `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot` (and any extensions in C.2.1+), **MUST**:
* follow the naming discipline of A.6.5 (`*Slot` for SlotKinds, `*Ref` only for RefKinds or fields),
* declare a ValueKind and refMode (`ByValue` or a RefKind),
* be used consistently across patterns that refer to the same conceptual position.

**CC‑C.2.1‑4 - DescriptionContext wiring.**
Any episteme species whose name or pattern claims to be a `…Description` or `…Spec` in the sense of E.10.D2 **MUST**:
* expose `subjectRef : U.SubjectRef`,
* provide a decoding to `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`,
* ensure that `EntityOfConcernRef` matches `entityOfConcernRef` (EntityOfConcernSlot), and
* ensure that `ViewpointRef` matches `viewpointRef` or is derivable from a `U.ViewpointBundle` under documented rules.

**CC‑C.2.1‑5 - Morphism declarations over slots.**
Any pattern in A.6.2–A.6.4, E.17, E.18, or discipline packs that defines morphisms between epistemes **SHALL**:
* state whether it is a species of `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, or `U.EpistemicRetargeting`,
* declare its `entityOfConcernChangeMode` (`preserve` or `retarget`),
* name which SlotKinds it reads and writes,
* state its behaviour on `entityOfConcernRef`, `groundingHolonRef`, `viewpointRef`, and `referenceScheme`.

**CC-C.2.1-5a - Episteme and publication relation-position split for semio-facing terms.**
Any pattern, publication-form profile, evidence-use note, or FPF-facing term that uses pre-FPF sign vocabulary, explanation, publication, source cues, authority-looking cases, or reader reliance **MUST** name the claim-bearing value as `U.Episteme`, `U.EpistemePublication`, or a declared species of `U.Episteme`. When publication is current, it **MUST** separately name the publication form, `U.View` or MVPK face, carrier or rendering, source-finding cue, and either `governingPatternRef` or `authoritySourceRef` when interpretation or use depends on a named authority reference. It **MUST NOT** use generic semio wording, generic source wording, generic project-work wording, or container-placement wording as solution terms.

**CC-C.2.1-6 - Semantic-triangle usage guard.**

If a semantic triangle or parallelogram diagram appears in a pattern or tutorial, there must be an explicit note that:
* it is a didactic projection of `U.EpistemeSlotRelation`, and
* normative laws are stated in terms of C.2.1 slots, graph-valued fillers such as `ClaimGraph`, and morphisms, not in terms of triangle corners.

**CC-C.2.1-7 - KD-CAL and ReferencePlane alignment.**
Any pattern that evaluates or compares epistemes (KD-CAL, LOG-CAL, CHR, CG-Spec, etc.) **MUST** point out:
* how `U.ClaimGraph` is interpreted in a ReferencePlane,
* how `GroundingHolonSlot` figures into measurement or validation,

**CC‑C.2.1‑8 - Context locality and Bridges.**
Any `U.Episteme` species that is consumed by KD-CAL, LOG-CAL, or CHR-based patterns **SHALL** declare a `U.BoundedContextRef`; all F-G-R computations and C.2.1 slot interpretations are **context-local**. Cross-context use **MUST** proceed via an explicit Bridge with CL and Phi-policy (F.9 and B.3), with penalties applied to the R component only; F and the slot structure from C.2.1 remain unchanged.

**CC‑C.2.1‑9 - Carriers and Work outside episteme content.**
C.2.1 **inherits** the current A.7 strict distinction plus C.2.1 slot-relation, E.17 publication and carrier, A.10 evidence-use and provenance, B.3 assurance, A.2 and A.2.1 role-assignment, A.15 work, and A.3.4 transformation discipline: `U.PresentationCarrier` values, publication-side values, `U.Work` occurrences, and role assignments **MUST NOT** be treated as parts of `U.Episteme` or as values of any SlotKind in `U.EpistemeSlotRelation`. Episteme content stays in `U.ClaimGraph` and `U.ReferenceScheme`; evidence enters only through an A.10 evidence-provenance graph relation or B.3 assurance-evidence input that points to evidence-producing or evidence-interpreting `U.Work` occurrences, carrier and source-currentness records, and role assignments when those are current. Changing carriers or re-publishing work alone does **not** change the episteme determined by the filled `content`, `entityOfConcernRef`, and effective `referenceScheme` positions in its `U.BoundedContext`.

**CC‑C.2.1‑10 - Reflexive entityOfConcern guard.**
When an episteme uses C.2.1 to speak **about** another episteme (ReferencePlane = episteme), or about itself (self-describing or meta-specification cases), patterns **SHALL** ensure that the resulting JustificationGraph and evaluation chains are **acyclic** along justification paths. Reflexive `describe` or citation edges may exist as literature references, but they MUST NOT form minimal justification cycles for acceptance or KD-CAL assurance decisions; the trust calculus MUST always bottom out in separated evidence relation material, such as evidence-producing or evidence-interpreting `U.Work` plus an A.10 evidence-provenance graph relation or B.3 assurance-evidence input, rather than in purely self-referential claims.

### C.2.1:12 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Carrier-as-episteme | A PDF, diagram, dashboard, repository, or database row is treated as the episteme itself. | Separate `U.Episteme`, `U.EpistemePublication`, publication face, carrier, and source relation. |
| EntityOfConcern drift | The thing being described changes while the same episteme label is kept. | Name the `EntityOfConcernSlot` value and any `EntityOfConcernChangeMode` explicitly. |
| View and viewpoint collapse | A view is treated as the stakeholder concern, or the viewpoint is treated as the view content. | Keep `ViewpointSlot` and `ViewSlot` distinct and use E.17 for multi-view publication. |
| Triangle-as-ontology | Symbol-Concept-Object is used as the normative episteme model. | Treat the triangle only as a didactic projection of `U.EpistemeSlotRelation`. |

### C.2.1:13 - Consequences  *(informative)*

**Benefits**
* **Single, extensible episteme core.**
  C.2.1 gives a small, stable set of positions (EntityOfConcern, GroundingHolon, ClaimGraph, Viewpoint, View, ReferenceScheme) and components (`U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication`) on which all higher‑level patterns depend. This avoids the proliferation of “epistemic objects” and “facets” with overlapping semantics.
**Transparent EntityOfConcern & grounding discipline.**
  The pair (`EntityOfConcernSlot`, `GroundingHolonSlot`) is no longer hidden inside ad-hoc “SubjectRef” fields or semantic triangles: both are explicit, typed slots. This makes retargeting, viewing and correspondence laws (A.6.2–A.6.4, E.17.0) easier to state and check.
* **Better fit for contemporary representation practice.**
  By distinguishing ClaimGraph, RepresentationScheme, Tokens, Carriers and Operations (in C.2.1+), the pattern matches contemporary SoTA views of notation and formalism:
  * formal languages as cognitive tools and de-semanticisation techniques (Novaes),
  * operational iconicity and medium‑sensitive reasoning (Krämer, Malafouris),
  * hybrid symbolic-neural reasoning methods (e.g. ReAct, tool-augmented LLMs, latent protocols).
  FPF can model both symbol-heavy and latent-heavy reasoning methods without privileging either.
* **Uniform substrate for multi‑view description and publication.**
  MultiViewDescribing, viewpoint bundles (TEVB), and MVPK all land on the same episteme core. This avoids the current “views vs viewpoints vs faces” confusion and leaves “architecture” as a domain‑specific specialisation rather than a competing meta‑ontology.
* **Tooling alignment.**
  Slot discipline plus explicit episteme components map cleanly to implementation types (records, row‑typed schemas, effectful handlers). Tools can generate code, schemas or telemetry from episteme species without guessing what “subject”, “context” or “object” mean.

**Trade-offs and costs**
* **More explicit structure.**
  Pattern users and authors must declare slots, ValueKinds and references explicitly, and keep DescriptionContext consistent. This is more upfront work than writing ad-hoc "Subject" or "Object" fields, but it pays off in substitution safety and cross-pattern reuse.
* **Repair effort.**
  Uses of “EpistemicObject”, “Facet”, “Subject”/“Object”, and raw `...Ref` fields need repair into C.2.1 slots + A.6.5 SlotSpecs when the claim is current. Current prose uses the selected C.2.1 slots and A.6.5 SlotSpecs directly; such wording is source material for repair, not a current alternate vocabulary.
* **Exposure of representation biases.**
  Being explicit about RepresentationSchemes and Operations may make disagreements visible about which representations are "primary" in a team or discipline. C.2.1 does not resolve these disagreements; it only makes them visible and therefore debatable.

### C.2.1:14 - Rationale

The rationale for C.2.1 is that modern epistemic work is not adequately captured by one Object, Concept, and Symbol triangle. Engineering specifications, formal theories, simulation models, dashboards, proof states, LLM-assisted reasoning traces, and architecture descriptions all need a common way to say what the episteme is about, how its claims are grounded, what claim graph it carries, which viewpoint or view is current, and which reference scheme makes claims readable.

### C.2.1:14.1 - SoTA-Echoing

C.2.1 echoes current work on formal languages as cognitive tools, operational iconicity of notations, material engagement, distributed representations, and tool-augmented reasoning by giving FPF a slot relation rather than one notation-bound representation model. The SoTA implication is practical: graph-valued claim and justification structures stay graph-valued, while the episteme core stays a typed n-ary slot relation that can be viewed through tuple or graph lenses only when C.29 makes that lens explicit.

### C.2.1:15 - Relations  *(overview)*

**Builds on**
* A.1 `U.Holon` — for treating episteme as a holon with components.
* A.6.0 `U.Signature` — for interpreting episteme kinds as n‑ary relations over slots.
* A.6.5 `U.RelationSlotDiscipline` - for SlotKind, ValueKind, and RefKind discipline over episteme slots.
* A.7, E.10.D2 - for the boundary between `EntityOfConcern` and Description episteme discipline, specification use and refinement gates, and the interpretation of `subjectRef` as DescriptionContext.
* C.2 (KD‑CAL, LOG‑CAL) — for ClaimGraph semantics, ReferencePlanes, and Bridges.
* E.8, E.10 — for pattern authoring discipline and lexical guards.

* **Constrains**
* A.6.2–A.6.4 — by fixing the minimal episteme component set those morphisms operate on and by requiring an explicit **EntityOfConcernChangeMode characteristic** (`entityOfConcernChangeMode ∈ {preserve, retarget}`) over `EntityOfConcernSlot`/`GroundingHolonSlot`.
* E.17.0–E.17.2 — by specifying how `EntityOfConcern`, `Viewpoint`, `View` and ReferenceSchemes are represented at episteme level.
* E.17 (MVPK) — by separating `U.View` (episteme) from `U.PresentationCarrier` (publication carrier), and by requiring that publication morphisms be `U.EpistemicViewing` species over C.2.1‑conformant views.
* F.18 (LEX-BUNDLE) - by providing the episteme-specific name cards and guards for EntityOfConcern, GroundingHolon, Viewpoint, View, ReferenceScheme, and their SlotKinds.

**Used by**
* A.6.2 `U.EffectFreeEpistemicMorphing` - as the default episteme slot and value structure for episteme-to-episteme transforms.
* A.6.3 `U.EpistemicViewing` — as the substrate for entityOfConcern‑preserving projections (views).
* A.6.4 `U.EpistemicRetargeting` — as the substrate for EntityOfConcern-bundle retargeting transforms between epistemes (Ep→Ep with `entityOfConcernChangeMode = retarget`).
* E.17.0 `U.MultiViewDescribing`, E.17.1, E.17.2 — to organise families of Description epistemes, including Description epistemes admitted for specification use, under Viewpoints and `EntityOfConcernClass` constraints.
* E.17 (MVPK) — to publish episteme views through publication faces, publication forms, and carriers.
* E.18 - to interpret StructuralReinterpretation and other engineering projections as episteme morphisms over a well-typed `U.EpistemeSlotRelation`.

Together, these relations make `U.EpistemeSlotRelation` the **single normative core** for thinking about epistemes, their EntityOfConcern mapping, their representations, and their transformations across FPF.

### C.2.1:End

