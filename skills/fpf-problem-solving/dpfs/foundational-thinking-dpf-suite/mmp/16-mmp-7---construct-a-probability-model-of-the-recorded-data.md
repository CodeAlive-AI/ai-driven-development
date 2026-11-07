## MMP.7 - Construct a Probability Model of the Recorded Data

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.7:1 - Problem frame

Use this pattern when inference depends on how events, responses or quantities become records, and that procedure has not yet been expressed in the probability model. A feedback log may contain successes more often than failures. A timed trial can end before its event occurs. Several readings can share one calibration error. In each case, fitting a familiar distribution to the visible numbers can answer a different question from the one you intended.

Start with one possible event and follow what the observing procedure would record. Include the possibility that it leaves no record, reports an interval or shares an influence with another observation. Repeat for a contrasting event. These cases reveal what the mathematical outcome must contain before you choose its distribution.

The result is a probability law for the recorded outcome under stated assumptions, together with its relation to the quantity being inferred. It can supply a likelihood, a distribution of future records or a reason the intended inference remains ambiguous. This pattern develops probabilistic formulation within mathematical modeling. The subject practice supplies the meaning of the event, the observation procedure and plausible relations among quantities.

You need conditional probability and sums over alternatives; continuous cases also use densities and integration. A collaborator can supply those operations when you can describe the observation procedure and interpret the returned law. If an existing model already represents that procedure and answers the question, use it. When only compatible ranges are needed, C.16.IR can provide a sufficient answer without probabilities.

### MMP.7:2 - Problem

The distribution of a subject property and the distribution of its records can differ. Selection changes which cases appear. Coarsening combines several possible values into one report. A common influence makes observations dependent. These transformations remain part of the inference even when a dataset presents every row in the same format.

A formula such as independent errors around a predicted value already makes choices about those transformations. If the choices are left implicit, more data and more accurate computation can reinforce a mistaken interpretation.

The difficulty is to construct the law of the observations from the modeled subject and its recording procedure, preserving the dependencies that matter to the question.

### MMP.7:3 - Forces

| Choice | What changes in the inference |
| --- | --- |
| Target population and included cases | A result about reported cases may require a selection model before it describes the target population. |
| Retain or remove unobserved quantities | Keeping them can clarify construction; summing or integrating them out can simplify computation. |
| Separate and shared influences | Conditional independence can hold while observations remain dependent after a shared influence is removed. |
| Rich observation model and obtainable information | Extra parameters can represent real effects while leaving the desired answer less identifiable. |
| Probabilistic answer and sufficient conditional answer | A likelihood can be useful before choosing an estimator or a prior. A bound may already settle the action. |

### MMP.7:4 - Solution

Construct the possible recorded outcomes from the observation procedure. Combine the subject and recording laws, remove the unobserved alternatives by the appropriate probability operation, and inspect what the resulting law permits you to infer. Return to the procedure or assumptions when its output does not answer the working question.

#### MMP.7:4.1 - Choose the target and the recorded outcome separately

State what the answer concerns: a rate in a population, a property before measurement, a future response, or another quantity selected by the work. Specify the population, conditions and time range when they change its meaning. Use C.16 for the characteristic being measured and C.16.MR for the relation from the property to an indication.

Describe one complete outcome of the observing procedure. It may contain a value and an inclusion flag, a duration and a timeout flag, or several related readings. The mathematical outcome space must distinguish every report the procedure can produce that affects the inference.

State what the observation plan fixes. Following a known cohort produces information about excluded cases that a sample drawn only from submitted reports may lack. Stopping after a specified time, after a specified number of records, or after an event can produce different data laws. Recover the actual plan before treating any count as fixed.

#### MMP.7:4.2 - Construct the joint law from the modeled dependencies

Introduce variables for the quantities used by that procedure. Explain their domains and meanings before assigning distributions. Let Z denote an underlying event or value and O its recorded outcome. Parameters theta describe quantities held fixed in the proposed probability model. When these laws are represented by probability masses or by densities under an appropriate reference measure, write the subject law as p_theta(z) and the conditional recording law as k_theta(o given z). Their joint expression is:

`p_theta(z,o) = p_theta(z) k_theta(o given z).`

Each factor needs an interpretation. The first describes variation in the subject under the stated conditions; the second describes how the procedure records it. A deterministic recorder assigns probability one to its specified output and zero to the other outputs. This accommodates rounding and threshold reports as well as random response or selection.

Use a sequence of conditional laws when more stages matter. Multiplication follows the chain rule. Omitting a variable from a conditional law asserts that, given the retained variables, it does not change that law. Make that assumption from the modeled relation; separate rows in a file provide no independence argument.

Keep an unknown fixed parameter as unknown. Give it a probability distribution only when that additional modeling choice is justified for the intended inference. A shared but unknown calibration offset can remain a parameter in a joint likelihood. A distribution over possible offsets supports a different, explicitly extended model.

#### MMP.7:4.3 - Obtain the law for what was actually recorded

The general operation averages the chance of an observed event over the underlying cases. Let K_theta(B given z) be the chance that the report falls in a set B, given underlying value z. Then:

`P_theta(O in B) = integral K_theta(B given z) P_theta(dz).`

Here P_theta(dz) means averaging with the probability law of Z: a weighted sum for discrete cases or an integral for continuous ones. A deterministic recorder O=g(Z) has K equal to one when g(z) lies in B and zero otherwise. This constructs its output law even when the joint pair (Z,O) has no ordinary joint density, as with O=Z for a continuously varying Z.

When the masses or densities used in :4.2 are available, the same averaging operation gives the law of a particular report. For discrete unobserved alternatives, sum:

`p_theta(o) = sum_z p_theta(z) k_theta(o given z).`

For continuous alternatives, integrate the product of the subject density and the recording factor. A report produced exactly when Z lies in a fixed set A has recording factor one inside A and zero outside; its probability reduces to the integral of the density over A. If the procedure chooses which set to report, retain that choice in k_theta(A given z).

For example, let Z be equally likely to be 0 or 1. A truthful recorder reports {0,1} always when Z=0 and with probability 1/2 when Z=1; otherwise it reports {1}. The probability of receiving {0,1} is `1/2 + (1/2)(1/2) = 3/4`, although the probability that Z lies in {0,1} is one. The recording factor makes the difference.

For an individually observed continuous value, use a density with respect to the stated measurement convention. A point density and the probability of an interval have different meanings.

When inclusion in the dataset is itself a condition of sampling, retain its normalization. If Z has density or mass p_theta(z), and s_theta(z) is its probability of inclusion, the included-case law is:

`p_theta(z given included) = p_theta(z) s_theta(z) / P_theta(included).`

The denominator is obtained by summing or integrating the numerator over all admitted z and must be positive. If it depends on theta, dropping it changes the inference. When the counts or identities of excluded cases are also observed, include that information in the joint outcome instead of silently discarding it by conditioning. Section :5.1 shows the change.

Keep shared influences shared during elimination. For observations conditionally independent given an unknown B, integrating one joint product over B generally differs from multiplying separately integrated factors. The latter construction assigns a fresh B to each observation. Use it only when that is the observing arrangement.

#### MMP.7:4.4 - Connect the law to inference and prediction

When the observation laws have a common probability-mass or density representation, insert the recorded outcome o into p_theta(o). As a function of theta, this gives a likelihood, up to a factor independent of theta. It need not sum or integrate to one over theta. Estimation or a posterior distribution requires the chosen inferential method and its assumptions; the observation law is the input to that work.

Before drawing an inference, check whether the recording rule admits the received report for any parameter value. A continuous reading can be admitted even though its single-point probability is zero; determine admissibility from the modeled observation mechanism and the cases it permits. If no admitted case produces the report, return the conflict and locate which assumptions or recording steps need reconsideration, using C.16.IR:4.4. For example, a fixed signal with one fixed additive offset and one unchanged threshold must produce identical bits on repetition. A mixed sequence contradicts that joint account. It cannot be repaired by fitting a different signal within the same family.

Identify how the requested quantity depends on theta or on a future outcome. Two parameter settings can induce the same law for every possible record while assigning different values to the target. Constructing such a pair shows that this observation model cannot identify that distinction. C.16.IR supplies the corresponding compatible-case reasoning; numerical fitting alone cannot resolve it.

For a future record, specify whether its recording procedure is the same. For the underlying population quantity, return through the subject law rather than interpreting a selected-case rate as the population rate. A proposed intervention requires its changed relations under C.28; changing a predictor value in a fitted association is insufficient when the intervention changes how the data arise.

#### MMP.7:4.5 - Test a consequence and revise the construction

Check normalization and a small case that follows the procedure. Enumerate a finite outcome space or generate subject cases and pass them through the recorder. Compare that construction with the probabilities or summaries derived from the observation law. C.29.2 supplies a computational construction when enumeration or integration needs further work.

When the inclusion rule, timeout, shared calibration or receiving question actually changes, revise the affected relation and carry its consequence through the calculation. Compare a plausible alternative condition when the comparison can change the intended use or returned claim; this can expose the observation mechanism beyond one fixed formula. An already sufficient construction under unchanged conditions needs no invented variation.

A simulation agreeing with the formula checks their agreement under the modeled assumptions. An available observation can challenge those assumptions; selected domain assurance determines which empirical comparison is worth performing. C.11.DUA helps choose between further observation, a conditional answer and acting with remaining uncertainty. Preserve a sufficient result without demanding another dataset merely because an influence remains unknown.

### MMP.7:5 - Archetypal Grounding

#### MMP.7:5.1 - Infer a success rate from a selectively submitted log

A team asks what fraction of attempts succeed. In a proposed model, each attempt succeeds with probability p. Every success is logged; each failure is logged independently with probability 1/4. Initially the team has a fixed-size sample of independently drawn log entries, with no information about how many attempts produced the source log.

The event variable Y is success or failure. The recording flag R says whether the attempt enters the log. Their joint probabilities are:

| Outcome | Probability |
| --- | --- |
| Success, logged | p |
| Failure, logged | (1-p)/4 |
| Failure, unlogged | 3(1-p)/4 |

The included-case success probability is `q = p / [p + (1-p)/4] = 4p/(1+3p)`. If the observed fraction of successes is 1/2, the likelihood estimate of q is 1/2, and transforming it gives `p_hat = q_hat/(4-3q_hat) = 1/5`. Sampling uncertainty remains; this calculation corrects which rate is being estimated.

The first useful result is the distinction between a 50% rate among reports and the estimated 20% rate among attempts under the supplied reporting assumptions. If the failure-reporting probability is unknown, several combinations of that probability and p can produce the same q. The log alone then leaves the population rate unresolved.

Now the procedure changes: a register names a fixed cohort of N attempts and links each submitted report to its attempt. Model those attempts as independent, each with the same success probability p, retaining the stated reporting rule. Since every success is reported, an unreported attempt is a failure. If there are k success reports, the likelihood for p is proportional to `p^k (1-p)^(N-k)`; the failure-reporting factors do not depend on p. The estimate becomes k/N. Conditioning only on reported entries would throw away information the revised procedure provides.

This is a change in the team's observing method. A.3.2.DE explains the changed recording rule; C.32.MWA.PP connects that contribution to actual performers and support. Whether to introduce it depends on what resolving the population rate would change in the team's work.

#### MMP.7:5.2 - Preserve a common influence across readings

Two sensors measure quantities x1 and x2 with one shared calibration offset b. Their readings are `Y1=x1+b+E1` and `Y2=x2+b+E2`, with independent zero-mean errors of variance sigma squared. Begin by retaining b as a common parameter. The joint conditional law factors given b; each factor uses that same value.

For the difference, `Y1-Y2=x1-x2+E1-E2`: the offset cancels. Its error variance is `2 sigma^2`. A measurement of the difference can therefore be useful while either absolute value remains uncertain.

For repeated measurements of one x, suppose an additional justified model describes the common offset as a zero-mean random variable B with variance tau squared, independent of the errors. The average of n readings has variance `tau^2 + sigma^2/n`. Integrating a separate offset for every reading would incorrectly produce `(tau^2+sigma^2)/n`. Repetition reduces independent noise but leaves this common calibration contribution.

If the instrument is independently recalibrated before every reading, the arrangement changes. A separate-offset model can then be appropriate. The governing operation is to trace which influences are shared and preserve that sharing in the probability construction.

#### MMP.7:5.3 - Use a timed-out trial as an interval report

A test asks how long an event takes. Each independent trial is observed until its event or a fixed timeout c. Record both `V=min(T,c)` and a flag D indicating whether the event occurred before timeout. As an illustrative subject assumption, let T have exponential density `lambda exp(-lambda t)` for t at least zero, with lambda positive.

An event at time t before c contributes the density `lambda exp(-lambda t)`. A timeout contributes `P(T>=c)=exp(-lambda c)`, obtained by integrating the density over the unobserved tail. For m completed trials and total observed time S, including the timeout durations, the likelihood is proportional to `lambda^m exp(-lambda S)`.

With completions at times 1 and 2 and one timeout at 4, `S=7` and `m=2`. Maximizing this illustrative likelihood gives `lambda_hat=2/7`. Treating the timeout as a third event instead gives 3/7; dropping it gives 2/3. The flag determines which operation is correct.

If only completed trials enter a database and neither the number nor identities of timed-out trials are available, the observed-time density instead conditions on completion: divide the event density by `1-exp(-lambda c)` on the interval before c. A changed recording rule changes the model even when the stored times look the same. The exponential assumption is dispensable: a different duration law supplies its own event density and tail probability.

### MMP.7:6 - Bias-Annotation

The visible dataset invites treating its rows as the whole observation procedure. Begin from how a row, absence or interval report is produced. A second temptation is to add one independent error to every row; trace shared influences before factorizing. More detailed modeling can also conceal missing knowledge, so retain uncertainty in the recording mechanism when the available information does not determine it.

### MMP.7:7 - Conformance Checklist

- Can a reader identify the target and all possible reports that affect the inference?
- Do the subject and recording factors describe the stated procedure, including what it fixes and what it reveals?
- Are unobserved alternatives removed by a justified sum, integral or conditioning operation?
- Does the joint law preserve common influences and any information about excluded cases?
- Is the first result interpreted as a likelihood, estimate, prediction, bound or unresolved distinction with its respective conditions?
- Can the formulation be changed when the observing procedure or receiving question changes?

### MMP.7:8 - Common Anti-Patterns and How to Avoid Them

| Failure in this work | Repair |
| --- | --- |
| Reported-case frequency is substituted for population frequency despite selective reporting. | Derive the included-case law and the relation to the target rate. |
| An interval report is replaced by an event at its endpoint. | Sum or integrate the joint subject-and-recording law over the underlying values that can produce the report. |
| A common influence is independently removed from every observation. | Keep it in the joint law before elimination. |
| A likelihood is read as a probability distribution over the unknown parameter. | Supply the inferential method that turns it into the requested result. |
| A fitted model is trusted because its simulator reproduces its own assumptions. | Separate computational agreement from the subject comparison needed for the use. |

### MMP.7:9 - Consequences

The constructed law allows computation to answer the intended observation question and can expose an ambiguity before expensive fitting. A changed reporting procedure becomes a model change that can be analyzed. The work may also show that the target needs assumptions or information absent from the records; a narrower conditional answer can remain useful.

### MMP.7:10 - Architectural Rationale

The observation procedure connects the subject to the data used in inference. Keeping that connection explicit makes deterministic coarsening, random selection and shared uncertainty instances of one construction. It also separates modeling choices from the later choice of an inference algorithm.

The factors are chosen for the procedure and question. Their order as a probability factorization does not establish a causal direction in the represented world. Several factorizations can describe one joint law; the subject account and intervention question determine any causal interpretation.

This method uses C.16's measurement and resolvability work while supplying the probability operations those patterns leave to statistical modeling. Its examples require different transformations: conditioning after selection, joint elimination and tail integration. The transferable operation survives replacing the logged activity, sensor or timed event.

### MMP.7:11 - SoTA-Echoing

[Gelman, Vehtari and McElreath, Statistical Workflow (2025), sections 1.1-1.7](https://sites.stat.columbia.edu/gelman/research/published/Statistical_Workflow_article.pdf), emphasize measurement, assumptions, shared information and the distinction between model parameters and inferential targets. Adopt the connection of those decisions to model construction and revision. Their comparison of Bayesian and other workflows supports leaving the inference method explicit; it does not select one estimator for every observation law.

[Rubin, Inference and missing data (1976)](https://doi.org/10.1093/biomet/63.3.581), is a historical foundation for specifying when a missing-data mechanism can be ignored. Adopt the requirement to establish the applicable conditions rather than assuming that absence is harmless. Its qualifications depend on the inferential method. The examples here derive their recording laws directly and require no blanket ignorability claim.

The [Stan User's Guide 2.39 treatment of truncation and censoring](https://mc-stan.org/docs/stan-users-guide/truncation-censoring.html) provides executable constructions for restricted observations and tail reports. Adapt those probability operations to :4.3 and :5.3. The guide's programming and inference conventions are useful implementations, not prerequisites of the method. A direct finite calculation or another suitable implementation can supply the same law.

The three demonstrations are elementary constructions for this pattern. They explain the modeling operations under stated assumptions.

### MMP.7:12 - Relations

C.16.MR constructs the relation from a sought property to its indication; this pattern makes its probability law usable for inference. C.16.IR identifies what the resulting observations can resolve. C.29.2 constructs a computation for marginalization, estimation or prediction when needed, and C.29.3 addresses its realization. C.28 governs a causal use of the result. MMP.8 uses the observation model to determine the information available to a decision. B.5.MPC.R coordinates a repair spanning subject interpretation, mathematical formulation and computation. MMP.22 uses a mathematical transformation to construct a changed observing rule; C.32.MWA.PP compares its practical conditions and A.3.1.MV retains a consequential Method variant.

### MMP.7:End
