## MMP.17 - Construct a Surrogate for Selected Model Responses

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.17:1 - Problem frame

**Use this when** repeated use of a model is too costly or cumbersome, and the next calculation needs only some of its responses. You may need values at many inputs, a probability of exceeding a limit, a field over a region, or a response used inside an inverse problem. Begin with one receiving question: which response must the replacement supply, over which inputs, and what error would change the answer?

A **surrogate** is a replacement constructed to reproduce selected responses of a source model. It may be an interpolation table, a constrained formula, a reduced representation of outputs, a learned function, or a correction to a cheaper model. The practical gain is a less costly response with a usable account of where substitution holds and where to return to the source.

This is a method of mathematical modeling. It applies to computational, physical, biological and organizational models; a differential equation or a neural network is one possible case. It governs the construction and use of a replacement, while the subject practice supplies the meaning and grounds of the source model. Agreement with that model and agreement with the world remain different questions.

Preparation requires functions, interpolation and an error comparison suited to the receiving calculation. The derivative branch uses elementary differentiation; the output-basis branch uses orthogonal projection and singular value decomposition. The stochastic branch requires expectation, variance and the meaning of interval coverage. For a learned replacement, CMP.7 supplies the learning rule and its further-use conditions, with CMP.6 supplying iterative computation when needed. A specialist can construct a harder approximation, but must return an evaluable replacement and the conditions under which its response can be substituted.

For a few inexpensive queries, evaluate the source or reuse already computed answers. If a prescribed numerical approximation already supplies the response and sufficient error control, CMP.8 may finish the work. Surrogate construction becomes useful when selecting the responses, cases and retained structure changes what can be obtained at affordable cost.

### MMP.17:2 - Problem

A replacement can fit its construction cases and fail at the inputs or operations that matter next. Average accuracy can conceal a wrong threshold crossing, a lost dependence between outputs, or a derivative with the wrong sign. A source model can also be wrong in a way that its accurate surrogate faithfully reproduces.

The modeling problem is to construct a useful substitution without silently enlarging its promise: choose what to reproduce, obtain informative cases, build the replacement, and act on consequential discrepancies or lost structure.

### MMP.17:3 - Forces

| Force | Tension |
| --- | --- |
| Selected response | Reproducing less can save work, while a later question may need something discarded. |
| Construction cost | More source evaluations can improve the replacement, but may consume the saving it was meant to provide. |
| Known structure | Conservation, bounds and symmetries restrict useful candidates; a convenient restriction can also exclude the needed response. |
| Local and broad use | Concentrating cases near a decision can improve that answer while leaving other inputs poorly represented. |
| Several error sources | Source computation, surrogate approximation and uncertain source premises can each limit use and require different repairs. |
| Continued use | Reuse makes construction worthwhile, but changed inputs or questions can invalidate the substitution. |

### MMP.17:4 - Solution

Construct the replacement around the response that another calculation or person will use. Carry the source conditions into that substitution, and refine only where the remaining difference matters.

#### MMP.17:4.1 - Select the response and the input region

Let \(M\) be the source model and let \(Q\) extract the required response. Write the target as

\[
r(x)=Q(M(x)),\qquad x\in D,
\]

where \(x\) contains the inputs and \(D\) is the intended region of use. The input may be a number, a vector, a history, a function or a discrete configuration. State enough of its meaning to distinguish materially different conditions. If the same listed input gives different deterministic responses because a regime or previous state was omitted, restore that input before fitting a function.

Choose \(Q\) from the receiving operation. A mean, a tail probability and an entire probability law are different targets. So are a field value, its spatial derivative and a quantity integrated over that field. For a random source output \(Y_x\), a mean surrogate targets \(\mathbb E[Y_x]\); reproducing individual draws or their distribution requires another construction.

Determine how response error affects the receiving result. For a comparison with a limit, the distance to the limit matters. For a ranking, the gap between alternatives matters. If the receiver will differentiate, iterate or invert the response, include the corresponding sensitivity or structural requirement. A low average value error does not select these requirements for the practitioner.

#### MMP.17:4.2 - Obtain construction cases that can distinguish useful replacements

Reuse source results whose inputs, output meanings and computation are compatible with the target. Choose further cases to expose consequential variation: the region the receiver will visit, boundaries or changes of regime, and places where plausible replacements disagree about the receiving answer.

For a scalar interval, an initial set of endpoints and interior points may suffice. For many inputs, a full grid can be unaffordable; use known structure to reduce the varying inputs, or distribute a finite set across the relevant region before concentrating additional cases. A design concentrated near one operating point supports a local construction unless another argument supports wider use.

Each case supplies an input and the selected source response. If the source response is itself approximate, carry its error into the construction. For a stochastic source, use MMP.7 to identify how the runs were obtained: repetitions, dependence, shared random inputs and selection can change what their averages or fitted probabilities estimate. MMP.13 supplies the uncertainty result needed from those runs.

Choose case placement and assessment together. Cases used to fit, select or repeatedly tune the replacement are construction cases. If the further-use claim depends on held-out performance, retain assessment cases suited to that use and do not count their later reuse for tuning as untouched assessment. For trajectories, repeated runs or grouped inputs, the unit that must be held out follows the claim; randomly separating nearby points does not by itself test a new trajectory or regime.

A query to the source model adds information about that model's response. An observation of the world may also challenge the model. Keep those contributions separate. Use existing bounds or observations when they already answer the question; another experiment is not an entry condition for constructing a surrogate.

#### MMP.17:4.3 - Construct an evaluable replacement with the needed structure

Start with a representation that can express the required response at the available construction cost. Use MMP.11 to preserve justified relations and to expose what remains adjustable.

For ordered scalar cases \((x_i,r_i)\), one complete construction is piecewise linear interpolation:

\[
\widehat r(x)
=\frac{x_{i+1}-x}{x_{i+1}-x_i}r_i
+\frac{x-x_i}{x_{i+1}-x_i}r_{i+1},
\qquad x_i\leq x\leq x_{i+1}.
\]

The rule supplies a response between distinct neighboring inputs. It needs no iterative training. Its adequacy between the cases still depends on the response's variation and the receiving tolerance.

For a field or a large output vector, one can instead construct

\[
\widehat y(x)=y_0+\sum_{j=1}^{k} a_j(x)\phi_j.
\]

Here \(y_0\) and the retained output shapes \(\phi_j\) come from known structure or computed cases. For example, take \(y_0\) as the mean case vector, stack the centered case vectors as columns, retain selected left singular vectors of that matrix, and project each centered case onto those orthonormal vectors. Then interpolate or learn the coefficient functions \(a_j(x)\) from the inputs and the computed coefficients. A small reconstruction error over sampled fields can still discard a localized feature that controls the receiver's maximum or threshold. If only \(Q(y)\) is needed, compare approximating that response directly with reconstructing the full field.

When a cheap model \(L\) already follows much of the response, construct a correction from paired cases:

\[
d_i=r(x_i)-L(x_i),\qquad
\widehat r(x)=L(x)+\widehat d(x).
\]

Pair the same inputs and corresponding outputs. This construction still evaluates \(L\) at each new input. It is useful when the discrepancy is easier to approximate than the whole response; if the cheap model misses the consequential regime, adding many cheap cases may help little.

For a learned function, supply CMP.7 with the target, construction cases, function family and loss that reflects the required response. Obtain its effective fitting procedure through CMP.6 or another suitable computation. Writing an objective without a way to obtain and evaluate its candidate leaves the replacement unfinished. Optimization progress, fit on construction cases and accuracy at further inputs are separate results.

Preserve a justified relation by construction when possible. If two delivered quantities must sum to an input \(d\), construct one and define the other as \(d-\widehat q_1\), while also enforcing any required nonnegativity or capacity limits. A small penalty for violating a relation permits violations; it does not implement the relation as an identity.

#### MMP.17:4.4 - Locate errors and losses that change the receiving use

Compare the replacement with the source in the quantities the receiver consumes. A deterministic bound, an empirical error on selected cases and a statistical interval support different conclusions.

When bounds are available in the same response metric, propagate them. For example, if interpolation of accurate case values differs from \(r\) by at most \(e_{\mathrm{int}}\), and each supplied case value has error at most \(e_{\mathrm{case}}\), convex linear interpolation has error at most \(e_{\mathrm{int}}+e_{\mathrm{case}}\). Other fitting rules need their own propagation: a poorly conditioned fit can amplify errors in its cases. CMP.8 supplies that numerical approximation and conditioning work.

For a scalar test \(r(x)\leq b\), a justified bound \(e(x)\) gives an immediate rule:

- if \(\widehat r(x)+e(x)\leq b\), the bound supports the test;
- if \(\widehat r(x)-e(x)>b\), the bound rules it out;
- otherwise the replacement leaves this test unresolved.

An observed maximum error at finitely many cases is not automatically a bound over \(D\). A statistical coverage result retains its sampling and calibration conditions and its pointwise, marginal or simultaneous meaning. A fitted uncertainty indicator can guide the next query without supplying such a result.

Test lost operations as well as values. On \([0,1]\), \(r(x)=x\) and \(\widehat r(x)=x+0.01\sin(1000x)\) differ in value by at most \(0.01\). Yet \(r'(x)=1\), while \(\widehat r'(\pi/1000)=-9\). If a receiver follows the derivative, this substitution can reverse the proposed direction. Include derivative information or a justified monotone family when that operation matters, or keep the source calculation for it.

A discrepancy with the source calls for examination of case coverage, representation or fitting. A discrepancy with observations can instead require MMP.14 to revise the source or its observation model. Agreement with the source cannot close that second question.

#### MMP.17:4.5 - Refine, combine or return where the difference matters

Choose the next change from the unresolved receiving result. With piecewise interpolation and a bound on curvature, subdivide intervals whose error bound can change that result. With an empirical construction, inspect informative new source cases, a different family or a local correction. Adding cases everywhere can cost more than repairing the affected region.

For adaptive case selection, make a finite candidate set in the allowed region, compare its points by the expected relevance of their unresolved responses and an error or disagreement indicator, and query the chosen source cases. Retain coverage of plausible unexplored regimes; a confident but misspecified replacement can otherwise prevent its own correction. Refit after adding the cases and assess the changed replacement under the conditions needed for the claim. The indicator is a reason to investigate a point, not evidence that the source response there has already been obtained.

A useful combination may keep the source near a threshold or regime boundary and use the surrogate elsewhere. It may keep a cheap model with a learned correction, or different replacements for different response questions. Make the selection condition usable by the caller. When a query is outside the supported region or the needed error control is unavailable, call the source if it can answer, restrict the claim, or return the unresolved response.

Compare total effort: case generation, fitting, checking, each later evaluation, and repairs after relevant changes. A source call can finish a single difficult query more cheaply than improving a reusable approximation. Stop when the receiving question has sufficient support at acceptable cost. Use the existing FPF choice and improvement methods when several worthwhile replacements or refinements remain; this construction does not require one universal best surrogate.

#### MMP.17:4.6 - Carry the substitution into continued use

Make the evaluation rule, input meanings and region, selected responses, and consequential limits available with the replacement. The receiver must be able to obtain its response and recognize when the fallback applies. A function with its conditions in the surrounding model may suffice.

When the surrogate enters an inverse problem or an uncertainty calculation, propagate its approximation in the observation metric and into the requested conclusion. A small forward-response error can matter greatly along a poorly resolved direction. MMP.12 supplies the ambiguity and regularization analysis; MMP.13 supplies the qualified inference and uncertainty. Treating the replacement as an exact likelihood or forward relation can give a tighter answer than its construction supports.

Reopen the construction when the input region, source assumptions or receiving operation changes. A new question about an intervention may need causal identification or a mechanism supplied by the subject practice, even if the old predictions remain accurate. A new request for explanation needs the relevant relations, not only the same output number. Use C.2.8 to distinguish the structure a reader can recover and EXD to construct an explanation from a supplied subject account. A compact surrogate may expose useful structure, but compactness and predictive fit do not establish that contribution.

### MMP.17:5 - Archetypal Grounding

#### MMP.17:5.1 - Refine an interpolation only until it settles the comparison

A repeated calculation needs the response \(r(x)\) of a costly reference model for \(0\leq x\leq1\). The present question is whether \(r(0.4)\leq0.3\). Available analysis of the reference model gives \(|r''(x)|\leq2\). Its accurate case values are \(r(0)=0\) and \(r(1)=1\).

The first surrogate is the line \(\widehat r(x)=x\). For linear interpolation on an interval of width \(h\), the curvature bound gives an error at most \(2h^2/8\). With \(h=1\), the response at \(0.4\) is therefore enclosed by \(0.4\pm0.25\). This interval crosses \(0.3\); the replacement has not answered the question.

Query the reference model at \(x=0.5\), obtaining \(r(0.5)=0.25\), and use the two half-intervals. In the first half, \(\widehat r(x)=0.5x\), so \(\widehat r(0.4)=0.2\). The bound is now \(2(0.5)^2/8=0.0625\), giving

\[
r(0.4)\in[0.1375,\,0.2625].
\]

The upper endpoint is below \(0.3\). One added case and a specified interpolation rule settle the comparison under the curvature premise. The three values alone would not justify the bound.

Now the receiving limit changes to \(0.18\). The same enclosure crosses that limit. For this one query, the practitioner returns to the reference model at \(0.4\), which gives \(0.16\), and can answer the stricter comparison. If many similar queries are expected, further subdivision may instead be worthwhile. There is no need to improve the surrogate over the entire interval to finish the single question.

These calculations establish agreement with the reference model under its stated smoothness and case-accuracy conditions. Whether that model's response represents the subject phenomenon remains a separate modeling question.

#### MMP.17:5.2 - Correct a cheap allocation model, then change its regime

A network model returns delivered quantities \(q_1(d)\) and \(q_2(d)\) through two channels for demand \(2\leq d\leq4\). In the normal regime all demand is served, so \(q_1+q_2=d\). A cheap approximation splits it equally: \(L(d)=(d/2,d/2)\).

The source supplies \(q(2)=(1.2,0.8)\) and \(q(4)=(3,1)\). The first-channel discrepancies from \(L\) are \(0.2\) and \(1\). Linear interpolation of that discrepancy gives

\[
\widehat d_1(d)=0.4d-0.6,\qquad
\widehat q_1(d)=0.9d-0.6,\qquad
\widehat q_2(d)=d-\widehat q_1(d).
\]

At demand \(3\), the replacement returns \((2.1,0.9)\). It preserves total delivery and nonnegativity throughout the declared interval. Those properties follow from the construction; agreement between the cases has not yet been established.

The receiving question is whether the first delivery stays at or below \(2.25\) at demand \(3\). The provisional value \(2.1\) is only \(0.15\) below the limit, and there is no supported error bound for this interpolation. A source query at \(3\) returns \((2.4,0.6)\), ruling out the proposed limit. Add its discrepancy \(0.9\) and interpolate separately over \([2,3]\) and \([3,4]\). The new surrogate matches all three cases and preserves the balance. Further-input accuracy remains an empirical question or requires a separate bound.

Now channel 2 becomes unavailable. The normal-regime fit does not describe this input. Suppose the changed source account states that channel 1 serves all demand up to \(3\) units and any excess remains unserved. The needed output now includes unserved demand \(u\):

\[
q_1=\min(d,3),\qquad q_2=0,\qquad u=d-q_1.
\]

At demand \(4\), the result is \((3,0,1)\). The balance has become \(q_1+q_2+u=d\). This branch follows from the newly supplied operating rule, not from extrapolating the normal-regime cases. Its formula is already cheap enough to use; training another replacement adds no benefit here. The caller can retain the normal-regime surrogate for its supported questions and use this formula for the stated unavailable-channel regime.

#### MMP.17:5.3 - Reuse stochastic cases when the requested response changes

A stochastic loss model returns either \(0\) or \(5\). Its source structure states that the probability \(p(x)\) of loss \(5\) is affine for \(0\leq x\leq1\); the two endpoint probabilities are unknown. All 2,000 runs in the construction are independent: 1,000 runs give 100 losses of \(5\) at \(x=0\), and another 1,000 give 300 at \(x=1\).

Fit the endpoint proportions and interpolate:

\[
\widehat p(x)=0.1+0.2x,\qquad
\widehat\mu(x)=5\widehat p(x)=0.5+x.
\]

The affine premise comes from the source structure, not from the two observed proportions. The mean surrogate is evaluable without rerunning the stochastic source.

At \(x=0.5\), the estimated mean is \(1\). A simple uncertainty calculation illustrates what must accompany that value. Each endpoint proportion has variance at most \(1/(4{,}000)\). Independence gives variance at most \(1/(8{,}000)\) for their average, an unbiased estimator of \(p(0.5)\) under the affine premise. Chebyshev's inequality therefore gives coverage of at least 95% for a half-width of \(0.05\) around that average. The resulting probability interval is \([0.15,0.25]\), and the corresponding mean interval is \([0.75,1.25]\). For a receiver using this 95% confidence procedure, the upper endpoint supports the mean-at-most-\(1.4\) comparison; it is not a deterministic bound. MMP.13 permits sharper uncertainty calculations when the receiving use needs them.

The receiver now asks whether \(\Pr(Y_{0.5}>4)\leq0.18\). The mean alone cannot answer: a constant loss of \(1\) has the same mean but a different tail. Here the retained two-point support supplies the relation \(\Pr(Y_x>4)=p(x)=\mu(x)/5\). Reuse the same cases and the probability surrogate; no new fit is needed. The interval \([0.15,0.25]\) crosses \(0.18\), so this uncertainty result leaves the new comparison unresolved.

The interval concerns the fixed input \(0.5\) under independent runs, the stated support and the affine probability law. It is not a simultaneous guarantee for all inputs, and it does not cover error in those source premises. A sharper inference, a useful bound, more runs or a qualified unresolved answer are different possible continuations; choose among them for the receiving question.

### MMP.17:6 - Bias-Annotation

Convenient source cases can overrepresent smooth central behavior and miss a boundary, rare response or minority regime. Begin with the receiving consequence, then check whether the construction and assessment actually expose it.

A family with a smooth uncertainty indicator can understate error where all its members share the same missing structure. Source comparisons outside the currently attractive region can reveal that failure. The indicator's numerical precision does not strengthen its grounds.

Construction cost can be hidden by reporting only evaluation speed. Compare the reuse expected in this work, including source queries and repair, before attributing a practical saving.

### MMP.17:7 - Conformance Checklist

Use these questions when relying on or passing on the replacement. The answers can remain in the model and its explanation.

| Check | Required content |
| --- | --- |
| Target | The source, selected responses, receiving operation and input region are recoverable. |
| Cases | Their obtaining conditions and any source-computation or sampling uncertainty fit the construction. |
| Construction | The representation and obtaining rule produce an evaluable replacement; justified coupled constraints are retained. |
| Consequential error | The error comparison addresses the receiving result and states whether its grounds are a bound, empirical comparison or statistical result. |
| Lost structure | A required derivative, dependence, regime or explanatory relation has not been inferred from value fit alone. |
| Continued use | The caller can identify unresolved queries and use the supported refinement, restriction or source return. |
| Effort | Construction and continued-use costs justify the substitution for the intended work. |

### MMP.17:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Declare success from small average error while a limit crossing is wrong. | Compare the response and error in the receiving operation, including the affected input region. |
| Treat an optimization objective as the constructed surrogate. | Supply the fitting procedure and the evaluator; inspect computational failure separately from inadequate cases or family. |
| Add cheap cases whose model misses the needed regime. | Examine the cheap-to-source discrepancy and compare correction with source-only construction at the same total effort. |
| Differentiate or invert a value surrogate without carrying its approximation. | Include the required operation in construction and error analysis, or keep the source for that operation. |
| Use the same cases repeatedly for tuning and claim untouched assessment. | Treat them as construction information and qualify the remaining further-use result. |
| Read a fitted interval as a guarantee against missing source structure. | Retain its conditions and return to source-model criticism or the subject account when those conditions change. |

### MMP.17:9 - Consequences

Selected responses can become cheap enough for repeated comparison, simulation or inference. Known constraints can remain usable even when most of the source calculation is replaced, and a local source return can resolve the few queries that remain difficult.

The saving comes with a narrower promise and construction cost. Different responses may need different replacements. A changed question can reuse the cases while changing the response construction, as in the tail-probability example, or require a changed source account, as in the unavailable-channel example.

### MMP.17:10 - Architectural Rationale

The response and the receiver's operation are chosen before the representation because they determine which differences matter. Reconstructing an entire model can waste effort; reproducing only a convenient summary can remove what the next operation needs. Selecting \(Q\) and \(D\) makes that trade-off actionable.

MMP.11 constructs families from known relations. MMP.17 adds the substitution question: which source responses to retain, which cases make their replacement informative, and where to refine or return when the replacement changes a receiving answer. CMP.7 and CMP.6 supply learning and computation when those are the chosen construction, while CMP.8 supplies numerical approximation control. The interpolation branch shows why a surrogate need not require a learner.

The source remains distinguishable from its replacement because a source call can repair approximation without repairing the model's account of the world. MMP.14 governs the latter discrepancy. Likewise, fast predictive use can coexist with a separate explanatory model; neither role earns the other's conclusions by sharing outputs.

### MMP.17:11 - SoTA-Echoing

The practice question is how to obtain a reusable response at lower total effort without losing what the receiver must do with it. The selected answer is a response-specific construction with informative cases, retained structure, and refinement or source return where the receiving consequence remains unresolved. It does not select one model family for every input dimension, data budget and error claim.

**Adaptive construction versus a fixed case budget.** [Winovich et al., *Active operator learning with predictive uncertainty quantification for partial differential equations*, v4 (2026), §§2 and 5](https://arxiv.org/html/2503.03178v4) compares uncertainty-guided construction with alternatives that differ in accuracy and training cost. **Adapt** this experimental line in :4.2 and :4.5: target informative queries while counting the guidance cost. Fixed distributed cases remain a serious alternative when guidance is unreliable or expensive. The PDE experiments establish neither general superiority nor error bounds at arbitrary inputs. Reopen the choice when consequential errors escape the indicator or the cost balance changes.

**Combined models versus a single replacement.** [Brunel et al., *A survey on multi-fidelity surrogates for simulators with functional outputs: unified framework and benchmark* (2025), §§3 and 6.6](https://arxiv.org/html/2408.17075v2) compares correction, mapping and fusion; its benchmark has no universal winner. **Adopt** paired correction in :4.3 and **adapt** the comparison in :4.5: retain the cheap model when its discrepancy is easier to represent than the whole response at comparable total effort. Interpolation or single-source construction can otherwise win. The functional-output results inform this branch, not the method's domain boundary. Lost features or weak correspondence reopen the choice.

**Structural restriction versus expressive universality.** [Kovachki, Lanthaler and Mhaskar, *Data Complexity Estimates for Operator Learning*, v2, introduction and main results](https://arxiv.org/html/2405.15992v2) supplies a theoretical counterweight to choosing an expressive learner first. Their general operator classes can require exponentially many examples, while more restricted approximation classes permit better rates under their assumptions. **Reject** expressive capacity as sufficient grounds for affordable construction; **adapt** the consequence in :4.1–:4.3 by reducing the target and using justified structure before expanding the learner. The results concern specified classes and access models, not the sample count for an arbitrary engineering model. Reopen the restriction when it excludes a consequential response.

For the scalar bounded case in :5.1, interpolation already answers the needed comparison with one added case and a supplied curvature bound. An operator learner or statistical uncertainty model would add assumptions and construction work without improving that answer. For coupled outputs or large response families, the retained contemporary branches can instead justify their extra cost. That difference, rather than a universal ranking of algorithms, selects the branch.

### MMP.17:12 - Relations

- **MMP.11** supplies families constrained by known relations; MMP.17 consumes them to reproduce selected source responses.
- **MMP.7 and MMP.13** supply the obtaining law and qualified inference for stochastic construction cases. **MMP.12** supplies ambiguity, stability and regularization when the replacement enters an inverse problem.
- **MMP.14** finds and repairs predictive discrepancies that can require a changed source model; a surrogate-to-source discrepancy can often be repaired within the present construction.
- **CMP.7, CMP.6 and CMP.8** supply, respectively, a learning rule with further-use conditions, iterative computation where needed, and numerical approximation or error propagation. None selects the receiving model response on behalf of the practitioner.
- **C.2.8 and EXD** distinguish recoverable structure and explanatory work from predictive agreement. **C.28.MR** supplies intervention consequences inside a stated causal model; agreement of surrogate outputs does not identify that model.
- **C.11 and C.11.CRC** compare worthwhile choices and contributions; **C.18** governs retention and Pareto-front claims; **G.5** declares a selected set when that is the needed result. **E.22 and E.23** frame and conduct improvement. MMP.17 supplies the candidate replacements and their response/error/cost consequences, not another portfolio or improvement method.

### MMP.17:End
