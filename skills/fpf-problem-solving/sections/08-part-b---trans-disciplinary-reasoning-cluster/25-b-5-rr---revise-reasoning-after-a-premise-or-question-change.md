## B.5.RR - Revise Reasoning After a Premise or Question Changes

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative unless marked informative

### B.5.RR:1 - Problem frame

Use this pattern when reasoning that you could previously use needs to answer a changed question, or when a premise, observation or application condition changes. You need to know what still follows, what must be worked again and what can now be done.

The object of revision is the reasoning used for that question: its premises, intermediate contributions, conclusion and conditions of application. The relevant practice supplies its inference rules and the grounds for using its premises.

**First useful move:** state the change beside the result you now need. Find where the earlier reasoning used the changed condition, or where the new result requires a contribution the earlier argument did not supply.

This work requires enough subject knowledge to follow the argument. Use B.5.RA when that reasoning must first be recovered. If the established result already answers the new question under conditions that still hold, apply it and stop. Rebuilding the entire argument is useful when recovery would cost more, or when a separate obligation requires a full new derivation.

### B.5.RR:2 - Problem

A familiar answer often survives in a formula, report or program after the reason for using it has changed. Repeating the earlier steps can produce a convincing answer to the former question. Discarding everything can waste constructions and arguments that remain useful.

Revision requires following the reason for a result. One conclusion may need several premises together; another may have two sufficient arguments. A premise may be shared by apparently different arguments. A change can also make a formerly fixed quantity the unknown, so replacing a number leaves the real task undone.

The result is reasoning that answers the changed question at its supported scope, or a useful partial result and the contribution still needed. It should let the receiver act, obtain that contribution or pursue the newly exposed question.

### B.5.RR:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse and hidden dependence | Retaining an established result saves work, but its application may use the changed premise indirectly. |
| Local repair and a changed question | A small correction can preserve the conclusion; a new objective may require another argument. |
| Several arguments and a shared weakness | An alternative can preserve a conclusion, while a premise common to both can defeat that apparent independence. |
| Useful qualification and continued inquiry | A conditional result or bound may suffice now; another use may need the unresolved premise or a new construction. |

### B.5.RR:4 - Solution

Start with the receiving question, follow the affected reasoning and derive the result that can now be used. A useful reminder is:

**Changed question or condition → affected reasoning → retained or replacement contribution → revised conclusion → receiving use.**

#### B.5.RR:4.1 - Say what changed and what is needed now

Compare the earlier question with the present one. State the result needed and the changed condition in terms that can be used in the reasoning. For a calculation, that may be a new range or an input that is now an unknown. For an empirical conclusion, it may be an observation, a changed population or an operating condition.

Distinguish a change in the situation from a correction to your account of it. A measurement taken yesterday can remain a sound report of yesterday while being insufficient for today's operation. A proposed condition can be explored hypothetically without replacing the account of what has happened.

Keep the meanings of the quantities and claims visible. If the same term now denotes a different quantity, translate the question before substituting its value. If only the spelling or presentation changed and the established application still fits, no reasoning revision is needed.

#### B.5.RR:4.2 - Recover the dependence that matters

Begin at the changed premise and at the desired conclusion. Find which intermediate claims or constructions connect them. At each relevant transition, ask what is needed together, what is produced and why that transition is allowed.

Keep a sufficient alternative separately. For example, recovering a file may require either a readable local copy or an available remote copy. If both are encrypted with one unavailable key, the two storage locations leave the same prerequisite unresolved.

Use an established lemma at the level its receiving use needs. Open its proof when the change reaches a condition of the lemma or the way its result is obtained. Do the same for an established measurement or computation: inspect the part whose application the change calls into question.

A sketch or a few statements can hold these dependencies. Use B.1.1 when a dependency representation needs its relation clarified. A reasoning dependency says which premise or operation supports a conclusion; physical causation and temporal order require their own relations.

If the needed dependence is missing from the account, recover it through B.5.RA or ask for that contribution. Treat a supposedly unaffected part as reusable only when its independence from the change is adequately understood for this use.

#### B.5.RR:4.3 - Derive what follows after the change

Work from available premises through the affected transitions. Reuse a contribution whose conditions and required result still fit. Where they do not, derive the replacement, select an adequate alternative or identify the unresolved step.

Withdrawing a premise removes that premise as a basis for asserting the conclusion. Another sufficient argument may still support it. To assert the opposite conclusion, obtain a reason for that assertion. The conditional argument can remain available for situations in which its premises hold.

Follow the change through each needed use of a shared prerequisite. Keep the premises of an alternative argument together: pieces from two incompatible situations do not form a supported argument for either situation. If conclusions refer back to one another, recover the grounding of that reasoning, such as an initial case and induction step. Mutual repetition alone cannot replace the starting support.

A changed requested result can require working backward as well. Identify what the new conclusion would need, reuse the earlier contributions that supply it, and produce the remaining contribution. Release a former fixed value when the question now asks you to determine it.

Compare the work of recovering and repairing the affected reasoning with the work of obtaining a fresh sufficient answer. A short new calculation can be cheaper and clearer. A maintained dependency account is useful when repeated revisions repay its cost; it is optional for an ordinary one-off question.

#### B.5.RR:4.4 - Choose the result the present reasoning supports

Relate the revised conclusion to the result requested in §4.1. It may supply the requested answer, a conditional answer, a bound or an obstruction. Say what the receiver can do with that result.

For a mathematical argument, carry the domain and assumptions into its conclusion. For an empirical application, examine the changed observation or applicability premise using the relevant subject method. Recomputing a model can establish its new consequence while leaving its correspondence with the physical situation unresolved.

If the original target is unattainable under the retained conditions, use the obstruction to propose a changed condition or a different question. Keep that proposal visible as a choice. A weaker result can be useful without silently replacing the requested result.

Obtain further evidence or checking when its possible outcomes can change this use. C.11.DUA helps compare that contribution with its cost. The method can finish with an explicitly conditional result when conditional use is sufficient.

#### B.5.RR:4.5 - Apply the result and carry the change to its users

Perform the receiving use, or give its next contributor the revised conclusion and the condition that governs it. When others rely on the earlier result, tell the affected users what changed and which application must change with it. Their unchanged uses need no new argument merely because a nearby result was revised.

Check the changed transition by the method appropriate to its claim. A small instance can reveal a substitution error; a proof establishes its stated general conclusion; an observation can test a physical consequence. Choose the check for the result actually being relied on.

Stop when the receiving question is answered at the required level, or when the remaining contribution has been located well enough to obtain it. A useful new question can begin another inquiry under B.5.

### B.5.RR:5 - Archetypal Grounding

#### B.5.RR:5.1 - Changing the range of a sum

A reader has established S(n)=n² for the sum of the first n positive odd integers, with S(0)=0 and n a nonnegative integer. The argument uses the shared initial value and increment: S(n+1)−S(n)=2n+1, also the increment from n² to (n+1)².

The new question asks for n terms beginning at 3: 3+5+...+(2n+1). The change is the range of summation. Reuse the established result on the first n+1 terms and remove the initial 1:

T(n)=S(n+1)−1=(n+1)²−1=n²+2n.

For n=4, the new sum is 3+5+7+9=24. The old formula applied unchanged would return 16. The proof of S survives; the application of that proof changes.

This repair also exposes a reusable construction. For n terms starting at a and increasing by 2, term j, counted from j=0, is (2j+1)+(a−1). Summing the established odd-number terms and the n equal additions gives n²+n(a−1). Changing the increment would require another derivation. The worked extension makes the next question precise without assuming that the same correction covers every progression.

For the next use, retain four terms and the increment 2, but require their sum to be 28. The former starting value a=3 becomes the unknown: 16+4(a−1)=28 gives a=4. Checking 4+6+8+10=28 confirms the required sum. If there are zero terms and the required sum is positive, no starting value can supply it: the empty sum is zero for every a. The changed question then requires a different term count or total.

#### B.5.RR:5.2 - Losing one way to recover a report

A team needs to read revision 17 of a report. Its established account has two ways to obtain that revision's bytes: decrypt the local backup using its available key and decryptor, or obtain an unencrypted remote copy. An available viewer then displays the report.

The key becomes unavailable. Following that change removes the local decryption route. The remote copy and viewer still supply the requested reading, so the team can proceed through them. The missing key need not be recovered for this use.

Now consider a different finding: the supposed remote alternative is encrypted with the same key. Both routes need that key, so neither supplied route obtains the bytes. The next contribution is the key, another usable copy or a different way to obtain the report. A second storage location had concealed a shared prerequisite.

If instead the viewer becomes unavailable, either route may still provide the bytes. Reading now needs a suitable viewer or format conversion. This repair preserves the obtained result and locates the different operation that the receiving use requires.

#### B.5.RR:5.3 - A repeated conclusion loses its starting support

An analysis establishes claim A from an observation O, derives B from A and uses B in a further argument for A. A corrected interpretation of O removes its support for A.

The second occurrence of A does not preserve that support: its offered reason B was itself obtained from A. Reopen both uses and look for an argument grounded in retained premises. The conclusion may be true, but this circular route no longer establishes it.

Contrast this with an induction argument whose base case remains established and whose step derives the next case from the preceding one. Its recurrence has a grounded way to obtain each finite case. The relevant inference, rather than the visual presence of a cycle or repeated letter, decides what can be retained.

### B.5.RR:6 - Bias-Annotation

The examples favor explicit premises and recoverable derivations. In statistical or interpretive work, revising one observation can require reconsidering dependence, selection or meaning before the changed conclusion can be obtained. Use the practice's inference method; a list of supporting statements does not supply it.

The method can also overvalue salvage. When the earlier reasoning is poorly recoverable and an adequate new answer is cheap, obtain the new answer.

### B.5.RR:7 - Conformance Checklist

- The present question and the consequential change are stated.
- The reasoning used by the receiving conclusion is recoverable at the needed depth.
- Joint prerequisites, shared premises and sufficient alternatives are preserved.
- Affected transitions are reworked under their applicable inference or construction rules.
- The revised conclusion retains its domain, conditions and any unresolved premise.
- The receiver can identify the next action, useful stop or contribution still required.

### B.5.RR:8 - Common Anti-Patterns and How to Avoid Them

| Observed failure in revision | Why it matters | Repair |
| --- | --- | --- |
| Replace a number while retaining the old question | The calculation still solves for the former unknown. | Restate the givens and requested result before choosing the computation. |
| Treat the loss of one argument as a refutation | A different sufficient argument may remain. | Examine its premises and derive the conclusion or its negation separately. |
| Count two dependent arguments as independent | Both can fail with their shared prerequisite. | Follow the common premise through both uses. |
| Preserve a conclusion through circular repetition | The retained statements supply no starting support. | Recover a grounded argument or leave the conclusion unresolved. |
| Repair the whole report to answer a small change | Unaffected results are needlessly reproduced. | Compare affected repair with a fresh sufficient answer and choose the useful scope. |

### B.5.RR:9 - Consequences

The practitioner can change an application while retaining useful reasoning, or explain why a larger change is required. A failure can expose a missing condition, a different construction or a worthwhile next question.

Recovery costs attention and sometimes specialist help. Its value increases when the same reasoning must be adapted repeatedly or divided among contributors. A short independent solution may remain the better choice for one small question.

### B.5.RR:10 - Architectural Rationale

An argument and an application can change separately. A theorem can remain established while its former substitution ceases to answer the question. An empirical premise can become doubtful while its conditional consequences remain worth investigating. Keeping those distinctions lets revision preserve knowledge without preserving an unsupported use.

The method therefore joins backward recovery of what the desired result needs with forward derivation from the premises now available. Alternative arguments preserve useful results; shared prerequisites explain where that preservation fails. Detailed deduction, statistical inference and physical-model revision remain contributions of their respective practices.

This is a method of obtaining and applying knowledge. Its result can also change the method repertoire: the revised sum reveals a parameterized construction, and an unresolved dependency can become the next research question. Those continuations are useful when they enable further work.

### B.5.RR:11 - SoTA-Echoing

**Which part of an argument needs revision?** Adapt the assumption-sensitive reasoning of de Kleer's [*A General Labeling Algorithm for Assumption-Based Truth Maintenance* (1988), §2](https://cdn.aaai.org/AAAI/1988/AAAI88-034.pdf). Compared with discarding every conclusion that used a removed premise, §4.3 retains sufficient alternatives and their shared conditions. This historical computational method supplies a precise model of conditional support. The present method uses that insight without requiring an ATMS or exhaustive assumption labels for an ordinary inquiry.

**When is incremental repair cheaper than starting again?** Adapt the comparison in Hu, Motik and Horrocks, [*Optimised Maintenance of Datalog Materialisations* (2018), §§1–4](https://www.cs.ox.ac.uk/people/boris.motik/pubs/hmh18optimised-maintenance.pdf): eagerly finding alternative derivations can avoid unnecessary deletion, but that search can itself be costly; recursive support needs more than simple counting. Section 4.3 therefore compares recovery and repair with a fresh answer. These are results for Datalog maintenance; selecting subject premises and interpreting empirical change require further reasoning.

**What should repair preserve for its receiver?** Adapt Klowden and Tao's [*Mathematical methods and human thought in the age of AI* (2026), §§4.4–4.6](https://arxiv.org/html/2603.26524v1). An inspectable proof result can serve one use, while changing its assumptions or applying its idea needs recoverable reasoning. Sections 4.1–4.5 retain that receiving question. The trade-off is explanation and recovery effort when another use actually needs them; full exposition is unnecessary for an already adequate application.

**What does current automated proof repair contribute?** [Wang et al., *Learning to Repair Lean Proofs from Compiler Feedback* (2026), §§3–5](https://arxiv.org/html/2602.02990v1), studies repair from generated failures and compiler feedback. Adapt its use of a localized failing transition when such feedback is available. Its single-shot formal-repair result answers a narrower question than choosing changed premises or interpreting an application. Section 4.4 preserves those questions instead of using compiler success as their answer.

Reopen these choices when better dependency recovery, subject inference or repair support changes the attainable result or the cost of obtaining it.

### B.5.RR:12 - Relations

- **B.5** coordinates inquiry and the next useful question. **B.5.RA** recovers the argument; **B.5.RC** recovers a needed construction.
- **B.1.1** clarifies the represented dependency relation. **A.6.3.RT** helps when the expression prevents the revision operation.
- **B.5.MPC** connects physical, mathematical and computational contributions. **B.5.MPC.R** uses this reasoning revision to repair a failed connection.
- **B.3, B.3.3 and A.10** supply the claim-specific assurance and evidence conditions. **C.11.DUA** helps choose worthwhile additional checking or information.
- **C.39** develops a missing way of obtaining a result. Revision may supply the construction from which that work begins.

### B.5.RR:End
