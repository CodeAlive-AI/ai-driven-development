## SYSE.24 - Choose How the Project Will Obtain a Needed Engineering Result

> **Status:** Stable

### SYSE.24:0 - Use This When

Use this pattern when a project needs one engineering result but someone has already assumed *we will build it*,
*we will buy it*, *a supplier will do it*, or *an AI agent can handle it*. The assumed answer may be attractive,
yet the other ways of obtaining the same result have not been described on a comparable basis.

Start by naming the result and its actual kind. It may be, for example, an engineered System, one usable System
configuration, a reusable Method or `MethodDescription`, access to a capability, performed provider Work, or an
engineering episteme. State who will use or rely on the result, what acceptance means for that use, and when the
result must exist or the Work must occur.

The first useful comparative result is a written comparison of at least two complete arrangements that would produce,
perform, transfer, or make the same result available. One `C.11` `ChoiceResult` then says: choose one arrangement
or a retained tie-set now, reject the current set, perform one worthwhile probe, or reroute to another named
question. Each arrangement says what result would exist or occur, which Agents would perform which Work, which
Methods and Systems they would use, what relations would provide ownership or access, and what integration,
configuration, assurance, support, capability, and exit conditions the project would accept.

An arrangement is complete enough for comparison when its omitted burden cannot reverse the choice. *Purchase*
is a possible transfer or agreement inside an arrangement. An AI Agent is a possible performer inside an
arrangement. Method development is an enabling branch unless the sought result is a Method or `MethodDescription`; in that
case use `A.15.6` to decide whether the Method is the project Method-of-interest for the current question. The
short labels above identify parts or cues, while the comparison alternatives are whole arrangements.

The constructive move is to work backwards from receiving acceptance to the results, Work, means, and access
that can make it possible; vary where those contributions are supplied; then work forwards through each proposed
arrangement to expose incompatible joins and unavailable conditions. Sections 4.2–4.3 develop this move. A list
of supplier or technology names is useful input, but does not perform it.

Do not create a second account when an existing engineering or acquisition comparison already supplies this
result under the same conditions. When only one arrangement is lawful or available, state that constraint and
its supported basis; do not invent a rival to satisfy a table. Its feasibility may still need work. If a real
obtaining choice remains but no second comparable arrangement can yet be constructed, return the precise
comparison gap rather than claim that the sole described arrangement is best.

Use `SYSE.5` when the unresolved question is only how functions could be borne. Use `SYSE.3` to develop a
retained arrangement's first unsupported realization branch, or earlier when that branch must be understood
to compare its feasibility. Use
`SYSE.8` when the project is designing an offering and the provider arrangement that will sustain another
System's use. Specialist decisions—for example, commercial, financial, legal, governance, organization, operations, asset,
and capability-development decisions—remain with their specialist practices.

#### SYSE.24:0.1 - Precision Restoration

| Wording in this pattern | Meaning used here |
| --- | --- |
| needed engineering result | The particular result this decision seeks, not a universal kind. The practitioner states the actual System, configuration, Method, `MethodDescription`, capability, access relation, performed Work, episteme, or other result and the use that makes it needed. |
| obtaining arrangement | The Systems, Agents, Work, Methods, and direct relations that would produce, perform, transfer, or make the result available in one possible future. The compared option is an episteme describing that arrangement; the described result still needs its own world-side facts. |
| complete arrangement | One option that states the result, performers and Work, Methods and means, provision or access relations, interfaces, integration, configuration, assurance, support, capability consequences, resources, and exit conditions far enough for the present comparison. *Complete* is relative to this decision. |
| internal or external | A qualifier relative to the project boundary chosen for this decision. Name the qualified System, Agent, Work, Method, capability, ownership or access relation, and authority separately when each matters. |
| buy, reuse, commission, subscribe, lease, develop | Common cues to relations and Work inside an arrangement. Expand a cue into the whole arrangement before comparing it. |
| provider | A System on the supplying side of a stated provision or access relation. When Work is expected or observed, name the Agent that performs it and state capability, assignment, duty, Work, and result claims separately where the comparison relies on them. |
| AI Agent | A possible Agent for named Work when the arrangement supports its agency, assignment, authority, capability, access, evidence, and stop conditions. Place it inside an arrangement and support the Work claim separately. |
| parity basis | The same acceptance conditions, use, configuration, horizon, consequence set, and counted burdens used to compare every arrangement. A scalar score is optional and cannot replace a protected condition. |


An Agent performs Work. Other participants—for example, tools, equipment, supplied Systems, materials, data,
and the changed subject—retain their own relations. Name the decision-making person, team, organization, or other
sufficiently agentic System and use the applicable FPF agency, assignment, and authority patterns when the
decision relies on that Agent.

### SYSE.24:1 - Problem Frame

Several recurring failures make this difficulty visible, often only after commitment. Internal development
begins because building is
prestigious or familiar. A polished supplier demonstration is accepted as if integration, configuration,
assurance, migration, support, and exit were already included. Outsourcing is treated as removal of engineering
responsibility. A continuing provider relation is compared with a one-time purchase price. An AI Agent is placed beside a department as a short label. Comparison becomes meaningful only after each
label is expanded into an arrangement that names Work, Methods, means, assignments, integration, and acceptance.

The practical difficulty is not merely make versus buy. It is constructing several ways of obtaining the same
result so that each way exposes the burdens and dependencies that can change the engineering choice. Until that
happens, general decision theory receives a false `OptionSet`: its rows seek different results, use different acceptance
conditions, and hide different Work.

### SYSE.24:2 - Problem

An engineering result can be obtained through many arrangements. For example, a project may adapt a System it
already has, acquire a ready product and integrate it, commission a custom result, obtain continuing provider Work
or access, develop the result with its own Agents, or combine several contributions. The same visible result can
depend on very different conditions, such as interfaces, provider capabilities, data custody, rights, configuration
evidence, support, internal capability, and recovery arrangements.

Label-only make-or-buy tables hide these differences. Developed acquisition practice already addresses
integration, qualification, support, and mixed arrangements; use those contributions where they answer the
question. The failure addressed here occurs when a project reduces that practice to a few familiar labels,
for example by placing a purchase
price beside a fully burdened internal estimate, comparing an external demonstration with an internal production
configuration, omitting integration or continued-access burdens, omitting assurance, and treating contract award
as if the System, access, Work, or episteme had already been accepted and used.

The opposite failure is an exhaustive procurement programme before the engineering question is clear. A project
team can spend months choosing contract or tender forms while the needed result, acceptance basis, interfaces, and
capability consequences remain unsettled. The first pass therefore starts from one result and stops when the comparison supports the team's next commitment.

### SYSE.24:3 - Forces

The following eight tensions recur in this decision.

| Force | Tension |
| --- | --- |
| Fast availability and later change | A ready product or provider arrangement may reduce time to first use while increasing dependence, migration cost, or change latency. |
| Internal capability and immediate delivery | Internal development can grow capability while delaying the result; an arrangement that relies on provider Work can make the result available sooner while displacing learning or making it dependent on continued access. |
| Comparable result and heterogeneous means | Every option must obtain the same result under the same acceptance conditions, while the Agents, Work, Methods, Systems, and relations can differ radically. |
| Low entry price and full burden | A visible price is easy to compare, while integration, assurance, data, support, change, and exit burdens often decide the outcome. |
| Provider freedom and engineering assurance | The Agent performing provider Work needs freedom to choose its Methods, while the receiving engineering team still needs evidence that the accepted result and interfaces satisfy the stated use. |
| Technical choice and specialist authority | The engineering team must connect the arrangement, while specialist practices retain their decisions, Methods, and authorities—for example, for commerce, law, finance, governance, organization, operations, safety, security, and assets. |
| Option generation and option choice | The engineering team must generate materially different complete arrangements before the deciding Agent applies `C.11` to the fixed `OptionSet`; candidate construction and choice need distinct results. |
| Local result and affected Systems | An arrangement may help achieve the project result while transferring work, risk, lock-in, delay, or harm to affected Systems such as users, maintainers, partners, and providers. |


### SYSE.24:4 - Solution


#### SYSE.24:4.1 - Name one receiving result and one decision

State the result being sought and its actual kind; the receiving use and affected
Systems; the configuration, operating conditions, horizon, and acceptance claims; the deciding Agent and the
commitment it may authorize; and the latest useful decision date. If the proposed result alternates among owning a
product, accessing it, performing Work, developing capability, and possessing an account, select the result
that changes this commitment. The other objects may be needed inside an arrangement, but they are not
interchangeable success conditions.

Make acceptance operational enough to work backwards from it. Identify what the receiver must be able to do
with the result, which important conditions it must cover, and what would show that the received subject is the
one described. For an engineering episteme, identify the observations and interpretive relation needed by the
receiving decision. For performed Work, identify the occurrence, subject, window, and result or effect relied
on. For access, identify the actual capability, eligible user, usable window, capacity, and permitted use. An
access entitlement is not evidence that the task can finish within that window. For a System configuration,
include the relevant interfaces and operating states, not merely a catalogue identifier.

Use existing qualified acceptance and specialist results. This pattern does not invent safety criteria,
measurement validity, legal rights, or operating commitments. When the project system-of-interest or intended
use itself is unsettled, return to `A.15.6`, `SYSE.1`, `SYSE.16`, and `SYSE.2`. When one criterion is unresolved,
name that input and preserve the other usable parts. A conditional comparison can show which alternatives
depend on its answer; it cannot authorize reliance that requires the missing answer.

Protect the conditions that cannot be traded away. State the relevant horizon explicitly: first acceptance,
three years of changed configurations, repeat interpretation of retained data, or another actual use. Longer
support and ownership can cost more without helping a one-time result; conversely, a cheap first result may
fail a continuing need. Keep any proposed change of acceptance or horizon as a separate authorized question.


#### SYSE.24:4.2 - Construct alternatives by changing what is supplied

`C.38` supplies the result-first comparison discipline. `C.39` supplies the general move from a receiving result
back to its prerequisites and forward through their connections. Here the engineering construction varies
which result is supplied at each consequential boundary, who performs the remaining Work, and which means or
access make that Work possible. The following development is an obtaining Method, not a prescribed lifecycle.

##### SYSE.24:4.2.1 - Recover how the accepted result could be produced

Begin at the receiver's last consequential use. Ask what must have been produced or performed immediately
before that use can meet acceptance. Find a domain Method or a qualified existing result that supplies it.
Then ask what that operation consumes: physical inputs, observations, an identified configuration, skilled
performance, authority, access, and enabling Systems as applicable. Continue backwards only through conditions
that can change feasibility or the present choice. Stop at an input that is available under the needed
conditions, or at an unsupported contribution whose acquisition must be compared. Calling an input
available requires more than finding its description or owner.

For example, a pipe-replacement decision may need an interpreted condition account. That requires an
interpretation Method applied to qualified observations with segment identity and uncertainty, while the
observations require suitable inspection Work, calibration, equipment, and pipe access. The receiver might
obtain the completed account, obtain observations and interpret them, or obtain means and perform collection
as well. This is how different alternatives arise from the receiving result. Beginning with an inspection
device would prematurely select one position in that construction.

Use the actual technical suppliers. `SYSE.5:4.1–4.1.1` develops candidate functional and bearer organizations
and explains how their interactions can realize the outside effect. Keep that causal account intact when the
obtaining alternatives use it; do not derive a new physical or analytical Method merely by drawing a Work
sequence. `SYSE.8:4.1` can supply an offering's promised result, receiving use, provider structure, and support
conditions. `SYSE.3:4.1–4.4` can expose an enabling realization branch when its availability changes the
comparison. A useful existing account can supply several of these results.

The backward account distinguishes three things that often get confused: a result needed at a boundary, Work
that can produce that result, and means used in that Work. A qualified measurement account is not an instrument;
a maintained controller configuration is not a licence; a `MethodDescription` is not an Agent's demonstrated
capability to apply it. Owning the means can be unnecessary when qualified Work supplies the result. Supplying
only the means can leave a substantial receiving-side capability and assurance branch.

##### SYSE.24:4.2.2 - Move a consequential supply boundary and close the remaining Work

Construct one plausible way through the account using known Methods and available or explicitly proposed
contributions. Then change a boundary whose position affects this decision. The following transformations are
useful because they change what the receiver must still make possible:

| Change to the arrangement | What must be reconstructed |
| --- | --- |
| Obtain a qualified end result instead of an intermediate result. | Move the intervening Work into the provider arrangement; establish how the supplied result, its evidence, and retained rights meet receiving acceptance. Count acceptance, integration, and exception Work still left with the receiver. |
| Obtain an intermediate result and perform the remaining Work. | Identify the remaining Method, capable Agent, means, usable input, evidence, and correction. Establish that the supplied intermediate result is sufficient for that Method, including configuration and uncertainty where relevant. |
| Obtain access to means instead of owning them. | Keep the required Work and capability visible, then replace ownership assumptions with actual availability, eligibility, capacity, setup, recovery, and end-of-access conditions. |
| Obtain performed Work instead of developing the receiving team's capability. | Identify the provider performance and its acceptance boundary; compare the dependency and retained knowledge with the time and burden of developing that capability. |
| Retain a supported component and change only its complement. | Preserve the component's qualified envelope and show that the new complement uses a supported interface. Reconstruct integration, joint assurance, change, and support rather than crediting the component's evidence to the whole. |
| Reuse or adapt an available result instead of producing a new one. | Test identity, condition, effectivity, rights, and fitness for the new use; add only the modification and qualification Work actually needed. |

These transformations can produce ready-product, custom-provider, internal-development, continuing-service,
reuse, and mixed arrangements. Those familiar labels help discovery; they do not determine the construction.
Generate a second alternative by changing a material
contribution, not by renaming the performer while retaining the same unsupported assumptions.

For every moved boundary, follow what has moved and what has remained. Commissioning an assembled unit may
move fabrication and assembly while leaving site integration, verification, and operator preparation with the
receiver. Leasing a laboratory may leave setup, qualified operators, calibration, and interpretation unchanged.
Having a provider perform the test may move those operations but leave the receiving project responsible for
supplying the correct article and deciding whether the resulting evidence is sufficient. Add those residual
operations to the arrangement until it can reach the same acceptance condition.

Do not divide an operation merely because several providers are available. A division can break necessary
coupling, obscure responsibility for the delivered result, or introduce more interface Work than it saves.
Compare a combined qualified contribution with the split alternative. Conversely, an unnecessarily large
package can require a scarce supplier or make change dependent on unrelated parts. `SYSE.5` supplies a technical
redesign when a different functional organization is needed; commercial and organization practices supply
their own packaging, responsibility, and agreement decisions.

Describe each candidate as one possible future. Identify which inputs are currently supported, which are
credible proposals needing qualification, and which remain unknown. An AI Agent can occur in any arrangement
as a performer of named Work, for example drafting code or classifying observations. The arrangement must also
provide its inputs, access, qualified receiving checks, correction, resource burden, and stop conditions. The
label AI neither closes an unsupported operation nor grants acceptance authority.

##### SYSE.24:4.2.3 - Let available contributions reshape the arrangement

A provider's actual capability can change the useful division. If it supplies calibrated observations but
cannot supply the required interpretation, either add a qualified interpreting contribution or retain a
different provider arrangement. If the receiver cannot interpret the supplied format, compare obtaining a
compatible output, adding a qualified conversion, moving interpretation, or choosing different means. A file
conversion that discards required observations cannot repair their absence.

Likewise, a ready System may expose only a stable supervisory interface, making a supported component plus
an internal supervisory layer feasible while an internal replacement of its protective logic is not. The
result of this step is a small set of causally plausible whole arrangements and their decisive gaps. It is
not yet evidence that all proposed conditions can be supplied together.

Stop generation when another variation is unlikely to change the next decision at acceptable cost, using
`C.19` and `C.11` where exploration or probe worth is current. If the effort itself needs an enduring archive,
Front, lineage, descriptors, or exploration telemetry, use `C.18` for that result. `C.18` does not supply the
domain operation for constructing an obtaining arrangement.


#### SYSE.24:4.3 - Follow each arrangement forwards to receiving use

Walk from the proposed available inputs through the Work to the accepted result. At each consequential
handover, compare what the supplying operation actually yields with what the receiving operation requires.
This can expose a defect that isolated descriptions miss: both operations may be qualified while their
configuration, timing, meaning, or authority assumptions are incompatible.

##### SYSE.24:4.3.1 - Make the material and evidential joins work

Use an ordinary representative case and a consequential exception from the declared use. For a System,
follow its inputs, states, interactions, identification, and necessary recovery. For an account, follow
observations through interpretation to the claims the receiver will use. For access or performed Work, follow
eligibility, preparation, actual performance, result recognition, and return from an interrupted or unsuccessful
attempt. This is a feasibility walkthrough of the proposed arrangement; stronger acceptance may require
performed tests or other claim-specific evidence under `SYSE.4`.

At a consequential join, establish compatible subject and configuration identity, physical or informational
interface, units and meaning, necessary state, timing, and scope of evidence. Include custody, permitted use,
and responsibility where the receiver relies on them. Carry the supplying result's limits into the next
operation. If one provider's analysis assumes a calibration that the field team did not perform, the complete
account remains unsupported even though both provider descriptions look complete.

Repair a failed join by changing something that can cause it to work: supply a different intermediate result,
add a qualified transformation or preparation, move the operation to a capable performer, revise the technical
interface, or obtain a larger qualified contribution. Re-run the affected continuation and update its time,
evidence, support, and resource burden. A new adapter is an engineering contribution with its own realization
and qualification needs. If no supported transformation is known, preserve that
gap and its effect on the choice.

##### SYSE.24:4.3.2 - Establish that the necessary conditions can coexist

Place prerequisite Work and simultaneous contributions in the relevant windows. Distinguish elapsed time from
person-time, equipment occupancy, and a contractual response interval. A sequential interpretation step starts
when usable observations and its other prerequisites are available, not when collection is commissioned. Work
may overlap only when its inputs, state, and resource conditions permit overlap.

Overlay demand on shared people, test facilities, data preparation, environments, and provider capacity. Two
branches can each fit their own estimate while requiring the same specialist during the only permitted outage.
A proposed reserve must be available at the same time as the resources it complements. Include preparation,
acceptance, correction, and consequential recovery where the selected estimates do not already include them;
do not count the same burden twice.

Use `OPS.10:4` or a suitable domain operating Method when capacity or service feasibility is load-bearing.
Request the actual result needed: for example, a finite schedule for the supplied readiness times and joint
resources, an infeasibility bound, or a qualified service forecast. A total-load bound is necessary but does not
establish that precedence and simultaneous-resource conditions can be met. A mean forecast is not a hard
deadline guarantee. Use the returned result under its conditions and retain the operating authority separately.

The same reasoning applies to access and continued support. Equipment available on Monday is not usable for a
Friday task if calibration expires on Thursday; an export permission that ends at termination may not allow
the transition Work to finish. If a needed person or provider is unavailable, compare rescheduling, reserving
the joint window, changing the division of Work, supplying equivalent qualified means, or changing the current
commitment. Add the consequences of the repair to the whole arrangement. Do not silently move its deadline,
acceptance condition, or another System's protected Work.

##### SYSE.24:4.3.3 - Continue through the horizon the choice actually protects

After first acceptance, follow the changes, maintenance, repeat use, recovery, and exit that matter within the
declared horizon. Ask which Work must still occur, who can perform it, which configuration and knowledge it
requires, and which access or support must remain available. Retained source or raw data helps only if the
receiver has the rights, Method, means, and capability to make the required use. Provider independence for
reanalysis of held observations does not imply independence for future collection.

When a support relationship ends, construct the needed continuation: preserve an interpretable configuration,
transfer knowledge, qualify a replacement, maintain a limited compatibility path, or deliberately end the use.
Include transition and concurrent support where they affect the choice. A sale, export clause, or retirement
date does not itself perform that Work. `SYSE.8` supplies a provider arrangement where continuing provision is
the unresolved question; `SYSE.13–SYSE.14` supply configuration and controlled change, and the applicable retirement
Method supplies a needed closure. Do not require an elaborate exit programme for a result whose accepted use
has already ended and leaves no relevant obligation.

##### SYSE.24:4.3.4 - Keep a common account of the constructed arrangements

Use the following questions to recover the constructed arrangements for comparison.

| Question | Required content |
| --- | --- |
| What result will exist or occur? | Actual kind, identity or designator, receiving use, acceptance, configuration, horizon, and completion or availability condition. |
| Who does what? | Agents and named Work, applicable Methods, assignments and authority where relied on, and participating Systems, data, tools, facilities, and materials. |
| How is it supplied? | Production, transfer, custody, ownership, licence, access, provision, acceptance, or other relations; the residual Work after each supplied contribution. |
| How does it fit and remain identifiable? | Supported interfaces and transformations, configuration identity and effectivity, integration and migration, and the earlier decision a failed join would reopen. |
| What supports reliance? | Capability and acceptance evidence, scope and uncertainty, shared-window feasibility, unsupported claims, and a feasible discriminating probe when worthwhile. |
| What happens after first use? | Support, updates, maintenance, repeat use, data and knowledge custody, recovery, replacement, and exit within the selected horizon. |
| What capability changes? | Capability gained, retained, displaced, or dependent on tools or providers for named later Work; the time and burden of any needed development. |
| What resources and consequences matter? | Money, elapsed and resource time, attention, capacity, displacement, risk, benefit, and harm for the receiving and affected Systems; specialist results kept within their scope. |

An unknown can remain unknown when its plausible answers cannot reverse the present choice or the feasibility
claim used by it. Otherwise identify the affected claim and obtain the missing contribution, compare conditional
outcomes, or choose a bounded probe. Uncertainty belongs to a named part of the arrangement; it is neither a
reason to discard valid parts nor a licence to treat the whole as established.


#### SYSE.24:4.4 - Restore parity and compare the whole alternatives

Apply the same acceptance, environment, configuration boundary, horizon, and burden categories to every
arrangement. Compare ready demonstrations and proposed internal development against representative project
conditions. For a provider arrangement count its fee and the receiving team's residual integration, acceptance,
retained risks, change, and exit Work. For internal development include unavailable capability, opportunity
cost, qualification, support, and time until use. If two candidates share an enabling contribution, retain its
feasibility condition in both and avoid counting it twice within either whole.

First eliminate an arrangement whose demonstrated consequence violates a protected condition. Keep a decisive
unknown distinct from a demonstrated failure. Then compare the supported survivors under the decision owner's
preferences, including uncertainty about time and consequences. A narrower account cannot win by omitting the
Work that made its competitor expensive. If filling a gap changes the arrangement, compare the repaired whole
and its new burden rather than keeping the old price with the new capability.

Do not force unlike consequences into one weighted total when that would hide a protected condition or
non-compensable loss. Retain a tie-set or partial order when appropriate. Use ranges or conditional consequences
where those are what the evidence supports. If a supplier's uncertain lead time crosses the last usable date,
neither the average lead time nor a cheap price establishes the required timely result.

Apply `C.11.CRC` when the missing input is a finite change's contribution relative to the project's present
configuration. Name `S0`, the change `Δ`, the realizable `S1`, and the obtaining decision that consumes the
comparison. That Method supplies a configuration-relative contribution claim. It does not construct the
obtaining arrangement or make the final choice.


#### SYSE.24:4.5 - Obtain specialist contributions and handle an incomplete return

Use `A.15.9` and `SYSE.9` when the arrangement needs a professional contribution. Give its owner the receiving
result and decision, relevant subject and configuration, use and time window, question to answer, supplied evidence,
and what an objection or unresolved answer would change. The specialist retains the Method and authority for
that contribution. The receiving engineer supplies enough context to make the answer usable and tests its fit
when it returns.

| Question inside the arrangement | Contribution consumed here and boundary retained |
| --- | --- |
| Can required operating Work fit with continuing commitments? | Operations supplies a capacity, schedule, service, or allocation result under stated conditions. `OPS.10` distinguishes a bound, feasible schedule, scenario, and forecast; the comparison does not create access or authorize interruption. |
| Does the arrangement require a different organization? | Organization Change Engineering supplies a contribution design, responsibility, position, or enabling-assignment result, for example under `OCE.4–OCE.6`. Allocating another case within existing authority is an operating question, not automatically organization redesign. |
| Must a person become able to perform different Work? | Human Capability Development supplies a qualified development comparison such as `HCD.2`, including representative later tasks, current evidence, support, practice, time, and resource burden. A course, job title, or proposed programme is not attained capability. |
| Can the arrangement be funded and what are its financial consequences? | Finance supplies the relevant funding, cash, valuation, or financial-risk result. Engineering supplies the complete technical and Work consequences needed for that account; it does not invent the financial policy. |
| What is actually offered, permitted, owed, or recoverable? | Commercial, legal, Governance, and Administration practices supply their offer, rights, duties, permission, tender, remedy, or public-procedure results. A technical specification cannot create those relations. |
| What broader option or acceptance is at stake? | Strategy and Enterprise Asset Management supply their strategic or portfolio conclusions; application practices supply safety, security, environmental, clinical, and other qualified criteria or assessments. Preserve their subject, scope, and deciding authority. |

Inspect a returned contribution for subject, configuration, window, assumptions, evidence, authority, and
receiving use. A provider may answer about equipment availability while leaving operator availability
unanswered. Accept the supported part as equipment evidence; leave the joint performance claim open. A legal
answer about data ownership does not establish export timing, format, or interpretive capability. Request only
the missing consequence that can change the choice, with the last time its answer would still be useful.

If the owner cannot answer, does not answer by that time, or returns an incompatible result, use another
qualified source where the needed claim permits it, change the arrangement, or restrict the current decision
to Work that does not rely on the gap. Silence is not evidence that a provider lacks the capability, and it is
not confirmation that the dependency will be available. A commitment requiring the missing result remains
unsupported. A pre-authorized fallback may use another already-supported arrangement; otherwise return the
constraint to the authorized decision owner. Continue unaffected analysis instead of restarting every branch.

When the missing contribution itself needs development, expose its enabling Work and burden through `SYSE.3`
or the specialist Method. If its feasibility is decisive, resolve or probe it before committing to the dependent
whole. Requesting it is not receiving it, and requesting a professional judgement does not make the engineering
team its authorized substitute.


#### SYSE.24:4.6 - Choose at the commitment the evidence supports

Pass the resulting `OptionSet` to `C.11`. State the `DecisionSubject`, comparison basis, `ChoiceRule`, belief
state and relevant consequence model, available authority, and the worth of a possible probe. Produce one
lawful `ChoiceResult`: choose an arrangement or retained tie-set now, reject the current set, probe again, or
reroute to a named unresolved question.

Locate a probe at a consequence that can change the decision. Describe the observations it can discriminate,
the continuation under each, its people, means, access, authority, cost, elapsed time, and stopping limit. A
probe whose possible observations leave the same next action unchanged adds no decision value for this
question. A probe can also be inappropriate when its result would arrive after the last useful commitment.
Use the actual `C.11` choice inputs rather than treating this observation alone as a complete worth calculation.

State what choosing now authorizes. Selecting an arrangement for bounded preparation does not authorize live
operation, contracting, acceptance, or reliance on unperformed Work. If a remaining unsupported branch could
still defeat the proposed irreversible commitment, a label such as first realization gap does not make that
commitment sound. Resolve the branch, restrict the commitment, or return the conditional choice. For a retained
arrangement whose next Work is now justified, `SYSE.3` identifies and develops the first unsupported realization
branch and the responsible next Work.

The `ChoiceResult` remains an episteme. Producing, performing, transferring, accepting, and using the result
require their own Agents, Methods, Work, and direct relations. The comparison can establish a feasible way
under stated premises without asserting that those events have already occurred.


#### SYSE.24:4.7 - Reconstruct only what a changed condition defeats

When observations or changed conditions can reverse the choice, recover the premise that changed and trace
which operations and joins rely on it. Start with the same receiving result unless its owner changes the use
or acceptance. A new instrument configuration can leave pipe access intact while defeating the interpretation
qualification; a lost operator window can leave the equipment's capability intact while defeating timely Work.
Preserve the valid parts and repair the affected continuation.

Construct the new whole by the same moves: change the supplied result, performer, Method, means, access,
sequence, or support boundary; then follow the repair forwards through interfaces and shared resources. Recheck
every surviving candidate on the changed parity basis. A repair's extra qualification days may make an option
infeasible even when the technical defect can be fixed. Reusing the old quote, schedule, or evidence after
changing their premises would compare a whole that nobody has proposed.

A changed horizon deserves the same treatment. Moving from one accepted account to repeated surveys changes
future collection, maintenance, capability retention, data comparability, and support needs. Moving from a
three-year to a six-year controller use can expose an unsupported update or replacement period. Compare an
extended arrangement, a deliberate replacement, a different provider division, and any other feasible variant;
do not assume that ownership or a longer subscription is sufficient. Strategy, assets, finance, and capability
owners supply their consequential new inputs only where needed.

Return the new comparison and decision, or the precise gap that prevents it. A provider failure can reopen the
obtaining arrangement while preserving the project system-of-interest. A changed receiving use may require a
wider return to `SYSE.1` or `SYSE.2`. Record observed use and the continuing conditions on which the retained
arrangement relies so that the next change is assessed from evidence.


#### SYSE.24:4.8 - Keep the first useful result recoverable

Keep one account of the decision and authorized commitment; sought result and acceptance; constructed
arrangements and their residual Work; compatible interfaces and joint conditions; qualified evidence and
decisive gaps; common comparison and `ChoiceResult`; next realization or specialist contribution; and conditions
that reopen it. Existing architecture, provider, operating, and acquisition accounts may carry this content.

A comparative choice needs materially different alternatives. If only one candidate can be made comparable,
state whether another way is excluded by evidence or remains unknown. Return the constraint or missing
contribution. The amount of description is adequate when the receiving decision can be made without a
decision-changing omitted burden, not when every possible lifecycle question has been filled.


#### SYSE.24:4.9 - Recognition, assurance, and what changes in practice

**Recognition.** The pattern applies when the team is arguing about buying equipment, doing Work internally,
or using a provider while it is still unclear how each proposal reaches the receiver's result. A small backward
construction and forward walkthrough can expose the real alternative or the first decisive missing result.

**Assurance.** Distinguish a proposed arrangement, a qualified claim that it is feasible under stated
conditions, and evidence that Work was performed and accepted. Qualify the claim the commitment actually
needs: check current capability, compatible configuration and evidence, feasible joint conditions, actual
rights and authority where relied on, and the receiving use's required acceptance evidence.

The practical change is that the team can generate alternatives by moving meaningful supply boundaries,
discover the receiving Work each move creates, repair an incompatible or unavailable contribution, and compare
the resulting wholes. It can also explain why a previously selected arrangement no longer works after a
configuration, resource, provider, or horizon change.

### SYSE.24:5 - Worked Cases

#### SYSE.24:5.1 - Climate control for a new greenhouse configuration

Small equipment company `GreenHeat-4` needs a climate-control System for greenhouse `GH-2`. Until identity
inception, `GreenhouseClimateControl-GH2` remains the designator for the intended System in the WorkPlan and
descriptions. The receiving use is control of heating, ventilation, misting, and shading during cold-night, rapid-
solar-rise, and failed-humidity-sensor conditions. Acceptance requires bounded temperature and humidity
performance, no unsafe actuator command after the sensor failure, identified software and controller
configuration, recoverable observations, and a supported fallback to manual operation. `GreenHeat-4`'s authorized
management team may choose the obtaining arrangement within its approved equipment budget; electrical-safety
acceptance remains with the named specialist authority.

The team works backwards from the protected greenhouse behaviour. Actuator commands require a supported
local control and protective function; greenhouse-specific optimization can supply supervisory demands only
within that function's qualified envelope. Integration must identify the sensor and actuator configuration,
and acceptance must cover the failed-sensor return to safe local or manual operation. These are consequences
of the supplied controls-engineering account, not conclusions obtained from a procurement label.

The team first asks who could supply the accepted controller configuration and its integration. It then moves
the supply boundary: obtain a custom whole, produce that whole internally, or retain the ready protective
controller and change its supervisory complement. The latter is a distinct alternative only if the actual
interface permits the needed optimization without invalidating the protective behaviour. `GreenHeat-4`'s
engineering team develops four complete arrangements:

| Arrangement | Agents, Work, Methods, and means | Integration, assurance, support, capability, and exit |
| --- | --- | --- |
| Ready controller plus integrator | The controller vendor's engineering team supplies a configured controller; the integration company's team performs sensor, actuator, network, and commissioning Work; `GreenHeat-4`'s engineering team maintains greenhouse requirements and accepts the result. | The controller supports the existing field interface, but the greenhouse-specific failure behaviour and configuration export remain unsupported. Vendor support is available for three years; control logic cannot be maintained without vendor access. |
| Commissioned custom controller | The engineering provider's team designs and integrates a custom controller using its named engineering Method and supplies source, configuration, test evidence, and support. | The arrangement gives change access and an escrow proposal, but the provider has not shown representative sensor-failure evidence and cannot meet the required commissioning date without narrowing the first configuration. |
| Internal development with AI assistance | `GreenHeat-4`'s controls engineers lead development; a general AI Agent assists with code and test generation; an independent controls specialist reviews the safety-relevant behaviour. | The company can retain knowledge and change the result quickly, but it lacks a qualified hardware-in-the-loop environment and evidence that the team can complete assurance before commissioning. The receiving team uses its checks of the AI-produced code and tests as evidence for capability and acceptance claims. |
| Ready controller plus internal supervisory layer | The vendor controller retains safety interlocks and local fallback; `GreenHeat-4`'s controls team develops a supervisory optimization layer through a documented interface. | This preserves a supported safety boundary and gives the company control over greenhouse-specific optimization. The arrangement still depends on the controller interface, configuration export, and vendor update policy; failure of that interface defeats the option. |


For the hybrid, the forward account follows a greenhouse demand through the supervisory interface to local
control, then follows a failed or absent demand back to the supported fallback. It also joins the controller
configuration and exported observations to the acceptance evidence. The ready controller's evidence alone
does not establish these joins. The same integrator and laboratory constraints are included in the survivors'
estimates; buying a controller does not remove commissioning or acceptance Work.

The parity basis includes the same three operating conditions, commissioning date, interface set, configuration
evidence, assurance burden, data access, support horizon, internal capability consequence, expected change
latency, and exit condition for all four arrangements. The internal-only and commissioned-custom arrangements do
not survive the commissioning-date condition. The ready-controller and hybrid arrangements remain a provisional tie-set for the obtaining decision;
their unresolved protected claims prevent commitment to commissioning either one.

The two survivors have different burdens. The ready-controller arrangement is estimated at EUR 84,000, nine
weeks, and eighteen days of `GreenHeat-4` engineering Work; later greenhouse-specific changes require a vendor
release expected to take four to six weeks. The hybrid arrangement is estimated at EUR 96,000, eleven weeks, and
thirty-two days of internal engineering Work; if the supervisory interface remains supported, the controls team
can make a greenhouse-specific change within five working days. The operating plan expects at least three such
changes during the next three years.

The management team is authorized to commit up to EUR 7,000, forty engineering hours, two hardware-in-the-loop
laboratory days, and five elapsed working days to the obtaining decision. Those limits fit the remaining one-week
decision reserve without moving the commissioning date. The electrical-safety specialist may authorize the
failed-sensor injection in the laboratory; that authorization does not extend to a greenhouse trial.

The management team uses this `ChoiceRule`: preserve the failed-sensor, configuration-identity, and commissioning-
date conditions first. Probe only when the probe stays within the stated limits and every possible outcome changes
what the team may lawfully do. If both arrangements survive, choose the hybrid only when its added price is no more than EUR
15,000 and its added internal burden is no more than fifteen engineering days; otherwise choose the ready-
controller arrangement.

The proposed replay costs EUR 5,500, thirty-two controls-engineering hours, eight integrator hours, two laboratory
days, and five elapsed working days. It uses the intended sensor and actuator interfaces and injects the failed-
humidity-sensor condition while checking configuration export and the supported supervisory API. Its possible
observations and execution outcomes have four decision effects:

- an unsafe local fallback or a configuration export that cannot reidentify the tested controller and software
  rejects both survivors and returns the team to arrangement generation;
- a safe fallback and usable configuration export combined with failed supervisory timing or withdrawn API
  support rejects the hybrid and retains the ready-controller arrangement;
- a safe fallback, usable configuration export, and supported API within the timing limit retain both survivors;
  the price-and-burden branch of the `ChoiceRule` then selects the hybrid arrangement; and
- an interrupted or inconclusive replay that cannot settle the protected claims within the authorized limits
  leaves those claims unresolved. The team stops that probe and returns **reroute** to the commissioning-plan
  decision; extending the probe, moving commissioning, or committing despite the gap needs its own supported
  decision. An unknown result is not recorded as a demonstrated controller failure.

`ChoiceResult-GH2-1` is **probe again**. Choosing either arrangement without the replay would leave a protected
acceptance claim unsupported, while rejecting both would discard a survivor that one bounded replay can retain.
This worked case stops at that first useful result. APP-SYSE-04 continues the case through performed replay and a
later choice. In this case the replay must settle the protected acceptance gap before commitment to an implementation
arrangement. After an arrangement is retained, `SYSE.3` develops its first unsupported realization branch;
it can also be used earlier if a proposed probe's own means or capability are unsupported.

#### SYSE.24:5.2 - Obtain a pipeline-condition account rather than an inspection device

`WaterUtility-North` must decide which pipe sections enter its next replacement programme. The sought result is
engineering episteme `PipeConditionAccount-2027` for twelve kilometres of buried pipe; an inspection device is
only one possible means. Acceptance requires stated coverage, location error, uncertainty for wall-loss estimates,
blind-sample checks, raw observation access, configuration and date of the inspected pipe segments, and a
supported relation from observations to replacement decisions.

The backward construction reaches an identified interpretation of calibrated observations, then the field
Work that can obtain those observations from the selected pipe segments. It stops at suitable instruments,
calibration, qualified field performance, and usable access. Moving the supply boundary yields four arrangements:
obtain the account, own means and perform collection and interpretation, obtain qualified collection and
interpretation without equipment ownership, or obtain compatible observations and interpret them internally.
The utility's engineering team compares these arrangements:

- a specialist provider's field team performs inspection Work and supplies interpreted results but keeps the raw
  data;
- the utility acquires inspection equipment; its engineering team develops internal capability, performs the
  Work, and maintains the equipment and analysis Method;
- the utility leases equipment while the provider's qualified field team operates it and the provider's analysts supply raw observations and interpreted results; and
- a provider's field team performs data collection while the utility's engineering team controls the interpretation
  Method, acceptance checks, and continuing data custody.

The whole arrangements expose different calibration Systems, field access, operating interruption, performer
capability, data rights, configuration identification, blind-sample evidence, support, future repeatability,
internal capability, cost, and exit conditions. A purchase price is not compared with a provider invoice alone.
The internal arrangement includes training, qualification, equipment maintenance, field Work, analysis, and the
cost of delaying the replacement decision. The provider arrangements include acceptance and rework conditions,
raw-data access, repeatability, and recovery if the provider leaves the market.

The utility needs the account once within three months and has no present inspection-equipment capability. Its
asset-replacement board is authorized to choose the inspection arrangement within a EUR 250,000 ceiling and to
allocate at most thirty utility analyst-days. Operations separately authorizes pipe access and interruption; the
board cannot supply that result itself.

The equipment-purchase arrangement fails the time condition. The interpretation-without-raw-data arrangement
fails the evidence-custody and exit conditions. The Finance result compares funding, the Operations result states
pipe-access and interruption conditions, and the legal-practice result states data and remedy terms. The board
uses those results but does not replace their Methods or authorities.

For the survivors, the field capability evidence supports the stated instrument family, pipe material, and
collection Method. The Operations account supplies feasible access and interruption windows for either
arrangement; a field release still has to establish that the actual day's conditions match that basis. The board's choice permits arrangement preparation
within its authority, while access release and inspection remain separate Work.

The forward walkthrough follows each segment identifier and calibration state into the raw observations and
then the analysis. The open format retains the observations, configuration, and uncertainty inputs the utility
Method needs; the utility's analysis replay uses that format. The two identified analysts can supply the
twenty-four required analyst-days in the four-week interpretation window after collection without displacing
protected operational Work. The ceiling of thirty analyst-days is therefore not being mistaken for an available schedule.
The two survivors are compared on the same basis:

| Basis | Leased equipment with provider collection and interpretation | Provider collection with utility interpretation |
| --- | --- | --- |
| Interpretation capability | The provider presents three comparable surveys and blind-sample results within the required location and wall-loss limits. | The utility's two asset-integrity analysts have replayed the identified analysis Method on held-back observations from the same instrument family and pipe material; all six blind samples met the same limits. |
| Field access and time | The provider mobilizes the qualified field team and leased equipment in six weeks and supplies the account in eight weeks. | The same field team completes collection in six weeks; utility interpretation and acceptance take four more weeks. Both arrangements fit the three-month limit. |
| Evidence custody | The utility receives raw observations in an open format and an interpreted account, but only a summary of the provider's analysis Method. | The utility receives the raw observations, keeps the identified MethodDescription and analysis configuration, and produces the account itself. |
| Repeatability and support | Reanalysis depends on the provider's analysts; the price includes eighteen months of analysis support. | The utility can repeat the analysis; the provider supports instrument calibration and collection for twelve months. |
| Resources | EUR 230,000 and eight utility analyst-days. | EUR 185,000 and twenty-four utility analyst-days. |
| Capability and exit | The utility gains inspection data but remains dependent on an analysis provider. After provider exit, another analyst must be qualified before the account can be reproduced. | The utility gains interpretation capability and retains the account, observations, MethodDescription, and configuration. Provider exit affects later collection but not reanalysis of observations already held. |

The board's `ChoiceRule` first rejects any arrangement that misses acceptance, raw-data custody, or the three-
month limit. Among survivors, it prefers the arrangement that the utility can reproduce after provider exit when
its total price stays within EUR 200,000 and its internal burden stays within thirty analyst-days. If the utility
capability evidence or either resource limit fails, the rule retains provider interpretation instead; if both
interpretation claims fail, it returns **probe again** on one shared blind dataset.

The evidence supports the utility-interpretation branch. `ChoiceResult-PCA-2027-1` is **choose now**: the provider's
field team performs collection and the utility's engineering team controls the interpretation Method, acceptance
checks, and raw-data custody. No decision-changing contribution from a further probe of those conditions is identified on this basis:
the utility capability and both resource limits have already been checked. The choice records the qualified basis for field
collection and interpretation and their conditions. The next realization Work establishes the actual access
release and ready field configuration under the supplied Operations conditions; it does not use the obtaining
choice as permission to interrupt service. A failure of those conditions reopens the affected arrangement.
Contracting, field Work, blind-sample acceptance, acceptance of `PipeConditionAccount-2027`, and pipe-replacement
decisions still require their applicable Work.

#### SYSE.24:5.3 - Changed instrument configuration defeats one arrangement

Before mobilization in the pipeline case, the specified inspection instrument becomes unavailable. The provider
offers configuration B. The same pipe segments, three-month deadline, budget, and acceptance conditions remain.
Configuration B supplies a different calibration representation and wall-loss observation schema. The field
team and provider analysts have representative B evidence that meets the supplied conditions; the utility
analysts' earlier replay covered configuration A. Its six successful blind samples do not establish B competence
or compatibility.

Trace the changed premise. Field access and segment identity remain valid. The join from observations to the
utility's interpretation Method is unsupported, so the old EUR 185,000 and twenty-four-day arrangement is no
longer a complete candidate for B. The team constructs three possible repairs from that join:

- obtain A-compatible observations through a qualified provider conversion;
- adapt and qualify the utility interpretation for B before applying it; or
- move B interpretation to the already qualified provider while retaining raw-data custody and utility
  acceptance Work.

The provider confirms that its export can preserve A's column names, but has not established that it preserves
the calibration meaning needed by the utility Method. The requested substantive answer does not arrive by the
last useful decision date. The export answer is retained as a file-format fact; the interpretation claim remains
unknown. The team does not equate silence with impossibility, and does not rely on the unqualified conversion.

The responsible specialists supply a bounded adaptation and qualification plan requiring eight additional
utility analyst-days and EUR 9,000 before interpretation. These are stipulated requirements of this proposed
repair, not measured general costs of a configuration change or a guarantee of successful qualification.
The repaired total is EUR 194,000 and thirty-two analyst-days. The price still
meets the board's preference, but the whole exceeds its allocation of thirty analyst-days. No qualified additional performer
or change to that allocation is available within the decision window. Checking only the price or counting the
eight days separately would preserve an infeasible candidate.

The provider-interpretation arrangement remains supported for B at EUR 230,000, eight utility analyst-days,
and eight elapsed weeks, including its qualification, raw-data return, and eighteen-month analysis support.
The revised operating account confirms that these eight weeks still fit before the unchanged due date,
including the time already spent seeking the conversion answer. The board's existing rule therefore returns **choose now** for that arrangement for B. It accepts the stated
reanalysis dependency rather than claiming that the former independence survived. It retains the utility's
qualified A Method and earlier data for uses they still support. A later qualified conversion or development
proposal can reopen the B comparison; it does not retroactively support the rejected commitment.

#### SYSE.24:5.4 - A longer use requires a different support arrangement

Suppose GreenHeat later needs the retained controller arrangement for six years rather than the three-year
horizon compared in §5.1. The first-use result and failed-sensor criterion remain, but the known vendor support
ends after year three. Source access to the internal supervisory layer does not supply controller updates,
replacement hardware, or qualification of future configurations.

The engineering team follows those unsupported continuations and constructs two bounded alternatives: obtain
qualified support through year six, or retain the three-year arrangement and prepare a replacement before its
support ends. The first needs an actual support offer covering the controller and interface configurations. The
second needs a feasible replacement, data and configuration continuity, migration and requalification Work,
and an overlap window that the greenhouse operation can tolerate. Both include the receiving team's continuing
Work and the relevant financial consequences. A promise to decide in year three supplies neither alternative.

With no six-year support commitment and no qualified replacement account yet available, the current result is
**reroute** to those support and realization contributions. The three-year comparison remains useful for
its original horizon, but cannot justify a six-year reliance. If a six-year commitment must be made now, the
deciding Agent must obtain a feasible whole or change the commitment under its authority; extending the heading
on the old account is not a support solution.

### SYSE.24:6 - Bias Annotation

The pattern favours one decision-usable result over a complete procurement programme and comparable whole
arrangements over familiar labels. Constructing from acceptance makes residual Work and hidden dependencies
visible, but can take more effort than reusing an adequate existing acquisition or realization account. Use
that existing account when it already answers the question.

The pattern does not develop the specialist Methods for market engagement, tender, contracting, law, public
accountability, finance, organization, capability development, or post-award operations. Their qualified
contributions remain necessary where the obtaining choice relies on them. The engineering construction also
depends on actual domain Methods; drawing connections cannot establish their physical or analytical validity.

Preserving non-dominated or conditional alternatives can delay a familiar commitment. Bound further inquiry
by what it can change before the last useful return time. Stop when further exploration cannot justify its
burden; certainty about every later event is not required.

### SYSE.24:7 - Conformance Checklist

The following eleven requirements form this pattern's complete conformance checklist.

| ID | Requirement |
| --- | --- |
| `CC-SYSE24-1` | The decision states one sought result with its actual kind, receiving use, configuration, horizon, and acceptance basis, and separately names the decision-making Agent. |
| `CC-SYSE24-2` | Every option is a whole possible-future obtaining arrangement constructed from receiving acceptance, with the supplied results, residual Work, means, and access connected. Treat labels and individual contributors only inside such an arrangement. |
| `CC-SYSE24-3` | A comparative choice uses materially different whole arrangements. If only one can be constructed, distinguish an established constraint from a comparison gap; do not invent a rival or claim unsupported superiority. |
| `CC-SYSE24-4` | The same result, acceptance conditions, operating environment, evidence horizon, and burden categories are applied to every arrangement. |
| `CC-SYSE24-5` | Each arrangement identifies Agents and Work separately from Methods, tools, supplied Systems, materials, data, changed subjects, assignments, and authority. |
| `CC-SYSE24-6` | The forward account supports consequential interface, configuration, meaning, state, time, joint-resource, assurance, capability, support, custody, change, and exit conditions, or preserves the precise gap. A repair is compared with its whole burden. |
| `CC-SYSE24-7` | Commercial, legal, financial, governance, organization, operations, asset, HCD, safety, security, and other specialist claims are obtained from their practices and used within those practices' conditions and authority boundaries. |
| `CC-SYSE24-8` | The comparison ends in one lawful `C.11` result: choose now, reject the current set, probe again, or reroute to another named question. |
| `CC-SYSE24-9` | A retained arrangement states the commitment supported now and any next realization Work needed. A decisive unsupported branch is resolved, probed, or used to restrict that commitment; `ChoiceResult` remains separate from authority, performed Work, and accepted result. |
| `CC-SYSE24-10` | Reopening follows changed premises through affected operations, joins, and shared conditions, reconstructs the whole alternatives on the changed basis, and preserves valid branches without automatically reopening the project focus. |
| `CC-SYSE24-11` | The method supports separate comparisons for different result kinds, including a System configuration and an engineering episteme. |


### SYSE.24:8 - Common Anti-Patterns and How to Avoid Them

The following rows document recurring failures and their repairs.

| Anti-pattern | Working symptom | Repair |
| --- | --- | --- |
| Make-or-buy word comparison | Rows say *buy*, *build*, *outsource*, *AI*, or *reuse* without the result-bearing arrangement behind them. | Work backwards from acceptance, vary the consequential supply boundary, and follow the resulting whole forwards before summarizing it in the common account. |
| Compatible parts, impossible whole | Each supplier or Work item looks qualified, but data meaning, configuration, timing, or shared resources do not fit. | Identify the failed join and compare actual repairs with their whole resource and support consequences. |
| Unanswered condition becomes true | A partial quote or late answer is treated as confirmation of operator availability, support, or usable rights. | Retain only the supported part, expose the decisive gap, and choose an available alternative, bounded probe, restricted commitment, or reroute. |
| Demonstration versus production comparison | A polished external demonstration is compared with unfinished but fully burdened internal work. | Apply the same operating conditions, configuration, acceptance evidence, integration, support, and exit basis. |
| Award as result | Supplier selection or contract award is reported as if the System, Work, access, capability, or episteme had been obtained and accepted. | Keep commercial selection, Work, production, integration, acceptance, and use as separate results. |
| Provider absorbs engineering | Outsourcing is treated as removal of interface, configuration, assurance, affected-System, and change responsibility. | State what remains with the receiving project and which provider result supports each reliance. |
| AI as an arrangement | An AI Agent is a peer row beside purchase and internal development. | Place the Agent inside each arrangement where it may perform named Work; state capability, access, authority, evidence, stop, and recovery. |
| Method development as free support | A required new Method is hidden inside an option with no time, evidence, or capability consequence. | Treat it as a separate enabling realization branch, or as the sought result when Method development is the decision itself. |
| Lowest visible price | Purchase or provider price wins while integration, support, knowledge, opportunity cost, exit, and displaced capability remain uncounted. | Restore parity and obtain the financial and specialist results that can change the choice. |
| One scalar hides a protected condition | A weighted score compensates for a safety, authority, evidence, or exit failure that the receiving use cannot accept. | Keep thresholds and partial order visible; reject arrangements that violate protected conditions. |
| Procurement umbrella | Systems Engineering silently chooses tender, contract, incentive, legal duty, financing, organization, or operating policy. | Request the specialist result and use only its consequence for the obtaining decision. |
| Endless option inventory | The team keeps expanding market and technology lists after no new arrangement can change the next choice. | Use `C.19` for exploration policy and `C.11` for the bounded probe-or-choose stop. |

### SYSE.24:9 - Consequences

Projects gain a comparable choice before architecture, integration, supplier, capability, and assurance
commitments become difficult to reverse. The comparison preserves each arrangement's distinct contributions,
dependencies and receiving Work.

The cost is that an apparently simple purchase decision becomes an engineering decision with explicit
interfaces, configuration, evidence, support, capability, and exit. Another practice may have to answer a named
question first, so the first result may be a retained tie-set or one worthwhile probe rather than an immediate winner.

### SYSE.24:10 - Rationale

General decision theory can compare options only after they answer the same decision question and carry a shared
comparison basis. `C.38` supplies the general arrangement comparison and `C.39` the construction of a usable
whole from available contributions. The domain move developed here is constructing complete ways of obtaining an
engineering result across a designated project system-of-interest and its builder arrangements when those
structures matter, together with provider and internal Work, interfaces, configuration, assurance, and continuing
change.

The obtaining arrangement is the unit of comparison. Comparing whole arrangements keeps their different
contributions visible: an AI Agent can perform Work in several arrangements; Method development can enable an
arrangement or be the sought result of a separate project.

The pattern stops before procurement becomes a universal Systems Engineering Method. Specialist areas—for
example, market engagement, contracting, incentives, tender, public authority, finance, organization, and
provider operation—have their own problem families and evidence. Systems Engineering keeps their consequences connected to the engineered result
without taking over their decisions.

### SYSE.24:11 - SoTA Echoing

The following source contributions have different force: standards scope, professional guidance, research
synthesis, and an economic model. Their use here does not establish universal effectiveness of this obtaining
Method or transfer a specialist decision into Systems Engineering.

| Source and actual contribution | Use in this pattern | Boundary and disposition |
| --- | --- | --- |
| [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html), public scope: lifecycle processes apply to internal and external acquisition and supply and may be used recursively, concurrently, and iteratively. | Keep internal and external provision within the engineering question and use the processes needed by the result. | **Adopt the scope.** The standard explicitly does not prescribe a lifecycle model or development Method; no mandatory process order is inferred here. Its public scope is not a substitute for the full standard or a domain obtaining Method. |
| [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), Rev 2, §§4.4 and 5.1: iterative design alternatives and purchase, make/code, or reuse implementation include enabling products, readiness, integration, qualification, configuration, and support. | Reuse its substantive treatment of alternatives and implementation preparation. Connect a proposed supply boundary to the remaining receiving Work and the resulting accepted use. | **Adapt with its strength preserved.** NASA programme guidance is a developed engineering baseline, not a price-only make-or-buy table. Its application context and tailoring remain; wider commercial and application decisions need their own Methods. |
| [NASA SWE-033, Version D, Acquisition vs. Development Assessment](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695412/SWE-033%2B-%2BAcquisition%2Bvs.%2BDevelopment%2BAssessment), especially §§2.9 and 3.1–3.5: includes hybrid arrangements, environment and requirements fit, capability, V&V, integration, support, rights, and life-cycle burden. | Use the existing acquisition assessment when it supplies comparable complete software arrangements; preserve equal confidence in acquired and developed software and count the remaining receiving Work. | **Adapt as software guidance.** No universal preference for ready, internal, or hybrid development follows. Software qualification and NASA assurance requirements do not automatically govern hardware or another application profile. |
| Prasetya et al., [“Procurement Strategy in Megaprojects”](https://discovery.ucl.ac.uk/id/eprint/10226738/) (2026): the research synthesis connects outcomes, internal and market capability, work packaging, interfaces, delivery, contracting, and tender questions. | Preserve its connected procurement scope and use qualified procurement contributions when a proposed division of supply or Work makes those questions consequential. | **Bounded adaptation.** The megaproject research synthesis and proposed PRIME framework are not evidence that one procedure works in every sector. Procurement strategy remains a substantive supplier, not a list of supplier names absorbed by this pattern. |
| Tadelis, [“Public procurement design: Lessons from the private sector”](https://faculty.haas.berkeley.edu/stadelis/pub_proc_des.pdf) (2012), §§2–5: models how incomplete design and adaptation interact with cost incentives and discusses conditional procurement implications. | Include consequential uncertainty and adaptation Work in the input to specialist contracting and economic comparison. | **Bounded contrast.** Model assumptions and historical institutional setting limit the inference. The pattern does not select a payment form, tender rule, or current legal interpretation from this paper. |

#### SYSE.24:11.1 - Compare with a developed acquisition and implementation account

A professional baseline can already answer much of this question. NASA's design-solution and product-
implementation guidance considers alternatives, enabling resources, qualification of reused products, readiness,
and the support needed after delivery. SWE-033 additionally addresses mixed software arrangements and comparable
assurance. Applying those contributions fully to GreenHeat would already prevent comparing a controller's
catalogue price with a fully burdened internal-development estimate, or assuming that a purchased controller's
prior evidence automatically covers the greenhouse configuration.

The additional use of this pattern is to make the receiver's obtaining construction explicit when that account
is still missing: identify the accepted outside result, change which intermediate result or Work is supplied,
close the residual receiving operations, and test their joints and common conditions. In GreenHeat this exposes
the supported local-protection/supervisory division as a candidate requiring its own interface evidence. In the
pipeline case it exposes an account, observations, performed inspection, and access to equipment as different
possible supply boundaries rather than equivalent outputs. General selection receives these constructed
arrangements only after their consequences are made comparable.

This is a conditional contribution, not a claim that competent NASA, procurement, or domain practitioners lack
such reasoning. If their existing account already supplies the whole comparison and continuation, use it
directly. Re-describing it in this vocabulary would add cost without improving the decision. The worked cases
show the proposed Method's operation under stated inputs; they do not measure a time saving or comparative
field effectiveness.

### SYSE.24:12 - Relations

- `A.15.6`, `SYSE.1`, `SYSE.16–SYSE.17`, and `SYSE.2` supply project focus, receiving use, environment, affected
  Systems, and linked use-and-System concepts where those questions remain. Consume their actual result and
  acceptance scope; a changed obtaining provider alone need not reopen the project focus.
- `C.38` supplies result-first comparison of ways of obtaining or developing a result. `C.39` supplies the
  backward and forward construction of the whole and selective repair after change. Sections 4.2–4.3 supply
  the engineering operation that varies supplied results, residual Work, means, and access. `C.18` preserves
  an open-ended generation effort only when needed; `C.19` governs its exploration policy. Neither supplies
  the technical Method missing from an arrangement.
- `SYSE.5:4.1–4.1.1` supplies functional/bearer alternatives and their joint functioning. This pattern consumes
  that technical account and constructs ways of obtaining its result; a supply-boundary change that requires
  another technical organization returns that question. `SYSE.6` supplies consequent architecture
  decisions and their rationale.
- `SYSE.8:4.1` supplies offering and provider accounts, including continuing provision, access, custody, and
  ordinary and exception Work. This pattern consumes their supported result, conditions, and residual receiver
  obligations. An adequate existing provider comparison is reused without another account.
- `A.15.9` and `SYSE.9` guide use or acquisition of a professional contribution for a named receiving use. The incomplete or
  missing return is handled in §4.5. `SYSE.10` supplies a qualified research, model, experiment, or trial
  result where a worthwhile probe is the next contribution.
- `C.11` supplies the bounded choice from the constructed options, preference, belief, outcome, probe-worth,
  and authority inputs. `C.11.CRC` supplies a missing configuration-relative contribution comparison only;
  neither replaces the arrangement construction.
- `SYSE.3:4.1–4.7` supplies the first unsupported realization branch and next justified Work. It is used after
  retention or during comparison when a decisive feasibility premise requires it. The remaining branch cannot
  be hidden behind choose-now when it defeats the actual commitment.
- `OPS.10:4` supplies qualified capacity and timing results. `OCE.4–OCE.6` supply organization contributions,
  positions, and enabling assignments where change is needed. `HCD.2:4` and `E.23.CDI` supply capability-
  development comparison where later human Work depends on learning. Their outputs retain their assumptions,
  authority boundaries, and distinction between a proposed arrangement and observed performance.
- `SYSE.12` and `SYSE.25–SYSE.29` supply platform questions when the result is a supported practitioner path;
  `SYSE.18` supplies independently governed constituent questions; `SYSE.23` supplies project and builder
  evolvability where these change the obtaining alternatives. Each returns the particular support,
  compatibility, or change consequence this comparison consumes.
- `SYSE.13–SYSE.14` and `SYSE.4` govern configuration, change and release, and claim-specific assurance. `A.13`,
  `A.15.1`, `A.2.1`, `F.6`, and the authority patterns distinguish actual Agent, assignment, Work, attribution,
  and permission facts from the arrangement's possible-future description.
- Strategy, Finance, Governance, Administration, Enterprise Asset Management, commercial and legal practices,
  and application practices retain their own Methods, evidence, and decisions. Section 4.5 states the
  result needed at their receiving boundary; Systems Engineering connects its consequence to the whole.

### SYSE.24:End
