## MATH.5 - Extend a Generator Assignment While Preserving Operations (Homomorphism)

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.5:1 - Problem frame

Use this pattern when you know what the basic elements of a mathematical construction should become and need a compatible map on everything built from them. A value assigned to a variable, a transformation assigned to a command, or a cost assigned to a generating step must extend to composite expressions in a way that preserves the chosen operations.

The needed map is a *homomorphism*: it carries each source operation to the corresponding target operation. To construct it, evaluate composite expressions from the assigned generator values. If the source identifies different expressions, establish that those expressions receive the same value.

Start with one generator and one composite expression. Return their images and the rule that extends the assignment, or a source equality that the proposed images cannot preserve. A first calculation can expose an incompatible assignment before a large translation is attempted.

The reader needs functions, finite expressions and the operations used in the chosen construction. The method covers total operations with finitely many inputs, finite words with associative composition, and the finite typed paths built by MATH.1. A typed path starts and ends at named objects; its interpretation must supply their images as well as the images of its arrows.

If the required map or one needed value is already available, use it. An arbitrary map on a small finite set can be simpler to specify directly when preserving operations is not part of the question.

### MATH.5:2 - Problem

A list of corresponding symbols leaves most compound expressions unassigned. Filling them independently can violate the operation that made the correspondence useful. Two source expressions may also denote the same object while their proposed target values differ.

The task is to obtain a reusable mapping rule and identify its scope. The assignment on generators must determine the composites, and every source identification used by the map must remain valid after evaluation.

### MATH.5:3 - Forces

| Force | Tension |
| --- | --- |
| Few generators and many composites | A compact assignment can govern arbitrarily large finite expressions, provided the extension rule is established. |
| Free construction and imposed equations | Syntax permits independent construction; equations identify expressions and restrict their possible images. |
| Preserved operations and retained information | A homomorphism can preserve composition while forgetting distinctions needed by another question. |
| Reusable translation and one calculation | Building the general map costs more than evaluating one expression, but supports substitutions and repeated use. |

### MATH.5:4 - Solution

**Local mantra:** name the generators and operations; assign their images; extend by construction; preserve the equations; use the resulting map.

#### MATH.5:4.1 - State the source construction and target operations

List the generators and the rules for building finite expressions from them. An expression can be a generator, a constant, or an operation applied to constituent expressions. State each operation's number of inputs. With generators `x,y`, constants `0,1` and binary operations `+` and `*`, the expression `(x*y)+1` is obtained by two construction steps.

Distinguish the freely formed expressions from any equations imposed on them. For example, treating `x*y` and `y*x` as the same requires a commutativity equation. The written resemblance of the expressions does not supply that equation.

Name the target set and a corresponding operation for each source operation, including the value of each constant. Every required target operation must be defined on the inputs it receives. This pattern's total-operation construction does not supply a partial operation's domain.

For a word construction, state the target composition `star` and its identity `e`. The operation must be associative for unparenthesized words to denote a composition independently of grouping. MATH.1 constructs the source words or paths; here the task is to build their map into the target structure.

For typed paths, assign each source object X a target object F(X). The target must supply arrows, associative composition on matching endpoints, and an identity at each object. Assign each generator `a:X -> Y` an arrow `a_target:F(X) -> F(Y)`. A target can consist of sets and functions; different source objects may then receive sets of different kinds of values. Check these domains before composing.

#### MATH.5:4.2 - Extend the assignment recursively

Assign a target value `a(x)` to every generator `x`. Define the evaluation `E` on finite expressions:

- a generator `x` receives `a(x)`;
- a constant receives its named target value;
- `op(t1,...,tn)` receives `op_target(E(t1),...,E(tn))`.

Each recursive call uses a constituent expression. MATH.4 supplies the finite-construction argument and the treatment of a result that needs additional information.

For a word `[x1,...,xk]`, the same move evaluates the assigned generator values in order. The empty word receives `e`; extending a word by `x` changes its value from `v` to `v star a(x)`. Associativity and the identity laws make this evaluation preserve concatenation:

`E(p;q)=E(p) star E(q)`.

For a typed path, set `E(id_X)=id_F(X)`. If `p:X -> Y` has been evaluated and `a:Y -> Z` is the next generator, set `E(p;a)=E(p) star a_target`, where `star` is again read in execution order. The intermediate object F(Y) makes this composition defined. Recursing by path length evaluates every finite path while keeping its endpoints. In a target of sets and functions, this means applying E(p) first and a_target second.

The image of a composite is now computed from its parts. It is no longer an independently chosen entry in a correspondence table.

#### MATH.5:4.3 - Establish preservation and uniqueness

For freely formed expressions, preservation follows from the defining clause: evaluating an operation on expressions gives the target operation on their evaluations. The generator and constant clauses cover the starting cases.

Suppose another operation-preserving map `H` has the same assigned generator values. It agrees with `E` on generators and constants. If it agrees on the constituents of an expression, preservation forces agreement on the whole expression. Induction therefore gives `H(t)=E(t)` for every expression.

The conclusion is uniqueness among maps preserving the named operations and agreeing with the given assignment. Changing the assignment or required operations changes that question.

For words, the corresponding argument starts with the empty word and extends by one generator. Every concatenation-preserving map with the same identity and generator images must return the same ordered product.

For paths, the base case uses the identity at each F(X). Induction on the second path's length, using target associativity, gives `E(p;q)=E(p) star E(q)` for every permitted join. A map preserving identities and composition with the same object and generator assignments must follow those recursive clauses, so it is unique. Such an object-and-arrow map between categories is called a functor. The one-object word construction is its monoid case.

#### MATH.5:4.4 - Make the map respect identified expressions

If the source equates expressions, test the equations under `E`. To define `E_bar([t])=E(t)` on an equivalence class, require:

`t~u implies E(t)=E(u)`.

MATH.2 supplies the quotient and representative-independence construction. Here it is applied to the evaluation just obtained.

For typed paths with the objects retained, impose equations between paths having the same source and target. Compare their target arrows, including the appropriate identity for an empty path. Closure under permitted composition makes the evaluation descend just as above. Identifying different source objects changes this setup and requires a construction that also accounts for their identities and permitted joins.

When the source equivalence is generated by stated equations and their use inside larger expressions, show that each generating equation has equal evaluated sides. Equality is preserved when equal values enter the same target operation. It is also preserved along reversal and a finite sequence of equation replacements. These facts extend the result to the generated equivalence.

An equation schema such as `s*t=t*s` ranges over its permitted substitutions. Checking one numerical substitution leaves the other instances unresolved. Establish the target law for the required range or return a failing instance. If the source also has additional identifications, include them in the comparison.

A failed equation gives a concrete choice: change the generator assignment, change the target operations, or use a source construction that retains the distinction. Each option changes the mathematical account. Select the one that still answers the receiving question.

#### MATH.5:4.5 - Use the map and inspect what it forgets

Evaluate the needed expression or pass the reusable map to its consumer. The preservation argument permits calculation by parts and supports substitution of an equivalent source expression.

Equal target values can still come from different source objects. If the receiver needs to recover a source object, obtain an inverse, a retained representative, or another construction that supplies it. A homomorphism by itself does not provide such recovery.

After a changed generator value, reuse the recursive definition and preservation proof for freely formed expressions. Recheck any imposed equation whose evaluated sides can change. After a changed target operation, revisit the clauses and laws that used it.

Stop with the needed value, the reusable homomorphism, or an equation that prevents the proposed extension. A mathematical map can then contribute to FPF C.29's interpretation-and-return method when the receiving question concerns another subject.

### MATH.5:5 - Archetypal Grounding

#### MATH.5:5.1 - Evaluate expressions, then test an equation

Build expressions from `x,y,0,1,+,*`. Assign `x=2` and `y=3`, and use ordinary integer addition and multiplication. Evaluation returns `E((x*y)+1)=7`. The same rules evaluate every finite expression and preserve its two operations.

Now let the source identify expressions using the usual commutative-semiring laws: associativity, the two identities, commutativity of both operations, distributivity, and multiplication by zero. Integer arithmetic satisfies those laws, so evaluation also defines a map from the identified expressions.

Change the assignment to matrices:

`A=[[0,1],[0,0]]`, `B=[[0,0],[1,0]]`.

Use matrix addition and multiplication, the zero matrix and identity matrix. This still evaluates freely formed expressions. But:

`A*B=[[1,0],[0,0]]`

`B*A=[[0,0],[0,1]]`.

The source's equation `x*y=y*x` therefore fails under this assignment. A substitution into the commutative quotient would give two answers for one source element.

If ordered multiplication is needed, use expressions whose equations retain its order. Matrix addition, multiplication, zero and identity support the remaining semiring laws. If commutative multiplication is essential to the original question, retain a target and assignment that satisfy it instead. The failed equation identifies the mathematical change required.

#### MATH.5:5.2 - Calculate the combined effect of a word of operations

Let a word contain commands `I` and `D`. Their mathematical effects on an integer are:

`I(x)=x+1`, `D(x)=2*x`.

Represent an affine transformation `x -> s*x+t` by the pair `(s,t)`. Thus `I` receives `(1,1)` and `D` receives `(2,0)`.

For `(s,t)` followed by `(u,v)`, define:

`(s,t) star (u,v)=(u*s,u*t+v)`.

Substitution derives this rule: `u*(s*x+t)+v=(u*s)*x+(u*t+v)`. The identity is `(1,0)`. For a third pair `(w,z)`, either grouping gives `(w*u*s,w*u*t+w*v+z)`, so the rule is associative.

Extend the two generator assignments to words. Then:

- `I;D` receives `(2,2)`, meaning `x -> 2*x+2`;
- `D;I` receives `(2,1)`, meaning `x -> 2*x+1`;
- `I;D;I` receives `(2,3)`, meaning `x -> 2*x+3`.

The third word sends 10 to 23. The pair describes its effect for every integer, allowing it to be composed with another affine operation without expanding the whole word again.

A different map can send each generator to cost 1 and concatenate by addition. It gives both `I;D` and `D;I` the value 2. This is a valid cost homomorphism but loses their different effects. Requiring the source equation `I;D=D;I` would preserve that cost map while preventing the stated effect map. The receiving question decides which distinction must remain.

If a command's availability depends on intermediate state, the all-words construction is no longer the intended source. Use state-sensitive paths under MATH.1 and preserve their interfaces when constructing the interpretation.

#### MATH.5:5.3 - Interpret paths with different kinds of values

Take source objects A and B, with generators `u:A -> B` and `v:B -> A`. Interpret A as the integers and B as pairs of integers. Assign `u_target(n)=(n,0)` and `v_target(n,m)=n`. The empty path at A becomes the identity on integers; the empty path at B becomes the identity on integer pairs.

Extension gives `E(u;v)(n)=n`, whereas `E(v;u)(n,m)=(n,0)`. The first composite therefore equals `E(id_A)`. The second differs from `E(id_B)`: it sends (7,5) to (7,0). The interpretation can descend through the source equation `u;v=id_A`, together with the equations generated from it by permitted composition. It keeps the information that the return path loses the second component.

Now require `v;u=id_B` as well. The same assignment fails that new equation. Keep the free-path interpretation or the first quotient, change the assigned maps, or change the required identification. Both composites are valid paths; the failed assertion concerns their values, not whether they can be formed. This distinction lets a representation carry construction followed by recovery without claiming recovery in both directions.

### MATH.5:6 - Bias-Annotation

Recognizable notation can encourage an unexamined substitution. Matrix multiplication retains order even when the same multiplication sign denotes commutative arithmetic elsewhere. Test the law that the source expression uses.

A compact target value can also be mistaken for a reversible description. The cost example preserves concatenation while merging words with different effects.

Finally, a few successful evaluations can hide an equation schema's range. The reusable extension depends on preservation for every admitted instance of the equations it consumes.

### MATH.5:7 - Conformance Checklist

- For typed paths, do the object assignments, generator endpoints and identities determine the extension, and do imposed equations compare arrows with the same endpoints?

- Are the generators, constants and source operations specified?
- Does each source operation have a defined target operation with the required inputs?
- Do the evaluation clauses determine every finite expression?
- Does the preservation argument cover the named operations and the identity?
- Is any uniqueness claim restricted to maps with the same assignment and preservation requirements?
- If expressions are identified, do their evaluated values agree for every required equation instance?
- Does the returned value retain the information needed by its consumer?
- Does a changed assignment, equation or operation lead to the affected comparison?

### MATH.5:8 - Common Anti-Patterns and How to Avoid Them

**Assign unrelated values to composites.** Define their values through the target operations. Otherwise the map can fail the very composition it is intended to represent.

**Carry commutative arithmetic into ordered operations.** The matrix and command cases supply counterexamples. Keep the source order or justify the commutativity required by the quotient.

**Check one instance of a general equation.** Recover its substitution range. Establish the law there or return a failing instance.

**Infer reversibility from operation preservation.** The cost map returns the same value for different effects. Retain a suitable source representative or construct the additional inverse needed for the question.

**Drop a composition precondition.** An unavailable word is not repaired by assigning it a numerical image. Use a source that represents permitted joins.

### MATH.5:9 - Consequences

A small assignment determines a map over arbitrarily large finite constructions. Its evaluation rule supports calculation, substitution and comparison of composite effects. A failed equation can locate the required change before the entire map is used.

The map may deliberately discard distinctions. Preserving operations and recovering original objects are separate results. Equality checks on complicated presentations can remain difficult even when the recursive evaluation itself is simple.

### MATH.5:10 - Architectural Rationale

The method connects three mathematical contributions: recursive construction, preservation of operations, and compatibility with imposed equations. Their combination answers a different question from constructing the source objects alone: how a chosen interpretation extends across that whole source.

The free-expression step makes evaluation and uniqueness accessible. The quotient step then exposes the obligations introduced by an identification. Keeping them separate lets a failed equation leave the valid free-expression map available.

For one small expression, direct evaluation can be sufficient. The general construction earns its cost when many expressions, substitutions or a reusable representation are needed. A ready homomorphism can supply the same result without reconstructing its proof.

The affine-pair case gives the same composition a second mathematical description. Its equation connects the descriptions.

### MATH.5:11 - SoTA-Echoing

**Question:** how can a generator assignment determine an operation-preserving map, including when the source equates different constructions?

Burris and Sankappanavar's [*A Course in Universal Algebra*, corrected 2012 edition](https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf), II §10, definitions 10.1-10.5, lemma 10.6 and theorem 10.8, supplies term formation, recursive evaluation and unique extension. **Adopt** that construction. The examples apply it to arithmetic expressions and composed affine transformations. The pattern's quotient step uses the congruence construction supplied by MATH.2 and gives its preservation argument.

The [Mathlib free-monoid implementation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/FreeMonoid/Basic.html#FreeMonoid.lift) gives an executable formalization of the word case. `FreeMonoid.lift` extends generator values by the product of their images; `hom_eq` states uniqueness from generator agreement. **Adapt** that presentation into ordinary mathematical instructions, retaining the monoid premises.

The [Mathlib path-category construction](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/PathCategory/Basic.html#CategoryTheory.Paths.lift) formalizes the typed branch: `Paths.lift` extends an object-and-generator assignment; `lift_nil`, `lift_cons` and `lift_unique` establish the identity, recursive composition and uniqueness clauses. The pattern spells out those operations for use after MATH.1. The integer/pair case derives a consequence and a failed additional equation directly from its assigned functions.

The useful comparison is with a supplied map or independent evaluation of a small number of expressions. Extension by generators improves repeated compositional use, while an imposed equation adds a real preservation obligation. Reopen when a partial operation has a domain beyond the path-endpoint construction supplied here, the source admits infinite constructions, an equation fails, or a simpler available map supplies the receiving result.

### MATH.5:12 - Relations

- **Uses MATH.1 where the source is a path construction:** assign images to its objects and generators, then extend to its identities and permitted composites.
- **Uses MATH.4:** construct the evaluation on finite expressions and prove its recursive clauses and uniqueness.
- **Uses MATH.2 when equations identify expressions:** obtain representative-independent evaluation on the quotient.
- **Connects with FPF C.29:** use the mathematical map in a subject correspondence and recover the result needed there.
- **Connects with Method Engineering:** a mathematical account of composed methods can use the affine-effect construction; B.1.5.CM develops the proposed composition account; A.3.1.CC checks its claims and returns a correction to the description or construction that needs it.

### MATH.5:End
