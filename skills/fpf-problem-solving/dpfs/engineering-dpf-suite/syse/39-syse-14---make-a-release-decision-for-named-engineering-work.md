## SYSE.14 - Make a Release Decision for Named Engineering Work or Use

> **Status:** Stable

### SYSE.14:0 - Use This When

Use this pattern when a workflow calls an engineering change *approved*, *released*, *deployed* or *implemented*, but
the receiving Agent cannot tell which work or use may follow for the release subject and any affected units, who has
authority, what the evidence supports or which conditions apply.

Begin with what the release would let its recipients do. Identify the descriptions, packages or actual Systems, configurations and next uses covered by the decision. A unit may qualify for a trial, several units for separate service, or an assembly for joint operation. Establish which of these the release must authorize.

The first useful result is a **bounded engineering release decision**. It states the disposition for the named Work or use, the release subject
and its applicable conditions, any units or intended configurations covered, the supporting evidence and authority, any scope withheld, and
what would reopen the decision. The decision is an episteme. Establish the deciding Agent’s authority and any required permission on
their own grounds. An assertion about an observed configuration, completed change Work, resulting transformation or operating result
needs evidence for that assertion.

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

Workflow tools can coordinate records and checks, but a status label can denote several different engineering results.
*Approved* can denote, for example, acceptance for analysis, technical selection, permission, release for build,
a gate result, an installed-state claim, or acceptance for use. Those results have different Agents, authority,
evidence, subjects, and consequences.

### SYSE.14:2 - Problem

The recurring engineering difficulty is to move fast without releasing the wrong change, the wrong unit, or a
change supported by evidence from another configuration. A usable release decision answers the following questions:

1. What identified description, software package, or actual System in which configuration may enter the named
   Work or use?
2. Which units or intended configurations, sites, intervals and operating conditions does the release cover?
3. What configuration basis connects the candidate and descriptions to those Systems or intended configurations for this use?
4. Which affected Systems, interfaces, Work, obligations and downstream consequences bear on the choice or its conditions?
5. Which Agent makes the decision, what gives that Agent authority for this decision, and which separate permissions are required?
6. Which evidence supports each claim for this configuration and use, and is there any material uncertainty?
7. What may happen next, is any scope withheld, and what change or observation would reopen the decision?

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
- As change Work continues, the deciding Agent needs an answer to the release question at hand.

### SYSE.14:4 - Solution

Develop one bounded release decision around the named next Work or use. Carry forward the configuration, consequence, authority,
permission and evidence claims needed to select or justify the disposition and its conditions.

Use an established professional release result or qualified software-delivery result directly when it already
answers this subject's next-use question with the required evidence and permissions. When a needed connection
is absent, construct that addition: for example, connect an installed unit's evidence and a separate service
permission to the current choice. An existing change account may carry the result.

Compare a focused addition to the existing records with a workflow that maintains those connections. Hold the
release subject, next use and required assurance constant; include the work of checking the connection now and
keeping it valid after corrections. Repeated releases may justify maintained integration. One bounded decision
may justify a checked addition without a new standing workflow.

#### SYSE.14:4.1 - Perform the Move

1. **Bound the release question.** Recover the subject, use, effective interval and deciding authority from the proposed release. Follow the use to the units and dependencies that could change that decision. If separately acceptable units are to operate together, check the interfaces, shared support and permissions needed in that arrangement. If only a subset qualifies, establish whether the authority can release it separately and what obligation remains for the rest. The options may include release, trial, withholding, rejection or obtaining a missing result.
2. **Establish the configuration and effectivity.** Use a compatible `SYSE.13` result or qualified direct sources for the descriptions,
   configurations, units, sites, intervals and conditions relevant to this release. When a necessary correspondence
   is missing, identify it and the release decision it prevents.
3. **Separate the trigger from the candidate.** Record the event that prompted reconsideration—for example, a request, criticism,
   incident, opportunity, or source change—with its evidence status. Describe viable change candidates separately.
   Keep the unchanged-System option when viable; treat deferral as a decision to await an event or obtain another
   result.
4. **Trace the consequences that bear on the choice or its conditions.** Identify the affected Systems and relations,
   descriptions, realization or integration Work, provider and receiving Agents, obligations, supporting evidence and reversibility
   that matter to this decision. Use files, team names and links to find the relevant records or Agents, then establish
   the engineering objects and relations affected.
5. **Name the Agents and governing relations.** Identify the deciding and receiving Agents, who grants any required permission, and
   who is assigned to perform later Work when that assignment bears on this decision. State the applicable assignments,
   authority, permissions, conflicts of interest and abstention conditions separately.
6. **Qualify the evidence.** Connect each evidence result—for example, a test result, model evaluation, trial
   observation, specialist result, or assurance result—to the claims, configurations, conditions, and uses it
   supports. When a relied-on source changed, use a compatible `SYSE.19` result or reopen the affected claim
   directly.
7. **Compare the current options.** Hold the option set and comparison basis stable long enough to choose.
   State protected characteristics, acceptable losses and any material uncertainty. Use `C.11` for
   the choice. If further evidence could change the choice or its warranted use, compare the cost
   of obtaining the next feasible observation with its value for the decision. Retain any inquiry judgement or limitation the decision
   or recipient needs. Choosing to proceed on the available evidence requires no new observation proposal or inquiry record.
8. **State and return the release decision.** Name the selected disposition, subject, effectivity, conditions, evidence, authority and
   any required permissions. State the permitted next Work, any unresolved risks or withheld scope, and what would reopen the decision.
   Apply the acceptance rule to its own subject. An attainable breach refutes an all-conditions guarantee. A required document absent at the deadline can warrant return while physical performance remains open. Check supported units or conditions against their other technical and permission requirements before disposing of a narrower offer.
9. **Connect later realization.** Establish the configuration and properties on which the next use depends. A recipient who can open the released archive and verify its contents may have enough evidence for that use while the identity of its installer remains unknown. An account of implementation or integration as performed Work also needs the performing Agent, dated Work, Method and actual transformation. Update the descriptions and notify the recipients affected by what was established.

A release for realization can occur before implementation; release to service can depend on later implementation
and observation; emergency containment Work can precede a full technical choice under its own authority. The case
must state which dependencies and timing apply.

#### SYSE.14:4.2 - Record the Result

| Field | Required content |
| --- | --- |
| release question | Release subject and kind, deciding Agent, receiving Work or use, current options, interval, and conditions. |
| configuration and effectivity | The relevant descriptions, configurations, supporting evidence and the subjects and conditions covered. For an existing System, identify the actual units, constituents, obtaining relations and characteristic values on which the decision relies. For release before realization, identify the intended configurations to which the description or package will apply. |
| trigger, candidates, and consequences | Trigger with epistemic status; viable candidates; affected Systems, interfaces, Work, obligations, downstream consequences, reversibility, and retained alternatives. |
| Agents, authority, and permissions | Deciding and receiving Agents and the relation that grants authority for this decision. For any required permission, identify its grantor, holder, subject, scope and interval. State the relevant assignments, including the performer of any assigned later Work, and any conflicts of interest or abstention conditions. |
| evidence and choice | Evidence for each claim, with provenance and limits; comparison basis; selected disposition; accepted losses; any material uncertainty; the judgement or limitation from a live inquiry alternative when needed by this decision or its recipient. |
| decision and continuation | Released, narrowed, trial-only, withheld, rejected or probe-again result; next Work allowed by the governing rules and permissions; any withheld scope or blockers; and the conditions for withdrawal or reconsideration. |
| later realization, when relevant | Observed configuration and properties, affected descriptions, recipients and known gaps. For a claim about performed implementation or integration, include the performing Agent, dated Work, Method and actual transformation. |

The result may be carried, for example, by an issue record, release note, model view, linked engineering
records, or generated report. The decision keeps its identity and grounds across those carriers; authority,
permission, performed Work, and actual configuration remain separately established.

#### SYSE.14:4.3 - What Changes in Practice

Engineers stop treating *approved*, *merged*, *passed*, and *released* as interchangeable completion signals.
They can release a supported subset of units and add independent evidence or permission where the change's
consequences require it.

The receiving Agent can tell whether to perform the named Work, use the released configuration, obtain a
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

The original request asked for release to all ten units. The engineering team retained three options: withhold
service release on the changed units; admit S006–S008 to monitored service; or extend a trial to S006–S010.
The last option failed the stated calibration-evidence threshold. Withholding avoids exposure to the
changed configuration but keeps the three otherwise eligible units out of service for now.

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

Suppose the order requires an applicable calibration certificate by noon for each unit. S005 still has none at noon: the board can return S005 under that rule while leaving its actual accuracy open. A qualified reading outside the protected response under an admitted condition would instead refute an all-conditions guarantee for S005. Either finding leaves the bounded, authorized decision on S006–S008 in force while its own premises hold.

The engineer adds the service decision to the existing change account and links the unit evidence and separate
permission. For this single subset release, the team chooses that checked addition over configuring a workflow
to maintain the same connections automatically. It accepts manual revalidation after an affected record changes.
Recurring releases could justify the maintained workflow; either approach needs the same choice, evidence and
permission. Neither approval of the software package nor its installation record answers this service question.

The decision can supply evidence to `SYSE.4` for the claims, units and interval it covers. The assurance judgement can support reliance within that scope,
identify an unsupported claim or return a blocker. It needs grounds beyond the fact that release was granted.

**When the full pattern is unnecessary.** A reversible internal script has one known configuration,
no physical effectivity question, and an established deployment Method that supplies the
needed choice, evidence, permission, Work and rollback results. Use those results for this
deployment.

### SYSE.14:6 - Bias Annotation

A document-control Method can turn every change into a long approval chain. A software workflow can treat a
green pipeline result as universal release authority. Scale scrutiny to consequence and reversibility while keeping
actual Systems, descriptions, evidence, authority, permission, and performed Work distinct.

Official procedures, vendor workflow labels and declared conformance can establish what was recorded or what a procedure requires.
Claims about what participants did, how effective it was or what configuration resulted need evidence for that claim. When broader
field evidence is unavailable, give any expert judgement and its epistemic status.

### SYSE.14:7 - Conformance Checklist

- [ ] The scope and authority of the decision cover the uses in the proposed release, including any required joint operation. A narrower disposition states which work it permits and what remains outstanding.
- [ ] The configuration basis covers the release subject, its applicable conditions and the same next-use decision, including the actual units when the release concerns them.
- [ ] The decision uses each approval or completion status only for what it establishes. Any required permission,
      claimed installation or resulting configuration has its own support.
- [ ] Consequence tracing reaches affected Systems and direct relations, not only files, departments, or links.
- [ ] Every relied-on authority, permission, and evidence result has the subject, scope, interval, and source
      needed by the decision.
- [ ] The comparison basis, selected disposition, retained alternatives, acceptable losses and any material
      uncertainty are recoverable. Any live inquiry alternative is resolved sufficiently for the choice, with
      the judgement or limitation needed by the decision or its recipient; inactive inquiry adds no entry.
- [ ] Any claimed implementation identifies the performing Agent, dated Work, Method, actual transformation,
      resulting configuration, and evidence.
- [ ] The disposition identifies its grounds, whether a technical limit was exceeded, a required acceptance condition was unmet, or a narrower use qualifies. It states the permitted next Work and conditions for withdrawal or reconsideration.

### SYSE.14:8 - Common Failures and Repairs

These errors can change which action is permitted next.

| Failure | Repair |
| --- | --- |
| Request equals decision | Keep the request as a trigger and compare viable change options. |
| Signed form supplies authority | Identify the deciding Agent and the authority relation for this decision. |
| Gate pass equals release | Use the gate result as one premise and state the release subject, kind, and effectivity separately. |
| Release equals implementation | Identify performed Work and actual transformation, or state that they remain future. |
| Updated status equals actual configuration | Obtain evidence about the identified units and keep the status as a claim. |
| Apply one software pipeline to every engineered System | Select review, automation, assurance and any required permission for the consequences, reversibility, actual or intended System and use under consideration. When the question is acceptance by a creator, apply those criteria to the activity or use that creator is accepting. |
| All units inherit one release | Name supported units and conditions; narrow or withhold the rest. |
| A changed source reopens everything | Trace the changed claim and reconsider only the affected decisions. |

### SYSE.14:9 - Consequences

Release speed and scrutiny can vary with consequence without losing accountability. Implementation, operation,
maintenance and assurance receive a decision that names configuration, effectivity, evidence, authority and
next Work. Related physical and software changes can share one release case while their Work retains its own cadences
and evidence.

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

An adequate professional release process or qualified software-delivery path can supply the bounded decision.
A competent configuration-management process can already relate affected-function contributions,
implementation costs, dependencies, effectivity and release. A software path can combine peer review, automated
feedback, recorded authorization and additional scrutiny for material risk. Use the result directly when
it covers this release subject and next use; construct a missing connection only when that decision needs it
(:4).

For the controllers in :5, installation and package approval leave a separate question:
may these units enter monitored service? Steps 2 and 5–8 connect unit-qualified evidence
and independent permission to the board's comparison. The stated priority, evidence
and accepted monitoring burden explain why the board prefers monitored service to
withholding. Eligibility alone leaves that preference unresolved.

A workflow can maintain the connections needed for the bounded decision. Compare it with
a checked addition to existing records for the same service question and assurance needs.
The team accepts manual checking and revalidation for one subset release. An integrated workflow
can become preferable when repeated releases justify its construction and upkeep.
Both paths must meet the same evidence and permission requirements. This example illustrates the trade-off; it supplies no measured comparison
of their performance or general basis for preferring either path.

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
  connects the relevant results for one engineering release.
- `C.2.1`, `E.17`, and `E.24.PUB` keep change descriptions, decision epistemes, publications, forms, and carriers
  distinct from the changed System and performed Work.
- `SYSE.13` can identify configuration and effectivity for this release directly or through a supported correspondence. Permission and release require the applicable governing decisions.
- A compatible `SYSE.19` result supplies revision consequences only for decisions that relied on the changed source. Use it before a release
  when the change bears on that choice, or return to an existing release when a later or newly discovered change bears on its grounds.
- An operating or maintenance result can establish restored function for a particular unit. Use it for another configuration or condition when the relied-on property carries across on a stated basis; use `SYSE.14` and the governing authority for release.
- `SYSE.14` can supply bounded evidence to `SYSE.4` for the same release question and evidence window. Use a matching assurance judgement where it already exists; when one is needed,
  obtain it through the applicable assurance work.
- Application moves—such as software deployment, electrical energization, medical-device release, ship
  alteration, building commissioning, or manufacturing release—may specialize the Method because their project
  Systems-of-interest, permissions, evidence, and effectivity differ.

### SYSE.14:End
