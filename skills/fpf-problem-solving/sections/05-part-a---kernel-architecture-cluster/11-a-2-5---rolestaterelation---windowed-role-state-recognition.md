## A.2.5 - RoleStateRelation - Windowed Role-State Recognition and Work Admission

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.5:0 - Use This When

**Plain name.** Role-state relation.

Use this pattern when an admitted system already holds a `U.Role`, but a method step, work occurrence, incompatibility check, or operational gate depends on the assignment being in a particular state during a particular window.

The first useful question is not "What status word is displayed?" It is: **Which current `U.RoleAssignment` satisfies which exact state predicate, during which window, and what evidence-use relation supports the assertion on which the next work decision relies?**

Typical working moments include these:

- a calibrated inspection robot is assigned `InspectorRole`, but inspection work should start only while calibration, synchronization, and operating-envelope predicates hold;
- an incident commander is on call, yet a conflict or fatigue predicate may make the assignment non-admitting for a particular response window;
- a method description declares a role-state predicate for its admission rule, while the current assignment and evidence have not yet been connected to that predicate;
- two role assignments are incompatible only while both satisfy the predicates that make them work-admitting;
- a DDD-style model-use organization changes the meaning of an otherwise identical state predicate.

**Primary EntityOfConcern.** The EntityOfConcern is one obtaining `RoleStateRelation`, a direct relation kind admitted under `U.Relation`. Its two participants are one current `U.RoleAssignment` occurrence and one by-value `RoleStatePredicate`; the occurrence's maximal continuous temporal extent is derived from uninterrupted predicate truth while the assignment obtains.

**Primary working reader.** The first reader is an engineer, operator, method designer, safety checker, or manager deciding whether a current assignment can support the next method or work claim without confusing assignment, capability, state, evidence, gate outcome, and performed work.

**What goes wrong if missed.** A role label is treated as current readiness. A dashboard value is substituted for the world-side role-state relation. Missing evidence is read as proof that the predicate is false. Capability is mistaken for work admission. A state-machine diagram silently becomes both the ontology and the method order.

**What this buys.** The reader can identify repeated role-state episodes, keep evidence and world-side obtaining distinct, combine several simultaneous predicates, and pass the exact state claim to the direct pattern governing the next decision or work use.

**Not this pattern when.** Use `A.2` for the role value, `A.2.1` for who holds it and when, `A.2.2` for capability and operating envelope, `A.2.7` for role substitution, incompatibility, and bundle relation structures, and `A.15.1` for work that actually occurred. Use `A.2.4` or `A.10` when the current object is the evidence-use relation rather than the role-state relation.

### A.2.5:0.1 - Kind Settlement

`RoleStateRelation` is admitted as a direct relation kind under `U.Relation`. It is not a new root kind, a role value, or a state graph.

`RoleStatePredicate` is a local ValueKind declared by this pattern, not another root U-kind. One value specifies a truth condition and temporal reading interpreted through the role assignment's `RoleTaxonomyEpistemeSlot` and `EffectiveReferenceSchemeSlot`. A state name such as `InspectionReady` can designate that predicate under the effective scheme; the name alone does not supply predicate identity.

A `RoleStateAssertion` is a `U.Episteme` whose EntityOfConcern is the exact `U.RoleAssignment` or an explicitly individuated `RoleStateRelation` occurrence, according to the claim. Its ClaimGraph names the `RoleStatePredicate`, the exact direct role-state claim family, and `assertionPolarity: affirmative | negative` for the direct obtaining predicate. An affirmative claim may state the known actual role-state extent only when A.2.5 independently establishes obtaining; a receiving evaluation may separately state its target window. `A.2.4` governs only the compact first evidence-use or status-use classification, while fuller evidence-provenance remains under `A.10`. `A.10` or the separately constituted receiving-evaluation result or reliance assertion owns supported, refuted, or unresolved reliance for the declared use. Neither negative polarity nor unresolved reliance fabricates a world-side occurrence; assertion, reliance posture, evidence episteme, evidence-use relation, and world-side role-state occurrence remain different objects.

A representation episteme may describe predicates, possible configurations, and possible changes. A statechart or state-machine display uses a mathematical or representational lens for that purpose; neither the episteme nor its graph becomes a role-state relation occurrence by displaying one.

### A.2.5:1 - Problem Frame

`U.RoleAssignment` establishes that one admitted system holds one role under a named role-taxonomy episteme and effective reference scheme for an assignment episode. That does not settle whether the assignment currently satisfies the condition needed by a particular method or work claim.

The distinction is easy to see in physical work. `Robot-7` can remain assigned `InspectorRole` through an eight-hour shift while calibration expires at noon. The assignment occurrence continues. The `InspectionReady` role-state occurrence ends when its predicate ceases to hold. A later recalibration can start another role-state occurrence without creating another assignment.

The same distinction appears in social and computational work. An on-call person can be assigned while conflicted or fatigued. A service can hold `ApproverRole` while the relations selected in one model-use structure give the role a fulfilment-approval interpretation and the relations selected in another give it a payment-approval interpretation. A tool-using agent can expose a capability while a concrete action is not admitted for the current task and input values.

The engineering problem is therefore to state the exact assignment, predicate, and interval; state affirmative or negative assertion polarity and the separately governed reliance posture; recognize an obtaining occurrence only when the direct predicate is true; and connect the assertion to the evidence needed by the consequence-bearing use. A universal list of state labels solves none of those tasks.

### A.2.5:2 - Problem

Without a direct role-state relation ontology, six recurring failures appear.

1. **Assignment becomes readiness.** Holding the role is treated as satisfying every state precondition of every method that names it.
2. **State label hides the predicate.** `Ready`, `Approved`, or `Active` travels between role taxonomies even though its truth conditions differ.
3. **Evidence becomes the state.** An evidence or display episteme is treated as the world-side role-state relation.
4. **Missing evidence becomes falsehood.** An unrecovered or stale evidence path is taken as proof that the world-side predicate does not obtain.
5. **Capability becomes admission.** A system's ability to perform an operation is overread as current admission of this concrete method or work claim.
6. **State notation becomes method order.** A transition arrow is treated as the work that changes the state, even though the method, work, transformation, and state-change claim have different ontics.

### A.2.5:3 - Forces

| Force | Tension |
|---|---|
| Lightweight assertion vs reusable identity | Ordinary work needs a short state sentence; later admission, history, or comparison may need one individuated relation occurrence. |
| World-side obtaining vs evidence-backed reliance | A state predicate can hold before anyone measures it, while consequence-bearing use needs a current assertion and evidence relation. |
| Simultaneous predicates vs single-state notation | `Calibrated`, `Synchronized`, and `InRange` may all hold together; a finite-state machine may still be useful for a narrower exclusive configuration. |
| Stable assignment vs changing state | One assignment can contain several state episodes without being recreated at each change. |
| Role meaning vs compulsory model-use structure | Role taxonomy and effective reference scheme determine generic meaning; a receiving assertion or work use may separately designate a selected model-use structure when it changes interpretation. |
| Capability vs action admission | Ability is a neighboring claim; current work admission depends on the exact state predicate and on the direct consumer's rule. |

### A.2.5:4 - Solution

Start from a readable assertion:

> `Robot-7`'s current `InspectorRole` assignment satisfies `InspectionReady` throughout the inspection window.

When a receiving use needs reusable participant typing, use the declared `RelationSignature`. When it needs occurrence identity, apply the world-side identity rule in section 4.3.

#### A.2.5:4.1 - Direct Relation Declaration

This pattern directly governs the `RelationSignature` for `RoleStateRelation`:

| SlotKind | ValueKind | refMode | Meaning |
|---|---|---|---|
| `RoleAssignmentSlot` | `U.RoleAssignment` | `U.EntityRef` | A reference resolving to the exact obtaining assignment occurrence whose holder-in-role state is current. |
| `StatePredicateSlot` | `RoleStatePredicate` | `ByValue` | The exact predicate interpreted through that assignment's role-taxonomy episteme and effective reference scheme. |

These are the only two generic participants. `RoleStateRelation` obtains exactly while the referenced assignment obtains and the by-value predicate is true under its declared temporal reading. Its actual extent is the maximal continuous interval of that obtaining. An affirmative assertion or occurrence description may state the known extent as `roleStateExtent` only for an independently established occurrence; a receiving evaluation may state a separate `declaredRoleStateEvaluationWindow`. Neither temporal value, assertion polarity, nor reliance posture is a relation participant or makes the relation obtain.

When a selected `BoundedModelUseStructure` changes interpretation, designate it in the receiving assertion or work use. It is not an optional participant of generic `RoleStateRelation`. A genuinely structure-dependent relation species requires its own direct pattern, required structure participant, stronger predicate, and occurrence-identity rule.

Evidence is not a participant that makes every role-state relation obtain. A relied-on assertion about the relation uses a direct evidence-use relation. Another world-side occurrence affects predicate truth only when the exact truth condition cites that occurrence under its direct governing pattern.

#### A.2.5:4.2 - Predicate Meaning and Role-Taxonomy Locality

A `RoleStatePredicate` states one exact truth condition for one exact `U.RoleAssignment` under its declared temporal reading. Its by-value content names:

- the role-state designator under the effective reference scheme;
- the exact truth-condition clauses, each naming its world-side object or relation and direct governing pattern;
- the temporal reading, such as truth at an instant, throughout a receiving-use window, or for a declared tolerated portion of that window.

This list defines one predicate value; it is not a union kind. The direct claims keep their own kinds and governing patterns.

The role-taxonomy episteme may state several predicates for one role. The direct consumer separately declares which predicate or conjunction its own admission rule uses. Predicates need not be mutually exclusive. `Calibrated`, `Synchronized`, and `InRange` can obtain simultaneously; `InspectionReady` may be a conjunction over them. Use an exclusive state configuration only when the subject-domain model actually needs one.

A shared label does not establish shared meaning. Reuse across role taxonomies needs either the same by-value predicate under a common effective scheme or an explicit comparison or bridge relation showing which truth and admission effects are preserved.

#### A.2.5:4.3 - Occurrence Identity and Repeated Episodes

Do not replace the identity rule with a tuple key. One `RoleStateRelation` occurrence begins when one fixed `U.RoleAssignment` starts satisfying one fixed `RoleStatePredicate` under that predicate's temporal reading. It continues while the assignment obtains and the predicate remains true without interruption. It ends when the assignment ceases, the predicate ceases to hold, or either participant changes. A later return to truth starts another occurrence.

An affirmative assertion or occurrence description may state the currently known `roleStateExtent` for an occurrence whose obtaining A.2.5 independently establishes. Recording an end boundary for a previously open extent refines the description of the same occurrence when assignment obtaining and predicate truth were uninterrupted. A demonstrated predicate gap separates occurrences. Two descriptions refer to the same occurrence only when they resolve to the same assignment, the same predicate value, and temporal information belonging to that one uninterrupted period.

A changed evidence relation, assertion edition, dashboard display, selected model-use structure in a receiving use, or publication does not create a new world-side occurrence while the same predicate continues to hold. A genuinely structure-dependent relation species can have another identity law only under its own direct pattern.

An evidence gap gives the receiving use unresolved reliance on the assertion. It does not demonstrate a gap in predicate obtaining or add a third assertion polarity. A direct observation or constituting occurrence may demonstrate such a gap only when its governing pattern supports that stronger world-side claim.

#### A.2.5:4.4 - Assertion and Evidence Use

For a relied-on role-state claim, keep this order:

1. name the exact `U.RoleAssignment`, by-value `RoleStatePredicate`, exact direct role-state claim family, and affirmative or negative assertion polarity;
2. when A.2.5 independently establishes that the relation obtains and a receiving use needs occurrence identity, individuate it under section 4.3; neither negative polarity nor unresolved reliance invents an occurrence;
3. state a `RoleStateAssertion : U.Episteme` whose ClaimGraph carries the predicate, exact direct claim-family reference, affirmative or negative `assertionPolarity`, the known `roleStateExtent` only for an affirmative claim about an independently established occurrence, and any separately current `declaredRoleStateEvaluationWindow`; leave compact first evidence-use or status-use classification to `A.2.4`, and keep supported, refuted, or unresolved reliance with `A.10` or the separately constituted receiving-evaluation result or reliance assertion;
4. if a selected model-use structure changes this interpretation, designate it in that assertion or receiving use rather than in the generic relation;
5. use `A.2.4` for compact evidence use, expanding through `A.10` only when fuller evidence-basis detail changes the relied-on use;
6. let the direct consumer use the supported assertion under its own governing pattern.

When role-state evaluation itself is current, name the exact evaluation work `W_eval : U.Work`, the admitted system that performed it, and the exact evaluator assignment through `F.6` `performedUnderAssignment(W_eval, RA_eval)`. Any separately constituted evaluation result is a `C.2.1` episteme whose ClaimGraph states the role-state judgment about the subject assignment or independently established occurrence. That work, its performer and assignment, the result episteme, its provenance under exact direct relations, and the receiving reliance evaluation remain neighboring governed objects; none becomes a `RoleStateRelation` participant or identity discriminator.

The actual role-state extent, target evaluation window, and evidence-relevance interval answer different questions. The first is derived from uninterrupted world-side obtaining. The second asks whether the predicate holds over a window selected by the receiving use. The third states when a particular episteme remains relevant enough to support the assertion. A calibration report can remain the same episteme while its relevance expires; that expiration lowers reliance without retroactively rewriting an earlier role-state occurrence.

For the declared use, supported, refuted, or unresolved reliance belongs to the separately constituted receiving-evaluation result or reliance assertion. This posture is neither a third assertion polarity nor a world-side role-state value and does not enter relation identity.

#### A.2.5:4.5 - Work-Admission Use

A.2.5 supplies the current state relation and the exact `RoleStateAssertion` form with affirmative or negative assertion polarity. `A.10` or the separately constituted receiving-evaluation result or reliance assertion owns any supported, refuted, or unresolved reliance posture for the declared use. A.2.5 does not itself select a method, create a gate decision, or assert that work occurred.

For a consequence-bearing admission use, the system performing the consumer's exact evaluation or decision work applies that consumer's direct governor and checks these conditions:

1. the exact `U.RoleAssignment` obtains throughout the receiving decision or work window;
2. the direct consumer declares one exact `RoleStatePredicate`; its truth condition may contain an explicit conjunction;
3. each relevant assignment has an obtaining `RoleStateRelation` whose actual extent covers the receiving-use window under the same effective reference scheme or an explicit bridge relation;
4. the assertion relied upon has the evidence relation and currentness needed by that consumer;
5. every other admission condition used by that consumer is separately established under its direct governing pattern.

The consumer's direct governor, not A.2.5, defines any admit, deny, defer, or unresolved outcome; exact system-performed decision work and its result remain separately governed. A.2.5 contributes no generic admission outcome; it contributes the exact state relation on which that decision work relies.

#### A.2.5:4.6 - Role-Relation Structure Use

When `A.2.7` selects role-substitution, incompatibility, or role-bundle relations, state sensitivity is expressed over exact assignments, predicates, and windows.

- Substitution is preserved only when the candidate role's current predicate entails the selected admission predicate under the declared scheme or bridge.
- Incompatibility is stated over the overlapping windows and predicate conditions in which the conflict actually appears.
- A work claim needing several roles uses the relevant role-state occurrences for each assignment. It does not require a Cartesian product of every possible state label.

If a role taxonomy declares a genuinely distinct composite `U.Role`, that role may have its own predicates and assignments. Mere conjunction for one work claim does not create a composite role value.

#### A.2.5:4.7 - State-Machine and Change Lenses

Use statecharts or state machines when mutually exclusive configurations, orthogonal regions, guarded changes, or event handling improve the subject-domain model. The notation describes possible configurations and changes; it does not replace the direct relation occurrence.

A change arrow represents a proposed or observed change in predicate truth; it is not the world-side change by form. Recover the exact changed object or relation, then use the direct pattern governing the exact claim that establishes the change. The statechart neither supplies a common world-side kind nor prescribes method order by itself.

When the model needs continuous coordinates rather than discrete labels, use `A.19` for the characteristic space and let the by-value state predicate select a region, band, ordering condition, or other exact condition over those coordinates. Measurement and evaluation stay with `C.16` and their direct patterns.

#### A.2.5:4.8 - Interpretation Qualification in the Receiving Use

Most role-state claims need no bounded-model-use structure. The assignment's role-taxonomy episteme and effective reference scheme already supply generic semantic locality.

When an independently selected `BoundedModelUseStructure` changes how a receiving assertion or work use interprets the state predicate, designate that structure in that assertion or use. Do not add an optional participant to generic `RoleStateRelation`. The structure organizes model-use relations; it does not hold the role, evaluate the predicate, make the relation obtain, or admit the work.

### A.2.5:5 - Working Guidance

1. Write the readable sentence naming the current assignment and predicate; name the receiving-use window only when the current check selects one.
2. Recover the predicate by value from the role-taxonomy episteme and effective reference scheme; do not stop at the state label.
3. Derive the actual maximal continuous extent from assignment obtaining and predicate truth; separately check any receiving-use window against that extent.
4. Ask whether a receiving use needs occurrence identity. If not, keep the readable assertion and stop.
5. For relied-on use, make the assertion episteme, affirmative or negative assertion polarity, exact direct claim-family reference, and direct evidence-use relation explicit; record supported, refuted, or unresolved reliance separately, and do not treat absent evidence as negative polarity or world-side nonobtaining.
6. Leave capability fit, method selection, gate outcome, assurance, and performed work with their direct governing patterns.
7. When a model-use structure changes interpretation, designate it in the receiving assertion or use, never in the generic relation signature.

### A.2.5:6 - Worked Slices

#### A.2.5:6.1 - Robot Inspection After Recalibration

`Robot-7` already has the assignment occurrence governed by `A.2.1`:

```text
RoleAssignmentAssertion@Robot7Inspection:
  participantDesignations:
    HolderSystemSlot: Robot-7
    RoleValueSlot: InspectorRole
    RoleTaxonomyEpistemeSlot: MaintenanceRoles-2026
    EffectiveReferenceSchemeSlot: Maintenance-Scheme-A
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]
```

The method description for a bearing inspection declares the by-value admission predicate `InspectionReady`, interpreted as calibration current, clock synchronization inside the declared tolerance, operating-envelope fit, and no active quarantine relation throughout the inspection window. The following filled assertion refers to one obtaining role-state occurrence; it is not the `RelationSignature` and does not create the occurrence by being recorded.

```text
RoleStateAssertion:
  directClaimFamilyRef: A.2.5 RoleStateAssertion
  RoleAssignmentSlot: Robot-7-InspectorAssignment-2026-07-13
  StatePredicateSlot:
    DesignatorUnderScheme: InspectionReady under Maintenance-Scheme-A
    TruthCondition: CalibrationCurrent(Robot-7)
                    and ClockSynchronizationWithinTolerance(Robot-7)
                    and InspectionOperatingEnvelopeFit(Robot-7)
                    and no ActiveQuarantineRelation(Robot-7)
    TemporalReading: continuous truth over the declared inspection interval
  assertionPolarity: affirmative
  roleStateExtent: [2026-07-13T09:20, 2026-07-13T12:00]
```

The calibration report is a `U.Episteme`. An A.2.4 evidence-use relation targets the assertion that this role-state occurrence obtains. At noon the declared calibration-validity interval ends, so `InspectionReady` ceases to hold under its own truth condition. The evidence-use relation may also cease to support a current assertion when its relevance interval ends, but that is a separate claim. The assignment continues until 17:00. Recalibration at 12:30 can begin another `InspectionReady` occurrence under the same assignment.

#### A.2.5:6.2 - Drive Motor in a Pump Assembly

`Motor-M1` holds `DriveMotorRole` under `PumpAssemblyRoles-v4` and `Pump-A-Operating-Scheme`. The current work claim needs `DriveReady`, whose predicate names the exact supply relation, torque capability-fit relation, thermal band, and installed-connection relation.

The pump assembly is the grounding system for those claims. It is not a mandatory context slot. No `BoundedModelUseStructure` is needed because the role taxonomy, scheme, assignment, direct physical relations, and state window determine the claim.

This case also shows why capability and role state differ. The motor can retain torque capability while a missing supply relation makes `DriveReady` false. Conversely, an affirmative current `DriveReady` assertion does not say that pumping work has occurred, and its receiving-use reliance remains separately governed.

#### A.2.5:6.3 - Socially Constituted Credential State

A clinician holds `ProcedureOperatorRole` for one shift. The selected admission predicate `CredentialCurrentForProcedure-X` depends on an accepted credential decision, its declared validity interval, and absence of a suspending decision.

Here the accepted decision relation helps constitute the institutional predicate because the credential ontology says so. A certificate publication may evidence that decision, but the publication does not substitute for it. The role-state occurrence still has assignment and predicate as its participants and derives its actual extent from uninterrupted obtaining; evidence and publication remain direct neighboring relations.

#### A.2.5:6.4 - DDD Model-Use Structure Changes a Receiving Interpretation

`ApprovalService-2` holds `ApproverRole`. In one selected model-use structure, `ApprovalReady` concerns a fulfilment-state change. In another, the same source label concerns payment authorization. The generic `RoleStateRelation` still has only the exact assignment and by-value predicate as participants.

When the fulfilment-side assertion is evaluated, its ClaimGraph or receiving-use relation may designate `Orders-Fulfilment-ModelUseStructure` beside the state claim. That designation selects how the receiving use interprets the predicate; it does not enter the generic relation signature or occurrence identity. The structure must already exist under `A.1.1`. It neither evaluates `ApprovalReady` nor performs approval work.

#### A.2.5:6.5 - Approved Standard or Evidence Dataset Is a Different Relation

Suppose a project says, "Standard S is approved." The standard is an episteme, not a system holding a work-facing role. Recover the direct status-use, decision, source-use, or publication-use relation.

Likewise, a dataset or report described as having an "evidence role" remains an episteme used through direct evidence, source, measurement, freshness, provenance, or assurance relations. Apply A.2.5 only if an admitted system's role assignment has a by-value predicate whose truth condition depends on one of those separately governed relations; neither the standard nor dataset becomes the holder, state, or role-state occurrence.

### A.2.5:7 - Archetypal Grounding and Bias Control

**Physical system.** A motor, robot, laboratory instrument, or production cell can hold a role while a role-state predicate changes as physical relations and measured characteristics change.

**Human or organizational system.** A person, team, or organization can remain assigned while a current conflict, credential, fatigue, resource, or decision relation changes the state predicate relevant to one work claim.

**Computational system.** A service or agent can expose a capability while each concrete action still needs current assignment, state predicate, task relation, and direct authorization or gate evaluation. This is one specialization, not the universal meaning of role state.

**Episteme boundary.** A representation or evidence episteme can describe or support a role-state claim. It does not become the holder or world-side occurrence by being visible.

The main bias risk is label-first reasoning. A familiar state word invites the reader to skip predicate recovery. The repair is always constructive: recover the assignment, predicate by value, state window, assertion, and evidence-use relation needed by the receiving use.

### A.2.5:8 - Conformance Checklist

| Check | Question |
|---|---|
| `CC-A2.5-01` | Is the current object one `RoleStateRelation : U.Relation`, rather than a role value, capability, assertion episteme, evidence relation, diagram, gate outcome, or work occurrence? |
| `CC-A2.5-02` | Does `RoleAssignmentSlot` resolve to one obtaining `U.RoleAssignment` with its four exact participants and maximal continuous assignment extent? |
| `CC-A2.5-03` | Is `StatePredicateSlot` present by value, with an exact truth condition and temporal reading rather than only a state label? |
| `CC-A2.5-04` | Is actual role-state extent derived from uninterrupted predicate truth while the assignment obtains, with any target evaluation window kept in the receiving use? |
| `CC-A2.5-05` | When occurrence identity is needed, does the identity rule use the fixed assignment, fixed predicate value, and uninterrupted obtaining rather than a representation key or temporal participant? |
| `CC-A2.5-06` | Are a demonstrated predicate gap and a mere evidence gap distinguished? |
| `CC-A2.5-07` | Does `RoleStateAssertion` keep predicate, exact direct claim-family reference, affirmative or negative assertion polarity, known actual extent only for an affirmative claim about an independently established occurrence, and any receiving-use window distinct, while supported, refuted, or unresolved reliance and evidence relations remain separate and fabricate no occurrence? |
| `CC-A2.5-08` | Are capability fit, method selection, gate outcome, assurance, and performed work left with their direct patterns? |
| `CC-A2.5-09` | If several predicates hold together, are they composed explicitly rather than forced into one exclusive state label? |
| `CC-A2.5-10` | Does cross-taxonomy reuse preserve predicate meaning and admission effect through the same scheme or an explicit bridge relation? |
| `CC-A2.5-11` | Is any selected model-use structure designated only in the receiving assertion or use, with no optional `ModelUseStructureSlot` in the generic relation? |
| `CC-A2.5-12` | If a statechart or graph is used, is it kept as a lens or description of possible configurations and changes? |

### A.2.5:9 - Common Failure Modes and Repairs

| Failure | Observable symptom | Repair |
|---|---|---|
| Assignment-as-readiness | A work claim proceeds because a holder is assigned. | Name the selected admission predicate and establish the corresponding role-state relation and supported assertion for the work window. |
| State-label transport | Two taxonomies use `Ready` as if it meant the same predicate. | Compare predicates by value under their schemes or declare a bridge with preserved and lost effects. |
| Evidence-as-state | A certificate or dashboard display is entered as the role state. | Keep the state relation world-side; target its assertion with the direct evidence-use relation. |
| Evidence-gap-as-false | A missing current report closes a role-state episode. | Record unresolved reliance for the receiving use; close the occurrence only when the predicate's direct truth condition is demonstrated not to hold. |
| Capability-as-admission | Tool exposure or measured ability admits a concrete action. | Keep capability in A.2.2; require exact system-performed consumer evaluation of current state and action-specific conditions. |
| Method-order drift | Transition arrows are used as the procedure. | Name the work, transformation, decision, or event occurrences that change predicate truth and put order in the method description. |
| Product-state explosion | A multi-role work claim enumerates every combination of state labels. | Use separate role-state occurrences and the exact conjunction needed by the current claim; introduce a composite role only when its taxonomy and assignment are real. |

### A.2.5:10 - Consequences

Benefits:

- one assignment can support several separately identifiable state episodes;
- simultaneous predicates remain expressible without pretending every case is a single-state automaton;
- state truth, state assertion, evidence use, and work admission can change independently and be repaired locally;
- method and gate patterns receive an exact current relation instead of a status label;
- physical, social, organizational, and computational role-state cases use the same relation discipline.

Costs and limits:

- load-bearing state predicates must be written by value, including temporal semantics;
- consequence-bearing use needs evidence currentness and an explicit direct consumer;
- cross-taxonomy reuse may need a bridge rather than label matching;
- A.2.5 does not define every subject-domain state predicate, measurement method, authorization relation, or state-change method.

Reopen or lower only the affected claim when the assignment episode, by-value predicate, actual role-state extent, receiving-use evaluation window, effective scheme, evidence relevance, direct consumer rule, or interpretation-changing model-use selection changes. Do not rewrite the role value or assignment when only one role-state episode changes.

### A.2.5:11 - Rationale

The pattern starts from the world-side relation because state claims can matter before a record exists. A robot can cease to satisfy its inspection predicate before a dashboard refreshes. A credential decision can constitute an institutional state before a certificate is published. A supported assertion is therefore necessary for reliance but is not the world-side state's truth-maker by default.

Using uninterrupted predicate truth as the identity boundary distinguishes repeated episodes even when assignment and predicate values stay the same. An assertion or occurrence description may state the known actual extent and refine an open end to a closed end without creating another occurrence.

The direct relation also explains why role state is not capability and not work. Capability says what operations a system can perform in an envelope. Role state says whether a current assignment satisfies one predicate over a window. Work says what change actually occurred. A method, gate, or work pattern may depend on all three, but no one of them proves the others.

### A.2.5:12 - SoTA-Echoing

| Current or mature line | What it contributes | Concrete mutation in A.2.5 |
|---|---|---|
| [W3C SCXML 1.0](https://www.w3.org/TR/scxml/), a mature 2015 Recommendation rather than current competitive SoTA | Explicit states, parallel regions, guarded transitions, events, and executable state-machine semantics. | Keep statecharts available when the subject-domain model needs them, but type them as mathematical or description lenses rather than the world-side relation occurrence or universal method order. |
| Esparza and Fischer, [Runtime Verification for LTL in Stochastic Systems](https://arxiv.org/abs/2508.07963), 2025 | Runtime monitoring distinguishes true, false, and inconclusive results; finite observations do not settle every temporal property. | Treat incomplete evidence as unresolved for the relying use, preserve the predicate's temporal reading, and do not close an occurrence merely because a finite evidence path is silent. |
| [Cedar Policy Language current reference](https://docs.cedarpolicy.com/policies/syntax-policy.html) | Fine-grained decisions evaluate a concrete principal, action, resource, current attributes, and request-time conditions rather than a role label alone. | Require the system performing consumer decision work to combine current assignment, exact predicate, state window, and action-specific relations. Keep this as an implementable software specialization rather than the ontology of every role state. |
| Zuvic, [Capability Gates Are Not Authorization](https://arxiv.org/abs/2606.28679), 2026 preprint | A current agent-framework audit distinguishes exposed capability from per-call, value-sensitive authorization and reports fail-closed enforcement experiments. | Keep capability in A.2.2 and require the consumer to evaluate the concrete state and action claim before side effects; do not infer authorization from tool exposure. The empirical scope remains the audited software frameworks. |
| Liu et al., [A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469), 2026 preprint | Task alignment, action alignment, source authorization, and data isolation require runtime checks over the current task and action. | In agentic cases, require the work or authorization consumer's governing claim to name the current task and action relations; A.2.5 supplies only the exact role-state relation and exact `RoleStateAssertion` form, while `A.10` or the separately constituted receiving-evaluation result or reliance assertion owns any supported, refuted, or unresolved reliance posture. |
| `A.6.REL`, `A.2.1`, `A.19`, `A.2.4`, and `A.10` | FPF already separates relation obtaining, occurrence identity, assignment episodes, characteristic-space predicates, assertions, and evidence use. | Give A.2.5 an occurrence identity rule, preserve the lightweight assertion path, and keep evidence outside generic state identity. |

These sources do not turn A.2.5 into an IT access-control pattern. Their transferable contribution is narrower: current action decisions need exact participants and predicates; temporal monitoring can remain unresolved; capability and action admission differ; and state-machine notation is optional modeling machinery.

### A.2.5:13 - Relations

| Related pattern | Relation |
|---|---|
| `A.2` | Governs `U.Role` and the role-taxonomy episteme through which role-state predicates are interpreted. |
| `A.2.1` | Governs the `U.RoleAssignment` occurrence referenced by every role-state relation. |
| `A.2.2` | Governs capability and operating-envelope claims that a state predicate may reference but does not replace. |
| `A.2.4` and `A.10` | Govern compact evidence use and full evidence-provenance support for the role-state assertion. |
| `A.2.7` | Governs role-substitution, incompatibility, and bundle relation structures that may consume current role-state occurrences. |
| `A.6.REL` | Governs progressive relation-occurrence individuation and occurrence-as-participant use. |
| `A.6.5` | Governs SlotKind, ValueKind, and reference-mode discipline for the direct declaration. |
| `A.19` and `C.16` | Govern characteristic spaces, predicates over measured coordinates, measurement, and comparability when those are used by a state predicate. |
| `A.15`, `A.15.1`, `A.15.2`, and `A.21` | Govern method participation, performed or planned work, and gate outcomes that consume role-state claims. |
| `A.1.1` | Governs any selected `BoundedModelUseStructure` designated by a receiving assertion or use; it is not a generic role-state participant. |
| `C.27` and `G.11` | Govern temporal currentness, decay, and evidence refresh when those claims are current. |

### A.2.5:End

