## A.3.2.DE - Describe a Method for Its Intended Use

> **Type:** Method pattern
> **Status:** Stable

> **Primary working result:** one `U.MethodDescription` edition and a use-coverage account for one admitted `U.Method`; or, when Method admission is absent, improved candidate-account content that keeps its candidate status.

### A.3.2.DE:0 - Use This When

Use this pattern when people need usable claims about an identified Method or a candidate account of a proposed way of working. The receiving use may concern planning, enactment, comparison, review, revision, publication or teaching; retain the claims' actual status. Start from one named use: who needs to do or decide what, which Method claims that use consumes, and what can remain outside the edition.

The first useful result is a short use-coverage row. It names the Method or candidate account, the receiving use, the claims needed now, the claims deliberately omitted, and the stop. That row prevents a documentation project from expanding before its practical question is clear.

Do not use this pattern merely to publish, diagram, approve, schedule, or record Work. A `U.MethodDescription` is the claim-bearing episteme whose exact `EntityOfConcern` is one Method already admitted under `A.3.1`; its code, diagram, form, carrier, approval, WorkPlan, and dated Work remain different things. If the proposed whole is still a candidate account, improve that account without classifying it as a `U.MethodDescription` for the whole.

#### A.3.2.DE:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| admitted Method | One reusable way of doing whose identity has been established under `A.3.1`. | A shared title, coherent document, WorkPlan, or successful occurrence does not establish it. |
| `U.MethodDescription` | One C.2.1 episteme about that Method whose claims say something substantive about how the Method is carried out. | Membership is not a completeness, approval, currentness, publication, or effectiveness result. |
| candidate account | Claims about a possible Method whose identity or obtaining relations remain unresolved. | It can be improved and used prospectively without being renamed a MethodDescription. |
| named use | A particular planning, enactment, comparison, audit, revision, publication, or teaching need with a receiver and stop. | A generic wish to “document the method” is not yet a use boundary. |
| use-coverage account | A C.2.1 account that states which Method claims an edition exposes for each named use and which it omits. | It does not prove that the claims are true enough for the use or that anyone used them. |
| representation and publication | A `C.29` correspondence, `E.24.PUB` form or publication occurrence, and carrier through which claims may be expressed or made available. | Form and availability do not decide MethodDescription membership. |

### A.3.2.DE:1 - Problem Frame

A working group often has too much material rather than too little: procedures, diagrams, code, examples, approval notes, logs, training slides, and tacit explanations. Different users need different portions. A planner needs applicability, preconditions, parameters, bounds, and stops; a performer needs the actionable claims for the current situation; a reviewer may need provenance, changed claims, and declared evidence limits.

Without a use boundary, authors either copy everything into one manual or reduce the Method to one convenient representation. Both moves hide whether the episteme actually describes an admitted Method and whether its claims are sufficient for the receiving use.

### A.3.2.DE:2 - Problem

A document can look complete while saying little about the way of doing. Conversely, a small claim set can be a valid MethodDescription yet be unsafe for a consequential enactment use. Teams also copy calendars, assignees, tool states, observed results, and approval decisions into the description as if adjacency turned them into Method semantics.

The result is difficult to reuse and difficult to challenge. Readers cannot tell which claims belong to the Method, which belong to one Work occurrence, which are evidence or policy, and which omissions require a return.

### A.3.2.DE:3 - Forces

| Force | Tension |
| --- | --- |
| Use fitness | Each receiving use needs enough claims, while one universal description becomes expensive and opaque. |
| Stable subject | Several editions and forms may describe the same Method, while a candidate or changed Method must not inherit that identity by typography. |
| Practical brevity | The first useful edition should be small, while hidden preconditions or stops can make it misleading. |
| Representation plurality | Text, code, diagrams, tables, and formal models may all help, while none determines MethodDescription membership. |
| Evidence limits | Claims may cite evidence and source limits, while the description must not become the evidence or assurance result. |
| Revision | A use may require a new edition, while editing a description does not by itself change the Method. |

### A.3.2.DE:4 - Solution

A.3.2 distinguishes description membership from adequacy for use. C.39:4.3–4.5 supplies construction of a missing action or join. Here the author develops the explanation for the declared reader: recover the actual operations, reasons, conditions and changed case that the reader must be able to follow, retaining an unresolved candidate as such.

Author claims for named uses while preserving the described Method's identity or the account's candidate status. Return gaps instead of filling them with neighboring objects.

#### A.3.2.DE:4.1 - Pattern-Use Unfolding

1. **Name the receiving use.** State the reader or consuming system, the action or decision, the situation and qualification window, and the stop. Replace “complete documentation” with the smallest question that changes work.
2. **Establish the subject branch.** Name the admitted `U.Method` and effective `U.ReferenceScheme`. If admission is absent, keep the subject as a candidate account and author only improved candidate content.
3. **Select the needed Method claims.** For the named use, consider the transformation or enactment concern, generic participant meanings, applicability, preconditions, intended effects or preserved conditions, bounds, parameters, variation, internal composition, evaluation conditions, and stops. Include only positions that change the use. For enactment or learning, recover the operations the performer must carry out and where their inputs come from.
4. **Separate neighboring claims.** Keep planned assignments and dates in a `U.WorkPlan`; actual performers, temporal extent, participation, and results with dated `U.Work`; operation declarations with `A.6.1`; evidence reliance with `A.10`; capability with `A.2.2`; approval, permission, and authority with the patterns that define those claims. Cite them when the use depends on them without absorbing them into Method semantics.
5. **Write the explanation or instruction.** For enactment or learning, connect each needed action to its inputs, the operation performed, the result and the condition for continuing or stopping. Explain why a connection or ordering matters when the reader needs that reason to apply or adapt it. For a Method that depends on professional judgment, explain which observations bear on the decision, how they change the proposed action, and which unresolved conflict needs another contribution or a stop. Naming a mindset without showing that effect leaves the explanation incomplete. Unfold a constituent operation until the intended performer can carry it out, or identify the missing know-how or contribution; do not invent an operation to fill a heading. Retain alternatives and genuine dependencies without imposing one order on independent actions. In the admitted-Method branch, identify the episteme by its claim content, Method as `EntityOfConcern`, and effective scheme. In the candidate branch, retain the account's proposed content and unresolved Method-identification conditions. State which claims were added, retained, narrowed, or removed when another edition is being revised.
6. **Record use coverage and omissions.** For each named use, list the claims exposed, claims deliberately omitted, unresolved claims, and the return condition. An omission is acceptable when the receiver does not rely on it; otherwise it is a gap.
7. **Choose expression and publication separately.** Select text, code, diagrams, a mathematical lens, publication form, and carrier only after the claims are stable enough for the use. When different named Method-related actions require complementary governed representations of the current MethodDescription or candidate account, C.37.MP returns a complete Method representation profile: one complete C.37 claim group per action, together with cross-use correspondences, conflicting omissions, edition relations, decisions to keep representations separate, and conditions that require reconsidering several selections. Use the FPF pattern governing any other represented entity.
8. **Try the receiving use from the description.** Recover the claims, conditions and omissions needed by the receiving use. For enactment or learning, work through a small case: recover the first action and its inputs, follow its result to the next needed action or stop, and expose any instruction supplied only from the author's memory. Return a description or candidate-account correction, or identify the missing input, know-how or other result needed by the use. This checks the description at that use; it does not establish the Method's effectiveness or a learner's acquired capability.

#### A.3.2.DE:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| subject | Admitted Method and identity basis, or candidate account and unresolved admission condition. |
| named use | Receiver, action or decision, situation, qualification window, and stop. |
| claim set | Method-side claims included in this edition and their effective scheme; the connected operations, inputs, results and conditions when the use requires an actionable instruction. |
| use coverage | Needed claims, exposed claims, deliberate omissions, gaps, and return condition for each use. |
| neighboring objects | Any WorkPlan, Work, representation, operation declaration, evidence path, capability, permission, authority, publication, or carrier relied on, each kept under its own kind. |
| edition disposition | MethodDescription edition, improved candidate-account content, or lower stop with the decisive missing condition. |

#### A.3.2.DE:4.3 - What Changes in Practice

Authors stop treating “the method document” as one undifferentiated object. They can issue a small edition for one use, explain why it is enough, and name the exact gap when it is not. Readers can distinguish a claim about a reusable way of doing from a plan, an observed occurrence, a tool presentation, or an approval fact.

### A.3.2.DE:5 - Archetypal Grounding

#### A.3.2.DE:5.1 - Stop at the Candidate Whole

`C-EC-Release-v2` is a prospective account of a possible release-coordination whole. Its intended result, alternatives A, B2, and R, guards, authority boundaries, confidentiality, reversibility, and D0 stop make it useful, but the whole is not admitted as a `U.Method`. A.3.2.DE may improve those claims for a selection or trial-planning use; it does not return a `U.MethodDescription` for that candidate whole.

The improved account remains useful: users can compare A and B2 before integration and plan a bounded trial with recovery R after a failed B2 closure. Every downstream use keeps the account's candidate status.

#### A.3.2.DE:5.2 - A Bounded Description of an Admitted Constituent Method

For the admitted constituent `M-HW-Verify`, suppose the named use is preparing safety-verification Work for one EC-417 release. A description edition can state the applicable safety-relevant change family, the distinction between provisional and signed evidence, the comparison and affected-verification actions, the signed-before-closure bound, confidentiality conditions, and the mismatch or stale-edition stop. The use-coverage account says that it exposes those Method claims but omits dates, assignees, actual evidence versions, actual verification results, and release authority decisions.

The planner may cite that edition when constructing a WorkPlan. Supply separate claims about the Work schedule, the assignment of `SafetyReviewer-17`, the required capability, closure authorization, and whether verification occurred whenever the plan or later Work relies on them.

#### A.3.2.DE:5.3 - Turn a reconciliation reminder into an instruction

In this constructed case, a stock-reconciliation Method has already been identified. Its working rule is available, but the draft for a new storekeeper says only: "Reconcile stock and investigate discrepancies." The reader can add and subtract counts; they still need to know which counts to compare and what the difference means.

The author recovers the rule's inputs and dependencies. For one item, unit and interval, an opening stock count plus receipts minus issues gives the expected closing count, provided the movement account includes every change once. A physical count at the closing boundary supplies a different input. The author writes this instruction:

1. Select the item, counting unit and interval. Obtain the opening count, receipts and issues for that same scope, and the physical count at its closing boundary. Resolve a missing movement class, unit conversion or mismatched boundary before treating the balance as complete.
2. Calculate expected closing stock as opening stock plus receipts minus issues. The additions and subtractions represent movements into and out of the selected stock.
3. Subtract expected stock from the physical count. Return the difference with the counts and scope used. A negative difference means fewer units were counted than the movement account predicts; it does not identify the cause.
4. If the counts disagree, return the discrepancy for checking the movements and counts. Do not change a source count merely to force agreement.

With opening stock 48, receipts 12, issues 17 and a closing physical count of 41, the expected count is 43 and the discrepancy is -2. The description now supplies an operation, its operands, their origins, the reason for their combination and a useful return. Its authoring result is the instruction, not evidence that a storekeeper performed it.

The receiving-use check asks the reader to recover that calculation and return from the description. If the opening figure is in boxes while movements are in individual units and the conversion is unknown, a numerical balance remains unavailable. A comparison-only description could legitimately omit this enactment detail; this edition promises the storekeeper a way to perform the reconciliation.

#### A.3.2.DE:5.4 - Explain the Basis of a Professional Judgment

A stakeholder map can keep the same boxes and labels while the way of constructing and using it changes. In this constructed case, an admitted contact-planning Method includes people who hold the approval or supply roles needed to arrange a rollout. A proposed child account instead asks whether a new shift-handover routine covers the work of the people who produce and use the handover information. Its author cannot explain that change merely by adding "be inclusive" to the old instruction.

The receiving use is a facilitator's preparation of a handover review. Available inputs are the proposed routine, the two-shift role roster, the information each role supplies or needs, and the known limits of those accounts. The author writes the proposed instruction:

1. Start from the handover information that must reach the next shift and identify the roles that produce or use it. Include a role because of that working dependency, even when its holder has little influence over rollout approval. Use actual supplied facts; mark an uncertain dependency for clarification.
2. For each included role, obtain an account of the information needed, the action it enables and a relevant missing-information case. Distinguish what a participant or work record actually supplies from the facilitator's assumption. A manager's approval does not supply another role's working account by itself.
3. Relate those needs to the proposed routine. Show which handover action supplies each needed result and which dependency remains uncovered or unknown. Influence can help arrange contact; it does not remove a required receiving role from this check.
4. Return the map with the supported coverage and the particular missing account or handover contribution. Stop a claim of complete coverage when a material dependency remains unresolved. The result can guide a correction or a bounded trial; it does not itself authorize rollout or show that the routine works.

For a small replay, suppose a day lead approves the trial, an IT maintainer supplies the display, and a night operator uses unresolved-item flags to resume work. The approval-contact map may correctly contain the first two roles. The proposed method also includes the night operator because the operator consumes a result needed for the handover. If the routine supplies a flag but no next action, the map exposes that missing contribution. If a relief operator's information need is unknown, add that unresolved dependency rather than treating a full roster of names as complete coverage.

The explanation now makes the changed judgment recoverable: inclusion follows a working dependency, and completion requires an account of its contribution. The canvas may remain unchanged, but the operation, required evidence and stop differ. This is proposed reusable content, so retain candidate status and use A.3.1.MV:5.2 for its derivation and evidence boundaries. The replay checks whether the explanation supplies the intended distinctions; it is not a field validation of the proposed method.

### A.3.2.DE:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| document identity bias | A titled document becomes the Method or its complete description. | Establish Method admission and identify the claim-bearing episteme separately. |
| completeness bias | More sections are assumed to make the edition adequate for every use. | Name uses and expose only the claim positions they consume. |
| execution bias | Code, a checklist, or executable syntax becomes evidence that Work happened. | Keep representation, WorkPlan, Work, and result claims separate. |
| policy absorption | Approval, permission, or authority is written as Method semantics. | Cite the separate policy or relation only where the receiving use needs it. |
| candidate laundering | A useful prospective account is called a MethodDescription. | Improve the account but do not call it a `U.MethodDescription` until `A.3.1` admits the Method. |

### A.3.2.DE:7 - Conformance Checklist

- [ ] Each `U.MethodDescription` result names one `A.3.1`-admitted Method as its exact `EntityOfConcern`.
- [ ] A candidate whole remains a candidate account when Method admission is absent.
- [ ] Every named use has a receiver, action or decision, situation, qualification window, and stop.
- [ ] Included claims say something substantive about the Method as a way of doing. An enactment or learning description lets the prepared reader recover the needed operations and their input/result connections, or exposes the missing contribution.
- [ ] Use coverage distinguishes exposed claims, deliberate omissions, unresolved gaps, and return conditions.
- [ ] WorkPlan, dated Work, actual participants and results, operation declarations, evidence, capability, permission, authority, representation, publication, and carrier claims remain separate.
- [ ] Representation choice does not decide MethodDescription membership.
- [ ] The result says only whether this edition covers the named claim need; it does not infer Method fit, effectiveness, assurance, or actual use.

### A.3.2.DE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Write the complete method once.” | Split the request into named uses and record coverage and omissions for each. |
| “The workflow diagram is the MethodDescription.” | Identify the claim-bearing episteme first; treat the diagram as one representation of selected claims. |
| “Add the project schedule so the description is actionable.” | Keep the reusable Method claims in the description and put dates and intended assignments in the WorkPlan. |
| “The procedure passed review, so the claims are adequate everywhere.” | Record the exact review or policy claim separately and evaluate each receiving use under its own conditions. |
| “The candidate account is detailed enough to count.” | Detail does not replace Method admission; return improved candidate content. |

### A.3.2.DE:9 - Consequences

Method descriptions become smaller, more reusable, and easier to compare because their subject and receiving uses are explicit. Candidate accounts remain useful without losing their truth status, and missing claims return to the right owner.

The cost is plurality: one Method may have several editions, use-coverage rows, and representations. Projects must also maintain links to neighboring plans, evidence, policy, and publication results instead of copying them into one manual.

### A.3.2.DE:10 - Rationale

Description adequacy is use-relative, while MethodDescription membership is not. Separating those questions allows a small episteme to describe an admitted Method without pretending to satisfy every receiver. It also lets a rich candidate account remain prospectively useful without turning description quality into Method identity.

The claim-first order prevents representation and publication choices from selecting ontology.

### A.3.2.DE:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| ISO/IEC/IEEE 24774:2021, [process-description elements](https://www.iso.org/standard/78981.html) | Adopt the discipline of describing purpose, outcomes, activities, tasks, information items, roles, and views only where the receiving description use needs them. | Description-side conformance does not establish process performance or FPF kinds. Practitioners still recover the admitted Method and each neighboring claim separately. |
| Daalhuizen and Cash, [Method content theory](https://doi.org/10.1016/j.destud.2021.101018) | Adapt the focus on content that helps a user understand and use a Method. | The source does not make one universal completeness schema. A.3.2.DE uses named-use coverage and explicit omissions instead. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Adopt intended use, procedure, representation, tools, and adaptation conditions as recurring authoring questions. | Conceptual elements do not prove Method identity, obtaining relations, Work, or effectiveness. The EC-417 slices preserve those stops. |
| Stacey et al., [Methods as a form of engineering knowledge](https://doi.org/10.1017/dsj.2025.9), §§2.4 and 4.4 | Adapt the connection between procedure, required knowledge and the generation of inputs and results: make the reasoning steps recoverable where the receiving use needs them. | This strengthens instruction construction and the small receiving-use check. Explicit content alone does not supply tacit skill, establish learning or settle FPF's Method/description distinction. |
| Current FPF `A.3.1`, `A.3.2`, `C.2.1`, `C.29`, and `E.24.PUB` | Adopt exact Method identity, MethodDescription membership, episteme identity, representation correspondence, and publication separation. | These patterns supply the identity and boundary rules; A.3.2.DE contributes the practitioner method for authoring a use-bounded edition and returning an honest lower result. |

Reopen the pattern when a representative user cannot state the named use without a universal field catalogue, when candidate status is repeatedly lost, or when the reader can find claims but cannot recover the promised operation, or when a current source offers a better way to select, explain or test the claims needed by a use at comparable effort.

### A.3.2.DE:12 - Relations

- `A.3.1` supplies Method admission; `A.3.2` defines `U.MethodDescription` membership and its boundary from plans, Work, representations, and publication.
- B.1.5.CM can supply an admitted whole or a prospective candidate account. A.3.2.DE preserves the branch it receives.
- RMP.10 can supply claim content and evidence limits for a candidate account; it does not admit the Method or create the description.
- C.37.MP consumes A.3.2.DE's current MethodDescription or candidate-account claims only when several unlike named Method-related actions require a Method-specific profile. It returns one complete C.37 claim group per action and a separate result showing how the selections relate: source correspondences, conflicting omissions, edition relations, decisions to keep representations separate, and conditions that require reconsidering several selections. For one action, use C.37 or the pattern that governs it; for another represented entity, use that entity’s governing FPF pattern.
- `A.15.2`, `A.15.1`, `A.10`, `A.2.2`, `C.29`, and `E.24.PUB` define or constrain the neighboring plan, Work, evidence, capability, representation, and publication claims that A.3.2.DE keeps separate.

### A.3.2.DE:End
