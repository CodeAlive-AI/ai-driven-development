## PHY.5 - Choose an Effective Physical Description by Scales and Couplings

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### PHY.5:1 - Problem frame

Use this pattern when a physical question leaves you uncertain which motions, interactions or material details its description must retain. Resolving every microscopic change may be impractical. Omitting a fast motion or a small interaction may change the answer that matters.

Begin with one consequence: a response over a stated interval, a propagation speed, an accumulated exchange, or a distribution of outcomes. Choose one proposed omission and follow how it could affect that consequence. A simpler account with a justified range of use, or a reason to restore the omitted contribution, is a useful first result.

An *effective physical description* here describes the physical behavior needed at chosen scales without resolving every underlying process. Unresolved processes can still contribute through response coefficients, constraints, dependence on earlier states or fluctuations. The method helps choose and examine that description across physical branches.

You need to identify the physical participants, explain the interactions relevant to the question and compare their characteristic sizes or rates. A qualitative separation can direct the next construction. The examples add their own mathematical preparation: elementary differential equations for the motor, waves for the discrete chain, and covariance for thermal motion.

When a known physical account already answers the question under the intended conditions, use it. PHY.1 supplies similarity between changed arrangements; PHY.2 constructs an analogue from physical interactions. MMP.9 supplies mathematical reduction once the governing relations and retained quantities have been chosen. Use this pattern for the physical choice of those quantities, relations and conditions.

### PHY.5:2 - Problem

A detailed account can obscure the mechanism that determines a response. A convenient coarse account can erase the same mechanism. The relevant distinction depends on the question: a description may preserve a mean displacement while losing its spread, or preserve slow motion while losing an initial torque.

A comparison of isolated time scales also misses how parts interact. A rapidly adjusting part can exert a sustained force. Unresolved molecular motion can produce both drag and continuing fluctuations. A small length can become consequential when the imposed variation approaches that length.

The task is to retain the physical influence required by the intended result, while choosing how much of its underlying process to describe.

### PHY.5:3 - Forces

| Force | Tension |
| --- | --- |
| Resolution and usable explanation | More resolved variables can expose a mechanism while making the relevant consequence harder to obtain. |
| Scale separation and coupling | A fast process can relax quickly yet continue to alter the slow behavior through its response. |
| Mean response and variability | An average can settle one question while missing fluctuations that determine another. |
| Local approximation and changed conditions | A useful omission can fail at a boundary, during preparation or after the work changes the forcing. |
| Available grounds and further inquiry | Existing laws and bounds may settle the choice; an unresolved physical premise can sometimes justify a targeted comparison. |

### PHY.5:4 - Solution

**Choose the consequence → locate its physical influences → compare their scales in the coupled situation → retain the needed effects of unresolved processes → test the resulting answer → use it or restore the consequential difference.**

#### PHY.5:4.1 - Choose the physical consequence and its resolution

State what the answer will let someone interpret, choose or do. Identify the relevant quantity and how it is used: an instantaneous value, a time integral, a spatial average, a peak, a correlation or a probability can require different descriptions of the same situation.

Include the preparation, forcing, spatial range and observation interval when they affect that answer. For example, the first moment after switching can include a motion that has already decayed when a later reading is taken. A question about a wave's arrival concerns a propagating disturbance and the wavelengths present in it.

Use the working question to choose adequate resolution. If a bound already determines the choice, recovering a detailed trajectory may add nothing to that choice. C.11.DUA helps when the value of further inquiry is uncertain. B.5.MPC connects the mathematical result and its conditions to the physical question.

#### PHY.5:4.2 - Locate the interactions and compare their scales

Follow the influence from preparation or input to the consequence. Identify what stores, transports, exchanges or dissipates the quantities involved. Include a boundary, contact, surrounding medium or measuring interaction when it carries an influence on that consequence.

Obtain the governing physical relations at the detail needed for this comparison. A studied theory, measured response or working hypothesis can supply them; retain which of these is being used. PHY.4 helps constrain an unresolved law. MMP.11 constructs its remaining mathematical family.

Derive characteristic sizes or rates from these relations and the proposed regime. Compare contributions to the same physical change. For time scales, compare relaxation with the fastest relevant forcing and with the interval of use. For spatial scales, compare a variation length with the scale of material structure or transport. An energy comparison may determine which states can be appreciably excited.

Inspect the coupled arrangement. A coupling can change a relaxation rate or create a collective mode. For a proposed rapidly adjusting state, ask whether small departures from its proposed response actually decay while the retained variables change. A response near loss of stability can become slow even though one component, considered alone, relaxes rapidly.

Scaling the equations as in PHY.1 makes these comparisons explicit. Keep the physical reason for each scale: a narrow gap, driving period or relaxation distance can matter more than the size of the whole apparatus.

#### PHY.5:4.3 - Choose how unresolved processes enter the retained account

Select the variables and interactions needed by the consequence. They may describe individual participants or collective quantities such as a displacement field, concentration or slowly changing amplitude.

For a part that adjusts rapidly, first determine what it adjusts *to*. Substitute that response into its coupling with the retained part. The resulting force, constraint or transport remains in the effective account. In the motor example, eliminating rapidly changing current retains its effect on torque and damping.

For a collection of unresolved processes, determine which of their effects remain:

- a mean response changes the retained forces or transport coefficients;
- a delayed response makes current change depend on earlier states;
- fluctuations produce a spread of possible changes around a mean response;
- a persistent unresolved mode may require another retained state.

Choose among these from the physical preparation and interactions. Eliminating variables mathematically can expose a memory term even in deterministic dynamics. A statistical description additionally needs grounds for the distribution of unresolved states. MMP.7 supplies probability composition for a specified information and recording situation; it does not choose the physical preparation.

An effective coefficient can be obtained from a more detailed description, existing measurements or a constrained response law. Compare the predicted quantity in a regime where the two descriptions apply and choose the coefficient to preserve that contribution. This matching can be useful even when no complete microscopic theory is available. Carry the range and remaining uncertainty that change its later use.

#### PHY.5:4.4 - Construct the approximation and its first omitted contribution

Use MMP.9 for the mathematical elimination or retained-state evolution. Keep the physical assumptions that permit the construction alongside its result.

For a rapidly relaxing state, examine its initial departure and response to changing inputs. Replacing it by a steady response is useful when the remaining departure has sufficiently little effect on the requested consequence. The motor calculation below derives that departure instead of assigning it zero at the initial instant.

For a spatial or energy expansion, choose the ratio in which the description is expanded and compare the first omitted contribution with the retained ones. The ratio and its powers come from the physical relations. In the chain example, expansion in the small ratio of lattice spacing a to wavelength lambda, or equivalently in `q*a=2*pi*a/lambda`, yields a continuum wave description and its leading correction.

When unresolved correlations persist over the interval of interest, retain their delayed influence or add variables that reproduce it. Replacing a delayed response by an instantaneous one needs a comparison of that response time with the retained motion and driving. A mathematically equivalent auxiliary state is another way to calculate the memory; its interpretation as a material component requires a separate physical account.

Maintain the relevant exchanges and constraints through the approximation. Recover the condition for a balance or an allowed motion when changing the variables or boundaries. C.29.BB supplies the common balance construction.

#### PHY.5:4.5 - Judge the influence on the requested answer

Follow the approximation through to the actual output. A small state error can grow under differentiation, accumulation, feedback or a sensitive later choice. MATH.20 supplies bounds. If the consequence is obtained in another mathematical account, C.29.1 establishes what transfers between the accounts.

Examine conditions suggested by the construction itself. An omitted initial transient matters when the reading moves into it. A spatial approximation becomes suspect when the wavelength approaches the unresolved structure. A weak loss can determine a resonant response. A nearly unstable mode can defeat the earlier time-scale separation. Use the conditions that affect the proposed account.

For a statistical description, compare the statistic the work uses. Preserving an average response need not preserve a variance or a transition probability. In thermal motion, eliminating velocity while retaining random forcing can preserve long-time displacement statistics. Deleting that forcing gives a different result.

A derivation, an existing limiting result or a suitable comparison can settle the choice. If a physical premise remains unresolved, identify a feasible change of preparation or readout for which the plausible accounts give different useful answers. Obtain that comparison when its possible outcomes warrant the effort. A conditional physical conclusion can remain useful while a stronger claim is unresolved.

#### PHY.5:4.6 - Use the account and reopen the affected physical choice

Return the answer with the conditions needed to use it. These may be expressed in a short derivation, an annotated model or an ordinary explanation.

Choose what the work now permits: use the simpler computation, interpret a measurement, change a drive, retain a fluctuation model, or restore an interaction. If several accounts provide complementary consequences, retain their respective uses. When a choice among available descriptions matters, C.11 supplies the comparison, including whether more inquiry is worth its cost. Use G.5 when the retained set itself must be stated: distinguish alternatives for later choice from descriptions used together for a named result. E.23 supports improvement when the chosen characteristics can judge a change.

For a new question or failed prediction, return to the influence whose omission is implicated. Change the physical variables, coupling, preparation or range, then redo the affected reduction and interpretation. B.5.MPC.R helps separate a physical-account failure from a mathematical or computational one.

The result can also change the method of work. A team may calculate a slow response with one model and delegate a short transient to another. B.1.5.CM describes those contributions and their joins; A.3.1.CC examines the claims needed for the combination. Each result retains the physical conditions that make it usable by the next participant.

### PHY.5:5 - Archetypal Grounding

#### PHY.5:5.1 - Keep a motor's torque while eliminating fast current dynamics

Consider an ideal linear motor over a range in which resistance R, inductance L, inertia J, damping b and conversion constant k are positive and constant. In consistent SI units, use the same k for torque per current and back voltage per angular speed:

`L*i' = V - R*i - k*omega`

`J*omega' = k*i - b*omega`

The electrical and mechanical balances describe the assumed device, including its load in J and b. Saturation, variable load or a different drive would require the corresponding physical relations.

Suppose the work needs the slow speed response. The electrical relaxation time is `tau=L/R`. The current toward which the electrical part relaxes is `q(t)=(V(t)-k*omega(t))/R`. Replacing i by q gives

`J*omega' = (k/R)*V - (b+k^2/R)*omega.`

The eliminated current still supplies driving torque and additional damping. The slow response time of this candidate is `J/(b+k^2/R)`. Compare tau with that time and the drive's variation time.

To examine the neglected response, set `e=i-q`. The full electrical equation gives `tau*e'=-e-tau*q'`. If `|q'|<=K` on the interval, integration yields

`|e(t)| <= |e(0)|*exp(-t/tau) + tau*K*(1-exp(-t/tau)).`

The bound on q' can come from `|q'|<=(|V'|+k*|omega'|)/R` and the allowed drive and acceleration, using the full physical account where needed. A bound inferred only by assuming the proposed approximation would leave that assumption unresolved.

For example, let R=2 ohms, L=0.02 henry, k=0.1 in the stated SI convention, J=0.02 kg m² and b=0.01 N m s per radian. Then tau=0.01 s and the candidate slow time is about 1.33 s. With `|e(0)|<=0.5` ampere and K=1 ampere per second, the current departure at 0.05 s is at most 0.01331 ampere, giving a torque departure at that instant of at most 0.001331 N m relative to kq.

The slow speed error is a different output. With the same initial speed and drive, let delta be full speed minus reduced speed. It satisfies

`J*delta' + (b+k^2/R)*delta = k*e.`

Let `B(s)` denote the current-departure bound above. Since the initial speed difference is zero and the response kernel is positive, integration gives

`|delta(t)| <= (k/J)*integral_0^t exp(-(b+k^2/R)*(t-s)/J)*B(s) ds.`

For the stated values, this speed-departure bound at 0.05 s is about 0.026064 rad/s, hence less than 0.02607 rad/s. An allowed error of 0.03 rad/s therefore permits the reduced calculation for that speed reading. The integral carries the earlier transient into the answer; the small current departure at the final instant alone would not give this bound.

**Changed work.** If the next question concerns torque immediately after switching, the bound includes the initial current departure. Use the electrical transient. If the drive varies on the electrical relaxation time, recompute its departure instead of extending the slow-drive approximation. These returns change which physical response is retained.

#### PHY.5:5.2 - Decide when a chain can be treated as a continuous medium

Consider an infinite ideal one-dimensional chain with identical masses m, spacing a and linear springs of stiffness kappa. Each mass moves a small distance u_j from its reference position. The balance is

`m*u_j'' = kappa*(u_(j+1)-2*u_j+u_(j-1)).`

For waves with wavenumber q in `0<q*a<pi`, substitution of a sinusoidal wave gives

`omega^2 = (4*kappa/m)*sin^2(q*a/2).`

For wavelengths long compared with a, expanding the neighboring displacements gives the continuum equation `u_tt=c^2*u_xx` with `c=a*sqrt(kappa/m)`. It predicts both phase and group speed c. The chain's phase speed divided by c is `sin(q*a/2)/(q*a/2)`; its group speed divided by c is `cos(q*a/2)`. Expanding those ratios gives `v_phase/c = 1-(q*a)^2/24+O((q*a)^4)` and `v_group/c = 1-(q*a)^2/8+O((q*a)^4)`, exposing their different first corrections.

At q\*a=0.2 these ratios are about 0.99833 and 0.99500. A half-percent allowance for these speeds accommodates this ideal comparison, subject to the question's waveform and other physical premises. The group-speed difference is already larger than the phase-speed difference.

**Changed work.** A disturbance containing wavelengths near the shortest traveling waves of the chain probes q\*a near pi. The chain's group speed tends to zero, while the continuum account keeps c. A question about that disturbance's propagation requires retaining the discrete dispersion or an adequate extension. Making the computation of the uncorrected continuum equation more accurate cannot recover the omitted physical dependence.

This case concerns an ideal linear chain. It demonstrates choosing spatial resolution from the wave that matters.

#### PHY.5:5.3 - Retain fluctuations after fast velocity has relaxed

For a one-dimensional Brownian particle in a uniform equilibrium bath, take mass m, drag coefficient gamma and temperature T, with no applied force. The underdamped account has position x, velocity v and thermal forcing. Let `tau=m/gamma` and `D=k_B*T/gamma`. With an initially equilibrated velocity, its velocity covariance is `(k_B*T/m)*exp(-|t-s|/tau)`.

Integrating that covariance over the two times gives

`E[(x(t)-x(0))^2] = 2*D*(t-tau*(1-exp(-t/tau))).`

At times large compared with tau, the overdamped diffusion description gives `2*D*t`. Its omitted contribution to this mean-square displacement is bounded by `2*D*tau`. This calculation states which long-time consequence the reduction preserves.

Setting the mean velocity to zero and deleting the forcing instead gives no displacement spread. The unresolved bath continues to transfer random impulses after the velocity's preparation has relaxed. For the displacement distribution, retain their diffusion effect.

**Changed work.** Change the bath to a spatially varying temperature and ask about entropy production. The uniform-bath calculation no longer answers the question. Celani and coauthors show a further distinction: under their smooth-temperature and small-inertia conditions, the overdamped position process has the appropriate limit, while the mean rate of entropy production retains an additional positive contribution absent from the naive overdamped expression. Return to the thermodynamic observable and its limiting calculation. Position accuracy alone cannot decide that use. Their [2012 paper](https://arxiv.org/html/1206.1742v2) states the preparation and the contribution.

### PHY.5:6 - Bias-Annotation

The worked calculations emphasize classical continuous-time descriptions with explicit laws. The method also applies to choosing physical states and interactions when only a constrained response or statistical account is available. In such cases the first result can be a qualified regime choice or a discriminating physical question.

Time-scale separation is especially convenient and can dominate the choice too early. The spatial chain and changed thermodynamic observable show other reasons to retain a contribution. Quantum coherence, rare transitions and collective behavior require their own physical grounds; the classical examples do not decide them.

### PHY.5:7 - Conformance Checklist

- The intended consequence specifies the physical quantity, relevant preparation, range and interval.
- The comparison uses the coupled physical arrangement and explains the characteristic scales.
- Each omitted process retains any mean response, constraint, delayed influence or fluctuation needed by that consequence.
- The approximation follows from stated physical relations or remains an identified hypothesis.
- A bound or comparison reaches the actual requested output, including a relevant initial or boundary contribution.
- A changed condition that can defeat the selected description leads back to the implicated physical choice.
- Existing results are used when sufficient; further inquiry is selected for what it could change.

### PHY.5:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the construction | Consequence | Repair |
| --- | --- | --- |
| Delete a fast part and its coupling together | The motor loses the torque and damping supplied by its adjusting current. | Substitute the part's response into the retained interaction. |
| Apply the settled response at every instant | The initial current and switching response disappear. | Carry the transient and propagate its effect into the requested output. |
| Match one propagation speed and assume the other matches | A continuum approximation can misstate the arrival of a wave packet. | Compare the dispersion and the output the disturbance uses. |
| Replace unresolved motion by its mean | The Brownian particle loses its displacement spread. | Retain the fluctuation contribution when the question uses that distribution. |
| Use a successful position reduction for a thermodynamic observable | A limiting position process can omit entropy production. | Reduce the observable and its physical exchanges with the dynamics. |

### PHY.5:9 - Consequences

A useful effective account makes a physical mechanism easier to reason about and calculate with. Its stated regime supports a targeted return when the forcing, observation or intended action changes.

The choice costs physical analysis and sometimes a comparison with a richer account. It saves work when those results permit a cheaper calculation or a clearer explanation. A range without adequate scale separation can require a coupled, memory-bearing or more resolved description.

### PHY.5:10 - Architectural Rationale

This method organizes the choice by physical consequence and coupling. Comparing parameter sizes alone would miss how an omitted process enters the result. Starting from the most detailed available theory can impose work that the question does not need.

Effective-theory construction supplies a useful way to retain selected influences and improve an approximation systematically. Projection and coarse-graining show why unresolved motion can remain as memory and fluctuations. The observable-specific limit shows why their adequacy is judged at the receiving physical result.

MMP.9 owns the mathematical elimination; PHY.1 uses an effective account to compare changed physical arrangements; PHY.2 uses it when constructing an analogue. The contribution here is choosing and revising the physical resolution and remaining influence of unresolved processes. The motor, chain and Brownian particle demonstrate that contribution in different comparisons.

### PHY.5:11 - SoTA-Echoing

[Stewart's introduction to effective field theory](https://ocw.mit.edu/courses/8-851-effective-field-theory-spring-2013/e4ebfd74257683c3efa47b240196c505_WB8r7CU7clk.pdf) (MIT, 2013, lecture transcript pp. 2-4) is a historical teaching source for selecting relevant degrees of freedom, scales and an improvable leading description. This pattern adapts that construction beyond its quantum-field setting. It retains the need to identify an expansion and its range; improvement by further terms remains conditional on that expansion being useful.

[Dalton and coauthors, Memory and Friction: From the Nanoscale to the Macroscale](https://doi.org/10.1146/annurev-physchem-082423-031037) (2025; [accessible manuscript, section 3](https://arxiv.org/html/2410.22588v1)) supplies the contemporary account of retained observables, memory-dependent friction and simulation through auxiliary variables. Adopt the distinction between eliminating explicit variables and discarding their influence. An instantaneous response saves computation when its conditions hold; resolved memory preserves effects that such a response misses. The review's stated projection, equilibrium and preparation conditions govern its particular equations.

[Celani, Bo, Eichhorn and Aurell](https://arxiv.org/abs/1206.1742) (2012) provide the observable-specific counterexample used in :5.3. Adopt the comparison of the physical result before and after the limit. Their thermal-gradient result qualifies an otherwise successful position reduction; it does not rule out overdamped modeling for the position questions it answers.

The synthesis combines controlled omission, retained coupling and use-specific comparison. It favors the least costly description that supplies the needed consequence under the established physical conditions. Memory kernels, white-noise diffusion and a fully resolved model are alternative constructions with different requirements, selected by the question.

### PHY.5:12 - Relations

- **B.5.TU and PHY.4:** supply application of a physical theory and constraints on an unresolved law.
- **A.3.3.TR and C.29.BB:** supply common state, interaction and balance constructions used by the physical account.
- **MMP.9:** supplies elimination and reduced evolution; **MMP.7/.11** supply probability composition and constrained response families.
- **MATH.20** bounds the unresolved contribution; **C.29.1** establishes transfer of a bound or consequence between mathematical accounts.
- **PHY.1/.2/.3:** use the chosen description in similarity, analogue construction and physical limits.
- **C.11.DUA and C.11:** examine the value of further inquiry and choose among available descriptions.
- **G.5 and E.23:** state retained alternatives or jointly used descriptions when needed, and guide improvement by the chosen characteristics.
- **B.5.MPC.R and B.1.5.CM and A.3.1.CC:** return to a failed contribution and revise the method that uses the physical result.

### PHY.5:End
