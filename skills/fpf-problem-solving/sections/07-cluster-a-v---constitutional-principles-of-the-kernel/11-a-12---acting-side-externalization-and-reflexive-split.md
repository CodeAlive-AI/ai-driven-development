## A.12 - Acting-Side Externalization and Reflexive Split

> **Type:** Part A architectural ontology pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### A.12:0 - Use This When

Use this pattern when self-action or passive wording hides the acting participant or the subject claimed to change, or when interaction is mistaken for parthood.

Typical moments:

- "the robot calibrates itself";
- "the model updates itself";
- "the document refreshes its own cross-references";
- "the organization corrected itself";
- "the system verifies that its own change succeeded";
- "the lathe makes the workpiece, therefore the workpiece is part of the lathe during manufacturing".

**First useful move.** Name the proposed acting participant and the subject claimed to change, then state the relation between them that matters to your question. For the robot below, the calibration controller acts on the sensor suite. Use the precise account in §4.1 when you need to distinguish their identities or establish a particular System, change, Work or evidence claim; the ordinary acting-side distinction does not require constructing that frame.

**What goes wrong if missed.** A controller and controlled part can collapse into one object, an automated publication update can hide its performer, and the performer’s output can be mistaken for sufficient evidence of success. Changing another holon can also be mistaken for containing it.

**What this buys.** You can locate the acting participant, trace the claimed change, and ask separately what establishes the change or its success. When both participants are distinct parts of one holon, Reflexive Split exposes their internal relation.

**Not this pattern when.**

- If the current question is whether a bounded change occurred, use `A.3.4`.
- If the current question is whether work was performed or succeeded, use `A.15` and `A.15.1`.
- If the current question is an assignment occurrence, use `A.2.1`; if it is a relation among exact local system-role kinds, use `A.2.7`. For another participation relation, use the pattern that defines that relation.
- If the current question is evidence independence or source use, use `A.10` and the evidence-use or source-use patterns.
- If the current question is part-whole admission, use `A.1`, `A.14`, and `C.13`.

### A.12:1 - Problem Frame

Separate the acting and changed participants before deciding whether the claimed change, Work or evidence obtains. Their participation, System recognition and part-whole relations are separate questions. A self-action sentence may describe internal regulation; §4.2 gives the conditions for that reading.

### A.12:2 - Problem

Without A.12:

1. **Self-action hides the acting side.** "The system changed itself" leaves unclear who acts, what changes, and which participation relation is asserted.
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
| Episteme use vs episteme agency | A carrier update, another episteme edition and a changed publication relation need different identity tests (§4.3). A Work performer or `U.SystemRoleAssignment` holder must be an admitted `U.System`. |
| Boundary crossing vs parthood | When an exact boundary-crossing relation independently satisfies the predicate, applicability, and identity rules that define it, it does not thereby make the acting system a part of the changed holon or the larger whole containing it. Without those rules, keep the crossing claim open rather than inferring either crossing or parthood. |

### A.12:4 - Solution

Separate the acting participant from the subject claimed to change. Add the precise claims needed to explain the case.

#### A.12:4.1 - Acting-Side Externalization

When a precise change-bearing account is needed, use the following frame to distinguish the participants and the claims you are making. It is not a required form for an ordinary acting-side explanation. Fill a neighboring-claim position only when that claim is needed and its own admission conditions hold:

```text
ActingSideExternalization@Context:
  changedSubjectRef: one exact continuing referent identified by the identity rule that defines that referent
  actingEntityRef: exact U.Entity proposed for the acting side
  actingSystemRef?: U.System, fill only after actingEntityRef satisfies the complete A.1 U.System criterion
  a1RecognitionDispositionOrBlockerRef?: required while actingSystemRef is unfilled
  actingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, only when one exact obtaining work-facing assignment is current
  actingSideParticipationRef?: one exact obtaining relation occurrence satisfying the predicate and participant meanings that define the participation, causal, or interaction claim
  transformationRef?: U.Transformation, fill only when A.3.4 identifies a bounded change of changedSubjectRef
  methodRef?
  methodDescriptionRef?
  workPlanRef?
  workOccurrenceRef?
  holonBoundaryCrossingRelationRef?: one exact obtaining relation occurrence satisfying the predicate, applicability, and identity rules that define the crossing relation
  evidenceRelationRefs?
  strongerOwnerRefs:
```

Identify `actingEntityRef` and `changedSubjectRef` as distinct participants in the claim. `changedSubjectRef` is a question-local position, not a U-kind or union ValueKind: its value retains its independently admitted kind and identity rule. A presentation carrier does not become a `U.Holon` by filling it. Fill `transformationRef` only when A.3.4 establishes a bounded change of that same continuing referent.

Before calling the acting entity a `U.System`, apply the complete A.1 criterion. Until recognition is established, retain the entity and its `recognized | rejected | unknown` disposition or blocker, and leave `actingSystemRef` unfilled. Once recognized, that position names the same entity under `U.System`, not another actor. Tight coupling or membership in a larger holon does not merge the acting and changed positions.

`ActingSideExternalization@Context` describes the relation frame; it does not define a U-kind or establish that a change occurred. Each neighboring claim has its own participants and defining or testing rule. Neither A.12 frame has a generic context, scope or qualifier position. Ask what the proposed qualifier changes:

- If claim content, EntityOfConcern or the effective reference scheme changes, C.2.1 identifies another episteme.
- If the question is whether a `U.ContextSlice` belongs to a claim’s set-valued applicability boundary, use A.2.6’s `U.ClaimScope` and membership evaluation.
- Select A.1.1’s `BoundedModelUseStructure` only when the decision depends jointly on one model edition’s applicability, actual use in assigned Work, fixed-content expression coherence, applied constraints and complete selection-use frame.

For another condition, state the condition or relation and apply its defining or testing rule. A pattern citation is usually enough to locate that rule. Recover its identity-bearing defining or constraining ClaimGraph only when the graph’s identity changes interpretation, comparison, migration, conflict, publication or reuse. A claim phrase or nearby participant does not fill an A.12 field unless it satisfies that field’s meaning.

Use:

- `A.3.4` when `transformationRef` becomes current;
- `A.15` and `A.15.1` when method, work plan, work occurrence or work success is claimed; for an actual Work occurrence, follow the performer/admission/attribution order below;
- `A.2.1` when an exact assignment occurrence becomes current, and `A.2.7` only when a relation among exact local system-role kinds becomes current;
- `A.10` when evidence or source independence becomes current;
- `A.1`, `A.14`, and `C.13` when holon identity, part-whole, or constructive grounding becomes current.

For a dated Work claim, first establish each actual performer’s A.13 core: an admitted System, a local agential system-role kind and criterion it satisfies, an obtaining assignment, and the scope, situation and window the use needs, supported by evidence. Add an agency-characteristic profile only for a consumed Grade/autonomy/profile claim, a characteristic-dependent local criterion, or an assurance use that requires it. Then admit the occurrence independently under A.15.1 from its performance history, enacted Method, temporal extent and obtaining containing-System relation. Only if precise assignment-bound attribution is also claimed does F.6 relate that admitted Work to the same obtaining assignment. A Work-only account stops after admission.

#### A.12:4.2 - Reflexive Split

Use Reflexive Split when the acting and changed participants are two distinct entity parts or subsystems of one containing holon, with an independently obtaining part relation for each. Establish those premises before using this frame; the word "self-" alone does not establish them. If the source supports another reading, keep that acting-side or relation account and leave any unsupported internal-parts claim open.

```text
ReflexiveSplit@Context:
  containingHolonRef: exact U.Holon
  actingPartOrSubsystemRef: exact U.Entity
  changedPartOrSubsystemRef: exact U.Entity
  holonDelimitationRelationRefs?: exact obtaining parthood relations to containingHolonRef
  holonBoundaryCrossingRelationRef?: one exact obtaining relation satisfying the predicate, applicability, and identity rules that define the crossing relation
  actingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, only when one exact obtaining work-facing assignment is current
  transformationRef?
  methodRef?
  workOccurrenceRef?
  evidenceRelationRefs?
```

`ReflexiveSplit@Context` carries no system-recognition position. Its two part-or-subsystem fields identify exact entities, not phases, assignments, relation occurrences, or generic structures. Each filled entity position needs an independently obtaining parthood or subsystem relation to `containingHolonRef` under A.14 and the direct part-relation specialization.

When the acting-position entity must also be evaluated as a system, use a companion `ActingSideExternalization@Context`: its `actingEntityRef` identifies that exact `U.Entity`; its disposition or blocker remains explicit before recognition; and its optional `actingSystemRef` may identify the same entity only after A.1 recognition. Do not insert `actingSystemRef` or an A.1 disposition into `ReflexiveSplit@Context`.

A temporal phase, system-role assignment, parthood occurrence, software-module description, or selected structure remains a separate object under the identity and relation rules that define it. A software component fills a part-or-subsystem field only when it is itself the exact entity and its direct part relation obtains. If a source supplies only unlike positions such as phases or assignments, state those direct relations and do not force them into this frame.

The minimal rule is:

```text
actingPartOrSubsystemRef != changedPartOrSubsystemRef
```

for the current change-bearing claim.

#### A.12:4.3 - Episteme And Publication Cases

If a source says "the document updates itself", identify the acting participant and decide which changed-object reading the claim needs:

- **Carrier-change reading.** One exact publication file, representation carrier, or source-record carrier continues through a separately grounded change under its direct carrier identity rule. It may fill `changedSubjectRef` as that exact carrier, not as a `U.Holon` merely by carrier form; use A.3.4 only when the bounded change of that same referent is independently admitted.
- **Episteme-edition reading.** Changed claim content identifies another episteme, with the predecessor, successor, and exact edition relation governed separately. Do not call it transformation of one unchanged episteme.
- **Relation-occurrence reading.** One exact episteme-related direct relation—for example constitution, empirical grounding, edition, reference, or publication use—obtains when its actual participants satisfy its direct predicate. Its direct identity and change rules determine whether that occurrence continues, ceases, or is replaced. Use C.2.1 for episteme identity and edition distinctions and E.17 or E.24.PUB for publication use. The relation occurrence does not fill `changedSubjectRef`; if an actual change is also claimed, identify its continuing subject and A.3.4 facts separately.

Choose the reading before filling a singular field; carriers, epistemes and relation occurrences are not interchangeable values. Call the acting entity a `U.System` only after A.1 recognition, and fill a work-facing assignment only when that `U.SystemRoleAssignment` obtains. Use C.2.1 for episteme identity, E.17/E.17.2 for publication relations and E.24.PUB for the publication-form boundary when those claims are needed.

#### A.12:4.4 - No Containing-Whole Inference From Interaction

Treat the interaction and part-whole claims separately. A system changing another holon does not thereby become its part or the larger whole containing it.

For a part-whole claim, use A.14 or the rule defining the exact part-whole predicate to test parthood independently of the interaction claim.

#### A.12:4.5 - No Self-Evidence Shortcut

A producer’s output does not automatically establish a claim of success, safety, adequacy or authorization. State the claim you need to support, then use A.10 to identify its evidence and provenance. The producer’s output may contribute when that evidence relation supports the claim.

Use B.3 when a separate assurance conclusion is requested. Introduce an observer, measurement setup or independent source only when its contribution matters to the evidence account.

### A.12:5 - Archetypal Grounding (Worked Cases)

#### A.12:5.1 - Robot Self-Calibration

Source wording: "the robot calibrates itself."

CalibrationController-R17 acts on SensorSuite-R17; both are parts of Robot-R17. The precise account below takes their A.1 recognition and two independently obtaining A.14 `ComponentOf` relations as premises, then distinguishes performer admission, Work, attribution and change:

```text
ReflexiveSplit@RobotInternals:
  containingHolonRef: Robot-R17
  actingPartOrSubsystemRef: CalibrationController-R17
  changedPartOrSubsystemRef: SensorSuite-R17
  holonDelimitationRelationRefs: ComponentOf(CalibrationController-R17, Robot-R17); ComponentOf(SensorSuite-R17, Robot-R17), each independently obtaining under A.14

ActingSideExternalization@RobotCalibration:
  changedSubjectRef: SensorSuite-R17, the exact continuing U.Holon identified under A.1 for this claim
  actingEntityRef: CalibrationController-R17
  actingSystemRef: CalibrationController-R17, the same entity after it satisfies the complete A.1 U.System criterion
  actingSystemA13CoreRef: A.13 core for CalibrationController-R17 as precise performer in this action, including CalibrationAssignment-R17 as the same obtaining assignment
  actingSystemRoleAssignmentRef: CalibrationAssignment-R17, one obtaining work-facing U.SystemRoleAssignment held by CalibrationController-R17
  transformationRef: SensorCalibrationTransformation-R17, independently admitted under A.3.4 as a bounded change of SensorSuite-R17
  workOccurrenceRef: CalibrationWork-R17, independently admitted under A.15.1 from its performance history, enacted Method, temporal extent, and containing-System relation; because this case claims exact assignment-bound attribution, F.6 afterward relates the already admitted Work to CalibrationAssignment-R17
  strongerOwnerRefs: A.1 identities of SensorSuite-R17 and CalibrationController-R17; A.14 part relations; A.13 performer core including A.2.1 CalibrationAssignment-R17; A.15.1 CalibrationWork-R17; F.6 performed-under-assignment relation; A.3.4 SensorCalibrationTransformation-R17
```

Robot-R17 remains the containing holon. CalibrationWork-R17 and SensorCalibrationTransformation-R17 are separate admitted objects. The A.13 core includes CalibrationAssignment-R17; after independent A.15.1 Work admission, this case’s additional F.6 attribution uses that same obtaining assignment. The references name the admissions used by the example; each admission still needs its stated basis.

#### A.12:5.2 - Document Cross-Reference Update

Source wording: "the document updates its cross-references."

BuildRunner-4 updates the cross-references in PublicationFile-17. BuildScriptEpisteme-9 describes CrossReferenceUpdateMethod-3 under A.3.2; the script is the MethodDescription, not the acting entity or the Method merely by its form. This case follows the publication carrier through the update.

The bounded case-local continuity rule treats PublicationFile-17 as the same carrier only if the file object opened for the build still exists when the build closes, every write asserted to update PublicationFile-17 targets that same open object, and the build neither deletes and recreates that file, atomically replaces it, nor substitutes another carrier. E.24.PUB states which publication form the carrier bears; it does not supply this case-local identity rule. If a continuity fact fails, identify the replacement carrier rather than asserting a transformation of one continuing file. If carrier identity is unresolved, stop before asserting that change. A changed C.2.1 episteme discriminator selects the separate episteme-edition reading.

```text
ActingSideExternalization@DocumentBuild:
  changedSubjectRef: PublicationFile-17, the exact continuing U.PresentationCarrier reidentified by the bounded case-local continuity rule stated above
  actingEntityRef: BuildRunner-4
  actingSystemRef: BuildRunner-4, the same entity after it satisfies the complete A.1 U.System criterion
  actingSystemA13CoreRef: A.13 core for BuildRunner-4 as precise performer in this action, including CrossReferenceUpdateAssignment-27 as the same obtaining assignment
  methodRef: CrossReferenceUpdateMethod-3, admitted under A.3.1
  methodDescriptionRef: BuildScriptEpisteme-9, admitted under A.3.2 as a description of CrossReferenceUpdateMethod-3
  actingSystemRoleAssignmentRef: CrossReferenceUpdateAssignment-27, one obtaining work-facing U.SystemRoleAssignment held by BuildRunner-4
  transformationRef: PublicationCarrierChange-27, independently admitted under A.3.4 from the build boundary, the before/during/after carrier-state facts below, and the bounded case-local continuity rule
  workOccurrenceRef: DocumentBuildWork-27, independently admitted under A.15.1 from its performance history, enacted CrossReferenceUpdateMethod-3, temporal extent, and containing-System relation; because this case claims exact assignment-bound attribution, F.6 afterward relates the already admitted Work to CrossReferenceUpdateAssignment-27
  evidenceRelationRefs: BuildLogEvidenceRelation-27, one exact A.10 evidence-provenance relation supporting the DocumentBuildWork-27 occurrence claim
  strongerOwnerRefs: E.24.PUB PublicationFormBearingRelation for the before/after bearing facts; bounded case-local PublicationFile-17 continuity rule, not E.24.PUB; A.1 recognition of BuildRunner-4; A.13 performer core including A.2.1 CrossReferenceUpdateAssignment-27; A.15.1 DocumentBuildWork-27; F.6 performed-under-assignment relation; A.7 carrier/episteme distinction; A.3.1 CrossReferenceUpdateMethod-3; A.3.2 BuildScriptEpisteme-9; A.3.4 PublicationCarrierChange-27; A.10 BuildLogEvidenceRelation-27
```

Before the boundary, exact `PublicationFormBearingRelation(PublicationFile-17, CrossReferencePublicationForm-26)` obtains and the borne form contains stale form-level link addresses. During the boundary, the same open file object remains in place while its link-address state is rewritten; the build log records no replacement event. After the boundary, exact `PublicationFormBearingRelation(PublicationFile-17, CrossReferencePublicationForm-27)` obtains and the borne form contains the refreshed addresses. Those facts, the build-open/build-close boundary, and the case-local continuity rule ground `PublicationCarrierChange-27` under A.3.4. They do not decide episteme identity: if claim content, EntityOfConcern, or the effective reference scheme changed, C.2.1 identifies another episteme and any historical continuation needs a separately governed edition relation.

An episteme-edition case instead identifies predecessor and successor epistemes plus their edition relation. A reference-relation case identifies one relation occurrence and its defining rule. Keep those accounts separate from the carrier-change case; they are not alternative values for its singular fields.

#### A.12:5.3 - Lathe And Workpiece

Source wording: "the lathe makes the workpiece, so the workpiece belongs to the lathe during manufacturing."

Lathe-3 is the acting participant; Workpiece-8 is the changed subject. That distinction does not establish that Workpiece-8 is part of Lathe-3. Test any such parthood claim independently under A.14 or its defining part-whole rule. The precise account separates the admitted Work and change:

```text
ActingSideExternalization@Machining:
  changedSubjectRef: Workpiece-8, the exact continuing U.Holon identified under A.1 for this claim
  actingEntityRef: Lathe-3
  actingSystemRef: Lathe-3, the same entity after it satisfies the complete A.1 U.System criterion
  actingSystemA13CoreRef: A.13 core for Lathe-3 as precise performer in this action, including MachiningAssignment-8 as the same obtaining assignment
  actingSystemRoleAssignmentRef: MachiningAssignment-8, one obtaining work-facing U.SystemRoleAssignment held by Lathe-3
  transformationRef: MachiningTransformation-8, independently admitted under A.3.4 as a bounded change of Workpiece-8
  workOccurrenceRef: MachiningWork-8, independently admitted under A.15.1 from its performance history, enacted Method, temporal extent, and containing-System relation; because this case claims exact assignment-bound attribution, F.6 afterward relates the already admitted Work to MachiningAssignment-8
  strongerOwnerRefs: A.1 identities of Workpiece-8 and Lathe-3; A.13 performer core including A.2.1 MachiningAssignment-8; A.15.1 MachiningWork-8; F.6 performed-under-assignment relation; A.3.4 MachiningTransformation-8
```

`MachiningWork-8` and `MachiningTransformation-8` are independently identified; this account asserts no Work-to-change relation between them.

The additional proposed claim is: "Lathe-3 transmits cutting force to Workpiece-8 during MachiningTransformation-8." To decide whether it supports a boundary-crossing explanation, a defining rule must supply the force-transfer or crossing relation kind, obtaining predicate, applicability and occurrence identity. This case supplies no such rule: that is its A.6.RCD `missing-governor`, and `holonBoundaryCrossingRelationRef` stays unfilled. The missing rule leaves this extension open; the acting/changed distinction remains usable and parthood still requires its own test.

### A.12:5.4 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Self-action convenience | "The system changed itself" hides the acting side and exact continuing changed subject. | Recover that changed subject by the identity rule that defines it, identify the acting-side entity, and then state each direct relation used by the claim. |
| Episteme agency | A document, model, report or source record is treated as acting. | Identify the acting entity; apply A.1 if Systemhood is claimed and §4.1’s admission order if Work is claimed. Keep C.2.1 episteme identity and E.17/E.24.PUB publication claims separate. |
| Containing-whole inference from interaction | A system that changes another holon is treated as that holon’s containing whole. | Test parthood independently under A.14 or C.13. §5.3 shows how the acting-side account remains usable while a crossing claim is open. |
| Self-evidence shortcut | The acting system’s output is treated as sufficient evidence by default. | Apply §4.5’s claim-first evidence question; add B.3 only for an assurance conclusion. |

### A.12:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A12-1` | A self-action or passive change account names the proposed acting participant and changed subject separately. When the precise frame is used, it identifies one exact continuing `changedSubjectRef` by that referent’s identity rule and requires `actingEntityRef`; before A.1 recognition it keeps the exact disposition or blocker and leaves `actingSystemRef` unfilled, and after recognition that optional position identifies the same entity under `U.System`. A filled `transformationRef` identifies an A.3.4 bounded change of that same `changedSubjectRef`. `ReflexiveSplit@Context` carries only acting and changed part positions; a companion acting-side frame carries this recognition boundary when needed. |
| `CC-A12-2` | A Reflexive Split case identifies distinct exact entity parts or subsystems inside one containing holon, and each position has its independently obtaining direct part relation. Temporal phases keep their phase identity rules; assignments use A.2.1; parthood uses A.14 or the exact part-relation rule; descriptions use C.2.1; selected structures use A.22. None fills an A.12 part position merely by being nearby. |
| `CC-A12-3` | A.12 does not create `U.Transformer`, `U.Boundary`, or `U.Interaction`. |
| `CC-A12-4` | Bounded transformation claims require `A.3.4`; method and work claims require `A.15` and `A.15.1`. For an actual Work claim, establish each performer’s A.13 core before independent A.15.1 occurrence admission. The profile is conditional as stated in §4.1. |
| `CC-A12-5` | A system-role-assignment field is filled only by one exact obtaining work-facing `U.SystemRoleAssignment`; any claim that exact Work was performed under it uses `F.6`. System-role-kind relation claims require `A.2.7`. |
| `CC-A12-6` | Evidence and source-use claims use A.10's direct relations; a separately current assurance conclusion uses B.3. |
| `CC-A12-7` | Episteme and publication cases do not assign agency to the episteme or publication form. |
| `CC-A12-8` | Changing another holon does not make it a part of the acting system. A filled singular crossing reference resolves one exact obtaining relation and its defining rule. If that rule is absent, leave the field unfilled and state the A.6.RCD `missing-governor` problem: the participants, needed sentence and receiving use. An ordinary explanation is enough; no additional record is required. Any containing-whole claim requires a separately admitted exact part-whole relation. |

### A.12:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Self-action literalism | "The system fixed itself" is accepted as one undivided claim. | Identify the acting and changed participants. Use `ReflexiveSplit@Context` only when §4.2’s two-entity-part and one-holon conditions hold. |
| Transformer kind inflation | The acting side is modeled as `U.Transformer`, as a special system kind, or as a provisional phrase placed in a `U.System` slot. | Before recognition retain the exact `U.Entity` and A.1 disposition or blocker and leave `actingSystemRef` unfilled. After recognition use the exact `U.System`. Add a local `TransformerSystemRole` classification only after C.3 recovers that kind from its system-candidate domain, work-facing membership distinction, member/non-member boundary, and continuity rule. Add acting-side participation or an assignment separately only when that exact relation is current. |
| Boundary as object by word | Boundary or interaction words become durable root objects. | Identify the relation actually claimed: holon delimitation, boundary crossing, transformation, signaling, evidence, source use or publication use. Apply its defining or testing rule; §4.1 gives the condition for recovering an identity-bearing ClaimGraph. |
| Work success by action | Because a system acted, the work is treated as successful. | Use A.15.1 and evidence-use patterns for performed work and success. |
| Evidence by producer | The acting system’s own output is accepted as enough evidence. | Use §4.5 to identify which claim the output supports under A.10. |
| Manufacturing as containment | A tool or teacher changing another holon is treated as its containing whole. | Keep transformation and part-whole claims separate. |

### A.12:8 - Consequences

Positive consequences:

- Self-action claims become inspectable without denying real internal regulation.
- Transformation, Work, assignment and evidence claims can be tested separately.
- An automated publication update identifies its performer separately from the script and changed content.
- Internal control loops and automated changes can be traced through their acting and changed participants.
- Interaction cases retain a separate parthood question.

Costs:

- When the acting/changed distinction matters, a compact "self-" sentence needs unpacking.
- Some diagrams need one more internal distinction between acting and changed positions.
- Supporting a success or safety claim can require evidence beyond the producer’s success message.

### A.12:9 - Rationale

The acting/changed distinction helps trace an internal control loop, locate the performer of an automated update and separate a produced result from the evidence supporting a claim about it. Those questions can require different admissions; §4.1 gives their conditional routes.

### A.12:10 - SoTA-Echoing

| Source or practice | Contribution to the distinction | FPF use |
| --- | --- | --- |
| Control practice | Distinguishing controller, controlled object, feedback and plant structure helps inspect regulation. | Use Reflexive Split for internal regulation when the two-entity-part and one-holon conditions hold. |
| [Constructor theory: introductory account](https://www.constructortheory.org/what-is-constructor-theory/) | A substrate undergoes a specified possible task; a constructor retains the capacity to perform the task again. | Keep the changed substrate and proposed acting entity distinct. FPF separately requires A.1 for a System claim and A.3.4 for a bounded change claim. |
| Assurance and evidence practice | A produced result and evidence supporting a claim about it are different objects. | Use A.10 for the claim’s evidence and provenance; use B.3 when an assurance conclusion is requested. |
| Software and automation practice | An automated-update sentence can hide the distinction between the executing entity, script and changed object. | Identify the acting entity and apply A.1 before calling it a System. Apply A.3.2 before treating the script as a MethodDescription; keep change, Work and evidence claims separate. |

### A.12:11 - Relations

- **Builds on:** `A.1` for holon and System admission, `A.2.1` for a directly declared assignment species and its obtaining occurrence, `A.2.7` for relations among exact local system-role kinds, and `A.3.4` for bounded transformation.
- **Coordinates with:** `A.10` for evidence, `A.14` and `C.13` for part-whole claims, `A.15` and `A.15.1` for method and work, `C.2.1` and `E.17` for episteme and publication cases, and `B.2.5` for supervisor-subholon feedback relation.
- **Does not own:** transformation occurrence evidence, work success, evidence independence, part-whole admission, MHT declaration, or the architecture of the larger holon.

### A.12:End
