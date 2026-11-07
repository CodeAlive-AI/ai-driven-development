## OPS.5 - Admit Work and Limit Starts

> **Status:** Stable


### OPS.5:0 - Use This When

Use this pattern when exact eligible operating demand may be explicitly started or committed now, but the operating System cannot honestly start everything that appears ready. Typical cues are “pull the next item”, “approve this case”, “the card is top priority”, “the agent is free”, “the rig has an opening”, or “we already selected it” without a current admission decision, start permission, or explicit start limit.

The first useful result is one bounded admission account:

> For eligible demand `D` serving operating result or commitment `R`, under criteria and non-negotiable conditions `K`, explicit-start limit `L`, deciding authority `A`, configuration and horizon `H`, each considered item is `admitted`, `deferred`, `rejected`, or `returned`; an admitted item has effective start conditions and an authorized starter where one exists; residual demand and the next review or return remain visible.

Recognition asks whether this demand may enter now. Assurance establishes its admission criteria, start permission and effective bound; any later performance or fulfilment claim needs its own evidence.

Do not use OPS.5 to design a queue or buffer policy, identify or exploit the current constraint, size capacity under variability, coordinate interacting structures, or make a whole-service commitment credible. Return those questions to `OPS.8`–`OPS.13` when their results are available, or to a qualified direct source. If the current problem is continuing an already admitted case after facts changed, use `OPS.6`. If age, dependency, risk, or consequence may revise priority or an existing commitment, use `OPS.7`.

#### OPS.5:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| eligible demand | An exact demand item, such as a request, need, condition, case, or candidate Work item, that may be considered for current admission. Identify the demand claim and the subject it concerns separately. Eligibility makes it a candidate for this decision, not a permitted start. |
| option or request | A possible demand item presented for consideration. Its presence in a list or account creates no right to admission. |
| admission decision | A bounded decision about whether exact demand may enter the selected current coordination account under stated criteria, limits, horizon, and authority. |
| admitted item | Eligible demand whose admission conditions obtain for the stated configuration and horizon. Admission permits a further start decision under its conditions; it does not establish start or result. |
| deferred item | Demand not admitted now, with the observation, condition, horizon, or changed fact that would make reconsideration useful. |
| rejected item | Demand declined for this operating use, with its reason and any receiving return that another owner can answer. |
| returned item | Demand for which a named missing, stale, unsupported, or externally owned condition prevents this admission decision. |
| start permission | An obtaining permission or authorization for the admitted matter under effective conditions. A comparison or selected answer is not permission unless the deciding System also has and exercises the required authority. |
| explicit-start limit | A stated bound on what may be started now for this operating use. It is not a universal WIP number, capacity model, queue policy, or constraint-buffer design. |
| commitment | A promise or obligation with parties, content, conditions, horizon, authority, and status. Admission can rely on or create a bounded commitment only where the relevant authority is present. |
| authorized starter | The System permitted to initiate the admitted Work under the effective conditions. Responsibility, capability, availability, and permission remain separate. |
| Work occurrence | Dated Work whose occurrence is established from performance evidence, independently of the demand-admission decision. A card move, approval, selected item, plan, agent invocation, or generated artifact does not establish that Work occurred. |
| residual demand | Every considered or still-relevant demand item not in the admitted set, with enough identity and disposition to avoid hidden starts or silent loss. |
| admission result | The dispositions, reasons, conditions, authority, horizon, starter relations, residual demand, and next review or return that make the admission decision usable. |

### OPS.5:1 - Problem Frame

Continuing operation usually receives more apparent demand than it can honestly start. Requests arrive through customers, incidents, clinical cases, release candidates, providers, planned changes, automated agents, and internal commitments. Each item may be valuable, urgent, visible, or technically ready while still lacking the identity, evidence, permission, access, authority, or explicit-start condition required now.

The practical problem is not merely choosing the highest-ranked item. It is deciding which exact demand may cross into current operating coordination without hiding residual demand or treating selection alone as evidence that Work occurred.

### OPS.5:2 - Problem

Boards and intake systems compress unlike truth states. “Ready”, “selected”, “approved”, “assigned”, and “in progress” become interchangeable labels. A high priority is treated as permission; an available performer as authority; a scheduled slot as capacity; a generated change as started Work; and an admission decision as a fulfilled commitment.

The opposite failure keeps every item nominally open. Nothing is explicitly rejected, deferred, or returned, so the operation accumulates hidden commitments and starts. Practitioners cannot recover which demand was considered, why it did not enter, or what would justify another look.

### OPS.5:3 - Forces

| Force | Tension |
| --- | --- |
| responsiveness versus truthful starts | Delay can harm service, but premature starts create hidden Work, interruption, or unsafe continuation. |
| common intake versus unlike subjects | A shared account aids coordination, but incidents, patients, release candidates, provider changes, and rig requests retain different identities and conditions. |
| comparison versus direct rule | Several live alternatives may need choice, while mandatory or recognition-based conditions should not be converted into an artificial option contest. |
| local limit versus wider policy | One explicit-start bound can close the current decision without claiming a complete queue, capacity, or constraint Method. |
| visibility versus authority | Making demand and evidence visible helps, but neither visibility nor rank grants permission or commitment authority. |
| fast admission versus adequate evidence | A short-horizon answer is useful only if evidence currentness, conditions, and reopen triggers remain explicit. |
| focus versus residual demand | A bounded admitted set reduces active burden, but deferred, rejected, and returned demand must not disappear. |

### OPS.5:4 - Solution

#### OPS.5:4.1 - Recover only the action-changing operating inputs

Name the deciding operating System, receiving result or commitment, configuration, and horizon. Reuse matching current `OPS.2`, `OPS.3`, and `OPS.4` results only where the selected coordination form, exact subjects and relations, current claims, uncertainty, permissions, commitments, or gaps can change admission. If an input is stale, mismatched, or absent, repair or return that exact blocker; do not reconstruct the whole operation by default.

#### OPS.5:4.2 - Name each exact demand item and its proposed use

For every item under consideration, state the demand subject, claimant or source, proposed operating result, relevant commitment, and why admission is current. Keep a request, option, candidate Work item, admitted item, commitment, start permission, and performed Work separate even when one record represents several of them.

#### OPS.5:4.3 - State criteria, non-negotiable conditions, and the explicit-start limit

Record the conditions that can change the admission decision. Test exact identity; relevant readiness and evidence; required authority or permission; intended receiving use; safety, legal, clinical, security, or other specialist returns; performer and access conditions; current commitments; and the capacity, resource access, bounded concurrency, or explicit-start limit that matters now.

Judge readiness for the proposed consuming operation, not for every eventual use. `OPS.8:4.2` supplies receiver-ready work; `OPS.13:4.2` connects preparation to a promised result. Recover the applicable prerequisites and the person who can confirm them. Name the start bound's unit, interval and counting rule, including how safe stops and suspended work count. A supplied justified bound can be applied here; deriving its value is a capacity or policy question.

Some conditions are mandatory, some admit qualified comparison, and some require a return to another owner.

#### OPS.5:4.4 - Choose only where a real choice exists

When a direct domain rule, mandatory condition, or recognition branch gives the answer, apply it and record the basis. When several live admissible alternatives genuinely require comparison, form a stable current OptionSet and comparison basis and use `C.11`. If the options or comparison facts are insufficient, choose a bounded probe only when it can change the decision, or return the missing condition.

#### OPS.5:4.5 - Give every item a usable disposition

Return each considered item as:

- **admitted**, with reason, effective conditions and horizon, governing authority, authorized starter where established, and next review;
- **deferred**, with the condition, observation, horizon, or changed fact that makes reconsideration useful;
- **rejected**, with the reason and receiving return where another owner can answer the need; or
- **returned**, with the exact missing or externally owned result, what it blocks, safe stop, and retry condition.

Keep the residual demand visible. Record no start merely because the item is admitted.

#### OPS.5:4.6 - Close the local decision and expose wider returns

State the admitted set, current explicit-start limit, unresolved or residual demand, next review, and the facts that reopen this admission. If the answer now depends on queue ordering, buffer design, a current constraint, capacity under variability, interacting structures, credible whole-service commitments, clinical triage, safety acceptance, release, law, finance, or another specialist result, return to that owner without filling the gap locally.

### OPS.5:5 - Archetypal Grounding — Three Admission Replays

#### OPS.5:5.1 - PumpWorks controller service

The following observations and permissions are constructed case inputs. At 09:00, PumpWorks has an established limit of **two active engineering work packages** for the 09:00–11:00 window. The staffing owner has justified this bound from available performers and protected recovery work; OPS.5 applies it without deriving a universal WIP value. A package counts from actual start until completion or a documented safe stop. Waiting demand is not counted as active. T8 is already running with engineer E17 until its expected safe completion at 09:30, so one slot is free.

| Proposed work | Obtaining conditions at 09:00 | Disposition and next action |
| --- | --- | --- |
| I73-D: inspect the captured incident logs | Exact installation and log identity confirmed; engineer E18 available; incident lead authorizes read-only diagnosis until 11:00; local copies and diagnostic procedure ready. | Admit I73-D under the incident-order exception in OPS.2:5.2. E18 starts at 09:05. With T8, there are now two active packages. No live setting change or release is permitted. |
| R42-T9: final laboratory validation | Lab testing is permitted independently of field release, but the signed fixture check is missing and the rig is occupied by T8. | Defer until the fixture check and rig access obtain; recheck at 09:40. An empty active slot alone is insufficient. |
| S19: resolve the safety question | The operating coordinator is not the safety authority. | Return the exact question and supporting material to the safety owner. Release remains blocked pending the safety decision; unrelated permitted diagnosis may continue. |
| P8-P: provider preparation | Inputs and permission exist, but it competes for E18; the resource owner confirms an afternoon review can preserve its existing obligation. | Defer to 13:00 rather than silently remove it from demand. Reopen earlier if that obligation or E18's availability changes. |

At 09:25 E18 safely completes the bounded log inspection, as developed in OPS.6:5.1. One active slot is freed, but the incident case is not resolved. At 09:30 T8 completes. At 09:40 the fixture owner supplies the missing signed check; the rig owner and E17 confirm access, and the coordinator admits R42-T9. E17 starts its permitted laboratory procedure. This is a new bounded admission, not permission for field release.

At 09:50 the field contact becomes unavailable. The next live I73 verification is returned for restored access and matching permission rather than being counted as started. R42-T9's independent lab permission and fixture evidence still hold, so that Work continues. The admission return records the permitted starts separately from the supplied observations of actual starts, with the active count at each time, the still-open S19 and I73 returns, and P8-P's afternoon reconsideration. `OPS.7:5.1` shows the resulting promise decision.

#### OPS.5:5.2 - Public-hospital emergency-care operation

One emergency-care operating function considers operating Work around exact patient and clinical-case subjects, changing observations, waiting, bed relations, service horizons, and current clinical and operating evidence. OPS.5 can return a bounded operating admission disposition only from authorized inputs. It does not turn a patient into a generic Work item or infer clinical priority from waiting age.

If consent, clinical evidence, competence, medical-safety, privacy, statutory permission, or another specialist condition is missing, the result names that blocker and its owner. Operations neither supplies treatment authority nor overrides clinical judgement. The first useful result is an authorized operating admission or an exact returned condition, not a dashboard state or automatic triage result.

#### OPS.5:5.3 - AI-assisted software operation

One software operation considers user issues, agent episodes, candidate changes, harness and tool access, traces, test results, human decisions, and release commitments. OPS.5 uses current context and tool capacity, bounded concurrency, integration burden, evidence needs, and established human or other authority to decide what may start.

A model score, available agent, free context window, generated patch, or scheduled episode does not by itself establish admission, permission, performed Work, or release. The result admits only the exact bounded Work whose identity, conditions, evidence, access, authority, and start limit obtain; it defers or returns the rest with retry conditions. Security, software assurance, provider capability, agenthood, and release authorization remain direct specialist returns.

### OPS.5:6 - Bias-Annotation

| Bias or pressure | How it distorts admission | Countermeasure |
| --- | --- | --- |
| visibility and rank bias | The top visible item appears authorized and ready. | Test identity, evidence, permission, authority, and start conditions separately. |
| sunk-commitment pressure | Earlier planning or public promise is used to force admission. | Recover the actual commitment parties, conditions, authority, and current status. |
| utilization pressure | Every available person, rig, tool, or model is filled immediately. | State the bounded receiving result and explicit-start limit; preserve deliberate non-start. |
| automation bias | A model recommendation or generated artifact is treated as admission or Work. | Require a separate admission result, authorized starter, performance evidence, and later result evidence. |
| urgency leakage | Age or consequence language becomes automatic admission order. | Leave priority and commitment revision to `OPS.7`; use only the current admission criteria here. |
| silent-rejection pressure | Deferred or rejected demand disappears from the account. | Preserve identity, disposition, reason, retry or return, and residual demand. |
| source-school anchoring | A familiar board, backlog, buffer, or WIP rule supplies the whole Method. | Adopt only the bounded mechanism that changes this decision and keep its limits explicit. |

### OPS.5:7 - Conformance Checklist

- [ ] The exact operating System, receiving result or commitment, configuration, and horizon are named.
- [ ] Every considered demand item has an identity and proposed receiving use.
- [ ] Matching `OPS.2`, `OPS.3`, and `OPS.4` inputs are reused only where action-changing and current.
- [ ] Admission criteria and non-negotiable conditions include relevant evidence, authority, permissions, access, specialist returns, and currentness.
- [ ] The explicit-start limit is bounded to this use and is not presented as a universal queue, capacity, or constraint policy.
- [ ] `C.11` is used only for several real live alternatives on a stable comparison basis.
- [ ] Every item is admitted, deferred, rejected, or returned with reason, conditions, horizon, and next review or return.
- [ ] The authorized starter is named only where that relation is established.
- [ ] Residual demand remains visible.
- [ ] Admission is not claimed as started or completed Work.
- [ ] Wider Operations and specialist questions return to their direct owners.

### OPS.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| top card means start | Rank substitutes for authority and permission. | Record admission, permission, starter, and start conditions separately. |
| everything is “in progress” | Hidden starts erase residual demand and overload the operation. | Apply an explicit-start limit and give every item a disposition. |
| availability implies capacity | A free slot, worker, rig, tool, or model is treated as a complete capability and access result. | Recover the exact performer, resource relation, capability, permission, and configuration. |
| choose-first option set | An artificial score replaces mandatory conditions or direct rules. | Use the direct branch; compare only genuine admissible alternatives. |
| admission by artifact | Ticket creation, assignment, plan, model output, or code generation becomes “Work started”. | Establish whether Work occurred from independent performance evidence; decide admission and permission before the prospective start. |
| rejection without return | Demand silently disappears or repeatedly re-enters. | Keep the reason, residual identity, owner, and retry condition. |
| local rule claims the system | One start limit becomes a universal WIP, queue, capacity, or constraint Method. | Bound the result and return wider policy questions. |

### OPS.5:9 - Consequences

The operation gains a truthful boundary between demand and current starts. Participants can see what entered, what did not, why, under whose authority, for which horizon, and what should be reviewed. Hidden starts and silent residual demand become easier to challenge.

The cost is explicit identity, evidence, conditions, authority, and disposition work. Some demand remains visibly deferred or returned rather than cosmetically “active”.

### OPS.5:10 - Rationale

Admission is valuable because it protects the boundary between possible demand and authorized current Work. Combining it with queue design, performed Work, or service assurance would make a locally usable decision depend on much wider results and would hide exactly where permission and evidence are needed.

The four dispositions prevent the false binary “start or lose”. Direct rules remain direct, genuine alternatives can be compared, and residual demand stays available for reconsideration or specialist return. The pattern therefore closes the smallest decision that lets a continuing operation limit starts while leaving unresolved queue, constraint, capacity, interacting-structure, and whole-service questions for their own decisions.

### OPS.5:11 - SoTA-Echoing

The question is which prepared work may start now. The serious comparator is competent policy-governed pull. The [Kanban Guide 2025.5](https://kanbanguides.org/the-kanban-guide/2025.5/) already provides explicit workflow policies and active-work control; TameFlow's preparation account adds useful-package readiness and distinguishes optional from committed demand. OPS adopts these contributions.

Apply both approaches to section 5.1. A capable pull policy sees one free slot, keeps the WIP bound, applies the authorized incident exception and starts I73-D. The possible residual is narrower: the fixture readiness required for R42-T9 differs from the safety decision required for release, and the operating coordinator cannot manufacture the latter. Sections 4.3–4.6 distinguish those consuming uses, apply the existing bound and return S19 to its owner while retaining permissible work. If the incumbent's policies and records already do this, they are the adequate admission arrangement.

The addition costs a check of current prerequisites and permission, an exact return for a missing condition, and follow-up on deferred demand. Where eligibility rarely changes and one authority already covers the operation, a separate per-item OPS form costs more without altering starts. Reuse the existing policy and item record; do not duplicate its queue history. Where multiple authorities or prerequisites differ by action, that bounded work can prevent a ready-looking item from acquiring a permission it lacks.

FPF `C.11` supplies comparison among genuine admissible alternatives; it neither sets the bound nor grants permission. Reinertsen's historical queue and economic mechanisms inform policy questions returned to OPS.8–OPS.10. No universal WIP value, service guarantee or proof of completed Work is imported. Reopen when the unit or counting rule, readiness, authority or protected capacity changes, or when the incumbent supplies the same dispositions with less total work.

### OPS.5:12 - Relations

- `OPS.2` supplies a selected coordination-form decision where that form changes admission. `OPS.3` supplies exact operating subjects and direct relations. `OPS.4` supplies current claims, evidence, permissions, commitments, uncertainty, and gaps. None of those results admits demand by itself.
- `C.11` governs comparison only when several live admissible alternatives require choice. `A.10` governs evidence reliance; `A.15.8` governs performance-configuration and recovery questions when they become the actual blocker.
- `OPS.6` consumes the applicable admission and independently supported current permission for the same matter and conditions; an admission account may carry both results.
- `OPS.7` separately governs current priority or bounded commitment revision. `OPS.8`–`OPS.13` retain queue, buffer, constraint, capacity, interacting-structure, and wider commitment questions.
- Clinical, safety, legal, privacy, security, finance, product release, capability, and other specialist practices retain their subjects, evidence, permission, authority, and conclusions.
- Practitioners may enter OPS.5 directly when matching current inputs already exist, repeat it as demand changes, or stop after its result.

### OPS.5:End
