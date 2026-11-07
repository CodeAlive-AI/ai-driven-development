## MATH.12 - Extract a Construction from a Proof

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.12:1 - Problem frame

Use this pattern when a mathematical proof says that an object can be obtained, but you still need the operation that obtains it. The proof may describe the object through several intermediate results, hide it inside a pair, or use cases whose choice must be made from the input.

Recover the values and operations carried by the argument. A proof that a number is divisible by four can supply the quotient; a proof connecting two function types can supply transformations between their functions. When a step supplies only existence, the same reading identifies the construction still needed.

**First useful move:** find where the wanted object is introduced. Write the expression for that object and the inputs used to form it. Follow each needed input back to a supplied value, an available operation or a missing construction.

The reader needs functions, pairs, case distinctions and elementary mathematical reasoning. The arithmetic cases use integers and fractions. The function case explains its own notation. Use an already available operation directly when it returns the required object. An existence conclusion can be sufficient when the receiving question does not require obtaining a witness.

This method works through constructive proof steps and their computation rules. A claim about every input needs a construction that can be applied to every input in that scope. Some proofs establish their conclusion without supplying such a construction; :4.4 determines what can still be used from them.

### MATH.12:2 - Problem

Knowing that an answer exists can leave the next calculation impossible to perform. Even when a proof contains an answer, its presentation may separate the values needed to compute it or suppress their dependencies.

There is also a possible mismatch between mathematical reasoning and execution. A proof can distinguish two cases without providing a procedure that selects one. A formal system can store an existence proposition in a form that does not expose its witness as program data.

The needed result is an operation with stated inputs and an argument that its output satisfies the requested relation. A missing branch decision, unavailable auxiliary operation or unsupported termination claim is a specific remaining problem.

### MATH.12:3 - Forces

| Force | Tension |
| --- | --- |
| Existence and obtaining an answer | Existence may settle the mathematical question; a subsequent calculation can require the witness itself. |
| Concise proof and visible dependencies | An omitted intermediate value saves exposition but can prevent reconstruction of the operation. |
| General statement and available input | An argument for each input must retain the information on which its witness depends. |
| Mathematical correctness and execution | The proof's logic and a program's evaluation rules need a correspondence for the claimed computational use. |
| Equal outputs and affordable use | Two extracted expressions can return the same result while repeating different amounts of work. |
| Reusable proof and changed premises | A local assumption change can alter a branch, an output type or the computation that uses it. |

### MATH.12:4 - Solution

**Name the wanted output → recover its construction → compose the supplying steps → check computation → obtain the witness → revise affected dependencies.**

#### MATH.12:4.1 - State what must be obtained

Name the input x, any parameters and the relation R(x,y) required of the output y. A statement “for every x there is a y satisfying R(x,y)” leaves the next task open until the needed y can be supplied.

State what the input actually contains. A value with an associated proof, a procedure returning such a value, and a proposition asserting that some value exists support different operations. For example, a pair (k,p), where p justifies n=4k, supplies k by projection. A statement that n is divisible by four may require recovering or constructing that k.

Keep the order of dependence. The output of “for each x, construct y” may depend on x. It does not thereby supply one y that works for every x.

When the argument is unfamiliar, B.5.RA can recover its premises and deductions before this computational reading.

#### MATH.12:4.2 - Recover what each proof step supplies

Begin at the desired conclusion and follow the steps needed to produce its object. Give each supplied value a name. For a lemma used along the way, recover the obtaining operation when the next step consumes its output as data.

The following constructions give a small working repertoire:

| Form of the argument | Construction to recover | How its result is used |
| --- | --- | --- |
| Given x, construct t(x) | A function `x ↦ t(x)` | Supply a particular input and evaluate t at that input. |
| Construct both b and c | The pair (b,c) | Project the component needed by the next step, or retain both. |
| Establish one of two cases constructively | A tag naming the chosen case and the data for that case | Select the corresponding branch using that tag. |
| Exhibit y and establish R(x,y) | A pair containing y and its justification | Return y; use the second component when the next argument needs the property. |
| Use an already constructed operation f on a value a | The application f(a) | Feed the returned value to the next construction. |

A constructive disjunction carries which case holds. If the source argument provides no such choice, name the missing decision before turning it into a conditional program.

For an inductive argument, recover the base and constructor operations through MATH.4. That pattern also handles a step that needs a stronger result. The present method assembles the values supplied by those operations with the other proof steps.

#### MATH.12:4.3 - Compose the operations and simplify their use

Substitute each supplied result into the place that consumes it. Preserve names for inputs whose values differ or whose dependencies matter.

Some simplifications directly expose a wanted value:

- Applying `x ↦ t(x)` to a gives t with a substituted for x.
- The first component of (b,c) is b; the second is c.
- A case distinction applied to a tagged value runs the branch named by its tag.

These are computation rules for the chosen constructions. Use their conditions, including the input type and any variable binding. Rename an auxiliary variable when substitution would confuse it with another input.

For a proof supplying a dependent pair p(x)=(y,q), define F(x) as its first component. The second component then supplies R(x,F(x)). This gives both an obtaining operation and the relation its output satisfies, provided the construction of p(x) is available.

Write the resulting expression or procedure in a representation the receiver can use. A short formula can be sufficient. Pseudocode or a proof-assistant term is useful when its evaluation or composition is the next question.

#### MATH.12:4.4 - Determine which computation the argument supports

Inspect every operation on which the returned data depends. Is it supplied? Does it return on the permitted inputs? Can the case distinctions be decided? Finite composition of terminating operations gives an obtaining procedure; recursion needs its stated termination argument.

A proof step that invokes a classical choice of an element does not, by that invocation alone, give an executable choice procedure. Retain the existence result and either obtain a construction for that step or use another proof that supplies one. Classical reasoning can still justify a separately defined computable function.

Suppose a finite list is supplied together with a terminating test P and a proof that some listed element passes. Test the elements in order and return the first that passes. The list makes the search finite, and the proof rules out exhaustion without a result. For [2,5,8] and P(n)=(n>6), this returns 8 after three tests. The existence proof may use classical reasoning: the returned data comes from the search.

For a formalized proof, inspect the system's actual rules for data and proofs. In Lean, for example, an existential proposition in `Prop` is not a data-bearing dependent pair whose witness a program may simply project. A value packaged in a data type with a proof of its property can retain its data while compilation erases the proof. Choice used to manufacture the data is a separate computational issue.

The chosen logic and evaluation rules determine the proof-to-computation correspondence. General recursion can describe a computation that never returns; its type alone need not establish the requested terminating construction. An ordinary proof narrative also needs its object-producing steps recovered before it provides that construction.

#### MATH.12:4.5 - Obtain the result and use its justification

Apply the extracted operation to the input of interest. Follow its reductions far enough to obtain the requested value, and use the proof's retained relation to justify that value.

A worked input checks that the expression can be followed. The general output claim comes from the construction and its proof under the stated assumptions. Where the representation can overflow, round or reorder dependent updates, establish that its operations preserve the mathematical result needed here.

Retain intermediate results when recomputation would matter. A proof transformation that preserves a function's output can still duplicate an expensive calculation. Compare implementation choices under the same output requirement.

For work on another subject, use C.29 to establish the correspondence between the mathematical construction and that subject. C.29.3 connects a computation with its input preparation, execution and result interpretation. A mathematical function transformation can inform a change of method while the changed method still needs its physical, resource and interaction conditions.

Stop with the required object, a reusable obtaining operation with its property, or the particular premise that still lacks a construction.

#### MATH.12:4.6 - Return to the changed dependency

If only the input value changes within the proved scope, apply the same operation. If a premise changes, locate the earliest producing step or branch that uses it.

A stronger output requirement can need an additional value. A changed representation can remove a previously available projection or decision. Reconstruct that part, then follow its effects through the receiving expressions and justification.

When different input descriptions are identified, MATH.2 determines whether the obtained output is independent of the description; MATH.7 can carry it through a reversible representation. B.5.RR follows changed premises through the surrounding argument.

### MATH.12:5 - Archetypal Grounding

#### MATH.12:5.1 - Recover the witness in an arithmetic argument

For integers a,b, a proof shows that `(a+b)^2-(a-b)^2` is divisible by four. The receiver wants the quotient.

Expanding the squares gives:

`(a+b)^2-(a-b)^2 = 4*a*b`.

The existence statement is “there is an integer k such that the difference is 4k.” Its witness-introducing step chooses `k=a*b`. The extracted operation is therefore multiplication of the two inputs, with the displayed identity as its justification.

At a=3,b=2, the difference is 25-1=24 and the operation returns k=6. The receiver can use 6 without reconstructing the expansion on every input.

Now ask for divisibility by eight. The old proof supplies 4ab, which is insufficient: at a=b=1 the difference is 4. A supplied stronger premise a=2r repairs the construction:

`4*a*b = 8*r*b`.

The new witness is `r*b`. If the input already carries r, the procedure uses it. If only an assertion that a is even is supplied, obtain the integer r with a=2r or use an available integer-division operation with its conditions. The changed proof identifies both the new premise and the additional input needed by its expression.

#### MATH.12:5.2 - Read a function equivalence as two transformations

Suppose f maps each a in A to a pair in B×C. A proof can split this into two functions by projecting its output:

`Split(f) = (a ↦ first(f(a)), a ↦ second(f(a)))`.

Conversely, given g:A→B and h:A→C, pair their values:

`Join(g,h) = a ↦ (g(a),h(a))`.

Applying Join after Split gives, at each a:

`(first(f(a)),second(f(a))) = f(a)`.

Applying Split after Join returns g and h pointwise. Thus the argument supplies transformations in both directions, together with the equalities that justify using the returned functions.

For `f(n)=(n+1,n^2)`, Split gives `g(n)=n+1` and `h(n)=n^2`. Joining their values at n=3 returns (4,9). The projections and applications are the computational content of the proof.

The equality concerns functions with values determined by their input. If evaluating f is expensive, the expression using two calls can repeat work; calculate f(a) once and keep its pair when both components are needed.

If the proposed implementation instead reads and increments a hidden counter, repeated calls change the situation. A single call returning (c,c) might give (1,1), while separate component calls yield (1,2). This no longer implements the fixed mathematical f used by the proof. Include the changing state in the model and reconsider the transformation before using this function equivalence to reorganize the work.

#### MATH.12:5.3 - Extract a case decision and its answer

For a rational input r=p/q, with integer p and positive integer q, construct either an indication that r=0 or a rational y such that r\*y=1.

The proof examines the decidable integer condition p=0:

- If p=0, return `Zero` with the equality r=0.
- Otherwise return `Inverse(q/p)`. Since p is nonzero, the fraction is defined, and `(p/q)*(q/p)=1`.

The result includes which case holds. At p=4,q=6 it returns `Inverse(3/2)`. At p=0,q=5 it returns `Zero`. This tag lets a receiving calculation choose its continuation.

Merely reporting that one of the two conclusions holds loses the branch information the continuation needs. The construction obtains that information by testing an integer, then carries it with the result.

Now replace the rational representation by access to successively narrower rational intervals enclosing an arbitrary real number. The rational procedure's test p=0 is no longer available. A nondegenerate rational interval containing zero does not by itself establish that the represented real is zero, because it also contains nonzero values. An interval [0,0] would establish equality, but the representation does not guarantee reaching such an interval. The previous proof does not supply a terminating zero test for this representation.

The next move is to obtain an appropriate decision procedure under additional input conditions, change the requested output to allow an unresolved case, or retain the existence conclusion without claiming the obtaining operation. The rational construction remains usable on its stated inputs.

### MATH.12:6 - Bias-Annotation

A familiar proof can make its witness look obvious to an author while leaving a reader without the expression that produces it. Starting at the witness-introducing step exposes that omission.

A second bias is to treat logical existence, a computable selection and an efficient implementation as one result. The branch and function cases make their different requirements visible through changed inputs and repeated work.

### MATH.12:7 - Conformance Checklist

1. The requested output and its relation to the input are stated.
2. Each data-consuming step has a supplied value or an obtaining operation.
3. Witness dependencies follow the statement's quantifier order.
4. Pairs, projections, functions and case tags retain what the next step consumes.
5. Every claimed executable branch has its decision, and a terminating construction has the needed computation argument.
6. The selected representation exposes the required data. An executable construction has an available procedure for every choice used to produce its data.
7. The extracted expression produces the worked result under the original relation.
8. A changed premise returns to its affected construction and receiving uses.

Recognition can recover one witness-producing step. Assurance of the general obtaining operation examines the dependencies and computation rules needed for that claim.

### MATH.12:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Read “there exists” as an available obtaining operation | Recover the witness-producing step or name the construction still needed. |
| Turn an unspecified disjunction into an executable branch | Supply a decision and return its case tag with the relevant data. |
| Change a witness that depends on x into one fixed witness for every x | Keep the input parameter and the statement's quantifier order. |
| Project program data from a formal proposition that does not expose it | Use an appropriate data-bearing construction or obtain the value by another supported method. |
| Infer termination from a program type that permits general recursion | Establish termination for the actual computation or retain its partial scope. |
| Replace one calculation by repeated calls while forgetting changing state or cost | Retain shared results and restore the state needed by the mathematical model. |

### MATH.12:9 - Consequences

The proof becomes usable for obtaining an object and for locating what changes when its premises change. Its constructive parts can be composed or assigned to different contributors through their stated inputs and outputs.

The recovered operation may be inefficient or depend on an unavailable decision. These are specific construction or implementation questions, which can be pursued while retaining the logical result already established.

### MATH.12:10 - Architectural Rationale

The central move reads object production through the structure of a proof. Function application, pairing and case analysis let a receiver carry the proof's intermediate results into the wanted output. Their computation rules explain why simplifying the construction preserves that output.

Inductive witness construction is one contributor. Recovering and assembling the computational content of an arbitrary supported argument also involves non-inductive steps, as the arithmetic identity and function equivalence show.

The correspondence between proofs and programs depends on the logic, data representation and evaluation rules. Keeping those choices explicit makes the connection usable: one can recover a mathematical construction, choose an implementation and then ask how it operates in the receiving subject.

### MATH.12:11 - SoTA-Echoing

**Adopt** the proof/construction correspondence explained by Philip Wadler in *Propositions as Types*, especially §3 and the paired proof and computation rules in §§6-7. Its useful contribution here is to reconstruct operations from proof structure rather than treat a logical consequence as a finished obtaining procedure. Sections :4.2-:4.3 and the function case use that distinction. The selected correspondence concerns a stated logic and typed computation; a different calculus can require different rules. [Author's paper](https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf).

**Use** Egbert Rijke's *Introduction to Homotopy Type Theory*, §2.2 and §4.6, for function application and dependent pairs with their projections. These give :4.3 a way to retain the witness together with its dependent property. The pattern presents those constructions without requiring the broader univalent foundation. [Book](https://arxiv.org/pdf/2212.11082).

**Compare** current Lean's *Axioms and Computation* with a blanket interpretation of every existence proof as executable witness production. Its distinction between proof erasure, computation and classical choice changes :4.4: trace the data-producing operation and the evaluation actually claimed. Classical reasoning can remain in a correctness argument for an independently computable function. [Lean documentation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/).

For an implementation using program extraction, Rocq's *Program extraction* explains how logical content, informative axioms and supplied realizations affect the extracted code. This supports checking the actual extraction assumptions rather than reading a successful proof as validation of arbitrary inserted implementation code. Such implementation work becomes useful when the receiver needs executable code; it is not required for the hand calculations here. [Rocq 9.1 documentation](https://rocq-prover.org/doc/V9.1.0/refman/addendum/extraction.html).

Reopen the chosen method when a needed proof rule has no available computational interpretation, a representation prevents a required decision, a source result changes that limit, or a more affordable construction provides the same wanted output.

### MATH.12:12 - Relations

- **B.5.RA** recovers an argument's premises and consequences. This pattern obtains the values and operations carried by its constructive steps.
- **MATH.4** constructs witnesses by induction; **MATH.5** extends assignments through mathematical composition. Their results can supply operations used in the extracted construction.
- **MATH.2** governs independence from identified input descriptions; **MATH.7** transports a construction through a bijection.
- **MATH.9** constructs a choice compatible with symmetry. Its existence and computation conditions remain relevant when the extracted result includes such a choice.
- **B.5.RR** revises an affected argument; **B.5.QD** develops a missing construction into the next mathematical question.
- **C.29.1** supplies a needed result-transfer argument; **C.29.2** develops a missing computational formulation; **C.29.3** connects a computation with its execution and interpreted result.

### MATH.12:End
