## A.20 - Constraint Validity for Transformation Steps

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain name.** Internal-constraint check.

**Technical result name.** `ConstraintValidityResult`.

### A.20:0 - Use this when

Use A.20 when one transformation or one operation application is current in a transformation-flow structure and the question is whether that subject satisfies one named internal constraint for one stated case. It also applies when an A.6.4 bounded-use assertion q is current there and q's exact proposition is the named internal constraint. A.6.4 retains the separate current-case judgement.

**First useful move.** Write one sentence:

> For subject S and case facts I, constraint C is applicable and required; test T returned outcome O under window W, with witness or reason R.

**Quick worked case.** `TemperatureConversion-7` must add 273.15 to a Celsius input and must not return a value below 0 K. For input 25 °C, the test returns 298.15 K, so both required conditions are `satisfied`; the witness records the formula edition, input, output, and test result for this evaluation window. The practitioner may reuse this result for that case and window, or pass it to a current gate or assurance use; changed input, formula edition, assumptions, or window requires another check. If the output were 297.15 K, the formula condition would be `violated`; if no output could be recovered, it would be `unknown`; if the test had not run, its evaluation state would be `notRun`.

Stop after that result unless a gate, assurance argument, publication, or another named task needs it. Path and crossing structure, refresh, gate decisions, evidence, assurance, Work, and semantic bridges keep their own patterns.
**What goes wrong if missed.** A class label or green status replaces the actual constraint and test. An unknown or unrun required check disappears inside `pass`. A failed local constraint makes unrelated gate-fit facts look inapplicable. A.20 then starts redefining paths, publications, refresh, gates, or retargeting instead of reporting its own result.

**What this buys.** A practitioner can see which constraint was tested, why it applied, what case was used, what the result means, and which later decision may consume it.

**Not this pattern when.**

- Use `A.21` for a gate decision or profile consequence.
- Use `E.18` for transformation-flow positions, paths, crossings, valuations, or `PathSlice` identity.
- Use `E.17` for publication forms and faces, `G.11` for refresh work, and `C.27` for temporal-claim adequacy.
- Use `A.6.4` for retargeting semantics and `F.9` only for a separately claimed semantic correspondence.
- A `Signature`, WorkPlan, dated Work, or gate check does not enter A.20 merely because it occupies an E.18 position; use the pattern that defines the actual claim.

### A.20:1 - Problem frame

An E.18 transformation-flow structure may place a transformation beside signatures, mechanism descriptions, work-planning material, Work, checks, and retargeting material. Those neighboring values do not all have the same internal constraints.

A.20 addresses a narrower question: one identified subject is tested against one identified constraint under stated assumptions and case facts. The result may later be used by a gate or assurance argument, but it is not itself a gate decision or policy consequence.

### A.20:2 - Problem

How can FPF report internal constraint validity without:

- inventing a world-side `FlowConstraintValidity` relation whose participants are unspecified;
- using one status value for not applicable, not run, unknown, policy degradation, and gate blocking;
- requiring every specialist constraint for every transformation;
- suppressing independently useful gate-fit results after one local failure;
- copying publication, path, refresh, gate, or retargeting architecture into A.20; or
- treating an entity reference as a semantic bridge or requiring every retargeting to be reversible?

### A.20:3 - Forces

| Need | Tension |
| --- | --- |
| Small local result | A user needs one check result, while later replay needs its constraint, case, and window. |
| Open constraint families | Different transformations carry different laws; a fixed universal checklist would create false requirements. |
| Truth and policy separation | Whether a constraint holds is not the same as what a gate does with the result. |
| Missing information | Not applicable, not run, unknown, and error lead to different next actions. |
| Reuse without fanout | A reusable result must be precise without copying every possible consumer's record and policy. |

### A.20:4 - Solution

#### A.20:4.1 - Result ontology

`ConstraintValidityResult` is a C.2.1 result episteme. It is not a new U-kind and not a world-side relation. Its exact EntityOfConcern is the constrained subject. Its ClaimGraph states one application of one named constraint to one case.

The constrained subject is normally:

1. one independently identified `U.Transformation` used at an E.18 transformation position;
2. one A.6.1 operation application whose internal law is being tested; or
3. the exact proposition carried by one A.6.4 bounded-use assertion q, only when that proposition is the named internal constraint. q remains a C.2.1 episteme about exact arrow r; its ClaimGraph and the separate current-case judgement remain under A.6.4, and any actual operation application remains separate.

Another subject is admissible only when its own pattern defines a named internal constraint and states why this result form applies. An E.18 locus label alone supplies neither the subject nor the constraint.

Minimum result content:

```text
ConstraintValidityResult:
  resultRef: C.2.1 episteme
  constrainedSubjectRef:
  constraintRef:
  constraintEdition:
  applicabilityValue: required | optional | notApplicable
  applicabilityBasis:
  caseFacts:
  referenceSchemeAndScope:
  evaluationWindow:
  evaluationState: evaluated | notRun
  outcome?: satisfied | violated | unknown | error
  witnessOrReason:
  effectiveUseWindow?:
  evaluationWorkRef?:
```

`outcome` is present only when `evaluationState=evaluated` and `applicabilityValue` is `required` or `optional`. A not-applicable constraint records the reason it is outside this case. A not-run constraint records that evaluation work has not produced a result. Neither is `unknown` and neither silently counts as success.

If a dated evaluation Work occurrence matters, cite it separately through `evaluationWorkRef`; the Work and result episteme do not become one object.

The legacy label `FlowConstraintValidity` may be retained only as a locator for this result family. It does not name a relation, gate status, publication record, or flow-wide property.

#### A.20:4.2 - Applicability, required set, and summary

Before evaluation, name the constraints applicable to the current subject and case. Mark each as `required`, `optional`, or `notApplicable` and state why. The required set is complete only when every constraint that the current use depends on is named.

For one evaluated applicable constraint:

- `satisfied` means the test established the named constraint for the stated case and window;
- `violated` means the test established a counterexample or failed condition;
- `unknown` means required facts, applicability facts, or witness content could not be determined;
- `error` means the selected evaluation could not complete correctly.

When a consumer needs one local summary over the complete required set, use:

`ConstraintValiditySummary ∈ {satisfied, violated, unresolved, notApplicable}`.

The summary rule is:

1. `notApplicable` only when the declared required set is empty because no A.20 internal constraint applies to this subject and use;
2. `violated` when at least one required result is `violated`;
3. `unresolved` when no required result is violated but at least one required constraint is `notRun`, `unknown`, or `error`; and
4. `satisfied` only when every required applicable constraint has an evaluated `satisfied` result.

Optional results do not change the summary unless a separately accepted use decision moves their constraints into the required set. A missing required result can therefore never disappear beside a satisfied result.

#### A.20:4.3 - Constraint families and outcome rules

The following families are recognition aids, not a universal required list. Each application still names the actual constraint, edition, assumptions, case facts, and test.

| Constraint family | Trigger | `satisfied` means | Other outcomes |
| --- | --- | --- | --- |
| Type, domain, and range | The subject consumes or produces typed values. | Every case input and result used by the claim lies in the declared type, domain, and range. | A counterexample is `violated`; unavailable values are `unknown`; a failed test is `error`. |
| Admissibility conditions | The operation or transformation declares guards or admissible cases. | Every required guard is true for the case and window. | A false guard is `violated`; undetermined guard truth is `unknown`. |
| Law or invariant set | The current claim relies on a named law or invariant. | The named invariant holds for the case under its assumptions. | A counterexample is `violated`; missing case facts or witness content are `unknown`. |
| Quantity and unit coherence | The current operation combines quantities or units. | The case is coherent under the already declared quantity, unit, and reference-scheme rules. | A mismatch is `violated`; an unrecovered declaration is `unknown`. A.20 does not define or translate units or planes. |
| Sensitivity or stability bound | A robustness, continuity, perturbation, safety-envelope, or stability claim actually depends on a bound. | The cited bound covers the stated domain, assumptions, distance or norm, and case. | A counterexample is `violated`; absent assumptions or certificate content are `unknown`. No bound is required without this trigger. |
| Return-shape preservation | A consumer relies on a declared set, archive, order, or other non-scalar result shape. | The transformation preserves that declared shape for the current case. | Hidden scalarization or lost required structure is `violated`; unrecovered shape facts are `unknown`. A.20 does not rank or select the result. |
| A.6.4 retargeting invariant | The exact proposition in q is the named internal constraint for the current use; q remains the C.2.1 bounded-use assertion about r. | Exact current case facts establish the proposition as stated, including its invariant, visible loss, named receiving use, conditions, and polarity. | A counterexample is `violated`; a missing deciding fact is `unknown` unless the constraint itself makes absence a failure. This A.20 result may enter the case basis for A.6.4's separate `satisfies`, `fails`, or `cannot decide` judgement; it is not that judgement, and the exact current facts remain separately named. r and any application remain separate. |

The constraint's own pattern supplies its truth condition. A.20 supplies the application result form and summary only.

#### A.20:4.4 - Gate and policy boundary

An A.21 gate may consume an exact A.20 result or summary as one declared input. A.20 does not translate `satisfied`, `violated`, or `unresolved` into `pass`, `degrade`, `block`, or `abstain`; A.21 applies the current gate rule to its complete check set.

Every other applicable gate-fit check keeps its own result. A failed or unresolved internal constraint may prevent the aggregate gate decision from passing, but it does not make freshness, system-role fit, channel fit, regulatory conformance, reference-plane crossing, or another independent fact undefined or not applicable.

An implementation may defer expensive evaluation work after an already blocking result. That is a Work or evaluation policy. A deferred required check remains `notRun`; it is not published as not applicable or as a successful neutral value. Any aggregate decision must preserve that incompleteness under A.21.

#### A.20:4.5 - Retargeting boundary

For a `StructuralReinterpretation` use, receive the exact A.6.4 arrow r and q, a C.2.1 bounded-use assertion about r. q's ClaimGraph states the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. A.20 opens only when that exact proposition is the named internal constraint. The separate A.6.4 current-case judgement compares exact current facts with q and returns `satisfies`, `fails`, or `cannot decide`; it is not the A.20 result. If an actual operation application is also current, identify and test it separately.

A.20 returns only a `ConstraintValidityResult` for that named internal constraint. That result may enter the case basis for the separate A.6.4 current-case judgement; the exact current facts remain separate, and the result reidentifies neither r nor q and records no application. It leaves `EntityOfConcernRef` as an entity reference and adds no `KindBridge` or UTS row. An isomorphism or lens, including reverse `put` and Put-Get or Get-Put laws, enters only as a separately current reversibility claim under its own governor.

Use F.9 separately only when the current claim also needs an obtaining semantic correspondence between two exact F.17 local senses. Keep its bounded-use claim, optional `CL`, evidence, and reliance separate; A.20 creates none of them.

#### A.20:4.6 - Neighboring claims

A.20 keeps only the result content needed to reuse the internal-constraint finding. When another claim is current:

- `E.17` defines publication relations and faces;
- `E.18` defines structure positions, transfers, paths, crossings, and `PathSlice` identity;
- `G.11` defines refresh planning and performed refresh work;
- `C.27` defines temporal-claim adequacy;
- `A.21` defines check applications, profile use, gate aggregation, and decision consequences;
- `A.10` and `B.3` define evidence use and assurance; and
- `A.15` defines plans and dated Work.

Citing an A.20 result in one of those claims does not copy that consumer's identity, scheduling, publication, or policy fields into A.20.

### A.20:5 - Worked cases

#### A.20:5.1 - Satisfied unit-conversion constraint

`TemperatureConversion-7` converts a Celsius input to kelvin. The named constraint says that the output must equal the input plus 273.15 K and must remain at or above 0 K. It is required for this use. For input 25 °C, the test obtains 298.15 K and a non-negative result, so the outcome is `satisfied`. The witness records the input, formula edition, output, and test result for this evaluation window.

The local summary is `satisfied` because this is the complete required set for the stated case. That result does not say that a release gate passed or that conversion Work occurred.

#### A.20:5.2 - Violation and missing-witness variants

If the same implementation returns 297.15 K for 25 °C, the formula constraint is `violated` and the returned values are the counterexample. If the implementation output cannot be recovered, the outcome is `unknown`, not `violated` and not `satisfied`. If the test was never run, its evaluation state is `notRun` and the summary is `unresolved`.

#### A.20:5.3 - Lossy retargeting

Suppose an A.6.4 arrow r relates an episteme about a detailed equipment classification to one about three maintenance classes. A separate q affirmatively states that the receiving classes preserve the maintenance action selected for every source case under named conditions and allows loss of manufacturer-specific distinctions for that use. Because that exact proposition is the named internal constraint here, A.20 tests it on the stated cases. No reverse mapping is part of that constraint. Exact facts that establish the invariant and keep loss within the boundary yield the A.20 outcome `satisfied`; a counterexample yields `violated`; a missing deciding fact yields `unknown`. The separate A.6.4 current-case judgement then compares all exact current facts with q's conditions and proposition and reports `satisfies`, `fails`, or `cannot decide`; the A.20 outcome does not replace it. Any operation that produced the receiving episteme remains separate.

### A.20:6 - Bias annotation

- **Status bias.** A green field or class label can look like a result. Recover the constraint application and case.
- **Gate bias.** A local constraint result can look like permission or release. Keep the gate decision separate.
- **Checklist bias.** A familiar list can look universally required. Select only the constraints triggered by the actual subject and use.
- **Formalism bias.** A reversible optic can look more rigorous than a lossy but adequate case. When q's proposition is the named internal constraint, test that proposition under its stated invariant and loss boundary; keep any separately claimed reversibility relation under its own governor.

### A.20:7 - Check the ordinary local result

For an ordinary A.20 use, check only these five points:

1. **Subject and constraint (`CC-A20-1`).** Name the exact subject and the exact constraint and edition being applied.
2. **Case and applicability (`CC-A20-2`).** State the assumptions, case facts, scope, evaluation window, and why the constraint is `required`, `optional`, or `notApplicable`.
3. **Evaluation and outcome (`CC-A20-2`).** Record `evaluated` or `notRun`. For an evaluated applicable constraint, record `satisfied`, `violated`, `unknown`, or `error` under the constraint's own outcome rule.
4. **Support (`CC-A20-1`).** Give the witness, counterexample, missing-information reason, or error reason that supports that result.
5. **Complete summary (`CC-A20-3`).** Use `ConstraintValiditySummary=satisfied` only when every constraint in the complete declared required set was evaluated and satisfied.

A specialist constraint such as a stability bound, return-shape condition, or retargeting invariant is present only when its trigger in section 4.3 applies (`CC-A20-4`).

#### A.20:7.1 - Extensions only when another use is current

| Trigger | Additional check | Direct pattern |
| --- | --- | --- |
| A gate consumes the result | Keep every applicable GateFit result independently recoverable; an A.20 failure changes only the A.21 aggregate under its current rule (`CC-A20-5`). A deferred required check remains `notRun` (`CC-A20-6`). | `A.21` |
| The exact proposition in an A.6.4 bounded-use assertion q is the named internal constraint | Apply A.20 to that proposition for the stated case and return only its `ConstraintValidityResult`; keep r, q, any operation application, and the A.6.4 current-case judgement separate. A Bridge or reversibility claim enters only when separately current (`CC-A20-8`). | `A.6.4`; add `F.9` only for a separate semantic-correspondence claim |
| Publication, structure, time, refresh, evidence, assurance, or Work is current | Keep those claims in their own result or relation and follow the direct pattern (`CC-A20-9`). A.20 adds no publication-face, path, slice, scheduler, gate-profile, or gate-algebra fields (`CC-A20-7`). | `E.17`, `E.18`, `C.27`, `G.11`, `A.10`, `B.3`, or `A.15`, as applicable |

### A.20:8 - Common mistakes

| Mistake | Why it fails | Repair |
| --- | --- | --- |
| Class label as truth | `LipschitzBounds` or `TypeDomainRange` does not identify the constraint application. | Name the constraint, edition, case, test, and result. |
| `abstain` for everything missing | Not applicable, not run, unknown, and policy consequence require different actions. | Keep applicability, evaluation state, outcome, and gate consequence separate. |
| Missing required result joins to pass | A neutral element erases incompleteness. | Use the complete required-set summary rule. |
| Constraint failure suppresses GateFit | Independent repair information disappears and results depend on evaluation order. | Preserve each applicable result; let A.21 combine them. |
| A.20 becomes a package architecture | Publication, paths, refresh, and gate fields are copied into a local result. | Keep only the result and cite the consumer's pattern. |
| Entity reference becomes bridge | Retargeting and semantic correspondence are confused. | Use A.6.4; add F.9 only for a separate cross-semantic claim. |

### A.20:9 - Consequences

The result is smaller and more reusable. A missing check can no longer disappear as success, and a gate can retain useful independent findings even after one internal failure. The cost is that a consequence-bearing use must name its required constraint set and cannot hide policy inside A.20 status words.

### A.20:10 - Rationale

Constraint truth, knowledge about that truth, and a policy response are different. A.20 records the evaluation result. The constraint's own pattern defines the truth condition. A.21 or another consumer decides what follows. Keeping those steps separate removes evaluation-order dependence and prevents a local validity pattern from becoming a second architecture for flows, publication, refresh, and gates.

### A.20:11 - SoTA echo

| Current practice line | Adopted move | Limit |
| --- | --- | --- |
| Refinement-type, property-based, and proof-carrying validation | Name the property, case, outcome, and witness rather than publishing an unqualified validation label. | A witness supports only the stated property and case. |
| Dimensional analysis and assumption-bound numerical validation | Keep quantity, unit, domain, assumptions, and validity region with the result. | The check does not define unit conversion or comparison policy. |
| Safety and assurance practice | Keep technical finding, evidence use, assurance, and decision consequence separate. | A complete record does not make the tested constraint true. |
| Current FPF A.6.4 retargeting | Use the exact proposition in q as A.20's constrained subject only when it is a named internal constraint; keep r, q, any application, and the separate tri-state current-case judgement distinct. | A semantic Bridge is a separate F.9 relation and use claim. |

### A.20:12 - Relations

- `E.18` places independently defined transformation and adjacent values in a selected transformation-flow structure.
- `A.6.1` and `E.20` define operation and mechanism content whose named constraints may be tested.
- `A.6.4` defines the retargeting arrow r, the separate bounded-use assertion q, and the separate current-case judgement. A.20 may test q's exact proposition only when it is a named internal constraint; any operation application remains separate.
- `A.21` consumes exact check results and defines gate-policy consequences without suppressing independent applicable results.
- `E.17`, `G.11`, `C.27`, `A.10`, `B.3`, and `A.15` define publication, refresh, temporal, evidence, assurance, and Work claims.
- `F.9` applies only when an additional semantic correspondence is current.
- `C.2.1` supplies result-episteme identity.

### A.20:End

