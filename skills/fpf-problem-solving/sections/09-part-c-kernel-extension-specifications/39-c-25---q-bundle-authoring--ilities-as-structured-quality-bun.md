## C.25 - Q-Bundle: Authoring "-ilities" as Structured Quality Bundles

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Quality-bundle normal form.

**Builds on.**
`A.2.6` (USM scope algebra), `A.6.1 U.Mechanism`, `C.16 MM-CHR`, `A.18 CSLC`, `B.3 Trust & Assurance Calculus`.

**Coordinates with.**
`C.17-C.19` for quality-related measurement families, `C.16.P` when characteristic/scale/score wording is not yet recoverable, `A.15` for method, work-plan, or work-occurrence gating, and `C.16.Q` for quality/evaluative-characterization wording before the endpoint is one explicit characteristic, Q-Bundle, objective, or another governing pattern.

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

`C.25` defines a lightweight authoring normal form for engineering quality families. A publisher facing a quality term first decides whether the intended endpoint is:

- **one admissible CHR characteristic**, or
- **one structured quality bundle** whose measurable slots, scope slots, mechanisms, statuses, and evidence remain explicit.

#### C.25:4.1 - Endpoint split

Use a **single `U.Characteristic`** when the quality claim is genuinely one measurable aspect with one declared scale and ordinary CHR legality.

Use a **Q-Bundle** when the quality family depends on more than one of the following:

- one or more measurable characteristics,
- a declared claim/work scope,
- mechanism or status requirements,
- qualification windows,
- evidence anchors that are not reducible to one scalar.

#### C.25:4.2 - Q-Bundle shape

`Q-Bundle := <Name, QualityBearer, ClaimScope?, WorkScope?, Measures[CHR], QualificationWindow?, Mechanisms?, Status?, Evidence?>`

The pattern adds no new Kernel kind for these slots. It reuses existing kinds and keeps them in one disciplined authoring structure.

#### C.25:4.3 - Field meanings

- **Name.** The engineering quality family label, such as `Availability`, `Resilience`, or `Security`.
- **QualityBearer.** The bearer of the quality claim: typically `U.System`, `U.PromiseContent`, or `U.Episteme`.
- **ClaimScope / WorkScope.** USM sets over `U.ContextSlice` describing where the claim holds or where the capability can deliver. These are **set-valued scope objects**, not characteristics.
- **Measures[CHR].** One or more admissible CHR characteristics, each bound to one declared scale.
- **QualificationWindow.** The temporal policy under which the quality claim is judged.
- **Mechanisms / Status.** References to `U.Mechanism` realizations, control presences, certification states, or similar gating structures. They are not measurements.
- **Evidence.** Anchors that justify the measures, mechanisms, or scope claims.

#### C.25:4.4 - Guard reading

A conforming quality guard typically has the conceptual form:

`Scope covers TargetSlice AND Measures meet thresholds AND QualificationWindow is valid AND required Mechanisms/Status are present`

This keeps coverage, thresholding, and admissibility in separate typed slots instead of hiding them inside one quality adjective.

### C.25:5 - Archetypal Grounding

**Tell.** A quality family is not automatically one metric. Sometimes it is one characteristic; often it is a structured bundle whose measurable, scope, and mechanism slots must remain explicit.

**Show (Availability).** Availability may be authored as one CHR-centric bundle with `AvailabilityRatio[%]` as the principal measure, a declared service/time scope, and explicit redundancy mechanisms. The measure is scalar; the scope is not.

**Show (Resilience / Security).** Resilience or security usually requires more than one measure, plus scenario scope, mechanism references, and qualification windows. Treating either as one scalar "quality score" erases the bundle structure that the claim actually needs.

### C.25:6 - Bias-Annotation

The pattern biases authors toward explicit decomposition. That bias is intentional. It is better to publish a visibly structured quality bundle than to gain short-term convenience by collapsing scope, measures, and mechanisms into one overloaded quality label.

### C.25:7 - Conformance Checklist

- `CC-C.25-1` If an engineering quality claim is intended as one measurement characteristic, the publisher **SHALL** bind it to one named `U.Characteristic` with one declared scale.
- `CC-C.25-2` If the claim requires multiple measures, scope slots, mechanism slots, status slots, or qualification windows, the publisher **SHALL** use a Q-Bundle rather than an undeclared scalar surrogate.
- `CC-C.25-3` `ClaimScope` and `WorkScope` **SHALL** remain USM set-valued scope objects; they **MUST NOT** be treated as ordinal or numeric quality levels.
- `CC-C.25-4` Mechanism or status slots **MUST NOT** be conflated with `Measures[CHR]`.
- `CC-C.25-5` Any scalar comparison or thresholding inside a Q-Bundle **SHALL** apply only to declared CHR measures, not to scope slots.
- `CC-C.25-6` Cross-context penalties and bridge losses **SHALL** apply to `R` per `B.3` / `F.9`; they **MUST NOT** silently alter the type of the bundle's `F`, scope, or CHR type authority.

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
| **Category hygiene.** Scope, measurement, mechanism, and status no longer collapse into one term. | Slightly heavier authoring structure; mitigation: only composite cases need the full bundle. |
| **Portable comparison.** CHR measures compare legally, while scope remains governed by USM set algebra. | Authors must declare scales and scope explicitly. |
| **Cleaner gating.** Method/work guards can read the same structure without hidden semantics. | Requires discipline in separating guard factors. |
| **Better endpoint classification.** `C.16.Q` can terminate in either one characteristic or one Q-Bundle with a clear endpoint pattern. | Requires a first-pass endpoint decision during authoring. |

### C.25:10 - Rationale

Engineering quality language is useful precisely because it groups recurring concerns under memorable family labels. The same grouping becomes dangerous when those labels are mistaken for one universal metric. `C.25` preserves the family labels but forces the underlying structure to stay typed and visible.

### C.25:11 - SoTA-Echoing

Contemporary engineering quality practice routinely mixes service-level measures, capability windows, scenario envelopes, mechanism presence, certification state, and evidence traces. `C.25` adopts that practical richness but refuses the common shortcut of compressing the whole family into one undefined score.

### C.25:12 - Relations

`E.21` specialises the Q-Bundle normal form for FPF pattern-quality claims. `C.25` remains the general endpoint for engineering quality families; `E.21` is the endpoint governing pattern when the quality claim evaluates one FPF pattern version as action-guiding FPF text.

**C.27 temporal-claim relation.**

- C.27 may flag: a quality-family statement where agility, resilience, adaptability, recovery, or robustness depends on braking, redirection, stabilization, recovery rate, or rhythm under effort.
- This pattern keeps: quality-family bundle structure, scope, mechanism/status slots, evidence, qualification window, and failure mode.
- Non-admissible use: temporal adequacy is not quality adequacy; speed, recovery, or rhythm becomes quality content only when C.25 declares the quality family, scope, mechanism/status slots, evidence, and failure mode.
- Coordinate with C.27 only when the temporal dynamic changes admissible use; do not make every quality bundle carry dynamic slots.

- **Builds on:** `A.2.6` for scope algebra, `A.6.1` for mechanism references, and `C.16 / A.18` for CHR legality.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `B.3` for assurance penalties, `A.15` for gate use, `C.16.P` for unresolved characteristic, scale, score, metric, or proxy wording inside a quality-family statement, `C.16.Q` for overloaded quality or evaluative-characterization wording, `C.33`, `C.34`, and `C.35` when captured structure, lost structure, preservation, or generated-carrier adequacy becomes part of a composite architecture quality family, `C.17`, `C.18`, and `C.19` for adjacent quality-family measures, and `F.9` or `F.9.1` when cross-context bundle comparison or bridge stance annotation is required.
- **Constrains:** engineering quality authoring whenever a quality term would otherwise drift between single-CHR and composite-bundle readings.

#### C.25:12.1 - Endpoint function in evaluative classification

In evaluative repair, `C.25` is the system-side endpoint pattern for engineering quality families after overloaded quality wording has been repaired by `C.16.Q` and any hidden characteristic, scale, score, metric, or proxy wording has been repaired by `C.16.P`. `qualityTermAscription(...)` may remain a transitional repair record, but it is **not** the universal resting place when the admissible endpoint is a single `Characteristic`, a `Q-Bundle`, or an explicit objective-oriented quality bundle.

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

The bundle is not a fallback for laziness. It is the explicit authoring form for claims whose truth conditions are already composite.

#### C.25:13.3 - Borderline cases

Some quality families contain both a bundle-shaped form and a narrow single-characteristic form. For example, a service team may use:

- one CHR characteristic for a very narrow uptime commitment, and
- one Q-Bundle for the broader service-availability family that includes scope, windows, failover mechanisms, and evidence.

This is legitimate as long as the text states clearly which head is currently in play. The single-characteristic form does not replace the broader family; it selects one evaluative slice of it.

### C.25:14 - Slot Interaction Law

The practical payoff of `C.25` is not just that it names the slots. It also stabilizes how those slots interact.

#### C.25:14.1 - Scope and measure remain orthogonal

`ClaimScope` and `WorkScope` answer **where** or **under what contextual slice** the quality claim holds. `Measures[CHR]` answer **how** a measurable aspect behaves. A broader scope is not a larger measurement value; a narrower scope is not a penalty value. Scope is governed by set inclusion and coverage, not by scalar order.

#### C.25:14.2 - Mechanism and status are gating slots

Mechanisms and statuses may be load-bearing for admissibility, but they do not become measurements merely because they matter. A redundancy mechanism may be required for claiming a resilience bundle, and a certification status may be required for external publication, yet neither slot is itself the `Measures[CHR]` head.

This matters because many quality arguments fail by turning mechanism presence into an implicit hidden score.

#### C.25:14.3 - Qualification windows are not decorative

A quality claim that depends on rolling windows, observation periods, maintenance intervals, or disruption horizons must publish that temporal qualifier explicitly. If the truth of the quality claim changes when the window changes, then the window is part of the declared bundle record rather than optional commentary.

#### C.25:14.4 - Report-only summary proxies

A publisher may compute a report-only summary proxy for convenience, for example a compact quality summary proxy value or an oversight-facing composite score. Such a proxy is admissible only if:

- it is explicitly declared as a **report-only proxy**,
- the underlying bundle slots remain visible,
- and no norm, gate, or bridge silently substitutes the proxy for the bundle itself.

This prevents a convenience summary from becoming a covert replacement for the typed quality claim.

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

Authors should begin with the question: *what is the actual head of this quality claim?* If the truthful answer is "several measures plus scope plus mechanism constraints," start with a bundle and narrow only if a later slice genuinely deserves one CHR head.

A useful authoring order is:

1. name the family label,
2. identify the bearer,
3. publish scope,
4. publish measures,
5. add mechanism/status slots,
6. publish qualification window,
7. bind evidence,
8. and only then consider whether a report-only summary proxy is needed.

#### C.25:16.2 - For assessors

A checking reader should ask:

- whether the chosen endpoint shape is admissible,
- whether any scope slot has been smuggled into scalar language,
- whether mechanism presence has been mistaken for a metric,
- whether the window is truly optional or actually load-bearing,
- and whether any summary proxy is trying to replace the underlying bundle.

In practice, most defects are visible as soon as the checking reader asks what exactly one reported number stands for.

#### C.25:16.3 - For gate designers and assurance leads

Gate designers should resist writing guards against vague family labels such as *resilience must be high*. A conforming gate should instead name the relevant bundle slots:

- coverage over the target slice,
- threshold satisfaction on declared measures,
- qualification-window validity,
- and any required mechanism or status slots.

This keeps the gate auditable and prevents later disputes about what the family label was supposed to mean.

### C.25:17 - Repair and Boundary Notes

#### C.25:17.1 - Repair from bare quality requirement prose

Bare phrases such as *quality requirement*, *security requirement*, or *availability requirement* should not survive as bare heads when the underlying endpoint is actually a characteristic or bundle. The repair rule is:

- choose the endpoint shape first,
- then bind the requirement or commitment to that explicit head.

`C.16.Q` may still be the entry repair for overloaded quality wording, and `C.16.P` may repair characteristic, scale, score, metric, or proxy wording inside the same statement; `C.25` is the resting place only after the engineering quality family has been made explicit.

#### C.25:17.2 - Boundary to assurance penalties

Cross-context transport, bridge loss, or plane mismatch do not change whether the endpoint is one characteristic or one bundle. Those effects apply to `R` and its penalties. `C.25` therefore should not be used to hide assurance degradation inside the quality-family ontology.

#### C.25:17.3 - Boundary to publication convenience

A report, summary publication, or executive summary may expose only one slice of a Q-Bundle, but the underlying authoring structure remains the bundle. Publication convenience is not a reason to collapse the ontology at the source.

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
A context may admissibly extract one narrow slice from a broader Q-Bundle and publish that slice as a single CHR characteristic, but the publication should say that the slice is only one member of the broader family. What is not admissible is to report the slice as though it exhausted the entire family claim.

#### C.25:18.3 - Cross-context family comparison
Cross-context comparison of quality families should proceed through explicit bundle alignment and, where needed, `F.9` bridge discipline on the relevant heads or slots. The bundle ontology stays in `C.25`; bridge loss, translation-relation adequacy, and cross-context penalties remain outside the bundle itself.

### C.25:19 - Gate, Proxy, and Reporting Discipline

#### C.25:19.1 - Report-only summary proxy
A context may publish a summary proxy for reporting convenience, but the proxy remains secondary to the Q-Bundle. The proxy should state what it summarizes and what it leaves out. No report-only proxy may replace the bundle in norms, gates, or endpoint ontology.

#### C.25:19.2 - Gate binding rule
When a gate uses a quality family, the gate should bind to explicit bundle slots: declared scope, specific measures, qualification window, and any required mechanism or status slots. Gate authors should not rely on the family label alone, because labels invite different local decompositions.

#### C.25:19.3 - Roll-up caution
A summary publication or review may aggregate several bundle instances, but the roll-up must remain visibly downstream from the underlying bundle structure. If the roll-up begins to drive local engineering decisions directly, the governing bundle slots should be made explicit again rather than hiding them behind one summary score.

### C.25:20 - Review Matrix and Repair Tests

A checking reader can test a Q-Bundle with five questions:

1. **Is the endpoint shape admissible?** One characteristic where one characteristic is live, one bundle where several typed contributors are load-bearing.
2. **Are scope and mechanism slots kept distinct from measures?**
3. **Is any summary number trying to replace the bundle?**
4. **Would a gate still be auditable if the family label were removed?**
5. **If the claim crosses contexts, is bridge work kept in `F.9` rather than hidden inside the family bundle?**

Repair from bare family prose should therefore recover bundle shape first, then choose whether any narrow slice deserves a separate CHR publication.

### C.25:20a - Viability-envelope, quantum-like, and temporal-claim relation note

Use `C.25` when the question under repair is a quality bundle, "-ility" decomposition, proxy metric, trade-off, gate, or report. A viability claim should not become quantum-like merely because it involves uncertainty, feedback, several qualities, or changing operating conditions; a temporal claim should not become a Q-Bundle merely because the working phrase mentions speed, cadence, rhythm, or recovery.

Practical reading:

1. Decide whether the quality claim is one admissible Characteristic or a Q-Bundle.
2. If it is a bundle, name bearer, scope, measures, qualification window, mechanisms/status, and evidence.
3. Ask whether the claim is really viability-envelope work: protected promise/function, viable region/bounds, several variables, disturbance, sensors/probes, actuators, boundary conditions, adaptation cost, and failure mode.
4. If one proxy or bundle is enough, stay in `C.25`.
5. If the envelope reading depends on a probe, sensor, frame, export, action, coarsening, or boundary interaction that changes what can be said admissibly, the remaining viability-envelope question belongs with `C.26.3`.
6. If the sentence is an intervention-sensitive temporal claim about rate-change under effort, window, resistance, or cadence, inspect `C.27` for the smallest honest temporal-claim adequacy card before using the quality label for action.
7. State viable region/bounds, trade-off, admissible use, non-admissible use, and failure mode before viability language is used for action.

Minimum viability-envelope note:

| Field | Required content |
| --- | --- |
| Bearer | System, service, organization, team, model, process, or role configuration whose viability is at stake |
| Protected promise / function | The promise, function, use, operating regime, or stakeholder value the envelope protects |
| Variables | Which qualities, constraints, resources, risks, or state descriptors define the envelope |
| Viable region / bounds | What counts as inside, near edge, degraded, or outside the envelope for this use |
| Disturbance class | What perturbation, demand shift, environment change, probe, or boundary condition stresses the envelope |
| Actuators | What work, design move, policy, boundary change, sensor change, or resource change can move the bearer |
| Trade-off / loss | What gets worse, hidden, coarsened, delayed, or made more expensive |
| Admissible use | Which action, decision, relation, or triage use the envelope reading can carry |
| Non-admissible use | Which release, audit, assurance, or universal quality claim requiring additional support it does not support |
| Failure mode | What it means to leave the envelope or to mistake one proxy for the envelope |

Useful outputs:

- a Q-Bundle when the issue is quality decomposition;
- a `C.26.3` envelope-regulation note when probes/actuators/boundary conditions change the admissible viability reading;
- a `C.27` temporal-claim adequacy card when rate-change, effort, window, resistance, or cadence changes the admissible use;
- no QL wording when ordinary quality-bundle, proxy, feedback, or control tuning carries the work.

#### C.25:20b - Architecture-decision Q-Bundle boundary

`C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite Q-Bundles as architecture-characteristic inputs, accepted-loss structure, guardrail rows, feedback concerns, or adequacy concerns. C.25 keeps composite quality-family slots, bearer, scope, measures, mechanisms, qualification window, and evidence distinct from the problem-to-structure architecturing flow, project architecture decision relation, and ADR-like publication projection.

### C.25:End

