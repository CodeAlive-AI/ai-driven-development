## B.2 - Meta-Holon Transition - Whole Reidentification

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.2:0 - Use This When

Use this pattern when a configured whole can no longer be treated as the same whole for the current claim: its delimitation, part relation, constitutive assembly, objective, supervision, capability envelope, agency threshold, or temporal consolidation has changed enough that the EntityOfConcern must be reidentified.

Typical moments:

- a set of coordinated parts becomes a regulated system with its own objective and externally visible commitments;
- a commissioning history crosses into operation and the assurance claim must restart for the operational whole;
- a theory, model family, or knowledge body becomes an episteme whole recognized under the already admitted `U.Episteme` kind rather than remaining a loose catalogue;
- separately governed structure, functioning, method, and work facts support a capability envelope that the existing whole cannot explain; evidence separately supports the claim about those facts;
- an architecture residual cannot be explained inside the existing whole.

**First useful move.** Compare the observed gain or shift with explanations that preserve the existing whole. If better parts, corrected relations, improved measurement, Method or Work repair, richer phase coverage, or architecture-view repair is sufficient, stay with the existing whole and use that subject pattern. Use B.2 only when the whole itself must be reidentified.

**What goes wrong if missed.** Emergence becomes rhetoric, ordinary improvement is overclaimed as a new whole, or a genuinely new whole remains hidden under old part, evidence, assurance, architecture, or responsibility claims.

**What this buys.** B.2 gives one accountable whole-reidentification move: recover the exact existing whole, the separately governed facts that challenge its identity, the exact candidate new whole, and decide whether the existing whole continues or the new whole must carry the claim before relying on evidence, a record, or a receiving-use decision.

**Not this pattern when.**

- If the claim is ordinary part-whole construction, use `B.1`, `A.14`, and `C.13`.
- If the claim is a whole-level characteristic change, use `C.16` and the direct measurement or evaluation pattern.
- If the claim is capability without whole reidentification, use the direct capability and characteristic patterns.
- If the claim is transformation or work, use `A.3.4`, `A.12`, `A.15`, and `A.15.1`.
- If the claim is only wording repair for emergence-family language, use `B.2.P` first.
- If the claim is graph, RG-like, MSPD, or other mathematical expression, use `C.29` unless whole reidentification is also current.

### B.2:1 - Problem Frame

A Meta-Holon Transition is not a new root ontology, generic emergence label, or mathematical graph result. It is a whole-reidentification claim about an exact holon already recognized through A.1 construction, identity, part relations, whole-level characteristics, and a direct kind-specific pattern.

The old whole remains a possible explanatory object. Use B.2 only when the old whole is no longer the right EntityOfConcern for the current claim. The candidate new whole can be recognized as a `U.System`, `U.Episteme`, `U.Method`, `U.Work`, `U.Discipline`, or another holon kind only after `E.24.UK` has admitted that public kind and the exact candidate satisfies A.1 plus the direct kind-specific criterion.

### B.2:2 - Problem

Without B.2:

1. **New whole is missed.** A constructive assembly or coordinated closure changes the object, but evidence and architecture still point to old parts.
2. **Ordinary improvement is overclaimed.** A better component, stronger measurement, or corrected method is called emergence.
3. **Record fields become ontology.** A result field, trigger mnemonic, profile, or checklist is treated as a U-kind or actor.
4. **Agency becomes binary.** A threshold crossing is read as “agent or not agent” instead of a characteristic-space threshold for an admitted System. A local system-role kind, classification, or assignment is a separate optional fact and neither establishes nor is required for the agency characteristic.
5. **Mathematics replaces ontology.** A graph, RG-like flow, MSPD score, or benchmark jump is treated as MHT without recovering the holon claim.
6. **Transformation becomes containment.** A system changing another holon is treated as its part or the larger whole containing it without a separately obtaining part-whole relation.

### B.2:3 - Forces

| Force | Tension |
| --- | --- |
| Parsimony vs real novelty | FPF should not mint new wholes for every improvement, but some closures really change the EntityOfConcern. |
| Continuity vs reidentification | History and phase continuity matter, but some transitions require identification of a new whole. |
| Trigger recognition vs trigger inflation | Delimitation, part-relation, objective, supervision, capability, agency-threshold, and temporal cues help recognition but do not declare MHT by themselves. |
| System-facing emergence vs broader holons | Holonic systems literature is system-facing, while FPF also needs cases in which the candidate new whole is an episteme, method, work occurrence, or discipline. |
| Math-lens power vs ontology discipline | RG-like, graph, algebraic, or benchmark expressions can bear on a claim only after the holon and relation are named. |

### B.2:4 - Solution

Use B.2 as a world-side whole-reidentification pattern. Start with the actual wholes and the facts governed by their direct patterns; add records only when a receiving use needs them.

1. Name the exact existing whole, its admitted kind, and its identity or reidentification rule.
2. Recover each changed delimitation, constituent, constructive part relation, assembly, supervision, objective, capability, characteristic, or temporal fact under its direct pattern. A cue word, profile field, measurement, or graph edge does not make the fact obtain.
3. Test whether those facts can be explained as a change of the same whole. If repair, maintenance, changed characteristics, phase coverage, method or work correction, measurement, or architecture-view correction is enough under the existing reidentification rule, keep that whole and stop B.2.
4. If the existing whole is not enough, identify the exact candidate new whole and execute the complete A.1 criterion. Recover its constituents, obtaining constructive relations, assembly, reidentification rule, and composition-grounded whole characteristic. Also show that the candidate's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions satisfy the applicability and compatibility conditions of at least one governed larger-assembly construction method or rule under which it can remain a constituent. Then name its already admitted holon kind and satisfy the direct kind-specific criterion. If a required condition fails, the candidate fails A.1; if missing evidence or an unavailable dependency prevents a determination, evaluation returns `unknown`.
5. State the whole-reidentification claim: why the existing whole no longer carries the current subject claim and why the candidate new whole is the EntityOfConcern. This comparison does not itself create, admit, or classify either whole.
6. Materialize a trigger profile, optional explanation-result episteme, reidentification assertion, or record only when a named receiving use must inspect, cite, compare, or preserve that claim.

The optional `MHTTriggerProfile`, `ExistingWholeExplanationResult`, and `HolonReidentificationRecord` are ordinary C.2.1 epistemes. Their content can designate exact wholes, facts, claims, and relation occurrences; the content fields are not world-side participants and supply no substitute for the preceding move.

#### B.2:4.1 - MHTTriggerProfile

`MHTTriggerProfile` is a `U.Episteme` whose EntityOfConcern is the exact existing whole already recognized under an admitted holon kind. It collects exact current cues and support for asking whether whole reidentification is live. It is not MHT itself, and its content fields do not declare another relation.

| Content field | Value kind and use |
|---|---|
| `existingWholeRef` | `U.HolonRef` resolving to the exact existing whole already recognized under an admitted holon kind. |
| `existingWholeIdentityRuleRef` | `U.EpistemeRef` resolving to the current identity-rule episteme. |
| `currentPartRelationRefs[]` | `U.EntityRef` values, each resolving to one explicitly individuated current part-relation occurrence. |
| `changedDelimitationRelationRefs[]` | References to exact changed delimitation relation occurrences under their direct patterns. |
| `changedPartRelationRefs[]` | References to exact changed part-relation occurrences. |
| `changedSupervisionRelationRefs[]` | References to exact changed supervision relation occurrences. |
| `changedCoordinationRelationRefs[]` | References to exact changed coordination relation occurrences. |
| `changedObjectiveClaimRef?` | `U.EpistemeRef` resolving to the exact objective-change claim. |
| `changedCapabilityClaimRef?` | `U.EpistemeRef` resolving to the exact capability-change claim. |
| `agencyThresholdClaimRef?` | `U.EpistemeRef` resolving to a current characteristic-space threshold claim. |
| `temporalConsolidationClaimRef?` | `U.EpistemeRef` resolving to the exact temporal-consolidation claim. |
| `evidenceRelationRefs[]` | References to exact evidence relation occurrences supporting the trigger claims. |
| `sourceUseRelationRefs[]` | References to exact source-use relation occurrences when a source is relied on. |

The profile's effective `U.ReferenceScheme`, any current `U.ClaimScope`, and an independently selected model-use structure can qualify this episteme under C.2.1 when its receiving use needs them. They do not identify either whole, become MHT trigger facts, or make any referenced relation obtain. A single cue warrants attention; it does not establish whole reidentification.

#### B.2:4.2 - Existing-whole comparison and optional result

First perform an ordinary comparison: compare the observed change with direct explanations that preserve the existing whole. Consider better parts, corrected relations, improved measurement, method or Work repair, richer phase coverage, capability change, and architecture-view repair only when their direct patterns make those explanations current. If one explanation is sufficient for the receiving use, keep the existing whole, use that subject pattern, and stop B.2.

When another use must inspect or cite the outcome, identify an optional `ExistingWholeExplanationResult` episteme whose EntityOfConcern is the existing whole:

| Content field | Value kind and use |
| --- | --- |
| `observedChangeClaimRef` | `U.EpistemeRef` resolving to the exact observed-gain or observed-shift claim. |
| `candidateExplanationClaimRefs[]` | Exact claims under their direct subject patterns. |
| `explanationEvidenceRelationRefs[]` | Evidence relations actually used to assess those explanations. |
| `existingWholeSufficiencyVerdict` | `sufficient | insufficient | unknown` for the named receiving use. |
| `remainingWholeReidentificationQuestionRef?` | The exact residual question when the result is `insufficient` or `unknown`. |

The comparison is an action a practitioner performs. The optional result records its claim-bearing outcome. Neither is a reusable checklist or Method unless an independent receiving use later requires and defines such an object. The episteme creates none of its referenced claims or relations.

#### B.2:4.3 - HolonReidentificationRecord
`HolonReidentificationRecord` is an optional `U.Episteme` whose EntityOfConcern is the exact new holon. Use it only when a person or system performing later work needs a durable account of why that new holon, rather than the prior whole, is the current EntityOfConcern. Candidate classification remains a separately governed judgment.

| Content field | Value kind and use |
|---|---|
| `existingWholeRef` | `U.HolonRef` resolving to the exact prior whole already recognized under an admitted holon kind. |
| `selectedTriggerProfileRef` | `U.EpistemeRef` resolving to the selected `MHTTriggerProfile`. |
| `existingWholeExplanationResultRef?` | `U.EpistemeRef` resolving to the optional `ExistingWholeExplanationResult`; omit it when the ordinary comparison sentence is enough. |
| `resultHolonRef` | `U.HolonRef` resolving to the exact candidate new whole. |
| `resultHolonKindRef` | `U.KindRef` resolving to its exact admitted holon kind. |
| `resultHolonClassificationAssertionRef?` | `U.EpistemeRef` resolving, only when a person or system performing later work must inspect or cite the judgment, to a C.2.1 assertion that the candidate new whole satisfies the A.1 criterion under the stated admitted holon kind. |
| `wholeReidentificationClaimRef` | `U.EpistemeRef` resolving to the claim that the candidate new whole, rather than the prior whole, now carries the subject claim. |
| `changedClaimPatternLocators[]` | `U.EpistemeRef` values resolving to the direct patterns for each changed claim used in the rationale. |
| `evidenceRelationRefs[]` | References to exact evidence relation occurrences supporting the reidentification claim. |
| `sourceUseRelationRefs[]` | References to exact source-use relation occurrences when sources are relied on. |
| `mathLensUseRelationRefs[]` | References to exact C.29 lens-use relations when mathematical results bear on the claim. |

The record does not make the A.1 criterion true, admit a public kind, or create the candidate new holon. `E.24.UK` is the pattern for public-kind admission; A.1 is the pattern for world-side recognition; C.2.1 is the pattern for the optional classification assertion; its warrant requires exact evidence and assurance relations. Publication of the record is another relation under the publication patterns.

#### B.2:4.4 - Candidate New Whole Reference And Kind

Use one `resultHolonRef : U.HolonRef` for the candidate new whole and one `resultHolonKindRef : U.KindRef` for its kind. `E.24.UK` must already have admitted that public kind, and the candidate new whole must satisfy the A.1 constructive criterion plus any kind-specific membership condition. Neither the references nor the record establish those facts.

When a person or system performing downstream work must inspect or cite the classification judgment, add the optional `resultHolonClassificationAssertionRef`. That C.2.1 assertion may report a governed evaluation of `true`, `false`, or `unknown`; its evidence, warrant, and G.11 currentness stay separate from world-side criterion satisfaction. B.2 still asks a different question: whether the existing whole can continue to carry the subject claim or a new whole must be identified.

Do not use `post*` field names as live governed names. They hide the candidate new whole and its kind and invite temporal shorthand. Name that whole and its admitted public kind; cite a classification assertion only when the receiving use needs that episteme.

#### B.2:4.5 - Agency Threshold

Agency is not a binary status and not a root kind. Treat agency as a characteristic-space threshold for one exact system, predicate, claim scope, and qualification window.

Use `A.13`, `A.19`, and `C.16` for the characteristic-space and threshold claim. Levin-line TAME work can discipline the multi-characteristic framing when agency evidence is relied on for the current claim. B.2 uses agency threshold only as one possible trigger in `MHTTriggerProfile`, and only when crossing the threshold changes closure, supervision, objective, or whole identity.

Recover the admitted System and its agency-relevant characteristic or threshold independently. A System may bear that characteristic while participating passively in the situation. Recover a local system-role kind, a separate System-classification judgment, an obtaining assignment, and ordinary source wording as separate branches; include one only when the receiving claim depends on it. If claim-bearing source wording still says only “role,” use `E.10.ROLE` rather than presuming classification or assignment.

#### B.2:4.6 - Acting-System Participation

When a source describes a system changing another holon, recover acting-system participation and transformation separately.

Use `A.12` for acting-side externalization, `A.3.4` for bounded transformation, and `A.15.1` for work occurrence. A system changing another holon does not thereby become its part or the larger whole containing it, and no `U.Transformer` kind is created.

#### B.2:4.7 - Mathematical-Lens Separation

Graph, algebra, RG-like, MSPD, benchmark, scaling, and morphism language can bear on MHT recognition only as mathematical or analytical expression.

Use `C.29` when the mathematical lens is relied on for the current claim. Use B.2 only after the holon identity claim is recovered and the ordinary existing-whole comparison leaves a whole-reidentification question.

#### B.2:4.8 - Keep Whole Identity, Evidence, Currentness, And Reliance Separate

Keep five results apart:

- the existing whole and candidate new whole, their constituents, obtaining constructive relations, assemblies, characteristics, and identity rules are world-side objects and facts under their direct patterns;
- a B.2 whole-reidentification assertion is a C.2.1 episteme about those objects;
- evidence and assurance relations support or warrant the assertion's claim content but create neither whole and decide neither identity rule;
- use G.11 to determine whether the selected assertion or record edition is current for the receiving use;
- a person or system performing the receiving work decides whether to rely, decline to rely, defer, or reopen.

Evidence present or missing, and a current or stale record, can change what an evaluation returns and whether a person or system relies while performing receiving work. They cannot turn the same whole into a new whole or a new whole into the same one. Whether the existing whole continues or a new whole must be identified follows the direct identity and reidentification rules plus the actual construction facts. A.1 recognition of either candidate supplies no B.2 warrant and does not select B.2.

### B.2:5 - Archetypal Grounding (Worked Cases)

#### B.2:5.1 - Closed-Loop Regulated System

Parts: plant, sensor, controller, actuator.

Existing-whole repair may be enough if only a sensor improved or a controller parameter changed. B.2 becomes current only when exact constructive relations and a governed assembly close the feedback and supervision around an objective, yielding one exact new whole proposed for recognition under the already admitted `U.System` kind, whose boundary, external commitments, and capability envelope are no longer explainable as changes of the existing whole. That proposed whole can satisfy A.1 only if its actual boundary, interfaces, relevant characteristics, and identity-preservation conditions also satisfy at least one applicable governed larger-assembly construction method or rule—for example, a rule under which the regulated system can remain one constituent of a larger plant or production system. If that compatibility condition does not hold, the proposed whole fails A.1; if the needed evidence or dependency is unavailable, evaluation remains `unknown`. Loop closure, a record, or a measurement supplies none of those facts.

```text
MHTTriggerProfile@Control : U.Episteme
  entityOfConcernRef: plant-plus-devices configuration
  content:
    changedSupervisionRelationRefs: closed feedback relation
    changedObjectiveClaimRef: maintain output y near reference r
    changedCapabilityClaimRef: capability envelope after closure

HolonReidentificationRecord@Control : U.Episteme
  entityOfConcernRef: regulated control system
  content:
    existingWholeRef: plant-plus-devices configuration
    selectedTriggerProfileRef: MHTTriggerProfile@Control
    existingWholeExplanationResultRef: ClosedLoopExistingWholeResult
    resultHolonRef: regulated control system
    resultHolonKindRef: U.System
    resultHolonClassificationAssertionRef: RegulatedControlSystemClassificationAssertion
    wholeReidentificationClaimRef: ClosedLoopWholeReidentificationClaim
    changedClaimPatternLocators: A.1, B.1.2, B.2.2, C.30.LCA, A.2.2
```

The exact EntityOfConcern is an actual participant in the C.2.1 `EpistemeConstitutionRelation`; `EntityOfConcernSlot` is only the corresponding declaration-local participant meaning inside `EpistemeConstitutionRelationSignature`. The `entityOfConcernRef` field and indented content fields carry participant or claim designations in each episteme; they are not SlotKinds or participants of a new MHT relation. The feedback and capability relations retain their direct identities, while the optional classification assertion retains its own C.2.1 identity and does not establish world-side holonhood.

#### B.2:5.2 - Compendium Becomes Theory

A collection of results can remain a catalogue. B.2 becomes current only when the knowledge body is reidentified as an episteme whole with its own claim-bearing structure, explanatory objective, reference scheme, and evidence relations.

`B.2.3` specializes this case when the exact candidate new holon named by the MHT claim is recognized under the already admitted `U.Episteme` kind. C.2.1 defines episteme constitution and identity; E.17 and E.24.PUB define publication occurrences, forms, and carriers; C.2.P recovers source-expression and source-to-use distinctions; A.10 and G.6 supply evidence-provenance relations when the receiving use relies on them.

#### B.2:5.3 - Capability Envelope Appears

Several systems, methods, and work occurrences align and a new capability envelope appears. Apply the direct capability, characteristic, function, transformation, method, work, evidence, and architecture patterns first.

Use `B.2.4` only when separately governed capability or functioning facts make a whole-reidentification question live under B.2. Evidence can support the claim about those facts; it creates neither the facts nor the question.

#### B.2:5.4 - Lathe And Workpiece

A lathe transforms a workpiece. That is transformation and work, not MHT and not parthood. B.2 becomes current only if the manufacturing arrangement creates or reveals a new whole that must be reidentified, such as a production cell with exact constituents, obtaining coordination and supervision relations, a governed assembly, an objective, a whole-level capability, and a reidentification rule that the earlier arrangement lacks. A.1 recognition additionally requires the cell's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions to fit at least one applicable governed construction method or rule under which the cell can remain a constituent of a larger production system.

#### B.2:5.5 - Same Whole, New Whole, And Lost Evidence

Replacing Pump #37's seal is an ordinary constituent change when the pump's reidentification rule admits that maintenance phase. The same pump remains the EntityOfConcern; use the direct maintenance, part-relation, work, transformation, and characteristic patterns and stop B.2.

Closing a controller-sensor-actuator loop can yield a new regulated-system whole only when the exact candidate assembly, supervision and coordination relations, boundary, objective, whole-level capability, admitted `U.System` kind, and reidentification rule satisfy A.1 and the system criterion. Its actual boundary, interfaces, relevant characteristics, and identity-preservation conditions must also satisfy at least one applicable governed larger-assembly construction method or rule under which the regulated system can remain a constituent. If that condition fails, the candidate fails A.1; if the needed evidence or dependency is unavailable, evaluation returns `unknown`. A wiring diagram, commissioning record, loop closure, or capability measurement alone supplies none of those construction or compatibility facts.

If the support for the reidentification assertion is present and its edition is current, a person or system performing receiving work may rely on it. If the same evidence is unavailable, evaluation can return `unknown`; use G.11 to test whether the edition is current for this use; and the actor may decline, defer, or reopen. None of those branches changes whether the regulated-system whole actually exists or whether the prior configuration remains the same whole.

#### B.2:5.6 - Selected Structure And Transformation Stops

A selected `BoundedModelUseStructure` organizes exact model-use relations. It is not the new holon named by an MHT claim and gains no parts, agency, or whole identity from selection, naming, or a Context Map.

Several actual changes during assembly may each be exact `U.Transformation` occurrences. B.2 does not treat them as constituents of one composite transformation. If whole reidentification would require positive transformation composition, transformation parthood, or composite-transformation identity and no direct governor supplies contribution, compatibility, boundary, interfaces, and reidentification, retain the exact blocker and the independently identified changes. The missing composition facts do not show that any change is atomic.

### B.2:6 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Emergence rhetoric | A gain, surprise, or synergy label declares a new whole. | Perform the ordinary existing-whole comparison before B.2. |
| Record as ontology | Trigger profiles, result fields, or checklist labels become U-kinds. | Keep the trigger profile, optional explanation result, and reidentification record as `U.Episteme` values; keep the ordinary comparison as an action. Let `E.24.UK` handle public-kind admission and A.1 recognize the candidate new whole. |
| Math as MHT | Graph, RG-like, MSPD, benchmark, scaling, or morphism expression declares whole reidentification. | Use `C.29`; recover holon identity and existing-whole explanation first. |
| Binary agency | Agency threshold crossing is treated as a root kind or binary status. | Use the direct characteristic-space and threshold patterns; use B.2 only when whole identity changes. |
| Transformation as containment | A system changes another holon and is treated as its part or containing whole without a separately obtaining part-whole relation. | Use A.12, A.3.4, A.15.1, and the direct crossing relation pattern; apply B.2 only when separately grounded facts make whole reidentification current. |

### B.2:7 - Conformance Checklist

| Check | Conformance condition |
| --- | --- |
| `CC-B2-1` | A B.2 use names the exact existing whole already recognized under an admitted holon kind, its identity rule, current part relations, and kind-specific pattern before declaring whole reidentification. |
| `CC-B2-2` | `MHTTriggerProfile` is a `U.Episteme` with the existing whole as EntityOfConcern, exact typed content references, and no mandatory bounded-context reference. |
| `CC-B2-3` | The ordinary existing-whole comparison precedes MHT. An optional `ExistingWholeExplanationResult` episteme is created only when a receiving use must inspect or cite its exact explanations, evidence, and sufficiency verdict. |
| `CC-B2-4` | `HolonReidentificationRecord` is a `U.Episteme` with one `resultHolonRef` for the candidate new whole, one reference to its admitted public kind, the whole-reidentification claim, direct evidence and subject-pattern references, and only an optional C.2.1 classification-assertion reference when a person or system performing later work needs to inspect or cite that judgment. |
| `CC-B2-5` | Agency-threshold claims use the direct characteristic-space and threshold patterns; B.2 uses them only when whole identity changes. The admitted System and characteristic are recovered independently of any optional local system-role classification or assignment, including when the System participates passively. |
| `CC-B2-6` | Acting-system participation and transformation use A.12 and A.3.4; B.2 does not create `U.Transformer`. |
| `CC-B2-7` | Mathematical expressions can bear on but do not replace the holon reidentification claim. |
| `CC-B2-8` | The candidate new whole reference and its kind reference remain separate; B.2 does not maintain one optional field per admitted holon species. |
| `CC-B2-9` | A candidate new episteme, system, method, work occurrence, or discipline uses A.1 recognition plus its kind-specific pattern; a dependent `U.Structure` is not the new holon named by an MHT claim. |
| `CC-B2-10` | Whether the existing whole continues or a new whole must be identified follows exact construction and reidentification facts; evidence availability, evaluation value, record currentness, and receiving reliance remain separate results. |
| `CC-B2-11` | B.2 does not infer transformation composition, transformation parthood, composite identity, holonhood, or atomism from several changes, one work episode, one selected structure, or missing part facts. |


### B.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Emergence by adjective | A capability or property is called emergent without reidentifying the whole. | Use `B.2.P` to recover claim kind, then B.2 only if whole reidentification is current. |
| Record as ontology | Trigger profile, result field, or record name is treated as a world-side kind. | Keep the trigger profile, optional explanation result, and reidentification record as `U.Episteme` values; keep the ordinary comparison as an action. Let `E.24.UK` handle the candidate new whole's public kind and A.1 recognize that candidate. |
| Content field as relation slot | A reference field inside a profile or record is treated as a participant SlotKind or as evidence that the referenced relation obtains. | Keep the field in episteme content, resolve its reference to the direct occurrence, and use that occurrence's subject pattern for obtaining and identity. |
| KPI jump as MHT | A metric improves and MHT is declared. | Perform the ordinary existing-whole comparison; use the direct measurement, characteristic, Method, Work, or architecture pattern when it explains the change. |
| Agency shortcut | Agency threshold crossing creates a new root kind. | Use the direct characteristic-space and threshold patterns; apply B.2 only when closure, supervision, objective, or identity changes. |
| Math result as MHT | Graph, RG-like, MSPD, or benchmark expression declares new whole. | Use `C.29`; recover holon identity before B.2. |
| Transformation as containment | A system changes another holon and is treated as its part or containing whole without a separately obtaining part-whole relation. | Use A.12, A.3.4, A.15.1, and the direct crossing relation pattern; use parthood only when an exact grounded part relation independently obtains. |

### B.2:9 - Consequences

Positive consequences:

- MHT becomes a precise whole-reidentification move rather than a synonym for improvement.
- Cases involving a candidate new system, episteme, method, work occurrence, or discipline use the same B.2 whole-reidentification solution while retaining their subject patterns.
- Trigger language remains useful without becoming ontology.
- Mathematical and benchmark evidence can be used without replacing the holon claim.

Costs:

- Users must try existing-whole explanations before declaring MHT.
- MHT records require a reference to the exact candidate new whole, a reference to its already admitted public kind, A.1 recognition, and the evidence needed by any classification assertion used downstream.
- Some attractive emergence claims will return to ordinary characteristic, method, work, architecture, or measurement repair.

### B.2:10 - Rationale

Holonic work needs a way to recognize when a whole has changed enough that the old EntityOfConcern no longer carries the current claim. B.2 provides that move without collapsing all novelty into "emergence" and without inventing record-field U-kinds.

The pattern is intentionally conservative: it applies repairs from subject patterns first, then supports whole reidentification only when the existing whole no longer explains the observed shift. This protects B.1 part-whole construction, A.15 work, A.3.4 transformation, C.16 characteristics, C.29 math-lens use, and episteme and publication discipline from being swallowed by MHT.

### B.2:11 - Decision-bearing SoTA account

| Practical question | Exact primary source | Adopt, adapt, or reject in B.2 | Exact effect in this pattern |
| --- | --- | --- | --- |
| When may a configured production arrangement be treated as a distinct operating whole? | Bartels et al., [*Dependable Cyber-Physical Matrix Production Systems Utilizing Holonic Multi-agent Systems*](https://www.dfki.de/en/web/research/projects-and-publications/publication/16121) (2025), and Macherki et al., [*QHAR: Q-Holonic-Based Architecture for Self-Configuration of Cyber-Physical Production Systems*](https://www.mdpi.com/2076-3417/11/19/9013) (2021), with a tested reconfiguration case. | **Adopt** the practical need to recover exact entities, flows, coordination, dynamic interdependence, control organization, and reconfiguration purpose. **Reject** a named holonic architecture, control layer, or reconfiguration event as sufficient whole identity. | Sections 4 and 5.1 require actual constituents, obtaining constructive relations, boundary, objective, whole-level characteristic, reidentification rule, and larger-assembly compatibility before A.1 recognition. |
| What separates inputs, construction, and the resulting whole? | Florio and Linnebo, [*Introduction to Constructional Ontology*](https://philarchive.org/rec/FLOITC-3) (2024), and Borgo and Righetti, [*Towards Applied Constructional Ontology*](https://doi.org/10.3233/FAIA250480) (2025). | **Adopt** the separation among accepted inputs, constitutive organization, and resulting identity. **Adapt** it to FPF's direct part relations, assembly, reidentification rule, and admitted holon kinds. **Reject** a trigger profile, record, tuple, or Method label as the constructor that makes the whole exist. | Sections 1, 4, 4.3, and 5 distinguish world-side construction from comparison and record epistemes. |
| How should agency bear on whole reidentification? | Michael Levin, [*Technological Approach to Mind Everywhere*](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2022.768201/full) (2022). | **Adopt** non-binary, multi-characteristic, empirically tested agency and multi-scale competency as possible evidence about a system. **Reject** an agency label or threshold as a root kind or automatic new-whole result. | Section 4.5 keeps agency as one possible trigger whose direct characteristics must affect closure, objective, supervision, or identity. |
| What can a multiscale mathematical signal contribute? | Akhtyrchenko, Katsnelson, and Ustyuzhanin, [*Directing Open-Ended Evolution in Artificial Life via Multi-Scale Path Divergence*](https://arxiv.org/abs/2606.17091) (v2, 3 August 2026), defines MSPD over realized trajectories as a multiscale analytical and optimization measure. | **Adopt** MSPD as a possible exact analytical input when its trajectory assumptions match the case. **Reject** a high MSPD, RG-like score, graph pattern, or benchmark jump as whole reidentification. | Sections 0, 4.7, and 8 route the mathematical result through C.29 and still require the B.2 identity comparison. |

These sources answer different questions. None supplies a universal emergence detector. Popular modeling languages and generic architecture standards are not used as decision authority here because they do not decide when the same whole ends and another begins.

### B.2:12 - Relations
- **Builds on:** `A.1` for world-side holon recognition, `B.1` for part-whole construction, `A.14` and `C.13` for relation and constructional grounding, and `E.24.UK` for one-time public-kind admission.
- **Coordinates with:** `A.12` and `A.3.4` for acting-side and transformation, `A.15` and `A.15.1` for method and work, `C.16` and `A.19` for characteristic space and threshold, `C.2.1` for optional claim and record epistemes, `A.10` and `B.3` for evidence and warrant, `G.11` for edition currentness, `C.29` for mathematical lenses, and `C.32.P2S` when architecturing pressure becomes whole reidentification rather than local structure repair.
- **Specialized by:** `B.2.2` when the candidate new whole is a system, `B.2.3` when it is recognized under the admitted `U.Episteme` kind, and `B.2.4` when capability or functioning facts require whole reidentification.
- **Can use neighboring evidence from:** `B.2.5` when a supervisor-subholon feedback relation is part of the B.2 case evidence or neighboring structure; that does not make B.2.5 a specialization for the candidate new holon's kind.
- **Uses:** `B.2.P` when emergence-family, MHT, MET, MFT, synergy, or metric-mirage wording hides which claim kind is current before B.2 is applied.

### B.2:End

