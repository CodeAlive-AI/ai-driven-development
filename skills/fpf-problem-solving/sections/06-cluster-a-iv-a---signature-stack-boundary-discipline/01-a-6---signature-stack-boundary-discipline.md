## A.6 - Signature Stack & Boundary Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Mixed (normative only where explicitly marked; claim-classification semantics live normatively in A.6.B)
> **Placement:** Part A → A.6.\* (cluster overview; coordinates A.6.0 / A.6.1 / A.6.3 / A.6.B / A.6.5 / A.6.6 / A.6.7)
> **Builds on:** E.8 (authoring template), A.6.B (Boundary Norm Square — quadrant semantics & link discipline), A.6.0 (U.Signature), A.6.1 (U.Mechanism), A.6.3 (optional source-to-receiving episteme construction), E.17.0 (viewpoint conformance and `U.View` membership), E.17 (MVPK — fixed face kinds & “no new semantics” publication), A.7 (EntityOfConcern and Description-episteme boundary; specification use and publication-carrier distinction), A.6.C, A.2.3, A.2.8, A.2.8.PER, and A.2.9 for promise-content, commitment, permission, speech-act, and work-and-evidence unpacking, F.18 only when recovered boundary terms need durable naming, E.10.D2 (EntityOfConcern and Description-episteme boundary; specification use and refinement discipline), E.10 publication face, form, unit, and carrier discipline
> **Purpose (one line):** Keep boundary claims evolvable by classifying each statement under the right layer of the Signature Stack and the right quadrant of the Boundary Norm Square (A.6.B).
>
> **Mint/reuse (terminology):** Mints “Signature Stack”, “Boundary Discipline Matrix”, and “Claim Register” as local authoring aids; reuses E.17.0 meanings of `U.View` and `U.Viewpoint`, with A.6.3 only for optional viewing construction, and uses publication face, publication form, or interop publication form terms for publication-use questions. The labels **L/A/D/E** used below are *claim-classification labels for statements*, not MVPK face kinds and not pattern IDs.
>
**Canonical companion.** The square itself (quadrant definitions, form constraints, and cross‑quadrant dependency discipline) is specified normatively in **A.6.B — Boundary Norm Square**. This overview only (i) maps quadrants onto the Signature Stack, and (ii) explains how MVPK faces project the canonical L/A/D/E-classified claim set. If anything in this overview conflicts with A.6.B, **A.6.B is authoritative**.

**Use this pattern when.** Use A.6 when a boundary package, API, protocol, contract, compliance statement, SLO/SLA, connector, interface, or publication boundary mixes definitions, admissibility predicates, duties, evidence, and work effects into one account.

**What goes wrong if missed.** Boundary prose starts doing too many jobs at once: invariants become permissions, permissions become duties, evidence becomes gate passage, and publication faces start acting as if they were the governed boundary object.

**What this buys.** The project gets an L/A/D/E-classified claim set with stable claim IDs, source references, stack placement, and publication-face citations, so work, reliance, evidence, commitment, and gate uses can return to their governing patterns.

**Start here when.** The dominant question is an API, protocol, contract, compliance, SLO or SLA, connector, interface, or publication boundary package whose statements are mixing runtime behaviour, governance, and evidence into one undifferentiated boundary account.

**First output.** One Claim Register or equivalent L/A/D/E-classified atomic claim set with stable `L-*`, `A-*`, `D-*`, and `E-*` identifiers, stack placement, and face citations by ID rather than paraphrase.

**Boundary-claim activation discipline.** Use only as much claim-classification structure as the live work claim or reliance claim requires. Split a statement only where one sentence carries more than one claim kind, `governingPatternRef` or `authoritySourceRef`, or work or reliance consequence, or where evidence, gate, duty, assurance, work occurrence, P2W class, admissible work, or admissible reliance would otherwise remain ambiguous. For a local first-pass repair, an equivalent L/A/D/E-classified claim set may be a two-to-four-row scratch table. Use a persistent Claim Register when the claim set is reused, published, audited, release-bearing, cross-context, or relied on by `A.15`, `A.10`, `B.3`, `A.21`, `A.20`, `A.2.8`, `A.2.8.PER`, `A.2.9`, or `A.15.1`. Do not atomize ordinary modifiers when one `governingPatternRef` or `authoritySourceRef` and one work or reliance consequence are already clear.

**Typical neighboring governing patterns and authority-reference repairs.** `A.6.B` for the quadrant semantics, `A.6.C` for contract unpacking, `A.6.P`, `C.16.Q`, or `A.6.A` for lexical repair, and `E.17` faces for audience-specific publication of the same decomposed claim set.

**Common neighboring-pattern mistakes.** If the real object is still cue preservation or an early unresolved cue, use `A.16` or `A.16.1`; if a qualified relation, quality term, or action invitation is itself being repaired, apply `A.6.P`, `C.16.Q`, or `A.6.A`; if duties, commitments, promise content, work effects, and evidence are being mixed into one contract sentence, split them through `A.6.B` and `A.6.C` rather than minting one more undifferentiated contract paragraph.

**Causal/deontic split.** A mixed boundary sentence such as "deploy because it would reduce harm" is not settled by one hidden pattern. `C.28` carries the causal-use question, `CausalityLadderRung`, estimand, support basis, support verdict, and supported causal use and unsupported causal use. `A.6.B` classifies deontic duties or permissions, boundary admissibility gates, and work-effects as atomic `L/A/D/E` claims. `A.6.C` unpacks contract, promise, commitment, permission, utterance, and boundary-publication language when the sentence is agreement-like or release-facing. A causal-use record does not by itself create a duty, commitment, permission result, promise, release gate, or boundary admissibility predicate.

**Authority wording split (subordinate boundary-claim stress case).** When a boundary, policy, API, schema, connector, or compliance statement uses "approved", "allowed", "authorized", "guaranteed", "certified", "recommended", or equivalent wording, do not decide by the word. The current object is still the L/A/D/E-classified boundary claim set: split the statement into `A.6.B` `L-*` definition or invariant claims, `A-*` admissibility or gate claims, `D-*` deontic claims, and `E-*` evidence or work-effect claims before treating it as action guidance. When "guaranteed", "promise", "contract", "SLA", "SLO", or certified-under-agreement wording is agreement-like, service-facing, promise-bearing, or release-facing, unpack promise content, utterance package, deontic commitment or permission result, and work or evidence substrate through `A.6.C`, `A.2.3`, `A.2.8`, `A.2.8.PER`, and `A.2.9` before using the L/A/D/E-classified claims. Duty, recommendation-as-duty, or prohibition uses `U.Commitment`; strong/weak permission, exercise, non-violation, or conflict uses the exact `A.2.8.PER` result; the instituting act stays in `A.2.9`. When "recommended" wording is cue preservation, advice, or action invitation, apply `A.16`, `A.16.1`, or `A.6.A` according to the current kind; when it is an admissibility criterion, use the `A-*` claim and any live `A.21` gate decision; when it is evidence-supported advice, use the `E-*` claim plus `A.10`; only recommendation-as-duty uses a `D-*` claim and `A.2.8`. If the reliance appearance is a dashboard or status display rather than boundary prose, do not turn color, label, or visible status into an `A-*` admissibility claim; return through `A.15`, `A.10`, and, when a gate decision is live, `A.21`. If the split result will guide work, release, permission, role or status reliance, evidence reliance, or assurance, return through `A.15` to the governing FPF pattern and project-side FPF kind and reference named by value that carry the claim being made or effect.

**Positive repaired result.** A repaired boundary statement is not merely "less vague"; it is an L/A/D/E-classified claim set that tells the user which statement is definitional, which is an admissibility predicate, which is an accountable commitment or exact permission result, which is an evidence or work-effect claim, and which FPF pattern or project-side FPF kind and reference named by value must be cited before the work claim or reliance claim is used.

**Credential-currentness boundary.** A displayed credential can substantiate only issuer, holder, verifier, status, and currentness claims after an `A.10` evidence relation verifies it for the relying context. Strong permission, permission exercise, weak non-prohibition/non-violation, or conflict needs `A.2.8.PER`; an actual commitment needs `A.2.8`; an instituting act needs `A.2.9`; role/status effects need `A.2.1`; classification and entry predicates need `A.6.B`; and gate passage needs `A.21`, each with the governing source named by value.

**Register-backed status boundary.** A pass, badge, dashboard cell, API response, certificate view, or other status-looking item may be only a publication of a governing register entry or status-source entry. If that entry creates or changes an effect, cite the register entry or status-source entry named by value and the direct owner: `A.2.8.PER` for a strong grant, exercise, weak non-prohibition/non-violation finding, or permission conflict; `A.2.8` only for an actual obligation, recommendation-as-duty, or prohibition; `A.2.9` for the instituting act; `A.2.1` for role/status effects; `A.6.B` for claim classification; and `A.21` for gate effects. If the item is only an extract, cache, screenshot, certificate view, or convenience display, keep it as source-finding or currentness support under `A.10` until the exact source is recoverable.

**Conflicting-source boundary.** When classified boundary wording, a display, copied summary, current source, gate decision, credential status, register entry, status-source display, recency signal, or provenance label disagree, do not resolve by wording emphasis, visual salience, color, or apparent freshness. Name the source order, decision source, freshness policy, and supersession rule; until those are resolved, keep only cue use, source-finding, or bounded reversible probes available.

**Adversarial wording guard.** Do not let intentionally ambiguous "allowed", "approved", "authorized", "certified", "recommended", or "guaranteed" wording collapse `L-*`, `A-*`, `D-*`, and `E-*` claims. Split the boundary statement first, then cite the supporting source named by value for the live work use, reliance use, evidence use, gate use, commitment use, permission-result use, or assurance use.

**Lint trigger.** In boundary, API, schema, or policy text, `approved`, `authorized`, `allowed`, `guaranteed`, `certified`, or `recommended` should trigger the A.6 split: identify the `L-*`, `A-*`, `D-*`, and `E-*` claims, then cite the exact source before work use, reliance use, evidence use, gate use, commitment use, permission-result use, or assurance use.

**Boundary and source repair assignment.** If splitting boundary wording exposes a missing or broken `L-*`, `A-*`, `D-*`, or `E-*` source, assign repair to the accountable boundary-maintenance or source-maintenance role assignment: boundary author, policy or schema maintainer, gate source, commitment source, permission-result source, evidence-carrier source, or publication face maintainer. Keep only cue use, source-finding, or bounded reversible use available until that source is exposed or repaired.

Role prompts for boundary wording use:

| Role in the situation | Prompt |
| --- | --- |
| Boundary author | Which words need L/A/D/E claim IDs before they can guide work or reliance? |
| Policy, API, or schema maintainer | Which `L-*`, `A-*`, `D-*`, and `E-*` claims must be separated, and which source carries each one? |
| Acting user | Is the wording only a cue or source-finding handle, or is there support relation named by value for the required source-backed claim or effect? |
| Gate, commitment, permission-result, or evidence source | Which gate decision, commitment, exact `A.2.8.PER` result, speech act, evidence relation, or work-effect source must be exposed or repaired? |
| Auditor or reviewer | Which L/A/D/E claim IDs are cited by each publication face, and where would paraphrase drift change the allowed use? |

**Recurring boundary ambiguity repair.** If the same boundary, API, schema, or interface wording repeatedly needs the same split or source recovery, repair the boundary package rather than making each user reinterpret it: replace misleading labels, expose L/A/D/E claim IDs, cite the gate source, commitment source, permission-result source, evidence source, or work-effect source, add currentness or supersession refs, or remove the phrase that invites unsupported work claims or reliance claims. Repetition is a signal that the boundary source or publication face needs repair, not a normal per-use task.

Display guidance for boundary wording: a publication face, API doc, schema page, connector card, or compliance statement that uses approval-, authorization-, permission-, recommendation-, certification-, or guarantee-like wording should expose the `L-*`, `A-*`, `D-*`, and `E-*` claim IDs, the source for each live work claim or reliance claim, freshness and supersession refs where currentness matters, and unsupported work claims, reliance claims, or effects. If it cannot expose those, keep the wording as source-finding or repair the boundary package.

Incident-learning fields for boundary wording overread: displayed phrase, intended next work occurrence or reliance use, required source-backed claim or effect, missing or ambiguous L/A/D/E claim ID, exact `L-*`, `A-*`, `D-*`, or `E-*` source needed, plausible overread, safe disposition used now, and upstream repair item for labels, L/A/D/E claim IDs, source refs, currentness refs, supersession refs, or publication-face wording.

**Conventions:** The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **SHALL** are to be interpreted as in RFC 2119/8174. Lower-case `must`, `may`, and `should` in explanatory prose is descriptive, not normative.

**Statement identifiers (recommended):** Adopt the quadrant‑prefixed ID scheme from **A.6.B:0** for classifiable statements:
`L-*` (law or definition), `A-*` (admissibility gate), `D-*` (deontic or commitment), `E-*` (effect or evidence).
Other sections and faces **SHOULD** refer to these IDs instead of restating the same constraint in new words.
IDs are intended to be “lintable” identifiers (and are especially useful when D‑duties enforce A‑gates or E‑claims). Consider pairing IDs with a lightweight Claim Register (A.6.B:7) to reduce paraphrase drift across faces.
**Non-collision note (informative):** The `A-*` prefix here is “Admissibility”, not Part‑A numbering and not MVPK’s `AssuranceLane` face kind. If this is a readability hazard in your program, prefer an explicit `G-*` (“Gate”) local convention while keeping the quadrant name “Admissibility”.

**Admissibility-predicate distinction (informative):** An `A-*` claim is a mechanism admissibility predicate or entry condition inside the L/A/D/E-classified boundary claim set. It is not an `A.21` `GateDecision`, `DecisionLogRef`, or proof that a gate passed. An `A-*` claim may name a condition that a later `A.21` gate evaluates; actual gate passage needs the `A.21` source. An `A.20` `ConstraintValidity` witness remains separate from both the predicate and the gate decision.

**Claim Register (informative, recommended).** Use the Claim Register mini‑record in **A.6.B:7**. In this cluster the register is additionally used to record stack placement (Signature, Mechanism, Norms, and Evidence) and the MVPK faces that cite each claim (`viewRef`/`viewpointRef`), so “no paraphrase drift” can be audited mechanically.

### A.6:1 - Problem frame

Boundaries are where architecture lives: at the edge of a theory, an API, a protocol, a hardware connector, an organisational interface, or a published model. FPF already has the core building blocks to describe such edges:

* `U.Signature` as a *public, law‑governed declaration* (with Vocabulary, Laws, Applicability).
* `U.Mechanism` as a specialization that introduces operational “entry gates” (AdmissibilityConditions) and additional operational blocks (Transport, Audit, etc.).
* Multi-view describing through E.17.0 `MultiViewDescribing`, plus separate E.17 publication discipline for selected epistemes, face uses, forms, and carriers.
* Strict separation of **EntityOfConcern vs Description episteme vs publication carrier** so we do not accidentally attribute agency or work to an episteme, or treat a file as the entity, claim, work, evidence, or decision.

Yet boundary descriptions in practice fail in a predictable way: authors blend several fundamentally different kinds of claims into one undifferentiated contract paragraph. The result is brittle architecture: signatures become entangled with runtime gates, deontic language is mixed into mathematical invariants, and “effects” are asserted without any disciplined carrier and evidence story.

This cluster overview makes one disciplined move:

1. Treat a boundary as a **stack of boundary layers** (Signature → Mechanism → work and evidence carriers) plus publication views and faces, and
2. Provide a **boundary discipline matrix** (2×2) that classifies statements by boundary layer, so evolution remains controlled and substitutions are possible.

*Terminology note (informative):* In this pattern:
* **Layer** names a stratum in the boundary stack (Signature → Mechanism → work and evidence carriers → Publication).
* **View** (`U.View`) is the same C.2.1 episteme individual when E.17.0 conformance to at least one exact viewpoint episteme obtains; it is not a projection operation, publication file, or document.
* **Viewpoint** (`U.Viewpoint`) is the same C.2.1 episteme individual when the fixed E.17.0 viewpoint-convention conditions obtain; its accountability use does not replace those membership conditions.
* **Face** (MVPK sense) is one named publication-use class (`PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane`). A face may select an episteme that independently has `U.View` membership, but the face, publication form, rendering, and carrier are not that view. Do not coin “signature or mechanism ...Surface” terms; use publication face, form, unit, carrier, and rendering terms only when publication use is live.

### A.6:2 - Problem

When boundaries are described without an L/A/D/E claim-classification discipline, four confusions dominate:

1. **Laws vs admissibility.** Authors encode runtime gate predicates as “laws”, or write invariants using RFC‑style deontic verbs, blurring “what is true or defined” with “what is allowed to be applied”. FPF explicitly separates these: operational guard predicates belong to mechanisms (A.6.1), not signatures (A.6.0).
   *Common mistake #0 — Applicability ≠ Admissibility (informative):* Signature `Applicability` scopes declared admissible use and bounded context; it is not a runtime entry gate. Runtime entry checks and admissibility predicates belong in `U.Mechanism.AdmissibilityConditions` as `A-*`. An `A-*` predicate may consume a current `A.2.8.PER` permission result as one condition, but it is not that result and does not institute a grant. If an accountable role assignment or admitted acting system is obligated to satisfy or enforce such a gate, express that as a `D-*` duty that references the `A-*` claim ID (per A.6.B), not by rewriting the gate as "X MUST …".

2. **Admissibility vs deontics.** RFC keywords such as `MUST`, `SHOULD`, and `MAY` can mask three distinct semantic destinations: an accountable duty, recommendation-as-duty, or prohibition commitment under `A.2.8`; an exact strong/weak permission result under `A.2.8.PER`; or a world-state entry/admissibility predicate under A.6.1. The keyword alone selects none. E.8 already requires deontics to remain distinct from admissibility and definitions and recommends predicate-style constraints for admissibility rather than RFC keywords.

3. **Contract talk category errors.** “The interface promises…” is a metaphor. Promise content, speech act, commitment, permission result, and delivered work are different FPF objects: A.2.3 owns promise content, A.2.9 the communicative work, A.2.8 accountable duty/recommendation/prohibition, A.2.8.PER strong/weak permission and exercise/conflict, and A.15.1 delivered work with its evidence relations. A.6.C unpacks the boundary case; F.18 only names recovered terms when durable naming is current.

4. **Effects without evidence or carriers.** Effects happen only in work; therefore, “effect claims” must be anchored to observation and carriers. Without A.7’s EntityOfConcern and Description-episteme / publication-carrier discipline, writers conflate the published description with runtime traces or treat a file as the system itself.

These confusions destroy evolvability: you cannot swap implementations behind a stable signature if the signature already smuggles mechanism‑gates, audit logistics, or role-assignment commitments into “laws”.

### A.6:3 - Forces

| Force                                        | Tension                                                                                                                                                            |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Modularity vs expressiveness**             | A stable boundary must be abstract, but users want operational detail “in the same doc”.                                                                           |
| **Truth vs governance**                      | Definitions and invariants (“is”, “iff”, “∀”) vs permissions and obligations (the RFC keywords `MUST`, `SHOULD`, and `MAY`).                                                                          |
| **Design‑time clarity vs run‑time evidence** | What can be checked statically vs what requires executing work and observing traces.                                                                               |
| **View, viewpoint, and construction discipline** | A view is an episteme satisfying exact viewpoint conformance; a viewpoint is an exact convention-bearing episteme; optional A.6.3 construction and publication remain different relations. Losing any distinction makes omissions and provenance uninterpretable. |
| **Local meaning vs cross‑context reuse**     | Boundaries should be local to a bounded context; reuse must be explicit (Bridge and CL), not hidden.                                                                  |
| **Evolvability vs auditability**             | Evolving interfaces requires change; auditors require stable evidence trails.                                                                                      |
| **Human readability vs formal precision**    | Plain explanations vs tech‑register constraints; both must remain aligned.                                                                                         |

### A.6:4 - Solution — A stack + a classification matrix

#### A.6:4.1 - Why “stack”: what is stacked, and what “higher and lower” means

This pattern uses **stack** in the same pragmatic sense as other FPF stacks (e.g., the holonic import stack and other layered disciplines): an ordered set of layers where **higher layers are more stable commitments**, and **lower layers are more volatile realizations and evidence**. “Higher” and “lower” are not metaphysical claims; they are **engineering guidance for evolvability**:

* **Higher in the stack** = closer to *public, reusable boundary intent*.
* **Lower in the stack** = closer to *execution, implementation, and evidence* (what is actually done and observed).

This is consistent with existing “stack discipline” uses in FPF (e.g., import layering over holonic strata).

The **Signature Stack** (as used in this cluster) is the ordered family of **canonical claim layers** for a boundary package. Each layer is a stable canonical placement for one quadrant of statements (L/A/D/E), with a canonical boundary publication form or section that carries those statements:

1. **Signature layer (L: laws or definitions).** `U.Signature` provides the stable declarative boundary: Vocabulary + Laws + Applicability, without runtime gate predicates.

2. **Mechanism layer (A: admissibility gates).** `U.Mechanism` specializes the signature and adds **AdmissibilityConditions** (the entry gate) plus operational blocks (e.g., Transport, Audit and observability). These blocks specify runtime gates and observability *interfaces*; they are still **descriptions**. The evidence itself exists only as carriers produced in work.

   *Audit vs AssuranceLane (avoid duplication):* the Mechanism’s **Audit and observability** block defines the required semantics of an observability and evidence interface (carrier classes and required fields, correlation keys, exposure interface). **Retention, access, and enforcement are D‑claims** (role-assignment or acting-system duties) that reference the same carrier classes by ID. An MVPK **AssuranceLane** is a projection for auditors that explains how to adjudicate the evidence interface. This is a special case of CC‑A.6.6: the `AssuranceLane` face references the Mechanism section and the relevant claim IDs rather than restating semantics.

3. **Deontic layer (D: commitments and permission results).** Duty, recommendation-as-duty, and prohibition statements are bound to accountable role assignments, role values, or admitted acting systems and use `A.2.8 U.Commitment`; strong/weak permission, exercise, non-violation, and conflict statements use their exact `A.2.8.PER` result and beneficiary. Canonical placement is a deontic section in the boundary package (typically rendered inside `TechCard`), and those statements reference `L-*`/`A-*`/`E-*` by ID rather than duplicating predicates.

4. **Evidence bindings layer (E: effects and evidence).** `E-*` claims bind observed behaviour to **carrier classes** and measurement conditions. Canonical placement is an Evidence-and-carriers section in the boundary package (typically rendered in `AssuranceLane`), and adjudication happens against carriers produced in work.

5. **Work & realizations (outside the description stack).** Realizations (substitutable implementations) are exercised by doing work; actual executions produce state changes, traces, and measurements. Effects exist only in work. A.6.0 already frames realizations as substitutable behind signatures and warns against smuggling bridge mechanics into the signature layer.

6. **Publication faces.** MVPK selects exact epistemes and publication forms for audience-specific face uses. A selected episteme has `U.View` membership only when E.17.0 conformance to the exact viewpoint episteme obtains; any A.6.3 source-to-receiving construction remains separate. The face class, publication occurrence, form, rendering, and carrier are not the `U.View`.

*Observability compatibility note (informative):* When specifying evidence carriers and correlation rules, it is often convenient to describe evidence-carrier classes in terms familiar from contemporary observability practice (post‑2015): traces and spans, logs and log records, and metrics time-series, with explicit correlation identifiers. Treat these as example *carrier schemas and join keys*, not as mandatory technology choices. (Concrete schema/exchange mapping remains outside Part E; keep Part E conceptual.)

##### A.6:4.1.1 - AssuranceLane skeleton (informative)

An MVPK **AssuranceLane** is a view that teaches a specific audience how to adjudicate `E-*` claims against carriers produced in work. It references (not restate) the Mechanism’s Audit and observability semantics.

Minimal content (suggested):
- **Scope:** boundaryRef, version, viewRef, viewpointRef.
- **Carrier inventory:** carrier-class and carrier-schema refs (A.7 Carrier) + where to obtain them.
- **E‑claim map:** a table keyed by `E-*` ID with: measurement conditions, carrierRef(s), join and correlation keys, and a reference to the canonical `E-*` text that defines pass or fail criteria.
- **Operational policies:** references to relevant `D-*` duties (retention, access control, exposure), without redefining them.
- **Limitations:** sampling, redaction, missing signals, expected false negatives and false positives.

**No new semantics reminder.** The `AssuranceLane` face may include *procedural* adjudication guidance (queries, joins, dashboards) as informative text. Any normative thresholds or criteria that would change the boundary’s commitments or permission results **MUST** be authored as `E-*` claims in the canonical Evidence-and-carriers section, while any changed `U.Commitment` or `A.2.8.PER` object is repaired at its direct owner; both are cited by ID rather than introduced only inside `AssuranceLane` face text.

Example (conceptual, no tools):

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
        conditions: "on every rejection due to A-AC-1"
        vantage: "Operator and auditor pipeline"
        correlation: ["traceId", "requestId"]
      adjudication:
        check: "query audit stream for code=NotAdmissible and join to traceId"
        criteriaRef: "E-OBS-1 (pass or fail criteria live canonically in the E-claim)"
      references: [A-AC-1, D-RET-1, Mechanism.AuditObservability]
```

Default placements (quadrant → stack layer / section):

* **L →** Signature.Laws (and, where appropriate, mechanism‑local semantic laws; never runtime gates)
* **A →** Mechanism.AdmissibilityConditions
* **D →** Deontic claims: accountable duty/recommendation/prohibition commitments under `A.2.8`, including publication and accountability duties, or the exact strong/weak permission, exercise, non-violation, or conflict result under `A.2.8.PER`
* **E →** Evidence-and-carriers (claims adjudicated against work via carriers; the publication face for these is typically `AssuranceLane`)

**Integration stitches (informative; this cluster is a classification hub, not a standalone philosophy):**
* **A.6.1 ↔ A‑quadrant:** `U.Mechanism.AdmissibilityConditions` is the canonical claim layer for `A-*` gate and admissibility claims.
* **A.10 / B.3 ↔ E‑quadrant:** `E-*` claims should cite evidence carriers and provenance (A.10); without an explicit evidence-carrier reference they are treated as `AssuranceLevel:L0 (Unsubstantiated)` in the Trust & Assurance calculus (B.3).
* **A.2.3 and F.12 ↔ D/E separation:** a `U.PromiseContent` promise is not evidence; promise acceptance is linked to work evidence via F.12, and role obligations to maintain admissibility are expressed as `D-*` duties referencing `A-*` and `E-*` by ID when needed.

 A stack is useful because the intended direction of change is clear:

* Lower layers (realizations, audit formats, transport mechanisms) are expected to change more frequently and can often evolve without forcing higher‑layer changes, provided higher‑layer commitments remain satisfied.
* Changes to higher layers are boundary-claim evolution and typically require explicit compatibility reasoning (and therefore explicit versioning and communication).

#### A.6:4.2 - Boundary Discipline Matrix: classify by A.6.B (the Boundary Norm Square)

**Normative source.** The canonical 2×2 square (the two A.6.B distinctions, quadrant semantics, form constraints, and cross‑quadrant reference rules) is defined in **A.6.B**. This section provides a short operational summary and worked rewrites only.

A “four‑part list” is insufficient, because real sentences reuse the same visible words (“must”, “guarantees”, “valid”) across different logical roles. A **2×2 matrix** is better fit because it arises from crossing **two independent distinctions**:

* **Modality family:** truth-conditional vs governance; governance still separates `U.Commitment` duty/recommendation/prohibition from `A.2.8.PER` permission results.
* **Adjudication substrate:** in‑description vs in‑work (whether satisfaction is decided from the description alone or requires observing executed work and carriers).

Operational summary (quadrant → canonical claim layer in the stack):
* **L** (Laws & Definitions) → `Signature.Laws` (truth‑conditional semantics, in‑description)
* **A** (Admissibility & Gates) → `Mechanism.AdmissibilityConditions` (runtime entry predicates; a predicate may check a current permission result but is not that permission)
* **D** (Deontics) → duty/recommendation/prohibition claims cite `A.2.8 U.Commitment`; strong/weak permission, exercise, non-violation, and conflict claims cite the exact `A.2.8.PER` result; either may reference `E-*` without becoming evidence
* **E** (Work‑Effects & Evidence) → Evidence-and-carriers (work‑adjudicated effects tied to carriers and measurement conditions)

Atomicity rule:

If a sentence mixes roles (e.g., “MUST” + a gate predicate + an effect claim), it is **not classifiable** as a single statement. Per **A.6.B**, split it into **atomic** claims so each one has exactly one quadrant (and, ideally, an identifier you can reference).

Micro‑template: **Atomize → Classify → Place → Bind to EntityOfConcern, Description, or carrier → Register**

1. **Split** the sentence into atomic claims (one logical role each).
2. **Assign** each claim to exactly one quadrant (L/A/D/E) using the matrix.
3. **Place** each claim into its correct section or publication form (stack layer + section).
4. **Anchor A.7:** for each claim, name the primary A.7 side it is *about* (`EntityOfConcern`, Description episteme, or publication carrier) and make the binding branch-specific: an `A.2.8 U.Commitment` `D-*` claim names its accountable role assignment, role value, or admitted acting system; an `A.2.8.PER` `D-*` claim cites the exact selected permission object and preserves its own participants and references; an `E-*` claim names its carriers.
5. **Register:** add the atomic claim to the Claim Register (if used) and ensure every downstream face references the claim by ID rather than paraphrasing.

Action outputs after classification:

- implement or repair an admissibility predicate when the claim being made is `A-*`;
- assign, remove, or clarify an accountable role assignment, `U.Commitment`, or exact `A.2.8.PER` permission result when the claim being made is `D-*`;
- add, repair, or expose evidence-carrier instrumentation when the claim being made is `E-*`;
- publish or update an MVPK face that cites L/A/D/E claim IDs rather than paraphrasing them;
- reopen an `A.21` gate decision, `A.20` constraint-validity witness, `A.2.9` speech act, `A.2.8` commitment, `A.2.8.PER` grant/finding/exercise/conflict result, `A.10` evidence relation, or `B.3` assurance claim when the L/A/D/E-classified statement is being used beyond boundary wording;
- downgrade the visible wording to cue use or source-finding only when the exact source is missing;
- keep the work claim or reliance claim local, reversible, or blocked only for the unsupported work claim or reliance claim while the source is repaired.

> **Informative example.** Example rewrite (mixed → atomic):

*Before (mixed, not classifiable yet):* “Clients **MUST** include header `X`; otherwise the request is invalid and the system logs `NotAdmissible`.”

*After (classifiable + lintable):*
* `A-AC-1` (Quadrant A, Mechanism.AdmissibilityConditions): `admissible(req) iff hasHeader(req, "X")`.
* `D-CL-1` (Quadrant D, Norms-and-commitments): “Client implementers **MUST** satisfy `A-AC-1`.”
* `E-OBS-1` (Quadrant E, Evidence-and-carriers): “When a request is rejected due to `A-AC-1`, an `AuditLogEntry{code="NotAdmissible"}` carrier is produced and can be observed in the audit stream.”

> **Informative example.** Example rewrite (guarantee + SLA + measurement + enforcement):
>
> *Before (mixed contract prose):* “The service **guarantees** 99.9% availability per calendar month and **MUST** keep p95 latency under 200ms; breaches are penalized; operators **SHALL** alert on violations.”
>
> *After (classifiable + adjudicable):*
> * `D-SLA-1` (Quadrant D, Commitments and SLA): “Provider **SHALL** meet `E-SLA-AVAIL-1` and `E-SLA-LAT-1` under the stated exclusions.”
> * `E-SLA-AVAIL-1` (Quadrant E, Evidence-and-carriers): “`availability ≥ 0.999` over calendar month `T`, measured by carrier `UptimeProbeSeries` from viewpoint `VP.ExternalMonitor`.”
> * `E-SLA-LAT-1` (Quadrant E, Evidence-and-carriers): “`latency_p95 ≤ 200ms` under workload `W`, measured by carrier `LatencyMetricSeries` from viewpoint `VP.Client`.”
> * `D-OPS-ALERT-1` (Quadrant D, Ops duty): “Operators **MUST** page on breach of `E-SLA-AVAIL-1` or `E-SLA-LAT-1` within 5 minutes (policy).”
> * `E-ALERT-1` (Quadrant E, Evidence-and-carriers): “Pages are evidenced by carrier `AlertEvent{ruleId,firedAt,target}` and can be joined via `incidentId`.”

See **A.6.B:4–A.6.B:6** for the normative square, quadrant form constraints, and explicit cross‑quadrant link patterns (notably: **D→A**, **E→A**, **D→E**, and **A/E→L**).

##### A.6:4.2.1 - Authority-wording split examples

These examples are informative. They show how to keep mixed authority prose from becoming evidence, assurance, commitment, gate passage, or work by wording alone.

*Before (mixed):* "This API is approved for production use and guarantees safe rollback."

*After (classifiable + source-ready):*
* `L-API-1` (Quadrant L): the API operation and rollback terms are defined in the signature vocabulary.
* `A-API-1` (Quadrant A): a request is admissible only under the named subject, action, object, context, and policy-version predicate.
* `D-API-1` (Quadrant D): the accountable provider or operator commits to maintain or enforce `A-API-1` under the named window and exclusions.
* `E-API-1` (Quadrant E): rollback success is evidenced only by the named work traces, audit records, or metrics; a gate decision carrier can support gate passage, but not rollback execution by itself.

Then:
- if a user is deciding whether the wording may guide action, enter `A.15`;
- if evidence, currentness, or provenance is live, attach the `A.10` evidence relation;
- if trust, readiness, compliance, or release confidence is being raised, build the `B.3` assurance tuple;
- if an actual gate decision or gate passage is asserted, cite `A.21` `OperationalGate(profile)`, `GateDecision`, and `DecisionLogRef`;
- if a flow witness or constraint witness is asserted, cite `A.20` `ConstraintValidity` status or witness;
- if an exact strong/weak permission, exercise, non-violation, or conflict result is asserted, cite the selected `A.2.8.PER` object and its governing references; an `A-*` predicate or gate decision does not substitute for it;
- if release, deployment, rollback, or execution work is asserted, cite `A.15.1` dated `U.Work` occurrence plus its `A.10` evidence carrier relation;
- if the phrase is only an action invitation or cue, keep it in `A.6.A`, `A.16`, or `A.16.1` according to the current kind.

Policy-as-code, dynamic authorization, credential, register-backed status, provenance, attestation, and assurance practices support complementary parts of this split: policy engines support bounded authorization decisions; credentials support issuer, holder, verifier, and status claims; governing registers or status-source entries may carry role effects, status effects, permission, duty, or gate-state effects only when the bounded context gives that source such force; provenance and attestation support bounded origin or process claims; assurance practice supports claim-argument-evidence confidence claims. None of them lets wording, a displayed credential, a register excerpt, a provenance label, or a schema cue stand in for the subject named by value, requested policy operation or work class, affected resource or work target, context, policy or gate version, evidence refs, validity or revocation window, gate decision, or work occurrence needed for work use or reliance use.

#### A.6:4.3 - View membership needs exact viewpoint conformance

`MultiViewDescribing` makes the candidate episteme and exact viewpoint episteme explicit. The candidate has `U.View` membership only when E.17.0 conformance obtains. A projection or query may participate in an A.6.3 construction, but that construction does not establish membership. MVPK separately fixes a closed set of publication face classes (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`).

A disciplined stack therefore requires:

* Every published face use identifies the exact selected episteme, the exact viewpoint episteme through `U.ViewpointRef`, the publication occurrence, the form, and the carrier. The face class is not any of those objects.
* Calling the selected episteme a `U.View` requires E.17.0 conformance; a face label, viewpoint reference, projection history, or publication does not establish it.
* Per **E.17** (“no new semantics”), a face **MUST NOT** introduce new semantic commitments or permission results beyond the boundary’s **canonical L/A/D/E-classified claim set** (the authoritative `L-*`, `A-*`, `D-*`, and `E-*` statements at their canonical locations). A face **MAY** add informative explanation, examples, and cross‑references, provided they are clearly marked as informative. Any **normative** sentence on a face **MUST** cite the L/A/D/E claim ID(s) and direct object it depends on (or be moved into the canonical claim set); paraphrase is allowed only as explicitly informative text.
* Per **E.17** and **publication-face and publication-form discipline** (face‑kind closure), a publication package that claims MVPK alignment **MUST NOT** mint additional MVPK face kinds (e.g., “EvidenceCard”, “NormsCard”) as if they were first‑class kinds; if you need local headings, keep them as sections within the canonical face kinds.

#### A.6:4.4 - “Contract” unpacking: avoid assigning agency to epistemes

When practitioners say “the API contract”, they usually compress multiple distinct things into one word. The governing split is the **A.6.C Contract Bundle**: promise content, utterance package or speech act, a deontic position whose commitment and permission branches stay separate, and work plus evidence. Boundary engineering keeps that split inside the L/A/D/E claim set:

* **Promise content (promise content; `U.PromiseContent`, A.2.3):** what is promised to be made available to eligible consumers — **a promise, not execution** (`U.Work`).
* **Utterance package (published descriptions + instituting act):** what is said and published and versioned (signature or mechanism descriptions plus MVPK faces), plus the `U.SpeechAct <: U.Work` that published or approved it when provenance matters (A.2.9).
* **Commitment (deontic commitment relation; `U.Commitment`, A.2.8):** what an accountable role assignment, `U.Role`, or admitted acting system is obligated, recommended-as-duty, or prohibited to do (often: to satisfy a promise content).
* **Permission (`A.2.8.PER`):** an exact strong grant, weak non-prohibition/non-violation finding, actual exercise relation, or conflict finding. It is neither a commitment modality nor an entry predicate.
* **Work + Evidence (adjudication substrate; `U.Work` + carriers):** what actually happens and what carriers and traces can adjudicate commitments, permission exercise or non-violation findings when current, and operational guarantees.

In A.6 terms:

* The **signature** is the *utterance substrate* for the boundary; it is not itself a promiser or obligor (A.7).
* Deontic claims belong to accountable role assignments, role values, admitted acting systems, or exact permission beneficiaries. Duty/recommendation/prohibition uses `D-*` plus `U.Commitment`; strong/weak permission, exercise, non-violation, and conflict use `D-*` plus the exact `A.2.8.PER` result. Both reference `L-*`, `A-*`, or `E-*` by ID without collapsing into them.
* Operational “guarantees” are empty rhetoric unless they are classified as either **L** (truth-conditional law), **D** (accountable commitment or exact permission result), or **E** (measured property with evidence).

This paragraph is a compact reminder; the reusable expansion (including “Service ≠ Work” discipline, claim‑ID link hygiene, and MVPK face projection rules) is **A.6.C — Contract Unpacking for Boundaries**.

#### A.6:4.5 - Where statements go (classification examples)

> **Informative.** Classification examples for learning the discipline; they do not add requirements beyond A.6:7.

The table below intentionally uses near‑everyday spec phrases. The same visible words appear in different quadrants depending on what they *do*.

| ID | Example statement (typical wording) | Matrix quadrant | Put it under… | A.7 primary layer |
| --- | --- | ---: | --- | --- |
| `L-1` | “`op f` is **defined iff** `P(x)` holds.” | L | Signature → **Laws** (`Definition:`) | Description |
| `L-2` | “For all requests, `idempotencyKey` is **unique** per subject.” | L | Signature → **Laws** (`Invariant:`) | Description |
| `A-1` | “The mechanism may be applied only if `tokenValid`.” *(rewrite as predicate: `admissible(req) iff tokenValid(req)`)* | A | Mechanism → **AdmissibilityConditions** (entry gate) | Description |
| `A-2` | “A request is admissible only if header `X` is present.” | A | Mechanism → **AdmissibilityConditions** | Description |
| `D-1` | “Client implementers **MUST** satisfy `A-2`.” | D | Norms-and-commitments (role duty; reference gate ID) | Object |
| `D-2` | “Authors **MUST** publish a versioned MVPK face for this boundary.” | D | Conformance Checklist and publication norms (authoring plane) | Object |
| `D-3` | “Operators **SHOULD** rotate keys every 90 days.” | D | Norms (role-assignment obligation; link to role and method claim IDs where applicable) | Object |
| `D-4` | “Implementers **MUST** expose audit‑log carriers via endpoint `/audit`.” | D | Norms-and-commitments (exposure duty) *about carriers* | Carrier |
| `D-5` | “The vendor commits to `99.9%` availability over window `T` (SLA).” | D | Commitments and SLA (identify committing role assignment or admitted acting system, window, exclusions) | Object |
| `E-1` | “When a state change occurs, an `AuditRecord` carrier is produced and can be observed in the audit stream.” | E | Evidence and observability: expected trace semantics; bind to carriers + conditions | Carrier |
| `D-6` | “Operators **MUST** retain audit‑log carriers for 30 days.” | D | Retention policy (deontic) *about carriers* | Carrier |
| `E-2` | “`latency_p95 ≤ 200ms` under workload `W` as measured by carrier `LatencyMetricSeries` from collector `C`.” | E | Evidence claim with measurement conditions | Carrier |

Notes:

* The classification is not just about modal verbs. “Shall” can be D (a duty) or A (a gate behavior). “Guarantees” can be D (a commitment) or E (a measured property). The matrix forces disambiguation.
* If a sentence reads like “X **MUST** … if … then …”, it almost always bundles multiple quadrants. Split into (A) a gate predicate (`A-*`), (D) an enforcement duty on a role assignment, `U.Role`, or admitted acting system (`D-*` referencing the gate ID), and (E) an evidence claim (`E-*`) if observability matters.
* When something needs to be enforceable but is mathematical, prefer predicate blocks rather than deontic language in the L/A blocks, per E.8’s deontics vs admissibility guidance.

#### A.6:4.6 - Classification sanity rules (informative, concept-level)

These are *writing diagnostics*, not tool requirements. They exist to keep the mental model crisp.

- **RFC keyword inside Definition, invariant, or admissibility predicate** → classification error (rephrase as predicate; move obligation to `D-*`).
- **`E-*` without (carrier + measurement conditions + viewpointRef)** → incomplete evidence claim (cannot be adjudicated).
- **`D-*` that re-states an `A-*`/`L-*` predicate instead of referencing its ID** → drift risk (prefer “MUST satisfy `A-…`”).
- **A face introduces new L/A/D/E content not present in underlying Signature and mechanism** → view-fork (make it informative only, or move the deontic result—`U.Commitment` or exact `A.2.8.PER` result—to its direct owner and cite it from the underlying signature or mechanism publication).
- **“The system or service SHALL …” where no accountable role assignment or admitted acting system is named** → likely misclassified deontic (rewrite as `E-*` behavior + `D-*` duty on implementers and operators).

### A.6:5 - Archetypal Grounding (Tell–Show–Show; System / Episteme)

> **Informative.** Worked examples for learning the L/A/D/E claim-classification discipline; they do not add requirements beyond A.6:7.

#### Tell (universal rule)

A boundary description is evolvable iff its claims are separated across the signature stack and each statement is classified by the boundary discipline matrix to its proper layer (Laws, Admissibility, Deontic results—commitments or permission results, Effects and evidence), while preserving EntityOfConcern and Description-episteme / publication-carrier separation.

#### Show #1 (`U.System`): effectful API boundary (algebraic effects intuition)

**System:** A “Payment Authorize” service.

* **Signature layer (A.6.0).**

  * Vocabulary: `PaymentRequest`, `AuthDecision`, `MerchantId`, `Money`, etc.
  * Laws: e.g., “If decision is APPROVED then reservedAmount = requestedAmount” (truth‑conditional).
  * Applicability: bounded context “Payments Authorization”.

* **Mechanism layer (A.6.1).**

  * Admissibility gate: request is admissible iff `tokenValid ∧ merchantActive ∧ amountWithinLimit`.
  * Transport: HTTP headers, idempotency key transport, canonical currency conversions.
  * Audit and observability: specifies required evidence carriers (e.g., `AuthorizationRecord` event, log entry) and their semantics (fields, correlation IDs, retention class).

* **Realization and work layer.**

  * Actual side effects: reservation entry in ledger, emission of event, timers, retries.
  * Evidence: traces, logs, metrics.

* **Publication faces (MVPK).**

  * PlainView: narrative for stakeholders (what the service promise is, in plain terms).
  * TechCard: signature or mechanism details (types, error codes, version policy, admissibility predicate refs).
  * InteropCard: machine‑exchange oriented boundary details (canonical field names, schema refs, transport bindings).
  * AssuranceLane: evidence bindings (which carriers exist, how to adjudicate `E-*` claims, retention and access duties by reference).

**SoTA tie‑in:** This boundary is naturally understood using *algebraic effects and handlers*: the signature is the “operation interface” (effect signature), while the mechanism or realization provides handlers (semantics). The stack keeps the abstract operation signature stable while allowing multiple handlers and realizations to evolve.

**Classification example:**

* “Defined iff tokenValid” belongs in Quadrant A (admissibility gate).
* “Clients MUST include Idempotency‑Key” belongs in Quadrant D (role-assignment or acting-system obligation) but should reference the same gate semantics to avoid divergence.
* “System emits AuthorizationRecord” belongs in Quadrant E (evidence via carriers).

#### Show #2 (`U.Episteme`): published evaluation protocol boundary (multi‑view + evidence)

**Episteme:** A published “Model Evaluation Protocol” for a safety‑critical classifier.

* **Signature layer:** defines operations like `Evaluate(model, dataset) → Report` and truth‑conditional definitions of metrics (AUROC, calibration error) as Laws.

* **Mechanism layer:** admissibility gate encodes when evaluation is permitted: dataset version must match declared license; measurement environment must meet constraints; seeds pinned.

* **Deontics and commitments:** reviewers MUST use dataset vX.Y; authors SHALL publish MVPK faces and cite the measurement environment; an organisation commits to a review SLA (explicitly a role-assignment or acting-system commitment).

* **Effects and evidence:** the produced report file, logs of evaluation runs, cryptographic hashes, and trace IDs are carriers. A.7 discipline prevents calling the report “the evaluation” (object) and prevents treating the file as the model.

* **Multi‑view (MVPK canonical face kinds only):**

  * PlainView for decision makers: what this protocol means for assurance.
  * TechCard for engineers: metric definitions named by value, admissibility predicates, and a clearly marked **Norms-and-commitments** section (D‑claims) for governance.
  * InteropCard for exchange-oriented consumers: conceptual field names, anchors, and schema references (concrete format mapping lives outside Part E).
  * AssuranceLane for auditors: evidence map (which carriers prove what happened) and adjudication steps keyed by `E-*` IDs.

This episteme is a boundary because it mediates between theory (“metric definitions”) and work (“a run produced a report”). The signature stack provides the stable interface for that mediation.

### A.6:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Ontological and Epistemic**, **Prag**, **Did**. Scope: **Universal** for boundary descriptions in A.6.\*.

* **Arch bias:** Biases toward separation of concerns and explicit layering; mitigated by allowing multiple faces (views) so audiences are not forced into the same amount of detail.
* **Ontological and Epistemic bias:** Treats signatures and mechanisms as epistemes that must not be conflated with work; mitigated by explicit evidence carriers and evidence records.
* **Gov bias:** Prefers auditable responsibility (viewpoint accountability and commitment unpacking); mitigated by keeping the stack conceptual and tool‑agnostic.

### A.6:7 - Conformance Checklist

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Purpose                                                             |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **CC‑A.6.1 (Stack declaration).**        | A conforming boundary description **SHALL** identify its stack layers (Signature, Mechanism, realization and work evidence, Publication faces) and state which boundary publication forms or sections belong to which layer.                                                                                                    | Prevents “one doc contains everything” ambiguity.                   |
| **CC‑A.6.2 (Square discipline).**        | A conforming boundary description **SHALL** conform to **A.6.B** (Boundary Norm Square), including atomicity, quadrant classification, and explicit cross‑quadrant references by claim ID.                                                                                                           | Makes the stack operational; prevents claim-kind mixing in contract prose. |
| **CC‑A.6.5 (A.7 separation).**           | A conforming boundary description **SHALL** respect EntityOfConcern and Description-episteme and publication-carrier separation; statements about logs or metrics **SHALL** be written as carrier-referenced evidence claims or policies, not as properties of the text itself. | Prevents category errors and improves auditability.                 |
| **CC‑A.6.6 (Viewpoint accountability).** | Every published MVPK face use **SHALL** identify the selected episteme and exact `viewpointRef`. When the selected episteme is called a `U.View`, E.17.0 conformance **SHALL** obtain independently; the face or publication form supplies no membership. Face content **MUST** cite canonical L/A/D/E claim IDs and direct objects rather than restating normative content and **MUST NOT** introduce semantic commitments or permission results beyond the governed source claims. | Preserves viewpoint discipline without identifying a publication face with an episteme. |
| **CC‑A.6.6a (MVPK face‑kind discipline).**  | A publication that claims MVPK alignment **MUST** conform to **E.17 and publication-face or publication-form discipline** face‑kind closure (i.e., use only `{PlainView, TechCard, InteropCard, AssuranceLane}` and **MUST NOT** mint additional face kinds). Local “cards” may exist only as headings or sections inside those face kinds. | Aligns with MVPK and publication-face or publication-form discipline; prevents new‑face drift.            |
| **CC‑A.6.7 (Contract unpacking).**       | When using “contract”, “guarantee”, or “promise” language, a conforming text **SHOULD** apply the reusable discipline in **A.6.C** to disambiguate promise content (`U.PromiseContent`, not execution), an utterance package, a published description, a speech act, a deontic commitment (`U.Commitment`), an exact permission result (`A.2.8.PER`), work effects, or evidence, and then classify each atomic statement via **A.6.B** (`L-*`, `A-*`, `D-*`, or `E-*`) with explicit claim-ID and direct-object references and no paraphrase drift. F.18 may provide durable names for recovered terms; it does not govern the contract ontology. | Stops agency attribution errors; clarifies responsibility.          |
| **CC‑A.6.8 (Causal/deontic split).**     | A boundary description that mixes causal support with duty, permission, promise, commitment, release, or admissibility language SHALL split the sentence into atomic claims: causal-use support to `C.28`, deontic and boundary-gate claims to `A.6.B`, and contract, promise, permission, and utterance unpacking to `A.6.C`. A `CausalUseSupportVerdict` does not by itself create a duty, commitment, permission result, promise, release gate, or boundary admissibility predicate. | Prevents causal evidence from being recast as boundary authority or a deontic result. |
| **CC-A.6.9 (Authority-wording split).** | A conforming boundary description SHALL split boundary, policy, API, schema, connector, or compliance prose using "approved", "allowed", "authorized", "guaranteed", "certified", "recommended", or equivalent wording into atomic `L-*`, `A-*`, `D-*`, and `E-*` claims before work use or reliance use. Any evidence, assurance, role effect, status effect, gate use, release use, commitment, permission result, speech-act, or work-occurrence use beyond the L/A/D/E-classified wording SHALL cite the exact `governingPatternRef` or `authoritySourceRef` rather than the wording itself. | Prevents boundary wording from becoming authority, evidence, assurance, gate passage, or work by slogan. |

### A.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti‑pattern                   | Symptom                                                         | Why it fails                                                                     | How to avoid / repair                                                                        |
| ------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Gate‑as‑law**                | Preconditions written as “laws” in the signature                | Breaks substitution; violates A.6.0’s separation of signature vs mechanism gates | Move predicates to Mechanism.AdmissibilityConditions; keep signature laws truth‑conditional. |
| **RFC‑keywords in invariants** | “MUST” appears inside `Definition:` blocks                      | Confuses deontics with mathematical admissibility; undermines auditability       | Rewrite as declarative predicate; reference predicate IDs from CC when needed.               |
| **Paraphrase drift**           | Same constraint restated in multiple faces with new wording      | Creates hidden divergence; breaks L/A/D/E claim-classification discipline and evidence accountability | Use `…-*` IDs + Claim Register; faces reference IDs rather than restating text.              |
| **Interface‑as‑promiser**      | “The interface promises…” without identifying an accountable role assignment or admitted acting system | Ontological category error; interface descriptions do not commit | Apply **A.6.C**: recover promise content, speech act or utterance package, explicit `U.Commitment`, accountable subject, and work and evidence adjudication; use F.18 only if the recovered terms need durable names. |
| **Evidence‑free guarantees**   | “Guaranteed latency” without measurement and evidence account       | Effects exist only in work; without carriers it’s non‑testable                   | Bind to carriers (metrics and traces) and specify the evidence carriers and logged records.       |
| **Face called a view by form** | A face, diagram, query result, or publication form is called `U.View` without exact E.17.0 conformance | Appearance or construction history replaces the dependent-kind condition | Recover the exact candidate and viewpoint epistemes, test E.17.0 conformance, and keep optional A.6.3 construction and publication relations separate. |
| **System‑as‑accountable-subject deontics** | “The system or service SHALL …” used where no accountable role assignment or admitted acting system is named | Blurs behavior semantics with enforcement; hides responsibility                   | Rewrite as (`E-*`) behavior and evidence semantics + (`D-*`) duty on implementers and operators.     |
| **One‑doc monoculture**        | Same document mixes laws, gates, duties, and evidence           | Evolvability collapses; updates become all‑or‑nothing                            | Use the stack: separate Signature, Mechanism, Norms, and Evidence faces; classify by matrix.           |
| **Deontic claim laundering or admissibility or gate overread** | "Allowed", "authorized", "approved", "certified", or "guaranteed" used as work permission, reliance permission, evidence, assurance, gate passage, or work occurrence | One word silently carries several claim families and hides missing source support | Split through `L-*`, `A-*`, `D-*`, and `E-*`; use `A.2.8.PER` for the exact permission result, `A.2.8` for commitment, and `A.15`, `A.10`, `B.3`, `A.20`, or `A.21` only when that exact work, reliance, evidence, assurance, constraint, or gate claim is live. |

### A.6:9 - Consequences

| Benefits                                                                                                           | Trade‑offs / Mitigations                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **Evolvable boundaries.** Implementations can change while signatures remain stable.                               | More upfront structure; mitigated by MVPK faces that present only relevant slices per audience. |
| **Reduced category mistakes.** Object, description, and carrier confusion becomes detectable.                            | Requires discipline in writing; mitigated by the “Where statements go” classification examples.        |
| **Auditability and reproducibility.** Effect claims are tied to evidence carriers; commitments are tied to accountable role assignments or admitted acting systems. | Requires evidence carriers and evidence-record formats to be designed; mitigated by making `AssuranceLane` (evidence bindings) a standard face.    |
| **Clearer cross‑disciplinary communication.** Legal and compliance deontics no longer compete with math invariants.    | Teams must align on viewpoint responsibilities; mitigated by explicit viewpointRef in MVPK.     |

### A.6:10 - Rationale

A boundary is simultaneously:

* a **mathematical object** (signature: operations over vocabulary, governed by laws),
* an **engineering boundary signature** (stable intent, evolvable implementations),
* a **governance object** (commitments, responsibilities, deontics), and
* an **operational phenomenon** (effects happen only by doing work and observing traces).

If these are mixed, evolution becomes impossible to reason about: every change becomes “semantic”, and every claim becomes unfalsifiable.

The stack creates a default **direction of dependence**: higher layers constrain lower layers, not vice versa. The matrix creates a default **classification** that is not reliant on word choice alone and therefore survives natural‑language variation (“must”, “guarantee”, “valid”, “allowed”).

### A.6:11 - SoTA-Echoing (post-2015 practice alignment)

> **Informative.** Alignment notes; not normative requirements.

* **Adopt — algebraic effects and handlers / effect systems.** Modern effect systems separate the *signature of operations* from handler semantics (e.g., Koka’s effect typing; mainstream effect handlers in OCaml 5 era). A.6 aligns by keeping boundary-signature content in `U.Signature` and placing execution semantics in `U.Mechanism`/Realizations, preserving substitution and evolvability.

* **Adopt — session and behavioural types for protocol boundaries.** Post‑2015 practice in behavioural typing treats boundaries as typed interaction protocols with progress and safety properties. A.6’s classification matrix makes “protocol laws” (Quadrant L) explicit and separates entry gates (Quadrant A) from role-assignment or acting-system duties (Quadrant D) and runtime evidence (Quadrant E), reducing ambiguity.

* **Adapt — categorical optics, lenses, and bidirectional transformations.** Contemporary lenses supply useful construction expressions with coherence laws. FPF uses that lesson only for explicit A.6.3 construction or C.29 representation: a projection expression, publication face, and `U.View` remain different objects, while any cross-context reuse stays explicit.

* **Adapt — model-based views-as-queries practice.** Query and projection operations can construct candidate epistemes and make omissions inspectable. E.17.0 still tests each candidate independently against one exact viewpoint episteme; generation, selection, or a `viewpointRef` alone supplies no `U.View` membership.

* **Adapt — DDD bounded contexts and microservice contract-language practice.** Modern architecture practice keeps meaning local and makes crossings explicit. A.6’s stack and L/A/D/E claim-classification discipline provide a precise placement scheme for what belongs to the context boundary claim set, what belongs at the entry gate, what belongs to governance duties, and what belongs to observability evidence.

* **Adapt — observability as evidence discipline.** Post‑2015 observability practice treats traces, logs, and metrics as first‑class evidence carriers. A.6 places such claims in Quadrant E and ties them to carriers (A.7), preventing “guarantees without telemetry”.

* **Adapt — Zero Trust, dynamic authorization, and policy-as-code practice.** Current authorization practice separates policy, API, or schema text from a decision over subject, requested policy operation or work class, affected resource or work target, context, policy or gate version, decision source, and evidence. Cedar-style policy language and Zanzibar-style relation authorization are useful practice references for this split: the wording is not the decision. A.6 keeps policy, API, or schema wording in classified `L-*`, `A-*`, `D-*`, and `E-*` claims and returns work use or reliance use to `A.15` rather than letting "allowed" or "authorized" wording decide by itself.
* **Adopt, adapt, and reject stance for authority-looking boundary wording.** A.6 adopts policy-as-code separation of policy text from evaluated decision, adapts credential, register-backed status, provenance, and attestation practice as source, evidence, and currentness support rather than as the `L/A/D/E` split itself, and rejects visible wording, schema cues, credential displays, register excerpts, or provenance labels as permission, gate passage, work occurrence, evidence, or assurance by themselves.

* **Adapt — Markov blankets and active inference as probabilistic boundary views only after restoration.** Markov-blanket thinking can help pick observables and diagnose boundary-condition failures, but the source phrase must be restored before it carries an A.6 boundary claim. It may name accepted local Markov dynamics, a mathematical or probabilistic lens, a holon delimitation or crossing relation, an interface, an interface module, a physical component, a boundary description, or an agency-threshold claim. A.6 uses the phrase only after the boundary claim set is recovered; it does not replace deontics, invariants, admissibility gates, or the direct owner of the physical or mathematical claim.

### A.6:12 - Relations

* **Implements authoring discipline:** Follows canonical section order and style expectations from E.8.
* **Constrains signature writing:** Reinforces A.6.0 separation of Laws vs operational gates (AdmissibilityConditions live in mechanisms).
* **Constrains mechanism writing:** Aligns with A.6.1 structure (Signature block plus mechanism‑only blocks such as AdmissibilityConditions, Transport, Audit).
* **Requires EntityOfConcern and Description-episteme / publication-carrier discipline:** Uses A.7 to prevent category mistakes; ties evidence to evidence carriers and publication faces to descriptions.
* **Coordinates `U.View`, `U.Viewpoint`, and publication use:** E.17.0 governs viewpoint and view membership; MVPK selects exact epistemes, viewpoints, face uses, and publication forms; A.6.3 governs only optional source-to-receiving construction.
* **Unpacks “contract” talk:** Uses A.6.C, A.2.3, A.2.8, A.2.8.PER, and A.2.9 to keep promise content, utterance or speech act, accountable commitment, positive permission result, and work and evidence adjudication explicit.
* **Connects to signature engineering patterns:** A.6.5 (slot discipline) and A.6.6 (anchor and base discipline) can be read as “constructor and enabling” operations that help *build* well‑formed signatures by disciplined unpacking and grounding (they belong in the same stack discipline because they govern boundary construction).
* **Coordinates with `C.28 CausalUse-CAL`:** When boundary prose uses causal-use evidence or a causal-use verdict to justify deployment, release, duty, commitment, or admissibility, A.6 splits the boundary sentence while `C.28` carries the causal-use question, `CausalityLadderRung`, estimand, support basis, support verdict, and supported causal use and unsupported causal use.
* **Coordinates with `A.15`, `A.10`, `B.3`, `A.21`, `A.20`, and `A.15.1`:** When classified boundary wording is then used for work, reliance, evidence, currentness, provenance, assurance, gate decision, constraint-validity witness, release work occurrence, or deployment work occurrence, the required claim or effect is carried by the governing source named by value: `A.21` for `OperationalGate(profile)`, `GateDecision`, and `DecisionLogRef`; `A.20` for `ConstraintValidity` status or witness; `A.15.1` for dated `U.Work` occurrence.

### A.6:12a - Quantum-like boundary-claim classification note

Use A.6 first for ordinary boundary, interface, API, protocol, contract, connector, publication-face, and observability-evidence wording. Quantum-like boundary prose is supported only after the boundary text still needs a probe, order, frame, export, or state-reading distinction that ordinary boundary patterns would otherwise erase.

Action classification:

1. Identify the boundary sentence and name the boundary object in ordinary A.6 terms.
2. Name endpoints, channel, and carrier separately; do not let one word such as "interface", "service", "contract", or "context" stand for all of them.
3. Apply the applicable ordinary FPF patterns to the ordinary boundary content: A.6, A.6.B, F.9, A.15, C.16, or C.25.
4. If the boundary text uses a coarsened representation to claim preserved action, intervention, manipulation, explanation, or preserved structure across representation scales, state the causal-abstraction or approximate-causal-abstraction mapping before retaining QL wording.
5. Ask whether the boundary act is being used as a passive read or unjustified lossless-transfer reading while actually changing the represented state, export validity, or viability decision.
6. If yes, apply `C.26.1` only to that remaining residual question; keep the ordinary boundary pattern active.
7. If no, keep the text in the ordinary boundary, bridge, work, measurement, or quality pattern and remove QL wording.

Minimum boundary discipline before a quantum-like boundary reading:

| Field | What the author names |
| --- | --- |
| Boundary | Which interface, protocol, context crossing, publication face, service situation, or evidence boundary is being described |
| Endpoints | Which systems, epistemes, roles, carriers, contexts, or faces stand on each side |
| Channel or interaction | Message, meeting, metric, dashboard, API read, bridge or export, split or merge, orchestration, or other boundary act |
| Claimed state reading | What represented state is claimed before and after the act, and whether the act is treated as passive read, action, export, or probe |
| Evidence / carrier | Which carrier, trace, metric, report, observation, or work result supports the reading |
| Export or loss | What is copied, transformed, no longer comparable, or not faithfully exportable |
| Ordinary pattern tried | Which of A.6, F.9, A.15, C.16, or C.25 already carries the baseline question |

Useful outputs:

- an L/A/D/E-classified boundary claim set when ordinary A.6 is enough;
- a Bridge Card when the issue is export loss across contexts;
- a C.26.1 probe-coupled boundary note only when the boundary act changes the represented state in a decision-relevant way;
- a relation repair using `A.6.P` when coupling words become reusable relation candidates, plus `F.18` only when the recovered relation term itself needs durable naming.

### A.6:End

