## C.30.TFS-REL - Architecture Transformation-Flow Structure Relation

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Tech-name:** `ArchitectureTransformationFlowStructureRelation` (relation record)
> **Plain-name:** architecture transformation-flow structure relation
> **Governed object:** the bounded architecture-use record connecting an actual `ArchitectureRelation`, exact selected architecture structure, exact structural-view or description episteme, or bounded architecture claim to one selected `TransformationFlowStructure` under `E.18` or one selected `TransformationFlowStructureNetwork` under `E.18.NET`; the record does not itself instantiate a direct relation.

### C.30.TFS-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on one exact selected `TransformationFlowStructure`, one selected `TransformationFlowStructureNetwork`, or a current path, path slice, crossing, flow valuation, edition pin, plane pin, context pin, no-hidden-scalarization claim, or mathematical description of the selected flow structure.

The first useful move is small. `ArchitectureTransformationFlowStructureRelation` is a bounded architecture-use record connecting one exact architecture locus to the selected E.18 TFS or E.18.NET network used in the question. The locus can be an actual `ArchitectureRelation` occurrence, exact selected architecture structure, exact architecture-description or structural-view episteme, or bounded architecture claim. When a network is selected, the record also says whether one named containing holon or several explicitly named holons supply the architecture side.

```text
ArchitectureTransformationFlowStructureRelation:
architectureRelationOccurrenceRefs?:
architectureClaimRefs?:
selectedArchitectureStructureRefs?:
architectureStructuralViewRefs?:
architectureDescriptionRefs?:
architectureUseConcernRefs?:
claimScope?: U.ClaimScope, byValue
effectiveReferenceScheme?: U.ReferenceScheme, byValue
modelUseStructureRef?: U.StructureRef
empiricalGroundingRelationRefs?:

functionalStructureViewRefs?:
functionalElementClaimRefs?:
functionalBehaviorClaimRefs?:
requiredOrDesiredEffectClaimRefs?:
actualTransformationRefs?:
transformerSideFillerRefs?:
candidateBearerRefs?:
inputConditionRefs?:
outputConditionRefs?:
functionalPortRefs?:

transformationFlowStructureViewRefs?:
transformationFlowStructureRef?:
transformationFlowStructureNetworkRef?:
networkCrossFlowRelationRowRefs[]?: E.18.NET NetworkCrossFlowRelationRowRef
networkArchitectureUseBranch?: namedContainingHolon | explicitInterHolon
containingHolonRef?:
containingArchitectureRelationRef?:
containingArchitectureClaimRef?:
participatingHolonRefs[]?:
participatingArchitectureRelationRefs[]?:
participatingArchitectureClaimRefs[]?:
noNetworkBearerHolonAsserted?:
transformationFlowUnfoldingStructureRef?:
selectedPathOrSliceRefs?:
crossingBundleRefs?:
flowValuationRefs?:

mathematicalDescriptionRefs?:
mathLensUseRefs?:
correspondenceClaimOrRelationRefs?:
sourcePublicationOrEditionRef?:
representationRefs?:
publicationOccurrenceRefs?:
publicationFormRefs?:
carrierRefs?:
extractionOrProbeLocusRef?:
relationObservationClassRef?:
unexploredRegionRefs?:
hiddenRelationStructureReturnCondition?:
admissibleUse:
stopOrReturnCondition:
nonAdmissibleUse?:
```

This is a use/trace record, not a universal direct `U.Relation` declaration and not an obtaining-condition shortcut. Establish each positive `architectureRelationOccurrenceRef`, flow relation, cross-member relation, correspondence relation, empirical-grounding relation, publication occurrence, or project/work relation under its direct pattern before asserting it. Keep a bounded claim or description separate from an obtaining relation occurrence. `groundedNonAdmissibleUse?` is an alias for the optional `nonAdmissibleUse?` value, included only when it passes F.19's plausible-reader test.

Ordinary minimum: name at least one exact architecture-side reference (`architectureRelationOccurrenceRefs`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRefs`, `architectureDescriptionRefs`, or a bounded `architectureClaimRefs` entry) and at least one flow-structure reference (`transformationFlowStructureRef`, `transformationFlowStructureNetworkRef`, `transformationFlowUnfoldingStructureRef`, `selectedPathOrSliceRefs`, `crossingBundleRefs`, or `flowValuationRefs`), the admissible use, and one stop or governing-pattern application. A network use also selects exactly one network architecture-use branch and supplies its required exact holon and relation/claim refs. Use remaining fields other than optional `nonAdmissibleUse` only when they change the next architecture move; otherwise mark them `not used`. Include that explanatory guard only under the full F.19:4 test. An unused guard may be omitted without an absence entry unless a concrete receiving use needs to distinguish absence from missing information.

Use this record only when an actual architecture relation, selected architecture-relevant structure, exact structural-view episteme, functional-structure view, transformation-flow-structure claim, or conditional architecture-description use depends on an E.18 TFS, an E.18.NET network, or one of the selected TFS's paths, crossings, or valuations. Stop when that architecture-to-flow-structure use and its stop or return condition are clear. If another claim is being made, apply its governing pattern and keep this record to the architecture/flow boundary.

What goes wrong if this pattern is missed: a transformation-flow diagram, graph-shaped mathematical description, path slice, flow valuation, requirement, or functional-view row becomes functional architecture, whole architecture ontology, actual `U.Transformation`, performed Work, work-result record, evidence, gate passage, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for one TFS or E.18.NET for one network while C.30 remains the direct architecture-relation and selected-structure adequacy locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the question is only the TFS or network, a mathematical description, path, crossing, or flow valuation and no architecture use is being made. Use E.18 for one TFS, E.18.NET for one network, E.18.2 for its mathematical description, and C.29 when mathematical-lens use is current. Use C.30 for a direct architecture relation or architecture claim without this flow-structure use; use C.30.AD for a durable architecture description and C.30.ASV/A.6.F for a functional view without it. Apply any other claim's governing pattern and keep C.30.TFS-REL only to the architecture/flow relation.

### C.30.TFS-REL:2 - Problem

Using actual architecture relations, selected architecture-relevant structures, exact architecture structural views, and conditional architecture descriptions often requires E.18 TFS objects or one E.18.NET network when the question concerns transformation-flow structure, required functional dependencies, actual change, data movement, control paths, evidence-flow descriptions, neural-network dataflow, or code-agent relation graphs.

C.30.TFS-REL prevents collapse by requiring the exact architecture-side reference before any E.18 TFS, E.18.NET network, path, slice, crossing, or valuation receives architecture use. It also keeps required or desired behavior/effect claims distinct from actual A.3.4 transformations. A network additionally needs the named containing-holon or explicit inter-holon branch; its graph, description, publication, or record cannot supply that branch.

### C.30.TFS-REL:3 - Forces

| Force | Tension |
| --- | --- |
| Transformation-flow relation vs architecture takeover | One E.18 TFS, one E.18.NET network, or a selected path or crossing can be essential, but none becomes all architecture ontology or an unnamed characteristic bearer. |
| Functional view vs transformation-flow view | A functional structure view may need a transformation-flow relation, but a required effect, path, crossing, valuation, or mathematical description is not a functional element or actual transformation by itself. |
| Structure precision vs work/change overread | E.18 gives selected structure, path, and flow-valuation objects; actual transformation, Work occurrence, and work results remain outside this record unless their own patterns admit those claims. |
| No-hidden-scalarization vs architecture scoring | E.18 set-return and no-hidden-scalarization discipline can inform architecture reasoning, but it does not by itself define a general architecture score. |
| Small relation vs unneeded non-architecture apparatus | A project often needs one use record, not a full C.29 lens card, evidence relation, assurance case, or decision record. |
| Flow-structure-owner stability vs C.30 integration | An actual architecture relation, selected structure, structural view, or conditional architecture-description use needs a trace to E.18 for one TFS or E.18.NET for one network without rewriting either owner as generic architecture adequacy theory. |

### C.30.TFS-REL:4 - Solution

C.30.TFS-REL is the C.30 entry record to E.18 and E.18.NET when an actual architecture relation, selected architecture-relevant structure, exact architecture structural view, or conditional architecture description uses one selected `TransformationFlowStructure`, one selected `TransformationFlowStructureNetwork`, or a current path, crossing, or flow valuation.

It supplies only the architecture-to-transformation-flow use boundary. Use the full field set shown in section 1; no filled field makes a direct relation obtain.

```text
ArchitectureTransformationFlowStructureRelation minimum:
  architectureLocusRef: exactly one actual ArchitectureRelation,
    selected architecture U.Structure, exact description/view episteme,
    or bounded ArchitectureClaim used by this question
  flowLocusRef: exactly one E.18 TFS, E.18.NET network,
    unfolding, member-local path/slice/crossing, or valuation
  requiredOrDesiredEffectClaimRefs?: claim content only
  actualTransformationRefs?: only with complete A.3.4 basis
  networkArchitectureUseBranch?: one complete branch from section 4.4a
  admissibleUse:
  stopOrReturnCondition:
  nonAdmissibleUse?:
```

At least one architecture-side field and at least one E.18 or E.18.NET field must be named by value. Network branch fields obey `C.30.TFS-REL:4.4a`; other optional trace fields stay `not used` unless they change inspection, correspondence, hidden relation-structure return, governing-pattern application, or stop. The explanatory `nonAdmissibleUse` guard follows the full F.19:4 test and needs no absence entry unless a concrete receiving use requires that distinction.

#### C.30.TFS-REL:4.1 - Use trigger

Use this pattern only when an actual `ArchitectureRelation` occurrence, selected architecture-relevant structure, exact architecture structural view, functional-structure view, transformation-flow-structure claim, or conditional `ArchitectureDescription` use depends on one or more of the following:

- `TransformationFlowStructureRef`;
- `TransformationFlowStructureNetworkRef`, when architecture use selects an E.18.NET-conforming network;
- `PathId` or `PathSliceId`;
- `CrossingBundleRef`;
- flow valuation over the `U.Transfer` relation;
- edition, plane, or context pin;
- no-hidden-scalarization or set-return discipline;
- a correspondence claim or independently governed relation between functional structure and transformation-flow structure;
- a generated or extracted relation graph used as candidate input for the architecture-to-transformation-flow use.

If the sentence only says that Work occurred, use A.15.1 or the governing Work pattern. If it says that an actual referent changed, use A.3.4 before citing a `U.Transformation`. If it only says that one selected TFS exists, use E.18; if it only says that one independently identified E.18.NET-conforming TFS network is selected, use E.18.NET. If the sentence uses a graph-shaped expression as mathematical description, use E.18.2. If it relies on a mathematical lens, use C.29.

Use `transformationFlowUnfoldingStructureRef?` only when the architecture use depends on one A.22-selected CGUS qualified under `E.18.3`. The ref names that selected CGUS; its E.18.3 account separately names one independently identified E.18 substrate branch and the exact positions, bindings, and already-obtaining occurrences the CGUS uses. Architecture, decision, work, feedback, narrative, or refresh values connect only through exact already-obtaining supporting relations, with predicate-definition content and current facts when the claim needs them; the pattern reference adds no connection relation. Generic architecture use of a constraint-governed unfolding structure belongs in `C.32.P2S` or the direct C.30 architecture governing pattern; this pattern keeps only the architecture-to-transformation-flow trace.

#### C.30.TFS-REL:4.2 - Relation to functional structure

A `FunctionalStructureView` under C.30.ASV may cite `ArchitectureTransformationFlowStructureRelation` when a transformation-flow use is current. That record does not make the selected E.18 structure a functional element or actual transformation, and does not make a functional-element claim identical with the system, module, method, bearer, or flow. It states a bounded claim or trace that exact functional-view content corresponds to, or is declared relative to, one exact E.18 selected structure, member-local path, crossing, or valuation. Positive co-reference states that the functional-structure and flow-structure designations refer to the same selected `U.Structure`.

Keep the same three branches used by C.30.ASV:

- `functionalBehaviorClaimRefs` and `requiredOrDesiredEffectClaimRefs` remain C.2.1 claim content under their requirement, architecture, capability, method, functional-view, or other direct owner;
- `actualTransformationRefs` cite only independently identified A.3.4 occurrences with exact changed referent, boundary or extent, boundary conditions, actual before/during/after facts, and continuity or reidentification basis;
- `selectedTransformationFlowStructureRefs` cite exact E.18 structures, which may organize several independently identified transformations and transfers but are not themselves required effects or actual transformations.

A `FunctionalElementClaim` is a bounded C.2.1 claim about one exact selected functional structure. Its bearer or candidate-bearer locus, capability, port, allocation, transformation, and correspondence refs retain their direct owners. A graph-shaped expression, path, valuation, required-effect statement, or flow packet is therefore not the functional element by default.

```text
FunctionTransformationFlowRelationNote:
functionalStructureViewRef:
functionalElementClaimRef?:
functionalBehaviorClaimRefs?:
requiredOrDesiredEffectClaimRefs?:
actualTransformationRefs?:
selectedTransformationFlowStructureRefs?:
transformerSideFillerRef?:
candidateBearerRef?:
inputConditionRefs?:
outputConditionRefs?:
functionalPortRefs?:
transformationFlowStructureViewRef?:
architectureTransformationFlowStructureRelationRef:
pathOrSliceRef?:
crossingBundleRef?:
correspondenceClaimOrRelationRefs?:
preservedStructure:
lostOrHiddenStructure:
sourcePublicationOrEditionRef?:
extractionOrProbeLocusRef?:
relationObservationClassRef?:
unexploredRegionRefs?:
hiddenRelationStructureReturnCondition?:
admissibleUse:
stopOrReturnCondition:
nonAdmissibleUse?:
```

**Required-cooling-effect / later-actual-cooling countercase.** `RequiredCoolingEffect-1` can require exact Rack 7 to be below 30 °C and can correspond to a selected cooling-flow structure before any change occurs. In that first use, fill `requiredOrDesiredEffectClaimRefs` and the selected TFS fields; leave `actualTransformationRefs` empty. A later `Rack7CoolingTransformation-42` is actual only when A.3.4 fixes Rack 7 as the changed referent, its thermal boundary and operating/ambient conditions, actual 38 °C before facts, actual heat-removal during facts, actual 27 °C after facts, and continuity or reidentification of Rack 7. Even then, a separate satisfaction or realization predicate is needed before claiming that the actual transformation satisfies the earlier requirement.

Use this note when the practitioner needs to see whether the function-to-transformation-flow relation changes inspection, split, relation-making, downgrade, selection of the governing pattern for the claim named by value, candidate generation, or stop. Use C.30.ASV for the functional structure view, A.6.F for function-like wording recovery, A.3.4 for an actual transformation, A.6.M for module-claim repair and the direct allocation/interface owner, and E.18 for selected transformation-flow structure.

`FunctionTransformationFlowRelationNote` is the one-TFS form. When architecture use selects a network, use the top-level `ArchitectureTransformationFlowStructureRelation` and the branch in `C.30.TFS-REL:4.4a`. Name a member TFS in this note only when the function correspondence is actually to that member; membership in the selected network alone does not create a function correspondence.

When several transformation-flow variants are kept or compared as candidate architecture inputs, keep each selected transformation-flow structure, path, crossing, valuation, graph-shaped expression, or mathematical description under `E.18`, `E.18.2`, and this record. Apply `C.32` only to the architecture candidate palette that uses those selected structures. The graph, path, and flow description do not become architecture adequacy, evidence, assurance, gate passage, selected-set result declaration, publication occurrence, or decision by serving as a candidate input.

#### C.30.TFS-REL:4.3 - Claim-kind applications named by value

| Claim kind being made | Governing pattern to apply |
| --- | --- |
| Work occurrence or work result | `A.15.1` for the occurrence; `A.15` for Method/Work alignment; the governing work-result or P2W relation for those claims |
| Gate decision | `A.21` |
| Evidence claim | `A.10` or `G.6` |
| Assurance claim | `B.3` |
| Causal flow or intervention claim | `C.28` |
| Mathematical-lens use | `C.29` |
| Architecture adequacy, description use, or structural-view adequacy | `C.30` for architecture adequacy, `C.30.AD` for architecture-description use, or `C.30.ASV` for structural-view adequacy |
| Function-like wording | `A.6.F` |
| Interface, signature, or module compatibility | `A.6.M` for module-claim repair and the direct pattern for the interface claim; `A.6.5` only when reusable relation-participant typing is needed, and `A.6.0` when a signature declaration is being made |
| Architecture decision | the project-side architecture decision pattern when the corresponding claim is being made |

This table is the single boundary for generic non-flow claims. Apply F.19's plausible-reader test before adding a local guard. Relevant candidates include structure-as-architecture, graph-description-as-architecture, flow-as-work-log, crossing-as-gate, valuation-as-score, generated relation-graph proof, and prompt-data-tool flow as authority proof.

#### C.30.TFS-REL:4.4 - E.18 selected-structure boundary statement

For an E.18-governed selected `TransformationFlowStructure` used by an actual `ArchitectureRelation` occurrence, exact selected architecture structure, `ArchitectureStructuralView` episteme, or conditional `ArchitectureDescription` episteme, the architecture-use record may cite that exact E.18 structure plus MVPK faces and correspondence claims or independently governed relations.

Grounded architecture adequacy and bounded architecture claims are governed by C.30; description identity by C.30.AD; view conformance by E.17.0 and C.30.ASV. E.18 supplies selected transformation-flow structures and relations; it does not define all architecture structure kinds, create an architecture relation, or turn required flow content into actual change.

#### C.30.TFS-REL:4.4a - Architecture use of a transformation-flow structure network

First ask whether one exact named containing holon has an independently obtaining `ArchitectureRelation` whose exact selected structure is the same `transformationFlowStructureNetworkRef`. If not, ask whether the architecture question instead spans several exact named holons while no containing holon has been grounded. Select exactly one branch; a connected diagram, network record, list, or common claim label does not answer either question.

1. **Named containing-holon use.** Set `networkArchitectureUseBranch=namedContainingHolon`. Name exactly one `containingHolonRef` and one actual `containingArchitectureRelationRef` whose selected structure is the same exact network. `containingArchitectureClaimRef` is optional claim/trace content. Keep all participating arrays and `noNetworkBearerHolonAsserted` absent. Member TFS values and their Work, valuations, boundaries, actual transformations, and direct relations remain independently governed.
2. **Explicit inter-holon use.** Set `networkArchitectureUseBranch=explicitInterHolon`. Put at least two exact distinct holons in `participatingHolonRefs[]`. Add exactly the actual `participatingArchitectureRelationRefs[]` and bounded `participatingArchitectureClaimRefs[]` on which this question relies; a network member whose architecture is not used by the question stays outside those arrays. Keep all containing fields absent and set `noNetworkBearerHolonAsserted=true`. This states one architecture-use question spanning named holons; it does not invent a containing holon, architecture relation, or characteristic bearer whose identity is the network.

Every other populated architecture-side reference must agree with the selected branch. In `namedContainingHolon`, each value in `selectedArchitectureStructureRefs` belongs to the containing architecture relation's selected structure route, and each structural view, architecture description, functional structure view, or architecture claim used by this record traces to the same exact containing holon and relation. In `explicitInterHolon`, each such reference traces to one named participating holon and, when actual, its exact architecture relation; a singular reference names only that participant and does not imply a containing architecture. If a reference depends on another holon or architecture relation, add it only when the current question actually relies on it, or use a separate record.

The branches are mutually exclusive. When `transformationFlowStructureNetworkRef` is absent, `networkCrossFlowRelationRowRefs[]` and all network branch fields are absent. A network ref without one complete branch is not ready for architecture use. When the record also names a path, slice, crossing, valuation, required effect, or actual transformation, bind it to the exact member TFS and the local positions, participants, or bindings that identify that value. When it names a network-aware unfolding, the E.18.3 substrate branch must name the same exact network and preserve its admitted position mappings, while `selectedCGUSRef` continues to name the separate A.22-selected CGUS. The network ref does not lift member-local values into network-global state.

Use `networkCrossFlowRelationRowRefs[]` only for E.18.NET-owned composite locators. Each locator's current containing record must describe the same exact selected network, and the direct occurrence plus complete ordered endpoint-binding identity must resolve exactly one nested row. Zero matches, several matches, or a record for a different network stop this architecture use. The locator identifies the row; it neither creates the relation occurrence nor changes its direct governor.

For every maintainability, capability, responsibility, production, safety, or other architecture-characteristic claim made or used by this record, name the exact holon, actual architecture relation, selected structure, description/view episteme, bounded claim, or other bearer governed by C.30 or the characteristic's direct owner. A network may have selected structural facts—members, relations, recursion, or exposed positions—but those facts do not make an unnamed network the bearer of holon characteristics, agency, Work, production, required effects, or actual transformations.

A network diagram, member graph, mathematical description, publication, or `TransformationFlowStructureNetworkRecord` is neither branch and does not enter architecture identity. It may represent, describe, or publish the selected network only under its direct representation, description, or publication pattern.

**Named containing-holon case.** Exact holon `ManufacturingPlatform-7` has one obtaining architecture relation whose selected structure includes the product-development/production-system-change network. C.30.TFS-REL may use that network to localize an architecture change while each member TFS, production relation, Work occurrence, and actual transformation keeps its own owner.

**Explicit inter-holon case.** Exact supplier holon and exact plant holon use one selected E.18.NET-conforming supply-linked TFS network to inspect a cross-company dependency. Both appear in `participatingHolonRefs[]`, with only the actual architecture relations and claims the question uses in their corresponding arrays. No containing supply-chain holon has been grounded, so `noNetworkBearerHolonAsserted=true`. The network is not called the architecture of an unnamed enterprise.

#### C.30.TFS-REL:4.5 - Worked slices

**Functional architecture with a transformation-flow relation being claimed.** A team says, "The functional architecture is this flow diagram." The repair is:

```text
functionalStructureViewRef: exact view episteme about required effects and dependencies
functionalElementClaimRefs?: not used; no filled functional-element claim is current
functionalBehaviorClaimRefs?: required-effect claim `authorize payment`
requiredOrDesiredEffectClaimRefs?: required-effect claim `authorize payment`
actualTransformationRefs?: not used; no A.3.4 actual change is claimed
selectedTransformationFlowStructureRefs: exact selected payment-authorization TFS
transformerSideFillerRefs?: not used
candidateBearerRefs?: not used
inputConditionRefs?: not used
outputConditionRefs?: not used
functionalPortRefs?: not used
transformationFlowStructureViewRef: exact description/view episteme about the selected E.18 structure, path, crossing, or flow valuation
transformationFlowStructureRef: TransformationFlowStructure@PaymentAuthorization
selectedPathOrSliceRefs: path slices used for the architecture claim
correspondenceClaimOrRelationRefs: bounded claim that the required effect corresponds to the flow path
stopOrReturnCondition: stop at the bounded correspondence claim; open actual transformation, Work, evidence, gate, or decision use only through its direct predicate
nonAdmissibleUse?: flow diagram as functional architecture itself
```

Filled use record:

```text
ArchitectureTransformationFlowStructureRelation:
architectureRelationOccurrenceRefs: exact obtaining CheckoutService architecture relation
architectureClaimRefs: bounded CheckoutService architecture claim when current
selectedArchitectureStructureRefs: exact selected request-handling and payment-authorization structure
architectureStructuralViewRefs: exact CheckoutRuntimeFlow view episteme
architectureDescriptionRefs: not used; durable description adequacy is not being evaluated here
functionalStructureViewRefs: exact CheckoutRequiredEffects view episteme
functionalElementClaimRefs: not used
functionalBehaviorClaimRefs: required-effect claim `authorize payment`
requiredOrDesiredEffectClaimRefs: required-effect claim `authorize payment`
actualTransformationRefs: not used
selectedTransformationFlowStructureRefs: TransformationFlowStructure@Checkout-v3
transformerSideFillerRefs: not used
candidateBearerRefs: not used
inputConditionRefs: not used
outputConditionRefs: not used
functionalPortRefs: not used
transformationFlowStructureViewRefs: exact PaymentAuthorizationPath description/view episteme
transformationFlowStructureRef: TransformationFlowStructure@Checkout-v3
selectedPathOrSliceRefs: PathSlice@request-to-payment-authorization
crossingBundleRefs: not used
flowValuationRefs: not used
mathematicalDescriptionRefs: not used
correspondenceClaimOrRelationRefs: claim that required effect `authorize payment` corresponds to the E.18 path slice; this is correspondence, not identity or actual change
sourcePublicationOrEditionRef: model or generated-graph edition when the flow relation was extracted from one
extractionOrProbeLocusRef: path-slice extraction or code-agent probe locus when current
relationObservationClassRef: observed, inferred, or unknown relation class when current
unexploredRegionRefs: not used
hiddenRelationStructureReturnCondition: reopen if mathematical-description edition, path slice, relation observation class, or required-effect declaration changes
admissibleUse: inspect whether the functional structure view depends on the E.18 path slice and whether an architecture split or correspondence claim is needed
stopOrReturnCondition: stop at the bounded architecture-to-flow correspondence and reopen when its source, path, observation class, or required-effect declaration changes
```

Cooling countercase: a selected cooling-flow TFS and `RequiredCoolingEffect-1` may fill the required-effect and correspondence fields while `actualTransformationRefs` stays empty. Only a later A.3.4 occurrence with Rack 7 as exact changed referent, fixed thermal boundary and conditions, actual 38 °C before / heat-removal during / 27 °C after facts, and Rack 7 continuity can fill that field. A separate realization predicate is still needed to relate the actual cooling to the requirement.

Near miss: if the selected transformation-flow structure has no exact C.30-side architecture reference named by value, the case stays in `E.18`. If the same sentence is a mathematical description, use `E.18.2`; if it is a math-lens-use claim, use `C.29`. If it is a Work log, evidence claim, gate decision, or benchmark result, that non-flow claim is governed by its governing pattern and this record keeps only the architecture-to-transformation-flow use.

**Pump-station flow relation.** A plant team says, "the safety architecture is the bypass flow." C.30.TFS-REL applies only if the exact plant holon, its actual architecture relation or bounded architecture claim as current, selected control or material-flow structure, and E.18 selected bypass-flow structure are named. The bypass path may be architecture-relevant, but it is not an actual cooling/pumping transformation, safety proof, performed maintenance Work, gate passage, or release permission. The record names the plant architecture locus, selected E.18 path or crossing, hidden relation-structure return condition, and the one architecture move changed by the bypass relation.

**Supply-chain transformation-flow relation.** A logistics architecture view may use an E.18 selected flow structure for supplier handoff, transport crossing, freshness window, and valuation. The exact subject holons, actual architecture relations when claimed, and selected supply-chain structures remain named; Work occurrences, contractual commitments, evidence, and gate decisions stay with their governing patterns.

**Neural-network dataflow change.** Source labels such as attention block, SSM block, convolution block, memory mechanism, cache mechanism, and MoE expert-selection go through `C.30.STRAT` unless the changed value is already recovered. C.30.TFS-REL applies only when the exact changed structure kind and transformation-flow relation are named. A benchmark, ablation, or pruning result may bear on a non-architecture claim named by value, but it does not make the flow relation an architecture decision, actual transformation, or evidence sufficiency by itself.

**Code-agent relation graph.** A code-agent relation graph with `IMPORTS`, `CALLS_API`, `REGISTRY_WIRES`, or `DATA_FLOWS_TO` edges can be used for an architecture-to-transformation-flow relation only with the source publication or codebase edition, extraction or probe locus, relation observation class selected from {observed, inferred, unknown}, typed relation semantics, unexplored regions, and hidden relation-structure return condition when subsequent action relies on hidden distinctions. The graph, representation, file, and publication occurrence remain distinct from both the selected TFS and every direct relation occurrence.

#### C.30.TFS-REL:4.6 - Lowering and currentness conditions

Lower, narrow, or reopen the relation at the smallest changed locus when:

- E.18 one-TFS structure, path, crossing, or flow-valuation semantics change;
- E.18.NET network identity, direct membership, exposed positions, exact cross-member relations, or nested-row locator resolution changes;
- the selected network architecture branch or any containing or participating architecture claim used by that branch changes;
- edition, plane, context pin, set-return, or no-hidden-scalarization discipline changes;
- source publication or graph edition, path slice, relation observation class, edition or context pin, unexplored region, or hidden relation-structure return condition changes;
- the C.30 architecture locus, selected architecture-relevant structure, architecture structural view, conditional architecture description, or C.30.ASV relation changes;
- functional-to-transformation-flow correspondence changes;
- a non-flow claim is being made and requires the direct governing pattern identified in `C.30.TFS-REL:4.3` rather than this architecture-to-flow record;
- C.29, C.16, C.28, A.10, G.6, B.3, A.20, A.21, A.15.1, A.15, C.30, C.30.AD, C.30.ASV, A.6.F, C.30.STRAT, E.18, or E.18.NET changes the governing boundary used by the relation.

Admissible repair results are: update the affected TFS or network reference, network branch, or row locator; add or change correspondence or the hidden relation-structure return condition; narrow admissible use; keep the one-TFS claim inside E.18 and the network claim inside E.18.NET; keep the mathematical-description claim inside E.18.2; keep the math-lens-use claim inside C.29; apply the governing pattern to a non-flow claim; lower to quote-only or reduced-use cue; or block the architecture-to-transformation-flow use.

### C.30.TFS-REL:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner sees one TFS or several connected TFSs and wants to use that flow structure in an architecture question. C.30.TFS-REL makes them name the exact TFS or network and exact architecture locus; for a network, they choose one containing holon/relation or the exact participating holons and relations/claims. The result is one usable trace or an exact stop, not an architecture relation inferred from the diagram. |
| Show: `U.System` | A software system, plant, AI agent, neural network, vehicle, or supply chain may have transformation-flow structure. A diagram or mathematical description can inform architecture reasoning about that structure without carrying the required-effect, actual-transformation, or other non-flow claims named in `C.30.TFS-REL:4.3`. |
| Show: `U.Episteme` | For a mathematical graph description, generated relation graph, code-agent probe output, neural-network diagram, dashboard, or architecture note, distinguish the description episteme from its representation or publication; E.17.0 governs whether that episteme is a view. The episteme can support the transformation-flow use only when exact E.18 TFS or E.18.NET network, the selected network architecture branch when applicable, edition/plane/context pins, correspondence, any relied-on row locator, hidden relation-structure return condition, and admissible use are recoverable. |

### C.30.TFS-REL:6 - Bias-Annotation

Bias lenses: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: architecture-to-transformation-flow uses of E.18 TFS or E.18.NET network objects.

| Bias risk | Mitigation |
| --- | --- |
| Structure-or-description-as-architecture bias | Direct architecture relations and bounded claims stay with C.30, descriptions with C.30.AD, mathematical representations with C.29, mathematical descriptions with E.18.2, math-lens uses with C.29, and structural views with C.30.ASV/E.17.0. |
| Function-flow/change collapse | Required functional content, selected transformation-flow structure, and actual A.3.4 transformation remain separate. Functional and flow structures are related, not identical by default. |
| Non-flow claim overread | The relation table assigns non-flow claim kinds to their governing patterns. |
| Mathematical overread | Mathematical-lens use of a graph or valuation is governed by C.29. |
| Check-only bias | Conformance checks include repair actions and stop conditions. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, use record, direct relations, or repair guidance above.

### C.30.TFS-REL:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-C30TFR-1 Flow-structure object.** | The record names the exact E.18 TFS, E.18.NET network, path, slice, crossing, or flow valuation object it uses. | Add the exact E.18 or E.18.NET reference named by value, or use C.30 or C.30.ASV without this record. |
| **CC-C30TFR-2 Architecture locus.** | The record names an actual `ArchitectureRelation`, exact selected architecture structure, exact `ArchitectureStructuralView` or `ArchitectureDescription` episteme, or bounded `ArchitectureClaim`. | Add the exact architecture relation/structure/episteme/claim as the selected use requires; otherwise keep the TFS or network claim with E.18 or E.18.NET, the mathematical-description claim with E.18.2, or the math-lens-use claim with C.29. |
| **CC-C30TFR-3 Functional, required, flow, and actual-change separation.** | Required/desired behavior and effect remain claim content; selected TFS remains structure; an `actualTransformationRef` appears only with the complete A.3.4 changed-referent, boundary, conditions, before/during/after, and continuity/reidentification basis. Functional and flow structure co-reference is explicit rather than assumed. | Repair through `FunctionTransformationFlowRelationNote`; split the required claim, selected structure, and actual transformation; add correspondence or positive selected-structure co-reference only when its predicate is governed. |
| **CC-C30TFR-4 No architecture takeover.** | The selected transformation-flow structure, network, mathematical description, or use record is not treated as generic architecture ontology or all architecture structure kinds. | Assign actual architecture relations, selected architecture-relevant structures, bounded claims, or description use to C.30/C.30.AD and keep this pattern to the architecture-to-transformation-flow trace. |
| **CC-C30TFR-4a Network architecture branch.** | A network use selects exactly one branch. The containing branch has one exact holon and actual architecture relation whose selected structure is the exact network. The inter-holon branch has at least two exact holons, exactly the actual architecture relations and bounded claims this question uses, no containing fields, and `noNetworkBearerHolonAsserted=true`; a singular participant ref never implies a containing architecture. | Complete one branch, remove or reroute a conflicting architecture-side ref, add a participant only when the current question relies on it, or keep the network claim under E.18.NET without architecture use. |
| **CC-C30TFR-4b Named characteristic bearer and representation boundary.** | Every architecture characteristic claimed or used remains on an exact named holon, actual architecture relation, selected structure, view/description episteme, bounded claim, or other governed bearer; no graph, representation, mathematical description, publication, or network record becomes that bearer merely by presenting it. | Name the exact bearer under C.30 or its direct owner; demote the visible object to representation, description, or publication use. |
| **CC-C30TFR-4c Member-local, unfolding, and row-reference boundary.** | Every path, slice, crossing, valuation, required effect, or actual transformation named with a network remains bound to its exact owning member TFS and local positions, participants, or bindings; a network-aware unfolding selects the same network through its E.18.3 locator; every `NetworkCrossFlowRelationRowRef` resolves exactly one row in a current record for that network without replacing the obtaining relation occurrence. | Restore the member-local binding or network-locator match; repair or remove a row locator that resolves zero or several rows or points to another network; keep occurrence truth with its direct governor. |
| **CC-C30TFR-5 Work boundary.** | Establish any Work occurrence through A.15.1 and any work-result claim through its governing predicate. | Keep the selected TFS, network, path, or slice as the flow-structure reference used by that claim; use A.15 for Method/Work alignment. |
| **CC-C30TFR-6 Evidence, assurance, and gate boundary.** | Establish any evidence-sufficiency, assurance, internal-constraint, gate-decision, or release-permission claim through its direct governing application and result. | Apply A.10 or G.6 for evidence, B.3 for assurance, A.20 for an internal-constraint result, A.21 for a named gate decision, or the direct domain pattern for the particular release, admissibility, or approval claim. |
| **CC-C30TFR-7 Causal and mathematical boundaries.** | Causal or intervention claims and mathematical-lens claims are assigned to C.28 and C.29. | Apply those governing patterns or narrow the record's admissible use. |
| **CC-C30TFR-8 Pin and scalarization boundary.** | Edition, context, and plane pins plus no-hidden-scalarization claims remain E.18-governed. | Add E.18 pin and set-return references or remove the comparison or selection claim. |
| **CC-C30TFR-9 Hidden relation return.** | Extracted, generated, coarsened, or partial relation graphs or flow diagrams state the source publication or edition, extraction or probe locus, relation observation class, unexplored regions, and hidden relation-structure return condition when hidden distinctions affect action. | Add the missing relation-structure fields or narrow the admissible use. |
| **CC-C30TFR-10 Useful action.** | The repair leaves a remaining use: name the selected TFS, path, or crossing; choose the containing or inter-holon branch for a selected network; add correspondence; return to source; assign the claim being made to a governing pattern; or stop. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |
| **CC-C30TFR-11 Lowering and currentness.** | The record states the smallest changed locus when E.18 TFS semantics or pins, E.18.NET network identity or relations, selected network branch or architecture loci, a relied-on row locator, relation observation class, correspondence, hidden relation-structure return, or related governing boundary changes. | Update the affected TFS/network reference, branch, architecture locus, or row locator; narrow admissible use; keep subject claims with their direct owners; lower the record; or block architecture-to-transformation-flow use. |

### C.30.TFS-REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-architecture** | The E.18 selected transformation-flow structure is called the whole architecture. | Use C.30 for the actual architecture relation, selected structure, or bounded claim; C.30.AD for description; keep this record only for the transformation-flow use. |
| **Unnamed network as architecture bearer** | A connected network or its graph is assigned maintainability, capability, responsibility, agency, production, required effect, or actual transformation without one containing holon/relation or explicit participating holons. | Select the named-containing-holon or explicit inter-holon branch, restore every characteristic to a named bearer, and keep graph/record outside architecture identity. |
| **Graph-description-as-functional-architecture** | A graph-shaped mathematical description or diagram is treated as functional architecture, functional element, or actual change. | Split functional claim, selected TFS, actual transformation, mathematical description, representation, and publication; add correspondence when needed. |
| **Flow-as-work-log** | Path or slice wording is treated as Work occurrence. | Use A.15.1 for the occurrence and the governing work-result or P2W relation for those claims; keep E.18 to selected structure, path, slice, or valuation. |
| **Crossing-as-gate-result** | A crossing relation is treated as gate passage. | Assign gate-decision claims to A.21 and keep crossing relation under E.18. |
| **Valuation-as-score** | A flow valuation is used as a generic architecture score. | State E.18 valuation and set-return discipline; assign measurement, characterization, selection, or candidate-set claims to `C.16` or an admitted governing pattern. |
| **Generated relation-graph proof** | A code-agent relation graph or probe output is used as proof of architecture understanding or safety. | Recover source publication/codebase edition, extraction/probe locus, observation class from {observed, inferred, unknown}, unexplored regions, hidden structure, and direct evidence or assurance application. |
| **Prompt-data-tool flow as authority proof** | A prompt, data, or tool-flow diagram is treated as permission for tool action or proof that authority is safe. | Keep it as a transformation-flow use or E.18.2 mathematical description. Route a selected `SecurityTrustBoundaryStructure` view through C.30.ASV; for agentic tool use, route call planning to `C.24` after the action or option is fixed and autonomy-budget enforcement to `E.16`. Use `A.20` for an internal-constraint result, `A.21` for a named gate decision, or the direct domain pattern for the particular release, admissibility, or approval claim when that claim is current. |

### C.30.TFS-REL:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| E.18 TFS paths, crossings, valuations, and E.18.NET network structure become usable across actual architecture relations, selected architecture structures, exact structural views, and conditional descriptions without merging owners. | Every use names the exact architecture locus. A network use also names either one containing holon/relation or all exact participating holons and needed relations/claims, and keeps every characteristic on a named bearer. |
| Required functional content, transformation-flow structure, and actual transformation stay separable. | Concise "the diagram is the architecture/change" prose is repaired before it carries an FPF claim. |
| Non-flow claim kinds are assigned to their governing patterns. | More governing patterns are named when practitioners try to overuse the diagram, mathematical expression, or selected structure. |
| The E.18 selected-structure boundary stays narrow. | Generic architecture adequacy remains outside E.18. |

### C.30.TFS-REL:10 - Rationale

E.18 governs one selected TFS, its paths, crossings, valuations, and pins; E.18.NET governs one selected network and its exact cross-member relations. Architecture needs to use either object without taking over its ontology or inventing an unnamed architecture bearer. The smallest stable result is therefore one C.30-side use record pointing to exact objects and stating the named-containing-holon or explicit inter-holon branch when a network is selected.

This pattern also protects functional architecture and actual-change semantics. A functional structure may correspond to a transformation-flow structure, and in some cases both views may designate the same selected `U.Structure`; that identity is not automatic. Required or desired effect remains claim content, while an actual `U.Transformation` requires the independent A.3.4 basis.

### C.30.TFS-REL:11 - SoTA-Echoing

| Practice or reference line | C.30.TFS-REL adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| E.18 one-TFS discipline and E.18.NET network discipline | Adopt E.18 as owner of one TFS, paths, crossings, and valuations; E.18.NET as owner of one selected network, member-local references, and exact cross-member relations. | Name the exact TFS or network, then add only the exact C.30 architecture locus and selected network branch. | Neither flow-structure owner becomes generic architecture or architecture-description ontology. |
| ISO/IEC/IEEE 42010:2022 and multi-view architecture practice | Adapt view and correspondence discipline to architecture-to-transformation-flow reliance. | Transformation-flow views relate to actual architecture relations, selected structures, exact structural views, or conditional descriptions through C.30, C.30.AD, C.30.ASV, and correspondence claims/relations. | Architecture views do not become proof, evidence, gates, decisions, required-effect realization, or actual transformation by view status alone. |
| MBSE and SysML v2 view and relation practice | Adapt model-derived flow views and path views as descriptions derived from a model publication or edition. | A model-derived flow description states model edition, selected structure, hidden/lost structure, and admissible use. | Tool models or query results do not establish FPF E.18, C.30, A.3.4, or E.17.0 relations without their defining predicates and case facts. |
| Neural-network dataflow and GonzoML architecture-operation corpus | Adopt practitioner recognition for block replacement, path selection, memory/cache placement, MoE expert selection, pruning, distillation, ablation, and compute/memory/latency tradeoffs. | Keep source labels with `C.30.STRAT` until exact values are recovered; C.30.TFS-REL applies only when recovered flow structure changes the architecture move. | Benchmarks, ablations, pruning masks, or search outputs do not become evidence, assurance, gate passage, actual transformation, or architecture decision by themselves. |
| Theory of Code Space (arXiv:2603.00601) code-agent relation graph probing | Adapt component-belief statuses from {observed, inferred, unknown} and partial-observability warnings to relation-graph use. | Generated code relation graphs can be used only with typed relation semantics, source/codebase edition, extraction/probe locus, unexplored regions, and hidden-relation return condition. | Do not mint `U.CodeSpace`; probe output alone does not prove internal belief or establish architecture adequacy, assurance, or a release-evidence claim. |

**Currentness boundary.** Inputs are E.18 TFS semantics and pins; E.18.NET network identity, cross-member relations, and row-locator resolution when selected; the chosen network architecture branch and exact containing or participating holons/relations/claims; C.30/C.30.AD/C.30.ASV architecture-side rules; observation class; required-versus-actual status; and non-flow governors named in `C.30.TFS-REL:4.3`. When one changes, the record changes only at the affected reference, branch, row locator, correspondence, hidden relation-structure return condition, admissible-use boundary, or governing-pattern assignment.

### C.30.TFS-REL:12 - Relations

Builds on: `C.30`, `C.30.AD`, `C.30.ASV`, `A.22`, `A.6.F`, `A.3.4`, `E.18` for one TFS, `E.18.NET` for one selected conforming network and exact obtaining cross-member relations, `E.17.0`, `E.24.PUB`, `A.7`, `E.10`, `C.2.P`, and `F.18`.

Coordinates with: `C.30.STRAT`, `C.32.P2S` when architecture-to-transformation-flow grounding is one stage of problem-to-structure architecturing, `C.32` when selected transformation-flow variants become candidate architecture inputs, `C.33` when transformation-flow relation descriptions capture or lose selected architecture structure, `C.34` when transformation-flow claims must be preserved across a mapping, model, generated output, or realization, `C.35` when a generated or discovered carrier may seed synthesis, `A.15.1` for Work occurrence, `A.15` for Method/Work alignment, `A.20`, `A.21`, `A.10`, `G.6`, `B.3`, `C.28`, `C.29`, `C.16`, admitted measurement, selection, or candidate-set governors, `A.6.M` module-claim repair and direct interface owner, `A.6.5` when reusable relation-participant typing is needed, and `A.6.0` when a signature declaration is being made.

Related claims stay with their governing patterns: `C.30.STRAT` for stratification wording and source-label repair; E.18 for one selected TFS, path, crossing, and flow valuation; E.18.NET for network identity and exact cross-member relations; E.18.2 for mathematical descriptions and C.29 for mathematical representations and lens use; C.30 for direct architecture relations and selected-structure adequacy; C.30.AD for description identity/use; E.17.0/C.30.ASV for structural-view conformance and adequacy; A.3.4 for actual transformations; C.32.P2S for connected problem-to-structure carry-through; A.6.F for function-use repair; and the non-flow governors named in section 4.3. C.30.TFS-REL governs only the bounded architecture use of the selected TFS or TFS network.

### C.30.TFS-REL:End

