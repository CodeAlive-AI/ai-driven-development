## SYSE.11 - Integrate a System for One Bounded Use

> **Status:** Stable

### SYSE.11:0 - Use This When

Use this pattern when locally completed parts or changes have accumulated, but their joint operation has not
yet established that one actual engineered System is usable for a stated purpose. Integration is the broader
engineering concern; this pattern develops the bounded move from available contributions to a configuration
that supports one receiving use. It includes choosing the integration progression, correcting discovered
incompatibilities and assessing the resulting whole.

Begin with the actual System, its current configuration and the needed use. Recover an adequate existing
integration strategy and assessment before constructing what is missing. A strategy can supply the grouping,
assembly and check order directly. A current qualified result covering the same configuration and use can
finish the assessment directly; neither a new trial nor another record is required merely to use this pattern.
Otherwise choose a joint change sufficient to support the use, expose its consequential interactions
early, perform the integration Work and use the resulting observations to assess the changed System.

The first useful result is a **bounded usability assessment**: an episteme stating what the actual System can
support, on what grounds, for which configuration, conditions and interval, and with what limits and fallback.
The changed System, the Work and transformations that produced its configuration, and this assessment remain
distinct. Permission and release are separately governed decisions.

Finish when that result answers the receiving question. If a further change or inquiry could improve a live
decision, use C.11.CRC when its finite contribution comparison is missing, then C.11 for the choice. A lack of
information about an optional feature does not by itself require further observation.

Use SYSE.14 for authorization or release, SYSE.4 for a load-bearing assurance claim, and Operations Management
for continuing queues, allocation or operating control. Specialist assembly, protection and test techniques
remain with the practices that qualify them; the integration strategy connects their results and conditions.

#### SYSE.11:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| increment | A project-relative name for an identified actual System under one resulting configuration, selected for a receiving use. The same System, the transformations that changed it, and configuration claims remain separately identified. |
| usable | A bounded claim that the System in this configuration supports one named use under declared conditions and evidence window. State benefit, assurance, permission, release, reliability or completeness separately when the decision needs them. |
| integration | Dated Work that establishes the relations needed by the intended configuration. A merge, assembly record, installation flag or interface description can supply evidence; the needed relations must actually obtain. |
| integration progression | The selected grouping and order of integration and checks, with the conditions for proceeding, correcting, revising the grouping or stopping. It can include concurrent Work and intermediate configurations that are useful for learning but not yet usable for the receiving purpose. |
| Work and transformation | An Agent performs dated Work by a Method. A transformation is the actual change of a continuing subject across time. Work can cause or participate in a transformation; the two occurrences remain distinct. |
| actual configuration | The decision-relevant actual constituents, obtaining relations and characteristic values of one identified actual System over an interval, as governed by SYSE.13. A configuration description carries claims about that configuration. |
| modernization | Continuing engineering of an existing System through separately identified bounded changes and resulting configurations. The System's reidentification rule decides whether it continued or another System began. |
| MVP or continuous engineering | Source-local cues. Recover whether MVP means, for example, a market probe, demonstrator or usable engineering configuration. For continuous, name the overlapping Work and actual changes intended by the source. |

### SYSE.11:1 - Problem Frame

Engineering Work often produces local completion before it produces a usable whole. A manufactured part can
match its drawing while failing an installed interface. Software can satisfy component-test conditions while, for
example, its controller interface, sensor relation, physical plant, operator procedure, or evidence basis remains
incompatible. A prototype can demonstrate one effect without supporting the configuration and operating envelope
needed by the next decision.

No one lifecycle or cadence governs all of these dependencies. Work on, for example, physical parts, software,
evidence, platforms, suppliers, configuration, and operation can overlap at different cadences.
Engineers select one bounded integration boundary, connect the contributing Work and transformations to it,
observe use, and return a result that can support the next decision within that use boundary.

### SYSE.11:2 - Problem

A claimed increment is not decision-usable until the responsible engineers can answer:

1. Which actual System and starting configuration are changing?
2. Which receiving use, operating conditions, affected Systems, and interval bound the result?
3. Which changes belong inside the increment—for example, physical, software, description, procedure, or
   interface changes—and which remain alternatives?
4. Which input results are needed—for example, results from realization, platform, constituent coordination,
   configuration, specialist, or authority Work—and were they available before the Work that relied on them?
5. Which Agents performed which dated Work by which Methods, and which actual transformations and relations
   obtained?
6. What integration and operating observations support usability, and what claims remain unsupported?
7. What fallback, stop, separate assurance or release decision, and later change can reopen the result?

Without these distinctions, *done* becomes a proxy for actuality. Engineers can ship incompatible parts,
overread a component test, confuse a release record with use, or keep adding features without producing a
configuration that anyone can use.

### SYSE.11:3 - Forces

- A small increment shortens feedback, while its use can still depend on relations outside the changed parts.
- Software and descriptions may change quickly; Work involving, for example, procurement, fabrication, access,
  integration, and physical observations often changes more slowly.
- Each contributor needs a local completion condition, but no local completion proves usability of the containing
  System.
- Some changes are easy to reverse; others alter scarce equipment, permits, safety conditions, or independently
  governed Systems.
- Automated tools can help Agents assemble records, compare configurations, and run checks rapidly. Establish
  the governed use, acceptable loss, and authority boundary separately.
- The receiving use needs a supported System configuration while engineers preserve alternatives for future
  change.

### SYSE.11:4 - Solution

Work back from the receiving use to the relations that must hold together. Choose a feasible progression that
reveals consequential incompatibility before it becomes expensive to correct. Establish those relations,
correct discrepancies and assess the resulting configuration using evidence that actually covers the use.

#### SYSE.11:4.1 - Perform the Move

1. **Name the System and use.** State the actual System, starting configuration, receiving use, affected Systems,
   operating envelope, interval, required behavior and deciding Agent. Distinguish a demonstrated episode from
   a claim about later use or continuing availability.
2. **Recover a sufficient strategy or construct the missing connection.** Inspect an existing specialist plan
   for the same starting state, intended configuration, interactions and use. Follow it where it is adequate.
   Where the grouping or progression remains unsupported, use :4.1.1 to connect the needed behavior to the joint
   change, intermediate configurations, integration Work and checks.
3. **Establish the inputs before relying on them.** Use realization, platform, coordination, configuration and
   specialist results only for matching subjects, uses and evidence windows. Close an unsupported branch,
   replace it with a qualified source or retain it as a blocker. A result obtained later was not available to support the earlier
   decision. Resolve conflicting demands on shared equipment, access or people before scheduling both uses.
4. **Prepare the next integration and its test of progress.** Name the actual items, relations and starting
   conditions, available means, expected behavior, unacceptable result, stop and practical fallback. Select the
   specialist procedure and observations that can distinguish a successful integration from a consequential
   mismatch. Reuse sufficient existing evidence; a planned check alone establishes nothing about the result.
5. **Perform Work and identify actual change.** Keep the performing Agents, dated Work, enacted Methods and
   results traceable to the relevant subjects. Identify the actual transformations and resulting configuration
   separately from Work records and descriptions.
6. **Check the interaction and act on the result.** Use :4.1.2 to proceed, correct and reintegrate, revise the
   progression or stop. Carry an intermediate result forward only within its demonstrated or otherwise
   justified scope. Perform the remaining whole-use observation when the assessment needs it.
7. **Construct the usability assessment.** Use SYSE.10:4.1 steps 6–8 and SYSE.10:4.1.1 for a missing trial-to-use
   inference or join between results; :4.1.3 below identifies its inputs here. Return the supported use, limits,
   unsupported claims, fallback and condition for reconsideration. Obtain separately governed assurance,
   permission, release or specialist results when the receiving decision needs them.
8. **Choose later work only when it can matter.** A repair needed for the current integration returns through
   step 6. A further modernization or inquiry is a separate choice. Use C.11.CRC when the finite contribution of
   realizable alternatives is unclear, and C.11 to compare that contribution with cost, delay and reversibility.
   Select further observation only when a feasible result could change the live choice or its warranted use.
   Otherwise finish with the current assessment.

Fabrication, software integration, preparation of the trial environment and assessment construction may overlap.
Reliance still requires the particular input to be established before the Work or decision that uses it.

##### SYSE.11:4.1.1 - Choose the Joint Change and Integration Progression

**Derive the boundary from the behavior.** Follow the needed behavior through the available architecture and
interaction account: what receives the demand, what acts, what it acts on, and what feedback or external
participation makes the result possible? Locate where an included change invalidates an existing relation or
assumption. A changed controller can require a sensor mapping and an operating procedure even when neither is
listed as a feature. Conversely, a proposed diagnostic sensor can remain outside when the existing qualified
protection and evidence already support this use. Retain unchanged contributions on their applicable grounds.
The boundary is sufficient when the needed behavior has no unsupported consequential dependency, not when
every component has been changed or every desirable feature included.

If the behavior or an essential interaction is unknown, return that concrete question to the responsible
design or specialist work. SYSE.3 can develop an unsupported realization branch; it does not turn an unknown
interaction into a feasible integration merely by placing it in a WorkPlan. An unavailable required item
prevents the dependent step, but may leave independent preparation or a useful partial integration possible.
Keep the partial result's purpose explicit.

**Choose what to bring together first.** Look for an interaction whose failure would defeat the use or make
later rework costly. Select an available configuration sufficient to exercise that interaction meaningfully. It may be an actual subset, an existing test rig with a qualified substitute, or the whole System.
A substitute is useful only for the behavior it represents: a controller rig can expose signal polarity while
leaving hydraulic loading unanswered. Select the later check that must establish the missing correspondence.

Compare feasible progressions where the choice matters. One whole assembly can avoid the expense of substitutes
and repeated setup when the few interactions are already well understood. Integration by functional subsets
can expose an uncertain interaction sooner and allow independent Work to continue, but needs suitable tools,
interfaces between subsets and a final check of their joint behavior. Adding items as they arrive can shorten
waiting, yet lose that advantage if it hides the critical interaction or repeatedly dismantles scarce equipment.
Use the architecture, expected fault localization, availability, safe access, total setup and correction burden,
and the receiving deadline to choose. No matrix, fixed assembly direction or universal batch size is required.

**Connect each step to the next.** For each consequential intermediate configuration, explain what it lets the
engineers learn or perform, what counts as sufficient progress, and which later operation uses that result.
Include the enabling means and any external commitments on which that step depends. Do not treat a passed
software check as completion of an unexamined physical relation. Do not repeat a qualified unchanged check
unless the new integration can defeat its premise.

The resulting strategy needs only enough detail to guide the actual Work and justify its progression. When
an existing strategy already makes these choices adequately, use it directly. When a delivery delay, changed
interface or new operating condition defeats its rationale, revise the affected grouping or order before
continuing; the calendar alone cannot authorize the next step.

##### SYSE.11:4.1.2 - Correct a Discrepancy and Establish Progress

Compare the observed interaction with the expected behavior under the identified configuration and test
conditions. If they agree, establish the progression condition and continue. If they disagree, contain the
affected operation using its qualified stop or fallback and preserve the observation that distinguishes the
failure. Keep independent successful results available.

Locate the first unsupported or contradicted relation along the exercised interaction. Check what was actually
installed and connected, the meaning of the exchanged signal or material, the test conditions and the
measurement basis. A discrepancy can arise from an actual incompatibility, an incorrect description or an
invalid test; those require different repairs. Use a discriminating observation or specialist diagnosis when
the available evidence cannot decide between them. Do not declare the nearest component faulty merely because
its output is where the mismatch became visible.

Give the responsible engineering practice the demonstrated discrepancy and the behavior to restore. A wiring
or mapping correction may be local; a newly discovered pressure interaction may require a design change and
revised fabrication. Identify the resulting actual configuration, then repeat the failed check and the checks
whose grounds that correction can invalidate. The comparison with the old result determines this scope; it is
neither every test nor only the originally failing one by default.

Proceed when the corrected interaction meets the next step's condition and no unresolved discrepancy can
defeat that reliance. If correction is infeasible in the available
window, reconsider the boundary, substitute or fallback under its own supported use, or stop. Repeated fixes
that expose the same unmodelled interaction reopen the architecture or strategy, rather than just adding
another repetition of the same test.

##### SYSE.11:4.1.3 - Turn Integration Evidence into a Bounded Use Assessment

Give SYSE.10 the required behavior, actual resulting configuration, qualified observations and specialist
results, the grounds linking them, and the intended use and interval. If one sufficient result already covers
that claim, use it. Otherwise its inference Method develops the missing connection, including why results about
different parts hold together and why a trial applies beyond its observed conditions.

Ask the consequential question: could all these observations be true while the proposed use still failed?
A rig can be correct while installed wiring differs; a station can pass a trial while a required external buffer
is unavailable for the later event. Resolve that premise or return a narrower supported claim. Explain which
part is observed, which extension rests on qualified domain knowledge, and which future condition must hold.
An evidence window does not itself supply a reason for extrapolation.

Return the assessment when it answers the receiving question, even when the answer is that the intended use
remains unsupported. If a later premise changes, reopen the dependent inference and retain unaffected results.
Loss of support is not by itself proof of physical failure. The ordinary assessment Method does not require
the separate assurance activities in SYSE.4 unless an assurance claim is actually being made.

#### SYSE.11:4.2 - Record the Result

Use the existing configuration, integration and assessment records where they already carry the needed
content. The following are questions to keep answerable, not a mandatory second form.

| Content | What the receiving engineer needs |
| --- | --- |
| System and use | Actual System, starting and resulting configurations, receiving use, affected Systems, conditions, interval and deciding Agent. |
| Boundary and progression | Why the included changes belong together, the selected intermediate configurations and checks, conditions for proceeding, actual fallback and stop. |
| Supplied inputs | Results actually relied on, their applicability and evidence windows, and any unresolved blocker or qualified substitute. |
| Work and actual change | Dated Work, Agents, Methods, subjects, results, transformations and obtaining relations; discrepancies, corrections and their resulting configurations. |
| Usability | What each observation or qualified result supports, the consequential inference to the use claim, limits, unsupported claims and conditions for reconsideration. |
| Separate decisions | Assurance, permission, release or specialist decisions still needed for the receiving use. |
| Later work, when selected | The separate comparison and choice, attainable contribution, burden, alternatives and reopen condition. No later-work record is required when the assessment completes the current question. |

#### SYSE.11:4.3 - What Changes in Practice

Engineers choose integration Work to expose the interactions that determine whole-System use. They can explain
why a partial result permits the next step, what must be repaired after a mismatch, and why the final evidence
supports the selected use. Sufficient existing strategies and assessments remain usable directly. Finishing
the increment does not depend on starting another modernization.

### SYSE.11:5 - Worked Case: A Flood-Pump Station for Bounded Emergency Discharge

This constructed case supplies qualified specialist procedures and results as inputs. Its numbers illustrate
integration and inference; they are not a pump design or operating procedure.

#### SYSE.11:5.1 - The Use Determines What Must Change Together

A municipal flood-pump station operates in C18. For the next flood-risk month, engineers are asked whether an
updated configuration can discharge at least 0.75 m³/s during an attended emergency episode lasting no more than
30 minutes, within the specified inlet-level, head, power and fluid envelope E. Correct response to the pressure
signal and the station's stop function are also required. The request for a month of readiness must distinguish
conditional fitness for an episode from a guarantee of availability throughout that month.

The new discharge manifold changes the hydraulic resistance. The selected controller package supplies the
corresponding operating settings, and its pressure-input mapping must match the installed transmitter. Those
three changes belong together: retaining the old settings or an incompatible mapping would defeat the hydraulic
qualification for the new manifold. The operator's existing procedure receives the changed configuration and
limits. The proposed bearing-temperature sensor remains outside: existing qualified protection and maintenance
conditions already cover this bounded duty, and no required behavior currently depends on the added sensor.

The engineers recover the realization arrangement, integration platform readiness, temporary collector-buffer
commitment and current configuration basis. An earlier unsupported fixture-and-weld branch has been resolved
through feasibility Work: a fixture design and current toolmaking/welding capability now support the chosen
fabrication Method. The actual fixture and manifold still have to be made. Platform evidence is available
before the controller trial; later participation will supply its own observations.

The station remains the same actual System under its reidentification rule: its stable boundary, foundation and
pump train continue. C19 names the resulting configuration, not another System or the description of the change.
Restoring C18 remains feasible with the retained manifold, settings and a qualified four-hour reinstatement
procedure. It restores only C18's previously supported lower-duty use; it neither instantly undoes C19 nor meets
the new 0.75 m³/s requirement. An urgent need outside either supported use requires a separate municipal response.

#### SYSE.11:5.2 - Expose the Interaction Before the Scarce Station Window

The manifold needs two days of fabrication; the controller, input hardware and existing qualified integration
rig are available now. The station has one planned outage window. The engineers compare two feasible strategies.
Waiting and testing everything only after assembly would avoid a rig setup, but a signal incompatibility found
then would consume the scarce outage and could require reinstatement. An early pressure-input/controller/drive
check costs half a day on the existing rig and can distinguish that incompatibility while fabrication continues.
They choose the latter. A new full hydraulic simulator would add cost without settling a remaining question that
the planned station trial and available hydraulic qualification cannot already address.

| Progression | Work, useful result and condition for continuing |
| --- | --- |
| Fabricate the manifold and fixture while checking the controller interaction. | The fabrication team produces and inspects the physical assembly by its qualified Method. The controls team uses the actual input hardware, selected software and drive interface on the existing rig, with a qualified pressure-signal source. Independent results can proceed concurrently. |
| Resolve the signal discrepancy on the rig. | An increasing input produces a decreasing pressure indication and the wrong control response. The team holds the dependent activation, compares the transmitter convention, installed input and mapping, and finds a reversed conversion in the mapping. It corrects the mapping and repeats the range, direction and stop checks that the change can affect. All now meet the rig procedure's conditions. |
| Establish the installed configuration. | After fabrication acceptance, the team installs the manifold and corrected controller/mapping. Inspection confirms the hydraulic geometry used by the qualification; an installed signal check confirms the actual transmitter, wiring and mapping. The rig result alone would not cover that wiring. The independent station stop check also passes. |
| Exercise the whole station in the bounded trial. | The municipality makes the temporary buffer actually available, the operator enacts the applicable procedure, and the engineering team observes discharge and control behavior in C19. The trial result and qualified extension in :5.3 support the assessment. |

The defect is an interaction mismatch: both local items could have passed checks using their own signal
conventions. Correcting the conversion changes the installed configuration basis; it does not require
refabricating the unaffected manifold. Conversely, a hydraulic mismatch would return to the relevant design or
fabrication question. The teams' dated Work and its results remain distinct from the manifold's transformation
through welding, cooling and rework, and from the station's transformation from C18 to C19.

The progression condition is substantive: correct range, direction and stop response permit the subsequent
installed check, which then permits the whole-use trial under its own conditions. If the manifold arrives
late, the rig result remains useful for its tested
configuration, but neither C19 nor emergency-discharge fitness has thereby been established. The team revises
the outage plan instead of treating software completion as permission to proceed.

#### SYSE.11:5.3 - Explain the Trial-to-Use Inference

The whole-station trial lasts 30 minutes at the qualification's reference condition in E. Its lowest indicated
discharge is 0.82 m³/s. The qualified measurement bound is 0.02 m³/s, so the observed lower bound is 0.80 m³/s.
Correct signal response and the independent stop function have been established in the installed configuration.
Those facts establish the tested episode; they do not alone cover every condition in E or the following month.

The available specialist result H19 supplies the missing hydraulic extension. For this installed geometry,
controller settings and correct pressure mapping, it bounds the reduction from the trial's lower flow bound
to any permitted episode in E at 0.03 m³/s. Its qualified scope includes the pump's allowed service condition
and the stated one-month application window, with a current pre-use condition check and confirmation of the
buffer relation. It includes the relevant interaction and model uncertainty; the trial's measurement bound is
handled separately. How those hydraulic and service bounds were established remains the specialist's work,
not a number inferred from the short trial. If H19 is unavailable or does not cover these conditions, that
extension remains unsupported.

Following SYSE.10:4.1.1, the engineers work backward from the required 0.75 m³/s and forward from the actual
results. The trial lower bound and H19's compatible one-sided reduction give 0.80 − 0.03 = 0.77 m³/s,
which meets the criterion with 0.02 m³/s margin. Configuration inspection and the installed signal check make
H19 applicable. The separately established stop behavior is also necessary; a flow margin cannot compensate
for its failure. The buffer must participate under the conditions used by both trial and extension.

The resulting technical assessment supports **an attended episode of at most 30 minutes in E during the named
month, in unchanged C19, with its qualified service condition and buffer participation confirmed before use**.
It does not guarantee that the station, power or buffer will be available for every flood event, nor support
greater head, longer operation or all-season reliability. The municipal decision-maker receives that conditional
fitness result and the still-open availability question. Release and authorization remain separate; if the
receiving decision requires unconditional month-long readiness, this assessment does not answer it.

#### SYSE.11:5.4 - Change One Premise and Keep the Surviving Result

The buffer operator later withdraws the commitment covering the remaining month. The trial observations,
mapping correction, installed configuration and independent stop result remain valid for their recorded
conditions. H19's hydraulic statement and the conditional fitness assessment also survive. What must be
withdrawn is the recommendation to count on C19 for a later event under the former buffer commitment. This
does not prove that the station has lost hydraulic capacity or that the earlier trial failed.

The engineers withhold that recommendation for an event lacking confirmed buffer participation. A new
compatible commitment can restore the missing premise; a different discharge route instead needs qualification
of its changed hydraulic conditions. Repeating the old trial while the temporary buffer is present would not
establish its later availability. Reinstatement of C18 remains possible only through its actual restoration
Work and within its lower-duty limits.

For the original completed integration, no extra load-window observation is selected merely because the
bearing-sensor option lacks evidence. Another run in E would not qualify that sensor's placement or maintenance,
and H19 already supplies the required flow extension. With no live challenge to that basis, repeating it
does not justify another buffer reservation for the current choice. The engineers finish with the supported
C19 assessment and its limits. A later proposal for longer duty, a changed service condition or a credible sensor alternative can
create a new choice; then C.11 compares a feasible inquiry's decision effect with its burden. The later buffer
withdrawal creates a concrete coordination problem, not a generic obligation to collect more pump data.

**Countercase.** A document bundle is approved while no actual configuration, integration Work or supporting
use evidence exists. Identify the missing contribution; approval alone does not produce a usable increment.

### SYSE.11:6 - Bias Annotation

A passed gate or successful software build can be mistaken for evidence of whole-System use. Recover what
its underlying checks actually establish and supply the missing interaction or applicability grounds. Conversely,
waiting for a complete physical assembly can postpone feedback that an available subset could already provide.
Choose the integration boundary from the useful evidence and its total burden.

Institutional status and labels supplied by, for example, vendors, tools, or standards can support particular
claims, but they do not establish actual integration or use. Automation can support bounded Work and checks; the
receiving Agent still selects the use and any authority relation remains separately supported.

### SYSE.11:7 - Conformance Checklist

- [ ] One actual System, starting configuration, bounded use, required behavior, conditions, interval and deciding Agent are named.
- [ ] The joint change and progression have a reason grounded in the needed behavior and interactions, or a sufficient existing strategy supplies that reason.
- [ ] Inputs match the subjects, uses and evidence windows and were available before the Work or decisions that relied on them.
- [ ] The actual integration and any correction establish the conditions for the next dependent step; a partial result is not overread as whole-use fitness.
- [ ] Work, transformation, actual configuration and the claims in its description remain distinguishable.
- [ ] The assessment explains what supports the whole-use claim and any extension beyond observed conditions, using a sufficient direct result or SYSE.10.
- [ ] Fallback is feasible for its own supported use; unresolved discrepancies and unsupported claims have a concrete stop or return.
- [ ] Separately governed assurance, permission, release and specialist decisions retain their own grounds.
- [ ] If later modernization or inquiry is selected, its separate comparison and choice justify the attainable contribution and burden. Otherwise the current result can finish.
- [ ] Reopen conditions identify the configuration, use, evidence or relation whose change matters.

### SYSE.11:8 - Common Failures and Repairs

| Failure | Repair |
| --- | --- |
| Treat a sprint, merge, release or document bundle as the increment | Identify the actual System, resulting configuration and grounds for its use. |
| Assemble everything before exposing a consequential uncertain interaction | Compare a useful early subset with the whole-assembly strategy, including substitutes, setup, correction burden and the receiving deadline. |
| Correct the visible symptom and continue without establishing the new interaction | Diagnose the discrepancy, identify the changed configuration, and recheck the failed interaction and the other results whose premises changed. |
| Infer whole-System usability from a component test | Establish the part–whole correspondence and missing joint evidence through the integration and assessment Methods. |
| Treat platform availability as participation | Keep pre-use capability and condition claims distinct from actual provision or participation Work and its later evidence. |
| Put every change into one cadence | Preserve independent physical, software and operating Work while enforcing the actual dependencies at integration. |
| Treat modernization as feature accumulation | Compare what a feasible change contributes to the receiving use, including repair, rollback and keeping the current configuration. |
| Order another trial because a field is empty | Identify how its attainable result could change a live choice; stop when it cannot justify its burden. |
| Treat a decision record as actual change | Keep the decision and its result separate from later Work and transformation. |

### SYSE.11:9 - Consequences

An early interaction check can expose a repair while independent Work continues. Intermediate configurations
also cost setup, qualification and repeated checks; they are worthwhile when that burden is justified by what
they reveal or make possible. A sufficient existing strategy can avoid new planning, and a simple well-understood
assembly may need no intermediate rig. The assessment preserves which use has support when a configuration or
external relation changes. These are conditional engineering gains, not a measured universal reduction in time
or failure rate.

### SYSE.11:10 - Rationale

An engineered System changes through actual Work and transformations. A bounded increment exposes compatibility
and use evidence before a larger commitment. Continuing modernization preserves the System's temporal identity
and repeatedly returns evidence to engineering decisions.

### SYSE.11:11 - SoTA and Source Use

**The working question is how to obtain a justified bounded-use result from available parts and local results
when some consequential interactions have not yet been established.** The same question includes the case in
which a competent specialist has already supplied an adequate integration strategy and assessment.

The selected line combines use-driven integration progression with explicit assessment of the resulting
whole. It adopts established interaction engineering rather than deriving a strategy from the vocabulary of
Work or evidence alone. NASA's Product Integration and SEBoK's System Integration are substantive candidates
for this work: they develop the choice and execution of an integration strategy. DORA's CI/CD line is a serious
alternative for software changes, with a potentially reusable rapid-feedback contribution in mixed systems.
The conditional choices below compare those complete arrangements under the same available inputs.

| Situation and receiving question | Selected complete arrangement and serious alternative | Consequence and accepted burden |
| --- | --- | --- |
| An established domain strategy and its qualified assessment already cover this configuration, use and interval. What remains to obtain the result? | Use that strategy and assessment directly. The alternative is to reconstruct a separate SYSE.11 plan and repeat observations. | No missing engineering contribution justifies the latter. Sections :0 and :4.1 preserve the direct path; extra documentation or trials would add burden without answering another question. The source's terminology need not be replaced to use a sufficient result. |
| The pump's fabrication plan and local controller checks exist, but the installed interaction and whole-use inference do not. How should the team use its one outage window? | Adapt the specialist integration-strategy line: check the available control interaction while fabrication proceeds, establish installed correspondence, then assess the whole trial using H19. The competent alternative is one planned whole-station assembly and trial, with the same protection, diagnostic capability, qualified assessment and restoration provision. | The latter saves the half-day rig setup and avoids substitute-to-installation transfer. Here it leaves a consequential uncertain signal interaction to the scarce outage. The selected arrangement accepts the setup and correspondence check to expose that fault earlier; :4.1.1–:4.1.3 and :5.2–:5.4 develop the decision, correction and inference. If the uncertainty is already resolved, or the rig cannot represent it, the extra stage loses this reason. |
| A software change has a qualified automated integration and acceptance environment that represents the receiving use. How can small changes remain usable? | Use the established CI/CD arrangement, its feedback and restoration practices, and the applicable release decision. For a mixed physical change, retain that software contribution and supply the remaining physical integration and whole-use grounds. | Rebuilding a separate physical-style progression adds no value to the covered software use. Conversely, software deployability alone leaves the pump's hydraulic and external-buffer premises unanswered. The added physical Work follows those particular gaps, not a claim that CI/CD is merely a merge or demands deployment of every change. |

The source choices have bounded roles:

- **Adopt and adapt:** [NASA, Product Integration, §5.2.1.2](https://www.nasa.gov/reference/5-2-product-integration/)
  supplies preparation, assembly/activation order, enabling means, interface checks and revision when delivery
  conditions change. It supports the construction in :4.1.1–:4.1.2. Its programme documentation and lifecycle
  organization are not mandatory outputs of this bounded pattern.
- **Adopt and adapt:** [SEBoK, System Integration, Integration Strategy and Process Approach](https://sebokwiki.org/wiki/System_Integration)
  supplies intermediate aggregates, strategy alternatives and their risk, availability and test burdens.
  Its distinction between developmental integration and production assembly remains source-local. SYSE.11
  instead follows the named actual System and receiving use, including a modification in operation; the
  qualified assembly and design practices still supply their own Methods.
- **Adopt within software scope; adapt the feedback contribution where correspondence holds:**
  [DORA, Continuous integration](https://dora.dev/capabilities/continuous-integration/) connects small integrated
  changes with rapid tests and prompt repair or reversion after failure.
  [Continuous delivery](https://dora.dev/capabilities/continuous-delivery/) develops deployability on demand,
  supported by technical, organizational and architectural capabilities. It is distinct from deploying every
  change. Reject transferring a software cadence or automated test's coverage to unrepresented physical use.
- **Adopt the concurrent and iterative application principle:**
  [SEBoK, Applying the Systems Approach, Application Principles](https://sebokwiki.org/wiki/Applying_the_Systems_Approach#Application_Principles)
  supports concurrent, iterative and evolutionary work. Its lifecycle presentation does not establish a fixed
  serial execution or a defect of the method. Section :4.1 preserves overlap while making particular reliance
  dependencies explicit.

The construction here connects the selected integration results to SYSE.10's ordinary assessment and,
only when another choice is live, to C.11. The worked margin and changed buffer premise show the bounded
consequence of that connection. They do not establish empirical superiority over a competent professional
integration programme. Qualification of domain models, equipment and tests remains real work in every
arrangement.

Reopen the comparison when a qualified existing strategy covers a previously missing interaction, an earlier
check fails to represent the installed relation, the cost or timing of intermediate integration changes, or a
different use invalidates the assessment's extension. A demonstrated lower-burden arrangement preserving the
same useful result also changes the selection. A newer source or a faster tool alone does not.

### SYSE.11:12 - Relations

- A compatible `SYSE.3` result supplies only the realization arrangement needed by this increment. Every relied-
  on unsupported branch must be closed, replaced by a qualified result, or retained as a blocker before Work
  uses it.
- A compatible `SYSE.12` result supplies pre-use platform capability and condition claims. Evidence produced by
  later participation or provision Work was not available to support the earlier decision.
- A compatible `SYSE.18` decision identifies the selected constituent arrangement and its unresolved
  dependencies. Rely on an obtaining commitment or observed coordination only when the accompanying evidence
  supports that claim; the decision alone supplies neither. `SYSE.13` supplies configuration and effectivity
  claims for the same Systems and use. Constituent outputs and the receiving Agent's authority need their own basis.
- `A.15.1`, `A.2.1`, and `A.3.1` distinguish Work, assignment, and enacted Method. `A.3.4` distinguishes actual
  transformations, and `A.15.PROD` governs claimed result production.
- `C.11.CRC` constructs a finite contribution comparison when a proposed change's contribution relative to the
  current configuration is not already explicit. `C.11` governs the next choice. Neither result is the later Work
  or transformation.
- SYSE.10:4.1 steps 6–8 and SYSE.10:4.1.1 supply the ordinary assessment inference and combination of results.
  The referenced instructions in SYSE.4:4.4 and SYSE.4:4.6 can be used without importing the separate assurance activities.
- A bounded usability assessment can inform SYSE.4 within its supported use and evidence window. SYSE.14
  retains release and evidence-continuity authority.
- Operations, Maintenance, Platform Engineering, safety, security, law, governance, finance, and other specialist
  practices retain their Methods and decisions.

### SYSE.11:End
