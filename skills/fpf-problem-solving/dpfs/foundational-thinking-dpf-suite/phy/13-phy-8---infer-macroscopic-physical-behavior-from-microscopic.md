## PHY.8 - Infer Macroscopic Physical Behavior from Microscopic Alternatives

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### PHY.8:1 - Problem frame

Use this pattern when you need to explain or predict collective physical behavior from possible microscopic states or histories. The difficulty is deciding which alternatives matter, why they receive particular weights, and whether their aggregate represents the observation you need. Many constituents can produce a stable average, persistent fluctuations or a response that depends on preparation.

The first result is a collective prediction with its physical grounds: a distribution of an observable, its mean and relevant fluctuations, or an evolution law at the required scale. If different plausible preparations give different answers, retain that difference and identify what would settle it.

Here *microscopic* and *macroscopic* refer to levels of physical description. A microscopic description retains distinctions that the selected collective observable combines. The method can apply to a small system's aggregate as well as a large population; the approximation of a stable macroscopic value requires its own grounds.

You need to interpret the physical preparation and interactions, and to understand the probability operations used in the calculation. Quantum cases require the corresponding state and measurement rules. A collaborator can supply those mathematical operations while you retain the question and physical interpretation. The worked cases state their additional branch-specific premises.

Use a direct balance or an established effective law when it already gives the needed consequence with adequate conditions. Construct the microscopic account when fluctuations, changed preparation or a proposed mechanism can alter that consequence. PHY.5 helps choose which detail to retain.

### PHY.8:2 - Problem

A correct average can answer the wrong physical question. A detector saturates on individual excursions, not on the ensemble mean. A system prepared in one part of its state space need not explore all alternatives during the observation. Separate constituents can share a preparation that makes their fluctuations add together.

The weighting is also a physical choice. Counting possible states does not by itself make them equally probable. Fitting a distribution to a signal does not establish the microscopic mechanism that produces it. A numerical sequence can sample the desired distribution without representing the time evolution of the system.

The task is to carry physical preparation and interaction through the statistical construction to the consequence that will be used.

### PHY.8:3 - Forces

| Force | Tension |
| --- | --- |
| Microscopic detail and useful aggregate | A detailed account can explain a changed response, while an unchanged total may need only a balance. |
| State counting and preparation | Many alternatives are possible, but the preparation and dynamics can weight them differently. |
| Typical behavior and rare outcomes | A narrow central range can support ordinary operation while missing a consequential excursion. |
| Individual properties and collective dependence | Local statistics can be unchanged while correlations alter the whole. |
| Long-time theory and available time | A limiting result may be valid yet unavailable within the observation interval. |
| Sampling economy and physical meaning | An efficient sampler can obtain a statistic without reproducing physical motion. |

### PHY.8:4 - Solution

**Choose the collective consequence → construct the microscopic alternatives and their weights → derive the observable statistics → test the relevant fluctuations and times → revise the implicated physical premise.**

#### PHY.8:4.1 - Specify the observable and how it will be used

Name the physical quantity, spatial extent and observation interval. Decide whether the work needs a value at one time, a time average, a response after an intervention or the chance of crossing a threshold. These uses can require different statistics from the same system.

Relate the observable to the retained microscopic description. In a classical account, write it as a function of the state, or of a history when the measurement integrates over time. Include a measurement response when it changes the answer. MMP.7 constructs the probability law of the recorded outcome from a subject law and a recording procedure.

Separate physical variation from uncertainty about a fixed parameter. A rate that changes among preparations, an unknown common rate and a fresh independent rate for each constituent describe different arrangements. Keep a fixed unknown parameter explicit unless a probability law over it is warranted for the intended inference.

#### PHY.8:4.2 - Construct admissible alternatives and their weighting grounds

Choose the microscopic variables and their physical constraints. Use the theory and preparation to determine possible states, conserved quantities, accessible transitions and coupling to the surroundings. Preserve collective restrictions: fixing total energy or particle number can couple otherwise separate constituents.

Then say what supports the weights. A controlled preparation can supply frequencies; an admitted dynamical law can transport an initial distribution; an equilibrium argument can supply a statistical ensemble under its physical assumptions. An ensemble is a statistical description of possible preparations or states, not an additional physical population that must exist.

For an equilibrium construction, identify what the surroundings hold fixed and what can be exchanged. If a weakly coupled subsystem exchanges energy with a large equilibrated reservoir, a canonical distribution may be appropriate. If the total energy is fixed, begin with that restriction instead. Retain state multiplicities: several distinct states with one energy contribute separately. Check equivalence of proposed ensembles for the observable and regime being used before substituting one for another.

A maximum-entropy inference selects a distribution relative to specified alternatives, a reference measure and constraints. It can provide a useful conditional prediction. Its inferential grounds remain distinct from an argument that this preparation physically equilibrates to that distribution.

For a quantum account, use the prepared state and the relevant observable or measurement operators. A density operator can represent a subsystem correlated with its environment. Its decomposition into weighted pure states need not identify a unique physical preparation. Compute the probabilities of the chosen measurement using the theory; do not replace the state by presumed simultaneous values for incompatible measurements.

If the grounds leave several weightings possible, carry their different consequences far enough to see whether the unresolved choice matters. A bound or a common consequence can already answer the work question.

#### PHY.8:4.3 - Derive the collective law without discarding dependence

Obtain the observable's distribution by combining the admissible alternatives with their weights. For a classical state X with probability law P and an observable Y=g(X), the probability of a set B of outcomes is

`P(Y in B) = integral 1[g(x) in B] P(dx)`.

The symbol 1 is one when its bracketed condition holds and zero otherwise. Use a weighted sum for a discrete state set. A non-ideal recording procedure adds its conditional response through MMP.7.

For a quantum state rho and an ideal measurement of observable A, outcome probabilities follow from the corresponding measurement projectors. When the second moment is finite, the mean is `Tr(rho A)` and the variance is `Tr(rho A²) - Tr(rho A)²`. Here Tr denotes the trace, and A represents the physical observable under the selected measurement. When the required moments are not finite, use the outcome distribution or a relevant bounded event instead of these finite-moment summaries. Other measurement arrangements require their own operators and response.

Retain correlations while forming collective quantities. For a finite collection of jointly defined classical outcomes X_i with finite second moments,

`E[sum_i X_i] = sum_i E[X_i]`,

`Var(sum_i X_i) = sum_i Var(X_i) + 2 sum_(i<j) Cov(X_i,X_j)`.

Linearity of the mean needs no independence assumption. The variance equals the sum of individual variances when the total covariance contribution, `2 sum_(i<j) Cov(X_i,X_j)`, is zero. Pairwise zero covariance is sufficient, and independence is a stronger sufficient condition. Retain the dependence supplied by the physical arrangement.

A mean may be all that the question needs. When excursions matter, derive a relevant variance, tail probability or bound. Preserve units and the normalization used for comparison: the variance of a total and that of a per-constituent average differ by the square of the constituent count.

#### PHY.8:4.4 - Establish when the aggregate represents a typical observation

Compare the predicted spread with the tolerance or decision in the work. For any scalar observable Y with finite variance and positive tolerance epsilon, Chebyshev's inequality gives

`P(|Y-E[Y]| >= epsilon) <= Var(Y)/epsilon²`.

This can settle a sufficient bound without reconstructing the whole distribution. If the bound is too loose to decide, a sharper calculation may help. Its cost is justified by the unresolved decision, not by the mere availability of another statistical method.

For an average over N constituents, the variance is bounded by a constant times 1/N when the sum of relevant covariances is bounded above by a constant times N. A common fluctuating influence can instead make the total variance grow as N². Inspect the physical dependence that determines this scaling. Increasing the number of constituents then has different effects on reliability.

Keep a probability claim relative to its measure. A set containing most of the probability need not contain most of the unweighted alternatives. Conversely, a large count of states says little about the prepared distribution until its weights are supplied.

Decide whether a finite system and the requested observable permit the limiting argument. Correlation lengths comparable to system size, constraints, long-range interactions or operation near a transition can invalidate the approximation used to obtain concentration. Return to the physical account when that invalidation changes the required result; do not require a thermodynamic limit for an already sufficient finite calculation.

#### PHY.8:4.5 - Connect ensemble behavior to physical time

An ensemble mean at time t and a time average along one history answer different questions. To use the latter as an estimate of the former, examine the relevant dynamics, preparation and observation duration.

Derive or obtain a relaxation or correlation time for the selected observable. Compare it with the duration available and with any external drive. A stationary distribution can exist while equilibration is too slow for the experiment. An invariant portion of state space can preserve dependence on the initial preparation. A theorem about an infinite-time average supplies no finite settling time by itself.

For a stationary scalar process A(t) with covariance C(tau)=Cov(A(t),A(t+tau)), the variance of its average over duration T is

`Var(A_bar_T) = (2/T²) integral from 0 to T of (T-tau) C(tau) d tau`.

This relation assumes finite second moments and a well-defined time integral. Use it, or a suitable finite-sample counterpart, when the accuracy of time averaging matters. Long correlations reduce the gain from repeated measurements; drawing more points from the same slow fluctuation does not make them independent.

If an eliminated variable leaves memory in the retained evolution, keep that memory or restore a sufficient state through PHY.5 and MMP.9. Decide which description serves the time-dependent question. A stationary histogram alone does not establish the transition law, response time or heat dissipation.

#### PHY.8:4.6 - Compute, compare and return to the physical premise

Use a finite enumeration, analytical calculation or numerical sampler appropriate to the selected statistic. C.29.2 helps formulate the computation. Check that the computation implements the chosen state space, preparation, dependence and observable.

A Monte Carlo sampler can deliberately use artificial transitions to obtain a distribution. Interpret its steps as physical time only when a separate physical transition law and time calibration justify that use. Convergence of a numerical estimate, statistical concentration of the physical observable and adequacy of the microscopic account are different questions.

Make the comparison that can change the work decision. A small case can reveal a lost correlation. An available observation can distinguish two preparations. A changed observation interval can expose an invalid equilibrium approximation. Retain a sufficient conditional answer when further evidence would not justify its cost; C.11.DUA governs that choice.

Return to the implicated premise: the prepared state, weighting, interaction, measurement response or time-scale assumption. Preserve unaffected balances and mathematical consequences. The next question may concern controlling fluctuations, constructing a different preparation or choosing a more informative observable.

### PHY.8:5 - Archetypal Grounding

#### PHY.8:5.1 - Predict an excited population from a reservoir argument

A device contains N=400 distinguishable, weakly interacting units. Each has a nondegenerate ground state of energy 0 and a nondegenerate excited state of energy Delta. The units have equilibrated with a large reservoir at temperature T. Treat interactions between units and their contribution to the reservoir's temperature change as negligible. An ideal readout counts excited units before appreciable relaxation changes that count.

The physical question is the mean count and its variation between independently repeated equilibrium preparations. The reservoir argument weights a unit's state by the number of compatible reservoir states. With reservoir entropy S_R and Boltzmann constant k_B,

`Omega_R(E-Delta)/Omega_R(E) approximately exp(-Delta/(k_B T))`,

using the first-order entropy change and `dS_R/dE=1/T`. This approximation needs the reservoir's temperature to remain effectively constant over the exchanged energies. The equal weighting used for the combined equilibrium energy shell is a premise of this construction.

Choose `Delta=k_B T ln(3)`. The excited-to-ground weight ratio is 1/3, so the excited probability is p=1/4, not 1/2. Two possible energy values do not receive equal weights under this preparation.

Under the stated independence approximation, the count K is binomial:

`P(K=k) = choose(400,k) (1/4)^k (3/4)^(400-k)`.

It has mean 100 and variance 75, giving a standard deviation about 8.66 units. If the receiving requirement is that the count differs from 100 by less than 50 in at least 96% of preparations, Chebyshev gives `P(|K-100|>=50)<=75/2500=0.03`. That bound already satisfies the requirement; calculating every binomial probability is unnecessary for this decision.

Now suppose the excited energy has three distinguishable states at the same Delta, with the same equilibrium and independence premises. Their total weight is three times larger. The excited probability becomes 1/2, the mean count 200 and the variance 100. The energy gap alone no longer supplies the previous count.

If the device is instead prepared with precisely 100 excited units and isolated during readout, the count variance is zero. Individual units can still each have excited probability 1/4 across a permutation-symmetric preparation. The fixed-total restriction prevents the binomial independence assumption. Use the preparation that the work actually supplies.

#### PHY.8:5.2 - Recover collective fluctuations from a prepared joint state

A readout measures the z component of N=100 spin-1/2 systems along one common axis. Write each normalized outcome as s_i=+1 or -1; the physical angular momentum is `(hbar/2) s_i`. The collective normalized signal is `M=sum_i s_i`.

Three ideal preparations give every individual spin equal probabilities of +1 and -1:

| Preparation during readout | Joint property used | Mean M | Variance of M |
| --- | --- | --- | --- |
| Independently prepared maximally mixed spins | Outcomes along the common axis are independent | 0 | 100 |
| Fifty independent singlet pairs | The two outcomes in every pair are opposite | 0 | 0 |
| With equal probabilities, all spins prepared up or all prepared down | Every outcome shares the same prepared sign | 0 | 10000 |

For a singlet pair, the state is `(|up down>-|down up>)/sqrt(2)`. Its ideal common-axis measurements give opposite results, so each pair contributes zero to M. For the last preparation, M itself is +100 or -100 with equal probabilities. The variance entries follow from these joint properties and from addition of independent variances in the first preparation.

A readout designed only from the individual mean would predict the same zero signal in all three cases. Their root-mean-square collective signals are 10, 0 and 100. If saturation occurs when |M| exceeds 50, the last preparation always saturates. The first has probability at most `100/50²=0.04` by the variance bound, and the ideal paired preparation never saturates.

Now retain the paired preparation but read only one spin from each pair. The sum of those fifty outcomes has variance 50, because different pairs were prepared independently. The zero-variance conclusion applied to a complete-pair sum, not to an arbitrary selected subset.

This calculation uses joint states and a stated measurement. Common-axis anticorrelation alone would also be compatible with other preparations; it does not identify the singlet uniquely. Recovering entanglement would require a different question and suitable measurements. Detector errors or correlations between pairs would change the recording law or the preparation premise.

#### PHY.8:5.3 - Derive transport from persistent microscopic motion

Particles move on an unbounded line with speed v>0. Each reverses direction at independent Poisson events of rate alpha>0. Initially each particle is at the origin, with either direction equally likely. This is a physical stochastic model for the motion; its validity must come from the selected mechanism and regime.

Let p_+(x,t) and p_-(x,t) describe position probabilities with positive and negative velocity. The point preparation leaves probability atoms at the unreversed fronts x=+vt and x=-vt; interpret the following density equations in the distributional sense. The transition and transport laws give

`partial_t p_+ = -v partial_x p_+ - alpha p_+ + alpha p_-`,

`partial_t p_- = v partial_x p_- + alpha p_+ - alpha p_-`.

Define total density n=p_++p_- and probability current j=v(p_+-p_-). Adding and subtracting give

`partial_t n = -partial_x j`,

`partial_t j = -v² partial_x n - 2 alpha j`.

The current retains the directional persistence. Eliminating it gives

`partial_tt n + 2 alpha partial_t n = v² partial_xx n`.

For times long compared with `1/(2 alpha)` and spatial variation slow enough for the current to relax, use `j approximately -D partial_x n`, with `D=v²/(2 alpha)`. The resulting diffusion equation is an approximation with physical grounds, not a consequence of fitting a bell-shaped histogram.

The mean position stays zero. For the stated initial preparation, the mean-square displacement is

`E[x(t)²] = (v²/alpha) [t - (1-exp(-2 alpha t))/(2 alpha)]`.

With v=2 cm/s and alpha=1/s, it is about 0.03746 cm² at t=0.1 s. A diffusion calculation would give 0.4 cm², more than ten times as much. At t=20 s, the values are about 78 and 80 cm²: diffusion overestimates this observable by about 2.56% relative to the microscopic model. A 3% tolerance admits the later approximation but not the earlier one.

Changing the requested time therefore changes the needed description. Retain the density-current equations for the early response; use the diffusion reduction when its error is adequate for the requested observable. Boundary arrival probabilities would need their own comparison, since this mean-square agreement does not validate every feature of the distribution.

A simulation that flips velocity with the specified rate implements physical time. A different Markov chain designed to sample a position distribution has no such interpretation merely because its histogram agrees.

### PHY.8:6 - Bias-Annotation

The examples emphasize finite statistics and tractable microscopic laws. Collective behavior can involve phase transitions, long-range coupling, non-equilibrium drive and quantum observables that require more specialized calculations. The reusable move is to connect preparation, weighting, dependence and the used observable; the simple example distributions are not defaults for those cases.

A macroscopic discrepancy can also arise from the recording procedure. Return through MMP.7 when the detector's selection, integration or disturbance changes what is observed.

### PHY.8:7 - Conformance Checklist

- The requested observable, preparation and observation interval are recoverable.
- The microscopic alternatives and their weights have stated physical or inferential grounds.
- Collective constraints and relevant correlations survive the aggregation.
- The statistic answers the intended use, including a fluctuation or tail question when one matters.
- A concentration or equilibration argument has conditions appropriate to the finite system and observation.
- Computational transitions are interpreted as physical time only with a supporting physical law.
- A changed result returns to the implicated premise, while a sufficient conditional answer can remain in use.

### PHY.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Equal weights from a count of alternatives | Two energy values are treated as equally likely despite a biased preparation. | Construct the weights from the reservoir, preparation or other applicable grounds. |
| Independence from separate constituents | A common preparation or fixed total disappears from the joint account. | Form the collective law before discarding dependence. |
| Mean as a prediction of every run | An excursion-sensitive device is assessed only at the mean signal. | Compute the fluctuation or threshold consequence needed for that device. |
| Equilibrium without an available settling interval | A stationary distribution replaces the prepared transient. | Compare the relevant relaxation with the observation time. |
| Sampler steps as elapsed time | Artificial moves become a claimed physical transition law. | Separate distribution sampling from a physically calibrated evolution. |
| One successful statistic validates the whole reduction | Mean-square agreement is used to justify a boundary-arrival probability. | Compare the observable that the changed question actually consumes. |

### PHY.8:9 - Consequences

A collective prediction becomes revisable through its physical premises. A team can assign construction of the preparation and microscopic law, probability calculation, numerical estimation and interpretation to different contributors while retaining what each result assumes.

The work can avoid both unnecessary microscopic simulation and an unjustified average. A bound can finish the present decision; a correlation or finite-time effect can instead open a different preparation, observation or physical account.

### PHY.8:10 - Architectural Rationale

The physical choice of alternatives and weights comes before their mathematical aggregation. This preserves the distinction between a distribution that fits records and a mechanism-based account that can predict a changed preparation. MMP.7 supplies the observation-law construction; this pattern supplies the physical grounds that construction needs.

Fluctuations and physical time remain alongside the mean because they can change the use without changing individual statistics. Keeping those relations explicit makes the method transferable from populations and transport to sensing and physical computation.

PHY.5 decides which physical detail can be omitted. Here a statistical consequence can show that an omitted correlation or memory matters, and return that problem to the effective-description method. A complete microscopic theory is unnecessary when a physically justified restricted account already settles the question.

### PHY.8:11 - SoTA-Echoing

[Baldovin, Gradenigo, Vulpiani and Zanghì, *On the foundations of statistical mechanics*](https://arxiv.org/abs/2411.08709), Physics Reports 1132 (2025), provides a current synthesis of equilibrium foundations. Sections 3.4-3.5 distinguish selected macroscopic observables and useful sampling from unrestricted dynamical claims; sections 5.1.3-5.1.5 connect quantum states, reduced states and equilibrium weighting. The method uses these distinctions without making one universal equilibration argument a prerequisite.

Compare the excited-count question in :5.1. A physically appropriate equilibrium ensemble gives the same count law that sufficiently repeated microscopic simulation would estimate, with less trajectory computation. Simulation is useful when interactions or preparation invalidate the simple ensemble calculation. A maximum-entropy inference from supplied constraints is another usable route when those are the available grounds; it does not alone establish a relaxation time or response to changed coupling. The different questions determine which contribution is needed.

[Corominas-Murtra, Hanel and Jizba, *Typicality, entropy and the generalization of statistical mechanics*](https://arxiv.org/abs/2409.06537) examines extensions of typicality beyond the usual independent-constituent setting. Its distinction between probability concentration and unweighted state counts supports :4.4. The present worked calculations use ordinary finite probabilities; generalized entropy is not required for their decisions. Reopen the concentration argument when the changing alternatives or dependencies defeat its current assumptions.

[Korbel and colleagues, *Quo vadis, stochastic thermodynamics?*](https://arxiv.org/abs/2604.26601), 2026, examines hidden variables, memory and limits of thermodynamic interpretation. Sections II and V matter here: a reduced stochastic description may retain memory, and observable irreversibility does not automatically determine physical dissipation. Use a physical energetic account for a heat claim. For the transport question in :5.3, the density-current account and its diffusion reduction answer the same late-time mean-square question; the current adds useful content when the early response is required. A larger microscopic simulation would cost more without improving this already solvable comparison.

The examples are constructions of the method. More demanding equilibrium, quantum or driven-system questions can require specialized physical and mathematical results. Their use retains the preparation, observable and time conditions that make the result transferable.

### PHY.8:12 - Relations

- **PHY.5:** chooses an effective physical description and restores an omitted coupling, state or memory when its consequence matters.
- **PHY.6 and C.29.BB:** construct the balance and response relations retained in collective evolution.
- **MMP.7:** composes the physical subject law with the recording procedure and derives the law of the recorded data.
- **MMP.9:** derives a reduced evolution from a more detailed mathematical account under stated assumptions.
- **B.5.MPC** connects the mathematical consequence to the physical question; **C.29.2** formulates any needed computation.
- **C.16.MR:** identifies the measurement relation whose physical and statistical realization is being used.
- **B.5.MPC.R:** repairs the implicated physical, mathematical or computational contribution and its affected uses.
- **C.11.DUA:** chooses whether resolving an uncertainty warrants further work or a sufficient conditional result should be used.

### PHY.8:End
