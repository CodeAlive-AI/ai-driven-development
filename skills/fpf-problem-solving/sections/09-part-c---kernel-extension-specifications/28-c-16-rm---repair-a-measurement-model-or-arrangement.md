## C.16.RM - Repair a Measurement Model or Arrangement

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative

### C.16.RM:1 - Problem frame

Use this pattern when a measurement disagrees with an expected result or cannot distinguish the cases needed for the work. A detector combines a beam with background light. A voltmeter changes the voltage it measures. A program turns correctly recorded counts and times into an incorrect rate. Each situation offers a different place to repair.

**First useful move.** Put the wanted quantity beside the indication and recover the relation used to connect them. Mark the contribution that prevents the wanted answer. If a detector responds to beam plus background, repeating that reading leaves their separate contributions unknown; a reading with the beam removed can make their difference usable.

The Method selects and carries through a change to a measurement model, its computation or the actual arrangement. The useful result is a corrected interpretation, an adequate changed measurement, a conditional design result or a remaining limitation with its effect on the work. C.16 supplies the measurement, model, performed work and obtained-result meanings.

The examples assume elementary algebra, bounds and units. The subject law, calibration and operating conditions come from the relevant physical or other domain practice. Apply a suitable established correction or repair procedure directly when the fault and applicable remedy are already known. Use the present Method when the choice of what to change remains consequential.

### C.16.RM:2 - Problem

A disagreement can arise from the measured subject, its description, the instrument, the instrument model or the calculation. Improving the wrong contribution consumes effort while leaving the wanted answer unavailable. Repeated observations can reduce some random effects and preserve a loading error, background contribution or computational mistake.

A change can also alter the quantity being measured. Cooling a specimen to stabilize an instrument may change the specimen property whose value was wanted at the original temperature. Better agreement in the changed situation therefore needs a relation back to the intended use.

The problem is to locate a useful repair, carry it through the affected relations and establish what the revised result supports. Explaining the historical cause of a fault and obtaining an adequate measurement can require different amounts of work.

### C.16.RM:3 - Forces

| Force | Tension |
| --- | --- |
| Better model and simpler conditions | Describing an influence can be costly; controlling it can change the subject or require new equipment. |
| Fault diagnosis and sufficient repair | Several causes may remain possible while an available change already restores the needed result. |
| Repeated data and structural ambiguity | More readings help only through the distinctions or error reduction their relation supports. |
| Changed arrangement and original target | A more convenient experiment may answer a different question. |
| Numerical correctness and measurement adequacy | Correct calculation can implement an inadequate model; a suitable model can be computed incorrectly. |
| Full restoration and useful completion | A conditional result or adequate bound may settle the work before every uncertainty is removed. |

### C.16.RM:4 - Solution

Follow the disagreement from the wanted result through the indication-producing relations. Compare changes at the contribution that matters, choose a sufficient available repair, and use the revised relation to obtain the result needed by the work.

**Align the question and observations → locate the consequential contribution → compare a model, computation or arrangement change → carry through the selected repair → determine what the revised result supports.**

The starting point can be a known fault, an unexplained discrepancy or a proved inability to distinguish the needed cases.

#### C.16.RM:4.1 - Align the comparison and target

State the quantity or distinction sought, its subject and operating conditions. Put the expected result and obtained indication on a comparable basis: same quantity, time interval, units and relevant preparation. If the expectation concerns an unconnected source but the reading concerns a loaded source, retain that difference in the relation.

Recover how the indication was produced and interpreted. Separate an observed disagreement from an assumed explanation. A temperature-dependent response may come from the subject, sensor or their interaction; the correlation alone leaves those contributions to be distinguished.

Use C.16.MR when the measurement relation itself is missing. Use C.16.IR to find which alternatives fit an available relation and which distinction remains unresolved. A sufficient bound may already answer the question and end the repair attempt.

#### C.16.RM:4.2 - Locate the contribution that could change the answer

Follow the target-to-indication relation far enough to identify the consequential influence or incompatible operation. Ask what each candidate explanation would require changing and what present information bears on it.

| Possible repair location | What to inspect | A useful change |
| --- | --- | --- |
| Subject model | Which interaction, boundary or varying condition is omitted from the predicted quantity? | Include a background contribution or the dependence on the actual preparation. |
| Instrument model | How does the instrument respond in the range and conditions used? | Include loading, offset, saturation or a calibrated nonlinear response. |
| Computation | Does the implemented operation evaluate the intended relation with its units, domains and required accuracy? | Correct a unit conversion, retained branch, numerical approximation or aggregation interval. |
| Subject arrangement | Can a relevant condition be controlled while retaining the target or a usable relation to it? | Shield an unwanted input or hold a consequential condition stable. |
| Measuring arrangement | Can a different interaction or indication distinguish the needed alternatives? | Change the input resistance, operating range, observation timing or reference measurement. |

The table locates choices; the domain Method supplies the physical law or diagnosis that makes one choice appropriate. A common influence can cross several rows. For example, a change in illumination can alter both the subject response and the detector response.

For a suspected computational fault, run a supplied or constructed input whose answer follows from the intended relation. Compare intermediate values, units and branch choices until the divergence is located. A successful calculation on that input checks implementation of the relation. Compare the relation with the actual subject separately when its adequacy is in question.

#### C.16.RM:4.3 - Compare changes by their predicted contribution

For each serious available repair, change the corresponding part of the relation and determine what would become knowable. An added parameter can represent a missing effect while introducing an unknown that one reading cannot determine. A physical change can remove the effect or make its influence small enough to bound.

A difference measurement is useful when the target changes between two observations in a known way while the influences being cancelled remain sufficiently stable. A larger input resistance is useful when the loading relation shows how much it reduces the consequential error. Repeating an unchanged observation needs its own error or dynamics account to support a narrower conclusion.

Prefer an already available comparison or a small reversible change when it can settle the repair choice. If several explanations predict the same result of a proposed test, that test cannot select among them. Use C.11.DUA to compare the gain from an attainable further observation with its effort and delay.

The needed conclusion sets the reach of diagnosis. Replacing a defective assembly and obtaining the required response may restore the measurement without identifying which internal component failed. Retain the unresolved cause if later reliability, maintenance or causal explanation depends on it. Use C.28 when the required result is a causal attribution.

#### C.16.RM:4.4 - Carry the selected repair through the measurement

Keep the target and receiving question fixed while revising the selected contribution. If an alternative target or operating condition is acceptable, make that change part of the receiving decision and derive the relation for the new use.

For a model repair, include the consequential influence and obtain its value, range or relation from available information. An added correction term earns its use through that basis. Carry any remaining uncertainty into the sought result.

For a computation repair, correct the operation and recalculate the affected results from retained inputs. Reuse observations whose meaning and conditions still fit. Identify outputs that depended on the incorrect operation so that subsequent comparisons use the repaired result.

For an arrangement change, derive how preparation, interaction, indication and calibration are affected. An attenuator can move a detector out of saturation while introducing an attenuation factor and its uncertainty. A shield can remove ambient light while changing alignment. Retain the conditions that make the new relation appropriate.

A planned change supports a conditional result. Once performed, use the resulting observations and conditions to interpret that measurement. Older observations can still answer their original question or be reinterpreted through a supported revised relation; changing a model now does not supply a new past observation.

#### C.16.RM:4.5 - Test the repaired contribution at the needed scope

Choose a comparison capable of exposing the defect the repair addresses. For computation, compare with an independently obtained result for the same mathematical input. For an omitted influence, use a relevant reference condition, intervention or already available contrast. For a claimed operating range, include the range boundary or change of behavior on which the claim depends.

Read the result through the repaired measurement relation. Propagate the uncertainty that could change the receiving answer, and use C.16.IR when compatible alternatives or an outer bound require interpretation. A closer numerical match can still leave a consequential ambiguity.

When the comparison leaves the needed answer unresolved, return to the remaining contribution. A further repair may be justified, or the useful result may be a narrower claim, a changed use or a stop. Do not expand a successful local comparison into a wider range claim without the corresponding basis.

#### C.16.RM:4.6 - Return the usable result

Give the corrected value or comparison, the conditions under which it applies and the consequence for the receiving work. Keep the reason for a changed interpretation where another user could otherwise continue using the old one.

Stop when the result is adequate for that use. Further investigation may have value for another question, such as broader operating conditions or the origin of the fault; it is a separate continuation whose gain should be clear.

### C.16.RM:5 - Archetypal Grounding

#### C.16.RM:5.1 - Separate a beam from background and detector offset

The wanted quantity is the optical power I from a beam at a detector. A supplied linear response model is:

`r = g*(I + A) + b.`

Here A is ambient optical power, g = 2 mV/mW is a known response coefficient and b is an electronic offset. The detector is unsaturated. During the following three observations, g, A and b remain unchanged:

| Condition | Reading |
| --- | --- |
| Beam on, receiver exposed | 12 mV |
| Beam off, receiver exposed to the same ambient light | 6 mV |
| Opaque cap over the receiver, excluding beam and ambient light | 2 mV |

The capped reading gives b = 2 mV. Subtracting only this offset from the beam-on reading and dividing by g gives 5 mW. That is I + A; it leaves the wanted beam contribution mixed with ambient light.

Use the exposed beam-off reading to cancel both unchanged contributions:

`I = (r_on - r_off)/g = (12 - 6) mV / (2 mV/mW) = 3 mW.`

The same observations give A = (6 - 2)/2 = 2 mW. Substitution reconstructs all three readings. The repaired interpretation supplies I using observations already available.

A possible arrangement repair is to shield the receiver from ambient light while preserving the beam at the detector. Under A = 0 and the same g and b, a new beam-on reading of 8 mV would also give I = 3 mW. That value is conditional until the new measurement is performed.

Suppose instead that the shield removes ambient light but transmits a known fraction alpha = 0.9 of the original beam. With the same g and b, a new reading of 7.4 mV gives (7.4 - 2)/2 = 2.7 mW for the transmitted beam. Recover the original beam through the changed relation:

`I = (r - b)/(g*alpha) = (7.4 - 2)/(2*0.9) = 3 mW.`

If the transmission fraction is unknown, this new reading alone leaves the original beam unresolved. The earlier valid on/off observations still support their result of 3 mW. The shield's changed interaction must be included in any conclusion drawn from the new measurement.

For a question I ≤ 3.2 mW, suppose each on/off reading has an arbitrary additive error between -0.1 and 0.1 mV, while g and the shared background remain fixed. The difference gives 2.9 ≤ I ≤ 3.1 mW, so the bound settles the question. Drift in A between on and off would add a further term. Alternating readings reduces that uncertainty only with a supplied account of the drift; the alternation itself is insufficient.

#### C.16.RM:5.2 - Reduce loading enough to settle the question

A source has open-circuit voltage E and internal resistance Rs between 0.8 and 1.2 MΩ. A meter with input resistance Rm reads:

`V = E*Rm/(Rs + Rm), hence E = V*(1 + Rs/Rm).`

With Rm = 1 MΩ and an ideal reading V = 5 V, the compatible bound is 9 ≤ E ≤ 11 V. It leaves the question E ≤ 10.5 V unresolved.

One option is to determine Rs more closely and correct the loaded reading. Another is to reduce loading. The second option is available here: change to a meter with Rm = 100 MΩ. Assume the same passive-source model and resistance range apply to the new measurement. If its ideal reading is 9.9 V, then:

`9.9*(1 + 0.8/100) ≤ E ≤ 9.9*(1 + 1.2/100),`

so 9.9792 ≤ E ≤ 10.0188 V. The bound settles E ≤ 10.5 V while Rs remains unresolved. The repair earned its place by reducing the unknown resistance's influence on this conclusion.

Restore a supplied reading-error bound of ±0.1 V for the new meter. The positive factors give:

`9.8*1.008 ≤ E ≤ 10.0*1.012,`

or 9.8784 ≤ E ≤ 10.12 V. The same decision remains settled. A more demanding threshold could make the error bound consequential again. Meter range, voltage stability and the loading model belong to the physical premises supporting this use.

#### C.16.RM:5.3 - Recompute a rate from retained observations

A flow logger records cumulative pulses and elapsed timestamps in milliseconds. The supplied calibration is one pulse per litre, with no missed pulses or resets in the interval. The receiving question concerns average volume flow over that interval.

Both endpoint timestamps are taken at pulse events. The retained endpoints are 120 pulses at 10,000 ms and 180 pulses at 40,000 ms. A program subtracts the timestamps, divides the count difference by 30,000 and labels its output 0.002 L/s.

The pulse difference represents 60 L. The timestamp difference represents 30 s. Evaluating the intended relation gives:

`average flow = 60 L / 30 s = 2 L/s.`

The program's division obtained 0.002 L/ms and then attached the wrong time unit. Convert milliseconds to seconds before division, or convert the resulting rate afterward. Both repairs give 2 L/s. Recompute other affected intervals from their retained counts and timestamps.

A reference input of 10 pulses over 2,000 ms should give 5 L/s. A program result of 0.005 L/s reproduces the conversion fault; 5 L/s confirms this operation for that input. This calculation checks the implementation. Whether the actual instrument counted every litre and its clock tracked elapsed time requires the relevant calibration and observation when those premises are disputed.

The useful result is a repaired average rate from existing observations. Repeating the physical flow measurement is unnecessary for the identified unit-conversion fault while those observations and their calibration remain usable.

### C.16.RM:6 - Bias-Annotation

Under the five Principle-Taxonomy lenses of E.3 (Gov, Arch, Epist, Prag and Did), this pattern is scoped to repairing model-based measurements for a receiving use. The examples separate influences with simple relations and supplied conditions. Coupled effects, nonlinear response, drift, hysteresis or uncertain model structure can require richer diagnosis and uncertainty Methods. The pattern identifies where those contributions become necessary; it does not supply their complete domain repertoires.

The method favors a repair sufficient for the receiving use. A fault investigation concerned with reliability, causal explanation or a wider operating range can require work beyond restoring one useful reading. Keep that broader question explicit when it governs the effort.

### C.16.RM:7 - Conformance Checklist

- **CC-C16.RM-1 - Comparable question.** The wanted quantity, actual indication, expectation and relevant conditions support the comparison being made.
- **CC-C16.RM-2 - Repair location.** The proposed change acts on a contribution capable of altering the unresolved answer.
- **CC-C16.RM-3 - Choice basis.** Available comparisons, domain relations or proportionate further inquiry support the selected repair.
- **CC-C16.RM-4 - Target continuity.** The revised arrangement retains the intended target or a stated relation to the accepted changed use.
- **CC-C16.RM-5 - Dependent results.** Changed models, computations, calibration and observations are carried through the affected interpretation.
- **CC-C16.RM-6 - Adequate test.** The comparison can expose the addressed defect and supports the range or result actually claimed.
- **CC-C16.RM-7 - Useful completion.** The returned result and remaining uncertainty answer the receiving question or state the consequential limitation.

### C.16.RM:8 - Common Anti-Patterns and How to Avoid Them

| Failure in these situations | Consequence | Repair |
| --- | --- | --- |
| Repeat a mixed signal and average it | The stable background remains in the result. | Cancel, estimate or control the consequential contribution through a justified relation. |
| Add an unknown correction without a way to bound or determine it | The formula changes while the target stays unresolved. | Obtain the missing relation or choose an arrangement that limits the influence. |
| Improve agreement by changing the wanted subject condition | The new reading answers a different question. | Preserve the target or derive the relation connecting the changed condition to it. |
| Treat an implementation test as confirmation of the physical model | Correct arithmetic is used to support an untested subject premise. | Match the comparison to the contribution whose adequacy is in question. |
| Continue fault diagnosis after a sufficient repair | The present result is delayed for an unrelated explanation. | Return the adequate result and pursue the remaining cause only for a question that needs it. |
| Apply a new correction to an old result without checking its conditions | The revised value can misrepresent the earlier measurement. | Reuse the retained observations through a relation supported for that situation. |

### C.16.RM:9 - Consequences

The practitioner can change the contribution responsible for an inadequate measurement and recover a usable result. Available observations may suffice; an equipment change can simplify the inference; a computational repair can restore results without a new physical experiment.

A targeted repair also limits what is established. A successful local result may leave the fault's cause, a wider operating regime or the uncertainty of a different quantity open. Those limits direct further work when its receiving question becomes current.

### C.16.RM:10 - Architectural Rationale

Measurement joins a subject, an interaction, a mathematical relation and a calculation used to interpret an indication. The same unwanted effect can be addressed by representing it, reducing it in the arrangement or changing how the indication distinguishes the target. Keeping these alternatives together helps avoid repairing the most familiar component merely because it is familiar.

C.16.MR constructs a relation and C.16.IR determines what it resolves. This Method begins when that existing use is inadequate and chooses what to change. B.5.MPC.R supplies the wider repair across physical, mathematical and computational contributions. Here the distinction between subject and instrument, cancellation conditions, loading reduction and reinterpretation of retained observations makes that repair actionable for measurement.

The result can be epistemic, such as a corrected interpretation, or include an actual physical alteration. Its status follows the work performed and the premises available. That distinction permits a useful design calculation before equipment is changed and a useful recomputation after an implementation fault is found.

### C.16.RM:11 - SoTA-Echoing

**Practice question and selected answer.** How should one change a measurement whose current model, calculation or arrangement fails the receiving question? Select a contribution-specific repair, compare what it would resolve, and stop at an adequate result. The serious alternatives are a known applicable correction, a more detailed model, or more observations under the unchanged procedure. A known sufficient correction remains the cheaper route. The selected comparison is useful when repetition preserves the defect or extra model detail adds an undetermined influence. In :5.1 the already available on/off contrast resolves the beam contribution; in :5.2 changing loading yields a sufficient bound without identifying every parameter. Changing equipment can cost more than calculation, so its value depends on availability and the wanted conclusion.

**Model and apparatus alternatives.** [Dounas-Frazer and Lewandowski (2018), §2 and §§4.1–4.3](https://arxiv.org/pdf/1805.10334) explains iterative comparison and revision of physical-system and measurement-system models and apparatus. Its optics cases distinguish controlling unwanted light, avoiding saturation and revising response models. **Adapt** these alternatives into :4.2–4.4's choice of repair location and conditions. The paper's educational investigations support these modeling moves in experimental physics; they do not establish universal transfer or the effectiveness of the present cross-case Method.

**Adequacy and computational comparison.** [JCGM GUM-6:2020, §12](https://www.bipm.org/documents/20126/2071204/JCGM_GUM_6_2020.pdf) distinguishes comparisons with reference situations, computational tests using generated data, fit over the intended range and the adequacy of a simpler model. **Adapt** those distinctions in :4.2 and :4.5: select a comparison for the contribution and claim being repaired. Section :4.3 applies C.11.DUA to its attainable value and cost. The numerical cases are constructed demonstrations; the source does not supply their instrument laws or performed observations.

The integrated repair sequence, target continuity and return through a useful conclusion are conceptual synthesis. Reopen the choice when a cheaper remedy settles the same question, a changed condition invalidates the correction, or a comparison reveals a consequential influence left outside the model.

### C.16.RM:12 - Relations

- **C.16** supplies measurement, model, work, result and uncertainty meanings.
- **C.16.MR** constructs or revises the measurement relation needed to interpret an indication.
- **C.16.IR** obtains compatible values and determines what the relation and readings resolve.
- **B.5.MPC.R** coordinates repair across the wider physical, mathematical and computational connection.
- **B.5.RR** carries a changed premise through affected reasoning.
- **C.29.2** constructs or repairs a needed computational formulation and its accuracy conditions.
- **C.28** supplies a causal account when identifying the cause is the required result.
- **C.11.DUA** compares further inquiry and its attainable contribution to the receiving use.

### C.16.RM:End
