## E.17 - Multi‑View Publication Kit
> **Status:** Stable
> **Type:** Part E publication pattern
> **Normativity:** Normative unless explicitly marked informative

**At a glance.** Use `E.17` when one already accepted engineering account must be published in one or more readable faces for different readers without changing its claims.

**Use this when.** The source account is already accepted for the present work, but a reader needs a plain explanation, technical card, interoperability card, or evidence-facing lane. The publication task is to expose the same account for that reader, not to create a new engineering claim, perform work, pass a gate, or establish assurance by presentation.

**What goes wrong if missed.** A readable face can silently add, widen, or hide claims. The opposite failure is to make every publication start with a four-face kit, a newly authored viewpoint or bundle, and an assurance dossier even when one small face would answer the reader's question.

**What this buys.** Each current reader gets the smallest useful face, the source remains recoverable, omitted detail and bounded use stay visible, and stronger identity or assurance apparatus is added only when a downstream use needs it.

**First action.** Point to the current source account and the engineering object or relation it describes, name the reader and what that reader must be able to understand or do, and choose only the face or faces needed for that use. Resolve an existing viewpoint when one already fits; do not author a new viewpoint or bundle merely to start publication.

**First output.** One useful publication face, or the smallest necessary set, that names the source, intended reader/use, what it preserves or omits, and how to return to the source. No ClaimGraph, formal profile, viewpoint bundle, evidence package, or four-face completion is required for this ordinary result.

**Working publication move.** Select the current source; choose the minimum face set for the named readers; copy or conservatively arrange only source-backed claims; mark material omissions and the bounded use; publish and stop. If a face will carry safety, release, evidence, cross-context, or other consequential reliance, strengthen only that face with the relations and records that the reliance needs.

**Ordinary formality rule.** A source pointer, reader/use line, readable face, and visible omission or return note are enough when the face is used for orientation, inspection, explanation, comparison, exchange preparation, or planning preparation and no downstream identity depends on it.

**High-reliance formality rule.** When reliance changes the engineering move, identify the exact source edition; resolve the exact viewpoint and E.17.0 conformance only if `U.View` membership matters; identify the E.24.PUB publication occurrence, form, carrier, and bounded use when their identities matter; and cite the concrete evidence, gate, release, provenance, or assurance record that carries the downstream claim. These additions do not turn the face itself into that record.

**Stop condition.** Stop as soon as every current reader has a useful face that preserves the needed claims and exposes its return to source. Do not create unused faces, fields, viewpoints, bundles, or assurance records for kit completeness.

| Publication case | Smallest useful result | Overread to block |
| --- | --- | --- |
| A project lead needs a plain account and an integrator needs the corresponding typed details from one accepted interface account. | Publish only a plain face and a technical card, both pointing to the same source and stating their omissions. | The two faces are treated as different engineering claims or as a mandatory four-face bundle. |
| A release or safety decision will rely on one face. | Strengthen that face with the exact source edition, any material viewpoint conformance, publication identity, and the separate gate, evidence, or assurance references. | The readable face or `AssuranceLane` is treated as the gate, evidence, assurance result, or release permission. |
| A card is labelled `PlainView`, `TechCard`, or carries `viewpointRef`. | Treat the label or reference as publication metadata until the exact E.17.0 conformance relation for the selected episteme obtains. | A face label, readable layout, or packaged reference is taken to establish `U.View` membership. |
| A skill pack or callable access service exposes a framework face or pattern card. | Use it for access, source-finding, and bounded orientation with edition and source return visible. | Protocol availability is treated as framework architecture, source evidence, permission, performed work, gate authority, or release authority. |
| A README, preface, front matter, or other publication carrier states scope, edition, intended use, or source pointers. | Use it for orientation, source-finding, and edition awareness. | Publication appearance is treated as truth, currentness proof, authorization, assurance, gate passage, or work readiness. |

**Boundary aid pointer.** Use `E.17:5.1d` only when a publication-facing unit begins to carry a distinct work, evidence, gate, approval, status, explanation, comparison, or reduced-use claim. Ordinary publication of a source-backed face does not require that boundary map.

At the first screen, keep only the current source, named reader/use, minimum useful face set, visible omissions, and return to source.

**Not this pattern when.** Use `A.15.1` for a performed-work claim, `A.10` for an evidence or provenance path, `B.3` for assurance or engineering justification, `A.20`/`A.21` for constraint or gate decisions, `A.7` for carrier work, and the relevant release or authority rule when that is the actual problem. E.17 only publishes the already accepted account and keeps those downstream claims separate.

> **Tech-name:** `MultiViewPublicationKit` (**MVPK**)

> **General publication-face form:** In E.17, `MVPK face` refers by default to the publication form. The selected source episteme, any separately constructed receiving episteme, the bounded-use declaration, the publication occurrence, and the carrier remain different objects and are named explicitly whenever one of them is meant. A face is not a U-kind and does not become a `U.View`, evidence, assurance, gate decision, work occurrence, authority, or release permission by its label or readability. Source-edition, viewpoint, scope, occurrence, form, carrier, pin, or downstream-record identities are stated when they change the receiving use.
> **USM binding (overview):** when publication-scope identity must travel, `U.PublicationScope` under A.2.6 carries that bound; an ordinary bounded-use line can precede that exact record. See §5.0.
> **Episteme-side view position.** MVPK can publish an already recognized `U.View`, or it can publish another selected episteme without claiming view membership. When `U.View` membership is material, E.17.0 tests that same episteme against the exact `U.Viewpoint` episteme resolved from `publicationViewpointRef`; `PublicationVPId` is the viewpoint episteme's designator, not the reference. A.6.3 construction, E.17.0 conformance, E.24.PUB publication occurrence/form/carrier, and C.29 representation remain separate relations.

### E.17:1 - Intent

Let a practitioner publish the few readable faces that current readers actually need from one accepted engineering account, without adding claims or turning publication metadata into engineering authority. The optional morphism profile keeps the earlier compositional publication tests for uses that genuinely publish morphisms; it is not the entry price for ordinary publication.

### E.17:2 - Problem frame

* Different readers often need different slices or presentations of the same accepted account, but a current task may need only one or two faces rather than the full quartet.
* Informal renderings can drift semantics, hide omissions, or sever source return; composite morphisms can also lose traceability when their publication claims are used compositionally.
* `PlainView`, `AssuranceLane`, and a packaged `viewpointRef` are easy to overread as `U.View` membership, assurance, or conformance even though none establishes those claims by itself.
* Exact publication identity, pins, carrier relations, and evidence references matter for some receiving uses, but putting all of them before the first readable face makes ordinary publication unnecessarily hard.

**MVPK** therefore starts from the current source, reader/use, and minimum useful face set. It then adds viewpoint conformance, E.24.PUB occurrence/form/carrier identity, pins, bridge records, evidence, or assurance only when a named use depends on those distinctions. The optional morphism profile retains the functorial publication discipline for Description epistemes, including Description epistemes admitted for specification use. **Part E is conceptual:** no machine-exchange formats are specified here.

### E.17:3 - Problem

1. **Semantic drift in publication.** Unchecked presentations introduce claims not present in the exact C.2.1 source epistemes about the arrow. Each such episteme, including a Description episteme admitted for specification use, keeps its exact claim content, EntityOfConcern, and effective `U.ReferenceScheme`; publication form, viewpoint reference, scope, or carrier supplies none of those identity discriminators.
2. **Non‑compositionality.** Publishing `g∘f` yields faces that do not match composing the faces of `f` and `g`.
3. **View, viewpoint, and face confusion.** A template or face is treated as the view or viewpoint, with no exact conformance relation between two claim-bearing epistemes.
4. **Unpinned numbers.** Numeric claims lack unit, scale, reference‑plane, and **edition pins** from Part F or Part G, undermining auditability.

### E.17:4 - Forces

| Force | Tension |
| --- | --- |
| **Compositionality vs legibility** | Preserve arrow invariants across views ↔ keep each view didactic and audience‑appropriate. |
| **Neutral naming vs domain idioms** | Use vocabulary stable across domains ↔ allow local templates (SOPs, APIs, checklists). |
| **Publication-face independence (A.7)** | Publication preserves EntityOfConcern, Description-episteme, and specification-use boundaries ↔ authors expect rich presentations. |
| **Evidence discipline** | Views cite CG-Spec and CHR references when numeric or comparable claims are exposed ↔ authors want compact cards. |

### E.17:5 - Solution — the **MVPK Kit**

#### E.17:5.0 - Publication-scope and face-profile binding (normative)

* **Ordinary selection.** Start with the current source account, intended reader/use, and the smallest publication-form set needed now. A one-form result is valid; adding another form requires another current reader/use or a material distinction that the first form cannot carry safely.
* **Bounded use before exact scope.** Alongside each selected publication form, state the separate bounded-use declaration in ordinary prose. Identify an exact `U.PublicationScope` under A.2.6 when scope identity must travel across publication, comparison, exchange, dispute, or reliance. The scope establishes neither `U.View` membership nor permission, evidence, work, assurance, or release, and it encodes neither the selected source, viewpoint, publication-form profile, Publication Characteristics, nor carrier.
* **Resolve before authoring.** Reuse an existing viewpoint when its concerns and rules fit the reader/use. Author a new reusable viewpoint, or create a project-local family declaration under E.17.1, only when the current need cannot be served truthfully by an existing viewpoint or a simple bounded publication face. E.17.0 tests viewpoint conformance. Use E.17.1 to identify the catalogue edition, ordinary family designator, local declaration claim block, and needed `U.ViewpointRef` subset.
* **Optional profile.** A formal MVPK profile fixes exact publication-form designators, any declared partial order, Publication Characteristics and pins, and any cross-context or reference-plane constraints. These fields apply only to the optional formal or load-bearing branch, not to the ordinary first result.
* **Canonical labels.** `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are historical MVPK face designators. None identifies a `U.View`, `U.Viewpoint`, evidence object, assurance result, or gate. Use only the designators needed by the current readers; MVPK-Max is the optional profile in which all four have an actual use.

#### E.17:5.1 - Terminology (normative)

* **View** (`U.View`): the same C.2.1 episteme individual for which `EpistemeViewpointConformanceRelation(E,P)` obtains under E.17.0 for an exact `U.Viewpoint` episteme `P`. A publication-form label, `viewpointRef`, direct authoring, A.6.3 construction, or publication occurrence does not establish that membership. An ordinary publication form exposes its current source reference and separate reader/use declaration; add the exact `publicationViewpointRef`, conformance relation, scope, occurrence, carrier, or pins only when those identities change publication or reliance.
* **Publication vs expression vs bearing vs presentation vs rendering vs representation (guard):**
    * **Publication occurrence** = the E.24.PUB `EpistemePublicationRelation` among the selected episteme edition, audience declaration, bounded-use declaration, publication form, and `U.PresentationCarrier`. Ontically these participants stay distinct; spell out their exact identities when availability, recurrence, dispute, cross-context exchange, or reliance depends on them. Preparing or inspecting an ordinary face need not begin with a five-participant dossier. A.6.3 construction and E.17.0 conformance remain separate.
    * **Form expression** = `PublicationFormExpressionRelation` among the selected edition, exact publication form, and bounded-use declaration. It states that the form expresses enough of that edition for the use; omission, coarsening, or changed admitted operations can end it without changing the carrier.
    * **Carrier bearing** = `PublicationFormBearingRelation` between the exact `U.PresentationCarrier` and exact publication form. It states that this carrier bears the recoverable form; it is neither publication availability nor episteme identity.
    * **Presentation** = rhetorical arrangement of a published carrier; **notation-neutral**, adds no claims and is **not** a `publication-face kind`.
    * **Rendering** = display layout of a carrier, purely graphical formatting; performed rendering is separate `U.Work` on its exact carrier, not a `publication-face kind` or publication occurrence.
    * **Representation** = a C.29 representation and its exact correspondence to independently recovered objects or relations; it is not a publication occurrence, publication form, view-membership rule, or carrier. Publication or representation does not by itself make any represented object or relation exist.
* **Architecture-description mapping note.** An architecture **viewpoint** maps to one exact `U.Viewpoint` episteme; `PublicationVPId` or `EngineeringVPId` designates it and a `U.ViewpointRef` resolves it. An architecture **view** maps to one exact episteme that passes E.17.0 conformance. An MVPK face is the separate publication form through which that episteme may be exposed for a separately declared bounded use and, when material, in an exact publication occurrence.
* **No-mechanism equivalence:** MVPK is not a mechanism and no face acts. Build, rendering, upload, or delivery may be actual `U.Work` performed by an exact System recovered through A.13. When such Work is current, A.15.1 independently identifies the Work, performers, Method, time, and containing System. Add F.6 only when the publication account expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 leaves the Work intact. Name a carrier relation separately only when the claim or downstream use depends on it.
* **Viewpoint (`U.Viewpoint`)** - an exact claim-bearing episteme edition recognized under E.17.0's dependent-kind rule. Resolve an existing viewpoint when it already states the relevant concerns and conformance rules. Author a new reusable viewpoint, or create an E.17.1 local family declaration inside an exact catalogue episteme edition, only when the current reader/use cannot be served truthfully without that separate result. The declaration packages exact `U.ViewpointRef` values; it is not another bundle entity. `PublicationVPId` designates the viewpoint episteme; `U.ViewpointRef` resolves it.
* **Explanation-use profile values.** An existing publication form can be paired with a bounded explanation-use profile value such as `SourcePinnedExplanation`, `SourceLinkedExplanationReconstruction`, `DidacticRetelling`, or `SpeculativeRetelling`; the profile value is neither the form nor a new face, explanation, or carrier-rendering kind. Pins, provenance references, and no-new-A.6.B-boundary-claims discipline apply only when the exact source, transformation, or receiving use makes them material.

#### E.17:5.1a - Episteme-publication relation-position binding  *(normative)*

For functional-description publications, E.17 covers only the publication relation.

**Publication relation position.** A principle scheme, functional diagram, comparison table, screen, export, scenario, explanation, or code-like method description can help interpretation, source-finding, comparison, selected-method inspection, or work-planning preparation.

**Unsupported neighboring claims.** The publication does not by itself assert performed `U.Work`, a work claim, gate passage, evidence, assurance, engineering justification, supervisory relation or control relation, authority, release permission, or a new transformation-flow kind.

**Interface and protocol proximity.** When interface, protocol, schema, boundary, or API wording appears beside a functional-flow description, keep that operational claim with its project claim set and exact reference. Apply the boundary, interface, protocol, or transformation rules in `A.6.B`, `A.6.C`, or `E.18` as the concrete claim requires; do not absorb it into the publication by layout proximity.

**Retargeting.** If the publication changes the EntityOfConcern or retargeting target from an already described component, recovered transformation, method, work occurrence, transformation-flow structure, material `U.Entity`, or source claim into a functional, control, or flow architecture claim, this is not a same-entity publication-use change. Use `A.6.4`, `OntologicalReframing`, or `E.18` as applicable.

**Source recovery.** When a requested use requires a project-side object or relation beyond the publication face, first recover the existing reference that actually carries that claim. The bullets below are different concrete checks, not one grouped route or generic pattern relation:

- source wording, publication construction, carrier-relation construction, source relation, project-side reference, or explicit non-use disposition under `C.2.P`;
- appearance-based reliance repair under `A.15.4`;
- project `U.Method`, `U.WorkPlan`, or work-result record under `A.15`;
- evidence and provenance path under `A.10`;
- engineering-justification record under `B.3`;
- constraint or gate decision under `A.20` or `A.21`;
- supervisory or control architecture record under `B.2.5`;
- carrier, export, OCR, or front-end record under `A.7`;
- same-entity textual relation under `A.6.3.CR`;
- representation relation under `A.6.3.RT`;
- reduced-use-rendering relation under `A.6.3.CSC`.

**No backdating.** If no existing typed project-side FPF kind and reference named by value carries a claim that was supposed to already have a source relation, do not create a backdated source. Create only a prospective repair request, prospective decision request, prospective work-plan entry, or explicit missing-source-relation note, and treat the earlier claim or effect as unsupported until the required source exists.

Ordinary orientation and source-finding can stay as an inline note.

**Functional-description guard (`CC-MVPK-FD`).** A functional-description publication separates the source `U.Episteme` or episteme-side `U.View`, the exact publication form (the MVPK face), any present carrier or rendering work, the separate bounded-use declaration, and unsupported neighboring use. The guard applies only when a functional-description face is present; it is not the first universal MVPK conformance gate.

MVPK inherits the distinction among `U.Episteme`, contingent published-episteme use, publication occurrence, publication form, `U.View`, `U.PresentationCarrier`, and authority-reference relation. It introduces no durable published-episteme kind or other generic semio kind. A publication face does not define another relation's claim, supply authority, or become the source claim merely by being published; use the exact source or authority relation when one is current.

When a morphism publication is encountered or reused, name only the relation positions needed by the current use:

* the selected source `U.Episteme`, `D` episteme, or `S` episteme edition and the claims actually exposed; identify its exact ClaimGraph only when claim identity must travel;
* the exact `PublicationFormExpressionRelation` occurrence among that selected edition, exact form, and exact bounded-use declaration;
* the exact `PublicationFormBearingRelation` occurrence between the presentation carrier and form;
* the exact five-participant `EpistemePublicationRelation` occurrence when that selected edition is available to the declared audience for the bounded use;
* the selected episteme's independent E.17.0 `U.View` membership when the publication use calls it a view, plus any separate A.6.3 construction history when current;
* the exact system-performed carrier or rendering Work; any A.10 evidence/provenance path or G.6 path citation needed to replay it; and any G.11 currentness result, only when those neighboring facts are current; and
* the exact project-side object, reference, or authority relation when the next work or reliance claim depends on it.

Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme edition under C.2.1. Re-evaluate `PublicationFormExpressionRelation` only when its selected edition, form, bounded-use declaration, or obtaining predicate changes; re-evaluate `PublicationFormBearingRelation` only when its carrier, form, or obtaining predicate changes. Independently, changing any of the five `EpistemePublicationRelation` participants identifies another publication occurrence without reidentifying an otherwise unchanged episteme. Publication availability lost and later restored creates a later occurrence; a file rename or layout change alone proves none of those changes.
The practical payoff is that a reader can recover which relation is available for reliance: the episteme claim, the published form, the view, the carrier, the typed project-side FPF kind and reference named by value, or the authority-reference relation. A dashboard tile, generated explanation, card face, credential view, or carrier can guide source-finding, but it does not by itself establish the source claim or effect, gate decision, evidence relation, assurance claim, local system-role kind, separate System-classification judgment, assignment occurrence or state, direct status predicate, responsibility or authority predicate, Work occurrence, or permission. If its source uses *role or status* without making one of those claims clear, treat that phrase as unresolved recognition wording and route it through `E.10.ROLE`; then use the recovered direct pattern or return the exact missing governor.

**Source-exposure rule.** A face, carrier, rendering, dashboard tile, credential view, status view, comparison unit, explanation, signed memo, release record, approval publication, or gate dashboard exposes another project-side object only when that exact object and its direct relation are recoverable. Readability, layout, title, color, fluency, proximity, copying, generation, or reuse establishes none of them. If a real `SpeechAct`, `GateDecision`, evidence path, credential or status source, `U.Work` occurrence, `U.Episteme`, or publication occurrence is recoverable, rely on that object and relation; otherwise use the face only for orientation or source-finding.

**No retroactive source creation.** When the required source relation is missing, a new entry can be only a prospective repair request, prospective decision request, prospective work-plan entry, or explicit missing-source-relation note. It is not used as earlier evidence, approval, gate passage, instituting speech act, `U.Work` occurrence, release permission, engineering justification, or assurance for the unsupported past claim or effect.

#### E.17:5.1b - Shared source-relation and bounded-use vocabulary

Use this vocabulary when a publication face, rendering, generated text, comparison note, narrower-use rendering, source-finding cue, or authority-looking display can be overinterpreted as carrying a wider source relation or bounded-use permission than it actually carries. The vocabulary names the source relation or bounded-use value for one claim or use. It does not instantiate evidence, gate, assurance, work, commitment, speech act, decision, release, or authority.

| Source-relation or bounded-use value | Meaning for the local claim or use |
| --- | --- |
| `source-pointer-only` | The publication-facing unit points to a possible source but does not show that the source is available, was used, or makes the claim recoverable. |
| `source-relation-unknown` | The publication-facing unit does not yet show whether the needed source relation exists or makes the local claim recoverable. This blocks the downstream use until checked; it does not show that the underlying world claim is false. |
| `source-relation-not-needed` | No operative work, reliance, evidence, gate, assurance, bridge, source-dispute, release, or durable-naming claim is present for this publication-facing unit. Orientation, learning, source-finding, review, or planning preparation can proceed without inventing a source relation. |
| `source-not-recoverable-here` | The needed source relation can exist elsewhere, but it is not recoverable from this publication-facing unit or its stated source refs. Treat the unit as orientation or source-finding only, or reopen the source-bearing side. |
| `source-relation-absent` | The needed source relation is known absent from the current publication-facing unit and available source set for the stated use. Block that use; do not infer that the underlying world claim is false merely from this absence. |
| `source-available` | The cited source can be recovered or inspected for the current use. This does not yet show that the rendering used it correctly. |
| `source-retrieved` | The cited source has actually been recovered for the current check. This still does not show that it was used correctly or makes the local claim recoverable. |
| `source-used` | The inspectable generation, rewrite, rendering, comparison, work, or reliance source relation actually used the named source rather than only similar background. If that relation is unavailable, treat the unit as pointer-only or orientation-only until a source relation is recovered. |
| `source-faithful` | The publication-facing unit stays within the source claim relation for the stated use; omissions, declared source-loss modes, and additions are visible enough to inspect. |
| `claim-recoverable-from-source` | The local claim is recoverable from the source, declared correspondence relation, or required typed project-side FPF kind and reference named by value for the stated use. |
| `claim-not-recoverable-from-source` | The local claim is not recoverable from the source relation currently available. |
| `claim-conflicts-with-source` | The local claim conflicts with the available source relation. |
| `claim-plausible-only` | The claim can sound reasonable, but the source relation currently available does not carry it. |
| `source-omitted` | Relevant source claim, source passage, qualifier, condition, alternative, caveat, or uncertainty is missing from the publication-facing unit. |
| `source-loss-declared` | The publication-facing unit declares a source-loss mode such as omitted-detail, qualifier-loss, redaction, aggregation, scope-narrowing, recoverability-loss, or representation-factor-loss for the local source-to-rendering relation. |
| `claim-widened` | The publication-facing unit turns a source possibility, hypothesis, bounded condition, low-confidence statement, narrower permission, or source-finding cue into a wider claim or use. |
| `added-linkage` | The publication-facing unit adds a causal, explanatory, bridge, comparison, work, evidence, gate, or authority relation not already carried by the source relation. |
| `independent-verification-present` | A separate named record makes the local claim or use available independently of the face, such as an `A.10` evidence path, `B.3` assurance claim, `A.21` `GateDecision`, `A.20` constraint profile, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, or `F.9` Bridge Card. |
| `admissible-for-this-use` | The face is usable for the named bounded purpose only. Wider work, evidence, decision, bridge, gate, release, or assurance use requires the exact separate object and relation that carry that claim. |
| `downstream-use-forbidden` | The publication-facing unit is not used for the named downstream claim or effect because the needed source relation is absent, source-loss-declared, contradicted, or outside scope. |
| `reopen-trigger-present` | A stated change, dispute, use escalation, source update, context shift, missing source relation, or contradiction requires return to the source-bearing side or recheck of the concrete claim, predicate, definition, constraint, or downstream record. Add exact assertion or ClaimGraph identity only when that identity is material. |

Patterns can use shorter local field names such as `sourceRelationStatus`, `explanationSourceStatus`, or `representationValidityStatus` when the local object is clear. Comparative patterns split source-relation status from comparative-relation status instead of using one overloaded field. The local field remains interpretable through the vocabulary above, and the bounded use is named beside it when downstream reliance could change.

For ordinary use, name only the status distinction that changes the next bounded use. The common light states are `source-pointer-only`, `source-relation-unknown`, `source-relation-not-needed`, `source-not-recoverable-here`, `admissible-for-this-use`, `downstream-use-forbidden`, and `reopen-trigger-present`. The vocabulary is neither an ordered source-stage scale nor a source-record or authority taxonomy, and it does not substitute for evidence, assurance, gate, or work records. A missing source relation blocks only the unsupported use; it does not prove the underlying world claim false. If `independent-verification-present` is relied on, name the exact separate evidence, assurance, decision, work, or bridge record that performs that check.

#### E.17:5.1c - Shared use-boundary terms

Use these terms when a publication face, rendering, narrower-use rendering, explanation, comparison note, source-finding cue, or authority-looking display can be interpreted beyond its named source relation. Define them once here and link back to this section from local patterns instead of minting local synonyms.

| Term | Meaning for FPF use |
| --- | --- |
| `orientation use` | The publication-facing unit helps a reader find, inspect, triage, compare, teach, discuss, or prepare planning while the unit itself does not carry a downstream work, reliance, claim, or effect. |
| `reliance use` | The publication-facing unit is used as the source relation for an engineering claim or effect that changes a next work occurrence or reliance use, such as method choice, work plan, performed-work claim, release, gate, approval, an unresolved *role or status* phrase routed through `E.10.ROLE`, a recovered classification, assignment, assignment-state or direct-status claim, evidence, assurance, or external-impact action. |
| `work, reliance, claim, or effect` | A claim or instituted effect about method selection, selected method, `U.WorkPlan`, performed `U.Work`, work result, gate or release, an unresolved *role or status* phrase routed through `E.10.ROLE`, a recovered local system-role-kind classification, assignment occurrence, assignment state or direct status predicate, evidence, assurance, boundary or policy effect, or another typed project-side FPF kind and reference named by value. |
| `operative claim` | A claim whose acceptance would change the next bounded work occurrence or reliance use, the typed project-side FPF kind and reference named by value to recover, or the cross-context use of the publication-facing unit. Explanatory prose, examples, and source-finding cues are not operative claims unless they are used that way. |
| `non-admissible downstream use` | A wider use that the current source relation does not carry. Narrow the use, return to the source-bearing side, recover the missing relation, or apply the concrete work, evidence, decision, bridge, gate, release, or assurance rule that carries the wider claim. |
| `reopen trigger` | A dispute, use escalation, missing, stale, or contradictory source relation, source update, context or window change, or wider claim that requires source refresh, re-expansion, or application of the concrete rule or test carrying that claim. |
| `authority-looking case` | A recognition phrase for a publication-facing unit that can be overread as permission, approval, evidence, gate passage, assurance, responsibility, authority, release, or an unresolved *role or status* claim. It is not a U-kind or authority record. Route the unresolved source phrase through `E.10.ROLE`; then recover the current result: a local system-role kind and classification, an assignment, assignment state, another participant or status predicate, responsibility or authority, actual Work whose exact performer is recovered through A.13 and which A.15.1 admits independently, optional precise F.6 attribution when expressly consumed, ordinary non-use, or the exact missing governor. |

#### E.17:5.1d - Compact boundary aid for the present claim or effect

When a publication-facing unit, publication face, rendering, narrower-use rendering, explanation, comparison note, dashboard tile, credential view, status view, carrier, or generated unit creates more than one possible interpretation, separate the claim being made or effect being used now and cite the source relation that makes that claim recoverable. This compact boundary aid applies only to the present claim or effect; it does not classify the whole unit. The same unit can expose several typed records; handle one claim or effect at a time instead of assigning one source relation to the whole unit.

**Mixed-case precedence.** When several publication-use patterns appear possible, repair the smallest unstable interpretation that changes the current bounded use before applying a neighboring pattern whose claim or effect is present:

1. If one local head is the only unstable part, apply `E.17.AUD.LHR` or `C.2.P` and stop when the repaired sentence names the local kind, relation, and bounded use.
2. If the bounded `PublicationUnit` or its primary EntityOfConcern interpretation is unstable, apply `E.17.AUD` or `E.17.AUD.OOTD` before using `E.17.ID.CR` or `E.17.EFP`.
3. If the unit is stable and the present problem is comparison overread, apply `E.17.ID.CR`; use `F.9`, `C.11`, `A.20`, or `A.21` only when equivalence, recommendation, selection, decision, gate, or release claim is actually being made.
4. If the unit is stable and the present problem is explanation overread, apply `E.17.EFP`; use `A.10`, `B.3`, `A.20`, `A.21`, or `A.15.4` only when evidence, engineering-justification, gate, release, work, or reliance claim is actually being made.
5. If the present problem is a durable reusable name, UTS row, Core-facing term, or cross-context naming relation, apply `F.18`; otherwise keep the lighter local repair pattern.

| Present claim or effect question | Apply or recover |
| --- | --- |
| Is the face being used to guide work or reliance by appearance while the acting user still lacks the concrete project-side relation? | Use `A.15.4` to repair appearance-based reliance, then recover the actual `A.15`, `A.15.1`, `A.10`, `B.3`, `A.20`, `A.21`, `A.2.8`, `A.2.9`, `A.6.B`, or other project-side reference needed by that use. If that exact relation is already the live question, use it directly. |
| Is the publication-facing unit being used as evidence, provenance, attestation, currentness, freshness, or a claim-bound evidence relation? | Use `A.10` for the evidence/provenance path. When currentness or freshness is itself claimed, cite the G.11 result and let A.10 represent only the bounded source-to-use path. |
| Is the publication-facing unit being used as engineering justification, assurance, confidence, readiness, or limitations relation? | `B.3` assurance or engineering-justification claim with evidence, limits, and decay explicit. |
| Is the publication-facing unit being used as gate passage, constraint validity, adjudication, or release decision source? | `A.20` or `A.21` project records, including gate profile, constraint profile, decision record, log reference, scope, window, replay reference and freshness reference. |
| Is it the same EntityOfConcern with textual restatement only? | `A.6.3.CR Conservative Retextualization`. |
| Is it the same EntityOfConcern with representation scheme or reasoning medium changed? | `A.6.3.RT Representation-Scheme Transition`. |
| Is it deliberately reduced-use and useful only under narrower bounded use, `non-admissible downstream use`, and source-bearing reopen? | `A.6.3.CSC Controlled Semantic Coarsening`. |
| Is the primary issue explanation-facing rendering class on an existing MVPK face? | `E.17.EFP ExplanationFaithfulnessProfile`. |
| Is the primary issue one bounded comparative review unit over sources? | `E.17.ID.CR ComparativeReviewUnit`. |
| Did the EntityOfConcern, target, ontology frame, or claim or relation record named by value change? | `A.6.4`, `OntologicalReframing`, or the retargeting or reframing pattern named by value. |
| Is the publication-facing unit being used as bridge, substitution, equivalence, "same", "equivalent", "align", or "map" wording, or cross-context comparison relation? | Use Part F and `A.6.9` to repair the wording. Use F.9 for the obtaining Bridge, bounded-use claim, optional `CL`, evidence and loss boundaries, and optional Card. Use F.9.1 only for a separate stance note about that claim. Comparison alone is not a Bridge, and a publication face is neither the Bridge nor the note. |
| Is the live question carrier, export, OCR, screen, front-end behavior, or work on carriers? | `A.7` and the exact carrier relation, front-end relation, or work-on-carrier record. |

**Evidence-path boundary.** An `A.10` evidence/provenance path, including one that cites attestation, freshness, or a G.11 currentness result, carries only the claim named by value it instantiates. It does not approve or authorize work, pass a gate, perform work, supply release permission, or raise assurance or engineering-justification use unless the typed project-side FPF kind and reference named by value that carries that downstream claim is also instantiated, such as `A.15.4`, `A.15`, `A.20`, `A.21`, or `B.3`.

**Gate-display boundary.** A dashboard tile, status view, or release screen exposes a gate decision only when the `GateDecisionRef`, gate or constraint profile version, target release or work scope, time window, currentness, freshness reference or replay reference, and evidence path are recoverable. Without that exact gate record, the display remains orientation or source-finding only; it is not a gate decision, gate passage, release permission, or performed-work record by color, label, layout, or proximity.

#### E.17:5.1e - Local review fields are not FPF kinds

Local review fields and values in CR, RT, CSC, EFP, ID.CR, or a neighboring publication-use pattern are local aids for one case. They are not `U.Kind`, `RelationKind`, evidence, gate, authority, work, publication face, or another project-side object unless the pattern that defines that exact object establishes its membership. When a local field starts carrying such a claim, cite the exact object and say whether the cited pattern defines it, constrains it, or supplies its test.

#### E.17:5.1f - Shared anti-overread invariants for publication-facing units

Use the FPF pattern that defines, constrains, or tests the claim being made or effect under use. Keep any local review field local, preserve reduced bounded use, and address only the unsupported wider claim or effect through the source relation it requires.

**Source-relation minimality.** Name the smallest direct relation sufficient for the live use. A source reference, publication occurrence, evidence path, engineering-justification record, gate decision, and release decision are different objects or relations; choosing one licenses none of the others. Do not apply `A.10`, `B.3`, `A.20`, or `A.21` when the use needs only source-finding, orientation, or inspection of an existing source episteme, publication occurrence, or status-register entry.

**Local repair vs publication redesign.** A local epistemic precision repair is enough only when it can preserve the current publication face or `PublicationUnit` while fixing one head, boundary, source relation, bounded use, explanation class, or unsupported downstream claim. If layout, grouping, visual emphasis, comparison arrangement, generated explanation, hidden source limitation, or mixed EntityOfConcern packaging still induces overread after the local relation is repaired, create a redesigned publication face or `PublicationUnit` instead of adding warning text around the misleading form.

**Most-likely careful interpretation constraint.** Design and word a publication-facing unit so its most likely careful interpretation does not exceed its named source relation and bounded use. A visible `Approved` head needs a visible `GateDecision` or a different head; sorted output needs its comparator or sorting relation visible if no recommendation is intended; generated explanation separates inferred links from pinned source claims by wording, label, or source reference.

**Visual cue claim pressure.** Layout, order, color, prominence, icon, grouping, and proximity can imply evidence, readiness, preference, equivalence, approval, or verification. Green can suggest readiness; top position preference; grouping equivalence; proximity to evidence an evidence relation; a badge approval; and a lock or checkmark verification. If that implication would change the next action, recover the exact evidence, assurance, gate, decision, recommendation, bridge, approval, or other record or relation that actually carries it, or redesign the face so the unsupported overread is no longer invited.

**Extraction survival.** When a `PublicationUnit` is excerpted, quoted, screenshotted, summarized, copied into a tutorial, retold by a generator, or moved to a slide, it keeps only the claims, source pins, boundary line, references named by value, and bounded use carried in that extracted unit. Any use that depended on hidden neighboring context is lost unless that context is carried by source pins, a boundary line, or a reference named by value. A dashboard screenshot does not carry the underlying gate record, a quoted comparison row does not carry the full comparator or sorting relation unless that relation is included or referenced, a copied explanation paragraph does not carry source pins unless pins remain recoverable, and a pattern excerpt does not carry the whole pattern boundary unless the excerpt states or cites it.

**No-extra-pattern case.** If a publication-facing unit has bounded use only for ordinary orientation, learning, source-finding, review, comparison, or planning preparation, and no operative work or reliance, evidence, gate, assurance, bridge, source-dispute, or release claim is present, keep the existing publication source relation and proceed with ordinary use. The visible closure is: no operative work or reliance, evidence, gate, assurance, bridge, source-dispute, release, durable naming, or project-side source-relation claim recovered; ordinary publication wording remains bounded to the current use.

**Pattern-inflation anti-pattern.** Do not apply a neighboring pattern merely because the publication-facing unit resembles a worked example. Apply the neighboring pattern only when a claim being made or effect changes the next available project move.

**Strategic overread invariant.** Apply the same anti-overread rules whether the misleading interpretation is accidental, conventional, incentive-driven, or intentionally induced by publication design. Green status color without `GateDecisionRef`, reviewed-looking wording without approval, selective source links without operative-claim source relation, comparison ordering without selection decision, hidden caveats behind a source link, or pins for trivial claims beside unpinned causal linkage do not create evidence, gate, decision, assurance, work, release, or bridge relation by design pressure.

**Carrier-travel invariant.** A copied, exported, screenshotted, summarized, generated, translated, or re-rendered face can carry orientation or source-finding cues. It carries no evidence, authority, gate, approval, engineering justification, work, currentness, or release relation unless the exact corresponding object and relation remain recoverable for that use.

**Derivative-chain decay.** A second-order rendering inherits at most the bounded use that is explicitly carried from the prior source relation. It does not inherit source faithfulness, evidence relation, currentness relation, authority-reference relation, gate decision, work relation, or reliance relation by default.

**Publication-face snapshot and refresh identity.** A face can keep the same layout, name, or carrier while its source pins, data window, source-relation status, currentness, `EditionId`, or bounded use changes. Visual sameness is not source, evidence, or use-boundary sameness. Beyond orientation, identify the face edition or snapshot, the source pins or data window that still carry the claim, and any changed bounded use. If those cannot be recovered, use the face only for orientation/source-finding or reissue it from the source under E.17 and the concrete downstream rule that the new use needs.

**Claim-level source relation only.** Do not assign one whole-unit source-relation status unless every operative claim in that publication-facing unit has the same source relation named by value for the same use and unsupported downstream uses are explicit.

**Modality and deontic-force preservation.** Publication-facing transformations preserve possibility, obligation, permission, recommendation status, decision status, confidence, scope, and temporal window when those values change the claim or use. If one changes, narrow the bounded use or apply the concrete definition, constraint, decision, evidence, work, gate, or authority rule that carries it. Comparison does not become recommendation or decision; explanation does not become evidence; a face does not become authority; a publication unit does not smuggle a downstream effect; source-linked does not mean source-available for reliance; ready-looking does not mean gate-passed.

This preservation rule also applies across extraction, translation, screenshotting, summary, and generated retelling. A translated permission is not wider permission, a screenshot of approval-looking display is not an approval record, a summary of evidence is not an evidence path, and a generated retelling of a decision is not the decision record unless the source relation that makes the operative claim recoverable by value and source pins survive in the new publication-facing unit.

**Reader position is not a project system-role kind or assignment.** Reader position, audience, target user model, verifier position, review-reader position, and learner position do not become project system-role kinds, `U.SystemRoleAssignment` occurrences, decision authority, gate authority, issuer relations, responsibility relations, or Work contexts by publication. If any of those values is current, cite its typed project-side reference and direct predicate separately; otherwise record the exact missing governor rather than inferring it from a reader label.

**Source-gap states.** When the source relation is missing, say which source gap is present: source not named; source named but unavailable; source available but not used; source used but insufficient; source stale or outside its window; source contradicted; or mismatch among the source-maintenance System, any maintenance Work whose exact performer is recovered through A.13 and which A.15.1 admits independently, the status register, and a separately established responsibility relation. Add F.6 only when the source-maintenance comparison expressly consumes precise assignment-bound attribution; its failure leaves the maintenance Work intact. Assignment establishes neither source-maintenance responsibility, classification, nor status-register authority. Block only the unsupported effect and keep any reduced bounded use available.

**Measure and display overread.** A number, score, percentage, color, rank, confidence value, similarity value, dashboard state, or measurement display is orientation only until its measurement source, aggregation rule, time window, scope, calibration or evidence path, and intended use are recoverable. Use `A.10` for evidence, `B.3` for assurance, `A.20`/`A.21` for gate use, `A.15.4` plus the recovered work relation for work reliance, and F.9 for a Bridge or bounded-use claim. Use F.9.1 only for an optional stance note about an already constituted claim.

**World-contact stop.** A face does not self-refresh after source update, revocation, policy change, holon-state change, incident, model update, environmental change, or new observation. Refresh the source, reissue the publication, or recover the new concrete project-side record before downstream work, evidence, gate, control, carrier, or reliance continues.

**Functional-description boundary.** A functional, architectural, descriptive, representational, or explanatory fit claim creates no permission, obligation, approval, gate passage, release relation, performed-work evidence, or engineering justification. Those uses need the exact separate work, authority, evidence, decision, gate, release, or assurance object and relation that carry the claim.

**Mixed bundle no-shared-evidence-relation rule.** A bundle with source-pinned, reduced-use, speculative, didactic, comparison, and evidence-facing parts is not interpreted under one shared evidence relation or use-boundary value borrowed from another member. Each operative claim keeps its own source relation and unsupported downstream use.

**Educational usefulness.** Didactic, onboarding, tutorial, and workshop usefulness is real orientation aid. It is not evidence, gate passage, approval, work occurrence, engineering justification, release permission, or bridge relation.

**Comparison exposes conflict; it does not adjudicate it.** A comparison note can expose contradiction, asymmetry, different foregrounding, or residue. It does not select an option, approve release, pass a gate, or create bridge or substitution relation unless the corresponding `C.11`, `A.20`/`A.21`, `F.9`, or other exact decision relation carries that result.

**Same publication-facing unit, multiple interpretations.** A green release dashboard can be one MVPK face for source-finding, an `A.10` evidence/provenance path that cites a G.11 currentness result when the source query is recoverable, an `A.21` gate-decision view when the `GateDecisionRef` is recoverable, or an unsupported release cue when those sources are missing. A generated comparative explanation can be an `E.17.EFP` explanation-use case, an `E.17.ID.CR` comparison case, a `A.6.3.CR` generated-summary case, or source-finding only; it is never all of those under one shared evidence-relation class or bounded-use value by fluency alone.

**Archetypal publication-use cases.** Use these as quick recognition slices, not as a closed taxonomy:

- **Green dashboard tile.** A tile says `Model ready`. Treat the tile as the `PublicationUnit` when that tile carries the present release overread. The useful publication use is source-finding and status orientation unless an exact `GateDecisionRef`, gate profile, source relation, and evidence or currentness relation are recoverable. Without those, the tile is not release permission or gate passage by green color or placement.
- **Generated explanation with source links.** A generated text explains a method and cites sources. The explanation rendering is not source replacement. Source links carry only the pinned operative claims they actually carry. If work or reliance is present, use `A.10` for the evidence path named by value or keep the rendering as reader help; if the rendering is deliberately reduced-use, use `A.6.3.CSC`.
- **Comparison table.** A table compares two methods and places one first. Ordering is not selection. The comparator or sorting relation, source references, shared review frame, and unsupported downstream claim remain visible. Choice or decision needs `C.11`; equivalence or a Bridge needs F.9, while F.9.1 may add only an optional stance note about an established bounded-use claim.
- **Unrecovered source wording.** A draft uses source-object wording, undeclared interpretive-view shorthand, or generic unit wording without naming the FPF kind. Recover the FPF kind and relation positions instead of minting source-relation pseudo-kinds or undeclared interpretive-view pseudo-kinds. Use `PublicationUnit` only when a bounded reader-inspected unit inside a publication is present; otherwise use the exact episteme, view, publication, carrier relation, section of a named non-pattern FPF publication form whose reader-help function and reference are recoverable, `A.6.P` relation claim, or typed project-side FPF kind and reference named by value.
- **Translated tutorial.** A translated tutorial can improve reader access to an FPF pattern. It is a derivative rendering, not the original source. Operative claims need source mapping for reliance, translated heads can need `E.17.AUD.LHR` or `C.2.P`, and `F.18` is present only when durable naming, UTS, Core-facing, or cross-context naming work is intended.

**Practical harm prevented by neighboring pattern.** Use this map when the reader asks what the discipline buys in practice:

**Blocked overread with useful publication use remaining.**

- A comparison table appears to select option B. Block the selection interpretation when no `C.11` `ChoiceResult`, decision record, or visible selection relation exists. Useful publication use remains: use the table as a bounded comparison under `E.17.ID.CR`, or apply `C.11` when selection is intended.
- A green dashboard tile appears to permit release. Block the release or gate-passage interpretation when no `GateDecisionRef`, gate profile, evidence or currentness relation, and source relation are recoverable. Useful publication use remains: use the tile for source-finding and status orientation, then inspect the exact gate or evidence source if release work is intended.
- A generated explanation appears to prove a causal relation. Block the evidence or assurance interpretation when source pins and evidence path are absent or insufficient. Useful publication use remains: use the explanation as reader help or source-finding, then use `A.10` for the evidence path or `B.3` for the engineering-justification claim.

- `C.2.P` prevents the wrong object from being treated as source, the wrong relation from being treated as source relation, and a loose phrase from being treated as an FPF kind.
- `E.17.AUD` and `E.17.AUD.OOTD` prevent action on a publication unit whose primary entity of concern, carried publication move, or outside boundary shifted silently.
- `E.17.ID.CR` prevents a comparison unit from being used as decision, equivalence, bridge, evidence, or release source relation.
- `E.17.EFP` prevents fluent explanation from laundering unsupported claims into reliance, assurance, gate, or evidence use.
- `E.17` MVPK prevents a readable publication face from being treated as evidence, gate, work, authority, or release source relation by display quality.
- `F.18` prevents a local name from becoming global identity without context, kind, lineage, and bridge or cross-context naming relation.

**Anti-escalation examples.** Do not apply a neighboring pattern when its claim being made is absent:

- Do not apply `F.18` when a one-off local phrase repair restores the local kind, relation, and bounded use without minting a durable reusable name.
- Do not apply `A.10` when the publication-facing unit is not being used for reliance, evidence, provenance, currentness, or claim-bound evidence relation.
- Do not apply `A.21` when a dashboard tile is merely status orientation and no `GateDecisionRef` or gate profile is present.
- Do not apply `F.9` when a comparison does not claim sameness, substitution, bridge relation, or cross-context equivalence.
- Do not apply `E.17.EFP` when the text is only a same-entity rewrite or representation change under `A.6.3.CR` or `A.6.3.RT`.

**Concrete reopen trigger.** Name the condition and the nearest source-bearing side or the concrete definition, constraint, test, decision, evidence, work, or authority relation to revisit. A vague `reopen if needed` does not preserve the source relation.

#### E.17:5.2 - Declared `publication-face kind` values at Part E

Part E restricts exact `publication-face kind` values to the literals **publication face/form** and **interop publication form**. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are face designators, not additional U-kinds or automatic `U.View` memberships.

**USM linkage (normative when exact scope identity is current).** An ordinary face first states its bounded use. When that bound must be cited, exchanged, compared, or relied on independently, identify `U.PublicationScope` under A.2.6. For a face selecting episteme `E`, `PublicationScope(face_E) ⊆ ClaimScope(E)`. For a face selecting a capability-description episteme about `C`, `PublicationScope(face_C) ⊆ WorkScope(C)`. Neither inclusion grants permission to perform work or proves that work occurred. A cross-context semantic claim separately retains its F.17 endpoint senses, F.9 Bridge, bounded-use claim, and any current A.10 or B.3 reliance result. An optional F.9 `CL` summarizes evidence strength; it is not a relation or use condition.

**Publication-face naming discipline.**

* The exact `publication-face kind` values remain **publication face/form** and **interop publication form**.
* Concrete face designators end in **...View**, **...Card**, or **...Lane** only within this family; the suffix does not establish kind membership.
* `PlainView` is a historical face name, not a `U.View` claim. Use `U.View` only for an episteme that passes E.17.0 conformance.
* `AssuranceLane` can expose evidence bindings or pins, but it is not an assurance claim, evidence-sufficiency result, confidence verdict, gate, or release permission.
* **carrier**, **bearer**, and **holder** retain their exact carrier or relation meanings and do not name a view or publication entity.
* Any legacy `ViewFamilyId` token is only the ordinary family designator used to retrieve one local E.17.1 declaration claim block inside an exact catalogue episteme edition; it is not a local id kind, `U.View`, `U.Viewpoint`, bundle-membership rule, or face kind.

**Profiles select only needed faces.**

* **MVPK-Min:** one selected face, normally a `PlainView` or `TechCard-Lite`, for one current reader/use. No assurance or interoperability face is implied.
* **MVPK-Lite:** the minimum two or more faces needed by current readers; add `AssuranceLane-Lite` only for a real evidence-facing use and `InteropCard` only for an exact external consumer.
* **MVPK-SetReady:** add the faces and pins required for replayable or external interchange; concrete exchange formats remain outside Part E.
* **MVPK-Max:** use all four designators only when all four reader/use obligations are current. It is not the default completeness target.
* A *-Lite* face removes optional fields only, never claims. Enrichment adds fields or pins without retracting, widening, or strengthening the source claim.

#### E.17:5.3 - The publication-face kit

The optional morphism-publication profile uses representation-side constructors, not another viewpoint ontology:

1. `FaceObj_s` is the conceptual object component for publication face designator `s`.
2. `F_face` is the finite set of exact publication-form designators. Its default formality order is `PlainView <= TechCard <= InteropCard`; `AssuranceLane` remains independent.
3. `Emit_s(-) : EpMorphism -> FaceMorph_s` constructs candidate publication-form content for `s` when this formal profile is current. If that work also constructs a different claim-bearing episteme, identify that receiving episteme and its source relation separately.
4. The coherence rules in section 6 and the pin policy constrain this representation-side construction.
5. `InteropCard` may carry exact interoperability-concern references; concrete exchange schemas remain outside Part E.

`FaceObj_s`, `FaceMorph_s`, and `Emit_s` are local conceptual-form symbols. They are not public U-kinds, `U.Viewpoint` epistemes, `U.View` individuals, publication occurrences, or presentation carriers.

**Result.** `MVPK(f,F_face)` yields a C.13 collection of selected publication forms, each paired with a current source reference and separate bounded-use declaration. If publication work constructs a different claim-bearing episteme rather than only a form of the selected source edition, identify that receiving episteme and its A.6.3 or other exact source relation separately; it is not the face. For each actual publication, E.24.PUB separately tests form expression, carrier bearing, and the five-participant publication occurrence with its declared audience, bounded use, and recurrence rule. E.17.0 conformance, A.22 organization, and C.29 representation remain separate and are checked under their own patterns. If a current use depends on organization among selected forms or among separately identified epistemes, select the exact `U.Structure` under A.22 from the corresponding exact collection, obtaining organizing relations, applied constraints, and use frame; the face collection supplies no structure by itself. `PromoteFace[s->t]` changes publication-form explicitness; it changes neither episteme identity nor viewpoint membership and adds no claims.

#### E.17:5.4 - EntityOfConcern-side input and output vs publication (normative convention)

1. **Input and Output are signature-side declarations.** The **Input and Output** sections of a morphism describe declared input and output data or episteme types under the morphism signature; they do **not** depend on any publication face.
2. **No duplication on faces.** In the optional morphism profile, faces do not restate Input and Output lists; they carry only the source references, presence pins, and edition identifiers needed by the selected face and use.
3. **Use Signature only for signatures.** Use **Signature** only when the named object is a signature under an applicable signature pattern, such as `U.Signature`. On faces, use **TechName** or **PlainName**.
4. **Set-returning comparison.** Whenever a face shows selection or comparison, it returns sets or declared partial orders and does not hide scalarization; cite a `ComparatorSetRef` for any total order.
5. **Bridge and plane references.** A semantic crossing cites its F.9 Bridge and separate bounded-use claim. A plane-dependent value cites its characteristic, selected `ReferencePlane`, and applicable C.16 or A.19.CPM transfer or comparison rule. If B.3 is triggered and its assurance claim depends on an integration relation, retain that relation's B.3 `CL` and `Φ(CL)` reference; infer no penalty from an F.9 Bridge or publication face.
6. **Carrier references and relation positions.** When the use depends on them, name the carrier reference, any A.10 evidence/provenance path or G.6 path citation, and the G.11 currentness result; keep `U.Work` occurrences distinct from epistemic claims via relation positions.
7. **Publication is not execution.** Faces carry no time or resource semantics; any build, render, or upload work is separate **`U.Work`**.

#### E.17:5.5 - Pins and local publication-profile fields (normative; never "axes")

**Intent.** Make publication-time numeric, comparison, evidence-reference, and crossing claims explicit and auditable without minting another public kind or importing geometric metaphors. This is an optional formal branch. An ordinary publication form retains only the source pins needed to interpret claims actually used from it.

**Reuse existing value definitions.** A measured aspect is an admitted `U.Characteristic` with its membership predicate and Scale. A product of characteristic slots is an admitted `U.CharacteristicSpace`. A publication-profile field, abbreviated locally as a **PC field**, is only a field in the selected E.17 formal profile: it points to one of those admitted values or to another value or relation whose meaning is already defined. A PC field is not a `U.` kind, characteristic, evidence relation, comparator, bridge, or viewpoint by being present.

**Initial local fields.** Use only the fields that the selected publication form and receiving use consume:

* **PC.Number** — a displayed numeric or comparable value of an exact `U.Characteristic`; name the characteristic reference and its unit, scale, reference plane, and edition when they affect interpretation.
* **PC.EvidenceBinding** — a reference to an existing A.10 evidence path, evidence carrier relation, F.9 Bridge occurrence or description, or optional F.9 `CL` note; the field itself supplies no evidence, relation truth, or use permission.
* **PC.ComparatorSetRef** — a reference to the comparator family used by a declared partial order.
* **PC.CharacteristicSpaceRef?** — an optional reference to an exact admitted `U.CharacteristicSpace` when the claim is interpreted in that space.

These are local field names, not members of a catalogue of public kinds. A formal profile may declare another local field only by naming the admitted value or existing reference it carries, the predicate or relation that gives it meaning, the consuming publication use, and any required pins.

**Norms (E17-PC).**

* **E17-PC-1 (Exact grounding).** A numeric or comparable field resolves the `U.Characteristic`, the membership or interpretation predicate or CG-Spec reference that gives the value meaning, and material pins `{unit, scale, reference-plane, edition}`.
* **E17-PC-2 (Lexical discipline).** Forms and PC fields avoid “axis”, “dimension”, or geometric metaphors; use **Characteristic**, **slot**, and **CharacteristicSpace** where those admitted objects are actually meant.
* **E17-PC-3 (No hidden arithmetic).** A form does not hide aggregation or normalization; it cites the calculation or normalization definition and edition.
* **E17-PC-4 (Crossing).** For a semantic crossing, cite the F.9 Bridge and separate bounded-use claim. For a plane-dependent value, cite the selected `ReferencePlane` and applicable transfer or comparison rule. Add an F.9 `CL` note or B.3 penalty reference only when the receiving use actually consumes it; a field manufactures none of these relations or claims.
* **E17-PC-5 (Edition pinning).** Fields that rely on maps, distances, spaces, set semantics, or transfer rules pin the exact applicable editions and trigger reissue when those editions change.
* **E17-PC-6 (Viewpoint conditionality).** The separate bounded-use declaration says why each field is present. Resolve `publicationViewpointRef` only when the selected episteme is claimed as a `U.View` or the formal operation actually depends on that viewpoint. `PromoteFace[s->t]` may reindex or annotate a form; it adds and widens no claim.

**Publication-form responsibilities when this profile is selected.** `PlainView` may show **PC.Number** only when the exact characteristic and material pins resolve; otherwise use qualitative wording. `TechCard` may add **PC.ComparatorSetRef** or **PC.CharacteristicSpaceRef?** only for a declared ordering or characteristic use. `AssuranceLane` may carry **PC.EvidenceBinding** only as a pointer to the exact evidence or policy relation. `InteropCard` remains notation-neutral and points to the references needed by the external consumer.

**Extending the profile.** Give a new local field a plain and technical label, the value or reference it carries, the predicate or relation that gives it meaning and establishes membership or applicability, the identity-relevant edition, pinning rule, and one named consuming use. If the work instead needs a new public ValueKind, return that as a separate kind-settlement and product decision; E.17 does not admit it by declaring a field.

**Adding or changing invariants.**

1. Put a new invariant in the CG-Spec or other specification-use source that defines it; supply the test there.
2. Version any affected `U.CharacteristicSpace`, comparator, map, distance, or transfer rule; publish an explicit correspondence relation when semantics change and never mutate slots in place.
3. Update an `A.21` gate check only when an actual gate consumes the invariant. Publication conformance can warn or block only according to the selected profile and bounded use; it does not create an operational gate.
4. State the edition-change and Lean-profile downgrade behavior that the concrete consuming use needs.

#### E.17:5.6 - Author ergonomics (non-normative)

*Quick author steps:*

1. **Name source and reader/use.** Point to the current source account and say what this reader must understand or do.
2. **Choose the minimum face set.** Start with one face; add another only when a different reader/use needs different detail or form. Copy no claim that the source does not carry, and state material omissions.
3. **Publish, compare, and stop.** Check the face against the source and stop when the named reader/use is served. Add exact viewpoint, scope, occurrence, pin, bridge, evidence, gate, or assurance records only when that stronger use makes their identities material.

For the optional morphism profile, declare `F_face`, pin numeric or comparable content once, and run only the composition and promotion tests actually claimed by the selected faces. A *-Lite* face may drop optional fields but never add or strengthen claims.

### E.17:6 - Rules and Invariants (normative)

**Publication-composition local test bundle.** A face that claims compositional publication passes five local tests:

1. `identity`: `Emit_s(id_X)` is the identity face morphism for `FaceObj_s(X)`;
2. `composition witness`: the face for `g o f` matches the composition of the faces for f and g, or is marked non-compositional or explanatory-only;
3. `no-new-claim diff`: comparison with the selected source episteme shows only formatting, indexing, pinning, or conservative construction;
4. `monotone promotion`: a richer face adds fields, pins, or typing without retracting or strengthening the source claim;
5. `scope non-widening`: `U.PublicationScope` stays within the exact claim or work scope used by the selected description.

For composable arrows `X -f-> Y -g-> Z` and exact `s,t` in `F_face`:

1. **Functoriality and typing per face.**
   * `Emit_s(id_X) = id_{FaceObj_s(X)}`.
   * `Emit_s(g o f) = Emit_s(g) o Emit_s(f)` only when the face carries the local witness.
   * If `f : X -> Y`, then `Emit_s(f) : FaceObj_s(X) -> FaceObj_s(Y)` is total in the selected formal substrate. An ill-typed composite blocks that formal claim; it is not repaired by weakening conformance.
2. **Face-promotion coherence.**
   * If `s <= t`, the t-face is a more explicit publication form for the same selected source claims.
   * `PromoteFace[s->t]_X : FaceObj_s(X) -> FaceObj_t(X)` is natural in X.
   * Identity and composition of `PromoteFace` follow the selected formal substrate. `AssuranceLane` is outside the default formality chain.
3. **Source episteme and construction.**
   * Every `Emit_s` use names the exact source episteme edition. It resolves an exact `publicationViewpointRef` only when the selected episteme is claimed as a `U.View` or the formal operation's definition actually depends on that viewpoint.
   * When another episteme is actually constructed from the source, use A.6.3 to identify that source-to-receiving construction relation. The face constructor is not a species of `U.EpistemicViewing`, and A.6.3 does not establish `U.View` membership.
   * Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme under C.2.1. Changed form, carrier, or publication occurrence does not by itself.
4. **Pin discipline.** Numeric or comparable claims used from a face retain the unit, scale, reference-plane, and edition pins required by the applicable characteristic and measurement patterns.
5. **Publication is not work.** Build, rendering, upload, or delivery is `U.Work` only when each exact actual performer has its A.13 core and A.15.1 independently admits the dated occurrence. F.6 enters only when the publication account also consumes precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 leaves the Work intact. A face, emitter symbol, view episteme, or publication occurrence does not act.
6. **Publication and carrier separation.** E.24.PUB identifies the selected episteme edition, publication occurrence, form, and presentation carrier separately. A.10 supplies the evidence/provenance source-to-use path, G.6 supplies addressable path citation, slicing, and local refresh, and B.3 supplies any assurance claim.
7. **Cross-context and reference-plane use.** For a semantic crossing, recover the F.17 endpoint senses, F.9 Bridge, and separate bounded-use claim. For a plane-dependent value, retain the characteristic, selected `ReferencePlane`, and applicable transfer or comparison rule. Add A.10 or B.3 only when reliance is current; an optional F.9 `CL` summarizes evidence strength and never grants use. Visual juxtaposition and scheme difference alone establish none of these claims.
8. **PublicationScope discipline.** For a face use v selecting episteme E, `PublicationScope(v)` does not exceed the claim scope on which that publication relies. A capability description may also cite a work scope, but the publication scope does not grant work admissibility. `PromoteFace` does not widen either scope.

The equations are conceptual-form constraints on the optional morphism-publication profile. They do not turn face symbols, formulas, or diagrams into world-side relations, viewpoints, views, publication occurrences, or work.

### E.17:7 - Objects used by the optional formal profile

| Object or symbol | Function | Boundary |
|---|---|---|
| source episteme E | carries the selected claims about its EntityOfConcern | identified under C.2.1 |
| `publicationViewpointRef` (conditional) | resolves publication viewpoint episteme P only for a material `U.View` claim or viewpoint-dependent formal operation | designator and reference remain distinct from P |
| `F_face` | finite C.13 collection of publication-form designators for this profile | not a viewpoint bundle or `U.ViewFamily` |
| `Emit_s`, `FaceObj_s`, `FaceMorph_s`, `PromoteFace` | conceptual-form symbols for constructing and checking publication-form content | defined only in the representation-side formalism; no U-kind membership follows |
| receiving episteme, when separately constructed | its claims are checked against the source and, only for a material `U.View` claim, against P | A.6.3 construction and E.17.0 conformance are independent claims |
| publication occurrence, form, carrier | makes the selected episteme available to a declared audience and use | E.24.PUB identifies these participants and tests whether the publication relations obtain |

In the optional morphism profile, the author selects source E and publication-form profile `F_face`; P is selected only for a material `U.View` claim or a formal operation whose definition depends on that viewpoint. A system performs any authoring, rendering, checking, or publication work. MVPK names the publication method and constraints; it neither acts nor mints a view-family entity.

### E.17:8 - Archetypal Grounding (SoTA-aligned Local Tests)

Read these examples as local tests for MVPK invariants, not as source citations by reputation.

**Ordinary two-reader publication.** An accepted interface account already states the service boundary, messages, and failure conditions. A project lead needs a short explanation and an integrator needs the typed details. Publish one `PlainView` and one `TechCard`, both pointing to that same account and stating what they omit; do not create `InteropCard`, `AssuranceLane`, a new viewpoint bundle, or a formal composition witness unless a later use actually needs them. The face labels establish neither `U.View` membership nor assurance.

The remaining examples exercise optional formal or load-bearing branches.

1. **Composite service pipeline (`InteropCard` + `AssuranceLane`).**
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability face whose path claim matches the declared relational composition of the two source claims; `AssuranceLane(g∘f)` cites the A.10 evidence/provenance path and, only when replay needs a stable path address, its G.6 `PathId` or `PathSliceId`. The faces neither establish that composition nor become evidence carriers.
2. **Control loop morphism (`TechCard` + `PlainView`).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed specification toolchains.)
3. **Optics-informed composition witness.**
    * Profunctor and optic accounts are useful only as a source idea for why compositional publication matters. The local FPF test is still the MVPK witness: emit the face for `g∘f`, compose the emitted faces for `f` and `g`, and compare them. If the comparison is not supplied or fails, the face stays non-compositional or explanatory-only; optics vocabulary does not carry the rule by analogy.

4. **Functional-description publication (`PlainView` + `TechCard`).**
    A principle scheme or functional diagram can publish a readable relation from signature or principle episteme content to method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement. The MVPK faces can help inspect that relation and prepare a work plan, but they do not become work, gate passage, evidence, engineering justification, or control architecture. When one of those claims is current, recover its concrete `A.15`/`A.15.1`, `A.10`, `B.3`, `A.20`/`A.21`, or `B.2.5` record; if none exists, create only a prospective repair, decision, or work-plan request rather than backdating the claim.

### E.17:8.1 - Bias-Annotation

E.17 blocks publication-face bias: a face, card, view, rendering, source pointer, dashboard tile, or generated explanation is treated as if readability or layout created the underlying claim, evidence, work, gate, authority, or release relation. It also blocks source-proximity bias: a source-proximate face points near source material or a source relation, but the operative source relation still has to be recoverable by value.

### E.17:9 - Conformance Checklist (normative)

`CC-MVPK-FD` is the functional-description guard in §5.1a. It is conditional on a functional-description publication face and does not function as the first universal MVPK gate.

A conformance check is kept only if it changes the next bounded use of the publication face, blocks a concrete overclaim, or preserves a source reference or reopen condition needed for the declared bounded use.

#### E.17:9.1 - Core ordinary checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC-MVPK-1 (Source, reader, and use visible)** | Each ordinary publication form points to the current source account and exposes the separate reader/use declaration it serves. | A cold reader can find the source, understand why this form exists, and see material omissions. |
| **CC-MVPK-1b (`U.View` claim conditional)** | Only when the selected episteme exposed through a face is claimed as a `U.View` does the publication resolve an exact `publicationViewpointRef` and cite the obtaining E.17.0 conformance relation. | A form label, layout, or packaged reference alone is rejected as membership evidence. |
| **CC-MVPK-1a (Publication relations explicit when load-bearing)** | When availability, recurrence, dispute, external exchange, or reliance depends on publication identity, name the selected edition, audience, bounded use, form, carrier, expression relation, bearing relation, and publication occurrence. | The exact values resolve only for that stronger use; an ordinary face is not rejected for lacking an unused identity dossier. |
| **CC‑MVPK‑3 (No content extension)** | `PlainView`, `TechCard`, and `InteropCard` add **no new claims** beyond the underlying Description epistemes, including Description epistemes admitted for specification use. | Red‑line vs Description episteme, including any exact specification-use source, shows only formatting or indexing. |
| **CC-MVPK-4 (Pins and source references when material)** | Numeric or comparable claims relied on through a publication form retain the units, scale, reference plane, edition, and source references that change their interpretation; an ordinal-only claim stays comparison-only and is neither averaged nor converted to a z-score. | Relevant pins are visible, and an ordinal-only face contains no mean or z-score; a qualitative ordinary form carries no irrelevant pin dossier. |
| **CC-MVPK-4j (Publication bound visible)** | Alongside every selected form, the separate bounded-use declaration is visible; identify exact `U.PublicationScope` when that bound must travel or constrain a stronger use. | The ordinary use line is readable, and any load-bearing scope reference resolves without granting work or reliance. |
| **CC-MVPK-5 (Return and carrier boundary)** | Every selected form retains a return to source; identify the carrier, the needed A.10 evidence/provenance path or G.6 path citation, and any G.11 currentness result only when carrier identity, carrier work, reliance, evidence, replay, or currentness is material. | Source return is visible; stronger carrier/provenance references appear only where used. |



#### E.17:9.2 - Conditional checks

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC-MVPK-0 (Lean conditional guard)** | A Lean face checks only features it actually carries: set or partial-order semantics for a real selection/comparison, relevant pins for numeric or plane-dependent claims, an F.9 Bridge plus bounded-use claim for a semantic crossing, and a selected `ReferencePlane` plus applicable rule for a plane-dependent value. | No absent selection, number, semantic crossing, or plane dependency creates a placeholder field or failed check. |
| **CC‑MVPK‑2 (Functoriality)** | `Emit_s(id)` is identity; `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)`. | Compose two cards and diff with the card of the composite. |
| **CC-MVPK-3b (Boundary claim-set integrity)** | If a published arrow is a boundary, interface, or protocol and an A.6.B claim set exists (`L-*`, `A-*`, `D-*`, and `E-*`), then normative text on faces is traceable to that claim set (prefer claim-ID citations); faces do not become a second boundary specification. | Lint flags uncited normative clauses; faces reduce to {claim-ID citations + informative commentary}. |
| **CC‑MVPK‑4b (Lean evidence-facing lane)** | If `AssuranceLane-Lite` is used, presence bits for current evidence or bridge references suffice; full evidence-carrier lists remain with the exact evidence source. | Presence bits are visible, and no assurance or sufficiency claim is inferred from the lane. |
| **CC-MVPK-4c (Input and Output vs publication)** | When a morphism face exposes input/output information, it points to the signature-side declarations instead of duplicating them; it carries only source references and pins needed by the face. | The face has no second Input/Output specification and no unused presence-pin dossier. |
| **CC-MVPK-4d (Set-returning ordering)** | Any selection or comparison on faces returns sets or declared partial orders with a **ComparatorSet** citation. | No hidden scalarization; ComparatorSetRef present. |
| **CC‑MVPK‑4e (Signature on faces — banned)** | The term **“signature”** is **not used** on faces; use **TechName** or **PlainName**. | Token scan: no “signature” on faces. |
| **CC‑MVPK‑4f (Numeric and optional-PC discipline)** | Numeric or comparable claims retain the source pins that affect interpretation; when the optional PC profile is selected, its PC and CHR/CG references are explicit. | Cards show the material unit, scale, reference-plane, and edition pins; selected PC fields resolve without making PC classification a prerequisite for an ordinary face. |
| **CC‑MVPK‑4g (No axis or dimension)** | Faces avoid “axis”, “dimension”, and “plane” metaphors except **ReferencePlane**; use CHR terms (**Characteristic**, slot, or **CharacteristicSpace**). | Lexical check flags none; only `ReferencePlane` appears. |
| **CC‑MVPK‑4h (Edition pins on defs)** | Where maps, distances, or spaces are cited, the face pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition?`. | Validation shows edition fields populated. |
| **CC‑MVPK‑4i (Crossing references)** | A semantic crossing cites its F.9 Bridge and separate bounded-use claim; a plane-dependent value cites its selected `ReferencePlane` and applicable rule. A B.3 `CL`/`Φ(CL)` reference appears only when the current assurance use consumes that integration relation. | F.9 and plane references resolve; any B.3 penalty belongs to the assurance-bearing integration relation, not to the face. |
| **CC‑MVPK‑4k (Subset‑of underlier)** | For views about epistemes or capabilities, `PublicationScope ⊆ ClaimScope or WorkScope`; reindexing **does not widen** it. | Subset witness passes; promotion diff shows no widening. |
| **CC‑MVPK‑6 (Γ‑separation)** | No cost, time, or data-spend on publication morphisms. | CI shows proof records or witness records; gate validation passes. |
| **CC‑MVPK‑7 (Reindexing monotone)** | If `s ⪯ t`, then `Emit_s(x) ⪯ Emit_t(x)`. | `TechCard` ≤ `InteropCard` (more structure, same claims). |
| **CC‑MVPK‑8 (`publication-face kind` discipline)** | Only literal `publication-face kind` values **publication face/form** or **interop publication form** are used; faces are named **...View** or **...Card**. | Token scan; no “rendering” or “presentation” as `publication-face kind` values. |
| **CC‑MVPK‑9 (Reindexing naturality)** | Conceptual-form coercions `PromoteFace[s->t]` exist, are total in the selected formal substrate, and commute with composition. | The local witness uses `PromoteFace` and is not overread as a world-side relation. |
| **CC‑MVPK‑10 (Iso‑preservation)** | Isomorphisms in `U` remain isomorphisms under each viewpoint. | Cards show mapped inverses or an iso‑witness. |
| **CC‑MVPK‑11 (Typing & totality)** | Ill-typed composites are rejected at `FaceObj_s` rather than weakening the selected conceptual-form rules. | Type-check fails early; no best-effort composition claim appears on cards. |
| **CC‑MVPK‑12 (Crossing distinctions)** | A cross-context semantic face keeps the F.9 Bridge, bounded-use claim, and reliance result distinct; a ReferencePlane-dependent face keeps its characteristic, plane, and transfer or comparison rule distinct. Optional F.9 `CL` and B.3 integration `CL` remain in their own uses. | The face exposes only the references consumed by its bounded use and grants no crossing, reliance, or assurance by display. |

### E.17:10 - Common Anti-Patterns and How to Avoid Them

1. **“Presentation logic” as semantics.**
    *Fix:* Keep every claim in the source ClaimGraph. When a reader needs to know how a claim arose, name the exact authoring, measurement, observation, model, source-use, representation, or refinement relation. Use an exact specification-use gate, CG-Spec, or KD-CAL when it owns the requirement; keep views declarative; publication adds **zero** claims.
2. **Publishing only view objects.**
    *Fix:* The optional formal profile constructs faces for `g o f`, not only endpoint faces for `FaceObj_s(X)`, `FaceObj_s(Y)`, and `FaceObj_s(Z)`. A system performs the construction work; MVPK does not act.
3. **Unpinned numbers.**
    *Fix:* Reject card; supply **pins** plus CG and CHR references.
4. **Face presented as a view without conformance.**
    *Fix:* Resolve the exact viewpoint episteme and apply E.17.0 to the exact candidate episteme; redesign or re-emit the face only after the semantic repair.
5. **`InteropCard` equivalent to `TechCard` duplication.**
    *Fix:* `InteropCard` can refine typing or shape but cannot contradict `TechCard` (reindexing monotone).

### E.17:11 - Consequences

| Benefit | Why it matters | Trade-off and mitigation |
| --- | --- | --- |
| **Arrow traceability.** | Composition preserved across views enables chain‑of‑evidence on pipelines. | Slight authoring overhead → MVPK templates. |
| **Review-ready faces.** | Pins plus CHR references make numeric claims verifiable. | Declared publication checks perform MVPK checks; project gates stay with the relevant `OperationalGate(profile)` or `GateDecision` source when the gate claim is present. |
| **Terminology hygiene.** | Clear View vs Viewpoint, Publication vs Presentation. | Enforce publication-face-kind discipline tokens in CI. |
| **Notation independence.** | Viewpoints talk concerns, not tools. | Provide adapters to local publication toolchains. |

### E.17:11.5 - Rationale

Multi-view publication is needed because one account can serve several concerns without any face becoming the whole account. Source return, bounded use, and material omissions must be visible enough for ordinary reading; exact viewpoint, correspondence, currentness, publication, evidence, assurance, decision, architecture, and release relations are added through their concrete defining or checking patterns only when the receiving use needs them.

### E.17:12 - SoTA-Echoing: Adopted And Adapted Invariants And Rejected Shortcuts

**SoTA and local-rationale alignment rule.** Read each external-source row as source idea -> local FPF invariant -> practical local test -> shortcut rejected. A cited source contributes only the idea translated into this pattern. A row deduced from named current FPF patterns is labelled local design rationale and is not presented as external SoTA evidence.

| Current source idea or explicit local design rationale | Local FPF invariant and practical local test | Adopted, adapted, or rejected shortcut |
| --- | --- | --- |
| Joint ISO, IEC, and IEEE 42010:2022 architecture-description practice, used as established practice lineage rather than current architecting SoTA, separates architecture description, stakeholder concern, viewpoint, view, model kind, correspondence, and correspondence rule. | MVPK publishes one source-pinned face over an exact selected episteme edition; when `U.View` membership is material, it separately resolves the exact viewpoint episteme and E.17.0 conformance. Publication occurrence, form, carrier work, rendering work, correspondence relation, exchange envelope, and evidence envelope remain distinct and are identified only when the receiving use depends on them; the no-new-claim diff always applies. | Adopt the object distinctions; reject the shortcut where a readable face or standards label becomes a view, evidence, work occurrence, gate passage, release permission, bridge relation, or exchange authority by presentation alone. |
| Pickering, Gibbons, and Wu, *Profunctor Optics: Modular Data Accessors* (ICFP 2017; arXiv [`1703.10857`](https://arxiv.org/abs/1703.10857)), and Clarke et al., *Profunctor Optics, a Categorical Update* (2020; arXiv [`2001.07488`](https://arxiv.org/abs/2001.07488)), used as a research/theory lineage rather than downstream-reliance evidence, provide the concrete compositional-optics source idea. | MVPK adopts only local publication-composition tests: identity, composition witness, no-new-claim diff, monotone promotion, and scope non-widening. | Adopt the five-test publication-composition bundle; reject optics vocabulary as proof by analogy or as a replacement for local witnesses. |
| **Local design rationale, not external SoTA evidence:** current FPF `C.16` defines characteristics, scales, measurement procedures, and result interpretation; `A.19` defines admitted `U.CharacteristicSpace` values and their slots. E.17 reuses those definitions because omitting a material unit, scale, reference plane, or edition can change the value read from a publication form. | A numeric or comparable value exposed through a publication form retains the characteristic reference and every pin that changes interpretation; focused test: remove each pin in turn and reject the form for the bounded use only when the interpreted value changes or becomes unresolved. | Adopt the existing characteristic and scale discipline; reject readable numbers and a local PC label as self-validating values or new kinds. |
| **Local design rationale, not external SoTA evidence:** current FPF `E.24.PUB` separates selected episteme, publication form, carrier, bounded use, and publication occurrence; `A.10` supplies source-to-use evidence/provenance paths and bounded reliance, `G.6` supplies addressable path citation, slicing, and local refresh, and `G.11` supplies currentness. E.17 combines only the references needed to stop a reader from mistaking an envelope or carrier for the carried claim. | A publication form may expose an exchange envelope, carrier, evidence pointer, or provenance pointer, but the source or evidence relation remains separately recoverable; focused test: removing the envelope leaves the source claim unchanged, while removing the source or evidence relation blocks only the use that relied on it. | Adopt the existing object separation and source-return discipline; reject envelope presence as semantic authority, evidence sufficiency, performed work, or gate passage. |

(External references are retained only for the payload they contribute; named local rationales are deductions from current FPF patterns rather than claims of external SoTA support. MVPK remains notation-agnostic.)

### E.17:13 - Relations
* **Architecture ADR projection boundary:** `C.32.ADR` is the architecture-specific publication projection for `ArchitectureDecisionDescription@Project`. E.17 keeps publication face, source episteme, carrier, scope, and downstream typed value separate for the broader MVPK claim.
  In that name, `@Project` is a compatibility and retrieval cue only. E.17 infers no project entity, composite-work identity, context, authority, viewpoint, or parthood from it; `C.30.AD` and `C.32.ADR` must identify the exact composite `U.Work` and the direct description-use or publication-use relation when project locality is current.

* **Builds on:** `C.2.1` for selected-edition identity; `E.24.PUB` for `PublicationFormExpressionRelation`, `PublicationFormBearingRelation`, and the exact publication occurrence; `E.17.0` for viewpoint and `U.View` membership; `A.22` for selected structure; `C.29` for representation; `A.7` and `E.10.D2` for carrier, front-end, EntityOfConcern, Description-episteme, and specification-use discipline; `A.6.2`-`A.6.3` for optional source-to-candidate construction; `E.8` and `E.10` for authoring and publication-language discipline; and Part F and Part G for bridge, terminology, characteristic, and pin discipline.
* **Constrains:** publication-face-emitting automation and hand-written faces. When another episteme is constructed from a source, A.6.3 supplies the separate construction relation; E.17.0 separately tests viewpoint conformance, and E.24.PUB separately identifies publication occurrence/form/carrier. Readable form creates none of those relations, nor an evidence path, gate decision, work occurrence, assurance record, release source, or bridge declaration.
* **Neighboring-pattern boundary use:** use the compact boundary aid in `E.17:5.1d` when a publication-facing unit starts carrying work, reliance, evidence, assurance, gate, release, bridge, explanation, comparison, retargeting, carrier, or front-end claims beyond ordinary publication use. This Relations section cites that aid instead of repeating the whole map.
* **Part F bridge wording boundary:** when the publication face uses or invites "same", "equivalent", "align", "map", substitutable, interchangeable, attribute, entity, or profile matching, or other Bridge-wording pressure across contexts, use Part F and `A.6.9` to repair the wording. Use F.9 for the Bridge and bounded-use claim, and F.9.1 only for a separate optional stance note about that claim. Neither object follows from a publication face, and no local Bridge taxonomy is introduced here.
* **Coordinates with:** `C.2.P` for exact source-expression and source-to-use recovery before publication-facing wording is relied on; `A.15.4` for appearance-based reliance repair; C-cluster selection or archive patterns when separately constructed epistemes are selected or retained; CHR and UNM for measurement and normalization semantics; F.9 for exact Bridge occurrences, bounded-use claims, optional `CL`, evidence and loss boundaries, and optional Cards; F.9.1 for separate optional stance epistemes; and `A.6.9` for sameness wording. Publication faces remain publication forms; their bounded-use declarations, selected or receiving epistemes, occurrences, and carriers remain separate, and face status never establishes `U.View` membership.

### E.17:14 - Minimal authoring template (Part E)

**Ordinary publication**

* **Current source/account:** `<recoverable source and edition or current subject>`
* **Reader and use:** `<who needs what understanding or action>`
* **Minimal publication-form set (MVPK faces):** `<one or only the needed forms>`
* **Bounded-use declaration for each form:** `<reader, permitted use, and blocked stronger use>`
* **Preserved and omitted:** `<claims retained; material omissions or narrowing>`
* **Return to source:** `<where the reader checks or reopens the source>`
* **Stop:** `<why no additional face or apparatus changes this use>`

**Add only when triggered:** exact `publicationViewpointRef` and E.17.0 conformance for a material `U.View` claim; exact `U.PublicationScope`; E.24.PUB occurrence/form/carrier identities; pins; F.9 Bridge and bounded-use claim; selected `ReferencePlane` and applicable transfer or comparison rule; provenance, evidence, gate, release, or assurance references for the concrete receiving use.

**Optional morphism profile:** declare `F_face` and the exact source morphism; use `Emit_s` and `PromoteFace` witnesses only for faces that claim compositional publication.

### E.17:15 - Manager’s one‑page review (copy‑paste)

> We publish only the publication forms current readers need, each tied to the same recoverable source and a separate bounded-use declaration, with material omissions visible and no added claims. A selected episteme exposed through a face is a `U.View` only through E.17.0 conformance; publication occurrence, form, carrier, work, evidence, gate, assurance, and release remain separate. Exact identities and formal witnesses appear only when the receiving use depends on them.

### E.17:End

