## C.16.IR - Determine What an Indication Can Resolve

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative

### C.16.IR:1 - Problem frame

Use this pattern when an available measurement relation leaves open what can be inferred from an indication. A loaded voltmeter reading can fit several source voltages. A saturated sensor can establish that a quantity exceeds one threshold while leaving a higher threshold unresolved. A stored counter remainder can correspond to several event counts.

**First useful move.** Try to construct two cases that fit the same indication and stated conditions but give different answers to the receiving question. If an ideal instrument reports the square of a signed displacement, a reading of 9 square metres fits both +3 and -3 metres. It determines the magnitude but leaves the direction unresolved. Restricting displacement to nonnegative values would resolve that difference only when the subject conditions support the restriction.

The Method determines what the indication resolves under the available relation, domain and uncertainty assumptions. Its result can be a value, a compatible range, a settled comparison, two remaining alternatives or an incompatibility among the premises. C.16 supplies the subject, Characteristic, Scale, performed measurement and result meanings. C.16.MR constructs a missing measurement relation.

The examples require elementary equations, inequalities and integer remainders. More difficult relations can require subject-specific inverse methods, probability models or validated numerical computation.

Apply an already suitable conversion or analysis function directly when it supplies the answer with adequate uncertainty. Use this construction when ambiguity, omitted influences or the meaning of a computed range can change that answer.

### C.16.IR:2 - Problem

A measurement relation can predict the indication without allowing the sought value to be uniquely recovered. Several quantities may jointly affect the same reading; a conversion can erase distinctions through clipping, averaging, squaring or wrapping. An algorithm can return one solution while other compatible solutions remain.

The receiving question also matters. An interval may settle an operating threshold even when a point value is unavailable. Conversely, precise arithmetic on one arbitrarily selected solution can hide a decision-changing ambiguity.

The problem is to recover the alternatives allowed by the indication and its conditions, then determine which differences matter to the intended use. This requires keeping the observation, model assumptions, computed approximations and supported conclusion distinguishable throughout the calculation.

### C.16.IR:3 - Forces

| Force | Tension |
| --- | --- |
| Convenient answer and remaining alternatives | One number is easy to use; several values may fit the same reading. |
| Target and influential quantities | Full parameter recovery can be costly; the sought quantity may already be determined. |
| Exact data and uncertain data | An ideal relation may have one solution while the actual error range permits many. |
| Complete computation and sufficient conclusion | Describing the entire compatible set can be expensive; a bound can answer the working question. |
| Additional observation and changed subject | A second reading can distinguish alternatives only under the relations that connect the two measurement situations. |
| Calculation and model revision | Inconsistent premises require diagnosis; forcing a numerical answer can conceal the conflict. |

### C.16.IR:4 - Solution

Construct the cases compatible with the indication and relevant conditions. Obtain the sought values represented by those cases, retaining the distinction between feasible examples and bounds that contain all solutions. Use that result to answer the current question.

#### C.16.IR:4.1 - Fix the sought distinction and available relation

State the quantity or property being sought, its subject and conditions, and the question that depends on it. Distinguish the state before measurement, the state during interaction and the reported indication when they differ. For the voltmeter case in :5.1, the target is open-circuit source voltage, while the reading is the voltage with the instrument connected.

Recover the relation used to interpret the indication, including the domain of each unknown, relevant calibration, influences and error assumptions. Keep a known input as known and an unknown influence as a variable. Derive a missing contribution with C.16.MR before treating it as part of the available relation.

A domain restriction needs its subject meaning. Positive length, a known rotation range and a passive resistance bound can exclude mathematical solutions when those conditions hold. An inconvenient branch is a reason to inspect the model, not a reason to drop that branch.

State whether the receiving question needs a point value, an interval, a threshold decision or a comparison. This selects which remaining differences matter.

#### C.16.IR:4.2 - Construct the jointly compatible cases

Substitute the obtained indication into the relation. Combine that condition with the admitted domains and available information about influences. For repeated or multiple readings, state which subject values and parameters are shared and which may change between them.

With bounded error, include the unknown error in its stated range. If a relation gives an ideal indication f(x,z), x is the sought value, z contains influential unknowns and r is the reported reading, a common model is:

`r = f(x,z) + e, with e in the supplied error range.`

Use that equation only when additive error describes the actual indication convention. An error before clipping, an error after clipping and a missed event can require different relations.

A compact mathematical expression for the compatible sought values is:

`S(r) = {x : there exist admitted z and e for which r = f(x,z) + e}.`

An implicit relation can be used in the same way without converting it to a single-valued function. Retain dependencies among unknowns: independently combining their separate ranges can introduce cases excluded by their joint relation.

A probability model supplies a different additional contribution. Values inside a bounded-error range have no assigned likelihood merely from membership in that range. A confidence interval or posterior distribution requires its corresponding statistical method and assumptions.

#### C.16.IR:4.3 - Obtain values or bounds without losing alternatives

Choose the lightest adequate computation. Solve a small equation, eliminate an influential variable, enumerate a finite domain, or obtain a bound. A numerical formulation can use C.29.2 when its construction is nontrivial.

During elimination, preserve the conditions of each operation. Dividing by an unknown expression can discard its zero case. Squaring an equation can admit additional roots. Test the retained cases in the original relation and domains. Finding one root establishes a possible case; uniqueness requires an argument covering the admitted domain or a sufficient justified restriction.

For several unknowns, obtain the sought value from each compatible joint case. The other unknowns can remain unresolved when every compatible case gives the same sought answer. Section :5.1 gives a source voltage determined while its internal resistance remains unknown.

When a complete solution is costly, distinguish two useful computational results:

- A **feasible example** is one case that satisfies the original relations and conditions. Two such cases can establish a consequential ambiguity.
- An **outer bound** contains every compatible sought value but can also contain values that no case realizes. If the whole bound satisfies an inequality, that inequality holds for every compatible value. A bound spanning both sides of a threshold alone does not establish that both outcomes are possible.

For example, let an ideal indication obey r = x² with x ≥ 0, and let r = 9. A computation that has retained only the outer bound 0 ≤ x ≤ 4 leaves values on both sides of the threshold x = 2. The original relation, however, admits only x = 3. Thus x > 2 is resolved, and no feasible witness with x ≤ 2 exists. The coarse bound left the calculation unfinished; it did not establish ambiguity in the indication.

Use a validated enclosure method when the conclusion depends on retaining every solution through numerical calculation. Ordinary sampling can discover a counterexample but can miss another branch. When computation has not established existence, completeness or a needed bound, retain that limitation in the answer instead of interpreting solver termination as the missing result.

#### C.16.IR:4.4 - Test what is resolved for the receiving question

For a point-value question, test whether all compatible cases agree on that value. For a threshold or other condition, test whether it holds throughout the compatible set or a sufficient outer bound. Establish that the premises admit a case before using such a bound as the interpretation of a measurement; substitution of an available feasible case may suffice.

If the question remains unresolved, construct two compatible cases with different answers. Check both against all readings, shared parameters and domain conditions. These witnesses identify what an additional relation or observation would have to distinguish.

Separate a proved empty compatible set from a search that has not found a case. An empty set shows that the combined readings, model and conditions are inconsistent. Locate a consequential conflict; the cause may be a recording error, a changed subject, an unsuitable error bound or an inadequate measurement relation. A failed search instead limits the computational result.

A point result under ideal data can broaden when input uncertainty is restored. Recompute the relevant range when a reading, calibration coefficient or domain changes. Numerical sensitivity and branch ambiguity can require different remedies.

#### C.16.IR:4.5 - Choose the useful return

Return the value, range or comparison with the conditions that support it. Stop when it is sufficient for the intended use. A lower bound can be more useful than an unnecessarily precise estimate.

For an unresolved decision, use the differing cases to choose a potentially useful next contribution: an available second reading, a different operating range, a better bound, a changed instrument or a narrower conclusion. Examine what that contribution could distinguish before obtaining it. In :5.3, another counter using a different modulus distinguishes alternatives that repeating the same remainder preserves.

Use C.11.DUA when the value and effort of reducing the ambiguity need comparison. It can be reasonable to act with the remaining uncertainty or leave the question unresolved. B.5.MPC.R coordinates a needed revision across the physical, mathematical and computational contributions.

### C.16.IR:5 - Archetypal Grounding

#### C.16.IR:5.1 - One source, two loads and an unidentified influence

Suppose a source has unknown open-circuit voltage E ≥ 0 and finite internal resistance Rs ≥ 0. An ideal meter of known input resistance Rm > 0 reads the connected voltage:

`V = E*Rm/(Rs + Rm).`

The relation and passive-source assumptions are supplied. The question is whether E is at most 8 V.

A reading of 5 V with Rm = 1 MΩ gives:

`E = 5 V*(1 + Rs/(1 MΩ)).`

Rs = 0 and E = 5 V fit the reading; Rs = 1 MΩ and E = 10 V also fit it. The threshold question is unresolved. The reading does establish E ≥ 5 V under the stated domain.

Now a meter with Rm = 3 MΩ reads 7.5 V. Assume E and Rs stayed unchanged between the readings and both meters obey the given model. The two equations share those two unknowns. Express E from each equation and equate:

`V1*(1 + Rs/R1) = V2*(1 + Rs/R2).`

Hence, when the denominator is nonzero,

`Rs = (V2 - V1)/(V1/R1 - V2/R2).`

The supplied readings give Rs = 1 MΩ and E = 10 V. Substitution recovers both 5 V and 7.5 V. The answer to E ≤ 8 V is now no.

The shared-source condition does work here. If E changes between readings, replacing it with E1 and E2 leaves the original inference unsupported. A second number is useful through the relation connecting its measurement to the first.

For two zero readings under the same model, E = 0 follows while Rs can be any finite nonnegative value. A zero denominator in the derived formula is a reason to return to the original equations. Full recovery of Rs is unnecessary for this voltage result.

#### C.16.IR:5.2 - A saturated reading can settle one threshold

An ideal instrument reports r = min(y,10), where y ≥ 0 is a quantity expressed on the instrument's stated scale. For r = 10, every y ≥ 10 is compatible.

If the working question is y ≥ 8, the reading settles it. If the question is y ≥ 12, y = 10 and y = 13 are compatible cases with different answers. Reporting y = 10 as the determined quantity would lose that distinction.

Now suppose the reported reading follows `r = min(y,10) + e`, with -0.2 ≤ e ≤ 0.2. This error is applied after the clipping operation. For the same r = 10, the ideal clipped value can lie from 9.8 to 10. The compatible set becomes y ≥ 9.8: y = 9.8 with e = 0.2 is a feasible endpoint, and every y ≥ 10 fits with e = 0.

The reading still settles y ≥ 8. It no longer settles y ≥ 10, since y = 9.8 and y = 10 are both compatible. This is a bound-based result; no probability was assigned to the error. Repeated readings do not narrow that bound merely by being repeated. A narrower result needs a relation that supports the reduction, such as a justified stochastic error model or a smaller error bound.

#### C.16.IR:5.3 - Combining counter remainders

A device starts at zero, increments once per event and stores N modulo 16. No reset or missed event occurs. A supplied count bound is 0 ≤ N < 100. The stored value 5 permits:

`N in {5,21,37,53,69,85}.`

These six values come from `N = 5 + 16*k` with an integer k in the range allowed by the bound. They all satisfy the original operation. The reading settles N < 90, while N < 30 remains unresolved; 21 and 37 are witnesses.

Suppose a second counter starts at the same event boundary, sees every same event, and stores N modulo 17. It reports 4. Test the six candidates against this second relation: only N = 21 remains. The physical event correspondence and initialization make the mathematical intersection appropriate.

If the supplied bound is relaxed to N < 300, both 21 and 293 satisfy the two remainders. The earlier uniqueness conclusion therefore depended on the bound. If the counters cover different event intervals, use separate counts and recover the relation between them before combining their readings.

### C.16.IR:6 - Bias-Annotation

Under the five Principle-Taxonomy lenses of E.3 (Gov, Arch, Epist, Prag and Did), this pattern is scoped to interpreting indications through available relations. The cases use supplied, simple relations. Real inverse problems may be high-dimensional, unstable or sensitive to uncertain model structure. Establishing complete bounds can then require considerably more work than exhibiting one ambiguity.

The set-based branch treats uncertainty as admitted possibilities. Statistical inference and decisions under risk can distinguish those possibilities by likelihood, loss or preference when their own assumptions are supplied. Use the result form appropriate to the question; a demand for uniqueness can make an already useful measurement appear inadequate.

### C.16.IR:7 - Conformance Checklist

- **CC-C16.IR-1 - Receiving distinction.** The target property, subject conditions and required conclusion are stated.
- **CC-C16.IR-2 - Joint premises.** Readings, domains, influences, errors and shared-value assumptions enter the available relation with their meanings preserved.
- **CC-C16.IR-3 - Inverse operations.** Elimination or numerical calculation retains the needed branches and tests candidates in the original relations.
- **CC-C16.IR-4 - Result strength.** Feasible cases, outer bounds, proved emptiness and incomplete computation have distinct interpretations.
- **CC-C16.IR-5 - Supported answer.** Uniqueness or a threshold answer follows across the compatible cases; claimed ambiguity has feasible witnesses with different answers.
- **CC-C16.IR-6 - Uncertainty meaning.** A range, confidence statement or probability distribution keeps the assumptions that justify that form.
- **CC-C16.IR-7 - Useful return.** Work stops with a sufficient result or identifies a contribution capable of changing the unresolved answer.

### C.16.IR:8 - Common Anti-Patterns and How to Avoid Them

| Failure in the worked situation | Consequence | Repair |
| --- | --- | --- |
| Use the displayed number as the sought value | Loading or clipping changes the answer. | Interpret the reading through the available relation and target conditions. |
| Select one root and discard the rest | A sign or other consequential branch disappears. | Test the admitted domain and retain every branch relevant to the conclusion. |
| Demand every parameter's unique value | Work continues after the requested quantity is determined. | Test agreement on the sought value, as in the zero-voltage case. |
| Treat a wide computational enclosure as realized ambiguity | Approximation slack is mistaken for attainable alternatives. | Construct feasible witnesses or report the unresolved computation. |
| Combine readings without their shared-subject condition | An apparent extra equation relates different unknowns. | Recover the time, initialization and subject correspondence before intersection. |
| Convert repeated readings into a narrower bound by counting them | A common bias or unrestricted bounded error survives repetition. | Supply the error relation that justifies the proposed reduction. |

### C.16.IR:9 - Consequences

The practitioner can identify what information the measurement actually supplies for a question. A useful bound can end inquiry; an explicit pair of alternatives can direct a better observation or a model repair.

The cost grows with the relation and the conclusion claimed. A single ambiguity witness can be cheap, while excluding every alternative may require a global argument or specialized computation. The Method retains that difference so the amount of work follows the receiving use.

### C.16.IR:10 - Architectural Rationale

Indication production and interpretation have different directions. A procedure can map many subject conditions to the same output. Interpreting that output therefore asks which of those conditions remain possible and which distinctions the receiving question needs.

This explains the separate contribution from C.16.MR. A measurement relation can already be available while its inverse use is unresolved. Constructing compatible cases makes that relation usable without requiring a new model or an estimate for every parameter.

The same reasoning connects physical measurement, mathematical inverse relations and computational information loss. Their subject premises differ. A source's loading law, an instrument's clipping order and a counter's event semantics supply the cases to which the common reasoning applies.

### C.16.IR:11 - SoTA-Echoing

**Practice question.** What does an indication determine when an available relation has influential unknowns, lost distinctions or consequential input uncertainty?

**Selected answer and serious alternative.** Adopt a question-relative compatible-set calculation or sufficient bound when those features can change the answer. The serious alternative is direct use of a suitable calibrated analysis function, or a justified estimate with its uncertainty. Keep that cheaper route when it settles the same question. In :5.1, using one loaded reading as E returns the wrong target; two elementary compatible cases expose the loss at comparable effort. In :5.2, a threshold result needs less work than a point estimate. The selected method trades a convenient single output for the alternatives needed by the decision.

**Measurement-model contribution.** [JCGM GUM-6:2020, §11.4 and §§13.5–13.6](https://www.bipm.org/documents/20126/2071204/JCGM_GUM_6_2020.pdf) distinguishes calibration and analysis functions, permits directly estimating an analysis function, and retains implicit measurement models under a stated local-uniqueness assumption. **Adapt** that direction distinction in :4.1–4.3. When uniqueness is unavailable, :4.4 returns the alternatives needed by the question. The document supplies quantitative measurement-model practice; it does not establish that every inverse problem has a unique solution.

**Computational contribution.** [IBEX 2.9, Contractors, Introduction and Forward-Backward](https://ibex-team.github.io/ibex-lib/contractor.html) describes filtering a domain while preserving its feasible solutions. **Adopt** that preservation requirement for the bounded numerical branch in :4.3. A surviving outer domain can still contain infeasible points, which motivates the feasible-witness distinction. Symbolic elimination and finite enumeration suffice for the worked cases.

The common question, target projection, sufficient-result return and diverse cases are conceptual synthesis. Specialized inverse, statistical and decision methods contribute where the question needs their further operations or guarantees. Reopen the comparison when a cheaper analysis settles the same use with equivalent uncertainty, when a proposed bound misses a compatible branch, or when a changed measurement relation invalidates the result.

### C.16.IR:12 - Relations

- **C.16** supplies measurement subject, Characteristic, Scale, model, actual work, uncertainty and obtained-result meanings.
- **C.16.MR** constructs a missing or unsuitable measurement relation.
- **C.29.1** examines the correspondence and preserved distinctions when mathematical representation itself is in question.
- **C.29.2** constructs a needed computational formulation and its accuracy conditions.
- **A.3.3.PI** retains information for a future question under a dynamics account; the present Method interprets an available indication.
- **B.5.MPC.R** coordinates a needed revision across physical, mathematical and computational contributions.
- **C.11.DUA** compares the useful effect and effort of obtaining additional information.

### C.16.IR:End
