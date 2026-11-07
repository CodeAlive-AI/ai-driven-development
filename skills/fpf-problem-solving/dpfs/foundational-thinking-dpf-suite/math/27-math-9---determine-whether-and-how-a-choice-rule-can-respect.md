## MATH.9 - Determine Whether and How a Choice Rule Can Respect Symmetry

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.9:1 - Problem frame

Use this pattern when a mathematical rule must choose an answer and transforming the input should transform that answer in the corresponding way. Examples include selecting an element after relabeling a configuration, returning a direction after rotating geometric data, and choosing a solution from problems related by a symmetry.

Start with one transformation that leaves the supplied input unchanged. Ask which permitted answers it leaves unchanged too. This can identify an admissible answer or expose an impossible choice before a selector is implemented.

The method then constructs a rule from one suitable answer for each represented input orbit. It also uses uniqueness, when established, to restrict a solution to the points fixed by the input's symmetries. A useful result is a compatible choice rule, a restricted candidate to calculate, or a requirement that must change.

The reader needs sets, functions, composition and elementary algebra. MATH.8 supplies group actions, orbits and stabilizers; the definitions needed for the choice argument are restated here. The plane example uses vector length and rotation. If a supplied rule already has the required correspondence, apply it. If the task accepts any answer in the given coordinates and requires no symmetry relation, use an ordinary selection method.

### MATH.9:2 - Problem

A problem can allow several answers while supplying no distinction that a requested deterministic rule is allowed to use. An arbitrary tie-break can then violate relabeling or rotation consistency.

Normalization can hide the same difficulty. Two transformations may put the input into the same representative form but return a proposed answer to different places. A common representative alone leaves that choice unresolved.

The task is to determine which permitted outputs respect the symmetries of the supplied input, then extend those choices consistently to related inputs.

### MATH.9:3 - Forces

| Force | Tension |
| --- | --- |
| One answer and indistinguishable alternatives | A deterministic output may require a distinction absent from the input. |
| A symmetric problem and its individual solutions | Symmetry preserves the solution set; uniqueness supplies the additional step that fixes an individual solution. |
| Reduced input and returned coordinates | The transformation used for normalization can affect an output even when the normalized input is unchanged. |
| Pointwise consistency and other requirements | A rule can satisfy the transformation law while its evaluation is expensive or its values change discontinuously. |

### MATH.9:4 - Solution

**State the permitted answers and their transformation → find the input stabilizer → choose a permitted fixed answer → extend it along the orbit → construct the needed scope → return the rule or revise the obstructed requirement.**

#### MATH.9:4.1 - State the input, permitted answers and transformation law

Let D be the inputs and Y the possible outputs. Write A(d) for the subset of outputs permitted for input d. An admissible root, minimizing allocation or selected vertex can define this subset.

Give a group G acting on both D and Y. Its action satisfies `e*d=d` and `(g*h)*d=g*(h*d)`, with analogous rules for outputs; every transformation has an inverse. Different actions on input and output can use the same group elements.

Establish that the permitted answers transform with the input:

`A(g*d) = g*A(d)`,

where `g*A(d)` means the set of `g*y` for y in A(d). MATH.8 supplies the solution-preservation argument when it has to be constructed.

The requested deterministic rule f must satisfy both f(d) in A(d) and

`f(g*d)=g*f(d)`.

This relation is *equivariance*. If the requested output stays unchanged under the transformations, use the trivial output action `g*y=y`; the relation then expresses invariance.

Keep attributes that the rule is allowed to use inside d. A distinguished label, orientation or mark can change the stabilizer and the existence of a choice. A coordinate label that merely changes under relabeling cannot silently serve as a fixed priority.

#### MATH.9:4.2 - Find the permitted answers fixed by the input's stabilizer

The stabilizer of d is the subgroup

`K_d = {g in G | g*d=d}`.

For every g in `K_d`, equivariance requires `f(d)=g*f(d)`. Thus the permitted answers for an equivariant rule at d are

`B(d) = {y in A(d) | g*y=y for every g in K_d}`.

To construct B(d), first obtain the transformations fixing the supplied data, then solve their fixed-point conditions together with membership in A(d). For a finite supplied group and a finite decidable answer set, enumerate those elements and test them. When either is infinite, use an algebraic description or another available construction; a failed finite search leaves the unsearched range open.

If B(d) is empty, no deterministic equivariant rule can answer this input under these requirements. Return the input symmetry and the fixed-output condition that permitted answers fail. This result concerns the supplied data and output requirement; it identifies what a repair must change.

If the original problem has a unique permitted answer y, its preservation under `K_d` forces every `g*y` to equal y. The fixed-point equations can therefore restrict or find that answer. Establish existence and uniqueness on the range used by this deduction. With several permitted answers, use the same fixed-point calculation to find a compatible choice; it need not recover every permitted answer.

#### MATH.9:4.3 - Extend a selected answer over one input orbit

Choose representative data d0 and an answer y0 in B(d0). For input d in the orbit of d0, obtain g with `d=g*d0` and define

`f(d)=g*y0`.

The answer is permitted because the relation in :4.1 carries A(d0) to A(d). It is independent of the transformation used. Indeed, if `g1*d0=g2*d0`, then `k=g2^-1*g1` fixes d0. Since k fixes y0,

`g1*y0=g2*(k*y0)=g2*y0`.

The rule is also equivariant: for another transformation q,

`f(q*(g*d0))=(q*g)*y0=q*f(g*d0)`.

This constructs the entire rule on that orbit. To evaluate it, retain a way to find g, or an equivalent formula for f(d). An existence argument for g alone may leave the computation unresolved.

If a normalization procedure instead supplies h with `h*d=d0`, return `h^-1*y0`. Keeping the direction of this transformation prevents returning a coordinate answer in the normalized frame. The position-selection case in :5.4 carries out both inverse returns.

#### MATH.9:4.4 - Cover the requested input range

For a finite group acting on a finite input set, enumerate input orbits as in MATH.8. Pick one representative d0 per orbit, compute B(d0), choose one of its members and extend it by :4.3. This supplies a rule on every processed orbit. Empty B(d0) blocks a total rule on a range containing that orbit.

For a larger or infinite range, give the representative construction and a compatible answer for each orbit needed by the claimed rule. These choices can be supplied by formulas or previously established mathematical results. Pointwise nonempty B(d) alone has not provided an evaluation algorithm or the choices across an arbitrary infinite family.

When an existing direct formula can be checked against A(d) and equivariance, use it without building an orbit table. The stabilizer argument can still expose a failed input or explain why its tie-break works.

Before returning the rule, check the other properties actually requested for it. If a geometric or learned model must vary continuously with its data, continuity requires its own argument: the pointwise construction here permits unrelated choices on different input orbits. If the result will be computed repeatedly, compare its evaluation cost with the available direct rule.

#### MATH.9:4.5 - Repair an obstructed choice

Choose the change that answers the receiving problem.

A supplied distinguished attribute can reduce the stabilizer. Include that attribute and its transformation in the new input, then repeat the fixed-output test. The marked-cycle case below constructs such a rule.

A different output may retain the alternatives the input leaves open. Returning the whole set A(d) respects its induced transformation from :4.1. When A(d) is finite and nonempty, a uniform probability distribution on it does too, if a distribution is the requested result. Sampling a single value is a further calculation with its own randomness and comparison requirement.

An average is usable only when it belongs to the permitted output set and has the required transformation law. The mean of two opposite unit directions is zero, which fails a unit-direction requirement.

The receiving task may instead allow coordinate-dependent choice or a narrower input range. State that changed requirement and construct the corresponding rule. Adding distinctions or weakening a requirement is useful only when the resulting answer serves that task; C.11.DUA helps decide whether obtaining further input is worth its cost when that question is unresolved.

#### MATH.9:4.6 - Return the result and reopen its changed premise

Return the rule with its input range, permitted output and transformation law, or the obstruction that changes the choice problem. A known unique solution can return a smaller fixed-point calculation instead.

When a criterion, attribute or output changes, recalculate the affected stabilizer and fixed-output condition. Retain orbit calculations and proofs whose premises are unchanged. Small perturbations can remove a tie and reverse a selected answer, so use the changed criterion when the choice depends on it.

Use FPF C.29 to establish what this mathematical result means for another subject. The obstruction for an abstract arrangement leaves available attributes and interventions in a real arrangement to that subject comparison.

### MATH.9:5 - Archetypal Grounding

#### MATH.9:5.1 - Select a cheapest position on a cycle

Four positions are arranged in a cycle with a given clockwise direction. A rule receives real costs c=(c0,c1,c2,c3) and must select one minimum-cost position. Relabeling by k moves position j to j+k modulo 4 and moves its cost with it. The selected position must move in the same way.

Take c=(1,3,1,3). Its minimizers are {0,2}. A half-turn leaves c unchanged but exchanges both permitted answers. Neither is fixed, so B(c) is empty. A deterministic rotation-equivariant selector cannot answer this input. Choosing the smallest coordinate label returns 0 both before and after the half-turn, whereas equivariance requires the result to move to 2.

Now supply a marked position m as part of the input. Choose, among minimizers, the one with least clockwise distance

`dist_m(j)=(j-m) modulo 4`,

using the values 0,1,2,3. The distances are distinct, so this gives one answer. Under joint rotation of costs, mark and position, `dist_(m+k)(j+k)=dist_m(j)`. The rule therefore respects rotation for every cost vector and mark.

With c=(1,3,1,3) and m=3, the distances of minimizers 0 and 2 are 1 and 3, so the rule selects 0. Rotating once gives costs (3,1,3,1), mark 0 and selected position 1. The same reasoning applies to every rotation.

For the unmarked input, returning {0,2} is a compatible set answer. If a probability distribution is wanted, assign probability 1/2 to each of those positions. Both alternatives retain the choice left open by the input.

A change of costs can also settle it: (1,3,0.9,3) has the unique minimizer 2; (1,3,1.1,3) has the unique minimizer 0. Their closeness to the tied input does not preserve that input's fixed-point obstruction. It also exposes a discontinuity for a rule required to return one minimizing index as these costs vary through the tie.

#### MATH.9:5.2 - Restrict a unique optimum by exchange symmetry

Let x1,x2 be nonnegative real numbers with x1+x2=10, and minimize J=x1²+x2². Exchanging the two allocations preserves feasibility and cost.

If the minimizer is known to exist uniquely, the exchange must fix it. Hence x1=x2, and the constraint gives the candidate (5,5). For this example, existence, uniqueness and its optimality can also be established directly: every feasible point has the form (5+h,5-h), and

`J(5+h,5-h)=50+2h²`.

The minimum is attained only at h=0. The direct calculation can finish this small problem; the symmetry deduction is reusable when uniqueness has another available justification.

If the same J is maximized on the segment, its maxima are (10,0) and (0,10). The exchange moves one to the other. Its fixed midpoint is the minimum, so the fixed-point equation alone would solve the wrong optimization question.

Now minimize x1²+2x2² with the same resource constraint. Exchange changes the criterion. Substituting x2=10-x1 gives

`J=3*(x1-20/3)²+200/3`,

so the unique optimum is (20/3,10/3). The old equality x1=x2 no longer follows. MATH.10 supplies the more general admissible-variation construction when the remaining optimization is the difficulty.

#### MATH.9:5.3 - Return a direction after geometric normalization

The input is an unordered pair P={-v,v} of opposite nonzero vectors in the plane. The requested answer is one of the two unit directions along its axis. Rotating the input should rotate the selected direction.

For P0={(-1,0),(1,0)}, a half-turn leaves the pair unchanged and negates every permitted unit direction. No permitted output is fixed, so a rotation-equivariant deterministic direction cannot be selected from this input.

The same failure appears in normalization. Both the identity and a half-turn map P0 to the same standard pair. Selecting (1,0) there and undoing those transformations returns opposite directions. The standard pair did not determine a direction of return.

Returning both directions, `{-v/|v|,v/|v|}`, is compatible with rotation when that set is the required output. Averaging them returns zero, whose length is zero rather than one.

Alternatively, mark one endpoint w in P and return `w/|w|`. Every rotation R preserves length, so `R*w/|R*w|=R*(w/|w|)`. The marked-input rule is therefore equivariant. It answers a question with additional supplied information, which the unmarked pair lacked.

#### MATH.9:5.4 - Choose a position despite an ambiguous normalization

Let the six permutations of positions 1, 2 and 3 act on the triples formed by permuting d0=(a,a,b), where a and b differ. An answer may be any of the three positions, and relabeling the triple must relabel the answer.

The transformations fixing d0 are the identity and the swap of positions 1 and 2. All three positions are permitted answers, but only position 3 is fixed by both transformations. Thus B(d0)={3}; choose y0=3.

For the input d=(a,b,a), two transformations normalize it to d0. The first, h1, swaps positions 2 and 3. The second, h2, sends positions 1 to 2, 2 to 3 and 3 to 1. Both carry the b entry to position 3 while placing the two a entries in the remaining positions.

Returning y0 uses their inverses:

`h1^-1(3)=2=h2^-1(3).`

For every permutation of d0, the transported answer is the position carrying b. This gives the rule on the entire three-input orbit. The stabilizer calculation makes the return independent of the normalizer even though the input initially permits three different answers.

### MATH.9:6 - Bias-Annotation

Finite cycles make an obstruction or a constructive repair cheap to display. Larger symmetry groups can make stabilizers, representatives or their transformations expensive to obtain. The rule's mathematical existence and a feasible evaluation procedure remain different contributions.

A symmetry claim also depends on what is actually supplied. Position names used only for coordinates differ from a distinguished mark the problem permits the rule to use. Keep that difference when translating a real selection problem into the mathematical input.

### MATH.9:7 - Conformance Checklist

- The permitted-answer set and both group actions belong to the declared input range.
- The solution relation carries A(d) to A(g\*d).
- A selected representative answer is permitted and fixed by the representative's whole stabilizer.
- Different transformations reaching the same input return the same answer.
- The claimed range has the required representative and answer construction.
- Any changed input, output type or choice requirement is reflected in the returned rule.

### MATH.9:8 - Common Anti-Patterns and How to Avoid Them

**Use coordinate order as an unannounced priority.** The cycle's smallest-label tie-break fails a half-turn. Supply a distinguished priority that the task permits, or return the alternatives.

**Infer a symmetric optimum from a symmetric feasible set.** Preserve the criterion and establish the premise needed for the fixed-point deduction. The sum-of-squares maximum and weighted minimum give different answers.

**Normalize the input and discard the transformation.** An answer in source coordinates needs the inverse return. If several normalizing transformations remain, check their agreement on the proposed output.

**Average valid answers into an invalid answer.** The zero mean of opposite unit directions is outside the required output set. Test the averaged result's membership or retain the set.

**Call a compatible pointwise rule continuous.** The cycle's minimizing index jumps near a tie. Apply the receiving regularity requirement when it is part of the task.

### MATH.9:9 - Consequences

A fixed-output calculation can prevent work on an impossible selector and identify what information or output change would make it possible. Where a compatible answer exists, the orbit construction turns it into a reusable rule for related inputs.

Different representatives can support different valid rules. Their evaluation cost, continuity and usefulness for a receiving task can differ even when each satisfies equivariance. The mathematical construction supplies a comparison basis; the receiving requirements select the rule.

### MATH.9:10 - Architectural Rationale

The stabilizer condition is necessary because transformations invisible at the input must leave a deterministic answer unchanged. It is sufficient for extension over one orbit because those same transformations account for every ambiguity in how that orbit is reached. The construction supplies both the impossibility result and its positive counterpart.

MATH.8 generates solution families from an action. This method selects a compatible member and extends that selection across related inputs. A unique solution supplies the fixed-member condition automatically, but several permitted solutions can still contain a suitable fixed member.

A canonical input and a normalizing transformation are different outputs. Choosing the same input representative throughout an orbit is an invariant operation. Recovering an oriented answer additionally uses a transformation and its output action; :5.3 shows why that transformation may not be unique.

Orbit-by-orbit construction is preferable when its fixed-point test settles existence or produces a useful rule. A direct formula can avoid representative search. Set or distribution outputs answer different questions, and geometric continuity can require a construction beyond the pointwise rule.

### MATH.9:11 - SoTA-Echoing

**Question:** when does a symmetry-compatible deterministic choice exist, how can it be constructed, and which changed requirement resolves an obstruction?

[Milne, Group Theory v4.01, November 2025](https://www.jmilne.org/math/CourseNotes/GT.pdf), chapter 4 and exercise 4-1 with its solution, characterizes maps between transitive group actions through stabilizers. **Adopt** that mathematical relationship. The argument in :4.2-:4.4 develops it as a construction constrained by the permitted-answer set. [Mathlib's fixed-point action results](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/FixedPoints.html), including MulActionHom.map_mem_fixedPoints, supply the corresponding necessary preservation property.

[Ma and colleagues, A Canonicalization Perspective on Invariant and Equivariant Learning, 2024](https://proceedings.neurips.cc/paper_files/paper/2024/file/702b67152ec4435795f681865b67999c-Paper-Conference.pdf), §2.1, distinguishes canonicalized inputs from a single equivariant group-valued canonicalizer, which can be obstructed at inputs with nontrivial stabilizers. **Adapt** this distinction in :4.3/:5.3/:10. It gives a concrete alternative to assuming normalization has selected a unique return transformation.

[Dym, Lawrence and Siegel, Equivariant Frames and the Impossibility of Continuous Canonicalization, 2024](https://arxiv.org/html/2402.16077), §2.2, separates orbit and group canonicalization and examines continuity; §6 retains stabilizer-related conditions when extending weighted constructions to equivariant outputs. **Adopt** the separate regularity question in :4.4. Their weighted-frame methods address additional geometric-learning requirements; they are not replaced by the finite construction here.

An arbitrary tie-break is cheaper but can fail the requested transformation law. A supplied direct rule with that law is preferable when it already works. The orbit construction earns its cost by revealing impossible outputs or generating a consistent rule. The cases demonstrate those differences.

Reopen when the input attributes, action, permitted answer, demanded regularity or available construction changes.

### MATH.9:12 - Relations

- **Uses MATH.8:** obtain the action, solution-preservation relation, input orbits and stabilizers.
- **Uses MATH.2:** check independence when a calculation is defined on identified inputs; the stabilizer argument supplies the concrete independence proof here.
- **Connects with MATH.7:** carry a computed answer through the appropriate inverse map, including its output interpretation.
- **Connects with MATH.13:** use the existing unique-solution and output-obstruction deductions; this method also constructs the compatible rule.
- **Uses MATH.10 when optimization remains:** construct admissible variations after symmetry has restricted a candidate.
- **Uses C.29 for another subject:** recover which supplied attributes and outputs the mathematical choice represents.
- **Uses C.11.DUA when further information has a material cost:** decide whether acquiring the distinction can improve the receiving choice.

### MATH.9:End
