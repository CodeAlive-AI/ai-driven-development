## C.25 - Q-Bundle: Authoring "-ilities" as Structured Quality Bundles

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Quality-bundle normal form.

**Builds on.**
`C.2.1` for the enclosing quality-claim episteme, `A.2.6` for scope algebra, `A.6.1` for operation-declaration references when current, and `C.16` / `A.18` for Characteristic and Scale legality.
**Coordinates with.**
`C.17-C.19` for quality-related measurement families, `C.16.P` when characteristic/scale/score wording is not yet recoverable, `A.15` for method, work-plan, or work-occurrence gating, and `C.16.Q` for quality/evaluative-characterization wording before the endpoint is one explicit characteristic, Q-Bundle-shaped claim content, objective, or another governing pattern.

**Use this pattern when.** Use C.25 when a familiar quality family such as availability, resilience, security, or maintainability may be hiding several differently typed contributors and the reader needs one claim that keeps them distinct.

**First useful move.** Ask: *what would make this quality claim false?* If one measure on one declared Scale answers the question, state that one Characteristic and stop. Use Q-Bundle-shaped claim content only when several differently typed contributors—such as a measure and scope, or measures plus a load-bearing window or mechanism—jointly determine the answer.

**First result.** Write one readable quality claim about one exact bearer and include only the contributors on which its truth or the next receiving action depends. An optional slot is omitted unless changing that slot could change the current claim or receiving action.

**Nearest non-use.** Stay with the direct Characteristic pattern when one measure and Scale carry the claim. Use the direct scope, measurement, evidence, assurance, gate, publication, viability-envelope, or temporal pattern when that neighboring question—not quality-family decomposition—is the current work.

### C.25:1 - Problem frame

Engineering quality language repeatedly drifts into one of two invalid simplifications: either every `-ility` is treated as one scalar characteristic, or every engineering-quality statement is left as loose evaluative prose. A conforming engineering corpus therefore needs a uniform discipline that keeps admissible measurements, scope declarations, mechanisms, statuses, and evidence visibly separated without inventing a new kernel ontology.

### C.25:2 - Problem

Without a normal form for engineering quality families:

1. **Composite families are scalarized illegally.**
   Terms such as *resilience*, *security*, or *maintainability* are treated as if one number exhausted them.
2. **Scope is confused with measurement.**
   A claim's `ClaimScope` / `WorkScope` is spoken of as if it were a magnitude rather than a USM set-valued applicability object.
3. **Mechanism and status are mistaken for evidence or metrics.**
   Presence of redundancy, certification, or audit controls is described as if it were itself a measurement value.
4. **Guards become unstable.**
   Admission checks silently mix scope coverage, numerical thresholds, mechanism presence, and evidence freshness in one phrase.
5. **Evaluative governing-pattern selection remains underspecified.**
   After `C.16.Q` repairs a bare quality term, or `C.16.P` repairs characteristic, scale, score, metric, or proxy wording inside that term, the admissible endpoint is unclear unless FPF distinguishes single-CHR cases from bundle-shaped quality families.

### C.25:3 - Forces

| Force | Tension |
|---|---|
| **Simplicity vs category hygiene** | Authors want one convenient quality label; the framework must still keep CHR, USM, mechanism, status values, and status-use relations distinct. |
| **Comparability vs local applicability** | Measures should compare legally across contexts, while scope remains context-local and set-valued. |
| **Thin ontology vs practical authoring** | The pattern should regularize quality authoring without creating a new heavy kernel family for every `-ility`. |
| **Endpoint clarity vs expressive breadth** | Some quality terms really are one characteristic; others are bundles. The endpoint rule must cover both without ambiguity. |

### C.25:4 - Solution - Q-Bundle normal form

`C.25` defines a lightweight normal form for the claim content of engineering quality families. A publisher facing a quality term first decides whether one claim episteme should state:

- **one admissible CHR characteristic**, or
- **one structured quality bundle** whose measurable slots, scope slots, mechanisms, statuses, and evidence remain explicit.

#### C.25:4.1 - Endpoint split

Use the **single-characteristic branch** when one exact `U.Characteristic`, one declared Scale, and the ordinary CHR laws carry the quality claim. The claim-bearing result is still one `C.2.1` episteme about its exact bearer; C.25 adds no bundle record.

Use the **Q-Bundle branch** when several differently typed contributors are part of one quality claim. The result is one `C.2.1` episteme whose ClaimGraph contains the record-shaped Q-Bundle content below.

#### C.25:4.2 - Q-Bundle shape and identity boundary

The full escalation form is:

`Q-Bundle := <Name, QualityBearer, ClaimScope?, WorkScope?, Measures[CHR], QualificationWindow?, Mechanisms?, Status?, Evidence?>`

`Q-Bundle` names a C.25-local record-shaped part of one exact `U.ClaimGraph`. It is not a new Kernel kind, an independently identified world object, or a second identity beside the enclosing episteme. That episteme supplies the exact claim content, one independently identified `QualityBearer` as its EntityOfConcern, and the effective `U.ReferenceScheme` under which the quality claim is read.

The `?` is operative: omit any optional slot unless changing it could change the current claim or receiving action. A bundle may therefore contain only Name, QualityBearer, Measures, and one load-bearing scope or window. The full tuple is an escalation aid, not a form every author must fill.

Changing any bundle content that changes the quality claim changes the ClaimGraph and therefore identifies another episteme under `C.2.1`. A changed layout, form, publication occurrence, or carrier can leave that episteme unchanged. A gate, publication, proxy, comparison, or roll-up cites the exact episteme or one exact `C.2.1 ClaimAddress`, meaning the exact edition plus an intrinsic claim identity declared by that edition's ClaimGraph. Later `ClaimAddress` uses in C.25 mean that same value; a field list or raw record reference is not enough.

#### C.25:4.3 - Field meanings

- **Name.** The engineering quality family label inside the claim content, such as `Availability`, `Resilience`, or `Security`; it is not an identity key.
- **QualityBearer.** The one independently identified EntityOfConcern of the enclosing claim episteme. It may be an exact `U.System`, `U.PromiseContent`, `U.Episteme`, or another exact entity under its direct identity pattern. When selected organization is the subject, use one `A.22` `U.Structure` with exact constituents, selected obtaining relations, applied constraints, and one selection-use frame. A list of local system-role kinds and assignment occurrences does not by itself identify a bearer.
- **ClaimScope / WorkScope.** USM sets over `U.ContextSlice` describing where the claim holds or where the capability's deliverability claim may be evaluated. These are **set-valued scope objects**, not characteristics.
- **Measures[CHR].** One or more admissible CHR characteristics, each bound to one declared scale.
- **QualificationWindow.** The temporal policy under which the quality claim is judged.
- **Mechanisms / Status.** References to realizations of operation families declared in `U.Mechanism` epistemes, control presences, certification states, or other named gating prerequisites. They are not measurements.
- **Evidence.** Anchors that justify the measures, mechanisms, or scope claims.

#### C.25:4.4 - Guard reading

A quality guard is conjunctive only over the truth conditions that the current claim actually declares. For example:

`declared scope covers TargetSlice AND declared measures satisfy their own laws AND each other declared prerequisite holds`

An absent optional slot contributes no condition. Each measure keeps its own Scale and comparison law; a trade-off, alternative, weighted combination, or partial order must be stated under the pattern that defines it rather than being smuggled into `AND`. If this typed decomposition cannot express what makes the claim true, do not force the family into C.25.

### C.25:5 - Archetypal Grounding

**Tell.** A quality family is not automatically one metric. Use one Characteristic when one measure and Scale carry the claim; use a Q-Bundle only when several differently typed contributors are jointly load-bearing.

**Minimal completed availability case.** Under `ServiceQualityScheme-v4`, the claim says: *CheckoutAPI maintained at least 99.9% availability for customer-facing request handling over the rolling 30-day window.* Its exact bearer is the independently identified `CheckoutAPI` System. Its Q-Bundle content has `Name: Availability`, `ClaimScope: customer-facing request handling`, `Measures: AvailabilityRatio[%] >= 99.9`, and `QualificationWindow: rolling 30 days`. `WorkScope`, `Mechanisms`, `Status`, and `Evidence` are omitted because this drafting use does not rely on them. If evidence reliance, a failover prerequisite, or a gate later becomes current, add only the direct relation or slot that question needs.

**Escalation examples.** A resilience or security claim often needs several measures, scenario or attack-class scope, mechanisms or control statuses, and a qualification window. Those contributors belong in the bundle only when they are part of that claim's truth conditions; treating the family as one scalar score would erase which contributor failed.

### C.25:6 - Bias-Annotation

The pattern biases authors toward explicit decomposition. That bias is intentional. It is better to publish a visibly structured quality bundle than to gain short-term convenience by collapsing scope, measures, and mechanisms into one overloaded quality label.

### C.25:7 - Conformance Checklist

- `CC-C.25-1` If an engineering quality claim is intended as one measurement characteristic, the publisher **SHALL** bind it to one named `U.Characteristic` with one declared scale.
- `CC-C.25-2` If the claim requires multiple measures, scope slots, mechanism slots, status slots, or qualification windows, the publisher **SHALL** use Q-Bundle-shaped ClaimGraph content rather than an undeclared scalar surrogate.
- `CC-C.25-3` `ClaimScope` and `WorkScope` **SHALL** remain USM set-valued scope objects; they **MUST NOT** be treated as ordinal or numeric quality levels.
- `CC-C.25-4` Mechanism or status slots **MUST NOT** be conflated with `Measures[CHR]`.
- `CC-C.25-5` Any scalar comparison or thresholding inside a Q-Bundle **SHALL** apply only to declared CHR measures, not to scope slots.
- `CC-C.25-6` When cross-context comparison is current, the publisher **SHALL** align the exact bundle heads or slots, resolve the two exact `F.17` local senses, and, when their `<ReferenceScheme, LocalSenseClaim>` projections differ and the comparison needs semantic correspondence, test the direct `F.9` Bridge predicate and state a separate bounded-use claim only if that Bridge obtains. The comparison and its reliance **MUST NOT** change any Q-Bundle slot; ordinary reliance uses `A.10`, while `B.3` opens only when an actual named assurance claim is current.
- `CC-C.25-7` A materialized Q-Bundle **SHALL** be recoverable as content of one exact `C.2.1` episteme with one independently identified QualityBearer as EntityOfConcern and one effective ReferenceScheme. A gate, publication, comparison, proxy, or roll-up **MUST NOT** cite a field list as though it were an independently identified bundle object.

### C.25:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **One-number `-ility`** | `Resilience = 82` with no declaration of what is being measured and what scope/scenario is intended. | `CC-C.25-2` requires a Q-Bundle when the family is composite. |
| **Scope as metric** | The claim treats wider applicability as a higher quality value rather than as a larger USM set. | `CC-C.25-3` keeps scope set-valued and non-CHR. |
| **Mechanism equals quality** | Presence of a mechanism or certificate is reported as if it were the measurement itself. | `CC-C.25-4` keeps mechanism/status slots distinct from measures. |
| **Collapsed guard prose** | One sentence mixes coverage, thresholds, windows, and mechanisms without typed separation. | `C.25` rewrites the claim into explicit slots and typed guard factors. |

### C.25:9 - Consequences

| Benefit | Trade-off / Mitigation |
|---|---|
| **Category hygiene.** Scope, measurement, mechanism, and status no longer collapse into one term. | Slightly heavier authoring structure; mitigation: only composite cases need a bundle, and immaterial optional slots remain absent. |
| **Portable comparison.** CHR measures compare legally, while scope remains governed by USM set algebra. | Authors must declare scales and scope explicitly. |
| **Cleaner gating.** Method/work guards can read the same structure without hidden semantics. | Requires discipline in separating guard factors. |
| **Better endpoint classification.** `C.16.Q` can terminate in either one characteristic or one Q-Bundle with a clear endpoint pattern. | Requires a first-pass endpoint decision during authoring. |

### C.25:10 - Rationale

Engineering quality language is useful precisely because it groups recurring concerns under memorable family labels. The same grouping becomes dangerous when those labels are mistaken for one universal metric. `C.25` preserves the family labels but forces the underlying structure to stay typed and visible.

### C.25:11 - SoTA-Echoing

The comparison below selects lines by the quality-family problem they can solve, not by publication popularity or by the availability of a convenient form.

| Current problem-solving line | What it solves well | Remaining limit or effort cost | C.25 disposition |
| --- | --- | --- | --- |
| [ISO/IEC 25010:2023 product quality model](https://www.iso.org/standard/78176.html) | Provides a current reference model of nine product-quality characteristics and their subcharacteristics for specification, measurement, evaluation, and acceptance criteria. It prevents one undifferentiated word *quality* from doing all the work. | Its reference taxonomy does not identify one local claim episteme, its exact bearer, use-bounded scope, window, mechanism prerequisite, or evidence reliance. A domain may also need qualities outside its ICT-product boundary. | Adopt characteristic decomposition and explicit measures; do not import the taxonomy as a universal bundle schema or bearer identity. |
| [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) and [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) | Couples an indicator and objective to an explicit time window, error budget, stakeholder decision, and actionable response; multiwindow and multi-burn-rate alerts expose the precision/recall and management trade-off. | It is a mature service-reliability line, not a general ontology of resilience, security, maintainability, or assurance. It assumes measurement and operational-policy work whose cost is justified only for the receiving use. | Adapt the explicit measure/window/action boundary and the rule that engineering effort should match the decision; do not make an SLO or error budget mandatory for every quality family. |
| [NIST SP 800-160 Vol. 2 Rev. 1, *Developing Cyber-Resilient Systems*](https://doi.org/10.6028/NIST.SP.800-160v2r1) | Treats cyber resilience through distinct goals, objectives, techniques, approaches, and design principles for anticipating, withstanding, recovering from, and adapting to adverse conditions. It keeps resilience from becoming one score. | The line is security-specific and intentionally broad; applying its life-cycle and risk constructs can be expensive. It does not provide one lightweight local claim identity or universal aggregation law. | Adopt the separation of scenario, measures, mechanisms, and outcomes when they are load-bearing; reject a universal resilience scalar and do not copy the full handbook into a Q-Bundle. |
| [OMG SACM 2.3](https://www.omg.org/spec/SACM/2.3) | Separates structured claims, argument links, artifact references, counter-evidence, and interchange packages, making an assurance case inspectable across tools. | A complete assurance case and its interchange structure can be much heavier than an ordinary quality claim. SACM does not decide which quality contributors make the claim true or whether one bundle guard is admissible. | Keep quality claim content distinct from evidence and assurance. Open `A.10` or `B.3` only on their own trigger instead of embedding an assurance case in C.25. |

**FPF-local synthesis.** C.25 combines only the non-dominated moves needed before a direct domain pattern takes over: one exact bearer; a single-Characteristic exit; otherwise a typed separation of load-bearing measures, scopes, windows, mechanisms, statuses, and evidence references; and a guard over only the conditions the claim actually states. The tuple and this conditional guard are FPF synthesis, not a claim that contemporary practice already shares one universal Q-Bundle.

**Defeating and reopen conditions.** Prefer a direct domain pattern when it already supplies a clearer composite-quality identity, aggregation law, and practitioner route. Reopen C.25 when a useful quality claim cannot be stated through the available typed contributors without inventing filler, when a non-conjunctive trade-off or dependency cannot be named under its direct pattern, when the record costs more than the receiving decision warrants, or when a proxy repeatedly becomes the decision object despite the source claims remaining load-bearing.

### C.25:12 - Relations

`E.21` specialises Q-Bundle-shaped claim content for FPF pattern-quality claims. `C.25` remains the general endpoint pattern for engineering quality families; `E.21` governs the claim when its exact EntityOfConcern is one FPF pattern version evaluated as action-guiding FPF text.

**C.27 temporal-claim relation.**

- C.27 may flag: a quality-family statement where agility, resilience, adaptability, recovery, or robustness depends on braking, redirection, stabilization, recovery rate, or rhythm under effort.
- This pattern keeps: quality-family bundle structure, scope, mechanism/status slots, evidence, qualification window, and failure mode.
- Non-admissible use: temporal adequacy alone does not establish quality adequacy; speed, recovery, or rhythm becomes quality content only when it contributes to a declared quality-family claim. Include scope, mechanism/status slots, evidence, and failure mode only when the claim or receiving action depends on them.
- Coordinate with C.27 only when a temporal claim is being used to change action; do not make every quality bundle carry dynamic slots.

- **Builds on:** `A.2.6` for scope algebra, `A.6.1` for operation-declaration references when current, and `C.16 / A.18` for CHR legality.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `A.10` for ordinary reliance on a bounded cross-context use, `B.3` only when an actual named assurance claim is current, `A.15` for gate use, `C.16.P` for unresolved characteristic, scale, score, metric, or proxy wording inside a quality-family statement, `C.16.Q` for overloaded quality or evaluative-characterization wording, `C.33`, `C.34`, and `C.35` when captured structure, lost structure, preservation, or generated-result adequacy becomes part of a composite architecture quality family, `C.17`, `C.18`, and `C.19` for adjacent quality-family measures, and `F.9` when bundle comparison needs semantic correspondence between local senses with different interpretation bases, or `F.9.1` when Bridge stance annotation is required.
- **Constrains:** engineering quality authoring whenever a quality term would otherwise drift between single-CHR and composite-bundle readings.

#### C.25:12.1 - Endpoint function in evaluative classification

In evaluative repair, `C.25` is the endpoint pattern for engineering quality families after overloaded quality wording has been repaired by `C.16.Q` and any hidden characteristic, scale, score, metric, or proxy wording has been repaired by `C.16.P`. `qualityTermAscription(...)` may remain a transitional repair record, but it is **not** the universal resting place when the admissible result is a claim about one `Characteristic`, one episteme with Q-Bundle-shaped claim content, or an explicit objective-oriented quality claim under its own endpoint pattern.

### C.25:13 - Decision Test: Single Characteristic or Bundle?

The most common authoring failure is not in the bundle syntax itself; it is in choosing the wrong endpoint shape. The quickest useful test is to ask what would make the quality claim false.

#### C.25:13.1 - Use one `U.Characteristic` when

A quality claim should terminate in one admissible CHR characteristic only when all of the following hold together:

- one measurable aspect is actually doing the evaluative work,
- one declared scale is enough to compare relevant cases,
- the bearer and scope are already clear without introducing extra quality slots,
- mechanism or status presence is not itself part of the core quality head,
- and downstream gates can read the claim without needing a bundle decomposition.

Examples include a narrowly declared `AvailabilityRatio[%]`, a specific latency percentile, or one response-time threshold under one fixed window.

#### C.25:13.2 - Use a `Q-Bundle` when

A quality claim belongs in `C.25` when one family label is standing over several distinct typed concerns, for example:

- several measures are needed together,
- scenario or claim scope is load-bearing,
- mechanism presence or certification state constrains admissibility,
- qualification windows alter the reading materially,
- or one scalar head would hide which part of the family is actually failing.

The bundle is the explicit authoring form for claims whose truth conditions are already composite.

#### C.25:13.3 - Borderline cases

Some quality families contain both a bundle-shaped form and a narrow single-characteristic form. For example, a service team may use:

- one CHR characteristic for a very narrow uptime commitment, and
- one Q-Bundle for the broader service-availability family that includes scope, windows, failover mechanisms, and evidence.

This is legitimate as long as the text states clearly which head is currently in play. The single-characteristic form does not replace the broader family; it selects one evaluative slice of it.

### C.25:14 - Slot Interaction Law

The practical payoff of `C.25` is not just that it names the slots. It also stabilizes how those slots interact.

#### C.25:14.1 - Scope and measure remain orthogonal

`ClaimScope` answers **where** or **under what contextual slice** the quality claim holds; `WorkScope` answers where the capability's deliverability claim may be evaluated. `Measures[CHR]` answer **how** a measurable aspect behaves. A broader scope is not a larger measurement value; a narrower scope is not a penalty value. Scope is governed by set inclusion and coverage, not by scalar order.

#### C.25:14.2 - Mechanism and status are gating slots

Mechanisms and statuses may be load-bearing for admissibility, but they do not become measurements merely because they matter. A redundancy mechanism may be required for claiming a resilience bundle, and a certification status may be required for external publication, yet neither slot is itself the `Measures[CHR]` head.

This matters because many quality arguments fail by turning mechanism presence into an implicit hidden score.

#### C.25:14.3 - Qualification windows are not decorative

A quality claim that depends on rolling windows, observation periods, maintenance intervals, or disruption horizons must publish that temporal qualifier explicitly. If the truth of the quality claim changes when the window changes, then the window is part of the declared bundle record rather than optional commentary.

#### C.25:14.4 - Report-only summary proxies

A publisher may compute a report-only summary proxy for convenience, for example a compact quality summary value or an oversight-facing composite score. State in claim content which exact Q-Bundle slots the proxy summarizes and what it leaves out. The proxy may be another Characteristic or claim under its direct pattern, but it does not replace the source quality-claim episteme or its addressed claims in a norm, gate, comparison, or cross-context use.

### C.25:15 - Worked Quality Families

#### C.25:15.1 - Availability family

A narrow service commitment may use `AvailabilityRatio[%]` as one characteristic. A broader availability family usually still needs a bundle because the claim depends on:

- declared service and time scope,
- observation and qualification window,
- one or more mechanism slots such as failover or redundancy,
- and evidence tying the measurement to declared observation conditions.

The bundle form makes it possible to distinguish "the measurement fell short" from "the measurement is fine but the declared mechanism prerequisite was absent".

#### C.25:15.2 - Resilience family

Resilience is almost never one scalar. It commonly binds together:

- disruption scenario scope,
- restoration-related measures such as `MTTR`, `RTO`, or `RPO`,
- recovery mechanisms and preparedness states,
- and scenario-specific evidence about drills, restorations, or incident traces.

Trying to compress this into a single resilience value usually destroys the difference between fast recovery in one scenario and structural fragility in another.

#### C.25:15.3 - Security family

Security claims routinely combine:

- trust-zone or attack-class scope,
- measurable characteristics such as patch latency, control coverage, or response interval,
- control-set and certification slots,
- and evidence from audit, observation, or incident review.

`C.25` therefore treats broad security-family claims as bundle-shaped unless the claim has already been narrowed to one admissible CHR characteristic.

#### C.25:15.4 - Maintainability and evolvability

Maintainability or evolvability claims often drift into pure rhetoric. In `C.25`, they become usable only when the publisher separates:

- the declared scope of systems or change classes,
- the measurable slots (for example change lead time, defect reintroduction rate, restoration interval, review load),
- the enabling mechanisms (modularity rules, test harnesses, interface discipline),
- and the window or evidence conditions under which those measures were observed.

This is exactly the kind of quality family that looks scalar in speech but turns composite once the claim is made explicit.

### C.25:16 - Authoring and Review Guidance

#### C.25:16.1 - For authors

Begin with *what would make this claim false?* Then:

1. identify the exact bearer and the quality-family label used in the claim;
2. if one measure on one declared Scale carries the claim, state that Characteristic and stop;
3. otherwise add only the differently typed contributors that jointly carry the claim;
4. omit scope, window, mechanisms, status, or evidence when changing that slot would change neither the claim nor the receiving action;
5. identify the enclosing C.2.1 episteme through its claim content, bearer, and effective ReferenceScheme; and
6. add a proxy, gate, publication, evidence relation, or assurance result only when its own receiving question is current.

The schema remains available for a demanding case; it is not the authoring order for every bundle.

#### C.25:16.2 - For assessors

A checking reader should ask:

- whether the chosen endpoint shape is admissible,
- whether any scope slot has been smuggled into scalar language,
- whether mechanism presence has been mistaken for a metric,
- whether the window is truly optional or actually load-bearing,
- and whether any summary proxy is trying to replace the underlying bundle.

In practice, most defects are visible as soon as the checking reader asks what exactly one reported number stands for.

#### C.25:16.3 - For gate designers and assurance leads

Resist a guard such as *resilience must be high*. Cite the exact quality-claim episteme or addressed claim and name only the slots the decision actually uses—for example one scope, one measure threshold, a load-bearing window, or a required mechanism. Do not require an absent slot merely because the source claim uses Q-Bundle-shaped content.

### C.25:17 - Repair and Boundary Notes

#### C.25:17.1 - Repair from bare quality requirement prose

Bare phrases such as *quality requirement*, *security requirement*, or *availability requirement* should not survive as bare heads when the underlying endpoint is actually a characteristic or bundle. The repair rule is:

- choose the endpoint shape first,
- then bind the requirement or commitment to that explicit head.

`C.16.Q` may still be the entry repair for overloaded quality wording, and `C.16.P` may repair characteristic, scale, score, metric, or proxy wording inside the same statement; `C.25` is the resting place only after the engineering quality family has been made explicit.

#### C.25:17.2 - Boundary to cross-context use and reliance

Cross-context comparison does not change whether the endpoint is one characteristic or one bundle and does not modify any bundle slot. Align the exact bundle heads or slots and resolve their exact `F.17` local senses. Test the direct `F.9` predicate when their `<ReferenceScheme, LocalSenseClaim>` projections differ and the comparison needs semantic correspondence. If a Bridge obtains, state the proposed direction, correspondence rule, tolerated loss, and polarity in a separate bounded-use claim. Observed loss remains evidence; permitted loss remains that claim's tolerance. Use `A.10` for ordinary bounded reliance and open `B.3` only when an actual named assurance claim is current.

#### C.25:17.3 - Boundary to publication convenience

A report, summary publication, or executive summary may express only one slice of the selected quality-claim episteme. Keep the selected episteme and any exact `ClaimAddress` distinct from its publication occurrence, form, and carrier under `E.24.PUB`. A coarser form does not collapse the source claim content, while changed Q-Bundle claim content identifies another episteme even when the file or layout stays the same.

#### C.25:17.4 - Serviceability and supportability

Serviceability, supportability, and adjacent family labels often look simple in prose but become composite as soon as operational use is declared. An admissible bundle for this family may need:

- support-scope slices,
- measured restoration or service intervals,
- mechanism slots for support mechanisms, access discipline, or replacement procedures,
- and evidence from service traces or support records.

The lesson is the same as elsewhere in `C.25`: once the truth of the family claim depends on several typed contributors, the bundle should stay explicit.

#### C.25:17.5 - Boundary to description-side and selector-side evaluation

`C.25` is for engineering quality families whose bearer is a system-side, promise-side, or explicit quality-bearing artifact. It does **not** automatically cover:

- viewpoint-fit or grounded architecture adequacy claims, which may belong in viewpoint or evaluative-ascription patterns,
- or selector/objective heads where *quality* means use-value under a search or portfolio frame.

This boundary matters because the same word *quality* appears across those zones. `C.16.Q` repairs overloaded quality wording, `C.16.P` repairs characteristic, scale, score, metric, or proxy wording when that is the hidden object, and the resting endpoint depends on what is actually being evaluated.

### C.25:18 - Bundle Decomposition and Comparison Law

#### C.25:18.1 - Local decomposition rule
A family label may remain stable while its internal slots differ materially across contexts. Conforming comparison therefore starts by aligning the bundle decomposition: scope slots with scope slots, measure slots with measure slots, mechanism/status slots with their own kinds, and evidence/window slots with their own kinds. Comparing one bundle's measure directly to another bundle's mechanism claim is a category error even if both sit under the same family label.

#### C.25:18.2 - Narrow slice versus whole family
A publication may expose one narrow Characteristic claim from a broader Q-Bundle-shaped claim episteme, but it must identify that addressed claim as only one contributor to the broader family. It must not cite the slice as though it exhausted or reidentified the source episteme.

#### C.25:18.3 - Cross-context family comparison
Cross-context comparison of quality families starts with explicit bundle alignment: compare scope with scope, measures with corresponding measures, mechanisms or statuses with their own kinds, and windows or evidence only when the receiving comparison uses them. For each semantic correspondence the comparison needs, resolve the two exact `F.17` senses and test the direct `F.9` predicate only when their `<ReferenceScheme, LocalSenseClaim>` projections differ. Cite a Bridge only when it obtains, then state the proposed use separately with its direction, correspondence rule, tolerated loss, and polarity. Keep observed loss in evidence, use `A.10` for ordinary reliance, and open `B.3` only on its own assurance trigger. None of this changes the Q-Bundle or supplies an automatic penalty.

### C.25:19 - Gate, Proxy, and Reporting Discipline

#### C.25:19.1 - Report-only summary proxy
A summary proxy remains a separate downstream claim. It identifies the source quality-claim episteme or exact `ClaimAddress`, states what it summarizes and omits, and never replaces that source in a norm, gate, or endpoint classification.

#### C.25:19.2 - Gate binding rule
When a gate uses a quality family, its decision claim cites the exact quality-claim episteme or addressed claims and names only the bundle slots on which the decision relies: for example declared scope, specific measures, a qualification window, or required mechanisms or statuses. The gate does not bind to a family label or raw record, and `C.25` does not define the gate decision.

#### C.25:19.3 - Roll-up caution
A roll-up is another claim-bearing episteme. It cites the exact source epistemes or ClaimAddresses being combined, states the admissible aggregation or summary rule, and remains distinct from them. If the roll-up begins to drive local engineering action directly, reopen the source claims and the exact Q-Bundle slots on which that action relies instead of treating the summary score as the bearer or bundle.

### C.25:20 - Review Matrix and Repair Tests

A checking reader can test a Q-Bundle with five questions:

1. **Is the endpoint shape admissible?** One characteristic where one characteristic is live, one bundle where several typed contributors are load-bearing.
2. **Are scope and mechanism slots kept distinct from measures?**
3. **Is any summary number trying to replace the bundle?**
4. **Would a gate still be auditable if the family label were removed?**
5. **If comparison needs cross-context semantic correspondence, is the `F.9` Bridge predicate tested separately from the family bundle?**

Repair from bare family prose should therefore recover the endpoint shape first, then choose whether any narrow slice deserves a separate CHR publication.

### C.25:20a - Viability-envelope, quantum-like, and temporal-claim relation note

Use `C.25` for the quality-family decomposition needed by a quality claim, proxy metric, trade-off, gate, or report. A viability claim should not become quantum-like merely because it involves uncertainty, feedback, several qualities, or changing operating conditions; a temporal claim should not become a Q-Bundle merely because the working phrase mentions speed, cadence, rhythm, or recovery.

Practical reading:

1. Decide whether one Characteristic answers the quality question; if it does, stop there.
2. If several differently typed contributors are load-bearing, identify the bearer and include only those measures, scopes, windows, mechanisms, statuses, or evidence anchors.
3. If one proxy or this proportional bundle answers the receiving question, stay in `C.25`.
4. Open `C.26.3` only when several characteristics must remain inside a viable region under disturbance and a candidate intervention, boundary condition, adaptation cost, or failure mode matters.
5. Open `C.27` only when a temporal claim is being used to change action—for example, when rate-change, effort, window, resistance, recovery, or cadence changes that action.
Minimum viability-envelope note:

| Field | Required content |
| --- | --- |
| Bearer | One exact `U.System` under A.1 when that System is the subject; or one exact `A.22` `U.Structure` when selected organization is the subject, with independently identified constituents, selected obtaining relations, applied constraints, and one selection-use frame. A service label, team label, or list of system-role kinds and assignment occurrences does not identify the bearer by itself. |
| Protected promise / function | The promise, function, use, operating regime, or stakeholder value the envelope protects |
| Variables | Which qualities, constraints, resources, risks, or state descriptors define the envelope |
| Viable region / bounds | What counts as inside, near edge, degraded, or outside the envelope for this use |
| Disturbance class | What perturbation, demand shift, environment change, probe, or boundary condition stresses the envelope |
| Actuators | Which proposed work, design move, policy, boundary change, sensor change, or resource change could alter the bearer or its operating conditions; use C.26.3 to recover each candidate intervention's proposal-side object and distinguish any performed work or resulting change claimed to exist |
| Trade-off / loss | What gets worse, hidden, coarsened, delayed, or made more expensive |
| Admissible use | Which action, decision, relation, or triage use the envelope reading can carry |
| Non-admissible use | Which release, audit, assurance, or universal quality claim requiring additional support it does not support |
| Failure mode | What it means to leave the envelope or to mistake one proxy for the envelope |

Useful outputs:

- one `C.2.1` quality-claim episteme with Q-Bundle-shaped content when the issue is quality decomposition;
- a `C.26.3` envelope-regulation note when probes, candidate interventions, or boundary conditions change the admissible viability reading;
- a `C.27` temporal-claim adequacy card when a claim used to change action says that an intervention changes a rate, recovery, or cadence; state its effort, window, and resistance where load-bearing;
- no QL wording when ordinary quality-bundle, proxy, feedback, or control tuning carries the work.

#### C.25:20b - Architecture-decision Q-Bundle boundary

`C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite exact C.25 quality-claim epistemes or ClaimAddresses as architecture-characteristic inputs, accepted-loss structure, guardrail rows, feedback concerns, or adequacy concerns. C.25 keeps their Q-Bundle claim content, bearer, scope, measures, mechanisms, qualification window, and evidence distinct from the problem-to-structure architecturing flow, project architecture decision relation, and ADR-like publication projection.

### C.25:End

