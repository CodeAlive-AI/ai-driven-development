## E.17.EFP - ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**One-line summary.** `ExplanationFaithfulnessProfile` classifies the bounded explanation use of a publication form or representation of one exact claim-bearing episteme. It does not decide which episteme the text expresses and cannot turn changed claims into another form of the source.

**Explanation-facing text in plain terms.** One published text on an existing MVPK face. If it expresses the source edition's exact ClaimGraph, it is a publication form or representation of that source edition. If its claim content differs, it can be a form only of a separately identified target episteme, not of the source edition.

**Ontic first screen.** Before assigning an explanation class, compare the claims expressed by the text with the exact source ClaimGraph.

1. If the text expresses that same ClaimGraph, identify the applicable E.24.PUB publication form or A.6.3.RT representation of the source edition. EFP then qualifies only the explanation use of that form or representation.
2. If omission, reconstruction, pedagogy, or another change produces a different ClaimGraph, identify the exact target `U.Episteme` under C.2.1 and the obtaining source-to-target relation under `A.6.3.CR`, `A.6.3.CSC`, or another exact pattern. EFP may then qualify the explanation use of a publication form of that target; its class label creates neither the target nor the relation.
3. A new causal or counterfactual proposition is a claim of a separate hypothesis episteme under `B.5.2`, or it stays outside EFP. It is not a passive rendering of the source merely because reliance on it is blocked.

**Explanation-use relation in plain terms.** State which exact episteme the published text expresses, how that episteme relates to the named source when it is a different target, which explanation-use class applies, and what downstream claim or effect still stays outside the profile. Name the exact E.24.PUB publication occurrence, pins, traces, or provenance only when they are material to the present use.

**Use this when.** Use EFP when a real source-pinned, reconstructive, didactic, or speculative ambiguity changes how a published explanation form may be reviewed or used—especially for generated, retrieval-facing, model-facing, derivative, or interactive explanation. Authorship alone does not trigger the profile.

**Start here when.** First decide whether the text expresses the same source ClaimGraph or a different target ClaimGraph. Only after the exact claim-bearing episteme and any required source-to-target relation are known, choose the explanation-use class.

**What goes wrong if missed.** A publication form, a rewritten episteme, and a new hypothesis are all called a rendering of one source. Helpful wording then hides a changed claim-bearing object or an unsupported source relation.

**What this buys.** One honest identity branch followed by one bounded explanation-use class: the reader can tell which episteme is being published, how a changed target was obtained, and which stronger use remains blocked.

**Not this pattern when.** For an ordinary human-authored note, if a source locator plus one natural-language bounded/blocked-use sentence already preserves meaning and prevents the credible overread, use that simpler publication note and stop. Also do not use EFP to establish rewrite, representation change, coarsening, comparison, retargeting, hypothesis production, evidence, work, assurance, or gate claims; apply their exact patterns first.

**First output.** One compact explanation-use note naming the exact source or related target episteme, explanation class, source reference, bounded explanation-reader use, blocked downstream use, and reopen or boundary condition. The note names a source-to-target relation only when the text expresses a different target ClaimGraph. MVPK face, pins, provenance, and other source fields are inherited by reference unless ambiguity or a load-bearing use makes them relevant.

**Ordinary-output claim inventory.** After `ExplanationFaithfulnessProfile`, the author has claimed only that a publication form or representation of this already identified episteme has this explanation class and bounded use. EFP has not constituted an episteme, made a source-to-target relation obtain, or established model truth, evidence, assurance, safe reliance, gate passage, work occurrence, release reliance, or source replacement.

**Working explanation move.** Perform the ontic first screen, identify the exact episteme expressed by the text and any already obtaining source-to-target relation, then classify the publication form's explanation use and state its bounded reader use. If the identity or relation cannot be established, do not repair that gap with an explanation class; return to C.2.1 and the exact rewrite, coarsening, representation, hypothesis, comparison, evidence, work, assurance, or gate pattern.
**Lower-burden ordinary branch.** First try a source locator plus one sentence naming the allowed reader help and blocked stronger use. If that resolves an ordinary human-authored case, do not instantiate EFP. When class ambiguity still changes the next action, use the compact EFP result and no fuller field block.

**Load-bearing use.** Open the fuller explanation review only when the rendering will guide work or reliance, be externally relied on, be disputed, cross context, affect person or team status, or be cited as evidence, approval, engineering justification, gate, or release reliance.

**Stop condition.** Stop before EFP when the simpler source-linked boundary sentence performs the task. After EFP is triggered, stop when the class, bounded/blocked use, and reopen condition settle the next action; add no field or check that does not change it.

**Bounded explanation-use examples.**

| Bounded explanation use | Source-finding check with no downstream claim or effect | Blocked explanation use |
| --- | --- | --- |
| A `SourcePinnedExplanation` or `SourceLinkedExplanationReconstruction` helps navigation, bounded restatement, or source inspection with pins and trace visible. | A didactic explanation helps onboarding or source-finding, while any operative claim returns to the exact source or target episteme and its obtaining source-to-target relation; an `A.10` evidence path opens only when the receiving use actually needs evidence. | A fluent explanation is used as assurance, evidence, approval, gate passage, release permission, or work-occurrence evidence. |

**Neighboring patterns and project records.** `E.17.ID.CR` supplies the bounded-comparison discipline for a comparative review unit; `A.6.3.CR` and `A.6.3.RT` define same-entity rewrite and representation change; `A.6.3.CSC` defines the narrower-use result, blocked downstream use, and source-bearing reopen needed after deliberate coarsening; `A.6.4` and `OntologicalReframing` address a changed EntityOfConcern; `A.15` and `A.15.4` define downstream work or reliance; `B.3` supplies assurance and engineering-justification tests; and `A.20` or `A.21` define gate-bearing claims and effects. For permission-looking or policy-bearing prose, use `A.2.8.PER` for strong grants, exercises, weak non-prohibition/non-violation findings, and permission conflicts; use `A.2.8` for obligation, recommendation-as-duty, and prohibition commitments; and use `A.2.9` for the communicative Work that institutes or revokes an effect.

**Common wrong escalations and boundary transfers.** Do not use this profile to hide new claims, bridge-comparison load, action-selection pressure, or gate-bearing guidance inside helpful prose. If the rendering is really a bounded comparison, apply `E.17.ID.CR`; if it is only same-entity rewriting or representation shift, apply `A.6.3.CR` or `A.6.3.RT`; if a deliberately coarsened rendering's narrower bounded claim or effect, blocked downstream use, and source-bearing reopen are the actual problem, apply `A.6.3.CSC`; if it is already making world, work or reliance, assurance, or gate-bearing claims, leave `E.17.EFP` for the more exact downstream FPF pattern or project-side record.

**Generated-explanation repaired case.** For a generated text, first compare its expressed claims with the exact source ClaimGraph. Unchanged claims permit a form or representation of the source edition; changed claims require an exact target episteme and obtaining A.6.3 or other source-to-target relation before EFP classification. Missing identity or relation yields only an unclassified text and a prospective repair request. After identity is settled, use beyond reader help additionally requires an `A.10` path for each operative claim and, for any assurance, gate, work, permission, approval, or release claim, its applicable pattern and exact project record when one is required; missing evidence keeps the classified form at reader help or source-finding.

**Common wrong first interpretation.** A fluent, confident, source-linked, or reliable-looking explanation is treated as evidence. First honest entry: identify the exact episteme expressed by the text and any required source-to-target relation, then classify its publication form for reader help or source-finding; only an operative claim with an A.10 evidence path or another source relation that carries, supports, or exposes the source basis for the operative claim can carry downstream reliance.

Negative result: if a generated explanation says "reliable" but no operative claim maps to a source relation, the E.17.EFP result is source-finding only or reader help only. If an attempted downstream reliance is still raised, the receiving `A.10`, `B.3`, `A.21`, or other relation named by value can return evidence-needed or no-bounded-current-use for that attempted reliance. It is not weak evidence by style, confidence, fluency, or citation-like wording.

**Generated-retelling survival.** A generated text that expresses the same source ClaimGraph may preserve an inspectable reader-help use, source-finding cue, and quoted source pins as a form or representation of that source edition. If it compresses, omits, strengthens, or otherwise changes claim content, identify a different target episteme and the obtaining A.6.3 or other source-to-target relation before classifying its publication form. It does not preserve source identity, evidence, assurance, gate passage, decision status, permission, or work authority by fluency or links.

**Derivative text and adaptation source-link rule.** A fork, adaptation, abridged guide, translation, generated explanation, tutorial, or access-format conversion first undergoes the same ClaimGraph test. Same claims permit a form or representation of the source edition; changed claims require an exact target episteme and an obtaining `A.6.3.CR`, `A.6.3.CSC`, or other direct relation. EFP then qualifies explanation use only if needed. If the result will guide work or reliance, `A.10` maps each operative claim to its exact source basis; a missing map permits only reader help, a source-gap note, or prospective evidence work.

**Published-form and episteme identity over revision and regeneration.** A revised or regenerated text is not reidentified by source face, prompt, template, carrier, or title. Compare its expressed ClaimGraph first: unchanged claims may identify another form or representation of the same episteme edition; changed claims identify another target episteme under C.2.1 and require the exact source-to-target relation. When use beyond ordinary reader help depends on how the text was produced, identify the exact generation or production relation and the source references it actually used; neither relation changes episteme identity by itself. EFP records only the bounded explanation use of the resulting published form.

**Pattern basis.** E.17 supplies face discipline; E.17.0 supplies viewpoint/view conformance only when `U.View` membership is material.
**Builds on.** `E.17.0 U.MultiViewDescribing`; `E.17` MVPK; `A.7`; `E.10.D2`; `A.6.B`; `F.9`; `F.18`.
**Coordinates with.** `ConservativeRetextualization`; `RepresentationSchemeTransition`; `E.17.ID.CR ComparativeReviewUnit`; `A.6.4`; `A.10`; `A.15`; `A.15.4`; `B.3`; `A.20`; `A.21`; `A.2.8`; `A.2.8.PER`; `A.2.9`.

### E.17.EFP:1 - Problem frame

The exact source ClaimGraph may need more than one publication form or representation. Explanation work may also produce a different target ClaimGraph, but that target is another episteme and must not be hidden inside the word `rendering`. Recurrent cases include:

- a manager-readable form of the same technical ClaimGraph;
- connective explanation that remains entailed by the source, or else belongs to an exactly related target episteme;
- didactic use of a same-ClaimGraph form or of a separately identified target with an obtaining rewrite or coarsening relation;
- exploratory use of a publication form of a separately constituted hypothesis episteme.
FPF already has C.2.1 for episteme identity, A.6.3 and neighboring patterns for source-to-target relations, `E.17.0` for viewpoints and views, `E.17` for publication faces, and E.24.PUB for publication occurrence, form, and carrier. EFP supplies only the remaining bounded explanation-use classification of one form of the already identified source or target episteme.

### E.17.EFP:2 - Problem

Without a dedicated profile:
1. a form of the source, a rewritten target episteme, and a new hypothesis blur together;
2. explanation prose starts behaving like a second semantic rule track;
3. publication-side reviewers cannot tell which faces remain bounded-use for a given explanation class;
4. source and evidence details are either demanded for every explanation or omitted when a named claim, dispute, derivative, or reliance actually needs them;
5. an EFP class quietly substitutes for C.2.1 identity, an obtaining source-to-target relation, bridge work, or a gate decision.

### E.17.EFP:3 - Forces

- **Clarity vs semantic restraint.** Explanation can help readers, but it does not mint new semantic commitments on publication faces.
- **Face discipline vs reader fit.** The same episteme can need different forms, while changed claims identify another episteme even when reader fit motivated the change.
- **Traceability vs accessibility.** Simpler renderings are useful only if readers can still recover how they relate to the source.
- **Didactic usefulness vs policy misuse.** A didactic or speculative retelling can help humans, but it does not masquerade as assurance or gate-bearing content.
- **Explanation vs interpretation.** Some moves still belong to explanation rendering; other uses require interpretation, retargeting, or the FPF rule or project record that actually defines the world-side or gate claim.

### E.17.EFP:4 - Solution — review profile for explanation renderings on existing MVPK faces

#### E.17.EFP:4.1 - Informal definition

> `ExplanationFaithfulnessProfile` is a review profile for the explanation use of publication forms or representations of exact claim-bearing epistemes on existing MVPK faces. E.17 supplies face discipline; E.17.0 supplies viewpoint/view conformance only when `U.View` membership is material.
>
> It does not create a new face family, episteme, or source relation. C.2.1 first identifies the exact episteme expressed by the text; E.24.PUB or A.6.3.RT identifies its form or representation; and, when the ClaimGraph changes, the applicable source-to-target pattern defines the relation and its obtaining test. EFP then states the bounded explanation use of that already identified object.

#### E.17.EFP:4.1.a - Profile, episteme, and published-form distinction

`ExplanationFaithfulnessProfile` is a **review profile**. Its cases concern passive publication forms or representations of an exact `U.Episteme`; the profile itself does not act, decide, publish, constitute an episteme, or make a source-to-target relation obtain.

The distinction is executable: same source ClaimGraph means a form or representation of that source edition; changed claim content means another target episteme under C.2.1 plus an exact source-to-target relation shown to obtain under its applicable test. An EFP class applies only after that branch and cannot legalize a hidden claim change.

#### E.17.EFP:4.1.b - How to read this profile

This profile does not decide whether a claim is true or which claim-bearing object exists. It starts after C.2.1 identity and any required source-to-target relation are recoverable, then qualifies the explanation use of one publication form or representation.

- `Faithfulness` names the review question for that explanation use, not a pass verdict or an episteme-identity rule.
- Class names are bounded-use labels for a form or representation, not merit labels and not source-to-target relations.
- Use E.17 for face discipline and E.24.PUB for publication occurrence and form.
- A changed ClaimGraph identifies another episteme even when the prose remains explanatory, didactic, reconstructive, or speculative.
- A causal or counterfactual addition requires a separate hypothesis episteme under B.5.2 before any publication form can receive an EFP use label.

#### E.17.EFP:4.1.c - Local working vocabulary

This profile uses a small local vocabulary for review.

- **Source episteme and publication occurrence** = the exact source `U.Episteme` edition and, when material, the exact E.24.PUB `EpistemePublicationRelation` occurrence through which it is available. Neither is an MVPK face, form, carrier, or arbitrary physical item.
- **Current claim-bearing episteme** = the source edition when the text expresses the same ClaimGraph, or an exact target episteme when claim content changed and an obtaining source-to-target relation has been established under its direct pattern.
- **Published explanation form** = one publication form or representation of that current claim-bearing episteme on one existing face.
- **Class assignment** = the explanation-use class assigned to that published form on that face.
- **Bundle-local class difference** = a case where two forms in one bundle carry different bounded explanation uses.

These are review aids, not new kinds or relation types. EFP neither creates the current episteme nor substitutes for C.2.1, E.24.PUB, A.6.3, B.5.2, or another direct source-to-target pattern.

#### E.17.EFP:4.2 - Core profile fields

The ontic first screen is performed once, not copied into a metadata record for every note. Most published forms whose identity branch is already recoverable need only the compact explanation-use note:

| Core field | Question |
| --- | --- |
| `explanationClass` | Which local profile value is assigned to this one rendering? |
| source reference | Which exact episteme's ClaimGraph does the text express: the source edition itself or an exact target already connected by an obtaining source-to-target relation? Which source locator is sufficient to reopen that decision, and which E.24.PUB occurrence matters only when availability is load-bearing? |
| bounded explanation-reader use | What can the explanation reader do with this explanation now: understand, navigate, inspect, teach, or prepare review? |
| blocked downstream use | What wider claim or effect is not carried by the explanation? |
| reopen or boundary condition | What source change, dispute, use escalation, missing source relation, or neighboring-pattern boundary condition ends this profile use? |

The fuller field vocabulary below opens only when ambiguity or load-bearing use is present: different classes across faces, source linkage dispute, connective reconstruction, reader-fit dispute, interaction or statefulness, derivative rendering, cross-context reuse, cited reliance, work or reliance, evidence, gate, engineering justification, bridge, or coarsening boundary.

- `faceRuleRef = E.17` and `viewpointConformanceRuleRef = E.17.0`;
- `sourcePublicationOrRecordForm`;
- `targetPublicationOrRecordForm`;
- `changeTargetRef`;
- `entityOfConcernPolicy = preserve` for explanation renderings over the same underlying source `U.Episteme` edition;
- `boundedContextPolicy`;
- `viewpointPolicy`;
- `referenceSchemePolicy`;
- `representationSchemePolicy`;
- `groundingPolicy`;
- `referencePlanePolicy`;
- `claimPolicy`;
- `claimScopePolicy`;
- `publicationScopePolicy`;
- `reliabilityTransportPolicy`;
- `pinningPolicy`;
- `provenancePolicy`;
- `lossProfile`;
- `claimContinuityClass`;
- `microtheoryContinuityClass`;
- `onticContinuityClass`;
- `bridgeRequirement`;
- `worldContactPolicy`;
- `evidencePolicy`;
- `gatePolicy`;
- `workCrossing`;
- `sourceRelationRuleRef?`, `upstreamAuthoritySourceRef?`, `downstreamUseRuleRef?`, and `downstreamAuthoritySourceRef?`;
- `boundedFaces`;
- `publication-face kind value` when `publication face/form` or `interop publication form` discipline is present;
- `publicNamePolicy`;
- `explanationSourceRelationClass` using the shared `E.17:5.1b` vocabulary when source pointer, source availability or retrieval, source use, source faithfulness, claim-source relation, contradiction, omission, claim widening, added linkage, independent verification, bounded use, forbidden downstream use, or reopen trigger could diverge;
- no generic source-relation field; source relation is recorded through `explanationSourceRelationClass`;
- `augmentationRelation`;
- `addedLinkPolicy` when a non-obvious `SourceLinkedExplanationReconstruction` connective points to an actual derivation from the source claims or to an exact relation occurrence that those source claims already report and whose obtaining is independently established;
- `targetUserModel?` when reader-fit materially shapes the rendering;
- `interactionMode?` when the explanation is more than one static explanatory paragraph;
- `contrastiveQuestion?` when the rendering is answering a specific user-facing contrast or why-question;
- `boundedReaderUse?` when downstream use is bounded by intended reader and task;
- `overreadRisk?` when overinterpretation pressure is part of the review load;
- `evidenceRelation?` only when a named operative claim or receiving reliance actually consumes an A.10 evidence/provenance path;
- `noNewBoundaryClaims = true` on explanation faces;
- `compositionRule`;
- `reopenCondition`.

These fields inherit the `E.17:5.1e` local-field rule. They classify one explanation-facing rendering for review; they do not create `U.Kind`, `publication-face kind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, authority reference, publication face, or project-side FPF kind and reference named by value unless another FPF pattern explicitly defines or instantiates that object. The `explanationClass` value is a local source-relation and bounded-use profile value, not `ExplanationKind`, not `U.Kind`, not `EvidenceKind`, not `FaceKind`, and not a truth certificate.

When claim content changes, pause EFP until the practitioner uses C.2.1 to identify the target episteme and the applicable source-to-target pattern to identify and test the relation. EFP may then qualify a publication form of that target only when explanation use remains a distinct question; it never substitutes for that relation or its obtaining test.

#### E.17.EFP:4.2.a - Working-model first

Ordinary published forms do not restate every field or replay the ontic decision. When their exact claim-bearing episteme, MVPK face, any material E.24.PUB occurrence, and already published source references make the branch recoverable, the compact note inherits those conditions by reference.

A source-bearing review record becomes necessary when:
- explanation class differs across faces in the same publication bundle;
- the rendering relies on bounded connective prose that is not obvious from the source wording alone;
- didactic or speculative wording creates a real risk of policy, assurance, or gate misuse;
- source linkage, provenance, or reliability transport would otherwise become unclear;
- the rendering is a fork, adaptation, translation, generated explanation, tutorial, access-format conversion, or another derivative publication that can be mistaken for the source publication, source relation, or source episteme itself.

When one rendering needs its own narrower bounded claim or effect line, blocked downstream claim or effect line, or source-bearing reopen rule because distinctions were deliberately coarsened for reader fit, the issue is no longer only explanation class. Do not keep that case here as if it were merely one more helpful rendering style; apply `A.6.3.CSC Controlled Semantic Coarsening`.

#### E.17.EFP:4.2.b - What a publication-side reviewer checks first

A publication-side reviewer starts with five questions:

1. Does the text express the exact source ClaimGraph, or a different target ClaimGraph?
2. If it differs, which exact target episteme does the text express, and which obtaining source-to-target relation connects it to the source?
3. Which E.24.PUB form or A.6.3.RT representation expresses that exact episteme?
4. Which explanation-use class is claimed for that form, and what reader action changes because of it?
5. Has the form begun carrying another unsupported claim, relation, reliance, or deliberately coarsened use that must return to its direct pattern?
Questions 1–3 are prerequisites: if the exact episteme, form, or required source-to-target relation is unavailable, leave EFP and repair that object or relation under its direct pattern. If they are recoverable and the class distinction changes the next action, the compact note is complete. Open a fuller face-by-face record only when one of the ambiguity or load-bearing triggers in section 4.2 consumes additional fields.

#### E.17.EFP:4.2.c - Interpretant-side block

This profile classifies explanation use on existing faces; it does not describe full interactive explanation systems.

When reader fit materially changes the explanation class, bounded use, blocked use, or reopen condition, make only the distinction needed for that change. A familiar audience and static note may need no separate reader-model field. A contrastive or interactive case may need one or more of `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedReaderUse`, or `overreadRisk`.

These names are optional prompts, not a five-field publication block. They create no source relation, permission, evidence relation, or authority; they only expose the reader-fit difference that changes the present use.

#### E.17.EFP:4.3 - Explanation class set

The explanation-class set used in this profile is:

- `SourcePinnedExplanation`
- `SourceLinkedExplanationReconstruction`
- `DidacticRetelling`
- `SpeculativeRetelling`

In field form, the local assignment is `explanationClass = SourcePinnedExplanation | SourceLinkedExplanationReconstruction | DidacticRetelling | SpeculativeRetelling`.

Class assignment follows, and never replaces, the ontic first screen.

- `SourcePinnedExplanation` qualifies a form or representation that expresses the source edition's same ClaimGraph.
- `SourceLinkedExplanationReconstruction` qualifies a non-obvious connective only when it remains in the same source ClaimGraph because a stated derivation from exact source claims recovers it, or because the source ClaimGraph already reports an exact relation occurrence whose obtaining is independently established under its defining pattern. An independently true relation that the source does not claim belongs to another target ClaimGraph.
- `DidacticRetelling` qualifies teaching or onboarding use. It may qualify a form of the source when claim content is unchanged, or a form of an exact target connected under `A.6.3.CR`, `A.6.3.CSC`, or another applicable source-to-target pattern when pedagogy changed the ClaimGraph.
- `SpeculativeRetelling` qualifies only the bounded exploratory use of a form of a separately constituted hypothesis episteme, normally produced under `B.5.2`. It is not a speculative form of the original source ClaimGraph.

These values are not `U.Kind` values, MVPK faces, semantic merit grades, source-to-target relations, or episteme identities. They state how the published form may be used after those objects and relations have been recovered.

Class assignment is per published form on a face, not one blanket label for a whole multi-face bundle. If a `PlainView` form stays source-pinned while a `TechCard` form expresses a separately related target episteme, the bundle names both exact epistemes and the class difference.

#### E.17.EFP:4.3.a - Ordinary class-selection guidance

A practical order is:

1. compare the text's claim content with the exact source ClaimGraph;
2. if it differs, constitute the exact target episteme and recover the obtaining source-to-target relation under its direct pattern;
3. identify the publication form or representation of the resulting exact episteme;
4. assign an EFP class only if a bounded explanation-use distinction still changes the reader's next action.

Then use `SourcePinnedExplanation` for same-ClaimGraph source explanation; `SourceLinkedExplanationReconstruction` for an already justified connective explanation; `DidacticRetelling` for bounded teaching use of the identified source or target; and `SpeculativeRetelling` only for a separately constituted hypothesis episteme. If the target identity or relation is missing, downgrade or stop rather than making the rendering sound more respectable through a class label.

Do not keep one narrower-use target with declared source-loss mode inside explanation merely because the prose is reader-friendly. When its narrower bounded claim or effect, blocked downstream use, and source-bearing return are primary, use `A.6.3.CSC Controlled Semantic Coarsening`; EFP may qualify a later publication form only if explanation use remains a separate live question.

#### E.17.EFP:4.3.b - Entailed connective and `addedLinkPolicy`

Harmless connective wording adds no proposition: conjunction markers, pronoun recovery, and sentence order can simply make an already explicit source statement readable. No `addedLinkPolicy` is needed for that case.

`SourceLinkedExplanationReconstruction` applies to a less obvious connective only when one of two bases is recoverable:

1. the exact source claims plus their effective reference scheme make the connective a consequence under a stated derivation; or
2. the exact source claims already report the relation occurrence, and that occurrence independently obtains under its defining pattern.

When that basis is material but not visible in the prose, a compact `addedLinkPolicy` points to it:

- `addedLinkKind` — the connective being exposed;
- `sourceReferenceSet` — the exact source claims used;
- `effectiveSchemeOrRuleRefs` — the designation, interpretation, ordering, or inference rules used by the derivation;
- `derivationOrRelationRef` — the inspectable derivation or the exact relation occurrence already reported by the source claims and independently shown to obtain;
- `claimContentResult = source-recoverable` — confirmation that the connective introduces no unsupported target claim;
- `reopenTrigger` — a source, scheme, rule, context, or relation change that invalidates the basis.

The policy is an index to the basis, not evidence that the basis exists. `boundednessReason`, a forbidden-link note, or author intent may help delimit use, but none substitutes for `derivationOrRelationRef`.

If neither a derivation from the exact source claims nor an exact source-reported relation occurrence that independently obtains can be recovered, the connective is another claim. Constitute its exact target episteme under C.2.1 and apply the direct relation, bridge, comparison, or B.5.2 hypothesis pattern that fits the new claim. If that result is unavailable, remove the connective or leave EFP; a downgrade label cannot make it source-linked.

#### E.17.EFP:4.4 - Working bounded-use matrix

| Class | Claim/source relation | Augmentation boundary | Usually bounded faces | Usually bounded publication-form use | Usually forbidden uses |
|---|---|---|---|---|---|
| `SourcePinnedExplanation` | form or representation of the source edition's same ClaimGraph | no claim-level augmentation | `PlainView`, `TechCard` | source inspection, navigation, or bounded restatement | an assurance, gate, evidence, or work claim not separately established |
| `SourceLinkedExplanationReconstruction` | same source ClaimGraph with a connective recovered by a stated derivation from source claims, or by an exact relation occurrence already reported there and independently shown to obtain | no new relation by class label | `PlainView`, `TechCard` | bounded explanation while the exact derivation or source-reported relation remains recoverable | use for which the source, scheme, derivation, source relation claim, or obtaining basis is unavailable |
| `DidacticRetelling` | form of the source when ClaimGraph is unchanged, otherwise form of an exact target connected under A.6.3 or another applicable pattern | pedagogy does not hide target identity or relation | `PlainView` | didactic or onboarding use | policy, assurance, gate, or source-replacement use |
| `SpeculativeRetelling` | form of a separately constituted B.5.2 hypothesis episteme | causal or counterfactual claim belongs to the hypothesis ClaimGraph | `PlainView` | clearly marked exploratory use | evidence, assurance, gate, release, or policy use |

This matrix assigns no evidence relation. An ordinary EFP result needs no A.10 path. Exact evidence, trace, pin, or provenance details open only when a named claim, dispute, derivative transformation, or receiving reliance consumes them and its applicable pattern or project record requires them.

`ExplanationFaithfulnessProfile` ordinarily stays on `publication face/form`. Any appearance on `interop publication form` remains source-pinned and structure-preserving, and does not smuggle explanation-specific semantics into interop publication. Didactic or speculative restrictions are use-profile restrictions over existing faces, not new face kinds.

Source-pinned explanation on `AssuranceLane`-facing publication is exceptional rather than ordinary. Unless the exact face or source policy permits that use with visible evidence carriers, source pins, and no added semantics, reviewers treat `AssuranceLane`-facing explanation rendering as blocked.

`DidacticRetelling` may carry analogy, scaffolding, or reader orientation without asserting a domain fact. Every domain claim it does express belongs either to the exact source ClaimGraph or to an identified target episteme with an obtaining source-to-target relation. Marking prose non-canonical or trace-free does not erase claim content, create its episteme, or establish that relation. When such analogy or scaffolding sits beside technical content, box or otherwise visibly separate it so readers do not merge it into the technical source; that cue limits likely use but does not establish episteme identity or a source relation.

The compact ordinary result needs only a source locator sufficient to reopen the exact source or target decision. Publish exact claim IDs, pins, trace paths, provenance details, or an A.10 evidence relation only when a named claim, dispute, derivative transformation, or receiving reliance consumes them. A reopenable locator is not automatically an evidence path.

When a reader-fit difference changes the bounded or blocked use, state only the relevant audience, interaction, question, use, or overread distinction. Do not publish or inherit all five reader-model fields for ordinary reader help.

#### E.17.EFP:4.5 - Shared explanation rule set

##### E.17.EFP:4.5.a. Preservation rule
Every published explanation form under this profile expresses one exact episteme edition. It stays a form or representation of the source edition only while it expresses the same ClaimGraph under the same C.2.1 identity; otherwise it expresses an exact target episteme connected by an obtaining source-to-target relation. E.24.PUB publication occurrence remains separate, and the EFP class changes neither identity nor relation.

##### E.17.EFP:4.5.b. Loss and reliability rule
A published form states material omission, reordering, simplification, or connection. When any such move changes claim content, the loss belongs to the exact target episteme and its obtaining source-to-target relation under A.6.3 or another applicable pattern, not to an EFP label. Reliability is never silently widened by more persuasive prose.

When a concrete reader-fit difference is load-bearing, expose only enough of its bounded use or overread risk to prevent the actual didactic or contrastive form from being mistaken for assurance, policy, or gate guidance.

##### E.17.EFP:4.5.c. Downstream-use and boundary rule
This profile stays explanation-facing and episteme-facing. It does not decide bridge stance, retargeting, action selection, executable docking, gate-bearing claims or effects, assurance, engineering justification, or work enactment. If a case starts carrying one bounded comparative review case, rival interpretations, bridge-mediated comparison load, world consequences, work or reliance consequences, gate consequences, assurance, or engineering justification, apply the neighboring FPF pattern, then name the project-side object or record that carries the claim or effect and its FPF kind (`E.17.ID.CR`, `F.9.1`, `B.5.2`, `A.6.4`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`).

Interpretant-side fields do not weaken that boundary rule. They only bound reader use; they do not authorize unsupported downstream guidance.

If a coarsened explanation-like rendering needs a narrower bounded claim or effect, blocked downstream use, and source-bearing reopen to remain honest, apply `A.6.3.CSC Controlled Semantic Coarsening` rather than keeping the case in ordinary explanation-use discipline.

##### E.17.EFP:4.5.d. Composition and reopen rule
Repeated `SourcePinnedExplanation` over forms of the same exact source edition can be idempotent. Any changed ClaimGraph reopens C.2.1 identity and the source-to-target relation before class review. Didactic target forms reopen when their target edition, relation, or use changes; speculative forms reopen when their B.5.2 hypothesis edition, prompt relation, or exploratory use changes.

#### E.17.EFP:4.6 - Hard boundary rules

A rendering reviewed under this profile keeps the following explicit:
- it does **not** create a second face family;
- it does **not** turn faces into a second semantic rule track;
- it does **not** license new A.6.B boundary claims on explanation faces: law claims, use-boundary claims, deontic or commitment claims, and effect or evidence claims;
- it does **not** replace bridge discipline, retargeting discipline, or world or gate boundary discipline;
- it does **not** let `publication face/form` and `interop publication form` collapse into one undifferentiated explanation channel.

If explanation text carries a changed ClaimGraph, stop class review, identify the exact target episteme and make the direct source-to-target relation obtain. Resume EFP only for a publication form of that target when bounded explanation use remains separately material.

### E.17.EFP:5 - Archetypal grounding

#### E.17.EFP:5.1 - Source-pinned explanation across multiple faces
**Source claim slice.** `Claim D-14: Cooling loop CL-2 maintains the required temperature margin during standard load. Evidence pins: T-44, E-17.`

**`PlainView` rendering.** `Cooling loop CL-2 keeps the required temperature margin in standard operation. Source pins: T-44, E-17.`

**`TechCard` rendering.** `D-14 stays source-pinned to T-44 and E-17; this rendering only shortens and reorders the claim.`

This stays within `SourcePinnedExplanation` because the rendering changes readability, not the semantic load.

#### E.17.EFP:5.2 - Genuinely entailed connective

**Source claims under exact thermal scheme `RS_plantThermal`.**

- `D-14: During standard load, CL-2 outlet temperature is at most 65 °C.`
- `D-18: During standard load, inspection criterion IC-7 is satisfied when that same outlet temperature is at most 70 °C.`

**Published reconstruction.** `During standard load, D-14 satisfies the IC-7 upper-bound criterion stated by D-18.`

The connective is recoverable because both claims concern the same outlet and load context, `RS_plantThermal` supplies the Celsius order, and `65 <= 70`. The compact `addedLinkPolicy` points to `{D-14,D-18}`, `RS_plantThermal.order`, and that one-step derivation. It does not merely call the link implied. This form may be `SourceLinkedExplanationReconstruction` while those exact premises and rules remain current.

#### E.17.EFP:5.2.a - Non-entailed link exits the profile

**Source claim.** `D-21: The reserve path remained available during observed overload interval O-7.`

**Proposed connective.** `Therefore the reserve-path design is robust against every short overload.`

No source premise, effective-scheme rule, or already obtaining robustness relation derives the universal design claim. `addedLinkPolicy` cannot repair that absence. To retain the sentence, constitute exact target episteme `E_robustnessClaim` and apply the direct robustness, comparison, bridge, or B.5.2 hypothesis pattern appropriate to the intended claim. Until that relation obtains, remove the sentence or leave EFP; it is not source-linked reconstruction.

#### E.17.EFP:5.2.b - Selected-method explanation with an explicit source relation

**Source slice.** `The method-selection note chooses method M-2 because the material stays below threshold T and resource window W is available. It also says that work plan WP-17 and result measurement RM-4 remain required before and after execution.`

**Published explanation.** `M-2 is selected here for the stated material condition and resource window. Planning still requires WP-17, and result measurement still requires RM-4.`

The selection relation and both limits are explicit in the source, so this is ordinary same-ClaimGraph re-expression; it needs no invented `addedLinkPolicy`. It is not evidence that work occurred, a gate decision, or engineering justification. Selection use still concerns exact `U.Method` M-2; planning concerns `U.WorkPlan` WP-17 under A.15; any claim that work occurred requires a dated `U.Work` under A.15.1. Evidence, engineering-justification, or gate use remains under A.10, B.3, A.20, or A.21 only when actually raised.

#### E.17.EFP:5.2.c - Mixed-face bundle with one entailed connective

**Source claims.** `D-31: The reserve path is configured to remain available for overload intervals no longer than five minutes.` `T-8: Observed interval O-7 lasted two minutes.` Both use exact duration scheme `RS_duration` and concern the same path and interval class.

**`PlainView` form.** `The reserve path is configured for overload intervals up to five minutes. Source: D-31.`

**`TechCard` form.** `O-7 falls within D-31's configured availability window. Sources: D-31, T-8.`

The `PlainView` form is `SourcePinnedExplanation`. The `TechCard` connective is derivable from `2 min <= 5 min` under `RS_duration` and may be `SourceLinkedExplanationReconstruction` with that derivation pointer. The bundle states the class difference; it does not infer availability beyond D-31's exact condition.

#### E.17.EFP:5.3 - Didactic retelling

**Source episteme claim.** `The pressure-control condition is satisfied whenever the reserve valve opens within 80 ms.`

**Didactic publication form.** `For onboarding: in this stated test, opening the reserve valve within 80 ms is enough to satisfy the pressure-control condition. The exact condition and threshold remain in the pinned source edition.`

The form expresses the same source ClaimGraph; `DidacticRetelling` qualifies only its teaching use. If the text instead says that the whole system is safe, that different safety claim requires its own target episteme, an obtaining source-to-target relation, and the applicable safety relation before publication. A didactic label cannot supply them.

#### E.17.EFP:5.4 - Speculative retelling

**Observed-source episteme.** `The pinned source notes record the observed recovery, but they do not explain why the recovery was so rapid.`

That observation may frame an abductive prompt. If `B.5.2` produces exact hypothesis episteme `E_couplingHypothesis` with claim `A temporary coupling effect may have accelerated recovery`, that claim belongs to the new hypothesis ClaimGraph, not to the observed-source edition.

**Speculative publication form of the hypothesis episteme.** `Exploratory hypothesis: a temporary coupling effect may have accelerated recovery. This is the separately identified L0 hypothesis, not a claim of the incident source.`

`SpeculativeRetelling` qualifies only this form's exploratory explanation use. It neither constitutes `E_couplingHypothesis` nor turns the form into a passive rendering of the observed source.

#### E.17.EFP:5.4.a - Anti-example: explanation that quietly becomes a new claim

**Source episteme claim.** `The reserve path remained available during the observed short overload interval.`

**Overreaching text.** `The reserve-path design is robust against short overloads.`

The second sentence has a different ClaimGraph. To retain it, constitute an exact target episteme under C.2.1, identify an obtaining source-to-target relation, and establish the wider design-robustness claim under its applicable pattern. Until that relation obtains and the wider claim is established, the sentence is unsupported and receives no EFP class; reopening the source or calling the text face-local does not make the claim part of the source edition.

#### E.17.EFP:5.4.b - Anti-example: reader help that quietly becomes policy-bearing use
**Source slice.** `The onboarding note explains, in simplified prose, that the reserve valve usually opens quickly enough to keep the local pressure condition inside the tolerated window.`

**Overreaching rendering on an `AssuranceLane`-facing use.** `This explanation is sufficient assurance that short overloads stay inside the tolerated window.`

This assurance sentence has a different ClaimGraph. It requires an exact target episteme under C.2.1 and the applicable A.10/B.3 relations; until those obtain it is unsupported and receives no EFP class. The earlier onboarding form may retain its bounded didactic use, but that class neither carries nor weakens the assurance claim.

#### E.17.EFP:5.4.c - Boundary to lighter explanatory note with source-bearing return
**Source slice.** `The technical incident note says the reserve path remained available during the measured load band, but it also keeps one unresolved ambiguity about recovery latency.`

**Lighter explanatory rendering.** `In plain terms: the reserve path stayed available during overload recovery.`

This does **not** remain ordinary explanation profiling. The lighter text expresses a coarsened ClaimGraph, so it must be identified as an exact target episteme under C.2.1 and related to the source through `A.6.3.CSC`; only a later publication form of that target can receive an EFP class if explanation use remains material.

#### E.17.EFP:5.5 - Class-specific reopen cues in the worked slices
- **`SourcePinnedExplanation`** reopens when the pinned source claim set, source pins, or face-use assumptions change so that the rendering can no longer remain omission-only and visibly source-bound.
- **`SourceLinkedExplanationReconstruction`** reopens when any source premise, effective-scheme rule, derivation, context identity, source claim about the exact relation occurrence, or that occurrence's obtaining basis changes or disappears.
- **`DidacticRetelling`** reopens when the exact source or target edition connected under A.6.3 changes, or when teaching use starts functioning as policy-bearing, design-bearing, or gate-bearing guidance.
- **`SpeculativeRetelling`** reopens when its exact B.5.2 hypothesis edition, prompt link, or exploratory use changes; it never falls back to being a passive form of the observation source.

#### E.17.EFP:5.6 - Boundary to interpretation and world or gate use

If a text carries a new hypothesis or another changed claim, first constitute its exact target episteme and apply `B.5.2`, A.6.3, or the other direct source-to-target pattern. Comparative review, rival interpretation, bridge, world, gate, assurance, and engineering-justification uses likewise leave to their exact patterns; EFP can only qualify a later published form's explanation use.

#### E.17.EFP:5.7 - Human-authored and generated task replay against the simpler alternative

This is a qualitative task replay for local architecture choice, not an empirical performance study. Each case compares EFP with the least-cost source-linked note on comprehension, semantic preservation, author/check time, and prevention of overread.

| Task and credible simpler alternative | Comprehension | Semantic preservation | Author/check time | Overread prevention | Non-dominated result |
|---|---|---|---|---|---|
| **Human-authored shift note.** An engineer writes two sentences that repeat inspection note N-14 without changing its claims. Simpler alternative: `Reader orientation; source N-14; not an operating procedure.` | The simple sentence is as easy to understand as an EFP class note. | The source locator and unchanged wording preserve the needed tether. | The simple note is shorter to write and check. | `not an operating procedure` blocks the only credible overread. | The simpler note dominates. Do not apply EFP; use the source/publication pattern and stop. |
| **Generated incident explanation.** A generated paragraph restates one observed recovery and adds `therefore the design is robust`. Simpler alternative: attach a source link and label the paragraph `AI summary`. | Both versions are readable. | The simple label misses the widened robustness claim; EFP's ClaimGraph screen detects another target claim and prevents source identity from being inherited. | EFP adds one focused claim comparison; no full metadata block is needed. | EFP blocks reliance on the widened claim until its target episteme and source-to-target relation exist. | EFP is non-dominated when the generated text will be reviewed, reused, disputed, or relied on. Keep the identity screen, class only after identity, bounded/blocked use, and reopen; add trace or evidence only for the named reliance. |

The human-authored case is the ordinary non-use boundary. The generated case is the source-grounded branch supported by XAI/NLP/generated-explanation literature. A human-authored case may still use EFP when a real source-pinned/reconstructive/didactic/speculative ambiguity changes the next action, but authorship alone never triggers the profile.

### E.17.EFP:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**. Scope: **Conditional** where explanation-class ambiguity changes use. External source grounding is limited to generated, model-facing, retrieval-facing, or interactive explanation; ordinary human-authored use remains a local design branch with a simpler-note non-use default.

The profile biases toward source restraint and against overread. Its counter-bias is the E.17.EFP:5.7 task replay: do not apply the profile when a shorter source-linked boundary sentence performs the human task equally well.

### E.17.EFP:7 - Conformance Checklist

These checks apply only after EFP's use condition survives the simpler-note comparison. Retain a check only if it changes the next bounded use, blocks a concrete overclaim, or preserves the source or reopen condition needed for that action.

Use core ordinary checks first. Conditional rows open only when reader-fit, bundle-local class difference, bounded explanation class, connective reconstruction, derivative rendering, or downstream reliance use is present.

#### E.17.EFP:7.1 - EFP-Core ordinary checks

0. **CC-EF-0 — Exact episteme and ClaimGraph branch are recoverable.**
   The text is identified as a form or representation of the same source ClaimGraph, or as a form of an exact target episteme connected by an obtaining source-to-target relation. A speculative causal or counterfactual claim is a separate B.5.2 hypothesis episteme.
1. **CC-EF-1 — Explanation class follows identity.**
   The class is explicitly named for the publication form after CC-EF-0; it is not used as episteme identity or source-to-target evidence.
2. **CC-EF-3 — Source reference and blocked downstream use are explicit.**
   The compact note states source reference, bounded explanation-reader use, blocked downstream use, and reopen or boundary condition.
4. **CC-EF-5 — No new A.6.B boundary claims on explanation faces.**
   The no-new-boundary-claims rule is explicit on explanation faces; the blocked claims are law claims tested under A.6.B, use-boundary claims, deontic or commitment claims, and effect or evidence claims.
5. **CC-EF-7 — No second face family.**
   A publication-side reviewer can tell why the case remains explanation-facing rather than becoming a second semantic rule track.

#### E.17.EFP:7.2 - EFP-Conditional checks

1. **CC-EF-4 — Interpretant-side block is explicit when reader-fit does real work.**
   Only the reader-fit distinctions that change the current class, bounded use, blocked use, or reopen condition are stated. The five optional prompts are not a required block.
2. **CC-EF-2 — Face and `publication-face kind` boundary is explicit when present.**
   State face, pinning, provenance, or reliability details only when the present form choice, dispute, derivative, or receiving use makes that boundary material and it is not already recoverable by source reference.
3. **CC-EF-6 — Boundary to interpretation, retargeting, coarsening, and world or gate use is explicit.**
   The boundary is explicit, including `A.6.3.CSC Controlled Semantic Coarsening` when a narrower bounded claim or effect, blocked downstream claim or effect, or source-bearing reopen condition becomes primary.
4. **CC-EF-8 — Bundle-local class differences are explicit.**
   When one publication bundle carries different explanation classes across faces, that difference is stated explicitly rather than hidden under one bundle-wide label.
5. **CC-EF-9 — Source-loss or changed-claim cases retain exact identity and use boundaries.**
   A didactic target names its exact A.6.3 or other relation; a speculative form names its exact B.5.2 hypothesis episteme. Any material source loss or reliability downgrade states its bounded and forbidden uses without pretending that the EFP class supplies identity or relation evidence.
6. **CC-EF-10 — Reopen triggers match the class.**
   The published review note makes class-relevant reopen triggers visible when source claim set, pins, provenance, or face-use assumptions change.
7. **CC-EF-11 — Every non-obvious source-linked connective has an actual basis.**
   The exact source claims and effective scheme yield a stated derivation, or those source claims already report an exact relation occurrence whose obtaining is independently established. `addedLinkPolicy` points to that basis; without it, the added claim becomes an exact target episteme under its direct pattern or exits EFP.
8. **CC-EF-12 — Derivative renderings keep source links operative.**
   A fork, adaptation, translation, generated explanation, tutorial, access-format conversion, or other derivative rendering that will guide work or reliance maps each operative claim to the exact source passage, carrier path, or project record that evidences it and names that record's FPF kind when material, or else downgrades to reader help or applies `A.6.3.CSC` as appropriate.
9. **CC-EF-13 — Generated explanation reliance boundary is explicit.**
   A generated explanation used beyond ordinary reader help states its explanation class, source-finding state, operative claims, the FPF pattern used to test each relied-on claim, the exact project record that carries it, and blocked downstream use. The explanation itself is not evidence, assurance, approval, gate passage, release reliance, or work authority.

### E.17.EFP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
|---|---|---|
| Treating every explanatory prose block as equally faithful | rendering, reconstruction, didactic work, and speculation have different review loads | first try the simpler source-linked note; when class ambiguity changes the next action, name only the applicable class, bounded/blocked use, and reopen condition |
| Letting reader-fit stay implicit when explanation is clearly tailored | a didactic or contrastive rendering can be overinterpreted as general or policy-bearing guidance | state only the audience, interaction, question, use, or overread distinction that changes the present class or boundary; do not publish a five-field block by default |
| Using an EFP class as a second claim or relation track | changed claims hide behind reader-friendly prose | compare ClaimGraphs first; identify the target episteme and direct source-to-target relation before classifying its publication form |
| Calling a connective source-linked because `addedLinkPolicy` names it | a policy declaration is mistaken for derivation or an obtaining relation | require exact source premises and effective scheme plus a derivation, or an exact relation claim already in the source plus an independently obtaining occurrence; otherwise constitute a target claim or leave EFP |
| Treating speculative prose as a source rendering | a new causal or counterfactual claim is hidden inside a form label | constitute the separate B.5.2 hypothesis episteme, then restrict only its publication form's use |
| Collapsing MVPK face and `publication face/form` or `interop publication form` discipline | explanation appears to create a new publication family | stay on existing MVPK faces and keep named `publication face/form` or `interop publication form` and carrier policy explicit |
| Derivative text as source replacement | a changed ClaimGraph is treated as the original source because the text is easier to read | identify same-source form versus exact target episteme and make its A.6.3 or other direct relation obtain before EFP classification |
| Explanation as evidence or assurance | a fluent or source-linked explanation is cited as proof, approval, gate passage, release reliance, work authority, or assurance | identify the exact episteme and any required source-to-target relation before classifying its publication form; open `A.10`, `B.3`, `A.21`, `A.15`, or another direct record only for the exact operative claim and receiving use that need it |

### E.17.EFP:9 - Consequences

- Explanation classes become explicit and reviewable.
- Existing MVPK face discipline stays intact.
- The ordinary result stays compact; exact pins, provenance, trace, reader-model, and evidence details appear only for the concrete use that consumes them.
- The boundary to interpretation, retargeting, and world or gate work becomes easier to review.

### E.17.EFP:10 - Rationale

Generated and model-facing explanation can hide source drift; ordinary human explanation can instead be burdened by a profile it does not need. EFP therefore keeps the ontic boundary and bounded-use benefit while making simpler-note non-use the default whenever it is equally effective.

### E.17.EFP:11 - SoTA Alignment and Source-Scope Boundary

**Source-use rule.** A source supports only claims within the problem population and action it actually studies. The external sources below concern AI explanations, NLP/model interpretations, LLM-generated explanations, RAG outputs, or interactive XAI systems. They do not establish a universal architecture for ordinary human-authored engineering notes.

| Claim need | Exact source and actual scope | Local use | Boundary or rejected transfer |
|---|---|---|---|
| Keep claim-bearing episteme, source-to-target relation, publication form, and carrier distinct. | Current FPF `C.2.1`, `A.6.3`, and `E.24.PUB`. | Apply the ClaimGraph identity branch before EFP classification. | This is current internal ontology, not a conclusion imported from an architecture-description standard. |
| Explanations of AI-system results are purpose- and recipient-sensitive and must state knowledge limits. | Phillips et al. (2021), *Four Principles of Explainable Artificial Intelligence*, NISTIR 8312, DOI `10.6028/NIST.IR.8312`; government-guidance lineage. | Adapt bounded reader use and explicit limits when an AI explanation is current. | Do not generalize this XAI guidance into mandatory fields or classes for every technical explanation, and do not present it as the whole current research line. |
| Plausibility and faithfulness of model interpretations are different evaluation questions. | Jacovi & Goldberg (2020), *Towards Faithfully Interpretable NLP Systems*, ACL DOI `10.18653/v1/2020.acl-main.386`; research lineage. | For NLP/model interpretation, do not infer faithfulness from persuasive prose. | The paper studies interpretable NLP systems, not ordinary human engineering exposition; later work further distinguishes self-consistency and intervention-based evaluation. |
| Output-level consistency tests for LLM explanations are not automatically tests of faithfulness to model internals. | Parcalabescu & Frank (2024), *On Measuring Faithfulness or Self-consistency of Natural Language Explanations*, ACL DOI `10.18653/v1/2024.acl-long.329`; later repair of an overclaim in the evaluation line. | Name the actual check as self-consistency when that is what it measures. | Apply only to generated/LLM explanation use; do not require it for human-authored notes. |
| Current LLM-explanation work tests faithfulness through model-behaviour intervention rather than surface plausibility alone. | Chuang et al. (2026), *FaithLM: Towards Faithful Explanations for Large Language Models*, EACL DOI `10.18653/v1/2026.eacl-long.177`; current research line. | Use an intervention-shaped evaluation only when the current task actually asks whether an LLM explanation reflects model decision behaviour. | EFP's source ClaimGraph comparison is not a FaithLM score and does not import model-internal faithfulness into ordinary engineering text. |
| Retrieval quality, answer faithfulness, and answer relevance are distinct RAG evaluation dimensions. | Es et al. (2023), *RAGAS*, arXiv:`2309.15217`; Saad-Falcon et al. (2023), *ARES*, arXiv:`2311.09476`; RAG-evaluation method lineage. | Keep retrieved context, source use, and claim recoverability separate for RAG-generated explanations. | These metrics do not define FPF ontology, do not exhaust current RAG evaluation, and do not apply without a retrieval pipeline. |
| Repeated queries, evolving models/data, responsiveness, and traceability create system-level demands for interactive XAI. | Labarta et al. (2026), *X-SYS: A Reference Architecture for Interactive Explanation Systems*, arXiv:`2602.12748v3`; current emerging preprint. | Use interaction-sensitive prompts only for an actual interactive explanation system. | Do not transfer a five-component XAI system architecture or its fields to a static human-authored note, and do not treat an emerging preprint as settled standard. |
| Decide whether ordinary human-authored engineering explanation needs EFP at all. | No external source in this set establishes EFP's four-class architecture for that population. Local evidence is the two-case task replay in E.17.EFP:5.7. | Prefer a source locator plus one bounded/blocked-use sentence when that performs the task. Use EFP only when class ambiguity changes action. | Present this branch as provisional local design rationale, not current external SoTA. Reopen if exact technical-writing, discourse, or decision-record evidence changes the comparison. |

**Source-grounded branch.** The XAI/NLP/RAG sources justify caution about generated or model-facing explanations: fluency, plausibility, retrieved context, or an `AI summary` label does not establish claim preservation, evidence, or reliance. They support the focused identity and use check only when that population is current.

**Local human-authored branch.** For ordinary human explanation, the architecture is justified only by the concrete local problem and the E.17.EFP:5.7 replay. The default is non-use when a simpler source-linked boundary sentence is equally comprehensible, preserves the claims, costs less, and prevents the same overread.

**Retained result.** Keep only the ClaimGraph identity screen, an explanation class when it changes the next action, the compact bounded/blocked use, and a reopen condition. Add reader-model, trace, provenance, evidence, RAG, self-consistency, or interactive-system details only when their exact source-scoped situation is present.

### E.17.EFP:12 - Relations

- **Builds on:** `E.17.0`, `E.17`, `A.7`, `E.10.D2`, `A.6.B`, `F.9`, `F.18`
- **Coordinates with:** `ConservativeRetextualization`, `RepresentationSchemeTransition`, `A.6.3.CSC Controlled Semantic Coarsening`, `E.17.ID.CR ComparativeReviewUnit`, `A.6.4`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`
- **Profile basis and main neighboring-pattern boundaries:** E.17 supplies face discipline; E.17.0 supplies viewpoint/view conformance only when `U.View` membership is material. A shift toward new semantics, a coarsened narrower-use target, or a gate-bearing claim or effect leaves the profile.
- **Boundary notes:** bounded comparison over a comparative review unit applies `E.17.ID.CR ComparativeReviewUnit`; explanation-like renderings with declared source-loss mode whose narrower bounded claim or effect, blocked downstream claim or effect, and source-bearing reopen are primary apply `A.6.3.CSC Controlled Semantic Coarsening`; retargeting applies `A.6.4`; work and reliance consequences apply `A.15` and `A.15.4`; assurance and engineering-justification consequences apply `B.3`; gate-bearing consequences apply `A.20` or `A.21`.

### E.17.EFP:12a - C.29 mathematical-lens use relation

> When a published explanation form uses a mathematical lens, EFP still classifies and bounds its explanation use. Cite the applicable `C.29` output only for the mathematical-lens claim actually used. When that claim is load-bearing, cite the exact `MathLensUse.LensCandidateNote`, `MathLensUse.OneLine`, `MathLensUse.MiniCard`, or `MathLensUse.FullCard` result required by C.29 and keep recoverable its candidate mathematical object, lens mapping mode, preserved and lost structure, exposed invariant or distinction, `LensUseAdmissibilityValue`, bounded use, blocked downstream use, and stop condition; do not copy fields already recoverable through that exact reference. Add source-relation, evidence, face, or forbidden-use detail only when the receiving use makes it material; the mathematical-lens result does not make the explanation faithful, evidential, or admissible downstream by itself.

### E.17.EFP:End

