## A.12 - Acting-Side Externalization and Reflexive Split

> **Type:** Part A architectural ontology pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.12:0 - Use This When

Use this pattern when a source says that something changes, repairs, configures, updates, verifies, teaches, controls, or improves itself, or when the acting side of a change is hidden behind a passive or self-action sentence.

Typical moments:

- "the robot calibrates itself";
- "the model updates itself";
- "the document refreshes its own cross-references";
- "the organization corrected itself";
- "the system verifies that its own change succeeded";
- "the lathe makes the workpiece, therefore the workpiece is part of the lathe during manufacturing".

**First useful move.** Separate the exact continuing subject named as changed from the exact entity proposed for the acting side. Identify the changed subject under its direct identity owner. Before A.1 recognizes the acting-side entity under `U.System`, retain the exact `U.Entity` and its `recognized | rejected | unknown` disposition or exact blocker; do not fill an acting-system position. After recognition, name the exact `U.System` and recover its acting-side participation or work-facing role assignment under the direct owner. If an actual bounded change is current, let `A.3.4` test that same continuing subject; then use `A.15` and `A.15.1` for method and work, `A.2.1` and `A.2.7` for role assignment and role relations, `A.10` for evidence, and `A.1`, `A.14`, or `C.13` for holon and part-whole claims.

**What goes wrong if missed.** A system becomes its own cause, a document acts, a controller and controlled part collapse into one object, evidence becomes self-certifying, and a system that changes another holon is mistaken for the larger whole containing it without an obtaining part-whole relation.

**What this buys.** Self-action wording becomes a reviewable relation among one exact continuing changed subject, the exact entity proposed for the acting side, its same-entity `U.System` reading only after A.1 recognition, and any separately governed participation, role, method, Work, boundary-crossing, or evidence claims that are current. Reflexive use remains the narrower holon case with two exact parts or subsystems.

**Not this pattern when.**

- If the current question is whether a bounded change occurred, use `A.3.4`.
- If the current question is whether work was performed or succeeded, use `A.15` and `A.15.1`.
- If the current question is the role assignment or role relation, use `A.2.1` and `A.2.7`.
- If the current question is evidence independence or source use, use `A.10` and the evidence or source-use owners.
- If the current question is part-whole admission, use `A.1`, `A.14`, and `C.13`.

### A.12:1 - Problem Frame

A.12 keeps a causality-facing modeling discipline without creating a second transformation ontology.

The pattern does not say that every change is already established, that work succeeded, that the acting-side entity has already been recognized as a system, that it belongs to a special `U.Transformer` kind, or that boundary wording creates a durable boundary object. It says only this: when a claim depends on a change, recover the exact changed participant and the exact entity proposed for the acting side as distinct participants in that claim. When ordinary language says "self-", split the larger holon into distinct acting and changed positions before using transformation, method, work, evidence, or part-whole patterns.

### A.12:2 - Problem

Without A.12:

1. **Self-action hides the acting side.** "The system changed itself" does not say which exact entity occupies the acting side, whether A.1 recognizes that entity under `U.System`, which exact continuing subject is claimed to change, or which direct relation governs the claim.
2. **Transformation and work collapse.** A bounded transformation, a method, a work occurrence, and evidence of success are treated as the same claim.
3. **Epistemes become agents.** A document, model, source record, report, or theory is said to update, decide, authorize, or verify itself.
4. **Reflexive systems become single blocks.** A regulator and regulated part are hidden inside one block, so failure analysis and architecture work lose the internal relation that mattered.
5. **Transformation becomes containment.** A system changing another holon is treated as that holon's containing whole.
6. **Evidence becomes self-certifying.** The acting system's own output is treated as sufficient evidence for the success or safety of its work.

### A.12:3 - Forces

| Force | Tension |
| --- | --- |
| Causal clarity vs convenient speech | Everyday speech compresses "self-repair" and "automatic update"; engineering use needs the acting side and changed object. |
| Internal regulation vs object collapse | A larger holon may contain both regulator and regulated parts; that does not make the regulator and regulated position identical for the current claim. |
| Automation vs accountability | Automated work still needs a system in role, method or work claim, and evidence relation when those claims matter. |
| Episteme use vs episteme agency | Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme. A different carrier, publication, grounding, or use belongs to its own object or relation. No episteme thereby acts. A causal or interaction claim gets its participants from its direct owner; a Work performer or `U.RoleAssignment` holder must be an admitted `U.System`. |
| Boundary crossing vs parthood | When an exact boundary-crossing relation independently obtains under its direct owner, it does not thereby make the acting system a part of the changed holon or the larger whole containing it. Without that governor, keep the crossing claim open rather than inferring either crossing or parthood. |

### A.12:4 - Solution

Use A.12 as a thin acting-side pattern.

#### A.12:4.1 - Acting-Side Externalization

For a change-bearing claim, recover this relation frame before relying on self-action wording:

```text
ActingSideExternalization@Context:
  changedSubjectRef: one exact continuing referent identified under its direct identity owner
  actingEntityRef: exact U.Entity proposed for the acting side
  actingSystemRef?: U.System, fill only after A.1 recognizes actingEntityRef
  a1RecognitionDispositionOrBlockerRef?: required while actingSystemRef is unfilled
  actingRoleAssignmentRef?: one exact obtaining U.RoleAssignment, only when a work-facing role claim is current
  actingSideParticipationRef?: one exact obtaining relation occurrence under its direct participation, causal, or interaction owner
  transformationRef?: U.Transformation, fill only when A.3.4 identifies a bounded change of changedSubjectRef
  methodRef?
  methodDescriptionRef?
  workPlanRef?
  workOccurrenceRef?
  holonBoundaryCrossingRelationRef?: one exact obtaining relation occurrence under its direct crossing-relation owner
  evidenceRelationRefs?
  strongerOwnerRefs:
```

The exact entity in `actingEntityRef` and the exact referent in `changedSubjectRef` are distinct participants in the current change-bearing claim. `changedSubjectRef` is a question-local position, not a U-kind or union ValueKind: its value keeps the kind and identity rule supplied by its direct owner. A presentation carrier does not become a `U.Holon` by filling the position, and a transformation reference is filled only when A.3.4 independently accepts that same continuing referent as its changed subject. Before A.1 recognition, the exact disposition or blocker remains explicit and `actingSystemRef` stays unfilled. After recognition, `actingSystemRef` identifies that same acting-side entity under `U.System`; it does not introduce another actor. The participants may be parts of a larger holon and may be tightly coupled, but the acting position is not the changed position for that claim.

`ActingSideExternalization@Context` is a relation frame, not a U-kind, acting-system kind, record that acts, or evidence that change occurred. It names which direct owner governs each neighboring claim. Neither A.12 frame has a generic context, scope, or qualifier position. First ask what the qualifier changes. If it changes claim content, EntityOfConcern, or the effective reference scheme, C.2.1 identifies another episteme. If it selects whether one exact `U.ContextSlice` belongs to the set-valued applicability boundary of a claim, A.2.6 governs the exact `U.ClaimScope` and membership evaluation. Select a `BoundedModelUseStructure` under A.1.1 only when the receiving decision depends on the joint organization of one model edition's applicability, actual use in assigned Work, fixed-content expression coherence, exact applied constraints, and a complete selection-use frame. Otherwise state the exact condition, value, or relation under its direct owner. Do not copy a claim phrase or nearby participants into an A.12 field, and do not invent one umbrella qualifier object.

Use:

- `A.3.4` when `transformationRef` becomes current;
- `A.15` and `A.15.1` when method, work plan, work occurrence, or work success becomes current;
- `A.2.1` and `A.2.7` when role assignment or role relation becomes current;
- `A.10` when evidence or source independence becomes current;
- `A.1`, `A.14`, and `C.13` when holon identity, part-whole, or constructive grounding becomes current.

#### A.12:4.2 - Reflexive Split

For "self-" claims, do not accept the self-action wording directly. Recover one larger holon and two exact entity parts or subsystems inside it:

```text
ReflexiveSplit@Context:
  containingHolonRef: exact U.Holon
  actingPartOrSubsystemRef: exact U.Entity
  changedPartOrSubsystemRef: exact U.Entity
  holonDelimitationRelationRefs?: exact obtaining parthood relations to containingHolonRef
  holonBoundaryCrossingRelationRef?: one exact obtaining relation under its direct crossing-relation owner
  actingRoleAssignmentRef?: one exact obtaining U.RoleAssignment, only when a work-facing role claim is current
  transformationRef?
  methodRef?
  workOccurrenceRef?
  evidenceRelationRefs?
```

`ReflexiveSplit@Context` carries no system-recognition position. Its two part-or-subsystem fields identify exact entities, not phases, assignments, relation occurrences, or generic structures. Each filled entity position needs an independently obtaining parthood or subsystem relation to `containingHolonRef` under A.14 and the direct part-relation specialization.

When the acting-position entity must also be evaluated as a system, use a companion `ActingSideExternalization@Context`: its `actingEntityRef` identifies that exact `U.Entity`; its disposition or blocker remains explicit before recognition; and its optional `actingSystemRef` may identify the same entity only after A.1 recognition. Do not insert `actingSystemRef` or an A.1 disposition into `ReflexiveSplit@Context`.

A temporal phase, role assignment, parthood occurrence, software-module description, or other selected structure remains a separate object under its direct owner. A software component fills a part-or-subsystem field only when it is itself the exact entity and its direct part relation obtains. If a source supplies only unlike positions such as phases or assignments, state those direct relations and do not force them into this frame.

The minimal rule is:

```text
actingPartOrSubsystemRef != changedPartOrSubsystemRef
```

for the current change-bearing claim.

#### A.12:4.3 - Episteme And Publication Cases

An episteme does not act by itself. If a source says "the document updates itself", first recover the exact acting entity and decide which one of these different changed-object readings is current:

- **Carrier-change reading.** One exact publication file, representation carrier, or source-record carrier continues through a separately grounded change under its direct carrier identity rule. It may fill `changedSubjectRef` as that exact carrier, not as a `U.Holon` merely by carrier form; use A.3.4 only when the bounded change of that same referent is independently admitted.
- **Episteme-edition reading.** Changed claim content identifies another episteme, with the predecessor, successor, and exact edition relation governed separately. Do not call it transformation of one unchanged episteme.
- **Relation-occurrence reading.** One exact episteme-slot, reference, or publication-use relation obtains, ceases, or is replaced under its direct owner. The relation occurrence does not fill `changedSubjectRef`; if an actual change is also claimed, identify its continuing subject and A.3.4 facts separately.

Choose one reading before filling a singular field; never use a carrier, episteme, and relation occurrence as interchangeable values. Name the acting entity under `U.System` only after A.1 recognition, and fill a work-facing assignment only when one exact `U.RoleAssignment` obtains. Use `C.2.1`, `E.17`, `E.17.2`, source-use, publication-use, carrier, edition, and evidence owners for their own objects and relations. A.12 only prevents the sentence from assigning agency to the episteme.

#### A.12:4.4 - No Containing-Whole Inference From Interaction

A system changing another holon does not thereby become its part or the larger whole containing it. A manufacturing, teaching, measurement, repair, control, telemetry, or source-use case may contain separately governed boundary-crossing, transformation, work, evidence, or publication-use claims; none is a part-whole claim merely by wording, and A.12 makes none of them obtain.

Use part-whole owners only when parthood is independently admitted.

#### A.12:4.5 - No Self-Evidence Shortcut

A.12 separates the acting side; it does not make the acting side's own output sufficient evidence for success, safety, adequacy, or authorization.

When evidence matters, use `A.10` or the direct evidence and assurance owner. The evidence relation may use an observer system, measurement setup, independent source, audit record, or accepted stronger relation. A.12 only blocks the overread that acting and evidence are the same by default.

### A.12:5 - Archetypal Grounding (Worked Cases)

#### A.12:5.1 - Robot Self-Calibration

Source wording: "the robot calibrates itself."

Recovered A.12 use:

```text
ReflexiveSplit@RobotInternals:
  containingHolonRef: Robot-R17
  actingPartOrSubsystemRef: CalibrationController-R17
  changedPartOrSubsystemRef: SensorSuite-R17
  holonDelimitationRelationRefs: ComponentOf(CalibrationController-R17, Robot-R17); ComponentOf(SensorSuite-R17, Robot-R17), each independently obtaining under A.14

ActingSideExternalization@RobotCalibration:
  changedSubjectRef: SensorSuite-R17, the exact continuing U.Holon identified under A.1 for this claim
  actingEntityRef: CalibrationController-R17
  actingSystemRef: CalibrationController-R17, the same entity after A.1 recognizes it under U.System
  actingRoleAssignmentRef: CalibrationAssignment-R17, one obtaining work-facing U.RoleAssignment held by CalibrationController-R17
  transformationRef: SensorCalibrationTransformation-R17, independently admitted under A.3.4 as a bounded change of SensorSuite-R17
  workOccurrenceRef: CalibrationWork-R17, performed under CalibrationAssignment-R17 through F.6
  strongerOwnerRefs: A.1 identities of SensorSuite-R17 and CalibrationController-R17; A.14 part relations; A.2.1 CalibrationAssignment-R17; F.6 performed-under-assignment relation; A.3.4 SensorCalibrationTransformation-R17; A.15.1 CalibrationWork-R17
```

The robot remains the containing holon. The two `ComponentOf` occurrences make the internal entity positions explicit. The companion acting-side frame carries the same-entity A.1 reading and names an obtaining assignment, exact Work, and independently admitted transformation through their direct owners. The fact that the change occurs inside Robot-R17 does not remove the acting side.

#### A.12:5.2 - Document Cross-Reference Update

Source wording: "the document updates its cross-references."

This case chooses the carrier-change reading rather than combining it with an episteme-edition or relation-occurrence reading. It invokes no reusable FPF carrier-identity owner. Its bounded case-local rule treats `PublicationFile-17` as the same carrier only if the file object opened for the build still exists when the build closes, every write targets that same open object, and the build neither deletes and recreates the file, atomically replaces it, nor substitutes another carrier. E.24.PUB governs what publication form that carrier bears; it does not supply this carrier identity. If a continuity fact fails, identify a replacement carrier and do not assert a transformation of one continuing file; if carrier identity is unresolved, stop. A changed C.2.1 episteme discriminator selects the separate episteme-edition reading, not carrier continuity.

```text
ActingSideExternalization@DocumentBuild:
  changedSubjectRef: PublicationFile-17, the exact continuing U.PresentationCarrier reidentified by the bounded case-local continuity rule stated above
  actingEntityRef: BuildRunner-4
  actingSystemRef: BuildRunner-4, the same entity after A.1 recognizes it under U.System
  methodRef: CrossReferenceUpdateMethod-3, admitted under A.3.1
  methodDescriptionRef: BuildScriptEpisteme-9, admitted under A.3.2 as a description of CrossReferenceUpdateMethod-3
  actingRoleAssignmentRef: CrossReferenceUpdateAssignment-27, one obtaining work-facing U.RoleAssignment held by BuildRunner-4
  transformationRef: PublicationCarrierChange-27, independently admitted under A.3.4 from the build boundary, the before/during/after carrier-state facts below, and the bounded case-local continuity rule
  workOccurrenceRef: DocumentBuildWork-27, performed under CrossReferenceUpdateAssignment-27 through F.6
  evidenceRelationRefs: BuildLogEvidenceRelation-27, one exact A.10 evidence-provenance relation supporting the DocumentBuildWork-27 occurrence claim
  strongerOwnerRefs: E.24.PUB PublicationFormBearingRelation for the before/after bearing facts; bounded case-local PublicationFile-17 continuity rule, not E.24.PUB; A.1 recognition of BuildRunner-4; A.7 carrier/episteme distinction; A.3.1 CrossReferenceUpdateMethod-3; A.3.2 BuildScriptEpisteme-9; A.2.1 CrossReferenceUpdateAssignment-27; F.6 performed-under-assignment relation; A.3.4 PublicationCarrierChange-27; A.15.1 DocumentBuildWork-27; A.10 BuildLogEvidenceRelation-27
```

Before the boundary, exact `PublicationFormBearingRelation(PublicationFile-17, CrossReferencePublicationForm-26)` obtains and the borne form contains stale form-level link addresses. During the boundary, the same open file object remains in place while its link-address state is rewritten; the build log records no replacement event. After the boundary, exact `PublicationFormBearingRelation(PublicationFile-17, CrossReferencePublicationForm-27)` obtains and the borne form contains the refreshed addresses. Those facts, the build-open/build-close boundary, and the case-local continuity rule ground `PublicationCarrierChange-27` under A.3.4. They do not decide episteme identity: if claim content, EntityOfConcern, or the effective reference scheme changed, C.2.1 identifies another episteme and any historical continuation needs a separately governed edition relation.

The document does not act. The build script is the exact MethodDescription episteme in this case, not the acting entity or the Method by form. An episteme-edition case instead identifies predecessor and successor epistemes plus their exact edition relation. A reference-relation case instead identifies one exact relation occurrence and its direct governor. Each variant receives its own account; neither is inserted as an alternative value in this frame's singular fields.

#### A.12:5.3 - Lathe And Workpiece

Source wording: "the lathe makes the workpiece, so the workpiece belongs to the lathe during manufacturing."

Recovered A.12 use:

```text
ActingSideExternalization@Machining:
  changedSubjectRef: Workpiece-8, the exact continuing U.Holon identified under A.1 for this claim
  actingEntityRef: Lathe-3
  actingSystemRef: Lathe-3, the same entity after A.1 recognizes it under U.System
  actingRoleAssignmentRef: MachiningAssignment-8, one obtaining work-facing U.RoleAssignment held by Lathe-3
  transformationRef: MachiningTransformation-8, independently admitted under A.3.4 as a bounded change of Workpiece-8
  workOccurrenceRef: MachiningWork-8, performed under MachiningAssignment-8 through F.6
  strongerOwnerRefs: A.1 identities of Workpiece-8 and Lathe-3; A.2.1 MachiningAssignment-8; F.6 performed-under-assignment relation; A.3.4 MachiningTransformation-8; A.15.1 MachiningWork-8
```

`MachiningWork-8` and `MachiningTransformation-8` are independently identified; this account asserts no work-to-change relation between them. The additional sentence needed for a positive crossing claim is: "Lathe-3 transmits cutting force to Workpiece-8 during MachiningTransformation-8." No current direct pattern in this case supplies an admitted relation kind, obtaining predicate, applicability, and occurrence-identity rule for that sentence. Result: `A.6.RCD missing-governor[receiving use: decide whether this force-transfer claim supports a boundary-crossing explanation without a parthood inference; participants: Lathe-3 and Workpiece-8; missing owner: direct force-transfer or crossing relation]`; `holonBoundaryCrossingRelationRef` stays unfilled. Fixture, control, and material-removal claims would need their own exact participants and direct owners. Neither the independently identified Work nor transformation establishes parthood; use part-whole owners only for a separately supported part-whole claim.

### A.12:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Self-action convenience | "The system changed itself" hides the acting side and exact continuing changed subject. | Recover that changed subject under its direct identity owner and the exact acting-side entity, then state each direct relation used by the claim. |
| Episteme agency | A document, model, report, or source record is treated as acting. | Recover the exact acting entity first; only after A.1 recognition name that same entity under `U.System`, and add a role assignment only when the work-facing claim is current. Use episteme or publication owners for the changed object. |
| Containing-whole inference from interaction | A system that changes another holon is treated as that holon's containing whole. | Use boundary-crossing, transformation, work, evidence, or part-whole owners according to the exact current relation. |
| Self-evidence shortcut | The acting system's output is treated as sufficient evidence by default. | Return evidence and assurance claims to `A.10` or the direct owner. |

### A.12:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A12-1` | A self-action or passive change claim names one exact continuing changed subject under its direct identity owner and one exact proposed acting entity separately. `ActingSideExternalization@Context` requires `actingEntityRef`; before A.1 recognition it keeps the exact disposition or blocker and leaves `actingSystemRef` unfilled, and after recognition that optional position identifies the same entity under `U.System`. A filled `transformationRef` identifies an A.3.4 bounded change of that same `changedSubjectRef`. `ReflexiveSplit@Context` carries only acting and changed part positions; a companion acting-side frame carries this recognition boundary when needed. |
| `CC-A12-2` | A reflexive case identifies distinct exact entity parts or subsystems inside one containing holon, and each position has its independently obtaining direct part relation. Phases, assignments, relation occurrences, and generic structures stay with their direct owners. |
| `CC-A12-3` | A.12 does not create `U.Transformer`, `U.Boundary`, or `U.Interaction`. |
| `CC-A12-4` | Bounded transformation claims return to `A.3.4`; method and work claims return to `A.15` and `A.15.1`. |
| `CC-A12-5` | A role-assignment field is filled only by one exact obtaining work-facing `U.RoleAssignment`; any claim that exact Work was performed under it uses `F.6`. Role-relation claims return to `A.2.7`. |
| `CC-A12-6` | Evidence and assurance claims return to `A.10` or the direct evidence or assurance owner. |
| `CC-A12-7` | Episteme and publication cases do not assign agency to the episteme or publication form. |
| `CC-A12-8` | Changing another holon does not make it a part of the acting system. A filled singular crossing reference resolves one exact obtaining relation and its direct governor. If that governor is absent, the field stays unfilled and the account returns an exact `A.6.RCD missing-governor` naming the participants, needed sentence, and receiving use. Any containing-whole claim requires a separately admitted exact part-whole relation. |

### A.12:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Self-action literalism | "The system fixed itself" is accepted as one undivided claim. | Use `ReflexiveSplit@Context` and recover acting and changed positions. |
| Transformer kind inflation | The acting side is modeled as `U.Transformer`, as a special system kind, or as a provisional phrase placed in a `U.System` slot. | Before recognition retain the exact `U.Entity` and A.1 disposition or blocker and leave `actingSystemRef` unfilled. After recognition use the exact `U.System`; keep `TransformerRole@Context` only when its direct role owner and exact acting-side participation or assignment are current. |
| Boundary as object by word | Boundary or interaction words become durable root objects. | Use holon delimitation, boundary-crossing relation, transformation, signal, evidence, source-use, publication-use, or another direct owner. |
| Work success by action | Because a system acted, the work is treated as successful. | Use A.15.1 and evidence owners for performed work and success. |
| Evidence by producer | The acting system's own output is accepted as enough evidence. | Use A.10 or stronger evidence and assurance owners. |
| Manufacturing as containment | A tool or teacher changing another holon is treated as its containing whole. | Keep transformation and part-whole claims separate. |

### A.12:8 - Consequences

Positive consequences:

- Self-action claims become inspectable without denying real internal regulation.
- A.12 stays thin and does not duplicate transformation, method, work, role, evidence, or part-whole ontics.
- Epistemes and publications stop acting by wording.
- Internal control loops, build scripts, and automated changes become easier to audit.
- Manufacturing, teaching, measurement, repair, and control examples no longer imply holonic containment by default.

Costs:

- Compact "self-" sentences need unpacking before use.
- Some diagrams need one more internal distinction between acting and changed positions.
- Evidence cannot be accepted merely because the acting system produced a success message.

### A.12:9 - Rationale

Engineering and scientific models need a recoverable acting side for changes. Control, cybernetics, constructor-theory-style transformation talk, software automation, and assurance practice all penalize models where the same undivided object is cause, changed object, method, work occurrence, and evidence source.

FPF keeps that discipline without overbuilding A.12. The transformation ontic lives in `A.3.4`; method and work live in `A.15` and `A.15.1`; role assignment lives in `A.2.1` and `A.2.7`; evidence lives in `A.10`; part-whole admission lives in `A.1`, `A.14`, and `C.13`. A.12 only supplies the acting-side split needed before those owners can be used cleanly.

### A.12:10 - SoTA-Echoing

| Source family | Current lesson for A.12 | FPF decision |
| --- | --- | --- |
| Control and cybernetic regulation | Regulation becomes inspectable when controller, controlled object, feedback, and plant-like structure are not collapsed into one undivided object. | Reflexive split names acting and changed positions before control or feedback claims are used. |
| Constructor-theory-style transformation framing | A transformation claim needs a substrate or changed object, a possible transformation, and a constructor-like acting side without making the acting side a new root kind. | A.12 keeps the exact acting-side entity distinct, requires A.1 before any `U.System` reading of that entity, and returns bounded transformation to `A.3.4`. |
| Assurance and evidence practice | A produced result and evidence for the result are different claims. | A.12 blocks self-evidence shortcuts and returns evidence to `A.10` or stronger evidence owners. |
| Software and automation practice | Automated-change wording may mention systems, services, scripts, agents, or organizational arrangements; none of those words alone identifies the acting entity or proves systemhood. | Recover the exact acting entity, use that same entity under `U.System` only after A.1 recognition, keep scripts with method-description or representation owners unless a stronger direct claim obtains, and keep the changed object, Work occurrence, and evidence relation separate. |

### A.12:11 - Relations

- **Builds on:** `A.1` for holon and system admission, `A.2.1` for role assignment, `A.2.7` for role relation structure, and `A.3.4` for bounded transformation.
- **Coordinates with:** `A.10` for evidence, `A.14` and `C.13` for part-whole claims, `A.15` and `A.15.1` for method and work, `C.2.1` and `E.17` for episteme and publication cases, and `B.2.5` for supervisor-subholon feedback relation.
- **Does not own:** transformation occurrence evidence, work success, evidence independence, part-whole admission, MHT declaration, or the architecture of the larger holon.

### A.12:End

