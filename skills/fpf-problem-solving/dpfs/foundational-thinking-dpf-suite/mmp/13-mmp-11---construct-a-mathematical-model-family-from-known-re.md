## MMP.11 - Construct a Mathematical Model Family from Known Relations

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.11:1 - Problem frame

Use this pattern when part of a model is supported, but a function or other relation is still unknown. You may know which quantities interact, what must be conserved, or how a response begins and ends, while lacking its form between those conditions. You need candidate models that retain this knowledge while allowing the missing contribution to vary.

Begin by locating the unknown contribution in the relations needed for the question. Say what it takes as input, what it supplies and which properties its variation must preserve. Construct a family for that contribution, then put it back into the model. For a response that rises from zero to one, a family of curves constrained by those properties gives a different starting point from an unrestricted fitted curve.

The first useful result is a family of models, its remaining adjustable parts and the restrictions introduced by its construction. It may already give a sufficient bound. When observations are available, the same construction lets you ask which functions, parameters or consequences those observations can distinguish.

You need the subject grounds for the retained relations and enough mathematics to construct and use the family, or access to that mathematical contribution. A known adequate relation can be used directly. An unknown numerical parameter inside a suitable family normally needs its estimation method. Use this pattern when the family itself needs construction or revision. B.5.FM and B.5.TU help when the missing contribution is the subject account or theory from which a relation should come.

### MMP.11:2 - Problem

A familiar formula can exclude the response being sought. Giving a learner unrestricted freedom can create the opposite problem: the fitted response may violate a known relation. Fitting two interacting contributions independently can also destroy a property that depends on their connection.

Agreement with recorded outputs leaves another difficulty. Several parameter settings may define the same function, and several functions may produce the same observations. Some receiving questions distinguish those alternatives; others need only a consequence on which they agree. Choosing one fitted instance can conceal this difference.

The modeling work is to construct the adjustable contribution in a form that retains the supported relations, then determine what that family can establish for the present question. The construction itself may impose additional restrictions, so its expressive limits belong to the answer.

### MMP.11:3 - Forces

| Force | Tension |
| --- | --- |
| Retained knowledge and flexibility | A structural relation can rule out impossible candidates; an unsupported restriction can remove the needed one. |
| Local fitting and coupled behavior | A contribution can fit its own samples while disrupting the model in which it is used. |
| Simple representation and family coverage | A small parameterization is easier to fit but can omit admissible functions. |
| Parameter recovery and useful inference | Parameters may remain ambiguous while a required consequence is determined. |
| Prediction and intervention | Two accounts can agree during observation and differ after one mechanism is changed. |

### MMP.11:4 - Solution

Locate the missing relation, separate what is retained from what may vary, construct the adjustable family, and derive its contribution to the receiving question. Observation or computation is then selected for what remains unresolved.

#### MMP.11:4.1 - Locate the contribution that may change

State the result wanted from the model. Identify the unknown relation and the quantities it connects. Keep its inputs, output, domain, units and permitted dependence explicit enough to substitute a candidate into the surrounding relations. A function of present state, a function of its history and a random response law admit different constructions. If equal proposed inputs require different deterministic outputs in the admitted circumstances, revise the inputs or retain those alternatives. Greater flexibility of a single-valued function cannot supply both outputs. For a dynamic model, A.3.3.TR supplies the corresponding reconsideration of state.

Recover the grounds and application range of the relations you retain. A balance may be required by the chosen boundary; monotonicity may hold only over one operating range; a shape assumption may be provisional. Keep an allowed discrepancy when the subject account supplies one. A convenient property is not automatically a property of the subject.

Use the smallest part that can be varied without silently changing another retained claim. If an adjustable term can absorb a known contribution, include that possibility in the inference question. Section :5.2 shows an ambiguity between two gross transfers even when their net effect is known.

#### MMP.11:4.2 - Construct the permitted variation

Translate each retained property into a mathematical condition, then choose a construction that satisfies it. MMP.10 supplies the general work of representing candidate objects and their conditions. Here the object being constructed is a family of relations to insert into the model. Direct conditions may already give a workable representation of that family. Constructing through free elements is useful when their variation should preserve the conditions; compare its obtaining and revision operations with those of the direct representation.

A useful construction separates a fixed part from free variation. If the unknown g must satisfy `L(g)=b` for a given linear operator L, find one particular solution g0 and choose a correction h with `L(h)=0`. Then `g=g0+h` retains the condition. This describes every solution only if the admitted corrections cover the whole null space in the chosen function domain. Restricting h to a few basis functions supplies a smaller family. Establish the linearity and domain before using this construction.

For a sign, bound or shape condition, construct through a map whose output has that property. Nonnegative weights can be normalized to probabilities. Integrating a nonnegative function can produce a nondecreasing response. Work out the domain and boundary of the resulting family: strict positivity excludes zeros, and an integral of an ordinary integrable function produces an absolutely continuous curve. Section :5.1 develops one such construction and its restriction.

When a property depends on coupling, construct the coupled contribution. Using the same transfer with opposite signs in two balance equations preserves their total. Two separately fitted right-hand sides have no such identity unless their joint conditions supply it. Use A.3.3.TR to assemble a change rule from the interacting relations.

A penalty during fitting offers a different construction: it discourages violations while allowing them. Use it when that allowance fits the question. If the account requires an identity, either build it into the representation or use an obtaining method that enforces it. The size of a training penalty does not by itself establish the identity.

#### MMP.11:4.3 - Choose the representation and its range

Choose a representation whose operations fit the required use and available resources. A table can represent a finite function. A basis expansion or program can retain a useful structure. A neural representation can supply a flexible adjustable function. The meaning of its inputs and outputs, and the retained relations, remain part of the model.

Check two different questions. Does every admitted parameter setting produce a relation allowed by the construction? Does the construction cover all relations needed for the present conclusion? A witness may need only one candidate; an impossibility claim over all admissible models needs coverage of that whole family or another sufficient argument.

State restrictions introduced by knots, basis functions, regularity, network architecture or domain truncation when they can change the answer. A numerical fit inside the restricted family answers for that family. If its consequence is sufficient, a more flexible family may add only cost. If the missing case matters, change the representation.

Different parameters can denote the same function. Recover the function or consequence needed by the receiving use rather than demanding unique parameters by default. Section :5.3 gives a normalization redundancy. Use MATH.7 when a change of representation has constructed inverse maps; use C.29.1 when correspondence is more general.

#### MMP.11:4.4 - Put the family into the model before using its fit

Substitute the adjustable contribution into the relations that consume it. Derive the resulting observable or answer condition with shared quantities kept shared. An error measured on an isolated contribution and an error in the coupled output are different fitting questions.

Choose the insertion point from what must remain meaningful. In a component model, inserting an unknown relation before algebraic elimination can retain a named component's inputs, outputs and connections. Adding a correction after elimination can be simpler, but the correction then acts on the transformed relations. Recover how it affects the properties needed by the original question. A reduced model may use MMP.9 to derive the contribution its simplification leaves open.

Represent how observations are produced. MMP.7 derives a probability law for records when probability is needed; C.16.IR uses the supplied indication relation to obtain compatible cases or bounds. Fitting an unobserved internal term as if it were measured supplies an extra premise. If that premise is unavailable, fit or constrain through the observable relation instead.

For a dynamic or implicitly defined model, obtain the consequence through its coupled equations and conditions. A good component fit does not settle whether the resulting evolution, initialization or constraints are usable. Apply the mathematical and computational method appropriate to the stated consequence; C.29.2 helps formulate its obtaining operation.

#### MMP.11:4.5 - Determine which remaining differences matter

Ask what the available observations constrain: the adjustable parameters, the unknown function over a stated domain, or a particular consequence. Use C.16.IR on the resulting observation relation. The function can remain undetermined away from the observed inputs even when its recorded values are fixed.

When ambiguity could change the answer, construct two admitted candidates with the same relevant observations and different receiving consequences. Such candidates show what further information must distinguish. If all compatible candidates or a sufficient bound give the same answer to the present question, use that answer without resolving unrelated differences.

Repeated numerical fits can discover alternatives. Agreement of finitely many fitted instances leaves unsearched alternatives possible. A claim of uniqueness needs its mathematical or statistical grounds; a sufficient decision can require much less. Numerical search failure also differs from a proof that the family is inconsistent with the observations.

Change the question explicitly when a new use requires it. An intervention may distinguish models with the same observational behavior. C.28.MR supplies the replacement of the affected mechanism under its causal premises. Explanation or modification of a working method can require structure beyond that needed for prediction; characterize the required explanatory use through C.2.8 and Explanation Design (EXD).

#### MMP.11:4.6 - Use the consequence or revise the family

Return the result with the family, input range and conditions that affect its use. It may be a candidate relation, a bound, a conditional prediction, a supported instruction or a located missing contribution. When the model is used to change a working method, C.32.MWA.PP receives the consequence and the conditions the proposed arrangement must preserve; MMP.22 supplies construction when the transformed mathematics does not yet yield a working rule.

Revise the part whose restriction prevents the needed result: the subject premise, permitted dependence, representation, observation relation or obtaining method. Use B.5.RR to carry a changed premise or question through the reasoning. General comparison, portfolios and improvement use the existing C.16, C.11, E.22 and E.23 methods when those questions arise.

Stop when the receiving use has a sufficient answer or the missing contribution is clear enough to obtain. Use C.11.DUA when deciding whether another observation, a richer family or further computation can improve that use enough to warrant its cost. A more detailed family is valuable only through what it enables.

### MMP.11:5 - Archetypal Grounding

#### MMP.11:5.1 - Construct a response from its known shape

A normalized input u lies in [0,1]. The subject account supports a nondecreasing response r with `r(0)=0` and `r(1)=1`. Its intermediate shape is unknown. Begin with these properties, rather than choosing a straight line as the only candidate.

Choose an integrable h with `h(u)>=0` almost everywhere and `H=integral_0^1 h(v) dv>0`. Define

`r(u)=integral_0^u h(v) dv / H`.

The endpoints follow by substitution. For `u2>=u1`, the difference is the nonnegative integral of h over [u1,u2], divided by H. Thus every member is nondecreasing. These curves are absolutely continuous. Every absolutely continuous nondecreasing response with these endpoints has such a representation using its almost-everywhere derivative, but a jump response is outside this family. The needed regularity must come from the question or remain a declared restriction.

For a small calculable family, use linear segments through (0,0), (1/4,q), (1/2,1/2) and (1,1). Their slopes are `4*q`, `2-4*q` and 1. They are nonnegative exactly when `0<=q<=1/2`. This is a construction of admissible candidates, not a conclusion from measurements alone.

Suppose observations establish only the three values at 0, 1/2 and 1. Every q in that interval agrees with them. The consequence `r(1/4)<=0.6` follows for this whole family; it also follows for every nondecreasing response with the given midpoint. There is no need to identify q for that question.

Now the receiving use asks whether `r(1/4)>0.3`. Candidates q=0.2 and q=0.4 satisfy the same observations and give opposite answers. Another repetition at the three old input values does not distinguish these ideal candidates. An observation near the disputed input may help; its precision and cost belong to that new question. Alternatively, a supported additional shape relation could narrow the family.

#### MMP.11:5.2 - Retain an exchange balance without inventing its mechanism

Two nonnegative amounts x and y exchange a conserved total N. The forward and reverse rates are unknown. Use locally Lipschitz nonnegative rate functions a(x,y) and b(x,y), defined on a neighborhood of the nonnegative states being used, and construct

`q=x*a(x,y)-y*b(x,y)`,

`x_dot=-q`, `y_dot=q`.

Adding the two equations gives zero change in x+y for every admitted a and b. At x=0, `x_dot=y*b(0,y)>=0`; at y=0, `y_dot=x*a(x,0)>=0`. With these regularity conditions the continuous-time solution preserves nonnegativity. These are properties of the coupled construction. The applicability of conserved exchange to the subject remains a premise.

Even complete knowledge of q need not identify the gross transfers. For any nonnegative locally Lipschitz h, define

`a_new=a+y*h`, `b_new=b+x*h`.

The two added contributions to q are `x*y*h` and `-y*x*h`, which cancel. The whole observed evolution is unchanged. This is an algebraic family of alternatives, not merely several successful numerical fits.

For a dimensionless instance, take a=b=1. The alternative h=1 gives `a_new=1+y` and `b_new=1+x`, yet both models have `q=x-y`. At x=2, y=1 they both predict `x_dot=-1`.

Change the question: a proposed intervention suppresses only the reverse transfer while leaving the forward rate law applicable. Under that causal premise, C.28.MR replaces the reverse contribution by zero. The first model gives `x_dot=-2`; the second gives `x_dot=-4` at the same state. Ordinary observations of x and y under the unchanged mechanisms cannot choose between these accounts. A prediction under the old operation can still be useful; the proposed intervention needs a contribution that distinguishes the mechanisms or a sufficient bound covering them.

For dimensional quantities, a and b have inverse-time units, while h has inverse-amount-inverse-time units. Restoring units prevents treating the added terms as arbitrary dimensionless corrections.

#### MMP.11:5.3 - Construct probabilities while keeping boundary outcomes

A report has three possible outcomes. Let `w_i>=0` and let their sum W be positive. Set `p_i=w_i/W`. Every candidate has nonnegative probabilities summing to one. Conversely, every probability vector on these outcomes is represented by choosing w=p. Thus this construction includes zero-probability outcomes.

The weights (0,1,3) and (0,2,6) both give probabilities (0,1/4,3/4). The parameter vector is redundant even if the probability vector becomes fully determined. There is no need to distinguish those weights when the receiving question uses only the law.

A strictly positive parameterization, such as exponentiating every finite unconstrained parameter before normalization, excludes zero probabilities. It can approximate a zero closely but cannot express it with finite parameters. If the subject account rules out the first outcome, retain that zero in the construction and normalize weights for the remaining outcomes. Whether a very small nonzero value would suffice depends on the receiving question.

The constructed p is a family member, not yet an estimate from data. MMP.7 composes it with selection, rounding or other recording behavior. The appropriate statistical method then determines what the observations support. Changing the recording procedure can change that inference without changing the underlying outcome family.

### MMP.11:6 - Bias-Annotation

Familiar formulas can turn an assumed shape into an unnoticed restriction. Flexible fitting can conceal a different commitment: the selected inputs, architecture and loss still determine which functions can be obtained. Recover those choices when they affect the receiving result.

A respected subject law can also be applied outside its range or boundary. Preserve its grounds and allowed discrepancy. If no supported structural restriction is available, an unrestricted family can be a reasonable candidate for a bounded use; further structure must earn its place through the subject question.

### MMP.11:7 - Conformance Checklist

- The unknown contribution has interpretable arguments, result, domain and permitted dependence.
- The retained relations have subject grounds and an application range.
- The construction shows why admitted adjustable values preserve the required properties.
- Restrictions introduced by representation are carried into conclusions that depend on family coverage.
- Coupled effects and the actual observation relation determine the fitting or inference question.
- Remaining parameter, function and consequence ambiguities are distinguished when they change use.
- A changed intervention or receiving question reopens the relevant contribution.
- The result can be used, qualified or passed to a named next method without requiring unrelated identification work.

### MMP.11:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Consequence | Repair |
| --- | --- | --- |
| Fit each contribution independently despite a shared identity | The fitted whole can violate the identity. | Build the shared quantity or joint condition into the family. |
| Treat a penalty as an enforced relation | A small fitting loss can conceal a consequential violation. | Match the construction and obtaining method to the allowed discrepancy. |
| Treat a finite fitted family as all admissible relations | A failure inside it becomes an unsupported impossibility claim. | State its restrictions and widen or bound the family when the question needs it. |
| Identify parameters when only a consequence is needed | Work is spent resolving distinctions that do not change use. | Apply the observation relation to the receiving consequence. |
| Transfer an observational fit to an intervention without modeling the mechanism change | Models agreeing on observed behavior can imply different intervention effects. | Construct the mechanism replacement and the alternatives it can distinguish. |

### MMP.11:9 - Consequences

The family carries usable knowledge through variation and fitting. It can supply a bound before a particular model is selected, or reveal why more observations of the same kind will leave the important ambiguity intact.

The cost is constructing and checking the representation. Strong restrictions reduce the search but can exclude useful candidates. A flexible family can retain more possibilities while increasing inference cost and leaving more uncertainty. Compare these costs against the result the work actually needs.

### MMP.11:10 - Architectural Rationale

Constructing the free part through the retained relations makes the reason for a property inspectable. A shared transfer preserves a total because the same quantity enters with opposite signs. A shape-constrained response preserves monotonicity because its increments are integrals of nonnegative values. Those reasons remain available when coefficients or learned functions change.

Separating function, representation and receiving consequence also permits economical inference. Many representations of the same function need not be distinguished. Functions that agree on the needed consequence may remain as alternatives. A new intervention can make a formerly irrelevant difference decisive.

The insertion point is therefore an architectural choice in the model. It determines what the adjustable contribution can change, which relations constrain it and which results still have the interpretation the work needs. A symbolic expression and a trained network can each participate in this construction when their mathematical role is recoverable.

### MMP.11:11 - SoTA-Echoing

**How much of the relation should be left free?** The historical [SINDy work, Brunton, Proctor and Kutz (2016), Discussion and Appendix B](https://robotics.caltech.edu/wiki/images/a/a3/BPK_PNAS.pdf), binds sparse discovery to the chosen coordinates and function library. The [universal differential equations construction, section 2.3](https://arxiv.org/html/2001.04385v4), combines retained mechanisms with an adjustable function. Sections :4.1-4.3 adopt this choice of where freedom belongs. A small fixed family can be sufficient when its restrictions fit the question. The flexible construction trades additional representation and inference work for retaining variations the small family omits.

**How should a required relation survive fitting?** For the conservation question in :5.2, :4.2 selects a shared transfer with opposite signs over independently fitted change laws for x and y with only a finite conservation penalty. The latter can fit observations while violating the required total elsewhere. The shared construction preserves that total for every admitted choice of its rate functions. Accept the extra derivation and restriction to conserved exchange in return for that identity; obtain the subject grounds for conservation first. When the question allows a specified discrepancy, a penalty or simpler approximate relation can be sufficient at lower construction cost. Carry its discrepancy into the requested consequence rather than requiring the identity anyway. Direct constraints enforcing the relation remain another option under MMP.10.

**Where does the adjustable part enter?** [Dyad's model-discovery documentation](https://help.juliahub.com/dyad/stable/analyses/udes.html) supports component-level insertion before structural simplification. [Micluta-Campeanu and colleagues (2026), sections 2.1-2.2](https://arxiv.org/html/2603.15943v1), demonstrate post-simplification correction followed by optional reduction and symbolic replacement. Section :4.4 retains both placements, chosen by their effect on the needed relations. Their thermal application supplies one use, not the scope of this method.

**What does fitting resolve?** [Loman and Baker (2025), sections 3.1, 3.3, 3.5 and B.5](https://arxiv.org/html/2510.14140), distinguish functions, parameters and predictions. Section 3.1 also constructs an algebraic compensation between an unknown function and a mechanistic parameter that preserves observed dynamics. Adopt that construction of indistinguishable alternatives in :4.5; :5.2 adapts it to coupled directional rates. Their finite fitted-ensemble comparisons in :2.4 and Appendix B can reveal alternatives, but agreement of sampled fits does not prove uniqueness over the admitted family. Constructing two admissible alternatives with different receiving consequences already establishes the consequential ambiguity, without fitting an ensemble.

Revisit the chosen family when new subject knowledge changes its restrictions, a different observation changes what is distinguishable, a new use needs a formerly discarded difference, or another construction supplies the needed result at lower cost.

### MMP.11:12 - Relations

- **MMP.10** constructs representations and the conditions making them admissible. **MMP.9** derives an unknown contribution caused by reduction and can use a constructed family to replace it.
- **A.3.3.TR** composes a rule of change; **C.29.1** relates model consequences to their receiving use; **C.29.2** constructs the needed computation.
- **MMP.7** supplies the recording probability law. **C.16.IR** determines what the resulting indication relation resolves. **MMP.8** uses the available information in a choice question.
- **C.28.MR** constructs the changed mechanism for an intervention. **B.5.RR** revises reasoning after a changed premise or question.
- **C.2.8 and Explanation Design (EXD)** characterize the explanatory contribution needed by a reader. **MMP.22** constructs the working rule from a mathematical change, while **C.32.MWA.PP** and **A.3.1.MV** compare its practical arrangement and retain its consequential variation.
- **C.11.DUA** compares a further modeling contribution with its cost; general model comparison and improvement use the existing framework methods.

### MMP.11:End
