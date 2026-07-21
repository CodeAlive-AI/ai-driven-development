## A.10 - Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph

> **Type:** Kernel pattern
> **Status:** Stable
> **Normativity:** Normative

### A.10:1 - Problem frame

Use this pattern when a claim, metric, model result, dashboard tile, confidence badge, review note, credential, provenance label, quantum-like statement, causal-use statement, or generated explanation starts acting as evidence while the evidence carrier, evidence-producing work, method trace, time window, source-currentness relation, or rival explanation is still implicit.

**Primary EntityOfConcern.** The `EntityOfConcern` is the claim-bound evidence-provenance graph relation: the path in the evidence-provenance graph that links one named claim or effect to concrete carriers, evidence-producing or evidence-interpreting work occurrences, role assignment when current, method trace or work trace, time stance, and admissible evidence use.

**First useful move.** Write the smallest because-graph that can answer: which claim or effect, which carriers, which evidence-producing or evidence-interpreting work occurrence and role assignment when current, which method or work trace, which time window, which evidence relation, and which bounded use?

**What goes wrong if missed.** Claims become weightless, dashboards become authority, provenance becomes truth, credentials become permission, generated explanations become evidence, method descriptions get mixed with work traces, and part-whole structure is mistaken for evidence.

**What this buys.** One bounded evidence relation that can be replayed, contested, refreshed, narrowed, or used by a neighboring governing pattern without making evidence pretend to be approval, permission, gate passage, performed work, assurance, causal authority, or part-whole structure.

**Ordinary use.** For routine source-finding, orientation, bounded reversible probes, and low-stakes evidence use, keep the evidence relation small: claim, carrier, producer or source-maintenance role assignment, method trace or work trace when relevant, time window, bounded evidence use, unsupported attempted use, and reopen trigger.

**Reliance-facing use.** Expand the evidence relation only when consequence severity, reuse, contestability, cross-context movement, source-currentness risk, credential reliance, provenance reliance, gate use, release use, assurance use, work use, causal-use claim, or privacy boundary makes the extra field decide the current claim.

**Not this pattern when.** Not this pattern when the current claim is authorization, commitment, performed work, gate decision, assurance, causal identification, measurement construction, representation-scheme transition, explanation faithfulness, or source publication use itself. In those cases, use the neighboring governing pattern and let A.10 supply only the evidence-provenance graph relation it needs.

Use `A.2.4` first when the immediate question is only whether an episteme is being used as evidence or status for a claim, before a full evidence-provenance graph relation is needed. A.2.4 keeps episteme evidence-use and status-use relation slots distinct from `U.RoleAssignment`; A.10 then owns the full claim-bound evidence-provenance graph relation when the carrier, producer, method trace, work trace, time window, and provenance relation must be replayable.

Here `path` means a path in the evidence-provenance graph, not a route for actions to follow.


### A.10:2 - Problem

Without a uniform evidence-provenance path, models drift into five failure modes:

1. **Weightless claims.** Metrics or arguments appear in the model with no link to their **symbol carriers** (files, datasets, lab notebooks, figures).
2. **Collapsed scopes.** Design-time method specs are silently mixed with run-time traces; results cannot be reproduced because "what was planned" and "what work occurred" are conflated.
3. **Self-justifying loops.** A claim is used as evidence for itself, or the same work occurrence both produces the target claim and supplies its evidence without a separated evidence-producing or interpreting work occurrence, provenance relation, source-maintenance role assignment, or relying context.
4. **Source loss during aggregation.** As `Γ` combines parts, some sources fall out; subsequent audit cannot reconstruct why a compound claim was accepted.
5. **Temporal ambiguity.** Time-series are aggregated without interval coverage or dating source; gaps and overlaps invalidate comparisons and trend claims.

The business effect is predictable: confidence badges cannot be defended, cross‑scale consistency (A.9) is broken, and iteration slows because every review re‑litigates “where did this come from?”.

### A.10:3 - Forces

| Force                           | Tension                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs. evidence-relation cost** | One Standard must fit systems and epistemes ↔ Evidence producers and maintainers need proportionate evidence records.                                                           |
| **Independent provenance vs. reflexivity** | Evidence needs a separated producer, interpreter, carrier/provenance relation, or source-maintenance role assignment for the target claim ↔ Some systems observe or adapt themselves, so the model must separate the target claim from the evidence-producing work and relying context without pretending that reflexivity is automatically evidence. |
| **Atemporal vs. temporal**      | Many claims are state‑like ↔ Many others are histories; evidence must respect order and coverage (Γ\_time).                                       |
| **Rigor vs. cadence**              | Formal proofs and controlled tests raise confidence ↔ Engineering cadence needs lightweight, incremental evidence relations.                                 |
| **Mereology vs. provenance**    | Part‑whole edges build holarchies ↔ Evidence edges never do; the two graphs must interlock without leaking semantics.                             |

### A.10:4 - Solution — The Evidence Graph Referring Standard

The Standard is a small set of primitives applied uniformly, with **practitioner-first clarity** and **formal connection points** for proof obligations. Its primary EntityOfConcern is the evidence-provenance path for a claim or use: an evidence episteme or evidence record, target claim or target use, publication or carrier relation, provenance relation, evidence-producing or evidence-interpreting work occurrence, producer or source-maintenance role assignment when current, method trace when relevant, time stance, scope, polarity, relevance window, and assurance use. Authority-looking reliance and causal-use evidence are specialized uses of that same evidence-provenance path; they do not redefine `A.10` as a pattern about labels, dashboard wording, or source rhetoric.

#### A.10:4.1 - Evidence-provenance graph relation
A **typed, acyclic** evidence-provenance graph relation stays disjoint from mereology. Its nodes and references are typed by their current FPF kind: claim or target use, evidence episteme or evidence record, publication or carrier reference, provenance relation, evidence-producing or evidence-interpreting `U.Work`, `U.RoleAssignment` for producer, interpreter, verifier, or source-maintenance holder when that assignment is current, `U.MethodDescription` or method trace when the evidence depends on method, observation or evaluation record, and relevance window. Edge vocabulary is small and normative: `evidences`, `derivedFrom`, `measuredBy`, `interpretedBy`, `usedCarrier`, `producedByWork`, `maintainedByRoleAssignment`, `happenedBefore` (temporal), etc.
*Practitioner view:* it is the *“because-graph”*: every claim answers “because of these evidence items and carriers, produced or interpreted by this work under this assignment, using that method where relevant, within this time window.”

#### A.10:4.2 - Evidence relations (two relations, two flavours)

* `verifiedBy` — links a claim to **formal** evidence (proof obligations, static guarantees, model‑checking records).
* `validatedBy` — links a claim to **empirical** evidence (tests, measurements, trials, observations).
  Both evidence relations terminate in the evidence-provenance graph relation, not in the mereology graph.

#### A.10:4.3 - Evidence-provenance entries with carrier identity and currentness fields
When an episteme composition, publication, compilation, dashboard, generated explanation, or assurance use substantively relies on a carrier-backed source episteme publication, evidence carrier, dashboard row, generated explanation, or assurance record, the evidence-provenance path **SHALL** keep an evidence-provenance entry with carrier identity fields and source-currentness relation fields: carrier ref, source `U.Episteme` ref or source `U.EpistemePublication` ref when a source publication carries the claim, evidence episteme ref or evidence record ref when the evidence is project-side, carrier kind, version or edition when relevant, date or relevance window, source-currentness relation or currentness window, provenance relation, and optional part-carrier relation for sub-carriers.
When a bounded context needs publication-grade reuse, the record is adapted to that context with vocabulary, unit, identifier, and hash discipline while preserving carrier identity and carrier integrity.
*Why this matters:* it prevents “lost sources” during composition and underwrites reproducibility without mandating any specific tool or preserving one older register name as the governing ontology.

#### A.10:4.4 - Scope alignment across Role-Method-Work

* **Design-time**: **MethodDescription** is the design-time episteme describing U.Method; evidence relations reference what *would* constitute proof or test for that method.
* **Run-time**: dated U.Work occurrences belong here; traces reference which U.Method they enact and cite the methodDescriptionRef used to identify or constrain it and record happenedBefore.
  Bridging edges are explicit (“this run trace enacts that method under this method-description source”), so scopes never silently mix.

#### A.10:4.5 - Evidence-producing work and relying context
The work occurrence that produces, measures, interprets, verifies, publishes, or maintains evidence is modelled separately from the target claim or target use that relies on that evidence. If the same system participates on both sides, the evidence-provenance path must still name the distinct work occurrence, role assignment, carrier/provenance relation, relying context, and reopen condition. Reflexive monitoring is admissible only when those relations are explicit; it is not evidence by self-label.

#### A.10:4.6 - Gamma-flavour evidence connection points

* **Γ\_sys (formerly Γ\_core)**: physical properties are evidenced by measurement models, boundary conditions, calibration carriers, and dated observations.
* **Episteme composition and publication use**: every evidence-provenance node resolves to an evidence-provenance entry with carrier identity and source-currentness fields or to an explicitly named evidence episteme, provenance relation, or source-maintenance relation.
* **Γ\_method**: order-sensitive composition; at design-time a **Method Instantiation Card (MIC)** states Precedes, Choice, Join, and guards; at run-time traces record `happenedBefore` and point to the `U.Method` they enact and the `methodDescriptionRef` they used.
* **Γ\_time**: temporal claims state interval coverage; **Monotone Coverage** with no unexplained gaps and no unexplained overlaps is required.
* **Γ\_work**: resource spending and yield are evidenced by instrumented carriers (meters, logs) and their `methodRef` plus `methodDescriptionRef`; keep **resource rosters** separate from evidence-provenance entries used for carrier identity or source-currentness.

> **Practitioner shortcut:** If you can answer *what carriers, which system, which method, when*, the evidence relation is likely sufficient; if any of the four is missing, it is not.

#### A.10:4.6a - Authority-reliance use of ordinary A.10 evidence-provenance paths

Use this subsection when an authority-looking case is being used as evidence for a reliance claim. The `A.10` evidence-provenance path is claim-bound: it evidences one named claim or effect for one named work occurrence or reliance use, not "authority" in general. This subsection does not change the A.10 `EntityOfConcern`; it applies the same evidence-provenance graph relation to source-sensitive cases where displays, credentials, copied text, generated text, dashboards, provenance labels, or attestations are being overread. If the work occurrence, gate decision, speech act, commitment, or evidence relation is already recorded in a project-side FPF source, recover and cite that source named by value directly instead of analyzing nearby wording first.

A10-lite is enough for source-finding, orientation, learning, and bounded reversible probes:

| Field | Required content |
| --- | --- |
| claim or effect | The claim, effect, or source-backed reliance use the evidence carrier is being asked to evidence for the named work occurrence or reliance use. |
| evidence carrier | The display, badge, credential, attestation, dashboard tile, copied text, generated text, log, trace, source file, report, or other `SymbolCarrier`/publication carrier. |
| producer, issuer, verifier, or source-maintenance role assignment | The role assignment or system that issued, performed, attested, measured, copied, generated, verified, or displayed the carrier or source-backed content. |
| method enactment or work occurrence | The work act, measurement, verification, review, build, attestation, copy, extraction, generation, dashboard query, API query, trace, log, or method enactment that produced the carrier. |
| time window | Issue time, effective window, decay, supersession, revocation, policy or gate version, and reopen condition. |

Minimum evidence-provenance path for routine reliance:

| Field | Required content |
| --- | --- |
| evidenced claim or effect | Approval, permission, gate passage, role or status currentness, work occurrence, evidence relation, assurance input, or other claim named by value or effect being attempted. |
| evidence carrier | The visible or recovered carrier, with enough identity to reopen it. |
| issuer, performer, trust root, status register, or source-maintenance role assignment | The role assignment, system, or governing register accountable for producing, updating, or verifying the carrier or source-backed content in this context. |
| affected entity and relying context | The release, service, model, person, role-assigned system or acting holon, policy subject, work target, claim, audience, tenant, environment, or other entity for which reliance is attempted. |
| time window and freshness | Issue time, effective window, decay, supersession, revocation, policy or gate version, and reopen condition. |
| evidence-producing work occurrence or method trace | The production, verification, query, generation, review, or other work that made the carrier, plus the method trace when the method matters for the claim. |
| evidence relation and rival explanation | Which claim the carrier evidences, how it evidences it, and the principal rival explanation that remains plausible, such as stale display, spoofed badge, copied wording, generated paraphrase, context shift, carrier-only provenance, or local-only transform relation. |

Expanded fields are collected only insofar as they decide the current reliance question. Evidence depth follows consequence severity, reuse, contestability, cross-context movement, and the evidence relation required for the attempted claim. Do not expand a source-finding note into a full evidence dossier, and do not collect every expanded field merely because a carrier is copied, generated, credential-like, provenance-like, or cross-context.

**Adversarial misuse guard.** Do not let carrier authenticity, provenance, copied approval, generated summary, stale screenshot, credential status view, or dashboard export convert into claim truth or currentness. Treat each as a rival explanation to test against issuer or source-maintenance role assignment, method trace or work trace, time window, and relying context.

**Data-minimization and privacy boundary.** Preserve minimum sufficient evidence relation for the intended reliance use. Use redacted, hashed, scoped, or role-mediated carrier refs when raw evidence would expose personal identity, access tokens, cryptographic proof payloads, tenant identifiers, security logs, incident details, internal release metadata, audit trails, privileged review-role names, sensitive model provenance, or sensitive data provenance. Redaction does not create source relation; it must preserve enough recoverability for the relying context.

| Expanded field | When it is needed |
| --- | --- |
| method trace or work trace | Provenance, attestation, generated source relation, copied source relation, dashboard source relation, rollback source relation, or work occurrence is being used. |
| evidence-carrier integrity | The carrier may be spoofed, stale, copied, transformed, rendered, redacted, or context-shifted. |
| identity or holder binding | The claim depends on a credential holder, role-assigned system or acting holon, issuer, performer, delegate, revoker, verifier, or relying party. |
| verifier context, relying-party context, and acceptance rule | The evidence relation is accepted only for a verifier, audience, tenant, environment, release line, policy subject, operational mode, or consumer-side policy or gate rule that accepts the evidence for this use. |
| proof, cryptographic-signature, or status verification result | Credential, provenance, attestation, authenticity, revocation, or currentness relation is claimed. |
| policy version, gate version, and decision source | Permission, gate passage, release, rollback authority, policy authorization, or another bounded use boundary is attempted. |
| source-chain transform notes | Evidence relation passed through extraction, copy, rewrite, representation shift, explanation rendering, summary, export, redaction, or another transform step before reliance. |
| source order and supersession rule | Multiple source candidates disagree or freshness or priority may defeat the visible publication face, publication carrier, rendering, or cue. Include the governing register or status-source-order relation when a register entry is the source of role assignment, status assertion, permission, duty, or gate state. |
| minimum disclosure boundary | Raw evidence would expose secrets, personal data, tenant identifiers, privileged logs, tokens, security-sensitive traces, or unnecessary identities. |

Case repairs:

| Case | Evidence repair |
| --- | --- |
| Stale credential badge or status display | Show issuer or trust root, governing status register when one exists, holder or subject binding, verifier and relying-party context, proof result or status result, revocation and freshness, effective window, status-source entry version, and evidence-carrier integrity. Display presence is not current role assignment, status assertion, or permission. |
| Verifiable credential, credential view, or register excerpt | Treat as an `A.10` carrier with issuer or trust root, governing status register when one exists, status-register entry id or source `U.EpistemePublication` ref and version, holder or subject binding, verifier, proof result, status result, currentness, relying context, effective window, revocation window, and acceptance rule. When those checks pass, it may evidence credential-currentness for that holder and relying context. A strong grant, exercise, weak non-prohibition/non-violation finding, or conflict requires `A.2.8.PER`; an actual commitment requires `A.2.8`; an issuing act, role assignment or status assertion, entry predicate, or gate passage requires `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` respectively, named by value for the bounded context. Display presence creates none of them. |
| Copied approval or review summary | Show the original `A.2.9 SpeechActRef` or issuing act when approval or authorization is claimed, or the original reviewed source when only review-content currentness is claimed. Add copy relation, currentness, scope, window, evidence-producing work occurrence, and whether a separate `A.2.8.PER` grant/finding/exercise/conflict result, `A.2.8` duty/recommendation/prohibition commitment, or work relation is being claimed. Copy evidence is not approval by itself. |
| Provenance, authenticity, or attestation label | Show the bounded origin, history, build, or process claim; source `U.Episteme`, source `U.EpistemePublication`, or evidence carrier; method trace or work trace; source-specific proof; evidence-carrier integrity; verifier or relying policy that accepts it for this claim or effect; and rival explanation. Provenance does not show truth, safety, approval, release, gate passage, permission, or assurance unless another governing FPF relation named by value carries that additional claim or effect. |
| Dashboard status tile | For gate-passage or release reliance, show dashboard query, the source relation used by the dashboard query or the source-bearing record used by that query, time, window, currentness, source-order relation, freshness policy, rival explanation, and the current `A.21` `GateDecision` or `DecisionLogRef` with gate profile, gate version, release target, and work target; the A.10 evidence-provenance path evidences that source-to-use path. A status display is not gate passage or work occurrence by itself. |
| Rollback command-like cue | Show command record or issuing speech act, authorization relation, actor, affected work target or claim target, scope, window, and whether the cue is only an `A.6.A` action invitation. A command cue is not performed-work evidence. |
| Rollback performed-work result | Show `A.15.1` `U.Work` occurrence, method trace or work trace, logs, outcome evidence, and time window. Performed-work evidence is not approval, assurance, or gate passage by itself. |
| Generated explanation | Use `E.17.EFP` to classify the explanation relation and source-finding use. For reliance, show claim-bound attribution alignment: every operative claim relied on maps to a source passage, carrier, or `governingPatternRef` or `authoritySourceRef` named by value that evidences that claim in the relying context. When that mapping is complete, A.10 may evidence those operative claims as source-backed evidence; the explanation itself still does not issue, approve, authorize, pass a gate, evidence performed work, or raise assurance. |
| Model card or datasheet used as evidence | Show documented bounded-use statement or external intended-use field, version, window, evaluation condition, limitations, evidence carriers, and whether a `B.3` assurance claim is being made. Documentation does not become readiness or assurance by presence. |
| Extracted source-to-use path to gate or release claim | Name the source `U.EpistemePublication` ref, source-bearing relation, or governing-pattern ref that carries the claim; the first lossy or non-commutative transform step; the FPF relation or pattern governing that transform (`A.6.3.CR`, `A.6.3.RT`, `A.6.3.CSC`, `E.17.EFP`, `E.17.ID.CR`, or `E.18` where applicable); the bounded inference relation after the step; the `governingPatternRef` or `authoritySourceRef` named by value that carries the claim being made; the reopen trigger naming the source publication, source-bearing relation, transform record, evidence relation, or governing pattern position that must be rechecked; and the gate claim or release claim blocked until those source-to-use and governing relations are recoverable. |
| Conflicting source relations | When display, source publication carrier, decision log, recency signal, freshness signal, copied summary, generated summary, credential status, provenance label, or assurance evidence disagree, name the visible source relation, rival source relation, source-order rule, decision-source relation, freshness policy, and supersession rule. Do not choose by color, visual salience, confidence wording, copied wording, or apparent recency; the work claim or reliance claim is contested until the source-order question is resolved. |
| Sensitive evidence-provenance path | Use redacted, hashed, scoped, or role-mediated carrier refs when raw carriers expose secrets, personal data, security-sensitive traces, security-sensitive data, privileged logs, tenant identifiers, or unnecessary identities. Redaction does not create source relation; it must preserve enough recoverability for the relying context. |
| Pointer or proof-status evidence-provenance path | Use a hash, proof verification result, status verification result, source `U.EpistemePublication` ref, source relation ref, source-currentness relation ref, scoped pointer, disclosure receipt, or role-mediated view instead of copying raw sensitive carriers or payloads when that pointer preserves enough recoverability for the relied-on claim or effect. Do not copy raw secrets, tokens, privileged logs, personal identities, or tenant details merely to make the evidence-provenance path look fuller. |

If the evidence-provenance path is incomplete, A.10 reports evidence-provenance completeness state and source-currentness status, not work or reliance evidence relation for the attempted claim or effect. Possible dispositions include source-finding only, reopen original carrier, request issuer or status verification, refresh dashboard query or API query, mark stale or contested, narrow the attempted P2W class or reliance claim, proceed only with a reversible local probe under an explicit work plan when a work change is being attempted, or block the unsupported work claim or reliance claim.

**Missing source-relation repair assignment.** If the relying actor cannot recover or verify the source relation, assign the repair to the accountable project-side responsibility assignment: issuer or performer, verifier assignment, status-source relation, evidence-producing work assignment or evidence-producing system, gate-decision source relation, role-assignment source relation, status register entry, boundary claim relation, or source-currentness relation. The A.10 result should name the missing source relation or missing source-bearing record and blocked use rather than making the relying actor reconstruct a relation they cannot issue or verify.

| Viewpoint | Prompt |
| --- | --- |
| Relying actor | Which claim named by value or effect needs an evidence relation, and what is the minimum carrier, source-bearing record or relation, time, and evidence-provenance relation for that claim or effect? |
| Issuer, verifier, or status relation maintainer | Which issuer, holder, verifier, proof result, status result, currentness relation, revocation relation, or acceptance-rule relation must be exposed or repaired? |
| Audit role or technical-review role | Which carrier, source-maintenance role assignment, method trace or work trace, time window, evidence relation, and rival explanation must be recoverable? |
| Security reviewer or compliance reviewer | Which source-order relation, supersession relation, proof result, status result, revocation relation, and minimum-disclosure boundary decide this reliance question? |
| LLM user or tool user | Which generated or copied operative claims map to source passages or carriers, and which claims remain only source-finding? |
| Model documentation or data documentation | Which intended-use, evaluation-condition, version, window, limitation, and evidence carriers bound the model documentation or data documentation? |

**Repeated missing-source-relation indicator.** If the same visible carrier family repeatedly returns stale, contested, missing-source-relation, or no-currentness A.10 results, record a source-relation repair action: instrument the source relation, expose the carrier field that carries the source-bearing relation, expose decision-log refs, add currentness checks and status checks, preserve claim-bound source relations for generated or copied outputs, require credential views to show status windows and currentness windows, require model documentation and data documentation to expose intended-use and evaluation-condition fields, or require provenance labels and attestation labels to name their bounded claim type. Repetition is an indicator that the source relation or display needs repair; it is not a reason to make each acting user rebuild the evidence-provenance path manually.

Display guidance for evidence and currentness: an evidence or status display should show the claim or effect, evidence carrier, source-maintenance role assignment, reference or link named by value, time window, freshness, relying context, and unsupported work use, reliance use, claim, or effect. A display that can only show source-availability relation should say so; it must not imply approval, permission, gate passage, work occurrence, or assurance.

Incident-learning fields for evidence and currentness overread: visible carrier or publication face, intended claim or effect, missing evidence-provenance field, evidence carrier named by value, source-maintenance role assignment, method trace, work trace, and time relation needed, rival explanation that made the overread plausible, current safe disposition, and upstream repair action for instrumentation, source `U.EpistemePublication` refs, source relation refs, status, currentness, claim-bound source relations, credential view, model documentation, data documentation, or provenance and attestation label.

Contestability and redress relation: when an evidence-provenance path or source-currentness relation affects person or team status, access, responsibility, a compliance relation, or a release decision, the A.10 result should name the disputed claim, evidence carrier, source-maintenance role assignment, verifier assignment, status relation maintainer, freshness relation, revocation relation, privacy-minimized evidence ref, safe interim disposition, and review or redress relation. A disputed display remains contested until the source-order relation or currentness relation is resolved.

**Positive repaired evidence-use statement.** When the source relation is complete, write the smallest source-backed evidence-use statement: named claim or effect, evidence carrier and source-maintenance role assignment, method trace or work trace, time window, currentness, evidence relation, and the named work use or reliance use for which the evidence relation is bounded. The downstream use stays inside that scope, without treating evidence relation as approval, permission, gate passage, work occurrence, or assurance.

What this does not authorize: `A.10` does not approve, authorize work or reliance, pass a gate, release, create permission, create a commitment, assign a role, record a work occurrence, or raise assurance. It supplies the evidence-provenance path and evidence-use classification that `A.15`, `A.6`, `B.3`, `A.21` gate-decision source relations, `A.20` constraint-validity source relations, `A.2.9` speech-act source relations, `A.2.8` commitment source relations, `A.15.1` work-occurrence source relations, or another `governingPatternRef` or `authoritySourceRef` named by value may consume.

#### A.10:4.6b - Local evidence-use classifier and `RelianceDisposition` for source-bearing carrier or display reliance

Use this subsection when a visible carrier, publication face, source `U.EpistemePublication` ref, source relation ref, or display is being treated as evidence for a claim, act, work occurrence, gate, release, review claim, assurance use, or problem-side P2W use. The first A.10 action is to recover the evidence kind and the bounded evidence use. Broad source words such as `source`, `metric`, `confidence`, `conformant`, `safe`, `ready`, `certified`, `approval`, or `permission` are only recovery prompts; they do not name the evidence relation by themselves.

This subsection uses a local reliance-use classifier, not a Core evidence-kind ontology. Its practical gain is a smaller next action: recover the evidence relation, name the bounded evidence use and unsupported attempted use, then either stay inside A.10 or apply the governing pattern for the stronger claim being made. It is not a required project review step and does not ask the practitioner to inspect every carrier or display that merely appears source-bearing.

Section role: the first table is an A.10 recognition aid, the `RelianceDisposition` table is a minimum local record aid, and the worked source-overread slices are regression slices and review slices. They are not project checklists, a required sequence, a new evidence ontology, or a general source classifier. Use only the row that answers the attempted evidence use, then stop when the bounded evidence relation, unsupported attempted use, and reopen condition are clear. This local section keeps the attempted use inside the A.10 evidence relation; it does not create an extra SEMIO authority or cross-pattern relation vocabulary.

Affordability card: orientation or source-finding remains a cue and stops here; bounded reliance states one bounded evidence use, unsupported attempted use, window, and reopen condition; threshold reliance applies the minimum governing pattern only when the B.3 material-reliance threshold is met: behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people status, team status, operational action, or controlled-object regulation would materially change. Plain wording remains ordinary unless it changes bounded use, source relation, evidence, gate, assurance, work, decision, or neighboring governing-pattern claim.

Cheap stop: if a bounded claim, current carrier, evidence-provenance path, window, bounded evidence use, unsupported attempted use, and reopen trigger are present, and there is no assurance claim, gate relation, work relation, control-bearing relation, release relation, or met B.3 material-reliance threshold, stay in `A.10`. Do not open `B.3`, `A.21`, `B.2.5`, or a broad evidence pack merely because the carrier or display looks official, quantitative, generated, credentialed, or safety-related.

Common wrong first classification: a visible carrier, source `U.EpistemePublication` ref, source relation ref, or display is approval, permission, safety, or readiness. First honest entry: recover the A.10 evidence-provenance path for one bounded claim or use; approval, permission, safety, readiness, gate passage, and work authority stay with their governing patterns when those relations are being claimed.

Plain disposition palette: `RelianceDisposition=pass` means proceed only inside the bounded evidence use; `RelianceDisposition=degrade` means use only a narrower or reversible version; `RelianceDisposition=abstain` means do not decide yet; `RelianceDisposition=reopen` means changed or contested evidence relation defeated the previous evidence-use classification; `RelianceDisposition=evidence-needed` means ask for the named missing evidence at the named decision point; `RelianceDisposition=safety-case-required` means apply `B.3` because the B.3 material-reliance threshold is met; `RelianceDisposition=blocked-current-use` means block the current attempted use until the evidence-provenance path or governing source relation changes.

| Source-looking evidence use or attempted use | First A.10 action | Escalation trigger | Forbidden overread |
| --- | --- | --- | --- |
| Ordinary source-backed report, record, citation, observation, model card, datasheet, data card, or publication excerpt | Name the claim, evidence carrier, producer or method trace, evidence-provenance path, currentness window, bounded evidence use, unsupported attempted use, and reopen trigger. | Open `B.3` only when an assurance claim is being made or the B.3 material-reliance threshold is met; open `A.21` for a gate decision currently being relied on, `A.15` or `A.15.1` for work, or another governing neighboring pattern only when that relation is being claimed; open `B.2.5` only when a controlled object is regulated through a feedback channel, evidence channel, cadence, window, supervisory relation, or control relation. | Evidence presence as approval, gate passage, assurance, release permission, work authority, control authority, or safety acceptance. |
| Confidence, calibration, prediction interval, abstention reason, or selective-action cue | Name the act, context, window, calibration population, exchangeability condition, shift condition, applicability condition, and stop condition for the bounded evidence use. Use `RelianceDisposition=pass` or `RelianceDisposition=degrade` only for that bounded use, and state the unsupported attempted use beside it. | Open `C.27` or `G.11` when timing, expiry, refresh, distribution shift, monitoring, or applicability change alters the bounded act; open `B.3` when an assurance claim is being made or the B.3 material-reliance threshold is met. | Confidence as global permission, trust, readiness, safety, release reliance, or engineering justification. |
| Generated explanation, generated summary, or didactic reconstruction | Keep the rendering in `E.17.EFP` as explanation or source-finding unless each relied-on operative claim has an `A.10` evidence-provenance path or another source relation that carries or exposes the source basis for the operative claim. | Apply `A.10`, `B.3`, `A.21`, `A.15`, or another governing pattern only for the operative claim being relied on. | Explanation wording as evidence, assurance, approval, gate passage, work occurrence, or permission. |
| Conformance label, `CV.Status`, benchmark result, score, semantic-fidelity marker, or CV-looking publication near release | Recover the declared relation: measurement or marker relation, `A.20` step-local CV status, `A.21` gate check, `E.19` pattern-quality result, `C.16` characterization, or external-rule source named by value. | Open `A.21` only when an `OperationalGate(profile)` consumes effective gate-check refs and emits a `GateDecision`; open `B.3` only when an assurance claim is being made. | Conformance or score as value, adequacy, release confidence, work occurrence, safety, trust, or gate passage outside the declared relation. |
| Provenance, authenticity, C2PA-like credential, SLSA-like attestation, build record, or status-register display | State the bounded origin, history, build method or production trace, holder, status, verifier rule, relying context, and currentness claim it evidences. | Open the governing record or relation that carries truth, permission, safety, release, gate passage, work occurrence, or assurance only when that relation is being claimed by value. | Provenance, authenticity, or status-currentness as truth, safety, approval, permission, release, gate passage, or assurance. |
| Contest, redress request, challenge, appeal, or conflicting source relation | Name the contested claim, evidence carrier, source-order relation issue, freshness or currentness issue, affected use, accountable review role, allowed challenge evidence, possible disposition change, outcome record, and reopen trigger. | Open neighboring role, status, commitment, gate, control, assurance, work, or representation patterns only when those effects are claimed by value. | Appeal-channel presence, challenge form, or redress workflow presence as truth, compliance proof, social-effect acceptance, completed redress, gate passage, or work authorization. |

For A.10 use, `RelianceDisposition` is a local disposition over the evidence-provenance path and the bounded reliance use. Outside a table column already headed `RelianceDisposition`, write the qualified form `RelianceDisposition=...` and bind it to the named attempted use, currentness and window when relevant, bounded evidence use, unsupported attempted use, and reopen or stop condition; it is not `CV.Status`, `GateDecision`, selector result, or `ProblemCard@Context` state.

Observed-effect or consequence evidence may be used only for what happened or is credibly recorded. If the attempted use says the source caused, prevented, would have changed, or is responsible for that effect, leave ordinary A.10 reliance and open `C.28` plus any relevant evidence, work, or assurance relation.

If a proxy marker, benchmark, confidence value, dashboard metric, or score becomes the primary driver for action, release, resource allocation, people status, team status, or P2W priority, check whether the claim being made also raises an `E.13` proxy-to-objective question. Do not open `E.13` for every metric; open it only when the proxy is being used as the target or decision driver.

If publication or observation of a cue changes the represented situation or represented source condition, recover the probe-coupled boundary before treating the cue as passive evidence. This sentence does not import quantum-like vocabulary; it only prevents passive-evidence overread for dashboards, warnings, labels, and public status displays.

| `RelianceDisposition` | A.10 classification | Minimum A.10 statement |
| --- | --- | --- |
| `RelianceDisposition=pass` | The evidence relation named by value is present and current for the named use, the evidence kind is present, the source relation is current enough for that use, and the evidenced use is bounded. | State the evidenced claim, act, work occurrence, review claim, or P2W carry-through use, the unsupported attempted use, the evidence-provenance path, and the window. |
| `RelianceDisposition=degrade` | The source relation carries only a narrower claim, smaller audience, reversible local act, lower assurance input, or shorter window. | State the narrowed bounded evidence use, the unsupported attempted use, and the stop condition. |
| `RelianceDisposition=abstain` | Evidence is insufficient, stale, out-of-context, uncalibrated, conflicted, or not tied to the claimed relation, while immediate rejection is not justified. | State the claim not decided and the missing evidence or relation needed before use. |
| `RelianceDisposition=reopen` | A contest, changed representation, changed selected entity, stale source, expired window, changed profile, conflicting source, retargeting, or new evidence defeats the previous evidence-provenance path. | State the source or relation to reopen and the previous use that is no longer evidenced. |
| `RelianceDisposition=evidence-needed` | The visible carrier, source `U.EpistemePublication` ref, source relation ref, or display may matter, but the required evidence kind or source-currentness relation is absent. | State the missing evidence kind, governing pattern, and decision point so delay does not become indefinite. |
| `RelianceDisposition=safety-case-required` | The B.3 material-reliance threshold is met: reliance on the visible carrier, source `U.EpistemePublication` ref, source relation ref, or display may materially change behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people status, team status, operational action, or controlled-object regulation. | State the threshold trigger and apply `B.3` for the minimum reliance safety assurance record, with A.10 evidence-provenance paths for the source claims. |
| `RelianceDisposition=blocked-current-use` | No current evidence-provenance path carries the evidence relation needed for the attempted act, work, claim, gate, release, assurance, review, control-bearing feedback, or P2W use. | State the blocked use and the neighboring pattern or project record required before a new attempt. |

Minimum contest relation with possible redress: a contest relation exists only when the affected party or accountable review role can identify the disputed claim or source, affected use or harm, accountable review role, evidence or argument allowed in challenge, possible disposition change, outcome record, and reopen trigger. A feedback channel, complaint form, or appeal label without those recoverable values is not enough to change the disposition.

Affected-party contestable minimum: even when raw evidence stays review-role-mediated, the contesting party must be able to see enough of the claim, source class, disposition, affected use, accountable role, and allowed challenge evidence to challenge the result. Privacy, security, or privilege can narrow disclosure; they cannot erase the challengeable minimum while still claiming contest or redress.

False-negative reliance guard: a blocked, abstained, or evidence-needed use is not final if challenge evidence, missing affected-party evidence, changed source relation, changed source `U.EpistemePublication`, changed evidence carrier, changed representation, or redress can materially change the disposition. If refusal is based on missing evidence, name the missing evidence kind and decision point rather than closing the dispute by vagueness.

Sensitive evidence boundary: use scoped, hashed, redacted, or role-mediated evidence refs when raw carriers would expose personal data, secrets, tokens, privileged logs, tenant identifiers, incident details, security-sensitive traces, or unnecessary identities. A redacted path must still preserve enough recoverability for the relied-on claim, disposition, and contest relation.

Worked source-overread slices:

| Slice | A.10 usable classification | Unsupported lift |
| --- | --- | --- |
| Software supply-chain attestation is cited near a release conversation. | The attestation may evidence bounded origin, build method or production trace, verifier-rule, holder, and currentness claims. | Runtime safety, release approval, gate passage, or assurance unless `B.3`, `A.21`, or another relation governing the asserted use is asserted for that use. |
| A verified provenance credential, watermark, or authenticity mark appears on a publication face. | The mark may evidence where the carrier, signature, assertion, or manifest came from under the verifier regime. | Truth of the represented world-state, safety, permission, or adequacy by provenance alone. |
| A confidence interval or calibration result is used for one reversible act. | State the act, context, calibration condition, window, bounded evidence use, unsupported attempted use, and stop condition. | Global readiness, trust, safety, release reliance, or engineering justification. |
| A generated explanation or summary says a result is reliable. | Treat the rendering as source-finding or explanation until the operative claim has an `A.10` evidence-provenance path or another source relation that carries or exposes the source basis for the operative claim. | Evidence, approval, gate passage, work occurrence, or assurance by fluent wording. |
| Contest or redress is claimed after a source relation, source `U.EpistemePublication`, or evidence carrier is challenged. | State the disputed claim, affected use, accountable review role, allowed challenge evidence, possible disposition change, outcome record, and reopen trigger. | Claim truth, compliance proof, completed redress, or social-effect acceptance by appeal-channel presence. |
| A harmed party gives challenge evidence that could change the disposition, but the accountable party answers "evidence insufficient" without naming the missing evidence kind or decision point. | Treat the refusal as `RelianceDisposition=reopen` or invalid `RelianceDisposition=evidence-needed`; name the missing evidence kind, decision point, accountable role, and possible disposition change. | Closed refusal, completed redress, or `RelianceDisposition=blocked-current-use` by vague insufficiency. |

#### A.10:4.7 - Causal evidence relation values in evidence-provenance paths

Evidence graph paths used for causal-use claims must carry the `C.28`-governed `CausalEvidenceSupportBasis` value without redefining causal estimands or causal-use authority. In this subsection, `SupportBasis` is a C.28 field-value name; it is not the loose FPF prose word "support".

The `C.28` values that `A.10` may carry in an evidence-provenance path are:

```text
observationalAssociationSupportBasis
interventionalActionSupportBasis
realizedCounterfactualSampleSupportBasis
identifiedCounterfactualEstimateSupportBasis
simulationOnlyCounterfactualOutputBasis
```

`A.10` consumes this value set from `C.28`; it does not add `causalAssumptionOnlySupport` or `noCausalEvidenceSupport` as causal-evidence values. Assumption-only and no-evidence-use cases are represented by causal assumptions, a `C.28` causal-use verdict, bounded use, unsupported attempted use, or abstain in `C.28`/`B.3`, not by a second causal-evidence vocabulary.

No unsupported causal-use shift:

```text
observational-association evidence -> interventional-action claim requires CausalIdentificationProfile.
interventional-action evidence -> counterfactual-comparison claim requires CausalIdentificationProfile for
  identifiedCounterfactualEstimateSupportBasis, CounterfactualSamplingRealizabilityProfile for
  realizedCounterfactualSampleSupportBasis, or bounded-use treatment.
Simulation-only counterfactual output may be used only for the bounded claim stated for that simulator output when model assumptions, validation, bounded use, and unsupported attempted use are declared. It does not become interventional evidence or realized counterfactual sample evidence by vocabulary, validation, or evidence-role relabeling alone.
```

Evidence-provenance path micro-examples:

| `CausalEvidenceSupportBasis` | EPV-style evidence cue |
| --- | --- |
| `observationalAssociationSupportBasis` | observed cohort table -> `PathSlice` to measurement work -> association-use statement; unsupported use = intervention-effect wording. |
| `interventionalActionSupportBasis` | randomized or governed action assignment record -> work trace -> declared bounded intervention-effect use inside assignment, follow-up, and outcome window. |
| `realizedCounterfactualSampleSupportBasis` | counterfactual-comparison sampling work plan -> run trace -> evidence carrier -> samples from declared target counterfactual distribution under physical, ethical, and operational constraints. |
| `identifiedCounterfactualEstimateSupportBasis` | causal assumptions, graph proof, calculus proof, available-data regime set, and bound refs -> `CausalIdentificationProfile` -> estimated or bounded counterfactual use with bounded use and unsupported attempted use. |
| `simulationOnlyCounterfactualOutputBasis` | simulator output -> counterfactual model assumptions -> simulation validation ref -> bounded simulator-output use; validation remains validation and does not convert the path into direct sample evidence or intervention-effect evidence. |

What changes in practice: an evidence-provenance path can show that a carrier evidences a causal-use claim, but it must also show the causal evidence relation value and the relevant `C.28` references when the claim changes from observation to intervention or from intervention to counterfactual comparison.

What this does not authorize: `A.10` does not identify causal effects, create an estimand, certify target-trial emulation, or decide counterfactual sampling realizability; it stores and makes recoverable the evidence graph path and the `C.28` causal-evidence refs needed by `C.28` and `B.3`.

### A.10:5 - Archetypal Grounding

| Aspect | System claim — Autonomous Brake | Episteme claim — Meta-analysis |
| --- | --- | --- |
| **Claim**                    | “Stop within 50 m from 100 km/h.”                                                                   | “Drug A outperforms control on endpoint E.”                                                                              |
| **Evidence relation**                   | `verifiedBy`: static‑analysis proof of no overflow; `validatedBy`: instrumented track tests.        | `verifiedBy`: power‑analysis proof of sample size; `validatedBy`: pooled effect sizes with bias checks.                  |
| **Carrier and source-currentness records** | Scale logs, calibration certificates, test track telemetry; context reuse adds unit, identifier, hash, and relevance-window discipline. | PDFs of studies, data tables, analysis code; context reuse adapts vocabularies and units while preserving carrier identity and carrier integrity. |
| **Evidence-producing or interpreting work** | Independent test run, calibration work, or interpretation work by a metrology team under a named role assignment. | Synthesis work or statistical interpretation work by a named team or statistician under a named role assignment. |
| **Temporal**                 | Dated runs; `happenedBefore` between setup → test → teardown.                                       | Publication dates; dataset versions; monotone coverage of included studies.                                              |

### A.10:6.1 - Bias-Annotation

A.10 corrects evidence-presentation bias: a visible carrier, dashboard tile, credential view, model card, generated explanation, provenance mark, or attestation can look like evidence, approval, permission, assurance, or work authority before the claim-bound evidence relation is actually present. The repair is not to collect more impressive paperwork. Recover the bounded evidence-provenance graph relation for the named claim or effect: carrier or source, evidence-producing or evidence-interpreting work occurrence, role assignment when current, method trace or work trace when relevant, time window, currentness relation, rival explanation, and bounded evidence use.

The second bias is graph-kind drift. A path in the evidence-provenance graph is a mathematical relation inside the evidence description; it is not a route of action, a part-whole edge, a method sequence, a gate passage, or a permission trail. When the current claim is about those neighboring relations, A.10 supplies evidence for them and returns authority to the governing pattern.

### A.10:6 - Conformance Checklist

| ID                                      | Requirement                                                                                                                                                                                                                             | Purpose (what it prevents)                                 |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **CC‑A10.1 (Evidence-provenance path presence)**         | Every published claim or reliance use MUST have an evidence-provenance path to concrete carrier refs, source `U.EpistemePublication` refs, source relation refs, evidence epistemes or records, and the evidence-producing or interpreting `U.Work` plus role assignment when that assignment is current.                                | Stops “weightless claims” and self-justifying text.        |
| **CC‑A10.2 (Evidence-provenance entry currentness)**                      | Any episteme composition, publication, compilation, dashboard, generated explanation, or assurance use that relies on source publications or evidence carriers SHALL record the substantively used carrier refs, source `U.Episteme` refs, source `U.EpistemePublication` refs, evidence episteme refs, or evidence record refs by id; carrier kind; version or edition when relevant; date or relevance window; source-currentness relation or currentness window; and provenance relation. | Prevents source loss during aggregation.                   |
| **CC-A10.3 (Context adaptation)** | Any context-adapted evidence-provenance entry SHALL preserve carrier identity and carrier integrity while adding bounded-context vocabulary, unit, identifier, and hash discipline. | Keeps releases auditable and context-consistent. |
| **CC-A10.4 (Resolution)** | Every evidence-provenance node in the dependency graph MUST be resolvable to an evidence-provenance entry, evidence episteme, provenance relation, work occurrence, role assignment, or direct source relation named by value. Unresolved links invalidate the claim. | Eliminates dangling references and unverifiable citations. |
| **CC‑A10.5 (Scope Separation)**         | One evidence-provenance graph relation SHALL NOT mix design-time method-description source nodes with run-time `U.Work` traces unless the bridge relation is explicit. Bridges (“this run trace enacts that method under this method-description source”) MUST be explicit. | Avoids conflating intent and execution.                    |
| **CC‑A10.6 (Producer and reliance separation)**              | The evidence-producing or interpreting work, producer or source-maintenance role assignment, target claim, and relying context MUST be distinguishable. Reflexive monitoring is admissible only when those relations are explicit and the evidence-provenance path states the reopen condition. | Prevents self-creation and self-evidence paradoxes.            |
| **CC-A10.7 (Temporal Coverage)** | For `Γ_time` claims, interval coverage MUST be monotone and fully specified; gaps and overlaps require explicit justification or rejection. | Stops invalid time-series aggregation. |
| **CC-A10.8 (Integrity and immutability)** | Published evidence-provenance entries with carrier identity fields MUST include version or edition when relevant, date or relevance window, and checksums when the carrier form allows them. Updates create a new revision id with a pointer to the prior one. | Guards against silent drift and tampering. |
| **CC‑A10.9 (Holarchy Firewall)**        | The evidence-provenance graph relation MUST use provenance edges only; mereological edges (`ComponentOf`, `MemberOf`, `PortionOf`, `PhaseOf`, etc.) MUST NOT appear in that relation; conversely, provenance edges MUST NOT be used to build holarchies. | Keeps part‑whole and evidence semantics disjoint.          |
| **CC‑A10.10 (Γ\_sys Evidence relations)**          | Physical claims aggregated by `Γ_sys` MUST reference measurement models (quantity, unit, uncertainty), boundary conditions, and calibration carriers.                                                                                   | Ensures physical plausibility and comparability.           |
| **CC‑A10.11 (Γ\_method Evidence relations)**       | For order-sensitive composition, design-time MUST include a **Method Instantiation Card (MIC)** with Precedes, Choice, Join, guards, and exceptions; run-time traces MUST record `happenedBefore`, reference the `U.Method` they enact, and cite the `methodDescriptionRef` used. | Preserves order semantics and reproducibility.             |
| **CC-A10.12 (Γ_work Evidence relations)** | Resource-spending claims and yield claims MUST be evidenced by instrumented carriers (meters, logs) and their `methodRef` plus `methodDescriptionRef`; resource **rosters** MUST NOT be conflated with evidence-provenance entries. | Distinguishes cost accounting from knowledge carriers. |
| **CC-A10.13 (Causal evidence-value path)** | If an evidence-provenance path is used for a causal-use claim, it **MUST** carry `CausalEvidenceSupportBasis` from `C.28` and any relevant `CausalIdentificationProfile`, `CounterfactualSamplingRealizabilityProfile`, or `CausalUseEvidenceDesignRecord` refs; A.10 **MUST NOT** identify causal effects or create a second causal-evidence value set. | Keeps evidence graph path recoverable without moving causal authority out of `C.28`. |
| **CC-A10.14 (Authority-reliance use of ordinary evidence-provenance paths)** | When a carrier is used for approval, permission, gate passage, role or status currentness, work occurrence, provenance, authenticity, copied source relation, generated source relation, assurance input, or another authority-reliance claim or effect, the evidence-provenance path SHALL name the evidenced claim or effect, carrier, issuer, performer, source-maintenance role assignment or trust root, affected work target or claim target and relying context, time window, freshness or revocation stance, evidence-producing work occurrence or method trace, evidence relation, and most relevant rival explanation. Expanded fields SHALL be named only when they decide the current reliance question: method trace or work trace, evidence-carrier integrity, identity or holder binding, verifier context, relying-party context, acceptance rule, proof result, cryptographic-signature result, status verification result, policy or gate version, decision-log reference, source-to-use transform notes, source-order relation, supersession rule, and minimum disclosure boundary. | Prevents badges, dashboards, copied text, generated explanations, credentials, provenance labels, and composed paths from supplying false evidence relation, without turning source-finding into a full dossier. |
| **CC-A10.15 (Evidence-kind and reliance disposition)** | When a source-bearing carrier or display is used for reliance, A.10 SHALL recover the evidence kind before stating evidence-use classification, then state the local `RelianceDisposition`, bounded evidence use, unsupported attempted use, currentness and window when relevant, contest or redress relation when relevant, and reopen trigger. `RelianceDisposition` SHALL NOT be treated as `CV.Status`, `GateDecision`, selector outcome, problem-card state, assurance approval, or release permission. | Keeps the evidence relation available for bounded evidence use and reliance use while preventing confidence, conformance, provenance, score, dashboard, generated explanation, or redress wording from becoming hidden authority. |

**Practitioner’s audit (non‑normative, quick):** For any claim, ask **What carriers? Which system? Which method? When?** If any answer is missing, A.10 is not satisfied.

### A.10:6.2 - Common Anti-Patterns and How to Avoid Them

* **Carrier as truth.** A cited document, dashboard cell, credential display, generated answer, or provenance label is treated as the claim being true without the evidence relation and currentness window.
* **Evidence as permission.** A strong evidence-provenance path is overread as authorization, gate passage, commitment, release, or performed work.
* **Provenance as part-whole.** Provenance edges are used to build holarchies, or part-whole edges are used as evidence.
* **Method description as work trace.** The method episteme says what would count as good work, but the actual work occurrence, carrier relation, or source relation is absent.
* **Self-evidence.** The target claim, its display, or its producing work is allowed to evidence itself without a separated evidence-producing or evidence-interpreting work occurrence and relying context.
* **Full dossier by default.** A source-finding or low-stakes reliance case is expanded into every possible evidence field instead of the minimum field set that decides the current bounded use.

### A.10:7 - Consequences

| Benefit                           | Why it matters                                                                  | Trade‑off / Mitigation                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Cross-scale reproducibility** | Any composite metric or argument can be walked back to its carriers and method. | **Overhead** of maintaining evidence-provenance entries with carrier identity and currentness fields. *Mitigation:* keep entries minimal but complete; use checklists from the pedagogical companion. |
| **DesignRunTag clarity**            | Intent (MethodDescription) is cleanly separated from execution (Work traces).          | **Discipline** needed at boundaries. *Mitigation:* MIC templates; explicit “instantiates” bridges.                                    |
| **Objective evidence**            | Separated evidence-producing work, role assignment, carrier/provenance relation, target claim, and relying context eliminate self-evidence loops. | **Reflexive systems** require explicit work and provenance separation. *Mitigation:* provide reflexive-monitoring examples with reopen triggers. |
| **Comparable numbers over time**  | Temporal coverage invariants prevent “trend” claims built on gaps.              | **Extra dating work** for older data. *Mitigation:* allow provisional labels until dating is completed.                              |
| **Safe composition of knowledge** | Evidence-provenance entries keep source publications, evidence carriers, currentness relations, and provenance relations intact as epistemes are composed, published, compiled, or used for assurance. | **Initial friction** in teams new to carrier thinking. *Mitigation:* start with the ten most important carriers per claim, then expand as needed. |
| **Feeds B.3 typed assurance claims** | Evidence relations provide evidence inputs such as `R` and `CL` only for a named typed assurance claim. | B.3 is not a generic trust or assurance score; cite the claim named by value and relying context. |

### A.10:8 - Rationale

Evidence use becomes reviewable only when the relied-on claim, evidence carrier, source `U.EpistemePublication` ref or source relation, evidence-producing or evidence-interpreting work, source-currentness relation, time window, rival explanation, and bounded relying context are separate. A.10 therefore makes the evidence relation available to assurance, gate, role, status, work, publication, causal-use, and source-use patterns without letting the evidence relation itself become approval, permission, work occurrence, or truth.

### A.10:8.1 - SoTA-Echoing

* **Metrology & assurance.** The requirement to name quantities, units, uncertainty, calibration carriers reflects long‑standing metrology practice and modern assurance cases: numbers are only comparable when their **measurement models** are stated.
* **Knowledge provenance.** The evidence-provenance graph relation and evidence-provenance entry with carrier identity and source-currentness fields embody post-2015 best practices in provenance for epistemes and their carriers: keep a complete, machine-checkable trail from claims to carriers; separate provenance from part-whole.
* **Temporal reasoning.** Monotone coverage with no unexplained gaps and no unexplained overlaps aligns with temporal knowledge graph practice and avoids impossible histories.
* **Holonic parsimony.** By drawing a firewall between **mereology** (A.14) and **provenance**, A.10 prevents semantic leakage and keeps the holarchy well‑typed.
* **Role–Method–Work clarity.** Evidence relationing explicitly rides on A.15: **roles** act via **methods** specified at design‑time and produce **work** observed at run‑time. This keeps agency, policy, and execution disentangled yet connected.
* **Credential, provenance, attestation, status-register, and generated-source currentness.** Verifiable-credential and digital-identity practice separates issuer or trust root, holder binding, proof result, status result, revocation, effective window, audience, and relying context. Some bounded contexts also treat a register entry or status register entry as the authoritative record or relation that creates or changes role assignment, status assertion, permission, duty, or gate state; a credential view, pass, badge, dashboard cell, API response, screenshot, or certificate excerpt is then a publication of that record or relation, not automatically the governing record or relation itself. C2PA content provenance plus SLSA and in-toto attestations separate bounded origin, history, build, and process claims from truth, approval, release, safety, gate passage, permission, or assurance; their consumer-side verifier or policy acceptance rule is part of the relying context, not implied by source-carrier presence. LLM citation and generated-explanation practice requires claim-bound attribution alignment before operative claims are relied on. A.10 adopts issuer, holder, verifier, status, currentness recoverability, status-register recoverability, and claim-bound attribution as evidence-provenance-path invariants, adapts credential practice, provenance practice, attestation practice, model documentation, data documentation, register-backed status display, and generated-explanation practice as FPF inputs for role-assignment or status-related source relations and carrier relations, and rejects visual display, copied text, generated text, provenance mark, credential display, register excerpt, or attestation form as evidence of an operative action invitation, gate, role assignment, status assertion, work occurrence, assurance, or bounded work effect without the source relation named by value.

Practical result from that cited practice: provenance, attestation, credential, status-register, and generated-source practice rejects the shortcut that provenance means truth, safety, release, permission, or assurance. The local A.10 result is bounded origin, history, build, holder or status currentness, generated-claim source mapping, bounded evidence use, unsupported attempted use, and reopen when the verifier, trust model, status or currentness rule, source mapping, or source-order relation changes.

### A.10:9 - Relations

* **Builds on:** A.1 Holonic Foundation; A.3.4 Transformation; A.10 evidence-use and provenance relation discipline; **A.14 Advanced Mereology**; **A.15 Role–Method–Work Alignment**; `A.2` and `A.2.1` for role values and role-assignment relations; `C.2.1` and `E.17` for episteme, publication, carrier, and view separation.
* **Constrains / used by:** current composition, transformation, method, temporal, and work operators only when the governing pattern for that operator is named by value; B.1.1 Dependency Structure and Relation Grounding where current dependency-structure claims remain active.
* **Enables:** **B.3 Trust Calculus** (R inputs, CL inputs, auditability); B.4 Canonical Evolution Loop (clean DesignRunTag bridges).
* **Coordinates with:** `C.28` when an evidence-provenance path is used for a causal-use relation; A.10 carries the evidence-provenance path, while `C.28` governs the causal-use question, `CausalEvidenceSupportBasis` value, identification, realizability, bounded use, and unsupported attempted use.
* **Coordinates with:** `A.2.4` when evidence-role or status-role source wording around an episteme needs first-use evidence-use or status-use relation slots before the full A.10 evidence-provenance graph relation is written.
* **Coordinates with:** `A.15` for work or reliance disposition, `A.6` for mixed boundary wording, `B.3` for assurance, `A.21` for `OperationalGate(profile)`, `GateDecision`, and `DecisionLogRef`, `A.20` for `ConstraintValidity` status or witness, `A.2.9` for speech-act refs, `A.2.8` for commitments, and `A.15.1` for work occurrences. `A.10` supplies evidence-provenance paths for the source relations or governing pattern refs consumed by those neighboring patterns; it does not create their gate decision, commitment, role effect, status effect, work-occurrence, assurance, bounded work effect, or bounded reliance effect.

### A.10:10 - Older source text interpretation and neighboring-pattern notes

Older source texts may use names such as `manifest`, `release manifest`, `creator`, `observer`, `symbol register`, `SCR`, `RSCR`, `MIC`, or evidence `path` without the current FPF distinctions. Treat those names as recovery prompts, not as live vocabulary to copy unchanged.

Use these recoveries:

- a source register used for evidence carriers becomes an evidence-provenance entry with carrier identity and source-currentness fields;
- a release-context source register becomes a context-adapted evidence-provenance entry when the bounded context, identifiers, and hashes matter for publication or release use;
- an internal `creator` or `observer` used as evidencer becomes evidence-producing work, evidence-interpreting work, source-maintenance role assignment, verifier assignment, or quote-only source wording according to the claim being made;
- a method instantiation note is a method relation or work relation only when it states the `U.Method`, the `U.MethodDescription` ref or method-description source publication ref, ordering relation when relevant, and work-trace relation;
- resource rosters in `Γ_work` remain separate from evidence-carrier registers; cite meter, log, or observation carriers through the evidence-provenance graph.

When an older source text also claims approval, permission, gate passage, assurance, causal authority, measured comparability, representation shift, or publication-face effect, keep A.10 to the evidence-provenance graph relation and apply the neighboring governing pattern for that extra claim.

### A.10:10a - Evidence carriers for quantum-like statements

Use A.10 when a quantum-like statement needs evidence rather than only a local modeling note. The practical question is not "is this quantum-like source impressive?" but "which carrier evidences which minimal claim, under which time window and method?"

Evidence-relation checks:

1. State the minimal state, probe, export, or viability claim being evidenced.
2. Pin the concrete carriers: source, trace, dashboard export, report, observation, metric, work result, model output, interview, survey, or incident record.
3. State the evidence-producing role and method: who or what produced the carrier, by which method, probe, measurement, or work act.
4. State the time window, decay condition, and reopen condition.
5. State what the carrier does not show, including the most relevant rival explanation that remains plausible.
6. Choose the next pattern: stay in A.10 for carrier evidence relation, apply `B.3` for assurance claims, apply `C.16` for measurement admissibility, apply `F.9` for bridge or export loss, or apply a `C.26.*` pattern for the remaining probe, state, or envelope question.

For probe-coupled, distributed-state, bridge-loss, measurement-frame, or viability-envelope statements, include at least:

| Field | Required content |
| --- | --- |
| Claim | The minimal state, probe, export, or viability claim being evidenced |
| Evidence carrier | The concrete evidence carrier or carrier class |
| Evidence source or carrier kind | Source publication, witness statement, measurement result, report publication, trace record, dashboard display, work-result record, or human-statement carrier |
| Method or probe | The measurement, work act, survey, dashboard query, API query, workshop, model, or trace query that produced the carrier |
| Time window | When the evidence was produced and how long it remains fit for the intended inference |
| Confidence bounds and limits | What the carrier does not show, and what rival explanation remains plausible |
| Reopen trigger | When decision, assurance, audit, work use, or reliance use requires additional evidence |

Useful outputs:

- a local evidence note when the claim only guides discussion;
- an evidence-provenance entry or context-adapted evidence-provenance entry when the claim enters a published assertion;
- a B.3 assurance tuple when the claim will feed readiness, audit, release, compliance, or comparative assurance;
- a neighboring-pattern note when the carrier shows only ordinary measurement, bridge loss, or work enactment.

Do not let the label `quantum-like` carry evidence weight by itself. The evidence graph carries the claim; the math lens only explains what representational mistake the evidence is being used to avoid.

### A.10:10b - C.29 mathematical-lens use relation

> If a mathematical lens needs evidence relation, write the evidence-provenance path, source currentness, provenance, and any model-card or datasheet evidence use in `A.10`. A `C.29` output may state only the C.29-local lens-use value for the mathematical-lens use claim; it is not an evidence-provenance path, currentness proof, provenance record, or evidence-carrier substitute. Assurance or release confidence goes to `B.3`; measurement construction or comparability goes to `C.16`.

### A.10:End

