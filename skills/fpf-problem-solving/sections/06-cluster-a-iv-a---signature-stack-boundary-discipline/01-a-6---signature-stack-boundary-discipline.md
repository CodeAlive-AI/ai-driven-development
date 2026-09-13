## A.6 - Signature Stack & Boundary Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Mixed (normative only where explicitly marked; claim-classification semantics live normatively in A.6.B)
> **Placement:** Part A → A.6.\* (cluster overview; coordinates A.6.0 / A.6.1 / A.6.3 / A.6.B / A.6.5 / A.6.6 / A.6.7)
> **Builds on:** A.6.B for claim classification, A.6.0 and A.6.1 for declaration boundaries, A.7 for subject/description/carrier distinctions, and E.17.0/E.17 for view membership and publication.
> **Purpose (one line):** Keep boundary claims evolvable by classifying each statement under the right layer of the Signature Stack and the right quadrant of the Boundary Norm Square (A.6.B).
>
> **Local terminology:** “Signature Stack”, “Boundary Discipline Matrix”, and “Claim Register” name authoring aids. **L/A/D/E** classify statements; they are not MVPK face designators or pattern IDs.
>
**Canonical companion.** The square itself (quadrant definitions, form constraints, and cross‑quadrant dependency discipline) is specified normatively in **A.6.B — Boundary Norm Square**. This overview only (i) maps quadrants onto the Signature Stack, and (ii) explains how MVPK faces project the canonical L/A/D/E-classified claim set. If anything in this overview conflicts with A.6.B, **A.6.B is authoritative**.

**Use this pattern when.** Use A.6 when a boundary package, API, protocol, contract, compliance statement, SLO/SLA, connector, interface, or publication boundary mixes definitions, admissibility predicates, duties, evidence, and work effects into one account.

**What goes wrong if missed.** Boundary prose starts doing too many jobs at once: invariants are read as permissions, permissions as duties, evidence as gate passage, and publication faces as the governed boundary object.

**What this buys.** The project gets an L/A/D/E-classified claim set with source references and stack placement. Material dependencies name the source claim by ID or canonical location, so work, reliance, evidence, commitment, and gate uses can return to their subject patterns; publication faces cite the same claims.


**First output.** One or more atomic L/A/D/E-classified claims, with stack placement and references for material dependencies.

**Boundary-claim activation discipline.** Use only as much claim-classification structure as the live work claim or reliance claim requires. Split a statement only where one sentence carries more than one claim kind, `relationFunctionClaimRef` or `authoritySourceRef`, or work or reliance consequence, or where evidence, gate, duty, assurance, work occurrence, P2W class, admissible work, or admissible reliance would otherwise remain ambiguous. For a local first-pass repair, ordinary atomic prose suffices; a two-to-four-row scratch table may help. Use a persistent Claim Register when stable claim references are needed for reuse, publication, audit, release, cross-context use, or reliance by `A.15`, `A.10`, `B.3`, `A.21`, `A.20`, `A.2.8`, `A.2.8.PER`, `A.2.9`, or `A.15.1`. Do not atomize ordinary modifiers when one `relationFunctionClaimRef` or `authoritySourceRef` and one work or reliance consequence are already clear.

**Typical neighboring subject patterns and authority-reference repairs.** `A.6.B` for the quadrant semantics, `A.6.C` for contract unpacking, `A.6.P`, `C.16.Q`, or `A.6.A` for lexical repair, and `E.17` faces for audience-specific publication of the same decomposed claim set.

**Common neighboring-pattern mistakes.** If the real object is still cue preservation or an early unresolved cue, use `A.16` or `A.16.1`; if a qualified relation, quality term, or action invitation is itself being repaired, apply `A.6.P`, `C.16.Q`, or `A.6.A`; if duties, commitments, promise content, work effects, and evidence are being mixed into one contract sentence, split them through `A.6.B` and `A.6.C` rather than minting one more undifferentiated contract paragraph.

**Causal/deontic split.** In “deploy because it would reduce harm”, `C.28` decides what the causal evidence supports; A.6.B separately classifies the boundary claims. If any atomic claim is permission-looking, choose one `A6-AW-*` row below. A causal-use record supplies none of those boundary claims.

**Authority-word branch (subordinate boundary-claim stress case).** When “approved”, “allowed”, “authorized”, “permitted”, or similar wording matters to action or reliance, choose one row by the claim being made—not by the visible word. These `A6-AW-*` labels are local claim-routing IDs, not new kinds.

| Branch ID | Ask this plain question | Placement and subject pattern | Stop / near-miss |
| --- | --- | --- | --- |
| `A6-AW-NORM-GRANT` | Does an exact policy prescribe an action, does one actual bearer have that duty, or may a named beneficiary perform one under stated conditions? | **D**: `A.2.8` for a generic prescription or, when separately instituted, one `U.Commitment`; `A.2.8.PER` for one `GrantedPermissionRelation@Context`, including beneficiary, action, scope/window, and policy-valid A.2.9 instituting act. | A policy sentence may state a generic prescription but by itself establishes neither an individual commitment nor a grant. |
| `A6-AW-GATE` | Does the sentence state a mechanism entry predicate, or claim one actual A.21 decision for a bounded action? | **A** for the A.6.1 entry predicate; **E** for an exact A.21 `GateDecisionResult` with its bounded action, profile application, complete required `GateCheckApplicationResult` set, decision value, consequence, scope/window, and recheck condition. | Split predicate and result into separate atomic claims. A checked grant or finding is an input; neither it nor a displayed carrier proves passage. |
| `A6-AW-EXERCISE` | Did this dated Work match the beneficiary and action of a current grant? | **E**: A.15.1 for the Work and `A.2.8.PER PermissionExerciseRelation@Context` for exercise. | A grant, plan, or green gate does not show that Work occurred or exercised it. |
| `A6-AW-WEAK` | Did a current, sufficiently complete frame find no prohibition before action or no violation in actual Work? | **E**: the exact A.2.8.PER `NonProhibitionFinding@Context` or `NonViolationFinding@Context`. | A stale or incomplete frame returns `unresolved`, not permission. |
| `A6-AW-CONFLICT` | Do a current grant and norm cover the same case, and has a rule or authorized decision selected the outcome? | **E**: `A.2.8.PER PermissionNormConflictFinding@Context` and its applicable rule or current resolution result. | A system-role kind, assignment, office, permit, or gate label alone leaves the conflict `unresolved`. |
| `A6-AW-SOURCE` | Does the sentence only say that a permit, badge, registry entry, message, or carrier exists, displays, or supports a claim? | **E** for the A.10 evidence claim; **L** only for a definition; keep the exact publication or carrier pattern. | A visible source is not a grant, gate, exercise, weak finding, or conflict resolution. |

**Concrete API/credential case.** A dashboard badge saying “API-7 approved for production” starts at `A6-AW-SOURCE`. It reaches `A6-AW-NORM-GRANT` only if a named policy-valid act instituted a current grant for a beneficiary and deployment action; the admission endpoint is separately `A6-AW-GATE`. Do not claim `A6-AW-EXERCISE` until a dated deployment Work occurrence matches that grant.

When agreement-like wording leaves an ambiguity that changes interpretation or use, use `A.6.C` to separate promise content, the instituting speech act, governance, Work, consequence, and evidence. For “recommended”, use A.16/A.6.A for a cue, `A6-AW-GATE` for an entry criterion, or A.2.8 only for recommendation-as-duty. Before action or reliance, return to the exact governing claim. Use A.15.4 while appearance hides the required prerequisite; use A.15 when the question is enactment alignment.


**Credential-currentness boundary.** Use A.10 to determine which claims a displayed credential's source and evidence support for the bounded use. Recover issuer, holder, verifier, status and currentness where they matter. Treat the display as `A6-AW-SOURCE`; move to another row only when that row's direct object and ground are independently present.

**Register-backed status boundary.** A pass, dashboard cell, API response, or certificate view may be only a publication of a register entry. Start at `A6-AW-SOURCE`; if the governing entry has institutional force, select the one row whose object it actually creates or changes and cite that row's subject pattern. Otherwise keep only source-finding or currentness support under A.10.

**Conflicting-source boundary.** When a classified boundary claim disagrees with its governing source or a display, resolve the source order, decision source, freshness policy and supersession rule. Until then, keep cue use or source-finding available; allow a bounded reversible probe only on its own adequate basis, without relying on the unsupported claim.



**Boundary and source repair assignment.** If the split exposes a missing claim or source, give the claim ID or canonical location, or the selected `A6-AW-*` branch to the identified boundary or source maintainer. Keep cue use or source-finding available. A bounded reversible probe needs its own adequate basis; the missing source still blocks the unsupported Work or reliance use.


**Recurring boundary ambiguity repair.** If the same wording repeatedly needs the same split, repair the boundary package: replace the misleading label, identify the L/A/D/E claims by ID or canonical location, and cite the source for the selected `A6-AW-*` branch. Repetition is a source defect, not a normal per-use burden.

Display guidance for boundary wording: a publication face, API page, or credential display should identify the relevant L/A/D/E claims by ID or canonical location and the source for the selected `A6-AW-*` branch. If it cannot, keep the wording at `A6-AW-SOURCE` or repair the boundary package.

For an incident-learning use, record the displayed phrase, intended Work or reliance use, unsupported claim or effect, missing or ambiguous L/A/D/E claim ID or canonical location, required source, plausible overread, safe disposition and upstream repair. Retain source, currentness and supersession references only where they change that case.

**Conventions:** The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **SHALL** are to be interpreted as in RFC 2119/8174. Lower-case `must`, `may`, and `should` in explanatory prose is descriptive, not normative.

**Statement identifiers (recommended):** Adopt the quadrant‑prefixed ID scheme from **A.6.B:0** for classifiable statements:
`L-*` (law or definition), `A-*` (admissibility gate), `D-*` (deontic or commitment), `E-*` (effect or evidence).
Other sections and faces **SHOULD** cite the canonical claim ID or location. Face prose may explain or faithfully paraphrase the claim without creating another specification.
IDs are intended to be “lintable” identifiers (and are especially useful when D‑duties enforce A‑gates or E‑claims). Consider pairing IDs with a lightweight Claim Register (A.6.B:7) to reduce paraphrase drift across faces.
**Non-collision note (informative):** The `A-*` prefix here is “Admissibility”, not Part‑A numbering and not MVPK’s `AssuranceLane` face designator. If this is a readability hazard in your program, prefer an explicit `G-*` (“Gate”) local convention while keeping the quadrant name “Admissibility”.

**Admissibility-predicate distinction (informative):** An `A-*` claim is a mechanism admissibility predicate or entry condition inside the L/A/D/E-classified boundary claim set. It is not an A.21 `GateDecisionResult`, `GateCheckApplicationResult`, optional `GateCheckRef`, optional `DecisionLog`, or proof that a gate passed. An `A-*` claim may name conditions consumed by a later A.21 profile application; actual passage is a separate `E-*` claim about the exact `GateDecisionResult`. An A.20 `ConstraintValidity` witness remains separate from the predicate, each check application, and the gate result.

**Claim Register (informative, recommended).** When a Claim Register is useful, use the mini-record in **A.6.B:7**. It can record stack placement (Signature, Mechanism, Norms, and Evidence) and the face designators that cite each claim. Add `viewRef`/`viewpointRef` only when the corresponding episteme identities matter. Mechanical checks can test ID resolution and exact text copying; inspect meaning for paraphrase drift.

### A.6:1 - Problem frame

Boundaries are where architecture lives: at the edge of a theory, an API, a protocol, a hardware connector, an organisational interface, or a published model. FPF already has the core building blocks to describe such edges:

* `U.Signature` as a *public, law‑governed declaration* (with Vocabulary, Laws, Applicability).
* `U.Mechanism` as a reusable operation declaration with OperationAlgebra, LawSet, AdmissibilityConditions and Applicability.
* Multi-view describing through E.17.0 `MultiViewDescribing`, plus separate E.17 publication discipline for selected epistemes, face uses, forms, and carriers.
* Recover each claim's **EntityOfConcern** separately from its claim-bearing **Description episteme** and any **publication carrier**. The concern may itself be an episteme or carrier; its position does not establish agency, Work, evidence, or a decision.

Yet boundary descriptions in practice fail in a predictable way: authors blend several fundamentally different kinds of claims into one undifferentiated contract paragraph. The result is brittle architecture: signatures become entangled with runtime gates, deontic language is mixed into mathematical invariants, and “effects” are asserted without any disciplined carrier and evidence story.

This cluster overview makes one disciplined move:

1. Treat a boundary as a **stack of boundary layers** (Signature → Mechanism → actual occurrences and their separately governed consequences/evidence) plus publication views and faces, and
2. Provide a **boundary discipline matrix** (2×2) that classifies statements by boundary layer, so evolution remains controlled and substitutions are possible.

*Terminology note (informative):* In this pattern:
* **Layer** names a stratum in the boundary stack (Signature → Mechanism → actual occurrences, separately governed consequences/evidence → Publication).
* **View** (`U.View`) is the same C.2.1 episteme individual when E.17.0 conformance to at least one exact viewpoint episteme obtains; it is not a projection operation, publication file, or document.
* **Viewpoint** (`U.Viewpoint`) is the same C.2.1 episteme individual when the fixed E.17.0 viewpoint-convention conditions obtain; its accountability use does not replace those membership conditions.
* **Face** (MVPK sense) is a publication form for a bounded reader/use. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are face designators, not additional `publication-face kind` values. A face may expose an episteme that independently has `U.View` membership; the form, rendering and carrier remain separate from that episteme.

### A.6:2 - Problem

When boundaries are described without an L/A/D/E claim-classification discipline, four confusions dominate:

1. **Laws vs admissibility.** Authors encode runtime gate predicates as “laws”, or write invariants using RFC‑style deontic verbs, blurring “what is true or defined” with “what is allowed to be applied”. FPF explicitly separates these: operational guard predicates belong to mechanisms (A.6.1), not signatures (A.6.0).
   *Common mistake #0 — Applicability ≠ Admissibility (informative):* Signature `Applicability` scopes declared admissible use and bounded context; it is not a runtime entry gate. Runtime entry checks belong in `U.Mechanism.AdmissibilityConditions` as `A-*`. Such a predicate may consume the direct object selected by one `A6-AW-*` row as input, but it neither creates that object nor proves gate passage. A generic prescription states what one exact policy or other normative episteme requires; it does not create an individual duty bearer or commitment occurrence. A claim that one actual System or separately governed party has that duty instead cites one separately obtaining A.2.8 `U.Commitment`. Either branch can reference the `A-*` gate by ID or canonical location without becoming the gate.

2. **Admissibility vs deontics.** `MUST`, `SHOULD`, `MAY`, and authority-looking words do not reveal whether a statement is a duty, one `A6-AW-*` permission branch, or an entry predicate. Classify the claim by its job; neither the word, selected subject pattern, nor kind of direct object decides the quadrant.

3. **Contract talk category errors.** If “the interface promises…” leaves a consequential ambiguity about the claim or its participant, use A.6.C to recover it before treating the wording as an agency error. Use A.2.3 for promise content, A.2.9 for the instituting speech-act Work, A.2.8 and A.2.8.PER for the commitment or grant, and A.15.1 only to identify the dated Work occurrence. An application result, production, delivery/transfer, acceptance, and evidence use each follows its own row in `A.15.1:4.6` and is omitted when that claim is absent. F.18 only names recovered terms when durable naming is current.

4. **Effect claims without an actual occurrence.** A description, diagram, log, or metric can state or support an effect claim, but none creates the effect. Ground the actual occurrence first. Use `U.Work` only when each exact actual performer has its A.13 core and A.15.1 independently identifies the Work, Method, time, and containing System. Add F.6 only when the receiving boundary claim expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 leaves the Work intact. Use A.3 and A.3.4, or the pattern that defines the interaction or causal claim, for natural, spontaneous, formal, or other non-Work change. Then name the observation and A.10 evidence path needed for reliance.

These confusions destroy evolvability: you cannot swap implementations behind a stable signature if the signature already smuggles mechanism gates, audit logistics, individual commitments, or assignment-based applicability conditions into “laws”.

### A.6:3 - Forces

| Force                                        | Tension                                                                                                                                                            |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Modularity vs expressiveness**             | A stable boundary must be abstract, but users want operational detail “in the same doc”.                                                                           |
| **Truth condition vs governance content** | Whether the sentence states what is true or observed, or states a prescription, individual duty, prohibition, commitment, or grant; visible RFC words and the selected subject pattern do not decide this axis. |
| **Design‑time clarity vs run‑time evidence** | What can be checked statically vs what requires executing work and observing traces.                                                                               |
| **View, viewpoint, and construction discipline** | A view is an episteme satisfying exact viewpoint conformance; a viewpoint is an exact convention-bearing episteme; optional A.6.3 construction and publication remain different relations. Losing any distinction makes omissions and provenance uninterpretable. |
| **Local meaning vs cross‑context reuse** | Boundaries keep meaning local ↔ cross-context reuse needs its actual correspondence and bounded-use basis. Use an F.9 Bridge only for two exact local senses when its predicate obtains; `CL` is optional evidence shorthand. |
| **Evolvability vs auditability**             | Evolving interfaces requires change; auditors require stable evidence trails.                                                                                      |
| **Human readability vs formal precision**    | Plain explanations vs tech‑register constraints; both must remain aligned.                                                                                         |

### A.6:4 - Solution — A stack + a classification matrix

#### A.6:4.1 - Why “stack”: what is stacked, and what “higher and lower” means

This pattern uses **stack** in the same pragmatic sense as other FPF stacks (e.g., the holonic import stack and other layered disciplines): an ordered set of layers where **higher layers are more stable commitments**, and **lower layers are more volatile realizations and evidence**. “Higher” and “lower” provide **engineering guidance for evolvability**:

* **Higher in the stack** = closer to *public, reusable boundary intent*.
* **Lower in the stack** = closer to *execution, implementation, and evidence* (what is actually done and observed).


The **Signature Stack** (as used in this cluster) is the ordered family of **canonical claim layers** for a boundary package. Each of the four claim layers below is a stable canonical placement for one quadrant of statements (L/A/D/E), with a canonical boundary publication form or section that carries those statements:

1. **Signature layer (L: laws or definitions).** `U.Signature` provides the stable declarative boundary: Vocabulary + Laws + Applicability, without runtime gate predicates.

2. **Mechanism layer (A: admissibility gates).** `U.Mechanism` specializes `U.Signature` through the operation declarations, LawSet, AdmissibilityConditions and Applicability governed by A.6.1. Its admission predicates remain declaration content. Evidence-interface declarations and transport details keep their own claim classification; use A.10 for evidence sources and carriers, and name carrier-producing Work only when that occurrence is claimed.

   *Audit vs AssuranceLane (avoid duplication):* a boundary's local **Audit and observability** section states its evidence-interface declarations: carrier classes and required fields, correlation keys, and exposure interface. `Mechanism.AuditObservability` below is a local publication-section locator, not an A.6.1 content component. **Retention, access, and enforcement are D-claims**. A general prescription remains a claim-bearing episteme; one obtaining individual duty cites the exact A.2.8 `U.Commitment`, its actual bearer, and its direct predicate. A system-role kind or assignment may be an applicability ground but is neither bearer nor commitment. An MVPK **AssuranceLane** is a publication face for auditors that explains how to adjudicate the evidence interface. Under CC-A.6.6, the `AssuranceLane` face references those evidence-interface declarations and relevant claim IDs or canonical locations; its explanation preserves their semantics.

3. **Deontic layer (D: duties, commitments, and grants).** Put here a general prescription or a claim about an exact individual duty, recommendation-as-duty, prohibition, commitment, or `A6-AW-NORM-GRANT`. For an individual duty, cite the exact A.2.8 `U.Commitment`, actual bearer, constitutive rule, required instituting basis, and direct predicate. Test any responsibility claim separately through its domain predicate or return the exact missing governor. Other `A6-AW-*` claims keep their own placement. Reference related `L-*`, `A-*`, or `E-*` claims by ID or canonical location rather than duplicating their constraints.

4. **Observable-effects and evidence layer (E: Work-Effects & Evidence).** `E-*` is the boundary's observable-effect and evidence claim family. Each claim names the actual occurrence or evaluated finding under its subject pattern and, when reliance is current, the observation conditions and A.10 evidence path. Name `U.Work` only after A.13 recovers each exact actual performer and A.15.1 independently identifies the Work, Method, time, and containing System. Add F.6 only when the receiving boundary use expressly consumes precise assignment-bound attribution; its absence or failure leaves the Work intact. A natural, spontaneous, or formal transformation may instead use A.3 and A.3.4. Canonical placement is an Evidence-and-carriers section, typically rendered in `AssuranceLane`.

5. **Actual occurrences and realizations (outside the description stack).** Substitutable realizations are exercised through dated Work only when each actual performer has its A.13 core and A.15.1 independently admits the occurrence. Add F.6 only when the receiving description also consumes precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 leaves the Work intact. Work may participate in change, production, speech-act effect, evaluation, or evidence production, but each relation or claim must be established under the pattern that defines or constrains it. A.3 and A.3.4 also admit natural, spontaneous, and formal transformations without a performer, assignment, Method, or Work occurrence.

6. **Publication faces.** MVPK selects exact epistemes and publication forms for audience-specific face uses. A selected episteme has `U.View` membership only when E.17.0 conformance to the exact viewpoint episteme obtains; any A.6.3 source-to-receiving construction remains separate. The face designator, publication occurrence, form, rendering, and carrier are not the `U.View`.

*Observability compatibility note (informative):* When specifying evidence carriers and correlation rules, it is often convenient to describe evidence-carrier classes using examples from observability practice: traces and spans, logs and log records, and metrics time-series, with explicit correlation identifiers. Treat these as example *carrier schemas and join keys*, not as mandatory technology choices.

##### A.6:4.1.1 - AssuranceLane skeleton (informative)

An MVPK **AssuranceLane** is a publication face that teaches a specific audience how to adjudicate `E-*` claims against the relevant evidence carriers, including those produced in Work. It cites the boundary's evidence-interface declarations and explains them without changing their semantics.

Minimal content (suggested):
- **Scope:** boundaryRef, version; viewRef and viewpointRef when view or viewpoint identity matters.
- **Carrier inventory:** carrier-class and carrier-schema refs (A.7 Carrier) + where to obtain them.
- **E‑claim map:** a table keyed by `E-*` ID with: measurement conditions, carrierRef(s), join and correlation keys, and a reference to the canonical `E-*` text that defines pass or fail criteria.
- **Operational policies:** references to relevant `D-*` duties (retention, access control, exposure), without redefining them.
- **Limitations:** sampling, redaction, missing signals, expected false negatives and false positives.

**No new semantics reminder.** An `AssuranceLane` may explain adjudication informatively, but any new boundary claim first enters its canonical source. A changed permission-looking claim cites its selected `A6-AW-*` row and subject pattern rather than being introduced inside the face.

Example (conceptual; uses view/viewpoint identity and the additional hypothetical header case in §4.2):

```
AssuranceLane:
  viewRef: <ViewId>
  viewpointRef: <ViewpointId>
  boundaryRef: <BoundaryId>
  version: <SemVer or revision>
  evidence:
    - E: E-OBS-1
      carrierRefs: [Carrier.AuthorizationRecord, Carrier.AuditLogEntry]
      measurement:
        conditions: "on every request lacking header X (A-AC-1)"
        vantage: "Operator and auditor pipeline"
        correlation: ["traceId", "requestId"]
      adjudication:
        check: "query audit stream for code=NotAdmissible and join to traceId"
        criteriaRef: "E-OBS-1 (pass or fail criteria live canonically in the E-claim)"
      references: [A-AC-1, D-RET-1, Mechanism.AuditObservability]
```

The absence condition also covers a request that was not rejected. A claim of complete coverage requires the relevant request population to be accounted for separately from individual query joins.

Default placements (quadrant → stack layer / section):

* **L →** Signature.Laws (and, where appropriate, mechanism‑local semantic laws; never runtime gates)
* **A →** Mechanism.AdmissibilityConditions
* **D →** generic prescriptions, individual duties or commitments, recommendations-as-duty, prohibitions, and `A6-AW-NORM-GRANT` claims at their exact A.2.8 or A.2.8.PER subject pattern
* **E →** actual occurrences, evaluated findings, and evidence claims, including `A6-AW-EXERCISE`, `A6-AW-WEAK`, `A6-AW-CONFLICT`, and `A6-AW-SOURCE` when those claims are current

**Related subject rules (informative):**
* **A.6.1 ↔ A‑quadrant:** `U.Mechanism.AdmissibilityConditions` is the canonical claim layer for `A-*` gate and admissibility claims.
* **A.10 / B.3 ↔ E‑quadrant:** for an `E-*` claim used for reliance, recover the A.10 evidence-provenance path and bounded use. A missing path narrows or blocks only the unsupported use. Open B.3 only for an actual named assurance claim about an exact target and assurance use.
* **A.2.3 and F.12 ↔ D/E separation:** a `U.PromiseContent` promise is not evidence; promise acceptance is linked to Work evidence via F.12. A general duty remains normative content, while an obtaining individual duty is one A.2.8 `U.Commitment` borne by an actual System or other admitted party. Any system-role kind or assignment used to establish applicability stays separate. `D-*` claims reference `A-*` and `E-*` claims by ID or canonical location when needed.

 A stack is useful because the intended direction of change is clear:

* Lower layers (realizations, audit formats, transport mechanisms) are expected to change more frequently and can often evolve without forcing higher‑layer changes, provided higher‑layer commitments remain satisfied.
* Changes to higher layers are boundary-claim evolution and typically require explicit compatibility reasoning (and therefore explicit versioning and communication).

#### A.6:4.2 - Boundary Discipline Matrix: classify by A.6.B (the Boundary Norm Square)

**Normative source.** The canonical 2×2 square (the two A.6.B distinctions, quadrant semantics, form constraints, and cross‑quadrant reference rules) is defined in **A.6.B**. This section provides a short operational summary and worked rewrites only.

The **2×2 matrix** crosses **two independent distinctions**:

* **Modality family:** truth-conditional versus governance content. For permission-looking wording, the selected `A6-AW-*` row states which side applies; A.2.8.PER membership alone does not.
* **Adjudication substrate:** in‑description vs in‑work (whether satisfaction is decided from the description alone or requires observing executed work and carriers).

Operational summary (quadrant → canonical claim layer in the stack):
* **L** (Laws & Definitions) → `Signature.Laws` (truth‑conditional semantics, in‑description)
* **A** (Admissibility & Gates) → `Mechanism.AdmissibilityConditions` (runtime entry predicates; a predicate may consume an exact grant or finding selected by `A.6.B:8.4.1`, but it neither creates nor resolves that object)
* **D** (Deontics) → generic-prescription or individual-duty A.2.8 claims and `A6-AW-NORM-GRANT`
* **E** (Work-Effects & Evidence) → actual-occurrence, evaluated-finding, and evidence claims, including the applicable E-side `A6-AW-*` row

Atomicity rule:

If a sentence mixes logical jobs, for example “MUST” plus a gate predicate plus an effect claim, it is **not classifiable** as a single statement. Per **A.6.B**, split it into **atomic** claims so each one has exactly one quadrant and, ideally, an identifier you can reference.

Micro‑template: **Atomize → Classify → Place → Identify EntityOfConcern → Register when useful**

1. **Split** the sentence into atomic claims, one logical job each.
2. **Assign** each claim to exactly one quadrant (L/A/D/E) using the matrix.
3. **Place** each claim into its correct section or publication form (stack layer + section).
4. **Anchor A.7:** name what each claim is about, separately from the episteme carrying it. Add publication and carrier relations when they change interpretation. For permission-looking wording, bind the direct object and participants required by the selected `A6-AW-*` row; the selected subject pattern or kind of direct object never supplies the quadrant.
5. **Register when useful:** add the atomic claim to the Claim Register if used. Downstream faces cite the claim by ID or canonical location and preserve its meaning in any explanation.

Action outputs after classification:

- implement or repair an admissibility predicate when the claim being made is `A-*`;
- repair the exact normative source for a generic D claim, the actual duty bearer and A.2.8 result for an individual D claim, or the direct object named by the selected permission row;
- recover the exact actual occurrence, evaluated finding, or evidence path named by an E claim; use the selected E-side `A6-AW-*` row when permission wording is current;
- publish or update an MVPK face that cites L/A/D/E claims by ID or canonical location and explains them faithfully where its readers need prose;
- reopen the exact subject pattern when the classified statement is used beyond boundary wording; the selected `A6-AW-*` row names the permission-side subject pattern;
- downgrade the visible wording to cue use or source-finding only when the exact source is missing;
- narrow the unsupported Work or reliance claim; allow a local or reversible use only on its own adequate basis and stated stop condition, or block the unsupported use while its source is repaired.

> **Informative example.** Example rewrite (mixed → atomic):

*Before (mixed, not classifiable yet):* “Clients **MUST** include header `X`; otherwise the request is invalid and the system logs `NotAdmissible`.”

*Recovered source clauses:*

* “Clients **MUST** include header `X`.”
* “If a request lacks header `X`, the request is invalid.”
* “If a request lacks header `X`, the system logs `NotAdmissible`.”

Recover the intended invalidity/admissibility meaning before fully classifying the second clause. The third clause states a generic logging rule; it reports no particular observed request.

*Additional hypothetical illustration.* Suppose a separate boundary policy defines invalidity here as failure of the entry condition below and adds an implementer duty to the quoted Clients duty. Also suppose the observation stated in `E-OBS-1` actually occurred in this hypothetical case:

* `A-AC-1` (Quadrant A, Mechanism.AdmissibilityConditions): `hasHeader(req, "X")` is a necessary entry condition.
* `D-CL-1` (Quadrant D, Norms-and-commitments): “Client implementers **MUST** include header `X` in each request to this boundary (`A-AC-1`).”
* `E-OBS-1` (Quadrant E, Evidence-and-carriers): “For the selected request `req` lacking header `X` (`A-AC-1`), the system logged `NotAdmissible`; the observer recovered its `AuditLogEntry{code="NotAdmissible"}` in the audit stream.” The carrier schema is an additional illustrative choice. Logging depends on the absence of `X`, including when the request was not actually rejected.

> **Informative example.** Example rewrite (guarantee + SLA + measurement + enforcement):
>
> *Before (mixed contract prose):* “The service **guarantees** 99.9% availability per calendar month and **MUST** keep p95 latency under 200ms; breaches are penalized; operators **SHALL** alert on violations.”
>
> *Recovered source clauses:*
>
> * “The service **guarantees** 99.9% availability per calendar month.”
> * “The service **MUST** keep p95 latency under 200ms.”
> * “Breaches are penalized.”
> * “Operators **SHALL** alert on violations.”
>
> Recover the guarantee's meaning and bearer, the measurement and acceptance basis, and the breach trigger, penalty and applicable parties. Use **A.6.C** for the unresolved contract meanings and **A.6.B** to classify the resulting atoms. The split alone does not settle them.
>
> *Additional hypothetical illustration.* Suppose a separate policy identifies Provider and the service being measured, states the exclusions and workload `W`, defines the availability and latency metrics, and sets the two criteria evaluated below. In addition to the quoted alert duty, it requires paging within 5 minutes. The following E-claims assume that the stated evaluations and observation actually occurred in this hypothetical case; the alert observation concerns a separate violation case.
>
> * `D-SLA-1` (Quadrant D, Commitments and SLA): “Provider **SHALL** meet the availability and latency criteria evaluated by `E-SLA-AVAIL-1` and `E-SLA-LAT-1` under the stated exclusions.”
> * `E-SLA-AVAIL-1` (Quadrant E, Evidence-and-carriers): “The evaluation of the observed calendar month `T` reported `availability ≥ 0.999`, with measurements recorded in carrier `UptimeProbeSeries` from viewpoint `VP.ExternalMonitor`.”
> * `E-SLA-LAT-1` (Quadrant E, Evidence-and-carriers): “The evaluation under workload `W` reported `latency_p95 < 200ms`, with measurements recorded in carrier `LatencyMetricSeries` from viewpoint `VP.Client`.”
> * `D-OPS-ALERT-1` (Quadrant D, Ops duty): “Operators **MUST** page on breach of the criteria evaluated by `E-SLA-AVAIL-1` or `E-SLA-LAT-1` within 5 minutes (additional policy).”
> * `E-ALERT-1` (Quadrant E, Evidence-and-carriers): “In the separate violation case, the operator's page was observed in carrier `AlertEvent{ruleId,firedAt,target}` and can be joined via `incidentId`.”
>
> These added policy and observation premises do not resolve the original guarantee, duty bearer or penalty clause.

See **A.6.B:4–A.6.B:6** for the normative square, quadrant form constraints, and explicit cross‑quadrant link patterns (notably: **D→A**, **E→A**, **D→E**, and **A/E→L**).

##### A.6:4.2.1 - Authority-wording split examples

These examples are informative. They separate authority wording from the evidence, assurance, commitment, gate-passage, or Work claim being made.

*Before (mixed):* "This API is approved for production use and guarantees safe rollback."

*Recovered source clauses:*

* “This API is approved for production use.”
* “This API guarantees safe rollback.”

Recover the approval's direct object and ground under the applicable `A6-AW-*` row, and the rollback subject and safety predicate. Both source claims remain unresolved until that meaning is supplied.

*Additional hypothetical illustration.* Assume supplied signature vocabulary defines the API operation and rollback terms; a separate boundary policy gives the request-admission predicate, policy window and exclusions. For `E-API-1`, additionally assume that a named evaluation of an independently identified rollback occurrence actually reported success under a stated success criterion and observation basis:

* `L-API-1` (Quadrant L): the API operation and rollback terms are defined in the supplied signature vocabulary.
* `A-API-1` (Quadrant A): a request is admissible only under the named subject, action, object, context, and policy-version predicate.
* `D-API-1` (Quadrant D): the exact provider policy prescribes maintaining or enforcing `A-API-1` under the named window and exclusions. If the claim is instead that one actual provider or operator bears this duty, cite its separately instituted A.2.8 commitment.
* `E-API-1` (Quadrant E): the named evaluation reported rollback success under its stated success criterion. Possible evidence inputs include the named work traces, audit records, or metrics. A gate decision carrier may support the exact gate-passage claim; rollback execution needs its own occurrence and evidence basis.

In this additional case, `A-API-1` applies `A6-AW-GATE`, while an approval badge remains `A6-AW-SOURCE` unless another row's closing facts are present. The original production approval and safe-rollback guarantee remain unresolved. A success result alone does not establish the unspecified safety claim.

For a filled grant/exercise/evidence case and its near-misses, use `A.6.B:8.4.5.4`. It applies `A6-AW-NORM-GRANT`, `A6-AW-EXERCISE`, and the separate A.10 evidence claim by value.

Then:
- if appearance hides the prerequisite for action or reliance, enter `A.15.4`; use `A.15` for enactment alignment;
- if evidence, currentness, or provenance is live, attach the `A.10` evidence relation;
- if an actual named assurance claim is current, use `B.3` for its exact target claim, argument, bounded assurance use and `AssuranceResult`; otherwise keep trust, readiness, compliance or release questions with their direct patterns;
- if an actual gate decision or passage is asserted, classify it as a separate E claim and cite the exact A.21 `GateDecisionResult`, bounded action, applicable `GateProfile` application, complete required `GateCheckApplicationResult` set, `decisionValue`, action consequence, scope/window, and recheck condition; use a short `GateCheckRef` only for a selected publication structure and a `DecisionLog` only when audit or reuse is current;
- if a flow witness or constraint witness is asserted, cite `A.20` `ConstraintValidity` status or witness;
- if a permission-looking claim is asserted, use the selected `A6-AW-*` row and its subject pattern; an entry predicate or `GateDecisionResult` does not substitute for another row;
- if release, deployment, rollback, or execution Work is asserted, cite the exact A.15.1 dated occurrence; then use only the applicable `A.15.1:4.6` row for an application result, A.15.PROD production branch, delivery/transfer relation, evaluation/acceptance relation, or A.10 evidence path. None is an intrinsic Work field;
- if the phrase is only an action invitation or cue, keep it in `A.6.A`, `A.16`, or `A.16.1` according to the current kind.

Policy engines, credentials, registers, provenance, and attestations can supply policy decisions, source claims, currentness, or evidence. Start a visible permit, badge, or registry value at `A6-AW-SOURCE`; move to another branch only when its named direct object and participants are independently established.

#### A.6:4.3 - View membership needs exact viewpoint conformance

`MultiViewDescribing` makes the candidate episteme and exact viewpoint episteme explicit. The candidate has `U.View` membership only when E.17.0 conformance obtains. A projection or query may participate in an A.6.3 construction, but that construction does not establish membership. MVPK separately uses publication face designators (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) and their E.17 profiles. E.17:5.2 specifies the declared `publication-face kind` values.

A disciplined stack therefore requires:

* Every published face use identifies the selected episteme and its separate reader/use declaration. Name the exact viewpoint episteme through `U.ViewpointRef` when `U.View` membership or viewpoint identity is used; name the publication occurrence, form, and carrier when those identities change publication or reliance. The face designator is not any of those objects.
* Calling the selected episteme a `U.View` requires E.17.0 conformance; a face label, viewpoint reference, projection history, or publication does not establish it.
* Per **E.17** (“no new semantics”), a face **MUST NOT** introduce a new semantic commitment or any new object or claim selected through `A6-AW-*`. A face **MAY** add informative explanation, examples, and cross-references that preserve the source claims. Normative face prose cites the canonical L/A/D/E claim ID or location and direct object; it may faithfully paraphrase the claim. Add any new boundary claim to its canonical source before publishing it on a face. Use verbatim text when exactness is critical or disputed.
* Per **E.17** and **publication-face and publication-form discipline** (face‑kind closure), a publication package that claims MVPK alignment **MUST NOT** mint additional MVPK face kinds (e.g., “EvidenceCard”, “NormsCard”) as if they were first‑class kinds; if you need local headings, keep them as sections within the selected faces.

#### A.6:4.4 - “Contract” unpacking: avoid assigning agency to epistemes

When “the API contract” leaves a consequential ambiguity, use **A.6.C** to ask only the live questions: what was promised, what was said or instituted, what governance position obtains, and what actually happened. Use `A.15.1:4.6` to separate any dated Work from the result, production, delivery/transfer, evidence, or acceptance claims actually made. Clear wording, including a semantic guarantee or recoverable ordinary metonymy, needs no unpacking record.

* **Promise content (promise content; `U.PromiseContent`, A.2.3):** what is promised to be made available to eligible consumers — **a promise, not execution** (`U.Work`).
* **Utterance package (published descriptions + instituting act):** what is said and published and versioned (signature or mechanism descriptions plus MVPK faces), plus the `U.SpeechAct <: U.Work` that published or approved it when provenance matters (A.2.9).
* **Commitment (individual deontic relation; `U.Commitment`, A.2.8):** whether one actual admitted System or other party is obligated, recommended-as-duty, or prohibited from doing something under an exact constitutive rule and required instituting basis. A system-role kind or assignment may help satisfy that rule's applicability conditions; neither is the duty bearer or the commitment relation. A commitment does not establish responsibility, which needs its own direct domain predicate or an exact missing-governor result.
* **Permission-looking claim:** do not make `Permission` a bundle part or quadrant. Select one `A6-AW-*` row for each atomic claim and cite its direct object.
* **Performed Work (`A.15.1`):** whether one dated Work occurrence happened, who performed it, which Method it enacted, when it happened, and within which System. Recover each exact performer through A.13 and admit the Work independently through A.15.1. Only when the receiving account expressly consumes precise assignment-bound attribution, recover the exact A.2.1 assignment independently and let F.6 check its link to the Work through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and a failed or absent result does not revoke Work. This claim supplies no result, delivery, or acceptance by itself.
* **Result or consequence (`A.15.1:4.6` dispatch):** only when current, name the exact A.6.1 application/result binding or subject-specific `WorkResultRelation`, A.15.PROD production branch, A.3.4 change, evaluation result, delivery/transfer relation, or acceptance relation.
* **Evidence (`A.10`):** only when a receiving use relies on one of those claims, name the claim-bound evidence path and carrier.

In A.6 terms:

* The **signature** is the *utterance substrate* for the boundary; it is not itself a promiser or obligor (A.7).
* Deontic claims use A.2.8 for generic prescriptions or separately obtaining individual duties and commitments, and `A6-AW-NORM-GRANT` for the current norm/grant branch. Other permission-looking claims keep the placement and object named by their selected row.
* Classify each atomic operational “guarantee” claim as **L** (truth-conditional law), **A** (entry predicate), **D** (generic prescription, individual commitment, or current grant), or **E** (actual exercise, evaluated result, work effect, or measured property with evidence).

**Compact optional-object replay.** `SVC-DEPLOY-1` states promise content. Admitted system `ReleaseManager-4` performs `SA-4711 : U.SpeechAct` under `ReleaseManager-4@ReleaseShift`; the exact policy may institute `COM-4711 : U.Commitment` or `PER-4711 : GrantedPermissionRelation@Context`. Later admitted system `Operator-7` performs `DeployRun-4711 : U.Work` under its covering assignment. If the application returns `ReleaseArtifact-4711`, cite the exact A.6.1 result binding or an already governed `WorkResultRelation`; if that artifact is delivered, cite a separately obtaining transfer relation defined by its subject pattern; if acceptance is claimed, cite the criterion, evaluation Work/result, and acceptance relation. An A.10 path may support whichever one of those claims is relied on. Omit every absent object: the Work can occur without a result, delivery, acceptance, or evidence-use claim.

Use **A.6.C — Contract Unpacking for Boundaries** for the expanded account and the same `A.15.1:4.6` dispatch.

#### A.6:4.5 - Where statements go (classification examples)

> **Informative.** Classification examples for learning the discipline; they do not add requirements beyond A.6:7.

The table below intentionally uses near‑everyday spec phrases. The same visible words appear in different quadrants depending on what they *do*.

The `A.7 primary layer` field below identifies the claim's EntityOfConcern, with its kind when needed; it is not a layer selected from the quadrant. The concern may itself be a Description episteme or publication carrier and remains separate from the episteme carrying the claim.

| ID | Example statement (typical wording) | Matrix quadrant | Put it under… | A.7 primary layer |
| --- | --- | ---: | --- | --- |
| `L-1` | “`op f` is **defined iff** `P(x)` holds.” | L | Signature → **Laws** (`Definition:`) | Operation `f`; the relation of `x` to `f` is unresolved |
| `L-2` | “For all requests, `idempotencyKey` is **unique** per subject.” | L | Signature → **Laws** (`Invariant:`) | Requests' `idempotencyKey` values; the request population and `subject` are unresolved |
| `A-1` | “The mechanism may be applied only if `tokenValid`.” *(rewrite as predicate: `admissible(req) implies tokenValid(req)`)* | A | Mechanism → **AdmissibilityConditions** (entry gate) | Entry predicate `admissible(req) implies tokenValid(req)` |
| `A-2` | “A request is admissible only if header `X` is present.” | A | Mechanism → **AdmissibilityConditions** | Request-entry predicate requiring header `X` |
| `D-1` | “Client implementers **MUST** satisfy `A-2`.” | D | Norms-and-commitments: a general prescription unless one exact A.2.8 individual commitment and actual bearer are also identified; reference the gate by ID or canonical location | Normative rule requiring client implementers to satisfy `A-2` |
| `D-2` | “Authors **MUST** publish a versioned MVPK face for this boundary.” | D | Conformance Checklist and publication norms (authoring plane) | Normative rule requiring authors to publish this boundary's versioned MVPK face |
| `D-3` | “Operators **SHOULD** rotate keys every 90 days.” | D | Norms: state the prescription; if an individual duty is claimed, identify its actual bearer, direct A.2.8 predicate, and any separately obtaining system-role assignment used only for applicability | Normative rule recommending that operators rotate keys every 90 days |
| `D-4` | “Implementers **MUST** expose audit‑log carriers via endpoint `/audit`.” | D | Norms-and-commitments (exposure duty) *about carriers* | Normative rule requiring implementers to expose audit-log carriers via `/audit` |
| `D-5` | “The vendor commits to `99.9%` availability over window `T` (SLA).” | D | Commitments and SLA: identify the actual admitted vendor System or other A.2.8 party as duty bearer, the direct commitment predicate, constitutive rule, required basis, window, and exclusions; any system-role assignment is only a possible applicability ground | The vendor's individual availability commitment |
| `E-1` | “`LedgerBalance-L17` changed from 80 to 65 across interval `T` under the stated account-continuity rule.” | E | A.3/A.3.4 actual transformation claim; no Work is inferred from the delta alone | Change of `LedgerBalance-L17` across `T` |
| `E-1-EVID` | “`AuditRecord-L17` evidences `E-1` for audit use under the stated source, window, and A.10 path.” | E | Evidence relation and carrier for the already named change | A.10 support relation from `AuditRecord-L17` to claim `E-1` for audit use |
| `D-6` | “Operators **MUST** retain audit‑log carriers for 30 days.” | D | Retention policy (deontic) *about carriers* | Normative rule requiring operators to retain audit-log carriers for 30 days |
| `E-2` | “`latency_p95 ≤ 200ms` under workload `W` using measurements recorded in carrier `LatencyMetricSeries` from collector `C`.” | E | Measured-property claim with measurement conditions; subject unresolved | Entity whose latency is measured: unresolved; `LatencyMetricSeries` is the measurement carrier, not that missing referent |

Notes:

* The classification is not just about modal verbs. “Shall” can be D (a duty) or A (a gate behavior). “Guarantees” can be D (a commitment) or E (a measured property). The matrix forces disambiguation.
* If a sentence combines a duty with an entry condition, split it into (A) a gate predicate (`A-*`) and (D) either a general prescription or a claim about one exact `U.Commitment` borne by an actual System or other admitted party (`D-*` referencing the gate by ID or canonical location). When observability matters, add an E claim only on a separate actual observation or result basis. A requirement to produce or retain logs is D; an expectation or plan supplies no actual E result. A system-role kind or assignment may establish applicability only through an independently obtaining rule; neither bears the duty.
* When something needs to be enforceable but is mathematical, prefer predicate blocks rather than deontic language in the L/A blocks, per E.8’s deontics vs admissibility guidance.

#### A.6:4.6 - Classification sanity rules (informative, concept-level)

These are *writing diagnostics*, not tool requirements.

- **RFC keyword inside Definition, invariant, or admissibility predicate** → classification error (rephrase as predicate; move obligation to `D-*`).
- **`E-*` with no exact actual occurrence or evaluated predicate, or with a carrier but no evidence relation for the claimed use** → incomplete effect/evidence claim. Ground Work through A.15.1 only when it actually obtains; otherwise use A.3/A.3.4 or the exact interaction or causal-use pattern. A carrier supports the claim but does not create the effect.
- **`D-*` that re-states an `A-*`/`L-*` predicate instead of citing its ID or canonical location** → drift risk (prefer “MUST satisfy `A-…`”).
- **A face introduces new L/A/D/E content not present in the canonical claim set** → view-fork. Recover the direct object and classify the new claim—duty/commitment/grant in D; exercise/evaluated finding/evidence in E; gate in A—then add it to its canonical source before face publication. Informative commentary may explain existing claims without adding boundary semantics.
- **“The system or service SHALL …” where the phrase does not name a direct behavior claim, general prescription, or exact individual commitment with its actual bearer and constitutive basis** → unresolved subject and modality. Recover the System or other party, state an actual `E-*` behavior claim separately only when its actual basis is supplied, and state either the normative content or the direct A.2.8 commitment. A service label, system-role kind, or assignment proves none of these claims.

### A.6:5 - Archetypal Grounding (Tell–Show–Show; System / Episteme)

> **Informative.** Worked examples for learning the L/A/D/E claim-classification discipline; they do not add requirements beyond A.6:7.

#### Tell (universal rule)

To support boundary evolvability, separate claims across the signature stack and classify each statement as Law, Admissibility, Deontic duty/commitment/grant, or the boundary's observable-effect/evidence family. An E claim names the exact actual occurrence under its subject predicate and retains the pattern only as a locator: dated Work only when the A.15.1 predicate is satisfied, or A.3/A.3.4 plus the exact interaction or causal predicate for non-Work change. EntityOfConcern, description, and publication carrier remain separate.

#### Show #1 (`U.System`): effectful API boundary (algebraic effects intuition)

**System:** A “Payment Authorize” service.

* **Signature layer (A.6.0).**

  * Vocabulary: `PaymentRequest`, `AuthDecision`, `MerchantId`, `Money`, etc.
  * Laws: e.g., “If decision is APPROVED then reservedAmount = requestedAmount” (truth‑conditional).
  * Applicability: bounded context “Payments Authorization”.

* **Mechanism layer (A.6.1).**

  * Admissibility gate: request is admissible iff `tokenValid ∧ merchantActive ∧ amountWithinLimit`.
  * Boundary transport details: HTTP headers and idempotency-key carriage. Declare canonical currency-conversion operations under A.6.1.
  * The local Audit and observability section specifies required evidence carriers (e.g., `AuthorizationRecord` event, log entry) and their fields, correlation IDs and retention class. Retention duties remain D-claims.

* **Actual occurrence and work layer.**

  * The payment-handling occurrence is `U.Work` only when its exact actual performer first has the A.13 core and A.15.1 independently admits the occurrence from its Method, time, containing System, and other required direct facts. If this payment account also asks under which assignment the performer acted, add F.6 through the same obtaining A.13 assignment; missing or failed attribution leaves the payment Work intact.
  * The ledger reservation change, event emission, timer transition, or retry effect is a separate actual-occurrence claim under A.3/A.3.4 or its exact interaction or causal-use pattern. Check each effect separately: knowing that the payment Work occurred does not show that the ledger changed, an event was emitted, or a retry happened.
  * Traces, logs, and metrics enter an A.10 evidence path for the exact effect being relied on; carrier presence creates neither Work nor change.
* **Publication faces (MVPK).**

  * PlainView: narrative for stakeholders (what the service promise is, in plain terms).
  * TechCard: signature or mechanism details (types, error codes, version policy, admissibility predicate refs).
  * InteropCard: machine‑exchange oriented boundary details (canonical field names, schema refs, transport bindings).
  * AssuranceLane: evidence bindings (which carriers exist, how to adjudicate `E-*` claims, retention and access duties by reference).

**Effects-and-handlers analogy.** In this software example, the signature exposes the operation interface. A.6.1 governs declared operation semantics and the separate realization relation; the realizing entity supplies the concrete handler implementation. Implementations can change while preserving the declared operation meanings and applicable constraints.

**Classification example:**

* “A request is admissible iff `tokenValid ∧ merchantActive ∧ amountWithinLimit`” belongs in Quadrant A (the declared admissibility gate).
* “Clients MUST include Idempotency-Key” belongs in Quadrant D as a normative prescription and should reference the same gate semantics to avoid divergence. It becomes a claim about one obtaining individual `U.Commitment` only after A.2.8 identifies the actual bearer, constitutive rule, required instituting basis, and direct predicate.
* “System emits AuthorizationRecord” belongs in Quadrant E (an actual event-emission claim).

#### Show #2 (`U.Episteme`): published evaluation protocol boundary (multi‑view + evidence)

**Episteme:** A published “Model Evaluation Protocol” for a safety‑critical classifier.

* **Signature layer:** names operations such as `Evaluate(model, dataset) → Report` and states metric definitions (AUROC, calibration error) as Laws. A.6.1 governs the corresponding operation declaration and its argument/result meanings.

* **Mechanism layer:** admissibility gate encodes when evaluation is permitted: dataset version must match declared license; measurement environment must meet constraints; seeds pinned.

* **Deontics and commitments:** the protocol may prescribe that reviewers use dataset vX.Y and that authors publish MVPK faces and cite the measurement environment. If an organisation has an individual review-SLA duty, identify that actual admitted System or other A.2.8 party as bearer and establish the direct `U.Commitment` predicate. Any system-role classification or assignment remains a separate possible applicability ground.

* **Effects and evidence:** the dated evaluation run is a Work occurrence only when A.15.1 grounds it; its result episteme, any model or dataset change, and the report publication remain separate. Report files, logs, hashes, and trace IDs support the selected claims through A.10 but create none of those occurrences or results.

**Non-Work E contrast.** A seedling's spontaneous first-leaf unfolding can be an actual A.3.4 transformation with no performer, assignment, method, or Work occurrence. Measurements may support that exact change claim through A.10; neither the observation work nor its carrier becomes the change.

* **Multi‑view (MVPK face designators):**

  * PlainView for decision makers: what this protocol means for assurance.
  * TechCard for engineers: metric definitions named by value, admissibility predicates, and a clearly marked **Norms-and-commitments** section (D‑claims) for governance.
  * InteropCard for exchange-oriented consumers: conceptual field names, anchors, and schema references.
  * AssuranceLane for auditors: evidence map (which carriers support which occurrence claims) and adjudication steps keyed by `E-*` IDs.

This episteme is a boundary because it mediates between theory (“metric definitions”) and work (“a run produced a report”). The signature stack provides the stable interface for that mediation.

### A.6:6 - Bias-Annotation


* **Arch bias:** Biases toward separation of concerns and explicit layering; mitigated by allowing multiple faces so audiences are not forced into the same amount of detail.
* **Ontological and Epistemic bias:** Treats signatures and mechanisms as epistemes that must not be conflated with work.
* **Gov bias:** Prefers auditable responsibility (viewpoint accountability and commitment unpacking).

### A.6:7 - Conformance Checklist

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Purpose                                                             |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **CC‑A.6.1 (Stack declaration).** | A conforming boundary description **SHALL** identify Signature, Mechanism, actual-occurrence, consequence/evidence, and Publication placements. A dated Work claim **SHALL** remain separate from any application result, production, change, delivery/transfer, evidence, or acceptance claim selected through `A.15.1:4.6`. | Prevents one “work and evidence” layer from recreating intrinsic outputs. |
| **CC‑A.6.2 (Square discipline).** | A conforming boundary description **SHALL** classify each atomic claim by its own modality and adjudication position. Every permission-looking claim **SHALL** cite one selected `A6-AW-*` row and that row's direct object; the selected subject pattern or kind of direct object alone never sets the quadrant. | Makes one actionable choice replace repeated permission catalogues. |
| **CC‑A.6.5 (Actual-occurrence, description, and carrier separation).** | An `E-*` claim **SHALL** identify the exact actual occurrence or evaluated finding under its subject pattern and **SHALL NOT** infer Work merely because change or a carrier exists. Any carrier used for reliance **SHALL** enter the exact evidence relation. | Preserves non-Work change and blocks carrier-as-effect errors. |
| **CC‑A.6.6 (Viewpoint accountability).** | Every published MVPK face use **SHALL** identify the selected episteme and bounded reader/use. When `U.View` membership or viewpoint identity is used, the face **SHALL** identify the exact `viewpointRef`. `U.View` membership still requires E.17.0 conformance. Normative face content **MUST** cite canonical L/A/D/E claims by ID or canonical location and name their direct objects; meaning-preserving prose may explain them. Face content **MUST NOT** introduce a new commitment or any new object or claim selected through `A6-AW-*`. | Preserves viewpoint discipline without letting a publication face create governance or permission claims. |
| **CC‑A.6.6a (MVPK face‑kind discipline).**  | A publication that claims MVPK alignment **MUST** use E.17’s declared `publication-face kind` values: **publication face/form** and **interop publication form**. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are face designators, with profiles selected under E.17. A publication **MUST NOT** mint additional MVPK face kinds. Local “cards” may exist only as headings or sections inside the selected faces. | Aligns with MVPK and publication-face or publication-form discipline; prevents new‑face drift.            |
| **CC‑A.6.7 (Contract unpacking).** | When ambiguity in “contract”, “guarantee”, “permission”, or “promise” language changes interpretation or use, a conforming text **SHOULD** use only the live A.6.C questions for the object split and `A.6.B:8.4.1` for classification. Promise content, instituting speech-act Work, commitment or grant, dated performed Work, application/result binding, production, delivery/transfer, evidence, and acceptance **MUST** remain independently optional objects under their subject patterns. | Stops agency attribution and result/output rebundling. |
| **CC-A6-CAUSAL-DEONTIC-SPLIT (Causal/deontic split).** | When causal support and authority wording share a sentence, a conforming description **SHALL** use C.28 for the causal-use question and route each permission-looking claim to one `A6-AW-*` row. Neither result creates the other. | Prevents causal evidence from becoming hidden authority. |
| **CC-A.6.9 (Authority-wording split).** | Before authority-looking wording guides work or reliance, a conforming description **SHALL** select one `A6-AW-*` row per atomic permission claim and cite that row's source and direct object. | Prevents a visible word from becoming authority or evidence. |

### A.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti‑pattern                   | Symptom                                                         | Why it fails                                                                     | How to avoid / repair                                                                        |
| ------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Gate‑as‑law**                | Preconditions written as “laws” in the signature                | Breaks substitution; violates A.6.0’s separation of signature vs mechanism gates | Move predicates to Mechanism.AdmissibilityConditions; keep signature laws truth‑conditional. |
| **RFC‑keywords in invariants** | “MUST” appears inside `Definition:` blocks                      | Confuses deontics with mathematical admissibility; undermines auditability       | Rewrite as declarative predicate; reference predicates by ID or canonical location from CC when needed.               |
| **Paraphrase drift** | Same constraint restated across faces with changed meaning | Creates hidden divergence; breaks L/A/D/E claim-classification discipline and evidence accountability | Cite claim IDs or canonical locations and preserve their meaning in readable face prose. Use a Claim Register when stable reuse needs it. |
| **Interface-as-promiser and Work-result bundle** | “The interface promises delivery” assigns an individual commitment to the interface description, or “A.15.1 delivered the result” identifies Work with its result | A description is made an agent, while Work, result, transfer, evidence, and acceptance lose their own identity conditions | Name the actual bearer of the individual commitment; use A.6.C when ambiguity about promise, utterance, or governance changes interpretation or use. Use A.15.1 for dated Work; then exactly one applicable `A.15.1:4.6` row for each separate result, delivery, evidence, or acceptance claim. |
| **Carrier-as-effect guarantee** | “Guaranteed latency” or “the log proves the change” with no exact actual occurrence and evidence relation | A description or carrier is treated as creating Work, change, or another effect; natural or formal change may also be forced into Work | Name the actual occurrence first: A.15.1 for grounded Work, A.3/A.3.4 or the exact interaction or causal-use pattern for non-Work change; then add the minimum A.10 path needed for reliance. |
| **Face called a view by form** | A face, diagram, query result, or publication form is called `U.View` without exact E.17.0 conformance | Appearance or construction history replaces the dependent-kind condition | Recover the exact candidate and viewpoint epistemes, test E.17.0 conformance, and keep optional A.6.3 construction and publication relations separate. |
| **Unresolved deontic subject** | “The system or service SHALL …” is used without deciding whether the sentence states behavior, a general prescription, or an obtaining individual commitment. | The phrase hides the actual subject, constitutive basis, and direct predicate; a system-role kind or assignment may be mistaken for the duty bearer or for responsibility. | Recover the exact admitted System or other party; state an actual `E-*` behavior claim separately only when its actual basis is supplied; then state either normative content or one direct A.2.8 commitment. Test responsibility independently. |
| **One‑doc monoculture**        | Same document mixes unclassified laws, gates, duties, and evidence           | Change impact is hard to isolate; updates can affect unrelated claim kinds                            | Use the stack: separate Signature, Mechanism, Norms, and Evidence sections; classify by matrix.           |
| **Authority-word overread** | “Allowed”, “approved”, or a visible permit is treated as a complete authorization result | The word hides which claim exists and which source grounds it | Select one `A6-AW-*` row; if no row's closure condition is met, keep only `A6-AW-SOURCE` or stop the unsupported use. |

### A.6:9 - Consequences

| Benefits                                                                                                           | Trade‑offs / Mitigations                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **Evolvable boundaries.** Implementations can change while signatures remain stable.                               | More upfront structure; mitigated by MVPK faces that present only relevant slices per audience. |
| **Reduced category mistakes.** Object, description, and carrier confusion becomes detectable.                            | Requires discipline in writing; mitigated by the “Where statements go” classification examples.        |
| **Inputs for audit and replication.** Effect claims name their exact Work, transformation, interaction, evaluation, or other actual occurrence and use evidence carriers only through the needed evidence relation. | Requires identifying the applicable occurrence and evidence relations; a compact `AssuranceLane` evidence map can expose them. |
| **Clearer cross‑disciplinary communication.** Legal and compliance deontics no longer compete with math invariants.    | Teams must align on viewpoint responsibilities; mitigated by explicit viewpointRef in MVPK.     |

### A.6:10 - Rationale

The claims in a boundary description concern:

* a **mathematical object** (signature: operations over vocabulary, governed by laws),
* an **engineering boundary signature** (stable intent, evolvable implementations),
* a **governance object** (commitments, responsibilities, deontics), and
* **actual occurrences and evidence** (effects may arise through Work, natural or spontaneous transformation, formal change, or another directly governed interaction, and evidence supports but does not create them).

Mixing these claims makes it harder to distinguish a semantic boundary change from an implementation change, and to test each claim against its own rule and evidence.

The stack creates a default **direction of dependence**: higher layers constrain lower layers, not vice versa. The matrix creates a default **classification** that is not reliant on word choice alone and therefore survives natural‑language variation (“must”, “guarantee”, “valid”, “allowed”).

### A.6:11 - SoTA-Echoing

> **Informative.**

* **Adopt — algebraic effects and handlers / effect systems.** Effect systems distinguish operation signatures from handler semantics (e.g., Koka’s effect typing; effect handlers in OCaml 5). In this analogy, `U.Signature` carries the boundary declaration, A.6.1 governs operation declarations and their realization relation, and the realizing entity supplies the implementation. Substitution requires the declared meanings and applicability to be preserved.

* **Adopt — session and behavioural types for protocol boundaries.** Behavioural typing treats boundaries as typed interaction protocols with progress and safety properties. A.6’s classification matrix makes protocol laws (Quadrant L) explicit and separates entry gates (Quadrant A) from general prescriptions or exact individual commitments (Quadrant D) and runtime evidence (Quadrant E), reducing ambiguity.

* **Adapt — categorical optics, lenses, and bidirectional transformations.** Lenses supply useful construction expressions with coherence laws. FPF uses that lesson only for explicit A.6.3 construction or C.29 representation: a projection expression, publication face, and `U.View` remain different objects, while any cross-context reuse stays explicit.

* **Adapt — model-based views-as-queries practice.** Query and projection operations can construct candidate epistemes and make omissions inspectable. E.17.0 still tests each candidate independently against one exact viewpoint episteme; generation, selection, or a `viewpointRef` alone supplies no `U.View` membership.

* **Adapt — DDD bounded contexts and microservice contract-language practice.** Architecture practice keeps meaning local and makes crossings explicit. A.6’s stack and L/A/D/E claim-classification discipline provide a precise placement scheme for what belongs to the context boundary claim set, what belongs at the entry gate, what belongs to governance duties, and what belongs to observability evidence.

* **Adapt — observability as evidence discipline.** Traces, logs and metrics can supply evidence inputs for an exact claim. Use A.10 for the evidence-provenance relation and bounded reliance.

* **Adapt — Zero Trust, dynamic authorization, and policy-as-code practice.** Authorization practice separates policy, API, or schema text from a decision over subject, requested policy operation or work class, affected resource or work target, context, policy or gate version, decision source, and evidence. Cedar-style policy language and Zanzibar-style relation authorization are useful practice references for this split: the wording is not the decision. A.6 keeps policy, API, or schema wording in classified `L-*`, `A-*`, `D-*`, and `E-*` claims and uses `A.15.4` while appearance hides a prerequisite for work or reliance; `A.15` retains the enactment-alignment question.
* **Adopt, adapt, and reject stance for authority-looking boundary wording.** A.6 adopts policy-as-code separation of text from evaluated decisions, uses credentials and registers as source/currentness evidence, and rejects any visible wording or display as a substitute for the selected `A6-AW-*` branch.

* **Adapt — Markov blankets and active inference as probabilistic boundary views only after restoration.** Markov-blanket thinking can help pick observables and diagnose boundary-condition failures, but the source phrase must be restored before it carries an A.6 boundary claim. It may name accepted local Markov dynamics, a mathematical or probabilistic lens, a holon delimitation or crossing relation, an interface, an interface module, a physical component, a boundary description, or an agency-threshold claim. A.6 uses the phrase only after the boundary claim set is recovered; it does not replace deontics, invariants, admissibility gates, or the subject pattern of the physical or mathematical claim.

### A.6:12 - Relations


* **Uses A.6.B as the classification authority:** `A.6.B:8.4.1` selects the job of permission wording. A.6 maps the resulting atomic claim to the stack; it does not put every `A.2.8.PER` object in D. The filled case in `A.6.B:8.4.5.4` is the concrete handshake.
* **Coordinates actual effects without merging them:** Use A.15.1 only to identify a grounded dated Work occurrence; use A.3.4 for an independently identified actual transformation, including spontaneous or formal change with no Work; state each interaction, causal, production, speech-act, evaluation, evidence, or result claim through its applicable predicate and pattern. A description or carrier creates none of them.
* **Constrains signature writing:** Reinforces A.6.0 separation of Laws vs operational gates (AdmissibilityConditions live in mechanisms).
* **Constrains mechanism writing:** Uses A.6.1 for OperationAlgebra, LawSet, AdmissibilityConditions and Applicability; local transport and evidence-interface sections retain their own claim classification.
* **Requires EntityOfConcern and Description-episteme / publication-carrier discipline:** Uses A.7 to prevent category mistakes; ties evidence to evidence carriers and publication faces to descriptions.
* **Coordinates `U.View`, `U.Viewpoint`, and publication use:** E.17.0 governs viewpoint and view membership; MVPK selects exact epistemes, viewpoints, face uses, and publication forms; A.6.3 governs only optional source-to-receiving construction.
* **Unpacks “contract” talk:** When boundary ambiguity changes interpretation or use, A.6.C applies A.2.3, A.2.8, A.2.8.PER, and A.2.9 to keep promise content, speech act, commitment or grant explicit; use A.15.1 only to identify dated Work, and its §4.6 dispatch requires the exact subject predicate for each application-result, production, change, delivery/transfer, evidence, or acceptance claim.
* **Uses relation-specific declaration disciplines:** use A.6.5 when an already recovered direct relation needs reusable participant typing. Use A.6.6 when basedness wording hides the dependent, base or direct predicate; stop at the ordinary assertion when it answers the receiving question.
* **Coordinates with `C.28 CausalUse-CAL`:** When boundary prose uses causal-use evidence or a causal-use verdict to justify deployment, release, duty, commitment, or admissibility, A.6 splits the boundary sentence while `C.28` carries the causal-use question, `CausalityLadderRung`, estimand, support basis, support verdict, and supported causal use and unsupported causal use.
* **Coordinates work and consequences:** `A.15.1` supplies only a dated `U.Work` occurrence. Its §4.6 table routes an application/result binding, production, change, evaluation result, evidence use, delivery/transfer, and acceptance to separate subject patterns. `A.15`, `A.10`, `B.3`, `A.21`, and `A.20` govern the exact enactment-alignment, evidence, assurance, gate, or constraint claim when current.

### A.6:12a - Quantum-like boundary-claim classification note

Use A.6 first for ordinary boundary, interface, API, protocol, contract, connector, publication-face, and observability-evidence wording. Quantum-like boundary prose is supported only after the boundary text still needs a probe, order, frame, export, or state-reading distinction that ordinary boundary patterns would otherwise erase.

Action classification:

1. Identify the boundary sentence and name the boundary object in ordinary A.6 terms.
2. Name the actual participants and any channel or carrier required by the boundary relation or operation separately.
3. Apply the applicable ordinary FPF patterns to the ordinary boundary content: A.6, A.6.B, F.9, A.15, C.16, or C.25.
4. If the boundary text uses a coarsened representation to claim preserved action, intervention, manipulation, explanation, or preserved structure across representation scales, state the causal-abstraction or approximate-causal-abstraction mapping before retaining QL wording.
5. Ask whether the boundary act is being used as a passive read or unjustified lossless-transfer reading while actually changing the represented state, export validity, or viability decision.
6. If yes, apply `C.26.1` only to that remaining residual question; keep the ordinary boundary pattern active.
7. If no, keep the text in the ordinary boundary, bridge, work, measurement, or quality pattern and remove QL wording.

Minimum boundary discipline before a quantum-like boundary reading:

| Field | What the author names |
| --- | --- |
| Boundary | Which interface, protocol, context crossing, publication face, evidence boundary, or exact service/access relation is being described; when service/access wording hides the subject or relation, recover it through A.6.P:4.11a before using this table |
| Endpoints | Name the actual participants required by the boundary relation or operation, preserving their direct kinds. Use A.6.5 only when reusable participant typing is needed; its declaration slots are not actual participants. If bare *role* remains ambiguous, use E.10.ROLE before assigning it a participant meaning. |
| Channel or interaction | Name the actual interaction or operation under its direct predicate. Add a channel only when that predicate uses one. |
| Claimed state reading | What represented state is claimed before and after the act, and whether the act is treated as passive read, action, export, or probe |
| Evidence / carrier | Name the exact supported claim, evidence object and any carrier used for reliance through A.10. Keep a measurement value, observation, Work result and carrier in their own positions. |
| Export or loss | What is copied, transformed, no longer comparable, or not faithfully exportable |
| Ordinary pattern tried | Which of A.6, F.9, A.15, C.16, or C.25 already carries the baseline question |

Useful outputs:

- an L/A/D/E-classified boundary claim set when ordinary A.6 is enough;
- an F.9 Bridge and separate bounded-use claim when the export question concerns two exact local senses and the Bridge predicate obtains; add a Bridge Card only when durable packaging is useful;
- a C.26.1 probe-coupled boundary note only when the boundary act changes the represented state in a decision-relevant way;
- a relation repair using `A.6.P` when coupling words become reusable relation candidates, plus `F.18` only when the recovered relation term itself needs durable naming.

### A.6:End
