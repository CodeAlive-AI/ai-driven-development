## A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → A.6.B (matrix module; referenced by A.6 cluster overview)
> **Builds on:** E.8 (authoring template), A.6.0 (`U.Signature`), A.6.1 (`U.Mechanism`), A.6.3 (`U.EpistemicViewing`), E.17.0/E.17 (MVPK + “no new semantics” faces), A.7 (EntityOfConcern and Description-episteme boundary; specification-use and publication-carrier distinction), A.2.3 (promise content when contract language is current), A.2.8 (`U.Commitment`), A.2.8.PER (subject pattern selected by the permission-word branch), A.2.9 (`U.SpeechAct`), E.10.D2 (EntityOfConcern and Description-episteme boundary; specification-use and refinement discipline), E.10 publication face, form, unit, and carrier discipline
> **Purpose (one line):** Provide a canonical four-way boundary-claim classification that classifies boundary statements (L/A/D/E), constrains how each quadrant is written, and defines explicit cross‑quadrant reference rules to support later boundary evolution and audit.

**Use this when.** Use `A.6.B` when boundary wording mixes definitions, runtime entry conditions, generic prescriptions, individual duties or grants, actual work or evaluation results, and evidence.

**First useful move.** Identify what the reader needs to decide or understand about the boundary. Use §4.4 to select the claims and grounds needed for that answer; split mixed claims, classify their jobs, and name consequential dependencies by ID or canonical location.

**What changes in practice.** Laws, gates, governance, and work-and-evidence claims can change without silently changing one another; publication faces reuse the canonical claims instead of restating them.

**Ordinary non-use boundary.** A one-off local sentence with one recoverable logical job still needs the correct quadrant, but it does not need a Claim Register or a separate publication form. Add those only when reuse, decision, audit, or cross-face citation needs them; §6.1 still requires any material dependency to name the claim by ID or canonical location.

### A.6.B:0 — Conventions

**Keywords.** The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **SHALL** have their RFC 2119/8174 meanings only when capitalized as shown.

**Quadrant labels.** This pattern uses the classification labels **L / A / D / E** as *statement quadrants*:

* **L** — Laws & Definitions
* **A** — Admissibility & Gates
* **D** — Deontics & Commitments
* **E** — Work‑Effects & Evidence

These labels are **claim-classification labels for statements**, not MVPK face designators and not pattern identifiers.

**Statement identifiers (recommended).** Classifiable statements **SHOULD** be given stable IDs with a quadrant prefix: `L-*`, `A-*`, `D-*`, `E-*`. Other sections and views **SHOULD** reference these IDs or the canonical claim locations. A faithful explanation may accompany the reference under §6.1.

**Non-collision note (informative).** The `A-*` prefix here is “Admissibility”, not Part-A numbering and not MVPK’s `AssuranceLane` face designator. If this is a readability hazard in your program, prefer an explicit `G-*` (“Gate”) local convention while keeping the quadrant name “Admissibility”. Also avoid introducing single-letter mnemonics for MVPK face designators inside this cluster; spell face designators in full to reduce collisions.

**Atomic claim.** An **atomic claim** is a sentence (or bullet) that performs exactly one logical role and is classifiable under exactly one quadrant. If a sentence mixes roles, it is **not atomic** and **MUST** be split before it can be classified.

**Claim job and adjudication basis.** A quadrant identifies what a boundary claim contributes. Its adjudication basis states how that claim can be settled. Definitions and declared entry predicates are both description content. Generic normative content is recovered from its exact source; an individual duty or grant requires its actual constitutive basis. An occurrence or evaluated-result claim requires the facts specified by its subject predicate.

**Deontic claims.** Writing a `D-*` claim records either generic normative content or a claim about an individual duty, commitment, or grant. When the wording is about permission, use the permission-word branch in §8.4.1 to recover the exact object, what makes it obtain, and the evidence needed before reliance. The instituting act and any compliance finding have their separate claims.

**Modality.** Preserve whether a sentence defines, prescribes, permits, hypothesizes or reports. Use that meaning together with the claim's job under §4; a modal word alone leaves the classification unresolved.

### A.6.B:1 — Problem frame

Boundary descriptions routinely collapse four distinct claim families into “contract soup”: definitions are written as obligations, runtime gates are hidden inside laws, governance talk is assigned to “the interface”, and operational-result “guarantees” are asserted without the actual Work, evaluation, or observation needed to settle them. The resulting boundary is brittle: substitution becomes unclear, and auditability becomes performative rather than adjudicable.

The classification connects the strata already distinguished in FPF: Signature and Mechanism; the EntityOfConcern, claim-bearing episteme and carrier; and views under viewpoints. It lets a reader identify each claim, how it is settled and which other claims its use depends on.

### A.6.B:2 — Problem

When authors cannot reliably answer two questions—

1. “What does this claim contribute: meaning, an admission condition, normative content or a deontic position, or an occurrence/evidence account?”
2. “What grounds are needed to settle this exact claim?”

—then boundary statements drift across layers, faces fork semantics, and “compliance” becomes a matter of interpretation rather than a property that can be checked.

A boundary needs a minimal, stable classification that:

* classifies every **atomic** statement into a unique quadrant, and
* forces any cross‑quadrant dependencies to be **explicitly referenced**, not smuggled by paraphrase.

### A.6.B:3 — Forces

| Force                              | Tension                                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Precision vs readability**       | Predicate‑style constraints reduce ambiguity; narrative helps adoption.                        |
| **Evolvability vs enforceability** | Stable laws should not embed volatile runtime gates; governance still needs enforcement hooks. |
| **Auditability vs simplicity**     | Evidence makes claims adjudicable; evidence also introduces operational design obligations.    |
| **Local meaning vs reuse**         | Boundaries must be local; reuse must be explicit via IDs and references, not duplicated prose. |

### A.6.B:4 - Solution — the Boundary Norm Square

#### A.6.B:4.1 - Four claim jobs and their grounds

The **Boundary Norm Square** distinguishes four jobs in a boundary account. A definition can remain fixed while a gate changes; a duty can obtain while its bearer fails to perform it. An earlier observation may still be valid evidence when a changed admission condition leads to refusal. Establish the observation’s fitness for the new check, then apply that condition to decide admission. Keeping those claims distinct makes their actual dependencies available for a change or audit decision.

Classify what the exact sentence asserts, then establish its grounds. For example, a declared entry predicate belongs in A and the result of applying it to one request belongs in E. A claim that a grant currently permits an action belongs in D; the instituting act, an evaluation of that grant and an actual exercise of it have their own E claims. The predicate definition and the individual claims remain description content, with different subjects and adjudication conditions.

#### A.6.B:4.2 — The square

| Quadrant | Job of the claim | What settles it |
| --- | --- | --- |
| **L — Laws & Definitions** | Defines vocabulary, a semantic constraint, invariant or typing rule. | The declared definition or assumptions and the corresponding inspection, proof, type validation or model reasoning. |
| **A — Admissibility & Gates** | Declares the condition for a mechanism application to enter. | The exact admission rule and its input meanings. A particular application's satisfaction or decision is a separate E claim. |
| **D — Deontics & Commitments** | States generic normative content or a claim about an individual duty or grant. | The exact normative source for generic content; the subject pattern's constitutive conditions and actual basis for an individual relation. |
| **E — Work‑Effects & Evidence** | Reports an occurrence, evaluated finding, observed condition or evidence support. | The actual facts and subject-specific conditions for that claim, with evidence support when the receiving use requires it. |

**Clarification (classify the claim by its job, not by its subject pattern).**

* Classify the exact atomic claim by what its sentence states and by the conditions that let a reader decide it.
* The exact ClaimGraph located through the subject pattern supplies the referenced object's predicate and obtaining conditions; it does not choose the claim's quadrant.
* When permission wording is present, use the single permission-word branch in §8.4.1. It separates the possible jobs of that wording without inventing a common “permission result” kind.

**Normative rule (single quadrant).** Each **atomic** boundary claim **MUST** be assigned exactly one job under L/A/D/E. Recover an unresolved meaning before assigning it. A condition or reference within one coherent claim does not by itself add another asserted claim.

**Normative rule (mixed claims).** A conforming boundary text **SHALL** separate independently asserted claims with different jobs. For example, a duty to enforce an entry rule and a report of one enforcement result have separate D and E claims referring to the A rule. Preserve the logical connection when splitting the wording.

#### A.6.B:4.3 — Canonical placements in the Signature Stack

The quadrants have canonical placements in the boundary stack:

* **L → Signature layer:** `U.Signature.Laws` (and mechanism‑local semantic laws if present).
* **A → Mechanism layer:** `U.Mechanism.AdmissibilityConditions` (entry gates / runtime admissibility predicates).
* **D → Deontics & Commitments layer:** atomic claims about a generic prescription or about one separately obtaining individual duty, recommendation-as-duty, prohibition, or commitment. When permission wording is live, §8.4.1 decides whether its claim also belongs here.
* **E → Work-Effects & Evidence layer:** truth-conditional claims whose satisfaction requires actual work, evaluation, observation, or produced carriers.

A publication face **MUST NOT** introduce new semantic claims outside this L/A/D/E-classified claim set. **E.17 (MVPK)** enforces this rule for publication faces and their selected profiles.

#### A.6.B:4.4 - Develop a boundary explanation for its receiving use

Start with the boundary passage, its available sources and the reader's question. The square helps recover what each claim contributes and what would settle it. The explanation connects the claims needed for the reader to interpret, use or change that boundary.

**1. Recover the question and the claims already made.** Establish which understanding or decision the text must support. Interpreting a metric, deciding whether a request may enter and determining whether a duty was fulfilled need different answers. Recover the draft's asserted content, modality and scope. If a word such as *guarantees* leaves the intended assertion open, use A.6.C:4.3 with the author or source to resolve that meaning. Keep a consequential unresolved meaning explicit until its source is available.

**2. Establish the grounds of the answer.** Split independently asserted jobs and classify them through §§4.1–4.3. Use the detailed procedure and conditional permission-word branch in §8.4.1 where needed. Recover the definition for a meaning claim, the declared predicate for an entry condition, the normative or constitutive basis for a duty or grant, and the facts for an occurrence or finding. Preserve the source's conditions and qualifications. A missing ground requires a targeted return to the source or the responsible practice. If the work calls for a new rule or commitment, develop and establish it through its governing practice before treating it as current boundary content.

**3. Select the claims and detail on which the reader's answer depends.** Work backward from that answer. A reported measurement needs its quantity, population, conditions and interpretation; judging fulfilment of a commitment additionally needs that commitment and its comparison rule. Follow such dependencies until the remaining premises are supplied by the text or by references the intended reader can obtain and understand. Use §6 for their actual relations. Include a detail when changing it could change the answer, when it explains why a step follows, or when the reader needs it to perform the stated use. A complete four-quadrant account is warranted when the question actually crosses all four jobs. Keep other valid claims in their canonical sources for their own uses.

**4. Compose the explanation around that reasoning.** State the answer in the reader's working terms, connect its supporting claims, and make the conditions that limit its use recoverable. Place a definition beside the claim that needs it and an observation beside the inference it supports. IDs or canonical locations preserve material dependencies under §6.1; the accompanying explanation supplies their meaning for this reader. Use a Claim Register or separate Tech and Plain forms when the reuse or publication conditions call for them. Selection and recomposition preserve the source claims; a new semantic constraint first needs its own canonical claim.

**5. Return the text to the reader's work.** Follow the intended interpretation or decision using the explanation. Identify any consequential premise the reader would still have to invent, obtain that premise or state the precise unresolved question, and revise the affected connection. Consider a relevant change of condition: show which claim must be reconsidered and which grounds remain usable. Stop when the text supports the assigned understanding or decision with its actual limits. A later question can require a different selection from the same canonical claims.

The cases in §8.4 show these authoring choices. Their claims about latency, coaxiality and project entry are the material being explained; the reusable operation is selecting and connecting that material for a reader's question.

### A.6.B:5 — Quadrant specifications

This section is the normative “API” of the square: what each quadrant is for, how it is written, and what it must not contain.

#### A.6.B:5.1 — Quadrant L: Laws & Definitions

**Intent.** State truth‑conditional content: definitions, invariants, typing and well-formedness constraints, equational laws.

**Adjudication.** In‑description: can be checked by inspection, proof, type validation, or model reasoning.

**Canonical form.** `Definition:` / `Invariant:` / predicate‑style constraints using “is / iff / for all”.

**Prohibitions.**

* An `L-*` statement **MUST NOT** contain RFC deontic keywords (**MUST, SHALL, SHOULD, or MAY**) as operators inside the law or definition itself.
* An `L-*` statement **MUST NOT** encode runtime gate predicates (those are `A-*`).
* An `L-*` statement **MUST NOT** assert evidence availability or measurement outcomes (those are `E-*`).

**A.7 EntityOfConcern binding.** Identify what the `L-*` definition, invariant,
or typing rule concerns, separately from the episteme carrying the claim. Its
EntityOfConcern need not itself be a description and may be Work.

**Typical dependence.** `A-*` and `E-*` claims may reference `L-*` IDs or canonical locations for vocabulary, metric definitions, and invariants needed for interpretation.

#### A.6.B:5.2 — Quadrant A: Admissibility & Gates

**Intent.** Specify when a mechanism application is admissible: runtime entry predicates, validity gates, and applicability checks that require context or execution environment. An `A-*` predicate may consume a separately established result as one input, but it does not create or settle that result. If the sentence uses permission wording, choose its job with the branch in §8.4.1.

**Applicability and admissibility.** Signature `Applicability` scopes intended use and bounded context; runtime entry predicates belong in `U.Mechanism.AdmissibilityConditions` as `A-*`. If prose says “clients must satisfy the applicability”, first recover whether it means the declared scope or an actual entry condition. State the generic `D-*` prescription, or the independently instituted individual duty, separately and reference the condition it actually requires. Classify that condition as `A-*` only when it is an entry predicate.

**Adjudication.** Inspect the declared entry rule and its inputs to establish the A claim. Evaluate that predicate at mechanism entry or the stated application point to obtain a particular satisfaction or gate-decision result; report that result separately in E.

**Canonical form.** Predicate style, e.g.:

* “A request is admissible iff …”
* `admissible(x) iff P(x)` (conceptual form; no particular syntax is required)

**Prohibitions.**

* An `A-*` statement **MUST NOT** be placed in `U.Signature.Laws`.
* An `A-*` statement **MUST NOT** use RFC deontic keywords as if it were an agent obligation. (It is a gate predicate, not a duty.)
* An `A-*` statement **MUST NOT** claim that evidence exists (that is `E-*`) or that someone must enforce the gate (that is `D-*`).

**A.7 EntityOfConcern binding.** An `A-*` claim concerns the mechanism-entry
predicate: what the mechanism admits, not a client's duty to comply with it.
Keep that predicate distinct from the episteme carrying the claim.

**Required references (explicit).** If an `A-*` predicate relies on defined terms or invariants, it **SHOULD** reference the relevant `L-*` IDs or canonical locations (or at minimum the signature that defines them).

#### A.6.B:5.3 — Quadrant D: Deontics & Commitments

**Intent.** State one atomic deontic claim. A generic prescription states what one exact policy or other normative episteme requires; it does not create an individual duty bearer or commitment occurrence. A claim that one actual System or separately governed party has that duty instead cites one separately obtaining A.2.8 `U.Commitment`. When a sentence sounds permissive, use §8.4.1; only its **Grant or norm** row enters D. Writing the `D-*` sentence neither institutes a relation nor establishes compliance.

**Adjudication.** For a generic prescription, inspect the exact normative source, its applicable rule content, scope, and current edition. For an individual duty, apply A.2.8 to the separately obtaining commitment and its actual basis. The wording itself decides neither obtaining nor compliance.

**Canonical form.** First choose the route. A generic D claim names the normative episteme and the rule content being stated, without inventing an individual bearer. An individual-duty D claim names the actual bearer and exact `U.Commitment`; a system-role kind or assignment may be a rule ground but is neither bearer nor duty. A responsibility claim uses an admitted domain responsibility predicate and its actual participants, or returns its exact missing governor. A permissive-looking word does not by itself select D; use §8.4.1 for the grant route. Examples:

* Generic: “`APIEntryPolicy-v4` requires covered clients to satisfy `A-…`.” No individual commitment is asserted.
* Individual: “Actual bearer `ClientIntegrator-A` has commitment `COM-17` to satisfy `A-…`.”

**Canonical assertion (recommended; lintable).** Use a `CommitmentAssertion` only when an individual-duty claim must be reused or audited. It concerns one exact separately obtaining `U.Commitment` and makes explicit:

* `entityOfConcernRef`, resolving to one exact `U.Commitment` occurrence, and the `D-*` claim ID;
* exactly one actual bearer branch: `dutyBearerSystemRef` or `dutyBearerPartyRef`;
* non-empty exact `dutyReferentRefs` and any actual counterparties;
* the A.2.8 `DeonticModalityToken`, scope, and validity window;
* the exact current constitutive policy, individualizing rule, and actual instituting basis required by that rule; and
* evidence-claim or carrier references only when the receiving reliance or adjudication needs them.

The assertion states and supports a claim about the relation. Its fields, publication, and evidence do not make the relation obtain.

**Prohibitions.**

* A generic `D-*` statement **MUST NOT** invent an individual bearer or commitment; name its exact normative source and rule content. An individual-duty `D-*` statement **MUST NOT** use “the system, service, interface, or specification” as a vague subject; name the actual duty-bearing system or separately governed party and exact `U.Commitment`, with an assignment only when the constitutive rule uses it as a ground. Use `A.6.C` when ambiguity in promise, utterance, approval, guarantee, or agreement-like boundary wording changes the claim's interpretation or use.
* A `D-*` statement **MUST NOT** give a referenced `L-*` or `A-*` predicate a different meaning. It **MUST** reference that predicate by ID or canonical location when its meaning depends on it; a faithful explanation may accompany the reference.
* A `D-*` statement **MUST NOT** pretend that a duty, commitment, or grant is a law or that writing the claim makes it obtain.

**A.7 EntityOfConcern binding.** A generic `D-*` claim episteme concerns the exact normative rule content it states. An individual `D-*` claim concerns the exact duty, commitment, or grant named by its content and does not substitute for that object. When permission wording is live, the branch in §8.4.1 names the subject pattern and the obtaining or non-obtaining test.

**Required references (explicit).**

* If a `D-*` claim states a prescription or duty to comply with a gate, it **MUST** reference the relevant `A-*` ID(s) or canonical location(s).
* If a `D-*` statement is meant to be auditable, it **SHOULD** reference the `E-*` claim(s) that provide evidence and the carrier classes involved.

#### A.6.B:5.4 — Quadrant E: Work‑Effects & Evidence

**Intent.** State an actual occurrence, evaluated finding, observed condition or evidence-support claim. Settle it from the actual work, evaluation, observation, or carrier conditions required by its predicate.

**Adjudication.** From actual work, evaluation or observation under the claim’s subject predicate. A record can support that judgment through its evidence relation; its presence alone does not settle the claim.

**Canonical form.** Write the ordinary result first, then make recoverable only what settles it:

1. the exact predicate and object that the claim concerns;
2. the participants, work or evaluation occurrence, scope/window, comparison frame, and other conditions required by that predicate; and
3. the evidence or source-use relation and its carrier only when a gate, plan, audit, or assurance decision relies on that support. A carrier may support the claim but does not create the work, effect, or finding.

When permission wording is current, use the branch in §8.4.1 for the exact occurrence or finding, its failure test, predicate, and subject-pattern locator; do not repeat that subject-question catalogue here.

**Prohibitions.**

* `E-*` statements **SHOULD NOT** use RFC deontic keywords; they report adjudicable results rather than obligations.
* An `E-*` statement **MUST NOT** hide a gate predicate; gate predicates are `A-*`.
* For a claim about a particular dated Work, first recover each actual performer through A.13 and let A.15.1 independently admit the Work. Ordinary metonymy is usable when the capable performer remains recoverable; an interface, record or publication does not supply a performer merely by being named. Add an A.2.1 assignment reference and F.6 only when this claim or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither the assignment nor the performer, and missing or failed F.6 leaves the Work intact. If a duty or commitment is also claimed, express it separately in `D-*`.

**A.7 EntityOfConcern binding.** An `E-*` claim episteme concerns the exact work effect, evaluated finding, evidence relation, or carrier condition named by its predicate. A record or carrier is a separate object and becomes the concern only when its existence or condition is itself the claim.

**Required references (explicit).**

* If the result depends on an entry predicate, the `E-*` statement **SHOULD** reference the relevant `A-*` claim. If it depends on an actual gate decision, reference the separate `E-*` claim about that A.21 decision result.
* If another object is needed to settle the predicate, reference that object's subject pattern without importing its quadrant.
* If evidence is used for reliance, recover the independently established support or evidence-use relation and its basis through A.10; use G.6 when an addressable provenance path is needed. Carrier presence alone is not support.

### A.6.B:6 — Cross‑quadrant link discipline

The square also makes dependencies between claims inspectable. A material dependency **MUST** be explicit by claim ID or canonical location.

#### A.6.B:6.1 — Explicit reference rule

If a claim’s meaning materially depends on another L/A/D/E-classified claim, that dependency **MUST** be represented as an explicit reference to its ID or canonical location. A faithful restatement may explain the referenced content; it does not define an alternative rule.

A reader can then follow the explanation back to its governing claim and reconsider dependent uses when that claim changes.

#### A.6.B:6.2 — Canonical cross‑quadrant dependency patterns

These patterns are valid (and common). The square becomes operational when these links are used systematically.

##### A.6.B:6.2.1 - (D → A) Prescription-or-duty-to-gate linkage

When governance says that a gate must be satisfied or enforced:

* generic `D-*`: “`Policy-P` requires covered subjects to satisfy or enforce `A-*`”; or
* individual `D-*`: “Actual bearer `S` has commitment `C` to satisfy or enforce `A-*`.”

This separates **what is admissible** (A) from generic normative content and any separately instituted individual duty (D). If responsibility is also claimed, state its admitted direct domain predicate or exact missing governor rather than inferring it from the duty.

##### A.6.B:6.2.2 - (E → A) Evidence-for-gate linkage

When a claim reports actual observability of a gate decision:

* `E-*`: “For the stated rejection or acceptance due to `A-*`, carrier `C` was produced or observed under conditions …”

This separates **gate semantics** (A) from the **actual observation or result** (E).
A prescription to produce or retain a carrier belongs in D; an expectation or
plan alone supplies no actual E result.

##### A.6.B:6.2.3 - (D → E) Prescription-or-duty-to-evidence linkage

When governance prescribes evidence production, retention, exposure, or a
measured property and a separate `E-*` claim states the related result:

* generic `D-*`: “`Policy-P` requires covered subjects to retain or expose carrier class `C` used by `E-*` …”; or
* individual `D-*`: “Actual bearer `S` has commitment `CMT` to meet the criterion evaluated by `E-*` under the stated exclusions …”

This separates a **generic prescription or individual duty** (D) from its **adjudication** (E).

##### A.6.B:6.2.4 - (A/E → L) Semantic grounding linkage

When a gate predicate or measurement relies on definitions or invariants:

* `A-*` / `E-*` references `L-*` that define terms or metrics.

This prevents “metric drift” and “definition drift” across views.

##### A.6.B:6.2.5 - (D → L) Governance-to-definition linkage

When a generic prescription or individual obligation relies on precise term or metric meanings:

* `D-*` references `L-*` that define the terms or metrics it uses.

This keeps governance text from accidentally redefining semantics in prose.

##### A.6.B:6.2.6 - (A → D/E) Normative or evaluated input to a gate

When entry depends on a current grant or a separately established finding, reference that exact D or E claim and state how its subject enters the predicate. For example, `A-CAL-01` in §8.4.5.4 requires the grant stated by `D-CAL-01` to cover the plan and time, together with the required conflict finding. The grant, finding and entry decision retain their own obtaining conditions. A changed input reopens the admission evaluation that consumed it.

#### A.6.B:6.3 — The “triangle decomposition” for mixed sentences

**Normative rule (decomposition).** A conforming boundary text **SHALL** decompose
any mixed sentence into its actual claim jobs. Recover the predicate and modality
of an observability clause before assigning its quadrant. The triangle applies
when the source states all three:

* **A:** admissibility predicate (`A-*`)
* **D:** generic prescription or individual-duty claim referencing the gate (`D-* → A-*`)
* **E:** actual observation or result referencing the gate, with carriers when needed (`E-* → A-*`)

Keep a prescription or individually instituted duty to produce evidence in D.
Preserve an expectation or plan as such; leave the actual E result absent until
its basis exists. This repairs mixed validity, authorization, compliance, audit,
and security claims without manufacturing a third claim.

#### A.6.B:6.4 — Ground each dependency

Reusable laws retain their declared meaning, while an admission predicate can consume a normative position or an evaluated result. For each material link, state what it supplies: meaning, an input condition, an evaluation target or evidence support. Settle each depended-on claim under its own rule.

These are cross-quadrant restrictions. They do not prohibit same-quadrant
references, such as `L-* → L-*` or `E-* → E-*`.

**Normative rule (dependency grounds).**

* `L-*` claims **MUST NOT** depend on or reference `A-*`, `D-*`, or `E-*` claims (except for purely informative notes explicitly marked informative).
* An `A-*` claim **MAY** reference a `D-*` claim for the normative content, duty or grant used by its entry predicate, and an `E-*` claim for a separately established finding or observation. It **MUST** identify the actual input and required scope or currentness under §5.2; deciding that entry is permitted still requires the predicate to be satisfied. `A-*` may reference `L-*` for defined terms or invariants.
* An `E-*` claim **MAY** reference a `D-*` claim as its evidence target or to identify the norm, duty, or grant used by its evaluation. The `E-*` result **MUST** still satisfy its own predicate and the actual-work, evaluation, or observation requirements of §5.4; the `D-*` claim alone establishes no result or compliance. (`E-*` may also reference `A-*` for conditioning and `L-*` for metric or term meanings.)
* `D-*` claims **MAY** reference `L-*`, `A-*`, and `E-*` claims when needed, and **SHOULD** do so by ID or canonical location rather than restating content.

**Rationale (informative).** The L restriction keeps the reusable definition or law independent of a particular gate application, deontic claim or observation. Expose a varying policy or state as a declared parameter; bind it where the particular condition or claim uses it. A and D may refer to one another for different reasons: a duty can require enforcing a gate, while that gate consumes a separately obtaining grant. Examine those reasons rather than treating every reference as one ordering relation. A grant justified only by a gate result that itself assumes that grant would leave both claims ungrounded. Evidence and results may report on normative claims or evaluate conduct against them under their own predicates.

### A.6.B:7 — Mini-register: Claim Register (informative, recommended)

A Claim Register is a drift‑control device that lists every classifiable statement verbatim with classification metadata. It is not a new meaning authority.

| ID | Quadrant | Statement (verbatim) | Canonical location (section or publication unit) | Stack layer | A.7 primary layer | viewRef | viewpointRef | References | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Guidance (informative):
* The **Statement** cell should contain the normative text as authored (copied by value), not a paraphrase.
* **Canonical location** should point to the one place the statement “lives” (e.g., `Signature.Laws`, `Mechanism.AdmissibilityConditions`, `TechCard.NormsCommitments`, `Evidence.Carriers`), so other faces can cite its ID or canonical location.
* **Stack layer** should be one of `{Signature, Mechanism, Norms-and-commitments, Evidence-and-carriers}` to make classification auditable.
* **A.7 primary layer** identifies the claim's EntityOfConcern, with its kind
  when needed. The concern may itself be a Description episteme or publication carrier;
  it remains distinct from the episteme carrying the claim.
* **viewRef** and **viewpointRef** are used when the corresponding view or viewpoint identity matters under E.17; `U.View` membership requires E.17.0 conformance.
* Use **References** for explicit cross‑quadrant links: for example, which `D-*`
  states a requirement or individual duty to enforce which `A-*` predicate, which
  `E-*` reports the result or evidence used to adjudicate which commitment, and
  which `L-*` defines a metric used by `E-*`. Add external standards or policies
  where applicable.

### A.6.B:8 - Archetypal Grounding (Tell–Show–Show)

> **Informative.** Examples for learning the square; they do not add requirements beyond A.6.B:10.

#### A.6.B:8.1 - Tell (universal rule)

Decomposing every normative statement into atomic claims, classifying each under
exactly one quadrant of the Boundary Norm Square, and expressing cross‑quadrant
dependencies by claim ID or canonical location rather than paraphrase supports
later boundary evolution and audit.

#### A.6.B:8.2 - Show #1: Effect signature vs handler (post‑2015 effect systems)

An effect interface declares operations; handlers supply computation behavior. To describe a deployed service using that interface, recover the additional semantic, admission, normative and observation claims that its use needs:

* **L:** defines the operation vocabulary and the semantic laws required of this service's realizations.
* **A:** defines when the operation is admissible (runtime guard predicates).
* **D:** states who must enforce guards and what the provider commits to (operator and implementer duties; SLAs).
* **E:** ties “what happened” to observable carriers (traces, logs, metrics, and events) so commitments can be adjudicated.

The square prevents accidentally writing handler obligations as laws or treating observability as a definition.

#### A.6.B:8.3 - Show #2: ML evaluation protocol boundary (reproducibility discipline)

A published “evaluation protocol” boundary (common in modern ML governance) benefits from strict classification:

* **L:** metric definitions and invariants (e.g., what counts as AUROC; data partition invariants).
* **A:** admissibility gates (dataset usage-term constraints; pinned environment constraints; seed policy).
* **D:** checker and author duties (publish required faces; use declared dataset version; retention duties for run evidence carriers).
* **E:** admitted system `EvaluationRunner-A` performed `MLProtocolEvaluation-T1 : U.Work` over `Model-M1`, `Dataset-D7`, the pinned environment and seed policy, and evaluation window `T`; the exact AUROC metric application declared by the L claim returned `AUROCResult-T1` with `measuredAUROC=0.91`. When a checker, gate, or audit decision relies on that result, an A.10 evidence-provenance path links it to exact carriers `RunLog-T1`, `DatasetHash-D7`, `EvaluationReport-R1`, and `TraceSet-T1`.

The square keeps “must use dataset vX” (D) separate from “evaluation is admissible iff dataset usage terms match” (A), and both separate from “`MLProtocolEvaluation-T1` returned `AUROCResult-T1(measuredAUROC=0.91)`” (E). The report and log carriers may support reliance on that result; producing a carrier is not the measured result.

#### A.6.B:8.4 — Worked Rewrite Kit (informative, recommended)

> **Informative.** These cases apply the authoring method in §4.4 and the rules for atomicity, L/A/D/E classification, explicit references, triangle decomposition and grounded dependencies. Use the case whose receiving question matches the present work. If anything here conflicts with A.6.B, **A.6.B is authoritative**.

##### A.6.B:8.4.0 - Goal

For the receiving question established in §4.4, recover the meaning of a boundary sentence that mixes “laws / gates / duties / evidence” and produce:

1. **atomic L/A/D/E-classified claims** (L/A/D/E),
2. **explicit references by claim ID or canonical location** (no paraphrase duplication),
3. **a readable recomposition** (separate Tech and Plain forms when their readers need them),
4. **a minimal anti-pattern lint** (things we reject / flag).

##### A.6.B:8.4.1 - Micro-procedure (Atomize → Classify → Triangle → Link → Bind References → Recompose)

Use this procedure to recover and express the claims selected through §4.4. The permission-word branch below supplies the detailed distinctions when permissive wording matters to that answer.

**Step 1 — Atomize.** Split mixed prose into atomic claims; each must classify to exactly one quadrant.

**Step 2 — Classify (L/A/D/E).**

* **L** if the claim is **truth‑conditional** and adjudicable *in‑description* (inspection, proof or type validation, or model reasoning **over declared assumptions**): definitions, invariants, typing and well-formedness constraints.
  **Guardrails:** `L-*` MUST NOT (i) use RFC deontic keywords as operators, (ii) encode runtime entry predicates (those are `A-*`), or (iii) assert evidence existence or measurement outcomes (those are `E-*`).
* **A** if it declares a **gate predicate**: what the mechanism admits at application time (“admissible iff …”). State the condition as a predicate; a duty to satisfy or enforce it is a separate D claim.
  **Guardrails:** `A-*` SHOULD be written in predicate form and MUST NOT (i) use RFC deontic keywords as if it were an agent obligation, (ii) claim that evidence carriers exist (that is `E-*`), or (iii) assign responsibility or enforcement (that is `D-*`).
  *(Do not confuse this with `Signature.Applicability`: applicability scopes intended meaning and intended use; it is not a runtime entry gate.)*
* **D** if the exact atomic statement states either a generic prescription or an individual duty, recommendation-as-duty, prohibition, or commitment. A permissive sentence enters D only through the **Grant or norm** row below.
  **Guardrails:** a generic claim names the exact normative episteme and applicable rule content without inventing an individual relation. An individual-duty claim names its actual bearer and exact separately obtaining A.2.8 commitment. A grant claim instead follows the participant and ground test in the **Grant or norm** row. A system-role kind or assignment may be a rule ground but is neither bearer nor deontic relation. Writing any claim does not make its object obtain.
* **E** if it reports an actual occurrence, evaluated finding, observed condition or evidence support under §5.4. A claim stating the normative content or obtaining duty or grant itself follows D; an evaluation or occurrence concerning it has its separate E claim.
  **Predicate-specific minimum:** name the exact `E-*` predicate and object, then the actual work, evaluation, or observation, scope/window, comparison frame, and other settling conditions that this predicate needs. Add an evidence or source-use relation, carrier/schema, viewpoint, or consumer only when the receiving gate, plan, audit, assurance, or other reliance decision depends on that support.
  **Guardrails:** `E-*` SHOULD NOT use RFC deontic keywords and MUST NOT hide a gate predicate (that is `A-*`). A reference to `D-*` follows §6.4: identify the evidence target or normative evaluation input, then establish the E result under its own predicate.
  *(If the source sentence is “Role SHALL measure, retain, or expose …”, first decide whether it is a generic prescription about an exact system-role kind or a claim about one actual bearer. Classify either as **D**, but assert an individual commitment only on the second route.)*

**Step 3 — Triangle decomposition.** Recover the observability clause's predicate
and modality under §6.3. Use the A/D/E triangle only when the source states an
entry condition, a generic prescription or individual duty, and an actual
observation or result:

* **A**: the condition under which the mechanism admits this application,
* **D → A**: which exact policy prescribes keeping or enforcing the predicate, or which actual bearer has that separately instituted duty; any responsibility relation is stated separately under its direct domain predicate
* **E → A**: the actual observation or result and, when needed, the evidence or
  traces used to adjudicate the predicate.

A requirement to produce or retain evidence stays in D. Preserve an expectation
or plan without inventing an actual E result.

**Permission-word branch (use only when the sentence sounds permissive).** Choose the row by the job the sentence performs, not by the word *may*, *approved*, *authorized*, or *permitted*.

| Branch | Ask this plain question | Square result | Subject pattern and what closes the row |
|---|---|---|---|
| **Grant or norm** | Does the sentence state a generic prescription, claim that one actual bearer has an individual duty, or tell a named beneficiary which action is permitted and under what conditions? | **D** | Use `A.2.8` for the generic-prescription or individual-duty route; only the individual route cites one separately obtaining commitment. For a grant use `A.2.8.PER`: name the exact grant occurrence, beneficiary, action, scope/window, and policy-valid A.2.9 act with its performer and assignment; confirm current policy conditions and absence of valid revocation or supersession; cite evidence needed before reliance. |
| **Gate predicate or result** | Does the sentence state the mechanism condition for entry, or claim one actual `A.21` decision for a bounded action? | **A** for the entry predicate; **E** for the actual decision result | Keep the mechanism predicate as its own `A-*` claim. For an actual decision, use one separate `E-*` claim naming the exact `GateDecisionResult`, bounded action, applicable profile application, complete required `GateCheckApplicationResult` set, scope/window, `decisionValue`, action consequence, and recheck condition. A grant, finding, or conflict is only an input; neither the predicate nor the result creates or resolves it. |
| **Actual exercise** | Did this dated Work match the named grant's action and beneficiary while that grant was in force? | **E** | Use `A.2.8.PER PermissionExerciseRelation@Context`: name the Work, grant occurrence, performer and the beneficiary-matching ground, scope and interval. Cite an assignment or on-behalf-of relation when that match depends on it. A failed match means that exercise relation does not obtain. |
| **Weak evaluation or non-violation** | Did an evaluation of a current, sufficiently complete normative frame find no applicable prohibition before action, or no violation in the actual Work? | **E** | Use `NonProhibitionFinding@Context` or `NonViolationFinding@Context`, its frame, subject/action or actual Work, scope and window. Name a separate evaluation Work only when a dated evaluation occurrence is claimed or required by the receiving use. A stale or incomplete frame returns `unresolved`. |
| **Conflict** | Do a current grant and norm cover the same case, and has a rule or authorized decision actually selected the outcome? | **E** | Use `A.2.8.PER PermissionNormConflictFinding@Context`. Cite the applicable selecting rule or the admitted system's authorized dated decision Work and current resolution result; otherwise keep the finding `unresolved`. |
| **Source or display only** | Does the sentence only say that a permit, badge, registry entry, message, or carrier exists, displays, or evidences something? | **E** for an observed carrier/evidence claim; **L** for its definition | Use A.10/G.6 for evidence and the applicable publication or carrier pattern. A visible or published item is not itself a grant, exercise, finding, or resolution. |

Choose one row. If one sentence answers two questions, split it before classification. If the sentence is not permission-like, do not use this branch. The branch classifies claims and selects existing subject patterns; it creates no `permission result` umbrella. Use the filled case in §8.4.5.4 when a concrete model is needed; point back to that case rather than adding another pattern list.

**Guideline.** Keep the gate predicate separate from the observations and results used to evaluate it. Write the predicate in `A-*`; state an actual observation or result in `E-*` and reference the gate when the result concerns its application (`E → A`). An `A-*` predicate may consume a separately established result under §5.2; express a material dependency by reference under §6.1. That reference does not establish the result or a gate decision.

**Step 4 — Link by ID or canonical location.** Apply the
cross-quadrant restrictions in §6.4, including its explicitly informative-note
exception for L references to A/D/E. Same-quadrant references remain available.

**Common link motifs (informative).** Boundary rewrites use `D→A`, `E→A`, `D→E`, `A/E→L`, and `D→L`; `A→D/E` supplies a stated gate input, while `E→D` identifies an evidence target or normative evaluation input under §6.4.

**Step 5 — Bind references (minimal A.7 discipline).**

* Place **L** claims in `Signature.Laws` (and mechanism-local semantic laws if present), and **A** claims in `Mechanism.AdmissibilityConditions`.
* Bind a generic **D** claim to its exact normative episteme and applicable rule content. Bind an individual-duty **D** claim to its actual duty-bearing System or separately governed party and exact `U.Commitment`; cite an assignment only when the constitutive rule uses it as a ground. State responsibility and authority, when claimed, through their own admitted direct relations or exact missing governors. Prefer ID or canonical-location references rather than restating `L-*` or `A-*` content.
* Bind each **E** claim first to its exact predicate/object and to the actual work, evaluation, observation, scope/window, comparison frame, and other conditions that settle that predicate. Add a carrier/schema, evidence or source-use relation, viewpoint, and consumer only when a receiving reliance decision depends on them; a claim about a carrier's own existence or condition names the carrier as its object.

**Optional drift-control.** Add each L/A/D/E-classified claim verbatim to a Claim Register row (A.6.B:7) with its canonical location and references when this helps maintain faithful faces.

**Step 6 — Recompose into readable text.**
Select the source claims and supporting detail needed for the receiving question
under §4.4. Include only the claim classes present in the source. Use separate
Tech and Plain forms when their readers need them; both may also serve as a
teaching aid.

* **Tech recomposition**: a short **L/A/D/E-classified claim bundle** listing the
  present claims and their ID or canonical-location references.
* **Plain recomposition**: a one-paragraph narrative that *summarizes* the bundle
  and cites its claims (**no new semantics**). If you need a new constraint, add a
  new atomic L/A/D/E-classified claim to the canonical source before publishing it
  in Plain.

##### A.6.B:8.4.2 - Anti-pattern (quick)

* **AP-1 Unestablished operational-result guarantees.** An asserted operational
  result lacks the actual Work, evaluation, or observation needed to settle it.
  If the guarantee's L/A/D/E meaning is ambiguous, use `A.6.C:4.3` to recover it.
* **AP-2 Unresolved duty bearer.** “The API promises” is used for an individual duty without a recoverable bearer and independently obtaining commitment; use A.6.C when the intended meaning remains ambiguous.
* **AP-3 Gate-as-evidence.** Treating the gate predicate (A) as if it were an observation (E).
* **AP-4 Gate-as-law.** Entry predicates as signature “laws or definitions” (L) instead of `A-*`.
* **AP-5 Unresolved qualifier.** “Fast”, “secure”, “approved” or “aligned” leaves the relevant predicate, criterion or relation unrecoverable.
* **AP-6 Paraphrase drift.** Restating L/A content in D or E with changed meaning (instead of citing by ID or canonical location).
* **AP-7 Deontics in predicates.** RFC keywords (“MUST, SHALL, and related RFC keywords”) used as operators inside `L-*` or `A-*` predicates (should be `D-*` that references `L-*`/`A-*`).
* **AP-8 View-fork semantics.** Recomposition/face text introduces new `L/A/D/E` meaning not present in the L/A/D/E-classified claim set (violates “no new semantics” discipline).
* **AP-9 Applicability-as-gate.** Using `Signature.Applicability` (intended use) as a substitute for `A-*` runtime admission predicates.

##### A.6.B:8.4.3 - Example 1 — Software engineering (SLO-ish API latency)

###### A.6.B:8.4.3.1 - Draft sentence (non-conformant)

> “This API guarantees p95 latency < 200ms.”

###### A.6.B:8.4.3.2 - Atomize + Classify (L/A/D/E)

The draft leaves open whether *guarantees* states a target, an obtaining duty or an observed result. The author first recovers the receiving question: the service reader wants to know what the dated evaluation established about latency. Recover the measurement definition, admitted operating envelope, actual evaluation and evidence support from the named sources. These are additional premises of this constructed case; the draft alone leaves them unresolved.

**Explain the dated measurement.** Under steps 2–3 of §4.4, the observed value requires its computation meaning, operating conditions and actual basis. The author therefore selects these claims:

**L-API-01 (Definition).**
`p95_latency(window W, population P, unit U, method M)` is defined as … (formal measurement definition).
*(Lives in Signature.Laws or a referenced measurement definition pack.)*

**A-API-01 (Gate predicate: admissibility).**
In this expanded case, the evaluation mechanism admits assessment of “p95 < 200ms” only under its declared load profile, deployment region, sampling method and window. Its entry predicate is:
`AdmissibleLatencyClaim := (region=US) ∧ (concurrency≤X) ∧ (payload≤Y) ∧ (W=5m) ∧ (M=HDRHistogram@v…) ∧ (P=requests that match filter F)`
*(References L-API-01 for definition.)*

**E-API-01 (Evidence / carriers).**
For `LatencyEvaluation-T1` over `Γ_time=[t1..t2]`, actual carriers `TraceBatch-T1`, `Histogram-H1`, `DashboardSnapshot-D1`, and `SamplingConfiguration-S1` were produced or observed under the operating and sampling conditions in `A-API-01`, using the metric and computation definition in `L-API-01`. An A.10 evidence-provenance path links those exact carriers to `LatencyEvaluation-T1` and its `LatencyResult-T1`.
*(References `A-API-01` and `L-API-01` for the operating conditions and metric definition.)*

**E-API-02 (Observed value claim).**
For interval `Γ_time = [t1..t2]` under conditions pinned to `A-API-01` and using carriers in `E-API-01`, `LatencyEvaluation-T1` produced `LatencyResult-T1` with observed `p95_latency = 173ms` (computed per `L-API-01`).
*(References A-API-01, L-API-01 and E-API-01.)*

**Return to the measurement question.** The author writes: “During `[t1..t2]`, the observed p95 latency was `173ms` under the operating and sampling conditions in **A-API-01**, using the definition in **L-API-01** and the evaluation evidence in **E-API-01** (**E-API-02**).” This connects the value to the conditions under which the reader can interpret it. The endpoint declaration and duty bearers do not change this bounded measurement answer. If the reader asks about another region or sampling method, return to the applicability of **A-API-01** and the basis of the corresponding evaluation.

**Changed question: explain the service assurance arrangement.** The reader now needs the interface being covered, who owes the latency performance, who must publish incident notes and how the supporting evidence remains available. The author recovers the declared interface and the separately obtaining commitments. Those premises select the following additional claims; their inclusion follows the new question:

**L-API-02 (Interface signature).**
The API endpoints and parameters are as declared (including parameter passing discipline / units).
*(Signature-level structure.)*

**D-API-01 (Commitment).**
Admitted service-maintaining system `ServiceOperations-A` is the actual duty bearer of separately obtaining `LatencyCommitment-API-01 : U.Commitment`; under that commitment it SHALL meet `p95_latency < 200ms` when `A-API-01` holds, adjudicated per `L-API-01` using the carriers and observation conditions in `E-API-01`.
*(References L-API-01 and A-API-01 by ID; does not restate them.)*

**D-API-02 (Operational duty).**
Admitted operations system `SRE-A` is the actual duty bearer of separately obtaining `IncidentNoteCommitment-API-02 : U.Commitment`; it SHALL publish incident notes when `LatencyCommitment-API-01` is violated and SHALL avoid claiming compliance outside `A-API-01`.
*(References D-API-01 and A-API-01 by ID.)*

**D-API-03 (Duty-to-evidence linkage).**
Admitted telemetry-maintaining system `TelemetryOperations-A` is the actual duty bearer of separately obtaining `TelemetryRetentionCommitment-API-03 : U.Commitment`; it SHALL retain or expose the actual carriers referenced in `E-API-01` for the audit window required by policy.
*(References E-API-01 by ID.)*

###### A.6.B:8.4.3.3 - Triangle decomposition (explicit)

For that assurance question, the author uses §6 to connect the declared condition, the duties and the actual observations. Each link explains one dependency of the assurance account:

* **A-API-01** is “the predicate”.
* **D-API-01 → A-API-01** states the commitment under the gate or envelope.
* **E-API-01 → A-API-01** binds adjudication (carriers used to decide the gate or commitment).
* **D-API-03 → E-API-01** expresses retention and exposure obligations for those carriers.

###### A.6.B:8.4.3.4 - Readable recomposition

The broader assurance question uses the following selection. The earlier measurement answer remains sufficient for its narrower question. A changed commitment requires reconsidering the duty and compliance conclusion while retaining an applicable measurement and its grounds.

**Tech recomposition (L/A/D/E-classified claim bundle, short):**

* `L-API-02` identifies the covered API endpoints and parameters.
* `L-API-01` defines p95 latency computation.
* `A-API-01` specifies when the latency claim is admissible.
* `D-API-01` states the commitment under that envelope.
* `E-API-01` lists adjudicable carriers and conditions used to adjudicate `A-API-01`.
* `D-API-02` states the operational incident-note duties.
* `D-API-03` states the retention and exposure duties for carriers in `E-API-01`.
* `E-API-02` reports observed performance under `A-API-01` for `Γ_time=[t1..t2]`.

**Plain recomposition (one paragraph, readable):**
“For the API endpoints and parameters declared in **L-API-02**, the latency target uses the p95 definition in **L-API-01**, and the mechanism admits its evaluation only under operating envelope **A-API-01**. `ServiceOperations-A` has the latency duty stated in **D-API-01**. Adjudication uses the telemetry carriers listed in **E-API-01**; `TelemetryOperations-A` has the retention duty in **D-API-03**, and `SRE-A` has the incident-note duty in **D-API-02**. Under that envelope, the observed p95 over `Γ_time=[t1..t2]` was `173ms` (**E-API-02**).”

##### A.6.B:8.4.4 - Example 2 — Mechanical engineering (fit / coaxiality)

###### A.6.B:8.4.4.1 - Draft sentence (non-conformant)

> “This fit ensures coaxiality.”

###### A.6.B:8.4.4.2 - Atomize + Classify

First recover which assertion *ensures* is meant to express. In this constructed case, a reader initially needs to interpret the geometric requirement at the shaft–bushing boundary. The author obtains the declared datum, tolerance and measurement convention, then uses steps 2–3 of §4.4 to select the two definitions that make that requirement interpretable:

**L-FIT-01 (Definition).**
`coaxiality` is defined relative to a declared base axis and measurement method (datum scheme, instrument, tolerance zone).
*(Truth-conditional: “what it means”.)*

**L-FIT-02 (Interface and boundary structure).**
The boundary relation involves shaft, bushing, datum axis, tolerance class, temperature window, assembly procedure class.
*(Signature-level arity recovery / slots.)*

**Return to the interpretation question.** The author writes: “Interpret the coaxiality requirement for the shaft–bushing boundary using its declared datum scheme, measurement method and tolerance zone (**L-FIT-01**), with the participants and applicable temperature and assembly conditions in **L-FIT-02**.” The reader can now locate what the geometric requirement means. A measured claim about a particular lot needs a further answer.

**Changed question: determine what was established for lot L123.** The author obtains the evaluation rule and the dated measurement facts. The admissible process envelope and actual evaluation connect the geometric meaning to this lot. Their source recovery supplies the next three claims:

**A-FIT-01 (Gate predicate).**
In this expanded case, the evaluation mechanism admits assessment of the coaxiality claim only when manufacturing and assembly satisfy the declared process envelope: material batch, temperature window, tool calibration validity, surface finish class and alignment procedure version.
*(Gate predicate; can be checked using evidence, but is not itself evidence.)*

**E-FIT-01 (Evidence carriers).**
For `CoaxialityEvaluation-L123` over lot `L123` and `Γ_time=[t1..t2]`, actual carriers `CMMReport-L123`, `CalibrationCertificate-C7`, `AssemblyLog-L123`, `TemperatureTrace-L123`, and `DatumSchemePin-D4` were produced or observed. An A.10 evidence-provenance path links those exact carriers to `CoaxialityEvaluation-L123` and its `CoaxialityResult-L123`.
*(References `A-FIT-01` and `L-FIT-01`; avoids RFC deontics.)*

**E-FIT-02 (Observed).**
For lot `L123` and window `Γ_time=[t1..t2]`, under conditions pinned to `A-FIT-01` and using carriers in `E-FIT-01`, `CoaxialityEvaluation-L123` produced `CoaxialityResult-L123`: measured coaxiality was within tolerance zone `T` (interpreted per `L-FIT-01`).
*(References A-FIT-01, L-FIT-01, and E-FIT-01.)*

The resulting account states: “For lot `L123` during `[t1..t2]`, the evaluation under **A-FIT-01** found coaxiality within tolerance zone `T`, interpreted through **L-FIT-01** and supported by the carriers in **E-FIT-01** (**E-FIT-02**).” If the datum scheme changes, the author reopens the interpretation and fitness of the measurement for that scheme. The earlier finding retains its stated datum and conditions.

**Further question: explain the production and evidence duties.** A reader arranging release and later reliance also needs to know who is bound to maintain the process envelope and retain its evidence. Recovering the separately obtaining commitments supplies these additional claims:

**D-FIT-01 (Duty).**
Admitted production-engineering system `ProcessEngineer-A` is the actual duty bearer of separately obtaining `ProcessEnvelopeCommitment-FIT-01 : U.Commitment`; it SHALL ensure `A-FIT-01` holds for the production lot and SHALL not release the lot for use when `A-FIT-01` is false.
*(References A-FIT-01.)*

**D-FIT-02 (Duty-to-evidence linkage).**
Admitted quality-engineering system `QualityEngineer-A` is the actual duty bearer of separately obtaining `FitEvidenceRetentionCommitment-02 : U.Commitment`; it SHALL retain or expose the carriers referenced in `E-FIT-01` for the production lot.
*(References E-FIT-01 by ID.)*

###### A.6.B:8.4.4.3 - Readable recomposition

For this broader question the author connects the definition, admissibility, duties and observation. This selection lets the reader distinguish what the lot evaluation established from what each duty requires.

**Tech bundle:**

* Meaning of coaxiality: `L-FIT-01`.
* Boundary arity and participants: `L-FIT-02`.
* When the claim is admissible: `A-FIT-01`.
* Who has the process-envelope duty: `ProcessEngineer-A` under `D-FIT-01`.
* What we observe and keep as carriers: `E-FIT-01` and measured outcome `E-FIT-02` (with retention duty `D-FIT-02`).

**Plain paragraph:**
“In this expanded case, ‘ensures coaxiality’ is made precise by fixing the definition and datum scheme (**L-FIT-01**) and by making the boundary participants explicit (**L-FIT-02**). The mechanism admits this coaxiality evaluation only under the declared manufacturing and assembly envelope (**A-FIT-01**). `ProcessEngineer-A` has the process-envelope duty stated in **D-FIT-01**. `QualityEngineer-A` has the evidence-retention duty in **D-FIT-02**. Compliance is adjudicated using the measurement and process carriers listed in **E-FIT-01**; for lot `L123` over `Γ_time=[t1..t2]`, the observed coaxiality was within tolerance **E-FIT-02**.”

##### A.6.B:8.4.5 - Example 3 — Management (project “approved or aligned”)

###### A.6.B:8.4.5.1 - Draft sentence (non-conformant)

> “The project is approved.”

###### A.6.B:8.4.5.2 - Atomize + Classify

With only the draft, ask which approval is claimed and which subsequent action the reader needs to decide. Here the question is whether the project may start execution. Recover the sponsor-approval definition, entry predicate, four actual check-application results and evidence path from the named sources. These additional premises let the author connect the prerequisite meanings to a current entry decision. The separately obtaining coordinator duty is needed for the broader question of who is bound to maintain this arrangement; it is also supplied in the constructed case below.

**L-PRJ-01 (Definition).**
For this case, the project-entry policy defines `RequiredProjectApproval(project)` as sponsor sign-off on the identified project. Risk-review completion, budget availability and staffing are separate prerequisites.

**A-PRJ-01 (Gate predicate: stage entry).**
For starting execution work, `ExecutionAdmissible(project)` holds iff `RequiredProjectApproval(project)` and the required prerequisites are satisfied: risk review completed, budget line exists and key roles staffed.
*(This is the real “may start work” entry predicate; it references L-PRJ-01 for what counts as approvals. If “approved” is meant as permission rather than gate evidence, use the permission-word branch in §8.4.1. An approval registry entry or evidence carrier alone remains source/display evidence and is not a grant.)*

**D-PRJ-01 (Duty).**
Admitted project-coordination system `ProjectCoordinator-A` is the actual duty bearer of separately obtaining `ProjectEntryCommitment-PRJ-01 : U.Commitment`; it SHALL not initiate execution unless `A-PRJ-01` holds, SHALL keep the approval registry current, and SHALL retain or expose the evidence carriers referenced in `E-PRJ-02`.
*(References A-PRJ-01 and E-PRJ-02 by ID.)*

**E-PRJ-01 (Gate decision result).**
At `Γ_time=snapshot(t)`, `ProjectEntryGateResult-P-t : GateDecisionResult` has `gateRef=ProjectEntryGate-P`, `decisionSubjectRef=ProjectEntryClaim-P-t`, `boundedActionRef=StartExecution-P`, and `profileApplicationRef=ProjectEntryProfileApplication-P-t`. That application of `ProjectEntryProfile-v3` uses the complete required set `{ApprovalCheck-P-t, RiskReviewCheck-P-t, BudgetCheck-P-t, StaffingCheck-P-t} : GateCheckApplicationResult[]`; each exact application reports its checked subject and criterion, has `sourceOutcome=satisfied`, and maps to `pass`. The result records `decisionValue=pass`, action consequence “start `StartExecution-P` within the admitted project-entry window”, the project-entry scope and window, and recheck on any changed approval, risk-review, budget, staffing, profile, scope, or window.
*(This actual `E-*` result applies the inputs named by `A-PRJ-01`; it is neither the `A-*` predicate nor performed execution Work.)*

**E-PRJ-02 (Evidence for reliance).**
For reliance on `E-PRJ-01`, the exact observed carrier set is `{DecisionRecord-R7, MeetingMinutes-M3, BudgetLine-B4, StaffingAssignments-S2, GateChecklistSnapshot-G9}`. An A.10 evidence-provenance path links those carriers to the four exact `GateCheckApplicationResult` values and `ProjectEntryGateResult-P-t`. `GateChecklistSnapshot-G9` displays the result; its presence alone establishes neither a check result nor the gate decision.
*(References `A-PRJ-01` and `E-PRJ-01`; avoids RFC deontics.)*

###### A.6.B:8.4.5.3 - Readable recomposition

**Answer the entry question.** The author uses **L-PRJ-01** and **A-PRJ-01** to interpret the prerequisites, **E-PRJ-01** for the actual decision and **E-PRJ-02** for the support needed before reliance. The answer is: “At snapshot `t`, the project-entry decision is `pass`, allowing `StartExecution-P` within the stated window (**E-PRJ-01**, supported by **E-PRJ-02**). Recheck when a prerequisite or the decision's profile, scope or window changes.” A changed budget check returns the reader to the affected admission decision. The definition of sponsor approval remains usable.

**Explain the wider arrangement when requested.** Adding **D-PRJ-01** answers who has the project-entry and registry-maintenance duties. The following recomposition addresses that wider question:

**Tech bundle:**

* The required sponsor approval is defined by `L-PRJ-01`; risk review, budget and staffing remain separate prerequisites.
* “May start execution” is a gate predicate: `A-PRJ-01`.
* `ProjectCoordinator-A`'s project-entry duty: `D-PRJ-01`.
* The actual A.21 gate result is `E-PRJ-01`; its bounded A.10 evidence support is `E-PRJ-02`.

**Plain paragraph:**
“In this expanded case, the required sponsor approval has the meaning defined in **L-PRJ-01**. Together with the separate risk-review, budget and staffing prerequisites, it supplies the inputs to the entry predicate **A-PRJ-01**. `ProjectCoordinator-A` has the project-entry and registry-maintenance duties stated in **D-PRJ-01**. At snapshot `t`, the current A.21 profile application maps every required check-application result to `pass`; **E-PRJ-01** records `decisionValue=pass` with the action consequence ‘start `StartExecution-P` within the stated window’, and **E-PRJ-02** supplies the evidence path for reliance on that result.”

###### A.6.B:8.4.5.4 - Filled permission case (each sentence classified)

Apply §4.4 to each receiving question in this case. To explain the current grant, connect its instituting basis **E-CAL-01** to **D-CAL-01**. For an entry decision, also recover the entry predicate and the actual decision with its applicable inputs. A question about whether the technician used the grant selects **E-CAL-02–03**; later compliance and renewed entry require their own findings below. The detailed permission branch in §8.4.1 explains these selections. Preserve the distinct claims so a later question can use its own grounds.

**E-CAL-01 (Instituting communicative Work).** Admitted system `MaintenanceCoordinator-A` performed dated `CalibrationGrantAct-17 : U.SpeechAct` under `MaintenanceCoordinator-A@DayShift`; that obtaining assignment has the system as holder and covers the act. In this filled case, `CalibrationGrantPolicy-v4` does not require a separate authority relation, so none is asserted. The assignment supplies no authority and performs no act. `CalibrationGrantAct-17` satisfies the policy in `PlantCalibrationContext` and is the actual instituting Work. A policy variant that does require grant authority must cite one exact obtaining authority relation under its direct predicate or stop at `missing-governor[grant authority]`.

**D-CAL-01 (Grant position).** `MaintenanceCalibrationGrant-17 : GrantedPermissionRelation@Context`, instituted by `CalibrationGrantAct-17`—the actual speech act stated in `E-CAL-01`—permits beneficiary `MaintenanceTechnicianSystemRole` to run `CalibrationProcedure-v3` in Zone 8 during `ServiceWindow-17`. `CalibrationGrantPolicy-v4` remains current, the grant still covers that system-role kind, procedure, zone, and window, and no valid revocation or supersession has ended this occurrence; this `D-*` claim records the grant but does not institute it.

**A-CAL-01 (Gate predicate).** `CalibrationEntryAdmissible(plan, checkTime)` holds only if `MaintenanceCalibrationGrant-17` is current for the plan's beneficiary, action, zone, and time and no applicable permission/norm conflict finding is `unresolved`. The predicate takes those inputs; it creates neither the grant, a conflict result, nor an actual gate decision.

**E-CAL-02 (Actual Work and actor).** Through its A.13 core, admitted system `Tech-17` is the exact actual performer for this case under obtaining assignment `Tech-17@Shift-B`, whose holder is `Tech-17` and whose extent covers the early part of `ServiceWindow-17`. A.15.1 independently admits dated `CalibrationWork-17B : U.Work` from that performer, its Method, extent, and containing-System facts. Because this filled case expressly claims precise assignment-bound attribution, F.6 separately relates `CalibrationWork-17B` to that same assignment. The assignment neither acts nor identifies the performer; failed attribution would leave the Work intact and remove only the under-assignment claim.

**E-CAL-03 (Optional exercise claim).** Because this case asks whether the grant was used, `CalibrationExercise-17B : PermissionExerciseRelation@Context` connects `CalibrationWork-17B` to `MaintenanceCalibrationGrant-17`: the Work instantiates `CalibrationProcedure-v3`; `Tech-17@Shift-B` is an assignment occurrence whose declared species uses `MaintenanceTechnicianSystemRoleKindDomain` as its assigned-kind domain, and the occurrence supplies `MaintenanceTechnicianSystemRole` as the value admitted by that domain; and the Work occurs in Zone 8 within `ServiceWindow-17` while the grant is current. If the action or beneficiary test failed, this exercise relation would not obtain.

**D-CAL-02 (Exercise non-use boundary).** The authoring rule says to add `E-CAL-03` only when the reader needs to know whether the grant was exercised; otherwise stop with the separately named grant and Work. This is a generic prescription for boundary text, not a claim that one particular author bears an individual `U.Commitment`.

**E-CAL-04 (Later non-violation finding).** Through its A.13 core, admitted system `ComplianceEvaluator-4` is the exact actual performer under obtaining assignment `ComplianceEvaluator-4@QualityShift`. A.15.1 independently admits dated `CalibrationComplianceEvaluation-17B : U.Work`; because this finding expressly preserves precise assignment-bound attribution, F.6 separately relates that Work to the same assignment. The Work checked `CalibrationWork-17B` against current `PlantCalibrationNormativeFrame-17`, explicitly complete enough for this technician, procedure, zone, and evaluation window, and returned `CalibrationNonViolation-17B : NonViolationFinding@Context(result=nonViolating)`. A stale or insufficient frame would return `unresolved`; a missing or failed F.6 relation would instead leave the Work and evaluation result intact while removing only the attribution.

**E-CAL-05 (Evidence for reliance).** An A.10 evidence-provenance path links the exact `CalibrationNonViolation-17B` finding to `CalibrationComplianceEvaluation-17B`, `ComplianceEvaluator-4@QualityShift`, `CalibrationRunLog-17B`, the log's source and currentness relations, and the bounded audit context. The path supports reliance on the finding; the log, assignment, and path do not perform the evaluation or create its result.

**E-CAL-06 (Unresolved conflict).** After `CalibrationWork-17B` and its evaluation, `Zone8EntryProhibition-17` becomes current for the same beneficiary, action, zone, and the remaining service window, including the calibration action specified by `CalibrationWorkPlan-17C`; no applicable rule selects an outcome and no authorized dated decision Work with a current resolution result exists. `CalibrationConflict-17 : PermissionNormConflictFinding@Context` therefore remains `unresolved`.

**E-CAL-07 (Source/display fact).** `SignedGrantRecord-17` and `GreenPermitTile-17` are visible carriers in this case; their presence is an observed source/display claim only.

**E-CAL-08 (Gate decision result).** At the later entry check, `CalibrationEntryResult-17C : GateDecisionResult` has `gateRef=CalibrationEntryGate-17`, `decisionSubjectRef=CalibrationWorkPlan-17C`, `boundedActionRef=StartCalibrationProcedure-v3-in-Zone8-17C`, and `profileApplicationRef=CalibrationEntryProfileApplication-17C`. The current profile application uses the complete required set `{CalibrationGrantCurrentCheck-17C, CalibrationConflictResolvedCheck-17C} : GateCheckApplicationResult[]`: the current-grant application maps to `pass`, while the exact `CalibrationConflict-17=unresolved` source outcome maps to `block`. The result records `decisionValue=block`, action consequence “hold `CalibrationWorkPlan-17C` outside entry”, the remaining Zone 8 service scope and window, and recheck when the grant, conflict result, profile, scope, or window changes. It neither resolves the conflict nor revokes `MaintenanceCalibrationGrant-17`.

**L-CAL-01 (Tempting wrong classification, rejected).** “The visible permit is D, so the grant exists, the Work exercised it, and the Work was non-violating” is not one atomic claim and is false as a classification shortcut. The carrier observation is `E-CAL-07`; the grant, exercise, evaluation finding, and `E-CAL-08` gate result remain the separately classified claims above.

##### A.6.B:8.4.6 - A compact recomposition aid

Select the source claims needed for the receiving question through §4.4. Cite
claim IDs or canonical locations. For a measurement account, connect the value
to its definition, conditions and actual basis; for an entry answer, connect the
entry rule to its evaluated inputs and current decision. Use the broader forms
below when the question also needs the normative arrangement and its evidence.
Use separate Tech and Plain forms when their readers need them.

###### A.6.B:8.4.6.1 - Tech register

> “This boundary claim is defined by **L-…** and applies only under **A-…**. **D-…** states either the exact generic prescription or the separately instituted duty of **[actual bearer]**. **E-…** states the observed or evaluated result for `Γ_time=…`; add its evidence support when the receiving use needs it.”

###### A.6.B:8.4.6.2 - Plain register

> “We mean **[short label]** in the sense of **L-…**, and use it only when **A-…** holds. **D-…** either states what the named policy requires or, when an individual duty was separately instituted, names its actual bearer. **E-…** states the observed or evaluated result for the declared interval; add its evidence support when the receiving use needs it. If responsibility is also claimed, cite its direct relation separately.”

### A.6.B:9 — Bias‑Annotation

Scope: **Universal** for boundary descriptions.

* **Arch bias:** favors explicit separation and explicit references; mitigated by allowing narrative faces while keeping commitments classified and referenced by ID or canonical location.
* **Gov bias:** makes actual duty bearers and duties explicit (D) and auditability explicit (E); mitigated by keeping evidence conceptual and carrier-referenced rather than tool-specific. Responsibility, when claimed, remains a separate direct relation.
* **Ontological and epistemic bias:** distinguishes the EntityOfConcern, claim-bearing episteme and carrier, and requires the actual basis for work, evaluation or observation claims. Cross-quadrant references preserve their connections in a readable account.

### A.6.B:10 — Conformance Checklist

| ID                                       | Requirement                                                                                                                                                                                                      | Purpose                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **CC‑A.6.B.1 (Atomicity).**              | A conforming boundary text **SHALL** decompose mixed sentences into **atomic claims** such that each atomic claim belongs to exactly one quadrant **L/A/D/E**.                                                    | Makes L/A/D/E classification unambiguous; prevents contract soup.       |
| **CC‑A.6.B.2 (Quadrant classification).** | Each atomic claim **MUST** be classified by its job under §4 and have its own adjudication basis recovered, rather than taking a quadrant from its subject-pattern family. When permission wording is present, the single branch in §8.4.1 **MUST** select the claim's job before assigning L/A/D/E. | Prevents one pattern catalogue from replacing the square's decision. |
| **CC‑A.6.B.3 (Form and obtaining constraints).** | `L-*` and `A-*` claims **MUST NOT** use RFC deontic keywords as operators. A generic-prescription `D-*` claim **MUST** name its exact normative source and applicable rule content without inventing an individual occurrence; an individual-duty `D-*` claim **MUST** name its actual bearer and exact separately obtaining `U.Commitment`; a grant `D-*` claim **MUST** satisfy §8.4.1. No claim text makes its relation obtain. Responsibility uses its direct predicate or exact missing governor. An `E-*` claim **MUST** name the work, evaluation, or observation that settles it and any evidence used for reliance. | Keeps normative content, individual institution, responsibility, and evaluated results distinct. |
| **CC‑A.6.B.4 (Explicit references).** | Where a claim materially depends on another L/A/D/E-classified claim, that dependency **MUST** be expressed by explicit ID or canonical-location reference. An accompanying explanation must preserve the referenced meaning. | Makes the governing claim recoverable across layers and faces. |
| **CC‑A.6.B.5 (E‑claim adjudicability).** | Each `E-*` claim names its exact predicate and object plus the actual work, evaluation, or observation, scope/window, comparison frame, and other conditions required to settle that predicate. It adds an evidence/source-use relation, carrier/schema, viewpoint, and consumer only when the receiving reliance decision depends on that support. | Makes work-effects adjudicable without forcing unrelated carrier apparatus into every result claim. |
| **CC‑A.6.B.6 (No gate smuggling).**      | Operational admissibility predicates **MUST NOT** appear as `L-*` laws in the signature layer; they **MUST** be `A-*` claims in the mechanism layer.                                                             | Preserves substitution and signature stability.          |
| **CC‑A.6.B.7 (Dependency grounds).** | `L-*` claims **MUST NOT** reference `A-*`, `D-*`, or `E-*`, except for purely informative notes explicitly marked informative. An `A-*` reference to `D-*` or `E-*` **MUST** meet §6.4's input and scope/currentness conditions. An `E-*` reference to `D-*` **MUST** meet §6.4's evidence-target or evaluation-input rule and **MUST NOT** treat the D claim alone as an E result. | Keeps reusable laws stable and makes gate inputs and evaluation grounds explicit. |

### A.6.B:11 - Common Anti‑Patterns and How to Avoid Them

| Anti‑pattern                 | Symptom                                            | Why it fails                                                | Repair (square‑consistent)                                                                  |
| ---------------------------- | -------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Gate‑as‑law**              | Preconditions written as “laws”                    | Collapses signature or mechanism boundary; breaks substitution | Move to `A-*` in Mechanism.AdmissibilityConditions; reference `L-*` terms.                  |
| **Deontics in predicates**   | “MUST” inside definitions or gates                 | Confuses governance with truth or admissibility                | Rewrite the definition or gate as `L-*`/`A-*`; add a generic `D-*` prescription or an independently established individual-duty claim when current. |
| **Unresolved duty bearer** | “The API promises” is used for an individual duty without its actual bearer and commitment | The institutional claim cannot be settled from the interface wording | Recover the policy and generic prescription, or the actual bearer and separately obtaining `U.Commitment` when an individual duty is claimed. Keep measured property (`E-*`) and metric definition (`L-*`) separate; use `A.6.C` when ambiguity changes interpretation or use. |
| **Unestablished operational-result guarantees** | An asserted p95 result lacks its actual evaluation | The operational-result claim lacks the basis needed to settle it | Use `A.6.C:4.3` when the guarantee's meaning is ambiguous. For an operational result, state the actual Work, evaluation, or observation, predicate and object, scope/window, and result; if that basis is absent, leave the result unestablished. Add A.10 support and a `D-* → E-*` link only when the receiving reliance and duty claims need them. A carrier-existence observation alone does not complete the measured claim. |
| **Paraphrase drift** | A restatement changes the governing rule | Different faces can then imply different conditions or consequences | Reference the claim ID or canonical location and repair the explanation to preserve its meaning; use a Claim Register when useful. |
| **View‑fork semantics**      | A face introduces new L/A/D/E content              | Violates “no new semantics” publication discipline          | Put any new boundary claim in its canonical source before publishing it on a face. Mark explanatory commentary informative when it adds no boundary semantics.                  |

### A.6.B:12 — Consequences

| Benefits                                                                                                     | Trade‑offs / mitigations                                                                         |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Stable modular boundaries.** Laws don’t accidentally become gates; governance doesn’t masquerade as truth. | Requires writers to split sentences; mitigated by the triangle decomposition pattern.            |
| **Explicit adjudication links.** Duties and claims about results can identify the evaluations and evidence relevant to their use. | Establishing that basis has a cost; require only the support the receiving use consumes. |
| **Recoverable meaning across faces.** References connect an explanation to its governing claim. | More cross-references; a Claim Register can help when the claim set needs persistent reuse. |

### A.6.B:13 — Rationale

Boundary changes need different comparisons. Changing an admission condition affects which applications can enter; changing a normative rule affects what is required or granted; changing an implementation can affect the result while leaving both declarations intact. The four claim jobs keep these questions and their connections recoverable. A.6:4.7 explains how to use them for a change decision.

The classification is an authoring convention, with one job assigned to each atomic claim. Modality and adjudication help recover that job, but neither supplies a two-way partition of every claim. In particular, A predicates are declarations, and an individual D claim requires actual constitutive grounds. The practical benefit comes from exposing the different grounds and preserving their dependencies across uses and publication faces.

For a small boundary, ordinary atomic prose and its existing contract or policy can be sufficient. Claim IDs, a register and additional faces earn their cost when several uses need to refer to the same content or follow a consequential change. Keep the direct subject conditions available in either form.

### A.6.B:14 — Source contributions

A.6:11 gives the exact source contributions and their limits. Effects and handlers distinguish declared operations from handler semantics; contract and behavioral-subtyping work supplies preservation questions; session types supply protocol-specific conditions. ISO/IEC/IEEE 42010 supports concern-oriented descriptions and correspondences. OpenTelemetry and SRE distinguish the observations available from the service property being examined; Cedar gives an explicit rule-evaluation and decision construction.

FPF uses these contributions to organize boundary claims. The four jobs, their FPF placements and §6.4's dependency rules are the construction explained here. In particular, provider duties require their governing normative source or individual instituting basis, and evidence support uses A.10. A source's typing or telemetry guarantees retain their own stated scope.

### A.6.B:15 — Relations

* **Used by A.6 and A.6.C:** supplies the canonical matrix and cross-quadrant link discipline. Both consumers classify each exact atomic claim by predicate and adjudication, keep the claim episteme separate from its EntityOfConcern, and use the §8.4.1 branch only when permission wording is live.
* **Constrains A.6.0 (`U.Signature`):** enforces that `L-*` laws are truth‑conditional and do not include admissibility predicates.
* **Constrains A.6.1 (`U.Mechanism`):** places admissibility in `AdmissibilityConditions` (`A-*`) and classifies actual results and evidence claims as `E-*`, adding carrier references when their use requires them.
* **Requires A.7:** identifies each claim's EntityOfConcern separately from the
  episteme carrying it. The concern may itself be a Description episteme or
  publication carrier.
* **Interacts with MVPK/E.17:** faces are projections that cite L/A/D/E-classified claims and mint no new semantics. When the permission-word branch is selected, its row names the subject pattern and obtaining or failure test; A.6.B only classifies the statement, and neither wording nor a carrier makes the referenced object obtain.

### A.6.B:15a - Probe-coupled boundary claim classification

When boundary text says that an interaction changes the state represented by its
output, identify the interaction, the changed state, and the receiving use, then
classify the atomic claims through the same L/A/D/E square. Such interactions may
include asking a question, measuring or intervening through a metric, reading a
dashboard, conducting a workshop, exporting through a Bridge, or making an API
read. Probe-coupled boundary language does not create a fifth quadrant.

Action classification:

1. Copy the boundary sentence being used for a decision.
2. Split it into its atomic claims before judging it, retaining only the classes
   present in the source: definition or law, runtime admissibility, generic
   prescription or individual duty, work effect or evaluated result, and any
   separate evidence-support claim.
3. Give each atomic claim its quadrant and any identifier required by a later reference.
4. Put the state, probe, update, or export part in the quadrant where it belongs rather than treating "quantum-like boundary" as one claim.
5. Apply `A.6.P` when a relation or its participants remain unclear; use `F.18` only when recovered terms
   need durable names. Use `A.10` for needed evidence support, `B.3` for a named
   assurance question, `C.16` for measurement, and `F.9` for a Bridge question.
   Use `C.26.1` for the residual probe-coupled question only when the interaction
   participates in the represented state and its output is being used as a
   passive read or export despite that decision-relevant effect.
6. Use a Claim Register when the claim set needs persistent reuse, dispute resolution or cross-face citation; otherwise keep the atomic prose.

For a local working note, atomize the sentence mentally and write one or more
atomic L/A/D/E-classified sentences, preserving every source claim. One sentence
suffices only when one logical job remains. Use the Claim Register when the claim
set must survive reuse or dispute; the phrase "quantum-like boundary" is not a
substitute for its separate claims.

| Quantum-like boundary phrase hides | Claim class | What the user writes |
| --- | --- | --- |
| The term, variable, state, frame, or relation being defined | `L-*` law or definition claim | Definition or invariant, without agent obligation language |
| When a mechanism admits use of a probe, metric, question, or bridge at the decision point; declaration-level intended-use scope remains in `Signature.Applicability` | `A-*` runtime-admissibility claim | Entry predicate, required current inputs, non-admitted outcome, and neighboring-pattern continuation |
| What exact policy prescribes about applying, retaining, exposing, or avoiding overuse of the probe result; or which actual bearer has that individually instituted duty; and, if separately claimed, who bears responsibility | generic `D-*` prescription or individual `D-*` claim about one exact `U.Commitment`; separate direct responsibility claim or missing governor | Exact normative source and rule content for the generic branch; actual duty bearer and referenced L/A/E claim IDs or canonical locations for the individual branch; responsibility predicate and participants only when that relation independently obtains |
| The actual work effect or observed before-state or after-state, plus any separate evidence relation or carrier used for reliance | `E-*` work-effect or evaluated-result claim; separate evidence-support claim when current | Exact predicate and object, actual Work, evaluation, or observation, conditions and window, and result; use A.10 to recover the independently established support relation and exact carrier only when a receiving use relies on that support |

Useful outputs:

- a Claim Register when persistent reuse, dispute resolution or cross-face citation needs it;
- one or more atomic L/A/D/E-classified sentences preserving every source claim
  for a local working note;
- an ordinary A.6.B L/A/D/E-classified claim set when no probe-coupled
  state-reading question remains;
- the `C.26.1:4.2` decision and finish result for a residual probe-coupled question
  that meets the activation condition above;
- the evidence-support, assurance, measurement, or Bridge result or continuation
  required by `A.10`, `B.3`, `C.16`, or `F.9` for the corresponding current question.

Do not write "the boundary is quantum-like" as one claim without L/A/D/E classification. Identify the interaction and its receiving use, split and classify the claims,
then apply the `C.26.1` activation condition above to any remaining question.

### A.6.B:End
