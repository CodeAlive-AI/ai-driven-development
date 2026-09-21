## B.5.RA - Recover an Argument for Its Next Use

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative unless marked informative

### B.5.RA:1 - Problem frame

Use this pattern when you have an argument or a reported result but cannot yet understand why it supports the conclusion you want to use. You may need to apply the result, criticize it, explain its decisive step or decide which part survives a proposed change.

The **argument** is the reasoning that connects premises to a conclusion. It may use a mathematical construction, a calculation or a subject inference from observations. The relevant practice supplies the permitted inference and the grounds for its premises.

**First useful move:** state what you want to do with the conclusion, then recover the main reason offered for it. Follow the needed intermediate claims until you can explain the decisive transition and its conditions.

The reader needs the subject preparation assumed by the source, or access to the missing explanation. Use an adequately understood result directly when its conditions already fit the task. A request to understand the argument can stop before re-proving every established result it uses. A separate obligation to validate the entire proof or underlying observations selects the corresponding checking work.

### B.5.RA:2 - Problem

An argument can be present without being usable by its reader. A reader may recognize each term yet miss why a lemma was introduced, where two premises must be used together, or how a local calculation establishes the general conclusion.

Reading each sentence fluently or checking isolated inferences leaves the overall method uncertain. Reading only the overview can hide a decisive unsupported transition. Either failure prevents useful transfer: the practitioner cannot tell what to use, which condition matters or where to ask for help.

The useful result is enough recovered reasoning to perform the intended use, or a localized gap whose resolution would make that use possible. This may be a conditional conclusion when a needed premise remains open.

### B.5.RA:3 - Forces

| Force | Tension |
| --- | --- |
| Local inference and overall method | Individual transitions can be understood while the purpose of a construction or the route to the conclusion remains obscure. |
| Understanding and checking | Understanding may reuse established results; validating a whole argument can require additional work under a different question. |
| Useful compression and hidden dependence | A lemma can make a long argument manageable, but the reader must know what it supplies and which conditions it uses. |
| Conditional result and unresolved premise | Useful consequences may follow before every premise is established, provided the next use preserves the condition. |
| Source recovery and new reasoning | Repairing a gap can open a valid use, while attribution must distinguish the supplied argument from the reader's addition. |

### B.5.RA:4 - Solution

Recover the reasoning at both the level of its main contributions and the transitions needed for the next use. Move between these levels when a local step changes your understanding of the whole argument.

#### B.5.RA:4.1 - State the use and read the claim

Name what the result would let you do: calculate a quantity, choose between alternatives, criticize a conclusion, adapt an argument or explain it to someone else. This determines how far recovery needs to go.

Read the conclusion with its objects, domain and conditions. In a mathematical statement, recover the quantifiers: which objects are arbitrary, which may be chosen, and on what a chosen object may depend. In an empirical argument, recover what observations and inference support which population, conditions or phenomenon.

Locate the source's definitions when a word or symbol admits different readings that would change this use. If a formal statement accompanies an informal one, compare the part of their meanings on which the intended application depends. For example, whether zero is allowed among “natural numbers” can change the statement.

#### B.5.RA:4.2 - Recover the main reason

Read for the difficulty the argument overcomes and the contribution that overcomes it. Ask why a construction, lemma, decomposition or comparison appears where it does.

Express the main reason in a short explanation: what is established first, what that makes possible, and how the remaining step reaches the conclusion. This may involve a reduction to an easier problem, an invariant, an exhaustive case distinction or another subject method. Use the method actually present in the source.

The first explanation is a working interpretation. Check it against the decisive steps. If it cannot explain why those steps are needed, revise it rather than retaining an attractive summary unrelated to the argument.

#### B.5.RA:4.3 - Recover the dependencies of the conclusion

Work backward from the conclusion through the claims or constructions it uses. At each needed transition, identify its premises, the inference or operation, and the result.

Keep jointly needed premises together. Preserve an independently sufficient alternative as a separate way to reach the conclusion. Track a shared premise wherever a later step uses it; repeated uses of one assumption do not provide independent support for that assumption.

Distinguish a premise supplied for the argument, a result established earlier and a temporary assumption used inside a subargument. Recover the point at which a temporary assumption is discharged and what then follows. If this logical form is unfamiliar, obtain the relevant explanation before treating the subargument's assumption as an established fact.

Use established results at the level needed for the task. If the question concerns what a lemma permits, its statement and conditions may suffice. If the question concerns how to alter the lemma's proof, recover its internal reasoning.

#### B.5.RA:4.4 - Explain the transition that is still missing

For a transition you cannot follow, recover the relevant definition, rule, earlier result or construction. Apply it to the participants at that transition. Say why these premises license this result and which condition is doing the work.

A useful self-explanation supplies this relation. “I understand this line” reports confidence; a paraphrase repeats the claim. Neither supplies the omitted inference when that is the difficulty.

Work a small instance when it helps reveal the operation or dependence. Then return to the stated scope: the instance may illustrate a general step, while the general conclusion still depends on the argument for all cases in its domain.

If the source's resources do not close the gap, ask for the missing step with its premises and desired result. A proposed repair is new reasoning until it is justified. Keep the consequence conditional when a premise remains unresolved and conditional use is sufficient.

Where the missing step constructs an auxiliary object, use B.5.RC. Where it makes a statistical, causal or other subject inference, use that subject's method and conditions.

#### B.5.RA:4.5 - Use the recovered reasoning and stop at a useful result

Perform the use named in :4.1. Apply the result under its conditions, explain the decisive step, identify a consequential criticism, or name what must be recovered before the use is possible.

Make the conclusion no stronger than the recovered reasoning supports. If recovering the argument reveals an open premise, state its effect on the intended use. When several sufficient arguments are available, an unresolved branch may be bypassed through a branch whose premises and reasoning are adequate.

If a premise or requested conclusion changes, use B.5.RR to follow the affected reasoning and derive what still follows. The recovered dependencies supply the starting point for that work. An unchanged, adequately supported part can be reused.

C.11.DUA governs whether more checking or information is worth obtaining for this decision. Understanding an argument, verifying its correctness and establishing its real-world premises can require different work. Select further work from the unresolved question. When the work is divided among agents, give the next contributor the premises at the missing transition, the result needed there and the intended use. On return, connect the supplied reasoning to the argument's main reason. Use the explanation or working notation that makes the continuation possible.

### B.5.RA:5 - Archetypal Grounding

#### B.5.RA:5.1 - Understanding why the sum of odd numbers is a square

Consider this compressed argument: “The sum of the first n positive odd numbers is n²: the sum and the square start at zero, and both increase by 2n+1 when n increases by one.” The statement concerns every nonnegative integer n. A reader recognizes the formula but needs to explain the steps compressed in that reason.

Write S(0)=0 and S(n+1)=S(n)+(2n+1). The main reason is that both the sum and the square start at zero and grow by the same amount when n increases by one. The algebraic identity (n+1)²−n²=2n+1 supplies that connection.

Recover the general transition. Assuming S(n)=n² for an arbitrary nonnegative integer n gives:

S(n+1)=S(n)+2n+1=n²+2n+1=(n+1)².

The temporary assumption is the induction hypothesis. It supports the successor step. Together with S(0)=0, that step establishes the statement for every nonnegative integer by induction.

For n=3, the sum is 1+3+5=9. Adding the next odd number, 7, gives 16. This instance makes the equal-increment operation visible. The argument's reach comes from the arbitrary n, the base value and the induction rule.

A square drawing gives another way to follow the increment: grow an n-by-n square with a row of n cells and a column of n+1 cells. That adds 2n+1 cells. The drawing and algebra expose the same increment under the counting interpretation.

The reader can now explain the role of the initial value and successor step. If the next task instead asks for the sum of n odd terms beginning at 3, the changed range opens a revision: use the established sum through the (n+1)th odd number and remove the first term, giving S(n+1)−1=n²+2n. For four terms, 3+5+7+9=24. The reusable contribution is the recovered relation between range, initial value and increment.

If the original question asked only for 1+3+5, direct addition would already supply the result. Recovering the general argument earns its effort when explanation, general use or revision needs it.

#### B.5.RA:5.2 - Understanding a drawing-recovery argument

A team needs to open an archived engineering drawing for reuse. Someone argues that the drawing is recoverable because three backup copies exist.

Recover the method behind that conclusion. For the encrypted-backup route, the needed contributions are readable stored data, an available way to decrypt it and a decoder for the drawing format. Their joint use produces a readable drawing. Having more copies addresses loss of stored data, while all three may still share one decryption key.

Suppose the key is unavailable. The backup count leaves the decoding route incomplete. The next useful question is whether the key can be recovered or another usable copy obtained. The recovered argument identifies that missing prerequisite.

Now suppose a separate plaintext copy in a readable format is available. That gives a different route to the drawing and permits the team to continue without recovering the encryption key for this use. The original encrypted route remains conditional.

The result is a usable recovery choice or a focused request for a missing contribution. A later claim that the opened drawing describes the present equipment requires its own comparison; the file-opening argument answers the immediate recovery question.

### B.5.RA:6 - Bias-Annotation

Familiar vocabulary and a correct-looking calculation can create confidence before the reasoning has been recovered. Conversely, checking every line can consume attention while leaving the role of a lemma unexplained. Use the local transition and the main reason together.

AI-generated formal proofs make the distinction consequential: a checked formal derivation supplies a result under its formal definitions, while the intended statement and the explanatory structure needed for reuse may still need recovery. The relevant comparison is the one that can change the contemplated use.

### B.5.RA:7 - Conformance Checklist

For the argument and use being recovered:

1. The intended use and the conclusion's domain and conditions are recoverable.
2. The explanation states the main reason for the result and connects it to the decisive steps.
3. The needed transitions identify their premises, inference or operation and result.
4. Joint premises, sufficient alternatives, shared assumptions and temporary assumptions retain their different roles.
5. The reader can perform the intended use or identify the missing transition or premise that prevents it.
6. A small instance supports the explanation at its stated scope; a general conclusion has its corresponding reasoning.
7. Further checking is selected for an unresolved question, and adequately supported parts remain reusable.

These are questions about the recovered reasoning. Their answers may already be evident in the working explanation or application.

### B.5.RA:8 - Common Anti-Patterns and How to Avoid Them

| Failure in the working situation | Repair |
| --- | --- |
| Paraphrasing successive claims while the inference remains missing | Apply the relevant definition, rule or earlier result to the transition's actual premises. |
| Checking local steps while failing to explain why a lemma or construction appears | Recover the difficulty that contribution resolves and connect it to the conclusion. |
| Treating several uses of one premise as several independent grounds | Keep the common prerequisite visible and examine its role in the needed branches. |
| Promoting a temporary assumption to an established premise | Recover the subargument and the conclusion obtained when that assumption is discharged. |
| Using one example to claim that the general statement has been proved | Recover the argument that covers the stated domain; retain the example as an illustration of it. |
| Demanding a complete reproof when the task only needs an established result under its stated conditions | Use that result at the needed level; open its internals when the new question requires them. |

### B.5.RA:9 - Consequences

A recovered argument can support application, explanation, criticism and later revision. Work can be divided around meaningful intermediate results, and a request for help can name the transition that remains obscure.

The method can reveal that the source's conclusion exceeds its support or that the reader lacks a prerequisite. It cannot supply every missing subject method. Its economical stopping points are a sufficient argument for the use, a useful conditional conclusion or a localized gap.

### B.5.RA:10 - Architectural Rationale

A source orders its text for exposition; the argument relates premises, intermediate contributions and conclusions. Understanding therefore needs more than following the paragraph order. Backward dependency recovery identifies what the desired conclusion uses, while recovery of the main reason explains why those contributions were chosen.

Local and overall understanding constrain each other. In :5.1, the equal-increment idea explains the role of the recurrence, and the induction step establishes the general result. In :5.2, the recovery route explains why the key and format matter, and their availability determines which route can be used. A fluent summary that cannot support these transitions is insufficient for the intended use.

This common method concerns recovery of reasoning already offered for a result. B.5 coordinates the broader inquiry; B.5.RC recovers an auxiliary construction; a subject method supplies an unfamiliar inference. To explain the result to someone else, select the reasoning and representation that make their intended use possible. C.2.8 helps characterize what that recipient can extract under stated preparation and access.

Recovery also makes revision possible. The changed premise can be followed through the contributions that use it, while independent arguments remain available. Revision has its own task and result; recovering the original argument supplies the dependency information it needs.

### B.5.RA:11 - SoTA-Echoing

**Local and overall proof comprehension.** Mejía-Ramos and colleagues distinguish understanding terms, logical status and justifications from understanding a proof's main idea, components, transfer and examples. Their [2017 account of developing and validating proof-comprehension tests](https://sites.math.rutgers.edu/~jpmejia/files/Mejia_TUES_method.pdf), §2.2, develops the earlier 2012 model and makes the dimensions operational for particular undergraduate proofs. This pattern adopts the combination of local transitions and overall method in :4.2–:4.4. The published assessment results concern those proof-reading settings, while the generic recovery procedure here is a synthesis.

**Self-explanation.** Hodds, Alcock and Inglis's work is accompanied by the [Loughborough guide for mathematics lecturers](https://www.lboro.ac.uk/media/media/schoolanddepartments/mathematics-education-centre/downloads/SE-booklet-guide.pdf). It explains why relating claims to prior knowledge and to other claims differs from confidence reports or paraphrase. This contribution informs :4.4. The evidence reported there concerns undergraduate mathematical proof comprehension; it does not establish the effectiveness of this whole method for every practice or AI agent.

**Later assessment work.** The [PRIUM framework](https://doi.org/10.1007/s11858-024-01628-1), Cooley and colleagues (2024), develops proof-comprehension assessment through questions about definitions, statements and their relationships, with revision informed by discrepancies between intended questions and student answers. That is an assessment contribution to consider when demonstrated comprehension is required. The present method supplies the recovery work; it does not require a departmental assessment programme for an ordinary use.

**AI-assisted reasoning.** Klowden and Tao's [Mathematical Methods and Human Thought in the Age of AI](https://arxiv.org/html/2603.26524v1), especially §4.4, distinguishes a verified formal statement from the intended statement and from the explanatory reasoning around a proof. This pattern adopts the intended-use comparison and the recovery of the method behind the result. The essay provides a contemporary conceptual argument, rather than an experiment validating this procedure.

**Recoverable methods beyond answer production.** The [Math and AI declaration](https://mathandai.org/) raises the risk that rapid answer production can outpace understanding and development of methods. It is a position statement. This pattern takes the resulting recovery question: which reasoning can the next practitioner actually use? Human or AI production does not settle that question; the returned argument and its use do.

**Bounded method choice.** Compare line-by-line paraphrase, full proof validation and use-directed recovery on the same short argument. Paraphrase can retain the odd-sum formula while missing the equal-increment reason. Full validation answers correctness, but may spend effort inside already usable lemmas. Recovering the main reason together with the needed transitions gives the explanation or changed-use basis sought here. Select it when that is the unresolved task; retain full validation when correctness of the complete argument is the required conclusion. The drawing-recovery case extends the dependency method to a practical inference without treating mathematical proof as the sole form of reasoning. Reconsider this recovery approach if prepared readers repeatedly cannot recover why the decisive inference works, while another explanation or reading method enables the same use with comparable effort.

### B.5.RA:12 - Relations

- **B.5:** coordinates inquiry and the revision that can follow recovery of an argument.
- **B.5.RC:** obtains an auxiliary construction that a decisive transition requires.
- **B.5.MPC:** connects arguments and constructions across physical, mathematical and computational contributions.
- **B.3 and B.3.3:** govern confidence and assurance questions when the intended reliance requires them.
- **C.11.DUA:** selects additional checking and information for the decision at hand.
- **C.2.8 and C.37:** characterize recipient-accessible structure and support selection of representations.


### B.5.RA:End
