## MATH.23 - Develop a Conjecture by Changing a Construction

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.23:1 - Problem frame

Use this pattern when a mathematical construction works in some cases, fails after a change, or reveals a relation that could support a new theorem. You need to formulate the next claim and a way to investigate it.

A **conjecture** is a mathematical assertion proposed for investigation. Developing it includes choosing its objects, assumptions, quantifiers and conclusion. The result can become a theorem, a refuted claim, or a more useful question. Its value lies in what the answer would let someone construct, infer, explain or change.

**First useful move:** change one mathematically consequential part of the construction and compare what happens. Replace a parameter by a variable, combine two outputs, remove a used assumption, or ask the same operation to preserve another property. Try the changed construction and identify the equation, condition or obstruction that controls its result.

The reader needs the mathematical operations used by the starting construction and elementary proof reasoning. The examples explain their additional operations; the last example develops a limit argument.

Use an established result when it already answers the question. MATH.19 helps prove a sufficiently clear claim. B.5.QD develops questions more generally. Here the work develops a mathematical assertion through construction, variation, proof analysis and counterexamples.

### MATH.23:2 - Problem

A list of successful cases leaves many possible general claims. A formula can match every computed value and fail beyond them. A proposed proof can depend on a property absent from the conjecture. Conversely, a failed conjecture can reveal a useful operation or a stronger question.

The difficulty is to extract a relation that can be investigated generally. Changing a number produces another instance; changing the construction law, allowed maps or quantifier can create a new problem. The latter change needs a mathematical reason and a feasible first attack.

### MATH.23:3 - Forces

| Force | Tension |
| --- | --- |
| Examples guide invention | Their generating rule may conceal a restriction that the conjecture omits. |
| Generality increases reuse | A broader claim can lose the construction that made the original case work. |
| Counterexamples improve understanding | Excluding a troublesome case can also discard the phenomenon the work needs to understand. |
| Computation expands exploration | Search quality depends on representation, tested cases and the property being evaluated. |
| A new problem opens work | Its first attainable result can be much smaller than the eventual theorem. |
| Results and methods develop together | An answer can be useful immediately while its construction opens further questions and transfers. |

### MATH.23:4 - Solution

Start with the construction and its use. Vary an ingredient that could change the answer, formulate the suggested law and seek its mathematical grounds. A proof, a counterexample or an open question with a worthwhile next operation can each advance the inquiry.

#### MATH.23:4.1 - Recover what makes the starting construction work

Write the inputs and the operations that produce the result. Identify a relation the result satisfies and where that relation is used. Separate what has been proved from what has only occurred in inspected cases.

Look inside the operation. Repeated updates may expose a recurrence. Combining two constructions may expose closure or an order dependence. A successful quotient may reveal which distinctions can be discarded. MATH.17 helps make the operations themselves available for this investigation.

When a program supplies examples, establish what it generates and what the conjecture asserts. A tree is a graph. A generated finite tree that meets the other premises and violates the conclusion refutes a claim about every such graph. An admissible tree exhibiting the required property witnesses existence. Success on every tree would extend to every graph only through a mathematical argument covering the remaining graphs. A run on some trees supplies the results for those inputs. Use the generator in the direction the question warrants.

#### MATH.23:4.2 - Construct a variation with a reason

Choose an ingredient whose change could affect the wanted relation. Useful mathematical moves include:

| Starting opportunity | Construction of the next problem |
| --- | --- |
| Several parameter values work similarly. | Replace the parameter by a variable, derive the update rule and ask which identity holds over its domain. |
| Two outputs can be combined. | Define their combination and ask whether it remains in the same class and preserves the required relation. |
| A proof uses a special hypothesis. | Remove or weaken it, locate the affected inference and ask for a replacement condition or counterexample. |
| A desired property fails. | Isolate the obstruction and ask whether it completely characterizes failure or only gives one sufficient obstruction. |
| The result survives a change of representation. | Construct the interpretation and ask which assertions, operations and equalities it preserves. |
| An approximation supports a limiting claim. | State the order of its quantifiers and ask which operations or properties survive the limit. |

Choose a variation that the starting construction gives you reason to investigate. MATH.8, MATH.11 and MATH.13 supply symmetry or invariant reasoning; MATH.18 supplies interpretations; MATH.22 develops changed assumptions. Use their fuller methods when that mathematical contribution is needed.

Keep the original use visible. If every reading is to count equally for arbitrary group sizes, requiring equal-sized groups leaves part of that request unanswered. The construction in :5.2 repairs it. If the agreed unit is a group with equal weight, averaging the group means already answers that different request.

#### MATH.23:4.3 - State the proposed law and its answer form

Give the objects, domains, allowed operations, assumptions and proposed conclusion. State the order of the quantifiers. These statements ask different questions:

- For each input, some construction has the property.
- One construction works for every input.
- Every admitted construction has the property.

A finite pattern of results can suggest a formula. Derive it from the generating operation, a recurrence, an invariant or another mathematical relation when possible. If that derivation is missing, retain the formula as a conjecture and identify the step that would establish it.

Say what would resolve the present question. An explicit construction, a characterization of all admissible cases, a bound, or a counterexample can open different next uses. A conjectured optimal construction needs both an attainable value and an argument excluding better ones when optimality is the required conclusion.

Check whether the proposed law is already a known result under another description. MATH.18 can compare representations. An available theorem can close this question and expose a more useful next one.

#### MATH.23:4.4 - Alternate a proof attempt with revealing cases

Use MATH.19 to find intermediate claims connecting the construction to the proposed conclusion. Identify which mathematical property each step consumes. This can expose a condition that the conjecture has not yet stated.

At an uncertain step, construct a case that challenges that condition. Prefer one that distinguishes plausible accounts. To test whether a summary supports composition, find inputs with the same summary and place them in the same surrounding construction. If their required outputs differ, the summary has lost information that composition needs.

Inspect the status of a failure. A counterexample satisfying the conjecture's premises refutes the conjecture. A failure of an auxiliary lemma may leave a different proof possible. A failed program may instead concern its representation or implementation. Recover the mathematical obstruction before revising the claim.

Computational search can propose constructions and counterexamples. Check a returned candidate against the mathematical conditions that its use requires. For a finite explicit object, this may be a small complete calculation. Sampled tests of an infinite family leave its universal claim to be justified.

#### MATH.23:4.5 - Revise the claim without hiding the lost use

Use the failure to choose the next mathematical change. Three common returns are:

1. **Repair a hypothesis.** State the condition that makes the failed lemma work, prove its sufficiency and check whether the intended cases satisfy it.
2. **Repair the construction.** Retain the original problem and change the objects, representation or operation so that the required property can be obtained.
3. **Change the conclusion.** Obtain a conditional answer, bound, obstruction or weaker property that still serves a useful question.

A sufficient condition can be worth developing before necessity is known. Label that difference: a proof that uniform convergence preserves continuity does not show that every continuous limit was obtained uniformly.

A counterexample can itself become a constructive ingredient. Ask what class it belongs to, which transformations preserve its obstruction, and which related conjectures it can test. The new question can concern the method of generating cases as well as the cases themselves.

Retain the result that survived. Changing the theorem should not erase a valid construction or an earlier unresolved requirement.

#### MATH.23:4.6 - Choose a next problem and begin its mathematical work

Compare the few continuations whose answers would change further work. A useful result can supply a missing lemma, a reusable combining operation, an explanation of failure, or a method that makes another class of questions approachable. Immediate engineering application is one possible use; developing a new mathematical operation can also enable later inquiry whose destination is not yet known.

Choose a first attempt that the available contributors can perform. For a broad characterization, this might be one direction of the theorem. For an extremal problem, it might be one explicit improved construction or a bound. For a limit question, it might be the estimate needed to justify one passage to the limit.

Return what the mathematical inquiry asked for. A conjecture under development needs its basis and a worthwhile next operation. A verified counterexample can finish a request to decide whether a stated claim holds. An attainable new conjecture about a restricted class can then be worth proposing in its own right. If a characterization is due, identify the implication the counterexample settles and the part still to be established.

Use B.5.QD and C.40.CD when several questions and ways must develop together. E.10.INT helps distinguish the interest of further possible work from surprise, fame or a search score. C.36.RP supplies retention of the reconstructible method when continuing capability is at stake. Obtain further observations or checking only when their possible outcomes can change the next move enough to justify the effort.

### MATH.23:5 - Archetypal Grounding

#### MATH.23:5.1 - From repeated instances to a family of operations

Repeatedly apply `f(x)=a*x+b` over real numbers. A few calculations give:

`f²(x)=a²*x+(a+1)*b`,

`f³(x)=a³*x+(a²+a+1)*b`.

The useful next question is how to represent any number of repetitions without expanding every substitution. The conjectured formula is:

`f^n(x)=a^n*x+b*S_n`, where `S_0=0` and `S_n=1+a+...+a^(n-1)` for `n>0`.

Recover the generating rule. Applying f once more changes the coefficient of x from `a^n` to `a^(n+1)`, and the constant from `b*S_n` to `b*(a*S_n+1)`. The identity `S_(n+1)=a*S_n+1` therefore supplies the induction step. At `n=0`, `f^0` is the identity and `S_0=0`. The formula is proved for every natural n.

Now vary the problem: combine two potentially different maps `f(x)=a*x+b` and `g(x)=c*x+d`. Their composite is:

`f(g(x))=(a*c)*x+(a*d+b)`.

This constructs an operation on coefficient pairs: `(a,b)` composed with `(c,d)` gives `(a*c,a*d+b)`. The class is closed under composition. MATH.17 can study this operation; a computational method can use it to combine repetitions.

Order now becomes a useful question. Reversing the maps gives the same linear coefficient but constant `c*b+d`. Thus they commute exactly when `d*(a-1)=b*(c-1)`. This condition says when reordered operations retain the result.

The progression has produced a general iteration formula, a closed combining operation and a condition for rearrangement. A further question about vector-valued affine maps needs its matrix composition law; scalar commutation cannot be silently carried into that new setting.

#### MATH.23:5.2 - A failed combination produces a better summary and another conjecture

A computation stores the arithmetic mean of each nonempty list of real numbers. The required whole is their concatenation, in which each occurrence counts. The proposed combining operation takes the mean of those means. For groups [0] and [2,4], it returns (0+3)/2=1.5, while the combined group has mean 2.

Inspect the missing mathematical relation. For a group of size n with exact arithmetic mean a, the sum is n·a. A zero mean fixes the sum at zero for every admissible size. With a nonzero mean, two possible sizes give different sums. For two such lists with means a, b and sizes n, m, the pooled mean is (n·a + m·b)/(n + m). The simple mean of a and b gives the same answer when the sizes are equal or the means are equal. Relative sizes suffice for the weighted mean. To combine arbitrary lists repeatedly, retain a summary that carries their weights.

Retain a sum s and count n. Combine (s,n) and (t,m) as (s+t,n+m), then return (s+t)/(n+m) when n+m>0. Associativity and commutativity follow from those of addition in both coordinates; (0,0) is an identity. Thus grouping and order of the combination do not change the final mean in real arithmetic. A finite-precision implementation needs its own error account.

The construction opens a broader mathematical question: **Which summaries permit the summary of a combined input to be computed from the two summaries alone?**

Let q map a collection of finite lists, closed under concatenation, to proposed summaries; let ++ concatenate lists. Means and medians here use nonempty lists, while sum and count also admit the empty list. A necessary condition is:

if q(u)=q(u') and q(v)=q(v'), then q(u++v)=q(u'++v').

It is also sufficient for defining a combining operation on attained summaries: choose lists representing the two summaries and apply q to their concatenation. The condition makes the result independent of those choices. This proves mathematical existence of the operation. Computing it from a concrete representation of the summaries still needs an effective rule. MATH.2 develops the compatible identification; MATH.12 and CMP handle obtaining the operation.

For means alone, take u=[0], u'=[0,0], and v=v'=[6]. The input summaries match, but the concatenated means are 3 and 2. The necessary condition fails. Sum and count repair it by an explicit operation.

Now ask whether median and count suffice. Take u=[0,1,100] and u'=[-100,1,2]. Each has count 3 and median 1. Append the same list [50,50]. The resulting five-element medians are respectively 50 and 2. This new conjecture is refuted by the same method.

The next useful problem concerns what more to retain. Sorted full lists are sufficient and can be merged, while a use requiring less storage can ask for a restricted input class or an approximate median with a stated error. The mathematical obstruction now informs a computational and modeling choice.

#### MATH.23:5.3 - A failed limit argument reveals a stronger condition

Consider the claim that a pointwise limit of continuous real functions is continuous. On `[0,1]`, let `f_n(x)=x^n` for positive natural n. Each function is continuous. At any fixed `x<1`, `x^n` tends to zero; at `x=1` it equals one. The limit f is zero below one and equals one at one, so it is discontinuous.

Locate the failed proof step. Pointwise convergence lets the approximation index depend on x. Continuity near a point needs control over nearby x together. Choosing a good approximation at the one point alone does not control its neighborhood.

This suggests a sufficient condition: **uniform convergence**. For every positive error allowance, one index makes all later approximations close to f at every point of the domain.

Work the proposed repair. Fix a point x0 and an error allowance e>0. Choose N so that the approximation error between f_N and f is less than e/3 everywhere. Continuity of f_N gives a neighborhood of x0 in which the difference between f_N(x) and f_N(x0) is less than e/3. The triangle inequality bounds the difference between f(x) and f(x0) by these three errors, hence by e. This proves continuity of f at x0.

The repaired theorem supplies a condition for transferring continuity. Here proof analysis discovered which quantifier change made the desired inference possible. A subsequent limit construction can use the proved condition to retain continuity.

Uniformity is sufficient, not necessary. On the domain `[0,1)`, the same `x^n` sequence has the continuous limit zero, but convergence is not uniform: for every n there is an `x<1` with `x^n=1/2`. The next question can therefore seek a weaker condition suited to the receiving use.

### MATH.23:6 - Bias-Annotation

Small examples are chosen to expose a relation and permit a full calculation. In a larger inquiry, simple generators can miss structures with different behavior. Change the generating rule or inspect a contrasting class when that difference could defeat the proposed claim.

A solved or famous problem can attract attention while its reusable mathematical contribution remains unclear. Recover the construction and the questions it opens. Choose the next problem for the work it can enable and the contributions available.

### MATH.23:7 - Conformance Checklist

For the conjecture being developed:

- The starting construction, established result and receiving use are recoverable.
- A mathematical change explains why the new question arises.
- Objects, domains, hypotheses, quantifiers and answer form distinguish the proposed claim.
- If a proof is attempted, its needed intermediate relations are exposed; any case used to investigate the claim tests a consequential condition.
- A counterexample is classified at the claim, lemma or implementation it defeats.
- A changed hypothesis, construction or conclusion has an explicit consequence for the requested mathematics. A result about a subclass can settle the earlier question when the inference carries back to that question.
- The grounds have the reach the claim requires. A single admissible counterexample refutes a universal statement. A proof for the full class, including an exhaustive finite argument where applicable, can establish it.
- If further work is selected, its first attainable operation and the earlier construction it needs are recoverable. A supported answer can finish the question already posed.

### MATH.23:8 - Common Anti-Patterns and How to Avoid Them

**Extrapolating the displayed values without the generating law.** The iteration formula in :5.1 is justified by its recurrence and induction. Agreement at a few n values alone would leave other continuations possible.

**Narrowing the inputs or changing how they combine.** The pooled mean in :5.2 must work for lists of unequal size. Sum and count compose under concatenation. A request for the mean over distinct subjects in overlapping rosters uses set union. Adding the two sums and counts would give extra weight to the subjects present in both.

**Treating a convenient condition as necessary.** Uniform convergence repairs the continuity argument in :5.3. The final countercase shows why necessity remains a different claim.

**Losing the operation behind a successful answer.** Keeping only the mean hides the combining structure. Retaining sum and count makes later aggregation possible; retaining the compatibility argument supports the next summary question.

### MATH.23:9 - Consequences

A result becomes material for developing another mathematical problem. A failure can yield a condition, a construction or a new object of study. A success can reveal a family of operations and a way to transfer the result.

The method can stop with a well-formed conjecture and first attempt. Completing its proof, obtaining a computational procedure, learning the method and applying it to a physical subject have their own requirements.

### MATH.23:10 - Architectural Rationale

B.5.QD locates a consequential next question. The mathematical contribution here is to construct its proposed law: expose composition and closure, change a quantifier, characterize a compatible identification, or isolate a premise through proof analysis. The cases show how these operations produce statements that can be proved or refuted.

MATH.17/.18, MATH.19/.22 and the other mathematical patterns supply the operative constructions. This pattern assembles them around the development of a conjecture. A case can close with a new question, an answer, or a further obstruction.

A correct answer and a reusable method have related but different uses. Retaining the derivation, allowed transformations and failed conditions permits another prepared contributor to adapt the work and formulate its next problem.

### MATH.23:11 - SoTA-Echoing

The working question is how to develop a mathematical conjecture from constructions and their failures, with a useful route into further work.

**Adapt proof analysis.** Lakatos's [Proofs and Refutations, Appendix 1](https://www.cambridge.org/core/books/abs/proofs-and-refutations/another-casestudy-in-the-method-of-proofs-and-refutations/AF9D68A35602B7F8F1409DF3E56C5D7B) connects counterexamples to the hidden lemmas and concepts in an attempted proof. The adopted move changes :4.4-.5: inspect the failed inference and consider a revised condition or construction. It improves on simply excluding the offending example when that exclusion abandons the intended class. The method can require more work than proving a fixed, adequate claim; use the latter route when its premises and conclusion already serve the inquiry. Lakatos supplies a method for developing the conjecture; its use can still leave the conjecture unresolved.

**Adapt construction search and generalization.** Georgiev, Gómez-Serrano, Tao and Wagner's [Mathematical exploration and discovery at scale, §§1.3-1.6 and 4](https://arxiv.org/html/2511.02864v3) distinguishes search for constructions from finding a program or formula that generalizes, and describes transitions to proof. It also reports evaluator defects and the limits of the tested search methods. This informs :4.1/:4.3-.4: inspect the generator and evaluator, recover a general construction, then establish the claim its use needs. Compared with direct object search, program search can retain reusable structure but adds generation and evaluation cost. A cheap direct search or existing theorem can be preferable.

**Retain methods as a usable result.** The [Math and AI declaration of 11 September 2026](https://mathandai.org/) argues that counting solved problems can obscure understanding and transmission of methods. Adopt that question in :4.6 and the relation to C.36.RP: preserve what another prepared contributor needs to change and use the construction. The construction-to-proof account above supplies a concrete alternative involving AI contributors.

Reopen the route when a new counterexample changes the admitted class, another representation makes the conjecture simpler, or the receiver needs a result the present construction cannot provide. Improved search tools change the means and cost of investigation; they leave the proposed mathematical assertion and its possible use to be stated.

### MATH.23:12 - Relations

- **B.5.QD and C.40.CD** develop questions and obtaining ways across practices; this pattern supplies the mathematical conjecture-forming contribution.
- **MATH.17/.18** supply operations on constructions and interpretations between accounts.
- **MATH.8/.9/.11/.13** supply symmetry, selection and invariant methods that reveal general relations or obstructions.
- **MATH.19/.6/.22** supply proof construction, countermodels and changed axioms.
- **MATH.2** supplies the compatible identification used by composable summaries.
- **C.29 and MMP** interpret the mathematical result for a subject; **CMP** supplies effective search, construction and execution when needed.
- **E.10.INT** helps assess interest in further mathematical work and **C.36.RP** helps keep methods available. **C.40.OCN** connects a proposed use with its conditions. **C.40.JD** connects a way of working with the capability of its performer and the support it needs. **HCD** supplies methods for human capability development.

### MATH.23:End
