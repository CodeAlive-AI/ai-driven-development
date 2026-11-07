## CMP.9 - Construct a Randomized Estimator or Sampling Procedure

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.9:1 - Problem frame

**Use this when** a computation needs a sample from a specified law, or an estimate that would be expensive to obtain by enumeration, and the sampling or estimation procedure must be constructed or changed. Available random bits, a stream, a convenient proposal distribution or local transitions can supply the starting operations.

The algorithm must connect those operations to the requested distribution or statistic. A random-looking output is insufficient: it may sample records in proportion to their multiplicity, favor high-degree states, or omit a rare but consequential contribution.

The gain is an effective sampler or estimator with its target, bias and dependence understood sufficiently for the receiving use. The reader needs elementary probability, expectations and the stated computational access. The method applies to discrete choices, data streams, simulation and learned procedures; a physical noise source is one possible realization.

Use a direct deterministic computation or an already suitable sampler when it meets the need affordably. Choosing a probability model for observations is a separate modeling task, supplied by MMP.7 when applicable. This method can also sample a mathematically specified set without making any empirical-population claim.

### CMP.9:2 - Problem

How can available random operations produce the desired law or an informative estimate under finite time and storage, and what conclusion remains warranted after changing the sampling or stopping procedure?

More samples reduce some variation but do not repair a wrong target or a missing region of support. Correct stationary probabilities do not establish rapid convergence from the chosen start. An interval valid for one fixed sample size may not remain valid when repeatedly inspected to decide when to stop.

### CMP.9:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Accessible randomness and target law | The easiest draws may have different probabilities from those the task needs. |
| Broad coverage and informative samples | Oversampling useful regions helps only with an appropriate correction and retained support. |
| Cheap transitions and useful information | Correlated steps may be inexpensive but add little information. |
| Unknown stream length and fixed storage | A representative sample must remain valid as unseen records arrive. |
| Adaptive effort and stated error | Stopping according to observed values changes some uncertainty guarantees. |
| Reproducibility and independent repetitions | Reusing a seed repeats a calculation; it does not create another independent draw. |

### CMP.9:4 - Solution

**Name the target law or quantity → choose obtainable random operations → derive the output law or correction → account for variation and dependence → choose effort and stopping → return and revise the qualified result.**

#### CMP.9:4.1 - Separate the target, access and output

State whether the result is a random object, a subset, an expectation, an event probability, or another statistic. For sampling, specify the target probabilities, item identity, replacement rule and any order requirement. For estimation, define the quantity, such as `μ=E_p[f(X)]`, before designing how X will be obtained.

Describe access: an indexed collection, a one-pass stream, evaluable weights, a generative operation, or neighbors of a current state. An evaluable probability density does not necessarily provide a cheap sampler. An unnormalized density does not supply its normalization constant.

If the inputs describe observations, MMP.7 supplies the relevant recording and inclusion law. Sampling uniformly from recorded rows remains different from sampling uniformly from the people, events or other objects those rows describe.

#### CMP.9:4.2 - Construct the random operation and its output law

Start with a random primitive whose assumptions are explicit, such as independent uniform bits or uniform integers in a bounded range. A finite generator supplies a particular implementation. Its period, correlations, state reuse or exposure to an adversary matter when the receiving claim depends on them.

For a finite categorical law with known probabilities, a cumulative-probability partition can transform a uniform draw. When generating a uniform integer from b bits for a range of size m, simply taking the remainder can bias the result unless m divides `2^b`. One repair accepts only bit values below `floor(2^b/m)*m`, then takes their remainder; rejected draws are repeated. Choosing `2^b≥m` makes this an effective rejection construction with acceptance greater than one half.

For a stream, maintain a distributional invariant that survives one new record; :5.1 derives such an update. For a proposal distribution q different from p, either correct the output distribution through an acceptance rule or correct the estimated contribution through weights. Derive which of those results the procedure actually returns.

When direct draws are unavailable, a transition rule can maintain a desired stationary law. Construct the transition probabilities and the condition that preserves that law. Reachability, convergence from the start and correlations remain additional algorithmic questions; :5.3 shows why an uncorrected neighbor walk can target the wrong distribution.

#### CMP.9:4.3 - Derive the estimator and its error sources

For independent draws from p, the mean of `f(X_i)` estimates `E_p[f(X)]`. Its expectation equals the target when the expectation exists. With finite variance σ², the mean's variance is `σ²/n`.

For independent draws from q, use contributions `Y_i=f(X_i)*p(X_i)/q(X_i)` when the ratio is computable and q is positive wherever `f*p` contributes. Then `E_q[Y_i]=E_p[f]`. Inspect the second moment under q: a poor proposal can greatly increase variance. If an unknown normalizing constant leads to a self-normalized ratio of sums, its finite-sample bias and uncertainty require their own account.

For dependent draws, the variance of a mean includes covariance terms:

`Var(mean Y_i)=(sum_i Var(Y_i)+2*sum_(i<j) Cov(Y_i,Y_j))/n²`.

This identity does not require stationarity. A chain's approximate equilibrium, correlation and initial transient cannot be assessed just by counting iterations. Use an applicable mixing argument, a justified dependence-aware uncertainty method, or retain a weaker empirical conclusion.

Keep computational variation distinct from uncertainty in the target model. Sampling an assumed distribution accurately improves its computed consequences; it does not by itself validate that distribution for the subject.

#### CMP.9:4.4 - Choose sample effort and a compatible stopping rule

Select the error statement that changes the receiving decision. For independent identically distributed contributions bounded in `[a,b]`, Hoeffding's bound gives

`P(|mean Y_i-μ|≥e)≤2*exp(-2*n*e²/(b-a)²)`

at a fixed n chosen independently of their observed values. Thus `n≥(b-a)²*log(2/δ)/(2*e²)` suffices for error at most e with failure probability at most δ. The range and independence assumptions belong to this particular bound.

If results are inspected to choose the stopping time, use a compatible sequential bound. A simple conservative construction assigns `δ_n=δ/(n*(n+1))` and applies a fixed-n bound at each n with that failure budget. Since the budgets sum to δ, all resulting intervals cover simultaneously with probability at least `1-δ`. Stop when the current interval settles the question. More efficient confidence-sequence methods can replace this construction under their stated hypotheses.

Generating more draws is one possible improvement. A better proposal, stratification, fewer redundant transitions or an affordable deterministic calculation can improve the answer more per unit work. Include the cost of drawing, evaluating, weighting and retaining the results. Use C.11.DUA when deciding whether further computation is worthwhile; exploratory sampling need not acquire a formal interval unless the intended claim needs one.

#### CMP.9:4.5 - Return the useful result and identify what a change invalidates

Return the sample or estimate with the target and qualification its recipient needs. Distinguish samples without replacement, independent repeated draws, correlated states and weighted observations. A retained seed can support replay; uncertainty across repetitions needs genuinely distinct random streams under the assumed generator model.

Check a finite case by deriving or enumerating its output probabilities. A frequency experiment can expose an implementation error, but agreement on a small run does not establish a claimed law for every input.

A changed inclusion rule, target statistic, proposal, random source or stopping rule can invalidate a different part of the construction. Revise that part. Preserve already useful samples only with the correction and dependence account that their new use requires.

### CMP.9:5 - Archetypal Grounding

#### CMP.9:5.1 - Keep one uniform record from a stream of unknown length

Store the first record. At record t, replace the stored record with probability `1/t`; otherwise retain it. Use a uniform integer in 1 through t to make this decision.

After t records, the new record has probability `1/t`. Every earlier record had probability `1/(t-1)` before this step and survives with probability `(t-1)/t`, giving `1/t` as well. This establishes the invariant inductively. The procedure needs one record, a counter, and one update decision per arrival; counter and record representation costs remain visible.

For the stream A, A, B, the resulting value is A with probability 2/3 and B with probability 1/3. This is correct uniform sampling of record positions. If the new request is uniform sampling of distinct values, the old invariant answers a different question. One construction keeps a set of already seen values and applies the same update only on a first occurrence. That requires storage for the distinct-value set or another algorithm with its own access and error assumptions.

#### CMP.9:5.2 - Concentrate draws without changing an expectation

The target is the mean of values 0,0,0,4 under the uniform law on four identifiable outcomes, so μ=1. Direct draws have variance 3 per contribution.

Choose proposal probabilities `q=(1/8,1/8,1/8,5/8)`, concentrating effort on the nonzero contribution. The corrected value on outcome 4 is `4*(1/4)/(5/8)=8/5`; the other corrected values are zero. Its expectation is `(5/8)*(8/5)=1`, and its variance is `(5/8)*(8/5)²-1=3/5`. At the same number of independent draws, this construction reduces variance by a factor of five; the proposal and weighting cost decide the actual work benefit.

Using the unweighted sample mean instead has expectation `(5/8)*4=5/2`, the wrong target. Increasing the sample count would concentrate that wrong answer. If the required statistic changes to a different function on the four outcomes, retain the proposal only after recomputing its support, corrections and variation for that function.

#### CMP.9:5.3 - Correct a local walk before using it as a sampler

Sample uniformly from three states connected in a path, `0—1—2`. A walk that chooses an adjacent state uniformly spends stationary probabilities `(1/4,1/2,1/4)`: the middle state has twice as many incident choices. Uniform selection among neighbors does not imply uniform selection among visited states.

Correct a proposed move x to y by accepting it with probability

`min(1, π(y)*q(x|y)/(π(x)*q(y|x)))`,

where π is the target and q the proposal probability. A rejection retains x. For positive target weights on connected states, the probability flow on either direction of an edge becomes the same minimum of the two proposed flows, so detailed balance holds. Normalizing constants cancel in the ratio.

For this uniform target, accept an end-to-middle move with probability 1/2 and a middle-to-end move with probability 1. The transition matrix, in state order 0,1,2, is

```text
1/2  1/2   0
1/2   0   1/2
 0   1/2  1/2
```

Its rows and columns each sum to one, so the uniform law is stationary. The finite chain is connected and has self-transitions, hence converges from any start. Its other eigenvalues are 1/2 and -1/2; for this small matrix, powers give an explicit decreasing transient. For instance, starting at 0 gives `(1/2,1/2,0)` after one step and `(1/2,1/4,1/4)` after two, still not uniform.

If the three target weights change to `(1,2,1)`, the original uncorrected neighbor walk has that stationary law. Reusing the former uniform-target acceptance probabilities would now be wrong. In either case, adjacent states are dependent observations; an independent-draw variance formula cannot be justified by the stationary law alone.

### CMP.9:6 - Bias-Annotation

A large sample count is an easy proxy for quality. The examples instead inspect the sampling unit, correction and transition law. Their small size permits direct derivation; a large state space may require stronger analysis or a more limited conclusion.

Randomness here is an algorithmic resource. Whether a physical source or pseudorandom generator adequately supplies it depends on the particular claim and environment, including adversarial use.

### CMP.9:7 - Conformance Checklist

- The target law or statistic, sampling unit and available access are explicit.
- Random primitives and the transformation, invariant or transition law determine the stated output.
- An estimator includes the needed correction and support condition.
- Bias, variance, dependence and target-model uncertainty are distinguished where they affect use.
- Sample effort and stopping support the error claim actually made.
- A changed target or sampling condition has a local consequence for the procedure and its qualification.

### CMP.9:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Sample a convenient law and average without correction | The estimate converges to another quantity. | Derive the weighting or acceptance operation. |
| Call repeated rows independent draws | Shared randomness or chain state can preserve dependence. | Model their joint generation and its error consequence. |
| Assume stationary means already equilibrated | The initial transient can remain large. | Establish sufficient mixing or qualify the finite result. |
| Inspect a fixed-n interval until it looks decisive | Its original coverage need not survive optional stopping. | Fix the sample size or use a compatible sequential bound. |
| Replace uniform records by uniform entities silently | Multiplicity changes inclusion probabilities. | Change the sampling unit and its obtaining algorithm. |

### CMP.9:9 - Consequences

An expensive enumeration can be replaced by a controlled random computation, and a sample can be maintained despite limited access or storage. The same derivation exposes a wrong target before more computation reinforces it.

A valid construction can still be inefficient. Support, weight variability, mixing and evaluation cost identify different routes to improvement; they do not all yield to a larger sample count.

### CMP.9:10 - Architectural Rationale

Sampling and estimation share the construction of an output law but return different things. An estimator can correct biased sampling without turning the retained draws into unweighted samples from the target. A transition can preserve a distribution without supplying independent draws. Keeping these results distinct makes their composition with learning, search and modeling reliable.

The general method derives probability statements from effective operations. Probability modeling supplies a target where needed; algorithmics supplies how to obtain, transform and use finite draws under resource limits.

### CMP.9:11 - SoTA-Echoing

How can a stream yield a uniform sample without knowing its length? **Adopt** the invariant-based construction in [Vitter, *Random Sampling with a Reservoir*, §2](https://www.cs.umd.edu/~samir/498/vitter.pdf), specialized to one stored record in :5.1. A two-pass method is simpler when counting and revisiting the input are cheap; reservoir updating removes that access requirement. Vitter also derives skip-based alternatives, so a per-record random decision is not asserted to be the fastest realization. Changed access costs, weighted sampling or a distinct-entity target reopen the choice.

When useful events are poorly represented by direct draws, **adopt** [Owen's importance-sampling construction, §§9.1–9.3](https://artowen.su.domains/mc/Ch-var-is.pdf), in :4.3 and :5.2: correct the contribution and compare variation together with drawing and weighting cost. Direct sampling remains preferable when a proposed correction costs more than the information it gains or produces unstable weights. A changed integrand, support, normalization or proposal can reverse the selection. The construction does not certify an empirical probability model.

For local state exploration, **adopt** the separation of stationary-law construction and mixing developed in [Levin and Peres, *Markov Chains and Mixing Times*, second edition, chapters 3–4](https://pages.uoregon.edu/dlevin/MARKOV/). Sections :4.2–4.3 and :5.3 retain that distinction instead of treating every random walk as a suitable sampler. Direct draws avoid a transient when available at comparable cost; local transitions are useful when direct generation is expensive and their finite-time behavior is adequate. A changed target, proposal, connectivity or mixing bound reopens that comparison.

When the stopping time follows the observations, **adapt** [Howard, Ramdas, McAuliffe and Sekhon's confidence-sequence framework](https://arxiv.org/abs/1810.08240) in :4.4. A fixed-n bound remains the lighter choice for a fixed-n claim; a simultaneous bound pays extra interval width to retain the claim under repeated inspection. The elementary failure-budget construction gives one transparent implementation, while the paper supplies sharper alternatives under explicit assumptions. Changed dependence, contribution bounds or stopping use requires a new compatible comparison.

### CMP.9:12 - Relations

- **MMP.7:** constructs the law of recorded data when the sampling target comes from observations.
- **C.29.2:** supplies the computational result, access and resource conditions; **MATH.20** supplies bounds used in the probability argument.
- **CMP.7:** uses generated examples or estimated feedback in a learning procedure; **CMP.6** uses stochastic feedback in an update.
- **CMP.3:** supplies storage and recomputation choices; shared draws must retain their dependence when reused.
- **C.29.3:** connects a computational procedure to its physical realization.
- **C.11.DUA:** chooses worthwhile additional sampling or a conditional result at the available effort.

### CMP.9:End
