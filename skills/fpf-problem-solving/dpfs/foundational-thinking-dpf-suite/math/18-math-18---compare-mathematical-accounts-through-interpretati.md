## MATH.18 - Compare Mathematical Accounts through Interpretations

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.18:1 - Problem frame

Use this pattern when two mathematical descriptions appear to address the same construction or question but use different objects, primitive operations, relations or notions of equality. You need to know which calculations, arguments or changes can be carried from one description to the other.

Begin with one consequence you want to transfer. It may be a constructed object, an equation, a solution, or a way of composing operations. An interpretation of that consequence, with its supporting construction or a reason it fails, is the first useful result. A broader equivalence claim requires correspondingly broader comparison.

A **mathematical account** here consists of the objects, operations, relations and assumptions used to describe the question. An **interpretation** specifies how to read those ingredients through another account and establishes the consequences needed for the proposed use. The main route requires functions, elementary algebra and reasoning with “for every” and “there exists”. It explains the order and algebra used in the first worked case. The vector-and-matrix case is an optional branch requiring elementary linear algebra.

If a supplied bijection and its transported operations already settle the change of representation, use MATH.7. Use the present method when primitives must be reconstructed, only part of an account transfers, or the round trip needs a structural comparison rather than literal equality.

### MATH.18:2 - Problem

Matching names or formulas can conceal different allowed objects, operations or solutions. Two descriptions may recover the same objects while allowing different transformations between them. A translation may preserve calculations for the translated inputs while a target quantifier ranges over additional objects and changes the answer.

The task is to construct the interpretation, determine the scope of the resulting agreement, and use it to transfer a consequence or locate the distinction that prevents transfer.

### MATH.18:3 - Forces

| Force | Tension |
| --- | --- |
| Different primitives and recoverable structure | An operation in one account may be definable through a relation in another, but its existence and uniqueness need an argument. |
| Object correspondence and allowed maps | Matching objects leaves open whether the accounts permit the same transformations of them. |
| Useful one-way translation and equivalence | An interpretation may carry the needed result without supporting a reverse interpretation or a broader equivalence. |
| Comparison scope and effort | A local consequence may need only a short argument; comparing entire theories requires their logical and structural conditions. |

### MATH.18:4 - Solution

**Local mantra:** choose the consequence; interpret the ingredients; derive what transfers; compare the round trips; use the agreement or its failure.

#### MATH.18:4.1 - Set the scope of the comparison

Name the source account, target account and intended use. Identify the objects involved, their operations and relations, and what counts as an answer. If transformations between objects matter, include those transformations in the comparison.

For each ingredient that the intended consequence uses, ask how the target will express it. Keep optional additional structure separate. For example, an additive operation, an order and a distance support different questions even when carried by the same underlying set.

Decide the strength of the needed conclusion. Transferring one equation, constructing a solution, comparing all compositions in a selected family, and establishing equivalence of two presentations are different claims. Inspect the ingredients and reasoning needed for that claim. Expand the comparison when the next use expands it.

#### MATH.18:4.2 - Construct the interpretation

Specify the source objects' target counterparts and the operations or relations that interpret each required primitive. Give a construction rather than a matching name. If an operation is to be recovered through a defining condition, establish that a result exists and is determined to the degree required by the source.

Respect the domains and arities. A binary operation needs two admitted inputs; a relation needs the participants on which it is asserted. When the source uses equivalence classes, establish that different representatives give equivalent interpreted results. MATH.2 supplies the detailed quotient test.

Extend the interpretation through constructed expressions. Interpret each input, then interpret the operation applied to those inputs. A composite expression is handled by repeating this rule through its construction. MATH.5 develops the extension from generators when the source is presented that way.

An assertion also has a construction. Translate equality, conditions and quantifier ranges. For `there exists x in A with P(x)`, the target must express both the interpreted domain A and the interpreted condition P. Enlarging that range can admit a solution that the original problem excludes; :5.2 works this failure.

When an interpretation uses a basis, representative or another choice, supply it or a means of obtaining it. Determine whether changing the choice changes the result, or only changes a representation with a known comparison.

#### MATH.18:4.3 - Establish what the interpretation preserves and reflects

For the consequence being transferred, follow its construction or argument through the interpretation. Establish that the required operations remain applicable and that each used equality or relation remains valid.

Distinguish the two directions. Preservation takes a source consequence to a target consequence. Reflection takes an interpreted target consequence back to the source. To use a target calculation as the source answer, obtain the required recovery and reflection argument.

For operations composed as maps, an object assignment F also assigns `F(f):F(A) -> F(B)` to each source map `f:A -> B`. To translate a sequence stage by stage, establish:

`F(g∘f)=F(g)∘F(f)` and `F(id_A)=id_F(A)`.

Such an assignment is a functor. Fix source objects A and B. To recover maps, determine which target maps `F(A) -> F(B)` have counterparts `A -> B`. To recover an equality, take two source maps `f,g:A -> B` and determine whether `F(f)=F(g)` implies `f=g`. The equality test concerns maps with these same endpoints. Recovery of the objects themselves is a further question, handled in :4.4.

**Formal-theory branch.** When the intended result is transport of theorems, give the translation of the relevant syntax and logic. Establish the interpreted axioms and justify the inference rules used by the theorem. Comparing collections of models through maps supplies a different mathematical result until its connection to this theorem-translation claim is established.

A failed preservation or reflection equation is useful. Work its inputs far enough to show what answer or construction changes. Then restrict the claim, enrich the interpretation or keep the accounts distinct for that purpose.

#### MATH.18:4.4 - Construct the return and examine the composites

When two-way use is needed, construct a return interpretation G. Apply `G∘F` to source ingredients and `F∘G` to target ingredients. Inspect what each round trip returns.

Sometimes the ingredients are recovered literally, as in the order-and-operation case below. Sometimes a specified isomorphism supplies recovery: an invertible map preserving the structure used by the comparison.

When whole systems of objects and maps are compared, pointwise isomorphisms need compatibility with the maps. If `eta_A:A -> G(F(A))` provides source recovery, require for every source map `f:A -> B`:

`G(F(f))∘eta_A = eta_B∘f`.

Both routes start in A and finish in `G(F(B))`. This equation means that translating and then applying the map agrees with applying the map and then translating. Require the corresponding compatibility on the target side as well. In categorical language, functors with these natural isomorphisms give an equivalence of categories.

Use that equivalence for properties supported by the chosen structure and invariant under its isomorphisms. If a later question uses additional structure, include it in the comparison. The length question in :5.3 shows why this return matters.

If only one direction is constructed or needed, retain that useful interpretation at its established scope. If two-way recovery fails, name the unrecovered operation, assertion or distinction that matters to the work.

#### MATH.18:4.5 - Transfer the result and reopen only the changed demand

Carry the intended calculation, construction or argument into the receiving account and recover its answer where required. State the conditions that make the transfer usable. A receiver needs the interpretation and relevant consequence; an equivalence label alone leaves the work to be reconstructed.

A changed primitive, quantifier range or allowed-map class can change the comparison. Revisit the affected construction and its argument. Keep conclusions whose ingredients and conditions are unchanged.

For mathematical work, the result may be an equivalence at the selected scope, a useful one-way interpretation or a separating consequence. For a computational or working-method application, C.29 and C.29.2 supply the further correspondence and execution questions. Mathematical agreement can then inform the application through those explicit connections.

### MATH.18:5 - Archetypal Grounding

#### MATH.18:5.1 - Recover an order from an operation, then compare allowed maps

One account starts with a set S and a binary operation `a∨b` satisfying associativity, commutativity and idempotence:

`(a∨b)∨c=a∨(b∨c)`; `a∨b=b∨a`; `a∨a=a`.

Another starts with a partial order in which every pair has a least upper bound. An upper bound of a and b is an element z with `a<=z` and `b<=z`. The least upper bound lies below every such z. Antisymmetry makes it unique. We want to move constructions between these descriptions.

From the operation, define `a<=b` to mean `a∨b=b`. Idempotence gives reflexivity. If `a∨b=b` and `b∨a=a`, commutativity gives a=b, establishing antisymmetry. If `a∨b=b` and `b∨c=c`, associativity gives:

`a∨c=a∨(b∨c)=(a∨b)∨c=b∨c=c`.

Thus the relation is transitive. Also `a∨b` is an upper bound of a and b. If z is any upper bound, then `(a∨b)∨z=a∨(b∨z)=a∨z=z`. So `a∨b<=z` and the original operation supplies the least upper bound.

Conversely, define `a∨b` to be the least upper bound in the ordered account. Uniqueness makes the operation commutative and idempotent. Both `(a∨b)∨c` and `a∨(b∨c)` are the least upper bound of the same three elements, giving associativity.

The round trips recover both primitives. Starting from the operation returns it as the least upper bound just proved. Starting from the order returns it because `a<=b` holds exactly when b is the least upper bound of a and b.

Now the intended use expands: can every order-preserving map be used as a map preserving the binary operation? A join-preserving map is monotone: apply it to `a∨b=b`. The converse fails. Take subsets of `{u,v}` ordered by inclusion, with union as join, and target `{0,1}` with its usual order. Define h to return 1 only on the full set and 0 on all other subsets. It is monotone, yet:

`h({u} union {v})=1`, while `max(h({u}),h({v}))=0`.

For constructions that combine joins, select join-preserving maps in both accounts. If all monotone maps are needed, retain that broader ordered account and its different transformation class. The objects matched; the expanded map claim required and received its own answer.

#### MATH.18:5.2 - An enlarged domain changes the available solution

The natural numbers `N={0,1,2,...}` embed in the integers Z. Inclusion preserves 0, addition and equality of expressions evaluated on natural-number inputs. It also reflects those equalities: two included natural numbers are equal in Z precisely when they were equal in N.

Suppose the next task is to solve `x+1=0`. The integer solution x=-1 is outside N. The interpretation useful for additive calculations therefore has not supplied a natural-number solution.

To express the original existential question in Z, retain its range: “there exists an integer x with `x>=0` and `x+1=0`.” That statement remains false. To use Z as a calculation space for another natural-number equation, compute there and test the recovered candidates against the source domain.

The revised use keeps the beneficial integer calculations and makes their return condition explicit. A demand to identify all natural-number and integer solution questions would instead fail this comparison.

#### MATH.18:5.3 - Compare linear maps with matrices, then add a length question

**Additional structure -- finite-dimensional real vector spaces.** In one account, each space comes with a specified ordered basis, and maps between spaces are all linear maps. In the other, an object is a nonnegative integer n and a map n to m is an `m-by-n` real matrix. Maps compose by matrix multiplication.

For a space V with basis `(b1,...,bn)`, let `c_V:V -> R^n` send a vector to its coefficients in that basis. Interpret `f:V -> W` by the matrix of `c_W∘f∘c_V^(-1)`. Composition agrees because the adjacent coordinate conversion and its inverse cancel. Identity maps become identity matrices.

The return takes n to `R^n` with its standard basis and a matrix to its linear map. The round trip on matrices is literal. The round trip on V returns its coordinate space, with recovery supplied by `c_V`. For each f, the equation `matrix(f)∘c_V=c_W∘f` establishes the required compatibility. This compares the entire selected system of linear maps, including their compositions, rather than only matching vector values.

Now ask for lengths in Euclidean space. With basis `b1=(1,0)`, `b2=(0,2)`, coordinates `(0,1)` represent a vector of length 2; their ordinary coordinate length is 1. The linear comparison did not include the inner product. Carry it as a Gram matrix: here `G=diag(1,4)` and squared length is `c^T*G*c`. Retaining G lets us calculate the same vector's length after changing coordinates.

A different question asks which linear maps preserve lengths. For a map from V to W represented by matrix M, with Gram matrices `G_V` and `G_W`, require `M^T*G_W*M=G_V`. This follows by comparing the squared length `c^T*G_V*c` of every input with `(M*c)^T*G_W*(M*c)` of its output. Use that condition to select the length-preserving maps. The earlier interpretation of arbitrary linear maps remains available when length preservation is not required.

#### MATH.18:5.4 - Recover an operation using a chosen origin

On the integers, one account supplies the ternary operation t(x,y,z)=x-y+z and a marked origin 0. It recovers addition as t(x,0,y) and negation as t(0,x,0). Conversely, addition and negation recover t. Substitution verifies both returns for every integer input.

Now remove the marked origin. Choosing any integer c gives an addition x+_c y=t(x,c,y)=x-c+y, identity c and inverse 2c-x. Combining these operations again gives the same t(x,y,z). The ternary operation alone therefore permits several choices of origin and corresponding binary operations.

For example, c=0 makes the sum of 2 and 3 equal 5; c=1 makes it equal 4 under +_1. Both choices recover the original ternary operation. A question using only t can continue without selecting an origin; recovering the former addition needs its marked origin again. This distinguishes a usable one-way interpretation from a return that silently supplies extra structure.

### MATH.18:6 - Bias-Annotation

Familiar terminology can encourage an equivalence claim before the allowed operations and quantifiers have been compared. Follow one consequential construction through both accounts, then enlarge the claim only as far as its arguments support.

The categorical branch is useful when objects and maps are already the subject of comparison. Algebraic definitions, order relations and explicit logical translations can provide more direct constructions for other questions. Select the form that makes the required transfer inspectable.

### MATH.18:7 - Conformance Checklist

For the comparison being used:

- The source, target, intended consequence and claimed scope are recoverable.
- Each required primitive has a constructed interpretation with its domain and assumptions.
- Needed preservation, reflection and recovery claims have arguments at that scope.
- Two-way claims inspect both composites and the compatibility required by the allowed operations.
- A failed claim identifies a changed answer or unavailable construction and determines the retained use or repair.
- The receiver can perform the intended transfer with the supplied result and conditions.

### MATH.18:8 - Common Anti-Patterns and How to Avoid Them

**Matching objects while silently widening maps.** The order-and-join comparison recovers the objects, but its operation-preserving maps form a narrower class than all monotone maps. Select the class required by the next construction.

**Solving the translated equation in an enlarged domain.** The integer solution in :5.2 fails the original domain condition. Translate the quantifier range and check the return of any computed candidate.

**Using an equivalence for added structure.** The linear comparison in :5.3 supports linear operations. A length question adds an inner product and the obligation to carry it through the coordinate change.

### MATH.18:9 - Consequences

Different mathematical descriptions can become usable alternatives with known transfers and returns. The comparison can also expose a useful one-way interpretation or a distinction that a proposed equivalence would erase.

The cost follows the scope. Recovering one primitive may settle a local use; comparing whole families of constructions requires their maps and compatibility laws. A changed task can reuse earlier results while reopening the additional structure it now needs.

### MATH.18:10 - Architectural Rationale

Organizing the method around a consequence keeps interpretation connected to mathematical work. Comparing objects, assertions and transformations prevents an object-level match from silently becoming a claim about every use.

The operation-and-order case reconstructs different primitives on the same carrier. The natural-number case exposes domain-sensitive assertion transport. The matrix case compares families of objects through compatible isomorphisms. Together they show different uses of one method without making any one mathematical branch its scope.

MATH.5 and MATH.7 remain direct construction methods for generator extension and bijective transport. This pattern supplies the wider comparison in which those methods may solve one part. MATH.17 supplies operations on operations when the interpretation itself must be constructed or transformed that way.

### MATH.18:11 - SoTA-Echoing

Fong and Spivak's [Seven Sketches in Compositionality](https://arxiv.org/abs/1803.05316), §§1.2-1.3, develops order, joins and what their maps preserve. The adopted contribution is to compare an observation or transformation by the operations it carries, including the ones it loses. The order-and-operation construction here makes that question usable when the accounts start from different primitives.

Riehl's [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf), §1.5, supplies equivalence through functors and compatible isomorphisms. It supports the family-level comparison. A claim about translated theorems additionally depends on the chosen logic and interpretation.

For a prepared change of coordinates, explicit inverse maps can be enough. A broader account comparison becomes useful when available operations, assumptions or quantifiers differ. The present method combines these alternatives according to the consequence to be transferred.

### MATH.18:12 - Relations

- **MATH.5** constructs the interpretation of generated objects from its values on generators.
- **MATH.7** transports mathematical structure through a supplied bijection.
- **MATH.2** establishes when an interpretation and its operations descend through identification.
- **MATH.16** constructs objects and comparison maps from required uses.
- **MATH.17** constructs operation collections and higher-order transformations, including composition-preserving assignments.
- **MATH.6** constructs a countermodel when an asserted transfer or equivalence fails.
- **B.5.RA and B.5.TU** recover an unfamiliar argument and carry a theoretical consequence into its intended case.
- **C.29 and C.29.2** supply subject correspondence and computational formulation for applications of the mathematical comparison.

### MATH.18:End
