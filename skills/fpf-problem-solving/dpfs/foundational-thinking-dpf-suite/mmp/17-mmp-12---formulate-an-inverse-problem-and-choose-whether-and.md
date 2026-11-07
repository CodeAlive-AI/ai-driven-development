## MMP.12 - Formulate an Inverse Problem and Choose Whether and How to Use Regularization

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.12:1 - Problem frame

Use this pattern when you can predict records from a proposed state or model, but recovering the needed unknown from the records is ambiguous or too sensitive to their errors. A mixture can reveal its total while scarcely distinguishing its components. Accumulated activity can be known much more reliably than its instantaneous rate. You need to decide what can be recovered and what additional structure a usable reconstruction would impose.

Begin with the quantity the next use needs. Write how a candidate unknown would produce the recorded result, then vary the unknown in a direction that changes that quantity. If the records remain unchanged, that distinction is unidentified. If they change only slightly, calculate how their uncertainty affects recovery. Introduce regularization only when the remaining task warrants its extra assumptions.

**Regularization** constructs a controlled reconstruction by restricting candidates or discouraging selected variations. Its practical gain is a usable answer whose dependence on that restriction is visible. It can suppress error amplification while also suppressing real detail. The result may be a conditional estimate, a sufficient target bound, or a reason the requested reconstruction needs another contribution.

This is the inverse-formulation branch of mathematical modeling. It constructs the reconstruction problem and the added structure that shapes its answer. Statistical inference supplies probability claims when needed; computational methods obtain solutions to the stated problem. The examples use linear equations, norms and elementary differentiation. More difficult operators require suitable mathematical preparation or a collaborator who can supply their inverse and stability analysis. A person or AI participant still needs the subject grounds for the forward relation and the proposed restriction.

Use an adequate direct inverse when its propagated error is acceptable. If an available range or comparison already settles the receiving question, return it through C.16.IR without reconstructing every unknown. Solver implementation alone calls for the corresponding computational method.

### MMP.12:2 - Problem

Matching the data can select the wrong kind of answer. Several unknowns may produce the same records, or the best fit may follow noise in a direction the observations barely constrain. More accurate solution of those fitting equations can make the reconstruction more extreme.

Additional structure can help, but it changes the grounds of the answer. A small norm favors small unknowns in a chosen representation. A smoothness penalty favors slow variation. A learned penalty favors features represented by its training and construction. Each can remove a feature the receiving question needs.

The problem is to formulate recovery so that the required target, observation relation, error account and added selection are distinguishable, and then to determine which improvement and loss the regularization produces.

### MMP.12:3 - Forces

| Force | Tension |
| --- | --- |
| Needed target and full reconstruction | A stable total or comparison can be sufficient even when individual components are unresolved. |
| Fit and sensitivity | Exact fitting retains recorded detail, including errors amplified by inversion. |
| Additional structure and lost alternatives | A restriction can make recovery usable while excluding a consequential subject case. |
| Strong regularization and bias | Suppressing weakly observed variation reduces sensitivity but can systematically displace the target. |
| Mathematical recovery and computation | Solving the selected objective accurately does not establish that it recovers the subject quantity accurately. |

### MMP.12:4 - Solution

Construct the forward relation for the requested target, locate the consequential loss of distinction or amplification, and choose the smallest justified restriction that changes that difficulty. Formulate its strength together with the error account. Return the target with the dependence and loss introduced by that choice.

#### MMP.12:4.1 - Construct the forward relation from the modeled situation

Name the unknown x, the target q=T(x), and the records y. The unknown may be a parameter vector, a function or a collection of relations. State its domain and the units and scales used to compare changes. A target can be a total, a value at one time or a threshold; it need not be x itself.

Follow a candidate x through the modeled process and recording operation. Write the resulting ideal record as F(x,z), where z contains influential unknowns that are not the target. Keep known inputs fixed and retain shared unknowns across records. MMP.11 constructs a missing model family; C.16.MR supplies a missing measurement relation. If probabilities matter, MMP.7 constructs the recording law.

For an additive bounded-error account, one possible formulation is

`y_delta = F(x,z) + e, with ||e||_Y <= delta.`

Here delta bounds error in the chosen record norm. Use this form only when the recording procedure supports additive error. For an implicit forward relation, retain its equations and jointly unknown outputs rather than forcing it into a single-valued map. A likelihood from MMP.7 can instead supply the data discrepancy appropriate to a probabilistic account.

Include consequential uncertainty in calibration and in the forward approximation. A fixed but unknown offset remains an unknown; setting it to zero can make recovery appear better determined. A noise bound and a standard deviation have different meanings and support different conclusions.

#### MMP.12:4.2 - Locate the part that needs regularization

Use C.16.IR's compatible cases or sufficient bounds to establish what the current records and premises resolve. Reuse that result. This pattern adds the construction of a recovery rule and analysis of the rule's sensitivity.

For a linear relation y=A\*x, a change h with A\*h=0 is invisible to the records. If both x and x+h are admitted and T(x+h) differs from T(x), full recovery of that target needs another premise. If T is unchanged, the invisible direction may be irrelevant to the current use. For unknown influences, vary x and z jointly.

Next examine changes that are visible but weak. In finite dimensions, after meaningful scaling, singular values of A describe the response to orthogonal input directions. A small nonzero singular value sigma means that direct inversion multiplies the corresponding record error by 1/sigma. Estimate the effect on T, not merely on an unnecessarily detailed reconstruction. For nonlinear models, a derivative can reveal local weak directions; it does not establish global uniqueness or exclude another branch.

Distinguish poor conditioning from a discontinuous inverse. An invertible finite matrix has a continuous inverse, although its error amplification may be unacceptable. In a function-space problem, data changes tending to zero can produce target changes that do not tend to zero. The spaces and norms determine this claim; :5.3 gives an explicit example. Refining a finite discretization can expose progressively larger amplification.

If the supported target bound is already sufficient, stop. If the premises are inconsistent, return to their diagnosis through C.16.IR. A penalty cannot make an incompatible observation account true.

#### MMP.12:4.3 - Turn the added structure into a reconstruction problem

State why particular alternatives should be excluded or discouraged. A known nonnegative quantity can justify a hard domain restriction. A supported slowly varying response can justify discouraging rapid changes. A reference state can justify penalizing departure from it. When the structure is only a preference for selecting one nominal model, say so; the selected model then remains one conditional representative.

A useful variational formulation is

`(x_lambda,z_lambda) in argmin over (x,z) in C of D(F(x,z),y_delta) + lambda*R(x,z).`

C contains the hard conditions. D measures discrepancy in records. R is the regularizer: the quantity whose increase discourages a candidate. The parameter lambda controls its weight. Explain each term's subject meaning and scaling. Adding squared errors with different units, or changing units without changing the weights, changes the problem.

Choose R by deriving which variations it penalizes. For a quadratic example,

`R(x) = ||L*(x-x0)||^2.`

The reference x0 and operator L determine the preference. L=I penalizes distance from x0; a difference operator penalizes changes between neighboring values. The latter permits constant shifts unless another condition fixes them. A sparsity penalty is appropriate only when concentrating the unknown in relatively few components fits the intended representation and subject question.

For a finite, unconstrained real linear problem with scaled squared discrepancy, differentiating the quadratic objective gives

`(A^T*A + lambda*L^T*L)*x = A^T*y_delta + lambda*L^T*L*x0.`

For lambda>0 this has a unique minimizer when the null spaces of A and L intersect only at zero. Thus adding a penalty does not by itself guarantee unique recovery. Constraints and nonlinear or nonconvex choices require their own existence, uniqueness and obtaining arguments.

An alternative is to minimize R subject to a justified discrepancy ceiling. This makes the acceptable fit explicit. It can agree with a penalized formulation for suitable parameters, but the correspondence must be established for the problem being used.

A learned regularizer is another way to construct R. Its training examples and training objective supply additional structure, whose relevance to the current subject and observation conditions must be justified. Compare it with the simpler available restriction on the same required target and with its training and obtaining costs included. A visually plausible or numerically precise reconstruction can still lose the feature the target asks for.

#### MMP.12:4.4 - Select strength from the required sensitivity and tolerated loss

Work out how the added structure changes recovery before choosing its numerical strength. For L=I, x0=0 and one nonzero singular direction, quadratic regularization replaces division by sigma with multiplication by

`sigma/(sigma^2 + lambda).`

This reduces noise amplification. With exact data, it also multiplies the true component by `sigma^2/(sigma^2+lambda)`, shrinking it toward zero. A component invisible to A is selected through the regularizer, not recovered from the records.

Choose lambda using the error account and the receiving use. A bound on acceptable noise amplification, together with a bound on tolerated shrinkage, can determine an interval of useful values. Section :5.1 computes such a choice. A supported discrepancy level can instead guide a parameter search: compare each candidate's residual with the level warranted by the observation and model errors. An empirical choice rule needs evidence appropriate to its own claim; fitting the available records best is not a general parameter-selection argument.

Evaluate both sides of the trade-off. Compare the changed target when the data are perturbed within their error account and when the reference, penalty or strength changes within its justified range. Return consequential dependence rather than hiding it behind one selected value. A few numerical trials can reveal a failure; they establish a bound only when an argument covers the claimed variation.

If no supported strength gives the needed sensitivity and tolerable loss, narrow the target or return the missing contribution. A stronger penalty can make outputs nearly constant while leaving them useless for the question.

#### MMP.12:4.5 - Separate recovery error from solving error

For a linear reconstruction rule H_lambda and exact data y, the triangle inequality separates two contributions:

`||H_lambda*y_delta - x_target|| <= ||H_lambda*(y_delta-y)|| + ||H_lambda*y - x_target||.`

The first is propagated data error; the second is the displacement caused by the reconstruction rule even with exact data. Choose x_target explicitly: an identified true unknown, a specified minimum-norm solution, or another admitted target. Those are different claims. Numerical approximation adds its own contribution, which MATH.20 and CMP.8 can bound.

For a fixed regularization strength, establish only the stability supported by the formulation. A unique minimizer in a general nonlinear problem is not automatically a quantitative stability bound. If the claim concerns recovery as noise tends to zero, specify how strength and any discretization change with that noise. Fixed-strength bias may persist. Classical regularization analysis supplies conditions for this limit; the existence of a penalty is insufficient.

Keep that limit separate from iterations of a solver converging at fixed data and strength. The solver can converge to the exact minimizer of a biased problem. Conversely, early stopping can itself be a regularization choice when its stopping rule has an appropriate noise-dependent justification. Additional iterations then need not improve the subject reconstruction.

For ordinary finite use, obtain only the error or settled distinction the receiver needs. A limiting theorem need not be proved anew when an applicable result and a sufficient finite bound are available.

#### MMP.12:4.6 - Return the useful target and the choice it depends on

Return T(x_lambda) with the forward relation, consequential error assumptions and added restriction needed to interpret it. State what remains unresolved and how much the target changes under the relevant data and regularization variations. Preserve a compatible range when it is needed alongside a nominal reconstruction. A penalty-selected point alone supplies neither a confidence interval nor a posterior distribution.

Regularization changes the grounds for selecting an answer; it creates no new observation from the old records. When a different premise, observation relation or target would remove the difficulty, name that contribution. Further computation helps only if the remaining problem is computational.

A person or AI can propose the formulation, calculate the example and compare alternatives. The needed subject relation and mathematical argument must still be available from a competent participant or established result. When they are missing, return the precise question they must answer. B.5.RR carries a changed premise through the reasoning; B.5.MPC.R helps coordinate a revision spanning subject, mathematical and computational contributions.

A methodological use can take the same result back to a working method: for example, replace an unstable instantaneous-rate target by a sufficient interval total, or revise how records are obtained when a needed distinction remains invisible. Such a change is selected for the original use, not made compulsory by the presence of an inverse problem.

### MMP.12:5 - Archetypal Grounding

#### MMP.12:5.1 - Recover a split whose contrast is weakly observed

Suppose two nonnegative loads x1 and x2 have exactly known total s=3. A second channel measures a small contrast:

`d=x1-x2; z=0.01*d+e; |e|<=0.02.`

All values are expressed in fixed normalized units. The recorded z is 0.03. The inverse relations are `x1=(3+d)/2` and `x2=(3-d)/2`, so nonnegativity gives -3<=d<=3. The error account gives 1<=d<=5; jointly, the compatible contrasts are 1<=d<=3.

If the question concerns the total or whether d is positive, this already answers it. A simulation that needs one nominal split must introduce a selection. Suppose its stated reconstruction requirement is to limit the contribution of channel error to at most 1 contrast unit, while accepting at most one-half shrinkage toward balanced loads. This is a modeling preference for the nominal input, not additional evidence that the loads are equal.

Use the objective

`J_lambda(d)=(0.01*d-0.03)^2 + lambda*d^2; -3<=d<=3.`

Its unconstrained minimizer, whenever it lies in that interval, is

`d_lambda=0.01*z/(0.0001+lambda).`

The data-error contribution is bounded by `0.01*0.02/(0.0001+lambda)`. Making it at most 1 requires lambda>=0.0001. The exact-data shrinkage fraction is `lambda/(0.0001+lambda)`; making it at most one-half requires lambda<=0.0001. These two declared requirements select lambda=0.0001.

The nominal result is d_lambda=1.5, hence (x1,x2)=(2.25,0.75). Its predicted contrast record is 0.015, leaving residual 0.015 within the supplied error bound. For this fixed strength, the interior reconstruction gain is 50, compared with 100 for direct inversion. Projection onto the admitted interval cannot increase that gain.

The bias matters. If the underlying contrast were d=1 and the error e=0.02, direct inversion would return 3 and this regularized rule would return 1.5. If the underlying contrast were d=3 with e=0, the same observed record would make direct inversion correct and the regularized rule would understate the contrast by 1.5. These are two constructed compatible cases.

For a worst-case guarantee from these records, retain [1,3]. Its midpoint 2 has maximum absolute error 1 over that interval, while the selected nominal value 1.5 has maximum error 1.5. The midpoint is the better choice for that different criterion. Regularization is justified here by the declared response and shrinkage requirements, not by a claim that it improves every error criterion.

**Changed condition.** A new acquisition reports the same z=0.03 with supported error bound 0.002. The compatible interval is now [2.8,3]. Direct inversion has data-error contribution at most 0.2, already below the allowed 1. Choose the weakest penalty meeting that requirement: lambda=0 now suffices and introduces no shrinkage. It returns d=3 with the interval [2.8,3]; a receiver minimizing worst-case absolute error could instead use 2.9.

Keeping the old strength would return d=1.5 and residual 0.015, incompatible with the new error bound. The changed observation condition, not more accurate minimization of the old objective, changes the useful formulation.

#### MMP.12:5.2 - A circulation selected away by minimum norm

Three stores exchange material around a directed cycle. Let the nonnegative transfers be a from the first to the second, b from the second to the third, and c from the third to the first. Their stock changes are

`F(a,b,c)=(c-a, a-b, b-c).`

Observed zero stock changes allow every (a,b,c)=(t,t,t) with t>=0. Minimizing a^2+b^2+c^2 selects t=0. The minimizer is unique, yet a circulation of one unit gives exactly the same records. Minimum norm has supplied a nominal no-circulation choice, not evidence that no transfer occurred.

A question about net stock change is already settled. A question about gross transported amount 3\*t remains unresolved unless the subject account supplies another restriction or observation. If the stores can circulate material during unchanged stocks, using the minimum-norm answer as measured throughput would erase the quantity being sought.

#### MMP.12:5.3 - An accumulated quantity with an unstable derivative

In a continuous model on the normalized time interval [0,2\*pi], accumulated activity is N(t), and its rate is r(t)=N'(t). Consider

`N(t)=2*t; N_k(t)=2*t + sin(k*t)/k`

for positive integers k. Their maximum difference is 1/k, tending to zero. Their rates are 2 and `2+cos(k*t)`, whose maximum difference remains 1. Both accumulated curves are nondecreasing. Thus nonnegativity of the rate does not remove this instability in the maximum norm.

A justified bound on rapid rate variation, or a penalty on changes in the rate, can suppress the oscillatory alternative. It also risks suppressing a real short surge. Specify which temporal detail the receiving use needs before selecting that structure.

If the use needs only the total over this interval, both curves give 4\*pi. Recover that target from the endpoints without differentiating. For a fixed sampling interval a finite-difference inverse is continuous, but its error amplification grows as the interval shrinks; this differs from the discontinuity of the function-space inverse just exhibited.

### MMP.12:6 - Bias-Annotation

The quadratic case makes sensitivity and shrinkage calculable. It does not make quadratic penalties appropriate for every unknown. A smoothness preference can remove discontinuities; a sparsity preference depends on the representation; a learned preference can lose features absent from its construction cases.

The method treats the subject grounds of additional structure as a separate contribution. Its mathematical examples establish consequences of stated premises, not the suitability of those premises for a particular physical or organizational situation. More consequential use can require stronger subject evidence or a validated target bound; ordinary use can stop at an already sufficient comparison.

### MMP.12:7 - Conformance Checklist

- The target and forward relation are recoverable, including consequential unknown influences, units and record-error assumptions.
- Indistinguishable alternatives and error amplification are distinguished; a sufficient target is used without demanding full recovery.
- Each hard restriction or penalty has a subject justification or an explicit nominal-selection purpose. Its excluded or discouraged variation is identifiable.
- The strength choice exposes both sensitivity reduction and target loss. A changed observation condition is carried through that choice.
- Existence, uniqueness, stability, vanishing-noise recovery and solver convergence are claimed only at the scope established for the formulation.
- The returned target retains consequential dependence on added structure and the uncertainty needed for its receiving use.

### MMP.12:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A unique penalized minimizer is reported as an identified subject value. | Show which data-indistinguishable alternatives the penalty selected among; retain the selection premise. |
| A smaller residual is treated as a better reconstruction. | Compare propagated error and regularization bias for the required target, as in :5.1. |
| An old penalty is retained after the noise or forward relation changes. | Recalculate its discrepancy, sensitivity and lost target detail under the changed condition. |
| A smooth or learned reconstruction is used for a feature its construction suppresses. | Change the restriction or return the feature as unresolved; the rate surge in :5.3 shows the relevant loss. |
| A solver's convergence is offered as stability of recovery. | State the fixed computational problem solved and separately establish sensitivity or the noise-dependent limit. |

### MMP.12:9 - Consequences

The practitioner obtains a reconstruction problem with visible reasons for its additional structure. Some questions become cheaper because a stable total or bound replaces full reconstruction. Others gain a useful nominal estimate at the cost of explicitly accepted bias.

The formulation also locates a failed use: unsupported regularity, an unresolved invisible direction, an inadequate forward relation or insufficient numerical control call for different contributions. Increasing regularization or computation indiscriminately does not resolve them.

### MMP.12:10 - Architectural Rationale

The forward relation determines what the records respond to. The target determines which unresolved variations matter. Regularization determines which remaining variations the reconstruction discourages. Keeping these three contributions separate explains why one fitted answer can be useful for a nominal simulation yet inadequate as evidence about the subject.

This method extends compatible-case interpretation by constructing the recovery rule, choosing its strength and analyzing its induced loss. The distinction from computational approximation preserves the ability to solve the chosen equations accurately while still revising their recovery assumptions.

### MMP.12:11 - SoTA-Echoing

**How should a needed reconstruction be stabilized at the available accuracy?** The selected line separates propagated error from regularization bias and chooses strength for their receiving use. The serious defaults are direct inversion or least-squares fitting, and the sufficient-bound route of C.16.IR. In :5.1, elementary calculations expose the direct gain of 100 and the selected gain of 50 at comparable effort, with shrinkage as the accepted cost. The bound wins when it settles the question; direct inversion wins after the tighter observation. **Adopt** this conditional choice in :4.2–4.5 rather than a default penalty. [Clason, *Regularization of Inverse Problems*, arXiv:2001.00617v2, Chapter 4, equation (26), and Chapters 6–7](https://arxiv.org/html/2001.00617v2) supplies the mathematical error decomposition and parameter-dependent recovery line, including iterative regularization. Its operator assumptions delimit those results; it does not justify a subject penalty. Reopen the choice when a simpler recovery or bound meets the same target conditions, or when changed error or model structure defeats the selected strength.

**When can newer learned reconstruction change that choice?** **Adapt** the distinction between reconstruction fit and recovery guarantees from [Bednarski and Roith, *Introduction to Regularization and Learning Methods for Inverse Problems*, arXiv:2508.18178v1, §§1.3–1.4, 2.3 and 3.2–3.3](https://arxiv.org/html/2508.18178v1). Its mathematical treatment is a best-known-line candidate for comparing classical and data-dependent regularization: training distributions and parameter rules matter to the resulting guarantee. This changes :4.3–4.5 by retaining the added structure and its recovery conditions when R is learned. A trained replacement is a serious alternative when a simple penalty loses important structure, but requires a target-specific comparison including its extra preparation cost.

[Hertrich et al., *Learning Regularization Functionals for Inverse Problems: A Comparative Study*, arXiv:2510.01755v1, §§5.1–5.5](https://arxiv.org/html/2510.01755v1) supplies bounded rival and failure evidence: its imaging comparisons show dependence on training, task and cost, and report attractive reconstructed geometry that differs from ground truth. **Reject** transferring an imaging ranking into a general reconstruction rule. Retain its action-changing lesson in :4.3: compare the actual required feature under applicable conditions. Reopen when a learned alternative preserves that feature better at justified total effort, or when a changed observation model or subject domain invalidates the comparison.

### MMP.12:12 - Relations

- **Uses MMP.11** to construct the model family from which the forward relation is assembled, and **MMP.7** when a probability law of records is needed.
- **Uses C.16.MR** for a missing measurement relation and **C.16.IR** for compatible alternatives and sufficient target bounds. Adds regularized formulation, strength selection and analysis of induced sensitivity and loss.
- **Uses MATH.20** for error and target bounds. **CMP.6 and CMP.8** supply an iterative obtaining method or controlled approximate computation for the selected problem.
- **Supplies statistical inference** with the target, observation account and unresolved dependence on added assumptions when an estimate's probability or uncertainty is needed. **Supplies observation design** with the distinctions an additional observation would need to resolve.
- **Returns to B.5.RR and B.5.MPC.R** when the required result changes the mathematical, subject or computational contribution. C.39 can use that result to construct a missing contribution to obtaining or using observations; C.32.MWA.PP compares its working arrangement.

### MMP.12:End
