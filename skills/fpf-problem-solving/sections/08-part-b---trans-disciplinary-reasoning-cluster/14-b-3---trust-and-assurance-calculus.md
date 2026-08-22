## B.3 - Trust and Assurance Calculus

> **Type:** Foundational (B)
> **Status:** Stable
> **Normativity:** Normative when an FPF use makes an assurance claim about one exact target claim.

> **Plain-English headline.**
> B.3 helps a practitioner state what an assurance claim is about, which argument and results support it, what use they support, what remains unsupported, and what would reopen the conclusion. It does not turn a badge, evidence item, calculation, record, publication, status, or decision into assurance by appearance.

**Use this when.** Use B.3 when an actual named assurance claim is current: for example, a claim that an exact model claim is credible for one decision, or that an exact safety claim is adequately supported for one release use.

**First useful move.** Write the target claim and the assurance use in one sentence. Then ask which direct results and argument make that use supportable. If there is no assurance claim, stop and use the pattern that defines or tests the actual evidence, status, gate, permission, safety, release, work, or domain-result claim.

**What goes wrong if missed.** A visible label or a convenient score starts raising trust without an exact target, argument, basis, limitation, and use. At the other extreme, a modest assurance question is forced through a universal score and a large record whose fields do not affect the decision.

**What this buys.** The user gets the smallest assurance result that changes the named use, with enough basis and limits to inspect or reopen it. Domain-specific characteristics and calculations remain usable without pretending that unlike measures share one scale.

**Not this pattern when.** Stay with `A.2.4` for the classification of an episteme as evidence, `A.10` and `G.6` for source recovery and bounded reliance, `G.11` for currentness, `F.10` for a status value and its use, `A.21` for a gate decision, and the direct domain pattern for safety, permission, access, responsibility, release, compliance, or controlled action. Consequence alone does not create an assurance claim. A direct domain rule may require one, but the claim must be stated before B.3 is applied.

**First output.** Produce either one bounded `AssuranceResult` claim or a plain statement that the available argument does not support the attempted assurance use. Do not create a B.3 result merely to record that another pattern is relevant.

### B.3:1 - Problem frame

Assurance concerns a claim, not the world-side subject in isolation. Begin with one exact C.2.1 target-claim episteme and one named use of an assurance conclusion. The claim's EntityOfConcern remains the system, episteme, method, work occurrence, relation occurrence, or other exact subject identified by its direct pattern.

For example:

- a battery-pack safety fact and its direct test result remain under their safety, measurement, and test patterns;
- the episteme that states the safety claim remains under C.2.1;
- an assurance result states whether a named argument carries that claim for a named release use;
- a later gate, permission, or release decision remains a separate result.

The word **calculus** here means a disciplined way to select, combine, and interpret the inputs that the assurance argument actually consumes. B.3 defines no universal arithmetic across systems and epistemes.

### B.3:2 - Problem

Five failures recur:

1. **Assurance by appearance.** A badge, dashboard, attestation, card, status, or publication is treated as the assurance conclusion.
2. **One scale for unlike properties.** Formality, reliability, coverage, congruence, and evidence quality are placed in one tuple even though they have different bearers and scales.
3. **Unsupported aggregation.** `min`, an average, a penalty, or another fold is called conservative without a dependency model and calibrated quantities.
4. **Process burden by default.** Every result is required to name dated Work, Method, assignment, bindings, and a reusable record even when the claim's own basis closes the use.
5. **Domain obligations absorbed into assurance.** Safety, rights, access, responsibility, contest, redress, status, or controlled-action rules are replaced by a generic assurance record.

### B.3:3 - Forces

| Force | Tension |
| --- | --- |
| Small result vs inspectability | A practitioner needs a quick result, while a consequential or reusable claim may need a replayable argument. |
| Shared discipline vs domain meaning | Assurance needs common boundaries, while each characteristic and aggregation rule gets its meaning from its subject and domain. |
| Conservatism vs useful synthesis | The result must avoid overstatement without discarding justified combination or independent lines of support. |
| Formal clarity vs warranted belief | Formalization can improve inspectability and checking while leaving truth or empirical adequacy unchanged. |
| Current use vs change over time | An assurance conclusion must be usable now and reopen when its basis, scope, or conditions change. |

### B.3:4 - Solution

#### B.3:4.1 - Start from one assurance question

State these three things before choosing measures or a record:

1. the exact target claim;
2. the named assurance use;
3. the conclusion that must be supported, narrowed, or refused for that use.

Keep the following objects separate whenever they are current:

1. world-side facts and direct domain results;
2. the target-claim episteme;
3. evidence-use relations and source-provenance paths;
4. any assessment Work and the System that performed it;
5. formal, empirical, causal, measurement, conformance, or comparison input results;
6. the assurance-result episteme;
7. calculation traces, witnesses, and an optional note or publication that cites the result;
8. later reliance, status use, gate, permission, release, or action.

Evidence can support or challenge a claim. It does not make the target fact true. A favorable assurance result does not pass a gate, grant permission, or prove that later work relied on it.

#### B.3:4.2 - Use the smallest sufficient result

The compact result contains only facts every B.3 use needs:

```text
AssuranceResult:
  targetClaimRef:
  assuranceUse:
  basisRefs:
  disposition: supported-for-use | narrowed | abstain | evidence-needed | reopen | blocked
  limitationsAndNotCarried:
  reopenCondition:
```

`targetClaimRef` identifies the exact C.2.1 episteme or one exact C.2.1 `ClaimAddress` when the use concerns one addressed claim inside a larger episteme. `basisRefs` cite the direct results, evidence-use relations, provenance paths, argument claims, or domain rules actually used. A compact result is complete when these fields decide the named use and another person can see why the stronger use is not carried.

Add a claim scope, condition set, interpretation scheme, audience, or time window only when changing it could change the conclusion. Keep design and run conclusions separate whenever their inputs or conditions differ.

Add assessment Work, performer, Method, application bindings, witnesses, or a reusable record only when the receiving use depends on competence, conflict of interest, timing, reproducibility, contest, redress, or later replay. These identities are never mandatory merely because B.3 is used.

An optional assurance note may cite the result and its basis. B.3 does not define a reusable `RelianceSafetyCase`, a safety authority, or a general contest-and-redress profile. If such a reusable object is needed, it requires its own problem, ontology, sources, minimum output, and direct domain boundaries.

#### B.3:4.3 - Name each characteristic by its bearer and scale

Include a characteristic result only when the assurance argument consumes it. State:

```text
AssuranceCharacteristicResult:
  bearerRef:
  characteristic:
  scaleAndUnit:
  valueOrInterval:
  interpretationForThisUse:
  basisRef:
```

One characteristic name must not silently change meaning between subjects. System reliability, replication quality, evidential support, proof inspectability, and relation congruence are different characteristics even when a local source labels several of them `R` or `CL`.

The legacy letters `F`, `G`, `R`, and `CL` may appear inside a declared local scheme, but B.3 assigns them no universal cross-domain meaning:

- **Formality or inspectability.** Formal structure can make assumptions and inference steps easier to check. It raises assurance only when the named argument explains which uncertainty or verification need it closes. Making a wrong model proof-grade does not improve truth or empirical adequacy.
- **Claim scope.** `U.ClaimScope` stays an A.2.6 value. It is not a quality coordinate. Widening or narrowing scope changes the claim and its applicable use under the declared scope rules.
- **Reliability-like characteristics.** Use the exact domain definition, bearer, population or trials, conditions, scale, unit, and qualification window. A system reliability measure and an evidence-quality judgment are not interchangeable.
- **Relation congruence.** Characterize one exact mapping, calibration, interface, or other relation occurrence only under a declared scale and interpretation. The value neither changes the participants nor supplies a universal penalty.

Never average ordinal values. Do not subtract an ordinal value from a ratio quantity. Thresholds and order comparisons are valid only under the scale that defines them.

#### B.3:4.4 - Aggregate only under an applicable model

B.3 supplies no default fold. When the assurance argument combines quantitative or ordered inputs, cite:

1. the exact result claims being combined;
2. the dependency or alternative-path structure;
3. the domain aggregation rule or model;
4. independence, dependence, calibration, and unit assumptions;
5. the calculation or ordered comparison;
6. the rival rule that would matter if an assumption fails.

Use `min` only when the cited domain rule makes the weakest input a lower bound or bottleneck for the exact quantity. It is not universally conservative. If no applicable aggregation rule is available, report the inputs separately and return a bounded, non-positive, or unresolved disposition. Do not manufacture one score to make the result look complete.

Several independent evidence lines may strengthen an argument only through the rule that states how their dependence and coverage are handled. Claim-scope intersection or union follows A.2.6 and the relevant evidence model; it is not an assurance arithmetic shortcut.

#### B.3:4.5 - Choose one of three proof paths

**Compact path.** Use the six-field result in 4.2. Stop when it decides the named use.

**Calculated or model-bearing path.** Add the characteristic results, dependency structure, assumptions, aggregation rule, rival, calculation trace, and sensitivity or failure condition actually used.

**Replay path.** Add Work, System, Method, assignment, application bindings, witnesses, and a reusable note only when the named assurance use depends on those identities. The System performs the assessment Work. The Work, Method, assignment, result, witness, note, and publication remain separate.

Do not select the replay path merely because the use is important. Importance may make more basis necessary, but every added field must change inspectability, contestability, or the decision.

#### B.3:4.6 - Keep visible authority outside the result

A badge, score, dashboard tile, credential display, provenance mark, model card, datasheet, data card, assurance document, attestation, generated confidence phrase, or publication form can be a cue, source, evidence item, or representation. It contributes to assurance only through an exact claim and basis relation used by the argument.

If the visible item only reports a status, gate decision, permission, warning, or source location, use its direct pattern and produce no B.3 result. If an assurance claim is current, cite the item only for the property it actually establishes. A valid signature or provenance chain can establish origin and integrity without establishing safety, truth, compliance, or readiness.

#### B.3:4.7 - Leave domain obligations with their direct patterns

B.3 evaluates an assurance claim. It does not define safety duties, access rules, responsibility, affected-party disclosure, contest, redress, people or team status, resource allocation, release authority, or controlled action. Cite each applicable direct rule as a premise or limitation.

When a direct domain rule says a consequential use requires an assurance claim, state that claim and then apply B.3. When the direct rule requires a decision, permission, review, contest route, or redress relation instead, use that result directly. A display that affects behavior does not by itself open B.3.

#### B.3:4.8 - Preserve time, currentness, and design/run distinctions

State the exact window only when time changes the assurance conclusion. Monitoring, drift, incidents, evidence refresh, version change, policy change, gate change, or a newly discovered defeater can narrow, reopen, or withdraw a result while the target fact and target-claim identity remain unchanged.

Design evidence and run evidence may support different claims. Produce separate results when target use, conditions, scope, or evidence window differs; compare them instead of merging them into one score.

#### B.3:4.9 - Keep causal-use and method-structure branches direct

When an assurance argument depends on a causal-use claim, consume the exact `C.28` result and its stated supported and unsupported uses. B.3 does not re-run causal identification. An unsupported causal-use result narrows, blocks, or leaves the assurance claim unresolved; it does not become a low universal reliability coordinate.

When composition, fallback, selection, or family organization among Methods matters to the assurance argument, use `A.22` to select the exact structure for that question and use the local designator `MethodRelationStructure` only for that selected structure. Do not introduce a universal method-relation kind or infer structure from a list of Methods.

#### B.3:4.10 - Use Working-Model declarations only for what they state

An E.14 Working-Model assertion may contribute its declared validation posture and grounding links. A postulate still needs the empirical basis required by the current assurance use; an inferential claim needs its reasoning basis; an axiomatic or constructive claim needs the exact construction and identity basis it relies on. The declaration, grounding link, assessment Work, assurance result, and publication remain different objects.

### B.3:5 - Proof obligations

#### B.3:5.1 - Common obligations

Every positive or narrowed B.3 result:

1. identifies the exact target claim and named assurance use;
2. cites only basis results and relations that actually bear on that use;
3. states assumptions, limitations, and unsupported stronger uses;
4. keeps target fact, claim, evidence, assessment, result, record, publication, and later use distinct;
5. names a reopen condition;
6. uses the direct domain rule for every safety, permission, access, status, release, responsibility, or controlled-action premise;
7. avoids aggregation unless its model and assumptions are explicit.

#### B.3:5.2 - Additional obligations for a calculated result

A calculated result also names every bearer, characteristic, scale, unit, dependency, calibrated mapping, aggregation rule, and calculation. It shows at least one assumption whose failure changes the result. If a rival rule is plausible at comparable effort, show why the selected rule fits the declared dependency structure.

#### B.3:5.3 - Additional obligations for replay

A replayable result adds only the Work and performance facts needed by the receiving use. Identify the assessment Work, the System that performed it, and any Method, assignment, application binding, witness, or timing fact on which competence, independence, reproducibility, contest, or redress actually depends. No record field stands in for an obtaining relation.

### B.3:6 - Worked cases

#### B.3:6.1 - Fully calculated case: two necessary independent conditions

Target claim: “The protection function succeeds on a demand.” Assurance use: a bounded reliability argument for a named design decision.

The domain model says that both independently tested conditions must succeed: sensor detection and actuator response. Each has estimated probability `0.9` under the same stated demand class and qualification window. Under the declared independence assumption, the joint probability is:

```text
0.9 × 0.9 = 0.81
```

Using `min(0.9, 0.9) = 0.9` would overstate this conjunction. If the conditions are dependent, even the product is not justified; the result must use the applicable conditional model or remain unresolved. The B.3 result therefore cites the two domain results, the series dependency structure, independence basis, product calculation, `0.81` conclusion, limitations, and the observation that reopens the independence assumption.

What changes in practice: the design decision is evaluated against `0.81`, not a falsely “conservative” `0.9`. No universal B.3 reliability formula is created.

#### B.3:6.2 - Routed-away case: dashboard status

Starting sentence: “The dashboard approves launch.”

The dashboard is a publication face. Suppose it displays `GateDecision GD-17`, which records that a named gate passed for release candidate R. The repaired sentence is: “The dashboard shows GateDecision GD-17 for release candidate R; the decision, not the display, records that the gate passed.”

Use A.21 and the release or permission pattern that consumes the gate decision. No assurance claim is present, so B.3 stops. If the dashboard does not resolve an exact gate decision, it is only a cue and launch approval remains unresolved.

#### B.3:6.3 - Episteme credibility with a compact result

Target claim: “Model edition M predicts response Y within the declared operating region.” Assurance use: whether an engineer may use that prediction as one input to a reversible design comparison.

The engineer cites the exact model claim, its empirical-validation result, the A.2.4 evidence-use relation, the A.10 provenance path, the operating region, and the expiry condition. No combination of unlike characteristics is needed. The compact disposition is `supported-for-use`, limited to the reversible comparison; release, safety, and operation are expressly not carried. No dated assessment Work or reusable record is added because the use does not depend on who performed the already cited validation.

#### B.3:6.4 - Order-sensitive Method case

An assurance argument relies on a manufacturing sequence whose result changes when two steps are reversed. The practitioner uses the direct Method and Work patterns for the sequence and, only because organization among several Methods affects the argument, uses A.22 to select a `MethodRelationStructure` for that exact question. The assurance result cites the sequence result and selected structure; B.3 creates neither the Methods nor their order.

### B.3:6.5 - Bias annotation

| Risk | Countermeasure |
| --- | --- |
| Formal prestige | Ask what uncertainty or verification need the formalization closes. |
| One-number preference | Keep unlike characteristics separate unless an applicable model combines them. |
| Visible-authority bias | Resolve the exact claim and property established by the artifact. |
| Record completion bias | Add only fields the named use consumes. |
| Consequence inflation | Use direct domain rules; consequence alone creates no assurance claim. |

### B.3:7 - Conformance checklist

| ID | Requirement |
| --- | --- |
| `CC-B3-1` | One exact target claim and one named assurance use are stated before measures or records are selected. |
| `CC-B3-2` | The compact result contains target, use, basis, disposition, limits, and reopen condition; optional fields appear only when they change the conclusion or its replay. |
| `CC-B3-3` | Every characteristic has one bearer, property, scale and unit where applicable, interpretation, and basis. |
| `CC-B3-4` | Formality is not treated as monotone truth, empirical adequacy, or warrant. |
| `CC-B3-5` | Aggregation cites the domain model, dependencies, assumptions, units, calculation, and relevant rival; no default `min`, mean, penalty, or ordinal arithmetic is used. |
| `CC-B3-6` | Design and run results remain separate when their conditions or evidence differ. |
| `CC-B3-7` | Target fact, target claim, evidence use, assessment Work, input results, assurance result, witness, note, publication, and later reliance or decision remain recoverable separately. |
| `CC-B3-8` | A label, dashboard, card, provenance mark, attestation, or publication contributes only the exact property established through a cited relation. |
| `CC-B3-9` | Safety, rights, access, responsibility, contest, redress, status, permission, release, and controlled action remain with their direct patterns. |
| `CC-B3-10` | A causal-use premise cites the exact C.28 result; a Method-organization premise cites an A.22-selected structure only when that structure matters. |
| `CC-B3-11` | Work, System, Method, assignment, bindings, witnesses, and reusable notes are added only for an actual replay, competence, independence, timing, contest, or redress need. |
| `CC-B3-12` | A positive result states the unsupported stronger use and exact reopen condition. |

### B.3:8 - Common anti-patterns and repairs

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Universal weakest-link formula | `min` can be an upper bound for a conjunction and can ignore alternatives or dependence. | Use the exact dependency model and domain rule; otherwise report inputs separately. |
| Ordinal penalty subtraction | An ordinal label is subtracted from a probability or ratio quantity. | Use a calibrated mapping to the same quantity when one exists, or keep the values separate. |
| Formality raises assurance | A more formal wrong model receives a better result. | State the inspectability gain and the uncertainty it closes; keep truth and empirical adequacy separate. |
| Same letter, different property | `R` names system reliability in one row and evidence quality in another. | Give each characteristic its own bearer and definition. |
| Safety-case inflation | A warning, access value, or consequential display triggers a generic B.3 package. | Use the direct domain pattern; apply B.3 only to an actual assurance claim. |
| Evidence creates truth | New evidence is said to make the target fact obtain. | Revise the warrant or disposition unless the world-side facts changed. |
| Assessment-record collapse | A checklist, trace, witness, or note is treated as the assessment Work or result. | Identify each object separately and add only what the use consumes. |
| Design/run chimera | Blueprint evidence and runtime observations are merged into one score. | Produce separate results and compare them. |

### B.3:9 - Consequences

**Benefits**

- Assurance remains explicit without forcing one cross-domain score.
- A small local claim can stop after six fields.
- Calculations become more trustworthy because assumptions and dependency structure are visible.
- Domain safety, access, responsibility, status, and decision rules retain their own meaning.
- Visible artifacts can contribute useful provenance or evidence without becoming authority.

**Trade-offs**

- B.3 no longer supplies a convenient universal number. A project must use the domain model that gives its inputs meaning.
- Some assurance questions return `unresolved` until a dependency model, calibrated mapping, or direct domain requirement is supplied.
- Reusable replay records cost more than a compact result and therefore require an actual receiver.

### B.3:10 - Rationale

Assurance-case practice supports explicit claims, arguments, evidence, and maintenance. Reliability engineering supports calculations tied to dependency structure and assumptions. Neither supports one universal `F-G-R-CL` score across unlike subjects. B.3 therefore standardizes the boundaries and the minimum result while leaving characteristics and aggregation with the exact models that define them.

### B.3:10.1 - Decision-bearing SoTA account

| Practical question | Exact current source | Adopt, adapt, or reject in B.3 | Reopen condition |
| --- | --- | --- | --- |
| What makes an assurance case inspectable? | [ISO/IEC/IEEE 15026-2:2022, edition 2](https://www.iso.org/standard/80625.html) specifies assurance-case structure and maintenance. The [GSN Community Standard v3](https://scsc.uk/gsn-standard) gives current engineering-argument notation and guidance. | **Adopt** explicit claim, argument, evidence, context, defeater, and maintenance structure. **Adapt** it to the compact and replay paths. **Reject** document or diagram appearance as assurance, approval, or permission. This decision shapes 4.1, 4.2, 5, and the dashboard case. | A successor changes the required claim-argument-evidence relation or validated use shows that a compact field is missing or redundant. |
| How may reliability-like inputs be combined? | NASA's [Fault Tree Handbook with Aerospace Applications, v1.1](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Fault%20Tree%20Handbook_NASA.pdf), chapter 6, derives AND-event probability from conditional probability and uses a product only under independence. | **Adopt** dependency- and assumption-specific calculation. **Reject** universal `min` and any claim that it is always conservative. This decision shapes 4.4 and worked case 6.1. | A direct domain model with different validated dependence semantics applies to the current claim. |
| Can one trustworthiness tuple compare unlike AI or system properties? | [NIST AI Risk Management Framework 1.0](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=936225) treats trustworthiness characteristics as context- and use-dependent and recognizes trade-offs and domain metrics. | **Adopt** named characteristics and use-specific thresholds. **Reject** same-letter cross-domain comparability and monotone formality. This decision shapes 4.3. | A validated common measurement model supplies shared bearers, scales, units, and interpretation for the exact properties being compared. |
| What can provenance and attestation establish? | [C2PA Technical Specification 2.4](https://spec.c2pa.org/specifications/specifications/2.4/index.html) distinguishes provenance validity from value judgments. [in-toto Attestation Framework 1.2](https://github.com/in-toto/attestation/releases/tag/v1.2.0) defines authenticated metadata about software artifacts. | **Adopt** exact subject, source, binding, and verification claims. **Reject** a valid credential, manifest, attestation, or display as automatic truth, safety, compliance, readiness, or release. This decision shapes 4.6 and case 6.2. | A successor specification changes the property warranted by the artifact or a direct domain rule makes that property sufficient for the named use. |

Older assurance-case editions and generic weakest-link slogans are lineage, not decision authority. Popularity, formal appearance, and publication recency do not establish the selected architecture.

### B.3:11 - Relations

- **Builds on:** `C.2.1` for target and assurance-result epistemes; `A.2.4` for exact evidence-use classification; `A.10` and `G.6` for source-provenance paths and bounded reliance; `A.2.6` for ClaimScope; `C.16` and `C.16.Q` for characteristic and scale discipline; and the direct domain patterns for every input result.
- **Coordinates with:** `A.15.1` and `A.6.1` only when assessment Work and applications matter; `G.11` for currentness; `F.10` for status; `A.21` for gates; permission, commitment, release, access, responsibility, contest, redress, safety, and controlled-action patterns for their own results; and `E.17`, `E.24.PUB`, and `C.29` for publication and representation.
- **Coordinates with:** `C.28` for causal-use results and `A.22` for a selected `MethodRelationStructure` when Method organization is part of the assurance argument.
- **Used by:** a pattern or project decision that consumes one exact assurance result. The consumer still applies its own decision, permission, gate, status, or work rule.

### B.3:11a - Quantum-like claims

Quantum-like wording does not require assurance by itself. If the wording only prevents a local representation mistake, keep the note with `C.26` and ordinary evidence. Apply B.3 only when an actual assurance claim about that exact quantum-like result and use is current. A comparative superiority claim must name the rival model, baseline, claimed mechanism, scope, evidence, and loss. Mathematical novelty or prestige supplies no assurance.

### B.3:11b - Mathematical-lens use

When a C.29 mathematical-lens result is an input to an assurance claim, cite the exact lens-result claim, its interpretation and limits, the evidence-use and provenance relations relied on, and the named assurance use. Mathematical elegance or a structure-preserving mapping does not raise assurance by itself. Measurement construction and comparability remain with C.16.

### B.3:End

