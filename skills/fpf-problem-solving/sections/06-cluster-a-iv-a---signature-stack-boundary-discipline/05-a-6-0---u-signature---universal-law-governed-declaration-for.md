## A.6.0 - U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind
> **Status:** Stable
> **Type:** Definitional ontic pattern

**Status.** Architectural pattern, kernel‑level and universal.
**Placement.** Part A (Kernel), **before A.6.1** (“U.Mechanism”).
**Builds on.** **A.2.6** (USM: context slices and scopes), **E.8** (pattern form and section order), **E.10** LEX-BUNDLE (registers, naming, stratification), **E.10.D1** D.CTX (Context discipline).

**Coordinates with.** **A.6.1** (U.Mechanism), **A.6.5** (`U.RelationSlotDiscipline` for n-ary arguments), **E.5.3** (Unidirectional Dependency), **E.10** (LEX-BUNDLE), and **Part F** (harnesses and cross-context transport; naming). Conformance keywords: RFC 2119.

### A.6.0:0 - Use and boundary

Use this pattern when you need to publish or check a reusable `U.Signature` declaration for a theory, mechanism family, method family, discipline vocabulary, `U.Signature(profile=FormalSubstrate)`, or `PrincipleFrame`, and the current question is: what subject kind is declared, over what ranged value kind, with which vocabulary, laws, and applicability?

Do not use this pattern when the claim being made is that some implementation runs, a handler realizes an effect, a method is authorized for work, a gate has passed, evidence supports a result claim, a measurement is comparable, or a bridge preserves enough structure across contexts. Those claims use A.6.1, A.15, gate, evidence, characterization, normalization, bridge, or decision patterns after the signature declaration is stable.

First useful move: write the four-row Signature Block before writing examples or realizations: `SubjectBlock`, `Vocabulary`, `Laws`, `Applicability`. Then add a `SignatureManifest` only when another signature imports this one or downstream text depends on its exported symbols.

What goes wrong if missed: a project may treat implementation detail, tutorial prose, bridge policy, measurement comparability, or handler behavior as if it were part of the public declaration. That makes reuse brittle because downstream work cannot tell what law is being reused and what later realization merely happened to satisfy it.

What this buys: the same declaration shape can be reused for mechanisms, methods, disciplines, `U.Signature(profile=FormalSubstrate)` declarations, and principle frames, while realizations, measurements, bridges, and work authorization stay in their own governing patterns.

### A.6.0:1 - Problem frame

FPF already uses “signatures” to stabilise public promises of **reusable extension vocabularies** and, via **A.6.1**, of **mechanisms**. But declaration publishers also need stable, minimal declarations for **theories**, **methods** (operational families), and **disciplines** (regulated vocabularies). Without **one** universal notion of signature:
* similar constructs proliferate under incompatible names;
* practitioners cannot tell what is **declared** (EntityOfConcern kind and laws) versus what is **realized** or admitted for specification use;
* cross-context reuse lacks a canonical place to state **applicability** and **declared admissible vocabularies**.

E.8 demands one publication voice and section order; E.10 demands lexical discipline across strata. A.6.0 provides the common kernel shape these patterns presuppose.

### A.6.0:2 - Problem

If each family (theories, mechanisms, methods, disciplines) invents its own “signature”:

1. **Tight coupling.** Private definitions leak as public standards, breaking substitutability.

2. **Lexical drift.** The same lexical label (e.g., *scope*, *normalization*) hides different laws.

3. **Scope opacity.** Applicability (where the words mean what) remains implicit, violating D.CTX.

### A.6.0:3 - Forces

| Force | Tension |
| --- | --- |
| **Universality vs. fitness** | One shape must fit **Kernel**, **Mechanisms**, **Protocols**, and other specialised signatures, without over‑committing to any one family. |
| **EntityOfConcern vs. specification use** | Signatures declare **the subject kind and laws**, not recipes or test harnesses. |
| **Simplicity vs. expressivity** | Keep the kernel small while allowing family-specific header metadata and usable projections (e.g., `imports` and `provides` DAGs, assurance matrices, transport views). |
| **Locality vs. transport** | Meaning is context‑local (D.CTX); transport must remain explicit and auditable (Part F) without smuggling implementation. |

### A.6.0:4 - Solution — **Define `U.Signature` once, reuse everywhere**

**Definition.** A **`U.Signature`** is a **public, law-governed declaration** for a named **SubjectKind** over a declared **RangedValueKind**. The Signature **SHALL** expose an explicit **SliceSet** and **ExtentRule**; if quantification is context-independent, the declaration **MUST** use a trivial `SliceSet` (e.g., a singleton) and a constant `ExtentRule` rather than omitting these fields. A Signature (i) introduces a **vocabulary** (value kinds, relations, operators), (ii) states **laws** (axioms and invariants; no operational admissions), and (iii) records **applicability** (where and under which contextual assumptions the declarations hold). Dependencies (**imports**) and exported names (**provides**) are declared in a `SignatureManifest` (see §4.4.1) and are **not** part of the four-row Signature Block. **Discipline for argument-position typing is delegated to A.6.5 `U.RelationSlotDiscipline`: whenever the Vocabulary declares an n-ary relation or operator, SlotSpecs for its parameter positions SHALL be provided as in §4.1.1 and A.6.5.**

Where the **Vocabulary** introduces an **n‑ary relation or morphism**, the Signature **SHALL**, for each parameter position `i`, declare a `SlotSpec_i = ⟨SlotKind_i, ValueKind_i, refMode_i⟩` as defined in **A.6.5 `U.RelationSlotDiscipline`**. SlotSpecs live inside the per‑relation parameter block of the **Vocabulary** row and **MUST NOT** introduce additional rows beyond the four‑row Signature Block.

**Arrow form (typing for MVPK).** Express a Signature as a **morphism**
`SigDecl : ⟨SubjectBlock⟩ → ⟨Vocabulary × Laws × Applicability⟩`
where `SubjectBlock = ⟨SubjectKind, RangedValueKind, SliceSet, ExtentRule, ResultKind?⟩`. This makes `U.Signature` directly consumable by **E.17 MVPK** (publication of morphisms) without adding semantics on faces (no new claims; pins for any numeric content).

*Guard clarification (normative).* **Operational guard predicates** (run‑time or admission guards) **BELONG ONLY** to **A.6.1 Mechanisms**. A Signature may express **domain and type constraints** as declaration-level constraints (e.g., restricting an operator’s domain) but **SHALL NOT** encode operational admissions.

*Guidance for `profile=FormalSubstrate` signatures.* Signatures that declare a formal-deductive profile (e.g., *FormalSubstrate*) MAY include, **as vocabulary elements**, an **EffectDiscipline** (algebraic, row, or graded effect signatures) and **InferenceKind** enumerations; handler semantics are **out of scope** for Signatures (see §4.3). The universal block remains conceptual and contains **no** run-time admissions or AdmissibilityConditions.

**Naming discipline.** The `Subject` **MUST** be a **single‑sense** noun phrase; avoid synonyms or aliases within the same Signature.

A `U.Signature` is conceptual: it contains no implementation, no packaging or CI metadata, and no Γ-builders. If a family wants to expose a Γ‑like *builder or aggregator*, publish it **outside** the Signature Block (typically as an **A.6.1** Mechanism‑level operator) and **namespace** it under the Signature id; do not treat Γ as part of the canonical Vocabulary.

#### A.6.0:4.1 - The **Signature Block (universal form)**

The **four conceptual rows** (“SubjectBlock, Vocabulary, Laws, and Applicability”) give a repeatable, holon‑stable pattern across mathematics → physics → engineering:
* **SubjectBlock** = *what it’s about + how quantified* (axiomatics + domain of interpretation),
* **Vocabulary and Laws** = *principles and laws* (postulates and constraints),
* **Applicability** = *where they hold in practice* (bounded context and time).

Every `U.Signature` **SHALL** present a **four‑row conceptual block** (names are universal; family-specific projections are stated below):

1. **SubjectBlock** — ⟨**SubjectKind**, **RangedValueKind**, **SliceSet**, **ExtentRule**, **ResultKind?**⟩.
   *SubjectKind* names the EntityOfConcern kind declared by the signature (C.3); *RangedValueKind* names the kind of values or entities ranged over through C.3 typed reasoning, admitted U-kind governance, Concept-Set evidence, or an imported signature symbol; *SliceSet* addresses the quantification domain (USM; e.g., **ContextSliceSet**); *ExtentRule* computes `Extension(SubjectKind, slice)` (C.3.2); *ResultKind?* (optional) is the output kind when outputs differ from the SubjectKind.
   **Editorial split (allowed).** Authors **MAY** render the **SubjectBlock** as two adjacent lines — **Subject** *(SubjectKind, RangedValueKind)* and **Quantification** *(SliceSet, ExtentRule, ResultKind?)* — **without changing semantics**. Even when visually split, SubjectBlock counts as **one** conceptual row.

   **Semantic functions of the SubjectBlock kinds (informative)**
   * **SubjectKind (EntityOfConcern kind).** The EntityOfConcern kind declared by the signature (C.3.1), ordered by `⊑`. It carries no Scope.
   * **RangedValueKind (ranged-over value kind).** The value kind over which values or entities are ranged. It is not a separate durable kind or type ontology; use C.3 `U.Kind`, an admitted durable U-kind, a Concept-Set row, or an imported signature symbol as the meaning source.
   * **SliceSet (addressability).** The addressable set of `U.ContextSlice`s (USM). It identifies where **extent** is computed; it is not a “space” unless CHR.
   * **ExtentRule (extent).** A rule yielding `Extension(SubjectKind, slice)` (C.3.2); this is the quantifier’s domain, computed per slice.
   * **ResultKind? (outputs).** Optional: the output kind for operations declared in *Vocabulary* (use when outputs differ in kind from the SubjectKind).

2. **Vocabulary** — names and sorts of the public **types, relations, and operators** this signature commits to (no handler semantics; no AdmissibilityConditions). For each **n‑ary relation or morphism** in the Vocabulary, parameters **SHALL** be declared via **SlotSpecs** `SlotSpec_i = ⟨SlotKind, ValueKind, refMode⟩` per **A.6.5 `U.RelationSlotDiscipline`**. SlotKinds and RefKinds **MUST** follow the `…Slot` and `…Ref` lexical discipline in **A.6.5** and **E.10 (LEX‑BUNDLE)**; ValueKinds **MUST** remain free of these suffixes.
   (No additional rows beyond the four‑row Signature Block.)

3. **Laws (Axioms and Invariants)** — equations and order and closure laws that are context‑local truths under the stated Applicability (no proofs here). **Operational guard predicates belong to Mechanisms (A.6.1)**, not to Signatures.

4. **Applicability (Scope and Context)** — conditions under which the laws are valid (bounded context, plane, stance, time notions). Applicability **MUST** bind a **`U.BoundedContext`** (D.CTX). Applicability here is the *context of meaning* for the Signature’s vocabulary and laws; it **MUST NOT** be used to encode claim‑level applicability, which remains a **Scope** on claims (`USM` and `C.3.2`). Cross‑context use **MUST NOT** be implicit; if intended, **name** the Bridge (conceptual reference only). When numeric comparability is implied, **bind** legality to **CG‑Spec and MM‑CHR** (normalize‑then‑compare; lawful scales and units).

*Mapping to existing families (normative projection correspondences).*
— **A.6.1 (Mechanism).** *SubjectBlock* ↔ **SubjectKind, RangedValueKind, and the remaining SubjectBlock fields**; *Vocabulary* ↔ **OperationAlgebra**; *Laws* ↔ **LawSet**; *Applicability* remains contextual; **AdmissibilityConditions** — separate field of mechanism (not in the `U.Signature`).
— **Task, Problem, and Discipline signatures (C.22, G-cluster).** These **SHALL** be introduced as **species of `U.Signature`** that reuse the same four-row Block (SubjectBlock, Vocabulary, Laws, and Applicability); any extra per-family views are projections only (no new conceptual rows).

*Optional projection views (normative).* Publications MAY include additional **projection views** (e.g., a Dependency View listing `imports` and `provides`, or an Assurance View listing audit and evidence hooks), but such views:
1) MUST be mechanically derivable from `SignatureManifest` + the four‑row Block (and referenced ClaimIds where used), and
2) MUST NOT introduce new semantics, obligations, or “extra rows”.

##### A.6.0:4.1.1 - SlotSpec for argument positions (normative; see A.6.5)

For every **n‑ary relation or operator** declared in the **Vocabulary** row, the Signature **SHALL** assign, to each argument position, a **SlotSpec** triple:

```text
SlotSpec_i := ⟨SlotKind_i, ValueKind_i, refMode_i⟩
```

where:
* **SlotKind_i** is a named position in the relation or operator (Tech name with `…Slot` suffix) whose semantics are documented (see A.6.5).
* **ValueKind_i** is the FPF kind of admissible values at that position: a C.3 `U.Kind`, an admitted durable U-kind, a direct governing-pattern value kind, or an imported signature symbol.
* **refMode_i** is either `ByValue` or a **RefKind** (e.g., `U.EntityRef`, `U.HolonRef`), indicating whether the episteme stores values directly or references or identifiers.

Full discipline and lexical rules for **SlotKind, ValueKind, and RefKind** are given in A.6.5 `U.RelationSlotDiscipline` and E.10 (§8.1). A.6.0 requires that every vocabulary‑level relation or operator that takes arguments **declare** these SlotSpecs; downstream patterns MAY provide templates for common shapes (e.g., episteme slots in C.2.1).

**Settlement for the `U.*` names in this example.** The example below does not admit new durable U-kinds. Names ending in `Ref`, such as `U.MethodRef`, `U.EntityRef`, `U.CharacteristicRef`, and `U.HolonRef`, are RefKind examples governed by A.6.5 and the direct pattern for the referenced value. `U.ClaimGraph` is used only as a ValueKind for `ClaimGraphSlot`, governed by the episteme slot relation in C.2.1 and A.6.5. A.6.0 only requires the SlotSpec form; if a project needs a new durable `U.*` value, E.24.UK and the direct governing pattern must admit it outside this signature example.

**Mini‑example (informative).** For an episteme kind `ModelEvaluationResultKind`, a simplified episteme might expose:
* `entityOfConcernRef : U.MethodRef`
* `datasetRef : U.EntityRef`
* `metricRef : U.CharacteristicRef`
* `groundingHolonRef : U.HolonRef`
* `claimGraph : U.ClaimGraph`

A SlotSpec table then states:

| Parameter (episteme field)   | SlotKind              | ValueKind          | refMode                |
| ---------------------- | --------------------- | ------------------ | ---------------------- |
| `entityOfConcernRef`   | `EntityOfConcernSlot` | `U.Method`         | `U.MethodRef`          |
| `datasetRef`           | `DatasetSlot`         | `U.Entity`         | `U.EntityRef`          |
| `metricRef`            | `MetricSlot`          | `U.Characteristic` | `U.CharacteristicRef`  |
| `groundingHolonRef`    | `GroundingHolonSlot`  | `U.Holon`          | `U.HolonRef`           |
| `claimGraph`           | `ClaimGraphSlot`      | `U.ClaimGraph`     | `ByValue`              |

This example illustrates the intended interpretation: **parameters are typed twice**—once by their **ValueKind** (what sort of value fills the position) and once by **refMode** (by‑value or which RefKind). SlotKinds (with `…Slot` suffix) give stable names for substitution laws and EntityOfConcern statements across patterns.

#### A.6.0:4.2 - Profile specialisations (normative; structure‑preserving)
To enable first‑principles signature specializations without minting new Kernel kinds, apply **profiles** to `U.Signature`:

* **`profile = FormalSubstrate`** — *formal‑deductive specialization*
  **Vocabulary:** `TermRegister` (ref-only), **InferenceKinds** (ref-only), **EffectDiscipline** (operation and effect signatures).
  **Laws:** equational and structural axioms of the calculus; **no handler semantics**.
  **Applicability:** binds a `U.BoundedContext` for conceptual declaration use; **no units, ReferencePlane, or Transport** on faces.
  **MVPK pins:** **`No‑Realization` pin (mandatory)** on `PlainView` and `TechCard` asserting that handler semantics live only in **A.6.1 `U.Mechanism::U.EffectRealization`**.
  **Faces:** On MVPK faces, **`InferenceKindsAllowed`** MAY present a **ref‑only subset** of the enumerated **`InferenceKinds`**; Signatures do not add handler semantics.

* **`profile = PrincipleFrame`** — *postulates + measurability intent (CHR‑binding)*
  **Vocabulary:** **PostulateSet** (in the calculus imported), **CHR-Binding presence** (ref-only to characteristic or observation profiles), **Ontology references** (ref-only to ontology types or morphisms used to name subject-matter entities).
  **Laws:** timeless and order-free invariants; **no operational admissions**.
  **Applicability:** binds a `U.BoundedContext`; **Signatures SHALL NOT publish units, ReferencePlane, ComparatorSet, or Transport** (first mention is in **UNM**).
  **MVPK pins:** **`NoReferencePlaneOnSignature`** and **`UNM-priority`** (units, planes, comparators, and Transport are declared only by **`U.ContextNormalization`** and cited by edition or ref-id where needed). Do not mint profile-local pin synonyms.

**Profile morphism discipline.** See §4.6 for the **structure‑preserving morphism** requirements for profile application.

#### A.6.0:4.3 - Effect-discipline and handler-semantics split (normative)

If a Signature’s **Vocabulary** includes an **EffectDiscipline** (operation and effect signatures), the Signature **SHALL NOT** declare **handler semantics** or any **EffectRealization**. Such realizations are declared only under **A.6.1 `U.Mechanism`** and cited by **ref-id** on faces where needed. This mirrors the modern algebraic-effects separation between *operation signatures* and *handlers* while keeping A.6.0 purely conceptual.

#### A.6.0:4.4 - Declaration Rules (strict-distinction-aware; lexically disciplined)

* **EntityOfConcern, Description, and specification-use separation.** A signature states the subject kind and laws; Realizations (if any) carry specification-use constraints. Do not mix tutorial text or operational recipes into the Block. Do **not** include **AdmissibilityConditions** or run‑time admissions here.
* **Context discipline.** Bind Applicability to a **`U.BoundedContext`**. If cross‑context use is intended, **name** the crossing and **reference** the Bridge (Part F and B.3); A.6.0 does **not** prescribe **compatibility and loss tables (CL, including `CL^plane`)** or penalty formulas.
* **Stratification.** Use LEX‑BUNDLE registers and strata; do not redefine Kernel names in lower strata (no cross‑bleed).
* **Signature manifest.** If the signature is intended to be imported or reused, publish a `SignatureManifest` immediately above the Block with explicit `id`, `imports`, and `provides` lists (§4.4.1). Keep the universal four‑row Block free of dependency and export metadata.

* **Realization discipline (normative extension point).** If a family publishes any *Realization* of a `U.Signature`, each Realization **MUST** (i) declare which `SignatureId` it implements, (ii) satisfy the Signature’s **Laws** (and imported laws) and **MAY** tighten them but **MUST NOT** relax them, and (iii) treat imported Signatures as **opaque**—it **MUST NOT** depend on their internal structure beyond what is exported via `provides` and cited via ClaimIds. Realization-specific build, tooling, and test metadata belongs to the Realization record or publication, not to the `U.Signature` Block.

##### A.6.0:4.4.1 - SignatureManifest (imports and provides; normative)

A `U.Signature` MAY be prefixed with a lightweight manifest that makes boundary dependencies explicit **without** introducing a separate “module system”.

**SignatureManifest** fields (conceptual; concrete syntax is editorial):

- `id : SignatureId` — stable identifier for cross-references.
- `version : SemVer` (optional; **required when the signature is imported or reused**).
- `publicationState : {draft | candidate | stable | deprecated}` (optional).
- `imports : [SignatureId]` — other signatures whose **provides** are referenced by this signature (directed edges; possibly empty).
- `provides : [SymbolId]` — the **only** new public symbols minted by this signature that downstream text may depend on (**types, relations, operators, SlotKinds, RefKinds**).

**Norms (boundary hygiene):**

- **Acyclicity.** The directed graph induced by `imports` MUST be acyclic.
- **Stratum dependency.** `imports` **MUST** respect **E.5.3** (Unidirectional Dependency) and **E.10** strata and token-class discipline; do not import from a lower stratum or across a forbidden dependency direction.
- **No redeclare.** `provides(S)` MUST NOT re‑declare any symbol already provided by any transitive import of `S`.
- **No ghost dependencies (vocabulary symbols).** Any non-Kernel **SymbolId** referenced in the **SubjectBlock** or **Vocabulary** rows (including `RangedValueKind`, `ResultKind?`, operator names, SlotKinds, ValueKinds, RefKinds) that is **not** provided by this signature MUST be provided by some imported signature. ClaimIds, BridgeIds, policy-ids, and EditionIds are exempt because they identify claims, bridges, policies, or editions rather than vocabulary symbols exported by this Signature.
- **Law reference.** When downstream text depends on laws or constraints from an imported signature, it SHOULD cite the corresponding **ClaimId** (A.6.B), not paraphrase prose.

The A.6.0 four-row Block remains the canonical meaning locus for Vocabulary, Laws, and Applicability. The manifest only declares dependency edges and exported names.

* **Token hygiene.** Do **not** mint new `U.*` tokens inside a Signature without an accepted FPF naming and kind decision; prefer referencing existing governed U-kinds, C.3 `U.Kind` values, Concept-Set rows, or imported signature symbols.

*MVPK publication discipline for Signatures (normative).* When publishing a `U.Signature` via MVPK (E.17), faces **SHALL** be typed projections that add **no new claims**; any numeric or comparable statement **MUST** pin unit, scale, reference-plane, and **EditionId** to **CG-Spec and MM-CHR** where applicable. For `profile=FormalSubstrate` signatures, faces **MUST** carry a **No-Realization pin** (handlers and realizers absent). For Principle-level signatures, faces **MUST NOT** introduce units, ReferencePlane, or Transport (first mention occurs in UNM).

#### A.6.0:4.5 - Specialisation knobs (for downstream patterns)

A.6.0 exposes **three** conceptual knobs; downstream patterns (A.6.1, method or discipline specifications) may **tighten** them:

1. **Builder policy.** The Block MUST NOT export Γ-builders. If a family publishes a Γ-like builder or aggregator, it MUST be outside the Block (typically as an **A.6.1** Mechanism-level operator), explicitly marked optional, and namespaced under the Signature id.

2. **Transport clause.** If cross-context or cross-plane use is part of the design, the signature **may declare** a conceptual Transport clause; **A.6.1** gives a concrete schema (Bridge, **CL, CL^k, and CL^plane**; Bridges per **F.9**, penalties per **B.3**, **CL^plane** per **C.2.1**), but A.6.0 remains agnostic about penalty shapes.

3. **Morphisms.** Families may define `SigMorph` (refinement, conservative extension, equivalence, quotient, product) to relate signatures; **A.6.1** instantiates this for mechanisms. Where such morphisms, or downstream **substitution and retargeting** laws (e.g., **A.6.2–A.6.4**), act on **n‑ary relations or morphisms**, they **SHALL** express their access, update, and retargeting discipline in terms of **SlotSpecs**  (SlotKind, ValueKind, RefKind) rather than unnamed parameter indices, using **A.6.5 `U.RelationSlotDiscipline`** as the normative slot calculus.

#### A.6.0:4.6 - Profile‑specialisation as a structure‑preserving morphism (normative)
Profile application `ι_profile : U.Signature → U.Signature(profile=…)` **SHALL** be a **structure‑preserving morphism**:
— **SubjectBlock** is preserved up to α-renaming (SubjectKind and RangedValueKind unchanged; ResultKind? only added when it exists in the universal intent).
— **Vocabulary** is **monotone** (adds or refines names and sorts without contradicting existing ones).
— **Laws** are **monotone** (add or strengthen axioms; never weaken).
— **Applicability** is **restrictive** (binds or tightens `U.BoundedContext`; never widens implicitly).
— No **AdmissibilityConditions**, **operational guards**, or **handler semantics** are introduced by the profile (those live under **A.6.1**).
This makes `profile=FormalSubstrate` and `profile=PrincipleFrame` *morphisms* in the sense of kernel specialisation and enables SigMorph reasoning (refinement or conservative extension).

### A.6.0:5 - Archetypal Grounding (Tell–Show–Show)

| quartet Element | `U.System` Example — **Grammar of Motions** | `U.Episteme` Example — **Normalization Family** |
| --- | --- | --- |
| **SubjectBlock** | **Subject:** SubjectKind=`MotionGrammar`; RangedValueKind=`U.System:TrajectorySpace`. **Quantification:** SliceSet=`ContextSliceSet`; ExtentRule=`admissible motion words per slice (kinematics and domain restrictions)`; ResultKind?=`Language[Segment]`. | **Subject:** SubjectKind=`NormalizationMethod-Class`; RangedValueKind=`U.Episteme:ChartFamily` (one `U.BoundedContext`). **Quantification:** SliceSet=`ContextSliceSet`; ExtentRule=`admissible method instances per slice (edition and validity)`; ResultKind?=`NormalizedChart`. |
| **Vocabulary** | Types: `Pose`, `Segment`; Operators: `concat`, `reverse`, `sample` (any Γ‑like aggregator is published outside the Signature Block, typically as a Mechanism‑level operator namespaced under the Signature id). | Operators: `apply(method)`, `compose`, `quotient(≡)`. |
| **Laws (Invariants and Constraints)** | Closure of `concat`; associativity; time-monotone sampling; **`reverse` is declared only for holonomic arms (domain restriction)**. | Ratio→positive-scalar; Interval→affine; Ordinal→monotone; Nominal→categorical; LUT(+uncertainty). |
| **Applicability (Scope and Context)** | Context: *industrial robotics*; stance: design; time notion: discrete ticks. Cross-context transport not declared. | Context: *clinical metrics*; stance: analysis; validity windows declared; cross-context transport via Bridge (concept only; details per A.6.1). Numeric comparability bound to CHR and CG-Spec. |

*Why these two?* E.8 requires pairs from **U.System** and **U.Episteme** to demonstrate trans‑disciplinary universality.

#### A.6.0:5.1 - Near-miss and anti-cases

**Near-miss: handler hidden in a `U.Signature(profile=FormalSubstrate)` declaration.** A `U.Signature(profile=FormalSubstrate)` declaration for an algebraic-effects calculus may list operation symbols, inference kinds, and equational laws. If the same block says how a database handler commits transactions, the text has crossed into A.6.1 `U.Mechanism`: keep the operation and effect signature in A.6.0, and publish the handler realization as a mechanism that cites this signature.

**Near-miss: measurement comparison hidden in a principle frame.** A `PrincipleFrame` may state that a physical model preserves a heat-flow invariant and that observability must be recoverable through CHR. It must not declare units, reference planes, comparator legality, or transport loss as if they were signature laws. Those belong to CHR, UNM, bridge, comparator, and measurement patterns that cite the principle frame.

**Anti-case: implementation manual called a signature.** A document that names build steps, CI checks, tool vendors, or work authorization before it states `SubjectBlock`, `Vocabulary`, `Laws`, and `Applicability` is not a conformant `U.Signature`. Rewrite the declaration first; then place realization, work, evidence, or tooling claims in their governing patterns.

### A.6.0:6 - Bias-Annotation (lenses and defaults)

* **Local‑first meaning.** Laws are **local** to the named Context; cross‑context use must be explicit (Bridge), never implicit.

* **No illicit scalarisation.** If numbers appear, legal comparability follows **CG-Spec and MM-CHR**; **no ordinal means**, **partial orders return sets**; unit and scale alignment is explicit.

* **Register hygiene.** Keep Tech vs Plain register pairs; avoid tooling or vendor talk in Kernel prose (E.10).

### A.6.0:7 - Conformance Checklist (normative)

| ID | Requirement |
| --- | --- |
| **CC‑A.6.0‑1** | A conformant text labelled **`U.Signature`** **SHALL** expose the **four‑row Signature Block**: *SubjectBlock; Vocabulary; Laws; Applicability*. A visual split of SubjectBlock into **Subject** and **Quantification** lines is allowed; it still counts as **one** conceptual row. |
| **CC‑A.6.0‑2** |  The Signature Block MUST remain conceptual: no code or CI metadata, no tool bindings, no execution steps, no implementation details, and no Γ-builder exports. Dependency and export metadata belongs in the `SignatureManifest` (§4.4.1), not inside the four-row Block. |
| **CC‑A.6.0‑3** | Applicability **binds** a `U.BoundedContext`; if cross-context use is intended, a **Transport clause** is *named* (Bridge reference) without re-stating Part F and B.3 details (including any **CL^plane**). |
| **CC‑A.6.0‑4** | Where numeric comparability is implied, Applicability **binds** to **CG-Spec and MM-CHR** legality (normalize-then-compare; scale and unit alignment). |
| **CC‑A.6.0‑5** | Families that specialise A.6.0 (e.g., A.6.1, method profiles, or discipline profiles) MAY add extra constraints and projection views, but MUST preserve the four-row Block as the canonical core (no extra semantic rows). |
| **CC‑A.6.0‑6** | Under E.10 and E.5, tokens MUST respect strata and family segregation: never redefine Kernel tokens in an Extension, Context, or Instance signature; instead, import and align. |
| **CC‑A.6.0‑7** | The **Laws** row contains **axioms and invariants** only; **AdmissibilityConditions** and operational admissions **MUST** appear only in **A.6.1 Mechanisms** that consume this Signature. |
| **CC‑A.6.0‑8 (No‑Realization on Signatures with EffectDiscipline).** | If **EffectDiscipline** appears in **Vocabulary**, faces **MUST** carry a **`No‑Realization` pin** and **MUST NOT** publish handler semantics; any **EffectRealization** is referenced (A.6.1) by id only. |
| **CC‑A.6.0‑9 (CHR‑binding without units or Transport).** | Signatures that declare **measurability intent** (e.g., PrincipleFrame) **SHALL NOT** publish **units, ReferencePlane, ComparatorSet, or Transport**; those are declared only by **UNM** and cited by edition or ref-id where consumers require numeric comparability. |
| **CC‑A.6.0‑10 (UNM‑priority on faces).** | Any numeric or comparable claim on a Signature face **pins** **CG-Spec and ComparatorSet edition ids** and, where scale or plane conversion occurs, **UNM.TransportRegistry edition** with **CL and CL^plane policy-ids**; **penalties are recorded only in `R` or `R_eff`**. |
| **CC‑A.6.0‑11 (Bridge‑only crossings).** | Cross-context or cross-plane reuse of Signature claims **MUST** name a **Bridge** (UTS row) and **MUST NOT** imply implicit equivalence by label; losses are recorded via **CL** (penalties → **R**). |
| **CC‑A.6.0‑12 (Profile conformance).** | If the Signature declares `profile=FormalSubstrate` or `profile=PrincipleFrame`, the corresponding **profile pins** in §4.2 are **mandatory**; failure to emit them makes the Signature **non‑conformant** for that profile. |
| **CC‑A.6.0‑13 (Profile morphism discipline).** | Applying a profile **SHALL** satisfy §4.6 (structure‑preserving morphism: SubjectBlock preserved, Vocabulary and Laws monotone, Applicability restrictive, no admissibility or handlers). |
| **CC‑A.6.0‑14 (SlotSpec for argument positions).** | Any `U.Signature` whose **Vocabulary** declares n‑ary relations or operators **SHALL** provide, for each argument position, a **SlotSpec** triple `⟨SlotKind, ValueKind, refMode⟩` (with `refMode ∈ {ByValue \| RefKind}`) as per A.6.5 `U.RelationSlotDiscipline`. |
| **CC‑A.6.0‑15 (Slot and Ref lexical discipline on signatures).** | Names of SlotKinds and RefKinds used in SlotSpecs **MUST** obey E.10 and A.6.5 lexical guards: tokens ending with **`…Slot`** denote SlotKinds only; tokens ending with **`…Ref`** denote either RefKinds or episteme fields whose type is a RefKind; no ValueKind ends with these suffixes. |
| **CC‑A.6.0‑16 (SlotSpecs for n‑ary relations).** | Any `U.Signature` whose **Vocabulary** declares an **n‑ary relation or morphism** **SHALL** assign to each parameter position a `SlotSpec_i = ⟨SlotKind, ValueKind, refMode⟩` as defined in **A.6.5 `U.RelationSlotDiscipline`**; SlotSpecs live inside the Vocabulary row’s per‑relation parameter block and **MUST NOT** introduce additional rows beyond the four‑row Block. |
| **CC‑A.6.0‑17 (SlotSpec-based substitution laws).** | Specialisations of A.6.0 that define **substitution, retargeting, or profile application** over n-ary relations or morphisms (e.g., **A.6.2–A.6.4**) **SHALL** phrase their rules in terms of **SlotSpecs** (SlotKind, ValueKind, and RefKind) rather than unnamed parameter indices and **SHALL** obey the `…Slot` and `…Ref` lexical discipline in **A.6.5** and **F.18**. |
| **CC‑A.6.0‑18 (Manifest required for reuse).** | If a signature is intended to be imported or reused, it MUST include a `SignatureManifest` (§4.4.1) with explicit `id`, `version`, `imports`, and `provides`. |
| **CC‑A.6.0‑19 (Imports acyclicity).** | If `imports` is present, it MUST be acyclic (no cycles in the signature import graph). |
| **CC‑A.6.0‑20 (No redeclare across imports).** | If `imports` is present, `provides(S)` MUST NOT re‑declare any symbol already provided by any transitive import of `S`. |
| **CC‑A.6.0‑21 (No ghost dependencies).** | If `imports` is present, any non-Kernel **SymbolId** referenced in the **SubjectBlock** or **Vocabulary** rows that is **not** provided by this signature MUST be provided by some imported signature. ClaimIds, BridgeIds, policy-ids, and EditionIds are exempt. |
| **CC‑A.6.0‑22 (Realization opacity).** | If a family publishes any Realization of a `U.Signature`, that Realization **MUST** treat imported Signatures as **opaque** (depend only on their `provides` symbols and cited ClaimIds), and **MUST NOT** reference internal structure of imported Signatures. |
| **CC‑A.6.0‑23 (Monotone Realization).** | A Realization **MAY** tighten but **MUST NOT** relax the Signature’s Laws; if weaker laws are needed, publish a new Signature (or publish an explicit refinement morphism) rather than weakening the existing Signature Laws. |

### A.6.0:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| Signature as implementation manual | Build steps, CI checks, vendors, or work authorization are placed before the public declaration. | State SubjectKind, RangedValueKind, Vocabulary, Laws, and Applicability first; put realization, tooling, work, and evidence in their governing patterns. |
| Signature as operational gate | Runtime admission predicates are treated as signature laws. | Keep declaration-level constraints in A.6.0 and put operational admissibility conditions in A.6.1 mechanisms. |
| Signature as measurement or bridge proof | Measurement comparability, cross-context transport, or bridge policy is treated as part of the declared law. | Keep the signature declaration stable and use measurement, bridge, evidence, gate, or decision patterns for those relations. |
| Signature as U-kind minting shortcut | A vocabulary symbol is treated as a durable U-kind because it appears in the declaration. | Use C.3, E.24.UK, and the relevant ontic pattern before admitting a durable U-kind. |

### A.6.0:8 - Consequences

* **Uniform kernel shape.** Practitioners can define **theory**, **mechanism**, **method**, **discipline**, or other family signatures without inventing new templates.

* **Hard decoupling.** Boundary interfaces stay stable: the A.6.0 Block defines the signature and laws, while mechanisms and realizations can evolve behind it (with monotone strengthening and explicit guard boundaries).

**Didactic cohesion.** Readers see the same four conceptual rows across the spec, satisfying E.8’s comparability goal.

### A.6.0:9 - Rationale

**Why “SubjectBlock”?** A.6.1 showed that making the **ranged-over value kind explicit** (here: *RangedValueKind*) avoids category mistakes when moving between domains (e.g., *set-algebra on context slices* vs *equivalence-classes of normalisations*). A.6.0 lifts this to the kernel so every signature can declare **what it is about** before saying **what it provides**.
**Why one universal Block?** Experience with extension and mechanism signatures shows the value of a single canonical shape for Vocabulary, Laws, Applicability, and Alignment; A.6.0 factors that universal core so other families can add headers and views without fragmenting the Kernel.

### A.6.0:9.1 - SoTA-Echoing
— **Algebraic effects and handlers** (OCaml 5, Koka, Effekt, Links): *operation signatures and handler laws* mirror **Vocabulary and Laws** while keeping implementations separate.
— **Session and behavioural types** (2016–2024): protocol and admissibility laws parallel the **Laws** row (at mechanism level).
— **Graded and row-polymorphic effects** (Granule, row-effects): inform the **EffectDiscipline** vocabulary and equational laws.

**Profiles rationale (informative).**
— **`profile=FormalSubstrate` signature profile.** Captures *mathematical language, inference kinds, and effect signatures* in the **conceptual declaration context**, ensuring the calculus stays independent from handler and realization choices; consuming mechanisms (A.6.1) provide **EffectRealization** only by reference.
— **PrincipleFrame.** Captures *postulates and invariants plus measurability intent (CHR binding)* without committing to **units, planes, or Transport**, which are declared centrally in **UNM** so that comparisons remain lawful and edition‑pinned.

### A.6.0:10 - Relations

* **Specialises and is specialised by:** **A.6.1** (adds `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, and `Transport` for mechanisms) and any domain‑profiled signature publications that preserve the four‑row Block.
* **Constrained by:** E.10 LEX-BUNDLE (registers, strata); D.CTX for Context binding; **Part F** (Bridges and cross-context transport; naming).
* **Consumed by (profiles):** **`U.Signature(profile=FormalSubstrate)`** and **`U.Signature(profile=PrincipleFrame)`** specializations in the first-principles use case; **UNM** (Context Normalization) remains the canonical edition source for **CG‑Spec, ComparatorSet, and Transport** editions that Signature consumers pin on faces.

* **Enables:** uniform declaration and comparison of signatures across Part C families, methods, and discipline glossaries (Part F).

### A.6.0:10a - P2W `U.Signature(profile=FormalSubstrate)` Use Relation

When `E.18.1` uses a first-principles or mathematical cue to select, declare, or cite a `U.Signature(profile=FormalSubstrate)` declaration, this pattern governs only that declaration: SubjectBlock, Vocabulary, Laws, Applicability, effect discipline, inference kinds, imported-symbol dependencies, and the no-realization pin. `E.18.1` may carry the cue and select the next admissible relation. `C.29` governs whether a mathematical-lens use is admissible for the stated use.

#### A.6.0:10a.1 - `profile=FormalSubstrate` signature, mathematical object, and lens-use slot discipline

Do not decide whether source wording names a `U.Signature(profile=FormalSubstrate)` declaration, a general `U.Signature` declaration, or a mathematical-lens use by lexical replacement. Decide which relation position is live. The same mathematical object, formalism, or family may fill more than one relation position, but the position changes the admissible claim.

| Live relation position | Governing pattern | Required recovery | Non-admissible overread |
|---|---|---|---|
| `U.Signature(profile=FormalSubstrate)` declaration | `A.6.0` | `U.Signature(profile=FormalSubstrate)` with SubjectBlock, Vocabulary, Laws, Applicability, effect discipline, inference kinds, imports and provides, and no-realization pin. | The declaration is not a mechanism, empirical identity claim, evidence proof, work authorization, gate passage, or mathematical-lens use result. |
| Mathematical-lens use | `C.29` | Candidate mathematical object or formalism, mapping mode, preserved structure, lost structure, visible payoff, admissible use, non-admissible use, and stop condition. | Lens-use adequacy does not declare the signature profile and does not settle handler semantics, mechanism realization, empirical truth, evidence, work, gate, or decision authority. |
| Mechanism consumption or realization | `A.6.1` and downstream mechanism patterns | A mechanism cites the signature by import or reference, publishes operation algebra, law set, admissibility conditions, transport, and any monotone realization relation when that relation is being made. | A mechanism does not rewrite the imported signature laws by use, and a realization does not become a new `U.Signature(profile=FormalSubstrate)` declaration unless a new signature is declared. |
| P2W carry-through cue | `E.18.1` | Source cue, carried distinction, live next relation, selected application, stop condition, and any return trigger. | P2W does not mint `U.SubstrateFormalization`, does not decide mathematical-lens admissibility, and does not replace A.6.0 or C.29. |

Old or source-local wording such as `SubstrateFormalization` recovers as a move to author, select, or cite a `U.Signature(profile=FormalSubstrate)` unless the claim being made is actually a `C.29` mathematical-lens use, an `A.6.1` mechanism relation, or another neighboring relation. In slot terms, the mathematical object can fill a `CandidateMathObject` position in `C.29`, a vocabulary or law position in a `U.Signature(profile=FormalSubstrate)` declaration, or an imported-signature position in a mechanism. Those are relation positions, not separate object kinds and not `U.Role`s.

The Rodin-style lesson used here is constructive rather than slogan-like: formal languages, axioms, rules, and mathematical objects help model a world-facing or episteme-facing EntityOfConcern only when their representational and operational limits are declared. A.6.0 therefore stores the formal-deductive declaration. C.29 stores the declared use of a mathematical lens. A.6.1, bridge, measurement, evidence, work, gate, and decision patterns store the later relations that apply, test, authorize, or use that declaration.

### A.6.0:10b - P2W PrincipleFrame Input Order

When `E.18.1` carries ontology, UTS, kind-relation, identity, context, boundary, characteristic, measurement, scale, comparator, or result-measurement wording toward a `PrincipleFrame`, write the input order explicitly. `PrincipleFrame` publishes postulates plus CHR observability in a bounded context; ontology editions, UTS rows, CHR editions, UNM, comparator, transport, normalization, bridge, and measurement relations stay with their own governing patterns.

### A.6.0:10c - PrincipleFrame And CHR Observability Relation

For P2W use, `PrincipleFrame` may cite CHR observability only after the relevant characteristic, observation, measurement, scale, comparator, normalization, or bridge relation is recoverable. Numeric comparability, characterization admission, parity, selected-set relation, and refresh continue under the current characterization, normalization, comparator, selected-set, parity, or refresh pattern.

### A.6.0:10d - PrincipleFrame Name And Profile Boundary For P2W

For P2W use, the durable object name is `PrincipleFrame`. Plain wording about principle framing may describe writing, selecting, or citing that object, but it does not create `U.PrincipleFraming` or a second profile.

### A.6.0:10e - P2W Boundary Summary For `U.Signature(profile=FormalSubstrate)` And PrincipleFrame

For P2W references to `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame`, first apply the slot discipline in `A.6.0:10a.1`. The signature profile carries only its declaration relation. If a source phrase also claims empirical realization, handler semantics, mechanism operation, work authorization, gate passage, evidence, assurance, result certification, units, reference planes, transport comparison, or downstream work use, recover that additional relation through its governing pattern before relying on the signature reference.

A CHR edition change, ontology edition change, or UNM change does not republish the `PrincipleFrame` by default. Republish, refresh, or changed downstream use requires a relation named by value that states whether the change affects postulates, observability binding, normalization, comparator, transport, measurement, bridge, work, gate, evidence, assurance, or result use.

### A.6.0:11 - Lowering, repair, and refresh conditions

A `U.Signature` remains usable while the four-row Block is stable and all downstream use can recover the same SubjectBlock, Vocabulary, Laws, Applicability, and imported-symbol dependencies.

Repair the signature, or mint a new signature when monotone repair is impossible, if any of these conditions holds:

* a realization, handler, work authorization, evidence proof, bridge policy, or measurement comparison has been written into the Signature Block;
* a downstream use depends on a symbol, law, policy, or edition not exported by this signature or by an imported signature;
* a profile application weakens a law, widens Applicability, or adds operational admission;
* a current SoTA change in algebraic effects, session types, typed effect systems, `profile=FormalSubstrate` signatures, or context normalization changes the declared operation vocabulary, inference kinds, law shape, or no-realization boundary;
* a renamed SubjectKind, RangedValueKind, SlotKind, RefKind, or exported SymbolId no longer recovers the same FPF kind under E.10 and F.18.

Do not repair the signature merely because a later realization, work plan, measurement run, bridge, or evidence record changed. Repair the object governed by that later relation unless the change alters the signature declaration itself or the exact dependency relation by which the later object cites the signature.

### A.6.0:End

