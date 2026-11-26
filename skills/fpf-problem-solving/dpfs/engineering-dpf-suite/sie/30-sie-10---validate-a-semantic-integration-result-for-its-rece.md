## SIE.10 - Validate a Semantic Integration Result for Its Receiving Use

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SemanticIntegrationValidationAccount@Use` that supports a bounded pass, narrow, unresolved, or stop conclusion with appropriate evidence and reopen conditions. A positive receiving-use claim covers all of its load-bearing obligations.

### SIE.10:1 - Problem Frame

**Use this when** you need to judge whether a candidate semantic interface or mapping package is fit for a receiving use. Enter especially when one test family already passes and is being used as evidence for the whole: valid JSON, conforming RDF shapes, successful ETL, high matcher score, complete provenance, good data-quality metrics, or one successful demonstration.

Judge one semantic-integration result against one receiving-use contract for an identifiable package revision that you can inspect. The first move is to identify the receiving claim being judged and whether known evidence already settles a bounded failure or unresolved result. For a positive claim, identify its load-bearing obligations and the evidence that can test them. The first result can be a supported local failure, scoped uncertainty, or qualified positive use.

The receiver can see which result it may rely on, under which source editions and conditions, and which gaps remain. Do not use SIE.10 to authorize product release, accept a quality result, approve a recall, certify a service, or prove business effectiveness. Those with the relevant authority can use the validation account when making those decisions.

### SIE.10:2 - Problem

Semantic integrations fail across several independent layers. A carrier can be well formed while meanings are wrong; correspondences can be defensible while transformation code violates them; identity rows can pass while claim conflicts are flattened; provenance can be complete while source claims are stale or false; quality dimensions can look good while the representative workflow receives the wrong answer.

One aggregate “quality” or “confidence” score hides which premise failed and what must reopen. It also encourages compensating a hard stop, such as unresolved identity or unauthorized source use, with strong results elsewhere.

### SIE.10:3 - Forces

| Force | Tension |
| --- | --- |
| Layering | Separate tests localize defects, while the receiver needs a whole-use conclusion. |
| Positive evidence | Expected matches demonstrate a path, while negative and unlike cases reveal hidden compression and defaults. |
| Coverage | A positive use claim needs its load-bearing premises supported, while a bounded failure can be settled by sufficient defect evidence. |
| Automation | Schemas, shapes, queries, and metrics scale checks, while semantic and authority judgments often require input from participants with relevant domain knowledge or authority. |
| Change | Stable evidence is reusable, while source editions, rules, interfaces, and receiving conditions can invalidate only some results. |
| Decision pressure | Stakeholders want a pass or fail. The evidence may support only a narrower use or leave the result unresolved. |

### SIE.10:4 - Solution

State the conclusion at the scope its evidence supports. A known decisive failure or bounded unresolved premise can finish with sufficient evidence for that result. For a positive whole-use or contract-permitted narrower result, obtain matching evidence for every load-bearing premise, including the receiver's interpretation. Use earlier results when their conditions still match. Preserve hard stops and distinguish unexamined premises from passing ones.

#### SIE.10:4.1 - Pattern-Use Unfolding

Steps 3–10 locate the grounds for the claim at issue. A supported finding can finish at step 2 when it settles that claim. For each remaining obligation, use an applicable rule, prior result or new observation according to what it establishes. A specification can settle what behaviour is prescribed. A claim that this implementation produced a response, or that a recipient acted on it, needs evidence of that occurrence. Perform a new test when commissioned or when the available grounds leave an important behaviour open.

1. **Identify the validation subject.** Name the mapping, interface, or package result and receiving use being judged. Record the revisions and conditions on which the conclusion depends.
2. **Choose the conclusion and inspect known evidence.** Take the relevant answer claim and stop condition from `SIE.1`. If a demonstrated defect already defeats it, return that bounded failure with sufficient evidence. If a necessary technical premise is unresolved, identify the affected claim. Apply the receiving authority’s separate acceptance rule. When a required record is absent at the contractual deadline, the authority can refuse that release while the technical property remains unknown. Keep the grounds for that decision distinct from evidence of a technical failure. For a positive claim, derive all load-bearing distinctions, loss, currentness/service/quality, authority, protection, branch, and representative-use obligations.
3. **Validate carrier and schema.** Test parseability, declared schemas/shapes, required fields, datatypes, cardinalities, identifiers, and branch encodings. Treat a pass as structural only.
4. **Validate semantic-model and endpoint adequacy.** Test whether source and target concepts, types, relations, constraints, units/codes, and any supplied model express the required distinctions throughout the scope claimed. Use discriminating cases where these distinctions remain in doubt.
5. **Validate correspondences and mappings.** Challenge the accepted `SIE.4` relations under the conditions of use. Establish whether the `SIE.7` rule preserves selection, cardinality, conversion, defaults, errors, loss and trace where the claim relies on them. For implementation behaviour, use suitable execution evidence or a conformance argument that covers the actual implementation.
6. **Validate identity and authority.** For each identity disposition used in the conclusion, establish what the source entries designate at the grain the decision requires. Check the issuer, version, effective interval, part–whole relation, reuse or split/merge where differences there could change the attribution. Preserve an unresolved branch that affects the decision. Verify required authority and permission inputs from their governing basis.
7. **Validate claim composition.** Test `SIE.6` comparability, conflict, non-comparability, supersession, incomplete-source, and uncertainty branches. Confirm that source claims and derivation remain recoverable.
8. **Validate realization and interface behavior.** Test currentness, latency, availability, snapshot/caching, invalidation, source failure, partial results, access/protection, provenance, error semantics, and challenge paths required by `SIE.8` and `SIE.9`. A timed response establishes this execution’s elapsed time. For a guarantee across loads, establish a bound under the admitted joint request and resource conditions. A percentile requires evidence for the specified request population and measure.
9. **Validate provenance, currentness, and quality.** Check that every relied-on output can recover its source and rule premises, that source/version/time status satisfies the use, and that selected quality measurements meet their action-changing thresholds. Do not treat provenance or process conformance as truth.
10. **Establish the receiving result.** Follow the qualified output to the action or judgement the recipient needs. Use matching earlier evidence when it covers the interpretation, terms and setting. Where the interpretation or behaviour remains uncertain, replay the use under conditions that discriminate the outcomes. For an order to run the query or observe the workflow, obtain evidence of that performance. If the order also calls for a particular reviewer’s independent judgement, establish what that reviewer examined and decided with the assistance permitted by the order.
11. **Assign dispositions at the supported scope.** Use pass, narrow, unresolved, or stop for tested claims, and preserve any material unexamined reach. A positive narrow result states the contract-permitted subset and covers all of that subset's load-bearing premises; excluded branches remain explicit. A hard stop cannot be offset by scores elsewhere.
12. **Record repairs, returns, and reopen.** Send source, semantic, mapping, implementation, authority, or receiver defects to their direct owners; state which layer and consumers require retest after change.

#### SIE.10:4.2 - Record the Result

| Validation position | Required content |
| --- | --- |
| subject and use | package/interface revision, source/rule versions, realization/test state, receiver and use |
| obligations | premises relevant to the claimed conclusion; all load-bearing contract obligations for a positive use claim |
| layer result | layer, tested claim, method/case, evidence, expected/observed result, pass/narrow/unresolved/stop, defect owner |
| dependency | source, correspondence, identity, composition, mapping, realization or interface premise consumed |
| coverage | examined cases and matching earlier results; material unexamined or unresolved premises, distinguished from passing ones |
| use disposition | supported local failure or gap, or positive result with its conditions and full load-bearing coverage; excluded subset and hard stops |
| continuation | repairs or direct-owner returns, focused retest, affected consumers, reopen condition |

#### SIE.10:4.3 - What Changes in Practice

The team stops asking whether “the integration” passed one test. Each claim has an appropriate layer, evidence, and owner. A bounded subset can be used without hiding excluded rows, and a source or rule repair triggers focused revalidation instead of an automatic full rebuild or a silent continuation.

### SIE.10:5 - Archetypal Grounding

#### SIE.10:5.1 - Positive AP242/QIF Subset Validation

The constructed AP242/QIF package is frozen with named AP242/QIF source occurrences, correspondence set, identity dispositions, claim-composition rules, mapping specification, hybrid realization, and review interface. It uses SIE.1:5's stipulated receiving contract: the preceding 24-hour observation window, two-second response limit, and permission to return qualified evidence while showing unresolved local-extension and unknown-unit branches separately.

| Layer | Constructed probe and result |
| --- | --- |
| carrier/schema | Request and response validate against their declared forms; unmatched, incompatible, unresolved, stale, and source-error states are representable. Passes structurally. |
| semantic-model/endpoints | AP242 feature/configuration/effectivity and QIF plan/characteristic/result senses are recoverable. One local extension remains undefined; rows that consume it are unresolved. |
| correspondence | The assigned pair joins. A shared label with no assignment in the accessible excerpt leaves the link unresolved. A complete governing plan with no assignment establishes a non-match at that revision and effectivity. Both objects can be identified in either case. A non-dimensional characteristic defeats a global type equivalence. Return partial coverage when the receiving contract permits it. A contract for the complete set still needs the unresolved assignment settled. |
| identity/authority | Known feature identifier relation passes at revision/configuration/effectivity grain; obsolete revision and unresolved local ID stop their dependent branches. Engineering and quality authority remain external. |
| claim composition | Compatible AP242 definition/effectivity and QIF plan/result claims retain sources; contradictory result status returns conflict; incompatible intervals remain non-comparable. Passes for qualified branches. |
| transformation | Known mapping, one-to-many characteristic, unit conversion, unmatched feature, unknown unit, stale result, missing provenance, and source-timeout cases return the specified branches. One unknown-unit row stops. |
| realization/interface | Stable semantic metadata is available; volatile source data is queried under captured occurrence times. The one-second response meets the two-second deadline for this review query. Timeout returns an incomplete answer only where the contract permits it. Challenge paths resolve to the relevant premises. |
| provenance/currentness/quality | Every accepted output row recovers sources, rules, and times. The configuration matches the released review basis; QIF observations six hours before T meet the 24-hour window, while a 25-hour control returns stale. Undefined-extension rows remain visibly unresolved outside the qualified set. |
| receiving workflow | The quality engineer retrieves a known result, recognizes unmatched/incompatible/conflict states, and stops on unresolved configuration or identity. Passes for the bounded subset. |

The quality engineer can use the qualified rows under the **narrow** permission in SIE.1:5. Return the unresolved local extensions and unknown units separately as agreed. If an assignment needed for the requested feature is also unresolved, the contract gives no permission to omit it. Obtain the governing plan, report that the requested relation is still open, or agree with the recipient on a further partial return. A complete governing plan can establish the absence of an assignment for that revision even while other rows remain open. If the release authority requires a signed inspection record by its deadline and that record is missing, it can refuse release on those grounds. The unrecorded technical property can remain unresolved. A definition or unit-table repair reopens only the affected rows and receiving tests.

#### SIE.10:5.2 - A Decisive Defect and a Changed Receiving Meaning

In a constructed mapping probe, an input of 1 metre produces an output labelled 1 millimetre; the receiving contract requires 1000 millimetres. The known input and required conversion settle the verdict on this output. To assign the repair, inspect the applicable rule and what actually ran. A specification that prescribes the wrong factor returns to its author through SIE.7. If it specifies the correct conversion, trace the selected rule version, execution and output labelling to locate the failure. An order confined to judging this output can finish before its cause is known. If the source unit is unavailable instead, the conversion premise remains unresolved at that scope.

Now consider a previously qualified availability interface. Its JSON field and numeric type stay unchanged, but the source changes the value from present availability to a future promise horizon. The receiver still reads the displayed quantity as “available now”. A passing shape check cannot support the earlier use conclusion: the changed interpretation defeats a relied-on premise. SIE.11 identifies the affected mapping and interface uses.

After repair, a positive conclusion for that receiving use needs the corrected interpretation and every other load-bearing condition. Matching earlier evidence can supply unchanged conditions; the known failure or its repair alone cannot establish the whole result.


### SIE.10:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | The validation team is treated as release, quality, safety, or business authority. | State the semantic conclusion and return the owning decision with its conditions. |
| Architecture | Available automated tests define all validation layers. | Add qualified semantic, identity, authority, and receiving-work evidence where automation cannot decide. |
| Ontology/Epistemology | Well-formed representation, true relation, supported claim, and usable decision collapse. | Test each claim at its layer and keep the whole-use composition explicit. |
| Pragmatics | A decisive failure still triggers every layer test. | Finish the bounded failure with sufficient evidence; require full load-bearing coverage for a positive whole-use or permitted subset claim. |
| Didactics | A score invites compensation across hard stops. | Use categorical layer dispositions with evidence and state that stops are non-compensatory. |

### SIE.10:7 - Conformance Checklist

Apply the checks to the conclusion claimed. For a positive result, cover each load-bearing obligation with the appropriate grounds. Use the cases below where they distinguish live outcomes. Existing evidence can do that work. A bounded failure or unresolved result needs grounds for that conclusion and its effect on the original question.

- [ ] The subject, receiving use, and conditions required by the conclusion are identified.
- [ ] Known decisive evidence can finish a bounded failure or scoped gap; material unexamined premises remain distinct from passing ones.
- [ ] Carrier/schema pass is not reported as semantic or receiving-use pass.
- [ ] The endpoint or model can express the distinctions the question requires. Any example or counterexample used supports the stated scope.
- [ ] The grounds for the correspondence and those for the mapping's actual behaviour support their respective conclusions.
- [ ] Each identity disposition, authority condition and unresolved branch on which the answer relies is qualified for its use.
- [ ] Claim composition preserves required distinctions such as conflict, non-comparability, incomplete source and recoverable source claims.
- [ ] Realization/interface tests cover currentness, failure, partial results, access/protection, provenance, and challenge paths as applicable.
- [ ] The evidence covers the features of receiving Work that determine the claim. A claim about an actual performance has evidence of its occurrence, and any newly commissioned trial was performed.
- [ ] The positive, boundary, negative, unlike or changed-source cases selected address failure modes left open by the other evidence.
- [ ] Whole-use disposition is pass, narrow, unresolved, or stop with no score-based compensation of hard stops.
- [ ] Repairs, direct-owner returns, focused retests, affected consumers, and reopen conditions are explicit.
- [ ] No external release, acceptance, authorization, effect, or universal correctness claim is implied.

### SIE.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Valid schema, therefore valid integration | Test meanings, relations, identity, composition, mappings, provenance, quality, and receiving Work separately. |
| One quality/confidence score | Record layer-specific evidence and categorical dispositions; preserve hard stops. |
| Happy-path demonstration | Identify the permitted condition that might defeat the claim. Obtain the distinguishing evidence or a sufficient argument that already covers it. |
| Provenance completeness means truth | Test the source claim and receiving adequacy; provenance only makes derivation inspectable. |
| High alignment benchmark score | Validate local endpoint relations and use loss against representative cases. |
| All-or-nothing readiness | A known defect can finish a bounded failure. A positive subset result requires the contract's permission and all premises on which that subset relies. |
| Semantic validation authorizes release | Return the account to the engineering, quality, safety, legal, or application authority. |

### SIE.10:9 - Consequences

Defects are localized to source, semantic, identity, composition, mapping, realization, interface, quality, or receiving-use layers. A bounded useful result can proceed without hiding excluded branches, and later changes can trigger focused replay through explicit dependencies.

The cost is several kinds of evidence and collaboration with domain and receiving practitioners. Some integrations that appear technically complete remain unresolved or stop because their identity, authority, or representative-use premises are missing.

### SIE.10:10 - Rationale

Semantic integration is a claim chain. Different links require different evidence, and the receiver depends on their composition. Layered validation keeps the scope of each test result explicit. A positive conclusion requires support for every load-bearing premise of the claimed whole use or contract-permitted subset.

### SIE.10:11 - SoTA-Echoing

The best-known line combines constraint validation, ontology-alignment evaluation, provenance, data-quality models, quality management, and user/task validation. The serious defaults are conformance-only testing and aggregate quality scoring. Conditions at different layers need their own evidence. Even when every condition is measured, a high score at one layer cannot offset failure of a required condition at another. SIE.10 combines these contributions in a dependency-aware account with categorical bounded dispositions and representative Work replay.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| [SHACL](https://www.w3.org/TR/shacl/) | adapt | Supplies declared RDF graph constraint validation; passing shapes do not establish all semantics, identity, truth, or use fitness. |
| [DQV](https://www.w3.org/TR/vocab-dqv/) and [ISO/IEC 25012:2008](https://www.iso.org/standard/35736.html) | adapt | Supply quality vocabulary and a data-quality model; select dimensions and measurements by receiving action. |
| [ISO 8000-61:2016](https://www.iso.org/standard/63086.html) | adapt | Contributes data-quality management process questions; process conformance does not prove fitness of the answer for its receiving use. |
| [OAEI 2025 results](https://oaei.ontologymatching.org/2025/results/) | adapt | Provide alignment-evaluation tasks and evidence; a local correspondence set still needs evidence for its intended use. |
| one conformance gate or aggregate score | reject as sufficient | Unlike layers and hard stops must remain separately visible before a whole-use conclusion. |

Reopen when a relied-on source, model, identifier, correspondence, composition, mapping, realization, interface, quality threshold, or receiving workflow changes; when new evidence defeats a layer; or when a representative case exposes an untested load-bearing obligation.

### SIE.10:12 - Relations

- `SIE.1` supplies the receiving obligations, accepted loss, authority, representative cases, and stop rules.
- `SIE.2` supplies source meanings, editions, authority, provenance, access, currentness, and gaps.
- `SIE.4`–`SIE.9` supply the correspondence, identity, claim-composition, mapping, realization, and interface subjects and their branch contracts.
- Current FPF `A.10` and `A.10.1` govern evidence/provenance reliance and generic affected-use discovery.
- `SIE.11` traces changed source, model, mapping, or interface premises to the receiving uses that rely on them. Matching earlier validation remains usable for unaffected results; material changes reopen the relevant premises and receiving interpretation.
- Applications, Systems Engineering, quality, safety, legal, MDM, Data Engineering, and Operations owners consume the bounded account and retain their own acceptance, authorization, operation, and outcome decisions.

### SIE.10:End
