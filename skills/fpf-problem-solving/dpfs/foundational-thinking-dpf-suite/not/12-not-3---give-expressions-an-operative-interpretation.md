## NOT.3 - Give Expressions an Operative Interpretation

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### NOT.3:1 - Problem frame

**Use this when** a notation can form expressions, but its users lack a clear way to obtain the consequence those expressions are supposed to support. A legend may explain the signs while leaving the reader to invent how to combine, inspect or manipulate them.

Start with one question an expression should help answer. Give its relevant parts an interpretation, supply the operations needed to read them together, and follow that reading to a result. A useful first result can also be a located gap: a value, interpretation rule or reader capability that must be supplied before the question can be answered.

An **operative interpretation** here connects what an expression stands for with what a prepared reader can do to obtain a needed consequence from it. Reading can involve calculation, inspection of a diagram, rule-based manipulation or enactment. The reader may be a person or a computational agent; the applicable operations and preparation depend on that reader.

The designer needs the intended subject account and the operations on which the reading depends. The first example uses elementary Boolean reasoning, explained in the case; the temporal example uses addition and interval comparison. A machine implementation is a further construction when required.

Use an existing interpretation directly when it already supplies the needed reading. A.6.3.RT.OE addresses building an operative expression under an available scheme. Use the present method to develop or repair the scheme's interpretation and its reading operations. NOT.2 addresses missing grouping, binding and connection rules.

### NOT.3:2 - Problem

How can a notation's interpretation give its intended reader a usable way to obtain a consequence, while keeping the conditions of that consequence recoverable?

Assigning names to marks can leave their combined use unexplained. Assigning a mathematical meaning can specify an answer without providing a way to obtain it. A familiar reader may bridge either gap from experience while a new reader cannot tell which operation is missing.

### NOT.3:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Meaning and obtaining | An expression can denote a result that the available reader cannot compute or recognize. |
| Local rules and whole expression | A reading of each component must account for their composition and context. |
| Useful tacit skill and recoverable preparation | A trained perceptual or manipulative operation can be efficient but unavailable to another reader. |
| Several reading routes and one required consequence | Different routes can expose different structure or cost different effort while agreeing on the intended answer. |
| Represented condition and actual occurrence | A model can imply a result without establishing that the described situation obtained. |

### NOT.3:4 - Solution

**Choose the consequence → interpret the expression's parts and composition → supply the reading operations → perform a case → test a consequential change → retain the usable reading and its conditions.**

#### NOT.3:4.1 - Choose what the reading must produce

State the question, the expression and the information available outside it. Identify what would count as a useful result. Examples include the value of a formula, a permitted next action, whether two intervals overlap, or a consequence of a diagram's relations.

Distinguish obtaining the expressed answer from establishing its use in the subject matter. Reading an interval from a schedule can answer what is planned; observing what happened needs the corresponding observation. The interpretation should identify which question it answers.

Specify the reader's available operations. It may be reasonable to presuppose arithmetic, following a visible connection or a trained movement. Expose a less familiar operation if the intended reader could otherwise mistake its absence for a defect in the expression. A short prerequisite explanation can suffice; a capability that requires practice belongs in the appropriate learning method.

#### NOT.3:4.2 - Interpret components, composition and context

For the parts used by the question, specify what they denote or instruct and how their combination is interpreted. Include grouping and reference rules from NOT.2. An arrow may supply an input to an operation, express a precedence condition or prescribe a movement; choose its role in this scheme before deriving a consequence.

Give the interpretation of a compound expression in terms that permit its use. For a compositional mathematical scheme, interpret the parts and then apply the corresponding operation to their interpretations. MATH.5 and MATH.18 develop that construction and its preservation questions. When context contributes to interpretation, include the relevant context among the inputs rather than assigning a context-free meaning that the notation does not support.

If the expression admits alternatives or has an unresolved part, specify what can still be concluded. A reader may be able to obtain a common consequence across the alternatives. Another question may have to wait for the missing information. Preserve that distinction instead of silently completing the expression.

#### NOT.3:4.3 - Construct the reading operations

Show how the intended reader moves from the expression and available inputs to the result. For each indispensable step, identify what is inspected or changed and how the next step uses what was obtained. The procedure may reuse an established method rather than explain that method again.

For a formula, this can mean resolving a parameter, evaluating selected subexpressions and combining their values. For a diagram, it can mean identifying a boundary, following the admitted connections and applying the corresponding inference. For a performed notation, it can mean recognizing a cue and executing a learned action. Choose operations that the reader can actually perform under the stated conditions.

Keep the reasoning behind a manipulation available at the level required by the work. A rule may be applied fluently after training, while changing the rule requires understanding what it preserves. NOT.4 develops expression transformations; B.5.RC and B.5.RA help recover an unfamiliar construction or argument when that is the missing contribution.

If a mathematical interpretation leaves the required obtaining procedure unavailable, name that remaining problem. CMP.12 constructs effective evaluation when the expression's operations admit it; other CMP methods can help construct the needed algorithm. Denotation alone does not establish computability or affordability. A human reading or trained perceptual operation also needs its actual capability and access conditions.

#### NOT.3:4.4 - Perform the reading and locate where it depends on additional knowledge

Take an expression whose relevant parts and input values are supplied. Carry the reading through to its stated result. At a step that cannot be performed, distinguish a missing input, an undefined interpretation and an unavailable operation. These lead to different repairs.

Compare the result with the intended consequence under the subject account. Repair an interpretation rule when it yields a different answer. Repair the reader preparation or access when the rule is usable in principle but cannot be carried out under the current conditions. If the subject account itself leaves the consequence unresolved, return that question to the corresponding mathematical, physical, computational or other practice.

When more than one reading route is offered, perform the routes on a case that could expose a difference. Establish the agreement needed by the use, or explain why the routes answer different questions. A route that only returns a final value may lose the dependency structure another operation needs.

#### NOT.3:4.5 - Change one condition that matters to the interpretation

Change a value, grouping, reference, context or intended question that could alter the result. Use the same rules to recover the new answer, or locate the rule that must change. The challenge should test the chosen interpretation rather than introduce an unrelated subject problem.

For a formal family, a general argument can establish that the reading operations implement the interpretation across that family. MATH.18 supplies interpretation-preservation questions; CMP.12 supplies executable translation and evaluation. For human or embodied use, C.2.8 can characterize what the prepared reader recovers and distinguish an expert walkthrough from observed use. Choose further checking when it can change the interpretation or permitted reliance.

#### NOT.3:4.6 - Keep the operative reading available to its users

Provide the interpretation, the indispensable reading operations and their prerequisites where the intended user can find them. A legend, one worked reading and a reference to a known method may be enough.

Stop when the required consequence can be obtained at the declared scope, or when the missing contribution and the next way to obtain it are clear. Retain a slower explanatory route alongside a fluent route when users need to learn, justify or change the operation. A further notation redesign belongs to NOT.7 if the reading works but imposes avoidable difficulty.

### NOT.3:5 - Archetypal Grounding

#### NOT.3:5.1 - Turn a condition diagram into a reading procedure

A team designs a notation for combinations of conditions. Labels `P`, `Q` and `R` refer to conditions with supplied truth values. An `ALL` enclosure holds only when every enclosed condition holds. An `ANY` enclosure holds when at least one enclosed condition holds. The conditions are stable while the expression is read, and reading them does not change their values.

Consider:

```text
ALL {
  P
  ANY { Q R }
}
```

The legend defines the operators, but a new reader still needs a way to apply them to a nested expression. Supply this reading procedure: resolve each condition label from the given inputs; evaluate the innermost enclosure; replace it by its Boolean result; continue outward.

With `P = true`, `Q = false` and `R = true`, the inner enclosure is true because R is true. The outer enclosure combines true with true, so the whole condition holds. This result concerns the supplied conditions. Establishing their truth in an actual project is separate work.

A second route examines only values that can still change the answer. For `ALL`, one false child settles the result as false; for `ANY`, one true child settles it as true. With the same inputs, the reader checks P, then Q and R, and obtains the same result. If P changes to false, the outer `ALL` is false without inspecting Q or R. The stable, side-effect-free condition premise makes this omitted reading legitimate.

Now change the inner operator from `ANY` to `ALL` while keeping the original inputs. The inner result becomes false and therefore the outer result becomes false. The reader has followed the changed expression through the same interpretation rules. Replacing a label without resolving its value would leave a different gap: the input is missing, not the nesting rule.

The two reading routes expose a choice about obtaining the answer. They agree on these Boolean results; one shows every intermediate value, while the other can avoid work. A user who also needs all intermediate values should retain the first route or extend the second to produce them.

With P false and the values of Q and R not supplied, the whole expression is still false. A request for every intermediate value still needs those missing inputs.

#### NOT.3:5.2 - Recover what an interval notation means before using it

A signal plan contains the pair `(2, 4)`. The notation designer must say whether the second component is an ending time or a duration. Under the first interpretation, the planned active interval is `[2, 4)`; under the second it is `[2, 6)`. Half-open intervals include their start and exclude their end.

Choose `(start, duration)`. Give the reader two operations: add duration to start to obtain the end, then test whether a queried time is at least the start and less than the end. At time 5 the planned signal is active, because `2 <= 5 < 6`. If duration changes from 4 to 2, the new end is 4, and the signal is inactive at time 5.

The pair's two numeric entries did not establish this interpretation by themselves. The chosen convention and the comparison procedure make the answer obtainable. A timeline can support another reading by locating the queried point against a drawn interval, provided its scale and endpoints carry the same values.

This answers a question about the plan. To determine whether a device actually emitted the signal at time 5, obtain the relevant observation and the conditions relating it to emission. The notation can retain that observation or a model of the device, but the planned interval alone supplies neither.

### NOT.3:6 - Bias-Annotation

Expert familiarity can conceal a reading step. A fluent reader may move from a symbol to a consequence without noticing the convention or skill used. Recover that step when it changes what another reader needs to know or be able to do.

The opposite bias treats every interpretation as a complete algorithm awaiting transcription into code. A mathematical meaning can leave an obtaining problem unsolved, and a practiced perceptual operation can lack a suitable machine realization. Keep these different contributions visible when allocating work among agents.

### NOT.3:7 - Conformance Checklist

When the interpretation needs checking, ask the following questions at the scope of the proposed use.

- Is the consequence to be obtained distinguishable from the subject claims on which it depends?
- Do the used parts, their composition and relevant context have an interpretation?
- Can the intended reader identify and perform the indispensable reading operations, or locate the missing input or capability?
- Does the worked reading obtain the stated result without an unexplained inference supplied only by the author?
- Does a consequential change lead to the corresponding new result or to a located interpretation question?
- If several routes are offered, is their agreement or difference established for the observations the user needs?

### NOT.3:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A legend names signs but leaves composition unused | Read a compound expression through to its result. The condition example needs a rule for proceeding through nested enclosures. |
| Treating a denotation as an available computation | Identify the operation that obtains the denoted answer and its conditions, or return the missing algorithmic problem. |
| Hiding a learned reading skill | Explain the operation or name the preparation needed to perform it. Test access and capability where uncertainty changes the next move. |
| Reusing a shortened reading after its premise changes | Recheck which observations it preserves. Short-circuit reading in the first case presupposes stable conditions without reading effects. |
| Reading a plan as a report of events | Obtain the observations needed for the event claim; the signal schedule alone states what is planned. |

### NOT.3:9 - Consequences

The notation acquires a path from expression to a useful consequence. Users can distinguish a missing input from a missing rule or capability and can allocate those contributions among people and computational agents.

Providing an operative interpretation can require more work than defining symbols. Several reading routes may be worth retaining because users need different intermediate results or have different preparation. A successfully performed small case supports that use; wider claims need the corresponding argument or experience.

### NOT.3:10 - Architectural Rationale

The interpretation connects representation with work. It identifies the meaning relevant to a question and the operations through which a reader can obtain a consequence.

The separation between interpretation and obtaining preserves generality. MATH.18 can establish a mathematical interpretation. CMP.12 can construct an effective evaluator under its algorithmic conditions. NOT.3 asks what reading the notation is to support and supplies the missing connection for its intended user. It can therefore include a manual or embodied route.

Several useful readings may expose the same structure differently. Choosing among them can change the work needed to recover an answer or the intermediate structure made available. This is one reason to design notations around operations, rather than treating them only as shorter ways to write conclusions.

### NOT.3:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Macbeth, [Seeing How It Goes: Paper-and-Pencil Reasoning in Mathematical Practice](https://doi.org/10.1093/philmat/nkr006), 2011, opening discussion and treatment of Peirce's alpha graphs, historical foundation | Adopt the distinction between recording an answer and working through signs to obtain or expose reasoning. Her different readings of a graph motivate retaining useful reading routes. Their mathematical case does not establish equal accessibility to every reader. |
| Dutilh Novaes, [Formal Languages in Logic](https://doi.org/10.1017/CBO9781139108010), 2012, §5.2, historical foundation | Adapt attention to the operations people perform with external inscriptions and the preparation those operations require. Treat the cited human studies at their studied scope; no general learning gain or cross-agent equivalence follows here. |
| Piedeleu and Zanasi, [An Introduction to String Diagrams for Computer Scientists](https://arxiv.org/abs/2305.08768), mathematical syntax/semantics account | Use compositional interpretation when the notation and target operations admit it: the whole interpretation follows the specified combination of parts. This offers a formal alternative to a merely demonstrated reading. The required obtaining procedure and the reader's access still depend on the intended use. |

**Choice between approaches.** If a known formal interpretation and an available evaluator already answer the question, use them; a new reading procedure adds no value. When the difficulty is obtaining the consequence from a new notation, the present method supplies that route and locates its tacit requirements. A trained reading can be useful before a full formal calculus exists; a broader preservation or automation claim can justify constructing that calculus through the mathematical and computational suppliers.

### NOT.3:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1/.2 | Supply the required operations and the formation, reference and connection rules. |
| A.6.3.RT.OE | Constructs an operative expression when the scheme and reading operations are already available. |
| MATH.5 and MATH.18 | Construct and compare mathematical interpretations, including consequences preserved through composition. |
| CMP.12 | Constructs an effective interpreter or meaning-preserving translation when the obtaining problem is algorithmic. |
| B.5.RC and B.5.RA | Recover the construction or argument needed when a reading contains an unfamiliar step. |
| NOT.4 and NOT.5 | Develop use-preserving transformations and translations once the relevant interpretation is available. |
| NOT.7 and NOT.8 | Develop an easier reading or a temporal or embodied notation where the available route remains difficult. |
| C.2.8 | Characterizes recoverable structure under the reader's preparation, access and effort conditions. |
| C.29 and B.5.MPC | Connect an interpreted mathematical consequence with its physical subject and the work needed to use it. |

### NOT.3:End
