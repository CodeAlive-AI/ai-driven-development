## C.11.CRC - Configuration-Relative Contribution Comparison

> **Tech name:** `ConfigurationRelativeContributionComparison`
>
> **Plain name:** compare what this finite change adds to the current configuration
>
> **Type:** C-pattern
>
> **Placement:** a narrow companion used before `C.11` when its comparison basis is not yet available

### C.11.CRC:0 - Use This When

Use this pattern when a bounded addition, replacement, removal, intervention, experiment, information/computation acquisition, capability-development element, project, or component is being justified by “what it adds,” but the current configuration, interactions, resources, horizon, uncertainty, and receiving decision are not yet part of the comparison.

**First useful result.** Return one ordinary `C.2.1` episteme that compares a realizable finite changed configuration with the current configuration under a declared basis. State the result coordinates and resource coordinates, interactions, uncertainty, option effects, unsupported overreads, and the `C.11` decision that can consume the claim. The comparison does not choose the option.

**Cheap exit.** If a current `A.19`/`C.11` account already states the same finite baseline, change, horizon, result and resource coordinates, interactions, uncertainty, and reopen condition, use that account directly.

**Not this pattern when.** Do not use it for a source-only comparison with no realizable configuration change; for a purely causal question under `C.28`; for a mathematical-lens question already answered by `C.29` and a field Method; for an archive/front relation under `C.18`; or as a substitute for field-specific finance, optimization, operations, engineering, experimental-design, or capability-development calculation.

### C.11.CRC:1 - Problem Frame

Candidates are often described by an isolated score, average benefit, frequency, local gradient, shadow price, or expected information gain. The receiving decision concerns something else: whether a finite change is worthwhile *from this current configuration*, over this horizon, for these affected Systems, under these resource and authority constraints.

The same candidate can contribute differently when prerequisites, complements, substitutes, bottlenecks, thresholds, congestion, implementation capability, uncertainty, reversibility, and future options differ. A good isolated characteristic can therefore coexist with a dominated configuration change, and a weak-looking local result can preserve valuable options or reveal a critical blocker.

### C.11.CRC:2 - Problem

Without an explicit configuration-relative comparison, practitioners make at least six transfers:

- a finite change is approximated by a derivative outside its valid region;
- a shadow price for one active constraint is multiplied into the value of an asset that changes several constraints;
- a candidate is compared with an empty system instead of the actual current configuration;
- several result and resource coordinates are hidden inside one scalar;
- interaction and common-cause overlap are counted as independent contribution; and
- information, option value, or reversibility is treated as realized benefit.

`A.19` provides comparison mechanisms and characteristic spaces, `C.29` governs mathematical lenses, and `C.11` makes the choice. The remaining recurring practitioner action is to construct the finite comparison claim that those patterns can consume.

### C.11.CRC:3 - Forces

| Force | Tension |
| --- | --- |
| Local simplicity vs finite reality | Derivatives and local prices can be useful while the realizable change is indivisible, thresholded, or interacting. |
| Multiple results vs decision closure | Several benefits, harms, and resources must stay visible without preventing a bounded choice. |
| Current value vs future options | Waiting, learning, staging, reversibility, and path dependence can change later possibilities. |
| Reuse vs domain authority | FPF can supply the comparison grammar; domain Methods must calculate quantities and judge evidence. |
| Recognition vs assurance | A well-formed comparison can still lack trustworthy inputs, implementation capability, or required assurance. |

### C.11.CRC:4 - Solution

Construct the smallest finite counterfactual comparison that can change one named decision.

1. **Name the receiving decision.** State the deciding System, current `DecisionSubject`, decision deadline, current `OptionSet` or the option-set question that this comparison will inform, and which result could change the decision.
2. **Freeze the current configuration.** Name the actual or currently relied-on configuration `S0`, system boundary, affected Systems, holder or beneficiary, relevant environment, and what is held fixed only for this comparison. A historical, empty, or ideal configuration is not the default baseline.
3. **Name the finite change.** State the addition, replacement, removal, intervention, or probe `Δ`, the realizable candidate configuration `S1`, admissibility conditions, implementation capability, transition Work, reversibility, and excluded variants.
4. **Fix horizon and scenarios.** State the interval, relevant states or scenarios, timing assumptions, and any decision or evidence window. Do not combine results from incompatible horizons without an explicit mapping.
5. **Declare result coordinates.** Name the result vector whose coordinates can change the decision and the protected coordinates that may not be silently scalarized. Include affected-System consequences and distributional differences when current.
6. **Declare resource coordinates.** Name the action, transition, information-acquisition, computation, attention, capital, time, material, energy, authority, and other resources that the field case actually consumes. Keep costs of evaluating and realizing the change distinct.
7. **Recover constraints and interactions.** State active and potentially activated constraints, complements, substitutes, thresholds, congestion, downstream effects, common causes, overlaps, and double-counting risks.
8. **Recover option effects.** State whether the finite change opens, closes, delays, preserves, or makes irreversible later options. Keep information value and option value as decision inputs, not already realized operating results.
9. **Qualify evidence and uncertainty.** Identify source claims, currentness, uncertainty, sensitivity/robustness results, transfer limits, rival explanations, and `A.10` reliance dispositions where an evidence-bearing claim is used.
10. **Write the comparison claim.** State what `S1` contributes relative to `S0` only under the declared coordinates, horizon, scenarios, constraints, interactions, and evidence. Use dominated, non-dominated, beneficial, harmful, or indeterminate wording only when the stated relation supports it; do not force one scalar winner.
11. **Route mathematical near-misses.** Apply the distinction in `C.11.CRC:4.2`; the finite comparison may consume a derivative, sensitivity, shadow price, variational, or inference result without becoming identical to it.
12. **Return to `C.11`.** `C.11` combines this claim with preferences, belief state, outcome model, probe worth, and other premises and emits one `ChoiceResult`. State the smallest configuration, horizon, evidence, resource, constraint, or option-set change that reopens this comparison.

#### C.11.CRC:4.1 - Lightweight comparison form

`ConfigurationRelativeContributionComparison@Context` is a form name for one ordinary comparison episteme. It is not a root U-kind, universal delta value, selector result, or decision.

```text
receivingDecisionRef:
currentConfigurationRef: S0
candidateFiniteChangeRef: Δ
candidateConfigurationRef: S1
systemBoundaryAndAffectedSystems:
horizonAndScenarios:
resultCoordinateRefs:
protectedCoordinateRefs:
resourceCoordinateRefs:
constraintsAndInteractions:
transitionAndImplementationBasis:
futureOptionEffects:
evidenceAndUncertaintyRefs:
comparisonClaim:
unsupportedOverreads:
reopenCondition:
nextGoverningPattern: C.11
```

Omit a field only when it cannot change this comparison and that omission is apparent from the bounded case. A polished record cannot compensate for a missing current configuration or decision.

#### C.11.CRC:4.2 - Mathematical and model-routing distinction

| Expression encountered | Exact question | Required boundary |
| --- | --- | --- |
| Finite difference or counterfactual configuration comparison | What changes between realizable `S0` and `S1` over the declared horizon? | Default here for indivisible, non-smooth, thresholded, path-dependent, or strongly interacting changes. Do not infer additivity. |
| Derivative or gradient | What is the local rate of change with respect to a coordinate under smoothness and small-change assumptions? | It approximates the finite contribution only when the validity region and remainder are adequate for `Δ`. |
| Sensitivity | How does a result vary with a parameter, assumption, input, model, or scenario? | It supplies robustness or assurance information; it need not describe a realizable configuration change. |
| Shadow price or dual variable | What is the local value of relaxing a formulated active constraint under the primal/dual model? | It depends on formulation, active set, regularity, units, and local region; it is not the contribution of an arbitrary asset or intervention. |
| Functional variation / calculus of variations | How does a functional change when the varied object is a function, path, trajectory, field, control, or shape in a declared admissible variation space? | Name the functional, admissible variations, constraints, boundary conditions, stationarity/extremum claim, sufficiency, and validation. An Euler–Lagrange equation is not a generic contribution claim or proof that a physical System optimizes. |
| Variational inference | Which member of an approximation family best approximates a target probability distribution under a declared divergence or bound? | The result is an approximate distribution and uncertainty account, not an extremal physical trajectory, capability acquisition, or general marginal value. |
| Evolutionary variation | How are retained variants generated and selected in an evolutionary or cultural process? | The shared word *variation* does not identify the mathematical object or Method above; route to `C.18`, `C.36`, or the field practice. |

This is why calculus of variations matters without becoming the default interpretation of marginality. When the candidate is a whole trajectory, field, function, control, or shape, pointwise finite-coordinate reasoning can miss the coupled admissible deformation. `C.29` governs the mapping from the world or domain model to that mathematical object, what structure is preserved or lost, and when the lens must stop. Specialist practice governs derivation, discretization, solver choice, optimality and sufficiency checks, and validation.

#### C.11.CRC:4.3 - Recognition and assurance split

**Recognition.** A user can recognize a conforming comparison when `S0`, finite `Δ`, `S1`, boundary, horizon, result and resource coordinates, interactions, uncertainty, and receiving decision are visible.

**Assurance.** Trust in the numbers and relations remains separate. Field evidence must support the baseline and candidate behavior; implementation capability and transition Work must be credible; causal claims use `C.28`; source reliance uses `A.10`; material assurance uses `B.3`; authority and permission use their direct patterns. This pattern creates none of those results.

### C.11.CRC:5 - Worked Slices

#### C.11.CRC:5.1 - Flood-pump modernization

The current station configuration `FPS7-C19` supports bounded discharge use. A candidate bearing-temperature sensor is not compared with “no pump” or by its isolated diagnostic accuracy. The finite comparison uses `FPS7-C19` as `S0`; sensor, placement, cabling, controller, maintenance access, calibration, and operating procedure changes as `Δ`; and the installed candidate as `S1`. Result coordinates include discharge continuity, failure detection, maintenance access, recoverability, and evidence continuity. Resource coordinates include outage time, installation Work, calibration, observation, and maintenance burden. The current result is indeterminate because placement and maintenance evidence are missing; another observed-load window can change the decision. `C.11` therefore remains free to emit `probe again` rather than the comparison silently selecting the sensor.

#### C.11.CRC:5.2 - Capability-development programme

Adding one pattern to a programme is compared with the person's current mastered and externally supported set, not with an empty curriculum. The comparison names target later Work, prerequisite complementarity, time to competent use, support dependence, critical-error detection, transfer and retention evidence, and future option value. A newly produced artifact or recent exercise-score gain can be evidence for a bounded claim, but neither is automatically the candidate element's capability contribution.

#### C.11.CRC:5.3 - Operations constraint intervention

A positive shadow price for one bottleneck supports a local statement about relaxing the formulated active constraint. A finite machine addition also changes labor, maintenance, setup, downstream capacity, energy, resilience, and perhaps the active constraint. The `S0`/`S1` comparison can therefore disagree with shadow-price multiplication without making the shadow price useless.

#### C.11.CRC:5.4 - Capital allocation

A project is compared with the current portfolio and financing/operating configuration. The comparison includes cannibalization, shared resources, risk concentration, financing constraints, irreversibility, staging, information gained before later commitments, and displaced options. NPV, real-options, scenario, and portfolio Methods remain Corporate Finance practice; this pattern supplies only the finite comparison grammar returned to `C.11`.

### C.11.CRC:6 - Bias Annotation

- **Scalar bias:** do not hide protected coordinates or distributional effects inside one score.
- **Smoothness bias:** do not replace a realizable finite change with a derivative outside its validity region.
- **Additivity bias:** inspect complements, substitutes, overlap, thresholds, congestion, and common causes.
- **Empty-baseline bias:** start from the actual current configuration unless another baseline is explicitly the decision subject.
- **Physics-prestige bias:** a variational or thermodynamic form does not establish a physical mechanism or decision authority.
- **Information-as-result bias:** expected information and option value are inputs to choice, not already realized target-System benefit.

### C.11.CRC:7 - Conformance Checklist

1. Is one receiving decision named?
2. Are `S0`, finite `Δ`, and realizable `S1` explicit?
3. Are system boundary, affected Systems, horizon, scenarios, and evidence window compatible?
4. Are result and resource coordinates explicit, with protected coordinates not silently scalarized?
5. Are implementation capability, transition Work, reversibility, and excluded variants recoverable?
6. Are constraints, interactions, overlap, thresholds, congestion, and downstream effects considered where material?
7. Are future option effects distinguished from realized results?
8. Are evidence, uncertainty, sensitivity/robustness, transfer limits, and unsupported overreads visible?
9. Is each derivative, sensitivity, shadow-price, functional-variation, variational-inference, or evolutionary-variation result used only for its exact question?
10. Does the output remain a comparison claim, with `C.11` retaining the `ChoiceResult`?
11. Is the smallest reopen condition stated?

### C.11.CRC:8 - Common Anti-Patterns and Repairs

| Anti-pattern | Repair |
| --- | --- |
| Candidate value is constant across configurations | Name `S0`, interactions, horizon, and affected Systems. |
| Average benefit chooses the next element | Preserve result/resource vectors and return the comparison to `C.11`. |
| Derivative times step equals finite contribution | State smoothness region and remainder or perform the finite comparison. |
| Shadow price equals asset value | Keep the local active-constraint result and model the finite intervention separately. |
| Functional stationarity proves physical optimality | Use `C.29`, physical/domain evidence, sufficiency checks, and validation. |
| Variational inference is calculus of variations or “learning” | Recover the target distribution, approximation family, objective, returned approximation, and diagnostics. |
| More information is already more capability or value | Treat information as a decision input and test the target result separately. |

### C.11.CRC:9 - Consequences and Reopen Condition

**Benefits.** Finite additions, removals, replacements, probes, and investments become comparable without requiring additivity, smoothness, or a universal scalar. Domain calculations can be reused while their validity regions remain visible. The result gives `C.11` a stable comparison input and keeps choice authority there.

**Costs.** Practitioners must name a baseline, vectors, interactions, and uncertainty that an isolated score could hide. Some cases remain indeterminate until field evidence or implementation capability is available.

Reopen this pattern when repeated cases cannot express their finite comparison with this spine; when a current `A.19`/`C.11` composition fully absorbs the same practitioner entry, action, first result, and stop; or when a mathematical branch requires a different transdisciplinary action rather than a field-specific Method.

### C.11.CRC:10 - Rationale

The pattern is narrow because its result is neither a new value ontology nor a decision. The reusable action is to construct a finite configuration-relative claim before local choice. `A.19` remains the comparison-mechanism owner, `C.29` the mathematical-lens owner, and `C.11` the choice owner.

The selected name follows `F.18`. *Marginal contribution decision* conflates finite difference, derivative, economic terminology, and the later decision; *marginal value* encourages one scalar; *sensitivity analysis* names a different question. `Configuration-Relative Contribution Comparison` names the reference configuration and comparison while leaving domain quantities and choice outside.

### C.11.CRC:11 - SoTA Echoing

| Source line | Adopted move | Limit retained here |
| --- | --- | --- |
| Current `C.11`, `A.19`, and `C.29` | Keep choice, comparison mechanisms, and mathematical-lens use with their current owners. | Internal architecture is not evidence for domain quantities. |
| Ortega and Braun, [information-processing costs in decision making](https://arxiv.org/abs/1204.6481), 2013 | Treat information and computation as explicit decision resources. | Statistical-physics form is a model under assumptions, not proof of literal physical free-energy minimization. |
| Blei, Kucukelbir, and McAuliffe, [*Variational Inference: A Review for Statisticians*](https://www.cs.columbia.edu/~blei/papers/BleiKucukelbirMcAuliffe2017.pdf), 2017 | Keep target distribution, approximation family, optimization, speed/scale, and uncertainty trade-offs visible. | Historical field anchor; it does not define calculus-of-variations design or general contribution. |
| MIT OpenCourseWare, [*Matrix Calculus for Machine Learning and Beyond*](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/pages/lecture-notes-and-readings/), 2023 calculus-of-variations material | Treat a function, trajectory, or field as the varied object under admissible variation and boundary structure. | Course material supplies a mathematical distinction, not FPF ontology, physical evidence, or DPF admission. |
| Huan, Jagalur, and Marzouk, [optimal experimental design review](https://arxiv.org/abs/2407.16212), 2024/2026 | Keep design variables, utility, model assumptions, computational cost, robustness, and myopic/non-myopic boundaries explicit. | Specialist experiment design remains outside this finite comparison pattern. |
| Current systems, operations, finance, and human-capability cases named in the receiving DPF programme | Stress-test finite baseline, interactions, constraints, uncertainty, and option effects across unlike fields. | Cross-field recurrence establishes the comparison spine, not transferable formulas, thresholds, or authority. |

Refresh only the affected source-use row when a newer result changes one Solution distinction or shows that a field-independent method can replace it. Older mathematical anchors remain historical where current work has repaired their limits.

### C.11.CRC:12 - Relations

- **Builds on:** `C.2.1`, `A.10`, `A.19`, `C.16`, `C.27`, `C.28`, and `C.29`.
- **Supplies:** one finite comparison claim to `C.11`; it can also supply an input to a field-specific portfolio, programme, intervention, architecture, or experiment decision.
- **Coordinates with:** `C.18` when the candidate changes the possibility space, `C.19` for pool governance, `B.3` for assurance, A.15 for transition Work, and the direct field practice for calculation and validation.
- **Keeps outside:** universal marginal value, a new delta kind, domain formulas and thresholds, causal proof, assurance, permission, selected-set declaration, and `ChoiceResult`.

### C.11.CRC:End

