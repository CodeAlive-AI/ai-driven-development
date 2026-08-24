## A.6.6 - Base Declaration Discipline - Direct relation first; reusable declaration only when needed
> **Status:** Stable
> **Type:** Definitional relation-discipline pattern

**Plain-name.** Saying exactly what something depends on.

**Use this pattern when** a sentence says that one thing is calibrated to, based on, attributable to, constrained by, or otherwise usable relative to another, and the actual relation is still hidden by words such as *anchor*, *support*, *ground*, or *based on*.

**First useful move.** Name the actual dependent and base, state the direct relation in an ordinary sentence, and apply that relation's own predicate to the current facts. Stop when this readable assertion answers the receiving question.

**What goes wrong if missed.** An umbrella word hides the relation kind or reverses its participants. At the opposite extreme, a simple assertion is expanded into slots, witnesses, editions, and a new record even though no later use needs them.

**What this buys.** A direct, testable assertion first. Scope, time, evidence, a reusable `RelationSignature`, or a reviewable record is added only when the direct predicate or one named receiving use needs that distinction.

**Not this pattern when.** If the direct relation and its participants are already clear, use its direct pattern. If *support* means evidence use, assurance, ordinary help, work enablement, navigation, source description, or another non-basedness reading, use that reading's direct pattern instead.

**E.24.UK settlement.** A.6.6 admits neither `U.BaseDeclarationDiscipline` nor `U.ScopedWitnessedBaseDeclaration`. The retired `U.ScopedWitnessedBaseDeclaration` spelling must not be used as a kind or as a world-side relation occurrence. When a named receiver needs a reviewable scoped assertion, the phrase *scoped witnessed base declaration* denotes an optional representation of one C.2.1 assertion or description episteme. Its ClaimGraph states a separately governed direct relation and any current qualifiers; the record makes none of those facts obtain. An already admitted relation kind may separately have a reusable `RelationSignature` under A.6.0.
**Status.** Normative (Core).

**Placement.** Part A, cluster A.IV “Signature Stack & Boundary Discipline”; adjacent to A.6.5 relation-declaration slot discipline.

**Depends on.**
- A.6.0 `U.Signature` (universal signature carrier).
- A.6.5 relation-declaration slot discipline (SlotKind, ValueKind, and RefKind stratification plus the slot-operation lexicon).
- A.2.6 (Scope discipline; explicit `Γ_time`; implicit “latest/current” is forbidden).
- A.2.4 evidence-use and status-use relation discipline for decision-relevant witness sets, including timespan, provenance, scope, polarity, and freshness constraints.
- A.7 (Strict Distinction; EntityOfConcern vs Description-episteme and specification-use cases vs publication face, form, unit, carrier, and rendering lanes).
- E.8 (pattern authoring order & SoTA discipline).
- E.10 and E.10.D1 for wording-use recovery, with F.0.1 and F.17 for source-local meaning and its optional durable address.

**Coordinates with.**
- A.10 evidence-provenance and bounded-reliance discipline; its graph cites independently obtaining direct relations and admits no generic `verifiedBy` or `validatedBy` fallback edge.
- A.14 per-edge constructive grounding (`tv:groundedBy`) and `validationMode` discipline.
- C.2.1 episteme constitution through exact claim content, EntityOfConcern, and effective ReferenceScheme, plus the separately obtaining `EpistemeEmpiricalGroundingRelation` between an exact episteme and grounding holon.
- A.6.3 `U.EpistemicViewing` (`EntityOfConcernRef`-preserving view operators; base-relative “how” without retargeting).
- A.6.4 EntityOfConcern retargeting: one local arrow between exact epistemes with different EntitiesOfConcern, plus a separate use assertion for invariant, visible loss, bounded use, conditions, support, and polarity.
- C.3.3 `U.KindBridge`, including the `CL^k` value declared for that bridge (explicit repair or translation when exact endpoint kinds differ; no silent re-typing).
- E.18 assurance-operations on `U.Transfer` (`CalibrateTo`, `CiteEvidence`, `AttributeTo`, `ConstrainTo`, …).
- F.9 only when the declaration consumes an obtaining Bridge between two exact F.17 local senses. Cite the Bridge and its separate bounded-use claim; `CL` is optional evidence shorthand. A ReferencePlane difference uses its applicable plane relation and does not create an F.9 Bridge.
- F.15 F-Suite validation harness (carrier/source-currentness, provenance, and refresh governance).
- F.18 naming governance (Tech/Plain twins and publication-lane naming boundaries).

**Source phrases and red-flag cues (informative; not normative vocabulary).**
- “anchoring / anchor” (source umbrella colloquial; a red-flag cue for *under-described dependence*). In Tech register, replace it with the ordinary sentence and relation-specific verb that name the actual participants and direct relation. Keep it only for an already reserved primitive (for example, E.10 MG-DA *Domain Anchoring*), or in quoted source text followed immediately by the direct rewrite.
- “Qualified statement / attributed edge” (knowledge-graph colloquial).
- “support / supported by / support basis / support relation” (ordinary umbrella support wording). Diagnostic for possible basedness only when the phrase asserts that a dependent content is admissible, usable, interpretable, comparable, publishable, or actionable relative to an explicit base. Otherwise classify the live reading and apply the governing ontology named by value: source-description, evidence, assurance, causal-use, mathematical-lens, work/resource, publication/navigation, or ordinary help.
- “Pinning” (when witnesses are edition pins).

**Mint-or-reuse note (informative).**
A.6.6 mints no public kind. It reuses the direct relation kind and predicate selected for the claim. A reusable definition uses that relation kind's existing or newly justified A.6.0 `RelationSignature`; one scoped assertion remains a C.2.1 episteme. The local labels `declareBase`, `rebase`, `retime`, and related terms may classify edits to such an assertion or declaration when a named receiver needs that history. They neither make the world-side relation obtain nor require a record for an ordinary sentence.

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

> **Deconfliction note (lexical).** This pattern is about *base-dependence in content* (“X is usable relative to B”). It is not about E.10’s **Domain Anchoring** (MG-DA), where “anchoring” is a lexical primitive. In a basedness sentence, `anchor*` is a defect until the actual participants, relation-specific verb, and direct predicate are recoverable.
>
> **Deconfliction note (source-local meaning).** This pattern is not a license to use “anchor” for a source, meaning, or the thing that supposedly makes a word mean something. Recover the exact source and edition, effective `ReferenceScheme`, local expression, local-sense claim, and exact supporting passage under F.0.1. Create an F.17 `SchemeSenseCell` or obtaining `LocalSenseBasisRelation` only when a later use needs that durable address or support claim. A small source note or Card may represent an already constituted episteme; its form supplies no meaning and is not a special base-declaration object.
>
> **Deconfliction note (support wording).** This pattern constrains *support* only when the claim is base-dependence: one identified dependent is usable, admissible, interpretable, comparable, publishable, or actionable relative to one identified base through a named direct relation. Ordinary help, source discovery, reader navigation, work enablement, evidence use, assurance, causal use, mathematical-lens use, and publication companionship keep their own direct accounts. A support phrase that cannot select one reading remains a cue, not a declaration.

Like A.6.5, this family can expose **typing conflicts across viewpoints**: an endpoint may be named by its self-kind while the selected direct relation expects another participant kind or reference mode. Make that mismatch explicit only when it is current; do not hide it by renaming ends or flipping direction. Use SlotSpecs only when a reusable relation declaration actually needs them.

The structural problem is smaller than the old record shape suggested. Every ordinary basedness assertion first needs only:

1. the actual **dependent**;
2. the actual **base**; and
3. the direct relation and its obtaining test.

Scope, time, evidence, continuity, or a reusable declaration is added only when the direct predicate or one named receiving use depends on it. Until the direct relation is named, umbrella words such as *anchor*, *ground*, *attach*, *support*, or *based on* usually mean only:

> “There is an under-described relation here.”

The repair is therefore progressive: recover and test the direct relation, stop if the assertion is enough, and materialize declaration or assertion machinery only for a concrete later use.

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
   A.6.5 distinguishes relation positions, their fillers, and stored references. Umbrella basing language can hide the direct relation at the next layer, while record-edit language can be mistaken for change in the relation itself.

9. **Anchor relapse (source or meaning surrogate).**
   “Anchor/anchoring” is used to mean “the source”, “the meaning”, “the global reference”, or “the thing that makes this true”. This hides the exact source, scheme, expression, local claim, and any obtaining basis relation behind a metaphor and makes review impossible.

10. **Support bucket relapse.**
    “Support”, “support basis”, “support relation”, or “support record” is used as a generic container for unlike relations. Some cases are direct base-dependence; others are evidence use, assurance input, causal-use support basis, mathematical-lens use, work enablement, source description, publication companionship, or ordinary help. Treating them as one support relation recreates the under-described dependence that A.6.6 is meant to repair.

### A.6.6:3 - Forces

| Force | Tension |
| --- | --- |
| **Universality vs precision** | One discipline must cover calibration, evidence linking, reference selection, attribution, gating, etc., without collapsing them into one pseudo-relation. |
| **Minimal kernel vs decision auditability** | Few primitives are preferred, but decision-relevant declarations must carry witnesses/pins and explicit time selectors where needed. |
| **Two perspectives, one reality** | Dependent-view and base-view must both be expressible without renaming relation-end meanings or flipping meaning. |
| **Compatibility with A.6.5** | Base declarations introduce slots and edits; they must remain SlotKind/ValueKind/RefKind disciplined and must not collapse slot edits with semantic re-declarations. |
| **Lexical guardrails** | Without strict wording rules, umbrella metaphors will return and erase the structure. |
| **Cross-local integrity** | When a declaration actually depends on a relation between different local kinds, local senses, scopes, or planes, that exact relation must remain explicit and reviewable; different sources alone do not create a Bridge. |

### A.6.6:4 - Solution - State the direct relation, then add only what the receiving use needs

#### A.6.6:4.0 - Ordinary direct path

Start with a readable sentence:

> `Thermocouple channel TC-17 is calibrated to standard ITS-90 for rig R3.`

Identify `TC-17` and `ITS-90`, then apply the direct `calibratedTo` predicate and its applicability rule to the current facts. If the task only asks whether that calibration relation obtains for this rig, the sentence and predicate result are complete. Do not create a declaration record, witness set, edition, or assurance package merely because those fields could be written down.

Add a qualifier only when it changes the direct assertion or a named receiving use:

- name scope when the relation is limited to a range, population, rig, publication, or other exact extent;
- name time when the predicate or the use is time-dependent;
- cite an evidence-use or provenance relation when a claim about the relation is relied on;
- open occurrence identity only when another claim must refer to the same occurrence, compare it, qualify it, or record its history; and
- open a reusable declaration only when at least two named consumers need the same participant meanings, predicate, laws, and applicability.

The assertion episteme, reusable declaration, world-side relation occurrence, evidence, and any Work remain different objects.

#### A.6.6:4.1 - Optional scoped assertion record

When replay, comparison, publication, or repeated review needs a stable representation, a project may show one C.2.1 assertion episteme in this local form:

```text
scoped witnessed base declaration :=
  < dependent,
    base,
    directRelationKind,
    assertionPolarity,
    scope?,
    gammaTime?,
    evidenceUseRefs? >
```

This is a representation of claim content, not a public kind, `RelationSignature`, or world-side occurrence. `directRelationKind` resolves to an already governed relation kind; the assertion is true only when that relation's predicate is satisfied for the actual participants. `scope` and `gammaTime` are present only when the direct relation or named use needs them. `evidenceUseRefs`, when present, resolve to exact A.2.4 evidence-use relations for this assertion. The evidence epistemes, producing Work, operation result, carrier, provenance, currentness, and later reliance remain separately identified under A.2.4 and A.10.

The record's C.2.1 identity follows its complete ClaimGraph, exact EntityOfConcern, and effective ReferenceScheme. Revising the record changes an episteme. It does not by itself begin, end, or alter the world-side relation it describes.

#### A.6.6:4.2 - Direct relation and optional assertion are different objects

The useful stable picture is a direct arrow in ordinary reading:

> dependent **stands in the named direct relation to** base.

The arrow is not a generic mathematical constructor. Its participant meanings, predicate, applicability, and occurrence identity come from the selected direct relation pattern. A scoped assertion episteme may state that this predicate holds, and evidence may support reliance on that assertion. Neither the assertion nor its evidence makes the relation obtain.

Calibration, attribution, policy dependence, constructive grounding, and other cases therefore remain different relation kinds. A.6.6 supplies a recovery discipline, not one universal `BaseRelation` kind.

#### A.6.6:4.3 - Reusable declaration only for a named reuse

Use the direct relation's A.6.0 `RelationSignature` only after the relation kind is already admitted and at least two named consumers need the same reusable declaration content. That signature states the participant meanings, predicate, applicability, and occurrence-identity rule. A.6.5 SlotSpecs belong inside that reusable declaration; they are not required in an ordinary one-case assertion.

If no direct pattern supplies the relation kind, participants, or predicate, keep the exact local claim or return the A.6.RCD `missing-governor` result. Do not repair the gap by minting a generic `BaseRelation` kind or token, SlotSpecs, or a scoped-record type.

#### A.6.6:4.4 - What a reusable direct-relation declaration must say

For a named receiving use that genuinely needs a `RelationSignature`, the direct relation definition states:

- the dependent and base participant meanings and direction or symmetry;
- the obtaining predicate and applicability;
- the occurrence-identity rule when occurrence identity is used;
- admissible participant kinds and reference modes;
- any scope, time, evidence, or cross-local condition that changes this predicate or the named reuse; and
- the direct continuity or change rules, when that history is current.

Different exact local kinds, F.17 senses, scopes, or ReferencePlanes are handled by their applicable direct relations. Source difference alone creates no Bridge. A RelationSignature declares reusable content; it neither asserts a current case nor creates an occurrence.

#### A.6.6:4.4a - Claim-scoped non-kind predicate-base branch

When one identified derivation or criterion-selection claim uses exact claim content as its base, reuse A.6.6's endpoint, scope, time, witness, Bridge/loss, change, and overread discipline without pretending that a new relation kind or special base-declaration occurrence has been admitted. Identify the exact dependent `U.ClaimGraph`, exact nonempty selected base subgraph by value, the `derive` or `evaluate` mode, exact derivation or evaluation-and-selection claim identity, bounded receiving use, and effective reference scheme. Add an exact A.2.6 ClaimScope, temporal policy/domain, source or witness qualification, or cross-scheme Bridge and loss account only when that independently varying fact changes the assertion.

The assertion is ordinary C.2.1 claim content under `derivedUsingRuleContent` or `evaluatedAgainstRuleContent`. The dependent and base are predicate parameters, not automatically A.6.5 SlotSpecs, participants of a reusable relation occurrence, or an intrinsic `rule-bearing` classification. Same-scheme use adds no Bridge. A source edition, designation, acceptance/currentness fact, trace, or witness qualifies the assertion but does not enter semantic-base identity. Equal graphs under the same scheme count as one semantic base with multiple qualifications; a changed graph is another base.

Change only the fact that changed: declare or withdraw a selected base, repoint the dependent, rescope, retime, refresh witnesses, or change the predicate relation. A changed subject, content, mode, bounded use, actual-use claim, scope extension, temporal policy, or interpreted endpoint creates the appropriate successor C.2.1 assertion. Do not infer a new relation kind, occurrence, evidence result, Work, authority, or reliance from that change.

A basis-family analysis is a separate, optional C.2.1 episteme opened only for a named comparison, replay, material-conflict, or reliance receiver. Its candidate universe, evaluations, pairwise compatibility, temporal partition, established family, and disposition neither edit this reusable predicate declaration nor become fields of each actual-use assertion.

#### A.6.6:4.4.1 - Perspective and voice

State the relation in the shortest ordinary sentence that keeps both participants and direction recoverable: `TC-17 is calibrated to ITS-90` is valid. Functional or arrow notation may be added when it helps a formal receiver; it is not the default. Base-view wording is also valid when it preserves the same relation and direction. Do not turn `B validates X` into an inverse relation unless that inverse is independently defined.

#### A.6.6:4.5 - Lexical discipline

**Normative lexical rule.** In Tech or normative prose, do not use umbrella metaphors (`anchor`, `attach`, `ground`, or `support`) in place of the actual relation. Prefer an ordinary relation-specific sentence; add functional or arrow notation only when a named receiver benefits from it.

**Red-flag rule (`anchor*` as dependence metaphor).**
* In **Tech or normative** prose, rewrite `anchor*` as an ordinary relation-specific sentence, or move to the already reserved primitive that actually governs the claim.
* In **Plain or source** commentary, quoted umbrella wording may remain for traceability when the repaired sentence immediately names the actual relation. It must not be converted into a generic `validatedBy`, `verifiedBy`, `SupportRelation`, or metaphor-headed token.

**Carve-outs (pattern-defined primitives).** This red-flag rule does **not** ban uses where “anchoring” is already a *pattern-defined primitive* elsewhere in the spec, such as E.10 MG-DA token-to-EntityOfConcern anchoring or A.10 evidence anchors. It still acts as a review trigger: confirm you are using the reserved sense, not smuggling a basedness meaning.

**Naming guard for relation vocabulary.** Do not mint a new direct relation whose name merely preserves a metaphor such as `Anchor*`, `Ground*`, or `Attach*`. Name the actual relation kind and use the corresponding ordinary verb phrase. In an optional assertion record, the local `directRelationKind` field identifies that already admitted relation kind; the field is not another relation kind.
**Lane guard for meaning.** If the intent is “say what this expression means in this source”, do not introduce an `Anchor…` or `Ground…` relation. Recover the source-local claim under F.0.1; use F.17 only when a durable `SchemeSenseCell` or obtaining `LocalSenseBasisRelation` is actually needed. Semantic meaning assignment is not a base-declaration record.

**Grounding disambiguation rule.** If the prose says “grounded”, it MUST be rewritten into one of:
* constructive grounding (`tv:groundedBy`, base is a trace),
* situational/empirical grounding (base is a grounding holon or experimental setup),
* source-local meaning lane (exact source, scheme, expression, local claim, and optional F.17 cell or basis relation; no special base-declaration object).

**Bind deconfliction note.** Do not use “bind/binding” as a synonym for declaring, refreshing, or changing an assertion or reusable relation declaration. “Bind/binding” remains reserved for name binding. Use the local declaration-change label only when a named receiver needs that history.

#### A.6.6:4.6 - Base-change operation lexicon

The following local labels classify changes to an optional assertion episteme or reusable declaration when a named receiver needs that history. They do not describe the beginning, ending, or change of the world-side relation itself, and an ordinary direct assertion needs none of them. In decision or publication use, editing the assertion or declaration creates a successor episteme under its own identity and continuity rules rather than silently mutating the prior edition.

Operation classes (conceptual):
1. **declareBase** - create a new optional assertion with explicit `dependent`, `base`, `directRelationKind`, and `assertionPolarity`, or a new reusable declaration for that same already governed direct relation kind; add only the scope, time, evidence-use, or other qualifications that its direct predicate or named receiver needs.
2. **withdrawBaseDecl** — retire an assertion or declaration (or render it inapplicable by scope narrowing or time restriction, depending on the direct relation's declaration).
3. **rebase** — change `base` while keeping the same `dependent` and `directRelationKind` (legality depends on the direct relation's declaration; often requires witness refresh).
4. **repointDependent** — change `dependent` while keeping the same `base` and `directRelationKind`.
5. **rescope** — change `scope` (widen/narrow/translate) under the direct relation's scope rule; widening often triggers witness refresh.
6. **retime** — change `Γ_time` selector/policy when time matters; not a substitute for witness-timespan/freshness predicates.
7. **refreshWitnesses** — add/refresh witnesses/pins when decision use continues across time advances, scope widening, or evidence refresh.
8. **changeDirectRelationKind** — not an edit-in-place. Changing `directRelationKind` changes claim meaning; mint a new assertion or declaration and relate it to the prior one through an explicit continuity relation (F.13 discipline), rather than silently rewriting the kind.

**Relation to A.6.5 slot operations (non-normative mapping).** A project may realize an edit to an optional assertion or declaration through A.6.5 slot operations. The semantic account must still say which episteme field changed. A separately claimed change to the actual relation uses the direct relation's change rule and any current Work; it is never inferred from the record edit.

**Relation to E.18 assurance ops (informative).** On `U.Transfer`, `ConstrainTo`, `CalibrateTo`, `CiteEvidence`, and `AttributeTo` have their own declared meanings and constraints. A project may use the local declaration-change labels to describe changes in a represented assertion, but those labels neither subsume the E.18 operations nor create their relations.

#### A.6.6:4.7 - Disambiguation guide for selecting the direct relation

When a draft uses an umbrella phrase (“anchored”, “attached”, “grounded”), replace it with the direct relation that actually fits the claim:

| Colloquial intent | Direct relation (illustrative) | Dependent | Base | Typical supporting material, when needed |
| --- | --- | --- | --- | --- |
| “This ID refers to that thing” | **Identification / indexing** (`identifies`, `indexedBy`, `registeredIn`) | entity-ref / slot-content | identifier / registry entry | issuance record, registry pin |
| “Make measurements comparable” | **Calibration and datum** (`calibratedTo`, `datumOf`, `normalisedTo`) | instrument, model, or output | standard or datum | calibration work plus certificate pin |
| “This result bears on that claim” | **Evidence use** under A.2.4, with A.10 only when replayable provenance or reliance is needed | result or other evidence episteme | target claim | exact evidence-use relation; producing Work, result binding, carrier, provenance, currentness, and reliance remain separate |
| “This edge is grounded in construction” | **Constructive grounding** (`tv:groundedBy`) | WM edge | constructor trace (`Γ_m`) | trace pins, edition pins |
| “This description is about X under a view” | **Viewing / retargeting (specialised)** (`viewedVia`, `retargetedAlong`) | episteme/view | exact source and receiving episteme and EntityOfConcern values | viewing pins, or the exact A.6.4 arrow r and separate use assertion q |
| “Allowed only under policy P” | **Constraint / policy** (`constrainedBy`, `permittedUnder`) | work-step / publication item | policy/rule | policy pin, waiver/work ref |
| “Property belongs to object” | **Attribution / aboutness** (`attributedTo`, `aboutEntity`, `characterises`) | property/abstraction | object | observation/derivation witnesses |
| “This expression means … in this source” | **Source-local meaning lane** (F.0.1; F.17 only when a durable address or basis relation is needed) | local expression | local-sense claim | exact source passage and, when current, an obtaining basis relation |

This table is illustrative. Each row keeps its own direct relation and governor; it is not a list of species of one universal base relation or record. The meaning row remains only a do-not-model-as-basedness reminder.

*Note.* A.6.3 and A.6.4 define the viewing or retargeting arrow and any separate use claim. This table only classifies their references as relative-to-base cases; it defines no second operator, arrow, application, or use assertion.

#### A.6.6:4.7a - Support wording selection test

When a draft uses `support`, `supported by`, `supporting`, `support basis`, `support relation`, or a support-headed compound, do not first choose a more formal synonym. Ask what assertion the next reader needs.

If the sentence is genuinely about basedness, write the smallest direct form:

```text
dependent stands in <direct relation> to base
```

Identify the actual participants and apply that direct predicate. Stop there when it answers the use. Add scope, time, an assertion record, a reusable `RelationSignature`, occurrence identity, or evidence only when the predicate or one named receiver needs it.

If the sentence is not basedness, use the matching ontology:

| Support wording means... | Use... |
| --- | --- |
| an episteme bears on a claim | the exact A.2.4 evidence-use relation; use A.10 when provenance, currentness, rival explanations, or bounded reliance must be replayed |
| a claim is acceptable for material reliance | B.3, with the exact evidence relations kept separate |
| a causal, intervention, counterfactual, or simulation-only use is admissible | C.28 |
| a mathematical lens exposes preserved or lost structure | C.29, C.26, F.9, or the direct mathematical pattern |
| one thing helps or enables work | the applicable work, resource, capability, or action relation, or ordinary Plain help |
| a file, section, packet, or companion helps a reader | E.17, E.11, I.2, or ordinary orientation |
| a source, model, diagram, or view describes something | A.7, C.2.1, E.17, and the direct describing or source-use relation |

Do not create `SupportRelation`, `SupportBasis`, `SupportRecord`, `validatedBy`, or `verifiedBy` as a fallback. Work, a result episteme, its carrier, provenance, evidence use, and later reliance remain separate.

### A.6.6:5 - Archetypal Grounding

#### A.6.6:5.1 - System archetype: calibration to a standard

**Tell.** A lab instrument channel `TC‑17` is described as “anchored to ITS‑90”. Later, the reference standard is swapped, the phrase “still anchored” is kept, and the applicability window silently expands. Downstream work disagrees and nobody can reconstruct what changed.

**Show.** First state the direct assertion: `TC-17 is calibrated to ITS-90 for rig R3 over 0–200 °C during the stated calibration interval.` Apply the calibration predicate and stop there if this answers the use. When a later publication or comparison needs the exact assertion edition, show the same claim in an optional scoped record:

```
BD#Calib_TC17_v5 :=
〈 dependent    = ThermocoupleChannelRef(TC-17),
base         = StandardRef(ITS-90 / CalStd-2025-09),
directRelationKind = calibratedTo,
assertionPolarity  = affirmative,
scope        = WorkScope{rig=R3, range=[0..200]°C},
gammaTime          = interval[2025-09-01, 2026-03-01] 〉
```

When a later decision relies on this assertion, cite the exact A.2.4 evidence-use relation from the calibration-certificate episteme to the assertion. Use A.10 only if that decision also needs the producing Work, operation result, carrier, provenance, or currentness path. Then distinguish changes by what actually changed:

* New standard ⇒ **rebase** + **refreshWitnesses**.
* Wider applicability window ⇒ **retime** and likely **refreshWitnesses**.
* Relation-kind change (“not calibration, just normalisation”) ⇒ **changeDirectRelationKind** is not an edit; mint a new assertion or declaration and relate it to the prior one through continuity.

#### A.6.6:5.2 - Episteme archetype: an evaluation result used as evidence

**Tell.** A report says that model M improved accuracy by 4%. The team points to `EvalRun-2025-10-12`, but that Work occurrence is neither the claim nor an evidence relation, and its log carrier does not become evidence merely by being attached.

**Show.** First identify the result episteme that states the measured comparison and the target claim about the 4% improvement. State the exact A.2.4 evidence-use relation between that episteme and claim, including the relevant ClaimScope, polarity, window, and receiving use. If the decision also needs replayable source, carrier, provenance, currentness, or bounded-reliance information, use A.10 to cite the evaluation Work, its actual operation-result binding, the result episteme, the log carrier, and their independently obtaining direct relations.

Stop with the short evidence-use statement when it answers the question. No `validatedBy(claim, Work)` edge or scoped base-declaration record is required. If a project later needs a reusable evidence-relation declaration, that direct relation must first have its own participant meanings, predicate, applicability, and occurrence-identity rule.

#### A.6.6:5.3 - Structural archetype: constructive grounding of a model edge

**Tell.** A structural edge is published (“A componentOf B”) without a constructor trace. It becomes treated as “obvious”, while the construction chain is not recoverable.

**Show.** First state and test the direct `tv:groundedBy` assertion between the model edge and constructor trace. Stop when that assertion answers the use. If a publication needs a stable assertion edition with its current qualifiers, it may represent that C.2.1 episteme as:

```
BD#EdgeGrounding_ComponentOf_17 :=
〈 dependent    = WMEdgeRef(Edge:componentOf#17),
base         = TraceRef(Γ_m:ComposeCAL#c17),
directRelationKind = tv:groundedBy,
assertionPolarity  = affirmative,
scope        = PublicationScope{view=WMCardLite, system=S, line=L3},
gammaTime          = snapshot(2025-11-02) 〉
```

The exact trace reference names the relevant constructor trace. If another use relies on the assertion that the grounding relation obtains, cite its exact evidence-use and provenance relations separately. This example shows why “grounding” must be disambiguated: here it is a declared constructive relation with an explicit base (trace), not a vague claim of “stability”.

### A.6.6:6 - Bias-Annotation

| Lens | Bias introduced by this pattern |
| --- | --- |
| **Governance / assurance** | Prefers explicit witnesses and explicit time selectors for decision-relevant declarations; increases auditability but adds authoring overhead. |
| **Architecture** | Prefers the direct assertion and predicate first. It permits a reusable declaration or scoped assertion record only for a named receiver, reducing both hidden relations and record-first over-formalization. |
| **Onto-epistemic** | Makes the actual relation kind and direct predicate explicit; resists both metaphor-only wording and a universal base-relation kind. |
| **Didactic** | Teaches the short dependent–base–direct-relation question first; the optional record vocabulary appears only for a named later use. |

### A.6.6:7 - Conformance Checklist

A carrier conforms to A.6.6 when the checks relevant to its actual use pass:

1. **CC-BD-1 - Direct assertion first.** The actual dependent, base, direct relation, and readable affirmative or negative assertion are recoverable. The direct pattern supplies the predicate; a record or label does not.
2. **CC-BD-2 - Ordinary stop.** If that assertion answers the receiving question, no SlotSpecs, declaration record, witnesses, edition, occurrence identity, or assurance package is required.
3. **CC-BD-3 - Reusable declaration is demand-driven.** A `RelationSignature` appears only for an already admitted relation kind and at least two named consumers of the same participant meanings, predicate, laws, and applicability.
4. **CC-BD-4 - Assertion and occurrence stay separate.** A scoped witnessed record, when used, is a C.2.1 assertion or description episteme. It neither is nor creates the world-side relation occurrence.
5. **CC-BD-5 - Qualifiers are local.** Scope and time are explicit when the selected predicate or named receiving use depends on them; they are not a universal field kit. `Gamma_time` is not used as a proxy for evidence freshness.
6. **CC-BD-6 - Evidence ontology is direct.** Evidence use follows A.2.4 and A.10. Work, operation result, result episteme, carrier, provenance, evidence-use relation, and reliance remain separate; no generic `verifiedBy` or `validatedBy` edge is minted.
7. **CC-BD-7 - Crossings are conditional.** An actual relation between two exact F.17 cells uses F.9 only when its predicate obtains and keeps the bounded-use claim separate. A ReferencePlane crossing uses its applicable plane relation. One creates neither the other.
8. **CC-BD-8 - No silent retyping or direction flip.** Participant kinds and direction follow the direct relation. A mismatch is repaired by the applicable narrowing, Bridge, retargeting, or direct relation rule, not by renaming an endpoint.
9. **CC-BD-9 - Plain language remains sufficient.** Ordinary relation-specific prose is preferred. Functional or arrow notation is optional and may not replace the readable assertion.
10. **CC-BD-10 - Metaphors do not become ontology.** `anchor`, `ground`, `attach`, and `support` remain source-word triggers unless they name an already reserved primitive; no metaphor-headed fallback kind or relation is minted.
11. **CC-BD-11 - Meaning lane stays separate.** Source-local meaning starts with F.0.1 and uses F.17 only when a durable sense address or basis relation is needed; it is not a base-declaration record.
12. **CC-BD-12 - Change claims name the changed object.** Editing an assertion or reusable declaration changes that episteme. An actual relation change requires the direct relation's own change predicate and any separately current Work.
13. **CC-BD-13 - Optional history is proportional.** `declareBase`, `rebase`, `rescope`, `retime`, or `refreshWitnesses` is used only when a named receiver needs that declaration history. The label establishes no world-side fact.

### A.6.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| **Generic support bucket** | Hides whether support means basedness, evidence use, assurance, work enablement, navigation, source description, or ordinary help | Apply the support wording selection test; state the direct relation or keep ordinary help instead of minting a support-headed relation or record |
| **Umbrella “anchored/attached/grounded” with no direct relation** | Hides relation kind and predicate | Name the participants, use the relation-specific verb, and apply its direct predicate |
| **Perspective flip without recoverable participants** | Direction and typing become ambiguous | Keep the same participants and direction in both active and passive wording; add formal endpoint names only when reused |
| **Work or carrier treated as evidence relation** | Collapses producing Work, result episteme, carrier, provenance, evidence use, and reliance | State the exact A.2.4 evidence-use relation; open A.10 only for the replayable provenance or reliance path |
| **Implicit “current/latest”** | Violates explicit time discipline | Declare `Γ_time` explicitly and use witness timespans for freshness where needed |
| **Decision use without its actual basis** | A relied-on assertion cannot be checked | Cite the exact evidence-use, provenance, currentness, or assurance relations required by that decision; do not add a generic witness field or new document |
| **Semantic meaning expressed as basedness** | Confuses source-local meaning with another relation | Recover the source-local claim under F.0.1 and add an F.17 cell or basis relation only when needed |
| **Relation-kind change presented as an edit** | A semantic shift masquerades as continuity | State the new direct relation and use the applicable continuity rule when that history matters |
| **Using `*Slot` to name an endpoint/value** | Confuses SlotKind with ValueKind/RefKind; breaks substitution and tooling | Keep `*Slot` for positions; use `base`/`dependent` for values and `*Ref` for stored references |
| **Optional record field treated as a carrier or free-text kind** | Lets a record label stand in for the direct relation | Make the field identify the already admitted relation vocabulary entry; keep the assertion, carrier, and relation occurrence separate |

### A.6.6:9 - Consequences

**Benefits**

- A readable direct assertion can close an ordinary question without record-first work.
- Reusable declarations remain available when several consumers need the same participant meanings and laws.
- Scope, time, evidence, and continuity are explicit exactly where they change a predicate or receiving use.
- Evidence use, source-local meaning, semantic Bridges, plane crossings, and ordinary help keep their own ontologies.

**Trade-offs and mitigation**

- The author must identify the direct relation instead of hiding it behind *support* or *anchor*. The mitigation is one ordinary sentence and the direct predicate, not a universal form.
- A later replay or publication use may require more detail. Add only the missing declaration, qualifier, assertion, evidence, or occurrence identity at that point.

**Adoption test (informative).** A team has adopted A.6.6 when it can answer three questions in order: What are the actual participants and direct relation? Does its predicate hold for this case? Does a named later use require a reusable declaration, occurrence identity, scope, time, evidence, or history? A negative answer to the third question is a valid stop.

### A.6.6:10 - Rationale

**Why focus on base declaration rather than a metaphor.**
The recurring ambiguity is not “how to attach”, but which direct relation is being asserted between which participants. A readable relation-specific sentence exposes that answer; an optional declaration can then preserve it for a named reuse.

**Why keep the direct relation, assertion, and evidence separate.** The relation's predicate determines whether the world-side fact obtains. A C.2.1 episteme may assert it, and A.2.4/A.10 may support reliance on that assertion. Conflating these objects lets a record or carrier stand in for truth.
A base is a participant in the selected direct relation. Evidence or other supporting material justifies an assertion only through its own direct relations. Conflating the two makes both reasoning and audit unreliable.

**Why add scope and `Gamma_time` conditionally.** They are required when the direct predicate or receiving use changes across extent or time. Adding them everywhere hides the ordinary relation behind a universal qualifier form.
A declaration is never “everywhere forever” by default in FPF. Scope makes applicability explicit; `Γ_time` prevents hidden time dependence (“recent”, “current”, “latest”).

**Why prohibit kind edits.**
Changing the relation kind changes meaning; treating it as an update erases history and breaks continuity discipline.

**Why retain a local declaration-change lexicon.** When a named receiver tracks assertion or declaration history, the labels distinguish which episteme field changed. They are optional and do not describe actual relation change without the direct relation's own predicate.
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

**Specialises A.6.P Relational Precision Restoration.** A.6.6 handles basedness wording by recovering the actual dependent, base, and direct relation, then stopping or opening only the additional object required by a named use.

**Builds on A.6.REL and `A.6.0`.** The direct pattern supplies relation obtaining and occurrence identity. A reusable `RelationSignature` is justified only for an already admitted relation kind and shared declaration content; it creates no occurrence.

**Builds on A.6.5 only when reusable declaration content is current.** SlotKinds, ValueKinds, and reference modes type participant positions inside that `RelationSignature`; an ordinary one-case assertion needs no SlotSpec record.

**Coordinates with A.2.4 and A.10.** A.2.4 states the exact evidence-use relation. A.10 represents the independently established sources, Work, result epistemes, carriers, provenance, currentness, and later-use relations needed for bounded reliance. Neither pattern admits generic `verifiedBy` or `validatedBy` edges, and Work is not an evidence carrier.

**Coordinates with A.14 and C.2.1.** Constructive grounding and empirical grounding retain their exact direct predicates and participants. Their assertion epistemes and evidence remain separate from the world-side relations.

**Coordinates with A.6.3 and `A.6.4`.** Viewing and retargeting arrows, any use assertion, operation application, and Work remain distinct. A.6.6 adds no second arrow or universal relative-to object.

**Coordinates with F.9 and ReferencePlane rules conditionally.** F.9 applies only to an obtaining Bridge between two exact F.17 cells and keeps its bounded-use claim separate. A ReferencePlane crossing uses its applicable plane relation. If both are current, state both; if only one is current, introduce no object from the other branch.

**Feeds E.10 and F.18 lexical governance.** Umbrella words trigger recovery of the direct relation. Ordinary relation-specific prose remains valid; notation and durable public names are added only for a named use.

### A.6.6:End

