## SYSE.54 - Make Domain Behaviour Explicit Together with EventStorming

> **Type:** Method
> **Status:** Stable
> **Normativity:** Guidance for collaborative domain modelling in an engineering undertaking; constructed cases do not establish observed system behaviour.

### SYSE.54:1 - Problem frame

Use this pattern when people involved in the same service or product describe incompatible accounts of what
happens, why it happens and what should happen next. An equipment dispatcher sees a confirmed booking,
maintenance sees an unavailable kit, and a software developer sees an updated row. An engineering team needs
the shared behaviour and its unresolved conditions before it can improve the use or design its support.

The first useful result is a jointly corrected domain model: meaningful events, the decisions and actions
connecting them, relevant state, disagreements and examples that can change the proposed behaviour. It can
support an existing-process investigation or a proposed design. Identify which one is being discussed and
keep observed facts, participant reports and proposed rules distinguishable.

Begin with the concrete difficulty and people who know different parts of it. Let each contribute a few
significant occurrences in ordinary domain language. Ask what happened, to which case or object, and why
that matters. Organize and test the explanation together before choosing software boundaries.

This is EventStorming applied to engineering understanding and design of domain behaviour. Its surrounding
practice includes organizational discovery and professional facilitation; this pattern develops a bounded
route from exploration to a usable process account and, when needed, software-design questions. It assumes
access to people with relevant domain experience and a facilitator able to keep dissent visible. For a
sensitive or politically constrained inquiry, obtain suitable facilitation and safe participation; a board
filled by people unable to contradict the official account is a poor basis for reliance.

Use an adequate existing account directly. When one actor's interaction and expected result are already
understood, `SYSE.2` and its use-case treatment can suffice. For a few unknown rules in one interaction,
clarify those rules and examples without convening a wide workshop. EventStorming is neither mandatory
before engineering nor a complete course in Domain-Driven Design, business transformation or facilitation.

### SYSE.54:2 - Problem

Knowledge is distributed across people and systems. Each local account may be reasonable while their
combination omits a waiting period, failed request, external decision or conflicting meaning of “complete”.
A requirements list can hide these relations; one expert's process diagram can make everyone else's
exceptions look like mistakes. Choosing tables or services at this point embeds an unexamined account.

A shared event wall makes differences discussable, but agreement and visual order can create false confidence.
“After” may be mistaken for “because”; a request may be mistaken for success; a desired occurrence may be
reported as observed. The task is to construct and challenge an explanation useful for the receiving design,
not merely to arrange coloured notes or produce a comprehensive diagram.

### SYSE.54:3 - Forces

- Broad participation exposes missing behaviour, while too much scope prevents a usable explanation.
- Loose initial language lets different perspectives emerge; a design commitment requires enough precision
  to distinguish actions, conditions and outcomes.
- A typical path gives people something to discuss; consequential alternatives can defeat that path.
- A common timeline helps coordination, while concurrent work and negotiation do not have one fixed order.
- Software boundaries can clarify consistency and responsibility, while premature technical partitioning
  can silence the domain questions that should determine those boundaries.
- Collective understanding has value even without a polished artifact; a later user still needs a recoverable
  account of the distinctions and decisions on which the engineering work relies.

### SYSE.54:4 - Solution

Choose the extent of modelling from the receiving question. For broad discovery, reconcile the event
account enough to locate consequential disagreements and select a useful inquiry. For a selected process,
develop the connecting causes and decisions, then challenge the flow with a variation that could change
the design. Add software structures only when they answer a current implementation question. The following
operations can repeat as the account changes; the selected depth determines which are needed now.

#### SYSE.54:4.1 - Choose the purpose and prepare participation

Distinguish three useful depths. **Big Picture** explores a broad domain or business line to find conflicting
accounts and important areas for inquiry. **Process Modelling** develops a selected behaviour, including its
alternative outcomes and people's decisions. **Software Design** asks how supporting software can preserve
that behaviour through state, consistency and interface boundaries. They can be used independently. A broad
workshop need not finish with services; a small design session need not repeat a broad exploration.

State the practical question and initial scope, the current or proposed situation, and the decision or learning
that would make the session useful. Invite the people who know the consequential perspectives, including
those handling exceptions or receiving the result. A representative cannot fill an unknown fact by agreement.
Record the missing perspective and obtain it before relying on the affected claim. Arrange a shared surface
that everyone can read and change. Physical notes and an accessible digital board are alternatives; verify
that remote participants can actually contribute rather than merely watch a facilitator move notes.

Use a simple visible legend. Introduce events first; add another notation only when the discussion needs its
distinction. Labels as well as colour carry meaning. Agree how disagreements will be marked and revisited.
Do not spend the opening negotiating a complete ontology. A facilitator maintains participation and the
question; domain participants supply and challenge the behaviour. An eventual design decision retains its
own deciding subject and authority.

#### SYSE.54:4.2 - Recover events and reconcile the stories

Collect significant domain events in past-tense language, such as “kit collected” or “inspection failed”.
Participants can initially contribute in parallel when an official story may be incomplete. For each
ambiguous note, ask which occurrence it means and who would notice a consequential difference. “Process
booking” names an activity; “booking recorded” names an occurrence; “booking is active” names a state that
can persist. Preserve separate interpretations until examples show whether they are the same.

Arrange events in a plausible temporal account. Use separate lanes for cases or simultaneous threads when
needed. Fix gross differences of granularity: a whole service completion and a keystroke do not explain the
same level of behaviour. Keep the level that exposes the working difficulty, allowing a detailed local
branch where it matters. Mark a **hot spot** for a disputed rule, missing link, risk or unanswered question.
Attach it to the affected behaviour so that it can be investigated, rather than collecting detached worries.

Walk through the account aloud with a narrator and participants who can correct it. Ask where a thread
starts, what interrupts it, what counts as a useful or failed ending, and what happens beyond the initial
scope. Follow a troublesome result backwards to its required conditions, then forwards again. Add the
surrounding event or participant when the initial boundary hid a cause or consequence. Agreement after this
walkthrough means that these participants corrected this account; establish actual behaviour with suitable
observations before relying on a claim about what actually happens.

#### SYSE.54:4.3 - Explain decisions and changing state

For a selected flow, make the connecting grammar explicit. Someone uses information to request an action
from a responsible person or system. The request can be accepted, rejected or remain unresolved. An event
note states the claimed outcome. Establish the occurrence separately when the receiving claim requires
evidence. A subsequent decision may initiate another action under a rule. Ask who
makes that decision, with what information, under which condition, and when. Human judgement and automatic
rules can both occur; a drawn rule does not supply authority to act.

| Element | Question that makes it useful | Distinction to preserve |
| --- | --- | --- |
| Domain event | What consequential occurrence has happened in this account? To which case or object? | Distinguish the report from the occurrence and qualify the occurrence claim. A future scenario can propose the occurrence. |
| Command or action request | Who asks whom to do what, and what permits or prevents acceptance? | Requesting a booking is not successful booking. A command is not the reusable Method of carrying out the work. |
| Decision rule or policy | On this event, under these conditions, what should be done next and by whom? | “Whenever” needs its exceptions and timing. Temporal order alone establishes neither a decision rule nor a causal connection. |
| Information used for a decision, often called a read model | What must the person or software know, where does it come from, and can it be stale? | A display of availability may differ from the state used to accept a reservation. |
| State-bearing domain object or system | What changes, which identity continues, and what must remain true? | The event “hold expired” differs from the interval during which a hold is active. |
| External participant or time condition | What can happen without this team's command, and how is it noticed? | A supplier refusal or elapsed deadline needs a reaction. |

Connect an event to a next action only after stating the rule or physical dependency that warrants the
connection. Ask whether it happens always, immediately, only on working days or only after additional
information. A payment notification, for example, may report something already done elsewhere rather than
perform it here. For uncertain external behaviour, show the waiting and failure outcome instead of drawing
an assured success.

Track one object through the relevant events to expose illegal transitions and missing information. For
concurrent requests, ask what must be decided together. When exploring software, an **aggregate** can be a
candidate consistency boundary around domain objects whose invariant one operation must preserve. Derive
that boundary from behaviour and invariants; it is not a synonym for any important project subject or alpha.
A **bounded context** bounds a particular model and its language. Neither it nor an aggregate determines one
service, one database or one team. Compare those architecture choices separately with `SYSE.5` and `SYSE.6`.

Some parts of the domain are conversational: negotiation, diagnosis or design can revisit questions in
many orders. Mark that region and the events or conditions allowing it to finish. Model consequential rules
and the ordering constraints needed by the decision. If exact concurrency or temporal guarantees
matter, return that question to an appropriate formal or specialist method; the workshop model does not
prove them.

#### SYSE.54:4.4 - Challenge the account and produce a usable return

When developing a flow, first complete a simple meaningful path while retaining deferred objections as
hot spots. Then choose a
variation that could change the model: rejection, interruption, stale information, concurrent demand,
external delay or an expired time condition. Use concrete identities and quantities where they expose the
rule. Follow every selected branch to a stable result, an explicit waiting condition with its continuation,
or a named unresolved question. If the variation defeats the baseline, change the baseline rather than
adding exceptions indefinitely.

For behaviour that will be implemented, express decisive examples as initial state and information, triggering
action or event, and expected observable outcome. Include a refused or delayed action where it matters.
The group should be able to explain why the outcome follows and what would change it. These examples are
candidate acceptance conditions; executable tests, real observations and qualification remain further work.

Resolve the hot spots that prevent the receiving use. A remaining question can be carried explicitly to a
person or inquiry able to answer it, with the affected decision and a condition for continuing. Do not label
a flow agreed while a blocking contradiction remains. Nor must an exploratory session solve every issue:
it can usefully select the next bounded investigation and preserve what the participants learned.

Keep enough of the account for its actual receiver. Broad discovery can return consequential meanings,
disagreements and a grounded next inquiry; process modelling adds the selected flow, rules and variations;
software design adds candidate consistency and interface boundaries. In each case preserve the question,
scope, grounds, uncertainties and affected engineering use. Preserve participant
understanding as well as an accessible description; test whether a receiving practitioner can retell the
consequential relation. A photograph alone may omit the discussion that made a note intelligible.

A compatible account can supply a scenario and changed premise to `SYSE.2`, functional contributions and
coordination questions to `SYSE.5`, or software alternatives to `SYSE.6`. A hypothesis about current functioning
may instead need observation assessed through `SYSE.10`. Use only the receiving relation that is needed now.
Building an event model does not require event-sourced storage, a message broker or a microservice architecture.

### SYSE.54:5 - Worked case: a promised kit that maintenance has withdrawn

A field-service team is redesigning its equipment-booking support. Dispatchers say a crew receives a kit
when a booking is confirmed. Storekeepers distinguish a temporary hold from physical pickup. Maintenance
can withdraw the kit after inspection. The workshop asks what the new support must promise and what it must
do when a hold cannot be fulfilled. The following values are constructed design inputs.

Participants initially place “request submitted”, “booking confirmed” and “kit collected” in one row.
A storekeeper asks whether “confirmed” means allocated or collected; maintenance asks where withdrawal
appears. They split the wording into “hold accepted” and “pickup recorded”, add the external event “kit
withdrawn”, and mark the reaction to withdrawal as a hot spot. This changes the proposed behaviour before
any database or service is chosen.

For kit K7, hold H31 belongs to crew C2 until 10:00. The proposed rule permits at most one active assignment
of K7. A catalogue display can be a minute old, so a dispatcher viewing “available” sends **request hold**;
the reservation operation checks authoritative availability before accepting it. Its outcome can be
**hold accepted** or **hold refused**. The displayed value cannot authorize the promise.

The crew's pickup request must name H31. Acceptance requires H31 to be active and the acceptance time to
be before 10:00 on the agreed reservation time basis. Accepted pickup changes the assignment from held to
collected; the hold is no longer available for expiry release. At or after the deadline, pickup under H31
is refused even if the expiry worker has not run. **Release expired hold** checks that H31 is still active
and its deadline has passed before releasing it. The group has now exposed a concurrency requirement:
pickup and expiry must be decided against compatible authoritative state and time conditions. It records
that requirement for software design rather than claiming the wall has implemented it.

| Challenge | Expected behaviour in the proposed model | Consequence for design |
| --- | --- | --- |
| A second crew requests K7 while H31 is active | Refuse that request or offer a different kit; do not promise the same assignment twice. | The acceptance operation must preserve the assignment invariant. |
| The deadline has passed but expiry processing has not run | Refuse pickup under H31; reconcile or release the expired hold. | Acceptance checks the deadline as well as the current status, with an agreed time basis. |
| Pickup has already been recorded when an expiry request is processed | Do not release the collected kit because of the old deadline. | Identify H31 and its current state; replay of a stale request must not reverse a completed pickup. |
| Maintenance withdraws K7 before pickup | Suspend fulfilment of the hold, inform the dispatcher and crew, and request a replacement decision. | External withdrawal needs an observable input and a responsible reaction; automatic success is unavailable. |
| The maintenance message arrives twice or late | Determine whether it concerns this kit and relevant interval; avoid repeating an irreversible response blindly. | Message identity, currentness and reconciliation need an implementation decision. |

The participants also ask what the crew sees while a replacement is unresolved. “Confirmed” would now be a
false promise. They choose an explicit awaiting-replacement state and notice requiring the dispatcher to
act. The model therefore changes the use concept, the information displayed and the work to be supported.
A policy for which replacement is acceptable remains a domain decision.

The immediate result is the corrected account, these proposed acceptance conditions and two implementation
questions: atomic handling of assignment transitions, and reliable receipt and reconciliation of maintenance
changes. `SYSE.2` uses the account to revise the linked use and system concept. `SYSE.6:4.4.4` shows why the
reservation invariant can stay in one authoritative operation while other work is separated. Observations
of current depot practice and implementation tests can support claims about actual practice and implemented
behaviour; agreement on the proposed model cannot establish either by itself.

**Changed condition.** Suppose maintenance provides no timely notification, only a nightly export. The
same visible event sequence no longer supports a firm real-time availability promise. Participants compare
a pickup-time inspection, a qualified provisional reservation and a changed provider arrangement. They must
change the promised behaviour or obtain a timely contribution; adding a queue box cannot supply missing
knowledge. Still-valid meanings of hold, pickup and identity remain useful.

**Unlike use.** In a design-consultancy inquiry, a client and engineer negotiate scope, revisiting cost and
options in arbitrary order. A conversational region with “proposal accepted”, “inquiry withdrawn” and
“response deadline reached” as exits can expose the handover to scheduled work. Enumerating a fixed command
for every conversation would misrepresent this use. If only one representative story is needed to understand
who exchanges which work objects, Domain Storytelling may supply a smaller sufficient account.

### SYSE.54:6 - Biases to watch

The loudest participant can make a preferred story look shared. Seek the exception handler's and receiver's
accounts, and preserve dissent at the affected step. A facilitator's plausible completion of a gap is a
hypothesis until someone supplies grounds. Familiar software objects can also dominate interpretation:
ask about domain behaviour before mapping a sticky note to a class, table or message.

A smooth typical path is an insufficient challenge. Choose the variation from the real risk or uncertainty,
not one guaranteed to preserve the current design. Distinguish disagreement about facts from disagreement
about which future behaviour to prefer; they need different continuations.

### SYSE.54:7 - Conformance checklist

| ID | A conforming use... |
| --- | --- |
| CC-SYSE54-1 | states the receiving question, current or proposed situation, scope and required perspectives. |
| CC-SYSE54-2 | constructs and corrects a shared account rather than imposing one participant's private model. |
| CC-SYSE54-3 | distinguishes occurrences, state, requests, performed actions and evidence where the receiving claim depends on them. |
| CC-SYSE54-4 | for a selected process or software design, explains the decisions, information and conditions connecting consequential events, including relevant external or time conditions. |
| CC-SYSE54-5 | tests consequential interpretations with concrete examples; when developing a flow, challenges its meaningful path with an action-changing variation and retains a blocking uncertainty as such. |
| CC-SYSE54-6 | derives any software consistency or language boundary from the behaviour and keeps its deployment choice open. |
| CC-SYSE54-7 | returns a usable account, proposed examples or bounded inquiry with grounds and limits appropriate to the next engineering use. |

### SYSE.54:8 - Common failures and repairs

| Failure | Repair |
| --- | --- |
| A wall of department tasks | Recover meaningful occurrences and the behaviour connecting them; use activities when asking how an occurrence is produced. |
| Every request becomes success | Add refusal, waiting and failure outcomes; identify the condition governing acceptance. |
| Timeline treated as causal proof | State the rule or physical dependency; obtain evidence for a claim about actual behaviour. |
| Every sticky becomes a service or event-store record | Recover the invariant, language and runtime question before comparing implementation boundaries. |
| A tidy happy path hides dissent | Revisit the attached hot spot with a concrete counterexample and the missing perspective. |
| Negotiation explodes into arrows and loops | Show the conversational region, consequential rules and exits; formalize only the required guarantee. |
| Workshop consensus substitutes for permission | Obtain the relevant decision and authority before changing actual work or promises. |

### SYSE.54:9 - Consequences

Participants gain a shared explanation they can challenge and use to change a concept, requirement or
architecture question. The method can reveal hidden coordination, ambiguous promises and missing information
before implementation commits to them. Learning and corrected relationships can be valuable even when the
next result is an inquiry rather than a design choice.

The cost is obtaining the right participation, sustaining a useful level of detail and preserving the
reasoning for later users. Missing access, unsafe participation or unresolved professional questions limit
reliance. No general reduction in defects, delivery time or conflict is asserted by these constructed cases.

### SYSE.54:10 - Rationale

An event gives different participants a shared point from which to ask what preceded it and what it changes.
Requests, decisions and state then explain the connections that chronology alone leaves open. Collective
construction makes incompatible perspectives visible; concrete variations test whether their reconciliation
survives a consequential change. The result is a domain explanation, with implementation and assurance
questions made more precise.

This complements `SYSE.2` rather than replacing it: a corrected domain flow can change a linked use and
system concept, while an available concept can supply the question for a narrow modelling session. It also
specializes the collaborative reasoning of `B.5.SD` with a particular subject grammar and constructive route.
These relations allow direct use without making a workshop a compulsory engineering stage.

### SYSE.54:11 - SoTA and source use

The practice question is how a mixed domain and engineering group can make behaviour understandable and
challengeable before relying on it in design. **Adopt and adapt** EventStorming's progressively corrected
shared account. [Brandolini's current overview](https://www.avanscoperta.it/it/eventstorming/), especially
“Main recipes” and its three format sections, distinguishes broad discovery, process modelling and software
design. It also explicitly permits paper-based processes and simpler software architectures. The useful
contribution is the relation between purpose, depth and modelling operations; promotional claims about
universal effectiveness are not evidence for this pattern's results.

[Brandolini, Collaborative Process Modelling with EventStorming (2022)](https://medium.com/@ziobrando/collaborative-process-modelling-with-eventstorming-17ed363650c0)
develops the request, decision-information and reaction-rule grammar. The current official patterns
[Chaotic Exploration](https://www.eventstorming.com/patterns/chaotic-exploration/),
[Incremental Notation](https://www.eventstorming.com/patterns/incremental-notation/),
[Rush to the Goal](https://www.eventstorming.com/patterns/rush-to-the-goal/),
[Raise the Bar](https://www.eventstorming.com/patterns/raise-the-bar/), and
[Extract Acceptance Tests](https://www.eventstorming.com/patterns/extract-acceptance-tests/)
explain different moves, not one mandatory workshop script. **Adopt** their conditional uses in §§4.1–4.4.
[Conversational System](https://www.eventstorming.com/patterns/conversational-system/)
supplies the important limit on forced sequencing. The kit case, its engineering returns and the distinction
between proposed behaviour and evidence are the present synthesis; they are not reported source experiments.

For the software-design question, [Microsoft's tactical DDD explanation](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design),
“Aggregates”, connects a consistency boundary to domain invariants. **Adopt** that question when modelling
conflicting state changes. The boundary can contain one entity or several; it is not inferred from the
number of event notes. This use of DDD does not require microservices or make an aggregate, bounded context
and deployed service identical.

An alternative is [Hofer and Schwentner's Domain Storytelling quick-start guide](https://domainstorytelling.org/quick-start-guide),
especially its scenario and workshop sections. It develops concrete stories of actors, activities and work
objects, with immediate correction and retelling. Prefer that route when a few representative interactions
supply the needed understanding with less notation. EventStorming becomes useful when comparing event-centred
accounts and the rules joining multiple reactions exposes the live difficulty. Neither method is generally
superior; both require participants who know the domain. Another smaller answer is the use-case route in
`SYSE.2:4.5` when the question is already a bounded actor interaction and its implementable, testable slice.

The current official [resources](https://www.eventstorming.com/resources/) provide further facilitation and
software-design material, including the inventor's book and workshop formats. They extend professional
preparation. Reopen
the selected route when its notation hides relevant behaviour, the participation burden exceeds its useful
contribution, or an adequate existing account answers the question more cheaply. Changed practice and source
conditions reopen the affected advice, not every unrelated engineering method.

### SYSE.54:12 - Relations

- `SYSE.2` consumes a compatible domain account when it changes a use or system concept; it can also supply
  the bounded situation being modelled.
- `SYSE.5` uses the explained contributions, state and coordination conditions to construct bearer alternatives.
  `SYSE.6` chooses among sufficiently developed architectures.
- `SYSE.7` keeps the resulting description compatible with other engineering accounts. `SYSE.10` assesses
  the observations or tests used to support claims about actual behaviour.
- `B.5.SD` supplies the general construction of a joint substantive answer.
- When an explicit state-change rule is needed, use `A.3.3.TR` to specify what an action reads, changes and
  leaves unchanged, and to distinguish jointly active conditions from alternative actions. Return the usable
  rule or missing condition to the domain account. An adequate qualitative account needs no additional rule.

### SYSE.54:End
