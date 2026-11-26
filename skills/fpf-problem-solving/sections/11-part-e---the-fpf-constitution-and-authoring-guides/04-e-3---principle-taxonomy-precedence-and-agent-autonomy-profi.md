## E.3 - Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)

> **Status:** Stable

### E.3:1 - Problem frame
When several provisions govern a decision, start with [the decision and the applicable provisions in §4.2](#e342---precedence-stack). Establish whether you can meet them together, which rule takes priority if they conflict, and who can settle an outstanding case or change the standing rule. Use §6 to design or select an autonomy oversight profile. Specify the decisions it permits, the limits, and the independent authority that can withdraw permission. When applying the profile, bind it to the actual action, budget and permission window. E.2 supplies the eleven constitutional pillars; their names alone do not settle a conflict.

### E.3:2 - Problem

When applicable pillars or derived principles prescribe incompatible actions, participants need an agreed basis for identifying which governs or which action must wait for an authorized resolution.

### E.3:3 - Forces
| Force                                 | Tension                                                            |
| ------------------------------------- | ------------------------------------------------------------------ |
| **Categorical Clarity**               | Coherent grouping ↔ preservation of individual nuance              |
| **Bounded Conflict Resolution**       | Predictable decisions or explicit holds ↔ authorized context‑specific priorities |
| **Evolutionary Stability**            | Durable core ↔ adaptability to new knowledge                       |

### E.3:4 - Solution

#### E.3:4.1 - **Principle Taxonomy**
   For this precedence classification, assign each principle **exactly one** class from { `Gov`, `Arch`, `Epist`, `Prag`, `Did` }.

   | Class                                    | Scope & Purpose                           | Example Pillars                                   |
   | ---------------------------------------- | ----------------------------------------- | ------------------------------------------------- |
   | **Gov** (Governance)                     | Change process, community decision‑making | P‑10 Open‑Ended Evolution - P‑11 SoTA             |
   | **Arch** (Architectural)                 | Macro‑structure & invariants              | P‑1 Cognitive Elegance - P‑4 Kernel               |
   | **Epist** (Epistemological and Ontological) | Semantics, evidence, trust                | P‑3 Scalable Formality - P‑8 Consistency          |
   | **Prag** (Pragmatic)                     | Real‑world value & cost/benefit           | P‑7 Pragmatic Utility                             |
   | **Did** (Didactic)                       | Cognition & learnability                  | P‑2 Didactic Primacy - P‑6 Lexical Stratification |

   *Epistemological* sub‑concerns (reasoning, falsifiability) reside inside **Epist**, keeping semantics and trust in one class.

 #### E.3:4.2 - **Precedence Stack**

Identify who would do what, for whom or to what, and when. Which provisions govern that decision? Can a course of action meet them together? A rule can require an action, forbid it, reserve a choice to a participant, or let another decision maker choose. A team can select a common format if the governing rule delegates that choice to the team. If the rule reserves the choice to each sender, a team instruction that removes the sender’s choice conflicts with it. Apply compatible provisions together. If applicability turns on a missing fact, compare what each possible rule would allow or require. When all support the same action on the same terms, it can proceed. Obtain the fact if it changes the decision or the required procedure, or if the task asks which rule applies.

The **FPF precedence rank** orders applicable provisions in the FPF constitution. A smaller number gives the provision priority where the two conflict. Rank 1 belongs to the eleven pillars themselves. The derived BLP policy also printed in E.2 has its own terms in §6. A passage that quotes a binding rule takes its force from that rule. When an organization adopts guidance for its own work, the terms of adoption establish where it binds.

| FPF precedence rank | Source | Effect for an FPF decision |
| --- | --- | --- |
| 0 | Vision & Mission (E.1) | Charter commitments govern what FPF may admit. |
| 1 | The Eleven Pillars (E.2:4) | Their applicable constraints bind principles and patterns within the charter. |
| 2 | Derived principles, including the precedence rules in E.3 | They govern pattern choices and proposals for change within the pillars. |
| 3 | Architectural and definitional patterns | Their applicable provisions constrain choices left to local rules in a conforming use. |
| 4 | Tooling and pedagogy | Their own suggestions guide implementation and teaching. |

**Apply the priority that governs the conflict.** Within higher-ranking constraints, first use an explicit priority for the provisions in conflict. For a remaining conflict between classified principles, use the default class order:
`Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did`

Apply the priority to the disputed choice and retain the other obligations. Several provisions can leave an obligation with no permitted way to satisfy it even when every pair is compatible. To establish that conflict, show how the provisions close every permitted alternative. If the alternatives are still unknown, identify what would establish them. After resolving a conflict, check the proposed course against the provisions together. Separately establish whether the people and resources needed for that course are available.

**When a conflict remains**, identify the provisions responsible, the affected action and the conditions that make them apply. Hold the dependent action. Independent permitted work can proceed. An existing ruling may already settle this case. If a holder is empowered to resolve this conflict, apply their actual decision within its scope and effective period. Until they decide, a known decision maker gives the parties someone to ask.

When the case would need an exception, use only an exception the governing terms authorize for these circumstances. If the mandate does not cover the conflict, keep the affected action on hold. To change a rule or priority for future cases, obtain the decision of the body or bodies empowered to change it. Record the rationale, affected scope, Pillar Impact Analysis and edge effects of an FPF change under E.9. For an exception governed by the FPF policy in §6, its DRR, rationale and expiry are required. An organization’s own policy sets the terms for exceptions within its authority. An earlier ruling governs a later case only when the governing terms give it that reach.

 **Graph Rule** — The precedence graph MUST be acyclic; any new edge that would form a cycle is **rejected**.

A release-schedule rule classified as Gov takes priority over a conflicting performance-tuning preference classified as Prag when the ranks and applicable explicit priorities leave the choice to the class order.

### E.3:5 - Conformance Checklist

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑PT.1** | Every principle record **MUST** state `class` and may list `precedence_over[]`.                                      | Makes declared priorities inspectable. |
| **CC‑PT.2** | Precedence graph **MUST** be acyclic.    | Prevents circular law.           |
| **CC‑PT.3** | Any DRR introducing/modifying a principle **MUST** include a *Pillar Impact Analysis* and the impact of proposed precedence edges on each affected Pillar (P‑1… P‑11). | Aligns evolution with Pillars.   |
| **CC‑PT.4** | When applicable provisions leave a conflict unresolved, identify the provisions and conditions that block the action. The dependent action **MUST** wait for an authorized resolution under §4.2. | Keeps the outstanding duty visible while other permitted work proceeds. |

### E.3:6 - Illustrative Conflict Resolution

**Same-kind wording.** First recover the intended kind under A.1. For an identified U.System, compare the plain name System with its technical expression U.System; both name the same kind. P-1 supports a precise, economical expression, while P-2 expressly gives human comprehension priority over theoretical or tooling purity. Use the familiar wording where it preserves the required meaning and make the technical designation recoverable where needed. The default Arch-over-Did order does not reverse that explicit P-2 priority. U.System is a proper subtype of U.Holon: replacing a non-System Holon with System would change the subject’s extension before any legitimate wording comparison.

**Two Gov rules with no priority.** G1 requires publishing report R to audience A at noon. G2 forbids the same publication. Both are Gov and have the same FPF precedence rank. Hold the report. Suppose the charter gives a duty officer power to decide individual report disputes. Naming the officer leaves today's decision open. If the officer rules that R must be withheld from A today, apply that ruling. Tomorrow's report still falls under the standing rules. A proposed change to their priority needs a decision from the authority empowered to change it.

**Changed case.** Suppose an authorized G2-over-G1 priority is in force for R, A and the noon window. G2 governs, so publication is forbidden; this pair needs no further priority resolution. A proposed G1-over-G2 edge would create a cycle and is rejected. The existing priority and G2's prohibition remain in force.

**Three provisions, two notice channels.** A service must send a notice today through either channel A or channel B. One provision closes A and another closes B. Both channels are working, yet there is no permitted way to send the required notice. Any two of these provisions could be met together. Report all three and the outstanding duty. If an authorized, effective exception opens A for this notice, send it through A. The restriction on B and the terms for tomorrow’s notices still apply.

**BLP and a guard.** If an applicable E.5 guard excludes a proposed implementation dependency, BLP-6 gives that guard priority over BLP. Compare those rules in their current scope, not the E.2 and E.5 files as whole nodes. B.3 enters the policy ordering for an assurance requirement consumed by the use.

**Local product policy and a pillar.** A product preference cannot override an applicable pillar merely because a local policy says it wins. A disclosed local tie-break can settle only a preference left open by the applicable higher rules. Classify the compared principles; a compound policy such as BLP need not receive one class for all its provisions.

**BLP-policy precedence (high → low, for applicable rules).** Law & Regulation → **E.5 Guard-Rails** → **B.3 assurance requirements consumed by the use** → **E.3 governance decisions** → **E/E-LOG policies** (editioned) → **BLP derived policy (E.2 §6)** → Product Policies → Implementation Tactics. This scope-specific ordering implements the stated BLP safeguards; it does not place a derived policy above a pillar or create unconditional file-to-file edges.

**Notes.**
* BLP is a constitutional policy (E.2) governing an activated scale comparison. E.5 Guard‑Rails and applicable B.3 assurance floors retain their force. A project can apply a separate generality preference only under the conditions its policy specifies.
* Wherever **NQD/E/E‑LOG** promotes illumination telemetry to dominance (via an explicit **CAL** policy; **policy‑id recorded in SCR**), **BLP adopts that lens** rather than overriding it (see E.2 BLP‑6).
* Any exception to policy **MUST** include a DRR with rationale and expiry.
* **BLP Override (Waiver).** A waiver is needed only when an applicable declared generality policy would otherwise decide the use and its exception rule is invoked. Name that policy, the rationale, responsible review System and direct responsibility basis, expiry/review, and the evidence required by the exception. Apply C.19.1's waiver and debt conditions. Ordinary bounded specialization is not an override. Add an AutonomyProfileId and GateDecision authority only when an independently applicable agentic profile governs the action.

**Set-returning parity.** Activated scale comparisons preserve parity and admissible operations under A.18; use G.5/G.9 where their selector/parity contracts apply. Independently applicable stronger profiles retain those requirements. Mixed-scale scalarization without an admissible operation remains prohibited.

**BLP — Bitter-Lesson Hooks into Precedence**
1) **Comparison and tie-breaking.** Under E.2 BLP-2, compare usable performance over the declared range and receiving conditions, with uncertainty in the contrast and applicable α/δ tolerances. When the comparison yields no scale-based preference, identify whether it establishes equivalence, establishes a trade-off or leaves the order open. A declared generality policy can settle the case if its terms cover that outcome and higher rules permit the choice.
2) **Procedure and search.** Select a positive procedure or general search under the task/control requirements and applicable policy. A mandated safety procedure keeps its force. BLP adds no universal prohibition-first rule or waiver for a fixed procedure.
3) **Publication.** A BLP precedence result retains the policy/edition and comparison basis. A performed full audit publishes its material resource and assurance accounts under E.2 BLP-1d and G.11. A bounded use with no scale claim creates no audit package.

**ABL — Autonomy‑Budget & Oversight Profiles (GateProfile)**
This section defines an **extensible family of autonomy oversight profiles** for agentic tool use: each profile specifies (i) a budget envelope, (ii) a Freedom‑of‑Action (FoA) descriptor, and (iii) the required **publication of a gate decision authorizing execution** under that envelope. The labels **L0…L4** are treated here as **profile identifiers** (not a fixed managerial ladder): projects MAY introduce additional profiles or sub‑profiles by minting new profile ids, provided they publish the same fields (budgets, FoA, decision roles, telemetry requirements) and keep profile changes explicit and auditable. For a further profile, declare which standard obligations it inherits and which additional safeguards govern it. Here “L1+” and “L2+” apply to the named standard profiles at or above those identifiers and to any additional profile that inherits the specified obligation. In documents that also use model abstraction levels, write *autonomy profile L2* for the oversight rule and *model abstraction level L2* for the modelling use in B.5.MR. A model at any abstraction level can be discussed under any applicable oversight profile.

| ProfileId | Name                         | Freedom‑of‑Action (FoA)                  | Explore‑Share (default) | Typical Use                                     | GateDecision authority |
|---------:|------------------------------|------------------------------------------|-------------------------|-------------------------------------------------|------------------------|
| **L0** | Scripted Execution           | **Whitelist only**; fixed scripts        | 0                       | Compliance‑critical, deterministic procedures   | Engineer‑of‑Record (EoR) or duly appointed maintainer |
| **L1** | Constrained Sequencing       | Negative constraints; **single‑tool**    | ≤ 0.10                  | Low‑risk automation with bounded novelty        | EoR + Peer Reviewer |
| **L2** | Supervised Autonomy          | Multi‑tool plans; bounded replanning     | 0.20 (±0.10)            | Ambiguous tasks; moderate budget                | Team Lead + Safety |
| **L3** | Auditable Autonomy           | Multi‑step, self‑replanning; adaptive    | 0.30 (±0.10)            | Production agents with learning under guard‑rails | Product + Safety + Legal |
| **L4** | Open‑Ended / Research Mode   | Broad FoA within sandbox & rails         | 0.40–0.50               | Illumination‑first exploration, sandboxes only  | Governance Board (Gov‑CAL) |

**Normative requirements by profile.**
* **Budgets.** Each profile **MUST** declare ceilings for **time / compute / cost / risk** and a FoA descriptor; each ceiling's meaning and scale must be explicit, with units where applicable under **C.16**. Planned ceilings remain **A.15.2** WorkPlan content, and run‑time consumption is tied to dated Work, aggregation, and provenance under **A.15.1**, **B.1.6**, and **A.10**. Budgets are **hard gates** at run‑time (**A.21**; C.Agent‑Tools‑CAL **ATC‑3** for stopping or replanning when a ceiling is breached).
* **Profile binding & change visibility.** Every CallPlan **MUST** declare the active profile id. A profile change **MUST** retain its from/to profiles, policy editions, effective window and A.21 permission result in the DecisionLog. Recompute the decision when its subject, action, rule, checks, scope or window changes. Cite an E.18 GateCrossing only when an independently selected TFS, exact source/receiving positions and changed CtxState bindings establish that structural transition. Add an F.9 Bridge only for its independently obtaining relation between the two F.17 local senses.
* **Assurance floors.** Apply B.3 to the named assurance claim and receiving use. A formality requirement names the expression properties needed under C.2.3, or a justified threshold on a declared local scale; any R threshold, composition, or CL loss needs its justified quantity, scale, and model under B.3/C.2.2. No universal F/R weakest-link minimum is imposed by an autonomy-profile label, and F does not substitute for R. Any justified profile-specific tightening for broader FoA **MUST** be declared on the profile and pinned by policy-id; the protection and decision-authority conditions remain binding. Pre-deployment **assurance deltas** MUST be recorded for L2+.
* **Exploration discipline.** When a live C.19 pool constrains the `CallPlan`, cite its `PoolPolicyResult`. Include the `EmitterPolicy` used by the plan and `explore_share` only when the plan uses that profile, including `0` when it explicitly plans no exploration. Apply the declared profile's exception rule to a deviation; do not invent live-pool refs after the action is fixed and pool treatment is irrelevant.
* **Provenance.** L1+ MUST emit a **CallGraph** with Service/Method editions, any used EmitterPolicyRef, budget deltas, and observation hooks (C.Agent‑Tools‑CAL **ATC‑5**).
* **BLP conformance.** Apply E.2 BLP when selection makes a scale claim or invokes a declared generality policy, retaining its α/δ tolerances and conditional debt requirements. L2+ alone does not establish a scale claim. A profile that independently requires a fuller comparison or audit must state that trigger and basis; its other budget, oversight and assurance duties remain binding.
* **Learning/Adaptation.** L3–L4 MAY enable adaptation only under product permission, change authority, E.5 and privacy controls. L0–L2 retain their profile default off unless their authorized policy change documents mitigation. Remaining fixed needs no BLP waiver; changing an applicable product requirement follows that requirement's exception rule.
* **Human‑in‑the‑Loop (HITL).** Use the profile’s **gate decisions and pause/resume hooks**. First distinguish authority to decide from a decision already in force. If the profile permits a standing resolution, establish that it covers this action, budget and window. Obtain a fresh decision wherever the profile requires one.
  * **L0–L1:** execution MAY start only after a **GateDecision** authorizing the CallPlan is present in the declared window.
  * **L2:** sentinels MUST be able to pause execution; resumption requires a new **GateDecision** recorded in the DecisionLog.
  * **L3:** the profile MUST declare periodic review windows; continued execution across a review boundary requires a **GateDecision**.
  * **L4:** continuous telemetry review; the default execution context is **sandboxed**. Leaving the sandbox requires an A.21 GateDecision for that bounded action, with the applicable signers, budget, scope/window and stop conditions. Publish the decision and profile/policy change. When the case also satisfies E.18’s structural crossing conditions, cite its CrossingRef and required per-binding accounts. Unchanged local meanings need no invented F.9 Bridge.

**Gate‑decision authority map (default signers; who may author GateDecisions).**
* **L0:** EoR or a duly appointed maintainer with authority for this action.
* **L1:** EoR **and** peer reviewer. Two distinct people exercise judgement in these roles. Each must be free to object, and both must actually assent within the scope the profile requires. They can issue one joint resolution. A service may prepare the evidence or record their assent. Require separate determinations or additional independence where the applicable profile prescribes them.
* **L2:** Team Lead **and** Safety representative.
* **L3:** Product Owner **and** Safety **and** Legal/Privacy.
* **L4:** **Gov‑CAL Board** (multi‑disciplinary) with documented scope, time‑boxed **trial budget**, and rollback criteria.

**Profile promotion / demotion triggers.**
* **Promotion.** Use the active profile’s required performance and assurance evidence for the actions and conditions it covers, including stability within the declared tolerances and budget for ≥ **N_policy** runs. Establish what the proposed profile would newly permit, which commitments and controls must hold together and what evidence covers those uses. Promotion requires its A.21 GateDecision. A supporting scale claim uses the usable-response comparison under E.2 BLP-1c. All independently required profile checks apply.
* **Restriction and reassessment.** Demote the profile when its declared risk or budget ceiling is breached, assurance drops below a required floor, or a significant **heuristic‑debt** item expires without replacement. A policy change calls for reassessing the affected permissions. Retain, restrict or extend them as the new terms, authority and grounds warrant. Publish a demotion as a profile-change and permission result with the applicable policy, budgets and effective window. E.18 governs a structural crossing when its conditions obtain.

**Profile-change cases.** A local budget revision from twenty to thirty minutes with unchanged meanings requires the authorized profile/policy change and its permission result; absent a selected TFS transition, it has no GateCrossing. If the profile label remains L2, the original twenty-minute permission cannot authorize execution at minute twenty-five. Apply the authorized new ceiling, required checks and effective window before continuing; otherwise stop at the old ceiling. A case that changes a CtxState binding between two positions in an independently selected TFS also satisfies E.18’s crossing obligations. Leaving a sandbox with unchanged F.17 senses needs the declared authorization and oversight, but supplies no semantic Bridge. Stop/resume, signer and budget duties remain applicable in each case under its profile.

### E.3:7 - **Conformance Checklist — E.3 ↔ BLP Interop**

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑E3.10** | Place **BLP** below E/E‑LOG and above product tactics. Resolve conflicts by the applicable precedence rules. Invoke the BLP exception procedure when seeking an exception to a preference that would otherwise decide the case (§6 and CC‑E3.11). | Identifies the governing rule and any required exception. |
| **CC‑E3.11** | A DRR invoking an exception to an applicable BLP/generality policy identifies that policy and meets its waiver, evidence and conditional debt requirements. Specialization or a fixed procedure alone creates no exception. | Keeps overrides visible without manufacturing them. |
| **CC‑E3.12** | Each agentic plan declares an **AutonomyProfileId** (e.g., L0–L4) with explicit budgets. Add `explore_share` and the **E/E‑LOG EmitterPolicyRef** only when the plan uses that live-pool profile under C.24 ATC-4. | Aligns autonomy with assurance. |
| **CC‑E3.13** | L1+ executions emit **CallGraphs** with editioned policy/method ids and budget deltas; L3+ include adaptation status. | Ensures replayability & audit. |
| **CC‑E3.14** | Profile changes follow **promotion/demotion** triggers and publish the profile/policy editions and A.21 decision. E.18 crossing refs and F.9 Bridge refs are present only when their separate predicates obtain. | Keeps autonomy under control. |

### E.3:8 - Consequences
*Positive* — Makes priorities and unresolved conflicts inspectable before the dependent action.

*Cost* — A conflict can delay the dependent work until a competent holder decides the case. Changing the priority for future uses can take longer and calls for the authority to amend the governing terms.

### E.3:9 - Rationale
The taxonomy groups principles according to what they govern: change (**Gov**), framework structure (**Arch**), meaning, evidence and trust (**Epist**), practical value (**Prag**), or comprehension (**Did**). Explicit override edges and the default hierarchy determine a winner where the declared ordering suffices. Where it does not, the hold leaves the decision with the holder empowered to settle this conflict. That mandate determines whether the ruling covers this case or changes future decisions. The taxonomy supports that decision; it does not make every pair comparable.

### E.3:10 - Relations
* **Depends on:** `E.1`, `E.2`
* **Governs:** Classification and precedence when an FPF pattern or DRR introduces, changes or compares principles. Guard‑Rail patterns reference CC‑PT. Section 6 also governs the oversight profile for agentic tool use.



### E.3:11 - SoTA-Echoing — resolve rule conflicts and bind oversight to the action

**Practice question and choice.** How can an agentic action use applicable governance rules and a budget profile without acquiring an undeclared priority or extra authority? The selected answer combines §4.2's partial order and unresolved-action hold with §6's editioned profile, concrete ceilings, checks and permission window. The simpler default uses one fixed conflict-combining rule and a stable table of profiles. That default is cheaper where every relevant rule fits its declared semantics and the table fully specifies the action; the added governance work is justified when obligations conflict or a profile's conditions change.

Under [Cedar's authorization algorithm](https://docs.cedarpolicy.com/auth/authorization.html), an applicable forbid overrides permits, otherwise an applicable permit allows the request, and the default is denial. **Adopt** explicit request scope and a declared combination rule where that permission policy is intended. **Reject** treating it as a universal ordering of obligations: a requirement to publish and a prohibition of publication can remain normatively inconsistent even when access is denied. Cedar does not claim to repair that inconsistency. Its policy-error handling also does not replace A.21's treatment of required check results. The source defines an authorization language, not FPF rule-change authority.

Engineering configuration management gives a practical test for the reach of an exception. After an authorized waiver for one item, a team inspecting the next item still works from the effective baseline. Apply that distinction to case rulings and standing amendments. The mandate governing the actual decision determines who can grant either and what the ruling covers. [NASA Systems Engineering Handbook, §6.5.1.2.3](https://www.nasa.gov/reference/6-5-configuration-management/)

For oversight, §6 draws on [NIST AI RMF 1.0 §6, pp.33–34](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf). Its profiles depend on the use, requirements, risk tolerance and resources; they can distinguish current and target conditions. **Adapt** that contextual treatment to §6's budgets, signers, checks and effective window. The source does not prescribe ABL's L0–L4 labels, numeric defaults or FPF permission semantics. A project's defaults need a basis appropriate to its use; an ordinal-looking label alone supplies none. This comparison uses the published 1.0 method.

At the same action and input scope, the two cases expose the chosen trade-off:

| Case | Simpler default | Selected move and cost |
| --- | --- | --- |
| G1 requires noon publication and G2 forbids it. Both have the same rank and class, with no priority between them. | A forbid-overrides policy can settle access when that policy governs the request. The duty to publish still needs a resolution. | Under §4.2 the report waits. A duly empowered officer can decide one report at the cost of referring that case. Changing the standing priority requires its own authority and rationale. |
| A plan keeps the label L2 while its requested ceiling changes from twenty to thirty minutes. | A stable profile table works if it already resolves the correct edition, checks and window. Looking only at an unchanged label cannot decide the new request. | §6 binds the new ceiling and permission before minute twenty-five. Maintaining those conditions costs more than checking a label; an existing table or policy system can carry them without another store. No E.18 or F.9 event is inferred from the budget change. |

The taxonomy groups principles for the declared fallback order; its five classes are not a claim that all governing duties reduce to permission predicates. Use the simpler default when its scope and maintained inputs suffice. Reopen only the affected priority or profile comparison when a new incompatible rule, changed permission condition, or equally adequate cheaper policy changes the action. BLP comparisons remain conditional on a scale claim or declared generality policy.

### E.3:End
