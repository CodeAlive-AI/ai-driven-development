## A.6.P.RI - Recover Agent-Relative References for Action

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.6.P.RI:1 - Problem frame

Use this pattern when an instruction or account depends on who says, reads or acts on it, and copying its words could change the intended object or action. “My left”, “our account”, “here”, “now” and an omitted actor can remain understandable to their originator while becoming ambiguous or misleading for another participant.

The subject is the interpretation and use of such an expression. Recover what it refers to at its source, decide what the receiving use must preserve, and connect the recipient to the relevant participant or position before deriving an action.

The first useful result is an interpretable account or instruction for the receiving work, or a specific missing reference or transfer condition. Sometimes it is enough to preserve an attributed report; sometimes another performer needs a different instruction to obtain the same result.

If the participants, relative expressions and intended action are already clear, proceed directly. Use this method where a difference of speaker, recipient, position, time or other reference condition could change what happens next.

### A.6.P.RI:2 - Problem

Two people can understand “left” and still move an object in opposite directions. Two systems can share the same description of a workplace while lacking the link that identifies which described participant each system is. A teacher can repeat a learner's first-person report while unintentionally presenting it as an observation the teacher made.

Making an account explicit helps, but does not settle how to use it after transfer. The recipient may be asked to preserve the same external destination, repeat a rule relative to their own body, or merely understand what the original speaker meant. These purposes can require different results even when everyone agrees on the participants and their orientations.

The difficulty is to preserve the relevant meaning without assuming that a copied expression retains its reference or that understanding an instruction supplies the means to perform it.

### A.6.P.RI:3 - Forces

| Need | Difficulty |
| --- | --- |
| Preserve the source meaning | A relative expression can acquire a new referent when copied. |
| Make the result usable by another participant | The recipient may occupy a different position or have different means of action. |
| Keep ordinary language useful | Expanding every pronoun creates work without resolving a live ambiguity. |
| Change an instruction deliberately | Preserving a result and repeating a relative rule are different tasks. |
| Relate experience and observation | The person experiencing a sensation and the person describing it have different access. |

### A.6.P.RI:4 - Solution

Recover the source reference, establish the receiving purpose, then derive only the interpretation or instruction that those conditions support.

#### A.6.P.RI:4.1 - Find the expression whose reference matters

Start with the actual statement and the work it is meant to support. Identify a word or omitted participant whose interpretation changes the result: for example, whose account, whose left side, which location or which time.

Use A.6.P to recover the relevant participants and relation. Read a quotation relative to its attributed speaker until the use calls for another interpretation. An imperative may leave the intended actor implicit; distinguish that actor from the person relaying the message.

Choose the smallest explicit account that removes the consequential ambiguity. A sentence such as “Dana means the cabinet to Dana's left” may suffice. If the source participant is unknown and the choice matters, retain that missing fact.

#### A.6.P.RI:4.2 - Recover the source conditions

Establish the source participant and only the conditions needed to interpret the expression. Direction can depend on orientation; “here” can depend on location; “now” on the time of utterance; “our account” on the organization and account relation.

C.2.1 supplies the distinction between the content and the rules used to designate its objects and interpret its expressions. Use the available records, communication setting or the participant's clarification to recover those values. A timestamp or sender field helps only if it identifies the relevant occurrence or speaker.

Keep unknown conditions visible. Where several interpretations permit the same safe continuation, that continuation may proceed without settling every detail. Where they lead to materially different actions, obtain the missing condition or give the conditional alternatives instead of silently selecting one.

#### A.6.P.RI:4.3 - Establish what the receiving use must preserve

Ask what the recipient is being asked to do with the source. For example:


- understand or report the original statement with its original referents;
- obtain the same external result through the recipient's own action; or
- apply the same relative rule afresh to the recipient.

Recover the actual purpose from the assignment or working agreement.

For example, “move the crate one metre to my left” can identify a direction from the speaker's orientation. A second performer preserving that displacement may need to move to their own right. “Repeat the movement to your own left” instead applies the relative rule to the second performer and can produce a different displacement.

Knowing both orientations does not choose between those tasks. If the transfer purpose is missing, state that missing condition before deriving an unconditional instruction.

#### A.6.P.RI:4.4 - Express the relation for the receiving use

Make the participants and preserved result recoverable in the form the recipient can use. This may be an ordinary sentence, a diagram or an instruction using an established coordinate convention. The relevant subject method supplies a spatial transformation, financial classification or other domain operation when one is needed.

Use A.6.3.RT for a change of representation scheme that keeps the EntityOfConcern. Extra information needed for the new expression remains an additional input. If C.2.1 identifies different EntitiesOfConcern, use A.6.4 for the invariant, visible loss and bounded receiving use. Changing the performer, notation or coordinates alone does not establish such a change.

For a report of experience, retain who experienced and expressed it. B.5.EA supports articulation and correction by that participant. Translating the report into an observer's vocabulary cannot by itself establish a bodily cause or give the observer the same experience.

#### A.6.P.RI:4.5 - Connect the recipient to the account and derive the action

Establish which described participant or position the receiving agent occupies for this use. A common description of all participants does not supply that link by itself. A person may recognize their part in the working situation. An artificial agent uses the identifying information and, where needed, sensed conditions supplied by its configuration.

Then interpret the account or derive the instruction under the purpose selected in §4.3. Recompute relative descriptions when necessary. When a message is only being quoted, preserve its original attribution rather than making the quoting recipient its speaker.

Before acting, retain the receiving work's requirements for authority, capability and resources. This method repairs the reference and transfer; the recipient performs the action using the relevant domain method.

#### A.6.P.RI:4.6 - Check the difference that could defeat the transfer

When a wrong reference could change the action, vary the relevant condition in a small safe case: another receiver, a changed orientation, a later time or a different organization. Derive the result from the recovered relation and compare it with the selected receiving purpose.

If the words stay the same but the result changes incorrectly, return to the source conditions or transfer purpose. If the instruction is correctly understood but cannot be performed, obtain the missing capability or support instead of continuing to repair its wording.

Stop when the account is sufficient for the intended use, or when a named unresolved condition prevents it. Retain a written reference or conversion rule only when later use needs it; an ordinary clarification can finish in the conversation.

### A.6.P.RI:5 - Archetypal Grounding

The following constructed cases show different things a transfer can preserve.

#### A.6.P.RI:5.1 - Preserve a displacement across orientations

A faces north and asks B to displace a crate one metre in the direction A calls left. B faces south. The assignment is to preserve the external displacement, and both headings are known.

The source direction is west. For B, facing south, west is right. The receiving instruction is therefore to move the crate one metre to B's right. If B turns east before acting, west becomes backward. Copying “left” would now send the crate north.

Change the assignment to “move the crate one metre toward your own left”. With B facing east, the correct displacement is now north. The known headings did not settle the instruction; the preservation condition did.

If B's heading is unavailable, “one metre west” can still be a complete instruction for a performer who can act in that frame. Otherwise the body-relative instruction remains unresolved. The method asks for the information needed by the chosen means, not for every possible position description.

A mobile robot receiving the same external displacement needs a usable relation between the shared frame and its action representation. Obtaining that relation and the capability to perform the movement is a separate technical task. The example does not prescribe its learning or control architecture.

#### A.6.P.RI:5.2 - Preserve the speaker when relaying a request

Dana writes to an assistant: “Put the comparison in my project folder.” The assistant sends the request to another worker. Replacing “my” with the new worker's own project folder would change the destination.

The receiving purpose preserves Dana's destination. The assistant identifies Dana's project folder through the available project information and relays: “Put the comparison in Dana's project folder,” with a usable reference to it. The worker uses its own authorized means of access; Dana's request does not grant access that the worker lacks.

If the next assignment is instead “each worker puts a copy in its own project folder”, the rule is applied relative to each worker. That is a changed distribution task, not another wording of the original destination.

Where the workspace contains several Dana projects and the intended one cannot be recovered, the useful result is a question selecting the project. Producing another fluent paraphrase leaves the same action unresolved.

#### A.6.P.RI:5.3 - Relate a dancer's report to an observer's account

A dancer facing the teacher says, “I feel a pull along my left side when I turn in this figure.” The teacher sees movement on the teacher's right. Both accounts can concern the dancer's left side even though the spatial words differ.

The first receiving task is to understand the report. Recover the dancer as the experiencing participant, the dancer's orientation and the turn being described. The teacher can say, “You report a pull along your left side during that turn,” and ask the dancer to correct the expression if needed.

A second task is to decide how to change the movement. The report and external observation can inform that inquiry, but do not themselves identify the tissue, force, cause or suitable exercise. The relevant bodily practice must supply the further operation.

In this figure, maintaining balance during the turn contributes to performing the figure; regulating bodily effort helps enact that balance, while the steps keep their required rhythm. Changing whose account is used can make another question accessible; it does not by itself identify which constituent needs development. B.1.5.EW supplies that vertical inquiry, and B.5.EA helps articulate a distinction the dancer cannot yet express.

### A.6.P.RI:6 - Bias-Annotation

A translator can assume that the recipient occupies the same position as the source. A shared diagram or vocabulary makes this especially easy. Test the particular changed condition on which the action depends.

An observer can also replace the performer's report with an interpretation that is easier to describe externally. Keep the report open to correction by its source and give the additional interpretation its own basis.

### A.6.P.RI:7 - Conformance Checklist

For a consequential interpretation or transfer, ask:

- Which expression depends on its speaker, user or situation?
- Are the source participant and action-changing reference conditions recoverable?
- What does the receiving use preserve?
- Can the recipient identify its own relevant position in the account?
- Does the derived action still satisfy that purpose when the consequential condition changes?
- Are missing information, authority, capability and support distinguished?
- Does any actual change of EntityOfConcern use A.6.4 rather than being assumed from new notation?

Use the questions needed for the receiving decision. An already clear instruction needs no additional record.

### A.6.P.RI:8 - Common Anti-Patterns and How to Avoid Them

**Copying a relative direction.** The source and recipient face different ways, but both act on the same word. Recover the source direction and the intended receiving result before deriving the recipient's instruction.

**Replacing every “I” with the recipient.** A quotation or relayed instruction loses its original speaker. Preserve the source attribution unless the new task deliberately applies a rule to another participant.

**Treating shared facts as self-identification.** Several systems receive the same participant description, but none has been linked to its own entry. Obtain that link from the actual working configuration.

**Turning a felt report into a bodily cause.** “The dancer reports tension here” becomes “this tissue causes the failure”. Preserve the report and use the appropriate subject method to examine the causal claim.

### A.6.P.RI:9 - Consequences

The same source account can support a usable receiving instruction without losing who or what it concerned. A changed position or participant becomes a condition to handle explicitly where it matters.

The method can expose missing information and thereby postpone an action that previously appeared clear. It does not create the unavailable information, movement capability or authority. Where ordinary shared understanding already settles the reference, further formalization would add cost without improving the action.

### A.6.P.RI:10 - Architectural Rationale

Relational precision restoration recovers missing participants. Agent-relative use additionally requires a link between the receiving agent and the described participants, together with a decision about what the transfer preserves. Neither a complete participant list nor a change of notation supplies these by itself.

The construction therefore combines the source interpretation, receiving purpose and recipient's position. Representation change and EntityOfConcern retargeting retain their existing conditions. Domain operations compute the actual conversion or classification; this method exposes the premises they need and returns their result to the receiving action.

The method applies when the receiving performer can be identified in the account and the relevant reference conditions can be recovered. Human first-person experience remains available through the experiencing person's account and correction. An artificial agent uses the identification, representations and signals its configuration supplies.

### A.6.P.RI:11 - SoTA-Echoing

The practice question is how an explicit shared account becomes usable by an agent whose position differs from its source. The method recovers the source reference, chooses what the receiving use preserves and connects the recipient to the account. Its serious alternative is to make all participants explicit and assume that this alone determines the receiving instruction.

**Adapt the distinction between common descriptions and agent-relative use.** [Partridge and colleagues, Ontology then Agentology (2018)](https://biblio.ugent.be/publication/8547739), §§2–4 and Figure 2, distinguish the reusable form of an account from its agent-dependent content and add a link identifying the system itself. This supports the self-identification required in §§4.2 and 4.5. It is a conceptual source, not evidence about human learning or current robot performance.

The crate case shows why this pattern also states the preservation condition in §4.3. Even correct source interpretation and self-identification leave two different possible tasks: preserve the displacement or repeat the relative movement. This is the pattern's methodological synthesis, rather than a result attributed to that paper.

**Reuse representation and retargeting methods under their own conditions.** A.6.3.RT is sufficient when the receiving use needs only a representation change under already available bindings. A.6.4 is needed when the independently identified EntitiesOfConcern differ.

Use the simpler direct clarification when it already settles the action. Reopen the construction when it cannot determine which reference changed, when the recipient cannot bind itself to the supplied account, or when the intended preservation condition fails under changed use. Technical conversion and learning methods require their own current subject evidence.

### A.6.P.RI:12 - Relations

- **A.6.P** restores the participants and relations hidden by an underspecified claim.
- **C.2.1** supplies designation, interpretation and EntityOfConcern distinctions.
- **A.6.3.RT** changes representation while preserving the EntityOfConcern; **A.6.4** governs bounded use across a real change of that object.
- **B.5.EA** articulates a distinction from experience while preserving the source participant's correction.
- **B.1.5.EW** recovers how constituent actions enact the encompassing work; a change of reference position is not itself a change of Method level.
- **A.15.10** recovers a transferred or interrupted continuation. Use this method when an unresolved agent-relative expression prevents that continuation.

### A.6.P.RI:End
