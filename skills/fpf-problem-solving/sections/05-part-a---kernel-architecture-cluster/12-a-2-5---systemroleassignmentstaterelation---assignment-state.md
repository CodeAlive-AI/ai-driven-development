## A.2.5 - SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.5:0 - Use This When

**Plain designations.** Say “this assignment to a system role satisfies this state condition” for the relation and “state condition for an assignment to a system role” for the predicate.

Use this pattern when one exact assignment to a system role already obtains, but a method step, Work occurrence, incompatibility check, or operational gate depends on that assignment satisfying a particular condition during a particular window.

Start with the practical question: **Does this exact assignment satisfy this exact state condition throughout the window that matters now?** The first useful result is the current `SystemRoleAssignmentStateRelation` occurrence or its absence. Add an assertion and evidence-use relation only when a later decision must rely on that result.

Typical working moments include these:

- a calibrated inspection robot is assigned to `InspectorSystemRole`, but inspection Work should start only while calibration, synchronization, and operating-envelope conditions hold;
- an incident commander remains on call, yet a conflict or fatigue condition may make that assignment non-admitting for one response window;
- a method description declares a state condition for an assignment to a system role, while the current assignment has not yet been tested against it;
- two assignments are incompatible only while both satisfy the conditions that make them work-admitting; and
- a model-use structure, `KindSignature`, reference scheme, or bridge changes the meaning of one predicate clause and must therefore be included in that predicate's semantic basis.

**Primary EntityOfConcern.** The EntityOfConcern is one obtaining `SystemRoleAssignmentStateRelation`, a direct relation kind admitted under `U.Relation`. Its two participants are one exact obtaining `U.SystemRoleAssignment` occurrence and one by-value `SystemRoleAssignmentStatePredicate`. The relation's maximal continuous temporal extent comes from uninterrupted predicate truth while that assignment obtains.

**Primary working reader.** The first reader is an engineer, operator, method designer, safety checker, or manager deciding whether a current assignment can support the next method or Work claim without confusing assignment, capability, state, evidence, gate outcome, and performed Work.

**What goes wrong if missed.** A system-role label is treated as current readiness. A dashboard value is substituted for the world-side state relation. Missing evidence is read as proof that the predicate is false. Capability is mistaken for Work admission. A state-machine diagram is used as both the ontology and the method order.

**What this buys.** The reader can identify repeated state episodes inside one continuing assignment, keep evidence and world-side obtaining distinct, combine simultaneous conditions, and pass the exact state claim to the direct pattern governing the next decision or Work use.

**Not this pattern when.** Use `A.2` and `C.3` for the exact local system-role kind, `A.2.1` for the assignment and its holder, `A.2.2` for capability and operating envelope, `A.2.7` for relations among system-role kinds, and `A.15.1` for Work that actually occurred. Use `A.2.4` or `A.10` when the current object is the evidence-use relation rather than the assignment-state relation. A displayed status, credential entry, gate decision, or organizational position keeps its own direct pattern.

### A.2.5:0.1 - Kind Settlement

`SystemRoleAssignmentStateRelation` is admitted as a direct relation kind under `U.Relation`.

`SystemRoleAssignmentStatePredicate` is a local ValueKind declared by this pattern, not another root U-kind. One predicate value is identified by:

1. the exact local system-role kind for whose assignments it is defined;
2. normalized truth-condition ClaimGraph clauses naming the governed qualities or relations tested;
3. its temporal reading;
4. its applicability conditions; and
5. the exact semantic basis whose edition changes meaning, including a `KindSignature`, reference scheme, bridge, or model-use structure only when the clauses depend on it.

A displayed name such as `InspectionReady` can designate the predicate. The name alone does not identify it. `Ready@InspectorSystemRole` and `Ready@ApproverSystemRole` are different predicate values unless one separately declared predicate has one exact common domain and identical clauses, temporal reading, applicability, and semantic basis.

A compatible semantic-basis edition preserves the predicate only through an explicit predicate-continuity decision showing that those identity-bearing facts continue. A changed system-role kind, truth clause, temporal reading, applicability condition, or meaning-bearing semantic basis yields another predicate.

A `SystemRoleAssignmentStateAssertion` is a `U.Episteme` whose EntityOfConcern is the exact assignment or an explicitly individuated state-relation occurrence, according to the claim. Its ClaimGraph names the predicate, direct claim family, and `assertionPolarity: affirmative | negative`. An affirmative claim may state a known actual extent only after A.2.5 independently establishes obtaining. A receiving evaluation may separately state its target window. Supported, refuted, or unresolved reliance belongs to `A.10` or a separately constituted evaluation result or reliance assertion. Assertion, reliance posture, evidence episteme, evidence-use relation, and world-side occurrence remain different objects.

A representation episteme may describe predicates, possible configurations, and possible changes. A statechart or state-machine display is a mathematical or representational lens.

### A.2.5:1 - Problem Frame

An occurrence of a declared `U.SystemRoleAssignment` species assigns an admitted System to one local system-role kind and supplies any other values required by that species. It does not establish that the assignment satisfies a condition needed by a Method or Work claim in the evaluated interval.

`Robot-7` can remain under `InspectionShiftAssignment-17` throughout an eight-hour shift while calibration expires at noon. The assignment continues. The `InspectionReady` state occurrence ends when its predicate ceases to hold. Recalibration can start another occurrence under the same assignment without creating another assignment.

The same distinction appears in social and computational Work. An on-call person can remain assigned while conflicted or fatigued. A service can remain assigned to `ApproverSystemRole` while one predicate concerns fulfilment approval and another concerns payment authorization. A tool-using agent can expose a capability while a concrete action remains inadmissible for the current task and inputs.

The engineering problem is therefore to identify the exact assignment, predicate, and interval; distinguish affirmative or negative assertion polarity from reliance posture; recognize an occurrence only while the direct predicate is true; and connect an assertion to evidence only when a consequence-bearing use needs that support.

### A.2.5:2 - Problem

Without a direct assignment-state relation ontology, six recurring failures appear.

1. **Assignment becomes readiness.** Holding an assignment is treated as satisfying every state precondition of every method that names its system-role kind.
2. **State label hides the predicate.** `Ready`, `Approved`, or `Active` travels between domains although its truth conditions differ.
3. **Evidence becomes the state.** An evidence or display episteme is treated as the world-side relation.
4. **Missing evidence becomes falsehood.** An unrecovered or stale evidence path is taken as proof that the predicate does not obtain.
5. **Capability becomes admission.** A system's ability to perform an operation is overread as current admission of this concrete method or Work claim.
6. **State notation becomes method order.** A transition arrow is treated as the Work that changes the state, although Method, Work, transformation, and state-change claim have different ontics.

### A.2.5:3 - Forces

| Force | Tension |
|---|---|
| Lightweight assertion vs reusable identity | Ordinary Work needs a short state sentence; later admission, history, or comparison may need one individuated relation occurrence. |
| World-side obtaining vs evidence-backed reliance | A predicate can hold before anyone measures it, while consequence-bearing use needs a current assertion and evidence relation. |
| Simultaneous predicates vs single-state notation | `Calibrated`, `Synchronized`, and `InRange` may all hold together; a finite-state machine may still help with one narrower exclusive configuration. |
| Stable assignment vs changing state | One assignment can contain several state episodes without being recreated at each change. |
| Predicate identity vs permanent interpretation participants | Meaning-bearing signatures, schemes, bridges, or model-use structures may distinguish predicate values; irrelevant editions must not become participants of every assignment or state relation. |
| Capability vs action admission | Ability is a neighboring claim; current Work admission depends on the exact state predicate and the direct consumer's rule. |

### A.2.5:4 - Solution

Start from a readable assertion:

> `Robot-7`'s current assignment to `InspectorSystemRole` satisfies `InspectionReady` throughout the inspection window.

When a receiving use needs reusable participant typing, use the declared `RelationSignature`. When it needs occurrence identity, apply the world-side identity rule in section 4.3.

#### A.2.5:4.1 - Direct Relation Declaration

This pattern defines the `RelationSignature` for `SystemRoleAssignmentStateRelation`:

| SlotKind | ValueKind | refMode | Meaning |
|---|---|---|---|
| `SystemRoleAssignmentSlot` | `U.SystemRoleAssignment` | `U.RelationRef` constrained to `U.SystemRoleAssignment` | The exact assignment occurrence being evaluated; its declared species remains recoverable. |
| `StatePredicateSlot` | `SystemRoleAssignmentStatePredicate` | `ByValue` | The exact predicate value identified under section 0.1. |

These are the only two generic participants. `SystemRoleAssignmentStateRelation` obtains exactly while the assignment obtains and the fixed by-value predicate is true under its temporal reading. Its actual extent is the maximal continuous interval of that obtaining. An affirmative assertion or occurrence description may state the known extent as `systemRoleAssignmentStateExtent` only for an independently established occurrence; a receiving evaluation may state a separate `declaredSystemRoleAssignmentStateEvaluationWindow`. Neither temporal value, assertion polarity, reliance posture, taxonomy episteme, reference scheme, bridge, nor model-use structure is another relation participant.

A relied-on assertion uses a direct evidence-use relation. Another world-side occurrence affects predicate truth only when an exact truth-condition clause cites that occurrence through its subject pattern.

#### A.2.5:4.2 - Predicate Meaning and Semantic Basis

One `SystemRoleAssignmentStatePredicate` value names:

- the exact local system-role kind for whose assignment species the predicate is defined;
- normalized truth-condition ClaimGraph clauses, each naming its governed quality or relation, actual participants, and subject pattern;
- the temporal reading, such as truth at an instant, throughout a receiving-use window, or for a declared tolerated portion of that window;
- applicability conditions; and
- only the semantic-basis references whose editions can change those clauses or their interpretation.

This content defines one predicate value. The direct qualities and relations keep their own kinds and subject patterns.

Predicates need not be mutually exclusive. `Calibrated`, `Synchronized`, and `InRange` can hold simultaneously; `InspectionReady` may be a conjunction over them. Use an exclusive state configuration only when the subject-domain model actually needs one.

A shared label does not establish shared meaning. Cross-context reuse needs the same predicate identity or an explicit comparison or bridge stating which truth and admission effects are preserved. A bridge or scheme enters the predicate's semantic basis only when the predicate clauses really depend on it.

#### A.2.5:4.3 - Occurrence Identity and Repeated Episodes

Do not replace the identity rule with a tuple key. One `SystemRoleAssignmentStateRelation` occurrence begins when one fixed assignment starts satisfying one fixed predicate. It continues while the assignment obtains and the predicate remains true without interruption. It ends when the assignment ceases, the predicate becomes false, or either participant changes. A later return to truth starts another occurrence.

An affirmative assertion or occurrence description may state the currently known `systemRoleAssignmentStateExtent`. Recording an end boundary for a previously open extent refines the description of the same occurrence when assignment obtaining and predicate truth were uninterrupted. A demonstrated predicate gap separates occurrences. Thus `true → false → true` produces two state occurrences inside one continuing assignment.

A later correction of an assertion interval, changed evidence relation, assertion edition, dashboard display, or publication creates no world-side occurrence while truth was uninterrupted. An evidence gap gives the receiving use unresolved reliance; it does not demonstrate a gap in predicate truth or add a third assertion polarity.

#### A.2.5:4.4 - Assertion and Evidence Use

For a relied-on state claim, keep this order:

1. name the exact `U.SystemRoleAssignment`, by-value `SystemRoleAssignmentStatePredicate`, direct claim family, and affirmative or negative assertion polarity;
2. when A.2.5 independently establishes obtaining and the receiving use needs occurrence identity, individuate the occurrence under section 4.3;
3. state a `SystemRoleAssignmentStateAssertion : U.Episteme` whose ClaimGraph carries the predicate, direct claim-family reference, polarity, known `systemRoleAssignmentStateExtent` only for an affirmative claim about an established occurrence, and any separate `declaredSystemRoleAssignmentStateEvaluationWindow`;
4. include a meaning-bearing semantic-basis reference in the predicate identity, while a non-meaning-changing receiving-use selection stays with that use;
5. use `A.2.4` for compact evidence use and `A.10` only when fuller evidence-basis detail changes the relied-on use; and
6. let the direct consumer apply the supported assertion under its own subject pattern.

When evaluation itself is current, recover the exact actual evaluator System through A.13 and let A.15.1 independently admit exact dated evaluation `W_eval : U.Work`. Add F.6 `performedUnderAssignment(W_eval, RA_eval)` through the same obtaining A.13 assignment only when this account or its receiving use expressly consumes precise assignment-bound attribution; F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the evaluation Work intact. A separately constituted evaluation result is a `C.2.1` episteme whose ClaimGraph states the judgment about the assignment or established occurrence. Work, performer, assignment, result episteme, provenance, and receiving reliance remain neighboring objects; none becomes a state-relation participant or identity discriminator.

The actual state extent, target evaluation window, and evidence-relevance interval answer different questions. Expired evidence lowers reliance without retroactively rewriting an earlier world-side occurrence.

#### A.2.5:4.5 - Work-Admission Use

A.2.5 supplies the state relation and exact assertion form. Use the direct subject patterns when Method selection, a gate decision, authority, or a claim that Work occurred is needed.

For a consequence-bearing admission use, the system performing the consumer's evaluation or decision Work applies that consumer's direct pattern and checks:

1. the exact `U.SystemRoleAssignment` obtains throughout the receiving decision or Work window;
2. the consumer selects one exact `SystemRoleAssignmentStatePredicate`, whose truth condition may be an explicit conjunction;
3. each relevant assignment has an obtaining `SystemRoleAssignmentStateRelation` whose actual extent covers the receiving-use window;
4. the assertion has the evidence relation and currentness that this consumer requires; and
5. every other admission condition is separately established under its subject pattern.

The consumer's direct pattern defines any admit, deny, defer, or unresolved outcome. A.2.5 contributes only the exact state relation on which that decision Work may rely.

#### A.2.5:4.6 - System-Role-Kind Relation Use

When substitution, incompatibility, bundle, or residual qualification among exact local system-role kinds is selected with `A.2.7`, test state sensitivity through exact assignments, state predicates, and windows.

- Substitution supports one admission condition only when the candidate assignment's current predicate satisfies the selected receiving rule.
- Incompatibility is stated for the exact same-holder or different-holder rule, Work identity condition, overlapping windows, and predicate conditions under which the conflict appears.
- A Work claim needing several system-role kinds uses the independently obtaining assignments and state occurrences needed by that claim. It does not require a Cartesian product of every possible state label.

A conjunction for one Work claim creates no composite system-role kind, assignment, or state predicate by form.

#### A.2.5:4.7 - State-Machine and Change Lenses

Use statecharts or state machines when mutually exclusive configurations, orthogonal regions, guarded changes, or event handling improve the subject-domain model. The notation describes possible configurations and changes; it does not replace the direct relation occurrence.

A change arrow represents a proposed or observed change in predicate truth; it is not the world-side change by form. Recover the exact changed object or relation, then use the direct pattern governing that change. Use the Method description for any prescribed Method order.

When the model needs continuous coordinates rather than discrete labels, use `A.19` for the characteristic space and let the by-value state predicate select a region, band, ordering condition, or other exact condition. Measurement and evaluation stay with `C.16` and their direct patterns.

#### A.2.5:4.8 - Semantic Basis and Receiving-Use Qualification

Most state claims need no bridge, reference scheme, or bounded-model-use structure. Directly governed truth-condition clauses are enough.

When a `KindSignature`, reference scheme, bridge, or `BoundedModelUseStructure` changes the meaning of a predicate clause, include its exact edition in `SystemRoleAssignmentStatePredicate` semantic basis and therefore in predicate identity. When it changes only how a separate receiving assertion, comparison, or Work use presents or consumes an unchanged predicate, cite it in that receiving use instead. The generic relation signature remains the two-participant declaration in §4.1.

### A.2.5:5 - Working Guidance

1. Write the readable sentence naming the current assignment and state condition; name the receiving-use window only when the current check selects one.
2. Recover the predicate by value: exact system-role kind, normalized truth-condition clauses, temporal reading, applicability, and only meaning-bearing semantic-basis editions.
3. Derive the maximal continuous extent from assignment obtaining and predicate truth; separately check any receiving-use window against that extent.
4. Ask whether the receiving use needs occurrence identity and whether it relies on the state claim. If both answers are no, keep the readable assertion and stop.
5. For relied-on use, make the assertion episteme, polarity, direct claim-family reference, and required evidence-use relation explicit. Record supported, refuted, or unresolved reliance separately; absent evidence is neither negative polarity nor world-side non-obtaining.
6. Leave capability fit, Method selection, gate outcome, authority, assurance, and performed Work with their subject patterns.
7. Put a meaning-changing semantic basis in predicate identity and a merely use-qualifying selection in the receiving use, never in the generic relation signature.

### A.2.5:6 - Worked Slices

#### A.2.5:6.1 - Robot Inspection After Recalibration

`Robot-7` already holds this A.2.1 assignment:

```text
Robot7InspectionShiftAssignment-17 : InspectionShiftAssignment
InspectionShiftAssignment <: U.SystemRoleAssignment
  HolderSystemSlot: Robot-7
  AssignedSystemRoleKindSlot: InspectorSystemRole
  assignmentInterval: [2026-08-10T09:00, 2026-08-10T17:00]
```

The bearing-inspection method description declares `InspectionReady`, whose clauses require current calibration, clock synchronization inside tolerance, operating-envelope fit, and no active quarantine relation throughout the inspection window.

```text
SystemRoleAssignmentStateAssertion:
  directClaimFamilyRef: A.2.5 SystemRoleAssignmentStateRelation
  SystemRoleAssignmentSlot: U.RelationRef(Robot7InspectionShiftAssignment-17)
  StatePredicateSlot:
    systemRoleKindRef: U.KindRef(InspectorSystemRole)
    NormalizedTruthConditionClaimGraph:
      CalibrationCurrent(Robot-7)
      and ClockSynchronizationWithinTolerance(Robot-7)
      and InspectionOperatingEnvelopeFit(Robot-7)
      and no ActiveQuarantineRelation(Robot-7)
    TemporalReading: continuous truth over the declared inspection interval
    Applicability: bearing inspection Work under InspectionShiftAssignment
    SemanticBasisRefs: omitted; these clauses use the direct subject predicates without another meaning-bearing edition
  assertionPolarity: affirmative
  systemRoleAssignmentStateExtent: [2026-08-10T09:20, 2026-08-10T12:00]
```

A calibration report is a separate `U.Episteme`; an A.2.4 evidence-use relation can support reliance on this assertion. At noon calibration validity ends and the predicate becomes false, so the first state occurrence ends while the assignment continues. Recalibration at 12:30 can make the same predicate true again and begins a second occurrence under that assignment.

#### A.2.5:6.2 - Drive Motor in a Pump Assembly

`Motor-M1` is the holder of an exact pump-maintenance assignment whose assigned local kind is `DriveMotorSystemRole`. The current Work claim needs `DriveReady`, whose predicate names the exact supply relation, torque capability-fit relation, thermal band, and installed-connection relation.

The pump assembly grounds those direct claims; it is not a mandatory context slot. No scheme or `BoundedModelUseStructure` is required because the direct predicate clauses determine the state. Torque capability can remain while a missing supply relation makes `DriveReady` false. An affirmative `DriveReady` assertion states the assignment's condition; use A.15.1 for any claim that pumping Work occurred.

#### A.2.5:6.3 - Socially Constituted Credential State

A clinician holds one exact assignment whose local kind is `ProcedureOperatorSystemRole`. Predicate `CredentialCurrentForProcedure-X` depends on an accepted credential decision, its validity interval, and absence of a suspending decision.

The accepted decision relation helps constitute the predicate because the credential ontology says so. A certificate publication may evidence that decision but does not substitute for it. The state occurrence still has the assignment and predicate as participants; evidence and publication remain neighboring relations.

#### A.2.5:6.4 - Two Approval Predicates

`ApprovalService-2` holds an exact assignment to `ApproverSystemRole`. `FulfilmentApprovalReady` concerns fulfilment-state change; `PaymentApprovalReady` concerns payment authorization. Their truth clauses and applicability differ, so they are different `SystemRoleAssignmentStatePredicate` values even if one interface displays both as `Ready`.

If an independently selected model-use structure changes the meaning of one predicate's clauses, its exact edition belongs in that predicate's semantic basis. If it only selects which already identified predicate a view presents, it remains a receiving-use qualification.

#### A.2.5:6.5 - Approved Standard or Evidence Dataset Is a Different Relation

Suppose a project says, “Standard S is approved.” The standard is an episteme, not a system under a work-facing assignment. Recover the direct status-use, decision, source-use, or publication-use relation.

Likewise, a dataset or report that “plays a role” remains an episteme used through direct evidence, source, measurement, freshness, provenance, or assurance relations. Apply A.2.5 only if an admitted system's exact assignment is being tested by a `SystemRoleAssignmentStatePredicate` that depends on one of those relations.

### A.2.5:7 - Archetypal Grounding and Bias Control

**Physical system.** A motor, robot, laboratory instrument, or production cell can hold an assignment while its state predicate changes as physical relations and measured characteristics change.

**Human or organizational system.** A person, team, or organization can remain assigned while a current conflict, credential, fatigue, resource, or decision relation changes the predicate relevant to one Work claim.

**Computational system.** A service or agent can expose a capability while each concrete action still needs current assignment, state predicate, task relation, and direct authorization or gate evaluation. This is one specialization, not the universal meaning of assignment state.

**Episteme boundary.** A representation or evidence episteme can describe or support a state claim.

The main bias risk is label-first reasoning. A familiar state word invites the reader to skip predicate recovery. Repair it by recovering the assignment, predicate by value, actual state extent, and only the assertion and evidence-use relation needed by the receiving use.

### A.2.5:8 - Conformance Checklist

| Check | Question |
|---|---|
| `CC-A2.5-01` | Is the current object one `SystemRoleAssignmentStateRelation : U.Relation`? |
| `CC-A2.5-02` | Does `SystemRoleAssignmentSlot` use a `U.RelationRef` constrained to `U.SystemRoleAssignment` and resolve to the exact assignment occurrence being evaluated, with its declared species, holder, and extent established under A.2.1? |
| `CC-A2.5-03` | Is `StatePredicateSlot` present by value with exact system-role-kind domain, normalized truth clauses, temporal reading, applicability, and only meaning-bearing semantic-basis refs? |
| `CC-A2.5-04` | Is actual state extent derived from uninterrupted predicate truth while the assignment obtains, with any target evaluation window kept separate? |
| `CC-A2.5-05` | When occurrence identity is needed, does it use the fixed assignment, fixed predicate value, and maximal continuous truth interval rather than a representation key? |
| `CC-A2.5-06` | Are a demonstrated predicate gap and a mere evidence gap distinguished? |
| `CC-A2.5-07` | Does `SystemRoleAssignmentStateAssertion` keep polarity, predicate, direct claim-family ref, known actual extent, target window, reliance posture, and evidence relations distinct? |
| `CC-A2.5-08` | Are capability, Method selection, gate outcome, authority, assurance, and performed Work left with their direct patterns? |
| `CC-A2.5-09` | If several predicates hold together, are they composed explicitly rather than forced into one exclusive state label? |
| `CC-A2.5-10` | Does cross-context reuse preserve the full predicate identity through an explicit continuity or bridge decision rather than label matching? |
| `CC-A2.5-11` | Is a meaning-bearing signature, scheme, bridge, or model-use structure included in predicate identity only when the clauses depend on it, and otherwise kept with the receiving use? |
| `CC-A2.5-12` | If a statechart or graph is used, is it kept as a lens or description of possible configurations and changes? |

### A.2.5:9 - Common Failure Modes and Repairs

| Failure | Observable symptom | Repair |
|---|---|---|
| Assignment-as-readiness | A Work claim proceeds because a holder is assigned. | Name the state predicate and establish the corresponding relation for the Work window. |
| State-label transport | Two domains use `Ready` as if it were one predicate. | Compare full predicate identities; use an explicit bridge only when cross-context preservation is claimed. |
| Evidence-as-state | A certificate or dashboard display is entered as the state. | Keep the world-side relation separate and target its assertion with an evidence-use relation. |
| Evidence-gap-as-false | A missing current report closes a state episode. | Record unresolved reliance; close the occurrence only when a truth-condition clause is demonstrated not to hold. |
| Capability-as-admission | Tool exposure or measured ability admits a concrete action. | Keep capability in A.2.2 and evaluate current state and action-specific conditions separately. |
| Method-order drift | Transition arrows are used as the procedure. | Name the Work, transformation, decision, or event occurrences that change predicate truth and put order in the Method description. |
| Product-state explosion | A multi-assignment Work claim enumerates every combination of labels. | Use separate state occurrences and only the conjunction needed by the current claim; create no compound system-role kind or assignment by form. |

### A.2.5:10 - Consequences

Benefits:

- one assignment can support several separately identifiable state episodes;
- simultaneous predicates remain expressible;
- predicate truth, assertion, evidence use, and Work admission can change independently and be repaired locally;
- Method and gate assertions cite an exact current relation instead of a status label; and
- physical, social, organizational, and computational cases use the same relation discipline.

Costs and limits:

- load-bearing predicates must be written by value, including temporal semantics and any meaning-bearing semantic basis;
- consequence-bearing reliance needs only the evidence currentness and direct consumer that its use requires;
- cross-context reuse may need a continuity or bridge decision rather than label matching; and
- A.2.5 does not define every subject-domain predicate, measurement method, authorization relation, or state-changing Method.

Reopen or lower only the affected claim when the assignment, predicate identity, actual state extent, receiving-use window, evidence relevance, direct consumer rule, or meaning-bearing semantic basis changes. Do not rewrite the system-role kind or assignment when only one state episode changes.

### A.2.5:11 - Rationale

The pattern starts from the world-side relation because state truth can matter before a record exists. A robot can cease to satisfy its inspection predicate before a dashboard refreshes. A credential decision can constitute an institutional condition before a certificate is published. A supported assertion is needed for some reliance uses.

Using uninterrupted predicate truth as the identity boundary distinguishes repeated episodes even when assignment and predicate stay the same. A description may refine an open interval's end without creating another occurrence; a genuine false gap does create a boundary.

Assignment state is neither capability nor Work. Capability says what operations a system can perform in an envelope. `SystemRoleAssignmentStateRelation` says whether one current assignment satisfies one predicate over an interval. A Work claim states what was actually performed. A Method, gate, or Work pattern may depend on all three, but none proves the others.

### A.2.5:12 - SoTA-Echoing

| Current or mature line | What it contributes | Concrete mutation in A.2.5 |
|---|---|---|
| [W3C SCXML 1.0](https://www.w3.org/TR/scxml/), a mature 2015 Recommendation rather than current competitive SoTA | Explicit states, parallel regions, guarded transitions, events, and executable state-machine semantics. | Keep statecharts available when the subject-domain model needs them, but type them as mathematical or description lenses rather than the world-side relation occurrence or universal Method order. |
| Esparza and Fischer, [Runtime Verification for LTL in Stochastic Systems](https://arxiv.org/abs/2508.07963), 2025 | Runtime monitoring distinguishes true, false, and inconclusive results; finite observations do not settle every temporal property. | Treat incomplete evidence as unresolved for the relying use, preserve the predicate's temporal reading, and do not close an occurrence merely because a finite evidence path is silent. |
| [Cedar Policy Language current reference](https://docs.cedarpolicy.com/policies/syntax-policy.html) | Fine-grained decisions evaluate a concrete principal, action, resource, current attributes, and request-time conditions rather than a system-role label alone. | Require the system performing consumer decision Work to combine current assignment, exact predicate, state window, and action-specific relations. Keep this as an implementable software specialization rather than the ontology of every assignment state. |
| Zuvic, [Capability Gates Are Not Authorization](https://arxiv.org/abs/2606.28679), 2026 preprint | A current agent-framework audit distinguishes exposed capability from per-call, value-sensitive authorization and reports fail-closed enforcement experiments. | Keep capability in A.2.2 and require the consumer to evaluate the concrete state and action claim before side effects; do not infer authorization from tool exposure. The empirical scope remains the audited software frameworks. |
| Liu et al., [A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469), 2026 preprint | Task alignment, action alignment, source authorization, and data isolation require runtime checks over the current task and action. | In agentic cases, require the consumer's governing claim to name the current task and action relations; A.2.5 supplies only the exact state relation and assertion form, while A.10 supplies only the evidence-use relation; the applicable evaluation or assurance pattern separately establishes any reliance posture. |
| `A.6.REL`, `A.2.1`, `A.19`, `A.2.4`, and `A.10` | FPF already separates relation obtaining, occurrence identity, assignment episodes, characteristic-space predicates, assertions, and evidence use. | Give A.2.5 an occurrence identity rule, preserve the lightweight assertion path, and keep evidence outside generic state identity. |

The sources' transferable contribution is bounded: current action decisions need exact participants and predicates; temporal monitoring can remain unresolved; capability and action admission differ; and state-machine notation is optional modeling machinery.

### A.2.5:13 - Relations

| Related pattern | Relation |
|---|---|
| `A.2` and `C.3` | Govern exact context-local system-role kinds and their `KindSignature`s; assignment-state predicates may name those kinds and signatures without making them relation participants. |
| `A.2.1` | Use for the declared `U.SystemRoleAssignment` species and the obtaining occurrence referenced by every state relation. |
| `A.2.2` | Governs capability and operating-envelope claims that a state predicate may reference but does not replace. |
| `A.2.4` and `A.10` | Govern compact evidence use and full evidence-provenance support for a state assertion. |
| `A.2.7` | Use for relations among system-role kinds that may consume current assignment-state results without merging kinds, assignments, or states. |
| `A.6.REL` | Governs progressive relation-occurrence individuation and occurrence-as-participant use. |
| `A.6.5` | Governs SlotKind, ValueKind, and reference-mode discipline for the direct declaration. |
| `A.19` and `C.16` | Govern characteristic spaces, predicates over measured coordinates, measurement, and comparability when used by a state predicate. |
| `A.15`, `A.15.1`, `A.15.2`, and `A.21` | Govern Method participation, performed or planned Work, and gate outcomes that consume state claims. |
| `A.1.1` | Use for any selected `BoundedModelUseStructure`; A.2.5 includes its exact edition in predicate identity only when meaning depends on it. |
| `C.27` and `G.11` | Govern temporal currentness, decay, and evidence refresh when those claims are current. |

### A.2.5:End

