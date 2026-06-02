## A.10 - Evidence Graph Referring (C‑4)

*“A claim without a chain is only an opinion.”*

### A.10:1 - Context

FPF is a holonic framework: wholes are built from parts (A.1, A.14), and reasoning travels across scales via Γ‑flavours (B.1). To keep this reasoning honest and reproducible, every **published assertion** must be *anchored* in concrete **symbol carriers** and **well‑typed transformations** performed by an **external TransformerRole** (A.12, A.15). **Publication** itself is the typed projection **I→D→S** (`Publ_ID`, `Formalize_DS`) per A.7 and is **not execution**; any physical/digital release, rendering, or upload is **Work** by an external transformer **on carriers**, cited in SCR.

Practitioner shorthand:
> **Claim → (Proof or Test) → Confidence badge**
> …where the proof/test is traceable to real carriers and to an external system/Transformer who executed an agreed method.

This pattern defines the **Evidence Graph Referring Standard** common to all Γ‑flavours (Γ\_sys — formerly Γ\_core, Γ\_epist, Γ\_method, Γ\_time, Γ\_work) and clarifies:
(a) the difference between **mereology** (part‑whole; builds holarchies) and **provenance** (why a claim is admissible; does *not* build holarchies);
(b) the run‑time / design‑time separation (A.4) across **Role–Method–Work** (A.15).

Use this when a model, report, metric, confidence badge, review note, or QL reading is starting to act like evidence but the carrier, transformer, method, time stance, or provenance edge is still implicit. The action is to turn the assertion into a small because-graph: name the claim, name the carriers, name the external transformer role, name the method or work trace, state the time/coverage condition, and attach the resulting evidence edge to the claim rather than to the holon itself.

Useful output: a claim that can answer "because of which carriers, by which transformer, using which method, and when?" without making provenance pretend to be part-whole structure.

### A.10:2 - Problem

Without a uniform anchor, models drift into five failure modes:

1. **Weightless claims.** Metrics or arguments appear in the model with no link to their **symbol carriers** (files, datasets, lab notebooks, figures).
2. **Collapsed scopes.** Design‑time method specs are silently mixed with run‑time traces; results cannot be reproduced because “what was planned” and “what actually ran” are conflated.
3. **Self‑justifying loops.** A holon attempts to evidence itself (violates A.12 externality), producing cyclic provenance and unverifiable conclusions.
4. **Source loss during aggregation.** As Γ combines parts, some sources “fall out”; later audit cannot reconstruct why a compound claim was accepted.
5. **Temporal ambiguity.** Time‑series are aggregated without interval coverage or dating source; gaps/overlaps invalidate comparisons and trend claims.

The business effect is predictable: confidence badges cannot be defended, cross‑scale consistency (A.9) is broken, and iteration slows because every review re‑litigates “where did this come from?”.

### A.10:3 - Forces

| Force                           | Tension                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs. support cost** | One Standard must fit systems and epistemes ↔ Evidence producers and maintainers need proportionate support records.                                                           |
| **Externality vs. reflexivity** | Evidence must be produced by an external TransformerRole (A.12) ↔ Some systems adapt themselves (need reflexive modelling without self‑evidence). |
| **Atemporal vs. temporal**      | Many claims are state‑like ↔ Many others are histories; evidence must respect order and coverage (Γ\_time).                                       |
| **Rigor vs. flow**              | Formal proofs and controlled tests raise confidence ↔ Engineering cadence needs lightweight, incremental anchors.                                 |
| **Mereology vs. provenance**    | Part‑whole edges build holarchies ↔ Evidence edges never do; the two graphs must interlock without leaking semantics.                             |

### A.10:4 - Solution — The Evidence Graph Referring Standard

The Standard is a small set of primitives applied uniformly, with **practitioner-first clarity** and **formal hooks** for proof obligations. Its governed object is the evidence/provenance path for a claim: carriers, external transformer roles, method traces, work traces, time stance, and evidence edges. Authority-looking reliance and causal-use support are specialized uses of that same evidence path; they do not redefine `A.10` as a pattern about labels, dashboard wording, or source rhetoric.

#### A.10:4.1 - EPV‑DAG (Evidence–Provenance DAG).
A **typed, acyclic** graph disjoint from mereology. Node types: **SymbolCarrier** (a `s.System` in **CarrierRole**, A.15), **TransformerRole** (external Transformer, A.12), **MethodDescription** (design-time blueprint of a method, A.15), **Observation** (a dated assertion or result record), **s.Episteme** (knowledge holon). Edge vocabulary is small and normative: `evidences`, `derivedFrom`, `measuredBy`, `interpretedBy`, `usedCarrier`, `happenedBefore` (temporal), etc.
*Practitioner view:* it is the *“because‑graph”*: every claim answers “because of these carriers, by this Transformer, using that method, then.”

#### A.10:4.2 - Anchors (two relations, two flavours).**

* `verifiedBy` — links a claim to **formal** evidence (proof obligations, static guarantees, model‑checking records).
* `validatedBy` — links a claim to **empirical** evidence (tests, measurements, trials, observations).
  Both anchors terminate in the EPV‑DAG, not in the mereology graph.

#### A.10:4.3 SCR / RSCR (Symbol Carrier Registers).
Every `Γ_epist` aggregation **SHALL** emit an **SCR**: an exhaustive register of **symbol carriers** substantively used in the aggregate, with id, type, version/date, checksum, source/conditions and optional `PortionOf` (A.14) for sub‑carriers.
Every `Γ_epist^compile` **SHALL** emit an **RSCR**: SCR specialised to a **bounded context** (vocabularies, units) with publication‑grade identifiers and hashes.
*Why this matters:* it prevents “lost sources” during composition and underwrites reproducibility without mandating any specific tool.

#### A.10:4.4 Scope alignment (A.4) across Role–Method–Work (A.15).

* **Design‑time**: **MethodDescription** lives here; methods are blueprints; anchors reference what *would* constitute proof or test.
* **Run‑time**: **Work** (actual execution) lives here; traces reference which MethodDescription they instantiate and record `happenedBefore`.
  Bridging edges are explicit (“this run trace instantiates that spec”), so scopes never silently mix.

#### A.10:4.5 External TransformerRole (A.12).
The system that produces or interprets evidence is **external** to the holon under evaluation. If true reflexivity is essential, model a **meta‑holon** (A.12): the self‑updating holon becomes the *object* of a meta-holon external transformer (the “mirror”), restoring objectivity.

#### A.10:4.6 Γ‑flavour hooks (how each flavour anchors).

* **Γ\_sys (formerly Γ\_core)**: physical properties are anchored by measurement models, boundary conditions, calibration carriers, and dated observations.
* **Γ\_epist**: always outputs SCR/RSCR; every provenance/evidence node resolves to an SCR/RSCR entry.
* **Γ\_method**: order‑sensitive composition; at design‑time a **Method Instantiation Card (MIC)** states `Precedes/Choice/Join` and guards; at run‑time traces record `happenedBefore` and point to the MethodDescription they instantiate.
* **Γ\_time**: temporal claims state interval coverage; **Monotone Coverage** (no unexplained gaps/overlaps) is required.
* **Γ\_work**: resource spending and yield are evidenced by instrumented carriers (meters, logs) and their MethodDescriptions; keep **resource rosters** separate from SCR/RSCR.

> **Practitioner shortcut:** If you can answer *what carriers, which system, which method, when*, the anchor is likely sufficient; if any of the four is missing, it is not.

#### A.10:4.6a - Authority-reliance use of ordinary A.10 evidence paths

Use this subsection when an authority-looking case is being used as evidence for reliance. The evidence path is claim-bound: it supports a named claim or effect for a named work move or reliance move, not "authority" in general. This subsection does not change the governed object of `A.10`; it applies the same evidence and provenance path to source-sensitive cases where displays, credentials, copied text, generated text, dashboards, provenance labels, or attestations are being overread. If the live work occurrence, gate decision, speech act, commitment, or evidence path is already clear, recover and cite that exact FPF source directly instead of analyzing nearby wording first.

A10-lite is enough for source-finding, orientation, learning, and bounded reversible probes:

| Field | Required content |
| --- | --- |
| claim or effect | The claim, effect, or source-backed posture the carrier is being asked to support for the named work move or reliance move. |
| carrier | The display, badge, credential, attestation, dashboard tile, copied text, generated text, log, trace, source file, report, or other external carrier. |
| producer, issuer, verifier, or source-maintenance role assignment | The role assignment or system that issued, performed, attested, measured, copied, generated, verified, or displayed the carrier or source-backed content. |
| method execution or work event | The work act, measurement, verification, review, build, attestation, copy, extraction, generation, dashboard query, API read, trace, log, or method instance that produced the carrier. |
| time window | Issue time, validity window, decay, supersession, revocation, policy or gate version, and reopen condition. |

Minimum path for routine reliance:

| Field | Required content |
| --- | --- |
| Supported claim or effect | Approval, permission, gate passage, role or status currentness, work occurrence, evidence support, assurance input, or other exact claim or effect being attempted. |
| Carrier | The visible or recovered carrier, with enough identity to reopen it. |
| Issuer, performer, trust anchor, status register, or source-maintenance role assignment | The role assignment, system, or governing register accountable for producing, updating, or verifying the carrier or source-backed content in this context. |
| Affected entity and relying context | The release, service, model, person, role holder, policy subject, work item, claim, audience, tenant, environment, or other entity for which reliance is attempted. |
| Time window and freshness | Issue time, validity window, decay, supersession, revocation, policy or gate version, and reopen condition. |
| Evidence-producing work event or method trace | The production, verification, query, generation, execution, or review work that made the carrier. |
| Evidence relation and rival explanation | Which claim the carrier supports, how it supports it, and the principal live rival explanation such as stale display, spoofed badge, copied wording, generated paraphrase, context shift, carrier-only provenance, or local-only transform support. |

Expanded fields are collected only insofar as they decide the live reliance question. Evidence depth follows consequence severity, reuse, contestability, cross-context movement, and the support required for the attempted claim. Do not expand a source-finding note into a full evidence dossier, and do not collect every expanded field merely because a carrier is copied, generated, credential-like, provenance-like, or cross-context.

**Adversarial misuse guard.** Do not let carrier authenticity, provenance, copied approval, generated summary, stale screenshot, credential status view, or dashboard export convert into claim truth or currentness. Treat each as a rival explanation to test against issuer or source-maintenance role assignment, method trace or work trace, time window, and relying context.

**Data-minimization and privacy posture.** Preserve minimum sufficient support for the intended reliance use. Use redacted, hashed, scoped, or role-mediated carrier refs when raw evidence would expose personal identity, access tokens, cryptographic proof payloads, tenant identifiers, security logs, incident details, internal release metadata, audit trails, privileged reviewer names, or sensitive model/data provenance. Redaction does not create source support; it must preserve enough recoverability for the relying context.

| Expanded field | When it is live |
| --- | --- |
| Method trace or work trace | Provenance, attestation, generated source support, copied source support, dashboard support, rollback support, or work occurrence is being used. |
| Carrier integrity | The carrier may be spoofed, stale, copied, transformed, rendered, redacted, or context-shifted. |
| Identity or holder binding | The claim depends on a credential holder, role holder, issuer, performer, delegate, revoker, verifier, or relying party. |
| Verifier context, relying-party context, and acceptance rule | The support is valid only for a verifier, audience, tenant, environment, release line, policy subject, operational mode, or consumer-side policy or gate rule that accepts the evidence for this use. |
| Proof, cryptographic-signature, or status verification result | Credential, provenance, attestation, authenticity, revocation, or currentness support is claimed. |
| Policy/gate version and decision source | Permission, admissibility, gate passage, release, rollback authority, or policy authorization is attempted. |
| Source-chain transform notes | Support passed through extraction, copy, rewrite, representation shift, explanation rendering, summary, export, redaction, or another transform step before reliance. |
| Source order and supersession rule | Multiple source candidates disagree or freshness or priority may defeat the visible publication face, carrier, rendering, or cue. Include the governing register or status-source order when a register entry is the source of role assignment, status assertion, permission, duty, or gate state. |
| Minimum disclosure posture | Raw evidence would expose secrets, personal data, tenant identifiers, privileged logs, tokens, security-sensitive traces, or unnecessary identities. |

Case repairs:

| Case | Evidence repair |
| --- | --- |
| Stale credential badge or status display | Show issuer or trust anchor, governing status register when one exists, holder or subject binding, verifier and relying-party context, proof result or status result, revocation and freshness, validity window, status-source entry version, and carrier integrity. Display presence is not current role assignment, status assertion, or permission. |
| Verifiable credential, credential view, or register excerpt | Treat as an A.10 carrier with issuer or trust anchor, governing status register when one exists, register entry or source-record id and version, holder or subject binding, verifier, proof result, status result, currentness, relying context, validity window, revocation window, and acceptance rule. When those checks pass, it may support credential-currentness for that holder and relying context. It supports permission, authorization, role assignment, status assertion, or gate passage only when the register entry or another exact source such as `A.2.8`, `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` creates or states that effect for the bounded context. |

| Copied approval or review summary | Show the original `A.2.9` `SpeechActRef` / issuing act when approval or authorization is claimed, or the original reviewed source when only review-content currentness is claimed. Add copy relation, currentness, scope/window, evidence-producing work/event, and whether separate commitment/work support is live. Copy evidence is not approval by itself. |
| Provenance, authenticity, or attestation label | Show the bounded origin, history, build, or process claim; source episteme, source episteme publication, or source carrier; method trace or work trace; source-specific proof; carrier integrity; verifier or relying policy that accepts it for this claim or effect; and rival explanation. Provenance does not show truth, safety, approval, release, gate passage, permission, or assurance unless another exact source carries that additional claim or effect. |
| Dashboard status tile | For gate-passage or release reliance, show dashboard query/source/time/window/currentness, source order, freshness policy, rival explanation, and the current `A.21` `GateDecision` / `DecisionLogRef` with gate profile/version and release/work target; the A.10 path evidences that source chain. A status display is not gate passage or work occurrence by itself. |

| Rollback command-like cue | Show command/authorization source, actor, affected work target or claim target, scope/window, and whether the cue is only an `A.6.A` action invitation. A command cue is not execution evidence. |
| Rollback execution result | Show `A.15.1` `U.Work` occurrence, method trace or work trace, logs, outcome evidence, and time window. Execution evidence is not approval, assurance, or gate passage by itself. |
| Generated explanation | Use `E.17.EFP` to classify the explanation relation and source-finding posture. For reliance, show claim-bound attribution alignment: every operative claim relied on maps to a source passage, carrier, or exact `governingPatternRef` or `authoritySourceRef` that supports that claim in the relying context. When that mapping is complete, A.10 may support those operative claims as source-backed evidence; the explanation itself still does not issue, approve, authorize, pass a gate, evidence execution, or raise assurance. |

| Model card or datasheet used as evidence | Show documented admissible-use statement or external intended-use field, version/window, evaluation condition, limitations, evidence carriers, and whether a `B.3` assurance claim is live. Documentation does not become readiness or assurance by presence. |
| Extracted-source chain to gate or release claim | Name the source reference, the first lossy or non-commutative transform step, the FPF relation or pattern governing that transform (`A.6.3.CR`, `A.6.3.RT`, `A.6.3.CSC`, `E.17.EFP`, `E.17.ID.CR`, or `E.18` where applicable), the admissible inference move after the step, the exact `governingPatternRef` or `authoritySourceRef` that carries the live claim, the source reopen trigger, and the gate claim or release claim blocked until those supports are recoverable. |
| Conflicting sources | When display, source carrier, decision log, recency signal, freshness signal, copied summary, generated summary, credential status, provenance label, or assurance evidence disagree, name the visible source, rival source, source order, decision source, freshness policy, and supersession rule. Do not choose by color, visual salience, confidence wording, copied wording, or apparent recency; the work claim or reliance claim is contested until the source-order question is resolved. |

| Sensitive evidence path | Use redacted, hashed, scoped, or role-mediated carrier refs when raw carriers expose secrets, personal data, security-sensitive traces/data, privileged logs, tenant identifiers, or unnecessary identities. Redaction does not create source support; it must preserve enough recoverability for the relying context. |
| Pointer or proof-status evidence path | Use a hash, proof verification result, status verification result, source ref, scoped pointer, disclosure receipt, or role-mediated view instead of copying raw sensitive carriers or payloads when that pointer preserves enough recoverability for the relied-on claim or effect. Do not copy raw secrets, tokens, privileged logs, personal identities, or tenant details merely to make the evidence path look fuller. |

If the path is incomplete, A.10 returns evidence-path posture and source-currentness posture, not work or reliance support for the attempted claim or effect. Valid dispositions include source-finding only, reopen original carrier, request issuer or status verification, refresh dashboard query or API query, mark stale or contested, narrow the live P2W class or reliance claim, proceed only with a reversible local probe under an explicit work plan when work is live, or block the unsupported work claim or reliance claim.

**Broken-source repair assignment.** If the relying actor cannot recover or verify the source path, assign the repair to the accountable project-side responsibility assignment: issuer or performer, verifier or status service, evidence-producing work role assignment or system, gate-decision source, role or status source, or boundary source. The A.10 result should name the missing source and blocked use rather than making the relying actor reconstruct a source they cannot issue or verify.

Role prompts for evidence or currentness use:

| Role in the situation | Prompt |
| --- | --- |
| Relying actor | Which exact claim or effect needs support, and what is the minimum carrier, source, time, and relation path for that claim or effect? |
| Issuer, verifier, or status source | Which issuer, holder, verifier, proof result, status result, currentness, revocation, or acceptance-rule source must be exposed or repaired? |
| Auditor or reviewer | Which carrier, source-maintenance role assignment, method trace or work trace, time window, evidence relation, and rival explanation must be recoverable? |
| Security source or compliance source | Which source order, supersession, proof result, status result, revocation, and minimum-disclosure posture decide this reliance question? |
| LLM/tool user | Which generated or copied operative claims map to source passages or carriers, and which claims remain only source-finding? |
| Model source or data source | Which intended-use, evaluation-condition, version, window, limitation, and evidence carriers bound the model documentation or data documentation? |

**Repeated missing-source indicator.** If the same visible-item family repeatedly returns stale, contested, no-source, or no-currentness A.10 results, record a source-system repair item: instrument the source, expose decision-source refs, add currentness checks and status checks, preserve claim-bound source links for generated or copied outputs, require credential views to show status windows and currentness windows, require model documentation and data documentation to expose intended-use and evaluation-condition fields, or require provenance labels and attestation labels to name their bounded claim type. Repetition is an indicator that the source path or display needs repair; it is not a reason to make each acting user rebuild the path manually.

Display guidance for evidence and currentness: an evidence or status display should show the claim or effect, carrier, source-maintenance role assignment, exact ref or link, time window, freshness, relying context, and unsupported action, claim, or effect. A display that can only show source availability should say so; it must not imply approval, permission, gate passage, work occurrence, or assurance.

Incident-learning fields for evidence and currentness overread: visible carrier or publication face, intended claim or effect, missing source-path field, exact carrier, source-maintenance role assignment, method trace, work trace, and time relation needed, rival explanation that made the overread plausible, current safe disposition, and upstream repair item for instrumentation, source refs, status, currentness, claim-bound source links, credential view, model documentation, data documentation, or provenance and attestation label.

Contestability and redress path: when an evidence path or currentness path affects person or team status, access, responsibility, a compliance relation, or a release decision, the A.10 result should name the disputed claim, carrier, source-maintenance role assignment, verifier or status source, freshness or revocation source, privacy-minimized evidence ref, safe interim disposition, and review or redress path. A disputed display remains contested until the source-order or currentness question is resolved.

**Positive repaired path.** When the source path is complete, return the smallest source-backed support statement: named claim or effect, carrier and source-maintenance role assignment, method trace or work trace, time window, currentness, evidence relation, and the exact action or reliance it supports. The downstream use is admissible only inside that scope, without treating evidence support as approval, permission, gate passage, work occurrence, or assurance.

What this does not authorize: `A.10` does not approve, authorize action, pass a gate, release, create permission, create a commitment, assign a role, record a work occurrence, or raise assurance. It supplies the evidence path and support posture that `A.15`, `A.6`, `B.3`, `A.21` gate-decision sources, `A.20` constraint-validity sources, `A.2.9` speech-act sources, `A.2.8` commitment sources, `A.15.1` work-occurrence sources, or another exact `governingPatternRef` or `authoritySourceRef` may consume.

#### A.10:4.6b - Local evidence-use classifier and `RelianceDisposition` for support-looking sources

Use this subsection when a visible source is being treated as evidence for a claim, act, work move, gate, release, review claim, assurance use, or problem-side P2W use. The first A.10 move is to recover the evidence kind and the bounded use it can actually support. Broad source words such as `source`, `metric`, `confidence`, `conformant`, `safe`, `ready`, `certified`, `approval`, or `permission` are only recovery prompts; they do not name the evidence relation by themselves.

This subsection uses a local reliance-use classifier, not a Core evidence-kind ontology. Its practical gain is a smaller next move: recover the evidence relation, name the supported and unsupported use, then stop or exit to the exact receiving pattern. It is not a required project review step and does not ask the practitioner to inspect every source-looking item.

Support role: the first table is an A.10 recognition aid, the `RelianceDisposition` table is a minimum local record aid, and the worked source-overread slices are regression/review slices. They are not project checklists, a required sequence, a new evidence ontology, or a general source classifier. Use only the row that answers the live attempted evidence use, then stop when the bounded evidence relation, supported use, unsupported use, and reopen condition are clear. This local section returns the attempted use to A.10 evidence relation; it does not create an extra SEMIO authority or cross-pattern relation vocabulary.

Affordability card: orientation or source-finding remains a cue and stops here; bounded reliance states one supported use, unsupported use, window, and reopen condition; threshold reliance exits to the minimum receiving pattern only when the B.3 material-reliance threshold is live: behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people/team status, operational action, or controlled-object regulation would materially change. Plain wording remains ordinary unless it changes admissible use, support, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

Cheap stop: if a bounded claim, current carrier, evidence path, window, supported use, unsupported use, and reopen trigger are present, and no assurance, gate, work, control-bearing relation, release relation, or B.3 material-reliance threshold is live, stay in `A.10`. Do not open `B.3`, `A.21`, `B.2.5`, or a broad evidence pack merely because the source looks official, quantitative, generated, credentialed, or safety-related.

Common wrong first reading: a visible source is approval, permission, safety, or readiness. First honest entry: recover the A.10 evidence path for one bounded claim or use; approval, permission, safety, readiness, gate passage, and work authority stay with their receiving patterns when live.

Plain move palette: `RelianceDisposition=pass` means proceed only inside the bounded use; `RelianceDisposition=degrade` means use only a narrower or reversible version; `RelianceDisposition=abstain` means do not decide yet; `RelianceDisposition=reopen` means changed or contested support defeated the previous reading; `RelianceDisposition=evidence-needed` means ask for the named missing evidence at the named decision point; `RelianceDisposition=safety-case-required` means return to `B.3` because the B.3 material-reliance threshold is live; `RelianceDisposition=no-supported-current-use` means block the current attempted use until a receiving source changes.

| Support-looking source or attempted use | First A.10 move | Escalation trigger | Forbidden overread |
| --- | --- | --- | --- |
| Ordinary source-backed report, record, citation, observation, model card, datasheet, data card, or publication excerpt | Name the claim, carrier, producer or method trace, evidence path, currentness window, supported use, unsupported use, and reopen trigger. | Open `B.3` only when assurance is live or the B.3 material-reliance threshold is live; open `A.21` for active gate decision, `A.15` or `A.15.1` for work, or another exact neighbor only when that relation is live; open `B.2.5` only when a controlled object is regulated through a feedback channel, evidence channel, cadence, window, or supervisory/control relation. | Evidence presence as approval, gate passage, assurance, release permission, work authority, control authority, or safety acceptance. |
| Confidence, calibration, prediction interval, abstention reason, or selective-action cue | Support only the named act, context, window, calibration population or exchangeability/shift basis, applicability condition, and stop condition. Use `RelianceDisposition=pass` or `RelianceDisposition=degrade` only for that bounded use, and state the unsupported attempted use beside it. | Open `C.27` or `G.11` when timing, expiry, refresh, distribution shift, monitoring, or applicability change alters the admissible act; open `B.3` when assurance is live or the B.3 material-reliance threshold is live. | Confidence as global permission, trust, readiness, safety, release support, or engineering justification. |
| Generated explanation, generated summary, or didactic reconstruction | Keep the rendering in `E.17.EFP` as explanation or source-finding unless each relied-on operative claim has an A.10 evidence path or another exact receiving source. | Open `A.10`, `B.3`, `A.21`, `A.15`, or another exact source only for the operative claim being relied on. | Explanation wording as evidence, assurance, approval, gate passage, work occurrence, or permission. |
| Conformance label, `CV.Status`, benchmark result, score, semantic-fidelity marker, or CV-looking publication near release | Recover the declared relation: measurement or marker support, `A.20` step-local CV status, `A.21` gate check, `E.19` pattern-quality result, `C.16` characterization, or exact external-rule locus. | Open `A.21` only when an active `OperationalGate(profile)` consumes effective gate-check refs and emits a `GateDecision`; open `B.3` only when assurance is live. | Conformance or score as value, adequacy, release confidence, work occurrence, safety, trust, or gate passage outside the declared relation. |
| Provenance, authenticity, C2PA-like credential, SLSA-like attestation, build record, or status-register display | State the bounded origin, history, build method or production trace, holder, status, verifier rule, relying context, and currentness claim it supports. | Open the source that carries truth, permission, safety, release, gate passage, work occurrence, or assurance only when that exact relation is live. | Provenance, authenticity, or status-currentness as truth, safety, approval, permission, release, gate passage, or assurance. |
| Contest, redress request, challenge, appeal, or conflicting source | Name the contested claim, carrier, source order, freshness/currentness issue, affected use, accountable review role, allowed challenge evidence, possible disposition change, outcome record, and reopen trigger. | Open neighboring role, status, commitment, gate, control, assurance, work, or representation loci when their effects are live. | Appeal-channel presence as claim truth, safety, compliance proof, social-effect acceptance, or completed redress. |

For A.10 use, `RelianceDisposition` is a local disposition over the evidence path and the bounded reliance use. Outside a table column already headed `RelianceDisposition`, write the qualified form `RelianceDisposition=...` and bind it to the named attempted use, currentness/window when live, supported use, unsupported use, and reopen or stop condition; it is not `CV.Status`, `GateDecision`, selector result, or `ProblemCard@Context` state.

Observed-effect or consequence evidence may be used only for what happened or is credibly recorded. If the attempted use says the source caused, prevented, would have changed, or is responsible for that effect, leave ordinary A.10 reliance and open `C.28` plus any live evidence, work, or assurance relation.

If a proxy marker, benchmark, confidence value, dashboard metric, or score becomes the primary driver for action, release, resource allocation, people/team status, or P2W priority, check whether the live claim also raises an `E.13` proxy-to-objective question. Do not open `E.13` for every metric; open it only when the proxy is being used as the target or decision driver.

If publication or observation of a cue changes the situation or source condition being read, recover the probe-coupled boundary before treating the cue as passive evidence. This sentence does not import quantum-like vocabulary; it only prevents passive-evidence overread for dashboards, warnings, labels, and public status displays.

| `RelianceDisposition` | A.10 reading | Minimum A.10 statement |
| --- | --- | --- |
| `RelianceDisposition=pass` | The exact evidence relation is live, the evidence kind is present, the source is current enough for the named use, and the supported use is bounded. | State the supported claim, act, work move, review claim, or P2W receiving use, the unsupported attempted use, the carrier path, and the window. |
| `RelianceDisposition=degrade` | The source supports only a narrower claim, smaller audience, reversible local act, lower assurance input, or shorter window. | State the narrowed admissible use, the attempted use still not supported, and the stop condition. |
| `RelianceDisposition=abstain` | Evidence is insufficient, stale, out-of-context, uncalibrated, conflicted, or not tied to the live relation, while immediate rejection is not justified. | State the claim not decided and the missing evidence or relation needed before use. |
| `RelianceDisposition=reopen` | A contest, changed representation, changed described entity, stale source, expired window, changed profile, conflicting source, retargeting, or new evidence defeats the previous evidence path. | State the source or relation to reopen and the previous use that is no longer supported. |
| `RelianceDisposition=evidence-needed` | The visible source may matter, but the required evidence kind or source-currentness path is absent. | State the missing evidence kind, receiving pattern, and decision point so delay does not become indefinite. |
| `RelianceDisposition=safety-case-required` | The B.3 material-reliance threshold is live: reliance on the visible source may materially change behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people/team status, operational action, or controlled-object regulation. | State the threshold trigger and return to `B.3` for the minimum reliance safety support record, with A.10 evidence paths for the source claims. |
| `RelianceDisposition=no-supported-current-use` | No current evidence path supports the attempted act, work, claim, gate, release, assurance, review, control-bearing feedback, or P2W use. | State the blocked use and the neighboring pattern or project record required before a new attempt. |

Minimum real contest/redress: a contest path exists only when the affected party or accountable reviewer can identify the disputed claim or source, affected use or harm, accountable review role, evidence or argument allowed in challenge, possible disposition change, outcome record, and reopen trigger. A feedback channel, complaint form, or appeal label without those recoverable items is not enough to change the disposition.

Affected-party contestable minimum: even when raw evidence stays reviewer-only, the contesting party must be able to see enough of the claim, source class, disposition, affected use, accountable role, and allowed challenge evidence to challenge the result. Privacy, security, or privilege can narrow disclosure; they cannot erase the challengeable minimum while still claiming contest or redress.

False-negative reliance guard: a blocked, abstained, or evidence-needed use is not final if admissible challenge evidence, missing affected-party evidence, changed source, changed representation, or redress can materially change the disposition. If refusal is based on missing evidence, name the missing evidence kind and decision point rather than closing the dispute by vagueness.

Sensitive evidence boundary: use scoped, hashed, redacted, or role-mediated evidence refs when raw carriers would expose personal data, secrets, tokens, privileged logs, tenant identifiers, incident details, security-sensitive traces, or unnecessary identities. A redacted path must still preserve enough recoverability for the relied-on claim, disposition, and contest path.

Worked source-overread slices:

| Slice | A.10 usable reading | Non-admissible lift |
| --- | --- | --- |
| Software supply-chain attestation is cited near a release conversation. | The attestation may support bounded origin, build method or production trace, verifier-rule, holder, and currentness claims. | Runtime safety, release approval, gate passage, or assurance unless `B.3`, `A.21`, or another exact receiving relation is live. |
| A valid provenance credential, watermark, or authenticity mark appears on a publication face. | The mark may support where the carrier, signature, assertion, or manifest came from under the verifier regime. | Truth of the represented world-state, safety, permission, or adequacy by provenance alone. |
| A confidence interval or calibration result is used for one reversible act. | State the act, context, calibration basis, window, supported use, unsupported use, and stop condition. | Global readiness, trust, safety, release support, or engineering justification. |
| A generated explanation or summary says a result is reliable. | Treat the rendering as source-finding or explanation until the operative claim has an `A.10` evidence path or another exact receiving source. | Evidence, approval, gate passage, work occurrence, or assurance by fluent wording. |
| Contest or redress is claimed after a source is challenged. | State the disputed claim, affected use, accountable review role, allowed challenge evidence, possible disposition change, outcome record, and reopen trigger. | Claim truth, compliance proof, completed redress, or social-effect acceptance by appeal-channel presence. |
| A harmed party gives admissible challenge evidence, but the accountable party answers "evidence insufficient" without naming the missing evidence kind or decision point. | Treat the refusal as `RelianceDisposition=reopen` or invalid `RelianceDisposition=evidence-needed`; name the missing evidence kind, decision point, accountable role, and possible disposition change. | Closed refusal, completed redress, or `RelianceDisposition=no-supported-current-use` by vague insufficiency. |

#### A.10:4.7 - Causal evidence support basis in evidence paths

Evidence graph paths that support causal-use claims must carry the `C.28`-governed `CausalEvidenceSupportBasis` without redefining causal estimands or causal support authority.

The `C.28` values that `A.10` may carry in an evidence path are:

```text
observationalAssociationSupportBasis
interventionalActionSupportBasis
realizedCounterfactualSampleSupportBasis
identifiedCounterfactualEstimateSupportBasis
simulationOnlyCounterfactualOutputBasis
```

`A.10` consumes this value set from `C.28`; it does not add `causalAssumptionOnlySupport` or `noCausalEvidenceSupport` as evidence-basis values. Assumption-only and no-support postures are represented by causal assumptions, support verdict, supported use, unsupported use, or abstain in `C.28`/`B.3`, not by a second evidence-basis vocabulary.

No unsupported `CausalityLadderRung` climb:

```text
observational-association evidence -> interventional-action claim requires CausalIdentificationProfile.
interventional-action evidence -> counterfactual-comparison claim requires CausalIdentificationProfile for
  identifiedCounterfactualEstimateSupportBasis, CounterfactualSamplingRealizabilityProfile for
  realizedCounterfactualSampleSupportBasis, or bounded-use treatment.
Simulation-only counterfactual output may support bounded model-supported use when model assumptions, validation, supported use, and unsupported use are declared. It does not become interventional evidence or realized counterfactual sample evidence by vocabulary, validation, or evidence-role relabeling alone.
```

Evidence-path micro-examples:

| `CausalEvidenceSupportBasis` | EPV-style path cue |
| --- | --- |
| `observationalAssociationSupportBasis` | observed cohort table -> `PathSlice` to measurement work -> association-use support statement; unsupported use = intervention-effect wording. |
| `interventionalActionSupportBasis` | randomized or governed action assignment record -> work trace -> declared intervention-effect support inside assignment, follow-up, and outcome window. |
| `realizedCounterfactualSampleSupportBasis` | counterfactual-comparison sampling work plan -> run trace -> evidence carrier -> samples from declared target counterfactual distribution under physical, ethical, and operational constraints. |
| `identifiedCounterfactualEstimateSupportBasis` | causal assumptions, graph proof, calculus proof, available-data regime set, and bound refs -> `CausalIdentificationProfile` -> estimated or bounded counterfactual use with supported use and unsupported use. |
| `simulationOnlyCounterfactualOutputBasis` | simulator output -> counterfactual model assumptions -> simulation validation ref -> bounded model-supported use; validation remains validation and does not convert the path into direct sample evidence or intervention-effect evidence. |

What changes in practice: an evidence path can show that a carrier supports a causal-use claim, but it must also show the causal evidence support basis and the relevant `C.28` support references when the claim climbs from observation to intervention or from intervention to counterfactual comparison.

What this does not authorize: `A.10` does not identify causal effects, create an estimand, certify target-trial emulation, or decide counterfactual sampling realizability; it stores and makes recoverable the evidence graph path and causal support-basis refs needed by `C.28` and `B.3`.

### A.10:5 - Archetypal Grounding

| Aspect | `s.System` — Autonomous Brake | `s.Episteme` — Meta-analysis |
| --- | --- | --- |
| **Claim**                    | “Stop within 50 m from 100 km/h.”                                                                   | “Drug A outperforms control on endpoint E.”                                                                              |
| **Anchor**                   | `verifiedBy`: static‑analysis proof of no overflow; `validatedBy`: instrumented track tests.        | `verifiedBy`: power‑analysis proof of sample size; `validatedBy`: pooled effect sizes with bias checks.                  |
| **Carriers (SCR/RSCR)**      | Scale logs, calibration certificates, test track telemetry; SCR lists all; RSCR adds context units. | PDFs of studies, data tables, analysis code; SCR lists carriers; RSCR adapts vocabularies/units for the target audience. |
| **External TransformerRole** | Independent test team / metrology lab.                                                              | Independent synthesis team / statistician.                                                                               |
| **Temporal**                 | Dated runs; `happenedBefore` between setup → test → teardown.                                       | Publication dates; dataset versions; monotone coverage of included studies.                                              |

### A.10:6 - Conformance Checklist

| ID                                      | Requirement                                                                                                                                                                                                                             | Purpose (what it prevents)                                 |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **CC‑A10.1 (EPV‑DAG Presence)**         | Every published claim MUST have a path in the Evidence–Provenance DAG (EPV‑DAG) to concrete **SymbolCarrier** nodes and to the **external** `TransformerRole` that produced or interpreted the evidence.                                | Stops “weightless claims” and self‑justifying text.        |
| **CC‑A10.2 (SCR)**                      | Any `Γ_epist^synth` operation SHALL output an **SCR** listing all symbol carriers substantively used in the aggregate `s.Episteme`.                                                                                                        | Prevents source loss during aggregation.                   |
| **CC‑A10.3 (RSCR)**                     | Any `Γ_epist^compile` operation SHALL output an **RSCR** adapted to the target bounded context (vocabularies, units) with publication‑grade identifiers/hashes; SCR→RSCR MUST preserve carrier identity/integrity.                      | Keeps releases auditable and context‑consistent.           |
| **CC‑A10.4 (Resolution)**               | Every provenance/evidence node in the dependency graph MUST be resolvable to an SCR/RSCR entry. Unresolved links invalidate the claim.                                                                                                  | Eliminates dangling references and unverifiable citations. |
| **CC‑A10.5 (Scope Separation)**         | A single EPV‑DAG instance SHALL NOT mix design‑time MethodDescription nodes with run‑time Work traces. Bridges (“this run trace instantiates that spec”) MUST be explicit.                                                                     | Avoids conflating intent and execution.                    |
| **CC‑A10.6 (Externality)**              | The evidencing `TransformerRole` MUST be **external** to the holon under evaluation (A.12). Reflexive cases require modelling a meta‑holon and an external mirror.                                                                      | Prevents self‑creation/self‑evidence paradoxes.            |
| **CC‑A10.7 (Temporal Coverage)**        | For `Γ\_time` claims, interval coverage MUST be monotone and fully specified; gaps/overlaps require explicit justification or rejection.                                                                                                 | Stops invalid time‑series aggregation.                     |
| **CC‑A10.8 (Integrity & Immutability)** | SCR/RSCR entries MUST include version/date and checksums; published SCR/RSCR are immutable—updates create a new revision id with a pointer to the prior one.                                                                            | Guards against silent drift and tampering.                 |
| **CC‑A10.9 (Holarchy Firewall)**        | EPV‑DAG MUST use provenance edges only; mereological edges (`ComponentOf`, `MemberOf`, `PortionOf`, `PhaseOf`, etc.) MUST NOT appear in EPV‑DAG; conversely, provenance edges MUST NOT be used to build holarchies.                     | Keeps part‑whole and evidence semantics disjoint.          |
| **CC‑A10.10 (Γ\_sys Anchors)**          | Physical claims aggregated by `Γ_sys` MUST reference measurement models (quantity, unit, uncertainty), boundary conditions, and calibration carriers.                                                                                   | Ensures physical plausibility and comparability.           |
| **CC‑A10.11 (Γ\_method Anchors)**       | For order‑sensitive composition, design‑time MUST include a **Method Instantiation Card (MIC)** (Precedes/Choice/Join, guards, exceptions); run‑time traces MUST record `happenedBefore` and reference the MethodDescription they instantiate. | Preserves order semantics and reproducibility.             |
| **CC‑A10.12 (Γ\_work Anchors)**         | Resource spending/yield claims MUST be evidenced by instrumented carriers (meters, logs) and their MethodDescriptions; resource **rosters** MUST NOT be conflated with SCR/RSCR.                                                               | Distinguishes cost accounting from knowledge carriers.     |
| **CC-A10.13 (Causal support-basis path)** | If an evidence path supports a causal-use claim, it **MUST** carry `CausalEvidenceSupportBasis` from `C.28` and any relevant `CausalIdentificationProfile`, `CounterfactualSamplingRealizabilityProfile`, or `CausalUseEvidenceDesignRecord` refs; A.10 **MUST NOT** identify causal effects or mint a second support-basis value set. | Keeps evidence graph support recoverable without moving causal authority out of `C.28`. |
| **CC-A10.14 (Authority-reliance use of ordinary evidence paths)** | When a carrier is used to support approval, permission, gate passage, role or status currentness, work occurrence, provenance, authenticity, copied source support, generated source support, assurance input, or another authority-reliance claim or effect, the evidence path SHALL name the supported claim or effect, carrier, issuer, performer, source-maintenance role assignment or trust anchor, affected work target or claim target and relying context, time window, freshness or revocation stance, evidence-producing work event or method trace, evidence relation, and most relevant rival explanation. Expanded fields SHALL be named only when they decide the live reliance question: method trace or work trace, carrier integrity, identity or holder binding, verifier context, relying-party context, acceptance rule, proof result, cryptographic-signature result, status verification result, policy or gate version, decision source, source-chain transform notes, source order, supersession rule, and minimum disclosure posture. | Prevents badges, dashboards, copied text, generated explanations, credentials, provenance labels, and composed chains from supplying false evidence support, without turning source-finding into a full dossier. |
| **CC-A10.15 (Evidence-kind and reliance disposition)** | When a support-looking source is used for reliance, A.10 SHALL recover the evidence kind before stating support posture, then state the local `RelianceDisposition`, supported use, unsupported use, currentness/window, contest or redress path when live, and reopen trigger. `RelianceDisposition` SHALL NOT be read as `CV.Status`, `GateDecision`, selector outcome, problem-card state, assurance approval, or release permission. | Keeps evidence support action-guiding while preventing confidence, conformance, provenance, score, dashboard, generated explanation, or redress wording from becoming hidden authority. |

**Practitioner’s audit (non‑normative, quick):** For any claim, ask **What carriers? Which system? Which method? When?** If any answer is missing, A.10 is not satisfied.

### A.10:7 - Consequences

| Benefit                           | Why it matters                                                                  | Trade‑off / Mitigation                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Cross‑scale reproducibility**   | Any composite metric or argument can be walked back to its carriers and method. | **Overhead** of maintaining SCR/RSCR. *Mitigation:* keep entries minimal but complete; use checklists from the pedagogical companion. |
| **DesignRunTag clarity**            | Intent (MethodDescription) is cleanly separated from execution (Work traces).          | **Discipline** needed at boundaries. *Mitigation:* MIC templates; explicit “instantiates” bridges.                                    |
| **Objective evidence**            | External `TransformerRole` eliminates self‑evidence loops.                      | **Reflexive systems** require a mirror meta‑holon. *Mitigation:* provide a “reflexive modelling” appendix with examples.              |
| **Comparable numbers over time**  | Temporal coverage invariants prevent “trend” claims built on gaps.              | **Extra dating work** for legacy data. *Mitigation:* allow provisional labels until dating is completed.                              |
| **Safe composition of knowledge** | SCR/RSCR keep sources intact as Γ\_epist composes epistemes.                    | **Initial friction** in teams new to carrier thinking. *Mitigation:* start with “top‑10 carriers per claim” rule, expand as needed.   |
| **Feeds B.3 typed assurance claims** | Anchors provide evidence inputs such as `R` and `CL` only for a named typed assurance claim. | B.3 is not a generic trust or assurance score; cite the exact claim and relying context. |

### A.10:8 - Rationale (SoTA alignment, reader‑friendly)

* **Metrology & assurance.** The requirement to name quantities, units, uncertainty, calibration carriers reflects long‑standing metrology practice and modern assurance cases: numbers are only comparable when their **measurement models** are stated.
* **Knowledge provenance.** The EPV‑DAG and SCR/RSCR embody post‑2015 best practices in provenance for epistemes and their carriers: keep a complete, machine‑checkable trail from claims to carriers; separate provenance from part‑whole.
* **Temporal reasoning.** Monotone coverage (no unexplained gaps/overlaps) aligns with temporal knowledge graph practice and avoids “impossible histories.”
* **Holonic parsimony.** By drawing a firewall between **mereology** (A.14) and **provenance**, A.10 prevents semantic leakage and keeps the holarchy well‑typed.
* **Role–Method–Work clarity.** Anchoring explicitly rides on A.15: **roles** act via **methods** specified at design‑time and produce **work** observed at run‑time. This keeps agency, policy, and execution disentangled yet connected.
* **Credential, provenance, attestation, status-register, and generated-source currentness.** Verifiable-credential and digital-identity practice separates issuer or trust anchor, holder binding, proof result, status result, revocation, validity window, audience, and relying context. Some bounded contexts also treat a register entry or status-source entry as the source that creates or changes role assignment, status assertion, permission, duty, or gate state; a credential view, pass, badge, dashboard cell, API response, screenshot, or certificate excerpt is then a publication of that source, not automatically the source itself. C2PA content provenance plus SLSA and in-toto attestations separate bounded origin, history, build, and process claims from truth, approval, release, safety, gate passage, permission, or assurance; their consumer-side verifier or policy acceptance rule is part of the relying context, not implied by source-carrier presence. LLM citation and generated-explanation practice requires claim-bound attribution alignment before operative claims are relied on. A.10 adopts issuer, holder, verifier, status, and currentness recoverability, status-source recoverability, and claim-bound attribution as evidence-path invariants, adapts credential practice, provenance practice, attestation practice, model documentation, data documentation, register-backed status display, and generated-explanation practice as FPF source-role and carrier-support inputs, and rejects visual display, copied text, generated text, provenance mark, credential display, register excerpt, or attestation form as evidence of an operative action invitation, gate, role assignment, status assertion, work-occurrence, assurance, or admissible-work effect without exact source support.

Action result from that cited practice basis: provenance, attestation, credential, status-register, and generated-source practice rejects the shortcut that provenance means truth, safety, release, permission, or assurance. The local A.10 result is bounded origin, history, build, holder or status currentness, generated-claim source mapping, supported use, unsupported use, and reopen when the verifier, trust model, status or currentness rule, source mapping, or source-order relation changes.

### A.10:9 - Relations

* **Builds on:** A.1 Holonic Foundation; A.4 Temporal Duality; **A.12 Transformer Externalization**; **A.14 Advanced Mereology**; **A.15 Role–Method–Work Alignment**.
* **Constrains / used by:** B.1 (all Γ‑flavours: `Γ_sys`, `Γ_epist`, `Γ_method`, `Γ\_time`, `Γ_work`); B.1.1 (Dependency Graph & Proofs).
* **Enables:** **B.3 Trust Calculus** (R/CL inputs, auditability); B.4 Canonical Evolution Loop (clean DesignRunTag bridges).
* **Coordinates with:** `C.28` when an evidence path is used as causal-use support; A.10 carries the evidence/provenance path, while `C.28` governs causal-use question, support basis, identification, realizability, and supported use and unsupported use.
* **Coordinates with:** `A.15` for work or reliance disposition, `A.6` for mixed boundary wording, `B.3` for assurance, `A.21` for `OperationalGate(profile)`, `GateDecision`, and `DecisionLogRef`, `A.20` for `ConstraintValidity` status or witness, `A.2.9` for speech-act refs, `A.2.8` for commitments, and `A.15.1` for work occurrences. `A.10` supplies evidence paths for those sources; it does not create their gate decision, commitment, role effect, status effect, work-occurrence, assurance, admissible work effect, or admissible reliance effect.

### A.10:10 - Migration (practical and brief)

Apply these text edits:

1. **Terminology**

   * `manifest` → **“Symbol Carrier Register (SCR)”**; `release manifest` → **“Release SCR (RSCR)”**.
   * `creator` / `observer` (as internal evidencer) → **`TransformerRole (external)`**.
   * “symbol register” (ambiguous) → **“Symbol Carrier Register (SCR)”**.
   * Keep **resource rosters** in `Γ_work` separate from SCR/RSCR.

3. **Boilerplate inserts**

   * In **A.10** (this pattern): retain definitions of **EPV‑DAG**, **SCR/RSCR**, and the flavour‑specific anchors.
   * In **B.1.3 (`Γ_epist`)**: add the **Obligations — SCR/RSCR** block (“`Γ_epist^synth` SHALL output SCR… `Γ_epist^compile` SHALL output RSCR…”).
   * In **B.1.5 (`Γ_method`)**: ensure **MIC** is referenced (Precedes/Choice/Join, guards, exceptions) and run‑time traces reference the **MethodDescription** they instantiate.
   * In **B.1.6 (`Γ_work`)**: say “resource rosters are not SCR/RSCR; anchor meter/log readings via EPV‑DAG.”

### A.10:10a - Evidence carriers for quantum-like readings

Use A.10 when a quantum-like statement needs evidence rather than only a local modeling note. The practical question is not "is this quantum-like source impressive?" but "which carrier supports which minimal claim, under which time window and method?"

Action path:

1. State the minimal state, probe, export, or viability reading being supported.
2. Pin the concrete carriers: source, trace, dashboard export, report, observation, metric, work result, model output, interview, survey, or incident record.
3. State the evidence-producing role and method: who or what produced the carrier, by which method, probe, measurement, or work act.
4. State the time window, decay condition, and reopen condition.
5. State what the carrier does not show, including the most relevant rival explanation still live.
6. Choose the next pattern: stay in A.10 for carrier anchoring, apply `B.3` for assurance claims, apply `C.16` for measurement legality, apply `F.9` for bridge or export loss, or apply a `C.26.*` pattern for the remaining probe, state, or envelope question.

For probe-coupled, distributed-state, bridge-loss, measurement-frame, or viability-envelope readings, include at least:

| Field | Required content |
| --- | --- |
| Claim | The minimal state, probe, export, or viability reading being supported |
| Carrier | The concrete evidence carrier or carrier class |
| Evidence source or carrier kind | Source publication, witness statement, measurement result, report publication, trace record, dashboard display, work-result record, or human-statement carrier |
| Method / probe | The measurement, work act, survey, dashboard query, API read, workshop, model, or trace query that produced the carrier |
| Time window | When the evidence was produced and how long it remains fit for the intended inference |
| Confidence / limits | What the carrier does not show, and what rival explanation remains plausible |
| Reopen trigger | When decision, assurance, audit, work use, or reliance use requires additional evidence |

Useful outputs:

- a local evidence note when the claim only guides discussion;
- an EPV-DAG / SCR / RSCR entry when the claim enters a published assertion;
- a B.3 assurance tuple when the claim will support readiness, audit, release, compliance, or comparative assurance;
- a neighboring-pattern note when the carrier shows only ordinary measurement, bridge loss, or work enactment.

Do not let the label `quantum-like` carry evidence weight by itself. The evidence graph carries the claim; the math lens only explains what representational mistake the evidence is being used to avoid.

### A.10:10b - C.29 MLA relation

> If a mathematical lens needs evidence support, write the evidence path, source currentness, provenance, and any model-card or datasheet evidence use in `A.10`. A `C.29` output may state only `LensSupportPosture` for the mathematical-lens adequacy claim; it is not an evidence path, currentness proof, provenance record, or evidence-carrier substitute. Assurance or release confidence goes to `B.3`; measurement construction or comparability goes to `C.16`.

### A.10:End
