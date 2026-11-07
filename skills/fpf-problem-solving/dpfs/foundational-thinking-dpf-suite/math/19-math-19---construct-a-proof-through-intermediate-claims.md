## MATH.19 - Construct a Proof through Intermediate Claims

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.19:1 - Problem frame

Use this pattern when you have a mathematical claim to establish and some relevant definitions or results, but no argument connecting them. A calculation may suggest the answer while leaving its generality unexplained. An induction step may need information that its hypothesis does not provide. A familiar theorem may almost fit, with one missing premise.

Construct intermediate claims that connect what is available to what is required. A **lemma** is an auxiliary proved claim used in another argument. Finding a useful lemma is part of the work: its conclusion must help the next step, and its premises must be obtainable where it is used.

**First useful move:** unfold the wanted conclusion once. Ask what would suffice to establish it, and which available statement or construction could supply that condition. Try to complete this connection on an arbitrary admitted object.

The reader needs elementary mathematical statements, functions and the idea of a proof from assumptions. The worked cases explain their additional notation. The method supports arguments about numbers, functions, structures and mathematical models; each branch retains its own assumptions.

Use a supplied theorem directly when its premises are met and its conclusion answers the question. B.5.RA helps recover an existing unfamiliar argument. MATH.4 develops the inductive construction when induction is the required step; MATH.12 recovers an obtaining procedure from a proof. Here the missing contribution is the proof's construction and organization.

### MATH.19:2 - Problem

Forward calculation can produce true statements without approaching the wanted conclusion. Working backward can produce a useful-looking requirement that is stronger than the available assumptions. Combining the two requires discovering a statement that is both obtainable and sufficient for the next inference.

The difficulty can be hidden in a parameter or an order of composition. A proof for one selected object may be used as if it covered all objects; an auxiliary claim may quietly assume the theorem being proved. A recursive step can demand a result for a changed parameter even though the induction hypothesis fixes it.

The needed result is an argument with its assumptions and connections recoverable. If it cannot yet be completed, identify the remaining mathematical claim and what proving or refuting it would enable.

### MATH.19:3 - Forces

| Force | Tension |
| --- | --- |
| A conclusion guides search | A sufficient intermediate claim can itself be harder than the original target. |
| Available constructions guide inference | Many consequences of the premises do no work in the desired argument. |
| Stronger lemmas support more uses | Extra hypotheses or conclusions can make the lemma unavailable or unnecessarily difficult. |
| Local reasoning supports collaboration | A lemma can be assigned separately only when its inputs, premises and required consequence are clear. |
| Automation can complete steps | The obtained proof still has to establish the mathematical statement the work requires. |

### MATH.19:4 - Solution

**Local mantra:** recover the claim; work backward from what would suffice; work forward from what is available; construct the connecting lemma; complete the argument; use it or revise the remaining question.

#### MATH.19:4.1 - State the claim at the scope its use needs

Identify the objects, assumptions and required conclusion. Unfold a definition when doing so exposes the operation the proof needs. For injectivity of f, the task becomes: for arbitrary a and b in its domain, derive a=b from f(a)=f(b).

Keep track of which parameters are fixed and which may vary. A claim for every input requires reasoning that covers every admitted input. A temporary assumption belongs to the implication or case in which it was introduced.

Choose the kind of conclusion needed. Proving existence, obtaining a particular object and supplying a uniform effective procedure can require different contributions. MATH.12 handles extraction when the proof is expected to yield data; CMP supplies execution and cost methods when those become the next question.

When the intended statement is still unclear, first recover or change it with B.5.FM or B.5.RA. Proof construction can begin with an informal mathematical statement whose objects and inferential obligations are clear.

#### MATH.19:4.2 - Work backward to sufficient claims

Inspect how the conclusion could be established. Common entry moves include:

| Wanted conclusion | First proof obligation |
| --- | --- |
| P implies Q | Assume P for this part of the argument and establish Q. |
| P and Q | Establish both claims under the required assumptions. |
| Every admitted x satisfies P(x) | Take an arbitrary admitted x and establish P(x) without adding a special property of it. |
| Some x satisfies P(x) | Construct a suitable x and establish P(x), when a witness construction is available. |
| Two mathematical expressions are equal | Find permitted transformations or an intermediate expression connecting them. |
| A theorem's conclusion applies here | Match its objects and discharge all premises needed for that application. |

An established theorem can replace one target with several premise obligations. A proposed lemma can do the same, but remains an obligation until proved. Retain why the proposed premises would suffice: this is the connection that makes the lemma useful.

Some backward moves deliberately strengthen the task. To show that two complicated expressions have the same value, finding one common normal form may be convenient. If the stronger task becomes obstructed, return to the weaker conclusion or find another route.

#### MATH.19:4.3 - Work forward and construct the connecting lemma

From the available definitions, equations, hypotheses or objects, derive consequences likely to supply an open obligation. Apply a function to an established equality; construct an element that a definition requires; substitute a known relation; or separate cases when they give different available facts.

Compare the expressions produced with the expressions needed. Their difference often identifies the lemma: an operation must commute past a repeated operation, an equality must survive a map, or a parameter must be allowed to vary. State that relation with all operands and hypotheses.

Then ask two questions together: can the lemma be established from what is available, and does it actually complete the next inference? Test the proposed statement on a small revealing case before investing in a long argument when such a case could defeat it. MATH.6 constructs a countermodel when a false intermediary is suspected.

Use the simplest sufficient connection. If substitution and a supplied identity finish the argument, no separate named lemma is needed. If several later steps need the same derived fact, prove it once and use it with its conditions.

When an auxiliary claim asks for more than the next inference needs, try a weaker conclusion that still closes that inference. Keep the original theorem fixed, prove the weaker lemma, and check its use in the argument. For a limit argument, a bound valid from some index onward may suffice even when the same bound on every term is false.

#### MATH.19:4.4 - Change the carried claim when a step needs more

At a stalled step, inspect what it actually consumes. It may need the claim for a different parameter, an additional retained quantity, or all smaller inputs instead of only the immediate predecessor.

Strengthen or generalize the carried claim to supply that information, then recheck its starting cases and every affected step. MATH.4 develops the corresponding inductive constructor and property proof. A stronger hypothesis inside an induction argument must come from the chosen induction principle and its proved cases.

Adding a new premise is a different repair. It narrows the theorem's applicability. Check whether the receiving problem supplies that premise; otherwise the revised theorem answers a changed question. The changed commutation condition in :5.2 demonstrates this boundary.

The argument may also need a different representation. MATH.17 supplies operations on operations, and MATH.18 compares interpretations when that change can make the missing mathematical relation available.

#### MATH.19:4.5 - Assemble the argument and inspect its dependencies

Order the proved claims so that each step uses available results. State an auxiliary lemma with the hypotheses under which it was proved, then bind its variables to the objects of the receiving step.

Inspect any apparent cycle. Induction can justify use of a smaller case under its decrease condition; it cannot justify using the current theorem as an unproved premise of its own auxiliary lemma. Separate the required earlier result or change the argument.

For cases, establish the target for every admitted branch. For an implication, discharge its temporary assumption when returning to the outer argument. For a contradiction argument, retain the logical principle that turns the contradiction into the requested conclusion; extracting a witness can remain a further question.

Write enough of the completed argument for another prepared reader to recover the decisive inference. A proof assistant can check a formal derivation and its dependencies when that is useful. Compare the checked statement with the intended statement before using the result.

#### MATH.19:4.6 - Return the result to its use

A completed proof supplies its conclusion under the stated assumptions. Use that result in the next mathematical construction, model argument or algorithmic design. When a changed premise invalidates a lemma, reopen its dependent steps and retain arguments that still apply.

An incomplete proof plan can still locate useful work: name the remaining lemma, its available premises, and the step it would close. This can support another reader, a specialist or an AI agent without concealing the open part. If a counterexample defeats the claim, return it and the failed premise or implication.

An obstruction can also motivate changing an axiom or developing a conjecture. Carry the failed relation and the intended use into that new mathematical question.

### MATH.19:5 - Archetypal Grounding

#### MATH.19:5.1 - Choose the intermediate equality that proves injectivity

Let f:A->B and g:B->A satisfy g(f(a))=a for every a in A. Prove that f is injective.

Work backward from injectivity: choose arbitrary a,b in A and assume f(a)=f(b). The required conclusion is a=b. The given identity involves g(f(a)), so work forward by applying g to the assumed equality:

g(f(a))=g(f(b)).

Substitute the two given identities to obtain a=b. The intermediate equality connects the assumption to the goal; no larger theory is needed.

Now replace the given identity by f(g(b))=b for every b in B. The same proof cannot simplify g(f(a)). What it does supply is surjectivity of f: for an arbitrary b, choose a=g(b), then f(a)=b.

For a concrete separating case, take `A={0,1}`, `B={*}`, `f(0)=f(1)=*`, and `g(*)=0`. The changed identity holds, but f is not injective. The failure identifies which composite was required and produces the useful conclusion that remains. MATH.18 can use these two composites when comparing descriptions.

#### MATH.19:5.2 - Discover the lemma needed to repeat a composition

Let f and g be maps `X->X` with f composed with g equal to g composed with f. Write composition as juxtaposition, with fg meaning apply g first and then f. Define `f^0=id` and `f^(n+1)=f^n f`, and similarly for g. Prove:

`(fg)^n=f^n g^n`

for every natural n.

The base n=0 holds. At the next step, the proposed induction hypothesis gives:

`(fg)^(n+1)=f^n g^n f g`.

The target is `f^(n+1)g^(n+1)`. The difference exposes a missing lemma: `g^n f=f g^n`. This states precisely how to move f past the repeated g.

Prove that lemma by induction. At n=0 both sides are f. If it holds at n, then:

`g^(n+1)f=g^n g f=g^n f g=f g^n g=f g^(n+1)`.

The second equality uses gf=fg; the third uses the lemma's induction hypothesis. Return to the original step:

`f^n g^n f g=f^n f g^n g=f^(n+1)g^(n+1)`.

The two inductions now have separate proved responsibilities. MATH.4 supplies their general induction method; the present work found which additional statement makes the main step possible.

Remove the commutation premise. On integers, `f(x)=x+1` and `g(x)=2x` give `(fg)^2(0)=3`, while `f^2 g^2(0)=2`. The theorem has become false. Retaining the premise or retaining the actual interleaved composition are different useful responses; continuing the old rearrangement would lose the result needed by the calculation.

#### MATH.19:5.3 - Generalize a parameter to make the proof close

Suppose a finite list is built as [] or x::xs. Define append ++ in the usual way, with []++a=a and (x::xs)++a=x::(xs++a). Let [x] denote the one-element list.

Define reversal by R([])=[] and R(x::xs)=R(xs)++[x]. A second construction carries an accumulator:

T([],a)=a,

T(x::xs,a)=T(xs,x::a).

The wanted result is T(xs,[])=R(xs). Induction on xs with only this statement stalls: the recursive call uses accumulator x::[], while the hypothesis concerns [].

Generalize to every accumulator a:

T(xs,a)=R(xs)++a.

The empty-list case gives a=[]++a. For a nonempty list, the generalized induction hypothesis gives:

T(x::xs,a)=T(xs,x::a)=R(xs)++(x::a).

Using x::a=[x]++a and associativity of append, this equals (R(xs)++[x])++a=R(x::xs)++a. Append associativity itself follows by induction on its first list: the empty case is the defining rule, and the nonempty case reduces after the common leading element to the induction hypothesis.

Setting a=[] recovers the original target, using append's right-identity law. That law also follows from the same two formation cases. On [1,2,3], the accumulator states [], [1], [2,1], [3,2,1] make the changed parameter visible.

The proof establishes equality of the two list results. A claim that one implementation uses less time or storage additionally depends on its list representation and execution model. Those are computational questions for the obtained construction.

### MATH.19:6 - Bias-Annotation

A short final proof can hide the search that found its auxiliary claim. When helping another reader construct a proof, expose the expression or missing premise that motivated the lemma, as in :5.2.

Successful instances can guide that search. The universal conclusion still needs an argument covering its admitted objects; the noncommuting maps in :5.2 show why one successful calculation could miss the decisive premise.

### MATH.19:7 - Conformance Checklist

For the argument being constructed:

- The objects, variable scope, assumptions and wanted conclusion are recoverable.
- Each backward obligation has a stated implication to the claim it is meant to establish.
- Each reused or newly proved lemma has its premises satisfied at the point of use.
- A strengthened induction claim supplies the actual changed parameter or retained information, with its starting cases and step rechecked.
- Every admitted case is covered, and circular dependence is discharged by a valid argument such as induction.
- The final statement is the one the mathematical work needs; any additional applicability condition is visible.
- The result is a completed argument, a counterexample, or a particular remaining mathematical obligation with a useful continuation.

### MATH.19:8 - Common Anti-Patterns and How to Avoid Them

**Using the desired conclusion inside its supporting lemma.** If the lemma that justifies a rearrangement is proved by assuming that rearrangement, the gap remains. Prove the smaller commuting statement from its own premise, as in :5.2.

**Fixing a parameter that the next step changes.** The empty-accumulator hypothesis in :5.3 cannot be applied to a nonempty accumulator. Generalize the statement and recheck the base and step.

**Silently changing a premise to finish the proof.** Commutation makes the rearrangement in :5.2 valid. If it is absent from the intended use, state the changed theorem or retain the interleaved operation.

**Closing a different composite.** The two inverse identities in :5.1 support different conclusions. Compare the operands and order of the proved statement with the question being answered.

### MATH.19:9 - Consequences

Proof construction becomes work on smaller mathematical claims with visible dependencies. The remaining difficulty can be assigned or investigated without requiring another agent to reconstruct the entire search.

A successful argument can reveal a more reusable lemma, a changed theorem or a new construction. When the claim fails, the separating case can guide the next problem. The resulting generality follows from the proved assumptions and operations.

### MATH.19:10 - Architectural Rationale

Backward obligations expose what would suffice; forward constructions expose what can be obtained. A useful intermediate claim joins the two. This organization supports informal reasoning and formal derivations while preserving the mathematical question as the governing object.

Induction, countermodels, interpretation and witness extraction contribute different operations. The stalled inference determines which contribution the argument needs: the list example requires a varying parameter, while the composition example requires a separately proved commutation relation.

The proof plan and its completion have different uses. A plan can locate a lemma for a collaborator; a completed argument supports the mathematical conclusion. Making that distinction visible permits useful incomplete work without treating the remaining obligation as already solved.

### MATH.19:11 - SoTA-Echoing

The working question is how to construct a missing mathematical argument from available objects, assumptions and results. The selected approach combines backward proof obligations with forward derivation, then changes an intermediary or the carried claim when their connection fails.

Avigad, Lewis and van Doorn's [Logic and Proof, §3.3](https://leanprover-community.github.io/logic_and_proof/natural_deduction_for_propositional_logic.html#forward-and-backward-reasoning) gives an explicit account of the two reasoning directions and hypothesis scope. The current [Theorem Proving in Lean 4, Tactics](https://lean-lang.org/theorem_proving_in_lean4/Tactics/) shows how applying a result creates premise goals and how local intermediate claims organize a derivation. Here those contributions inform :4.1-.3/:4.5; using Lean is optional.

Tao's [mathematical research advice](https://www.math.ucla.edu/~tao/advice.html) connects progress at lemma scale with the larger problem and recommends changing the point of attack when present methods are insufficient. The pattern gives that move concrete form through a failed intermediate claim and its revised continuation.

A direct calculation or an already applicable theorem is preferable when it settles the claim with less effort. Unstructured forward manipulation becomes a poor alternative when it leaves the target unchanged; a single backward chain becomes a poor alternative when its generated premise cannot be obtained. The adopted combination changes :4.2-.4, as the missing commutation lemma and accumulator generalization demonstrate.

The sources provide construction methods and inspectable formal mechanisms. Reopen the chosen proof route when a premise changes, a lemma fails, a better theorem or representation becomes available, or the receiver needs a constructive output or execution property not yet supplied.

### MATH.19:12 - Relations

- **B.5.RA** recovers an existing argument for its next use; **B.5.FM** helps formulate an unresolved question.
- **MATH.4** constructs and justifies inductive operations, including strengthened parameters.
- **MATH.6** develops a countermodel when an intermediate or final claim may be false.
- **MATH.12** extracts the construction an argument supplies.
- **MATH.17/.18** develop operations on operations and interpretations used by a proof.
- **C.29** connects a mathematical result to its modeled subject. Computational realization and cost remain with the corresponding CMP methods.
- **B.5.QD and C.40.CD** develop the next useful question when the argument or obstruction opens one.

### MATH.19:End
