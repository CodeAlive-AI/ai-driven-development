## SYSE.14 - Make a Release Decision for Named Engineering Work or Use

> **Status:** Stable

### SYSE.14:0 - Use This When

Use this pattern when a workflow says that an engineering change is *approved*, *released*, *deployed*, or
*implemented*, but the receiving Agent still cannot tell what may happen next, to which actual Systems, under
whose authority, on what evidence, or under which conditions.

Begin with one question: may an identified description, software package, or actual System in a stated
configuration enter named Work or use—for example, realization, integration, trial, deployment, delivery, or
service? A release decision relates that subject to a permitted next use under stated conditions; a generic status
label does not.

The first useful result is a **bounded engineering release decision**. It states what may enter the named Work or
use, for which units and conditions, what evidence and authority support the decision, what remains blocked, and
what later observation reopens it. The decision is an episteme. Separate evidence establishes the deciding
Agent's authority and any required permission, the observed configuration, performed change Work, resulting
transformation, and operating result.

Use `SYSE.13` when the immediate difficulty is identifying the relevant units, configurations, or effectivity.
Use `SYSE.19` when a changed source may invalidate an earlier decision. Use a governing FPF pattern directly when
one isolated result—such as a choice, permission, gate, Work, transformation, evidence, assurance, status, or
transfer result—already answers the question.

#### SYSE.14:0.1 - Terms and Distinctions

| Name in this pattern | What it denotes |
| --- | --- |
| trigger | A source event such as a request, criticism, incident, opportunity, or changed source that starts reconsideration. Its problem claim, proposed response, and permission each need their own grounds. |
| change candidate | An episteme describing a possible-future change, affected Systems and descriptions, expected consequences, conditions, and evidence gaps. It is not an actual transformation. |
| technical choice | A `C.11` result comparing stated options. Authority, permission, release, and later realization require separate relations or results. |
| release subject and release kind | The identified description, software package, or actual System being considered, its relevant configuration, and the named next Work or use. Release for realization and release to service are different decisions. |
| authority | A grounded relation that gives an Agent the right to make the named decision within a stated scope. Establish its scope and grounds separately from a title, assignment, signature field, or meeting attendance. |
| permission | A separately governed allowance concerning a named action, holder, subject, scope, and interval. Authority, evidence, assurance, and release retain their own relations and results. |
| implementation or integration Work | A dated Work occurrence performed by an Agent using a Method and relevant Systems. A ticket state or released description is not performed Work. |
| actual change | A world-side transformation of an actual System under stated conditions. It remains distinct from the Work, Method, candidate description, and decision. |
| actual configuration and effectivity | The actual configuration comprises the resulting System's constituents, obtaining relations, and characteristic values over an interval. Effectivity is an episteme stating which identified Systems and conditions a description, change, or release applies to. |
| evidence and assurance | Evidence bears on named claims; assurance evaluates warranted reliance for a use. Neither supplies authority or entails release. |
| description or status update | An episteme used for coordination. Updating it neither changes the System nor proves that the intended change was realized. |
| handover, delivery, deployment, or commissioning Work; acceptance decision | Work and decision results that source vocabularies often call *release*. Name the occurrence or result at issue. |

The deciding, performing, permission-granting, and receiving Agents may differ. Evidence-producing Work may be
performed by another Agent. The release subject, changed System, and other affected Systems retain their own
identities and need not be Agents.

### SYSE.14:1 - Problem Frame

One controller change can alter actual Systems, interfaces, and behaviour; change needed manufacturing or service
Work; and invalidate descriptions or supporting evidence. A release for realization may precede implementation
under the applicable release rule. A release to service normally concerns an actual System in an observed configuration after
implementation. Treating both as one generic approval loses the decision subject and its evidence.

Workflow tools can coordinate records and checks, but their status labels are not the engineering ontology.
*Approved* can denote, for example, acceptance for analysis, technical selection, permission, release for build,
a gate result, an installed-state claim, or acceptance for use. Those results have different Agents, authority,
evidence, subjects, and consequences.

### SYSE.14:2 - Problem

The recurring engineering difficulty is to move fast without releasing the wrong change, the wrong unit, or a
change supported by evidence from another configuration. A usable release decision answers seven questions:

1. What identified description, software package, or actual System in which configuration may enter the named
   Work or use?
2. Which actual units, sites, intervals, and operating conditions are covered?
3. What current configuration basis connects the candidate, descriptions, and actual Systems?
4. Which affected Systems, interfaces, Work, obligations, and downstream consequences can change the choice?
5. Which Agent makes the decision, what authority obtains, and which separate permissions are required?
6. Which evidence supports which claim for this configuration and use, and what material uncertainty remains?
7. What may happen next, what remains withheld, and which change or observation reopens the decision?

Without those answers, a technically sound change can reach an incompatible unit, a valid partial release can
wait behind irrelevant approvals, or a green status can conceal missing implementation and operating evidence.

### SYSE.14:3 - Forces

Recurring tensions include:

- Routine and reversible changes can benefit from fast feedback; select criticism, evidence and required
  permissions according to the consequences, reversibility and intended use.
- Participants need one connected change case, while the request, choices, permissions, Work, transformations,
  descriptions, and decisions remain different objects.
- A local improvement can shift failure, service burden, cost, or risk to another System.
- Family descriptions support reuse, while release and service decisions can depend on serial units and installed
  configurations.
- Automated checking shortens feedback, while decision authority and any required legal, safety, commercial, or
  organizational permission need their own grounds.
- Change Work continues; one release question still needs a usable current answer.

### SYSE.14:4 - Solution

Develop one bounded release decision around the named next Work or use. Carry forward only the configuration,
consequence, authority, permission, and evidence claims that can change that decision.

Use an established professional release result or qualified software-delivery result directly when it already
answers this subject's next-use question with the required evidence and permissions. When a needed connection
is absent, construct that addition: for example, connect an installed unit's evidence and a separate service
permission to the current choice. An existing change account may carry the result.

Compare a focused addition to the existing records with a workflow that maintains those connections. Hold the
release subject, next use and required assurance constant; include the work of checking the connection now and
keeping it valid after corrections. Repeated releases may justify maintained integration. One bounded decision
may justify a checked addition without a new standing workflow.

#### SYSE.14:4.1 - Perform the Move

1. **Bound the release question.** State the identified description, software package, or actual System under
   consideration; its relevant configuration; the named next Work or use; the deciding Agent; the interval and
   conditions; and the current options. The option set may include release, narrower release, trial, withholding,
   rejection, or obtaining another result first.
2. **Establish the configuration and effectivity.** Use a compatible `SYSE.13` result or qualified direct sources
   for the units, descriptions, installed realizations, sites, intervals, and conditions that matter. Return a
   missing configuration result instead of guessing correspondence.
3. **Separate the trigger from the candidate.** Record the triggering event—for example, a request, criticism,
   incident, opportunity, or source change—with its evidence status. Describe viable change candidates separately.
   Keep the unchanged-System option when viable; treat deferral as a decision to await an event or obtain another
   result.
4. **Trace consequences far enough to change the choice.** Identify affected actual Systems and relations,
   descriptions, realization and integration Work, provider and receiving Agents, obligations, supporting evidence,
   and reversibility. Use files, team names, and hyperlinks to locate relevant records or Agents, then establish
   the affected world-side objects and relations.
5. **Name the Agents and governing relations.** Identify the Agent making the release decision, Agents granting
   required permissions, Agents performing later Work, and receiving Agents. State assignments, authority,
   permissions, conflicts of interest, and abstention conditions separately.
6. **Qualify the evidence.** Connect each evidence result—for example, a test result, model evaluation, trial
   observation, specialist result, or assurance result—to the claims, configurations, conditions, and uses it
   supports. When a relied-on source changed, use a compatible `SYSE.19` result or reopen the affected claim
   directly.
7. **Compare the current options.** Hold the option set and comparison basis stable long enough to choose. State
   protected characteristics, acceptable losses and material uncertainty. Use `C.11` for the choice itself.
   When further evidence is being considered because it could change this choice or its warranted use, compare
   the feasible next observation's cost and decision value. Retain the resulting inquiry judgement or limitation
   needed by this decision or its recipient. When no further inquiry is selected, no new observation proposal or record is needed.
8. **State and return the release decision.** Name the selected disposition, subject, effectivity, conditions,
   evidence, authority, permissions, unresolved risks, permitted next Work, withheld scope, and reopen conditions.
   If a decision-changing input is missing, return that missing result rather than *approved with caveats*.
9. **Connect later realization.** When implementation or integration has occurred, identify
   the performing Agent, dated Work, Method, actual transformation, resulting configuration, and observations.
   Update affected descriptions and recipients, but do not use a record update as proof of realization.

A release for realization can occur before implementation; release to service can depend on later implementation
and observation; emergency containment Work can precede a full technical choice under its own authority. The case
must state its actual dependencies and timing.

#### SYSE.14:4.2 - Record the Result

| Field | Required content |
| --- | --- |
| release question | Release subject and kind, deciding Agent, receiving Work or use, current options, interval, and conditions. |
| configuration and effectivity | Identified actual Systems; actual constituents, obtaining relations, and characteristic values; relevant descriptions; supporting evidence; and the subjects and conditions to which the decision applies. |
| trigger, candidates, and consequences | Trigger with epistemic status; viable candidates; affected Systems, interfaces, Work, obligations, downstream consequences, reversibility, and retained alternatives. |
| Agents, authority, and permissions | Deciding, permission-granting, performing, and receiving Agents; assignments; direct authority and permission relations; conflicts and abstention conditions. |
| evidence and choice | Evidence for each claim, with provenance and limits; comparison basis; selected disposition; accepted losses; material uncertainty; the judgement or limitation from a live inquiry alternative when needed by this decision or its recipient. |
| decision and continuation | Released, narrowed, trial-only, withheld, rejected, or probe-again result; next Work allowed by the governing rules and permissions; withheld scope; blockers; withdrawal and reopen conditions. |
| later realization, when relevant | Performing Agent, dated Work, Method, actual transformation, resulting configuration, observations, description updates, recipients, and known correspondence gaps. |

The result may be carried, for example, by an issue record, release note, model view, linked engineering
records, or generated report. The decision keeps its identity and grounds across those carriers; authority,
permission, performed Work, and actual configuration remain separately established.

#### SYSE.14:4.3 - What Changes in Practice

Engineers stop treating *approved*, *merged*, *passed*, and *released* as interchangeable completion signals.
They can release a supported subset of units and add independent evidence or permission where the change's
consequences require it.

The receiving Agent gets a usable next action: perform the named Work, use the released configuration, obtain a
missing result, or stop. On later implementation or operating evidence, the authorized deciding Agent may narrow
or supersede the release decision; the earlier decision and performed Work retain separate identities.

### SYSE.14:5 - Worked Case: Cold-Start Protection for Ten Pump Controllers

A pump manufacturer must decide which of ten installed controllers may enter monitored service with a cold-start
protection change. The configuration basis from `SYSE.13` distinguishes four groups:

| Installed units | Current finding | Consequence for this release |
| --- | --- | --- |
| S001–S004 | IO-A input board; candidate package supports IO-B. | Outside the candidate's hardware compatibility claim. |
| S005 | IO-B and the required sensor; current calibration evidence is missing. | Withheld until the missing evidence is obtained. |
| S006–S008 | IO-B, current calibration evidence, installed candidate realization, and chamber-test evidence. | Eligible for the current service-release comparison. |
| S009–S010 | IO-B; database says *installed*, but current calibration and cold-start evidence are absent. | Trial or service release is not supported by the current evidence. |

The original request asked for release to all ten units. The engineering team retained three real options:
withhold service release on the changed units; admit S006–S008 to monitored service; or extend a trial to
S006–S010. The last option failed the stated calibration-evidence threshold. Withholding avoids exposure to
the changed configuration but keeps the three otherwise eligible units out of service for now.

The release board acts as the deciding Agent and has authority for this service-release decision. An independent
safety team acts as the permission-granting Agent; its permission covers only S006–S008, the named temperature
envelope, and the monitoring interval. Assignment to either team is recorded separately from authority.

The controller-integration team had already performed the installation Work on S006–S008. The firmware package
description, installation record, software attestation, and physical inspection are separate sources for the
resulting configuration claim. A revised calibration source had reopened only the cold-start claim. Chamber tests
for S006–S008 restored that evidence. A maintenance observation showed restored pump-train functioning for S006
under one load and temperature interval; it added evidence for S006 only and established neither safety nor the
state of S007–S008.

For this illustrative comparison, assume the chamber tests cover the proposed temperature envelope and support
correction of the observed cold-start failure without loss of the required control response. They support an
expected benefit on S006–S008, with uncertainty about field behaviour remaining. Staff and a practicable way
to detect a recurrence and stop the affected unit are available throughout the monitoring interval.

The board gives priority to restoring needed cold-start-capable service while preserving the required control
response. Its rule prefers monitored service to withholding when that response and the separate permission
are supported and recurrence can be detected and contained. On the same evidence, withholding avoids the
remaining change risk and monitoring work but forgoes that service. The board accepts the monitoring burden
and residual field uncertainty for this bounded interval. If monitoring is unavailable or the required control
response lacks support, this rule favours withholding; permission alone cannot settle the choice.

The release decision therefore admits S006–S008 to monitored service under the stated conditions. S005 and
S009–S010 remain withheld pending calibration and cold-start evidence; S001–S004 remain outside hardware
compatibility. The next Work is monitored service, not another installation inferred from the decision. A sensor
replacement, firmware change, calibration-source change, cold-start failure, or operating-envelope change
reopens only the affected unit and claim.

The engineer adds the service decision to the existing change account and links the unit evidence and separate
permission. For this single subset release, the team chooses that checked addition over configuring a workflow
to maintain the same connections automatically. It accepts manual revalidation after an affected record changes.
Recurring releases could justify the maintained workflow; either approach needs the same choice, evidence and
permission. Neither a package's software approval nor its installation record already answers this service question.

The decision can supply bounded evidence to `SYSE.4`, whose assurance Work may still find an unsupported claim or
return a blocker. The release decision itself establishes no assurance conclusion.

**When the full pattern is unnecessary.** A reversible internal script has one known configuration, no physical
effectivity question, and an established deployment Method that already supplies the needed choice, evidence,
permission, Work, and rollback results. Use those direct patterns instead of constructing a connected engineering
release case.

### SYSE.14:6 - Bias Annotation

A document-control Method can turn every change into a long approval chain. A software workflow can treat a
green pipeline result as universal release authority. Scale scrutiny to consequence and reversibility while keeping
actual Systems, descriptions, evidence, authority, permission, and performed Work distinct.

Official procedures, vendor workflow labels, and declared conformance support claims about their records or
requirements. Actual enacted practice, effectiveness, and configuration need their own evidence. Use expert
judgement with an explicit epistemic status when broader field evidence is unavailable.

### SYSE.14:7 - Conformance Checklist

- [ ] One release subject, release kind, receiving Work or use, deciding Agent, and current option set are stated.
- [ ] The configuration basis concerns the same actual Systems, descriptions, conditions, and release question.
- [ ] The decision uses each approval or completion status only for what it establishes. Any required permission,
      claimed installation or resulting configuration has its own support.
- [ ] Consequence tracing reaches affected Systems and direct relations, not only files, departments, or links.
- [ ] Every relied-on authority, permission, and evidence result has the subject, scope, interval, and source
      needed by the decision.
- [ ] The comparison basis, selected disposition, retained alternatives, acceptable losses and material
      uncertainty are recoverable. Any live inquiry alternative is resolved sufficiently for the choice, with
      the judgement or limitation needed by the decision or its recipient; inactive inquiry adds no entry.
- [ ] Any claimed implementation identifies the performing Agent, dated Work, Method, actual transformation,
      resulting configuration, and evidence.
- [ ] The result states permitted next Work, withheld scope, blockers, and withdrawal and reconsideration
      conditions.

### SYSE.14:8 - Common Failures and Repairs

These recurring release errors change the next permissible action:

| Failure | Repair |
| --- | --- |
| Request equals decision | Keep the request as a trigger and compare viable change options. |
| Signed form supplies authority | Identify the deciding Agent and the authority relation for this decision. |
| Gate pass equals release | Use the gate result as one premise and state the release subject, kind, and effectivity separately. |
| Release equals implementation | Identify performed Work and actual transformation, or state that they remain future. |
| Updated status equals actual configuration | Obtain evidence about the identified units and keep the status as a claim. |
| Apply one software pipeline to every engineered System | Select review, automation, assurance, and permission by consequence, reversibility, and the actual System or intended System referent selected for engineering and the use this release permits, including bounded creator acceptance when that is the current question. |
| All units inherit one release | Name supported units and conditions; narrow or withhold the rest. |
| A changed source reopens everything | Trace the changed claim and reconsider only the affected decisions. |

### SYSE.14:9 - Consequences

Release speed and scrutiny can vary with consequence without losing accountability. Implementation, operation,
maintenance, and assurance receive a decision that names configuration, effectivity, evidence, authority, and
next Work. Mixed physical and software changes can share one connected case while retaining their own Work
cadences and evidence.

Consequential cases cost additional impact recovery, evidence maintenance, and authority checks. Some decisions
must remain narrowed or blocked. Specialist rules—for example, safety, legal, cybersecurity, medical, aviation,
financial, commercial, or organizational rules—remain with their own patterns and application DPFs.

### SYSE.14:10 - Rationale

The decision concerns one subject entering one named Work or use. This boundary lets contributors see how configuration, consequences, evidence, authority, and permissions
bear on the same current choice while preserving each result's identity.

Effectivity makes partial release possible when evidence differs by unit or condition. Explicit reopen conditions
let engineering continue from the current decision and identify which later configuration changes require
reconsideration.

### SYSE.14:11 - SoTA and Source Use

**Working question:** How should an engineer obtain a justified release for named Work or use without adding
approval and record-keeping work that cannot change that decision?

The selected line reuses an adequate professional release process or qualified software-delivery path and
constructs only a missing connection needed by the receiving decision. A competent CM process can already
relate affected-function contributions, implementation costs, dependencies, effectivity and release. A software
path can combine peer review, automated feedback, recorded authorization and additional scrutiny for material
risk. Use either result directly when it covers the same release subject and next use; :4 makes this the
ordinary entry rather than requiring a second release account.

The authored connection matters when those results do not yet answer the receiving question. In :5, installed
software and package approval do not decide whether the identified controllers should enter monitored service.
Steps 2, 5–8 connect unit-qualified evidence and independent permission to the board's explicit comparison.
The case shows why monitored service is preferred to withholding under the stated illustrative evidence,
priority and accepted burden. Eligibility alone leaves that preference unresolved.

A workflow that maintains these connections and returns the same bounded decision is a serious alternative
to constructing it from existing records. Compare both for the same service question and assurance needs.
The case accepts manual checking and revalidation for one subset release, retaining the result in the existing
account. An integrated workflow can become preferable when repeated releases justify its construction and
upkeep. Neither path reduces the required evidence or permission. This is an explicit trade-off, not measured
superiority of a manual case or a universal argument against release automation.

| Source answer considered | Disposition in this Method | Scope and limit |
| --- | --- | --- |
| Frank B. Watts, *Configuration Management for Senior Managers* (2015), request evaluation, technical release and change implementation | **Adopt** early contributions from affected functions, alternatives and implementation costs; **adapt** the technical-release/incorporation distinction to the named next use in :4.1 and :5. A professional arrangement that already supplies the bounded result is sufficient. | This historical practitioner treatment includes coordination, online processing and limited signatures. Its specific departmental and payback rules, and its claim that release ends technical uncertainty, are not conditions of this Method. |
| [DORA, Streamlining change approval](https://dora.dev/capabilities/streamlining-change-approval/), updated 2025-10-30, especially implementation and improvement guidance | **Adapt** peer review, automated feedback and risk-sensitive scrutiny for the software path admitted by :4 and the direct-use case in :5. Retain recorded authorization and consequential cross-team trade-offs. | The page points to the 2019 research; its maintenance date is not new empirical evidence. Software guidance alone does not qualify physical effectivity or the separate service permission in the controller case. A path that supplies those results can suffice. |
| [Beibl and Krause 2024](https://doi.org/10.1017/pds.2024.253), §§1–5, changes from development, production and customer-owned viewpoints | **Adapt** consequence tracing to the receiving context in :4.1 step 4, including testing windows and downstream work. This limits transfer of a release arrangement between contexts. | The observations come from one manufacturer. They supply a context-sensitive constraint on the comparison, not a complete release Method, universal prevalence or a preferred release frequency. |
| [Zampetti et al. 2022](https://doi.org/10.1145/3571854), mixed cyber-physical delivery practices and challenges | **Adapt** the combination of software feedback, physical qualification and specialist contributions when constructing the alternative release path. Keep their needed results connected while allowing different cadences. | The qualified cases support heterogeneous simulation, hardware-in-the-loop and deployment arrangements. They establish neither one universal pipeline nor equivalence between software feedback and physical release evidence. |

Reopen the affected selection when the release's units or next use change, a relied-on result loses its scope
or permission, or recurring connection work makes a maintained alternative worthwhile. A better source Method
changes the relying step only where it supplies the same required result under applicable conditions.

### SYSE.14:12 - Relations

- `C.11` governs choice among current options. `A.21` governs a gate decision. `A.2.8.PER` governs permission,
  `A.15.1` Work, `A.3.4` actual transformation, `F.10` status, `A.10` evidence, and `B.3` assurance. This pattern
  composes their results for one engineering release and replaces none of them.
- `C.2.1`, `E.17`, and `E.24.PUB` keep change descriptions, decision epistemes, publications, forms, and carriers
  distinct from the changed System and performed Work.
- A compatible `SYSE.13` result supplies configuration and effectivity only for the same change and release use.
  It establishes neither permission nor release.
- A compatible `SYSE.19` result supplies revision consequences only for decisions that relied on the changed
  source. Co-use does not impose a universal temporal order.
- Restored-function evidence from maintenance or operation can support only the same actual System,
  configuration, conditions, and claim. It neither selects the change nor authorizes release.
- `SYSE.14` can supply bounded evidence to `SYSE.4` for the same release question and evidence window. `SYSE.4`
  performs its own assurance Work.
- Application moves—such as software deployment, electrical energization, medical-device release, ship
  alteration, building commissioning, or manufacturing release—may specialize the Method because their project
  Systems-of-interest, permissions, evidence, and effectivity differ. They are not synonyms merely because each can use this pattern.

### SYSE.14:End
