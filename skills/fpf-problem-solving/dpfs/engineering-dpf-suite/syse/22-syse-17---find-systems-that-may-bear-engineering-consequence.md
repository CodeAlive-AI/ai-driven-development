## SYSE.17 - Find Systems That May Bear Engineering Consequences

> **Status:** Stable

### SYSE.17:0 - Use This When

Use this pattern when a decision about a proposed System, configuration, or use change already names some
participants—for example, users, owners, operators, or interacting Systems—but may still omit bearers of
consequences. Their states or decision-relevant characteristics could change through Work or events such as
realization, operation, maintenance, misuse, failure, recovery, retirement, or later modification. Retain existing
bearers even when their identities are only partly known. Qualify not-yet-present bearers as intended System
referents in modal claims.

Begin with one proposed engineering alternative or change and the decision that can still alter it. If an existing
account already covers the material consequences at the needed scope and evidence strength, use that answer.
Otherwise trace possible consequences beyond the current contractual, organizational, and technical-interface
boundaries. Keep obtaining relations, modal path claims, observed changes, value judgements, and specialist
decisions separate. When the missing result is a person's preference, an agreement, or an account of how a proposed
operation would work, use a corresponding elicitation or scenario result, or return that missing input to the
decision. Tracing consequences alone cannot supply it.

The first useful result is a **bounded engineering consequence account**. It identifies material consequence
bearers as far as the evidence permits, preserves unresolved identity or existence questions, qualifies each
consequence, and connects it to an action or unresolved need in the receiving decision—for example, a constraint,
alternative, probe, safeguard, specialist question, monitoring condition, or explicit gap. The account is an
episteme; the Systems and changes it describes remain world-side. Add a value or representation claim only when
the receiving decision uses it and its own grounding is available.
`A.1.CSD` supplies the general discovery move. This pattern specializes it for engineering choices: start from a
proposed System, configuration, or use change and connect qualified consequences to the named engineering
decision.
Use `C.28` when one already identified causal claim is the whole question. Obtain a result from the applicable
specialist practice whenever the decision relies on authority outside Systems Engineering.

#### SYSE.17:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| focus of inquiry | A proposed engineering alternative or change, together with the actual System or intended System referent and configuration to which it applies. If an observed result prompts the inquiry, use it as evidence for a newly stated change question. |
| consequence-bearing System | An actual System whose state or decision-relevant characteristic may change under the proposed alternative or change. Its identity may be only partly known. A not-yet-present bearer remains an intended System referent inside a modal claim. |
| unresolved bearer reference | A reference whose identity, boundary, or existence is not established to the extent needed by the decision. State which question is unknown. Unknown personal identity does not erase evidence that someone was present. |
| supported obtaining relation occurrence | An actual relation occurrence under stated conditions, supported by evidence about its participants and predicate. Preserve any limits on participant identification: an observed encounter can be supported while personal identities remain unknown. A line in a diagram is only a representation. |
| modal consequence-path claim | An episteme describing relations and changes that may connect the proposed alternative or change to a bearer, with candidate participants, conditions, evidence, uncertainty, and the limit that matters to the receiving decision. A probe is conditional on its selected contribution. Establish every world-side relation occurrence in the path separately. |
| consequence claim | A claim about a possible or observed change, bearer, conditions, direction, time, evidence, uncertainty, and causal status. The claim and its world-side change have separate identities. |
| value-qualified consequence claim | A descriptive consequence plus a stated value judgement—for example, benefit, harm, burden, or opportunity—under a named value frame, bearer, scope, and evidence. |
| affected-System claim | A consequence claim that identifies the System bearing the possible or observed change. It supports that bearer–consequence statement; establish any project assignment, authority, or other relation separately when the decision needs it. |
| unresolved decision need | An episteme naming a result or relation that the receiving decision needs but does not yet have—for example, additional evidence, a specialist result, an authority relation, an authorized representative, or a safeguard. |
| engineering consequence account | The episteme returned here: focus, examined situations, bearer references, supported obtaining relations, modal path claims, consequence claims, evidence, uncertainty, decision contributions, unresolved needs, and reopen conditions. |

Test System identity when the claim relies on treating a bearer as one System—for example, when attributing a
consequence to a population as a whole. Candidate bearers include people, organizations, technical Systems, and
ecological Systems. Preserve evidence of an actual bearer even when its name or full boundary is unknown. Use an
intended System referent for a not-yet-present bearer, and state uncertainty explicitly when existence itself is
unestablished. A project assignment or decision authority requires its own grounding.

### SYSE.17:1 - Problem Frame

Engineering decisions and descriptions guide realization, operation, maintenance, and modernization Work. The
resulting changes can reach Systems outside the project's influence and formal organization—for example, a
downstream resident, future operator, maintenance provider, ecological System, supplier, bystander, competing
resource user, or later user. Discover such a bearer from the consequence claim rather than from a stakeholder
label.

The engineering problem is to discover enough consequence-bearing Systems, qualify the claims about them, and
return unresolved consequences while the receiving engineering decision can still be altered.

### SYSE.17:2 - Problem

Stakeholder lists are commonly built from cues such as visibility, power, contracts, interfaces, or organization
charts. Those cues can miss, for example, quiet, weakly represented, future, indirect, non-human, or cross-boundary
consequence bearers.
The opposite error is to call every mentioned party affected without naming a change, evidence basis, or decision
use.

A plausible arrow from a proposed change to a possible bearer can be mistaken for an actual relation or
causal effect. Treat the arrow as a representation and ground the represented relation's participants and predicate
separately. Scale words such as *person*, *team*, *organization*, *society*, and *ecosystem* provide candidate
scopes; recover actual Systems, whole–part relations, causal relations, and observed changes from their own
evidence.

Too little discovery can leave material cost or harm outside the decision. Unbounded inquiry can consume the
resources needed to act, especially when possible consequences are treated as equally established.

### SYSE.17:3 - Forces

Recurring tensions include:

- Consequences can cross, for example, contractual, ownership, organizational, interface, and project boundaries.
- Early choices need expert judgement; exhaustive measurement is often unavailable or uneconomic.
- A weakly supported possibility can justify a cheap probe or reversible design, but not an observed-effect claim.
- A descriptive consequence claim, a value judgement, and a deontic or governance claim use different predicates
  and evidence.
- Constituent, containing, neighbouring, and later reidentified Systems can change differently; aggregates can
  hide those distributions.
- Specialist safeguards must inform the engineering decision without Systems Engineering claiming authority it
  does not have.

### SYSE.17:4 - Solution

Apply the general affected-System discovery move to one proposed engineering alternative or change. First compare
the available account with the receiving decision: does it cover the material bearers, consequences, conditions,
and evidence needed now? Reuse a sufficient answer. If a missing consequence or bearer could change the choice,
perform the bounded discovery below. If the choice instead needs preferences, agreement, or developed operating
situations, use an available elicitation or scenario result, or assess its acquisition under step 8. Return a
needed but unavailable result as an explicit gap.

Retain consequence claims that change or hold open the named engineering decision, and state what supports each.
This bounded account can support a choice with explicit uncertainty; it does not promise complete preferences,
representation, or operational scenarios.

#### SYSE.17:4.1 - Perform the Move

1. **Name the focus and receiving decision.** State the proposed alternative or change, the actual System or
   intended System referent and configuration to which it applies, the use situation, relevant scope and horizon,
   and the engineering decision that can use the result.
2. **Generate consequence-producing situations.** Consider Work and events that may expose the alternative's
   consequences—for example, realization, intended use, maintenance, plausible misuse, failure, recovery,
   retirement, or later modification. Retain only situations whose consequences could alter the receiving decision;
   these examples do not impose a lifecycle.
3. **Trace outward without promoting hypotheses to facts.** Follow supported obtaining relation occurrences
   separately from modal consequence-path claims. For each modal path, name candidate participants and proposed
   relation kinds—for example, material transfer, energy transfer, information transfer, exposure, access, resource
   use, an economic relation, or an institutional relation—together with conditions, evidence, uncertainty, and
   the useful consequence or limit for this decision. A modal path does not itself select a probe.
4. **Identify the bearer to the extent needed by the claim.** Keep an observed participant actual even if its
   name or full identity is unknown; refer to the observation, place, and time that support the claim. Keep a
   not-yet-present bearer as an intended System referent in a modal claim. If existence itself is uncertain,
   retain that uncertainty. Test System identity and boundary when the consequence claim depends on that
   classification, especially for a collection treated as one whole. A role label or representative cannot supply
   that evidence. Return any unresolved recognition question that matters to the decision.
5. **Qualify the consequence.** State the characteristic or condition that may change, bearer, configuration,
   conditions, direction or magnitude cue when known, interval, and uncertainty. Distinguish an observed occurrence
   from a modal claim. State the evidence basis—for example, observation, measurement, simulation, model-based
   prediction, or a bounded expert estimate—and its limits. Use `C.28` when reliance depends on a causal,
   intervention, or counterfactual claim.
6. **Add value and specialist claims only when needed.** Name the bearer and value frame for a value-qualified
   consequence—for example, a claimed benefit, harm, burden, opportunity, or accepted loss. Preserve conflicts and
   distributions. Select any specialist acquisition through A.15.9 and C.11.DUA before sending the question with
   its System, claim, evidence, and receiving decision; keep the returned authority boundary visible.
7. **Connect consequences to the engineering choice.** Add or revise a decision contribution—for example, a constraint, alternative,
   probe, safeguard, monitoring condition, reversible step, refusal, or escalation. When that contribution relies
   on permission, authority, responsibility, or representation, establish the required relation separately.
8. **Finish with the useful answer and its material uncertainty.** A qualified consequence account, constraint,
   alternative, or explicit unknown can complete this use. Select a further discovery action through C.11.DUA
   only when its obtainable contribution warrants the full preparation, access, performer, interpretation,
   delay, displacement, and downside. Compare observations separately and together against shared resources
   and the decision window. Retain the residual and reopen condition that matter to the receiver. Reopen the account when a new bearer, changed configuration
   or use, conflicting value claim, failed premise, or required missing authority could change the decision. If
   discovery reveals that the operating situation or affected people's requirements are insufficiently understood,
   reconsider broader elicitation or scenario work against that missing result and its attainable contribution.

Discovery, design, trial, specialist inquiry, and consequence observation can overlap and reopen one another.
A receiving decision still needs the claims and evidence on which it relies. An observed encounter can support an
account before personal identities are known; a claimed future consequence remains conditional on its path and
conditions. Select any further inquiry separately from identifying that possible consequence.

#### SYSE.17:4.2 - Record the Result

| Field | Required content |
| --- | --- |
| focus and receiver | Proposed alternative or change; actual System or intended System referent and configuration to which it applies; use, scope, horizon, and receiving engineering decision. |
| examined situations | Consequence-producing Work or events retained because their consequences could alter the decision. |
| bearer references | Actual bearers with the evidence and limits of identification; intended System referents for not-yet-present bearers; explicit unknowns where identity, boundary, or existence remains unresolved. Include a System-recognition basis when the consequence claim relies on that classification. |
| relations and modal paths | Supported obtaining relation occurrences; separately stated modal consequence-path claims; conditions, evidence, uncertainty, any selected probes, and missing-relation blockers. |
| consequence claims | Changed characteristic or condition, bearer, configuration, time, direction or magnitude cue, observed-or-modal status, evidence basis, uncertainty, and causal status. |
| value and specialist results | Current value judgement and value-frame source, any conflict, the required specialist result, and its authority boundary. |
| engineering decision contribution | A named change to or unresolved need in the receiving decision—for example, a constraint, alternative, probe, safeguard, monitoring condition, reversible step, refusal, escalation, authorized representative, or protection result. |
| residual and reopen | Missing bearer references or modal paths and the concrete change that matters to a later receiving use. Include a further action only when its obtainable contribution warrants the complete inquiry burden. |

An initial account can contain one qualified consequence and one named uncertainty—for example, an
unidentified bearer, unsupported relation, or missing specialist result—when they already change the decision.
A bounded expert estimate can be usable when better evidence is not affordable, provided it meets the receiving
decision's evidence requirements. Label it as judgement with its basis and uncertainty rather than measurement
or prevalence evidence.

#### SYSE.17:4.3 - What Changes in Practice

Visibility, influence, contract, and project role stop being the entry criteria. Engineers trace a proposed
alternative or change to consequence bearers, retaining supported occurrences even when identities remain
partly unknown. They distinguish obtaining relations from modal path claims and feed uncertain but material
consequences back into decisions while change remains affordable.

### SYSE.17:5 - Worked Cases

#### SYSE.17:5.1 - Quiet Consequence Bearers of a Heat-Pump Upgrade

The engineering-use account from `SYSE.16` describes an existing heat-pump plant, a proposed controller, the next
heating season, and the architecture decision. The team examines consequences of the proposed controller for
Systems not captured by the original user-and-owner list:

| Possible bearer and change | Claim and evidence status | Engineering decision contribution |
| --- | --- | --- |
| Heat-pump plant: increased compressor cycling and wear | The current command relation obtains. Manufacturer data support a conditional wear estimate; the proposed configuration has not run for a heating season. | Add a cycle-rate constraint and monitored-service condition. |
| Maintenance-provider organization: higher expected inspection workload and less remaining recovery capacity | Service records and the current agreement identify the provider organization and the maintenance Work it performs. The additional workload remains an estimate, and no current commitment covers it. | Keep remote monitoring conditional; use `SYSE.8` or `SYSE.24` to settle provider capacity and commitment. |
| Maintenance technician: reduced cabinet clearance and greater exposure during inspection | Current geometry is described by drawings; the reduction under the proposed cabinet position remains unmeasured. | Hold the cabinet-location choice open pending a plant-room measurement and specialist safety result. |
| Individual residents in a nearby building: increased low-frequency night noise | An acoustic model supports a possible increase; no night measurement establishes an observed effect or its distribution among residents. | Retain a low-noise alternative and the conditional noise/distribution claim; a stronger release claim still needs its applicable acoustic basis. The model settles neither legal compliance nor ethical acceptability. |
| Individual building occupants: room-temperature deviation during grid load shifting | Current thermal relations are supported, but sensor latency, override behaviour, and the distribution of deviations among occupants remain unresolved. | Retain an override-safe concept branch and the latency limit; select a trial when its obtainable result warrants the burden for the decision. |
| Electricity-distribution System: changed peak-load contribution | Meter history supports the baseline; the proposed controller effect is simulated. | Keep the grid-response claim conditional; commission measurement only when its obtainable contribution warrants the work. |

Each row links a possible or observed change to a named System and supports only the stated consequence and
decision contribution. Ground any authority or representation used later with separate evidence. The team can
make a bounded architecture choice using these qualified contributions while keeping measurement gaps explicit.
For example, suppose a plant-room measurement and competent safety interpretation are available before layout
freeze; their combined result could rule out an unsafe irreversible placement at a burden justified by that gain.
Select that acquisition. An unavailable seasonal noise study is a different proposal: retain the low-noise
alternative and the conditional noise claim without making the study a condition of this narrower return.
The resulting account grants neither release permission nor evidence of an observed improvement.

#### SYSE.17:5.2 - Observed Pedestrians and a Not-Yet-Installed Locker

A team must decide tomorrow whether to fix the geometry of an east-side delivery-cart route across an existing
public footpath. Its participant list names the operator, supplier, and customer. Video shows people crossing
between 07:30 and 08:00, but their names are unknown. A maintenance log records a van using the loading bay at
07:45. The proposed locker has not been built or installed, and the carts have not operated there. A simulation
predicts short cart queues near the proposed locker; a west-side route is only a sketch.

The people and van were actual participants in the recorded events. Their presence identifies a footpath and
access use that the engineering decision must retain, without requiring personal names. Possible obstruction or
delay from future carts remains a modal consequence. For the not-yet-built locker, retain an intended System
referent: a claim that queues could impede its replenishment depends on its eventual position and operation.
Neither the observations nor the simulation establish that future interaction as an obtaining relation. No claim here depends on recognizing the
pedestrians as one collective System.

The account now connects two missing consequences to the layout decision: preserve pedestrian and maintenance
access, and examine the proposed replenishment access. It returns the observations, the conditional queue claim,
and the unresolved geometry. These inputs do not yet rank the east and west alternatives or establish physical
clearance. The team can compare a layout that preserves room for later access correction, if feasible, with
deferring the irreversible geometry choice; operating approval remains a separate decision.

Suppose the only qualified engineer has 45 minutes before the decision. A proposed 30-minute geometry walkthrough
is attainable only if access, preparation, and interpretation also fit that window. If entry requires a
70-minute induction, withdraw that proposal and return the qualified account already available. A larger inquiry
is warranted only for a result the receiving decision needs: for example, elicitation if footpath-priority
requirements remain unsettled, or scenario development if replenishment and crossing arrangements are not yet
defined. Those results may expose further bearers and revise the layout alternatives; they do not replace the
missing physical-clearance evidence. If an existing qualified geometry and access account already settles the
narrow choice, use it directly.

**When the full pattern is unnecessary.** If the available account already answers the decision at its required
scope and strength, return that answer. If one identified causal claim about one already identified System is
the whole question, use `C.28` and the direct subject pattern.

### SYSE.17:6 - Bias Annotation

Trace consequences from proposed engineering alternatives and changes rather than institutional visibility.
Quiet or unidentified people can bear consequences. Preserve their supported involvement without inventing
preferences, representatives, or agreement.

Use affordable evidence. A bounded expert estimate, simulation, or modal path claim can justify a reversible probe;
an observed-effect claim needs observation. Include any actual System or intended System referent whose qualified
consequence can change the decision; specialist authority remains with the applicable practice.

### SYSE.17:7 - Conformance Checklist

- [ ] One proposed alternative or change, its actual System or intended System referent, configuration, use,
      horizon, and receiving decision are stated.
- [ ] Bearers are found by tracing the proposed alternative or change. Observed participants remain actual when
      personal identity is unknown; not-yet-present bearers remain intended referents in modal claims.
- [ ] Unknown identity, boundary, or existence is explicit where it matters. System recognition is performed when
      the consequence claim relies on that classification.
- [ ] Supported obtaining relation occurrences remain distinct from modal consequence-path claims and
      missing-relation blockers.
- [ ] Every affected-System claim states the qualified consequence and bearer; every further relation used by the
      decision is grounded separately.
- [ ] Every material claim states bearer, changed characteristic or condition, configuration, time, evidence,
      uncertainty, and causal status.
- [ ] Every value-qualified consequence names its bearer and value frame, and any conflict remains explicit.
- [ ] Each retained consequence changes or holds open an engineering choice through a named decision contribution.
- [ ] The account retains the residual uncertainty and reopen condition needed by its recipient. Further inquiry
      is selected for attainable value against its whole burden, including the combined programme.

### SYSE.17:8 - Common Failures and Repairs

These recurring failures hide a bearer, relation, claim status, or decision contribution:

| Failure | Repair |
| --- | --- |
| Only purchasers, owners, formal roles, or influential participants appear | Trace the proposed alternative or change outward and challenge the current boundary. |
| An affected-System claim is read as a project role | State the System and consequence; add a role or assignment only when that separate relation obtains. |
| A System is ignored because it cannot object | Discover bearers from possible consequences, whether or not they can object or are represented in project governance. |
| A diagram arrow becomes an actual relation | Keep the represented relation conditional until its occurrences and conditions are supported. |
| Scale labels become a System hierarchy | Recover actual Systems and the relations used to organize them; a scale label is only a search cue. |
| Every mentioned party is called affected | Require a decision-relevant possible or observed change under stated conditions. |
| Consequence list becomes an ethical verdict | Send actual value conflicts and authority questions to their governing practices. |
| Simulation becomes causal proof | Use `C.28` and retain the narrower supported claim. |
| Inquiry produces no usable result until definitive research exists | Use a bounded expert estimate or uncertainty claim when it improves a reversible choice. |
| An unidentified observed person becomes an intended future bearer | Preserve the observed occurrence and the identity gap; qualify the possible future consequence separately. |

### SYSE.17:9 - Consequences

Engineers can compare benefits to visible participants with consequences borne elsewhere.
Quiet and future bearers enter through qualified consequence claims. Those claims can change the decision through,
for example, a probe, safeguard, specialist result, monitoring condition, or unresolved decision need.

The cost is additional inquiry and maintenance of uncertain claims. Every retained bearer or modal path claim must
change a decision, evidence need, probe, or reopen condition so the account does not grow without bound.

### SYSE.17:10 - Rationale

`A.1.CSD` supplies the transdisciplinary discovery action. Systems Engineering adds a recurring subject-specific
move: start from a proposed System, configuration, or use change, examine physical and operational consequences,
and connect qualified claims to the engineering decision that can still change the choice.

Questions that need specialist authority remain with the applicable practice.

### SYSE.17:11 - SoTA and Source Use

The practice question is how much consequence discovery an engineering choice needs when the visible participant
list may omit those who bear its effects. Three approaches answer different missing questions:

| Approach | Use when | Result and tradeoff |
| --- | --- | --- |
| Use an adequate existing account | Its bearers, configuration, use, horizon, and evidence answer the current decision. | Reuse the qualified answer. Its scope must still fit the choice; a familiar participant list alone is insufficient. |
| Bounded consequence discovery in this pattern | A possible omitted bearer or consequence could change a named engineering choice, while enough is known about the alternative and use to trace that consequence. | Return supported occurrences, modal paths, and a decision contribution or explicit gap. Accept residual uncertainty without claiming complete preferences, representation, or operating scenarios. |
| Broader stakeholder elicitation and operational-scenario development | Requirements, conflicting expectations, agreement, or the way an operation would work are themselves missing inputs. | Develop those inputs and revisit the consequence account. The broader work can expose alternatives and consequences that a narrow trace misses; its access, participant effort, and delay must be justified for the receiving decision. |

NASA's [Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/),
especially §§4.1.1.2.1–4.1.1.2.4, connects stakeholder identification and elicitation with expectations, agreement,
and nominal and off-nominal operational scenarios. Adopt its attention to affected participants and operating
situations. Adapt that broader practice to the present question: stop with a sufficient bounded answer when it
settles the engineering use, and request elicitation or scenario development when that is the missing result.
Consequence tracing cannot establish someone's preference or agreement.

`A.1.CSD` supplies the discovery and claim distinctions: actual occurrences, intended future referents, and
unresolved recognition questions remain separate from modal consequences. This pattern adapts that move to
configuration choices and physical and operational situations. `A.15.9` and `C.11.DUA` govern acquiring further
results: compare attainable decision contributions with the complete burden, including competing use of the
same people and decision window.

The research contributions qualify how the account is used. [Volden and Welde](https://doi.org/10.1016/j.ijproman.2022.06.006)
distinguish delivery performance from outcomes and wider effects, with context-dependent indicators and valuations.
Carry relevant valuation differences into step 6 before any aggregation selected for the decision.
[Williams et al.](https://doi.org/10.1080/09537287.2023.2256287) examine changing interpretations and continuing benefits
in three public projects; use that contribution to reconsider beneficiaries and consequences when use changes,
without assuming the same evolution in every project. [Thabit, Sancino, and Mora](https://doi.org/10.1111/puar.13877)
synthesize public-administration work on representation and benefit distribution. Preserve those as distinct
questions in step 6 and in any later authority claim; that review does not supply a complete engineering-harm
discovery method.

Apply the comparison at entry and when deciding whether to continue discovery: a sufficient direct account can
finish the use, a material bearer gap opens bounded discovery, and an unsettled operating situation can require
broader work. In the cart case, the
observations already restore omitted access uses; the unavailable walkthrough supplies no further result.
Reopen only the affected claims when a new bearer, changed use, conflicting concern, required authority, or failed
premise changes what the decision needs.

### SYSE.17:12 - Relations

- `A.1.CSD` supplies the general discovery move and bounded consequence account. This pattern adds engineering
  alternatives, configuration, physical and operational situations, decision contributions, and specialist
  interfaces.
- `SYSE.1` supplies the System and candidate boundary; `SYSE.16` supplies use structures, other Systems,
  conditions, and unsupported assumptions. Equivalent qualified direct sources can be used without implying a
  temporal order.
- `A.1`, `A.14`, `B.1`, `B.1.2`, and `C.13` govern Systems, wholes, collections, delimitation, crossings, and
  constructive facts. Treat a scale word only as a cue until those objects and relations are grounded.
- `C.28` qualifies a causal-use claim. The Agent performing consequence-discovery Work applies this pattern to
  identify the Systems that may bear consequences and supplies the resulting account to the receiving engineering
  decision.
- `D.1`–`D.5` govern value frames, actual conflicts, mediation, and audits when those questions arise. An
  affected-System claim states the qualified consequence and bearer.
- A compatible consequence account can inform `SYSE.2`, `SYSE.8`, `SYSE.4`, `SYSE.6`, `SYSE.10`, `SYSE.14`, and
  specialist practices. Each receiver rechecks focus, configuration, use, horizon, evidence, and authority.
- Application profiles retain their own consequence-discovery Methods—for example, safety, security, medical,
  ecological, legal, economic, software, electrical, building, or transport specializations.

### SYSE.17:End
