## OPS.15.1 - Derive Operating Quantities from Events

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative

### OPS.15.1:1 - Problem frame

**Use this when** a decision depends on waiting, unfinished work, output or resource use, but the available totals do not make clear what was counted. Two teams report different “cycle times”. A batch completion appears against several orders and inflates machine use. A short observation window excludes unfinished cases and makes service look faster.

Choose the operating subject and boundary events, construct the relevant intervals or counts, and aggregate them under a common clock and population rule. The first useful result can be a corrected comparison or a bound showing that an unknown event cannot change the decision.

**Start with one case.** Identify the events that would start and end the proposed measurement, then locate what the records actually establish about them. A database timestamp can mark entry of a record rather than occurrence of the work event.

**Practical gain.** The practitioner can tell a change in service from a change in counting, find which records are needed for a particular decision, and use partial observations without inventing a complete history.

The reader needs to identify the operation's subjects and events and understand elementary intervals, rates and averages. Statistical inference requires additional methods when the intended claim goes beyond the observed cases.

Use an existing quantity directly when its definition and observations already fit the receiving question. This pattern does not require a new log format or complete event capture before an operating decision.

### OPS.15.1:2 - Problem

An operating name can conceal several measurement constructions. Time from customer request, internal release, service start or approval produces different intervals. Counting orders, visits, samples or occupied resources produces different populations. A shared event can belong to several accounts without becoming several occurrences.

Aggregation can hide these differences. A mean over completed cases omits those still waiting. Summed task durations double-count overlapping occupation. Missing end events are silently treated as zero or as completion at the observation cutoff. The resulting number may be calculated correctly from the records while answering another question.

### OPS.15.1:3 - Forces

| Force | Tension |
| --- | --- |
| Common indicators and different decisions | One familiar name is convenient, but recipients can need different event boundaries. |
| Case detail and shared work | Individual cases need their own histories while a batch or resource episode occurs once. |
| Timely feedback and unfinished cases | A short window supports prompt action but cuts through residence and service intervals. |
| Comparable aggregates and heterogeneous work | Counts are simple while resource demand, routes and acceptance conditions differ. |
| Additional observation and useful action | A missing timestamp may matter or may be irrelevant to the decision already supported. |

### OPS.15.1:4 - Solution

Define the quantity from the operating question, reconstruct the events and their subjects, derive the intervals or count changes, and then aggregate. Keep incomplete observation visible in the result. Return the number with enough meaning to use or recompute it.

#### OPS.15.1:4.1 - Choose what the decision needs to measure

Name the subject and the consequence being compared. A customer's time to an accepted result, a machine's occupied time and the number of service visits answer different questions even when they concern the same order.

Define membership of the counted population. State when a subject enters and leaves that population. For unfinished orders, choose the arrival and completion events for the service being considered. For a ready queue, include the conditions that make the next operation possible.

Separate unique cases from visits. A return for correction may create another visit to a station while the same customer case remains unfinished. If the case is closed and later reopened, decide whether the receiving question concerns separate episodes or one extended service. Use its operating meaning; do not decide from the number of log rows.

OPS.15 supplies the decision-specific account, and OPS.3 helps identify its subjects. A short statement of the chosen quantity is enough when it removes the ambiguity.

#### OPS.15.1:4.2 - Relate the records to the operating events

For the events used in the calculation, recover the subject, event meaning and occurrence time as far as the available information supports them. Distinguish occurrence time from recording time when their difference affects the result. Reconcile time zones, clock offsets and timestamp precision before comparing events from different systems.

Recover the relationships needed by the question. A dispatch can concern several order lines; one machine cycle can process several parts; one invoice can cover charges for several deliveries. Keep the common event identifiable while following each related subject. A row per event-subject relation is a useful representation, but its row count is not automatically an event count.

Check what the recorded label establishes. “Completed” may mean that a worker reported completion, that inspection accepted the result or that the customer received it. If the receiving comparison needs a later event, either obtain it or report the result under the available boundary.

Use MMP.7 when selection, censoring or the recording procedure affects an inference. Missing records do not by themselves show that the corresponding work did not occur.

#### OPS.15.1:4.3 - Construct the intervals and count changes

For each relevant subject or visit, pair the boundary events belonging to that episode. Its elapsed residence is end time minus start time. If only a range for an endpoint is known, propagate that range instead of selecting an unsupported point.

For resource use, reconstruct the intervals during which the resource is occupied under the chosen meaning. Occupied machine time, operator attention and reservation can differ. A machine can run unattended while its operator serves another machine.

Combine intervals according to the quantity. For a single resource's occupied fraction, take the duration of the union of its occupied intervals; overlapping descriptions of the same occupation are counted once. To measure total occupied resource-hours across distinct resources, sum those resource-specific durations. To measure part residence during batch processing, retain each part's interval.

Calendar time and available working time are also different quantities. For working time, intersect the interval with the relevant open-calendar intervals before adding durations. A calendar conversion does not remove a customer's overnight wait from elapsed service time.

For counts, follow entries and exits of the chosen population. With fixed case identity and no splitting or merging, ending population equals starting population plus entries minus exits. Include cancellations or other exits under their own meanings. If the subject is split or combined, recover the changed counting unit before using that balance.

#### OPS.15.1:4.4 - Respect the observation window

Choose a positive-duration observation window for a time-average quantity. Include the subjects already present at its beginning and those still present at its end.

For a subject entering at a and leaving at d, its contribution within the window [u,v] is:

~~~
overlap = max(0, min(d,v) - max(a,u)).
~~~

For a subject known to remain present through v, use v as the overlap endpoint without asserting completion at v. An unknown arrival before u similarly contributes from u while leaving the full residence unresolved.

Add these overlaps to obtain the population-time area. Divide by v-u to obtain the mean population during that window. This is the area under the population count: each present subject contributes one unit for each unit of time it remains present.

For a fixed counting unit without splitting or merging, an empty-to-empty interval gives a useful relation. Its population-time area equals the sum of residence times of all episodes that leave. With at least one departure, mean population equals departure rate multiplied by mean residence of those same episodes. The departure rate is the successful completion rate only when every departure meets the chosen completion condition. If no episode occurs, the area and mean population are zero; a mean residence over zero departures is undefined.

For example, three cases enter at zero. One is cancelled at hour one; the others complete successfully at hours two and three. Area is 1+2+3=6 case-hours over three hours, so mean population is two. All three departures contribute to that relation. The two successful completions remain a separate result count.

On an arbitrary cut window, the departed-episode mean and departure rate alone generally omit the partial intervals. Calculate each present episode's overlap with the window, including episodes still unfinished at its end.

This finite observation identity does not estimate an unseen tail, establish a long-run regime or explain what caused waiting. OPS.10 uses the appropriate capacity or queueing model when those further questions matter.

#### OPS.15.1:4.5 - Aggregate only compatible observations

Keep the population, event pair, clock and weighting rule consistent within the reported aggregate. Combine totals before dividing when group sizes differ. An unweighted mean of departmental means gives each department equal weight, not each case equal weight.

Choose the weighting from the question. A case-weighted mean describes a typical counted case. Resource-demand weighting describes a different burden. Retain classes when the proposed change affects them differently or an aggregate conceals a service commitment.

To compare policies, use the same recipient boundary unless changing that boundary is the point of the decision. If internal admission moves later, report upstream waiting together with internal residence before concluding that customers receive results sooner.

For uncertain or incomplete observations, derive the consequence still supported. A residence known to be between four and ten hours cannot decide an eight-hour criterion. It can already satisfy an upper limit of twelve hours under the same assumptions. Choose further observation through C.11.DUA; a complete history is not a prerequisite for every comparison.

#### OPS.15.1:4.6 - Return the quantity to the operating decision

Explain the result in terms the recipient uses: for example, “the machine was occupied for forty of the sixty available minutes” or “the shorter internal time excludes four hours of waiting before admission”.

Retain the definition and observations needed to reproduce a consequential quantity, using the existing account when it suffices. Distinguish a direct calculation from a model-based estimate or forecast. MMP.13 supplies inference when the result must generalize beyond the observed population.

When a check fails, localize the repair: a subject was counted twice, a boundary event was misidentified, a clock was shifted, an unfinished interval was excluded, or the aggregation rule answered another question. Correct that construction and the decisions that used it. A changed route, acceptance event or recording procedure reopens the affected quantity.

### OPS.15.1:5 - Archetypal Grounding

#### OPS.15.1:5.1 - A window cuts through unfinished work

Observe an operation from hour zero to hour eight. Case A arrived at minus three and leaves at two. B arrives at one and leaves at four. C arrives at six and is still present at eight.

| Case | Full known residence | Residence inside [0,8] |
| --- | --- | ---: |
| A | 5 hours | 2 hours |
| B | 3 hours | 3 hours |
| C | At least 2 hours; unfinished | 2 hours |

The population-time area is seven case-hours, so mean population is 7/8. Counting departures gives two in eight hours. Their full residence mean is four hours; multiplying 2/8 by four gives one, not 7/8.

There is no contradiction. The departure cohort includes three hours of A before the observation window and excludes C's two observed hours. Computing the clipped intervals answers the window question. C's eventual completion is unnecessary for that result.

Now the question changes to the mean full residence of all three cases. C's endpoint matters. If no later information is available, the sum is at least ten hours and the mean at least 10/3, with no supported finite upper bound. The earlier mean population does not fill that missing endpoint.

#### OPS.15.1:5.2 - One batch, several parts, one machine

A machine processes three parts together from minute zero to thirty. The completion event is linked to all three parts. The machine is otherwise available throughout a sixty-minute observation window.

The batch occupies thirty machine-minutes: utilization under this occupied-time definition is 30/60. The parts accumulate ninety part-minutes of batch residence. Copying the cycle interval into three part records preserves each part's history but does not create ninety machine-minutes.

Part 2 requires another ten-minute cycle from minute forty to fifty. Machine occupation becomes forty minutes and utilization 40/60. There are three distinct parts and four processing visits. The returned part's additional visit consumes capacity while its customer-level completion follows the acceptance rule.

If an operator attends only loading and unloading, machine occupation does not establish operator attention time. Recover those intervals before making a staffing claim.

#### OPS.15.1:5.3 - An unknown endpoint need not stop the decision

One uninterrupted processing episode starts at hour ten. A reliable observation shows it still in progress at fourteen and a later observation shows completion by twenty. The elapsed processing duration is bounded by four and ten hours; its precise endpoint is unknown.

A question about completion by eighteen remains unresolved. A question about completion by twenty-two is already settled by the observation at twenty. The second decision needs no search for the precise endpoint. If the claim instead concerns uninterrupted duration and interruption was possible but unobserved, that premise must be revisited before using the duration bound.

These cases are constructed demonstrations of the measurement operations.

### OPS.15.1:6 - Bias-Annotation

Event logs privilege what the information system records. Unrecorded work, informal coordination and off-system waiting can disappear from an apparently complete account. Compare the chosen event meaning with the work when that omission could alter the decision.

Case counting also privileges discrete populations. For continuous material, the corresponding subject may be an amount with changing inflow and outflow. Retain its unit and balance; a row count cannot replace the measured amount.

### OPS.15.1:7 - Conformance Checklist

- The quantity has a subject, population, event boundaries, clock and receiving question.
- Common events remain identifiable when related to several subjects.
- Case, visit, part and resource counts are distinguished where their consequences differ.
- Interval combinations match the question, including overlap and calendars.
- A cut observation window retains initially present and unfinished subjects.
- Aggregation uses compatible definitions and an appropriate weighting rule.
- Missing observations produce supported bounds or an unresolved contribution rather than invented completion.
- A claimed service improvement retains the recipient's waiting origin.

### OPS.15.1:8 - Common Anti-Patterns and How to Avoid Them

| Mistake invited by ordinary records | Consequence | Repair |
| --- | --- | --- |
| Count one event-subject row as one event | A shared batch or delivery is multiplied. | Count distinct occurrences or the intended subject relations explicitly. |
| Treat the observation cutoff as completion | Unfinished work receives a false short duration. | Clip its exposure to the window and retain its unresolved endpoint. |
| Sum overlapping resource intervals | Recorded occupation can exceed possible available time. | Form the union for each resource before calculating its occupied fraction. |
| Compare internal time after moving admission | A counting change appears as faster customer service. | Include upstream waiting under the unchanged recipient boundary. |
| Use a mean without its population and weights | Different mixtures masquerade as changed performance. | Reconstruct the aggregate from compatible totals and counts. |

### OPS.15.1:9 - Consequences

Operating comparisons become reproducible and many apparent disagreements resolve into different measurement constructions. Partial observations can still support a useful decision.

Recovering event meaning can require domain knowledge that a data export does not contain. Some questions remain underdetermined, and some aggregations intentionally discard detail. Retaining those limits prevents an observed quantity from silently becoming a prediction or explanation.

### OPS.15.1:10 - Architectural Rationale

Events establish boundaries from which intervals and populations can be constructed. The receiving question then determines how to combine them. This ordering lets one set of observations support several accounts without forcing all participants to use one completion event.

The method distinguishes an occurrence, its record and its participation in several subjects' histories. That distinction preserves common work while avoiding duplicate counts. Window clipping follows the same principle: retain the part actually observed without inventing the unobserved rest.

General measurement and inference methods supply the epistemic conditions. The operating contribution is how arrivals, service, returns, delivery and resource occupation produce the quantities used by operating decisions.

### OPS.15.1:11 - SoTA-Echoing

When a decision needs comparable quantities from shared events or a cut observation window, derive the interval contributions before averaging. Adopt the sample-path area construction from [Sigman's notes on Little's Law](https://www.columbia.edu/~ks20/stochastic-I/stochastic-I-LL.pdf) and adapt the shared-event representation of [OCEL 2.0, §§2–4](https://www.ocel-standard.org/2.0/ocel20_specification.pdf). This is preferable to a completed-only average when a window cuts through visits: :5.1 obtains 7/8 for mean population where the departure shortcut gives one. Sections :4.3–4.4 retain partial exposure and all relevant exits. Sigman's area argument supports that finite calculation; estimating an unseen tail or a long-run regime requires additional premises.

Summing a shared processing interval once per part overstates machine time. In :5.2 this would turn thirty machine-minutes into ninety. Keeping the common cycle identifiable while following its three parts preserves both the machine occupation and part residence. OCEL supplies qualified event-to-object and object-to-object relations and changing attributes. Its instantaneous records still require the interval interpretation in :4.2–4.3; the standard does not establish how much work occurred or whether a policy improved service.

The added effort is to recover a shared relationship or an interval boundary when the receiving quantity depends on it. A simple case table remains sufficient when events belong to one case and the table retains the boundaries needed for the calculation. A few shared-event references can handle a small batch; full OCEL serialization is unnecessary. Sections :4.2–4.5 retain only the relationships, window contributions and weighting needed by the question.

[Hopp and Spearman, Factory Physics](https://www.waveland.com/browse.php?t=587), supplies the operating uses of flow, cycle-time and capacity quantities. This pattern reconstructs their populations and boundaries before applying those relations; a compatible average alone does not establish a cause. Reopen the construction when an event changes meaning, a recording change affects an interval or shared occurrence, the decision needs another population, or a simpler construction preserves the same required distinctions. The affected event relation or aggregate is the place to revise.

### OPS.15.1:12 - Relations

OPS.15 chooses the decision-specific account; this method constructs its operating quantities. OPS.3 supplies subject distinctions, OPS.8 consumes readiness and waiting quantities, and OPS.10 uses them in capacity and service models.

OPS.11.1 reconciles operating models whose inputs and outputs use these quantities. C.16 supplies common measurement, and F.0.1/F.9 recover and relate local meanings when needed.

MMP.7 accounts for the observation and recording law; MMP.13 supplies inference. C.11.DUA governs the worth of another observation. C.29 qualifies using a mathematical relation to answer the operating question.

### OPS.15.1:End
