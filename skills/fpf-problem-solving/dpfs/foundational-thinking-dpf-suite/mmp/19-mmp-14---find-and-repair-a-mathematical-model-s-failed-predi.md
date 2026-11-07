## MMP.14 - Find and Repair a Mathematical Model's Failed Predictions

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.14:1 - Problem frame

Use this pattern when a mathematical model's predictions leave a consequential feature of the available observations unexplained, or when a proposed use makes such a discrepancy worth examining. A model may reproduce an overall average while missing conditional responses, bursts, extremes or the records that a selection rule actually permits.

Start with one needed prediction and a feature whose failure would change its use. For overload, compare relevant tails or sequences, not only the fitted mean. Construct that feature under the model on comparable records. The first result can be a localized discrepancy, a repaired calculation, or a sufficient reason to retain a narrower use.

The principal result is a changed model, the assumption changed, and the consequence that must be recalculated. A supported restriction of use or an unresolved choice between repairs can also be the useful result. A small residual is not a certificate of adequacy; a nonzero residual is not automatically a model failure.

This is model criticism within mathematical modeling. MMP.7 supplies the recording law, MMP.11 the available model family, and MMP.13 inference within a stated model. Here the work constructs and interprets comparisons that can change that model. A physical, biological, economic or other subject method supplies the meaning and admissibility of the proposed repair. Predictive improvement alone identifies neither a causal mechanism nor an intervention effect.

Do not reopen an adequate application merely to run a standard collection of diagnostics. An established calculation, bound or checked prediction may already suffice under unchanged conditions. C.11.DUA selects further checking when its possible outcomes can change the answer, claim or warranted use. New observations, model enlargement and simulation are not routine prerequisites.

### MMP.14:2 - Problem

An optimizer can improve fit without repairing the needed prediction. A model can fail a broad diagnostic while retaining a sufficient narrower answer. Apparent disagreement can also come from comparing latent quantities with selected records, numerical approximation, or ordinary model-permitted variation.

Even a real discrepancy rarely names its cause. Large residuals might reflect a missing predictor, varying noise, dependence, selection or an erroneous observation. Wholesale replacement hides the changed assumption; making every observed feature look ordinary can fit chance patterns.

The working problem is to construct a comparison that can expose the relevant mismatch, trace it to a revisable part of the model, and establish what the revision changes without treating reused data or simulated agreement as new external evidence.

### MMP.14:3 - Forces

| Force | Consequence for the method |
| --- | --- |
| Intended use versus overall fit | The discrepancy must retain distinctions on which the receiving prediction depends. |
| Sensitivity versus ordinary variation | A useful diagnostic can reveal systematic failure without declaring every unusual observation erroneous. |
| Localization versus ambiguity | A pattern of failure narrows repairs but often does not uniquely identify the defective assumption. |
| Adaptation versus evaluation | Data used to choose a repair cannot also supply an untouched assessment of that choice. |
| Flexibility versus retained structure | A repair must preserve needed constraints and account for the additional estimation or regularization it introduces. |
| Assurance versus effort | Use available comparisons first; acquire more evidence only for a consequential unresolved claim. |

### MMP.14:4 - Solution

**Choose a consequential discrepancy → construct comparable predictions → locate the mismatch → change the implicated assumption → recalculate and compare the consequence → return the warranted use.**

#### MMP.14:4.1 - Choose the prediction and the discrepancy together

State the receiving quantity and conditions: a response at specified inputs, a probability of exceeding a limit, a distribution of recorded counts, or a forecast for a given horizon and group. Name the relevant observational unit. A message, a batch of messages and a whole operating period support different comparisons.

Recover the model and its observation law. Retain units, inputs, initial conditions, exposure, recording rules and material dependence. Separate unknown parameters from assumptions such as constant response, independent errors or complete recording.

Choose a discrepancy \(D\) that responds to a failure relevant to this use. For example:

- Conditional bias can be exposed by mean residuals within relevant input ranges, rather than a mean over all inputs.
- A tail count \(D(y)=\sum_i 1\{y_i>u\}\) asks whether the model accounts for excursions beyond the consequential level \(u\).
- A run length or \(D(r)=\sum_{i=2}^n r_i r_{i-1}\), with residuals in their actual order, can expose dependence hidden by a histogram.
- A distribution of recorded categories can reveal that predictions concern unfiltered events while observations concern selected records.

A conditional plot, a few statistics or a direct bound can suffice. Explain which repair would change the feature. A statistic that fitting nearly forces to agree, such as the mean in a fitted constant-mean model, usually contributes little to detecting omitted structure.

The user needs the target, conditional distributions or bounds, and the comparison's construction. Obtain a missing calculation from a mathematically qualified collaborator: for example, a record generator and a discrepancy's reference distribution. A human or AI participant may supply it; recover the subject assumptions and interpretation before using its output.

#### MMP.14:4.2 - Generate the comparison the question requires

Compare quantities with the same meaning. Replicated physical states are not yet rounded, censored or selected records. Carry them through MMP.7's recording law.

For a **posterior predictive comparison**, obtain joint parameter draws from MMP.13 and generate records conditionally:
\[
 \theta^{(s)}\sim\pi_M(\theta\mid y,x),\qquad
 y^{\mathrm{rep},(s)}\sim p_M(y^{\mathrm{rep}}\mid x,\theta^{(s)}).
\]
Here \(M\) names the model and \(x\) the retained input and recording conditions. Compare \(D(y)\) with \(D(y^{\mathrm{rep},(s)})\). If the discrepancy depends on parameters, calculate \(D(y,\theta^{(s)})\) and \(D(y^{\mathrm{rep},(s)},\theta^{(s)})\) at the same draw.

Decide what repeats. New observations for existing groups with their inferred effects differ from new groups with regenerated effects. Retain or regenerate effects according to the questioned prediction. Do not independently redraw an effect that should be common to an entire batch.

A **non-Bayesian comparison** can use a specified parameter value, an exact conditional reference distribution that eliminates a nuisance parameter, or a fitted-model simulation. State which is used. When the reference concerns a statistic of a fitted procedure, reproduce the fitting step on each simulated dataset; a simulation that holds its fitted coefficients fixed generally answers a different question. A parametric bootstrap may approximate a reference distribution, not make its calibration exact.

For a **held-out comparison**, construct the forecast without using the records being predicted to fit, tune or select that forecast. Keep preprocessing inside the corresponding training operation. Choose the withheld unit and allowed information for the receiving prediction: new observations in an existing group, a whole new group, or a future block with a specified horizon. A convenient random split does not by itself establish future or new-group performance. An alternative split needs an argument that its bias and variability suffice for the intended conclusion.

Write a held-out predictive law as \(Q_M(y_H\mid y_T,x)\), where \(T\) is the available training information and \(H\) the withheld portion. Compare the models on the same \(H\), target and scoring convention. Use a joint block prediction when the question depends on within-block dependence. Pointwise scores can still answer a declared marginal prediction question; they do not test all joint behavior.

Exact enumeration or algebra may replace simulation. If a deterministic prediction and an observation each have established error bounds, compare their admissible ranges. Disjoint ranges expose an incompatibility under those bounds; overlapping ranges do not prove the model.

#### MMP.14:4.3 - Interpret the difference at the comparison's actual strength

Inspect where discrepancies occur, not just whether one aggregate score changes. Compare direction, size, input region and persistence with the variations that the reference construction permits.

A posterior predictive tail fraction describes a conditional comparison under the fitted model. It is not generally a frequentist p-value with a uniform null distribution. An exact conditional tail probability, a fitted bootstrap approximation and a held-out loss have different interpretations. None is the probability that the model is false.

Account for the construction's resolution when it can change the result. Zero exceedances in finitely many simulations does not establish a zero tail probability. Approximation error, poor sampling or an inaccurate held-out calculation can create an apparent discrepancy. CMP.8 and CMP.9 supply the relevant numerical error account. Checking recovery on data generated by the model can expose computational faults; success there does not establish the model's correspondence with the subject.

A pattern found after searching many views remains a useful clue, but its nominal tail area is not automatically calibrated for that search. If a repeated-error guarantee matters, account for the selection or use a suitable untouched comparison. Exploratory diagnosis need not claim that guarantee.

A discrepancy can warrant restricted use, examination of one component, or rejection of a prediction. Failure to expose one means only that this check, at this resolution, has not exposed it.

#### MMP.14:4.4 - Change the part that explains the consequential mismatch

First trace the disputed prediction through its calculation and observation meaning. A wrong unit, event label, numerical solution or censoring convention can require correction without changing the underlying subject relation.

Then formulate a small number of plausible revisions. Show the changed mathematical component and why it can affect the discrepancy:

| Located feature | Possible construction to examine |
| --- | --- |
| Residual means vary with an omitted input | Replace \(m_0(x)\) by \(m_0(x)+b\,h(x)\), with a subject-admissible function \(h\); estimate \(b\) and recalculate the relevant conditional response. |
| Dispersion varies by input while the mean remains adequate | Replace constant error scale by a positive function \(s(x)\); compare conditional spread and the receiving tail probability. |
| Residual sequences have dependence absent from the model | Replace independent errors by a specified covariance or a recurrence such as \(e_t=\rho e_{t-1}+\eta_t\); derive the resulting block or horizon prediction. |
| Available records exclude outcomes the prediction includes | Change the recording or selection component using the established inclusion rule; predict the retained records, keeping the latent law separately visible. |

These are candidates, not conclusions from the symptom alone. Do not delete observations or inflate noise until everything passes. Several changes can reproduce the feature; use subject knowledge and existing discriminating observations to choose, retain conditional alternatives, or return the missing distinction.

Use MMP.11 to preserve support, constraints and known relations when extending the family. Use MMP.13 to infer the revised unknowns; MMP.12 supplies a justified restriction when added flexibility makes recovery unstable. Changed priors, constraints or noise laws can change the answer without adding information to the records.

If the remaining difference is worth a new observation, return the distinguishing prediction and feasible-design question to the applicable observation-design and subject methods. A predictive repair does not identify an intervention effect; obtain the required causal assumptions and identification separately when that is the receiving question. A narrower supported use can finish without either continuation.

#### MMP.14:4.5 - Recalculate the consequence and examine the repair

Recalculate the original discrepancy and the receiving quantity under the revision. Adding a term to an equation leaves both questions unfinished. Show what changes and what remains unchanged.

Compare the revised consequence with the previous one on the same relevant basis. Compare another available model or a narrower use when it can change the choice of repair. A simpler model can be preferable when its retained result suffices and the added component contributes only estimation noise or cost. A better average score can coexist with a worse consequential tail or subgroup prediction; inspect that conflict directly.

Distinguish **repair construction** from **assessment of the repaired prediction**. Reproducing the data that motivated the revision shows what the revision accommodates. An untouched set of suitable existing records can assess a forecast fixed before those records are inspected. When repeated tuning consumes that set, it becomes part of development. If the needed performance claim concerns the whole adaptive procedure, its assessment must include that adaptation, for example through a suitable outer split; it is not a test of one retrospectively selected fit.

Fresh observations are not the only useful continuation. Recalculate with available held-out records, derive the affected consequence, retain a conditional result or restrict use. C.11.DUA determines whether resolving the remaining limitation is worth its cost. Do not describe an unperformed comparison as successful.

#### MMP.14:4.6 - Return the model and its changed use

Return the changed relation or distribution, retained assumptions, relevant comparison, and consequence to use or recalculate. Include ambiguity where it affects use. A short explained calculation can suffice.

For a methodological use, return which discrepancy reveals the omitted distinction, how to produce comparable predictions, and which component to reconsider. For an unresolved subject use, identify the missing contribution instead of a generic demand for more data.

Recognition starts with a consequential disagreement. Assurance depends on the claim: algebra establishes a recalculated consequence; a computational check establishes its numerical execution; an appropriate comparison with observations supports the bounded subject use. Reopen when the target, regime, recording law, relevant evidence or consequential error requirement changes.

### MMP.14:5 - Archetypal Grounding

The following are constructed cases. Their arithmetic demonstrates the method; the stated observations are example inputs.

#### MMP.14:5.1 - A correct overall mean conceals failed conditional predictions

Two message routes, A and B, are used under ordinary load. The target is the chance of timely delivery for each known route. In this small example every message has a complete binary record, the deadline is unchanged, and outcomes are assumed independent with a stable probability within each route and load regime.

The supplied records are partitioned before fitting. Only the fitting and diagnostic portions are opened during model construction; the assessment portion remains withheld until the revised forecasts are fixed.

| Portion | A: timely / total | B: timely / total |
| --- | --- | --- |
| Fitting | 8 / 10 | 2 / 10 |
| Diagnostic | 9 / 10 | 1 / 10 |
| Withheld assessment | 8 / 10 | 2 / 10 |

The original model \(M_0\) ignores route: \(Y_i\sim\mathrm{Bernoulli}(p)\). Its maximum-likelihood estimate from the fitting portion is \(\hat p=1/2\). Its expected diagnostic total equals the observed total: 10 timely deliveries out of 20. That agreement does not answer the route-specific question.

Choose \(D=|K_A/10-K_B/10|\), where \(K_A,K_B\) are the timely counts in the diagnostic portion. Observed \(D=0.8\). Under the common-probability model, condition on the observed total \(K_A+K_B=10\). Then
\[
 P(K_A=k\mid K_A+K_B=10,M_0)
   =\frac{\binom{10}{k}\binom{10}{10-k}}{\binom{20}{10}}.
\]
This reference retains the two sample sizes and removes the unknown common \(p\). The exact two-sided tail for \(D\ge0.8\) is
\[
 \frac{2(1+100)}{184756}
 =\frac{101}{92378}\approx0.001093.
\]
It exposes a discrepancy in the common-probability account under its independence and stability assumptions. It does not identify a causal route effect. A shared disturbance confounded with route could demand a different repair.

Suppose the subject account permits route-specific response probabilities. Construct \(M_1\): \(Y_i\mid g_i\sim\mathrm{Bernoulli}(p_{g_i})\). Using the same fitting records gives \(\hat p_A=0.8,\hat p_B=0.2\). The changed component is the relation between the known route and the response probability, not the binary recording rule.

Recalculate the original discrepancy under the fitted \(M_1\), retaining the same total of 10. Conditional replicate counts have weights
\[
 w_k=\binom{10}{k}^{2}16^k,\qquad
 P(K_A=k\mid K_A+K_B=10,\hat M_1)=w_k/\sum_{j=0}^{10}w_j,
\]
where \(16=(0.8/0.2)/(0.2/0.8)\) is the fitted odds ratio. Summing \(k=0,1,9,10\) gives \(P(D\ge0.8)=0.37348\). The revised point model accommodates the diagnostic contrast. This calculation is conditional on its fitted probabilities; it neither calibrates a test of the estimated family nor independently confirms the repair.

Fix these point-probability forecasts and open the assessment portion. The sum of log probabilities of its 20 individual outcomes, using natural logarithms, is
\[
 L_0=20\log(0.5)=-13.86294,\qquad
 L_1=16\log(0.8)+4\log(0.2)=-10.00805.
\]
Thus \(M_1\)'s fixed forecasts gain \(3.85490\) on this portion. This is an observed paired comparison, not a guaranteed future gain or a parameter-uncertainty interval. The diagnostic portion was used to propose the repair; it was not counted as untouched assessment.

For three future independent A messages under the same regime, the point forecast of at least one late delivery changes from \(1-0.5^3=0.875\) to \(1-0.8^3=0.488\). That receiving calculation must change. If uncertainty about the probabilities matters, MMP.13 must propagate it; the point calculation does not already do so.

**Changed condition.** The supplied operating condition now specifies high load. Before any refitting, a supplied high-load batch has 5/10 timely outcomes on each route. The ordinary-load forecasts give
\[
 L_1^{H}=10\log(0.8)+10\log(0.2)=-18.32581,
\]
whereas the common \(0.5\) forecast still gives \(-13.86294\). Carrying over the repaired forecast loses \(4.46287\) on this batch. The earlier assessment concerned ordinary load and does not establish transfer. Keep that use boundary and examine invariance if a high-load forecast is needed. A high-load common-rate fit of \(0.5\) is a possible new model; its fit here is not an untouched assessment. Its three-message late-delivery forecast would again be \(0.875\), conditional on that rate and independence.

For the narrower question of expected timely deliveries with equal numbers of A and B under ordinary load, both fitted models give one half of the total. If only that expectation is needed and its basis suffices, this case does not require adopting the richer model or obtaining new observations. It does not make the two models' conditional or joint predictions equivalent.

#### MMP.14:5.2 - Repair the law of the exported records

A candidate latency model assigns \(X\) uniformly to the integer values 1 through 6. An export contains only values 1, 2 and 3. Comparing these records with unconditional replications of \(X\) suggests too few large values.

The documented export rule, supplied independently of that discrepancy, retains a record only when \(X\le3\). The failed comparison omitted selection. Compose the candidate event law with the actual rule:
\[
 P(R=j\mid\mathrm{retained})
 =\frac{P(X=j)}{P(X\le3)}=\frac13,\quad j=1,2,3.
\]
The predicted mean of exported values is 2, not 3.5. Their probability of exceeding 2 is \(1/3\), not \(2/3\). Construct comparable replications by applying the same filter, or draw directly from this conditional law. Do not reduce the latent model's tail merely to make the unfiltered comparison agree.

If the documented export cutoff changes to 4, the corresponding mean becomes 2.5 and the probability of an exported value exceeding 2 becomes \(1/2\), with no alteration to the candidate uniform latent law. These are recalculated consequences of the changed recording rule, not new empirical confirmation of that law.

Agreement within the retained range does not establish the distribution among unrecorded values. If the target is only the distribution of exported records, that unresolved tail may be irrelevant. If the target needs latent large-latency probabilities, return the missing information or assumption through MMP.12 and C.16.IR; the selection correction has not recovered it.

#### MMP.14:5.3 - A failed numerical prediction need not require a new subject model

A normalized quantity is modeled by \(u'(t)=-u(t)\), \(u(0)=1\). A record at \(t=1\) is \(0.370\), with an established absolute recording error at most \(0.005\). A forward-Euler computation with step \(h=1\) predicts 0.

Before replacing the decay law, compare the numerical result with the model's exact consequence \(u(1)=e^{-1}\approx0.367879\). Euler steps \(h=1/2\) and \(h=1/4\) give \(0.25\) and \(0.316406\); the sequence of approximations exposes a material computational error. The exact value lies in the observed admissible interval \([0.365,0.375]\). Here the repair belongs to CMP.8, while this observation supplies no reason to change the decay relation.

That interval overlap establishes compatibility for this record under the error bound, not the correctness of the decay model at every time. If a relevant observation instead excludes the accurately computed consequence, the subject relation or observation account becomes live again. Numerically precise evaluation and adequate subject prediction remain separate achievements.

### MMP.14:6 - Bias-Annotation

Familiar diagnostics favor failures that are easy to display. Aggregate scores can hide sparse but consequential regimes; selecting the most striking plot can exaggerate ordinary variation. A preferred causal story can make one repair appear uniquely compelled when several produce the same records.

Preserve the intended use, the role of each data portion and the compatible alternatives. Do not transfer support to unrepresented conditions.

### MMP.14:7 - Conformance Checklist

- The questioned prediction and a discrepancy that can change its use are recoverable.
- Observed and predicted quantities share the relevant inputs, recording meaning, unit and dependence conditions.
- The replication, conditioning or withholding construction supports the interpretation actually claimed.
- Computational error and ordinary model-permitted variation have not been silently treated as subject-model failure.
- A proposed repair names the changed mathematical component and its subject basis; unresolved alternatives remain visible where consequential.
- The receiving consequence has been recalculated, and the role of data reused during repair is stated where it limits assessment.
- The result gives a warranted use, restriction or missing contribution, without imposing new evidence acquisition on a sufficient existing answer.

### MMP.14:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Fit the overall mean and infer adequacy for every conditional forecast | Compare the feature on which the receiving use depends. |
| Call every residual an error in the model | Compare with the model's permitted variation and relevant numerical or recording error. |
| Simulate latent states and compare them with selected records | Pass replications through the actual recording law. |
| Treat a predictive tail fraction as the probability that the model is wrong | Retain the reference distribution and its actual probability statement. |
| Tune repeatedly on a “test” set and report an untouched test result | Treat that set as development data; qualify or separately assess the adaptive procedure. |
| Replace an inconvenient observation or inflate noise until a check passes | Examine the observation basis and competing model components; preserve legitimate unusual outcomes. |
| Improve prediction and claim the causal explanation is established | Retain the predictive claim; obtain identification and subject grounds for the causal claim. |
| Require a new experiment after every mismatch | Use C.11.DUA to choose among available repair, narrower use, conditional continuation and worthwhile inquiry. |

### MMP.14:9 - Consequences

The practitioner can replace “the model fits badly” with a calculable failed prediction and an explicit revised assumption. Downstream users can see which consequence changes, which remains sufficient, and which use is unsupported.

Comparable predictions cost work. Adaptive repair consumes assessment information, and extra parameters can weaken estimation. Improving one feature can leave another failure unresolved. Retain the use boundary without demanding exhaustive criticism of every model.

### MMP.14:10 - Architectural Rationale

B.5.TC aligns competing accounts; B.5.RR carries a changed premise into its consequences. Neither alone constructs a conditional discrepancy distribution, a predictive replication or a withholding scheme. Those mathematical operations provide the contribution here.

MMP.13 determines inference under a model. This method examines where that model fails a needed prediction and changes a component before inference is repeated. MMP.7 prevents a change in recording from being mistaken for a change in the subject. MMP.11 supplies admissible replacement relations, while the subject method determines what those relations purport to represent.

The cases separate a missing conditional relation, a missing selection rule and an inaccurate computation.

### MMP.14:11 - SoTA-Echoing

**Working question.** How can a practitioner find the model component that spoils a needed prediction and repair it without confusing better fit, statistical surprise and external confirmation?

**Selected line.** Combine discrepancy-directed predictive criticism with evaluation appropriate to the intended prediction. Use an exact conditional comparison, fitted simulation, posterior replication or held-out prediction according to the claim. No inferential framework wins independently of the question.

- Gelman, Vehtari and McElreath, [*Statistical Workflow*](https://sites.stat.columbia.edu/gelman/research/published/Statistical_Workflow_article.pdf), §§1.7–1.8 and 1.10–1.11. The text used is the author manuscript dated 5 December 2025 for the 2026 article, not the publisher's typeset version. Its operative contributions here are localizing misfit through predictive comparisons, understanding changes through related models, and separating computational calibration from subject adequacy. Adopt those in :4.3–:4.5. Adapt the wider workflow to a consequential local question; fitting increasingly flexible models until no anomaly remains can absorb legitimate rare patterns.
- [Stan User's Guide 2.39, “Posterior and Prior Predictive Checks”](https://mc-stan.org/docs/stan-users-guide/posterior-predictive-checks.html), posterior checks, discrepancy statistics and mixed hierarchical replication. Adopt the explicit replicated-data construction and the choice of what is regenerated in :4.2. Retain the limitation that a posterior predictive tail fraction is not generally a classically calibrated p-value. A statistic largely determined by fitting can miss the omitted structure. The Bayesian construction is one available comparison, not a requirement to replace an exact conditional or sufficient deterministic argument.
- Aki Vehtari, [*Cross-validation FAQ*](https://avehtari.github.io/modelselection/CV-FAQ.html), online version consulted 16 September 2026, §§3, 5 and 7–11. Adopt its separation of the prediction task, partition and loss in :4.2/:4.5, and its treatment of selection-induced bias. The closest task-matching split is a useful starting point, not an unconditional optimum: alternative partitions can trade bias for variance. Held-out performance can compare predictions without identifying the component that needs revision.

**Serious alternatives on the same question.** In :5.1, optimizing and checking the pooled fit costs less and answers the expected-total question. It fails to expose the conditional discrepancy relevant to forecasting an A message. A held-out log-score comparison of the two fixed forecasts supplies useful performance evidence on the supplied assessment portion, but the score alone does not explain what relation to change. The chosen construction adds the route contrast and a conditional reference, then compares the explicit repair on that same predictive question. It costs an additional fitted probability and leaves uncertainty and regime transfer unresolved; it is not superior for a target already supplied by the pooled expectation.

Reopen the choice when the target becomes a new group, a different horizon, a tail or an intervention; when dependence or selection changes; or when the error requirement makes an approximate comparison insufficient. A more elaborate model or checking scheme earns its place through the new question, not through its recency.

### MMP.14:12 - Relations

- **B.5.TC / B.5.RR:** align accounts and revise dependent reasoning; this method supplies the model-criticism constructions.
- **MMP.7:** constructs the law of recorded data used for comparable predictions and repairs to selection or measurement assumptions.
- **MMP.11 / MMP.10:** supply admissible model families and constraint formulations when the failed prediction requires a changed relation.
- **MMP.13 / MMP.12 / C.16.IR:** supply inference, regularized recovery and the limits of what records resolve; a repaired fit does not remove those limits.
- **CMP.8 / CMP.9 / MATH.20:** obtain predictions and discrepancy calculations with the relevant numerical error or bound.
- **Causal-identification and observation-design methods:** receive the unresolved causal effect or distinguishing-observation question when it matters. Obtain these contributions from a suitable subject source or collaborator.
- **C.11.DUA and the subject method:** select worthwhile checking and establish the subject meaning of a repair. The receiving practice uses the revised prediction or restriction.

### MMP.14:End
