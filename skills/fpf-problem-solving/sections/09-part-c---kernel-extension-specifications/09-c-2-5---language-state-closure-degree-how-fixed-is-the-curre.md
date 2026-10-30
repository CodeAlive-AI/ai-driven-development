## C.2.5 - Language-State Closure Degree — How Fixed Is the Current Candidate Space?

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state closure degree.

**Use this pattern when.** Use C.2.5 when a governed `U.Episteme` publication must say how fixed its candidate space, route space, or frame space has become before endpoint use, reopening, or retreat.

**What goes wrong if missed.** A confident tone is mistaken for closure, closure is mistaken for truth or gate authority, or a closure drop leaves readers unable to tell which endpoint uses and route commitments remain supported.

**What this buys.** A separate ordinal characteristic for closure degree, so teams can distinguish exploration, stabilization, selected route, guarded fixation, and admissible retreat without collapsing closure into formality, articulation, warrant, or obligation.

### C.2.5:1 - Problem frame
A governed `U.Episteme` may already be explicit enough for publication while its declared position claim remains intentionally open to rival routes or frames. The declared language-state chart over `U.CharacteristicSpace` therefore needs a separate pattern defining the closure-degree basis slot: how fixed or closed the current candidate space has become.

### C.2.5:2 - Problem
Closure is often hidden inside vague words such as "ready", "settled", or "open". When closure is not explicit, teams cannot reason cleanly about reopen, sketch-backoff, or the admissibility of endpoint docking.

### C.2.5:3 - Forces
| Force | Tension |
|---|---|
| **Commitment vs exploration** | Preserve open search without losing auditability. |
| **Stability vs reversibility** | Allow closure increases, but also admissible reopening and reframing. |
| **Authority vs explicit retreat** | Let strong closure matter, but keep visible the moves that relax it. |

### C.2.5:4 - Solution
Language-state closure degree (`CD`) characterizes how firmly a specified candidate space is fixed in the position expressed by an episteme for a named use. The candidates may be answers, frames or possible next moves. Identify which choice is being assessed and which alternatives remain live. The ordinal Scale in :4.2 describes the progression from open exploration to stronger fixation.

#### C.2.5:4.0a - Characteristic, reading and assessment

Closure degree is the Characteristic; `CD0`–`CD5` name values on its ordinal Scale. A reading attributes a supported value, or a set of remaining possible values, to an identified episteme edition within a stated assessment scope and receiving use. A language-state chart binds the Characteristic and Scale in a slot under A.19. The Characteristic, its Scale values, a reading and the chart slot remain distinct under A.18/A.19.

A closure assessment states the actual fixity and its grounds. Claims about a binding route commitment, gate or authority relation follow their own rules and case facts. A note or C.2.LS profile can express the closure assessment; its reusable form and the filled assessment remain distinct.

#### C.2.5:4.5 - Recover the choice before assigning a level

Name the question or choice whose candidate space matters. Recover the live alternatives, any selected route or frame, and the reason that limits further choice. State the scope of that fixation and what would justify reopening it. The different sources of narrowing in :16.2 determine what must be reconsidered when conditions change.

Use that ordinary account directly when it supplies the receiving decision's condition. Assign a `CD` reading when the work needs comparison on this Scale, a chart position or a test against a declared threshold. Match the actual narrowing and reopening conditions to :4.2; retain an unresolved reading when the available grounds do not establish them. A level does not replace the surviving alternatives or the reason for their treatment.

The Scale's order describes greater fixity, not a universal improvement. Inquiry may need several alternatives kept live; a particular operational use may need one route fixed under a separately justified rule. C.2.4 assesses how explicit this content is. Writing out the alternatives and the decision rule can improve articulation without changing closure. New evidence or a changed use can instead reopen one choice while other commitments remain fixed. Preserve the supported observations and surviving choices, then revise only the conclusions affected by the change, using A.16.2 when a publication move is needed.

#### C.2.5:4.1 - Characteristic specification
- **Assessed subject:** the identified episteme edition, with the candidate space, assessment scope and receiving use stated.
- **Scale discipline:** ordinal.
- **What rises:** the candidate space or selected route becomes more fixed for the named use. Any binding force comes from its separately established rule.
- **What does not follow automatically:** truth, trust, formality, or quality.

#### C.2.5:4.2 - Starter anchor set
| Anchor | Reading | Typical interpretation for use |
|---|---|---|
| `CD0` | exploratory-open | broad rival space remains live |
| `CD1` | weakly stabilized | some contrasts are present, but rival routes remain normal |
| `CD2` | narrowed candidate space | explicit rivals remain, but the field is meaningfully reduced |
| `CD3` | selected route or framing | one route is chosen, though reopening remains routine |
| `CD4` | publication- or operation-fixed under guard | changes require named justification |
| `CD5` | strongly fixed | relaxation requires an explicit `A.16.2` move and governance note |

#### C.2.5:4.3 - Non-collapse rules
`LanguageStateClosureDegree` is not:

- `F`;
- articulation explicitness;
- gate decision;
- evaluator confidence;
- warrant strength.

A text may be highly explicit but low-closure, or low-explicitness but already high-closure by policy. Those states shall not be collapsed.

#### C.2.5:4.4 - Change discipline
Increasing `CD` requires narrowing candidate space, route space, or frame space explicitly. Lowering `CD` is admissible only through a named move such as `reopen`, `sketchBackoff`, or `respecify`, with a retained-witness and discarded-assumption note.

An ordinary PatternID in `governingPatternRef` locates the FPF rule relevant to the closure claim. Use a separate `relationFunctionClaimRef` for its exact defining or constraining `ClaimGraph` only when admissible interpretation, comparison, migration, publication, or reuse depends on that exact rule identity (`E.10`, `E.4.PFR`). Use `authoritySourceRef` when a non-pattern source carries the relevant authority.

### C.2.5:5 - Archetypal Grounding
**Tell.** Two notes may look equally explicit, but one is still intentionally open while the other is already committed to a single route.

**Show (System).** An incident cue can be routed to rollback while remaining reopenable if new evidence arrives.

**Show (Episteme).** A hypothesis sketch can be highly articulated but still low closure because rival explanations remain live.

### C.2.5:6 - Bias-Annotation
Explicit closure takes description work; it makes the remaining rivals and grounds of fixation recoverable.

### C.2.5:7 - Conformance Checklist
- `CC-C.2.5-1` Closure **SHALL** be declared independently from `F` and `AE` when it matters for routing, docking, or reopening.
- `CC-C.2.5-2` Reopen/backoff moves **SHALL** cite the prior closure state they are relaxing.
- `CC-C.2.5-3` Strong-closure states **SHOULD** name the guard, `governingPatternRef`, or `authoritySourceRef` that makes the closure binding.
- `CC-C.2.5-4` A closure drop **SHALL NOT** silently preserve an endpoint-use claim when the supporting route or publication form no longer supports it.

### C.2.5:8 - Common Anti-Patterns and How to Avoid Them
- **Closure by mood.** A sentence sounds decisive, so teams assume high closure. State the actual fixation and its grounds; add a `CD` reading when the receiving use needs that scale.
- **Irreversible drift.** Closure rises informally but no reopening condition exists. Use `A.16.2`.
- **Authority smuggling.** High closure is treated as if it were automatically a gate or obligation. Check the applicable gate condition for a gate claim; use `A.2.8` to check whether the claimed obligation obtains.

### C.2.5:9 - Consequences
The benefit is admissible handling of stabilization, commitment, and reopening. The trade-off is more explicit state declaration and more explicit retreat records.

### C.2.5:10 - Rationale
Closure describes how fixed the candidate space is; articulation describes how explicit its meaning is. `A.16.0` and its related patterns can use both when each affects the move condition.

### C.2.5:11 - SoTA-Echoing
The facet aligns with iterative design, open-world reasoning, and exploratory search practices where closure is a governance choice rather than a hidden by-product.

### C.2.5:12 - Relations
- Builds on: `A.18`, `C.2.2a`, `C.2.LS`.
- Coordinates with: `C.2.4`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`.
- Constrains: reopen, backoff, and endpoint docking guards.
### C.2.5:13 - Worked Examples and Retreat Cases

#### C.2.5:13.1 - Explicit but still open
The constructed `Pump-alert-21` in C.2.LS:13.1 makes its diagnostic question and the contrasting implications of three alternatives explicit. It has `AE4` for that question and `CD1` because all three alternatives remain live. When an accepted reference-gauge reading excludes one alternative, the candidate field narrows to `CD2`; neither remaining route is selected. The question remains fully articulated at `AE4`.

A practitioner choosing the next diagnostic question can use the stated alternatives and observations directly. A chart or comparison that needs both Scales can use the separate readings. The full case supplies the observations and discrimination rule; the two levels alone would not justify excluding a candidate.

#### C.2.5:13.2 - Strong closure under policy guard
An operator rule may be only moderate in `AE` but high in `CD` because policy already fixes the next step under the current horizon. This shows why closure is governance-facing, not merely stylistic.

#### C.2.5:13.3 - Reopen case
A route may move from `CD4` back to `CD2` when counter-evidence appears. Record the counter-evidence and the retreat as an admissible `A.16.2` move.

### C.2.5:14 - Authoring and Review Guidance

#### C.2.5:14.1 - Author prompt
To assign `CD`, ask:

- how many rivals remain live?
- is one route merely preferred, or actually fixed?
- if the closure is binding, what applicable guard, `governingPatternRef`, or `authoritySourceRef` makes it so?
- what would count as an admissible reopen trigger?

#### C.2.5:14.2 - Review prompt
An assurance reader should identify the actual narrowing and its source under :16.2, including a policy or protocol when it fixes the route. Confident tone or an appeal to hierarchy alone does not establish that fixity.

#### C.2.5:14.3 - Governance note
Whenever a claim about a gate, commitment, or endpoint use depends on `CD`, the supporting guard, `governingPatternRef`, or `authoritySourceRef` should be visible.

### C.2.5:15 - Extension and Migration Notes

#### C.2.5:15.1 - Local anchor refinement
Contexts may refine the starter closure anchors, but shall keep the ordinal progression and the explicit link to reopen/backoff discipline.

#### C.2.5:15.2 - Migration from readiness language
When routing, endpoint use or reopening depends on words such as "settled", "closed", "final", or "open", recover the claimed fixity and its grounds. Use an explicit `CD` reading when that scale is needed and a named `A.16.2` move when the closure changes. Sufficient ordinary wording needs no separate level solely to repeat it.

#### C.2.5:15.3 - Boundary reminder
`CD` is not warrant strength and not a gate decision. It speaks only about the local fixity of the current episteme or publication position and its candidate space.
### C.2.5:16 - Closure Publication Package Discipline

#### C.2.5:16.1 - Minimal closure package
A publishable `CD` claim should name what has narrowed:

- the rival routes or frames that remain live;
- the route, frame, or interpretation that is currently privileged or fixed;
- any guard, `governingPatternRef`, `authoritySourceRef`, or policy that makes the narrowing binding;
- the condition under which an admissible reopen or backoff would occur.

A bare claim such as "now settled" is insufficient when closure affects routing or authority.

#### C.2.5:16.2 - Narrowing-source rule
Closure may rise because evidence eliminates rivals, governance temporarily binds a route, or protocol requires fixation under time pressure. State the source of narrowing because different sources imply different reopen expectations.

#### C.2.5:16.3 - Partial-closure rule
Closure may be local rather than global. A note can be closed enough for one route while remaining open about broader explanation or classification; a prompt may be fixed enough to hold one question steady while still open enough that rival answers remain live. Publish that locality explicitly.

### C.2.5:17 - Continuing and Withdrawn Authority Handling

#### C.2.5:17.1 - Authority retention rule
If higher `CD` carried endpoint expectations, guard claims, or route commitments, a closure drop must say which consequences remain and which are withdrawn. Treat any actual authority-relation change separately under its direct pattern, as required by `A.16.2`.

#### C.2.5:17.2 - Admissible retreat record
An admissible retreat through `reopen`, `sketchBackoff`, or `respecify` should retain:

- the prior closure state;
- the reason the prior fixation no longer holds;
- the assumption or route being relaxed;
- the still-binding remainder, if any.

This prevents false continuity after retreat.

#### C.2.5:17.3 - Closure versus obligation boundary
High `CD` may coexist with obligations. When prose treats "closed" as "must now be done", use `A.2.8` to identify the duty bearer, duty, and instituting rule and basis; retain the applicable `governingPatternRef` or `authoritySourceRef` for that obligation claim.

### C.2.5:18 - Review Matrix and Reopen Tests

#### C.2.5:18.1 - Review matrix
An assurance reader should ask:

- what was narrowed;
- what evidence, choice or applicable rule supports that narrowing, with a `governingPatternRef`, `authoritySourceRef` or guard when one is used;
- what would reopen it;
- which gate, release, work, evidence-use, assurance, policy, or adjudication claims depend on the stated closure conditions and remain supported;
- whether the publication distinguishes local closure from whole-case finality.

#### C.2.5:18.2 - False-finality test
When a receiving action relies on "final", "settled", or "decided", check the actual scope and source of fixation and any applicable guard. A final-sounding word alone does not establish those conditions.

#### C.2.5:18.3 - Cross-facet reminder
Assess articulation under C.2.4 and representation under C.2.7 independently of closure. Source, evidence, access and action conditions retain their separate claims under C.2.6.

#### C.2.5:18.4 - Split-closure review case
A publication may be closed enough for immediate local work use or reliance use while remaining open about broader explanation, long-horizon consequences, or alternative classification. Allow the split when locality is explicit; reject prose that advertises whole-case finality when only one language-state segment is fixed.

### C.2.5:End
