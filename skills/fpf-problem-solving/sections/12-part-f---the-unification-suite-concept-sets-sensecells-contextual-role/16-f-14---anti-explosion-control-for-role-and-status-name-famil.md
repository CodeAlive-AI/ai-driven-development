## F.14 - Anti-Explosion Control for Role and Status Name Families
> **Status:** Stable

**"Name less; recover the governed values first."**

**Type.** Architectural pattern.
**Status.** Stable.
**Normativity.** Normative.
**Builds on:** `A.2` for work-facing `U.Role`; `A.2.1` for `U.RoleAssignment`; `A.2.5` for role state; `A.2.7` for exact role-requirement substitution, incompatibility, qualification, and bundle relations; `A.15.1` for performed work; `F.4` for RoleDescription; `F.5` for local naming discipline; `F.8` for one mint-or-reuse decision; `F.9` for actual relations between exact local senses; `F.10` for status families and windows; `F.18` for durable naming; and `A.6.5` for relation-slot discipline.

**Coordinates with:** `A.2.2` for capability, `A.3.1` and `A.3.2` for method and method-description naming, `A.10` and `B.3` for evidence and assurance use, `E.10.D2` for description use, `E.24.PUB` for publication occurrence/form/carrier, and `F.17` only when a public, Core-facing, durable, or cross-local term row is current.

**Plain entry cues (informative).** Name explosion guard; role-name economy; status-name economy; stop before another card or row.

### F.14:1 - Intent and applicability

**Use this when.** Use F.14 when proposed names, aliases, cards, local-sense cells, or rows begin to multiply faster than the independently governed distinctions. Apply its cheap stop question before minting any NameCard, `SchemeSenseCell`, Unified Term Sheet row, or durable name family: **does an existing designation, alias, local expression, or direct-pattern name already let the practitioner perform the proposed use?**

**First useful move.** For every candidate expression, name the one independently recovered governed value or relation, its exact kind, its direct pattern, the proposed use, and the effective naming `U.ReferenceScheme`. If no such value or relation is independently recoverable, keep the expression local or return it to the direct subject/value-recovery owner; do not send a value-less expression to F.8 or manufacture an object so that the name has something to denote. F.8 receives only an unresolved naming disposition for an already recovered value-or-relation/use pair, with its exact kind, direct pattern, and proposed use.

**Intent.** Keep role-like and status-like vocabularies small without losing real distinctions. F.14 is a control pass over candidate expressions and name families. It defines no role, status, assignment, sense, card, row, Bridge, or publication. It decides only whether naming pressure can stop at a smaller disposition.

**Primary working object.** One candidate family and one proposed use, with its recovered values and direct patterns. A durable control record is optional; no generic context object, selected structure, card, or table row identifies the pass.

**Primary working reader.** A method author, terminology steward, architect, manager, or checker who sees names such as `NightOperatorRole`, `EvidenceRole`, `SeniorReviewer`, `AtRiskStatus`, `PreValidated`, `AccessRole`, or `RequestApproverRole` and must stop vocabulary growth from becoming a second ontology.

**What goes wrong if missed.** Role labels become capability models, status labels become role families, access-control labels become work roles, and every local wording difference acquires a card, sense cell, row, or identifier. The corpus then contains many near-duplicate naming objects whose apparent precision hides different kinds and uses.

**What this buys.** A smaller vocabulary with stronger type separation and a short stopping path: no durable name, an existing designation, an alias, or a local expression whenever one suffices; only then the smallest justified durable naming object.

**Not this pattern when.** F.8 owns the final naming disposition for one candidate expression only after its governed value or relation, exact kind, direct pattern, and proposed use have been recovered; F.14 supplies the preceding anti-explosion stop rather than a second decision record. Assignment and performed-work claims go to A.2.1, F.6, and A.15.1. Status, evidence, authorization, publication, and subject-relation claims return to their direct patterns. F.17 constitutes a reader-facing row only after kind recovery, F.14, F.8/F.18 where needed, and the public-row threshold; E.24.PUB separately governs availability.

**Recognition versus assurance.** Recognition is the visible name-growth pressure plus the first kind-and-use recovery. Assurance is the optional record, invariants, worked countercases, and conformance tests. Neither turns F.14 into naming authority or ontology.

### F.14:2 - Problem frame

Name explosion usually begins with a helpful shortcut:

1. **Hybrid-role shortcut.** `RequestApproverRole`, `DevOpsEngineerRole`, or `IncidentLeadOnCall` is minted because several roles often appear together.
2. **Modifier-as-role shortcut.** `NightOperatorRole`, `RemoteOperatorRole`, or `APIApproverRole` is minted because a qualifier is visible.
3. **Status-as-type shortcut.** `AtRisk`, `Grace`, `PreValidated`, or `TemporarilyBreached` is minted as if time stance or status value were a new essence.
4. **Source-suffix shortcut.** `EvidenceRole`, `RequirementRole`, `AccessRole`, or `ProviderRole` is minted because a source tradition uses role-like language.
5. **Prestige shortcut.** `SeniorReviewer` or `LeadApprover` is minted to bypass a separation, capability, or assurance question.
6. **Locality shortcut.** The same spelling under two local-sense bases is treated as one value, or every difference is answered with a Bridge, card, cell, and row before a receiving use exists.

F.14 prevents those shortcuts from becoming durable ontology or automatic naming infrastructure.

### F.14:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| Parsimony versus real difference | A small vocabulary is useful only if every real governed distinction remains recoverable. |
| Local expression versus durable reuse | Most wording can remain local; public or repeated reuse may justify one durable settlement. |
| Recognition versus assignment | A good role name helps recognition; it does not assign a holder or prove work. |
| Relation structure versus new role | Role substitution, incompatibility, qualification, and bundle relations may be useful without minting another `U.Role`. |
| Status family versus status-name growth | Time windows, values, confidence, and presentation labels should not multiply status families. |
| Discoverability versus naming-object cascades | Cards, cells, rows, identifiers, and publications can help retrieval, but none is justified merely because the previous one exists. |

### F.14:4 - Core idea

Use this sequence before minting a durable name or any supporting naming object:

1. **Recover the governed value first.** Split candidate expressions into exact role values, RoleDescription labels, direct relation kinds or occurrences, assignments, Work, capability, method, status, evidence, source, publication, requirement, policy, local-sense, and local-phrase cases. Each retained value keeps its exact kind and direct owner.
2. **Name one proposed use and its interpretation basis.** State what the reader will do with the expression and the effective naming `U.ReferenceScheme`. An independently selected `BoundedModelUseStructure` appears only when that organization changes this exact naming use; it is never a generic locality field.
3. **Try the light dispositions in order.** Prefer no durable name, an existing designation, a recorded alias, a local expression, or an existing direct-pattern/public-row name. Stop as soon as the proposed use works without hiding a governed distinction.
4. **Create only the next object that pays for itself.** A local `SchemeSenseCell` is useful only when the exact local sense needs a stable address; a NameCard only when the naming settlement itself must endure; an F.17 row only for public, Core-facing, durable, or cross-local reuse; E.24.PUB only when the selected row edition must actually be made available. None implies the next.
5. **Use exact subject relations instead of fused names.** Role bundles and incompatibilities remain A.2.7 relations; holder and Work claims remain A.2.1/F.6/A.15.1; status families and windows remain F.10; qualifiers remain with their direct patterns.
6. **Treat cross-local wording as a relation question only when one is current.** Resolve the exact local senses first. Same spelling proves nothing; different local-sense projections only open F.9. Cite a Bridge only when its predicate obtains, then state the proposed use and reliance separately. A Bridge does not merge governed values or require a public row.

The result is the smallest naming disposition that preserves the exact governed value and supports the named use. It is not a claim that any value, relation, assignment, Work, evidence, status, authority, or publication exists.

### F.14:5 - Minimal vocabulary

* **Anti-explosion control pass** — one bounded review of related candidate expressions before durable naming objects are added.
* **Candidate name family** — proposed expressions that appear to cover related role, status, work, evidence, source, capability, method, policy, or local-sense concerns.
* **Recovered governed value** — the exact typed value or relation the expression is trying to designate, under its direct pattern.
* **Naming use** — the exact reader or practitioner action for which the expression is being considered.
* **Light disposition** — no durable name, existing designation, alias, local expression, or existing row reuse.
* **Role-relation expression** — an expression designating an exact A.2.7 substitution, incompatibility, qualification, or bundle relation rather than another role value.
* **Status-family expression** — an expression for a status family, value, window, confidence claim, or status-use relation governed by F.10 or a direct status pattern.
* **Blocked minting** — the explained result that the candidate remains a light disposition or direct-pattern expression rather than a new durable name or naming object.

### F.14:6 - Optional anti-explosion record

Ordinary use needs no record: recover the value, choose the lightest sufficient disposition, and stop. Persist this C.2.1 description episteme only when several related candidates, a contested decision, or later replay makes the family-level reasoning useful.

```text
AntiExplosionControlRecord:
  CandidateNameFamily:
  ProposedNamingUse:
  EffectiveNamingReferenceScheme:
  CandidateExpressionRefs:
  RecoveredGovernedValueRefs:
  GovernedValueKindRefs:
  DirectGoverningPatternRefs:
  ExistingDesignationOrAliasRefs:
  LocalSenseRefsOrCellRefs?:
  LocalSenseBasisRelationRefs?:
  ModelUseStructureRef?: only when an independently selected structure changes this use
  ExactRoleRelationRefs?:
  AssignmentOrWorkRefs?:
  StatusFamilyOrWindowRefs?:
  QualifierOrDirectPatternRefs?:
  ActualBridgeRefs?:
  BlockedMinting:
  DurableNamingRefs?:
  RemainingLocalExpressions:
  ReopenTrigger:
```

The record describes the control result. It creates no governed value, naming decision occurrence, designation, local sense, Bridge, row, publication, evidence, role, status, or Work. A field is omitted when its object is not independently current; filling the record is never a completeness goal.

### F.14:7 - Levers

#### F.14:7.1 - Recover kind before naming

| Candidate shape | Likely recovery | Direct pattern |
| --- | --- | --- |
| `ReviewerRole`, `OperatorRole` | work-facing role value or RoleDescription label | A.2, F.4, F.5, F.18 |
| `AliceAsReviewer` | role assignment or performed-work attribution | A.2.1, F.6, A.15.1 |
| `SeniorReviewer` | role value plus qualifier, role state, capability, or assurance claim | A.2, A.2.2, A.2.5, B.3, F.18 |
| `RequestApproverRole` | role-bundle expression or forbidden hybrid | A.2.7, F.8 |
| `AtRisk`, `Grace`, `PreValidated` | status value, window, confidence, or presentation label | F.10 or direct status pattern |
| `EvidenceRole`, `RequirementRole`, `AccessRole` | evidence-use, requirement-use, policy/access, or source-use relation | A.10, E.10.D2, policy/access/source patterns |
| same spelling under two local-sense bases | two designations or an exact F.9 relation question | F.18, F.9; F.17 only at its public-row threshold |

#### F.14:7.2 - Reuse before minting

Reuse only when the exact recovered value, kind, direct pattern, proposed use, and admitted naming scope match. Try an existing designation, alias, local expression, or current row before creating a card, cell, row, policy id, or new U-kind candidate. Local-sense reuse does not imply sameness with another local sense; row reuse does not widen the row's admitted use.

#### F.14:7.3 - Use role relations before hybrid roles

If two roles travel together, recover the exact A.2.7 bundle or qualification relation. If they must stay apart, recover exact incompatibility and check assignments through A.2.1 and F.6. If one role can satisfy another requirement, recover exact substitution. The relation expression does not assign a holder and does not become a role value by name.

#### F.14:7.4 - Use a status window before multiplying status families

If the proposed name marks evaluation, active use, grace, archival state, confidence, or presentation, keep the status family and use F.10 windows, values, or direct status-use relations. A new status family needs a recovered governed difference, not another adjective.

#### F.14:7.5 - Keep qualifiers with their direct owners

Time, location, object type, seniority, permission, method, capability, evidence, source, and publication are not role or status identity by suffix. Keep each qualifier with its direct pattern. Retain it in a durable name only when the already governed value and the named use genuinely require that designation.

#### F.14:7.6 - Stop before a naming-object cascade

A candidate can justify one object without justifying all later objects. A durable local expression needs no cell; a stable local sense may need a cell but no NameCard; a durable naming settlement may need a NameCard but no public row; a row may exist without a current publication occurrence; publication availability creates neither row truth nor governed-value truth. Apply the next gate only when its own use is current.

### F.14:8 - Invariants

1. **Governed value first.** No durable naming object is added until the exact value or relation, kind, direct owner, and proposed use are recoverable.
2. **Lightest sufficient disposition.** Prefer the dispositions `no durable name`, existing designation, alias, or local expression whenever one supports the use without hiding a distinction.
3. **No status roles.** Status, evidence, requirement, source, publication, and access uses do not become work-facing roles by suffix.
4. **No assignment by name.** A designation, RoleDescription, role-relation expression, card, cell, or row assigns no holder and proves no Work.
5. **No hybrid role by convenience.** Exact A.2.7 relations remain relations unless the direct role owner independently admits a different role value.
6. **No capability or authority by label.** Role and status names prove no capability, skill, permission, assurance, evidence use, method validity, or publication authority.
7. **Local senses do not globalize.** Same spelling and different local-sense projections establish neither governed-value identity nor an F.9 Bridge.
8. **Naming objects remain optional and distinct.** Expression, designation, alias, cell, NameCard, row, identifier, publication occurrence, form, and carrier neither imply nor replace one another.
9. **Selected structure is conditional.** A `BoundedModelUseStructure` is cited only when its organization changes the exact naming use and never becomes a locality slot or naming identity field.
10. **Lineage is not ontology.** Historical spelling may be recorded as lineage without carrying its former fused commitments forward.

### F.14:9 - Reasoning primitives

```text
candidateExpression(e) and recoveredGovernedValue(e, v) and proposedUse(u)
  -> choose a naming disposition for <v,u>, not an ontology for string e.
```

```text
existingDesignationOrLocalExpression(v, u) is sufficient
  -> stop; do not mint NameCard, SenseCell, row, or name family.
```

```text
roleBundleRelation(R1, R2) obtains
  -> not(newRoleValue(R1R2)).
```

```text
statusVariant(S, windowOrValue)
  -> keep status family S unless its direct owner establishes a different family.
```

```text
differentLocalSenseProjections(c1, c2)
  -> test F.9 only for a named correspondence use; not(Bridge(c1,c2)) by difference alone.
```

```text
namingObjectPresent(x)
  -> not(governedValueExists) and not(nextNamingObjectRequired).
```

These are stopping and dispatch rules. They create no values or relation occurrences.

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
* A new role is blocked unless A.2 independently admits a distinct role value with a different RoleDescription, assignment predicates, and method or Work implications for the proposed use; the naming ReferenceScheme does not create that difference.

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
* Evidence, requirement, standard, source, and publication uses go to A.10, B.3, E.10.D2, E.24.PUB, or the direct requirement or source pattern.
* A durable name may be admitted for the recovered relation, but not as a role value.

#### F.14:10.5 - Same spelling across two local-sense bases

A plant team uses `Operator` for one work-facing role value. An access-control team uses `Operator` for one permission grouping. Recover both independently under their direct patterns; neither spelling nor organizational proximity makes them one value.

For local use, keep the existing expressions and stop. If one named cross-local naming use is later proposed, resolve its exact F.17 `SchemeSenseCell` endpoints and test F.9. Cite a Bridge only when its predicate obtains, then state the use direction, rule, tolerated loss, polarity, and reliance separately. A Bridge, NameCard, cell, or row imports no access permission as `U.RoleAssignment`, capability, authority, or performed Work. Publish an F.17 row only when the public/durable reuse threshold independently holds.

#### F.14:10.6 - Ordinary composite role names

A project says: "Vasya is an engineer, he works on musical robots, and he is also a musician who teaches robots to play music."

Result:

* Ordinary prose may remain `robotics engineer and musician` or `engineer-musician` when readers can recover the two exact role values and the sentence's use without ambiguity. FPF does not require a `Role` suffix.
* Recover engineering and musician role values independently under A.2. If robotics narrows the engineering role for this use, keep the exact qualifier, RoleDescription, or A.2.7 qualification/bundle relation rather than minting `EngineerRoboticistRole` automatically.
* Method and Work remain separate: engineering methods, music-teaching methods, robot-training Work, and performed music Work stay under their direct patterns. They motivate no role name by themselves.
* A durable qualified role name is considered only when the already governed role value has different assignment predicates, capability expectations, incompatibilities, method/Work implications, or a real public naming need. Otherwise keep the ordinary phrase and cite the exact relations only where they matter.

### F.14:11 - Anti-patterns and repairs

| ID | Anti-pattern | Symptom | Repair |
| --- | --- | --- | --- |
| AP-1 | Hybrid-role minting | `RequestApproverRole` becomes one role. | Use exact A.2.7 relations; admit a new role only under the direct role owner and later naming gates. |
| AP-2 | Modifier-as-role | Every circumstance yields `NightOperatorRole` or `RemoteOperatorRole`. | Recover schedule, location, state, plan, or policy qualifier. |
| AP-3 | Status or evidence role | `ReadyReviewerRole` or `EvidenceRole` becomes a role family. | Return status/evidence use to F.10, A.10, B.3, E.10.D2, or its direct owner. |
| AP-4 | Prestige bypass | `SeniorReviewer` substitutes for assurance or separation. | Keep the role fixed and recover capability, state, assurance, policy, or assignment checks. |
| AP-5 | Row duplication | Another row is added for an already admitted name and use. | Reuse the exact row within its admitted use; retain old wording as lineage when useful. |
| AP-6 | Assignment hidden in a name | `AliceReviewerRole` looks like a role value. | Use A.2.1/F.6 and keep the role value separate. |
| AP-7 | Method hidden in a role name | `PressureTestReviewerRole` fuses method and role. | Keep method and role under their direct owners; name either only after recovery. |
| AP-8 | Presentation as status family | Red/amber/green becomes status ontology. | Recover the exact status criterion and keep display form separate. |
| AP-9 | Naming-object cascade | A word automatically gets a cell, card, row, id, and publication. | Apply each gate separately and stop at the lightest useful disposition. |
| AP-10 | Spelling-based cross-local identity | Same label merges values or automatically creates a Bridge. | Resolve exact local senses; test F.9 only for a named use and keep governed values distinct. |

### F.14:12 - Conformance checklist

| Check | Question |
| --- | --- |
| CC-F14-01 | Is each candidate tied to one independently recovered governed value/relation and proposed use, or explicitly left local? |
| CC-F14-02 | Were the light dispositions—no durable name, existing designation, alias, and local expression—tested before minting anything stronger? |
| CC-F14-03 | Are role value, RoleDescription, direct role relation, assignment, capability, method, and performed Work distinct? |
| CC-F14-04 | Are status family, value, window, use relation, evidence, and presentation distinct? |
| CC-F14-05 | Are effective naming ReferenceScheme and exact local-sense basis used instead of a generic context slot? |
| CC-F14-06 | Is a selected model-use structure absent unless its organization changes this exact naming use? |
| CC-F14-07 | Does any cited F.9 Bridge actually obtain between exact cells, with proposed use and reliance separate? |
| CC-F14-08 | Are NameCard, cell, row, id, publication occurrence, form, and carrier independently justified and mutually distinct? |
| CC-F14-09 | Does every stronger ontology, relation, role, status, Work, evidence, authority, or publication claim return to its direct owner? |
| CC-F14-10 | Are lineage spellings retained without carrying fused ontology or widening admitted use? |

### F.14:13 - Regression checks

Reopen only the affected naming use when candidate expressions grow faster than recovered values; a name starts carrying assignment, capability, method, Work, evidence, status, source, publication, equivalence, or authority; a row is reused beyond its admitted use; local wording is silently globalized; or one naming object begins to imply the next. A changed spelling alone does not require a new governed value or full family replay.

### F.14:14 - Relations

* **A.2, A.2.1, A.2.5, A.2.7, F.6, and A.15.1** govern roles, assignments, role state, exact role relations, Work attribution, and Work. F.14 only blocks names that hide them.
* **F.8** owns one candidate's smallest mint-or-reuse disposition after the F.14 stop test.
* **F.9** owns only an actual relation between exact local senses. Shared spelling and cell presence establish none.
* **F.17** owns a public term-row episteme after its entry threshold; **F.18** owns a durable naming-settlement NameCard; neither owns the governed value.
* **C.2.1** owns every persisted NameCard, row, or control-record episteme and `EpistemeEditionRelation`; **E.24.PUB** owns row publication occurrence, expression form, and carrier bearing.
* **F.10, A.10, B.3, E.10.D2, and direct policy/access/source patterns** own the status, evidence, assurance, description, policy, access, and source claims that often arrive with role-like suffixes.

### F.14:15 - SoTA-Echoing

F.14 does not import access-control, terminology, or status taxonomies as FPF ontology. It adopts their shared practical discipline: separate the governed value, designation, assignment, permission, status, evidence, publication, and currentness before making a durable name.

| Current pressure | Practice line | F.14 adoption |
| --- | --- | --- |
| Role labels are too weak for authorization, Work attribution, or capability. | RBAC, ABAC, zero-trust, and policy-as-code separate attributes, policy decision, resource action, and evidence. | Keep role names separate from holder, capability, permission, policy, and Work. |
| Terminology practice distinguishes values/concepts, designations, local senses, records, and mappings. | Shared spelling is insufficient for identity or semantic equivalence. | Recover the value first; prefer light dispositions; use F.9/F.17/F.18 only at their exact triggers. |
| Status dashboards often hide criteria. | Monitoring and assurance separate indicator, threshold, time window, status, evidence, decision, and display. | Keep status and presentation objects separate and return each claim to its direct owner. |

### F.14:16 - Didactic distillation

When names multiply, do not ask for a better name first. Recover the exact values and the proposed use. Try no durable name, an existing designation, an alias, or a local expression. Keep role relations, status windows, capability, method, Work, evidence, source, policy, and publication under their direct patterns. Create a cell, NameCard, row, identifier, or publication only when that exact object buys a named use; none requires the next and none makes the governed value real.

### F.14:End

