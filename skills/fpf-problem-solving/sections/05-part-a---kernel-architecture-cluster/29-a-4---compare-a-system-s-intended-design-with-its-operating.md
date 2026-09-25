## A.4 - Compare a System's Intended Design with Its Operating Conditions

### A.4:1 - Problem frame

**Use this when** a decision depends on whether an independently identified System's operation matches a selected design account, and that comparison is still unresolved. The account may state an intended operating condition, required result or predicted behavior. Select the account edition and its operative comparison criterion before diagnosing a discrepancy or choosing a change.

The first useful result is a fit, a stated discrepancy or the exact missing/incomparable basis. An engineer can obtain that answer without starting an adaptation loop or changing the System or its design.

**Not this pattern when.** Reuse a sufficient direct domain comparison. Use A.1.1 for an unresolved model-applicability question, C.2.1 for episteme identity and edition relations, A.3.4 for an actual change claim, and B.4 when repeated adaptation itself needs coordination. An unchanged theorem being cited is an episteme-use question, not a System design/operation comparison.

### A.4:2 - Problem

| Failure | Practical consequence |
|---|---|
| A design account is treated as the actual System. | Editing the account appears to improve a System whose operation has not changed. |
| An operating result is compared with an unspecified target or under different conditions. | A reported pass or failure cannot guide the receiving decision. |
| A discrepancy automatically triggers design revision. | A still-applicable target may be weakened merely to make the discrepancy disappear. |
| Measurement, its record and target change are conflated. | A new observation is mistaken for a changed subject or a new System. |

### A.4:3 - Forces

| Force | Tension |
|---|---|
| Stable subject, changing accounts | Compare the continuing System with the selected account without deriving System identity from document versions. |
| Intended result and actual facts | Preserve a normative target while learning what is happening; a descriptive prediction can raise a different revision question. |
| Comparable evidence and effort | Obtain the facts needed by the criterion while reusing an adequate comparison or observation. |
| Diagnosis and authority | Discover a discrepancy without presuming which participant may change the subject, account or receiving use. |

### A.4:4 - Solution - One Bounded Comparison

1. **Select the subject, account and use.** Identify the System, the design account edition and the decision this comparison must inform. Keep the System's identity under its own rule and the account's identity under C.2.1. Choose the relevant account claim rather than treating the entire design as one test.
2. **Recover the operative criterion.** State the target or expected behavior, relevant conditions, units and tolerances, and the rule for comparing them with actual facts. Identify what force the account claim has:

   | Account claim | What the comparison can establish |
   |---|---|
   | Normative target, such as a required minimum flow | Whether the actual operation meets that target under the rule. A miss does not by itself make the target inapplicable. |
   | Descriptive prediction | Agreement or discrepancy between predicted and actual behavior under the prediction's conditions. Model revision remains a separate decision. |
   | Applicability condition | Whether the named condition is met. Use A.1.1 when the question is the model's applicability to this subject/use; do not substitute target conformance for that judgment. |

3. **Obtain or reuse comparable facts.** Recover the actual operating conditions and results required by the criterion. Check their temporal reference, units, tolerance, relevant configuration and measurement uncertainty when it affects the selected decision rule. If the design and observation concern different conditions, use an already justified translation only within its limits. Otherwise name the missing basis. Use C.27 when temporal adequacy is itself unresolved.
4. **Perform the comparison and return its boundary.** State what meets the criterion, the discrepancy, or the precise missing or incomparable premise. Qualify the result to the named System, account claim, conditions and use. When a rule withholds acceptance because the evidence is too uncertain, distinguish that outcome from an established physical failure. A partial comparison can leave other requirements unexamined.
5. **Separate any response decision.** Keeping the present use, qualifying reliance, changing the System and revising the account are different possible next decisions. Use their own authority and subject methods when needed; B.4 coordinates repeated adaptation. Do not replace the selected target with an easier one and report that as improved conformance. Stop at the comparison when it answers the working question.

No additional record is required when the subject, criterion, actual facts and bounded answer are already recoverable in the working account. Describing this method does not assert that an observation or Work occurrence happened.

#### A.4:4.1 - Observation, change and continuity

An observation may involve dated measurement Work. Recover that Work under A.13 and A.15.1 only when the receiving claim needs the occurrence; identify the result and its relied-on evidence under their own patterns. A new record does not establish a target change. A.3.4 governs any actual before/during/after change claim, and A.12 distinguishes actual acting and changed participants when internal action is asserted.

Changed account claim content identifies a different C.2.1 episteme. An obtaining edition relation is a further claim with its own conditions, including any actual branching. Neither an account edit nor overlapping operation and design work decides the System's continuity. Particular practices may define design and operating regimes where useful; these regimes do not partition every holon's existence.

### A.4:5 - Archetypal Grounding

#### A.4:5.1 - One continuing pump, two selected design accounts

In this constructed case, `Pump37` operates under condition set C. A justified domain comparison uses exact flow values in L/min under those matched conditions. The available observation is 105. Account D1 requires at least 100; account D2 requires at least 110.

| Selected basis | Comparison | Bounded result |
|---|---|---|
| D1, C, minimum 100 L/min | 105 ≥ 100 | This flow requirement is met. |
| D2, C, minimum 110 L/min | 105 < 110 | Flow misses this requirement by 5 L/min. |
| D2 under C, observation under C′, with no justified translation | The comparison premise is missing. | Unresolved comparison, not a failed pump or a false design. |

Selecting D2 changes the comparison basis; it does not physically change Pump37. Editing D1 into D2 changes the account's claim content. Its historical edition relation, if claimed, must independently obtain. The discrepancy against D2 may justify a later response question, but supplies neither change authority nor a requirement to revise the design.

#### A.4:5.2 - Distinguish the actual event and its next use

| Working situation | Correct exit |
|---|---|
| A pump circulates coolant while its CAD account is edited. | Use the continuing pump and the selected CAD account claim in the comparison. Operating Work and editing Work concern different subjects; the edit establishes no physical pump change. |
| An author cites an unchanged theorem. | Use the direct episteme-use rule. The theorem executes no OperationalMethod; any reasoning Work has its own performer and Method. |
| An unused pump weathers. | A.3.4 can qualify the actual material change without invented Work. If later design conformance matters, compare the resulting condition with the selected criterion. |
| A sensor measurement produces a new observation record. | Use the observation as warranted input to the comparison. Measurement and result do not by themselves establish target change. |
| A pump's internal control System performs maintenance. | A.12 distinguishes acting and changed participants. The System's identity rule can preserve the same pump; compare its relevant resulting facts if the intended use requires it. |

### A.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| **CC-A.4.1** | Identify the System, selected account edition, account claim and receiving use. | Fix the comparison's subject and basis. |
| **CC-A.4.2** | Distinguish normative target, descriptive prediction and applicability condition; recover the comparison rule. | Prevent a failed target test from silently becoming an applicability or revision decision. |
| **CC-A.4.3** | Use comparable actual facts with the required conditions, temporal reference, units and tolerances, or state the missing premise. | Give fit and discrepancy their warranted scope. |
| **CC-A.4.4** | Return the bounded comparison before any separately selected adaptation. | Preserve a useful answer without compulsory change. |
| **CC-A.4.5** | Keep account identity/edition, actual Work, target change, System continuity and response authority under their direct rules. | Allow overlapping activity and branching accounts without a universal phase or predecessor law. |

### A.4:7 - Consequences

The practitioner can distinguish a changed System, changed knowledge of its operation and a changed design criterion. A discrepancy becomes actionable because it names the unmet condition or missing comparison basis. Reusing adequate facts and stopping at a sufficient answer keeps a simple comparison small.

The comparison costs the recovery of its account, criterion and relevant actual facts. It cannot supply missing domain law, resolve every uncertainty or decide who may alter a target. When repeated adaptation is warranted, B.4 consumes the result with the independently selected response and continuity rules.

### A.4:8 - Rationale

The difference between intended design and actual operation is a relation between an account claim and facts about its subject. It is not explained by labeling every state “design-time” or “run-time”. A pump may operate while engineers edit its description; an observation may change knowledge while the pump remains unchanged.

Selecting the criterion first makes the distinction useful. The same observed flow can meet one requirement and miss another, and unmatched conditions can leave both conclusions unsupported. Keeping the response separate preserves an applicable target and permits a justified decision to retain the current arrangement, qualify its use or investigate further.

Repeated improvement remains available through B.4. It follows a selected need and subject-specific continuity, rather than a law requiring every holon to evolve or every account to have exactly one predecessor.

### A.4:9 - SoTA-Echoing

**Practice question.** How can an operating observation answer a design question while preserving the selected requirement, comparable conditions and a separate decision about what to change?

The selected line first identifies what the comparison is meant to establish, then applies an explicit decision rule. **Adopt** the distinction in the NASA *Systems Engineering Handbook*, Rev. 2, NASA/SP-2016-6105, [§2.4](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/): compliance with specified requirements and suitability for intended use in the intended environment answer different questions. This supports §4 steps 1–3: a passed flow requirement is not by itself proof of operational suitability. NASA's wider life-cycle process is outside this bounded method; its source role here is the substantive separation of comparison purposes.

For a quantitative requirement near a measurement limit, the competing answers are simple acceptance and guarded acceptance. [JCGM 106:2012, §§8.2–8.3](https://www.bipm.org/en/doi/10.59161/jcgm106-2012), supplies both: simple acceptance compares the measured value directly with the tolerance; guarded acceptance narrows the acceptance region to reduce false acceptance. The former is a serious, inexpensive choice when the parties accept its risk and the measurement uncertainty is adequate for their purpose. The latter can cost more false rejections. Neither changes the specified tolerance itself.

**Adapt** that comparison in §4 steps 2–4: retain the applicable rule and its uncertainty basis instead of silently treating every point estimate as decisive. Where the receiving use requires protection against false acceptance, guarded acceptance is the better answer at comparable effort when the uncertainty estimate is already available. Where that extra protection is unnecessary, reuse a sufficient simple comparison. **Reject** automatically tightening the rule or weakening the requirement merely because the result is inconvenient.

The exact-value pump comparison in §5.1 needs no extra uncertainty calculation. In a separate constructed variant, the available estimate is `105 L/min`, its justified coverage interval is `97–113 L/min`, and the minimum requirement remains `100 L/min`. Simple acceptance accepts the point value. A selected rule requiring the entire interval to satisfy the minimum withholds acceptance because `97 < 100`. Both use the same observation; the second result does not establish that the pump actually delivers less than 100. This is why step 4 distinguishes an evidential limit from an established discrepancy, and step 5 leaves any response to its own authority.

Reopen the chosen rule if the uncertainty or condition-translation basis changes, or the receiving use changes the tolerated decision risk. If the selected account instead contains a descriptive prediction, return to step 2 and recover its prediction-comparison rule; a conformity-assessment source does not authorize recalibrating the prediction or revising a requirement.

### A.4:End
