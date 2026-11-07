## SYSE.10 - Assess Research, Model, and Trial Results for an Engineering Decision

> **Status:** Stable

### SYSE.10:0 - Use This When

Use this pattern when an engineering decision relies on a knowledge or evidence input such as a theory,
heuristic, model, simulation result, benchmark result, experiment, prototype trial, test result, operating
observation, or research paper, but the project has not said what engineering claim the input supports, where
that support stops, or how the decision changes.

Begin with one sentence: “This decision may rely on this claim about this subject, configuration, use, and
interval.” Then connect each source or produced result to that claim and state whether it supports, contradicts,
narrows, or leaves the claim unresolved. The first useful result is a **bounded engineering claim assessment**
that names the decision effect and any material claim it still leaves unsupported.

A small reversible choice may need only that sentence and its source. A fuller assessment is useful, for example,
when several evidence bases disagree, the result must survive handoff or delay, automation obscures provenance,
or an error would be costly. The assessment is an episteme about evidence use and its decision effect. It cites
the separately identified sources, subjects, Work, results, and any assurance or acceptance decision on which it
relies.

Use `A.10` directly when ordinary evidence reliance needs no Systems Engineering specialization. Use `C.28` for
causal, interventional, or counterfactual support; `C.11` when deciding whether one further probe is worth its
cost before a local choice; and a specialist experimental-design Method for a set or sequence of experiments.
For an ordinary assessment that must explain an extension or combination, use the inference construction in
[SYSE.4:4.4](41-syse-4---decide-whether-and-how-to-challenge-an-engineering.md#syse444---recover-performed-work-direct-results-and-evidence-use) and the combination rules in
[SYSE.4:4.6](41-syse-4---decide-whether-and-how-to-challenge-an-engineering.md#syse446---combine-evidence-only-for-the-decision-question), as applied in :4.1.1 below. Their use
here needs no assurance conclusion. Use the wider `SYSE.4` Method when assurance or a release-facing consequence
is the actual question. Scientific and specialist practices retain their own research Methods.

#### SYSE.10:0.1 - Terms and Distinctions

The same research word can name a Method, dated Work, a result, or a publication. Restore the object and
relation needed by the engineering claim:

| Name in this pattern | What it denotes |
| --- | --- |
| research result | An episteme produced or revised by inquiry Work. A paper or another publication carries claims; identify the Agent and inquiry Work separately when their performance matters. |
| theory, hypothesis, or heuristic | A theory or hypothesis is a claim-bearing episteme proposed for explanation, prediction, or criticism. A heuristic may supply a context-dependent Method or a claim about such a Method for search, diagnosis, or choice. Use either as evidence only through a bounded evidence relation. |
| model or mathematical lens | A model is a description used for a stated subject, purpose, assumptions, omissions, and validity boundary. A mathematical lens additionally states its correspondence, preserved and lost structure, practical gain, and unsupported inference under `C.29`. The represented subject remains separately identified. |
| simulation | Plain wording that may denote a simulation Method, one dated simulation Work occurrence, or its result. For a relied-on result, identify the Agent, Method, model, Work, inputs, and produced result separately. A simulation result concerns model behavior unless a separate evidence relation supports a physical claim. |
| experiment, trial, or test | Plain words that may denote reusable Methods or dated evidence-producing Work. An experiment varies selected conditions to distinguish claims; a trial exposes an actual configuration to selected conditions; a test applies a Method and criterion to a named claim. State the Method, Work, and result separately. |
| verification, validation, or calibration | Plain words that may name a Method, dated Work, comparison, or result claim about a named subject. State that subject, the applied criterion or comparison, and the result. Calibration can improve fit while transfer and future adequacy remain separate questions. |
| observation or measurement result | An observation is an episteme about an occurrence or state. A measurement result attributes a value to a measurand with its Method, model, calibration, uncertainty, and time. The observed occurrence or measured state remains separately identified. |
| evidence | Use of an episteme for a named claim with provenance, polarity, scope, relevance window, and reliance limit under `A.10`. Citation or availability alone does not establish this use. |
| acceptance or assurance | An acceptance result records application of a governed rule to a named subject and input. An assurance result addresses a named assurance claim and reliance threshold. Each has its own Method, Work, authority, and evidence when those facts matter. |
| engineering claim assessment | The episteme produced here: which claims the named evidence supports, contradicts, narrows, or leaves unresolved for one engineering decision. |

A dashboard or report may display several of these objects together. Identify each object and relied-on relation
before using the display in an engineering decision.

### SYSE.10:1 - Problem Frame

Engineering decisions often precede complete knowledge. Models make alternatives cheap to explore; experiments
and trials expose selected parts of reality; operating observations arrive only after use. Each can be valuable
without supporting the whole decision.

For example, a heat-transfer model can compare storage concepts while saying little about installation error. A
controller bench can expose timing and interface faults while omitting occupants and seasonal operation. A field
trial can support one configuration in one environment while leaving rare failures and another variant
unresolved. A formal proof can establish a property of a formal object while leaving the implementation-to-model
correspondence unsupported.

Projects fail in both directions. Scientific or mathematical prestige is promoted to a universal engineering
law, so “the model says” or “research proves” dictates the design. Or useful partial knowledge is rejected
because it cannot settle the whole outcome. The engineering move is to use the claims supported by the
current basis, state the material limits on reliance, and show what changes in the decision.

### SYSE.10:2 - Problem

A decision-usable assessment answers seven questions:

1. Which decision and alternative can change?
2. What claim about which subject, configuration, environment, use, interval, scale, and criterion is at issue?
3. What theory, model, observation, prior result, or other source is current, and what are its transfer limits?
4. Which Agent performed the dated Work that produced each result, which Method did that Work apply, and which inputs, tools, and physical or simulated subject did it use?
5. Why does the result support or challenge this claim, and which extension or joint premises does that inference need?
6. What could overturn the reliance—for example, a rival explanation, shared assumption, configuration mismatch,
   failed trial, or affected-System consequence?
7. What decision effect follows—for example, a changed choice or constraint, another probe, postponement, redesign,
   or stop—and what later change reopens the assessment?

Without these answers, *validated*, *verified*, *passed*, *peer reviewed*, and *AI confidence* become authority
labels. Conversely, *not proved* becomes an excuse to ignore a well-scoped result that should change a reversible
choice.

### SYSE.10:3 - Forces

- Waiting for exhaustive evidence can destroy opportunity; relying on an unbounded claim can create avoidable
  harm and rework.
- Useful models omit detail deliberately. The missing structure matters only when it can overturn the decision.
- Simulations and formal analyses run quickly; later physical conditions such as manufacture, installation,
  wear, environment, and use may dominate the eventual result.
- Different practices use *verification* and *validation* for different subjects and relations. One universal
  ladder hides the current engineering question.
- More evidence costs time and can repeat one shared assumption. `C.11` governs one next local probe; specialist
  experimental design governs a non-myopic set or sequence.
- Independent criticism can expose common-mode error; collaboration can repair subject and interpretation
  mismatch. Neither arrangement is always superior.
- AI Agents can generate artifacts such as models, tests, scenarios, and summaries at scale. The same scale can
  amplify source opacity, benchmark leakage, hidden tool changes, and integration errors.
- Counterevidence—including failed trials, abstentions, contradictions, and out-of-envelope results—can matter
  more than the positive cases favored by publication and project reporting.

### SYSE.10:4 - Solution

Assess each engineering claim against the results actually available, preserve the distinction between model
behavior and physical evidence, and supply a supported reliance limit to the receiving decision. An authorized
Agent uses `C.11` or a specialist experimental-design Method when further evidence is a live alternative: the
choice determines whether to obtain it and, if so, which Work to undertake. This choice and any resulting probe
or experiment design remain separate from the later assessment of available results described here.

#### SYSE.10:4.0.1 - Keep Different Decision Inputs Distinct

Keep each decision input's kind explicit. An evidence-bearing result keeps its kind; state how it bears on a
named claim under `A.10`. An objective, reward, loss, or heuristic enters `C.11` as the evaluative or choice-rule
input it actually supplies; a number does not make it evidence. A novelty or surprise characterization remains a
characteristic claim. Use `SYSE.10` to assess the engineering claim and its evidence use. The deciding Agent
separately applies `C.11` to choose a current option or record a next-probe result.

#### SYSE.10:4.1 - Perform the Move

1. **Name the decision and claim.** State the alternatives, deciding Agent, consequence, needed interval, and
   claim whose support can change the choice. Bind the claim to a subject, configuration, environment, use,
   interval, scale, and criterion.
2. **Recover the current knowledge basis.** Identify the relevant source epistemes and editions, including
   explanations, hypotheses, heuristics, models, mathematical lenses, observations, prior Work, and contradictory
   results. State their currentness and transfer limits. Identify the receiving claim separately from the sources' own claims.
3. **State what each result can distinguish.** Name the rival claims or alternatives, applicable conditions,
   inputs and controls, measurements, sensitivity, uncertainty, and the result that would leave the decision
   unchanged. If the live problem is choosing one further probe, use `C.11`; for an experiment set or sequence,
   use a specialist experimental-design Method.
4. **Qualify model and representation use.** State the modeled subject, purpose, assumptions, omissions,
   parameters, boundary conditions, solver or inference Method, verification, calibration, validation,
   uncertainty, sensitivity, and extrapolation boundary needed by this claim. Use `C.29` for a mathematical
   correspondence and loss account.
5. **Identify Work, observations, and measurements.** Keep planned Work separate from dated Work. Name the
   performing Agent, enacted Method, tools, resources, subject configuration, inputs, controls, disturbances,
   result production, calibration, measurement interval, uncertainty, and missing data to the degree the claim
   needs.
6. **Explain the inference and construct the evidence use.** Start with the result's own claim and show why it
   bears on the receiving engineering claim. Reuse a sufficient direct result or specialist argument with its
   conditions. Where the receiving claim extends or combines results, construct the missing connection through
   :4.1.1. Retain the target, polarity, actual grounding subject when relevant, source scheme, scope, relevance
   window, provenance and unsupported use. Use `C.28` for a causal or counterfactual step.
7. **Compare and criticize.** Try to make the relied-on results hold while the receiving claim fails. Examine
   the consequential extension or joint premise, including shared assumptions, implementation-to-model gaps,
   configuration mismatch, rival explanations, contradictory results, selection effects, extrapolation and
   affected-System evidence omitted by the original study. Keep an unsupported inference distinct from
   evidence that actually contradicts the claim.
8. **Record the assessment and decision effect.** State what is supported, contradicted, narrowed, or unresolved;
   the reliance limit; residual uncertainty; and any material unsupported claim. Then state the resulting engineering
   action—for example, choose, narrow, postpone, redesign, seek evidence, or stop. The assessment itself supplies
   neither the decision nor its authority.
9. **Stop and reopen deliberately.** State why the current basis is enough for this decision. Record a compatible
   `C.11` result or specialist experimental-design result when further evidence is chosen. Name the later change
   that would matter, such as a change to a relied-on source, configuration, environment, use, Method, capability,
   observation, or claim.

Evidence-producing Work may overlap, iterate, or occur in another order. A physical trial can precede simulation
during reverse engineering; operating evidence can reopen theory and architecture; a formal check and bench trial
can address different claims concurrently.

##### SYSE.10:4.1.1 - Explain What Makes the Results Sufficient

Use the developed inference and combination instructions in `SYSE.4:4.4` and `SYSE.4:4.6` for the part of this
assessment that is missing. The receiving result remains an engineering claim assessment. These instructions
do not require the other assurance activities when no assurance claim is being made.

**Work backward from the needed claim.** Recover what the receiving decision actually requires. A temperature
claim and a compressor-cycling claim may both be necessary; evidence for one cannot compensate for the other.
Identify which available result addresses each necessary premise or operating case. When several arguments
instead offer alternative grounds for the same claim, determine whether any one is sufficient. A source may
generate a candidate, explain a phenomenon or report an association without supplying the support this decision
needs. Keep that useful contribution in its own role.

**Follow each contribution forward.** State what its Method and performed Work directly establish under their
own conditions. Then explain the consequential step to the receiving claim. For a qualified measurement of the
required quantity under that claim's conditions, comparison with the criterion may finish the assessment.
A sufficient specialist argument can be cited with its applicability and limits; neither a second diagram nor
a new trial is required.

An extension needs its actual reason. For example, a prediction about an installed controller needs a justified
correspondence between the model's inputs and the installed configuration. A component limit needs a reason
that interactions and operating conditions preserve it in the whole System. Follow `A.1.1` for model
applicability and `C.28` for causal support when those contributions are missing. State which premise has
support and which remains an assumption, why that assumption is allowable for this use, and which inference
loses support if that premise is false. An assumption cannot substitute for evidence required by the receiving rule. Unknown units,
configuration or timing cannot be repaired by relabeling the result.

**Explain the join.** Check that the necessary results apply together: the same configuration and operating
cases, compatible definitions and units, and no omitted interaction on which the conclusion depends. Use the
domain's combination rule and its qualifications. Bounds on consecutive parts of one path can bound its total
only when they cover that whole path under compatible conditions; component averages or confidence ratings do
not supply those bounds. Do not add uncertain quantities or multiply confidence values without the appropriate
measurement or probability relation. Two accounts copied from one trace do not add an independent observation.
Preserve shared premises so that a correction can reach every dependent use.

**Challenge the reason and return the surviving claim.** Could every listed result still be true while the
required claim is false? An untested operating region, unrepresented interaction or different interpretation of
the same word may expose that possibility. Resolve an action-changing challenge using the available domain
results or keep the whole claim unresolved while retaining supported parts. A failed bridge removes its support;
it establishes a contrary physical claim only with further grounds. When several necessary premises are
established and their joining rule suffices, return the bounded assessment and its decision effect. Stop there
unless a separately selected inquiry could change that use. Section :5.2 works this join, and :5.3 changes one
premise without discarding the independent result.

#### SYSE.10:4.2 - Record the Result

Use one claim-and-decision sentence for a small reversible choice. For several evidence bases or consequential
reliance, record:

| Field | Required content |
| --- | --- |
| decision and claim | Alternatives, deciding Agent, relying Work, consequence, claim, subject, configuration, environment, use, interval, scale, criterion, and material unsupported uses. |
| source basis | Source epistemes and editions, currentness, hypotheses, explanations, heuristics, prior observations, rival accounts, and transfer limits. |
| Method and Work | Evidence-producing Method, discrimination question, planned or dated Work, performer, tools and resources, inputs, controls, disturbances, subject configuration, and result production. |
| model or representation use | Modeled subject, purpose, assumptions, omissions, parameters, boundary conditions, computation or inference, verification, calibration, validation, uncertainty, sensitivity, extrapolation, and `C.29` correspondence when relevant. |
| observations and evidence | Observed occurrence or state, measurement Method and result, uncertainty and interval; the reason it bears on the target claim, consequential extension or joint premises and their grounds; polarity, grounding subject, scope, provenance, relevance window, supported and unsupported use. |
| criticism | Rival explanations, common assumptions, contradictions, negative results, configuration or implementation mismatch, selection effects, transfer limits, and omitted affected-System evidence. |
| assessment and decision effect | Supported, contradicted, narrowed, and unresolved claims; reliance limit; residual uncertainty; material unsupported claims; and the choice, constraint, redesign, postponement, or stop that changes. |
| further evidence and reopen | Stopping reason and later change that reopens the assessment. When further evidence is chosen, the compatible `C.11` or specialist experimental-design result; if that required result is unavailable, name it and the dependent use on hold. |

The assessment may cite supporting records—for example, model cards, trial reports, measurement records, or
evidence graphs—instead of copying them. Keep the assessment tied to the receiving decision.

#### SYSE.10:4.3 - What Changes in Practice

Engineers stop asking whether a model is *validated* or a test *passed* in the abstract. They ask which claim
about which configuration is supported for which use, what limits that reliance, and how the
decision changes. A usable assessment explains the step from each relied-on result to the claim and why the
necessary contributions hold together. It can therefore retain a valid result while withdrawing a conclusion
that depended on a failed transfer or shared premise.

Different inputs change different parts of the decision. For example, a theory can generate an alternative, a
heuristic can guide search, a simulation result can reject an infeasible region, a failed trial can expose an
interface assumption, and an operating observation can reopen a model-use claim. Each input keeps its governed
kind and epistemic status. Additional evidence is obtained only after an authorized Agent chooses the probe or
experiment design under the applicable Method.

### SYSE.10:5 - Worked Case: Evidence for a Heat-Pump Controller Increment

A heat-pump project is deciding whether to integrate a first controller increment that coordinates compressor
modulation with thermal storage. The claim is:

> For the named controller, sensor, and plant configurations, the controller keeps supply-water temperature
> within the declared comfort envelope and avoids harmful compressor cycling in selected low-ambient and
> tariff-response situations inside the qualified compressor-map region.

The project uses several unlike results:

| Method and Work | Result used | Supported and unsupported use |
| --- | --- | --- |
| analytic control reasoning | Stability and sampling claims for a linearized plant region. | Supports local stability under the stated approximation; does not cover nonlinear storage behavior, sensor faults, or installed performance. |
| Modelica simulation | Plant and controller traces over selected weather, load, and tariff situations. | Rejects several storage-dispatch candidates and supports one timing range; does not provide observed physical performance or cover unmodeled installation effects. |
| software-in-the-loop checks | Repeatable results for controller logic, state transitions, and selected properties. | Supports correspondence for the tested software edition; does not establish hardware timing, sensor behavior, actuator response, or building benefit. |
| controller-in-the-loop trial | Measurements from controller hardware, sensor emulation, inverter interface, and selected fault injections. | Supports timing, I/O, fallback, and selected cycling claims for the bench configuration; does not establish installed hydraulic, acoustic, or occupant effects. |
| installed-plant trial | Calibrated temperature, power, state, and fault observations during a bounded low-ambient interval. | Supplies observations and configuration grounds for the first increment's assessment; the receiving claim still needs the inference and joint conditions below. It does not establish seasonal reliability, another compressor variant, or every tariff policy. |
| independent criticism | Compressor-map and maintenance-access checks by relevant specialists. | Exposes an out-of-envelope map region and an inaccessible recovery action; neither result alone decides release. |

#### SYSE.10:5.1 - Finish with a Sufficient Direct Result

Suppose the immediate question is whether the completed one-hour trial met its declared 40–45 °C
supply-water criterion. Its qualified measurement result gives 41.0–44.0 °C with a conservative 0.2 °C
uncertainty bound covering that recorded interval and the named setup. The resulting 40.8–44.2 °C range lies
inside the criterion. The engineer can finish: “The temperature criterion was met in this recorded trial under
its qualified measurement conditions; use that result in the increment assessment.” This does not yet assess
another operating interval or the cycling criterion. Repeating the measurement or creating a full account adds
no required contribution to this direct question.

#### SYSE.10:5.2 - Construct the Missing Join for the Increment

Now consider the stronger receiving claim: the named increment can keep supply water within 40–45 °C and
space compressor restarts by at least ten minutes over the selected low-ambient and tariff-response use.
For this constructed example, professional qualification supplies the following results. The numerical limits
are stipulated case inputs, not reported heat-pump performance or general design limits.

Let E be the common qualified envelope: the named plant, compressor, controller binary and interfaces;
the selected low-ambient loads and tariff transitions; storage charge from 20% to 60%; and the specified
continuous operating interval without power reset or override of the restart limiter. The engineer receives:

- **M17, a qualified model-based prediction:** supply water remains within 40.6–43.6 °C throughout E provided
  the sensed-state age at physical actuation is at most 1.0 s. The prediction treatment already includes the
  relevant numerical, input, parameter, model-discrepancy and transfer uncertainties. Its evidence and
  applicability argument are available; a numerically verified solver alone would not supply this result.
- **S6, B12 and P5, qualified timing and installation results:** sensor acquisition and filtering contribute
  at most 0.5 s of state age; execution and command delivery add at most 0.2 s; command-to-physical-actuation
  adds at most 0.2 s. The reports use consecutive endpoints on the same event path, include the relevant
  waiting and integration effects, and bound those intervals for the same E. Installation checks connect the
  actual binary, sensor, interface and plant configuration to those named in M17. These are conservative
  bounds, not averages or percentiles from incompatible runs.
- **L4, a separately qualified limiter result:** consecutive actual compressor restarts remain at least ten
  minutes apart throughout E. Its clock, logic, interface and override conditions are established separately;
  its conclusion does not depend on M17's temperature prediction or the sensor update rate.

Combine the timing results before using M17. Because the three timing segments cover the complete event path under
the same conditions, their bounds give a state-age bound of 0.5 + 0.2 + 0.2 = **0.9 s**. This use of conservative
bounds needs complete path coverage and simultaneous applicability; it does not require statistical
independence. The result satisfies M17's 1.0 s premise. The installed configuration correspondence and E then
permit the prediction to support the temperature claim: its 40.6–43.6 °C range lies within 40–45 °C. L4 supplies
the different necessary cycling premise. Their common applicability lets the engineer support the conjunction
of these two criteria for the stated use. M17 and L4 are complementary grounds, not two votes for one claim.

The engineer returns that bounded technical recommendation to the deciding Agent. The argument deliberately
depends on the supplied professional qualifications; the addition above does not derive a measurement Method
or validate the model. The results leave seasonal reliability, higher storage charge, another compressor and
unexamined installation or maintenance consequences outside the supported claim. Specialist criticism of an
inaccessible recovery action still matters to its own integration or assurance question. Passing these two
criteria does not settle every condition of integration, commissioning or permission.

If an available specialist assessment already supplies this complete inference for the same configuration,
criteria and E, use that assessment and its limits directly. Section :4.1.1 is needed only for the missing
connection; it does not demand reconstructing an adequate argument in a second form.

#### SYSE.10:5.3 - Change the Premise and Keep the Independent Result

The selected sensor configuration now supplies one update every two seconds after filtering, whereas M17's
qualified configuration used two updates per second. The applicable sensor-age bound becomes 2.0 s. With
the unchanged downstream bounds, the available whole-path bound is **2.4 s**, which no longer establishes
M17's premise of at most 1.0 s. The model's old temperature prediction remains a result for its old conditions;
it no longer supports the current installed temperature claim. This loss of support does not show that the
actual water temperature violates 40–45 °C.

Retain the valid downstream timing results and L4's independently established restart limit. The conjunction
needed for the original favorable recommendation is unresolved because its temperature premise is missing;
the passing cycling result cannot compensate. Copied plots of M17 or additional summaries of its traces do
not repair that premise. The engineer returns this precise limitation and withholds the favorable assessment
for the changed increment. Choosing a supported narrower use, changing the estimator, obtaining a suitable
model result or repeating a controller-in-the-loop trial is a separate engineering or inquiry choice. Further Work proceeds only when its continuation has been selected as feasible and worthwhile under `C.11`
or the specialist Method. Its returned result can then reopen the affected assessment; a missing evidence
entry alone is not a reason to commission an experiment.

An AI Agent also proposes fault scenarios and a trace summary. One proposed scenario invents an interface
state absent from the configuration. Reject that proposal for this use. The summary can help locate traces,
but the assessment relies on their actual results and justified connections. A generated confidence score
neither supplies the missing state-age premise nor decides assurance, acceptance or release.

### SYSE.10:6 - Bias Annotation

Sources such as official verification procedures, software test automation, peer-reviewed papers,
sophisticated models, and AI benchmarks can contribute useful Methods or results. Their prestige, publication,
conformance label, mathematical form, or benchmark score does not establish a universal evidence order or the
project's effectiveness.

Across physical, cyber-physical, biological, and social-system cases, the relied-on evidence may depend on
configuration, calibration, integration, environment, use, or affected-System consequences that a software test
or simulation does not cover. Failed trials and actual project practice can matter more than published positive
cases.

Demanding definitive proof can be as harmful as overclaiming when no affordable study can settle the choice. Use
the best current assessment, state its epistemic status, make the decision reversible where possible, and name
the observations that would reopen it.

### SYSE.10:7 - Conformance Checklist

- [ ] The receiving decision, alternatives, deciding Agent, consequence, and claim are named.
- [ ] The claim has a subject, configuration, environment, use, interval, scale and criterion;
      material limits on supported reliance are explicit.
- [ ] Theory, model, simulation, experiment, trial, observation, evidence use, assurance, and decision remain
      different objects or relations.
- [ ] Source editions, Work, performer, Method, model assumptions, physical grounding, observations, measurement
      uncertainty, and transfer limits are recoverable to the degree the reliance needs.
- [ ] Each evidence use explains why the result bears on the target claim and retains polarity, scope, provenance,
      relevance window and unsupported use; causal reliance uses `C.28`.
- [ ] An extended or combined claim has its consequential premises, joining rule and applicability grounds;
      supported parts remain usable when the whole is unresolved. A sufficient direct result or specialist
      argument can finish the assessment without duplicate reconstruction.
- [ ] Rival explanations, common assumptions, contradictions, negative results, configuration mismatch, and
      affected-System evidence have been sought in proportion to the decision consequence.
- [ ] The assessment states what is supported, contradicted, narrowed, or unresolved and how the decision changes;
      it is not treated as authority or acceptance.
- [ ] A further local probe comes from `C.11`, an experiment set or sequence from a specialist Method, and the
      stopping and reopen conditions are explicit.

### SYSE.10:8 - Common Failures and Repairs

| Failure | Repair |
| --- | --- |
| “Research proves the architecture” | Connect the source claim to the project claim, transfer limits, evidence use, and decision effect; keep the architecture decision separate. |
| “The model is validated” | State the modeled subject, purpose, configuration, comparison basis, result, uncertainty, unsupported use, and currentness. |
| Treat simulation as physical evidence | Keep model behavior separate from observations of the actual configuration; seek physical evidence only for claims that need it. |
| Treat test pass as acceptance or release | Separate test Work, criterion result, evidence use, acceptance rule, assurance, permission, and release decision. |
| Count reports or climb one universal test ladder | Distinguish complementary premises from alternative arguments and copied sources. Explain the joint conditions and domain combination rule; use `C.11` or specialist experimental design only for selected further Work. |
| Hide a failed or negative trial | Record the result, validity limits, and alternatives it changes. |
| Accept a benchmark or AI confidence as general capability | State the task, population, configuration, Method, measure, result, checking Work, and transfer boundary. |
| Demand certainty before a reversible action | Use a stated reliance limit, accepted uncertainty, reversible choice, observation, and reopen condition. |

### SYSE.10:9 - Consequences

Research and model results guide decisions within their stated limits. Tests and trials address specific
claims; negative and partial results can change concepts, architecture, and realization Work early.

The cost is preserving configuration identity, assumptions, measurement provenance, uncertainty, evidence
polarity, and unsupported uses. Some decisions remain unresolved or receive a narrower operating envelope. Too
little evidence can shift harm to other Systems; too much low-value testing can delay the project. The Agents
performing Work guided by `SYSE.17`, `SYSE.4`, specialist Methods, or Methods for choosing further probes retain
their respective decision authority.

### SYSE.10:10 - Rationale

Engineering claim assessment connects heterogeneous knowledge and evidence results, actual configurations, and
decisions. It uses the FPF patterns for evidence, measurement, causal use, mathematical lenses, dynamics,
assurance, decisions, and currentness.

An authorized Agent chooses further probes using `C.11` or a specialist Method and records a choice or
experiment-design result. Assessment Work keeps descriptions, simulation results, and observations of actual
Systems separate, preserves configuration and extrapolation boundaries, and returns a claim-specific result to
the receiving engineering Work.

Inquiry Work can produce, for example, explanations, observations, models and Method candidates. Engineering
Work uses those results while choosing and realizing changes in Systems; later trials and operation can in
turn revise the inquiry's claims or Methods. Distinguish these contributions when they occur within the same
project, without imposing a temporal sequence.

### SYSE.10:11 - SoTA and Source Use

**Receiving question.** With the available qualified results in :5, what technical recommendation can the
engineer return for the two increment criteria, and what changes when the sensor premise changes? Compare a
specialist assessment centred on credible model prediction with the bounded combination of heterogeneous
results in :4.1.1. Keep the same configuration, criteria, evidence access and required professional preparation.

A serious model-based answer is supplied by Riedmaier, Danquah, Schick and Diermeyer,
[*Unified Framework and Survey for Model Verification, Validation and Uncertainty Quantification*](https://link.springer.com/article/10.1007/s11831-020-09473-7)
(published online 2020; journal volume 2021), §§2.5, 3.3 and 8.1–8.4. **Adapt** its use-specific prediction,
uncertainty treatment and selection among VV&UQ approaches. Validation conditions and application conditions
may differ; credible prediction must account for that difference. Its approach already has conditional
applicability and trade-offs. A generic validation label is not the alternative being compared.

| Same receiving conditions | Specialist model-based answer | Assessment through :4.1.1 |
| --- | --- | --- |
| An applicable specialist assessment already covers both required criteria and their joint conditions. | Use that complete result and its limits. | Use the same result; another argument or record adds no required contribution. |
| M17 supplies the temperature prediction while timing, installation and limiter results are separately qualified as in :5.2. | Retain the qualified prediction. A complete increment recommendation also needs the applicable timing/configuration connection and the cycling result; an existing specialist integration argument may already supply them. | Reuse those same contributions and construct only the missing join: the 0.9 s bound establishes M17's timing premise, the installation result establishes correspondence, and L4 supplies the other necessary criterion. |
| The sensor-age premise changes as in :5.3. | Reconsider prediction applicability; the old model result cannot settle the changed claim. | Withdraw the dependent temperature assessment and the favorable conjunction, retain the independent restart result, and return the missing premise to the deciding Agent. |

**Choice and accepted cost.** Use a sufficient specialist answer directly. Otherwise use this assessment to
explain the remaining connection between unlike qualified results and the receiving engineering claim. It
makes a partial technical result, a missing joint premise and their decision effect recoverable without first
requiring a new model of every contribution. A competent specialist may already provide exactly that argument;
in that case the answers coincide and a separate account has no demonstrated benefit.

When direct comparative evidence is unavailable and obtaining it would cost more than its value to the decision,
use qualified expert judgement with an explicit epistemic status, assumptions and limits.

The narrower construction retains real dependence on domain qualification. It does not calculate M17's error
model, establish the timing bounds or prove L4's behavior. When those results are missing, obtain the applicable
technical contribution or return the gap. Count its acquisition, specialist access, computation, integration
and later maintenance burden whichever assessment form is chosen. The worked comparison explains a
conditional construction; it supplies no measured project saving or general superiority of one Method.

Two further source contributions change the stop or the permitted inference:

- Schwarzburg et al., [*On the factors influencing confidence in models and simulations for decision-making:
  a survey*](https://www.cambridge.org/core/journals/design-science/article/on-the-factors-influencing-confidence-in-models-and-simulations-for-decisionmaking-a-survey/2ABC108661F76142864AC7C54443C06D)
  (2024), §§5.2–5.3: **retain the distinction** between reported confidence and qualified support. Its forty-response
  convenience sample and exploratory constructs concern confidence in use. They do not turn confidence into a
  physical temperature bound. This limits the confidence-score shortcut in :5.3; it is not a calibrated rule
  for combining the case's results.
- Huan, Jagalur and Marzouk, [*Optimal experimental design: Formulations and computations*, v2](https://arxiv.org/abs/2407.16212v2)
  (2024 article; 2026 corrected version), abstract: **adapt the scope distinction** among design criteria,
  computation and non-myopic sequential design policies. Use current `C.11:4.2`, step 5, for a worthwhile next
  local inquiry; return a coupled experiment programme to a specialist Method. This changes :4.1 step 9 and
  the continuation in :5.3. The abstract supplies this boundary, not the full numerical design procedure.

Reopen the selected assessment arrangement when the receiving claim exceeds an available result's qualified
domain, a necessary contribution or joining rule changes, or a sufficient specialist answer becomes available
with less total reconstruction. Reopen the technical VV&UQ choice when a changed application or uncertainty
question defeats its assumptions; the bounded assessment cannot repair that defect by changing labels. A new
publication matters when it changes one of these contributions or limits, not merely because it is newer.

### SYSE.10:12 - Relations

- `C.2.1`, `A.3.1`, `A.3.2`, `A.3.3`, and `C.29` distinguish source and result epistemes, Methods,
  MethodDescriptions, dynamics, and mathematical-lens use without making them physical results.
- `C.11` governs the choice of one next local probe among available options. A specialist experimental-design
  Method governs a set or sequence of experiments. An authorized Agent applies the relevant Method in decision
  or experimental-design Work. The Agent assessing available results applies `SYSE.10`. Keep the choice or
  experiment-plan result distinct from the later engineering claim assessment.
- `A.15.1`, `A.15.2`, `F.6`, and `A.15.PROD` distinguish planned Work, dated Work, performer attribution, and
  result production. A procedure, model or status label alone does not establish that Work occurred; use a report only within its supported claims about that occurrence.
- `C.16`, `C.16.P`, and `A.18` govern measurement, characteristics, scales, units, uncertainty, and admissible
  operations. `A.10`, `G.6`, and `G.11` govern evidence use, provenance, and currentness; `C.28` governs causal
  and counterfactual support.
- `SYSE.4:4.4` supplies the explanation of a consequential inference and `SYSE.4:4.6` the distinction among
  joint premises, alternative arguments and shared evidence. This assessment can use those instructions
  without making an assurance claim. `B.3`, `A.21`, `G.4`, and the applicable acceptance and permission
  patterns govern the separate assurance, gate and consequence-bearing results.
- Assessment Work can produce evidence for `SYSE.6`, `SYSE.4`, or `SYSE.19` only when the claim, configuration,
  horizon, and receiving decision match. Evidence neither authorizes nor entails those decisions.
- Results from engineering Work—for example realization, integration, operation, configuration change, specialist
  Work, or affected-System inquiry—become evidence only through their source and evidence-use relations. Adjacency
  between pattern names creates no such relation or temporal order.
- Applied engineering profiles may require different Methods for modeling, simulation, experiments, tests,
  trials or evidence use when a domain-specific fact—such as the engineered-System kind, physical mechanism,
  regulation, characteristic, scale or consequence—changes the working move.

### SYSE.10:End
