## PSDA.9 - Test Robustness and Sensitivity of Decision Alternatives and Their Comparison

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** **robust regions, reversals, and information priorities** for one decision-support comparison: the conditions under which a claim holds, changes, or cannot be established, and the questions that could usefully change it.

### PSDA.9:1 - Problem frame

**Use this when** a favored alternative depends on a forecast, weight, model, or threshold that might change, or when a precise ranking hides plausible reversals. Also use it when the recipient asks whether further information would improve the decision rather than merely improve the estimate.

Start with one claim: what exactly should remain true, under which changes? Vary the decision-bearing conditions within a justified range and inspect where the claim survives or fails. The gain is a bounded statement of stability and a useful next question.

The governed object is that robustness account. **Sensitivity** describes how a result changes with inputs, assumptions, or models. **Robustness** says whether a declared performance, admissibility, or comparison condition continues to hold across specified variation. A sensitive magnitude can leave the preferred set unchanged; an insensitive average can hide a decisive threshold crossing. Section 4.3.1 supplies a small paired-response test when the response at a central input can conceal such a difference.

**Do not use this pattern** when a current robustness result already covers the exact comparison and changes now in question. Use direct model validation for whether a model is adequate in the first place, and the authorized choice owner for the actual decision or probe. Stability inside a model does not validate the model or authorize action.

### PSDA.9:2 - Problem

A one-point ranking can hide a narrow region of support. Small changes in a value trade-off can reverse it; a common-cause failure can defeat every alternative; a different model can change which conditions are even represented.

Sensitivity work can also miss the decision. A tornado chart may rank output variance rather than choice relevance. One-factor-at-a-time tests can miss interactions. Running thousands of similar scenarios can create an appearance of broad coverage, and their frequency can be mistaken for probability. More calculations do not by themselves support a stronger robustness claim.

### PSDA.9:3 - Forces

| Force | Tension |
| --- | --- |
| Coverage and effort | Joint or structural changes can matter, while unrestricted scenario expansion consumes the available time. |
| Stability and truth | Repeated agreement supports only the tested model and region, not the omitted world. |
| Values and evidence | Better information can resolve a fact, while a disputed trade-off needs a value judgement or legitimate collective decision. |
| Flexibility and commitment | Staging can preserve options, while monitoring, lead time, reversibility, and later authority may be unavailable. |
| Information and action | A probe can change a decision, but it also costs time, resources, exposure, and foregone opportunity. |

### PSDA.9:4 - Solution

Declare the claim and variation space, challenge it with the least costly tests that cover the live failure mechanisms, and return supported regions, reversals, and bounded information questions. Keep the actual later decision separate.

#### PSDA.9:4.1 - State what is being tested

Recover the exact alternatives, consequence comparison, value basis, subject, configuration, horizon, and receiving use. Use `PSDA.8`'s comparison and evidence only where they match those conditions. A qualified direct comparison can supply the same input.

Specify the test. It might ask whether one alternative remains no worse under a declared rule, whether every retained alternative meets a service threshold, whether a protected condition is ever violated, or whether the recommendation must remain conditional. Different tests can produce different answers.

Name the robustness criterion before interpreting results. Satisfactory performance across tested conditions, worst-case loss, regret relative to the best available alternative in each condition, and stability across compatible value models answer different questions. Do not change the criterion after seeing which candidate it favors. If the criterion or admissible trade-off is unresolved, return that question rather than presenting a universal winner.

#### PSDA.9:4.2 - Bound the changes by evidence and the decision

Identify the uncertainties or judgement changes that could affect this test: input values, future conditions, model structures, consequence definitions, preference models, evidence qualification, candidate membership, or horizon. State why the selected variations are relevant and what they omit.

Ranges and scenarios need a basis. Distinguish observed bounds, elicited judgements, scientifically or operationally plausible cases, and deliberately extreme stress tests. A stress-test failure can reveal vulnerability without establishing the failure's probability.

Preserve dependencies and feasibility. Joint variations should describe possible or explicitly hypothetical conditions, not arbitrary combinations of incompatible endpoints. Changing a binding legal, safety, consent, or security condition is not an ordinary parameter perturbation. Its meaning, applicability and current force require their own competent result. If the question is whether its protection warrants its measure, threshold or burden, use the bounded `C.11.DUA` §4.3 appraisal through `PSDA.6` §4.4. Return the substantive recommendation and actual amendment authority/window separately; until a revision applies, test present alternatives under the binding condition.

If a needed variation cannot be bounded, retain that coverage gap. “Across all plausible futures” is stronger than “across the three stated futures” and needs stronger support.

#### PSDA.9:4.3 - Test locally, then expand where the failure can hide

Begin with a cheap discriminating test: a boundary value, an alternative value judgement, an omitted condition, or a direct challenge to one decisive assumption. Recompute the same comparison for all affected alternatives under that changed basis.

Use joint or global variation when interactions, nonlinearities, common causes, thresholds, or structural alternatives can change the result. A one-at-a-time test is insufficient for a claim about those combinations. Use the direct modeling and analysis Method to choose suitable tests, sampling, or proofs.

Keep empirical variability, model uncertainty, and value disagreement distinguishable. If a model change alters the meaning or comparability of an output, repair the comparison before treating the difference as another numerical sample.

A computational result is limited by the tested region and procedure. An analytical inequality may establish a whole region under its assumptions; a finite sample usually establishes only sampled behavior unless a further guarantee is justified. State that difference.

##### PSDA.9:4.3.1 - Compare a central response with two equally displaced inputs

Use this small test when the response to a varying input may make a central estimate misleading. It needs a response account suitable for the stated comparison, not an assumed probability distribution.

1. Name the input and the response it affects. Fix the arrangement, affected subject, time window, other relevant conditions, response unit and preferred direction. Choose a central input `x` and displacement `h > 0` so that `x-h`, `x` and `x+h` lie within the account's admissible domain. Equal input differences and averaging the responses must be meaningful on their respective scales; numerical labels alone do not suffice.
2. Obtain the three comparable response values from the qualified model or suitable observations. For response `r`, calculate the endpoint mean and its difference from the central response: `D = (r(x-h) + r(x+h))/2 - r(x)`. The equal weights define this constructed test. Calling the mean a real-world expectation requires a separately qualified probability model.
3. Interpret `D` on the declared response coordinate. A positive difference means the endpoint mean exceeds the central response: worse for a loss, better for a benefit whose higher value is preferred. For a target-valued response, use its declared preference rule. Zero means no midpoint gap at these three points; it does not prove linearity or robustness over an interval. Examine each tested response against any independently justified threshold as well.
4. Widen the displacement or test another consequential condition only when it could change the receiving decision and the model's domain permits it. Report the tested values and gaps; do not turn one finite comparison into a regional convexity, derivative or global robustness claim.

If the response account or scale is inadequate, return that specific limit. A clearly conditional calculation or qualitative comparison may remain useful; requesting more observations is a separate worth question, not an automatic next step.

When a harmful response suggests changing exposure, formulate the actual alternative arrangement and compare its whole contribution through `C.11.CRC`. Include the means, carrying burden and displaced work required to maintain a proposed protection. A stated spending limit alone does not enforce a consequence limit. `C.16` governs quantity and scale use; `C.29` governs a needed mathematical-representation correspondence and its transfer limits. The robustness account remains the result here.

#### PSDA.9:4.4 - Map holding regions and reversals


Report which condition holds in each relevant region, where alternatives exchange order, where a threshold is crossed, and where the comparison becomes unsupported. Include boundaries and ties when they can change the return.

Separate a genuine reversal from a different question. A new value rule, candidate, subject, or horizon may define another comparison rather than a parameter change inside the old one. Preserve the original basis so that the reader can see which happened.

Test omissions as well as numbers. A stable two-candidate result can be irrelevant if a material third candidate remains unexamined. A common failure can show that all current alternatives are inadequate. Return that candidate or formulation gap instead of calling the least bad option acceptable.

The result may be a robust retained set, a conditional preference, several non-dominated alternatives, a failure region, an unresolved boundary, or a blocker. No single preferred alternative is required.

#### PSDA.9:4.5 - Connect the remaining uncertainty to information value

Ask what feasible observation, experiment, calculation, or interpretation could move the comparison across a material boundary. Distinguish “this factor changes the output a lot” from “this attainable result could change the decision”.

When the consequence probabilities and preferences support an expected-utility comparison, use MMP.16:4.2–4.5 to construct the value of the actual observation: model the records it can produce, determine the available action after each record, and average those resulting values before the record is known. Include the probe's cost, delay and changed opportunities in the consequences of the compared continuations before applying the utility account. Subtract a cost directly from expected utility only when its additive value on the same scale is justified and has not already been included in those consequences. PSDA.6:4.5.6 supplies a finite utility construction when that preference input is missing. For several compatible probability and utility accounts, carry out the information comparison within each account and retain the supported range or conditional choice; averaging those accounts requires a separate basis. Perfect-information value can be an upper bound under the same available actions and other conditions; it is not the value of an imperfect test. MMP.16 also distinguishes learning from an observation that changes the system. Information values from several sources are not automatically additive.

Where probabilities are not defensible, state the discriminating conditions and what a probe could resolve without inventing expected value. Some uncertainty will remain.

Use `C.11` or the direct decision owner for the actual choice of a next probe over the current options, budget, value, and cost. This pattern supplies information priorities and conditions, not probe authorization or a research WorkPlan. A preference or authority dispute may require an explicit judgement rather than more empirical data.

#### PSDA.9:4.6 - Examine adaptive alternatives without assuming free flexibility

When a staged candidate is live, test what it actually preserves. The later observation must arrive early enough, be interpretable, and leave a feasible response within the remaining resources and authority. Include monitoring cost, lead time, temporary exposure, transition burdens, and irreversible loss of options where material.

A policy-failure condition is not automatically an action trigger. The future decision arrangement must determine what observation warrants reconsideration and who can act. If those premises are missing, return the candidate's specific adaptive-capability gap.

Do not favor a pilot solely because uncertainty is high. A probe can be unsafe, too slow, uninformative, or unable to change the relevant commitment. Conversely, a bounded information result can be more useful than a premature direction recommendation when its supported value justifies the delay.

#### PSDA.9:4.7 - Return a bounded robustness account

Return the tested claim and comparison basis; the variation region and omissions; the method and evidence limits; supported holding regions and reversal conditions; unresolved comparisons or candidate gaps; information priorities and feasibility limits; and the observation that reopens the result.

`PSDA.14` may use this evidence for the same configuration and horizon to compose a recommendation. Evidence does not entail that recommendation or the later receiving decision. An unavailable, stale, or incompatible robustness result can be replaced only by a qualified direct result or an explicit gap.

Recognition starts with a plausible reversal. Consequential assurance also requires qualified model and source use, correct analysis, adequate challenge coverage, and the direct domain's protection and independence requirements. Robustness to uncertain parameters does not cure an invalid model or missing safety result.

### PSDA.9:5 - Archetypal Grounding

#### PSDA.9:5.1 - An explicit reversal boundary for the pump comparison

Use the illustrative F and M slice from `PSDA.8`: F costs 8 incremental budget units and loses 2 service hours with normal access or 3 with road loss; M costs 5 and loses 1 or 9 hours. N remains the baseline and S still has an unqualified whole-arrangement result. The following calculation tests only F against M; it does not close the wider candidate comparison.

For an illustrative analytical question, suppose a declared value model minimizes expected service-loss hours plus `lambda` times incremental budget units. Here `lambda` is an explicitly elicited value conversion, in service-hour-equivalent value per budget unit; it is not a measurement conversion or an unspoken public preference. Let `p` be the road-loss probability if a qualified probability model supports one.

Under those assumptions:

- F's value loss is `2 + p + 8*lambda`.
- M's value loss is `1 + 8*p + 5*lambda`.
- F has lower value loss precisely when `7*p > 1 + 3*lambda`; equality is a tie.

For `lambda = 0.5`, the reversal is at `p = 5/14`, approximately 0.357. At `p = 0.2`, F and M give 6.2 and 5.1 respectively, so M is better under this model. At `p = 0.6`, they give 6.6 and 8.3, so F is better. These are invented sensitivity settings, not a forecast.

The source comparison supplied no probability. Therefore the valid return is the conditional boundary, not a claim that either setting is likely. If a probability model cannot be qualified, retain the scenario comparison instead of assigning equal chances.

A different declared test asks whether modeled service loss is at most 4 hours in both stated access conditions. F satisfies that illustrative test; M fails it under road loss. This is a different robustness criterion, not a hidden replacement for the value model. The four-hour cut is an example, not a domain standard. F's result covers only those two modeled conditions.

The account returns the reversal boundary, the limited threshold result, the unresolved probability and value premises, and S's candidate gap. Reachable assistance, wider property consequences, and protected conditions still require their direct results. None of the calculations authorizes a pump investment.

##### PSDA.9:5.1.1 - A separate constructed delay-response question

Keep the preceding probability and value-reversal question separate. For this new illustration, fix a thirty-day service window and one access interruption. A stipulated model supplies the service-loss hours for F and M at three access delays; lower service loss is preferred. Each arrangement and all other modeled conditions stay fixed while delay varies.

| Access delay in days | F: service-loss hours | M: service-loss hours |
| --- | ---: | ---: |
| 0 | 2 | 1 |
| 1 | 2.5 | 3 |
| 2 | 3 | 9 |

With `x = 1` day and `h = 1` day, M's central response is 3 hours, its endpoint mean is `(1 + 9)/2 = 5` hours, and `D = 2` hours. F's central response and endpoint mean are both 2.5 hours, so its `D = 0`. F has no midpoint gap at these three points; this does not establish a linear response between them.

Under the separately declared four-hour service-loss criterion, M's two-day response of 9 hours fails. F satisfies that criterion at the three stated points only. Neither endpoint mean is an expected real loss without a probability basis, and a central response below four hours does not settle the endpoint test.

The useful return is the finite response difference, M's failure condition and the remaining model and coverage limits. F's additional investment and the feasibility of any alternative access protection still need their whole-configuration comparison. If the stipulated model lacks support for real use, retain the calculation as conditional or illustrative; do not report an established pump-performance result. No additional observations or investment are authorized by it.

#### PSDA.9:5.2 - What would change a development recommendation?


In the illustrative ninety-day organization case, I is internal development with covered service duties and H is a mixed human–tool arrangement. The earlier supplier bounds, 12–18 and 8–20 service-loss hours, do not establish a robust ordering.

Suppose a qualified joint operating model now supplies two admissible conditions within those bounds:

| Condition | I: service-loss hours | H: service-loss hours | Supported comparison on this coordinate |
| --- | --- | --- | --- |
| Required handoff coverage is present. | 14 | 10 | H has less service loss. |
| The specified handoff coverage is absent. | 16 | 20 | I has less service loss. |

The robustness result locates a reversal in the whole arrangement's coverage condition. It does not attribute the difference solely to human learning or model quality. The useful next question is the feasibility and persistence of that exact coverage under the proposed allocation, not a generic demand for a higher AI benchmark or another course test.

If that result can be obtained within the decision window, the adviser can return it as an information priority with its cost and limits. If not, the recommendation remains conditional or retains both directions. A service model for another team or model version does not close this holder-specific boundary.

#### PSDA.9:5.3 - Cheap non-use and honest stop

A current analysis already proves the same service comparison throughout the relevant parameter interval, and the only proposed new computation repeats interior points without challenging another assumption. Reuse the result. If the untested issue is instead a missing causal or safety premise, stop the robustness calculation and obtain that direct result; more parameter samples will not supply it.

### PSDA.9:6 - Bias-Annotation

**Scope:** robustness and information questions for bounded decision support. **Lenses:** **Epist** distinguishes model stability from truth; **Prag** tests decision relevance; **Arch** exposes interactions and omitted alternatives; **Gov** preserves protected conditions and future authority; **Did** makes reversals and limits readable.

Winner-protection bias selects narrow ranges or convenient criteria. Scenario-count bias mistakes volume for coverage. Variance bias selects a probe that cannot change the decision. Flexibility bias assumes cost-free adaptation. Counter these by declaring the claim, criterion, region, and real response capability before interpreting the result.

### PSDA.9:7 - Conformance Checklist

- [ ] The exact comparison, subject, configuration, horizon, and robustness claim are stated.
- [ ] The robustness criterion is explicit and not chosen after seeing the preferred winner.
- [ ] Variation ranges, scenarios, dependencies, and exclusions have a recoverable basis.
- [ ] Binding conditions are not silently relaxed as parameters. A disputed requirement's merits return remains separate from its present force and from the robustness result.
- [ ] Tests address relevant interactions, structural differences, and omitted alternatives.
- [ ] Sampled behavior, analytical region claims, and unsupported extrapolation are distinguished.
- [ ] A paired-response test states its admissible inputs, comparable response scale, construction weights, preferred direction and exact finite result; no midpoint gap or constructed mean is overread as global robustness or an actual expectation.
- [ ] Holding regions, ties, reversals, failures, and gaps are reported at their actual scope.
- [ ] Information priorities concern attainable decision-changing results and include cost or feasibility limits.
- [ ] Adaptive claims account for observation, lead time, response feasibility, and later authority.
- [ ] The return supplies evidence for recommendation, not truth, authorization, Work, or effectiveness.

### PSDA.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The winner is robust” after a few small perturbations. | State the claim, variation region, method, and untested failure mechanisms. |
| Count successful scenarios as a success probability. | Supply a qualified probability measure or report conditional coverage only. |
| Change one input at a time despite common-cause failure. | Test the relevant joint conditions under a justified dependence model. |
| Treat the largest output variance as the best information target. | Ask whether attainable information can change a decision or eligibility. |
| Recommend a pilot whenever evidence is thin. | Establish information value, safety, timing, reversibility, and response feasibility. |
| Change the robustness criterion to preserve the preferred option. | Show the different questions and return the criterion disagreement. |

### PSDA.9:9 - Consequences

The recipient learns not only what currently compares favorably but where the conclusion can fail. A retained set or conditional recommendation can be more useful than a fragile winner. The cost is targeted recomparison and explicit coverage limits; stop when further work cannot change the declared return or when a different missing premise governs the next action.

### PSDA.9:10 - Rationale

A decision-support result is strengthened by exposing its reversal conditions, not by defending one point estimate. Separating uncertainty, values, model structure, and response capability prevents robustness from becoming a general assurance label. Decision-linked information priorities keep remaining uncertainty useful without making inquiry endless.

### PSDA.9:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can a comparison remain useful when future conditions or models are unsettled? | Stress-test declared performance and comparison claims across justified conditions; examine feasible adaptation where it matters. | Optimize one forecast or call an unspecified staged policy robust. | **Adapt:** :4.1–:4.4 and :4.6 return bounded holding and failure regions. Extra scenario and response analysis is accepted when a single forecast or assumed flexibility can conceal failure. | Lempert et al.'s [2024 DMDU analysis](https://doi.org/10.3389/fclim.2024.1380054) supplies the current robust-decision line; the [2019 DAPP chapter](https://doi.org/10.1007/978-3-030-05252-2_4) supplies pathway, timing, and failure-condition distinctions. Their applied domains do not supply universal thresholds, scenario probabilities, or local authority. | Reopen when an omitted condition, implementation lead time, or response constraint defeats the stated region. |
| Which sensitivity result should guide further inquiry? | Link local and joint sensitivity to the decision boundary and the value of attainable information. | Use output variance or a one-factor chart as a universal research priority. | **Adapt:** :4.3–:4.5 distinguish magnitude sensitivity, reversal, and probe value. More computation is justified only when the added question can change the bounded return; actual probe choice remains separate. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) is the synthesis candidate for sensitivity and information acquisition. Its formal approaches need their own model assumptions; `C.11` retains the local choice and probe-worthiness result. | Reopen when the feasible probe, decision window, dependency model, or costs change. |
| What can a central-input response conceal? | Compare the central response with a symmetric endpoint mean and test consequential thresholds separately. | Rely on the central response alone or infer a whole-region property from three points. | **Adapt:** :4.3.1 and :5.1.1 make a finite nonlinear-response check usable without inventing probabilities. | Taleb and West's [2023 finite-difference and convexity account, §III-C and Appendix B](https://arxiv.org/html/2209.14631v2), supplies the distinction between a finite comparison and stronger smoothness, regional or probability claims. Its clinical models do not validate a decision-support response model. | Reopen when the response model, scale, supported domain, subject or decision threshold changes. |
| What if the value model, rather than the forecast, is incomplete? | Test relations across the models compatible with the expressed preferences. | Treat one fitted weight vector as uniquely known. | **Adapt:** :4.1–:4.4 retain value-dependent reversals instead of calling preference uncertainty factual noise. The deliberate trade-off is a possibly larger retained set. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) supplies robust ordinal regression as a best-known-line candidate for this question, not a requirement to use one algorithm or to collapse participants' values. | Reopen when elicitation or a legitimately governed value decision changes the compatible model set. |

### PSDA.9:12 - Relations

- `PSDA.8` may supply the consequence comparison and its evidence for the same configuration and horizon. Evidence enables this test but does not establish its result.
- `PSDA.14` may consume robust regions, reversals, and information priorities as evidence for its recommendation. This neither entails the recommendation nor transfers the later choice authority.
- `A.10` governs bounded evidence reliance; direct domain and modeling practices govern the validity of claims, models, ranges, and tests. Changed actual source uses receive their direct revalidation rather than a blanket robustness assertion.
- `C.16` governs quantities, scales and response comparability; `C.29` governs a needed mathematical representation and its correspondence limits. Neither supplies domain validation merely through the calculation.
- `C.11.CRC` compares a proposed finite change to the arrangement, including the feasibility and burden of maintaining a protection. A sensitivity result does not itself change that arrangement.
- `C.11` governs an actual local choice and the worth of another probe. Information priority, probe selection, WorkPlan, performed inquiry, and observed effect remain distinct results.
- Candidate formation, value elicitation, model repair, and follow-up remain their own questions when the test exposes a gap there. Missing or incompatible inputs require a qualified direct result or an exact stop.

### PSDA.9:End
