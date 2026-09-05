## A.6.2 - Effect-free episteme morphing
> **Status:** Stable
> **Type:** Definitional pattern

**One-line summary.** Effect-free episteme morphing (EFEM) is a local mathematical discipline for law-constrained arrows between exact epistemes. It compares what the source and receiving epistemes say, what they concern, and the schemes that make their claims interpretable, then states the allowed ClaimGraph difference. If its rule needs grounding, representation, conformance, or another separately obtaining relation, it names and reads that occurrence without changing it. The declaration, arrow, use claim, operation application, and performed Work remain distinct.

**Use this pattern when** a project needs to state and reuse a law-constrained mathematical relation between two exact epistemes while keeping that arrow distinct from a claim that it suits one use, an operation application, publication, and performed Work.

**What goes wrong if missed.** A view, retargeting, refinement, representation change, publication rendering, mechanism application, or work occurrence is treated as the same operation, so the project can no longer tell whether the EntityOfConcern changed or only the episteme changed.

**What this buys.** EFEM gives one law-constrained episteme-to-episteme morphism discipline with explicit preserve/retarget mode, clear boundaries among actual values, declaration-local participant meanings, and references, plus conservativity and composition conditions.

**Placement.** After **A.6.1 `U.Mechanism`** and before the A.6.3 epistemic-viewing and A.6.4 EntityOfConcern-retargeting branches.

**Builds on.**
A.6.0 `U.Signature` for subject, vocabulary, laws, and applicability; A.6.1 `U.Mechanism`; A.6.5 for declaration-local SlotSpecs; C.2.1 for `U.Episteme` identity and direct constitution, empirical-grounding, and edition relations; E.10.D2 for the EntityOfConcern, Description-episteme, describing-use, and specification-use boundary; and C.3 plus F.9 for kind-level and exact cross-local reasoning.

**Used by.**
A.6.3 epistemic viewing; A.6.4 EntityOfConcern retargeting; E.17.0 multi-view describing; E.17 (MVPK); and E.18 structural reinterpretation over transformation-flow structure.

**EntityOfConcern change-mode discipline.** EFEM classifies each arrow as `preserve` or `retarget` by comparing the exact C.2.1 EntitiesOfConcern designated by its endpoint `entityOfConcernRef` values. Earlier source-side spellings must be normalized to the EntityOfConcern family before conformant use and do not define a second EntityOfConcern ontology.

**Object settlement.** EFEM and `EpMorphism` are local mathematical classes under C.29, not admitted durable U-kinds. `U.Episteme` is reused from C.2.1. An A.6.0 FormalSubstrate signature that declares EFEM vocabulary and laws is a separate episteme; one arrow, one use-specific assertion about that arrow, any operation application, performed Work, and publication remain separate objects under their direct governors.

### A.6.2:1 - Problem frame

FPF repeatedly needs to relate one exact episteme to another, often alongside a separately described operation that produced the receiving episteme:

* turning an informal method description into a more formal specification;
* projecting a large system description into a smaller “for‑safety‑officer” view;
* re‑expressing the same behavioural model in a different calculus or notation;
* relating an analysis about one subsystem to an analysis about another, with a separate bounded-use assertion about the invariant, visible loss, receiving use, conditions, and polarity, plus a current-case judgement from exact facts.

All of these can be described by **episteme-to-episteme mathematical arrows**. The arrow relates exact epistemes and states its laws; it does not itself change an episteme, measure, execute, or actuate. Any operation application and Work remain separate.

Without one reusable local discipline for such arrows:

* each family (KD‑CAL, E.18, MVPK, discipline packs) reinvents its own notion of “projection”, “reinterpretation”, or “refinement”;
* laws about which parts of the source and receiving epistemes may differ, and which grounding or reference-plane facts their rules read and compare, fragment across the spec;
* cross‑family reasoning (e.g. “this E.18 structural reinterpretation is a retargeting, not a view”) becomes brittle and ad‑hoc.

### A.6.2:2 - Problem

Concretely, without EFEM:

1. **No single place for “effect‑free” discipline.**
   The laws for mathematical relations between exact epistemes are otherwise scattered or implicit; any operation application remains separate.

2. **Endpoint EntityOfConcern identity or difference is unclear.**
   Some arrow families have endpoint epistemes about the same exact EntityOfConcern; others have endpoints about independently different entities. Without a common `EntityOfConcernChangeMode` classification, a relation that looks like a harmless representation change can hide a different receiving EntityOfConcern.

3. **No functorial backbone.**
   MVPK, KD‑CAL, and E.18 all rely on episteme arrows that compose and respect identities, but the conditions for identity, composition, purity, conservativity, formal domain, and any arrow-family repeat law are not formulated once and reused. Different parts of the spec repeat subtly different sets of laws.

4. **Slot/Ref confusion.**
   C.2.1 identifies an episteme through exact claim content, one exact EntityOfConcern, and one effective ReferenceScheme. A.6.5 SlotSpecs apply only inside an exact reusable relation declaration. Laws for projection or retargeting that rely on unnamed fields or tuple positions therefore hide which parts of the source and receiving epistemes are being compared and which separately obtaining facts the rule reads.

The result: engineers and tool builders can no longer tell whether a mathematical relation keeps the same EntityOfConcern, identifies a different receiving one, or merely accompanies an operation. When the endpoints concern different entities, they also need a separate A.6.4 bounded-use assertion and a current-case judgement of whether the exact facts satisfy it.

### A.6.2:3 - Forces

* **Epistemic purity vs operational power.**
  Effect-free episteme arrows are useful because their laws can be reasoned about algebraically and composed. If a use needs I/O, solver calls, measurements, or another effect, identify the operation application and Work separately instead of giving that activity to the arrow.

* **Preserve vs retarget.**
  A viewing arrow has endpoint epistemes with the same EntityOfConcern; a retargeting arrow has independently different ones. A separate A.6.4 bounded-use assertion states the invariant, visible loss, receiving use, conditions, and affirmative or negative polarity. A current-case judgement separately reports `satisfies`, `fails`, or `cannot decide` from exact facts.

* **Conservativity vs usefulness.**
  EFEM should be **conservative**: no new commitments about the EntityOfConcern beyond what input epistemes already entail. The receiving ClaimGraph may factor, aggregate, normalize, or re-express source content and may use a different representation when the loss and interpretation rule are explicit. Any operation or Work that produces that receiving episteme remains separate.

* **Locality vs reference planes and Bridges.**
  Epistemes are interpreted on **reference planes** (C.2.1). When a use relates two exact source-local senses, test the direct F.9 predicate and cite a Bridge only when it obtains; state the bounded-use claim and any reliance separately. When a use crosses a ReferencePlane, cite its applicable plane relation. EFEM cannot hide either relation inside a “pure” content rewrite, and a local-sense or plane difference alone creates neither one.

* **EntityOfConcern and Description-episteme boundary and specification-use refinement.**
  The EntityOfConcern is distinct from a Description episteme about it; the EntityOfConcern itself may be `U.Episteme` when an episteme is under concern. `...Description` names a Description episteme, and `...Spec` names one admitted for specification use only when its claims are checkable and the named harness or validation relation can test them. EFEM compares what the two epistemes say, what they concern, and their effective schemes; it states what remains the same and what differs. When grounding or a describing-use viewpoint matters, name the exact relation occurrence or use qualification on each side and compare its facts. Any change to that occurrence follows its direct relation pattern; viewpoint selection and conformance require their own claims (A.7, E.10.D2).

### A.6.2:4 - Solution — define one local arrow discipline

#### A.6.2:4.1 - Informal definition

> **Definition.** An **effect-free episteme morphism** is a local mathematical arrow `f : X -> Y` between two exact epistemes. Under its selected formal substrate, it states how claim content, the EntityOfConcern, and any material reference or representation scheme correspond. Its content is this mathematical relation and its laws. Any Work, mechanism application, or episteme creation is a separate fact under its direct governor.

This is a local mathematical class under C.29, not an admitted durable U-kind. The pattern keeps the short name **EFEM** for that class. A reusable A.6.0 FormalSubstrate signature may declare its vocabulary and P0-P5 laws, but that signature episteme is not the class and is not one arrow.

An arrow in this class:

* has exact domain and codomain epistemes identified under C.2.1;
* is effect-free: no Work, mechanism application, system change, or carrier mutation follows from the arrow;
* states the exact conservativity rule it claims;
* obeys the declared identity and composition laws; and
* is classified locally by `EntityOfConcernChangeMode` as `preserve` or `retarget`.

Within the selected formal substrate, one arrow is identified by its exact domain, codomain, arrow rule or designator, and declared formal equivalence. Two arrows can have the same endpoints and still be different. Changing a claim about whether the same arrow is suitable for another use does not reidentify the arrow.

The ordinary FPF objects remain separate:

* `f` is the local mathematical arrow;
* the A.6.0 FormalSubstrate signature is a C.2.1 episteme declaring reusable vocabulary and laws for the arrow family;
* a C.2.1 bounded-use assertion `q` about `f` is another episteme; its ClaimGraph states the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity;
* a current-case judgement separately compares exact facts with `q` and returns `satisfies`, `fails`, or `cannot decide`;
* an operation application and any Work that computes, authors, or changes an episteme are identified only when they actually occur.

The A.6.3 viewing branch has endpoint epistemes about the same EntityOfConcern. The A.6.4 retargeting branch has endpoints about independently different entities and adds the separate bounded-use assertion `q` and current-case judgement defined above.

#### A.6.2:4.2 - Direct signature components (A.6.0 alignment)

When repeated use needs a reusable formal declaration, an A.6.0 `U.Signature(profile=FormalSubstrate)` episteme may declare this local arrow family. Its direct declaration components are:

```text
SubjectKind     = local formal type EpMorphism
RangedValueKind = admitted ordered-pair range over exact U.Episteme values satisfying the declared endpoint-kind constraints
ResultKind      = omitted; the arrow is the declared subject, not an operation result
Applicability   = selected formal substrate, admitted endpoint kinds, and arrow-family conditions
```

`SubjectKind` here is a type inside the selected formal substrate, not a durable FPF U-kind. Add `SliceSet` and `ExtentRule` only if one declared local type genuinely has slice-varying membership; do not use them to hide a use-specific suitability claim.

**Vocabulary.**

* `U.Episteme` — the exact domain and codomain values.
* `EpMorphism` — the local formal type of arrows in the selected substrate.
* `EntityOfConcernChangeMode = {preserve, retarget}` — a local two-value classification of one arrow, derived from its resolved endpoint EntitiesOfConcern rather than a durable U-kind or a `U.Characteristic`.
* `Ep` — the selected category whose objects are the admitted exact epistemes and whose arrows are the admitted `EpMorphism` values. Call it a category only when it contains the required identities and is closed under every declared composition.
* `EoCBase` — the endpoint-only thin category used to compare EntityOfConcern identity. Its objects are the exact independently resolved EntitiesOfConcern represented in the substrate. Between every ordered pair of admitted objects `A,B` it has one formal endpoint arrow `u_{A,B}`; `u_{A,A}` is the identity, and composition follows endpoints. These arrows are not independently meaningful domain or world-side relations.
* `dom(f)` and `cod(f)` — the exact endpoint epistemes; `id_X` and `compose(g,f)` — the declared identity and composition operations.
* `α : Ep -> EoCBase` — the declared mapping on objects and arrows. `α(X)` is X's exact EntityOfConcern after `entityOfConcernRef(X)` resolves it. For `f : X -> Y`, `α(f)` is the unique endpoint arrow `u_{α(X),α(Y)}`. It deliberately forgets f's arrow rule; different Ep arrows with the same endpoint EntitiesOfConcern therefore have the same image.
For each arrow, recover the C.2.1 identity values of X and Y and state which identity-bearing values or ClaimGraph parts are preserved or differ. If the arrow rule uses a neighboring relation, name its exact predicate and participants on each side and state which endpoint facts it reads or compares. Equal or different endpoint profiles do not mean that the arrow changed a relation occurrence or made it obtain or cease; any actual relation change and producing application or Work remain under their direct patterns. `SubjectRef` remains only a legacy source projection; resolve it to the exact episteme and EntityOfConcern.

A claim that `f` is suitable for one exact use is a separate C.2.1 bounded-use assertion `q`; a current-case judgement separately tests exact facts against it. A.6.1 governs the application occurrence and its argument and result bindings when those facts are current; the applicable system and Work patterns govern the performing system and performed Work. The A.6.0 signature and the mathematical arrow `f : X -> Y` remain the reusable declaration and relation.

**Laws and applicability.** P0-P5 below govern the local arrow class. A.6.5 SlotSpecs enter only when an exact reusable direct-relation declaration is current; they are not fields of X, Y, or `f`.

#### A.6.2:4.3 - Laws P0–P5 (normative)

All laws below test membership in the local EFEM arrow class under the selected formal substrate. They do not assert membership in a durable U-kind.

##### A.6.2:4.3.1 - P0 — Typed episteme, endpoint-value, and relation-read profile (C.2.1-grounded)

For any arrow `f : X→Y` presented as an effect-free episteme morphism:

1. **Typed epistemes.** `X` and `Y` are epistemes of declared kinds `K_X, K_Y : U.EpistemeKind`, each identified under C.2.1 by exact claim content, one EntityOfConcern, and one effective ReferenceScheme. Grounding and representation relations are added only when current; a viewpoint selected for a named describing use remains outside episteme identity.

2. **Value and use projection.** For each episteme `E`—and separately for a named describing use when one is current—EFEM laws may refer to:
   * `content(E) : U.ClaimGraph` — E's exact identity-bearing claim content;
   * `entityOfConcernRef(E) : U.EntityRef` — designates E's exact EntityOfConcern;
   * `selectedViewpointRef?(use) : U.ViewpointRef` — only when the named describing use selects one exact viewpoint; this is not a component of E's identity;
   * `referenceScheme?(E) : U.ReferenceScheme` — E's effective designation and interpretation scheme;
   * `representationSchemeRef?(E) : U.RepresentationSchemeRef` — only when an exact C.29 representation scheme and correspondence relation are current for E; this is not a C.2.1 identity component;
   * a separately current neighboring fact — name the exact `EpistemeEditionRelation`, exact A.10 evidence or provenance relation, or other governed predicate and its participants when the arrow family reads or compares it; do not collect these facts in a generic projection. If E asserts such a fact, that assertion is already part of `content(E)`.

   When grounding matters, name the exact grounding relation, its grounding holon, and the claims it covers; grounding is not another component of episteme identity.

3. **Derived `EntityOfConcernChangeMode` and subtype restriction.**
   Each admitted arrow receives its mode from its resolved endpoint EntitiesOfConcern:

   * `entityOfConcernChangeMode(f) = preserve` when X and Y concern the same exact entity; a current grounding relation remains a separately governed fact;
   * `entityOfConcernChangeMode(f) = retarget` when X and Y concern independently different entities. Any claim that `f` supports one receiving use is a separate A.6.4 bounded-use assertion `q`; its ClaimGraph states the invariant, visible loss, receiving use, conditions, and affirmative or negative polarity. A current-case judgement separately tests the exact facts.

   The parent EFEM class contains both modes. A named species or subtype may admit only one mode, but that restriction does not by itself make the subtype closed under composition. Classify each composite again from its final endpoints under P3.
4. **Legacy SubjectRef and describing-use discipline.**
   For Description epistemes, including those admitted for specification use, resolve legacy `subjectRef(E)` to exact E and its EntityOfConcern. State which endpoint claim content, EntityOfConcern, and effective scheme are preserved or differ. When grounding or a selected describing-use viewpoint matters, name the exact occurrence or use qualification on each side and state which facts the rule reads or compares. Any occurrence change follows its direct relation pattern, while viewpoint selection and conformance remain separately claimed.

##### A.6.2:4.3.2 - P1 — Effect-free arrow, separate execution

The mathematical statement `f : X -> Y` records only the arrow and its laws. A claim that a system computed, authored, stored, transmitted, or published Y requires the corresponding application, Work, result, or publication facts separately.

When a system actually measures, simulates, translates, normalizes, fits, or otherwise produces or changes an episteme, identify separately:

* the exact A.6.1 operation application and its argument and result bindings, when that declaration is current;
* the system and any performed Work;
* the affected or newly constituted episteme and its C.2.1 identity facts; and
* any production, evidence, publication, or reliance relation that actually obtains under its own direct governor.

The same arrow can relate already existing epistemes, or be used in several separately identified applications. Conversely, two applications do not become the same because they use the same arrow. When a result or production relation is current, identify its separately governed application and exact result facts.

##### A.6.2:4.3.3 - P2 — Claim conservativity (no unlicensed commitments)

Let `content_X = content(X)` and `content_Y = content(Y)`, with their effective ReferenceSchemes and exact EntitiesOfConcern. Interpret each ClaimGraph through its effective scheme. Name any additional exact source episteme, current fact, grounding relation, or scheme correspondence that the arrow rule actually admits; an entity or label by itself is not a claim premise. Then:

> Every assertion in `content_Y` must be recoverable as a logical consequence, conservative re-expression, selection, or declared aggregation of the identified source ClaimGraphs and exact admitted facts under the named schemes. This includes assertions about an episteme's edition, source, status, witness, provenance, or evidence. Calling an assertion metadata does not exempt it from P2.

An EFEM arrow may omit claims or conservatively reorganize and re-express them. It may not introduce an unsupported atomic commitment, silently widen claim scope, or cross a ReferencePlane without the exact relation required for that move.

A separately obtaining edition, provenance, evidence, or status relation remains outside episteme identity. If the arrow family compares such a relation across X and Y, name the exact predicate and participants on each side. The arrow records that comparison; it does not create or update the relation. If Y asserts the relation, that assertion is identity-bearing `content_Y` and must pass the same source-to-result trace as every other assertion.

Where `entityOfConcernChangeMode(f) = retarget`, the arrow declaration states its formal cross-entity correspondence; it does not itself establish conservativity for a receiving use. A separate A.6.4 bounded-use assertion `q` states the invariant, visible loss, receiving use, conditions, and polarity, and a current-case judgement separately tests the exact facts. An ordinary time-to-frequency representation of the same signal instead routes through C.29 and A.6.3.RT. A Fourier relation enters a retargeting case only after C.2.1 independently identifies a different receiving EntityOfConcern.

##### A.6.2:4.3.4 - P3 — Category structure and EntityOfConcern mapping

Use this law only after the selected FormalSubstrate declares both categories and the mapping below. `Ep` has admitted exact epistemes as objects and admitted EFEM arrows as arrows. It is a category only when it contains the required identities and every composite of admitted arrows with a matching middle episteme. If that closure is absent, keep the individual arrows and do not claim this category or functor.

`EoCBase` is the endpoint-only thin category over the exact resolved EntitiesOfConcern represented in the substrate. For every admitted pair `A,B`, it contains one formal arrow `u_{A,B}`. Its only endomorphism at A is `u_{A,A}=id_A`, and `compose(u_{B,C},u_{A,B})=u_{A,C}`. This formal arrow records only endpoint identity or difference; it is not an F.9 Bridge, a domain relation, or a claim that any world-side relation obtains.

```text
α : Ep -> EoCBase
```

On objects, `α(X)` is the exact EntityOfConcern resolved through `entityOfConcernRef(X)`; the reference is only the means of resolution. For `f : X -> Y`, `α(f)=u_{α(X),α(Y)}`. Thus a preserve-mode arrow maps to the base identity even when f is not an identity arrow in Ep, while a retarget-mode arrow maps to the unique formal arrow between its different endpoint entities. `α` intentionally forgets the rule that distinguishes two Ep arrows with the same endpoint entities.

**Practitioner check.** Point to exact X, Y, and f; resolve both EntitiesOfConcern; and identify the resulting endpoint arrow. For a proposed composition, point to the exact middle episteme and the admitted composite, then check P0-P2 for that composite. If the family lacks a required identity or composite, use its individual arrows without claiming the category or functor. No extra proof or record is required unless the receiving use calls for one.

1. **Identities.** For each admitted episteme X, Ep contains `id_X : X -> X`. For every `f : X -> Y`:

   ```text
   dom(id_X) = X
   cod(id_X) = X
   compose(id_Y, f) = f = compose(f, id_X)
   α(id_X) = id_α(X)
   ```

   `id_X` preserves the episteme's claim content, EntityOfConcern, effective ReferenceScheme, and every other declared episteme value. A viewpoint selected for one named describing use remains a separate use qualification.

2. **Composition.** For admitted `f : X -> Y` and `g : Y -> Z`, Ep contains an admitted `h = compose(g,f) : X -> Z`; h must satisfy P0-P2. It also satisfies:

   ```text
   dom(h) = X
   cod(h) = Z
   α(h) = compose(α(g), α(f))
   compose(k, compose(g,f)) = compose(compose(k,g), f)
   ```

   The α equation is replayable from endpoints. For a retargeting round trip from entity A through B back to A, both sides are the unique base endomorphism `u_{A,A}=id_A`; this says nothing about inverse world-side relations or identical Ep arrow rules. The composite has `preserve` mode when X and Z concern the same exact entity and `retarget` mode when they concern different entities.

   A preserve-only or retarget-only subtype is not thereby closed under parent composition. A composite remains in that subtype only when its final mode and all additional subtype laws match; otherwise it remains an EFEM arrow in the parent class. A separate `q` states the final-use invariant, accumulated visible loss, receiving use, conditions, and polarity; a separate current-case judgement tests the final facts.

3. **Scheme-aware composition.** If endpoint RepresentationSchemes or effective ReferenceSchemes differ, name the exact C.29 or A.6.3.RT correspondence used by each route and state the equality or declared equivalence that makes the two routes agree. Use `natural`, `oplax`, or similar terminology only when the substrate supplies the actual mapping, comparison arrow, diagram, and working probe. Otherwise state the required two-route agreement in ordinary language. Any witness episteme remains separately identified.

##### A.6.2:4.3.5 - P4 — Arrow and repeat boundary

The common EFEM model treats `f : X -> Y` as one arrow with exact endpoints, an arrow rule or designator, and declared formal equivalence. It does not treat every arrow as a function that can be evaluated on an object, and it makes no claim that a separately declared operation is deterministic. A concrete substrate may add an evaluation operation only after declaring its argument kind, result kind, and relation to these exact arrows; that extra operation is not part of the common EFEM laws.

No universal idempotence follows. A normalization or another endomorphism `f : X -> X` may separately claim a repeat law such as `compose(f,f) ≃ f` only when composition is defined on the declared domain, `≃` is the substrate's stated equivalence, and a working fixture or proof supplies the witness. This mathematical repeat claim is not evidence that an operation was executed twice.

##### A.6.2:4.3.6 - P5 — Formal domain and separate use conditions

Each arrow family states the formal domain in which its laws apply:

* the allowed kinds of the two exact endpoint EntitiesOfConcern;
* any exact grounding relations or endpoint facts that the arrow rule reads;
* the admitted RepresentationScheme and ReferenceScheme pairs and any C.29 or A.6.3.RT correspondence needed by the formal relation; and
* any ClaimScope constraint required by the arrow law itself.

If `X` or `Y` lies outside that domain, the arrow is not a member of this local family. This is distinct from an operation application being admitted or rejected. A use-specific scope, operating condition, or selected viewpoint enters `q` only when it changes the invariant, visible loss, receiving use, or conditions; `q` carries affirmative or negative polarity, and a separate current-case judgement tests exact facts against it. Changing either does not reidentify the arrow.

When the use also relates two exact F.17 local senses and the F.9 predicate obtains, cite that Bridge and a separate bounded-use claim. When it crosses a ReferencePlane, cite the applicable plane relation. If transport is performed, identify the A.6.1 application separately. Different labels, contexts, schemes, planes, or operating conditions alone create none of these relations.

### A.6.2:5 - Archetypal Grounding (Tell–Show–Show)

The examples below show how EFEM is intended to be used across the EntityOfConcern and Description-episteme boundary, specification-use refinements, and Viewpoint/MVPK publication lanes.

#### A.6.2:5.1 - Typed specification-use refinement `Specify_DescEp_SpecDesc` (species of EFEM)

*Context.* You have a `U.MethodDescription` for a safety check and want a more formal `U.MethodSpec` with checkable constraints or test-harness obligations about the same Method. Before calling the relation conservative, identify the exact claims that already support those constraints.

*Shape.*

* Domain: `X = U.MethodDescription` episteme with `entityOfConcernRef(X) : U.MethodRef`, `content(X) : U.ClaimGraph_D`, and `ReferenceScheme_D`; when the named engineering validation use selects viewpoint P, record that selection separately.
* Codomain: `Y = U.MethodSpec` episteme with the same `entityOfConcernRef(Y) = entityOfConcernRef(X)`, more structured `content(Y) : U.ClaimGraph_S`, and a more explicit ReferenceScheme. If the same named validation use continues, it preserves its selected viewpoint P separately.

`Specify_DescEp_SpecDesc` is a species of EFEM only when all of these hold:

* `entityOfConcernChangeMode(Specify_DescEp_SpecDesc) = preserve`. The shared Method establishes endpoint EntityOfConcern equality; the Method entity itself is not a logical premise.
* P1 — effect-free: it is the declared arrow between the two epistemes; any operation application that produces Y is separate.
* P2 — conservative: every behavioral claim, constraint, and test obligation in Y traces to exact claims in X, an additional named source episteme, or an independently current fact under its named relation and effective scheme.
* P3-P5 — category structure and scope: the declared arrows compose only when their exact endpoints and P3 mappings agree, and applicability is bounded by the named engineering scope, operating conditions, effective scheme, and any viewpoint selected for the named validation use.

If an author chooses a new threshold, acceptance condition, harness obligation, or other commitment not supported by that basis, Y has been strengthened and the proposed arrow fails P2. Identify the new assertion in Y's changed ClaimGraph. When a particular application or Work accounts for that strengthening, identify that occurrence and the direct production relation separately. The new assertion remains outside the conservative arrow; the application, Work, and production relation account for its origin.

Keeping episteme identity, describing use, and production separate matches A.7 and E.10.D2. Under C.2.1, each Description episteme is identified by its complete claim content, its own exact EntityOfConcern reference, and its effective ReferenceScheme; any describing use or production relation is separately identified. `Specify_DescEp_SpecDesc` is an optional EFEM species once a specification-use or refinement gate admits that use. E.10.D2 governs specification-use admission, A.7 governs the Description/Specification distinction, and the declared `Specify_DescEp_SpecDesc` arrow carries the episteme-to-episteme relation.

#### A.6.2:5.2 - Internal normalisation of a View (species of EFEM, `entityOfConcernChangeMode = preserve`)

*Context.* In MVPK you compute an engineering view `V` of a system description; you then normalise the view (sort, factor, put equations into normal form) without changing what it says.

Let `X = V_raw`, `Y = V_norm`, both `U.EpistemeView` instances with the same:

* `entityOfConcernRef(X) = entityOfConcernRef(Y)` (same system);
* when grounding is current, the same exact grounding occurrence and grounding holon are found on both sides; this is an endpoint comparison, not a change made by `NormalizeView`;
* any viewpoint selected by the named normalization use is the same exact P for X and Y; this selection is outside episteme identity;
* `representationSchemeRef(X) = representationSchemeRef(Y)` (same notation).

The EFEM `NormalizeView : X→Y`:

* has `entityOfConcernChangeMode(NormalizeView) = preserve`;
* has a source-to-receiving ClaimGraph difference consisting only of the declared normalization. If an exact `EpistemeEditionRelation` or another neighboring relation matters, name its predicate and participants on each side and compare the endpoint facts; `NormalizeView` does not change that occurrence. An assertion such as “normalised at edition E” is part of Y's ClaimGraph and must pass P2;
* is effect-free and separately claims idempotence on the output-closed domain of valid `EpistemeView` values under the fixed scheme and normalization rules; equality means exact normalized ClaimGraph equality plus equality of all identity-bearing episteme values, and a fixture that composes `NormalizeView` with itself supplies the repeat witness (P4);
* is conservative (P2): no new claims, only re‑expression.

MVPK can then **assume** functoriality of such normalisations without re‑stating the EFEM laws.

#### A.6.2:5.3 - Retargeting sketch (`entityOfConcernChangeMode = retarget`)

*Context.* E.18 structural reinterpretation relates a physical-layout episteme to a functional-behaviour episteme. The EntityOfConcern changes from the physical assembly to the functional network.

Inside EFEM, this becomes a species with `entityOfConcernChangeMode = retarget`:
* input episteme describes `S₁` (e.g. a component hierarchy holon);
* output episteme describes `S₂` (e.g. a functional network holon);
* one exact arrow `r` relates the two endpoint epistemes under its declared formal rule; a separate A.6.4 assertion `q` states the invariant, visible loss, bounded receiving use, conditions, and polarity; and a current-case judgement separately tests the exact facts;
* P2 checks only the formal consequence relation declared for `r`; the ordinary current-case judgement tests the exact facts against `q`, and A.20 enters only when that proposition is an internal constraint.

The details belong to A.6.4 and E.18; EFEM provides the generic discipline.

#### A.6.2:5.4 - Worked endpoint-value and relation-read profile (engineering SystemDescription episteme kind)
*(informative)*

To make the C.2.1 value and EFEM law discipline concrete, consider an engineering episteme of a dependent system-description kind whose exact EntityOfConcern is one `U.System`:

| Value named by the EFEM species | Kind or reference form | Use |
| --- | --- | --- |
| exact EntityOfConcern | `U.Entity` constrained to `U.System`; designated by `U.EntityRef` | identifies the system that the claims concern |
| claim content | `U.ClaimGraph` | carries the description or specification claims |
| effective ReferenceScheme | `U.ReferenceScheme` | makes the claims and their designations interpretable |

This table names the three values that identify an episteme; it is not a `RelationSignature` or SlotSpec table. `EntityOfConcernSlot`, `ClaimGraphSlot`, and `ReferenceSchemeSlot` are declaration-local SlotKinds only when the reusable C.2.1 `EpistemeConstitutionRelationSignature` is being inspected. An EFEM species states how the endpoint values compare. If its rule uses a selected viewpoint, empirical-grounding relation, or representation relation, it names the exact occurrence or use qualification separately and reads or compares the endpoint facts without changing the occurrence.

Two typical EFEM species over this kind are:
* `Specify_DescEp_SpecDesc_Sys : SystemDescription → SystemSpec` — an `EntityOfConcernChangeMode = preserve` species that:
  * relates independently identified source and receiving epistemes with the same exact EntityOfConcern, makes their effective ReferenceSchemes explicit, and cites any separately obtaining empirical-grounding relation or viewpoint selection only when the formal relation depends on it;
  * satisfies P2 only when every claim in the receiving specification is recoverable from exact source ClaimGraphs or independently current facts under named relations and schemes; the unchanged EntityOfConcern is an endpoint identity condition, not a proposition or additional premise;
  * satisfies C.2.1:7.1 by declaring its endpoint-value comparison, named relation-read profile, and change mode.

* `Normalize_EngView : EpistemeView → EpistemeView` — a view‑normalisation EFEM (again with `EntityOfConcernChangeMode = preserve`) that:
  * states how the formal relation uses the three C.2.1 identity values and makes the exact source-to-receiving ClaimGraph difference explicit; any difference between separately obtaining endpoint facts that it compares is named by the exact predicate and participants, and any normalization application remains separate;
  * is effect-free and separately claims idempotence on its output-closed engineering-view domain under the fixed scheme and normalization rules; equality means exact normalized ClaimGraph equality plus equality of all identity-bearing episteme values, and a composition fixture supplies the repeat witness (P4);
  * is conservative (P2) by construction: it never introduces new atoms about the selected system.

Concrete `A.6.3/A.6.4/E.17.*` patterns for engineering description and specification-use idioms state explicitly, under C.2.1:7.1 and `CC-EFEM.*`, which of the three C.2.1 endpoint values remain the same or differ and which exact separately obtaining relation occurrences their arrow rules read or compare.

### A.6.2:6 - Bias-Annotation

* **Episteme‑first, world‑second.** EFEM relates epistemes as mathematical objects. For measurement or execution, identify the capable system, the A.6.1 application when current, the Work it performs, the resulting episteme, and any production relation separately.

* **Actual values, not unnamed fields.** Laws name the exact claim content, EntityOfConcern, and effective ReferenceScheme they use and keep empirical grounding, representation, view conformance, and describing-use viewpoint selection separate. A SlotKind is mentioned only when the exact reusable relation declaration is current.

* **Arrow domain and use-local semantics.** EFEM names the formal domain of each arrow family. A separate `q` carries the receiving-use invariant, visible loss, conditions, and polarity; a current-case judgement separately tests the exact facts. Scope, operating conditions, and selected viewpoint enter only when they change that proposition or judgement. An obtaining semantic Bridge between two exact local senses, a ReferencePlane relation, and any transport application remain separately identified; no implicit cross-local or cross-plane EFEM is permitted.

* **EntityOfConcern and Description-episteme boundary and specification-use/refinement respect.** EFEM never collapses an EntityOfConcern with a Description episteme or with a specification-use refinement. C.2.1 identifies each Description episteme directly; any authoring, measurement, observation, model, source-use, representation, or refinement relation is stated only when it is current. A specification refinement can be represented by an EFEM arrow only after an exact specification-use or refinement gate admits it; any application that produces the refined episteme remains separate.

### A.6.2:7 - Conformance Checklist (normative)

| ID                                                  | Requirement                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC-EFEM.1 (Typed episteme objects).** | Every arrow presented as an effect-free episteme morphism SHALL have exact domain and codomain epistemes whose C.2.1 claim content, EntityOfConcern, and effective ReferenceScheme are recoverable. The FormalSubstrate declaration names which of those three values it uses and which exact separately obtaining relation occurrences its rule reads or compares. Those occurrences retain their independently established currentness; any change follows the direct relation pattern. A.6.5 SlotSpecs are required only for an exact reusable relation declaration and remain local to that declaration. |
| **CC‑EFEM.2 (Derived EntityOfConcernChangeMode).** | Each arrow family declares `entityOfConcernChangeMode : EpMorphism -> {preserve, retarget}` and derives each arrow's value from its resolved endpoint EntitiesOfConcern: `preserve` for the same exact entity, `retarget` for independently different entities. A named subtype may restrict one value but is closed under composition only when every admitted composite still meets that restriction. Any bounded-use assertion `q` remains separate, and its current-case judgement separately tests exact facts. An F.9 Bridge is additional only for a separate local-sense relation. |
| **CC‑EFEM.3 (Purity).** | An EFEM arrow SHALL assert no Work, mechanism execution, or carrier mutation. If a system constructs or changes an episteme, identify the exact application, bindings, system, Work, and resulting episteme separately; the arrow may then relate the exact epistemes under P2–P5. |
| **CC‑EFEM.4 (Conservativity).** | Each arrow family states which of the three endpoint identity values and which ClaimGraph parts remain the same or differ under the declared schemes and arrow-family conditions. A separate `q` states the receiving-use invariant, visible loss, conditions, and polarity; the current-case judgement reports `satisfies`, `fails`, or `cannot decide` from exact facts. An arrow declaration does not make unsupported output commitments valid. |
| **CC‑EFEM.5 (Category structure and repeat claims).** | Each arrow family names its exact endpoints, arrow rule or designator, declared equivalence, identity and composition conditions. Claim category `Ep` and mapping `α` only when identities and every matching composition close. The resolved endpoint EntitiesOfConcern uniquely determine the thin-base arrow `α(f)`, but they do not identify f itself. A retargeting round trip maps to the thin-base identity and is reclassified from its final endpoints. Idempotence or another repeat claim is added only for an endomorphism whose declared domain makes composition meaningful, with its equivalence and witness stated. Any evaluation operation, deterministic-execution claim, or repeat claim about an operation application is separate and follows that operation's rule. |
| **CC‑EFEM.6 (Formal domain and separate use conditions).** | Each arrow family SHALL state its allowed endpoint EntityOfConcern kinds, any endpoint facts or grounding relations its formal rule reads, admitted schemes and correspondences, and any ClaimScope constraint required by the arrow law. Use-specific scope, operating conditions, or selected viewpoint enter `q` only when they change its invariant, visible loss, receiving use, or conditions; `q` carries polarity, and the separate current-case judgement tests exact facts. When the use also relies on an obtaining Bridge between two exact F.17 local senses, cite F.9 and its separate bounded-use claim; when it crosses a ReferencePlane, cite the applicable plane relation. No context, scheme, plane, or operating-condition difference creates either relation automatically. |
| **CC‑EFEM.7 (Description and specification-use discipline).** | For any `...Description` or `...Spec` episteme, identify exact E and its EntityOfConcern under C.2.1; admit specification use only under E.10.D2; and state which endpoint claim content, EntityOfConcern, and effective scheme are preserved or differ. Name any grounding occurrence and describing-use viewpoint qualification separately and compare only the facts the rule actually reads. Any occurrence change follows its direct relation pattern; viewpoint selection and E.17.0 conformance require their own claims. |
| **CC-EFEM.8 (Endpoint-value and relation-read declaration).** | Any EFEM species SHALL declare its morphism family and change mode and compare the three C.2.1 endpoint identity values. It SHALL name every empirical-grounding, representation, or conformance occurrence and every describing-use viewpoint qualification that its rule reads, together with the endpoint facts compared. Those occurrences retain their separately governed current values. Any actual relation change follows its direct pattern, and any producing activity follows its exact application and Work. |

### A.6.2:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| EFEM as performed work | An episteme rewrite is treated as measurement, actuation, or work occurrence. | Use EFEM only for episteme-to-episteme morphisms; use A.15 when work in the world is current. |
| EFEM as publication rendering | A face, carrier, or rendering change is treated as the episteme morphism itself. | Use E.17 for publication forms and use EFEM only for the episteme relation being represented. |
| Retargeting as harmless view | Endpoint epistemes concern different entities, but the bounded-use proposition or current case remains unstated. | Identify the A.6.4 arrow; write `q` with its invariant, visible loss, use, conditions, and polarity; then report the current-case judgement from exact facts. Add F.9 only for a separate local-sense relation. |
| Representation lens as ontology | A category arrow, graph, or mapping notation is treated as a new root U-kind. | Keep the mathematical object as the lens over the EFEM relation and keep U-kind settlement in E.24/C.3. |

### A.6.2:9 - Consequences

* **Single place for episteme‑to‑episteme laws.**
  Effect-free arrow families used across KD‑CAL, MVPK, E.18, and discipline packs can reuse one local law set instead of re-inventing it. Each actual application and use claim remains separate.

* **Clear separation from mechanisms & work.**
  Measurement, execution, and simulation require a capable system, the applicable A.6.1 operation application when current, and performed `U.Work`; identify any resulting episteme and production relation separately. EFEM remains effect-free and compositional. Any semantic correspondence, temporal qualification, evidence, or reliance claim remains under its own pattern.

* **Stable backbone for Viewing & Retargeting.**
  A.6.3 and A.6.4 do not need to repeat P0–P5; they specialise EFEM with additional constraints (preserve/retarget). Other patterns (e.g. MultiViewDescribing, MVPK, E.18 structural reinterpretation) can depend on EFEM as a stable base.

* **Value-and-relation clarity.**
  By requiring each EFEM species to compare the three C.2.1 identity values and name the exact separately obtaining relations its rule reads, the pattern keeps an EntityOfConcern, a declaration-local SlotKind, and a reference to the entity distinct. Equal or different endpoint relation facts are a comparison result, not an effect of the arrow.
* **Better didactics.**
  When a didactic expression–meaning–subject triangle is useful, map its three positions explicitly to the effective ReferenceScheme, ClaimGraph, and EntityOfConcern of the current episteme. Keep viewpoint, empirical grounding, representation, and reference as separately named neighboring relations rather than extra triangle slots.

### A.6.2:10 - Rationale

**Why a separate EFEM pattern (A.6.2) instead of folding into A.6.1 or C.2.1?**

* A.6.1 defines Mechanism declarations and their separately identified applications, including operational guards and time conditions. A.6.2 instead defines a local mathematical arrow class. Any semantic Bridge, plane relation, transport application, or Work remains under its direct pattern.
* C.2.1 fixes episteme identity through claim content, exact EntityOfConcern, and effective ReferenceScheme and keeps neighboring direct relations separate, but does not define morphisms. EFEM is a morphism-level pattern over those values and relations.

This split mirrors how A.6.0 separates a declaration from what later uses it: C.2.1 says what an episteme is; A.6.2 states the laws of a local episteme-to-episteme arrow family; A.6.1 and A.15 govern any application and Work.

**Why insist on EntityOfConcernChangeMode?**

Because a relation can look like a harmless view even though its endpoint epistemes concern different entities—for example, component assembly and function bundle. Declaring `preserve` versus `retarget` exposes that endpoint distinction. It does not make the arrow fit for a use: the separate `q` states the invariant, visible loss, receiving use, conditions, and polarity, and the current-case judgement separately tests the exact facts.

**Why name actual values and exact relation reads instead of informal fields?**

FPF distinguishes actual participants and their references from the declaration-local SlotKinds used in a reusable `RelationSignature`. Reusing that distinction here:

* aligns episteme morphisms with the framework's direct-relation architecture;
* enables checks that an EFEM species compared only the three declared endpoint values, read only the named neighboring occurrences, and left any actual relation change to its direct pattern and producing application or Work;
* avoids minting another generic parameter, field, or relation-role vocabulary.

### A.6.2:10.1 - SoTA-Echoing

**Practice question.** What current transformation practice supports reusable definitions and composition while keeping execution and correctness evidence separate, and does it justify a universal repeat law?

| Source or practice | Contribution used here | Limit and disposition | A.6.2 locus changed |
| --- | --- | --- | --- |
| [Zhao et al., *KBX: Verified Model Synchronization via Formal Bidirectional Transformation* (2024)](https://arxiv.org/abs/2404.18771) | Separates formal BX definitions, generated synchronization, and consistency verification. | **Adapt.** Supports the declaration, arrow, application, and use-claim split. Its formal synchronizer does not make every arrow effect-free or idempotent in FPF. | Sections 4.1, 4.2, P1, and CC-EFEM.1-5. |
| [He and Zan, *BIT: A template-based approach to incremental and bidirectional model-to-text transformation* (2024)](https://doi.org/10.1016/j.jss.2024.112148) | Separates a user-facing surface language, formal core semantics, printer/parser execution, round-trip properties, and empirical cases; it also treats some computational effects explicitly. | **Adapt.** Supports a readable first route and explicit effect boundary. BIT's round-trip laws are construction-specific, not a universal EFEM idempotence law. | P1, P3-P4, examples, and CC-EFEM.3-5. |
| Category, optic, fibration, cospan, and BX traditions | Supply durable mathematical lineage for arrows, identities, composition, views, and correspondences. | **Retain as lineage.** Use only through a declared C.29/FormalSubstrate lens. Reject automatic F.9 Bridge, EntityOfConcern decision, or idempotence. | P0-P5 and Relations. |
| Current FPF C.2.1, C.29, A.6.3.RT, and A.6.4 | Separate episteme identity, mathematical representation, same-entity representation change, and changed-entity retargeting with a use-specific claim. | **Adopt.** These are the direct FPF boundaries. | P0-P2, the Fourier branch, and the worked cases. |

The thin EFEM arrow class is a bounded FPF synthesis. Reopen it if a current transformation practice needs a different arrow identity or effect boundary, or if a concrete composition cannot be stated without collapsing the declaration, application, or correctness claim.

### A.6.2:11 - Relations

* **Specialises / is specialised by.**

  * Builds on A.6.0 `U.Signature` for direct subject, range, optional result, slice, and extent components together with Vocabulary, Laws, and Applicability; coordinates with A.6.1 `U.Mechanism` without making mechanism application part of EFEM.
  * Refined by the A.6.3 EntityOfConcern-preserving viewing branch and the A.6.4 EntityOfConcern-retargeting branch.

* **Constrained by.**
  A.6.5 declaration-local SlotSpec discipline; C.2.1 episteme constitution and any separately current empirical-grounding or edition relation; E.10.D2 for the EntityOfConcern, Description-episteme, describing-use, and specification-use boundary; Part F for exact local-sense or ReferencePlane relations; and E.10 for naming discipline.

* **Consumed by.**
  E.17.0 `U.MultiViewDescribing` (families of Description epistemes, including Description epistemes admitted for specification use, under Viewpoints); E.17 (MVPK — publication as species of Viewing/EFEM); E.18 (structural reinterpretation and other transformation-flow relations over epistemes); KD‑CAL/LOG‑CAL rules that reason about episteme transforms categorically.

### A.6.2:End

