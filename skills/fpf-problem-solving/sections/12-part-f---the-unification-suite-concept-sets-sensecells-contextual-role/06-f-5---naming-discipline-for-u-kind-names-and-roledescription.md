## F.5 - Naming Discipline for U-kind Names and RoleDescription Labels

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### F.5:0 - Use This When

**Plain name.** Meaning-first naming discipline.

Use this pattern when a project needs a durable name for either:

- a U-kind or other cross-context concept already admitted through `E.24.UK` or its direct governing pattern; a Concept-Set row may cite comparison evidence but does not admit the value; or
- a label used by a role-description episteme for one work-facing `U.Role` interpreted under one named role-taxonomy episteme and effective `U.ReferenceScheme`.

Typical moments:

- a Concept-Set comparison has enough witnesses for a naming question and an `E.24.UK` or direct-pattern decision has already admitted the reusable value, but the candidate names import one source tradition too strongly;
- a role-description episteme names a role such as `ReviewerRole`, `OperatorRole`, `InspectorRole`, or `TransformerRole`, and the label must stay faithful to the exact role-taxonomy episteme and effective reference scheme without smuggling capability, permission, method, work, evidence, or status;
- a role-like external phrase must be named for local use, but the project has not yet decided whether it is a work-facing `U.Role`, a status-use relation, an access or policy term, a relation slot, or only a local phrase;
- two similar names threaten to make a U-kind, a `U.Role`, a status value, a method, and a work occurrence look like one object.

**Primary EntityOfConcern.** The EntityOfConcern is the naming discipline for these two name families. It governs the relation between a recovered meaning and its Tech and Plain labels. It does not define the named U-kind, does not define the described `U.Role`, does not assign a holder to a role, does not assert status, does not provide evidence, and does not make a publication form authoritative.

**Primary working reader.** The first reader is an engineer-manager, analyst, pattern author, or terminology steward who already has a candidate meaning and must choose a name that remains usable by readers without creating a second ontology.

**First useful move.** Before choosing the label, recover the exact named value and its direct source of meaning: `E.24.UK` or the direct governing pattern for a U-kind, with any Concept-Set row retained only as comparison evidence; or the role-description episteme, described `U.Role`, exact role-taxonomy episteme, effective reference scheme, and local sense for a role label. Then choose Tech and Plain labels whose morphology matches that kind and whose scope does not exceed the recovered meaning. Keep the selected label as a designator distinct from both the role value and its role-description episteme.

**Smallest useful result and stop.** Stop with one already-governed value, one Tech label, and a short Plain gloss as soon as the label resolves unambiguously for the named local use. Do not create a NameCard, public row, Bridge, or new kind merely to complete a naming form. Return to the direct subject owner when the value or kind is unresolved; open `F.18` or `F.17` only for a durable or public naming need, and open the F.9 bounded-use path only when an actual cross-scheme correspondence is consumed. If the proposed label starts carrying assignment, work, result, provenance, assurance, or publication claims, stop naming and recover those objects under their direct governors.

**What goes wrong if missed.** Names become arguments. A role label starts implying permission or capability. A status phrase becomes a role. A U-kind name imports one context's private ontology. A pretty global word hides that the Concept-Set witnesses do not agree. Downstream patterns then repair "semantics" that were actually broken at naming time.

**What this buys.** Readers can use short names without guessing the ontology. U-kind names stay neutral across their witnesses. RoleDescription labels remain interpretable through their named role-taxonomy episteme and effective reference scheme and point to work-facing roles. Status, evidence, access, requirement, source, publication, assurance, and gate names remain governed by their direct patterns instead of becoming "roles" by naming accident.

**Not this pattern when.**

- If the current problem is ordinary phrase repair rather than a durable name, use `E.10`, `E.10.ARCH`, `A.6.P`, or the direct governing pattern.
- If the current issue is whether a `U.*` spelling or structural name should survive as a durable U-kind, use `E.24.UK` before F.5.
- If the current issue is the broader local-first naming protocol, Name Cards, candidate fronts, lineage, or public naming governance, use `F.18`.
- If the current issue is a role-description episteme itself, use `F.4`.
- If the current issue is role assignment, holder, role-taxonomy episteme, effective reference scheme, assignment extent, or performed-work attribution, use `A.2.1`.
- If the current issue is status classification, use `F.10` or the direct status-use pattern.
- If the current issue is evidence, source, standard, requirement, publication, assurance, gate, or decision use of an episteme, use the direct pattern for that relation.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.
- If cross-taxonomy or cross-scheme correspondence is current, use `F.9`.

### F.5:1 - Problem Frame

FPF needs names that humans can use without dragging the wrong ontology behind them. A good name is short enough to be used in documents and conversations, but it is not free-floating. It belongs to a recovered meaning.

This pattern keeps two recurrent naming families separate.

First, a U-kind or similar cross-context concept gets its name only after `E.24.UK` or its direct governing pattern admits the exact value. A Concept-Set row may preserve witness comparison and evidence for that decision; it neither admits nor identifies the value. The name should be neutral with respect to the witnesses and should name the least shared kind that the direct admission source actually admits.

Second, a role-description episteme labels one work-facing `U.Role` interpreted through one exact role-taxonomy episteme and effective `U.ReferenceScheme`. The label should fit the admitted role meaning and make the role recognizable. It should not make a holder assignment, capability, method, work occurrence, status, evidence relation, permission, publication, or relation slot look like part of the role value.

The tempting shortcut is to make "Role Description" cover both roles and statuses because both need labels. That is convenient wording, but it creates duplicate ontology. Statuses and evidence uses need names too; they do not become roles because they are named.

### F.5:2 - Problem

Without this pattern:

1. **Context-local terms look global.** A name such as `Observation`, `Activity`, or `Process` is promoted to a U-kind name even though it carries one witness tradition's private commitments.
2. **Role names become hidden assignments.** A label such as `ReviewerRole` is treated as if someone already holds the role.
3. **Role names become capability claims.** A holder is assumed able because the role label sounds competent.
4. **Role names become methods.** A noun label hides a method or method family.
5. **Status names become roles.** `Approved`, `AccessRole`, `ModelFitEvidenceRole`, or `RequirementRole` becomes a role-name family instead of a status-use, evidence-use, access-policy, requirement-use, or source-use relation.
6. **Relation positions become roles.** Signature, relation, or argument-position names borrow role morphology and collide with `U.Role`; interface wording is used only when a governing boundary or interface pattern makes that meaning current.
7. **Names carry interpretation metadata.** Labels such as `Task-IEC61131` or `Participant-BPMN` fossilize an edition, source vocabulary, taxonomy, or scheme inside the label instead of keeping those facts in the governing admission, Concept-Set, role description, reference scheme, or Name Card.
8. **Aliases become silent renames.** Several labels circulate for one meaning without lineage or bridge discipline.

### F.5:3 - Forces

| Force | Tension |
| --- | --- |
| Local idiom vs cross-context neutrality | RoleDescription labels must remain faithful to their role taxonomy and effective scheme; U-kind names must not privilege one witness context. |
| Brevity vs kind recovery | Names must be usable, but the reader must still recover whether the named value is a kind, role, status, method, work, relation, or episteme-use relation. |
| Teaching vs widening | Plain labels should help readers, not broaden the Tech label's meaning. |
| Stability vs changed meaning | Names should remain stable across edition or publication changes, but real sense change must split or rename with lineage. |
| Morphology vs ontology | Word form should hint at kind, but suffixes are not ontology. A word ending in `Role` does not create `U.Role`. |
| Open-world use vs name burden | A lightweight local label may be enough; stronger public or cross-context use needs `F.18`, `F.9`, or `F.17`. |

### F.5:4 - Solution

Name after meaning. For each candidate name, first recover the named value, its meaning source, and its intended use. Then choose labels that preserve that meaning.

For each naming decision, make the following facts recoverable in the prose, governing admission, role-description episteme, Concept-Set row, or Name Card. This is a naming checklist, not a new relation signature or mandatory record:

- the exact named value and its admitted kind;
- the direct source of its meaning;
- for a role label, the described `U.Role`, exact role-taxonomy episteme, and effective `U.ReferenceScheme`;
- the selected Tech label and its Plain teaching gloss;
- any aliases or previous labels with lineage;
- the morphology, neutrality, and minimal-generality checks;
- the neighboring-use boundary that prevents the name from absorbing assignment, capability, method, work, status, evidence, permission, publication, or relation-slot claims.

#### F.5:4.1 - Name Families Governed Here

| Name family | Meaning source | Naming rule |
| --- | --- | --- |
| U-kind or cross-context concept name | Exact value admitted by `E.24.UK` or its direct governing pattern; a Concept-Set row may retain witness comparison and evidence but supplies neither value identity nor admission | Use a neutral Tech label at minimal generality. Do not use one witness context's private term when a neutral head exists. |
| RoleDescription label for one `U.Role` | Role-description episteme, described `U.Role`, exact role-taxonomy episteme, effective reference scheme, and local sense | Use role-faithful morphology. Do not smuggle assignment, capability, method, work, evidence, status, permission, or publication into the label. |
| Role-relation, role-expression, or role-method expression name | `A.2.7` role relation structure whose participating roles are interpreted through their exact role taxonomies and effective schemes, plus `A.3.1`, `A.3.2`, or `A.15` when method or work is current | Ordinary labels may name qualified role expressions or role-bundle expressions without a `Role` suffix. Hyphenation can mark a recovered factor, domain, practice, method-family qualification, or combined expression; it must not mechanically concatenate operands or hide independent assignments. |
| Method, method-family, method relation structure, work-plan, or work name | Direct method and work patterns: `A.3.1`, `A.3.2`, `A.15`, `G.5`, and any direct method-composition pattern when current | Do not make the name a role-relation result because it shares words with role labels. Name the method value, method family, method relation structure, work plan, or work value directly and cite the role relation separately when it constrains use. |
| Mathematical or representation lens name | Lens or representation description over a selected role relation structure, method relation structure, transformation-flow structure, or other governed structure | Name the lens only when it is the governed value. Otherwise name the recovered role relation, method relation structure, method, work, or assignment. |
| Status, evidence, requirement, source, standard, publication, assurance, gate, or decision name | Direct governing status-use, evidence-use, source-use, publication-use, requirement-use, assurance, gate, or decision pattern | Do not treat it as a RoleDescription branch. Use `F.18` for durable naming only after the direct relation is recovered. |
| Relation slot or argument-position name | `A.6.5` SlotSpec discipline and the governing relation or signature pattern; use an interface-governing pattern only when interface meaning is current | Name the slot as a slot or argument position, not as a `U.Role`, unless a direct role-assignment relation is truly current. |

For every role-facing name, keep three objects distinct: the selected label or designator `L`, the described `U.Role` value `R`, and the F.4 role-description episteme `RD`. Under the effective `U.ReferenceScheme`, `L` designates `R`; under C.2.1, `RD` has `R` as its exact EntityOfConcern and names the governing role-taxonomy episteme in its ClaimGraph. Spelling, a `Role` suffix, a NameCard, a public row, or a source citation creates none of `L`'s governed referent, `R`, `RD`, a role assignment, dated work, a result or claim-bearing episteme, provenance, or publication occurrence.

#### F.5:4.2 - Tech and Plain Labels

Use two human-facing labels when the name is durable enough to be reused:

| Label | Job | Constraint |
| --- | --- | --- |
| Tech label | The stable label used by the local pattern, table, or role-description episteme. | Must fit the recovered kind and meaning source. |
| Plain label | A short teaching gloss. | Must explain without widening the sense. |
| Symbolic alias | Optional symbol or source abbreviation. | Informative only; it is not the Tech label. |

For a role-description label, the Tech label may be an agentive noun, local role term, or role phrase such as `ReviewerRole`, `PumpInspectorRole`, `Participant`, or `Approver`. The suffix `Role` is a disambiguator, not a universal law. Use it when it prevents confusion with a status, method, work occurrence, organization unit, publication, or access-policy term. Do not add it merely to make the name look formal.

For a coupled role-method label, recover the role expression and the method value or work value separately before naming. `RoboticsEngineerRole` may be a durable Tech label for a robotics-qualified engineering role value. `RobotEngineeringMethod` names a method or method family. The ordinary label "engineer-roboticist" can be useful when the role taxonomy, effective scheme, and method relation make the coupled meaning recoverable, but it must not replace the method description or work description.

For a U-kind, the Tech label should be neutral enough that no witness context wins by vocabulary alone. If witnesses disagree between `Observation`, `Reading`, and `MeasurementResult`, a Concept-Set row can preserve that comparison, but the selected head is admissible only when `E.24.UK` or the direct governing pattern has already admitted the exact shared value and invariants. The row, a source title, or the selected spelling does not perform admission.

#### F.5:4.3 - Positive Naming Rules

Use these rules when choosing or checking a name.

1. **Recover kind first.** State whether the named value is a U-kind, `U.Role`, role-description episteme, role-relation expression, method, work, status-use value, evidence-use relation, relation slot, lens description, or another named kind.
2. **Recover meaning source.** Use the exact `E.24.UK` or direct-pattern admission for a U-kind, retaining any Concept-Set row only as witness-comparison evidence; use the role-description episteme, described `U.Role`, exact role-taxonomy episteme, and effective reference scheme for role labels; use `A.2.7` for role-relation expressions; use `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern for method, method-family, method relation structure, or work names; use the direct governing pattern for statuses, evidence, source, requirement, publication, assurance, gate, decision, and relation slots.
3. **Use minimal generality.** The name's scope stays no wider than the admitted invariants.
4. **Keep interpretation metadata out of the label string.** Edition, source, witness, role taxonomy, and effective reference scheme belong in their governing admission, Concept-Set row, role-description episteme, reference-scheme relation, or Name Card, not inside the main label.
5. **Make morphology kind-sensitive.** Agentive role names fit work-facing roles. State or level forms fit statuses. Verbal or gerund forms fit methods only when the method pattern admits them. Slot names should say `Slot`, `Argument`, `Endpoint`, or another declared slot or position head when current.
6. **Keep coupled role-method names typed.** A phrase like "engineer-roboticist" may be the ordinary label for a qualified role expression; "robot engineering" may be a method or work name. Do not make one label carry holder assignment, role value, method, work, and capability at once.
7. **Do not encode thresholds or windows in the name.** Put time, state, threshold, capability envelope, or admission window in the governing pattern.
8. **Use aliases only with lineage.** A source term, previous term, symbol, or translation can be an alias; it does not create a second Tech label.
9. **Escalate when reuse becomes public or cross-scheme.** Use `F.18` and `F.17` for durable or public naming. When an actual cross-taxonomy or cross-scheme correspondence is consumed, first name the exact obtaining F.9 Bridge occurrence, then keep the separate current C.2.1 claim that it is suitable for the named bounded use. Reliance follows F.9's two branches. Ordinary below-threshold use with no assurance claim requires the exact A.10 evidence-provenance graph relation and `RelianceDisposition=pass` for that same use. When an assurance claim is made or B.3's material-reliance threshold is met, enter B.3 and first decide whether a current assurance claim exists; positive reliance requires a positive current assurance claim carrying the same bounded assurance use with its sufficient minimum reliance safety assurance record, while an exact `no-assurance-claim`, `insufficient-record`, `narrowed`, `rejected`, `withdrawn`, `abstaining`, or `blocked` disposition stops or narrows the use. A Bridge, profile, NameCard, row, label, evidence path, assurance record, or publication neither authorizes the use nor establishes assignment, work, result, provenance, assurance, or publication occurrence.

#### F.5:4.4 - Neighboring Use Boundary

When a label contains a tempting word, recover the current claim instead of replacing words mechanically.

| Source wording | First ontological question | Likely governing pattern |
| --- | --- | --- |
| `EvidenceRole`, `ModelFitEvidenceRole`, or "evidence role" | Is an episteme being used as evidence for a target claim with scope, polarity, relevance window, and provenance? | `A.10`, `B.3`, `C.2.1`, or the direct evidence-use pattern |
| `RequirementRole` or "standard role" | Is an episteme, standard, or clause used as a requirement, source, or specification-use item? | `C.28`, `E.10.D2`, `E.17`, or the direct requirement-use or source-use pattern |
| `Access Role` in RBAC | Is this a policy or permission-set term, not a work-facing behavioral role? | Direct access, policy, or status-use pattern; `F.18` for naming when durable |
| "role of subject, provider, or input" | Is this a relation position? | `A.6.5` |
| `ReviewerRole` | Is this a work-facing role value under one exact role-taxonomy episteme and effective reference scheme? | `A.2`, `F.4`, `A.2.1` when assigned |
| `robotics engineer` or `engineer-roboticist` | Is this a qualified role expression, independent role conjunction, method name, work name, or capability name? | `A.2.7`; `A.3.1`, `A.3.2`, or `A.15` when method or work is current; `F.18` for durable naming |
| `Reviewing`, `ReviewMethod`, `RobotEngineeringMethod`, `ReviewWorkflow`, or `MethodAlgebra` | Is this a method, method description, method relation structure, work plan, performed work, or lens over one of those objects? | `A.3.1`, `A.3.2`, `A.15`, `G.5`, `C.29`, or a direct method-composition pattern when current |
| `ReviewWork` or "review happened" | Is this performed work? | `A.15.1` |

Select the name only after this recovery. A cleaner string is not a repair if it hides the same kind error.

### F.5:5 - Archetypal Grounding

#### F.5:5.1 - Cross-Context Type Name

A Concept-Set row compares SOSA `Observation`, metrology `measurement result`, ML practice `metric reading`, and a dashboard value exported for later comparison. The row is a comparison and evidence surface, not the admission or identity of a common result value.

Keep its concrete exemplars under their direct owners. `Work_MeasurePump14_2026-07-14T10-42Z` is one exact dated measurement `U.Work` occurrence under A.15.1. `Pump14PressureReading_2026-07-14T10-42Z` is the separately constituted domain-local measurement-result episteme under C.16 and C.2.1. `Pump14CalibrationTrace_2026-07-14` is the exact provenance record whose G.6 and A.10 relations make the calibration and source path recoverable. A dashboard publication may cite the reading, and the Concept-Set row may cite all three objects; neither publication nor row is the Work occurrence, result episteme, provenance record, or a generic relation that establishes them.

The row therefore justifies neither `Observation` nor `DashboardValue` as a U-kind name. Only an exact `E.24.UK` or direct-pattern admission can establish a shared value and its invariants. After that admission, F.5 may select `Reading`, `Result`, or another neutral head no wider than that exact governed value; the selected spelling still creates no result or provenance identity.

#### F.5:5.2 - Work-Facing Role Label

Under `Plant-A-Maintenance-Scheme`, label `PumpInspectorRole` designates the exact role value `PumpInspectorRole`; it is not that value. `PumpInspectorRoleDescription-v3` is a separate C.2.1 episteme whose exact EntityOfConcern is that role value and whose ClaimGraph names `PlantMaintenanceRoles-2026` as the governing role-taxonomy episteme. The Tech label is `PumpInspectorRole`; the Plain label is `pump inspector role`.

`Robot7-PumpInspector-Assignment-2026Q3` is the separate A.2.1 role-assignment occurrence. `Work_InspectPump14_2026-07-14T11-05Z` is the exact dated inspection `U.Work` under A.15.1. `Pump14InspectionFinding_2026-07-14T11-18Z` is the separately constituted domain-local claim-bearing result episteme under its inspection-result governor and C.2.1. `Pump14InspectionTrace_2026-07-14` is the exact provenance record connected through its G.6 and A.10 relations. Any current method enactment, production or inception claim, and evidence use remains under its direct owner.

The role label helps readers recover the role; the role-description episteme describes it. Neither says Robot-7 holds the role, performs the inspection, produces the finding, or supplies its provenance. A `Role` suffix, NameCard, row, pattern section, or source citation identifies none of the assignment, dated Work, result episteme, provenance record, or their direct relations.

#### F.5:5.3 - Evidence Use Is Not a Role Name

Source text may say `ModelFitEvidenceRole`. The repair is not to invent a prettier role name. Recover the exact objects: `Work_EvaluateModelFit_2026-07-15T09-00Z` is the dated evaluation `U.Work`; `ModelFitResult_2026-07-15T09-22Z` is a separately constituted domain-local result episteme; `ModelFitTargetClaim-v5` is the exact claim for which that result may be used; and `ModelFitRunTrace_2026-07-15` is the provenance record connected through exact G.6 and A.10 relations. The actual operation-result binding, any result-episteme inception claim, evidence use, provenance, and assurance remain distinct under their direct governors.

A durable name, if needed, names an already recovered evidence-use relation, local status-use value, work occurrence, result episteme, or provenance value under that object's direct pattern. `ModelFitEvidenceRole`, a NameCard, a row, or a source citation creates none of those objects and supplies no generic evidence/result relation. It is not a work-facing `U.Role` and not a role-description label.

#### F.5:5.4 - Relation Position Is Not a Role Name

In a relation signature, "provider role" may mean "the provider argument position". F.5 does not make `ProviderRole` a `U.Role` name. Use `A.6.5` to recover `ProviderSlot`, its admitted `ValueKind`, and its reference mode. If a provider system also has a work-facing role in a method, that is a separate `U.Role` claim and, when assigned, a separate `U.RoleAssignment` claim.

### F.5:6 - Bias-Annotation

This pattern protects against four naming biases.

1. **Semio-bias.** A name, card, table row, publication, or source label is mistaken for the named value or for authority to use it.
2. **Role-bias.** Useful relation words such as evidence, status, access, source, requirement, or argument position are put into `Role` language because role words sound familiar.
3. **Source-vocabulary capture.** One source context's term becomes the FPF Tech label without proving cross-context fit.
4. **Suffix formalism.** Adding `Role`, `Status`, `Record`, `Graph`, or `Map` makes a label look precise while leaving the kind unresolved.

The repair is always kind recovery first, label second.

### F.5:7 - Conformance Checklist

Use this checklist on each durable name governed by F.5.

| Check | Pass condition |
| --- | --- |
| `CC-F5-1` | The named value kind is explicit. |
| `CC-F5-2` | The direct meaning source is explicit: exact `E.24.UK` or direct-pattern admission for a U-kind, role-description episteme plus exact role taxonomy and effective scheme for a role label, or another direct governing pattern; a Concept-Set row, card, or citation is not treated as admission or value identity. |
| `CC-F5-3` | The Tech label scope is no wider than the recovered meaning. |
| `CC-F5-4` | The Plain label teaches without widening the sense. |
| `CC-F5-5` | Edition, source, witness provenance, role taxonomy, and effective reference scheme are not baked into the main label. |
| `CC-F5-6` | A U-kind name is neutral with respect to witness contexts unless the Concept-Set row shows that the source term is genuinely shared. |
| `CC-F5-7` | A role-facing label, the described `U.Role`, and the F.4 role-description episteme are distinct; the label encodes no assignment, capability, method, dated work, result or claim-bearing episteme, status, evidence, provenance, permission, or publication. |
| `CC-F5-8` | Status, evidence, requirement, source, publication, assurance, gate, decision, and relation-slot names remain governed by direct patterns before durable naming. |
| `CC-F5-9` | Alias, symbol, previous term, or translation use is marked as alias or lineage, not a second Tech label. |
| `CC-F5-10` | Durable or public reuse invokes `F.18` and `F.17` as needed; actual cross-scheme use names the exact F.9 Bridge and separate bounded-use suitability claim. Ordinary below-threshold use with no assurance claim relies only through the exact A.10 evidence-provenance graph relation with `RelianceDisposition=pass` for that use. Assurance-bearing or threshold use enters B.3's first-claim decision and requires either a positive current assurance claim carrying the same bounded assurance use with its sufficient minimum reliance safety assurance record or an explicit non-positive disposition that stops or narrows the use. None of these objects is the receiving work, result, provenance, assurance, or publication occurrence. |
| `CC-F5-11` | Every worked naming case that relies on performed-work, result or claim, or provenance facts names the exact dated `U.Work`, domain-local result or claim-bearing episteme, and provenance value separately under their direct governors; no role description, label, suffix, card, row, or source citation substitutes for them or for a generic evidence/result relation. |

### F.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Interpretation tag in label | `Participant-BPMN`, `Task-IEC61131`, `ReviewerRole-SchemeA` | Put source, edition, role taxonomy, and effective reference scheme in their governing episteme or Name Card; keep the label clean. |
| Witness capture | `Observation` chosen because one standard uses it | Recover the exact value and its `E.24.UK` or direct-pattern admission; use the Concept-Set row only as witness-comparison evidence, then choose a neutral head if the admitted witnesses diverge. |
| Role and status fusion | `ApprovedReviewerRole`, `AccessRole` treated as work-facing role | Separate `U.Role` from status-use, policy relation, or access relation before naming. |
| Evidence role revival | `EvidenceRole` kept as durable role ontology | Recover evidence-use relation slots and name that relation only if needed. |
| Verbified role | `Reviewing` used as a role label | Use role noun for `U.Role`; use method or work patterns if the current claim is action or occurrence. |
| Slot role | `ProviderRole` names a relation argument | Use `ProviderSlot` or another slot head under `A.6.5`. |
| Threshold in name | `CriticalReviewer0.2mmRole` | Put threshold, capability envelope, or window in the governing pattern. |
| Alias spray | Several Tech labels for one meaning | Keep one Tech label; place other strings in alias or lineage records under `F.18` or `F.13`. |
| Decorative precision | `CanonicalActionStatus`, `ValidatedRoleCue` | Recover the governed kind and relation; do not replace one umbrella with another. |

### F.5:9 - Consequences

Good consequences:

- durable names become shorter because the ontology is carried by the right pattern, not by compound labels;
- role-description labels stay usable without becoming assignment, capability, method, or evidence claims;
- U-kind names become easier to bridge because their Concept-Set row is explicit;

- E.10 repair cases that uncover durable naming issues use the direct `F.5` or `F.18` naming discipline instead of inventing ad hoc word replacements.

Costs:

- authors must recover kind and meaning source before naming;
- some familiar source labels cannot be promoted as FPF Tech labels;
- public or cross-context names may require `F.18`, `F.17`, and `F.9` even when the local name looks obvious;
- source text that used `Role` for status, evidence, access, or relation position must be repaired by ontology, not by suffix editing.

Reopen F.5 when role-description label morphology, U-kind neutrality rules, Tech and Plain label relation, alias lineage, or cross-context naming boundaries change. Reopen neighboring patterns when the dispute is about the named object itself.

### F.5:10 - Rationale

Naming is late ontology, not early decoration. FPF can tolerate many local phrases, but durable names become references used in reasoning, search, publications, and pattern relations. If a name is wrong, subsequent users inherit a false kind claim.

The key design choice is to split naming by meaning source rather than by source spelling. `Role` in a source phrase may refer to a work-facing role, a policy term, a status label, an evidence-use relation, a relation position, or ordinary English. F.5 does not decide by suffix. It recovers the current value and then applies naming discipline.

This also keeps F.5 smaller than F.18. F.18 governs the fuller local-first naming protocol, Name Cards, candidate fronts, lineage, and public naming. F.5 supplies the special discipline needed by U-kind names and RoleDescription labels so that Part F does not preserve role and status fusion.

### F.5:11 - SoTA-Echoing - Source-Use

| Practice line | What FPF adopts | Practical implication |
| --- | --- | --- |
| Role-taxonomy and model-boundary practice | A role label is interpreted under an explicit role vocabulary and effective scheme. An actual correspondence across taxonomies or schemes starts with an exact F.9 Bridge and a separate bounded-use suitability claim; ordinary below-threshold non-assurance reliance uses the exact A.10 evidence-provenance graph relation with local `RelianceDisposition=pass`, while assurance-bearing or threshold use takes B.3's first-claim branch to either a positive current assurance claim with its sufficient minimum reliance safety assurance record or an explicit non-positive stop-or-narrow disposition. | Shared spelling creates neither the Bridge nor the receiving use; a Bridge, bounded-use claim, evidence path, assurance record, card, row, or label establishes no assignment, work, result, provenance, assurance, or publication occurrence. |
| Terminology and controlled-vocabulary practice | Preferred labels, plain explanations, symbols, and aliases are different fields. | Tech label, Plain label, symbol, and alias are not interchangeable. |
| Ontology engineering practice | Class names and relation names should not encode accidental provenance, thresholds, or temporary use. | Source, edition, witness, role taxonomy, reference scheme, window, and threshold stay in their governing assertions rather than the label. |
| Human-centered technical writing | A teaching gloss helps only when it does not change the underlying concept. | Plain labels explain; they do not widen the Tech label. |
| Morphology-aware naming practice | Word form affects reader expectations about actor, action, state, result, and relation position. | Role, method, work, status, and slot names use different morphology when the kind differs. |

Source-use boundary: external labels, Concept-Set rows, and source citations are evidence for local meaning or common practice, not automatic FPF Tech labels, admission decisions, or work/result/provenance identities. A source term becomes the selected label only after `E.24.UK` or the direct governing pattern admits the exact value, or after F.4 constitutes the exact role-description episteme about an already governed role value; naming changes none of those objects.

### F.5:12 - Relations

**Builds on.** `A.2`, `F.4`, `F.7`, `F.18`, `E.10`, and `E.10.ARCH`.

**Coordinates with.** `E.24.UK` for U-kind admission and structural `U.*` repair; `A.2.1` for role assignment; `A.2.2` for capability; `A.2.5` for role state; `A.2.7` for role relation structure and role-algebra lens use; `A.6.5` for relation-slot names; `A.15` and A.15.1 for role-method-work alignment and dated work; C.2.1 and direct result patterns for claim-bearing and result epistemes; G.6 and A.10 for provenance and ordinary evidence reliance; B.3 for assurance-bearing reliance; `F.8` for mint-or-reuse; `F.9` for exact cross-taxonomy and cross-scheme Bridge occurrences; `F.10` for status mapping; `F.13` for aliases and continuity; `F.14` for anti-explosion; `F.15` for harness checks; `F.17` for public term-sheet use.

**Used by.** Part F unification patterns, role-description authors, Concept-Set authors, E.10 repairs that uncover naming rather than only phrase-use issues, and any FPF pattern that creates a durable local name for a U-kind or work-facing role label.

**Does not replace.** Direct evidence-use, status-use, requirement-use, source-use, publication-use, assurance, gate, decision, relation-signature, method, work, or architecture patterns.

### F.5:End

