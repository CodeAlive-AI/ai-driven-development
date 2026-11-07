## MATH.8 - Generate a Solution Family by Symmetry

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.8:1 - Problem frame

Use this pattern when a mathematical solution is known and transformations that preserve its defining conditions can produce further useful solutions. You may need related roots of an equation, arrangements considered equivalent under rotation, or answers to problems whose data have been permuted.

Start with the known solution and one proposed transformation. Apply it and establish which problem the result solves. This can return another answer immediately, expose changed data, or identify a condition that the transformation fails to preserve.

A *symmetry* is an invertible transformation preserving the structure named by the problem. Its *orbit* at an object is the family of objects reached by the chosen group of transformations. The construction below obtains that family, distinguishes repeated objects, and explains what is still missing from a claim to have found all solutions.

The reader needs sets, functions, elementary equations and composition. The required group-action rules are stated below. The polynomial example uses factorization; the finite-arrangement example needs only binary strings and rotation. Use a direct calculation when it already supplies the needed answer. A transformation that changes the problem can still transfer a solution to the changed problem when that is useful.

### MATH.8:2 - Problem

Several transformed answers can be repetitions of one object. An orbit can also omit whole families of solutions. Conversely, a supposed symmetry can change a coefficient or boundary datum that the original problem holds fixed.

The mathematical task is to obtain solutions with a stated reach. This requires the transformation's action on both data and candidate answers, an argument that it preserves the solution condition, and a way to identify the objects its repeated use actually reaches.

### MATH.8:3 - Forces

| Force | Tension |
| --- | --- |
| Reusing one solution and finding all solutions | Transformations reuse a known answer, but another answer may lie in a different orbit. |
| A law and a fixed problem | Transforming the data can preserve the form of a law while changing the problem being solved. |
| Many transformations and distinct objects | Different transformations can return the same object. |
| Reduced calculation and returned information | Treating an orbit as one case can simplify an invariant question while losing an orientation or label needed by another result. |

### MATH.8:4 - Solution

**Specify the actions → preserve the solution relation → transform a known solution → construct its orbit → establish the family's reach → return the needed answer.**

#### MATH.8:4.1 - Specify the problem and the transformations

Write the solution condition as `S(d,x)`: candidate x solves the problem with data d. State the data that are held fixed, the domain of candidates and the equality used to distinguish answers. An equation, a feasibility condition or a minimum under a stated criterion can provide S.

Give the transformations and their actions on d and x. For a group G, the action satisfies `e*x=x` and `(g*h)*x=g*(h*x)`; the same rules apply to the data action. Here e is the identity transformation, and multiplication in G means composition, with h applied first. Every g has an inverse. A supplied family of permutations can make these rules immediate.

If the group is given by generating transformations, include their inverses and retain the relations they must satisfy. MATH.5 can construct an action from generator images that respect those relations. Listing generators without their action leaves the proposed symmetry undecided.

For a fixed datum d, retain only transformations with `g*d=d`. These form its stabilizer: the subgroup of transformations that leave that datum unchanged. Include compositions when finding this subgroup: the two-mark case in :5.2 is fixed by a half-turn although a single turn changes the marks. A larger group can relate different data instances, which is a different useful calculation.

#### MATH.8:4.2 - Establish the solution-preserving relation

Show that `S(d,x)` implies `S(g*d,g*x)` for every transformation and candidate in the claimed range. Applying the same implication to the inverse gives the converse. The transformation therefore pairs the two solution sets.

For an equation, substitute the transformed variables and data. For several constraints, preserve each one used by the solution. An optimization result needs both transformed feasibility and the corresponding criterion: if feasible candidates are paired bijectively and `J_(g*d)(g*x)=J_d(x)`, a better transformed candidate would return a better original candidate. Thus a minimizer transfers.

Preservation for generating transformations and their inverses extends to every finite composition by applying the implications successively. Use MATH.4's finite-construction argument when that extension needs explanation. A check on a few candidate values establishes only those cases unless a general argument is also available.

If a transformation fails, retain the first changed condition and decide whether the changed problem is useful. MATH.6 can exhibit the failure; FPF C.29 relates the mathematical correspondence to another subject when one is involved.

#### MATH.8:4.3 - Generate related solutions and remove repetitions

From a known solution x, calculate `g*x` and return it with the data `g*d`. To obtain solutions of the original fixed problem, use its data stabilizer from :4.1.

For a chosen group H acting on the same fixed problem, define the orbit:

`H*x={h*x | h in H}`.

All its members solve that problem by :4.2. Compare the resulting objects using the problem's equality; distinct transformation expressions can give equal answers.

With a finite list of generating transformations, a finite orbit and decidable equality, generate the orbit by closure. Start with x. Apply each generating transformation and its inverse to every newly found member, adding only previously absent results. Once every stored member has been processed and no new one appears, the set is closed under the generators and inverses. Every finite word in them stays in that set, so it is the whole generated orbit.

This procedure terminates when the reached orbit is finite and the stated operations return. For an infinite orbit, a formula such as `{h*x | h in H}` with a usable parameterization can be the result. A stopped enumeration without closure supplies only the reached subset.

#### MATH.8:4.4 - Explain duplicates and the limit of one orbit

The transformations fixing x form its stabilizer `H_x={h in H | h*x=x}`. Two transformations give the same answer precisely when the composition of one with the other's inverse fixes x:

`h1*x=h2*x` exactly when `(h2^-1*h1)*x=x`.

Choose one transformation h0 in H. All transformations returning the answer `h0*x` have the form `h0*k` with k in H_x: composing with k leaves x unchanged, and any h giving that answer satisfies `h0^-1*h` in H_x. These sets of transformations are called the left cosets of the stabilizer. They partition H, and each contains as many transformations as H_x, since multiplication by h0 is reversible. Therefore, for finite H, the number of distinct answers is `|H|/|H_x|`. Use this count when it helps construct or check the requested family; explicit comparison can be simpler for a small example.

One orbit contains exactly the answers reachable from its starting member under H. To claim all solutions, establish that every solution belongs to a represented orbit. This can use a complete finite classification, a mathematical reduction, or an argument that H acts transitively on the solution set, meaning that every solution is reachable from the starting solution. Finding no new member in the current orbit proves its closure, not that another orbit is absent.

When another solution lies outside the family, use it as the starting member of another orbit. A property unchanged by every transformation can show that two candidates cannot belong to the same orbit. Such a property can also suggest what a wider transformation group would need to change.

#### MATH.8:4.5 - Use an orbit representative without losing the requested result

A quantity constant on each orbit can be calculated from any representative. To define additional operations on orbit classes, use MATH.2's representative-independence condition; an orbit partition by itself only supplies classes.

When a problem is solved using representative data d0 and solution x0, retain a transformation g with `g*d0=d` for the requested data d. Return `g*x0`. If two transformations satisfy `g1*d0=g2*d0=d`, an answer independent of that choice requires `g1*x0=g2*x0`. A disagreement identifies information that the representative alone does not supply.

MATH.13 supplies the fixed-point restriction on a unique solution and the test for an impossible equivariant choice. Those questions require the output action and, for the unique-solution deduction, a justified uniqueness premise. Generating a solution set here does not select one member from it.

Stop with the requested related solution, complete orbit, orbit classification or identified failure of preservation. When data, constraints or the output change, reopen the affected action and preservation argument before reusing the family. A more costly enumeration or symmetry computation is useful only if it can improve the receiving result.

### MATH.8:5 - Archetypal Grounding

#### MATH.8:5.1 - An even polynomial has more than one solution orbit

For real x, solve `P(x)=x^4-5*x^2+4=0`. The two transformations are identity and sign reversal `r(x)=-x`. Since `P(-x)=P(x)`, they preserve the equation.

The known solution 1 gives the orbit `{1,-1}`. Applying sign reversal again returns to 1, so this orbit is complete. It is not the complete root set: 2 also solves the equation and belongs to the different orbit `{2,-2}`.

Factorization `P(x)=(x^2-1)*(x^2-4)` establishes that these two orbits cover all real roots. Symmetry generated each pair; factorization supplied the missing completeness argument.

Now change the equation to `Q(x)=x^2+x-2=0`. The value 1 remains a root, but `Q(-1)=-2`. The linear term breaks the sign symmetry. Reusing the old transformation would give a false answer to the changed problem.

#### MATH.8:5.2 - Binary arrangements on a cycle

Consider binary strings of length four with exactly two entries equal to 1. Positions are numbered 0 through 3 around a cycle. Let r move each entry to the next position, wrapping the last to the first. Four rotations return the original string, and rotation preserves the number of ones.

Starting with `1100`, repeated rotation gives:

`1100 -> 0110 -> 0011 -> 1001 -> 1100`.

There are four distinct members. Only the identity rotation fixes `1100`, agreeing with the count `4/1=4`.

Starting instead with `1010` gives:

`1010 -> 0101 -> 1010`.

A rotation by two positions fixes either alternating string. Its stabilizer has two members, so the orbit count is `4/2=2`.

Every two-one string either has adjacent ones around the cycle or has opposite ones. This covers the six possible strings and separates the two orbits. If the question asks for arrangements up to rotation, two representatives suffice. If it asks for every labeled string, return all six.

If position 0 receives a distinguished mark that must remain fixed, only the identity rotation preserves that data. The old orbit classification then forgets a distinction required by the new problem. The strings remain available; their identification must change.

Instead put identical marks at positions 0 and 2, with neither mark distinguished from the other. A single rotation and its inverse move the marked set to {1,3}; a half-turn returns it to {0,2}. The data stabilizer is therefore {e,r²}. To find this subgroup, examine compositions such as r² as well as the supplied generators.

#### MATH.8:5.3 - Permuting coefficients changes which equation was solved

Let the data be coefficients `a=(2,1)` and right-hand side 5. The equation is `2*x1+x2=5`, with known solution `x=(1,3)`.

The swap sends `a` to `(1,2)` and x to `(3,1)`. Their scalar product remains 5 because both positions are exchanged. Thus the transformed solution satisfies `x1+2*x2=5`.

Keeping the original coefficients instead gives `2*3+1=7`. The swap preserves the relation between transformed data and transformed solutions; it does not preserve this fixed original equation.

For comparison, `x1+x2=5` has equal coefficients. Its data are fixed by the swap, so a solution `(1,4)` gives another solution `(4,1)` of the same equation. Neither the swap nor the equation singles out one of them. A requirement for one distinguished answer needs an additional criterion or a compatible choice method.

For a representative-data calculation, take coefficients (1,2) and its solution (3,1). The swap maps those data back to (2,1) and the solution back to (1,3), recovering the original answer. With the equal coefficients (1,1), both identity and swap return the same data, while the chosen solution (1,4) returns as either (1,4) or (4,1). Each is a valid solution, but this choice does not define a transformation-independent rule. This ambiguity concerns the chosen pair; a request for a swap-fixed solution can instead use (5/2,5/2).

### MATH.8:6 - Bias-Annotation

Finite permutations make complete orbits cheap to display. Infinite and continuous actions can instead require symbolic parameterizations, different equality procedures or further mathematical methods. The complete finite examples therefore establish their own construction, while the general group argument states what can be reused.

Familiar visual symmetry can also hide supplied labels or coefficients. The equation and marked-cycle cases keep those data in the comparison.

### MATH.8:7 - Conformance Checklist

- The actions on the data and candidates satisfy the claimed composition and inverse rules.
- The preservation argument uses every condition required by the solution.
- Each returned solution is attached to its unchanged or transformed data.
- Distinct orbit members are distinguished by the problem's equality.
- A complete-orbit claim has closure or a corresponding argument; an all-solutions claim covers the other possible orbits too.
- A representative retains the information required to recover the requested answer.

### MATH.8:8 - Common Anti-Patterns and How to Avoid Them

**Close one orbit and declare the equation solved.** The polynomial has two complete sign orbits. Supply the additional classification or restrict the returned claim to the generated family.

**Count transformation expressions as different solutions.** The alternating string is fixed by a half-turn. Compare objects or use the stabilizer to account for repetition.

**Transform variables while silently retaining changed data.** Swapping variables and coefficients preserves the linear relation; swapping only the variables can fail it. Return the corresponding data with the solution.

**Use every old rotation after a mark is added.** The fixed mark changes the permitted subgroup. Recompute the identification from the new data.

**Return a normalized answer without its coordinate relation.** An invariant quantity and an equivariant answer need different return information. Retain the transformation or expose the remaining ambiguity.

### MATH.8:9 - Consequences

A known solution can supply a useful family without solving every transformed case independently. Orbit closure and stabilizers explain both the family and its repetitions. Separate orbits reveal a remaining construction problem rather than an apparent lack of progress in the same enumeration.

The gain depends on the cost of finding and applying the transformations. For a small isolated equation, direct calculation may finish sooner. For repeated or related questions, the shared preservation argument can save substantial work; the construction alone does not quantify that saving.

### MATH.8:10 - Architectural Rationale

The method builds a solution family from an action and a preservation relation. Keeping data inside that relation distinguishes transformations of one fixed problem from transformations between problems of the same form.

Generating the orbit and classifying all solutions answer different questions. The finite-closure argument explains when generation is complete; a stabilizer explains repeated results; another representative or reduction accounts for a missing orbit. These operations keep useful mathematical content beyond the instruction to notice a symmetry.

MATH.7 constructs operations through an arbitrary bijection. Here the transformations act on a specified problem and preserve its solution relation. MATH.5 can construct the action from assigned generators, while MATH.2 controls additional operations on identified results. The same orbit can support different receiving questions without giving its quotient every operation of the original set.

A direct solution, an existing orbit classification or a supplied parameterization is preferable when it already supplies the requested result. The group construction earns its cost when related answers, reduced cases or the reach of a family matter.

### MATH.8:11 - SoTA-Echoing

**Question:** how can transformations construct related mathematical solutions while retaining data, distinguishing repetitions and establishing the reach of the family?

Milne's [*Group Theory*, version 4.01, November 2025](https://www.jmilne.org/math/CourseNotes/GT.pdf), chapter 4, definition 4.1, the orbit discussion and proposition 4.7/corollary 4.8, supplies actions, orbit partition and the stabilizer description of an orbit. **Adopt** those mathematical relations. The procedure here makes finite generation, returned data and the separate all-solutions question explicit.

[Bronstein, Bruna, Cohen and Veličković, *Geometric Deep Learning*, chapter 3, §3.1](https://geometricdeeplearning.com/book/algebraicpriors.html) distinguishes the structure preserved by an automorphism from a change to an isomorphic object. **Adapt** that distinction to a relation between problem data and solutions. A fixed mark or coefficient can change the available symmetries.

The selected construction competes with direct calculation or a ready classification. It is useful when one preservation argument replaces repeated solution work or exposes omitted families. Direct calculation remains sufficient for a single easy result. The finite examples demonstrate closure and incomplete coverage.

Reopen when the action, data, solution relation, equality procedure or requested return changes. A more effective orbit-generation or canonicalization method can replace the finite implementation while retaining its required mathematical result.

### MATH.8:12 - Relations

- **Uses MATH.1 and MATH.5:** compose generating transformations and construct an action that respects their relations.
- **Uses MATH.4:** extend preservation through finite compositions and justify the finite-closure result.
- **Uses MATH.2:** decide which further operations remain defined on orbit classes.
- **Connects with MATH.6:** exhibit a changed condition or a counterexample to a completeness claim.
- **Connects with MATH.7:** compare an arbitrary representation change with an action preserving a given structure.
- **Uses C.29 for another subject:** recover what the mathematical transformation and returned solution mean there.
- **Uses MATH.13 when the requested answer is unique or must be chosen equivariantly:** obtain its fixed-point restriction or an obstruction under the stated premises.
- **Uses B.5.QD and C.11.DUA when continuation matters:** choose a useful missing family, new transformation or further calculation.

### MATH.8:End
