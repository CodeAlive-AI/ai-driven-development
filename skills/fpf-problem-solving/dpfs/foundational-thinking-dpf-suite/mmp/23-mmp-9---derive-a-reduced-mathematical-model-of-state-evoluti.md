## MMP.9 - Derive a Reduced Mathematical Model of State Evolution

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.9:1 - Problem frame

Use this pattern when a supplied model describes how a state changes, but predicting the quantities you need would be easier with less state, shorter memory or a simpler update. After removing detail, the proposed update still depends on something you removed. You need to derive what can replace that contribution while retaining a useful answer.

Start with the quantity you want to keep and compute its change from the supplied model. Circle the part that cannot be obtained from the proposed smaller state. For an average, this may be the variance of the underlying values. For one observed component, it may be the effect of unobserved components. That expression identifies the construction needed next.

The result can be a smaller evolution law, a history-dependent rule, an approximation with a stated error, or bounds sufficient for the question. Keep the initial information, inputs and time range on which it depends. A model that is already affordable and sufficient can be used directly. If the original change law is missing, recover or construct it in the subject practice before using this reduction method.

You need the mathematics used by the supplied law: substitution and recurrence for discrete changes; differentiation and integration for differential equations; expectations when reducing a probability distribution. A mathematical collaborator may perform those operations from your stated question and model. This is reduction within mathematical modeling. A.3.3.PI supplies the general test of which information a prediction needs; C.29.1 supplies the comparison that transfers the reduced result back to the source question.

### MMP.9:2 - Problem

A description can retain today's quantity while losing what determines tomorrow's. Differentiating a mean can introduce higher moments. Solving for an unobserved component can make its past influence explicit. Dropping a quickly decaying component can retain a lasting change it caused before decaying.

The missing contribution is often called an **unclosed term**: the proposed retained state does not determine it. A **closure** supplies a way to obtain or approximate that contribution from the information the reduced model carries. Its choice changes the resulting evolution.

Finding the unclosed term locates the difficulty. The remaining work is to derive a usable replacement and determine what that replacement permits the model to answer.

### MMP.9:3 - Forces

| Choice | Consequence for the construction |
| --- | --- |
| Smaller state and longer memory | Eliminating coordinates can replace present-state work with a history calculation. |
| Detailed trajectory and selected result | A bound on one output can be cheaper than a replacement for the whole trajectory. |
| Additional moments and finite closure | Deriving another moment can expose yet another missing moment. |
| Short-lived component and lasting effect | A small or fast component can make a consequential accumulated contribution. |
| Fit to supplied trajectories and use inside a new evolution | Once the replacement supplies the next state, its errors can change the states it later receives. |
| Several adequate replacements and available effort | An existing bound or larger model can cost less than developing a new closure. |

### MMP.9:4 - Solution

**Choose the retained result → derive its change → expose the unclosed contribution → construct a replacement or bound → use it over the required horizon → revise the part that changes the answer.**

The work may end at a useful bound. It may also show that the smaller description would cost more than continuing with the source model.

#### MMP.9:4.1 - Express the retained result and its change

Name the source state z, its initial possibilities and the admitted inputs u. Specify the answer and horizon: a quantity at time T, a threshold crossing, a response to an input, or a distributional feature. Construct the retained description x=r(z) from those needs. A.3.3.PI:4.1-4.2 tests whether merged source states can still answer that question; use an already sufficient result from that test.

For a discrete source update z_next=F(z,u), substitute it into the retained description:

`x_next = r(F(z,u)).`

For a differentiable r and a differential law z_dot=F(z,u), the chain rule gives:

`x_dot = Dr(z) F(z,u).`

Dr is the derivative of r. If r also depends explicitly on time, include its time derivative. A discontinuous readout or event needs its own change relation rather than this differentiable formula. A.3.3.TR supplies composition of the relevant changes.

Rewrite the result using x, the admitted inputs and whatever other information the smaller model proposes to carry. The part still depending on discarded quantities is the unclosed contribution. One convenient decomposition is `x_dot=f0(x,u)+c(z,u)`, where f0 is the part you will compute directly and c is the remaining contribution. Another decomposition can be useful; what matters is the complete retained law and what information obtains each term.

If every term is obtainable from the retained information, construct the closed update through A.3.3.PI and compare it through C.29.1. Continue here when the replacement itself still needs construction.

#### MMP.9:4.2 - Derive the discarded contribution before approximating it

Try to express the discarded variables through their own evolution, initial conditions and the retained history. In a discrete law, iterate the discarded update and substitute each earlier term until the dependence has a usable form. In a differential law, solve or integrate the discarded equation under the supplied retained history, then substitute the result into the retained equation.

For constant compatible matrices and supplied initial values, consider:

`x_dot=A*x+B*y`, `y_dot=C*x+D*y`.

Solving the second equation while treating x(s) as its input gives:

`y(t)=exp(D*t)*y0 + integral_0^t exp(D*(t-s))*C*x(s) ds`.

Substitution gives the retained law:

`x_dot(t)=A*x(t)+B*exp(D*t)*y0 + integral_0^t B*exp(D*(t-s))*C*x(s) ds`.

The first added term carries the discarded initial condition. The integral carries the past influence of x through y. With a forcing term in the discarded equation, its propagated contribution also appears in the integral. These terms identify what a proposed memory approximation would replace. Unknown y0 remains an initial uncertainty; it cannot be set to zero solely because y is being removed.

Look for a less costly way to compute the derived expression. Equal decay modes can be combined; a sum of exponentials can be updated through a few auxiliary variables. For example, `v(t)=integral_0^t exp(-lambda*(t-s))*x(s) ds` satisfies `v_dot=x-lambda*v`, v(0)=0. This replaces storage of the whole history with an evolving value. Carry a nonzero initial contribution separately or incorporate its matching initial condition. Count the required auxiliary values and update work before claiming a computational saving.

For nonlinear discarded dynamics the same elimination question remains, but the response to retained history may require solving a nonlinear problem. Use the derived dependence to select an approximation, retained variable or bound; an implicit formula that still requires the original computation has not yet supplied a cheaper model.

#### MMP.9:4.3 - Choose and construct a useful replacement

Use the expression just derived to decide which information or calculation earns its cost.

**Retain a quantity that obtains the missing contribution.** If c depends on a small additional observable v, derive v's update from the source law and repeat the closure test for the pair (x,v). This operation can reveal a useful finite system or a growing hierarchy. For members obeying `Z_dot=-Z^2`, the mean m has `m_dot=-mean(Z^2)`. Retaining `q=mean(Z^2)` gives `q_dot=-2*mean(Z^3)`. The new equation exposes the next assumption needed; adding q alone does not finish the closure.

**Compute the effect through memory.** Use the history expression from :4.2. To truncate old history, bound its omitted contribution for the admitted histories. To replace the memory kernel by a simpler one, bound or estimate the resulting difference on those histories, then propagate that difference through the retained evolution. A slowly decaying kernel can make distant history consequential. An auxiliary-state representation can be cheaper than truncation when a few modes express that kernel.

**Bound the requested output.** If the use asks for a threshold or interval, derive bounds directly from the source law and available initial information. For a population, solve or bound the member response as a function of its initial value, then average using known ranges or moments. Monotonicity, convexity or conservation can give a bound without choosing a complete distribution. The nonlinear example in :5.2 constructs such bounds. Use C.29.1:4.5 to turn them into the corresponding decision, or to expose the still-unresolved range.

**Approximate a contribution whose accumulated effect is small.** Identify the parameter and the class over which smallness is claimed: initial values, inputs, horizon and required error. Derive or bound the contribution integrated over that horizon. A small coefficient can multiply a large hidden value, and a fast transient can shift the later state. If a transient only matters near the start, retain its effect in an adjusted initial value and state when the later approximation begins. :5.3 shows both constructions.

A learned closure is another possible approximation to the missing contribution. Specify what its inputs contain and how its output enters the retained update. Pairs of retained inputs and source contributions can support fitting, but different hidden states can give different contributions at the same retained input. A fitted conditional mean then answers a distribution-dependent question; it is not an all-cases replacement of those contributions. When probability is needed, MMP.7 helps construct the law of the sampled or recorded training cases. Use the resulting closure at its intended inputs and horizon before drawing the corresponding predictive conclusion.

Compare the candidates through the existing characterization and choice methods: the required output or bound, obtaining cost, initial information and conditions. There is no need to develop every alternative. C.11.DUA helps choose whether more derivation, data or computation can change the decision.

#### MMP.9:4.4 - Evaluate the replacement inside the retained evolution

Write the model that will actually be used, including its initial values, any auxiliary variables, input rule and observation interpretation. Construct the requested output from that model. Substituting the closure into known source trajectories tests a different computation from letting it generate successive retained states.

Compare the retained source result and the reduced result for the same admitted initial case and input. For an identity, use the derivation to establish the covered equality. For an approximation, propagate the discrepancy to the requested output and horizon through C.29.1:4.5. A numerical scheme adds its own approximation; include it when it can change the answer. A.3.3.PI:4.5 supplies the repeated-use and changed-condition questions.

For a probabilistic model, choose the distributional feature the work needs. Agreement of a mean can coexist with different variance, correlations or event probabilities. A further observable is worth checking when it can change the planned use. State which result the comparison supports rather than extending one fitted statistic to the whole model.

When inputs are chosen from observations, retain the information the choice rule uses. If reduction removes that information, formulate the revised choice under MMP.8 before claiming that the same intervention or control method remains available. A changed intervention also requires the corresponding source law or mechanism under C.28.MR.

#### MMP.9:4.5 - Return the result and revise the construction when needed

Return the reduced law, sufficient bound or located obstacle with the assumptions that affect its use. An existing derivation and calculation can carry this information. Explain which discarded contribution was replaced, how to initialize and run the replacement, and which question it answers.

If a bound settles the working question, use it. If the result is too weak, locate why: uncertain initial influence, unresolved higher moment, long memory, error amplification, or information unavailable to an action. Improve that contribution or retain more of the source model. A mathematical construction can also show that the proposed simplification offers no saving.

Reopen the affected construction when the source law, initial class, inputs, observation, horizon or required output changes. Keep conclusions whose conditions still hold. In a model of a working method, MMP.22 can use the mathematical comparison to construct a different working rule, while C.37 selects a changed representation; the actual work must still provide the quantities and relations assumed in the model.

### MMP.9:5 - Archetypal Grounding

#### MMP.9:5.1 - Replace many response components by two evolving quantities

Suppose a dimensionless model has an observed x and n hidden response components:

`x_dot=-x+sum_i y_i+u(t)`, `y_i_dot=c_i*x-2*y_i`,

where the nonnegative c_i sum to one. Initial values and a prescribed input u(t) are supplied. The question asks for x over a finite horizon; each y_i separately is irrelevant to that result.

Retaining x alone leaves the unclosed contribution sum_i y_i. Solve each hidden equation and sum:

`sum_i y_i(t)=exp(-2*t)*sum_i y_i(0)+integral_0^t exp(-2*(t-s))*x(s) ds`.

All hidden contributions have the same decay kernel. Define v=sum_i y_i. Differentiating the sum gives the two-variable model:

`x_dot=-x+v+u(t)`, `v_dot=x-2*v`, `v(0)=sum_i y_i(0)`.

The derived equations and initial sum preserve x for every supplied input for which these linear equations have their solution. For n>1 this uses two evolving quantities instead of n+1. The required hidden initial information is their sum. Arbitrarily setting v(0)=0 would already change x_dot(0) when the actual sum is nonzero.

The initial sum requires n terms once. Each subsequent evaluation of the reduced right-hand side uses x, v and u(t); it no longer recomputes n component contributions. This saves repeated arithmetic when those components would otherwise be advanced separately.

Now one component has decay rate 3 instead of 2. Summing produces `v_dot=x-2*v-y_1`; the old two-variable model has lost a contribution. Retain y_1 separately and update it by `y_1_dot=c_1*x-3*y_1`, or separate the two decay groups. The change determines which added state is needed. The same grouping can combine any components that share their response kernel; different kernels remain distinct until another justified approximation combines them.

#### MMP.9:5.2 - Answer about a nonlinear population without a closed mean equation

A finite population has nonnegative member values X_i with `X_i_dot=-X_i^2`. The available initial information is 0<=X_i(0)<=M and mean m0. The requested output is the mean m(t).

Differentiating the mean gives:

`m_dot=-mean(X_i^2)=-m^2-Var(X_i)`.

Replacing this by m_dot=-m^2 sets the variance contribution to zero. Populations with the same mean can have different variance, so first ask whether a bound already answers the question.

Each member has `X_i(t)=X_i(0)/(1+t*X_i(0))` for t>=0. Since X_i(0)<=M, averaging gives the lower bound `m0/(1+M*t)`. The response `a/(1+t*a)` is concave for nonnegative a and t>=0; the mean of the responses is at most the response of the mean. Thus:

`m0/(1+M*t) <= m(t) <= m0/(1+m0*t)`.

With M=2, m0=1 and t=1, the mean lies between 1/3 and 1/2. A requirement m(1)<=0.55 is established without a variance model or a complete initial distribution.

Change the requirement to m(1)<=0.4. A population whose members all start at 1 has m(1)=1/2. An equally divided population starting at 0 and 2 has m(1)=1/3. Both fit the supplied initial information, so it cannot settle the changed requirement. Information about the initial population or a different acceptable requirement would change the next move. Treating the zero-variance closure as the whole population would conceal this distinction.

#### MMP.9:5.3 - Decide whether a fast transient can be omitted

For a dimensionless model with epsilon>0,

`x_dot=y`, `epsilon*y_dot=-y`,

the solutions for t>=0 are `y(t)=y0*exp(-t/epsilon)` and `x(t)=x0+epsilon*y0*(1-exp(-t/epsilon))`.

Suppose the admitted initial values satisfy abs(y0)<=Y. Replacing the model by constant x0 gives an error at most epsilon\*Y for every t>=0. With epsilon=0.01 and Y=1, that is 0.01. It can meet a tolerance 0.02 while failing to establish tolerance 0.001. The coefficient alone is insufficient if the initial class changes: y0=1/epsilon leaves a later change approaching one.

When y0 is known and the use concerns only later times, a different approximation is constant `x0+epsilon*y0`. Its error is at most `epsilon*Y*exp(-t/epsilon)`. For tolerance `0<eta<epsilon*Y`, it meets that tolerance at all times starting from `t_start=epsilon*log(epsilon*Y/eta)`. With eta=0.001 in the preceding case, t_start is about 0.0231. The adjusted initial value has retained the transient's later effect; it does not reproduce the initial interval.

If y0 is unknown, the adjusted value is also unknown. Its stated range can still yield a useful interval for x. The choice between an early transient calculation, a later approximation and a bound follows the requested result and available initial information.

### MMP.9:6 - Bias-Annotation

Compact equations can conceal transferred effort. Removing variables may require a history integral, extra initial information or an expensive closure. Compare the work needed to obtain the requested result. A familiar equilibrium substitution or learned fit is a candidate construction whose lost contribution must remain visible in that comparison.

### MMP.9:7 - Conformance Checklist

- Can the retained quantity's change be derived from the supplied law, with its initial and input conditions?
- Which contribution is unavailable from the proposed retained information, and how does the replacement obtain, approximate or bound it?
- Does an added variable have its own usable update and initialization? If a hierarchy remains, where is the closing assumption?
- For a memory or small-parameter approximation, what bounds the omitted effect on the requested output over the stated horizon?
- Is the comparison made in the model's intended repeated use, with the relevant numerical and observation conditions?
- Does the resulting law or bound settle the working question? If not, which changed contribution could do so at worthwhile cost?

### MMP.9:8 - Common Anti-Patterns and How to Avoid Them

| Observed difficulty in the construction | Repair |
| --- | --- |
| Replacing the mean of a nonlinear response by the response at the mean loses heterogeneity. | Derive the missing moment term, then retain, model or bound its effect; :5.2 may already settle the output question. |
| Hidden state is eliminated together with its initial effect. | Carry the initial-condition term in the memory formula or initialize the corresponding auxiliary value. |
| A small coefficient is used as the entire error argument. | Bound the multiplied state, accumulated contribution and admitted initial class, as in :5.3. |
| A closure is judged only on inputs from the source trajectory. | Insert it into the retained evolution and compare the requested result at its intended horizon. |
| Adding a moment is presented as completing a model although its equation needs another moment. | Continue the derivation until a usable closure or sufficient bound is obtained; otherwise retain the unresolved contribution. |

### MMP.9:9 - Consequences

A reduced model can expose which information determines the answer and make repeated calculation cheaper. Bounds can support a decision before a full reduced trajectory is available. Derivation also identifies a reusable limitation: which initial conditions, inputs or new questions require restoring discarded content.

The cost can move into initialization, memory, closure construction or verification at the required horizon. Where that cost exceeds using the source model, the larger account remains a useful option.

### MMP.9:10 - Architectural Rationale

Reduction is organized around the requested result and the source law's unclosed contribution. This makes the choice between retained state, memory, approximation and bounds depend on what each construction obtains. Beginning with one favored approximation would select what to discard before establishing its effect.

A.3.3.PI supplies the question-relative information test. This method develops the subsequent mathematical construction of a replacement contribution. C.29.1 supplies the common exact-or-bounded transfer and error propagation; those rules also apply to constructions outside model reduction.

Linear response, nonlinear aggregation and fast transients require different constructions. A new source law requires deriving its own discarded contribution; it need not resemble one of these examples. When the deriving operation itself requires a further subject method, retain that mathematical dependency rather than presenting a technique's name as an already obtained closure.

### MMP.9:11 - SoTA-Echoing

The practice question is how to replace unresolved dynamics economically while retaining the needed result. **Adopt** construction from the source law and evaluation within the reduced evolution, including memory, initial information and question-relative outputs. A serious alternative fits an instantaneous missing term on source trajectories and judges primarily that fit. It can be cheaper and adequate for a limited use, but it can miss errors generated when the closure supplies its own future inputs.

[Sanderse, Stinis, Maulik and Ahmed, Scientific machine learning for closure models in multiscale problems, version 2 (2024), sections 2.1-2.2, 3.2 and 7.1](https://arxiv.org/html/2403.02913v2), is a comparative synthesis of closure constructions. It distinguishes an unclosed term from its replacement, and fitting the term from testing the evolving reduced model. **Adapt** these distinctions in :4.1-4.4. Its memory discussion supports preserving initial and historical effects during elimination. An exact elimination identity still needs an affordable way of obtaining its result; :4.2 makes that cost question explicit. The linear elimination, population bounds and transient estimates above are elementary derivations developed here.

[Freitas, Um, Desbrun, Buzzicotti and Biferale, A posteriori closure of turbulence models: are symmetries preserved? (2026 preprint), sections 3-5](https://www.geometry.caltech.edu/pubs/FUDBB26.pdf), provides a current countercase. A learned shell-model closure reproduces selected statistics while missing other correlations and scale-invariance properties. **Adopt** its consequence in :4.4: select the observables that the receiving use needs instead of extending fit of one statistic to all requested behavior. Missing memory is a proposed explanation in that case; it does not establish a universal cause or require every reduced model to carry the same memory construction.

The selected method spends effort on the omitted contribution and the use it can change; it need not reproduce every property of the detailed model. A sufficient analytic bound can be cheaper than training or testing another closure. Reopen the comparison when changed inputs, initial conditions, horizon or requested observables expose a consequential error, or when another construction obtains the same needed result at lower cost.

### MMP.9:12 - Relations

- **A.3.3.TR and A.3.3.PI:** compose source changes, determine the information needed for the future question and update the retained account. MMP.9 constructs a remaining closure or bound after those operations expose the gap.
- **C.29.1 and MATH.2:** compare the retained construction with the source and determine which answers survive identification; use their exact or bounded transfer where applicable.
- **MMP.7 and MMP.8:** construct observation laws and information-limited choices when a learned or controlled reduced model uses them. Their conditions determine which data law or action rule is actually being compared.
- **C.28.MR and B.5.MPC.R:** reconsider the relevant mechanism or connected accounts when an intervention or model change alters the source law.
- **C.11.DUA:** decide whether further derivation, observation or comparison is worth its cost for the receiving decision.
- **E.22 and E.23:** frame the question for evaluating a candidate, then organize repeated improvement under that evaluation when needed.
- **EXD and C.2.8:** EXD develops an explanation for the recipient's question; C.2.8 compares what structure that recipient can recover from its expression under stated conditions. Prediction and explanation can require different retained results.
- **MMP.22:** use the mathematical result to construct a changed working rule; return its practical arrangement to C.32.MWA.PP.

### MMP.9:End
