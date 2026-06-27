## B.2.3 - Meta-Holon Transition With Episteme Result

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.2.3:0 - Use This When

Use this pattern when a Meta-Holon Transition result is admitted as `U.Episteme`: a theory, model family, standard, doctrine, specification body, research programme, field-level knowledge body, or other claim-bearing non-agentive holon.

Use `B.2` first to decide whether whole reidentification is current. Use `B.2.3` only when the result-kind question points to `mhtResultEpistemeRef`.

**First useful move.** Recover the episteme result as a `U.Episteme` holon with its C.2.1 slot relation: EntityOfConcern, grounding holon, claim graph, reference scheme, viewpoint, view, and publication or source-use relations when current.

**What goes wrong if missed.** A catalogue, literature review, dashboard, model repository, or vocabulary is called a new theory without claim-graph reidentification; or a real new episteme whole is treated as a pile of publications.

**What this buys.** The pattern preserves B.2 whole reidentification while keeping episteme ontology with C.2.1 and the episteme family. It prevents episteme-result MHT from becoming episteme agency, publication authority, generic emergence, or a second episteme ontology.

**Not this pattern when.**

- If the result whole is an acting physical or operational holon, use `B.2.2`.
- If the question is episteme slot relation, publication, source use, view, viewpoint, claim graph, reference scheme, or description use without MHT, use `C.2.1`, `C.2.P`, `C.2.P.DR`, `E.17`, and the episteme family directly.
- If the question is effect-free episteme morphing, viewing, retargeting, or controlled semantic coarsening, use `A.6.2`, `A.6.3`, `A.6.4`, or `A.6.3.CSC`.
- If the question is synthesis work, use `A.15.1` for performed work and `A.12` or `A.3.4` for acting-side and transformation claims.
- If the wording is ambiguous emergence-family language, use `B.2.P` before selecting B.2.3.

### B.2.3:1 - Problem Frame

A library is not a theory, and a theory is not its publication.

A group of papers, models, datasets, design notes, forecasts, standards, or local doctrines may remain a collection. It becomes an MHT-result episteme only when the current claim needs one reidentified claim-bearing holon whose C.2.1 slot relation can be filled and governed as one episteme.

B.2.3 does not introduce a special episteme ontology. It uses `mhtResultEpistemeRef` in the B.2 record and then returns episteme structure to C.2.1.

### B.2.3:2 - Problem

Without this specialization:

1. **Catalogues become theories.** Aggregated publications or dashboards are treated as a new episteme because they are stored together.
2. **Theory becomes publication.** The paper, report, standard document, model card, or dashboard is used as the episteme itself.
3. **Episteme receives agency.** The theory, standard, or doctrine is described as if it performs work or enforces behavior by itself.
4. **Morphing becomes MHT.** A view, retargeting, coarsening, translation, or model transformation is treated as a new episteme whole.
5. **Assurance is inherited silently.** Trust in constituent sources is treated as trust in the reidentified episteme whole.
6. **Generic emergence replaces claim structure.** "Emergent theory" hides the actual claim graph, reference scheme, and grounding relation.

### B.2.3:3 - Forces

| Force | Tension |
| --- | --- |
| Synthesis vs aggregation | A new episteme whole can integrate claims, but many collections remain indexes, reviews, or portfolios. |
| Episteme identity vs publication form | The episteme may be published in many forms; no publication form is the episteme by appearance. |
| Claim organization vs agency | An episteme can organize claims and guide use, but systems perform work with or on it. |
| Constituent evidence vs result assurance | Evidence for parts may bear on the result, but the result episteme needs its own claim and assurance relations. |
| Source mnemonic vs current ontology | Short labels can aid recognition while hiding whether the current object is B.2, C.2.1, A.6, E.17, or source-use. |

### B.2.3:4 - Solution

Use B.2.3 as the episteme-result specialization of B.2.

#### B.2.3:4.1 - Episteme-Result MHT Slice

When `mhtResultEpistemeRef` is selected, use:

```text
EpistemeResultMHTSlice@Context:
  existingWholeRef: U.Holon
  mhtResultEpistemeRef: U.Episteme
  boundedContextRef:
  selectedTriggerProfileRef: MHTTriggerProfile@Context
  existingWholeExplanationCheckRef: ExistingWholeExplanationCheck@Context
  epistemeKindAdmissionRef: C.2.1
  epistemeSlotRelationRef: U.EpistemeSlotRelation
  entityOfConcernSlotRef:
  groundingHolonSlotRef:
  claimGraphSlotRef:
  referenceSchemeSlotRef:
  viewpointSlotRef?
  viewSlotRef?
  publicationOrSourceUseRefs?
  constituentEpistemeRefs:
  synthesisWorkRefs?
  evidenceOrAssuranceRefs:
  mathematicalLensUseRefs?
  blockedOverreads:
```

This slice is not a U-kind and not a second episteme ontology. It is the B.2 record slice that says the MHT result is an episteme and names the C.2.1 relation that governs it.

#### B.2.3:4.2 - Episteme Slot Re-Basing

For the result episteme, re-base at least these C.2.1 slots when current:

- `EntityOfConcernSlot`: what the result episteme is about;
- `GroundingHolonSlot`: where the result claim is grounded or tested;
- `ClaimGraphSlot`: what the result episteme says as a claim structure;
- `ReferenceSchemeSlot`: how claims are read as about their entities;
- `ViewpointSlot` and `ViewSlot`: when the result episteme has viewpoint-governed views;
- publication, source-use, and representation relations when the result episteme is published, cited, carried, or represented.

Do not infer these slots from the existence of a publication set. Fill them as episteme slots.

#### B.2.3:4.3 - Episteme Trigger Interpretation

Interpret `MHTTriggerProfile@Context` for epistemes without giving agency to epistemes:

| Trigger family in `MHTTriggerProfile@Context` | Episteme-result reading | Direct owner kept visible |
| --- | --- | --- |
| Delimitation change | The knowledge body now has a stable EntityOfConcern, scope, reference scheme, and claim scope. | `C.2.1`, `A.7`, source-use owners |
| Objective or evaluation change | The result episteme answers or evaluates a question that the collection did not answer as one claim-bearing whole. | `C.2.1`, `C.16`, `E.21` or relevant evaluation owner |
| Supervision or coordination change | Principles, axioms, invariants, reference schemes, or claim-graph constraints organize how constituent claims are interpreted. | `C.2.1`, `A.6.0`, `A.6.1`, `C.29` when formal lens is current |
| Capability or closure evidence | The result episteme enables a new explanatory, predictive, specification, or coordination use. | `C.2.1`, `C.16`, `A.10`, use-specific owner |
| Agency threshold | Usually not applicable to the episteme itself; if agency is claimed, recover the acting system in role. | `A.12`, `A.2.1`, `A.13`, `A.19`, `C.16` |
| Temporal consolidation | A field, standard, or theory becomes one current knowledge body after phase consolidation or source-currentness change. | `C.27`, `E.17`, source-use owners |
| Context reframe | New terms, reference schemes, or EntityOfConcern mapping reframe the knowledge body. | `C.2.1`, `A.6.3`, `A.6.4`, `F.18` |

B.2.3 uses these rows as evidence to inspect. B.2 decides whether whole reidentification is admitted.

#### B.2.3:4.4 - Blocked Readings

Do not use B.2.3 as:

- a name for generic emergence;
- an authority claim for a publication;
- an agentive claim about a theory, standard, or doctrine;
- an effect-free episteme morphism, view, retargeting, or coarsening;
- a second episteme ontic beside C.2.1;
- a shortcut from source synthesis to high trust;
- a replacement for source-use, evidence, assurance, or publication patterns.

### B.2.3:5 - Archetypal Grounding (Worked Cases)

#### B.2.3:5.1 - Reliability Doctrine

Before MHT, teams have local runbooks, incident reports, dashboards, and reliability definitions. They may be useful, but they are not yet one episteme.

After MHT, the result may be a reliability doctrine if it has one EntityOfConcern, one reference scheme for service harm and reliability claims, a claim graph with principles and definitions, grounding relations to operating services, publication relations, and source-use relations for its standards and training materials.

```text
EpistemeResultMHTSlice@Reliability:
  mhtResultEpistemeRef: reliability doctrine
  epistemeSlotRelationRef: U.EpistemeSlotRelation
  entityOfConcernSlotRef: user-visible service harm and reliability
  groundingHolonSlotRef: operating service systems
  claimGraphSlotRef: doctrine claims and invariants
  referenceSchemeSlotRef: shared reliability vocabulary
  publicationOrSourceUseRefs: handbook and standard publication forms
```

The doctrine does not enforce anything by itself. Systems in role use it, cite it, train with it, and work according to it.

#### B.2.3:5.2 - Model Family Becomes Theory

A model family can remain a toolbox. It becomes an episteme-result MHT only if the result has a unified claim graph, reference scheme, grounding holons, and admissible explanatory or predictive use that the collection did not carry as one whole.

If the change is only a new model publication or benchmark score, use publication, source-use, measurement, evidence, and mathematical-lens owners instead.

#### B.2.3:5.3 - Standard Body

A set of clauses, examples, and annexes can become a standard episteme when the result is one claim-bearing whole with terms, references, scope, conformance claims, and publication forms.

The standard is not the committee, not the PDF, and not the work of enforcement. The committee is an acting system or role-bearing system; the PDF is a publication form; enforcement is work by systems in role.

### B.2.3:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Library as theory | A repository, dashboard, or reading list is treated as one claim-bearing episteme. | Fill C.2.1 slots and use B.2.3 only when whole reidentification remains current. |
| Publication as episteme | A PDF, report, standard document, model card, or dashboard is treated as the episteme itself. | Keep publication forms with E.17 and source-use owners. |
| Episteme agency | A theory, standard, or doctrine is described as performing work or enforcement. | Recover acting systems, role assignments, methods, work, and evidence separately. |
| Morphing as MHT | View, translation, coarsening, or retargeting is called a new episteme whole. | Use A.6 episteme-morphism owners unless B.2 whole reidentification remains current. |
| Source trust transfer | Trust in constituent sources becomes assurance for the result episteme. | Rebuild assurance and source-use relations for the result episteme. |

### B.2.3:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B2.3-1` | B.2 has left a whole-reidentification question before B.2.3 is used. |
| `CC-B2.3-2` | The result kind is admitted as `U.Episteme` and recorded as `mhtResultEpistemeRef`. |
| `CC-B2.3-3` | `EpistemeResultMHTSlice@Context` names `U.EpistemeSlotRelation` and does not create a second episteme ontic. |
| `CC-B2.3-4` | Publication, source-use, view, viewpoint, claim-bearing, and representation questions return to C.2.1, E.17, C.2.P, C.2.P.DR, and direct episteme-family owners. |
| `CC-B2.3-5` | The episteme is non-agentive; acting systems, synthesis work, and enforcement work use A.12, A.2, A.15, A.15.1, or work owners. |
| `CC-B2.3-6` | Assurance for the result episteme is not silently inherited from constituent epistemes or publications. |
| `CC-B2.3-7` | Effect-free morphing, viewing, retargeting, and controlled coarsening are not treated as B.2.3 unless whole reidentification is current. |

### B.2.3:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Library as theory | A repository or reading list is treated as one episteme. | Fill C.2.1 slots; use B.2.3 only if one result episteme whole is recovered. |
| PDF as episteme | A publication form is used as the theory itself. | Use E.17 and publication owners; keep `mhtResultEpistemeRef` for the episteme. |
| Doctrine receives agency | "The standard enforces..." or "the theory decides..." | Recover the acting system, role, method, work, evidence, or decision claim. |
| Morphism as MHT | A view, translation, coarsening, or retargeting is called a new episteme whole. | Use A.6.2, A.6.3, A.6.4, or A.6.3.CSC unless B.2 whole reidentification is current. |
| Synthesis as high trust | A new theory inherits trust because its sources were reliable. | Rebuild assurance for the result episteme through A.10, B.3, B.3.5, C.2.1, and source-use owners. |

### B.2.3:8 - Consequences

Positive consequences:

- Episteme-result MHT becomes usable without preserving title mnemonics as ontology.
- C.2.1 remains the episteme ontic owner.
- Publications, source use, synthesis work, evidence, assurance, and acting systems remain separate.

Costs:

- A claimed synthesis must fill episteme slots, not only cite a portfolio.
- Result-episteme assurance requires fresh relation work.
- Some "new theory" claims return to publication, source-use, morphism, benchmark, or evidence owners.

### B.2.3:9 - Rationale

Knowledge synthesis can create a new holon, but only when the result is a reidentified claim-bearing episteme. B.2.3 keeps that useful case and removes the drift toward episteme agency, publication authority, generic emergence, and duplicate episteme ontology.

This pattern is deliberately thin. B.2 owns whole reidentification; C.2.1 owns episteme slot relation; E.17 and source-use patterns own publications; A.6 episteme-morphism patterns own morphing and retargeting; A.15 and A.12 own synthesis work and acting systems.

### B.2.3:10 - SoTA-Echoing

| Source family | Lesson for B.2.3 | FPF decision |
| --- | --- | --- |
| Evidence synthesis and living-review practice | Synthesis claims need explicit scope, evidence relation, currentness, and maintenance rather than narrative authority. | B.2.3 requires result-episteme slots, assurance relations, and source-use relations. |
| Knowledge-graph and claim-network practice | A knowledge body can be represented as related claims, evidence, and sources. | `ClaimGraphSlot` remains C.2.1 material; graph representation does not declare MHT by itself. |
| Science-of-science and paradigm-change studies | Fields and theories can consolidate into named bodies with new scope and organizing principles. | B.2.3 treats consolidation as possible evidence for episteme-result MHT, not as automatic admission. |
| Publication and standards practice | Standards, reports, models, and dashboards are carriers and publication forms. | E.17 and source-use owners remain separate from the episteme whole. |

### B.2.3:11 - Relations

- **Specializes:** `B.2` for MHT-result holons admitted as `U.Episteme`.
- **Builds on:** `C.2.1` for `U.EpistemeSlotRelation`, `A.1` for holon admission, and `E.24.UK` for result-kind admission discipline.
- **Coordinates with:** `C.2.P`, `C.2.P.DR`, `E.17`, `E.17.*`, `A.6.2`, `A.6.3`, `A.6.4`, `A.6.3.CSC`, `A.10`, `B.3`, `B.3.5`, `C.29`, `F.18`, and `F.19`.
- **Uses:** `B.2.P` when source wording such as emergence-family or title-mnemonic wording hides the claim kind.
- **Contrasts with:** `B.2.2` for system-result MHT and `B.2.4` for capability and functioning whole-reidentification evidence.

### B.2.3:End

