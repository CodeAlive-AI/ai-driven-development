## SYSE.23 - Choose What to Change So Later System Changes Become Easier

> **Status:** Stable

### SYSE.23:0 - Use This When

Use this pattern when an engineer or manager says that a product or product family must become *more
evolvable*, but the next change is still slow, expensive, unsafe, or hard to assure. The limiting condition may
be in the project system-of-interest, its family architecture, a builder or enabling System, an engineering
platform, a Method, an Agent's capability, the Work that enacts a change, or a relation among them. Calling all
of these *the system* hides both the present difficulty and the architecture change worth funding.

Here, the **builder arrangement** comprises the named Systems, Agents, Methods, Work, services, configurations,
and direct relations used to make, change, verify, release, or support the project system-of-interest for the
selected future-change family. An account of that arrangement identifies each participant and relation.

The first useful result has three parts:

1. a grounded account of the project system-of-interest and its builder arrangement that keeps five claim kinds separate: characteristics of obtaining selected
   structures, capabilities of named holders for named Work, results and resources of change-Work occurrences,
   claims about a joint arrangement with named participants and relations, and supported causal or contribution
   claims;
2. separate specifications of possible-future selected structures for the project system-of-interest and builder arrangement, including the
   genuine holonic levels, non-holonic dependencies, and Work relations that matter to the decision; and
3. one replayable `ChoiceResult` for a bounded investment or reconfiguration.

**First move.** Name one class of future change the project expects to make: for example, add a sensor variant,
replace a supplier component, adapt to a new operating environment, reuse evidence across configurations, or
change the release Method. State the available basis: actual observations where available, otherwise the
qualified model or estimate supporting the prospective account. Distinguish what is observed, estimated and
unresolved. Classify each claim: does it concern an architecture characteristic, a holder capability, a result
or resource of change Work, a constraint in the joint arrangement of the project system-of-interest and
builders, or a supported or suspected contribution? Keep obtaining structures and actual Work separate from
proposed structures and expected results. If the sentence still says only *the system is hard to change*,
the decision is not ready.

In practitioner-facing prose here, an **Agent** means an admitted System considered in an agent role, with
enough agency for the named decision or Work, scope, and period; `A.13` supplies the underlying agency result.
System identity, local system-role classification, capability, assignment, authority, and actual performance
remain separate claims. `C.11` uses `DecisionSubject` for the person, team, organization, or other collectivity
whose choice is recorded.

Use `C.25` when the immediate task is to repair one composite quality claim. Use `C.30` and `C.32` when the
immediate task is to characterize or choose one architecture independently of the relation between the project system-of-interest and builder arrangement. Use
`SYSE.6` when the current option set concerns only the engineered-System architecture. Use `SYSE.12` when the
practical result needed is one engineering-platform service. When the needed change is primarily organizational
or concerns human capability, use the relevant Organization Change Engineering or Human Capability Development
DPF result when available; otherwise name the specialist help needed and use a qualified source. Use `SYSE.21`
when cultural continuation is the current question.

#### SYSE.23:0.1 - Short Practitioner Use

For a first pass, use one expected change family and one decision horizon:

1. State the change to be made, the project system-of-interest when it already exists or the intended-system
   claim when it does not, the configurations affected, the horizon, protected consequences, resources,
   `DecisionSubject`, chooser granularity, and authority.
2. Classify each current claim before assigning a quality bearer. Separate architecture characteristics, holder
   capabilities, change-Work results and resources, joint-arrangement claims, and causal or contribution claims.
3. Recover three structures when they matter: genuine part–whole or membership levels with their scale and
   cross-level conflicts; non-holonic dependencies or service relations between the project system-of-interest and builder arrangement; and first–then or
   overlapping Work.
4. Keep obtaining architecture relations and current observations separate from specifications and expected
   characteristics of possible-future structures.
5. Develop alternatives that change different selected structures of the project system-of-interest or builder arrangement. Show how each alternative
   changes option reachability, change cost, assurance, rollback, and displaced burden.
6. Compare the finite changes through `C.11.CRC`. Then carry the full `C.11` decision record: stable
   `OptionSet`, shared comparison basis, `ChoiceRule`, probe cost and value when relevant, and one
   `ChoiceResult` permitted by that rule.
7. Plan, authorize, perform, and observe the chosen change separately. Later Work can support or defeat the
   earlier claims; the decision record does not make the architecture change occur.

This attention order is not a universal Method unfolding. Development of the project system-of-interest,
development of its builders, platform service, Method change, evidence Work, and capability development can
overlap, recur, or remain separate Work wholes.

### SYSE.23:1 - Problem Frame

An engineered System does not become easier to evolve in isolation. A replaceable module may still require a
fixture the factory lacks. A configurable product family may outrun test and evidence reuse. A simulation
platform may generate variants that manufacturing cannot build or service. A flexible Method may depend on
skills, permissions, or data that the assigned Agents do not have. Conversely, a costly redesign of the project system-of-interest
may add little when the actual bottleneck is a slow builder or unavailable test service.

*Evolvability* is therefore an entry word, not a ready-made scalar or one universal quality bearer. An
architecture-characteristic claim concerns an identified selected structure of a System, family relation,
platform, or Method. A capability claim concerns a named holder and target Work under stated conditions. Lead
time, rework, defects, and consumed effort may be results or resources of bounded change Work. A claim about the joint arrangement of the project system-of-interest and builders identifies its participating Systems, Methods, Agents, and relations. A claim
that one architecture change caused or contributed to a Work result needs its own support. These claims may be
compared, but they do not become the same kind.

The structures also differ. The project system-of-interest and a builder System can each have genuine
constructive part–whole levels. Actual family members can participate in a membership structure. A component-
level change can create a simultaneous whole-System or family-level conflict. Those are genuine level claims
only when the part–whole or membership relation, scale, and horizon are stated. A dependency between the project
system-of-interest and builder arrangement, a provider relation, or a platform service is non-holonic unless
another relation establishes otherwise. Build-the-builder Work
that precedes testing of the project system-of-interest is temporal Work order, not a level.

### SYSE.23:2 - Problem

The first failure assigns every evolvability quantity to an unnamed *system*. Evidence from one software
module, prototype, team, or change occurrence is then reported as a characteristic of the product family,
factory, engineering platform, Method repertoire, organization, and culture. No one can tell whether the claim
concerns architecture, capability, Work performance, a joint arrangement, or causal contribution.

The second failure chooses a familiar mechanism before the claim subject is known. Mechanisms such as modularity, standard interfaces, automation, digital twins, feature flags, AI coding,
continuous delivery, or reusable tests are treated as universal answers. Each can help one change family and damage another through latency, coupling,
option loss, verification load, supplier dependence, configuration growth, security exposure, or maintenance
burden.

The third failure describes a desired architecture as if it already obtained. A roadmap contains a configurable
platform and automatic evidence reuse, so current lead-time claims are calculated from those possible-future
features. The investment decision then uses benefits that only the investment could create.

The fourth failure demands open-ended improvement without a bounded horizon or stop. Candidate generation grows,
but admissibility, integration, safety, cost, environmental consequences, and selection do not improve. More
variants become more inventory and assurance debt.

### SYSE.23:3 - Forces

The recurring tensions are:

- **Reachability and control.** More admissible variants can preserve future options, while uncontrolled variation
  increases configuration, integration, safety, and service burden.
- **Modularity and system performance.** Looser coupling can localize change, while added interfaces, indirection,
  mass, latency, or duplicated capability can damage current performance.
- **Gain in the project system-of-interest and builder debt.** A shortcut in the project system-of-interest can deliver one increment quickly while making later
  manufacturing, integration, evidence, or maintenance Work harder.
- **Platform reuse and local difference.** A shared platform can reduce repeated Work, while forcing unlike
  profiles through one service can erase constraints that matter.
- **Change speed and evidence continuity.** Small reversible changes shorten feedback, while assurance and
  configuration evidence must still refer to the changed System and use.
- **Automation and authority.** AI and robotic Agents can generate, implement, or test more variants, while
  assignment, review, permission, release, and responsibility remain separate.
- **Exploration and exploitation.** A project needs alternatives and stepping stones, while a current decision
  needs a finite budget, protected losses, and a stop condition.
- **Project intervention and cultural continuation.** One successful reconfiguration can justify local use, while
  it does not establish discipline-wide selection, prevalence, or retention.

### SYSE.23:4 - Solution

Classify the current claims before deciding what should change. Recover the obtaining structures of the project system-of-interest and builder arrangement, including genuine
levels where they matter. Keep their non-holonic relations separate from temporal Work structure. Specify possible-future structures separately, compare materially different
investments against the current arrangement, and return one replayable architecture `ChoiceResult` whose later
consequences can be observed.

**Local mantra.** An expected change exposes a current difficulty. The team identifies whether the difficulty is
an architecture characteristic, capability limit, change-Work result or resource, joint-arrangement constraint,
or suspected contribution. Several views show genuine levels, dependencies between the project system-of-interest and builder arrangement,
and Work order or overlap without merging them. Alternatives that change either side are compared from one current
basis. A bounded choice is recorded; later Agents perform Work and supply observations.

#### SYSE.23:4.1 - Perform the Move

1. **Bind the future-change question.** Name what the decision concerns. When the designated project
   system-of-interest already exists, cite a compatible `SYSE.1` result and the plan or decision that designates
   it. When the System is still intended, keep its designator and expected change or use in a WorkPlan, decision,
   System description, or other claim episteme until identity inception. When a System family is in scope,
   identify the family, its actual member Systems, possible-future specifications, membership relation, and
   effectivity basis without calling the family another System. Add current configurations, expected change
   family, use, environment, affected Systems, horizon, frequency or scale of change, protected characteristics,
   resource limits, receiving decision, `DecisionSubject`, chooser granularity, and authority. The expected
   changes must be concrete enough that an engineer can tell what counts as admitted, completed, failed, or out
   of scope.
2. **Classify the claim before naming its subject.** Use one of five working forms:
   - an architecture-characteristic claim about an identified selected structure and its bearer;
   - a capability claim about a named holder, target Work, conditions, and evidence;
   - a result or resource claim about a bounded change-Work occurrence or a declared class of comparable Work;
   - a claim about a joint arrangement with the named project system-of-interest, builder Systems, Methods, Agents, and direct relations; or
   - a causal or contribution claim that connects a changed structure or capability to a later result.
   Identify the world-side subject independently. Treat descriptions, role labels, organization charts, Method
   accounts, and dashboard rows as epistemes or presentation elements used by Work.
3. **Qualify each claim on its own basis.** For an architecture characteristic or `C.25` quality bundle, state
   the bearer, selected structure, change family, scale, reference scheme, window, constraints, mechanism,
   evidence, uncertainty, and material limits on use. For capability, state holder and target Work. For
   change Work, state the Work occurrence, enacted Method, result and resource coordinates, configuration, and
   conditions. For a joint arrangement, state participants and relations. Keep causal contribution separate
   from co-occurrence, sequence, and correspondence. Do not compare claims that use different subjects, change
   families, scales, or horizons without a declared comparison relation.
4. **Recover three different structures.** For each view, state its `EntityOfConcern`, relation type, scale,
   horizon, and decision use.
   - In the **holonic or membership view**, identify constructive parts and wholes or actual family members.
     Record simultaneous cross-level conflicts when a local change improves one level while burdening another.
   - In the **system-of-interest–builder relation view**, identify the direct dependencies, correspondences,
     provider, service, interface, or enabling relations used by this decision. Do not infer part–whole from dependence.
   - In the **Work view**, identify first–then, overlap, concurrency, and recurrence among Work occurrences. Do
     not infer a level from earlier Work.
   Leave a view unused when it cannot affect this decision.
5. **Separate current facts from possible-future specifications.** For every proposed change—for example, a
   module boundary, interface, product-family rule, fixture, test service, automation, Method change, or provider
   arrangement—write a possible-future architecture specification and the later Work and observation needed to establish it.
   Keep expected characteristics separate from current readings.
6. **Find the constraining relation and its evidence.** Ask which proposed change to the project system-of-interest is unreachable, too costly, too slow, too hard to
   assure, or too hard to roll back under the current builder arrangement. State the selected structure of the
   project system-of-interest, the builder structure or service, their direct relation, the affected result,
   evidence, uncertainty, and moved burden. When a causal contribution is needed, state the mechanism and the comparison or intervention basis;
   do not promote co-occurrence or earlier order into causation.
7. **Develop alternatives on both sides.** Include the incumbent and materially different changes such as a
   boundary or interface of the project system-of-interest, family configuration rule, builder fixture or manufacturing cell, test
   and evidence platform, release Method, supplier arrangement, or a change spanning both sides. In product–production cases,
   include production-process and production-System reconfiguration when they constrain product-family change
   across generations. State which selected structure each alternative changes and which constraints it leaves
   untouched.
8. **Compare finite changes.** Use `C.32.ACS` to choose a few optimization indicators and monitored guardrails
   with their actual claim subjects and scales. Apply `C.11.CRC` to each realizable finite change relative to the
   current configuration of the project system-of-interest and builder arrangement. Preserve result and resource vectors, implementation Work,
   interactions, uncertainty, reversibility, future-option effects, and displaced burdens. Do not score possible
   option reach as an already realized operating result.
9. **Return a replayable investment choice.** Freeze the viable `OptionSet`. State one shared preference order
   or evaluative measure, `BeliefState`, and `OutcomeModel`. When another probe is live, state its action set,
   budget, cost, and expected decision value. Apply one `ChoiceRule` and emit one `ChoiceResult` from the current `C.11` result set: choose the incumbent or a change to the
   project system-of-interest, builder arrangement, or both; retain a tie-set; reject the current set; request a
   probe; or reroute and end this decision pass because the question, authority, or needed input lies elsewhere.
   Record protected losses, budget, dependencies, why the `ChoiceRule` permits this result, and overturn conditions. The choice may issue an
   implementation request, but it does not authorize or perform the change.
10. **Realize and observe separately.** Assigned Agents later perform separately identified Work that changes the project system-of-interest, a builder
    System, platform, Method, or organization arrangement under its own authority and enacted Method. Observe
    representative future changes through measures relevant to this decision—for example, reachability, lead
    time, rework, defect introduction, evidence reuse, rollback, consequences for the project system-of-interest,
    provider burden, or newly exposed constraints. Revise only the claims and architecture decisions that the
    observations support or defeat. Send human capability demand to Human Capability Development and cultural-continuation
    evidence to `SYSE.21` rather than hiding either inside an evolvability score.

##### SYSE.23:4.1.1 - Make the future change concrete enough to diagnose

The short move above starts with an expected change family. Construct that input from a current use need,
a supported `SYSE.22` correspondence, a supplier or operating change, or a recurring difficulty in actual change
Work. Do not begin with “adopt microservices” or “buy a digital platform”; those already select a means.

Describe a representative change as a difference between two usable configurations under stated conditions.
Name the changed behaviour or interface, the members or installations affected, the result needed from the
changed System, and how successful completion would be recognized. Include the configuration that must continue
to operate during transition. A supplier replacement, a network-loss mode and a different service environment
are different scenarios even when all are called “add a variant.”

Select scenarios that could distinguish the investment alternatives. A near-term change can expose present
burden; a consequential different change can reveal whether the proposed mechanism generalizes; a protected
operating or recovery condition can expose its unacceptable loss. Give projected frequency or scale only when
there is a basis for it. When future demand is uncertain, compare the investment under several plausible
demands and say where the preference changes.

The question can be narrower than general evolvability: “make the next supplier replacement possible while
six released configurations remain supportable.” If that is the present need, a general platform may be
unwarranted. If the source is a `SYSE.22` probe result, preserve exactly what it settled. A pass for local
fallback in two configurations does not establish compatibility with a new compressor supplier or justify
cross-variant evidence reuse.

##### SYSE.23:4.1.2 - Trace what has to change and why

Work one scenario through the current arrangement. Begin at the proposed change in functioning, configuration
or interface and ask what must be revised, reproduced, obtained, checked and supported for the result to become
usable. Follow the action-changing dependencies across target parts, descriptions, production means, tests,
release and service. Use the realization branch construction in `SYSE.3:4.2–SYSE.3:4.4` rather than reconstructing
a complete builder hierarchy. A branch can stop at an adequate supplied result.

Explain each consequential propagation. A new protocol may require an adapter because its timing differs;
an evidence result may need renewal because its configuration basis changed; a rig may require requalification
because its emulator now represents a different physical response. Check timing, failure behaviour and support
demands even when the interface name is unchanged.

Distinguish two mechanisms that often get mixed:

- **Change propagation:** modifying one description, interface or implementation requires compatible changes
  elsewhere before the new configuration can be used.
- **Operational propagation:** a disturbance or failure in one part affects another during use.

A boundary can reduce one propagation while worsening the other. An adapter may localize future firmware
changes yet add response delay or another failure mode. A shared test service may reduce duplicated setup
while making several projects depend on its availability. Retain both consequences where they matter.

For every apparent bottleneck, compare the required contribution with what the current arrangement supplies.
A slow task can result from intrinsic technical work, repeatable setup, waiting for a shared resource,
missing capability, unresolved authority or unavailable evidence. Each suggests a different intervention.
The number of touched modules and elapsed time of one change are observations, not a causal decomposition.
Use the five claim kinds in §4.1 to keep the supported constraint distinct from the suspected explanation.

The useful intermediate result is a small set of constraining relations and their effects on the chosen
scenarios. It can be written directly on the existing architecture or realization account: what change demands
what contribution, why, from which System or performer, under which condition, and with what support or gap.
Do not model an entire organization when one interface and rig correspondence decides the question.

##### SYSE.23:4.1.3 - Construct mechanisms on both sides of the constraint

For each limiting relation, ask which premise an intervention could change. Keep the incumbent as the common
basis and construct materially different responses. The following alternatives illustrate how to reason.

| Limiting relation | Change to consider | Why it could help and what it can worsen |
| --- | --- | --- |
| A supplier difference propagates into several target parts | Stabilize a boundary and place the varying behaviour behind an adapter | Localizes some later changes; adds translation, interface qualification and possible run-time cost |
| Target differences are manageable, but every variant needs a new setup | Reconfigure or parameterize the production or test means | Reuses setup and description-to-configuration relations; creates parameter validation and provider maintenance Work |
| A common asset forces unrelated members to change together | Separate a justified branch or accept bounded duplication | Reduces coordinated change; increases maintenance, stock, evidence and eventual reconciliation burden |
| Configuration differences repeatedly invalidate evidence | Change the family rule and the evidence argument together | Can make qualified reuse explicit; no identifier or automation by itself establishes that the earlier evidence applies |
| Suitable technical means exist but practitioners cannot obtain a usable result | Change access, service provision, Method, support or assignment under its proper authority | Can remove waiting or missing support; may move burden to another provider or demand capability development |
| The next change is singular and the retained architecture remains adequate | Make a local adaptation, defer generalization, or retain the incumbent | Avoids speculative investment; can leave later changes expensive or foreclose options if the commitment is irreversible |

Derive an alternative through the complete scenario. A target-only change is insufficient when the unchanged
rig cannot represent the new behaviour. A builder-only change may work by accepting wider test and maintenance
Work. A mixed change can reduce that wider burden, but it adds migration and coordination. Demonstrate those
differences; the label “mixed” gives no presumption of superiority.

A builder can itself need a new fixture, Method, service or qualified performer. Apply `SYSE.3:4.4` to that
specific unresolved branch. Recursion ends when a compatible supported means is available, an attainable
next inquiry is selected, or the investment is rejected or narrowed. It does not require developing every
builder anew.

When architecture and team responsibilities must change together, involve the affected practitioners in
the same technical reasoning. Explain the constraint that failed, the proposed boundary, what later decisions
are fixed or still open, and the evidence that would overturn the proposal. Ask the production, test and service
contributors to carry the scenario through their work and return an incompatibility they can substantiate.
Organization redesign, assignments and authority still need their own decisions and Methods.
`SYSE.6:4.1` supplies the architecture decision's fixed/open constraints and receiving uses.

##### SYSE.23:4.1.4 - Compare the transition as well as the possible future

An investment is useful only if the proposed arrangement can be reached and then used. For each serious option,
identify a viable transition from the current configuration through any necessary coexistence to the intended
arrangement. State which current service or production must continue, what can be taken out of use, what must
be qualified before reliance, and what can be restored if the change fails. A physical change may require
rework or replacement rather than an instantaneous rollback.

Examine the required contributions together. The controller boundary, rig adapter, evidence mapping and
service procedure must agree on the same variant and interface semantics. Their readiness must fit the needed
window. If the same engineer or facility supplies several contributions, compare the joint demand with its
available capacity. Separately feasible plans cannot be added when they spend the same exclusive resource.
`SYSE.20` supplies reasoning about overlapping Work and usable partial results; `SYSE.13` supplies the
configuration and effectivity basis.

A staged investment can be preferable: first isolate one boundary and qualify its matching rig slice, then
generalize only if a further change demonstrates sufficient reuse. For such a proposal, say what useful result
the first commitment produces even if later expansion stops. Retain the incumbent where coexistence is
necessary and affordable. Do not use expected capabilities of the finished platform to justify reliance during
its own construction.

This comparison also exposes complementarity. Suppose an adapter alone cannot reduce release burden because
the rig and evidence account still require a full rebuild; rig parameterization alone cannot localize that
rebuild because the target remains coupled. Their joint change may remove the constraint. Count that joint
benefit once. Conversely, removing one constraint can expose another, such as review capacity or service
commissioning. Carry that remaining constraint into the alternative rather than reporting a whole improvement
from the first local gain.

##### SYSE.23:4.1.5 - Judge future benefit against commitment and continuing burden

Compare each alternative for the same change scenarios, horizon and current arrangement. Keep current
implementation and transition Work, recurring operation and maintenance of the new means, later target-change
Work, and displaced protective Work visible. Use a single quantity only for genuinely commensurable terms;
safety, comfort, evidence strength and option reach do not become hours or money by being in the same table.

For a bounded effort comparison, suppose equivalent admissible changes currently require 60 engineering hours
each. A proposed means requires 240 hours to establish and 16 hours per later change. Under those stipulated
conditions, with all differing effort included in those terms, its total is lower only when
`240 + 16n < 60n`, hence at six or more changes. At five, the totals are 320 and 300 hours. This calculation
does not establish that six changes will be needed, that the effort estimates are supported, that other
characteristics are equal, or that the transition fits the calendar. If recurring provider maintenance,
qualification or adaptation differs, add those contributions before using the comparison.

When the benefit is preserving an option rather than saving repeated effort, name the future change that
would otherwise become impossible or costly, the mechanism keeping it available, its carrying burden, and the
event that makes it worth exercising. A reversible first commitment can be preferable under uncertainty.
An unused option is not a realized operating gain, and preserving every imaginable option is not free.

Select one worthwhile additional observation only when it could change the choice. A model can settle a
known resource bound; it cannot establish the service team's ability to use a new commissioning procedure.
A trial can reveal an integration difficulty; it need not justify a general causal claim. Use `SYSE.10` for
what the result supports and `C.11.DUA` when further inquiry's value is uncertain. A qualified decision to
retain the current arrangement is a substantive outcome.

##### SYSE.23:4.1.6 - Make the choice usable and learn from its actual consequences

The investment result names both what should change and which later change it is meant to enable. Give the
receiving architect, platform provider or realization performer the selected constraint, intended result,
accepted loss, unchanged protections, unresolved input and reconsideration condition. Use `SYSE.24` if a
needed fixture, service or other result can be obtained in materially different ways. Use `SYSE.12` for the
platform's supported readiness and later observed-use account. Neither replaces this investment comparison.

In the resulting Work, observe the connection the investment was intended to improve. If the boundary localized
the target change but the rig still required a full rebuild, one expected benefit failed. If change effort
fell because an expert supplied unplanned help, retain the observed effort and help while qualifying the
claim about the new means. Compare later change occurrences only to the extent their configurations, demands
and support are comparable. A small observation can justify local correction without establishing the
cause of a profession-wide trend.

Return a changed feasibility or burden premise to `SYSE.22:4.1.6` only for the problem–option correspondences
it affects. Return an architecture constraint to `SYSE.6`, a failed realization dependency to `SYSE.3`, or
a platform-use failure to `SYSE.12` when that is the precise receiver. If the intended future changes no
longer matter, reconsider the investment's purpose before optimizing the builder further. If the arrangement
is being copied and retained beyond the project, use `SYSE.21` for that different cultural question.

#### SYSE.23:4.2 - Record the Result

Record the following content for the stated decision using linked descriptions. Keep the different claim kinds,
decisions and observations distinguishable; each claim keeps its own subject and scope. Include view-specific
content only for views used in this decision.

| Account content | What to record |
| --- | --- |
| decision boundary | Project system-of-interest when it already exists, or the intended-system claim when it does not; any System family with its membership and effectivity basis; configurations, expected change family, use, environment, affected Systems, horizon, scale, protected characteristics, resources, `DecisionSubject`, chooser granularity, authority, and receiving decision. |
| current claim inventory | Claim kind; identified subject; architecture bearer and selected structure, capability holder and target Work, change-Work occurrence and its result/resource coordinates, or joint-arrangement participants and relations; scale, window, evidence, uncertainty, and material limits on use. |
| holonic or membership view | `EntityOfConcern`; obtaining part–whole or actual-member relations; decision-bearing levels; scale and horizon; simultaneous cross-level characteristic conflicts. |
| system-of-interest–builder relation view | `EntityOfConcern`; selected structures of the project system-of-interest and builder arrangement; the direct dependency, correspondence, provider, service, interface, or enabling relations used by this decision; consequence, moved burden, evidence, uncertainty, and unsupported causal claim. |
| Work view | `EntityOfConcern`; Work occurrences, performing Agents, enacted Methods, first–then, overlap, recurrence, required order, and separately obtaining assignment and authority. |
| possible-future specifications | Proposed selected structures and mechanisms, expected characteristic changes, required realization and evaluation Work, assumptions, and failure conditions. |
| alternatives and comparison | Incumbent and materially different changes to the project system-of-interest, builder arrangement, or both; current and candidate configurations; result and resource vectors; guardrails; interactions; uncertainty; reversibility; future-option effects; and displaced burdens. |
| investment `ChoiceResult` | `DecisionSubject` and granularity; stable `OptionSet`; shared comparison basis; `ChoiceRule`; probe budget, cost, and value when relevant; choose, tie-set, reject, probe, or reroute result; why the `ChoiceRule` permits this result now; protected losses; budget; implementation request if any; and overturn conditions. |
| later Work and observation | WorkPlan and authorization when they obtain; performed Work, changed structures, representative future-change cases, observations, supported and defeated claims, separately supported contribution claims, consequences for the project system-of-interest and other affected Systems, and receiving feedback. |

#### SYSE.23:4.3 - What Changes in Practice

Managers can tie an evolvability investment to a named future-change family. Engineers can say what kind of claim
failed, which current structure or Work result it concerns, which part–whole or membership level or
system-of-interest–builder relation matters, what burden each alternative moves, and why the `ChoiceRule` permits the present result. They
compare platform investment and redesign of the project system-of-interest on one declared basis.

### SYSE.23:5 - Worked Case: Where to Invest for the Next Heat-Pump Controller Variants

The heat-pump controller project from `SYSE.22:5` expects three changes over the next two years: support another
compressor supplier, add a local fallback mode for buildings with unreliable networks, and reuse assurance
evidence across controller configurations. Management says that the controller family must become *more
evolvable*.

The following table is the complete current claim set used by this decision:

| Claim kind and subject | Current claim | Evidence and limit |
| --- | --- | --- |
| architecture characteristic of the selected compressor-control and network-interface structure in controller configuration `C17` | the current coupling exposes four firmware components to one compressor replacement | one recent replacement found those four changes; it does not establish the same coupling in every family member. |
| architecture characteristic of the `ControllerFamily-F7` membership and effectivity structure | six released variants remain admitted under current interface, configuration, and assurance rules | two proposed supplier/network combinations lack effectivity and evidence; specifications are not current family members. |
| result and resource claim for `RigChangeWork-41` on the hardware-in-the-loop rig | representing another compressor interface required eleven hours of manual rewiring and produced coverage for only two interface variants | this is a result and resource use of one Work occurrence under one rig configuration, not a quality of every platform or future test. |
| result and resource claim for the 2026 commissioning and recovery Work sample | manual parameterization produced repeated field errors and slow restoration | the service records bound the sample; they do not establish platform automation as the only cause or repair. |
| capability claim for release-team Agent `RT2` | `RT2` can review the current configuration, evidence, and rollback package but lacks supported capability for the proposed cross-variant evidence slice | the current Method account and observed review Work support this bounded claim; a report about the Method is not the team's capability. |
| joint-arrangement claim for `C17`, rig `R4`, release Method `M2`, and team `RT2` | the compressor-interface coupling, rig adapter correspondence, test-service relation, and release-evidence dependency constrain the currently reachable supplier-change cases | the named participants and relations support the bounded arrangement claim; they do not establish how much each participant causes the observed Work result. |
| proposed causal-contribution claim about changing the compressor boundary and rig adapter | the mixed change is expected to reduce supplier-change lead time and improve evidence reuse | this is a possible-future contribution claim. Later comparable change Work supplies observations with which to test the expected contribution. |

The team then fills three different architecture views:

| View and `EntityOfConcern` | Obtaining relations | Decision use |
| --- | --- | --- |
| holonic and membership view of controller `C17`, rig `R4`, and family `F7` | `C17` has processor board, I/O assembly, and network module as constructive parts. `R4` has a host, I/O rack, compressor emulator, and network-fault injector as constructive parts. Six actual controllers are members of `F7` under the current effectivity basis. | A versioned compressor boundary can localize component replacement while adding processor load at controller level and configuration/evidence burden at family-member level. Rig parameterization can reduce rewiring Work while adding maintenance and qualification burden at rig-whole level. These are simultaneous cross-level conflicts, not stages. |
| non-holonic system-of-interest–builder relation view of the `C17`–`R4` test arrangement | the controller compressor interface corresponds to a rig adapter; the rig provides a test service to release Work; the evidence pipeline depends on configuration identity | The controller does not contain the rig, team, or Method as parts. Changing either side can move the supplier-change and assurance burden. |
| Work view of the next supplier-change trial | adapter parameterization precedes closed-loop test; evidence review overlaps later testing; rollback preparation and service planning overlap the release decision | Earlier and overlapping Work constrain the investment, but their order creates no holonic level. |

The holonic and membership view exposes processor and evidence burdens at levels different from the interface
change. The system-of-interest–builder relation view matters because the rig is not a part of the controller. The Work view matters because test readiness and review overlap determine calendar and assurance
resources. None of the three can be inferred from another.

Three alternatives survive admission beside the incumbent:

1. **Redesign the controller:** isolate compressor and network dependencies behind versioned interfaces. This can
   localize later changes but adds interface translation, processor load, and an immediate verification burden.
2. **Change the builder arrangement:** parameterize the test rig and configuration/evidence pipeline for the known
   supplier and network-loss variants. This can shorten trial and evidence Work but leaves four coupled controller
   components unchanged.
3. **Mixed bounded change:** introduce one compressor boundary for the next supplier and parameterize only the
   corresponding rig and evidence slice. This preserves less future reach than a general redesign but limits
   current cost and provides evidence for the larger choice.

The deciding Agent applies `C.11.CRC` to compare each finite change with the current controller-and-builder configuration. For this case, the complete result-coordinate set contains admitted supplier and network variants, change lead time, defect reintroduction, evidence reuse, rollback
time, comfort, energy, safety, and service error exposure. Resource coordinates include engineering time, rig
outage, supplier Work, review load, capital, and later maintenance. The team does not add these to one
evolvability score.

The choice below is an illustrative design comparison. In addition to the observations above, assume the team
has obtained these option estimates for the same two-year horizon. All three changes fit the architecture
budget and have an identified way to meet the declared guardrails; actual release still requires its own
qualification.

| Option | Next supplier replacement and evidence reuse | Irreversible commitment relative to the other eligible changes |
| --- | --- | --- |
| Retain the incumbent | Neither improves. | No new investment, but it does not meet the present improvement objective. |
| Redesign the controller | Replacement work becomes more local. The unchanged rig and release arrangement still prevent the required cross-variant evidence reuse. | A broad interface redesign commits more controller and verification work than the mixed option. |
| Change the builder arrangement | Both improve. To reuse evidence while the four controller components remain coupled, this option parameterizes and qualifies their wider rig and evidence interactions. | The estimated committed adaptation and maintenance burden of that wider arrangement exceeds the mixed option's, including the latter's controller change. |
| Mixed bounded change | Both improve for the next supplier. The compressor boundary confines the corresponding rig and evidence change to one slice. | Less committed adaptation and maintenance burden than the builder-only option; less controller redesign than the general redesign. Wider future variants remain outside this commitment. |

These are comparison premises, not consequences of counting four coupled components. Without the estimated
effect on evidence reuse and the comparative commitment burden, the earlier observations would not distinguish
the mixed and builder-only options. Retain that unresolved comparison rather than claiming the same choice.

The architecture choice follows from those observations and estimates:

| `C.11` content | Filled result |
| --- | --- |
| `DecisionSubject` and granularity | The `ControllerFamily-F7` investment council at team level may allocate the approved two-year architecture budget. Safety and product-release authorities remain separately identified. |
| current `OptionSet` | Retain the incumbent arrangement; redesign the controller; change the builder arrangement; or make the mixed bounded change. |
| shared comparison basis | Safety, comfort, and rollback are hard guardrails. The `BeliefState` contains the observed four-component coupling, manual rig rewiring, service errors, current family/effectivity records, and bounded transfer uncertainty. The `OutcomeModel` uses the option estimates above to relate each finite change to the result and resource vectors over the two-year horizon. They remain estimates until subsequent Work supplies observations. |
| probe decision value | Feasible pre-choice probes are an additional supplier-interface simulation and a rig mock-up, bounded to four weeks and one rig outage. Neither can establish the coupled interface–rig–evidence result without constructing nearly the same slice as the mixed option; their expected information value does not justify their delay and cost. |
| `ChoiceRule` | Reject any option that violates safety, comfort, effectivity, or rollback guardrails. Among survivors, retain the non-dominated set and choose a change within budget that improves at least the next supplier replacement and evidence-reuse case while minimizing irreversible burden. Request a probe only when it can change the survivor relation enough to justify its cost. Reject the set if no option survives; reroute when the decision subject, authority, or comparison basis is missing. |
| `ChoiceResult` | `choose_now`: make the mixed bounded change. Under the stated comparison premises, it meets the present supplier-change and evidence-reuse objective with less irreversible burden than the other qualifying change, the builder-only option. No smaller pre-choice probe is worth its cost. The implementation request for one interface and one rig/evidence slice is a later record, not implementation or improved evolvability. |

Reconsider controller redesign if evidence shows that the rig already supports the new supplier, or the
builder-only change if controller coupling proves local and stable. Compare again under the changed premise;
either finding can alter the relative burden without selecting a replacement by itself. A cheap probe that
could reverse the survivor relation would change the result to `probe_again`; guardrail failure by every option
would produce `reject_current_set`; missing authority would produce a reroute that ends the current decision pass without stopping unrelated Work. These are
the conditions for reconsidering the choice.

Assigned Agents later perform redesign, platform, test, release, and observation Work under their own
authorities. Two supplier-change occurrences provide observations about controller coupling, rig time, evidence
reuse, and service burden. A failed transfer reopens only the claims and decision that used it; it does not erase
the separate facts about released configurations.

The manufacturing coevolution studies used below support joint product-family and production-system work across
generations. Applying that line to this test, release, and service arrangement is a bounded engineering
synthesis. The case must be reopened if the transfer hides a software, Method, organization, or capability
difference that changes the decision.

#### SYSE.23:5.1 - Follow the mixed proposal through its constraining relations

To make the choice above constructible, take the next supplier replacement as the representative change.
In the current arrangement the supplier's command and response differences enter four firmware components;
the rig represents those differences through manual wiring and interface-specific scripts. The release
account relates evidence to controller, interface, rig and test configurations. Changing only the component
name in that account would not preserve its evidence claim.

The mixed proposal places the next supplier's differences behind one versioned compressor boundary. Its
contract specifies the command and response meanings, timing and failure behaviour relied on by the rest of
the controller. The corresponding rig adapter must reproduce those same meanings and relevant dynamics.
The evidence slice identifies what the boundary preserves, what changed, and which earlier observations remain
applicable. These are the actual proposed joins. A matching connector or schema alone does not settle them.

The controller engineers can retain the other components only if the boundary preserves their relied-on
behaviour under the required load. Test engineers can reuse a result only if the supplier change leaves the
claim and its applicable conditions supported. Release team `RT2` must obtain support or capability for
the new evidence argument before it is relied on. The investment can include obtaining that contribution.
The coupled slice is viable for development when those bounded contributions can be obtained within the
stated commitment and window.

The team also examines transition. Existing controllers continue using the old boundary and qualified test
configuration while the new slice is prepared. Rig time for supporting them competes with time for adapting
and qualifying the new slice. The comparison includes that contention and the service procedure for identifying
which configuration is installed. A fast new adapter without this coexistence account would not supply the
complete proposal evaluated in §5.

The resulting architecture request is therefore limited: establish the one boundary and its matching rig and
evidence slice for the next supplier, preserve the stated protections and support for released configurations,
and leave generalization to wider variants open. Controller, rig and release contributors receive the same
interface assumptions and return any incompatibility to the investment choice. This completes the choice's
technical explanation while implementation and release retain their separate evidence and authority.

**A changed future demand.** Now retain the case's current configuration facts but suppose the supplier has
confirmed that only one final replacement is needed before this product line retires. There is no longer a
supported programme of later replacements, and the retained configurations can be supported with the existing
rig. The previous two-year improvement objective must be reconsidered: repeated-use savings no longer warrant
the same generalization by themselves.

Assume, for this changed comparison, that a local supplier-specific adaptation can meet the same safety,
comfort and effectivity conditions, remains supportable until retirement, and consumes less total implementation,
test and maintenance effort than establishing the mixed slice. Under a rule to meet this one replacement with
the least justified commitment, choose that bounded adaptation; retain the mixed design as possible material
for a later use. These new comparison premises, rather than the word “retirement,” support the changed choice.
If the local adaptation instead destroys required rollback or cannot support an installed member, it does not
qualify and the investment question remains open.

The change does not invalidate the observations about four-component coupling or manual rig work. It changes
the horizon and the value of reducing that work. Send that changed obtaining burden and family boundary to
`SYSE.22`; preserve its earlier comfort and network-loss evidence where applicable. A future programme that
again requires multiple supplier variants would reopen the investment's purpose and comparison.

#### SYSE.23:5.2 - A manufacturing boundary that changes the method

Consider a constructed family of reusable containers. A new closure improves the target container's leak
performance, but its rim geometry cannot be formed by the current die. Installing a new die would stop the
only press that also produces replacement containers for existing users. “The container is modular” and
“the new die can be made” are individually plausible but do not establish a usable transition.

The engineers trace the closure change through rim geometry, tooling, press setup, leak evidence and service
stock. They compare retaining the old closure, redesigning the closure to fit the existing rim, obtaining
a compatible temporary production service, and changing the die while building adequate stock. A production
specialist must supply the forming and capacity results; this pattern supplies no metal-forming calculation.

For this comparison, assume that the current closure fails a new required leak limit. Supplier quotations
make temporary production and building enough stock for the die change exceed the authorized budget. Qualified
results support the redesigned closure on the existing rim, its required leak performance, continued stock
supply and total burden within that budget. The new-die option without that stock still lacks a way to preserve
the needed supply during changeover. Under a rule to meet the leak limit, preserve supply and stay within
budget, the bounded decision selects the closure redesign as the only admitted option in this set. Wider
tooling changes remain conditional. If later demand needs a geometry the old rim cannot support, that target-side answer is no longer
sufficient: the obtaining and capacity question becomes decisive. Use `SYSE.24` for the service-versus-build
comparison and the production practice's own capacity method. A software-style instantaneous rollback would
not answer the physical tooling or stock constraint.

### SYSE.23:6 - Bias Annotation

Watch for these nine biases:

| Bias | Likely drift | Repair |
| --- | --- | --- |
| claim-kind collapse | Architecture characteristics, holder capability, change-Work results, joint arrangements, and causal contribution are all assigned to one *evolvability bearer*. | Classify the claim first; identify the subject and evidence required by that claim kind. |
| system-of-interest-only bias | All change difficulty is attributed to the architecture of the project system-of-interest. | Inspect family, builder, platform, Method, Agent, Work, and cross-structure constraints for the named change family. |
| single-score bias | Lead time, option reach, evidence reuse, rollback, defects, and cost collapse into one evolvability number. | Use one characteristic where sufficient or a `C.25` quality bundle with visible coordinates and windows; keep Work results and resources under their own subjects. |
| modularity dogma | More modules and interfaces are assumed to mean easier evolution. | Name the change family, coupling affected, interface cost, cross-level conflict, performance loss, and evidence needed. |
| software-transfer bias | Feature flags, CI/CD, fitness functions, or microservices are copied into physical engineering unchanged. | Preserve material configuration, manufacturing, integration, specialist, safety, assurance, release, and service constraints. |
| platform halo | A new engineering platform is assumed to improve product outcomes. | Compare its finite contribution to representative changes of the project system-of-interest and displaced provider burden. |
| automation and AI bias | Variant generation or code change is treated as autonomous whole-project evolution. | Identify the performing Agents, assignments, Work, review, authority, evidence, and release decisions. |
| level-and-stage bias | The project system-of-interest, family, builders, platform, Methods, capabilities, and culture are arranged as one vertical sequence, or genuine part–whole levels disappear with the false stack. | Recover part–whole or membership levels, non-holonic system-of-interest–builder relations, and Work order or overlap separately; state cross-level conflicts when they matter. |
| success-story bias | One fast change is treated as establishing a durable characteristic or cultural improvement. | State the case, exposure, horizon, competing explanations, transfer limit, and later observations required. |

### SYSE.23:7 - Conformance Checklist

All ten conditions below are required for a conforming use of this pattern.

| ID | A conforming use... |
| --- | --- |
| `CC-SYSE23-1` | names one expected change family, project system-of-interest when it already exists or intended-system claim when it does not, configurations, use, environment, affected Systems, horizon, scale, protected characteristics, resources, `DecisionSubject`, chooser granularity, and receiving decision. |
| `CC-SYSE23-2` | classifies each relied-on claim as an architecture characteristic, holder capability, change-Work result/resource, joint-arrangement claim, or causal/contribution claim before naming its subject. |
| `CC-SYSE23-3` | gives each claim its required subject, scale, window, constraints, evidence, uncertainty, and material limits on use; one description or common word does not merge them. |
| `CC-SYSE23-4` | distinguishes current obtaining architecture relations and selected structures from possible-future architecture specifications. |
| `CC-SYSE23-5` | recovers part–whole or membership levels and simultaneous cross-level conflicts when they matter; keeps them distinct from dependencies between the project system-of-interest and builder arrangement and from Work order or overlap. |
| `CC-SYSE23-6` | states a supported dependency, correspondence, provider, service, interface, or enabling relation between the project system-of-interest and builder arrangement that changes option reachability, cost, assurance, rollback, or another decision coordinate; causal contribution has separate support. |
| `CC-SYSE23-7` | compares the incumbent and materially different changes to the project system-of-interest, builder arrangement, or both relative to one current arrangement, preserving result and resource vectors and guardrails. |
| `CC-SYSE23-8` | gives AI, robot, person, team, supplier, or organization Agents only the Work and authority supported for the named scope and window. |
| `CC-SYSE23-9` | carries the stable `OptionSet`, shared comparison basis, `ChoiceRule`, probe cost and value when relevant, a `ChoiceResult` permitted by the `ChoiceRule`, and overturn conditions; implementation and observation remain separate. |
| `CC-SYSE23-10` | states the transfer limit of product–production coevolution evidence and sends human capability and cultural-continuation results to HCD and `SYSE.21`. |

### SYSE.23:8 - Common Failures and Repairs


| Failure | Symptom | Repair |
| --- | --- | --- |
| *The system is evolvable* | No claim kind, subject, change family, scale, horizon, or evidence is named. | Classify the claim, identify its subject, and use `C.25` only when several typed quality coordinates are required. |
| Work result becomes System quality | One change duration or defect count is assigned to a platform, family, Method, or team. | Keep the Work occurrence, enacted Method, result/resource coordinate, configuration, and conditions visible; make a separate architecture or capability claim only with its own evidence. |
| Mechanism equals characteristic | The presence of modules, APIs, tests, a digital twin, or AI establishes evolvability. | Assess the declared architecture characteristic or Work result and preserve the mechanism as an explanatory input. |
| Builder mistaken for a system-of-interest part | A factory, test rig, platform, or team is drawn below the project system-of-interest as a holonic level. | Recover the builder, service, dependency, assignment, or Work relation separately; also retain genuine part–whole levels inside the project system-of-interest and builder Systems when they matter. |
| Possible future equals current architecture | Roadmap benefits enter the baseline. | Keep current relations, candidate specifications, implementation Work, and later readings separate. |
| More variants equals improvement | Candidate count rises while admissibility, integration, evidence, and selection degrade. | Preserve archive value, Front basis, guardrails, and finite resource constraints. |
| Platform metric chooses product investment | Deployment or test speed improves locally, but consequences for the project system-of-interest and provider burden are absent. | Compare changes to the project system-of-interest and builder arrangement on one shared basis and expose displaced burden. |
| Project choice equals cultural selection | A local change is called a new engineering culture. | Use `SYSE.21` and later population evidence for transmission, recognition, selection, retention, and loss. |

### SYSE.23:9 - Consequences

The project gains a practical answer to *where should we invest so that the named later changes become reachable
and affordable?* Redesign of the project system-of-interest, family architecture, builder reconfiguration,
platform Work, Method change, and separately justified capability or organization work can be compared while
keeping their subjects and relation types distinct. Genuine cross-level conflicts remain visible. Possible-future benefits do not enter
the current baseline.

The cost is a more disciplined claim and architecture account. There may be no single evolvability number, and
the best first decision may improve only one change family. Some constraints require a neighboring DPF or
specialist source; a bounded project cannot establish profession-wide cultural continuation or unlimited
open-endedness.

### SYSE.23:10 - Rationale

`C.25`, `C.30`, `C.32.ACS`, `C.32.HCS`, `C.32.MWA`, and `C.36` govern quality bundles, architecture
relations, project criteria, holon-family starter material, several practice structures, and cultural evolution.
For this engineering decision, relate the project system-of-interest and family to builder and enabling Systems,
platform, Methods, Work, configuration, evidence, and consequences for named affected Systems. Then choose which
selected structure to change for one future-change family.

The pattern keeps builder Work separate from Work on the project system-of-interest and retains genuine levels.
It can use a constructive part–whole view of the project system-of-interest or a builder System, a family-
membership view, a non-holonic system-of-interest–builder relation view, and a Work-order or overlap view because these answer different concerns. Each view
states its `EntityOfConcern` and relations. Correspondences and contribution claims among views need their own
basis.

### SYSE.23:11 - SoTA and Source Use

Continued engineering can require changes in a project system-of-interest, its builder platform or both. Relate those alternatives to product and problem portfolios, characterize the changes they make possible, and examine reversibility and the observations that would reopen a choice. Apply the builder question recursively when changing a builder requires changing its own means of construction.



A developed alternative may already connect the work this pattern needs. The [evolutionary-architecture
authors' account](https://evolutionaryarchitecture.com/precis.html) combines incremental change, engineering
support and protection of architectural concerns; the [second edition](https://www.thoughtworks.com/en-us/insights/books/building-evolutionaryarchitectures-second-edition)
extends its applied treatment. Its lesson here is to compare a complete change arrangement. The local
investment question still needs the selected future changes, actual configurations and burden on the builders.

Likewise, May et al.'s (2023) [Product-Production-CoDesign account, §§3–5](https://publikationen.bibliothek.kit.edu/1000160496/151016640)
addresses product and production change across generations without requiring synchronized one-to-one
lifecycles. It supplies a substantial manufacturing approach. Use its compatible result where it answers
the question; do not claim target–builder coevolution as a distinction from all professional practice.

The current practice example [Governing data products using fitness functions (2024)](https://martinfowler.com/articles/fitness-functions-data-products.html)
also combines platform-supported checks with domain-team responsibility and explicitly limits what basic
checks establish. For this pattern, the receiving question is whether an observed or expected change
supports the named investment, including transition and continuing burden. A check result remains evidence
for its particular claim rather than a general evolvability verdict.

| Source line | Use here | Epistemic boundary |
| --- | --- | --- |
| Bryan et al. (2007), [*Co-Evolution of Product Families and Assembly Systems*](https://doi.org/10.1016/j.cirp.2007.05.012); Tolio et al. (2010), [*SPECIES—Co-evolution of products, processes and production systems*](https://doi.org/10.1016/j.cirp.2010.05.008); and Albers et al. (2022), [*Product-Production-CoDesign*](https://doi.org/10.1016/j.procir.2022.05.231) | Supplies joint product-family and assembly/production-system design, product–process–production-system coevolution, coupling across generations, future-characteristic treatment, and production reconfiguration. This pattern adopts joint alternative development, adapts it into the system-of-interest–builder relation and the manufacturing branch in steps 4, 6, and 7, and rejects the idea that product architecture can be optimized independently of the production arrangement. | The studies concern manufacturing and product–production settings. They do not establish transfer to software, Methods, organizations, human capability, or every builder arrangement. Those extensions remain bounded engineering syntheses and reopen when a transfer failure changes the practitioner decision. |
| Ross, Rhodes, and Hastings (2008), [*Defining changeability*](https://doi.org/10.1002/sys.20098) | Supplies explicit change agents, change effects, change mechanisms, context change, and tradespace-based changeability distinctions. | Its filtered-outdegree measure answers a declared tradespace question; it is not a universal evolvability scalar and does not include every builder, Method, capability, culture, or evidence relation used here. |
| Ford, Parsons, Kua, and Sadalage (2022), [*Building Evolutionary Architectures*, second edition](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/) | Supplies practical software-architecture mechanisms for guided incremental change, several architectural dimensions, fitness functions, deployment pipelines, reversibility, and appropriate coupling. | Software examples do not transfer automatically to physical configuration, manufacturing, integration, safety, assurance, specialist authority, or product-family effectivity. A fitness function is evidence input, not the architecture characteristic itself. |
| MacCormack, Rusnak, and Baldwin (2008), [*The Impact of Component Modularity on Design Evolution*](https://doi.org/10.2139/SSRN.1071720) | Supplies empirical motivation and cautions for relating component modularity to later software-design evolution, including the need for repeatable measures and longitudinal evidence. | Software source structure and one modularity construction do not make more modules better or establish causality for another engineering profile. |
| Castle, Stock, and Gorochowski (2024), [*Engineering is evolution*](https://doi.org/10.1038/s41467-024-48000-1), and Zhang et al. (2025), [*Darwin Gödel Machine*](https://arxiv.org/abs/2505.22954) | Supplies bounded examples in which engineers change variation-and-selection arrangements or a lineage-bearing builder that generates later variants. | Bioengineering perspective and coding-agent benchmarks do not establish one universal OEE Method, unrestricted self-improvement, transfer to every system-of-interest–builder arrangement, or cultural selection. |

Assess currentness for each relied-on claim. Reopen a source row only when changed evidence alters the claim kind or subject,
change family, architecture relation, transfer limit, decision, or observation used here. Recency alone does not
make a Method or mechanism preferable.

### SYSE.23:12 - Relations


- Receive a compatible `SYSE.22` result containing the project focus, selected problem portfolio, System-family
  options, supported correspondences, unresolved mismatches, and replayable `ChoiceResult`. Accept or qualify
  that account even when its `ChoiceRule` permits a choose, reject, or reroute result instead of an experiment
  decision. If a needed input is missing, state which `SYSE.23` decision it blocks. The input selects neither the claim subject nor the
  architecture investment.
- Use `SYSE.3` for the recursive realization arrangement; `SYSE.6` for the current engineered-System architecture;
  `SYSE.7` for descriptions and provenance; `SYSE.10` for evidence; `SYSE.12` for engineering-platform
  capabilities; `SYSE.13` for configuration and effectivity; `SYSE.15` for the Method repertoire; and `SYSE.20`
  for Method-and-Work structures. Each result keeps its own subject and use boundary.
- `SYSE.23:4.1.1–SYSE.23:4.1.6` explains how to turn a future-change scenario into a target–builder investment comparison, including propagation, transition, joint conditions and continuing burden. `SYSE.22:4.1.6` receives a changed feasibility or burden premise only at the strength established by the investment or later Work.
- Use `C.25` when composition among quality contributors matters: recover the bearer and those contributors
  through its construction, retaining a single Characteristic when that suffices. Use `C.30` for obtaining
  architecture relations and selected structures, `C.32.ACS` for a small project criteria set, `C.32.HCS` for
  family-specific starter material, and `C.32.MWA` for several non-isomorphic Method, Work, subject, dependency,
  and cultural structures. None supplies the engineering decision that compares changes to the project
  system-of-interest and builder arrangement by itself.
- Use `C.18` for archive and Front claims, `C.11.CRC` for finite configuration-relative contribution
  comparisons, and `C.11` for the later choice. Keep generation, selection, architecture, capability, Work
  result, implementation, observation, and causal attribution distinct.
- Supply revision feedback to `SYSE.3`, `SYSE.6`, `SYSE.11`, `SYSE.12`, `SYSE.15`, or `SYSE.20` only when later
  evidence crosses a stated limit or changes an assumption of the receiving result. Feedback is an input to
  another decision, not an automatic stage.
- Supply `SYSE.23 → SYSE.21` only with a bounded Method or arrangement variant and observations relevant to later
  cultural work. A project choice or successful change establishes no transmission, cultural selection, or
  retention.
- Send a human capability demand to Human Capability Development only for a named human holder population,
  target Work, support arrangement, capability evidence, and horizon. Do not treat an AI or robot as a human
  holder, or turn a platform, Method, assignment, organization, or authority relation into a capability of that
  human population. Use `A.13` for the actual performer and `A.15.1` for independent Work admission; use `F.6`
  when precise assignment-bound attribution is needed. Use the pattern that defines the named assignment or authority relation.
- For organization or assignment reconfiguration, continuing flow and capacity, Method construction, or service
  intervention and restored use, use the relevant DPF result when available. Otherwise name the specialist help
  that is missing and use a qualified source. Similar change language does not merge Organization Change
  Engineering, Operations Management, Method Engineering, and Maintenance Engineering.

### SYSE.23:End
