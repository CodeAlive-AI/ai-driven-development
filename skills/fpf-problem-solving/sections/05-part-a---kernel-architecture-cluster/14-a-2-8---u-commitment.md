## A.2.8 - `U.Commitment` (Deontic Commitment Relation)

> **Status:** Stable
> **Type:** Definitional ontic pattern

### A.2.8:0 - Use This When

Use this pattern when you need to decide whether one actual system or party is obliged, required as a duty, recommended as a duty, or prohibited from doing something in a stated scope and time.

Start with the ordinary question: **does this actual bearer have this duty now?** Name the bearer and the duty content. Then find the policy or prescription, the rule by which it creates an individual duty, and the actual event or other basis that the rule requires. The first useful result is one obtaining `U.Commitment`, a demonstrated non-obtaining result, `unknown`, or `missing-governor[individual commitment institution]`.

**What goes wrong if missed.** A policy sentence, system-role kind, assignment, publication, ticket, interface description, or complete-looking record is treated as the duty itself. A named office is called responsible without a responsibility predicate. Evidence is made constitutive merely because the duty is auditable.

**What this buys.** The actual duty bearer, content, modality, scope, validity, constitutive rule, and instituting basis remain inspectable. Generic prescriptions stay usable without inventing an individual relation, while evidence and records can support a claim without becoming the commitment.

**Not this pattern when.** Use `A.2.3` for promise content, `A.2.9` for the communicative Work that may institute a duty, and `A.2.8.PER` for permission or authorization. For responsibility, use an admitted domain responsibility predicate; if none exists, return its exact `A.6.RCD` missing governor. Use a gate pattern for admissibility and `A.15.1` for performed Work. If no current subject pattern defines how the proposed individual duty is instituted, return `missing-governor[individual commitment institution]` instead of completing a record by convention.

### A.2.8:0.1 - Kind Settlement and Wording Boundary

`U.Commitment` is an enduring individual deontic relation. It covers obligation, recommendation-as-duty, and prohibition. It is not a policy episteme, normative prescription, system-role kind, assignment, speech act, record, gate, permission, responsibility relation, performed Work, evidence item, or compliance result.

The words *bind* and *binding* already denote technical bindings in FPF; they do not name this relation. Source phrases such as *binding promise*, *must*, *shall*, *guarantees*, *is responsible for*, or *legally required* are recognition cues. Recover their exact claim before selecting `U.Commitment`; the words alone institute nothing.

### A.2.8:1 - Problem Frame

FPF needs both generic normative content and actual individual duties:

- a policy can say what would apply to systems of a stated kind;
- one constitutive rule can say when that content creates an individual duty;
- actual world-side facts can satisfy or fail that rule;
- one assertion or record can describe the resulting relation for reliance or audit.

Those are different objects. If a generic policy and an individual relation share one record-shaped ontology, an assignment row or published clause can appear to create a duty by being filled in. If the actual bearer is replaced by a system-role kind or assignment, the model cannot say who is obliged. If responsibility is inferred from the duty, another independent relation disappears.

### A.2.8:2 - Problem

How can a practitioner state an individual deontic relation so that:

1. the actual duty bearer is explicit;
2. the duty referents, modality, scope, and validity are exact;
3. one applicable constitutive rule and its required actual basis make institution testable;
4. a generic prescription remains generic until the rule is satisfied;
5. relation identity survives compatible description changes but not a changed bearer, content, rule, or interrupted validity;
6. records and evidence support the claim without constituting the relation; and
7. responsibility, permission, authority, assignment, Work, and compliance remain separately governed?

### A.2.8:3 - Forces

| Force | Tension |
| --- | --- |
| Direct bearer vs generic policy | Policy often speaks about a system-role kind, while an individual commitment needs an actual system or party. |
| Minimal use vs truthful institution | Routine prose should stay short, but a positive world-side relation cannot omit the rule and actual instituting basis that make it obtain. |
| Stable identity vs changing records | A correction or compatible policy edition need not create another duty, while a changed bearer, content, constitutive rule, or interrupted validity does. |
| Auditability vs constitution | Evidence is needed for reliance, but evidence and publication do not create the duty. |
| Local meaning vs cross-context reuse | Modality and policy interpretation are local; a similar label or Bridge does not transfer an individual relation. |
| Duty vs neighboring governance | Commitment, responsibility, permission, authority, assignment, Work, gate result, and compliance can co-occur without becoming one object. |

### A.2.8:4 - Solution

#### A.2.8:4.1 - Direct Participants and Predicate Parameters

One `U.Commitment` occurrence has:

- exactly one actual duty bearer, expressed by either `dutyBearerSystemRef : U.EntityRef constrained to an admitted U.System` or a separately governed local `dutyBearerPartyRef : PartyRef`;
- a non-empty exact set of duty referents stating the action, avoidance, outcome, promise content, claim, or other governed object to which the duty applies; and
- optional actual counterparties or beneficiaries when the duty is owed to someone.

Exactly one duty-bearer branch is filled. A system-role kind, classification judgment, assignment occurrence, organizational-position label, publication, policy, or claim record is not the bearer.

The normalized modality is a by-value predicate parameter:

```text
DeonticModalityToken ::= MUST | MUST_NOT | SHOULD | SHOULD_NOT
```

`SHALL` and `REQUIRED` map to `MUST`; `SHALL NOT` and `PROHIBITED` map to `MUST_NOT`; `RECOMMENDED` maps to `SHOULD`; and `NOT RECOMMENDED` maps to `SHOULD_NOT` only after the source claim has been recovered as a duty. `MAY` and `OPTIONAL` do not normalize into `U.Commitment`; route their current meaning to A.2.8.PER, an admissibility predicate, or ordinary prose.

Scope and validity delimit applicability. Duty referents are cited by exact identifiers when they already exist. Useful referent kinds include a claim ID, `U.PromiseContent`, an action or outcome specification, an admitted Method, or an already identified Work occurrence when the duty concerns that occurrence. A MethodDescription is cited only when the duty depends on claims in that exact episteme edition; description is not mandatory indirection to the Method.

The current normative policy or prescription, its constitutive rule, the actual instituting basis, provenance, and adjudication evidence are grounds or qualifiers. They are not extra duty bearers and do not become deontic participants by appearing in a record.

#### A.2.8:4.2 - When the Relation Obtains

For proposed occurrence `C`, the direct predicate `C : U.Commitment` obtains only when all of the following hold:

1. the actual duty bearer and any actual counterparties are admitted, and the duty referents are identified;
2. one identified normative policy or prescription is current and applies to those participants, referents, scope, and time;
3. that policy contains or cites one exact constitutive rule for an individual commitment rather than only generic content about a system-role kind;
4. the rule's required instituting basis and world-side facts obtain;
5. modality, scope, validity window, and every rule-required condition are satisfied; and
6. no valid revocation, defeat, expiry, or supersession has ended the relation.

For the current A.2.9 path, the instituting basis is an actual `U.SpeechAct` Work occurrence recognized by the current policy, with the actual performer and exact covering system-role assignment independently established. Another basis is usable only when a subject pattern admits it and gives its occurrence rule.

If the corpus lacks the constitutive rule or the required instituting-relation predicate, return `missing-governor[individual commitment institution]`. If an applicable rule is false, the proposed commitment does not obtain. If a required evidence dependency is unavailable, reliance on the assertion is `unknown`; do not invent the relation or infer its negation.

#### A.2.8:4.3 - Occurrence Identity and Continuity

One occurrence is identified by:

- the actual duty bearer;
- exact duty referents and counterparties;
- normalized modality and scope;
- constitutive policy and rule;
- the actual instituting basis, only when that rule makes the basis identity-bearing; and
- one maximal continuous validity interval.

The actual instituting basis is always required for obtaining. It is part of occurrence identity only when the exact constitutive rule says that reinstitution identifies another duty. A compatible policy edition, new record, or later instituting act preserves the occurrence only through an explicit continuity decision showing that every identity-bearing fact and the rule's deontic effect continue. A changed bearer, modality, referent set, constitutive rule, identity-bearing basis, or interrupted validity yields another occurrence. The commitment ID and its describing claim do not decide sameness.

When a rule makes a duty end with a system-role assignment, an assignment boundary ends that commitment. When the rule makes the duty persist for the same actual system across a replacement assignment, state that continuity explicitly. A different actual bearer always requires another commitment occurrence.

#### A.2.8:4.4 - Generic Prescriptions and Assignment-Mediated Rules

A generic prescription states what one exact policy or other normative episteme requires; it does not create an individual duty bearer or commitment occurrence. A claim that one actual System or separately governed party has that duty instead cites one separately obtaining A.2.8 `U.Commitment`.

For example, a policy can concern `ProviderSystemRole` or another exact local system-role kind. Its `systemRoleKindRef : U.KindRef` can appear in the rule's antecedent, but the policy episteme is not an individual `U.Commitment`.

An exact `systemRoleAssignmentRef : U.RelationRef constrained to U.SystemRoleAssignment` can show that an actual system satisfies one applicability condition for a time. The assignment is still not the duty bearer or the commitment relation. The only valid direction is:

```text
current policy or prescription
+ exact constitutive rule
+ actual admitted system
+ obtaining exact system-role assignment or other rule-required facts
+ actual instituting basis required by that rule
-> one separately identified U.Commitment whose duty bearer is that actual system
```

Classification or assignment alone never completes the implication. The rule states whether the duty starts, continues, and ends with the assignment.

#### A.2.8:4.5 - Assertion, Record, and Adjudication

An assertion or record about a commitment is a separately identified claim-bearing episteme. A compact reliance record can expose:

```text
CommitmentAssertion:
  entityOfConcernRef: U.RelationRef constrained to one exact U.Commitment occurrence
  dutyBearerSystemRef? | dutyBearerPartyRef?: the actual bearer stated by the relation
  dutyReferentRefs: non-empty exact set
  counterpartyRefs?: actual counterparties or beneficiaries
  modality: normalized by-value token
  scopeRef:
  validityWindowRef:
  constitutivePolicyRef: exact current normative episteme edition
  constitutiveRuleRef: exact rule claim
  institutingBasisRef: exact actual basis required by that rule
  evidenceClaimRefs?: exact support used for reliance or adjudication
  carrierRefs?: carriers used as evidence or source
  assertionStatus: affirmed | denied | unresolved
```

The record is not the relation. `evidenceClaimRefs` and carriers support reliance; they are not participants or instituting facts unless the identified constitutive rule makes one such fact current and the pattern for that subject supplies its test. If adjudication is intended, cite the exact evidence claims, criteria, and carriers. If no adjudication is claimed, do not invent an audit apparatus.

When a later use must compare incompatible commitments, keep the commitments unchanged and carry the needed conflict inputs in one local claim:

```text
CommitmentConflictInputClaim:
  selectionUseRef: exact conflict or choice question
  commitmentRows: non-empty set of
    commitmentRef: U.RelationRef constrained to one exact U.Commitment occurrence
    institutingBasisRef: exact actual basis required by its constitutive rule
    issuingSystemRef | issuingPartyRef: exactly one actual issuer recoverable from that basis
    authorityRelationRef?: U.RelationRef constrained by the direct authority predicate used by selectionUseRef
  selectingRuleRef?: exact priority or choice rule required by selectionUseRef
  unresolvedInputRefs?: exact missing-information or missing-governor results
```

This claim creates no issuer, authority, priority, or resolution and adds none of them to commitment identity by default. Each authority relation must already obtain under its own predicate, and each selecting rule must be current and applicable to this selection use under the pattern that defines it. If this selection use requires an authority relation or selecting rule and that input is unavailable or no current pattern defines it, put its exact unresolved result in `unresolvedInputRefs`, such as `missing-governor[commitment conflict authority relation]` or `missing-governor[commitment conflict selecting rule]`. An optional field means that the input is not required for this use; it never licenses dropping a required input. For an interlevel ethical conflict, use D.3 to map the conflict and D.4 for mediation or decision use. When an explicit choice among already available options is current, C.11 supplies the `ChoiceRule` and `ChoiceResult`. Otherwise apply the direct pattern for the claimed conflict result; if none exists, return `missing-governor[commitment conflict resolution]`.

Evidence used only to measure or verify the duty belongs to the support for the assertion. An evidence-producing or evidence-retaining duty instead names that production or retention content among its duty referents.

#### A.2.8:4.6 - Direct Neighboring Relations

| Current question | Direct result | Commitment does not establish |
| --- | --- | --- |
| What does a generic policy prescribe? | one normative claim episteme and its applicable rule content | an individual duty |
| Which System holds a local system-role assignment? | one A.2.1 assignment occurrence and its declared species | a duty or responsibility |
| Did a communicative act occur? | one A.2.9 `U.SpeechAct` Work occurrence | its institutional effect without the constitutive rule |
| Is the bearer responsible? | one admitted domain responsibility predicate and occurrence; otherwise the exact missing governor | responsibility from duty, assignment, position, or “owner” wording |
| Is an action permitted or authorized? | the exact A.2.8.PER grant, exercise, non-prohibition, non-violation, or conflict result | permission from commitment or assignment |
| Did access occur? | an exact domain access relation; otherwise `missing-governor` | access from permission, duty, or assignment |
| Did the bearer perform Work? | one dated `U.Work` plus F.6 attribution when under assignment | Work from the duty alone |
| Was the duty satisfied or violated? | a separately governed evaluation or compliance result using actual Work and evidence | compliance from publication or record completeness |
| What resulted? | the separately identified result and its direct result relation, or A.15.PROD for production and inception | a generic result relation from duty or Work |

`U.Commitment` establishes only its own deontic relation. The common corpus has no universal responsibility predicate. `VP.AllocationResponsibility` can help a reader recognize the concern but cannot make a responsibility relation obtain.

#### A.2.8:4.7 - Boundary Claim Use

An A.6.B D-quadrant claim about an obtaining individual obligation, recommendation-as-duty, or prohibition cites the exact `U.Commitment` occurrence. It does not become that occurrence. A D-claim about generic policy content remains a claim about that content until the individual predicate above is satisfied.

Strong or weak permission, exercise, non-violation, and permission-conflict claims cite their exact A.2.8.PER result and do not acquire a `U.Commitment` payload. Gates remain A-claims, laws and definitions remain L-claims, and Work and evidence effects remain E-claims.

### A.2.8:5 - Archetypal Grounding

#### A.2.8:5.1 - Incident Response

Current `IncidentResponsePolicy-2026` says that systems assigned to `ProviderSystemRole` are subject to a four-hour incident-response prescription. That policy and its kind reference remain generic content.

`OpsTeamProviderAssignment-2026` is an assignment occurrence with admitted System `OpsTeam` as holder; its species is declared under `U.SystemRoleAssignment`. If the policy contains the holder-application rule, speech act `SA-Issue-IncidentDuty-2026 : U.SpeechAct` is the policy-recognized instituting Work, and the predicate is satisfied, then `IncidentResponseCommitment-2026 : U.Commitment` obtains with `OpsTeam` as duty bearer. Its modality is `MUST`; its referents include `SVC-SLO-RESP-4H` and the Sev-1 applicability claim; its scope is `IncidentManagement`; and its validity window is the interval established by the rule. The assignment and `ProviderSystemRole` are not the bearer.

The commitment assertion may cite `E-SLO-RESP-1`, incident tickets, timestamps, and the selected clock source for adjudication. Those values make reliance testable; they do not institute the duty.

If `OpsTeamProviderAssignment-2026` ends and `RecoveryTeamProviderAssignment-2026` begins, the assignment edge does not transfer one commitment. When the rule ties duty continuity to the assignment, the OpsTeam commitment ends and a RecoveryTeam commitment begins only after its own required basis and facts obtain. If the rule instead preserves the duty for the same system across a replacement assignment, the continuity decision says so. A different bearer always means another occurrence. Likewise, a second policy-recognized act reissuing the same uninterrupted duty identifies another commitment only when the constitutive rule makes that instituting basis identity-bearing; otherwise the new act is a new ground or record for the continuing occurrence.

A policy-recognized speech act can also institute `ShutdownNoticeCommitment-7` directly for admitted system `PlantController-7`. No system-role kind or assignment is manufactured merely to carry that duty.

`IncidentResponseCommitment-2026` can obtain while no incident-ownership responsibility relation exists. Conversely, an admitted `MaintenanceActionResponsibilityRelation@Plant` can obtain while no `U.Commitment` obtains. Both can obtain for the same system and interval only as separately identified relations with separate predicates, participants, bases, and occurrence identities.

Without an applicable individualizing rule, required basis, or subject pattern, the outcome is `missing-governor[individual commitment institution]`. A speech act, assignment, policy publication, or D-claim supplies only the facts it actually establishes.

#### A.2.8:5.2 - Protocol Rule

A protocol description says: “Participants MUST follow the state machine; invalid traces are rejected; traces are retained for audit.” Recover separate claims:

- L-claims define the state machine and its safety or progress properties;
- A-claims define which runtime traces are admissible;
- one generic normative claim states the participant prescription;
- one actual `U.Commitment` is asserted only for an admitted bearer after an applicable constitutive rule and its required basis obtain;
- the duty referents cite the state-machine, admissibility, and trace-retention content by exact identifiers; and
- evidence claims and trace carriers support later adjudication.

The protocol episteme does not bear the duty. A `ParticipantImplementerSystemRole` reference in the policy does not identify an actual bearer. A visible `MUST` does not complete institution.

### A.2.8:6 - Invariants and Reasoning Primitives

1. Every positive `U.Commitment` has one actual system or party as duty bearer.
2. A system-role kind or assignment can be a rule ground but never the duty bearer.
3. Generic normative content, individual relation, and describing assertion remain separate.
4. The direct predicate includes an applicable constitutive rule and the actual basis that rule requires.
5. Modality, scope, validity, and referents are explicit.
6. Missing evidence makes reliance unresolved; it does not invent or negate the relation.
7. Assignment turnover does not transfer a duty automatically.
8. Responsibility, permission, authority, access, Work, result, and compliance remain separately governed.
9. Compatible record correction does not decide world-side continuity.
10. A Bridge or similar wording in another context creates no local commitment.

```text
applicable current policy and exact constitutive rule
  and admitted actual bearer and referents
  and required instituting basis and facts obtain
  and modality, scope, validity, and continuation conditions hold
  and no defeat, revocation, expiry, or supersession applies
  -> one U.Commitment occurrence obtains.
```

```text
policy mentions one system-role kind
  or one system-role assignment obtains
  -> no individual U.Commitment follows without the exact rule, bearer, and basis.
```

### A.2.8:7 - Bias Annotation

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Record-first bias | A filled form is treated as an obtaining relation. | Test the direct predicate; keep the record as an assertion. |
| Office-label bias | A role, office, or assignment becomes the bearer. | Recover the actual system or party and use the kind or assignment only as a rule ground. |
| Legal-form bias | A maximal legal-policy schema is imposed on every duty. | Keep the direct participants minimal and add grounds or assurance only when the current claim needs them. |
| Evidence-as-constitution | An audit trail is treated as what creates the duty. | Keep support and institution separate. |
| Responsibility overreach | Duty is read as ownership or accountability. | Apply the direct responsibility predicate or return its missing governor. |
| Keyword bias | `MUST`, `SHALL`, `MAY`, or `responsible` selects an ontology by spelling. | Recover the claim first, then select the exact relation or ordinary non-use. |

### A.2.8:8 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| `CC-A2.8-1` | Exactly one actual admitted system or separately governed party is the duty bearer. |
| `CC-A2.8-2` | Duty referents are non-empty and exact; existing claim or object identifiers are cited rather than paraphrased. |
| `CC-A2.8-3` | Modality, scope, and validity are explicit. |
| `CC-A2.8-4` | One current policy or prescription and its exact individualizing constitutive rule are identified. |
| `CC-A2.8-5` | The actual instituting basis required by that rule obtains under the pattern that defines that basis. |
| `CC-A2.8-6` | The occurrence identity and continuity decision distinguish changed bearers, content, rules, and interrupted intervals, and treat a changed instituting basis as identity-bearing exactly when the constitutive rule says so. |
| `CC-A2.8-7` | System-role kind, classification, assignment, policy, publication, assertion, and evidence are not commitment participants or duty bearers by form. |
| `CC-A2.8-8` | Responsibility, permission, authority, access, Work, result, and compliance are separately asserted or left unresolved. |
| `CC-A2.8-9` | A reliance or audit record names its exact `U.Commitment` EntityOfConcern and does not claim to create it. |
| `CC-A2.8-10` | Missing rules, governors, or information return the exact non-obtaining, `missing-governor`, or `unknown` result rather than a completed placeholder relation. |

### A.2.8:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| “The API shall…” as duty-bearer structure | An interface description is an episteme, not the actual bearer. | Identify the policy claim and actual system or party; test institution. |
| `CommitmentSubject ::= RoleRef | RoleAssignmentRef | PartyRef` | It merges a kind, relation occurrence, and actual bearer. | Use one actual bearer branch; keep kind and assignment in the rule's grounds. |
| Optional institution source | A published sentence appears sufficient to create the relation. | Require the applicable rule and its actual instituting basis. |
| Assignment-as-duty | Staffing becomes obligation. | Treat the assignment only as a rule fact and identify a separate commitment. |
| Duty-as-responsibility | One deontic relation silently creates ownership. | State the independent responsibility predicate or return `missing-governor`. |
| Gate-as-duty | Entry conditions become obligations. | Keep the A-claim and let an independently instituted commitment cite it when required. |
| Auditable rhetoric without support | “Guaranteed” cannot be adjudicated. | Cite exact evidence claims and carriers only when reliance or adjudication is current. |
| Silent mutation | Changed bearer or rule is hidden under one ID. | Apply occurrence identity and create another relation when identity-bearing facts change. |

### A.2.8:10 - Consequences

**Benefits**

- Generic policy content and actual duty no longer collapse.
- Actual bearers are directly recoverable.
- Modality, scope, referents, and validity remain lintable.
- Assignment and responsibility independence is explicit.
- Assurance can be added proportionately without becoming universal process overhead.

**Costs and mitigations**

- A positive individual-duty claim needs more than a policy sentence. This is the necessary cost of claiming a world-side relation; generic policy content remains cheap to state.
- Domains with another instituting basis need the pattern that defines that basis. Until then, `missing-governor` is an honest usable result.
- Conflict resolution remains outside this pattern. Preserve each current commitment plus the exact source, independently obtaining authority relation, and selecting rule required by the named conflict or choice use; apply D.3/D.4 for an interlevel ethical conflict, C.11 for an explicit choice among available options, or return `missing-governor[commitment conflict resolution]` when no direct result rule exists.

### A.2.8:11 - Rationale

An individual duty is not whatever a normative-looking record names. Requiring an actual bearer, constitutive rule, and actual basis prevents description, assignment, and publication from becoming causes by form. Keeping assertion and evidence separate preserves both ontology and auditability. Keeping responsibility separate avoids replacing one ambiguous word with an equally ambiguous omnibus governance object.

### A.2.8:12 - SoTA-Echoing

> **Informative.** These comparisons motivate the distinctions; they do not govern local claims.

- **BCP 14 (RFC 2119 and RFC 8174).** Controlled normative keywords support explicit modality, but keywords do not identify an individual bearer or institute a duty. **Adapt.**
- **W3C ODRL 2.2.** Duties, permissions, assignees, actions, constraints, and policy provenance motivate explicit participants and qualifiers. FPF keeps individual commitment, permission, policy episteme, and evidence separate. **Adapt.**
- **Institutional and constitutive-rule approaches.** Their distinction between rule content, institutional conditions, and resulting relations supports the required constitutive rule and actual basis. **Adopt the separation.**
- **Policy-as-code practice.** Admission predicates and policy evaluation should not be confused with individual obligation or performed Work. **Adapt.**
- **Trace-based compliance and supply-chain attestations.** Evidence and carriers can support adjudication while remaining distinct from relation obtaining. **Adopt.**

### A.2.8:13 - Relations

- **Builds on:** A.2 and C.3 for system-role kinds and classification; A.2.1 for declared system-role-assignment species and their obtaining occurrences; A.2.6 for scope and temporal qualification; A.2.9 for communicative Work; A.6.RCD for missing governors; A.7 for episteme and world separation.
- **Coordinates with:** A.2.3 for promise content; A.2.8.PER for permission; F.6 and A.15.1 for Work attribution; A.6.B and A.6.C for claim classification and boundary wording; A.10 for evidence and source reliance.
- **Does not define:** a universal responsibility, authority, access, compliance, or result relation; a system-role kind; a system-role assignment; a policy language; or a legal-party model.

### A.2.8:End

