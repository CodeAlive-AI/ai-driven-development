## F.14 - Anti-Explosion Control for Role and Status Name Families
> **Status:** Stable

**"Name less; recover the kinds first."**

**Type.** Architectural pattern.
**Status.** Stable.
**Normativity.** Normative.
**Builds on:** `A.2` for work-facing `U.Role`; `A.2.1` for `U.RoleAssignment`; `A.2.5` for role state; `A.2.7` for context-local role relation structure; `A.15.1` for performed work; `F.4` for RoleDescription; `F.5` for local naming discipline; `F.8` for mint-or-reuse decisions; `F.9` for cross-context bridges; `F.10` for status families and windows; `F.18` for durable naming; `A.6.5` for relation-slot discipline.

**Coordinates with:** `A.2.2` for capability, `A.3.1` and `A.3.2` for method and method-family naming, `A.10` and `B.3` for evidence and assurance use, `E.17` and `E.10.D2` for publication and description use, and `F.17` only when public or cross-context term-sheet reuse is current.

**Plain entry cues (informative).** Name explosion guard; role-name economy; status-name economy.

### F.14:1 - Intent and applicability

**Intent.** Keep role-like and status-like vocabularies small without losing real distinctions. F.14 is a control pass over candidate names and local name families. It does not define `U.Role`, does not define status ontology, and does not assign a holder. It asks what each proposed name is trying to name and blocks new durable names when the needed value is already a role value, role-relation expression, status family, status value, status window, qualifier, direct-pattern value, local phrase, or alias.

**Applicability.** Use F.14 when a project proposes several new role, status, access, evidence, requirement, source, method, capability, or work-like labels and the vocabulary starts to grow faster than the underlying distinctions. Use it before adding RoleDescriptions, Concept-Set rows, public names, cross-context rows, or role-relation names.

**Primary EntityOfConcern in plain terms.** One anti-explosion control pass over a candidate family of names in a bounded context or bridge family. The EoC is not the role value, not the status value, not the holder, not the work occurrence, and not a publication.

**Admissible move in plain terms.** Recover the kind of each candidate name, choose reuse or direct-pattern naming where possible, and record why no new durable role or status name is needed unless F.8 and F.18 admit it.

**Primary working reader.** A method author, terminology steward, architect, manager, or checker who sees names such as `NightOperatorRole`, `EvidenceRole`, `SeniorReviewer`, `AtRiskStatus`, `PreValidated`, `AccessRole`, or `RequestApproverRole` and must stop the vocabulary from becoming a second ontology.

**Use this when.** Use F.14 when name growth hides one of these questions:

1. Is this one work-facing `U.Role`, a RoleDescription label, a role-relation expression, a role assignment, a capability requirement, a method name, a work name, or only a local phrase?
2. Is this one status family, status value, status window, status-use relation, evidence-use relation, source-use relation, requirement-use relation, or presentation label?
3. Is the candidate cross-context and therefore dependent on F.9 or F.17 before durable reuse?

**What goes wrong if missed.** Role labels become capability models, status labels become role families, access-control labels become work roles, and role-relation expressions become fake holders. The corpus then gets many small near-duplicate names that look precise but hide different kinds.

**What this buys.** A smaller vocabulary with stronger type separation: fewer durable names, clearer role relation structure, cleaner status families, fewer aliases with hidden claims, and more reliable F.8 and F.18 naming decisions.

**Not this pattern when.** Not F.14 when the question is one candidate expression only; use F.8. Not F.14 when the question is assigning a holder or attributing performed work; use A.2.1, F.6, and A.15.1. Not F.14 when the question is a status-use or evidence-use claim; use F.10, A.10, B.3, or the direct governing pattern. Not F.14 when the question is public terminology publication; use F.17 and F.18 after kind recovery.

**Recognition versus assurance note.** The recognition block is the name-growth situation plus the first kind-recovery move. The assurance block is the record, invariants, role-relation and status-family boundaries, conformance tests, and SoTA note. Assurance text tightens the same anti-explosion control pass; it must not turn F.14 into role ontology, status ontology, or naming authority for every value.

### F.14:2 - Problem frame

Name explosion usually begins with a helpful shortcut:

1. **Hybrid role shortcut.** `RequestApproverRole`, `DevOpsEngineerRole`, or `IncidentLeadOnCall` is minted because several roles often appear together.
2. **Modifier-as-role shortcut.** `NightOperatorRole`, `RemoteOperatorRole`, or `APIApproverRole` is minted because a qualifier is visible.
3. **Status-as-type shortcut.** `AtRisk`, `Grace`, `PreValidated`, or `TemporarilyBreached` is minted as if time stance or status value were a new essence.
4. **Source-suffix shortcut.** `EvidenceRole`, `RequirementRole`, `AccessRole`, or `ProviderRole` is minted because a source tradition uses role-like language.
5. **Prestige shortcut.** `SeniorReviewer` or `LeadApprover` is minted to bypass a separation or assurance question.
6. **Cross-context shortcut.** The same label in two contexts is treated as one durable name without an F.9 bridge.

F.14 prevents those shortcuts from becoming durable ontology.

### F.14:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| Parsimony versus real difference | A small vocabulary is useful only if real distinctions remain recoverable. |
| Locality versus public reuse | Role and status names start in bounded contexts; some later need public or cross-context reuse. |
| Recognition versus assignment | A good role name helps recognition; it does not assign a holder or prove work. |
| Role relation structure versus new role | Role-requirement substitution, incompatibility, qualification, and bundle expressions are useful, but they do not automatically mint a new `U.Role`. |
| Status family versus status name | Time windows, values, confidence, and presentation labels should not multiply status families. |
| Qualifier visibility versus kind discipline | A visible qualifier may belong to role state, work plan, capability, method, status window, evidence, source, or publication rather than the role name. |

### F.14:4 - Core idea

Use the anti-explosion sequence before minting a durable role or status name.

1. **Recover kind first.** Split the candidate family into role values, RoleDescription labels, role-relation expressions, assignments, work, capability, method, status, evidence, source, publication, requirement, policy, bridge, and local-phrase cases.
2. **Reuse existing values.** If a role value, status family, Concept-Set row, local sense, or public term already admits the current use, reuse it and record aliases where needed.
3. **Use role relation structure instead of hybrid roles.** If one role can satisfy another role requirement, two roles conflict, or roles travel together, use A.2.7 role relation structure. Do not mint a fused role unless the bounded context deliberately creates a new `U.Role` with RoleDescription and F.8 and F.18 admission.
4. **Use assignment checks instead of prestige names.** If the issue is who may hold a role, whether a separation holds, or whether work occurred, use A.2.1, F.6, A.15.1, and role state checks.
5. **Use status families and windows instead of status-name sprawl.** If the issue is time stance, evaluation state, grace, confidence, or presentation, use F.10 or the direct status pattern.
6. **Use direct patterns for qualifiers.** Capability, method, work, evidence, source, publication, requirement, policy, and assurance qualifiers stay with their direct patterns. They may inform a name later; they do not become role or status ontology by suffix.

### F.14:5 - Minimal vocabulary

* **Anti-explosion control pass** - one review of a candidate family of related names to prevent unnecessary durable names.
* **Candidate name family** - a local set of proposed names that appear to cover related work, role, status, evidence, source, capability, method, or policy concerns.
* **Recovered value** - the typed FPF value or relation that the candidate name is trying to name.
* **Role-relation expression** - a context-local role-requirement substitution, incompatibility, qualification, or bundle expression governed by A.2.7.
* **Status-family expression** - a status family, value, window, confidence, or status-use relation governed by F.10 or a direct status pattern.
* **Qualifier value** - a value governed by a direct pattern that narrows use without becoming part of the role or status kind.
* **Blocked minting** - a decision that the candidate name remains an alias, local phrase, qualifier, role-relation expression, or direct-pattern name rather than a new durable role or status name.

### F.14:6 - Anti-explosion record

Use this record when more than one related candidate name is under pressure.

```text
AntiExplosionControlRecord:
  BoundedContextRef:
  CandidateNameFamily:
  CandidateExpressionRefs:
  RecoveredValues:
  ExistingValueOrRowRefs:
  RoleRelationStructureRefs:
  AssignmentOrWorkRefs:
  StatusFamilyOrWindowRefs:
  QualifierOrDirectPatternRefs:
  BridgeOrPublicTermRefs:
  BlockedMinting:
  DurableNamingRefs:
  RemainingLocalAliases:
  ReopenTrigger:
```

`RecoveredValues` is the center of the record. Each candidate expression is mapped to the value or relation it is trying to name. If no typed value is recovered, the expression stays local or goes to F.8 for a mint-or-reuse decision. `DurableNamingRefs` cites F.5, F.17, or F.18 only after the relevant value is recovered.

### F.14:7 - Levers

#### F.14:7.1 - Recover kind before naming

Ask what the candidate expression is trying to name.

| Candidate shape | Likely recovery | Direct pattern |
| --- | --- | --- |
| `ReviewerRole`, `OperatorRole` | work-facing role value or RoleDescription label | A.2, F.4, F.5, F.18 |
| `AliceAsReviewer` | role assignment or performed-work attribution | A.2.1, F.6, A.15.1 |
| `SeniorReviewer` | role value plus qualifier, role state, capability, or assurance claim | A.2, A.2.2, A.2.5, B.3, F.18 |
| `RequestApproverRole` | role-bundle expression or forbidden hybrid | A.2.7, F.8 |
| `AtRisk`, `Grace`, `PreValidated` | status value, window, confidence, or presentation label | F.10 or direct status pattern |
| `EvidenceRole`, `RequirementRole`, `AccessRole` | evidence-use, requirement-use, policy or access, or source-use relation | A.10, E.10.D2, E.17, policy or access patterns |
| same label in two contexts | cross-context bridge or public term | F.9, F.17, F.18 |

#### F.14:7.2 - Reuse before minting

Reuse a value when the recovered value, bounded context, and admitted use match. Use F.9 when reuse crosses context. Use F.8 when a candidate appears new. Use F.18 only when a durable name is needed after kind recovery.

#### F.14:7.3 - Role Relation Structure Before Hybrid Role

If two roles often appear together, state a role-bundle expression in A.2.7. If two roles must stay apart, state an incompatibility relation in A.2.7 and check assignments with A.2.1 and F.6. If one role value can satisfy another role requirement, state a role-requirement substitution relation in A.2.7. The role-relation expression does not assign a holder and does not become a role value by itself.

#### F.14:7.4 - Status window before status family multiplication

If the proposed name marks evaluation, active use, grace, archival state, confidence, or presentation, keep the status family and use F.10 windows, values, or direct status-use relations. A new status family needs a recovered value difference, not a new adjective.

#### F.14:7.5 - Qualifier before role-name clone

If the proposed role name adds time, location, object type, seniority, permission, method, capability, evidence, or source, recover the qualifier's direct pattern. Only keep it in a durable role name if F.18 admits that the bounded context truly needs a separate role value.

### F.14:8 - Invariants

1. **Kind first.** A candidate name is not admitted as a durable role or status name until its recovered value is named.
2. **No status roles.** Status, evidence, requirement, source, publication, and access uses do not become work-facing roles by suffix.
3. **No assignment by name.** A RoleDescription label or role-relation expression does not assign a holder and does not prove performed work.
4. **No hybrid role by convenience.** Role-bundle and incompatibility expressions stay in A.2.7 unless a bounded context deliberately creates a new role value with F.8 and F.18 admission.
5. **No capability by role label.** Role names do not prove capability, skill, permission, assurance, or method validity.
6. **Status windows stay status-side.** Time, confidence, grace, or presentation variation stays with F.10 or the direct status pattern unless a new status family is recovered.
7. **Cross-context reuse needs a bridge.** Shared labels across contexts use F.9 before any Concept-Set row, public name, or durable cross-context reuse.
8. **Lineage labels do not preserve ontology.** A historical label may be recorded as lineage or source wording, but it does not carry its old fused ontology forward.

### F.14:9 - Reasoning primitives

```text
candidateName(e) and recoveredValue(e, v)
  -> name decision must be made for v, not for e as a string.
```

Interpretation: the expression is a cue. The recovered value governs the naming decision.

```text
roleBundleExpression(R1, R2, C)
  -> not(newRoleValue(R1R2)).
```

Interpretation: a bundle expression may be named as an expression, but it does not mint a fused `U.Role`.

```text
roleIncompatibility(R1, R2, C, W)
  -> assignment check must consider holder and overlapping window.
```

Interpretation: separation questions need A.2.1 and F.6 checks, not prestige names.

```text
statusVariant(S, windowOrValue)
  -> keep status family S unless F.10 recovers a new family.
```

Interpretation: status values and windows do not multiply status families by default.

```text
qualifier(q) governedBy(P)
  -> q may constrain a name only after P recovers the qualifier value.
```

Interpretation: capability, method, work, evidence, source, publication, policy, and assurance qualifiers must not hide inside role or status names.

### F.14:10 - Worked cases

#### F.14:10.1 - Requester and approver

Candidate family: `RequesterRole`, `ApproverRole`, `RequestApproverRole`, `SeniorApprover`.

Result:

* `RequesterRole` and `ApproverRole` are work-facing role values with RoleDescriptions.
* `RequestApproverRole` is blocked as a fused role. Use an A.2.7 role-bundle expression when the two roles travel together.
* If the same holder must not carry both assignments in the same change window, use A.2.7 incompatibility plus A.2.1 and F.6 assignment checks.
* `SeniorApprover` is not proof of independence or assurance. Recover role state, capability, assurance, or local policy before durable naming.

#### F.14:10.2 - Operators across shifts

Candidate family: `OperatorRole`, `NightOperatorRole`, `RemoteOperatorRole`, `OnCallOperatorRole`.

Result:

* `OperatorRole` is the role value.
* `night`, `remote`, and `on-call` are recovered as schedule, location, role-state, work-plan, or policy qualifiers.
* A new role is blocked unless the bounded context shows a distinct role value with different RoleDescription, assignment predicates, and method or work implications.

#### F.14:10.3 - SLO compliance labels

Candidate family: `Compliant`, `AtRisk`, `Grace`, `Breached`, `Waived`.

Result:

* These are not role names.
* F.10 recovers status family, status value, status window, confidence, or deontic or policy use.
* Presentation labels may stay local or be named by the direct status pattern. They do not become `U.Role`, RoleDescription, or role relation structure.

#### F.14:10.4 - Evidence and requirement suffixes

Candidate family: `EvidenceRole`, `RequirementRole`, `StandardRole`, `SourceRole`.

Result:

* No work-facing role is recovered from suffix alone.
* Evidence, requirement, standard, and source uses go to A.10, B.3, E.10.D2, E.17, or the direct requirement or source pattern.
* A durable name may be admitted for the recovered relation, but not as a role value.

#### F.14:10.5 - Cross-context role labels

Two contexts both use `Operator`. One is a plant-control role; the other is an access-control permission grouping.

Result:

* F.9 Bridge Card first.
* The bridge may admit Naming-only or RoleDescription naming for a local work-facing role when the role value is recovered.
* The bridge does not import access permission as `U.RoleAssignment`, capability, or performed work.

#### F.14:10.6 - Ordinary composite role names

A project says: "Vasya is an engineer, he works on musical robots, and he is also a musician who teaches robots to play music."

Result:

* The ordinary phrase may remain "robotics engineer and musician" or "robotics engineer-musician" when the reader can recover it without ambiguity. FPF does not require a `Role` suffix in ordinary prose.
* Recover at least two work-facing role values when they are current: `EngineerRole@RobotEngineeringContext` and `MusicianRole@MusicPracticeContext`. If the engineering work is specifically robotics engineering, use a role qualifier, RoleDescription, or A.2.7 role-relation expression rather than minting `EngineerRoboticistRole` automatically.
* If "robotics engineer" is a stable local bundle or qualification relation, record it as `RoleRelationStructure@BoundedContext` under A.2.7. The relation structure may be named for local use, but it is not a new role value by itself.
* Recover method and work values separately: engineering method, robotics-engineering method family, music teaching method, robot-training work, and performed music work stay under the method and work patterns. They may motivate a role name only after F.8 and F.18 admission.
* A durable role value is selected only when the bounded context needs different assignment predicates, capability expectations, incompatibilities, method/work implications, or public naming. Otherwise keep the ordinary composite phrase and cite the recovered role relation, method, work, and capability values where they matter.

### F.14:11 - Anti-patterns and repairs


| ID | Anti-pattern | Symptom | Why it breaks thinking | Repair |
| --- | --- | --- | --- | --- |
| AP-1 | Hybrid role minting | `RequestApproverRole` becomes one role. | Erases role relation structure and separation checks. | Use A.2.7 bundle or incompatibility relation; create a role only after F.8 and F.18 admission. |
| AP-2 | Modifier-as-role | `NightOperatorRole` or `RemoteOperatorRole` appears for every circumstance. | Circumstances become kinds. | Recover schedule, location, role state, work-plan, or policy qualifier. |
| AP-3 | Status role | `ReadyReviewerRole` or `EvidenceRole` becomes a role-name family. | Status or evidence use becomes role ontology. | Use F.10, A.10, B.3, E.10.D2, or direct status and evidence patterns. |
| AP-4 | Prestige bypass | `SeniorReviewer` bypasses incompatibility or assignment checks. | Trust label substitutes for assurance or separation. | Keep role relation; use B.3, capability, role state, or assignment checks. |
| AP-5 | Row duplication | New row or public term for a name already admitted by a bridge and row. | Concept-Set table widens without new meaning. | Reuse the row; record the old term as lineage or source wording when needed. |
| AP-6 | Assignment hidden in role name | `AliceReviewerRole` looks like a role value. | Holder assignment is hidden in a name. | Use A.2.1 and F.6; keep the role value separate. |
| AP-7 | Method hidden in role name | `PressureTestReviewerRole` mixes method requirement and role. | Method and role become one ontology. | Use A.3.1 and A.3.2 for method, A.2 for role, F.18 only after recovery. |
| AP-8 | Presentation as status family | Red, amber, and green become status types. | Display colors substitute for status values and criteria. | Use direct status or presentation pattern; keep status family explicit. |

### F.14:12 - Conformance checklist

| Check | Question |
| --- | --- |
| CC-F14-01 | Is each candidate name tied to a recovered value or explicitly left as a local phrase? |
| CC-F14-02 | Are role values, RoleDescription labels, role-relation expressions, role assignments, and performed work kept separate? |
| CC-F14-03 | Are status family, status value, status window, status-use relation, and presentation label kept separate? |
| CC-F14-04 | Are capability, method, work, evidence, source, publication, requirement, policy, and assurance qualifiers handled by direct patterns? |
| CC-F14-05 | Are role-bundle and incompatibility cases sent to A.2.7 rather than minted as hybrid roles? |
| CC-F14-06 | Are public and cross-context names backed by F.9, F.17, or F.18 only after value recovery? |
| CC-F14-07 | Are lineage labels recorded without carrying old fused ontology forward? |
| CC-F14-08 | Is every durable new role or status name justified by F.8 and F.18 or by the direct status or naming pattern? |

### F.14:13 - Regression checks

| Check | Reopen condition |
| --- | --- |
| RSCR-F14-01 | Reopen when candidate names grow faster than recovered values. |
| RSCR-F14-02 | Reopen when a role name starts carrying assignment, capability, method, work, evidence, status, source, or publication claims. |
| RSCR-F14-03 | Reopen when a status label starts carrying role, holder, assignment, or work claims. |
| RSCR-F14-04 | Reopen when a public or cross-context name is reused without F.9, F.17, or F.18 admission. |
| RSCR-F14-05 | Reopen when role-relation expressions become fake holders, fake capabilities, or fake method families. |

### F.14:14 - Relations

* **A.2.** Governs the work-facing role value; F.14 only prevents unnecessary role-name growth.
* **A.2.1 and F.6.** Govern assignment and performed-work attribution; F.14 blocks names that hide those relations.
* **A.2.5.** Governs role state and enactable-state admission; F.14 blocks role-state qualifiers from becoming unexamined new roles.
* **A.2.7.** Governs role-requirement substitution, incompatibility, qualification, and bundle expressions; F.14 chooses that expression before hybrid-role minting.
* **F.4 and F.5.** Govern RoleDescription and local naming; F.14 supplies pressure to keep names few.
* **F.8.** Governs one candidate mint-or-reuse decision; F.14 uses F.8 when a family-level pass leaves a candidate unresolved.
* **F.9 and F.17.** Govern bridge and public term-sheet reuse; F.14 does not admit cross-context durable names by label alone.
* **F.10.** Governs status families, status values, windows, and status-use relations; F.14 prevents status-name sprawl.
* **F.18.** Governs durable naming after value recovery.
* **A.10, B.3, E.17, and E.10.D2.** Govern evidence, assurance, publication, source, description, and specification-use cases that often arrive with role-like suffixes.

### F.14:15 - SoTA-Echoing

**SoTA note.** F.14 does not import access-control, policy, terminology, or status taxonomies as FPF ontology. It uses their shared discipline: separate the named value from assignment, permission, status, evidence, and currentness claims before making a durable name.

| Current pressure | Practice line | F.14 adoption |
| --- | --- | --- |
| Role labels alone are too weak for authorization, work attribution, or capability claims. | RBAC lineage, ABAC, zero-trust, and policy-as-code practice separate role-like attributes, current context, policy decision, resource action, and evidence. | Keep role names separate from holder assignment, capability, policy, and work; use A.2.1, A.2.2, A.2.5, A.15.1, and direct policy and evidence patterns. |
| Terminology work distinguishes terms, concepts, designations, and contexts. | Current terminology and ontology practice treats a shared term as insufficient for identity. | Recover the value first; use F.9, F.17, and F.18 before public or cross-context reuse. |
| Status dashboards and presentation labels often hide criteria. | Operational monitoring and assurance practice separates indicator, threshold, time window, status value, evidence, and decision. | Keep status family, status value, window, evidence, and presentation separate; use F.10, A.10, B.3, and E.17. |

### F.14:16 - Didactic distillation

When names multiply, do not ask for a better name first. Ask what values are being named. Reuse existing roles and status families when they already admit the use. Use role relation structure for role-requirement substitution, incompatibility, qualification, and bundles. Use status windows and values for temporal or evaluative variation. Send capability, method, work, evidence, source, publication, requirement, policy, and assurance qualifiers to their direct patterns. Mint durable names only after the recovered value deserves one.

### F.14:End

