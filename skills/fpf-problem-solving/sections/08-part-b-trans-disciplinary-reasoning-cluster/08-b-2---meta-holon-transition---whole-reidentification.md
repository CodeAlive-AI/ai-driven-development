## B.2 - Meta-Holon Transition - Whole Reidentification

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.2:0 - Use This When

Use this pattern when a configured whole can no longer be treated as the same whole for the current claim: its delimitation, objective, supervision, capability envelope, agency threshold, temporal consolidation, or bounded context has changed enough that the EntityOfConcern must be reidentified.

Typical moments:

- a set of coordinated parts becomes a regulated system with its own objective and externally visible commitments;
- a commissioning history crosses into operation and the assurance claim must restart for the operational whole;
- a theory, model family, or knowledge body becomes an admitted episteme whole rather than a loose catalogue;
- a capability envelope appears only after structure, functioning, method, work, and evidence align;
- an architecture residual cannot be explained inside the existing whole.

**First useful move.** Try `ExistingWholeExplanationCheck@Context` first. If the observed gain or shift can be explained inside the existing whole by better parts, corrected relations, improved measurement, method or work repair, richer phase coverage, or architecture-view repair, stay with the existing whole and its direct owners. Use B.2 only when the whole itself must be reidentified.

**What goes wrong if missed.** Emergence becomes rhetoric, ordinary improvement is overclaimed as a new whole, or a genuinely new whole remains hidden under old part, evidence, assurance, architecture, or responsibility claims.

**What this buys.** B.2 gives one accountable whole-reidentification move: recover the existing whole, trigger profile, result holon kind, identity claim, evidence, direct owner of changed content, and blocked overreads before any MHT claim is relied on.

**Not this pattern when.**

- If the claim is ordinary part-whole construction, use `B.1`, `A.14`, and `C.13`.
- If the claim is a whole-level characteristic change, use `C.16` and measurement or evaluation owners.
- If the claim is capability without whole reidentification, use capability and characteristic owners.
- If the claim is transformation or work, use `A.3.4`, `A.12`, `A.15`, and `A.15.1`.
- If the claim is only wording repair for emergence-family language, use `B.2.P` first.
- If the claim is graph, RG-like, MSPD, or other mathematical expression, use `C.29` unless whole reidentification is also current.

### B.2:1 - Problem Frame

A Meta-Holon Transition is not a new root ontology, not a generic emergence label, and not a mathematical graph result. It is a whole-reidentification claim about a holon in a bounded context.

The old whole remains a possible explanatory object. B.2 is selected only when the old whole is no longer the right EntityOfConcern for the current claim. The result can be admitted as a `U.System`, `U.Episteme`, `U.Work`, `U.BoundedContext`, `U.Discipline`, or another holon kind only when the direct governing pattern admits that kind and slot discipline.

### B.2:2 - Problem

Without B.2:

1. **New whole is missed.** A coordinated closure or context reframe changes the object, but evidence and architecture still point to old parts.
2. **Ordinary improvement is overclaimed.** A better component, stronger measurement, or corrected method is called emergence.
3. **Record fields become ontology.** A result field, trigger mnemonic, profile, or checklist is treated as a U-kind or actor.
4. **Agency becomes binary.** A threshold crossing is read as "agent or not agent" instead of a characteristic-space threshold for a system in role.
5. **Mathematics replaces ontology.** A graph, RG-like flow, MSPD score, or benchmark jump is treated as MHT without recovering the holon claim.
6. **Transformation becomes containment.** A system changing another holon is treated as that holon's super-holon.

### B.2:3 - Forces

| Force | Tension |
| --- | --- |
| Parsimony vs real novelty | FPF should not mint new wholes for every improvement, but some closures really change the EntityOfConcern. |
| Continuity vs reidentification | History and phase continuity matter, but some transitions require a new result whole. |
| Trigger recognition vs trigger inflation | Delimitation, objective, supervision, capability, agency threshold, time, and context cues help recognition but do not declare MHT by themselves. |
| System-facing emergence vs broader holons | Holonic systems literature is system-facing, while FPF also needs episteme, work, bounded-context, and discipline result cases. |
| Math-lens power vs ontology discipline | RG-like, graph, algebraic, or benchmark expressions can bear on a claim only after the holon and relation are named. |

### B.2:4 - Solution

Use B.2 as a whole-reidentification pattern with three artifacts: a trigger profile, an existing-whole explanation check, and a holon reidentification record.

#### B.2:4.1 - MHTTriggerProfile

`MHTTriggerProfile@Context` is a trigger and evidence profile for possible whole reidentification. It is not a U-kind and not MHT itself.

```text
MHTTriggerProfile@Context:
  existingWholeRef: U.Holon
  boundedContextRef:
  holonDelimitationChangeRef?
  objectiveOrEvaluationChangeRef?
  supervisionOrCoordinationChangeRef?
  capabilityOrClosureEvidenceRef?
  agencyThresholdRef?
  temporalConsolidationRef?
  contextReframeRef?
  evidenceRelationRefs:
  sourceUseRelationRefs?
  candidateResultHolonKindRef?
```

The profile asks whether enough has changed to make the old whole no longer the right EntityOfConcern. A single trigger is evidence for attention, not automatic admission.

#### B.2:4.2 - ExistingWholeExplanationCheck

Before declaring MHT, run:

```text
ExistingWholeExplanationCheck@Context:
  observedGainOrShiftRef:
  existingWholeRef:
  explanationByBetterParts?
  explanationByCorrectedPartRelation?
  explanationByImprovedMeasurement?
  explanationByRaisedCongruenceOrSourceQuality?
  explanationByMethodOrWorkRepair?
  explanationByTemporalCoverageRepair?
  explanationByArchitectureViewRepair?
  explanationByCapabilityOrFunctioningRepair?
  remainingWholeReidentificationQuestion:
```

If an existing-whole explanation is sufficient, do not declare MHT. Use the direct owner for the repair.

#### B.2:4.3 - HolonReidentificationRecord

Declare MHT only with a record that names the old whole, result whole, result kind, triggers, identity claim, and owner boundaries.

```text
HolonReidentificationRecord@Context:
  existingWholeRef: U.Holon
  boundedContextRef:
  selectedTriggerProfileRef: MHTTriggerProfile@Context
  existingWholeExplanationCheckRef: ExistingWholeExplanationCheck@Context
  mhtResultHolonRef:
  mhtResultSystemRef?
  mhtResultEpistemeRef?
  mhtResultWorkOccurrenceRef?
  mhtResultBoundedContextRef?
  mhtResultDisciplineRef?
  resultHolonKindAdmissionRef:
  identityContinuationOrReidentificationClaim:
  changedContentOwnerRefs:
  evidenceRelationRefs:
  sourceUseRelationRefs?
  mathLensUseRefs?
  blockedOverreads:
```

This record is not a U-kind and not an actor. It carries the reidentification claim and the direct owners of neighboring claims.

#### B.2:4.4 - Result References

Use result references as fields, not as kinds:

- `mhtResultHolonRef` for the reidentified whole;
- `mhtResultSystemRef` only when the result is admitted as `U.System`;
- `mhtResultEpistemeRef` only when the result is admitted as `U.Episteme`;
- `mhtResultWorkOccurrenceRef` only when the result is admitted as `U.Work`;
- `mhtResultBoundedContextRef` only when a bounded context is itself the result whole under its direct owner;
- `mhtResultDisciplineRef` only when the result is a discipline holon under `C.20`.

Do not use `post*` field names as live governed names. They hide the result kind and invite temporal shorthand.

#### B.2:4.5 - Agency Threshold

Agency is not a binary status and not a root kind. Treat agency as a characteristic-space threshold for a system in bounded context.

Use `A.13`, `A.19`, and `C.16` for the characteristic-space and threshold claim. Levin-line TAME work can discipline the multi-characteristic framing when agency evidence is relied on for the current claim. B.2 uses agency threshold only as one possible trigger in `MHTTriggerProfile@Context`, and only when crossing the threshold changes closure, supervision, objective, or whole identity.

#### B.2:4.6 - Acting-System Participation

When a source describes a system changing another holon, recover acting-system participation and transformation separately.

Use `A.12` for acting-side externalization, `A.3.4` for bounded transformation, and `A.15.1` for work occurrence. A system changing another holon does not become that holon's super-holon, and no `U.Transformer` kind is created.

#### B.2:4.7 - Mathematical-Lens Separation

Graph, algebra, RG-like, MSPD, benchmark, scaling, and morphism language can bear on MHT recognition only as mathematical or analytical expression.

Use `C.29` when the mathematical lens is relied on for the current claim. Use B.2 only after the holon identity claim is recovered and the existing-whole explanation check leaves a whole-reidentification question.

### B.2:5 - Archetypal Grounding (Worked Cases)

#### B.2:5.1 - Closed-Loop Regulated System

Parts: plant, sensor, controller, actuator.

Existing-whole repair may be enough if only a sensor improved or a controller parameter changed. B.2 becomes current when a closed supervisory structure and objective create a result system whose external commitments and capability envelope are no longer explainable as independent parts.

```text
MHTTriggerProfile@Control:
  existingWholeRef: plant-plus-devices configuration
  supervisionOrCoordinationChangeRef: closed feedback relation
  objectiveOrEvaluationChangeRef: maintain output y near reference r
  capabilityOrClosureEvidenceRef: capability envelope after closure

HolonReidentificationRecord@Control:
  mhtResultSystemRef: regulated control system
  resultHolonKindAdmissionRef: U.System admission under A.1 and B.1.2
  changedContentOwnerRefs: control-structure view, transformation, capability, evidence
```

#### B.2:5.2 - Compendium Becomes Theory

A collection of results can remain a catalogue. B.2 becomes current only when the knowledge body is reidentified as an episteme whole with its own claim-bearing structure, explanatory objective, reference scheme, and evidence relations.

`B.2.3` specializes this case when the MHT-result holon is admitted as `U.Episteme`. `C.2.1` and the episteme family own episteme slot relation, publication, source-use, and claim-bearing structure.

#### B.2:5.3 - Capability Envelope Appears

Several systems, methods, and work occurrences align and a new capability envelope appears. Use direct capability, characteristic, function, transformation, method, work, evidence, and architecture owners first.

Use `B.2.4` only when that capability or functioning evidence creates or reveals a whole-reidentification question under B.2.

#### B.2:5.4 - Lathe And Workpiece

A lathe transforms a workpiece. That is transformation and work, not MHT and not parthood. B.2 becomes current only if the manufacturing arrangement creates or reveals a new whole that must be reidentified, such as a production cell with closure, objective, coordination, and evidence that cannot be explained by the existing parts alone.

### B.2:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Emergence rhetoric | A gain, surprise, or synergy label declares a new whole. | Run `ExistingWholeExplanationCheck@Context` before B.2. |
| Record as ontology | Trigger profiles, result fields, or checklist labels become U-kinds. | Admit result holon kind through direct owners and keep records as records. |
| Math as MHT | Graph, RG-like, MSPD, benchmark, scaling, or morphism expression declares whole reidentification. | Use `C.29`; recover holon identity and existing-whole explanation first. |
| Binary agency | Agency threshold crossing is treated as a root kind or binary status. | Use characteristic-space and threshold owners; use B.2 only when whole identity changes. |
| Transformation as containment | A system changes another holon and is treated as its super-holon. | Use A.12, A.3.4, A.15.1, and boundary-crossing owners before part-whole or MHT admission. |

### B.2:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B2-1` | A B.2 use names the existing whole and bounded context before declaring whole reidentification. |
| `CC-B2-2` | `MHTTriggerProfile@Context` is a trigger and evidence profile, not a U-kind or substitute for MHT. |
| `CC-B2-3` | `ExistingWholeExplanationCheck@Context` is completed before MHT is declared. |
| `CC-B2-4` | `HolonReidentificationRecord@Context` names result refs, result kind admission, identity claim, evidence, source-use relation, math-lens use when current, and blocked overreads. |
| `CC-B2-5` | Agency-threshold claims use characteristic-space and threshold owners; B.2 uses them only when whole identity changes. |
| `CC-B2-6` | Acting-system participation and transformation use A.12 and A.3.4; B.2 does not create `U.Transformer`. |
| `CC-B2-7` | Mathematical expressions can bear on but do not replace the holon reidentification claim. |
| `CC-B2-8` | Result references are fields, not new U-kinds. |
| `CC-B2-9` | Episteme, system, work, bounded context, and discipline result cases use their direct admission patterns. |

### B.2:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Emergence by adjective | A capability or property is called emergent without reidentifying the whole. | Use `B.2.P` to recover claim kind, then B.2 only if whole reidentification is current. |
| Record as ontology | Trigger profile, result field, or record name is treated as a U-kind. | Keep profile and record as forms; admit the result holon kind through direct owners. |
| KPI jump as MHT | A metric improves and MHT is declared. | Run `ExistingWholeExplanationCheck@Context`; use measurement, characteristic, method, work, or architecture owners if sufficient. |
| Agency shortcut | Agency threshold crossing creates a new root kind. | Use characteristic-space threshold owners; B.2 only when closure, supervision, objective, or identity changes. |
| Math result as MHT | Graph, RG-like, MSPD, or benchmark expression declares new whole. | Use `C.29`; recover holon identity before B.2. |
| Transformation as containment | A system changes another holon and is treated as its super-holon. | Use A.12, A.3.4, A.15.1, and boundary-crossing relation owners; use parthood only if independently admitted. |

### B.2:8 - Consequences

Positive consequences:

- MHT becomes a precise whole-reidentification move rather than a synonym for improvement.
- System, episteme, work, bounded-context, and discipline result cases share one B.2 spine while keeping their direct owners.
- Trigger language remains useful without becoming ontology.
- Mathematical and benchmark evidence can be used without replacing the holon claim.

Costs:

- Users must try existing-whole explanations before declaring MHT.
- MHT records require explicit result-kind admission and evidence.
- Some attractive emergence claims will return to ordinary characteristic, method, work, architecture, or measurement repair.

### B.2:9 - Rationale

Holonic work needs a way to recognize when a whole has changed enough that the old EntityOfConcern no longer carries the current claim. B.2 provides that move without collapsing all novelty into "emergence" and without inventing record-field U-kinds.

The pattern is intentionally conservative: it preserves ordinary direct-owner repairs first, then admits whole reidentification only when the existing whole no longer explains the observed shift. This protects B.1 part-whole construction, A.15 work, A.3.4 transformation, C.16 characteristics, C.29 math-lens use, and episteme and publication discipline from being swallowed by MHT.

### B.2:10 - SoTA-Echoing

| Source family | Current lesson for B.2 | FPF decision |
| --- | --- | --- |
| Holonic systems and cyber-physical systems practice | Closure, coordination, objective, and system-wide outcomes can justify treating a configured whole as a new operating object. | `MHTTriggerProfile@Context` includes delimitation, objective, supervision, capability or closure, agency threshold, time, and context cues. |
| Constructional ontology and identity work | Reidentification must say what object is being continued, replaced, or newly admitted. | `HolonReidentificationRecord@Context` names existing whole, result whole, identity claim, and result-kind admission. |
| TAME and agency-as-continuum work | Agency is multi-characteristic and thresholded by concern, not a binary kind. | Agency threshold remains a characteristic-space trigger, not a root kind. |
| Mathematical modeling and RG-like analysis | Scale, coarse-graining, and trajectory measures can reveal pressure for reidentification but are lenses. | B.2 uses `C.29` when mathematical-lens use is relied on and requires holon recovery before MHT. |

### B.2:11 - Relations

- **Builds on:** `A.1` for holon admission, `B.1` for part-whole construction, `A.14` and `C.13` for relation and constructional grounding, and `E.24.UK` for result-kind admission discipline.
- **Coordinates with:** `A.12` and `A.3.4` for acting-side and transformation, `A.15` and `A.15.1` for method and work, `C.16` and `A.19` for characteristic space and threshold, `C.29` for mathematical lenses, `C.32.P2S` when architecturing pressure becomes whole reidentification or emergence rather than local structure repair, and `A.10` for evidence.
- **Specialized by:** `B.2.2` for system-result MHT, `B.2.3` for MHT-result holons admitted as `U.Episteme`, and `B.2.4` for capability and functioning whole reidentification.
- **Can use neighboring evidence from:** `B.2.5` when a supervisor-subholon feedback relation is part of the B.2 case evidence or neighboring structure; that does not make B.2.5 a result-kind specialization.
- **Uses:** `B.2.P` when emergence-family, MHT, MET, MFT, synergy, or metric-mirage wording hides which claim kind is current before B.2 is applied.

### B.2:End

