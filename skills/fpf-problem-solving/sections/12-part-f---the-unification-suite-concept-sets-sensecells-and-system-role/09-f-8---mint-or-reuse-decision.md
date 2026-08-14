## F.8 - Mint-or-Reuse Decision

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### F.8:0 - Use This When

**Plain name.** Name admission decision.

Use this pattern when a project has one candidate expression, has independently recovered the exact governed value or relation that the expression might designate, knows that value's subject pattern, and must choose the smallest naming disposition for one proposed use. The expression may stay local, reuse an existing designation, become an alias, reuse a direct-pattern name or an admitted Unified Term Sheet row, name a `SystemRoleKindDescription` episteme, open a durable naming settlement, introduce a policy identifier, propose a new public row, or remain only a rare U-kind candidate.

Typical moments:

- a role-like expression such as `ReviewerRole`, `AccessRole`, `EvidenceRole`, `RequirementRole`, `ProviderRole`, or "actor" appears and the project must decide whether it designates a context-local system-role kind for `U.System` candidates, a status-use relation, an evidence-use relation, an access or policy value, a relation position, or only a local phrase;
- a source tradition supplies a convenient name, but its local sense would import that tradition's ontology if promoted as an FPF designation;
- an F.17 row seems reusable, but its admitted use may be only naming rather than substitution, system-role assignment, measurement, or structural inference;
- a project wants a new U-kind, policy identifier, `SystemRoleKindDescription` label, NameCard, or public term row because no existing expression feels comfortable; or
- an `E.10` repair discovers that a smoother word would still hide the current kind or relation.

**Primary working object.** The working object is one F.8 naming disposition concerning one candidate expression, one independently recovered value or relation, and one proposed naming use. Ordinary use needs no separately identified decision occurrence. When citation, replay, or accountability genuinely requires such an occurrence, first recover it through the direct decision or choice pattern: name that pattern, its admitted predicate, actual participants, applicability, and occurrence-identity rule. If no such direct pattern is current, return the A.6.RCD `missing-governor` result instead of inventing a `...NamingDecision` individual. A C.11 `ChoiceResult`, a C.2.1 episteme describing a decision, and any dated decision-making Work remain separate. F.8 introduces no generic decision kind.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, pattern author, or terminology steward deciding whether a candidate expression deserves durable FPF treatment.

**First useful move.** Write four things before judging the wording: the candidate expression, the exact governed value or relation already recovered under its direct pattern, that direct pattern, and one proposed use. Then apply F.14 and try, in order, a local phrase, an existing designation, an alias, a current direct-pattern name, and an admitted F.17 row. Create no `SchemeSenseCell`, NameCard, row, policy identifier, or U-kind candidate until every lighter sufficient disposition has failed.

**What goes wrong if missed.** A convenient label becomes new ontology. A source word becomes global. A status, evidence, access, requirement, source, publication, or relation-position use gets named as a local system-role kind. A public row is used beyond its admitted scope. A review label is treated as a context object, performed Work, system-role assignment, evidence use, or authority. FPF then accumulates duplicate kinds and naming records where it needed a smaller decision.

**What this buys.** Teams can reuse names without growing FPF by accident. Durable names become harder to mint but easier to trust. A role expression becomes a local system-role-kind name only when A.2 has independently recovered that ontology; other readings return to their direct patterns before naming. The effective naming ReferenceScheme and exact local-sense basis stay visible without inventing a universal context object.

**Not this pattern when.**

- If the issue is ordinary phrase repair with no durable name, use `E.10`, `E.10.ARCH`, `A.6.P`, or the subject pattern.
- If the issue is choosing labels after the mint-or-reuse disposition is already settled, use `F.5` for the local name family and `F.18` for the fuller durable naming settlement.
- If the issue is describing one local system-role kind, use `F.4`.
- If the issue is assigning a system to a local system-role kind or attributing performed work, use `A.2.1`, `F.6`, and `A.15.1`.
- If the issue is an actual relation between two different local-sense projections, use `F.9`; use `F.17` only when a public, Core-facing, durable, or cross-local row is current.
- If the issue is status, evidence, source, standard, requirement, publication, assurance, gate, decision, policy use, method, work, or another subject claim, use its direct pattern before naming.

### F.8:1 - Problem Frame

Name pressure is often a sign of unresolved ontology. A project wants one short expression, but that expression may stand for several different governed values or uses: one local sense, an already selected designation, a public row, a `SystemRoleKindDescription` label, a status value, a method name, a Work occurrence label, a policy identifier, or a new U-kind candidate.

The dangerous shortcut is to decide by word form or administrative setting. If the word contains `Role`, it is treated as a local system-role kind. If the same spelling appears under two schemes, it is treated as the same concept. If a source standard uses the name, the name is promoted. If a record says a decision was made, the record is treated as the decision occurrence. If a label such as `PatternReview_2026` surrounds the work, it is treated as a context, system-role kind, assignment, evidence source, or authority without recovering the actual object and relation.

F.8 delays naming until the exact governed value, effective naming ReferenceScheme, local-sense basis, and proposed use are recovered. It is the gate between a local expression and a stronger naming disposition, not the naming style guide and not the subject pattern of the named value.

### F.8:2 - Problem

Without this pattern:

1. **Local phrases become durable names.** A temporary phrase outlives its use and looks like FPF vocabulary.
2. **Source names capture FPF.** One tradition's word becomes the selected FPF name before its local sense and cross-local fit are shown.
3. **Role expressions become system-role ontology.** `EvidenceRole`, `RequirementRole`, `AccessRole`, or `ProviderRole` is promoted without checking whether one exact context-local system-role kind exists for `U.System` candidates.
4. **System-role-kind names hide assignments.** A `SystemRoleKindDescription` label is treated as if a system were already assigned to the kind.
5. **Public rows overreach.** A row admitted for naming is reused for assignment, measurement, equivalence, or structural inference.
6. **Aliases change meaning.** A prettier label is introduced but silently changes kind, scope, occurrence identity, or use.
7. **Kernel inflation follows comfort.** A new U-kind is proposed because existing names feel awkward.
8. **Policy identifiers appear as strings.** A policy identifier is reused without a separately resolvable policy specification, or introduced for an accountable use without the direct basis for its mint decision or choice occurrence.
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
- when independently current, the exact mint-or-reuse decision or choice occurrence and its direct pattern;
- any C.2.1 decision-result episteme and any record or carrier that designates it;
- any F.18 NameCard, F.17 row, policy specification, policy identifier, publication occurrence, form, or carrier; and
- an independently selected bounded-model-use Structure only when its organization changes interpretation for this exact naming use.

Ordinary use may stop with a readable disposition and no durable decision object. Materialize a decision-occurrence reference or C.2.1 result episteme only after a direct pattern has independently admitted the exact occurrence and a receiving claim needs citation, replay, or accountability. In that conditional branch, use this compact readable projection of the result episteme's claim graph:

```text
MintReuseDecisionResultEpisteme:
  DecisionResultEpistemeId:
  EntityOfConcernRef: [exact decision or choice occurrence already admitted by its direct pattern]
  DecisionGovernorLocator:
  DecisionPredicateRef:
  DecisionParticipantRefs: [actual participants with their meanings]
  DecisionApplicability:
  DecisionOccurrenceIdentityBasis:
  DecisionMakingWorkRef?: [separate A.15.1 Work only when current]
  DecisionOrChoiceResultRef?: [separate result, such as a C.11 ChoiceResult, only when current]
  CandidateExpression:
  GovernedValueOrRelationRef:
  GovernedKindOrRelationKindRef:
  GovernedValueSubjectPatternLocator:
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
The block describes the result episteme; it is not the decision or choice occurrence. `EntityOfConcernRef` resolves to the occurrence already admitted by `DecisionGovernorLocator`; the predicate, participant, applicability, and identity fields show why that occurrence exists. `GovernedValueSubjectPatternLocator` separately identifies the pattern for the value being named. A C.11 `ChoiceResult` is a separate result, and dated decision-making Work is a separate A.15.1 occurrence. A record identifier, completed field set, NameCard, row, or publication creates none of them. If the direct occurrence cannot be recovered, do not instantiate this block: return the exact A.6.RCD `missing-governor` result. If no result episteme is needed, apply the same distinctions in prose without creating a record.

Admissible dispositions are:

- `localPhraseOnly`;
- `reuseExistingDesignation`;
- `aliasOnly`;
- `reuseDirectPatternName`;
- `reuseAdmittedTermRow`;
- `nameSystemRoleKindDescription`;
- `openDurableNamingSettlement`;
- `proposePublicTermRow`;
- `introducePolicyIdentifier`;
- `proposeUKindCandidate`; and
- `blockOrLowerUse`.

These are F.8 result labels, not new `U.*` kinds. A stronger result opens its subject pattern; it does not itself mint the corresponding card, row, identifier, policy specification, relation occurrence, or U-kind.

#### F.8:4.1 - Decision Targets

| If the candidate expression designates... | Smallest F.8 disposition | Subject pattern |
| --- | --- | --- |
| A one-off phrase after local repair | `localPhraseOnly` | `E.10` or the subject pattern |
| An existing selected designation for the exact governed value and use | `reuseExistingDesignation` | The direct pattern, with `F.1`, `F.2`, and `F.3` for local-sense discovery and `F.5` or `F.18` only if naming settlement work is separately current |
| A wording variant for the same exact value, kind, scope, occurrence identity, and use | `aliasOnly` | `F.5`, `F.13`, `F.18` |
| An adequate name already supplied by the direct subject pattern | `reuseDirectPatternName` | The subject pattern |
| A cross-local or public reading already admitted by one exact F.17 row | `reuseAdmittedTermRow` only for its declared use | `F.17`; `F.9` only when an actual Bridge between exact cells is relied on |
| A label for a `SystemRoleKindDescription` episteme describing one independently recovered context-local system-role kind for `U.System` candidates | `nameSystemRoleKindDescription` | `A.2`, `F.4`, `F.5`; `F.18` if durable naming is current |
| A status, evidence, source, requirement, publication, assurance, gate, decision, method, Work, relation-position, characteristic, architecture, access, or policy value | `reuseDirectPatternName`, or `openDurableNamingSettlement` only after that value is recovered | Subject pattern, then `F.5` or `F.18` when needed |
| A recurring durable naming settlement not served by lighter dispositions | `openDurableNamingSettlement` | `F.14`, then `F.18`; a NameCard is optional until its own enduring-use gate passes |
| A public, Core-facing, durable, or cross-local term not covered by a current row | `proposePublicTermRow` | `F.17` after the exact F.18 inputs and row threshold are current |
| A policy identifier | reuse the current identifier or `introducePolicyIdentifier` with its separately resolvable specification and, for accountable minting, its direct occurrence basis | `F.8:8.1`, plus the pattern for the policy use |
| A missing cross-family primitive | `proposeUKindCandidate` | `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, `F.18` |

#### F.8:4.2 - Decision Sequence

Use this order and stop at the first disposition that supports the exact proposed use without hiding a governed distinction.

1. **Recover the four starting facts.** Name one candidate expression, one exact already-governed value or relation, its direct pattern, and one proposed use. If the value or obtaining relation is not independently current, stop and use the direct pattern; F.8 cannot establish it.
2. **Split mixed candidates.** If one expression covers a system-role kind, system-role assignment, status, evidence, Work, method, measurement, policy, source, publication, or structure at once, split it into separate `<governed value, proposed use>` decisions.
3. **State exact semantic locality.** Carry the effective naming `U.ReferenceScheme` by value and state the local-sense claim. Cite a `SchemeSenseCell` and its exact `LocalSenseBasisRelation` only when those independently governed objects are current. Cite a selected bounded-model-use Structure only when its organization changes interpretation for this use.
4. **Apply F.14 and try a local phrase.** If ordinary local wording supports the use, choose `localPhraseOnly` and stop.
5. **Try an existing designation.** Reuse it only when exact value, kind, scope, occurrence identity, local-sense claim, and proposed use match.
6. **Try an alias.** Use `aliasOnly` when the governed meaning is unchanged and lineage can expose the wording variation. An alias may not change kind, scope, occurrence identity, use, or authority.
7. **Try the subject's existing name.** Use the name already supplied for the exact system-role kind, status, evidence, policy, method, Work, relation, or other governed subject. Treat local system-role-kind labels under the exact predicates located through `A.2`, `F.4`, and `F.5`; treat assignment or performed Work under `A.2.1`, `F.6`, and `A.15.1` rather than as a naming problem.
8. **Try one admitted F.17 row.** Reuse only the row's declared `AdmissibleUse`. Local-sense reuse does not imply cross-local sameness; a row and equal spelling create no F.9 Bridge.
9. **Open only the next naming object that pays for itself.** A stable local address may justify a cell; an enduring naming settlement may justify a NameCard; a public/Core/durable/cross-local need may justify an F.17 row. None implies the next object.
10. **Introduce a policy identifier only for a recovered policy specification.** A local non-accountable identifier may designate that specification without manufacturing a decision occurrence. When the introduction or mint history must be cited, replayed, treated as normative, reused across its local boundary, or made accountable, also recover the exact mint decision or choice occurrence through its direct pattern; if no such pattern is current, return `missing-governor` for that stronger history claim and do not make the accountable introduction. Keep any C.11 result, decision-making Work, result episteme, and displayed record separate.
11. **Propose a new U-kind only rarely.** Require cross-family recurrence, irreducibility to existing FPF values or relations, `E.24.UK`, and the relevant A.8, A.11, C.3, E.9, and F.18 admission basis. F.8 only routes the proposal.
12. **Block or lower.** If no disposition is justified, keep the expression local, quote it as source wording, or lower the claim.

#### F.8:4.3 - Role Expression Boundary

A role expression becomes a durable name for a local system-role kind only after `A.2` has independently recovered one exact context-local `U.Kind` whose candidates are `U.System` values, or `F.4` has constituted the `SystemRoleKindDescription` episteme for that kind. The kind's identity basis states the stable, assignable, work-facing contribution; its `KindSignature` states how a candidate system qualifies. The naming ReferenceScheme interprets the expression; it neither defines the kind nor assigns a system.

| Source expression | Recovered case | F.8 result |
| --- | --- | --- |
| `ReviewerRole` in a review method | One local review-system-role kind needs a description and label | `nameSystemRoleKindDescription`; use `A.2`, `F.4`, `F.5`, and `F.18` only when durable or public use is current |
| `Alice as reviewer` | A system is assigned to a local system-role kind for an interval | Not a name decision until `A.2.1` recovers the `U.SystemRoleAssignment` occurrence |
| `review happened` | Dated performed Work | Use `A.15.1`; durable naming only if the Work-kind designation itself is current |
| `EvidenceRole` | Episteme used as evidence | Use evidence-use patterns; only then consider a name for the exact governed value or relation |
| `AccessRole` | Permission or policy grouping | Use access, policy, status, or deontic pattern; do not mint a local system-role kind by suffix |
| `ProviderRole` in a signature | Relation position | Use `A.6.5` SlotSpec discipline; name a slot only if needed |
| `RoleEnactment` in source prose | Source wording around a `U.SystemRoleAssignment` plus a Work occurrence | Use `F.6`; do not mint `U.RoleEnactment` |

#### F.8:4.4 - F.17 Row-Scope Consumption

F.8 consumes one exact F.17 row and its declared use; it does not constitute the row or define Bridge strength. F.17 keeps the row episteme, governed value, designations, cell, basis relation, any F.9 Bridge, edition relation, and publication package distinct. F.8 asks only whether the row's `AdmissibleUse` covers the proposed naming use.

| Declared row use | F.8 admissible naming use | Non-admissible overread |
| --- | --- | --- |
| Naming-only | Shared prose label, glossary text, teaching label | equivalence, assignment, performed Work, structural inference, measurement equivalence |
| System-role-kind-description naming | A `SystemRoleKindDescription` label may cite the row as a comparison aid while one local system-role kind remains primary | cross-local kind identity or assignment by row alone |
| Measurement naming | Shared measurement label where units and procedure constraints remain visible | procedure interchange without the measurement pattern |
| Type-structure naming | Name for an admitted structural relation under the row's invariants | universal U-kind without `E.24.UK` and direct admission |

If the row does not admit the proposed use, lower the name's use or repair the exact F.17 row and any required F.9 relation. Do not strengthen a name because the wording is attractive, and do not infer cross-local sameness from local-sense reuse.

### F.8:5 - Invariants

1. **Governed value before disposition.** The candidate expression, exact governed value or relation, direct pattern, and one proposed use are named before any F.8 result.
2. **One decision, one exact use.** Mixed expressions are split by governed value and use before deciding.
3. **Lightest sufficient result.** Local phrase, existing designation, alias, direct-pattern name, and admitted row reuse are tried before a cell, NameCard, new row, policy identifier, or U-kind candidate.
4. **Reuse preserves identity.** Reuse cannot change kind, scope, occurrence identity, local-sense claim, admitted use, or authority.
5. **Local senses do not globalize.** Reusing a designation under one effective ReferenceScheme establishes neither sameness with another cell nor an F.9 Bridge.
6. **System-role-kind names are work-facing.** Such a name or `SystemRoleKindDescription` label points to an independently recovered context-local `U.Kind` for `U.System` candidates; status, evidence, access, source, publication, requirement, assurance, gate, decision, policy, and relation-position uses remain direct-pattern values.
7. **System-role assignment and Work are not naming.** A name, decision result, NameCard, cell, row, or identifier neither assigns a system nor demonstrates performed Work.
8. **Rows stay within admitted use.** F.8 may reuse an F.17 row only at its declared use and gains no equivalence from the row.
9. **Decision occurrence and description stay distinct.** Ordinary F.8 use creates no durable decision object. When a direct pattern has admitted an exact decision or choice occurrence, a C.2.1 result episteme or displayed record may describe it but cannot perform it; absent that predicate, participants, applicability, and identity rule, return `missing-governor`.
10. **Naming objects stay distinct.** Governed value, designation, alias, cell, basis relation, NameCard, row, identifier, publication occurrence, form, carrier, and currentness relation imply none of the others.
11. **Selected structure is conditional.** A bounded-model-use Structure is cited only when independently selected organization changes interpretation for this exact use; it is not a generic locality or identity slot.
12. **New U-kind candidates are rare.** Cross-family recurrence, irreducibility, `E.24.UK` admission, and accepted decision basis are necessary; F.8 itself admits no U-kind.
13. **Policy identifiers are resolvable.** A policy identifier remains distinct from its policy specification, the exact independently admitted mint decision or choice occurrence when one is required, any C.11 result, any decision-making Work, and the decision-result episteme or record.
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
E names one local system-role kind K
  -> use A.2/F.4/F.5 for system-role-kind-description naming; use A.2.1 for `U.SystemRoleAssignment` and A.15.1/F.6 for performed Work.
```

```text
E names an episteme-use, status-use, policy-use, source-use, publication-use, or relation-position case
  -> recover the direct pattern before selecting any durable designation.
```

```text
F17Row(Row) and admittedUse(Row,U)
  -> F.8 may reuse Row for U only; not(equivalence) and not(widerUse).
```

**Decision-occurrence check.** A decision-result episteme describes an occurrence; it does not perform the decision. Before accepting its `EntityOfConcernRef`, resolve the direct decision or choice pattern, admitted predicate, actual participants, applicability, and occurrence identity. If any of those are unavailable, return the exact `missing-governor` result and do not mint an occurrence identifier. Keep a C.11 `ChoiceResult` and any dated decision-making Work as separate objects under their own patterns.
```text
E is a proposed new U-kind
  -> require irreducibility, cross-family recurrence, E.24.UK, and an accepted direct admission basis; F.8 only routes.
```

### F.8:7 - Archetypal Grounding - worked cases

#### F.8:7.1 - `ReviewerRole` Expression vs Review Report

The source label `PatternReview_2026` is not a context object. Classify the actual claim before using it:

- `ReviewWork-82` can be one dated `U.Work` occurrence under `A.15.1`;
- `ReviewPlan-2026-v3` can be a separately constituted plan episteme or edition under its subject pattern;
- `PatternReviewReferenceScheme-2026` can be an effective by-value `U.ReferenceScheme` for interpreting review terminology; and
- "used while deciding the label for the 2026 review method" can be claim content describing the decision-use setting without minting any context entity.

If the independently governed `ReviewerSystemRole` is a local system-role kind, F.8 may return `nameSystemRoleKindDescription`: use `F.4` for the `SystemRoleKindDescription` episteme and `F.5` or `F.18` for the label when its durability is current. The review label does not define that kind, assign a reviewer system, or demonstrate review Work.

The expression "review report has reviewer role" is a different case. `ReviewReport-82` is an episteme. A direct evidence, source, or publication relation may later use it for an adequacy claim about a reviewed pattern; the report is not a `U.System`, is not classified by the local review-system-role kind, and cannot enter its assignment relation. Its title does not make any evidence use or publication authority obtain.

#### F.8:7.2 - Actor Across BPMN and PROV

A manager wants one word, "actor", for a BPMN participant and a PROV agent in a diagram. First recover the two exact local senses under their effective ReferenceSchemes. If an actual F.9 Bridge relates the exact cells and one F.17 row admits naming-only use, F.8 returns `reuseAdmittedTermRow` for prose and diagram labels only.

No governed-value identity, substitution, system-role assignment, or Work follows. If the project later needs a local system-role kind under one scheme, it creates or reuses the local `SystemRoleKindDescription` episteme for that independently recovered kind.

#### F.8:7.3 - Access Role

An access-control source says `ApproverRole`. Under the source's effective naming ReferenceScheme, the expression may designate a permission grouping or exact policy relation. F.8 first recovers the exact access, policy, status, or deontic assertion and predicate. Only if A.2 independently recovers an exact local approval-system-role kind does a `SystemRoleKindDescription` naming decision become current.

Otherwise the durable designation, if needed, belongs to the direct access, policy, status, or gate pattern. The `Role` suffix, a source card, or a selected model-use Structure creates no local system-role kind or assignment.

#### F.8:7.4 - Policy Identifier

A gate profile proposes `Aut-Guard-2026`. F.8 treats this as a policy-identifier question only after an exact policy specification is independently recoverable. Ordinary reuse resolves the existing identifier and its separate specification. Recover the original mint decision or choice occurrence only when the current reuse relies on that history for citation, replay, accountability, supersession, or another named relation. New introduction requires the direct mint basis when such a claim is made; without its predicate, participants, applicability, and occurrence identity, return `missing-governor` for that stronger claim. Any C.11 result, decision-making Work, result episteme, or displayed record stays separate.

The identifier is not the specification, local system-role kind, method, gate result, evidence value, permission, or source authority. It is a reference used by the pattern that defines or constrains the exact policy claim.

#### F.8:7.5 - New U-kind Candidate

A team proposes `U.InfluenceEdge` because many documents use "influence". F.8 blocks immediate minting. The team must show that the candidate is not an existing relation, causal claim, evidence relation, characteristic, method relation, Bridge relation, structural name, publication form, or local frame under current patterns. If it remains cross-family, irreducible, and needed by several domain families, the proposal goes to `E.24.UK`, `A.8`, `A.11`, `C.3`, `E.9`, and `F.18`. F.8 neither creates nor admits the kind.

#### F.8:7.6 - Readable Disposition and Explicit Stops

The first case needs only the light F.8 result. `PatternReviewReferenceScheme-2026` is the effective naming scheme; the actual review Work, any review plan, and this naming use remain separate. The following is a readable projection, not an identified decision occurrence or durable decision record:

```text
CandidateExpression: ReviewerRole
GovernedValueOrRelationRef: ReviewerSystemRole
GovernedKindOrRelationKindRef: the admitted U.Kind for ReviewerSystemRole
GovernedValueSubjectPatternLocator: A.2
ProposedNamingUse: durable local label for the SystemRoleKindDescription episteme used by the review method
EffectiveNamingReferenceScheme: PatternReviewReferenceScheme-2026
LocalSenseClaim: local U.Kind for U.System candidates, identified by the stable review contribution and tested by its KindSignature; assignment is separate
ReuseCandidateRefs: no existing designation or alias supports the exact proposed use
SelectedDisposition: nameSystemRoleKindDescription
ResultingNamingRefs: F.4 SystemRoleKindDescription authoring next; F.18 only if durable reuse remains current
DurableDecisionOccurrence: omitted; no receiving claim needs citation, replay, or accountability
DecisionResultEpisteme: omitted
NonAdmissibleOverread: the disposition assigns no System, establishes no review Work or evidence use, and publishes no label
ReopenCondition: reopen if the expression is used for evidence, status, access, source, publication, or cross-local row claims
```

If a later receiving claim genuinely needs an accountable occurrence, first recover its direct decision or choice pattern, predicate, actual participants, applicability, and identity rule. No such direct pattern is current in this worked case, so the correct durable branch result is `missing naming-decision governor`; do not mint `ReviewerSystemRoleNamingDecision-2026-07-31`. A C.11 `ChoiceResult` may be used only when the case is genuinely a local choice among already available options and satisfies C.11; any dated decision-making Work remains separate under A.15.1 and F.6.

The second case does not enter F.8. The proposed `EvidenceRole` wording has exposed an evidence-use question, but no exact governed relation, relation kind, or single subject pattern has yet been recovered. The review label again supplies no context, evidence, or authority.

```text
PreF8RecoveryStop:
  CandidateExpression: EvidenceRole
  KnownSubject: ReviewReport-82 : U.Episteme
  ProposedNamingUse: reusable wording for one exact evidence-use relation
  EffectiveNamingReferenceScheme: PatternReviewReferenceScheme-2026
  RecoveredFact: ReviewReport-82 is proposed for evidence use concerning an adequacy claim; it is not a system and cannot be assigned to a local system-role kind
  MissingEntryFacts: the exact target claim and polarity; the exact evidence-use relation and relation kind; provenance, assurance or reliance use, and validity window when current; one subject pattern
  RequiredDirectPatternUse: apply the one pattern whose Solution defines the exact evidence-use relation and recover the missing entry facts there
  LocalSenseState: no stable cell address or independently current LocalSenseBasisRelation is needed for this blocked role-word reading
  SelectedModelUseStructureState: none; no independently selected Structure changes this use
  DirectTerminologyProbe: test the eventual direct evidence-pattern terminology only after recovery
  StopResult: do not enter F.8 and do not mint EvidenceRole; keep the expression local until the governed relation, exact kind, one direct pattern, and proposed naming use are present
  NonAdmissibleOverread: this stop creates no evidence relation, local system-role kind, SystemRoleKindDescription, assignment, authority, or publication
  ReopenCondition: enter F.8 only after one exact governed relation, its exact relation kind, one subject pattern, and the proposed naming use are independently present; reopen the direct claim first if its target claim, polarity, provenance, assurance or reliance use, or validity window changes
```

### F.8:8.0 - Bias-Annotation

F.8 blocks minting bias and record-first bias. A convenient expression, suffix, title, source term, review label, stable identifier, filled card, or memorable public phrase proves neither that FPF needs a new name nor that the named object or decision exists. Start from the exact governed value or relation, direct pattern, proposed use, effective naming ReferenceScheme, and local-sense basis. Choose the smallest adequate disposition. Treat a selected bounded-model-use Structure, decision result, NameCard, row, and publication package as separate objects only when their own direct conditions are current.

#### F.8:8.1 - Policy-Identifier Mint-or-Reuse Discipline

FPF treats policy identifiers such as `Phi(CL)`, `Phi_plane`, `Psi(CL^k)`, `Aut-Guard`, `EmitterPolicyRef`, insertion-policy identifiers, and acceptance-clause identifiers as versioned references whose meaning must be recoverable. They are not "just strings", system-role-kind names, gate decisions, permissions, or policy specifications.

```text
PolicyIdentifierReference:
  PolicyIdentifier:
  PolicySpecificationRef:
  MintDecisionOrChoiceOccurrenceRef?: required only for cited, replayed, normative, cross-local reuse, or accountable mint history
  MintDecisionSubjectPatternLocator?: paired with MintDecisionOrChoiceOccurrenceRef
  MintDecisionPredicateRef?: paired with MintDecisionOrChoiceOccurrenceRef
  MintDecisionParticipantRefs?: [actual participants with their meanings]
  MintDecisionApplicability?:
  MintDecisionOccurrenceIdentityBasis?:
  MintDecisionMakingWorkRef?: [separate A.15.1 Work only when current]
  MintDecisionOrChoiceResultRef?: [separate result, such as a C.11 ChoiceResult, only when current]
  MintDecisionResultEpistemeRef?:
  ScopeOrNamespaceRef:
```
`PolicyIdentifier` is the selected designator. `PolicySpecificationRef` resolves to the separate policy-definition episteme and pins an edition or equivalent digest when needed. A local non-accountable introduction can stop there with explicit local scope. The conditional mint-occurrence fields are required when the use cites, replays, makes normative, reuses across the local boundary, or assigns accountability to the mint history; together they resolve one independently admitted decision or choice occurrence and its direct pattern, predicate, actual participants, applicability, and identity rule. If that stronger use is requested and those facts are absent, return `missing-governor` for it rather than inventing an occurrence. A C.11 `ChoiceResult` and any dated decision-making Work remain separate. `MintDecisionResultEpistemeRef`, when current, resolves to a C.2.1 episteme or accepted record describing the occurrence; the record does not perform the decision.

For FPF normative policy identifiers, the durable result episteme is usually an accepted `E.9` decision record, but only after the direct decision or choice pattern has admitted the occurrence that record describes. A local non-exported and non-accountable identifier needs only its separately recoverable specification and explicit scope; it need not create a decision or result episteme. In every branch, the policy specification, identifier, any decision or choice occurrence, any C.11 result, any decision-making Work, and any record remain distinct.

Rules:

1. **No silent policy-identifier introduction.** Every new identifier resolves the separate `PolicySpecificationRef` and states its scope. A local non-accountable introduction stops there. A cited, replayed, normative, cross-local, or accountable mint history additionally resolves the exact decision or choice occurrence plus its direct pattern, predicate, participants, applicability, and identity rule; without that direct basis, return `missing-governor` for the stronger branch and do not claim it.
2. **Reuse is reference use.** Reusing an existing identifier resolves the same identifier and policy specification. Resolve the original mint occurrence only when the current reuse consumes or asserts that history; it does not restate policy semantics, turn a record into the occurrence, or silently create another decision.
3. **Gate checkability.** A gate, crossing, Bridge, assurance, or publication claim that depends on a policy identifier includes `PolicyIdentifierReference` or an equivalent resolvable structure admitted by its subject pattern.
4. **Policy authority stays with the subject pattern.** F.8 selects introduction or reuse of the identifier; it does not decide whether the policy permits Work, passes a gate, makes a relation obtain, or provides evidence.
5. **The identifier grants nothing by itself.** Name, namespace, suffix, source prestige, specification publication, or decision record grants no permission, status, equivalence, or authority beyond the exact direct policy claim.

### F.8:8 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-F8-01` | One candidate expression, one exact independently governed value or relation, its direct pattern, and one proposed use are named before the disposition. |
| `CC-F8-02` | Mixed system-role-kind, system-role-assignment, status, evidence, source, requirement, method, Work, measurement, policy, publication, or structure uses are split by governed value and use. |
| `CC-F8-03` | Effective naming ReferenceScheme and exact local-sense claim are explicit; a cell, basis relation, or selected Structure appears only when independently current. |
| `CC-F8-04` | Local phrase, existing designation, alias, direct-pattern name, and admitted F.17 row were tried before any stronger naming object. |
| `CC-F8-05` | Reuse preserves kind, scope, occurrence identity, local-sense claim, admitted use, and authority boundary. |
| `CC-F8-06` | A role expression becomes a durable local system-role-kind name only after A.2 has recovered the exact context-local `U.Kind`, its `U.System` candidate domain, contribution identity basis, `KindSignature`, and `SystemRoleKindDescription`; assignment remains separate. |
| `CC-F8-07` | Assignment and performed-Work claims use `A.2.1`, `F.6`, and `A.15.1`, not naming. |
| `CC-F8-08` | Status, evidence, access, source, requirement, publication, assurance, gate, decision, and relation-position names return to subject patterns. |
| `CC-F8-09` | F.17 row reuse stays within the row's `AdmissibleUse`; local-sense reuse and equal spelling imply neither F.9 Bridge nor equivalence. |
| `CC-F8-10` | Ordinary use creates no durable decision object. Any cited decision or choice occurrence resolves its direct pattern, predicate, actual participants, applicability, and occurrence identity; otherwise the result is `missing-governor`. Any C.11 result, decision-making Work, C.2.1 episteme, displayed record, and resulting naming objects remain distinct. |
| `CC-F8-11` | `PatternReview_2026` or another locality label is reclassified as exact Work, plan/edition, decision-use claim content, or effective ReferenceScheme when that object is current; the label creates none of them. |
| `CC-F8-12` | New U-kind candidates cite cross-family recurrence, irreducibility, `E.24.UK`, and the accepted direct admission basis; F.8 claims no admission. |
| `CC-F8-13` | A policy identifier resolves its separate specification and explicit scope. A local non-accountable introduction requires no manufactured occurrence. A cited, replayed, normative, cross-local, or accountable mint history additionally resolves the direct pattern, predicate, actual participants, applicability, and identity basis for its occurrence; without them, that stronger branch returns `missing-governor`. Any result record or Work remains separate. |
| `CC-F8-14` | The result states its non-admissible overread and the smallest condition that reopens it. |

### F.8:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Suffix minting | A word ending in `Role`, `Status`, `Graph`, `Map`, or `Record` becomes ontology. | Recover the exact governed value or relation, subject pattern, and proposed use first. |
| Evidence-role revival | `EvidenceRole` becomes a system-role-kind name family. | Recover the exact evidence-use relation; name it only through its subject pattern. |
| Status-system-role fusion | `ReadyReviewerRole` or `ApprovedRole` names a local system-role kind plus state. | Separate the system-role kind from the assignment-state or status-use relation. |
| Row overuse | A public naming row justifies equivalence, system-role assignment, or structural inference. | Lower use to the exact F.17 `AdmissibleUse` or repair the row and any required Bridge. |
| Alias with payload | An alias changes kind, scope, occurrence identity, use, or authority. | Treat it as a different decision; use `F.5`, `F.13`, and `F.18`. |
| Source prestige minting | A standard or framework term becomes the selected FPF name by prestige. | Keep it as source wording, evidence for a local sense, or an alias until exact recovery and selection pass. |
| Review label as context | `PatternReview_2026` is used as context, Work, system-role assignment, evidence, or authority. | Recover the exact dated Work or plan or edition, decision-use claim, or effective ReferenceScheme needed by the actual assertion. |
| Decision identifier or record as decision | An identifier or filled record is treated as the decision occurrence or as creating its result. | Recover the occurrence through its direct pattern, predicate, actual participants, applicability, and identity rule. If none is current, return `missing-governor`; constitute a separate C.2.1 result episteme only when needed. |
| Naming-object cascade | One expression automatically gets a cell, NameCard, row, identifier, and publication. | Apply F.14 at every gate and create only the next object whose receiving use pays for it. |
| U-kind comfort minting | A new U-kind is proposed because existing names feel awkward. | Attempt reduction to local phrase, existing designation, alias, direct-pattern name, admitted row, existing relation, or existing U-kind; use `E.24.UK` before admission. |
| Policy identifier as magic word | An identifier is used without a separately resolvable specification, or its mint history is called accountable, cited, replayable, normative, or reusable across the local boundary without an occurrence basis. | Supply the specification for every identifier. For the stronger history claim, supply its direct occurrence basis or return `missing-governor`; a merely local non-accountable identifier does not manufacture one. |

### F.8:10 - Consequences

Good consequences:

- durable vocabulary grows more slowly and with clearer justification;
- role words used for status, evidence, access, source, requirement, publication, or slot positions stop forming duplicate system-role-kind ontology;
- effective ReferenceSchemes and exact local-sense claims replace generic context slots without erasing real locality;
- F.17 rows keep their declared scope, and local-sense reuse no longer masquerades as cross-local equivalence;
- F.5 and F.18 receive better naming inputs because F.8 has already selected the smallest disposition;
- independently current decision or choice occurrences and their result records remain separately inspectable; and
- policy identifiers become checkable references instead of decorative strings.

Costs:

- authors must recover kind, subject pattern, use, scheme, and local-sense basis before naming;
- mixed expressions require separate decisions;
- some attractive names remain local phrases or aliases;
- durable public or cross-local names may require independently justified cell, NameCard, Bridge, row, reliance, decision-result, and publication objects; and
- a new U-kind becomes harder to justify because minting waits for `E.24.UK` and the relevant admission law rather than naming comfort.

Reopen F.8 when `E.24.UK`, `A.2`, `A.2.1`, `A.6.RCD`, `A.15.1`, `C.11`, `F.4`, `F.5`, `F.6`, `F.9`, `F.14`, `F.17`, `F.18`, `A.6.5`, `C.2.1`, `E.10`, `E.9`, `A.8`, `A.11`, or policy-identifier discipline changes enough that the dispositions or object boundaries would change.

### F.8:11 - Rationale

F.8 is placed before naming style because a naming mistake is often a kind, locality, or use mistake. A practitioner should not ask "what name should we use?" until the exact governed value or relation, its subject pattern, proposed use, effective ReferenceScheme, and local-sense claim are recoverable.

The pattern is intentionally narrower than `F.18`. F.18 can run a durable naming settlement, candidate comparison, NameCard, lineage, and later F.17 row gate. F.8 supplies the prior disposition: should this expression remain local, reuse something already current, or open one stronger naming path? It does not create the value or perform the stronger path.

The strict role-expression boundary is central. A role expression names a local system-role kind only when A.2 independently recovers the exact context-local `U.Kind`, its `U.System` candidate domain, contribution identity basis, and `KindSignature`. Epistemes, publications, standards, requirements, evidence, statuses, permissions, gates, decisions, methods, Work, and relation positions may need names, but they do not become system-role kinds because source prose used `role`.

The decision-description boundary is equally important when a direct pattern has admitted an accountable decision or choice occurrence. That occurrence, a C.2.1 result episteme about it, and a rendered record answer different questions. Keeping them distinct provides traceability without letting administrative artifacts perform content decisions; ordinary F.8 use stops earlier with no durable decision object.

### F.8:12 - SoTA-Echoing - Source-Use

| Practice line | What FPF adopts | Practical implication |
| --- | --- | --- |
| Controlled-vocabulary and terminology practice | Preferred labels, aliases, definitions, scope notes, and deprecated labels are separate fields and uses. | F.8 decides the smallest disposition; F.5, F.13, and F.18 then name without confusing alias with meaning change. |
| Ontology engineering and conceptual modeling | New classes or kinds are expensive and should be tested against existing values, relations, and constraints. | New U-kind candidates require `E.24.UK`, irreducibility, and direct admission basis, not comfort. |
| Domain-driven bounded-model-use practice | Interpretation may depend on an independently selected organization of model use. | Carry the effective naming ReferenceScheme for every naming use; cite a selected bounded-model-use Structure only when its organization changes this use. |
| Authorization and policy-reference practice | Policy identifiers must resolve to definitions and, when accountable minting is claimed, the direct basis for that mint decision or choice occurrence. | Keep identifier, policy specification, occurrence, any C.11 result, any decision-making Work, and result record separate; the identifier is not permission, gate passage, or evidence. |
| FPF system-role, Work, and episteme ontology | Local system-role kinds, `SystemRoleKindDescription` epistemes, `U.SystemRoleAssignment` occurrences, dated Work, decision results, evidence use, and status use are distinct. | Split role-like and record-like source expressions by exact kind or relation before durable naming. |

Source-use boundary: a source tradition may supply candidate expressions, aliases, and current practice pressure. It does not select the FPF disposition, establish the governed value, make a relation obtain, or confer authority. Those claims follow the direct pattern and independently recovered facts.

### F.8:13 - Relations

**Builds on.** `A.7`, `E.24.UK`, `A.8`, `A.11`, `E.10`, `E.10.ARCH`, `F.1`, `F.2`, `F.3`, `F.5`, `F.9`, `F.14`, `F.17`, and `F.18`.

**Coordinates with.** `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.6.5`, `A.6.RCD`, `A.15`, `A.15.1`, `C.11`, `F.4`, `F.6`, `F.10`, `F.13`, `F.15`, `C.2.1`, `C.3`, `E.9`, `E.24.CD`, `E.24.PUB`, and the direct status-use, evidence-use, source-use, publication-use, requirement-use, assurance, gate, decision, choice, policy, method, Work, characteristic, and architecture patterns.

**Constrains.**

- `F.5` names only after F.8 has selected the exact naming case.
- Use `F.4` only for local `SystemRoleKindDescription` naming cases.
- `F.9` governs an actual Bridge between exact cells; `F.17` governs any admitted public-row use before F.8 reuses it.
- `F.18` expands durable naming only after lighter dispositions have failed.
- `F.14` supplies the anti-explosion stop before every stronger F.8 disposition.
- `F.15` may check the resulting distinctions; it neither chooses the disposition nor creates a naming object.

**Does not replace.** The subject patterns for the value or relation, decision occurrence, local system-role kind, `U.SystemRoleAssignment`, performed Work, status, evidence, source, publication, requirement, assurance, gate, policy, method, relation slot, characteristic, architecture, selected Structure, or their descriptions.

### F.8:14 - Didactic Memory

Do not ask for a better name first. Recover one exact value or relation and one use; state the effective naming ReferenceScheme and local-sense claim; then try local phrase, existing designation, alias, direct-pattern name, and admitted F.17 row. Stop with the readable disposition unless a receiving claim truly needs an accountable decision occurrence. In that rarer branch, recover its direct predicate, participants, applicability, and identity or return `missing-governor`. A label, card, row, identifier, publication, C.11 result, Work occurrence, or decision record creates none of the ontology, assignment, evidence, status, equivalence, authority, or decision occurrence it mentions.

### F.8:End

