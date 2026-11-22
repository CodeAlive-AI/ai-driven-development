## SYSE.19 - Revalidate Engineering Decisions When a Relied-on Source Changes

> **Status:** Stable

### SYSE.19:0 - Use This When

Use this pattern when a later edition or replacement may change an engineering source claim—for example, one in
a model, requirement, standard, MethodDescription, supplier specification or research result—and the project needs to find which
decisions depend on it. Determine which uses remain supported, which need further Work, and which must be limited or stopped.

Begin with the predecessor and later source epistemes. Compare their claims and applicability for the engineering use.
Trace material differences to the decisions and Work results that rely on them, including implicit premises. Revalidate an affected use when needed. A
new file or edition label is a reason to inspect the source.

The first useful result is a **bounded source-change impact decision**: the engineering use supported by the current
basis, with any limitation or blocker that matters to its receiver. A compatible carrier change can finish with a
repaired reference. For a material claim change, preserve, narrow, reopen or withdraw only the affected use. New
revalidation Work is selected when the receiving question warrants it. Identify any later performed Work, returned
evidence and replacement engineering decision separately.

Use `SYSE.14` for an engineering release decision and `SYSE.13` when configuration identity or effectivity is the question. Use `SYSE.7`
to coordinate descriptions needed by one decision and to maintain their connections while the work continues to rely on them. Use `SYSE.10`
to qualify relevant model, experiment or trial evidence. Use FPF `E.15` when the edition being revised is an FPF pattern.

This method assumes the engineering claims can be interpreted and a suitable specialist calculation,
calibration or test Method obtained when needed. Compare the reasoning before and after the source change.
If an inference has lost support, work out what would restore it for the receiving decision
and obtain the result when warranted. A laboratory technique needs its own professional basis; release requires the applicable authority. If the relying
decisions are unknown, use `A.10.1:4.3–A.10.1:4.4` to discover them.


#### SYSE.19:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| engineering source | A claim-bearing episteme that an Agent uses while performing engineering Work. Record its publication, carrier, or access relation only when that relation changes the use. |
| source edition | An episteme related to an earlier episteme by the `C.2.1` edition-continuity predicate. A revision label or date is evidence to inspect, not the edition relation itself. |
| replacement source | A later episteme proposed for the predecessor's use when edition continuity is absent or unresolved. Its applicability is decided for that use. |
| publication or carrier change | A change to availability or presentation—for example, another URL, file, layout, form, or publication occurrence. Compare claim content before treating it as a semantic change. |
| material claim change | A change in claim content or applicability that can alter engineering action—for example, a changed proposition, scope, assumption, limit, evidence status, or MethodDescription statement. |
| direct reliance | A named engineering decision or Work result whose justification or content depends on a source claim as a premise under stated conditions. A citation or link is discovery evidence until the receiving content confirms that dependence. |
| affected reach | The set of decisions reached through direct-reliance relations whose engineering action can change because of the material claim change. |
| revalidation Work | Work that rechecks an affected claim or decision under the current configuration, conditions, Method, evidence needs, and authority. |
| decision disposition | For this decision, select one of `preserve`, `narrow`, `reopen`, `supersede`, `withdraw reliance` or `blocked`. |

The source episteme, its publication, the claim-change observation, planned revalidation, performed Work, returned
evidence, and engineering decision have separate identities. An Agent performs revalidation Work. Equipment,
models, repositories, and the engineered System are examples of other participants; state each direct relation.

### SYSE.19:1 - Problem Frame

Engineering decisions depend on changing sources. For example, a supplier can revise a material limit, a standard
can change an interface claim, a MethodDescription can narrow an operating range, or a research result can weaken
an evidence line. The engineered System may stay unchanged while the warranted decision basis changes. Conversely,
a new carrier or revision label may leave every relied-on claim intact.

The project needs two kinds of continuity. Historical source and decision identities stay recoverable so earlier
Work can be understood. A change to the source calls for reconsideration only where it changes a premise on which the decision relies. Repeating everything is
expensive and hides the reason for change; comparing only files can miss a one-sentence change that alters release.

A source-change impact decision connects changed claims to their actual use in engineering Work and states what
revalidation is needed for the current configuration.

### SYSE.19:2 - Problem

Two damaging shortcuts recur. One repeats every downstream activity merely because the source label
changed. The other keeps every decision merely because the engineered System did not change. Both avoid the
central question: which relied-on claim changed enough to alter engineering action?

Other recurring failures appear when the source episteme cannot be identified, reliance is known only at document
level, a semantic difference is confused with a text diff, revalidation uses the wrong configuration, or a passing
test is treated as permission or release. The project then either spends effort without a decision or keeps a
decision whose premise no longer applies.

### SYSE.19:3 - Forces

Recurring tensions include:

- Revalidation should stay bounded, while an undeclared reliance can matter more than a declared trace link.
- Source identity must remain recoverable without turning every carrier change into a semantic event.
- One changed sentence can alter release; a large rewrite can leave the relied-on premise intact.
- Automated search can find candidate uses. Engineering judgement determines whether the changed claim matters to them and where it applies.
- A newer official or popular source can fit the use worse than an older bounded source.
- Preserve the reason for retaining a decision so that it can be recovered when later Work needs it.

### SYSE.19:4 - Solution

Compare source claims, recover their actual engineering uses, and revalidate only what is needed to decide
whether the affected engineering decisions remain usable.

#### SYSE.19:4.1 - Perform the Move

1. **Start from the decision or the changed source.** If a receiving decision is known, state it, any Work result it relied on, the configuration, use and interval, and what action or warranted conclusion might change. If the
   source change is the starting point, compare the editions or replacement in steps 2–3. Trace material claim changes to their uses in steps 4–5.
2. **Identify the source epistemes.** Recover the predecessor and later claim-bearing epistemes, their applicability,
   provenance, and publication or carrier facts when those facts matter. Establish an edition relation only when
   its predicate obtains; otherwise treat the later source as a replacement candidate or record an identity gap.
3. **Compare claims rather than files.** State every material change in claim content or applicability—for
   example, proposition, scope, assumptions, limits, evidence status, or MethodDescription content. Classify the
   publication and carrier differences separately from changes to claim content. When relevant meaning, applicability and access remain
   compatible, finish with any needed reference repair. Missing comparison facts remain a scoped gap.
4. **Recover direct reliance.** For each material claim, inspect candidate receiving content found by means such
   as search, citations, traces, or AI assistance. State the decision or Work result and the direct premise or
   evidence-use relation that connects it to the claim.
5. **Bound the affected reach.** Distinguish `depends`, `mentions only` and `unresolved` within the searched frame. Group
   equivalent irrelevant mentions; retain a short exclusion reason when the receiver needs it. Follow a dependency while
   the changed premise could alter a downstream conclusion, its qualification or the engineering action it supports.
   Use `A.10.1` when several receiving uses need discovery and retain the coverage needed for the stated conclusion.
6. **Choose any needed revalidation Work.** Use adequate existing evidence first. A scoped limitation or blocked
   use can be the completed answer. Select further Work under `C.11.DUA` when its obtainable contribution warrants
   the complete programme burden within the receiving window. For selected Work, name the Agent, Method,
   configuration, conditions, evidence need, authority, cost and stop. Cost does not make an unsupported use safe
   or supply missing permission.
7. **Perform and qualify selected Work.** Identify performed Work and returned evidence separately. State
   what the result supports for the current configuration and what remains unknown.
8. **Decide separately for each affected engineering decision.** Assign one disposition from section 0.1 and state its reason, evidence
   and applicable interval. Name next Work only when selected for this use. If a check result bears on the
   decision, the authorized Agent uses it as a premise, including when it defeats the proposed use.
9. **Supply the result and preserve history.** Give the recipient that will use the conclusion the supported use, relevant
   revalidation evidence and any material blockers. For a change or release decision, supply the Agent authorized to make
   it. That return can complete the question. Prepare a common account when a receiver needs an overview, and keep earlier
   source editions and decisions recoverable for their original uses and intervals.
10. **Stop at the completed receiving answer.** Finish a compatible reference repair directly. For material change,
    return the qualified in-scope decisions or the specific blockers and preserve independently resolved branches. A
    no-impact claim requires adequate discovery coverage and actual-use support; uninspected or inaccessible
    surfaces remain gaps.

Source comparison, design, testing, operation, and release Work may overlap. Only dependencies established for
the current claims impose an order.

##### SYSE.19:4.1.1 - Recover the reasoning that made the decision usable

Begin with one decision whose continuation matters: for example, allowing a controller to start in a cold
room. Recover what that decision required, what the source supplied and why the latter supported the former.
A useful short account is: *under these conditions, this observation or bound supports this claim, which
permits this engineering choice*. Recover the configuration, units, operating range and interval at the
places where changing them would alter the inference.

For a quantitative claim, reconstruct the governing calculation or constraint. For a qualitative claim,
recover the mechanism or argument connecting the evidence to the conclusion. A test report can support
observed behaviour on a specimen without supporting every produced unit or future operating condition.
Distinguish a requirement about what must hold from a claim that it holds and from the evidence offered for
that claim. An old approval establishes who decided; it does not repair an invalid engineering premise.

The deciding engineer can use this account to see whether a connection holds or where it fails. If the original reason
cannot be recovered, identify the person or function responsible for the design or assurance claim and the
question that needs reconstruction. The missing reason limits reliance; it does not establish a physical failure.
Use `SYSE.10:4` for the model, specimen, measurement and inference qualifications needed by the account.

##### SYSE.19:4.1.2 - Substitute the changed premise before ordering new work

Read the old and new claims with their applicability conditions. Temporarily substitute the later
claim into the recovered reasoning, retaining other premises only where still justified. Ask what the
engineer can now conclude and do differently. This is a test of the argument, not a claim that the new source
caused the physical system to change.

Several changes call for different responses:

- A corrected value can change a calculated margin. Recalculate the affected result before deciding whether
  another experiment is needed.
- A reduced validity range can remove support for one operating condition while preserving another. Outside
  the supported range, the old inference is unavailable; failure of the system is not thereby observed.
- A withdrawn experiment or disputed model assumption can weaken the evidence without providing an opposite
  numerical answer. Look for independent support and check whether it shares the disputed basis.
- A changed requirement can make an unchanged measured result insufficient. Establish that requirement's
  applicable version and effective conditions; a test cannot authorize a different requirement.
- A new description of a calibration or test Method can change how further evidence must be obtained without
  proving that every earlier observation is false. Inspect which earlier uses relied on the changed part.

The later source may be less applicable, disputed, or effective only for future products. Explain that
difference before replacing a current basis. Conversely, an erratum can undermine a premise used in past
decisions. Preserve the historical source and decision as history while reconsidering any historical claim
that depended on the error. Preservation is not a verdict that the earlier conclusion was correct.

##### SYSE.19:4.1.3 - Find the engineering consequences and the boundary of propagation

Use the changed premise to search both outward from the source and backward from the affected engineering
use. Search identifiers and citations, but also the old value, equivalent formula, operating condition or
assumption in models, test procedures, assurance arguments and release decisions. Inspect the receiving
content before classifying a relation. A bibliography entry can be irrelevant while an uncited spreadsheet
cell carries the decisive assumption. `A.10.1:4.3–A.10.1:4.4` supplies the search-frame and coverage method when
several uses need discovery.

At each confirmed use, perform the substitution in section 4.1.2. Continue through its consumers if the
changed result, qualification or required action could alter their conclusions. A changed internal value can
leave an outward bound valid because sufficient margin remains. Explain that surviving bound and stop that
branch there. If a relation or receiving document is unavailable, keep that branch unresolved; complete the
independent branches whose premises can be inspected.

Inspect shared and joint premises where they matter. Two changes may each fit an error budget separately and
exceed it together. Several documents quoting one experiment provide one evidence line, not independent
confirmation. A joint decision requiring several conditions cannot inherit a positive conclusion from only
the resolved conditions. The propagation boundary is where the receiving engineering conclusion is supported,
not the end of a graph query or the boundary between departments.

##### SYSE.19:4.1.4 - Construct the missing revalidation from its required result

Start with the conclusion now needed and work backward to the missing support. Then follow a proposed way
forward: what input the engineer obtains, what operation transforms it, which result comes back, and why that
result would repair the specific inference. Keep a qualified available operation intact. Construct or obtain
only the operation or connection that is missing.

| What prevents the receiving conclusion | Candidate way to obtain the needed contribution |
| --- | --- |
| A parameter changed but the model and its use remain applicable | Recompute the affected output or sensitivity bound with the new parameter; compare it with the same required result. |
| Existing observations are valid but the old interpretation changed | Reanalyse the original observations under the current interpretation, if they contain the required quantities and conditions. A missing measurement cannot be supplied by reinterpretation. |
| Support is absent for a particular unit or operating range | Obtain a suitable calibration, experiment or trial on those units and conditions; establish how its observations support the intended range and duration. |
| The relied-on Method or model is unsuitable | Use `SYSE.15` for a changed Method choice or `SYSE.7` for a changed decision-usable description. Obtain any missing professional Method-development result before relying on it, then qualify its evidence through `SYSE.10`. Repeating the old operation does not fix its failed premise. |
| Applicability, obligation or permission is unsettled | Obtain the relevant source or decision from its responsible holder. A successful engineering test supplies neither that interpretation nor that authority. |

For a test proposal, derive the discriminating observation from the failed claim. Name the changed condition
to exercise, the unchanged controls needed for attribution, and the result that would support, contradict or
leave the claim unresolved. Do not select a familiar test merely because it is available. If a bound is
claimed over an interval, show why the sampled observations cover that interval; add a justified model or
uncertainty bound, change the test, or limit the conclusion to the observed points. Similarly, one calibrated
unit does not qualify its neighbours without a justified population inference.

This construction may return several adequate ways: reuse qualified observations, obtain a supplier's
applicable result, perform a targeted experiment, change the engineering solution, or restrict its use. It
may also expose that the required evidence cannot be obtained. Compare these whole continuations, including
the resulting usefulness, through `C.11.DUA:4`; use `SYSE.6` when they become substantial design alternatives.
There is no fixed requirement to run a model, a calibration and a chamber test on every source change.

##### SYSE.19:4.1.5 - Choose and perform an available continuation

First compare what the present evidence already permits with what the project needs. A narrower operating
range can answer the question only if its receiving use remains worthwhile and its conditions can be met.
A proposed restriction that no operator or control can enforce is not an available continuation.

For additional work, identify the performers, capability, equipment, specimens, access and authority that make
the proposed result obtainable. Include preparation, coordination, execution, interpretation, delivery and
displaced work in the burden. Check joint use of a laboratory or specialist across the selected activities;
individually timely estimates do not establish a timely programme. Select work when an attainable outcome can
change the decision or meet a necessary evidence condition within the relevant horizon. Keep a delay or stop
when no available option supports the required use. Cost cannot turn a missing premise into evidence.

Give each performer the claim, configuration and conditions needing support, and the contribution expected from that work. Before
relying on the return, establish what Method, configuration and conditions were actually used and what the
observations and limits were. A changed instrument, specimen or procedure may reopen only the inferences that
depended on it. Use `SYSE.10` to qualify the evidence. The authorized Agent makes the engineering decision and any
required release permission has its own basis.

##### SYSE.19:4.1.6 - Resolve each decision and carry the result into use

Rebuild the affected reasoning with the qualified returns and retained premises. Check the whole claim,
including the joint conditions in section 4.1.3. Use the dispositions in section 0.1 to state the result:

| Disposition | Engineering consequence |
| --- | --- |
| `preserve` | The same decision remains supported for its declared use, with the current basis identified. |
| `narrow` | Support remains only for a stated subset of units, conditions or time; give the receiver that limit. |
| `reopen` | A premise requires a new decision; state what remains unresolved and what continuation is currently warranted. |
| `supersede` | A new qualified result or decision replaces the old one for the named use and effective conditions. |
| `withdraw reliance` | The old basis is no longer to be used for this claim; identify any separately supported continuation. |
| `blocked` | A named missing fact, capability, access or authority prevents deciding the affected use. |

These dispositions summarize the affected local decision. Establish evidence use through `A.10` and the authority for the
engineering decision separately. Keep an unchanged physical observation, a revised interpretation and a replacement decision
distinguishable. A limit on one engineering use can leave another supported.

Return the sufficient result to the engineer or Agent who must act on it. When continuing work relies on a
restriction, establish how the relevant user receives and applies it; storing a revised report alone does not
make the restriction effective. Use `SYSE.13` for the affected configuration/effectivity relation and `SYSE.14`
for a required engineering release decision. Do not demand those later operations when a compatible reference
repair or direct engineering answer already finishes the question.

When a relied-on source, requirement, configuration, operating condition, evidence qualification or available support
changes, reconsider the inferences it affects. Retain the other qualified results. When more work is needed,
select the action that addresses the changed premise: this may mean repeating a test under its valid Method, changing
the Method, or revising its description.

#### SYSE.19:4.2 - Record the Result

Record only the content needed by the receiving decisions in their existing result. The rows below apply to the branch taken; a harmless reference repair needs no revalidation dossier.

| Result position | Content when needed by this receiving decision |
| --- | --- |
| receiving decision | Engineering decision, any relied-on Work result, current configuration and use, relevant interval, deciding Agent, and action that may change. |
| source comparison | Predecessor and later or replacement epistemes; material claim changes; publication or carrier changes; source-access and identity gaps. |
| direct reliance | Every affected decision or Work result, the source claim on which it depends, and the premise or evidence-use relation that establishes the dependence. |
| affected reach | Actual-use bases and unresolved candidates that affect the conclusion; equivalent irrelevant mentions may share one exclusion reason. Retain discovery coverage and the last action-changing decision. |
| revalidation | For selected revalidation, identify the plan, performer, Method, configuration, conditions, evidence needed, authority, cost and stop. When Work has been performed, identify what was done, under which conditions, and the results returned. |
| decision dispositions | One disposition from section 0.1 for each affected decision, with reason, evidence and interval; next Work only when selected. |
| continuation | Material gaps and historical source/decision references; a receiving Agent or reopen condition when the actual continuation needs one. |

For example, a compact table, linked decision note, model query result, or generated report may present this
episteme. Treat the form as a representation; keep the source claims and direct-reliance relations recoverable.

#### SYSE.19:4.3 - What Changes in Practice

Engineers stop using a source version as a proxy for impact. A source update can matter while the engineered System
stays unchanged because the warranted decision basis changed. A carrier update can leave engineering decisions
usable when claim content and applicability remain compatible.

The bounded impact decision identifies what remains usable, what must be narrowed, reopened, superseded or withdrawn,
and where a specific gap prevents a conclusion. It identifies further Work when that work is warranted. Search and AI-assisted comparison can reduce discovery effort; an Agent with
suitable capability and authority judges materiality and applicability.

### SYSE.19:5 - Worked Case: A Changed Sensor-Calibration MethodDescription

This constructed case supplies its numerical and professional premises explicitly. They illustrate the
reasoning; they are not measurements from a real pump-controller project or a general calibration procedure.

#### SYSE.19:5.1 - Recover the claim and the affected use

A project needs three pump controllers for operation from `-15 °C` to `40 °C`. Its required absolute
temperature error is at most `1.5 °C`. The project's qualified error model bounds total error by the sum of
sensor error and a separately supported `0.4 °C` contribution from the remaining controller path. The bounds
apply to the same condition and quantity; the project has not inferred independence or combined statistical
confidence levels by simple addition.

Supplier edition E2 supports sensor error at most `0.8 °C` for module `TS-2` from `-20 °C` to `50 °C`.
The old reasoning was therefore `0.8 + 0.4 = 1.2 °C`, below the `1.5 °C` requirement. E3 is a confirmed
continuing edition. Its correction retains the `0.8 °C` bound only from `-10 °C` to `50 °C`: the earlier
calibration basis did not justify the lower temperatures. E3 offers Method C3 for obtaining unit-specific
low-temperature evidence. It does not state that every TS-2 has failed below `-10 °C`.

Substitution shows why the cold-start conclusion must reopen. The required `-15 °C` lies outside E3's
ordinary range, so the old `1.2 °C` bound cannot support that use. At `20 °C`, the same bound remains
applicable. Replacing `-20` with `-10` in a test's acceptance condition would not meet the project's
unchanged need to operate at `-15 °C`.

The impact engineer can classify reliance; release authority belongs to the release holder. In this controller
project, source identifiers and claim addresses lead to the thermal model, cold-start procedure and safety
argument. The engineer also checks equivalent temperature and error assumptions in the model inputs, unit
records, test repository and release basis. Those responsible for these sources confirm the search covers
the material controlled for this release question. The inaccessible supplier-internal model falls outside
that coverage and provides no additional assurance.

The thermal model uses the range to admit a cold-start parameter; the test procedure uses it to justify its
sensor reading; the safety argument relies on the resulting error bound. All three depend on the changed
premise. The interface description cites E2 only bibliographically and uses separate electrical-interface
evidence. Its interface decision remains supported. Room-temperature observations also remain observations
under unchanged valid conditions. The dependent cold-start release premise is the last action-changing
receiver in this question; the entire controller documentation is not reopened.

#### SYSE.19:5.2 - Construct and choose the revalidation

Today's eight-hour preparation window serves tomorrow's decision on three cold-capable controllers running the changed package. That package requires IO-B. `S006`–`S010` have the affected configuration. `S005` has IO-B but lacks current calibration evidence and is unavailable for this preparation window. `S001`–`S004` use IO-A and a different sensor with an independently qualified basis. They remain candidates for an order accepting their existing function. If the actual order permits any three cold-capable units, first check whether those existing qualifications already answer it.

The missing result is a current bound for the installed TS-2 units across the required temperature interval.
The engineer compares these continuations:

| Continuation | What it can supply in this case |
| --- | --- |
| Reuse E2's cold-range claim | No supported cold bound after the correction; the old decision cannot be preserved on that basis. |
| Restrict the units to `-10 °C` and above | A possible supported warm use, but it does not supply the three cold-capable units the current project needs. |
| Obtain a new supplier batch qualification | A potentially useful basis, but the supplier's confirmed delivery is five days away. It cannot answer tomorrow's release question. |
| Apply available C3 and the receiving controller check to three units | An obtainable unit-specific answer within the current window, subject to the actual results below. |

C3's qualified profile supplies the temperature points, settling conditions, reference instrument,
calibration operation and an interval allowance. The engineer obtains that profile and confirms its fit to
the installed configuration. C3 returns a conservative sensor bound as the largest observed absolute
residual plus `0.1 °C` reference uncertainty and a justified `0.2 °C` allowance for the covered intervals and
use period. The qualified profile supplies those last two premises. Three measured residuals
alone would not establish them.

The whole selected programme comprises one hour to update the model inputs and receiving check, three hours
for preparation and C3 calibration of `S006`–`S008`, two hours for the configured chamber check, and one hour
to interpret and return the result: seven hours. These are stipulated complete estimates for the named batch,
including setup, with on-site units, a reserved chamber, suitable instruments and available qualified people.
The shared specialist's work is counted in the sequence. The project accepts this
burden to answer its three-unit cold-use question. There is no basis for claiming all five units calibrated.

The updated model uses the returned bound instead of extrapolating E3's ordinary range. The chamber check
exercises the configured controller's cold-start behaviour and checks that the model's receiving conditions
hold; it is not a substitute for C3's sensor qualification. If C3 or its interval justification were
unavailable, repeating the old chamber test would leave the missing premise unresolved.

#### SYSE.19:5.3 - Follow the returns through the engineering decision

For the illustrative completed work, the records identify the C3 operations, units, instruments, conditions
and observations. C3's largest absolute residuals are `0.5`, `0.6` and `0.5 °C` respectively. Thus the sensor
bounds are `0.8`, `0.9` and `0.8 °C`; adding the unchanged `0.4 °C` controller contribution gives total bounds
`1.2`, `1.3` and `1.2 °C`. Each is at most `1.5 °C`. The chamber results support the declared configured
cold-start behaviour. The unit-specific conclusions remain limited by C3's covered interval and use period.

The impact decision preserves the independent interface and warm-use conclusions; supersedes the old
cold-range model input and test justification for `S006`–`S008`; and preserves those three units' engineering
eligibility on the new basis. `S009` and `S010` still lack the needed calibration evidence, so their cold-use
release premises remain reopened. The earlier results for `S001`–`S004` remain usable on their different basis.

The impact engineer supplies these unit and condition limits to the authorized release holder through `SYSE.14`.
That holder decides release, with any required permission grounded separately. If a warm-only
restriction is selected for other units, make it effective in their assignments and operating arrangements. Recording
it in the impact report alone does not make it effective.

#### SYSE.19:5.4 - Change a condition without discarding the valid remainder

Before release, a separate correction raises the other controller-path error bound from `0.4` to `0.7 °C`
for the same configuration. The sensor observations and C3 qualifications remain valid. Recompute the whole
bound: for `S006` and `S008` it is `1.5 °C`. For `S007` it is `1.6 °C`, which no longer establishes compliance with the `1.5 °C`
requirement. This outer bound leaves `S007`'s compliance open. Two units qualify for the changed package; the available evidence for these three does not qualify a third. A finding that three cannot be supplied by tomorrow would also have to exclude timely substitution or qualification under the actual order. Recalibrating all sensors would target the wrong changed premise.

The engineer reports that the available bound does not qualify a third unit. Possible responses include qualifying the unit with
adequate existing or new evidence, obtaining a qualified alternative unit, repairing and qualifying the controller contribution,
or asking the holder to change the receiving use. These options depend on what is available. Evidence for two units does
not itself authorize a two-unit deployment. If no supported continuation meets the three-unit need or changes that requirement
in time, the batch remains blocked while the sensor results and the two adequate unit bounds remain usable.

**Carrier-only countercase.** Republishing the same E3 at another URL and with another layout changes no
relied-on meaning, applicability or access. Repairing the reference completes the question; no revalidation
dossier or new engineering decision is needed.

**Unlike case: a withdrawn research result.** A design comparison cites two reviews based on the same withdrawn
experiment. Counting them as independent support does not preserve the decision. Determine what the
remaining premises support. If they leave a decision-relevant gap, identify an observation that could distinguish
the alternatives. Return a specific limitation if neither a qualified model nor a feasible experiment
can supply it. The controller calibration programme does not provide a research-replication Method.

**World-change boundary.** Replacing an actual TS-2 sensor changes the engineered configuration. Use
`SYSE.13` and `SYSE.14` for that change, and retain only the evidence applicable to the replacement.

### SYSE.19:6 - Bias Annotation

A newer official source deserves inspection because its claims or authority may matter. Official status,
publication volume, and academic attention describe the source and discourse. Project use and effectiveness need
evidence about performed engineering Work and outcomes.

Search, dependency graphs, and AI summaries can find candidate uses. Actual reliance still depends on the receiving
claim or decision, and authority remains with the Agent who holds it.

### SYSE.19:7 - Conformance Checklist

- [ ] The predecessor and later or replacement source epistemes are identified.
- [ ] The relation between the sources is established for this comparison: apply `C.2.1` when they are editions of the same episteme, identify a replacement when supported, or state the identity gap.
- [ ] Material claim changes are separated from publication and carrier changes.
- [ ] Every affected use names the source claim, receiving decision or Work result, and direct-reliance relation.
- [ ] A searched frame distinguishes dependent, irrelevant and unresolved uses; equivalent irrelevant mentions can
      be grouped. Actual-use support and coverage justify any no-impact claim. Stop tracing a branch once the changed premise can no longer affect a receiving conclusion.
- [ ] Any selected revalidation Work warrants its complete burden for this use. Its plan identifies the performer, Method, configuration, conditions, evidence
      needed, authority, expected contribution and stop. If Work has been performed, identify the result returned.
- [ ] Where a material claim change affects an engineering argument, its consequences have been examined in that argument. If revalidation is proposed,
      the chosen work can supply the required contribution for its range and whole-use conditions.
- [ ] Surviving observations, revised interpretations and replacement decisions remain distinct; coupled changes
      are considered together when their combined effect can alter the receiving decision.
- [ ] The impact decision has its own grounds. Keep any claims about performed Work, evidence, permission, assurance and a release decision distinct, and identify the grounds for each claim the
      receiver relies on.
- [ ] Historical source editions and decisions remain recoverable for their original uses and intervals.
- [ ] The receiver gets the sufficient branch result and its material limits. A harmless reference repair or direct
      engineering answer closes without a duplicate record; next Work is included only when selected.

### SYSE.19:8 - Common Failures and Repairs

| Recurring failure | Repair |
| --- | --- |
| A new version triggers a full rerun | Compare claims and trace actual reliance; reopen only action-changing dependent reach. |
| A small text diff is assumed harmless | Ask what a relying engineer may now do or conclude differently. |
| A new file is treated as a new source meaning | Separate source episteme, edition relation, publication, and carrier. |
| A trace link is treated as reliance | Inspect the receiving content and state the direct-reliance relation. |
| No physical change is treated as no impact | Recheck the epistemic basis of engineering decisions. |
| A passing test is treated as the decision | Ground evidence-producing Work, evidence use, decision Work, and authority separately. |
| The latest official source wins automatically | Compare applicability and evidence for the named use. |
| `Pending review` hides the blocker | Name the missing source, claim content, applicability fact, evidence, capability, or authority. |

### SYSE.19:9 - Consequences

Source refresh becomes proportional. Decisions remain stable when their premises remain compatible, while one
material claim can reopen a release even if the engineered System is unchanged. Historical sources and decisions
remain inspectable, and automated discovery can reduce effort while the deciding Agent retains authority.

The work includes identifying source claims and maintaining the links to engineering decisions and Work results that rely on them. If missing
source content or applicability prevents a conclusion, identify the blocked use and continue the branches with adequate grounds. Application DPFs may add source
controls for domains such as regulated products, software supply chains, clinical devices, finance or contracting.

### SYSE.19:10 - Rationale

The pattern separates a changed source claim from a world-side engineering change. A changed episteme can alter the
warranted basis of a decision while the engineered System remains unchanged. Revalidation Work and later
engineering change therefore receive separate identities.

Keep revalidation proportionate by following changed claims only as far as they can alter engineering action.
Reopening whole files is too broad, while comparing isolated words cannot establish engineering meaning or reliance. Preserving source editions, actual uses, performed
checks, and decision dispositions makes the Method replayable with project-local trace sources.

Test what the changed source does to the engineering argument. When the conclusion remains supported, identify
the surviving grounds. When an inference fails, use that failure to determine whether recalculation,
reinterpretation, new evidence, a different solution or a restricted use will answer the receiving question.
Follow the proposed way forward to see whether its contribution is obtainable and sufficient for
the whole decision. This avoids work that cannot close the gap.

`A.10.1` supplies claim comparison, two-way discovery and bounded affected reach. Use it directly for that question.
For an engineering decision, recover the model or assurance argument and determine what the changed premise supports
for its configuration. If an inference fails, derive the revalidation that could restore it and return the qualified
result to its engineering use, including to the release holder when that decision is at issue. In the sensor case,
finding a cold-start dependency alone neither supplies a cold-range bound nor chooses C3.

`SYSE.10:4.1.1` supplies the substantive inference and combination method: work backward from the claim,
follow qualified contributions forward, explain their join and challenge the whole conclusion. Use that
explanation when the engineering inference itself is missing. Here the source difference selects which old
premise to substitute, which observations and arguments survive, and which obtaining way can restore the
particular changed use. The additional contribution is this selective repair and its decision continuation;
source change is not a reason to repeat every assessment under SYSE.10.

A graph or model tool is useful when many interdependent descriptions make manual discovery unreliable or
expensive. It can supply the candidate relations used here. A complete engineering-change framework is
preferable when the work also needs continuing supplier constraints, design alternatives and implementation
coordination. This pattern does not replace that encompassing work; it can supply its changed-source
judgement. For a small compatible source change, the direct reference repair remains sufficient.

The numerical case uses an available, qualified calibration profile. Where the required experiment, model
or operating restriction cannot be supplied, this method exposes the gap and its consequence. It promises a
warranted continuation, which may be a stop; some desired uses may remain unsupported.

### SYSE.19:11 - SoTA and Source Use

When a relied-on source changes, identify which claims, MethodDescriptions, decisions and uses may need revision. Keep source content and edition change, the Agents using it, performed Work and evidence separately recoverable. Revalidate the affected applicability and use under the current FPF distinctions.


| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `C.2.1`, `A.10`, `E.15`, and `G.11` | Episteme and edition identity, claim-bound evidence, affected-use inspection, and bounded refresh. | `E.15` governs FPF pattern editions; this DPF supplies the engineering source-use specialization. |
| [Wu et al. 2025](https://doi.org/10.1016/j.aei.2025.103490) | One landing-gear case demonstrates tool support for heterogeneous model semantics, conflict handling, traceability, and versioning. | Use the case for candidate impact discovery; establish reliance, configuration change, and release authority separately. |
| [Hernández, Moros, and Nicolás 2023](https://doi.org/10.1007/s00766-023-00396-w) | A multivocal mapping reports requirements Work continuing through DevOps with changing descriptions and monitoring. | The software-heavy review supports this recurring source-change problem, not a universal requirement or revalidation Method. |
| [Norheim et al. 2024](https://doi.org/10.1017/dsj.2024.8) | Analysis of LLM use in requirements Work exposes source, consistency, verification, and cyber-physical limits. | Use generated summaries for candidate discovery; ground engineering evidence and decisions separately. |
| [Kosenkov et al. 2025](https://doi.org/10.1016/j.infsof.2024.107622) | Regulatory-compliance research connects legal interpretation, engineering descriptions, evidence, and change Work. | The mapping study supplies candidate relations; the applicable legal interpretation and permission need their own authority. |
| [Bantwal and Fatahi Valilai 2026](https://doi.org/10.1007/s00170-025-17175-2) | A brake-caliper case exposes change propagation across physical parts, descriptions, supply constraints, engineering tools, and validation. | Use its links as candidate affected reach; inspect actual reliance before reopening a decision. |

When a source, Method or practice is described as current, state the grounds and what kind of claim they support. Academic attention, institutional
promotion, a supplier's `latest` label and public reporting indicate communication or publication status. Distinguish direct observations from
qualified expert estimates when making claims about enacted engineering practice, its prevalence or its effectiveness.

For a developed engineering-change comparison, Bantwal and Fatahi Valilai (§§3–4) connect incoming constraints,
propagation analysis, design alternatives and validation. This pattern retains that need to follow the result
through the whole use; it specializes the earlier question of which source-dependent inference needs repair.
The paper's part-dependency weights do not establish how strongly an epistemic claim supports a decision.

The [2026 ProReFiCIA revision by Etezadi et al.](https://arxiv.org/html/2511.00262v6) (§§3, 4.7–4.9) combines
LLM discovery with reconsideration of unselected requirements and filtering. It offers a concrete scalable
discovery alternative to a single similarity search. Its evaluated filtering still loses relevant items.
Use its candidate output with the actual-use and coverage judgement above; a low-ranked or unreturned item
is not thereby established unaffected. Transfer to another corpus requires its own fitness judgement.

Reconsider the chosen discovery or revalidation arrangement when a new technique changes attainable coverage,
professional support or whole burden for this engineering use. Publication date and reported benchmark
performance do not alone establish that change.

### SYSE.19:12 - Relations

- `C.2.1` governs source-episteme identity and edition continuity. `E.17` and `E.24.PUB` govern publication forms,
  carriers, audiences, and availability.
- `A.10` governs claim-bound evidence, `B.3` assurance, and `C.11` the later choice. `A.10.1` supplies needed multi-use
  discovery and branch-scoped completion. `C.11.DUA` selects further inquiry by attainable contribution and full
  burden. This pattern retains the engineering subject judgment and its direct receiving use.
- `E.15` applies when an FPF pattern edition changes. `G.11` supplies only its declared Part-G refresh results.
- A compatible `SYSE.7` result can supply a MethodDescription or representation use for the named claim. A
  compatible `SYSE.10` result can supply evidence for the same engineering claim, configuration, decision, and
  evidence interval.
- `SYSE.19` supplies the source-change judgement to `SYSE.14` when a release decision depends on it. The Agent with release authority decides whether, and for
  which use and conditions, to release or withhold the change.
- `SYSE.13` and `SYSE.14` govern configuration and world-side engineering change. An episteme edition relation is
  used only as source-change input.
- Application profiles may specialize this Method for domains such as software supply chains, electrical parts,
  regulated products, medical devices, ships, or buildings. A specialization adds an action-changing source or
  revalidation distinction.

### SYSE.19:End
