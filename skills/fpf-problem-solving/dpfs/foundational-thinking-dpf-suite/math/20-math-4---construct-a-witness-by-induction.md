## MATH.4 - Construct a Witness by Induction

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.4:1 - Problem frame

Use this pattern when an input is given as a finite construction from smaller inputs, and you need a way to produce an object with a required property for every such input. You may know the desired equation or have an existence argument, while the operation that obtains an answer remains missing.

A witness is the object that satisfies the requirement: a quotient and remainder, for example, or a coloring with a stated property. Construct a witness for each base case, then construct one for a larger input from the witnesses for its immediate constituents. The same case structure gives a reason why the result has the required property.

Start with the smallest input and one step that builds the next input. Return a base witness and a usable step, or identify what the step still cannot construct. You need functions, elementary logical conditions and the input's formation rules. The number example also uses integer arithmetic; the tree example explains its own constructors.

This method starts with freely formed constructor expressions: each input supplies its outermost constructor and its constituent inputs. When different expressions represent the same object, section 4.4 explains the additional step needed for a function of that object. If a supplied operation already returns the required object, use it. An existence result can also be sufficient when no witness or way of producing one is needed. Infinite behavior or a recursion that does not follow smaller constituents needs a different termination or continuation argument.

### MATH.4:2 - Problem

An assertion that a suitable object exists can leave the receiver unable to obtain it. A recursive formula can leave a different gap: it may call itself without reaching an answer, omit a case, or return objects that fail the required property.

The mathematical task is to build the operation and its justification together. The case for a larger input must use only what the smaller-input results actually provide. Sometimes this reveals that the proposed result was too weak: the step needs an extra parameter or an auxiliary value.

### MATH.4:3 - Forces

| Force | Tension |
| --- | --- |
| One requested object and a reusable construction | A single instance may be easiest to solve directly; a family benefits from one operation and argument that cover its formation rules. |
| A small result and a usable inductive step | Discarding an auxiliary value can make the next case impossible to construct. |
| A complete definition and executable choices | Every input case needs an output rule; saying that a suitable choice exists may leave the rule missing. |
| Simple recursion and efficient execution | Following the input's construction makes correctness accessible, but another algorithm may use fewer operations or less storage. |

### MATH.4:4 - Solution

**Local mantra:** state the wanted object; build the base; build the next case from smaller cases; justify the construction; use the witness.

#### MATH.4:4.1 - State the input construction and wanted result

Name the input family, its constructors and any fixed parameters. For natural numbers, the constructors are zero and successor. A finite binary tree can be a leaf or a new root joining two smaller trees. The supplied constructor and constituents determine which recursive clause applies. If different constructions are later identified, retain that identification as a separate condition.

For each input `x`, state the kind of output `y` and the property `P(x,y)` it must satisfy. Include bounds or retained information that the next use consumes. For division by a positive integer `d`, the output is a pair `(q,r)` satisfying `n=q*d+r` and `0≤r<d`.

Use the input's actual formation rules to choose the cases. A proof about trees cannot be applied to a structure with additional edges without considering those edges.

#### MATH.4:4.2 - Construct the base witnesses

For each constructor with no smaller inputs, give an output and show that it satisfies the required property. This supplies the point at which recursive evaluation can return a value.

If the base fails, inspect the specification or its parameter conditions. Do not invent a default output that fails the requirement merely to complete the cases.

#### MATH.4:4.3 - Construct the step and strengthen what it needs

Take one constructor with smaller inputs. Assume that each smaller input already has an output satisfying the stated property. Give an operation that uses those outputs to build the required output for the whole input.

Show why the construction preserves the property. Check each branch that changes the returned object. When the step needs information absent from the proposed output, strengthen the result or generalize a fixed parameter, then revisit the base cases and affected steps.

For example, a tree-coloring step may need to choose either color for a subtree's root. A construction that promises only a root of color zero leaves that step unsupported. A construction parameterized by the required root color supplies what the step uses.

To obtain an executable construction, each case distinction must be decidable from the supplied data, and each operation used to build an output must itself return. A step that says only “choose a suitable object” identifies further mathematical work unless a way to make that choice is already supplied.

#### MATH.4:4.4 - Define the operation and establish its result

For a natural-number input, let `b` be the base witness and let `step(n,y)` produce a witness for `n+1` from one for `n`. Define:

`F(0)=b`

`F(n+1)=step(n,F(n))`.

The base argument establishes `P(0,F(0))`. The step argument establishes `P(n+1,F(n+1))` from `P(n,F(n))`. Induction therefore establishes the property for every natural number.

For another finite inductive input, give one defining clause and one property argument per constructor. Recursive calls use its immediate constituents. Evaluation terminates because these calls descend through a finite input construction, provided the operations within each clause terminate.

When different constructor expressions represent one object, the recursion first gives a function of expressions. To obtain a function of the represented object, establish that all its permitted expressions yield the same required output, using MATH.2. Alternatively, supply an additional rule that chooses one construction from the object. Keeping the construction as part of the input is also useful when its history matters.

For example, build a finite set with `Empty` and `Insert(a,S)` for `a` outside `S`. Returning `[]` at the base and prepending `a` at each step gives a list containing each element once. Yet `Insert(1,Insert(2,Empty))` and `Insert(2,Insert(1,Empty))` represent the same set and return `[1,2]` and `[2,1]`. Both are valid witnesses, but these clauses define a function of the insertion construction. If a function of the set is required and its elements have a supplied total order, strengthen the output requirement to an increasing list and insert each element in order. The unique increasing list then makes the output independent of insertion order. This repair uses the ordering operation and a stronger specification.

A dependent-type description can package the output with a proof of its property. Its first projection returns the witness; the other component justifies that witness for the stated input. An ordinary mathematical presentation may instead give the function and proof separately. Use the presentation needed for the receiving work.

#### MATH.4:4.5 - Use the witness and return after a changed requirement

Evaluate the construction for the needed input. Return the object and the property on which its next use relies. Reuse the general argument while its constructors, clauses and premises remain unchanged.

If the receiver needs another quantity, check whether the current result retains it. If a parameter or formation rule changes, return to the affected base or constructor clause. If constructions are newly identified, check whether the output still defines a function on those identified inputs. A failed clause can supply a counterexample or a more specific construction question.

An executable recursive construction is already an algorithm. Its operation count, storage and representation can become further design questions when the intended scale makes them matter. A faster implementation can retain the same mathematical specification; the correspondence between the two constructions needs its own argument.

Stop with the required witness, a reusable construction with its property, or a particular unresolved clause. Formalizing the same result in a proof assistant is useful when that receiving use needs it.

### MATH.4:5 - Archetypal Grounding

#### MATH.4:5.1 - Obtain quotient and remainder together

Given a natural number `n` and a fixed positive integer `d`, construct natural numbers `q,r` such that `n=q*d+r` and `0≤r<d`.

At `n=0`, return `(0,0)`. The equation holds, and positivity of `d` gives the remainder bound.

Suppose the result for `n` is `(q,r)`. To obtain the result for `n+1`:

- if `r+1<d`, return `(q,r+1)`;
- otherwise return `(q+1,0)`.

Because `r<d` and the values are integers, the second branch has `r+1=d`. In the first branch, `n+1=q*d+(r+1)`; in the second, `n+1=(q+1)*d+0`. Both branches preserve the required bound. This proves the recursive construction for all natural-number inputs.

For `d=3`, successive witnesses include:

| Input `n` | Witness `(q,r)` |
| ---: | --- |
| 0 | (0,0) |
| 1 | (0,1) |
| 2 | (0,2) |
| 3 | (1,0) |
| 4 | (1,1) |
| 5 | (1,2) |
| 6 | (2,0) |
| 7 | (2,1) |
| 8 | (2,2) |

The output for 8 determines both two completed groups of three and a remainder of two. Keeping only the remainder would lose the number of completed groups. MATH.2 explains which questions such a reduced result can still answer.

The construction takes one successor step per unit of `n`. It exposes the witness and proof economically as mathematics, but a large encoded integer can call for a different division algorithm. If division with the same convention is already supplied, use that operation.

Changing the parameter to `d=0` defeats the specification: no natural `r` satisfies `0≤r<0`. This returns a failed input condition before any recursive step. Extending the input to negative integers also requires a new case; the natural-number recursion does not cover that extension.

#### MATH.4:5.2 - Strengthen the construction to color a tree

Consider finite binary trees formed as `Leaf` or `Branch(left,right)`. A leaf is one vertex. A branch adds a new root with edges to the roots of its two constituent trees. The constituent vertices occur separately in the constructed tree.

The required output colors each vertex 0 or 1 so that each edge joins different colors. Suppose a first attempt always colors a root zero. At a new branch, using those subtree results unchanged would give edges from zero to zero.

Generalize the construction: `Color(t,c)` takes a tree and a required root color `c∈{0,1}`. Its result must have root color `c` and different colors across every edge.

- For `Leaf`, return its single vertex with color `c`.
- For `Branch(left,right)`, color the new root `c`, and use `Color(left,1-c)` and `Color(right,1-c)` for its constituent trees.

The leaf has no edge to violate the property. At a branch, the induction hypotheses supply the property within each constituent tree. Their roots have color `1-c`, so both new edges also join different colors. The construction therefore satisfies the specification for both choices of `c`.

For `Branch(Leaf,Branch(Leaf,Leaf))` with root color 0, the two children receive color 1 and the two grandchildren receive color 0. The strengthened parameter made the recursive step possible.

Now add edges beyond the tree construction. On a triangle, choosing colors 0 and 1 for two adjacent vertices forces the third to be 0 to differ from the second, but it then agrees with the first. The tree result therefore cannot provide the requested coloring for every graph. The new edge condition leads to a different construction or an obstruction, while the tree method retains its original use.

### MATH.4:6 - Bias-Annotation

A familiar induction proof can tempt the writer to leave the output operation implicit. Recover the witness produced in each case and the information the next case uses.

A second temptation is to keep the initial statement fixed even after the recursive step exposes missing information. The tree case needs both root colors; strengthening that specification repairs the construction.

Simple recursion can also look like a recommended implementation. The division case states its cost so that a mathematically useful construction can be replaced for a larger computational use.

### MATH.4:7 - Conformance Checklist

- Are the input constructors, supplied construction and parameter conditions stated?
- When different constructions represent one object, is any claimed function of that object independent of the construction or supported by a stated selection rule?
- Does each base case return an object satisfying the specification?
- Does every constructor clause use only supplied data and results justified for smaller inputs?
- When an auxiliary value or parameter is needed, do the strengthened specification, base and step agree?
- Are all case distinctions and witness-producing operations available for the claimed executable use?
- Do recursive calls descend through finite constituents, or is another termination argument supplied?
- Can the receiver obtain the witness and recover the property it uses?
- After a changed requirement, is the affected clause or missing construction identified?


### MATH.4:8 - Common Anti-Patterns and How to Avoid Them

**Prove existence while omitting the requested witness.** Recover the producing operation in each case. If the argument supplies no such operation, keep its existence conclusion and return the remaining construction question.

**Fill an uncovered case with an arbitrary value.** A total expression can still violate the specification. Check the value under the case's premises or expose the failed condition, as with division by zero.

**Use an induction hypothesis too weak for the step.** The tree's fixed-root-color attempt fails at the new edges. Quantify the needed color parameter and establish the stronger base and step.

**Recurse on an unchanged input.** The finite-constituent argument no longer establishes termination. Change the recursive calls or obtain a different well-founded argument.

**Transfer the proof after changing the input's formation.** The extra edge in the triangle is absent from the tree constructors. Reopen that new case before claiming the property for the larger family.

### MATH.4:9 - Consequences

The result is a reusable way to obtain witnesses, with a reason for the property each witness satisfies. Construction and justification expose the same case boundaries, making a changed premise easier to locate.

Strengthening the result can add parameters or auxiliary values. Those additions cost representation and calculation but can supply the information that makes the inductive step work.

An efficient implementation remains a further opportunity when the simple construction is too costly.

### MATH.4:10 - Architectural Rationale

The input's formation rules determine the cases. Pairing each output rule with its property argument links object construction, reasoning and computation without requiring a proof-assistant language.

The stronger specification is part of the construction method. It lets a smaller-input result provide what a larger input needs, as the root-color parameter shows. Returning the witness separately from optional proof packaging keeps the result usable in different mathematical and computational descriptions.

Structural recursion was selected because finite constituent structure supplies a local termination argument. Finite enumeration is a serious alternative for one small instance, and an existing operation can be the cheapest way to obtain its answer. Inductive construction earns its extra work when a family, reusable operation or premise-sensitive argument is needed.

The division and tree cases use different objects while sharing the base-and-constructor move.

### MATH.4:11 - SoTA-Echoing

**Question:** how can a specification over inductively formed inputs produce a witness-building operation and a reusable correctness argument?

**Adopt** the induction and computation rules from Egbert Rijke's [*Introduction to Homotopy Type Theory*](https://arxiv.org/pdf/2212.11082), §3.1, printed pp.19-22. Section 4.6, pp.33-34, supplies dependent pairs and their projections as one formal presentation of an output with dependent information. The pattern uses these construction questions in ordinary mathematical language; it does not require univalent foundations for the examples.

The current [*Theorem Proving in Lean 4*, §8.3](https://lean-lang.org/theorem_proving_in_lean4/Induction-and-Recursion/) gives an operative comparison: recursive definitions and induction follow the input constructors, with recursive calls on smaller constituent terms. **Adapt** that organization here by foregrounding the wanted witness and strengthening the result when a step cannot be built. The integer and tree constructions are authored examples of the method.

The book's [axiom-of-choice discussion](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/) shows why formal existence and executable witness production require separate attention: definitions that manufacture data through classical choice are noncomputable in that setting. This makes recovering the output rule consequential; classical reasoning about an independently computable operation can still be useful.

Direct enumeration or a supplied operation can answer a small instance with less construction work. Reopen the selected method when the input is no longer finite and inductively formed, a required choice lacks an obtaining operation, or execution cost calls for another algorithm. The set example adds the representative-independence question supplied by MATH.2: producing a witness from each expression and defining one function on identified inputs require different arguments.

### MATH.4:12 - Relations

- **Uses FPF B.5.RC and B.5.RA when needed:** recover an unfamiliar input construction or proof before choosing the cases.
- **Connects with MATH.1:** a witness can itself be a constructed path; a changed step can alter its permitted joins.
- **Uses MATH.2 when input constructions are identified:** establish whether the output is independent of their representative. MATH.2 also helps retain the information needed by the next operation when simplifying a witness.
- **Connects with FPF B.5.RR and B.5.QD:** locate the first failed clause after a changed premise and develop the resulting construction question.
- **Connects with FPF C.29 and C.29.2:** interpret the mathematical result and relate an executable procedure to its claimed result.
- **Connects with algorithm design:** compare other constructions, representations and resource use while preserving the needed specification.

### MATH.4:End
