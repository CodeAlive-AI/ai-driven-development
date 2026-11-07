## MATH.7 - Transport a Mathematical Structure Through a Bijection

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.7:1 - Problem frame

Use this pattern when another representation makes a mathematical construction easier to work with and you need to carry its operations and results across a reversible map. You may want to calculate with coordinates, encode sets by bit vectors, or give a familiar carrier a different algebraic structure.

A *bijection* pairs every element of one set with one element of another and has an inverse in both directions. It can be used to define operations and relations on the receiving set. With those definitions, the map becomes an *isomorphism* of the chosen structures: it preserves their operations and reflects their relations.

Start with one needed operation and one input. Recover the input in the source, perform the source operation, and map its result back. Return the resulting operation and its domain, or the part of the proposed correspondence that cannot be reversed.

The reader needs functions, composition, inverse functions and elementary algebra. The main construction covers operations with finitely many inputs, constants and relations on sets. The worked coordinate example also uses squared Euclidean length. If the map and the needed preservation result are already available, use them. A one-way representation or a summary that deliberately forgets distinctions can instead use MATH.2, MATH.5 and FPF C.29.1 for the result it preserves.

### MATH.7:2 - Problem

Changing the names or coordinates of elements leaves the receiving operations undecided. Reusing the familiar operation on the new labels can produce a different result. Even when one operation survives unchanged, another quantity or relation may require a different formula.

The task is to construct the receiving structure, establish what it preserves, and use that preservation to calculate or solve a problem. If the receiver already requires particular operations, the transported construction must be compared with them.

### MATH.7:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar carrier and chosen structure | The same set can carry several operations with different identities and laws. |
| Reversible elements and preserved work | Recovering elements supplies the means to transport operations; it does not choose which operations matter. |
| One convenient representation and several quantities | A change can simplify one calculation while complicating another. |
| Reusable proof and computing cost | Transport can reuse an algebraic argument, while repeated encoding and decoding can make a calculation expensive. |

### MATH.7:4 - Solution

**Choose the structure to carry → establish both inverse equations → transport operations and relations → derive the retained laws → calculate and return the result.**

#### MATH.7:4.1 - Choose the source structure and the receiving use

Name the source set X and the operations, constants or relations needed by the question. For an additive structure these might be addition, zero and negation. For an ordered structure the comparison relation matters too. Include a quantity such as length when the requested conclusion depends on it.

Name the receiving set Y and distinguish two tasks: constructing its operations, or showing that operations already required there correspond to the source. In the second task, retain those required operations for the comparison. Replacing them with different transported operations changes the proposed mathematical structure.

For a single update, C.29.1's correspondence comparison can be sufficient. Use the construction below when you need the related operations, their laws, a reusable representation or a way to move solutions between the two structures.

#### MATH.7:4.2 - Establish the reversible map on its declared sets

Give `h:X→Y` and `r:Y→X` and establish both equations:

`r(h(x))=x` for every `x` in X;

`h(r(y))=y` for every `y` in Y.

They establish that r is the inverse of h. A formula, a complete finite table or an existing applicable result can supply the maps and these equations.

If h only covers part of the proposed Y, you can take its image `h(X)` as the receiving set when that answers the question. If h combines distinct source elements, returning the whole original element requires more information or a different map. A quotient may still retain the requested operation under MATH.2. MATH.6's left-inverse examples show why recovery in one direction alone leaves the other direction open.

Keep restrictions in the sets. For example, squaring is reversible from nonnegative real numbers to nonnegative real numbers, with the nonnegative square root as inverse. Squaring on all real numbers combines opposite inputs and cannot support that inverse construction for the whole source.

#### MATH.7:4.3 - Define the receiving operations and relations

For a source operation `op_X:X^n→X`, define:

`op_Y(y1,...,yn)=h(op_X(r(y1),...,r(yn)))`.

In words: decode each input, perform the source operation, then encode the output. Constants have no inputs, so a source constant c becomes `h(c)`. A source relation R becomes:

`R_Y(y1,...,yn)` holds exactly when `R_X(r(y1),...,r(yn))` holds.

The construction can have different input and output sets. For `op:X1×...×Xn→Z`, use a bijection `h_i:Xi→Yi` for each input and `k:Z→W` for the output. Then:

`op_target(y1,...,yn)=k(op(h_1^-1(y1),...,h_n^-1(yn)))`.

An unchanged scalar result uses the identity map on that scalar set. Thus transporting a length calculation changes its input coordinates while retaining the numerical length.

For a partial source operation, transport its domain too. The receiving tuple is allowed precisely when its decoded tuple is in the source domain; define its output there by the same formula. A larger independently supplied receiving domain needs its own comparison before its extra inputs are used.

Calculate one small case in both descriptions. Use it to check the direction of the maps, the constants and the operation being performed. The general preservation result comes from the defining formula and inverse equations.

#### MATH.7:4.4 - Derive the laws that the chosen structure retains

For each operation, substituting `h(x_i)` into its definition and cancelling `r(h(x_i))` gives:

`op_Y(h(x1),...,h(xn))=h(op_X(x1,...,xn))`.

Any other receiving operation with this equality must coincide with the constructed one: every receiving input has the form `h(x_i)`. Thus the source operation and h determine the transported operation uniquely on Y.

To carry an equation built from these operations, follow its expressions from the variables and constants through each operation. Variables are mapped by h, constants by their specified images, and the displayed equality carries each composite expression. This is an induction on the expression's construction; MATH.4 supplies that form of argument.

For expressions s and t in one carrier, it yields:

`s_Y(h(x1),...)=h(s_X(x1,...))` and `t_Y(h(x1),...)=h(t_X(x1,...))`.

An equality of the source expressions therefore gives equality of the receiving expressions. Conversely, h is injective, so equality of those receiving values gives equality of the source values. Surjectivity covers all assignments in Y. The same reasoning with the map for each sort treats operations with different input and output sets.

This transfers equational laws such as associativity, an identity law or distributivity for the operations actually carried. A further order, distance or other relation must use its own transported definition or an established compatibility result. For partial operations, compare the definedness of the compound expressions as well as their values.

#### MATH.7:4.5 - Calculate in the useful representation and recover the answer

Translate the inputs, constants and requested relation. Calculate or solve the corresponding problem using the receiving operations. Map the result back with the inverse appropriate to its kind.

For example, a source equation `t_X(x)=b` becomes `t_Y(y)=h(b)`, where `y=h(x)` and all other parameters in t are translated too. A receiving solution y returns `x=r(y)`. The correspondence gives both directions, so it also carries absence or uniqueness of a solution when the equations range over the declared sets.

Use a simpler formula for a transported operation after establishing equality with its defining formula. This can avoid repeated encoding and decoding. Compare the resulting calculation effort with direct source calculation when the representation is being chosen for efficiency. Preservation alone establishes no speed advantage.

If Y already had a required operation, compare it with the constructed one before transferring its laws or solutions. A disagreement can lead to a changed map, a different receiving structure, or continued use of the original description.

#### MATH.7:4.6 - Revisit only what the changed question uses

When h changes, derive the affected receiving operations and constants again. When the question adds a quantity or relation, construct its receiving form even if the earlier operations are unchanged. When a domain restriction changes, revisit both inverse equations and the allowed operation inputs.

Return a failed equation or two source cases that the map cannot distinguish through MATH.6 or MATH.2 as appropriate. Use C.29 when the mathematical representation is being related to another subject. Stop with the needed calculation, reusable transported structure, or identified obstruction.

### MATH.7:5 - Archetypal Grounding

#### MATH.7:5.1 - Shifted numbers with a shifted addition law

Start with real numbers under addition. Let `h(x)=x+1` and `r(y)=y-1`. Both inverse equations hold on all real numbers. The transported addition is:

`u ⊕ v=h(r(u)+r(v))=u+v-1`.

The source zero becomes `h(0)=1`, and source negation becomes `neg_Y(u)=h(-r(u))=2-u`. Thus `u⊕1=u` and `u⊕(2-u)=1`. Associativity follows directly because both groupings of three inputs give `u+v+w-2`; it also follows from the general transport argument.

To solve `x+3=7`, translate it as `y⊕4=8`. The receiving equation gives `y=5`, and decoding gives `x=4`. Using ordinary addition on the new labels would instead solve `y+4=8` and return `x=3`, which fails the original equation.

The transported operation is useful as a representation of the source addition. If ordinary addition on Y is part of the receiving requirement, this h does not preserve that requirement; the construction has exposed a different operation.

The same map can transport real division, defined when the source denominator is nonzero. Its receiving formula is `u⊘v=(u-1)/(v-1)+1`, with domain `v≠1`. The label 1 decodes to the forbidden denominator zero; the label 0 decodes to the allowed denominator −1. For example, `3⊘0=-1` decodes to −2, the result of the source calculation `2/(-1)`. Using the familiar restriction `v≠0` would exclude an allowed input and admit a forbidden one.

#### MATH.7:5.2 - Sets represented by bit vectors

Let X be the subsets of `{a,b,c}`. Map a subset to its membership vector in `{0,1}^3`; for example, `{a,c}` maps to `(1,0,1)`. Decode by selecting the positions marked 1. These maps are inverse on all eight subsets and all eight vectors.

Take symmetric difference as the source operation: an element belongs to `S△T` when it belongs to exactly one of S and T. Its transported operation is coordinatewise XOR, whose output bit is 1 exactly when the two input bits differ. The empty set becomes `(0,0,0)`.

For `S={a,c}` and `T={b,c}`, symmetric difference gives `{a,b}`. In coordinates:

`(1,0,1) XOR (0,1,1) = (1,1,0)`.

Decoding returns `{a,b}`. This gives a way to perform the set operation in a binary representation and recover its result. The inverse map and operation formula explain why the method works for every subset pair; the eight-by-eight table is a finite check if needed.

If the next question asks for union instead, derive its operation: coordinatewise OR. Reusing XOR would discard an element present in both inputs. The same bijection supports both operations once each is defined.

#### MATH.7:5.3 - Addition survives a coordinate change while length needs a new formula

In `X=R^2`, let `h(x,y)=(x+y,y)`. Its inverse is `r(u,v)=(u-v,v)`. Transported vector addition coincides with ordinary coordinatewise addition because h is linear.

Now ask for squared Euclidean length, `L_X(x,y)=x^2+y^2`. The result is a real number whose interpretation stays unchanged, so its output map is the identity. The transported quantity is:

`L_Y(u,v)=(u-v)^2+v^2`.

The source vector `(0,1)` has squared length 1 and maps to `(1,1)`. The transported formula still returns 1. The familiar formula `u^2+v^2` would return 2.

A length bound `L_X(x,y)≤1` consequently becomes `(u-v)^2+v^2≤1`. It does not become `u^2+v^2≤1` through this coordinate map. The example separates an unchanged operation from a quantity whose receiving formula must be constructed. A later physical interpretation of these coordinates uses C.29 for its subject correspondence.

### MATH.7:6 - Bias-Annotation

Bijections give a particularly strong form of transfer: full recovery on the declared sets. Many useful summaries and approximate models intentionally retain less information. They can still answer a specific question through a different correspondence method. The elementary examples also make the maps cheap to calculate; a complicated inverse may remove the computational benefit of a representation while leaving its mathematical validity intact.

### MATH.7:7 - Conformance Checklist

- The receiving question determines the operations, constants and relations to carry.
- Both inverse equations hold on the sets used by the result.
- Each receiving operation uses the appropriate input and output maps, including transported domains for partial operations.
- The claimed laws concern the transported structure or operations shown to coincide with it.
- The calculation translates its parameters and returns a result of the required kind.

### MATH.7:8 - Common Anti-Patterns and How to Avoid Them

**Change the labels and retain an incompatible operation.** In :5.1 ordinary addition on the new labels solves a different equation. Construct the receiving operation and compare any required incumbent.

**Recover source elements and assume every target element is covered.** Establish the second inverse equation or restrict the target to the image, as :4.2 requires.

**Transfer every property after checking one operation.** The coordinate example preserves addition while squared length needs another formula. Include the quantity or relation used by the requested result.

**Choose a familiar operation for a new question.** The bit-vector example needs OR for union and XOR for symmetric difference. Translate the operation the question actually asks for.

### MATH.7:9 - Consequences

A reversible correspondence becomes a constructive way to obtain operations, laws and solutions in another representation. The same carrier can support a newly useful structure, and the proof of preservation can be reused across many calculations.

The benefit can be a clearer expression, an easier proof or a cheaper computation. These benefits can differ. More than one representation may remain useful for different parts of the work.

### MATH.7:10 - Architectural Rationale

Encoding the result of a decoded operation determines the structure that the bijection preserves. Uniqueness prevents an independent choice of a familiar operation from being silently treated as the same construction. The expression-induction argument then explains why equations and their solutions travel.

C.29.1 already gives the common correspondence method and conjugation of a single update. This pattern develops the mathematical structure construction: constants, operations of several arities, relations, their laws and solution return. A single-update use can stay with C.29.1. MATH.5 starts instead with generator images and builds a homomorphism, which may forget information; here a supplied reversible map determines the receiving operations.

Transport is preferable when an available source structure and a useful bijection save construction or reasoning work. Direct definitions can be simpler or faster. A pre-existing isomorphism can supply the result without repeating the derivation. These alternatives retain the question that the representation is meant to answer.

### MATH.7:11 - SoTA-Echoing

**Question:** how can a reversible map supply a usable mathematical structure and carry its calculations?

Burris and Sankappanavar's [*A Course in Universal Algebra*, corrected 2012 edition](https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf), II §2, definition 2.1, states algebraic isomorphism through a bijection and operation preservation. **Adopt** that mathematical relation. The pattern makes the receiving operations constructive and gives an expression-based argument for the transferred equations.

The maintained [Mathlib algebraic-structure transfer definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/TransferInstance.html) implement transport of constants, operations and their laws through an equivalence. **Adapt** this as the general construction here. Its library note also identifies an implementation cost from repeated unfolding; mathematical equivalence does not choose the most efficient computational representation. The [module-transfer construction](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/TransferInstance.html) further illustrates retention of a fixed scalar domain while carrying vector structure.

A direct definition or an existing isomorphism can provide the same result with less work. Transport earns its cost when the correspondence and reusable law matter. Reopen when the inverse, the selected operations, or the required result domain changes.

### MATH.7:12 - Relations

- **Uses MATH.4:** extend preservation through finite expression construction.
- **Connects with MATH.5:** distinguish extending generator images from constructing structure through an already reversible map.
- **Returns to MATH.2 when the representation combines elements:** construct the quotient and determine the retained operation.
- **Uses MATH.6 for a failed preservation claim:** exhibit the incompatible input or missing inverse direction.
- **Specializes the mathematical construction used by C.29.1:** construct operations, relations and laws through a bijection. Use C.29 for their interpretation in another subject.
- **Connects with A.6.3.RT.OE:** use the available expression rules to make the transported calculation operable; invention of a notation language is a further notational method.

### MATH.7:End
