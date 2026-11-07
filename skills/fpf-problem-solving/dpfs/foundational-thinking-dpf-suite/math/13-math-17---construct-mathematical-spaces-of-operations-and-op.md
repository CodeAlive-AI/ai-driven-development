## MATH.17 - Construct Mathematical Spaces of Operations and Operations on Them

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.17:1 - Problem frame

Use this pattern when the rule for constructing or transforming something has itself become the object of work. You may need to combine allowable rules, apply a rule to a different kind of input, compare ways of repeating it, or change the rule while retaining a useful property. Knowing how to execute each individual rule leaves these questions open.

Start with the operation you want to perform on rules and the consequence you need from it. For example: “Can these permitted updates be composed?” or “Can I transform each stage separately and obtain the same result as transforming their composite?” One constructed operation, together with its applicability and the law or counterexample that answers that question, is a useful result.

Here a **space of operations** is a specified collection of operations with the equality, composition and further structure needed by the question. The main route uses sets and functions; it requires understanding function application, composition, sets and elementary equality arguments. MATH.16 explains functions as mathematical objects, evaluation and currying. The polynomial example is an optional branch using polynomial arithmetic.

Use an existing rule directly when its application settles the question. Construct a space of operations when you need to reason about, generate or change rules. A topology, metric or order on that space becomes part of the construction when the question needs continuity, approximation or comparison in that sense.

### MATH.17:2 - Problem

An operation can be permissible on its own yet leave the permitted class when combined with another. A transformation of operations can produce a valid operation yet alter the result of a sequence. These failures occur at different places: membership, composition, or the proposed transformation.

To locate the failure, specify the rule's domain, construction and relevant laws. These supply the mathematical questions: which operations belong to the permitted collection, what can be done with them, and which conclusions follow?

### MATH.17:3 - Forces

| Force | Tension |
| --- | --- |
| Individual applicability and composition | Two allowable operations can have a composite that violates the condition used to select them. |
| Useful abstraction and needed distinctions | Functions expose input-output behavior; questions about construction steps or cost need a representation retaining those distinctions. |
| Changing rules and retaining consequences | A higher-order operation may preserve some laws, replace others, or require a narrower domain. |
| Uniform construction and branch-specific structure | One construction can work across many sets, while continuity, differentiability or other additional requirements need their own arguments. |

### MATH.17:4 - Solution

**Local mantra:** state the change to the rule; construct its admissible inputs; establish composition; construct the higher-order operation; derive its consequence; use or revise it.

#### MATH.17:4.1 - Specify the operations and the question about them

Name the inputs and outputs of an operation. Write `f:A -> B` when f assigns an element of B to every element of A. Write `g∘f` for “first f, then g”; it is defined when f's output is an allowed input to g.

Choose what counts as equality for the present question. In the main function route, f and g are equal when they have the same domain and codomain and `f(x)=g(x)` for every input x. If the question concerns the steps used, resource cost or another distinction between ways of producing that function, retain a construction or program representation carrying that distinction. A function value alone leaves it unavailable. MATH.1 supplies constructions retaining ordered steps; MATH.2 handles an identification when the needed operations respect it.

Formulate the intended operation on rules. It might take two operations and compose them, send an operation on individual inputs to an operation on collections, or turn an expression for a function into another expression. State which result matters: admissibility, an identity, a comparison, a changed construction, or a failed requirement.

#### MATH.17:4.2 - Construct the admissible collections

For each relevant pair A, B, specify `Adm(A,B)`, the collection of operations allowed from A to B. Give a condition that can be used to establish membership. Examples include preserving an order, maintaining a relation between components, or mapping a designated subset into itself.

When the operations are functions, MATH.16 supplies the function object and evaluation `ev(f,x)=f(x)`. Restrict that object by the required condition. A rule with several inputs can be represented by a function on their product when a tuple contains all the inputs it needs.

For a partial operation, include its domain of definition. If f is defined on D within A and g on E within B, their composite is defined on `{x in D | f(x) in E}`. Whether this is an acceptable domain belongs to the current question.

Changing the admissibility condition changes the collection. An update preserving a set of possible states and a map preserving an algebraic operation answer different requirements. State the requirement before using either as an admissible rule.

#### MATH.17:4.3 - Establish the composition that the work needs

Try to construct:

`Adm(B,C) x Adm(A,B) -> Adm(A,C), (g,f) -> g∘f`.

The formula already defines a function composite. To obtain the displayed operation, establish that the composite satisfies the selected admissibility condition. Establish identity membership when doing nothing must be an allowable operation. Associativity then follows from function composition.

For example, fix a subset P of X and admit every `f:X -> X` with `f(P) contained in P`. If f and g are admitted and x lies in P, then f(x) lies in P and g(f(x)) lies in P. Thus their composite is admitted, as is the identity. These operations form a **monoid**: a set with associative composition and an identity. Several object types with identities and compatible associative composition form a **category**. These names make the established structure reusable.

If closure fails, use the failing input or pair to choose the repair. You might restrict the operations, enlarge the permitted result class, or keep a sequence of operations whose total admissibility is checked separately. For a cumulative resource bound, for example, retain the sequence and accumulated cost needed to assess the whole. Calling each step allowable leaves that total unresolved.

An interchange of steps is another claim. Establish `g∘f=f∘g` when a proposed reordering needs it; associativity by itself only changes the grouping of a fixed order.

#### MATH.17:4.4 - Construct an operation on operations and its law

Give the higher-order operation its own input and output types. For a transformation sending a function f to a new function T(f), start with an arbitrary input x of the desired new function. Express its required output using f and the available operations. That expression defines T(f)(x). Then establish that the constructed function belongs to the promised output collection.

Choose the law from the needed use. If T is meant to translate a sequence stage by stage, test:

`T(g∘f)=T(g)∘T(f)` and `T(id)=id`.

The types on both sides must agree. When T also changes the objects, specify that object assignment and the corresponding operation collections. An assignment preserving these compositions and identities is a **functor**.

For instance, we want to apply `f:A -> B` separately to each entry indexed by a fixed set I. Represent the input by `s:I -> A`; the set of such inputs is `A^I`. At index i the input is s(i), so the required output is f(s(i)). Collecting these outputs gives the function `i -> f(s(i))` from I to B. We have constructed:

`L_I(f):A^I -> B^I`, defined by `[L_I(f)(s)](i)=f(s(i))`.

To derive the composition law, take arbitrary s and i:

`[L_I(g∘f)(s)](i)=g(f(s(i)))=[(L_I(g)∘L_I(f))(s)](i)`.

Equality at every index proves the composition law. The identity law follows by applying the identity at every index. If admissibility requires each entry to remain in P, the earlier membership argument applies entry by entry. A condition relating different entries needs a further preservation argument.

A different higher-order operation can have a different useful law. Differentiation of polynomials preserves sums and scalar multiples and obeys the product and chain rules. Use those laws when deriving a derivative; a composition-preservation requirement would ask it to do a different job. The needed mathematical operation determines which laws to establish.

#### MATH.17:4.5 - Use the construction to change or compare rules

Compute the proposed changed operation and derive the consequence that motivated it. When comparing “transform each step” with “transform the whole”, keep both expressions until their equality is established or a separating input is found.

The result consists of the usable construction and the conditions supporting the particular consequence. For a finite example, a counterexample can settle a failed universal claim. A general preservation claim needs an argument over its stated inputs.

Return to the affected condition when the task changes. A new interaction between entries may invalidate pointwise lifting. A narrower resource budget may invalidate closure. A new question about how the operation was obtained may require retaining the construction that an input-output function discarded.

When this mathematics describes a working method, use C.29's correspondence to identify what the mathematical operations represent and which practical distinctions they retain. A proposed program transformation also needs its execution semantics. Those connections let the result inform actual work while keeping the mathematical and subject claims recoverable.

### MATH.17:5 - Archetypal Grounding

#### MATH.17:5.1 - Individually permitted changes and a permitted whole

Let `X={0,1} x {0,1}`. An update is allowed to change at most one coordinate of each input pair. Flipping the first coordinate is allowed; flipping the second is allowed. Their composite sends `(0,0)` to `(1,1)` and changes two coordinates. The proposed collection is not closed under composition.

If the requirement limits each elementary step, keep a sequence of these steps and inspect intermediate states. If it limits the difference between initial and final states, test the composite against that bound and reject this pair. The same counterexample distinguishes the two intended uses.

Now take another requirement: the two coordinates must stay equal. Put `P={(0,0),(1,1)}` and admit functions sending P into P. The joint flip belongs; either single-coordinate flip fails. Closure follows from :4.3. This change of admissibility supplies a composable class suited to the equality requirement.

#### MATH.17:5.2 - Lift a rule, then change how repetition is distributed

Take integer operations `f(n)=n+1` and `g(n)=2n`. Pointwise lifting to pairs is the case `I={1,2}`. Applied to `(1,3)`, the lifted composite produces `(4,8)`. Lifting f and g separately and then composing produces the same pair. The proof in :4.4 establishes that agreement for arbitrary inputs and functions.

Consider a different change: `S(h)=h∘h`, meaning repeat an operation twice. This always gives another integer endofunction, but the two sequencing proposals give:

`S(g∘f)(n)=4n+6`;

`(S(g)∘S(f))(n)=4n+8`.

At n=0 the answers are 6 and 8. To repeat the complete sequence, retain `(g∘f)∘(g∘f)`. To run each stage twice, use `g∘g∘f∘f`. If f and g commute, rearrangement proves the two proposals equal; the present f and g do not.

The construction therefore returns both a valid operation on operations and a failed composition-preservation claim. That failure determines which changed rule implements the intended repetition.

#### MATH.17:5.3 - An operator whose useful law has another form

Let `P=R[x]`, the real-coefficient polynomials in one variable, and define `D:P -> P` by differentiating each monomial: `D(a*x^n)=n*a*x^(n-1)` for n>0, and D(a)=0 for constants. This constructs an operation on functions through their polynomial expressions.

For `p=x^2` and `q=x+1`:

`D(p*q)=3*x^2+2*x`.

The product of derivatives is `D(p)*D(q)=2*x`. The applicable law is instead:

`D(p*q)=D(p)*q+p*D(q)`,

which gives the required result. To establish the law generally, first expand two monomials: differentiating `a*b*x^(m+n)` gives coefficient `(m+n)*a*b`, the sum of the two product-rule contributions. Distributing over the finite sums proves it for polynomials.

The same method of working is used as in :5.2: construct the operator, identify the law needed for the proposed use, and establish that law. Here it enables transforming a product expression into its derivative.

#### MATH.17:5.4 - Change a function while preserving its increments

Given a function f from the real numbers to the real numbers and a chosen point c, construct a function g that fixes c and preserves every increment of f. The requirements are g(c)=c and g(x)-g(y)=f(x)-f(y) for every x,y.

Set y=c in the second requirement. It forces g(x)=f(x)-f(c)+c. This defines a real-valued function; substituting c establishes the fixed point, and subtracting its values at x and y cancels the added constant and preserves the required increment. Thus the formula supplies the unique function under these requirements.

The transformation takes f itself as an input and returns g. Fixing a point and preserving increments do not settle an additional question about composition or cost. The repetition case in :5.2 shows how different requested changes lead to different operations on the same input rules.

### MATH.17:6 - Bias-Annotation

A familiar collection of “valid operations” can conceal an unproved closure claim. A familiar higher-order operation can conceal the choice of law used to combine its results. Work with the actual membership condition and proposed equation; the failing inputs in :5.1 and :5.2 locate those different errors.

The set-and-function route makes these questions accessible. A question involving topology, approximation, randomness or an alternative equality calls for the corresponding additional structure and argument.

### MATH.17:7 - Conformance Checklist

For the construction being used:

- The operations have recoverable inputs, outputs, equality and admissibility conditions.
- The needed compositions land in the claimed collection, or a concrete failure has changed the proposed use.
- The higher-order operation has a construction and returns an admissible output.
- Each law used to derive the result has the required scope and an argument; a tested finite case supports only what it establishes.
- The resulting comparison or changed rule answers the starting question.
- A subject or computational application supplies the correspondence or execution account needed by that use.

### MATH.17:8 - Common Anti-Patterns and How to Avoid Them

**Inferring closure from individual permission.** The two flips in :5.1 each meet the step condition but fail it when composed. Decide whether the requirement concerns a step, a sequence or the whole input-output change, and construct the corresponding collection.

**Moving a transformation through composition without its law.** Repeating each stage twice changed the answer in :5.2. Derive the transformation equation before using it to reorganize a sequence.

**Demanding the wrong preservation law.** Polynomial differentiation supplies a useful operator through linearity and the product rule. Choose the law from the intended transformation instead of requiring every operator to preserve multiplication or composition.

### MATH.17:9 - Consequences

Operations become available for construction, comparison and change. A law established for the higher-order construction can replace repeated case-by-case reasoning, while a counterexample can identify a proposed change that needs revision.

The abstraction has a cost: the operation collection and its laws must be constructed. It pays when the rule itself is changing or when one result will organize many operations. Questions about implementation, approximation or real interaction can require further structure beyond the function account.

### MATH.17:10 - Architectural Rationale

Separating membership, closure and higher-order transformation locates three different sources of failure. Combining them into a generic instruction to “check composition” would leave the repair unclear.

MATH.16 supplies the function-object construction. Here the practitioner selects a collection of allowable operations and constructs further operations whose arguments are members of that collection. Monoid and category language make the established composition reusable; the derivative example shows why other higher-order operations need other laws. The choice follows the problem about rules.

The same structure can support mathematical work, computational transformations and mathematical accounts of methods. Its applicability in the latter two depends on the interpretation of operations and consequences, which remains the responsibility of the receiving method.

### MATH.17:11 - SoTA-Echoing

Riehl's [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf), §§1.1 and 1.3, supplies the algebraic account of composable maps, monoids and functors. The adopted contribution is the ability to study transformations of operations by their preserved structure. This pattern turns that account into a method for selecting admissible operations, finding a failed closure condition and constructing the transformation required by the question.

A direct formula is sufficient when one operation settles the task. The structured account helps when rules must be combined or changed. Polynomial operators illustrate the alternative: linearity and a product rule may provide the useful calculus even when composition preservation is inapplicable. Additional mathematical structure is selected by the needed consequence.

### MATH.17:12 - Relations

- **MATH.16** constructs function objects, evaluation, products and maps selected by their required uses.
- **MATH.1** retains generating steps and their order; **MATH.5** extends an assignment to generators through the operations it must preserve.
- **MATH.2** establishes when an identification of operations supports the proposed further operations.
- **MATH.7** transports structure through a bijection. Comparing broader mathematical accounts uses interpretations of their objects, operations and assertions.
- **MATH.11 and MATH.13** develop invariant and symmetry consequences once the transformations are specified.
- **B.5.FM, C.29 and C.29.2** connect the mathematical construction with a working question, subject correspondence and computational use.

### MATH.17:End
