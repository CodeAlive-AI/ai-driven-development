## A.2.7 - SystemRoleKindRelationStructure - Relations among System-Role Kinds

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.7:0 - Use This When

**Plain designation.** Say “structure of relations among system-role kinds” for `SystemRoleKindRelationStructure`.

Use this pattern when several exact context-local system-role kinds are already admitted, and a later admission, allocation, or interpretation check needs one of these results:

- an assignment to one system-role kind may satisfy a condition written for another kind;
- two system-role kinds are incompatible under one exact holder, Work, and time rule;
- several independently obtaining assignments are required together under one allocation rule; or
- one system-role kind narrows another, and the practitioner must decide whether that narrowing is monotonic `U.SubkindOf` or a different residual relation.

Typical working moments include these:

- a pressure-test MethodDescription names `HydraulicsTechnicianSystemRole`, while the proposed holder is assigned to `SeniorHydraulicsTechnicianSystemRole`;
- the same system must not hold author and approver assignments for the same hazard-analysis Work during overlapping windows;
- a surgical procedure needs surgeon, anesthetist, and scrub-practitioner assignments together, with three distinct holders;
- `RoboticsEngineerSystemRole` may be a subkind of `EngineerSystemRole`, but neither a nested label nor one assignment can establish that order.

**First useful result.** Write the readable direct relation or `U.SubkindOf` claim needed by the receiving use. Recover its exact predicate. Stop there unless another claim needs one relation occurrence as an identifiable object or needs several obtaining relations selected into one structure.

**Primary EntityOfConcern.** For one direct question, the EntityOfConcern is the exact relation occurrence or exact `C.3.1 U.SubkindOf` occurrence. When several such occurrences must be selected together, it is one `SystemRoleKindRelationStructure`: a dependent `U.Structure` selected from exact local system-role-kind constituents and exact obtaining relations under the exact applied constraints and one named selection-use frame.

The structure contains neither holder systems nor system-role-assignment occurrences. A graph, taxonomy table, policy file, or organization chart may describe it but does not become the structure or any selected relation by form.

**Primary working reader.** The first reader is an engineer, Method designer, safety practitioner, clinical team designer, or manager deciding which relations a later check may rely on. The reader should be able to recover the exact system-role kinds, relation rule, applicability, occurrence identity, and assignment inputs without treating a name hierarchy or policy row as the relation itself.

**What goes wrong if missed.** A job-title order is used as admission authority. An independence rule omits the holder, Work, or overlap condition. A bundle name hides whether one or several systems must hold the assignments. A semantic restriction is called `U.SubkindOf` although a known broader classification can be false. A scheme or taxonomy edition is then inserted as a participant of every relation even when it changes no meaning.

**What this buys.** Admission substitution, incompatibility, joint allocation, monotonic kind order, and residual qualification remain different claims with different truth and identity laws. Actual holders remain systems, actual assignments remain direct species of `U.SystemRoleAssignment`, and the system performing a receiving check remains visible.

**Not this pattern when.** Use `A.2` and `C.3` to admit and classify exact local system-role kinds. Use `A.2.1` for assignments and their holders, `A.2.5` for `SystemRoleAssignmentStatePredicate` and `SystemRoleAssignmentStateRelation`, `A.2.2` for capability, A.3 patterns for Methods, and A.15 patterns for planned or performed Work. Use `F.9` and `A.6.9` for an actual cross-scheme Bridge, then a separate bounded-use assertion and reliance decision. Use `C.29` when a graph, matrix, algebra, embedding, or table is the object under evaluation.

### A.2.7:1 - Problem Frame

A system applying a maintenance-admission Method may admit a current assignment to `SeniorHydraulicsTechnicianSystemRole` where the MethodDescription names `HydraulicsTechnicianSystemRole`. A system applying a safety Method may reject overlapping author and approver assignments. A clinical MethodDescription may state a joint condition over three assignments. A classification review may ask whether every true `RoboticsEngineerSystemRole` judgment implies a true `EngineerSystemRole` judgment.

These uses all concern exact system-role kinds, but they do not concern the same relation. The assignment occurrences used by a receiving check are also not participants of the kind relation. They remain independently obtaining A.2.1 relations whose holder, exact assigned kind, extent, and any real domain participant are recovered under their direct species.

A system-role-kind description or taxonomy episteme may state a relation claim, and its reference scheme may help interpret that claim. The world-side relation obtains under its direct predicate. When a `KindSignature`, scheme, Bridge, or other edition changes the relation rule, include that edition in the predicate's semantic basis; otherwise keep it as interpretation material outside occurrence identity.

`SystemRoleKindRelationStructure` is the selected organization among exact kinds and exact obtaining relations. For any checking Work, identify the acting system and dated Work under their direct patterns; the selected structure supplies only the organization used by that check.

### A.2.7:2 - Problem

The practitioner needs a reusable relation for a later engineering check, but familiar shorthand collapses four different questions:

1. Can an assignment to one system-role kind satisfy an admission condition written for another?
2. Are assignments to two system-role kinds incompatible under a stated holder, Work, and time rule?
3. Must assignments to a finite set of system-role kinds be present together, and how may holders be allocated?
4. Does one kind monotonically narrow another, or does the restriction require a different relation?

Calling every answer a hierarchy loses the predicate. Calling the answer a role part introduces mereology without constructive assembly or a meta-holon transition. Calling the answer a policy, chart, taxonomy, or scheme confuses a relation with an episteme or convention that describes or interprets it. The receiving check then cannot show which premise it used or what change would invalidate the outcome.

### A.2.7:3 - Forces

| Force | Tension |
|---|---|
| Reuse vs local meaning | Several contexts may use similar labels while their exact local kinds and relation rules differ. |
| Direct relation realism vs socially constituted rules | A row does not create predicate truth, while some specialized social relations genuinely depend on an accepted act or decision named by their direct rule. |
| Readable claim vs occurrence identity | Ordinary use should stop at a direct sentence, while a later assertion may need one exact relation occurrence. |
| Kind relation vs holder assignment | A relation among kinds may guide a check; each holder assignment must obtain under its own direct rule. |
| Monotonic order vs residual restriction | True subkind order must preserve every defined classification judgment; many useful semantic restrictions do not. |
| Joint admission vs compound kind | Several assignments may be required together without creating a combined system-role kind. |
| Stable predicate vs changing semantic basis | A compatible edition may preserve meaning, but a changed rule or identity-bearing basis creates another predicate and occurrence. |
| Structure vs representation | A graph or matrix can make organization inspectable without becoming that organization. |

### A.2.7:4 - Solution

Start with the one relation family needed by the receiving use. Use exact local system-role kinds as its participants and put the rule, applicability, and only meaning-changing semantic-basis editions in its by-value predicate. Current assignments, assignment-state relations, capability, evidence, and the receiving window remain inputs to the later check.

Build a structure only when several exact relation occurrences must be selected together:

```text
SystemRoleKindRelationStructure : U.Structure
  systemRoleKindSubstrate:
    exact finite set of independently identified context-local system-role kinds, by value
  selectedSystemRoleKindRelationOccurrenceRefs:
    finite set of references to exact obtaining relation occurrences
  appliedConstraintClaimRefs:
    exact constraint claims applied in this selection; an empty set is stated explicitly
  namedSelectionUseFrame:
    question:
    admissibleAction:
    stopOrNonAdmissibleOverread:
      exact stop or return condition; also named stopOrReturnCondition
  groundedNonAdmissibleOverread?:
    optional explanation outside the identity basis
```

The structure specializes A.22's four-part identity: the exact system-role-kind constituents, the exact selected obtaining relation occurrences, the exact constraint claims applied, and one named selection-use frame stating the question, admissible action, and stop or return condition. `stopOrReturnCondition` and `stopOrNonAdmissibleOverread` name that same condition, not two independently filled values. A `groundedNonAdmissibleOverread?` is optional explanatory material under F.19:4's plausible-reader test and is not an identity discriminator. A changed rendering, identifier, selecting Work, publication, table, or graph changes no structure while all four values remain unchanged. Replacing a constituent, selected relation occurrence, applied constraint, or use frame identifies another structure. Without a required constraint or named frame, the material is still an arrangement or description rather than an admitted `SystemRoleKindRelationStructure`.

#### A.2.7:4.1 - Direct Relation and Declaration Discipline

Substitution, incompatibility, bundle, and residual qualification are four families of direct relations under `U.Relation`. This pattern gives their different laws. Each context declares its exact direct species with exact local ValueKinds in its `RelationSignature`; A.2.7 does not introduce a permissive root signature or four additional universal Tech kinds over every possible system-role kind.

Apply the relation-object order from `A.6.REL`:

1. recover the exact participant kinds and by-value predicate;
2. establish from current facts or accepted constituting history whether the predicate obtains;
3. individuate one occurrence only when a receiving use needs occurrence identity;
4. assign a stable reference only when another episteme needs it; and
5. keep assertion, evidence, reliance, and representation separate from the occurrence.

Each direct species declares one SlotSpec for every actual system-role-kind participant and one by-value predicate SlotSpec. A context-local kind domain gives each system-role-kind SlotSpec its exact ValueKind. A system-role-taxonomy episteme, effective reference scheme, `KindSignature`, Bridge, or selected model-use structure is not another generic participant. Include its exact edition in predicate identity only when the rule depends on that edition.

Establish predicate truth under the context-local rule. If a specialized direct relation obtains only through an accepted appointment, policy decision, installation, or other constituting act, the context-local predicate must name that act and its acceptance condition.

Logical form supplies argument order, set semantics, and relation laws. Use the direct rules to establish participant kinds and predicate truth, and to recover occurrence identity when the receiving use needs it. Use the relevant patterns when the claim also concerns a Method, Work, transformation, agency, constructive assembly, or holon admission.

If current facts concern one actual bounded change, make that change a separate subject and use `A.3.4` to recover one `U.Transformation` at the resolution and boundary needed by the use. Name its affected entity, boundary, precondition, postcondition, and obtaining relations. Keep it distinct from the relation among system-role kinds, an assertion about that relation, and the Work that checks it. `U.Transformation` by itself supplies neither a transformation-composition predicate nor holonhood.

#### A.2.7:4.2 - Admission Substitution

Use the admission-substitution family when one assignment may satisfy a receiving condition written for another system-role kind. The relation is directional.

For an exact context-local species, declare:

```text
<exact context-local admission-substitution relation species> : U.Relation
RelationSignature:
  CandidateSystemRoleKindSlot: exact candidate-kind domain, ByValue
  RequiredSystemRoleKindSlot: exact required-kind domain, ByValue
  AdmissionSubstitutionPredicateSlot:
    exact context-local admission-substitution predicate kind, ByValue
```

One predicate value is identified by the ordered candidate and required system-role kinds, the exact receiving-use rule, applicability, and only the semantic-basis editions that change that rule. Reversing the two kinds requires another predicate evaluation. A job-grade order, common word stem, or `U.SubkindOf` relation may be evidence or another premise; none is the substitution relation by itself.

Current assignments and any required A.2.5 state occurrences are inputs to the receiving check. They are not participants of the relation among kinds. Establish classification, assignment, capability, authorization, gate outcomes, and Work under their direct patterns as the receiving use requires them.

#### A.2.7:4.3 - Incompatibility

Use the incompatibility family when assignments to two system-role kinds cannot be jointly admitted under one exact rule.

For an exact context-local species, declare:

```text
<exact context-local incompatibility relation species> : U.Relation
RelationSignature:
  IncompatibleSystemRoleKindSlot[1]: exact local kind domain, ByValue
  IncompatibleSystemRoleKindSlot[2]: exact local kind domain, ByValue
  IncompatibilityPredicateSlot:
    exact context-local incompatibility-predicate kind, ByValue
```

The predicate is identified by the unordered pair of kinds, the exact same-holder or different-holder rule, Work identity condition, temporal-overlap test, applicability, and only meaning-changing semantic-basis editions. The relation obeys the symmetry law:

```text
incompatible(k1, k2, p) = incompatible(k2, k1, p)
```

The exact assignments later evaluated are receiving inputs. A conflicting allocation is a case satisfying the incompatibility rule; it is not what creates the kind relation. A system applies the receiving Method and records the resulting admit, reject, defer, or unresolved outcome under the pattern for that decision.

#### A.2.7:4.4 - Monotonic Kind Order and Residual Qualification

When one exact system-role kind appears to narrow another, test `C.3.1 U.SubkindOf` first. Use that relation only when the paired classification judgments satisfy monotonicity under the exact aligned editions and effective-reference-scheme edition required by C.3.1:

```text
for every candidate x in the defined comparison domain:
  judgment(x, NarrowerSystemRoleKind) = true
  implies judgment(x, BroaderSystemRoleKind) = true
```

The proposed `U.SubkindOf` edge is never a premise for either membership judgment. Direct feature criteria must establish both judgments independently. A known narrower `true` with broader `false` refutes the relation. An unavailable broader dependency yields `unknown` and leaves the order unresolved.

When the restriction is useful but non-monotonic, use a separate residual relation rather than weakening `U.SubkindOf`:

```text
<exact context-local residual qualification relation species> : U.Relation
RelationSignature:
  QualifiedSystemRoleKindSlot: exact local qualified-kind domain, ByValue
  ReferenceSystemRoleKindSlot: exact local reference-kind domain, ByValue
  ResidualQualificationPredicateSlot:
    exact context-local residual-qualification-predicate kind, ByValue
```

The residual predicate names the exact restriction, applicability, orientation, and only meaning-changing semantic-basis editions. A receiving Method needing substitution must establish that separate directional relation.

#### A.2.7:4.5 - Joint-Admission Bundle

Use the bundle family when a receiving use needs assignments to a finite set of system-role kinds together and the holder-allocation rule matters.

For an exact context-local species, declare:

```text
<exact context-local bundle relation species> : U.Relation
RelationSignature:
  BundledSystemRoleKindSetSlot:
    exact order-insensitive finite set of local system-role kinds, ByValue
  JointAdmissionPredicateSlot:
    exact context-local joint-admission-predicate kind, ByValue
```

The predicate is identified by the exact order-insensitive set, joint-admission and holder-allocation rule, applicability, and only meaning-changing semantic-basis editions. It states whether one system may hold several assignments, distinct systems must hold specified assignments, some assignments may be shared, and how the receiving window is tested.

Exact current assignments and the receiving window remain inputs to the later check. The bundle specifies a joint condition over distinct system-role kinds. Use the applicable direct pattern when assignment, team, or Work identity is needed. A list of labels without a joint-admission and allocation rule is not a bundle relation.

#### A.2.7:4.6 - Occurrence Identity and Continuity

For substitution and residual qualification, one occurrence begins when fixed ordered kinds satisfy one fixed predicate. For incompatibility, the participant identity is the unordered pair. For a bundle, it is the order-insensitive finite set. In every case, the occurrence continues through the maximal uninterrupted interval during which the fixed predicate obtains for those fixed participants.

A compatible declaration, scheme, `KindSignature`, Bridge, or other semantic-basis edition preserves the predicate only through an explicit continuity decision showing that the rule, orientation or set semantics, applicability, system-role-kind identities, and meaning-bearing semantic basis remain unchanged. Otherwise another predicate and relation occurrence begin. Equal displayed labels establish no continuity.

An affirmative assertion or occurrence description may state the known `systemRoleKindRelationExtent` only after current facts or accepted constituting history satisfy the predicate and the identity rule recovers the occurrence. Closing an open extent refines the same occurrence when obtaining was uninterrupted. A demonstrated predicate-false gap ends it; later truth begins another. Missing evidence leaves reliance unresolved and does not demonstrate a truth gap.

`systemRoleKindRelationExtent` is content of an affirmative assertion or occurrence description, not a temporal SlotSpec. A target `declaredSystemRoleKindRelationEvaluationWindow` belongs to the receiving assertion or check and is not part of the direct relation signature or occurrence identity.

For `U.SubkindOf`, use C.3.1's own obtaining and identity law, including its exact effective-reference-scheme edition. Do not replace it with the generic A.2.7 interval rule.

`SystemRoleKindRelationStructure` identity follows all four A.22 discriminators: exact kind constituents, exact selected relation occurrences, exact applied constraint claims, and the named selection-use frame. A scheme change that changes a constituent, selected relation, applied constraint, or use frame changes the structure; selecting System, Method, Work, result episteme, and publication remain outside identity.

#### A.2.7:4.7 - Assertion and Receiving Check

A relied-on kind-relation claim is a C.2.1 assertion episteme, not the relation occurrence. Keep these moves in order:

1. name the exact direct relation family or `U.SubkindOf`, participant kinds, predicate, and applicability;
2. establish whether current facts or accepted constituting history satisfy that predicate;
3. when the receiver needs occurrence identity, apply the direct identity rule and recover the already obtaining occurrence;
4. only then let an affirmative assertion use that occurrence as its `EntityOfConcern` and state its known extent; and
5. add evidence, currentness, and reliance only when the receiving use needs them.

When no positive occurrence is recovered, a negative, candidate, counterfactual, or unsupported affirmative claim normally uses the exact admitted relation kind, or another independently identified entity, as its EntityOfConcern. Its ClaimGraph carries proposed fillings, predicate, polarity or modality, and meaning-bearing semantic basis. It carries no fabricated positive occurrence reference or actual extent.

Unresolved reliance preserves the assertion's stated polarity and leaves relation obtaining and occurrence identity unchanged. C.2.1 still identifies the assertion by its content, exact EntityOfConcern, and effective reference scheme.

Supported assertions serve as typed premises for another Method. A system performing a receiving check normally:

1. resolves the exact local system-role kinds and any current direct `U.SystemRoleAssignment` species or A.2.5 state occurrences needed by the rule;
2. tests the exact relation predicate without copying assignments or state occurrences into the kind-relation participant set;
3. individuates the relation only when the receiving use needs its identity;
4. records the appropriate assertion and its separate reliance posture;
5. evaluates capability, resource, interface, risk, evidence, currentness, assurance, or other conditions under their direct patterns; and
6. performs the checking Work by the selected Method and records the outcome defined for the next question's exact decision kind.

Current facts make a world-side relation obtain. Optional individuation recovers one occurrence. An episteme asserts it. Evidence supports reliance. A system performs the check.

#### A.2.7:4.8 - Recover Apparent Decomposition

When ordinary wording says *subrole*, *role part*, or *combined role*, start from the engineering question:

| Engineering question | Recovered object |
|---|---|
| May this assignment satisfy a condition written for another system-role kind? | directional admission-substitution relation |
| Does every true narrower classification imply the broader classification? | `C.3.1 U.SubkindOf` after independent paired judgments |
| Does one kind restrict another without monotonicity? | residual system-role-kind qualification relation |
| Must assignments to two kinds not overlap under an exact condition? | symmetric incompatibility relation |
| Must assignments to several kinds be present together under an allocation rule? | order-insensitive bundle relation |
| Which system is assigned, and for which interval? | exact direct species under `U.SystemRoleAssignment`; use A.2.1 to recover it |
| Does an assignment satisfy a Work-admitting state condition? | `SystemRoleAssignmentStateRelation`; use A.2.5 to recover it |
| Can the holder perform within an operating envelope? | capability and capability-fit relations under A.2.2 |
| Are ways of doing or Work occurrences composed? | Method composition under A.3 and B.1.5, or Work structure under A.15 |
| Did one actual bounded change occur? | one `U.Transformation` under A.3.4, with its affected entity, boundary, precondition, postcondition, and obtaining relations |

This recovery introduces no system-role mereology. Recover exact kinds, relations, assignments, predicates, Methods, and Work through the direct patterns above.

#### A.2.7:4.9 - Representation, Model-Use, and Cross-Scheme Boundaries

A graph, table, matrix, algebra, embedding, policy file, taxonomy, or organization chart may describe a `SystemRoleKindRelationStructure` or support a C.29 mathematical-lens use. It is not the selected structure or any selected relation occurrence by form. State what organization the representation preserves and loses before relying on it.

Reference an independently selected `BoundedModelUseStructure` only when interpretation depends on that model-use organization. Keep it with the receiving assertion or use unless one direct relation predicate truly depends on its exact edition; only then does that edition enter the predicate's semantic basis.

When a comparison, translation, or reuse crosses schemes, first recover the exact F.17 sense cells and obtaining F.9 Bridge. Then state a separate C.2.1 bounded-use assertion naming direction, correspondence rule, tolerated loss, polarity, use, and effective scheme. Ordinary reliance requires the current A.10 evidence-provenance relation and a passing disposition for that use. Use B.3 only when an actual named assurance claim is current; require its result for the same bounded assurance use. Establish any required authorization separately.

Apply the direct rule for each claim of bounded-use suitability, an A.2.7 relation, assignment, authorization, receiving-check outcome, or performed Work. A Bridge, profile, or card may provide information for that claim. A local relation that obtains keeps the participant set and identity declared here.

#### A.2.7:4.10 - Lightweight Path

Ordinary prose may state a readable relation and stop:

```text
For pump pressure-test Work, an assignment to SeniorHydraulicsTechnicianSystemRole
may satisfy the condition written for HydraulicsTechnicianSystemRole.
```

Add an exact direct-species `RelationSignature` when reusable participant typing matters. Individuate an occurrence only when another claim depends on its identity. Assign a stable reference only when another episteme needs it. Build a `SystemRoleKindRelationStructure` only when several selected relations must be used together and all four A.22 discriminators are recoverable. Completeness is not a reason to materialize every layer.

### A.2.7:5 - Worked Slices and Archetypal Grounding

#### A.2.7:5.1 - Manufacturing Admission Substitution

Plant A admits `SeniorHydraulicsTechnicianSystemRole` and `HydraulicsTechnicianSystemRole` as exact local kinds. During 2026H2, the pressure-test admission Method uses this rule: an assignment to the senior kind may satisfy the condition written for the technician kind only for `PumpPressureTestMethodFamily` and only while the candidate assignment satisfies A.2.5 predicate `PressureTestReady`.

The direct species uses the local `PlantMaintenanceSystemRoleKindDomain`:

```text
PlantPressureTestSystemRoleKindSubstitution :
  U.Relation
RelationSignature:
  CandidateSystemRoleKindSlot:
    PlantMaintenanceSystemRoleKindDomain, ByValue
  RequiredSystemRoleKindSlot:
    PlantMaintenanceSystemRoleKindDomain, ByValue
  AdmissionSubstitutionPredicateSlot:
    PlantPressureTestAdmissionSubstitutionPredicate, ByValue
```

The predicate names the ordered two kinds, receiving Method family, `PressureTestReady` rule, 2026H2 applicability, and the exact semantic basis whose edition changes either clause. `PlantMaintenanceRoles-2026` and `Plant-A-Maintenance-Scheme` may be cited in the assertion; they are not extra relation participants. If a later compatible edition preserves all identity-bearing clauses, an explicit continuity decision preserves the predicate. Otherwise another predicate and occurrence are required.

```text
PlantPressureTestSubstitutionAssertion:
  entityOfConcernRef: Plant-A-Pressure-Test-Substitution-2026H2
  ClaimGraph:
    directClaimFamilyRef:
      PlantPressureTestSystemRoleKindSubstitution
    participantDesignations:
      CandidateSystemRoleKindSlot:
        SeniorHydraulicsTechnicianSystemRole
      RequiredSystemRoleKindSlot:
        HydraulicsTechnicianSystemRole
      AdmissionSubstitutionPredicateSlot:
        PlantPressureTestAdmissionSubstitutionPredicate
    assertionPolarity: affirmative
    systemRoleKindRelationExtent: [2026-07-01, 2026-12-31]
```

The system performing admission checking resolves the candidate's exact A.2.1 assignment and its current `PressureTestReady` state occurrence. Those are inputs to the receiving rule, not substitution-relation participants. Capability is checked separately. A claim about performed pressure-test Work needs its own A.15 basis.

#### A.2.7:5.2 - Safety Separation of Duties

For one hazard-analysis Work item, the same system must not hold both author and approver assignments during overlapping windows. The direct species uses the exact `SafetyCaseSystemRoleKindDomain` and a predicate identified by the unordered pair `{HazardAnalysisAuthorSystemRole, HazardAnalysisApproverSystemRole}`, same-holder rule, same-Work rule, overlap test, applicability, and meaning-bearing semantic basis.

```text
HazardAnalysisAuthorApproverIncompatibility :
  U.Relation
RelationSignature:
  IncompatibleSystemRoleKindSlot[1]:
    SafetyCaseSystemRoleKindDomain, ByValue
  IncompatibleSystemRoleKindSlot[2]:
    SafetyCaseSystemRoleKindDomain, ByValue
  IncompatibilityPredicateSlot:
    HazardAnalysisSeparationPredicate, ByValue
```

The predicate has characterized these kinds continuously since 2026-01-01. A particular pair of assignments with the same holder and Work item during overlapping windows is a later case satisfying the rule; it does not create the kind relation.

```text
HazardAnalysisAuthorApproverIncompatibilityAssertion:
  entityOfConcernRef:
    HazardAnalysisAuthorApproverIncompatibility-2026
  ClaimGraph:
    directClaimFamilyRef:
      HazardAnalysisAuthorApproverIncompatibility
    participantDesignations:
      IncompatibleSystemRoleKindSlot[1]:
        HazardAnalysisAuthorSystemRole
      IncompatibleSystemRoleKindSlot[2]:
        HazardAnalysisApproverSystemRole
      IncompatibilityPredicateSlot:
        HazardAnalysisSeparationPredicate
    assertionPolarity: affirmative
    systemRoleKindRelationExtent: [2026-01-01, open]
```

A verifier system applies the work-admission Method to two exact assignment occurrences and the target Work item. The checking Work produces the receiving decision.

#### A.2.7:5.3 - Clinical Joint Admission

A surgical MethodDescription states a joint rule: assignments to `SurgeonSystemRole`, `AnesthetistSystemRole`, and `ScrubPractitionerSystemRole` must be held by three distinct systems throughout the procedure window selected by the receiving check.

```text
OperatingTheatreThreeSystemRoleBundle :
  U.Relation
RelationSignature:
  BundledSystemRoleKindSetSlot:
    OperatingTheatreSystemRoleKindDomain, ByValue
  JointAdmissionPredicateSlot:
    ThreeDistinctHoldersForProcedurePredicate, ByValue
```

The set is order-insensitive. The predicate names the three exact kinds, distinct-holder rule, full-window rule, procedure applicability, and meaning-bearing semantic basis. The taxonomy episteme and clinical reference scheme may help an assertion designate or interpret the kinds; they are not participants of the bundle relation.

```text
OperatingTheatreThreeSystemRoleBundleAssertion:
  entityOfConcernRef: OperatingTheatreThreeSystemRoleBundle-2026
  ClaimGraph:
    directClaimFamilyRef: OperatingTheatreThreeSystemRoleBundle
    participantDesignations:
      BundledSystemRoleKindSetSlot:
        {SurgeonSystemRole,
         AnesthetistSystemRole,
         ScrubPractitionerSystemRole}
      JointAdmissionPredicateSlot:
        ThreeDistinctHoldersForProcedurePredicate
    assertionPolarity: affirmative
    systemRoleKindRelationExtent: [2026-01-01, open]
```

For one planned procedure, the receiving check separately names its evaluation window and resolves three independently obtaining assignments. The bundle supplies the allocation rule; the three system-role kinds remain distinct even when the holders form one procedure team. Credentials, state, capability, gate decisions, and procedure Work remain separate.

#### A.2.7:5.4 - Robotics Kind Order and Independent Musician Assignment

The lab proposes:

```text
RoboticsEngineerSystemRole U.SubkindOf EngineerSystemRole
```

The proposal is not a premise for classifying Vasya or any other system. Under the exact aligned `KindSignature` editions and effective reference-scheme edition, direct robotics-engineering features are evaluated against both kinds. Only if every defined true `RoboticsEngineerSystemRole` judgment implies a true `EngineerSystemRole` judgment may C.3.1 establish the relation.

A known robotics-engineer `true` with engineer `false` refutes the relation. If a dependency required by the broader judgment is unavailable, the result is `unknown` and the order remains unresolved. A restriction concerning only one Method family, project phase, or allocation condition that fails monotonicity uses a residual qualification relation instead.

Vasya may separately hold assignments to `RoboticsEngineerSystemRole` and `MusicianSystemRole`. Those assignment identities and extents remain under A.2.1. Robot-engineering Work, music-performance Work, and teaching-robots-music Work remain A.15 occurrences. Establish capability and admission substitution separately when the receiving use needs them.

### A.2.7:6 - Conformance Checklist

| Check | Question |
|---|---|
| `CC-A2.7-01` | Is the current object one exact relation among system-role kinds, one `C.3.1 U.SubkindOf` occurrence, or one dependent `SystemRoleKindRelationStructure` whose exact kind constituents, selected obtaining relation occurrences, applied constraint claims, and named selection-use frame are all recoverable? |
| `CC-A2.7-02` | Are all participants exact context-local system-role kinds rather than systems, assignments, labels, taxonomy rows, or scheme values? |
| `CC-A2.7-03` | Does each direct context-local species declare exact SlotSpec ValueKinds and one by-value predicate? |
| `CC-A2.7-04` | Does the predicate state the actual receiving, incompatibility, allocation, or residual-restriction rule, applicability, and only meaning-changing semantic basis? |
| `CC-A2.7-05` | Are system-role-taxonomy and scheme epistemes absent as generic participants and included in predicate identity only when they change meaning? |
| `CC-A2.7-06` | Is relation obtaining distinct from assertion, evidence, identifier, publication, representation, and receiving-check outcome? |
| `CC-A2.7-07` | Is substitution directional, incompatibility symmetric, and bundle membership order-insensitive? |
| `CC-A2.7-08` | Does incompatibility name the same- or different-holder rule, Work identity condition, overlap test, and applicability? |
| `CC-A2.7-09` | Does a bundle state its joint-admission and holder-allocation rule without creating a compound kind? |
| `CC-A2.7-10` | Is `U.SubkindOf` used only after independent paired judgments establish monotonicity under the exact C.3.1 basis? |
| `CC-A2.7-11` | Does a non-monotonic restriction remain a separately predicated residual relation? |
| `CC-A2.7-12` | When occurrence identity matters, does it use fixed kind participants, fixed predicate, and maximal continuous truth interval rather than a row, graph key, or temporal SlotSpec; and is any target evaluation window kept in the receiving assertion or check? |
| `CC-A2.7-13` | Does an explicit continuity decision cover a compatible edition before predicate and occurrence identity are preserved? |
| `CC-A2.7-14` | Are current assignments and A.2.5 state occurrences inputs to the receiving check rather than relation participants? |
| `CC-A2.7-15` | Does the system performing the check, its selected Method, checking Work, and exact outcome kind remain visible? |
| `CC-A2.7-16` | Are graphs, tables, matrices, algebras, policies, taxonomies, and publications kept as descriptions, lenses, or epistemes? |
| `CC-A2.7-17` | Does a negative, candidate, counterfactual, or unsupported claim avoid fabricating a positive occurrence reference or actual extent? |
| `CC-A2.7-18` | Does cross-scheme use keep the Bridge, bounded-use assertion, reliance, local relation, assignment, authorization, and Work distinct? |

### A.2.7:7 - Failure Modes and Repairs

| Failure | Why it fails | Repair |
|---|---|---|
| Job-title or taxonomy order used for admission | The order states neither the receiving rule nor its applicability. | Recover a directional admission-substitution predicate for the exact use. |
| `RoboticsEngineerSystemRole` treated as a subkind because of its name | A proposed edge is used as its own membership premise. | Evaluate paired classifications independently and apply C.3.1 monotonicity. |
| Non-monotonic restriction forced into `U.SubkindOf` | A true narrower judgment can coexist with a false broader judgment. | Keep the order unresolved or use a separately predicated residual relation. |
| Independence asserted without a joint condition | The checker cannot determine which holder, Work, and window combination is incompatible. | Put same- or different-holder, Work identity, overlap, applicability, and basis into the incompatibility predicate. |
| Bundle name treated as one kind | Holder allocation and independent assignments disappear. | Keep an order-insensitive kind-set relation and exact allocation predicate. |
| Taxonomy or scheme made a permanent participant | Interpretation support is turned into world-side relation identity even when meaning does not change. | Keep only kind participants and predicate; include an edition in semantic basis only when the rule depends on it. |
| Positive assertion reference used to create an occurrence | A reference and interval appear before predicate truth and individuation. | Establish truth, apply the identity rule when needed, then designate the occurrence. |
| Structure produces a decision | A non-agentive organization is made to act. | Name the system, Method, checking Work, and outcome pattern. |
| Graph treated as the relation structure | Representation identity replaces selected relation identity. | Recover the exact kind constituents, selected obtaining occurrences, applied constraints, and named selection-use frame; use C.29 for the graph and its preserved and lost structure. |
| Bridge used as substitution licence | Correspondence is overread as suitability, assignment, authorization, or outcome. | Keep Bridge, bounded use, reliance, local relation, and receiving Work separate. |
| Evaluation window declared as a participant | The receiver's target interval is confused with the world-side relation's derived extent. | Remove the temporal SlotSpec; keep `systemRoleKindRelationExtent` in an affirmative assertion or occurrence description and the target window in the receiving assertion or check. |

### A.2.7:8 - Consequences

**Benefits.** Receiving Methods can reuse exact kind relations without hiding their predicates. Safety checks state separation conditions precisely. Joint Work distinguishes the required kind set from holder allocation. Monotonic order remains a classification law rather than a label convention. Residual restrictions remain useful without weakening `U.SubkindOf`. Relation assertions can stay readable until a receiving use needs occurrence identity.

**Costs.** A consequence-bearing use must state the rule that an informal hierarchy or bundle name concealed. Each context-local relation species needs exact kind domains and predicate identity. Cross-context reuse may need a Bridge and bounded-use reliance. A compatible edition needs an explicit continuity decision before the same predicate is claimed.

**Limits.** This pattern ends at the exact relation among system-role kinds and any selected structure over those relations. Use A.2.1 for assignments, A.2.2 and A.2.5 for capability and assignment-state relations, and A.15 for planned or performed Work. The final decision remains an occurrence of its own exact outcome kind. Storage and visualization remain implementation and lens choices.

Reopen only the affected relation or structure when a participant kind, rule, applicability, meaning-bearing semantic basis, truth interval, selected relation occurrence, or C.3.1 basis changes.

### A.2.7:9 - Rationale

Systems applying receiving Methods often need stable organization among system-role kinds before they inspect actual assignments. Keeping that organization as a dependent `U.Structure` preserves its engineering use without inventing a system-role holon, assignment configuration, second taxonomy, or universal context object.

The families are separate because their laws differ. Substitution is directional. Incompatibility is symmetric under one joint condition. A bundle uses an order-insensitive finite set and an allocation rule. Monotonic qualification belongs to `U.SubkindOf`; non-monotonic restriction stays residual. One generic hierarchy cannot preserve those distinctions.

Relation realism prevents a document model from becoming the ontology. Direct predicates determine obtaining, and identity laws determine whether the same world-side relation occurrence continues; assertions, policies, and diagrams describe those facts. Slot discipline makes context-local participant domains reviewable and keeps the system-role kind, holder, assignment, predicate, slot, and representation position distinct.

### A.2.7:10 - SoTA-Echoing

| Current or mature line | What it contributes | Concrete use in A.2.7 |
|---|---|---|
| [gUFO 2026](https://arxiv.org/abs/2603.20948) | A current foundational-ontology comparator with explicit type and relation reification distinctions. | Keep relation obtaining, occurrence individuation, assertion episteme, and representation separate without importing gUFO's upper taxonomy. |
| [OpenFGA role-modeling guidance](https://openfga.dev/docs/best-practices/modeling-roles), updated 2026 | Distinguishes static role-like relations, user-defined role forms, and instance-specific assignments in authorization models. | Use it as a software stress case for separating kind relations, assignment inputs, and outcomes; do not make authorization the universal ontology. |
| [Cedar policy construction](https://docs.cedarpolicy.com/policies/syntax-policy.html) | Evaluates concrete principal, action, resource, scope, and additional conditions. | Keep structure as one premise while the checking system, exact assignments, action condition, and outcome remain visible. |
| Separation-of-duties practice across safety, clinical work, governance, and authorization | Useful independence claims depend on exact holder, Work, overlap, and applicability conditions rather than title intuition. | Put those conditions in the symmetric incompatibility predicate and test actual assignments separately. |
| FPF `C.3.1`, `A.6.REL`, `A.6.5`, and `A.22` | Supply monotonic kind order, relation occurrence identity, declaration-local SlotSpecs, and dependent structure identity. | Reuse the existing apparatus instead of creating another role taxonomy or relation-record ontology. |

The software sources are stress cases, not the universal subject. Their transferable contribution is the separation of kind definitions, instance assignments, evaluation inputs, and outcomes.

### A.2.7:11 - Relations

| Pattern | Relation |
|---|---|
| `A.1` | Keeps systems distinct from kinds, assignments, relation occurrences, and selected structures; only admitted systems act. |
| `A.1.1` | Use for a selected `BoundedModelUseStructure` when interpretation truly depends on it. |
| `A.2` and `C.3` | Use for exact context-local system-role kinds, their descriptions, membership, and classification. |
| `C.3.1` | Use for monotonic `U.SubkindOf`, its three-valued judgment discipline, effective-reference-scheme edition, obtaining, and identity. |
| `A.2.1` | Use for direct `U.SystemRoleAssignment` species and occurrences supplied to receiving checks. |
| `A.2.2` and `A.2.5` | Use for capability and assignment-state predicates and relations that remain separate from kind relations. |
| `A.3.1`, `B.1.5`, and `A.15` | Use for Method and Work identity, composition, planning, participation, and performance. |
| `A.3.4` | Use when current facts require one actual bounded change as a separate `U.Transformation`; it supplies neither a transformation-composition predicate nor holonhood. |
| `A.6.0`, `A.6.5`, and `A.6.REL` | Use for exact signatures, declaration-local SlotSpecs, relation obtaining, and progressive occurrence individuation. |
| `A.22` | Use to recover `SystemRoleKindRelationStructure` as a dependent non-agentive `U.Structure` over exact kinds and relations. |
| `A.6.9`, `F.9`, `C.2.1`, `A.10`, and `B.3` | Use for cross-scheme Bridges, bounded-use assertions, evidence reliance, and assurance without preserving local relation identity by form. |
| `A.2.4`, `C.27`, and `G.11` | Use for evidence-use relations, currentness, and support for assertions consumed by a receiving check. |
| `C.29` | Use for graph, table, matrix, algebra, and embedding representations and their preserved or lost structure. |
| `E.24.UK` | Use to avoid admitting a selected structure, local relation slot, or convenient bundle name as a root U-kind by punctuation. |
| `E.10.ROLE`, `F.5`, and `F.18` | Use for recovery of ambiguous source wording and durable naming after the exact object is known. |
| `F.19` | Test any optional explanatory overread against the intended reader and use. |

### A.2.7:End

