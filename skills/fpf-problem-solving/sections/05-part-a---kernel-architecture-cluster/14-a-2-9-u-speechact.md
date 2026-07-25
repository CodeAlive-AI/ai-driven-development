## A.2.9 — `U.SpeechAct` (Communicative Work Kind, Occurrences, and Records)

> **Status:** Stable
> **Type:** Definitional work-ontic pattern

### A.2.9:0.1 - Kind Settlement

`U.SpeechAct` is the admitted communicative-work kind under `U.Work`. One individual such as `SA-Approve-4711 : U.SpeechAct` is an actual temporally bounded speech-act occurrence. A `SpeechActRecord : U.Episteme` may state claims about that occurrence; it is neither the occurrence nor what makes the occurrence actual.

### A.2.9:0 - Use This When

Use this pattern when a communicative event must be modeled as performed work: an approval, authorization, revocation, notice, declaration, publication, or similar act whose occurrence changes what a project can claim or do.

**What goes wrong if missed.** A document, interface, ticket, message, or log is treated as if it performed the act; approval, utterance content, evidence carrier, commitment, and performed work collapse into one governance phrase.

**What this buys.** Actual communicative Work occurrences become inspectable without collapsing them into a claim-bearing `SpeechActRecord`, an utterance description, or an evidence carrier.

Typical moments:

- a release, gate, or work step depends on whether a named approval or authorization was performed;
- a publication, notice, or revocation changes status in a bounded context;
- a commitment must cite the act that instituted it, rather than only pointing at a document;
- a message, ticket, signed record, or API call log is being mistaken for the act itself.

**Primary EntityOfConcern.** The EntityOfConcern is one actual speech-act occurrence admitted under the kind `U.SpeechAct`: a communicative Work individual performed by an admitted accountable `U.System` under an exact obtaining `U.RoleAssignment` in a bounded context. The system performs the act; the assignment supplies the role and authority ground. A `SpeechActRecord`, the utterance-description episteme, and the file, message, ticket, or log carrier are separate objects.

**First useful move.** Name the actual occurrence, performer system, and assignment under which it acts, then name the judgement context, time window, act type, what the utterance is about, and—only when current—the intended institutional target and independently established effect. Create a `SpeechActRecord` only when a receiving use needs a persistent claim about that occurrence; add utterance or carrier references only when observation, audit, or source return needs them.

**Not this pattern when.** If the question is only what a document says, use A.7/C.2/E.17. If the question is who is accountable under a deontic relation, use A.2.8. If the question is evidence, use A.10/G.6. If the work has no communicative effect, use A.15.1 directly.

> **Type:** Definitional (D)
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → **A.2 Roles & Agency Kernel**
> **Refines:** A.2 (Role Taxonomy)
> **Builds on:** A.2.1 (RoleAssignment), A.2.6 (`Γ_time` and windows), A.7 (EntityOfConcern, Description episteme, and carrier), A.10 (SCR/RSCR carrier discipline), A.15.1 (`U.Work`)
> **Purpose (one line):** Admit communicative enactments under the `U.SpeechAct` kind, identify each actual Work occurrence, and provide a minimal optional `SpeechActRecord` for claims about it while keeping the act, record, utterance description, and evidence carrier separate.

> FPF already treats communicative acts as observable events used in role-state checklists and grounding (“presence of act: AuthorizationSpeechAct exists…”); those checks cite actual occurrences admitted under `U.SpeechAct`, not the kind itself.
> The spec’s micro-examples and conformance gates distinguish **communicative Work** (“performed a SpeechAct”) from **operational Work** (“executed Work”) while keeping both inside `U.Work` (cf. CC‑A15‑10 GateSplit).
> F.18 can name `U.SpeechAct` in the promise/utterance/commitment triad; A.2.9 keeps the ontology and conformance discipline in Part A where communicative work, utterance description, and evidence carrier can be kept distinct.

### A.2.9:1 — Problem frame

FPF repeatedly needs to reference “someone said/did the approving/authorizing/declaring thing”:

* Role eligibility and enactability checklists often depend on the **presence of an approval/authorization act** within a freshness window.
* Governance patterns and boundary writing (A.6 stack) need **provenance**: “this obligation or commitment, or this separately represented granted permission, was instituted by *that* act”.
* Operational patterns need auditable **notices** (“depletion notice”, “override invoked”) whose existence and timing matter.

Without a first-class kind for such communicative Work and a separate way to describe each occurrence, authors tend to:

* attribute agency to descriptions (“the spec approves…”, “the interface guarantees…”),
* collapse “utterance text” and “speech act event”,
* leave provenance dangling as “if modeled”,
* encode gates as prose obligations, or treat obligations as gates.

This pattern admits `U.SpeechAct` as an explicit Work kind, identifies actual speech-act occurrences under it, and keeps their optional records separate from `U.Commitment`, utterance descriptions, and carriers.

### A.2.9:2 — Problem

How can FPF represent communicative enactments so that:

1. **Agency is explicit:** an admitted accountable `U.System` performs the act under a covering role assignment, not a role value, assignment, document, spec, or interface.
2. **The act is locatable in time:** the act has an explicit Window (and thus freshness can be evaluated).
3. **The act is locatable in meaning:** the act is recognized inside a declared **bounded context** (the `U.Work` judgement context), not via `U.ClaimScope` (which expresses applicability of claims/commitments, not the judgement context for Work occurrences).
4. **The act is auditable:** it has at least one declared utterance description, evidence carrier, or both when used for gate checks or governance.
5. **Institutional effects are linkable:** the act can institute (or update/revoke) commitments, role assignments, statuses, etc., by reference.
6. **Ambiguity is handled pragmatically:** the model supports multi-function and multi-party communication without requiring full linguistic pragmatics.

### A.2.9:3 — Forces

| Force                  | Tension                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Minimality             | Needs to be light enough for routine modeling and linting; not a full pragmatics or legal-contract system.              |
| Auditability           | If used as a gate, it must be evidence-backed; but not all communicative acts are equally observable or retainable.     |
| Context locality       | Meaning and “institutional force” are context-local; cross-context reuse must remain explicit (Bridge-only discipline). |
| Multi-party reality    | Many real boundaries are multiparty (protocols, organizations); dyadic “speaker-hearer” is too narrow.                  |
| Multi-function reality | One utterance can carry multiple recognizable functions; “one act = one force” is often false.                          |
| Separation discipline  | Must preserve **kind** ≠ **actual act occurrence** ≠ **SpeechActRecord** ≠ **utterance description** ≠ **carrier or trace**. |

### A.2.9:4 — Solution

`U.SpeechAct` is the admitted kernel kind for communicative Work. An individual `SA : U.SpeechAct` is the actual enactment performed by an admitted accountable `U.System` under an exact obtaining role assignment within a bounded context. A `SpeechActRecord` may describe that occurrence and point to utterance descriptions or evidence carriers; none of those epistemic or representational objects is the act.

#### A.2.9:4.1 — Normative definition

`U.SpeechAct <: U.Work` is a kind declaration. An actual Work individual is admitted as `SA : U.SpeechAct` when its primary effect is **communicative**: it places an utterance into a context in a way that is recognized by that context’s institutional semantics (policies, procedures, protocol rules) as potentially:

* asserting/informing,
* requesting/directing,
* promising/committing (as an instituting act),
* declaring/authorizing/revoking (status-changing acts),
* notifying (event announcement relevant for downstream work).

Per A.7 and A.15.1, the actual speech-act occurrence is a Work individual; its `SpeechActRecord` and **utterance descriptions** are epistemes, while its **carriers** are utterance carriers, publication carriers, or traces that allow observation and audit. *(Note: “Surface” is reserved for MVPK publication/interoperability surfaces; do not use it here.)*

Whether a given act type institutes commitments, permissions, or status changes is entirely context-policy dependent. Absent an explicit policy, treat `SA : U.SpeechAct` only as an actual communicative Work occurrence; neither its kind membership nor a complete-looking record licenses a deontic inference.

#### A.2.9:4.2 — Minimal occurrence-description record (normative)

Use the following declaration schema only when a receiving use needs a persistent claim about an actual or candidate speech-act occurrence. The record fields state claims about the referenced occurrence; they are not fields stored in the Work individual and do not make it occur.

```
U.SpeechAct <: U.Work

SpeechActRef ::= U.EntityRef
  // resolves to one actual Work individual admitted as SA : U.SpeechAct

SpeechActRecord <: U.Episteme

SpeechActRecord ::=
    {
      speechActOccurrenceRef: SpeechActRef,
      performedBy: U.EntityRef,                     // resolves to the admitted U.System that acts
      performedUnderAssignment: RoleAssignmentRef,  // exact covering role/authority ground
      enactsMethodRef: optional<U.EntityRef>,        // resolves to the exact U.Method when recovered
      methodDescriptionRef: optional<U.EpistemeRef>, // separate description, only when the use needs it
      unresolvedEnactsMethodClaimRef: optional<ClaimIdRef>,
      methodRelationGapProvenanceRef: optional<U.EpistemeRef>,
      reliancePosture: observationOnly | relianceReady,
      executedWithin: U.EntityRef,                   // claim about the containing U.System
      window: [start, end | open],                   // claim about the occurrence's actual extent
      judgementContextRef: U.BoundedContextRef,
      utteranceSubjectRefs: optional<set<U.EntityRef>>,
      institutionalTargetRefs: optional<set<U.EntityRef>>,
      actTypes: set<SpeechActTypeRef>,               // ≥1 act types (supports multi-function)
      addressedTo: optional<set<AddresseeRef>>,      // optional: who is addressed / audience
      utteranceRefs: optional<set<DescriptionRef>>,  // where the utterance description is stated or recorded (A.7: Description)
      carrierRefs: optional<set<CarrierRef>>,        // evidence carriers/traces (A.7: Carrier; use A.10 when evidentiary)
      institutes: optional<InstitutedEffects>,       // references to objects/claims instituted/updated by this act
      notes: optional<InformativeText>               // explicitly informative
    }

DescriptionRef ::=
  ClaimIdRef | EpistemeRef
  // Pointer to an utterance description (e.g., spec clause claim ID, a policy episteme, a message-content episteme).

SpeechActTypeRef ::=
  ContextLocalTokenRef
  // Must be defined/recognized in the Work’s judgement context (bounded context).

AddresseeRef ::=
  PartyRef | RoleRef | RoleAssignmentRef

GrantedPermissionRelationRef@Context ::= U.EntityRef
  // resolves only to one exact GrantedPermissionRelation@Context occurrence

EpistemePublicationRelationRef ::= U.EntityRef
  // resolves only to one exact E.24.PUB EpistemePublicationRelation occurrence

InstitutedEffects ::=
  {
    commitments: optional<set<CommitmentIdRef>>,
    permissions: optional<set<GrantedPermissionRelationRef@Context>>,
    roleAssignments: optional<set<RoleAssignmentRef>>,
    publicationRelations: optional<set<EpistemePublicationRelationRef>>
  }
```

**Occurrence-side constraints:**

* **(SA‑C0) Actual Work conformance.** The individual referenced by `speechActOccurrenceRef` **MUST** independently satisfy `U.Work` conformance (A.15.1), including the actual performer system, covering assignment, enacted method, containing system, temporal extent, and judgement-context anchoring. A complete record neither creates those facts nor substitutes for them.
* **(SA‑C1) The accountable system performs; the assignment grounds.** The occurrence's actual performer **MUST** be an admitted `U.System`. The exact obtaining `U.RoleAssignment` under which it acts **MUST** have that system in `HolderSystemSlot` and cover the act. The assignment supplies role, authority, and attribution ground; it does not perform the act.
* **(SA‑C2) Act types are occurrence classifications and context-local.** The occurrence **MUST** instantiate at least one `SpeechActTypeRef` recognized in its judgement context. A token written into a record does not establish that classification unless the context's predicate is satisfied.
* **(SA‑C3) Time honesty.** The occurrence **MUST** have an actual temporal extent so freshness can be evaluated; a recorded timestamp is a claim about that extent, not the extent itself.

Keep three questions separate. `utteranceSubjectRefs` answers **what the utterance or claim is about**. `institutionalTargetRefs` answers **which object or relation the act is intended to institute or update under the named policy**. Actual change or institutional effect is a third world-side fact and is stated only through its exact direct change/effect relation and the matching typed `institutes.*` reference when the record needs it. An informative notice or assertion may have a subject without any institutional target or changed entity. Shared reference values do not collapse these relation meanings.

**Record- and reliance-side constraints:**

* **(SA‑C4) A relied-on occurrence must be observable.** When a gate, checklist, commitment, or grant relies on a `SpeechActRef`, the `SpeechActRecord` **SHALL** identify that same occurrence and cite at least one applicable `utteranceRef`, `carrierRef`, or separately governed evidence relation. Evidence-critical uses **SHOULD** cite at least one carrier through A.10. Record completeness alone does not prove occurrence or institutional force.
* **(SA‑C5) Institutional-effect claims are typed references to world-side effects.** `institutes.*` may reference only the exact commitment or relation occurrence through its declared RefKind. Each `institutes.permissions` value **MUST** be a `GrantedPermissionRelationRef@Context` whose context matches the speech-act occurrence's judgement context or is connected by the explicit Bridge used by the receiving claim. Each `institutes.publicationRelations` value **MUST** resolve to an obtaining `EpistemePublicationRelation` under E.24.PUB. A status claim is an episteme about an effect, not an instituted effect; keep it and its A.10 evidence relation outside `institutes.*`. The cited policy and direct world-side obtaining conditions still decide whether any effect exists.
* **(SA‑C6) Cross-context use is Bridge-only.** If a `SpeechActRef` or `SpeechActRecord` is interpreted for checking, gate evidence, or provenance in a different bounded context than the occurrence's judgement context, the receiving claim **MUST** cite the Bridge/policy that licenses that interpretation rather than assuming equivalent force from the same label.

#### A.2.9:4.3 — `SpeechActRef` discipline (normative)

A **`SpeechActRef`** resolves to one actual Work individual admitted as `SA : U.SpeechAct`. It never denotes the kind itself or a `SpeechActRecord`.

* If another object (for example, `U.Commitment.source.speechActRef`) cites a `SpeechActRef`, the referenced occurrence **MUST** satisfy occurrence-side **SA‑C0…SA‑C3**. A gate, audit, or provenance use additionally needs the record/evidence basis in **SA‑C4** and **SA‑C6** when cross-context.
* A `SpeechActRef` **MUST NOT** be replaced by an `EpistemeRef` (“see the document”) when occurrence provenance is needed. A `SpeechActRecord` or utterance-description episteme may make claims about the occurrence but is not the act.
* If a source cannot complete a `SpeechActRecord`, it may create an observation stub with the candidate `speechActOccurrenceRef`, known claims, provenance for those claims, and explicit unknowns. When the actual `enactsMethod` relation is not recoverable, leave `enactsMethodRef` absent, cite the exact unresolved claim and source-gap provenance, and set `reliancePosture=observationOnly`. The stub does not make the candidate actual, satisfy occurrence-side conformance, or support gate/deontic provenance. It becomes reliance-ready only after the exact `enactsMethod -> U.Method` relation is recovered, or after the governing Work architecture explicitly establishes that this occurrence needs no such relation. Never mint an `AdHocCommunication` or other `U.MethodDescription` solely to fill the gap; a description neither is the method nor enacts itself.

#### A.2.9:4.4 — Separation rules with `U.Commitment`, `GrantedPermissionRelation@Context`, and `U.PromiseContent` (normative)

1. **Speech act is not the enduring deontic relation.**
   A speech-act occurrence may **institute** a `U.Commitment` for an obligation, recommendation-as-duty, or prohibition, or a `GrantedPermissionRelation@Context` for strong permission. The enduring relation is the separately governed object, not the act. Do not encode obligations or permissions as prose inside its `SpeechActRecord`: cite commitments in `institutes.commitments` and grants in `institutes.permissions`, each under the exact instituting policy (`A.2.8`, `A.2.8.PER`).

2. **Speech act is not the service promise clause.**
   `U.PromiseContent` is the promised-outcome statement; a speech act may be the act of offering or issuing that promise, but the promise content lives in the promise-content object and is referenced from the resulting commitments.

3. **Speech act is not the carrier.**
   A “signed approval PDF”, ticket, message, or API log is a carrier; it may carry an utterance-description episteme or a `SpeechActRecord`. The speech act is the Work occurrence described or evidenced, not either episteme and not the carrier.

4. **Publishing a spec is not a commitment by default.**
   **Default interpretation rule (normative).** A conformant model/interpreter **MUST NOT** infer a `U.Commitment`, `GrantedPermissionRelation@Context`, publication occurrence, or subject-specific status relation solely from a `Publish`/`Approve` speech-act occurrence or its record. Publication work may establish an `EpistemePublicationRelation` only when E.24.PUB's selected edition, audience, bounded use, form, carrier, and availability conditions obtain. A constitutive policy may let an act institute a subject-specific `Approved`, `Published`, or similar status relation; then cite that exact relation occurrence through the subject pattern and separately cite any C.2.1 status claim and A.10 evidence. The claim represents the status; neither its ID nor its publication makes the status obtain.

#### A.2.9:4.5 — Multi-function and multi-party support (normative)

* **Multi-function:** `actTypes` is a **set**. If one utterance performs multiple recognizable acts (e.g., “approve + instruct + warn”), the model may either:

   * identify one speech-act occurrence and let its `SpeechActRecord` state multiple satisfied `actTypes`, or
   * identify multiple actual speech-act occurrences and give each its own `SpeechActRef`; their records may share the same `carrierRefs/utteranceRefs`.
   In either case, institutional effects must remain referenceable (SA‑C5).

* **Multi-party:** `addressedTo` is a set and may include roles/parties/assignments. If addressees matter for validity (e.g., “approval by CAB chair to deployment bot”), they should be explicit.

### A.2.9:5 — Archetypal Grounding (Tell–Show–Show)

#### A.2.9:5.1 — Tell (universal rule)

When governance or gating depends on “someone said/did X”, identify **that saying/doing** as an actual Work occurrence `SA : U.SpeechAct`. Add a `SpeechActRecord` only to state relied-on claims about it, and keep the utterance text and carriers separate. If the occurrence creates obligations, recommendations-as-duty, or prohibitions, cite explicit `U.Commitment` objects; if it creates strong permission, cite an explicit `GrantedPermissionRelation@Context`. The act institutes neither effect without the exact context policy.

#### A.2.9:5.2 — Show #1 (system archetype: change-control approval gates a deployment)

**Situation (messy prose):**
“Change is approved, so the pipeline may deploy.”

**Conformant modeling sketch.** The first line names the actual Work individual. The following episteme reports claims about it; those claims must be true independently.

* Actual occurrence: `SA-Approve-4711 : U.SpeechAct`

* `SA-Approve-4711-Record : SpeechActRecord`

  * `speechActOccurrenceRef = SpeechActRef(SA-Approve-4711)`
  * `actTypes = {SpeechActTypeRef(Approval@ChangeControl)}`
  * `performedBy = U.EntityRef(CAB_Chair_A)` where `CAB_Chair_A : U.System`
  * `performedUnderAssignment = RoleAssignmentRef(CAB_Chair_A@ApproverRole@ChangeControl)`
  * `enactsMethodRef = U.EntityRef(ChangeApprovalMethod_v3)`; the actual `enactsMethod` relation independently obtains
  * `methodDescriptionRef = EpistemeRef(ChangeApprovalProcedure_v3)`
  * `reliancePosture = relianceReady`
  * `executedWithin = ChangeControlBoardSystem`
  * `window = [t,t]`
  * `judgementContextRef = ChangeControl`
  * `utteranceSubjectRefs = {ChangeRequestId(4711)}`
  * `institutionalTargetRefs = {GrantedPermissionRelationRef@ChangeControl(PER-Deploy-4711)}`
  * `utteranceRefs = {EpistemeRef(ChangeTicket#4711)}`
  * `carrierRefs = {CarrierRef(TicketSystemRecord#4711)}`
  * `institutes.permissions = {GrantedPermissionRelationRef@ChangeControl(PER-Deploy-4711)}`

* `GrantedPermissionRelation@ChangeControl PER-Deploy-4711`

  * `beneficiaryRef = RoleAssignmentRef(OpsBot#DeployerRole:CD_Pipeline_v7)`
  * `permittedActionSpecificationRef = EpistemeRef(DeployChange4711WorkSpecification)`
  * `institutingSpeechActRef = SA-Approve-4711`
  * `grantorAssignmentRef = RoleAssignmentRef(CAB_Chair_A@ApproverRole@ChangeControl)`
  * `grantValidityPolicyRef = EpistemeRef(ChangeControlGrantPolicy_v3)`
  * `scope`, `validityWindow`, and revocation stance are explicit.

The utterance is about `ChangeRequestId(4711)`; its policy-selected institutional target and demonstrated effect are the separately obtaining grant occurrence. Nothing here claims that the change-request entity itself changed.

* Gate predicate `A-Gate-Deploy-4711` independently states whether deployment entry conditions hold. It may check `exists SpeechAct(type=Approval, utteranceSubjectRefs includes ChangeRequestId(4711), performedBy=CAB_Chair_A, performedUnderAssignment role=ApproverRole, within 90d)`, consume the current grant occurrence, and apply other prerequisites; passing the gate neither institutes nor equals the grant.

This preserves:

* kind vs actual act vs record vs utterance text vs carrier vs enduring grant,
* explicit performer and grant beneficiary,
* time window and policy for currentness,
* explicit provenance from the grant to the instituting act, and
* the distinction between strong permission and an admissibility gate.

#### A.2.9:5.3 — Show #2 (episteme archetype: publishing a spec edition without making the spec an agent)

**Situation (anti-pattern):**
“The interface spec declares MUST/SHALL requirements.”

**Conformant modeling sketch.** `SA-Publish-API-v12` is the actual occurrence; the record is a separate episteme about it.

* Actual occurrence: `SA-Publish-API-v12 : U.SpeechAct`

* `SA-Publish-API-v12-Record : SpeechActRecord`

  * `speechActOccurrenceRef = SpeechActRef(SA-Publish-API-v12)`
  * `actTypes = {SpeechActTypeRef(Publish@APISpecContext), SpeechActTypeRef(DeclareNorms@APISpecContext)}`
  * `performedBy = U.EntityRef(StandardsEditor_A)` where `StandardsEditor_A : U.System`
  * `performedUnderAssignment = RoleAssignmentRef(StandardsEditor_A@PublisherRole@APISpecContext)`
  * `enactsMethodRef = U.EntityRef(SpecPublicationMethod_v12)`; the actual `enactsMethod` relation independently obtains
  * `methodDescriptionRef = EpistemeRef(SpecReleaseProcedure_v12)`
  * `reliancePosture = relianceReady`
  * `executedWithin = SpecPublicationSystem`
  * `window = [t,t]`
  * `judgementContextRef = APISpecContext`
  * `utteranceSubjectRefs = {EpistemeRef(APISpec_v12)}`
  * `institutionalTargetRefs = {EpistemeRef(APISpec_v12)}`
  * `utteranceRefs = {EpistemeRef(APISpec_v12)}`
  * `carrierRefs = {CarrierRef(GitTag:v12), CarrierRef(SignedReleaseArtifact:v12)}`
  * `institutes.publicationRelations = {EpistemePublicationRelationRef(APISpec-v12-Publication)}`

* `APISpec-v12-Publication : EpistemePublicationRelation` separately names the selected `APISpec_v12` edition, audience declaration, bounded-use declaration, publication form, and exact carrier; it obtains only while that edition is available under E.24.PUB.

The same `APISpec_v12` episteme is both the subject of the publication utterance and the object made available by the publication relation, but those are different relations. The act does not thereby change the spec's claim content or make the episteme an actor. If `D-StdStatus-APISpec_v12-Published` is needed, keep it as a separate C.2.1 claim about the publication occurrence and cite its evidence through A.10; do not put the claim in `institutes`. Norms live in the **published utterance descriptions**, while the **act of publication** is performed by `StandardsEditor_A` under its publisher assignment.

### A.2.9:6 — Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Kernel universal** for speech-act usage that matters for governance, eligibility, gating, provenance, and protocol boundaries.

* **Gov bias:** favors explicit accountable performers and auditable records; increases clarity but adds modeling overhead.
* **Arch bias:** optimizes evolvability by keeping institutional effects referenceable rather than embedded in prose.
* **Onto/Epist bias:** enforces kind≠actual act≠record≠utterance≠carrier and prevents episteme-as-agent metaphors.
* **Prag bias:** models only what is needed for decisions/audit (not full intention/sincerity/perlocutionary psychology).
* **Did bias:** keeps the record minimal and queryable for state checklists and boundary reviews.

### A.2.9:7 — Conformance Checklist (normative)

1. **CC‑A.2.9‑1 (Occurrence, performer, and assignment).** One actual Work individual is admitted as `SA : U.SpeechAct`; its performer is an admitted accountable `U.System`, and the exact covering `U.RoleAssignment` has that system as holder. Any `SpeechActRecord` states those as claims and **MUST NOT** make the assignment, role value, organizational label, episteme, or carrier the performer.
2. **CC‑A.2.9‑2 (Act-type predicate).** The actual occurrence satisfies at least one context-local `SpeechActTypeRef`; merely writing a token into `SpeechActRecord.actTypes` is insufficient.
3. **CC‑A.2.9‑3 (Actual extent versus timestamp claim).** The occurrence has an actual temporal extent. A record's `window` must truthfully state that extent at the required precision; it does not create it.
4. **CC‑A.2.9‑4 (Observable relied-on occurrence).** If a checklist, guard, commitment, or grant cites the occurrence, one `SpeechActRecord` identifies it and cites an applicable utterance, carrier, or direct evidence relation. Evidence-critical uses **SHOULD** cite at least one carrier through A.10.
5. **CC‑A.2.9‑5 (Typed world-side effects, separate claims).** A record's `institutes.*` branch references only an exact commitment or obtaining relation occurrence through its declared RefKind. A grant uses `GrantedPermissionRelationRef@Context`; publication uses `EpistemePublicationRelationRef`; a subject-specific status uses its direct relation type. A status claim and its evidence stay separate, and no record field makes any effect obtain.
6. **CC‑A.2.9‑6 (Bridge-only cross-context use).** A receiving claim that interprets a `SpeechActRef` or `SpeechActRecord` in another bounded context cites the Bridge/policy that licenses that interpretation.
7. **CC‑A.2.9‑7 (No fabricated method anchor).** If the occurrence's actual `enactsMethod -> U.Method` relation cannot be recovered, the record names the unresolved claim and source-gap provenance, remains `observationOnly`, and is not used for gate or deontic provenance. A placeholder `U.MethodDescription` never closes the gap.
8. **CC‑A.2.9‑8 (Subject, target, and effect stay distinct).** A record uses `utteranceSubjectRefs` for aboutness and `institutionalTargetRefs` only for a policy-selected target. It claims actual change or institutional effect only through the exact direct relation; an informative act needs no changed target.

### A.2.9:8 — Common Anti-Patterns and How to Avoid Them

| Anti-pattern                                                              | Why it fails                         | Repair                                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------- |
| **Episteme- or assignment-as-actor** (“the spec/assignment approves”)     | assigns agency to a description or relation | represent the act with `performedBy` naming the admitted system and `performedUnderAssignment` naming its covering role/authority relation |
| **Kind/occurrence/record collapse** (`U.SpeechAct` used for all three)     | a complete record is mistaken for actual Work | reserve `U.SpeechAct` for the kind, identify `SA : U.SpeechAct` as the occurrence, and use `SpeechActRecord` only for claims about it |
| **Carrier-as-act** (“the signed PDF is the approval”)                     | conflates carrier with act           | identify the actual speech-act occurrence; let its separate `SpeechActRecord` cite the PDF carrier and any utterance-description episteme |
| **Placeholder method as Work anchor**                                     | a fabricated description hides an unknown world-side relation | leave `enactsMethodRef` unresolved with source-gap provenance and `observationOnly`; recover the actual method relation before reliance |
| **`affected` as aboutness, target, and effect**                            | one field makes mention look like world-side change | state the utterance subject and intended institutional target separately; cite an exact obtaining change/effect relation only when one exists |
| **Status claim listed as instituted effect**                              | a claim ID is mistaken for the status it describes | cite the exact status or publication relation occurrence; keep the C.2.1 claim and A.10 evidence separate |
| **Free-text type** (“type=‘approved-ish’”)                                | not lintable; drifts across faces    | register `SpeechActTypeRef` in the context and use it                                    |
| **Act carries obligations** (obligations embedded as prose in speech act) | collapses act and deontic binding    | model obligations as `U.Commitment` objects instituted by the act                        |
| **Gating without window**                                                 | cannot evaluate freshness            | add explicit `window` and reference it in the guard/checklist                            |
| **Hidden multi-act** (one event silently creates multiple commitments)    | loses traceability; creates disputes | represent multi-function via `actTypes` set or multiple speech acts sharing the same carrier |

### A.2.9:9 — Consequences

**Benefits**

* Makes approvals/authorizations/notices **first-class and queryable**, enabling clean RSG checklists and guard rules.
* Provides stable provenance: commitments, granted permissions, and status transitions can cite the **instituting act** explicitly.
* Prevents recurring category errors: “documents promise”, “interfaces commit”, “logs prove”.

**Trade-offs / mitigations**

* Reliance-bearing uses require a small structured `SpeechActRecord` plus adequate evidence; ordinary occurrence talk needs no record when no later claim must cite it.
* Requires context-local `SpeechActTypeRef` registration; mitigated by starting with a small set (Approve, Revoke, Publish, Notify, Authorize) and extending as needed.

### A.2.9:10 — Rationale

FPF already relies on communicative acts (approvals, notices, overrides) as operationally meaningful events. A.2.9 therefore admits `U.SpeechAct` as the Work kind, treats each actual act as a temporally bounded Work individual under it, and uses `SpeechActRecord` only for claim-bearing representation. That separation keeps performer, scope, time, utterance descriptions, carriers, and separately governed deontic effects (`U.Commitment` or `GrantedPermissionRelation@Context`) inspectable without letting a record stand in for actuality.

This also improves modularity:

* **F.18** can remain a **lexical entry point** for naming (why “SpeechAct” and “utterance” are useful labels),
* while **A.2.9** carries the ontology and conformance discipline for the kind, its actual occurrences, their optional records, and their connections to commitments, granted permissions, and evidence.

### A.2.9:11 — SoTA-Echoing (informative; post-2015 alignment)

> **Informative.** Alignment notes; not normative requirements.

* **Adopt — ISO 24617‑2:2020 / multi-dimensional communicative functions.** Modern dialogue‑act standards treat communicative behavior as potentially multi‑functional. A.2.9 mirrors this by allowing `actTypes` to be a **set** and by supporting shared carriers across multiple acts.
* **Adapt — commitment-based semantics for communication (multi-agent/protocol practice, 2015+).** A pragmatic way to avoid mental-state modeling is to track communication by its **social/institutional effects**, especially on commitments, permissions, and protocol states. A.2.9 reflects this via separate `institutes.commitments` and `institutes.permissions` links to `U.Commitment` and `GrantedPermissionRelation@Context` without modeling sincerity or intention.
* **Adopt (warning) — illocutionary pluralism in multiparty discourse (2015+).** One utterance commonly performs multiple recognizable functions. A.2.9 avoids the “single force” trap by permitting multi-type acts, multiple acts sharing the same utterance and carriers, or both.

### A.2.9:12 — Relations

**Uses / builds on**

* Uses **A.15.1 (`U.Work`)** for the event/work backbone (actual performer system, covering assignment, window, and stance).
* Uses **A.7** for the strict actual-act≠record/description≠carrier split.
* Coordinates with **A.2.6** for scope/window discipline.

**Used by**

* **A.2.8 (`U.Commitment`)** as a concrete target for `source.speechActRef` provenance, and **A.2.8.PER** for a `GrantedPermissionRelation@Context` grounded by `institutingSpeechActRef`.
* **A.2.5 (RSG checklists/guards)** when “presence of authorization/approval act” is a criterion.
* **A.6.C (Contract unpacking)** as the “utterance/instituting act” hook that prevents episteme-as-agent claims and improves provenance.

### A.2.9:End

