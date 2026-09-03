## E.10.D1 - Recovering What “Context” Means in Use

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative when *context* carries meaning needed by an FPF claim; informative for quoted source wording and ordinary prose that already makes its meaning clear.

### E.10.D1:1 - Problem frame

Use this pattern when the word *context* can change a statement or the next practical move, but the statement does not yet say what supplies the relevant boundary, interpretation, or situation.

**What goes wrong if missed.** A reader treats a source edition, reference scheme, local sense, claim scope, model-use boundary, working situation, architecture, environment, or domain boundary as one generic Context object. The sentence then hides the distinction that should decide what to inspect, compare, change, or stop doing.

**First useful result.** One repaired statement names the value, relation, claim, scope, situation, or use that supplies the missing meaning and, when useful, cites the pattern that defines, constrains, tests, or supplies a method for it. The reader can then take the next subject-matter action or stop.

**Not this pattern when.** Keep *context* when it is a quoted source term, an ordinary word whose meaning is already clear, or an established Plain designation whose value, relation, scope, situation, or use is already named under the pattern that defines or tests it. Use that pattern directly; `E.10.D1` does not require a second wording pass.

### E.10.D1:2 - Problem

The word *context* is useful because it points toward locality, but it does not say which locality matters. Terminology work uses source schemes and local senses. Domain-driven design uses a model boundary and relations among model uses. Claims use scopes and qualification windows. Architecture work distinguishes a described holon, actual subject relations, a selected structure, an obtaining `ArchitectureRelation`, and an `ArchitectureClaim`; viewpoint, environment, and operating-condition claims introduce further distinctions. A pattern's Problem frame describes a recognizable situation. A DPF has a domain subject, audience, source basis, and local qualification conditions.

Treating these uses as one `Context` participant, `ContextId`, or two-part `SenseCell(Context, LocalSense)` hides the distinctions supplied by `A.1.1`, `A.2.6`, `C.2.1`, `F.0.1`, `F.17`, and `F.9`. Replacing that proxy with another universal container preserves the failure under a new name.

### E.10.D1:3 - Forces

| Force | Tension |
| --- | --- |
| Short wording and recoverable meaning | *Context* is concise, but the reader still needs to know which boundary changes the action. |
| Shared recovery and subject-specific rules | One recurring wording problem deserves one method, while the subject patterns still define or test each recovered value or relation. |
| Cheap repair and complete repair | Most sentences need one small rewrite; a recurring cross-framework problem may require `E.10.ARCH`. |
| Source fidelity and FPF precision | A source may use *context* as a technical term, while an FPF claim must state the source-local value and its receiving use without importing the source ontology wholesale. |
| Familiar shorthand and subject precision | Readers recognize *context*. Subject patterns define or test the available values and relations; the practitioner selects the one used by the statement. |

### E.10.D1:4 - Solution

Start with the sentence and the practical use that makes it matter.

1. Mark the phrase containing *context* and state what a reader would do differently under another interpretation.
2. Select the smallest branch in `E.10.D1:4.1` that answers that difference.
3. Apply the named subject pattern and recover its value, relation, claim, or situation. For source-local meaning, reuse an adequate current `F.0.1` result or apply `F.0.1` only when that meaning remains unclear. Do not create a generic Context participant as an intermediate step.
4. Rewrite the sentence with the recovered content and state the next action or stop.
5. If the same defect recurs across framework contributions, use the shared method in `E.10.ARCH`; keep this pattern as the word-specific branch and keep the recovered content in its subject pattern or DPF.

The bounded result is the repaired statement. No additional record is part of this result; create one only when a named later use needs its identity.

#### E.10.D1:4.1 - Positive recovery branches

| Wording use | Recover this content | Next move or stop |
| --- | --- | --- |
| Source-local meaning | An adequate current `F.0.1` result: the exact F.17 `SchemeSenseCell <ReferenceScheme, LocalExpression, LocalSenseClaim>` and its obtaining `LocalSenseBasisRelation` to the identified basis episteme. | Reuse that result. If the source-local meaning remains unclear, apply `F.0.1`, rewrite the sentence, and return to the subject question. Open `F.1` only when source selection is live, `F.9` only when the receiving claim needs a relation between different semantic-context projections, and `F.0.2` only when several source ontologies must be compared for the receiving claim. |
| DDD or model-use boundary | The direct A.1.1 `ModelApplicabilityRelation`, assigned-Work `ModelUseRelation`, or `ModelExpressionCoherenceRelation`. Select one `BoundedModelUseStructure` only when the organization of several such facts changes the engineering decision. | Stop at the direct relation when it answers the question. Select the wider structure only under A.1.1 and A.22. |
| Claim applicability or comparison boundary | The A.2.6 `U.ClaimScope`, its admitted `U.ContextSlice` values and membership facts, effective scheme, qualification window, comparison scheme, and any direct relation needed by the claim. | State those values and predicates under their subject patterns. Do not add a generic context participant. |
| Working situation, project use, or reader use | The named situation; intended reader; use; decision; non-use boundary; and the participants, Work, and claims whose change would alter that use or decision. `Problem frame` remains a readable pattern heading rather than a formal Context value. | Write the situation and use directly. Introduce a formal value only when a named later use needs its identity. |
| Design-time or run-time wording | The design artifact, plan, description, or model edition, or the performed Work, world-side occurrence, or state on which the sentence actually relies. | Keep design-time descriptions and plans separate from run-time holons, states, relations, and Work. Apply the pattern for the recovered object; the labels *design* and *run* create no shared Context or time-tag object. |
| Architecture relation or claim | The described holon, actual subject relations, selected `U.Structure`, and an obtaining `ArchitectureRelation` only when the C.30 predicate holds. Otherwise recover an `ArchitectureClaim` whose content says that the relation does not obtain, remains unresolved, or concerns a candidate or expected structure. | Apply `C.30`. State the actual relation and selected structure when they obtain. If the described holon, selected structure, architecture concern, or actual-versus-candidate distinction is still missing, stop with C.30's `concernCueOnly` or `problemCardReady` result. |
| Viewpoint or view | One identified candidate episteme, one identified `U.Viewpoint` edition with fixed rules, and the `EpistemeViewpointConformanceRelation` question between them. The same candidate episteme is a `U.View` relative to that viewpoint only when the relation obtains. | Apply `E.17.0` and return its readable positive, negative, or unresolved result. Stop there unless a named receiving use needs occurrence identity, warrant, new-viewpoint authoring, multi-view organization, or publication detail. |
| Environment, operating region, or operating condition | The subject claim and the actual holon, relation, state, spatial or temporal qualifier, constraint, or condition whose change affects that claim or the next action. An environmental label remains source wording until the practitioner uses the subject pattern's definitions or constraints to identify the content used by the statement. | Apply the pattern that defines or constrains the subject claim. If the statement still cannot name which environmental fact or operating condition changes the claim or action, return an unresolved wording result; do not infer an architecture or viewpoint claim. |
| DPF, domain, or local-practice boundary | The domain subject; intended audience and use; effective scheme; claim scope; qualification window; and source basis. | Keep domain or local meaning in its DPF or LPF. The word *domain* is neither restricted to a catalogue mark nor promoted to a U-kind by this pattern. |

#### E.10.D1:4.2 - Word use is a trigger, not a verdict

`E.10.D1` defines no `U.BoundedContext`, generic `Context`, universal `ContextId`, or two-part `SenseCell(Context, LocalSense)`. A source or subject pattern may define a value whose established designation contains *context*; keep that designation and its defined meaning. A DDD **bounded context** is the Plain retrieval name for the A.1.1 `BoundedModelUseStructure`, not a universal semantic-locality container.

Do not ban *anchor*, *domain*, *design*, *run*, or *context* by spelling. When a subject pattern defines the word's current use, preserve it. When the word hides the claim being made, recover that claim and rewrite the sentence. A source-local expression remains quotable even when its ontology differs from FPF.

An F.1 Source-Cut Card is a memory aid for one retained source edition and its answer-changing claims. It supplies neither local meaning nor source authority. A `SenseCellAddressRef` designates one identified F.17 cell; the address is not the cell and does not create a Context object.

#### E.10.D1:4.3 - Short working script

Use this sentence-sized script:

```text
This phrase uses “context” to mean [identified value, relation, scope, scheme, situation, or use].
[PatternID] [defines, constrains, tests, or supplies the method for] that content.
Therefore the reader [takes this action or stops].
```

The bracketed words are prompts, not a public schema. Delete them in the final prose.

### E.10.D1:5 - Archetypal Grounding

**Tell.** Recover the distinction that changes the action; do not model *context* itself.

**Show — source-local meaning.** A draft says, “In the maintenance context, *service* includes scheduled inspection.” The author finds an existing `F.0.1` result for the current `MaintenanceGuide-2026` edition: its exact F.17 cell says that *service* includes scheduled inspection, and its `LocalSenseBasisRelation` names the supporting claim episteme. That result is adequate for this sentence, so the author reuses it and writes, “In `MaintenanceGuide-2026`, *service* includes scheduled inspection,” with a citation to the cell. If the source-local meaning were still unclear, the author would apply `F.0.1` first. `F.1`, `F.9`, and `F.0.2` remain closed unless source selection, a cross-local relation, or comparison of several source ontologies becomes a live question.

**Show — model-use decision.** A change note says, “The controller change stays inside the press-control context.” If the decision asks only whether `PressControlModel-5` applies to `Press-3` within the stated claim scope, the engineer states that `ModelApplicabilityRelation` and stops. If release review depends jointly on model applicability, actual assigned-Work use, fixed-content coherence, applied constraints, and one selection-use frame, the engineer selects their A.1.1 `BoundedModelUseStructure`. The word *context* does not decide between those branches.

**Show — claim boundary.** A review says, “The comparison is valid in this context.” The repaired claim names the compared bearers, comparison scheme, `U.ClaimScope`, member slices, qualification window, evidence basis, and intended use. If those values already make the claim interpretable, no additional formal object is introduced.

**Ordinary non-use.** A source quotation says, “Context mapping is collaborative.” If the current claim is only that the source uses this phrase, keep the quotation and cite the source. Open A.1.1, F.9, or another branch only when the receiving text relies on a model-use structure, semantic relation, or other recovered content.

### E.10.D1:6 - Bias-Annotation

| Bias | Risk | Countermeasure |
| --- | --- | --- |
| Terminology bias | Every use of *context* is read as local sense. | Compare the applicable branches; select source-local meaning only when the effective scheme and sense claim change the statement. |
| DDD bias | Every boundary becomes a `BoundedModelUseStructure`. | Start with A.1.1's direct relations and select the structure only when their organization changes the decision. |
| Ontology bias | A small wording repair expands into a new kind or record. | Return one repaired sentence and stop unless another use needs durable identity. |
| Lexical policing | The spelling is banned even when a source or subject pattern defines it precisely. | Judge the wording use, preserve quotations and established designations, and repair only content needed by the FPF claim. |
| English-language bias | The English word *context* is mistaken for a universal semantic category. | Recover the source expression, language, edition, effective scheme, and local-sense claim before cross-language comparison. |

### E.10.D1:7 - Conformance Checklist

A use of `E.10.D1` conforms when:

1. the sentence and the action-changing ambiguity are named;
2. one recovery branch supplies the smallest sufficient content;
3. the repaired sentence names the relevant value, relation, scope, scheme, situation, or use and the contribution of any cited pattern;
4. source-local meaning reuses an adequate current `F.0.1` result or applies `F.0.1` when that result is absent or inadequate, then cites a basis relation only when it obtains;
5. an A.1.1 structure is selected only when the organization of its direct facts changes the decision;
6. a claim boundary uses A.2.6 scope and membership facts rather than a generic Context participant;
7. an F.9 Bridge is opened only between different semantic-context projections, and its bounded-use claim remains separate;
8. architecture wording distinguishes an actual selected structure and obtaining `ArchitectureRelation` from a negative, unresolved, candidate, or expected `ArchitectureClaim`;
9. viewpoint or view wording identifies the candidate episteme and viewpoint edition and uses the E.17.0 positive, negative, or unresolved conformance result;
10. environment, operating-region, or operating-condition wording returns to the subject claim and names the fact or condition that changes it, or returns an unresolved wording result;
11. quoted source wording and already precise ordinary wording remain available; and
12. the result gives the reader a practical next move or a truthful stop without creating a universal Context kind, field set, or card.

### E.10.D1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Universal Context proxy | One entity stands for source scheme, scope, situation, architecture, and model-use boundary. | Select the branch and name the direct value or relation. |
| Context field as participant | A `ContextId` or `...ContextRef` field silently becomes a relation participant or identity discriminator. | Resolve the field to the subject-pattern value; otherwise keep it as a designator and state the blocker. |
| Automatic bounded-context structure | The phrase *bounded context* selects A.1.1 even when one direct relation answers the decision. | Begin with applicability, actual use, or coherence and stop at the first sufficient result. |
| Context map as relation truth | A diagram or table is treated as an obtaining Bridge, `ArchitectureRelation`, or model-use crossing. | Recover the represented objects, correspondence, and direct relation under their subject patterns. Use an `ArchitectureClaim` when architecture remains negative, unresolved, candidate, or expected. |
| Blanket word ban | Every occurrence of *context* or *anchor* is deleted, including precise source terms and established designations. | Preserve the defined source or subject-pattern use; rewrite only wording that hides content needed by the FPF claim. |
| Bare pattern citation | The sentence cites a PatternID but still leaves the boundary unexplained. | State whether the cited pattern defines, constrains, tests, or supplies a method for the recovered content. |

### E.10.D1:9 - Consequences

The repair removes one convenient universal alias. Authors must sometimes name several values that the old word compressed, and legacy `ContextId`, `U.BoundedContext`, and two-part SenseCell fields need semantic repair rather than mechanical renaming.

In return, the author can use the method supplied for the subject question. Source-local meanings remain traceable to schemes and basis epistemes; model-use boundaries remain engineering structures; claim scopes remain scopes; working situations remain readable; obtaining `ArchitectureRelation` occurrences remain distinct from `ArchitectureClaim` content; and environment, domain, and publication claims keep their own participants and tests. A local repair can stop after one sentence, while recurring problems can reuse `E.10.ARCH` without copying a second ontology into every DPF.

### E.10.D1:10 - Rationale

The useful outcome of the earlier edition was to make context wording visible, separate situational narrative from semantic locality, and demand explicit treatment of cross-local meaning. Its mechanism was too strong: one universal `U.BoundedContext` erased distinctions that later FPF patterns now make directly.

Positive recovery is preferred to a forbidden-word list. A spelling check can find candidates, but only the receiving claim tells whether the phrase hides a scheme, scope, structure, situation, or other value. Naming that content opens the next practical move; banning the word does not.

### E.10.D1:11 - SoTA-Echoing

| Practice question | Current or lineage source | Use of source | FPF response | Adoption status |
| --- | --- | --- | --- | --- |
| How should terminology distinguish the thing discussed, its concept, definition, and designation? | ISO 704:2022, *Terminology work — Principles and methods*. | Current terminology-work reference for this narrow distinction; it is not authority over FPF ontology. | `C.2.1`, `F.17`, and this pattern keep the claim-bearing episteme, reference scheme, local expression, local-sense claim, designation, and the value designated by that expression separate. | **Adopt and specialize.** Adopt the separation; use FPF claim and relation identity. |
| How should a model boundary remain explicit in domain-driven design? | Eric Evans, *Domain-Driven Design Reference* (2015 reference edition); DDD Crew, *Context Mapping* (maintained practice resource, checked 2026-08-10). | DDD lineage plus current practitioner material: bounded contexts and their relations answer explicit model and integration questions, and small question-specific maps are preferred to one all-purpose map. | A.1.1 defines direct model-applicability, actual-use, and fixed-content-coherence relations and gives the practitioner the condition for selecting `BoundedModelUseStructure`: their organization must change the engineering decision. | **Adapt.** Keep the Plain retrieval term and decision focus; reject use as a universal semantic, organizational, or project container. |
| What makes a model usable for one engineering decision rather than usable without qualification? | Erik Rosenlund et al., [*The Role of Standardization for Simulation in Model-Based Systems Engineering: A Survey Study Supplemented with Industrial Experiences*](https://doi.org/10.1007/s10270-025-01344-8) (2025). | The survey and four industry accounts make intended use and known limitations necessary to model handoff and ask whether a model or its result can be used for that intended use. The evidence concerns modeling and simulation practice; it does not define every FPF model relation. | A.1.1 separates model applicability, actual assigned-Work use, and fixed-content coherence. The practitioner therefore starts with the direct relation that changes the decision and selects a wider structure only when its organization matters. | **Adopt the use-specific boundary.** Reject an unqualified model “context” and reject a metadata package as proof that the relation obtains. Do not import simulation-specific credibility machinery into every model use. |
| Which qualifications belong to a claim rather than to one generic context object? | Veronica dos Santos et al., [*CoaKG: A Contextualized Knowledge Graph Approach for Exploratory Search and Decision Making*](https://doi.org/10.4230/TGDK.3.1.4) (2025). | CoaKG shows that temporal and provenance qualifiers and task constraints can change whether a claim answers a decision. Its contextualized-graph formalism is a comparison source, not an FPF data model. | A.2.6 keeps the claim, `U.ClaimScope`, admitted slices, qualification window, effective scheme, comparison scheme, and evidence relations distinct. Provenance does not become a member of one universal Context participant. | **Adapt the separation.** Reject the source's generic context label as a new U-kind and stop the transfer before its graph representation and inference rules. |
| How should ambiguous wording be repaired when the missing detail changes downstream work? | Anmol Singhal et al., [*Generating Clarification Questions for Disambiguating Contracts*](https://aclanthology.org/2024.lrec-main.672/) (LREC-COLING 2024). | The study asks targeted clarification questions so non-legal readers can turn ambiguous clauses into actionable requirements. Its contract corpus and automated question generation do not establish a general ontology or an automatic FPF repair. | Step 1 asks what the reader would do differently; the selected recovery branch then returns one repaired statement or an honest unresolved result. A working situation, project use, or reader use is recovered only when naming it changes that action; otherwise the ordinary non-use boundary applies. | **Adapt the action test.** Keep human judgement and the truthful stop; reject contract-specific automation as the general method. |
| Should architecture, its description, and a viewpoint be recovered as one kind of context? | [ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise — Architecture description*](https://www.iso.org/standard/74393.html). | This is a published architecture-description comparator, not SoTA authority for FPF architecture. It distinguishes an entity's architecture from an architecture description and treats viewpoints as conventions used in that description; it explicitly does not define the entity's architecture or environment. | C.30 distinguishes the described holon, obtaining `ArchitectureRelation`, selected structure, and `ArchitectureClaim`. E.17.0 separately tests a candidate episteme against a viewpoint edition. | **Adapt only the separations.** Do not import its heterogeneous Entity-of-Interest list as an FPF kind hierarchy or treat architecture, viewpoint, and environment as one recovery branch. |
| What does an operating boundary contribute to an environment or operating-condition claim? | Morayo Adedjouma et al., [*Defining Operational Design Domain for Autonomous Systems: A Domain-Agnostic and Risk-Based Approach*](https://doi.org/10.1109/SOSE62659.2024.10620936) (SoSE 2024). | The paper treats an operational design domain as a delimited operating domain that combines technological, environmental, regulatory, and user considerations for autonomous systems. It does not make an environment an architecture or viewpoint. | The environment branch returns to the subject claim and names the holon, relation, state, qualifier, constraint, or condition whose change affects the claim or action. | **Adapt the explicit operating boundary.** Reject automatic promotion to architecture and stop the transfer at claims about operating conditions; the paper does not supply a universal environment ontology. |
| How should lexical labels remain distinct from concepts, schemes, and ontology entities? | W3C SKOS Recommendation (2009) and OntoLex-Lemon Community Report (2016). | Older but still current reference models for this limited separation. Their classes and mapping properties are source vocabulary, not imported FPF relation semantics. | F.17 defines local expression and sense under a by-value scheme; F.9 independently tests each direct Bridge and each proposed bounded use. | **Adapt.** Keep label/sense/scheme separation; reject scheme membership or a mapping label as relation truth or use permission. |

These comparisons support the recovery branches for the wording uses named here. They do not show that the branch set is complete for every use of *context* or that this method dominates every alternative. The comparison changed the method in four places: it made intended model use explicit; kept claim scope, qualification, and provenance separate; split architecture, viewpoint, and environment; and made the wording repair depend on the reader's next action. Reopen the method when a subject pattern defines a better distinction, a recurring use of *context* needs another productive branch, or a current practice source changes one of these action-bearing separations.

### E.10.D1:12 - Relations

- Apply `E.10` to recognize a local wording problem and make the smallest local repair. Apply `E.10.D1` when *context* hides content that changes the statement or next action.
- Apply `E.10.ARCH` when the same consequential wording problem recurs across framework contributions. That pattern supplies the shared restoration method; `E.10.D1` supplies this word-specific branch.
- `A.1.1` defines the direct model-use relations and the decision condition for selecting `BoundedModelUseStructure`.
- `A.2.6` defines claim scopes, context slices, and their membership facts. `C.2.1` identifies claim-bearing epistemes and their effective schemes.
- `F.0.1` supplies the source-local recovery method, exact F.17 cell and basis-relation result, reuse rule, and stop. `E.10.D1` recognizes the wording use and returns the repaired sentence; it does not repeat that recovery method.
- `F.1` is used only when source selection is live. `F.0.2` is used only when several source ontologies must be compared for one receiving claim. Neither follows automatically from a source-local wording repair.
- `F.17` defines `SchemeSenseCell`, `SenseCellAddressRef`, and `LocalSenseBasisRelation`. `F.9` defines semantic-context projection, direct Bridge truth, separate bounded-use claims, and reliance boundaries; use `F.9` only when the receiving claim needs that cross-local relation.
- `C.30` defines the obtaining `ArchitectureRelation` and the separate `ArchitectureClaim` form. Use the actual relation only when its predicate holds; use claim content for a negative, unresolved, candidate, or expected architecture statement.
- `E.17.0` defines viewpoint identity, the direct `EpistemeViewpointConformanceRelation`, its readable positive, negative, and unresolved results, and the resulting same-episteme `U.View` membership.
- For environment, operating-region, and operating-condition wording, use the pattern that defines or constrains the subject claim. When the affecting fact or condition cannot be recovered, keep the wording result unresolved rather than inferring architecture or viewpoint content.
- Apply `F.19` only for final phrase repair after the ontology and practical use are recovered. Apply `F.18` only when the repair creates a durable reusable designation.

### E.10.D1:End

