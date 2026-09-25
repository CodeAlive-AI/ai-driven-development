## A.6.S - TargetSignature and optional ConstructorSignature - demand-driven signature engineering

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Mixed (normative where RFC 2119 keywords appear; quadrant classification is governed by A.6.B)
> **One-liner:** Start from the actual signature assertion, revision, relation, operation application, or Work. Add a separate ConstructorSignature only when a named receiving use needs reusable constructor vocabulary, laws, and applicability. Keep an operation description, any mathematical arrow, its application, performed Work, and publication faces distinct.

**E.24.UK settlement.** A.6.S admits no `U.SignatureEngineeringPair` kind or durable arrangement individual. The spelling is retired. `TargetSignature` and `ConstructorSignature` are use-specific designations for two independently identified `U.Signature` epistemes; neither designation adds another kind, constitution relation, or identity discriminator. Merely pairing two documents or naming both signatures establishes no relation between them.

**Use this pattern when** a project already has, or genuinely needs, a reusable signature that declares how another signature is to be authored or revised, and at least one named receiving use needs that declaration to remain stable across applications, editions, or publishers.

**Do not use this pattern** merely because one signature is edited, one direct relation is stated, one view is prepared, or one work occurrence changes a carrier. Apply that direct rule and stop. A one-off revision needs no ConstructorSignature.

**First useful move.** Say what changes in ordinary language: for example, `The editor added the refund law to PaymentBoundarySignature and issued edition 4.` Identify the changed signature episteme and, when current, the operation application, System, Work, result, or edition relation. Only then ask whether a later receiver needs a reusable declaration of the constructor operations.

**What goes wrong if missed.** At one extreme, the signature, the operation description, and the Work that changes or publishes it collapse into one “contract/editing” story. At the other, every small edit acquires a second signature, a pair object, two operation lexicons, and a full attribution package.

**What this buys.** The light path stays light. Where repeatable constructor language has real users, the ConstructorSignature can preserve that language while the TargetSignature, operation description, A.6.2 arrow, application, Work, assignment, carrier, and publication view keep their own identities and direct relations.

### A.6.S:0 - PCP-TERM/LEX token guards (local-first)

This pattern reserves the following tokens in Tech (normative) register:

* **TargetSignature** — the engineered signature episteme (and its editions) under construction and stabilisation (**not** the EntityOfConcern, and **not** the target source or cell of an F.9 relation).
* **ConstructorSignature** — the enabling signature that describes constructor operations for TargetSignature evolution (do **not** mint a second Tech token such as `EnablingSignature`).

Rename-guards (common collisions):

* **enabling** — Plain adjective meaning “producing/maintaining the TargetSignature”; it is not a `U.*` token.
* **constructor** — MUST distinguish `ConstructorSignature` (episteme), a constructor-operation description, the A.6.2 arrow used to state its effect-free episteme relation, and the admitted System that applies the described constructor operation and performs any separately admitted construction Work. State any local system-role classification and obtaining assignment separately. If the physics term is intended, spell **Constructor Theory** explicitly.
* **target** — avoid bare “target” in Tech clauses; use `TargetSignature` or qualify the target (for example, “F.9 target cell” or “target holon”).
* **contract** — if source wording uses this Plain shorthand, recover whether it means `TargetSignature`, Contract Bundle, promise content, commitment, or work/evidence. In this pattern the intended recovered value is usually `TargetSignature`; promises, duties, and gates are classified under `A.6.B` and `A.6.C`.

### A.6.S:1 - Problem frame

Boundary descriptions often arrive as “half-signatures”: an n-ary relation in ordinary prose, overloaded markers such as *binding*, *anchoring*, or *contract*, and unstated assumptions about participants, applicability, and publication. Teams then revise the boundary through edits, reviews, and partial publications.

A.6.5, A.6.6, A.6.2-A.6.4, and E.17 already govern several different moves that may occur during that work. The missing discipline is not a universal engineering container. It is a proportional choice:

1. state the actual edit, relation, arrow, application, Work, edition, or view and stop when that answers the use; or
2. when a named receiver needs the same constructor vocabulary and laws again, identify a separate ConstructorSignature and state the exact dependency or use that connects it to the work.

Without that choice, four failures recur:

1. the TargetSignature, constructor-operation description, application, and performed Work are conflated;
2. a one-off revision is inflated into a durable two-signature apparatus;
3. semantic changes hide behind generic edit language instead of identifying the receiving episteme and any actual edition, continuity, or reference change; and
4. publication views acquire claims not present in the described signature.

An episteme does not act. When performed Work is claimed, recover each actual performer `U.System` and the complete A.13 core, then independently admit the dated occurrence under A.15.1, as set out in §4.0. A System may separately apply a described operation. Use F.6 afterward only for a receiving claim that consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and the assignment itself does not act.

### A.6.S:2 - Problem

FPF needs a pattern for **engineering signatures as boundary epistemes**: a disciplined way to construct, revise, and publish a target `U.Signature` from partial input, while maintaining:

* separation between *signature* and *mechanism* (A.6.0 vs A.6.1),
* separation between *laws*, *admissibility*, *deontics*, and *work evidence* (A.6.B),
* explicit multi‑view publication without semantic drift (E.17),
* reproducible evolution across editions without silent mutation.

### A.6.S:3 - Forces

* **Stability vs evolution.** TargetSignatures must be stable enough to coordinate, yet change as understanding improves.
* **Explicitness vs overhead.** Unpacking slots/bases/views increases clarity but also increases authoring effort.
* **Arrow law vs enacted work.** An A.6.2 arrow may state the effect-free relation between source and receiving signature epistemes. An application of the described constructor operation has its own predicate, extent, and identity rule under A.6.1. Claims about a created successor or written carrier identify the changed object and effect; any performed Work is admitted separately. For performed Work, recover each actual performer's complete A.13 core and let A.15.1 independently admit the occurrence, as in §4.0. Add F.6 only when a later claim expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 checks that exact Work-assignment link and identifies neither the assignment nor the performer. Missing or failed F.6 leaves the Work intact.

* **Multi‑view richness vs semantic coherence.** Views help stakeholders, but they risk becoming divergent “versions of truth”.
* **Local meaning vs cross-local reuse.** Signature claim content pins its effective ReferenceScheme where interpretation matters. The local kind and any source-local meaning remain separate values. Use F.9 for an actual semantic Bridge between exact local senses whose `<ReferenceScheme, LocalSenseClaim>` interpretation bases differ, and judge its bounded-use claim separately. Distinct F.17 cells or a mapping alone do not establish that relation.
* **Contract talk vs ontology.** “Contract” language invites mixing promises, norms, and invariants; FPF requires quadrant discipline.


### A.6.S:4 - Solution - start with the direct move; add a ConstructorSignature for named reuse

#### A.6.S:4.0 - Keep the signature, arrow, application, and Work separate

The smallest account names the actual object and move. Describe a signature revision through its source and receiving signature epistemes. A changed C.2.1 discriminator identifies another episteme; an edition or continuity relation requires its own source use, continuation rule, and preserved or deliberately changed features. Republishing unchanged claim content need not identify another episteme. A view, direct relation assertion, operation application, carrier write, and performed Work remain under their own patterns.

A **ConstructorSignature** is optional. When used, it is a `U.Signature` whose reusable declaration content describes a family of constructor operations: its subject and value or result range, vocabulary, laws, and applicability. It does not perform those operations and does not contain the Work that applies them.

If a constructor family also uses an A.6.2 mathematical arrow, identify that arrow separately. The arrow relates exact source and receiving epistemes. Its rule states how their claim content, EntityOfConcern, and effective ReferenceScheme compare. When it reads a neighboring grounding, representation, conformance, edition, or provenance occurrence, name that occurrence and the endpoint facts compared; the arrow neither changes the occurrence nor makes it obtain. A.6.3 and A.6.4 apply only to their exact viewing or EntityOfConcern-retargeting cases.

When dated authoring, deriving, materializing, validating, storing, or publishing Work is claimed, first recover each actual performer as a System under A.1 and its complete A.13 core: the local agential system-role kind and criterion, System classification, obtaining A.2.1 assignment, and the scope, working situation, and window needed by the use, with evidence for those claims. A.15.1 then independently admits the dated occurrence from its performance history, at least one Method actually followed, temporal extent, and at least one obtaining locally declared containing-System relation. Use F.6 afterward only for precise assignment-bound attribution through that same obtaining assignment; missing or failed F.6 leaves the independently admitted Work intact. Additional classifications or assignments, an operation application and its bindings, the resulting episteme, and carrier, evidence, or publication relations enter only when their own claims are current. Add an agency-characteristic profile only when the local criterion, a claimed characteristic, or an assurance use requires it under A.13/A.15.1.

#### A.6.S:4.1 - Decide whether a second signature is needed

Start with the **TargetSignature**: the `U.Signature` being authored, stabilized, or revised. Its A.6.0 declaration content identifies its subject and value or result range and supplies the reusable vocabulary, laws, and applicability that make it a signature. It contains neither operational gates, deontic duties, evidence claims, nor construction Work merely because those topics occur nearby.

Add a **ConstructorSignature** only when a named receiver needs reusable constructor-operation vocabulary, laws, and applicability. The receiver may be a later editioning process, another authoring System, a publication process, or another repeatable use that would otherwise have to reconstruct the same operation declaration. A one-off edit, direct relation assertion, arrow, operation application, or Work occurrence does not qualify by itself.

The two signatures remain separate C.2.1 epistemes. State only the relation that is actually current:

* when one signature cannot interpret a required term or replay a law without the other, use the exact A.6.0 declaration-dependency claim;
* when a System uses a Method or MethodDescription that cites the ConstructorSignature while revising the TargetSignature, state that method/source use and any actual application or Work under its direct pattern;
* when both signatures are merely relevant to the same local question, name them without inventing a pair relation; and
* if a future use needs a durable relation occurrence between them, first supply that relation kind's participant meanings, predicate, applicability, occurrence identity, and E.24/E.24.UK settlement. A.6.S supplies none by default.

`TargetSignature` and `ConstructorSignature` are Tech designations of each signature's place in this use, not local system-role kinds. A publication may explain TargetSignature as “the signature being engineered”; it need not introduce the abbreviation *SoI*. Do not conflate the TargetSignature with its exact C.2.1 EntityOfConcern. Distinct signature editions remain distinct epistemes when their C.2.1 discriminator triples differ; any empirical-grounding, edition, continuity, dependency, source-use, or publication relation remains separately identified.

**Mint-or-reuse note.** A ConstructorSignature is admitted by the ordinary A.6.0 membership rule, not by being named next to a TargetSignature.

#### A.6.S:4.2 - Choose the constructor vocabulary that the receiving use needs

A ConstructorSignature declares only operation families that a named receiver will reuse. It need not contain both A.6.5 slot operations and A.6.6 declaration-change labels, and it need not contain either family when another direct operation declaration is enough.

**Slot operations, when current.** Use A.6.5 when a reusable relation declaration needs stable participant positions, fillers, or references. Its vocabulary distinguishes name binding, first or later by-value filling, reference retargeting, typed substitution, resolution, and parameter passing. Keep `bind` for name binding; do not use generic *edit* to hide a reference retargeting or a referent-internal change. A one-off ordinary edit that needs no reused SlotSpec stays an ordinary edit.

**Assertion or declaration history, when current.** Use A.6.6 first to state the actual dependent, base, and direct relation. Stop when that readable assertion answers the use. If a named receiver needs the history of an optional assertion representation or reusable declaration, its local labels such as `declareBase`, `rebase`, `rescope`, `retime`, or `refreshWitnesses` may describe which represented field changed. They do not establish or change the world-side relation. Producing new evidence is separate Work; changing a witness reference is only a record edit.

**Mathematical arrows, when current.** An operation description may cite an A.6.2, A.6.3, or A.6.4 arrow only when that mathematical relation is useful to the receiver. The ConstructorSignature states the arrow family and the endpoint values or facts it reads or compares. The arrow remains effect-free; an application that produces a receiving episteme and any performed Work remain separate.

**Publication operations, when current.** For E.17 publication, a ConstructorSignature may declare a reusable publication or view-producing operation when its named receiver needs that declaration. Apply A.6.3 only when the operation uses a mathematical source-to-receiving viewing construction; identify those epistemes and the viewing rule. Keep the publication face faithful to its source and apply §4.4 for any separate `U.View` claim. For publishing a face, writing a carrier, committing a file, or issuing a release, distinguish any claimed operation application under A.6.1, any actual changed-object or effect claim, and Work admitted under §4.0. Neither signature performs those actions.

The test is practical: remove the proposed operation family. If the named receiver can still perform or assess its use without reconstructing a shared vocabulary or law, leave that family out.

#### A.6.S:4.3 - Change discipline: Viewing vs Retargeting vs editing

When more than one distinction is current, classify each move separately rather than forcing all four buckets into every revision:

1. **Publication form and conditional viewing.**
   A *presentation* change (views, stakeholder cards, projections) may be an E.17/E.24.PUB form or carrier change. Use A.6.3 only when a mathematical source-to-receiving viewing construction is current, preserving the exact EntityOfConcern; E.17.0 separately governs any `U.View` membership claim.

2. **Direct edits and conditional declaration history.**
   State a one-off vocabulary, law, applicability, or reference change directly. Use A.6.5 only for reusable relation-participant declarations or reference operations that matter to the receiver. Use A.6.6 declaration history only after the actual base-dependence relation is stated and a named receiver needs that history.
3. **Editioning + reference retargeting (A.6.5).**
   Use when the TargetSignature meaningfully changes and downstream coordination needs a new TargetSignature edition. Do not silently mutate the existing episteme: identify the successor edition and retarget the references whose receiving use now selects it (`Retarget<...>` in the relevant Ref slots).


4. **Epistemic retargeting and structural reinterpretation (A.6.4; rarer).**
   Use only when the source and receiving `EntityOfConcernRef` values resolve to different exact EntitiesOfConcern. A reference-only change that still resolves to the same entity stays with its actual reference operation. A.6.4 identifies the source and receiving epistemes and one exact arrow `r`. A separate C.2.1 bounded-use assertion `q` is about that exact `r`; its ClaimGraph contains the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. A separate current-case judgement compares the exact facts with `q` and returns exactly `satisfies`, `fails`, or `cannot decide`; `cannot decide` names the missing fact and reopen condition. This is distinct from an ordinary new edition of the same TargetSignature.

Rule of thumb:

* If only the publication form or carrier changes, use E.17/E.24.PUB and stop; no slot/base declaration is required unless another receiving use needs it.
* If the change is “new TargetSignature edition for consumers”, identify the new edition and explicitly retarget the references whose receiving use now selects it.
* If the change is a different EntityOfConcern, use A.6.4's three-part account: the exact arrow `r`, a separate C.2.1 bounded-use assertion `q`, and a separate current-case judgement. A kind difference alone identifies none of them.

**EFEM discipline.**
When a constructor operation really uses an A.6.2 arrow family, declare its endpoint comparison and `entityOfConcernChangeMode` under A.6.2. An operation description that needs no mathematical arrow introduces none.
**Editioning is orthogonal**: you MAY mint a new edition even under `preserve`; references whose receiving use now selects that edition MUST be retargeted explicitly, with A.6.5 slot discipline where applicable.
For an actual measurement, actuation, validation run, carrier write, or other effect, identify any claimed operation application under A.6.1, changed-object or effect claim under its direct rule, and Work under §4.0 independently. An effect alone establishes neither application nor Work; the A.6.2 arrow performs none of these actions.

#### A.6.S:4.4 - Add publication and claim controls only when they are current

For E.17 publication, choose a faithful publication form for the bounded reader/use and point to the exact source episteme edition. Preserve E.17's no-content-extension rule: informative explanation may expose source meaning without adding boundary commitments. Only when the selected episteme's `U.View` membership is asserted or needed, resolve its exact viewpoint and E.17.0 conformance; add an A.6.3 source-to-receiving construction only when that separate relation is current. The publication occurrence, carrier, viewpoint use, conformance claim, and any publication Work remain separate. When E.17's CC-MVPK-3b boundary claim-set condition applies, keep normative face text traceable to that A.6.B claim set, with informative commentary; a face does not become a second boundary specification. No MVPK package is required merely because a signature changed.

Classify atomic claims under A.6.B, keeping laws, operational admissibility, deontic commitments, and evidence-use claims separate. Correct quadrant classification alone needs no register. Use the applicable claim register when stable identifiers serve reuse, a decision, audit, or cross-face citation; keep a return to the claim's ID or canonical source location for a material dependency. Do not put operational gates, duties, evidence results, or Work into the TargetSignature merely to make one authoring record complete. Without a need for the register, ordinary claim content and the direct patterns are enough.

#### A.6.S:4.5 - Signature-construction relation in a transformation-flow structure (informative)

If a team represents actual signature-construction Work as an E.18 `TransformationFlowStructure`, reference only the A.6.S objects and direct relations that the flow uses; do not convert them into a second graph ontology:

* Declared constructor arrows may appear at transformation-flow loci as independently defined A.6.2 values over signature epistemes. An actual operation application and any performed Work remain separately identified.
* Concrete carrier writes (commits, releases, registry writes, and carrier and source-currentness pinning) may be admitted as Work under §4.0; an E.18 Work locus may bind that already admitted Work. Use F.6 afterward only when the receiving flow account consumes precise attribution through the performer's obtaining A.13 assignment; missing or failed attribution leaves the carrier-write Work intact. Use A.10 for evidence and provenance, E.17 for publication, and the relevant carrier patterns for carriers. The constructor-operation declaration, any identified application that writes a carrier, and the admitted Work remain distinct.
* For validation and admission, E.18 governs any selected gate/check position; each check follows its own subject rule. When an actual gate decision is present, use A.21 and name its exact `GateDecisionResult`, bounded action, applicable `GateProfile` application, complete required `GateCheckApplicationResult` set, decision value, consequence, scope/window, and recheck condition. Use a short `GateCheckRef` only when a selected publication structure needs one, and a `DecisionLog` only when audit or reuse is current.
* When the source and receiving `EntityOfConcernRef` values resolve to different exact EntitiesOfConcern, use A.6.4: identify the exact arrow `r`, separate bounded-use assertion `q`, and any separate current-case judgement, then let E.18 place each only when that transformation-flow use is current. A kind change without that basis supplies no positive claim, and any actual operation application remains separate.

This mapping is optional. A one-off revision needs neither an E.18 flow nor a ConstructorSignature. When a flow is current, use E.18 for its structure and E.18.2 for any mathematical description of that selected structure, including a graph or path description. Use C.29 only for a declared mathematical-lens use. A.6.S identifies the TargetSignature and any independently justified ConstructorSignature and operation declarations.

#### A.6.S:4.6 - State during construction (informative)

Do not mint a new kernel “signature state” unless you need it.
In most cases, use:

* **edition** + explicit continuity/withdrawal links for semantic evolution, and
* a coarse **status** (`Draft`/`Review`/`Stable`/`Deprecated`) for process signalling.

If a project needs a reusable state-change policy, place it in the applicable signature's declared content or in a separately identified policy episteme, according to its actual EntityOfConcern and use. A one-off status change is stated directly.
Where state-change policy is normative, express it as a status or state-transition policy for the relevant signature episteme or publication under its effective scheme and ClaimScope, with A.2.4 and F.10 status-use discipline and A.6.5 slot discipline where needed. Do not call the episteme's status a system role or create a system-role assignment for it; use E.10.ROLE to route bare *role* wording to the actual status, state, declaration position, or other direct branch.

### A.6.S:5 - Worked cases

**Ordinary cheap stop.** An editor adds the law `Refund does not increase net balance` to `PaymentBoundarySignature` and issues edition 4. The changed ClaimGraph identifies a new signature episteme; the edition or continuity relation and the editor's Work are stated only when the receiving claim uses them. If nobody needs reusable constructor vocabulary, stop. No ConstructorSignature or pair object is created.

#### A.6.S:5.1 - Repeated engineering of a service boundary

**Working situation.** Several client teams and two authoring Systems will revise and republish the same payments boundary over multiple editions. They need one reusable account of the allowed authoring operations.

**TargetSignature:** `PaymentBoundarySignature` declares operations such as `Authorize`, `Charge`, and `Refund`; the participant meanings and ref modes reused in any actual relation declaration; laws such as idempotent charging; and the external-API applicability boundary. Keep operation arguments and results under A.6.1; A.6.5 governs participant positions only in an exact RelationSignature.

**ConstructorSignature:** `PaymentSignatureEngineering` is justified because the named authoring and review uses reuse the same operation vocabulary and laws. It may declare:

* a by-value law revision and a reference-retargeting operation when those distinctions are reused; apply A.6.5 only if the move concerns a SlotSpec in an exact RelationSignature, keeping ordinary law-content revision under its declaration rule and operation arguments/results under A.6.1;
* a direct calibration, provenance, or other relation assertion under its own pattern, with an A.6.6 declaration-change label only when a receiver tracks its represented history; and
* an E.17 publication operation for the repeated Plain, Tech, and interoperability publications, with a reusable view-producing operation only when needed and any A.6.3 construction identified separately.

`PaymentSignatureEngineeringPipeline`, if admitted as a System, may apply the described operations. Any claimed dated authoring or publication Work requires its complete A.13 performer core and independent A.15.1 admission as in §4.0. The ConstructorSignature does not act. Add the separate F.6 Work-assignment relation only for precise attribution through that same obtaining assignment; state an application binding, carrier, evidence relation, or additional classification or assignment only when its own claim is current.

The sentence `Charges are recorded in Ledger L for the external API` must first name and test its actual direct relation. Do not replace it with `declareBase`, a generic `baseRelation`, or a witness package. If later comparison needs a stable representation of that assertion and its scope, A.6.6 may add the optional declaration history.

The publication faces are faithful forms over the exact TargetSignature edition for their bounded readers and uses. Any claim that the selected episteme is a `U.View` requires its own E.17.0 conformance under §4.4. `Guarantees idempotency` is unpacked into the actual law, any separate mechanism admission condition, deontic commitment, and evidence-use claim; the word *contract* creates none of them.

#### A.6.S:5.2 - Repeated engineering of a model-correspondence signature

**Working situation.** A research group maintains a correspondence signature across several model editions and publishes mathematical and engineering views. A second group must reproduce the same revisions.

`ModelCorrespondenceSignature` is the TargetSignature. Its vocabulary, laws, and applicability state the exact correspondence claim and the schemes in which it is interpreted. An actual F.9 Bridge is cited only when a relation between two exact F.17 cells obtains and a separate bounded-use claim is current.

`CorrespondenceSignatureEngineering` is an optional ConstructorSignature because the second group reuses its declared revision and view-production vocabulary. A reference-retargeting operation may identify a new model edition. An A.6.2 arrow may compare exact source and receiving signature epistemes and any named neighboring facts; it changes none of those facts. The actual application, authoring System, Work, resulting episteme, and publications remain separate.

If the project only changes one reference dataset window once, state that direct revision and any needed Work or successor edition, then stop. Do not create the ConstructorSignature merely to host `retime`.

### A.6.S:6 - Bias-Annotation

Scope: signature-engineering uses that meet the entry condition; ordinary one-off revisions remain outside the two-signature branch.

* **Architecture bias (Arch):** a reusable ConstructorSignature can improve repeated work but can also turn one edit into a framework.
  *Mitigation:* require a named receiver for the reusable vocabulary and laws; otherwise use the direct move and stop.
* **Onto/Epist bias (Onto/Epist):** treating “editing the signature” as harmless can hide semantic change.
  *Mitigation:* distinguish a direct edit or new same-EntityOfConcern edition from an A.6.4 retargeting. A changed C.2.1 discriminator identifies another episteme; A.6.4 opens only when the exact EntityOfConcern changes.

* **Pragmatic bias (Prag):** repeatable operation declarations cost authoring effort.
  *Mitigation:* introduce them only when a named receiver would otherwise reconstruct the same vocabulary or law.

### A.6.S:7 - Conformance Checklist

| ID | Requirement | Purpose |
| ---: | --- | --- |
| **CC-A.6.S-1** | State the actual assertion, revision, relation, arrow, application, or Work first. If it answers the receiving use, no ConstructorSignature or pair object is required. | Preserves the cheap direct path. |
| **CC-A.6.S-2** | A ConstructorSignature appears only when one named receiving use needs reusable constructor vocabulary, laws, and applicability. It is an independently identified `U.Signature`; `U.SignatureEngineeringPair` is not used. | Prevents an unsupported object and needless second signature. |
| **CC-A.6.S-3** | When two signatures are both current, state the exact A.6.0 dependency, method/source use, or other direct relation that actually obtains. Co-mentioning them creates no relation. | Keeps the connection explicit without inventing a universal pair. |
| **CC-A.6.S-4** | The ConstructorSignature declares only operation families its named receiver reuses. A.6.5 slot verbs, A.6.6 declaration-change labels, A.6.2-A.6.4 arrows, E.17 views, assignment identity, and evidence are each conditional on their own current use. | Prevents the constructor menu from becoming a mandatory package. |
| **CC-A.6.S-5** | A meaning change identifies a new TargetSignature episteme when a C.2.1 discriminator changes. State edition, continuity, and reference-retargeting claims only under their actual predicates; use A.6.4 only when the exact EntityOfConcern-retargeting arrow `r` is current, and identify any bounded-use assertion `q` and current-case judgement separately. | Separates episteme change, editioning, reference change, and retargeting. |
| **CC-A.6.S-6** | If an A.6.2-A.6.4 arrow is declared, keep the arrow, any separately governed use assertion, any current-case judgement, operation description, application, and Work distinct. Name the endpoint values and neighboring facts read or compared; the arrow changes no neighboring relation occurrence. | Preserves the accepted arrow/application/Work boundary. |
| **CC-A.6.S-7** | If E.17 publication is used, each face is a faithful publication form over the exact source episteme and adds no new claim. A claimed `U.View` requires E.17.0 conformance; an A.6.3 construction is separate and conditional. Preserve applicable boundary claim-set traceability under §4.4. The publication occurrence, carrier, viewpoint use, conformance, and Work remain separate. | Prevents publication drift. |
| **CC-A.6.S-8** | A System, not a signature, assignment, or local system-role kind, performs actual Work. Recover each actual performer's complete A.13 core, including its classification and obtaining A.2.1 assignment, and let A.15.1 independently admit the Work as in §4.0; add the separate F.6 Work-assignment relation afterward only when the receiving claim consumes precise attribution through that same assignment. Add application, carrier, provenance, or evidence relations only when their own distinctions are needed. | Preserves agency without mandatory attribution paperwork. |
| **CC-A.6.S-9** | Laws, operational admissibility, deontic commitments, evidence use, and Work remain under their direct patterns. The TargetSignature and ConstructorSignature do not become all-purpose containers. | Preserves A.6.B and direct-relation boundaries. |
| **CC-A.6.S-10** | The account begins with an ordinary sentence naming what changed or was reused and what visible result follows. Formal vocabulary is added only where it changes a receiving inference. | Keeps the pattern usable by a cold reader. |

### A.6.S:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
| --- | --- | --- | --- |
| **Pair object by juxtaposition** | Two signatures are named and called `U.SignatureEngineeringPair`. | No admitted kind, predicate, applicability, or occurrence identity exists. | Retire the pair token; state the exact dependency or use that actually obtains, or merely name both signatures. |
| **ConstructorSignature for every edit** | A one-line revision acquires two operation lexicons, arrow metadata, assignment, evidence, and publication records. | Reusable declaration work has replaced the actual task. | State the direct revision and stop; add a ConstructorSignature only for a named reuse of its vocabulary and laws. |
| **One publication mixes declaration and work record** | Target laws, constructor notes, review history, gates, and Work evidence share one undifferentiated artifact. | Signature, operation description, application, Work, and carrier cannot be distinguished. | Separate only the objects current for the receiving use; do not create a ConstructorSignature merely to hold notes. |
| **Silent semantic edit** | A law or applicability changes while consumers still cite the old episteme. | A new C.2.1 discriminator triple is presented as the same episteme. | Identify the successor episteme and the exact edition, continuity, or reference change actually used. |
| **Arrow as performed operation** | An A.6.2 arrow is said to author, validate, or publish a signature. | Mathematical relation, application, and Work collapse. | Let the arrow compare exact epistemes; identify any application, System, and Work separately. |
| **View as another truth** | Plain and Tech faces add different commitments. | Publication gained semantics. | Keep each face a faithful E.17 publication form over the exact source episteme and state any new claim separately; use §4.4 for view membership and boundary claim-set integrity. |
| **Episteme as actor** | The ConstructorSignature builds or publishes the TargetSignature. | Hides the acting System and gives agency to a description. | Say what the signature describes; name the System and Work only when the receiving claim needs them. |

### A.6.S:9 - Consequences

**Benefits.** One-off work remains readable and cheap. Repeated engineering can still reuse a stable ConstructorSignature. Edition, view, arrow, application, Work, assignment, evidence, and carrier claims remain independently repairable.

**Costs.** A project must decide whether reusable constructor content exists instead of opening a standard package automatically. When it does exist, maintaining another signature costs attention. The mitigation is the named-receiver test and a declaration containing only the vocabulary and laws that receiver reuses.

**Adoption test (informative).** Ask three questions in order: What actual signature claim or change is current? Does that direct account answer the use? Which named receiver, if any, needs reusable constructor vocabulary and laws? A valid adoption result may contain one TargetSignature and one ordinary revision sentence, with no ConstructorSignature.

### A.6.S:10 - Rationale

Stable boundaries sometimes benefit from a reusable description of how they are revised. That is the useful two-signature technique: one `U.Signature` is the current target declaration, and another `U.Signature` declares constructor operations for a named reuse. It is not a universal architecture for editing and does not require a third pair object.

A.6.5, A.6.6, A.6.2-A.6.4, and E.17 supply distinct optional moves. Treating all of them as mandatory constructor primitives would recreate the ambiguity and overhead those patterns are meant to remove. The direct move comes first; the reusable ConstructorSignature packages only the operation language that has an actual receiver.

The result keeps viewing, declaration edits, episteme succession, reference retargeting, EntityOfConcern Retargeting: Judge a Bounded Use Across Different Entities, application, and Work distinct. A.6.B likewise keeps laws, gates, duties, and evidence-use claims from competing in one “contract” paragraph.

**SoTA source note (informative).** Modern effect systems support the separation between an operation declaration and effectful realization; categorical optics inform explicit preservation claims; and architecture-description practice informs accountable views. A.6.S adopts those limited separations without importing a tool ontology or making a ConstructorSignature mandatory.

### A.6.S:11 - SoTA-Echoing

* **Adopt: algebraic effects and effect systems separate operation signatures from handler semantics.**
  Contemporary effect systems emphasise that an operation signature can be described independently of how effects are handled. A.6.S adopts that separation here: the TargetSignature remains the boundary declaration, while any operation application, construction Work, and operational enforcement remain separately identified. This echoes row-typed algebraic effects and modern handler formulations (Leijen 2017; Hillerström & Lindley 2018).

* **Adapt: categorical optics treat “focus” and “round‑trip laws” as a disciplined interface for bidirectional structure.**
  Optics offer a compact mathematical language for “what is preserved” under a transformation and when updates are coherent. A.6.S adapts this mindset to boundary evolution: viewing corresponds to projection, and retargeting corresponds to an explicit transition with stated preservation claims. Profunctor optics provide a post‑2015 reference point for this style of interface reasoning (Pickering, Gibbons & Wu 2017).

* **Adapt: architecture-description practice relates views to viewpoints and stakeholder concerns.**
  ISO/IEC/IEEE 42010:2022 contributes that discipline. FPF's local adaptation identifies the exact `U.Viewpoint` episteme and tests the selected episteme's `U.View` membership through E.17.0 conformance; a publication face remains the separate form over its source for a bounded reader/use, with membership and A.6.3 construction conditional under §4.4. Any separate `responsibility` or `view-accountability` claim needs its actual participants and governing predicate. A ConstructorSignature is added only when a named receiver reuses the view-producing operation declaration; it is not required to explain how every view was produced.

* **Adopt in spirit: behavioural protocol disciplines treat boundaries as typed interaction protocols with safety commitments.**
  Session and behavioural type practice treats boundaries as protocols with progress and safety properties, which matches the A.6 split between signature laws and mechanism entry gates. A.6.S does not import tooling or typechecking, but it adopts the practice of making boundary interactions explicit and law‑governed (e.g., modern MPST practice as cited in A.6.1).

### A.6.S:12 - Relations

* **Depends on:**

  * A.3.1/A.3.2/A.15/A.15.1/A.15.2 — Method, MethodDescription, WorkPlan, Work, and work-result separation
  * A.7 — Strict Distinction (object ≠ description ≠ carrier; Face ≠ Surface)
  * A.6 — Signature Stack: Classify and Place Boundary Claims
  * A.6.0 — `U.Signature`
  * A.6.2 — effect-free episteme-arrow discipline, only when a constructor operation uses a mathematical arrow; endpoint facts are read or compared, not changed by the arrow
  * A.1, A.13, and A.15.1 — System admission, the complete actual-performer core including local-kind classification and an obtaining A.2.1 assignment, and independent dated-Work admission; F.6 follows only for precise attribution through that same assignment
  * C.2.1 — episteme identity through claim content, exact EntityOfConcern, and effective ReferenceScheme, with empirical grounding and edition continuity kept as separate direct relations
  * (optional) E.18 — TransformationFlowStructure, when signature-construction work is represented as a transformation-flow structure
  * E.10 and LEX discipline — if the publication uses Plain twins (“SoI”) or shorthands, keep their exact Tech readings recoverable and keep Plain twins out of normative register
  * A.6.3 — `U.EpistemicViewing`
  * A.6.4 — EntityOfConcern-retargeting arrows, their separate C.2.1 bounded-use assertions, and separate current-case judgements
  * A.6.5 — relation-declaration slot discipline
  * A.6.6 — Base Declaration Discipline
  * A.6.B — Boundary Norm Square & Claim Register discipline
  * E.17 and E.17.0 — MVPK and multi‑view describing

* **Coordinates with:** A.6.5 for reused relation-participant or reference operations and A.6.6 for direct base-dependence assertions and optional declaration history; neither vocabulary is mandatory.

* **Constrains:** a signature-engineering use only where the relevant meaning change, edition, reference retargeting, view, application, or Work claim is current; one distinction does not make the others mandatory.

### A.6.S:End
