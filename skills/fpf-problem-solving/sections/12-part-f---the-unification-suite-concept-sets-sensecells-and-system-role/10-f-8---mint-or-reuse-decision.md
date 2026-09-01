## F.8 - Mint-or-Reuse Decision

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### F.8:0 - Use This When

**Plain name.** Keep, reuse, or strengthen a name.

Use F.8 after the subject is known and a project must decide the smallest naming treatment for one expression and one use. Start only when these four facts are available: the expression, the governed value or relation, its subject pattern, and the proposed naming use.

Typical triggers include:

- a familiar source word may be useful locally but would import the source ontology if promoted;
- a role-like word such as `ReviewerRole`, `AccessRole`, or `EvidenceRole` may name a system-role kind, another governed value or relation, or only ordinary wording;
- an alias, subject-pattern name, or F.17 row may already serve the use, but only within its stated meaning and scope;
- a governed value may need a durable name, public row, or policy identifier; and
- pressure for a new U-kind appears. That last case stops before naming until E.24.UK has returned a stable admission disposition.

**Primary working object.** One F.8 disposition for the expression and proposed use. Ordinary use creates no decision occurrence or result episteme. If a later claim must cite, replay, or assign accountability to the decision itself, use the separately triggered branch in §4.5.

**Primary working reader.** An engineer-manager, analyst, method author, pattern author, or terminology steward choosing whether an expression should stay local, reuse a name, or open a stronger naming path.

**First useful move.** Write the four starting facts. Then try, in order, a local phrase, an existing designation, an alias, the subject pattern's name, and an admitted F.17 row. Stop at the first sufficient result. Open a cell, NameCard, public row, or policy identifier only when the receiving use needs it.

**What goes wrong if missed.** A convenient expression is treated as the subject it merely names. Local or source wording becomes durable ontology; a row or alias gains uses it never admitted; a role-like word hides a kind, description, assignment, Work occurrence, or another governed relation; or a record is mistaken for the decision it describes.

**What this buys.** Teams get short usable names without creating duplicate kinds or naming records. Stronger names are harder to introduce but easier to trust because the governed subject and use remain visible.

**Not this pattern when.**

- For one-off wording repair, use the applicable wording rule—E.10, E.10.ARCH, or A.6.P—or the subject pattern.
- If the governed subject or relation is not yet known, recover it first. For an unsettled U-kind proposal, use E.24.CD when the object is unclear and E.24.UK for admission.
- To constitute a `SystemRoleKindDescription`, use F.4. To assign a system, use A.2.1. For precise performed Work, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated occurrence; add F.6 only when the naming case or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment.
- For an obtaining relation between different local-sense projections, use F.9. Use F.17 when a public, Core-facing, durable, or cross-local row is needed.
- For a status, evidence use, policy, Method, Work, publication, or any other governed subject, use its subject pattern before naming it.
- After F.8 has selected a name family, use F.5 for its naming discipline and F.18 only for a durable naming settlement.

### F.8:1 - Problem Frame

Name pressure often reveals an unresolved subject. One word may be offered for different things—for example, a designation, local system-role kind, optional description of that kind, assignment occurrence, status value, policy identifier, or Work label. Shared spelling proves none of these identities.

F.8 therefore asks what the expression will designate and for which use before judging the wording. It is the gate from a local expression to a stronger naming treatment. It neither defines the governed value nor performs the later naming work.

### F.8:2 - Problem

Without this pattern:

1. **Local or source wording becomes durable ontology.** A temporary phrase or familiar standard term survives without a recovered subject and use.
2. **Role-like wording collapses different objects.** A local system-role kind, its optional F.4 description, an A.2.1 assignment, performed Work, or another governed relation receives one misleading label.
3. **Reuse widens silently.** An alias changes meaning, or an F.17 row admitted for naming is reused for equivalence, assignment, measurement, or structural inference.
4. **Naming is asked to admit ontology.** A proposed U-kind enters F.8 before E.24.UK has settled whether the result is an admitted kind, reused kind, local kind, or recovered non-kind object.
5. **Identifiers and records act by proxy.** A policy identifier lacks a resolvable specification, or a filled record is treated as the decision occurrence or result it describes.
6. **Locality labels become subjects.** A review, team, project, or date label is used as if it created Work, assignment, evidence, status, or authority.

### F.8:3 - Forces

| Force | Tension |
| --- | --- |
| Parsimony vs coverage | Avoid new durable names while keeping enough vocabulary for recurring work. |
| Local fit vs reuse | A name may be clear under one ReferenceScheme and unsafe for another use or local sense. |
| Readability vs hidden ontology | Short names help readers but can hide kind, relation, scope, or occurrence identity. |
| Familiarity vs neutrality | A source word may be a useful alias without being the selected FPF designation. |
| Speed vs downstream cost | Quick minting is cheap now and expensive when later patterns must repair it. |
| Traceability vs record-first collapse | A result episteme can support replay without becoming the decision occurrence. |
| Open-world use vs false completeness | No durable name may mean “not needed now”, not “a new U-kind is required”. |

### F.8:4 - Solution

Treat mint-or-reuse as a decision about an already recovered subject, not a vote on wording. Start with four facts:

1. the candidate expression;
2. the governed value or relation;
3. the subject pattern that defines or tests that value or relation; and
4. the proposed naming use.

If any fact is missing, stop at the subject-recovery route; naming cannot supply it. Otherwise try the dispositions in this order and stop at the first one that supports the proposed use:

1. keep a local phrase;
2. reuse an existing designation;
3. use an alias without changing the governed meaning;
4. reuse the subject pattern's name;
5. reuse an admitted F.17 row within its stated use;
6. name a separately justified `SystemRoleKindDescription` when that is the governed object;
7. open a durable naming settlement;
8. propose a public row;
9. introduce a policy identifier for an already recovered policy specification; or
10. block or lower the naming use.

The smallest result is one readable sentence, not a mandatory record: state the governed subject, proposed naming use, selected disposition, resulting name when any, and the change that would reopen the decision. Add a non-use boundary only when `F.19`'s grounded-contribution test admits it. For example: “Under `PatternReviewReferenceScheme-2026`, use `ReviewerRole` as the Plain designation of `ReviewerSystemRole` for local review-method prose; select `openDurableNamingSettlement` and revisit the decision if the naming use becomes public or cross-local.”

The corresponding F.8 result labels are `localPhraseOnly`, `reuseExistingDesignation`, `aliasOnly`, `reuseDirectPatternName`, `reuseAdmittedTermRow`, `nameSystemRoleKindDescription`, `openDurableNamingSettlement`, `proposePublicTermRow`, `introducePolicyIdentifier`, and `blockOrLowerUse`. They are not new `U.*` kinds. A stronger result opens its subject pattern; it does not itself create a card, row, identifier, policy specification, or relation occurrence.

#### F.8:4.1 - Decision Targets

| If the candidate expression designates... | Smallest F.8 disposition | Subject pattern |
| --- | --- | --- |
| A one-off phrase after local repair | `localPhraseOnly` | `E.10` or the subject pattern |
| An existing selected designation for the governed value and use | `reuseExistingDesignation` | The subject pattern, with `F.1`, `F.2`, and `F.3` for local-sense discovery; use `F.5` or `F.18` only when naming work is separately needed |
| A wording variant for the same value, kind, scope, occurrence identity, and use | `aliasOnly` | `F.5`, `F.13`, and `F.18` |
| An adequate name already supplied by the subject pattern | `reuseDirectPatternName` | The subject pattern |
| A cross-local or public reading admitted by one F.17 row | `reuseAdmittedTermRow` only for its declared use | `F.17`; `F.9` only when an obtaining Bridge between the named cells is used |
| A new designation for a recovered local system-role kind | `localPhraseOnly` when local wording is enough; otherwise `openDurableNamingSettlement` when durable reuse is needed | `A.2` and `C.3` for the kind, then `F.5`; `F.18` only for a durable settlement |
| A label for a separately justified `SystemRoleKindDescription` episteme about that kind | `nameSystemRoleKindDescription` | `F.4` for the description, then `F.5`; `F.18` only when the description's own name must be durable |
| Any other governed subject—for example, a status, evidence use, source use, requirement, assurance use, gate, decision, access value, policy, Method, Work, publication use, characteristic, architecture value, or relation position | `reuseDirectPatternName`, or `openDurableNamingSettlement` only after that subject is recovered | Its subject pattern, then `F.5` or `F.18` when needed |
| A recurring durable naming settlement not served by lighter dispositions | `openDurableNamingSettlement` | `F.14`, then `F.18`; a NameCard is optional until its own enduring-use gate passes |
| A public, Core-facing, durable, or cross-local term not covered by an admitted row | `proposePublicTermRow` | `F.17` after the F.18 inputs and row threshold are met |
| A policy identifier | reuse the existing identifier, or select `introducePolicyIdentifier` for a recovered policy specification; add a mint-occurrence basis only for the stronger history uses in §8.1 | `F.8:8.1` and the subject pattern for the policy use |
| An expression offered as a new cross-family primitive before its admission disposition is stable | `blockOrLowerUse`; no naming disposition is available yet | `E.24.CD` when the governed object is still unclear; if a U-kind proposal remains, `E.24.UK` decides admission. Return only after the governed object is recovered or one stable `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject` result is available. |

#### F.8:4.2 - Decision Sequence

Use this order and stop at the first disposition that supports the proposed use without hiding a governed distinction.

1. **Recover the four starting facts.** Name the expression, governed value or relation, its subject pattern, and the proposed use. If the value or relation is not available, stop and use its subject-recovery route; F.8 cannot establish it.
2. **Split mixed candidates.** If one expression covers more than one governed subject or use—for example, a kind, assignment, evidence use, policy, Method, or Work—make separate naming decisions.
3. **State the naming locality.** Carry the naming `U.ReferenceScheme` by value and state the local-sense claim. Cite a `SchemeSenseCell`, an obtaining `LocalSenseBasisRelation`, or a selected bounded-model-use Structure only when the naming use needs that object.
4. **Apply F.14 and try a local phrase.** If ordinary local wording supports the use, choose `localPhraseOnly` and stop.
5. **Try an existing designation.** Reuse it only when the value, kind, scope, occurrence identity, local sense, and proposed use match.
6. **Try an alias.** Use `aliasOnly` when the governed meaning is unchanged and lineage can expose the wording variation. An alias may not change kind, scope, occurrence identity, use, or authority.
7. **Try the subject's existing name.** Use the name supplied for the governed subject. A.2 and C.3 govern a local system-role kind and F.5 governs its designation; use F.18 only for a durable settlement and F.4 only for a separately needed `SystemRoleKindDescription`. A.2.1 continues to govern any assignment. For precise performed Work, A.13 first recovers each exact actual performer and A.15.1 independently admits the occurrence; F.6 follows only when the naming case or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment.
8. **Try one admitted F.17 row.** Reuse only the row's declared `AdmissibleUse`. Local-sense reuse does not imply cross-local sameness; a row and equal spelling create no F.9 Bridge.
9. **Open only the next naming object that pays for itself.** A stable local address may justify a cell; an enduring naming settlement may justify a NameCard; a public/Core/durable/cross-local need may justify an F.17 row. None implies the next object.
10. **Introduce a policy identifier only for a recovered policy specification.** A local identifier can stop with that specification and its scope. If the mint history is cited, replayed, normative, cross-local, or accountable, recover its decision or choice occurrence through the subject pattern; otherwise return `missing-governor` for that stronger history claim. Keep any C.11 result, decision-making Work, result episteme, and record separate.
11. **Stop before naming an unsettled U-kind proposal.** Select `blockOrLowerUse`. If the governed object is still unclear, use E.24.CD; otherwise send the recovered proposal episteme or source construct to E.24.UK. F.8 does not test or admit the candidate. After E.24.UK returns a stable `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject` disposition, re-enter F.8 only if the admitted or reused kind, local kind, or recovered non-kind object needs a designation.
12. **Block or lower.** If no disposition is justified, keep the expression local, quote it as source wording, or lower the claim.

#### F.8:4.3 - Role Expression Boundary

A role expression is not enough to choose the object. For a system-role naming case, keep these four objects distinct:

| Symbol | Object |
| --- | --- |
| `L` | The candidate or selected designation, interpreted under the effective naming ReferenceScheme. |
| `K` | The local system-role kind recovered through A.2 and C.3, with its work-facing contribution distinction and `KindSignature`. |
| `D` | An optional F.4 `SystemRoleKindDescription` episteme whose EntityOfConcern is `K`. |
| `A` | An optional A.2.1 assignment occurrence in which an admitted system is assigned under `K`. |

Under the effective naming scheme, `L` designates `K`. Needing `L` does not create or require `D`; `D` may receive its own designation when a separate description is justified. Naming either object creates no `A`. The naming ReferenceScheme interprets the expression; it neither defines the kind nor assigns a system.

After A.2 and C.3 have recovered `K`, apply the naming ladder. Keep a one-off expression local when that is enough, and reuse an existing designation when it fits. If the kind needs a durable designation, select `openDurableNamingSettlement`, use F.5 to name `K`, and use F.18 for the durable settlement. Use `nameSystemRoleKindDescription` and F.4 only when the governed object is a separately justified description episteme `D`.

| Source expression | Recovered case | F.8 result |
| --- | --- | --- |
| `ReviewerRole` in a review method | A recovered review-system-role kind needs a durable designation; that naming need requires no description episteme | `openDurableNamingSettlement`; A.2 and C.3 govern the kind, F.5 its designation, and F.18 the durable settlement; use F.4 only for a separately needed description |
| `Alice as reviewer` | A system is assigned to a local system-role kind for an interval | Not a name decision until `A.2.1` recovers the `U.SystemRoleAssignment` occurrence |
| `review happened` | Dated performed Work | Use `A.15.1`; open naming only if a Work-kind designation is needed |
| `EvidenceRole` | An episteme used as evidence | Use the evidence-use pattern; only then consider a name for the governed relation |
| `AccessRole` | Permission or policy grouping | Use access, policy, status, or deontic pattern; do not mint a local system-role kind by suffix |
| `ProviderRole` in a signature | Relation position | Use `A.6.5` SlotSpec discipline; name a slot only if needed |
| `RoleEnactment` in source prose | Source wording around a `U.SystemRoleAssignment` plus a Work occurrence | Recover the exact actual performer through A.13 and let A.15.1 independently admit the Work; use F.6 only when the naming case expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment, and do not mint `U.RoleEnactment` |

#### F.8:4.4 - F.17 Row-Scope Consumption

F.8 consumes one named F.17 row and its declared use; it neither constitutes the row nor defines Bridge strength. F.17 keeps the row episteme, governed value, designations, cell, basis relation, any F.9 Bridge, edition relation, and publication package distinct. F.8 asks only whether `AdmissibleUse` covers the proposed naming use.

| Declared row use | F.8 admissible naming use | Other claims return to |
| --- | --- | --- |
| Naming-only | Shared prose label, glossary text, teaching label | The direct subject pattern for any stronger claim—for example equivalence, assignment, performed Work, structure, or measurement. |
| System-role-kind designation naming | A designation may cite the row as a comparison aid after the local kind is recovered | The direct result for kind admission, cross-local identity, classification, or assignment. |
| System-role-kind-description naming | A label for a separately justified `SystemRoleKindDescription` may cite the row as a comparison aid | The direct result for kind identity, cross-local identity, or assignment; the description keeps its own subject. |
| Measurement naming | Shared measurement label where units and procedure constraints remain visible | The measurement pattern for any claim of procedure interchange. |
| Type-structure naming | Name for an admitted structural relation under the row's invariants | `E.24.UK` for U-kind admission. |

If the row does not admit the proposed use, lower the name's use or repair the F.17 row and any needed F.9 relation. Attractive wording supplies neither a stronger use nor cross-local sameness.

#### F.8:4.5 - Accountable Decision Branch

Open this branch only when a receiving claim needs to cite, replay, or assign accountability to the mint-or-reuse decision occurrence itself. First recover that occurrence through the decision or choice pattern that admits it. The ordinary naming result remains valid without this branch.

Keep these objects distinct in the accountable branch:

- the governed value or relation and its subject pattern;
- the candidate expression, selected designation, and any alias;
- the effective naming `U.ReferenceScheme`, local-sense claim, optional `SchemeSenseCell`, and any obtaining two-participant `LocalSenseBasisRelation`;
- the decision or choice occurrence and the pattern that admits it;
- any C.2.1 decision-result episteme and the record or carrier that designates it;
- any F.18 NameCard, F.17 row, policy specification, policy identifier, publication occurrence, form, or carrier; and
- a selected bounded-model-use Structure only when its organization changes interpretation for this naming use.

When a result episteme is needed, use the full projection below:

```text
MintReuseDecisionResultEpisteme:
  DecisionResultEpistemeId:
  EntityOfConcernRef: [decision or choice occurrence already admitted by its direct pattern]
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
  LocalSenseCellRef?: [only when a current SchemeSenseCell is needed]
  LocalSenseBasisRelationRef?: [only when the cell-to-basis-episteme relation obtains]
  SelectedModelUseStructureRef?: [only when a selected Structure changes this use]
  ReuseCandidateRefs?:
  SelectedDisposition:
  ResultingNamingRefs?: [only objects current after the disposition]
  GroundedNonUseBoundary?: [only when admitted by `F.19`'s grounded-contribution test]
  ReopenCondition:
```

The block describes the result episteme. `EntityOfConcernRef` resolves to the decision or choice occurrence admitted through `DecisionGovernorLocator`; the predicate, participants, applicability, and identity basis establish that occurrence. `GovernedValueSubjectPatternLocator` identifies the pattern for the value being named. For this use, the result is complete when the governed subject, proposed naming use, selected disposition, resulting naming refs when any, and reopen condition are recoverable; `GroundedNonUseBoundary` is optional. A C.11 `ChoiceResult` and dated decision-making Work keep their direct identities and relations. If the occurrence and its governor cannot be recovered, return the A.6.RCD `missing-governor` result. If no result episteme is needed, state the ordinary result and stop.

### F.8:5 - Invariants

1. **Four facts, one use.** Every disposition names the expression, governed value or relation, its subject pattern, and one proposed use. Split an expression that covers more than one governed subject or use.
2. **Lightest sufficient result.** Try the ordinary reuse ladder before creating a cell, NameCard, row, or policy identifier. An unsettled U-kind proposal stops before naming.
3. **Reuse preserves meaning.** Reuse or aliasing changes no kind, scope, occurrence identity, local-sense claim, admitted use, authority, or lineage. Shared spelling under another scheme establishes neither sameness nor an F.9 Bridge.
4. **Kind, description, assignment, and Work stay distinct.** A designation may name a recovered local system-role kind `K` without creating the optional F.4 description `D`. Neither name classifies a candidate, creates an A.2.1 assignment `A`, or demonstrates Work. Other governed uses remain with their subject patterns.
5. **Rows stay within admitted use.** Reusing an F.17 row supplies only its `AdmissibleUse` and no equivalence.
6. **Ordinary and accountable decisions stay distinct.** Ordinary F.8 use needs no decision occurrence or result episteme. The §4.5 branch opens only after the decision or choice pattern admits the occurrence; otherwise it returns `missing-governor`.
7. **Naming objects imply none of one another.** A designation, cell, basis relation, NameCard, row, identifier, publication occurrence, form, or carrier is created only for its receiving use. A selected Structure appears only when its organization changes interpretation of this naming use.
8. **Admission precedes naming.** Before E.24.UK returns a stable disposition, F.8 can only block or lower the proposed naming use. Afterward it may name only the admitted, reused, local, or recovered non-kind object identified by that result.
9. **Policy identifiers remain references.** Every identifier resolves a policy specification. Its mint occurrence and history are required only for the stronger uses stated in §8.1 and remain distinct from any C.11 result, decision-making Work, result episteme, or record.
10. **Labels grant no authority.** A source title, suffix, row, record, or identifier creates no governed subject, obtaining relation, permission, evidence, equivalence, or publication authority.

### F.8:6 - Reasoning Checks

Use these as reading checks, not as a required notation or record.

| Situation | Decision |
| --- | --- |
| The expression is present but the governed value or relation is not known. | Stop F.8. Use E.10 for phrase repair or the subject-recovery route for the object. |
| The expression, governed value or relation, subject pattern, and proposed use are present. | Choose the lightest disposition for that value and use. The naming decision neither establishes the value nor makes a relation obtain. |
| A local phrase or existing designation is sufficient. | Stay local or reuse it; create no cell, NameCard, row, or identifier. |
| An alias is proposed. | Preserve the governed kind, scope, occurrence identity, admitted use, and lineage to the selected designation. |
| The same spelling appears under another ReferenceScheme or local-sense claim. | Infer neither sameness nor an F.9 Bridge. Use a Bridge only when its predicate obtains between the relevant F.17 cells. |
| `L` is proposed for a local system-role kind `K`. | A.2 and C.3 govern `K`; F.5 governs `L`; F.18 opens only for a durable settlement. F.4 is used only for a separately needed description `D`, while A.2.1 governs any assignment `A`. For precise performed Work, A.13 first recovers the exact actual performer and A.15.1 independently admits the Work; F.6 is added only when this naming case or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. |
| A role-like expression is actually about another governed use—for example, evidence, status, policy, source, publication, or a relation position. | Recover that subject through its pattern before selecting a durable designation. |
| An F.17 row is proposed for reuse. | Reuse it only for its `AdmissibleUse`; the row supplies neither equivalence nor a wider use. |
| A receiving claim needs the decision occurrence itself. | Use §4.5. Recover the decision or choice pattern, predicate, participants, applicability, and identity basis. If no such governor is available, return `missing-governor`; keep any C.11 result and decision-making Work separate. |
| An expression is offered as a new U-kind before E.24.UK has settled admission. | Return `blockOrLowerUse`. Use E.24.CD if the governed object is unclear and send any surviving U-kind proposal to E.24.UK. Re-enter F.8 only for the object identified by the stable result. |

### F.8:7 - Archetypal Grounding - worked cases

#### F.8:7.1 - `ReviewerRole` Expression vs Review Report

The source label `PatternReview_2026` is not a context object. Classify the actual claim before using it:

- `ReviewWork-82` can be one dated `U.Work` occurrence under `A.15.1`;
- `ReviewPlan-2026-v3` can be a separately constituted plan episteme or edition under its subject pattern;
- `PatternReviewReferenceScheme-2026` can be an effective by-value `U.ReferenceScheme` for interpreting review terminology; and
- "used while deciding the label for the 2026 review method" can be claim content describing the decision-use setting without minting any context entity.

If the recovered `ReviewerSystemRole` kind needs a durable local designation, F.8 returns `openDurableNamingSettlement`: A.2 and C.3 keep governing the kind, F.5 governs its designation, and F.18 supplies the settlement. The recovered kind is the governed subject; F.4 enters only for a separately needed description, A.2.1 for an assignment, and A.15.1 for performed review Work.

The expression "review report has reviewer role" is a different case. `ReviewReport-82` is an episteme. An evidence, source, or publication relation may later use it for an adequacy claim about a reviewed pattern; the report is not a `U.System`, is not classified by the review-system-role kind, and cannot enter its assignment relation. Its title establishes neither evidence use nor publication authority.

#### F.8:7.2 - Actor Across BPMN and PROV

A manager wants one word, "actor", for a BPMN participant and a PROV agent in a diagram. First recover the two local senses under their ReferenceSchemes. If an obtaining F.9 Bridge relates the named cells and an F.17 row admits naming-only use, F.8 returns `reuseAdmittedTermRow` for prose and diagram labels only. This supports no governed-value identity, substitution, system-role assignment, or Work.

If the project later needs a local system-role kind under one scheme, it first recovers the kind through A.2 and C.3. F.5 then governs any new designation, with F.18 only for durable reuse; F.4 is added only if a separate description episteme is needed.

#### F.8:7.3 - Access Role

An access-control source says `ApproverRole`. Under its naming ReferenceScheme, the expression may designate a permission grouping or policy relation. First recover the access, policy, status, or deontic claim and predicate. Only if A.2 and C.3 recover a local approval-system-role kind does F.8 consider a name for that kind. F.5 governs its designation, F.18 applies only for durability, and F.4 remains optional for a separately needed description.

Otherwise any needed durable designation belongs to the access, policy, status, or gate pattern. The `Role` suffix, a source card, or a selected model-use Structure creates no local system-role kind or assignment.

#### F.8:7.4 - Policy Identifier

A gate profile proposes `Aut-Guard-2026`. F.8 treats this as a policy-identifier question only after the policy specification is recovered. Ordinary reuse resolves the identifier and specification. Recover the mint decision or choice occurrence only when reuse relies on that history for citation, replay, accountability, supersession, or another named relation. If a new introduction makes that stronger claim without an occurrence basis, return `missing-governor`. Any C.11 result, decision-making Work, result episteme, or record stays separate.

The identifier is not the specification, local system-role kind, Method, gate result, evidence value, permission, or source authority. It is a reference used by the pattern that defines or constrains the governed policy claim.

#### F.8:7.5 - New U-kind Candidate

A team proposes `U.InfluenceEdge` because many documents use "influence". At F.8 entry there is no recovered governed value with a stable admission disposition, so F.8 returns `blockOrLowerUse` and stops naming. If the expression still hides whether the subject is an existing relation or claim—for example, a causal, evidence, Method, or Bridge relation—or a characteristic, structural name, publication form, local frame, or another object, E.24.CD recovers that object or the unresolved proposal. A recovered governed object returns to its subject pattern; a surviving U-kind proposal goes to E.24.UK for `root`, `same-individual-dependent`, `identity-dependent`, `reuse`, `local-kind`, or `reject`. Only after that result is stable may F.8 reopen for a name of the admitted or reused kind, bounded local kind, or recovered non-kind object. F.8 creates neither the proposal object nor a public spelling and admits no kind.

#### F.8:7.6 - Readable Disposition and Explicit Stops

The `ReviewerRole` case closes with one readable result. The recovered kind is a local `U.Kind` for `U.System` candidates, distinguished by its stable review contribution and tested by its `KindSignature`; any assignment remains separate. The result is:

> Under `PatternReviewReferenceScheme-2026`, use `ReviewerRole` as the Plain designation of `ReviewerSystemRole` for local review-method prose. Select `openDurableNamingSettlement`: A.2 and C.3 govern the kind, F.5 governs its designation, and F.18 supplies the durable settlement. Reopen when the naming use or audience changes enough that this local settlement no longer supports it.

That sentence is the F.8 result. It needs no decision occurrence or result episteme. If a later claim must cite, replay, or assign accountability to the decision, use §4.5. No naming-decision governor is available in this case, so that branch returns `missing-governor` rather than inventing `ReviewerSystemRoleNamingDecision-2026-07-31`. C.11 applies only to a genuine local choice among available options. For any precise decision-making Work, A.13 first recovers the exact actual performer and A.15.1 independently admits the dated Work; F.6 follows only when the later claim expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment.

`EvidenceRole` stops earlier and does not enter F.8. The known subject is `ReviewReport-82 : U.Episteme`, proposed for evidence use concerning an adequacy claim. Still missing are the target claim and polarity, the evidence-use relation and relation kind, the provenance and any assurance or reliance use and validity window, and one subject pattern that defines the relation. Apply that pattern and keep the wording local until those facts are recovered. `PatternReviewReferenceScheme-2026` may interpret the source wording, but the review label creates no evidence relation, system-role kind, description, assignment, authority, or publication. No `SchemeSenseCell`, `LocalSenseBasisRelation`, or selected Structure is needed merely to record this stop.

Re-enter F.8 only after one governed relation, its kind, its subject pattern, and the proposed naming use are available. If the target claim, polarity, provenance, assurance or reliance use, or validity window changes, reopen the subject claim rather than the name.

### F.8:8.0 - Bias-Annotation

F.8 counters two shortcuts: a familiar word is treated as proof that a stronger name is needed, or a record is treated as the subject or decision it describes. Recover the four starting facts, choose the lightest disposition, and add a Structure, decision result, NameCard, row, or publication object only when its own receiving use requires it.

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
`PolicyIdentifier` is the selected designator. `PolicySpecificationRef` resolves to the separate policy-definition episteme and pins an edition or equivalent digest when needed. A local non-accountable introduction can stop there with explicit local scope. The conditional mint-occurrence fields are required when the use cites, replays, makes normative, reuses across the local boundary, or assigns accountability to the mint history; together they resolve one admitted decision or choice occurrence and the pattern, predicate, actual participants, applicability, and identity rule that establish it. If that stronger use is requested and those facts are absent, return `missing-governor` for it rather than inventing an occurrence. A C.11 `ChoiceResult` and any dated decision-making Work remain separate. `MintDecisionResultEpistemeRef`, when current, resolves to a C.2.1 episteme or accepted record describing the occurrence; the record does not perform the decision.

For FPF normative policy identifiers, the durable result episteme is usually an accepted `E.9` decision record, but only after the decision or choice pattern has admitted the occurrence that record describes. A local non-exported and non-accountable identifier needs only its separately recoverable specification and explicit scope; it need not create a decision or result episteme. In every branch, the policy specification, identifier, any decision or choice occurrence, any C.11 result, any decision-making Work, and any record remain distinct.

Rules:

1. **No silent policy-identifier introduction.** Every new identifier resolves the separate `PolicySpecificationRef` and states its scope. A local non-accountable introduction stops there. A cited, replayed, normative, cross-local, or accountable mint history additionally resolves the decision or choice occurrence plus the pattern, predicate, participants, applicability, and identity rule that establish it; without that basis, return `missing-governor` for the stronger branch and do not claim it.
2. **Reuse is reference use.** Reusing an existing identifier resolves the same identifier and policy specification. Resolve the original mint occurrence only when the current reuse consumes or asserts that history; it does not restate policy semantics, turn a record into the occurrence, or silently create another decision.
3. **Gate checkability.** A gate, crossing, Bridge, assurance, or publication claim that depends on a policy identifier includes `PolicyIdentifierReference` or an equivalent resolvable structure admitted by its subject pattern.
4. **Policy authority stays with the subject pattern.** F.8 selects introduction or reuse of the identifier; it does not decide whether the policy permits Work, passes a gate, makes a relation obtain, or provides evidence.
5. **The identifier grants nothing by itself.** Name, namespace, suffix, source prestige, specification publication, or decision record grants no permission, status, equivalence, or authority beyond the policy claim defined by its subject pattern.

### F.8:8 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-F8-01` | The expression, governed value or relation, subject pattern, and proposed use are named before the disposition. |
| `CC-F8-02` | An expression that covers several governed subjects or uses is split; for example, a kind, assignment, evidence use, policy, Method, or Work is not handled as one naming case. |
| `CC-F8-03` | The naming ReferenceScheme and local-sense claim are stated. A cell, basis relation, or selected Structure appears only when the naming use needs that object. |
| `CC-F8-04` | Local phrase, existing designation, alias, subject-pattern name, and admitted F.17 row were tried before a stronger naming object. |
| `CC-F8-05` | Reuse preserves kind, scope, occurrence identity, local-sense claim, admitted use, authority, and lineage. |
| `CC-F8-06` | A system-role-kind designation follows A.2 and C.3 recovery of the kind and does not require an F.4 description. If the description is separately needed, its label remains distinct from the kind designation. |
| `CC-F8-07` | Classification and assignment remain under C.3 and A.2.1. Any precise performed Work begins with the exact actual performer recovered through A.13 and independent A.15.1 admission; F.6 appears only for an expressly consumed precise assignment-bound attribution through the same obtaining A.13 assignment. None is inferred from a name. |
| `CC-F8-08` | Any other governed subject—for example, a status, evidence use, access value, policy, publication use, or relation position—returns to its subject pattern before naming. |
| `CC-F8-09` | F.17 row reuse stays within `AdmissibleUse`; spelling or local-sense reuse implies neither an F.9 Bridge nor equivalence. |
| `CC-F8-10` | Ordinary use creates no decision object. The accountable branch resolves the decision or choice occurrence through the pattern that admits it or returns `missing-governor`, while any C.11 result, Work, result episteme, record, and naming object stays separate. |
| `CC-F8-11` | A locality label such as `PatternReview_2026` is interpreted as the Work, plan, claim content, ReferenceScheme, or other object actually present; the label creates none of them. |
| `CC-F8-12` | An unsettled U-kind proposal receives only `blockOrLowerUse` and the needed E.24.CD or E.24.UK route. Naming reopens only for the object identified by a stable admission result. |
| `CC-F8-13` | A policy identifier resolves its specification and scope. When its mint history is cited, replayed, normative, cross-local, or accountable, the occurrence basis required by §8.1 is also recoverable; otherwise that stronger claim returns `missing-governor`. |
| `CC-F8-14` | The result states the governed subject, selected disposition, admitted naming use, and smallest change that reopens the decision. Any non-use boundary passes `F.19`'s grounded-contribution test. |

### F.8:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Suffix minting | A word ending in `Role`, `Status`, `Graph`, `Map`, or `Record` becomes ontology. | Recover the governed value or relation, subject pattern, and proposed use first. |
| Evidence-role revival | `EvidenceRole` becomes a system-role-kind name family. | Recover the evidence-use relation; name it only through its subject pattern. |
| Status-system-role fusion | `ReadyReviewerRole` or `ApprovedRole` names a local system-role kind plus state. | Separate the system-role kind from the assignment-state or status-use relation. |
| Row overuse | A public naming row justifies equivalence, system-role assignment, or structural inference. | Lower use to the F.17 `AdmissibleUse` or repair the row and any needed Bridge. |
| Alias with payload | An alias changes kind, scope, occurrence identity, use, or authority. | Treat it as a different decision; use `F.5`, `F.13`, and `F.18`. |
| Source prestige minting | A standard or framework term becomes the selected FPF name by prestige. | Keep it as source wording, evidence for a local sense, or an alias until the subject and naming use are recovered and a designation is selected. |
| Review label as context | `PatternReview_2026` is used as context, Work, system-role assignment, evidence, or authority. | Recover the dated Work, plan or edition, decision-use claim, or naming ReferenceScheme needed by the assertion. |
| Decision identifier or record as decision | An identifier or filled record is treated as the decision occurrence or as creating its result. | Recover the occurrence through the decision or choice pattern, predicate, actual participants, applicability, and identity rule that establish it. If none is available, return `missing-governor`; constitute a separate C.2.1 result episteme only when needed. |
| Naming-object cascade | One expression automatically gets a cell, NameCard, row, identifier, and publication. | Apply F.14 at every gate and create only the next object whose receiving use pays for it. |
| U-kind comfort minting | A new U-kind is proposed because existing names feel awkward, and F.8 is asked to name or admit it. | Return `blockOrLowerUse`; recover the object through E.24.CD when needed, let E.24.UK settle admission, and reopen naming only for the object named by that stable result. |
| Policy identifier as magic word | An identifier is used without a separately resolvable specification, or its mint history is called accountable, cited, replayable, normative, or reusable across the local boundary without an occurrence basis. | Supply the specification for every identifier. For the stronger history claim, supply its direct occurrence basis or return `missing-governor`; a merely local non-accountable identifier does not manufacture one. |

### F.8:10 - Consequences

Good consequences:

- vocabulary grows only when a receiving use needs a stronger name;
- role-like, source, and record-like expressions return to their governed subjects before naming;
- aliases and F.17 rows retain their admitted meaning and scope;
- F.5 and F.18 receive a recovered subject and a selected naming path; and
- accountable decisions and policy identifiers remain inspectable without making their records act.

Costs:

- authors must recover the subject, pattern, use, scheme, and local sense before naming;
- mixed expressions need separate decisions, and some attractive words stay local or remain aliases;
- durable or public use may require its own NameCard, Bridge, row, reliance, decision result, or publication object; and
- a proposed U-kind receives no F.8 name before E.24.UK settles admission.

**Refresh by meaning, not by neighbour edition.**

- If F.14, F.5, F.17, or F.18 changes the lightest-sufficient naming ladder, row-entry threshold, `AdmissibleUse`, or escalation to a stronger naming object, revisit §§0 and 4.1–4.4, case 7.2, checks 03–09, and the compact corpus entry.
- If A.2, C.3, F.4, A.2.1, A.13, A.15.1, or F.6 changes how a local system-role kind is recovered, how `L`, `K`, `D`, and `A` relate, how an exact actual performer and Work are admitted, or when precise assignment-bound attribution enters, revisit the corresponding target rows, step 7, §4.3, cases 7.1, 7.3, and 7.6, invariant 4, and checks 06–08.
- If A.6.RCD, C.11, C.2.1, or A.15.1 changes how a decision or choice occurrence, result, result episteme, decision-making Work, or missing governor is established, revisit §4.5, the accountable stop in 7.6, invariant 6, and check 10.
- If E.24.CD, E.24.UK, A.8, or A.11 changes object recovery, admission dispositions, or the admission-before-naming order, revisit the entry and ordinary conditions for use, stopping, or returning, the pre-admission target and step 11, case 7.5, invariant 8, and check 12.
- If the policy subject pattern, E.9, A.6.RCD, C.11, or C.2.1 changes the policy specification–identifier distinction or the support required for mint history, revisit the policy target, step 10, case 7.4, §8.1, invariant 9, and checks 10 and 13.
- If a source used in §12 changes a distinction that F.8 adopted, or a better current source preserves the needed precision and readability at lower use cost, revisit that source row and only the F.8 loci named by it.

A new edition number, publication status, link, harmless wording repair, or added example does not reopen F.8 when these meanings stay unchanged. A changed disposition, governed subject, kind or relation, admitted use, ordering dependency, or better solution reopens only the dependent loci named above.

### F.8:11 - Rationale

A naming mistake is often a subject or use mistake. Asking “what name should we use?” too early lets wording decide ontology, scope, or authority. F.8 therefore recovers the subject and proposed use before selecting a naming treatment.

F.8 is narrower than F.18. It decides whether the expression stays local, reuses something available, or opens one stronger naming path. F.18 runs a durable settlement, candidate comparison, NameCard, lineage, and any later public-row gate. F.8 creates neither the governed value nor the objects produced by the stronger path.

The system-role branch shows why the ordering matters. A designation `L`, local system-role kind `K`, optional F.4 description `D`, and any assignment `A` are different objects. The word *role* can also point to another governed subject. Recovering that subject first keeps naming from creating a false kind or assignment.

The accountable branch follows the same rule. A decision occurrence, C.2.1 result episteme about it, C.11 result, decision-making Work, and rendered record answer different questions. Section 4.5 opens only when a receiving claim needs that stronger traceability; ordinary F.8 use stops earlier.

### F.8:12 - SoTA-Echoing - Source-Use

**Qualification and selection rule.** These decisions are qualified on 2026-08-15 for the cited editions and the F.8 questions below. The set is deliberately small. ISO 704 and SKOS are current standards or durable lineage, not claimed as research frontiers. The gUFO–OBO row combines a current formal comparator with an operational ontology-maintenance practice. The Cedar row is a current research-and-practice comparator. A source belongs here because it changes an F.8 disposition or boundary, not because it is official, popular, or easy to find.

| Source, status, and question | Decision for F.8 | What F.8 uses and rejects | Affected loci and smallest source-driven revisit |
| --- | --- | --- | --- |
| [ISO 704:2022](https://www.iso.org/standard/79077.html), edition 4 — current international terminology standard. Question: how should an expression, its designation use, the concept or other subject, and any definition stay distinguishable? Its Pareto position here is the latest general standard that directly treats links among objects, concepts, definitions, and designations across fields; it is not presented as a research frontier. | **Adopt the subject-before-designation order; adapt its terminology distinctions to FPF values, relations, and subject patterns.** | Keep expression, designation, governed subject, and any description separate. Reject using terminology work to admit an ontic kind, and reject a full terminology entry when a local phrase is sufficient. | §§0, 4.1–4.3, and checks 01–08. Revisit only if a later ISO 704 edition or a better general terminology account changes the designation–subject–definition distinction or preserves it with lower practitioner cost. |
| W3C [SKOS Reference](https://www.w3.org/TR/skos-reference/), 2009 Recommendation — current standard and representation lineage for lightweight labels and concept schemes. Question: what can preferred and alternative labels, scheme placement, and mapping links support without importing class identity? Its Pareto position is the small, explicit label model and its stated non-entailments, not its age. | **Adapt preferred/alternative-label and scheme discipline as a reuse stress test.** | Preserve the selected-designation/alias split and local-sense scope. Reject RDF or SKOS as required FPF representation; reject same spelling, `skos:exactMatch`, or scheme membership as FPF identity, F.9 Bridge, kind admission, or wider F.17 use; do not require a cell merely to keep wording local. | §§4.1–4.4, 7.2, and checks 03–09. Revisit if a normative SKOS successor or a better lightweight label model changes these label or mapping boundaries. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint, read with the current [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) and its [term-stability rule](https://obofoundry.org/principles/fp-019-term-stability.html) — accepted synthesis for the new-kind question. gUFO supplies a current typology-of-types and relational-aspect comparator; OBO supplies operational scope, reuse, identifier, relation-reuse, and stable-referent pressure. Together they cover formal category discipline and maintained-vocabulary cost better than either alone. | **Adapt the category/label separation and reuse pressure.** | A spelling or source class does not establish an FPF kind. Test existing values, relations, scopes, and stable meanings before proposing another kind. Reject gUFO's hierarchy, OWL commitments, OBO's biomedical scope and IRI rules, and any external source as FPF admission authority. | The pre-admission stop in §§0 and 4.1–4.2, case 7.5, invariants 3 and 8, and checks 05 and 12. Revisit if gUFO's type distinctions or the cited OBO scope, reuse, or stability principles change materially, or a better account reduces admission burden without losing these distinctions. |
| Cutler et al., [Cedar](https://arxiv.org/abs/2403.04651), 2024, read with current Cedar 4 and [Verified Permissions policy-name and policy-id practice](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/terminology.html), checked 2026-08-15 — current research-and-operation comparator for policy references. Question: how should policy content, a name or identifier, request evaluation, and enforcement stay separate? Its Pareto position is a modern readable and formally analysed policy language with active operational use, not vendor popularity. | **Adapt only the separation of policy reference, policy content, evaluation, and effect.** | Keep a policy identifier resolvable to its specification and keep any decision occurrence, result, Work, or enforcement separate. Reject Cedar and AWS types, stores, API identifiers, and authorization semantics as FPF ontology; reject any inference that an identifier grants permission or makes a policy claim true. | The policy target and step 10, case 7.4, §8.1, and checks 10 and 13. Revisit if the cited line changes the separation among policy name or identifier, policy content, and decision, or a more general current source preserves it with less domain-specific machinery. |

**Internal FPF basis, not external SoTA.**

- F.14, F.5, F.17, and F.18 supply the local-phrase, designation, alias, row-use, and durable-naming ladder.
- A.2, C.3, and F.4 keep designation `L`, local system-role kind `K`, and optional description `D` distinct; A.2.1 governs assignment `A`. For precise performed Work, A.13 recovers each exact actual performer and A.15.1 independently admits the dated occurrence; F.6 is a later separate relation only when precise assignment-bound attribution is expressly consumed.
- E.24.CD, E.24.UK, A.8, and A.11 recover an unclear object and decide kind admission before F.8 names the result.
- A.6.RCD, C.11, C.2.1, and E.9 govern any accountable decision occurrence, separate result, result episteme, and policy-history record.
- F.1–F.3 and F.9 govern local-sense discovery and an obtaining Bridge; A.1.1 and A.22 govern any selected bounded-model-use Structure. F.8 cites those objects only when the naming use needs them.

**Source-use boundary.** External sources can supply candidate expressions, a comparison pressure, or a narrow representation test. They do not select the F.8 disposition, establish the governed subject, make a relation obtain, admit a kind, or grant authority. Those results remain with the named FPF pattern and the recovered facts.

### F.8:13 - Relations

**Builds on.** `A.7`, `E.24.UK`, `A.8`, `A.11`, `E.10`, `E.10.ARCH`, `F.1`, `F.2`, `F.3`, `F.5`, `F.9`, `F.14`, `F.17`, and `F.18`.

**Coordinates with.** `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.6.5`, `A.6.RCD`, `A.15`, `A.15.1`, `C.11`, `F.4`, `F.6`, `F.10`, `F.13`, `F.15`, `C.2.1`, `C.3`, `E.9`, `E.24.CD`, and `E.24.PUB`, plus the subject pattern for any other governed value.

**Constrains.**

- `F.5` names only after F.8 has selected the naming case.
- Use `F.4` only for a separately needed `SystemRoleKindDescription`; naming the local kind itself does not require that episteme.
- `F.9` governs an obtaining Bridge between F.17 cells; `F.17` governs admitted public-row use before F.8 reuses it.
- `F.18` expands durable naming only after lighter dispositions have failed.
- `F.14` supplies the anti-explosion stop before every stronger F.8 disposition.
- `F.15` may check the resulting distinctions; it neither chooses the disposition nor creates a naming object.

**Does not replace.** The subject pattern for any governed value or relation. For example, it does not replace the rules for a system-role kind, assignment, performed Work, decision occurrence, status, evidence use, policy, relation slot, selected Structure, or description episteme.

### F.8:14 - Didactic Memory

Name the subject and use before judging the word. Try the light naming ladder and stop at the first sufficient result. An unsettled U-kind goes to E.24.UK before naming; an accountable decision opens §4.5 only when the decision occurrence itself must be used. A name, card, row, identifier, publication, or record creates neither the subject nor any relation or authority it mentions.

### F.8:End

