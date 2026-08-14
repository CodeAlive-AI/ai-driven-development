## A.6.2 - `U.EffectFreeEpistemicMorphing` — Effect‑free morphisms of epistemes
> **Status:** Stable
> **Type:** Definitional ontic pattern

**One-line summary.** `U.EffectFreeEpistemicMorphing` (EFEM) is the universal class of **effect-free, law-constrained morphisms between epistemes**. An EFEM morphism transforms one exact episteme into another and states what happens to claim content, the exact EntityOfConcern, and the effective ReferenceScheme when that scheme is material. Grounding and any viewpoint selected for a named describing use remain separately identified. The morphism declares `EntityOfConcernChangeMode` as either `preserve` or `retarget` under C.2.1.

**Use this pattern when** a project needs to transform an episteme into another episteme while preserving the distinction between episteme-only change, EntityOfConcern retargeting, publication rendering, mechanism application, and performed work.

**What goes wrong if missed.** A view, retargeting, refinement, representation change, publication rendering, mechanism application, or work occurrence is treated as the same operation, so the project can no longer tell whether the EntityOfConcern changed or only the episteme changed.

**What this buys.** EFEM gives one law-constrained episteme-to-episteme morphism discipline with explicit preserve/retarget mode, clear boundaries among actual values, declaration-local participant meanings, and references, plus conservativity and composition conditions.

**Placement.** After **A.6.1 `U.Mechanism`** and before any specialisations (`A.6.3 U.EpistemicViewing`, `A.6.4 U.EpistemicRetargeting`).

**Builds on.**
A.6.0 `U.Signature` for subject, vocabulary, laws, and applicability; A.6.1 `U.Mechanism`; A.6.5 for declaration-local SlotSpecs; C.2.1 for `U.Episteme` identity and direct constitution, empirical-grounding, and edition relations; E.10.D2 for the EntityOfConcern, Description-episteme, describing-use, and specification-use boundary; and C.3 plus F.9 for kind-level and exact cross-local reasoning.

**Used by.**
A.6.3 `U.EpistemicViewing`; A.6.4 `U.EpistemicRetargeting`; E.17.0 `U.MultiViewDescribing`; E.17 (MVPK); E.18 (structural reinterpretation over transformation-flow structure).

**EntityOfConcern change-mode discipline.** EFEM uses `EntityOfConcernChangeMode` for the preserve/retarget characteristic over the exact C.2.1 EntityOfConcern designated by `entityOfConcernRef`. Earlier source-side spellings must be normalized to the EntityOfConcern family before conformant use and do not define a second EntityOfConcern ontology.

**Body-level U-kind settlement.** `U.EffectFreeEpistemicMorphing` is the durable value defined in this pattern. `U.Episteme` is reused from C.2.1; an episteme card, view, or publication is a dependent episteme or publication value only when C.2.1 and E.17 define or constrain it. `ClaimGraph` and `ReferenceScheme` are C.2.1 values, while a viewpoint selected for one describing use is a separate use qualification. `SubjectRef` is only a legacy source-wiring name: recover the exact episteme, its EntityOfConcern, and any material scheme or use-level viewpoint instead of treating the name as a second ontology. `EpMorphism` below is the local mathematical-lens arrow value for the episteme category, not a root U-kind. Claims about performed Work use A.15.1; mechanism application uses A.6.1 and E.20; publication form, face, and carrier use E.17 and E.24.PUB. None is an EFEM claim merely because the same source mentions it.

### A.6.2:1 - Problem frame

FPF has many operations that **transform knowledge epistemes or publications** without directly doing work in the world:

* turning an informal method description into a more formal specification;
* projecting a large system description into a smaller “for‑safety‑officer” view;
* re‑expressing the same behavioural model in a different calculus or notation;
* retargeting an analysis from “this subsystem” to “that subsystem” along a known KindBridge.

All of these are **episteme→episteme** transforms: they change what is written in an episteme, but they **do not themselves measure, execute, or actuate**. They are neither Work (A.15) nor Mechanisms in the A.6.1 sense; they are “pure morphisms over epistemes”.

Without a universal pattern for such morphisms:

* every family (KD‑CAL, E.18, MVPK, discipline packs) reinvent their own notion of “projection”, “reinterpretation”, or “refinement”;
* laws about what may change in an episteme (content vs EntityOfConcern vs grounding holon vs reference plane) fragment across the spec;
* cross‑family reasoning (e.g. “this E.18 structural reinterpretation is a retargeting, not a view”) becomes brittle and ad‑hoc.

### A.6.2:2 - Problem

Concretely, without EFEM:

1. **No single place for “effect‑free” discipline.**
   The distinction between episteme-only change and Work in the world is already important: C.2.1 separates the three episteme identity values and neighboring direct relations from Work, publication forms, renderings, and carriers. The laws for episteme-only operations are otherwise scattered or implicit.

2. **EntityOfConcern behaviour is unclear.**
   Many transforms **intend** to keep “what this episteme is about” fixed (viewing), others **intend** to change it under an invariant (retargeting). Without a common *EntityOfConcernChangeMode* discipline we get silent breaks in “entityOfConcern”: an operation that looks like a harmless format change may in fact surreptitiously change the entity of concern.

3. **No functorial backbone.**
   MVPK, KD‑CAL, and E.18 all implicitly assume that episteme transforms **compose** and respect identities, but the conditions for this (purity, conservativity, idempotence, scope) are not formulated once and reused. Different parts of the spec repeat subtly different sets of laws.

4. **Slot/Ref confusion.**
   C.2.1 identifies an episteme through exact claim content, one exact EntityOfConcern, and one effective ReferenceScheme. A.6.5 SlotSpecs apply only inside an exact reusable relation declaration. Laws for “projection” or “retargeting” that instead rely on unnamed fields or tuple positions therefore hide what the morphism actually reads or changes.

The result: engineers and tool builders can no longer tell **when they are allowed to transform epistemes without changing what is being claimed about the world**, nor what needs to be witnessed by Bridges and CL‑penalties when entityOfConcern does change.

### A.6.2:3 - Forces

* **Epistemic purity vs operational power.**
  Effect-free episteme transforms are attractive precisely because they can be reasoned about algebraically and composed freely. But the more operational power they are given (IO, solver calls, measurements), the less they remain “pure” and the more they belong under `U.Mechanism` or performed `U.Work` as defined in A.15.

* **Preserve vs retarget.**
  Viewing is entityOfConcern‑preserving; reinterpretation along a KindBridge is entityOfConcern-retargeting. Both are important, but **they must be distinguished and witnessed differently**.

* **Conservativity vs usefulness.**
  EFEM should be **conservative**: no new commitments about the EntityOfConcern beyond what input epistemes already entail. At the same time, transformations may *factor*, *aggregate*, or *normalise* content, which may drop information or change representation when the loss and interpretation rule are explicit.

* **Locality vs reference planes and Bridges.**
  Epistemes live on **reference planes** (C.2.1). When a use relates distinct source-local senses or crosses a reference plane, apply the exact F.9 Bridge or plane relation and its reliance consequences. EFEM cannot hide either change inside a “pure” content rewrite.

* **EntityOfConcern and Description-episteme boundary and specification-use refinement.**
  The EntityOfConcern is not identical to the Description episteme produced by this use; it may itself be `U.Episteme` when an episteme is under concern. `...Description` names a Description episteme, and `...Spec` names a Description episteme admitted for specification use only when its claims are checkable and the named harness or validation relation can test them. When a describing use selects a viewpoint, name that use and exact viewpoint separately; selection is neither an episteme constituent nor conformance. EFEM states whether claim content, EntityOfConcern, grounding, effective scheme when material, and any selected use-level viewpoint are preserved or changed, while keeping EntityOfConcern, Description episteme, specification use, publication form, publication unit, carrier, and rendering distinct (A.7, E.10.D2).

### A.6.2:4 - Solution — define `U.EffectFreeEpistemicMorphing` once

#### A.6.2:4.1 - Informal definition

> **Definition.** A `U.EffectFreeEpistemicMorphing` (EFEM) is a class of **episteme→episteme morphisms** that:
>
> * operate **only** on exact epistemes identified under C.2.1 and state by value what happens to their claim content, EntityOfConcern, and effective ReferenceScheme; any grounding or viewpoint selected for a named describing use remains separate;
> * are **effect‑free** (no Work, no Mechanism application, no mutation of systems or carriers);
> * are **conservative** in what they claim about the EntityOfConcern: no new EntityOfConcern commitment may appear unless it is a logical consequence under the declared ReferenceScheme, correspondence, or bridge invariant;
> * are **functorial** (identities and composition behave as expected on the category of epistemes);
> * declare an explicit **EntityOfConcernChangeMode in {preserve, retarget}**, controlling how the EntityOfConcern changes, and explicitly preserve or change every material scheme, grounding, scope, or selected describing-use viewpoint rather than decoding a compound context value.

The category-theory **objects** of the EFEM universe are exact `U.Episteme` values of admitted dependent kinds; an episteme may also be the same individual as a `U.View` when E.17.0 conformance obtains. Publication form, carrier, and `EpistemePublicationRelation` occurrence remain separate from that episteme. The **arrows** are EFEM morphisms `f : X → Y` satisfying the P0-P5 laws below.

Specialisations:

* `U.EpistemicViewing` (A.6.3) — EFEM with `EntityOfConcernChangeMode = preserve`.
* `U.EpistemicRetargeting` (A.6.4) — EFEM with `EntityOfConcernChangeMode = retarget`, tied to KindBridges/ReferencePlanes.

#### A.6.2:4.2 - Direct signature components (A.6.0 alignment)

As a `U.Signature`, EFEM declares the following direct A.6.0 components, specialised to episteme-to-episteme morphisms. They are declaration content, not fields of an additional container kind.

```
SubjectKind     = U.EffectFreeEpistemicMorphing
RangedValueKind = pair of U.Episteme values <X, Y>
ResultKind      = EpMorphism
SliceSet        = ContextSliceSet
ExtentRule      = admissible EFEM morphisms in each selected slice
```

`X` and `Y` are respectively the domain and codomain epistemes. `EpMorphism` is the local mathematical-lens arrow value `f : X -> Y` in the `Ep` category. `SliceSet` and `ExtentRule` are current here because later viewing and retargeting declarations rely on the admitted morphism family varying by selected slice; they are not mandatory signature filler.

**Vocabulary (core operators & kinds)**

* **Types**
  * `U.Episteme` (as holon, including any same-individual admitted dependent episteme kind or `U.View` membership); publication is contingent participation in exact E.24.PUB relations, not an episteme species.
  * `U.EpistemeKind` (an admitted dependent kind of `U.Episteme`; it does not make the episteme a relation record or give it participant slots).
  * `SubjectRef` (legacy source wiring name only). When it occurs, recover the exact episteme and EntityOfConcern; recover the effective scheme when it changes interpretation and any selected viewpoint only for the named describing use. It does not define another EntityOfConcern family or a compound context value.
  * `EpMorphism` (local arrow value in `Ep`, defined here and interpreted through C.29 when the mathematical-lens use is current).
  * `U.EntityOfConcernChangeMode = {preserve, retarget}` (enumeration; no new durable U-kind named “EntityOfConcern”).

* **Operators (arrow algebra)**

  * `id_X : EpMorphism(X->X)` for any episteme `X`.
  * `compose(g,f) : EpMorphism(X->Z)` where `f : X->Y`, `g : Y->Z`.
  * `apply(f, x:U.Episteme) : U.Episteme`.
  * `dom(f), cod(f) : U.Episteme`.
  * `subjectRef(E) : SubjectRef` only as a legacy source projection; conformant use resolves E and its EntityOfConcern, then names any material scheme or use-level viewpoint separately.
  * `entityOfConcernChangeMode(f) : U.EntityOfConcernChangeMode`  // EFEM‑level characteristic from C.2.1.

Each operator that takes epistemes as arguments names by value the C.2.1 discriminators it reads or changes: claim content, exact EntityOfConcern, and effective ReferenceScheme. It names any empirical-grounding, representation, view-conformance, or describing-use viewpoint relation separately. When an exact reusable relation declaration is current, its A.6.5 SlotSpecs describe that relation's participant meanings; they are not fields of an episteme.

**Laws row** and **Applicability** are given by P0–P5 and the Scope clause below.

#### A.6.2:4.3 - Laws P0–P5 (normative)

All laws below are **admissibility predicates**: a morphism advertised as an instance of `U.EffectFreeEpistemicMorphing` satisfies them.

##### A.6.2:4.3.1 - P0 — Typed episteme and value-and-relation profile (C.2.1-grounded)

For any EFEM morphism `f : X→Y`:

1. **Typed epistemes.** `X` and `Y` are epistemes of declared kinds `K_X, K_Y : U.EpistemeKind`, each identified under C.2.1 by exact claim content, one EntityOfConcern, and one effective ReferenceScheme. Grounding and representation relations are added only when current; a viewpoint selected for a named describing use remains outside episteme identity.

2. **Value and use projection.** For each episteme `E`—and separately for a named describing use when one is current—EFEM laws may refer to:
   * `content(E) : U.ClaimGraph` — E's exact identity-bearing claim content;
   * `entityOfConcernRef(E) : U.EntityRef` — designates E's exact EntityOfConcern;
   * `selectedViewpointRef?(use) : U.ViewpointRef` — only when the named describing use selects one exact viewpoint; this is not a component of E's identity;
   * `referenceScheme?(E) : U.ReferenceScheme` — E's effective designation and interpretation scheme;
   * `representationSchemeRef?(E) : U.RepresentationSchemeRef` — only when an exact C.29 representation scheme and correspondence relation are current for E; this is not a C.2.1 identity component;
   * `meta(E)` — any separately current C.2.1 edition relation, A.10 provenance or evidence relation, or named status value, each with its exact predicate and participants. An EFEM species may use those values, but none becomes an episteme-identity component by appearing here.

   When grounding matters, name the exact grounding relation, its grounding holon, and the claims it covers; grounding is not another component of episteme identity.

3. **Declared `EntityOfConcernChangeMode`.**
   Each EFEM species **declares** a fixed `EntityOfConcernChangeMode ∈ {preserve, retarget}`. At the level of individual morphisms:

   * if `entityOfConcernChangeMode(f) = preserve`, then `entityOfConcernRef(Y) = entityOfConcernRef(X)`; any current grounding relation is preserved or changed separately;
   * if `entityOfConcernChangeMode(f) = retarget`, then `entityOfConcernRef(Y) ≠ entityOfConcernRef(X)` in general and the record names a **KindBridge** between the two EntityOfConcern values (A.6.4 / F.9).

4. **Legacy SubjectRef and describing-use discipline.**
   For Description epistemes, including those admitted for specification use, resolve legacy `subjectRef(E)` to exact E and its EntityOfConcern. State separately whether the morphism preserves or changes claim content, EntityOfConcern, grounding, effective scheme when material, and any viewpoint selected for a named describing use. Viewpoint selection is neither identity nor conformance.

##### A.6.2:4.4.2 - P1 — Purity (no external effects)

EFEM morphisms are **pure functions on epistemes**:
* Applying `f : X→Y` **does not**:
  * change any `U.System` or `U.Holon` state;
  * perform `U.Work` or run a `U.Mechanism` (A.6.1) with operational guards;
  * create, update, or mutate a presentation carrier, publication carrier, file, database, message bus, or IDE artifact.
* The **only** state change introduced by EFEM is the replacement of input epistemes by output epistemes according to `apply(f, X) = Y`; P2-P5 constrain every change to an identity value or neighboring relation.

Any operation that requires **measurements, simulations, solver calls, or tool use with external side-effects** is modelled as a `U.Mechanism`/`U.Work` that **produces new epistemes**, which may then be related by EFEM morphisms.

##### A.6.2:4.3.3 - P2 — Conservativity (no new EntityOfConcern commitments)

Let `content_X = content(X)`, `content_Y = content(Y)`, with associated `referenceScheme_X`, `referenceScheme_Y`, `entityOfConcernRef_X`, and `entityOfConcernRef_Y`. Interpret each `content` via its `ReferenceScheme`. When the claim depends on grounding, identify the source and receiving grounding relations and holons separately. Then:

> The set of **claims about the EntityOfConcern values** that can be interpreted from `Y` **introduces no new atomic commitments** beyond those that are logical consequences of the claims interpreted from `X`, possibly after applying a declared correspondence between representation/reference schemes.

Intuitively:

* EFEM may:
  * delete information (projection/abstraction);
  * normalise or re‑express information (e.g., reordering ClaimGraph, changing notation via a ReferenceScheme/RepresentationScheme correspondence);
  * add **meta‑claims about the episteme** itself (edition, source, status, witness entries).

* EFEM may **not**:
  * assert new atomic facts about the EntityOfConcern values or grounding holons beyond what is derivable from input ClaimGraphs under the declared ReferenceSchemes and any named grounding relations;
  * silently widen the scope of claims or cross a ReferencePlane without the exact scope or plane relation required for that move.

Where `entityOfConcernChangeMode(f) = retarget`, conservativity is understood **relative to a declared invariant** of the KindBridge (A.6.4): e.g., conservation of energy for a Fourier transform, or preservation of functional behaviour for a structural reinterpretation.

##### A.6.2:4.3.4 - P3 — Functoriality (identity, composition, correspondence)

We work in the category **Ep** whose objects are epistemes (species of `U.Episteme`) and whose arrows are EFEM morphisms satisfying P0–P2, together with the functor

```
α : Ep → Ref
```

that maps each episteme to the reference designating its exact EntityOfConcern, `entityOfConcernRef(E)`, in the selected mathematical description. EFEM instances with `entityOfConcernChangeMode(f) = preserve` are vertical morphisms for α (`α(f) = id`), while those with `entityOfConcernChangeMode(f) = retarget` reindex along a declared `KindBridge` in **Ref**.

1. **Identities.** For each episteme `X`, there exists `id_X : X→X` such that:

   ```text
   apply(id_X, X) = X
   compose(id_Y, f) = f = compose(f, id_X)
   ```

   `id_X` preserves the episteme's claim content, EntityOfConcern, effective ReferenceScheme, and every other declared episteme value. If the same named describing use is carried through the identity morphism, its selected viewpoint also remains unchanged as a separate use qualification.

2. **Composition.** For `f : X→Y`, `g : Y→Z`, the composite `h = compose(g,f)` is an EFEM morphism `X→Z` with:

   ```
   apply(h, X) = apply(g, apply(f, X))
   entityOfConcernChangeMode(h) = combine(entityOfConcernChangeMode(f), entityOfConcernChangeMode(g))   // as per species-specific rules
   ```

and P0–P2 hold for `h`. For example, two `preserve` morphisms compose to `preserve`; `preserve` after `retarget` is `retarget` if the KindBridge composition exists.

3. **Correspondence-aware composition.** When EFEM changes a representation scheme or effective ReferenceScheme, name the exact C.29 or A.6.3.RT correspondence or transition relation that must commute. Composition respects that relation up to the declared isomorphism or oplax-naturality rule; any witness episteme remains a separately identified value.

##### A.6.2:4.3.5 - P4 — Idempotence & determinism (on fixed configuration)

For any EFEM morphism `f : X→Y` with fixed configuration (episteme kinds, `EntityOfConcernChangeMode` characteristic, KindBridge/CorrespondenceModel where needed):

1. **Determinism.**
   For the same input episteme `X`, the same separately declared inputs, and the same fixed configuration, `apply(f, X)` yields the same output episteme `Y` up to declared structural equivalence such as normal form or alpha-renaming. There is no dependence on ambient time, randomness, network state, or solver heuristics unless these are encoded as explicit inputs.

2. **Idempotence (up to declared equivalence).**
   Re‑applying the same EFEM to its own output yields no further essential change:

   ```text
   apply(f, apply(f, X)) ≅ apply(f, X)
   ```

   where `≅` denotes the structural equivalence declared for the episteme kinds in question (e.g., ClaimGraph normalisation).

Species MAY weaken idempotence to “idempotent after normalisation”; if so, the normalisation step is itself specified as an EFEM morphism and the composite be idempotent.

##### A.6.2:4.3.6 - P5 — Applicability, scope & compatibility

Each EFEM species **publishes** an Applicability clause:

* **EntityOfConcernClass / EntityOfConcern class.**
  A constraint on the admitted kinds of the exact EntityOfConcern, expressed for example as `EntityOfConcernClass ⊑ U.Entity`: “epistemes whose claims concern a `U.Holon` that is a system of type X”.

* **Grounding holon and operating conditions.**
  Name the exact grounding holon and the lab, runtime, organizational, scope, or other operating conditions that bound applicability when they matter. These conditions do not form a universal context object.

* **Representation/ReferenceSchemes.**
  Enumerates admissible `RepresentationScheme`/`ReferenceScheme` pairs and any required CorrespondenceModels.

* **Viewpoint discipline.**
  For Description epistemes, including Description epistemes admitted for specification use, EFEM specifies which `U.Viewpoint`s (E.17.0) are admissible and how it interacts with `U.MultiViewDescribing` families (e.g., “works only on engineering viewpoints from TEVB” or “viewpoint‑agnostic normalisation”).

Applying EFEM **outside** its Applicability (e.g., wrong EntityOfConcernClass, missing grounding holon, incompatible Viewpoint) is **non‑conformant**: a conformant implementation rejects such attempts or models them as different mechanisms/works, not as EFEM.

Use that actually relates distinct F.17 local senses or crosses a ReferencePlane is **not part of EFEM**. Apply the exact F.9 Bridge or plane relation and A.6.1 transport when those relations are current, then feed the resulting epistemes into EFEM. Different source labels or operating conditions alone create no Bridge.

### A.6.2:5 - Archetypal Grounding (Tell–Show–Show)

The examples below show how EFEM is intended to be used across the EntityOfConcern and Description-episteme boundary, specification-use refinements, and Viewpoint/MVPK publication lanes.

#### A.6.2:5.1 - Typed specification-use refinement `Specify_DescEp_SpecDesc` (species of EFEM)

*Context.* You have an informal `U.MethodDescription` for a safety check and want a more formal `U.MethodSpec` with test harness obligations, but **about the same method**.

*Shape.*

* Domain: `X = U.MethodDescription` episteme with
  `entityOfConcernRef(X) : U.MethodRef`, `content(X) : U.ClaimGraph_D`, and `ReferenceScheme_D`; when the named engineering validation use selects viewpoint P, record that selection separately.
* Codomain: `Y = U.MethodSpec` episteme with the **same** `entityOfConcernRef(Y) = entityOfConcernRef(X)`, more structured `content(Y) : U.ClaimGraph_S`, and a more explicit ReferenceScheme. If the same named validation use continues, it preserves its selected viewpoint P separately.

`Specify_DescEp_SpecDesc` is a species of EFEM:

* `entityOfConcernChangeMode(Specify_DescEp_SpecDesc) = preserve`.
* P1 — effect‑free: it transforms epistemes only.
* P2 — conservative: any behavioral claims in the Spec must be logical consequences of the informal Description and the exact Method that both epistemes concern. If the Spec adds a commitment not entailed by that basis, the operation is not a valid EFEM instance; identify the new claim as a separate C.2.1 episteme and state the operation, its entry condition, and its result under the rule that defines that operation.
* P3-P5 — functorial and scoped: specifications compose, and applicability is bounded by the named engineering scope, operating conditions, effective scheme, and any viewpoint selected for the named validation use.

This matches A.7 and E.10.D2: EntityOfConcern-to-Description (`Describe_EoC_DescEp`) is the strict-boundary describing step and is not itself an episteme→episteme morphism; `Specify_DescEp_SpecDesc` is an optional EFEM species over a Description episteme after a specification use/refinement gate is present. EFEM supplies the episteme→episteme laws for that refinement; it does not make Specification a third peer in A.7.

#### A.6.2:5.2 - Internal normalisation of a View (species of EFEM, `entityOfConcernChangeMode = preserve`)

*Context.* In MVPK you compute an engineering view `V` of a system description; you then normalise the view (sort, factor, put equations into normal form) without changing what it says.

Let `X = V_raw`, `Y = V_norm`, both `U.EpistemeView` instances with the same:

* `entityOfConcernRef(X) = entityOfConcernRef(Y)` (same system);
* the exact grounding relation and grounding holon used by the normalization remain unchanged, when grounding is current;
* any viewpoint selected by the named normalization use is the same exact P for X and Y; this selection is outside episteme identity;
* `representationSchemeRef(X) = representationSchemeRef(Y)` (same notation).

The EFEM `NormalizeView : X→Y`:

* has `entityOfConcernChangeMode(NormalizeView) = preserve`;
* changes only `content` and maybe `meta` (e.g. “normalised at edition E”);
* is idempotent and deterministic (P4);
* is conservative (P2): no new claims, only re‑expression.

MVPK can then **assume** functoriality of such normalisations without re‑stating the EFEM laws.

#### A.6.2:5.3 - Retargeting sketch (bridge‑backed, `entityOfConcernChangeMode = retarget`)

*Context.* E.18 structural reinterpretation maps a physical layout view into a functional behaviour view, changing the EntityOfConcern from “physical module assembly” to “functional graph” along a KindBridge.

Inside EFEM, this becomes a species with `entityOfConcernChangeMode = retarget`:
* input episteme describes `S₁` (e.g. a component hierarchy holon);
* output episteme describes `S₂` (e.g. a functional network holon);
* a declared `KindBridge(S₁,S₂)` and invariant (e.g. behavioural equivalence) provide the semantic glue;
* P2 conservativity is checked **w.r.t. that invariant**.

The details belong to A.6.4 and E.18; EFEM provides the generic discipline.

#### A.6.2:5.4 - Worked value-and-relation profile (engineering SystemDescription episteme kind)
*(informative)*

To make the C.2.1 value and EFEM law discipline concrete, consider an engineering episteme of a dependent system-description kind whose exact EntityOfConcern is one `U.System`:

| Value named by the EFEM species | Kind or reference form | Use |
| --- | --- | --- |
| exact EntityOfConcern | `U.Entity` constrained to `U.System`; designated by `U.EntityRef` | identifies the system that the claims concern |
| claim content | `U.ClaimGraph` | carries the description or specification claims |
| effective ReferenceScheme | `U.ReferenceScheme` | makes the claims and their designations interpretable |

This table names actual episteme values; it is not a `RelationSignature` or SlotSpec table. `EntityOfConcernSlot`, `ClaimGraphSlot`, and `ReferenceSchemeSlot` are declaration-local SlotKinds only when the reusable C.2.1 `EpistemeConstitutionRelationSignature` is being inspected. An EFEM species reads or changes the actual participants. It names any selected viewpoint, empirical-grounding relation, or representation relation separately.

Two typical EFEM species over this kind are:
* `Specify_DescEp_SpecDesc_Sys : SystemDescription → SystemSpec` — an `EntityOfConcernChangeMode = preserve` species that:
  * **reads** the exact EntityOfConcern and effective ReferenceScheme, separately uses an obtaining empirical-grounding relation or named describing-use viewpoint only when current, and **writes** refined claim content and possibly a strengthened effective ReferenceScheme;
  * satisfies P2 by only adding claims that are logical consequences of the original description plus the fixed `EntityOfConcern` (A.7 and E.10.D2);
  * satisfies C.2.1:7.1 by declaring its value-and-relation read/change profile and change mode.

* `Normalize_EngView : EpistemeView → EpistemeView` — a view‑normalisation EFEM (again with `EntityOfConcernChangeMode = preserve`) that:
  * **reads** the three C.2.1 identity values and every separately declared neighboring relation on which the operation depends, and **changes** only the output claim content and `meta`;
  * is idempotent and deterministic (P4) and pure (P1);
  * is conservative (P2) by construction: it never introduces new atoms about the selected system.

Concrete A.6.3/A.6.4/E.17.* patterns for engineering description and specification-use idioms state explicitly, under C.2.1:7.1 and CC-EFEM.*, which episteme values and separately obtaining relations their EFEM species read or change.

### A.6.2:6 - Bias-Annotation

* **Episteme‑first, world‑second.** EFEM is strictly about **epistemes as objects**; any world contact (measurements, executions) lives in `U.Mechanism`/`U.Work` and produces new epistemes that EFEM may subsequently relate.

* **Actual values, not unnamed fields.** Laws name the exact claim content, EntityOfConcern, and effective ReferenceScheme they use and keep empirical grounding, representation, view conformance, and describing-use viewpoint selection separate. A SlotKind is mentioned only when the exact reusable relation declaration is current.

* **Use-local semantics.** EFEM names the effective scheme, scope, grounding, and operating conditions that bound its use. An actual relation between distinct local senses or ReferencePlanes is delegated to F.9 or the plane relation and, when current, A.6.1 transport. No implicit cross-local EFEM is permitted.

* **EntityOfConcern and Description-episteme boundary and specification-use/refinement respect.** EFEM never collapses EntityOfConcern with Description epistemes or with specification-use refinements: EntityOfConcern-to-Description and optional specification-use refinement operations are typed explicitly. The former remains the A.7 describing boundary; the latter is an EFEM species only when it is an episteme→episteme refinement admitted by an exact specification use/refinement gate.

### A.6.2:7 - Conformance Checklist (normative)

| ID                                                  | Requirement                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC-EFEM.1 (Typed episteme objects).** | Every morphism advertised as `U.EffectFreeEpistemicMorphing` SHALL have exact domain and codomain epistemes whose C.2.1 claim content, EntityOfConcern, and effective ReferenceScheme are recoverable. The declaration names which of those values and which separately obtaining relations it reads or changes. A.6.5 SlotSpecs are required only for an exact reusable relation declaration and remain local to that declaration. |
| **CC‑EFEM.2 (Declared EntityOfConcernChangeMode).** | Each EFEM **species** SHALL declare the `EntityOfConcernChangeMode` characteristic `entityOfConcernChangeMode : EpMorphism -> {preserve, retarget}` as per C.2.1. For every instance `f`, `entityOfConcernChangeMode(f)` MUST be either `preserve` (=> `entityOfConcernRef` unchanged) or `retarget` (=> a KindBridge and invariant are explicitly named; see A.6.4 / F.9).                                                                                         |
| **CC‑EFEM.3 (Purity).**                             | EFEM morphisms SHALL be effect‑free: they MUST NOT directly perform Work or run mechanisms with operational guards; they only read input epistemes and construct output epistemes consistent with P2–P5. Any use of external solvers/measurements MUST be modelled as separate Mechanisms/Work that feed new epistemes into EFEM.                                                                     |
| **CC‑EFEM.4 (Conservativity).**                     | Laws for EFEM species SHALL state their conservativity regime: claims in the output MUST be logical consequences of input claims under declared ReferenceSchemes and any CorrespondenceModels/KindBridges. If an operation may strengthen claims (e.g. add commitments not entailed by inputs), it is **not** EFEM and MUST be modelled separately.                                                   |
| **CC‑EFEM.5 (Functoriality & idempotence).**        | EFEM species SHALL satisfy identity and composition with the usual category laws, and SHALL specify any structural equivalence under which idempotence holds. Non‑deterministic or order‑sensitive behaviour (beyond declared structural equivalences) is non‑conformant.                                                                                                                             |
| **CC‑EFEM.6 (Applicability and scope).** | Each EFEM species SHALL state the allowed EntityOfConcern kinds, grounding, effective schemes, claim scopes, operating conditions, and any optional describing-use viewpoint on which its operation actually depends. Applying EFEM outside those conditions is non-conformant. An actual cross-local or cross-plane use MUST name the exact F.9 or plane relation and any A.6.1 transport; no universal context object or automatic Bridge is inferred. |
| **CC‑EFEM.7 (Description and specification-use discipline).** | For any `...Description` or `...Spec` episteme, identify exact E and its EntityOfConcern under C.2.1; admit specification use only under E.10.D2; and state whether claim content, EntityOfConcern, grounding, effective scheme, and every material use qualification are preserved or changed. A viewpoint is named only for the describing use that selects it, and selection establishes neither identity nor E.17.0 conformance. |
| **CC-EFEM.8 (Value-and-relation read/change declaration).** | Any EFEM species SHALL declare its morphism family and change mode, name the C.2.1 values it reads or changes, and state its behavior on EntityOfConcern, claim content, and effective scheme. It SHALL separately state any empirical-grounding, representation, conformance, or describing-use viewpoint relation it reads or changes rather than treating that relation as episteme identity. |

### A.6.2:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| EFEM as performed work | An episteme rewrite is treated as measurement, actuation, or work occurrence. | Use EFEM only for episteme-to-episteme morphisms; use A.15 when work in the world is current. |
| EFEM as publication rendering | A face, carrier, or rendering change is treated as the episteme morphism itself. | Use E.17 for publication forms and use EFEM only for the episteme relation being represented. |
| Retargeting as harmless view | EntityOfConcern changes without a declared bridge or retargeting witness. | State `EntityOfConcernChangeMode=retarget` and use the relevant KindBridge or retargeting pattern. |
| Representation lens as ontology | A category arrow, graph, or mapping notation is treated as a new root U-kind. | Keep the mathematical object as the lens over the EFEM relation and keep U-kind settlement in E.24/C.3. |

### A.6.2:9 - Consequences

* **Single place for episteme‑to‑episteme laws.**
  All effect-free transforms of knowledge epistemes, across KD‑CAL, MVPK, E.18, discipline packs, can now be defined as species of EFEM, instead of each family re‑inventing its own law set.

* **Clear separation from mechanisms & work.**
  Anything that touches the world (measurements, execution, simulation) is forced into `U.Mechanism` or performed `U.Work`, with CL‑penalised Bridges and Γ_time; EFEM remains pure and compositional.

* **Stable backbone for Viewing & Retargeting.**
  A.6.3 and A.6.4 do not need to repeat P0–P5; they specialise EFEM with additional constraints (preserve/retarget). Other patterns (e.g. MultiViewDescribing, MVPK, E.18 structural reinterpretation) can depend on EFEM as a stable base.

* **Value-and-relation clarity.**
  By requiring each EFEM species to name the C.2.1 identity values and separately obtaining relations it reads or changes, the pattern keeps an EntityOfConcern, a declaration-local SlotKind, and a reference to the entity distinct.
* **Better didactics.**
  The traditional “semantic triangle” becomes a didactic projection over C.2.1 episteme constitution and the neighboring relations an EFEM species actually uses. It can gesture at expression, meaning, and subject without turning viewpoint, empirical grounding, representation, or reference into one slot tuple.

### A.6.2:10 - Rationale

**Why a separate EFEM pattern (A.6.2) instead of folding into A.6.1 or C.2.1?**

* A.6.1 defines **Mechanism** declarations—operations with AdmissibilityConditions, Γ_time, transport and Bridges—which are too operational for the pure episteme transforms needed here.
* C.2.1 fixes episteme identity through claim content, exact EntityOfConcern, and effective ReferenceScheme and keeps neighboring direct relations separate, but does not define morphisms. EFEM is a morphism-level pattern over those values and relations.

This split mirrors how Signature (A.6.0) separates “what is declared” from “how it is realised”: C.2.1 says what an episteme is; A.6.2 says what an admissible episteme-to-episteme transform is.

**Why insist on EntityOfConcernChangeMode?**

Because almost all subtle errors in multi‑view reasoning show up as **silent retargeting**: a transform that appears to keep the same EntityOfConcern actually changes it (e.g., from “component assembly” to “function bundle”) without naming the bridge or invariant. By forcing every species to declare `preserve` vs `retarget`, EFEM makes those decisions explicit and reviewable.

**Why name actual values and relation effects instead of informal fields?**

FPF distinguishes actual participants and their references from the declaration-local SlotKinds used in a reusable `RelationSignature`. Reusing that distinction here:

* aligns episteme morphisms with the framework's direct-relation architecture;
* enables checks that an EFEM species changed only the identity values and neighboring relations it declared; and
* avoids minting another generic parameter, field, or relation-role vocabulary.

### A.6.2:10.1 - SoTA-Echoing (informative, lineage)

EFEM is intentionally thin: it provides a minimal categorical value-and-relation discipline for episteme-to-episteme morphisms, making it possible to align with several post-2015 lines of work without importing their ontology.

* **Categorical semantics & displayed categories.**
  Treating `Ep` as a category over `Ref` via a functor `α : Ep -> Ref` that maps each episteme to its exact EntityOfConcern reference matches the displayed-categories view on fibrations: EFEM arrows are vertical when they preserve α and structured reindexings when they retarget under a `KindBridge`. This is a mathematical lens over C.2.1's EntityOfConcern distinction, not another C.2.1 relation or identity component.

* **Optics as universal projections.**
  Viewing operations (`U.EpistemicViewing`) refine EFEM in a way analogous to **lenses/prisms/traversals** in the optics literature: effect‑free, compositional accessors for parts of a larger structure. EFEM captures the laws that underlie those projections (purity, conservation, functoriality); optics‑style constructions can then be used inside discipline packs without modifying the core.

* **Structured cospans & correspondences.**
  Many correspondence‑based multi‑view patterns (ISO 42010 correspondences, model synchronisation, traceability links) can be seen as spans/cospans between epistemes. EFEM ensures that the legs of such cospans are effect‑free and conservative, while CorrespondenceModels carry the extra structure needed for consistency management.

* **Bidirectional transformations (BX).**
  The “no new commitments” and “functorial & idempotent” constraints mirror modern BX practice around **consistency restoration**: EFEM is the universal core that BX‑like constructions (view updates, synchronisers) must respect when instantiated for epistemes.

EFEM does *not* prescribe a specific calculus (deductive, probabilistic, latent‑space), nor a specific representation (symbolic vs distributed); those choices are captured in `U.ClaimGraph`, `U.RepresentationScheme` and discipline‑level patterns. EFEM only says what it means to transform epistemes **admissibly** in that chosen substrate.

### A.6.2:11 - Relations

* **Specialises / is specialised by.**

  * Builds on A.6.0 `U.Signature` for direct subject, range, optional result, slice, and extent components together with Vocabulary, Laws, and Applicability; coordinates with A.6.1 `U.Mechanism` without making mechanism application part of EFEM.
  * Specialised by A.6.3 `U.EpistemicViewing` (entityOfConcern‑preserving EFEM) and A.6.4 `U.EpistemicRetargeting` (entityOfConcern-retargeting EFEM).

* **Constrained by.**
  A.6.5 declaration-local SlotSpec discipline; C.2.1 episteme constitution and any separately current empirical-grounding or edition relation; E.10.D2 for the EntityOfConcern, Description-episteme, describing-use, and specification-use boundary; Part F for exact local-sense or ReferencePlane relations; and E.10 for naming discipline.

* **Consumed by.**
  E.17.0 `U.MultiViewDescribing` (families of Description epistemes, including Description epistemes admitted for specification use, under Viewpoints); E.17 (MVPK — publication as species of Viewing/EFEM); E.18 (structural reinterpretation and other transformation-flow relations over epistemes); KD‑CAL/LOG‑CAL rules that reason about episteme transforms categorically.

### A.6.2:End

