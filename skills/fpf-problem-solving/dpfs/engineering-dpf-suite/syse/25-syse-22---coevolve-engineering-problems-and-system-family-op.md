## SYSE.22 - Coevolve Engineering Problems and System-Family Options

> **Status:** Stable

### SYSE.22:0 - Use This When

Use this pattern when an engineering project keeps improving one problem statement and one proposed System while
the situation around both has changed. For example, a new operating condition, affected-System consequence,
supplier limit, technology, or evidence result can make the old problem–solution pair obsolete even while its
backlog closes.

Begin with one observation or claim that can change the current engineering decision. Put the selected problem
record beside the System option it currently constrains. State the receiving decision and the claim within it that
would change—for example, an admission rule, comparison coordinate, affected-System consequence, evidence need,
or choice. If none changes, keep the observation without reopening this decision.

The first useful result contains these four parts:

1. the problem records selected for current attention and a separately retained problem archive;
2. actual Systems in current configurations and possible-future System-family specifications with their
   architecture, membership, and effectivity bases;
3. supported problem–option correspondences and unresolved mismatches; and
4. one replayable `ChoiceResult`: choose an option or tie-set, reject the current set, request one worthwhile
   probe, or refer the question to the decision and authority that can answer it.

An Agent makes the bounded choice under authority. A `DecisionSubject` states whose choice is represented.
Identify the performer and applicable authorization for any later experiment or implementation Work separately;
the deciding Agent may also perform that Work.

Use `SYSE.1`, `SYSE.16`, and `SYSE.17` first when project focus, operating environment, or affected Systems are
unclear. Use `SYSE.2` when one linked use-and-System concept is the immediate result, and `SYSE.6` when the problem
and option set are stable and only an architecture choice remains. Use `C.18` when the question concerns only an
archive or Front. A contested problem formulation may require a Decision Design Method;
a changed Method may require Method Engineering.

#### SYSE.22:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| problem situation | The world-side condition or relation that can frustrate an interest or intended use. |
| problem record | A `ProblemCard` episteme describing a problem situation or unresolved claim for one decision and period. |
| problem archive | Retained problem records, weak signals, alternative formulations, and stepping stones kept for possible later inquiry under a stated retention rule. This is an open content set governed by that rule. |
| selected problem portfolio | The finite set of problem records receiving attention, resources, or experiments in the current decision horizon. |
| actual System configuration | A world-side System and its obtaining configuration during a stated interval. |
| possible-future System-family option | A specification of a candidate member, variant, or configuration under a named family architecture, membership rule, and effectivity basis. |
| System family | A family relation among member Systems or possible-future specifications under explicit membership and effectivity rules. The family is identified through that relation rather than reclassified as another System. |
| exploration archive | Retained candidate descriptions and lineage kept under a stated exploration-value rule. |
| Front | A non-dominated set identified for one candidate set, admission rule, comparator or dominance relation, characteristic set, and date. |
| decision OptionSet | The finite set eligible for consideration in one current `C.11` choice under that decision's inclusion rule. Inclusion for a development or probe decision does not establish admission for operational use. Membership in an archive or Front supplies no automatic membership here. |
| problem–option correspondence | A supported claim stating how one option changes admission, comparison, consequence, evidence need, or next action for one selected problem. |
| experiment proposal | Possible-future content describing a bounded change and distinguishing observation whose expected decision value can be compared with its cost. |

### SYSE.22:1 - Problem Frame

Engineering problems and System concepts develop together. For example, an architecture can expose a
manufacturing constraint; a prototype can change what users consider possible; an operating failure can reveal
an affected System absent from the original scope; a new component can make a previously unaffordable option
feasible.

Five recurring confusions make that mutual development hard to manage:

1. a problem situation is confused with its `ProblemCard`;
2. a problem archive is confused with the finite portfolio receiving attention now;
3. an actual System is confused with a possible-future specification;
4. an exploration archive or Front is confused with the current decision's `OptionSet`; and
5. an experiment proposal is confused with authorized and performed experiment Work.

Keeping these distinctions lets the project preserve lineage while changing only the claims affected by a new
observation.

### SYSE.22:2 - Problem

The usual failure is a frozen pair: one backlog becomes *the problem* and one baseline becomes *the solution*.
Local optimization continues after a relevant condition changes—for example, intended use, environment, a
protected characteristic, a supplier condition, or the reachable System family.

Another failure retains many alternatives without their identities and rules. A single *portfolio* mixes records
of unlike kinds—for example, signals, problem formulations, architectures, configurations, experiment proposals,
and decisions. A moving Pareto Front then hides changes in its candidate set or comparator and appears to
demonstrate improvement across incomparable questions.

Reopening everything after every signal can add work without changing the decision. The project needs dependencies
and currentness conditions for individual claims so it can revise a problem without restarting unrelated Work.

### SYSE.22:3 - Forces

- Stable identities preserve evidence and decisions, while stale problem or family boundaries make that
  continuity misleading.
- Retained variants preserve stepping stones, while a project still needs finite current commitments.
- Shared family architectures reduce repeated Work, while one environment or affected System can require a
  distinct branch.
- Several options can remain non-dominated, while the next project move still needs a choice or probe.
- Novelty can open a useful region, while admission, safety, evidence, integration, and service constraints remain.
- Dependencies support selective reopening, while records that change no decision add maintenance cost.
- A local gain can move cost, risk, Work, or failure exposure to another affected System.

### SYSE.22:4 - Solution

Maintain a finite selected problem portfolio and a separately identified set of System-family options. Connect
them through decision-bearing correspondence claims, compare them under the current use and evidence, and end the
pass with one replayable choice or probe result. Observations from either side can then reopen the other without
discarding archives and lineage. A supported current comparison can remain usable while its carrier ages; neither
retention nor an unchanged receiving use requires a fresh trial.

#### SYSE.22:4.1 - Pattern-Use Unfolding

The Method uses eight recurring moves. They organize production of the account; problem-development, System-development,
research, realization, integration, operation, and decision Work can overlap.

1. **Decision boundary.** The Agent identifies the actual System or intended System referent selected for engineering, or the System family with its membership and effectivity rules. For a creator, retain the products or classes of future use whose demands and shared resources its options must serve. Current use, environment, affected Systems, configuration, horizon, resources, `DecisionSubject` and authority complete the boundary. Local realization and acceptance do not require calling the creator a new SoI.
2. **Situation and problem records.** The Agent separates the world-side occurrence or condition from assertions,
   observations, and evidence about it. Each selected `ProblemCard` states detection, problematic relation or
   unresolved claim, improvement check, constraints, affected Systems, evidence, receiving use, and the premises
   that make that evidence applicable. Include an expiry only where an actual qualification, right, resource or
   promised-use window ends; a review date alone does not invalidate the claim.
3. **Archive and portfolio.** Alternative formulations and weak signals remain in the archive under retention
   rules. The selected portfolio is finite and states why each record receives current attention or resources and
   what removes or reopens it.
4. **System-family options.** Actual Systems and configurations, candidate architectures, family membership and
   effectivity rules, and possible-future specifications are identified separately. Each option states what is
   realizable now and which builder or platform change it needs.
5. **Problem–option correspondences.** Every relied-on pair states the changed admission, comparison coordinate,
   protected characteristic, affected-System consequence, evidence need, or next action. A pair with no supported
   decision-bearing difference remains an unresolved mismatch.
6. **Plural comparison.** Archives, Fronts, and the decision `OptionSet` retain their own membership rules. The
   Agent compares several result and resource coordinates while retaining protected losses, uncertainty, and
   non-dominated alternatives. Do not force those coordinates into one scalar objective.
7. **Choice or probe.** The current `OptionSet` is fixed. The deciding Agent performs comparison-and-choice
   Work, applies `C.11.CRC` when a finite configuration-relative contribution comparison is needed, and applies
   `C.11` to produce a decision result: a choice, tie-set, rejection, named probe, or reroute. The Agent selects a
   probe only when its expected contribution warrants its full burden: participant and engineering effort,
   delay, foregone alternatives and displaced protective Work as well as direct expenditure. The performer,
   resources, access, authority and useful observation window must be available. An affordable discriminator is
   not by itself a worthwhile probe; a useful qualified result may stand without new observations.
8. **Later Work and selective reopening.** Assigned Agents plan, authorize, perform, and interpret later Work
   through the applicable relations. New observations reopen only the problem records, correspondences, options,
   Fronts, configurations, or decisions that relied on the changed claim.

##### SYSE.22:4.1.1 - Recover the changed engineering question

Use the eight moves above as a short reminder. The following explanation supplies their construction when the
problem and alternatives are not already available. The intended practitioner can interpret the project's
operating and configuration records and obtain the needed domain, production, service, and assurance judgements.
This pattern does not supply a missing compressor model, safety limit, or manufacturing process.

Start at the observation that made the old pair doubtful. Recover the earlier use claim and the System concept
that was supposed to support it. For one consequential operating situation, follow what happens from the
triggering event through the proposed behaviour to the effect on the user or another affected System. Use
`SYSE.2:4.3–4.6` for that linked construction; use an adequate existing result directly. The return needed here
is a use–concept pair with its conditions, any main uncertainty and failed or supported connection, not a complete
new concept study.

Identify what the observation changes. It may contradict the predicted effect, expose an omitted condition,
change the value of the effect, or make a new means available. These lead to different engineering questions.
For example, repeated network outages can change “minimize purchased peak power using cloud forecasts” into
“maintain occupied-building comfort during a demand reduction, including loss of network service.” The new
formulation retains the useful outside result and adds a condition that the old means did not meet. It does not
make reduced comfort acceptable simply because the incumbent cannot deliver it.

A new means can instead initiate the inquiry: a local controller may make coordinated short demand reductions
possible where only fixed schedules were previously affordable. Ask which use would benefit, what change in
behaviour could supply that benefit, and which operating condition could defeat it. Keep a technically
interesting challenge in the archive until there is a reason to spend current project resources on it.
`C.40.CD:4.1–4.5` supplies this general reciprocal development of a problem and a way; here the returned
question must bind an engineering use, family configurations and realization conditions.

Preserve the obligation or interest behind the earlier formulation. Distinguish correcting a mistaken
description, negotiating a different wanted result, and exploring a deliberately relaxed condition. A solution
to the relaxed question answers the original only if its result can be returned under the original condition.
When interests or authority remain contested, return that specific formulation question to the competent
decision participants. Do not hide it as a low score for a design variant.

The result of this inquiry is a revised problem record and a reasoned relation to its predecessor: retained
need with corrected conditions, a distinct new need, a superseded premise, or an unresolved disagreement.
That relation tells later engineers which earlier evidence still applies.

##### SYSE.22:4.1.2 - Construct family alternatives with a feasible common basis

Develop alternatives around the disputed connection. Change the allocation of behaviour, the physical or
computational means, the interface, or the operating arrangement when that could answer the revised question.
An alternative can retain the incumbent, vary a current member, add a family branch, change the shared
architecture, replace a previously assumed means, or stop pursuing this use. Creativity need not come from
one assigned role: production, service and domain practitioners can expose a better candidate through their
own constraints and available means.

For each promising alternative, recover what remains common and what must vary. State the retained
architectural commitments, permitted differences and dependencies between differences. Use `SYSE.13:4.1`
for variant, unit, configuration and effectivity identity. It supplies the distinctions and supported mappings;
the engineering work here determines which proposed combinations can meet this problem.

For example, local fallback, a different compressor, a larger processor and a network gateway are four design
choices, not four independent switches. The new compressor may require a different output board; the fallback
algorithm may fit only the larger processor; that board may lack an applicable test result. Build a candidate
by carrying these dependencies together. Reject an incompatible combination, retain a visibly conditional
combination for inquiry, or propose the missing interface or realization change. Do not count the Cartesian
product of independently feasible features as reachable family variants.

Retain more than one alternative when they answer materially different conditions or preserve a useful future
choice. Ask which differences change admission, value, burden or later reuse; do not expand every possible
parameter. A family boundary is itself revisable. If an option requires different functioning, support and
evidence assumptions from the shared architecture, compare a separate branch or family with extending the
common basis. Forced commonality can move repeated adaptation and service burden into every member.

This produces candidate specifications with explicit variation and compatibility rules. It does not produce
new actual Systems or establish that current installed units realize the specifications.

##### SYSE.22:4.1.3 - Test the join between use, variant and means of realization

A correspondence becomes useful when an engineer can follow why the variant could answer the problem.
For each relied-on pair, connect the outside result to the proposed behaviour, the required configuration,
the means of obtaining it, and the evidence the receiving decision needs. Use the supported realization branch
from `SYSE.3:4.2–4.4`, a platform result from `SYSE.12:4.1`, and the applicable `SYSE.10` evidence
assessment where these already answer the question. Open only the first unsupported result that can change
the decision.

The conditions must hold together. A candidate that fits one board, a test that covers another firmware
realization, and a service procedure for a third installation do not combine into one supported family option.
Likewise, separate statements that two trials can each use the only rig this week do not make their simultaneous
commitment feasible. Compare compatible configurations, conditions and receiving decisions, and check shared
capacity where the portfolio relies on simultaneous Work. Use `SYSE.20` when overlap or acceptance of a
partial result is the engineering question.

Keep two different conclusions visible. An option can deserve development attention while its operational
admission remains unresolved. A bounded experiment can be feasible even when its subject variant is not yet
admissible for ordinary use. State the scope of admission at the receiving decision; evidence sufficient to
select a probe does not become evidence that permits deployment.

Use a failed join constructively. If a variant cannot be tested within the existing arrangement, the result
may be a precise builder investment question for `SYSE.23`. If the proposed behaviour cannot supply the
required outside effect, return to the use–concept pair. If every candidate fails a protected condition,
reject the set or seek an authorized reformulation; ranking failed options cannot supply a successful one.

##### SYSE.22:4.1.4 - Let one side revise the other without losing the original need

Run the candidate forward far enough to reveal the consequential mismatch. A model, an existing comparable
case, a supplier answer or a performed trial can supply that result at its own evidential strength. Relate it
back to the problem before generating another variant.

| Result that changes the inquiry | Engineering revision | What remains to be established |
| --- | --- | --- |
| A candidate achieves the stated output but an occupant or service System is worse off | Correct the problem's consequence or protected condition; revisit dependent alternatives | Whether a replacement candidate satisfies the corrected use |
| A new means makes a previously unattainable use plausible | Add a use–concept pair and compare its worth with the selected portfolio | Actual demand, feasibility and admission; technical possibility alone supplies none of them |
| Different family members require incompatible assumptions | Separate their applicable conditions, introduce a justified branch, or change the family basis | Shared resources and cross-member consequences under the proposed arrangement |
| The target variant is plausible but its construction, evidence or support cannot be obtained | Keep its promise conditional and frame the limiting builder relation for `SYSE.23` or the obtaining question for `SYSE.24` | A compatible supported means of obtaining the result |
| A candidate disproves one interpretation of the problem but leaves another useful | Revise or retire the defeated claim and preserve the supported branch | The unresolved branch; a local failure does not erase independent evidence |

A better means may change which problem is worth current attention. Conversely, a revised problem may change
which retained design is useful. Preserve the decision-bearing reason for that movement. This is how an old
stepping stone can become useful again without treating its earlier rejection as an error or its archive
membership as current endorsement.

##### SYSE.22:4.1.5 - Compare complete alternatives and stop at a useful decision

Use one comparison situation per consequential operating profile, including the failure condition that reopened
the question. Compare complete candidates under the same profile and assumptions. Keep admission constraints
separate from preferences among survivors. If an option obtains its benefit only with an unprovided builder
change, include that change and burden in the comparison or keep the benefit conditional.

When profiles favor different members, the useful result can be a family rule assigning different variants to
different conditions, rather than one universal winner. Examine the shared consequence: supporting two members
may require extra configuration, spare parts, qualification or service Work. The cost of the portfolio is not
necessarily the sum of isolated variant estimates; common tools can save work while common scarce resources
can create conflicts. Do not claim family superiority from two separate local wins.

A revealing probe is worth selecting only if an obtainable outcome could change this comparison enough to
justify its full burden. The current result can also be enough to choose, retain a tie, reject, narrow or stop.
Use the existing decision account in `C.11`.

##### SYSE.22:4.1.6 - Pass the unresolved engineering question at its actual scope

The receiving work determines the next use of the joint account. A compatible use–concept pair can go directly
to architecture Work through `SYSE.6`; a supported member can proceed through its existing realization
arrangement. Use `SYSE.23` when the unresolved question is which change in the target or its builders is
worth making to enable later changes. Send the expected change family, blocked correspondence, current
configuration and realization basis, protected conditions, horizon and relevant uncertainty. The receiver
constructs its investment alternatives; the `SYSE.22` choice does not select an investment for it.

Use `SYSE.24` when the needed contribution is already clear and the remaining comparison is how to obtain it.
If the question instead concerns wider agreement about the problem, return that question to the relevant
problem-structuring or strategy practice. These are conditional result uses, not stages through which every
project must pass.

A builder improvement from `SYSE.23` returns as a changed feasibility premise only for the family options it
actually affects. An investment decision alone supplies an expected premise; a supported capability or
realization result supplies a stronger one. Reopen the corresponding comparison at that strength. This keeps
problem and means developing together without borrowing benefits from unfinished Work.

#### SYSE.22:4.2 - Record the Result

The joint problem–System-family account records these eight items:

| Result position | Required content |
| --- | --- |
| decision boundary | Project System or System family, membership and effectivity basis, current use, environment, affected Systems, configuration, horizon, resources, chooser, authority, and receiving decision. |
| situation and claim basis | World-side occurrence, condition, or unresolved possibility; separate assertions, observations, evidence, source, interval, and uncertainty. |
| problem archive and portfolio | Retained and selected problem records, their different membership rules, lineage, resources, applicable premises, stops and reopen conditions; actual expiry where a qualification, right, resource or promised-use window ends. |
| System-family options | Actual Systems and configurations, family identity, architecture, variant and effectivity rules, possible-future specifications, realizability, and builder dependencies. |
| plural-search results | Exploration archive and each Front with its candidate set, retention or admission rule, comparator, characteristics, date, and currentness. |
| correspondences | Every decision-bearing problem–option claim, its source and uncertainty, plus unresolved mismatches. |
| choice or probe | Fixed `OptionSet`, shared comparison basis, choice rule, probe budget and value when relevant, result permitted by the choice rule, reason, and overturn conditions. |
| continuation | Retained alternatives, planned and performed later Work when it occurs, receiving results, and selective reopen relations. |

#### SYSE.22:4.3 - What Changes in Practice

The project stops treating backlog items and design variants as two fixed columns. It can say which world-side
change reopened which problem–option pair, why a candidate remains in an archive but not the current decision,
and why the choice rule permits a choice, rejection, probe, or reroute as the next result.

### SYSE.22:5 - Worked Case: Heat-Pump Controller Family

In this constructed case, a manufacturer maintains heat-pump controllers for occupied apartment buildings. The current decision concerns
the controller family and a reversible building pilot. Installed controllers and a laboratory unit are actual
Systems; the options below are possible-future specifications under the family's architecture and effectivity
rules.

The earlier selected problem was peak electrical demand during cold mornings. The preferred specification used a
schedule optimizer and cloud forecast service. These three field observations now reopen the comparison:

1. several buildings lose network service during the coldest periods;
2. compressor cycling increases service calls in one installed configuration; and
3. a new tariff rewards short demand reductions but penalizes slow recovery that leaves occupants cold.

The current problem portfolio and System-family options produce four correspondence rows:

| Problem record | System-family option | Decision-bearing correspondence |
| --- | --- | --- |
| peak demand, now with recovery-time and occupied-temperature acceptance | cloud schedule specification | Network loss makes the option inadmissible without a qualified fallback; recovery time enters comparison. |
| network-loss continuity | local-fallback specification | Local forecasting can change continuity and recovery, but processor-load and fallback evidence are missing. |
| compressor cycling for the affected configuration | variable-speed-control specification and incumbent control | Variable speed can change cycling and energy use while increasing calibration and service burden. |
| speculative voice-control request, retained only in the archive | voice-gateway specification, retained only in the option archive | No current use or affected-System consequence gives this pair decision priority. |

The final row explains archive retention and current non-selection; it supplies no `OptionSet` member. The first
three rows are the complete correspondence set used by the current decision.

The earlier Front compared energy use and peak demand. The current comparison uses a new candidate set and the
following complete coordinate set: continuity, recovery time, occupied-zone temperature, peak power, compressor
cycling, processor load, calibration effort, and service burden. It is therefore a new Front with its own basis.

The fixed current `OptionSet` has three members:

1. continue developing the cloud-schedule specification;
2. develop the local-fallback specification; or
3. develop the variable-speed-control specification.

Safety and occupied-zone comfort are hard guards. The remaining coordinates form a partial order. The cloud-
schedule specification without a qualified local fallback fails the network-loss guard. The variable-speed option
retains the incumbent local control during network loss and remains admitted, but evidence about processor load
and cold recovery is missing for the local-fallback option. That option cannot yet be admitted or rejected.

The **controller-family council** is the deciding Agent. Its current assignment authorizes it to choose the next
engineering probe, or decline new probing on the present basis, and allocate no more than 160 engineering hours.
A building operations manager separately
authorizes any occupied-building trial; the product-family owner separately authorizes later adoption. The probe
choice grants neither authority.

The council uses one shared comparison basis:

- The fixed `OptionSet` remains cloud schedule, local fallback, and variable-speed control.
- The current `BeliefState` contains the three field observations, the hard safety and comfort guards, the cloud
  option's network-loss failure, the variable-speed option's admitted local control, and the missing local-fallback
  processor-load and recovery evidence.
- The `OutcomeModel` states how each possible probe observation changes admission and the survivor relation. A
  local-fallback pass admits that option and leaves it non-dominated with variable-speed control; a guard failure
  or processor overload rejects it. The current calibration uncertainty changes burden estimates for variable-
  speed control but does not change its admission or resolve the local-fallback question.

| Candidate next probe | Bounded burden | Distinguishing observations | Effect on the current decision |
| --- | --- | --- | --- |
| Scripted network-loss and cold-recovery trial | 96 engineering hours, two hardware-in-the-loop bench days, one three-day reversible building-pilot window, and about one week of decision delay. | In each of two representative building configurations: no safety violation; occupied-zone recovery inside 20 minutes; and controller processor load below 70%. An established safety or comfort guard failure, or processor load at or above 70% in either configuration, is a contrary outcome even if the other configuration passes. Incomplete, uncertain or otherwise non-decisive observations remain unresolved only when no such failure has been established. | A pass admits local fallback and leaves it with variable-speed control in the survivor set while cloud-only is rejected. A contrary outcome rejects local fallback and leaves variable-speed control as the admitted next-development option. An unresolved outcome preserves the unresolved local-fallback status and requires a new bounded decision. |
| Variable-speed calibration trial | 128 engineering hours, four calibration-rig days, the same single building-pilot allocation, and about two weeks of decision delay. | Calibration effort and service burden may fall or rise within the currently supported range; the trial does not observe network-loss recovery or local-fallback processor load. | Either bounded outcome refines the burden comparison for an already admitted option but leaves the local-fallback admission defect and survivor question unchanged. |
| No probe | No immediate trial resource use or delay; preserves the scarce pilot allocation and engineering capacity. | No new observation. | Retain the qualified current comparison: cloud-only fails the guard, variable-speed control remains admitted, and local fallback is retained only as an unresolved candidate, not admitted for use. Later development or adoption still belongs to its competent owner. |

The `ChoiceRule` compares obtainable probes with retaining the qualified current result. Changing admission or
the survivor relation is a possible contribution, not an obligation to buy it. In the first resource situation of
this case, the council's qualified judgement is that resolving the local-fallback option before the next family
investment is worth the 96 hours, scarce pilot allocation and one-week delay. Assume that capable performers and
the windows can be obtained, and that this allocation does not displace more valuable protective or development
Work. This value-and-feasibility premise, not the 160-hour ceiling, supports the choice. The calibration trial
cannot resolve that question. The deciding Agent applies `C.11` and records
`ChoiceResult-HPF-1 = probe_again` for the network-loss and cold-recovery trial.

In the paired resource situation, the same discriminator would consume the only pilot window needed for already
supported protective maintenance, or no competent performer can use it before the investment decision. The
council can decline that probe and retain the qualified comparison above. Local fallback stays unresolved; no
observation or safety assurance is invented. A later owner can make a supported bounded development choice among
admitted options.

In the selected-probe situation, after that `ChoiceResult`, a planning Agent must still prepare the trial plan, the building operations manager
must authorize the occupied-building trial, and assigned Agents must perform and interpret the Work. Family
adoption remains a separate decision by the product-family owner. If pilot authority is withdrawn before
the trial Work, a new decision pass records `reroute` and the missing authority without rewriting `ChoiceResult-HPF-1`.
Later observations reopen only the three current problem–option correspondences and dependent family results; the
voice-control archive entry remains unchanged.

For currentness, first keep the same configurations, relied-on observations, calibration, rights and supported
use while only the source export date changes: the comparison remains usable. Now change a controller
configuration so that the relied-on processor-load evidence no longer covers it, or let a real calibration or
pilot permission window end: reopen or suspend the affected use, not every claim in the source. Keep the needed
qualification with the comparison for later receivers; do not turn the first case into renewal Work. The case's
20-minute and 70% limits are receiving acceptance conditions, not universal thresholds supplied by this pattern.
Their protective basis and any proposed amendment require the relevant engineering judgement and authority;
merely choosing or declining a probe changes neither.

#### SYSE.22:5.1 - Construct the family account behind the probe and use its return

The heat-pump case starts with observations, not three fully formed alternatives. To obtain the specifications
above, the engineers first retain the outside need for acceptable heating and change the problem from
peak reduction alone to peak reduction with continuity and timely recovery. Following `SYSE.2:4.3`, they
trace the cloud command through the connection, local controller and compressor to the occupied-zone effect.
The trace exposes the missing behaviour during disconnection. Continuing with only a lower peak-power target
would leave that failure intact.

They then vary the means at the failed connection. One proposal adds an independently functioning local mode;
another changes compressor control while retaining the existing local protection. The cloud-only proposal is
kept in the comparison long enough to show why it fails the revised condition. Voice control does not repair
that connection and stays outside the selected portfolio.

For this constructed account, assume the larger processor is available only in two controller configurations,
and that the variable-speed compressor needs its matching output board. The option descriptions therefore
name those combinations and the effectivity proposal; they do not offer every feature on every installed unit.
The local-fallback option's conditional status is precise: a plausible configuration exists, but the current
decision lacks the load and recovery evidence that would permit its admission. The rig and occupied-building
window in §5 explain how that uncertainty could be resolved.

Now take the selected-probe branch and stipulate that the authorized trial is subsequently performed and
passes its stated limits in both configurations. The interpretation admits local fallback on that bounded
basis and preserves variable-speed control as a non-dominated alternative. It does not choose a release or
extend the observation to other boards. The family owner can now compare different members for their applicable
buildings rather than insisting on one universal controller. The problem portfolio remains the three selected
problems; the voice-control request is unchanged.

The next supplier-change inquiry reveals that producing and assuring more combinations with rig `R4` requires
repeated interface work. The returned `SYSE.23` question is specific: for the named controller family and next
supplier replacement, which target, rig and evidence changes would reduce that repeated work while preserving
the existing comfort and configuration limits? Local-fallback evidence supplies one applicable input; it does
not settle the supplier interface or evidence-reuse questions in `SYSE.23:5`.

**Changed condition.** Suppose a later building requires the smaller processor, on which the fallback algorithm
would exceed the same load limit. The passed trial remains valid for its two configurations. The revised family
account keeps the supported larger-processor member where applicable. The same fallback specification fails
the smaller-processor condition and is excluded for that use; it is not merely awaiting more evidence.
Incumbent local control can retain its previously supported use while a different algorithm or board is
considered for the unmet demand. The owner compares a separate branch's supply, configuration and service
burden with replacing the small board. Reclassifying the small-board building as “not a customer” would change
the problem scope and require its own grounds and authority; it would not demonstrate that the fallback solves
the original use.

This continuation explains the joint result of the Methods. `SYSE.22` changes which problem–variant pairs are
worth pursuing; `SYSE.23` can change the means and burden of reaching them. Either result can stand for its
own decision while the other remains unresolved.

### SYSE.22:6 - Bias Annotation

Watch for these six recurring biases:

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| requirements-freeze bias | The approved backlog becomes the permanently current problem. | Recover the world-side situation and the receiving claim's applicable premises, including real time limits; reopen only decisions affected by their change. |
| solution-fixation bias | Every observation becomes a modification of the incumbent design. | Reopen both problem formulations and family alternatives; admit a branch, replacement, or stop when supported. |
| archive-as-portfolio bias | Everything worth remembering receives current attention and budget. | Keep retention membership separate from current portfolio membership. |
| one-Front bias | Points from changed candidates or comparators are plotted as one improvement curve. | Identify each Front and its basis; make any cross-basis comparison separately. |
| novelty bias | A distant or AI-generated option is treated as useful or admissible by novelty alone. | State the reference set, admission rules, consequences, and evidence. |
| measurement maximalism | The project waits for field-wide prevalence or conclusive causal attribution before a reversible probe. | Use proportionate evidence with explicit uncertainty and limits. |

### SYSE.22:7 - Conformance Checklist

- [ ] The decision boundary identifies the actual System or intended System referent selected for engineering, or the System family; current use, environment, affected Systems, configuration, horizon, chooser and authority. For a creator, it retains the product-use grounds and bounded acceptance.
- [ ] World-side problem situations and `ProblemCard` epistemes remain separate.
- [ ] The problem archive and finite selected problem portfolio have separate membership rules.
- [ ] Actual Systems and configurations remain separate from possible-future specifications.
- [ ] Every option identifies its family architecture, membership or variant rule, and effectivity basis.
- [ ] Exploration archive, Fronts, and current `OptionSet` retain their own candidate and admission rules.
- [ ] Every relied-on correspondence changes a decision-bearing claim or remains visibly unresolved.
- [ ] The comparison preserves relevant result and resource coordinates, protected losses, affected-System
      consequences, uncertainty, and non-dominated alternatives.
- [ ] The choice or probe result states its basis, rule, full burden and value when relevant, actual obtaining
      conditions, authority, and reopen condition. Retaining a supported result is not conditional on a new probe.
- [ ] Proposal, planning, authorization, performed Work, observation, and later adoption retain separate results.

### SYSE.22:8 - Common Failures and Repairs


| Recurring failure | Repair |
| --- | --- |
| Backlog equals problem portfolio | Repair the selected `ProblemCard` values and state why each receives current attention. |
| Candidate specification equals future System | Keep the specification possible-future; state realization and later-test Work. |
| *Addresses problem* fills every correspondence cell | State the changed admission, coordinate, consequence, evidence need, or next action. |
| Archive equals Front | Preserve archive membership under its retention rule and Front membership under its comparator. |
| A changed Front is presented as improvement on the old Front | Identify both bases and make any cross-basis claim separately. |
| A probe choice is presented as family adoption | Identify later planning, authorization, Work, evidence, and adoption decision. |
| Every new source restarts the project | Trace the source claim to its receiving use and reopen only dependent results. |

### SYSE.22:9 - Consequences

The project can change both what it is solving and what Systems it considers without discarding lineage. Useful
stepping stones remain recoverable, stale comparisons become visible, and one bounded probe can be chosen while
the problem and System family remain revisable.

The cost is maintenance of identities and decision-bearing correspondences. Some cells remain unresolved, and
the best current result may be a probe, rejection, or reroute rather than a selected System variant.

### SYSE.22:10 - Rationale

FPF already supplies problem records, plural search, archives, Fronts, currentness, comparison, and choice.
Systems Engineering adds the action-changing specialization: selected problem formulations must be compared with
architecture- and configuration-identified System-family options under project use, operational environment,
affected-System consequences, realization limits, and engineering evidence.

The terms *problem factory* and *solution factory* describe different but corresponding Work and Method structures. The described Work can take place concurrently. Identify the Systems involved separately; use SYSE.20 when overlap or required order becomes the engineering problem.

### SYSE.22:11 - SoTA and Source Use

Engineering can revise problem formulations and System-family options together, including the Work and Methods used to develop them. Problem archives and portfolios retain material for later choices; comparison and acceptance use their stated bases. When the way of developing a System becomes the obstacle, the same inquiry can extend to its builders.


The source comparison matters to the choice of Method. NASA's currently provided [Design Solution Definition
guidance, §4.4.1.2](https://www.nasa.gov/reference/4-4-design-solution-definition/) already connects iterative
concept development, operating concepts, stakeholder expectations, technology maturity and enabling products.
Use a sufficient result from that practice directly. This pattern's additional work is the engineering
connection between a changing problem portfolio and configuration-qualified family alternatives: explaining
which combination is reachable, which use it can answer, and which changed premise reopens the comparison.

A competent product-line practice can already provide a variability model and a way of producing its members.
For example, the SEI [production-plan guidance](https://www.sei.cmu.edu/library/guidelines-for-developing-a-product-line-production-plan/)
describes how core assets are used to build a particular product. Retain that supported basis rather than
rebuilding it here. The remaining question in this pattern is whether changed use and realization conditions
require a different family option, problem formulation or current commitment.

The table names the sources used here and the contribution and limits of each.

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Dorst and Cross (2001), [*Creativity in the design process: co-evolution of problem–solution*](https://doi.org/10.1016/S0142-694X(01)00009-6) | Mutual development of problem and solution spaces in protocol studies of experienced industrial designers. | Use as bounded design-process evidence; establish the current System family and configuration separately. |
| Liker et al. (1996) and Sobek, Ward, and Liker (1999) on set-based concurrent engineering | Communication about design sets, delayed commitment, feasibility, and narrowing in automotive product development. | Transfer the set-based moves only where the receiving profile's constraints and evidence support them. |
| Castle, Stock, and Gorochowski (2024), [*Engineering is evolution*](https://doi.org/10.1038/s41467-024-48000-1) | Variation, expression, evaluation, selection, exploration, and exploitation as an engineering perspective. | Use the evolutionary analogy as a hypothesis source; ground the current engineering Method and cultural claims separately. |
| Zhang et al. (2025), [*Darwin Gödel Machine*](https://arxiv.org/abs/2505.22954) | An AI-engineering case retaining a lineage-bearing archive of coding-agent variants for later improvement. | Treat coding benchmarks as one application case; test transfer to physical Systems and causal claims separately. |

Reopen one source-use row when changed evidence alters its practical contribution or boundary.

### SYSE.22:12 - Relations

- `SYSE.1`, `SYSE.16`, and `SYSE.17` supply project focus, operational environment, and affected-System
  consequences for compatible uses.
- `SYSE.2`, `SYSE.6`, `SYSE.7`, `SYSE.10`, and `SYSE.13` supply linked concepts, architecture decisions,
  descriptions, evidence, and family/configuration/effectivity identity.
- `SYSE.15` can supply a compatible engineering-Method repertoire. `SYSE.21` can supply bounded observations of
  an enacted variant and its population; each claim keeps its own evidence and transfer boundary.
- `C.40.CD:4.1–4.6` supplies the general reciprocal development of a question and a way; `SYSE.22:4.1.1–4.1.6` binds its use here to family compatibility, realization and receiving decisions. `SYSE.2:4.3–4.6` supplies the linked use–concept construction, and `SYSE.3:4.2–4.4` the realization branch.
- `C.22.2` governs `ProblemCard` epistemes and `C.22.PFR` any world-side `ProblematicForRelation`. `C.17`, `C.18`,
  `C.19`, `G.5`, and `G.11` govern characterization, archives and Fronts, live pools, selected sets, and
  use-qualified currentness. `SYSE.19` and `SYSE.23` retain changed-premise and claim-specific receiving rules.
- `C.11.CRC` governs finite configuration-relative contribution comparisons and `C.11` the bounded choice.
- Supply the project focus, selected problem portfolio, System-family option set, correspondences, unresolved
  mismatches, and current `ChoiceResult` from `SYSE.22` to the Agent using `SYSE.23` for an investment or
  reconfiguration decision.
- Feedback reopens `SYSE.2`, `SYSE.6`, or `SYSE.13` only when the changed result crosses their stated reopen
  condition.
- Decision Design, Strategy, Method Engineering, and Operations Management retain their
  domain Methods even when their Work uses the same archives or decisions.

### SYSE.22:End
