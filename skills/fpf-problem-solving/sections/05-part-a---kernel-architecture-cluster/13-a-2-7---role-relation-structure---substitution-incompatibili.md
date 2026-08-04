## A.2.7 - Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.7:0 - Use This When

**Plain name.** Relations among role values that a later admission or interpretation check can use.

Use this pattern when a role taxonomy contains several `U.Role` values and an engineer must state how those values are related before a system applying a receiving method can evaluate an actual assignment.

Typical moments include these:

- an inspection method description names `InspectorRole`, while the proposed holder is assigned `SeniorInspectorRole`;
- the same system must not hold author and approver roles for the same work during overlapping windows;
- a surgical procedure needs several role assignments jointly, with an explicit allocation rule;
- `RoboticsEngineerRole` narrows the meaning of `EngineerRole`, but that narrowing does not yet say whether one role can satisfy an admission condition written for the other.

**Primary EntityOfConcern.** The EntityOfConcern is one `RoleRelationStructure`: a selected, dependent `U.Structure` over declared `U.Role` values and exact obtaining relation occurrences among them. `RoleRelationStructure` is not a new root U-kind and not a holon. It is the non-agentive organization selected because that organization matters for a receiving use. An admitted system performs the receiving evaluation work by a selected method.

**Primary working reader.** The first reader is an engineer, method designer, safety practitioner, clinical team designer, or manager deciding which role relations a later check may rely on. The next reader must be able to recover the exact role meanings, relation predicates, temporal extents, and assignment checks without treating a role label, diagram, or policy row as the relation itself.

**First useful move.** Name the role-taxonomy episteme and effective reference scheme, select the exact relation species needed by the receiving use, and write its `RelationSignature` with one `SlotSpec` for every participant and predicate. Stop at a readable direct assertion if no receiving use needs relation-occurrence identity. Individuate and reference an occurrence only when a later claim depends on that identity.

**What goes wrong if missed.** A job-title hierarchy is used as if it settled admission. A statement that two duties should be independent has no exact holder, work, and time condition. A named bundle hides whether one system or several systems must hold the roles. A qualification such as `robotics engineer` is silently treated as system-kind subsumption, capability, assignment, or performed work. The receiving check then appears decisive while its actual relation premise is unavailable.

**What this buys.** Role admission, separation of duties, semantic qualification, and joint allocation can be reviewed as different relations. The same relations can support manufacturing, medicine, organizational work, and software authorization without making software policy the general ontology. Actual holders remain systems, actual assignments remain `U.RoleAssignment` occurrences, and the system performing the check remains visible.

**Not this pattern when.** Use `A.2.1` when the question is which admitted `U.System` holds a role and during which assignment episode. Use `A.2.5` for a role-state predicate, `A.2.2` for capability, A.3 patterns for methods, and A.15 patterns for planned or performed work. When meanings cross reference schemes, use `F.9` and `A.6.9` first for the exact Bridge, then `C.2.1` for the separate bounded-use assertion and `A.10` or `B.3` for current reliance; Bridge truth alone is not an A.2.7 relation or use licence. Use `C.29` when a graph, matrix, algebra, or embedding is the object under evaluation.

### A.2.7:1 - Problem Frame

A system applying a maintenance admission method may admit a current assignment to `SeniorHydraulicsTechnicianRole` where the method description names `HydraulicsTechnicianRole`. A system applying a safety method may reject overlapping author and approver assignments. A clinical method description may state a joint admission condition over surgeon, anesthetist, and scrub roles. These uses all concern relations among role values, but they do not concern the same relation.

The values are interpreted through a named role-taxonomy episteme and an effective `U.ReferenceScheme`. The direct relation predicate may obtain under that interpretation even before FPF publishes an assertion about it. A taxonomy statement can correctly or incorrectly assert the relation; the statement is not the occurrence by form. A specialized social ontology may make an accepted appointment, policy decision, or installation act constitutive, but only when its direct pattern says so.

Plainly, the role-taxonomy episteme is the claim-bearing description in which the role vocabulary and its relation claims can be inspected. The effective reference scheme is the by-value interpretation convention under which the current use resolves those role names and relation terms. `RoleRelationStructure` is the selected organization among the interpreted role values; a table or diagram may describe that organization but does not become it.

The relation structure is also not the actual assignment configuration. Only an admitted `U.System` can hold `U.RoleAssignment`. Systems act and perform work. Role values, taxonomy epistemes, relation occurrences, and selected structures do not.

### A.2.7:2 - Problem

The engineer needs a reusable role relation for a later engineering check, but common shorthand collapses at least four different questions:

1. Can an assignment to one role satisfy an admission condition written for another role?
2. Are two role assignments incompatible under a stated holder, work, and time condition?
3. Does one role value narrow the interpreted meaning of another role value?
4. Which role assignments must be present together, and how may they be allocated among systems?

Calling every answer a role hierarchy loses the predicate that makes the answer true. Calling the answer a role part introduces mereology without constructive assembly or a meta-holon transition. Calling the answer a policy, chart, or taxonomy record confuses the relation with an episteme that describes it. The resulting check cannot show which relation it consumed or what would invalidate its outcome.

### A.2.7:3 - Forces

| Force | Tension |
|---|---|
| Reuse of role vocabularies vs local meaning | The same role label can occur under different role-taxonomy epistemes and reference schemes. |
| Direct relation realism vs social constitution | Predicate truth is not created by a record, while some specialized social relations genuinely depend on an accepted constituting act. |
| Readable assertions vs occurrence identity | Ordinary work should remain light, but repeated or time-varying relations need distinguishable occurrences when later claims rely on them. |
| Role relation vs holder assignment | A relation among role values can guide a check, but it does not assign a role to a system. |
| Qualification vs admission substitution | Narrower meaning does not automatically license substitution in a consequence-bearing use. |
| Joint admission vs combined role | A method description may state a condition over several assignments without creating one composite role value or one role holon. |
| Structure vs representation | Selected organization may be made inspectable through a graph or matrix that remains a description or mathematical lens. |

### A.2.7:4 - Solution

Select one `RoleRelationStructure : U.Structure` over a declared role-value substrate. Populate it only with exact relation occurrences governed below. Use supported assertions about those occurrences as premises in work performed by a system under the receiving method, gate, or decision pattern.

```text
RoleRelationStructure : U.Structure {
  declaredRoleValueSubstrate: FinSet(U.Role), byValue,
  roleTaxonomyEpistemeRef: U.EpistemeRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  selectedRoleRelationOccurrenceRefs: FinSet(U.EntityRef),
  admissibleUse,
  nonAdmissibleUse,

}
```

Each `selectedRoleRelationOccurrenceRefs` value resolves to one explicitly individuated occurrence of one of the four direct A.2.7 relation species. This declaration is a compact recovery aid. The A.22 identity is the declared role-value substrate together with the selected organization of obtaining relations under the stated interpretation. A changed rendering, publication, diagram, table, identifier, or receiving-use model selection does not change that selected structure. A changed role-value substrate or relation organization does. When a selected `BoundedModelUseStructure` changes one receiving interpretation, designate it in that receiving assertion or use rather than in this structure declaration.

#### A.2.7:4.1 - Relation Realism and Constructive Settlement

Each governed relation is a direct species of `U.Relation`. Apply the order established by `A.6.REL`:

1. the exact predicate obtains for its participant fillings under the named role interpretation;
2. the occurrence is admitted under its direct relation species;
3. a receiving use explicitly individuates the occurrence only when it needs identity;
4. an identifier designates the individuated occurrence only when stable reference is needed;
5. a later assertion, check, or decision refers to it.

The role-taxonomy episteme and effective reference scheme fix the meanings of the role values and the by-value predicate. They therefore have explicit `SlotKind` declarations in each relation signature. The taxonomy episteme may contain an assertion that the predicate obtains, but an assertion, database row, policy text, graph edge, or publication does not become the relation occurrence by form.

Generic A.2.7 relations are predicate-realistic: the direct predicate determines obtaining. If a specialized role-governance ontology says that an accepted decision or installation act constitutes a relation, that specialization must name the constituting act and its acceptance condition. A.2.7 does not silently make every taxonomy statement constitutive.

Logical form contributes the predicate, argument discipline, and relation laws. Constructive ontology additionally requires grounded participant values, an obtaining condition, and an occurrence identity rule for any receiving use that needs one occurrence as an object of attention. Taxonomy nesting alone therefore admits neither a relation occurrence, a selected structure, nor a holon.

Relation predicates are often written as verbs, but the grammatical form does not admit an action, `U.Work`, `U.Method`, `U.Transformation`, acting system, or holon. The four A.2.7 relation species have typed participants, obtaining conditions, and occurrence identities; this pattern admits no own part relation, constructive assembly, or meta-holon transition for them. When actual change, a way of doing, or dated performance is current, state the neighboring `U.Transformation`, `U.Method`, or `U.Work` through its direct pattern. A.3.4 identifies one `U.Transformation` as an actual bounded change at the resolution and boundary needed by the current use; it supplies neither a transformation-composition governor nor holonhood. `U.Method` and `U.Work` are admitted holon kinds under A.3.1/B.1.5 and A.15.1, but an exact candidate still passes A.1 only through independently grounded constituents, whole-forming relations and assembly, reidentification, a composition-grounded whole-level characteristic, and larger-assembly compatibility. Verb-shaped wording supplies none of those facts. `U.Role` remains a non-holon role value held only through an assignment to an admitted `U.System`.

`RelationSignature` names the whole declaration. Each `SlotSpec = <SlotKind, ValueKind, refMode>` names one local position, its admitted filler kind, and its by-value or reference mode. In Plain explanation, a SlotKind may be called a position. `Place` is not introduced as another technical object. A role value can fill a SlotKind; the SlotKind does not thereby become a `U.Role`.

The four generic declarations below contain only the actual role-value or role-value-set participant, by-value predicate, role-taxonomy episteme, and effective reference scheme needed by that relation species. They contain no temporal participant. `RoleRelationExtent` is a local content ValueKind for an affirmative assertion or occurrence description; it states the currently known extent of one independently established occurrence. A predicate may declare how a receiving-use window is tested, while the receiving assertion or check may separately state `declaredRoleRelationEvaluationWindow`. Neither temporal value is a SlotSpec or makes the world-side relation obtain. For fixed participants, the actual occurrence extent is derived as the maximal continuous interval during which the exact predicate obtains.

#### A.2.7:4.2 - Role-Admission Substitution Relation

Use `RoleAdmissionSubstitutionRelation` when the engineering question in a receiving use is whether an assignment to one role value may satisfy an admission condition written for another role value.

```text
RoleAdmissionSubstitutionRelation : U.Relation
RelationSignature:
  CandidateAssignmentRoleValueSlot: U.Role, byValue
  AdmissionConditionRoleValueSlot: U.Role, byValue
  RoleAdmissionSubstitutionPredicateSlot: RoleAdmissionSubstitutionPredicate, byValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, byValue
```

`RoleAdmissionSubstitutionPredicate` states the exact receiving-use condition under which an assignment to the candidate role can satisfy the role condition. Its truth condition names the receiving `EntityOfConcern`, the applicability scope, and every direct predicate on which substitution depends instead of hiding that dependence in the role labels.

The relation is directional. Reversing its role-value fillings requires another predicate evaluation. Its claim is limited to admission substitution between the two interpreted role values. A.1 governs holder system kind, A.2.1 governs the current assignment, A.2.2 governs capability fit, A.2.5 governs role state, and A.15 governs performed work. The system performing the receiving check resolves the needed neighboring claims and applies the selected admission method.

The relation obtains while the fixed by-value substitution predicate is true for the two fixed role values under the fixed role-taxonomy episteme and effective reference scheme. Its occurrence extent is the maximal continuous interval of that truth. A mere label hierarchy, job grade, or taxonomy indentation is evidence at most; it is not the truth condition.

#### A.2.7:4.3 - Role Incompatibility Relation

Use `RoleIncompatibilityRelation` when two role assignments cannot be jointly admitted under one exact condition.

```text
RoleIncompatibilityRelation : U.Relation
RelationSignature:
  IncompatibleRoleValueSlot[1]: U.Role, byValue
  IncompatibleRoleValueSlot[2]: U.Role, byValue
  RoleIncompatibilityPredicateSlot: RoleIncompatibilityPredicate, byValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, byValue
```

The two indexed SlotKinds distinguish the two fillings in the declaration; the relation obeys the symmetry law

```text
incompatible(r1, r2, p) = incompatible(r2, r1, p)
```

`RoleIncompatibilityPredicate` states the exact rule over assignment configurations: which same- or different-holder test, receiving `EntityOfConcern` or work identity, temporal-overlap test, and other joint-admission condition makes the two interpreted role values incompatible. In the safety case below, the rule tests the same holder and same hazard-analysis work item during overlapping assignment windows. The exact `U.RoleAssignment` occurrences later evaluated are inputs to the receiving check under A.2.1; they are not copied into this role-value relation signature or occurrence identity. The relation obtains while the fixed rule truthfully characterizes the two fixed role values under the fixed taxonomy episteme and scheme. A conflicting allocation is a case satisfying the rule, not what creates the role relation.

The role-value relation does not itself reject an assignment. A system in the checking role applies the receiving method to the two current assignment occurrences and records the resulting admit, reject, defer, or unresolved outcome under the receiving pattern.

#### A.2.7:4.4 - Role Qualification Relation

Use `RoleQualificationRelation` when one role value narrows the interpreted meaning of another role value under a declared predicate.

```text
RoleQualificationRelation : U.Relation
RelationSignature:
  QualifiedRoleValueSlot: U.Role, byValue
  BaseRoleValueSlot: U.Role, byValue
  RoleQualificationPredicateSlot: RoleQualificationPredicate, byValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, byValue
```

The predicate states the exact semantic restriction. `RoboticsEngineerRole` may qualify `EngineerRole` by the robotics domain and the engineering methods for which the role is interpreted. The qualification claim concerns interpreted role meaning. C.3 separately governs `U.SubkindOf`, A.1 governs holder system kind, A.2 governs the non-holonic role value, A.2.2 governs capability, and `RoleAdmissionSubstitutionRelation` governs any additional admission-substitution claim.

The relation obtains while the fixed by-value qualification predicate is true for the two fixed role values under the fixed role-taxonomy episteme and effective reference scheme. Its occurrence extent is the maximal continuous interval of that truth. A shared word stem or a nested row in a taxonomy rendering does not establish that truth.

#### A.2.7:4.5 - Role Bundle Relation

Use `RoleBundleRelation` when a receiving use needs a finite set of role assignments jointly and the allocation rule matters.

```text
RoleBundleRelation : U.Relation
RelationSignature:
  BundledRoleValueSetSlot: FinSet(U.Role), byValue, cardinality at least 2
  JointRoleAdmissionPredicateSlot: JointRoleAdmissionPredicate, byValue
  RoleTaxonomyEpistemeSlot: U.Episteme, U.EpistemeRef
  EffectiveReferenceSchemeSlot: U.ReferenceScheme, byValue
```

`JointRoleAdmissionPredicate` states the allocation rule over candidate assignment configurations: whether one system may hold several assignments, distinct systems must hold specified assignments, some assignments may be shared, and how a receiving work window or method-applicability interval is tested. Exact current assignments and the selected receiving window remain inputs to the receiving check under their direct owners; they are not copied into this role-value-set relation signature. The relation does not create a combined role value. A durable combined role value requires its own A.2 settlement and assignment use; a convenient name for this bundle remains a name for the relation unless that stronger settlement exists.

The relation obtains while the fixed by-value allocation rule truthfully characterizes the fixed interpreted role-value set under the fixed role-taxonomy episteme and effective reference scheme. Its occurrence extent is the maximal continuous interval of that truth. A list of role labels without an allocation predicate is not a bundle relation occurrence.

#### A.2.7:4.6 - Occurrence Identity and Continuity

Do not replace the world-side identity rule with a database, graph, or tuple key. One occurrence begins when the exact fixed participant fillings of one direct relation species satisfy its fixed predicate. It continues while those same participants remain fixed and the predicate obtains without interruption. Its identity therefore uses the direct relation species, exact role-value or role-value-set filling, exact by-value predicate, exact role-taxonomy episteme, exact effective reference scheme, and the derived maximal continuous obtaining extent.

For symmetric incompatibility, exchanging the two role-value fillings does not change identity. For a bundle, set order does not change identity. Changing a role value, predicate, taxonomy episteme, or effective scheme identifies another occurrence even if every displayed label remains the same.

A.2.7 defines each relation-specific obtaining predicate and same-versus-new-occurrence rule. It does not inspect a current case and does not establish that one current occurrence obtains. Relevant current case facts or accepted constituting history must satisfy the direct predicate. When a receiving use needs one occurrence as a referent, a system performing explicit-individuation work applies the identity rule to those facts and recovers the already obtaining occurrence before any assertion or identifier designates it. If no receiver needs occurrence identity, keep the readable direct relation and stop before individuation.

An affirmative assertion or occurrence description may state the currently known `roleRelationExtent` only after that predicate-satisfaction and identity application have recovered the occurrence. `[relationStart, open]` can describe the current extent before its end is known. Later closure refines the temporal description of the same occurrence when obtaining was uninterrupted. A demonstrated predicate-false interval ends the occurrence; later resumption begins another. Missing evidence leaves reliance on the assertion unresolved and does not demonstrate a non-obtaining gap. A target `declaredRoleRelationEvaluationWindow` belongs to the receiving assertion or check, not to the direct relation signature or occurrence identity.

A selected model-use structure does not enter these generic relation signatures or identities. A genuinely structure-dependent relation species requires its own direct pattern, required structure participant, stronger obtaining predicate, and explicit identity law. A changed publication or rendering of the same taxonomy episteme creates no relation occurrence. An F.9 Bridge between changed scheme-local meanings likewise never preserves or merges A.2.7 occurrence identity; it can support only a separately stated bounded use across the independently identified meanings.

#### A.2.7:4.7 - Assertion and Receiving Check

A relied-on role-relation claim is an ordinary C.2.1 assertion episteme, not the relation occurrence. Keep three moves in this order:

1. A.2.7 defines the direct relation predicate, applicability, and same-versus-new-occurrence rule.
2. Relevant current case facts or accepted constituting history satisfy or fail that predicate. Predicate satisfaction makes the direct relation obtain. When the receiving use needs one occurrence as an exact referent, a system performing explicit-individuation work applies the A.2.7 identity rule to those facts and recovers that already obtaining occurrence.
3. Only then may an affirmative assertion use the recovered occurrence as its exact `EntityOfConcern` and designate its currently known `roleRelationExtent`. The assertion states the result; it neither establishes predicate satisfaction nor individuates the occurrence.

When no positive occurrence has been recovered, a negative, candidate, counterfactual, or unsupported affirmative claim normally uses the exact admitted A.2.7 direct relation kind as its C.2.1 `EntityOfConcern`. Its ClaimGraph carries the proposed role-value fillings, by-value predicate, effective scheme, and exact polarity or modality. If the claim instead concerns another independently identified exact entity, name that entity by value and state the relation proposal in the ClaimGraph. A tuple of proposed fillings, a policy row, or a convenient label is not an alternative EntityOfConcern. Neither branch carries a positive occurrence reference or an actual `roleRelationExtent`.

Unresolved reliance preserves the assertion's stated polarity; it is not a third polarity and does not create or erase an occurrence. In every branch the C.2.1 identity triple remains claim content, exact `EntityOfConcern`, and the assertion's effective reference scheme. Evidence, currentness, and supported, refuted, or unresolved reliance remain separate and make no world-side occurrence obtain.

Supported assertions about selected role relations serve as typed premises for another method; the selected structure is not the checker. A system performing a receiving check normally makes these moves:

1. resolve the current facts and any exact `U.RoleAssignment` or A.2.5 role-state occurrences needed to test the direct A.2.7 predicate under their own patterns;
2. test that predicate for the fixed role values, taxonomy episteme, and effective scheme;
3. when the receiving use needs occurrence identity, apply the direct identity rule and recover the exact role-relation occurrence without copying assignment or role-state objects into its participant set;
4. establish the appropriate C.2.1 assertion: designate the recovered occurrence only for the affirmative recovered-occurrence branch, or use the direct relation kind or another independently identified entity for a no-recovered-occurrence branch;
5. evaluate any separate A.2.2 capability-fit, resource, interface, risk, evidence, currentness, or assurance conditions under their direct patterns; and
6. perform the checking work by the selected method and record the check outcome defined by the receiving pattern.

This order keeps three layers visible: case facts make the role relation obtain, explicit-individuation work recovers one occurrence only when a receiver needs it, and an episteme asserts it with some support before a system may use that assertion while performing a check. None of these layers substitutes for the others.

#### A.2.7:4.8 - Recovering Apparent Role Decomposition

When ordinary wording says `subrole`, `role part`, or `combined role`, start from the engineering question rather than the word:

| Engineering question | Recovered object |
|---|---|
| May this assigned role satisfy a condition written for another role? | `RoleAdmissionSubstitutionRelation` |
| Does this role value narrow another role's interpreted meaning? | `RoleQualificationRelation` |
| Must these role assignments not overlap under an exact condition? | `RoleIncompatibilityRelation` |
| Must these role assignments be present together under an allocation rule? | `RoleBundleRelation` |
| Who holds the role and when? | `U.RoleAssignment` under A.2.1 |
| Is the assignment in a work-admitting state? | `RoleStateRelation` under A.2.5 |
| Can the holder perform within an operating envelope? | capability and capability-fit relations under A.2.2 |
| Are ways of doing or work occurrences composed? | method composition under A.3 and B.1.5, or work structure under A.15 |

This recovery is constructive. `U.Role` has no admitted part relation or meta-holon transition. The recovered relations and neighboring objects remain available without pretending that they are role parts.

#### A.2.7:4.9 - Representation, Model-Use, and Cross-Scheme Boundaries

A graph, table, matrix, algebra, embedding, policy file, or organization chart may describe a `RoleRelationStructure` or support a `C.29` mathematical-lens use. It is not the selected structure or any selected relation occurrence by form. State what organization the representation preserves and loses before relying on it.

Role semantic locality normally comes from one role-taxonomy episteme and effective reference scheme. Reference an independently selected `BoundedModelUseStructure` only when interpretation depends on its DDD-style model-use organization; designate it in the receiving assertion or use, not in a generic A.2.7 signature.

When a proposed comparison, substitution, translation, or reuse crosses schemes, first recover the exact F.17 sense cells and exact obtaining F.9 Bridge. Then state a separate C.2.1 assertion about that Bridge naming the bounded use `u`, source-to-receiving direction `d`, use-specific correspondence rule `r`, tolerated semantic loss `t`, affirmative or negative polarity, and effective reference scheme. For ordinary reliance below B.3's material-reliance threshold and with no assurance claim, require the exact current A.10 evidence-provenance graph relation and `RelianceDisposition=pass` for that same use. When an assurance claim is made or the threshold is met, B.3 first asks whether a current positive assurance claim exists: only one carrying the same use with a sufficient minimum reliance safety assurance record supports it; otherwise an explicit no-assurance, insufficient-record, narrowed, rejected, withdrawn, abstaining, or blocked disposition stops or narrows the use. Neither branch supplies authorization.

The Bridge, its profile, or an optional Bridge Card alone establishes neither bounded-use suitability nor an A.2.7 relation, assignment, receiving-check outcome, or performed work. If a receiving check uses the bounded-use assertion while evaluating an A.2.7 predicate, that assertion remains a separate premise; any local role relation that obtains keeps the participant set and identity declared here, and the actual check remains work performed by a system under its direct owner.

#### A.2.7:4.10 - Lightweight Path

Ordinary prose may state a readable relation and stop:

```text
For pump pressure-test work, SeniorHydraulicsTechnicianRole may satisfy
the role condition written for HydraulicsTechnicianRole.
```

Add a full signature when reusable typing matters. Individuate an occurrence when another claim depends on its identity. Assign an identifier only when stable reference matters. Build a `RoleRelationStructure` only when several selected relations or constraints must be used together. Completeness is not a reason to materialize every layer.

### A.2.7:5 - Archetypal Grounding

#### A.2.7:5.1 - Manufacturing Admission Substitution

`PlantMaintenanceRoles-2026` under `Plant-A-Maintenance-Scheme` interprets two role values. Throughout 2026H2, the operating Plant-A pressure-test admission method applies this fixed conditional rule: a current assignment to `SeniorHydraulicsTechnicianRole` may satisfy the condition written for `HydraulicsTechnicianRole` in `PumpPressureTestMethodFamily` only while the exact A.2.5 `PressureTestReady` predicate obtains. The current method configuration and observed admission-gate behavior establish that this rule truthfully characterizes those two interpreted role values for the interval; the fact is not inferred merely from a taxonomy row.

Those case facts satisfy the direct `RoleAdmissionSubstitutionPredicate`. Because the assertion below needs one occurrence as its EntityOfConcern, explicit-individuation work applies the A.2.7 identity rule to the fixed relation species, role-value fillings, predicate, taxonomy episteme, scheme, and maximal continuous predicate-true interval. It recovers the exact occurrence `Plant-A-Pressure-Test-RoleSubstitution-2026H2` with extent `[2026-07-01, 2026-12-31]` before the assertion designates it:

```text
RoleAdmissionSubstitutionAssertion:
  entityOfConcernRef: Plant-A-Pressure-Test-RoleSubstitution-2026H2
  effectiveReferenceScheme: Plant-A-Maintenance-Scheme
  ClaimGraph:
    directClaimFamilyRef: A.2.7 RoleAdmissionSubstitutionRelation
    participantDesignations:
      CandidateAssignmentRoleValueSlot: SeniorHydraulicsTechnicianRole
      AdmissionConditionRoleValueSlot: HydraulicsTechnicianRole
      RoleAdmissionSubstitutionPredicateSlot:
        receiving method belongs to PumpPressureTestMethodFamily
        and candidate assignment has an obtaining A.2.5 PressureTestReady relation
      RoleTaxonomyEpistemeSlot: PlantMaintenanceRoles-2026
      EffectiveReferenceSchemeSlot: Plant-A-Maintenance-Scheme
    assertionPolarity: affirmative
    roleRelationExtent: [2026-07-01, 2026-12-31]
```

The system performing work-admission checking resolves the proposed holder's exact `SeniorHydraulicsTechnicianRole` assignment under A.2.1 and the exact current `PressureTestReady` occurrence or assertion under A.2.5 while applying the selected method. Those objects satisfy inputs named by the substitution predicate; they are not additional substitution-relation participants. Pressure-test capability is evaluated separately under A.2.2. The substitution relation does not prove capability and does not say that pressure-test work occurred.

#### A.2.7:5.2 - Safety Separation of Duties

For one hazard-analysis work item, the same system must not both author and approve during overlapping assignment windows. Since 2026-01-01, `SafetyCaseRoles-2026` under `Safety-Assurance-Scheme` has continuously interpreted the two role values with exactly that same-holder, same-work, overlapping-window incompatibility rule. The operating work-admission method and accepted safety-control history show that the rule remains in force with no demonstrated predicate-false interval; a particular conflicting allocation is only a later case tested by the rule.

Those case facts satisfy the direct `RoleIncompatibilityPredicate`. Because the assertion below needs an exact occurrence as its EntityOfConcern, explicit-individuation work applies the symmetric A.2.7 identity rule to the fixed role-value pair, predicate, taxonomy episteme, scheme, and maximal continuous predicate-true interval. It recovers `HazardAnalysisAuthorApproverIncompatibility-2026` with extent `[2026-01-01, open]` before the assertion designates it:

```text
RoleIncompatibilityAssertion:
  entityOfConcernRef: HazardAnalysisAuthorApproverIncompatibility-2026
  effectiveReferenceScheme: Safety-Assurance-Scheme
  ClaimGraph:
    directClaimFamilyRef: A.2.7 RoleIncompatibilityRelation
    participantDesignations:
      IncompatibleRoleValueSlot[1]: HazardAnalysisAuthorRole
      IncompatibleRoleValueSlot[2]: HazardAnalysisApproverRole
      RoleIncompatibilityPredicateSlot:
        incompatible when one HolderSystem fills both exact assignments
        for the same HazardAnalysisWorkItem
        during overlapping assignment extents
      RoleTaxonomyEpistemeSlot: SafetyCaseRoles-2026
      EffectiveReferenceSchemeSlot: Safety-Assurance-Scheme
    assertionPolarity: affirmative
    roleRelationExtent: [2026-01-01, open]
```

A verifier system applies the work-admission method to two exact A.2.1 assignment occurrences and the target hazard-analysis work item. Those receiving inputs can satisfy the incompatibility rule, but they do not enter the role-value relation signature. The verifier's checking work produces the receiving pattern's rejection outcome for the overlapping allocation. The incompatibility relation neither performs verification nor produces that outcome.

#### A.2.7:5.3 - Clinical Joint Admission

A surgical method description states a joint admission rule: surgeon, anesthetist, and scrub roles must be held by three distinct systems throughout whichever procedure window the receiving check selects. Since 2026-01-01, `OperatingTheatreRoles-2026` under `Hospital-Clinical-Scheme` has continuously interpreted the fixed three-role set with that exact distinct-holder and full-window allocation rule. The operating admission method and accepted clinical-governance history establish that the rule currently characterizes the role-value set; the assignments for one planned procedure are later receiving inputs, not relation participants or occurrence creators.

Those case facts satisfy the direct `JointRoleAdmissionPredicate`. Because the assertion below needs one occurrence as its EntityOfConcern, explicit-individuation work applies the bundle identity rule to the order-insensitive role-value set, fixed predicate, taxonomy episteme, scheme, and maximal continuous predicate-true interval. It recovers `OperatingTheatreThreeRoleBundle-2026` with extent `[2026-01-01, open]` before the assertion designates it:

```text
RoleBundleAssertion:
  entityOfConcernRef: OperatingTheatreThreeRoleBundle-2026
  effectiveReferenceScheme: Hospital-Clinical-Scheme
  ClaimGraph:
    directClaimFamilyRef: A.2.7 RoleBundleRelation
    participantDesignations:
      BundledRoleValueSetSlot:
        {SurgeonRole, AnesthetistRole, ScrubPractitionerRole}
      JointRoleAdmissionPredicateSlot:
        for the declared receiving procedure window:
        each role has one obtaining A.2.1 assignment;
        the three HolderSystems are distinct;
        every assignment extent covers that window
      RoleTaxonomyEpistemeSlot: OperatingTheatreRoles-2026
      EffectiveReferenceSchemeSlot: Hospital-Clinical-Scheme
    assertionPolarity: affirmative
    roleRelationExtent: [2026-01-01, open]
```

For the planned procedure `[2026-07-13T08:00, 2026-07-13T14:00]`, the receiving check records that interval as `declaredRoleRelationEvaluationWindow` and resolves the three exact assignment occurrences separately. The bundle relation supplies the allocation rule; the check supplies the current fillings. Clinical credentials, current readiness, and procedure-specific capability remain separate assertions. The procedure team is not created as a role value by naming this bundle.

#### A.2.7:5.4 - Robotics Qualification and Independent Musician Assignment

Since 2026-01-01, `MusicalRobotLabRoles-2026` under `Musical-Robot-Lab-Scheme` has continuously interpreted `RoboticsEngineerRole` as narrowing `EngineerRole` by participation concerning robotics systems and `RoboticsEngineeringMethodFamily`. The lab's current interpretation practice and accepted role-semantics history agree on that exact restriction with no demonstrated predicate-false interval; a shared word stem or nested taxonomy row alone would not establish it.

Those case facts satisfy the direct `RoleQualificationPredicate`. Because the assertion below needs one occurrence as its EntityOfConcern, explicit-individuation work applies the directional A.2.7 identity rule to the fixed role-value fillings, predicate, taxonomy episteme, scheme, and maximal continuous predicate-true interval. It recovers `RoboticsEngineerQualification-2026` with extent `[2026-01-01, open]` before the assertion designates it:

```text
RoleQualificationAssertion:
  entityOfConcernRef: RoboticsEngineerQualification-2026
  effectiveReferenceScheme: Musical-Robot-Lab-Scheme
  ClaimGraph:
    directClaimFamilyRef: A.2.7 RoleQualificationRelation
    participantDesignations:
      QualifiedRoleValueSlot: RoboticsEngineerRole
      BaseRoleValueSlot: EngineerRole
      RoleQualificationPredicateSlot:
        engineering participation interpreted for robotics systems
        and the RoboticsEngineeringMethodFamily
      RoleTaxonomyEpistemeSlot: MusicalRobotLabRoles-2026
      EffectiveReferenceSchemeSlot: Musical-Robot-Lab-Scheme
    assertionPolarity: affirmative
    roleRelationExtent: [2026-01-01, open]
```

Vasya may separately hold `RoboticsEngineerRole` and `MusicianRole` through two exact `U.RoleAssignment` occurrences. Those assignment identities and extents remain under A.2.1. Robot-engineering work, music-performance work, and teaching-robots-music work remain A.15 work occurrences. If a method description written for `EngineerRole` allows admission of the robotics assignment, add a separate substitution relation; qualification alone does not settle that use.

### A.2.7:6 - Conformance Checklist

| Check | Question |
|---|---|
| `CC-A2.7-01` | Is the current object an exact role relation occurrence or one dependent `U.Structure` selecting such occurrences? |
| `CC-A2.7-02` | Are all role meanings fixed by a named role-taxonomy episteme and by-value effective reference scheme? |
| `CC-A2.7-03` | Does every direct relation declaration have one `RelationSignature` and complete `SlotSpec` discipline? |
| `CC-A2.7-04` | Does the by-value predicate state the actual admission, incompatibility, qualification, or allocation condition? |
| `CC-A2.7-05` | Is relation obtaining kept distinct from assertion, evidence, identifier, publication, and receiving-check outcome? |
| `CC-A2.7-06` | Is only an admitted `U.System` used as a role-assignment holder and as the performer of checking work? |
| `CC-A2.7-07` | Are qualification and admission substitution represented as different relations? |
| `CC-A2.7-08` | Does incompatibility name its holder, work, temporal, or other exact joint-admission condition? |
| `CC-A2.7-09` | Does a bundle state its holder-allocation rule without creating a combined role value by name? |
| `CC-A2.7-10` | When occurrence identity matters, does it use the exact fixed participant fillings plus the derived maximal continuous obtaining extent, rather than a storage key or temporal participant? |
| `CC-A2.7-11` | Does a demonstrated non-obtaining gap create a later occurrence while an evidence gap remains unresolved? |
| `CC-A2.7-12` | Is any selected model-use structure designated by the receiving assertion or use rather than appended as an optional participant of a generic role relation? |
| `CC-A2.7-13` | Does the receiving pattern own evaluation and outcome, with separate state, capability, method, work, evidence, and assurance relations where needed? |
| `CC-A2.7-14` | Are graphs, tables, matrices, algebras, embeddings, policies, and publications kept as descriptions, lenses, or epistemes rather than selected relations by form? |
| `CC-A2.7-15` | Is a verb-shaped relation predicate kept distinct from acting, work, method, transformation, constructive assembly, and holon admission? |
| `CC-A2.7-16` | Is `RoleRelationExtent` only affirmative assertion or occurrence-description content, with any target evaluation window kept in the receiving assertion or check and no temporal SlotSpec in a generic relation signature? |
| `CC-A2.7-17` | Before an affirmative assertion designates an occurrence, do current case facts or accepted constituting history satisfy the direct predicate and has explicit-individuation work applied the identity rule? When no positive occurrence is recovered, is the exact direct relation kind or another independently identified entity the C.2.1 EntityOfConcern, with proposed fillings, predicate, polarity or modality kept in the ClaimGraph and no fabricated occurrence reference or actual extent? |
| `CC-A2.7-18` | Does any cross-scheme use keep the exact F.9 Bridge, separate C.2.1 bounded-use assertion, and current A.10 or B.3 reliance distinct, with no Bridge, profile, or card used as a substitution licence or occurrence-identity bridge? |

### A.2.7:7 - Failure Modes and Repairs

| Failure | Why it fails | Repair |
|---|---|---|
| Job-title order used for admission | The title order does not state the receiving-use predicate. | Declare a directional `RoleAdmissionSubstitutionRelation` for the exact method or work condition. |
| `RoboticsEngineerRole` treated as a system subkind | Role meaning is confused with holder kind. | Keep the holder's system kind stable and state `RoleQualificationRelation`; add substitution only if admission is also intended. |
| Independence asserted without a joint condition | A system applying the receiving method cannot determine which holder, work, and window combination is incompatible. | Put that exact condition into `RoleIncompatibilityPredicateSlot`. |
| Bundle name treated as one role | Holder allocation and independent assignments disappear. | Keep `RoleBundleRelation` and its allocation predicate; admit a separate role value only through A.2. |
| Taxonomy row treated as relation occurrence | Episteme form is confused with predicate obtaining. | State the direct predicate first; use the row as an assertion and support it under evidence rules. |
| Positive assertion reference used to create an occurrence | A reference and interval are filled before current case facts satisfy the direct predicate and before the identity rule recovers one occurrence. | State the case facts, test the predicate, apply the direct identity rule when the receiver needs occurrence identity, and only then designate the recovered occurrence. Without a recovered occurrence, use the direct relation kind or another independently identified entity as the assertion's EntityOfConcern and keep proposed fillings in the ClaimGraph. |
| Relation structure produces a decision | A non-agentive structure is made to act. | Name the system, method, checking work, and outcome governed by the receiving pattern. |
| Graph treated as role ontology | Representation identity replaces selected relation identity. | Name the `RoleRelationStructure` and exact occurrences; use C.29 for the graph's preserved and lost structure. |
| Temporal window declared as a participant | A receiving or descriptive window is confused with the direct occurrence's world-side extent. | Remove the temporal SlotSpec; derive maximal continuous obtaining extent and state `roleRelationExtent` or a target evaluation window only in the appropriate assertion or check. |
| Bridge used as role-substitution licence | Semantic correspondence is overread as suitability, reliance, assignment, or a receiving outcome. | Keep the exact Bridge, bounded-use assertion, A.10 or B.3 reliance, local A.2.7 relation, and actual receiving work as separate objects. |

### A.2.7:8 - Consequences

**Benefits.** A system applying a method can reuse role relations without hiding its admission predicate. Safety and governance checks can state separation conditions exactly. Joint work can distinguish role-set membership from holder allocation. Role qualification remains semantic and does not become system taxonomy. Relation assertions can stay readable until a receiving use needs explicit occurrence identity.

**Costs.** A consequence-bearing use must write the predicate that an informal hierarchy or bundle name previously concealed. Repeated relations may need temporal extent or another direct identity discriminator. Existing policy tables and organization charts may need a separate assertion layer and explicit links to the selected occurrences they describe.

**Limits.** This pattern ends at the selected role relation and its structure. A.2.1 establishes actual assignments, A.2.2 and A.2.5 establish capability and current role state, A.15 establishes performed work, evidence patterns establish support, and the receiving pattern governs the final admission outcome. Storage and visualization remain implementation and lens choices.

### A.2.7:9 - Rationale

Role relation structure is useful because systems applying receiving methods often need stable organization among role values before they evaluate actual assignments. Keeping the organization as dependent `U.Structure` preserves its engineering use without inventing a role holon, a second role taxonomy, or a universal context object.

The four relation species are separate because they answer different questions and have different laws. Substitution is directional. Incompatibility is symmetric under one exact joint condition. Qualification narrows interpreted meaning without licensing admission. A bundle names joint admission and holder allocation without creating a composite role value. A generic role hierarchy cannot preserve these distinctions.

Relation realism keeps the ontology from becoming a document model. Constructive discipline keeps admission explicit: FPF recognizes the relation through its direct predicate, typed participants, interpretation, and occurrence identity; it does not infer existence from a label or record. Slot discipline then makes each local position reviewable without calling it a role or a place.

### A.2.7:10 - SoTA-Echoing

| Current research or practice line | What changes in this pattern | Practitioner implication |
|---|---|---|
| [gUFO 2026](https://arxiv.org/abs/2603.20948) provides a current foundational-ontology comparator with explicit type typology and reification patterns for relational aspects. | A.2.7 keeps relation obtaining, occurrence individuation, assertion episteme, and representation separate; it does not import gUFO's taxonomy as the FPF constructive ontology. | A relation can be referred to when needed without making every relation a record or every imported class an FPF kind. |
| [OpenFGA role-modeling guidance, updated 2026](https://openfga.dev/docs/best-practices/modeling-roles) documents static role-like relations, user-defined roles, and instance-specific role assignments as different modeling choices. | A.2.7 keeps role-value relations separate from actual `U.RoleAssignment` occurrences and supports a lightweight path before instance-specific assignment complexity is needed. | A stable role relation can be reused while holder assignment remains explicit and instance-specific. |
| [Cedar policy construction](https://docs.cedarpolicy.com/policies/syntax-policy.html) separates principal, action, resource, scope, and additional conditions during authorization evaluation. | A.2.7 treats role structure as one typed premise of a receiving evaluation, not as the acting principal or the decision itself. | The checking system, evaluated assignments, action-facing condition, and outcome remain inspectable. |
| Separation-of-duties practice across safety, clinical work, governance, and authorization depends on exact joint-admission conditions rather than title intuition. | `RoleIncompatibilityPredicateSlot` names holder, work, and temporal conditions, and `RoleBundleRelation` names the allocation rule. | Independence and team-composition claims can be tested in the domain where they matter. |

The software authorization sources are stress cases, not the universal subject. Their useful move is the separation of role definitions, instance assignments, evaluation inputs, and outcomes. A.2.7 generalizes that move to any project in which admitted systems hold roles and perform work.

### A.2.7:11 - Relations

| Pattern | Relation |
|---|---|
| `A.1` | Keeps role values, relation structures, and role assignments out of holon admission unless their direct kinds pass the constructive test. |
| `A.1.1` | Governs optional `BoundedModelUseStructure` when interpretation genuinely depends on a DDD-style model-use organization. |
| `A.2` | Governs `U.Role`, role-taxonomy epistemes, effective reference schemes, the system-holder boundary, and the rejection of role mereology. |
| `A.2.1` | Governs actual `U.RoleAssignment` occurrences used by receiving checks. |
| `A.2.2` and `A.2.5` | Govern capability and role-state predicates that remain separate from role relations. |
| `A.3.1`, `A.3.4`, `B.1.5`, and `A.15` | A.3.1/B.1.5 and A.15 govern method/work identity, composition, participation, planning, and performance. A.3.4 governs actual bounded-change identity and supplies no transformation composition or holonhood; A.1 remains the independent exact-candidate test. |
| `A.6.0`, `A.6.5`, and `A.6.REL` | Govern `RelationSignature`, `SlotSpec`, and progressive relation-occurrence individuation. |
| `A.22` | Governs `RoleRelationStructure` as dependent non-agentive `U.Structure` over a declared substrate. |
| `A.6.9`, `F.9`, `C.2.1`, `A.10`, `B.3`, `F.5`, and `F.18` | Govern the exact cross-scheme Bridge, separate bounded-use assertion, current reliance branch, and durable naming after role values and local relations are settled; none preserves A.2.7 occurrence identity or supplies assignment, authorization, checking work, or outcome. |
| `A.10`, `A.2.4`, `C.27`, and `G.11` | Govern evidence, currentness, and support for assertions used by receiving checks. |
| `C.29` | Governs mathematical-lens evaluation of graphs, matrices, algebras, and embeddings used to represent the selected structure. |
| `E.24.UK` | Prevents a selected structure, relation SlotKind, or convenient bundle name from becoming a root U-kind by punctuation. |

### A.2.7:End

