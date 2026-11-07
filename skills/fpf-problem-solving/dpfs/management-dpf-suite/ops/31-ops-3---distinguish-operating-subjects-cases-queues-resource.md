## OPS.3 - Distinguish Operating Subjects, Cases, Queues, Resources, and Records

> **Status:** Stable


### OPS.3:0 - Use This When

Use this pattern when one card, ticket, order, object identifier, case file, event row, or status label is being asked to stand for several different things. Enter when a measure cannot say what it measures, a queue cannot say what waits, an incident record is treated as the incident, a resource is treated as its availability, or two views cannot agree because they identify their subjects differently.

The first useful move is to resolve one decision-bearing subject and the claim needed about it. An existing account or a short explanation can carry this result:

> Subject `S` has identity condition `I`. The decision-bearing claim `Q` about `S` and its relations `R` is qualified for time or horizon `T` and supported by `E`. State a formal kind, represented view, governing rule or missing condition when the receiving use depends on it.

Repeat only for items whose distinction changes the decision. The result is a small operating-subject account, not a universal data model.

Recognition is cheap: enter when a record label, metric denominator, queue item, or “work object” has several plausible referents. Assurance is claim-specific: entity kinds, Work, relations, commitments, state, evidence, event occurrence, control participation, resource availability, and representation each retain their FPF or specialist tests.

Do not use OPS.3 to model every object in the operation, redesign a database, declare an event log complete, infer a case from a ticket, or create a catch-all `operational object` kind. If an existing subject pattern already answers the identity or relation question, use it and record only the Operations correspondence needed here.

#### OPS.3:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| operating subject | The exact entity, relation, case subject, material, service, account, or other concern whose state or relation changes the operating decision. This is a reading position, not a new universal kind. |
| case | One bounded continuing Work situation organized around a named subject, commitments, current facts, evidence, authority, permissible next Work, and closure conditions. The case is neither its file nor every Work item within it. |
| Work occurrence | Actual dated Work admitted through its governing pattern. A ticket, plan, or event record does not establish that Work occurred. |
| Work item | A bounded item admitted to a selected workflow or coordination account with stated start, finish, subject/result relation, and receiving use. |
| queue membership | An obtaining relation placing one eligible item in one named waiting or service order under a policy and time window. A column or list is a representation. |
| buffer membership | An obtaining relation to a bounded protective or coordination reserve with purpose, policy, extent, and receiving use. It is not inferred from spare inventory or a board column. |
| resource relation | The exact availability, access, consumption, support, allocation, or other relation through which a System, capability, material, information, time, or condition is used by Work. The resource and relation remain distinct. |
| event | An occurrence or change under its subject rule and time boundary. An event record or timestamp is evidence about it, not the event by identity. |
| record or trace | A claim-bearing episteme about subjects, Work, events, relations, or decisions, recorded on an identified carrier. Its claims have stated sources and scope limits. |
| state claim | A qualified claim about one subject at a stated time or horizon with provenance, uncertainty and conditions; include authority where the claimed state or receiving action depends on it. A status label is one possible representation. |
| control participant meaning | Observer, controller, plant or supervisor as the participant meaning in an actual control relation. Qualify a selected control structure when that claim is needed. The label does not establish that the relation obtains. |
| operating-subject account | The smallest relation-specific set of identities, direct relations, records, state claims, and explicit gaps needed by the current operating decision. |

### OPS.3:1 - Problem Frame

Operational tools compress the world so people can coordinate. That compression is useful until one row is read as the customer, order, case, Work, queue position, resource claim, event history, and current state at once. Object-centric and case-responsive approaches repair parts of this problem, but their own records and identifiers still need receiving-use limits.

The practitioner needs a small account that restores identity and obtaining relations before measures and policies are applied. The account can use several records and views while keeping the world-side subjects and claim-bearing epistemes distinct.

### OPS.3:2 - Problem

When identities collapse, flow measures acquire false denominators, cases close while the conditions they were meant to resolve persist, queue policies compare unlike items, resources are double-counted, and events are reconstructed into Work that may never have occurred. A record update can then masquerade as an operational change.

An unnecessarily broad modeling effort can delay the current decision while still omitting the few direct relations it needs. Tool categories require the same check against the subjects and relations they claim to represent.

### OPS.3:3 - Forces

| Force | Tension |
| --- | --- |
| Coordination shorthand | One ticket or identifier is affordable, while it can hide several subjects and relations. |
| Measurement | Stable units enable comparison, while identity changes and joins can silently change the measured population. |
| Several records | Logs, trackers, files, and physical observations can complement one another, while their claims may conflict. |
| Runtime change | Cases and subjects evolve, while records arrive late or use stale identity rules. |
| Resource scarcity | Capacity decisions need resource relations, while people and machines must not be reduced to scalar capacity. |
| Minimality | The operation needs decisive distinctions now, while a complete domain model is expensive and brittle. |

### OPS.3:4 - Solution

Build the smallest operating-subject account that preserves exact identities, obtaining relations, time, evidence, and representation for the current decision. Start from the subjects and views selected by OPS.1 and OPS.2; add no item merely because a source schema contains it.

#### OPS.3:4.1 - Pattern-Use Unfolding

1. **Name the receiving decision and suspected compression.** Name the two items being treated as the same, the measure, queue, case continuation, commitment, control question, or account use that depends on that identity assumption, and what fails if the assumption is false.
2. **Select the primary subject.** Name the entity or relation whose state changes action and its identity condition across time. Use its direct subject pattern when kind membership is load-bearing.
3. **Separate case, Work, and Work item.** Name the case subject and closure conditions; admit actual Work independently; define each coordination Work item by start, finish, subject/result relation, and receiving use.
4. **Recover queue and buffer relations.** Name eligible item, queue or buffer, membership interval, order or protective purpose, policy, resource/service relation, and evidence. A drawn position creates none of these facts.
5. **Recover resources through exact relations.** Distinguish the System, capability, material, information, access condition, or time from availability, access, allocation, support, consumption, or other obtaining relation. Preserve authority and human-condition questions.
6. **Separate events, records, and state claims.** Identify the occurrence or changed subject and the records supporting it. For a consequential time, distinguish occurrence, observation, receipt and later correction; recover the clock and field meaning actually used. A later upload does not move the occurrence or reset its waiting time. State the supported claim and its uncertainty. Event order alone does not establish performed Work.
7. **Recover commitments and direct relations.** Use `A.6.REL` or the direct governor for each relied-on relation. Keep promise, obligation, fulfilment, responsibility, authority, assignment, and evidence distinct.
8. **Apply the control branch only when selected.** Preserve actual Systems or holons and direct observation, actuation, reference, supervision, and feedback relations. Treat observer, controller, plant, and supervisor as relation-specific meanings. Use `B.2.5` only when both observation/report and returned influence/constraint sides obtain.
9. **Reconcile records by subject and claim, not by row.** When a relation or timestamp is disputed, identify the source that can settle that particular meaning and the person authorized to correct its account. Preserve the original observation and explain the correction. Recompute only the state, elapsed time, queue membership or other decision that used the defective relation. Keep an unresolved association unusable for that inference; do not guess a replacement. Retain independently supported claims and ongoing work. A correction to a record does not itself change permission or undo performed Work.
10. **Stop at the smallest sufficient account.** Return the subjects, relations, state claims and support needed by the decision, with any unresolved condition. Use OPS.4 when participants need to maintain or share the current account; otherwise the resolved identity or relation can finish this use. Identify revision conditions when the result will be reused. Leave unrelated objects outside.

#### OPS.3:4.2 - Carry the Result

Preserve the content needed by the selected question. Use the existing record or explain the result directly; create or maintain a record only when coordination, later reliance or another governing requirement needs it.

| Result position | Content when relevant to the receiving use |
| --- | --- |
| use boundary | User, decision, horizon, suspected compression, and useful stop. |
| subjects and identity | Exact primary and related subjects, governing kinds or predicates, identity conditions, and unresolved referents. |
| cases and Work | Case subject and closure; actual Work basis; Work-item start/finish, subject/result relation, and receiving use. |
| queue, buffer, and resource relations | Participants, membership or access interval, purpose/policy, order or extent, direct relation, and evidence. |
| events and records | Occurrences, claim-bearing records and carriers, source, scope, time, uncertainty, and non-admissible inferences. |
| state and commitments | Qualified state claims, commitment relations, provenance, authority, conflicts, and currentness. |
| control relations, when the control branch is selected | The actual participants and decision-bearing observation, actuation, reference or supervision relations. Omit this row for an account that makes no control claim. |
| continuation | Any unresolved condition or needed account maintenance; revision conditions for a result that will be reused. |

#### OPS.3:4.3 - What Changes in Practice

Measures, queues, and dashboards acquire named subjects and relation semantics. A card move updates the record. Separately establish any change in the subject or relation that the updated record represents. Teams can keep several tools while knowing which claim each can support and where a missing identity or relation blocks action.

### OPS.3:5 - Archetypal Grounding — PumpWorks Subject Account

The weekly release decision initially sees four cards and a rig calendar. OPS.3 expands only the distinctions that change action:

| Visible item | Recovered subject or relation | Record boundary |
| --- | --- | --- |
| `ReleaseCandidate-R42` card | A release-candidate subject and its candidate contents, required evidence results, release Work items, and receiving release decision. | The card and commit identifiers are records; moving the card does not change deployed field state or satisfy the release commitment. |
| `FieldIncident-I73` ticket | A case organized around `FieldPumpInstallation-P4`, reported symptoms, service commitments, evidence, authority, permissible next Work, and closure conditions. | Ticket closure does not establish restored field condition or fulfilled service. |
| `SafetyQuestion-S19` issue | A question episteme, related evidence needs, specialist safety decision, and any Work items created to obtain that result. | A red label is neither a safety state nor authority to accept risk. |
| `ProviderChange-P8` epic | A time-bounded change subject with provider relations, access conditions, project WorkPlan content, affected release cases, and decisions. | The epic does not make the provider part of PumpWorks or prove performed migration Work. |
| test-rig booking row | Queue membership of an exact eligible request for resource relation to `TestRig-2`, with interval, order/policy, access condition, and status evidence. | The booking row records planned access. Establish request eligibility, allocation authority, performed test Work, and test completion separately. |

Records remain distinct: ticket, trace, source commit, build result, test result, service log, field-engineer report, telemetry record, and release decision each support bounded claims. A multi-object event record may relate one event to several subjects, but it does not identify those subjects with one case or prove the represented Work.

Consider a later, constructed PumpWorks reconciliation. An imported test event L17 has been associated with both R41 and R42 because their records share a release folder. The board consequently removes R42's test request from the ready queue and reports “tested at 10:20.” That conclusion consumes two unsupported assumptions: that L17 tested R42, and that 10:20 is test completion rather than receipt of the message.

The lab's signed execution record identifies the tested build as R41 and completion at 09:50; the intake trace identifies 10:20 as message receipt. The lab engineer confirms those meanings, and the authorized record maintainer replaces the false R42 association with the supported R41 association while retaining the original import and the correction's basis. R42's completion claim is withdrawn. After confirming that R42's independently established inputs and permission still hold, the scheduler restores its waiting eligibility and the priority justified by the current queue rule and original waiting history. Correction time does not restart its age or revoke work already permitted or performed on other requests. L17 supports the stated R41 test result, not R41's wider release or field condition.

S19's unresolved safety question, I73's field observations and the independently permitted work on them remain as they were. The correction reaches OPS.4's R42 state and OPS.8's test population because those uses consumed the bad link; it does not invalidate the entire operating account. If the execution record cannot identify the tested build, neither R41 nor R42 acquires test completion from L17. Return the missing applicability result to the lab and keep any otherwise permissible work running. This small reconciliation is sufficient when those are the only affected uses; a full data-model migration would add cost without changing the decision.

For the product-side control view, `FieldPumpInstallation-P4`, `FieldTelemetryObserver-O4`, `DeployedController-C17`, and `FieldModeSupervisor-S1` retain their relation-specific meanings. For operating supervision, `ReleaseSupervisorTeam-S2` is an admitted acting System only where supported and the two-sided report/constraint relation to `PumpWorks-ControlServiceOps` is recorded only if both sides obtain. The diagram, participants, relations, state claims, and operating account remain distinct.

The result supplies OPS.4 with exact subjects, records, current claims, conflicts, permissions and refresh needs. Reopen only the affected identity or relation when a release candidate is superseded, an incident splits or merges under an explicit rule, a queue membership changes, a record source becomes stale, or a claimed control relation loses one side.

### OPS.3:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| card-identity bias | Card, case, Work item, and subject become one thing. | State separate identities and direct relations. |
| case-file bias | The file becomes the continuing case. | Name the subject, commitments, current facts, permissible Work, and closure conditions. |
| queue-container bias | A column or list is treated as an obtaining queue. | Recover membership, order/service relation, policy, interval, and evidence. |
| resource-scalar bias | A person, machine, or capability is reduced to available hours. | Preserve the subject and exact access, support, allocation, or use relation. |
| event-log realism | A log is treated as complete performed Work. | Preserve source limits and admit Work independently. |
| object-centric collapse | Multi-object linkage is read as one universal case or process. | Keep subjects, event relations, records, views, and receiving uses distinct. |
| control-role reification | Observer, controller, plant, or supervisor labels become permanent kinds. | Recover participant meanings in exact obtaining relations. |

### OPS.3:7 - Conformance Checklist

- [ ] The account begins from one receiving decision and a named suspected compression.
- [ ] Each decision-bearing subject has an identity condition and direct subject governor when needed.
- [ ] Case, actual Work, Work item, queue membership, buffer membership, resource, event, record, and state claim remain distinct.
- [ ] Work items state start, finish, subject/result relation, and receiving use.
- [ ] Queue, buffer, and resource claims name exact participants, purpose or policy, interval, and obtaining relation.
- [ ] A relied-on record preserves its source, subject, claim scope, time and uncertainty, and any inference limit material to the receiving use.
- [ ] Direct relations use current governors; a representation or co-occurrence creates none.
- [ ] Control participants and two-sided feedback are recorded only where actual relations obtain.
- [ ] The result is the smallest account sufficient for the decision, with any unresolved condition and the revision conditions needed for reuse.

### OPS.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “One issue equals one unit of value.” | Name the represented subject, Work item, result relation, identity rule, and receiving decision. |
| “The customer is in the queue.” | State whether the queued participant is a request, case, Work item, physical subject, or another exact entity. |
| “The resource is 80% utilized.” | Identify the resource subject, availability/allocation/use relation, time window, Work, and decision. |
| “The event log shows the process.” | State the logged events, object relations, source coverage, reconstruction rule, and missing Work evidence. |
| “Status Done means fulfilled.” | Recover the commitment, supplied result, acceptance or fulfilment evidence, and authority separately. |
| “The dashboard closes the feedback loop.” | Recover both in-life relation sides and keep the display, claims, rates, and proof separate. |

### OPS.3:9 - Consequences

The pattern produces trustworthy units for measurement and policy and makes cross-view reconciliation possible. It also localizes repairs: a stale record source, changed identity rule, missing relation, or uncertain state claim can reopen without rebuilding the whole operating account.

The cost is refusing convenient conflations. Some metrics and historical analyses become unusable because their unit identity or source coverage cannot be recovered. That loss is explicit rather than hidden in a precise-looking chart.

### OPS.3:10 - Rationale

Operations decisions act on subjects and obtaining relations, while coordination normally uses records and representations. Keeping those layers distinct preserves practical speed without allowing tool schemas to decide ontology. A minimal relation-specific account is enough when it names what can change the decision and what remains unsupported.

### OPS.3:11 - SoTA-Echoing

The question is which subjects, relations and times must be recovered before an operating decision can trust its records. A capable object-centric account already relates events to several objects, retains histories and distinguishes relation meanings. OPS adapts that contribution.

[OCEL](https://www.ocel-standard.org/specification/overview/) supplies an exchange model for that account. The [2026 object-centric process management manifesto](https://publications.rwth-aachen.de/record/1036372/files/1036372.pdf), particularly §2.3 and §3, distinguishes execution data from their representations and identifies changing relations as a limitation of OCEL 2.0. The [2026 object-centric data-quality study](https://link.springer.com/article/10.1007/s44311-026-00043-x), “Relationship-based quality issues” and its practitioner cases, shows why a well-formed multi-object log can still have wrong or insufficiently qualified links and changing timestamp meanings. These ground the correction in steps 6 and 9 of OPS.3:4.1 and in OPS.3:5.

In the L17 choice, a competent data-quality procedure that already checks the build, timestamp meaning, correction provenance and affected consumers is sufficient. Use it unchanged. Where it repairs the log but leaves the operating consequence undecided, OPS adds the narrow return: withdraw the unsupported R42 completion, recompute only dependent membership and age, and retain the independently supported work. The extra cost is consulting the responsible source and following the faulty relation into its actual consumers. Recreating every object or copying all histories into a second account is unnecessary. An unresolved relation can block one inference without blocking the rest of the operation.

Current FPF `A.6.REL` governs the direct relations relied on; distinguish relation occurrences only when the receiving use must tell repeated occurrences apart. `C.2.1` governs claim-bearing accounts and `B.2.5` the selected two-sided supervision relation. Subject-specific identity and specialist evidence remain with their direct governors. [CMMN 1.1](https://www.omg.org/spec/CMMN/1.1/PDF), [DCR](https://doi.org/10.4204/EPTCS.69.5) and DEMO's bounded commitment/coordination account retain their case-planning and relation contributions; none makes record closure proof of physical completion. Integrated network descriptions can retain unlike coupled relations without identifying their subjects.

Reopen this choice when the record's meaning, relation history, clock, consumer or correction authority changes, or when the incumbent supplies the same bounded correction and operating return at lower effort. Use specialist data engineering for a larger migration; no universal Operations schema follows.

### OPS.3:12 - Relations

- `OPS.1` supplies operating scope, subject candidates, commitments, units, and evidence questions. `OPS.2` supplies selected views, grains, correspondences, and conditional control questions.
- `A.6.REL` and direct subject patterns govern obtaining relations and identities; `C.2.1` governs claim-bearing accounts; `B.2.5` and `C.30.LCA` govern the conditional control relation/view boundary.
- `OPS.4` consumes exact subjects, direct relations, records, state claims, provenance, conflicts, permissions, and gaps.
- `OPS.8`, `OPS.9`, `OPS.10`, `OPS.11`, `OPS.12`, and `OPS.18` later consume the exact subjects and relations whose queue, constraint, capacity, interaction, human-condition, or quality claim is current.
- Data engineering, process mining, product engineering, safety, finance, law, medicine, and other specialists retain their schemas, inference Methods, evidence, and authority.

### OPS.3:End
