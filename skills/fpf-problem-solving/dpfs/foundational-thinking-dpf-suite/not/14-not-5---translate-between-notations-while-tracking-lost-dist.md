## NOT.5 - Translate between Notations while Tracking Lost Distinctions

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### NOT.5:1 - Problem frame

**Use this when** work must continue in another notation and you need to construct or repair the translation. A diagram may need a textual form, an ordered performance may need a compact score, or an expression may need a representation accepted by another reader or tool.

Start with the operation the receiving notation must support. Construct its expression from the source's interpreted parts and connections, then use it to obtain the needed answer. Find a pair of source expressions that the translation would make indistinguishable. If the work needs their difference, retain it, enrich the target or restrict the translation's use.

The first result is a usable translation with an answer-recovery procedure, or a demonstrated loss and a concrete way to repair it. Recovering a needed answer, reproducing the source expression and carrying a target edit back are different demands; choose the ones the work actually has.

The reader needs the two notations' formation and interpretation rules, supplied by NOT.2 and NOT.3 where they are missing. Subject knowledge establishes which consequences matter. The examples need directed connections, ordered sequences and elementary arithmetic.

Use an established translation directly when its conditions meet the need. NOT.4 handles transformations within one notation. NOT.6 handles continuing coordination of several representations and their changes. CMP.12 develops an effective translator and its execution-preservation argument when software must perform the translation. A.6.3.RT governs the underlying representation change and the claims it can preserve.

### NOT.5:2 - Problem

How can a change of notation make the next operation possible while keeping its answer connected to the source and exposing distinctions that can no longer be recovered?

Two source expressions can produce the same target expression. The target may still answer a useful question, but a reverse converter cannot infer which source was used from that target alone. A familiar default can conceal this loss. Conversely, requiring complete reversibility can exclude a cheap summary that is sufficient for the actual question.

A target edit adds another difficulty. There may be several source changes consistent with it, each preserving different features of the earlier source. Successful conversion in one direction does not choose among them.

### NOT.5:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Receiving operation and source detail | A simpler target can make one operation easier while removing distinctions needed by another. |
| Meaning and expression form | The same consequence can survive different layouts or spellings; some work also needs those forms retained. |
| Recovery and retained information | Keeping extra source information enables a return but adds storage, access and maintenance work. |
| Forward translation and backward change | A forward rule can determine the view without determining which source update the user intended. |
| Composition and accumulated loss | A locally usable conversion can remove information that a later conversion needs. |

### NOT.5:4 - Solution

**Choose the receiving operation → construct the translation → obtain and return an answer → expose collapsed distinctions → repair the needed loss → establish the required return.**

#### NOT.5:4.1 - Choose what must remain possible

Name the source notation, target notation and intended reader operation. Specify the source expressions admitted for this use and the context required to interpret them. A drawing may use position as meaning or only as layout; a spoken sequence may rely on a separately maintained beat. Carry the context that the question uses.

Decide what the recipient must return: a value, a construction, an explanation, a reconstructed expression or a proposed change. These demands can require different information. An answer expressed in target units or names needs a way back to the source question.

If a source choice is unresolved, preserve the alternatives or the unresolved status that matters to the question. A default introduced by the translation is an added decision. Accept it only when making that decision is part of the intended work and its basis is available.

#### NOT.5:4.2 - Construct target expressions from interpreted source structure

For every kind of source part used by the operation, give its target construction. Then give a rule for translating their composition. Preserve operand order, connections, scope and reference where the interpretation uses them.

Translate an expression by following its construction. For a diagram, this can mean declaring its nodes and translating each directed connection; for a sequence, translating each event while retaining its position or duration. Derive the target composite from those contributions. NOT.2 supplies the formation and reference rules; NOT.3 supplies the reading operations.

When a source ingredient has no target counterpart, choose an explicit treatment. Extend the target, carry an annotation, leave a visible unresolved part, or limit the admitted source expressions. Make this choice from the receiving operation. Silently deleting the ingredient or guessing its counterpart leaves the recipient unable to locate the loss.

For a mathematical interpretation, MATH.18 develops preservation and reflection of the required constructions and assertions. For a bijective change of mathematical representation, MATH.7 transports the operations through the inverse. Use those arguments when their conditions hold.

#### NOT.5:4.3 - Perform the receiving operation and recover its answer

Translate a small source expression, perform the intended operation in the target and interpret the result as an answer to the original question. Show the return explicitly. If the target gives a list of numbered nodes, say which source nodes those numbers refer to. If it supplies only a bound or a set of possible answers, retain that limitation on return.

Compare this result with what follows from the source under its declared interpretation. A mismatch locates a failed translation rule, a missing premise or a target operation that answers a different question. Repair the affected correspondence before relying on that answer.

A target-side answer can be spurious for the source if the target admits additional possibilities. Retain the source restriction or construct the needed reflection argument. For example, allowing arbitrary real values does not preserve a source question that admits only whole counts.

One successful expression establishes that case. A reusable translation needs an argument for its admitted family, such as a rule-by-rule construction over expressions. A separating example can refute a proposed general claim. Additional checking is warranted when its result can change the use or repair of the translation.

#### NOT.5:4.4 - Expose distinctions the target collapses

Look for different admitted source expressions with the same target expression. Ask whether the required operation gives different answers on them. If it does, the target alone cannot determine that answer: the translation has removed something the work needs. Section :5.2 makes this failure visible through cue order.

If every collapsed pair gives the same needed answer, the loss need not obstruct that question. For a claim about the whole admitted family, justify this independence over that family rather than infer it from a few pairs. MATH.2 supplies the mathematical construction through equivalence classes when that form is useful.

Include differences in assumptions, unfinished choices, references and reading context when they can change the answer. Equal visible strings can have different interpretations under different contexts. Conversely, two differently laid out diagrams can express the same directed structure when position has no role in their interpretation.

For several translation stages, follow the information needed by the final operation through each stage. A later, richer format cannot recover a distinction that an earlier stage removed unless another input supplies it.

#### NOT.5:4.5 - Repair the loss needed by the work

Choose the least burdensome repair that actually restores the operation. Retain the original expression when an occasional return is enough. Add the missing distinction to the target when the recipient must work independently. Otherwise, carry supplementary information with a defined recovery rule.

Call that supplementary information a *complement* when the target and the supplement together permit the required source recovery. State what it contains and how the return uses it. In :5.2 the position of a cue complements its count; in :5.3 a retained phase duration selects one backward update.

Keep the target and its supplement associated with the same source. If the target is edited, check whether the old supplement still permits the intended reconstruction. A stored position can become invalid after deleting an event. Locate that conflict instead of returning an invented original.

The repair may instead be an explicit narrower use. A cue count remains useful for inventory even when it cannot recover order. Retain that useful result and identify the additional contribution needed by an order-sensitive question.

#### NOT.5:4.6 - Establish the return that the work requires

For an unchanged round trip, translate and reconstruct the source at the required level: the same expression, the same interpreted structure or the same needed consequence. State which level is obtained. Recovering a directed graph up to layout does not recover where its boxes were drawn.

For a target edit, construct a backward update using the edited target and retained source information. Specify what remains fixed and what may change. In the ordinary single-view setting, check two properties: returning an unchanged view leaves the source unchanged; translating the updated source yields the requested view. These properties still leave a choice of update policy, worked in :5.3. They do not mean that all possible edits must be accepted.

When several views constrain a shared source, distinguish the user's changed requirement from values merely copied from the earlier view. NOT.6 handles their propagation and possible conflict. An unchanged value in a submitted view is not necessarily an instruction to freeze it.

If conversion performs effects such as asking a reader for missing information or changing external state, include the relevant behavior in the return claim. Recovering the same output value need not undo those effects. CMP.12 supplies the computational correspondence when an executable implementation is required.

Stop once the chosen operation and required return work within their stated conditions. Retain the translation rule, any supplement and the loss that changes later use where the recipient can find them. Reopen the affected construction when the receiving question, source interpretation or admitted edits change.

### NOT.5:5 - Archetypal Grounding

#### NOT.5:5.1 - Translate a dependency drawing without inventing geometric meaning

A drawing has named nodes A, B, C and D. An arrow X→Y means that Y takes X's result as its direct input. Box positions carry no meaning. In one drawing the arrows are A→B and B→C; D is isolated. The receiver must determine C's direct input using ordinary text.

Construct this textual notation:

```text
nodes: A, B, C, D
direct-input pairs (supplier, receiver): (A, B), (B, C)
```

The reading rule selects the pair whose receiver is C and returns its supplier, B. Translating back draws one node per declared name and one arrow per pair. This recovers the named directed structure, including isolated D. It need not recover the original layout.

A list of node names alone fails. The second drawing with A→B and A→C would give the same list but a different answer for C. Retaining the pairs repairs that loss. Retaining only pairs would create a different loss: isolated D would disappear from a reconstructed drawing.

Now suppose horizontal position additionally records a planned start time. The earlier translation still answers the direct-input question, but it cannot reconstruct that timing. Add a start-time value for each node if timing is now needed. That extension follows a changed interpretation or question; it is not evidence that the original drawing already specified times.

#### NOT.5:5.2 - Keep cue counts and recover order when needed

A toy score is a sequence of four equally spaced cue positions. D and T name two distinct sounds; there are no rests. Translate a score into the counts of D and T. Both `D T D D` and `D D T D` become `D:3, T:1`.

The target answers how many sounds are required: four. It cannot answer which sound occurs second. In the first score it is T; in the second it is D. No reverse choice made from the counts alone can recover both originals.

For this family with one T, retain its position as a supplement. Counts plus `T-position:2` reconstruct `D T D D`: place T at position 2 and fill the remaining positions with D. This permits both the count and the second-cue question. If the score may contain several T cues, retain their positions, check that they are distinct and within the score, and check that their number agrees with the count. If rests or unequal intervals become relevant, the chosen description needs further distinctions.

The counts remain a sufficient result for inventory. Reconstructing performance order requires the supplement; reconstructing tempo would require a time scale that this toy score never supplied.

#### NOT.5:5.3 - Choose what a backward update preserves

A plan describes two successive phases by `[A:3; B:5]`, in whole minutes. A summary notation shows only their total, 8. The recipient changes that total to 10. Several source plans fit: `[A:3; B:7]` and `[A:5; B:5]` both do. The new total does not choose between them.

Suppose the work requires A to remain fixed. Retain A's duration, 3, and reconstruct B as `new total - 3`. The requested total 10 gives `[A:3; B:7]`. Returning the unchanged total 8 recovers `[A:3; B:5]`; summing the updated plan returns 10. If instead B must remain fixed, the other update policy gives `[A:5; B:5]`.

Assume phase durations must be nonnegative. A requested total of 2 is incompatible with retaining A at 3. Report that conflict and obtain a changed requirement if the work allows one. Substituting B = -1 would preserve the sum while violating the admitted source plan.

### NOT.5:6 - Bias-Annotation

A familiar target can look more definite than its source. Preserve the source's unresolved choices and restrictions where they affect the receiving use. A translator's chosen default is additional content.

Conversely, fear of information loss can make every conversion retain a complete original. Start with the actual question. The cue inventory needs counts; an editable score needs more. Retain the extra information when it opens a needed operation.

### NOT.5:7 - Conformance Checklist

When the translation needs checking, use the questions relevant to its declared use.

- Can the recipient construct the target from the source parts, connections and required context?
- Can a target result be returned as an answer to the source question at the stated strength?
- Do two collapsed source cases require different answers for any promised operation?
- Does a necessary supplement have a usable recovery rule and remain associated with the right source?
- Is the round-trip claim about expressions, interpreted structures or selected consequences?
- For an edited target, is the backward policy explicit, including incompatible edits?
- Does a changed question or translation stage require a distinction already discarded?

### NOT.5:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Matching labels while losing their connections or scopes | Translate interpreted structure; the node/pair construction in :5.1 retains the required relation. |
| Recovering an arbitrary source and calling it the original | Exhibit the collapsed alternatives and retain the information needed to distinguish them. |
| Treating a useful summary as a complete substitute | Keep its successful use and add the missing information for the new question. |
| Returning a target answer outside the source's admitted cases | Restore the source restriction and the return argument. |
| Accepting a target edit by silently changing a protected source feature | Declare the backward policy and expose incompatible edits, as in :5.3. |
| Assuming a later format restores an earlier loss | Trace the needed distinction through the translation sequence or return to a retained source. |

### NOT.5:9 - Consequences

The recipient gains a usable expression and can tell which answers, reconstructions and changes it supports. A loss becomes a reason to choose a supplement, a richer notation or a narrower use instead of an unexplained conversion failure.

Retained information has an access and maintenance cost. A more restrictive reverse policy can protect a source feature while excluding useful edits. These trade-offs remain choices about the work; a round-trip law alone does not settle them.

### NOT.5:10 - Architectural Rationale

Translation changes the means through which an operation is performed. Its success therefore depends on both interpretation and the receiving operation. Two expressions may be interchangeable for counting and different for performing an ordered sequence.

The constructive loss test gives a local reason for a limit: when one target stands for two sources with different required answers, the target cannot by itself select the answer. Supplementary information repairs that failure only through a defined recovery operation.

Backward change is a further construction. Keeping one source feature fixed and changing another can realize the same target edit as a different policy. This is why two-way translation needs its own use conditions, and why continuing coordination of shared views belongs with NOT.6.

### NOT.5:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Foster, Matsuda and Voigtländer, [Three Complementary Approaches to Bidirectional Programming](https://janis-voigtlaender.eu/papers/ThreeComplementaryApproachesToBidirectionalProgramming.pdf), 2012, §§2–3 | Retain the historical construction of recovery from a view and a complement, and its treatment of partial backward updates. This grounds :4.5–4.6 without requiring complete invertibility of the forward view. Its pure-function setting does not cover every interactive conversion. |
| Xie, Schrijvers and Hu, [Effectful Lenses: There and Back with Different Monads](https://lirias.kuleuven.be/4268513), ICFP 2025, §§2.1–2.2 and 2.5 | Their effect-sensitive round-trip relations extend the pure setting. Use the consequence in :4.6: state which effects the return claim covers. Adopt no general promise that recovering values reverses external actions; implementing their formal framework is a separate computational construction. |
| Matsuda, Nguyen and Wang, [Lenses for Partially-Specified States](https://link.springer.com/chapter/10.1007/978-3-032-22723-2_2), ESOP 2026, §1 | Their shared-source problem shows why a copied value and an intended update constraint differ. Preserve that distinction in :4.6 and return multi-view coordination to NOT.6. The paper's stronger compositional results need its formal partial-state construction; this pattern does not infer them for arbitrary notations. |

**Choosing the translation method.** A bijection with transported operations is a strong choice when both notations express the same required information and a suitable inverse exists. It unnecessarily restricts a useful summary that deliberately omits detail. For that case, construct the receiving answer and retain only the information needed by the required return. A lens-style backward policy becomes useful when edits must propagate; it adds conditions and design choices that a one-way question need not carry. The pure view-and-complement account remains adequate for pure single-view conversions. Effects or interacting views select the stronger lines above when those difficulties actually occur.

This synthesis adapts those computational constructions to notation design by making the reader's operation determine the needed recovery. Reopen the chosen method when a previously harmless loss obstructs a new question, an edit violates its preserved feature, or conversion effects change the relied-on result.

### NOT.5:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| A.6.3.RT | Governs representation changes, preservation of the claimed content and disclosure of loss or narrowed use. |
| NOT.1–.3 | Supply the needed operations, expression construction and operative interpretations used by the translation. |
| NOT.4 | Supplies justified transformations within a notation that can be combined with translation. |
| MATH.2/.7/.18 | Supply quotient-based independence, reversible transport, and preservation/reflection through mathematical interpretations when those constructions apply. |
| C.29.1 | Supplies correspondence and result return when using a mathematical representation for the original problem. |
| CMP.12 | Constructs an effective interpreter or translator and the required relation between executions. |
| NOT.6 | Maintains complementary representations and propagates changes through their shared references. |
| NOT.7/.8 | Develop reading-effort redesign and temporal or embodied representations when the target has those demands. |

### NOT.5:End
