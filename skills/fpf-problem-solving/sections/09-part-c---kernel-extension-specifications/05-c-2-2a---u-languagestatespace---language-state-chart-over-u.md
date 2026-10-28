## C.2.2a - `U.LanguageStateSpace` - Language-state chart over `U.CharacteristicSpace`

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state space.

**Builds on.**
`A.19`, `E.10`, `F.18`.

**Used by.**
`C.2.LS`, `C.2.3`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `F.9.1`, `A.6.P`, `C.16.Q`, `A.6.A`.

**Use this pattern when.** A team is about to route, compare, or publish a note by calling it `early`, `ready`, or `settled`, and the next action depends on what is actually known.

**First question.** Which of the five aspects can change the next action—formality, articulation, closure, anchoring, or representation—and which readings or unknowns does that action need?

**What goes wrong if missed.** Teams flatten those five aspects, the grounds for judging them, and the publication lane into one maturity adjective. A polished document can then look ready although the claim is still open, or a useful early cue can be rejected because it is not yet polished.

**What this buys.** One small chart row that shows only the distinctions needed by the next action while keeping the episteme publication separate from its grounds, publication form and carrier.

### C.2.2a:0 - First useful chart

Start with the smallest row that can change the next action:

- the exact episteme publication being positioned;
- only the currently relevant facet values or supported sets of possible values; use intervals where the Scale admits them and mark a decision-relevant unknown as `unknown`;
- the grounds for those readings;
- any local threshold used by the named next action and whether the readings meet it, fail it, or leave the result undecided;
- publication form, face, or carrier only when that distinction changes interpretation, preservation, or the next action.

**Filled example.** `Pump-alert-17` is the alerting episteme publication being positioned. Its affected asset and discrepant reading are visible, but the claim structure is not yet complete; rival diagnostic routes remain open; the alert is anchored in the operator loop; and its representation mixes text with telemetry. Formality is omitted because the present routing decision does not depend on it. The grounds are trace `T-17` and operator note `N-4`. The local rule permits routing to the diagnostic-question seam once the affected asset and discrepant reading are explicit. Form, face, and carrier are omitted because none changes that decision.

**Non-use.** If an existing chart already supplies the applicable values and threshold for the same next action, cite it instead of publishing another row. If `early` or `ready` is only ordinary prose and no routing, comparison, publication, or threshold decision depends on it, leave it as ordinary prose rather than creating a governed position.

**Practical result.** The row tells the practitioner whether to continue, stop, or route the publication to the pattern that governs the next question; it does not itself authorize that action.

### C.2.2a:1 - Problem frame
In engineering, inquiry, operator, and management practice, teams often need to say where a governed `U.Episteme` publication currently stands before it has reached an endpoint subject pattern. That governed publication may appear through several cue-bearing, route-bearing, or endpoint-bound publication forms, but the chart claim remains about the governed `U.Episteme` publication rather than about a local alias or a carrier lane.

Reusable arrangements or notations for cue packs, routed cue sets, abductive prompts, typed route-bounded projection publications, partial normal forms, and endpoint records are publication forms. A completed cue or record can express the episteme being assessed; its arrangement does not determine its chart position. An MVPK face is a selected publication form under E.17; it remains separate from the episteme, publication occurrence and carrier under E.24.PUB. By contrast, a service disturbance, a model-vs-observation discrepancy, a bodily tension, a telemetry trace, a model output, or a carrier document may trigger, witness, or carry that episteme, but none of those is itself a coordinate in the space.

Practitioners still have to determine the relevant readings, any threshold used, the publication form needed and the claims those readings support. Labels such as `raw`, `early`, `settled`, or `ready` can hide these separate values and decision conditions.

### C.2.2a:2 - Problem
Without an explicit language-state chart:

1. teams collapse several facets into one maturity story;
2. `F` is silently misused as a surrogate for articulation, closure, anchoring, and representation factors;
3. thresholds are published as vague readiness statements instead of explicit facet conditions;
4. source phenomena, governed epistemes, publication forms, publication faces, and carriers are conflated;
5. bridge and endpoint work inherit under-described upstream states.

### C.2.2a:3 - Forces
| Force | Tension |
| --- | --- |
| **Multi-facet fidelity vs readable publication** | The chart must preserve several independent facets without becoming unreadable. |
| **Stable basis vs local thresholds** | Basis slots should stay stable across contexts, while thresholds remain context-local. |
| **Position semantics vs publication semantics** | A position claim is not identical to the source phenomenon, publication form, or carrier through which it is currently expressed. |
| **Comparability vs non-collapse** | Teams need to compare positions, but not by flattening them into one pseudo-scale. |
| **Bridge reuse vs local authority** | Cross-context work benefits from a stable upstream chart, yet each context keeps local threshold authority. |

### C.2.2a:4 - Solution
`U.LanguageStateSpace` is the cluster-local name for the declared language-state chart over `U.CharacteristicSpace` as disciplined by `A.19`.

It is not a second kernel state-space apparatus beside `A.19`. It is the particular declared `U.CharacteristicSpace` whose basis slots represent the selected language-state Characteristics. A profile containing several Characteristics expands into their separate slots; it is not one atomic Coordinate.

#### C.2.2a:4.0a - Kind and chart boundary

`U.LanguageStateSpace` is a dependent durable chart value under `U.CharacteristicSpace` and the episteme language-state boundary, not a new root state-space U-kind. Its identity is the declared characteristic-space chart for governed episteme publication positions. Here, the positioned episteme publication is the selected published `U.Episteme` edition being assessed; the E.24.PUB publication occurrence remains separate. Practitioners can publish or use the chart through score tables, publication forms, local route maps, and carriers, which remain distinct from the chart.

#### C.2.2a:4.1 - Core use
`U.LanguageStateSpace` gives FPF an explicit declared chart for answering five questions:

- which basis slots define where the governed episteme stands;
- what a position claim in that chart means;
- which thresholds are locally declared over those slots;
- what comparisons are admissible without cross-facet collapse;
- and how the same position claim stays distinct from the publication form currently expressing it.

#### C.2.2a:4.2 - Position reading under `A.19`
A language-state position is a partial, slot-explicit coordinate claim in the declared language-state `U.CharacteristicSpace`.

`ValueSet(Scale)` in A.19 is the full Scale domain. Publish each selected slot's reading as one value or as a supported set of remaining possible values within that domain. This set describes incomplete information about the slot's value. Use an interval only where the Scale admits it; state a decision-relevant `unknown` separately when the available information does not determine the needed reading. For anchoring, `{AM.TraceAnchored, AM.OperatorLoop}` can report two remaining possibilities; `AM.Mixed` instead requires identified component modes that both matter substantively (C.2.6:4.3).

`position` here abbreviates these slot-explicit `A.19` coordinate claims.

#### C.2.2a:4.3 - Facet basis
The language-state chart is coordinated by explicit facet subject patterns rather than by an informal master progression. Select the actual Characteristics and Scales needed for the next action from:

- `C.2.3` for the selected expression properties in a formality assessment, or an explicitly justified local summary;
- `C.2.4` for articulation explicitness;
- `C.2.5` for language-state closure degree;
- `C.2.6` for language-state anchoring mode;
- `C.2.7` for the language-state representation-factor bundle.

The selected basis slots together define the chart under A.19. Each actual Characteristic has its own Scale and slot. In particular, neither a formality profile nor a representation-factor bundle is silently treated as one Coordinate. `C.2.2a` does **not** govern the internal meanings or Scale semantics of those Characteristics.

#### C.2.2a:4.4 - Position, grounds and publication
Keep the positioned episteme publication separate from the grounds for its assessment and from its publication form and carrier:

- **positioned episteme publication** - the governed `U.Episteme` publication whose current position is being claimed;
- **grounds / witnesses** - disturbances, discrepancies, traces, model outputs, bodily tensions, exemplars, or contrasts that justify the current reading;
- **publication forms** - arrangements or notations used for publications such as cue packs, prompts, typed projections, partial normal forms and endpoint records; an MVPK face is a selected publication form, identified when that distinction matters;
- **carriers** - physical or digital media, such as a paper sheet, file or console display, that bear the selected form.

`U.LanguageStateSpace` governs only the coordinate reading of the position claim. Keep that claim distinct from its grounds, publication form and carrier.

#### C.2.2a:4.5 - Position publication rule

A published position states the exact episteme publication, the facet readings that matter to the present use, and the grounds for those readings. A decision-relevant unknown is stated as `unknown`; unrelated facets need not be filled merely to complete a form.

Add the local threshold and named next action only when the row is used for movement, routing, comparison, or endpoint entry. Add publication form, MVPK face, carrier, or SCR/RSCR lane only when that distinction affects interpretation, preservation, distribution, or the next action.

The position is reviewable when the named or inherited episteme publication, relevant readings, grounds, and any relied-on threshold are recoverable, and when any form, face, or carrier actually mentioned remains distinct from the positioned episteme publication. A polished note or better carrier does not by itself prove a new chart position.

#### C.2.2a:4.6 - Non-substitution of `F`
The formality assessment supplies the selected expression Characteristics, each with its own basis slot. A justified local summary may occupy one slot; a multi-property profile does not. These readings describe only the expression properties selected under C.2.3.

A conforming account shall not infer:

- closure from formality alone;
- anchoring from publication-face format alone;
- representation factors from articulation alone;
- or routing admissibility from a lone `F` statement.

Where operationally meaningful thresholds exist, they must be published on the relevant slots rather than being disguised as informal `F` sublevels.

#### C.2.2a:4.7 - Position versus publication form
A position claim states facet readings about the identified episteme. Witnesses provide grounds for those readings; a selected publication form, including an MVPK face, expresses the claim; a carrier bears that form. Changing the form or carrier does not by itself change a facet reading. Any later publication qualified under an endpoint subject pattern still needs that pattern's conditions.

#### C.2.2a:4.8 - Threshold publication discipline
If a threshold is used to justify a move or endpoint entry, that threshold shall be stated on explicit basis slots in the chart. Statements such as `this is now ready`, `this has matured`, or `this is still too early` are non-conformant when they substitute for undeclared slot conditions.

#### C.2.2a:4.9 - Comparison and bridge note

Positions may be compared directly only under one shared chart meaning and the applicable local comparison rule. When comparison or reuse depends on distinct local meanings, recover the two exact F.17 local senses and test the direct F.9 predicate. Cite a Bridge only when that predicate obtains. State the proposed bounded use and any reliance separately; a loss note is optional and belongs to that use, not to the fact that the contexts differ.

If no Bridge obtains, preserve both local positions. Name the actual comparison or translation relation needed by the receiving use, or return the applicable missing-governor result instead of inventing correspondence.

#### C.2.2a:4.10 - What changes after the row exists

Compare the relevant readings with the local threshold named by the next action. Use the result to decide whether to keep the publication where it is, route it through a seam or prompt pattern, open a facet or endpoint question, or stop because a required reading is unknown. The receiving pattern governs the actual route, comparison, or publication decision; the chart row supplies only the position facts that decision uses.

### C.2.2a:5 - Archetypal Grounding
**Tell.** One note can have operator-loop anchoring yet still low closure. Another can be document-mediated and symbol-heavy while still open on route choice. Both notes have positions in one language-state chart, but not on one maturity progression.

**Show (System).** A service disturbance is a system-side phenomenon. The positioned governed `U.Episteme` publication is the alerting episteme published from that disturbance. In `Pump-alert-21` (:13.2), its position combines declared observation terms and unit-bearing values, `CD1`, `AM.OperatorLoop`, and local/sparse/symbolic readings for the defined indicator code.

**Show (Episteme).** A model-vs-observation discrepancy is a witness-level tension, not the positioned episteme publication itself. Once preserved as a cue pack, the resulting governed `U.Episteme` may be low in articulation, low in closure, trace-anchored, and only partly symbolic even when rendered into prose.

### C.2.2a:6 - Bias-Annotation
The pattern favors separate facet readings over one stage adjective when a decision depends on them. Ordinary descriptions remain sufficient under the non-use boundary in :0.

### C.2.2a:7 - Conformance Checklist
- `CC-C.2.2a-1` `U.LanguageStateSpace` **SHALL** be treated as the declared language-state chart over `U.CharacteristicSpace`, not as a rival kernel space and not as a disguised `F` progression.
- `CC-C.2.2a-2` Published positions **SHALL** cite explicit facet subject patterns when those positions matter for movement, routing, or endpoint entry.
- `CC-C.2.2a-3` Position claims **SHALL** use slot-explicit values, supported sets of remaining possible values, or intervals admitted by the slot's Scale; uncertainty **SHALL NOT** be hidden inside stage words such as `ready`, `early`, or `mature`.
- `CC-C.2.2a-4` A position claim in the chart **MUST NOT** be conflated with the current ground, witness, publication form (including an MVPK face), or carrier.
- `CC-C.2.2a-5` Comparison or reuse that depends on distinct local meanings **SHALL** recover the two exact F.17 local senses and test the direct F.9 predicate. Cite a Bridge only when it obtains; keep the bounded-use claim, reliance, and any optional loss note separate. If it does not obtain, keep the local positions distinct and name the missing comparison or translation governor.
- `CC-C.2.2a-6` Corridor and navigation notes **MUST NOT** be read as relocation of facet, seam, bridge, or downstream subject-pattern semantics into the chart subject-pattern set.
- `CC-C.2.2a-7` If a position claim is used for routing, endpoint entry, or gate-adjacent reasoning, its relied-on threshold **SHALL** remain explicit or recoverable from the cited applicable upstream publication. The positioned episteme publication **SHALL** remain identifiable. Include form, MVPK face or carrier distinctions when they affect interpretation or the next action, as in :4.5.

### C.2.2a:8 - Common Anti-Patterns and How to Avoid Them
- **Maturity monism.** Replace five facets with one stage word. Repair by publishing explicit slot placement.
- **Formality capture.** Use `F` to stand in for articulation, closure, or anchoring. Repair by naming the actual facet subject pattern.
- **Carrier collapse.** Treat a document, cue pack, or routed note as if it were the position itself. Repair by distinguishing the position claim, publication form (including an MVPK face) and carrier.
- **Threshold folklore.** Speak of readiness without any explicit threshold declaration. Repair by publishing relevant local threshold notes on explicit slots.
- **Bridge by vibe.** Similar stage language is treated as equivalence. Recover the two exact F.17 local senses and test F.9; cite a Bridge only when its predicate obtains. Otherwise keep both positions local and route the actual comparison or translation question.
- **Corridor inflation.** Treat the navigation cluster or corridor map as if it were the subject-pattern set for all downstream semantics. Repair by naming the pattern that governs the current chart, seam, or downstream claim; identify any seam publication form separately.

### C.2.2a:9 - Consequences
Practitioners can state the language-state readings of a governed `U.Episteme` and their grounds without hiding them inside one maturity adjective. The trade-off is that publication must carry explicit slot and threshold information when decisions depend on it.

### C.2.2a:10 - Rationale
Language-state work needs one explicit statement of what this chart is before individual facet, move, and endpoint patterns start using it. Its declared basis and each facet's rule let readers interpret a position and test the threshold needed by the next action.

### C.2.2a:11 - SoTA-Echoing

The external comparisons below concern publication distinctions and scoped profiles. The chart basis remains grounded in A.19 and its facet patterns.

| Claim need | Practice contribution | Primary source | Alignment with `C.2.2a` | Adoption status |
|---|---|---|---|---|
| Complex technical state should be published through explicit views, viewpoints, and model distinctions rather than one implicit maturity word. | Contemporary architecture-description governance separates source architecture description, view, viewpoint, and correspondence evidence instead of letting one visible adjective stand in for the whole state. | ISO/IEC/IEEE 42010:2022 | `C.2.2a` keeps chart position, publication form and carrier distinct; an MVPK face is a form under E.17. A stage adjective cannot substitute for the required facet readings. | **Adopt.** |
| Governance-relevant readiness requires context-local profiles and thresholds, not one global adjective. | Current governance and risk frameworks use explicit profiles, thresholds, and scoped conditions rather than one blanket readiness label. | NIST AI RMF 1.0 (2023) | `C.2.2a` adopts the threshold-publication discipline and rejects the popular shortcut where `ready`, `early`, or `mature` replaces explicit slot conditions. | **Adopt/Reject-popular-shortcut.** |

**Architecture-description contribution.** Keep the position claim and the form and carrier through which it is published distinguishable when their identity changes interpretation or use.

**Characteristic-space and profile discipline.** The multi-facet chart is grounded in FPF `A.19` and the current `C.2.3`–`C.2.7` facet patterns; it is not imported from an external modeling language. Current governance practice contributes the narrower discipline of publishing scoped profiles and thresholds.

**Local stance.** The load-bearing architecture decision is FPF-native: governed language-state uses a multi-facet chart with explicit thresholds and the publication distinctions needed by the receiving use, not one maturity progression or one polished publication face. The external rows support the narrower view, publication, profile, and threshold disciplines stated above.

### C.2.2a:12 - Relations
- Builds on: `A.19`, `E.10`, `F.18`.
- Coordinates with: `C.2.LS`, `C.2.3`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `F.9`, `F.9.1`, `E.17.1`.
- Constrains: threshold publication, positional claims, and anti-collapse discipline across the language-state cluster.

### C.2.2a:13 - Worked Examples

#### C.2.2a:13.1 - Inquiry cue before endpoint capture
A position claim for a research cue note may state:

- `F`: the terms needed for the inquiry are defined, while the proposed inferences remain in prose,
- low articulation explicitness,
- low closure,
- `AM.EmbodiedFelt` or `AM.TraceAnchored`, according to the cue's actual anchor,
- and mixed representation factors.

Keep these readings explicit when testing entry into `A.6.P` or `C.25`; the note should remain upstream while the relevant receiving pattern's entry conditions remain unmet, even if its prose happens to look polished.

#### C.2.2a:13.2 - Routed operator alert note
Use `Pump-alert-21` from C.2.LS:13.1 to compare the three stated diagnostic alternatives before selecting a check. The alert names Pump P7, its indicated pressure of 70 kPa, the alarm condition `p_indicated(P7,t21) < 90 kPa`, and the contrasting implications of sensor bias, low supply, and an open bypass. Its chart readings are:

- `F`: the pressure variables and units are defined, the alarm predicate is explicit, and the question and diagnostic contrasts are expressed in prose;
- `AE = AE4`: the diagnostic question has the participants, conditions, and bounds needed for this comparison;
- `CD = CD1`: the three alternatives have explicit contrasts, but none has yet been excluded and no diagnostic route has been selected;
- `LanguageStateAnchoringMode = AM.OperatorLoop`: the alert is connected to the operator's console acknowledgement and diagnostic-check selection;
- `RepresentationFactorBundle = {local, sparse, symbolic}` for the alert's indicator-code component only: one of eight named units is active, the fixed decoder gives its report label, and the active fraction `1/8` meets the example's local sparse criterion. C.2.LS:13.1 supplies the unit order, decoder, and criterion.

If an accepted reference-gauge reading of 72 kPa for the same sample t21 excludes sensor bias under the stated case rule while the other two alternatives remain, update `CD` to `CD2`. The question remains fully stated and the code, expression properties, and operator-loop connection are unchanged. Keep the live responses explicit in the route-bearing seam publication. Before publishing an endpoint-subject-qualified work record or reliance record, test the applicable downstream pattern's conditions; these chart readings do not decide that result.

#### C.2.2a:13.3 - Viewpoint-bound adequacy note
A document-mediated adequacy note about an architecture description may state an explicit vocabulary and predicates for its claims, with articulation sufficient for the described comparisons, mid-level closure, document-mediated anchoring and symbolic representation. That position remains within the same language-state chart even though its carrier lane differs from an embodied inquiry cue.

#### C.2.2a:13.4 - Polished prose is not closure
A prose rewrite may look cleaner, more compact, or more manager-readable than the source cue and still remain low in closure or articulation explicitness. If the underlying slot values, uncertainty, and route plurality remain unchanged, then publication polish changes the rendering or carrier lane, not the chart position by itself.

### C.2.2a:14 - Position Publication Package Discipline

A publishable row contains the exact episteme publication, the decision-relevant facet readings or intervals, their grounds, and any local threshold used by the named next action. Add form, face, carrier, freshness, or inherited pins only when the receiving use relies on them.

Minimum self-check:

1. Does the row name the positioned episteme publication rather than a ground, form, face, or carrier?
2. Does it state every facet that can change the named next action and mark a relevant unknown as unknown?
3. Are the grounds and any relied-on local threshold recoverable?
4. Does the row say whether its readings meet the named action's threshold, fail it, or leave the result undecided, while the receiving pattern governs the action?
5. If the use depends on distinct local meanings, was F.9 tested on the two exact local senses rather than inferred from similar wording?

### C.2.2a:15 - Extended corridor map

After the first useful row is understood, the wider `Language-State & Semantic Routing Corridor` can be read as a distributed overlay over `C.2.2a`, `C.2.LS`, `C.2.4`–`C.2.7`, `A.16`, `A.16.0`–`A.16.2`, `B.4.1`, and `B.5.2.0`.

`A.16.1 / PreArticulationCuePack` is the earliest durable seam publication form in that corridor. `B.4.1` is the explicit route-bearing seam after cue preservation, and `B.5.2.0` is typed prompt entry. `C.16.Q`, `A.6.A`, `A.6.P`, `B.5.2`, `A.15`, and `C.25` are downstream subject patterns, not members of the language-state chart. The map explains navigation only; it relocates none of their semantics into C.2.2a.

### C.2.2a:End
