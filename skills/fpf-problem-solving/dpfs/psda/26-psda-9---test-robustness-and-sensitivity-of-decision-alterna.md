## PSDA.9 - Test Robustness and Sensitivity of Decision Alternatives and Their Comparison

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** the conditions under which a specified claim holds, reverses or remains open. Identify useful further information when it could change the finding or a decision that relies on it.

### PSDA.9:1 - Problem frame

**Use this when** you need to know how a forecast, weight, model or threshold affects a finding about alternatives. Test whether a ranking reverses, whether a service still meets its limit, or whether obtaining further information would improve the evidence or decision enough to justify its cost.

State the claim and which changes it must withstand. Vary the relevant conditions over a justified range. Report where the claim holds, fails or remains open. If further information could matter, identify the question it could answer.

**Sensitivity** describes how a result changes with inputs, assumptions, or models. **Robustness** says whether a declared performance, admissibility, or comparison condition continues to hold across specified variation. A sensitive magnitude can leave the preferred set unchanged; an insensitive average can hide a decisive threshold crossing. Section 4.3.1 supplies a small paired-response test when the response at a central input can conceal such a difference.

Reuse a current robustness result that covers the claim and the changes in question. Validate the underlying model where the conclusion needs that assurance. The authorized holder chooses or authorizes a decision or probe when one is called for.

### PSDA.9:2 - Problem

A one-point ranking can hide a narrow region of support. Small changes in a value trade-off can reverse it; a common-cause failure can defeat every alternative; a different model can change which conditions are even represented.

Sensitivity work can also miss the decision. A tornado chart may rank output variance rather than choice relevance. One-factor-at-a-time tests can miss interactions. Running thousands of similar scenarios can create an appearance of broad coverage, and their frequency can be mistaken for probability. Check whether the additional calculations cover a relevant untested condition.

### PSDA.9:3 - Forces

| Force | Tension |
| --- | --- |
| Coverage and effort | Joint or structural changes can matter, while unrestricted scenario expansion consumes the available time. |
| Stability and truth | Agreement across tests supports stability within their model and coverage. Extending that finding requires grounds for the larger region. |
| Values and evidence | Better information can resolve a fact, while a disputed trade-off needs a value judgement or legitimate collective decision. |
| Flexibility and commitment | Staging can preserve options, while monitoring, lead time, reversibility, and later authority may be unavailable. |
| Information and action | A probe can improve the finding or change a decision, but it also costs time, resources, exposure, and foregone opportunity. |

### PSDA.9:4 - Solution

State the claim, the variation to be covered and the evidence already available. Choose the least costly adequate tests or proofs for the remaining uncertainty. Report where the claim holds or fails and which information could resolve any consequential gap. A later choice belongs to its authorized holder.

#### PSDA.9:4.1 - State what is being tested

Identify the claim, subject, configuration, horizon and intended use. For a comparison, recover the alternatives, consequences and applicable rule or value basis. Compatible evidence from `PSDA.8` or a direct comparison can supply the input.

Specify the test. It might ask whether one alternative remains no worse under a declared rule, whether every retained alternative meets a service threshold, whether a protected condition is ever violated, or whether the recommendation must remain conditional. Different tests can produce different answers.

Name the robustness criterion before interpreting results. Satisfactory performance across tested conditions, worst-case loss, regret relative to the best available alternative in each condition, and stability across compatible value models answer different questions. Do not change the criterion after seeing which candidate it favors. If the criterion or allowable trade-off remains open, report any conditional results the supported criteria yield and what remains undecided.

#### PSDA.9:4.2 - Bound the changes by evidence and the decision

Identify the uncertainties or judgement changes that could affect this test: input values, future conditions, model structures, consequence definitions, preference models, evidence qualification, candidate membership, or horizon. State why the selected variations are relevant and what they omit.

Ranges and scenarios need a basis. Distinguish observed bounds, elicited judgements, scientifically or operationally plausible cases, and deliberately extreme stress tests. A stress-test failure can reveal vulnerability without establishing the failure's probability.

Preserve dependencies and feasibility. Joint variations should describe possible or explicitly hypothetical conditions, not arbitrary combinations of incompatible endpoints. Changing a binding legal, safety, consent, or security condition is not an ordinary parameter perturbation. Use applicable evidence of its meaning, scope and force, or identify the missing ruling where a decision is required. If the question is whether its protection warrants its measure, threshold or burden, use the bounded `C.11.DUA` §4.3 appraisal through `PSDA.6` §4.4. Return the substantive recommendation and actual amendment authority/window separately; until a revision applies, test present alternatives under the binding condition.

If a needed variation cannot be bounded, identify the claim that the gap limits. “Across all plausible futures” is stronger than “across the three stated futures” and needs stronger support.

#### PSDA.9:4.3 - Test locally, then expand where the failure can hide

Use an existing adequate test or begin with a low-cost discriminating check, such as a boundary value, an alternative value judgement, an omitted condition, or a direct challenge to one decisive assumption. If the basis is changed, recompute the comparison for the affected alternatives or use a result that already covers the change.

Use joint or global variation when interactions, nonlinearities, common causes, thresholds, or structural alternatives can change the result. A one-at-a-time test is insufficient for a claim about those combinations. Choose tests, sampling or proofs appropriate to the model and the claim about the combinations.

Keep empirical variability, model uncertainty, and value disagreement distinguishable. If a model change alters the meaning or comparability of an output, establish comparability before combining numerical outputs. Otherwise report their different meanings and keep the values separate.

A computational result is limited by the tested region and procedure. An analytical inequality may establish a whole region under its assumptions; a finite sample usually establishes only sampled behavior unless a further guarantee is justified. State that difference.

##### PSDA.9:4.3.1 - Compare a central response with two equally displaced inputs

Use this small test when the response to a varying input may make a central estimate misleading. It needs a response account suitable for the stated comparison, not an assumed probability distribution.

1. Name the input and the response it affects. Fix the arrangement, affected subject, time window, other relevant conditions, response unit and preferred direction. Choose a central input `x` and displacement `h > 0` so that `x-h`, `x` and `x+h` lie within the account's admissible domain. Equal input differences and averaging the responses must be meaningful on their respective scales; numerical labels alone do not suffice.
2. Obtain the three comparable response values from the qualified model or suitable observations. For response `r`, calculate the endpoint mean and its difference from the central response: `D = (r(x-h) + r(x+h))/2 - r(x)`. The equal weights define this constructed test. Calling the mean a real-world expectation requires a separately qualified probability model.
3. Interpret `D` on the declared response coordinate. A positive difference means the endpoint mean exceeds the central response: worse for a loss, better for a benefit whose higher value is preferred. For a target-valued response, use its declared preference rule. Zero means no midpoint gap at these three points; it does not prove linearity or robustness over an interval. Examine each tested response against any independently justified threshold as well.
4. Widen the displacement or test another consequential condition when the model supports the altered inputs and the further result could change a needed finding or decision enough to justify the work. Report the tested values and gaps; do not turn one finite comparison into a regional convexity, derivative or global robustness claim.

If the response model or scale is inadequate, identify the resulting limit. Give a conditional calculation or qualitative comparison where its assumptions support one. Assess the value of further observations if they are being considered.

When a change of exposure is under consideration, specify the proposed arrangement and compare its whole contribution through `C.11.CRC`. Include the means, carrying burden and displaced work required to maintain a proposed protection. A stated spending limit alone does not enforce a consequence limit. `C.16` governs quantity and scale use; `C.29` governs a needed mathematical-representation correspondence and its transfer limits. The robustness account remains the result here.

#### PSDA.9:4.4 - Map holding regions and reversals


Report which condition holds in each relevant region, where alternatives exchange order, where a threshold is crossed, and where the comparison becomes unsupported. Include boundaries and ties when they can change the return.

Separate a genuine reversal from a different question. A new value rule, candidate, subject, or horizon may define another comparison rather than a parameter change inside the old one. Preserve the original basis so that the reader can see which happened.

Test omissions as well as numbers. A stable two-candidate result can be irrelevant if a material third candidate remains unexamined. A common failure can show that all current alternatives are inadequate. Return that candidate or formulation gap instead of calling the least bad option acceptable.

The result may be a robust retained set, a conditional preference, several non-dominated alternatives, a failure region, an unresolved boundary, or a blocker.

#### PSDA.9:4.5 - Connect the remaining uncertainty to information value

Identify an attainable observation, calculation or interpretation that could change the requested finding, its grounds, eligibility or the action available. Compare its expected contribution with the cost and delay. A large change in a numerical output may leave the relevant conclusion unchanged.

For an expected-utility comparison, use MMP.16:4.2–4.5 to model the records the proposed observation could produce. For each record, find the highest conditional expected utility among the actions then available. Weight these values by the probabilities of the records, and compare their sum with the best expected utility available without the observation. For a record with a continuous distribution, use the corresponding expectation. Include collection cost, delay, any change to the system and lost opportunities in the consequences of the compared options. Subtract a cost directly from expected utility only if it is additive on that scale and has not already been counted. Use PSDA.6:4.5.6 if a required utility account must be constructed. If several probability and utility accounts are compatible, report the comparisons within each account or the supported range. Averaging accounts needs separate grounds. Perfect information can bound the benefit of information under the same actions and conditions. Several observations may supply overlapping information.

If the probabilities lack support, report the result under the specified conditions and what a feasible observation could resolve. Calculate an expected value on stipulated probabilities only for an explicitly conditional question.

When selecting a further probe, use `C.11` or the applicable decision procedure to compare the attainable options, budget, benefits and costs. Identify the authority required for execution. A dispute about a value or mandate may need a judgement by its holder.

#### PSDA.9:4.6 - Examine adaptive alternatives without assuming free flexibility

When a staged candidate is live, establish which later actions it keeps feasible. The later observation must arrive early enough, be interpretable, and leave a feasible response within the remaining resources and authority. Include monitoring cost, lead time, temporary exposure, transition burdens, and irreversible loss of options where material.

Check the applicable rule for responding to a policy failure. It may trigger a specified protection or require reconsideration by a decision holder. If a necessary route, response or authority is missing, identify that limitation of the staged option.

Before recommending a pilot, check its safety, timing, information value and which response would remain feasible. Report an attainable information result when its value to the question warrants the delay.

#### PSDA.9:4.7 - Return a bounded robustness account

Return the tested claim and criterion, variation and omissions, methods and evidence limits. Report the holding regions, failures, ties or reversals the evidence establishes. Identify any consequential unresolved comparison, missing candidate or useful further information, its feasibility, and the condition under which the result would need reconsideration.

A practitioner preparing a recommendation with `PSDA.14` can use compatible evidence for the same configuration and horizon. If a necessary result is missing, stale or incompatible, use a qualified direct result or state the gap. The decision requires its own authority.

Recognize the need when a relevant variation could alter a finding, a threshold result or its grounds. Consequential assurance also requires qualified model and source use, correct analysis, adequate challenge coverage, and the direct domain's protection and independence requirements. Robustness to uncertain parameters does not cure an invalid model or missing safety result.

### PSDA.9:5 - Archetypal Grounding

#### PSDA.9:5.1 - An explicit reversal boundary for the pump comparison

Use the illustrative F and M slice from `PSDA.8`: F costs 8 incremental budget units and loses 2 service hours with normal access or 3 with road loss; M costs 5 and loses 1 or 9 hours. N remains the baseline and S still has an unqualified whole-arrangement result. The following calculation tests only F against M; it does not close the wider candidate comparison.

For an illustrative analytical question, suppose a declared value model minimizes expected service-loss hours plus `lambda` times incremental budget units. For this illustration suppose `lambda` has been elicited as a trade-off in service-hour-equivalent value per budget unit. The calculation can equally be made conditional on an explicitly stipulated trade-off. Attributing it to the public requires evidence about the public’s values. Let `p` be the road-loss probability if a qualified probability model supports one.

Under those assumptions:

- F's value loss is `2 + p + 8*lambda`.
- M's value loss is `1 + 8*p + 5*lambda`.
- F has lower value loss precisely when `7*p > 1 + 3*lambda`; equality is a tie.

For `lambda = 0.5`, the reversal is at `p = 5/14`, approximately 0.357. At `p = 0.2`, F and M give 6.2 and 5.1 respectively, so M is better under this model. At `p = 0.6`, they give 6.6 and 8.3, so F is better. These are invented sensitivity settings, not a forecast.

The source comparison supplies no road-loss probability. The calculation therefore establishes the conditional boundary. Without a probability basis, report the service loss in each access condition.

A different declared test asks whether modeled service loss is at most 4 hours in both stated access conditions. F satisfies that illustrative test; M fails it under road loss. The four-hour cut is a second criterion stipulated for this illustration. F's result covers only those two modeled conditions.

Return the reversal boundary and the threshold result for F and M under their stipulated conditions. Identify unresolved real-world probability and value premises, the gap for S and any unassessed consequences or protections needed for a wider comparison. The authorized board makes the investment decision.

##### PSDA.9:5.1.1 - A separate constructed delay-response question

For a different question, fix a thirty-day service window and one access interruption. A stipulated model supplies the service-loss hours for F and M at three access delays; lower service loss is preferred. Each arrangement and all other modeled conditions stay fixed while delay varies.

| Access delay in days | F: service-loss hours | M: service-loss hours |
| --- | ---: | ---: |
| 0 | 2 | 1 |
| 1 | 2.5 | 3 |
| 2 | 3 | 9 |

With `x = 1` day and `h = 1` day, M's central response is 3 hours, its endpoint mean is `(1 + 9)/2 = 5` hours, and `D = 2` hours. F's central response and endpoint mean are both 2.5 hours, so its `D = 0`. F has no midpoint gap at the tested points. A claim about values between them requires further grounds.

Under the separately declared four-hour service-loss criterion, M's two-day response of 9 hours fails. F satisfies that criterion at the three stated points only. Neither endpoint mean is an expected real loss without a probability basis, and a central response below four hours does not settle the endpoint test.

Report the finite response difference, the failure at the two-day delay and the model and coverage limits. A question about investing in F or changing access protection requires evidence about the whole arrangement and the relevant authority. Where the model is stipulated, keep the answer conditional on it.

#### PSDA.9:5.2 - What would change a development recommendation?


In the illustrative ninety-day organization case, I is internal development with covered service duties and H is a mixed human–tool arrangement. The suppliers’ separate bounds of 12–18 and 8–20 service-loss hours leave the ordering open.

Suppose a qualified joint operating model now supplies two admissible conditions within those bounds:

| Condition | I: service-loss hours | H: service-loss hours | Supported comparison on this coordinate |
| --- | --- | --- | --- |
| Required handoff coverage is present. | 14 | 10 | H has less service loss. |
| The specified handoff coverage is absent. | 16 | 20 | I has less service loss. |

In this joint model the relative service loss reverses when the handoff coverage changes. The comparison concerns whole arrangements. A choice that relies on this coverage needs evidence of its feasibility and persistence under the proposed allocation. Use applicable evidence or retain the conditional comparison. Attributing the difference to human learning or model quality would require other evidence.

Where evidence about the coverage could be obtained in time and would justify the effort, identify it as an information priority with its cost and limits. Otherwise retain the conditional comparison. A different team or model version needs a basis for transfer to this arrangement.

#### PSDA.9:5.3 - Cheap non-use and honest stop

A current analysis already proves the same service comparison throughout the relevant parameter interval, and the only proposed new computation repeats interior points without challenging another assumption. Reuse the result. If the untested issue is instead a missing causal or safety premise, use an applicable direct result or identify the missing premise and what it prevents; more parameter samples will not supply it.

### PSDA.9:6 - Bias-Annotation

**Scope:** robustness and information questions for bounded decision support. **Lenses:** **Epist** distinguishes model stability from truth; **Prag** tests decision relevance; **Arch** exposes interactions and omitted alternatives; **Gov** preserves protected conditions and future authority; **Did** makes reversals and limits readable.

Winner-protection bias selects narrow ranges or convenient criteria. Scenario-count bias mistakes volume for coverage. Variance bias favors a probe that changes the output but contributes little to the requested finding or choice. Flexibility bias assumes cost-free adaptation. Counter these by declaring the claim, criterion, region, and real response capability before interpreting the result.

### PSDA.9:7 - Conformance Checklist

- [ ] The claim, criterion, subject, configuration and horizon are stated, including the alternatives where they are compared.
- [ ] The robustness criterion is explicit and not chosen after seeing the preferred winner.
- [ ] Variation ranges, scenarios, dependencies, and exclusions have a recoverable basis.
- [ ] Binding conditions are not silently relaxed as parameters. A disputed requirement's merits return remains separate from its present force and from the robustness result.
- [ ] Tests address relevant interactions, structural differences, and omitted alternatives.
- [ ] Sampled behavior, analytical region claims, and unsupported extrapolation are distinguished.
- [ ] A paired-response test states its admissible inputs, comparable response scale, construction weights, preferred direction and exact finite result; no midpoint gap or constructed mean is overread as global robustness or an actual expectation.
- [ ] Holding regions, ties, reversals, failures, and gaps are reported for the conditions the evidence covers.
- [ ] Information priorities concern attainable results that can change a needed finding, its evidence or a decision and include cost or feasibility limits.
- [ ] Adaptive claims account for observation, lead time, response feasibility, and later authority.
- [ ] The conclusion states what the robustness evidence establishes and any further grounds needed for a recommendation, authorized action or claim of effect.

### PSDA.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The winner is robust” after a few small perturbations. | State the claim, variation region, method, and untested failure mechanisms. |
| Count successful scenarios as a success probability. | Supply a qualified probability measure or report conditional coverage only. |
| Change one input at a time despite common-cause failure. | Test the relevant joint conditions under a justified dependence model. |
| Treat the largest output variance as the best information target. | Check whether attainable information could improve the requested finding, establish a condition of eligibility or change the decision. |
| Recommend a pilot whenever evidence is thin. | Establish information value, safety, timing, reversibility, and response feasibility. |
| Change the robustness criterion to preserve the preferred option. | Show the different questions and return the criterion disagreement. |

### PSDA.9:9 - Consequences

The recipient can see the conditions supporting a comparison and where it fails. Recomputing selected cases costs time. Stop when further work would add too little to the requested result or when a different missing premise limits it.

### PSDA.9:10 - Rationale

Stating when the conclusion holds or reverses makes its scope inspectable. Distinguishing the uncertainty, values, model and capacity to respond lets the recipient judge whether a further inquiry could improve the finding or decision.

### PSDA.9:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can a comparison remain useful when future conditions or models are unsettled? | Stress-test declared performance and comparison claims across justified conditions; examine feasible adaptation where it matters. | Optimize one forecast or call an unspecified staged policy robust. | **Adapt:** :4.1–:4.4 and :4.6 return bounded holding and failure regions. Extra scenario and response analysis is accepted when a single forecast or assumed flexibility can conceal failure. | Lempert et al.'s [2024 DMDU analysis](https://doi.org/10.3389/fclim.2024.1380054) supplies the current robust-decision line; the [2019 DAPP chapter](https://doi.org/10.1007/978-3-030-05252-2_4) supplies pathway, timing, and failure-condition distinctions. Their applied domains do not supply universal thresholds, scenario probabilities, or local authority. | Reopen when an omitted condition, implementation lead time, or response constraint defeats the stated region. |
| Which sensitivity result should guide further inquiry? | Link local and joint sensitivity to the decision boundary and the value of attainable information. | Use output variance or a one-factor chart as a universal research priority. | **Adapt:** :4.3–:4.5 distinguish magnitude sensitivity, reversal, and probe value. More computation is justified only when the added question can change the bounded return; selecting a probe requires its own decision. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) is the synthesis candidate for sensitivity and information acquisition. Its formal approaches need their own model assumptions; `C.11` retains the local choice and probe-worthiness result. | Reopen when the feasible probe, decision window, dependency model, or costs change. |
| What can a central-input response conceal? | Compare the central response with a symmetric endpoint mean and test consequential thresholds separately. | Rely on the central response alone or infer a whole-region property from three points. | **Adapt:** :4.3.1 and :5.1.1 make a finite nonlinear-response check usable without inventing probabilities. | Taleb and West's [2023 finite-difference and convexity account, §III-C and Appendix B](https://arxiv.org/html/2209.14631v2), supplies the distinction between a finite comparison and stronger smoothness, regional or probability claims. Its clinical models do not validate a decision-support response model. | Reopen when the response model, scale, supported domain, subject or decision threshold changes. |
| What if the value model, rather than the forecast, is incomplete? | Test relations across the models compatible with the expressed preferences. | Treat one fitted weight vector as uniquely known. | **Adapt:** :4.1–:4.4 retain value-dependent reversals instead of calling preference uncertainty factual noise. The deliberate trade-off is a possibly larger retained set. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) supplies robust ordinal regression as a best-known-line candidate for this question, not a requirement to use one algorithm or to collapse participants' values. | Reopen when elicitation or a legitimately governed value decision changes the compatible model set. |

### PSDA.9:12 - Relations

- `PSDA.8` may supply the consequence comparison and its evidence for the same configuration and horizon. Evidence enables this test but does not establish its result.
- `PSDA.14` may consume robust regions, reversals, and information priorities as evidence for its recommendation. This neither entails the recommendation nor transfers the later choice authority.
- `A.10` governs bounded evidence reliance; direct domain and modeling practices govern the validity of claims, models, ranges, and tests. Revalidate a source-dependent conclusion when the changed use affects its grounds.
- `C.16` governs quantities, scales and response comparability; `C.29` governs a needed mathematical representation and its correspondence limits. Neither supplies domain validation merely through the calculation.
- `C.11.CRC` compares a proposed finite change to the arrangement, including the feasibility and burden of maintaining a protection. A sensitivity result does not itself change that arrangement.
- `C.11` governs a local choice and the worth of another probe. Information priority, probe selection, WorkPlan, performed inquiry, and observed effect remain distinct results.
- Candidate formation, value elicitation, model repair, and follow-up remain their own questions when the test exposes a gap there. For a missing or incompatible input, use a qualified direct result or report precisely what remains open.

### PSDA.9:End
