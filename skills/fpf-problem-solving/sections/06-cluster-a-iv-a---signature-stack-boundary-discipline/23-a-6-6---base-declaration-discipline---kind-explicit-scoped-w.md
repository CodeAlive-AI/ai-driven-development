## A.6.6 - Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)
> **Status:** Stable
> **Type:** Definitional relation-discipline pattern

**Plain-name.** Scoped witnessed base declaration discipline.

**Use this pattern when** a dependent content is admissible, usable, interpretable, comparable, publishable, or actionable only relative to an explicit base through a declared base relation, scope and time condition, and witness set.

**What goes wrong if missed.** Umbrella words such as anchor, support, ground, attach, or based-on hide the relation kind, endpoint kinds, scope, time, and witness discipline; authors then rename endpoints or flip directions instead of repairing the relation.

**What this buys.** The project gets a scoped witnessed base declaration with typed dependent and base slots, explicit baseRelation, scope and time condition, witnesses or pins, and named change classes for rebasing, retiming, or withdrawing the declaration.

**E.24.UK settlement.** A.6.6 does not admit `U.BaseDeclarationDiscipline` as a durable U-kind. The pattern defines or constrains base-declaration discipline. It retains `U.ScopedWitnessedBaseDeclaration` only as a dependent durable declaration value under the A.6 signature and slot-relation settlement: a scoped declaration that relates dependent content to an explicit base through a declared base relation, scope and time condition, and witnesses. Local support wording, anchor wording, source pointers, publication records, and witness carriers do not become U-kinds by appearing in this discipline.

**Status.** Normative (Core).

**Placement.** Part A, cluster A.IV “Signature Stack & Boundary Discipline”; adjacent to A.6.5 relation-declaration slot discipline.

**Depends on.**
– A.6.0 `U.Signature` (universal signature carrier).
– A.6.5 relation-declaration slot discipline (SlotKind, ValueKind, and RefKind stratification plus the slot-operation lexicon).
– A.2.6 (Scope discipline; explicit `Γ_time`; implicit “latest/current” is forbidden).
– A.2.4 evidence-use and status-use relation discipline for decision-relevant witness sets, including timespan, provenance, scope, polarity, and freshness constraints.
- A.7 (Strict Distinction; EntityOfConcern vs Description-episteme and specification-use cases vs publication face, form, unit, carrier, and rendering lanes).
– E.8 (pattern authoring order & SoTA discipline).
– E.10 and E.10.D1 for wording-use recovery, with F.0.1 and F.17 for source-local meaning and its optional durable address.

**Coordinates with.**
– A.10 Evidence–Provenance DAG discipline (`verifiedBy`, `validatedBy`).
– A.14 per-edge constructive grounding (`tv:groundedBy`) and `validationMode` discipline.
- C.2.1 episteme constitution through exact claim content, EntityOfConcern, and effective ReferenceScheme, plus the separately obtaining `EpistemeEmpiricalGroundingRelation` between an exact episteme and grounding holon.
– A.6.3 `U.EpistemicViewing` (`EntityOfConcernRef`-preserving view operators; base-relative “how” without retargeting).
– A.6.4 `U.EpistemicRetargeting` (base-change along `KindBridge`; retargeting lexicon and continuity rules).
– C.3.3 `U.KindBridge`, including the `CL^k` value declared for that bridge (explicit repair or translation when exact endpoint kinds differ; no silent re-typing).
– E.18 assurance-operations on `U.Transfer` (`CalibrateTo`, `CiteEvidence`, `AttributeTo`, `ConstrainTo`, …).
– F.9 Bridge relations and the `CL` value declared for each relation when the declaration actually consumes a relation between distinct F.17 local-sense cells or ReferencePlanes; cite the exact relation and its admitted use.
– F.15 F-Suite validation harness (carrier/source-currentness, provenance, and refresh governance).
- F.18 naming governance (Tech/Plain twins and publication-lane naming boundaries).

**Source phrases and red-flag cues (informative; not normative vocabulary).**
– “anchoring / anchor” (source umbrella colloquial; a red-flag token for *under-described dependence*). **Prohibited in Tech register** as a meaning-surrogate; treat it as a defect to be rewritten into an explicit `baseRelation(dependent, base)` form. Allowed only when referring to a **pattern-defined primitive** that already reserves the word (e.g., E.10 MG‑DA *Domain Anchoring*; evidence/pin “anchors” where the term is explicitly reserved), or inside quoted source text that is immediately followed by a conformant rewrite.
– “Qualified statement / attributed edge” (knowledge-graph colloquial).
– “support / supported by / support basis / support relation” (ordinary umbrella support wording). Diagnostic for possible basedness only when the phrase asserts that a dependent content is admissible, usable, interpretable, comparable, publishable, or actionable relative to an explicit base. Otherwise classify the live reading and apply the governing ontology named by value: source-description, evidence, assurance, causal-use, mathematical-lens, work/resource, publication/navigation, or ordinary help.
– “Pinning” (when witnesses are edition pins).

**Mint‑or‑Reuse note (informative).**
This pattern **mints** the declaration value name `U.ScopedWitnessedBaseDeclaration` (SWBD) and the **base‑change lexicon** operation class names (`declareBase`, `rebase`, `retime`, …) as canonical labels for semantic change classes.
It **reuses** A.6.5 SlotSpec discipline (SlotKind/ValueKind/RefMode), A.2.6 Scope discipline (`U.Scope`, explicit `Γ_time` when time matters), and A.2.4 evidence-use relation discipline as the enforcement substrate for witness use.

### A.6.6:1 - Problem frame

FPF repeatedly needs to express a family of situations of the form:

> **A dependent content is admissible, usable, or interpretable only relative to an explicit base.**

This family appears across disciplines:

* reference selection and identification (IDs, handles, pointers, registries),
* scale/datums/calibration (measurement traceability, baselines, normalisation),
* grounding of properties and abstractions to objects (attribution; “this property is about that thing”),
* admissibility/assurance (claims linked to evidence, checks, or proofs),
* publication discipline (what a statement is fit to be used for, where, and when).

In drafts, authors often reach for a single umbrella metaphor (frequently “anchor/anchoring”). That metaphor collapses **different ontological situations** and **different operation classes**, blocking precise invariants and making perspective-flips inevitable.

> **Deconfliction note (lexical).** This pattern is about *base-dependence in content* (“X is usable relative to B”). It is not about E.10’s **Domain Anchoring** (MG-DA), where “anchoring” is a *lexical* primitive for binding token morphology to the term's selected EntityOfConcern. When you see `anchor*` in a basedness sentence, treat it as a defect unless an explicit baseRelation token is present.
>
> **Deconfliction note (source-local meaning).** This pattern is not a license to use “anchor” for a source, meaning, or the thing that supposedly makes a word mean something. Recover the exact source and edition, effective `ReferenceScheme`, local expression, local-sense claim, and exact supporting passage under F.0.1. Create an F.17 `SchemeSenseCell` or obtaining `LocalSenseBasisRelation` only when a later use needs that durable address or support claim. A small source note or Card may represent an already constituted episteme; its form supplies no meaning and is not an SWBD.
>
> **Deconfliction note (support wording).** This pattern defines or constrains support wording only when the claim being made is base-dependence: `dependent` is usable, admissible, interpretable, comparable, publishable, or actionable relative to `base` via a declared `baseRelation`. It does not govern support as ordinary help, source discovery, reader navigation, work enablement, evidence-use polarity, assurance calculus, causal-use support basis, mathematical-lens use, or publication companion use. Those readings use their ontology of the subject pattern for that claim: source-description, evidence, assurance, causal-use, mathematical-lens, work/resource, publication/navigation, or publication-companion patterns as live. A support phrase that cannot select one support reading remains a cue, not a base declaration.

Like A.6.5, this family also triggers **typing conflicts across viewpoints**: an endpoint may be spoken about in its self-kind while the baseRelation declaration expects a different ValueKind (or a different `refMode`). If that mismatch is not made explicit (SlotSpec + relation-specific constraints), authors “solve” it by renaming ends or flipping direction, and the ontological obligation (bridge / narrowing / retargeting) is lost.

The structural reason for the collapse is consistent: what looks like “one anchoring” in prose is, in fact, a *based declaration* with at least five components:

1) **Dependent** — what is being made admissible/usable/meaningful,
2) **Base** — what it is relative to: reference frame, evidence carrier, standard, policy, or declared entity,
3) **BaseRelation** — the specific relation kind that states *how* dependent depends on base,
4) **Scope/Time** — where/when the declaration holds (`scope` plus explicit `Γ_time` when time matters),
5) **Witnesses / pins** — what justifies or enforces the declaration when it is used for decisions.

Until **BaseRelation** is named, umbrella words (“anchor”, “ground”, “attach”, “based on”) nearly always mean:

> “There is an under-described type of dependence here.”

This pattern introduces a single stable lens — **the based declaration** — and couples it with a strict lexical discipline and an operation lexicon, so that base-dependence can be expressed precisely across domains without collapsing back into metaphor.

### A.6.6:2 - Problem

Typical failure modes this pattern is designed to eliminate:

1. **Relation-kind elision.**
   One verb phrase is used to cover: ID-to-registry reference, claim-to-evidence admissibility, calibration-to-standard, property-to-object attribution, policy gating, etc. Rules and invariants cannot be stated because the relation kind is unspecified.

2. **Perspective flip (dependent-view vs base-view).**
   The same situation is described alternately as “X is anchored/grounded” and “Y is an anchor/ground”, with incompatible naming, hidden directionality, and silent re-typing of the ends.

3. **Base–witness confusion.**
   Evidence, pins, certificates, or proofs are treated as “the base”, even when they are only witnesses for a base relation (or conversely: a true base is treated as a mere witness).

4. **Scope/time collapse.**
   Based declarations are treated as timeless truths; time dependence is smuggled in via “current/latest/recently”, violating explicit `Γ_time` discipline.

5. **`Γ_time` used as a proxy for freshness.**
   Authors treat `Γ_time` as “freshness” or “evidence decay”, collapsing TimePolicy with witness-timespan/freshness predicates.

6. **Decision use without witnesses.**
   Declarations that gate work, publication, or assurance are asserted without a witness/pin, breaking auditability and enabling folklore.

7. **Grounding conflation.**
   “Grounding” is used as if it were one relation, while FPF already distinguishes at least:
   * constructive grounding of a model-edge by a trace (`tv:groundedBy`),
   * situational/empirical grounding of an episteme via a grounding holon (C.2.1),
   * source-local meaning recovery and, when needed, an F.17 `SchemeSenseCell` and `LocalSenseBasisRelation` (not a base declaration).

8. **Slot/basing conflation.**
   A.6.5 disambiguates positions in n-ary relations (SlotKind) vs fillers (ValueKind) vs stored references (RefKind). Umbrella basing language reintroduces confusion at the next layer: “why this link exists” (BaseRelation) is missing, and slot-edit operations are conflated with base-declaration edits.

9. **Anchor relapse (source or meaning surrogate).**
   “Anchor/anchoring” is used to mean “the source”, “the meaning”, “the global reference”, or “the thing that makes this true”. This hides the exact source, scheme, expression, local claim, and any obtaining basis relation behind a metaphor and makes review impossible.

10. **Support bucket relapse.**
    “Support”, “support basis”, “support relation”, or “support record” is used as a generic container for unlike relations. Some cases are SWBD basedness; others are evidence polarity, assurance input, causal-use support basis, mathematical-lens use, work enablement, source-description, publication companion, or ordinary help. Treating all of them as one undifferentiated support relation recreates the same under-described dependence that A.6.6 exists to repair.

### A.6.6:3 - Forces

| Force | Tension |
| --- | --- |
| **Universality vs precision** | One discipline must cover calibration, evidence linking, reference selection, attribution, gating, etc., without collapsing them into one pseudo-relation. |
| **Minimal kernel vs decision auditability** | Few primitives are preferred, but decision-relevant declarations must carry witnesses/pins and explicit time selectors where needed. |
| **Two perspectives, one reality** | Dependent-view and base-view must both be expressible without renaming relation-end meanings or flipping meaning. |
| **Compatibility with A.6.5** | Base declarations introduce slots and edits; they must remain SlotKind/ValueKind/RefKind disciplined and must not collapse slot edits with semantic re-declarations. |
| **Lexical guardrails** | Without strict wording rules, umbrella metaphors will return and erase the structure. |
| **Cross-local integrity** | When a declaration actually depends on a relation between different local kinds, local senses, scopes, or planes, that exact relation must remain explicit and reviewable; different sources alone do not create a Bridge. |

### A.6.6:4 - Solution — The `U.ScopedWitnessedBaseDeclaration` object and its lexicon

#### A.6.6:4.1 - Canonical object

**Definition.** A **`U.ScopedWitnessedBaseDeclaration`** (SWBD) is a first-class base-declaration value shape (a signature in the A.6.0/A.6.5 sense): it reifies “dependent is usable relative to base via baseRelation, under scope/time, witnessed by pins”.

```
U.ScopedWitnessedBaseDeclaration ::=
  〈 * DependentSlot     : SlotContent(VK_dep,  refMode_dep),
    * BaseSlot          : SlotContent(VK_base, refMode_base),
    * BaseRelationSlot  : SlotContent(U.NameToken, ByValue),     // relation-specific token; not free text; not publication-side object*
    * ScopeSlot         : SlotContent(U.Scope, ByValue),         // concretely: ClaimScope | WorkScope | PublicationScope
    * GammaTimeSlot?    : SlotContent(GammaTimePolicy, ByValue)?,
    * WitnessSetSlot?   : SlotContent(VK_wit,  refMode_wit)? 〉
 ```

Where:

* **`DependentSlot`** is the dependent content whose admissibility/usability/interpretation is being constrained.
* **`BaseSlot`** is the base, such as a reference frame, target, declared entity, standard, policy, or evidence carrier, that the dependent is declared relative to.
* **`BaseRelationSlot`** is a **declared relation/predicate/operator token** (a vocabulary element with a signature and relation-specific constraints) that states the precise kind of dependence. It is not a prose metaphor and is not a `publication-side object`/publication carrier.
* **`ScopeSlot`** is an explicit USM scope object (`U.Scope`): Claim scope (**G**), Work scope, or Publication scope.
* **`GammaTimeSlot`** is an explicit time selector/policy when time-dependent assumptions exist.
* **`WitnessSetSlot`** is a set of witness references/pins establishing justification or enforcement when the declaration is used for decisions.

**Notation.** `SlotContent(VK, refMode)` is a compact shorthand for “a slot whose SlotSpec declares `ValueKind=VK` and `refMode ∈ {ByValue | RefKind}` (A.6.5)”.

**SlotSpec note.** `VK_*`, `RK_*`, and `refMode_*` above are **not** “anything goes”: they are fixed by the selected `BaseRelationSlot` vocabulary entry and must be declared as SlotSpecs (A.6.5). In other words, SWBD is a reusable *shape*, but the selected local `baseRelation` declaration makes it a concrete, typed signature.

**Instance/prose notation note (convention).** In the prose and examples below, the slot fillers are written as `dependent`, `base`, `baseRelation`, `scope`, `Γ_time`, `witnesses` (no `*Slot` suffix). The `*Slot` suffix is reserved for SlotKinds/positions only (A.6.5 / E.10).

**Well-formedness constraints.**
* **WF‑BD‑1 (No kind-elision).** A base declaration is well-formed only if `BaseRelationSlot` is present and points to a declared vocabulary element with a known signature.
* **WF‑BD‑2 (No silent re-typing).** `DependentSlot` and `BaseSlot` type-check against the `baseRelation` vocabulary entry (ValueKinds + `refMode`). If the intended endpoint kinds do not match, the repair option is explicit (Bridge, narrowing, or explicit retargeting), rather than a rename.
* **WF‑BD‑3 (Time explicit when time matters).** If the declaration’s interpretation depends on time, `GammaTimeSlot` is explicit; “latest/current” is not a substitute.
* **WF‑BD‑4 (Decision use requires witnesses).** If the declaration is used for assurance, gating, or admissibility decisions, `WitnessSetSlot` is non-empty and resolvable.
* **WF‑BD‑5 (Edition fence for decision/publication).** An SWBD that is cited by PublicationScope or used for decision is immutable per edition: any permitted change class is represented as a new declaration linked via explicit continuity/withdrawal, not as an in-place rewrite.
* **WF‑BD‑6 (No silent cross-local reuse).** If an SWBD consumes a relation between different exact local kinds, distinct F.17 cells, translated scopes, or ReferencePlanes, it cites the applicable C.3.3, F.9, scope, or plane relation and the limits of the receiving use. Merely drawing dependent and base from different sources does not create a Bridge. No informal “it is the same entity anyway” prose is an admissible substitute.

This is the discipline-level analogue of A.6.5’s move: disambiguation is achieved by making the missing structural component explicit and non-optional in decision-relevant contexts.

#### A.6.6:4.2 - Underlying mathematical lens

SWBD reifies a **kind-labelled dependence arrow over a base**:

* a dependence edge **(dependent → base)**,
* labelled by a declared **relation token** (`baseRelation`),
* qualified by explicit **scope** and (when time matters) explicit **`Γ_time`**,
* optionally supported by a **witness set** (mandatory for decision use).

This “object over a base” lens is stable across disciplines:
calibration is “measurement over standard”, admissibility is “claim over evidence”, attribution is “property over object”, and constructive grounding is “edge over trace”.

#### A.6.6:4.3 - Slot discipline for SWBD

Any signature that introduces SWBD (or SWBD-like relations) SHALL define SlotSpecs per A.6.5: every position declares **SlotKind / ValueKind / RefKind-or-ByValue**.

Recommended canonical SlotKinds for SWBD:

* `DependentSlot`
* `BaseSlot`
* `BaseRelationSlot`
* `ScopeSlot`
* `GammaTimeSlot`
* `WitnessSetSlot`

**Slot vs filler guard.** `*Slot` names the **position** (SlotKind), not a container relation. In prose, say “fills `BaseSlot` with …” or “uses `baseRef` …” rather than calling the base itself “a BaseSlot”. (`Slot` suffix is structural; E.10.)

**Slot-level invariants (derived from WF‑BD‑1..4; testable).**
* **Invariant (SlotSpec completeness).** In any SWBD signature, the SlotSpec for `DependentSlot` and `BaseSlot` declares admissible `ValueKind` and `refMode` explicitly (A.6.5). If those types cannot be stated, the `baseRelation` vocabulary entry is not yet defined.
* **Invariant (Relation tokenness).** `BaseRelationSlot` holds a declared `U.NameToken` that resolves to a vocabulary entry with a known signature and relation-specific constraints (A.6.0 + A.6.5). It is not free text and is not typed as a publication-lane object (`publication-side object*`).
* **Invariant (Scope objectness).** `ScopeSlot` holds a `U.Scope` object (ClaimScope/WorkScope/PublicationScope) and is not replaced by “where it applies” prose.
* **Invariant (Time gating).** If time-dependent assumptions exist, the SWBD includes `GammaTimeSlot` carrying a `GammaTimePolicy` (WF‑BD‑3).
* **Invariant (Witness gating).** If the declaration participates in assurance/gating/admissibility decisions, the SWBD includes a non-empty, resolvable `WitnessSetSlot` (WF‑BD‑4).

**Field naming guard (implementation; informative).** When materialising SWBD as a record or representation, implementations SHOULD avoid naming data fields with the `*Slot` suffix. Prefer `dependentRef`, `baseRef`, `baseRelationRef`, `scope`, `gammaTime`, and `witnesses`, or the corresponding terms in the selected local declaration. `*Slot` remains reserved for SlotKinds and SlotSpecs (A.6.5).

#### A.6.6:4.4 - BaseRelation declaration

A `baseRelation` token is not “just a label”. For each selected local baseRelation declaration, its definition SHALL include:

* **Relation-end polarity.** Which end is dependent and which end is base (or declare symmetry explicitly).
* **Typing expectations.** Admissible ValueKinds and `refMode` for `DependentSlot` and `BaseSlot`.
* **Token discipline (LEX).** The token SHALL satisfy E.10 token-class morphology for relations/verbs; it SHALL NOT use metaphor heads (`Anchor*`, `Ground*`, `Attach*`) as a meaning-surrogate. If a source phrase must be retained for traceability, record it as source wording through F.18 naming discipline while keeping the relation-specific token specific.
* **Repair path for mismatches.** If an endpoint’s self-kind does not match the expected ValueKind, the allowed repairs are declared (KindBridge, explicit narrowing, or explicit retargeting); “renaming the endpoint” is not a repair.
* **Parameter placement.** Any additional qualifiers required by the relation kind (ranges, metrics, reference planes, policies) SHALL be represented either inside `scope` (preferred) or as explicit additional slots in an extended base-declaration signature; they MUST NOT be smuggled as adjectives on the endpoints.
* **Scope class.** Whether the declaration is claim-scoped (**G**), work-scoped, or publication-scoped.
* **Time discipline.** Whether `Γ_time` is required, optional, or forbidden for this relation kind.
* **Witness discipline.** Whether witnesses are always required versus required only for decision use, and what witness-use relations or pinned witness records are admissible: evidence-use relations, edition pins, calibration certificate pins, proof-bearing publications, or policy pins named by subject patterns.
* **Admissible change classes.** Which base-change operations are permitted (below) and what continuity requirements apply.
* **Cross-local and cross-plane policy.** State whether the relation may connect different exact local kinds, distinct F.17 cells, translated scopes, or ReferencePlanes. When it may, name the applicable C.3.3, F.9, scope, or plane relation, admitted use, and loss or limit; source difference alone is insufficient.

This mirrors A.6.5: a SlotKind without ValueKind/RefMode is underspecified; a baseRelation without its vocabulary entry is equally underspecified.

#### A.6.6:4.4a - Claim-scoped non-kind predicate-base branch

When one identified derivation or criterion-selection claim uses exact claim content as its base, reuse A.6.6's endpoint, scope, time, witness, Bridge/loss, change, and overread discipline without pretending that a base relation kind or SWBD occurrence has been admitted. Identify the exact dependent `U.ClaimGraph`, exact nonempty selected base subgraph by value, the `derive` or `evaluate` mode, exact derivation or evaluation-and-selection claim identity, bounded receiving use, and effective reference scheme. Add an exact A.2.6 ClaimScope, temporal policy/domain, source or witness qualification, or cross-scheme Bridge and loss account only when that independently varying fact changes the assertion.

The assertion is ordinary C.2.1 claim content under `derivedUsingRuleContent` or `evaluatedAgainstRuleContent`. The dependent and base are A.6.0 predicate parameters, not A.6.5 SlotSpecs, participants of a `BaseRelation`, or an intrinsic `rule-bearing` classification. Same-scheme use adds no Bridge. A source edition, designation, acceptance/currentness fact, trace, or witness qualifies the assertion but does not enter semantic-base identity. Equal graphs under the same scheme count as one semantic base with multiple qualifications; a changed graph is another base.

Change only the fact that changed: declare or withdraw a selected base, repoint the dependent, rescope, retime, refresh witnesses, or change the predicate relation. A changed subject, content, mode, bounded use, actual-use claim, scope extension, temporal policy, or interpreted endpoint creates the appropriate successor C.2.1 assertion. Do not infer a new relation kind, occurrence, evidence result, Work, authority, or reliance from that change.

A basis-family analysis is a separate, optional C.2.1 episteme opened only for a named comparison, replay, material-conflict, or reliance receiver. Its candidate universe, evaluations, pairwise compatibility, temporal partition, established family, and disposition neither edit this reusable predicate declaration nor become fields of each actual-use assertion.

#### A.6.6:4.4.1 - Perspective/voice discipline (dependent-view vs base-view)

**Normative rule.** In Tech / normative prose, authors SHALL express a based declaration in one of the following explicit forms:

* `baseRelation(dependent, base)` (functional notation), or
* `dependent --baseRelation--> base` (arrow notation).

Authors SHALL NOT use passive/umbrella voice (“X is anchored/grounded/attached”) as a substitute for an explicit `baseRelation(dependent, base)` form, because it invites direction flips and silent re-typing.

**Base-view is allowed only if the polarity is preserved.** If authors use base-view wording (“B validates X”), they SHALL either (i) keep both endpoints visible using the same polarity-preserving token (e.g., `validatedBy(X,B)`), or (ii) use an explicit inverse token that is declared in the baseRelation declaration. Authors SHALL NOT flip endpoint positions implicitly in prose.

#### A.6.6:4.5 - Lexical discipline

**Normative lexical rule.** In Tech / normative prose and Tech register naming, authors MUST NOT use umbrella metaphors (“anchor/anchoring”, “attach/attachment”, “ground/grounding”) as substitutes for an explicit `baseRelation` token.

**Red-flag rule (`anchor*` as dependence metaphor).**
* In **Tech / normative** prose: authors MUST treat `anchor*` as **prohibited** as a meaning-surrogate for an unnamed dependence kind. Authors SHALL rewrite into explicit `baseRelation(dependent, base)` form (or move to the correct reserved primitive lane).
* In **Plain / source** commentary only: authors MAY quote `anchor*` as a source umbrella only if it is immediately paired with an explicit baseRelation token (e.g., “source ‘anchored’ ⇒ `validatedBy(...)`”) and does not introduce a new relation-specific token.

**Carve-outs (pattern-defined primitives).** This red-flag rule does **not** ban uses where “anchoring” is already a *pattern-defined primitive* elsewhere in the spec, such as E.10 MG-DA token-to-EntityOfConcern anchoring or A.10 evidence anchors. It still acts as a review trigger: confirm you are using the reserved sense, not smuggling a basedness meaning.

**Naming guard for baseRelation tokens.** Do not mint new baseRelation tokens whose head noun is a metaphor (`Anchor*`, `Ground*`, `Attach*`). If you are tempted to do so, you either (i) have not named the relation kind yet, or (ii) are retaining source wording that must be recorded against an existing, more specific relation token through F.18.

Instead:
1) Name the **BaseRelation token** (declared vocabulary element), and
2) Use a **relation-specific verb phrase** that corresponds to that token.

**Lane guard for meaning.** If the intent is “say what this expression means in this source”, do not introduce a baseRelation named `Anchor…` or `Ground…`. Recover the source-local claim under F.0.1; use F.17 only when a durable `SchemeSenseCell` or obtaining `LocalSenseBasisRelation` is actually needed. Semantic meaning assignment is not expressed by SWBD.

**Grounding disambiguation rule.** If the prose says “grounded”, it MUST be rewritten into one of:
* constructive grounding (`tv:groundedBy`, base is a trace),
* situational/empirical grounding (base is a grounding holon or experimental setup),
* source-local meaning lane (exact source, scheme, expression, local claim, and optional F.17 cell or basis relation; not SWBD).

**Bind deconfliction note.** Authors MUST NOT use the verb “bind/binding” as a synonym for declaring/refreshing/changing a base declaration. “bind/binding” is reserved for **name binding** (LEX discipline). For SWBD edits, authors SHALL use the base‑change lexicon (below) instead.

#### A.6.6:4.6 - Base-change operation lexicon

As A.6.5 distinguishes slot operations by whether they change a stored reference, resolve a reference, or replace a value, A.6.6 distinguishes **base declaration changes** by which component changes and what semantics are affected.

Operation classes (conceptual):

These names denote **semantic change classes**. In decision/publication lanes, implementations MUST represent these changes by minting a new SWBD (new id/edition) and linking it to the prior one via explicit continuity/withdrawal (WF‑BD‑5 / CC‑BD‑10), rather than mutating the prior record.

1. **declareBase** — create a new base declaration with explicit `dependent`, `base`, `baseRelation`, `scope`, and, when applicable, `Γ_time`, plus witnesses when decision-relevant.
2. **withdrawBaseDecl** — retire a declaration (or render it inapplicable by scope narrowing or time restriction, depending on baseRelation declaration).
3. **rebase** — change `base` while keeping the same `dependent` and `baseRelation` (legality depends on the baseRelation declaration; often requires witness refresh).
4. **repointDependent** — change `dependent` while keeping the same `base` and `baseRelation`.
5. **rescope** — change `scope` (widen/narrow/translate) under the baseRelation’s scope rule; widening often triggers witness refresh.
6. **retime** — change `Γ_time` selector/policy when time matters; not a substitute for witness-timespan/freshness predicates.
7. **refreshWitnesses** — add/refresh witnesses/pins when decision use continues across time advances, scope widening, or evidence refresh.
8. **changeBaseRelation** — not an edit-in-place. Changing `baseRelation` changes meaning; mint a new declaration and relate them via an explicit continuity relation (F.13 discipline), rather than silently rewriting the kind.

**Relation to A.6.5 slot operations (non-normative mapping).** These are *semantic change classes*; an implementation may realise them using A.6.5 slot operations on the SWBD record fields. Example: a **rebase** may be implemented as a `retarget` of `baseRef` on a *new* SWBD edition. The point of A.6.6 is that “we retargeted a ref” is not the semantic story; “we rebased the declaration” is.

**Relation to E.18 assurance ops (informative).** On `U.Transfer`, the allowed ops—`ConstrainTo`, `CalibrateTo`, `CiteEvidence`, and `AttributeTo`—can be viewed as pattern-defined specialisations of `declareBase`, `rescope`, `rebase`, and `refreshWitnesses` for specific declared `baseRelation` readings, with stricter declared constraints and lintability.

#### A.6.6:4.7 - Disambiguation guide for selecting a baseRelation

When a draft uses an umbrella phrase (“anchored”, “attached”, “grounded”), replace it by selecting a declared `baseRelation` reading:

| Colloquial intent | Declared `baseRelation` reading (illustrative) | Dependent | Base | Typical witnesses |
| --- | --- | --- | --- | --- |
| “This ID refers to that thing” | **Identification / indexing** (`identifies`, `indexedBy`, `registeredIn`) | entity-ref / slot-content | identifier / registry entry | issuance record, registry pin |
| “Make measurements comparable” | **Calibration and datum** (`calibratedTo`, `datumOf`, `normalisedTo`) | instrument, model, or output | standard or datum | calibration work plus certificate pin |
| “This claim is admissible because …” | **Evidence admissibility** (`validatedBy`, `verifiedBy`) | claim | evidence carrier or proof | A.10/G.6 carrier, source-currentness, or provenance records; proof-bearing publications |
| “This edge is grounded in construction” | **Constructive grounding** (`tv:groundedBy`) | WM edge | constructor trace (`Γ_m`) | trace pins, edition pins |
| “This description is about X under a view” | **Viewing / retargeting (specialised)** (`viewedVia`, `retargetedAlong`) | episteme/view | selected EntityOfConcern | view operator pins, Bridge ids (if retargeting) |
| “Allowed only under policy P” | **Constraint / policy** (`constrainedBy`, `permittedUnder`) | work-step / publication item | policy/rule | policy pin, waiver/work ref |
| “Property belongs to object” | **Attribution / aboutness** (`attributedTo`, `aboutEntity`, `characterises`) | property/abstraction | object | observation/derivation witnesses |
| “This expression means … in this source” | **Source-local meaning lane** (F.0.1; F.17 only when a durable address or basis relation is needed) | local expression | local-sense claim | exact source passage and, when current, an obtaining basis relation |

This table is illustrative; the discipline requirement is that the chosen baseRelation be explicit, declared, and relation-specific. The “Meaning lane” row is included only as a **do-not-model-with-SWBD** reminder.

*Note.* The `viewedVia` / `retargetedAlong` operators are defined by the A.6.3/A.6.4 viewing/retargeting patterns; this table only classifies them as “relative-to-base” cases.

#### A.6.6:4.7a - Support wording selection test

When a draft uses `support`, `supported by`, `supporting`, `support basis`, `support relation`, or a support-headed compound, do not first choose a nicer synonym. First decide whether the phrase is a based declaration.

A support phrase is governed by A.6.6 only when all of the following can be stated:

```text
dependent:
base:
baseRelation:
scope:
Γ_time?, if time matters:
witnesses?, if decision/publication/admissibility use is live:
admissibleUse:
nonAdmissibleUse:
```

If these fields can be stated, rewrite the phrase as `baseRelation(dependent, base)` or `dependent --baseRelation--> base` and use an SWBD or a selected local SWBD specialization. Examples include `validatedBy(claim, evidenceCarrier)`, `calibratedTo(measurementOutput, standard)`, `normalisedTo(metric, datum)`, `attributedTo(propertyClaim, selectedEntity)`, `aboutEntity(description, entityOfConcern)`, and `permittedUnder(workStep, policy)`.

If these fields cannot be stated, do not create a `SupportRelation`, `SupportBasis`, `SupportRecord`, or local support-headed type. Classify by reading and apply the matching ontology:

| Support wording means... | Governing ontology to apply |
| --- | --- |
| a source, model, diagram, publication, or view describes, constrains, or exposes something | source-description, specification-use, and publication patterns (`A.7`, `A.6.3`, `A.6.2`, `C.2.3`, `E.17`, local source rules) |
| an observation, test, proof, carrier, or source phrase such as *evidence role* says that an episteme bears on a claim | recover the exact bounded evidence-use, status-use, provenance, or support relation through `A.2.4`, `A.10`, or `G.6`; a separately obtaining system-role classification or assignment may itself be evidence only through another evidence-use fact |
| a claim is acceptable in an assurance or trust calculus | assurance patterns (`B.3`) plus evidence ontology named by value when evidence is live |
| a causal, intervention, counterfactual, off-policy, or simulation-only use is admissible | causal-use pattern (`C.28`) |
| a mathematical lens, mapping, or model makes a use admissible or exposes preserved/lost structure | mathematical-lens patterns (`C.29`, `C.26`, `F.9`) |
| a metric, score, threshold, benchmark, or characteristic warrants a comparison | measurement/characteristic/comparison patterns (`C.16`, `C.25`, `G.9`) |
| one thing helps work, enables an action, supplies a resource, or makes operation easier | work/resource/action patterns (`A.15`, `A.15.4`, `A.6.A`, `C.11`) or ordinary Plain help |
| one file, section, packet, companion, entry cue, or expanded case helps a reader find, inspect, or compare another item | publication, entry, or navigation patterns (`E.17`, `E.11`, `I.2`) or ordinary orientation |

This test prevents support wording from becoming either a source-relation bucket or a basis bucket. A.6.6 governs only the support cases that are genuinely base-relative.

### A.6.6:5 - Archetypal Grounding

#### A.6.6:5.1 - System archetype: calibration to a standard

**Tell.** A lab instrument channel `TC‑17` is described as “anchored to ITS‑90”. Later, the reference standard is swapped, the phrase “still anchored” is kept, and the applicability window silently expands. Downstream work disagrees and nobody can reconstruct what changed.

**Show.** Express it as a base declaration:

```
BD#Calib_TC17_v5 :=
〈 dependent    = ThermocoupleChannelRef(TC-17),
base         = StandardRef(ITS-90 / CalStd-2025-09),
baseRelation = calibratedTo,
scope        = WorkScope{rig=R3, range=[0..200]°C},
Γ_time       = interval[2025-09-01, 2026-03-01],
witnesses    = { WorkRef(CalibrationRun#8841), CertRef(CalCert@edition=5) } 〉
```

**Show.** Disambiguate edits by operation class:

* New standard ⇒ **rebase** + **refreshWitnesses**.
* Wider applicability window ⇒ **retime** and likely **refreshWitnesses**.
* Relation-kind change (“not calibration, just normalisation”) ⇒ **changeBaseRelation** is not an edit; mint a new declaration and relate via continuity.

#### A.6.6:5.2 - Episteme archetype: claim admissibility via evidence relations

**Tell.** A report asserts: “Model M improves accuracy by 4%.” The team says the claim is “anchored in an experiment”, but dataset version, evaluation harness, and time selector are unclear, and no resolvable evidence is linked.

**Show.**

```
BD#AccGainClaim_2025Q4 :=
〈 dependent    = ClaimRef(CG:Claim#acc_gain_4pct),
base         = EvidenceCarrierRef(Work:EvalRun#2025-10-12),
baseRelation = validatedBy,
scope        = ClaimScope{dataset=BenchX@v3, metric=Top1, hardware=A100},
Γ_time       = snapshot(2025-10-12),
witnesses    = { ProvenanceRecordRef(EvalLog@edition=12), ComparatorSetRef@edition=7 } 〉
```

What becomes explicit is not “anchoring”, but:
* the relation kind (`validatedBy`),
* the scope slice,
* the time selector,
* the witness carriers that make the declaration admissible for decision use.

#### A.6.6:5.3 - Structural archetype: constructive grounding of a model edge

**Tell.** A structural edge is published (“A componentOf B”) without a constructor trace. It becomes treated as “obvious”, while the construction chain is not recoverable.

**Show.**

```
BD#EdgeGrounding_ComponentOf_17 :=
〈 dependent    = WMEdgeRef(Edge:componentOf#17),
base         = TraceRef(Γ_m:ComposeCAL#c17),
baseRelation = tv:groundedBy,
scope        = PublicationScope{view=WMCardLite, system=S, line=L3},
Γ_time       = snapshot(2025-11-02),
witnesses    = { WorkRef(AssemblyRun#7712), EditionPin(Γ_m:ComposeCAL@edition=4) } 〉
```

This example shows why “grounding” must be disambiguated: here it is a declared constructive relation with an explicit base (trace), not a vague claim of “stability”.

### A.6.6:6 - Bias-Annotation

| Lens | Bias introduced by this pattern |
| --- | --- |
| **Governance / assurance** | Prefers explicit witnesses and explicit time selectors for decision-relevant declarations; increases auditability but adds authoring overhead. |
| **Architecture** | Encourages reifying “relative-to” facts as first-class records rather than implicit prose. |
| **Onto-epistemic** | Treats “kind of base relation” as first-order; pushes authors to mint explicit baseRelation tokens instead of hiding semantics in adjectives. |
| **Didactic** | Introduces a new stable vocabulary (“dependent/base/baseRelation”) and requires authors to maintain it consistently across views. |

### A.6.6:7 - Conformance Checklist

A carrier (pattern, spec, schema, code carrier, or publication) conforms to A.6.6 iff:

1. **CC‑BD‑1 — Base relation kind is explicit.**
   Every base-declaration-like statement SHALL name an explicit `baseRelation` token (a declared vocabulary element). No umbrella metaphor SHALL substitute for a relation kind.

2. **CC‑BD‑2 — Dependent and base are explicit and typed.**
   Every based declaration SHALL make both `dependent` and `base` explicit, and SHALL be SlotKind/ValueKind/RefMode disciplined per A.6.5.

3. **CC‑BD‑3 — Scope is explicit.**
   Every based declaration SHALL include an explicit `scope` (Claim scope (**G**) / Work scope / Publication scope).

4. **CC‑BD‑4 — `Γ_time` is explicit when time matters.**
   If any time-dependent assumption exists, the based declaration SHALL include an explicit `Γ_time`; implicit “latest/current” SHALL NOT be used as a substitute.

5. **CC‑BD‑5 — Decision use is witnessed.**
   If a base declaration participates in assurance, gating, or admissibility decisions, it SHALL include a non-empty, resolvable `witnesses` set (pins).

6. **CC‑BD‑6 — No silent kind edits.**
   Changing `baseRelation` SHALL be treated as a semantic change: it SHALL be represented as a new declaration plus explicit continuity, not as an edit-in-place.

7. **CC‑BD‑7 — Grounding is disambiguated.**
   Any use of “grounding/grounded” SHALL be disambiguated to a specific declared relation kind or moved to source-local meaning recovery under F.0.1 and, when needed, F.17.

8. **CC‑BD‑8 — Actual cross-local use is explicit.**
   If the declaration consumes a relation between different exact local kinds, distinct F.17 cells, translated scopes, or ReferencePlanes, it SHALL cite the applicable C.3.3, F.9, scope, or plane relation and its admitted-use limits. Different sources alone do not require or establish a Bridge.

9. **CC‑BD‑9 — `Γ_time` is not treated as freshness.**
   When witness freshness/decay matters, it SHALL be expressed explicitly through evidence-use timespans, witness qualification windows, or explicit freshness predicates, not by treating `Γ_time` as a proxy.

10. **CC‑BD‑10 — Edition fence for decision/publication.**
   If a base declaration is used for decision or cited in PublicationScope, it SHALL be immutable per edition: updates SHALL mint a new declaration and connect it via explicit continuity/withdrawal.

11. **CC‑BD‑11 — Slot suffix discipline is respected.**
   The `*Slot` suffix SHALL be used only for SlotKinds/positions, never for endpoint values or references.

12. **CC‑BD‑12 — No “anchor” relapse.**
   `anchor*` / `ground*` / `attach*` SHALL NOT be used as surrogates for a source, local meaning, F.17 cell, local-sense basis relation, or unnamed dependence kind. Authors SHALL either use the reserved primitive sense (where explicitly defined elsewhere) or rewrite into explicit `baseRelation(dependent, base)` form. Metaphor-head tokens SHALL NOT be minted as new relation-specific `baseRelation` vocabulary entries; if quoted source wording must be retained, record it as source wording against the specific non-metaphor token.

13. **CC‑BD‑13 — BaseRelation declarations are explicit.**
    Every `baseRelation` token used in an SWBD SHALL resolve to a vocabulary entry that declares at least polarity; typing expectations (ValueKind + `refMode`) for `DependentSlot` and `BaseSlot`; admissible repair options (KindBridge, narrowing, or explicit retargeting); scope class; time discipline (`Γ_time` required, optional, or forbidden); witness discipline; admissible change classes; and any cross-local or cross-plane policy with the exact applicable relation, admitted use, and loss or limit.

14. **CC‑BD‑14 — Authoring voice is explicit.**
    In Tech / normative prose, based declarations SHALL be written as `baseRelation(dependent, base)` or `dependent --baseRelation--> base`. Base-view prose SHALL be used only if polarity is preserved via explicit inverse-token use; implicit polarity flips SHALL NOT be used.

15. **CC‑BD‑15 — Meaning lane separation.**
    Semantic meaning assignment SHALL begin with the exact source, edition, effective ReferenceScheme, local expression, and local-sense claim under F.0.1; an F.17 cell or basis relation is added only when that stronger use is current. It SHALL NOT be modeled as SWBD. SWBD SHALL be used only for non-semantic base-dependence (admissibility, calibration, attribution, policy gating, constructive grounding, and viewing and retargeting specialisations).

16. **CC‑BD‑16 — Reserved “bind” discipline.**
    `bind/binding` SHALL be reserved for **name binding** (LEX discipline) and SHALL NOT be used as a synonym for declaring/refreshing/changing a base declaration. Authors SHALL use the base‑change lexicon (`declareBase`, `rebase`, `rescope`, `retime`, `refreshWitnesses`, …) and explicit continuity/withdrawal relations instead.

17. **CC‑BD‑17 — Support wording is classified before base declaration.**
    A support-looking statement SHALL pass the support wording selection test before it is modeled as SWBD. If the reading is not base-dependence, the text SHALL name the ontology of the subject pattern for that claim or keep the phrase as ordinary help/orientation; it SHALL NOT mint a support-headed baseRelation or record as a generic container.

### A.6.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| **Generic support bucket** | Hides whether support means base-dependence, evidence polarity, assurance input, causal-use basis, mathematical-lens use, work enablement, source-description, publication companion, or ordinary help | Apply the support wording selection test; use SWBD only for genuine basedness and apply every other reading's ontology of the subject pattern for that claim |
| **Umbrella “anchored/attached/grounded” with no baseRelation** | Hides relation kind; cannot state invariants | Introduce a declared baseRelation token and rewrite prose to use it |
| **Perspective flip without endpoint-position names** | Directionality and typing become ambiguous | Use `dependent`/`base` endpoint positions consistently; declare polarity in baseRelation declaration |
| **Treating evidence as “the base”** | Confuses base with witnesses | Make evidence/pins witnesses unless the relation kind’s base is explicitly an evidence carrier |
| **Implicit “current/latest”** | Violates explicit time discipline | Declare `Γ_time` explicitly and use witness timespans for freshness where needed |
| **Decision gating without witnesses** | Becomes folklore; not reviewable | Add resolvable witnesses through evidence-use relations, A.10/G.6 carrier, source-currentness, or provenance records, certificate pins, or proof-bearing publications named by the subject pattern |
| **Semantic meaning expressed as a base declaration** | Confuses source-local meaning with admissibility | Recover the exact source-local claim under F.0.1 and add an F.17 cell or basis relation only when needed; keep SWBD for non-semantic basedness |
| **Change baseRelation in place** | Semantic shift masquerades as update | Mint a new declaration and connect via continuity |
| **Using `*Slot` to name an endpoint/value** | Confuses SlotKind with ValueKind/RefKind; breaks substitution and tooling | Keep `*Slot` for positions; use `base`/`dependent` for values and `*Ref` for stored references |
| **Typing `baseRelation` as a `publication-side object*` carrier** | Confuses a relation-specific relation token with a publication-lane object; invites “free text as relation kind” | Store `baseRelation` as a declared `NameToken` that resolves to a vocabulary entry with an explicit signature and relation-specific constraints |

### A.6.6:9 - Consequences

**Benefits**
* Disambiguation by construction: base-dependence becomes explicit via `baseRelation`.
* Cross-domain reuse: one stable record shape works for calibration, evidence admissibility, attribution, policy gating, and constructive grounding.
* Determinism where required: explicit scope and `Γ_time` prevent silent “latest/current” assumptions.
* Reduced “grounding” confusion: multiple grounding senses become distinguishable relation kinds.

**Trade-offs / mitigations**
* More explicit metadata and vocabulary: mitigated by defining each selected local `baseRelation` vocabulary entry once and reusing it.
* Authoring overhead for witnesses in decision contexts: mitigated by pointing to already-existing `U.Work` refs and witness pins instead of creating new documents.

**Adoption test (informative).**
A team has adopted A.6.6 if, for any decision-relevant “relative-to” statement, it can produce a resolvable tuple
`〈dependent, base, baseRelation, scope, Γ_time?, witnesses?〉`
and can classify any update as one of:
`declareBase`, `withdrawBaseDecl`, `rebase`, `repointDependent`, `rescope`, `retime`, `refreshWitnesses`, and `changeBaseRelation`.

### A.6.6:10 - Rationale

**Why focus on base declaration rather than a metaphor.**
The recurring ambiguity is not “how to attach”, but “what is the declared base, and what kind of dependence is being asserted”. Naming the baseRelation token makes the dependence explicit and reviewable.

**Why separate base from witnesses.**
Bases are semantic reference frames; witnesses are justifiers/enforcers for decision use. Conflating them makes both reasoning and audit impossible.

**Why include scope and `Γ_time`.**
A declaration is never “everywhere forever” by default in FPF. Scope makes applicability explicit; `Γ_time` prevents hidden time dependence (“recent”, “current”, “latest”).

**Why prohibit kind edits.**
Changing the relation kind changes meaning; treating it as an update erases history and breaks continuity discipline.

**Why the base-change lexicon.**
Without explicit change classes, prose collapses distinct edits (rebase vs retime vs rescope vs witness refresh) and recreates the same ambiguity A.6.5 removed at the slot layer.

### A.6.6:11 - SoTA-Echoing

1. **RDF-star and statement qualification.**
   **Adopt/Adapt.** RDF-star/SPARQL-star continues the semantic-web tradition of attaching qualifiers/provenance to statements and edges. We adopt the “qualified statement” intuition, but adapt it by requiring an explicit relation kind token and by tying time and scope discipline to FPF’s explicit `Γ_time` and USM scopes rather than leaving them implicit or purely notational.
   *Primary source:* Hartig et al., “Foundations of RDF* and SPARQL*” (2017+).

2. **Wikidata-style statements with qualifiers and references.**
   **Adopt/Adapt.** The Wikidata model popularised practical “statement + qualifiers + references” structures at scale. We adopt the separation of the core statement from its qualifiers/references, and adapt it by making decision-relevant witness requirements explicit through evidence-use relation slots and by requiring explicit scope/time where time-dependent assumptions exist.
   *Primary sources:* Wikidata statement model documentation and design lineage (post‑2015 practice).

3. **Metrology traceability and calibration competence.**
   **Adopt/Adapt.** Laboratory competence standards treat calibration as traceability to standards with documented evidence and bounded validity. We adopt the expectation that calibration-to-standard is not timeless, and adapt it by representing the validity window via explicit `Γ_time` plus witnesses as pinned calibration records.
   *Primary source:* ISO/IEC 17025:2017.

4. **Assurance case metamodels for claim–evidence structure.**
   **Adopt/Adapt.** SACM formalises claim/evidence structures and emphasises structured support relations. We adopt the idea that decision-relevant admissibility links should be explicit, and adapt it by using FPF’s scope/time discipline and by treating relation-kind elision as a first-order defect.
   *Primary sources:* OMG Structured Assurance Case Metamodel (SACM), 2018+.

5. **Objects over a base as a stable mathematical lens.**
   **Adopt/Adapt.** Modern category-theory texts make “objects over a base” (slice categories) a reusable pattern for “X relative to B”. We adopt that lens as the stable abstraction behind base declarations, and adapt it with explicit scope/time and witness semantics needed for engineering governance.
   *Primary source:* Riehl, *Category Theory in Context* (2016).

**SoTA binding note (informative).** This pattern’s “qualified statement + explicit relation kind + references” move aligns with RDF*/Wikidata practice (items 1–2); the explicit time-window + witness semantics in decision use align with metrology traceability and assurance-case structures (items 3–4); the “object over a base” lens is the abstraction used to keep the pattern stable across domains (item 5).

### A.6.6:12 - Relations

**Specialises A.6.P Relational Precision Restoration (RPR).**
A.6.6 is the RPR specialisation for “basedness / relative‑to” claims: it makes the relation kind explicit via `baseRelation`, qualifies it with scope/`Γ_time`/witnesses, and standardises evolution via a base‑change lexicon plus lexical red‑flags (`anchor*`).

**Builds on A.6.5 relation-declaration slot discipline.**
SWBD introduces a structured record with slots; those slots must be SlotKind/ValueKind/RefKind disciplined, and its change classes must not be confused with slot-edit operations (A.6.5) or name-binding terminology (E.10 / L‑BIND).

**Constrains A.10 evidence admissibility links.**
`verifiedBy` and `validatedBy` are treated as baseRelation tokens; their scope/time and witnesses become explicit when used for decisions.

**Aligns with A.2.4 evidence-use relation discipline.**
Decision-relevant witness sets should be represented through evidence-use relations or pinned witness records with explicit timespans and provenance discipline, not as ad-hoc prose references and not as system-role kinds or assignments attributed to epistemes.

**Aligns with A.14 constructive grounding (`tv:groundedBy`).**
Constructive grounding is one specific declared `baseRelation` reading: dependent is a model edge, base is a constructor trace; witnesses pin the trace and `U.Work` records.

**Coordinates with C.2.1 grounding holons.**
When a base declaration depends on situational or empirical grounding, name the exact episteme, covered claims, grounding holon, and obtaining C.2.1 `EpistemeEmpiricalGroundingRelation`. Treat that relation as a distinct `baseRelation` reading; do not substitute its declaration-local `GroundingHolonSlot`, collapse it with `tv:groundedBy`, or use it as semantic meaning assignment.

**Coordinates with A.6.3–A.6.4 viewing/retargeting.**
Viewing and retargeting are specialised “relative-to-base” moves (preserve `EntityOfConcernRef` vs retarget it along a declared bridge). They should reuse SWBD vocabulary where an explicit base declaration is required (scope/time/witness), without collapsing into generic “anchoring” prose.

**Coordinates with A.2.6 and `Γ_time`.**
Base declarations inherit the rule that time-dependent assumptions require explicit `Γ_time`; “current/latest” is not admissible.

**Feeds E.10 / F.18 lexical governance.**
Umbrella metaphors are disallowed as substitutes for baseRelation tokens; prose must name explicit relation kinds and keep source-local meaning, its optional F.17 cell, and any obtaining basis relation separate.

**Constrains support wording in A.6.P/E.10.**
Support-looking phrases that mean base-dependence are governed here: select a declared `baseRelation`, name `dependent` and `base`, add scope/time/witnesses as live, and preserve polarity. Support-looking phrases that do not mean base-dependence use the ontology of the subject pattern for that claim rather than becoming `SupportRelation`, `SupportBasis`, or `SupportRecord` buckets.

### A.6.6:End

