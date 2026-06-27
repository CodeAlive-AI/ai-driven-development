## B.2.2 - Meta-System Transition - System Specialization of MHT

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.2.2:0 - Use This When

Use this pattern when a Meta-Holon Transition result is an acting physical or operational holon admitted as `U.System`: a swarm, production cell, cloud platform, regulated control system, organizational unit, or another operating whole that now has system participation slots of its own.

The first useful question is not "is there emergence?" but:

```text
Is the MHT-result whole a U.System whose delimitation, objective,
supervision or coordination, capability envelope, role assignments,
methods, work occurrences, transformations, functioning, evidence,
assurance, and temporal claims must be re-declared for the result whole?
```

Use `B.2` first to decide whether whole reidentification is needed. Use `B.2.2` only after the result-kind question points to `mhtResultSystemRef`.

**What goes wrong if missed.** A real operating whole is still managed through old component claims, or a mere collection is declared a new system without system participation evidence.

**What this buys.** The system MHT keeps the useful meta-system-transition intuition while preserving FPF's direct owners for system participation, architecture, capability, transformation, work, evidence, and assurance.

**Not this pattern when.**

- If the result whole is claim-bearing and non-agentive, use `B.2.3` and the episteme family.
- If the evidence is only a capability or functioning gain without whole reidentification, use `A.2.2`, `C.16`, `A.6.F`, `A.3.4`, `C.30.TFS-REL`, and `A.10`.
- If the claim is ordinary system aggregation or delimitation, use `B.1.2`, `A.1`, `A.14`, and `C.13`.
- If the claim is a mathematical, simulation, graph, benchmark, or scaling expression, use `C.29` and the relevant description or publication pattern before returning to B.2.
- If the claim is only supervisor-subholon feedback relation inside an already admitted system whole, use `B.2.5`.

### B.2.2:1 - Problem Frame

`B.2` is holon-general. `B.2.2` is its system-result specialization.

A system-result MHT occurs when the result of whole reidentification is an acting physical or operational holon. The old constituent systems may remain parts, participants, resources, or interacting neighbors, but the current claim now needs a result system with its own selected delimitation, objective, supervision or coordination, capability envelope, functioning relation, architecture claims, transformation participation, work occurrences, evidence, assurance, and temporal claims.

The pattern does not say that every collection of systems is a system MHT. It says how to carry the system ontic when B.2 has already left a whole-reidentification question and the result-kind admission is `U.System`.

### B.2.2:2 - Problem

Without this specialization:

1. **System identity stays on old parts.** The project keeps component assurance, component responsibilities, and component interfaces after the operating whole has changed.
2. **System claims become rhetoric.** A group gets a collective name, but no result-system delimitation, objective, coordination, or capability evidence is named.
3. **Supervision is overread.** A coordination mechanism is treated as a super-holon, safety evidence, or a complete system admission.
4. **Transformation is confused with containment.** One system changing another holon is treated as part-whole construction instead of transformation and work.
5. **Architecture description replaces architecture.** Dashboards, diagrams, simulations, bills, and digital twins are treated as the operating system rather than descriptions of it.

### B.2.2:3 - Forces

| Force | Tension |
| --- | --- |
| Component assurance vs result-system assurance | Old component claims may still matter, but they do not automatically cover the new operating whole. |
| Delimitation vs external participation | The result system needs an admitted delimitation while external acting systems, resources, and environments remain outside it. |
| Coordination vs whole identity | Coordination can be evidence for system MHT, but coordination alone does not admit a new system whole. |
| Capability gain vs identity change | A new capability envelope can reveal a result system, but some gains remain ordinary capability or functioning claims. |
| System architecture vs system description | Architecture claims concern the operating whole; diagrams and records are description epistemes or publication forms. |

### B.2.2:4 - Solution

After `B.2` leaves an MHT question open, admit the system-result case with a system-focused slice of the `HolonReidentificationRecord@Context`.

#### B.2.2:4.1 - System-Result MHT Slice

Use this slice when `mhtResultSystemRef` is selected.

```text
SystemMHTSlice@Context:
  existingWholeRef: U.Holon
  mhtResultSystemRef: U.System
  boundedContextRef:
  selectedTriggerProfileRef: MHTTriggerProfile@Context
  existingWholeExplanationCheckRef: ExistingWholeExplanationCheck@Context
  systemKindAdmissionRef: A.1 or B.1.2 admission
  resultDelimitationRelationRef:
  resultBoundaryCrossingRelationRefs:
  objectiveOrEvaluationRelationRef?
  supervisionOrCoordinationRelationRef?
  capabilityEnvelopeRef?
  roleAssignmentRefs?
  methodOrMechanismRefs?
  transformationParticipationRefs?
  workOccurrenceRefs?
  functioningRelationRefs?
  architectureClaimRefs?
  evidenceOrAssuranceRefs?
  temporalOrDynamicsRefs?
  blockedOverreads:
```

This slice is not a U-kind. It is the system-result part of the B.2 record, written so that every system-dependent claim can return to its direct owner.

#### B.2.2:4.2 - System Participation Re-Basing

When the result is `U.System`, re-base system participation slots for the result system:

- role assignments through `A.2.1` and role-relation owners;
- capabilities through `A.2.2` and `C.16`;
- methods and mechanisms through `A.15`, `A.6.1`, and their current direct owners;
- transformations through `A.3.4`;
- work occurrences through `A.15.1`;
- functioning and functional structure through `A.6.F` and `C.30.TFS-REL`;
- architecture through `C.30`, `A.22`, and `C.30.ASV`;
- evidence and assurance through `A.10`, `B.3`, and `B.3.5`;
- temporal and dynamics claims through `C.27`, `A.19`, and the direct temporal owners.

Do not reuse old component evidence as if it automatically covered the result system. Carry continuities by explicit relation; re-declare changed slots for the result system.

#### B.2.2:4.3 - System Trigger Interpretation

The B.2 trigger profile can be interpreted for systems as follows:

| Trigger family in `MHTTriggerProfile@Context` | System-result reading | Direct owner kept visible |
| --- | --- | --- |
| Delimitation change | The operating whole now has an external delimitation and crossing relations that differ from the old aggregate. | `A.1`, `B.1.2`, `A.14`, `C.13` |
| Objective or evaluation change | The whole is now evaluated by a system-level objective, mission, SLO, safety case, or viability claim. | `C.16`, `E.13`, `A.10`, decision or assurance owners |
| Supervision or coordination change | A controller, protocol, governance relation, or distributed coordination relation regulates constituent behavior for the result whole. | `B.2.5`, `A.12`, `A.3.4`, `A.15.1` |
| Capability or closure evidence | The capability envelope belongs to the result system, not to any one constituent alone. | `A.2.2`, `C.16`, `B.2.4` when whole reidentification is current |
| Agency threshold | The result whole crosses a concern-specific agency threshold in characteristic space. | `A.13`, `A.19`, `C.16` |
| Temporal consolidation | A commissioning, phase, release, or operating-time consolidation changes the current system identity claim. | `C.27`, `A.15.1`, temporal owners |
| Context reframe | The relevant bounded context changes the operating whole under concern. | `A.1`, bounded-context owners, architecture owners |

No single row is enough by itself. The row names evidence to inspect. B.2 decides whether the whole must be reidentified.

#### B.2.2:4.4 - Delimitation and External Acting Systems

For system-result MHT, distinguish:

- a part of the result system;
- an external acting system that changes the result system or a constituent;
- an environment or resource that participates in work;
- a description, dashboard, twin, model, diagram, or publication about the result system.

A lathe making a workpiece, a controller steering a plant, or a teacher changing a learner does not become a super-holon merely because it changes another holon. Use `A.12`, `A.3.4`, and `A.15.1` for acting side, transformation, and work. Use part-whole owners only when parthood itself is admitted.

#### B.2.2:4.5 - Assurance Re-Basing

When `mhtResultSystemRef` is admitted, old assurance must be tested against the result system.

Ask:

- Which component evidence still applies unchanged?
- Which evidence applies only through explicit correspondence or source-use relation?
- Which assurance claims must be rewritten for the result system?
- Which architecture, capability, functioning, work, temporal, or evidence claims now have different owners?

The result system can inherit evidence only through named relations. It does not inherit safety, reliability, responsibility, or performance claims by label.

### B.2.2:5 - Archetypal Grounding (Worked Cases)

#### B.2.2:5.1 - Search-And-Rescue Swarm

Before MHT, the project has individual drones with local navigation and maintenance records. After MHT, the current object may be one search-and-rescue swarm if the result whole has its own mission objective, coordination relation, external command relation, capability envelope, and swarm-level risks.

```text
SystemMHTSlice@Rescue:
  existingWholeRef: drone fleet as managed aggregate
  mhtResultSystemRef: search-and-rescue swarm
  resultDelimitationRelationRef: command-and-operating-area delimitation
  supervisionOrCoordinationRelationRef: formation and coverage coordination
  capabilityEnvelopeRef: area-search coverage under wind and battery conditions
  evidenceOrAssuranceRefs: swarm-level test evidence, not only drone certificates
```

The old drone evidence remains relevant, but it is not enough for the swarm-level assurance claim.

#### B.2.2:5.2 - Cloud Platform

Independent services become a platform only if the current claim concerns a result system: a shared control plane, system-level SLO, deployment and rollback coordination, platform-level evidence, and external commitments.

If the only change is a better dashboard or one more service, use architecture-description, publication, measurement, or component owners. Use B.2.2 only when `mhtResultSystemRef` is the operating platform itself.

#### B.2.2:5.3 - Production Cell

A machine, robot, fixture, workpiece carrier, and inspection station can become a production cell when the cell has its own delimitation, objective, coordination, transformation structure, work occurrence evidence, and capability envelope.

The fixture being manufactured is not part of the machine merely because the machine changes it. The production cell claim needs a result system; the manufacturing relation remains transformation and work.

### B.2.2:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Named aggregate as system | A fleet, platform, or cell name is treated as system admission. | Require result-system delimitation, objective, coordination, capability, and evidence refs. |
| Component evidence transfer | Component certificates are read as result-system assurance. | Re-base assurance and evidence for `mhtResultSystemRef`. |
| Coordination as whole | A controller, protocol, or coordination relation is treated as automatic system MHT. | Keep supervision evidence visible, but require B.2 whole reidentification and system admission. |
| Description as system | Dashboard, simulation, model, twin, or bill is treated as the operating system. | Use episteme, publication, source-use, and architecture-description owners for description objects. |
| Transformation as containment | An external system changes a holon and is treated as its super-holon. | Use A.12, A.3.4, A.15.1, B.2.5, and part-whole owners separately. |

### B.2.2:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B2.2-1` | B.2 has already left a whole-reidentification question before B.2.2 is used. |
| `CC-B2.2-2` | The result kind is admitted as `U.System` and recorded as `mhtResultSystemRef`. |
| `CC-B2.2-3` | `SystemMHTSlice@Context` does not act; it carries refs to direct owners. |
| `CC-B2.2-4` | Result-system delimitation and crossing relations are named without creating `U.Boundary` or `U.Interaction`. |
| `CC-B2.2-5` | Supervision or coordination evidence is not treated as automatic system admission or safety evidence. |
| `CC-B2.2-6` | Acting-system participation, transformation, and work are separated from parthood. |
| `CC-B2.2-7` | Component assurance is not silently transferred to the result system. |
| `CC-B2.2-8` | Descriptions, dashboards, simulations, and digital twins remain epistemes or publications unless the operating system itself is the EoC. |

### B.2.2:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Named aggregate as system | "The platform" or "the fleet" is treated as a system because it has a name. | Recover `SystemMHTSlice@Context`; require result-system delimitation, objective, coordination, capability, and evidence refs. |
| Component certificate transfer | Individual part certificates are used as result-system assurance. | Re-base assurance through B.2.2:4.5 and evidence owners. |
| Controller as super-holon | A controller or external system is treated as the new whole because it changes the parts. | Use A.12, A.3.4, B.2.5, and part-whole owners separately. |
| Dashboard as system | A monitoring model is treated as the operating system. | Use episteme, publication, source-use, C.30.AD, or digital-twin description owners. |
| Capability jump as system MHT | A metric improves and the result is called a new system. | Use `ExistingWholeExplanationCheck@Context`; return to capability, characteristic, method, work, or architecture owners if sufficient. |

### B.2.2:8 - Consequences

Positive consequences:

- Meta-system transition remains usable for engineering and organizational systems without making B.2 system-only.
- System ontic preservation becomes explicit: system slots are re-based rather than replaced by generic whole language.
- Assurance, responsibility, architecture, work, and evidence claims are kept with their direct owners.

Costs:

- A system-result MHT cannot be declared by name, diagram, dashboard, or metric jump alone.
- Teams must separate old component evidence from result-system evidence.
- Some apparent emergence claims return to ordinary system aggregation, capability, measurement, or architecture repair.

### B.2.2:9 - Rationale

Valentin Turchin's meta-system transition remains a useful intuition for the system case: components can become a higher operating whole when coordination and control create a new object of management and assurance. FPF generalizes that intuition in B.2, then uses B.2.2 to keep the classical system case precise.

The key distinction is ontological, not lexical. A result system is not a trigger profile, coordination mechanism, graph, description, dashboard, or process label. It is an admitted `U.System` whose system participation slots must be available and, where changed, re-declared.

### B.2.2:10 - SoTA-Echoing

| Source family | Lesson for B.2.2 | FPF decision |
| --- | --- | --- |
| Meta-system transition and holonic systems lineage | A new coordinated whole can become the relevant operating object. | B.2 owns whole reidentification; B.2.2 specializes it for `mhtResultSystemRef`. |
| Systems-of-systems and cyber-physical systems practice | Operational closure, coordination, external commitments, and assurance often change at the result-system level. | B.2.2 requires result-system slot re-basing rather than component evidence transfer. |
| Constructional and part-whole ontology | Acting on an object and being part of it are different relations. | A.12, A.3.4, A.15.1, A.14, and C.13 remain separate owners. |
| Digital-twin and architecture-description practice | Rich descriptions can track a system without being the system. | Dashboards, models, twins, and publications use episteme and description owners unless the operating system is recovered as EoC. |

### B.2.2:11 - Relations

- **Specializes:** `B.2` for MHT-result holons admitted as `U.System`.
- **Builds on:** `A.1`, `B.1.2`, `A.14`, and `C.13` for holon and system delimitation and part-whole grounding.
- **Coordinates with:** `A.12`, `A.3.4`, `A.15`, `A.15.1`, `A.2.1`, `A.2.2`, `C.16`, `A.6.F`, `C.30`, `A.22`, `C.30.ASV`, `C.30.TFS-REL`, `A.10`, `B.3`, and `B.3.5`.
- **Uses:** `B.2.5` when supervisor-subholon feedback relation is part of the system-result evidence.
- **Contrasts with:** `B.2.3` for MHT-result holons admitted as `U.Episteme` and `B.2.4` for capability and functioning whole-reidentification evidence.

### B.2.2:End

