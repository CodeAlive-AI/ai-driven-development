## E.5.2 - Notational Independence

> **Status:** Stable

### E.5.2:1 - Problem frame

Use this pattern when expressing FPF content or using another expression to carry that content. Keep the conceptual meaning recoverable while choosing an expression that supports the intended work. A diagram, calculus or sequence of learned signs may help a reader reason or construct a result.

A single expression needs an explanation of its interpretation. A semantic mapping is needed when expressions are compared or one is translated, substituted or relied on as carrying the other's content.

A **representation language** supplies conventions for forming and interpreting expressions. A particular table, drawing, formula or vocal phrase is an **expression** read under those conventions. When a decision depends on which forms the language admits or which readings they can carry, use E.5.2.L:4.1. An ordinary choice of expression can be made here.

FPF concepts must remain understandable across disciplines, tools and future notations. If their meaning can only be recovered from one diagram style, file syntax or markup dialect, other users must reconstruct it before they can apply the pattern.

### E.5.2:2 - Problem
A definition can depend on unstated conventions of one glyph set or diagram grammar. Translation then changes its claims or leaves them unclear. Treating every visual form as an illustration leaves a useful construction or reasoning operation out of the description when the expression carries that operation.

### E.5.2:3 - Forces

| Force | Tension |
|-------|---------|
| **Expressiveness** | An expression may support reasoning and construction. Its meaning must remain recoverable in another suitable notation. |
| **Continuity of use** | Framework claims need to remain recoverable as representation conventions and the tools used to read them change. |
| **Reader preparation** | An expression can make an operation convenient for a reader trained in its conventions, while another reader needs more preparation or a different expression for that task. |

### E.5.2:4 - Solution - Keep meaning portable while choosing a useful expression

1. **Explain the meaning and operative use.**
   Normative content **SHALL** state the concepts, claims and conditions needed for its use, using prose and mathematics as appropriate. Explain the interpretation of meaning-bearing signs and relations.

   A diagram, calculus or learned vocal-gestural expression may carry a reasoning or construction step. When it does, explain the operation and its prerequisites locally or cite the guidance for that subject. The pattern about that subject or the applicable Method governs the reasoning or construction. The reader obtains the subject result by applying that Method.

   When the intended operation depends on a change of representation language or reasoning medium, use A.6.3.RT to construct and compare the expressions. A faithful translation whose purpose is textual restatement can use A.6.3.CR.

2. **State the semantic mapping.**
   When expressions are compared or one is translated, substituted or relied on as carrying the other's content, their semantic mapping **SHALL** be stated.

   Name the source expression and the expression being compared with it. Name their representation languages when the rules matter to interpretation. State the correspondences for the claims and conditions needed by the intended use. If a relevant distinction is lost, state the loss and limit the equivalence claim accordingly.

   First check that the display, its conventions and the other information available to the recipient fit at least one possible situation. If they conflict, resolve the conflict before relying on the display. For a value or a yes-or-no decision, start with the answer the recipient needs. Could two situations consistent with everything the recipient gets yield the same display and different answers to that question? If so, locate the missing information or limit the use. A display can determine whether a limit was exceeded even when it gives only a range for the value. To rely on it, show that every value still possible gives the same decision. Count any independent information used in that argument among the prerequisites.

   The recipient may instead need any one acceptable choice. A choice that works in every situation still consistent with the display can be made now, even when the complete lists of acceptable choices differ. If every situation has a solution but they share none, another observation may show which one to choose.

   Show how the intended reader obtains the determined answer or makes the supported choice with the preparation and resources available. Use A.6.3.RT.OE when the expression needs to support a calculation, comparison or edit. Use B.5.MR to compare models when the substitution also changes what they say is possible about the same subject.

3. **Reference the conceptual role.**
   If the Core cites a diagram, refer to its conceptual role, such as a boundary schematic, rather than making a file or syntax name part of the concept.

4. **Keep conceptual prefixes neutral.**
   Use E.10.P for the prefix registry and required anchors. A conceptual label's meaning **MUST NOT** depend on its expansion into a serialized name or URI. If a tool supplies such an expansion, describe the relation between the conceptual label and the tool's name or URI in Tooling or Pedagogy, and mark it informative.

5. **Identify what the form governs.**
   A Core card or table can identify what the reader needs to record and how the entries relate. Another expression can carry those same claims. When the work calls for a file, publication or message in a specified form, check the submitted expression against the convention for that form. E.5.1:4 permits the exact syntax needed for this judgement. A correctly formed submission can still contain an incorrect claim. An independently specified tool or delivery procedure has its own conditions. When proposing a new syntax rule, explain what the users of the governed form need it for. A restriction needed solely by one validator belongs in Tooling with that validator. Put the implementation of the automated check there as well.

The first result is an expression whose meaning can be recovered, with an explanation of any reasoning or construction step it supports. Include a semantic mapping when the use compares it with another expression or depends on the content it carries from that expression.

If a claim changes, compare again with the named source expression. Then repair the correspondence or narrow the claimed equivalence and permitted use.

Use A.6.3.RT to compare content carried between expressions and A.6.3.RT.OE to construct an expression with which the intended operation can be performed. If the representation language cannot express a needed distinction, select another language or extend its conventions before claiming that the distinction is preserved.

### E.5.2:5 - Archetypal Grounding (System / Episteme)

A pattern describes a pump boundary by specifying which components belong to the pump. A table records each component's membership. A diagram places the same components inside or outside a closed line. The line denotes the selected boundary, with no claim about physical distance or drawing scale.

The table's reading convention assigns membership through a field value. The diagram's convention assigns it through enclosure. The table and diagram are the two expressions being compared. Their semantic mapping relates entries to labelled components and membership values to placement relative to the line. Both expressions preserve the membership claims.

The diagram can help the user examine connections across the boundary. That operation depends on the represented connections and their interpretation. The boundary's meaning remains available if the table, or another notation that preserves the membership claims, replaces the diagram.

In the episteme case, F-G-R assurance components can be described in prose and represented in a diagram. Explain which elements denote the assurance components and which relations denote their connections. A triple-store serialization stores this content using tooling conventions. Its storage names do not define the components.

An R-score table can also be rendered as a heatmap. State which score or interval each colour denotes and how the review threshold treats equality. For a cell that represents several scores, apply the review rule to every score still possible. If all would be flagged, flag the cell. If all would pass, the cell passes this threshold check. If some would be flagged and others would pass, consult the values or other available evidence for that decision. For an order requiring the numeric table itself, deliver the table even if the heatmap settles every flag.

A project instruction permits a motor to start only while both the clamp-closed and pressure-present signals are true. A local sketch replaces this with `clamp closes -> pressure arrives -> motor starts`, where each arrow means only that one event precedes the next.

The sketch shows an event order but omits the required overlap: it does not rule out the clamp reopening before pressure arrives.

Compare the source condition with the sketch's timing relations. Show that motor start falls within the overlap of the two true signals, or limit the sketch to showing a proposed event order and use the source instruction to decide whether starting is permitted. This comparison is needed because the sketch is used in place of the instruction.

### E.5.2:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑NI.1** | A Core pattern **MUST** make its concepts, claims and conditions intelligible independently of the notation used to present them and explain how to interpret meaning-bearing signs and relations. Where the claim concerns conformance to a particular form, the explanation identifies the governing convention and retains the syntax needed to test the submitted expression (E.5.1:4). |
| **CC‑NI.2** | An illustrative expression **SHALL** be marked “informative”. When an expression carries a reasoning or construction step, explain that operation and its prerequisites locally or refer to the guidance that defines them. |
| **CC‑NI.3** | When expressions are compared, translated, substituted or relied on as carrying the same content, the semantic mapping **MUST** identify the compared expressions, their interpretation rules where needed, the claims and conditions preserved, and any use-relevant loss or limit. The mapping claim does not assert equal user capability or effort. |
| **CC‑NI.4** | A conceptual prefix follows E.10.P's registry and anchor rules. If its expansion into a serialized name or URI is shown, that expansion **SHALL** be marked *informative* and **MUST NOT** be required to interpret the concept. |

### E.5.2:7 - Consequences

The explanation and mapping let a reader follow named claims between the compared expressions. Stated losses show where a substitution needs a narrower use or a repair, as in the heatmap and timing examples.

Authors must explain the correspondences needed for that use. Keep the comparison to the expressions and distinctions the use requires. Reuse a mapping when it covers the expressions, interpretation rules and claims needed for the present use.

Readers may also need preparation for an expression's operation. State those prerequisites or refer to the guidance that supplies them, as required by §4.

### E.5.2:8 - Rationale
A notation can preserve meaning while changing which operations a reader can perform readily. Explaining interpretation, comparing expressions when needed, and retaining their operative use supports **P-1 Cognitive Elegance** and **P-2 Didactic Primacy**. Keeping conceptual meaning in the Core and implementation formats in Tooling preserves **P-5 FPF Layering**.

**SoTA question and choice.** How can framework content remain understandable across notations while an expression also supports reasoning or construction? Adopt recoverable interpretation of concepts, claims and conditions. Adapt this portability rule to an expression that carries an operation by explaining its use and prerequisites. Compare the content whenever another expression is used as equivalent.

A prose-first alternative treats diagrams and written calculi as secondary illustrations. It keeps verbal definitions accessible, but can exclude an operation from the normative account when the operation is performed through the expression. Reject that blanket restriction.

For example, in the Euclidean construction in A.6.3.RT.OE:5.1, the same segment participates as a radius and as a triangle side. The prepared expression helps the reader combine those relations. Its role needs an explanation of that operation, beyond a caption describing the picture. Either intersection of the two circles yields a valid triangle on the given segment. A request for the triangle on a specified side adds a condition to that construction.

A second alternative is to require one canonical notation. This can provide shared interpretation and manipulation rules within a practice whose readers have learned them. Retain that option for such a practice. Extending it across FPF would also require readers in other practices to acquire those conventions, even when another expression supports their task.

Compare these choices for the same content, operation and reader preparation. The selected rule accepts the cost of explaining local conventions and mapping compared expressions in exchange for allowing the expression suited to the work. It claims no universal advantage in learning time or performance.

**Effect on this pattern.** Section 4, item 1 and CC-NI.2 require guidance for an operation-bearing expression. Item 2 and CC-NI.3 require comparison when content is carried between expressions. The pump and timing cases in §5 show preservation and consequential loss. The heatmap case limits a coarsened expression's use. These moves keep interpretation and usable operations together. Subject Methods supply the reasoning or construction.

**Source roles and limits.** Macbeth's [paper-and-pencil analysis](https://doi.org/10.1093/philmat/nkr006) (2011, especially pp. 16-18 and 31-42) supplies the constructive argument from prepared expressions and shared parts.

Dutilh Novaes's *Formal Languages in Logic* (2012, §§3.2, 5.2 and 6.1) supplies the account of learned manipulation and interpretation. On p. 202 she argues that temporarily disregarding meaning is neither necessary nor sufficient for a cognitive gain.

These are conceptual grounds for the selected line and its reader-dependent limits. They provide neither a universal notation-design procedure nor a comparative estimate of learning or performance across all readers and notations.

**Reopen the choice** if interpretation and mapping satisfy this rule yet a needed claim or operation remains unrecoverable, or if a canonical-notation alternative supports the same work for the intended readers with less total preparation and explanation. Reconsider the affected requirement. An incorrectly prepared expression instead calls for the local repair or source return in §4.

### E.5.2:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **Constrains:** the expression of normative Core content, including project-local expressions used as carrying that content. The semantic-mapping requirement follows the comparison or intended reliance.
* **Uses:** A.6.3.RT when the intended operation depends on a change of representation language or reasoning medium, A.6.3.RT.OE for constructing an operative expression, and C.2.8 and C.37 when recovery or use must be assessed.
* **Conceptual prefixes:** E.10.P supplies the policy, registry and anchor requirements. E.5.2 keeps interpretation independent of tooling-specific expansion.
* **Subject reasoning and construction:** the pattern about the represented subject or the relevant Method governs the operation.
* **Method descriptions:** use `U.MethodDescription` only when A.3.2 applies: the episteme concerns one admitted Method and makes substantive claims about that way of doing.
* **Instantiates pillars:** P‑1, P‑2, P‑5

### E.5.2:End
