## E.23.CAE - Capability Access and Expression Differential Probe

> **Tech-name:** `CapabilityAccessAndExpressionDifferentialProbeMethod`
> **Plain-name:** test whether a capability is unavailable, unrecognized, unexpressed, unadapted, unenacted, or changed
> **Type:** Method-description pattern for an observation-first differential probe; coordinated with `E.23` and `E.23.CDI`
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### E.23.CAE:1 - Problem frame

**Use this when.** Use this pattern when one exact holder previously produced a result, passed a qualified reference test, or has a current capability claim for a named Work family, but performance now fails, transfers poorly, or changes with conditions. Use it only when the next question depends on distinguishing at least two of these possibilities:

- the demand lies outside the claimed capability envelope;
- a performer, tool, record, interface, authority, state, or other support is unavailable;
- an available response is not selected as applicable;
- a response cannot be accessed or activated;
- context or interference changes expression;
- an available response cannot be adapted to the changed demand;
- the response cannot be enacted in the current performer arrangement; or
- the holder's capability has actually changed.

**First useful move.** State the case in ordinary language:

> This holder previously obtained this result for this Work family under these conditions. The result now fails under this changed demand. Before more training, redesign, rehearsal, or parameter updating, return once to a qualified reference condition without further development, vary the smallest decision-bearing condition, and record which observable distinction changes first.

**First useful result.** Return the controlled observations, one or more qualified differential dispositions, the strongest surviving rival, the limits of the result, and candidate routes to the patterns or domain Methods that could receive it. The result is not a choice, authorization, selected next Work, performed Work, hidden memory, or causal mechanism.

**What changes in practice.** A practitioner no longer treats one failed performance as proof that the capability or memory disappeared. They first ask whether the claimed demand, configuration, cue or routing, applicability selection, response access, adaptation, and enactment can be separated by a safe contrast. Development or redesign begins only after a separate steering or choice result uses that evidence.

**What this buys.** The probe can recover a still-available response, avoid unnecessary redevelopment, identify the earliest observable failure position, and return a smaller next question to the right owner. It works across unlike holders because the common part is the contrast and disposition, not one theory of memory, organization, learning, or model internals.

**Not this pattern when.**

- Use `A.2.2` when only the holder, Work family, envelope, measures, evidence, or currentness of a capability instance must be stated.
- Use `A.15.8` when one exact Work or WorkPlan configuration and its recovery relation already bound the whole question.
- Use `E.23.CDI` when capability development has already been selected and the live question is the intervention and representative transfer check.
- Use `A.15.7` when ongoing Work merely needs one next action; use `C.11` only when a current chooser and `OptionSet` already exist and comparison can change the choice.
- Use the direct domain Method when a human memory mechanism, organization routine, continual-learning algorithm, robotic controller, medical condition, safety rule, threshold, or intervention is the live subject.
- Do not use one successful occurrence to infer a capability, and do not run a risky live probe when replay, simulation, staged testing, or another protected evidence route is required.

### E.23.CAE:2 - Problem

Apparent capability loss compresses different failures into one sentence: “they knew it yesterday,” “the organization forgot the routine,” “the model catastrophically forgot,” or “the robot cannot do it anymore.” Each sentence can trigger expensive or harmful Work before anyone checks whether the old response still appears under a qualified condition.

The opposite error is to explain every recovery with one theory. Human sensorimotor memories can be expressed according to contextual inference; conceptual knowledge can remain inert until relational retrieval; organizational performance can depend on roles, rules, records, artefacts, and authority; an AI function can remain represented while its activation is biased; a robot can retain a policy while sensing, state estimation, actuation, or configuration prevents enactment. These structures are not one memory system.

The reusable problem-solving move is narrower: bind one capability claim, control further change long enough to compare conditions, recover a reference response where possible, separate observable positions, retain rivals, and return an evidence-bounded disposition. The method must admit both genuine capability change and an unresolved result.

### E.23.CAE:3 - Forces

| Force | Tension |
| --- | --- |
| Exact claim versus familiar story | “Forgot” is recognizable, while the probe needs one holder, Work family, envelope, prior basis, current demand, and window. |
| Recovery versus transfer | Reappearance under an old condition can reject simple global loss, while it does not establish capability in the changed condition. |
| Controlled contrast versus ecological realism | One changed factor helps discriminate rivals, while actual contexts can be coupled, sequential, and partly hidden. |
| Observation versus mechanism | A shared contrast can guide unlike holders, while human memory, organizational routine, AI routing, and robotic control need different explanations. |
| Probe versus intervention | A clean contrast should avoid new learning or updating, while repeated trials can themselves train, prime, fatigue, adapt, or reorganize the holder. |
| Useful disposition versus premature choice | The result should change the next question, while it must not become a `ChoiceResult`, authorization, or selected Work. |
| Information versus safety and cost | Another contrast can reduce uncertainty, while live probing can be unsafe, disruptive, slow, or too expensive. |

### E.23.CAE:4 - Solution

#### E.23.CAE:4.1 - Bind the claim before probing

Name only the values that can change the probe or its later use:

1. the exact holder System;
2. the named Work family or exact current demand;
3. the capability envelope, measures, evidence, and qualification window currently relied upon;
4. the prior qualified result or reference condition;
5. the present failure or unstable expression;
6. the relevant performer and support configuration;
7. any development, rehearsal, procedure change, parameter update, model update, calibration, or other change that must be held fixed where safe;
8. protected conditions and probe limits; and
9. the receiving question that a differential observation could change.

If the holder or Work family is unclear, return to `A.2.2`. If the current demand is already outside the claimed envelope, return `outsideClaimedEnvelope` and stop the loss diagnosis. If a known configuration failure fully explains the case, use `A.15.8` and stop here.

For a compact retained account, use this local shape only when another use needs it:

```text
CapabilityAccessExpressionProbe@Use:
  holderRef:
  workFamilyOrDemand:
  claimedEnvelopeAndWindow:
  priorReferenceCondition:
  presentObservation:
  controlledChangeCondition:
  protectedConditions:
  disposition:
  strongestSurvivingRival:
  unsupportedUse:
  candidateRoutes:
```

This card is a local Method result, not a new FPF kind. Its fields create no capability, context, memory, choice, authorization, Work, or causal relation.

#### E.23.CAE:4.2 - Run the differential probe

1. **Check the demand against the claim.** Confirm that the current task belongs to the Work family and capability envelope being relied upon. Compare measures and qualification windows before calling a difference loss or transfer failure.
2. **Recover the relevant configuration.** Name actual or intended performers, roles, tools, records, interfaces, authority, environmental conditions, state, and other supports only where their direct rules apply. Use `A.15.8` when one exact Work or WorkPlan configuration is current.
3. **Hold development and updating fixed.** During the contrast, avoid new teaching, rehearsal, procedure rewrite, fine-tuning, parameter update, recalibration, or other development where safe and feasible. If the probe necessarily changes the holder, mark the affected distinction unresolved or narrow the claim.
4. **Return to a qualified reference condition.** Recreate a previously successful or separately qualified condition without further development. Prefer an `A → B → A` or equivalent return when order, recency, or transition history can matter. Reappearance rejects simple global loss under those tested conditions; it does not establish general transfer.
5. **Vary a decision-bearing condition.** Change the smallest condition that can distinguish live rivals: an overt cue, cue reliability, preceding decision state or uncertainty, role, record, authority, tool, task or context identifier, state feedback, blocked versus interleaved order, transition frequency, or another domain-relevant condition. A label or visible setting is not assumed to be the effective context.
6. **Observe applicability separately.** Ask whether the relevant Method, response, routine, policy, or prior case is selected as applicable before judging execution. For a person this may involve recognition or choice; for an organization it may involve routing, role, record, or authorization; for AI or robotics it may involve task/context identification, policy routing, or function activation. These are different mechanisms occupying one observational position.
7. **Separate availability, adaptation, enactment, and result.** Where the case permits, observe whether the response can be accessed or activated, whether it can be transformed for the changed demand, whether the actual performer arrangement can enact it, and whether the required result obtains. A later failure does not by itself establish an earlier one.
8. **Compare live rivals.** Retain every explanation still compatible with the observations. Ordinary cue effects, interference, envelope mismatch, configuration loss, applicability failure, access or activation failure, adaptation failure, enactment failure, and actual holder change are not synonyms.
9. **Return a disposition and candidate routes.** State the earliest supported distinction, evidence and conditions, strongest surviving rival, unsupported overread, and patterns or domain Methods that could receive the result. Do not select a route merely because the probe produced a disposition.

These steps organize observations, not a universal cognitive pipeline. A holder may implement them through simultaneous, recurrent, distributed, or structurally different processes.

#### E.23.CAE:4.3 - Qualify the disposition

| Differential disposition | Minimum useful observation | Candidate route | What the observation does not establish |
| --- | --- | --- | --- |
| `outsideClaimedEnvelope` | The current demand differs on an envelope coordinate excluded from or unsupported by the current capability claim. | Reframe the claim through `A.2.2`, or open development only through a separate next-action or choice result. | Loss or forgetting inside the old envelope. |
| `configurationOrSupportUnavailable` | Performance changes with a controlled performer, role, record, tool, interface, authority, state, or environment contrast. | `A.15.8` and the direct owner of the failed relation. | Changed holder capability or a human-like memory in a collective. |
| `responseAvailableUnderReferenceCondition` | The prior response or result reappears in a qualified reference condition without new development or update. | Probe applicability, transfer, adaptation, or enactment; then use the applicable steering or choice pattern. | Whole-envelope capability, a particular retrieval mechanism, or sufficient transfer. |
| `applicabilitySelectionFailureSupported` | The response can be produced when selected or prompted, but is not identified, routed, or authorized as applicable under the target demand. | Holder-specific HCD, organization, AI/robotics, or domain inquiry; `A.15.7` or `C.11` only under their own entry conditions. | One common recognition mechanism or the intervention to choose. |
| `accessOrActivationFailureSupported` | Applicability is established, yet access or activation changes under a controlled cue, task/context, or routing contrast before adaptation and enactment. | Holder-specific access, retrieval, activation, or routing inquiry. | Erased content, a universal latent context, or a sufficient repair. |
| `contextDependentExpressionOrInterferenceSupported` | Expression changes systematically with a qualified context, cue-reliability, or transition-statistics contrast and can reappear without development. | Holder-specific explanation and development Method when separately selected. | The hidden context representation or memory architecture that caused the observation. |
| `adaptationFailureSupported` | The response is selected and available, but cannot be transformed to the changed demand while enactment supports are adequate. | Direct adaptation or domain Method inquiry. | Loss of the original response or the correct adaptation Method. |
| `enactmentFailureSupported` | The response or adapted Method is selected and available, but performer assignment, coordination, authority, body, actuator, interface, tool, or another condition prevents actual Work or its result. | `A.15.8`, performer/authority owners, and the direct domain Method. | Capability change when the necessary performer arrangement did not obtain. |
| `capabilityClaimRevisionWarranted` | Qualified reference and target probes fail across relevant conditions, envelope and configuration rivals have been addressed, and holder-specific evidence supports changed ability in the stated window. | Reassess the `A.2.2` capability claim; use a separate steering or choice result before development. | A specific human, organizational, model, or controller memory mechanism. |
| `unresolvedDifferential` | Safety, missing reference evidence, concurrent updating, coupled changes, insufficient measures, or surviving rivals block a responsible distinction. | Obtain the missing evidence, use a protected test, narrow the claim, or stop. | Permission to choose the most familiar explanation. |

One case may support several ordered dispositions. Keep each observation and its limits visible. No disposition is a `ChoiceResult`, authorization, selected next Work, or performed Work.

#### E.23.CAE:4.4 - Keep recognition and assurance separate

**Recognition.** A quick return probe is warranted when the practitioner hears “it worked before,” “the model forgot,” “the team knows the routine,” “the dancer can do it only in class,” or another apparent-loss phrase and at least two live explanations would lead to different next Work.

**Assurance.** Stronger reliance needs proportionate evidence:

- a qualified reference basis rather than a nostalgic recollection or one cherry-picked success;
- commensurable measures, envelopes, configurations, and windows;
- protection against probe-induced learning, fatigue, priming, adaptation, or update;
- enough order, cue-reliability, and transition variation to address the live rival;
- replay, simulation, staged testing, or specialist assurance when live probing would be unsafe; and
- holder-specific evidence before claiming a memory mechanism, causal explanation, or actual capability change.

A cheap reversible probe can support a narrow disposition. A high-stakes capability-loss, safety, medical, employment, deployment, or public-performance decision may require a direct domain evaluation and assurance account before anyone relies on the result.

#### E.23.CAE:4.5 - Route without choosing

The first result should fit in six lines:

> **Claim tested:** [holder, Work family, envelope, window].
> **Controlled contrast:** [reference, changed condition, and what was held fixed].
> **Observation:** [what reappeared, disappeared, or changed first].
> **Disposition:** [qualified differential result].
> **Surviving rival and limit:** [what remains plausible and what is not established].
> **Candidate routes:** [patterns or domain Methods that could receive the result].

During ongoing Work, `A.15.7` can use the disposition as current information while recovering a next action. Use `C.11` only when a current chooser and `OptionSet` already exist and comparison or another probe can change the choice. `E.23.CAE` supplies neither pattern's result. Use `E.23.CDI` only after a separate applicable steering or choice result selects capability development.

### E.23.CAE:5 - Archetypal Grounding

#### E.23.CAE:5.1 - Human knowledge that remains inert

**Tell.** A practitioner can explain a structural decision principle when it is named but does not use it in a differently worded workplace case. The failure may concern retrieval, recognition of applicability, adaptation, enactment, or an envelope limit; “they forgot” decides none of these.

**Show.** First confirm that the workplace case lies inside the claimed capability envelope. Without reteaching, present a qualified reference case that the practitioner previously solved, then the workplace case, then the reference again. Ask separately whether the principle is relevant before asking for a solution. If a structural comparison makes the principle recognizable and the practitioner can then adapt it, the observations support availability plus an applicability-selection failure under the uncued condition. They do not prove one universal retrieval mechanism or complete workplace capability. Human Capability Development or a direct domain Method can receive the result only after a separate next-action decision.

This is the minimally viable case: one holder, one Work family, one reference return, one applicability observation, one changed demand, one disposition, one surviving rival, and one candidate route.

#### E.23.CAE:5.2 - Organizational handover

**Tell.** An incident-handover arrangement previously obtained an accepted result, then fails after a shift, tool, role, record, or authority change. Calling this “organizational forgetting” hides the exact relation that changed.

**Show.** Name the admitted organizational holder or performer arrangement and the handover Work. Compare the earlier roster, record, dispatch tool, authority, and interface configuration with the current one. Run a protected `A → B → A` replay or simulation: established configuration, changed configuration, then restored configuration. Observe which routine or Method is selected, whether it can be adapted to the new shift, whether authorized performers enact it, and whether the handover result obtains. If the result returns when record access and authority are restored, `configurationOrSupportUnavailable` is supported. Routine theory, organization design, staffing, governance, and collective learning remain OCE or organizational questions; no human-like organization memory has been established.

#### E.23.CAE:5.3 - AI or robotic apparent forgetting

**Tell.** A continually updated model or robot previously expressed a task function or policy and later appears to forget it. A benchmark drop can reflect parameter change, task/context routing, function activation, interface state, sensing, actuation, support configuration, or a demand outside the tested envelope.

**Show.** Hold parameters fixed during the probe where feasible. Compare no task/context cue with a qualified task cue or routing intervention; vary cue reliability, state feedback, blocked versus interleaved order, and relevant transition statistics; then return to the earlier condition without further update. For a robot, keep sensing, controller state, actuation, calibration, tool, and environment conditions explicit. If the earlier function or policy reappears under a qualified activation condition, availability under that condition is supported and simple global loss is weakened. Function vectors, context inference, routing, controller state, continual-learning algorithms, and parameter overwrite remain model-specific explanations. If no response reappears and direct model or controller evidence supports change, `capabilityClaimRevisionWarranted` may be returned without claiming a universal memory mechanism.

### E.23.CAE:6 - Bias-Annotation

**Scope: limited.** This pattern supplies a conservative cross-holder probe and disposition. It supplies no universal memory substrate, latent context, capability pipeline, organization-learning theory, continual-learning algorithm, intervention catalogue, or choice rule.

| Lens | Declared bias and counter-check |
| --- | --- |
| **Gov** | Favors delaying redevelopment until a cheaper differential observation is available. Counter-risk: delay itself causes harm. Use the protected or specialist route and stop when the next probe is not safe or decision-relevant. |
| **Arch** | Favors one exact holder and explicit configuration. Counter-risk: an organization, team, equipped person, AI service, or robot is admitted as one whole merely because the label is convenient. Reapply the System and capability boundaries. |
| **Onto-Epist** | Favors separating capability, response, observation, disposition, mechanism claim, choice, Work, and causal claim. Counter-risk: local field names appear to create new kinds. Keep the compact ordinary result and expose the card only for a named receiving use. |
| **Prag** | Favors an `A → B → A` or similarly discriminating contrast. Counter-risk: repeated probing changes the holder or exceeds its value. Record contamination, narrow the claim, or return `unresolvedDifferential`. |
| **Did** | Favors human, organizational, and AI/robot cases to block a human-only analogy. Counter-risk: readers copy case-specific interventions. Reuse only the common observation positions and return mechanisms and interventions to their owners. |

### E.23.CAE:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-E23CAE-1` | One exact holder, Work family or demand, claimed envelope, evidence basis, and qualification window are explicit. |
| `CC-E23CAE-2` | A prior qualified result or reference condition exists; one anecdote or familiar label is not substituted. |
| `CC-E23CAE-3` | The current demand is checked against the claimed envelope before loss, forgetting, or transfer failure is asserted. |
| `CC-E23CAE-4` | Relevant performer and support configuration is stated, with `A.15.8` used when that exact configuration question is live. |
| `CC-E23CAE-5` | Development, rehearsal, procedure change, parameter update, calibration, or another holder-changing operation is controlled where safe; contamination narrows or blocks the disposition. |
| `CC-E23CAE-6` | A qualified reference return and at least one decision-bearing condition distinguish live rivals; cue reliability, order, and transition history are included when they can change the observation. |
| `CC-E23CAE-7` | Applicability selection, response access or activation, adaptation, enactment, and obtained result are not inferred from one undifferentiated success or failure. |
| `CC-E23CAE-8` | The disposition names its observation, conditions, strongest surviving rival, unsupported overread, and claim limit. |
| `CC-E23CAE-9` | Human, organizational, AI, robotic, collective, or hybrid explanations and interventions remain with their direct owners; no common hidden mechanism is asserted. |
| `CC-E23CAE-10` | The result remains a premise and candidate-route set, not a `ChoiceResult`, authorization, selected next Work, or performed Work. |
| `CC-E23CAE-11` | Unsafe, overly costly, coupled, or change-inducing probes return a protected alternative, narrower claim, or `unresolvedDifferential`. |
| `CC-E23CAE-12` | Reopen conditions include changed holder, Work family, envelope, configuration, source, cue structure, update state, measure, evidence, window, or direct-consumer contradiction. |

### E.23.CAE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| “It failed, so the capability is gone.” | Envelope, support, applicability, access, adaptation, and enactment remain untested. | Bind the claim and run the smallest safe differential contrast. |
| “It returned, so nothing changed.” | Reference recovery is mistaken for transfer or whole-envelope capability. | State the tested condition and continue only with the distinction the receiving decision needs. |
| “The organization remembered.” | Roles, records, rules, tools, authority, and actual performance collapse into a human-memory metaphor. | Name the exact organizational relations and actual Work; retain organization-specific explanation. |
| “The model catastrophically forgot.” | Benchmark failure is treated as parameter overwrite without routing or activation probes. | Hold update fixed and test qualified task/context activation before making a model-specific change claim. |
| Cue theater | A visible label is varied while the decision-bearing state, uncertainty, order, or transition statistics remain unchanged. | Vary the condition that distinguishes the live rivals and state what was held fixed. |
| Probe that teaches | Repeated trials, prompts, correction, or fine-tuning alter the holder while being called measurement. | Record the intervention, narrow the claim, redesign the contrast, or return unresolved. |
| Disposition as decision | A candidate route is written as selected development, authorization, or performed Work. | Pass the result to `A.15.7`, `C.11`, or the direct owner under its own entry conditions. |
| Universal stage pipeline | The observation order becomes a cognitive or organizational architecture. | Keep the order methodological; allow simultaneous, recurrent, distributed, and holder-specific implementations. |

### E.23.CAE:9 - Consequences

The pattern reduces premature retraining, redesign, procedure rewrite, and parameter updating by making still-available responses observable before a capability claim is revised. It also returns smaller questions: configuration recovery, applicability selection, access or activation, adaptation, enactment, development, claim revision, or honest uncertainty.

The cost is a qualified reference basis, controlled contrast, explicit claim boundary, and possible protected replay or simulation. Context dimensions can be coupled, reference evidence can be stale, and the probe can change the holder. A narrow unresolved result is therefore a successful outcome when the available evidence cannot support a stronger distinction.

What changes in practice is not the adoption of one memory theory. It is the refusal to move directly from failed expression to capability loss or development Work without first asking which observable contrast could change that conclusion.

#### Reopen condition

Revisit this pattern when a current FPF neighbor supplies the whole differential with less burden; actual human, organizational, and AI or robotic uses cannot share the observation-only action; a direct source correction removes a load-bearing contrast; a new direct consumer requires a different disposition; or repeated uses show that one observation position is an independent Method with its own result and boundary.

### E.23.CAE:10 - Rationale

A capability is bounded by holder, Work family, envelope, measures, evidence, and currentness. One failed occurrence does not rewrite that claim automatically. A controlled return to a qualified condition can cheaply distinguish global change from availability under at least one condition, while separate applicability, access, adaptation, and enactment observations prevent a later-stage failure from being projected backward.

The method stays transdisciplinary only by refusing a common hidden mechanism. Its common result is the smallest one that the unlike cases can honestly share: observation, disposition, surviving rival, limit, and candidate routes.

### E.23.CAE:11 - SoTA-Echoing

**Practice question.** When prior performance, failed transfer, or unstable expression leaves several live explanations, what is the smallest current defensible move that distinguishes an envelope or configuration failure, applicability or access failure, context-dependent expression, adaptation or enactment failure, and actual capability change without yet choosing development or repair Work?

**Selected best-known line and serious alternatives.** **Adopt** an observation-first differential: bind the capability claim, hold development or updating fixed where safe, return to a qualified reference condition, vary the smallest decision-bearing condition, separate the observable failure positions, and retain genuine-change and unresolved exits. The serious defaults are to infer capability loss and begin development immediately, or to **adopt** a latent-context or COIN-style explanation as the common mechanism. At comparable first-decision effort, the selected line can be as small as one safe reference return and one discriminating contrast. It is no worse on affordability, safety honesty, or admission of genuine change, and it is better at avoiding premature redevelopment and cross-holder mechanism overreach. Its deliberate cost is that the extra contrast needs a qualified basis, may contaminate or endanger the case, and may truthfully return `unresolvedDifferential`.

**Defect overcome and pattern mutation.** Immediate loss/development projects one failed expression backward into capability change; a universal latent-context account projects one useful human explanation across non-isomorphic holders. The selected line changes `E.23.CAE:4.2` steps 4–8, the observation-qualified dispositions in `4.3`, the three holder cases in `5`, the assurance stop in `4.4`, the anti-patterns in `8`, and the source-sensitive reopen condition in `9`. It leaves mechanisms and interventions with their direct owners.

| Comparison role and source | Material move and receiving locus | Retained limit |
| --- | --- | --- |
| Best-known human contextual-expression line: Heald, Lengyel, and Wolpert, [*Contextual inference underlies the learning of sensorimotor repertoires*](https://doi.org/10.1038/s41586-021-04129-3), 2021, and [*Contextual inference in learning and memory*](https://doi.org/10.1016/j.tics.2022.10.004), 2023; Ogasa et al., [*Decision uncertainty as a context for motor memory*](https://doi.org/10.1038/s41562-024-01911-x), 2024; Kumar et al., [*Contextual cues and transition statistics drive expression of competing motor memories*](https://doi.org/10.1016/j.isci.2026.116281), 2026. | **Adapt** recovery without relearning, preceding decision uncertainty, cue reliability, order, recency, and transition statistics into `4.2` steps 4–5, the human and AI/robot contrasts, and the assurance check. **Reject** latent-context inference as a required FPF object or universal explanation. | Human sensorimotor experiments and synthesis do not establish an organization, AI, or robotic memory mechanism, one mandatory schedule, or sufficient transfer. |
| Human recognition-and-application line: Gentner, Loewenstein, Thompson, and Forbus, [*Reviving inert knowledge: Analogical abstraction supports relational retrieval of past events*](https://doi.org/10.1111/j.1551-6709.2009.01070.x), 2009; Corral and Carpenter, [*Effects of retrieval practice on retention and application of complex educational concepts*](https://doi.org/10.1016/j.learninstruc.2025.102219), 2025. | **Adapt** the separation of stored or available knowledge, recognition of applicability, and later application into `4.2` steps 6–7 and the minimally viable human case in `5.1`. **Reject** analogical training or retrieval-practice dose and timing as the generic probe. | These human learning results do not define other holders' applicability mechanisms or select an instructional intervention. |
| Organizational-routine counterline: D'Adderio, [*The performativity of routines: Theorising the influence of artefacts and distributed agencies on routines dynamics*](https://doi.org/10.1016/j.respol.2007.12.012), 2008. | **Adapt** the separation of formal routine, actual performance, artefacts, roles, records, and distributed agency into the configuration and enactment observations in `4.2`, `4.3`, and `5.2`. **Reject** human-like organizational memory as the common explanation. | One longitudinal automotive case does not supply universal organization theory, staffing or governance Methods, or a capability-change decision. |
| AI activation counterline: Jiang et al., [*Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning*](https://proceedings.iclr.cc/paper_files/paper/2025/hash/74fc5575632191d96881d8015f79dde3-Abstract-Conference.html), ICLR 2025. | **Adapt** the test of task/context routing or activation under fixed parameters before an overwrite claim into `4.2`, `4.3`, and `5.3`. **Reject** benchmark decline as sufficient proof of parameter loss and reject function vectors as the common cross-holder mechanism. | Function vectors, tested models, benchmarks, activation account, and mitigation remain model-specific; robotics also retains sensing, controller, actuation, calibration, and safety questions. |

Reopen this comparison when a direct-source correction removes a load-bearing contrast; a stronger current line supplies an equally safe, cheaper, or more discriminating first move; actual human, organizational, and AI or robotic uses cannot share the observation-only action without importing one holder's mechanism; or a direct consumer requires a different disposition or assurance boundary.

### E.23.CAE:12 - Relations

| Pattern or practice | Relation |
| --- | --- |
| `A.2.2` | Supplies the exact holder-dependent capability instance, Work family, envelope, measures, evidence, qualification window, and currentness. The differential probe does not create or update that capability claim automatically. |
| `A.13`, `A.15.1`, `A.2.1`, `F.6` | Govern actual performer recovery, dated Work admission, assignment, and precise assignment-bound attribution independently when those claims are current. A probe result establishes none of them by itself. |
| `A.15.8` | Governs an exact Work or WorkPlan performance configuration and recovery. Its observation may support a configuration disposition here; this pattern does not absorb its relation tests. |
| `E.23.CDI` | Receives the result only after a separate applicable steering or choice result selects capability development. It retains limiting-contribution diagnosis, intervention, protected conditions, and representative transfer. |
| `E.23` | Uses this pattern first only when the proposed object under improvement remains ambiguous because a capability may be available but inaccessible, unexpressed, unadapted, or unenacted. It retains the repeated object-improvement loop. |
| `A.15.7` | May use the disposition as current information for a light next action during ongoing Work. It retains chooser, performer, authority, action, and feedback; no amendment is required. |
| `C.11` | May use the disposition as a premise when a current chooser and `OptionSet` exist and comparison or another probe can change the choice. It alone emits the `ChoiceResult`; no amendment is required. |
| `E.22`, `A.10`, `B.3` | Govern an explicit evaluation frame, evidence reliance, and assurance when a receiving use needs them. The probe record is not evidence or assurance by form. |
| `E.10.LRN` | Repairs ambiguous learning wording; it supplies no substantive differential probe or holder-specific learning Method. |
| `C.36` | Governs cultural generation, transmission, reconstruction, recognition, selection, retention, and loss across a population. Cultural continuation is not one holder's capability or response availability. |
| HCD, OCE, AI and robotics, MDPE, health, and exact domain practices | Retain holder-specific mechanisms, development Methods, interventions, thresholds, safety rules, and evidence. They consume only the observation and disposition their use requires. |

### E.23.CAE:End
