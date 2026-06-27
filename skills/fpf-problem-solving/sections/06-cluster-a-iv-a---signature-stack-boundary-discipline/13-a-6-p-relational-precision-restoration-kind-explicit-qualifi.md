## A.6.P — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (Core)

**Plain-name.** Relational precision restoration.

**Intent.** Provide a reusable governing discipline for repairing a recurring defect in FPF texts: **under-specified relational language** (often phrased as a seemingly binary verb) that actually hides **(i)** higher arity (missing participant positions), **(ii)** multiple semantic change classes, **(iii)** asymmetry between `U.Viewpoint` specifications and `U.View` instances, **(iv)** boundary requirements such as signature invariants, admissibility, deontics, evidence, or work, and **(v)** endpoint referential compression through pronominal stand-ins, metonymic stand-ins, or over-broad kinds.
RPR patterns turn “umbrella relations” into **kind‑explicit, slot‑explicit, qualified relation records** with an explicit **change-class lexicon** and **lexical guardrails**, while respecting the **A.6 Signature Stack** and **A.6.B Boundary Norm Square** separation.

**Use this when.** Use `A.6.P` when wording hides a relation-bearing use: sameness, linkage, grounding, support, basedness, mapping, comparison, dependency, whole or part, service, cross-context bridge wording, endpoint compression, qualifier-carried claim, or another relation-bearing phrase that must be used for FPF guidance, publication, comparison, gating, assurance, decision, or reuse.

**What goes wrong if missed.** An umbrella verb or noun starts acting like a relation ontology: endpoints, slot kinds, direction, scope, time, admissible use, and neighboring governing patterns disappear behind a familiar phrase.

**What this buys.** The relation becomes reviewable: head kind, endpoints, slots, qualifiers, scope, time, viewpoint, admissible use, non-admissible overread, and relation record are made explicit enough for the neighboring FPF pattern governing that claim to compose with it.

**First useful move.** Restore the head kind and the relation or comparison use separately. If the problem is only source-expression, publication, architecture or structure, characteristic or scale, quality characterization, evaluative characterization, or function-like kind recovery, use the pattern governing the recovered claim named below instead of forcing relation repair.

**Not this pattern when.** Do not use `A.6.P` as a universal wording-repair pattern, evidence pattern, assurance pattern, quality pattern, source-use pattern, or architecture pattern. If `E.10` already recovered the pattern governing the recovered claim, kind, or relation, use that governing pattern directly.

**Placement.** Part A → cluster **A.6 Signature Stack & Boundary Discipline** → governing pattern for **RPR specialisations** (A.6.5, A.6.6, A.6.8, A.6.9, A.6.H, and any additional A.6.x pattern that declares this RPR relation).

**Builds on.**

* **A.6** (stack layering + boundary discipline requirements).
* **A.6.B `U.BoundaryNormSquare`** (L, A, D, and E classification; claim atomicity; cross-quadrant references).
* **A.6.S `U.SignatureEngineeringPair`** (TargetSignature vs ConstructorSignature; canonical constructor verb mapping; effect‑free constructor ops).
* **A.6.0 `U.Signature`** (SlotSpec requirement for argument positions).
* **A.6.5 `U.RelationSlotDiscipline`** (SlotKind, ValueKind, and RefKind stratification + canonical slot verbs; `bind` reserved for name binding).
* **A.6.RSIR** (interface cue, signature, role, slot, and relation precision restoration; selects the governing interface-like case before generic RPR is allowed).

* **E.8** (pattern authoring discipline; Tell–Show–Show; SoTA echoing hygiene).
* **F.18** (local-first reusable naming after relation kind and use recovery: minting decisions, reuse decisions, externally fixed name documentation decisions, collision checks, lineage notes, and durable-name discipline).
* **E.10** (LEX‑BUNDLE discipline; EntityOfConcern versus Description epistemes and specification-use cases plus publication face, form, unit, carrier, and rendering discipline; publication-face or publication-form token discipline; reserved primitives; Tech↔Plain pairing). *(Referenced conceptually; no extra authoring apparatus implied.)*

**Coordinates with.**

* **A.10, B.3, F.10, and E.17 evidence, status, and source-use discipline** (carrier-referenced evidence use, assurance use, status-source use, publication use, timespan, and freshness when decision-relevant).
* **A.2.6 scope + `Γ_time` discipline** (avoid implicit “current” or “latest”; make time selectors explicit when time matters).
* **A.7 Strict Distinction** (EntityOfConcern, Description episteme, specification use, publication face, form, unit, carrier, and rendering; avoid treating evidence or logs as properties of prose).
* **A.6.2–A.6.4** (effect‑free episteme morphisms, epistemic viewing and retargeting as disciplined slot writes).
* **A.10 evidence discipline** (witnesses are carrier-referenced; freshness is adjudicated in work and evidence relations).
* **C.2.1 `U.EpistemeSlotRelation`** (slot read and write profiles for constructor operators, when declared).
* **C.3.3 `U.KindBridge` + `CL^k` discipline** (repairing endpoint kind mismatches; kind-level congruence + loss notes).
* **E.17 MVPK and multi-view publication** (faces are views; "no new semantics"; viewpoint accountability).

* **F.17 `UTS`** (when ambiguity clusters become recurring vocabulary: publish stable `RelationKind` tokens and facet head phrases as UTS and LEX-UTS term assets, so rewrites do not live only inside A-patterns).
* **F.9 Bridges + CL** for cross-Context or cross-plane reuse (no silent sameness).
* **C.2.2a, A.16, A.16.1, A.16.2, B.4.1, and B.5.2.0** for the language-state boundary: language-state chart positions, admissible moves, pre-threshold cue preservation, next-pattern publication, admissible retreat or reopen, and prompt-shaped continuations that are not yet stable relation publication; use **A.16.0** only when lineage, branch, loss, or responsibility-transfer history itself must be published as an explicit trajectory account.
* **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for language-state facet governance: articulation explicitness, closure degree, language-state anchoring mode, and the language-state representation-factor bundle may be cited by RPR patterns but are not governed here.

**Specialisations already in Core.**
These retained specialisations are current because they each carry one stable recurring repair case. Their mnemonic heads remain admissible entry points, but generic `A.6.P` does **not** treat token recurrence alone as sufficient to mint one new specialisation per overloaded trigger word.

* **A.6.5**: RPR for n-ary relations and slot discipline (archetype: "putting something into a place"; explicit SlotKinds, ValueKind, RefKind, and slot-operation lexicon).
* **A.6.6**: RPR for relative-to and basedness claims (explicit `baseRelation` token, scoped witnessed base declarations, and base-change lexicon; lexical red-flags for `anchor*`; support-as-basedness selection test for `support`, `supported by`, `support basis`, and `support relation` wording).
* **A.6.8 (RPR-SERV)**: RPR for the "service" cluster polysemy (facet-explicit `serviceSituation` lens; canonical rewrites for `service`, `server`, and `service provider`; classification tests for clause, access point, provider commitment, work, and evidence).
* **A.6.9 (RPR-XCTX)**: RPR for cross-Context "same", "equivalent", "align", or "map" talk (explicit Bridges with direction, endpoint refinement, substitution licence, CL, and loss notes; blocks silent inversion and "alignment" umbrella verbs).
* **A.6.H (RPR-WHOLE)**: RPR for "whole", "part", "integrity", and "complete" polysemy (WHOL triggers plus Boundary-Parthood-Fold-Order-Time-Completeness lens; maps turnkey and end-to-end wording into A.15 coverage; includes publication-form, referent, and work-level tests).

### A.6.P:0 — TERM and LEX token guards (local-first)

This pattern reserves the following tokens in Tech and normative prose:

* **RPR** — *Relational Precision Restoration* (the governing repair discipline; not a durable U-kind).
* **RelationKind** — a Context-local vocabulary token (signature-level) that fixes polarity and SlotSpecs for participant and qualifier positions. It is a *registry entry token*, not a relation instance.
* **QualifiedRelationRecord** — the slot-explicit relation instance record kind (Context-local episteme or record kind); instances carry a `relationKind` token reference plus explicit participant and qualifier slots.

**Mint-or-reuse note (pattern-level).** This pattern mints the label **RPR**, the role name **RelationKind**, and the generic shape name **QualifiedRelationRecord** as local-first terms for relation precision restoration. It reuses existing FPF terms (`U.Signature`, SlotKind, ValueKind, RefKind, Bridges, CL, `U.Scope`, `Γ_time`, `U.View`, `U.Viewpoint`, evidence pins, and carriers) without changing their meanings.

**Definitions (pattern-level; non-deontic).**

* **RelationKind token** — a declared vocabulary element (signature-level) whose public definition fixes polarity and SlotSpecs for participant and qualifier positions, and that is referenced by L, A, D, and E-classified claims that govern admissibility, duties, commitments, evidence, and work.
* **QualifiedRelationRecord** — a Context-local episteme or record kind whose `relationKind` field points (by ID or reference) to a RelationKind token and whose instance records make all relation-specification-required participant and qualifier slots explicit.

Rename-guards (common collisions):

* **agreement-like boundary wording** — Plain shorthand for a published boundary-interface description; a conforming text MUST NOT treat such wording as itself establishing a promise or obligation. Promises, duties, and gates are classified under `A.6.B`.
* **bind and binding** — reserved for **name binding** (Identifier to SlotKind or slot instance) and MUST NOT be used as a synonym for relation instance edits.
* **same, synced, linked, connected, anchored, grounded, supported, and supporting** — treated as umbrella tokens; allowed as Plain gloss only when immediately mapped to an explicit RelationKind token (Tech) or to an claim kind governed by an FPF pattern named by value or admissible-use boundary via rewrite rules.

### A.6.P:1 — Problem frame

FPF repeatedly encounters a predictable precision failure mode:

Authors describe a situation with an apparently simple relational phrase:

* “X **is the same as** Y”, “X **is linked to** Y”, “X **is synced with** Y”
* “X **depends on** Y”, “X **is grounded or anchored** in Y”
* “X **maps to** Y”, “X **aligns with** Y”, “X **is connected to** Y”
* “X **supports** Y”, “X is **supported by** Y”, “X gives **support for** Y”

…but the intended meaning is actually:

1. **Hidden multiarity.** The claim requires additional participant positions: scope, time selector, witness carriers, policy, direction or inverse, reference scheme, representation scheme, mediator publication form, or mediator carrier.
2. **Kind elision.** The umbrella verb stands in for an unstated set of relation kinds (different invariants; different admissibility; different evidence, source, or authority requirements).
3. **Viewpoint fights.** Different stakeholders describe “the same” relation from incompatible viewpoints, creating polarity flips and silent re‑typing.
4. **Unnameable change semantics.** Authors say “update, bind, anchor, or sync”, but mean distinct semantic change classes (retarget vs revise vs rescope vs retime vs witness refresh).
5. **Regression via prose.** Even after ontology repairs, umbrella language re‑enters and collapses distinctions unless structural precision is coupled to lexical guardrails.
6. **Pronominal and metonymic endpoints.** Even when the relation verb is fixed, endpoints may be referred to via pronoun‑like or umbrella tokens (or metonymic pointers), so the relation cannot be typed or audited until endpoint facets and endpoint kinds are restored from context.

A.6.P defines a **repeatable precision restoration recipe** that makes this defect repairable and reusable across additional admitted A.6.x patterns.

### A.6.P:2 — Problem

How can FPF represent and evolve “relations in prose” that are structurally richer than they appear, so that:

* the **relation kind** is explicit and reviewable,
* missing positions can be made explicit **without semantic drift**,
* changes to the relation can be narrated with **stable semantic change classes**,
* multi‑view publication can exist **without creating multiple incompatible relation specifications**, and
* cross-Context or cross-plane reuse cannot silently assume “sameness by label”?

### A.6.P:3 — Forces

| Force                                 | Tension                                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Universality vs precision             | The repair must be reusable across domains, but must not hide the distinctions it is meant to recover. |
| Prose convenience vs relation-specification clarity | Humans want short verbs; engineering and assurance needs declared kinds, slots, and invariants.            |
| Kernel minimality vs safety           | Few primitives are good; umbrella relations are cross‑Context safety hazards.                          |
| Multi‑view reality vs coherence       | Viewpoints must be expressible without silent polarity flips or re‑typing.                             |
| Evolution vs auditability             | Relations change; edits must not rewrite meaning invisibly.                                            |
| Stack discipline                      | Signature invariants, admissibility, deontics, and evidence and work must not be mixed (A.6 + A.6.B).                      |

### A.6.P:4 — Solution — The RPR recipe (Lens → Slots → Change Lexicon → Guardrails), aligned to A.6 / A.6.B / A.6.S

A.6.P defines the **RPR specialisation envelope**. A pattern is a **RPR specialisation under A.6.P** iff it provides the ingredients below.

#### A.6.P:4.0 - Admission rule after lexical trigger scan

`A.6.P` is not the first post-authoring check for conformant FPF pattern text and not an all-purpose trigger-word registry. In conformant FPF text, `E.10` carries the lexical trigger scan. When that scan selects `epistemic precision restoration required`, `C.2.P` supplies the epistemic precision-restoration profile for pattern prose and FPF-facing publication prose. `A.6.P` is applicable when the `E.10` scan has selected relation precision, endpoint recovery, support-like claim-kind discrimination, basedness, cross-context bridge wording, or another RPR repair case.

For non-FPF intake, source, review, project, or tool-output prose, `A.6.P` may still be used directly as a repair method once a reader has recognized a relation-bearing use. That use produces a repaired FPF phrase, candidate-set note, relation record, or transfer disposition. It does not make the source text itself non-conformant FPF text and does not require the source text to be rewritten.

A relation mention or relation-bearing phrase is in-scope for `A.6.P` when **any** of the following holds:

* the predicate or verb phrase has been selected as overloaded relation wording, such as sameness, connection, grounding, dependency, support-like, source-to-EntityOfConcern, or cross-context bridge wording;
* one or more endpoints or qualifiers are expressed via **pronominal, deictic, or metonymic stand-ins** or **over-broad kind tokens** such that multiple referents or facets remain plausible;
* a **generic or over-broad head noun** carries its semantic work only through a qualifier, modifier, or surrounding phrase, so the object kind is still ambiguous even though the qualifier sounds informative;
* the statement implicitly relies on **scope, Γ_time, viewpoint or view, or reference or representation schemes**;
* the relation is used for **assurance, admissibility, gating, or publication** decisions;
* the relation crosses **Contexts or planes** and therefore requires Bridge and CL discipline rather than silent equivalence;
* different stakeholders interpret endpoints differently, creating multi-view asymmetry or polarity fights.

**Repair order note.** When a FPF-governed phrase is triggered because its **head noun** is too generic, first restore what kind of thing the head actually names: record, carrier, interpretive claim kind or admissible-use boundary, process, A.7 position, authority use, or another local kind with named authority-reference relation. Use local EntityOfConcern and claim-target discipline (`E.10`, `A.7`, and nearby authority-reference guidance). A narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` may narrow the phrase, but it does **not** by itself restore the head kind. Then apply A.6.P to restore the remaining relation or comparison reading. Mixed-kind comparison checks come **after** those two repairs, not before them.

**Adoption test (reader heuristic).** If a reader can reasonably ask any of: “Which kind is this?”, “What exactly does this span refer to (which facet or kind, and which A.7 position: EntityOfConcern, Description episteme, or publication carrier)?”, “What relation or comparison reading is hidden in this qualifier?”, “What else participates?”, “Under what scope, time, or view?”, “What changed?”, or “What makes this admissible?”, then authors SHOULD treat the mention as in-scope and rewrite it into explicit kind-and-slots form before using it for cross-Context reuse or decision or publication claims.

**Precision and relaxation note.** A.6.P is not a blanket demand that every sentence stay maximally explicit forever. It is a trigger-based repair discipline for **FPF-governed** prose. In design-time FPF texts and in run-time texts being prepared for admissible publication, review, gating, or reuse, the repair should be performed before any later didactic plain-language softening or admissible coarsening. Later relaxation is allowed only when the more precise upstream repair remains recoverable and authoritative.

**Generic trigger-word governance rule (normative).** Overloaded words are diagnostic entry points, not default governing FPF patterns or `authoritySourceRef` targets. Generic `A.6.P` therefore requires this order: restore head kind first, restore the remaining relation or comparison reading second, and only then judge whether one reusable repair-case specialisation is justified. A new `A.6.P` specialization or broader trigger-word governing FPF pattern or `authoritySourceRef` target is owed only when one stable recurring repair case, one reusable lens or rewrite kit, and one `F.18 -> A.6.P`-surviving head already exist by value across more than one worked case. Otherwise token-specific retained knowledge stays with an existing admissible specialization or in one cluster-local / source-local note rather than expanding generic `A.6.P` into a token bucket store.

**Interface cue selection rule (normative).** Bare `interface`, `port`, `API`, `protocol`, or service-access wording is not a recovered relation kind and does not mint `U.Interface`. First recover the direct EntityOfConcern: module or architecture boundary, functional port, signature, service-access protocol, description or publication interface, or plain source label. Use `A.6.RSIR` for the recovery map; continue in `A.6.P` only when the selected case is a relation-precision restoration case requiring a `RelationKind` token and qualified relation slots.


**Replacement-candidate anti-umbrella rule (normative).** When an RPR repair selects a replacement term, apply the shared `E.10:0.2` replacement-candidate anti-umbrella rule before accepting the term. Then run the candidate through the local A.6.P recovery: name the FPF kind or local field it denotes, the A.7 position, the participant, carrier, view, or EntityOfConcern positions, the relation or publication function if any, and the admissible and non-admissible use. If those cannot be named, keep the line in Candidate-Set Note form rather than treating the new term as repaired.

**Support precision restoration rule (normative).** `support`, `supported`, `supporting`, `support-looking`, and support-headed compounds are diagnostic tokens, not one recovered relation kind, not one generic record kind, not one universal evidence verdict, not one universal source relation, and not one universal reason container. Before an in-scope support phrase is used for publication, comparison, reliance, gate, assurance, decision, work, cross-context reuse, pattern-quality claims, or architecture claims, first recover the support-like claim kind or admissible-use boundary under the full A.6.P repair sequence: head kind, A.7 position, candidate endpoints, EntityOfConcern or grounding holon when live, relation kind, qualifiers, admissible use, and governing ontology named by value or governing pattern when the selected support-like case is not an A.6.P relation. If the selected support-like case is base-dependence, apply A.6.6 ontology and state `dependent`, `base`, `baseRelation`, `scope`, `Γ_time` when live, witnesses when decision, publication, or admissibility use is live, `admissibleUse`, and `nonAdmissibleUse`; do not mint a generic `SupportRelation`, `SupportBasis`, or `SupportRecord`.

**Support-like claim-kind discrimination.** A conforming repair does not ask only "what more precise word can replace support?" It asks which support-like claim kind or admissible-use boundary is live:

| Live support-like claim kind or admissible-use boundary | What must be named | Governing ontology to apply |
| --- | --- | --- |
| **Source-to-EntityOfConcern description relation.** A source episteme, publication, view, document, model, diagram, graph, trace, or generated representation is being used to describe, expose, render, cite, or make inspectable one claim-bearing EntityOfConcern. | source episteme, publication, view, or carrier where relevant, EntityOfConcern, publication or view relation, source pins or source-return condition, admissible and non-admissible use. | `E.17`, `E.17.0`, `A.6.3.RT`, `A.7`, and local publication and source rules. |
| **EntityOfConcern or grounding-holon contact.** The phrase says that a claim-bearing episteme, view, representation, or pattern application is grounded in the EntityOfConcern it concerns, the situation it is about, the observation setting, or the local world contact needed for the claim. | `EntityOfConcernSlot`, `GroundingHolonSlot` when grounding-holon grounding is being claimed, bounded context, reference plane, reference scheme, viewpoint, witness or observation condition if needed. | `C.2.1`, `A.6.4`, `A.6.3.RT`, `C.2.6`, `A.7`, and evidence or observation patterns governing world-contact claims when world contact is live. |
| **Base, anchor, or basedness relation.** The phrase means relative-to, based-on, anchored-in, base change, dependency on a base, or local grounding as a base relation rather than a source or document relation. Support wording belongs here only when a dependent content is usable, admissible, interpretable, comparable, publishable, or actionable relative to an explicit base. | `dependent`, `base`, declared `baseRelation` token, scoped witnessed base declaration, `Γ_time` when live, witnesses when decision, publication, or admissibility use is live, base-change condition, admissible and non-admissible use. | `A.6.6`; use its support wording selection test and SWBD discipline. |
| **Evidence or witness support.** The phrase says a carrier, observation, test, role assignment, or evidence path bears on a claim. | evidence-use or witness relation, evidence path when path-addressable, claim ref, witness carrier, timespan and freshness, and any governing-pattern field named by value when the direct evidence, assurance, status, source, or publication pattern defines one. | `A.10`, `B.3`, `G.6`, `F.10`, `E.17`, and any direct evidence, status, source, or publication pattern named by value. |
| **Assurance or engineering-justification support.** The phrase says a claim is acceptable for assurance, safety, trust, engineering justification, or assurance calculus use. | assurance claim, argument component, confidence or trust calculus input, cited evidence path, non-admissible claim escalation. | `B.3` plus the evidence pattern governing the claim when an assurance or evidence claim is live. |
| **Causal-use support.** The phrase says a causal, intervention, counterfactual, policy, off-policy, or simulation-only use is admissible. | causal-use question, `CausalityLadderRung`, estimand, `CausalEvidenceSupportBasis`, `CausalUseSupportVerdict`, supported and unsupported use. | `C.28`; do not substitute A.6.P or A.10 value sets for the C.28 causal-use vocabulary. |
| **Mathematical-lens use result.** The phrase says a lens, model, mapping, similarity, or formal construction makes a claim admissible or exposes preserved and lost structure. | lens candidate, lens-use card, primary `EntityOfConcern` or relation record or claim record named by value, preserved and lost structure, declared loss, stop condition, lens-use result, lens-use admissibility value, and the non-lens claim-kind pattern governing the claim when evidence, causal, assurance, decision, or publication claim kind or admissible-use boundary is live. | `C.29`, `C.26`, `F.9`, `A.6.3.RT`, or a named mathematical-lens pattern. |
| **Characteristic, measurement, threshold, or comparison reference.** The phrase says a characteristic, metric, score, threshold, benchmark, or comparison warrants a claim. | bearer, characteristic space, scale, measure, measurement procedure, comparison reference set, threshold rule, proxy-distortion risk. | `C.16`, `A.17`-`A.19`, `C.25`, `G.9`, and the bridge or comparison pattern governing the characteristic, measurement, threshold, benchmark, or comparison claim being made. |
| **Admissible-use or boundary-use rule.** The phrase says a current use, publication use, project action, work preparation, gate use, or downstream reliance is allowed. | `admissibleUse` target named by value, non-admissible claim escalation or adjacent use, L, A, D, and E split when boundary-use reading is being made, project-side kind or reference if needed. | `A.6.B`, `E.17:5.1c`, `C.2.P`, and project-side pattern governing the claim. |
| **Work, enablement, prerequisite, resource, or operational help.** The phrase says one thing helps, enables, prepares, funds, resources, scaffolds, directs, or makes work easier, without claiming evidence, authority, truth, or admissibility. | enabled work and method or action, prerequisite or resource relation if FPF-governed, remaining reader use, explicit non-admissible evidence, gate, assurance, or decision use. | `A.15`, `A.15.4`, `A.6.A`, `C.11`, or Plain orientation when no FPF-governed use is live. |
| **Publication companion, entry, navigation, or reader help.** The phrase says one publication unit, section, README scenario, ToC query cue, expanded entry-disambiguation case, review packet, companion document, or reader aid helps readers find, inspect, compare, or review another EntityOfConcern. | publication unit or companion-publication kind, entry-distribution locus, reader function, publication or episteme being found, inspected, or reviewed, source-description relation, evidence path, architecture or structure relation, or review relation when that relation is being made; no downstream authority unless separately named. | `E.17`, `E.11`, `I.2`, `C.2.P`, and the governing pattern if action guidance becomes FPF-governed. |

If no support-like claim kind or admissible-use boundary can be selected from the current claim context, the phrase remains ordinary help, orientation, source-finding, quote-only wording, reduced-use cue, or blocked current transfer. A support-headed name such as `SupportRecord`, `support source`, `support relation`, `support line`, `support basis`, a support phrase that hides a state-family claim, `support view`, or `supported use` is a diagnostic trigger; it is conforming only when rewritten to a locally governed record, field, relation, admissible-use boundary, or, for the A.19 case, `DeclaredSubstrateInterpretiveView` under `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`. When the selected support-like case is base-dependence, the conforming form is A.6.6 SWBD or a Context-local SWBD specialization with explicit `baseRelation(dependent, base)`, not a generic support-headed type. Otherwise, use the selected row above and name the relation named by value, slot, field, source-use relation, evidence path, grounding, or governing pattern ontology for that support-like case.

#### A.6.P:4.0r - Relation realization of `E.10.ARCH`

`A.6.P` is the relation-construction realization of the shared wording-use recovery order in `E.10.ARCH`.
When `E.10` selects relation-like repair case, endpoint recovery, support-like claim-kind discrimination, basedness, cross-context bridge wording, whole or part wording, mapping, comparison, dependency, service wording, or another RPR repair case, `A.6.P:4.0a` supplies the relation-specific recovery sequence: head kind, candidate endpoints and facets, relation kind, slots, qualifiers, admissible use, non-admissible overread, and relation record or fail-closed disposition.

This pattern does not become the parent for every wording-use precision-restoration problem. Source-expression, publication, carrier, face, `PublicationUnit`, and source-use wording use `C.2.P` when that stack is live. Architecture or structure wording whose selected structure, architecture relation, architecture-description use, structural-view use, or source-use relation is hidden uses `C.30.P`. Characteristic, scale, score, metric, indicator, threshold, comparison, or scalar-quality wording whose construction is hidden uses `C.16.P`. Quality or evaluative characterization uses `C.16.Q`, `C.25`, `E.21`, or another characterization pattern governing the claim unless the found problem is relation construction. Function-like wording whose FPF kind named by value, relation, or claim is hidden uses `A.6.F` first.

The old quality-term precision-restoration placement is not retained as a live `A.6.P` child after `C.16.Q` exists. `A.6.P` remains applicable for relation-shaped entry cases inside quality prose, such as bridge, basedness, comparison, action-invitation relation, or endpoint mismatch; it does not carry quality characterization or evaluative characterization as a relation by default.

#### A.6.P:4.0 - Language-state entry note

RPR entry normally presupposes enough `C.2.4` articulation explicitness that at least one relation-like skeleton can be named explicitly, and often enough `C.2.5` closure that one candidate relation-bearing use is worth publishing as a relation record rather than remaining cue-pack material.

If the content is still best treated as a cue pack, `RoutedCueSet`, or unresolved cue content, keep it in `A.16.1` / `B.4.1` rather than forcing relation publication prematurely. If the admissible continuation is still an open explanatory question, apply `B.5.2.0`. If a previously published relation must be reopened or backed off because the articulation or closure record no longer holds, apply `A.16.2` for that retreat rather than silently narrowing the published relation in place.

#### A.6.P:4.0a — Operational repair sequence (how repairs actually proceed)

The RPR specialisation envelope is presented as **lens → slots → change lexicon → guardrails** because the *stable abstraction* is what keeps repairs reusable. In actual editing, repairs often start from a **triggering token** and proceed through a context-reconstruction step.

Operationally, authors SHOULD follow this repair sequence when applying an RPR repair:

0. **Restore the head kind if needed.** If the triggering phrase uses a generic or over-broad head noun (`note`, `view`, `guidance`, `output`, `record`, `carrier`, and similar placeholders), first state what kind of thing it actually is in source-local terms (publication form, interpretive claim kind or admissible-use boundary, process, authority use, and so on). Do not let a qualifier do this job by implication alone.
1. **Trigger on textual form.** Detect umbrella relation predicates, pronominal or umbrella endpoint tokens or metonymic pointers, and generic-head-plus-FPF-governed-qualifier combinations (including domain clusters such as **service** in A.6.8 and cross-Context “same, equivalent, align, or map” in A.6.9).
When endpoint identity (pronoun, deixis, metonymy, or coarse kind) or relation-kind selection is ambiguous, repairs can collapse into “lexicon debates”. A.6.P treats this as an ontology reconstruction step with an explicit, checkable intermediate record.
3. **Choose a stable lens** that can represent the reconstructed arity and polarity without ad-hoc role invention.
4. **Refine the ontology under the lens.** Turn implied relation positions into SlotSpecs; repair endpoint kind mismatches explicitly through narrowing, `KindBridge`, or `retargetParticipant`; separate head kind, relation-bearing use, and qualifier-carried claim; make qualifiers explicit as slots or classified conditions.
5. **Emit canonical rewrites plus L, A, D, and E hooks.** Produce Tech-form rewrites such as `relationKind(...)` or arrow form and state the A.6.B hooks: which parts are L, A, D, or E, and which witnesses, commitments, or work claims are now demanded.
6. **Only then allow later relaxation.** If a Plain, didactic, or coarsened restatement is still wanted, derive it from the repaired form and keep the repaired form as the authoritative source for any later use that claims bridge, substitution, or reliance beyond the declared note.

**Decision or publication fail-closed (normative).** If an in-scope mention is used to justify an admissibility gate, publication claim, or cross-Context reuse, authors MUST resolve the candidate sets to a selected `RelationKind`, selected endpoint facets and endpoint kinds, and any required head-kind reconstruction and emit an explicit rewrite. If that cannot be done from available context and witnesses, keep the statement as Plain or informative gloss (or split into multiple explicit alternatives) and do not treat it as admissible input for the gate.

**Informative: referential compression spectrum.** Many triggers live on a spectrum from high to low referential precision:
pronouns and deictics → overloaded polysemes → coarse domain kinds → facet head phrases → precise domain terms.
Metonymy often shifts the candidate EntityOfConcern or endpoint (e.g., a place phrase standing in for an object or a role). The repair sequence explicitly treats this as a **candidate-set** problem, not as “the dictionary meaning”.

**Metonymy micro-example (informative; endpoint-side trigger beyond anaphora).**

Draft: “Alice is **at the table**.”

`at the table` → candidates `{place, meeting, record or carrier, role}` → choose explicitly → rewrite into endpoint-refs + qualifiers:

```
CandidateSetNote(triggerSpan="at the table", position=endpointFacet(p₂)):
- candidates: {PlaceRef(Table#7), MeetingRef(NegotiationSession#3), RecordRef(AgendaDoc#12), RoleRef(DecisionMakerSeat#2)}
- selected:   MeetingRef(NegotiationSession#3) + RoleRef(DecisionMakerSeat#2)  // metonymy: place → meeting or role
- consequence: require explicit `meetingRef`, `roleRef`, `Γ_time`, `witnesses` (and apply A.6.B separately for decision or admissibility)

participatesInMeetingUnder(
  personRef  = PersonRef(Alice),
  meetingRef = MeetingRef(NegotiationSession#3),
  roleRef    = RoleRef(DecisionMakerSeat#2),
  Γ_time     = snapshot(t),
  witnesses  = {attendanceLogPins}
)
```

If the literal location interpretation is intended, select `PlaceRef(Table#7)` and rewrite as `locatedAt(…)` with an explicit `Γ_time` qualifier.

This step is intentionally **not lexicon-only**. The lexical rewrite is the *output* of an ontology- and lens-constrained repair, not the starting point. If you cannot state the candidate referents and facets, the selected head kind where needed, and the selected `RelationKind` token, the repair is incomplete.

#### A.6.P:4.0b — Candidate‑Set Note (informative; repair/disambiguation record)

When endpoint identity (pronoun, deixis, metonymy, or coarse kind) or relation-kind selection is ambiguous, reviews can collapse into “lexicon debates”. A.6.P treats this as an ontology reconstruction step with an explicit, checkable intermediate record.

**Candidate‑Set Note template (informative).**

> **Collision note.** This “Candidate‑Set Note” is **not** the F.18 naming-process *candidate set* (NQD-front). It is a local disambiguation record for endpoint referents and facets and RelationKind selection during RPR repairs.

For each ambiguous position (relation kind, endpoint facet or kind, qualifier, mediator), record:

* **Trigger span:** the trigger token named by value(s) in the draft (copied by value).
* **Position being disambiguated:** `headKind` | `relationKind` | `endpointFacet(pᵢ)` | `endpointRef(pᵢ)` | `qualifier(qⱼ)` | `mediator`.
* **A.7 side (when endpoint-side):** `EntityOfConcern` | Description episteme | publication carrier (state explicitly when live contenders span sides; side-mixing is a common source of boundary-interface category errors).
* **Candidate set:** a short list of plausible **head kinds**, **endpoint facets or endpoint kinds**, and **RelationKind tokens** when relation-kind selection is live, each with the local cue(s) that made it plausible.
* **Selected facet or kind (and selected RelationKind, if relevant):** the chosen candidate(s).
* **Why:** the discriminating test(s) that were applied, plus pointers to the specific local evidence and witness cues used (carriers, claims, records, or carrier records).
* **Consequence:** which SlotSpecs become required or forbidden and which A.6.B hooks are now triggered (L, A, D, and E).

Minimal one‑screen representation:

| Candidates (kinds, facets, or tokens) | Selected facet or kind | Why (tests and cues) | Consequence (slots plus L, A, D, and E hooks) |
| --- | --- | --- | --- |
| C1 …; C2 …; C3 … | … | … | … |

**Notes.**

* For **metonymy**, list both the literal candidate and the intended endpoint candidate (and make the shift explicit).
* Keep the candidate set small: include only live contenders, and state the elimination test for the others.
* This note is **informative**: it does not replace classified L, A, D, and E claims. It exists to prevent "lexicon instead of ontology".

#### A.6.P:4.1 — Stable lens

A RPR‑pattern SHALL name a stable mathematical “lens” that prevents re‑inventing roles per domain. Examples of lenses (illustrative):

* **Kind-labelled qualified relation record** (default A.6.P lens)
* **n‑ary relation with distinguished positions** (A.6.5 style)
* **kind‑labelled dependence arrow over a base** (A.6.6 style)
* **span and cospan + declared loss and correspondence notes** (Bridge‑like relation patterns)
* **correspondence relation + repair operations** (sync and consistency relation patterns)

The lens is a compression device: one stable abstraction that keeps the relation’s **arity and polarity** stable and makes invariants speakable.

#### A.6.P:4.2 — Kind‑explicit relation tokens (no umbrella meaning‑surrogates)

For every in‑scope relational claim, authors SHALL select (or mint) an explicit **RelationKind token** as a declared vocabulary element.

A RelationKind token is authored as a `U.Signature`‑level vocabulary element with explicit SlotSpecs for its participant and qualifier positions (`⟨SlotKind, ValueKind, refMode⟩`). When no suitable token already exists, authors SHALL NOT improvise a one-off string by intuition. They SHALL use **F.18** for mint-or-reuse: use **MintNew** by default, build a seed candidate set, show an honest NQD-front, run the sense-seed read-through, and record why the selected token is chosen from the non-dominated front. Use **DocumentLegacy** only when the label is externally fixed and that status is stated explicitly.

**RelationKind relation specification skeleton (minimum, recipe-level).**
For each `RelationKind` token, a conforming Context publication SHALL publish a vocabulary entry whose **signature-level definition** is paired with (or points to) an **L, A, D, and E-classified claim bundle** ("relation specification skeleton") that declares (at minimum):

The leading **(L)/(A)/(D)/(E)** tags below indicate the intended **A.6.B quadrant classification** for each element of the skeleton.

* **(L) applicability** (A.6.0): the Contexts or planes where the kind is defined (local meaning is first-class).
* **(L) polarity**, and (if needed) explicit **inverse tokens** (no silent endpoint-position flips in Tech prose).
* **(L) SlotSpecs** for all participant positions (and any qualifier slots exposed by the relation pattern) (`⟨SlotKind, ValueKind, refMode⟩`, where `refMode` is either `ByValue` or a concrete `RefKind` token per A.6.5).
* **(A) admissible repair options for endpoint kind mismatches** (normative): allowed repairs are (i) explicit narrowing, (ii) a `KindBridge` (+ `CL^k` + loss notes), (iii) explicit `retargetParticipant`, or a stated combination of these repairs when several mismatch conditions are live. Renaming endpoints is not a repair.
* **(L) qualifier expectations**: which qualifiers are required, optional, or forbidden (scope, `Γ_time`, `U.Viewpoint` and `U.View`, reference scheme, representation scheme).
* **(D) qualifier placement discipline**: extra parameters belong in `scope` or explicit qualifier slots, not as adjectives attached to endpoint names.
* **(A/E) witness discipline**: when witnesses are required as an admissibility gate and what carrier-referenced witness sets look like in this relation pattern.
* **(L/A) admissible semantic change classes** (see §4.4) and whether they require a new edition.
* **(A/E) cross-Context or cross-plane policy** when applicable (Bridge ids + CL + loss notes policy).

**Important stack constraint (A.6, A.6.S, and A.6.B).**
Treat a relation specification as a classified set of claims, not a single magical object:

* **L‑claims** (signature invariants; polarity; SlotSpec typing) live in the signature-level invariant and rule set.
* **A‑claims** (admissibility gates) are authored as admissibility predicates (canonically placed in `Mechanism.AdmissibilityConditions` when an explicit mechanism exists) and may reference the RelationKind token by ID.
* **D‑claims** (duties or commitments) name accountable role assignments, role values, or admitted acting systems and may reference `L-*`/`A-*` by ID.
* **E‑claims** (evidence or work effects) attach to carriers and observation conditions and may reference `L-*`/`A-*` by ID.

#### A.6.P:4.3 — Slot‑explicit qualified relation records (recover hidden arity)

A conforming text SHALL ensure that each in‑scope relation instance is representable as a **Qualified Relation Record** (a first-class record or episteme in the relevant Context) that fills the relation’s slots.

Conceptual notation‑neutral shape:

**Notation note (A.6.5 alignment).** In this pattern `refMode` is a slot-content mode: either `ByValue` (inline value of the declared ValueKind) or a concrete `RefKind` token (slot holds a reference or pin of that RefKind).
```
QualifiedRelationRecord :=
⟨ relationKind : RelationKind, // vocabulary token / registry entry (signature-level)

  // participant positions (pattern-specific; relation specification fixes SlotSpecs)
  p₁ : SlotContent(VK₁, refMode₁),
  …,
  pₙ : SlotContent(VKₙ, refModeₙ),

  // qualifier kit (pattern-specific; relation specification selects subset)
  scope?       : SlotContent(U.Scope, ByValue | RefKind),
  Γ_time?      : SlotContent(GammaTimePolicy, ByValue), // time selector or policy; not an evidence freshness proxy
  viewpoint?   : SlotContent(U.Viewpoint, ByValue | RefKind),
  view?        : SlotContent(U.View, ByValue | RefKind),
  refScheme?   : SlotContent(U.ReferenceScheme, ByValue | RefKind),
  reprScheme?  : SlotContent(U.RepresentationScheme, ByValue | RefKind),

  witnesses?   : SlotContent(VK_wit, ByValue | RefKind)
⟩
```

**Slot naming guard.** `*Slot` suffix names positions (SlotKinds), not fillers; prose SHOULD use filler names (`scope`, `witnesses`, `base`, `dependent`, …) for slot contents. This is the same guard used in A.6.6 and A.6.5.

**Well‑formedness principle.** The record is typed by the relation specification: SlotSpecs are fixed by the selected RelationKind token, and missing slots are permitted only if the relation specification says they are optional. This mirrors A.6.6’s scoped and witnessed declaration move (SWBD): “shape + relation specification makes a concrete typed signature”.

**Well‑formedness constraints (non‑deontic).**

* **WF‑A6P‑QR‑1 (Required slots are present).** For any QualifiedRelationRecord `r` with `r.relationKind = k`, `r` provides values for every SlotSpec that `k` marks as required.
* **WF‑A6P‑QR‑2 (No silent kind swap).** `relationKind` is part of a record’s identity and edition boundary. If the kind changes, the result is represented as a distinct record or edition linked by an explicit `changeRelationKind` (or an explicit withdrawal + re‑declaration), not as an in-place mutation that preserves identity.

**Normative prose forms (Tech).**
In Tech or normative prose, authors SHALL express an in‑scope relation instance in one of the following equivalent forms:

* **Functional form:** `relationKind(p₁=…, …, pₙ=…, qualifiers…)`
* **Arrow form (binary projection only):** `p_left --relationKind{qualifiers}--> p_right`

Passive umbrella voice (“X is synced, linked, or anchored …”) is permitted only as Plain gloss when immediately rewritten into one of the above forms.

**Cross-Context or cross-plane note (recipe-level).**
If any participant or qualifier implies cross‑Context or cross‑plane reuse, the L/A/D/E-classified claim bundle MUST cite the relevant Bridge ids + CL policy (and loss notes, when applicable) in the appropriate L/A/D/E-classified claims: A-classified claims, E-classified claims, or both when both admissibility and evidence or disclosure consequences are live. Label identity is not an admissible substitute.

#### A.6.P:4.4 — Change‑class lexicon (operations are not adjectives)

A RPR‑pattern SHALL publish a **relation‑change lexicon**: a small set of semantic change classes used in normative prose to describe “what changed” without umbrella verbs.

Minimum semantic change classes (conceptual; specialisations may add more):

1. **declareRelation** — mint a new qualified relation record (slot‑explicit).
2. **withdrawRelation** — retire a relation instance (render it inactive for downstream use). If the intent is narrowing (still valid within a smaller scope or window), use `rescope` or `retime` rather than overloading withdrawal.
3. **retargetParticipant(slotKind, newRef)** — change a RefKind slot-content while preserving SlotKind and ValueKind (conceptually corresponds to slot‑level **retarget**).
4. **reviseByValue(slotKind, newValue)** — edit embedded by‑value content (conceptually corresponds to slot‑level assign or update or “by‑value edit”).
5. **rescope(newScope)** — change scope explicitly (no “in our context” prose).
6. **retime(newΓ_time)** — change `Γ_time` when time matters; not a substitute for witness freshness claims.
7. **refreshWitnesses(newWitnessSet)** — update witness bindings to point at appropriate carriers; generating evidence is Work, not a constructor op.
8. **changeRelationKind(newRelationKindToken)** — semantic change; MUST NOT be treated as an edit‑in‑place.

**Edition fence rule (A.6.S / A.6.6 alignment).**
In decision or publication use, any semantic change that alters meaning SHALL be represented as a new edition and connected via explicit continuity and withdrawal, rather than mutating the old record in place.

**Mapping note (informative, conceptual).**
These change classes are semantic; they may be realised by A.6.5 slot verbs (retarget vs by‑value edit) and, when the relation is a basedness pattern, by A.6.6 base‑change verbs. The semantic story must not collapse into “we edited something”.

#### A.6.P:4.5 — Lexical guardrails (ban umbrella metaphors as meaning‑surrogates)

A RPR‑pattern SHALL define **red‑flag umbrella tokens** for its ambiguity cluster, and SHALL provide canonical rewrite forms.

Normative base rules (A.6.P-level):

* In **Tech or normative prose**, umbrella predicates (e.g., “same”, “synced”, “linked”, “connected”, “anchored or grounded”) MUST NOT substitute for an unnamed RelationKind token.
* **“bind” and “binding” is reserved for name binding** (Identifier → SlotKind or slot-instance) and MUST NOT be used as a synonym for declaring or changing a relation instance. Use the change‑class lexicon instead.
* Pattern-defined carve‑outs MAY exist (reserved primitives elsewhere), but they remain review triggers to ensure the reserved sense is intended (as in A.6.6’s `anchor*` carve‑out rule).

**Recommended publication move (no extra authoring apparatus implied).** For stable ambiguity clusters, publish the red‑flag token list and canonical rewrites as a LEX‑BUNDLE entry (PTG=Guarded) and, when the cluster introduces new `RelationKind` tokens or stable facet head phrases, include them in the relevant UTS rows (F.17). This keeps rewrite discipline shareable outside the A.6 cluster.

#### A.6.P:4.5a - Trigger-word repair split for discoverability vocabulary

The overloaded trigger-word repair case around `discoverability` is not collapsed into one
universal substantive pattern.
`A.6.P`, `F.18`, and `E.10` govern the repair-side trigger-word, naming, collision, and
split-classification discipline for discoverability vocabulary.

For this vocabulary repair case, apply settled governing patterns like this:

* description recognition signatures in general -> `A.6.RSIG`;
* pattern-entry discoverability -> `E.11`;
* Problem-frame recognition signatures -> `E.8`;
* expanded entry-disambiguation cases -> `I.2`;
* entry lexeme retrieval aid -> `F.17, F.18, and E.10`.

`A.6.P` therefore repairs the overloaded trigger-word side of the vocabulary.
It does not govern the substantive pattern bodies for description recognition,
pattern-entry discoverability, local recognition form, expanded entry-disambiguation
cases, or entry-lexeme retrieval aid.

#### A.6.P:4.6 — Progressive elaboration (the “precision dial” rule)

A.6.P defines a controlled escalation discipline that preserves meaning and prevents drift:

1) Start with a minimal explicit **RelationKind token** + principal endpoints (a binary projection is allowed only if every omitted participant or qualifier slot is declared optional by the relation specification *and* irrelevant for the downstream uses).

2) When ambiguity emerges, **do one (or more) explicitly**:
   * add missing participants as additional slots (turn the projection into n‑ary),
   * add explicit qualifiers: scope, `Γ_time`, viewpoint or view, reference or representation schemes, and witnesses,
   * refine the RelationKind token to a more specific one (new relation specification skeleton; `changeRelationKind`),
   * introduce Bridges + CL (and loss notes) when crossing Contexts or planes.

3) Authors MUST keep the transition monotone:
   * no silent re‑typing,
   * no implicit polarity flips,
   * no “edit‑in‑place” that changes meaning (use edition fences + explicit continuity and withdrawal links).

#### A.6.P:4.7 — Two-view and polarity discipline (no silent endpoint-position flips)

A RPR‑pattern SHALL specify how the same relation is expressed from both “sides” without polarity flips:

* Either keep both endpoints visible with the same polarity-preserving token, **or**
* declare explicit inverse tokens and require them for inverse prose.

Implicit endpoint-position flips (“B validates A” without explicit inverse) are prohibited in Tech or normative prose. This is already a core rule for basedness patterns and is generalised here.

#### A.6.P:4.8 — Disambiguation guide (rewrite and selection)

A RPR‑pattern SHALL include an actionable guide:

> “If the draft says *X*, decide between relation kinds A/B/C, expand missing slots, and rewrite into explicit kind+slots notation.”

For basedness repair, A.6.6 provides an existence proof of such a guide (select the `baseRelation` relation kind; add scope, time, and witnesses). A.6.P requires this move across RPR specialisations.

**Recommended format: RPR‑Disambiguation Guide (Winograd‑style, but ontology‑first).**
To keep disambiguation from collapsing into dictionary debates, present the guide as a compact decision scaffold:

* **trigger form** → **candidate RelationKinds and candidate facets or kinds** → **discriminating questions and tests** → **canonical rewrite(s)** → **L/A/D/E L/A/D/E hooks**

Rules for the guide:

* Triggers may be **relation umbrellas** (“same, synced, linked, or anchored…”) *or* **participant umbrellas** (pronominal, metonymic, or over-broad kind tokens). The guide SHALL state which relation position(s) the trigger is standing in for (relation kind, endpoint kind, qualifier, mediator).
* Candidate sets SHALL be stated as **kinds, facets, and RelationKind tokens**, not as synonym lists. “Service” ⇒ {promise content, access point, provider principal, commitment, performed work and evidence, …} is the archetype (A.6.8).
* When endpoint‑side ambiguity is present, the guide SHOULD recommend producing a **Candidate‑Set Note** (A.6.P:4.0b) as part of the rewrite, so the chosen facet or kind is reviewable.
* Discriminating questions SHOULD be phrased as small **tests** that map directly to slot requirements (e.g., “Can you call it?” ⇒ `accessPointRef`; “Is it deontic?” ⇒ `commitmentRef` + accountable principal; “Is it actuals?” ⇒ `deliveryWorkRef` + witnesses).
* Canonical rewrites SHALL land in the A.6.P Tech forms (functional or arrow) and SHALL specify any newly required qualifiers (scope, Γ_time, `U.Viewpoint` and `U.View`, schemes, witnesses).
* Quadrant hooks SHALL name which claim(s) are expected in each L/A/D/E quadrant so that “unpacking” reliably produces reviewable claim requirements rather than prose paraphrases.

**Mini-row (metonymy; endpoint-side trigger, illustrative).**

`"at the table"` → `{PlaceRef(Table#7), MeetingRef(NegotiationSession#3), RoleRef(DecisionMakerSeat#2)}` → tests `{Is the claim about physical location? about participation? about accountable role? which carrier-referenced witnesses exist (badge or access log, calendar invite, minutes or recording)?}` → rewrite `{locatedAt(personRef=…, placeRef=…, Γ_time=…, witnesses=…) | participatesInMeetingUnder(personRef=…, meetingRef=…, roleRef?=…, Γ_time=…, witnesses=…)}` → L/A/D/E hooks `{L: publish RelationKind tokens + SlotSpecs + polarity and inverses; A: decision or publication use requires explicit Γ_time + witness set; D: forbid metonymic endpoint spans in Tech prose (require explicit refs); E: cite carrier-referenced witnesses and their observation conditions}`.

#### A.6.P:4.9 — A.6.B classification template for RPR relation specifications

Any RPR‑pattern that claims boundary-bearing relation semantics SHALL classify its normative content using **A.6.B**:

* **L‑claims**: signature‑level structure and invariants and rules (SlotSpecs, polarity, invariants).
* **A‑claims**: admissibility or entry-gate rules for *using* relation instances in specified uses (e.g., decision use requires witnesses; time dependence requires `Γ_time`; cross‑Context use requires Bridge and CL).
* **D‑claims**: deontic obligations on authors or agents (lexical firewall; prohibited umbrella use; rewrite obligations).
* **E‑claims**: work and evidence expectations and carrier reference (what counts as a witness; evidence freshness is a property of carriers, not prose).

A.6.P does not mandate a particular claim‑ID format; it mandates the **separation and cross‑reference discipline**.

**Atomicity + explicit references (normative, recipe-level).**
Per A.6.B, mixed sentences MUST be decomposed into **atomic** claims so each claim belongs to exactly one quadrant, and any dependencies MUST be expressed as explicit references (by claim ID or canonical location), not paraphrased duplicates.

**No upward dependencies (normative, recipe-level).**
`L-*` claims MUST NOT reference `A-*`, `D-*`, or `E-*`; `A-*` and `E-*` claims MUST NOT reference `D-*`. Where cross‑quadrant coupling is needed, link by explicit IDs in the allowed directions.

#### A.6.P:4.10 — A.6.S compatibility note (ConstructorSignature is optional but canonical for engineered relation specialisations)

If an RPR‑pattern is applied as an engineered relation specialisation (created or evolved over time), it SHOULD be expressible as:

* a **TargetSignature**: declared relation kinds + SlotSpecs + invariants and rules, and
* a minimal **ConstructorSignature**: effect‑free operations that rewrite under‑specified prose into the explicit form and evolve relation records using the change‑class lexicon (mapped to A.6.5/A.6.6 canonical verbs).

If a ConstructorSignature is provided, it SHOULD (conceptually) declare, for each constructor operation entry:

* whether it is a species of **A.6.2 / A.6.3 / A.6.4**, and
* which **`U.EpistemeSlotRelation` slots** (C.2.1) it may read and write (SlotKind, ValueKind, and RefKind profile).

**Publication note (recommended).**
If the TargetSignature or relation-kind registry is published via MVPK, treat every face as a **view** (no new semantics), keep viewpoint accountability explicit, and prefer stable claim IDs (Claim Register) so downstream carriers cite claims rather than paraphrasing.

### A.6.P:5 — Archetypal Grounding (System / Episteme)

A.6.P requires Tell-Show-Show grounding in both System and Episteme cases.

#### A.6.P:5.1 — System archetype: “same system across environments”

**Tell.**
An operations note says: “Staging is the same service as Production.” Months later, incident metrics are aggregated “because it is the same service”, and evidence across environments is mixed, producing an incorrect causal story.

**Show.**
Treat “same” as a red-flag umbrella token. Rewrite into an explicit cross-Context relation kind,
typed to the facet the draft actually uses (service delivery system sameness for actuals and evidence aggregation; not about promise contents).

**Show (candidate‑set note; endpoint facet restoration).**

```
CandidateSetNote(triggerSpan="service" in "same service", position=endpointFacet(p₁)):
- candidates: {promiseContent, serviceAccessPoint, serviceProviderPrincipal, serviceDeliverySystem}
- selected:   serviceDeliverySystem
- why:        the claim is later used to justify mixing operational actuals and evidence (metrics + incident logs);
  local cues point to delivery records or carriers (manifests, config, and test runs), not clause carriers
- consequence: endpoints typecheck as `DeliverySystemRef` participants; clause or provider facets are explicitly out-of-scope

sameDeliverySystemUnder(
  leftDeliverySystemRef  = SystemRef(staging_delivery_system),
  rightDeliverySystemRef = SystemRef(prod_delivery_system),
  scope     = ClaimScope{SLO_family = X, signals = {latency, error_rate}},
  Γ_time    = interval[2025-12-01, 2026-01-31],
  viewpoint = OpsViewpoint,
  witnesses = {deploymentManifestPins, configPins, testRunPins}
)

aggregationAdmissibleIff(
  relationRef  = RelationRef(sameDeliverySystemUnder, SystemRef(staging_delivery_system), SystemRef(prod_delivery_system), ed=…),
  aggregatedActuals = deliveryWorkMetrics,              // actuals
  Γ_time       = interval[2025-12-01, 2026-01-31],
  witnesses    = {metricCarrierPins, incidentLogPins}   // evidence carriers for the actuals
)
```

**Show.**
Now the relation is auditable: aggregation is admissible only if the relation kind’s admissibility
claims say it preserves the needed characteristics under the declared scope and time, and if witnesses exist.
Cross-Context reuse is explicit and cannot piggyback on label identity.

#### A.6.P:5.2 — Episteme archetype: “the models are synced”

**Tell.**
A draft says: “The simulation model is synced with the physical twin.” Reviewers ask what “synced” means. The authors respond with examples, but downstream users still cannot tell whether the claim is about parameters, structure, calibration, evidence freshness, or mapping quality.

**Show.**
Rewrite “synced” as an explicit correspondence relation kind + explicit qualifiers + witnesses:

```
entityMatchedBy(
  leftRef          = ModelRef(SimModel@ed=12),
  rightRef         = SystemRef(PhysicalTwin@ed=7),
  mappingArtifactRef = AlignmentModel_2025_11,
  scope            = ClaimScope{signals = S, metrics = M},
  Γ_time           = snapshot(t),
  referenceScheme  = RefScheme(CustomerIdRegistry#EU),
  viewpoint        = DataEngineeringViewpoint,
  witnesses        = {evalRunPins, calibrationPins, mappingArtifactPins}
)
```

**Show (change narration).**
Two weeks later, the mapping publication is replaced and the witness set is refreshed. In decision or publication use, represent this as a new edition and narrate the change via change classes (not via “re‑synced”):

```
withdrawRelation( relationRef = RelationRef(entityMatchedBy, leftRef, rightRef, ed=12) )

declareRelation(
  entityMatchedBy(
    leftRef           = ModelRef(SimModel@ed=12),
    rightRef          = SystemRef(PhysicalTwin@ed=7),
    mappingArtifactRef= AlignmentModel_2026_01,
    scope             = ClaimScope{signals = S, metrics = M},
    Γ_time           = snapshot(t₂),
    referenceScheme   = RefScheme(CustomerIdRegistry#EU),
    viewpoint         = DataEngineeringViewpoint,
    witnesses         = {evalRunPins_2026_01, calibrationPins_2026_01, mappingArtifactPins_2026_01}
  )
)
```

**Show.**
Different “sync meanings” become different **RelationKind tokens** (e.g., `entityMatchedBy`, `schemaAlignedUnder`), not adjectives. Subsequent changes become narratable as `retargetParticipant`, `rescope`, `retime`, or `refreshWitnesses`, rather than “we updated the sync”.

### A.6.P:6 — Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Ontological and Epistemic**, **Prag**, **Did**. Scope: **Universal** for RPR‑style precision restoration in the A.6 cluster.

* **Gov bias:** prefers explicit admissibility and evidence-use and witness-relation explicitness; increases auditability but raises authoring cost.
* **Arch bias:** favours reusable structural lenses (records and hyperedges) over narrative prose.
* **Ontological and Epistemic bias:** pushes kind‑explicit relations and polarity discipline; discourages metaphor-first modeling.
* **Prag bias:** reduces rework and cross-team misinterpretation; may feel heavy in exploratory notes.
* **Did bias:** enforces teachable rewrite guides; can be perceived as prescriptive.

### A.6.P:7 — Conformance Checklist (CC‑A.6.P)

A pattern P conforms to A.6.P (i.e., is an RPR‑pattern) iff:

 > **Note.** This checklist defines conformance for **RPR specialisations** (e.g., A.6.5, A.6.6, A.6.8, A.6.9, A.6.C, and additional admitted A.6.x patterns). A.6.P itself is the **governing RPR pattern**.

1. **CC‑A.6.P‑1 — Lens is explicit.**
   P SHALL name the stable lens used to stabilise the ambiguity cluster and justify its fit.

2. **CC‑A.6.P‑2 — RelationKind is explicit and named through admissible mint-or-reuse.**
   Every in‑scope relation claim SHALL name an explicit RelationKind token, and that token SHALL resolve to a vocabulary entry whose relation specification skeleton publishes (at minimum): polarity (and explicit inverses if needed), participant SlotSpecs `⟨SlotKind, ValueKind, refMode⟩`, qualifier requirements, witness expectations for decision or publication use, admissible semantic change classes, and (when applicable) cross-Context or cross-plane policy (Bridge + CL + loss notes). Claims classified under A.6.B SHALL respect A.6.B.
   When a suitable token does not already exist, authors SHALL mint or document it through **F.18** rather than inventing a one-off label by intuition: **MintNew** is the default, the seed candidate set and NQD-front SHALL be shown, and the final token SHALL be selected from that non-dominated front unless an explicit continuity exception is recorded.
   The relation specification skeleton SHALL also declare admissible **repair options for endpoint kind mismatches** (KindBridge / explicit narrowing / explicit retargeting) and enforce **qualifier placement discipline** (no adjective smuggling).

3. **CC‑A.6.P‑3 — Slot‑explicit instances.**
   P SHALL ensure that every in‑scope relation instance is expressible as a Qualified Relation Record filling all relation-specification-required participant slots (no hidden arity; see WF‑A6P‑QR‑1).

4. **CC‑A.6.P‑4 — Qualifiers are explicit when required.**
   If scope, time, or viewpoint or reference-scheme assumptions matter (or the relation kind requires them), they SHALL be explicit; implicit “current”, “latest”, or “in our context” SHALL NOT substitute.
   When witness freshness or decay matters, it SHALL be expressed explicitly (evidence-use or witness-relation timespans, qualification windows, explicit freshness predicates), not by treating `Γ_time` as a proxy.

5. **CC‑A.6.P‑5 — No silent polarity flips.**
   If inverse wording is used, it SHALL use explicit inverse tokens or polarity‑preserving forms; implicit endpoint-position flips are forbidden.

6. **CC‑A.6.P‑6 — Change semantics use a change‑class lexicon.**
   Normative prose about relation evolution SHALL use named semantic change classes (declare, withdraw, retarget, revise, rescope, retime, refreshWitnesses, or changeKind), not generic “update, modify, sync, bind, or anchor”.
   Any mapping to more specific slot verbs MUST preserve the A.6.5 retarget vs by‑value edit distinction.

7. **CC‑A.6.P‑7 — “bind” and “binding” discipline.**
   `bind` and `rebind` SHALL be reserved for name binding (Identifier → SlotKind or slot-instance) and SHALL NOT be used as a synonym for relation edits.

8. **CC‑A.6.P‑8 — Lexical firewall is normative.**
   P SHALL list red-flag umbrella tokens for the relation pattern and provide rewrite rules; umbrella tokens SHALL NOT function as meaning‑surrogates in Tech or normative prose. If retained Plain umbrella wording appears, it SHALL be immediately mapped to an explicit Tech form (`relationKind(…)` or `--relationKind-->`).

9. **CC‑A.6.P‑9 — A.6.B atomicity, classification, and explicit references are respected.**
   Normative text SHALL be decomposed into atomic claims classifiable under exactly one quadrant (L/A/D/E). Dependencies SHALL be expressed by explicit references (IDs or canonical locations), not paraphrase. No‑upward‑dependency constraints SHALL be preserved.

10. **CC‑A.6.P‑10 — Evidence is carrier-referenced (A.7 separation).**
    Statements about witnesses, evidence, and freshness SHALL be framed as properties and expectations of carriers and work, not as properties of prose.

11. **CC‑A.6.P‑11 — A.6.S compatibility when engineered.**
    If the RPR specialisation is presented as engineered or evolving, it SHALL be compatible with A.6.S: distinguish TargetSignature vs ConstructorSignature; map constructor verbs to A.6.5/A.6.6 canonical verbs; keep constructor ops effect‑free; and (when a ConstructorSignature is present) declare the C.2.1 slot read and write profile and whether ops are A.6.2/A.6.3/A.6.4 species.

12. **CC‑A.6.P‑12 — Cross-Context or cross-plane reuse is explicit (no “sameness by label”).**
    If a relation instance crosses Contexts or planes (or requires translation), the carrier SHALL cite Bridge ids + CL policy (and loss notes, when applicable). Label identity or “same anyway” prose SHALL NOT substitute.

13. **CC‑A.6.P‑13 — Disambiguation guide is actionable.**
    P SHALL include an explicit rewrite and selection guide that maps each red-flag umbrella cluster or generic head phrase with FPF-governed use to candidate head kinds, candidate `RelationKind` tokens, and (when the ambiguity is endpoint-side) candidate endpoint facets and candidate endpoint kinds, plus required qualifiers and canonical rewrite forms.
    The guide SHOULD follow the RPR‑Disambiguation format: **trigger → candidates → discriminating questions and tests → canonical rewrite → L/A/D/E hooks**.

    Where endpoint referential compression is a primary risk, the guide SHOULD also include (or point to) the **Candidate‑Set Note** template (A.6.P:4.0b) so instance‑level reviews have an auditable trail: candidates → selected facet or kind → why.

14. **CC‑A.6.P‑14 — Grounding spans System and Episteme.**
    P SHALL include at least one Tell–Show–Show vignette in a **System** case and at least one **Episteme** case (per E.8), demonstrating a real ambiguity repair and a relation‑change narration using the change‑class lexicon.

15. **CC‑A.6.P‑15 — Trigger rule is explicit.**
    P SHALL include an explicit trigger rule (or selection heuristic) stating when the repair case applies and what counts as “in-scope” umbrella relational prose.

### A.6.P:7a - Portfolio, front, archive, and shortlist disambiguation

- Treat bare uses of `portfolio`, `front`, `archive`, `Pareto`, `shortlist`, `space`, `reachability`, and `stepping stone` as repair triggers whenever they carry live explanatory work.
- Use the helper declarations from A.0:QF.1a when repairing the sentence: do not let `SetResultFamily`, `SourceSetFamily`, `SourceSetComposition`, `SubjectKind`, `DerivedViewKind`, `BasePaletteRef`, `SelectorOutcomeKind`, `HandoffKind`, `PromotionPolicy`, `RetentionIntent=steppingStone`, `EligibilitySet`, `DominanceSet`, `TieBreakerSet`, or `TelemetrySet` read as public set-outcome heads.
- The minimum repair is to state the `SubjectKind`, the declared comparison bundle, and, when selection or publication outcomes are involved, the declared `SelectorOutcomeKind`, the applicable `SetResultFamily` or `HandoffKind`, the declared `SourceSetFamily`, `SourceSetComposition` when several sources are actually composed, `DerivedViewKind` or `BasePaletteRef` when a derived palette view matters, `LensId`, and which member of the shortlist family is meant.
- The declared comparison bundle is:
  - `EligibilitySet`
  - `DominanceSet`
  - `TieBreakerSet`
  - `TelemetrySet`
- If one front sentence depends on current `Q`, say whether the `DominanceSet` is the declared `Q` components or one promoted bundle under explicit policy.
- If one archive claim depends on coverage, stepping-stone retention, or reachability rather than current dominance, state that archive purpose explicitly instead of borrowing `Front` language.
- If one phrase uses `SoTA portfolio` before comparison or choice semantics exist, rewrite it as `TraditionPalette` only when the members are traditions; otherwise rewrite it as `Palette + SubjectKind`.
- If one phrase uses `Pareto archive` for the whole retained exploration outcome, rewrite it as `ExplorationArchive`.
- If one phrase uses `stepping-stone set` for the whole retained exploration outcome, rewrite it as `ExplorationArchive` and reserve `SteppingStoneSet` for one narrower retained subset when that narrower retention requirement really matters.
- If one selected set is mentioned, name the shortlist-family stack explicitly:
  - `Shortlist` for the selected outcome
  - `RankedShortlist` for its ordered specialization
  - `ShortlistId` for the emitted identity or public token
  - `ChoiceSet` only when the mathematical set object itself is the point of the sentence
- If one phrase says `choice set` but the sentence is naming the public selected outcome, rewrite it as `Shortlist` and keep `choice set` only as one mathematical gloss when needed.
- If one phrase says `shortlist` and the output is explicitly ordered, rewrite it as `RankedShortlist` and keep it distinct from `Shortlist`.
- If one phrase says `shortlist` but really points at one emitted token or publication handle, rewrite it as `ShortlistId`.
- If one sentence moves between search-space and outcome-space talk, name the space whose objects are being compared before making claims about dominance, archive retention, or frontier expansion.
- If one sentence says `Pareto` but really means one post-lens selected result, rewrite it as `Shortlist` or `RankedShortlist` rather than widening `Front` until it means everything.
- Canonical rewrites for FPF-governed Q-Front / NQD prose:
  - `portfolio by Q` -> `Front over the declared Q components` when the sentence is about non-domination.
  - `portfolio by NQD` -> `Front over the declared DominanceSet plus ExplorationArchive under the declared retention policy` when both current front and retained exploration outcome are meant.
  - `Pareto shortlist` -> `Shortlist from <SourceSetFamily> under <LensId>` when the sentence is about publication or selection.
  - `Pareto archive` -> `ExplorationArchive under <RetentionPolicy>` when the sentence is about retained exploration rather than current non-domination.
  - `space of traditions, methods, and hypotheses` -> `Palette + SubjectKind` first; add `TraditionPalette` only for `SubjectKind=Tradition`.
- Discriminating tests:
  - If the sentence answers "what counts as current non-domination?", repair toward `Front` / `Q-Front` plus `DominanceSet`.
  - If the sentence answers "what remains worth retaining for reach, coverage, or later probing?", repair toward `Archive`, `ExplorationArchive`, or `RetentionIntent=steppingStone`.
  - If the sentence answers "what selected set was emitted for downstream use?", repair toward `Shortlist`, `RankedShortlist`, and optional `ShortlistId`.
  - If the sentence answers "which goal, capability, or learning frontier might widen next?", repair toward `GoalSpaceExpansionCue`, `LearningProgressSignal`, or `CompetenceModelRef`, and keep those outside default dominance unless one policy promotes them.

### A.6.P:8 — Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| ---------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| “Just define the umbrella word” | Definitions do not separate arity, operation classes, or viewpoint asymmetry. | Replace umbrella use with explicit RelationKind + qualified record + change lexicon. |
| Keep the umbrella verb, add adjectives | Adjectives are not relation specifications; invariants remain unstated. | Mint or select distinct RelationKind tokens; enforce rewrite discipline. |
| Leave a FPF-governed generic head uninterpreted | Readers cannot tell what kind of thing the phrase governs, so later qualifiers float without an ontology. | Restore the head kind first in source-local terms; only then repair the remaining relation or comparison reading. |
| Let a qualifier smuggle the real claim kind or admissible-use boundary | A phrase like "comparative note", "safe guidance", or "reliable output" sounds precise while leaving the actual relation, comparison reference set, or authority-reference requirement implicit. | Unpack the qualifier into explicit comparison reference set, relation kind, admissibility condition, or L, A, D, and E-classified claim before any claim requiring explicit relation, admissibility, authority-reference relation, or reliance. |
| Treat support as the recovered kind or relation | `SupportRecord`, `support source`, `support line`, `support relation`, or `supported use` can sound precise while hiding whether the claim kind being made or admissible-use boundary is evidence path, source-use relation, admissible-use boundary, assurance claim, causal-use relation, decision help, publication help, C.29 lens-use result, characteristic construction, or ordinary orientation. | Recover the governing claim kind named by value or admissible-use boundary and governing pattern first: evidence path, `E.17:5.1b` source relation or claim-admissibility vocabulary, relationClaimSlice, admissibleUse, projectSideFPFRef, assurance claim, causal evidence path or causal-use verdict, C.29 lens-use result, characteristic construction, bridge or comparison relation, or companion-only reader function. Use support-headed wording only when that local pattern named by value defines the field or record and states admissible and non-admissible use. |
| Leave pronominal and metonymic endpoints implicit | Endpoint identity or facet remains guesswork; slot typing cannot stabilise. | Reconstruct candidate referents and facets (**capture as a Candidate‑Set Note**); add explicit slots and references; then rewrite (A.6.8 is the archetype for “service” polysemy). |
| Ontology only, no lexical guardrails | Prose re-collapses meaning. | Add red-flag tokens + prohibited umbrella use in Tech or normative prose. |
| Lexicon only, no structural lens | Becomes subjective policing. | Introduce stable lens + slot schema; then attach guardrails. |
| Solve viewpoint mismatch by renaming endpoints | Silent re-typing breaks cross-pattern reuse. | Keep endpoint positions stable; use explicit kind selection + explicit repair options. |
| Using “bind” to mean “edit relation” | Collapses name-binding vs slot-writing classes. | Reserve `bind` and `rebind` for names; use change lexicon / slot verbs properly. |
| Implicit “current” or “latest” | Violates explicit time discipline. | Add explicit `Γ_time` where time matters. |
| Treat `Γ_time` as witness freshness | Time selection does not equal evidence freshness or decay; this conflates time discipline with evidence relations. | Keep `Γ_time` for temporal scope; express freshness or decay via witness metadata and carrier-referenced E-claims. |
| Collapse search-space refs, declared-substrate interpretive views, and publication forms into one `space` or `view` | Search-space refs, outcome-space refs, declared-substrate interpretive views, and source sets and set results become indistinguishable, so later claims lose their primary `EntityOfConcern` or relation named by value or claim record. | Restore the declared `CharacteristicSpace`, any `SearchSpaceRef` and `OutcomeSpaceRef`, the active source set or active set result, the declared-substrate interpretive view or atlas view if any, and any `OutcomeMapRef` or `BridgeDistortionNote` before making the claim. |
| Compare across mixed kinds | `PublicationUnit`, project record, process, authority-use claim, or source-use claim gets ranked on one comparison reference set before its kind and governing requirement are restored. | First restore head kind, then qualifier-carried claim, then rewrite the sentence through the evidence path named by value, threshold, transfer condition, admissible-use boundary, or source-description claim wording so the comparison reference set is homogeneous. |

**Worked repair slice — NQD and OEE space, view, and publication stack.**

Draft: “The archive projects into the outcome space through the atlas view.”

Repair sequence:

* `TraditionArchive` = derived retention view over one declared palette.
* `OutcomeSpaceRef` = guarded role reference to the declared `CharacteristicSpace` used for outcome-side judgment.
* `TraditionAtlasView` = optional related interpretive view, not the default meaning of the archive.
* `OutcomeMapRef` = explicit source-to-outcome map ref if the passage must show how the archive maps into one outcome-side or effect-side declared space or reference.

Canonical rewrite:

* Keep `TraditionArchive` as the source set for the set publication.
* Cite `OutcomeSpaceRef` only when the claim is about outcome-side evaluation against the declared `CharacteristicSpace`.
* Cite `OutcomeMapRef` only when the source-to-outcome relation or named map ref itself matters.
* Use `TraditionAtlasView` only if several declared views or qualifiers must stay visible together; otherwise leave the passage at archive-first or palette-first precision.

### A.6.P:9 — Consequences

**Benefits**

* **Predictable precision upgrades.** Umbrella relational prose becomes systematically expandable into explicit structure.
* **Viewpoint conflict becomes repairable.** Differences are shown as explicit role values, kinds, and qualifiers, not silent rewrites.
* **Change becomes speakable.** “What changed?” is a named semantic change class, reducing folklore.
* **Cross‑Context safety improves.** “Same, synced, or linked” becomes boundary-bearing relation specification and auditable, not rhetorical.

**Trade‑offs / mitigations**

* **Higher authoring overhead.** Mitigated by progressive elaboration: expand only when invariants, reuse, or decisions require it.
* **More explicit qualifiers.** Mitigated by keeping the lens stable and reusing slot templates (A.6.5/A.6.6).
* **Perceived prescriptiveness.** Mitigated by allowing Plain-register glosses that are immediately mapped to Tech tokens (without creating new relation specifications).

### A.6.P:10 — Rationale

Upper and foundational ontologies optimise for broad applicability via sparse commitments. FPF’s recurring, high-cost failures are often elsewhere: **under‑specified relations** in prose, where ambiguity hides in arity, kind selection, viewpoint, and change semantics.

A.6.P is orthogonal to “add a global taxonomy”:

* It provides a repeatable method to **restore relational precision** without requiring any external formalism or auxiliary authoring apparatus.
* It operationalises A.6’s boundary discipline by ensuring relation talk can be cleanly separated into signature invariants, admissibility, deontics, and evidence and work (A.6.B), rather than becoming one undifferentiated boundary claim.

### A.6.P:11 — SoTA-Echoing (informative; post-2015 alignment)

A.6.P echoes contemporary practice across independent traditions, while remaining notation-neutral and Context-local. A row is retained only when it changes the A.6.P solution, checklist, boundary, worked case, or reopen condition.

| Practice source line | Use of source | Echo | What A.6.P adopts or adapts | What A.6.P rejects |
| --- | --- | --- | --- | --- |
| W3C SHACL Recommendation (2017) for shape validation over RDF graph assertions. | Current-standard and reference use for assertion and constraint separation; not a complete current-best answer for FPF relation precision restoration. | Separates graph assertions from constraints over node and value shapes. | Adopts explicit structural constraint thinking for relation records and mutates `CC-A.6.P-2`: relation claims need explicit SlotSpecs, qualifiers, witness expectations, and admissible use, not only prose assertions. | Rejects treating validation shape notation as the required FPF notation or as a substitute for relation-kind selection and lexical guardrails. |
| RDF-star / SPARQL-star W3C Community Group Report (2021) and RDF and SPARQL WG current line for quoted triples and statement qualification. | Current-practice and working-standardization source use for qualified statements; not stable ontology authority for FPF. | Shows why hidden arity and qualification need explicit representation when statements carry statement-about-statement claim. | Adapts the qualification pressure into `RelationKind` plus qualifier slots and change-class lexicon; mutates the hidden-arity and candidate-set examples. | Rejects "reification solves the relation" when kind selection, endpoints, admissible use, and change semantics remain hidden. |
| ISO/IEC/IEEE 42010:2022 architecture-description practice on viewpoints, model kinds, and correspondences. | Current-standard and reference use for viewpoint accountability and correspondence discipline. | Treats viewpoints and correspondences as first-class description concerns. | Adopts viewpoint accountability for relation qualification and mutates boundary cases involving views, viewpoints, correspondences, and silent polarity flips. | Rejects importing architecture-description ontology as the general relation ontology; architecture-specific cases still go to `C.30`, `C.30.ASV`, or `C.30.P`. |
| Pickering, Gibbons, and Wu, "Profunctor Optics: Modular Data Accessors" (ICFP 2017) and successor optics practice. | Current formal-lens source use for bidirectional view and update intuition; used as a stabilizing lens, not as mandatory notation. | "Pairs of projections plus invariants" makes multi-view relation discipline teachable. | Adapts optics as a didactic stabilizer for multi-view relation repair and mutates the rationale for stable lens -> explicit slots -> change classes. | Rejects requiring profunctor notation or treating formal elegance as proof of admissible relation use. |
| Fong and Spivak, "Seven Sketches in Compositionality" (2019), as applied-category-theory lineage for compositional modeling. | Lineage and didactic source use for compositional lens choice; not by itself current-best source use for FPF wording repair. | Shows why stable abstract lenses can be reused across domains. | Adapts compositionality as a reason to keep A.6.P notation-neutral while requiring relation slots and change lexicon; mutates the rationale and teaching examples. | Rejects adding a global category-theory ontology to FPF relation repair. |

These echoes justify why A.6.P is structured as: **stable lens -> explicit slots -> explicit change classes -> lexical guardrails**, rather than "just define the verb". A source row that does not change A.6.P fields, examples, checklist rows, boundaries, or reopen conditions is decorative and should be removed or demoted to lineage outside the SoTA echo.

### A.6.P:12 — Relations

**Specialised by**

* **A.6.5 `U.RelationSlotDiscipline`** — slot precision restoration for n‑ary relations.
* **A.6.6 Base Declaration Discipline** — base‑dependence precision restoration (SWBD + base‑change lexicon + `anchor*` red‑flags).
* **A.6.8 (RPR‑SERV)** — service polysemy unpacking as a relation and facet precision restoration discipline (serviceSituation lens + canonical rewrites + service‑specific tests and change narration).
* **A.6.9 (RPR-XCTX)** - Cross-Context Sameness Disambiguation - Repairing cross-context "same", "equivalent", "align", or "map" via explicit Bridges
* **A.6.H (RPR‑WHOLE)** — wholeness language unpacking (“whole, part, integrity, or complete”) into boundary, typed parthood, explicit Γ selection, order and time classification, and A.15 completeness and coverage claims.

**Coordinates with**

* **A.6.S `U.SignatureEngineeringPair`** — RPR rewrite operations can be packaged as a ConstructorSignature for engineered relation specialisations; must preserve canonical verb mapping and effect‑free constructor semantics.
* **A.19 `U.CharacteristicSpace` + `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`** — for declared characteristic spaces, guarded role references, and interpretive-view and atlas-view discipline when one relation repair needs those layers explicit.
* **G.2** — for palette, front, archive, or tradition-atlas specialization when the repaired passage is SoTA-harvest or synthesis prose.
* **F.18** — when the remaining issue is naming-side choice among candidate labels rather than relation typing or publication-use repair.
* **C.2.2a, A.16, A.16.1, A.16.2, B.4.1, and B.5.2.0 + C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** - relation publication enters only after admissible language-state chart positioning, articulation, and closure record exist; earlier cue-pack material stays under the language-state boundary, prompt-shaped continuations stay with `B.5.2.0`, retreat or reopen moves remain governed by `A.16.2`, and `A.16.0` is used only when lineage, branch, loss, or responsibility-transfer history must itself be published.

**Candidate extraction signals (informative; not queued specialisations)**

These recurring relation-repair families are signals for applying the `E.10.ARCH` extraction criterion. They do not by themselves create a new A.6.x pattern.

* Cross‑Context equivalence / “sameness” discipline (Bridge + loss-note relation patterns)
* Correspondence and consistency + repair discipline (sync and alignment relation patterns)
* Transfer and responsibility-transfer discipline (multi‑party “give, assign, or accountability” relation patterns)

### A.6.P:12a - Quantum-like relation and probe wording precision note

Treat quantum-like FPF-governed wording such as `coupled`, `interaction`, `probe`, `measurement`, `export`, `collapse-like`, `field-like`, `state update`, or `non-copyable` as ordinary RPR triggers when they carry live explanatory work. These words are not reusable FPF relation predicates merely because they appear in a quantum-like source or example.

Action classification:

1. Mark the trigger span in the draft.
2. Restore the head kind first: is the phrase naming a boundary interaction, bridge or export, evidence carrier, measure, work act, viability move, decision comparison, or representation shortcut?
3. Build a small candidate set for the relation kind and endpoint facets.
4. Select the relation kind or refer the case to an existing governing pattern.
5. Fill slots: participants, polarity, channel or mediator, time window, witness, and change class.
6. Rewrite the sentence into explicit local prose or a relation form only after the ontology is clear.
7. Move to `C.26` only when ordinary relation repair still leaves order-sensitive, probe-frame-sensitive, incompatible-probe, no faithful-enough export, or state-representation coarsening claim kind or admissible-use boundary.

Minimum repair for FPF-governed quantum-like relation wording:

| Relation slot | Required recovery |
| --- | --- |
| Participants | Which endpoints, carriers, contexts, roles, views, or systems participate |
| Relation kind | Whether the prose means bridge or export, evidence, measurement, work enactment, boundary interaction, viability regulation, or local decision comparison |
| Direction / polarity | Whether the relation is one-way, mutual, symmetric, asymmetric, reversible, lossy, or only observer-relative |
| Channel or mediator | Message, API read, workshop, metric, dashboard, carrier, bridge, instrument, or other interaction medium |
| Time / window | `Γ_time`, persistence, decay, refresh, or reprobe condition when state interpretation depends on time |
| Witness | Evidence carrier or observation that makes the relation readable |
| Change class | Whether the relation is a retarget, rescope, reframe, update, export-loss, state-interpretation change, or ordinary relation refinement |

Useful outputs:

- an ordinary `F.9`, `A.6.8`, `A.6.9`, `C.16`, `A.15`, or `C.25` governing pattern when the repaired slots reduce to one existing governing claim kind or admissible-use boundary;
- a local explanatory phrase when no reusable relation token is justified;
- an `A.6.P` repair plus `F.18` naming pass when a reusable relation token is actually needed;
- a `C.26` application only for the remaining state, probe, export, frame, or coarsening claim kind or admissible-use boundary.

### A.6.P:12b - C.29 mathematical-lens use relation

> **Mathematical-lens use relation.** `A.6.P` may select a stable mathematical substrate for relation precision restoration: arity, polarity, endpoint discipline, slot structure, and relation-kind repair. This does not by itself apply `C.29`. `C.29 Mathematical Lens Use` applies only when that substrate is used as a FPF-governed mathematical representation of a selected subject, relation, claim, or structure beyond relation repair. `A.6.P` does not by itself license source-domain ontology transfer.

### A.6.P:End

