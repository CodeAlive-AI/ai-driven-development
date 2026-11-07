## MATH.21 - Construct an Object through Convergent Approximations

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.21:1 - Problem frame

Use this pattern when a number, function, infinite structure or other mathematical object is to be obtained from increasingly informative constructions, and the work needs to establish what their limit is and what can be done with it. A formula, finite prefix or finite family can describe an approximation even when the object it describes is infinite.

The governing question is what the receiving argument or operation must retain as approximation improves. Examples include a value within a tolerance, the settled first part of an infinite sequence, or a function whose integral or derivative can be obtained from approximating functions. These requests can require different notions of convergence.

**First useful move:** state one requested observation or operation on the intended object, then find a condition under which an approximation supplies it. A shrinking interval can answer a numerical tolerance request. A compatible prefix can answer a request for finitely many entries. This gives a usable result before constructing every property of the limiting object.

The reader needs elementary reasoning about functions, sequences and inequalities. The numerical case introduces its use of real completeness; the function case also uses elementary differentiation. Other spaces require the knowledge needed to state their convergence and operations.

Use an already supplied object or applicable limit theorem when it answers the question. Use the fuller method when existence, retained structure, or use of a finite approximation remains unresolved. Physical adequacy and computational realization add their own questions to the mathematical construction.

### MATH.21:2 - Problem

Finite stages can look increasingly satisfactory while leaving the mathematical result undetermined. The intended limit may be absent from the chosen space. Agreement at each fixed input may fail to control all inputs together. An operation valid on every stage may cease to be valid at the limit.

Even established convergence can leave a practical question open: which stage supplies the requested result? Conversely, a finite observation can be available before an entire limiting construction has been resolved. The method must connect the convergence claim to the particular subsequent use.

### MATH.21:3 - Forces

| Force | Tension |
| --- | --- |
| Finite access | A finite construction can supply an observation of an infinite object without exposing all its properties. |
| Choice of space | A sequence can have a limit in a larger space while lacking one among the originally admitted objects. |
| Strength of convergence | A stronger condition can preserve more operations but require unnecessary work for a weaker request. |
| Representation | Different approximation families can construct the same object; their operations must respect that identification. |
| Existence and obtaining | A theorem can establish a limit while leaving the procedure for a requested approximation unspecified. |
| Reuse | An established convergence theorem saves work when its hypotheses match the new construction. |

### MATH.21:4 - Solution

**Local mantra:** name the limiting object and its next use; construct the approximation family; choose and establish convergence; obtain the object in the admitted space; carry only the justified properties and operations; return a sufficient finite result or the remaining mathematical question.

#### MATH.21:4.1 - State what approximation must preserve

Name the space of intended objects, the approximating objects and how the latter are compared with the former. If they initially have different kinds, supply an embedding or interpretation. For example, a rational number can approximate a real number; a finite word can determine the beginning of an infinite word.

State the requested result. Does the receiver need a value, an operation on the limit, an existence theorem, or a finite observation? For a numerical use, specify the error quantity and tolerance. For a prefix use, specify which entries must be settled. The mathematical question determines the approximation requirement.

Choose a convergence notion that supports that result. In a metric space, with distance d, a sequence x_n converges to x when, for every positive epsilon, all sufficiently late terms satisfy d(x_n,x)<epsilon. For functions, pointwise convergence allows the sufficiently late index to depend on the input; uniform convergence requires one index to work for all inputs in the named set. For infinite words, convergence can mean eventual agreement on every fixed finite prefix.

These are different constructions of the convergence requirement. Use their definitions to decide what they permit. Numerical distance is useful when it measures the requested difference; finite observation or another mathematical relation can be more suitable elsewhere.

#### MATH.21:4.2 - Construct and compare the finite stages

Give the approximating rule and establish the relations on which improvement depends. For nested intervals, prove containment and decreasing width. For compatible prefixes, prove that later stages retain the earlier entries. For a series or iterative construction, obtain a bound on the unresolved remainder.

The same argument must cover the stages used by the conclusion. A finite sample can suggest a bound or expose a failure; a claimed statement about all later stages needs the corresponding argument.

When the candidate limit is not yet available, a Cauchy condition can express progress using only the approximations. In a metric space it says: for every positive epsilon there is N such that d(x_m,x_n)<epsilon whenever m and n are at least N. This compares the entire remaining tail.

If a stopping rule uses only successive changes, derive how they bound the remaining tail. Successive changes of size 1/n become small, yet their accumulated sum is unbounded. A summable bound, a contraction estimate or another proved remainder relation can make a successive-change test useful.

Retain a cheaper construction when it already supplies the requested observation. Refinement need not improve every property at every stage.

#### MATH.21:4.3 - Obtain the limit where it is needed

If a candidate object is already available, prove convergence to it by the selected definition or a suitable theorem. Otherwise use an existence result whose conditions the approximation satisfies.

For example, completeness of a metric space means that every Cauchy sequence in it has a limit there. Establishing a Cauchy condition and applying a known completeness result can obtain an object without guessing its closed form. A local existence argument may suffice even when the whole space is incomplete.

When the limit falls outside the original objects, decide whether the receiving work admits an extension. Construct the new objects and the embedding of the old ones; prove the properties the subsequent work will use. One route takes suitable Cauchy sequences as representations and identifies those whose mutual distance tends to zero. MATH.2 supplies the quotient operation: operations on equivalent representatives must produce equivalent outputs, so the quotient result is independent of the representative. The real-number construction is one instance of this route.

Establish uniqueness when the receiver needs a single result. In a metric space, if x_n tends to both x and y, the triangle inequality gives d(x,y)≤d(x,x_n)+d(x_n,y); the right side can be made arbitrarily small, so x=y. Other convergence structures need their own uniqueness condition or an explicitly retained class of possible limits.

If convergence or existence fails, return the failed condition and the still valid finite information. That can suggest a different space, a different approximation family, or a weaker requested conclusion.

#### MATH.21:4.4 - Pass properties and operations through the limit

For every operation used next, establish the relevant interchange. If F is continuous for the chosen source and target convergence, x_n→x gives F(x_n)→F(x). The argument can be local to this family; global continuity is sufficient in many cases but is more than every use needs.

Check the property actually consumed. A limit of objects in a closed subset remains in that subset. Other properties can disappear: finite words padded with zeros can converge to an infinite word with infinitely many ones.

For a function limit, distinguish a claim about its values from a claim about integration or differentiation. The required limit theorem may ask for uniform control, domination, or another hypothesis specific to the operation. In :5.3 a uniform value bound supports integration over a finite interval, but it does not support differentiating the approximations to obtain the limiting derivative.

When an interchange fails, retain the established limit and repair the affected operation. Strengthen the convergence condition, choose another family, restrict the domain, or calculate that operation by a different argument. Select the repair from the receiver's need.

#### MATH.21:4.5 - Obtain a sufficient finite result

Translate the receiving request into a condition on a stage. If an established bound gives d(x_n,x)≤e_n, a stage with e_n within the requested tolerance supplies the approximation. For nested numerical intervals, the midpoint has error at most half their width. For compatible prefixes, a stage containing all requested entries supplies them.

When execution must find that stage, provide either an obtaining rule or a recognizable stopping condition with a reason it will be reached. An explicit rate of convergence is one option. An enclosure whose width can be checked during refinement may suffice without a rate fixed in advance.

A residual is useful only through its established relation to the requested error. A small equation residual can accompany a large error in the unknown; the comparison needed by the use must connect them.

Return the approximation with the mathematical bound or settled observation it supplies. If only existence has been established, retain that result and identify the missing obtaining procedure for a computational continuation. Numerical conditioning, finite arithmetic and execution cost belong to that continuation.

#### MATH.21:4.6 - Use and revise the construction

Use the limiting object in the argument, or use the finite result for the selected observation. Keep the convergence notion and any condition needed by the next operation with that use.

A changed tolerance can require a later stage. A changed operation can require a stronger convergence result. A changed space can remove existence or uniqueness. Reopen the affected argument and retain the finite constructions and proved consequences that survive.

In modeling, interpret the resulting mathematical consequence against the subject using C.29 and the corresponding modeling method. The approximation's mathematical convergence and its ability to answer the subject question remain separately assessable.

### MATH.21:5 - Archetypal Grounding

#### MATH.21:5.1 - Obtain a real object from rational intervals

The task is to construct a positive number r with r²=2 and obtain rational approximations with a chosen absolute error.

Start with l_0=1 and u_0=2. At each step take the rational midpoint m. If m²≤2, replace the lower endpoint by m; otherwise replace the upper endpoint. Squaring is increasing on the positive interval, so each step retains l_n²≤2≤u_n². The intervals are nested and their widths are 2⁻ⁿ.

The lower endpoints form a bounded increasing sequence. In the real numbers, their supremum r exists. Each l_n≤r≤u_n: every later lower endpoint is at most u_n, and earlier ones are no larger than l_n. The shrinking width makes this r the only common point.

Both r² and 2 lie between l_n² and u_n². Since the endpoints stay between 1 and 2, the width of this squared interval is (u_n-l_n)(u_n+l_n)≤4·2⁻ⁿ. It tends to zero, so r²=2. This obtains the desired object without presupposing a square-root value to drive the construction.

After four bisections the interval is [22/16,23/16]. Its midpoint 45/32 differs from r by at most 1/32. For a smaller tolerance epsilon, choose a stage with 2⁻ⁿ⁻¹≤epsilon, or refine until the interval width is at most twice epsilon.

**Changed space.** If the result must remain rational, existence fails. In a fraction p/q in lowest terms, p²=2q² would make p even, and then q even, contradicting lowest terms. The rational approximations and their widths remain available, but they construct a real number rather than a missing rational solution. The next decision concerns admitting that extension or retaining a finite rational answer.

#### MATH.21:5.2 - Construct an infinite word and return a finite observation

Let p_n be a binary word of length n, with p_n a prefix of p_(n+1). Positions start at zero. Define b(k) to be entry k of p_(k+1). Compatibility makes that entry agree with every later prefix, so b is an infinite binary word whose first n entries are p_n.

For a common space of approximations, pad each p_n with zeros to obtain an infinite word b_n. Use convergence by eventual agreement on each finite prefix. For a request about the first m entries, every b_n with n≥m agrees there with b. This proves convergence and gives the return stage: p_m supplies those entries. Any calculation depending only on them, such as their count of ones, can use that finite result.

The global property "has only finitely many ones" does not pass to this limit. Take p_n to consist of n ones. Each zero-padded b_n has finitely many ones, but b has a one at every position. A question about a fixed finite prefix is settled; a question about the entire tail needs another argument.

The construction uses a consistency relation between finite stages and a rule for obtaining every entry. Its computational realization additionally needs a way to obtain the required p_m. Merely knowing that such prefixes exist does not supply their generator.

#### MATH.21:5.3 - Preserve values and integrals, then inspect differentiation

For n≥1, let f_n(x)=sin(nx)/n on [-1,1]. The inequality |f_n(x)|≤1/n holds for every input in the interval. Thus the functions converge uniformly to f(x)=0.

For a requested value error epsilon, n≥1/epsilon is sufficient. Integration over the interval is also controlled: the absolute integral of f_n-f is at most 2/n, by the interval length and the uniform bound. This estimate supplies an integral-error result without depending on cancellation of positive and negative values.

Now ask for the derivative at zero. Each f_n has derivative cos(nx), so f_n'(0)=1 for every n. The limit function has f'(0)=0. The value convergence therefore fails to justify passing this operation through the limit, even at that one point.

One possible sufficient repair, for differentiable functions on a common open interval, is pointwise convergence of the functions together with locally uniform convergence of their derivatives. A suitable limit theorem then identifies the limiting derivative. The present f_n fail that condition. If the construction can change, a family with controlled derivatives can support the stronger use; if it must stay fixed, obtain the derivative of its limit by another argument.

The result retains uniform convergence and its finite value and integral bounds. Only the derivative interchange has been refused. This is why the requested next operation belongs in the initial choice of approximation.

### MATH.21:6 - Bias-Annotation

Numerical examples can make convergence look like increasing decimal accuracy. The prefix case exposes another form: agreement on finitely many observations of an infinite object. Function examples show that even numerical convergence has different strengths according to the subsequent operation.

The examples use ordinary classical mathematics. An effective or constructive account must retain the obtaining information its logic and representation require. A user of a known complete space can apply its theorems directly; a constructor of a new space must establish the relevant properties of that construction.

### MATH.21:7 - Conformance Checklist

For the proposed construction:

- The intended space, approximation family and comparison between their objects are stated.
- The receiving observation or operation determines the convergence requirement.
- The general argument covers the stages claimed, including the unresolved tail when it matters.
- The limit exists in the admitted space, or the required extension is justified.
- Uniqueness and representative independence are established where the subsequent use needs them.
- Each retained property or limit interchange has its applicable condition.
- A finite return supplies the requested error or observation; an executable return has an obtaining or stopping rule.
- A failed condition leaves the remaining valid construction and a useful next question identifiable.

### MATH.21:8 - Common Anti-Patterns and How to Avoid Them

**Small increments used as a tail bound.** The harmonic increments in :4.2 shrink while their sum grows. Derive a remainder estimate before using such an increment to decide that the requested approximation has been reached.

**An absent limit treated as an object of the original space.** The intervals in :5.1 have no rational point in common. Admit the real extension or return a finite rational approximation.

**A property inherited merely because every stage has it.** Each padded word in :5.2 has finitely many ones; its limit does not. Establish preservation for the particular property.

**A value approximation used for a different operation.** The functions in :5.3 approximate values uniformly but supply the wrong limiting derivative at zero. Inspect the interchange needed by the operation.

### MATH.21:9 - Consequences

The method can obtain new objects, justify a finite use of them, and localize the reason a proposed use fails. A family can remain valuable even when one requested operation does not pass to its limit.

Changing the space, convergence relation or preserved operation can open a further mathematical problem. Those changes also create different modeling and computational possibilities, whose additional costs and subject conditions can then be compared.

### MATH.21:10 - Architectural Rationale

Approximation is a construction through a relation between stages and a result. The relation determines what information accumulates and what a finite stage can supply. This explains the common method across rational intervals, prefixes and functions without making their convergence definitions interchangeable.

Existence, identification of equivalent constructions, preservation of operations and finite return are connected tasks. Quotient construction handles identification; proof construction supplies missing implications; convergence and continuity supply the limiting passage. Keeping their contributions explicit lets a changed operation reopen the relevant mathematical step.

A stronger notion of convergence is useful when it supports a needed consequence. A weaker one is sufficient when it already supplies the receiver's observation. This permits economical use of mathematical results while preserving their conditions.

### MATH.21:11 - SoTA-Echoing

The working question is how a family of approximations supplies an object and the operations needed on it. The selected line combines a convergence relation, an existence argument in the chosen space, preservation of the required operations, and a finite-use condition.

Avigad, Lewis and van Doorn's [Logic and Proof, §§21.3-21.4](https://leanprover-community.github.io/logic_and_proof/the_real_numbers.html#constructing-the-real-numbers) develops the Cauchy-sequence quotient and completeness of the reals. Its construction informs :4.3: specify when approximation families represent the same object and make arithmetic respect that identification. An existing completeness theorem is a cheaper alternative when its space already fits; constructing a new completion is useful when a missing object prevents the intended operation.

[Mathematics in Lean, chapter 11](https://leanprover-community.github.io/mathematics_in_lean/C11_Topology.html) organizes convergence and continuity through filters, while exposing metric versions for ordinary calculations. This supports the generality of :4.1/:4.4 without requiring filter notation for every use. Mathlib's current [uniform convergence](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/UniformConvergence.html) and [limits of derivatives](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/UniformLimitsDeriv.html) give inspectable statements with different hypotheses. They inform the operation-specific repair in :5.3. Repeated numerical agreement cannot replace those hypotheses; an applicable theorem can avoid repeating its proof.

Bauer and Kavkler's [A Constructive Theory of Continuous Domains Suitable for Implementation](https://math.andrej.com/wp-content/uploads/2008/01/constructive-domains.pdf), 2008, is an implementation-oriented methodological anchor. It compares prescribed approximation rates with interval representations that test a requested width during computation, keeping the logical assumptions of that implementation explicit. The adopted contribution to :4.5 is the choice between a supplied rate and a justified stopping observation. Its particular logic and real-number implementation are alternatives for that branch, not requirements on every convergent construction.

Use the weakest established condition that supports the requested result. Reopen the comparison when the space or operation changes, when a claimed approximation cannot be obtained, or when a different representation supplies the same use with less work. These sources support the stated constructions; choosing a particular numerical algorithm remains a further task.

### MATH.21:12 - Relations

- **MATH.2** identifies equivalent representations and carries well-defined operations to their quotient.
- **MATH.19** constructs an existence, convergence or preservation argument when an intermediate implication is missing.
- **MATH.18** compares different mathematical accounts of a limiting construction.
- **MATH.22** changes assumptions when a needed limit or operation is absent; **MATH.23** develops the resulting conjecture.
- **C.29** interprets the mathematical consequence in its subject. Modeling methods choose the subject-relevant approximation and computational methods obtain its finite realization.
- **B.5.QD and C.40.CD** develop the next useful question after a construction, obstruction or changed use.

### MATH.21:End
