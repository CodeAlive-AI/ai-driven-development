## C.2.LS - Language-State Facet Profile: Publish Readings and Use Conditions Together

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state facet profile.

**Technical alias.** `LanguageStateFacetProfile` names the optional record form below. A filled profile is an assessment account governed by C.2.1.

**Use this pattern when.** Use C.2.LS when the next use of a published `U.Episteme` needs an explicit profile of selected language-state readings and local thresholds. Select the required formality, articulation, closure and representation readings, together with any source or use conditions needed to interpret or apply them.

**Sufficient result and non-use.** The profile can point to existing readings and include only the facets needed together. If ordinary wording, one direct facet reading or an applicable existing profile already serves the receiving use, use it without constructing another bundle.

**What goes wrong if missed.** Teams replace the facet profile with a maturity adjective such as `ready`, `raw`, or `stable`, then use that label to choose routes, decide whether to reopen, interpret Bridges, or make publication decisions. The label hides the actual facet values.

**What this buys.** A thin, decomposable profile bundle: each facet keeps the definition and tests supplied by its own pattern, while the profile gives authors, assurance readers, and integrators one place to publish a threshold-relevant language-state position.

### C.2.LS:1 - Problem frame
To publish or compare position claims in the language-state chart over `U.CharacteristicSpace`, collect the needed facet references and readings in one profile. This makes the readings and their contribution to a receiving threshold inspectable while each facet pattern supplies its own definition.

### C.2.LS:2 - Problem
When authors need several facet readings together, a vague maturity label can conceal their different contributions, or `F` can become their surrogate. That blocks admissible threshold publication, undercuts `A.16` move guards, and makes school-to-school bridge work harder than it needs to be.

### C.2.LS:3 - Forces
| Force | Tension |
|---|---|
| **Thin profile bundle vs practical coordination** | Keep the bundle small, but still give one stable place where the language-state facets are named together. |
| **Reuse vs duplication** | Reuse A.18/A.19 characteristic machinery and A.16 moves; use E.18 only for an independently selected TransformationFlowStructure. |
| **Local thresholds vs cross-context comparability** | Contexts need local thresholds, but the facet names must stay stable enough for bridge work and viewpoint bundles. |

### C.2.LS:4 - Solution
A language-state facet profile records the selected readings and use conditions about one identified episteme edition. Characteristic readings use the declared language-state chart over `U.CharacteristicSpace`; a separate relation account keeps its own predicates. Use C.2.2a:0 and :4.2–4.5 to select the needed facets, obtain readings and grounds, and identify any conditions used by the receiving action. The profile brings those results together. Its fields can refer to existing readings or to the source and use account supplied by C.2.6. A reading reference makes its Characteristic, Scale, value and assessment scope recoverable; a reference to a source or use claim makes the predicate, participants and grounds recoverable. Select the applicable fields from:

- `formalityRef` -> the expression-property assessment governed by `C.2.3`, including its selected basis and any justified local ordered summary
- `articulationExplicitnessRef` -> the articulation reading governed by `C.2.4`
- `languageStateClosureDegreeRef` -> the closure reading governed by `C.2.5`
- `languageStateAnchoringModeRef` -> the source, evidence, access or action-condition claims selected under `C.2.6`; cite their account or an explicitly defined local summary with its criterion
- `languageStateRepresentationFactorBundleRef` -> the selected representation-factor readings governed by `C.2.7`
- `thresholdRefs?` -> context-local threshold declarations over the named facets
- `routeNotes?` -> informative notes that help interpret routing or reopening decisions

`C.2.LS` therefore defines only the **profile bundle**; it defines neither an individual characteristic nor a trajectory. A formality assessment or representation-factor bundle can contain several Characteristics. If placed in a CharacteristicSpace, each of those Characteristics receives its own declared Scale and slot; the reference to the assessment is not itself a Coordinate. The C.2.6 account is likewise separate from those slots; a local summary needs its own declared Characteristic and Scale before it can supply a Coordinate. `A.18/A.19` supply characteristic semantics, `A.16` defines admissible moves, and `E.18` governs an independently selected TransformationFlowStructure.

#### C.2.LS:4.0a - Kind and profile-bundle boundary

The optional `LanguageStateFacetProfile` form expresses an ordinary C.2.1 assessment account. The episteme edition being assessed is its EntityOfConcern. Its claims give the selected readings under their chart and scope, their grounds, any required source or use conditions, and any thresholds used in the assessment. C.2.1 governs the account's identity; E.24.PUB governs its expression and publication. No additional profile individual or dependent U-kind is needed for this use.

Distinguish the **selection of facets** from the **filled assessment**. A selection identifies the Characteristics and Scales in the A.19 basis and any separate C.2.6 questions needed by the receiving use. The same selection can be used for several assessments, just as the same record form can express them. A filled assessment states readings about its identified episteme edition and scope; changing a reading or a stated relation changes that claim content even if every definition reference stays the same. A threshold predicate has its own by-value identity under A.19:5.1.8. Reusing readings with a different predicate requires a new evaluation of that predicate, while the readings can remain unchanged.

For reuse, recover the assessed edition, chart meanings, scope, readings and relied-on grounds from the profile or its applicable cited source. Recover a threshold or a separate source or action condition and its receiving use when the conclusion relies on it. Saying which of the selection, readings, threshold or whole assessment is being reused prevents an unchanged label from concealing changed content. Rearranging the same claims in a dashboard or table leaves their meanings available under the same account-identity rule.

**Choose direct readings or a shared profile.**

Use direct facet readings when they already provide the inputs for the receiving judgement. A shared profile is useful when several readings and their conditions must be interpreted, compared or reused together: the reader can recover their joint scope and see which of them a local threshold actually uses. This saves reassembling dispersed references. The profile adds no stronger warrant to the readings. Keep it partial when the task needs only part of the facet family, and reuse an existing applicable assessment rather than writing another.

#### C.2.LS:4.1 - Contribution boundary
`C.2.LS` defines only profile composition and requires the language-state facets to remain explicit and non-collapsed. It does **not**:

- redefine `F`;
- invent a universal formality progression or an undeclared local summary;
- redefine the scale semantics of `AE`, `CD` or the representation factors in `C.2.7`, or replace the direct predicates recovered through C.2.6;
- define reopen/backoff moves;
- define endpoint classification or bridge kinds.

#### C.2.LS:4.2 - Threshold publication discipline
Any threshold used to choose a next question, constrain an admissible move, or begin `A.6.P` recovery shall be published on explicit named facets in the profile. Do not describe hidden sub-levels of `F` when the real issue is articulation, closure, a source or use condition, or the representation-factor bundle. A required relation is tested under its direct predicate; only a declared Characteristic reading participates as a slot value in an A.19 threshold.

#### C.2.LS:4.2.a - Local profile-reading witness
For this pattern, a published facet profile is reviewable when:

- the assessed episteme edition, chart, scope, selected refs, readings and any relied-on source or use claims are explicit or recoverable from a cited applicable upstream publication;
- any threshold-bearing use names the facet whose threshold is being invoked;
- route notes or local overlays remain informative and visibly docked to the explicit facet bundle;
- and any claimed move, Bridge, gate state or downstream result retains its own governing definition and test.

A polished label, one strong facet, or one memorable route note does not by itself yield an admissible profile reading. The profile remains conformant only when the named facets stay explicit and decomposable.

#### C.2.LS:4.3 - Composite readings
A language-state judgement may be composite, but the composite shall be decomposable. For example, a cue may be:

- low `AE`,
- medium `CD`,
- derived from an identified trace, with any evidential use separately qualified,
- and representation-wise mixed rather than purely symbolic.

A conforming profile makes this decomposition visible rather than hiding it under one stage label such as "early" or "raw".

#### C.2.LS:4.4 - Corridor map note
`C.2.LS` participates in the current `Language-State & Semantic Routing Corridor`, but contributes only the thin facet-profile bundle. Readers who need one map of the full language-state pattern set should read the corridor note in `C.2.2a`.

That map does not change this boundary: `C.2.LS` still does not define cue preservation, route-bearing publication, prompt entry, or downstream endpoint use.

### C.2.LS:5 - Archetypal Grounding
**Tell.** A team may say a draft is "still forming" for different reasons. The profile lets the team identify whether the issue is low articulation, low candidate-space closure, an unavailable observation or use condition, or an unresolved representation-factor bundle.

**Show (System).** An operator alert note can have stable alert terms and structure and low closure, while participating in an operator acknowledgement-and-check procedure.

**Show (Episteme).** An inquiry note can be low articulation while reporting identified exemplars and observations.

### C.2.LS:6 - Bias-Annotation
Making selected facet readings explicit costs more than using one stage adjective. It lets the receiving reader test the actual threshold; retain the ordinary wording or existing reading when that already serves the use.

### C.2.LS:7 - Conformance Checklist
- `CC-C.2.LS-1` A language-state facet profile **SHALL** reference the patterns that define its facets rather than invent local unnamed factors.
- `CC-C.2.LS-2` `C.2.LS` **MUST NOT** redefine the C.2.3 assessment or conceal several expression properties in one undeclared rank.
- `CC-C.2.LS-3` Thresholds that matter for routing, reopening, or lexical repair **SHALL** be published on explicit facets.
- `CC-C.2.LS-4` Trajectory accounts that rely on facet profiles **SHOULD** reuse A.16 move kinds. Apply E.18 only to an independently selected TransformationFlowStructure; use E.18.2 when its mathematical description is needed.
- `CC-C.2.LS-5` Composite labels such as `early`, `settled`, or `ready` **SHALL NOT** stand in for the explicit facet bundle when those states matter operationally.
- `CC-C.2.LS-6` Composite readings, overlays, and route notes **SHALL** remain decomposable into named facets and **MUST NOT** behave as hidden master factors.
- `CC-C.2.LS-7` Profile references or notes **MUST NOT** replace the governing move, Bridge, gate or downstream rule. Cite the applicable rule when a proposed consequence depends on it.

### C.2.LS:8 - Common Anti-Patterns and How to Avoid Them
- **Shadow progression.** Treating `early/late` as a master scale. Split the judgement into the named facets.
- **Formality capture.** Letting `F` stand in for closure or articulation. Publish those facets explicitly.
- **Bundle inflation.** Turning the profile into a second `A.19`. Keep it thin and referential.
- **Opaque readiness.** Using words such as `ready` or `mature` without naming which facet justifies the claim.
- **Route-note capture.** Letting an informative route note act as a move rule, gate state, or endpoint rule. Keep route notes informative. Use `A.16` for admissible moves, the applicable pattern for a downstream definition or test, the applicable gate or Work pattern for those claims, and an `authoritySourceRef` only when an external authority actually supplies the rule.

### C.2.LS:9 - Consequences
The benefit is clearer source and rule references: early cue work, bridge annotations, and reopen moves can all refer to one explicit facet profile. The trade-off is more explicit profile authoring and threshold publication.

### C.2.LS:10 - Rationale
The profile brings together the references needed to interpret facet readings and test a local threshold. Each referenced pattern supplies the corresponding definition and test; the profile preserves their different contributions to the receiving judgement.

### C.2.LS:11 - SoTA-Echoing

**Source boundary.** The facet meanings and profile rules come from `A.18/A.19` and the neighboring FPF patterns. The external comparisons below contribute scoped conditions and publication distinctions.

| Claim need | Bounded comparison | Exact source | Use in `C.2.LS` | Disposition |
|---|---|---|---|---|
| Readiness claims should stay scoped instead of collapsing into one global adjective. | A profile can state scoped conditions and local thresholds rather than one blanket readiness label. | NIST AI RMF 1.0 (2023) | Require explicit facet-level thresholds and reject a polished profile label as a substitute for the facet values. | **Adopt/Adapt.** |
| A publication can keep several named description elements visible without making their container identical to those elements. | Architecture-description vocabulary distinguishes named elements and their correspondence in a published description. | ISO/IEC/IEEE 42010:2022 | Use this only as a narrow publication comparator; it does not establish the language-state facet ontology. | **Narrow comparator only.** |

**Local stance.** The useful bounded result is a small explicit facet profile with local thresholds and decomposable readings, not one maturity adjective or one route-coloured bundle label.

### C.2.LS:12 - Relations
- Builds on: `A.18`, `A.19`, `C.2.1`, `C.2.2a`, `C.2.3`, `E.24.PUB`.
- Coordinates with: `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `E.18`, `F.9` for any Bridge and bounded-use claim, and `F.9.1` only for an optional stance note about that claim.
- Constrains: language-state threshold publication and profile composition.
### C.2.LS:13 - Worked Examples and Composition Notes

#### C.2.LS:13.1 - Operator-facing early alert
In this constructed case, the console publishes `Pump-alert-21` for an operator comparing diagnostic alternatives before selecting a check:

> At sample t21, Pump P7 indicates 70 kPa, below its alarm threshold of 90 kPa: `p_indicated(P7,t21) < 90 kPa`. Which of sensor bias, low supply, or an open bypass explains this indication? Keep these three alternatives live until an observation distinguishes them.

For this comparison, the three candidates have these stated implications:

| Candidate | Distinguishing implication in this case |
|---|---|
| Sensor bias | An accepted independent reference gauge would read at least 90 kPa despite the indicated 70 kPa. |
| Low supply | The reference gauge would read below 90 kPa and the upstream pressure below 80 kPa. |
| Open bypass | The reference gauge would read below 90 kPa and the bypass would be open. |

Initially no reference-gauge reading, upstream-pressure reading, or bypass-state observation is available. The alert makes the contrasts explicit without excluding a candidate or selecting a diagnostic route. Its receiving use is comparison within this stated candidate field. The console connects the alert to the operator's acknowledgement and selection of the next diagnostic check.

The alert's code component uses eight indicator units in this order: `NORMAL`, `LOW_PRESSURE`, `HIGH_PRESSURE`, `LOW_FLOW`, `HIGH_TEMPERATURE`, `VIBRATION`, `SENSOR_FAULT`, `LINK_LOSS`. Exactly one unit is active at a time. The fixed decoder assigns the active unit its corresponding report label; `LOW_PRESSURE` denotes the alarm predicate above. Thus `[0,1,0,0,0,0,0,0]` denotes this low-pressure alert. For this code comparison, the local criterion calls an active-unit fraction at most `1/4` sparse and a greater fraction dense.

The profile states:

- its formality assessment covers the displayed alert condition and question: the pressure variables and units are defined, the threshold predicate is explicit, and the question and diagnostic contrasts are expressed in prose;
- `AE = AE4` for the initial diagnostic question, because its subject, indicated condition, alternatives, contrasting implications, and bounded receiving use give a complete branch-appropriate expression (C.2.4:4.2);
- `CD = CD1`, because the contrasts weakly stabilize the stated candidate field while all three alternatives remain live and no route is selected (C.2.5:4.2);
- the C.2.6 account states that the console connects the alert to the operator's acknowledgement and diagnostic-check selection; this action condition is separate from the chart readings;
- `RepresentationFactorBundle = {local, sparse, symbolic}` for the indicator-code component: one unit identifies the report, the active fraction `1/8` satisfies the stated local criterion, and the named units have an explicit decoding rule (C.2.7:4.1). These readings concern the code; assess the surrounding prose separately if its representation factors matter.

**Changed condition.** Suppose an accepted reference-gauge reading for the same sample t21 becomes available: 72 kPa. Under the stated case implications it excludes sensor bias, while low supply and an open bypass remain live. The meaningful reduction from three candidates to two supports `CD2`; it selects neither remaining route. The updated diagnostic question still has its complete expression, and the pressure vocabulary, alarm predicate, indicator code, and operator-loop connection are unchanged. Apply the receiving pattern's own conditions when choosing the next question, check, or endpoint use.

The alert has a complete question and still-open diagnostic alternatives. Its code factors and operator-loop connection answer different questions; no one facet replaces the others.

#### C.2.LS:13.2 - Research cue before lexical repair
An inquiry note reporting a mismatch noticed through bodily observation may state:

- low `AE`,
- very low `CD`,
- the observer, bodily observation and reported mismatch, with a trace reference if an instrumental observation also contributes,
- and representation-wise mixed because the cue is partly verbal, partly kinesthetic, partly exemplar-based.

Use the profile to identify what the next question still needs. `A.16.1` preserves the cue; `A.6.P` can recover an unclear relation, and `B.5.2` starts from an admissible `U.AbductivePrompt`. Apply the receiving pattern's conditions when choosing the move.

#### C.2.LS:13.3 - Architecture-description case
A viewpoint-bound note about the adequacy of an architecture description may state its constraints through explicit typed predicates, be moderately high in `AE`, still mid-level in `CD` and symbolic in its representation-factor bundle. Its C.2.6 account identifies the document edition and assertions used for the adequacy judgement. The profile keeps description-side adequacy distinct from system-side engineering quality.

#### C.2.LS:13.4 - Same `F`, different profile
Two notes may supply the same required expression properties and still differ sharply in articulation, closure, source and use conditions, and representation factors. One may be used in an operator's check procedure with diagnostic alternatives still open; another may assess a document's assertions with comparatively closed alternatives. The profile bundle keeps that difference visible instead of letting `F` behave like a master factor.

#### C.2.LS:13.5 - Reuse the selection while readings or thresholds change

In :13.1, the facet definitions and record form remain available after the reference-gauge reading arrives. The closure assessment changes from `CD1` to `CD2`; retain the assessed alert edition and the new grounds in the updated assessment. This is reuse of the facet selection with changed claim content, not reuse of the earlier closure reading.

Now consider two stipulated receiving rules for that same assessment. A diagnostic-comparison meeting requires an explicit question and contrasting alternatives; it can use the available `AE4` reading. An action-selection rule additionally requires a selected diagnostic route. `CD2` still leaves two alternatives live, so that rule's condition is not met. The same readings support these different conclusions because the receiving conditions differ. If both assessments publish their threshold conditions, their full contents differ; the common readings may be cited once. Neither rule changes what `AE4` or `CD2` means, and each applies only to the stated receiving use.

### C.2.LS:14 - Authoring and Review Guidance

#### C.2.LS:14.1 - For authors
When publishing a language-state facet profile:

1. start from the local authoring problem rather than from a memorized progression;
2. name the facet refs explicitly;
3. add threshold refs only when a threshold changes routing, repair, or another operative decision;
4. when a label such as "mature", "raw", or "ready" carries an operational claim, make the relevant facet readings and conditions visible.

#### C.2.LS:14.2 - For assurance readers
An assurance reader should ask:

- is any facet silently replaced by `F`?
- is a threshold published on an explicit facet rather than on a poetic surrogate?
- do route or reopen claims actually match the published facet bundle?
- do profile notes guide interpretation while preserving the definitions and tests supplied by the applicable patterns?

#### C.2.LS:14.3 - For integrators
Integrators should preserve the profile references. A local alias is acceptable when the underlying facet references remain recoverable and unambiguous.

### C.2.LS:15 - Extension and Migration Notes

#### C.2.LS:15.1 - Local extension rule
Contexts may extend the profile with local threshold refs, route notes, or additional descriptive aids, but they shall not add a new master facet that collapses the named facet set into one summary factor.

#### C.2.LS:15.2 - Migration from surrogate prose
When a stage label carries a claim used in routing, comparison or another decision, recover the readings and conditions it abbreviates. Examples include:

- "the episteme is still early",
- "the issue is not mature enough",
- "the note is ready",
- "the cue is still raw".

For that use, state the relevant readings or relation claims and their grounds, whether any relied-on threshold is met, and the governing rule for the resulting move. An ordinary description with no such operational claim needs no profile expansion.

#### C.2.LS:15.3 - Boundary reminder
Use the profile to refer to facet readings and applicable thresholds. Definitions and tests for moves, Bridges, Scales and bundles remain with their governing patterns.
#### C.2.LS:15.4 - Use a facet selection in an assessment

A record containing only references to facet definitions supplies a selection of Characteristics and any separate source or use questions to be answered. To use it for a position assessment, add or cite the required readings and relation claims, identify the episteme edition being assessed and state the assessment scope. Retain the definition references so the meaning of each reading remains recoverable.

### C.2.LS:16 - Profile Publication Package Discipline

#### C.2.LS:16.1 - Minimal publishable profile package
A publishable `LanguageStateFacetProfile` carries what its receiving use needs:

- the selected refs from :4, with the relevant readings or relation claims, stated here or cited;
- any threshold refs that substantively affect routing, repair, bridge interpretation, or review load;
- the relation to `F` when readers might otherwise treat `F` as a surrogate;
- any missing or unknown reading or unresolved source or use condition that could change the receiving judgement.

One-line publication is admissible only if the applicable facet definitions and tests, and the grounds of any relation claims, remain recoverable.

#### C.2.LS:16.2 - Partial-profile rule
A partial profile identifies its selected facets and any missing reading that could change the receiving judgement. Publishing `AE` and `CD` can suffice when a source or interaction condition is irrelevant to that use. When such a condition matters, state the relation and its grounds or the decision-relevant unknown under C.2.6:4.3. For an independently defined local Characteristic, use C.2.2a:4.2 for its reading and uncertainty.

One facet can be sufficient for the named use. Refer to other readings only when that use needs them; no note about irrelevant omissions is required.

#### C.2.LS:16.3 - Overlay discipline
Local overlays such as "explicit-but-open", "derived from trace T", or "requires operator acknowledgement" are admissible only when their meanings are recoverable from the readings or relation claims stated or cited in the profile. Overlays remain secondary to the declared profile and must not replace the facet bundle.

### C.2.LS:17 - Cross-Facet Reading Rule

#### C.2.LS:17.1 - No master-facet reading
Do not infer the whole language-state profile from one facet. High `AE` does not entail high `CD`; an operator acknowledgement condition does not fix `AE` or `CD`; symbolic representation does not establish the expression properties needed by the receiving use; low `CD` does not imply low operational consequence.

#### C.2.LS:17.2 - Threshold interaction rule
When a threshold is expressed over one facet, say whether the other facets are merely informative or also constraining. An applicable local rule may allow entry into `B.5.2.0` once `AE` suffices for an explicit open question while still capping `CD` so rival answers remain live; it may allow entry into `A.6.P` at `AE3+` while still capping `CD` so the move remains exploratory rather than endpoint-binding.

#### C.2.LS:17.3 - Transition reading rule
Read changes in the profile's readings and source or use conditions separately. A note may become more explicit without becoming more closed. Replacing direct access to an observation with access to its written report can leave closure unchanged while changing which check the recipient can perform. A representation may become more symbolic without adding the expression properties needed by its receiving use. `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, and `B.5.2.0` should therefore cite the change in a reading or in a source or use condition that justifies the move.

### C.2.LS:18 - Review Matrix and Migration Tests

#### C.2.LS:18.1 - Review matrix
An assurance reader should ask:

- does each published facet keep the definition and test supplied by its own pattern rather than by surrogate prose;
- does any overlay smuggle a hidden scalar or gate decision;
- are threshold claims tied to the facet that really bears them;
- do cited moves in `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, or `B.5.2.0` actually match the facet bundle;
- if reuse depends on distinct local meanings, was `F.9` used for the actual Bridge and its bounded-use claim, keeping any optional loss account or F.9.1 stance note separate from the facets;
- if viewpoint conformance is claimed, was it tested under `E.17.0`?

#### C.2.LS:18.2 - Migration test for source prose
When a receiving use depends on a source phrase such as "still immature" or "already stable enough", recover the claimed reading or relation, its grounds, any threshold or route consequence, and the cited rule that warrants that consequence. Add an external `authoritySourceRef` only when an external authority actually supplies the rule.

#### C.2.LS:18.3 - Comparative profile use
Compare profiles on the named facets. A missing reading leaves that facet's comparison unresolved. A reporting aggregate needs a declared local model and operations admissible for the actual Scales under A.18/A.19; publishing an aggregation rule alone does not establish that basis. The aggregate remains secondary and must not replace the profile in norms, thresholds, or Bridge claims.

### C.2.LS:End
