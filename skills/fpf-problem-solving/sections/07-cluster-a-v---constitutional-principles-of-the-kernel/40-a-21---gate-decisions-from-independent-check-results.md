## A.21 - Gate Decisions from Independent Check Results

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain name.** Gate decision.

**Technical result name.** `GateDecisionResult`.

### A.21:0 - Use this when

Use A.21 when a named gate must decide whether one bounded action or transition may proceed under an applicable profile rule. Identify every check that the rule requires, including the subject and criterion of each check.

**First useful move.** Name the action being decided, the profile rule that applies, and every required check result. Map each check result under that rule, then let the worst mapped value win.

**Quick worked case.** `WorkshopEntryGate-4` decides whether `CalibrationCycle-17` may start before 16:00. `WorkshopEntryProfile-E5` requires two checks: `CalibrationCertificate-44` for `TorqueWrench-12` is current under `CalibrationRule-E3`, and `WorkshopEnclosure-2` is closed under `EnclosureRule-E2`. Both checks are evaluated and satisfied, so each maps to `pass`; the gate returns `pass` and the cycle may start before 16:00. Recheck if the instrument, certificate edition, enclosure state, profile edition, or time window changes.

If the state of `WorkshopEnclosure-2` is unknown, that check remains `unknown`. `WorkshopEntryProfile-E5` maps the uncertainty to `block`, not to `abstain`, so the cycle stays on hold until the enclosure is checked. A different policy may accept a bounded uncertainty only through an explicit rule that names the subject, tolerance, consequence, and validity window.

**Short boundary.** A gate decision is neither work-entry readiness nor performed Work. Use `A.15.5` for the ordinary readiness question. If Work later occurs, identify it through the A.15 family; do not treat the gate, plan item, or prospective claim as that later Work.

**What goes wrong if missed.** A green display is mistaken for permission, an unknown required check disappears as a neutral value, two different check subjects are merged by label, or a new path slice is treated as authority to weaken policy.

**What this buys.** The practitioner can recover what was decided, which rule applied, which facts supported the decision, what action follows, and when the decision must be made again.

**Not this pattern when.**

- Use `A.20` for one internal-constraint result.
- Use `A.15.5` for full-kit or work-entry readiness without a gate decision.
- Use `E.18` for transformation-flow positions, paths, slices, and structural crossings.
- Use the pattern that defines the policy, safety rule, regulatory rule, evidence claim, channel condition, or system-role claim for the truth of that check.
- Use `E.17` only when the decision is published through a form or carrier.

### A.21:1 - Problem frame

A gate combines results defined elsewhere. A.20 may report an internal constraint; A.10 or B.3 may support an evidence or assurance check; E.18 may establish a structural crossing; a regulatory or safety pattern may define another criterion. A.21 does not redefine those truths. It records how one applicable profile maps their results to one bounded decision.

The gate is optional. A guard, dashboard, readiness label, plan item, path boundary, or publication form does not create a gate decision by resemblance.

### A.21:2 - Problem

How can one gate decision remain reproducible without:

- losing the identity and result of each check application;
- treating not applicable, not run, unknown, and policy consequence as one value;
- allowing a missing required result to vanish beside a passing result;
- inferring policy selection or weakening from a `PathSlice` boundary;
- requiring semantic-Bridge, publication, replay, crossing, or LaunchGate apparatus for an ordinary local decision; or
- turning a prospective work-entry question into a future Work individual?

### A.21:3 - Forces

| Need | Tension |
| --- | --- |
| One usable decision | The practitioner needs one action, while every contributing result must remain recoverable. |
| Order independence | Evaluation order should not change the decision, but early failure may justify deferring expensive work. |
| Policy flexibility | Different profiles may react differently, but no implicit default or path boundary may supply policy authority. |
| Plain entry | “Worst result wins” is easy to use, while exact result and rule identities are needed for replay. |
| Conditional assurance | Crossing, publication, regulation, safety, and reuse can need more evidence, but ordinary local use should stop earlier. |

### A.21:4 - Solution

#### A.21:4.1 - The decision result

`GateDecisionResult` is a C.2.1 result episteme. Its EntityOfConcern is the bounded action or transition being decided. Its ClaimGraph says that one identified profile application maps one complete effective set of check-application results to one decision and action consequence.

Minimum content:

```text
GateDecisionResult:
  resultId
  gateRef
  decisionSubjectRef
  boundedActionRef
  profileApplicationRef
  requiredCheckApplicationIds[]
  optionalCheckApplicationIds[]
  checkApplicationResultRefs[]
  scope
  qualificationWindow
  decisionValue: abstain | pass | degrade | block
  actionConsequence
  recheckCondition
  rationale
```

`decisionSubjectRef` names the proposal, transition, crossing, or prospective work-entry claim being decided. `boundedActionRef` names what the practitioner may do or must hold. Neither identifies a later Work occurrence.

One result is identified by the tuple containing the gate, decision subject, bounded action, profile application, canonical required and optional check-application identity sets, scope, and qualification window. A changed rule edition, checked subject, criterion, case, result, scope, or window requires another result. The decision value and rationale are the content derived for that fixed tuple; a contradictory value for the same tuple is an error, not another result to merge.

The rationale links every check-application result to its mapping rule and then to the aggregate and action consequence. A `GateDecisionExplanation` may restate that rationale in ordinary language; it is optional, carries no decision value, and cannot replace the result or rationale.

#### A.21:4.2 - One check application

A `GateCheckApplicationResult` is a C.2.1 result episteme that keeps the gate-facing use of one source result recoverable:

```text
GateCheckApplicationResult:
  checkApplicationId
  checkKind
  checkedSubjectRef
  criterionRef
  criterionEdition
  ruleApplicationRef?
  caseFactsRefOrValue
  scope
  qualificationWindow
  requirement: required | optional | notApplicable
  evaluationState: evaluated | notRun
  sourceResultRef?
  sourceOutcome?
  mappingRuleRef
  mappingRuleEdition
  mappedDecisionValue?: abstain | pass | degrade | block
  witnessOrReasonRefs[]
```

The pattern that defines or tests the source claim determines `sourceOutcome`; A.21 only applies the cited mapping rule. A not-applicable application states why the criterion does not apply. A not-run application states that evaluation work did not produce a result. Unknown, error, violation, and success keep the meanings supplied by their source patterns.

The application identity includes the checked subject, criterion and edition, applicable rule application, case facts, scope, and window. Two `SystemRoleFit` applications for different Systems and two `RegulatedConformance(X)` applications for different regulators or rule editions are different applications. Deduplicate only genuinely identical application results. If two copies claim different source outcomes for the same identity, stop and resolve the contradiction; do not join them by `checkKind`.

When a publication or selected structure needs a short `GateCheckRef`, that value refers to one identified `GateCheckApplicationResult`. It is not the old `{aspect, kind, edition, scope}` record and cannot omit the checked subject, criterion or rule application, case, scope, or window needed to resolve that result.

#### A.21:4.3 - Profile application

A `GateProfile` describes a policy. It does not show that the policy applies. Every gate decision points to the current application of one profile rule. That application identifies:

- the profile rule and edition;
- the gate, decision subject, and bounded action to which it applies;
- its scope and qualification window;
- the complete required and optional check set;
- the mapping rule for each applicable source outcome;
- the consequence attached to each aggregate decision; and
- any separately required authority or responsibility relation.

A.21 has no implicit default profile. A branch name, `PathSlice`, sentinel, publication mode, product label, or earlier decision does not select or authorize a profile. A new slice may bound changed data or trigger reevaluation; it cannot weaken inherited safety, regulatory, evidence, or other obligations. Any weakening needs another current rule application that permits it and any authority relation required for that change.

#### A.21:4.4 - Complete check set and independent results

Before aggregation, recover the complete effective required set from the profile application. Every required application is present even when it is `notRun`, `unknown`, `error`, or failed.

- `notApplicable` is allowed only when the application gives its scope or applicability reason.
- `notRun` never becomes `abstain` or `pass`.
- `unknown` and `error` remain visible before their explicit profile mapping.
- a failed A.20 result can prevent passage but cannot make freshness, channel, role-fit, regulatory, crossing, or another independent check inapplicable.
- evaluation work may defer an expensive check after a blocking result, but the deferred required check remains `notRun` in the result.

If a profile deliberately accepts known uncertainty, its mapping rule names the checked subject, tolerated uncertainty, permitted bounded action, consequence, and expiry or recheck condition. A generic neutral fold is insufficient.

#### A.21:4.5 - Aggregate and action meaning

In ordinary language: **the worst mapped result wins**. Only after every required application is present and its mapping is known, the technical aggregation is the order-independent join:

`abstain <= pass <= degrade <= block`.

The join is associative, commutative, and idempotent. `abstain` is neutral and `block` absorbs other values, but those algebraic properties do not change the source results.

| Decision | Meaning for the bounded action |
| --- | --- |
| `abstain` | The applicable profile says this gate makes no decision for this action and names the remaining decision route or absence of one. It grants no permission. It is not used for missing, unknown, failed, or unrun required checks. |
| `pass` | Every required application is present and the current profile accepts the bounded action without an added restriction, within the stated scope and window. |
| `degrade` | The profile accepts only the named restricted or conditional form of the action. The result states the restriction, stop or exit condition, and recheck condition. It is not an unspecified “proceed carefully”. |
| `block` | The profile refuses or holds the bounded action under the current facts and states what change or new result can reopen the decision. |

An optional application affects the aggregate only when the cited profile rule says it does. A required missing or `notRun` result can map to `degrade` or `block` under an explicit rule, never to `pass` or neutral `abstain`.

#### A.21:4.6 - Scope, composition, and change

Compose check sets only through the exact profile applications that cover the decision subject and scope. A more specific application may add, replace, or remove a check only when its policy rule and applicability fact say so. Preserve parameterized identities such as regulator X and its rule edition.

`lane`, `locus`, `subflow`, and `profile` may be used as scope values only when the selected structure or policy defines the corresponding boundary for this application. A scope label alone neither selects a profile nor merges check applications.
Recompute the result when the decision subject, bounded action, profile application, required set, check application identity or result, scope, or window changes. A refresh, edition bump, expired evidence window, changed crossing, or changed path slice matters only when it changes one of those inputs under its own pattern.

#### A.21:4.7 - Optional LaunchGate use

Use `LaunchGate` only when an A.21 gate-decision relation is current for one prospective `workEntryClaimRef`, WorkPlan or PlanItem entry question, and bounded attempted action. The gate refers to that prospective claim; it never targets a not-yet-existing Work individual.

`A.15.5` remains the ordinary route for full-kit and work-entry readiness. Add a LaunchGate only when the selected transformation-flow structure actually contains that gate use. Freshness, design-run-tag consistency, A.20 ingress validity, structural crossing, and SquareLaw are checks only when their exact claims, rules, and defining patterns are current. No one of them is mandatory merely because the word “launch” appears.

If a required ingress A.20 summary is not `satisfied` and the applied profile defines a pre-run barrier, the aggregate is `block`. Other available results remain visible; deferred checks remain `notRun`.

#### A.21:4.8 - Crossing and semantic-Bridge boundary

For a structural crossing, receive the exact changed-binding and crossing facts from E.18. Add a crossing check only when its criterion applies. SquareLaw is required only when the E.18 crossing rule for that case requires it.

A structural crossing does not imply an F.9 semantic Bridge. Add an F.9 Bridge, bounded-use claim, reliance, optional Bridge Card, or optional `CL` only when the separate semantic-correspondence relation and downstream use obtain. A non-crossing gate carries none of this apparatus. Do not encode absent Bridge material as mandatory fields with `none` values.

#### A.21:4.9 - Guards and check families

A guard event is not automatically a GateCheck. When a selected structure assigns a guard failure to a gate, the current profile may consume that identified event through a declared check application and mapping rule.

The following names are recognition aids, not a universal catalogue: freshness, design-run-tag consistency, reference-plane crossing, comparator constraints, evidence completeness, safety envelope, regulator conformance, system-role fit, channel fit, equivalence preservation, outflow audit, and snapshot consistency. Each application names its checked subject, criterion, rule edition, case, and source result. Use A.10 or B.3 for evidence and assurance truth, A.2 and C.3.2 for system-role classification, A.2.1 and F.6 for exact assignments, A.2.6 for channel claims, and E.18 plus the comparison patterns for crossing and comparator claims.

#### A.21:4.10 - Publication, rationale, and reuse

The ordinary one-time result needs the fields in section 4.1 and a short rationale. It does not require a Multi-View Publication Kit (MVPK) face, AssuranceLane, evidence bundle, Bridge apparatus, cache key, or equivalence witness.

When publication is current, E.17 defines the publication form and carrier relations. A publication mode changes only that form; it neither selects a profile nor changes the required check set or aggregate. The published minimum is the result identity, decision subject, profile application, check-application refs, decision, action consequence, scope, window, and recheck condition. Crossing, evidence, regulation, safety, and assurance fields appear only when the corresponding claim is current.

A `DecisionLog` is an optional audit or reuse record that cites one or more `GateDecisionResult` values. It may retain source outcomes, mappings, rationale, evidence refs, and change history; it neither creates nor changes the decision.

Require an equivalence witness only when reuse, cacheability, or a stability interval is claimed. That witness covers every input whose equality is needed for the claimed reuse. A changed profile edition, required set, checked subject, criterion, case, source result, mapping, scope, or window defeats reuse and requires another decision.

### A.21:5 - Worked cases

#### A.21:5.1 - Ordinary local pass

The workshop case at the entry uses two required checks. Each application names its subject and criterion: `CalibrationCertificate-44` for `TorqueWrench-12` is current under `CalibrationRule-E3`, and `WorkshopEnclosure-2` is closed under `EnclosureRule-E2`. `WorkshopEntryProfile-E5` maps both satisfied results to `pass`. Worst-result aggregation gives `pass`; the short rationale names both results, and the bounded action is “start `CalibrationCycle-17` before 16:00”. No publication or replay record is required.

#### A.21:5.2 - Unknown and failed checks

If the state of `WorkshopEnclosure-2` cannot be established, that application is `unknown`; it does not disappear as `abstain`. The profile maps it to `block`, so the action is “hold the cycle and inspect the enclosure”. If `CalibrationCertificate-44` is expired while the enclosure check passes, the certificate application maps to `block`; the passing enclosure result remains available for repair and need not be rerun unless its own recheck condition is met.

If inspection was not performed after the block was already known, record that check as `notRun`. It remains in the required set and cannot support `pass`.

#### A.21:5.3 - Conditional high-consequence extension

`RegulatedReleaseProfile-E9` adds `RegulatedConformance(Regulator-X, Rule-E9)` and evidence-completeness applications for `ReleaseLot-27`. Unknown regulator conformance maps to `block`. The profile cites Regulator X, Rule E9, the evidence tolerance, the refusal consequence, and the window. If the decision is published or reused, add the E.17 publication and an audit or equivalence record; ordinary gates do not inherit that apparatus.

### A.21:6 - Bias annotation

- **Green-display bias.** A display can look like a decision. Recover the gate result and applicable profile.
- **Neutral-value bias.** An algebraic neutral can hide an unknown or unrun check. Preserve applicability and evaluation state before mapping.
- **Profile-label bias.** A profile name can look authoritative. Require its applicable rule and any separate authority relation.
- **Infrastructure bias.** Publication and replay fields can look like the gate itself. Keep the decision result primary and add infrastructure only for its triggered use.

### A.21:7 - Check the ordinary gate decision

1. **Decision.** Name the gate, the action or transition being decided, its scope, and its time window.
2. **Applicable rule.** Point to the profile rule and edition that apply to this gate and subject. Recover its required checks, mappings, consequences, scope and window, and any authority the rule itself requires.
3. **Checks.** For each check, name its subject, criterion and edition, case, requirement, evaluation state, source result, and mapping rule.
4. **Nothing missing.** Keep every required check visible, including `notRun`, `unknown`, error, and failure.
5. **Worst result wins.** Aggregate only after the rule has mapped every required result. A missing or unrun required result cannot support `pass`.
6. **Next action.** State what `pass`, `degrade`, `block`, or `abstain` means for this action and when to decide again.
7. **Boundary.** Do not turn the decision into work-entry readiness or performed Work, and add no crossing, Bridge, publication, or assurance claim that is absent.

#### A.21:7.1 - Triggered additions

| Current use | Add | Direct pattern |
| --- | --- | --- |
| Launch decision | Prospective work-entry claim and only the checks selected by the applicable profile | `A.15.5`, `E.18`, and the pattern defining each check |
| Structural crossing | Changed-binding and crossing facts; SquareLaw only when its crossing rule applies | `E.18` |
| Semantic correspondence | Separate Bridge and bounded-use claim; optional evidence or publication apparatus only when used | `F.9`, `F.17`, `E.17` |
| Publication | Form, carrier, publication occurrence, and the minimum decision refs | `E.17` |
| Evidence, safety, regulation, or assurance | Exact source result and its evidence or assurance relation | `A.10`, `B.3`, or the applicable domain pattern |
| Reuse or replay | Decision log or equivalence witness covering the claimed reuse inputs | `G.6`, `G.11`, and the publication pattern when published |

### A.21:8 - Common mistakes

| Mistake | Why it fails | Repair |
| --- | --- | --- |
| Green cue as pass | No result, profile application, or check set is recoverable. | Recover the A.21 result or leave the cue non-decisional. |
| Merge by check label | Different subjects, criteria, regulators, or cases disappear. | Merge only identical check-application identities. |
| Unknown as `abstain` | A missing required fact becomes neutral and may yield pass. | Preserve `unknown`; apply an explicit profile rule. |
| New slice weakens checks | Locality is mistaken for policy authority. | Cite another applicable policy fact and any required authority. |
| `degrade` with no action | The word sounds precise but gives no usable consequence. | State the permitted restricted action, condition, stop, and recheck. |
| Every gate is a LaunchGate or crossing | Optional branches become universal infrastructure. | Activate only the branch present in the decision subject and selected structure. |
| Every crossing has a Bridge | Structural and semantic relations are collapsed. | Use E.18 for the crossing and F.9 only for a separate semantic relation. |

### A.21:9 - Consequences

The gate result is smaller and more truthful. It preserves repair information, prevents unknown or unrun required checks from disappearing, and makes profile change auditable without turning a path boundary into authority. Ordinary gates stop after one result and short rationale; publication, replay, crossing, safety, regulation, and assurance add cost only when their claims are current.

The cost is explicit identity. A practitioner must name the decision subject, profile application, and each required check application instead of relying on labels such as “green”, “Core”, or “regulated”.

### A.21:10 - Rationale

Constraint truth, evidence about that truth, policy application, and bounded action are different claims. The source patterns establish check results. A.21 applies one current profile and records the consequence. Keeping those claims separate makes the decision independent of evaluation order and keeps failures useful for repair.

The join lattice is retained because it gives a compact, deterministic aggregation after every source result has been identified and mapped. It does not supply applicability, evidence, permission, authority, or a missing result.

### A.21:11 - SoTA echo

| Practice line already used by A.21 | Adopted move | Limit |
| --- | --- | --- |
| Join-semilattice aggregation in distributed-systems practice | Use an associative, commutative, idempotent worst-result join after explicit mapping. | Algebra does not make unknown or unrun input neutral. |
| Policy evaluation and safety decision tables | Identify the applicable rule, subject, inputs, outcome mapping, and action consequence. | A profile label or default-looking branch is not policy application or authority. |
| Attestation and provenance practice, including in-toto and SLSA lineage | Publish refs and rationale when audit, transfer, or reuse is current. | An attestation, log, or dashboard does not create the gate decision or source truth. |
| Compositional crossing checks | Apply crossing equations to an exact structural crossing when its rule requires them. | A crossing does not imply a semantic Bridge, and a non-crossing gate needs neither. |

### A.21:12 - Relations

- `A.20` supplies exact internal-constraint results or a complete required-set summary without gate policy.
- `E.18` supplies selected-structure positions, paths, slices, and structural crossing facts; it does not make every work-entry question a gate or crossing.
- `A.15.5` defines full-kit and work-entry readiness and remains the ordinary route when no gate decision is current.
- `A.10`, `B.3`, safety patterns, regulatory patterns, A.2, C.3.2, A.2.1, F.6, and A.2.6 define or test the source claims used by applicable checks.
- `F.9` and `F.17` apply only to a separately established semantic correspondence and bounded use.
- `E.17` defines publication forms and carrier relations when the result is published.
- `G.6` and `G.11` apply when provenance visibility, refresh, replay, or reuse is claimed.
- `F.19` keeps the ordinary decision path visible before algebra, publication, and assurance extensions.

### A.21:End

