## F.5 - Naming Discipline for U-kind Names and SystemRoleKindDescription Labels

> **Type:** Definitional (D)
> **Status:** Stable in the current FPF
> **Normativity:** Normative unless marked informative

### F.5:0 - Use This When

**Plain name.** Meaning-first naming discipline.

Use F.5 when a project needs a durable name for either:

- a public U-kind already admitted through E.24.UK, or another durable cross-local value whose defining membership rule is satisfied; a Concept-Set row may cite comparison evidence but does not admit the value; or
- one exact local system-role kind and, when needed, the separate `SystemRoleKindDescription` episteme that describes it.

Typical moments:

- a Concept-Set comparison has enough witnesses for a naming question and the reusable value is already admitted, but candidate names import one source tradition too strongly;
- an F.4 description names `ReviewerSystemRole`, `OperatorSystemRole`, `InspectorSystemRole`, or `TransformerSystemRole`, and the label must remain faithful to the exact local kind without smuggling assignment, capability, permission, Method, Work, evidence, status, or responsibility;
- source wording with *role* must be named locally, but the project has not yet recovered its use—for example, a system-role kind, assignment, status or access relation, relation position, another object, or ordinary wording; or
- similar names threaten to collapse independently governed objects—for example, a kind, assignment, status, Method, Work occurrence, and description episteme.

**Primary EntityOfConcern.** The EntityOfConcern is the naming discipline for these name families. It relates a recovered meaning to selected Tech and Plain designations. It defines neither the named U-kind nor the local system-role kind, constitutes no description, classifies no candidate, creates no assignment, asserts no status or responsibility, supplies no evidence, and publishes no form.

**Primary working reader.** The first reader is a practitioner who already has a candidate meaning and must choose a name that readers can use without creating another ontology—for example, an engineer-manager, analyst, pattern author, or terminology steward.

**First useful move.** Recover the exact named value and its direct meaning source before choosing the label. For a U-kind, use its accepted E.24.UK admission result or its direct admission rule. For a local system-role kind, use its A.2 and C.3 identity and criterion; use F.4 for the separate description episteme. Then choose one Tech label and one short Plain explanation whose scope does not exceed the recovered meaning.

**Smallest useful result and stop.** Stop with one already identified value, one Tech label, and one Plain explanation as soon as they resolve unambiguously for the named local use. Do not create a NameCard, public row, Bridge, description episteme, or new kind merely to complete a form. If the value or kind is unresolved, apply its admission or relation-defining rule. Use F.18 or F.17 only for the durable or public use they address. Use C.3.3 only for an actual relation between exact local kinds and F.9 only for an actual relation between distinct F.17 cells. If the label starts carrying assignment, Work, result, provenance, assurance, responsibility, or publication claims, stop naming and recover those objects first.

**What goes wrong if missed.** Names become arguments. A system-role-kind label smuggles in neighboring claims—for example, assignment, permission, responsibility, or capability. A status phrase becomes a system-role kind. A U-kind name imports one practice's or source's private ontology. A polished global word hides disagreement among witnesses. Downstream patterns then repair semantics that naming already broke.

**What this buys.** Readers can use short names without guessing the ontology. U-kind names stay neutral across witnesses. Concrete `...SystemRole` designations point to exact local kinds, and `...SystemRoleKindDescription` designations point to their separate description epistemes. Names for neighboring claims—for example, status, evidence, access, requirement, source, publication, assurance, gate, and decision claims—remain with their direct relations.

**Not this pattern when.**

- If the problem is ordinary phrase repair, use E.10, E.10.ROLE, E.10.ARCH, A.6.P, A.6.RSIR, or the direct pattern.
- If the question is whether a `U.*` spelling or structural name should survive as a durable U-kind, use E.24.UK before F.5.
- If the broader local-first protocol, NameCards, candidate comparisons, lineage, or public naming is current, use F.18.
- If the current object is a `SystemRoleKindDescription`, use F.4 to constitute it before naming it.
- If the question concerns kind admission, classification, assignment, assignment extent, or performed-Work attribution, use A.2 with C.3, A.2.1, or F.6.
- If the current object is another governed value rather than a name—for example, a status, evidence use, source use, standard use, requirement use, publication use, assurance claim, gate result, or decision—use its direct pattern.
- If *role* denotes a relation position, recover the position under A.6.RSIR and A.6.5.
- If an actual cross-local relation is current, use C.3.3 for exact local kinds or F.9 for distinct F.17 cells.

### F.5:1 - Problem Frame

FPF needs names that humans can use without dragging the wrong ontology behind them. A good name is short enough for documents and conversation, but it belongs to a recovered meaning.

This pattern keeps two recurrent naming tasks separate.

First, a public U-kind gets a name only after E.24.UK admits the exact value; another durable cross-local value gets a name only after it satisfies its defining membership rule. A Concept-Set row may preserve witness comparison and evidence; it neither admits nor identifies the value. The name should be neutral across witnesses and no wider than the admitted invariants.

Second, one concrete local system-role kind receives a `...SystemRole` designation after A.2 and C.3 settle the practice or source boundary in which it is constituted, its stable work-facing contribution distinction, and its criterion. `SystemRole` is common morphology, not a universal kind. An F.4 description episteme is another object and may receive a separate `...SystemRoleKindDescription` name. Neither label creates the kind, description, classification, or assignment.

The tempting shortcut is to make system-role descriptions cover statuses and episteme uses because all need labels. That convenience creates duplicate ontology. Another governed value—for example, a status, evidence use, permission, or publication—may need a name; none becomes a system-role kind because it is named.

### F.5:2 - Problem

Without this pattern:

1. **Local terms look global.** `Observation`, `Activity`, or `Process` becomes a U-kind name although it carries one practice's or source's private commitments.
2. **System-role names become hidden admissions.** A label such as `ReviewerSystemRole` is treated as if the local kind or candidate classification already exists.
3. **System-role names become hidden assignments.** A concrete kind label is treated as if someone is already assigned.
4. **System-role names become capability claims.** A candidate is assumed able because the kind label sounds competent.
5. **System-role names become Methods.** A noun label hides a Method or Method family.
6. **Description and described kind collapse.** `PumpInspectorSystemRoleKindDescription` is treated as `PumpInspectorSystemRole` itself.
7. **Status names become system-role kinds.** For example, `Approved`, `AccessRole`, `ModelFitEvidenceRole`, or `RequirementRole` creates a fake work-facing classification instead of the exact direct relation.
8. **Relation positions become system-role kinds.** Signature, relation, or argument-position names borrow role morphology even though they name participation or a declaration place.
9. **Names carry interpretation metadata.** `Task-IEC61131`, `Participant-BPMN`, or `ReviewerSystemRole-SchemeA` fossilizes an edition, source, local boundary, or scheme in the label.
10. **Aliases become silent renames.** Several labels circulate for one meaning without lineage or Bridge discipline.

### F.5:3 - Forces

| Force | Tension |
| --- | --- |
| Local fit versus cross-local neutrality | A local system-role-kind name must fit the named practice or source use; a public U-kind name must not privilege one witness. |
| Brevity versus object recovery | A usable name must still let a reader distinguish kind, description, classification, assignment, status, Method, Work, relation, and episteme use. |
| Teaching versus widening | A Plain designation should help readers without broadening the Tech designation. |
| Stability versus changed meaning | Names should survive harmless edition or publication changes, but real sense changes need a split, rename, or lineage record. |
| Morphology versus ontology | Word form guides expectations but establishes no kind. `SystemRole` does not create a universal kind or assignment. |
| Open-world use versus name burden | A lightweight local label may be enough; durable public reuse can require F.18 or F.17, and an actual cross-local relation can require C.3.3 or F.9. |

### F.5:4 - Solution

Name after meaning. Recover the value, its kind, direct meaning source, and intended use. Then choose designations that preserve them.

Make these facts recoverable in the prose, direct admission, F.4 description, Concept-Set row, or NameCard. This is a naming checklist, not a relation signature or mandatory record:

- the exact named value and its admitted kind;
- the direct source of its meaning;
- for a local system-role-kind designation, the practice or source boundary in which the kind is constituted, its stable work-facing contribution distinction, current `KindSignature`, and effective scheme;
- for a description name, the separate F.4 `SystemRoleKindDescription` and its exact EntityOfConcern;
- the selected Tech and Plain designations;
- aliases or predecessor labels with lineage;
- morphology, neutrality, and minimal-generality checks; and
- the boundary that prevents the name from absorbing classification, assignment, capability, Method, Work, status, evidence, permission, responsibility, publication, or relation-position claims.

#### F.5:4.1 - Name Families Used Here

| Name family | Meaning source | Naming rule |
| --- | --- | --- |
| Public U-kind or durable cross-local value name | Public U-kind admitted through E.24.UK, or another exact value that satisfies its defining membership rule; a Concept-Set row may retain witness comparison but supplies neither identity nor admission | Use a neutral Tech head at minimal generality. Do not let one witness's private vocabulary win by spelling alone. |
| Concrete local system-role-kind designation | Exact C.3 kind admitted under A.2, with a named practice or source boundary, stable work-facing contribution distinction, direct criterion, and local sense | Use a concrete `...SystemRole` Tech designation. `SystemRole` is morphology, not a universal value; do not add `Kind` when `: U.Kind` is already explicit. |
| `SystemRoleKindDescription` designation | F.4 description episteme whose exact EntityOfConcern is one local system-role kind | Name the description separately, for example `PumpInspectorSystemRoleKindDescription`; never use the description name as the kind or assignment name. |
| Relation among system-role kinds or a system-role–Method expression | Exact relation under A.2.7 and, when current, a separately recovered Method, MethodDescription, or Work | Name the recovered relation or neighboring object. Ordinary phrasing may stay compact but must not hide independent classifications or assignments. |
| Method, Method family, Method relation structure, WorkPlan, or Work name | A.3, A.15, G.5, and the exact composition or Work pattern | Name that object directly. Shared words with a system-role-kind label create no relation or identity. |
| Mathematical or representation lens name | Description of a selected system-role-kind relation structure, Method relation structure, transformation-flow structure, or another governed structure | Name the lens only when the representation is itself the governed value. Otherwise name the underlying structure or relation. |
| Status, evidence, requirement, source, standard, publication, assurance, gate, or decision name | Exact direct relation or value | Do not treat it as a `SystemRoleKindDescription` branch. Use F.18 only after the direct object is recovered. |
| Relation slot or argument-position name | A.6.RSIR, A.6.5, and the exact relation or signature declaration | Name the participant meaning, slot, or argument position. Do not use `SystemRole` morphology unless the value is independently a local system-role kind. |

For every system-role-facing naming use, keep these objects distinct: selected designation `L`, local system-role kind `K`, optional F.4 description episteme `D`, and any assignment occurrence `A` that the current use actually needs. Under the effective scheme, `L` designates `K`; under C.2.1, `D` has `K` as EntityOfConcern. Under A.2.1, `A` must be an occurrence whose species is declared under `U.SystemRoleAssignment`, not an occurrence admitted by a generic two-place signature. That species declares a holder slot for an admitted `U.System`, one declaration-local assigned-kind slot whose domain is the exact local system-role-kind domain containing `K`, its own predicate and applicability, its uninterrupted occurrence-identity rule, and any real additional identity-bearing participant. In `A`, the holder slot identifies the admitted holder system and the assigned-kind slot identifies `K`. If assignment identity is not part of the naming use, stop with the naming objects and say only that any assignment remains a separate A.2.1 claim; do not invent `A`. Spelling, suffix, NameCard, public row, description, or citation creates none of the other objects or any dated Work, result episteme, provenance record, or publication occurrence.

#### F.5:4.2 - Tech and Plain Designations

Use two human-facing designations when a name is durable enough to be reused:

| Designation | Job | Constraint |
| --- | --- | --- |
| Tech designation | Stable label used by the local pattern, table, or description episteme | Must fit the recovered kind and exact meaning source. |
| Plain designation | Short teaching phrase or sentence | Must point to the same value without widening the sense. |
| Symbol or source abbreviation | Optional local notation or lineage spelling | Informative only; it is not another selected Tech or Plain designation. |

For a concrete local system-role kind, the Tech designation normally ends in `...SystemRole`, for example `ReviewerSystemRole` or `PumpInspectorSystemRole`. The Plain designation may remain ordinary, for example “reviewer” or “pump inspector”, when the named practice and criterion make the intended kind clear. Add “system role” only when it prevents a live neighboring reading. The compound does not imply non-human technical systems, kind admission, candidate classification, assignment, agency, capability, Method, or Work.

For the description episteme, name the description rather than the described kind: `PumpInspectorSystemRoleKindDescription` may have Plain designation “description of the pump-inspector system-role kind”. `SystemRoleKindDescription` identifies the construction; `Kind` identifies the EntityOfConcern and `Description` already identifies the episteme.

For a coupled system-role–Method phrase, recover the local kind and Method separately before naming either one. Recover and name a MethodDescription, WorkPlan, or dated Work only when that exact object is already admitted and the naming use consumes it; a shared phrase does not require any of them to exist. `RoboticsEngineerSystemRole` may designate one admitted local kind; `RobotEngineeringMethod` names a Method or Method family. Ordinary *engineer-roboticist* may remain the Plain expression for the local kind when its named practice or source boundary and criterion are recoverable. It replaces neither a qualifying MethodDescription nor any description of planned or performed Work.

When a later naming use actually consumes one dated Work identity, that Work must already be constituted before F.5 naming begins. The admitting claim must already recover the performer System, exact semantic Method, time, containing System, the assignment occurrence that covers the Work and its declared species, equality of performer and assignment holder, and the F.6 performed-under-assignment relation. Otherwise keep the activity in ordinary wording and do not mint a Work identifier merely to support a name.

For a U-kind, the Tech designation should be neutral enough that no witness wins by vocabulary alone. If witnesses disagree between `Observation`, `Reading`, and `MeasurementResult`, a Concept-Set row preserves the comparison; the exact shared value and invariants must still pass E.24.UK admission or their direct defining rule before an author uses F.5 to choose a name.

#### F.5:4.3 - Positive Naming Rules

1. **Recover the object first.** State the governed kind or construction of the value—for example, a U-kind, local system-role kind, description episteme, classification judgment, assignment, relation, Method, Work, status, evidence use, slot, lens, or another object.
2. **Recover the meaning source.** Use the exact E.24.UK or direct admission for a U-kind; A.2 with C.3 for a local system-role kind; F.4 for its description; A.2.7 for relations among kinds; A.3, A.15, G.5, or the exact composition pattern for Method and Work names; and the direct relation for status, evidence, source, requirement, publication, assurance, gate, decision, and relation-position names.
3. **Use minimal generality.** The designation's scope is no wider than the admitted invariants.
4. **Keep interpretation metadata out of the label.** Edition, source, witness, local boundary, reference scheme, and threshold belong in the direct declaration, description, relation, or NameCard.
5. **Make morphology object-sensitive.** Concrete local system-role kinds use `...SystemRole`; description epistemes use `...SystemRoleKindDescription`; states use state or level wording; slots say `Slot`, `Argument`, `Endpoint`, or another exact position head.
6. **Keep coupled names typed.** A compact phrase may help a reader, but one label must not carry several independently governed objects—for example, kind, assignment, capability, Method, Work, and description—at once.
7. **Do not encode thresholds or windows in the name.** Put time, state, threshold, capability envelope, or admission window in the direct claim.
8. **Use aliases only with lineage.** A source term, predecessor term, symbol, or translation does not become a second selected Tech label.
9. **Escalate only for actual reuse.** Use F.18 and F.17 for durable or public naming. When an actual cross-local relation is consumed, name the exact obtaining C.3.3 relation between local kinds or F.9 relation between distinct F.17 cells, as applicable, and keep the separate current C.2.1 claim that it suits the named receiving use. For ordinary below-threshold use with no assurance claim, require the exact A.10 evidence-provenance relation and local `RelianceDisposition=pass`. When an assurance claim is made or B.3's material-reliance threshold is met, first decide whether a current assurance claim exists; positive reliance needs that positive claim for the same bounded assurance use and a sufficient minimum reliance-safety assurance record. An exact non-positive disposition—such as no assurance claim, insufficient record, narrowed, rejected, withdrawn, abstaining, or blocked—stops or narrows the use. None of the cross-local relation, receiving-use claim, evidence path, assurance record, NameCard, row, designation, or publication establishes assignment, Work, result, provenance, assurance, or publication occurrence.

#### F.5:4.4 - Neighboring Use Boundary

When a candidate contains a tempting word, recover the current claim instead of replacing words mechanically.

| Source wording | First ontological question | Direct next locus |
| --- | --- | --- |
| `EvidenceRole`, `ModelFitEvidenceRole`, or “evidence role” | Is an episteme used as evidence for a target claim with exact scope, polarity, relevance window, and provenance? | A.10, B.3, C.2.1, or the exact evidence-use relation |
| `RequirementRole` or “standard role” | Is an episteme, standard, or clause used as a requirement, source, or specification? | E.10.D2, C.28, E.17, or the exact source or requirement relation |
| `Access Role` in RBAC | Is this a policy or permission grouping rather than a work-facing kind? | Exact access, policy, permission, or status relation; F.18 only if durable naming is needed |
| “role of subject, provider, or input” | Is this participant meaning, a declaration slot, or a representation position? | E.10.ROLE, A.6.RSIR, and A.6.5 |
| `ReviewerSystemRole` | Is one exact local C.3 kind with a direct criterion current? | A.2 with C.3; F.4 for its description; A.2.1 only when assigned |
| `robotics engineer` or `engineer-roboticist` | Is this a local kind, conjunction, relation, Method, Work, or capability? | A.2.7, A.3, A.15, A.2.2, and F.18 when durable naming is current |
| `Reviewing`, `ReviewMethod`, `RobotEngineeringMethod`, `ReviewWorkflow`, or `MethodAlgebra` | Is this a Method, MethodDescription, Method relation structure, WorkPlan, performed Work, or lens? | A.3, A.15, G.5, C.29, or the exact composition pattern |
| `ReviewWork` or “review happened” | Is one performed Work occurrence current? | A.15.1 |

Select the name only after recovery. A cleaner string is not a repair if it hides the same ontological error.

### F.5:5 - Archetypal Grounding

#### F.5:5.1 - Public or Cross-Local Kind Name

A Concept-Set row compares SOSA `Observation`, metrology *measurement result*, ML practice *metric reading*, and a dashboard value exported for comparison. The row is a comparison and evidence surface, not admission or identity of a common result value.

Keep the concrete objects at their direct loci. Pump 14 was measured before the reading was recorded, but this naming example does not identify a dated Work occurrence. If a use needs that occurrence, admit it separately under A.15.1 and attribute it under F.6.

C.16 constitutes the measurement result: a value attributed to the measurand together with the Characteristic, Scale, uncertainty, method, model, calibration basis, time stance, and measurement Work needed to interpret it. `Pump14PressureReading_2026-07-14T10-42Z` is one C.2.1 episteme that states that result; F.5 does not repeat either pattern's schema. The result and its episteme are distinct from raw output, indication, Pump 14's actual state, a later diagnosis, a criterion verdict, evidence, or a dashboard display. `Pump14CalibrationTrace_2026-07-14` is a provenance record whose G.6 and A.10 relations make the calibration and source path recoverable. A dashboard publication may cite the reading, and the Concept-Set row may cite the reading and trace; neither is the result, its episteme, provenance, or a generic relation that establishes them.

Only E.24.UK or the direct result pattern can admit a shared value and its invariants. After admission, use F.5 to select `Reading`, `Result`, or another neutral head no wider than that value. The spelling still creates no result or provenance identity.

#### F.5:5.2 - Local System-Role Kind and Its Description

Under `Plant-A-Maintenance-Scheme`, `PumpInspectorSystemRole` designates one exact local kind; it is not that kind. `PumpInspectorSystemRoleKindDescription-v3` is a separate C.2.1 episteme whose EntityOfConcern is the kind and whose ClaimGraph names the Plant-A maintenance practice in which the kind is constituted, its stable pump-inspection contribution distinction, current `KindSignature`, and effective scheme. The Tech designation for the kind is `PumpInspectorSystemRole`; the Plain designation is “pump inspector”.

This worked slice needs an assignment identity, so `Robot7-PumpInspector-Assignment-2026Q3` is one occurrence of the directly declared `PlantAPumpInspectionAssignment` species under `U.SystemRoleAssignment`. The species' holder slot admits a `U.System`; its declaration-local assigned-kind slot uses the exact `PlantAMaintenanceSystemRoleKindDomain`; and its predicate applies within the Plant A maintenance scheme and obtains while the fixed holder is assigned under `PumpInspectorSystemRole` to supply the pump-inspection contribution. The occurrence identifies Robot-7 as holder and `PumpInspectorSystemRole` as assigned kind, and spans the maximal uninterrupted interval over which that predicate obtains for those values. This simple species declares no additional identity-bearing participant; a commission, position, or installation locus would become one only in a species whose predicate and identity actually require it.

This naming example does not identify Robot-7's inspection of Pump 14 as a dated Work occurrence. `Pump14InspectionFinding_2026-07-14T11-18Z` is a separate claim-bearing result episteme, and `Pump14InspectionTrace_2026-07-14` is the exact provenance record connected through G.6 and A.10.

The kind label helps readers recover the kind; the description episteme describes it. Neither says Robot-7 satisfies the kind, has an assignment, performed the inspection, produced the finding, or supplied its provenance. A suffix, NameCard, row, pattern section, or citation identifies none of those objects or relations.

#### F.5:5.3 - Evidence Use Is Not a System-Role Name

Source text may say `ModelFitEvidenceRole`. The repair is not a prettier role label. This naming example does not identify the model-fit evaluation as a dated Work occurrence. Recover the exact objects it does consume: `ModelFitResult_2026-07-15T09-22Z` is a separately constituted domain-local result episteme; `ModelFitTargetClaim-v5` is the target claim; and `ModelFitRunTrace_2026-07-15` is the provenance record connected through exact G.6 and A.10 relations. Keep any operation-result binding, result-episteme inception claim, evidence use, provenance, and current assurance claim separate, and apply the rule that defines or tests each relation.

A durable name, if needed, names one recovered evidence-use relation, status value, Work occurrence, result episteme, or provenance value. `ModelFitEvidenceRole`, a NameCard, row, or citation creates none of them and supplies no generic evidence-result relation. It is neither a local system-role kind nor a `SystemRoleKindDescription` label.

#### F.5:5.4 - Relation Position Is Not a System-Role Name

In a relation signature, “provider role” may mean the provider argument position. Use E.10.ROLE and A.6.RSIR to recover the participant meaning; use A.6.5 to declare `ProviderSlot`, its `ValueKind`, and its reference mode. A provider system's classification under a local `ProviderSystemRole` kind is a separate C.3 claim. When assignment identity is irrelevant to naming that relation position, say only that any provider assignment remains independently governed by A.2.1; do not invent an occurrence. When it is relevant, recover the assignment occurrence and its declared species rather than asserting that the provider simply “has an assignment”.

### F.5:6 - Bias Annotation

1. **Semio-bias.** A name, card, row, publication, or source label is mistaken for the named value or authority to use it.
2. **Role-bias.** Evidence, status, access, source, requirement, participation, or argument-position wording is forced into `SystemRole` morphology.
3. **Source-vocabulary capture.** One source's term becomes the Tech designation without showing fit to the admitted value or exact local kind.
4. **Suffix formalism.** Adding `SystemRole`, `KindDescription`, `Status`, `Record`, `Graph`, or `Map` makes a label look precise while the object remains unresolved.

The repair is object recovery first, designation second.

### F.5:7 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-F5-1` | The exact named value and kind are explicit. |
| `CC-F5-2` | The direct meaning source is explicit: E.24.UK or direct admission for a U-kind, A.2 with C.3 for a local system-role kind, F.4 for its description, or another exact relation. A Concept-Set row, card, or citation is not admission or identity. |
| `CC-F5-3` | The Tech designation is no broader than the recovered meaning. |
| `CC-F5-4` | The Plain designation points to the same value without widening it. |
| `CC-F5-5` | Edition, source, witness provenance, local boundary, scheme, threshold, and window stay outside the main label unless one truly distinguishes the local value. |
| `CC-F5-6` | A U-kind name is neutral across the named witness sources or practices. Shared source spelling establishes neither the governed value nor a local kind's identity; the direct admission and identity rules must already have done that work. Treat the term as genuinely shared only when evidence establishes the same referent. |
| `CC-F5-7` | The system-role-kind designation, local kind, F.4 description, classification judgment, assignment species, and assignment occurrence remain distinct. For any assignment identity used, recover the occurrence and its declared A.2.1 species. The species defines the participant meanings, assigned-kind domain, predicate, applicability, and occurrence identity; the occurrence supplies the holder, assigned-kind value, case applicability, extent, and any other participant values. Otherwise the text does not invent an occurrence. |
| `CC-F5-8` | Status, evidence, requirement, source, publication, assurance, gate, decision, responsibility, and relation-position names remain at their direct objects before durable naming. |
| `CC-F5-9` | A source term, symbol, predecessor term, or translation is marked as lineage or alias, not another selected Tech designation. |
| `CC-F5-10` | For durable or public reuse, use F.18 and F.17 as needed; actual cross-local use names the exact C.3.3 kind relation or F.9 local-sense relation and the proportionate receiving-use, A.10, or B.3 claims required by rule 9. None substitutes for the receiving Work, result, provenance, assurance, or publication occurrence. |
| `CC-F5-11` | A worked case does not mint a dated Work identity merely to support naming. When it consumes an already admitted Work, the performer, Method, time, containing System, covering assignment held by that performer, and F.6 relation are recoverable. Result epistemes, provenance values, and their relations remain separate; no label, description, suffix, card, row, or citation substitutes for them. |

### F.5:8 - Common Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Interpretation tag in label | `Participant-BPMN`, `Task-IEC61131`, `ReviewerSystemRole-SchemeA` | Put source, edition, local boundary, and scheme in the direct declaration, description, or NameCard. |
| Witness capture | `Observation` chosen because one standard uses it | Recover the exact value and admission; use comparison evidence only as evidence, then choose a neutral head when witnesses diverge. |
| System role and status fusion | `ApprovedReviewerSystemRole` or `AccessRole` treated as a work-facing kind | Separate the local kind from status, policy, permission, and access relations. |
| Evidence role revival | `EvidenceRole` retained as durable ontology | Recover and, if needed, name the evidence-use relation. |
| Verbified system role | `Reviewing` used as a kind label | Use a concrete kind noun; use Method or Work patterns for action or occurrence. |
| Position role | `ProviderRole` names a relation argument | Use an exact slot or position name under A.6.RSIR and A.6.5. |
| Threshold in name | `CriticalReviewer0.2mmSystemRole` | Put threshold, capability envelope, or window in the direct claim. |
| Alias spray | Several Tech labels for one meaning | Keep one selected Tech designation; retain other strings as lineage or aliases under F.18 or F.13. |
| Decorative precision | `CanonicalActionStatus`, `ValidatedSystemRoleCue` | Recover the governed object and relation; do not replace one umbrella with another. |

### F.5:9 - Consequences

Good consequences:

- durable names become shorter because the ontology stays at the right object;
- local system-role-kind names stay usable without becoming assignment, capability, Method, or evidence claims;
- description names no longer collapse into the kinds they describe;
- U-kind names are easier to bridge because their comparison evidence remains explicit; and
- For an E.10 repair that uncovers a durable naming issue, use F.5 or F.18 instead of ad hoc word substitution.

Costs:

- authors recover the object and meaning source before naming;
- some familiar source labels cannot become FPF Tech designations;
- durable public names may need F.18 and F.17, while actual cross-local relations may need C.3.3 or F.9 even when a local label looks obvious; and
- source text that uses *role* for status, evidence, access, participation, or relation position needs ontological recovery, not suffix editing.

Reopen F.5 when U-kind neutrality, `SystemRole` or `SystemRoleKindDescription` morphology, the Tech-Plain relation, lineage, or durable cross-local naming boundaries change. Reopen a neighboring pattern when the dispute is about the named object itself.

### F.5:10 - Rationale

Naming is late ontology, not early decoration. Durable names become references used in reasoning, search, publications, and pattern relations. A wrong name makes later readers inherit a false kind claim.

The design choice is to split naming by meaning source rather than source spelling. Bare *role* can point to many different objects or uses—for example, a local system-role kind, assignment, policy term, status, evidence use, relation position, representation position, or ordinary English. Do not decide by suffix. Use E.10.ROLE and the direct patterns to recover the object, then F.5 to name it.

F.5 remains narrower than F.18. Use F.18 for the full local-first protocol, NameCards, candidate comparison, lineage, and public naming. F.5 supplies the special discipline needed by U-kind names, concrete system-role-kind names, and `SystemRoleKindDescription` labels.

### F.5:11 - SoTA-Echoing and Source Use

| Practice line | What FPF adopts | Practical implication |
| --- | --- | --- |
| Terminology and controlled-vocabulary practice | Referent, preferred designation, Plain explanation, symbol, alias, and lineage are separate. | Tech designation, Plain designation, symbol, and source spelling are not interchangeable. |
| Ontology engineering practice | Class and relation names should not encode accidental provenance, thresholds, or temporary use. | Source, edition, witness, local boundary, scheme, window, and threshold stay in direct claims. |
| Human-centered technical writing | A teaching phrase helps only when it preserves the underlying concept. | Plain wording explains; it does not widen the Tech designation. |
| Morphology-aware naming | Word form affects expectations about actor, action, state, result, description, and relation position. | `...SystemRole`, `...SystemRoleKindDescription`, Method, Work, status, and slot morphology remain distinct. |
| Cross-local terminology use | Shared spelling is evidence at most; an actual relation and reliance need explicit claims. | A label, Bridge, use claim, evidence path, assurance record, card, or row creates no kind, assignment, Work, result, or publication. |

SysML is intentionally not used as naming or ontology authority here. A familiar modeling notation does not settle the referent, kind, description, assignment, participation, permission, Method, or Work.

Source-use boundary: external labels, Concept-Set rows, and citations are evidence for local meaning or common practice, not automatic Tech designations, admission decisions, or Work, result, and provenance identities. A source term becomes selected only after the exact value is admitted and the naming comparison passes; naming changes none of those objects.

### F.5:12 - Relations

**Builds on.** A.2, C.3, F.4, F.7, F.18, E.10, E.10.ROLE, and E.10.ARCH.

**Coordinates with.** E.24.UK for U-kind admission; A.2.1 for system-role assignment; A.2.2 for capability; A.2.5 for assignment state; A.2.7 for relations among system-role kinds; A.6.5 and A.6.RSIR for relation positions; A.15 for system-role–Method–Work alignment and dated Work; C.16 for measurement results; C.2.1 for descriptions and result epistemes; G.6 and A.10 for provenance and ordinary evidence reliance; B.3 for assurance-bearing reliance; F.8 for mint or reuse; C.3.3 for relations between exact local kinds and F.9 for relations between distinct F.17 cells; F.10 for status; F.13 for lineage; F.14 for anti-explosion; F.15 for conformance; and F.17 for public term-sheet use.

**Used by.** Part F naming patterns, F.4 description authors, Concept-Set authors, E.10 repairs that uncover naming rather than phrase-use issues, and any pattern use that creates a durable local name for a U-kind, system-role kind, or `SystemRoleKindDescription`.

**Does not replace.** Direct evidence, status, requirement, source, publication, assurance, gate, decision, responsibility, relation-signature, Method, Work, or architecture patterns.

### F.5:End

