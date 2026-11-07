## PHY.10 - Construct a Physical Test That Separates Rival Accounts

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### PHY.10:1 - Problem frame

Use this pattern when competing physical accounts remain compatible with what has been observed, and the work needs a distinction between them. The missing contribution is a physical test: a preparation, intervention or understood comparison whose recorded consequences can separate the relevant alternatives.

A resistor and a capacitor can produce identical current traces under one imposed voltage history. Changing that history can expose the difference between dissipation and storage. A decaying collective signal can also hide different individual dynamics; a suitable intervention can make those dynamics distinguishable.

The first result is a proposed physical comparison, with the response each account permits, the conditions needed to produce and read it, and what the possible outcomes would change. It can reveal that the available apparatus cannot make the wanted distinction. A performed test adds observations and an interpretation under those conditions.

You need the physical meaning and applicable laws of the accounts being compared. Mathematical, computational and experimental collaborators can supply particular derivations and implementations. B.5.TC helps align the accounts when their questions or predicted quantities still differ. PHY.9 constructs a missing measuring interaction.

Use an existing discriminating observation or sufficient comparison directly. Leave the difference unresolved when it does not change the intended use, or when acting with the remaining uncertainty is preferable to another test.

### PHY.10:2 - Problem

Agreement with an observed response can have several physical explanations. A parameter can compensate for a missing interaction. A particular drive can make two response laws coincide. Different hidden dynamics can produce the same aggregate decay.

Collecting more data under the same uninformative conditions can leave the disagreement intact. Conversely, changing conditions to enlarge a predicted difference can introduce a new interaction, defeat the detector or leave the range in which either account was proposed.

A discrepancy also tests the combined account of the subject, preparation and observation. It need not identify the disputed physical premise by itself. The practitioner needs a comparison that exposes that premise while retaining the alternatives introduced by the apparatus and operating conditions.

### PHY.10:3 - Forces

| Force | Tension |
| --- | --- |
| Discrimination and estimation | Better knowledge of one account's parameters can leave its difference from another account unresolved. |
| Larger contrast and changed regime | A stronger intervention can expose the wanted effect while adding another physical mechanism. |
| Control and feasibility | A mathematically useful input need not be physically preparable with the available actuator, subject and resources. |
| Shared conditions and informative change | A comparison needs enough continuity to interpret a difference, while the test deliberately changes something. |
| Specific prediction and uncertain premises | Different nominal predictions can overlap after consequential parameter and apparatus uncertainty is included. |
| Useful criticism and effort | A simple consequence can settle the working question while a more elaborate experiment promises broader knowledge at greater cost. |

### PHY.10:4 - Solution

**Locate the consequential physical difference → find a condition that exposes it → construct the preparation and readout → compare the permitted responses → use the result and locate any defeated premise → develop the next useful test or stop.**

#### PHY.10:4.1 - State which physical disagreement matters

Ask the accounts the same physical question under corresponding conditions. Recover what each treats as the subject, its state, its interactions and the measured quantity. Use B.5.TC if the apparent conflict instead concerns different questions, representations or approximations.

State the consequence the work needs to distinguish. It may concern a law, an omitted interaction, stored state, a response time or another physical dependence. A distinction matters through what it changes in explanation, prediction, construction or subsequent inquiry.

Retain the parameter freedom that each account still has. An account with an adjustable coefficient is a family of possible responses, not just the curve at one fitted value. Include the available information that restricts that freedom. Do not choose a new parameter value independently at every observation unless the account itself permits that dependence.

Identify the auxiliary premises on which the comparison turns. For a driven specimen, these can include its preparation, the applied input, its coupling to surroundings and the relation between its response and the recorded indication. A test of the specimen's law can fail because one of these premises fails.

#### PHY.10:4.2 - Find a physical change that makes the accounts diverge

Trace the disputed difference forward to an observable consequence. Then ask which feasible change exposes it. For example:

- Change an amplitude, scale or operating regime when the accounts predict different dependence on it.
- Change the time course of a drive when the earlier input made different response laws coincide.
- Interrupt, reverse or refocus an interaction when the accounts retain different state or memory.
- Use a symmetry or balance when one account requires a response to vanish or remain within a bound.

Choose the change from the physical dependence at issue. PHY.4 supplies law constraints, PHY.5 examines a regime change and PHY.6-.8 derive the corresponding evolution or collective response.

Recompute both accounts under the proposed change. A prediction under the original preparation cannot be compared with a rival's prediction under the new one. Retain any changed interaction that can imitate or obscure the intended difference.

If intervention on the subject is unavailable, look for an accessible physical contrast: for example, a naturally varying condition with an understood relation to the accounts. Identify other differences between the observed situations. Their effects remain part of the comparison; naming the contrast does not make it controlled.

#### PHY.10:4.3 - Construct the experiment that can realize the contrast

Translate the mathematical change into physical preparation and operation. Identify the means of imposing the input, the initial or boundary conditions it requires, and the observable response. Include timing when a transient, memory or change of state is decisive.

Determine which shared conditions must survive. Maintaining geometry, material state or a reference can be more consequential than increasing the number of readings. When the intervention itself changes one of these conditions, either include that change in both predictions or construct another contrast.

Derive the subject-apparatus response far enough to establish that the difference reaches the recorded indication. PHY.9 constructs a missing coupling, reference or readout; C.16.MR represents the resulting measurement relation. A detector that clips both predictions to the same indication cannot implement their proposed separation.

Account for feasibility through the parts that can change this design. Available force, pulse duration, preparation time or observation range can rule out a proposed contrast or leave it conditional. An established apparatus or supplied capability can settle those questions without rebuilding its justification. If the required operation remains unavailable, return that specific limit or choose another contrast.

Use a reference or control for a named alternative explanation. A no-drive comparison can reveal an offset; a reference pulse can bound a control error. Add it when the result can change the interpretation.

#### PHY.10:4.4 - Compare the responses that can actually be distinguished

For each candidate design, obtain the readouts allowed by each physical account, including consequential parameter freedom and uncertainty in preparation, conversion and recording. MMP.7 supplies a probability law when records are random; C.16.IR helps determine what an indication can resolve.

Disjoint bounded response ranges give a particularly simple separation under their premises. If the ranges overlap, some outcomes can still discriminate the accounts while others remain compatible with both. Equal expected values likewise need not mean equal distributions or equal time dependence.

When discrimination depends on statistical evidence, use the appropriate model-comparison method with its dependence, sampling and error assumptions. Repeated readings do not automatically supply independent trials. A mathematical design criterion is useful only after the physical design and the interpretation of its records are supplied.

Compare designs on the distinction needed by the work and their full resource demand. A more informative record about one parameter need not be more informative about the rival mechanisms. Use a cheap sufficient contrast before constructing a costly optimization. C.11 compares available options; C.11.DUA addresses the value of another observation or computation.

Before performing the comparison, make its outcome interpretation clear enough to resist changing the question after seeing the result. State what would remain compatible with each account and which apparatus or preparation failure could mimic the disputed effect. The existing explanation or protocol can carry this reasoning.

#### PHY.10:4.5 - Obtain the result and locate the failed premise

Work the proposed preparation through to the predicted indication before committing the apparatus. This can expose an uninformative design or missing physical contribution without a new experiment.

When observations are obtained, interpret them under the stated recording and physical conditions. A response compatible with one supplied account and incompatible with another narrows this comparison. It does not exclude physical accounts that were never represented in the alternative set.

If the result disagrees with both, inspect the consequential premise rather than forcing a winner. Separate a computational error, an incorrect readout relation, an unachieved preparation and a defeated physical account. Follow the dependence of the failed prediction to identify a useful return. A supplied bound on an apparatus effect can sometimes exclude that explanation; when it cannot, retain the competing interpretations.

An agreement can also reveal a design limit. Determine whether the test retained the distinction it was meant to expose. If both accounts predict the observed outcome within the relevant uncertainty, report that limited result and preserve any unaffected consequence.

Reuse a result for the preparation, response range and question it supports. A successful test of a small-signal account does not determine its response after a regime-changing drive.

#### PHY.10:4.6 - Revise the account or develop the next contrast

Return the interpreted result and the physical reason for the next move. This may be use of a sufficient account, a narrower parameter range, an added interaction, a different preparation or readout, or an unresolved difference that the work can tolerate.

Develop a subsequent test from what remains unresolved. One outcome can identify which regime, hidden state or control error matters next. Sequential design can exploit that information, but a complete sequence need not be invented when one comparison already supplies the useful result.

When a revision changes the physical account, propagate it to the mathematical formulation, computation and interpretation that depend on it. Use B.5.RR and B.5.MPC.R for the corresponding reasoning and cross-contribution revision.

Stop when the obtained distinction suffices, or when no worthwhile available test changes the present use. Preserve a promising unresolved physical question when it opens a useful later construction or investigation.

### PHY.10:5 - Archetypal Grounding

#### PHY.10:5.1 - Change speed to separate two drag accounts

A specimen moves through the same fluid at an imposed positive speed v. In the proposed operating range, account L takes the opposing force magnitude to be `F=b v`; account Q takes it to be `F=c v²`. The coefficients are positive and constant under their respective accounts.

At v=1 m/s, an earlier calibrated force comparison places the true drag between 0.95 and 1.05 N. Thus L permits b between 0.95 and 1.05 N·s/m, while Q permits c between 0.95 and 1.05 N·s²/m². Both explain that observation.

A repeat at the same speed leaves this disagreement intact. Instead impose v=2 m/s while retaining specimen geometry and the fluid conditions on which the coefficients depend. L predicts a force between 1.9 and 2.1 N; Q predicts between 3.8 and 4.2 N. With an additional bounded force-readout error of ±0.1 N, the possible indications lie in [1.8,2.2] N and [3.7,4.3] N. They are disjoint.

The drive and readout must sustain that comparison. Under Q the required mechanical power can reach 8.4 W, since P=Fv. A 5 W drive cannot establish the proposed steady speed for every admitted Q response. A 10 W drive at that speed can meet this particular power demand, while its other operating limits remain relevant.

Suppose the comparison returns 2.05 N. It is compatible with L and incompatible with Q under the stated ranges and conditions. A return of 2.9 N instead disagrees with both. It prompts examination of the retained physical regime, parameter constraints and readout; it does not justify selecting whichever nominal curve is closer.

Heating or a geometry change can make a coefficient vary between runs. If that effect can span the separation, the test no longer has the same interpretation. Restore the shared condition, include the changed dependence or choose another contrast. Increasing speed without this return can defeat the very accounts being compared.

#### PHY.10:5.2 - Change a drive that makes storage and conduction coincide

A two-terminal element is driven with `V(t)=V_0 exp(t/tau)`. One proposed account is an ideal resistor, `I=G V`. Another is an ideal capacitor, `I=C dV/dt`, prepared with charge C V_0 at the start of the recorded ramp.

Since `dV/dt=V/tau`, choosing C=G tau makes the complete current traces identical during this ramp. More accurate recording of that same drive cannot distinguish the accounts.

Use V_0=1 V, tau=2 s, G=1 mS and C=2 mF. Stop increasing the voltage when it reaches 2 V and hold it there. After the drive and readout have settled, the resistor predicts 2 mA and the ideal capacitor predicts zero current. The change removed dV/dt while retaining V.

The waiting interval must be interpreted physically. A source with finite output resistance and a detector with finite response can create a transient after the change. Include it or choose a readout time after its consequential effect. The ideal predictions also exclude a significant leakage path.

Now suppose the held-voltage current is 0.6 mA, while the earlier ramp still has I/V=1 mS. The ideal pair is inadequate for these records. A parallel conductance and capacitance give

`I=G V+C dV/dt`.

The hold gives G=0.3 mS. Substitution into the ramp relation `G+C/tau=1 mS` gives C=1.4 mF. The test has opened a physically different account in which conduction and storage coexist. These two records determine its two parameters under the stated idealization; they do not establish that this account suffices at every frequency or voltage.

The resulting distinction changes use. A continuously held voltage dissipates power through the conductance, while the capacitance stores charge and supplies a transient response. Subsequent pulse or frequency use can therefore ask a question that the original exponential ramp could not resolve.

#### PHY.10:5.3 - Refocus a hidden physical difference

A prepared ensemble has a transverse phase signal. Consider two idealized accounts of its free decay. In account S, each member has a fixed frequency offset delta, drawn from the Lorentzian density

`p(delta)=Gamma/[pi (delta²+Gamma²)]`, with Gamma>0.

Each phase advances by delta t. Averaging over the ensemble gives `M_S(t)=exp(-Gamma t)` for t≥0. The individual offsets remain fixed even though the mean signal decays.

In account D, the phase instead has independent Gaussian increments with variance `2 Gamma dt` over an interval dt. This Markov dephasing gives the same free signal, `M_D(t)=exp(-Gamma t)`. The two accounts agree on this free-decay observation.

Apply a refocusing rotation at time tau and read the signal at 2 tau. In the ideal pulse comparison, the sign of phase accumulation is reversed for the second interval. Under S, each accumulated phase becomes `delta tau-delta tau=0`; the ensemble signal returns to 1. Under D, the two intervals have independent phase increments. Subtracting them leaves variance `4 Gamma tau`, so the signal remains `exp(-2 Gamma tau)`.

For Gamma=10 s⁻¹ and tau=0.1 s, the predicted refocused signals are 1 and approximately 0.135. The intervention exposes a difference hidden by the equal free decays.

A physical pulse has finite duration, range and accuracy. Its response over the occupied frequency range, other relaxation during the sequence and readout error must be included where they can change this separation. For illustration, if their combined effect on each predicted normalized signal is bounded by 0.05, the predicted indication intervals around 1 and 0.135 remain disjoint. This bound is a condition of that proposed implementation, not supplied by the ideal calculation.

If the pulse cannot refocus a consequential part of the ensemble, a small return can have that cause as well as irreversible dephasing. Change the pulse or reference comparison, retain its bounded effect, or leave the interpretation conditional. A partial echo can also motivate an account with both static variation and changing noise. The performed comparison then guides which hidden dynamics to retain.

### PHY.10:6 - Bias-Annotation

The cases use controlled laboratory comparisons and idealized response laws. Astronomical, geological and other field questions can require naturally available contrasts whose backgrounds cannot be independently fixed. The relevant physical premises must then support the observational comparison.

A finite candidate set can exclude a useful account before the test begins. A result inconsistent with every candidate, or a new physical dependence exposed by the experiment, can justify developing the set. It need not become a competition among the original labels.

### PHY.10:7 - Conformance Checklist

- The accounts answer the same physical question under corresponding conditions.
- Their remaining parameter freedom and consequential auxiliary premises are retained.
- The proposed physical change makes a difference in an observable response.
- Preparation, drive and readout can realize that change, or their unresolved limit is stated.
- Discrimination is judged with the relevant physical and recording uncertainty.
- Possible results retain their different implications, including agreement with several accounts or disagreement with all supplied accounts.
- The first result and subsequent physical, mathematical or computational return are usable.

### PHY.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Better data from an uninformative drive | The resistor and capacitor retain identical ramp traces. | Change the physical input that made the laws coincide. |
| Nominal curves treated as complete accounts | Adjustable coefficients make the predicted response families overlap. | Compare the responses allowed by the admitted parameter information. |
| Increase the drive until the curves separate | A new physical regime defeats the retained laws or apparatus. | Derive the changed interactions and check attainable preparation. |
| Distinct states, identical indications | The detector erases the predicted difference. | Change the measuring interaction or readout. |
| Nearest curve must win | A response outside both admitted ranges is forced into the original pair. | Locate the failed premise and develop another account when needed. |
| A failed echo proves irreversible loss | Control error or an unaddressed frequency range can suppress the return. | Include or distinguish the consequential pulse and readout effects. |

### PHY.10:9 - Consequences

Physical comparison becomes a construction that can change what is observable. Its result can be a discriminating experiment, a useful limit on current apparatus, an improved account or a justified stop.

The calculation, apparatus and interpretation can be developed by different contributors while retaining the common physical disagreement. The cost is concentrated on the dependencies that determine the comparison. A result may remain local even when it resolves the present work.

### PHY.10:10 - Architectural Rationale

B.5.TC compares how theoretical accounts answer a working question. This method develops a physical consequence of that comparison: how a preparation or interaction can expose the disputed dependence. PHY.9 supplies an observable readout; the statistical or mathematical design uses that physically realizable relation.

Equal unperturbed responses can conceal different retained state. Changing a drive or reversing an interaction therefore supplies more than another sample of the old observation. It asks the accounts how the physical system responds to a different operation. That response can also reveal how the system might be controlled or used.

The test retains the apparatus and preparation because they participate in the consequence being compared. This makes an unsuccessful comparison informative: a return can change the subject account, the experimental construction or their mathematical description, according to which premise failed.

### PHY.10:11 - SoTA-Echoing

[Huan, Jagalur and Marzouk, *Optimal experimental design: Formulations and computations*](https://arxiv.org/abs/2407.16212), Acta Numerica (2024), with corrections and clarifications in the 2026 author revision, distinguishes design for parameter information, prediction and model discrimination. Its sections 2.2 and 6.1 retain uncertain influences and the possibility of model misspecification. These distinctions enter :4.1 and :4.4-.5. A design based on a supplied model set does not establish that the set contains an adequate account.

For the drag comparison, the disjoint force ranges give a sufficient design without a numerical optimizer. When feasible inputs are numerous and predicted records are uncertain, an experimental-design method can compare their expected contribution. Its advantage depends on a useful objective and credible response models. The cost of constructing and evaluating that optimization matters alongside the cost of the experiment.

[Vezvaee et al., *Fourier transform noise spectroscopy*](https://www.nature.com/articles/s41534-024-00841-w), npj Quantum Information (2024), develops noise reconstruction from free-induction and spin-echo measurements. The adopted physical contribution is changing how a prepared probe couples to temporal structure. The paper's spectral reconstruction relies on its pure-dephasing and stationary Gaussian-noise setting; those assumptions are not imposed on the Lorentzian static-offset construction in :5.3.

For a noise question within that setting, the paper compares reconstruction from simple sequences with methods requiring many pulses. It also exposes different limitations: finite pulse timing, a restricted accessible frequency range and sensitivity of time derivatives to measurement error. Choosing more elaborate control is therefore not a general improvement. The simpler sequence can be sufficient for the needed distinction, while a different noise or control question calls for another method.

The three numerical cases are constructed comparisons under stated physical laws. Their purpose is to exhibit the changed preparation, response and interpretation. New physical effects or apparatus limits change the corresponding case premises.

### PHY.10:12 - Relations

- **B.5.TC and B.5.TU:** align the theoretical comparison and construct a missing application of an account.
- **PHY.4-.8:** constrain a law and derive the physical response to a changed preparation or interaction.
- **PHY.9 and C.16.MR:** construct the measuring interaction and its relation to the recorded indication.
- **C.16.IR and MMP.7:** determine what the indication resolves and supply the applicable recording probability law.
- **PHY.1-.3:** receive a discriminating comparison when similarity, a physical analogue or a limiting transformation needs examination.
- **C.11 and C.11.DUA:** compare available designs and the value of further inquiry.
- **B.5.RR and B.5.MPC.R:** revise the affected reasoning and its physical, mathematical and computational contributions.

### PHY.10:End
