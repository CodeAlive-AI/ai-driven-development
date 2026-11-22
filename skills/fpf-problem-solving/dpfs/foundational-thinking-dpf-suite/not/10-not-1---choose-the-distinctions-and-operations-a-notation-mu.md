## NOT.1 - Choose the Distinctions and Operations a Notation Must Support

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### NOT.1:1 - Problem frame

**Use this when** you are choosing or designing a notation and cannot yet say what its users must be able to express, recognize or do with an expression. A candidate may name all the right objects while hiding their order, dependence or duration. Another may express the distinction but make a frequent change require rebuilding the whole description.

Begin with a piece of work the user must perform with the notation, such as composing operations, tracing a dependency or performing a sequence. If the user needs a value, ask whether cases that look alike can require different values. If the user needs a workable action, look for one they can take across all cases that look alike. The proposed expressions and the knowledge available to their reader may already suffice.

The reader needs enough knowledge of the practice to explain why the cases differ and what a useful result would be. The designer can supply that knowledge or obtain the needed distinctions and inferences from a collaborator or an established source.

The result is a choice of distinctions and operations to support, with grounds showing how the proposed notation makes them available. Those grounds may come from a decoding rule that covers the required expressions, a constructed expression or an observation of use. The work may also justify keeping an existing notation, preserving an unresolved choice or obtaining a missing subject account before adding symbols.

If a suitable notation already exists and only one expression needs repair, construct that expression under its rules using A.6.3.RT.OE. Return here when the rules themselves lack a needed distinction or make the required operation impractical.

### NOT.1:2 - Problem

How can a notation designer determine what the notation needs to make possible before committing to its symbols and rules?

A list of concepts leaves the work underdetermined. The same concepts can enter different compositions, questions and changes. A notation sufficient for recognizing an object may be insufficient for constructing it; a description sufficient for one question may discard what another question needs. Designing from familiar examples alone can conceal these differences until a new case exposes the missing distinction.

### NOT.1:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Discrimination and economy | Showing more distinctions increases expression and reading work; omitting one can prevent the required conclusion. |
| Reading and changing | A compact finished description can be expensive to revise. |
| Shared conventions and reader preparation | Familiar conventions save explanation for one group while imposing learning or translation on another. |
| Expression and environment | A distinction may be carried by marks, layout, an interaction or available context. Changing the medium can remove that support. |
| Present work and discovery | Trying a notation can expose a useful operation absent from the initial requirements. |

### NOT.1:4 - Solution

**Choose the operation and its conditions → identify the distinctions it needs → find what carries them → establish how the proposed convention supports the work → retain or revise the requirement.**

#### NOT.1:4.1 - Choose an operation and the conditions for performing it

Describe what the user starts with, what they do and what they need to obtain. Prefer a question such as “after exchanging these two operations, what changes in the result?” to an aim such as “make the notation intuitive”. The former exposes what an expression must support.

Specify the preparation and access on which the operation relies. A mathematician may use established algebraic conventions; a performer may recognize a learned gesture; a program may receive only serialized text. An AI agent's access to a rendered page, a text extraction and an editor's internal structure are different conditions. Include the context the intended user can access.

One operation can settle a commission limited to that use. For a family of uses, trace each promised use to the distinctions and reading rule it needs. A composition or decoding rule can cover an entire family of expressions. Use contrasting cases when they help uncover a requirement or test a disputed distinction. For a shared expression, vary a local part while keeping the proposed summary fixed. Can another reader still recover the needed effect on their part or on the whole? When several readers can edit the expression, determine which choices they can make separately and which must identify the same item, revision or agreed change. One argument about the shared convention can cover several uses.

#### NOT.1:4.2 - Find cases whose difference changes the work

Start with what the reader must obtain. For an exact answer, see whether two possible situations can give different answers. If the answer is fixed by what the reader already knows, the same expression may serve the entire group. Two arrangements of the same components can have different outputs. Two performances with the same starting times can have different sustained intervals. For a choice of any acceptable action, consider the alternatives that the reader would still group together and the actions each permits.

Try the proposed notation with the context available at the moment of use. For an exact answer, indistinguishable situations with different answers reveal a loss. For one guaranteed action, look for an action that works across the whole group. Three possible editions might allow {A,B}, {B,C} and {A,C}. Every pair allows an action, while no action serves all three. If the work needs this choice, add a distinguishing reference, an accessible query or a reading rule backed by subject knowledge. A context that already identifies an applicable action can be sufficient. [NOT.5:4.4](14-not-5---translate-between-notations-while-tracking-lost-dist.md#not544---expose-distinctions-the-target-collapses) gives the corresponding test when translating an expression.

Conversely, two visibly different cases may be interchangeable for the present operation. Keep their shared representation if that simplification preserves the needed result. The question determines which differences matter.

A deliberately unfinished choice can itself matter. If the work permits an unspecified order or duration, retain a way to leave it unspecified and a way to recognize when the next operation needs it settled. A convention that silently chooses a value would change the work being described.

#### NOT.1:4.3 - Locate the information and operations behind the marks

Follow the user through the proposed operation. Which part of the expression identifies a participant, establishes a relation or permits a transformation? Which part is supplied by a convention, the surrounding account or an interaction with a tool?

This examination can reveal three different needs:

- The difference is known but cannot be expressed or recovered under the available rules. Design a way to carry it.
- The expression carries the difference, but obtaining or changing it is too costly. Change the arrangement or the supported operation; NOT.7 develops that redesign.
- The practice has not supplied the needed distinction or inference. Obtain that contribution from the relevant practitioner or method before prescribing how it must be expressed.

Test the whole expression and its usable context. A symbol may be ambiguous in isolation yet clear in a composition. A diagram may be clear to a prepared human reader while its plain-text export loses the grouping on which that reading depends. Preserve the effective context or revise the notation for the receiving conditions.

#### NOT.1:4.4 - Try a design choice through use

Propose a change capable of supporting the selected operation. It could mark operand groups, refer to a shared component, expose event duration or distinguish an unresolved alternative. Establish how a reader can recover the needed distinction under the proposed convention and the context available to them. A decoding rule can settle that question throughout its domain. When a difference could still be lost, construct the contrasting expressions and follow the operation through each.

Where modification matters, change an input, component or relation and follow the resulting edits. A contrasting case can expose a failing rule. For a reusable design, explain which construction or subject condition preserves the required operation throughout the intended expressions and changes. The demonstration of one successful edit gives a reader a place to start.

Separate the notation's contribution from supplied subject knowledge. In a diagram for composing functions, arrows can expose the order of application; the functions and the ability to apply them supply the numerical result. If the result cannot be obtained because an algorithm or physical law is missing, return that question to the corresponding practice.

An expert walkthrough can establish an explicit loss or a useful candidate change. When it remains uncertain whether the intended reader can recover or perform the operation, use C.2.8 to choose a bounded reading probe with the intended preparation and access. Obtain further evidence only when its outcome could change the design or the permitted use.

#### NOT.1:4.5 - Compare the work enabled and the work displaced

Compare candidate notations on the selected operations under comparable conditions. Look for a practical trade-off: a shared definition may make one update cheap while requiring the reader to follow references; expanded expressions may be easy to read locally while repeating changes in several places.

Keep both alternatives when they serve different necessary operations and the correspondence between them can be maintained. NOT.6 develops that arrangement. For a choice among alternatives, compare only characteristics that affect the work and state the selection criterion. A simple contrast can settle the local choice: one notation loses an answer that the other preserves.

A second design team may reuse a documented observation when its notation, operation and working conditions still match. To compare two admitted profiles under a declared comparator, use A.19.CPM. A.19.SelectorMechanism governs selecting a set from those results. One notation may make a needed expression easier to read while another makes its next alteration easier to perform. Establish each advantage in the intended work. If the effort for one operation is still unknown and could change the ordering, indicate what remains open. The design team can use an established trade-off to choose for its use or retain both notations for their different uses. A trade-off vocabulary helps identify what to examine. Ground a claim about the reader’s ability in evidence of the operation under its intended conditions.

Trying a candidate can reveal that the original question was incomplete. Revise the selected operations or cases when the newly visible distinction changes a useful next move. Then test the affected requirement again. This is a development of the problem and its proposed solution, for which C.40.CD supplies the common method.

#### NOT.1:4.6 - Retain the decision at the scale needed for the next construction

State the operation to support, the distinction it needs, how a candidate carries it and the burden or unresolved choice that remains. A short explanation beside the candidate can suffice. Keep the contrasting cases when they will help construct, teach or revise the rule.

Stop when the next notation construction or choice is clear enough to undertake. Detailed expression formation, interpretation and transformation can then be developed where needed. If a new example changes a supported operation or its conditions, revisit the affected choice.

### NOT.1:5 - Archetypal Grounding

#### NOT.1:5.1 - Same components, different composition

A team is designing a diagram notation for constructing pipelines of functions. Its first sketch shows the input, output and an unordered collection of function names. The current operation is to determine the result and then exchange two functions without losing their connections.

Use the supplied functions `f(z) = z + 1` and `g(z) = 2z`, with input `3`. Applying `f` then `g` gives `g(f(3)) = 8`. Applying `g` then `f` gives `f(g(3)) = 7`. Both cases have the same named components. The unordered sketch therefore loses a difference that the operation needs.

The designer tries directed connections, with the rule that a connection passes the output of one function to the input of the next:

```text
3 -> f -> g -> result     gives 8
3 -> g -> f -> result     gives 7
```

Now the reader can recover the composition order and derive each result from the supplied functions. Exchanging the two functions changes their connections; merely dragging a box on the page must either preserve those connections or expose that it changed them. The design has acquired both an expression requirement and a question about the editing operation.

If the diagram is only an inventory of available functions, the original unordered sketch can remain adequate. If later work needs branching or shared intermediate results, try those operations before deciding how their connections and identities will be expressed. Success with this linear case leaves those questions open.

#### NOT.1:5.2 - Same starting times, different durations

A notation for a sequence of signals lists their starting times in units of a shared pulse. Two sequences both start signals at `0` and `2`. In sequence A each signal lasts one unit; in sequence B each lasts two. The intervals are half-open: the signal is active at its start and inactive at its end.

For the question “when should each signal begin?”, the list `0, 2` suffices. For “is a signal active at time 1.5?”, it does not: the answer is no for A and yes for B. The omitted duration now changes the answer.

Try pairs of `(start, duration)`. Sequence A becomes `(0, 1), (2, 1)`; B becomes `(0, 2), (2, 2)`. The reader adds duration to start and compares 1.5 with the resulting interval. This exposes the needed difference with one simple convention. A timeline with interval bars might make repeated overlap questions easier; the pair notation is easier to transmit as plain text. Their comparative value depends on the operation and access.

If a performer's action determines the duration later, retain that unresolved value and identify which questions remain answerable. Suppose the first signal's duration is still to be chosen between 1 and 2. Write `(0, d)` with `d in {1, 2}, not yet chosen`. In either permitted case the signal is active at 0.5; at 1.5 the answer remains unresolved. Choosing `d = 2` makes the latter answer yes. The starting-time question remains answerable throughout. The notation must keep that choice open until the work settles it. Temporal and embodied notation design in NOT.8 develops such cases beyond this elementary timing example.

### NOT.1:6 - Bias-Annotation

Fluency can hide a notation's demands. A designer who knows the answer may supply order, grouping or duration from memory while believing the expression carries it. Test the selected operation with only the expression, declared conventions and available context. C.2.8 distinguishes this expert judgement from an actual reader's recovery.

A successful notation for one audience can require unavailable preparation in another. Apply a reading result to its audience, operation and access conditions. A human reading and a program’s interpretation may depend on different inputs or operations. Check the receiving conditions that can change the choice.

### NOT.1:7 - Conformance Checklist

Use these questions to examine the design decision when its adequacy matters.

- Can the intended user identify the working operation, its starting information and the result they need?
- Which lost difference would change the exact answer or leave the reader's choices without a common acceptable action? If the cases can safely share an expression, what establishes that for the intended use?
- Is the necessary information available in the expression, its declared conventions or an accessible interaction?
- For this task, can the intended reader use the expression and, if needed, change it? For a promise of reuse, how does the reading or editing rule cover the admitted family?
- Are the subject knowledge and reader preparation needed for that use recoverable?
- Does the next construction follow from the decision, with remaining uncertainty and displaced work visible where they matter?

### NOT.1:8 - Common Anti-Patterns and How to Avoid Them

| Failure | What changes the next move |
| --- | --- |
| Choosing symbols from a concept inventory | Add the relation or operation that distinguishes cases. The pipeline inventory names both functions but loses their order. |
| Validating recognition while relying on manipulation | Try the required change. A reader's ability to name a diagram's boxes leaves the effect of moving or reconnecting them unresolved. |
| Requiring every difference to be written | Keep the simpler expression when the omitted distinction cannot change the selected result; the onset list suffices for starting times. |
| Completing an unknown to fit the notation | Express the unresolved choice or narrow the answerable question. A supplied duration would change the partly designed signal sequence. |
| Treating a familiar layout as shared context | Check which parts of the layout reach the reader. Text export can remove grouping used in the displayed diagram. |

### NOT.1:9 - Consequences

The next notation decision becomes a choice about work that can be attempted. A designer can explain why a distinction, convention or editing operation is needed and can recognize when a simpler notation suffices.

Establishing a notation requirement can take analysis of an existing rule, construction of contrasting expressions or observation of use. It can also reveal a gap in the subject account that notation design alone cannot settle. Keep the operations and conditions the grounds cover. A new use may depend on a distinction that was dispensable for the earlier one.

### NOT.1:10 - Architectural Rationale

A notation provides ways to form and use expressions. What to support depends on what the user needs to obtain or change. Starting with that operation connects the subject matter, reader preparation and representation.

Contrasting cases can make an omitted distinction consequential. If the same available representation is compatible with different required answers, a reader relying on it cannot be guaranteed the right answer in both cases. Recover the difference, obtain additional information or qualify the use. A decoding or cost argument can establish what the representation permits under its assumptions. For a claim about what intended readers actually did and what it cost them, use evidence of their work under the relevant conditions.

The method derives a notation requirement from the work the expression must support. A general argument, a decisive contrast or observations of use supply different grounds for choosing a scheme. NOT.2-.4 develop formation, interpretation and transformation rules. A.6.3.RT.OE addresses a different starting condition: the scheme is available and an operative expression must be built under it. C.2.8 characterizes what a prepared observer can extract; the present method uses that question to construct or choose a scheme.

### NOT.1:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Blackwell and Green, [Cognitive Dimensions of Notations](https://www.cl.cam.ac.uk/~afb21/publications/BlackwellGreen-CDsChapter.pdf), historical foundation, especially the activity and system analysis sections | Adopt analysis relative to activity, notation, environment and medium. The method uses concrete operations to expose costs and trade-offs. It retains the source's warning that the dimensions are not a checklist yielding a universally best notation. |
| Brazauskas and Blackwell, [PUX Explorer](https://ppig.org/files/2024-PPIG-35th-brazauskas.pdf), PPIG 2024, §§2, 4.2 and 6 | Adapt the co-development of design problem and solution and the activity/experience comparison. Its study involved six specialist music-notation researchers. This supports a design aid at that scope, not general performance gains. Its trade-off weights were assigned from textual descriptions; they are not measured universal effects and are not imported here as quality scales. |
| Ross and colleagues, [Affordances of Sketched Notations for Multimodal UI Design and Development Tools](https://arxiv.org/abs/2508.09342), 2025 preprint, abstract-level contribution | Retain the distinction between isolated-symbol recognition and interpretation of a whole contextual sketch in AI-assisted work. The abstract motivates checking the receiving context. It does not establish a general advantage of a particular design or interpreter. |
| Kruchten, McNutt and McGuffin, [Metrics-Based Evaluation and Comparison of Visualization Notations](https://ieeevis.b-cdn.net/vis_2023/pdfs/v-full-1328.pdf), IEEE VIS 2023, §§3–4 | Reuse matched examples and their metrics to locate differences for closer reading when comparing working notations. The method assumes expressions implementing the shared tasks. Its metrics do not capture the whole user experience or supply a universally best notation. |

**Choosing the design move.** When the needed distinction is still unknown, look for indistinguishable cases whose required answer or collectively available actions reveal the loss. A gallery-based comparison already needs expressions that implement chosen tasks; preparing that gallery cannot replace discovering the missing task or distinction. Once several viable notations support a stable family of work, a shared set of examples becomes useful: compare the same readings and edits, use metrics to find costly cases, then inspect those cases. Preparing that comparison takes additional work but can expose repeated-change burdens hidden by one successful example. Reopen the small comparison when that broader burden could change the choice; NOT.7 develops the corresponding redesign. Cognitive Dimensions and PUX can also help discover or reformulate the operations to compare.

This method adapts those sources to construct requirements from contrasting cases, as illustrated by the function pipeline and signal durations. The method connects notation design to available FPF representation, extraction and problem-development methods.

### NOT.1:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| A.6.3.RT and A.6.3.RT.OE | Choose a representation and a medium that support the intended operation. If using an existing notation, construct the expression under its formation and interpretation conventions. Develop a missing convention here when it prevents the required construction or reading. |
| C.2.8 | Characterizes recoverable structure for a prepared reader with stated access and effort; use it when extraction difficulty changes the notation choice. |
| C.40.CD | Develops a problem and candidate ways of dealing with it together when a notation trial changes the useful question. |
| C.11.DUA | Helps decide whether another comparison or reader probe can change the choice enough to justify its cost. |
| A.19.CPM and A.19.SelectorMechanism | Govern reusable comparison and set selection under declared conditions; preserve trade-offs instead of forcing one winner. |
| MATH.17/.18 and CMP.12 | Supply mathematical constructions and interpretations, or an effective interpreter and translation. They develop consequences and operations whose needed expression can be selected here. |
| NOT.2-.4 | Develop the chosen expression-formation, interpretation and transformation rules. |
| NOT.5/.6 | Develop translation and complementary representations when the needed operations call for more than one notation. |
| NOT.7/.8 | Develop redesign around difficult operations and notation whose distinctions unfold in time or embodied action. |

### NOT.1:End
