## MATH.16 - Choose a Mathematical Construction from Its Required Maps (Universal Property)

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.16:1 - Problem frame

Use this pattern when you need a mathematical object but have not decided how to construct it. You can describe what should be recoverable from it, what data should determine it, or which functions it must support. The difficulty is choosing among constructions that can all look plausible while supporting different uses.

For example, a result may need to carry two answers together, carry either kind of answer, or combine answers that agree about a shared quantity. These requests lead to different mathematical objects. Choosing a familiar representation first can hide the difference until a later operation fails.

Start by naming one operation the new object must support and the information that should determine its result. Draw the corresponding functions, including their directions. A useful first result is a requirement that distinguishes two candidate constructions. Continue to a construction and its use when the question needs them.

The method develops a **universal property**: a specification of an object through the maps it must admit and the equations those maps satisfy. The main route uses sets and all functions between them. The reader needs elementary sets, function composition and equality; the remainder example also explains the modular arithmetic it uses. Paragraphs marked **Additional structure** are optional and assume knowledge of the named mathematical theory.

If an available object and operation already answer the question, use them. A universal specification becomes useful when choosing, explaining, comparing or changing the construction is part of the work. Establishing the property for every allowed input needs an argument; working a few examples can expose a failure but cannot establish that general claim.

### MATH.16:2 - Problem

A familiar notation can suggest an object without explaining why it has the right structure. A pair of entries, a sequence, an equivalence class and a tagged alternative may all hold related information, yet the operations available on them differ.

Even an apparently adequate requirement can leave the object underdetermined. An object from which two entries can be recovered might also contain an extra entry. To say that the first two entries determine the whole, we need a further condition. Without it, a later map may require information that the proposed construction never supplied.

The problem is to turn the intended use into a mathematical specification, construct an object that satisfies it, and derive the maps and comparisons needed next.

### MATH.16:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar representation and needed operations | A convenient notation can make calculation easy while omitting a required construction or recovery. |
| Recoverable data and additional choice | Recovering the inputs leaves open whether they determine the complete result. |
| General specification and existence | A universal property can identify the desired object even when it has no realization in the chosen setting. |
| Structural sameness and computational effort | Two constructions can support the same maps while requiring different work to calculate with them. |

### MATH.16:4 - Solution

**Local mantra:** start from the use; choose maps and laws; construct the object; derive its uses; revise the changed requirement.

#### MATH.16:4.1 - Express the needed use as maps and equations

Describe what a user of the mathematical object will put in and obtain. Introduce symbols after those meanings are clear. A function `f:X -> A` takes an input in X and returns one element of A. Its direction matters: receiving an A and returning an X is another operation.

Ask what information completely determines the proposed result. If later use needs an extra choice, include that choice in the input. If the supplied data should suffice, require the resulting map to be unique.

The following contrasts help select a construction; they are examples of different mapping requirements:

| Needed use | Maps and question to formulate |
| --- | --- |
| Carry two components together and recover each one. | Seek maps from the new object to both component objects. What combined map is determined by supplying the two components? |
| Carry either kind of input, then process it according to that kind. | Seek maps from each input object into the new object. Do the two processing rules determine one rule on the combined object? |
| Combine components that must agree about a common quantity. | Express both accounts of that quantity in one codomain and require equality. |
| Identify inputs while retaining selected answers. | Which maps give the same answer on identified inputs, and therefore can operate on classes? MATH.2 supplies that quotient construction. |
| Interpret everything built from generating operations. | Which assignment to generators extends to a map preserving the operations? MATH.5 supplies the extension and its uniqueness. |

Choose the mathematical setting along with the maps. In the main route, the objects are sets and the permitted maps are all functions between them. A category specifies a setting through its objects, maps, identity maps and associative composition.

**Additional structure -- groups and topology.** For groups, choose homomorphisms preserving the group operation; for topological spaces, choose continuous functions. These choices change what must be constructed and proved.

#### MATH.16:4.2 - State the universal property before choosing an encoding

Turn the use into a requirement by comparing the proposed object with arbitrary permitted ways of supplying or processing its data:

1. Fix the objects already given by the question, together with their maps and laws. They remain the same throughout this comparison.
2. Introduce a variable object X for a possible source of data, or Z for a possible destination. Describe the maps and equations that make it an allowed instance of the needed use. Let it vary over every permitted instance, not just one sample. For example, a source of two components supplies functions from X to each fixed component set.
3. Seek an object P with the maps through which it will be used. Ask how an allowed instance should relate to P: should its data assemble into P, or should processing extend from P to a destination? Draw that comparison map in the corresponding direction.
4. Combine the comparison map with P's use maps in the order their domains require, and equate the resulting routes with the original maps. Require a comparison map for every allowed instance, and uniqueness when the supplied data should determine it completely.

This specifies the behavior a construction must realize. If the intended use leaves the maps or agreements undecided, return to that particular choice before asking for a universal object. The prepared-function case in :5.4 follows these steps for a use beyond pairing or tagging.

Suppose the question requires two recoverable components in A and B, and those components must determine the entire result. A and B are fixed; a trial source X supplies maps to both. Seek an object P with projections `pA:P -> A` and `pB:P -> B`.

For every allowed object X and maps `f:X -> A`, `g:X -> B`, require a unique map `<f,g>:X -> P` such that:

`pA composed with <f,g> = f`;

`pB composed with <f,g> = g`.

These equations say that forming the combined result and reading either component returns the supplied component. Uniqueness says there is no further choice in that combination. Any map `h:X -> P` is consequently recovered from its components:

`<pA composed with h, pB composed with h> = h`.

An object with these projections and property is a **product** of A and B. Its specification describes both how to construct a result and how to use it.

Now suppose the components must agree through maps `s:A -> C` and `t:B -> C`. Seek projections that satisfy:

`s composed with pA = t composed with pB`.

Require a unique combined map only for f and g satisfying `s composed with f = t composed with g`. This is a **pullback** of s and t: it combines precisely the data compatible under that equation.

To choose an object for either kind of input, reverse the mapping question. Seek maps `iA:A -> S` and `iB:B -> S` that place the inputs in the new object. For maps `f:A -> Z` and `g:B -> Z`, require a unique map `[f,g]:S -> Z` with `[f,g] composed with iA = f` and `[f,g] composed with iB = g`. This is a **coproduct**. In sets, a tag can preserve which input was supplied, so the processing rule can select the correct branch.

The comparison points into the product or pullback and out of the coproduct. Its direction follows the needed operation: assemble supplied components or extend supplied processing rules.

#### MATH.16:4.3 - Construct an object and establish the property

In sets, the product is the set of ordered pairs `A x B`. Use the coordinate projections and define `<f,g>(x)=(f(x),g(x))`. Both projection equations follow by reading the corresponding coordinate. Any function with those projections must return that same pair at every x, which proves uniqueness.

For the pullback, form the subset:

`Q={(a,b) in A x B | s(a)=t(b)}`.

The same pairing formula lands in Q exactly when the compatibility equation holds. Reading the coordinates again proves uniqueness. Q may be empty. The empty set is still a valid pullback in sets; it says no pair meets the stated compatibility requirement.

For a coproduct of sets, distinguish the two input branches with tags 0 and 1:

`S=({0} x A) union ({1} x B)`.

The injections are `iA(a)=(0,a)` and `iB(b)=(1,b)`. Define `[f,g](0,a)=f(a)` and `[f,g](1,b)=g(b)`. Every element has one of these forms, which establishes existence and forces the rule uniquely. Even when A and B are the same set, the tags keep the two branches distinct. For `A=B={0}`, handlers `f(0)=0` and `g(0)=1` therefore extend to a function taking `(0,0)` to 0 and `(1,0)` to 1.

**Additional structure -- groups and topology.** Establish that the object and maps have the chosen structure. For groups, define product multiplication componentwise. If f and g preserve multiplication, then their paired map does too, because each coordinate does. For a pullback of group homomorphisms, the compatibility equation is preserved by multiplication and inverses. A construction with continuous maps requires the appropriate topology and continuity arguments.

Use a known applicable construction when available. For quotient and generator questions, MATH.2 and MATH.5 provide the detailed operations. If the required object cannot yet be constructed, identify the unresolved existence or construction question. An existence theorem may supply a result for reasoning while leaving an effective way to obtain its elements for further work.

#### MATH.16:4.4 - Derive the next map, comparison or operation

Use the universal property to build the map the question needs. For a product, give the two component maps. For a pullback, also establish their agreement in C. For a coproduct, give a processing rule for each input kind.

The property also supplies equality tests. Two maps into a product or pullback are equal when both their projections agree. Two maps out of a coproduct are equal when composing each with iA gives equal maps and composing each with iB gives equal maps. This lets you compare an entire map through its required parts.

It can compare different constructions of the same object. If P and P' satisfy the same product property for A and B, the projections of each determine a map to the other. Composing these maps preserves both projections. The identity does too, so uniqueness makes the composites identities. Thus the two constructions are isomorphic by the maps that preserve their projections. MATH.7 develops the transport of further structure when a usable bijection has been obtained.

A new operation on the components needs a compatibility test. Here take Q to be the pullback of sets and `u:A -> A`, `v:B -> B` to be functions proposing updates. They induce a function `(a,b) -> (u(a),v(b))` on Q exactly when:

`s(u(a))=t(v(b))` whenever `s(a)=t(b)`.

The original agreement does not settle the changed one. A failed pair identifies which update or agreement condition must change. This gives a way to work on operations themselves while keeping their required uses visible.

**Additional structure -- groups.** When the update must also be a homomorphism, establish preservation of the group operation. Agreement of the updated components alone establishes only a function on the set of compatible pairs.

#### MATH.16:4.5 - Use the result and return to a changed requirement

Return the construction with the maps and conditions needed by its consumer. A name such as “product” helps recognition; the projections, formation rule and applicable laws let the receiver use it.

For a mathematical question, stop with the required map, equality, usable construction or demonstrated obstruction. For computation, obtain the procedure and resources needed for the chosen representation through C.29.2. A finite pullback can be enumerated by testing pairs, while a large or infinite one needs an appropriate computational method.

For an application to another subject, C.29 supplies the correspondence that gives the mathematical objects and equations their subject meaning. In particular, a compatibility equation must represent the actual agreement needed by the work. A pairing of functions on one input describes a different operation from two executions that modify a shared input. For the latter use, first specify which values each step reads and changes, and which intervening steps are permitted. Use that account to decide whether a function construction represents the work; the pairing alone leaves those interactions unspecified.

When the question changes, return to the affected mapping requirement. Adding agreement can turn a product question into a pullback question. Needing to accept either input can call for a coproduct. Needing only selected answers can call for a quotient. Retain a useful earlier construction while its earlier question remains current.

### MATH.16:5 - Archetypal Grounding

#### MATH.16:5.1 - Two classifications, then one shared integer

Two separately chosen integers have been classified. The first report gives its remainder modulo 2; the second gives its remainder modulo 4. The task is to combine the reports so that both can be recovered, and to add combined reports by adding their corresponding remainders. The two reports should determine the complete combined result.

Let `A={0,1}`, with addition reduced modulo 2, and `B={0,1,2,3}`, with addition reduced modulo 4. Adding the two reported numbers into one number loses recovery: reports `(0,1)` and `(1,0)` both give 1. Keeping a pair supplies both projections and requires no additional choice. All eight pairs are possible because the original integers may be chosen separately.

Now both reports must describe the same integer. The pair `(0,1)` fails: an integer with remainder 1 modulo 4 is odd. The modulo-4 report determines parity through `t(b)=b modulo 2`. Set s to the identity on A and construct the compatible pairs:

`Q={(0,0),(1,1),(0,2),(1,3)}`.

Every member comes from an integer. Addition stays within Q: `(1,1)+(1,3)=(0,0)`. A report determines the original integer only modulo 4.

**Additional structure -- groups.** With the stated modular additions, A and B are groups. The identity on A and the parity map t preserve addition, so Q with componentwise addition is also their pullback in groups.

The projection `(a,b) -> b` has inverse `b -> (t(b),b)`. If the next calculation is easier with one modulo-4 value, MATH.7 transports it through these maps. If the next question is which integers may be identified while retaining both reports, MATH.2 instead constructs their quotient modulo 4.

Returning to functions on the underlying sets, a proposed update exposes another choice. Incrementing the modulo-4 component alone sends `(0,0)` to `(0,1)`, outside Q. Incrementing both components gives `(1,1)` and preserves agreement for every pair in Q. The intended change to the underlying integer determines which component updates belong together.

**Additional structure -- groups.** The joint increment is not a homomorphism: it takes the identity `(0,0)` to `(1,1)`. It is suitable for updating the represented integer, but fails a requirement to preserve the group operation.

#### MATH.16:5.2 - Process both results or either result

One calculation returns an integer count; another returns a text label. A report containing both results needs a product. Its projections recover the count and the label, and the two values determine the report.

A different interface accepts either an integer count or a text label. It must display a count numerically and leave a text label as supplied. A tagged union, the coproduct of these sets, allows both handlers to determine one display function. An input tagged as a count follows the numeric handler; a text-tagged input follows the text handler.

The word “combine” did not decide which object to build. The question about formation and use did: recover two components from one report, or process either input through its own rule. These constructions describe values and functions. Whether executing the calculations reads or changes shared state is a further question about their execution.

#### MATH.16:5.3 - Two views of one quantity

A model has candidate states A and B for two component descriptions. Each description specifies the value of a shared quantity in C. For example, the two ends of an ideal connection may be required to have equal potential.

The product contains arbitrary state pairs. Requiring agreement selects the pullback of the two quantity maps. Its projections retain both component states, so a later calculation can still use their other quantities.

The physical account must justify the ideal connection and the meaning of that potential. If the connection has a relevant drop, the equality premise changes. A relation involving the drop and other quantities must be modeled before constructing its compatible states. The mathematical construction supplies the combination once that relation has been formulated; it does not choose the physical interaction law.

#### MATH.16:5.4 - Construct an object that can itself be applied

A function can be prepared by supplying a setting, then used with different inputs. We want a mathematical object representing the prepared function. Fix the input set A and output set B. A possible set of settings X supplies behavior `eX:X x A -> B`: it returns an output for a setting x and input a. Different X and eX describe different ways to prepare such behavior.

Seek a set E of prepared functions and an evaluation rule `ev:E x A -> B` for applying them. Preparing from a setting should give a map `h:X -> E`. To retain the original behavior, require:

`ev(h(x),a)=eX(x,a)` for every x and a.

Here prepared functions are equal when they give the same answer for every input. Thus the behavior specified by eX should determine h completely. Require a unique such h for every X and eX.

Construct `E=B^A`, the set of all functions from A to B. Define `ev(k,a)=k(a)`, and let `h(x)` be the function sending a to `eX(x,a)`. The required equation follows by evaluation. Any other proposed value for `h(x)` must give that same answer at every a, so it is the same function. This proves uniqueness.

For example, take A, B and X to be the integers and `eX(n,a)=n+a`. Then `h(3)` is the function that adds 3; `ev(h(3),6)=9`. The construction allows us to pass, apply and compare that function as an object. The conversion from a two-input function to a function returning a function is called **currying**. Distinguishing procedures with the same answers but different costs requires a further computational description of those procedures.

### MATH.16:6 - Bias-Annotation

Recognizing a familiar construction can make its requirements seem inevitable. In :5.2 the same informal request to combine results leads to a product or a coproduct depending on the needed operation. Write that operation before naming the construction.

The set examples make existence easy to see. Other choices of objects and allowed maps can change existence or require additional structure. Carry that choice into the argument rather than relying on the appearance of paired entries.

### MATH.16:7 - Conformance Checklist

- The working question identifies what must be formed, recovered or compared.
- Each map has a domain, codomain and meaning; its direction matches the required operation.
- The permitted maps and their preservation conditions are stated.
- Fixed objects are separated from the allowed varying instances of use.
- The universal property identifies the supplied data, the comparison map for every allowed instance, its equations and why uniqueness is wanted.
- A construction or applicable existence result supplies the object; a claimed construction has its existence and uniqueness arguments.
- A changed requirement is reflected in the construction or its admissible maps.
- Any computational or subject use obtains the additional operations and premises it needs.

### MATH.16:8 - Common Anti-Patterns and How to Avoid Them

**Recovery mistaken for full determination.** Take `A=B={0}`. Recovering both components from `A x B x {0,1}` works, but forming an element also requires choosing 0 or 1. If only A and B should determine the result, require the unique combining map. If the extra choice is useful, name it as part of the input.

**Compatible components processed incompatibly.** A map on each component need not preserve their agreement. Test the equation in :4.4; the one-component increment in :5.1 supplies a failing case and its repair.

**A familiar encoding chosen before its use.** A pair and a tagged alternative support different functions. Recover the intended formation and processing operations before selecting either.

### MATH.16:9 - Consequences

The result can be specified and compared through its permitted uses. Construction, extraction and equality arguments become connected, and a changed requirement identifies which mathematical work must be revisited.

The universal property leaves room for different implementations. Their mathematical correspondence can be established through the property, while their computational costs remain a separate reason for choosing one implementation.

### MATH.16:10 - Architectural Rationale

Organizing the choice around maps makes the required operations explicit before committing to an encoding. Including uniqueness expresses when the supplied data determine the whole result. It also gives reusable arguments for comparing maps and comparing realizations.

A direct representation remains economical for a single familiar calculation. The universal-property method earns its additional abstraction when several constructions are plausible, a representation must be changed, or later maps and arguments need to be derived. The product, pullback and coproduct cases expose different requirements. The prepared-function case shows how to formulate another requirement by varying its settings and behavior while keeping the input and output sets fixed.

Detailed quotient, generator-extension and structure-transport methods remain separately usable. They supply constructions and proofs after this method has identified the needed property. This separation permits a broader choice method without compressing those techniques into unexplained instructions.

### MATH.16:11 - SoTA-Echoing

For choosing an object through the maps it must support, the adopted line is universal construction in category theory. Riehl's [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf), §§2.3, 3.1 and 3.2, gives the general account and concrete set constructions. The present method uses that line to move from a working requirement to a construction, then to its derived maps and equality arguments.

Fong and Spivak's [Seven Sketches in Compositionality](https://arxiv.org/abs/1803.05316), especially the chapter on databases and categories, develops the use of these constructions across applications. Its contribution here is the attention to what transformations and queries the constructed object supports. Example 3.72 supplies the function-as-object construction through currying used in :5.4.

At comparable effort, a direct pair or tagged union is often enough when the operation is already settled. Use the universal account when the ambiguity or later reasoning makes it useful. A more elaborate categorical description adds no benefit to a calculation whose relevant conditions and result are already clear.

The elementary examples use ordinary equality and functions. If the work changes the permitted maps or the meaning of equality, reformulate the comparison and its equations in that setting. A requirement to compute the result can also reopen the choice of construction.

### MATH.16:12 - Relations

- **MATH.1** constructs composable paths when the required object retains generating steps and their order.
- **MATH.2** constructs quotients while preserving the selected operations and answers.
- **MATH.5** extends generator assignments to operation-preserving maps and proves their uniqueness.
- **MATH.7** transports structure through a bijection when a different representation is useful.
- **B.5.FM and B.5.TU** connect the working question, construction and use at the common reasoning level.
- **C.29 and C.29.2** supply subject correspondence and computational formulation.

### MATH.16:End
