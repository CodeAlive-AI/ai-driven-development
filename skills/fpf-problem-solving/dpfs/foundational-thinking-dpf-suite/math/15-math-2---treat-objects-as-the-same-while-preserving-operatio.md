## MATH.2 - Treat Objects as the Same While Preserving Operations (Quotient)

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.2:1 - Problem frame

Use this pattern when you want to treat several mathematical objects as one because a working question appears not to distinguish them. You still intend to apply operations to the resulting classes. The recurring difficulty is that two apparently interchangeable inputs can produce different classes of output, or permit different next operations.

Start with the proposed identification and one operation the receiver will use. Find two identified inputs and apply that operation. A differing output class, or availability after only one input, is already a useful counterexample. Repair the identification or change the intended use before calculating with the classes.

The method constructs a quotient: a set of equivalence classes with operations inherited from the original objects. You need elementary sets, relations and functions. It applies to specified total operations, and to partial operations under the additional domain condition in :4.3. When individual objects already support the question economically, use them directly.

### MATH.2:2 - Problem

An equivalence relation makes classes, but by itself it does not determine usable operations on those classes. An operation defined by selecting a representative is ambiguous if a different representative changes the returned class.

There is a second loss to check: even a mathematically sound quotient may discard the quantity or distinction the receiver wants. The task is to construct an identification that preserves both the selected operations and the intended class-level question, or to expose why the proposed identification cannot do so.

### MATH.2:3 - Forces

| Force | Tension |
| --- | --- |
| Fewer objects and retained operations | Merging objects simplifies reasoning but may erase a distinction used by an operation. |
| A convenient resemblance and an equivalence relation | Closeness or one shared property may suggest a grouping without giving reflexivity, symmetry and transitivity. |
| Total and partial operations | Matching returned classes is enough for a total operation; a partial operation also has an availability condition. |
| Valid quotient and useful answer | An operation can descend to classes while the receiver's requested quantity cannot. |

### MATH.2:4 - Solution

**Local mantra:** choose what may be identified; test the operations; repair the distinction; form the classes; answer only what those classes determine.

#### MATH.2:4.1 - Specify the carrier, operations and receiving question

Name the set `A` of objects and the operations to retain. An n-ary total operation `f` maps every tuple in `A^n` to an element of `A`. A partial operation has a stated domain `D_f⊆A^n`.

When an operation takes inputs from different sets or returns a result in another set, choose an equivalence relation on each participating set. Compare corresponding inputs under their sets' relations and the resulting outputs under the output set's relation. A transition on states and concatenation of paths are different operations; choose the one actually used by the proposed identification.

State the receiving question. For example, the receiver may need the parity of a sum, the cost of a continuation, or whether a next step is available. This determines which distinctions a useful quotient can lose.

#### MATH.2:4.2 - Make the proposed equality into an equivalence relation

Write `a~b` for the proposed identification. An equivalence relation is reflexive, symmetric and transitive. Its class `[a]` contains all objects identified with `a`; these classes partition `A`.

If the candidate is a resemblance, test the missing law before forming classes. For instance, on integers `a~b` defined by `|a-b|≤1` is reflexive and symmetric but fails transitivity: 0 is related to 1 and 1 to 2, while 0 is not related to 2.

You can refine a proposed relation by retaining an additional property. Requiring both `a~b` and `h(a)=h(b)` remains an equivalence relation when `~` was one. Choose `h` from the failure that matters to the operation or query. The repaired relation still needs the operation test.

#### MATH.2:4.3 - Test compatibility, including the domain of a partial operation

For a total operation `f`, compare tuples whose corresponding entries are equivalent. The compatibility condition is:

`a1~b1, …, an~bn ⇒ f(a1,…,an)~f(b1,…,bn)`.

An equivalence relation satisfying this condition for every retained total operation is a congruence for those operations.

For a partial operation, first require agreement about whether it can be applied:

`a1~b1, …, an~bn ⇒ ((a1,…,an)∈D_f ⇔ (b1,…,bn)∈D_f)`.

Where both tuples are in the domain, require equivalent outputs as above. This pattern uses the resulting quotient convention in which availability is independent of the representative. A set-valued or approximate account that deliberately combines differing possibilities is another construction.

Use an algebraic argument for a general claim, or exhaustive checking when the specified carrier is finite. A few successful examples can suggest the relation; one failure is enough to refute compatibility.

If the test fails, keep the distinguishing information in the objects or narrow the operation/question being claimed. For a finite partition, split the failing class using the exposed distinction and retest the affected operations. This is a local repair; repeated splitting is not being offered here as a general minimization algorithm.

#### MATH.2:4.4 - Define the quotient operation and show that it is well defined

When the conditions hold, form `A/~`, the set of classes, and define the inherited operation by:

`f_bar([a1],…,[an])=[f(a1,…,an)]`.

The right side is independent of the chosen representatives precisely because compatible inputs return equivalent outputs. For a partial operation, agreement of domains also makes its availability independent of that choice.

This argument is reusable for unchanged conditions. The useful result is an operation on classes, together with the relation and the reason it is valid. There is no need to reproduce the proof for every subsequent calculation with the same quotient.

Preserve a representative or a way to construct one when later work needs an individual object. Knowing only a class may be sufficient for one answer and insufficient for a later request about a member.

#### MATH.2:4.5 - Check which answers can be recovered and use the result

A value `q(a)` can be recovered from `[a]` when it is constant on that class: `a~b ⇒ q(a)=q(b)`. Then define `q_bar([a])=q(a)`. If this fails, return to the original objects, retain more information, or return the range of possibilities when that answers the question.

Use the quotient for the declared operations and answers. A new operation or query can require a finer relation. The old quotient retains its earlier use; revise the part that the new question distinguishes.

Stop with a valid class-level operation and usable answer, or with a counterexample identifying the lost operation or quantity. Additional formalization is useful only when it resolves a remaining mathematical or receiving question.

### MATH.2:5 - Archetypal Grounding

#### MATH.2:5.1 - Absolute value fails, parity works for addition

Suppose integers are identified when they have the same absolute value. Then 1 and -1 are identified. Add the same integer 1 to both: the results are 2 and 0, which have different absolute values. This equivalence relation therefore cannot support addition inherited from integer representatives.

For a question about parity, choose a different relation: `n~m` when `n-m` is even. Reflexivity, symmetry and transitivity follow from the corresponding facts about differences divisible by 2.

If `n~n'` and `m~m'`, then `(n+m)-(n'+m')=(n-n')+(m-m')` is even. Addition therefore preserves the relation. There are two classes:

| `+` | Even | Odd |
| --- | --- | --- |
| Even | Even | Odd |
| Odd | Odd | Even |

The class of 7 plus the class of 4 is Odd. This answers the parity question using two classes. It does not determine whether the sum is 11 or another odd integer; a request for the sum itself requires the operands or more information.

Now request multiplication as well. The earlier addition argument does not settle the new operation. Here a separate calculation does:

`n*m-n'*m'=(n-n')*m+n'*(m-m')`.

Both terms on the right are even when the corresponding inputs have the same parity. The quotient can therefore also support multiplication. The changed request led to a new compatibility argument while preserving the earlier addition result.

#### MATH.2:5.2 - A location class loses availability

Let `V0` and `V1` be states at location `V`, without and with permission. A partial transition `r` is defined at `V1` and returns `T`; it is undefined at `V0`.

The proposed location-only relation identifies `V0~V1`. Output comparison alone would find no conflicting pair of returned values, because one value does not exist. The domain test detects the failure: `V1∈D_r` and `V0∉D_r`.

Refine the relation to retain permission. The two states are now in different classes, and the inherited transition is available only on the class containing `V1`. In MATH.1's route case, this retains the permitted `q;r` of cost 6 and excludes the apparent `p;r` of cost 3.

A convention that declares a class enabled whenever any representative is enabled would answer a different question: a transition is possible from some member. To execute it from the actual state, that convention still needs a suitable member or an enabling step. The present construction preserves the availability of the given operation at the represented state.

#### MATH.2:5.3 - Identifying words changes the question they answer

Take the one-generator paths `a^n` from MATH.1, with concatenation `a^m;a^n=a^(m+n)`. Impose `a^2~a^0` and choose the smallest equivalence relation compatible with concatenation that contains this equation.

Compatibility propagates this equation under concatenation. Adding one `a` gives `a^3~a`, and repeated deletion of a pair reduces every even-length word to the empty path and every odd-length word to `a`. These two groups remain distinct: parity itself is a compatible relation satisfying the imposed equation, as :5.1 shows, so the smallest such relation cannot identify opposite parities. This yields two classes and a composition table identical to the addition table above.

The quotient can describe the parity of repeated toggling. It discards the number of toggles. If each use takes time, elapsed cost cannot be recovered from those two classes alone. Retain the length or accumulated cost for a question that consumes it.

#### MATH.2:5.4 - Normalize labelled values before identifying them

A temperature-checking method accepts values labelled Celsius or kelvin. It converts them to kelvin, then tests membership in the inclusive interval [273.15,303.15]. Grouping inputs by their numeral alone loses the answer: 20 Celsius becomes 293.15 kelvin and passes, while 20 kelvin fails.

Let n(v,C)=v+273.15 and n(v,K)=v. Identify inputs when their n-values agree. Every input has a normalization result, and identified inputs have equal results; both the normalization and the following interval test therefore descend to these classes. This uses the separate input and output sorts of :4.1.

A later question about the original unit cannot be answered from the class alone. Retain the label when that question matters. If the description of the working method places comparison before normalization, Method Engineering A.3.1.CC:4.4 helps locate and repair that contradiction. The mathematical compatibility test and the repair of the described work answer different parts of this example.

### MATH.2:6 - Bias-Annotation

A shared appearance or outcome can make identification seem self-evident. The absolute-value case tests that intuition through an operation, and the permission case tests it through availability.

Compression can also look like improvement simply because there are fewer classes. The query condition in :4.5 keeps the receiving answer in view. A larger description can be preferable when it retains a consequential distinction.

### MATH.2:7 - Conformance Checklist

- Are the carrier, retained operations and receiving query identifiable?
- Does the relation used to form classes satisfy equivalence, rather than only resemblance or proximity?
- Do equivalent input tuples give equivalent outputs for every operation claimed on the quotient?
- For each retained partial operation, is availability also independent of the representative?
- Does the quotient definition return one class without requiring an unstated representative choice?
- Is the requested answer constant on the relevant classes, or is the lost information explicitly retained or returned as possibilities?
- Has a changed operation or query been checked at the condition it changes?

A counterexample closes a failed proposed identification. It does not require a completed replacement quotient before it can be useful.

### MATH.2:8 - Common Anti-Patterns and How to Avoid Them

**Use a resemblance as if it partitioned the set.** The distance-at-most-one example fails transitivity. Establish the relation being used before computing with its classes.

**Check outputs but ignore availability.** In the permission case, the absence of one output is the failure. Include the domain condition when operations are partial.

**Treat any valid quotient as adequate for every query.** Parity supports addition of classes while losing the numerical sum. Check the value the receiver actually asks for.

**Impose one equation but ignore its consequences under composition.** Identifying `a^2` with the empty path also identifies `a^3` with `a`. Carry the equation through the retained operation, or keep the objects distinct.

### MATH.2:9 - Consequences

A successful construction gives equivalence classes on which the retained operations remain meaningful. It can reveal a simpler mathematical structure, such as addition on two parity classes.

A failure identifies the information that the proposed grouping would erase. This can improve the original formulation, expose an unavailable continuation, or suggest a better question before an algorithm is built.

Refinement preserves more information and can increase the cost of representation and calculation. Deliberate approximation or set-valued abstraction can be worthwhile alternatives when their weaker answer is useful; they require their own stated operation and result conditions.

### MATH.2:10 - Architectural Rationale

Quotient construction and result transfer answer related but different questions. Here the mathematical operation on equivalence classes is constructed and its well-definedness established. A subsequent interpretation determines whether those classes and operations answer a question about another subject.

The domain condition is explicit because partial operations can fail before returning a value. The permission example would pass an output-only test vacuously, yet the intended next step would depend on the representative. Preserving availability repairs that defect.

The receiver's query remains separate from operation compatibility. A congruence can make addition well defined and still lose the requested sum. This separation lets one quotient remain useful for parity while a different use retains the individual numbers.

The method is about the particular identification proposed. Broader search for an optimal quotient, automated state minimization or a learned abstraction can reuse these conditions while supplying additional algorithms and selection methods.

### MATH.2:11 - SoTA-Echoing

**Question:** when can operations be inherited by classes without depending on an arbitrary representative?

**Adopt** congruence and quotient algebra from Burris and Sankappanavar, [*A Course in Universal Algebra*, corrected 2012 edition](https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf), Chapter II §5, pp.35-36. The compatibility condition and quotient definition supply :4.3-:4.4 for total operations. This is a constructive answer whose general reason applies beyond any one example.

The serious alternative is an equivalence relation chosen only by a shared property. It costs less to state, but the absolute-value example cannot support the required addition. The compatibility argument adds work where the quotient operation is claimed and resolves that ambiguity.

**Adapt** the construction to the partial-operation use by preserving domain membership as well as output classes. The alternative existential convention permits an operation when some class member permits it. That is useful for a possible-transition question but loses availability at the represented state. The permission case selects the stronger convention and places its added condition in :4.3. The cited total-algebra passage does not supply this partial-operation convention.

**Adopt** the composition consequences of imposed path equations from Fong and Spivak's [*Seven Sketches in Compositionality*](https://arxiv.org/pdf/1803.05316), §3.2.2, pp.84-85, in :5.3. Reopen the choice if the receiving question accepts a weaker bound or set of possibilities at lower cost, or a new operation distinguishes members of an existing class. Neither source establishes that a particular physical or organizational interpretation is adequate.

### MATH.2:12 - Relations

- **Uses or follows MATH.1:** a generated path structure provides objects and composition to identify.
- **Connects with FPF C.29.1:** use the quotient and its map in a wider result correspondence; check the subject interpretation separately.
- **Connects with FPF A.3.3.PI:** a description can lose a distinction needed to predict continuation; the present method supplies the quotient-side operation and domain test.
- **Connects with FPF B.5.RR and B.5.QD:** revise the argument after a changed operation, or turn a counterexample into a new construction question.

### MATH.2:End
