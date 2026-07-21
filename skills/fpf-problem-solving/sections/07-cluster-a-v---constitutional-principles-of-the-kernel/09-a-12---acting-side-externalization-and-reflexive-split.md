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

**First useful move.** Separate the changed holon from the acting system or candidate acting system. Then use the direct owner for the current claim: `A.3.4` for bounded transformation, `A.15` and `A.15.1` for method and work, `A.2.1` and `A.2.7` for role assignment and role relations, `A.10` for evidence, and `A.1`, `A.14`, or `C.13` for holon and part-whole claims.

**What goes wrong if missed.** A system becomes its own cause, a document acts, a controller and controlled part collapse into one object, evidence becomes self-certifying, and a system that changes another holon is mistaken for that holon's super-holon.

**What this buys.** Self-action wording becomes a reviewable relation among a changed holon, an acting system in role, method or work claims when current, boundary-crossing relation when current, and evidence when current.

**Not this pattern when.**

- If the current question is whether a bounded change occurred, use `A.3.4`.
- If the current question is whether work was performed or succeeded, use `A.15` and `A.15.1`.
- If the current question is the role assignment or role relation, use `A.2.1` and `A.2.7`.
- If the current question is evidence independence or source use, use `A.10` and the evidence or source-use owners.
- If the current question is part-whole admission, use `A.1`, `A.14`, and `C.13`.

### A.12:1 - Problem Frame

A.12 keeps a causality-facing modeling discipline without creating a second transformation ontology.

The pattern does not say that every change is already established, that work succeeded, that the acting system is a special `U.Transformer` kind, or that boundary wording creates a durable boundary object. It says only this: when a claim depends on a change, the acting side and the changed holon must be recoverable as distinct slot fillers for that claim. When ordinary language says "self-", split the larger holon into acting and changed positions before using transformation, method, work, evidence, or part-whole patterns.

### A.12:2 - Problem

Without A.12:

1. **Self-action hides the acting side.** "The system changed itself" does not say which system in role changed which holon under which conditions.
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
| Episteme use vs episteme agency | Epistemes can be changed, published, cited, or used, but acting belongs to systems in role. |
| Boundary crossing vs parthood | A system can act on another holon across a boundary-crossing relation without becoming its super-holon. |

### A.12:4 - Solution

Use A.12 as a thin acting-side pattern.

#### A.12:4.1 - Acting-Side Externalization

For a change-bearing claim, recover this relation frame before relying on self-action wording:

```text
ActingSideExternalization@Context:
  changedHolonRef:
  actingSystemRef: U.System or candidate acting system admitted by direct pattern
  actingRoleAssignmentRef:
  boundedContextRef:
  transformationRef?: U.Transformation
  methodRef?
  methodDescriptionRef?
  workPlanRef?
  workOccurrenceRef?
  holonBoundaryCrossingRelationRef?
  evidenceRelationRefs?
  strongerOwnerRefs:
```

The acting system and the changed holon are distinct slot fillers for the current change-bearing claim. They may be parts of a larger holon, and they may be tightly coupled, but the acting position is not the changed position for that claim.

`ActingSideExternalization@Context` is a relation frame, not a U-kind, acting-system kind, record that acts, or evidence that change occurred. It names which direct owner governs each neighboring claim.

Use:

- `A.3.4` when `transformationRef` becomes current;
- `A.15` and `A.15.1` when method, work plan, work occurrence, or work success becomes current;
- `A.2.1` and `A.2.7` when role assignment or role relation becomes current;
- `A.10` when evidence or source independence becomes current;
- `A.1`, `A.14`, and `C.13` when holon identity, part-whole, or constructive grounding becomes current.

#### A.12:4.2 - Reflexive Split

For "self-" claims, do not accept the self-action wording directly. Recover a larger holon and at least two distinct positions inside it:

```text
ReflexiveSplit@Context:
  containingHolonRef:
  actingPartOrSubsystemRef:
  changedPartOrSubsystemRef:
  boundedContextRef:
  holonDelimitationRelationRefs?
  holonBoundaryCrossingRelationRef?
  actingRoleAssignmentRef?
  transformationRef?
  methodRef?
  workOccurrenceRef?
  evidenceRelationRefs?
```

The split is a modeling move, not a claim that the two positions are always permanent physical modules. They can be stable subsystems, temporal phases, organizational assignments, software components, or another directly governed structure. If the split relies on parthood, use A.14 and C.13. If it relies on role assignment, use A.2.1 and A.2.7. If it relies on temporal phases, use the temporal owner.

The minimal rule is:

```text
actingPartOrSubsystemRef != changedPartOrSubsystemRef
```

for the current change-bearing claim.

#### A.12:4.3 - Episteme And Publication Cases

An episteme does not act by itself. If a source says "the document updates itself", recover the acting system in role and the object that changed:

- a publication file or representation changed;
- a source record changed;
- an episteme slot relation changed;
- a claim relation, reference relation, or publication-use relation changed.

Use `C.2.1`, `E.17`, `E.17.2`, source-use, publication-use, and evidence owners for the episteme or publication side. A.12 only prevents the sentence from assigning agency to the episteme.

#### A.12:4.4 - No Super-Holon Inference

A system changing another holon does not become that holon's super-holon. Manufacturing, teaching, measurement, repair, control, telemetry, or source use can be boundary-crossing, transformation, work, evidence, or publication-use relations without being part-whole relations.

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
  containingHolonRef: Robot R17
  actingPartOrSubsystemRef: CalibrationController
  changedPartOrSubsystemRef: SensorSuite
  actingRoleAssignmentRef: CalibrationController as calibration acting system
  transformationRef: sensor calibration change, if A.3.4 is current
  workOccurrenceRef: calibration run, if A.15.1 is current
```

The robot may remain the containing holon. The calibration controller and sensor suite are distinct positions for the current claim. The fact that the change occurs inside the robot does not remove the acting side.

#### A.12:5.2 - Document Cross-Reference Update

Source wording: "the document updates its cross-references."

Recovered A.12 use:

```text
ActingSideExternalization@DocumentBuild:
  changedHolonRef: publication file or episteme slot relation under direct owner
  actingSystemRef: build script or editing system
  actingRoleAssignmentRef: cross-reference update role in DocumentBuild
  workOccurrenceRef: build run, if A.15.1 is current
  evidenceRelationRefs: build log, diff, validation check, or stronger evidence owner
```

The document does not act. If the changed object is a publication form, use publication owners. If the changed object is a claim-bearing episteme relation, use episteme owners.

#### A.12:5.3 - Lathe And Workpiece

Source wording: "the lathe makes the workpiece, so the workpiece belongs to the lathe during manufacturing."

Recovered A.12 use:

```text
ActingSideExternalization@Machining:
  changedHolonRef: workpiece
  actingSystemRef: lathe
  actingRoleAssignmentRef: machining acting system
  transformationRef: bounded machining transformation, if A.3.4 is current
  workOccurrenceRef: machining work occurrence, if A.15.1 is current
  holonBoundaryCrossingRelationRef: cutting force, fixture relation, control relation, or material-removal relation under direct owner
```

The lathe can transform the workpiece without being the workpiece's super-holon. Use part-whole owners only if the workpiece is independently admitted as part of a containing holon.

### A.12:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Self-action convenience | "The system changed itself" hides the acting side and changed holon. | Recover distinct slot fillers for the current claim. |
| Episteme agency | A document, model, report, or source record is treated as acting. | Name the acting system in role and use episteme or publication owners for the changed object. |
| Super-holon inference | A system that changes another holon is treated as that holon's containing whole. | Use boundary-crossing, transformation, work, evidence, or part-whole owners according to the current relation. |
| Self-evidence shortcut | The acting system's output is treated as sufficient evidence by default. | Return evidence and assurance claims to `A.10` or the direct owner. |

### A.12:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A12-1` | A self-action or passive change claim names the changed holon and the acting system or candidate acting system separately. |
| `CC-A12-2` | A reflexive case uses distinct acting and changed positions inside a containing holon for the current claim. |
| `CC-A12-3` | A.12 does not create `U.Transformer`, `U.Boundary`, or `U.Interaction`. |
| `CC-A12-4` | Bounded transformation claims return to `A.3.4`; method and work claims return to `A.15` and `A.15.1`. |
| `CC-A12-5` | Role assignment and role-relation claims return to `A.2.1` and `A.2.7`. |
| `CC-A12-6` | Evidence and assurance claims return to `A.10` or the direct evidence or assurance owner. |
| `CC-A12-7` | Episteme and publication cases do not assign agency to the episteme or publication form. |
| `CC-A12-8` | A system changing another holon is not treated as that holon's super-holon unless a separate part-whole relation is admitted. |

### A.12:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Self-action literalism | "The system fixed itself" is accepted as one undivided claim. | Use `ReflexiveSplit@Context` and recover acting and changed positions. |
| Transformer kind inflation | The acting side is modeled as `U.Transformer` or as a special system kind. | Keep `TransformerRole@Context` as role value or role assignment material under direct owners; the acting holder remains a system or candidate acting system. |
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
| Constructor-theory-style transformation framing | A transformation claim needs a substrate or changed object, a possible transformation, and a constructor-like acting side without making the acting side a new root kind. | A.12 keeps the acting system distinct and returns bounded transformation to `A.3.4`. |
| Assurance and evidence practice | A produced result and evidence for the result are different claims. | A.12 blocks self-evidence shortcuts and returns evidence to `A.10` or stronger evidence owners. |
| Software and automation practice | Automated changes are still performed by concrete systems, services, scripts, agents, or organizational arrangements. | Document and model update examples recover the acting system, changed object, work occurrence, and evidence relation separately. |

### A.12:11 - Relations

- **Builds on:** `A.1` for holon and system admission, `A.2.1` for role assignment, `A.2.7` for role relation structure, and `A.3.4` for bounded transformation.
- **Coordinates with:** `A.10` for evidence, `A.14` and `C.13` for part-whole claims, `A.15` and `A.15.1` for method and work, `C.2.1` and `E.17` for episteme and publication cases, and `B.2.5` for supervisor-subholon feedback relation.
- **Does not own:** transformation occurrence evidence, work success, evidence independence, part-whole admission, MHT declaration, or the architecture of the larger holon.

### A.12:End

