## F.8 - Mint-or-Reuse Decision

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### F.8:0 - Use This When

**Plain name.** Name admission decision.

Use this pattern when a project has one candidate expression, has independently recovered the exact governed value or relation that the expression might designate, knows that value's direct governing pattern, and must choose the smallest naming disposition for one proposed use. The expression may stay local, reuse an existing designation, become an alias, reuse a direct-pattern name or an admitted Unified Term Sheet row, name a RoleDescription episteme, open a durable naming settlement, introduce a policy identifier, propose a new public row, or remain only a rare U-kind candidate.

Typical moments:

- a role-like expression such as `ReviewerRole`, `AccessRole`, `EvidenceRole`, `RequirementRole`, `ProviderRole`, or "actor" appears and the project must decide whether it designates a work-facing `U.Role`, a status-use relation, an evidence-use relation, an access or policy value, a relation position, or only a local phrase;
- a source tradition supplies a convenient name, but its local sense would import that tradition's ontology if promoted as an FPF designation;
- an F.17 row seems reusable, but its admitted use may be only naming rather than substitution, role assignment, measurement, or structural inference;
- a project wants a new U-kind, policy identifier, RoleDescription label, NameCard, or public term row because no existing expression feels comfortable; or
- an `E.10` repair discovers that a smoother word would still hide the current kind or relation.

**Primary working object.** The working object is one mint-or-reuse decision occurrence concerning one candidate expression, one independently governed value or relation, and one proposed naming use. If another claim needs to cite that occurrence, identify it through the direct decision or work owner. A separately constituted C.2.1 decision-result episteme may describe the occurrence, and a displayed record may designate that episteme; neither the episteme nor its record performs the decision. F.8 introduces no generic decision kind.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, pattern author, or terminology steward deciding whether a candidate expression deserves durable FPF treatment.

**First useful move.** Write four things before judging the wording: the candidate expression, the exact governed value or relation already recovered under its direct pattern, that direct pattern, and one proposed use. Then apply F.14 and try, in order, a local phrase, an existing designation, an alias, a current direct-pattern name, and an admitted F.17 row. Create no `SchemeSenseCell`, NameCard, row, policy identifier, or U-kind candidate until every lighter sufficient disposition has failed.

**What goes wrong if missed.** A convenient label becomes new ontology. A source word becomes global. A status, evidence, access, requirement, source, publication, or relation-position use gets named as a role. A public row is used beyond its admitted scope. A review label is treated as a context object, performed Work, role assignment, evidence use, or authority. FPF then accumulates duplicate kinds and naming records where it needed a smaller decision.

**What this buys.** Teams can reuse names without growing FPF by accident. Durable names become harder to mint but easier to trust. Role expressions become work-facing role names only when the role ontology is independently current; other expressions return to their direct patterns before naming. The effective naming ReferenceScheme and exact local-sense basis stay visible without inventing a universal context object.

**Not this pattern when.**

- If the issue is ordinary phrase repair with no durable name, use `E.10`, `E.10.ARCH`, `A.6.P`, or the direct governing pattern.
- If the issue is choosing labels after the mint-or-reuse disposition is already settled, use `F.5` for the local name family and `F.18` for the fuller durable naming settlement.
- If the issue is describing one work-facing role, use `F.4`.
- If the issue is assigning a holder to a role or attributing performed work, use `A.2.1`, `F.6`, and `A.15.1`.
- If the issue is an actual relation between two different local-sense projections, use `F.9`; use `F.17` only when a public, Core-facing, durable, or cross-local row is current.
- If the issue is status, evidence, source, standard, requirement, publication, assurance, gate, decision, policy use, method, work, or another subject claim, use its direct pattern before naming.

### F.8:1 - Problem Frame

Name pressure is often a sign of unresolved ontology. A project wants one short expression, but that expression may stand for several different governed values or uses: one local sense, an already selected designation, a public row, a RoleDescription label, a status value, a method name, a Work occurrence label, a policy identifier, or a new U-kind candidate.

The dangerous shortcut is to decide by word form or administrative setting. If the word contains `Role`, it is treated as a role. If the same spelling appears under two schemes, it is treated as the same concept. If a source standard uses the name, the name is promoted. If a record says a decision was made, the record is treated as the decision occurrence. If a label such as `PatternReview_2026` surrounds the work, it is treated as a context, role, assignment, evidence source, or authority without recovering the actual object and relation.

F.8 delays naming until the exact governed value, effective naming ReferenceScheme, local-sense basis, and proposed use are recovered. It is the gate between a local expression and a stronger naming disposition, not the naming style guide and not the direct owner of the named value.

### F.8:2 - Problem

Without this pattern:

1. **Local phrases become durable names.** A temporary phrase outlives its use and looks like FPF vocabulary.
2. **Source names capture FPF.** One tradition's word becomes the selected FPF name before its local sense and cross-local fit are shown.
3. **Role expressions become role ontology.** `EvidenceRole`, `RequirementRole`, `AccessRole`, or `ProviderRole` is promoted without checking whether a work-facing `U.Role` exists.
4. **Role names hide assignments.** A RoleDescription label is treated as if a holder already has the role.
5. **Public rows overreach.** A row admitted for naming is reused for assignment, measurement, equivalence, or structural inference.
6. **Aliases change meaning.** A prettier label is introduced but silently changes kind, scope, occurrence identity, or use.
7. **Kernel inflation follows comfort.** A new U-kind is proposed because existing names feel awkward.
8. **Policy identifiers appear as strings.** A policy identifier is reused or introduced without a separately resolvable policy specification and mint decision.
9. **Decision records act by proxy.** A filled card or record is treated as if it performed the decision or created its governed value.
10. **Locality labels become objects.** A review, team, project, or date label is made into a generic context and then used to manufacture work, roles, evidence, status, or authority.

### F.8:3 - Forces

| Force | Tension |
| --- | --- |
| Parsimony vs coverage | Avoid new durable names while still giving teams enough vocabulary for real recurring work. |
| Local sense vs cross-local reuse | A name can be obvious under one effective ReferenceScheme and unsafe for another exact local-sense projection. |
| Human readability vs ontology | Short names help use; they also hide kind, scope, occurrence identity, and relation if admitted too early. |
| Source familiarity vs FPF neutrality | A familiar source word may be useful as an alias while still being a bad selected FPF designation. |
| Naming speed vs downstream cost | Quick minting is cheap now and expensive when every subsequent pattern must repair it. |
| Traceability vs record-first collapse | A result episteme can make a decision inspectable, but it must not replace the decision occurrence or perform the governed action. |
| Open-world use vs false completeness | A missing durable name may mean "not current", not "new U-kind required". |

### F.8:4 - Solution

Treat mint-or-reuse as a typed disposition over an already recovered candidate, never as a vote on wording. Keep the following objects distinct:

- the exact governed value or relation and its direct pattern;
- the candidate expression, any selected designation, and any alias;
- the effective naming `U.ReferenceScheme`, exact local-sense claim, optional `SchemeSenseCell`, and any actual two-participant `LocalSenseBasisRelation`;
- the mint-or-reuse decision occurrence;
- any C.2.1 decision-result episteme and any record or carrier that designates it;
- any F.18 NameCard, F.17 row, policy specification, policy identifier, publication occurrence, form, or carrier; and
- an independently selected bounded-model-use Structure only when its organization changes interpretation for this exact naming use.

Ordinary use may stop with a readable disposition and no durable decision object. Materialize a decision occurrence reference or result episteme only when a receiving claim needs citation, replay, or accountability. When a C.2.1 result episteme is current, use this compact readable projection of its claim graph:

```text
MintReuseDecisionResultEpisteme:
  DecisionResultEpistemeId:
  EntityOfConcernRef: [the separately identified mint-or-reuse decision occurrence]
  CandidateExpression:
  GovernedValueOrRelationRef:
  GovernedKindOrRelationKindRef:
  DirectGoverningPatternRef:
  ProposedNamingUse:
  EffectiveNamingReferenceScheme: [U.ReferenceScheme carried by value]
  LocalSenseClaim:
  LocalSenseCellRef?: [only when an independently current SchemeSenseCell is needed]
  LocalSenseBasisRelationRef?: [only when the exact cell-to-basis-episteme relation obtains]
  SelectedModelUseStructureRef?: [only when an independently selected Structure changes this use]
  ReuseCandidateRefs?:
  SelectedDisposition:
  ResultingNamingRefs?: [only objects independently current after the disposition]
  NonAdmissibleOverread:
  ReopenCondition:
```

The block describes the result episteme; it is not the decision occurrence. `EntityOfConcernRef` resolves to that occurrence, while the remaining fields designate claims in the episteme's `U.ClaimGraph`. A record identifier, completed field set, NameCard, row, or publication creates neither the decision occurrence nor the governed value. If no result episteme is needed, apply the same distinctions in prose without creating a record.

Admissible dispositions are:

- `localPhraseOnly`;
- `reuseExistingDesignation`;
- `aliasOnly`;
- `reuseDirectPatternName`;
- `reuseAdmittedTermRow`;
- `nameRoleDescription`;
- `openDurableNamingSettlement`;
- `proposePublicTermRow`;
- `introducePolicyIdentifier`;
- `proposeUKindCandidate`; and
- `blockOrLowerUse`.

These are F.8 result labels, not new `U.*` kinds. A stronger result opens its direct owner; it does not itself mint the corresponding card, row, identifier, policy specification, relation occurrence, or U-kind.

#### F.8:4.1 - Decision Targets

| If the candidate expression designates... | Smallest F.8 disposition | Direct governing pattern |
| --- | --- | --- |
| A one-off phrase after local repair | `localPhraseOnly` | `E.10` or the direct governing pattern |
| An existing selected designation for the exact governed value and use | `reuseExistingDesignation` | The direct pattern, with `F.1`, `F.2`, and `F.3` for local-sense discovery and `F.5` or `F.18` only if naming settlement work is separately current |
| A wording variant for the same exact value, kind, scope, occurrence identity, and use | `aliasOnly` | `F.5`, `F.13`, `F.18` |
| An adequate name already supplied by the direct subject pattern | `reuseDirectPatternName` | The direct governing pattern |
| A cross-local or public reading already admitted by one exact F.17 row | `reuseAdmittedTermRow` only for its declared use | `F.17`; `F.9` only when an actual Bridge between exact cells is relied on |
| A label for a RoleDescription episteme describing one independently governed work-facing `U.Role` | `nameRoleDescription` | `A.2`, `F.4`, `F.5`; `F.18` if durable naming is current |
| A status, evidence, source, requirement, publication, assurance, gate, decision, method, Work, relation-position, characteristic, architecture, access, or policy value | `reuseDirectPatternName`, or `openDurableNamingSettlement` only after that value is recovered | Direct governing pattern, then `F.5` or `F.18` when needed |
| A recurring durable naming settlement not served by lighter dispositions | `openDurableNamingSettlement` | `F.14`, then `F.18`; a NameCard is optional until its own enduring-use gate passes |
| A public, Core-facing, durable, or cross-local term not covered by a current row | `proposePublicTermRow` | `F.17` after the exact F.18 inputs and row threshold are current |
| A policy identifier | reuse the current identifier or `introducePolicyIdentifier` with separately resolvable objects | `F.8:8.1`, plus the pattern governing the policy use |
| A missing cross-family primitive | `proposeUKindCandidate` | `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, `F.18` |

#### F.8:4.2 - Decision Sequence

Use this order and stop at the first disposition that supports the exact proposed use without hiding a governed distinction.

1. **Recover the four starting facts.** Name one candidate expression, one exact already-governed value or relation, its direct pattern, and one proposed use. If the value or obtaining relation is not independently current, stop and return to the direct pattern; F.8 cannot establish it.
2. **Split mixed candidates.** If one expression covers role, status, evidence, Work, method, measurement, policy, source, publication, or structure at once, split it into separate `<governed value, proposed use>` decisions.
3. **State exact semantic locality.** Carry the effective naming `U.ReferenceScheme` by value and state the local-sense claim. Cite a `SchemeSenseCell` and its exact `LocalSenseBasisRelation` only when those independently governed objects are current. Cite a selected bounded-model-use Structure only when its organization changes interpretation for this use.
4. **Apply F.14 and try a local phrase.** If ordinary local wording supports the use, choose `localPhraseOnly` and stop.
5. **Try an existing designation.** Reuse it only when exact value, kind, scope, occurrence identity, local-sense claim, and proposed use match.
6. **Try an alias.** Use `aliasOnly` when the governed meaning is unchanged and lineage can expose the wording variation. An alias may not change kind, scope, occurrence identity, use, or authority.
7. **Try the direct-pattern name.** Use the name already supplied by the exact role, status, evidence, policy, method, Work, relation, or other subject owner. Route work-facing role labels through `A.2`, `F.4`, and `F.5`; route assignment or performed Work through `A.2.1`, `F.6`, and `A.15.1` rather than naming.
8. **Try one admitted F.17 row.** Reuse only the row's declared `AdmissibleUse`. Local-sense reuse does not imply cross-local sameness; a row and equal spelling create no F.9 Bridge.
9. **Open only the next naming object that pays for itself.** A stable local address may justify a cell; an enduring naming settlement may justify a NameCard; a public/Core/durable/cross-local need may justify an F.17 row. None implies the next object.
10. **Introduce a policy identifier only for a recovered policy specification.** Keep the identifier, specification, mint decision occurrence, and result episteme or record distinct.
11. **Propose a new U-kind only rarely.** Require cross-family recurrence, irreducibility to existing FPF values or relations, `E.24.UK`, and the relevant A.8, A.11, C.3, E.9, and F.18 admission basis. F.8 only routes the proposal.
12. **Block or lower.** If no disposition is justified, keep the expression local, quote it as source wording, or lower the claim.

#### F.8:4.3 - Role Expression Boundary

A role expression becomes a durable role name only when the direct role owner has independently recovered one work-facing `U.Role`, or F.4 has constituted the RoleDescription episteme for that role. The naming ReferenceScheme interprets the expression; it neither supplies a role value nor assigns a holder.

| Source expression | Recovered case | F.8 result |
| --- | --- | --- |
| `ReviewerRole` in a review method | Work-facing role value needs a description and label | `nameRoleDescription`; use `A.2`, `F.4`, `F.5`, and `F.18` only when durable/public use is current |
| `Alice as reviewer` | Holder assigned to a role for a window | Not a name decision until `A.2.1` recovers the assignment |
| `review happened` | Dated performed Work | Use `A.15.1`; durable naming only if the Work-kind designation itself is current |
| `EvidenceRole` | Episteme used as evidence | Use evidence-use patterns; only then consider a name for the exact governed value or relation |
| `AccessRole` | Permission or policy grouping | Use access, policy, status, or deontic pattern; do not mint a `U.Role` by suffix |
| `ProviderRole` in a signature | Relation position | Use `A.6.5` SlotSpec discipline; name a slot only if needed |
| `RoleEnactment` in source prose | Source wording around assignment plus Work occurrence | Use `F.6`; do not mint `U.RoleEnactment` |

#### F.8:4.4 - F.17 Row-Scope Consumption

F.8 consumes one exact F.17 row and its declared use; it does not constitute the row or define Bridge strength. F.17 keeps the row episteme, governed value, designations, cell, basis relation, any F.9 Bridge, edition relation, and publication package distinct. F.8 asks only whether the row's `AdmissibleUse` covers the proposed naming use.

| Declared row use | F.8 admissible naming use | Non-admissible overread |
| --- | --- | --- |
| Naming-only | Shared prose label, glossary text, teaching label | equivalence, assignment, performed Work, structural inference, measurement equivalence |
| Role-description naming | RoleDescription label may cite the row as a comparison aid while one local `U.Role` remains primary | cross-local role identity or assignment by row alone |
| Measurement naming | Shared measurement label where units and procedure constraints remain visible | procedure interchange without the measurement pattern |
| Type-structure naming | Name for an admitted structural relation under the row's invariants | universal U-kind without `E.24.UK` and direct admission |

If the row does not admit the proposed use, lower the name's use or repair the exact F.17 row and any required F.9 relation. Do not strengthen a name because the wording is attractive, and do not infer cross-local sameness from local-sense reuse.

### F.8:5 - Invariants

1. **Governed value before disposition.** The candidate expression, exact governed value or relation, direct pattern, and one proposed use are named before any F.8 result.
2. **One decision, one exact use.** Mixed expressions are split by governed value and use before deciding.
3. **Lightest sufficient result.** Local phrase, existing designation, alias, direct-pattern name, and admitted row reuse are tried before a cell, NameCard, new row, policy identifier, or U-kind candidate.
4. **Reuse preserves identity.** Reuse cannot change kind, scope, occurrence identity, local-sense claim, admitted use, or authority.
5. **Local senses do not globalize.** Reusing a designation under one effective ReferenceScheme establishes neither sameness with another cell nor an F.9 Bridge.
6. **Role names are work-facing.** A role name or RoleDescription label points to an independently recovered work-facing `U.Role`; status, evidence, access, source, publication, requirement, assurance, gate, decision, policy, and relation-position uses remain direct-pattern values.
7. **Role assignment and Work are not naming.** A name, decision result, NameCard, cell, row, or identifier neither assigns a holder nor demonstrates performed Work.
8. **Rows stay within admitted use.** F.8 may reuse an F.17 row only at its declared use and gains no equivalence from the row.
9. **Decision occurrence and description stay distinct.** A C.2.1 result episteme or displayed record can describe a separately identified decision occurrence but cannot perform it.
10. **Naming objects stay distinct.** Governed value, designation, alias, cell, basis relation, NameCard, row, identifier, publication occurrence, form, carrier, and currentness relation imply none of the others.
11. **Selected structure is conditional.** A bounded-model-use Structure is cited only when independently selected organization changes interpretation for this exact use; it is not a generic locality or identity slot.
12. **New U-kind candidates are rare.** Cross-family recurrence, irreducibility, `E.24.UK` admission, and accepted decision basis are necessary; F.8 itself admits no U-kind.
13. **Policy identifiers are resolvable.** A policy identifier remains distinct from its policy specification, mint decision occurrence, and decision-result episteme or record.
14. **Labels grant no authority.** Source titles, review labels, suffixes, rows, records, and identifiers create no ontology, evidence, status, equivalence, permission, or publication authority.

### F.8:6 - Reasoning Primitives

```text
candidateExpression(E) and not(independentlyRecoveredGovernedValueOrRelation(V))
  -> stop F.8; run E.10 or the direct subject pattern before naming.
```

```text
candidateExpression(E) and governedValueOrRelation(V) and directPattern(P) and proposedUse(U)
  -> choose the lightest naming disposition for <V,U>; not(establish(V)) and not(makeObtain(V)).
```

```text
existingDesignationOrLocalPhrase(V, U) is sufficient
  -> reuse or stay local; do not mint a cell, NameCard, row, identifier, or U-kind candidate.
```

```text
alias(E2, designation(E1,V))
  -> preserve kind(V), scope(V), occurrenceIdentity(V), admittedUse(V), and lineage(E1,E2).
```

```text
localSense(E, ReferenceScheme S, LocalSenseClaim L)
  -> not(crossLocalSameness) and not(Bridge) without an independently obtaining F.9 relation.
```

```text
E names one work-facing Role R
  -> use A.2/F.4/F.5 for role-description naming; use A.2.1 for assignment and A.15.1/F.6 for performed Work.
```

```text
E names an episteme-use, status-use, policy-use, source-use, publication-use, or relation-position case
  -> recover the direct pattern before selecting any durable designation.
```

```text
F17Row(Row) and admittedUse(Row,U)
  -> F.8 may reuse Row for U only; not(equivalence) and not(widerUse).
```

```text
DecisionResultEpisteme(R) and entityOfConcern(R,D)
  -> R describes decision occurrence D; not(R = D) and not(recordPerformsDecision(R)).
```

```text
E is a proposed new U-kind
  -> require irreducibility, cross-family recurrence, E.24.UK, and an accepted direct admission basis; F.8 only routes.
```

### F.8:7 - Archetypal Grounding - worked cases

#### F.8:7.1 - Reviewer Role vs Review Report

The source label `PatternReview_2026` is not a context object. Classify the actual claim before using it:

- `ReviewWork-82` can be one dated `U.Work` occurrence under `A.15.1`;
- `ReviewPlan-2026-v3` can be a separately constituted plan episteme or edition under its direct owner;
- `PatternReviewReferenceScheme-2026` can be an effective by-value `U.ReferenceScheme` for interpreting review terminology; and
- "used while deciding the label for the 2026 review method" can be claim content describing the decision-use setting without minting any context entity.

If the independently governed `ReviewerRole` value is work-facing, F.8 may return `nameRoleDescription`: use `F.4` for the RoleDescription episteme and `F.5` or `F.18` for the label when its durability is current. The review label does not create that role, assign a reviewer, or demonstrate review Work.

The expression "review report has reviewer role" is a different case. `ReviewReport-82` is an episteme. A direct evidence, source, or publication relation may later use it for an adequacy claim about a reviewed pattern; the report does not hold the work-facing role, and its title does not make any evidence use or publication authority obtain.

#### F.8:7.2 - Actor Across BPMN and PROV

A manager wants one word, "actor", for a BPMN participant and a PROV agent in a diagram. First recover the two exact local senses under their effective ReferenceSchemes. If an actual F.9 Bridge relates the exact cells and one F.17 row admits naming-only use, F.8 returns `reuseAdmittedTermRow` for prose and diagram labels only.

No governed-value identity, substitution, role assignment, or Work follows. If the project later needs a work-facing role under one scheme, it creates or reuses the local RoleDescription episteme for that independently recovered role value.

#### F.8:7.3 - Access Role

An access-control source says `ApproverRole`. Under the source's effective naming ReferenceScheme, the expression may designate a permission grouping or exact policy relation. F.8 first returns to the access, policy, status, or deontic owner. Only if `A.2` independently governs a work-facing approval role does a RoleDescription naming decision become current.

Otherwise the durable designation, if needed, belongs to the direct access, policy, status, or gate pattern. The `Role` suffix, a source card, or a selected model-use Structure creates no work-facing role or assignment.

#### F.8:7.4 - Policy Identifier

A gate profile proposes `Aut-Guard-2026`. F.8 treats this as a policy-identifier question only after an exact policy specification is independently recoverable. Reuse resolves the existing identifier, its separate specification, and the original mint decision. New introduction identifies a new mint decision occurrence and, when durable trace is needed, its separate result episteme or record.

The identifier is not the specification, role, method, gate result, evidence value, permission, or source authority. It is a reference used by the pattern that governs the exact policy claim.

#### F.8:7.5 - New U-kind Candidate

A team proposes `U.InfluenceEdge` because many documents use "influence". F.8 blocks immediate minting. The team must show that the candidate is not an existing relation, causal claim, evidence relation, characteristic, method relation, Bridge relation, structural name, publication form, or local frame under current patterns. If it remains cross-family, irreducible, and needed by several domain families, the proposal goes to `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, and `F.18`. F.8 neither creates nor admits the kind.

#### F.8:7.6 - Filled Decision Result and Explicit Pre-F.8 Stop

The first projection records a result about a separately identified naming decision. `PatternReviewReferenceScheme-2026` is the effective naming scheme; the actual review Work, any review plan, and this decision-use setting remain separate.

```text
MintReuseDecisionResultEpisteme:
  DecisionResultEpistemeId: MRD-ReviewerRole-2026-v1
  EntityOfConcernRef: ReviewerRoleNamingDecision-2026-07-31
  CandidateExpression: ReviewerRole
  GovernedValueOrRelationRef: ReviewerRoleValue
  GovernedKindOrRelationKindRef: U.Role
  DirectGoverningPatternRef: A.2
  ProposedNamingUse: durable local label for the RoleDescription episteme used by the review method
  EffectiveNamingReferenceScheme: PatternReviewReferenceScheme-2026
  LocalSenseClaim: work-facing role whose holder may perform exact pattern-review Work under a separately governed assignment
  LocalSenseCellRef: omitted; no receiving use needs a stable cell address yet
  LocalSenseBasisRelationRef: omitted; the direct local-sense claim and A.2/F.4 basis are sufficient at this gate
  SelectedModelUseStructureRef: omitted; no independently selected Structure changes this naming use
  ReuseCandidateRefs: no existing designation or alias supports the exact proposed use
  SelectedDisposition: nameRoleDescription
  ResultingNamingRefs: F.4 RoleDescription authoring next; F.18 only if durable reuse remains current
  NonAdmissibleOverread: the decision and its result episteme do not assign Alice, show that review Work occurred, make a review report evidence, or publish the label
  ReopenCondition: reopen if the expression is used for evidence, status, access, source, publication, or cross-local row claims
```

The second case does not enter F.8. The proposed `EvidenceRole` wording has exposed an evidence-use question, but no exact governed relation, relation kind, or single direct owner has yet been recovered. The review label again supplies no context, evidence, or authority.

```text
PreF8RecoveryStop:
  CandidateExpression: EvidenceRole
  KnownSubject: ReviewReport-82 : U.Episteme
  ProposedNamingUse: reusable wording for one exact evidence-use relation
  EffectiveNamingReferenceScheme: PatternReviewReferenceScheme-2026
  RecoveredFact: ReviewReport-82 is proposed for evidence use concerning an adequacy claim; it is not a role holder
  MissingEntryFacts: the exact target claim and polarity; the exact evidence-use relation and relation kind; provenance, assurance or reliance use, and validity window when current; one direct governing pattern
  RequiredDirectOwnerAction: recover those facts under the single pattern that directly governs the exact evidence-use claim
  LocalSenseState: no stable cell address or independently current LocalSenseBasisRelation is needed for this blocked role reading
  SelectedModelUseStructureState: none; no independently selected Structure changes this use
  DirectTerminologyProbe: test the eventual direct evidence-pattern terminology only after recovery
  StopResult: do not enter F.8 and do not mint EvidenceRole; keep the expression local until the governed relation, exact kind, one direct pattern, and proposed naming use are present
  NonAdmissibleOverread: this stop creates no evidence relation, role, RoleDescription, assignment, authority, or publication
  ReopenCondition: enter F.8 only after one exact governed relation, its exact relation kind, one direct governing pattern, and the proposed naming use are independently present; reopen the direct claim first if its target claim, polarity, provenance, assurance or reliance use, or validity window changes
```

### F.8:8.0 - Bias-Annotation

F.8 blocks minting bias and record-first bias. A convenient expression, suffix, title, source term, review label, stable identifier, filled card, or memorable public phrase proves neither that FPF needs a new name nor that the named object or decision exists. Start from the exact governed value or relation, direct pattern, proposed use, effective naming ReferenceScheme, and local-sense basis. Choose the smallest adequate disposition. Treat a selected bounded-model-use Structure, decision result, NameCard, row, and publication package as separate objects only when their own direct conditions are current.

#### F.8:8.1 - Policy-Identifier Mint-or-Reuse Discipline

FPF treats policy identifiers such as `Phi(CL)`, `Phi_plane`, `Psi(CL^k)`, `Aut-Guard`, `EmitterPolicyRef`, insertion-policy identifiers, and acceptance-clause identifiers as versioned references whose meaning must be recoverable. They are not "just strings", role names, gate decisions, permissions, or policy specifications.

```text
PolicyIdentifierReference:
  PolicyIdentifier:
  PolicySpecificationRef:
  MintDecisionOccurrenceRef:
  MintDecisionResultEpistemeRef?:
  ScopeOrNamespaceRef:
```

`PolicyIdentifier` is the selected designator. `PolicySpecificationRef` resolves to the separate policy-definition episteme, pins an edition or equivalent digest when needed, and remains findable through the same publication family or an exact cited source relation; it does not identify or mint the identifier. `MintDecisionOccurrenceRef` resolves to the separate decision that introduced the identifier in the declared namespace. `MintDecisionResultEpistemeRef`, when current, resolves to a C.2.1 episteme or accepted record describing that occurrence; the record does not perform the decision.

For FPF normative policy identifiers, the durable result episteme is usually an accepted `E.9` decision record. For a local non-exported identifier, the direct gate, decision, or publication pattern may admit a smaller result episteme when local scope is explicit. In either case, the policy specification, identifier, decision occurrence, and record remain distinct.

Rules:

1. **No silent policy-identifier introduction.** A newly introduced identifier resolves both the separate `PolicySpecificationRef` and mint decision occurrence; when durable trace is needed, it also resolves the separate result episteme or record.
2. **Reuse is reference use.** Reusing an existing identifier resolves the same identifier, its policy specification, and its original mint decision; it does not restate policy semantics or silently create another decision.
3. **Gate checkability.** A gate, crossing, Bridge, assurance, or publication claim that depends on a policy identifier includes `PolicyIdentifierReference` or an equivalent resolvable structure admitted by its governing pattern.
4. **Policy authority stays with the governing pattern.** F.8 selects introduction or reuse of the identifier; it does not decide whether the policy permits Work, passes a gate, makes a relation obtain, or provides evidence.
5. **The identifier grants nothing by itself.** Name, namespace, suffix, source prestige, specification publication, or decision record grants no permission, status, equivalence, or authority beyond the exact direct policy claim.

### F.8:8 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-F8-01` | One candidate expression, one exact independently governed value or relation, its direct pattern, and one proposed use are named before the disposition. |
| `CC-F8-02` | Mixed role, status, evidence, source, requirement, method, Work, measurement, policy, publication, or structure uses are split by governed value and use. |
| `CC-F8-03` | Effective naming ReferenceScheme and exact local-sense claim are explicit; a cell, basis relation, or selected Structure appears only when independently current. |
| `CC-F8-04` | Local phrase, existing designation, alias, direct-pattern name, and admitted F.17 row were tried before any stronger naming object. |
| `CC-F8-05` | Reuse preserves kind, scope, occurrence identity, local-sense claim, admitted use, and authority boundary. |
| `CC-F8-06` | Role expressions become durable role names only after the exact `U.Role` and RoleDescription ontology are recovered. |
| `CC-F8-07` | Assignment and performed-Work claims use `A.2.1`, `F.6`, and `A.15.1`, not naming. |
| `CC-F8-08` | Status, evidence, access, source, requirement, publication, assurance, gate, decision, and relation-position names return to direct governing patterns. |
| `CC-F8-09` | F.17 row reuse stays within the row's `AdmissibleUse`; local-sense reuse and equal spelling imply neither F.9 Bridge nor equivalence. |
| `CC-F8-10` | Decision occurrence, C.2.1 result episteme, displayed record, and any resulting naming objects remain distinct. |
| `CC-F8-11` | `PatternReview_2026` or another locality label is reclassified as exact Work, plan/edition, decision-use claim content, or effective ReferenceScheme when that object is current; the label creates none of them. |
| `CC-F8-12` | New U-kind candidates cite cross-family recurrence, irreducibility, `E.24.UK`, and the accepted direct admission basis; F.8 claims no admission. |
| `CC-F8-13` | Policy identifiers resolve to separate policy specifications and mint decisions; any result record remains a description. |
| `CC-F8-14` | The result states its non-admissible overread and the smallest condition that reopens it. |

### F.8:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Suffix minting | A word ending in `Role`, `Status`, `Graph`, `Map`, or `Record` becomes ontology. | Recover the exact governed value or relation, direct owner, and proposed use first. |
| Evidence role revival | `EvidenceRole` becomes a role-name family. | Recover the exact evidence-use relation; name it only through its direct owner. |
| Status-role fusion | `ReadyReviewerRole` or `ApprovedRole` names a role plus state. | Separate the work-facing role from the state or status-use relation. |
| Row overuse | A public naming row justifies equivalence, role assignment, or structural inference. | Lower use to the exact F.17 `AdmissibleUse` or repair the row and any required Bridge. |
| Alias with payload | An alias changes kind, scope, occurrence identity, use, or authority. | Treat it as a different decision; use `F.5`, `F.13`, and `F.18`. |
| Source prestige minting | A standard or framework term becomes the selected FPF name by prestige. | Keep it as source wording, evidence for a local sense, or an alias until exact recovery and selection pass. |
| Review label as context | `PatternReview_2026` is used as context, Work, role assignment, evidence, or authority. | Recover the exact dated Work or plan/edition, decision-use claim, or effective ReferenceScheme needed by the actual assertion. |
| Decision record as decision | A filled record is treated as performing a mint decision or creating its result. | Identify the decision occurrence through its direct owner; constitute a separate C.2.1 result episteme only when needed. |
| Naming-object cascade | One expression automatically gets a cell, NameCard, row, identifier, and publication. | Apply F.14 at every gate and create only the next object whose receiving use pays for it. |
| U-kind comfort minting | A new U-kind is proposed because existing names feel awkward. | Attempt reduction to local phrase, existing designation, alias, direct-pattern name, admitted row, existing relation, or existing U-kind; use `E.24.UK` before admission. |
| Policy identifier as magic word | An identifier is used without a separately resolvable specification or mint decision. | Supply the exact references or lower the claim. |

### F.8:10 - Consequences

Good consequences:

- durable vocabulary grows more slowly and with clearer justification;
- role, status, evidence, access, source, requirement, publication, and slot-position cases stop forming duplicate role ontology;
- effective ReferenceSchemes and exact local-sense claims replace generic context slots without erasing real locality;
- F.17 rows keep their declared scope, and local-sense reuse no longer masquerades as cross-local equivalence;
- F.5 and F.18 receive better naming inputs because F.8 has already selected the smallest disposition;
- decision occurrences and result records become independently inspectable; and
- policy identifiers become checkable references instead of decorative strings.

Costs:

- authors must recover kind, direct owner, use, scheme, and local-sense basis before naming;
- mixed expressions require separate decisions;
- some attractive names remain local phrases or aliases;
- durable public or cross-local names may require independently justified cell, NameCard, Bridge, row, reliance, decision-result, and publication objects; and
- a new U-kind becomes harder to justify because minting waits for `E.24.UK` and the relevant admission law rather than naming comfort.

Reopen F.8 when `E.24.UK`, `A.2`, `A.2.1`, `A.15.1`, `F.4`, `F.5`, `F.6`, `F.9`, `F.14`, `F.17`, `F.18`, `A.6.5`, `C.2.1`, `E.10`, `E.9`, `A.8`, `A.11`, or policy-identifier discipline changes enough that the dispositions or object boundaries would change.

### F.8:11 - Rationale

F.8 is placed before naming style because a naming mistake is often a kind, locality, or use mistake. A practitioner should not ask "what name should we use?" until the exact governed value or relation, its direct owner, proposed use, effective ReferenceScheme, and local-sense claim are recoverable.

The pattern is intentionally narrower than `F.18`. F.18 can run a durable naming settlement, candidate comparison, NameCard, lineage, and later F.17 row gate. F.8 supplies the prior disposition: should this expression remain local, reuse something already current, or open one stronger naming path? It does not create the value or perform the stronger path.

The strict role boundary is central. A role expression names a work-facing role only when `U.Role` is independently recovered. Epistemes, publications, standards, requirements, evidence, statuses, permissions, gates, decisions, methods, Work, and relation positions may need names, but they do not become roles because source prose used `role`.

The decision-description boundary is equally important. A mint-or-reuse decision occurrence, a C.2.1 result episteme about it, and a rendered record answer different questions. Keeping them distinct provides traceability without letting administrative artifacts perform content decisions.

### F.8:12 - SoTA-Echoing - Source-Use

| Practice line | What FPF adopts | Practical implication |
| --- | --- | --- |
| Controlled-vocabulary and terminology practice | Preferred labels, aliases, definitions, scope notes, and deprecated labels are separate fields and uses. | F.8 decides the smallest disposition; F.5, F.13, and F.18 then name without confusing alias with meaning change. |
| Ontology engineering and conceptual modeling | New classes or kinds are expensive and should be tested against existing values, relations, and constraints. | New U-kind candidates require `E.24.UK`, irreducibility, and direct admission basis, not comfort. |
| Domain-driven bounded-model-use practice | Interpretation may depend on an independently selected organization of model use. | Carry the effective naming ReferenceScheme for every naming use; cite a selected bounded-model-use Structure only when its organization changes this use. |
| Authorization and policy-reference practice | Policy identifiers must resolve to definitions and governance decisions. | Keep identifier, policy specification, mint decision occurrence, and result record separate; the identifier is not permission, gate passage, or evidence. |
| FPF role, Work, and episteme ontology | Work-facing roles, RoleDescriptions, assignments, dated Work, decision results, evidence use, and status use are distinct. | Split role-like and record-like source expressions by exact kind before durable naming. |

Source-use boundary: a source tradition may supply candidate expressions, aliases, and current practice pressure. It does not select the FPF disposition, establish the governed value, make a relation obtain, or confer authority. Those claims follow the direct pattern and independently recovered facts.

### F.8:13 - Relations

**Builds on.** `A.7`, `E.24.UK`, `A.8`, `A.11`, `E.10`, `E.10.ARCH`, `F.1`, `F.2`, `F.3`, `F.5`, `F.9`, `F.14`, `F.17`, and `F.18`.

**Coordinates with.** `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.6.5`, `A.15`, `A.15.1`, `F.4`, `F.6`, `F.10`, `F.13`, `F.15`, `C.2.1`, `C.3`, `E.9`, `E.24.CD`, `E.24.PUB`, and the direct status-use, evidence-use, source-use, publication-use, requirement-use, assurance, gate, decision, policy, method, Work, characteristic, and architecture patterns.

**Constrains.**

- `F.5` names only after F.8 has selected the exact naming case.
- `F.4` governs only work-facing RoleDescription naming cases.
- `F.9` governs an actual Bridge between exact cells; `F.17` governs any admitted public-row use before F.8 reuses it.
- `F.18` expands durable naming only after lighter dispositions have failed.
- `F.14` supplies the anti-explosion stop before every stronger F.8 disposition.
- `F.15` may check the resulting distinctions; it neither chooses the disposition nor creates a naming object.

**Does not replace.** The direct governing patterns for the value or relation, decision occurrence, RoleAssignment, performed Work, status, evidence, source, publication, requirement, assurance, gate, policy, method, relation slot, characteristic, architecture, selected Structure, or their descriptions.

### F.8:14 - Didactic Memory

Do not ask for a better name first. Recover one exact governed value or relation and one use; state the effective naming ReferenceScheme and local-sense claim; then try local phrase, existing designation, alias, direct-pattern name, and admitted F.17 row. Mint only the next object that pays for itself. A label, card, row, identifier, publication, or decision record creates none of the ontology, Work, assignment, evidence, status, equivalence, or authority it mentions.

### F.8:End

