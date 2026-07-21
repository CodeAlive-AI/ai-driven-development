## A.6.C — Contract Unpacking for Boundaries

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → **A.6 Signature Stack & Boundary Discipline**
> **Builds on:** A.6 (stack + classification intent), **A.6.B** (L/A/D/E), **A.6.8 (RPR‑SERV)** (service‑cluster polysemy unpacking), **A.7** (EntityOfConcern, Description episteme, and carrier separation), **A.2.3** (`U.PromiseContent`), **A.2.8** (`U.Commitment`), **A.2.8.PER** (strong/weak permission, exercise, and conflict), **A.2.9** (`U.SpeechAct`), **A.15.1** (`U.Work`), **A.10** and **B.3** (evidence and assurance use), E.10 (`L-SERV` and `LEX-BUNDLE`), E.17 (MVPK “no new semantics” faces), F.12 (service acceptance and evidence discipline)
> **Naming boundary:** **F.18** may provide durable names for recovered terms when naming is current; it does not govern the promise-content, speech-act, commitment, permission, work, evidence, or boundary ontology.
> **Mint or reuse (terminology):** Reuses “contract”, “SLA”, and “guarantee” as Plain-level boundary shorthand; mints **Contract Bundle** as an unpacking lens (not a new entity kind), plus optional register columns (`bundleId`, `bundlePart`, and `faceRefs`). **NQD-front seeds (informative):** contract packet, agreement bundle, boundary bundle (chosen: *Contract Bundle* for low collision with existing “bundle” terms).
> **Purpose (one line):** Prevent “contract soup” and agency misattribution by unpacking contract-language into distinct promise-content, utterance package, commitment or permission under separate direct owners, performed work, and carrier-referenced evidence as adjudication basis, then classifying each part into the Boundary Norm Square.

### A.6.C:1 — Problem frame

Boundary descriptions frequently use “contract” as a shorthand for “the thing that governs the interaction”. That shorthand is useful in conversation, but it collapses distinct layers that FPF deliberately keeps separate:

* **Promise-level intent** (what is promised to be true or provided),
* **Published description** (what is written and versioned),
* **Deontic governance results** (accountable obligations/recommendations/prohibitions as commitments, and strong/weak permission under its separate owner),
* **Operational work and evidence** (what actually happens and what can be observed).

When these layers are collapsed, authors accidentally assign agency to epistemes (“the interface guarantees…”), encode runtime gates as if they were internal laws, or treat observability as a property of text rather than of carriers and work. A.6 and A.6.B already provide an L/A/D/E claim-classification discipline for boundary claims, but “contract” language remains a recurring entry point for category mistakes.

**Service-cluster note (modularity + lexicon).** Boundary “contract talk” commonly co‑moves with the *service* cluster (*service*, *service provider*, *server*, *SLA*, *SLO*, and *service-level*). When those tokens appear, their referents MUST be disambiguated per **A.6.8 (RPR‑SERV)** before (or while) applying the four‑part Contract Bundle below. In particular, `U.PromiseContent` is promise content and is written in normative prose as **promise content** (not as bare “service”).

A.6.C makes contract-language usable inside the A.6 stack by providing a canonical unpacking that can be applied to APIs, hardware interfaces, protocols, and socio-technical boundaries.

**Non‑goals (to preserve modularity).** A.6.C does **not**:
* define “legal contract” doctrine (offer, acceptance, consideration, jurisdictional enforceability, etc.);
* resolve conflicts between incompatible commitments or between a current grant and prohibition across scales or contexts (capture them as separate `D-*` claims and apply the direct commitment, permission-conflict, or mediation owner when it exists);
* redefine the core meanings of `U.PromiseContent`, `U.Work`, `U.SpeechAct`, `U.Commitment`, or the exact `A.2.8.PER` results—it only makes “contract talk” classifiable into those objects or claims.
* redefine quadrant semantics (`L/A/D/E`) or cross‑quadrant reference rules; those are defined normatively in A.6.B.

### A.6.C:2 — Problem

How can an author write (or repair) contract-language so that:

1. **Agency is not misattributed** to descriptions (signatures, docs, specs, “interfaces”),
2. **Governance statements** (obligation/recommendation/prohibition commitments and separately governed permission results) are distinguishable from **admissibility gates** and from **semantic laws**,
3. **Operational “guarantees”** become adjudicable via explicit evidence expectations, without smuggling evidence into semantics,
4. **Multi-view publication** (MVPK faces) does not create parallel Contract Bundles or rival canonical claim sets by paraphrase drift?

### A.6.C:3 — Forces

| Force                      | Tension                                                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conversational convenience | People will keep saying “contract”; banning the term is unrealistic.                                                                              |
| Ontological correctness    | “Contract” is a metaphor unless we explicitly locate who promises or commits and what can be evidenced.                                              |
| Boundary diversity         | Software APIs, hardware connectors, protocols, and SLAs share the “contract” word but differ in what is adjudicated and how.                      |
| Multi-view publication     | Faces are necessary for audience fit, but rephrasing easily creates new commitments.                                                              |
| Adjudicability             | “Guarantee” claims must be (i) semantic truths, (ii) exact deontic commitment or permission results, or (iii) evidenced properties—otherwise they are empty rhetoric. |
| Minimality                 | The unpacking should be lightweight enough to apply during routine authoring and review.                                                          |

### A.6.C:4 — Solution

A.6.C introduces a **Contract Bundle** lens for boundary writing. It is not a new foundational entity kind; it is a disciplined way to interpret and rewrite contract-language under A.6.B.

#### A.6.C:4.1 — The Contract Bundle (four positions; deontic position has two direct-result branches)

Whenever a text uses “contract”, “guarantee”, “promise”, “SLA”, or “interface agreement” language, unpack it into four parts:

1. **Promise Content (Promise content)**

   * The promised value or effect (the promise *content*) in the intended scope.
 * In FPF terms (A.2.3), **`U.PromiseContent` is promise content**—a **promise content**, not an execution event (`U.Work`) and not (by itself) an accountable deontic binding (`U.Commitment`).
 * **Prose head rule (normative).** When referring to `U.PromiseContent` in normative prose, authors SHALL use the head phrase **promise content** (or **service offering clause** or **service promise clause**) and SHALL NOT rely on the bare head noun *service*. If the surrounding text also talks about endpoints, systems, and operations, apply **A.6.8** to select facet‑typed phrases (service access point, service delivery system, service delivery work, and so on) rather than collapsing them into “service”.
   * **Recommendation:** give the promise-content a stable local ID (e.g., `SVC-*`) so it can be cited from commitments, gates, evidence, and MVPK faces without paraphrase drift.
 * **Claim-classification discipline:** keep the semantics and definitions of the promised behavior in **L**; express *who is accountable for satisfying the promise* as a **D** claim (`U.Commitment`) that **references** the `U.PromiseContent` (plus any `A-*` and `E-*` claims as needed).

2. **Utterance Package (speech act + published descriptions)**

   * The work occurrence of stating, publishing, or approving (a `U.SpeechAct <: U.Work`, A.2.9) **and** the utterance descriptions it produces or updates (versioned **epistemes** on carriers) that carry the L/A/D/E-classified claim set.
   * A speech act **may** institute or update commitments or strong granted permissions, but only under an explicit context policy that recognizes that `actType` as having the corresponding institutional force.
   * The published utterance descriptions (signature or mechanism descriptions plus MVPK faces) carry L/A/D/E-classified claims. The act is not “the contract”; it is the work occurrence that created or updated the descriptions and, when recognized, instituted the separately represented commitments or granted permissions.
   * **Default interpretation rule (normative).** A conformant boundary model **MUST NOT** infer `U.Commitment` or `GrantedPermissionRelation@Context` occurrences solely from a `Publish` or `Approve` `U.SpeechAct`. Publication creates or updates utterance descriptions and MAY institute publication/status claims (for example, “Published”, “Approved as Standard”, or “Deprecated”), but commitments and strong grants exist only as explicit direct-owner objects under an exact context policy.
   * If a bounded context defines a policy mapping publish or approve act types to deontic effects, the model **MUST** cite that policy. Resulting duties, recommendations-as-duty, or prohibitions **MUST** still be explicit `U.Commitment` objects with accountable subjects; resulting strong permissions **MUST** still be explicit `A.2.8.PER` grant occurrences with their exact beneficiaries and ground.

3. **Deontic governance (commitment and permission kept separate)**

   * Accountable obligations, recommendations-as-duty, and prohibitions (including accountability for satisfying a promise content) are one or more explicit `U.Commitment` records under A.2.8.
   * A strong grant, weak non-prohibition/non-violation finding, actual permission exercise, or permission conflict is an exact `A.2.8.PER` result. It is not stored in `U.Commitment.modality` and is not inferred from a permit carrier or `MAY` token.
   * **Commitment-branch checklist (A.2.8 minimal structure):**
     * `id` (stable; often the `D-*` claim ID),
     * `subject` (accountable role or party; never an episteme),
     * `modality` (the exact A.2.8 `DeonticModalityToken`: `MUST | MUST_NOT | SHOULD | SHOULD_NOT`),
     * `scope` (`U.ClaimScope`) and `validityWindow` (`U.QualificationWindow`),
     * `referents` (by reference or ID: promise content IDs like `SVC-*`, plus `L-*`, `A-*`, `MethodDescriptionRef(...)`, or `PromiseContentRef(...)` as needed),
     * optional `owedTo` (beneficiary or counterparty),
     * optional `adjudication.evidenceRefs` when the commitment is meant to be auditable (point to `E-*`),
     * optional `source` when authority or provenance matters (issuer + instituting `speechActRef` + description reference),
     * optional `notes` for explicitly informative commentary (not part of the binding).
   * **Permission-branch pointer:** cite the exact selected `A.2.8.PER` grant, finding, exercise, non-violation, or conflict object and preserve its own schema, participants, and references; do not reuse the commitment checklist as a generic permission record.
   * A commitment is not “the spec text”: utterance descriptions carry the statement, but the binding is the `U.Commitment` object (A.7 and A.2.8).
4. **Performed work and evidence (Adjudication substrate)**

   * The executed work and observable carriers and traces that can adjudicate whether a commitment was met or whether actual work exercised a grant or was non-violating in the checked frame.
   * This is **E quadrant**: “what evidence is produced, exposed, or retained, under what conditions, and how it is interpreted”.
   * Work is not “the contract”; it is what makes any operational claim testable.
   * In FPF terms, evidence is normally expressed as **carrier-referenced `E-*` claims**, evidence paths, witness relations, or assurance claims governed by `A.10`, `B.3`, or the direct evidence pattern named by value.

#### A.6.C:4.2 — Classification recipe into A.6.B (L/A/D/E)

After unpacking, classify each **atomic** statement using the Boundary Norm Square as defined normatively in **A.6.B** (quadrant semantics + form constraints + cross‑quadrant reference discipline). A.6.C does not redefine `L/A/D/E`; it applies them to contract-language as follows:

* **Promise content → L/A (promise semantics + eligibility).**
  * Put meanings, invariants, and metric definitions for what is promised in **L** (`L-*` in signature laws and definitions).
  * Put “eligible, covered, or valid iff …” predicates as **A** (`A-*` admissibility or gate predicates), not as deontic obligations.
* **Deontic governance → D (which direct result).**
  * Put “MUST, SHALL, or commits to …” statements as **D** (`D-*`), preferably as `U.Commitment` payloads (A.2.8).
  * Put strong/weak permission, exercise, non-violation, and conflict statements as **D** with the exact `A.2.8.PER` result; do not convert them to commitment modality.
  * If compliance requires satisfying or enforcing a gate, the commitment **MUST** reference the relevant `A-*` ID(s) (D→A).
  * If the commitment is meant to be auditable, include evidence hooks by referencing `E-*` (D→E), preferably via `U.Commitment.adjudication.evidenceRefs`.
* **Performed work and evidence → E (how we can tell).**
  * Put observable traces, audit records, measurement windows, and carrier semantics as **E** (`E-*`) with explicit carrier and observation or measurement conditions (A.6.B:5.4).
**Keyword placement rule (canonical claim set).**
Within the canonical L/A/D/E-classified claim set, BCP‑14 norm keywords (RFC 2119 + RFC 8174) and their common synonyms (for example SHALL, REQUIRED, RECOMMENDED, and OPTIONAL) are statement operators, not ontology selectors. `MUST`, `MUST NOT`, `SHOULD`, and `SHOULD NOT` route to `U.Commitment` only when the recovered claim is an accountable duty, recommendation-as-duty, or prohibition. `MAY` and `OPTIONAL` route to `A.2.8.PER` when the recovered claim is strong or weak permission; when they express only mechanism entry, rewrite the claim as an `A-*` predicate. Authors **SHOULD** avoid these keywords in **L/A/E** claims; phrase **L** as definitions or invariants (“is defined as…”, “holds iff…”), **A** as predicates (“is admissible iff…”), and **E** as observable/evidenced properties. If a BCP‑14 keyword or synonym appears in an **L/A/E** claim, it **SHOULD** be rewritten into predicate or definition form or explicitly marked informative before publication.

A helpful rewrite rule:

> First recover what “allowed” asserts: an entry condition becomes an **A** predicate; an actual strong/weak permission, exercise, non-violation, or conflict claim becomes **D** plus its exact `A.2.8.PER` object; an accountable duty to satisfy or enforce a gate becomes **D** plus `U.Commitment`; observable adjudication remains **E**. The keyword alone selects none, and references across these claims follow A.6.B.

#### A.6.C:4.3 — “Guarantee” disambiguation

Treat “guarantee” as ambiguous until classified:

* **Semantic guarantee** → **L** (“by definition or invariant”).
* **Governance guarantee** → **D** (“provider commits or implementer must”).
* **Operational guarantee** → **E** (measured property with evidence expectations; optionally referenced by D as the adjudication target).

If none of these fits, the statement is likely rhetorical and should be rewritten or explicitly marked as aspirational or informative.

#### A.6.C:4.4 — MVPK faces are not second contracts

A contract bundle has one canonical claim set. Publication faces are **views** of that set under viewpoints:

* Faces may **select, summarize, and render** claims for audiences.
* Faces must not **introduce new semantic commitments or permission results** beyond the underlying claim set.
* Any face-level decision-relevant or normative-looking statement **SHOULD** cite the underlying claim ID(s). If it cannot be traced to claim IDs, it **MUST** be explicitly presented as informative commentary.

**Keyword rule (faces).**
If a face contains BCP‑14 norm keywords (RFC 2119 + RFC 8174), including common synonyms such as SHALL, REQUIRED, RECOMMENDED, and OPTIONAL, each sentence MUST project an existing classified claim and cite its underlying claim ID. Duty/recommendation/prohibition projections cite the corresponding `D-*` and `U.Commitment`; permission projections cite the corresponding `D-*` and exact `A.2.8.PER` grant, finding, exercise, non-violation, or conflict result with that object's own participants and references. A face-level `MAY` or `OPTIONAL` cannot manufacture any direct object. If no underlying claim and direct object are traceable, the sentence MUST be rewritten to remove the keyword or moved out of the face.
To avoid keyword‑evasion, equivalent deontic phrasings (e.g., “is required to…”, “is prohibited from…”) SHOULD follow the same trace-by-ID discipline even when no BCP‑14 keyword is present.

Projection may be paraphrased for audience fit, but it **MUST NOT** change the deontic or semantic claim; if exactness is critical or disputed, use verbatim.

This prevents faces from becoming “second contracts” by paraphrase drift.

#### A.6.C:4.5 — Default register: Contract Claim Register (recommended)

Use the **A.6.B Claim Register** (IDs, statements, quadrant, and canonical location). Add two optional columns that make A.6.C auditable without adding new ontology:

* `bundleId: ContractBundleId` (local stable ID grouping the claims that constitute one boundary “contract bundle”)
* `bundlePart ∈ {PromiseContent, Utterance, Commitment, Permission, WorkEvidence}` (the deontic position has two direct-result branches)
* `faceRefs = {PlainView|TechCard|InteropCard|AssuranceLane : …}` (where the claim is rendered)

### A.6.C:5 — Archetypal Grounding (Tell–Show–Show)

#### A.6.C:5.1 — Tell

If you use contract-language for a boundary, do not treat “the interface or specification” as an acting system. Instead:

1. Identify the **promise content** (promise content) being promised,
2. Identify the accountable **Commitment** holder(s) for a duty/recommendation/prohibition branch; when permission is current, identify the exact `A.2.8.PER` grant, finding, exercise, non-violation, or conflict result and preserve that object's own participants and references,
3. Identify the **Utterance** surfaces that publish the boundary (signature or mechanism descriptions plus MVPK views),
4. Identify the **Performed work and evidence** carriers that could adjudicate whether commitments were met or whether actual work exercised a grant or was non-violating in the checked frame,
5. Classify each claim through **L/A/D/E** and reference across quadrants rather than paraphrasing.

#### A.6.C:5.2 — Show (System archetypes)

**(A) Software API boundary**

*Draft wording (contract soup):*
“The Payments API guarantees idempotency. Clients must provide `Idempotency-Key`. We log all requests. Availability is 99.9%.”

**Unpack + classify:**

* **Utterance:** signature or mechanism publication for `PaymentsAPI` (MVPK faces: TechCard, InteropCard).
* **L:** define idempotency and the uniqueness semantics of `Idempotency-Key`.
  (“Idempotent” is a semantic property, not a duty.)
* **A:** admissibility predicate: request is admissible iff `Idempotency-Key` is present and valid.
  (Gate belongs to mechanism.)
* **D:** client implementers are obligated to satisfy the gate; provider implementers are accountable for the idempotency behavior **as defined in L** when the gate holds; provider commits to the availability target (scoped by window and exclusions).
  (Name the committing role; do not say “the API commits”.)
* **E:** evidence expectations: audit and log carriers include request id, idempotency key, rejection reason; availability measurement uses defined window and signal definition.

**(B) Hardware interface boundary**

*Draft wording:*
“The connector guarantees safe operation. Devices must not exceed 20V. Negotiation must succeed before power is applied.”

**Unpack + classify:**

* **Utterance:** published interface spec (pinout, electrical ranges, handshake procedure).
* **L:** electrical invariants and allowable ranges are definitions and invariants (truth-conditional).
* **A:** admissibility predicate: power delivery is admissible only after handshake state reaches an agreed mode.
* **D:** manufacturer or integrator obligations: implement handshake; enforce voltage constraints.
* **E:** evidence: test-report carriers; measurement traces; observable negotiation logs (if exposed), or lab measurements under a declared method.

**(B-PER) Compact permission replay (only when the permission branch is live)**

*Situation:* “ReleaseAuthority approved Operator-A to deploy Release-4711; deployment is allowed after preflight.”

**Unpack + classify:**

* **Utterance and institution:** the dated `Approve` speech-act occurrence `SA-4711`, performed by the exact grantor assignment under current `ReleaseGrantPolicy`, institutes—not merely publishes—the separately represented grant occurrence `PER-4711`. Approval text without that policy and act does not create the grant.
* **D — permission result:** `GrantedPermissionRelation@Context` names beneficiary `RoleAssignmentRef(Operator-A)` and `permittedActionSpecificationRef = U.EpistemeRef(Deploy-Release-4711)`; `SA-4711`, the grantor assignment, policy, context, scope, and window remain ground or qualifiers. If the available basis establishes only current absence of prohibition, record `NonProhibitionFinding@Context` instead and do not promote it to a strong grant.
* **A — independent entry predicate:** “deployment is admissible iff `PER-4711` currently obtains and preflight is green” is an `A-*` predicate. It may consume the grant as one condition but is neither the grant nor proof of gate passage.
* **Work and exercise:** only after later dated actual `U.Work` occurrence `DeployRun-4711` exists, instantiates the action specification, matches the beneficiary branch, and stays inside the grant's scope and window may `PermissionExerciseRelation@Context` bind `WorkRef(DeployRun-4711)` to `U.EntityRef(PER-4711)`. Planned work, the approval wording, and preflight alone are not exercise.
* **E:** speech-act, policy-edition, grant-occurrence, preflight, work, and observation carriers support the classified claims without replacing their direct objects.

#### A.6.C:5.3 — Show (Episteme archetypes)

**(C) Multiparty protocol boundary (behavioural and session-type motif)**

*Draft wording:*
“The protocol guarantees progress. Participants must follow the sequence.”

**Unpack + classify:**

* **Utterance:** protocol description (could be a type spec or protocol spec plus explanatory views).
* **L:** safety and progress properties as laws over the protocol model (truth-conditional, within the theory).
* **A:** admissibility: when an interaction trace is considered valid or admissible (e.g., runtime checks; compilation checks; gating conditions for entering a session).
* **D:** obligations on implementers or operators: implement the protocol; do not send messages outside the allowed state machine; publish conformance records if required.
* **E:** evidence: message trace carriers, conformance test-run records, and audit trails for disputed interactions.

**(D) Socio-technical “SLA + audit trail” boundary**

*Draft wording:*
“Provider shall respond within 4 hours for Severity‑1 incidents. Only Severity‑1 is covered. Evidence is provided by ticket logs.”

**Unpack + classify:**

* **Promise content (service promise clause):** responsiveness promise for a defined incident class and window.
* **Utterance:** SLA publication (and its views for different audiences).
* **A:** admissibility predicate for the promise: ticket qualifies iff severity classification meets stated conditions.
* **D:** provider commitment to meet the target; client duties (e.g., provide required info); auditor duties if applicable.
* **E:** evidence: ticket carriers, timestamps, classification records, and the measurement procedure binding “4 hours” to a time window and clock source.

### A.6.C:6 — Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Ontological and Epistemic**, **Prag**, **Did**. Scope: **Universal** for “contract talk” in boundary descriptions.

* **Gov bias:** prefers explicit accountability and adjudication hooks; increases clarity but adds authoring overhead.
* **Arch bias:** optimises evolvability by preventing hidden coupling (contract soup) across stack layers.
* **Ontological and Epistemic bias:** enforces EntityOfConcern, Description episteme, and carrier separation; discourages “interface-as-agent” metaphors in Tech prose.
* **Prag bias:** accepts that “contract” is common vocabulary; offers a disciplined rewrite rather than prohibition.
* **Did bias:** aims to be teachable via repeated unpacking examples across boundary types.

### A.6.C:7 — Conformance Checklist

A boundary description conforms to A.6.C iff it satisfies all items below:

1. **CC‑A.6.C‑1 (Unpacking when contract-language appears).**
   If the text uses “contract”, “guarantee”, “promise”, or “SLA” language, it **SHALL** explicitly disambiguate the statement as referring to at least one of: **Promise content**, **Utterance** (published description), **Commitment** (duty/recommendation/prohibition), **Permission** (exact `A.2.8.PER` result), or **Performed work and evidence** (adjudication).

2. **CC‑A.6.C‑2 (No agency to epistemes).**
   The text **MUST NOT** attribute promising, committing, or obligating agency to signatures, mechanisms, interfaces, or documents. Any duty or commitment **SHALL** name an accountable role assignment, `U.Role`, or admitted acting system.

3. **CC‑A.6.C‑3 (Classify contract-language statements via A.6.B).**
   Contract-language statements **SHALL** be classifiable as atomic claims to **L/A/D/E**, with dependencies expressed by explicit references rather than paraphrase.

4. **CC‑A.6.C‑4 (Promise content ≠ Work discipline).**
   Statements about what is executed or observed **SHALL** be expressed as **E** claims about work, evidence, and carriers. Promise-content language **SHALL** refer to the **promise content** (`U.PromiseContent`, A.2.3) and its **L-defined** semantics (and to explicit `D-*` commitments represented as `U.Commitment`, A.2.8), not to execution events (`U.Work`) or runtime effects.
   Unqualified head‑noun *service* (and the co‑moving cluster *service provider* and *server*) in normative boundary prose SHALL be unpacked per **A.6.8 (RPR‑SERV)**.

5. **CC‑A.6.C‑5 (Evidence hook for operational guarantees).**
   If a “guarantee” is operational (requires reality to decide), the text **SHALL** include an **E** claim that states what evidence would adjudicate it, with the evidence carrier or evidence claim named when current.

6. **CC‑A.6.C‑6 (No second contracts via faces).**
   MVPK faces **MUST NOT** add new commitments or permission results beyond the underlying L/A/D/E-classified claims; faces may only project, summarize, or select from the canonical claim set under a viewpoint.

7. **CC‑A.6.C‑7 (RFC‑keyword discipline inside faces).**
   If an MVPK face contains BCP‑14 norm keywords, each sentence **MUST** cite the underlying classified claim ID and direct object: `U.Commitment` for duty/recommendation/prohibition or the exact `A.2.8.PER` result for permission. If it cannot, the face is non-conformant until rewritten without the BCP‑14 keyword or moved out of the face.

8. **CC‑A.6.C‑8 (No commitment-by-publication default).**
   A `Publish` or `Approve` utterance, including publication of a `…Spec`, MUST NOT be treated as instituting `U.Commitment` or `GrantedPermissionRelation@Context` by default. If a Context policy maps publication acts to deontic effects, the policy SHALL be cited; every resulting duty/recommendation/prohibition remains an explicit `U.Commitment` with an accountable subject, and every resulting strong grant remains an explicit `A.2.8.PER` relation occurrence with its exact beneficiary and ground.

### A.6.C:8 — Common Anti-Patterns and How to Avoid Them

| Anti-pattern                                        | Why it fails                                                   | Repair                                                                                      |
| --------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Interface-as-promiser** (“the API promises…”)     | Epistemes and publication carriers are descriptions; they do not commit                 | Name the committing role assignment or admitted acting system; classify as a D claim; keep the API, signature, or interface description as description episteme or publication carrier |
| **Guarantee-without-substrate**                     | “Guarantee” is empty unless it is L, D, or E                   | Decide: semantic law (L), exact commitment or permission result (D), or evidenced property (E) |
| **SLA smuggled into laws**                          | Mixes governance with semantics; breaks substitution reasoning | Put SLA targets as D claims referencing L-defined metrics and E evidence                    |
| **Gate written as obligation**                      | Confuses admissibility predicates with duties                  | Write predicate as A; write duty-to-gate as D→A reference                                   |
| **Evidence as prose property** (“document proves…”) | Violates EntityOfConcern, Description episteme, and carrier                            | State evidence as E claims about carriers produced or observed in work                         |
| **Face-level paraphrase drift**                     | Creates multiple incompatible contracts                        | Faces should reference canonical claims; keep commitments and permission results with their direct owners |
| **Cross‑scale contract collapse**                   | Different agents claim incompatible “contracts” at different scales or contexts | Represent each as separate, scoped `D-*` claims with accountable roles or exact permission beneficiaries plus Context; apply `A.2.8.PER` for a grant/prohibition conflict and the exact commitment, conflict, or mediation owner rather than collapsing them into one “contract”. |

### A.6.C:9 — Consequences

**Benefits**

* Category mistakes (“contract soup”) become systematically repairable.
* Commitments become accountable (named roles) and adjudicable (evidence expectations).
* Boundaries remain evolvable: laws, gates, governance, and evidence can evolve with controlled coupling.

**Trade-offs and mitigations**

* Additional authoring effort; mitigated by applying the unpacking only when contract-language appears or when a claim is used for decision or publication.
* Some stakeholders prefer “one sentence contract”; mitigated by MVPK faces that present curated projections while keeping the underlying claim set coherent.

### A.6.C:10 — Rationale

FPF already distinguishes signatures, mechanisms, and work and evidence layers. Contract-language is a high-frequency linguistic entry point that collapses these layers unless a disciplined unpacking is applied.

F.18 may supply durable names for recovered terms when naming is current, but it does not provide the ontology. A.6.C makes the boundary split operational: promise content, speech act or utterance package, deontic commitment or separately governed permission result, performed work, and carrier-referenced evidence as the adjudication basis. This keeps “contract” language classifiable under A.6.B and compatible with MVPK multi-view discipline without relocating ontology into the naming chapter.

### A.6.C:11 — SoTA‑Echoing (informative; post‑2015 alignment)

> **Informative.** Alignment notes; not normative requirements.

* **Adopt — BCP 14 (RFC 2119 + RFC 8174) norm keyword discipline for spec language.** Modern spec-writing practice treats these keywords as a disciplined modality family; A.6.C constrains where such modality belongs (D) versus where predicate-style constraints belong (A or L).
* **Adopt — behavioural and session types for protocol boundaries (post‑2015 practice).** Protocols as typed interactions emphasize separating safety and progress properties (L) from runtime admission (A) and from implementer obligations (D), with trace-based evidence (E).
* **Adopt or adapt — algebraic effects and handlers plus effect systems.** The “operation signature vs handler semantics” split mirrors “utterance substrate vs work and evidence”, preventing execution semantics from being conflated with governing spec refs.
* **Adapt — ISO/IEC/IEEE 42010:2022 viewpoint discipline.** Multi-view publication is treated as viewpoints governing projections; A.6.C applies this to contract talk to avoid face-level semantic forks.

### A.6.C:12 — Relations

* **Uses and is used by**

  * Uses **A.6.B** for L/A/D/E claim classification, atomicity, and cross-quadrant reference discipline.
  * Used by **A.6** cluster conformance (“contract unpacking”) as the detailed, reusable form of that discipline.
  * Complements **A.6.S** (signature engineering): contract unpacking is a common constructor step when turning prose boundaries into publishable signatures.
  * Coordinates with **A.6.P** families: when an RPR pattern touches “contract or guarantee” language, apply A.6.C to avoid category errors. (A.6.C is **not** a specialization of A.6.P; A.6.P is relation‑precision, A.6.C is boundary‑contract disambiguation.)

* **Coordinates with**

  * **A.7** (EntityOfConcern, Description episteme, and carrier) for correct placement of evidence claims.
  * **F.12** (service acceptance) for structuring how promise-level commitments connect to evidence and acceptance windows.
  * **E.17** MVPK “no new semantics” rule to prevent publication faces from becoming new contracts.
  * **A.2.8.PER** for strong/weak permission, exercise, non-violation, and conflict results kept outside `U.Commitment`.

### A.6.C:End

