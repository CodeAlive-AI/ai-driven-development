## C.16.MR - Construct a Measurement Relation

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative

### C.16.MR:1 - Problem frame

Use this pattern when you have an indication or a proposed measurement procedure, but the relation between that indication and the property you want to determine is missing or unsuitable. A connected voltmeter can change the voltage. A test response can depend on both capability and the assistance offered. A counter can report the remainder after a wrap rather than the total number of events.

**First useful move.** Follow one indication back through the procedure that produces it. Name the sought property, the conditions under which it is sought, and one interaction or transformation that can make the indication differ from it. Express the relation supplied by that interaction. For an ideal source with open-circuit voltage E and series resistance Rs, a voltmeter of resistance Rm reads V=E*Rm/(Rs+Rm). This already shows why the indication alone need not determine E.

The Method constructs a measurement relation: how sought values, the measuring arrangement and relevant influences produce an indication, or how those contributions jointly constrain the sought value. The relation may use laws, an applicable calibration, an empirical response model or their combination. It can be used to plan a measurement or interpret an obtained indication.

The worked constructions concern quantities and event counts; they require elementary algebra and, in the assessment case, conditional probabilities. Subject Methods supply the physical laws, instrument response, assessment meaning or computational operations. C.16 supplies the Characteristic, Scale and performed-measurement account. This construction can return a conditional relation before any measurement is performed.

When a usable relation already supplies the needed answer under the current procedure and conditions, use it. If the relation is available but several sought values fit the indication, the next work is to determine what that indication can resolve. If an existing measurement disagrees with a prediction, compare possible changes to the models and arrangements.

### C.16.MR:2 - Problem

An instrument display, test outcome or log value is produced by a procedure. Its meaning depends on that procedure and on the conditions in which the property is sought. Substituting the display for the sought value can therefore answer a different question.

A correction copied from another arrangement can also fail. Its sign, magnitude and uncertainty depend on the relation that produced it. Unknown influences can leave multiple compatible values even when the displayed number is stable.

The working difficulty is to construct enough of that relation to interpret the indication for the intended use, without modeling every possible influence or assuming that a familiar formula applies unchanged.

### C.16.MR:3 - Forces

| Force | Tension |
| --- | --- |
| Sought property and observed response | A procedure can transform or disturb what it observes. |
| Available relation and changed conditions | A calibration can save construction work while depending on its arrangement and range. |
| More detail and useful interpretation | Adding an influence costs information and computation; omitting a consequential one changes the answer. |
| Physical and statistical accounts | A deterministic response and a distribution of responses support different inversions. |
| Direct calculation and joint constraints | Some relations give the sought value directly; others require solving several relations together. |
| Planning and obtained measurement | A conditional model can guide an experiment before the data and conditions of an actual measurement exist. |

### C.16.MR:4 - Solution

Fix the property and conditions of interest. Follow the production of the indication, combine the relations that connect it to the sought value, and retain the influences that can change its interpretation. Obtain a first conditional result or expose the missing relation.

#### C.16.MR:4.1 - Fix what the measurement is meant to determine

Specify the subject, Characteristic, Scale and conditions needed to distinguish the sought value. Include timing, location, population or averaging interval where they change the question. Use C.16:5.1-:5.2 for that specification.

Distinguish values that can differ across stages of the procedure. The open-circuit voltage before connecting a meter and the terminal voltage during measurement are different sought quantities. Either can be a legitimate target; choosing one determines the required relation.

Name the receiving question. Estimating a value, deciding whether it exceeds a limit and detecting a change can tolerate different remaining uncertainty. This choice helps decide which influences are consequential.

#### C.16.MR:4.2 - Follow the production of the indication

Trace the procedure from the subject through the interactions, transformations and sampling that produce the indication. For each consequential stage, identify the relation supplied by the physical principle, known operation, applicable calibration or response model.

Start with relations already available for the actual or proposed arrangement. A supplied conversion can be enough. When it is missing, derive it from the subject account or identify the empirical relation that must be learned. B.5.RC helps recover a construction from an unfamiliar description; B.5.FM helps formulate the first model.

Retain an intermediate value when another relation uses it or when it exposes a consequential interaction. In the voltmeter example, current connects the source equation to the meter indication. Eliminate that current only after the relations use the same current and conditions.

For a statistical procedure, describe how response probabilities depend on the sought property and relevant conditions. The expected response and one realized sample are separate inputs to inference. Learning or transporting the response model requires the subject's estimation and applicability work.

#### C.16.MR:4.3 - Include the influences needed by the question

Ask which features of the arrangement can change the interpretation at the intended range or decision boundary. Relevant candidates include loading the subject, offsets, limited resolution, sampling, timing, saturation and dependence on environmental or operating conditions. Follow the procedure to choose among them.

Describe a consequential effect where it enters the relation. An offset at an instrument's input can propagate differently from an offset added to its displayed output. A known correction follows from that relation; an uncertain effect retains its uncertainty. Several effects can be modeled together when their combined contribution is sufficient for the use.

Retain an unknown influential value as unknown. Available bounds or a justified probability model can support a useful conditional answer. Do not assign zero solely because the influence has not been measured.

Compare omission with inclusion at the needed result. A simple limiting case or a bound can show that an influence is negligible for this question. Keep the condition under which that conclusion holds, so a tighter requirement can reopen it.

#### C.16.MR:4.4 - Compose the relation and obtain a first result

Combine relations only after their shared quantities, units, stages and conditions agree. Use substitution, a joint equation system, a conditional response calculation or another operation appropriate to the supplied model. C.29.2 helps construct the computation when obtaining the consequence is itself difficult.

A direct formula for the sought value is convenient but not required. Keep an implicit relation when solving it needs additional information or when several sought values remain compatible. A computational procedure can express the relation when its steps and interpretation are available.

Work one small case. Supply the known values, retain unknowns, derive a sought value or compatible set, and substitute back where that tests the construction. Inspect an informative limit: a meter with negligible loading, identical assessment response rates, or an interval too long for a wrapping counter.

Carry uncertainty that can change the conclusion. C.16:5.4 gives its interpretation requirements; the mathematical propagation Method depends on the relation. Algebraic solvability alone does not determine whether a near-threshold decision is resolved.

#### C.16.MR:4.5 - Return the relation and its next useful use

Return the relation with the meanings of its inputs and sought value, the conditions that make it applicable, and the first result it supports. Preserve this information in the calculation, model or explanation being used; a new record is needed only when the receiving work requires one.

If the relation leaves a consequential ambiguity, name the indistinguishable values or the missing contribution. The next measurement should be selected for how it can resolve that distinction. C.11.DUA helps compare the value and cost of obtaining it.

When a discrepancy calls for repair, keep open the distinct possibilities of changing the subject model, the measurement model, the subject arrangement or the measuring arrangement. Additional mathematical detail is one option. Removing an unwanted interaction or restoring the specified procedure can be simpler.

Reopen the affected part when the target conditions, measuring procedure, calibration range or consequential influence changes. Use B.5.MPC.R when that change also affects connected physical, mathematical and computational work.

### C.16.MR:5 - Archetypal Grounding

#### C.16.MR:5.1 - Recover an open-circuit voltage from a loaded indication

The sought value is a source's open-circuit voltage E. The supplied ideal circuit represents the source by E in series with resistance Rs. Connecting a voltmeter of input resistance Rm completes the circuit. Assume positive resistances, a stable source and a meter whose indication equals its terminal voltage.

The common current I satisfies

    E = I*Rs + I*Rm
    V = I*Rm

Eliminating I gives

    V = E*Rm/(Rs+Rm)
    E = V*(1+Rs/Rm)

For Rs=Rm=1 megohm and V=5 volts, the inferred open-circuit voltage is 10 volts. Substitution returns I=5 microamperes and the original 5-volt indication. The two voltage drops explain both the sign and magnitude of the correction.

If the desired quantity were instead the connected terminal voltage, V would already be the value in this ideal model. The measurement question determines which result is needed.

As Rm becomes large relative to Rs, loading becomes small and V approaches E. For a use that needs only a bound on this effect, E-V=V*Rs/Rm supplies it. If Rs/Rm is at most 0.001 and V is 5 volts, the loading correction is at most 0.005 volts. Whether that is negligible depends on the receiving question and the other uncertainties.

If Rs is unknown, the same relation can expose an unresolved contribution. With V=5 volts, Rm=1 megohm and Rs between 0.8 and 1.2 megohms, E lies between 9 and 11 volts under the ideal assumptions. The interval may be enough. A performed measurement additionally accounts for indication and resistance uncertainty and relevant model inadequacy.

#### C.16.MR:5.2 - Build the relation for an assessment of independent performance

The sought quantity p is the fraction of a stated population able to perform a specified action independently under specified conditions. An applicable assessment account supplies s, the probability of a positive response when that capability is present, and f, the probability when it is absent.

Partition the population by the capability. The probability of a positive response is

    q = s*p + f*(1-p)
      = f + (s-f)*p

For s=0.9 and f=0.1, q=0.1+0.8*p. A sample positive fraction of 0.7 gives the estimate p=0.75 obtained by substituting the sample fraction. Its use also depends on sampling uncertainty, uncertainty in s and f and whether those rates apply to this population and procedure. The formula describes the expected response; the sample proportion estimates it.

If s=f, q is independent of p and the test does not distinguish the two conditions through this response. The failure is visible in the constructed relation. Further estimates of that same marginal positive rate cannot identify p through this relation.

Now change the procedure by offering hints. The earlier rates may cease to apply. Recover rates for the changed procedure or restore independent performance if that remains the target. The subject's capability and assessment Methods establish those conditions; the general construction shows where they enter the inference.

This population estimate does not identify which particular people or agents have the capability. That different question requires an individual assessment account.

#### C.16.MR:5.3 - Interpret a wrapping event counter

A modeled counter increments once for each event and retains a value from 0 to 15, returning to 0 after 15. Readings immediately before and after an interval are r0 and r1. The sought quantity is the number N of intervening events. Assume no reset, no missed increment and readings taken at the stated interval boundaries.

The counter operation gives

    r1 = (r0+N) mod 16
    N = d + 16*k

Here d is the least nonnegative remainder of r1-r0 modulo 16, and k is a nonnegative integer. With r0=14 and r1=3, d=5: the compatible counts are 5,21,37 and so on.

If the interval is known to contain fewer than 16 events, N=5. Without that bound, subtracting the displayed numbers or returning the modular difference loses possible complete wraps. A wider counter, a recorded wrap count or shorter observation intervals can supply the missing information for a later measurement.

To infer elapsed time, another relation is needed: the counter must count timing ticks with an applicable tick-duration account. A counter of arbitrary work events alone measures no duration. This identifies a missing relation rather than inventing one from the numerical display.

### C.16.MR:6 - Bias-Annotation

The examples have small, supplied subject models. Real instruments can require dynamic response, correlated influences or numerical inversion. Assessment rates can depend on population and conditions. A familiar model should therefore be reused with its applicable range and interpretation.

The construction can be shared across human, organizational and machine measurement practices. Its concrete laws and response models remain those of the subject. The general steps do not establish that a statistical assessment measures an individual's capability.

### C.16.MR:7 - Conformance Checklist

- **CC-C16.MR-1 - Sought property.** Subject, Characteristic and target conditions identify what is to be determined.
- **CC-C16.MR-2 - Indication production.** The procedure's consequential interactions and transformations have relations with recoverable meanings.
- **CC-C16.MR-3 - Shared values.** Composed relations agree on units, stages and shared quantities.
- **CC-C16.MR-4 - Influences.** Consequential effects enter where they act; unknown effects retain their relevant uncertainty.
- **CC-C16.MR-5 - First result.** A case supplies a sought value, compatible set, conditional result or missing contribution.
- **CC-C16.MR-6 - Interpretation.** A statistical expectation, sample estimate and obtained measurement retain the qualifications needed by the use.
- **CC-C16.MR-7 - Useful return.** Further work addresses a distinction that can change the receiving result.
- **CC-C16.MR-8 - Changed conditions.** The construction identifies which relation must be reconsidered when the procedure, range or target changes.

### C.16.MR:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Effect on use | Repair |
| --- | --- | --- |
| Read the display as the sought value after the procedure changes the subject | The answer can concern the measured arrangement instead of the target conditions. | Model the interaction and state which quantity is sought. |
| Copy a correction without its measurement relation | Its direction, magnitude or range can be wrong for the current arrangement. | Recover where the effect enters and derive its contribution. |
| Fill an unknown influence with zero | A numerical answer hides unresolved alternatives. | Keep the influence unknown and use available bounds or a justified distribution. |
| Treat expected response as an error-free observed proportion | The inferred population property loses sampling uncertainty. | Keep the response model and sampling inference distinct. |
| Repeat measurements to remove structural ambiguity | The same indication can still fit different sought values. | Change the relation or observation that distinguishes those values. |
| Model every conceivable influence before answering | The work expands without changing the result. | Test the consequence of the influence for the intended use and stop with an adequate result. |

### C.16.MR:9 - Consequences

The reader obtains a relation usable for interpreting or planning a measurement. Intermediate interactions, response assumptions and unknown influences become parts of a calculation whose result can be inspected and revised. A missing contribution becomes a specific next task.

The cost is recovering the procedure and the subject relations it uses. A complete metrological or statistical investigation can be much larger than the first construction. The Method permits a useful conditional result or interval before that larger work.

### C.16.MR:10 - Architectural Rationale

The result is a relationship for interpreting an indication with respect to a specified property. A model of the subject can predict its behavior while leaving the measuring procedure undescribed. Connecting that procedure to the target property is an independently useful construction.

Construction, resolving ambiguity and repairing an inadequate arrangement cooperate but can start from different inputs and return different results. A measurement relation can be available before its data are obtained. It can also reveal that a particular indication leaves the target unresolved.

Physical interaction, mathematical expression and computational readout participate together. Their roles explain why revising a measuring instrument can require revising an equation or interpretation, and why a new display format alone may leave the underlying ambiguity unchanged.

### C.16.MR:11 - SoTA-Echoing

The working question is to connect an indication to the property needed by the task. The selected construction follows the indication-producing procedure and includes its consequential interactions and transformations. A serious alternative is to reuse a supplied direct calibration or conversion. That alternative saves derivation when it already applies to the current arrangement and range. The present Method is needed when a changed interaction, procedure or target leaves that relation incomplete.

The voltmeter case exhibits the trade-off. Reading V directly is sufficient for the connected terminal voltage in the ideal model. Recovering the open-circuit value adds the source resistance and loading relation; it changes the answer from 5 to 10 volts in the worked case. At a sufficiently small resistance ratio, an available loading bound can justify the simpler use. More detail is valuable through that changed interpretation.

[GUM-6:2020, §§7, 9-10](https://www.bipm.org/documents/20126/2071204/JCGM_GUM_6_2020.pdf) develops measurement models from a principle, empirical information and effects of implementation. **Adapt:** :4.2-:4.4 combine those contributions, locate an influence where it acts, and retain unknown effects when no useful correction is available. The guide concerns quantity measurement; the assessment and counter constructions here use their separately stated response and operation models.

[Dounas-Frazer and Lewandowski (2018), §2](https://arxiv.org/pdf/1805.10334), distinguishes the investigated phenomenon, measuring equipment and their models. **Adapt:** :4.1-:4.2 recover the measurement contribution, while :4.5 preserves the separate model and arrangement repairs. The source studies experimental physics education; this cross-practice construction does not claim that its educational findings establish transfer to all agents or domains.

The common procedure and worked cases are a conceptual synthesis. Reopen the construction choice when a supplied calibration achieves the same interpretation with less work, or when a newly consequential interaction or response condition defeats the existing relation. Detailed uncertainty propagation, calibration design and model identification remain substantial specialized Methods.

### C.16.MR:12 - Relations

- **C.16** identifies measurement, Characteristic, Scale, indication, model and obtained result.
- **B.5.RC** recovers a needed construction from its description; **B.5.FM** develops a first model.
- **A.3.3.CC** constructs compatible variables and constraints; **A.3.3.TR** constructs a rule for change where a dynamic measurement requires one.
- **A.3.3.PI** retains information for a future prediction; a measurement relation supplies its observation contribution.
- **C.29.2** constructs the computation needed to obtain a modeled result.
- **B.5.MPC.R** revises connected physical, mathematical and computational contributions.
- **C.11.DUA** decides whether reducing a remaining ambiguity is worth the work.

### C.16.MR:End
