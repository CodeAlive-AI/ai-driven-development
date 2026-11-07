## SYSE.18 - Decide Whether and How to Integrate Systems Governed by Different Agents

> **Status:** Stable

### SYSE.18:0 - Use This When

Use this pattern when one use depends on several actual Systems, but decisions that can change that use—for
example, a constituent's operating condition, configuration, commitment, interface, or later modification—belong
to different Agents. The integrating Agent cannot command every change that can defeat the use.

Begin with the shared use and the actual constituent Systems that can defeat it. For each constituent, state how
it affects that use, who can decide the relevant change, what authority that Agent has, and which configuration,
interface, commitment, evidence, or withdrawal condition the decision relies on. Then compare arrangements for the same use, separating changes already within authority from proposals
that require another Agent's decision. A useful current decision can authorize preparation or retain the existing
arrangement while a particular dependency remains unresolved.

The first useful result is a **bounded constituent-integration decision**. It states the selected coordination alternative,
the deciding Agent's authority, decisions required from other Agents, accepted losses, unsupported dependencies,
and next Work. If integration Work is later performed, identify that Work, its actual transformation or newly
obtaining relation, and the observed-coordination claim separately from the decision episteme.

Use ordinary architecture and integration patterns when one deciding Agent controls every constituent change
that can alter the use. Use the neighboring practice that owns a different question—for example, Organization
Change when an organization is the System being changed, Corporate Governance for ownership and governing-body
decisions, Operations Management for continuing allocation and coordination Work, or a configuration or other
specialist pattern for its own subject.

#### SYSE.18:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| shared use | One named result or use whose conditions depend on several Systems. Any hierarchy or whole–part claim needs its own relation. |
| constituent System | An independently identified actual System whose participation, result, failure, change, or withdrawal can alter the shared use. *Constituent* names that use-relative relation; state any proper-part relation separately. |
| independently governed | A decision relevant to the use—for example, a commitment, operating choice, configuration change, or withdrawal—is controlled outside the integrating Agent's authority. Independence concerns the named decision, not every aspect of the System. |
| system of systems | A source or domain label that prompts recovery of the actual Systems and relations relevant to the shared use. Classify those Systems and relations directly rather than treating the label as a universal kind. |
| interoperability | The evidence-backed ability of named Systems, under a stated configuration and conditions, to exchange results through identified interfaces and make those results usable for the shared use. Interface descriptions are epistemes about this ability, not participants in the exchange. |
| commitment | An obtaining duty relation with a bearer, referents, scope, validity, governing rule, and instituting basis. Record its content, later Work, delivered result, and evidence of fulfilment as separately grounded claims. |
| constituent-integration decision | The episteme that selects one bounded coordination alternative within stated authority and records outside decisions, unsupported dependencies, next Work, and reopen conditions. |
| observed-coordination claim | A later evidence-backed claim that named Systems coordinated for the shared use under stated configurations and conditions. Record the earlier decision, performed Work, commitments, observation, and claim interval separately. |

A System described, for example, as an owner, operator, integrator, supplier, or decision maker is an Agent only
when the agency claim is warranted. State the direct predicate and participants for every relied-on claim. Use the
applicable pattern when the decision depends on agency, authority, a commitment, performed Work, capability, or
evidence; state constituent participation and the shared use separately.

### SYSE.18:1 - Problem Frame

For example, district drainage can depend on separately governed pump stations, gates, drainage networks,
dispatch Systems, provider organizations, and public infrastructure. A product can likewise depend on independently
evolving software, communication, payment, and energy Systems or regulatory organizations. Each constituent can
remain useful elsewhere and change for reasons outside the integrating project.

Drawing a larger boundary does not create authority or interoperability. A model or interface description can
carry claims. An agreement can institute a commitment. A meeting is Work. A governing body is a System whose
participating Agents may make authorized decisions. For constituent Work, identify its performing Agent; for
another Agent's decision, identify that Agent's authority.

### SYSE.18:2 - Problem

An integrating team needs answers to seven practical questions:

1. Which shared use, conditions, interval, and engineering decision are at issue?
2. Which actual Systems can defeat the use by changing, failing, withdrawing, or withholding a result?
3. Which direct relation connects each System to the shared use, and what does that relation change?
4. Which Agent controls each relevant decision, and what authority, permission, or escalation relation obtains?
5. Which configurations, interfaces, capacities, timings, commitments, and evidence make coordination possible?
6. What can the integrating Agent change, and which decisions must come from other Agents?
7. What actual observation would show that the changed arrangement works for this use?

Missing answers produce four recurring errors: interface syntax is mistaken for interoperability, an agreement
for performance, a constituent label for parthood, or an integration team for authority over Systems it does not
govern.

### SYSE.18:3 - Forces

Recurring tensions include:

- The shared use needs coherent results; constituents retain other uses, priorities, owners, and decision centres.
- Integration benefits from stable interfaces and commitments; Systems and environments continue to change.
- Receiving decisions need comparable evidence; every source keeps its provenance, limits, and authority.
- One Agent can compare shared-use options while several Agents separately permit constituent changes.
- Some coordination can be agreed in advance; operating conditions can require continuing reconfiguration.
- A broad account reveals dependencies, while the current decision must remain feasible within actual authority.

### SYSE.18:4 - Solution

Recover the constituent arrangement from the shared use, make distributed decisions and dependencies explicit,
and choose one bounded coordination alternative within the deciding Agent's authority.

#### SYSE.18:4.1 - Perform the Move

1. **Bound the shared use.** State the result, operating conditions, interval and decision to be made. Identify
   the losses that this decision may accept and the conditions it must preserve. Begin with an adequate current
   account when one exists; use this Method only for the missing or changed connection.
2. **Recover constituents by consequence.** Follow the result back to the Systems whose participation, failure,
   change or withdrawal could defeat it. State what each contributes or constrains and why that matters here.
   Preserve an observed participant whose identity is still unknown; distinguish that uncertainty from an
   unknown existence claim or a future intended System.
3. **Trace the relied-on connection.** Follow one representative use through the constituent results and
   interfaces. Match what the receiving operation needs with what the supplying System can provide, under the
   same configuration and conditions. Section :4.1.1 explains how to turn a mismatch into a design question.
4. **Recover the relevant decisions.** Identify who can change each decisive condition, what authority or
   permission obtains, and which other uses constrain that choice. An unresolved authority claim can leave
   comparison possible while preventing authorization of the corresponding change.
5. **Construct alternatives around the mismatch.** Change the receiving operation, supplied result, interface,
   allocation, timing or means of recovery that produces the failure. Keep a sufficient existing arrangement
   among the alternatives. For another Agent's proposed change, identify the needed decision and the consequence
   if it is refused or delayed; :4.1.2 explains the comparison.
6. **Select a bounded continuation.** Compare admissible alternatives for the same result and interval. State
   what the selected arrangement gains, what it gives up and which unresolved condition limits the decision.
   Reuse sufficient analysis. Select further inquiry by what it could change and its attainable cost and delay,
   using `SYSE.9` and `C.11.DUA` when needed. A required permission or physical qualification still governs use.
7. **Make the decision usable by its participants.** Explain the choice, consequences and remaining freedom to
   the people who must decide or perform the affected work. Resolve a consequential mismatch of understanding
   through :4.1.3. Record the decision within the deciding Agent's authority, required outside decisions,
   accepted losses, next Work and reconsideration conditions.
8. **Follow authorized enactment and selective change.** When integration Work occurs, retain its performer,
   Method, actual change, configuration and evidence. Observe the shared use at the scope needed for the
   receiving claim. Section :4.1.4 connects changed conditions to the decision that relied on them.

Constituent operation, engineering, governance, and integration can be simultaneous; only stated dependencies
and temporal relations establish order. Finish when the current decision and its useful continuation are
supported. An integration decision need not wait for the later installation or operating observation.

##### SYSE.18:4.1.1 - Find the condition that breaks the shared use

Start at the required result and work backward to its necessary contributions, then follow a concrete occurrence
forward. At an interface, identify the supplying and receiving Systems, what passes between them, and the
condition that makes it usable. For a timed contribution, distinguish when it is produced, received, acted on
and needed. Compatible message formats can still carry a late, stale or inapplicable result.

Compare needs and provision on the same basis. A receiving operation may need six hours after a notice while
its provider promises only four hours before an outage. The missing two hours then becomes a specific question:
can the provider give earlier notice, can the receiver respond sooner, or can another arrangement support the
use during the interval? Those proposals alter different things and require different decisions. The notice commitment is the duty to give notice. Evidence of response capability or actual performance
supports the separate claim about what response can be relied on under the stated conditions.

Include a constituent's competing uses when they consume the same capacity or determine its availability.
Two individually sufficient offers may be incompatible when they reserve the same resource at the same time.
Use `SYSE.13` for configuration correspondence, `SYSE.9` for a needed specialist result and `SYSE.20` when the
issue is joint Work or resource use. Retain a compatible supplied result rather than repeating its production.
If the necessary condition cannot be established, carry that precise dependency into the comparison.

##### SYSE.18:4.1.2 - Compare arrangements that could actually supply the use

Generate an alternative by naming the changed connection and following its consequences to the whole result.
For a proposed buffer, derive the quantity to be held over the unsupported interval, where it goes, when it is
available and how normal operation resumes. For a replacement provider, follow the new result through the
receiving operation, including transfer and qualification. For a changed commitment, establish what its bearer
would have to decide and perform. Narrowing the use is a different offered result; its loss needs acceptance
by whoever may decide that scope.

Separate three questions for each proposal: would the arrangement satisfy the required use under its stated
premises; can its necessary changes be authorized and supplied in time; and does its benefit warrant the
whole burden? A technically workable proposal awaiting another Agent's agreement can remain a conditional
alternative. It cannot serve as an already available fallback. Conversely, a requested change refused by one
Agent does not preclude an admissible change within another's authority.

Eliminate a proposal from the present operating choice when it violates a protected condition. Compare the
remaining arrangements on the same horizon, including acquisition, transition, operation and later reversal
where they matter. Keep unlike losses explicit. A weighted score is useful only with an applicable comparison
rule; it cannot turn missing permission or an unacceptable physical consequence into a compensable cost.
`SYSE.6:4` supplies the fuller comparison when the choice fixes project-shaping structures across later work.
Here the additional question is which independent decisions and commitments make each arrangement possible.

Preserve a tie or conditional result when the present basis cannot settle the choice. Name the particular
outside decision, professional result or affordable inquiry that could settle it. If no attainable answer is
needed for the current useful decision, stop with that decision and its limit. Prefer a sufficient unchanged
arrangement over a new one whose extra burden buys no needed result.

##### SYSE.18:4.1.3 - Explain the technical choice and resolve its effect on others

Take the proposed arrangement to the affected decision makers and practitioners with its reason: the shared
result, the condition currently defeating it, the alternatives considered and the change proposed for their
own contribution. Ask them to apply it to a representative occurrence and a relevant failure or change. What
would each do, what input would they rely on, and what would they return to the next participant?

Compare these accounts at the consequential joins. If one participant interprets an acknowledgement as a
promise of capacity while another means only receipt of a message, repair that misunderstanding before relying
on the exchange. If everyone understands but a provider cannot reserve the resource, the missing result is
provision or a different arrangement. If a participant lacks the professional means to perform the action,
obtain that contribution or revise the proposal. More explanation alone cannot supply either resource or skill.

Keep a substantive objection available to change the technical choice. Resolve the local decision within
established authority; obtain another participant's decision for the part they control. Use the relevant
negotiation, organization or governance Method when that becomes the unresolved question. Agreement to discuss
a proposal remains different from commitment to perform it. The explanation can finish when the affected
participants can use the same conditions and identify their own decisions, actions and return conditions;
it need not make every participant an expert in every constituent System.

##### SYSE.18:4.1.4 - Follow changes through the connection that depended on them

Select observations for the reliance being made. A description-consistency result can support comparison of
models. A claim that the configured Systems coordinate in operation needs corresponding operating evidence;
`SYSE.11` supplies the integration and qualification Method. Reuse adequate evidence at its actual scope.
Record a later observed-coordination claim separately from the earlier decision and each commitment's fulfilment.

When a constituent changes, identify which relied-on condition changes and follow its receiving uses. Revised
notice time can invalidate a buffer's duration even when the buffer's measured capacity remains valid. A new
interface version can require qualification of an exchange without reopening unrelated ownership decisions.
Continue through affected dependencies until a compatible result or explicit gap bounds the consequence.
Retain unaffected claims and independent work.

For a selected fallback, establish the trigger, deciding authority, available means and bounded result before
relying on it. If continuing constituent evolution requires repeated selection during operation, arrange the
needed observations and decision authority with the operating practice. Automating that selection adds its
own qualification question. A single successful exercise does not establish the ability to manage every later
configuration or unannounced withdrawal.

#### SYSE.18:4.2 - Record the Result

| Field | Required content |
| --- | --- |
| shared use | Result or use, conditions, interval, affected Systems, current decision, and deciding Agent. |
| constituent Systems and relations | Actual Systems, configurations, other uses, reasons for inclusion, and one direct relation or stated gap for every relied-on contribution or constraint. |
| decisions and authority | Ownership and other governing relations, deciding Agents, assignments when relevant, authority, permissions, conflicts, escalation, and decision-centre boundaries. |
| commitments and interoperability | Commitments with bearers and conditions; interfaces, capacities, timings, actual exchange or use evidence, notice, withdrawal, and failure-recovery conditions. |
| alternatives and choice | Arrangements compared for the same result and interval; decisive conditions, whole burden and accepted losses; selected or conditional continuation, outside decisions, unsupported dependencies and next Work. |
| later integration, when current | Performing Agent, Method, dated Work, actual change or newly obtaining relation, resulting configuration, representative observation, and evidence limits. |
| decision use and reopen | Decision contribution supplied to next Work; separately supported observed-coordination claim when available; fallback, gaps, and conditions for reopening each affected claim. |

The first useful decision does not wait for implementation. Identify the earlier decision, performed Work, and
later observed-coordination claim separately. An observed coordination result does not establish that every
constituent commitment was fulfilled.

#### SYSE.18:4.3 - What Changes in Practice

Engineers can explain why a proposed arrangement could support the shared use, compare the available ways to
repair a failed connection, and identify which decisions and professional results each way still needs. The
receiving practitioner gets the reason for the choice and the condition that would change it. An unsupported
dependency has a specific consequence and next question; an already sufficient arrangement can be retained.

### SYSE.18:5 - Worked Case: Emergency Discharge Across Four Independently Governed Systems

This illustrative case concerns a district's planned emergency-discharge provision. The quantities, permissions
and engineering qualifications below are stipulated inputs for comparing arrangements; they are not field
measurements or a flood-control design supplied by this pattern.

Four existing Systems affect the use: a flood-pump station, an upstream gate, a municipal drainage network and
an emergency-dispatch System. Their respective owner, river-control agency, municipal operator and regional
dispatch agency control different decisions. The station integrator may install qualified station-side
equipment and use an already agreed dispatch escalation. It cannot change the gate envelope or the municipal
operator's commitments. The use requires accommodation of up to **50 m³/h** while preserving the supplied
hydraulic, discharge-quality and gate limits.

The municipal operator commits to notice received at the station at least four hours before a planned
interruption of drainage reception. The station's qualified fallback is ready no later than six hours after
receipt of that notice; this bound includes
dispatch acknowledgement and mobilization. The agreed dispatch response is already included in those six
hours, so invoking escalation cannot be counted as a second time saving. Unannounced outages require a
different contingency and lie outside this particular decision.

#### SYSE.18:5.1 - Derive and compare the alternatives

Consider the limiting permitted timeline: notice arrives four hours before municipal reception ends, and
fallback reception begins six hours after notice. The two-hour gap at the permitted 50 m³/h requires
**50 m³/h × 2 h = 100 m³** of storage to cover that case. This bounds the required coverage; actual demand
may be lower. It is not yet a qualified buffer design. For a varying flow, use the accumulated net inflow
over the unsupported interval.

A supplier offers an existing mobile buffer with **120 m³ of usable storage**, qualified for the stated
medium and connection. The supplied hydraulic assessment supports its inlet rate, location and recovery
path; the 120 m³ is available storage after its required reserves. It can be installed before the required
date within the station integrator's delegated budget. The fallback has qualified spare capacity to empty it
after hour 6 without losing the continuing 50 m³/h service. These are necessary specialist and provision
inputs; the volume calculation supplies none of them.

The same decision compares the following arrangements for the same service interval:

| Arrangement | Result under the stated premises | Authority, availability and burden | Present disposition |
| --- | --- | --- | --- |
| Retain the four-hour notice with no buffer | Cannot cover the permitted two-hour gap at 50 m³/h | Immediately available; cannot meet the required coverage | Excluded for this use. |
| Obtain six-hour notice | Could remove the unsupported interval with the current fallback | Municipal operator controls the change and cannot commit before the required date | Keep as a possible later improvement; it is unavailable for the current reliance. |
| Shorten fallback mobilization to four hours | Could remove the same interval | Current qualified Method needs six hours; no adequate shorter Method is supplied | Return the specific development or qualification need; do not assume faster dispatch solves it. |
| Install the qualified 120 m³ buffer | Holds the required 100 m³ and retains 20 m³ of additional usable capacity | Within the integrator's authority and date; adds hire, installation, inspection and later removal | Feasible for the declared use. |
| Narrow the offered discharge provision | May reduce the required storage or avoid the interval | The receiving authority has not accepted the lost coverage | A different result requiring a scope decision. |
| Stop the proposed service increment | Makes no unsupported service promise | Leaves the receiving need unmet | Retain if no admissible arrangement can be supplied. |

The buffer is selected for preparation because it is the only currently supplied arrangement in this comparison
that meets the required use by the date. Its extra cost and maintenance are accepted within the delegated
budget. The selection makes no claim that buffering is generally cheapest or superior to earlier notice.
An available six-hour notice agreement could reverse that choice by avoiding the buffer's burden.

#### SYSE.18:5.2 - Connect the decision to performance and a changed condition

The integrator explains the timeline and choice to station, municipal and dispatch participants. In their
walkthrough, dispatch initially describes acknowledgement as confirmation of the fallback's readiness. The
station team points to the six-hour mobilization: acknowledgement starts and tracks that work; readiness has
its own confirmation. They correct the receiving instruction and retain the agreed escalation for a missed
acknowledgement. The municipality's four-hour commitment remains unchanged.

The decision now authorizes the installation and its necessary qualification. It does not yet establish
installed availability. In the example's later performance, the team installs the buffer and completes the
required checks; a representative exercise under the stated load supports storage, transition to the fallback
and recovery. `SYSE.11` can use that configuration-specific evidence. The earlier decision, installation Work,
actual availability and observed coordination remain separately identifiable.

Now suppose the municipal operator proposes changing notice to **two hours**, with every other case premise
unchanged. The fallback still needs six hours from receipt. Required storage would become
**50 m³/h × 4 h = 200 m³**. The existing buffer's 120 m³ qualification survives, but it does not establish
support for this changed use. The integrator reopens the arrangement and the municipal decision; it cannot
authorize that operator's notice change. It may seek a larger qualified provision, an accepted narrower use
or another adequate arrangement. Until one is supplied, the changed service claim remains unsupported.
Unrelated gate limits and the original arithmetic remain usable within their original conditions.

If a subsequent occasion retains the original notice, flow, configuration and permissions, an adequate current
account can support the same bounded decision without another modelling project or exercise. Recheck a changed
or expired qualification when the receiving reliance requires it.

#### SYSE.18:5.3 - A different mismatch needs a different remedy

An order-fulfilment service uses an independent stock provider and payment provider. A compatible message
format does not settle whether a stock response reserves an item until payment completes. Following one order
exposes the dependency: stock may disappear between the response and the sale. Queueing the response does not
create a reservation. Compare obtaining a time-bounded reservation from the stock provider, a supported
confirmation-and-compensation arrangement, or a narrower service promise. Each needs its own operational
semantics, authority and evidence. If those means are absent, this Method returns that precise gap; the
drainage buffer offers no transferable guarantee of transactional correctness.

**When the full pattern is unnecessary.** Use ordinary architecture, configuration, integration and Work
patterns when one Agent controls every decision that can change the integration result. Reuse an adequate
constituent-coordination decision when the present use and its relied-on conditions are unchanged.

### SYSE.18:6 - Bias Annotation

Systems-of-Systems literature is influenced by defence, formal model federation, and software orchestration. Use
each source for the Method and case it actually studies. A cross-domain constituent classification, governance
form, representation, or integration Method needs its own evidence. Official attention and conformance describe
publications or declared rules; project use and effectiveness need evidence from performed Work and outcomes.

Compare several decision centres by their actual authority, operations, outcomes, and feedback. Distributed and
centralized arrangements can each help or harm; the label decides nothing.

### SYSE.18:7 - Conformance Checklist

- [ ] One shared use, conditions, interval, affected Systems, current decision, and deciding Agent are stated.
- [ ] Every constituent is an actual System included because its participation, output, failure, change, or
      withdrawal can alter the use.
- [ ] Each relied-on relation has its own predicate and participants; no umbrella contribution relation replaces it.
- [ ] Independence is stated for named decisions and relations, not as an absolute property.
- [ ] Every deciding Agent, assignment when relevant, authority, permission, conflict, and escalation is stated.
- [ ] Interface syntax is supplemented by configuration-bound exchange and use evidence where interoperability is
      claimed.
- [ ] Alternatives address the same receiving result or expose an accepted scope change; the comparison
      preserves protected conditions, competing uses, whole burden and unresolved premises.
- [ ] The selected continuation remains within the deciding Agent's authority and names outside decisions and
      unsupported dependencies. A conditional alternative is not relied on as an available fallback.
- [ ] Affected practitioners can recover the choice and its reasons for their own action; a material objection,
      missing resource or missing professional means receives its appropriate continuation.
- [ ] Any claimed coordination change identifies performing Agent, Method, dated Work, actual change or relation,
      configuration, representative observation, and evidence limits.
- [ ] The decision episteme, performed Work, world-side change, and observed-coordination claim are identified and
      grounded separately.

### SYSE.18:8 - Common Failures and Repairs

These recurring failures hide a relation, deciding Agent, or evidence boundary:

| Failure | Repair |
| --- | --- |
| *System of systems* is treated as a kind and explanation | Recover actual Systems, use-relative relations, and decision boundaries. |
| Participation is treated as parthood | State the direct relation and keep Work, capability, commitment, interface, resource, and evidence claims separate. |
| Interface syntax is treated as interoperability | Obtain configuration-bound evidence that results are exchanged and usable. |
| Agreement is treated as performance | Separate commitment, later Work, delivered result, and fulfilment evidence. |
| Integrator is assumed to own constituent decisions | Name each deciding Agent and authority; state which decision each blocker prevents. |
| Decision record is treated as coordination change | Perform authorized Work and identify the actual transformation or relation before claiming a changed condition. |
| Decentralized is assumed to be better | Compare decision centres, operations, outcomes, and feedback for this use. |
| Model federation is treated as physical integration | Separate description consistency, actual configuration, integration Work, and operating evidence. |

### SYSE.18:9 - Consequences

Distributed authority and unsupported dependencies become visible before integration fails. The integrating Agent
can make a bounded useful change within its authority. The conditions relied
on by the shared use and the monitoring Work needed to maintain them become explicit.

The cost is negotiation and maintenance of constituent claims. Keep the account focused on Systems that can
affect the shared use, and reopen only the claims a change affects.

### SYSE.18:10 - Rationale

Shared use depends on actual relations among Systems while authority and evolution remain distributed. Treating
every constituent as an owned component hides withdrawal and decision boundaries. Engineers can act through
named interfaces, commitments, buffers, and fallbacks. Separate decisions, Work, changes, and observations make
bounded integration possible.

### SYSE.18:11 - SoTA and Source Use

The professional question is how to choose a workable shared-use arrangement when constituent changes and
resources are controlled independently. This pattern selects a bounded comparison of consequences, feasible
configurations and independent decisions. It preserves useful current arrangements and develops only the
connection needed for the decision. The selection is conditional on that scope, not a claim of universal
effectiveness.

A serious alternative is a formal mission-configuration analysis. [Raz et al. 2024](https://doi.org/10.1109/JSYST.2024.3409231),
sections III–V, connect a mission description, spatial and temporal feasibility, and analysis of candidate
configurations. That connected construction is useful when several allocations and shared resources make
informal comparison unreliable. Their example is notional and the analytical choice remains domain-specific.
Section :4.1.2 retains feasibility before preference; it adds the independent authorization and provision needed
for the present engineering use.

For the four-System case, both approaches can expose the two-hour interval. The short timeline and comparison
already settle the current bounded choice with the supplied engineering results. A new formal model would add
construction and maintenance without a demonstrated change to this decision. The limitation is that this small comparison leaves wider combinations of interacting configurations
unexamined. Reopen this depth choice when multiple concurrent demands,
alternative constituent allocations or coupled changes defeat the inspectability of the small comparison.
Use the fuller analysis where its result can change the choice; a model still requires compatible source data
and its outputs do not grant a participant's permission.

The following contributions answer different parts of the problem:

| Source and question | Contribution used here | Retained boundary |
| --- | --- | --- |
| [Baldwin et al. 2024](https://doi.org/10.1111/psj.12518), context–operations–outcomes–feedbacks framework; [Papadopoulos, Tortola and Geyer](https://doi.org/10.1080/13597566.2024.2334470), online 2024, issue 2025 | Compare interacting decision centres, outcomes and adjustment, rather than preferring centralization or decentralization by label; :4.1.3–:4.1.4 retain the affected participants and returns. | Governance reviews do not supply a hydraulic design or guarantee beneficial distributed governance. |
| [Swickline, Mazzuchi and Sarkani 2024](https://doi.org/10.1002/sys.21727), model-federation contribution | Where constituent descriptions are separately maintained, preserve their source responsibility and compare compatible configuration claims before using them together. | The SysML/Cameo treatment supplies description integration; it does not establish installed interoperability. Use it for a material description problem, not as a prerequisite for the timeline case. |
| [Ashfaq et al. 2026](https://doi.org/10.1016/j.jss.2025.112661), runtime-composition review | Repeated operational reconfiguration needs its own arrangement and evaluation; :4.1.4 keeps that question distinct from one integration decision. | The computational literature contains several approaches and transfer gaps. Neither its prevalence findings nor a simulation establish field suitability or authorize autonomous changes. |

Reconsider a used claim when a relevant source correction, comparative result or observed use failure
changes its configuration, authority, outcome or transfer premise. Preserve useful unaffected contributions.

### SYSE.18:12 - Relations

- A compatible `SYSE.6` result supplies architecture constraints for the same shared use. Ground constituent
  participation, commitments, authority, and interoperability under their direct patterns.
- `A.1.SCR` governs actual System recognition; `A.22` governs selected structures; `E.18.NET` governs a
  transformation-flow network only when its members and relations are independently established.
- `A.6.P`, `A.2.2`, `A.2.8`, and `A.10` separately govern service wording, capability, commitment, and evidence
  claims.
- `A.2.1`, `A.2.8.PER`, `A.15.1`, `A.3.1`, `A.3.4`, and `A.15.PROD` govern assignment, permission, Work, Method,
  actual change, and production claims. Another Agent's decision authority still needs its own direct claim.
- A specialist practice retains its own decisions and authority—for example, Organization Change, Corporate
  Governance, Operations, Configuration, Maintenance, safety, security, law, finance, or contracting.
- `SYSE.11` can use a compatible observed-coordination claim for the same constituent Systems, configuration,
  shared use, and interval. Ground any later fulfilment or authority claim separately.

### SYSE.18:End
