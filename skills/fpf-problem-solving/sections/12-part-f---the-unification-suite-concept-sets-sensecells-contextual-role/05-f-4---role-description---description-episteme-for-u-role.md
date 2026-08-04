## F.4 - Role Description - Description Episteme for U.Role

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### F.4:0 - Use This When

**Plain name.** Role-description episteme.

Use this pattern when a project needs a short, reusable description that makes one work-facing `U.Role` recognizable, teachable, and checkable under one named role-taxonomy episteme and effective `U.ReferenceScheme`.

Typical moments:

- a project has a role name such as `ReviewerRole`, `OperatorRole`, `InspectorRole`, `TransformerRole`, `ShipyardCoordinatorRole`, or `ModelCardReviewerRole`, but the governing role-taxonomy episteme, effective reference scheme, admitted holder kind, role invariants, capability conditions, or work-facing boundary are unclear;
- a method description names required roles, but readers cannot tell what role value is required before a `U.RoleAssignment` can be checked;
- a role name is starting to carry method, capability, work, permission, evidence, publication, or status claims that belong to neighboring patterns;
- a former source phrase says that a report, standard, dataset, theorem, dashboard, publication, or requirement has a "role" and the text must decide whether that phrase is a real work-facing role description or a direct episteme-use relation.

**Primary EntityOfConcern.** The exact C.2.1 EntityOfConcern of the role-description episteme is the described `U.Role` value. The governed object is one `U.Episteme` constituted under `C.2.1` by its exact ClaimGraph, that role value, and the effective `U.ReferenceScheme`; its claims name the role-taxonomy episteme that supplies the vocabulary. The role-description episteme is not the role value itself, holder, role assignment, capability, method description, performed work, status-use relation, or publication form.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, or pattern author who must let people recognize a role while keeping role value, holder, assignment, capability, method, work, evidence use, status use, and publication use distinct.

**First useful move.** Name the role value, its role-taxonomy episteme, the effective reference scheme, the admitted holder kind, and the smallest role invariants needed by the next assignment, method, work, naming, or bridge claim.

**What goes wrong if missed.** A role-description card becomes a hidden method, access policy, permission badge, evidence relation, status assertion, staffing plan, or work log. Then FPF grows one role ontology for acting holons and a second role-like ontology for epistemes, publications, statuses, and relation positions.

**What this buys.** A project can publish a compact, human-readable role description while keeping operational claims in their direct patterns. The role remains recognizable; the assignment remains checkable; capability, method, work, evidence, status, and publication claims stay inspectable instead of being smuggled into the role name.

**Not this pattern when.**

- If the current claim is the role value itself or role taxonomy, use `A.2`.
- If the current claim is which admitted system holds which role and during which uninterrupted assignment occurrence, use `A.2.1`.
- If the current claim is role state or enactable-state admission, use `A.2.5`.
- If the current claim is role-requirement substitution, role incompatibility, role-factor qualification, or bundle expression, use `A.2.7`.
- If the current claim is capability, use `A.2.2`.
- If the current claim is method, method description, work plan, or performed work, use `A.15` and its neighbors.
- If the current claim is evidence use, status use, source use, standard use, requirement use, publication use, assurance use, gate use, or decision use of an episteme, use the direct pattern for that relation. Do not call that episteme a role holder.
- If the current issue is only a durable name, use `F.18`.
- If the current issue is correspondence between role meanings under different taxonomies or reference schemes, use `F.9`.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.

### F.4:1 - Problem Frame

Role descriptions are useful because a role value needs a recognizable description before people can assign it, name it, compare it, or use it in a method condition. A role such as `InspectorRole` is not self-explanatory. The project needs the exact role-taxonomy episteme and effective reference scheme that give the value its current meaning, the admitted holder kind, the role invariants that matter, and the neighboring checks that may become current.

The recurring failure is to make the role description carry too much. A compact card is tempting: put role, status, permission, evidence, capability, method, assignment, work, and publication cues into one "assignable" template. That looks convenient but creates duplicate ontology. A standard used as a requirement source becomes a "standard role"; a report used as evidence becomes an "evidence role"; an access-control label becomes a behavioral role; a role name becomes proof of capability or proof that work occurred.

F.4 therefore treats a role description as a description episteme about a work-facing `U.Role`. It may mention neighboring relations, but it does not absorb them.

### F.4:2 - Problem

Without this pattern:

1. **Role description and role value collapse.** The description is treated as if it were the `U.Role` value.
2. **Role description and assignment collapse.** A role name or card is treated as proof that a holder has the role.
3. **Role description and capability collapse.** A role name is treated as evidence that the holder can do the work.
4. **Role description and method collapse.** Role invariants become a hidden procedure or method description.
5. **Role description and performed work collapse.** A role card is treated as evidence that work happened.
6. **Status and evidence uses become roles.** Epistemes, publications, standards, datasets, and claims are put into role language because they are used in project reasoning.
7. **Relation positions become roles.** Slot positions in signatures, interfaces, evidence relations, or status-use relations are called roles.
8. **Cross-context labels overreach.** The same role-like word in two contexts is treated as one role description without a bridge.

### F.4:3 - Forces

| Force | Tension |
| --- | --- |
| Recognition vs ontology | A role description must be easy to read, but it cannot replace the role value, assignment relation, capability, method, or work occurrence. |
| Local meaning vs reuse | Role descriptions are interpreted through one role-taxonomy episteme and effective scheme, while labels may later need a bridge across taxonomies or schemes. |
| Compactness vs completeness | A useful card is small, but the current claim may require neighboring checks for state, capability, method, assignment, evidence, or status. |
| Open-world use vs form burden | Some uses need only a role gloss; stronger uses need slot dispositions and neighboring references without pretending every slot is always filled. |
| Work-facing role ontology vs episteme-use ontology | Acting holons can hold work-facing roles. Epistemes are used through evidence, status, source, publication, requirement, explanation, assurance, or gate relations. |

### F.4:4 - Solution

Constitute one role-description episteme through `C.2.1`: its exact ClaimGraph describes one `U.Role`, that role is the EntityOfConcern, and one effective `U.ReferenceScheme` governs interpretation. The ClaimGraph names the exact role-taxonomy episteme that supplies the role vocabulary. The description gives readers enough to recognize and check the role while routing neighboring claims to their direct patterns.

The following is a content checklist, not a relation signature or a mandatory record:

**Always make recoverable:**

- the described `U.Role`;
- the role-taxonomy episteme and effective reference scheme;
- a short recognition explanation;
- the independently admitted `U.System` holder kind and, when needed, a reference to its separately governed admission claim;
- the smallest role-invariant set needed by the current use;
- the non-role boundary: what this description does not assert about assignment, capability, method, work, evidence, status, permission, publication, or relation slots.

**Add only when the current use depends on them:**

- role-state predicate references under `A.2.5`;
- capability-condition references under `A.2.2`;
- method or method-description references under `A.3.1`, `A.3.2`, or `A.15`;
- durable-name or alias references under `F.18`;
- bridge references under `F.9`;
- a selected `BoundedModelUseStructure` designated by the receiving assertion or use when it changes that interpretation.

These are claims and neighboring references in an episteme. They are not `SlotSpec` declarations and do not add participants to `U.RoleAssignment` or another generic role relation. A card, table row, method appendix, or pattern section may publish the description; publication form and carrier remain separate from the episteme.

#### F.4:4.1 - Content Meanings

| Content element | Meaning |
| --- | --- |
| Described role | The exact `U.Role` that is the episteme's EntityOfConcern. |
| Role taxonomy and effective scheme | The exact episteme and by-value interpretation scheme under which the role vocabulary is read. |
| Eligible holder kind | Which independently admitted `U.System` kind may participate as holder in `U.RoleAssignment`; the description itself admits nobody and creates no assignment. |
| Recognition explanation | The first-minute explanation that lets a reader distinguish this role from neighboring roles. |
| Role invariants | Conditions about the role value that remain current under the named taxonomy and scheme. |
| Conditional neighboring references | Direct exits for role state, capability, method, naming, and bridges only when the receiving use depends on them. |
| Non-role boundary | The explicit separation from assignment, work, evidence, status, permission, publication, and relation-slot claims. |

A quick local description can stop after the always-recoverable content. A consequence-bearing work-admission use opens only the neighboring relations it actually needs.

#### F.4:4.2 - Role Description vs Neighboring Values

Keep these distinctions:

| Current claim | Governing pattern |
| --- | --- |
| What role value is this? | `A.2` |
| Which admitted system holds the role, and during which assignment occurrence? | `A.2.1` |
| Is the assignment in an admitted role state? | `A.2.5` |
| Can the holder do the relevant work? | `A.2.2` |
| Which method, method description, plan, or work occurrence is current? | `A.15`, `A.15.1`, `A.15.2`, `A.3.1`, `A.3.2` |
| How do role values satisfy admission conditions, conflict, qualify, or bundle under one interpreted taxonomy and scheme? | `A.2.7` |
| What durable name should this role have? | `F.18` |
| How do role meanings compare across taxonomies or schemes? | `F.9` |
| How is an episteme used as evidence, source, standard, requirement, status bearer, publication, or assurance input? | Direct episteme-use, evidence-use, status-use, source-use, publication-use, requirement-use, or assurance pattern |
| Which relation position admits which filler kind? | `A.6.5` |

F.4 may point to these patterns; it does not copy their ontology.

#### F.4:4.3 - Positive Construction Rule

Write a role description in this order:

1. Name the described `U.Role`, its role-taxonomy episteme, and effective reference scheme.
2. State the independently admitted holder kind eligible for role assignment.
3. Give one short recognition paragraph.
4. List the role invariants that make the role different from neighboring roles.
5. State the non-role boundary: what this description does not say about assignment, capability, method, work, evidence, status, permission, publication, or slot positions.
6. Add neighboring references only when the current use depends on them.
7. If the name is durable, public, or Core-facing, settle it through `F.18`; if role meanings must be compared across taxonomies or schemes, use `F.9`.

### F.4:5 - Invariants

1. **One described role.** A role description describes exactly one `U.Role` value in the current application.
2. **One interpreted role meaning.** Name one role-taxonomy episteme and effective reference scheme; correspondence to another taxonomy or scheme needs `F.9`.
3. **Description boundary.** The role description is a `U.Episteme`; it is not the role value, assignment relation, holder, capability, method, work, or status-use relation.
4. **Work-facing holder boundary.** The holder participating in an obtaining role assignment is an independently admitted `U.System`; the assignment does not perform that admission. An episteme is not a role holder because it is used as evidence, source, standard, specification, definition, explanation, status bearer, publication, or assurance basis.
5. **No hidden capability.** Capability requirements may be referenced, but the role description does not prove capability.
6. **No hidden method.** Method requirements may be referenced, but the role description is not a method description.
7. **No hidden work.** A role description may enable work attribution checks, but it is not evidence that work occurred.
8. **No status-template fusion.** Status-use and evidence-use relations are direct relations, not a second branch of role description.
9. **Slot discipline.** If a source says "role" for a relation position, recover `SlotKind`, `ValueKind`, and `RefKind` through `A.6.5`.
10. **Name after meaning.** Durable naming follows `F.18` only after the role value, role-taxonomy episteme, effective scheme, and local sense are recovered.

### F.4:6 - Reasoning Primitives

Use these judgement schemas as thinking checks.

```text
RoleDescription RD describes Role R under taxonomy episteme T and scheme S
  -> RD is a C.2.1 episteme about R, not R, T, or S themselves.
```

```text
RoleDescription RD names independently admitted U.System holder kind HK for Role R
  -> A RoleAssignment may use a holder of HK only after that exact holder satisfies A.1 and the assignment's exact participants satisfy A.2.1; RD establishes neither.
```

```text
RoleDescription RD lists capability requirement CapReq
  -> capability claim is governed by A.2.2, not by RD.
```

```text
RoleDescription RD lists method requirement MReq
  -> method or method-description claim is governed by A.15, A.3.1, or A.3.2.
```

```text
Source says "X has role Y" and X is an episteme
  -> recover direct episteme-use relation before considering U.Role.
```

### F.4:7 - Worked Cases

#### F.4:7.1 - Pump Inspector Role

`PumpInspectorRoleDescription` is a C.2.1 episteme whose EntityOfConcern is `PumpInspectorRole`, whose effective scheme is `Plant-A-Maintenance-Scheme`, and whose ClaimGraph names `PlantMaintenanceRoles-2026` as the governing role-taxonomy episteme. Its recognition explanation says that the role is used for inspecting pump condition before maintenance work is admitted. It names maintenance-technician, inspection-robot, or service-team `U.System` kinds as eligible holder kinds only when each exact system kind and any current holder entity are independently admitted; the description itself admits neither a system nor an assignment.

Its role invariants say that the role concerns pump-condition inspection, does not itself perform repair, and requires a current assignment before work attribution. It references pump-inspection capability conditions or the inspection method only when a receiving work claim needs them. Its non-role boundary states that an inspection report is an episteme used through direct evaluation, evidence, source, or publication relations, not a role holder.

The description makes `PumpInspectorRole` recognizable. It does not say that Robot-7 holds the role, can inspect, followed the method, or performed work. Those claims go to `A.2.1`, `A.2.2`, `A.15`, and the direct evaluation or evidence patterns.

#### F.4:7.2 - Reviewer Role and Review Report

`ReviewerRole` under `PatternReviewRoles-2026` and `Pattern-Review-Scheme` may have a role-description episteme with invariants about checking a pattern against declared scales. A review report produced by a reviewer is an episteme used as evidence or source for a pattern-quality claim. The report is not the role holder and does not hold an evidence role.

Use:

- `A.2` for `ReviewerRole`;
- `F.4` for the role-description episteme;
- `A.2.1` for Alice's exact `ReviewerRole` assignment under that taxonomy and scheme;
- `A.15.1` for the review work occurrence;
- `A.10`, `B.3`, `G.6`, or a direct evidence-use pattern for the review report as evidence.

#### F.4:7.3 - Standard Used as a Specification or Source

The sentence `Standard S has the architecture-standard role in this work` is unsafe if it makes the standard episteme a role holder. Repair it by naming the direct relation: the exact edition of Standard S is used as a specification, external rule, premise, or source for named claims in the receiving work. Only an admitted `U.System` can hold a work-facing role. The standard may constrain or support a claim through its direct episteme-use relation.

#### F.4:7.4 - Access Role Is Not Automatically Work-Facing Role

RBAC `role` often names a permission grouping. If the current claim is permission or access standing, use the status, policy, or deontic governing pattern. Do not describe it as `U.Role` unless the role taxonomy and effective scheme explicitly introduce a work-facing role value and the holder, assignment, method, and work claims are current.

### F.4:8 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Role-description as assignment | A card says `the inspector is assigned` without the exact holder, role taxonomy, effective scheme, or assignment episode. | Use `A.2.1`; keep F.4 for description of the role value. |
| Role-description as capability proof | "ReviewerRole can verify formal models." | Put capability under `A.2.2`; F.4 may reference the requirement. |
| Role-description as method | A role description contains a procedure. | Move the procedure to method or method-description patterns. |
| Role-description as work evidence | A role card is cited as proof that review occurred. | Use `U.Work` and evidence-use patterns. |
| Episteme as role holder | A report, standard, dataset, theorem, dashboard, or publication is said to hold a role. | Recover evidence-use, source-use, standard-use, requirement-use, publication-use, status-use, or assurance-use relation. |
| Status-template fusion | A status, permission, or evidence standing is made a second kind of role description. | Use direct status-use, policy, or evidence patterns. |
| Slot position as role | "The subject role in this relation..." | Use `A.6.5` SlotKind and ValueKind wording. |
| Bridge by label | The same role-like label under two taxonomies or schemes is treated as one role. | Use `F.9` Bridge and `F.18` naming discipline. |

### F.4:9 - Consequences

**Benefits.**

- Role descriptions become short enough for practical use while preserving ontology.
- Part F naming and bridge patterns can rely on role descriptions without inheriting assignment, capability, method, work, evidence, or status claims.
- Episteme-use relations stay direct and do not become a parallel role ontology.
- Method and work checks can cite role descriptions without treating them as work evidence.

**Costs.**

- Former "role-or-status template" material must move to F.10, A.2.4, B.3, A.10, E.17, G.6, or direct use patterns.
- A stronger claim may require several neighboring patterns instead of one overloaded role card.
- Durable names require `F.18` when the role name is public, Core-facing, or cross-context.

### F.4:10 - SoTA-Echoing and Source-Use

| Practice line | What FPF takes | Practical implication |
| --- | --- | --- |
| Role modeling in organizations, access-control, safety, and method engineering separates role labels, assigned holders, permissions, responsibilities, and performed work. | F.4 keeps only the role-description episteme and sends assignment, permission, capability, method, and work to direct patterns. | A readable role description does not become an access policy, staffing record, or work log. |
| Role-taxonomy and interoperability practice keeps local role meanings scheme-relative and compares them by explicit correspondences, not shared labels. | F.4 names the role-taxonomy episteme and effective scheme; cross-taxonomy or cross-scheme comparison goes through `F.9`. | Same label does not make the same role meaning. |
| FPF episteme and publication ontology separates the described entity, description episteme, and publication form. | A role description is a description episteme about `U.Role`; a card or table may publish it. | Editing the publication is not automatically changing the role value or assignment relation. |
| FPF slot discipline separates relation positions from fillers. | "Role" in a relation-position phrase is repaired to SlotKind or ValueKind when no work-facing `U.Role` is current. | Slot names do not create role values. |

Current best-known pressure for this problem is not a larger universal role taxonomy. It is explicit separation of local role value, assignment, attributes or capability, permission or policy standing, performed work, and evidence or status use. RBAC, ABAC, zero-trust authorization, safety independence practice, method engineering, and FPF slot discipline all push in that direction, while F.4 keeps only the role-description episteme and hands the neighboring claims to direct patterns.

Currentness and reopen condition: reopen this pattern when `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.15`, `A.6.5`, `C.2.1`, `F.9`, `F.10`, `F.18`, or the accepted episteme-use and status-use discipline changes enough that role-description, holder admission, or non-role-use boundaries would be stated differently.

### F.4:11 - Relations

**Builds on.** `A.2`, `A.2.1`, `A.6.5`, `A.7`, `C.2.1`, `E.10.D2`, and `E.24`.

**Coordinates with.** `A.2.2`, `A.2.5`, `A.2.7`, `A.15`, `A.15.1`, `A.15.2`, `F.9`, `F.10`, `F.14`, `F.15`, `F.18`, evidence-use, status-use, source-use, publication-use, requirement-use, and assurance patterns.

**Constrains.**

- `F.5` must name role descriptions after the described `U.Role`, role-taxonomy episteme, effective reference scheme, and local sense are recovered.
- `F.8` must decide durable role-name minting or reuse without turning status-use or episteme-use relations into role descriptions.
- `F.14` must treat bundles and separation-of-duties as role relation structure or neighboring role-description claims, not as hybrid role descriptions.
- `F.15` must check role-description single-role and non-role-use boundaries.

### F.4:12 - Conformance Checklist

| Check | Question |
| --- | --- |
| `CC-F4-01` | Is the role-description episteme's exact C.2.1 EntityOfConcern exactly one described `U.Role` value? |
| `CC-F4-02` | Are the exact role-taxonomy episteme and effective `U.ReferenceScheme` named? |
| `CC-F4-03` | Is the description kept separate from the role value and any publication form? |
| `CC-F4-04` | Is every named eligible holder kind an independently admitted `U.System` kind, with any actual holder and assignment recovered separately under A.1 and A.2.1? |
| `CC-F4-05` | Are assignment claims sent to `A.2.1`? |
| `CC-F4-06` | Are capability claims sent to `A.2.2`? |
| `CC-F4-07` | Are method, plan, and work claims sent to `A.15` and neighboring patterns? |
| `CC-F4-08` | Are evidence, source, standard, requirement, publication, assurance, and status uses sent to direct episteme-use patterns? |
| `CC-F4-09` | Are relation-position "role" words sent to `A.6.5`? |
| `CC-F4-10` | Are durable or cross-context names sent to `F.18` and `F.9` when current? |
| `CC-F4-11` | Are open-world missing slots treated as unknown, not recovered, not asserted, or not current rather than false? |

### F.4:13 - Phrasebook

Prefer:

- `role-description episteme describing ReviewerRole under ReviewRoles-v5 and Review-Scheme-A`;
- "holder-system admission is established under A.1 and E.24.UK; any actual `ReviewerRole` assignment is governed by A.2.1";
- "capability requirement referenced by the role description";
- "method requirement referenced by the role description";
- "review report used as evidence for the claim";
- "standard used as requirement source";
- "relation position governed by SlotSpec discipline".

Avoid as live vocabulary:

- "evidence role" for an episteme;
- "status role" for a badge or status-use relation;
- "standard role" for a standard used as source;
- "holder" for a publication, report, standard, dataset, or theorem unless the exact entity is independently admitted as a `U.System` and a current `U.RoleAssignment` names it as holder;
- "role" for a SlotKind;
- "role description" for a method, capability, work record, access policy, or status-use relation.

### F.4:14 - Didactic Memory

A role description is the readable episteme that tells people what a role value means under one named role-taxonomy episteme and effective reference scheme. It helps someone assign, check, name, or compare the role. It does not assign the role, prove capability, define the method, perform the work, grant permission, carry evidence, publish itself, or turn every useful episteme into a role holder.

### F.4:End

