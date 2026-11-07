## MATH.11 - Construct an Invariant from Transformation Rules

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.11:1 - Problem frame

Use this pattern when a mathematical construction can take many steps and you need a relation that survives every allowed step. Such a relation can rule out a proposed result, constrain a search or derive a formula for a quantity that the steps accumulate.

Here an **invariant** is a function whose value is unchanged by each allowed transformation. The method constructs that function from the transformations. It starts with a small family of expressions, derives conditions on their coefficients and uses the resulting expression in a proof. Conserved weighted totals, polynomial relations and residues provide different ways to carry out that construction.

**First useful move:** write one allowed change, substitute it into a candidate expression and calculate what changes. Derive coefficient conditions that make the change vanish, then include the remaining allowed rules. Once preservation holds for them all, compare the invariant at the starting and proposed states.

The reader needs substitution, elementary algebra and the arithmetic used by the example. The polynomial branch uses collection of like terms and linear equations; the residue branch explains arithmetic modulo two. An available invariant can be used directly after checking that it fits the allowed transformations. When a short explicit sequence already answers the question, constructing an invariant may add no useful result.

### MATH.11:2 - Problem

Trying more sequences can leave a reachability question unresolved. A proposed formula may hold in the first few calculations but fail at a later step or a different branch. Guessing that an unweighted total stays constant can also fail when a rule replaces two units of one kind with three of another.

The difficulty is to obtain a relation from the actual rules and explain why it survives sequences of arbitrary finite length. A useful relation must then answer the question: a constant function is always preserved, but cannot distinguish a reachable proposal from an impossible one.

The result is a constructed invariant with its preservation argument and a consequence for the stated task. A failed search within the chosen expression family can instead identify a reason to change that family or try another method.

### MATH.11:3 - Forces

| Force | Tension |
| --- | --- |
| Short calculation and unbounded sequences | One substitution can establish what every step preserves, but only when it covers all allowed steps. |
| Simple expression and useful distinction | A small expression family is cheap to search, while its invariants may leave the target question undecided. |
| Mathematical rule and implementation | Integer, real and modular arithmetic can preserve different expressions under similar-looking updates. |
| Necessary condition and construction | Different invariant values prove impossibility; equal values can leave ordering and enabling conditions unresolved. |
| General preservation and one starting state | An identity valid for every input is reusable, while a particular reachable set can satisfy further relations. |
| Stable reasoning and changed operations | A changed start may require only a new value; a changed transformation can invalidate the preservation proof. |

### MATH.11:4 - Solution

**Specify the transformations → choose expressions → derive preservation equations → solve and verify → use the invariant → revise the affected part.**

#### MATH.11:4.1 - Specify the states, steps and requested consequence

Let X be the mathematical state set, and write x → y when one allowed step takes x to y. Retain every condition that enables a step and every component of the state that its calculation uses. A rule may be given as y=T(x) with a condition on x, or as a relation allowing several possible successors.

Name the initial state a and the target question. You may need to exclude a particular state b, derive the value of an accumulated quantity after a stated number of steps, or restrict the candidates worth searching.

For an invariant I, the required preservation statement is:

`x → y implies I(y)=I(x).`

It concerns each allowed step. When several rules or branches are available, each needs that equality. If X describes an external process, establish the correspondence between the mathematical steps and that process through C.29.

#### MATH.11:4.2 - Choose a small expression family

Look at what the transformations add, remove or combine. For states represented by counts x1,...,xn, try a weighted total:

`I(x)=w1*x1+...+wn*xn`.

The unknown weights let different kinds contribute differently. For additive changes x → x+d, the change in that total is `w1*d1+...+wn*dn`.

If the update combines variables or changes an accumulated sum, try a few expressions suggested by those operations. For example, an update containing n can make n² useful because `(n+1)^2-n^2=2*n+1`. Write a candidate as `I(x)=c1*p1(x)+...+ck*pk(x)`, where the expressions pi are chosen and the coefficients ci are unknown.

A known invariant, a calculated short sequence or an equation needed at the target can suggest these expressions. Choose only as large a family as the next question warrants. A larger polynomial degree adds unknowns and substitution work.

Choose the value arithmetic too. If the question concerns a remainder, calculate the proposed invariant modulo the relevant integer. That can preserve a distinction which an ordinary rational-valued linear expression misses.

#### MATH.11:4.3 - Derive and solve the preservation equations

For every rule T, calculate `I(T(x))-I(x)` in the chosen arithmetic. Require it to be zero wherever that step is allowed.

For a rule given as a relation, use `I(y)-I(x)` on its allowed pairs. A finite relation supplies one equation per pair; a supplied parameterization gives expressions to substitute. If neither is available, obtaining a usable description of those pairs is the missing construction.

For additive count changes, this gives one linear equation on the weights per change. Solve the equations jointly. If all weights must be zero, this family supplies no distinguishing weighted total.

For polynomial updates and a rational-coefficient polynomial family, expand the difference and collect like monomials. Setting every resulting coefficient to zero gives a linear system in the unknown ci. Solving it constructs polynomial identities that preserve I for every input. On a state set or enabled region smaller than the full polynomial domain, this identity test is sufficient but can be stronger than the preservation actually required. A relation valid only on the reachable states may therefore need another construction.

For example, let X={0,1}, T(x)=x² and I(x)=c\*x+d. Requiring the polynomial identity `c*(x²-x)=0` over all rational x forces c=0. On X the two allowed pairs are 0→0 and 1→1; checking them admits I(x)=x. Starting at 0, this invariant excludes 1. Here inspecting the allowed pairs produces a useful invariant within the same linear family.

The simultaneous equations can be solved by substitution in a small case or by linear algebra for a larger one. If several independent solutions are useful, keep them together as a tuple of invariants. A constant solution can be discarded for a target-separation question because it has the same value at every state.

If a tool proposes coefficients, substitute the resulting expression into the original rules. This confirms the identity and the arithmetic to which it applies. A few numerical trials can reveal an error; a proof for all allowed steps needs the corresponding algebraic argument or an exhaustive finite check.

#### MATH.11:4.4 - Prove the consequence for a sequence

Let a=x0 → x1 → ... → xm be any finite allowed sequence. Preservation gives:

`I(xm)=I(xm-1)=...=I(x0)=I(a)`.

Equivalently, use induction on the number of steps: the zero-step state has value I(a), and one more preserving step keeps that value.

Now use the relation. If `I(b)≠I(a)`, no finite allowed sequence reaches b. If an invariant equation determines an output quantity from other known quantities, derive that output under the equation's conditions. When several invariants are retained, every component must agree.

For a set of initial states, compare the target's invariant value with the values of I on that set.

#### MATH.11:4.5 - Resolve what equality leaves open

If the target and start have the same invariant value, the invariant has supplied a necessary condition. To claim reachability, construct an allowed sequence or use a theorem that supplies one under the remaining conditions.

Inspect a failed continuation. A rule may be irreversible, lack the required input units or require an order the invariant ignores. Refine the state or expression when that can answer the question. MATH.1 constructs paths with their intermediate conditions; MATH.8 generates a family when the available transformations form the relevant symmetry action.

When the coefficient calculation yields only constants, state the family actually exhausted. Changing from linear to polynomial expressions or from rational values to residues can change what is found. General polynomial-invariant search has its own algorithms and scope conditions; it is worthwhile when the simpler construction leaves a consequential question open.

Stop with the established formula, impossibility result, useful restriction or identified next construction. A request for one of these results need not expand into finding every invariant.

#### MATH.11:4.6 - Retain the construction through a change

For a changed initial state, retain the preservation equations and recompute the initial invariant value. For a changed target, compare its value using the same proved relation.

For an added or altered transformation, substitute that rule into the current invariant first. If it fails, include the new preservation equation and solve the affected system again. Removing transformations preserves any old invariant, although further invariants may become available.

A change of arithmetic, rounding or retained state can change the algebra itself. Recompute the affected identity before using its consequence. MATH.7 can transport the expression through a reversible representation; MATH.2 addresses an identification that must preserve a requested operation or answer. B.5.RR follows the changed mathematical result through a larger argument.

### MATH.11:5 - Archetypal Grounding

#### MATH.11:5.1 - Derive weights for an exchange construction

States are triples (a,b,c) of nonnegative integer counts. Two rules are allowed:

- Replace two A units with three B units when a≥2: `(a,b,c) → (a-2,b+3,c)`.
- Replace one B unit with one C unit when b≥1: `(a,b,c) → (a,b-1,c+1)`.

Starting with four A units, can the construction end with exactly five C units and nothing else?

The unweighted count changes under the first rule. Try `I(a,b,c)=α*a+β*b+γ*c`. The two differences are `-2*α+3*β` and `-β+γ`. Their joint equations have the solution `(α,β,γ)=(3,2,2)`, giving:

`I(a,b,c)=3*a+2*b+2*c`.

Every allowed step preserves this value. The start (4,0,0) has value 12; the target (0,0,5) has value 10. The target is impossible under the stated rules, however many steps are attempted.

The same invariant helps formulate a useful alternative: six C units have value 12. They are attainable. Apply the first rule twice to obtain (0,6,0), then the second rule six times to obtain (0,0,6). This sequence supplies the contribution that equality of the invariant alone left open.

Now start at (0,3,0) and ask for (2,0,0). Both values are 6, but the first rule cannot create A and the second only consumes B to create C. Thus the requested target is unreachable. Adding the reverse exchange `(a,b,c) → (a+2,b-3,c)` when b≥3 makes that target reachable in one step. Its invariant change is `2*3-3*2=0`, so the old invariant survives while the reachability answer changes.

For a material or operational application, interpret the counted kinds and allowed exchanges before using this mathematical result. The calculated weights express preservation by these rules; identifying them with physical mass or monetary value requires the corresponding subject account.

#### MATH.11:5.2 - Derive an accumulated sum from an update

A construction starts at `(n,s)=(0,0)` and repeatedly applies:

`(n,s) → (n+1,s+n+1)`.

The question is what s will be when n has reached a chosen nonnegative integer. The new term added to s depends on n, so try `I(n,s)=a*s+b*n^2+c*n+d`.

Substitution gives:

`I(n+1,s+n+1)-I(n,s)=(a+2*b)*n+(a+b+c)`.

Set `a+2*b=0` and `a+b+c=0`. Choose `a=2`, `b=-1`, `c=-1` and `d=0`. The resulting invariant is `I(n,s)=2*s-n^2-n`. It starts at zero, so every state reached by the update satisfies:

`2*s=n^2+n`, hence `s=n*(n+1)/2`.

After three steps, (3,6) satisfies it. The proposed state (3,7) has invariant value 2 and cannot result from these updates.

The same relation can be used with a different start. Starting at (2,10) gives invariant value 14, so later states satisfy `2*s-n^2-n=14`. One step produces (3,13), which satisfies that changed equation. The preservation proof is unchanged.

Now change the update to `(n,s) → (n+1,s+2*n+1)`. Substitution into the old invariant gives change `2*n`, so the old formula fails in general. Reusing the same candidate family gives equations `2*a+2*b=0` and `a+b+c=0`. Choose `a=1`, `b=-1`, `c=0`: the new invariant is `s-n^2`. From (0,0), it gives `s=n^2`.

These constructions use integer arithmetic without overflow. They also use the update as a simultaneous substitution: the expression for the new s contains the old n. An implementation that increments n before evaluating that expression would need a different calculation.

#### MATH.11:5.3 - Change the value arithmetic to find a parity obstruction

The state is an integer n. Allowed steps add 2 or subtract 2. Starting at zero, can the construction reach 1?

A rational-valued linear candidate `I(n)=a*n+b` changes by `2*a` under addition of 2. Requiring zero forces a=0, leaving only constants in this family.

Instead take `I(n)=n mod 2`, with values 0 and 1. Both +2 and -2 preserve the remainder. The start has remainder 0 and the target remainder 1, proving impossibility.

Here the necessary condition also leads to a construction. For any even target n=2k, use k additions of 2 when k≥0, or -k subtractions of 2 when k<0. Thus the reachable states are exactly the even integers. The invariant and the explicit sequence establish the two directions of that statement.

Adding the steps +1 and -1 destroys this parity invariant: 0 can now move to 1. Every integer becomes reachable by repeated unit steps. The earlier two-step rules and their parity calculation remain correct, but no longer cover all allowed steps.

### MATH.11:6 - Bias-Annotation

A familiar conserved total can be imposed before examining the transformations. Deriving its weights from each rule makes the assumed conservation testable. A small search can also encourage the claim that no useful invariant exists; retain the searched expression family and arithmetic when interpreting its failure.

An easily generated invariant may have little value for the target question. Compare its values or use its equation to obtain a consequence before investing in a larger repertoire.

### MATH.11:7 - Conformance Checklist

For the construction and use at hand:

1. The state set, initial condition and every allowed transformation are recoverable.
2. The candidate expression family and its value arithmetic are stated.
3. The preservation equations cover all allowed rules, with any stronger polynomial-identity requirement visible.
4. The constructed expression satisfies those equations and gives the stated initial value.
5. The finite-sequence argument supplies the reach of the conclusion.
6. An impossibility claim separates invariant values; a reachability claim also has its sequence or sufficient theorem.
7. A failed invariant search retains the family and scope actually searched.
8. Changes to initial data, target, transformations or arithmetic reopen the corresponding calculation.

Recognition can begin with one rule and a useful candidate expression. Assurance of a general consequence examines the preservation and sequence argument on which that consequence depends.

### MATH.11:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Assuming an ordinary total is preserved by an exchange with unequal counts | Derive weights from the contribution of each rule. |
| Checking only one branch of a construction | Include every allowed branch in the preservation equations. |
| Inferring reachability from equal invariant values | Supply a sequence or a theorem that also resolves enabling and ordering conditions. |
| Calling a constant-only coefficient result proof that no invariant exists | Retain the exhausted family; change expressions or arithmetic when useful. |
| Treating a polynomial identity search as complete for a restricted reachable set | Check preservation on the stated set using a description of its allowed steps. |
| Using a mathematical identity after changing update order or arithmetic | Substitute the implemented rule and recalculate the affected relation. |

### MATH.11:9 - Consequences

A small equation system can replace an unbounded search for an impossible construction. The resulting relation can also derive an output formula or narrow the next construction to candidates consistent with it.

The method's cost depends on the chosen expressions and substitutions. Weighted totals are often inexpensive; polynomial expansion can grow quickly. When an invariant leaves the consequential question open, a constructive path or a different mathematical method may be the better next move.

### MATH.11:10 - Architectural Rationale

The preservation question is local to a transformation, while the useful conclusion concerns any finite composition of transformations. The sequence argument joins those scales. Deriving the expression from the rules supplies the missing step in the advice to “find an invariant.”

Unknown coefficients turn a family of guesses into equations. Weighted counts expose exchange ratios; polynomial terms expose accumulation; residues retain divisibility information. The examples use different arithmetic but the same question: what function stays unchanged, and what does that prevent or determine?

An invariant usually compresses the state. Equality of its values can forget irreversible directions or unavailable inputs, as the exchange example shows. A proof of reachability therefore needs more than this compression. Conversely, different values can close an impossibility question without reconstructing every sequence.

These are mathematical constructions even when their states represent programs, resource transformations or physical models. Their interpretation and use in another subject need the correspondence and premises of that subject. Mathematical construction, subject interpretation and implementation can be divided among contributors while preserving those dependencies.

### MATH.11:11 - SoTA-Echoing

For deriving a condition valid after arbitrarily many steps, **adopt** the induction-based Invariant Principle in Lehman, Leighton and Meyer's *Mathematics for Computer Science*, §5.4.3. Compared with inspecting more executions, :4.4 uses one preservation proof to cover every finite sequence. This pattern constructs an invariant function; the book's principle also covers broader preserved predicates. Stop when the resulting relation answers the question, and reopen if an allowed transition changes. [MIT text](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).

For constructing polynomial expressions from update rules, **adapt** Bayarmagnai, Mohammadi and Prébet's *Algebraic and Algorithmic Methods for Computing Polynomial Loop Invariants*, §5, Corollary 5.4 and Algorithm 6. The adopted move substitutes an expression with unknown coefficients and solves the resulting linear equations. It improves on unstructured guessing in :4.2-:4.3 and the sum construction in :5.2. The source's stronger algorithms distinguish invariant form, initial-value conditions and search space. Here the polynomial-identity construction has its stated scope; a restricted reachable-set question can require a different method. Reopen when a richer family or specialized algorithm obtains a more useful relation at acceptable cost. [Extended paper](https://arxiv.org/html/2412.14043v2).

For count transformations, **adapt** the conserved linear expression described by Gopalkrishnan in *Autocatalysis in Reaction Networks*. The weighted-exchange derivation in :5.1 makes such a quantity available instead of assuming an unweighted total. Equal values still require a reachability construction. The source's chemical-network results need their own premises; they are not used to identify the counted kinds in this mathematical example. A changed exchange rule reopens the weight equations. [Author's account](https://johncarlosbaez.wordpress.com/2013/10/11/autocatalysis-in-reaction-networks/).

The three worked constructions and their changed conditions are derived here.

### MATH.11:12 - Relations

- **MATH.1** constructs permitted paths and retains intermediate state; **MATH.4** constructs witnesses by induction. This pattern constructs a preserved function and uses induction to obtain its consequence.
- **MATH.2** forms identifications under retained operations. Equal invariant values give a possible identification, whose adequacy for another operation remains a separate question.
- **MATH.5** extends a supplied generator assignment through composites. This method instead solves for an assignment that transformations preserve.
- **MATH.7** transports an expression with its structure through a bijection. **MATH.8** generates solution orbits; an invariant can rule out membership but need not distinguish all orbits.
- **B.5.RA** recovers the resulting argument; **B.5.RR** revises its affected dependencies; **B.5.QD** develops the next question from its obstruction or formula.
- **C.29** connects the mathematical result to another subject. **C.11.DUA** helps decide whether a larger invariant search would change the next useful action.

### MATH.11:End
