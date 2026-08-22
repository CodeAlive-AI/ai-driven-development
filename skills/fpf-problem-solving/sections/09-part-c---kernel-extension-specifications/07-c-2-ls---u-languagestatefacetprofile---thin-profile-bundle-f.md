## C.2.LS - `U.LanguageStateFacetProfile` - Thin profile bundle for language-state facets

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state facet profile.

**Use this pattern when.** Use C.2.LS when a `U.Episteme` publication needs one explicit profile that keeps formality, articulation, closure, anchoring, representation factors, and local thresholds visible together.

**What goes wrong if missed.** Teams replace the facet profile with a maturity adjective such as `ready`, `raw`, or `stable`, then use that label to choose routes, decide whether to reopen, interpret Bridges, or make publication decisions. The label hides the actual facet values.

**What this buys.** A thin, decomposable profile bundle: each facet keeps the definition and tests supplied by its own pattern, while the profile gives authors, assurance readers, and integrators one place to publish a threshold-relevant language-state position.

### C.2.LS:1 - Problem frame
Once position claims in the declared language-state chart over `U.CharacteristicSpace` must be published and compared, teams need one thin profile bundle that keeps the relevant facets visible as one explicit facet profile without turning that profile into a second characteristic calculus or a surrogate maturity progression.

### C.2.LS:2 - Problem
Without a dedicated profile bundle, authors blur articulation, closure, anchoring, and representation into one vague maturity story, or they silently reuse `F` as a surrogate. That blocks admissible threshold publication, undercuts `A.16` move guards, and makes school-to-school bridge work harder than it needs to be.

### C.2.LS:3 - Forces
| Force | Tension |
|---|---|
| **Thin profile bundle vs practical coordination** | Keep the bundle small, but still give one stable place where the language-state facets are named together. |
| **Reuse vs duplication** | Reuse `A.18/A.19` characteristic machinery and `E.18` transition-structure publication rather than building a rival calculus. |
| **Local thresholds vs cross-context comparability** | Contexts need local thresholds, but the facet names must stay stable enough for bridge work and viewpoint bundles. |

### C.2.LS:4 - Solution
`U.LanguageStateFacetProfile` is a typed profile bundle that names the facets by which position claims in the declared language-state chart over `U.CharacteristicSpace` are published and interpreted:

- `formalityRef` -> `U.Formality` from `C.2.3`
- `articulationExplicitnessRef` -> `U.ArticulationExplicitness` from `C.2.4`
- `languageStateClosureDegreeRef` -> `U.LanguageStateClosureDegree` from `C.2.5`
- `languageStateAnchoringModeRef` -> `U.LanguageStateAnchoringMode` from `C.2.6`
- `languageStateRepresentationFactorBundleRef` -> `U.LanguageStateRepresentationFactorBundle` from `C.2.7`
- `thresholdRefs?` -> context-local threshold declarations over the named facets
- `routeNotes?` -> informative notes that help interpret routing or reopening decisions

`C.2.LS` therefore defines only the **profile bundle**; it defines neither an individual characteristic nor a trajectory. `A.18/A.19` supply characteristic semantics, `A.16` defines admissible moves, and `E.18` describes publication of explicit transition structures.

#### C.2.LS:4.0a - Kind and profile-bundle boundary

`U.LanguageStateFacetProfile` is a dependent durable profile-bundle value under the declared `U.LanguageStateSpace` and `U.CharacteristicSpace` boundary, not a root U-kind. Its identity is the explicit bundle of language-state facet refs used for position reading and threshold publication. A local dashboard, table, route note, or maturity label is a publication or interpretation over the bundle, not the bundle itself.

#### C.2.LS:4.1 - Contribution boundary
`C.2.LS` defines only profile composition and requires the language-state facets to remain explicit and non-collapsed. It does **not**:

- redefine `F`;
- invent a second formality progression;
- redefine the scale semantics of `AE`, `CD`, `LanguageStateAnchoringMode`, or `U.LanguageStateRepresentationFactorBundle`;
- define reopen/backoff moves;
- define endpoint classification or bridge kinds.

#### C.2.LS:4.2 - Threshold publication discipline
Any threshold used to choose a next question, constrain an admissible move, or begin `A.6.P` recovery shall be published on explicit named facets in the profile. Do not describe hidden sub-levels of `F` when the real issue is articulation, closure, anchoring, or the representation-factor bundle.

#### C.2.LS:4.2.a - Local profile-reading witness
For this pattern, a published facet profile is reviewable when:

- the facet refs are explicit or explicitly inherited from an already pinned upstream publication;
- any threshold-bearing use names the facet whose threshold is being invoked;
- route notes or local overlays remain informative and visibly docked to the explicit facet bundle;
- and the profile does not smuggle move rules, bridge rules, gate state, or downstream definitions and tests into the bundle record.

A polished label, one strong facet, or one memorable route note does not by itself yield an admissible profile reading. The profile remains conformant only when the named facets stay explicit and decomposable.

#### C.2.LS:4.3 - Composite readings
A language-state judgement may be composite, but the composite shall be decomposable. For example, a cue may be:

- low `AE`,
- medium `CD`,
- `AM.TraceAnchored`,
- and representation-wise mixed rather than purely symbolic.

A conforming profile makes this decomposition visible rather than hiding it under one poetic label such as "early" or "raw".

#### C.2.LS:4.4 - Corridor map note
`C.2.LS` participates in the current `Language-State & Semantic Routing Corridor`, but contributes only the thin facet-profile bundle. Readers who need one map of the full language-state pattern set should read the corridor note in `C.2.2a`.

That map does not change this boundary: `C.2.LS` still does not define cue preservation, route-bearing publication, prompt entry, or downstream endpoint use.

### C.2.LS:5 - Archetypal Grounding
**Tell.** A team may say a draft is "still forming" for different reasons. `U.LanguageStateFacetProfile` forces the team to say whether the issue is low articulation, low candidate-space closure, an anchoring mismatch, or an unresolved representation-factor bundle.

**Show (System).** An operator alert note can be `AM.OperatorLoop` anchored and low-closure without being low-formality in every respect.

**Show (Episteme).** An inquiry note can be low articulation yet already tightly anchored to exemplars and traces.

### C.2.LS:6 - Bias-Annotation
The pattern biases authors toward keeping facets explicit and away from master-scale stories. That cost is intentional: the goal is to prevent surrogate progressions from entering the Core.

### C.2.LS:7 - Conformance Checklist
- `CC-C.2.LS-1` A language-state facet profile **SHALL** reference the patterns that define its facets rather than invent local unnamed factors.
- `CC-C.2.LS-2` `C.2.LS` **MUST NOT** redefine `F` or create a second formality progression.
- `CC-C.2.LS-3` Thresholds that matter for routing, reopening, or lexical repair **SHALL** be published on explicit facets.
- `CC-C.2.LS-4` Trajectory accounts that rely on facet profiles **SHOULD** reuse `A.16` move kinds and `E.18` transition-structure publication rules.
- `CC-C.2.LS-5` Composite labels such as `early`, `settled`, or `ready` **SHALL NOT** stand in for the explicit facet bundle when those states matter operationally.
- `CC-C.2.LS-6` Composite readings, overlays, and route notes **SHALL** remain decomposable into named facets and **MUST NOT** behave as hidden master factors.
- `CC-C.2.LS-7` A profile bundle **MUST NOT** smuggle move rules, bridge rules, gate state, or downstream definitions and tests into what should remain a thin facet-profile record.

### C.2.LS:8 - Common Anti-Patterns and How to Avoid Them
- **Shadow progression.** Treating `early/late` as a master scale. Split the judgement into the named facets.
- **Formality capture.** Letting `F` stand in for closure or articulation. Publish those facets explicitly.
- **Bundle inflation.** Turning `U.LanguageStateFacetProfile` into a second `A.19`. Keep it thin and referential.
- **Opaque readiness.** Using words such as `ready` or `mature` without naming which facet justifies the claim.
- **Route-note capture.** Letting an informative route note act as a move rule, gate state, or endpoint rule. Keep route notes informative. Use `A.16` for admissible moves, the applicable pattern for a downstream definition or test, the applicable gate or Work pattern for those claims, and an `authoritySourceRef` only when an external authority actually supplies the rule.

### C.2.LS:9 - Consequences
The benefit is clearer source and rule references: early cue work, bridge annotations, and reopen moves can all refer to one explicit facet profile. The trade-off is more explicit profile authoring and threshold publication.

### C.2.LS:10 - Rationale
The pattern gives the declared language-state chart over `U.CharacteristicSpace` one stable record through which its facet bundle can be published together, without taking over definitions and tests supplied elsewhere in FPF.

### C.2.LS:11 - SoTA-Echoing

**SoTA note.** This section does not mint a second rule source. It is a load-bearing alignment statement: the Solution, Conformance Checklist, and boundary discipline of this pattern must match the stance stated here or explicitly justify divergence.

**Source boundary.** The exact facet meanings and profile rules come from `A.18/A.19` and the neighboring FPF patterns. External sources are used only when they change a rule or case.

| Claim need | Bounded comparison | Exact source | Use in `C.2.LS` | Disposition |
|---|---|---|---|---|
| Readiness claims should stay scoped instead of collapsing into one global adjective. | A profile can state scoped conditions and local thresholds rather than one blanket readiness label. | NIST AI RMF 1.0 (2023) | Require explicit facet-level thresholds and reject a polished profile label as a substitute for the facet values. | **Adopt/Adapt.** |
| A publication can keep several named description elements visible without making their container identical to those elements. | Architecture-description vocabulary distinguishes named elements and their correspondence in a published description. | ISO/IEC/IEEE 42010:2022 | Use this only as a narrow publication comparator; it does not establish the language-state facet ontology. | **Narrow comparator only.** |

SysML v2 is deliberately excluded from the positive SoTA basis and from useful lineage for this question. Search prominence and official status do not show that it solves the facet-profile problem, and no demonstrated use here changes a rule or worked case. Treat it as a historical dead end for this comparison. Do not add a replacement citation merely to fill the removed row.

**Local stance.** The useful bounded result is a small explicit facet profile with local thresholds and decomposable readings, not one maturity adjective or one route-coloured bundle label.

### C.2.LS:12 - Relations
- Builds on: `A.18`, `A.19`, `C.2.2a`, `C.2.3`.
- Coordinates with: `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `E.18`, `F.9` for any Bridge and bounded-use claim, and `F.9.1` only for an optional stance note about that claim.
- Constrains: language-state threshold publication and profile composition.
### C.2.LS:13 - Worked Examples and Composition Notes

#### C.2.LS:13.1 - Operator-facing early alert
A console alert note may be published with a language-state facet profile such as:

- `F = F2/F3` because the note is structurally controlled but still lightweight;
- `AE = AE2` because candidate anchors are visible but not yet fully relation-shaped;
- `CD = CD1` because several routes remain live;
- `LanguageStateAnchoringMode = AM.OperatorLoop` because the note is directly anchored to operator intervention/work;
- `RepresentationFactorBundle = {local, sparse, mixed-symbolic}` because alert text and compact codes coexist.

This example shows why no one facet can replace the others. The note is not `simply early`; it is early in a specific, decomposable way.

#### C.2.LS:13.2 - Research cue before lexical repair
A felt or trace-anchored mismatch cue in an inquiry note may be:

- low `AE`,
- very low `CD`,
- `AM.EmbodiedFelt`,
- and representation-wise mixed because the cue is partly verbal, partly kinesthetic, partly exemplar-based.

That profile explains why the cue should remain in `A.16.1` rather than being forced into `A.6.P` or `B.5.2` immediately.

#### C.2.LS:13.3 - Architecture-description case
A viewpoint-bound note about the adequacy of an architecture description may be moderately high in `F`, moderately high in `AE`, still mid-level in `CD`, document-mediated in `AM`, and symbolic in its representation-factor bundle. The profile keeps description-side adequacy distinct from system-side engineering quality.

#### C.2.LS:13.4 - Same `F`, different profile
Two notes may share the same rough `F` band and still differ sharply in articulation, closure, anchoring, and representation factors. One may be operator-loop anchored and low-closure; another may be document-mediated and comparatively closed. The profile bundle keeps that difference visible instead of letting `F` behave like a master factor.

### C.2.LS:14 - Authoring and Review Guidance

#### C.2.LS:14.1 - For authors
When publishing a language-state facet profile:

1. start from the local authoring problem rather than from a memorized progression;
2. name the facet refs explicitly;
3. add threshold refs only when a threshold changes routing, repair, or another operative decision;
4. avoid global labels such as "mature", "raw", or "ready" unless the profile decomposition is already visible.

#### C.2.LS:14.2 - For assurance readers
An assurance reader should ask:

- is any facet silently replaced by `F`?
- is a threshold published on an explicit facet rather than on a poetic surrogate?
- do route or reopen claims actually match the published facet bundle?
- are profile notes genuinely informative, or are they smuggling definitions or tests from elsewhere?

#### C.2.LS:14.3 - For integrators
Integrators should preserve profile references rather than rephrasing them into local slang. A local alias is acceptable only if the underlying facet docking remains explicit and stable.

### C.2.LS:15 - Extension and Migration Notes

#### C.2.LS:15.1 - Local extension rule
Contexts may extend the profile with local threshold refs, route notes, or additional descriptive aids, but they shall not add a new master facet that collapses the named facet set into one summary factor.

#### C.2.LS:15.2 - Migration from surrogate prose
Older prose often says:

- "the episteme is still early",
- "the issue is not mature enough",
- "the note is ready",
- "the cue is still raw".

A conforming migration rewrites such statements into explicit facet talk: which facet is low, which is high, which threshold is or is not met, and which move that fact justifies.

#### C.2.LS:15.3 - Boundary reminder
`U.LanguageStateFacetProfile` is a coordination record. If authors put move rules, bridge rules, scale rules, or bundle semantics into the profile itself, that content belongs with the pattern that defines the move, Bridge, scale, or bundle.
### C.2.LS:16 - Profile Publication Package Discipline

#### C.2.LS:16.1 - Minimal publishable profile package
A publishable `U.LanguageStateFacetProfile` should normally carry:

- the declared facet refs for `AE`, `CD`, `LanguageStateAnchoringMode`, and `LanguageStateRepresentationFactorBundle`;
- any threshold refs that substantively affect routing, repair, bridge interpretation, or review load;
- the local relation to `F` when readers might otherwise treat `F` as a surrogate;
- any omission note when a facet is intentionally unpublished, unknown, or locally irrelevant.

One-line publication is admissible only if the facet definitions and tests remain legible.

#### C.2.LS:16.2 - Partial-profile rule
A partial profile is admissible only when omission is explicit. Publishing `AE` and `CD` while deferring `LanguageStateAnchoringMode` is acceptable; silently omitting it and then speaking in scalar prose such as "early" or "ready" is not.

If only one facet is published, either explain why the others are not included in the current note or point to the note where they are already published.

#### C.2.LS:16.3 - Overlay discipline
Local overlays such as "explicit-but-open", "trace-heavy", or "operator-tight" are admissible only when they dock to explicit facet refs. Overlays remain secondary to the declared profile and must not replace the facet bundle.

### C.2.LS:17 - Cross-Facet Reading Rule

#### C.2.LS:17.1 - No master-facet reading
Do not infer the whole language-state profile from one facet. High `AE` does not entail high `CD`; strong `AM.OperatorLoop` does not fix `AE` or `CD`; symbolic representation does not entail high `F`; low `CD` does not imply low operational consequence.

#### C.2.LS:17.2 - Threshold interaction rule
When a threshold is expressed over one facet, say whether the other facets are merely informative or also constraining. A Context may allow entry into `B.5.2.0` once `AE` suffices for an explicit open question while still capping `CD` so rival answers remain live; it may allow entry into `A.6.P` at `AE3+` while still capping `CD` so the move remains exploratory rather than endpoint-binding.

#### C.2.LS:17.3 - Transition reading rule
Read profile transitions facetwise. A note may become more explicit without becoming more closed, more document-mediated without changing closure, or more symbolic without becoming more formal. `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, and `B.5.2.0` should therefore cite the facet transition that actually justifies the move.

### C.2.LS:18 - Review Matrix and Migration Tests

#### C.2.LS:18.1 - Review matrix
An assurance reader should ask:

- does each published facet keep the definition and test supplied by its own pattern rather than by surrogate prose;
- does any overlay smuggle a hidden scalar or gate decision;
- are threshold claims tied to the facet that really bears them;
- do cited moves in `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, or `B.5.2.0` actually match the facet bundle;
- if the profile crosses a Bridge or viewpoint boundary, did the author use `F.9` for the Bridge, bounded-use claim, and loss account, and keep any optional F.9.1 stance note separate rather than importing it as a fake facet?

#### C.2.LS:18.2 - Migration test for source prose
Source phrases such as "still immature", "not ready yet", or "already stable enough" should be unpacked into: which facet is claimed, which anchor or bundle member justifies it, which threshold or route consequence follows, and which cited rule or external `authoritySourceRef` justifies that consequence.

#### C.2.LS:18.3 - Comparative profile use
Compare profiles facetwise unless a Context has published an explicit local aggregation for reporting. Such an aggregation remains secondary and must not replace the profile in norms, thresholds, or bridge claims.

### C.2.LS:End

