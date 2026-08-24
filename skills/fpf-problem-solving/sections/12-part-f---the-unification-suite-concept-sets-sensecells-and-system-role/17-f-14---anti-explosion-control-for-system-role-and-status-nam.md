## F.14 - Anti-Explosion Control for System-Role and Status Name Families

**"Name less; recover the governed values first."**

**Type.** Architectural pattern.
**Status.** Stable.
**Normativity.** Normative.
**Builds on:** `A.2` for exact context-local system-role kinds; `A.2.1` for `U.SystemRoleAssignment`; `A.2.5` for assignment-state predicates and direct state relations; `A.2.7` for exact substitution, incompatibility, qualification, and bundle relations among system-role kinds; `A.15.1` for performed Work; `F.4` for system-role-kind descriptions; `F.5` for local naming discipline; `F.8` for one mint-or-reuse decision; `F.9` for actual relations between exact local senses; `F.10` for status families and windows; `F.18` for durable naming; and `A.6.5` for relation-slot discipline.

**Coordinates with:** `A.2.2` for capability, `A.3.1` and `A.3.2` for Method and MethodDescription naming, `A.10` and `B.3` for evidence and assurance use, `E.10.D2` for description use, `E.24.PUB` for publication occurrence, expression form, and carrier, and `F.17` only when a public, Core-facing, durable, or cross-local term row is current.

**Plain entry cues (informative).** Name explosion guard; system-role-name economy; status-name economy; stop before another card or row.

### F.14:1 - Intent and applicability

**Use this when.** Use F.14 when proposed names, aliases, cards, local-sense cells, or rows begin to multiply faster than the independently governed distinctions. Apply its cheap stop question before minting any NameCard, `SchemeSenseCell`, Unified Term Sheet row, or durable name family: **does an existing designation, alias, local expression, or direct-pattern name already let the practitioner perform the proposed use?**

**First useful move.** For every candidate expression, name the one independently recovered governed value or relation, its exact kind, its direct pattern, the proposed use, and the effective naming `U.ReferenceScheme`. If no such value or relation is independently recoverable, keep the expression local or keep it with the exact assertion that recovers its subject or value; do not pass a value-less expression to F.8 or manufacture an object so that the name has something to denote. F.8 receives only an unresolved naming disposition for an already recovered value-or-relation and proposed-use pair, with its exact kind and direct pattern.

**Intent.** Keep system-role-facing, role-like, and status-like vocabularies small without losing real distinctions. F.14 is a control pass over candidate expressions and name families. It defines no system-role kind, status, assignment, sense, card, row, Bridge, or publication. It decides only whether naming pressure can stop at a smaller disposition.

**Primary working object.** One candidate family and one proposed use, with its recovered values and direct patterns. A durable control record is optional; no generic context object, selected structure, card, or table row identifies the pass.

**Primary working reader.** A method author or designer, an author of a `U.MethodDescription`, a terminology steward, architect, manager, or checker who sees names such as `NightOperatorSystemRole`, `EvidenceRole`, `SeniorReviewer`, `AtRiskStatus`, `PreValidated`, `AccessRole`, or `RequestApproverSystemRole` and must stop vocabulary growth from becoming a second ontology.

**What goes wrong if missed.** System-role-kind labels become capability models, status labels become system-role families, access-control labels become work-facing kinds, and every local wording difference acquires a card, sense cell, row, or identifier. The corpus then contains many near-duplicate naming objects whose apparent precision hides different kinds and uses.

**What this buys.** A smaller vocabulary with stronger type separation and a short stopping path: no durable name, an existing designation, an alias, or a local expression whenever one suffices; only then the smallest justified durable naming object.

**Not this pattern when.** Use F.8 to make the final naming disposition for one candidate expression only after its governed value or relation, exact kind, direct pattern, and proposed use have been recovered; F.14 supplies the preceding anti-explosion stop rather than a second decision record. Assignment and performed-Work claims go to A.2.1, F.6, and A.15.1. Status, evidence, authorization, publication, and other relation claims require exact predicates in their direct patterns. Add a reader-facing F.17 row only after kind recovery, the F.14 stop, any needed F.8 or F.18 naming decision, and satisfaction of the public-row threshold; treat publication availability as a separate E.24.PUB question.

**Recognition versus assurance.** Recognition is the visible name-growth pressure plus the first kind-and-use recovery. Assurance is the optional record, invariants, worked countercases, and conformance tests. Neither turns F.14 into naming authority or ontology.

### F.14:2 - Problem frame

Name explosion usually begins with a helpful shortcut:

1. **Hybrid-system-role shortcut.** `RequestApproverSystemRole`, `DevOpsEngineerSystemRole`, or `IncidentLeadOnCall` is minted because several local system-role kinds often appear together.
2. **Modifier-as-system-role shortcut.** `NightOperatorSystemRole`, `RemoteOperatorSystemRole`, or `APIApproverSystemRole` is minted because a qualifier is visible.
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
| Recognition versus assignment | A good system-role-kind name helps recognition; it does not assign a system or prove Work. |
| Relations versus a new kind | Substitution, incompatibility, qualification, and bundle relations among system-role kinds may be useful without admitting another local kind. |
| Status family versus status-name growth | Time windows, values, confidence, and presentation labels should not multiply status families. |
| Discoverability versus naming-object cascades | Cards, cells, rows, identifiers, and publications can help retrieval, but none is justified merely because the previous one exists. |

### F.14:4 - Core idea

Use this sequence before minting a durable name or any supporting naming object:

1. **Recover the governed value first.** Split candidate expressions into exact local system-role kinds, `SystemRoleKindDescription` epistemes, direct relation kinds or occurrences, assignments, Work, capability, Method, status, evidence, source, publication, requirement, policy, local-sense, and local-phrase cases. Each retained value keeps its exact kind and direct pattern.
2. **Name one proposed use and its interpretation basis.** State what the reader will do with the expression and the effective naming `U.ReferenceScheme`. An independently selected `BoundedModelUseStructure` appears only when that organization changes this exact naming use; it is never a generic locality field.
3. **Try the light dispositions in order.** Prefer no durable name, an existing designation, a recorded alias, a local expression, an existing direct-pattern name, or an existing public row. Stop as soon as the proposed use works without hiding a governed distinction.
4. **Create only the next object that pays for itself.** A local `SchemeSenseCell` is useful only when the exact local sense needs a stable address; a NameCard only when the naming settlement itself must endure; an F.17 row only for public, Core-facing, durable, or cross-local reuse; E.24.PUB only when the selected row edition must actually be made available. None implies the next.
5. **Use exact relations instead of fused names.** Bundles and incompatibilities among system-role kinds remain A.2.7 relations; assignment and Work claims remain A.2.1, F.6, and A.15.1; status families and windows remain F.10; qualifiers remain with their direct patterns.
6. **Treat cross-local wording as a relation question only when one is current.** Resolve the exact local senses first. Same spelling proves nothing; different local-sense projections only open F.9. Cite a Bridge only when its predicate obtains, then state the proposed use and reliance separately. A Bridge does not merge governed values or require a public row.

The result is the smallest naming disposition that preserves the exact governed value and supports the named use. It is not a claim that any value, relation, assignment, Work, evidence, status, authority, or publication exists.

### F.14:5 - Minimal vocabulary

* **Anti-explosion control pass** — one bounded review of related candidate expressions before durable naming objects are added.
* **Candidate name family** — proposed expressions that appear to cover related system-role, status, Work, evidence, source, capability, Method, policy, or local-sense concerns.
* **Recovered governed value** — the exact typed value or relation the expression is trying to designate, under its direct pattern.
* **Naming use** — the exact reader or practitioner action for which the expression is being considered.
* **Light disposition** — no durable name, existing designation, alias, local expression, or existing row reuse.
* **System-role-kind relation expression** — an expression designating an exact A.2.7 substitution, incompatibility, qualification, or bundle relation rather than another local system-role kind.
* **Status-family expression** — an expression for a status family, value, window, confidence claim, or status-use relation defined under F.10 or a direct status pattern.
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
  PatternContributionByClaimOrValue:
    - ClaimOrValueRef:
      PatternRef:
      Contribution: defines | constrains | tests
  ExistingDesignationOrAliasRefs:
  LocalSenseRefsOrCellRefs?:
  LocalSenseBasisRelationRefs?:
  ModelUseStructureRef?: only when an independently selected structure changes this use
  ExactSystemRoleKindRelationRefs?:
  AssignmentOrWorkRefs?:
  StatusFamilyOrWindowRefs?:
  QualifierOrDirectPatternRefs?:
  ActualBridgeRefs?:
  BlockedMinting:
  DurableNamingRefs?:
  RemainingLocalExpressions:
  ReopenTrigger:
```

The record describes the control result. It creates no governed value, naming decision occurrence, designation, local sense, Bridge, row, publication, evidence, system-role kind, status, assignment, or Work. A field is omitted when its object is not independently current; filling the record is never a completeness goal.

### F.14:7 - Levers

#### F.14:7.1 - Recover kind before naming

| Candidate shape | Likely recovery | Direct pattern |
| --- | --- | --- |
| `ReviewerSystemRole`, `OperatorSystemRole` | exact local system-role kind or its separate `SystemRoleKindDescription` episteme | A.2, F.4, F.5, F.18 |
| `AliceAsReviewer` | ordinary wording for a candidate classification, system-role assignment, or performed-Work attribution | A.2 with C.3, A.2.1, F.6, A.15.1 |
| `SeniorReviewer` | a proposed system-role-kind name that may hide a qualifier, assignment-state condition, capability, or assurance claim | A.2, A.2.2, A.2.5, B.3, F.18 |
| `RequestApproverSystemRole` | system-role-kind bundle expression or forbidden fused kind | A.2.7, F.8 |
| `AtRisk`, `Grace`, `PreValidated` | status value, window, confidence, or presentation label | F.10 or direct status pattern |
| `EvidenceRole`, `RequirementRole`, `AccessRole` | first recover the exact claim: evidence reliance, an actual assurance claim, ambiguous description use, publication occurrence or form, or a requirement, standard, source, access, or policy use | A.10 for evidence reliance; B.3 only for an actual assurance claim; E.10.D2 only to recover description-use ambiguity; E.24.PUB for publication occurrence, form, or carrier; otherwise the pattern that directly defines, constrains, or tests the recovered claim, or `missing-governor` |
| same spelling under two local-sense bases | two designations or an exact F.9 relation question | F.18, F.9; F.17 only at its public-row threshold |

#### F.14:7.2 - Reuse before minting

Reuse only when the exact recovered value, kind, direct pattern, proposed use, and admitted naming scope match. Try an existing designation, alias, local expression, or current row before creating a card, cell, row, policy id, or new U-kind candidate. Local-sense reuse does not imply sameness with another local sense; row reuse does not widen the row's admitted use.

#### F.14:7.3 - Use relations among system-role kinds before hybrid kinds

If two system-role kinds travel together, recover the exact A.2.7 bundle or qualification relation. If they must stay apart, recover the exact A.2.7 incompatibility. Use A.2.1 and any applicable A.2.5 currentness condition to identify the assignment occurrences. Use F.6 only when the receiving claim separately says that dated Work was performed under one of those assignments. If one kind can satisfy another requirement, recover exact substitution. The relation expression assigns no system and does not become a new kind by name.

#### F.14:7.4 - Use a status window before multiplying status families

If the proposed name marks evaluation, active use, grace, archival state, confidence, or presentation, keep the status family and use F.10 windows, values, or direct status-use relations. A new status family needs a recovered governed difference, not another adjective.

#### F.14:7.5 - Keep qualifiers with the claims they qualify

Time, location, object type, seniority, permission, Method, capability, evidence, source, and publication are not system-role-kind or status identity by suffix. Keep a qualifier with the claim it qualifies and use the pattern that defines, constrains, or tests that claim. Retain the qualifier in a durable name only when the already governed value and named use genuinely require that designation.

#### F.14:7.6 - Stop before a naming-object cascade

A candidate can justify one object without justifying all later objects. A durable local expression needs no cell; a stable local sense may need a cell but no NameCard; a durable naming settlement may need a NameCard but no public row; a row may exist without a current publication occurrence; publication availability creates neither row truth nor governed-value truth. Apply the next gate only when its own use is current.

### F.14:8 - Invariants

1. **Governed value first.** No durable naming object is added until the exact value or relation, kind, proposed use, and the pattern contribution that defines, constrains, or tests each needed claim are recoverable.
2. **Lightest sufficient disposition.** Prefer the dispositions `no durable name`, existing designation, alias, or local expression whenever one supports the use without hiding a distinction.
3. **No status roles.** Status, evidence, requirement, source, publication, and access uses do not become system-role kinds by suffix.
4. **No assignment by name.** A designation, `SystemRoleKindDescription`, system-role-kind relation expression, card, cell, or row assigns no system and proves no Work.
5. **No hybrid kind by convenience.** Exact A.2.7 relations remain relations unless A.2 with C.3 independently admits a different local system-role kind.
6. **No capability or authority by label.** System-role-kind and status names prove no capability, skill, permission, assurance, evidence use, Method validity, or publication authority.
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
systemRoleKindBundleRelation(K1, K2) obtains
  -> not(newSystemRoleKind(K1K2)).
```

```text
statusVariant(S, windowOrValue)
  -> keep status family S unless the pattern that defines the status claim establishes a different family.
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

Candidate family: `RequesterSystemRole`, `ApproverSystemRole`, `RequestApproverSystemRole`, `SeniorApprover`.

Premise: the local practice has already admitted `RequesterSystemRole` and `ApproverSystemRole` as exact local system-role kinds under A.2 with C.3. If that independent basis is absent, the case returns two candidates whose kind status is unresolved; the spellings do not admit them.

Result after that premise:

* Reuse the two admitted kinds and keep separate `SystemRoleKindDescription` epistemes only when descriptions are needed.
* `RequestApproverSystemRole` is blocked as a fused kind. Use an A.2.7 bundle relation when the two kinds travel together.
* If the same holder must not carry both assignments in the same change window, use the A.2.7 incompatibility relation. Recover the two assignment occurrences through A.2.1 and any applicable A.2.5 currentness condition. Use F.6 only if a separate claim says that dated Work was performed under one of them.
* `SeniorApprover` is not proof of independence or assurance. Recover the intended local system-role kind, exact assignment-state predicate or relation, capability, assurance, or policy claim before durable naming.

#### F.14:10.2 - Operators across shifts

Candidate family: `OperatorSystemRole`, `NightOperatorSystemRole`, `RemoteOperatorSystemRole`, `OnCallOperatorSystemRole`.

Premise: A.2 with C.3 has independently admitted `OperatorSystemRole` as an exact local system-role kind. Without that basis, `OperatorSystemRole` is still a candidate name and the case makes no kind claim.

Result after that premise:

* Reuse the admitted `OperatorSystemRole` kind.
* `night`, `remote`, and `on-call` are qualifiers in the proposed wording. Recover the claim each qualifies—for example, a schedule, location relation, `SystemRoleAssignmentStatePredicate`, WorkPlan, or policy condition—and use the pattern that defines, constrains, or tests that claim.
* A new system-role kind is blocked unless A.2 with C.3 independently admits a distinct local kind from its bounded work-facing contribution identity and a non-circular `KindSignature`. Its criterion may use, for example, a capability, Work, or an assignment established separately, but assignment conditions, a Method, and Work implications are not universal requirements. The naming ReferenceScheme does not create the kind or its difference.

#### F.14:10.3 - SLO compliance labels

Candidate family: `Compliant`, `AtRisk`, `Grace`, `Breached`, `Waived`.

Result:

* These are not system-role-kind names.
* F.10 recovers status family, status value, status window, confidence, or deontic or policy use.
* Presentation labels may stay local or be named by the direct status pattern. They do not become a system-role kind, `SystemRoleKindDescription`, or relation structure among system-role kinds.

#### F.14:10.4 - Evidence and requirement suffixes

Candidate family: `EvidenceRole`, `RequirementRole`, `StandardRole`, `SourceRole`.

Result:

* No work-facing system-role kind is recovered from suffix alone.
* Route each recovered claim separately: bounded evidence reliance goes to A.10; an actual named assurance claim goes to B.3; description-use ambiguity goes to E.10.D2 for recovery only; and publication occurrence, form, or carrier goes to E.24.PUB. A requirement, standard, source, access, or policy use goes to the pattern that directly defines, constrains, or tests that exact claim. If none exists, return `missing-governor`.
* A durable name may be admitted for the recovered relation, but not as a local system-role kind.

#### F.14:10.5 - Same spelling across two local-sense bases

A plant team uses `Operator` for one local system-role kind. An access-control team uses `Operator` for one permission grouping. Recover both independently under their direct patterns; neither spelling nor organizational proximity makes them one value.

For local use, keep the existing expressions and stop. If one named cross-local naming use is later proposed, resolve its exact F.17 `SchemeSenseCell` endpoints and test F.9. Cite a Bridge only when its predicate obtains, then state the use direction, rule, tolerated loss, polarity, and reliance separately. A Bridge, NameCard, cell, or row imports no access permission as `U.SystemRoleAssignment`, capability, authority, or performed Work. Publish an F.17 row only when the public or durable reuse threshold independently holds.

#### F.14:10.6 - Ordinary composite role-like phrases

A project says: "Vasya is an engineer, he works on musical robots, and he is also a musician who teaches robots to play music."

Result:

* Ordinary prose may remain `robotics engineer and musician` or `engineer-musician` when the sentence is clear and no FPF claim relies on either noun as an exact classification. Create no Tech kind merely to explain the phrase, and do not require a `SystemRole` suffix in ordinary prose.
* If the sentence supports a load-bearing FPF claim, apply E.10.ROLE and recover only the supported branch: for example, a local system-role kind and classification, an assignment occurrence, a capability, a participation or contribution relation, a Method or Work claim, or a finding that no pattern yet defines the needed claim. Do not infer two kinds from the two nouns.
* Any claim about an engineering or music-teaching Method, robot-training Work, or performed music Work stays under its direct pattern and remains separate from the ordinary phrase. Such a claim does not by itself justify a system-role-kind name.
* A durable qualified system-role-kind name becomes a candidate only after A.2 with C.3 independently admits that exact local kind and its bounded contribution identity. Differences in, for example, assignment conditions, capability expectations, incompatibilities, or Method or Work implications matter only when the `KindSignature` or named use actually consumes them. A readable suffix does not perform that admission.

### F.14:11 - Anti-patterns and repairs

| ID | Anti-pattern | Symptom | Repair |
| --- | --- | --- | --- |
| AP-1 | Hybrid-system-role minting | `RequestApproverSystemRole` becomes one kind. | Use exact A.2.7 relations; admit a new kind only under A.2 with C.3 and later naming gates. |
| AP-2 | Modifier-as-system-role | Every circumstance yields `NightOperatorSystemRole` or `RemoteOperatorSystemRole`. | Recover schedule, location, state, plan, or policy qualifier. |
| AP-3 | Status or evidence role | `ReadyReviewerSystemRole` or `EvidenceRole` becomes a system-role family. | Use F.10 for the recovered status claim. Route bounded evidence reliance to A.10, an actual assurance claim to B.3, description-use ambiguity to E.10.D2 for recovery only, and publication occurrence, form, or carrier to E.24.PUB. Route every other recovered requirement, standard, source, access, or policy claim to its direct pattern, or return `missing-governor`. |
| AP-4 | Prestige bypass | `SeniorReviewer` substitutes for assurance or separation. | Keep the system-role kind fixed and recover capability, state, assurance, policy, or assignment checks. |
| AP-5 | Row duplication | Another row is added for an already admitted name and use. | Reuse the exact row within its admitted use; retain old wording as lineage when useful. |
| AP-6 | Assignment hidden in a name | `AliceReviewerSystemRole` looks like a kind but encodes one assigned system. | Use A.2.1 to recover the exact assignment occurrence. Use F.6 only when a separate claim attributes dated Work to that assignment; keep the local system-role kind separate. |
| AP-7 | Method hidden in a system-role name | `PressureTestReviewerSystemRole` fuses a Method and a kind. | Keep the Method and system-role kind under their direct patterns; name either only after recovery. |
| AP-8 | Presentation as status family | Red, amber, or green becomes status ontology. | Recover the exact status criterion and keep display form separate. |
| AP-9 | Naming-object cascade | A word automatically gets a cell, card, row, id, and publication. | Apply each gate separately and stop at the lightest useful disposition. |
| AP-10 | Spelling-based cross-local identity | Same label merges values or automatically creates a Bridge. | Resolve exact local senses; test F.9 only for a named use and keep governed values distinct. |

### F.14:12 - Conformance checklist

| Check | Question |
| --- | --- |
| CC-F14-01 | Is each candidate tied to one independently recovered governed value or relation and proposed use, or explicitly left local? |
| CC-F14-02 | Were the light dispositions—no durable name, existing designation, alias, and local expression—tested before minting anything stronger? |
| CC-F14-03 | Are the system-role-kind designation, local kind, `SystemRoleKindDescription`, exact relation among kinds, assignment, capability, Method, and performed Work distinct? |
| CC-F14-04 | Are status family, value, window, use relation, evidence, and presentation distinct? |
| CC-F14-05 | Are effective naming ReferenceScheme and exact local-sense basis used instead of a generic context slot? |
| CC-F14-06 | Is a selected model-use structure absent unless its organization changes this exact naming use? |
| CC-F14-07 | Does any cited F.9 Bridge actually obtain between exact cells, with proposed use and reliance separate? |
| CC-F14-08 | Are NameCard, cell, row, id, publication occurrence, form, and carrier independently justified and mutually distinct? |
| CC-F14-09 | Does every stronger ontology, relation, system-role kind, status, Work, evidence, authority, or publication claim require its direct pattern? |
| CC-F14-10 | Are lineage spellings retained without carrying fused ontology or widening admitted use? |

### F.14:13 - Regression checks

Reopen only the affected naming use when candidate expressions grow faster than recovered values; a name starts carrying assignment, capability, method, Work, evidence, status, source, publication, equivalence, or authority; a row is reused beyond its admitted use; local wording is silently globalized; or one naming object begins to imply the next. A changed spelling alone does not require a new governed value or full family replay.

### F.14:14 - Relations

* **A.2, A.2.1, A.2.5, A.2.7, F.6, and A.15.1** define or constrain system-role kinds, assignments, assignment-state predicates and direct state relations, relations among system-role kinds, Work attribution, and Work. F.14 only blocks names that hide them.
* Use **F.8** to make one candidate's smallest mint-or-reuse disposition after the F.14 stop test.
* **F.9** defines only an actual relation between exact local senses. Shared spelling and cell presence establish none.
* **F.17** defines the public term-row form and its entry threshold; **F.18** defines the durable naming-settlement NameCard form; neither defines the governed value.
* Use **C.2.1** to identify every persisted NameCard, row, or control-record episteme and its `EpistemeEditionRelation`; use **E.24.PUB** to state row publication occurrence, expression form, and carrier bearing.
* Use **F.10, A.10, B.3, E.10.D2, and the direct policy, access, and source patterns** for the corresponding status, evidence, assurance, description, policy, access, and source claims that often arrive with role-like suffixes.

### F.14:15 - SoTA-Echoing

F.14 does not import access-control, terminology, credential, or modeling-language taxonomies as FPF ontology. It uses the sources below only where they change the anti-explosion rule.

| Anti-explosion question | Exact source and source-use status | Adoption or rejection in F.14 | Currentness and reopen condition |
|---|---|---|---|
| Why is a system-role-kind label insufficient for authorization? | Rose et al., NIST [SP 800-207, *Zero Trust Architecture*](https://doi.org/10.6028/NIST.SP.800-207) (2020), is a **current security-architecture reference** that separates a subject's access to a resource, policy decision, policy administration, and policy enforcement. | **Adapt the separation.** Keep the kind name, assigned System, request, requested resource and action, policy decision, permission, and Work distinct. Reject authorization, capability, or trust inferred from a system-role-kind label. | Reopen when NIST replaces SP 800-207 or a stronger authorization architecture changes the separation among subject, policy, decision, and enforcement used by this rule. |
| Why should role-like convenience names not replace an explicit policy relation? | Cutler et al., [*Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization*](https://arxiv.org/abs/2403.04651) (OOPSLA 2024 extended version), is a **current primary policy-language source** separating principal, action, resource, context, policy, and authorization decision while supporting role-, attribute-, and relation-based policies. | **Adapt only the explicit-policy lesson.** Recover the direct policy relation and its participants instead of minting a hybrid system-role kind. Reject importing Cedar entities, schema, or evaluator as FPF ontology. | Reopen if current policy-language practice shows that the explicit boundary between participants and policy no longer prevents the name explosion addressed here. |
| Why must a governed value be recovered before a durable designation or family is minted? | [ISO 704:2022](https://www.iso.org/standard/79077.html) is a **current terminology standard** connecting objects, concepts, definitions, and designations. | **Adopt.** Recover the value and use first; then choose no durable name, an existing designation, a local expression, a NameCard, or a public row only at its own trigger. Reject shared spelling as value identity or semantic equivalence. | Reopen when ISO 704 or F.17 and F.18 change the distinction between a value and its designation or the publication threshold used here. |
| Why are credential presentation, status, and relying use different from the governed value? | W3C [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (2025) is a **current W3C Recommendation** separating issuer, subject, holder, verifier, credential, presentation, and credential status, and leaving authorization decisions outside the data model. | **Adapt.** Keep status, evidence, credential, view, verifier action, and relying decision distinct. Reject a suffix, badge, credential view, or dashboard row as a system-role kind, assignment, permission, assurance, or decision. | Reopen when the VC Recommendation or its status family changes the boundaries among presentation, status, and relying use applied in the worked cases. |

SysML is intentionally excluded from the positive SoTA basis and from lineage for this pattern. The official [OMG SysML 2.0 specification](https://www.omg.org/spec/SysML/2.0) (September 2025) is recorded only as a **rejected-popular comparison**: a modeling-language role spelling does not independently establish FPF's local system-role kind, classification, assignment, capability, permission, Method, or Work. Official status and popularity are not evidence for this anti-explosion question. Reopen that rejection only if demonstrated practice supplies a directly relevant, lower-cost kind-admission and assignment boundary that improves the F.14 cases.

### F.14:16 - Didactic distillation

When names multiply, do not ask for a better name first. Recover the exact values and the proposed use. Try no durable name, an existing designation, an alias, or a local expression. Keep relations among system-role kinds, status windows, capability, Method, Work, evidence, source, policy, and publication under their direct patterns. Create a cell, NameCard, row, identifier, or publication only when that exact object buys a named use; none requires the next and none makes the governed value real.

### F.14:End

