## B.2.4 - Capability and Functioning Whole Reidentification

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.2.4:0 - Use This When

Use this pattern when capability-envelope evidence, functioning-relation evidence, or transformation-flow-structure evidence creates or reveals a B.2 whole-reidentification question.

The first useful question is:

```text
Does this capability or functioning evidence show that the existing whole
is no longer the right EntityOfConcern, or is this only a direct capability,
functioning, transformation, method, work, module, characteristic, or
architecture claim?
```

Use `B.2.4` only for the first case. Use direct owners for the second.

**What goes wrong if missed.** A genuine new whole is hidden under ordinary capability improvement; or every impressive capability, function, method chain, module allocation, or metric gain is overclaimed as emergence.

**What this buys.** The pattern keeps capability and functioning evidence available for B.2 while preventing B.2.4 from becoming a generic capability, function, method, work, module, or emergence pattern.

**Not this pattern when.**

- If the claim is ordinary capability, use `A.2.2` and `C.16`.
- If the claim is function-like wording or functioning relation without whole reidentification, use `A.6.F`.
- If the claim is transformation or transformation-flow structure, use `A.3.4`, `E.18`, and `C.30.TFS-REL`.
- If the claim is method, method relation, method description, work plan, or work occurrence, use `A.15`, `A.3.1`, `A.3.2`, `A.15.2`, and `A.15.1`.
- If the claim is module allocation or bearer allocation, use `A.6.M` and architecture owners.
- If the claim is measurement, threshold, score, robustness, quality, or whole-level characteristic, use `C.16`, `A.19`, and evidence owners.
- If the wording is ambiguous emergence, synergy, or title-mnemonic language, use `B.2.P` before selecting B.2.4.

### B.2.4:1 - Problem Frame

A new capability is not automatically a new whole. A function-like relation is not automatically a part-whole relation. A transformation-flow structure is not automatically MHT.

B.2.4 is the narrow B.2 specialization for cases where capability, functioning, or transformation-flow evidence makes the existing whole explanation fail and points to a reidentified holon. It is not a pattern for all capabilities or all functions.

### B.2.4:2 - Problem

Without this specialization:

1. **Capability becomes generic emergence.** A threshold crossing or new envelope is treated as a new whole without B.2 checks.
2. **Function becomes ontology.** Function-like wording creates `U.Function` or a hidden peer kind.
3. **Method and work collapse.** The way of doing, description of doing, planned work, and performed work are compressed into one vague operational claim.
4. **Module allocation becomes functional truth.** A module label is treated as evidence for the required behavior or selected structure.
5. **Transformation-flow description replaces in-life structure.** A graph, diagram, or publication of a flow is treated as the flow structure or whole.
6. **Whole reidentification is missed.** A real result whole is left as "just a better capability".

### B.2.4:3 - Forces

| Force | Tension |
| --- | --- |
| Capability evidence vs whole identity | Capability evidence can reveal a new whole, but most capability claims stay with A.2.2 and C.16. |
| Functioning relation vs part-whole relation | Functioning often crosses parts and bearers; it is not parthood by wording. |
| Transformation-flow structure vs mathematical description | Flow structure may enter architecture claims; graphs and diagrams remain lenses or publications unless selected as objects. |
| Method composition vs performed work | A method relation can describe possible doing, while work occurrence evidence concerns dated performance. |
| New whole vs local improvement | The pattern must preserve real novelty without turning every improvement into MHT. |

### B.2.4:4 - Solution

Use B.2.4 as a decision bridge from capability and functioning evidence to B.2 whole reidentification.

#### B.2.4:4.1 - Capability-Functioning Whole-Reidentification Slice

Use this slice only when B.2 remains current after direct-owner explanations are checked.

```text
CapabilityFunctioningWholeReidentificationSlice@Context:
  existingWholeRef: U.Holon
  boundedContextRef:
  capabilityEnvelopeRef?
  functioningRelationRef?
  transformationFlowStructureRef?
  functionalStructureViewRef?
  candidateBearerRefs?
  methodRelationRefs?
  methodDescriptionRefs?
  workPlanRefs?
  workOccurrenceRefs?
  moduleAllocationRefs?
  characteristicOrThresholdRefs?
  evidenceOrMeasurementRefs:
  existingWholeExplanationCheckRef: ExistingWholeExplanationCheck@Context
  candidateB2RecordRef:
  blockedDirectOwnerOverreads:
```

This slice is not a U-kind and not a capability object. It carries the evidence needed to decide whether B.2 whole reidentification is current.

#### B.2.4:4.2 - Direct-Owner Test

Before using B.2.4 for whole reidentification, test whether a direct owner explains the evidence:

| Evidence under concern | Direct owner if sufficient | B.2.4 becomes current only when |
| --- | --- | --- |
| Capability envelope | `A.2.2`, `C.16`, `A.10` | the envelope belongs to a result whole that cannot be explained by the existing whole |
| Function or functioning relation | `A.6.F`, `A.3.4`, `C.16` | the relation creates or reveals a new whole-level EntityOfConcern |
| Transformation-flow structure | `C.30.TFS-REL`, `E.18`, `A.3.4`, `C.29` when mathematical lens is current | the flow structure changes the identity of the whole under B.2 |
| Method relation or method family | `A.15`, `A.3.1`, `G.5`, `C.29` when lens is current | method evidence changes the whole, not merely the way of doing |
| Method description or procedure text | `A.3.2` and `C.2.1`; use publication-use or source-use owners when publication or source reliance is current | description is not enough; in-life whole reidentification must be recovered |
| Work plan or work occurrence | `A.15.2`, `A.15.1` | performed or planned work is evidence for a result whole, not the whole by label |
| Module, component, or bearer allocation | `A.6.M`, `C.30`, `A.22`, `C.30.ASV` | allocation evidence changes the whole under concern |
| Metric, score, threshold, robustness, quality | `C.16`, `A.19`, `A.10` | the characteristic shift defeats existing-whole explanation |

#### B.2.4:4.3 - Existing-Whole Explanation

Use `ExistingWholeExplanationCheck@Context` before claiming whole reidentification.

Direct-owner explanations that often stop B.2.4:

- better measurement or benchmark normalization;
- improved component capability;
- corrected function-like wording;
- a clearer method relation or method family selection;
- a new method description without performed capability evidence;
- better work coordination inside the same whole;
- module allocation repair;
- architecture-view or transformation-flow-structure repair;
- evidence or source-currentness improvement.

If one of these explanations is sufficient, do not use B.2.4. Use the direct owner.

#### B.2.4:4.4 - When B.2.4 Returns To B.2

Return to B.2 when the evidence shows that the current object must be reidentified as a result holon. Examples:

- a production cell now has a capability envelope, coordination relation, transformation-flow structure, and assurance claim that cannot be explained by individual machines;
- a service platform now has a functioning relation and external commitments that cannot be assigned to one service or module;
- a team, toolchain, and method family now operate as one result system with new capability and work evidence;
- an episteme or standard now has a capability for explanation, prediction, or specification use that requires result-episteme reidentification.

After the return, B.2 owns the MHT record and result-kind admission. B.2.4 carries only the capability and functioning evidence slice.

### B.2.4:5 - Archetypal Grounding (Worked Cases)

#### B.2.4:5.1 - Production Cell Capability

A milling machine, robot arm, fixture, inspection station, and scheduling rule can remain a collection of assets. A new production-cell whole becomes current only when capability and functioning evidence shows one bounded result whole: cell-level cycle time, tolerance, transformation-flow structure, coordination, and assurance cannot be explained by any single component or old aggregate.

Use A.6.F for function-like wording, A.3.4 for transformations, C.30.TFS-REL for transformation-flow structure, A.15.1 for performed work, C.16 for cycle-time and tolerance characteristics, and B.2 only when the cell whole must be reidentified.

#### B.2.4:5.2 - CI/CD Capability

A team may have methods for coding, testing, and releasing. That does not by itself create a new whole. Use method and work owners for the method relations and performed release work.

B.2.4 becomes current only if the capability evidence points to a result holon: a platform, team-system, or work occurrence whole with new delimitation, coordination, external commitments, evidence, and assurance. An automated delivery sequence label does not decide the ontology.

#### B.2.4:5.3 - Theory Explains New Phenomena

A new theory may explain phenomena that the source portfolio did not explain. B.2.4 can carry the explanatory-capability evidence, but B.2.3 owns the episteme-result MHT if the result is `U.Episteme`; C.2.1 owns the episteme slot relation; C.29 owns mathematical-lens use when the lens is relied on for the current claim.

### B.2.4:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Capability as emergence | A new capability label declares a new whole. | Test direct capability, characteristic, evidence, and existing-whole explanations first. |
| Function as part | A function block or functioning relation becomes physical or organizational parthood. | Separate functioning relation, bearer allocation, selected structure, and part-whole claims. |
| Method chain as whole | A sequence of methods or work stages is called a new holon. | Keep method, method description, work plan, and work occurrence with direct owners. |
| Diagram as flow structure | A diagram or graph is treated as the in-life transformation-flow structure. | Use mathematical, description, publication, and selected-structure owners before B.2. |
| Metric jump as MHT | A benchmark, KPI, robustness, or threshold gain declares whole reidentification. | Use C.16, A.19, A.10, and B.2 existing-whole explanation before MHT. |

### B.2.4:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B2.4-1` | B.2.4 is used only when capability, functioning, or transformation-flow evidence creates or reveals a B.2 whole-reidentification question. |
| `CC-B2.4-2` | Ordinary capability, function, functioning, transformation, method, work, module, characteristic, evidence, and architecture claims return to direct owners. |
| `CC-B2.4-3` | No generic `U.Emergence`, `U.Function`, `U.MetaMethod`, or capability-root kind is created. |
| `CC-B2.4-4` | Method, method description, work plan, and work occurrence remain separate. |
| `CC-B2.4-5` | Mathematical or publication descriptions of transformation-flow structure do not replace the in-life structure. |
| `CC-B2.4-6` | If B.2 remains current, B.2 owns the MHT record and result-kind admission. |

### B.2.4:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Capability by declaration | A leader names a new capability, but evidence remains component-level. | Use A.2.2, C.16, and A.10; use B.2.4 only if the existing whole explanation fails. |
| Function as part | A function block is treated as a physical or organizational part. | Use A.6.F, C.30.TFS-REL, A.6.M, and architecture allocation owners. |
| Method chain as whole | A sequence of methods is called a new holon. | Recover method relation and work occurrence; return to B.2 only when a result holon is current. |
| Diagram as flow structure | A diagram or graph is treated as the transformation-flow structure itself. | Use C.29, E.17, C.30.AD, or publication owners unless the selected structure is recovered. |
| Metric jump as whole | A KPI improves and MHT is declared. | Use C.16, A.10, and existing-whole explanation first. |

### B.2.4:8 - Consequences

Positive consequences:

- Capability and functioning evidence can bear on real whole reidentification without becoming a generic emergence owner.
- Direct owners remain visible, so local improvements are not overclaimed.
- Method, work, function, module, and architecture distinctions survive high-pressure capability language; each claim remains with its governing pattern.

Costs:

- Teams must do the direct-owner test before using B.2.4.
- Many impressive capability claims will stay outside MHT.
- B.2.4 depends on B.2 for the final whole-reidentification record.

### B.2.4:9 - Rationale

Capabilities and functioning relations are often where new wholes first become visible. But the evidence is mixed: it may belong to capability measurement, function-like wording, architecture structure, transformation flow, method relation, work occurrence, module allocation, or whole reidentification.

B.2.4 exists to keep that mixed evidence disciplined. It does not rename all of it as "meta-function". It asks whether the evidence defeats the existing whole explanation and, only then, returns to B.2.

### B.2.4:10 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Capability and functioning approaches | A capability envelope is evidence about what a holon can do under conditions; it is not automatically a new whole. |
| Functional architecture and transformation-flow practice | Functioning and flow structures can expose a result whole, but descriptions and diagrams remain distinct from selected in-life structures. |
| Method and work ontology in FPF | Method, method description, work plan, and performed work occurrence must stay separate when capability evidence is interpreted. |
| TAME and agency-as-characteristic-space work | Agency-like evidence is multi-characteristic and thresholded by concern; B.2.4 does not create a binary agency kind. |

### B.2.4:11 - Relations

- **Specializes:** `B.2` for cases where capability, functioning, or transformation-flow evidence creates or reveals whole reidentification.
- **Uses:** `B.2.P` when emergence-family or title-mnemonic wording hides the claim kind.
- **Coordinates with:** `A.2.2`, `C.16`, `A.6.F`, `A.3.4`, `E.18`, `C.30.TFS-REL`, `A.15`, `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `A.6.M`, `C.30`, `A.22`, `C.30.ASV`, `C.29`, `A.10`, and source-use patterns.
- **Contrasts with:** `B.2.2` for system-result MHT and `B.2.3` for episteme-result MHT.

### B.2.4:End

