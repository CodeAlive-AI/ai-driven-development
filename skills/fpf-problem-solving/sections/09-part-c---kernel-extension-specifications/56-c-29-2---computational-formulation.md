## C.29.2 - Computational Formulation

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative when this Method is selected; worked cases retain their stated assumptions.

### C.29.2:1 - Problem frame

**Use this when.** You know what a mathematical answer would mean, but the available expression, data and operations do not yet explain how to obtain it. An equation may characterize a solution without giving a procedure; a proposed procedure may need information its stored state has discarded; or a short calculation may expand into an unaffordable representation.

The practical question is: **What should be represented, and how will the available computation obtain an interpretable answer?** Begin with the distinction the answer must make. For example, if an executor must accept either “increment, then double” or “double, then increment”, storing only the two operation names loses a distinction: on input 3 the required answers are 8 and 7. Ordered instructions and a current position make that distinction operable.

**The object being developed** is a computational construction for a stated question: represented quantities or state, computational rules, and a way of obtaining and interpreting the requested result. *Computational formulation* names this work. The construction may leave evaluation order to a solver or describe a stochastic or continuing process. Its account can be a short derivation, pseudocode or a program with an explanation; these are ways to communicate the construction, not additional required records.

**Intended reader.** A practitioner who can state the working question and read its subject mathematics, and who needs to recover, construct or commission the computation. Elementary arithmetic and following a sequence of instructions suffice for the first case. A numerical or quantum-modeling case additionally supplies its relevant mathematical assumptions locally; developing a production solver still needs that discipline's preparation.

Computational thinking is the wider practice. This pattern covers formulation: represented inputs and state, computational rules, a way to obtain and interpret the output, and the argument and resource account needed for its use. Algorithm design, numerical analysis, programming-language design, learning and distributed computation supply deeper construction methods. This body is not a complete repertoire for those disciplines.

**Family relation.** C.29 groups methods for constructing, transferring and realizing interpretable mathematical accounts. C.29.2 contributes a computational formulation by composition and result use; it does not inherit every step or recording option of C.29. C.29.1 supplies a needed result-transfer argument. C.29.3 connects a computation with a system that prepares, performs and exposes its result. Enter this pattern directly when the working question is already available.

**First useful result.** Return a formulation with an applicable way to obtain and interpret the requested result under stated conditions, or a demonstrated obstruction and the particular construction still needed. A justified restriction, error bound or resource rejection may finish the current question.

**Ordinary non-use.** Use an already adequate local calculation or implementation directly when its inputs, operations and result are understood. Open C.29.1 for an unsettled transfer between accounts, C.29.3 for an unsettled execution correspondence, or the relevant subject method when that is the only missing contribution.

### C.29.2:2 - Problem

Knowing a condition that the answer satisfies does not always tell a practitioner how to get that answer. Writing `y = argmin f(x)` specifies a selection problem; it supplies a computation only together with a way to represent and search or otherwise solve the admitted problem. Conversely, a running procedure may return a value without establishing that it satisfies the requested condition.

Three failures make this gap expensive:

- A representation identifies cases that require different answers. No later procedure using only that representation can recover the missing distinction without another input.
- An operation such as “solve”, “update” or “sample” hides the very construction that is unavailable. Giving it a name does not make it elementary or obtainable.
- A procedure is assessed under the wrong semantics or cost model. Exact integers, fixed-width words and rounded values have different operations; a single arithmetic instruction may manipulate a growing number of bits.

The repair is to connect the requested answer to an actual construction, then follow the construction's meaning and costs. It need not start by writing software. A hand calculation, an invariant or a storage count can locate the decisive obstacle first.

### C.29.2:3 - Forces

| Force | Choice the practitioner must make |
| --- | --- |
| Answer specification and obtaining a result | Preserve what counts as an answer while finding operations that can actually produce one. |
| Sufficient state and affordable representation | Retain distinctions needed by later steps without storing the whole history by default. |
| Familiar algorithm and problem-specific structure | Reuse an understood construction when applicable; exploit special structure when its gain warrants another argument. |
| Exactness and useful approximation | Match error to the receiving question instead of treating every real number as exactly available or every approximation as adequate. |
| Transparent procedure and resource efficiency | A simple construction can be a good first answer or reference calculation even when a different implementation is needed at scale. |
| Abstract operations and executing capabilities | Let available system operations inform formulation while keeping their physical correspondence separately established. |

### C.29.2:4 - Solution

Establish how the computation obtains the requested result and why that result has the required meaning. Read the following steps as connected work with returns: an unaffordable state, an unavailable operation or a failed argument can change an earlier choice. Begin with any contribution already available.

#### C.29.2:4.1 - Specify the answer before selecting its representation

State the admitted inputs and the answer the receiver needs. Say whether the result is a value, a witness satisfying a condition, a bound, an approximation or a continuing response to inputs. These are illustrative result forms; choose the one used by the task.

Distinguish the answer condition from the proposed calculation. For a value, ask how it will be obtained. For a witness, ask how candidates will be constructed and tested. For a negative answer, ask what establishes that no admitted witness was missed. A search that eventually finds a witness need not decide the cases in which none exists.

Make an approximation requirement operational. `|y_hat - y| <= epsilon` means an absolute error bound on the requested quantity; relative error uses a different comparison and needs care near zero. A probability guarantee must state what is random and the event whose probability is bounded. Neither a small residual in a different equation nor a favorable average automatically supplies the required result.

For stochastic computation, distinguish a requested distribution, samples from it and an estimated statistic. Those outputs require different constructions and resources. For an approximate distribution, name the events, statistics or distance over which accuracy is required. A distribution's definition does not by itself supply a sampler; a sample average needs an argument connecting it with the requested population quantity.

Identify an input distinction that would change the answer. If two such inputs have the same proposed representation, retain the missing information, add an obtainable input, restrict the admitted cases, or obtain agreement to answer a weaker question. C.29.1 develops the preservation argument when that comparison is itself the difficulty.

#### C.29.2:4.2 - Choose represented state and operations together

Choose data in which the relevant next operation can be expressed. Explain what each stored value means, how an input initializes it, and how a returned value will be interpreted. The same mathematical quantity may be represented by an integer, an interval, a symbolic expression or another subject-appropriate object; the operations must match that choice.

Construct the state from what the continuation needs. In a sequential procedure this often includes a control position and intermediate values. For each proposed next step, ask what it reads, changes and preserves. If two histories reach the same stored state but require different continuations, recover the omitted condition or summary. Use A.3.3 for the underlying state-and-continuation construction; keeping every past observation is only one possible repair.

Specify the meaning of an elementary operation at the level used by the argument. An exact integer addition is different from modular word addition. A comparison of exact rational numbers is different from comparing rounded observations. If an operation is available only through another procedure, expose that dependency when its conditions or cost can change this computation.

A formulation can specify equations or constraints without choosing an evaluation order. Identify the supplied quantities or boundary conditions, admissible solutions and the output the receiver needs. An applicable solver or modeled computational process must connect those relations to obtaining a result; its execution order may remain an implementation choice. When restructuring the equations, preserve the required solutions under the stated conditions and retain expressions that recover requested quantities removed from the computational state. If no such construction is available, the equations still characterize answers and the missing way remains a task under :4.3.

The available operations can also be the starting contribution. A collaborator working under C.29.3 may supply preparable inputs, controllable changes, readable outputs and their limits for a candidate system. Use those capabilities to propose computational states and operations that can answer a useful question; do not force them into an unsuitable instruction set. Keep the physical model and the experimental or conditional basis of that contribution visible. A new computational model or language needs meanings for its expressions as well as formation rules. A.6.3.RT helps construct expressions under available notation rules; designing missing rules is separate notation or language-design work.

#### C.29.2:4.3 - Obtain the computational construction

If a known construction answers the question, recover its inputs, operative rules or steps and assumptions from its explanation and use it. B.5 supports that recovery. Check that the available operations can perform those steps and that their result has the required interpretation. A library or solver can supply the construction, but its accepted input class, result guarantee and failure behavior must fit the present use.

When the connection is not yet known, work on the missing operation rather than rewriting the output condition:

1. Calculate a small instance with enough detail to see what is being produced.
2. Identify what remains to be obtained after one available operation. Try to express that remainder using the same kind of problem or a known subproblem.
3. Retain the intermediate information needed to join the contributions. If an operation overwrites a value still needed later, save it or change the ordering.
4. State how the joined result satisfies the original answer condition, then try a case that changes a material assumption.

This is a way to expose and develop a construction, not a universal algorithm-discovery guarantee. Recurrence construction, search, optimization, numerical discretization and other techniques have their own subject methods. Use C.39 to find or develop a missing way; use C.40 when a workable change-and-test operation is already available and branching search is the live difficulty.

For a still-missing contribution, return a substantive task: the available inputs and operations, the result or intermediate relation needed, the conditions it must preserve, and what would count as a useful solution. “Find a better algorithm” is usually too weak. After a dense-state rejection, for example: “Given this circuit family and this requested observable, provide a representation and update/readout procedure with a justified error bound and a peak-memory estimate below the stated budget; do not materialize the full amplitude array in a hidden conversion.”

#### C.29.2:4.4 - Explain the result and progress

For a proposed computation, follow a small case from supplied inputs through the available construction to the interpreted output. Show the changing values or solved relations, and expose operation order when it affects the result. This catches missing state, ambiguous instruction order and an output interpreted under the wrong convention.

Then supply the argument appropriate to the claimed range. For a loop, find a statement relating the current state to the work already completed and the answer still sought. Show that initialization establishes it, each iteration preserves it, and the stopping condition makes the desired conclusion follow. This statement is the loop invariant. Separately explain why the loop reaches that condition, for example through a nonnegative integer that decreases at every iteration. For a recursive construction, explain its initial cases, the smaller calls and how their results give the caller's answer.

These are useful proof forms, not compulsory syntax for every computation. A direct finite composition may need only substitution through its operations. A randomized procedure needs its probability argument. For an estimated statistic, state the sampling assumptions and connect the claimed error or uncertainty to the sample count. For a continuing interaction, state the preservation or response property required and the assumptions under which progress is claimed; global termination may be the wrong requirement.

Keep the extent of the conclusion honest. A trace establishes that traced case. A proof using exact arithmetic establishes the stated abstract procedure under exact arithmetic. A finite precision implementation or an executing device requires the relevant additional comparison. Tests can expose failures and support selected empirical claims; a few passing tests do not prove an unrestricted input claim.

#### C.29.2:4.5 - Resolve accuracy and computational limits that affect the use

A well-defined mathematical object need not have the finite representation or uniform procedure being assumed. Ask what information the input representation actually provides and which operations are effective on it. Replacing “all real numbers” by finite strings, an evaluation oracle or a family of increasingly accurate approximations changes the computational problem. If a computability or impossibility claim matters, obtain the applicable subject argument rather than inferring it from a failed attempt.

For a finite search domain with an effective test, explicit enumeration can provide a terminating baseline. It may be too expensive, but it separates an obtainable procedure from an open construction. For an unbounded search, failure to find an answer in the allotted time leaves a different result; it does not establish nonexistence.

For numerical work, connect the stopping test to error in the requested output. Locate relevant errors in input representation, algorithmic approximation, arithmetic and output conversion. Allocate tolerance among them only under a justified rule for combining their effects. Physical-model and measurement uncertainty remain separate inputs from the relevant modeling and C.16 methods; numerical convergence does not settle them.

If finite precision can reverse a decisive comparison, increase precision, use a justified enclosure, reformulate the test or return that comparison as unresolved. If an iteration no longer changes its stored state, a limit of the ideal iteration does not show that the implementation will reach the requested tolerance. Return to the representation or stopping rule. Narrow the claim only when the narrower answer remains useful and the change is explicit.

#### C.29.2:4.6 - Calculate costs from the chosen representation

Begin with the resource that can decide the choice. For a stored array, derive how many elements the representation requires and how much storage each element occupies:

`payload storage = element count × bytes per element`.

For several simultaneously live arrays, add their payloads and the workspace, indices, temporary copies and other storage used by the proposed algorithm. Peak memory concerns what must coexist, not the total amount ever allocated. A payload lower bound may already reject a design; a payload that fits is not yet a complete fit argument.

In a model of discrete operations, count how often each operation is performed and what each performance costs. State the size parameters. An instruction count with one unit per arithmetic operation answers a different question from bit operations on growing integers, memory transfers or elapsed time on a particular machine. Explain the dominant term before using asymptotic notation. A bound for one representation is not a lower bound for every algorithm solving the mathematical problem.

A computation described by continuous dynamics may need a cost relation for duration and accuracy rather than an instruction count; obtain the relevant estimate with C.29.3.

Include input conversion, preparation computation and output production when they can dominate the result. Precomputation can be worthwhile across many uses, but say how many uses amortize it. A compact internal state does not make an explicitly requested exponential-size output cheap to enumerate.

When resources fail, change one of the actual causes: represented structure, stored precision, retained data, procedure, admitted problem class, requested answer or proposed execution resources. Recompute for the chosen alternative. An exact structural reduction, a lossy approximation and a different cost model are different changes. C.29.1 supplies a needed consequence-transfer argument; C.29.3 assesses whether the resulting execution arrangement supports the selected computation.

#### C.29.2:4.7 - Return the sufficient result and its next use

Return the formulation and its obtaining construction when available, with enough representation and output meaning to use them, the conditions of the argument, and the resource or accuracy limit that can change the decision. Reuse an existing explanation where it supplies these connections.

If a contribution is absent, identify it at the failing connection. A missing state distinction returns to formulation; an unavailable algorithm returns to its construction; an unsupported numerical bound returns to the numerical method; an execution mismatch returns to C.29.3, which may in turn supply a reason to revise this formulation. The iteration can change both model and executing arrangement.

A conditional procedure, a restricted result or an obstruction can be sufficient. Keep “no procedure obtained”, “this representation exceeds the budget”, “no algorithm exists in the stated model”, and “the implementation failed on this case” as different conclusions, each with its own basis.

### C.29.2:5 - Archetypal Grounding

The cases construct an interpreter, a bounded numerical approximation, a resource-sensitive representation, two computations from one system of relations, and a probability estimate with an error guarantee. Their conclusions follow under the stated mathematical and physical premises.

#### C.29.2:5.1 - Make calculation rules available as data

**Question.** A team must change an integer calculation without changing the executor. The input is an integer `x0` and a finite sequence `P` consisting of `n` instructions chosen from `increment` and `double`, followed by one `stop`. Other sequences are outside this procedure's admitted input class.

**Construction.** Store the ordered sequence and use mutable state `(p, x)`: the position of the next instruction and the current integer. Positions start at zero. The meaning of the output is the left-to-right composition of the arithmetic instructions applied to `x0`.

```text
p := 0
x := x0
while P[p] != stop:
    if P[p] == increment:
        x := x + 1
    else:                         # the admitted alternative is double
        x := 2*x
    p := p + 1
return x
```

This explains the elementary operations and their order. A parser or caller admitting other strings must validate the sequence or define the additional cases; it must not silently interpret an unknown instruction as doubling.

| Instructions and input | Initial state | After first operation | After second operation | Read at stop |
| --- | --- | --- | --- | --- |
| `increment, double, stop`; `x0 = 3` | `(0,3)` | `(1,4)` | `(2,8)` | `8` |
| `double, increment, stop`; `x0 = 3` | `(0,3)` | `(1,6)` | `(2,7)` | `7` |

**Argument.** After `p` arithmetic steps, `x` is the result of applying exactly the first `p` instructions to `x0`, and `0 <= p <= n`. Initialization gives the empty composition. Each branch applies the next specified operation and advances the position, preserving that statement. While an arithmetic instruction remains, `n-p` decreases by one and cannot be negative. At `p=n` the next instruction is `stop`, so the returned integer is the requested composition. With `P = [stop]`, the same procedure returns `x0` immediately.

**Cost changes with representation.** Counting one step for each arithmetic instruction and the final `stop` gives `n+1` instruction steps, apart from validation and input/output costs. That does not make arbitrary-size arithmetic constant-time. Represent the magnitude in binary and retain the sign separately. Let `b0` be the binary length of `|x0|`, counting zero as one bit. Each operation increases the magnitude's length by at most one, so the current magnitude needs at most `b0+n` bits, plus one sign bit. The position and stored program need additional space.

With simple materialized binary arithmetic that scans or copies the current digits, an arithmetic step on `b` bits costs at most proportional to `b`. Summing the growing lengths gives an arithmetic-work upper bound proportional to `n*b0 + n^2` for that implementation, before any separately material program-access costs. A representation that treats doubling differently requires another estimate. On a fixed-width integer implementation, enough increments or doublings can instead overflow; the exact-integer argument then requires a range restriction or a different realization.

**What became possible.** The executor can perform any calculation in this finite instruction class by receiving another sequence. [Turing's 1936 construction, §§5–7](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf), makes encoded computation rules available to an interpreter; this small case uses that constructive idea. Turing's universal-machine result concerns a much richer simulation construction. Adding jumps or continuing input to this case changes its progress and cost questions and requires their own argument.

#### C.29.2:5.2 - Turn a root condition into a bounded approximation

**Question and representation.** Return a rational approximation `y` to the positive root of `z^2 = 2` with `|y - sqrt(2)| <= 0.001`. The equation characterizes the root. The requested rational output still needs a way to compute it. Use exact rational arithmetic in this construction.

The initial interval is `[l,u] = [1,2]` because `1^2 <= 2 <= 2^2`. For nonnegative arguments squaring is increasing, so a comparison of the midpoint's square with 2 determines which half still contains the root.

```text
l := 1
u := 2
epsilon := 1/1000
while u - l > 2*epsilon:
    m := (l + u)/2
    if m*m < 2:
        l := m
    else:
        u := m
return (l + u)/2
```

**Meaning and argument.** The preserved statement is `1 <= l <= sqrt(2) <= u <= 2`. The square comparison preserves it, and every iteration halves the interval width. After `k` iterations that width is `2^(-k)`. The returned midpoint therefore differs from the root by at most `2^(-k-1)`. Choosing the first `k` for which this is at most `epsilon` supplies both the stopping rule and a finite bound on the iteration count for every positive requested tolerance.

| Halvings | Retained interval |
| --- | --- |
| 0 | `[1, 2]` |
| 1 | `[1, 1.5]` |
| 2 | `[1.25, 1.5]` |
| 3 | `[1.375, 1.5]` |
| 8 | `[1.4140625, 1.41796875]` |
| 9 | `[1.4140625, 1.416015625]` |

After nine halvings, return `1449/1024 = 1.4150390625`. Its error is at most `1/1024 = 0.0009765625`, which satisfies the requirement. The interval argument establishes the bound without requiring a previously calculated decimal expansion of the root.

**Resource and accuracy consequences.** There are nine midpoint-square comparisons in this case. For finer tolerances, the dyadic numerators and denominators grow; a count of comparisons alone does not include the growing cost of exact squaring. A finite precision version must preserve the bracket decisions and avoid a midpoint that rounds to an endpoint while the tolerance remains unmet. Output rounding also consumes accuracy. These are returns to arithmetic and representation choices, not evidence that the exact rational construction failed.

For a costly general continuous function, an established bracketed method using interpolation may save function evaluations. Bisection remains useful when a simple interval argument and predictable reduction are worth the extra evaluations. For a function not known to be continuous, a sign change alone does not justify this root argument. A demand for an exact finite decimal expansion of this irrational root changes the answer format to an impossible one; an exact symbolic expression or a rational approximation is a different, obtainable request.

#### C.29.2:5.3 - Count a dense state before allocating it

**Question.** Can a proposed dense numerical pure-state array for 50 qubits fit in a 64 GiB memory budget? The representation stores one complex amplitude for each binary string of length 50. There are two choices at each position, hence `2^50` entries. Stipulate 16 bytes per stored complex value: two 8-byte components.

The payload alone is:

`16 × 2^50 = 2^54 = 18,014,398,509,481,984 bytes`,

or `16 PiB = 16,777,216 GiB`, where `1 GiB = 2^30 bytes` and `1 PiB = 2^50 bytes`. Since `64 GiB = 2^36 bytes`, the payload exceeds the budget by a factor of `2^18 = 262,144`. Workspace, copies and indexing cannot reduce this payload requirement. This rejects the proposed dense allocation without building the simulator.

**The count is tied to a representation.** It says nothing by itself about the cost of every way of answering a quantum-modeling question. Using 8 bytes per amplitude halves the payload to 8 PiB and still fails this budget; it also changes numerical precision. Discarding small amplitudes requires an error argument for the requested output. Calling the representation sparse supplies no bound on the number of retained entries or on growth during its operations.

**Construct a restricted alternative.** Suppose the admitted states are products of 50 normalized single-qubit pure states, every operation is a single-qubit unitary gate, and the requested output is the probability that a named qubit is read as 1. Store the 50 pairs `(alpha_i, beta_i)` instead of the full array. The corresponding joint amplitude for bit string `s` is the product, over positions `i`, of `alpha_i` when `s_i=0` and `beta_i` when `s_i=1`.

Initialize each pair from its supplied single-qubit state. For a gate with unitary 2-by-2 matrix `U` on qubit `i`, replace just that pair by `U*(alpha_i,beta_i)`, retaining the old two values while computing both new ones. The tensor-product rule preserves the product form, and unitarity preserves the pair's normalization. For normalized pairs, return `|beta_i|^2`. The payload is now `50 × 2 × 16 = 1,600 bytes`, with additional algorithm and representation overhead to be counted separately.

Starting with all pairs `(1,0)`, apply the Hadamard operation `(a,b) -> ((a+b)/sqrt(2),(a-b)/sqrt(2))` to the first pair. It becomes `(1/sqrt(2),1/sqrt(2))`, and the requested probability for the first qubit is `1/2`. The construction uses a fixed number of complex operations per gate and stores only the pairs. Its structural factorization is exact under the admitted model; stored numerical coefficients still require their precision account.

An entangling gate can invalidate that representation. The two-qubit state with nonzero amplitudes `1/sqrt(2)` at `00` and `11` and zeros at `01` and `10` cannot be one product: nonzero `alpha_0*alpha_1` and `beta_0*beta_1` would make all four factors nonzero, contradicting a zero cross term. The product procedure must therefore reject that extension or receive a richer representation and update algorithm. Even in the product class, requesting all `2^50` amplitudes explicitly restores an exponential output count.

**First result and next contribution.** The original dense proposal is ruled out. The factorized procedure answers the separately stated restricted question; it is not a replacement for an unspecified general circuit. To continue, recover the actual input-state and gate family, requested observable or samples, and tolerated error, then obtain and cost an applicable domain algorithm. The general method supplied the count and the construction question; quantum simulation supplies the representations and update/readout algorithms.

#### C.29.2:5.4 - Obtain different computations from the same circuit relations

**Model and questions.** An ideal resistor and capacitor are connected in series to a voltage source. Let `i` flow toward the capacitor's positive plate, `v_R` be the resistor's voltage drop in that direction, and `v_C` the capacitor voltage. Use `R = 10 ohm`, `C = 0.1 F` and these relations:

```text
v_s = v_R + v_C
v_R = R*i
i = C*dv_C/dt
```

The equalities do not assign a computational direction. One question supplies the source voltage and asks for current; another supplies a desired current and asks for the source voltage. Keep the component relations while changing which quantities are given and which must be obtained.

**Voltage given: construct the trajectory and its readouts.** Take constant `v_s = 12 V` and the initial condition `v_C(0) = 2 V`. Substitute the first two relations into the third:

`dv_C/dt = (v_s - v_C)/(R*C)`.

The reduced differential state is `v_C`. Retain `v_R = v_s - v_C` and `i = (v_s - v_C)/R` as readout expressions, so eliminating those variables from the state does not remove the requested outputs.

Here `tau = R*C = 1 s`. Put `z = v_s - v_C`; then `dz/dt = -z/tau` and `z(0) = 10 V`. Thus `z(t) = (10 V)*exp(-t/tau)`: differentiation gives `dz/dt = -z/tau`, and substitution at zero gives the prescribed initial value. Recover the original quantities as `v_C = 12 V - z`, `v_R = z` and `i = z/R`. At `t = tau*ln(2)`, the exponential is `1/2`, so the returned quantities are `v_C = 7 V`, `v_R = 5 V` and `i = 0.5 A`.

**Current given: choose another computational dependency.** Now require `i(t) = 0.5 A` and keep `v_C(0) = 2 V`; the source voltage is to be found. The same relations give `dv_C/dt = i/C = 5 V/s`, hence `v_C(t) = 2 V + (5 V/s)*t`. Then `v_R = R*i = 5 V` and `v_s(t) = 7 V + (5 V/s)*t`. At `t = 0.1 s`, return `v_C = 2.5 V`, `v_R = 5 V` and the required `v_s = 7.5 V`.

Release the earlier condition `v_s = 12 V` when making `v_s` an unknown. Keeping it would contradict the new question already at `t=0`, where the relations require `v_s = 7 V`. This change chooses another computation from the model; whether a source can deliver the resulting waveform is a C.29.3 question.

**Structural reduction and numerical choice are separate.** The substitutions remove algebraic unknowns and retain their reconstruction formulas under `R,C > 0`. They do not select a time-stepping algorithm. The closed form is adequate for the constant-voltage question above. A numerical variant could instead take a forward Euler step:

`v_C_next = v_C + h*(v_s - v_C)/(R*C)`.

With `h = 0.1 s`, its first step gives `v_C_next = 3 V`, from which the readouts are `v_R = 9 V` and `i = 0.9 A`. The closed form gives `v_C(0.1 s) = 12 V - (10 V)*exp(-0.1) ≈ 2.95162582 V`; this step's voltage error is about `0.04837418 V`. Selecting a step rule and size therefore needs the requested accuracy. The exact elimination of `v_R` and `i` did not cause that time-discretization error.

**Consistent initialization is another problem.** In the voltage-given question, the prescribed `v_C(0)=2 V` and `v_s(0)=12 V` force `v_R(0)=10 V`, `i(0)=1 A` and `dv_C/dt(0)=10 V/s`. An initializer's guess `i(0)=0 A` may be replaced while finding these values. Making `i(0)=0 A` an additional required condition instead contradicts the relations. The capacitor's prescribed initial voltage represents an initial physical condition in this model. A starting guess guides numerical search; the resulting numerical approximation is assessed against the initial constraints and required accuracy.

For a larger differential-algebraic model, obtain the needed consistent-initialization, tearing or index-reduction Method from that discipline. Return the actual equations, givens, initial constraints and requested readouts with the unresolved question. A numerical initialization failure alone does not establish that the constraints are inconsistent; the contradiction in this small case follows from the displayed algebra.

#### C.29.2:5.5 - Construct a probability estimate with a specified error guarantee

**Question and available operation.** Estimate a fixed unknown probability p from independent binary observations X_1,...,X_n with the same probability p of 1. Require the procedure's probability of an error of at least 0.05 to be at most 0.05, for every p in [0,1]. The sampling operation and its independence are premises supplied to this construction; C.29.3 examines their realization.

**State and procedure.** Retain two integer counters: observations read j and ones observed s, initially zero. For each observation x, set s = s+x and j = j+1. After the selected n observations, return p_hat = s/n. The invariant is that s counts the ones in the first j observations. Thus the counters obtain the sample mean without retaining every observation.

**Choose n from the guarantee.** For a binary observation, E[X]=p and Var(X)=p*(1-p) ≤ 1/4. Independence gives E[p_hat]=p and Var(p_hat) ≤ 1/(4*n). On the event |p_hat-p| ≥ epsilon, the squared error is at least epsilon². Therefore

~~~text
epsilon² * P(|p_hat-p| ≥ epsilon)
    ≤ E[(p_hat-p)²]
    = Var(p_hat)
    ≤ 1/(4*n).

P(|p_hat-p| ≥ epsilon) ≤ 1/(4*n*epsilon²).
~~~

Taking n = 2,000 makes the bound 0.05 at epsilon = 0.05. The guarantee concerns repeated executions under the sampling model; it is not a posterior probability assigned to p after seeing one estimate. For instance, s=1,100 returns 0.55, while the guarantee still belongs to the stated procedure.

This construction consumes 2,000 observations and counter updates. Each counter needs 11 bits to represent values through 2,000; the output can be retained as the rational s/2,000. Include the cost of obtaining an observation when that cost matters. This conservative bound already supplies a finite construction; a sharper concentration argument can reduce the required observations when that saving is worth obtaining.

**Change the sampling premise.** If every read repeats one sampled bit B, then p_hat=B for every n. At p=0.5, its error is always 0.5, so the requested guarantee fails. More reads of that retained bit do not repair the construction. Obtain a sampling operation with the required independence, or recompute the error bound from the dependence actually supplied.

### C.29.2:6 - Bias-Annotation

| Bias | Correction that changes the work |
| --- | --- |
| Formula familiarity | Separate a condition on answers from the operations that obtain them; an existing executable construction can close the gap. |
| Digital-machine default | Treat supported physical operations as possible formulation inputs, while requiring a meaningful computational interpretation. |
| Exact-arithmetic default | Name representable values and operation semantics before transferring a proof to finite precision. |
| Successful-example confidence | Preserve the traced result but obtain the argument needed for a larger input claim. |
| Cheap-operation assumption | Recount when operand length, data movement or requested output size grows. |
| Representation inevitability | Reject the failed representation at its demonstrated scope; test a concrete alternative rather than claiming the problem is impossible. |

### C.29.2:7 - Conformance Checklist

Apply these checks to the computational claim being made.

| Check | What must be recoverable |
| --- | --- |
| Answer and scope | The input class, required answer and any accuracy or interaction condition; an output characterization is distinguishable from its obtaining procedure. |
| Represented distinctions | Input meaning, computational state and output interpretation, including a retained distinction that a later operation needs. |
| Available operations | What each consequential operation does and where any non-elementary construction comes from. |
| Obtaining construction | An executable ordering, an applicable solver for declared relations, another specified computational behavior, or a substantive missing-construction task. |
| Argument | A proposed computation has a worked case and the argument needed for its claimed range, including termination or response properties when claimed. An obstruction has an argument establishing its scope. |
| Accuracy | The error relation or probability guarantee used by the receiver and the arithmetic, approximation, sampling and interpretation conditions that support it. |
| Resources | The relevant element/operation counts, per-element or per-operation costs, size parameters and material preparation/readout costs. |
| Result boundary | A qualified answer, restriction or obstruction; no unsupported promotion of one trace, failed representation or simulated execution. |
| Return | The failed connection and the contribution that can change it, without requiring further work after a sufficient result. |

### C.29.2:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| “Solve the constraints” is the algorithm | Supply an applicable solver or construct the search/update procedure, with its input class and result guarantee. |
| Store only the current answer estimate | Recover the control position, bounds, pending work or other information the next operation actually needs. |
| A branch chooses an exactly known sign of an arbitrary real value | Explain how that sign is obtainable from the available representation; use a justified enclosure or return the unresolved comparison. |
| The invariant holds, so the loop finishes | Supply the separate progress argument or state the continuing behavior actually intended. |
| A tiny equation residual proves a tiny answer error | Connect residual to output error under the applicable conditioning or other subject argument. |
| One matrix operation costs one step | Expand the operation count and storage for the actual matrix dimensions and representation. |
| The dense array fails, so no simulation is possible | Retain the dense-allocation rejection; examine the needed output and an applicable alternative algorithm. |
| A smaller numeric type is an exact compression | State the changed precision and establish the error consequence. |
| A reference simulator defines what the physical system did | Retain the computational result and use C.29.3 for preparation, execution and result-reading correspondence. |

### C.29.2:9 - Consequences

The practitioner can now tell whether the computation answers the question, answers a useful restricted question, or still lacks a particular construction. Procedure recovery can expose missing information before implementation, and a representation-level estimate can reject an infeasible design before substantial resource use.

The cost is making the answer-producing connection explicit. For an ordinary small calculation this may take only a few lines. A large or delicate problem can require substantial algorithmic and numerical work; this pattern helps identify that work and connect its results, but does not remove it. Retaining a simple reference procedure may cost extra implementation effort while providing an intelligible comparison for an optimized candidate.

### C.29.2:10 - Architectural Rationale

**Why formulate around the answer and operations together?** Starting with a data structure is convenient when it already supports the required query. Otherwise it can discard the needed distinction or force an unnecessarily expensive computation. Starting only with an answer predicate has the opposite defect: it can hide unavailable operations. Connecting the two makes each choice answerable to the same use.

**Why recover a known construction before inventing another?** Its procedure and argument may already resolve the question at low cost. A new representation or specialized algorithm becomes worthwhile when a concrete input property, repeated use, precision requirement or resource limit changes the result. A direct formula, a library routine, exhaustive enumeration and a new algorithm are genuine alternatives; none wins merely by looking more formal or sophisticated.

**Why keep a simple procedure when a faster one exists?** A small exact baseline exposes meaning and can provide expected results for selected implementation tests. Bisection's interval reduction is easy to inspect; a more elaborate solver can reduce expensive evaluations. The choice depends on the present cost of evaluation and the needed guarantee. A reference calculation is not required if an already adequate construction supplies those answers.

**Why separate computability, correctness and feasibility?** A finite procedure can be correct yet exceed available memory. A fast implementation can return the wrong interpretation. A failed search can leave computability open. Distinguishing these questions makes the return useful: obtain a construction, repair its argument, choose another representation, or change the execution arrangement.

**Why allow formulation to return from realization?** Available physical operations may suggest a better computational model, and a mismatch may reveal that an assumed primitive or output is unavailable. The connected use therefore permits revising the formulation and the proposed executing arrangement together. The formulation still needs an interpretable result and a justified computational claim; the physical comparison remains a separate contribution.

### C.29.2:11 - SoTA-Echoing

**Practice question.** What is the strongest usable way to turn a stated mathematical result into a computation at the effort warranted by the task? The selected line is to reuse an applicable construction when possible, make its input/output meaning and argument explicit, and compare alternatives using the accuracy and resources that can change the answer. There is no single best algorithm across the input classes in this pattern.

#### C.29.2:11.1 - Meaning and correctness before a larger claim

The current [Dafny tutorial, “Loop Invariants” and “Termination”](https://dafny.org/latest/OnlineTutorial/guide#loop-invariants), demonstrates constructing a preserved relation to the answer and proving progress separately. **Adapt** that practice in :4.4 and :5.1: a short manual argument can establish the finite interpreter's stated semantics; a few traces cannot establish its whole input class. Mechanized checking is a serious alternative when program complexity or assurance needs justify its specification and proof effort. Reopen the choice when the procedure or required assurance becomes too large for the retained argument.

#### C.29.2:11.2 - Choose numerical methods by their guarantees and costs

The [SciPy bisection documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html) states the bracketing premises and its absolute-plus-relative termination criterion. **Adopt** explicit tolerance selection in :4.5; library defaults need not match the receiver's requirement.

[The documented Brent routine](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html) is a serious alternative combining bracketing, bisection and interpolation. **Adapt** the choice in :5.2: retain bisection for its simple bound and small exact case, while considering Brent's method when function evaluations are costly. The deliberate trade-off is a simpler argument for potentially more evaluations. Reopen for a changed function class, tolerance, evaluation cost or finite precision failure.

#### C.29.2:11.3 - Cost the represented objects, not the problem label

[Qiskit Aer's simulator documentation](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html) supplies a concrete current comparator: dense state-vector storage, alternative simulation representations, and controls that discard matrix-product-state coefficients. **Adopt** representation-sensitive counting in :4.6 and **reject** treating a truncation setting as an accuracy guarantee for an arbitrary observable. The :5.3 payload arithmetic and restricted product-state construction expose the relevant gain directly. The suitable general simulator remains unselected until the state family, operations, output and error are known. Reopen the calculation when those conditions or the actual algorithm change.

#### C.29.2:11.4 - Let executing capabilities change the formulation

[Kalita, Butler, Stepney and Kendon, *Novel models of computation from novel physical substrates: a bosonic example*, v1 (2026), §§1, 3–4](https://arxiv.org/html/2603.24531v1), develop computational concepts, a language and reference implementation from a physical-model contribution. Their bosonic example includes probability distributions in the computational meaning. **Adapt** the reverse entry in :4.2 and the return in :4.7 instead of requiring every device to implement a preselected model. This is a research Method candidate with a bosonic illustration. Section 4.7.1 explicitly leaves physical implementation for later work; its simulation does not establish device execution.

[Stepney, *Co-designing the computational model and the computing substrate* (2019), §§4–5](https://eprints.whiterose.ac.uk/id/document/1547865), proposes jointly exploring model and substrate rather than fixing one permanently. **Adapt** that reciprocal return while retaining a settled model when it already answers the use. Joint design costs a larger search; undertake it when a capability or mismatch can change the useful computation. The paper's demonstrated reservoir-characterization work does not establish the proposed general co-design process. Reopen for a useful operation excluded by the chosen model or a formulation whose required operation cannot be realized.

#### C.29.2:11.5 - Keep structural reformulation and numerical solution distinct

[ModelingToolkit's model-building reference, “System simplification” and “Exploring the results of simplification”](https://docs.sciml.ai/ModelingToolkit/stable/API/model_building/), describes reformulating equations and recovering eliminated variables through stored expressions. **Adopt** that pairing in :4.2 and :5.4. Hand substitution suffices for the small circuit; a symbolic compiler becomes useful when model size or changing equations make that work substantial.

[Its initialization tutorial](https://docs.sciml.ai/ModelingToolkit/stable/tutorials/initialization/) distinguishes required conditions from guesses and shows how changing the givens can require releasing a retained constraint. **Adapt** that distinction when parameters or initial quantities become unknowns. Consistency of an initial system and numerical success in finding its solution are different questions.

[Dyad's transient-analysis documentation](https://help.juliahub.com/dyad/stable/analyses/transient.html) separates the initial-value problem from algorithm and tolerance choices. **Adopt** that separation: structural reduction supplies a computational problem and recoverable outputs; numerical analysis supplies an appropriate solution method and accuracy argument. Reopen the affected choice when equations, initial constraints, requested outputs or accuracy change.

### C.29.2:12 - Relations

- **Member of C.29:** supplies the computational formulation used when the mathematical account does not yet provide a way to obtain its consequence. Direct entry is available.
- **Uses C.29.1 when needed:** establishes the result-preservation or bounded-transfer claim for a representation reduction or changed operation.
- **Exchanges results with C.29.3:** supplies represented inputs, operations, output interpretation and computational conditions; receives execution limits or available capabilities that can revise them.
- **Uses B.5:** recovers an available construction and its argument from an explanation, and revises dependent reasoning when premises change.
- **Uses A.3.3:** constructs sufficient state and permitted continuations, including control and retained history when required.
- **Uses A.6.3.RT:** constructs expressions under available notation rules and checks the content of a representation change. Notation- or language-design methods supply missing rules.
- **Uses C.39 and C.40 by their entry conditions:** obtains a missing way, or develops branching search when a workable change-and-test operation is available.
- **Uses subject Methods:** algorithm design, numerical analysis, symbolic computation and other computational disciplines supply their specific constructions, proofs and cost models. C.16 and physical-modeling methods supply measurement and empirical conditions when the requested result depends on them.
- **Coordinates with A.3.1, A.6.1, B.1.5 and B.1.6:** Method identity, an explicitly needed operation declaration, composition of identified Methods and resource accounting for performed Work remain under those patterns. A description of a procedure is not a claim that its execution occurred.
- **Uses C.2.1, A.10 and B.3 for the corresponding claims:** C.2.1 governs episteme identity, A.10 governs evidence use, and B.3 governs assurance of the particular result and reliance being asserted.

### C.29.2:End
