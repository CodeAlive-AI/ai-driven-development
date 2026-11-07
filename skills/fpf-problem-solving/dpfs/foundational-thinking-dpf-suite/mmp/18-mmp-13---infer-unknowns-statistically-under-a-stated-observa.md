## MMP.13 - Infer Unknowns Statistically under a Stated Observation Model

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.13:1 - Problem frame

Use this pattern when a probability model describes how records arise, and the work needs an estimate, an interval or a probability about something not directly known. The wanted quantity may be a failure probability, a mean before measurement error, a response for a different mix of cases, or a future outcome.

Start by writing the sentence the result must support. “This procedure covers the fixed unknown in at least 95% of its modeled repetitions” differs from “the unknown lies here with 95% posterior probability under these assumptions.” A probability about the next observation is another question. Choose the inferential construction that supports the required sentence.

The result is an estimator or posterior and its consequence for the requested target, with an interpretable account of uncertainty. It exposes which assumptions make the conclusion possible and which change would require recalculation. Reporting a fitted coefficient and a number labeled “error” can otherwise leave the actual question unanswered.

This is statistical inference within mathematical modeling. MMP.7 supplies the law of the records; MMP.12 supplies unresolved recovery ambiguities and any regularization choices. The present method constructs what may be concluded under that law and additional inferential assumptions. Selecting an action also needs its consequences and preferences, supplied by a decision method such as MMP.8.

The reader needs conditional probability, expectations and quantiles; continuous models also use integration. A mathematically qualified collaborator can supply those operations when the practitioner can specify the observation process and interpret the target.

Use an existing sufficient inference directly. If a compatible range already settles the question, C.16.IR can end the work without a probability model. A missing observation law returns to MMP.7; constructing a numerical sampler for an already specified posterior belongs to CMP.9.

### MMP.13:2 - Problem

The distribution of the observed records does not itself choose an estimator, an uncertainty statement or a prior. Those additions can produce different useful conclusions from the same data.

The inferential target may also differ from the fitted parameters. A nonlinear function of parameter estimates can give a different answer from averaging that function over a posterior. Shared uncertainty can remain after many repeated readings. A narrow interval for an expected response can coexist with a wide distribution for the next response.

The problem is to construct the inference needed by the receiving use while preserving its sampling, conditioning and approximation assumptions. Changing one of those assumptions must change the relevant calculation, rather than only the qualification attached to an unchanged number.

### MMP.13:3 - Forces

| Force | Tension |
| --- | --- |
| Target and parameterization | The model can contain many unknowns while the use needs only one function of them. |
| Conditional probability and repeated-use performance | A posterior probability and confidence coverage answer different questions. |
| Convenient defaults and supported assumptions | Independence, a prior or a normal approximation can simplify the calculation while changing its meaning. |
| Joint uncertainty and simple summaries | Separate standard errors can lose covariance needed by the target. |
| Inferential precision and computational precision | More accurate integration can leave the subject uncertainty unchanged. |

### MMP.13:4 - Solution

Specify the target and the intended uncertainty claim. Combine the record law with the inferential assumptions needed for that claim, derive the estimator or posterior, and propagate it to the target. Carry any actual consequential revision through the affected calculation. Compare a plausible alternative assumption only when doing so can change the use or returned claim. Return the sufficient result at the scope the calculation supports.

#### MMP.13:4.1 - Fix the target before choosing a fitting routine

Write q=g(theta), where theta denotes the unknowns in the observation model. It can index a distribution or unknown function, not just a finite vector. State the population, conditions and time range that make q meaningful. Distinguish unknowns needed only to explain the records from the target being returned.

For prediction, instead name the new outcome Y_new and its observing conditions. A conditional mean of Y_new is a function of theta; the realized Y_new also varies under the model. A proposed intervention requires a supplied causal identification argument before a fitted association can be interpreted as its effect.

Select the smallest result that changes the next use. It may be a point estimate with a stated error property, an upper confidence bound, a posterior probability of a threshold, or a predictive distribution. A threshold action still needs its loss or decision rule; a probability or confidence level does not choose that action by itself.

#### MMP.13:4.2 - Recover the law and the assumptions being added

Take the joint law P_theta of the records Y from MMP.7. Retain its inclusion, censoring, dependence and stopping conditions. Where a common probability-mass or density representation exists, inserting the observed y gives the likelihood L(theta;y)=p_theta(y).

The likelihood compares how parameter values account for the same records. It is not a probability distribution over theta merely because it can be plotted or maximized. Likewise, records in separate rows are not necessarily independent observations.

Use the existing ambiguity result from MMP.12 or C.16.IR. If two parameter values give the same observation law and different q, the records cannot distinguish that target. A prior or restriction may support a conditional answer, whose dependence on that addition remains visible.

Choose the inferential branch by the claim required. Frequentist construction assesses a data-to-answer rule across the specified observation law at fixed unknown values. Bayesian construction adds a prior law and conditions their joint model on the observed records. Neither branch removes the need for a justified observation model.

If the same data choose a model, tuning value or prior hyperparameter, include that adaptation in the inference being claimed. Treating an estimated quantity as externally known can understate uncertainty. A sensitivity comparison can instead hold the data fixed and show the consequence of several explicitly conditional assumptions.

#### MMP.13:4.3 - Construct an estimator and its frequentist uncertainty when needed

An estimator is a rule q_hat=T(Y), chosen before its repeated-use properties are assessed. Derive it from the target and observation law: for example, invert an observable expectation, solve an estimating equation, or maximize a likelihood and obtain the required function of the fitted values. State the selected property, such as a controlled error probability or mean squared error. Likelihood maximization alone supplies no interval.

One general confidence construction chooses, for each admitted theta, an acceptance region A_theta of possible records such that

`P_theta(Y in A_theta) >= 1-alpha.`

After observing y, retain those theta for which y lies in A_theta, and map them through g. The resulting set C(y) has coverage

`P_theta(g(theta) in C(Y)) >= 1-alpha`

under the stated law. A target-specific statistic can make this much cheaper than constructing a set for every nuisance parameter. The binomial inversion in :5.1 is a small example.

Coverage describes the procedure across repetitions allowed by the model, at fixed theta. It does not assign posterior probability to the parameter in the one observed interval. Nor is a confidence set the set of all logically possible values: a value outside it may still assign a small positive probability to these records.

Use an exact distribution or justified pivot when available. An asymptotic approximation needs its sample-size, regularity and boundary conditions. A bootstrap needs a resampling unit and mechanism that represent the dependence and the fitted procedure; resampling individual readings cannot reproduce an omitted common calibration error. Retain approximate coverage as approximate unless a stronger result is available.

The observation plan belongs to the guarantee. An interval justified at a fixed sample size need not preserve its coverage when repeatedly inspected until it looks favorable. Use a method valid for the actual stopping plan. For countably many looks, one conservative construction allocates error probabilities alpha_j with sum at most alpha to valid per-look intervals; the union bound gives simultaneous coverage. An applicable confidence-sequence method can provide a less conservative construction. This is a choice of inferential guarantee, not a requirement to collect more data.

#### MMP.13:4.4 - Construct a posterior when conditional probability is needed

Supply a prior probability law Pi with its subject meaning. Reweight that law by the observed likelihood and normalize, preserving any point masses and continuous parts. For a set A to which the prior assigns a probability,

`Pi_y(A) = integral_A L(theta;y) Pi(dtheta) / integral L(u;y) Pi(du).`

Pi_y denotes the posterior law. Integration against Pi means combining values under the actual prior: a sum for discrete unknowns, integration against a density where one exists, and both contributions for a mixture. A function-valued unknown requires a specified prior law and likelihood on that space, not an assumed ordinary density.

The denominator must be finite and positive; an unnormalized expression alone does not establish a posterior probability law. For a real vector theta whose prior has a density pi(theta) with respect to ordinary volume dtheta, the posterior density is

`pi(theta | y) = L(theta;y)*pi(theta) / integral L(u;y)*pi(u) du.`

This density formula is a representation of the preceding law construction under that condition. A uniform prior depends on the parameterization, and an improper prior requires a separate argument that the posterior exists.

For example, give a failure probability p prior mass 1/2 at p=0 and a uniform distribution on [0,1] for the remaining 1/2. One failure-free Bernoulli observation has likelihood 1-p. The unnormalized atom has mass 1/2; the weighted continuous part has mass 1/4. Normalizing by 3/4 leaves posterior mass 2/3 at zero. The remaining 1/3 has conditional density 2\*(1-p) on [0,1]. Using only the ordinary density would lose the atom.

Retain joint dependence when removing nuisance unknowns. Sum or integrate the joint posterior over them, or calculate g(theta) from joint posterior draws. Independently combining draws from marginal distributions changes the joint law unless independence is established.

Derive the posterior of q through that transformation. For a set B,

`P(q in B | y) = integral 1{g(theta) in B} Pi_y(dtheta).`

A credible set has its stated posterior probability under this model and prior. A posterior mean, median or quantile is a chosen summary of that law. In general, `E[g(theta)|y]` differs from `g(E[theta|y])`; :5.1 computes the difference.

A penalized optimum from MMP.12 can coincide with a posterior mode when its objective represents the chosen likelihood and prior. That optimum still does not supply the posterior spread. If a prior resolves an otherwise unidentified difference, preserve that source of the resolution in the returned result.


#### MMP.13:4.5 - Propagate uncertainty to the actual receiving quantity

For a posterior predictive result, construct the law of the new observation under its specified conditions and average it over the posterior law:

`P(Y_new in B | y) = integral P(Y_new in B | theta,y) Pi_y(dtheta).`

In the density case of :4.4, Pi_y(dtheta) is pi(theta | y) dtheta. For a mixed posterior, include its atoms as well as its continuous contribution.

This includes both uncertainty in unknowns and the modeled variation of a new outcome. Where variances exist, the decomposition is

`Var(Y_new|y) = E[Var(Y_new|theta,y)|y] + Var(E[Y_new|theta,y]|y).`

The second term alone concerns uncertainty in the conditional mean. It is not the full predictive variance.

A frequentist prediction interval also needs the joint law of the original and future records. Derive a prediction error or another statistic with the needed coverage. Sharing a calibration influence with the old readings and using a fresh calibration produce different prediction problems, as in :5.2.

For a posterior of a real parameter vector theta with covariance V, the linear target q=a\^T\*theta has posterior variance a\^T\*V\*a. A frequentist covariance calculation instead uses the sampling covariance of the joint estimator, retaining its repeated-use interpretation. For a nonlinear target, propagate the joint posterior or derive uncertainty from the estimator's sampling law; an approximation needs its own conditions. A confidence set for theta can be mapped through g to obtain a confidence set for q; projecting a large joint set can be conservative. A marginal interval for each coordinate does not automatically give simultaneous coverage for a function of them.

Then obtain the numerical answer with the needed accuracy. CMP.8 supplies controlled approximate computation; CMP.9 supplies a sampler or randomized computational estimator. The posterior distribution, a confidence procedure and the algorithm approximating their consequences are different results. More posterior draws can reduce Monte Carlo error in a computed mean while leaving the posterior uncertainty about q unchanged.

#### MMP.13:4.6 - Test the claimed consequence and revise the assumption that matters

Check the derivation at the level needed for its use. In a finite model, normalization, enumeration or an exact calculation may suffice. For an approximate frequentist procedure, simulation at fixed parameter values can expose bias or coverage failures under the assumed law. For a posterior computation, a suitable simulation-based calibration check draws parameters and data from their joint model and tests the inference computation. These are different checks. Agreement under a model does not establish that the model describes the subject.

Select such work for an unresolved claim. A routine use of an applicable exact result need not become a new simulation study, and simulated datasets are not additional subject observations.

When a premise or target actually changes, recalculate the affected target and uncertainty; reuse unaffected results. Compare a plausible alternative dependence, prior scale, inclusion probability or target-population weight only when that comparison can change the intended use or returned claim. State whether an altered result comes from changed records, changed assumptions or a changed target, and keep a material disagreement visible. A sufficient inference under unchanged grounds needs no invented alternative.

If observed failures call for a richer model, return the model-criticism and revision question to the relevant subject method and MMP.11. If the desired effect is not causally identified, return that identification question. Designing a new observation is a further choice when the existing result is insufficient; it is not part of every inference.

#### MMP.13:4.7 - Return the conclusion at its established meaning

Return the target, the estimate or distribution, the meaning of its uncertainty, and the assumptions whose variation changes its use. Identify a numerical approximation limit separately. Give the receiver enough to distinguish a frequentist coverage claim, a posterior probability and a predictive claim without consulting the fitting software.

Use the sufficient result. C.11.DUA helps compare another observation, a changed formulation, more computation or action with remaining uncertainty when that choice is live. B.5.RR carries a changed premise through the reasoning; MMP.8 receives inference when an actual choice needs its consequences and preferences.

A methodological use can revise how a working method treats uncertainty: retain a shared influence, compute the requested derived quantity, or stop demanding an unidentified parameter when a sufficient consequence is available.

### MMP.13:5 - Archetypal Grounding

#### MMP.13:5.1 - Zero recorded failures: two different uncertainty claims

A device is tested for a fixed four operations. All failures are recorded, and the supplied model gives independent Bernoulli outcomes with one unchanged failure probability p. No failures occur, so K=0 and the likelihood is proportional to (1-p)^4.

Suppose the requested target is the probability of at least one failure in two further operations under the same condition:

`q=1-(1-p)^2.`

The future operations are assumed independent conditional on the same p. The question concerns q, rather than every detail of an operating model.

**Frequentist construction.** The likelihood estimate is p_hat=K/4=0. Inserting it into the familiar normal standard-error expression gives zero estimated standard error and the interval [0,0]. At p=0.2, zero failures occur with probability 0.8^4=0.4096, and [0,0] excludes the true p on every such occurrence. This alone rules out 95% coverage.

For a one-sided 95% binomial upper confidence procedure, invert the lower-tail probability: for k<4 choose U(k) satisfying

`P_(p=U(k))(K<=k)=0.05,`

and set U(4)=1. Binomial test inversion gives coverage at least 95%, allowing conservatism from discreteness. At k=0,

`(1-U)^4=0.05; U=1-0.05^(1/4)=0.5271.`

Since q increases with p, its upper confidence limit is

`1-(1-U)^2=1-sqrt(0.05)=0.7764.`

This is the result of a covering procedure, not a statement that q has a 95% probability of being below 0.7764 after these records.

**Bayesian construction.** Choose a uniform prior for p on [0,1]. Multiplying and normalizing gives posterior density

`pi(p|K=0)=5*(1-p)^4; 0<=p<=1.`

Thus E[p|K=0]=1/6, and the posterior 95% upper quantile of p is `1-0.05^(1/5)=0.4507`. Transforming that quantile gives a posterior 95% upper quantile of q of `1-0.05^(2/5)=0.6983`. Its smaller value does not make it a uniformly better confidence limit; it expresses a different conditional claim with a prior.

To obtain the probability of a failure in the next pair, average q itself:

`E[q|K=0] = 1 - integral_0^1 (1-p)^2*5*(1-p)^4 dp = 2/7.`

Using the posterior mean of p first would give `1-(5/6)^2=11/36`, a different value. The posterior predictive probability is 2/7; the event of a failure in that pair remains a binary future outcome.

**Changed assumption.** Hold the four records fixed but replace the uniform prior with density `9*(1-p)^8`, favoring lower failure probabilities. The posterior becomes `13*(1-p)^12`. The posterior probability of p<0.2 changes from `1-0.8^5=0.67232` to `1-0.8^13=0.94502`; the predictive probability for a failure in the next pair becomes 2/15.

These changes come entirely from the prior. They neither add operations to the observed test nor establish that the new prior is appropriate. If its relevance is unresolved, return the conditional results and their difference. The frequentist bound remains available without that prior under the original fixed-sample observation model.

#### MMP.13:5.2 - A common calibration error survives averaging

Four readings in fixed units are 9, 10, 10 and 11, giving mean 10. Initially suppose

`Y_i=mu+epsilon_i; epsilon_i independently Normal(0,1).`

The noise variance 1 is supplied, not estimated from these four values. The sample mean is an estimator of mu with variance 1/4. An exact normal 95% confidence procedure uses `mean(Y) +/- c/2`, where c is the 0.975 standard-normal quantile, approximately 1.96. The realized interval is approximately [9.020,10.980].

A prediction interval for one independent future reading uses the error `Y_new-mean(Y)`, whose variance is `1+1/4`. Its realized 95% interval is approximately [7.809,12.191]. Uncertainty about the mean and variation of the future reading require different intervals even before any model revision.

Now revise the calibration account:

`Y_i=mu+B+epsilon_i; B~Normal(0,1).`

B is independent of the individual errors, shared by all readings in one setup, and drawn afresh across the repeated setups used to define the coverage claim. Then

`Var(mean(Y))=1+1/4.`

The confidence interval for mu widens to [7.809,12.191]. Treating B as a fresh independent error on each row would instead give variance 2/4 and understate the uncertainty. More readings in this same setup reduce the individual-noise term but leave the calibration term.

Prediction also depends on what stays shared. A new reading in the same setup has the same B, which cancels in `Y_new-mean(Y)`; the prediction-error variance remains 1+1/4. A reading in a new setup with independent B_new has variance `1+1+1+1/4=3.25` for that error, giving approximately [6.467,13.533].

These are coverage statements over the stated repeated-observation law. If B is only an unknown fixed offset with no bound or probability law, these normal intervals for mu do not follow. MMP.12 then retains the unresolved separation of mu and B; assigning B a distribution is an additional modeling contribution.

#### MMP.13:5.3 - Infer the rate for the receiving workload

Two classes of requests have different probabilities of finishing by a deadline. For class A, seven of eight observed requests finish; for class B, one of eight finishes. Assume fixed sample counts, independent Bernoulli outcomes within each class, independent class data, and independent uniform priors for p_A and p_B.

The posterior densities are proportional to `p_A^7*(1-p_A)` and `p_B*(1-p_B)^7`: Beta(8,2) and Beta(2,8). Their means are 0.8 and 0.2, and each variance is 4/275. The posteriors are independent under the stated construction.

For a future workload selecting the two classes equally, the conditional completion probability is `q_old=(p_A+p_B)/2`, with posterior mean 0.5. Now change only the receiving workload: its known class proportions are one-quarter A and three-quarters B. The target becomes

`q_new=p_A/4+3*p_B/4.`

Its posterior mean is 0.35 and its posterior variance is

`(1/4)^2*(4/275)+(3/4)^2*(4/275)=1/110.`

No new fitting is needed for this changed target. Carrying forward 0.5 would answer for the old mixture. If the target were an individual future completion indicator, its posterior predictive probability would be 0.35 and its variance 0.35\*0.65, rather than 1/110.

The transfer assumes that the within-class probabilities remain applicable. Changed operating conditions require their own relation. Uncertain class proportions or a shared influence on the two probabilities require joint uncertainty, rather than the independent weighted-variance calculation above.

### MMP.13:6 - Bias-Annotation

The worked laws are simple enough for exact calculations. Real records can have selection, dependence, weak identification or model mismatch that a convenient binomial or normal family conceals. The resulting uncertainty is conditional on the assumptions represented; it does not automatically include an omitted mechanism.

Bayesian and frequentist results are compared by the conclusions they support. A narrower interval alone cannot rank different probability meanings. The choice of prior, coverage domain and receiving target is part of the inference, even when software supplies defaults.

### MMP.13:7 - Conformance Checklist

- The inferential target and its subject conditions are stated separately from nuisance unknowns and the subsequent decision.
- The observation law retains consequential recording, dependence and stopping assumptions.
- The estimator's repeated-use claim or the posterior's conditioning assumptions are recoverable; normalization or coverage has an applicable basis.
- Joint uncertainty is propagated to the actual target. Parameter uncertainty, future-observation variation and numerical error are distinguished.
- Any actual consequential revision is propagated through the affected target and uncertainty calculation. A sensitivity comparison addresses a live alternative that can change the use or returned claim; an unchanged sufficient inference needs none.
- The returned conclusion is sufficient for its use or names the missing contribution without requiring an automatic new experiment.

### MMP.13:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A confidence interval is read as posterior probability for the observed interval. | State which object varies under the probability law and which claim the construction supports. |
| A likelihood curve or penalized optimum is treated as a posterior distribution. | Supply and normalize the prior-likelihood construction before using posterior probabilities. |
| A derived result is computed only from parameter means or separate standard errors. | Transform the joint inference; retain nonlinear effects and covariance. |
| More readings are assumed to remove a shared uncertainty. | Derive the variance under the actual dependence, as in :5.2. |
| Smaller Monte Carlo error is reported as less subject uncertainty. | Qualify the computed summary separately from the distribution it summarizes. |
| The prior or fitted model is changed without recalculating the receiving conclusion. | Carry the revised assumption through the target and uncertainty calculation. |

### MMP.13:9 - Consequences

The receiver gets an estimate or distribution with a usable meaning for its uncertainty. A needed probability, bound or prediction can be obtained without recovering every parameter, and a changed target can sometimes reuse the existing joint inference.

The method also makes the cost of assumptions visible. Another record, another prior and another numerical approximation change different parts of the answer. A sufficient inference can be used while a stronger claim remains unresolved.

### MMP.13:10 - Architectural Rationale

The observation model describes how records vary. The inferential construction determines how those records support conclusions about unknowns. Target propagation determines which consequence reaches the receiving use. Their separation permits a computation to be correct while its prior, target or observation assumption is still reconsidered.

This preserves the distinction from inverse-problem regularization, numerical computation, causal identification, model criticism and decision making. Those methods supply or receive particular contributions; none is obtained merely by fitting a statistical model.

### MMP.13:11 - SoTA-Echoing

**Carrying fitting into the required conclusion.** **Adopt** target-specific propagation of joint uncertainty rather than reporting a coefficient table or substituting parameter means. [Gelman, Vehtari and McElreath, *Statistical Workflow*, §§1.3–1.6 and 1.10, author manuscript dated 5 December 2025 for the 2026 article](https://sites.stat.columbia.edu/gelman/research/published/Statistical_Workflow_article.pdf) explains how dependencies, derived quantities and calibration affect both Bayesian and non-Bayesian workflows. This changes :4.1 and :4.5–4.6. In :5.1 and :5.3 the extra calculation is small and corrects the actual requested probability or workload target. The source does not rank one inferential philosophy above the other, nor validate a particular subject model. Reopen when another construction gives the same target meaning and uncertainty at lower effort, or when changed dependencies defeat the propagation.

**Uncertainty near a parameter boundary.** The serious default is the normal standard-error interval, which collapses in :5.1. **Adopt** binomial tail inversion when its fixed-sample coverage is the requirement; **retain** a posterior alternative when its prior-conditional probability is wanted. [NIST/SEMATECH e-Handbook, §7.2.4.1](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) supplies the explicit comparator and small-sample construction. The few tail calculations cost little here and repair the degenerate result; discreteness can make coverage conservative. A posterior requires the additional prior and can change materially with it. This comparison governs :4.3–4.4 and :5.1, not a universal preference for exact intervals. Reopen for a changed sampling law or a justified approximation that meets the same coverage need more efficiently.

**Inference when observations determine stopping.** **Adapt** simultaneous coverage as a conditional alternative to fixed-time intervals in :4.3. [Howard et al., *Time-uniform, nonparametric, nonasymptotic confidence sequences*, §1 and equation (1), arXiv:1810.08240v9](https://arxiv.org/html/1810.08240v9) supplies the stronger guarantee and its cost in interval width. Its stated stochastic conditions still apply. A fixed-time method remains sufficient for its own observation plan; sequential machinery is unnecessary there. Reopen when the actual stopping rule changes or a narrower valid construction improves the needed inference at comparable effort.

### MMP.13:12 - Relations

- **Uses MMP.7** for the law of recorded outcomes and **MMP.11** for the model family when that family needs construction.
- **Uses MMP.12 and C.16.IR** for unresolved recovery distinctions and sufficient target bounds. Adds estimator or posterior construction and the meaning of inferential uncertainty.
- **Uses CMP.8 and CMP.9** to obtain numerical consequences of the selected inference, with computational error separate from inferential uncertainty.
- **Supplies prediction and model criticism** with conditional consequences that can be compared with relevant observations. A causal interpretation additionally needs its identification argument under C.28.
- **Supplies MMP.8** with estimates or distributions used in a decision; **C.11.DUA** compares the value of further information or computation when needed.
- **Uses B.5.RR** to propagate a changed premise. C.39 can use the resulting inference to construct the changed contribution to obtaining or interpreting records; A.3.1.MV distinguishes a Method variant from an implementation correction.

### MMP.13:End
