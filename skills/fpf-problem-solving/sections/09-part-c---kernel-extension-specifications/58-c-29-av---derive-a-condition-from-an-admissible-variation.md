## C.29.AV - Derive a Condition from an Admissible Variation

> **Type:** Method
> **Status:** Draft
> **Normativity:** Normative

### C.29.AV:1 - Problem frame

Use this pattern when you have a candidate allocation, shape, history or other mathematical construction under constraints, and need to find an improving change or a condition that an optimum or stationary construction must satisfy.

For example, two allocations obey the same resource limit, but it is unclear how moving some resource between them changes the criterion. Or a proposed physical history has fixed endpoints, and you need to find what its action principle requires of the motion between them. In both cases, construct changes that preserve the relevant constraints, calculate their effect and determine the strength of the resulting conclusion.

The subject of the Method is a family of admissible mathematical candidates and the change of a stated scalar quantity over that family. A *variation* is a specified change within the family; *admissible* means that the changed candidate satisfies the conditions retained for this question.

The first useful result is an improving candidate, a necessary condition, a justified minimum or maximum, or a located obstacle to obtaining one. A necessary condition can narrow a search even when it does not settle the optimum.

The reader needs the candidate, its constraints, the quantity being compared and the mathematical operations used to calculate its change. Elementary algebra is enough for the allocation example. The history example additionally uses differentiation and integration. A specialist can supply a construction or theorem at the step where that preparation is needed.

If an available evaluation of a few fixed alternatives already answers the question, use that comparison. This Method is useful when constructing the allowed changes or reasoning from them is the difficulty.

### C.29.AV:2 - Problem

Changing one value independently can leave the allowed set. A derivative calculated in that direction can then recommend an impossible change. Even with admissible directions, a zero first derivative can describe a maximum, a saddle point or a flat comparison; further reasoning is needed for a minimum.

The reverse difficulty occurs at a constraint boundary: an optimum can have a nonzero derivative because the improving direction is unavailable. A calculation that discards the allowed parameter range loses that conclusion.

These errors share a missing connection between what can vary, what the variation does to the quantity and what the examined family establishes about the original question.

### C.29.AV:3 - Forces

| Force | Tension |
| --- | --- |
| Preserved conditions | A convenient change is easy to calculate, but it must retain the constraints used by the conclusion. |
| Local information | A first-order change can expose a useful direction cheaply; stronger conclusions can require finite changes, further terms or a theorem. |
| Coverage | A small family can reveal an obstruction, while a claim about every candidate needs a reason that the family or argument covers them. |
| Form of the candidates | Discrete choices, smooth vectors and histories support different kinds of variation. |
| Use of the result | A mathematical improvement can guide a decision or a model construction; its application still depends on the meaning of the criterion and constraints. |

### C.29.AV:4 - Solution

**Construct an admissible family → calculate the change → derive the condition → establish what it settles → use or revise the result.**

#### C.29.AV:4.1 - Fix the comparison

State the candidate, the conditions to retain, the scalar quantity and the conclusion sought. Write the candidate as `x` and the quantity as `J(x)` when that notation helps. For minimization, smaller values of J are preferred; for maximization, reverse the comparisons below.

Keep the meaning of J visible. It might be a supplied allocation cost, an approximation error or a physical action functional, which assigns a number to a history. A physical principle can require stationarity of an action without selecting its minimum. Recover that principle and its conditions before using the variational calculation to describe physical behavior.

Distinguish a search for one improving change from a claim of local or global optimality. Local optimality concerns a specified neighborhood of the candidate; global optimality concerns all candidates admitted by the problem.

#### C.29.AV:4.2 - Construct changes that remain admissible

Build a family `x(h)` with `x(0)=x`. State the allowed values of the parameter h and substitute the family into the constraints. The parameter may be a scalar, a vector or a discrete choice.

For a fixed total `x1+x2=b`, the change `(x1+h, x2-h)` preserves the total. If both components must stay nonnegative, its range is `-x1 <= h <= x2`. A further capacity limit can shorten that range.

For a history with fixed endpoint values, try `q_h(t)=q(t)+h*eta(t)`, where eta vanishes at both endpoints and has the regularity required by the functional. Check any additional path constraint as well.

A direction tangent to a constraint may preserve it only to first order. At `(1,0)` on the unit circle, `(1,h)` has squared length `1+h^2` and leaves the circle whenever h is nonzero. The curve `(cos(h),sin(h))` stays on it. Use an admissible curve for a finite comparison, or keep a tangent calculation at the first-order scope its mathematical argument supports.

When a useful family cannot yet be constructed, the missing result is concrete: a parameterized change that retains the named constraint. Obtain the corresponding mathematical construction rather than continue with an inadmissible substitute.

#### C.29.AV:4.3 - Calculate the effect of the variation

Form the difference

`DeltaJ(h) = J(x(h)) - J(x(0)).`

Substitute the whole changed candidate, including dependent values. Simplify enough to determine the sign or magnitude relevant to the question.

For a differentiable comparison with a scalar parameter h near zero, write

`DeltaJ(h) = a*h + r(h), with r(h)/h -> 0,`

when that expansion is justified. The coefficient a is the first variation along this family. Higher-order terms or a bound on the remainder can be needed when a vanishes, or when choosing a finite step.

A derivative tells how sufficiently small changes behave under its limit assumptions. To select a particular step, check the finite difference or a bound that covers that step. For a discrete family, compare its admissible members directly; differentiability is not an entry requirement.

If the calculation uses a numerical approximation, relate its error to the sign or comparison being used. C.29.2 develops that computational task. A difference interval entirely below zero can establish improvement for minimization; an interval spanning zero leaves that comparison unresolved.

#### C.29.AV:4.4 - Derive a condition with the allowed directions

For minimization, an admissible h with `DeltaJ(h)<0` supplies an improvement. For a local conclusion, use families whose candidates approach the base candidate as h approaches zero, under the neighborhood notion of the problem.

At a local minimum, a differentiable family allowing sufficiently small changes of both signs must have `a=0`: a positive or negative a would give a decrease in one of those directions. If only small nonnegative h are allowed, the necessary condition is `a>=0`. For other parameter domains, test the directions actually available.

When a is zero, inspect the remaining change. The differences `h^2`, `-h^2` and `h^3` all have zero derivative at zero but respectively give a minimum, a maximum and neither on a two-sided neighborhood. This distinction changes whether the candidate is selected, rejected or needs a stronger argument.

For a vector of variation parameters, keep their joint constraints. Checking one coordinate at a time can miss an improving combination.

#### C.29.AV:4.5 - Establish the reach of the conclusion

Say which candidates the family reaches and which conclusion the calculation proves.

If every admissible candidate can be represented by a member of the family, and `DeltaJ(h)>=0` throughout its allowed domain, the base candidate is a global minimizer. If equality occurs only for the base candidate, it is the unique minimizer. An argument restricted to a neighborhood establishes the corresponding local result.

A narrower family can still supply an improving candidate or a necessary condition. Extending that condition to a stronger conclusion requires coverage of the relevant variations or an applicable sufficiency theorem. A convexity argument can sometimes supply the latter; recover its hypotheses before using it. Repeated failure of a chosen local move supplies no general global-optimality guarantee.

For a physical action, derive the stationarity condition required by the physical model. Establish a minimum only if the functional and allowed histories support that stronger conclusion. The free-history example below does so by a nonnegative finite difference.

#### C.29.AV:4.6 - Return the result to the working question

Use the obtained change or condition in the calculation, model or decision that needed it. Keep the admissible family and the reason for the conclusion in the explanation so another practitioner can alter the comparison.

When a criterion changes, recalculate its difference. When a constraint changes, rebuild the parameter domain or family first. B.5.RR helps revise the dependent reasoning while retaining what remains valid.

The mathematical comparison can be completed before any physical change is performed. B.5.MPC supplies the return to physical interpretation and use. If the question is whether an actual intervention causes a result, C.28 supplies the causal-use question.

Stop at the result sufficient for the current use. An improving feasible candidate can be enough to continue; a demand for the global optimum calls for the stronger argument.

### C.29.AV:5 - Archetypal Grounding

#### C.29.AV:5.1 - Reallocate a fixed total, then change the criterion

Allocate ten divisible units between two uses: `x1>=0`, `x2>=0` and `x1+x2=10`. The supplied cost is `J=x1^2+x2^2`. Take the admissible family `(x1+h,x2-h)`, with `-x1<=h<=x2`.

Substitution gives

`DeltaJ(h)=2*(x1-x2)*h+2*h^2.`

For an interior candidate, both signs of small h are allowed. The first-order condition gives `x1=x2`, hence `(5,5)`. At this candidate, the entire finite difference is `2*h^2`. Every feasible allocation is `(5+h,5-h)` for `-5<=h<=5`, so this proves the unique global minimum, with cost 50.

Now change the cost to `J=x1^2+2*x2^2`, retaining the total and nonnegativity. The same family gives

`DeltaJ(h)=2*(x1-2*x2)*h+3*h^2.`

The condition becomes `x1=2*x2`, giving `(20/3,10/3)`. Its difference is `3*h^2` across the whole feasible interval, so its cost `200/3` is the unique minimum. Keeping the earlier equal split would miss the change introduced by the new criterion.

If the units must instead be whole, x1 and x2 are integers. Completing the square gives `J=3*(x1-20/3)^2+200/3`; the admissible integer closest to 20/3 is 7. Thus `(7,3)` has the lowest cost, 67, in that discrete problem. The continuous stationary point helped locate the candidates; the integer comparison settles their use.

Keep the weighted cost `J=x1^2+2*x2^2`, make the units divisible again, and add `x1<=6` while retaining the total and nonnegativity. The previous continuous minimizer `(20/3,10/3)` is now unavailable. At `(6,4)`, the allowed family has `-6<=h<=0` and

`DeltaJ(h)=-4*h+3*h^2>=0.`

This family covers every newly feasible allocation. Thus `(6,4)`, with cost 68, is the unique global minimizer despite its nonzero derivative along the unrestricted line. The parameter domain carries the decisive information.

These are calculations for the stated cost model. Its use in an allocation decision requires the supplied cost to represent the consequence being compared.

#### C.29.AV:5.2 - Compare histories between fixed endpoints

Consider a one-dimensional free particle with mass `m>0`, elapsed time `T>0`, and fixed positions `q(0)=0`, `q(T)=L`. The model's action is

`J[q] = integral from 0 to T of (m/2)*(qdot(t))^2 dt.`

Take the straight history `q0(t)=L*t/T`. For any continuously differentiable eta with `eta(0)=eta(T)=0`, construct `q_h(t)=q0(t)+h*eta(t)`. Expanding the square gives

`DeltaJ(h) = (m*h*L/T)*integral eta_dot(t) dt + (m*h^2/2)*integral eta_dot(t)^2 dt.`

The first integral is `eta(T)-eta(0)=0`. The remaining term is nonnegative, and it vanishes for a changed history only when its derivative change is identically zero; the fixed endpoints then force the change itself to vanish. Every continuously differentiable history with these endpoints can be expressed as q0 plus such a change. The straight history therefore uniquely minimizes this functional over that class.

The construction exposes the reason: the fixed endpoints remove the cross term, while every remaining velocity deviation adds a nonnegative contribution.

Now include a restoring potential. In dimensionless variables, use the harmonic-oscillator action `J[q]=integral from 0 to 2*pi of (qdot^2-q^2)/2 dt`, with `q(0)=q(2*pi)=0`. At the history `q=0`, every admissible family `q_h=h*eta` has zero first variation. Yet the admissible directions `eta=sin(t/2)` and `eta=sin(3*t/2)` give respectively `DeltaJ=-3*pi*h^2/8` and `DeltaJ=5*pi*h^2/8`: integration uses `integral eta^2 dt=pi` and `integral eta_dot^2 dt=n^2*pi/4` for these directions with n=1 and n=3. Arbitrarily small changes of both lower and higher action are available. The stationary history is therefore a saddle, not a minimum.

Changing an endpoint condition also requires rebuilding the allowed histories before reusing the free-particle argument. Its vanishing cross term depended on both endpoint values.

This example uses a supplied classical model. Constructing an appropriate action for an unfamiliar physical system is a further physical and mathematical modeling task.

### C.29.AV:6 - Bias-Annotation

A convenient coordinate can make some changes easy to express and hide others. State what the chosen family reaches before treating its result as a property of all candidates.

A modeler can also import minimization from an allocation problem into a physical action principle. Recover whether the subject requires improvement, an extremum or stationarity; the same variation calculation supports different conclusions under those premises.

For a search procedure, separate a failure to find a better local move from a proof about the full feasible set. This matters when discrete choices or disconnected regions prevent the chosen family from reaching other candidates.

### C.29.AV:7 - Conformance Checklist

| Question | Passing result |
| --- | --- |
| What is being compared? | The candidate, retained conditions, scalar quantity and sought conclusion are stated. |
| Which changes are allowed? | Substitution or another applicable argument establishes the family's admissibility and parameter domain. |
| What does the change do? | The difference, first variation or bounded numerical comparison is obtained for that family. |
| Which directions matter? | Boundary and joint-parameter constraints remain in the sign or stationarity argument. |
| How strong is the conclusion? | The reached candidate class and the argument distinguish improvement, necessity, local optimality and global optimality. |
| What follows in use? | The receiving calculation or decision can use the result, or the missing construction is located. |

### C.29.AV:8 - Common Anti-Patterns and How to Avoid Them

| Observed or text-invited mistake | Repair |
| --- | --- |
| Vary each allocation independently while retaining a fixed-total claim. | Couple the changes so the total remains fixed and derive their allowed range. |
| Use a tangent displacement as a finite feasible move on a curved constraint. | Construct a feasible curve or retain only the first-order conclusion supported by the tangent argument. |
| Accept a zero derivative as a minimum. | Determine the remaining change or use a sufficiency theorem with its hypotheses. |
| Reject a boundary optimum because its unrestricted derivative is nonzero. | Test the available one-sided or constrained changes. |
| Apply a small-step sign to an arbitrarily large step. | Calculate the finite difference or bound the remainder over that step. |
| Declare global optimality after testing one restricted family. | Supply the missing coverage or limit the conclusion to that family. |

### C.29.AV:9 - Consequences

A constrained comparison becomes a reusable calculation. It can expose a feasible improvement, reduce an optimization problem to a condition or explain why a proposed change cannot help.

The main effort is constructing a useful admissible family and establishing the sign over the range needed by the conclusion. The Method permits an early useful result; full optimization is a larger task when the working question demands it. Keeping the family and argument makes later changes of criterion or constraints easier to handle.

### C.29.AV:10 - Architectural Rationale

The admissible family, change calculation and conclusion are separated because each can fail independently. A correct difference can describe impossible candidates. An admissible comparison can yield only a necessary condition. A strong mathematical result can still use a criterion that does not answer the practitioner's question.

Finite differences provide the direct comparison whenever they are manageable. Derivatives expose local structure economically, and sufficiency theorems can extend that information under additional hypotheses. Keeping these routes connected lets the reader use the least machinery that obtains the needed result.

The same construction spans a resource allocation and a continuous history. What carries across is the preservation of conditions and reasoning from the resulting change. The cost model and the physical action retain their different origins and uses.

### C.29.AV:11 - SoTA-Echoing

For a constrained comparison, the selected approach is to construct feasible changes before interpreting their effect. Direct substitution is useful for small expressions; differential conditions and numerical optimization become useful as the candidate class or calculation grows. The choice depends on the result needed and the assumptions available.

[Boyd and Vandenberghe, *Convex Optimization*, §4.2.3](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=153) gives the differentiable convex case: the gradient's inner product with every feasible displacement characterizes optimality. Adopt its attention to the feasible set and the hypotheses that make a first-order condition sufficient. The Method above also admits nonconvex and discrete comparisons, where that sufficiency cannot be inherited. Specialized convex formulations and algorithms remain useful external constructions when their inputs fit.

[Tong, *Classical Dynamics*, §2.1](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) develops variations of a history with fixed endpoints and the resulting Euler-Lagrange equations. Adopt the explicit endpoint conditions and the distinction between stationary action and a minimum. This is an established classical source; it supplies neither an action for every new physical system nor its empirical justification.

C.29 supplies the mathematical interpretation and return, while C.29.2 supplies computational formulation and error-sensitive use. Here the reusable contribution is construction of the admissible family and the argument from its change. If those operations require a specialized variational, optimization or physical-modeling technique, recover that technique at the point where the needed result becomes specific.

Revisit the construction when constraints, regularity, candidate class or the required conclusion change. A newer solver can improve cost without changing the meaning of the admissibility and optimality claims.

### C.29.AV:12 - Relations

- **C.29** connects the mathematical candidates and conclusion to the original subject and working question.
- **C.29.1** establishes the transfer of a result when a change of representation could lose a relevant distinction.
- **C.29.2** constructs a computation and relates numerical error to the comparison being used.
- **B.5.RC and B.5.RA** help recover a needed mathematical construction or argument; **B.5.RR** revises dependent reasoning after a premise changes.
- **B.5.MPC** connects the physical account, mathematical construction, computation and use. **C.28** handles a causal consequence attributed to an intervention.

### C.29.AV:End
