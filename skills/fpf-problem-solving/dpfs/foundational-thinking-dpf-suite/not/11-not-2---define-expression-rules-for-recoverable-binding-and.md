## NOT.2 - Define Expression Rules for Recoverable Binding and Composition

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### NOT.2:1 - Problem frame

**Use this when** a notation needs rules for combining expressions or referring to their parts, and the proposed marks leave those rules unclear. Readers may disagree about an operation's operands, the declaration an occurrence of a name uses, or which connections join two components.

The working question is “How can another user construct and recover the intended arrangement under these rules?” Start with one expression that admits two consequentially different readings. Give its components explicit places, make their grouping and references recoverable, and use the resulting construction to perform the intended operation.

The result is a small set of formation, binding and connection rules demonstrated by an expression and a contrasting case. These rules can support mathematical formulas, diagrammatic descriptions or structured sequences. A complete grammar or software parser is needed only when the work requires it.

The reader must know what the relevant components and operations mean, or obtain that account from a practitioner. The examples below require elementary arithmetic and the stated conventions. Theory of formal languages and category theory are optional tools for extending or proving properties of a scheme.

Use the rules already provided by a suitable notation when they settle the question. A.6.3.RT.OE helps construct an operative expression under such a scheme. Use NOT.1 first if the work has not yet determined which distinctions or operations the notation must support.

### NOT.2:2 - Problem

How can the rules for forming an expression expose its components, references and permitted composition well enough to support the required reading or change?

A printed formula can conceal two groupings. The same letter can name an external parameter and a locally introduced variable. Diagram ports with the same value type can have different roles. Correctly recognizing the individual signs therefore leaves open which whole has been expressed.

### NOT.2:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Compact writing and recoverable structure | Omitting delimiters saves space but can hide an operand boundary. |
| Local naming and larger composition | A useful short name inside one component can collide with a name supplied by its surroundings. |
| Equal types and different roles | Two admissible inputs may occupy different positions in an operation. |
| Flexible presentation and stable interpretation | Layout may change while connections remain; another layout change may alter the expression. |
| Partial construction and usable interpretation | An unfinished expression can retain a missing part, provided the reader knows which operations remain available. |

### NOT.2:4 - Solution

**Identify the constructors and their places → make grouping recoverable → define how references are resolved → define permitted connections → construct and read contrasting cases → abbreviate only what the reader can recover.**

#### NOT.2:4.1 - Identify the expression constructors and their operands

Take the needed operation and distinctions from the working question or NOT.1. Describe the elementary expressions and the ways to construct a larger expression from them. For each construction, identify the required parts and what may occupy each place.

For example, a summation expression needs an index declaration, bounds and a body. A two-input transformation needs both inputs and a way to distinguish their roles. A repeated sequence needs a repeat count and the sequence being repeated. These are different constructors with different rules.

State the restrictions that the intended use needs. The restrictions may concern the kind of an operand, the number and order of connections, or a relation between component interfaces. Keep a missing part visible when partial construction is allowed. Identify the operation that requires the part to be supplied.

#### NOT.2:4.2 - Make the composition structure recoverable

Choose how a user can determine which parts belong to each construction. Text may use delimiters, indentation or precedence; a diagram may use enclosures, named ports or connections. A notation unfolding in time may use a learned boundary gesture or a segmentation convention. Explain the selected rule where its effect is not already established for the intended reader.

Try a nested construction. Recover the outer operation and its immediate parts, then repeat that reading within each part. This is a useful structural reading for tree-like expressions. When a component is shared or a connection returns to an earlier component, expose its reference or connection instead of pretending that every use is an independent nested copy.

Choose the structural distinctions needed by the operation. Some schemes identify several bracketings or drawings as the same expression. Establish the relevant equivalence before omitting their differences. If alternatives are intentionally unresolved, show that unresolved choice and postpone only the operation that needs it decided.

#### NOT.2:4.3 - Define which declaration or external value a reference uses

Identify the constructions that introduce local names and the parts in which those names apply. State how a name occurrence reaches its declaration or an input supplied from outside. The visible extent of a box or line becomes a scope boundary only through an established rule of the notation.

For a notation with lexical scope, a common rule resolves a name at its nearest enclosing declaration with that name; if there is none, the value must come from the declared external context. Adopt that rule only when it fits the intended interpretation. Other schemes can make references available through earlier statements, explicit identifiers or connections. Define their resolution accordingly.

Trace the references in one expression with repeated names and one expression with a free input. Here a free input is one whose value must be supplied from outside the expression. If insertion, copying or renaming changes which declaration an occurrence reaches, expose that change before treating the result as equivalent. NOT.4 develops transformations that preserve the intended use.

For a reusable component, distinguish its locally introduced names from the inputs and results made available at its boundary. Compose components by those boundary references. A displayed label can be repeated without identifying its occurrences as the same declaration; the reference rule must settle that question.

#### NOT.2:4.4 - Define the permitted connections between components

Specify which component places can be connected and what the connection means for forming the expression. If a connection passes a result to an operand, include the operand's position or role as well as its accepted kind. Two inputs of the same kind may still be ordered.

Construct the compound expression and determine its remaining external inputs and outputs. Check each newly connected boundary; an unconnected required input remains an input to be supplied. If the scheme permits shared values, show how repeated references obtain that value. If it describes resources whose copying requires an operation, include that operation rather than deriving copying from a forked line alone.

A connection that forms a cycle needs a rule admitting and interpreting that cycle. Depending on the practice, it might describe an equation, feedback through time or a repeated computation. Choose the intended construction before using one picture for these different operations. NOT.3 develops its interpretation, and CMP.12 supplies an effective evaluator when one is required.

Formation rules establish a permitted expression. Whether its described mathematical construction exists, its algorithm terminates or its physical realization works remains a question for the corresponding methods. The rules should expose the information those questions need.

#### NOT.2:4.5 - Construct and read the cases that challenge the rule

Build the intended expression from the declared parts. Recover its grouping, resolve the references and identify the component boundaries. Then perform the required operation with the supplied interpretation.

Use a contrasting case that could reveal a mistaken rule. Depending on the chosen construction, change the grouping, reuse a name inside another scope, exchange two ports or introduce a shared component. Select the challenge because its interpretation can change the result.

If two readers still recover different arrangements that matter to the work, locate the point of divergence. Add or repair the corresponding delimiter, reference rule or connection convention. If both arrangements express the intended equivalence, make that equivalence part of the scheme instead of forcing one arbitrary drawing.

#### NOT.2:4.6 - Retain usable conventions and controlled abbreviations

Keep the rule at the scale required by its next use. A legend and a worked construction can suffice for a local diagram; repeated automated processing can justify a grammar, parser or structural editor. A user must be able to recover any omitted structure that changes the operation.

For an abbreviation, give the expansion or another way to establish its meaning. If several expansions are allowed, show why the difference does not affect the intended use. NOT.4 handles the corresponding preservation argument. Retain a visible distinction when no such argument is available and the choice matters.

The method finishes with rules that permit the required construction and make its use recoverable, or with a specific unresolved formation or interpretation question. Teaching those rules and comparing their reading cost use the relevant learning and explanation methods; a more explicit syntax alone does not establish that a reader has learned it.

### NOT.2:5 - Archetypal Grounding

#### NOT.2:5.1 - A sum with a local index and an external parameter

A team is designing a compact notation for repeated addition. Its proposed expression is:

```text
sum i=1..2 of i + p
```

The notation has not specified where the summation body ends. At external parameter `p = 10`, two readings give different results: `(1 + 10) + (2 + 10) = 23`, or `(1 + 2) + 10 = 13`.

Choose a constructor `sum(index, lower, upper, body)`. It introduces the index only within `body`; bounds use the surrounding context. Choose `add(left, right)` for addition. These rules express the first reading as:

```text
sum(i, 1, 2, add(i, p))
```

The occurrence of `i` in `add(i, p)` reaches the local index declaration. The occurrence of `p` has no local declaration and uses the external value 10. Substituting the two index values gives 11 and 12, then 23. The second reading has a different construction:

```text
add(sum(i, 1, 2, i), p)
```

Its outer operation adds the external parameter once and gives 13. The notation now makes the two operand structures recoverable.

Naming also matters. The expression `sum(p, 1, 2, add(p, p))` is a valid expression under the chosen lexical rule, but both occurrences in its body refer to the index. It gives 6 and no longer uses the external parameter. To rename the index while preserving that parameter, choose a name such as `j` that does not capture it: `sum(j, 1, 2, add(j, p))` still gives 23. This example identifies the binding condition; NOT.4 supplies the general transformation method.

#### NOT.2:5.2 - Two ports of the same type with different roles

A diagram notation describes a ratio operation. It has two numeric inputs, `numerator` and `denominator`, and a numeric output. The supplied rule divides the numerator by a nonzero denominator. Source A supplies 6 and source B supplies 3.

The first drawing joins both sources to an unlabeled box. Knowing that both connections carry numbers leaves their operand positions undecided. Choose named input ports and preserve their identities when the box is moved or redrawn:

```text
A: 6 -> ratio.numerator
B: 3 -> ratio.denominator
ratio.result -> answer
```

The result is 2. Reversing the two input connections is another well-formed construction with result 0.5. Port names make that change visible even though the input types remain the same.

Now enclose the ratio in a reusable component. Its exposed inputs refer to those two ports, and its output refers to `ratio.result`. Renaming the internal ratio box or changing its position can preserve those boundary connections. Swapping the connections changes the expressed operation. A rule that permits the former does not thereby permit the latter.

The same design question arises whenever compatible participants occupy different roles in a relation or operation. More elaborate diagram calculi can give the permitted connections and drawing equivalences mathematical definitions.

#### NOT.2:5.3 - Scope in a structured sequence

Suppose `sequence(A, B)` means perform A and then B, and `repeat(n, S)` means repeat S n times. Then `repeat(3, sequence(A, B))` contains three performances of each action. `sequence(repeat(3, A), B)` contains three of A and one of B. A written delimiter, spoken grouping cue or learned gesture can carry this boundary if the receiver can reliably use its convention. The temporal realization and effort of perceiving or performing it are further questions for NOT.8.

#### NOT.2:5.4 - Resolve a movable label at the time of its use

Three physical cups have permanent numbers 1, 2 and 3, volumes 20, 10 and 0 ml, and capacity 50 ml each. Removable tags A, B and C initially mark cups 1, 2 and 3 respectively. An instruction H says to transfer 5 ml from A to B. Each letter refers to the cup bearing that tag when the transfer is performed.

Write `H; swap-tags(B, C); H`, where the swap moves only tags. The first H gives volumes `(15, 15, 0)` by permanent cup number. After the swap, B marks cup 3. The second H therefore gives `(10, 15, 5)`. Both transfers have sufficient source volume and destination capacity.

The abbreviation H retains a lookup to perform, not cup numbers fixed when H was defined. If the intended instruction instead bound A and B permanently to the original cups, the same two transfers would give `(10, 20, 0)`. The designer must choose the rule matching the work. Changing the tags is an action on the represented situation; renaming a letter in the notation while preserving its reference is a different change.

### NOT.2:6 - Bias-Annotation

A designer can mistake their own intended grouping for a rule already available to the reader. Recover the expression from its declared conventions before relying on the intended result. The sum example separates those two readings with different outputs.

Familiar programming conventions can also be imported into another notation without justification. State the resolution policy that fits the represented work. An arrow, enclosure or repeated name acquires its binding and composition role through that policy.

### NOT.2:7 - Conformance Checklist

Use the applicable questions when the construction rules need checking.

- Can the reader recover the components and the places they occupy from the expression and available conventions?
- Are the groupings that change the operation distinguishable, or explicitly retained as unresolved alternatives?
- Does each needed reference reach its declaration, external input or unresolved place according to the stated policy?
- Do composition rules account for the roles of connected participants and the resulting external boundary?
- Does a contrasting construction expose a consequential change of grouping, reference or connection?
- Can an abbreviation be expanded or otherwise interpreted without losing a distinction needed by the operation?

### NOT.2:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Supplying a constructor list without binding rules | State which constructors introduce names and where those names apply. The sum's index declaration governs its body. |
| Treating a repeated spelling as the same reference | Resolve the occurrence through its context. Local `p` can hide the external parameter in the sum example. |
| Checking input types but ignoring operand roles | Identify ordered or named places. The ratio receives numbers in either arrangement but computes different answers. |
| Letting layout imply an undocumented operation | Define which spatial or temporal relations carry grouping and connection; preserve those relations when changing presentation. |
| Dropping delimiters without recoverability or equivalence | Retain them until the precedence rule or an appropriate equivalence justifies their omission. |

### NOT.2:9 - Consequences

Users can construct expressions whose parts and references can be recovered, and can locate where a change alters the described operation. The same rules provide an input to interpretation, translation and automated processing.

Explicit structure can make an expression longer or impose conventions to learn. Controlled abbreviations and alternative views can reduce that burden once their interpretation is established. A scheme can also require a richer account of scope or interfaces than the first examples revealed.

### NOT.2:10 - Architectural Rationale

Formation, binding and composition answer connected questions. Formation identifies how an expression is built. Binding determines how its references obtain their values or participants. Composition determines how component boundaries are joined. A grammar that answers only the first question can leave the other two undecided.

This method develops the missing rules. NOT.1 selects what the work needs them to support; NOT.3 gives the interpretation and reading operations. A.6.3.RT.OE supplies construction under an available scheme. MATH.17/.18 can describe the operations and their interpretations mathematically, while CMP.12 constructs an effective interpreter or translation when required. The general notation-design result remains usable without first constructing all of those formal accounts.

Different graphical presentations or local names can express the same construction under the chosen rules. Treating them as equivalent requires the corresponding argument; it cannot be inferred from visual similarity. Conversely, giving two ports the same type cannot identify their roles. Keeping those questions explicit allows the notation to help reasoning about the construction itself.

### NOT.2:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Gheri and Popescu, [A Formalized General Theory of Syntax with Bindings](https://www.andreipopescu.uk/papers/bindings.pdf), §2 | Constructors alone leave binding positions undecided. Sections :4.1/.3 add the required binding rules; :5.1 works the sum and capture contrast. The source's alpha-equivalence, freshness and substitution theory supports formal development when needed. |
| Piedeleu and Zanasi, [An Introduction to String Diagrams for Computer Scientists](https://arxiv.org/abs/2305.08768), §2 | Sections :4.2/.4 use typed, ordered interfaces and drawing equivalence under stated equations; :5.2 shows why equal input types alone lose a needed role distinction. Symmetric monoidal categories supply one mathematical class of schemes. |
| Wehmeier, [Binding in classical and dynamic predicate logic](https://link.springer.com/article/10.1007/s10849-026-09472-0), 2026, introduction and §2 | Shared surface syntax can have different semantic binding behaviour. Section :4.3 therefore selects a resolution policy that fits the interpretation instead of treating nearest lexical binding as universal. |
| Dutilh Novaes, [Formal Languages in Logic](https://doi.org/10.1017/CBO9781139108010), 2012, pp. 53-54 and §5.2.1, historical foundation | Keep diagrammatic formation and work with external inscriptions among the available choices in :4.2/.6. This counters selecting textual syntax merely because it has explicit rules. The resulting convention still has to support the reader's operation; explicitness alone establishes no learning advantage. |
| Zwaan and van Antwerpen, [Scope Graphs: The Story so Far](https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.EVCS.2023.32), 2023, §§1–2 and 5 | Scopes, references and declarations can be related by paths with visibility and precedence policies. This is a developed alternative when static name resolution crosses nonlexical boundaries. Its expressiveness and execution costs remain relevant. |

**Choosing the rule design.** Retain familiar conventions when they already determine the needed grouping, reference and connection. A constructor list or an implicit layout is cheaper to state, but the sum and ratio cases show the price when it leaves two consequential readings. For that local difficulty, add the missing scope, delimiter or operand role and try the changed expression. This costs more signs or conventions to learn, while preserving a first use through a legend and worked construction.

When static references cross imports or other boundaries that simple nested environments do not handle conveniently, a scope-graph model can make the resolution policy explicit and reusable. It requires constructing those scopes, paths and priorities, and assessing the available implementation. Use that richer account when the reference problem calls for it, rather than adding it to the elementary sum. Likewise, choose a formal binding theory or diagram calculus when its laws are needed for repeated transformation or reasoning.

Revisit the retained choice when a needed expression cannot recover its references or composition, the interpreted operation changes, or a less costly available scheme preserves the same needed distinction. The synthesis is a way to construct and revise those rules.


### NOT.2:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1 | Selects the distinctions and operations the notation must support. |
| A.6.3.RT and A.6.3.RT.OE | Supply representation-scheme distinctions and expression construction when rules already exist. |
| NOT.3 | Develops the interpretation and reader operations that use the constructed expressions. |
| NOT.4 | Develops transformations with the necessary preservation, binding and side conditions. |
| MATH.17 and MATH.18 | Supply operations on operations and interpretations for formal accounts of composition and binding. |
| CMP.12 | Constructs effective evaluation and translation of an admitted expression structure. |
| NOT.5 and NOT.6 | Develop translations or complementary expressions while retaining needed references. |
| NOT.7 and NOT.8 | Develop redesign for difficult reader operations and notation carried through time or embodied action. |
| C.2.8 | Characterizes what the prepared reader can recover under the actual access and effort conditions. |

### NOT.2:End
