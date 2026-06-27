## C.32.CONWAY - Transformer and Transformed Architecture Correspondence

> **Type:** Architectural subpattern under C.32
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative

### C.32.CONWAY:1 - Problem frame

Use this pattern when a practitioner is synthesizing an architecture for a holon that changes another holon, and the architecture of the changing holon constrains, enables, or degrades the architecture of the holon being changed.

Primary working reader: an architect or architecture-responsible practitioner who must co-synthesize selected structures of the changing holon and the changed holon under one changing relation.

Typical entry phrases:

```text
"The product architecture we want cannot be built by the existing manufacturing line."
"The service boundaries we chose still require every team to coordinate every release."
"The method family changes documents, but its review roles do not match the evidence structure it must create."
"The AI-agent toolchain changes project work products, but its control and evidence boundaries do not match the transformed work-product architecture."
"We need an inverse Conway candidate alternative, not another diagram of the desired transformed-holon architecture."
```

**First-minute use slice.** A product-family team wants independently replaceable field modules. The existing manufacturing and certification organization is built around one batch line and one shared evidence responsibility. Using C.32.CONWAY, the practitioner names the two holons in the changing relation: the manufacturing and certification holon as transformer, and the product family as transformed holon. The C.32 candidate palette now includes three architecture configurations: change the manufacturing cell and evidence roles to match module variation, change the product-family module split to fit the fixed line, or keep a bounded mismatch with a clear exception cost and reopen trigger.

The primary `EntityOfConcern` is a local correspondence frame inside architecture candidate synthesis. The frame relates selected structures of the changing holon and selected structures of the changed holon under one changing relation. Organization-design decisions, organization-design authority relations, module-interface repair, structural-equivalence claims, and architecture decisions belong to their governing patterns when those claims are being made; C.32.CONWAY may use them only as constraints, costs, or candidate-change inputs.

What goes wrong if C.32.CONWAY is missed: the team either treats the existing organization, toolchain, manufacturing line, method family, or communication structure as if it already settled the transformed-holon architecture, or it draws a desired transformed-holon architecture that the changing holon cannot actually produce, test, maintain, evolve, or certify.

What C.32.CONWAY buys in practice: the practitioner can turn Conway pressure and inverse Conway maneuvers into candidate alternatives inside the C.32 palette. An alternative may change the transformer side, the transformed side, both sides, or a bounded mismatch; each variant names gains, losses, affected architecture characteristics, and the receiving pattern.

Ordinary working move: name the changing holon, the changed holon, the changing relation, and the selected structures on both sides; then prepare alternatives that change the transformer side, the transformed side, both sides, or keep a bounded mismatch.

Adoption test: after using C.32.CONWAY, the recorded candidate palette states whether each alternative changes the transformer side, the transformed side, both sides, or a bounded mismatch, and what gain, loss, affected characteristic, and stop condition follow.

Not this pattern when the current work is only module-interface repair, bounded-transformation identification, work or role assignment without architecture synthesis, mathematical structural similarity, local choice, or project architecture decision.

Common exits by claim kind:

- `A.6.M` for module-interface repair.
- `A.3.4` or `A.3.4.P` for bounded transformation.
- The A.15 family, `A.2`, or the direct role pattern for work and responsibility.
- `C.29` and the project-selected structural-equivalence pattern for structural similarity.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `G.5` for selected-set publication; `C.18` and `C.19` for archive, front, or pool-treatment policy.
- `C.11` for fixed local choice and `C.32.PAD` for project decision.

The first useful output is `TransformerTransformedArchitectureCorrespondenceFrame@Project`. The frame is the project working record for the correspondence question. It records candidate co-synthesis pressure; it does not make a C.29 structural-equivalence claim, organization-design decision, or new correspondence ontology:

For a first pass, fill only the bounded context, synthesis question, changing relation, transformer holon, transformed holon, the selected-structure pair that changes the candidate frame, affected architecture characteristics, candidate configurations, and next governing pattern. Add full correspondence claims, C.29 refs, detailed source-return fields, and extra structure pairs only when a receiving comparison, structural-similarity, publication, choice, or decision claim needs them.

```text
TransformerTransformedArchitectureCorrespondenceFrame@Project:
  boundedContextRef:
  synthesisQuestion:
  changingRelationRef:
  transformerHolonRef:
  transformedHolonRef:
  transformerArchitectureRef?:
  transformedArchitectureRef?:
  transformerSelectedStructureMap:
    - structureKindRef:
      selectedStructureRef?:
      contributionToChangingRelation:
      architectureCharacteristicPressure:
      governingPatternRef:
      sourceReturnCondition?:
  transformedSelectedStructureMap:
    - structureKindRef:
      selectedStructureRef?:
      requiredArchitectureRole:
      architectureCharacteristicPressure:
      governingPatternRef:
      sourceReturnCondition?:
  correspondenceClaims:
    - correspondenceId:
      transformerStructureRef:
      transformedStructureRef:
      correspondenceUse:
      pressureDirection:
      affectedArchitectureCharacteristicRefs:
      expectedArchitectureGain:
      knownArchitectureLoss:
      preservedStructure:
      lostOrHiddenStructure:
      receivingPatternRef:
      sourceReturnCondition:
  candidateArchitectureConfigurations:
    - candidateRef:
      transformerSideChange:
      transformedSideChange:
      coordinationChange:
      expectedArchitectureGain:
      knownArchitectureLoss:
      stopOrEscalationCondition:
  c29LensOrStructuralEquivalenceRef?:
  nextGoverningPatternRef:
```

### C.32.CONWAY:2 - Problem

Architecture synthesis often crosses a changing relation. A manufacturing system changes a product. A design organization changes a system design. A method family changes documents and work products. An AI-agent toolchain changes project work. A school changes student capabilities. A hospital triage organization changes patient-flow states. In each case, the architecture of the changing holon can make some transformed-holon architectures cheap, slow, brittle, feasible, infeasible, evolvable, or hard to certify.

Conway's law and the mirroring hypothesis make this pressure visible, but they do not replace architecture synthesis. The recurring engineering failure is that a desired transformed-holon architecture is synthesized without recovering whether the changing holon's work, communication, toolchain, manufacturing, certification, operational, or evidence structures can produce and evolve it. The result is predictable: the candidate looks architecturally clean, then independent change, deployability, testability, certification, or maintenance collapses into cross-team and cross-structure coordination work.

The inverse Conway maneuver is also an architecture candidate change, not a slogan. It means deliberately changing selected structures of the changing holon so that the desired changed-holon architecture becomes feasible and maintainable. Sometimes the stronger candidate changes the transformed-holon architecture instead. Often the honest candidate changes both and records the new burden.

C.32.CONWAY makes the correspondence explicit enough to prepare comparison inputs without collapsing the two sides.

### C.32.CONWAY:3 - Forces

| Force | Tension |
|---|---|
| Existing transformer architecture | Current work, communication, tool, method, placement, and evidence structures shape what can be changed. |
| Desired transformed architecture | The changed holon may need module, functional, control, evidence, placement, or variation structure that the transformer cannot yet sustain. |
| Inverse change cost | Changing the transformer may be more expensive than changing the transformed architecture, or vice versa. |
| Structural similarity temptation | Mirroring language can be used to treat correspondence as architecture adequacy. |
| Evolution window | A correspondence that works now can fail after transformer-side or transformed-side structures evolve; those changed structures then constrain the next candidate frame. |

### C.32.CONWAY:4 - Solution

Build a correspondence frame before treating Conway or inverse Conway as guidance.

Work in eight steps:

1. Name the changing relation. Use `A.3.4` when one bounded transformation is being claimed, `E.18` when a transformation-flow structure is being claimed, or the direct work and method patterns when the claim is work or method use.
2. Name the transformer holon and the transformed holon. Keep their architectures distinct even when they belong to one larger holon.
3. Map only the selected structures that carry the constraint or option shaping the candidate frame. On the transformer side, name the actual structure that makes one transformed-holon architecture feasible or infeasible. On the transformed side, name the actual structure that must carry the desired function or architecture characteristic. Stop at the smallest pair that can change the candidate frame or the later comparison input.
4. State only the architecture characteristics that can change the comparison. Use the local q-bundle when possible; otherwise name the few characteristics under pressure, such as independent change, substitutability, evidence reuse, latency, coupling, cohesion, coordination load, or source-return cost.
5. State the correspondence claim. Say which transformer-side selected structure constrains or enables which transformed-side selected structure, what is preserved, what is hidden or lost, and which receiving pattern governs the next claim.
6. Generate candidate architecture configurations:
   - change the transformer-side structure so the desired transformed architecture becomes feasible;
   - change the transformed-side architecture to fit a transformer constraint that is not worth changing now;
   - change both sides as one co-synthesis candidate;
   - keep a bounded mismatch with exception cost, source-return condition, and reopen trigger.
7. Use `C.29` only when the correspondence is claimed as structural similarity, homomorphism-like mapping, equivalence, or formal preservation. Otherwise keep it as architecture synthesis material.
8. Stop when the C.32 candidate palette contains the fields required by `A.19.CPM` explicit comparison, `C.32.MLAO` residual reduction, `C.32.FAIL` repair, publication of a selected set under `G.5`, `C.11` choice, or `C.32.PAD`.

Correspondence repair rows are local C.32.CONWAY entries. They do not create new FPF kinds.

| Correspondence repair row | Use | Minimum repair against overread |
|---|---|---|
| `changingRelationRecovery` | The case names a designer, team, line, tool, method, or organization before the changed object and change relation are clear. | Recover the bounded transformation, work, method-use, or transformation-flow relation before making an architecture claim. |
| `transformerStructureMapping` | A selected structure of the changing holon makes one transformed architecture feasible or infeasible. | Keep the selected transformer structure distinct from the transformed-holon architecture. |
| `transformedStructureMapping` | A selected structure of the changed holon must carry the desired function or architecture characteristic. | Name the selected transformed structure and the architecture characteristic it must support. |
| `inverseConwayRetargeting` | The desired transformed architecture is sound, but the changing holon cannot produce or sustain it. | Change transformer-side selected structures and record migration cost, new burden, and stop condition. |
| `transformedArchitectureRetargeting` | The transformer-side structure is fixed or expensive to change in the declared evolution window. | Change the transformed architecture candidate and record the lost desired property or exception. |
| `jointCorrespondenceSynthesis` | Neither side alone can carry the architecture characteristic. | Create a candidate that changes both sides and records preserved structure, lost structure, and coordination burden. |
| `boundedCorrespondenceMismatch` | A mismatch is tolerable for now. | State exception cost, bounded-use limit, source-return condition, and reopen trigger. |

**Didactic mini-slices.**

| Situation | C.32.CONWAY repair row | Candidate repair |
|---|---|---|
| A field-device family wants replaceable modules, but the manufacturing line and certification evidence are organized by full-product batches. | Name manufacturing and certification as transformer-side selected structures; name module-interface and evidence-scope structures on the transformed side. | Either change cells and evidence roles, change module split, or keep a bounded batch exception with certification cost. |
| A software group wants independently deployable services, but every release still crosses a shared test environment and shared approval role. | Treat team, work, test, and approval structures as transformer-side constraints; treat service and deployment structures as transformed-side structures. | Use inverse Conway retargeting for team and test responsibility, or choose a less independent service architecture for this evolution window. |
| A reusable review method changes authored specifications, but no role carries exception evidence after automated checks. | Treat the review method and exception role as transformer-side selected structures; treat authored-section and evidence-scope structures as transformed-side structures. | Add an exception role and evidence scope, change the method step, or reject the automation candidate. |
| An AI-agent toolchain changes project tasks, but policy control and evidence refresh remain outside the tool boundary. | Treat toolchain module, control, and evidence-refresh structures as transformer-side structures; treat task architecture and policy-conformance evidence as transformed-side structures. | Add supervisor relation and evidence refresh, change task decomposition, or keep bounded autonomy with source-return trigger. |

**Stop condition.** Stop when the frame names both holons, the changing relation, selected structures on both sides, architecture characteristics under pressure, candidate changes, known losses, receiving patterns, and source-return conditions.

**Lowering condition.** Keep a correspondence claim as C.32.CONWAY synthesis material only while the changing relation, both holons, both selected structures, affected architecture characteristics, preserved structure, lost or hidden structure, evolution window, and receiving pattern remain current. Lower the claim to diagnostic pressure when one of those values is unknown, stale, or outside the current synthesis question. Retire a candidate configuration when its transformer-side change, transformed-side change, bounded mismatch, or known loss no longer belongs to the declared evolution window. Return to `A.3.4` or `E.18` when the changing relation is not recovered, to work or organization-governance patterns when no transformed-holon architecture characteristic is under pressure, and to `C.29` when the current claim is structural similarity, preservation, mapping, or equivalence.

### C.32.CONWAY:5 - Worked Correspondence Cases

| Grounded working case | Correspondence question | Candidate work | Stop condition |
|---|---|---|---|
| Product family and manufacturing system | Which manufacturing, evidence, and station structures must correspond to product module and evidence-scope structures? | Prepare manufacturing-cell change, product-split change, and bounded mismatch as candidate alternatives or comparison inputs. | Stop before product decision, factory work authorization, or certification assurance unless those claims are being made. |
| Organization that designs and operates a service platform | Which work, communication, deployment, and service-interface structures must be co-synthesized for independent change? | Prepare inverse Conway team-boundary change, service-boundary change, and platform mediation as candidate alternatives or comparison inputs. | Stop before organization-redesign decision, organization-redesign authority relation, G.5 publication of a selected set, or architecture decision. |
| Method family that changes authored work products | Which method, role, and evidence structures must fit the authored-section architecture being created? | Prepare method-step split, role retargeting, evidence-scope change, and bounded exception as candidate alternatives or comparison inputs. | Stop before method governance or publication-face use unless that claim is being made. |
| School or training system changing a declared learner-capability structure | Which teaching role, curriculum, feedback, and evidence structures must fit that declared learner-capability structure? | Prepare curriculum architecture, feedback-role change, evidence scope, and bounded cohort exception as candidate alternatives or comparison inputs. | Stop before educational policy, evidence sufficiency, or ethical mediation claims. |
| AI-agent toolchain changing project work | Which toolchain, control, evidence, and work-method structures must fit the transformed work-product architecture? | Prepare supervisor relation, task decomposition, evidence-refresh boundary, and bounded autonomy as candidate alternatives or comparison inputs. | Stop before safety, release, or assurance claims unless those claims are being made. |

### C.32.CONWAY:6 - Correspondence Failure Modes

| Failure mode | C.32.CONWAY repair action |
|---|---|
| **Transformer architecture omitted** | The transformed-holon architecture assumes independent change, testing, deployment, certification, or maintenance, but the changing holon's existing structures force shared queues, shared approval, shared evidence, or shared rework. Add transformer-side candidates before the transformed-holon architecture enters comparison, selection, local choice, or decision work. |
| **Transformed-only inverse Conway** | The text asks for inverse Conway while changing only the changed-holon modules, services, product variants, or evidence scopes. Name the transformer-side structure to change and record expected gain, loss, migration burden, and stop condition. |
| **Transformer-only reorganization** | The organization, method, toolchain, line, or platform is changed without a transformed-holon architecture characteristic under pressure. Return to work or organization design unless a selected transformed structure and architecture characteristic are named. |
| **Mirroring treated as adequacy** | A mirroring claim is used without asking what is preserved, what is lost, and where exceptions are acceptable. Keep it as correspondence pressure, or use `C.29` when a structural-similarity lens is being claimed. |
| **One-sided optimization** | Changing only the transformer or only the transformed holon creates a new residual in another scope. Prepare transformer-side change, transformed-side change, joint change, and bounded mismatch as candidate alternatives or comparison inputs. |
| **Software delivery overfit** | DORA or Team Topologies gives the source pattern, but the described holon is a product family, manufacturing system, method family, school, hospital, or other non-software holon. Transfer the selected-structure correspondence and architecture characteristics, not the software ontology. |
| **Static correspondence** | A good correspondence is treated as durable after the evolution window changes. Add source-return and reopen conditions. |

### C.32.CONWAY:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C32.CONWAY-1` | The changing relation is named through `A.3.4`, `E.18`, work, method, or the direct governing pattern. | Prevents actor names or source phrases from standing in for the change relation. |
| `CC-C32.CONWAY-2` | Transformer holon and transformed holon are named separately. | Prevents architecture collapse. |
| `CC-C32.CONWAY-3` | Selected structures on both sides are named with governing patterns. | Keeps organization, work, module, method, tool, and transformed architecture distinct. |
| `CC-C32.CONWAY-4` | Architecture characteristics under pressure are named. | Makes the correspondence architecturally relevant. |
| `CC-C32.CONWAY-5` | Each candidate states transformer-side change, transformed-side change, expected gain, known loss, and stop condition. | Makes Conway pressure constructive. |
| `CC-C32.CONWAY-6` | Structural similarity claims use `C.29` or the structural-equivalence pattern when that claim is being made. | Blocks treating mirroring as architecture adequacy. |
| `CC-C32.CONWAY-7` | Source-return and evolution-window conditions are present. | Keeps correspondence from becoming timeless. |

### C.32.CONWAY:8 - Common Repair Cues

| Repair cue | Symptom | First repair |
|---|---|---|
| `TransformerArchitectureOmitted` | The transformed-holon candidate requires independent change, testing, deployment, certification, or maintenance that the declared changing holon cannot support. | Add transformer-side candidates, transformed-side retargeting candidates, joint candidates, and bounded-mismatch candidates before the palette enters comparison, selection, local choice, or decision work. |
| `TransformedArchitectureNoTransformerFit` | The desired transformed-holon architecture cannot be produced or sustained by the declared changing holon. | Open inverse Conway retargeting or transformed architecture retargeting as candidate alternatives. |
| `InverseConwayNoTransformerChange` | The text says inverse Conway but names no transformer-side selected structure change. | Name the transformer-side selected structure changed, affected architecture characteristic, loss, migration burden, and receiving pattern. |
| `CoordinationCostHidden` | A candidate reduces visible coupling in the changed holon while shifting coordination cost into shared work, test, approval, evidence, manufacturing, or operational structures. | Name the transformer-side structure carrying the cost and prepare candidate alternatives that change it, change the transformed architecture, or keep a bounded mismatch. |
| `MirroringNoExceptionTest` | A mirroring claim is used without stating preserved structure, lost structure, exception condition, or evolution window. | Keep it as diagnostic pressure, or use `C.29` for a declared structural-similarity lens. |
| `TransformerTransformedCollapse` | The changing holon architecture and changed holon architecture are written as one architecture. | Name the two architecture refs, selected structures on each side, and the changing relation between them. |
| `BoundedMismatchHidden` | A known mismatch is kept without cost or trigger. | Record exception cost, bounded-use limit, source-return condition, and reopen trigger. |

### C.32.CONWAY:9 - Consequences

| Positive consequence | Cost or trade-off |
|---|---|
| Conway pressure is handled as architecture synthesis work rather than as a metaphor. | The practitioner must map two sides and the changing relation. |
| Inverse Conway work supplies candidate architecture changes with gains and losses. | Changing the transformer side can be organizationally or technically expensive. |
| Desired transformed-holon architectures are checked against transformer-side production, maintenance, evidence, and evolution structures. | Some attractive transformed-holon architectures are rejected as unfit for the declared evolution window. |
| Organization, work, method, tool, and module structures stay distinct. | More receiving-pattern exits may be needed before comparison. |
| Structural-similarity claims are not smuggled into architecture adequacy. | Formal correspondence may require C.29 or later structural-equivalence work. |

### C.32.CONWAY:10 - Rationale

Conway and inverse Conway are important because architecture work is not done by an abstract architect outside the world. The holon that changes another holon has its own architecture. That architecture can shape feasible candidate architectures for the changed holon.

The nontrivial work is to make both sides visible as selected structures in a candidate synthesis frame. Then the practitioner can prepare four alternatives that the next comparison, selection, choice, or decision step can actually use: change the transformer, change the transformed architecture, change both, or keep a bounded mismatch. This is architecture synthesis; similarity-based adequacy, organization-design decisions, organization-design authority relations, and publication discipline belong to their governing patterns when those claims are being made.

### C.32.CONWAY:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.CONWAY. Each row states which field, repair row, or boundary the draft sets or revises from the source. The source family is used as architecture practice support, not as an ontology import.

| Source to inspect | Why this source is load-bearing here | Transfer into C.32.CONWAY | Concrete C.32.CONWAY mutation | Blocked overread |
|---|---|---|---|---|
| Melvin Conway, `How Do Committees Invent?` (`https://www.melconway.com/Home/Committees_Paper.html`) | Original mature source for the relation between a design organization and the structure of the designed system. It also states the graph-like correspondence idea that later practice uses as Conway's law. | Treat communication and design organization as pressure on architecture candidates. | The frame requires `transformerHolonRef`, `transformedHolonRef`, selected structures on both sides, architecture characteristics under pressure, and `correspondenceClaims`. | The correspondence claim must say which transformer structures constrain which transformed structures, and what candidate change or bounded exception follows. |
| MacCormack, Rusnak, and Baldwin 2012 mirroring hypothesis (`https://doi.org/10.1016/j.respol.2012.04.011`) and Colfer and Baldwin 2016 exceptions survey (`https://www.hbs.edu/ris/Publication%20Files/16-124_7ae90679-0ce6-4d72-9e9d-828872c7af49.pdf`) | Empirical and theory line for product and organization architecture mirroring, including exceptions. It keeps the pattern from treating mirroring as adequacy. | Use correspondence as a hypothesis evaluated across selected structures and exceptions. | Failure-mode rows add mirror-as-adequacy and static-correspondence guards; conformance requires source-return and C.29 use for structural similarity claims. | A mirrored structure must still be evaluated against architecture characteristics, exception cost, and a receiving claim pattern before it can guide a candidate. |
| DORA loosely coupled teams, last updated 2025-10-20 (`https://dora.dev/capabilities/loosely-coupled-teams/`) | Current practitioner line tying architecture, team independence, testing, deployment, coordination load, and inverse Conway. It is load-bearing because it gives observable architecture characteristics, not only terminology. | Treat independent change, testability, deployability, and coordination load as architecture characteristics under pressure when transformer-side structures constrain transformed-holon change. | Solution and checklist require affected architecture characteristics; repair cue `TransformedArchitectureNoTransformerFit` opens inverse-Conway or transformed-architecture retargeting as the candidate-change question. | Evidence about microservices, team autonomy, or work-transfer count must be mapped to selected structures and architecture characteristics before it guides a candidate. |
| Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | Current organization-design pattern family for fast flow, team interaction modes, cognitive load, platform teams, and evolving team boundaries toward a desired transformed architecture. | Team types and interaction modes are transformer-side selected structures or candidate-change inputs when they shape architecture synthesis. | Row `inverseConwayRetargeting` and worked cases require migration cost, interaction burden, and evolution window. | Team-topology vocabulary must be converted into selected transformer structures, interaction burden, and candidate-change cost before module-interface, work-authorization, or decision claims are handled by their receiving patterns. |
| Current FPF `A.3.4`, `A.3.4.P`, `E.18`, `A.15`, `A.6.M`, `C.29`, `C.32`, `C.32.MLAO`, and `C.32.FAIL` | Governing local ontology for bounded transformation, transformation-flow structure, work and role claims, module-interface repair, mathematical-lens use, candidate synthesis, residual reduction, and failure repair. | Recover the changing relation and selected structures before using Conway wording. | Relations and conformance rows assign stronger claims to exact receiving patterns and keep C.32.CONWAY inside candidate synthesis. | No new `U.Conway`, no new `U.Correspondence`, no local adequacy kind, and no bypass around architecture-decision work. |

**Source-currentness boundary.** Use each source row only for the C.32.CONWAY field, repair row, or boundary named in that row. Recheck the row when the project's transformer structures, transformed structures, evolution window, source practice, or named receiving FPF pattern changes. If the source row no longer supports the local selected-structure correspondence, lower it to background lineage and keep the candidate frame only when the local architecture-characteristic pressure remains recoverable.

### C.32.CONWAY:12 - Relations

- **Builds on:** `C.32` for candidate architecture synthesis, `A.3.4` and `A.3.4.P` for bounded change recovery, `E.18` for transformation-flow structure, `A.15` and role patterns for work and responsibility, `A.6.M` for module-interface relation repair, and `C.30` for grounded architecture over selected structures.
- **Uses:** `C.32.MLAO` when the correspondence problem is a cross-scope or interlevel residual; `C.32.FAIL` when a Conway or inverse-Conway cue first appears as a repair failure; `C.29` when structural similarity, preservation, homomorphism-like mapping, or equivalence is being claimed.
- **Receiving patterns:** `A.19.CPM` for explicit comparison claims, `A.19.SelectorMechanism` for set-returning selection claims, `G.5` for claims about publishing a selected set, `C.18` and `C.19` for archive, front, or pool-treatment policy, `C.11` for fixed local choice, `C.32.PAD` for project architecture decisions, `A.10` for evidence sufficiency, `B.3` for assurance, `A.20` or `A.21` for gate or release claims when those claims are being made, and method, work, or organization-governance patterns when those claims are being made.
- **P2S docking:** `C.32.P2S` uses C.32.CONWAY when a problem-to-structure flow must co-synthesize selected structures of the transformer holon and the transformed holon under one changing relation.
- **Boundary:** C.32.CONWAY governs correspondence framing inside architecture candidate synthesis. It does not govern organization-redesign decisions, organization-redesign authority relations, work authorization, evidence sufficiency, assurance, gate passage, release, structural-equivalence theory, or final architecture decision.

### C.32.CONWAY:13 - Footer marker

`C.32.CONWAY` governs architecture candidate synthesis where selected structures of a changing holon and selected structures of the changed holon must be co-synthesized under Conway, mirroring, or inverse-Conway pressure.

### C.32.CONWAY:End

